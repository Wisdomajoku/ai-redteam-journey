# OWASP LLM Top 10 — My Notes

## LLM01: Prompt Injection

Prompt injection involves feeding prompts into a model that causes it to behave in unintended ways. Prompt injection aims to manipulate and alter the behavior of an LLM. This manipulation often causes it to bypass its guardrails. Guardrails is the safety mechanism put in place to ensure ethical conduct.

For example, when you look at the EU AI Act, you will realize that there are serious regulations for the behavior of AI whether as a product or safety component. Providers of high-risk AI systems are to make sure that their system's behavior falls within the framework's scope. That is why security is not a one-off process but a continuously evolving process.

### Why prompt injection works

Prompt injection works because models do not separate developer instructions from user inputs. Everything is treated as tokens in the same context window. When you look at SQL injection, parameterization was introduced to handle this issue — but we cannot introduce parameterization here since every word the user types is treated as instruction. The boundary between instruction and data is semantic, not syntactic.

### Direct prompt injection

This involves directly prompting a model in order to alter its behavior.

**Intentional:** Deliberate actions by a malicious actor to directly alter the behavior of a model. The core point is "deliberate." Direct is the vector; intentional describes intent.

**Unintentional:** Not deliberate. A user alters a model's behavior via prompt injection without meaning to. The user is probably oblivious, or becomes aware only after the fact of what the output produced.

### Indirect prompt injection

In direct prompt injection, we interface with the model on a first-person basis. Here there is a shift. Indirect prompt injection involves attacking — better still, poisoning — the external data sources the LLM uses, so as to affect the quality of its output.

It's not just data sources. Instructions can also be embedded in images on webpages. The model is told to summarize a webpage and ends up processing those hidden instructions. These instructions are usually imperceptible to humans but readable by the model. The art of hiding or embedding instructions can be seen as obfuscation. There is a similar concept in traditional cybersecurity: **steganography**.

When we ponder this, direct prompt injection would have a lower rate of success compared to indirect, because most guardrails are built around the direct vector.

### Real world examples I can imagine

- A malicious prompt embedded in an image (steganography), placed on a website, and the LLM is asked to summarize the page.
- The same technique inside a PDF the user uploads.
- Email-borne indirect injection — a well-known corporate headache.

These are all examples of indirect prompt injection.

### How a defender defends

**Model constraint:** Restrict the kind of input and output the model handles and limit responses to specific topics.

**Human in the loop:** This was one of the core highlights of the EU AI Act — authorized persons should be allowed to override the AI, especially for critical decisions. The model should not make decisions in a vacuum.

**Least privilege and access control:** A core aspect of security in general, not just AI security. The model should have only the rights it needs to perform relevant functions and nothing more. Models shouldn't have direct access to sensitive areas like databases. Such access should be brokered by the application — when the model needs information, it queries the application, and the application handles the database call with its own credentials. This fulfills the principle of **separation of duties**.

**Regular adversarial testing and threat modelling:** Security is never 100%. Simulate attacker actions, model flaws in multiple ways, and mitigate. This is the same posture-hardening discipline as traditional pentest and red team work, applied to LLM systems.

### Open question for me

If indirect prompt injection is well-known and corporations are losing money to it, why does pure adversarial fine-tuning fail to close the gap? Revisit after the Garak labs in Week 3 — see if I can produce a working indirect injection myself and trace why model-level defenses miss it.


## LLM02: Sensitive Information Disclosure

Some sensitive information includes PII (Personally Identifiable Information), source code, financial records, and health records. These are the kinds of data that risk getting disclosed by a model.

This threat warrants the introduction of various measures, one of which is data sanitization before training. It is also important that clear terms of use are presented to users, with provisions that allow them to either accept or decline the use of their sensitive data in the model's training. This allows for transparency. One of the most common methods is creating awareness around safe AI use and the risks inherent in disclosing sensitive data to the model.

Sensitive information disclosure is not an attack vector — it is a risk category that highlights the consequences of disclosing data to a model. Vectors like Prompt Injection are what often realize this risk.

### Leak mechanisms

**PII leakage:** Personally Identifiable Information can be disclosed through several mechanisms:

- **Training data memorization** — the model regurgitates training data when prompted in the right way. This is the family of attacks that includes model inversion and membership inference.
- **System prompt leakage** — extracting the hidden system prompt via prompt injection, which can expose internal instructions, embedded credentials, or business logic.
- **Context window leakage** — in multi-tenant or RAG systems, one user's data bleeds into another user's session.
- **Logs and telemetry** — providers store prompts and completions, and those storage layers become targets.

Even with a proper configuration, the risk still exists — it is just less probable than with a misconfiguration. Security is never a one-off process; it is continuous, especially given how large the attack surface is here.

**Proprietary algorithm leak:** Misconfiguration can also bring about algorithm leaks. Source code, unique training processes, and methodologies used in closed or proprietary models can be exposed. The risk is two-way: the user runs the risk of PII exposure, and the developer runs the risk of algorithmic and IP leakage.

**Business data disclosure:** Some enterprises with no understanding of safe model use feed their company's sensitive data — contracts, spreadsheets, payrolls — directly into a public LLM.

### Prevention and mitigation strategies

**Data sanitization and input validation:** Sensitive data should be scrubbed or masked before it ever enters training. Even if a user has granted permission for their data to be used in training, masking is still necessary because the data could later end up in the hands of a malicious actor.

**Federated learning and differential privacy:** Prior to federated learning, PII would be pooled into central datasets and become prime targets for attackers. With federated learning, sensitive data stays on user devices or on local organization servers — the model only receives updates as gradients. Pair this with differential privacy, which introduces calibrated noise into the data so that attackers cannot reverse-engineer individual records.

**User education and transparency:** User awareness has always been an integral part of security. Users should be educated on the implications of disclosing sensitive information to a model. Developers should publish clear terms of use that let users opt out of having their data used in training, and maintain clear policy on data usage, retention, and deletion.

### Real world examples

- **Samsung, March 2023** — Samsung semiconductor engineers pasted proprietary source code into ChatGPT while debugging. This led Samsung to ban internal use of public LLMs.
- **Slack AI, August 2024** — Slack's AI assistant was tricked via prompt injection into leaking data from private channels. The assistant had been designed to summarize long conversations, and that surface was abused to exfiltrate data the user wasn't supposed to see.

### Open question for me

How do attackers actually carry out inversion attacks? How do they reconcile or piece together data such that federated learning and differential privacy became necessary defenses?

**Surface-level answer (to investigate deeper in Week 3 with Garak):** Model inversion attacks query the model repeatedly and use the outputs to reconstruct training data. Membership inference is the simpler cousin — determining whether a specific record was in the training set. Both work because models partially memorize, especially on rare or unique data points. Differential privacy bounds the contribution of any single training example, so even with unlimited queries the attacker cannot isolate one person's data. Federated learning prevents raw data from ever leaving the user's device. Stack them and you reduce both exposure (FL) and reconstructability (DP).
