---
title: "Coding by Design GPT4 Agile MDD"
original_file: "./Coding_by_Design_GPT4_Agile_MDD.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "agents", "fine-tuning", "evaluation"]
keywords: ["code", "model", "agent", "constraints", "diagrams", "our", "software", "language", "approach", "generated"]
summary: "<!-- Page 1 -->


## Coding By Design: Gpt-4 Empowers Agile Model


## Driven Development

Ahmed R. Sadik1 a, Sebastian Brulin1 b and Markus Olhofer1 c
1Honda Research Institute Europe, Carl-Legien-Strasse 30, Offenbach am Main, Germany
{ahmed.sadik, sebastian.brulin, markus.olhofer}@honda-ri.de
Keywords: GPT-4. Auto-generated Code, AI-Empowered Model Driven Development, Ontology-Constrained Class

### Diagram, Object Constraint Language, Cyclomatic Complexity

Abstract: Generating code from a n"
related_documents: []
---

# Coding by Design GPT4 Agile MDD

<!-- Page 1 -->


## Coding By Design: Gpt-4 Empowers Agile Model


## Driven Development

Ahmed R. Sadik1 a, Sebastian Brulin1 b and Markus Olhofer1 c
1Honda Research Institute Europe, Carl-Legien-Strasse 30, Offenbach am Main, Germany
{ahmed.sadik, sebastian.brulin, markus.olhofer}@honda-ri.de
Keywords: GPT-4. Auto-generated Code, AI-Empowered Model Driven Development, Ontology-Constrained Class

### Diagram, Object Constraint Language, Cyclomatic Complexity

Abstract: Generating code from a natural language using Large Language Models (LLMs) such as ChatGPT, seems
groundbreaking. Yet, with more extensive use, it's evident that this approach has its own limitations. The
inherent ambiguity of natural language presents challenges for complex software designs. Accordingly, our
research offers an Agile Model-Driven Development (MDD) approach that enhances code auto-generation
using OpenAI's GPT-4. Our work emphasizes "Agility" as a significant contribution to the current MDD
method, particularly when the model undergoes changes or needs deployment in a different programming
language. Thus, we present a case-study showcasing a multi-agent simulation system of an Unmanned
Vehicle Fleet. In the first and second layer of our approach, we constructed a textual representation of the
case-study using Unified Model Language (UML) diagrams. In the next layer, we introduced two sets of
constraints that minimize model ambiguity. Object Constraints Language (OCL) is applied to fine-tune the
code constructions details, while FIPA ontology is used to shape communication semantics and protocols.
Ultimately, leveraging GPT-4, our last layer auto-generates code in both Java and Python. The Java code is
deployed within the JADE framework, while the Python code is deployed in PADE framework. Concluding
our research, we engaged in a comprehensive evaluation of the generated code. From a behavioural
standpoint, the auto-generated code aligned perfectly with the expected UML sequence diagram.
Structurally, we compared the complexity of code derived from UML diagrams constrained solely by OCL
to that influenced by both OCL and FIPA-ontology. Results indicate that ontology-constrained model
produce inherently more intricate code, but it remains manageable and low-risk for further testing and
maintenance.
a https://orcid.org/ 0000-0001-8291-2211
b https://orcid.org/ 0000-0002-9710-6877
c https://orcid.org/0000-0002-3062-3829

<!-- Page 2 -->

1 INTRODUCTION generation processes solely rely on the static
structure offered by class diagrams, they might miss
out on these dynamic and interactional aspects of
In the AI era, with Large Language Models (LLMs)
system behaviour. Thus, for truly comprehensive
trained on diverse code, new opportunities arise for
and complete auto-generated code, there is an
innovation in Model-Driven Development (MDD).
imperative need to synergistically combine the static

### MDD is an evolving field that holds promise to

semantic richness with the dynamic perspectives
improve the efficiency and robustness of software
offered by other UML diagrams (Kapferer &
engineering practices (Hailpern & Tarr, 2006). This
Zimmermann, 2020).
study introduces an agile MDD approach that
However, while class diagrams focus on the
leverages the use of existing LLMs such as
structural aspects of a system, they frequently miss

### OpenAI's ChatGPT, to auto-generate complete,

capturing intricate rules, constraints, or the
deployment-ready software artifacts (Sadik,
specifications inherent to a domain. This is where
Ceravola, et al., 2023). Our approach eliminates the
the Object Constraint Language (OCL) plays a
intensive time and effort seen in conventional MDD,
pivotal role in adding the code construction fine
where it is needed to craft a unique code generator
details, as it offers a declarative language to specify
for each deployment or update the generator with
precise constraints and derived values, that are vital
every model alteration. Complete software implies
for maintaining the integrity and consistency of the
that the auto-generated artifacts are not only intricate
model (Cabot & Gogolla, 2012). Furthermore, the
but also synergistically structured to collectively
dynamic constraints of the model such as
ensure their designated functionality and meet its
communication between the classes can be
specified requirements (Feltus et al., 2017).
constrained as well via a domain-specific ontology
Code generation, especially from formal models
language such as FIPA-ontology (FIPA, 2000).
such as Unified Modeling Language (UML),

### Domain-specific ontology enables the common


### Systems Modeling Language (SysML), or Business

understanding of knowledge that is exchanged via

### Process Model and Notation (BPMN) diagrams has

bridging the semantic gap that conventional class
emerged as an influential paradigm in modern
diagrams do not include (Siricharoen, 2009). The
software engineering practices (OMG, 2006). Class
integration of class diagrams, combined with OCL
diagrams, a primary component of most objectconstraints and domain-specific ontologies, could
oriented design methodologies, capture the static
spearhead a novel epoch in code generation. This
structure of software systems by representing
integrated approach would enable the production of
classes, their attributes, operations, and their
code that's not merely structurally accurate but also
interrelationships. When paired with the appropriate
enriched with semantic details, ensuring the
tools, these diagrams can be directly converted into
resulting software mirrors both its foundational
executable code, facilitating a more streamlined
design and the detailed domain expertise.
software development process (Sharaf et al., 2019).
Evaluation of auto-generated code is an essential

### Such automation not only guarantees a solid

step in grasping its software quality (Liu et al.,
alignment between the design and its corresponding
2023). Traditionally, criteria to assess this quality,
implementation but also reduces manual coding
such as testability, maintainability, and reliability,
errors. This leads to improved software quality and
have been qualitative in nature. This inherent
quicker market deployment (Sarkisian et al., 2022).
qualitative character has often rendered them
The dynamic behaviour, interactions, and holistic
relative and open to subjective interpretation.
views of the system play a fundamental role in

### Accordingly, our research tends to adopt more

comprehending its overall functionality. UML offers
objective, quantifiable criteria. Given our primary
a suite of diagrams, each with a unique perspective
objective to auto-generate seamless code from a
on system modelling. For instance, UML sequence
model, our evaluation lens sharply focused on the
diagrams represents the interactions among objects
structural integrity of this auto-generated code. We
in a time-sequential manner, capturing the intricacies
utilized cyclomatic complexity as an instrumental
of object communications(Perez-Martinez & Sierrametric to provide insights into its structural

### Alonso, 2004). Use case diagrams focus on the

soundness. Furthermore, a comparative analysis was
system's functionalities from an end-user's
executed, pitting the behaviors of the generated
perspective, ensuring the system's relevance and
code—deployed in varied languages—against each
usability. Moreover, state diagrams offer insights
other and against the expected behavior from a
into the various states an object can have and the
model's perspective (Ahmad et al., 2023).
triggering events for state transitions. When code

<!-- Page 3 -->

The paper is structured to guide the reader as the primary artifact from which the final
through our study. Section 2 provides a detailed application is generated (Sadik & Goerick, 2021).
problem statement, where we pinpoint the current However, the process of designing and maintaining
challenge with existing MDD approach that these models, introduces challenges that can limit
hindering it from become agile. Section 3 breaks the MDD effectiveness. Herein, two main problems
down the four layers of the proposed agile MDD can be identified. Firstly, traditional modeling
techniques, such as UML diagrams, while being
approach. Section 4 applies the proposed approach
excellent for data structuring in software
to model a Multi-Agent System (MAS) of an
development, often lacks the semantic richness and

### Unmanned Vehicle Fleet (UVF) and Mission

rule-based derivation of knowledge inherent to
Control Center (MCC). After modeling the structure
ontologies (Belghiat & Bourahla, 2012). This leads
of the case-study using a comprehensive UML class
to models that are accurate in terms of structure and
diagram, we add two layers of constraints to
behavior but lacking in semantic depth, making
constrain both the model construction and
them less effective in modeling complex real-world
communication. We used OCL to describe the
scenarios. Secondly, transforming these models into
model details such as invariants, pre, and post
executable code is not a straightforward process
conditions. Furthermore, we used Intelligent (Petrovic & Al-Azzoni, 2023). As it involves manual
Physical Agents (FIPA) ontology, to define the scripting of the code generator, that requires to be
communication semantics among the agents. Then meticulously maintained and updated to keep pace
we modelled the case-study behaviour by UML use with changes in the model and the underlying
case diagram, activity diagram and state machine. technology stack. This is particularly true when
Finally, we auto-generate Java and Python code alternating the deployment from one programming
from the same model by using GPT-4. The code is language to another (Cámara et al., 2023)
deployed to simulate the UVF-MCC multi agent in
The Java code is deployed within the Java Agent
Development (JADE) framework, and Python Agent
Development (PADE) framework consequently. In

### Section 5, we evaluate the model behavior by

comparing JADE and PADE simulation behavior to
each other’s and to the originally designated
predicated behavior from the model. Furthermore,
we took a closer look at the generated autocade
structure via its cyclomatic complexity. In this part
we compared a generated code complexity from a
model with only OCL constrains to the same model
that is constrained by OCL and FIPA-ontology.

### Finally, Section 6 wraps up our findings, discusses

their implications, and suggests next steps in future
research. Figure 1: Difference between traditional coding and

## Mdd.

2 PROBLEM STATEMENT To comprehensively address the challenge in
code generation within the framework of the current
Natural language inherently possesses ambiguity, MDD approach (Kelly & Tolvanen, 2008), it is
which is not only a challenge for machines to essential to pinpoint the distinction between
comprehend but is also confusing for humans. When traditional coding and MDD code generation as
utilizing ChatGPT to auto-generate intricate shown in Figure 1. Traditional coding tends to
software artifices, defected code is often produced, directly encode the software functionalities in code.
due to the uncertain and open-ended nature of the This approach works well for smaller features that
input prompt. This issue becomes significantly can be transcribed straightforwardly as code.
pronounced in cases where the software to be Debugging, testing, and maintenance are also
generated is complex, multi-dimensional and cannot performed at the code level. In contrast, the modelbe effectively described using natural language. and-code separation approach involves the use of
Yet, MDD promises an elevated level of models to abstract and understand the system better,
software abstraction, where high-level model is used separate from the code. Developers interpret these

<!-- Page 4 -->

models while coding the application, and once
coding is done, models are often discarded due to
the high cost of keeping them up to date. Code
visualization involves creating models after the
software is designed and built, to understand what a
program does or to import libraries or other
constructs from code to be used as elements in
models. These models, however, are typically not
used for implementing, debugging, or testing the
software as we have the code (Fadjukoff &
Tolvanen, 2022).

### While in MDD, models are the primary artifacts

in the development process. These source models
are used instead of source code. The target code is
automatically generated from these models, which
raises the level of abstraction and hides complexity.
Tools like Eclipse Papyrus, MagicDraw, Enterprise

### Architect, or IBM Rational Rhapsody have

traditionally been used for this purpose (David et al.,
2023). Yet, every time there is a shift in the
deployment language or a significant update in the
model, these tools necessitate substantial alterations
Figure 2: Proposed Agile Model Driven Development
to the code generators, impeding agility in the
approach.
development cycle. However, creating a code
generator is a demanding task, consuming

### In the proposed approach in Figure 2. The

considerable time and energy from modelers.
modeller initially creates the different model layers,

### Further complicating matters is the requirement to

which are structural, behavioural, and constraints.
craft a unique code generator for each programming
The structural layers contain all the diagrams that
language, making the prevailing MDD approach less
reflect the static by illustrating the software
adaptive to different deployment languages, and
components and the intricate relationships among
therefore agile MDD fails to exist. It's in this context
them. For example, Class diagrams detail object
that we see potential in leveraging LLMs like
relationships and hierarchies, while package
ChatGPT as universal code generators (Chen et al.,
diagrams group these objects, highlighting
2021). Accordingly, our study highlights the
dependencies. Component diagrams then break
challenging issue that "Although, MDD provides a
down system functionality at a high level, capturing
structured methodology that overcomes the
inter-component relationships. For the real-world
inadequacies of natural language for auto-generating
physical layout, deployment diagrams depict
deployable code, the existing MDD approach has
hardware configurations and component
not been adequately adapted to the present LLM
distributions. Object diagrams offer runtime object
capabilities in code auto-generation. This
snapshots, while profile diagrams tailor UML
misalignment makes the current MDD approach
models to specific platforms. The behavioural layer
unfit for the agile software development workflow."
models how the system operates and interacts.

### Sequence diagrams lay out events in a linear

progression, giving a clear timeline of interactions.

## 3 Proposed Approach


### Activity diagrams present a flowchart-like

representation of processes, detailing step-by-step
To tackle the challenge outlined in the problem actions. Interaction diagrams showcase the interplay
statement, our proposed MDD approach necessitates
between components, while timing diagrams
that ChatGPT fully understands the model and its
emphasize the importance of timing and sequence.
associated views. Given that ChatGPT currently
On the user side, use case diagrams illustrate how
processes information through text prompts, we
external entities engage with the system. Lastly,
employed PlantUML to convert the visual UML
state diagrams capture the life cycle of entities,
diagram to formal text representation, that can be
showing how they transition between different
easily copied into ChatGPT prompt.
states.

<!-- Page 5 -->

Although, the structural and behavioural bugs, possibly with assistance from ChatGPT, and
diagrams provide a holistic architectural view, they iteratively run the code until it successfully
often lack the rules that regulate the model accomplishes its intended purpose."
architecture semantics. Accordingly, in this research
we propose the constraints layer that fine-tunes the
model, by explicitly the model meta-values that 4 CASE-STUDY MODEL
cannot expressed by UML notations. OCL for
example is used to restrict the construction details of

### The chosen use-case involves a UVF, comprising

the structural and behavioural layers, by specifying
various types of UVs that undertake specific
invariants on classes and stereotypes, describe premissions and are coordinated by an MCC involving
and post-conditions on method and states, and limits a human operator (Sadik, Bolder, et al., 2023). This
the parameters’ values. Furthermore, communication case-study is intentionally distributed, enabling it to
constraints can be defined using the proper formal be modeled and simulated as a MAS (Brulin &
method such as an ontology language to express the Olhofer, 2023) . Such MAS often encompasses a
communication semantics meanings, and protocol high complexity level, as each entity is represented
that is necessary to communicate and share as an agent and must communicate and share
knowledge among the software artifacts. information with other entities (i.e., agents) to
Ultimltiy in the code deployment layer, we achieve a common goal (i.e., the fleet mission). To
employed ChatGPT, which is based on the GPT-4 avoid overwhelming the reader with the intricacies
architecture, to generate code. The reason to use of MAS in the following sections, we will highlight
GPT-4 rather than GPT-3.5 is the higher capability only the essential model views that facilitate an
of GPT-4 to reason, which is very important value understanding of the MAS operation concept (Sadik
for our approach as the LLM must understand the & Urban, 2018).
model semantics and rules that is encapsulated in the
4.1 Model Structural Layer
constraints layer to embed them in the generated
code. Furthermore, after the using ChatGPT to autogenerate the code, it is important that the modeler
deploys the generated code onto the software
platform and ensure that it is operational. However,
it’s important to be aware that ChatGPT’s code
generation capabilities are still evolving and not
flawless (Dong et al., 2023). As such, it is
anticipated that there may be bugs encountered
during the deployment of the code. Consequently, it
is necessary for the mod to address these bugs,
potentially with the assistance of ChatGPT, and
repeatedly run the code until it is successfully
fulfilling its intended purpose.

### Ultimately, in the code deployment layer,


### ChatGPT, based on the GPT-4 architecture, is

employed to generate code. The choice of GPT-4
over GPT-3.5 is due to its superior reasoning
capabilities, a vital feature for our approach. The
LLM must comprehend the model semantics and Figure 3: Case-study class diagram.
semantics encapsulated in the constraints layer to
integrate them into the generated code. Furthermore, Class diagram can be considered the most important
post auto-generation of code using ChatGPT, it is view in the model structure layer. Every entity
crucial for the modeler to deploy the generated code within the case-study is represented as an agent class
and verify its operationality. However, it's essential as shown in Figure 3. A summery of these agents are
to acknowledge that ChatGPT's code generation explained as follows:
capabilities are continually evolving and may not be ▪ Operator: models the human operator and
flawless. Therefore, the possibility of encountering contains attributes such as operator-ID. It also
bugs during the code deployment is anticipated. It includes the actions such as send the missionbecomes imperative for the modeler to address these brief and receive the mission-performance.

<!-- Page 6 -->

▪ MCC: models the command center, including assigns the tasks to the available UVs. Subsequently,
attributes like MCC-ID. MCC coordinates the UVF-manager agent awaits the completion of
missions and monitoring the fleet. It includes tasks by each UV and collates their performance,
actions such as receive the mission-brief, send which is instrumental in assessing the overall UVF
the fleet-plan, receive the fleet-performance, performance. This consolidated performance is
and send the mission-performance. relayed to the MCC, translated into mission-
▪ UVF-Manager: models the UVF-manager, performance, and communicated back to the
containing attributes like UVF-ID, UVs’ operator agent.
number, fleet-plan, and fleet-performance. It
includes actions such as receive the fleet-plan,
send UV-tasks, send the fleet-performance,
and receive the UV-performance.
▪ UV: a generic class that models the UVs. It
contains attributes such as UV-ID, the UV’s
Task, the UV’s Status, and Performance.
Actions include receive the UV-task and send
the UV-performance.
▪ UAV, UGV, USV: these are subclasses of
UV, each modelling different types of a UV.

### The previously described class diagram has been

employed to articulate the intricate internal details of
each agent, encompassing attributes, operations, and
visibility. Additionally, the class diagram is utilized
to delineate all conceivable relationships among the
agents, including composition, aggregation, and
inheritance. Moreover, the multiplicity of the classes
establishes the cardinality between the agents.
4.2 Model Behavioural Layer

### Furthermore, the state diagram provides a

granular exploration into the agent internal
To maintain brevity and keep the article focused, the
behaviour, illustrating the transitions triggered by
article will only explain two views which are the
events and the corresponding actions undertaken by
activity and state diagrams, as they are the most
the agents. In the scenario presented, the operator
important behavioral views to understand the caseagent, the MCC, and the UVF-manager are all
study model. The activity diagram refines and
modelled using a straightforward two-state diagram,
complements the class diagram by meticulously
representing states of being either busy or free.
detailing aspects such as synchronization, parallel
However, for the UV, modelling a more intricate
execution, and conditional flows, which are
state machine was imperative, as it is utilized later
indispensable for effectively achieving the mission
by the agent to assess its task performance. Figure 5
goals. In contrast, the state diagram offers a
explains the different UV states as follows:
microscopic perspective, unveiling the life cycle of
the agents’ class within the model and illuminating
how they coordinate and respond to realize the
overarching mission objectives.

### The activity diagram in Figure 4 elaborates the

interplay of information and task flows within the
agents. It illustrates the orchestration of processes
and the sequence in which tasks are allocated,
carried out, and assessed, providing an
understanding of the MAS temporal and logical
dynamics. Thus, the interaction begins when the
operator agent sends the mission-brief to the MCC
agent. The latter transforms the brief into a plan and
conveys it to the UVF-manager, which, in turn,
Figure 4: Case-study activity diagram.
Figure 5: UV agent state diagram.

<!-- Page 7 -->

▪ Initial: the UV is prepared and ready to During our study, we categorized five different
operate. types on constraints, and we applied them on all the
▪ Available: the UV can be either registered or agent classes. Figure 6 shows an example of some of
unregistered. the constrains that applied on the UV agent class.
▪ Unavailable: the UV is rendered unregistrable The five constraint types are summarised as follows:
due to being out of service, possibly due to a ▪ Uniqueness: to ensure that every instance
failure or battery charging. agent is unique. For example, the UV agent
▪ Unregistered: In this condition, the UV is must have a unique identifier across MAS.
available but has not been registered, as it is ▪ Cardinality: to ensure the association of the
still configuring its parameters. agent instances with each other’s, for each
▪ Registered: the UV can be either controlled or UVF-manager with a unique ID is associated
uncontrolled. with a group of UVs with different unique
▪ Uncontrolled: the UV is registered but has IDs.
not been assigned any mission. ▪ Value: this constraint type is ensuring that
▪ Controlled: the UV is not only registered but some of the agent class values are limited to
also allocated a mission. certain threshold. For example, the
performance value of any UV agent is within
4.3 Model Constraints Layer the 0 to 100 range.
▪ Pre-condition: this constraint type guarantee
The constraints layer in the proposed MDD the state consistency of an agent instance
approach acts as a meta-model that encapsulates all before triggering the next state. For example, a
aspects of the technical requirements that cannot be UV agent can only receive a new task if its
formalized in the structural and behavioral layers. In current status is 'Idle'. This ensures that an
the following sections we will discuss in detail the agent must complete its current task or be in a
different types of meta-model constraints that have standby state before being assigned a new
been considered within the case-study modeling. task, preventing overloading or task conflicts.
▪ Post-condition: this constraint type mandates
4.3.1 Construction Constraints the new state of an agent instance after
moving from old state. For example, after a
The OCL is a declarative language used primarily UV agent has received a new task, its status
with UML to describe rules that apply to classes must be updated to be 'Active'. This reflects
within a model. Incorporating OCL as construction that the agent is currently engaged with a task
constraints within UML diagrams serves as a key and helps in the accurate tracking and
enabler for refining the model. Therefore, OCL management of the agent's workload.
enhances the model clarity by addressing the
inherent ambiguities in its construction details. This 4.3.2 Communication Constraints
precision is particularly beneficial in the generation
of deployed implemented code directly from model OCL, while adept at specifying constraints on the
views. The added constraints ensure that the static aspects and behaviors of classes within a UML
transition from model to code is more accurate and model, is not inherently designed to manage or
seamless. constrain communication among the classes
themselves. Its limitations become especially
pronounced when addressing our case- study
requirements to achieve a mission in MAS, where
interaction and communication among agents are
fundamental (Sadik & Urban, 2018). Multi-agent
frameworks like JADE and PADE offer a robust and
dynamic ontology language that is called FIPA-
ontology communication language (Foundation for

### Intelligent Physical Agents, 2023). FIPA offers a

comprehensive set of interaction protocols, that can
achieve intricate patterns of interaction, negotiation,
and knowledge exchange among diverse agents,
which is a capability OCL doesn’t naturally extend.
Figure 6: UV agent construction constraints in OCL.

<!-- Page 8 -->

▪ Send (schema-x): represents the action of
transmitting data, e.g., the operator agent uses
this action to send a mission-brief to the MCC.
▪ Receive (schema-x): represents the action of
receiving data, e.g., the MCC agent uses this
action to receive the mission-brief from the
operator.
4.3.3 Other Constraints
Other technical requirements must be considered in
the constraints layer as well. Examples of these
constraints can be the auto-generated code quality,
code privacy, cybersecurity, etc. One way to

### FIPA-ontology is standard that defines a set of

formalize these constraints is by using the OCL. For
fixed schemas that together form the MAS
instance, to ensure a consistent indentation we used:
communication model as show in Figure 7. The first
set of schemas in our model are the message
self.leadingSpaces.mod(spacePerIndent)
communication schemas. These set of = 0.
communication schemas are listed as follows:
▪ Mission-Brief: holds information regarding Other OCL constraints that we have considered
the mission-brief, containing attributes like within this model to regulate the maximum line
mission-ID, description, and status. length, whitespace, function length, and import
▪ Fleet-Plan: contains attributes that provide Statements. Therefore, applying these code quality
details about the fleet-plan, such as plan-ID, constraints is ensuring that the auto-generated code
description, and status. is functionally accurate, readable, maintainable, and
▪ UV-Task: includes attributes like task-ID, clear.
description, and status. Furthermore, formal constraints in this layer can
▪ UV-Performance: includes attributes like be added to regulate other important aspects of the
UV-performance-ID and performance-metric. autogenerated code such as data privacy and
▪ Fleet-Performance: includes attributes like cybersecurity. However, in order not to diverse from
Fleet-Performance-ID and performance- the main paper topic, we will prefer to discuss that in
metric. the future work section.
▪ Mission-Performance: includes attributes
like mission-performance-ID and
performance-metric.

## 5 Code Evaluation


### The second set of schemas are the predicates,

which depict relationships between agent classes
Due to our proposed MDD approach, after modeling
including the communication schemas:
the system in a textual formal format such as
▪ (agent-x) <is-a> (agent-y): expresses the
PlantUML, we give this model as an input to GPT-4
inheritance relationship between agents, e.g.,
prompt, then we use the output code. In our case
UAV is a type of UV.
study, few bugs have been produced by GPT-4,
▪ (agent-x) <has-a> (agent-y): represents the
however by fixing these bugs, the output code was
composition relationship between agent, e.g.,
capable of being deployed. As our focus in this
MCC has a UVF-manager.
study is not the auto-generated code correctness
▪ (agent-x) <owns> (agent-y): expresses the
rather than its completeness. We focused on our
aggregation relationship, e.g., the UVF-
evaluation on exploring and analyzing the
manager owns multiple UVs.
autogenerated code structure and behavior, rather
▪ (agent-x) <collaborates> (agent-y): defines
than discovering the type and number of generated
the collaboration between agents, e.g., the
code bugs. For this reason, we conducted two
operator collaborates with the MCC.
different experiments. First Experiment targets the

### The third set of schemas are the actions. Actions

exploring of the autogenerated code behavior, while
stand for operations that can be performed by an
the second experiment aims to analysis the
agent specially in our model on a message schema:
autogenerated code structure and complexity.
Figure 7: Case-study FIPA-ontology model.

<!-- Page 9 -->

5.1 Experiment 1: Behavioural UGV, and USV. Each UV, upon task completion,
Dynamic analysis relays performance data to the UVF-manager.

### Collating this data, the UVF-manager formulates a

In the first experiment, we orchestrated the comprehensive fleet-performance metric, which is
generation of two distinct deployments. The first, relayed back to the MCC. The MCC, in turn,
written in Java, is tailored to run on JADE platform, evaluates this metric in congruence with the mission
while the second, crafted in Python, is designated to objectives, compiling a definitive missionbe implemented in PADE. The goal of the performance report. This report, the culmination of
experiment is to compare the code behaviour that the entire operation, is ultimately returned to the
run on JADE against the code is running on PADE, Operator.
to ensure the consistency of the system dynamic Two important remarks have been noticed from
regardless the deployment execution language. comparing these two sequence diagrams in Figure 8
Accordingly, we observed the agent interaction with the original case-study activity diagram in
behavior on JADE vs PADE framework. We found Figure 4. First, we noticed that ChatGPT has
that the agents' behavior as captured by JADE enhanced the interaction by adding new behaviours
Sniffer tool aligns with the plotted sequence diagram to MCC agent and UVF-manager agent. This new
from PADE agent interaction, as shown in Figure 8. behaviour can be seen when the MCC is sending
Both JADE and PADE deployment have three UV DiscoverUVs message to the UVF-Manger agent
instances, which are UAV, UGV, and USV. and waiting the UVList before forming a FleetPlan,
as logically the MCC needed to know what the
available UVs resources are before planning them
based on the mission-brief. This new interaction
behaviour was not explicitly mentioned in the casestudy activity diagram. The second remark that the
timing of interaction between the MCC and the UVs
differ in JADE and PADE, most probably due to the
difference in the state machine of each UV instance.

### This is a good indication that these UV state

machine can emulate the operation of the agents.
5.2 Experiment 2: Structural

### Complexity assessment

In both sequence diagrams in Figure 8, we see The second experiment focuses on exploring the
that the depicted process commences with the autogenerated code structure and complexity.
Operator transmitting a mission-brief to the MCC. Therefore, in this experiment we used the
On receiving this, the MCC solicits the UVF- cyclomatic complexity metric, to measure and
manager to identify available UVs. Upon obtaining a analysis the autogenerated code complexity.
list of accessible UVs, the MCC devises a fleet-plan Cyclomatic complexity quantifies the code
and conveys it to the UVF-manager. After this, the complexity by counting the number of linearly
UVF-manager dispatches specific tasks to the UAV, independent paths through its source code.
Figure 8: JADE vs PADE Sequence diagram. Figure 9: code control-flow graph example.

<!-- Page 10 -->

Calculated using the control-flow graph of the code constraints only, the agents are communicating via
as the one shown in Figure 9. In the control-flow string-based message as shown in the agent
graph example shown in Figure 9, the cyclomatic communication message in Figure 10-a, while using
complexity (M) can be calculated from the formula: OCL along with FIPA-ontology constraints resulted
M = E - N + 2P (1) in agents that communicate via schema-based
Where: message as shown in Figure 10-b.
▪ E is the number of edges in the flow graph
▪ N is the number of nodes Table 1: Cyclomatic Complexity of auto -generated code
▪ P is the number of graph separate branches model with OCL constraints only.
Thus, M in this case equals 3.
Accordingly, M can be used to assess the
difficulty of code testing, maintenance,
understanding, refactoring, performance, reliability,
and documentation, where the following values are
considered in the assessment:
▪ M = 1-10: law risk
▪ M = 11-20: moderate risk
▪ M = 21-50: high risk; needs to be reviewed Table 2: Cyclomatic Complexity of auto -generated code
and perhaps split into smaller modules with OCL and Ontology constraints.
▪ M > 50: sever risk; necessary refactoring is
required

### After generating the two distinct deployments,

we transformed the agent classes into control flow
diagrams to calculate their M, as shown in Table 1
and Table 2. By comparing M values of the autogenerated code in Table 1 and Table 2, we will find
that the code complexity is slightly increasing by
adding the FIPA-ontology constraints in the second
the deployment. however, the complexity of all the
agent classes in both deployments is still locating
under the law risk category. This means that the
auto-generated structure is adequate and does not
need any further refactoring. Furthermore, the
highest M value belongs to the UVF-manger in the
second deployment, where we considered both the

### OCL and the FIPA-ontology constraints. This value

Figure 10: String based communication vs equals to 6, which means that there is a still a large
schema-based communication. risk marge that allows us to add further constraints
in our model without negatively influencing the
As in our MDD approach, we emphasized the complexity of the autogenerated code.
effect of adding the formal constraints on generating
a deployed code, our interest in this experiment is to
understand the influence of the constraints layer on

## 6 Discussion, Conclusion,

the autogenerated code. Therefore, in the experiment

## And Future Work

we autogenerated two distinct deployments, that
differ in the level of constraints involved in their
models. The first model implements only the OCL In our research, we highlighted the difficulties in
constraints, while the second model add the FIPA- auto-generating deployable code from natural
ontology to the model. In case of using OCL language using LLMs like ChatGPT, primarily due

<!-- Page 11 -->

to language ambiguity. To address this, we provide meaningful semantics without unduly
employed formal modelling languages, such as complicating the resultant codebase. Furthermore,
UML, for better interpretation by ChatGPT. We the analysis also hinted at a notable latitude in our
found that current UML code generation practices approach. There appears to be a reasonable buffer
don't fully exploit LLMs, revealing a gap in agility allowing for the inclusion of additional constraints to
within the MDD process. To enhance this agility, we the model in future iterations without triggering an
introduced "constraints" into UML models, adding immediate need for a code refactor. This is
semantic depth to ensure accurate code generation. indicative of the robustness and scalability inherent
These constraints improve various software aspects, in our MDD approach.
such as structure, and communication. In our exploration into integrating the advantages
In our case study, we showcased our proposed of LLMs into MDD, we've identified that using
MDD approach by modelling a multi-agent of UVF. formal modelling languages can significantly bridge
We used class diagrams to outline agents, while the gap between the challenges of natural language
activity and state diagrams captured their ambiguities and the precision of code generation.
interactions and internal behaviours. Detailed The incorporation of meta-modeling constraints not
constraints were provided using the Object only refines the code generation process but also
Constraint Language (OCL) for structure, and FIPA- provides insights into its structural complexity,
ontology for agent communication. This model then ensuring a more informed and resilient codebase.
served as a foundation for auto-generating code in Combined, these advancements hint at a
both Java and Python using GPT-4, chosen for its transformative path to achieving the elusive agility
advanced reasoning over GPT-3.5. The effectiveness in current MDD practices. As the world of software
of our MDD approach relies on the LLM's ability to development evolves, this seamless interplay
accurately understand the model's constraints, between structured modeling, advanced LLM
ensuring code generation remains true to our design. reasoning, and structural complexity assessments
In the first evaluation experiment, we examined will be paramount in crafting agile, efficient, and
the behaviour of auto-generated code within robust software solutions.
simulation environments: Java's JADE and Python's In upcoming research, we plan to assess the
PADE frameworks. Both deployments effectively correctness of the auto-generated code by
captured the intended agent interactions, though quantifying the bugs present and pinpointing if
there were minor sequence variations between them. certain defects consistently relate to the model.
Remarkably, GPT-4 not only adhered to the Given the influential role of constraints in refining
specified agent logic but also enriched it by the auto-generated code, we intend to incorporate
introducing two new behaviours in the MCC agent's new privacy and cybersecurity constraints and
communication sequence. This addition highlighted subsequently analyse the characteristics of the
the power of communication constraints in guiding resultant code. It's also essential to compare our
GPT-4 and its enhanced comprehension of agent methodology with current MDD frameworks,
interactions. While these improvements were evaluating factors like efficiency, accuracy, and
impressive, they underscored a need for meticulous reliability in various contexts. Through
code review. Despite GPT-4's advancements, comprehensive enhancement and evaluation, we aim
ensuring that the generated code remains consistent to pave the way for broader industry adoption.
with design intentions is crucial to prevent
unexpected behaviours.

### In the second experiment, we examined the REFERENCES

structural of the auto-generated code, specifically by
assessing its cyclomatic complexity. In this
Ahmad, A., Waseem, M., Liang, P., Fehmideh, M., Aktar,
experiment, we created two separate deployments.

### M. S., & Mikkonen, T. (2023). Towards Human-Bot

The first deployment code resulted from a model Collaborative Software Architecting with ChatGPT
that involves only OCL constraints, while the second (arXiv:2302.14600).
deployment coded resulted from a model that Belghiat, A., & Bourahla, M. (2012). From UML Class
involves both OCL and FIPA-Ontology constraints. Diagrams to OWL Ontologies: A Graph
Our analysis revealed the intriguing remake that Transformation Based Approach. ICWIT, 330–335.
Brulin, S., & Olhofer, M. (2023). Bi-level Network Design
integrating FIPA-ontology constraints didn't
for UAM Vertiport Allocation Using Activity- Based
dramatically augment the complexity of the auto-
Transport Simulations.
generated code. This suggests that these constraints

<!-- Page 12 -->

Cabot, J., & Gogolla, M. (2012). Object constraint Intelligence and Lecture Notes in Bioinformatics),
language (OCL): A definitive guide. In International 3047.
school on formal methods for the design of computer, Petrovic, N., & Al-Azzoni, I. (2023). AUTOMATED
communication and software systems (pp. 58–90). APPROACH TO MODEL-DRIVEN ENGINEERING
Springer. LEVERAGING CHATGPT AND ECORE.
Cámara, J., Troya, J., Burgueño, L., & Vallecillo, A. Sadik, A. R., Bolder, B., & Subasic, P. (2023). A self-
(2023). On the assessment of generative AI in adaptive system of systems architecture to enable its
modeling tasks: An experience report with ChatGPT ad-hoc scalability: Unmanned Vehicle Fleet - Mission
and UML. Software and Systems Modeling, 22(3), Control Center Case study. Proceedings of the 2023
781–793. 7th International Conference on Intelligent Systems,
Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H. P. de Metaheuristics & Swarm Intelligence, 111–118.
O., Kaplan, J., Edwards, H., Burda, Y., Joseph, N., Sadik, A. R., Ceravola, A., Joublin, F., & Patra, J. (2023).
Brockman, G., Ray, A., Puri, R., Krueger, G., Petrov, Analysis of ChatGPT on Source Code
M., Khlaaf, H., Sastry, G., Mishkin, P., Chan, B., (arXiv:2306.00597).
Gray, S., … Zaremba, W. (2021). Evaluating Large Sadik, A. R., & Goerick, C. (2021). Multi-Robot System
Language Models Trained on Code Architecture Design in SysML and BPMN. Advances
(arXiv:2107.03374). in Science, Technology and Engineering Systems
David, I., Latifaj, M., Pietron, J., Zhang, W., Ciccozzi, F., Journal, 6(4). https://doi.org/10.25046/aj060421
Malavolta, I., Raschke, A., Steghöfer, J.-P., & Hebig, Sadik, A. R., & Urban, B. (2018). CPROSA-Holarchy: An
R. (2023). Blended modeling in commercial and open- Enhanced PROSA Model to Enable Worker–Cobot
source model-driven software engineering tools: A Agile Manufacturing. International Journal of
systematic study. Software and Systems Modeling, Mechanical Engineering and Robotics Research, 7(3).
22(1), 415–447. https://doi.org/10.1007/s10270-022- Sarkisian, A., Vasylkiv, Y., & Gomez, R. (2022). System
01010-3 Architecture Supporting Crowdsourcing of Contents
Dong, Y., Jiang, X., Jin, Z., & Li, G. (2023). Self- for Robot Storytelling Application.
collaboration Code Generation via ChatGPT Sharaf, M., Abusair, M., Eleiwi, R., Shana’a, Y., Saleh, I.,
Fadjukoff, L., & Tolvanen, J.-P. (2022). Comparing the & Muccini, H. (2019). Modeling and Code Generation
Effort of Developing Enterprise Applications with Framework for IoT (pp. 99–115).
Programming and with Domain-Specific Modeling. Siricharoen, W. (2009). Ontology Modeling and Object
Feltus, C., Grandry, E., Kupper, T., & Colin, J.-N. (2017). Modeling in Software Engineering. International
Model-driven Approach for Privacy Management in Journal of Software Engineering and Its Applications,
Business Ecosystem: Proceedings of the 5th 3.

### International Conference on Model-Driven

Engineering and Software Development, 392–400.
FIPA, S. (2000). FIPA ontology service specification.
Citeseer.
Foundation for Intelligent Physical Agents. (2023).
http://www.fipa.org/

### Hailpern, B., & Tarr, P. (2006). Model-driven

development: The good, the bad, and the ugly. IBM
Systems Journal, 45(3), 451–461.
Kapferer, S., & Zimmermann, O. (2020). Domain-specific
Language and Tools for Strategic Domain-driven

### Design, Context Mapping and Bounded Context

Modeling: Proceedings of the 8th International
Conference on Model-Driven Engineering and
Software Development, 299–306.
Kelly, S., & Tolvanen, J.-P. (2008). Domain-Specific
Modeling: Enabling Full Code Generation. John Wiley
& Sons.
Liu, C., Bao, X., Zhang, H., Zhang, N., Hu, H., Zhang, X.,
& Yan, M. (2023). Improving ChatGPT Prompt for
Code Generation (arXiv:2305.08360).
OMG, O. I. (2006). Object management group. Needham,

## Ma, Usa, 2(2).

Perez-Martinez, J. E., & Sierra-Alonso, A. (2004). UML
1.4 versus UML 2.0 as languages to describe software
architectures. Lecture Notes in Computer Science
(Including Subseries Lecture Notes in Artificial