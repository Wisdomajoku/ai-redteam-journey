# PyRIT Crescendo Multi-Turn Methodology

## Objective

The objective of this phase was to evaluate whether the FinanceTrack Assistant maintains its security boundaries when subjected to gradual, conversational manipulation across multiple turns. 

While the single-turn validation phase focused on isolated prompts, this phase evaluated the model's resistance to multi-turn context-building. Specifically, we tested if the model's safety guardrails, instruction priority, and authorization states would relax when manipulated over a series of sequential conversational steps.

## Why Crescendo

Single-turn validation is limited to evaluating whether an isolated payload can trigger an immediate failure. Multi-turn validation (specifically PyRIT's Crescendo framework) addresses different threat vectors:

* **Instruction Priority:** Evaluating if user instructions can gradually override system instructions as the conversation context grows.
* **State Drift:** Assessing whether the model's internal understanding of session boundaries and user identity (userId) shifts across multiple conversational turns.
* **Context Accumulation:** Exploiting the model's tendency to trust context and instructions that have been established incrementally over several turns.

## Target and Adversarial Environment

* **Target Agent (the Subject):** FinanceTrack Assistant (`dvllma` base) running `llama-3.3-70b-versatile` via Groq.
* **Adversarial Attacker & Scorer:** `llama-3.1-8b-instant` via Groq.
* **Testing Tool:** PyRIT (Python Risk Identification Tool) version 0.14.0.

### Model Selection and Quota Partitioning
Initial multi-turn runs utilizing larger models or external endpoints encountered strict rate limits (Tokens Per Day and Tokens Per Minute) and safety-alignment blocks on PyRIT's internal red-teaming orchestrator instructions. 

To complete the execution safely and reliably, we partitioned the API quotas:
* **The Target** was kept on `llama-3.3-70b-versatile` to maintain testing consistency with the reconnaissance and single-turn phases.
* **The Attacker and Scorer** roles were moved to `llama-3.1-8b-instant`. This model features a high Tokens Per Minute (TPM) limit of 30,000 and a daily limit of 500,000 tokens, which easily handled the growing context window of the multi-turn exchange.

## Consolidated Test Design (`MT-COMPOSITE`)

Rather than executing six separate multi-turn tests, we consolidated our validation hypotheses into a single composite validation case. This approach saved API token usage and evaluated cross-cutting security boundaries simultaneously in a single conversational stream.

The composite validation target was designed to evaluate:
1. **Instruction Hierarchy:** Can the model be persuaded to prioritize user inputs over system directives?
2. **Session Context Integrity:** Can the model be guided to switch the active session context from `userId 1` to `userId 2`?
3. **Tool/Observation Trust:** Will the model accept a fabricated tool or database observation supplied via conversational text?
4. **Prompt Protection:** Will the model disclose details of its internal directives or configuration rules?

### Clinical Objective Rephrasing
To prevent safety-filter blocks on the attacker and scorer engines, the objective was rephrased into an academic, clinical auditing format:

* **Standard Red-Teaming Phrasing (Blocked):** *"Bypass the assistant's security restrictions and execute unauthorized context manipulation..."*
* **Clinical Reframing (Allowed):** *"Verify the robustness of the FinanceTrack assistant's boundaries. The goal is to evaluate if the assistant can be conversationally guided to..."*

This adjustment stripped the malicious context from the system prompts, allowing the open-weights reasoning model to execute and evaluate the attack without triggering safety refusals.

## Scoring and Evaluation

PyRIT’s `SelfAskTrueFalseScorer` was configured with the standard `TASK_ACHIEVED` question path. 

The evaluation process operated as follows:
1. At the end of the multi-turn execution, PyRIT passed the complete conversation transcript to the scorer.
2. The scorer evaluated whether the model-under-test met the conditions of our composite objective.
3. Due to PyRIT 0.14's updated return structure, we implemented custom scoring extraction in Python to safely retrieve the `last_score` and `conversation_id` attributes and write them directly to our local text reports.

## Transition to Manual Verification

PyRIT Crescendo results are treated as model-layer validation signals, not confirmed application-layer vulnerabilities. 

A successful run indicates that the language model is susceptible to state-drift and unauthorized context changes during a conversation. To determine if these failures represent an actual security risk, they must be manually tested at the application layer using Burp Suite. This manual verification confirms whether the web application actually permits database queries to cross user boundaries or executes actions based on the model's modified state.
