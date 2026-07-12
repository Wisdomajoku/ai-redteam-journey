# Garak Observations

## Assessment Summary

The Garak assessment was conducted as an initial baseline evaluation of the FinanceTrack Assistant model behavior.

Testing focused on selected probe families related to prompt manipulation and model instruction handling.

Completed probe families:

* Prompt Injection
* System Prompt Extraction

A DAN probe was initiated but not completed during the assessment window due to increased token consumption and execution time under provider-imposed limits.

## Prompt Injection Observation

The prompt injection assessment was completed.

The probe generated responses that were recorded in the Garak reports and supporting artifacts.

The results require further review against application behavior and targeted testing performed during later engagement phases.

Artifacts collected:

* Garak JSONL report
* Garak HTML report
* Garak hit log
* Execution screenshots

## System Prompt Extraction Observation

The system prompt extraction assessment was completed.

The probe evaluated whether adversarial prompts could influence the model into disclosing information associated with system-level instructions.

Execution results were captured through Garak output files and retained as assessment evidence.

Further analysis will be performed alongside PyRIT testing and manual verification.

Artifacts collected:

* Garak JSONL report
* Garak HTML report
* Garak hit log
* Execution screenshots

## DAN Probe Observation

A DAN probe was executed as part of the baseline assessment.

The scan progressed but required significantly more execution time and token consumption compared with other probe families. The assessment was stopped before completion due to provider-imposed usage constraints and execution time considerations.

No conclusion was drawn from the incomplete run.

## Assessment Notes

Garak results are treated as indicators for further investigation.

The automated output identifies model behaviors that require validation but does not independently establish the presence or severity of a security issue.

Final conclusions will be based on correlation between:

* Automated assessment results
* PyRIT adversarial testing
* Manual verification
* Application behavior analysis
* Collected evidence
