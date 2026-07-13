# Microsoft "Lessons from Red Teaming 100 Generative AI Products" - Reading Notes

*Reading completed: May 21, 2026. Source: Microsoft AI Red Team - "Lessons from Red Teaming 100 Generative AI Products."*

---

## Lesson 1: Understand What the System Can Do and Where It Is Applied

This is reconnaissance. The same discipline traditional security demands before any engagement — understand the system you are up against instead of blind testing or spray and pray. Microsoft's team was not making baseless assumptions but informed ones grounded in system understanding.

**The core questions to ask first:**

- What can the AI system do?
- Where is it applied?

Answering those two questions leads you to impact, which leads you to downstream effects, which gives you criticality. Criticality gives you insight into the depth of impact. Same reasoning flow as threat modeling in traditional security.

### Model Capabilities and Attack Surface

The expansion or contraction of a model's capabilities is a strong determining factor in vulnerability exposure - it widens or contracts the attack surface directly.

Example: if an AI system was designed with image-reading ability and another was not, the first becomes exposed to image-based indirect prompt injection. The second is not. Remove that capability and that is minus one attack surface.

Practical implication for engagements: if a client asks for more capabilities, respond by pointing out what that exposes and how it widens the attack surface, then assess whether the addition is worth the risk. That pre-risk assessment thinking is what separates senior practitioner reasoning from purely technical execution.

Notice the framing here: vulnerabilities arise from the capabilities chosen for the model, not immediately from flaws in methods or tools - but from the process adopted to achieve business objectives. That is business logic thinking applied to AI security.

### Downstream Applications

Downstream application means taking a trained base model and narrowing it by deploying it into a specific use case, sometimes through fine-tuning (PEFT, LoRA, etc.). The impact on downstream use cases cannot be fully or conclusively assessed at the base model level.

Example: the same model used for text-based research can also be used to run a phishing campaign by a malicious actor. One model, multiple uses - legitimate use and misuse. This is a significant gap in how we currently evaluate AI system risk.

---

## Lesson 2: You Don't Have to Compute Gradients to Break an AI System

Microsoft reinforces a position many in security have always held: the simplest attacks are often the most effective. Complexity does not automatically equal effectiveness.

Gradient-based attacks are common in ML research. The team found that for subverting guardrails, prompt injection was highly effective - no complex gradient-based approach required.

My take: method selection within this context should be progressive. Start simple. Move up in complexity only when simple approaches fail. Complexity is a tool, not a default.

### System-Level Perspective

Focusing purely on the model because of the label "AI red teaming" is self-defeating if you fail to consider the systems surrounding the model. Depending on the architectural makeup of the surrounding system, that architecture may be more susceptible to attack than the model itself. This is why Microsoft's operations focused on end-to-end systems, not models in isolation.

---

## Lesson 3: AI Red Teaming Is Not Safety Benchmarking

The output of an AI red team exercise at any point in time does not constitute a benchmark. Continuous testing is the standard since systems are evolving, threat landscapes are evolving, and complexity is increasing. Crucially, the increasing complexity of the AI landscape does not diminish the effectiveness of simple approaches - but it does mean the overall risk and threat surface is not simple.

### Novel Harm Categories

As models advance, they improve operationally but simultaneously introduce vulnerabilities that are not yet understood. We cannot rely on existing safety benchmarks because they are based on current known data. What we do not yet know is where the next harm category will emerge.

### Context-Specific Risks

No single safety benchmark adequately covers every model or every dataset. The team called out the impracticality of applying one benchmark generically. My read: dataset quality matters enormously. The output of a model is largely a function of its training data. Using the same safety benchmark for a model trained on image datasets as for one trained purely on text is logically unsound. Contextualisation over generalisation is the right posture.

---

## Lesson 4: Automation Can Help Cover More of the Risk Landscape

The increasing challenge of securing the AI landscape led Microsoft to build PyRIT.

### Testing at Scale

Before PyRIT, attack strategies were fragmented, lacked efficiency, and produced limited coverage. PyRIT provides access to a range of attack strategies including Crescendo, various converters, and scorers for multi-modal outputs - structured and composable.

### Tools and Weapons

A tool is whatever its user makes it. AI models follow the same logic: in the hands of a malicious actor they become dangerous; in the hands of a legitimate user they are used as intended. The more advanced the model, the greater the potential danger in misuse. Capability expansion serves both legitimate users and adversarial ones.

---

## Lesson 5: The Human Element of AI Red Teaming Is Crucial

Tools like PyRIT increase efficiency and coverage. They do not replace the human layer. AI red teaming is fundamentally human-centric.

### Subject Matter Expertise

Even a capable tool like PyRIT lacks domain knowledge to accurately evaluate a model in a specific context. Functional testing alone is insufficient. A medical AI chatbot can be tested for safe-word patterns - but evaluating whether a response is genuinely harmful in a medical context requires someone with medical domain knowledge.

### Cultural Competence

Most AI models are trained on Western data, which is not a true representation of global demographics. The team acknowledged this directly and noted that model developers are actively working to train with other languages and cultural contexts. Implication for my engagements: applying a US-centric harm evaluation lens to an AI system deployed in Lagos, Nigeria may miss entirely different categories of cultural harm or misuse. This is a gap I can position specifically.

### Emotional Intelligence

The impact of a model's response can only be fully evaluated by humans - the effect on the user, the multiple possible interpretations, the emotional weight of certain outputs. No automation captures this. Since human interactions with AI systems are dynamic and effectively limitless, no single operator or set of operators can evaluate the full range. The scope of human impact is practically unbounded.

---

## Lesson 6: Responsible AI Harms Are Pervasive but Difficult to Measure

Responsible AI means building and deploying AI systems that do what we want them to do, fairly and safely, without causing harm. The core difficulty in measuring responsible AI harm is that harm is highly subjective - developing a singular benchmark for it is practically impossible.

### Adversarial vs Benign Actors

Two distinct actor types produce RAI violations:

- **Adversarial/malicious actors** - intentionally subverting the model's safety mechanisms using deliberate techniques
- **Benign users** - unintentionally triggering violations through ordinary interaction, with no intent to subvert guardrails

Both produce harm. Only one is intentional. This distinction matters for how you scope an engagement: purely adversarial testing misses the benign-user harm category entirely.

### RAI Probing and Scoring

Due to the probabilistic nature of generative AI, even if a malicious prompt is fed into a model, the timing and conditions under which it will trigger are unknown. This is a significant gap in current AI security practice. Current approaches involve curating large datasets and analyzing model responses. PyRIT is positioned here as a combination of manual and automated testing to address this at scale.

---

## Lesson 7: LLMs Amplify Existing Security Risks and Introduce New Ones

### Application Security Is Often Ignored

While attention in AI security focuses heavily on model-level concerns, the team highlighted how application security is routinely neglected. Familiar vulnerabilities persist in AI-backed applications: improper input/output sanitization, improper error handling, outdated dependencies. These are not new problems - they are old problems that the excitement around AI has caused practitioners to overlook.

### Model-Level Weaknesses

Capability expansion widens attack surface. A RAG system automatically introduces default vulnerabilities - indirect prompt injection being one of the most significant. Even if system-level and model-level security are both implemented, never assume the model is safe. AI safety practices become an additional defensive layer, not a substitute for the other layers.

---

## Lesson 8: The Work of Securing AI Systems Will Never Be Complete

Security and safety in this field is an ongoing, evolving process. The team challenged what they described as inadequate framing - treating AI vulnerabilities purely as technical problems. They proposed three additional lenses.

### Economics of Cybersecurity

No system is foolproof. Even with the best standards, methods, tools, and practices applied, you secure only with respect to what is currently known. In the unknown lies likelihood and vulnerability. The operational goal of cybersecurity is to make exploitation so expensive that the cost outweighs the benefit. When you consider prompt injection and its variations, we are far from achieving that objective at the AI application layer.

### Break-Fix Cycles

The break-fix cycle is a forward simulation of offensives - simulate attacks, implement mitigations discovered through that process, repeat. The aim is to make the system increasingly difficult to break. Important trade-off: if you operate purely offensively without considering what mitigations introduce as new risk, you may fix one surface while opening another. No system has zero vulnerabilities.

### Policy and Regulation

Regulations are useful but do not completely solve the problem. Regulating AI is difficult because governments must balance safety requirements against not stifling innovation. The EU AI Act is the clearest current example of regulatory framing with consequences. Clear consequences introduce deterrence. However, regulation addresses what is known and declared - it does not address what is not yet understood.

---

## Key Extractions for My Practice

### Attack Surface Framing

- New harm categories increase attack surface
- Expanding model capabilities increases attack surface
- Contracting model capabilities decreases attack surface
- Complex architecture increases attack surface
- Simple architecture decreases attack surface

This maps directly to traditional security's principle of minimizing attack surface. The framing is the same; the application is new.

### Capability Expansion Conversation with Clients

If a client wants to add model capabilities, always surface the associated risk clearly. Explain what the addition exposes. Assess whether it is worth it. This is a pre-risk assessment conversation, not just a technical observation. It shows senior reasoning and earns trust.

### Harm vs Vulnerability

**Harm** = the negative impact arising not only from vulnerabilities but from the use or misuse of AI. Harm is the potential for a model's output to negatively affect deployers of the AI system, users, or third parties. Examples: racist outputs, medically inappropriate advice, facilitation of fraud. Harm is not limited to deployers but extends to the broader system and its users.

**Vulnerability** = the weakness in an AI system that risks exploitation.

Harm is broader than vulnerability. A model with no exploitable vulnerabilities can still produce harm through misuse by a benign user. Both categories require testing. Only one maps cleanly to traditional penetration testing methodology.
