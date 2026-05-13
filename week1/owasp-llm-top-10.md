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


## LLM03: Supply Chain

The LLM supply chain is not exempt from supply chain vulnerabilities. When we talk about supply chain, we mean the various components involved in producing and running a model — if any of them is compromised, that becomes problematic not just for the provider but also for the downstream user running it in production.

### Components in the LLM supply chain

- **Base model** — e.g. Meta Llama, OpenAI models, models hosted on Hugging Face
- **Fine-tuning and training datasets** — including techniques like LoRA (Low-Rank Adaptation) and other Parameter-Efficient Fine-Tuning methods
- **Software dependencies and runtime stack** — vLLM, Python, LangChain, and the broader set of libraries that let the model run, serve, and communicate over the internet

### Categories of risk

**Traditional third-party package vulnerability:** Even if you have a secure model, it still runs on a stack of dependencies — Python, C++ libraries, framework code. A bug in any dependency can give an attacker a path into the LLM application. This is why LLM applications are best described as a stack of dependencies, not a single artifact.

**Licensing risk:** AI development requires pulling data and code from many sources. Most code on GitHub is open source, but open source is not public domain — it comes with licenses. The GPL (General Public License) is particularly dangerous because of its copyleft clause: if you incorporate GPL code into your model or product, you can be legally compelled to release your own source code under the same license. Dataset licenses carry similar contamination risks.

**Outdated or deprecated models:** The market is flooded with models, and it is hard to tell which are still maintained. Users often confuse availability with choice. Outdated or deprecated models are already a security risk because they no longer receive patches for newly discovered vulnerabilities.

**Weak model provenance:** Model provenance means tracing where a model came from and verifying its integrity. Provenance in AI is currently very weak. Hugging Face offers model cards that describe the provider, training process, and intended use — but model cards are metadata, not cryptographic proof. There is no widespread signing or hashing standard that lets a downstream user verify that the weights they downloaded are the weights the provider released.

**Vulnerable LoRA adapters:** Retraining a full model is expensive and resource-intensive, so LoRA adapters have become popular — you train a small adapter layer and insert it into the base model to teach it new behavior. This saves cost and avoids breaking the base model. The downside is that a compromised adapter can compromise the entire model, and adapters are often shared casually online without integrity checks.

**Malicious model weights:** Pre-trained model files (`.pt`, `.bin`, pickle-based formats) are not just data — when loaded by frameworks like PyTorch, they can execute arbitrary code via pickle deserialization. Downloading a poisoned model from a public registry is the LLM equivalent of pulling a malicious npm package.

### Real world examples

- **PoisonGPT (2023)** — Researchers at Mithril Security demonstrated this by uploading a subtly poisoned model to Hugging Face that gave deliberately wrong answers on specific topics. The point was to prove that model hubs have no integrity verification — anyone can upload a tampered model with a clean-looking model card.
- **Malicious pickle files in model weights** — Repeated incidents of `.bin` and `.pt` files on Hugging Face containing embedded code that executes on load, exploiting Python's unsafe pickle deserialization.

### Prevention and mitigation strategies

**Red team third-party models before adoption:** Trust benchmarks are useful but bypassable. Carry out adversarial testing on any third-party model before integrating it into production, especially if it will handle sensitive workflows.

**Vet data sources and suppliers:** Read their terms and conditions, assess their security posture, review their privacy policies, and check their incident history. This is standard third-party risk management applied to AI suppliers.

**Maintain a Software Bill of Materials (SBOM):** An accurate, signed inventory of every model, dataset, adapter, and dependency in your stack. SBOMs let you respond quickly to newly disclosed vulnerabilities and zero-days, because you know exactly what you have.

**Verify model integrity:** Because provenance standards are weak, only use models from verifiable or reputable sources, and apply your own integrity checks — file hashes, signature verification, and where possible, loading models in sandboxed environments to limit blast radius from malicious weights.

### Open question for me

How does the AI/ML community plan to solve the model provenance problem long-term? Are there efforts like Sigstore-for-models, signed model cards, or any cryptographic standard emerging? Revisit when I look at Hugging Face's security tooling in Week 2.
