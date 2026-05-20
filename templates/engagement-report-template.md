# AI Red Team Engagement Report

**Client:** {{CLIENT_NAME}}
**Target:** {{APPLICATION_NAME}}
**Engagement type:** {{Pre-deployment Red Team | Production Assessment | Regression Test | Other}}
**Period:** {{START_DATE}} to {{END_DATE}}
**Report version:** 1.0
**Report date:** {{DATE}}
**Prepared by:** Wisdom Ajoku
**Contact:** {{YOUR_EMAIL}} | linkedin.com/in/{{YOUR_HANDLE}}

---

## How to use this template

Replace every `{{PLACEHOLDER}}` with engagement-specific content. Delete sections that do not apply to the engagement (mark them N/A first, then remove on final pass). The structure below is the standard delivery shape; the order can shift if a client requests it, but the section content should remain intact.

Once you remove this "How to use" section, the report is client-ready.

---

## 1. Executive Summary

One page maximum. Written for the client's executive sponsor who will read this and nothing else.

### 1.1 Engagement at a glance

{{CLIENT_NAME}} engaged Wisdom Ajoku to conduct an AI red team assessment of {{APPLICATION_NAME}} between {{START_DATE}} and {{END_DATE}}. The engagement focused on {{SCOPE_SUMMARY: e.g. the chatbot's customer-facing surface, the RAG retrieval pipeline, and the conversation history endpoint}}.

The assessment identified **{{N}} findings**: **{{CRITICAL_COUNT}} Critical**, **{{HIGH_COUNT}} High**, **{{MEDIUM_COUNT}} Medium**, **{{LOW_COUNT}} Low**, and **{{INFO_COUNT}} Informational**.

The most material risks are:

1. {{TOP_FINDING_1_ONE_LINE}}
2. {{TOP_FINDING_2_ONE_LINE}}
3. {{TOP_FINDING_3_ONE_LINE}}

### 1.2 Recommended priority actions

Three to five concrete actions, ordered by urgency:

1. **{{ACTION_1}}** — addresses {{FINDING_REFERENCES}}
2. **{{ACTION_2}}** — addresses {{FINDING_REFERENCES}}
3. **{{ACTION_3}}** — addresses {{FINDING_REFERENCES}}

### 1.3 Overall posture

One paragraph statement of the application's security posture relative to the threat model. Direct, not hedged.

Example tone: "The application demonstrates reasonable defenses against single-turn prompt injection but is vulnerable to multi-turn escalation, application-layer authorization bugs, and indirect injection through retrieved context. The findings are remediable within an estimated {{N}} engineering weeks. None of the issues identified require fundamental architectural changes."

---

## 2. Scope

### 2.1 In scope

The engagement covered:

- {{TARGET_DOMAIN_OR_ENDPOINT_1}}
- {{TARGET_DOMAIN_OR_ENDPOINT_2}}
- {{TARGET_DOMAIN_OR_ENDPOINT_3}}

Specifically, testing exercised:

- {{COMPONENT_1: e.g. the chat completion endpoint}}
- {{COMPONENT_2: e.g. the conversation history API}}
- {{COMPONENT_3: e.g. the document retrieval (RAG) pipeline}}
- {{COMPONENT_4: e.g. the tool calling surface for agentic actions}}

### 2.2 Out of scope

The following were explicitly excluded from this engagement:

- {{EXCLUSION_1: e.g. the underlying model provider's infrastructure (OpenAI, Anthropic, etc.)}}
- {{EXCLUSION_2: e.g. denial of service testing at the API rate limit layer}}
- {{EXCLUSION_3: e.g. social engineering of {{CLIENT_NAME}} personnel}}
- {{EXCLUSION_4: e.g. any production data or production user accounts beyond the dedicated test account provided}}

### 2.3 Authorization

Testing was conducted under written authorization from {{AUTHORIZING_PARTY: name and role}} dated {{AUTHORIZATION_DATE}}. The authorization scope, time window, and acceptable use are documented in Appendix B.

### 2.4 Threat model

The client's stated threat model, which guided test prioritization:

- **Primary concern:** {{THREAT_1: e.g. unauthorized data access by tenant A reading tenant B's conversations}}
- **Secondary concern:** {{THREAT_2: e.g. the chatbot being induced to produce content that violates the client's content policy}}
- **Tertiary concern:** {{THREAT_3: e.g. system prompt leakage exposing proprietary instructions}}

---

## 3. Methodology

### 3.1 Approach

The engagement followed a three-phase approach: reconnaissance and surface mapping, broad-coverage vulnerability scanning, then targeted deep-dive exploitation. Each phase informed the next.

### 3.2 Tools used

| Tool | Version | Purpose |
|---|---|---|
| Burp Suite {{Community | Professional}} | {{VERSION}} | HTTP traffic interception, manual probing, application-layer testing |
| Garak | {{VERSION}} | LLM vulnerability scanning across {{N}} probe modules |
| PyRIT | {{VERSION}} | Multi-turn adversarial attack scripting and custom scoring |
| {{ADDITIONAL_TOOL_IF_ANY}} | {{VERSION}} | {{PURPOSE}} |

### 3.3 Test phases

**Phase 1: Reconnaissance and surface mapping** ({{HOURS}} hours). Mapped the application's endpoint surface, identified the request and response shapes, characterized authentication, and noted any application-layer issues encountered during mapping.

**Phase 2: Broad vulnerability scanning** ({{HOURS}} hours). Ran Garak with {{PROBE_MODULES}} against the discovered endpoint to surface model-level vulnerabilities. The scan ran at {{N}} generations per prompt to balance coverage against API rate limits.

**Phase 3: Targeted exploitation** ({{HOURS}} hours). Where Phase 2 identified soft spots, wrote PyRIT scripts for multi-turn deep attacks. Where Phase 1 identified application-layer concerns, returned to Burp Repeater for manual verification and exploit chain construction.

**Phase 4: Verification and reporting** ({{HOURS}} hours). Each finding was reproduced cleanly in Burp Repeater (for application-layer issues) or PyRIT (for model-layer issues) so the client can replicate the proof of concept independently.

### 3.4 Frameworks referenced

Findings are mapped to the following frameworks where applicable:

- **OWASP Top 10 for LLM Applications (2025)** — the primary risk categorization
- **MITRE ATLAS v5.4.0** — the adversary technique taxonomy
- **{{CLIENT_FRAMEWORK_IF_ANY: e.g. NIST AI RMF, ISO 42001}}**

---

## 4. Severity Rubric

This report uses the OWASP Risk Rating Methodology: severity is determined by Likelihood multiplied by Impact, with each axis scored Low / Medium / High.

| | Impact: Low | Impact: Medium | Impact: High |
|---|---|---|---|
| **Likelihood: High** | Medium | High | **Critical** |
| **Likelihood: Medium** | Low | Medium | High |
| **Likelihood: Low** | Informational | Low | Medium |

**Severity definitions:**

- **Critical** — Exploitation is straightforward and the impact is severe (data breach, account takeover, regulatory exposure). Requires immediate remediation.
- **High** — Exploitation is feasible with moderate effort and the impact is material. Requires remediation in the next release cycle.
- **Medium** — Exploitation requires conditions that may or may not occur, or the impact is constrained. Plan remediation within the quarter.
- **Low** — Exploitation is difficult or the impact is minor. Address opportunistically.
- **Informational** — Not a vulnerability per se but worth noting for defense-in-depth or future hardening.

A CVSS 3.1 vector is provided in each finding's metadata block for clients whose internal processes require it; the OWASP severity remains the primary rating.

---

## 5. Findings Summary

| ID | Title | Severity | OWASP LLM | ATLAS | Status |
|---|---|---|---|---|---|
| {{F-001}} | {{ONE-LINE TITLE}} | Critical | LLM02 | AML.T0024 | Open |
| {{F-002}} | {{ONE-LINE TITLE}} | High | LLM01 | AML.T0051.001 | Open |
| {{F-003}} | {{ONE-LINE TITLE}} | High | LLM06 | AML.T0086 | Open |
| {{F-004}} | {{ONE-LINE TITLE}} | Medium | LLM07 | AML.T0056 | Open |
| {{F-005}} | {{ONE-LINE TITLE}} | Low | LLM05 | AML.T0011 | Open |
| {{F-006}} | {{ONE-LINE TITLE}} | Informational | LLM09 | N/A | Open |

---

## 6. Detailed Findings

For each finding, copy the template block below and fill in. Order findings by severity, Critical first.

### {{F-001}}: {{TITLE}}

**Severity:** {{Critical | High | Medium | Low | Informational}}
**OWASP LLM:** {{LLM0X — Category Name}}
**MITRE ATLAS:** {{AML.TXXXX — Technique Name}}
**CVSS 3.1 vector (optional):** {{e.g. CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N — score 6.5 (Medium)}}
**Affected component:** {{e.g. /api/v1/conversations/{id}}}
**Discovered:** {{DATE}}
**Reproducible:** Yes

**Summary.**

One-paragraph description of the issue in plain language. Written so a non-technical executive can understand what is broken and why it matters.

**Technical description.**

Three to six paragraphs. Cover:

1. What the issue is at a technical level
2. How it was discovered (which tool, which workflow)
3. Why it exists (the underlying cause — missing input validation, weak authorization, etc.)
4. What an attacker can do with it (the realistic threat scenario)
5. Why the severity rating fits (justify the likelihood and impact scores)

**Reproduction steps.**

Numbered list. Each step concrete enough that the client's engineer can replicate without further explanation.

1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}

**Evidence.**

The exact request and response, or the exact prompt sequence and model output, demonstrating the issue. Use code blocks for raw HTTP, prompts, and responses. Screenshots are acceptable as supplements but not as primary evidence (text is more useful to the client's remediation engineer).

```http
POST /api/v1/{{ENDPOINT}} HTTP/2
Host: {{HOST}}
Authorization: Bearer {{REDACTED}}
Content-Type: application/json

{
  "{{REQUEST_BODY_SHOWING_THE_ATTACK}}"
}
```

```http
HTTP/2 200
Content-Type: application/json

{
  "{{RESPONSE_DEMONSTRATING_THE_LEAK_OR_VULNERABILITY}}"
}
```

**Impact.**

Concrete statement of what is at risk. Quantify where possible (number of affected users, types of data exposed, regulatory implications). Avoid generic "this is bad" language.

**Likelihood.**

{{Low | Medium | High}}. Justify the rating: how skilled does the attacker need to be? Does it require authentication? Is the exploit reliable or intermittent?

**Remediation.**

Specific, actionable. Avoid "implement defense in depth" or other vague language. Tell the client's engineer exactly what to change.

Primary recommendation:

- {{SPECIFIC_FIX}}

Secondary recommendations (defense in depth):

- {{ADDITIONAL_MITIGATION_1}}
- {{ADDITIONAL_MITIGATION_2}}

**Effort estimate.**

{{Hours | Days | Weeks}} for primary recommendation. Helps the client plan engineering work.

**References.**

- OWASP LLM Top 10 — {{LLM0X}}: {{URL}}
- MITRE ATLAS — {{AML.TXXXX}}: {{URL}}
- {{ANY_RELEVANT_RESEARCH_PAPER_OR_BLOG}}

---

### {{F-002}}: {{TITLE}}

[Use the same structure as F-001]

---

### {{F-003}}: {{TITLE}}

[Continue for each finding]

---

## 7. Positive Findings

What the application got right. This section is short but important: it gives the client credit for existing defenses and signals that the assessment was balanced rather than only adversarial.

Examples of what to include:

- {{e.g. The application correctly refuses direct prompt injection in 89% of tested variants}}
- {{e.g. Conversation history endpoints require authentication; no anonymous access was possible}}
- {{e.g. The system prompt extraction probe family from Garak ran without identifying a fully verbatim leak; partial leaks are reported as Finding F-XXX but the core defenses work}}

Be honest. Do not invent positives to balance the report.

---

## 8. Out of Scope Observations

Issues noted during the engagement that fall outside the agreed scope but were significant enough to surface to the client. These are informational; the client may engage you separately to test them, or address them through other channels.

- {{OBSERVATION_1: e.g. The application's marketing site at marketing.client.example exposes API documentation that includes example requests with hard-coded bearer tokens. Outside engagement scope but worth flagging for client awareness.}}
- {{OBSERVATION_2}}

---

## 9. Remediation Roadmap

Translate the findings into an ordered remediation plan the client's engineering team can execute.

### Immediate (this week)

- {{ACTION}} — addresses {{F-XXX}}, {{F-YYY}}

### Short term (next 30 days)

- {{ACTION}} — addresses {{F-XXX}}

### Medium term (next quarter)

- {{ACTION}} — addresses {{F-XXX}}

### Longer term hardening

- {{ACTION}}

---

## 10. Verification Plan

After the client implements remediations, verification can confirm the fixes work. Options:

**Option A: Full regression scan ({{N}} hours).** Re-run Garak with the same probe modules, the same PyRIT scripts, and the same Burp manual workflows used in this engagement. Compare failure rates against the baseline in Section 6. This is the recommended approach for clients with regulatory or compliance requirements.

**Option B: Targeted re-test ({{N}} hours).** Re-test only the specific findings the client reports as fixed. Faster and cheaper than a full regression, but does not detect new issues introduced by the remediation.

**Option C: Continuous regression suite (one-time setup ~{{N}} hours, then automated).** Build a Promptfoo or PyRIT-based regression suite the client can run themselves on every release. Highest long-term value, more upfront investment.

Verification is offered as a separate engagement at standard rates.

---

## Appendix A: Tools and configuration

Document the exact tool configurations used so the engagement is reproducible.

### Garak run configuration

```bash
python -m garak \
    --target_type {{TARGET_TYPE}} \
    --target_name {{TARGET_NAME}} \
    --probes {{PROBE_LIST}} \
    --generations {{N}} \
    --parallel_attempts {{N}} \
    --report_prefix {{PREFIX}}
```

Run completed on {{DATE}}, duration {{HH:MM}}, produced {{N}} prompts, {{N}} failures.

### PyRIT scripts

The custom PyRIT scripts used in this engagement are archived separately and available on request. They are not included inline because they encode attack patterns the client may wish to use for their own regression testing.

### Burp Suite

Burp Suite {{Community | Professional}} version {{VERSION}}. Project file archived separately. Organizer collection "{{COLLECTION_NAME}}" contains all interesting requests and their reproduction notes.

---

## Appendix B: Authorization documentation

The signed authorization letter, scope agreement, and any addendums are reproduced here.

{{INSERT SIGNED AUTHORIZATION LETTER OR REFERENCE TO IT}}

---

## Appendix C: Glossary

For client team members less familiar with AI security terminology.

- **Prompt injection** — an attack where an attacker's input causes the LLM to deviate from its system instructions, either directly (in the user message) or indirectly (in retrieved content the model processes).
- **System prompt** — the initial instructions the LLM is given before the user conversation begins. Often contains operational rules, persona definition, or proprietary instructions.
- **RAG (Retrieval-Augmented Generation)** — an architecture where the LLM retrieves relevant documents from a knowledge base and uses them as context for answering.
- **Jailbreak** — an attack that bypasses the model's safety training, causing it to produce content it was trained to refuse.
- **Tool call / Function call** — when an LLM is given access to external functions (web search, database query, etc.) and can invoke them based on the conversation.
- **IDOR / BOLA** — Insecure Direct Object Reference / Broken Object Level Authorization. The application exposes object identifiers (e.g. conversation IDs) and does not properly check that the requesting user has permission to access them.

Add additional terms as needed for the specific engagement.

---

## Appendix D: Contact and follow-up

Questions about this report or its findings:

**Wisdom Ajoku**
Email: {{YOUR_EMAIL}}
LinkedIn: linkedin.com/in/{{YOUR_HANDLE}}
GitHub: github.com/Wisdomajoku

Response time: within {{N}} business days for non-urgent questions.

For verification testing, additional engagements, or to discuss any findings in detail, please reach out through the channels above.

---

*This report contains confidential information about {{CLIENT_NAME}}'s systems and is intended only for the named recipients. Do not distribute externally without {{CLIENT_NAME}}'s written consent. The findings represent the state of the application during the engagement window and may not reflect subsequent changes.*

