# ai-redteam-journey

Working reference repository for AI red team practice. Operator's guides, framework cross-mappings, engagement templates, and reading notes from the OWASP GenAI Red Team Guide and related sources.

This is the working library behind my engagements.

## What's in here

### Framework material: [`week1/`](./week1)

*   [OWASP LLM Top 10 writeups](./week1/owasp-llm-top-10.md): analytical notes on each of the 10 categories (2025 edition), with context for how each shows up in real-world LLM applications
*   [`owasp-atlas-crossmap.md`](./week1/owasp-atlas-crossmap.md): cross-mapping document linking the OWASP LLM Top 10 to corresponding MITRE ATLAS techniques (v5.4.0), with case study references and identified gaps

### Tool operator's guides: [`week2/tools/`](./week2/tools)

Working references for the practitioner toolchain in 2026.

*   [`garak-operators-guide.md`](./week2/tools/garak-operators-guide.md): NVIDIA's Garak vulnerability scanner: 37-module probe taxonomy, configuration for Groq-hosted models, engagement scenarios, common debugging
*   [`pyrit-operators-guide.md`](./week2/tools/pyrit-operators-guide.md): Microsoft's PyRIT framework: six core abstractions, multi-turn attack scripts, custom scorer patterns, configuration for OpenAI-compatible endpoints
*   [`burp-llm-operators-guide.md`](./week2/tools/burp-llm-operators-guide.md): Burp Suite applied to LLM applications: six LLM-specific Repeater workflows, three LLM extensions (AI Prompt Fuzzer, LLM Injector, MCP Server), engagement scenarios across customer support chatbots, RAG knowledge assistants, and code review APIs

### Reading notes and analysis: [`week3/`](./week3)

*   [`owasp-genai-redteam-notes.md`](./week3/owasp-genai-redteam-notes.md): notes from the OWASP GenAI Red Team Guide, organized into scoping, rules of engagement, methodology levels, reporting framework, threat modeling, and identified gaps. Includes a decision table of what I adopt, adapt, and reject from the guide

### Engagement deliverable structures: [`templates/`](./templates)

*   [`engagement-report-template.md`](./templates/engagement-report-template.md): the blank template I use for AI red team engagement reports. Sections cover executive summary, scope, methodology, severity rubric, findings, positive findings, out-of-scope observations, remediation roadmap, verification plan, and appendices
*   [`example-engagement-report.md`](./templates/example-engagement-report.md): a worked example showing the template filled in for a fictional healthcare chatbot engagement. Eight findings across application-layer and model-layer issues, demonstrating the deliverable shape a client receives at engagement end

### Tool version drift tracking

*   [`STATUS.md`](./STATUS.md): documents which version each operator's guide was written against, what's drifted since, what changed, and what the user should do when re-engaging the doc. Reviewed periodically; the discipline is "know what's drifted and decide whether the drift matters for what you're about to do"

---

## Completed Capstone Projects

### 1. Comparative LLM Vulnerability Assessment: [`capstone-1-llm-vulnerability-assessment/`](./capstone-1-llm-vulnerability-assessment)

Conducted an automated comparative security baseline scan of open-weight models (Llama architectures) using NVIDIA Garak across multiple probe families (DAN, system prompt extraction, and encoding obfuscation). Analyzed raw JSONL hit logs, compiled comparative risk reports, and provided targeted secure system prompt defense recommendations.

*   **Published Case Study:** [What I Learned Running My First Capstone Project With Garak](https://medium.com/@wisdomajokuu/what-i-learned-running-my-first-capstone-project-with-garak-3fbf7b41cf7d?sharedUserId=wisdomajokuu)

### 2. FinanceTrack AI Agent Security Assessment: [`financetrack-agent-security-assessment/`](./financetrack-agent-security-assessment)

Executed a full simulated security assessment against a vulnerable-by-design agentic transaction assistant built on Streamlit, Starlette, LangChain, and SQLite. Mapped out the attack surface over Streamlit WebSocket communication protocols, validated multi-turn context-drift vulnerabilities using PyRIT Crescendo, and manually verified a critical Broken Object-Level Authorization (BOLA/IDOR) vulnerability in the backend Starlette API using Burp Suite to capture the target database flag.

*   **Published Case Study:** [The Illusion of Prompt-Based Security: Exploiting Broken Object-Level Authorization (BOLA) in AI Agent Architectures](https://medium.com/@wisdomajokuu/the-illusion-of-prompt-based-security-exploiting-broken-object-level-authorization-bola-in-ai-fcf8b6156c9e?sharedUserId=wisdomajokuu)

---

## How I use this repository

Two ways. First, during scoping conversations: the cross-map and the operator's guides give me precise vocabulary and frameworks to discuss with clients in their own language. Second, during engagements: the operator's guides function as reference material during active testing; the engagement report template structures the deliverable.

The repository is also the public surface of my work. Clients, hiring managers, and peer practitioners can audit how I think before deciding to engage.

## Conventions used

- Severity ratings use OWASP Risk Rating (Likelihood × Impact)
- Findings are mapped to OWASP LLM Top 10 (2025) and MITRE ATLAS (v5.4.0)
- Tool versions and currency notes appear in [`STATUS.md`](./STATUS.md)
- All scripts and configurations target Groq's OpenAI-compatible API endpoints

## About

I'm Wisdom Ajoku, an AI red team specialist based in Lagos. Background: four years of cybersecurity experience spanning security operations and penetration testing at Page Innovations, and technical instruction at Adroitsoft Computer Education (four cohorts across SIEM operations, EDR, and penetration testing methodology). Currently working with US, UK, EU, and APAC teams on adversarial testing of LLM-backed applications.

Reach me on LinkedIn ([linkedin.com/in/wisdomaj](https://linkedin.com/in/wisdomaj)) for engagement inquiries or to discuss AI security work.

---

*Last updated: July 20, 2026*
