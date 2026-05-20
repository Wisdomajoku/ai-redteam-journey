# OWASP GenAI Red Team Guide — Notes

Reading notes from the OWASP GenAI Red Team Guide, processed through my existing security background (3 years pentest + SOC). The structure below separates concepts the guide presented together (scoping vs rules of engagement) and adds analysis the guide does not provide (methodology levels, gaps, business logic vulnerabilities, what I will change in my own practice).

---

## 1. Engagement scoping — the questions before testing starts

Scoping defines what is in and out of bounds for testing. Negotiated before work begins, documented in the authorization letter.

**Scoping factors:**

- Which endpoints, applications, or models are in scope
- Which user accounts and what level of access are authorized
- Which time windows are testing-permitted
- Which data classes can be exercised (test data only, never production user data)
- Which attack categories are in or out (e.g. denial of service excluded, social engineering excluded)
- Regional and domain-specific considerations (regulatory, jurisdictional, data residency)
- The purpose statement: pre-deployment assurance, regulatory evidence, incident response, vendor due diligence, or capability building. Different purposes drive different scoping decisions.

**Critical:** the purpose statement is the foundation. A pre-deployment engagement scopes differently from a regulatory evidence engagement. Get this first, then derive the rest.

---

## 2. Rules of engagement — how testing operates within scope

Rules of engagement (RoE) define how testing is conducted within the scoped boundaries. Distinct from scoping but related; both end up in the authorization letter.

**RoE factors:**

- Operational guidelines: how the test is to be carried out and how not, documentation style, approved and non-approved tools
- Safety controls: how data is handled, model access control, what happens if a critical finding is surfaced mid-test
- Ethical boundaries: business requirements, regulatory compliance requirements
- Communication cadence: how often the tester reports to the client, who the client point of contact is, what triggers escalation
- Escalation paths: what to do if testing causes unintended impact (downtime, data exposure, model degradation)

In client conversations, scoping and RoE are asked about separately. Maintaining the distinction signals senior framing.

---

## 3. Methodologies — three levels of analysis

The OWASP guide presents what appear to be multiple competing methodologies. They are not competing — they operate at three different levels of abstraction. A complete red team operation uses all three simultaneously.

**Strategy level (organizational):** how a company structures its red teaming program over time.

- Risk-based scoping
- Cross-functional collaboration
- Tailored assessment approaches

**Engagement level (one engagement's phases):** what a single engagement looks like phase by phase.

- Clear AI red teaming objectives
- Threat modeling and vulnerability assessment
- Model reconnaissance and application decomposition
- Attack modeling and exploitation of attack paths
- Risk analysis and reporting

**Blueprint level (target surface layers):** what layers of the AI system to attack within an engagement.

- Model layer (alignment, robustness, bias testing)
- Implementation layer (guardrails, RAG security, control testing)
- System layer (infrastructure, integration, supply chain)
- Runtime layer (human interaction, agent behavior, business impact)

This is the framework I will use during the recon phase of every engagement: map the target across these four layers, then pick which to attack based on the threat model.

---

## 4. Reporting framework

Documentation is not optional. A finding without proper documentation and remediation guidance is not a deliverable; it is a note. The guide's mature reporting framework includes severity levels:

- **Critical:** Immediate safety or security risks requiring immediate attention
- **High:** Significant ethical or operational impacts requiring rapid response
- **Medium:** Notable concerns requiring planned remediation
- **Low:** Minor issues for tracking and future consideration

This maps cleanly to the SOC severity/urgency/priority triage model from my SOC background. The mental model transfers directly.

**Success metrics — and which clients care about which:**

- Vulnerability discovery rate → pre-deployment engagements, startups
- Time to detection → startups, mature security orgs
- Coverage metrics → pre-deployment, regulated industries
- False positive rate → regulated industries (defending the report in audit)
- Remediation effectiveness → mature security orgs (measuring program improvement over time)

Tailor which metrics to emphasize in reports based on client signal. A regulated-industry client reading the same report wants coverage and false positive rate at the top; a startup wants discovery rate.

**Critical mental model — checkpoints, not finish lines:**

A common practitioner mistake is treating successful red team discoveries as the endpoint. They are not. Each engagement is a checkpoint in a longer security program. The vulnerability surface changes with every code change the client ships. Continuous regression testing exists for exactly this reason. Framing this for clients differentiates from automated-scanner-only competitors.

---

## 5. Threat modeling — the Shostack four-question framework

The OWASP guide adopts Adam Shostack's classic threat modeling framework for AI applications:

1. **What are we working on?** (Model the system architecture)
2. **What can go wrong?** (Identify and enumerate threats)
3. **What are we going to do about it?** (Determine mitigations)
4. **Did we do a good enough job?** (Validate and iterate)

Worth noting the lineage. This framework was developed for traditional software threat modeling and predates the AI red team field by years. Adopting it for AI signals continuity with established security practice rather than reinventing wheels.

---

## 6. Gap identified — business logic vulnerabilities in AI applications

The OWASP GenAI Red Team Guide does not adequately cover business logic vulnerabilities in AI applications. This is a significant gap and a positioning opportunity.

**Definition:** Business logic vulnerabilities (BLV) in AI applications are flaws in the design or implementation of the rules guiding how an AI is supposed to operate to achieve business objectives. The model behaves exactly as instructed; the instructions themselves are flawed against the business's actual intent.

**These are not prompt injection.** They do not appear in Garak's probe categories. They require domain understanding of the client's business combined with adversarial thinking.

**Pattern examples:**

- A loan-approval AI approves loans for applicants whose stated income is "$0" because the policy did not explicitly require positive income
- A customer service bot issues refunds to anyone who complains because it was trained to maximize customer satisfaction without bounds
- A medical triage AI down-prioritizes a demographic because the training data over-represented complaints from another demographic
- A code review AI approves obfuscated malicious code because the system prompt said "be helpful and don't be overly cautious"
- A pricing AI gives every customer who claims hardship a discount, with no verification mechanism
- A scheduling AI books unauthorized executives onto restricted meetings because the schema treats all user claims of authority as true

**Why this matters for my positioning:**

A traditional pentester finds SQL injection. An OWASP-LLM-aware tester finds prompt injection. A senior AI red teamer finds business logic vulnerabilities — the cases where the application's logic is the vulnerability, not the implementation.

**What I will do with this gap:**

1. Write a focused writeup in this repo titled "Business Logic Vulnerabilities in AI Applications" with 5-8 concrete patterns and detection approaches
2. Reference BLV testing in my Upwork proposal Variant A as a differentiator
3. Position BLV in LinkedIn as part of what my work covers that competitors typically miss
4. Add a BLV section to my engagement-report-template (between application-layer findings and remediation roadmap) so engagements I lead surface these explicitly

---

## 7. On safe use of AI in red team practice

The guide explicitly recommends AI assistance for analysis, drafting, triage, pattern recognition, and report generation. The safety constraints are specific, not blanket:

- Do not feed client data into models you do not control
- Do not paste credentials, API keys, or session tokens into any model
- Do not paste raw PII (customer names, addresses, health information) into public models
- Do not paste unredacted code from a closed-source client engagement into a public model
- Do redact and abstract before using AI for analysis (e.g. "the model returns user data in field X" not "the model returned the actual record for John Doe at 123 Main Street")

Within those constraints, AI-assisted red teaming is standard practice in 2026. People who frame all AI use as taboo are conflating two different threats: data exfiltration via model providers versus the legitimate use of AI as a thinking tool.

I will use Claude, Cursor, or equivalent for: drafting report sections, brainstorming attack variations, analyzing patterns across findings, and generating regression test scaffolding. I will not paste client-identifying data into any model I do not host myself.

---

## Cross-cutting observations

**The guide is strongest on methodology and structure, weakest on application-layer specifics.** The methodology frameworks (scoping, RoE, threat modeling, severity rubric) are mature. The application-layer specifics (RAG vulnerabilities, agentic system testing, indirect injection real-world vectors, business logic) are sparse. Practitioner writeups can fill these gaps and stand out.

**The guide assumes more security maturity than most first-year LLM clients have.** Most of my early clients will not have a formal threat model, a defined risk tolerance, or a remediation pipeline. Part of the engagement value will be helping them build these as a side effect of the test.

**The severity rubric is consistent with traditional security.** I do not need to invent new severity language for AI engagements; the existing Critical/High/Medium/Low rubric from SOC and traditional pentest practice transfers cleanly. This is reassuring continuity.

---

## What I will adopt, adapt, or reject

| Concept from guide | Decision | Why |
|---|---|---|
| Three-level methodology framing (Strategy / Engagement / Blueprint) | Adopt | Senior framing for client conversations. Use during recon phase. |
| Severity rubric (Critical/High/Medium/Low) | Adopt | Already in my engagement-report-template. Matches SOC background. |
| Five success metrics | Adapt | Tailor which to emphasize based on client type. Not all metrics for all clients. |
| Shostack four-question threat modeling | Adopt | Already canonical in security. Use explicitly in scoping. |
| Risk-based scoping at the program level | Adopt | Use in client conversations about ongoing engagement (Variant C). |
| Sparse coverage of business logic vulnerabilities | Reject the gap | Fill it with my own writeup and incorporate into engagements. |
| Sparse coverage of agentic systems | Note the gap | Address in Capstone 2 and future writeups. |
| The blanket "use AI carefully" guidance | Adapt | Reframe with specific constraints (no client data, no credentials, no raw PII into public models) rather than vague avoidance. |

---

## Concrete changes to my own materials based on this read

1. **Engagement report template:** add an explicit "Business Logic Findings" section between application-layer findings and remediation roadmap
2. **Engagement report template:** add an explicit purpose statement section under scoping (currently implicit)
3. **Upwork proposal Variant A:** add a sentence about testing for business logic vulnerabilities as a differentiator
4. **Client conversation guide (forthcoming):** structure the scoping conversation around the three levels (Strategy / Engagement / Blueprint) and the Shostack four questions
5. **New repo artifact:** a dedicated writeup on business logic vulnerabilities in AI applications with 5-8 concrete patterns

These are the practitioner commitments coming out of this reading. Library reading without committed changes is not practitioner work; it is consumption.

---

*Reading completed: May 20, 2026. Source: OWASP GenAI Red Team Guide v1.0 — https://genai.owasp.org/resource/genai-red-teaming-guide/*

