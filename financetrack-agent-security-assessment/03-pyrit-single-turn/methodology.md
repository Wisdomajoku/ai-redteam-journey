# PyRIT Single-Turn Methodology

## Objective

The purpose of this phase was to validate specific security hypotheses identified during reconnaissance and the Garak assessment. Rather than testing random prompts, each test case was created from observations made during earlier phases of the engagement.

This phase focused on model-layer behavior. Application-layer verification was reserved for the manual testing phase.

## Why PyRIT

Garak provided a broad assessment of the model and identified areas that deserved further investigation. PyRIT was then used to perform focused validation against those areas.

The goal was to determine whether the model would exhibit the behaviors suggested by the earlier assessment when presented with targeted inputs.

## Test Case Selection

Test cases were selected from evidence gathered during previous phases.

Reconnaissance identified:

* The chat interface as the primary user input.
* The tool workflow used by the agent.
* The trust relationship between the model and tool outputs.
* The exposed database schema within the application.

The Garak assessment identified:

* High susceptibility to prompt injection.
* Moderate susceptibility to system prompt extraction.

These observations were converted into targeted single-turn test cases. Each case was linked to a specific security objective instead of being written as a standalone jailbreak prompt.

## Assessment Approach

Each test case was executed independently using PyRIT's `PromptSendingAttack`.

A fresh interaction was used for every test. Previous conversations were not reused. This ensured that the outcome of one test could not influence another.

The engagement focused on one prompt and one model response for each assessment case.

## Scoring

PyRIT's `SelfAskTrueFalseScorer` was used as the evaluation method.

The scorer acted as an LLM judge. After each response, it evaluated whether the model achieved the attack objective.

The scorer was used to provide a consistent evaluation across all assessment cases. Final conclusions were not based only on the scorer output. Responses were also reviewed manually during analysis.

## Scope

This phase evaluated model behavior only.

The assessment did not interact directly with the deployed application or its backend components.

Manual verification against the running application was planned as a separate phase using Burp Suite.

## Limitations

The target for this phase was the language model.

Because the deployed application communicates through WebSockets, the application itself was not tested directly during this phase.

Results from this assessment were treated as validation signals for later manual verification rather than confirmed application vulnerabilities.
