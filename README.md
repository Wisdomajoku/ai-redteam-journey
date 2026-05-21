# ai-redteam-journey

Working reference repository for AI red team practice. Operator's guides, framework cross-mappings, engagement templates, and reading notes from the OWASP GenAI Red Team Guide and related sources.

This is the working library behind my engagements.

## What's in here

### Framework material — [`week1/`](./week1)

- [OWASP LLM Top 10 writeups](./week1) — analytical notes on each of the 10 categories (2025 edition), with context for how each shows up in real-world LLM applications
- [`owasp-atlas-crossmap.md`](./week1/owasp-atlas-crossmap.md) — cross-mapping document linking the OWASP LLM Top 10 to corresponding MITRE ATLAS techniques (v5.4.0), with case study references and identified gaps

### Tool operator's guides — [`week2/tools/`](./week2/tools)

Working references for the practitioner toolchain in 2026.

- [`garak-operators-guide.md`](./week2/tools/garak-operators-guide.md) — NVIDIA's Garak vulnerability scanner: 37-module probe taxonomy, configuration for Groq-hosted models, engagement scenarios, common debugging
- [`pyrit-operators-guide.md`](./week2/tools/pyrit-operators-guide.md) — Microsoft's PyRIT framework: six core abstractions, multi-turn attack scripts, custom scorer patterns, configuration for OpenAI-compatible endpoints
- [`burp-llm-operators-guide.md`](./week2/tools/burp-llm-operators-guide.md) — Burp Suite applied to LLM applications: six LLM-specific Repeater workflows, three LLM extensions (AI Prompt Fuzzer, LLM Injector, MCP Server), engagement scenarios across customer support chatbots, RAG knowledge assistants, and code review APIs

### Reading notes and analysis — [`week3/`](./week3)

- [`owasp-genai-redteam-notes.md`](./week3/owasp-genai-redteam-notes.md) — notes from the OWASP GenAI Red Team Guide, organized into scoping, rules of engagement, methodology levels, reporting framework, threat modeling, and identified gaps. Includes a decision table of what I adopt, adapt, and reject from the guide

### Engagement deliverable structures — [`templates/`](./templates)

- [`engagement-report-template.md`](./templates/engagement-report-template.md) — the blank template I use for AI red team engagement reports. Sections cover executive summary, scope, methodology, severity rubric, findings, positive findings, out-of-scope observations, remediation roadmap, verification plan, and appendices
- [`example-engagement-report.md`](./templates/example-engagement-report.md) — a worked example showing the template filled in for a fictional healthcare chatbot engagement. Eight findings across application-layer and model-layer issues, demonstrating the deliverable shape a client receives at engagement end

### Tool version drift tracking

- [`STATUS.md`](./STATUS.md) — documents which version each operator's guide was written against, what's drifted since, what changed, and what the user should do when re-engaging the doc. Reviewed periodically; the discipline is "know what's drifted and decide whether the drift matters for what you're about to do"

## How I use this repository

Two ways. First, during scoping conversations: the cross-map and the operator's guides give me precise vocabulary and frameworks to discuss with clients in their own language. Second, during engagements: the operator's guides function as reference material during active testing; the engagement report template structures the deliverable.

The repository is also the public surface of my work. Clients, hiring managers, and peer practitioners can audit how I think before deciding to engage.

## Currently in progress

Two capstone projects scheduled for completion in early-to-mid June 2026:

1. **Comparative LLM vulnerability assessment** — Garak-based comparison of three architecturally diverse Groq-hosted models, with comparative analysis and defender recommendations
2. **End-to-end engagement simulation** — full simulated engagement against a target chatbot stack, using the complete Burp + Garak + PyRIT toolchain, producing a complete engagement report using the template in this repo

Also queued: a writeup on business logic vulnerabilities in AI applications (a gap identified in the OWASP GenAI Red Team Guide), and notes from Microsoft's Red Teaming 100 GenAI Products paper, Google SAIF, and selective NIST AI RMF reading.

## Conventions used

- Severity ratings use OWASP Risk Rating (Likelihood × Impact)
- Findings are mapped to OWASP LLM Top 10 (2025) and MITRE ATLAS (v5.4.0)
- Tool versions and currency notes appear in [`STATUS.md`](./STATUS.md)
- All scripts and configurations target Groq's OpenAI-compatible API endpoints

## About

I'm Wisdom Ajoku, an AI red team specialist based in Lagos. Background: three years of offensive security and SOC operations at Page Innovations, currently teaching cybersecurity at Adroitsoft (four cohorts across SIEM operations, EDR, and penetration testing methodology). Currently working with US, UK, EU, and APAC teams on adversarial testing of LLM-backed applications.

Reach me on LinkedIn ([linkedin.com/in/wisdomaj](https://linkedin.com/in/wisdomaj)) for engagement inquiries or to discuss AI security work.

---

*Last updated: May 21, 2026*
