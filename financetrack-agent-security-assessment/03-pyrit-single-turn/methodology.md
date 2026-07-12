# PyRIT Single Turn Methodology

## Objective

Perform targeted adversarial testing against the FinanceTrack Assistant using Microsoft PyRIT.

This phase moves beyond automated baseline scanning by testing specific security objectives against the application and model interaction flow.

## Assessment Approach

Single-turn attacks were used to evaluate how the application responds to individual adversarial objectives.

Each test was designed around a defined objective rather than a broad probe category. This allowed individual behaviors to be isolated, reviewed, and reproduced.

Testing objectives included:

* Attempting to identify available agent capabilities.
* Attempting to influence the agent into revealing restricted information.
* Evaluating resistance to adversarial instructions.
* Testing instruction-following boundaries.

## Attack Execution

Each objective was submitted as an independent attack.

The objective, conversation identifier, model response, and scoring result were retained as part of the assessment record.

The testing focused on the interaction between the user input, the agent behavior, and the resulting model response.

## Scoring and Validation

PyRIT scoring was used to assist with evaluating whether an attack objective was achieved.

Scoring results were treated as supporting evidence and not as standalone confirmation of a vulnerability.

Successful attack objectives required additional review against:

* Application behavior.
* Authorization boundaries.
* Business impact.
* Manual verification evidence.

## Result Interpretation

PyRIT results represent targeted test outcomes.

A successful adversarial interaction does not automatically represent a security finding. Findings are only reported after validating the behavior and determining its security impact within the application context.
