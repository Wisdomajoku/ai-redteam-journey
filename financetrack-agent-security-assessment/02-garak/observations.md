# Garak Observations

## Assessment Summary

The automated assessment covered multiple probe families selected to establish a baseline of the model's behavior before targeted adversarial testing.

Completed probe families:

* Prompt Injection
* System Prompt Extraction

A DAN probe was initiated but not completed because of provider token limits during execution.

## Prompt Injection

The prompt injection assessment completed successfully and produced measurable responses across the supplied prompts.

The generated report and execution logs have been retained as assessment evidence. Detailed interpretation of these results is deferred until they can be compared with targeted PyRIT testing and manual validation.

## System Prompt Extraction

The system prompt extraction assessment completed successfully.

The probe attempted multiple prompt variations designed to elicit system prompt disclosure. Execution artifacts, logs, and generated reports have been retained for later analysis alongside evidence collected during the manual assessment phase.

## Operational Observations

Provider rate limits had a direct impact on assessment planning.

Probe families varied significantly in execution time and token consumption. Rather than executing multiple probe families in a single session, each family was run independently with a single generation per prompt.

This approach reduced unnecessary token consumption, simplified result review, and allowed testing to continue across multiple assessment sessions.

## Evidence

Supporting evidence for this phase includes:

* Garak JSONL reports
* Terminal execution logs
* Execution screenshots
* Provider usage observations recorded during testing

