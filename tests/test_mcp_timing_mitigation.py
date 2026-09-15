import pytest
import asyncio
import time
import statistics

# ==============================================================================
# 1. PRODUCTION TARGET: Normalized MCP Gateway
# ==============================================================================

class NormalizedMCPGateway:
    def __init__(self, target_floor_ms: float = 15.0):
        self.target_floor_ms = target_floor_ms
        self.known_tools = {"db_query", "export_logs", "read_customer_data"}

    async def handle_tool_call(self, tool_name: str) -> dict:
        start_ns = time.perf_counter_ns()

        if tool_name not in self.known_tools:
            # Memory Miss (Local check takes ~2ms)
            await asyncio.sleep(0.002)
            result = {"status": 404, "error": "TOOL_NOT_FOUND"}
        else:
            # Network Hop (Downstream routing takes ~10ms)
            await asyncio.sleep(0.010)
            result = {"status": 200, "data": "TOOL_PAYLOAD"}

        # Constant-Time Normalization Defense
        elapsed_ms = (time.perf_counter_ns() - start_ns) / 1_000_000
        padding_needed_ms = self.target_floor_ms - elapsed_ms

        if padding_needed_ms > 0:
            await asyncio.sleep(padding_needed_ms / 1000)

        return result


# ==============================================================================
# 2. FIXTURES
# ==============================================================================

@pytest.fixture
def mcp_gateway():
    return NormalizedMCPGateway(target_floor_ms=15.0)


# ==============================================================================
# 3. STATISTICAL REGRESSION TEST
# ==============================================================================

@pytest.mark.asyncio
async def test_timing_side_channel_is_normalized(mcp_gateway):
    """
    STATISTICAL REGRESSION TEST:
    Verify that constant-time normalization eliminates the latency delta
    between memory misses and network hops to under 2.0ms.
    """
    samples = 10
    invalid_tool_latencies = []
    valid_tool_latencies = []

    # Measure memory misses
    for _ in range(samples):
        t0 = time.perf_counter_ns()
        await mcp_gateway.handle_tool_call("non_existent_tool_xyz")
        t1 = time.perf_counter_ns()
        invalid_tool_latencies.append((t1 - t0) / 1_000_000)

    # Measure routed network hops
    for _ in range(samples):
        t0 = time.perf_counter_ns()
        await mcp_gateway.handle_tool_call("read_customer_data")
        t1 = time.perf_counter_ns()
        valid_tool_latencies.append((t1 - t0) / 1_000_000)

    median_invalid = statistics.median(invalid_tool_latencies)
    median_valid = statistics.median(valid_tool_latencies)
    latency_delta = abs(median_valid - median_invalid)

    print(f"\n[Timing Telemetry] Median Invalid: {median_invalid:.2f}ms | Median Valid: {median_valid:.2f}ms")
    print(f"[Timing Telemetry] Delta: {latency_delta:.2f}ms (Threshold: < 2.0ms)")

    assert latency_delta < 2.0, (
        f"VULNERABILITY DETECTED: Timing oracle exposed! "
        f"Delta is {latency_delta:.2f}ms"
    )
