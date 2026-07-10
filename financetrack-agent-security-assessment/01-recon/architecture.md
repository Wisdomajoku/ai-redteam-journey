# Application Architecture

## Overview

During reconnaissance, the FinanceTrack Assistant application architecture was mapped through browser traffic inspection and WebSocket analysis.

The application consists of a Streamlit frontend connected to a LangChain-based AI agent. The agent uses available tools to retrieve application data and communicates with the underlying language model through LiteLLM.

## Identified Technology Stack

| Component             | Technology               |
| --------------------- | ------------------------ |
| Frontend              | Streamlit 1.58.0         |
| Backend Server        | Starlette-managed server |
| Agent Framework       | LangChain                |
| Agent Type            | ReAct Agent              |
| LLM Interface         | LiteLLM                  |
| Model Provider        | Groq                     |
| Model                 | llama-3.3-70b-versatile  |
| Database              | SQLite                   |
| Runtime               | Python 3.12.9            |
| Communication Channel | WebSocket                |

## High-Level Architecture

Observed application flow:

```text
User Browser
     |
     |
     v
Streamlit Web Interface
     |
     |
     v
WebSocket Communication
/_stcore/stream
     |
     |
     v
LangChain ReAct Agent
     |
     |
     +----------------+
     |                |
     v                v
 LiteLLM          Agent Tools
     |                |
     v                |
 Groq LLM            |
                      |
                      v
              SQLite Database
```

## Agent Execution Flow

A normal transaction request followed the sequence below:

```text
1. User submits request:
   
   "What are my recent transactions?"


2. Request is transmitted through WebSocket


3. LangChain ReAct agent processes the request


4. Agent invokes available tools


5. Tool responses are returned to the agent


6. Agent generates final response


7. Response is returned to the user interface
```

## Identified Agent Tools

### GetCurrentUser

Purpose:

Retrieves information about the current user.

Observed invocation:

```json
{
    "action": "GetCurrentUser",
    "action_input": ""
}
```

---

### GetUserTransactions

Purpose:

Retrieves transaction information associated with a user identifier.

Observed invocation:

```json
{
    "action": "GetUserTransactions",
    "action_input": "1"
}
```

## Communication Architecture

The application does not expose a traditional REST API endpoint for chat interaction.

Instead, user interaction occurs through the Streamlit WebSocket channel:

```text
/_stcore/stream
```

The WebSocket channel carries:

* User messages
* Agent action requests
* Tool execution data
* Final responses

## Security Assessment Relevance

Understanding this architecture is required for later testing phases.

The assessment will evaluate security boundaries between:

* User-controlled input
* Agent decision-making
* Tool execution
* Data retrieval
* Model behavior

The architecture mapping provides the foundation for identifying where controls should exist and where weaknesses may occur.

