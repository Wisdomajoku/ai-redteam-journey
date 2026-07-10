# Attack Surface Mapping

## Overview

This document records the attack surface identified during reconnaissance of the FinanceTrack Assistant application.

The purpose of this phase is to identify components, interfaces, and data flows that require security testing.

This document describes observed exposure points only. Security impact and exploitability are assessed during later testing phases.

## User Interaction Surface

### Chat Input

Location:

```text
Streamlit chat interface
```

Description:

The user provides natural language input through the application chat interface.

Observed behavior:

* User input is transmitted through the application's WebSocket communication channel.
* The message is processed by the LangChain agent workflow.

Security testing relevance:

The chat input represents the primary user-controlled input entering the AI agent.

Areas for assessment:

* Prompt injection resistance
* Instruction manipulation
* Agent behavior under adversarial input

## Communication Surface

### Streamlit WebSocket Channel

Observed communication path:

```text
/_stcore/stream
```

Description:

The WebSocket channel was observed carrying application interaction data.

Observed data types:

* User messages
* Agent action messages
* Tool execution information
* Final responses

Security testing relevance:

The communication channel provides visibility into the interaction between the user interface and agent workflow.

## Agent Execution Surface

### LangChain ReAct Agent

Observed component:

```text
LangChain ReAct agent
```

Description:

The application uses an agent workflow where the model selects actions and interacts with available tools.

Observed execution pattern:

```text
User Input
    |
    v
Agent Processing
    |
    v
Tool Selection
    |
    v
Tool Response
    |
    v
Final Answer
```

Security testing relevance:

The agent decision-making layer requires assessment for unintended actions and unsafe tool usage.

## Tool Interface Surface

Two agent tools were observed during reconnaissance.

### GetCurrentUser

Observed action:

```json
{
    "action": "GetCurrentUser",
    "action_input": ""
}
```

Purpose:

Retrieves current user information.

Security testing relevance:

The handling of identity information and agent interaction with this tool requires assessment.

---

### GetUserTransactions

Observed action:

```json
{
    "action": "GetUserTransactions",
    "action_input": "1"
}
```

Purpose:

Retrieves transaction information associated with a user identifier.

Security testing relevance:

The interaction between agent-selected parameters and backend data access requires assessment.

## Model Interface Surface

Observed components:

```text
LangChain Agent
        |
        v
LiteLLM
        |
        v
Groq API
```

Description:

The application uses LiteLLM as the interface between the agent framework and the language model provider.

Security testing relevance:

Model behavior will be assessed separately through model-level testing tools.

## Data Access Surface

Observed backend data component:

```text
SQLite database
```

Description:

The agent tools interact with application data stored within the database.

Security testing relevance:

Testing will evaluate whether agent-controlled actions can cause unintended data exposure or unsafe data access.

## Attack Surface Summary

| Component                | Observed Exposure              | Assessment Focus                      |
| ------------------------ | ------------------------------ | ------------------------------------- |
| Chat interface           | User-controlled prompt input   | Prompt injection testing              |
| WebSocket channel        | Application communication path | Manual traffic analysis               |
| LangChain agent          | Decision-making layer          | Agent behavior testing                |
| GetCurrentUser tool      | Agent tool interface           | Tool interaction testing              |
| GetUserTransactions tool | Data retrieval tool            | Authorization and data access testing |
| LiteLLM/Groq interface   | Model communication layer      | Model behavior assessment             |
| SQLite database          | Application data layer         | Data access validation                |

## Evidence Source

Attack surface mapping was based on:

* Burp Suite HTTP history review
* Burp WebSocket inspection
* Normal application interaction
* Observed agent action messages

