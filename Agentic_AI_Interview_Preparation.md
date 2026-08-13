# Agentic AI --- Interview Preparation Guide

## 1. What is Agentic AI?

### Simple definition

> **Agentic AI is an AI system that can understand a goal, reason about
> what needs to be done, plan and execute multi-step tasks, use tools,
> observe results, and take further actions until the goal is
> completed.**

### Interview definition

> **Agentic AI refers to AI systems that can autonomously plan and
> execute multi-step tasks by reasoning, using tools, observing
> outcomes, and taking the next appropriate action to achieve a given
> goal.**

### Key characteristics

-   Goal-oriented
-   Reasoning
-   Planning
-   Tool usage
-   Action/execution
-   Observation and feedback
-   Memory/state
-   Adaptability
-   Autonomy
-   Guardrails and human oversight

A useful way to remember it:

``` text
Goal
  ↓
Reason
  ↓
Plan
  ↓
Use tools
  ↓
Observe results
  ↓
Reason again
  ↓
Take next action
  ↓
Goal completed
```

------------------------------------------------------------------------

# 2. Generative AI vs Agentic AI

This is one of the most important interview distinctions.

## Generative AI

Generative AI primarily focuses on **generating content** from a prompt.

Examples:

-   Generate text
-   Summarize a document
-   Generate code
-   Generate an image
-   Answer a question
-   Translate text

A simple flow is:

``` text
User Input
    ↓
   LLM
    ↓
Generated Output
```

Example:

> User: "Explain fraud detection."

Generative AI:

> "Fraud detection is the process of identifying suspicious
> transactions..."

The system mainly produces an answer.

## Agentic AI

Agentic AI focuses on **achieving a goal through reasoning, planning,
tool use, and actions**.

Example:

> User: "Investigate this suspicious transaction."

The agent might:

``` text
Receive goal
    ↓
Check transaction history
    ↓
Check customer profile
    ↓
Check location
    ↓
Run fraud model
    ↓
Search fraud policy
    ↓
Analyze evidence
    ↓
Create investigation case
    ↓
Notify fraud analyst
```

### Main difference

  -----------------------------------------------------------------------
  Generative AI                       Agentic AI
  ----------------------------------- -----------------------------------
  Primarily generates content         Pursues a goal

  Usually input → output              Goal → multiple steps → outcome

  May answer a question               Can investigate and act

  Tool use is optional                Tool use is often central

  Usually less autonomous             Can be autonomous within defined
                                      limits

  Example: summarize a report         Example: investigate an incident
                                      and create a ticket
  -----------------------------------------------------------------------

### Important point

Agentic AI often **uses Generative AI/LLMs as its reasoning engine**.

So:

> **Generative AI is about generating content; Agentic AI is about using
> AI capabilities to accomplish goals through actions.**

They are not mutually exclusive.

------------------------------------------------------------------------

# 3. AI Agent vs Agentic AI

These terms are related and are sometimes used interchangeably in
industry, but conceptually they are different.

## AI Agent

An **AI agent** is a specific software system/worker that can:

-   Receive a goal
-   Reason
-   Use tools
-   Take actions
-   Observe results
-   Continue until the task is completed

Example:

> **Fraud Investigation Agent**

``` text
Investigate transaction
        ↓
Check history
        ↓
Check location
        ↓
Run fraud model
        ↓
Create investigation case
```

## Agentic AI

**Agentic AI** is the broader paradigm/approach for building AI systems
with goal-oriented and autonomous behavior.

It may contain:

``` text
Agentic AI System
       ↓
   One or more agents
       ↓
Tools + APIs + RAG + Memory
       ↓
Enterprise systems
```

### Interview answer

> **An AI agent is an individual AI system capable of reasoning, using
> tools, and taking actions to accomplish a task. Agentic AI is the
> broader paradigm of designing AI systems with this goal-oriented and
> autonomous behavior, potentially involving one or multiple agents,
> tools, memory, RAG, and workflows.**

------------------------------------------------------------------------

# 4. How does an AI Agent actually work?

An LLM by itself does not automatically have access to company
databases, APIs, or business systems.

We give the agent **tools and capabilities**.

Think of an agent like an employee:

-   **LLM = brain**
-   **Tools = hands**
-   **Memory = notebook**
-   **Planner = planning capability**
-   **Orchestrator = manager/controller**
-   **RAG = knowledge source**
-   **Guardrails = rules**

## Basic architecture

``` text
                    AI AGENT
                       |
          ┌────────────┼────────────┐
          ↓            ↓            ↓
         LLM         TOOLS        MEMORY
        Brain        Hands       Notebook
          |            |            |
       Reason         Act        Remember
          └────────────┼────────────┘
                       ↓
                 Complete Goal
```

------------------------------------------------------------------------

# 5. The Five Building Blocks of an AI Agent

## 5.1 LLM --- The Brain

The LLM provides:

-   Understanding
-   Reasoning
-   Context interpretation
-   Decision-making about the next step

Example:

> "I need to check the customer's transaction history."

The LLM decides that this information is required.

However, the LLM does not directly access the bank database.

------------------------------------------------------------------------

## 5.2 Tools --- The Ability to Act

Tools are functions/APIs that the agent is allowed to use.

Examples:

``` text
get_customer_details()
get_transaction_history()
check_location()
run_fraud_model()
query_database()
search_web()
create_ticket()
send_notification()
```

The basic flow is:

``` text
LLM decides
    ↓
Tool is called
    ↓
Tool performs action
    ↓
Result comes back
    ↓
LLM reasons about result
```

### Most important concept

> **LLM decides what action should be taken; the tool performs the
> actual action.**

------------------------------------------------------------------------

# 6. Memory

Memory allows an agent to retain useful information.

## Short-term memory

Information needed for the current task or conversation.

Example:

``` text
User: I want to book a flight to Delhi.
User: Tomorrow.
User: I prefer a window seat.
```

The agent can use the current context to understand the request.

## Long-term memory

Information that can persist across sessions, depending on how the
application is designed.

Example:

``` text
User preference:
Prefers window seats.
```

### Important

Memory is different from the LLM's pretrained knowledge.

``` text
Pretrained knowledge → learned during model training

Memory → application-managed information stored/retrieved for the agent
```

------------------------------------------------------------------------

# 7. Planner

A **planner decides how a larger goal can be broken into smaller
sub-goals or steps**.

Example:

> "Plan a 3-day trip to Delhi."

The planner could create:

``` text
Main goal
   ↓
Plan Delhi trip
   ↓
Sub-goals
   ├── Find flights
   ├── Find hotel
   ├── Find places to visit
   ├── Calculate budget
   └── Create itinerary
```

A planner can also revise a plan when new information changes the
situation.

Example:

``` text
Original plan:
Hotel A

New information:
Hotel A is unavailable

Revised plan:
Hotel B
```

### Planner vs LLM

The LLM itself can perform planning.

In some architectures:

``` text
LLM = reasoning + planning
```

In other architectures, planning can be represented as a more explicit
component.

Therefore:

> **Planner does not always mean a separate model or separate software
> component.**

------------------------------------------------------------------------

# 8. Orchestration / Controller

The **orchestrator/controller coordinates the execution of the agent's
workflow**.

It can control:

-   Which step runs next
-   Which tool/agent is called
-   How results are passed between components
-   When the agent should continue
-   When the task should stop

Your trainer's useful description is:

> **The code that runs the perceive → reason → act → observe cycle and
> decides when to stop.**

## Example

``` text
User
 ↓
Orchestrator
 ↓
Agent / LLM
 ↓
Tool
 ↓
Tool result
 ↓
Agent / LLM
 ↓
Another tool
 ↓
Tool result
 ↓
Orchestrator checks completion
 ↓
Final result
```

### Planner vs Orchestrator

**Planner:**

> "What steps should we take?"

**Orchestrator:**

> "How do we coordinate and execute those steps?"

------------------------------------------------------------------------

# 9. ReAct

**ReAct = Reason + Act**

It is a common pattern for agent behavior.

The agent repeatedly:

``` text
Reason
  ↓
Act
  ↓
Observe
  ↓
Reason again
  ↓
Act again
  ↓
Observe
  ↓
...
```

## Fraud example

User:

> "Investigate transaction TX12345."

### Reason

> I need the customer's transaction history.

### Act

``` text
get_transaction_history()
```

### Observe

``` text
Normal spending: ₹500–₹10,000
Suspicious transaction: ₹1,50,000
```

### Reason

> The amount is unusual. I should check the location.

### Act

``` text
check_location()
```

### Observe

``` text
Location: London
Typical customer activity: India
```

### Reason

> The location is also unusual. I should run the fraud model.

### Act

``` text
run_fraud_model()
```

### Observe

``` text
Fraud probability: 92%
```

### Reason

> The evidence is strongly suspicious. I should create an investigation
> case.

### Act

``` text
create_fraud_case()
```

This is the ReAct-style loop.

------------------------------------------------------------------------

# 10. Autonomy in Agentic AI

Agents **can work autonomously**, but autonomy is not unlimited.

Autonomy means:

> The agent can decide the next step without a human specifying every
> individual action.

Example:

User:

> "Investigate this suspicious transaction."

The user does NOT need to specify:

``` text
1. Check history
2. Check location
3. Run model
4. Check policy
5. Create case
```

The agent can decide those steps.

## But autonomy needs boundaries

Real enterprise agents normally have:

-   Permissions
-   Guardrails
-   Rules
-   Limits
-   Authentication
-   Authorization
-   Human approval for sensitive actions

Example:

``` text
Low-risk action
      ↓
Agent can execute automatically
```

But:

``` text
Block customer's bank account
      ↓
Human approval
      ↓
Agent executes after approval
```

So:

> **Autonomous does not mean unrestricted.**

------------------------------------------------------------------------

# 11. Fraud Investigation --- Complete Agent Example

Fraud investigation is a good example of Agentic AI.

Suppose:

``` text
Customer normally spends:
₹500–₹10,000

New transaction:
₹1,50,000

Location:
London

Customer's normal location:
India

Device:
New device

Fraud model:
92% probability
```

## Traditional fraud model

``` text
Transaction
     ↓
Fraud Detection Model
     ↓
Fraud probability = 92%
```

The model predicts.

## Agentic fraud investigation

``` text
Transaction
     ↓
Fraud Investigation Agent
     ↓
Check customer profile
     ↓
Check transaction history
     ↓
Check location
     ↓
Check device
     ↓
Run fraud model
     ↓
Search fraud policy
     ↓
Reason over evidence
     ↓
Create investigation case
     ↓
Notify fraud analyst
```

### Key distinction

> **A fraud-detection model predicts fraud. A fraud-investigation agent
> investigates the prediction and can take the next permitted actions.**

------------------------------------------------------------------------

# 12. Industry Use Cases for Agentic AI

Agentic AI can be used across many industries.

  -----------------------------------------------------------------------
  Industry                            Example Agentic AI Tasks
  ----------------------------------- -----------------------------------
  Banking & Finance                   Fraud investigation, loan
                                      processing, compliance

  Healthcare                          Appointment workflows, document
                                      processing, insurance claims

  Retail                              Order management, returns,
                                      inventory workflows

  Telecom                             Network troubleshooting, ticket
                                      creation, incident resolution

  Manufacturing                       Predictive maintenance, quality
                                      workflows

  Logistics                           Shipment tracking, route planning,
                                      supplier communication

  Travel                              Trip planning, booking workflows,
                                      itinerary changes

  IT                                  Incident management, log analysis,
                                      testing, support

  HR                                  Resume screening, interview
                                      scheduling, onboarding

  Legal                               Contract analysis, legal research,
                                      compliance

  Marketing & Sales                   Lead qualification, research, CRM
                                      updates

  Education                           Personalized tutoring and student
                                      support

  Government                          Application/document processing and
                                      citizen support
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 13. Agentic AI Project Lifecycle --- From Development to Deployment

In a real company, an engineer may build agents, integrate tools,
evaluate them, deploy them, monitor them, or improve them.

A typical lifecycle is:

``` text
Business Problem
      ↓
Requirements
      ↓
Decide whether an Agent is needed
      ↓
Agent Architecture
      ↓
Data / RAG
      ↓
Tools & APIs
      ↓
Agent Development
      ↓
Testing
      ↓
Evaluation
      ↓
Security & Guardrails
      ↓
Deployment
      ↓
Production Monitoring
      ↓
Continuous Improvement
```

------------------------------------------------------------------------

# 14. Step 1 --- Understand the Business Problem

Do not start by writing code.

First determine:

-   What problem are we solving?
-   Who will use the agent?
-   What is the goal?
-   What actions should it perform?
-   What decisions need human approval?

Example:

> Build a telecom network troubleshooting agent that investigates common
> connectivity problems and creates a support ticket when required.

------------------------------------------------------------------------

# 15. Step 2 --- Decide Whether an Agent is Necessary

Not every problem needs Agentic AI.

Simple request:

> "What is my mobile plan?"

A normal API call may be enough.

More complex request:

> "Investigate why my internet stopped working and resolve it."

This may involve:

``` text
Customer profile
      ↓
Network status
      ↓
Diagnostics
      ↓
Previous incidents
      ↓
Knowledge base
      ↓
Decision
      ↓
Action
```

That is a stronger use case for an agent.

------------------------------------------------------------------------

# 16. Step 3 --- Design the Agent

Define:

### Goal

> Network troubleshooting agent

### Tools

``` text
get_customer_details()
check_network_status()
run_diagnostics()
search_knowledge_base()
create_ticket()
send_notification()
```

### Data

-   Network documentation
-   Troubleshooting manuals
-   Customer information
-   Previous incidents

### Policies

-   What the agent can do
-   What requires human approval
-   What data it can access

------------------------------------------------------------------------

# 17. Step 4 --- Build RAG if the Agent Needs Enterprise Knowledge

For company documentation:

``` text
Documents
    ↓
Document loading
    ↓
Chunking
    ↓
Embedding
    ↓
Vector database
    ↓
Retriever
    ↓
Relevant information
    ↓
Agent
```

The agent can have a tool such as:

``` text
search_knowledge_base()
```

RAG provides **retrieval of relevant knowledge**; the agent decides when
and how to use that knowledge as part of the task.

------------------------------------------------------------------------

# 18. Step 5 --- Build Tools

Tools connect the agent to real systems.

Example:

``` python
def check_network_status(customer_id):
    # Call the company's network API
    ...
```

Another:

``` python
def create_ticket(customer_id, issue):
    # Call ticketing system API
    ...
```

Architecture:

``` text
Agent
  ↓
Tool
  ↓
Company API
  ↓
Database / Enterprise system
  ↓
Result
  ↓
Agent
```

This is how the agent gets its **action capability**.

------------------------------------------------------------------------

# 19. Step 6 --- Build the Agent

An agent can conceptually contain:

``` text
Agent
 ├── LLM
 ├── Instructions
 ├── Tools
 ├── RAG
 ├── Memory / State
 └── Guardrails
```

Example with an agent development framework:

``` text
Network Troubleshooting Agent

LLM       → Gemini
Tools     → Network API, Customer API, Ticket API
RAG       → Troubleshooting documentation
Memory    → Session/conversation state
Rules     → Security and business policies
```

If using Google's ecosystem, **Google ADK** can be used to develop
agents and integrate tools.

------------------------------------------------------------------------

# 20. Step 7 --- Multi-Agent Systems

Sometimes one agent is enough.

If the problem is complex, multiple specialized agents may be used.

``` text
                 Main Agent / Orchestrator
                         ↓
             ┌───────────┼───────────┐
             ↓           ↓           ↓
        Fraud Agent  Billing Agent  Customer Agent
             ↓           ↓           ↓
           Tools       Tools       Tools
```

The main agent can delegate work to specialized agents.

This is where **multi-agent systems** and concepts such as **A2A
(Agent2Agent)** become relevant.

### Important

> **Not every project needs multiple agents. Start with one agent if one
> agent can solve the problem.**

------------------------------------------------------------------------

# 21. Step 8 --- Testing

Test different scenarios.

### Normal case

> "My internet is slow."

### Ambiguous case

> "Internet isn't working."

### Tool failure

> Network API is unavailable.

### Invalid input

> Customer provides an invalid account number.

### Safety-sensitive action

> "Cancel my account."

### Hallucination test

> Ask about information that does not exist in the knowledge base.

Check:

-   Correct tool selection
-   Correct reasoning
-   Correct output
-   Task completion
-   Hallucination
-   Safety
-   Error handling

------------------------------------------------------------------------

# 22. Step 9 --- Evaluation

Agent evaluation is more than checking whether the final answer sounds
good.

Evaluate:

-   Did it select the correct tool?
-   Did it retrieve the correct information?
-   Did it follow the expected workflow?
-   Did it complete the task?
-   Did it make an unsafe decision?
-   How many LLM/tool calls were made?
-   How much did the task cost?
-   How long did it take?

Example evaluation dataset:

  User request           Expected behavior
  ---------------------- ---------------------
  Internet not working   Check network
  Slow internet          Run diagnostics
  Billing issue          Use billing tool
  Unknown issue          Create support case

------------------------------------------------------------------------

# 23. Step 10 --- Security and Guardrails

Production agents must be controlled.

Example:

``` text
Agent permissions

Allowed:
✓ Read customer information
✓ Check network
✓ Create ticket

Not allowed:
✗ Delete customer
✗ Change billing without approval
✗ Access unrelated customer data
```

Important controls include:

-   Authentication
-   Authorization
-   IAM
-   Least-privilege access
-   Input validation
-   Output validation
-   PII protection
-   Human-in-the-loop
-   Audit logs
-   Guardrails

------------------------------------------------------------------------

# 24. Step 11 --- Deployment

After development and evaluation:

``` text
Local development
       ↓
Git
       ↓
CI/CD
       ↓
Automated testing
       ↓
Cloud deployment
       ↓
Production agent
```

In a Google Cloud environment, technologies such as:

-   Google ADK
-   Vertex AI
-   Vertex AI Agent Engine

can be used as part of an agent development/deployment architecture.

The exact production architecture depends on the company's requirements.

------------------------------------------------------------------------

# 25. Step 12 --- Production Monitoring

After deployment, the work is not finished.

Monitor:

-   Agent accuracy
-   Task completion rate
-   Tool failures
-   Latency
-   Token usage
-   Cost
-   Errors
-   Hallucinations
-   Security events
-   User feedback

Example:

``` text
Network API failure rate

Normal:
2%

Suddenly:
35%
       ↓
Monitoring detects problem
       ↓
Engineer investigates
       ↓
Fix API/agent integration
       ↓
Test
       ↓
Deploy updated version
```

This is why companies can have both:

> **Agent developers AND Agent/LLMOps/production monitoring engineers.**

------------------------------------------------------------------------

# 26. Step 13 --- Continuous Improvement

Production feedback becomes new development input.

``` text
Real-world interaction
        ↓
Failure / feedback
        ↓
Analyze
        ↓
Improve prompt/tool/RAG/workflow/model
        ↓
Test
        ↓
Evaluate
        ↓
Deploy new version
        ↓
Monitor again
```

------------------------------------------------------------------------

# 27. Advantages of Agentic AI

## 1. Automates multi-step tasks

An agent can perform an entire workflow instead of only answering a
question.

## 2. Autonomous operation

It can decide the next step without the user specifying every action.

## 3. Tool integration

It can interact with:

-   APIs
-   Databases
-   Web search
-   RAG systems
-   Enterprise applications

## 4. Adaptability

It can change the next step based on new information.

## 5. Productivity

It can automate repetitive work and allow employees to focus on
higher-value activities.

## 6. 24/7 operation

Agents can operate continuously when the application is designed for it.

------------------------------------------------------------------------

# 28. Disadvantages of Agentic AI

## 1. Incorrect actions

A wrong answer from a chatbot is bad; a wrong action by an agent can be
worse.

``` text
Wrong reasoning
      ↓
Wrong tool
      ↓
Wrong real-world action
```

## 2. Hallucination

LLMs can produce incorrect information, which can lead to incorrect
decisions or actions.

## 3. Security and permissions

Agents may have access to sensitive systems, so access must be tightly
controlled.

## 4. Higher cost

Multi-step agent workflows may involve multiple LLM calls and tool
calls.

## 5. Difficult debugging

Agent behavior can be dynamic:

``` text
LLM
 ↓
Tool A
 ↓
LLM
 ↓
Tool C
 ↓
LLM changes plan
 ↓
Tool B
```

Tracing and observability are therefore important.

## 6. Complexity

Production agents can involve:

``` text
LLM
+ Tools
+ APIs
+ RAG
+ Memory
+ Planning
+ Orchestration
+ Guardrails
+ Evaluation
+ Monitoring
+ Security
```

## 7. Human oversight may be required

For high-risk decisions, the agent may investigate/recommend while a
human approves the final action.

------------------------------------------------------------------------

# 29. Key Concepts --- Quick Revision

  -----------------------------------------------------------------------
  Concept                             Easy meaning
  ----------------------------------- -----------------------------------
  **LLM**                             Brain --- understands and reasons

  **Agent**                           Goal-oriented AI worker

  **Agentic AI**                      Broader paradigm for goal-oriented
                                      AI systems

  **Generative AI**                   Generates content

  **Tool**                            Allows the agent to perform an
                                      action

  **Memory**                          Stores/retrieves useful information

  **Short-term memory**               Current task/conversation
                                      information

  **Long-term memory**                Persistent information across
                                      sessions

  **Planner**                         Breaks a goal into steps

  **Orchestrator**                    Coordinates execution

  **ReAct**                           Reason → Act → Observe loop

  **RAG**                             Retrieves relevant external
                                      knowledge

  **Guardrails**                      Controls what the agent can/cannot
                                      do

  **Multi-agent system**              Multiple specialized agents working
                                      together

  **A2A**                             Communication between agents

  **MCP**                             Standardized way to connect AI
                                      applications/agents with tools and
                                      external data
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 30. Interview Questions and Answers

## Q1. What is Agentic AI?

> Agentic AI refers to AI systems that can understand a goal, reason and
> plan, use tools, take actions, observe results, and continue through
> multiple steps to accomplish the goal.

## Q2. What is an AI agent?

> An AI agent is a software system that uses an AI model, tools,
> memory/state, instructions and other components to perform
> goal-oriented tasks.

## Q3. How is Agentic AI different from Generative AI?

> Generative AI primarily focuses on generating content from prompts,
> while Agentic AI focuses on achieving goals through reasoning,
> planning, tool usage and actions. Agentic AI often uses an LLM or
> Generative AI model as its reasoning component.

## Q4. Does an agent work autonomously?

> Yes, an agent can work autonomously within the permissions and
> guardrails defined by the system. It can decide the next step without
> requiring a human to specify every individual action.

## Q5. How does an agent get the ability to perform actions?

> The LLM provides reasoning, while tools provide action capabilities.
> The agent is given functions or APIs that allow it to interact with
> databases, enterprise systems, web services and other applications.

## Q6. What is ReAct?

> ReAct stands for Reason and Act. It is an agent pattern where the
> agent reasons about what to do, takes an action using a tool, observes
> the result, and then reasons about the next action.

## Q7. What is a planner?

> A planner breaks a larger goal into smaller sub-goals or steps and can
> revise the plan when new information changes the situation.

## Q8. What is orchestration?

> Orchestration is the coordination and execution of the different
> components, tools, agents and workflow steps required to complete a
> goal.

## Q9. Planner vs Orchestrator?

> The planner decides what steps should be taken, while the orchestrator
> coordinates and executes those steps and manages the overall loop.

## Q10. What are the building blocks of an AI agent?

A useful conceptual answer is:

``` text
LLM
Tools
Memory
Planner
Orchestrator / Controller
```

A production system may additionally contain:

``` text
RAG
State
Guardrails
Security
Evaluation
Observability
```

## Q11. Give a real-world Agentic AI example.

> A fraud investigation agent can receive a suspicious transaction,
> retrieve transaction history, check customer information, call a fraud
> model, check location and policy information, reason over the
> evidence, create an investigation case, and notify a fraud analyst.

## Q12. Does Agentic AI always require multiple agents?

> No. A single agent can be sufficient. Multiple agents are useful when
> the problem can be naturally divided into specialized
> responsibilities.

## Q13. What happens after an agent is deployed?

> It needs production monitoring, evaluation, error analysis, security
> monitoring, cost/latency tracking and continuous improvement.

------------------------------------------------------------------------

# 31. One-Minute Interview Explanation

If an interviewer asks:

> **"Explain Agentic AI."**

A strong answer is:

> **"Agentic AI is a paradigm where AI systems can pursue a goal rather
> than only generate a response. An agent typically uses an LLM for
> reasoning, tools for taking actions, memory or state for retaining
> relevant information, planning for breaking a goal into steps, and
> orchestration for coordinating execution. A common pattern is ReAct,
> where the agent reasons, acts through a tool, observes the result and
> then decides the next action. For example, a fraud investigation agent
> can investigate a suspicious transaction by checking customer history,
> calling a fraud model, checking location and policy information, and
> then creating an investigation case. In production, these agents
> require security, guardrails, evaluation, monitoring and sometimes
> human approval for high-risk actions."**

------------------------------------------------------------------------

# 32. Final Mental Model

Remember this:

``` text
                    AGENTIC AI
                        |
                        ↓
                     GOAL
                        |
                        ↓
                      LLM
                  "What should I do?"
                        |
                        ↓
                    PLANNER
                  "What are the steps?"
                        |
                        ↓
                 ORCHESTRATOR
              "Run the workflow"
                        |
              ┌─────────┴─────────┐
              ↓                   ↓
            TOOLS               RAG
         "Take action"      "Get knowledge"
              ↓                   ↓
              └─────────┬─────────┘
                        ↓
                     OBSERVE
                        ↓
                       LLM
                  "What next?"
                        |
                        ↓
                     MEMORY
              "What should I retain?"
                        |
                        ↓
                   GUARDRAILS
              "What am I allowed to do?"
                        |
                        ↓
                  GOAL COMPLETED
```

## The one sentence to remember

> **Generative AI generates; an AI agent reasons and acts; Agentic AI is
> the broader system/paradigm that enables AI to pursue goals using
> reasoning, planning, tools, memory, orchestration and controlled
> autonomy.**
