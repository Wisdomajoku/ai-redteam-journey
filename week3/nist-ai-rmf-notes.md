# NIST AI Risk Management Framework (AI RMF 1.0) — Reading Notes

*Reading completed: May 21, 2026. Source: NIST AI Risk Management Framework 1.0 — nist.gov/itl/ai-risk-management-framework*

---

## Overview

The AI Risk Management Framework is a structured approach for assessing, categorizing, and mitigating the challenges that arise from AI systems — model bias, model drift, hallucination, adversarial manipulation, and more. Every model has challenges and vulnerabilities arising from both use and misuse, and there is a genuine need for a uniform approach to categorization, assessment, and mitigation of these risks. One key advantage of a unified framework is that it allows for consistency in reference between users and providers.

---

## The Four Core Functions

### Govern

Govern is the foundation on which the other three pillars — Map, Measure, Manage — are built. This function ensures that risk management is embedded in an organization's culture through clearly defined policies, accountability structures, and oversight mechanisms. It operates at the policy level.

Govern requires setting clear rules and ethical standards, and assigning specific people to be responsible for AI systems across both technical and non-technical domains.

Two points the document makes explicitly worth noting:

- Risk management is a continuous process, not a one-time exercise
- Multi-disciplinary input from diverse teams is necessary when deploying AI. Diversity of perspective surfaces problems that a single viewpoint would likely miss

### Map

Map focuses on identifying and understanding the context of the AI system in order to define what risk looks like for that specific deployment. The starting point is documenting the intended use of the AI and its potential impact on users and stakeholders.

By mapping out the system's data sources, technical capabilities, expected functions, and potential interactions, an organization can with high precision anticipate its expected risk profile from each of those areas.

### Measure

Measure involves using qualitative, quantitative, or mixed methods to test and evaluate AI system performance. This includes applying technical benchmarking and AI red teaming to detect unintended behavior such as model bias, data drift, and hallucination.

This function is critical because the metrics produced from evaluation are used to compare against organizational objectives and expectations — and to determine whether further action is needed or whether the system is performing within acceptable bounds.

### Manage

During mapping and measuring, risks will be identified. The Manage function works to reduce those risks by prioritizing what requires immediate attention, implementing technical and operational controls, and ensuring continuous monitoring to detect new threats. The basis on which risk priority is determined flows from the Govern function — the policies and accountability structures set at the governance level inform what gets fixed first.

---

## AI Risk and Trustworthiness

The document opens with a foundational claim: if AI is to be considered trustworthy, it must be responsive to a multiplicity of criteria that are of value to interested parties.

By multiplicity, it means multiple, sometimes competing criteria. A model may be considered safe from the perspective of a developer but unfair from the perspective of a regular user. A single model interacts with many users carrying varying perspectives and life circumstances. To some that model is safe; to others it is not.

NIST explicitly acknowledges that the full trustworthiness list cannot always be entirely fulfilled — the goal is to find a balance depending on the specific context of use. Context of use means the specific environment, circumstances, and intended purpose. An AI recommending movies will fulfill a different and likely larger proportion of the trustworthiness criteria than an AI running medical diagnostics. Neither is expected to be perfect; both are expected to be contextually appropriate.

### Trustworthiness Attributes

**Valid and Reliable**

Validation is the confirmation, through objective evidence, that the requirements for a specific intended use have been fulfilled (ISO 9000:2015). Absence of this is considered critical and reduces trustworthiness.

Reliability is the ability of an item to perform as required, without failure, for a given time interval, under given conditions (ISO/IEC TS 5723:2022).

Accuracy is the closeness of results of observations, computations, or estimates to the true values or values accepted as being true (ISO/IEC TS 5723:2022).

Robustness or generalizability is the ability of a system to maintain its level of performance under a variety of circumstances (ISO/IEC TS 5723:2022).

**Safe**

AI systems should not, under defined conditions, lead to a state in which human life, health, property, or the environment is endangered (ISO/IEC TS 5723:2022).

**Secure and Resilient**

AI systems and the ecosystems in which they are deployed may be considered resilient if they can withstand unexpected adverse events or unexpected changes in their environment or use — or if they can maintain their functions and structure in the face of internal and external change, and degrade safely and gracefully when necessary (Adapted from ISO/IEC TS 5723:2022).

**Accountable and Transparent**

Trustworthy AI depends on accountability. Accountability presupposes transparency. Transparency reflects the extent to which information about an AI system and its outputs is available to individuals interacting with the system — regardless of whether they are even aware that they are doing so. Meaningful transparency provides access to appropriate levels of information based on the stage of the AI lifecycle and tailored to the role or knowledge of the individuals interacting with or using the system.

**Explainable and Interpretable**

Explainability refers to a representation of the mechanisms underlying AI systems' operation. Interpretability refers to the meaning of AI systems' output in the context of their designed functional purposes. Together, they assist those operating, overseeing, or using an AI system to gain deeper insights into its functionality and trustworthiness, including its outputs.

**Privacy-Enhanced**

Privacy refers generally to the norms and practices that help safeguard human autonomy, identity, and dignity. Privacy-enhancing technologies (PETs) for AI, as well as data-minimizing methods such as de-identification and aggregation for certain model outputs, can support the design of privacy-enhanced AI systems.

**Fair — With Harmful Bias Managed**

The document acknowledges that bias cannot be eliminated, only managed. Bias is often baked into societal norms and data — the goal is not complete elimination but identification and mitigation. What one person considers bias may be acceptable to another. Dynamic human perspectives make this a moving target, not a solved problem.

---

## How Risk Is Categorized

### Harm to People

Harm at the individual level includes harm to rights and civil liberties, discrimination at the personal, group, or community level, and broader societal harm. Example: an individual denied a loan due to a faulty model decision. The harm is personal, traceable, and often invisible until the affected party challenges it.

### Harm to an Organization

Risk extends beyond individuals to organizations through security breaches, reputational damage, and operational disruption. These harms have ripple effects — among them, loss of customer trust. Organizational harm often aggregates individual harms and amplifies them.

### Harm to the Ecosystem

Harm to interconnected and interdependent systems — the global financial market, supply chains, critical infrastructure. The scale here is macro. When you aggregate multiple affected micro or fragmented units, you arrive at a whole whose impact is greater than the sum of its parts. If the global financial system is affected, the devastation ripples from the macro level down to every micro unit that depends on it.

---

## Key Extractions for My Practice

- The four functions give me a clean vocabulary for conversations with regulated-industry clients. My engagement work feeds directly into their Map and Measure functions — I produce the evidence they need for those activities.
- The trustworthiness attributes are useful for framing findings in client reports. Any finding I surface can be mapped to the specific trustworthiness attribute it threatens: a prompt injection that leaks PII threatens Privacy-Enhanced. A model that produces discriminatory outputs threatens Fairness. This framing lands better with compliance teams than raw CVSS scores.
- NIST's explicit acknowledgment that trustworthiness criteria cannot all be fully met simultaneously is useful for client expectation-setting. It validates a risk-based prioritization approach rather than a "secure everything completely" posture that no organization can achieve.
- The three-tier harm categorization (people, organization, ecosystem) maps well to severity rubrics in engagement reports. A finding that threatens individual PII is harm to people. A finding that could expose proprietary model weights is harm to the organization. A finding in a widely-deployed financial AI is potentially harm to the ecosystem.
