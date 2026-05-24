# NIST AI 600-1 - Generative AI Profile Reading Notes

*Reading completed: May 21, 2026. Source: NIST AI 600-1 - Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile - nist.gov/itl/ai-risk-management-framework*

---

## Why This Document Exists Separately from the Core RMF

The AI RMF is a broad, high-level policy document. It applies to every AI system, simple or complex, and defines the four functions (Govern, Map, Measure, Manage) that give organizations a consistent language and process across the board.

NIST AI 600-1 differs in scope. Where the AI RMF is broad, 600-1 specializes in generative AI specifically. An organization can use the AI RMF for broad coverage and 600-1 for teams working directly on generative AI products. Both complement each other. They are not in opposition.

One reframing the AI RMF introduces that 600-1 builds on: it pushes practitioners away from treating prompt injection as just a security vulnerability in isolation, toward weighing it based on actual impact on humans, organizations, and ecosystems. 600-1 applies that exact thinking to generative AI risk categories.

---

## Risk Categories Under NIST AI 600-1

### CBRN Information

CBRN stands for Chemical, Biological, Radiological, and Nuclear. The concern is that generative AI may make it easier for threat actors to access information in these domains.

The danger is real but analysts argue it is not immediately imminent. Whatever a model knows is largely drawn from publicly accessible information, and actual development and deployment of such agents still requires significant human expertise.

One admission in the document worth flagging explicitly: it states that current LLMs lack the capacity to plan biological attacks. That statement is itself an acknowledgment that the likelihood is real. As models become more capable, the possibility of facilitating such planning becomes a genuine threat worth tracking.

### Confabulation

Often called hallucination. Confabulation is when a model confidently generates false information due to gaps in its training data relative to a users query, pressure from a system prompt to produce a response, or a combination of both.

The term hallucination is increasingly rejected in technical circles because it attributes human qualities of awareness to the model. Confabulation is the more precise term.

### Dangerous or Violent Recommendations

Generative AI systems have been known to generate harmful responses across modalities including text, audio, video, and images. This includes detailed, step-by-step outputs on how to harm oneself or others.

Some models implement restrictions against this class of output. Attackers can and do circumvent those restrictions through prompt injection, jailbreaking, and similar techniques. The restriction is a layer, not a guarantee.

### Data Privacy

A serious risk in generative AI. Models have been shown to leak sensitive information including biometrics and personally identifiable information, sourced from the high-volume, multi-source training data they were built on.

One specific mechanism: during training, a model may overfit or memorize specific training data including PII, and that memorized content can surface in model responses. This maps directly to OWASP LLM02 (Sensitive Information Disclosure) and OWASP LLM05 (Improper Output Handling).

Users should be guided toward safe AI use and explicitly warned against sharing sensitive information in model interactions.

### Environmental

Training a model is computationally and environmentally costly. The carbon footprint is substantial. Estimates put the emissions from training a single large transformer model at roughly the equivalent of 300 round trips between San Francisco and New York.

Proposed mitigations include model distillation and compression. Not a primary security concern for most engagements but relevant for enterprise clients with sustainability mandates or ESG reporting requirements.

### Human-AI Configuration

The core focus here is overreliance on model output, also called automation bias. The correct posture is human supervision of model judgments through domain expertise.

An important nuance the document raises: even with domain expertise, a human supervisor may lack sufficient model expertise to effectively evaluate or steer the model toward its intended objective. Domain knowledge and model knowledge are not the same. Both are needed for effective human oversight.

### Information Integrity

Not to be confused with data integrity. Information integrity focuses on the models output and its real-world impact, specifically the models capacity to amplify, generate, and propagate misinformation and propaganda.

The risk is not just that misinformation exists but that the model generates it at scale, with apparent confidence, and with perceived accuracy. Disinformation has already been amplified by current models, and not only in text. AI-generated images, audio, and video extend the surface area considerably.

### Information Security

Two distinct threats sit under this category.

First, generative AI as an offensive tool: scanning code for vulnerabilities, writing custom exploits, planning and executing attacks, running personalized social engineering campaigns at scale.

Second, generative AI as a target: models themselves can be attacked through prompt injection, jailbreaking, and indirect injection to manipulate behavior, extract sensitive data, or cause unintended actions.

Both directions are active and in use today.

### Intellectual Property

Generative AI may reproduce copyrighted material including trade secrets, trademarked content, and proprietary code due to memorization during training.

A concrete example: code on platforms like GitHub may be open source but that does not make it public domain. If a model memorizes GPL-licensed code and reproduces it in a startups proprietary product, that startup may be legally compelled through a lawsuit to make their entire product open source. The consequences are not theoretical. They are already being litigated.

### Obscene, Degrading, and Abusive Content

Before generative AI, producing high-fidelity synthetic media required significant skill and time. That bottleneck no longer exists. Users are now one interaction away from accessing or generating this content.

Recalling the multiplicity criteria from the core RMF: what one person considers harmful another may not with respect to the same content. While that tension exists, certain content is generally considered unacceptable regardless of perspective, and the provider of an AI system carries a moral obligation to address it. The clearest example is Child Sexual Abuse Material (CSAM).

### Toxicity, Bias, and Homogenization

Toxicity refers to the models capacity to generate hate speech, harassment, profanity, or content that promotes harm. Models trained on vast internet data absorb toxicity as part of that data.

Bias is the amplification of historical, cultural, and systemic prejudice and the reinforcement of harmful stereotypes. Same root cause: training data reflects the world as it is, not as it should be.

Homogenization is a risk that receives less attention than it deserves. The concern is that we may be approaching a phase where AI-generated content dominates the data landscape and models are subsequently trained on that AI-generated content. Codes, blogs, articles, documentation: if the training corpus becomes predominantly synthetic, models progressively lose diversity of thought, voice, and perspective. The feedback loop compounds.

### Value Chain and Component Integration

The OWASP LLM Top 10 equivalent is LLM03, Supply Chain Vulnerability. In any generative AI system, the value chain typically includes data vendors with unverified data, pretrained models, fine-tuning pipelines, and third-party plugins.

In practice, you are rarely building AI from scratch. You are stacking dependencies on dependencies. If any single dependency becomes faulty or gets compromised, the impact propagates through the entire system. The weakness does not need to be in your code. It only needs to be somewhere in your dependency chain.

---

## NIST AI 600-1 to OWASP LLM Top 10 Mapping

| NIST AI 600-1 Risk | OWASP LLM Top 10 Equivalent |
|---|---|
| Confabulation | LLM09 - Misinformation |
| Data Privacy | LLM02 - Sensitive Information Disclosure, LLM05 - Improper Output Handling |
| Human-AI Configuration | LLM09 - Misinformation |
| Obscene, Degrading Content | LLM04 - Data and Model Poisoning |
| Value Chain and Component Integration | LLM03 - Supply Chain |
| Information Security | LLM01 - Prompt Injection |
| CBRN Information | No direct OWASP equivalent - gap |
| Environmental | No direct OWASP equivalent - out of scope for red team |
| Toxicity, Bias, Homogenization | No direct OWASP equivalent - gap |
| Information Integrity | Partial - LLM09, but NIST frames it broader |
| Intellectual Property | No direct OWASP equivalent - gap |

NIST AI 600-1 covers several risk categories with no direct OWASP LLM Top 10 equivalent: CBRN, environmental impact, intellectual property, and homogenization. These are policy and societal concerns that sit outside the scope of a standard AI red team engagement. Worth knowing for client conversations at the governance level.

---

## Key Extractions for My Practice

- The value chain risk reinforces the supply chain section of my OWASP-ATLAS cross-map. Every dependency is a potential attack vector. Clients building on third-party models, plugins, or data vendors inherit that risk whether they acknowledge it or not.
- The human-AI configuration risk connects directly to Excessive Agency findings (OWASP LLM06). Overreliance on model output without human oversight is both a safety risk and a security risk. They are not separate concerns.
- The information integrity framing is relevant for clients in media, finance, and healthcare where model-generated content feeds downstream systems or public-facing channels. In those sectors, scope engagements to include information integrity testing, not just prompt injection and application-layer bugs.
- The CBRN risk category signals that certain regulated industries such as defense, pharma, and biotech will have AI red team requirements that go beyond what standard OWASP and MITRE frameworks cover. 600-1 is the document to reference when working in those sectors.
- Intellectual property risk is the one category where a finding could produce legal liability for the client, not just reputational or security liability. Worth flagging as a separate risk category in engagement reports for clients deploying AI in content-generation or code-generation use cases.
