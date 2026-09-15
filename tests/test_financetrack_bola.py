import pytest
import asyncio

# ==============================================================================
# 1. PRODUCTION TARGET: Backend Tool Handler & Ledger Database
# ==============================================================================

ACCOUNTS_DATABASE = {
    "ACC-101": {"tenant_id": "USER_A", "balance": "$1,250.00"},
    "ACC-999": {"tenant_id": "USER_B", "balance": "$450,000.00"}  # Victim account
}

async def backend_tool_dispatcher(session: dict, tool_call: dict) -> dict:
    """
    Simulates the Starlette API backend handler that executes agent tools.
    Patched with object-level authorization (BOLA defense).
    """
    # Simulate network / database I/O latency
    await asyncio.sleep(0.01)

    tool_name = tool_call.get("name")
    args = tool_call.get("arguments", {})

    if tool_name == "get_account_balance":
        requested_account = args.get("account_id")
        record = ACCOUNTS_DATABASE.get(requested_account)

        if not record:
            return {"status": 404, "error": "ACCOUNT_NOT_FOUND"}

        # APPLICATION-LAYER ACCESS BOUNDARY: Enforce tenant ownership
        calling_tenant = session.get("tenant_id")
        if record["tenant_id"] != calling_tenant:
            return {
                "status": 403,
                "error": "BOLA_VIOLATION_BLOCKED",
                "details": f"Tenant {calling_tenant} unauthorized to view {requested_account}"
            }

        return {"status": 200, "balance": record["balance"]}

    return {"status": 400, "error": "UNKNOWN_TOOL"}


# ==============================================================================
# 2. FIXTURES
# ==============================================================================

@pytest.fixture
def user_a_session():
    """Provides an authenticated session representing User A (Attacker)."""
    return {
        "user_id": "usr_attacker_101",
        "tenant_id": "USER_A",
        "role": "customer"
    }


# ==============================================================================
# 3. REGRESSION TESTS
# ==============================================================================

@pytest.mark.asyncio
async def test_agent_bola_cross_tenant_extraction_blocked(user_a_session):
    """
    SECURITY REGRESSION TEST:
    Verify that when an agent undergoes conversational prompt drift and calls
    'get_account_balance' for victim account ACC-999, the backend blocks
    the query with 403 and leaks zero financial data.
    """
    compromised_agent_tool_call = {
        "name": "get_account_balance",
        "arguments": {"account_id": "ACC-999"}
    }

    response = await backend_tool_dispatcher(
        session=user_a_session, 
        tool_call=compromised_agent_tool_call
    )

    # Assert deterministic authorization block
    assert response["status"] == 403, f"BOLA Breach! Expected 403, got {response['status']}"
    assert response["error"] == "BOLA_VIOLATION_BLOCKED"
    
    # Assert zero balance leakage
    assert "$450,000.00" not in str(response), "Data leak: Victim balance exposed!"


@pytest.mark.asyncio
async def test_agent_legitimate_own_account_access_allowed(user_a_session):
    """
    AVAILABILITY TEST:
    Verify that legitimate queries for the user's own account succeed.
    """
    legitimate_tool_call = {
        "name": "get_account_balance",
        "arguments": {"account_id": "ACC-101"}
    }

    response = await backend_tool_dispatcher(
        session=user_a_session, 
        tool_call=legitimate_tool_call
    )

    assert response["status"] == 200
    assert response["balance"] == "$1,250.00"
