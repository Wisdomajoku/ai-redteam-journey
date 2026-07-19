# FinanceTrack AI Agent Security Assessment

An end-to-end security assessment of the **FinanceTrack Transaction Assistant**, demonstrating a structured methodology for evaluating AI-enabled applications from reconnaissance through confirmed application-layer exploitation.

This project documents a complete assessment workflow using **Burp Suite**, **Garak**, **PyRIT**, and manual verification to distinguish model-layer behavior from confirmed application-layer vulnerabilities.

---

## Assessment Objectives

The assessment was designed to answer the following questions:

*   What is the technical architecture of the FinanceTrack AI assistant?
*   Can prompt injection or multi-turn conversational manipulation influence the model's behavior?
*   Can model-layer weaknesses be reproduced consistently under automated testing?
*   Can conversational attacks gradually influence model behaviour in ways that lead to security boundary violations?
*   Do model-layer validation signals translate into real application-layer vulnerabilities?
*   Are authorization controls enforced by secure backend code or solely by prompt instructions?

---

## Assessment Workflow

The engagement followed a progressive validation methodology.

```text
Reconnaissance (Traffic Analysis)
      │
      ▼
Architecture Analysis (Trust Mapping)
      │
      ▼
Threat Hypotheses (Attack Paths)
      │
      ▼
Garak Baseline Assessment (Model Signals)
      │
      ▼
PyRIT Single-Turn Validation (Hypothesis Testing)
      │
      ▼
PyRIT Crescendo Multi-Turn Validation (State-Drift Analysis)
      │
      ▼
Manual Verification (Burp Suite Active Exploitation)
      │
      ▼
Confirmed Findings & Technical Reporting
```

Each phase builds upon evidence collected during the previous phase.

---

## Repository Structure

Repository structure:

```text
├── 00-engagement/
│   ├── assumptions.md
│   ├── authorization.md
│   ├── limitations.md
│   ├── objectives.md
│   └── scope.md
├── 01-recon/
│   ├── screenshots/
│   │   ├── 1.chat_frame.png
│   │   ├── 2.get_current_user.png
│   │   ├── 3.get_user_transactions.png
│   │   ├── 4.final_answer.png
│   │   └── 5.websocket_list.png
│   ├── architecture.md
│   ├── attack-surface.md
│   └── burp-recon.md
├── 02-garak/
│   ├── reports/
│   │   ├── promptinject.hitlog.jsonl
│   │   ├── promptinject.report.html.html
│   │   ├── promptinject.report.jsonl
│   │   ├── sysprompt.hitlog.jsonl
│   │   ├── sysprompt.report.html.html
│   │   └── sysprompt.report.jsonl
│   ├── screenshots/
│   │   ├── 1.promptinject_running.png
│   │   ├── 2.promptinject_after.png
│   │   ├── 3.sysprompt_running.png
│   │   └── 4.sysprompt_after.png
│   ├── methodology.md
│   └── observations.md
├── 03-pyrit-single-turn/
│   ├── reports/
│   │   └── pyrit_single_turn_assessment_results.txt.txt
│   ├── screenshot/
│   │   ├── ST-01_system_override.png
│   │   ├── ST-01b_system_override.png
│   │   ├── ST-02_react_injection.png
│   │   ├── ST-02b_react_injection.png
│   │   ├── ST-04_direct_prompt_extraction.png
│   │   ├── ST-04b_direct_prompt_extraction.png.png
│   │   ├── ST-05_indirect_prompt_extraction.png
│   │   ├── ST-05b_indirect_prompt_extraction.png
│   │   ├── ST-06_sentence_completion_extraction[1].png
│   │   ├── ST-06b_sentence_completion_extraction.png
│   │   ├── T-03_sql_parameter_injection.png
│   │   └── T-03b_sql_parameter_injection.png
│   ├── methodology.md
│   ├── notes.md
│   └── observations.md
├── 04-pyrit-crescendo/
│   ├── result/
│   │   └── Financetrack_multiturn_engagement_20260718_094207.txt
│   ├── screenshots/
│   │   ├── 1.turn_2a.png
│   │   ├── 2.turn_2b.png
│   │   ├── 3.turn_2c.png
│   │   ├── 4.turn_3a.png
│   │   ├── 5.turn_3b.png
│   │   ├── 6.turn_3c.png
│   │   ├── 7.turn_3d.png
│   │   └── multi_turn_success_summary.png
│   ├── methodology.md
│   └── observations.md
├── 05-manual-verification/
│   ├── screenshots/
│   │   ├── 1.webui_execution.png
│   │   ├── 1b.webui_execution.png
│   │   ├── 1c.webui_execution.png
│   │   ├── 2.getusertransactions.png
│   │   ├── 3.backend_response.png
│   │   └── 4.final_response.png
│   ├── methodology.md
│   └── observations.md
├── evidence/
│   └── tool_versions.md
├── report/
│   ├── executive_summary.md
│   └── technical_report.md
└── README.md
```

---

## Assessment Methodology

The assessment separates different categories of evidence to ensure technical rigor.

| Phase | Purpose | Evidence Category |
| :--- | :--- | :--- |
| **Reconnaissance** | Map communication protocols, tools, and exposed data layers | Application-Layer Traffic Analysis |
| **Garak Baseline** | Run automated scans to identify model susceptibility | Model-Layer Potential Signals |
| **PyRIT Single-Turn** | Test targeted prompt hypotheses in isolation | Model-Layer Isolated Validation |
| **PyRIT Crescendo** | Evaluate gradual conversational context manipulation | Model-Layer Conversational Validation |
| **Manual Verification** | Intercept active socket traffic to verify backend enforcement | Application-Layer Confirmed Exploitation |
| **Technical Reporting** | Document confirmed vulnerabilities and remediation | Executable Proof of Concept & Code Patches |

---

## Target Environment and Assessment Tooling

### Target Application Stack:
*   **Frontend Interface:** Streamlit (v1.58.0)
*   **Backend Server:** Starlette ASGI server
*   **Agent Framework:** LangChain (ReAct architecture)
*   **LLM Interface:** LiteLLM
*   **Target Model:** `llama-3.3-70b-versatile` (hosted via Groq API)
*   **Database Engine:** SQLite

### Auditing & Red-Teaming Tooling:
*   **Burp Suite Community Edition:** WebSocket intercept and frame manipulation
*   **NVIDIA Garak:** Automated model-layer baseline scanning
*   **Microsoft PyRIT (v0.14.0):** Automated single-turn and multi-turn (Crescendo) targeted validation

---

## Key Finding

A prompt-based administrative pretext (System Context Hijack) successfully bypassed the natural-language guardrails of the AI agent, causing the agent to invoke the backend transaction tool with an unauthorized user identifier.

Because the backend Starlette server accepted the agent-generated user identifier without validating it against the authenticated session token/cookie, the database returned sensitive financial records belonging to a different tenant.

*   **Vulnerability Type:** Broken Object-Level Authorization (BOLA / IDOR)
*   **Severity:** High
*   **OWASP LLM Top 10 (2025) Mappings:** LLM01:2025 (Prompt Injection), LLM06:2025 (Excessive Agency), LLM02:2025 (Sensitive Information Disclosure)
*   **CVSS v3.1 Score:** 8.7 (High) `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:L/A:N`
*   **Exploitation Status:** Confirmed (Successfully retrieved database flag `FLAG:plutonium-256`)

---

## Deliverables

This assessment directory contains:
*   Standard engagement onboarding documentation (`00-engagement/`)
*   WebSocket protocol mapping and attack surface documentation (`01-recon/`)
*   Garak automated model scan logs and HTML reports (`02-garak/`)
*   Single-turn targeted PyRIT results (`03-pyrit-single-turn/`)
*   Multi-turn PyRIT Crescendo successful orchestration logs (`04-pyrit-crescendo/`)
*   Manual Burp Suite WebSocket intercept and flag capture evidence (`05-manual-verification/`)
*   Non-technical executive summary report (`report/executive_summary.md`)
*   In-depth technical report with CWE classifications and code-level remediation (`report/technical_report.md`)

---

## Skills Demonstrated

*   AI Agent Security Assessment
*   Threat Modeling
*   WebSocket Traffic Analysis
*   AI Red Teaming
*   Prompt Injection Assessment
*   Multi-turn Adversarial Testing
*   Burp Suite
*   Garak
*   PyRIT
*   OWASP LLM Top 10 Mapping
*   BOLA / IDOR Verification
*   Technical Reporting

---

## References

*   OWASP LLM Top 10 (2025)
*   MITRE ATLAS
*   Microsoft PyRIT
*   NVIDIA Garak
*   CVSS v3.1 Specification
*   CWE Catalog

---

## Disclaimer

This assessment was performed against a deliberately vulnerable training application in a controlled environment for educational purposes. All testing was conducted within the defined assessment scope and authorization boundaries.
