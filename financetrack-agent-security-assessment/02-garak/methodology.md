# Garak Methodology

## Objective

Establish a baseline understanding of the model's security posture before targeted adversarial testing. The automated assessment was used to identify behaviors that warranted further investigation during the manual and PyRIT phases of the engagement.

## Assessment Approach

The assessment was performed with NVIDIA Garak against the language model configured for the FinanceTrack Assistant. Testing focused on representative probe families rather than exhaustive coverage. This approach provided broad visibility while remaining within the operational limits of the model provider.

Each probe family was executed independently with a single generation per prompt. Running probes separately reduced execution time, simplified result analysis, and limited the impact of provider rate limits on the assessment.

The assessment included:

* Prompt injection
* System prompt extraction
* Targeted evaluation of a DAN probe

Probe selection was based on their relevance to the application's threat model and the assessment objectives defined during engagement planning.

## Operational Constraints

The assessment was conducted against a hosted model with provider-enforced limits on requests and token consumption. These limits affected execution time and prevented continuous large-scale automated testing.

Rather than repeatedly exhausting the available quota, testing was spread across multiple sessions. This allowed each completed probe family to be reviewed before moving to the next phase of the engagement.

This decision prioritized efficient use of the available testing window while maintaining sufficient coverage for a baseline assessment.

## Result Interpretation

Garak output was treated as an indicator for further investigation rather than a confirmed security finding.

Automated probe results were evaluated alongside application behavior, manual verification, and targeted PyRIT testing before any security conclusion was reached.

Findings reported at the end of this engagement are based on correlated evidence from multiple assessment activities rather than on automated tool output alone.

