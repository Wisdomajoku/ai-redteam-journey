# Google Secure AI Framework (SAIF) — Reading Notes

*Reading completed: May 21, 2026. Source: saif.google/secure-ai-framework*

---

## Overview

The Google Secure AI Framework (SAIF) is a framework that seeks to mitigate risk around AI systems - model theft, training data poisoning, prompt injection, and related threats. As AI keeps getting integrated into products globally, there is a natural evolutionary logic to calling for an objective, clear, and responsible framework. Hence SAIF.

---

## The Six Core Elements of SAIF

### 1. Expand Strong Security Foundations to the AI Ecosystem

AI is growing fast and there is a natural need to keep pace — particularly through organizational expertise. The practical implication is to expand traditional red teaming to include AI red teaming, so that you are actively attempting to circumvent or break through guardrails.

By "ecosystem," Google was not talking about just the AI model alone but also the applications and the users — the downstream components as well. The model should be treated as an extension of the application stack, which automatically means new attack vectors emerge from that framing.

### 2. Extend Detection and Response to Bring AI Into an Organization's Threat Universe

Just as most organizations have some form of monitoring or monitoring teams, that arrangement must be extended to AI. Fast detection and response is a known priority in cybersecurity. The same applies to AI. For some organizations this involves monitoring inputs and outputs to detect anomalies — a direct parallel to traditional SOC operations.

### 3. Automate Defenses to Keep Pace with Existing and New Threats

The irony here is that attackers often use AI to prepare and execute their attacks, making those attacks highly effective with high accuracy. Red teamers can capitalize on the same advancement in AI to fight back, effectively protecting and defending against such attacks. The arms race is symmetric.

### 4. Harmonize Platform-Level Controls to Ensure Consistent Security Across the Organization

To scale AI security effectively, you must move away from per-application security patches and toward centralized, platform-level governance. The goal is to provide developers with secure-by-default guardrails so they do not have to build security from scratch for every deployment.

### 5. Adapt Controls to Adjust Mitigations and Create Faster Feedback Loops for AI Deployment

Instead of making the AI rigid or static, adopt a dynamic approach that prioritizes evolution and improvement based on factors such as past incidents. Since the threat landscape keeps changing, the AI must also change — fine-tuned where and when necessary to get progressively hardened.

### 6. Contextualize AI System Risks in Surrounding Business Processes

Organizations must carry out operational assessments to gain clear insight into what their organizational risk looks like when they deploy AI, so that insight informs decisions. Organizations should also develop systems to monitor AI performance. Key areas to watch include hallucination, forced relationships, and other output quality concerns that carry downstream business risk.

---

## SAIF Risk Map

Just as traditional software development has code, infrastructure, and application components, AI has four components: **Data, Infrastructure, Model, and Application**. These are useful in several ways but in a security context, their primary value is in mapping vulnerabilities and attack vectors. Instead of treating the model as a black box, identify the vulnerability or vector and locate where it falls within the components.

An important property of this map: it is not rigid or static. It is highly dynamic. Every mapping can be treated with context, which means a single vector or vulnerability can appear in multiple components depending on the context.

---

## Data Components

AI models are not static. They are highly dynamic in operation, relying on user input, code, and learned parameters encoded internally as weights. There are three main data components in the SAIF Risk Map:

**Data Sources**

Where data is curated or gathered from. This is critical because of the possibility of data and model poisoning - as mapped in the OWASP LLM Top 10. Trusted data sources matter seriously. The quality of the data is equally important.

**Data Filtering and Processing**

Raw data is not used as-is. It must be filtered and processed to determine its suitability and quality. Data also needs to be labeled. Since there are various data types and sources, incomplete data can be addressed during this processing phase.

**Training Data**

What remains after filtering and processing becomes the training data. The output of the model is a direct function of what goes in here.

---

## Infrastructure Components

Infrastructure components include data storage, development platforms, and deployment platforms. Attackers do not always target the model directly - they sometimes target the platforms. Compromise the platforms and you may gain access to proprietary data including model source code, processes, and more. Traditional security practices are implemented at this layer: authentication, authorization, access control, MFA, and so on.

Key risks found here:

**Model Framework and Code**

The code and framework used in the training and use of the model. Two distinct code types exist here:
- **Model code** - defines the model architecture, number of layers, and layer types
- **Framework code** - used for training and for making inferences or predictions

**Training, Tuning, and Evaluation**

- **Training** - the process of teaching a model how to make inferences and extract correct patterns by iterating the likelihood of an outcome
- **Tuning** - adjusting or optimizing a model's hyperparameters for a specific task; also spans Parameter Efficient Fine Tuning (PEFT)
- **Evaluation** - testing the model's final outcome to determine whether objectives were met

**Data and Model Storage**

Concerned with confidentiality and integrity. This layer must be treated as distinct. If training data is poisoned, the output becomes equally compromised - and this is difficult to detect since the model still functions normally, only incorrectly or with hidden bias.

Model weight confidentiality is critical. Weights are the crown jewels. If a malicious actor exfiltrates weights from storage, they can prepare attacks against a model without ever touching it - simply by studying and testing the stolen weights locally.

**Model Serving**

When a model is live, risk shifts to the infrastructure and execution environment. Infrastructure attacks at this layer include model denial of service and API/endpoint hijacking. Mitigations include rate limiting, authentication, and proper access controls.

---

## Model Components

The central component of the AI application.

**The Model**

A set of software algorithms paired with learned numerical weights derived from training data. The model is the core artifact produced by the integration of the data and infrastructure layers. It produces no utility until it is paired with the application layer.

**Input Handling**

Includes filters and sanitizers for inputs. Directly parallel to the OWASP LLM Top 10 improper input handling category. This component acts as a wedge against various input-based attacks, especially prompt injection.

**Output Handling**

The output-side equivalent of input handling - concerned with model responses. Without proper output handling, there is significant risk that the AI produces harmful responses. This maps to OWASP LLM05 - Improper Output Handling.

---

## Application Components

Unlike traditional software which uses structured searches, AI accepts unstructured input in the form of natural language. This shifts risk to the semantic layer - prompt engineering, context manipulation, and related vectors. The ability to accept unstructured input is defined by the application component.

**Application**

The product or service the AI is integrated into. A common example is a customer service chatbot.

**Agent (Tool Use)**

The external software, APIs, plugins, or services that the AI model calls to perform specific tasks. Each integration adds new attack surface area, as the model's reasoning capability now directly controls external system functions. This maps directly to OWASP LLM06 - Excessive Agency, and is a primary area of focus in agentic system red teaming.

---

## Key Extractions for My Practice

- SAIF treats the model as one layer within a broader stack - not the whole target. Application and infrastructure layers are equally in scope.
- The four-component breakdown (Data, Infrastructure, Model, Application) gives a clean mental model for mapping where any given finding lives - useful for structuring engagement reports and scoping conversations.
- The emphasis on platform-level controls (Element 4) aligns with what I already highlight to clients: per-application patching is not a sustainable security posture for organizations deploying AI at scale.
- Model weight confidentiality is underemphasized in most AI red team frameworks. SAIF naming it explicitly as a crown-jewels concern is worth referencing in client conversations.
- The agent/tool use component in SAIF maps directly to where my most valuable application-layer findings tend to live - tool call manipulation, excessive agency, and authorization failures on external API integrations.
