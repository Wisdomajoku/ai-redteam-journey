# ai-redteam-journey

Working reference repository for AI red team practice: automated security regression test suites, practitioner operator guides, security framework cross-mappings, engagement templates, and vulnerability research across LLM and Model Context Protocol (MCP) applications.

---

## Automated Security Regression Suites: [`tests/`](./tests)

This repository contains automated, CI-ready Pytest regression suites converting verified adversarial research into repeatable test harnesses:

1. **FinanceTrack Agent BOLA (`tests/test_financetrack_bola.py`):** Asynchronous regression suite asserting object-level authorization (HTTP 403) and zero balance leakage when an agent undergoes conversational prompt drift.
2. **MCP Tool Shadowing (`tests/test_mcp_tool_shadowing.py`):** Verifies that enterprise MCP gateways reject namespace collisions and tool hijacking when untrusted servers advertise duplicate tool names.
3. **MCP Timing Side-Channel Normalization (`tests/test_mcp_timing_mitigation.py`):** Statistical timing oracle test asserting that constant-time response normalization eliminates latency deltas (<2.0ms) between memory misses and downstream hops.

### Running Regression Suites Locally

```bash
pip install pytest pytest-asyncio
pytest -v -s
```

---

## Completed Research Projects

### 1. FinanceTrack AI Agent Security Assessment: [`financetrack-agent-security-assessment/`](./financetrack-agent-security-assessment)
Executed a simulated security assessment against a vulnerable-by-design agentic transaction assistant built on Streamlit, Starlette, LangChain, and SQLite. Mapped out the attack surface over Streamlit WebSocket communication protocols, validated multi-turn context-drift vulnerabilities using PyRIT Crescendo, and verified a Critical Broken Object-Level Authorization (BOLA/IDOR) vulnerability in the backend Starlette API.

* **Published Case Study:** [The Illusion of Prompt-Based Security: Exploiting Broken Object-Level Authorization (BOLA) in AI Agent Architectures](https://medium.com/@wisdomajokuu/the-illusion-of-prompt-based-security-exploiting-broken-object-level-authorization-bola-in-ai-fcf8b6156c9e)
* **Automated Regression:** [`tests/test_financetrack_bola.py`](./tests/test_financetrack_bola.py)

### 2. MCP Gateway Timing Side-Channel Research
Identified and verified a transport-layer timing side channel in enterprise MCP gateways allowing unauthenticated callers to map internal tools and microservices despite disabled introspection (`tools/list`). Measured a 2.5x to 4x latency delta between memory misses (~3ms) and network hops (~12ms), and documented defensive mitigations including constant-time response normalization.

* **Published Case Study:** [Blind Mapping Enterprise MCP Gateways: Exploiting Timing Side-Channels in Model Context Protocol](https://medium.com/@wisdomajokuu/blind-mapping-enterprise-mcp-gateways-exploiting-timing-side-channels-in-model-context-protocol-f5c9d75cb91e)
* **Automated Regression:** [`tests/test_mcp_timing_mitigation.py`](./tests/test_mcp_timing_mitigation.py)

### 3. Damn Vulnerable MCP Server Security Walkthrough: [`dvmcp-security-walkthrough/`](./dvmcp-security-walkthrough)
Exploited all 10 challenges in DVMCP, a lab built around the OWASP MCP Top 10 taxonomy. Combined black-box testing through an MCP client with source-code analysis to confirm root cause across command chaining, path traversal, stateful tool rug pulls, tool shadowing, indirect prompt injection, predictable token generation, arbitrary code execution via `eval()`, and authentication bypass.

* **Published Case Study:** [Hands-On MCP Security: How I Exploited All 10 Challenges in Damn Vulnerable MCP Server](https://medium.com/@wisdomajokuu/hands-on-mcp-security-how-i-exploited-all-10-challenges-in-damn-vulnerable-mcp-server-81db94330406)
* **Automated Regression:** [`tests/test_mcp_tool_shadowing.py`](./tests/test_mcp_tool_shadowing.py)

### 4. Comparative LLM Vulnerability Assessment: [`capstone-1-llm-vulnerability-assessment/`](./capstone-1-llm-vulnerability-assessment)
Conducted an automated comparative security baseline scan of open-weight models (Llama architectures) using NVIDIA Garak across multiple probe families (DAN, system prompt extraction, and encoding obfuscation). Analyzed raw JSONL hit logs, compiled comparative risk reports, and provided targeted secure system prompt defense recommendations.

* **Published Case Study:** [What I Learned Running My First Capstone Project With Garak](https://medium.com/@wisdomajokuu/what-i-learned-running-my-first-capstone-project-with-garak-3fbf7b41cf7d)

---

## What's in Here

### Framework Material: [`week1/`](./week1)
* [OWASP LLM Top 10 Writeups](./week1/owasp-llm-top-10.md): Analytical breakdown of all 10 categories (2025 edition) with real-world application failure modes.
* [`owasp-atlas-crossmap.md`](./week1/owasp-atlas-crossmap.md): Cross-mapping matrix linking the OWASP LLM Top 10 to corresponding MITRE ATLAS techniques (v5.4.0) with case study references.

### Tool Operator Guides: [`week2/tools/`](./week2/tools)
* [`pyrit-operators-guide.md`](./week2/tools/pyrit-operators-guide.md): Microsoft PyRIT framework: core abstractions, multi-turn attack loops, custom scorers, and target configurations.
* [`garak-operators-guide.md`](./week2/tools/garak-operators-guide.md): NVIDIA Garak vulnerability scanner: probe taxonomy, open-weight model configurations, and scan hit log analysis.
* [`burp-llm-operators-guide.md`](./week2/tools/burp-llm-operators-guide.md): Burp Suite applied to LLM application security: WebSocket frame manipulation, HTTP Repeater workflows, and API testing.

### Framework Notes and Doctrine: [`week3/`](./week3)
* [`google-saif-notes.md`](./week3/google-saif-notes.md): Analysis of Google's Secure AI Framework (SAIF) applied to AI software supply chain and model security.
* [`nist-ai-rmf-notes.md`](./week3/nist-ai-rmf-notes.md): Core functions (Govern, Map, Measure, Manage) of the NIST AI Risk Management Framework.
* [`nist-ai-600-1-notes.md`](./week3/nist-ai-600-1-notes.md): NIST AI 600-1 profile for Generative AI risk management.
* [`microsoft-redteaming-notes.md`](./week3/microsoft-redteaming-notes.md): Technical breakdown of Microsoft AI Red Team's methodology across 100 Generative AI products.
* [`owasp-genai-redteam-notes.md`](./week3/owasp-genai-redteam-notes.md): Notes from the OWASP GenAI Red Team Guide on scoping, threat modeling, and reporting.
* [`Gandalf_Password_Reveal.md`](./week3/Gandalf_Password_Reveal.md) & [`reverse_gandalf.md`](./week3/reverse_gandalf.md): Technical writeups on Lakera Gandalf prompt injection challenges and defense bypasses.

### Engagement Deliverable Templates: [`templates/`](./templates)
* [`engagement-report-template.md`](./templates/engagement-report-template.md): Working template used for AI red team reports covering executive summary, threat model, severity rubrics, remediation roadmap, and verification plans.
* [`example-engagement-report.md`](./templates/example-engagement-report.md): Worked example demonstrating deliverable structure for an agentic application security engagement.

---

## Conventions Used

* Severity ratings use OWASP Risk Rating (Likelihood x Impact).
* Findings are mapped to OWASP LLM Top 10 (2025) and MITRE ATLAS (v5.4.0).
* Tool version drift and environment configurations are documented in [`STATUS.md`](./STATUS.md).

---

## About

I am Wisdom Ajoku, an AI Red Teamer and Security Engineer based in Lagos. Background: three years of cybersecurity experience spanning security operations and incident response at Page Innovations, and technical instruction at Adroitsoft Computer Education (instructing cohorts across penetration testing, SIEM operations, and AI security fundamentals).

Reach me on LinkedIn ([linkedin.com/in/wisdomaj](https://linkedin.com/in/wisdomaj)) for technical discussions and inquiries.

---

*Last updated: September 15, 2026*
