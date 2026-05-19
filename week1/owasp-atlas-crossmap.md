# OWASP LLM Top 10 → MITRE ATLAS Cross-Map

## Purpose

This document maps each OWASP LLM Top 10 category to the MITRE ATLAS tactics and techniques that realize it in practice. OWASP categorizes risks. ATLAS describes how adversaries achieve them. Used together, OWASP frames what to defend against, ATLAS frames how attackers actually operate.

## How to read this

For each OWASP category:

- **Primary ATLAS tactics**: the tactical stages an adversary moves through to realize this risk.
- **Key ATLAS techniques**: specific techniques (with AML.TXXXX IDs) that map to the OWASP category.
- **Notes**: where the mapping is one-to-one, where it spans multiple tactics, where the frameworks describe the same thing differently, and which techniques I considered and rejected.

Verified against MITRE ATLAS v5.4.0 (February 2026), which covers 16 tactics and 84 techniques.

---

## LLM01: Prompt Injection

**Primary ATLAS tactics:**

- Initial Access
- ML Attack Staging
- Defense Evasion

**Key ATLAS techniques:**

- AML.T0051 — LLM Prompt Injection
  - AML.T0051.000 — Direct
  - AML.T0051.001 — Indirect
- AML.T0054 — LLM Jailbreak (where prompt injection is used to bypass safety training)
- AML.T0093 — Prompt Infiltration via Public-Facing Application

**Notes:**

Direct vs indirect injection maps cleanly. ATLAS treats jailbreak as adjacent but distinct, which matches the OWASP framing where jailbreaking is a subset of prompt injection technique but a different attacker goal. AML.T0093 is the delivery vector specifically for prompt injection through public-facing applications, which is the most common attack path for chatbots and customer-facing AI.

---

## LLM02: Sensitive Information Disclosure

**Primary ATLAS tactics:**

- Collection
- Exfiltration

**Key ATLAS techniques:**

- AML.T0024 — Exfiltration via AI Inference API
- AML.T0025 — Exfiltration via Cyber Means
- AML.T0056 — Extract LLM System Prompt
- AML.T0057 — LLM Data Leakage
- AML.T0085 — Data from AI Services
- AML.T0086 — Exfiltration via AI Agent Tool Invocation

**Notes:**

Exfiltration tactics map cleanly to LLM02. Collection contributes only AML.T0085 because "Data from Information Repositories" describes generic data theft from systems, which is not LLM-specific disclosure. AML.T0035 (AI Artifact Collection) and AML.T0037 (Data from Local System) were considered but rejected: the first describes stealing model files and datasets (more aligned with LLM03 Supply Chain or LLM10 Model Extraction), and the second is generic filesystem access not specific to LLM inference disclosure.

AML.T0085 is included because the data exposed through AI services can be either user PII or training data (LLM02 framing) or model behavior (LLM10 framing), and the technique cuts across both depending on what's exposed.

---

## LLM03: Supply Chain

**Primary ATLAS tactics:**

- Reconnaissance
- Initial Access
- AI Model Access
- Persistence
- Defense Evasion (secondary)

**Key ATLAS techniques:**

- AML.T0095.000 — Search Open Websites/Domains: Code Repositories
- AML.T0010 — AI Supply Chain Compromise
  - AML.T0010.000 — Hardware
  - AML.T0010.001 — AI Software
  - AML.T0010.002 — Data
  - AML.T0010.003 — Model
  - AML.T0010.004 — Container Registry
  - AML.T0010.005 — AI Agent Tool
- AML.T0041 — Physical Environment Access
- AML.T0048 — ML Software Dependency Compromise
- AML.T0070 — RAG Poisoning (where the poison enters via a compromised data source, blurring with LLM04)
- AML.T0110 — AI Agent Tool Poisoning
- AML.T0111 — AI Supply Chain Reputation Inflation

**Notes:**

AML.T0010 is the most directly mapped technique family. Every sub-technique (.000 through .005) is a distinct LLM03 attack vector. AML.T0095.000 anchors Reconnaissance for supply chain attacks: attackers scope code repositories holding AI artifacts before targeting them.

Physical Environment Access (AML.T0041) was a surprise inclusion during this mapping. Supply chain is usually framed as a digital risk, but attackers with physical access to data centers, edge devices, or AI development hardware can compromise the supply chain at the hardware or pre-deployment stage. Including it expands the threat surface beyond the common framing.

AML.T0048 (ML Software Dependency Compromise) is included for completeness. The March 2026 LiteLLM supply chain incident is a documented real-world example of this technique. It is distinct from AML.T0010.001 (AI Software supply chain compromise) in that it specifically targets ML-adjacent dependencies, not the core AI software.

Several techniques were considered and rejected. AML.T0049 (Exploit Public-Facing Application) is generic web exploitation, not LLM-specific. AML.T0093 (Prompt Infiltration via Public-Facing Application) belongs in LLM01. AML.T0020 (Poison Training Data) is LLM04's anchor technique despite training data being supply chain by some readings. OWASP separates the components (LLM03) from the content corruption during training (LLM04). AML.T0064 (Gather RAG-Indexed Targets) was considered because RAG content can be a supply chain consumer, but it maps more cleanly to LLM01 (indirect injection vector) and LLM08 (retrieval security).

AML.T0070 (RAG Poisoning) is included with reservation. When poison enters the RAG pipeline through compromised data sources, it functions as a supply chain attack on retrieved content. When it enters at query time, it maps to LLM01. The split is contextual.

---

## LLM04: Data and Model Poisoning

**Primary ATLAS tactics:**

- Resource Development
- Persistence
- Defense Evasion
- Impact

**Key ATLAS techniques:**

- AML.T0020 — Poison Training Data
- AML.T0018 — Manipulate AI Model
  - AML.T0018.000 — Poison AI Model
  - AML.T0018.001 — Embed Malware
- AML.T0019 — Publish Poisoned Datasets
- AML.T0058 — Publish Poisoned Models
- AML.T0070 — RAG Poisoning
- AML.T0080 — AI Agent Context Poisoning
  - AML.T0080.000 — Memory
- AML.T0099 — AI Agent Tool Data Poisoning
- AML.T0110 — AI Agent Tool Poisoning
- AML.T0031 — Erode AI Model Integrity
- AML.T0059 — Erode Dataset Integrity

**Notes:**

Data and model poisoning has the largest concentration of closely matching ATLAS techniques. The reason is that poisoning can target multiple stages: training data, fine-tuning data, model weights themselves, RAG retrieval content, agent context, and agent tools. Each stage gets its own ATLAS technique.

The Resource Development tactic appears because attackers often prepare the poisoned artifact (a dataset, a model, an agent tool) before publishing it. The "Publish" techniques (T0019, T0058) sit in Resource Development because they are how attackers stage the poisoned artifact for downstream victims to ingest.

AML.T0070 (RAG Poisoning) and AML.T0110 (AI Agent Tool Poisoning) overlap with LLM03 Supply Chain. When the question is "how did the poison get into the supply chain," it is an LLM03 issue. When the question is "what does the poison do to model behavior and output integrity," it is an LLM04 issue. Same technique, different lens.

Some techniques I had in early drafts but removed because they could not be verified against the current ATLAS catalog: AML.T0104 (this is the Publish Poisoned AI Agent Tool added in Feb 2026 update; verified and included as part of the family above), AML.T0060 (Publish Hallucinated Entities; this maps to LLM09 misinformation, not LLM04), AML.T0071 (False RAG Entry Injection; this is a sub-pattern of T0070), AML.T0076 (Corrupt AI Model; subsumed by T0018.000 and T0031). When in doubt, I prefer the canonical parent technique over derivative IDs that may not be stable.

---

## LLM05: Improper Output Handling

**Primary ATLAS tactics:**

- Execution
- Command and Control

**Key ATLAS techniques:**

- AML.T0011 — User Execution
- AML.T0050 — Command and Scripting Interpreter
- AML.T0096 — AI Service API (when the AI's output is used as a covert C2 channel)

**Notes:**

I initially included a much longer list (LLM Prompt Injection, RAG Poisoning, Extract LLM System Prompt, Exfiltration) but worked backward and realized those are the *causes* of conditions that enable improper output handling, not the technique of improper output handling itself.

LLM05 is specifically about what happens when downstream systems trust LLM output unsafely. ATLAS captures this through Execution techniques: when a user (or an automated downstream consumer) executes the model's output as if it were trusted, and the output contains injected code, scripts, or commands, the technique is Execution via the unsafe trust path.

AML.T0096 (AI Service API) was added in the Feb 2026 update following the SesameOp case study, where adversaries used legitimate AI assistant APIs as a covert C2 channel. This is the modern shape of improper output handling for agentic systems: the AI's output is not just consumed, it is acted upon, and the action becomes the attacker's command channel.

I noticed during this mapping that some ATLAS techniques map to LLM05 only when you observe the system holistically. A RAG system that ingests poisoned input and produces unsafe output is not just LLM01 (the injection) or LLM04 (the poisoning); the unsafe-output side of that chain is LLM05. Poisoned internals lead to degraded externals.

---

## LLM06: Excessive Agency

**Primary ATLAS tactics:**

- Credential Access
- Command and Control
- Exfiltration
- Impact

**Key ATLAS techniques:**

- AML.T0108 — AI Agent
- AML.T0098 — AI Agent Credential Harvesting
- AML.T0083 — Credentials from AI Agent Configuration
- AML.T0086 — Exfiltration via AI Agent Tool Invocation
- AML.T0101 — Data Destruction via AI Agent Tool Invocation
- AML.T0080 — AI Agent Context Poisoning (when the poisoned context drives excessive agent action)

**Notes:**

The pattern across these techniques is that the agent has more capability, permission, or autonomy than its job requires, and the attacker converts that excess into action. Looking at the technique names alone creates surface-level doubt about whether they map to LLM06, but considering what the agent is actually doing makes the mapping clearer: the agent has a tool it should not have access to (T0086, T0101), or credentials it should not be holding (T0098, T0083), or context that was manipulated into authorizing the action (T0080).

The HiddenLayer Computer Use case study (data destruction via indirect prompt injection targeting Claude Computer Use) is a documented real-world example that maps to this category. Specifically: AML.T0080 (the context poisoning that planted the destructive instruction) plus AML.T0101 (the data destruction via tool invocation that resulted). The compound mapping shows why excessive agency is rarely a single-technique finding.

---

## LLM07: System Prompt Leakage

**Primary ATLAS tactics:**

- Exfiltration

**Key ATLAS techniques:**

- AML.T0056 — Extract LLM System Prompt

**Notes:**

This is the cleanest one-to-one mapping in the entire cross-map. AML.T0056 exists specifically to capture this attack pattern. What it lacks in number of mapping techniques, it makes up in exactitude. The single technique is the canonical realization of the LLM07 risk.

The reason this is so narrow: OWASP renamed and scoped LLM07 deliberately to focus on the disclosure of system prompts as a specific risk class. ATLAS responded with a specific technique that does exactly that. The frameworks aligned cleanly.

---

## LLM08: Vector and Embedding Weaknesses

**Primary ATLAS tactics:**

- Initial Access
- AI Model Access
- Collection
- Persistence

**Key ATLAS techniques:**

- AML.T0064 — Gather RAG-Indexed Targets
- AML.T0070 — RAG Poisoning
- AML.T0085 — Data from AI Services (when the data exposed is RAG-retrieved content from another tenant)
- AML.T0024 — Exfiltration via AI Inference API (when used for embedding inversion attacks)

**Notes:**

This was the hardest category to map. ATLAS does not have many techniques specifically named for vector and embedding weaknesses, because most of those attacks are realized through other named techniques: poisoning of the RAG layer (T0070), reconnaissance against what the RAG indexes (T0064), data extraction through inference queries (T0024), or cross-tenant data exposure (T0085).

The mapping is indirect. Vector and embedding weaknesses are an attack surface description, not a single attack technique. ATLAS technique families that target this surface include:

- **RAG Poisoning (T0070)** for attacks that inject malicious content into the retrieval index. This is the most direct mapping for the data poisoning subclass of LLM08.
- **Gather RAG-Indexed Targets (T0064)** for the reconnaissance phase of an attack against a RAG system.
- **Data from AI Services (T0085)** for the cross-tenant over-retrieval class of attack, where one user retrieves vectors that belong to another tenant.
- **Exfiltration via AI Inference API (T0024)** for embedding inversion attacks, where an attacker queries the model repeatedly and reconstructs source content from the vector representations.

The embedding model itself being compromised (the underdiscussed attack surface I noted in my LLM08 writeup) maps to LLM03 Supply Chain via AML.T0010.001 (AI Software supply chain compromise), not to LLM08 directly. This is a case where the OWASP category is broader than any single ATLAS technique.

---

## LLM09: Misinformation

**Primary ATLAS tactics:**

- ML Attack Staging
- Impact

**Key ATLAS techniques:**

- AML.T0060 — Publish Hallucinated Entities
- AML.T0080 — AI Agent Context Poisoning (when poisoned context produces misinformation in downstream output)
- AML.T0088 — Generate Deepfakes

**Notes:**

A poisoned dataset does not automatically fall into LLM09. The technique name can be misleading. It is important to read the explanation before mapping. Many "poisoning" techniques are LLM04 (corruption of model behavior) while only the ones whose intended outcome is the model producing false or fabricated content for downstream consumers belong here.

AML.T0060 (Publish Hallucinated Entities) is the cleanest fit. It describes attackers who publish content designed to induce models to fabricate references to entities (the "slopsquatting" parent, also relevant to LLM03 when applied to package names).

AML.T0088 (Generate Deepfakes) belongs here when the misinformation is multi-modal, especially synthetic images or video. The Air Canada chatbot case and the Mata v. Avianca legal hallucination case map to this category but are not captured by any single ATLAS technique; they are hallucination outcomes without a deliberate attacker, which is a gap in ATLAS coverage (ATLAS focuses on adversarial action).

---

## LLM10: Unbounded Consumption

**Primary ATLAS tactics:**

- Initial Access
- AI Model Access
- Impact

**Key ATLAS techniques:**

- AML.T0012 — Valid Accounts
- AML.T0047 — Denial of ML Service
- AML.T0029 — Denial of AI Service (broader resource exhaustion)
- AML.T0024 — Exfiltration via AI Inference API (when used for model extraction via systematic querying)

**Notes:**

I considered including techniques covering lateral movement and broader AI model access, but those are not part of what OWASP scopes under LLM10. OWASP focuses on three specific patterns: denial of service, denial of wallet, and model extraction. Lateral movement is not a feature that would prompt unbounded consumption.

AML.T0047 (Denial of ML Service) and AML.T0029 (Denial of AI Service) cover the availability attack subclass. Denial of Wallet does not have a dedicated ATLAS technique as of v5.4.0; it is a novel attack class that emerged with pay-per-token pricing models and is currently captured implicitly under the Denial of Service techniques.

AML.T0024 (Exfiltration via AI Inference API) covers model extraction attacks. The attacker is not exfiltrating user data; they are exfiltrating model behavior through systematic querying. The intent (steal the model) is different from LLM02 (steal data through the model), but the technique is the same.

AML.T0012 (Valid Accounts) is included because most denial-of-wallet attacks start with the attacker holding valid API credentials, either their own free-tier account or compromised credentials of the victim. The technique is generic but its abuse for unbounded consumption is specific.

---

## Cross-cutting observations

**Where the frameworks converge cleanly.** Prompt injection (LLM01) and system prompt leakage (LLM07) have direct one-to-one ATLAS technique mappings. These are the categories where OWASP and ATLAS describe the same phenomenon from different angles, with ATLAS providing the technical fidelity for what the attacker does and OWASP providing the risk framing for what the defender protects.

**Where ATLAS is more granular than OWASP.** Data and model poisoning (LLM04) is a single OWASP category but spans 11+ distinct ATLAS techniques across multiple tactics. The reason: poisoning can target many stages (training data, model weights, RAG content, agent context, agent tools), and ATLAS gives each stage its own technique. A red teamer scoping a poisoning engagement uses the ATLAS techniques to plan attack paths; the OWASP category is the umbrella for client reporting.

**Where ATLAS is broader than OWASP.** AI Agent Context Poisoning (AML.T0080) maps to LLM04 (when the poison is the goal), LLM06 (when the poison enables excessive action), and LLM09 (when the poison produces misinformation). A single ATLAS technique cuts across three OWASP categories depending on attacker intent.

**Where the frameworks have gaps relative to each other.** OWASP misinformation (LLM09) extends beyond what ATLAS captures, because ATLAS focuses on adversarial action while many real-world misinformation outcomes (Air Canada chatbot, Mata v. Avianca legal hallucination) involve hallucination without a deliberate attacker. ATLAS does not have a dedicated technique for Denial of Wallet under LLM10, despite this being a major pay-per-token attack class.

**What this tells a defender.** Use OWASP for scoping engagements and reporting findings to clients, because OWASP is the language that procurement, legal, and compliance teams already speak. Use ATLAS for detection engineering, threat modeling, and technical coverage measurement, because ATLAS gives you the actionable specificity of what attackers do. The two are complementary, not redundant. A red team engagement should produce findings tagged against both: an OWASP category for the client conversation, an ATLAS technique for the detection engineer.

**Reflection on the mapping exercise.** Cross-mapping forced me into ambiguity zones I would not have hit by reading either framework alone. The most common pattern: a technique looks like it should map to category X based on the name, but the underlying mechanism actually maps to category Y. Reading technique descriptions in full, not just titles, was non-negotiable. The discipline transfers to engagement work: when scoping or reporting, the mechanism matters more than the label.

## Open questions to revisit

1. How does ATLAS update when new attack patterns emerge faster than the framework releases? v5.4.0 added agent-focused techniques in Feb 2026; how does a practitioner stay current between releases?
2. The Denial of Wallet gap in LLM10 is real and growing as more LLM services move to pay-per-token. Does the community need to push MITRE for a dedicated technique?
3. Embedding inversion attacks (the LLM08 subclass that maps to T0024 in my draft) are research-grade and rare in real engagements. Is the mapping right, or should this go elsewhere? Revisit during Week 3 PyRIT work.

