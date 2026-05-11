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
