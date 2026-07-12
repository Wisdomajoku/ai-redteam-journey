# Garak Methodology

## Objective

Establish a baseline understanding of the model's behavior before targeted adversarial testing. The automated assessment was used to identify behaviors that required further investigation during the PyRIT and manual verification phases of the engagement.

## Assessment Approach

The assessment was performed with NVIDIA Garak against the language model configured for the FinanceTrack Assistant.

Testing focused on selected probe families relevant to the engagement objectives and identified threat areas. The goal was to obtain broad coverage across relevant attack categories before conducting deeper targeted testing.

Each probe family was executed independently using one attack class at a time and one generation per prompt.

This approach was selected to:

* Reduce unnecessary token consumption.
* Simplify result analysis and attribution.
* Allow individual probe families to be reviewed independently.
* Maintain broader coverage across different attack categories within the available testing window.

The assessment included:

* Prompt injection
* System prompt extraction
* Targeted evaluation of a DAN probe

Probe selection was based on their relevance to the application's threat model and the assessment objectives defined during engagement planning.

## Operational Constraints

The assessment was conducted against a hosted model with provider-enforced request and token limits.

These limits affected execution time and required testing to be distributed across multiple sessions. Probe families were therefore executed separately rather than running multiple large scans in parallel.

This approach prioritized efficient use of available testing resources while maintaining sufficient coverage for the baseline assessment.

## Result Interpretation

Garak output was treated as an indicator for further investigation and not as a confirmed security finding.

Automated results were reviewed alongside application behavior, targeted PyRIT testing, and manual verification before any security conclusion was reached.

A probe result alone does not establish a vulnerability. Findings reported during this engagement are based on validated behavior supported by collected evidence.

## Evidence

Supporting evidence for this phase includes:

* Garak JSONL reports
* Garak HTML reports
* Garak hit logs
* Execution screenshots
* Provider usage observations recorded during testing
