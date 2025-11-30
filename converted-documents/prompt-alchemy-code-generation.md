---
title: "Prompt Alchemy Code Generation"
original_file: "./Prompt_Alchemy_Code_Generation.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["prochemy", "code", "prompt", "generation", "shot", "tasks", "models", "prompts", "zero", "language"]
summary: "<!-- Page 1 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 1

Prompt Alchemy: Automatic Prompt Refinement for

### Enhancing Code Generation

Sixiang Ye∗, Zeyu Sun†, Guoqing Wang‡, Liwei Guo∗, Qingyuan Liang‡, Zheng Li∗, Yong Liu∗
∗Beijing University of Chemical Technology

### Beijing, China

Emails: yesx.sxye@gmail.com, liwei.glw@outlook.com, lizheng@mail.buct.edu.cn, lyong@mail.buct.edu.cn
†National Key Laboratory of Space Integrated Information System
Institute of Soft"
related_documents: []
---

# Prompt Alchemy Code Generation

<!-- Page 1 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 1

Prompt Alchemy: Automatic Prompt Refinement for

### Enhancing Code Generation

Sixiang Ye∗, Zeyu Sun†, Guoqing Wang‡, Liwei Guo∗, Qingyuan Liang‡, Zheng Li∗, Yong Liu∗
∗Beijing University of Chemical Technology

### Beijing, China

Emails: yesx.sxye@gmail.com, liwei.glw@outlook.com, lizheng@mail.buct.edu.cn, lyong@mail.buct.edu.cn
†National Key Laboratory of Space Integrated Information System
Institute of Software, Chinese Academy of Sciences

### Beijing, China

Email: zeyu.zys@gmail.com
‡Peking University

### Beijing, China


### Emails: guoqingwang@stu.pku.edu.cn, liangqy@stu.pku.edu.cn

Abstract—Code generation has gained increasing attention [3]. This capability accelerates the development process and
as a task to automate software development by transforming reduces human error by automating repetitive coding tasks.
high-level descriptions into executable code. While large lan-
As the demand for efficient software development grows, the
guage models (LLMs) are effective in generating code, their
use of large language models (LLM) for code generation has
performance heavily relies on the quality of input prompts.
Current prompt engineering methods involve manual effort in become increasingly significant [4].
designing prompts, which can be time-consuming and yield To effectively use LLM, prompt engineering plays an iminconsistentresults,potentiallyconstrainingtheefficacyofLLMs portantrole,involvingdesignandrefinementofinputprompts
in practical applications. This paper introduces Prochemy, a
to optimize model performance and improve the quality of
novel approach for automatically refining prompts iteratively
generated code [5], [6]. Early prompt engineering approaches
to enhance code generation. Prochemy addresses the limitations
of manual prompt engineering by automating the optimization focus on natural language processing tasks, including text
process, ensuring prompt consistency during inference, and generation and sentiment analysis [7], [8]. In these tasks,
aligning with multi-agent systems. It iteratively refines prompts few-shot learning enables models to adapt to new tasks with
based on model performance, using an optimized final prompt
minimal examples [9], [10]. The Chain of Thought (CoT)
to improve consistency and reliability across tasks. We evaluate
method enhances precision in complex tasks by incorporating

### Prochemy on both natural language-based code generation and

code translation tasks using three series of LLMs. Results show reasoning steps into prompts [6]. Recently, researchers who
thatwhencombiningProchemywithexistingapproaches,itout- supplement prompts with additional code contextual inforperformsbaselinepromptingmethods.Itachievesimprovements mation [3] or adopting multi-agent system approaches to
of 5.0% (GPT-3.5-Turbo) and 1.9% (GPT-4o) over zero-shot
debugging and regenerating existing code [11], [12], these
baselinesonHumanEval.Forthestate-of-the-artLDB,Prochemy
methods demonstrate improvements in the quality of code
+ LDB outperforms standalone methods by 1.2–1.8%. For code
translation, Prochemy elevates GPT-4o’s performance on Java- results.
to-Python (AVATAR) from 74.5 to 84.1 (+12.9%) and Python- Although prompt-based techniques have shown their effecto-Java from 66.8 to 78.2 (+17.1%). Furthermore, considering tiveness, their limitations become apparent in the realm of
thattheo1-minimodelintegratespromptengineeringtechniques,
code generation. Such tasks often involve intricate contextual

### Prochemy can continue to show good performance among it,

demands, and different coding challenges may hinge on spefurther validating its effectiveness in code generation and translation tasks. Additionally, Prochemy is designed to be plug-and- cific aspects of the prompt.
play, optimizing prompts with minimal human intervention and However, existing approaches depend on manually crafting
seamlesslybridgingthegapbetweensimplepromptsandcomplex optimal prompts, which is time consuming and susceptible
frameworks.
to errors. Human intuition often fails to meet the stringent
IndexTerms—CodeGeneration,PromptRefinement,Automa- demands of coding standards, which could lead to suboptimal
tion results. Furthermore, human-designed prompts may not align
consistently with the specific needs of LLM, which can
I. INTRODUCTION compromise performance [13].
To mitigate these problems and enhance code generation,

### CODEgenerationhasbecomeatransformativeapplication

the necessity for an automated prompt optimization approach
in software engineering, allowing the automatic generabecomes evident. This approach must address two key chaltionofcodefromhigh-leveldescriptionsorspecifications[1]–
lenges. The first challenge is automation: it should leverage
ManuscriptreceivedApril19,2021;revisedAugust16,2021. algorithms to analyze coding contexts, automatically gener-
5202
raM
41
]ES.sc[
1v58011.3052:viXra

<!-- Page 2 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 2

ating prompts that accurately capture the specific needs of tegrates seamlessly into current frameworks. This adapt-
LLMs on diverse coding tasks. Once generated, the prompt ability allows for its use without requiring modifications
must be fixed for use during inference, ensuring that it to established workflows.
can be reused without adjustments. The second challenge is • We conduct extensive empirical validation of Prochemy
compatibility: the approach should ensure alignment with across multiple datasets and language models, demonexisting techniques, such as multi-agent approaches. This stratingconsistentimprovementsinperformanceforboth
compatibility will enable integration into current workflows, natural-language-based code generation and code transultimately enhancing both performance and efficiency in code lation tasks. This evaluation confirms the robustness and
generation. generalizability of Prochemy across diverse architectural
Toaddressthesechallenges,weproposeProchemy(derived frameworks.
from Prompt Alchemy), a novel execution-driven automated
promptgenerationframeworkdesignedtoguideLLMsincode II. RELATEDWORK
generation tasks. For automation, Prochemy begins with an Fine-tuning large language models (LLMs) for different
initial prompt, such as a zero-shot prompt, and iteratively domainsisadauntingtask[21],particularlywhendealingwith
refines it based on the model’s performance evaluated by the sheer volume of parameters, such as DeepSeek-V3, which
execution.Thisrefinementusesatrainingsetderivedfromex- contains 671 billion parameters [20]. In response, prompting
istingdatasetsandtheirgeneratedvariations.Theprocessaims techniqueshaveemergedasapreferredstrategytoadaptLLMs
toalignthepromptwiththeneedsofLLMs,enhancingitsac- for specific tasks by supplying a specialized prompt [22].
curacyforspecifictasks.Aftertheserefinements,thepromptis PromptEngineeringforNaturalLanguage. Earlyefforts
finalizedandset,ensuringitcanbereusedconsistentlywithout in prompt engineering for LLMs revolved around zero-shot
further adjustments. For compatibility, Prochemy is designed and few-shot prompting [9], [10]. In zero-shot prompting, the
asaplug-and-playapproachthatintegratesseamlesslywithout model is required to generate code directly based on the task
requiringanymodificationstoexistingpromptmethodologies, description, without any prior examples. This method enables
such as CoT and multi-agent systems. LLMs to tackle diverse tasks but may lack accuracy in more
We conduct experiments on natural-language-based code complexscenarios.Few-shotpromptingextendsthistechnique
generation and code translation tasks using three se- by incorporating a few example pairs of tasks and correries of LLMs: the ChatGPT series [9], [14], [15], the sponding responses, allowing the model to learn from these
Claude series [16], [17], and the DeepSeek series [18]– samples and adjust its outputs accordingly. This example-
[20]. Prochemy enhances code generation and translation basedapproachenhancesthemodel’saccuracy,leveragingthe
across LLMs, achieving average gains of +4.04% (zero- provided information to guide its reasoning process.
shot), +4.55% (chain-of-thought), and +2.00% (multi-turn) Researchers have advanced prompt engineering to enon HumanEval/MBPP benchmarks. Correctness-critical vari- hancemodels’reasoningcapabilities.Chain-of-Thought(CoT)
ants (HumanEval+/MBPP+) see +4.21–7.76% improvements, prompting [23] instructs models to articulate intermediate
with LDB integration reaching state-of-the-art results (96.3% reasoning steps, improving performance on tasks that require
on HumanEval). On LiveCodeBench, Prochemy delivers logical, step-by-step problem-solving. This technique ensures
+14.15% (zero-shot) and +12.28% (chain-of-thought) aver- more coherent and accurate handling of complex tasks.
age gains. For code translation, it achieves +13.68% (Java- Automated methods like the Automatic Prompt Engineer
Python) and +8.25% (Python-Java) average improvements on (APE) automate the optimization of LLM instructions, often
CodeNet and AVATAR datasets. Considering that the o1-mini exceeding the performance of human-written prompts by remodelintegratesCoTtechniques,wesubsequentlyappliedthe fining model behavior to enhance results like informativeness
same Prochemy approach to this model. Prochemy continues andtruthfulness[24].Similarly,ProTeGiusesgradientdescent
to show good performance, further validating its effectiveness methodology to optimize prompts automatically, improving
incodegenerationandtranslationtasks.Theseresultsvalidate task performance by up to 31% [25]. The LLM as the
Prochemy’s unified framework, which aligns prompts with Optimizer (OPRO) method uses LLMs’ natural language untask requirements and model capabilities without architectural derstanding to iteratively refine prompts and enhance soluchanges, establishing a scalable paradigm for LLM-driven tion quality. Without relying on gradient-based techniques,
code tasks. it adjusts solutions based on past evaluations, effectively
We summarize our contributions in this paper as follows. balancing exploration and exploitation to improve problem-
• We propose Prochemy, the first approach designed to solving efficiency [26].
specifically optimize prompts for code generation tasks. Black-BoxPromptOptimization(BPO)[27]enhancesLLM
It iteratively refines prompts by analyzing the model’s alignment for the natural language processing tasks by opperformance against a training set composed of existing timizing user prompts based on human preferences without
datasetsandtheirgeneratedvariations.Prochemyrequires modifying model parameters. It boosts model output quality
only a single training run for a given task. After the across various tasks and outperforms methods like PPO [28]
optimization process, the prompt is fixed as the final andDPO[29],offeringanefficientandinterpretablealignment
prompt. solution.
• Prochemyiscompatiblewithexistingpromptengineering Prompt Engineering for Code Generation. In the domethodologies, offering a plug-and-play solution that in- main of software engineering, traditional prompt engineering

<!-- Page 3 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 3

2) Optimization

### Initial Prompt Selected Prompt Final Prompt

You are a code generation assistant. Mutate You are a code generation assistant
Your task is to generate Python code specializing in Python programming.
based on … Prompt A Your objective is to …

### Else

Prompt B
… Stop
1) Training Set Generation a) Mutation
Max Iterations or

### Add Code

Description Early Stop?
b) Evaluation

### LLM LLM c) Selection

Existing Data Mutated Data
Generate

### Prompt


### Code A’

Code B’ Get the Prompt
… withthehighestscore
Compute 42.97
Test Score
Evaluate
55.87

### Training Set


### Fig.1. OverviewofProchemy

methods designed for natural language tasks face limitations for evaluating the effectiveness of prompts (in Sec. III-B).
due to the need for strict adherence to standards [4]. 2) Optimization aims to iteratively refine prompts through
To overcome these challenges, researchers have developed three sub-steps III-C: a) Mutation—Generates variations of
specialized approaches that integrate structured reasoning and existing prompts to introduce diversity and explore different
multi-agent systems. For example, SCoT (Structured Chain- structures,providingapoolofcandidatesforfurtherevaluation
of-Thought) leverages program architecture to enhance code (in Sec. III-C1). b) Evaluation—Assesses the performance of
generation accuracy by using programmatic structures [3], these mutated prompts using the training data, employing a
while agent-based systems like AgentCoder combine special- weighted averaging mechanism to determine their effectiveized agents—such as test designers, executors, and program- ness(inSec.III-C2).c)Selection—Choosesthemosteffective
mers—toautomatetestingandimprovecodequality[11].Self- prompt from the pool based on their evaluated performance,
collaborationframeworksalsosimulatehumansoftwaredevel- guiding the subsequent mutation process (in Sec. III-C3).
opment processes, optimizing models for complex program- In particular, Prochemy requires only a single training run
ming tasks [30]. Furthermore, techniques like LDB (Debug- for a given task. After the optimization process, the prompt is
Like-Human) use runtime information and program segmen- finalizedandsetasthefinalprompt.Thisstreamlinedapproach
tation to improve debugging [12]. Despite their effectiveness, not only enhances efficiency but also ensures that the refined
these methods often struggle with high token consumption, prompt is tailored for optimal performance and can be reused
highiterationcounts,andlimitedapplicabilityacrossdifferent consistently without further adjustments in the context of the
models. task at hand.
Our approach is designed to create a flexible prompt optimization pipeline that is suitable for a range of models.

### B. Training Set Generation

This pipeline refines prompts by utilizing insights gained
The training set generation step is designed to create a
fromprogramexecution,aimingtodiscoverthemosteffective
dataset T that facilitates the indirect evaluation of prompt
discrete prompt for code generation. This approach can be
quality. In the context of code generation, this step constructs
integrated with existing prompt engineering techniques to
the dataset where each data entry T ∈T consists of an input
achieve improved results. i
natural language description T(NL) and its corresponding set
i
ofexecutabletestcasesT(test),ensuringthateachdescription

### III. APPROACH i

isactionableandtestable(T =(T(NL),T(test))).Thisdataset
i i i

### A. Overview

is derived from two primary sources: existing training data
To optimize prompts in a plug-and-play manner and it- from datasets, and new data generated by LLMs through
eratively refine them based on the model’s performance, mutation processes applied to pre-existing data.
Prochemy involves two steps, as illustrated in Fig. 1: 1) a) Existing Data: For existing data, we construct the
Training Set Generation aims to generate the training set trainingsetD viaimplementingasamplingstrategy.This
existing

<!-- Page 4 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 4

involves randomly selecting samples from existing datasets retains the core semantic structure but incorporates changes
until K samples are obtained1. in linguistic or structural elements, allowing for a detailed
b) Mutated Data: To enhance the diversity of our train- evaluation of how these variations influence the performance
ing set, we utilize an automated data augmentation mecha- of the LLM. The modifications include adjustments such as
nism that generates new data through mutations by LLMs. rephrasing sentences, refining clarity, or altering the presenta-
Prochemy employs LLMs to create additional samples by tion of task instructions.
mutating reference data, which is randomly sampled from Formally, given the set of selected prompts S(k−1) from
existing datasets but does not overlap with the previously iteration k −1 (for the first iteration, S(0) contains only an
mentioned existing data D . Specifically, the initial input initial prompt like zero-shot or CoT), the mutation process
existing
for mutation is a random sample from the existing dataset, produces a new set P(k) (|P(k)|=n ) of prompt variants for
ensuring that the mutated data is different from the existing iteration k:
ones.
Formally, we sample L distinct reference data from the P(k) ={P(k),P(k),...,P(k)},
1 2 n
existing datasets, ensuring no overlap with D . For each
existing
reference data, we use the LLM with a specific prompt to where each P(k) is generated by applying a mutation
i
mutate it into new samples that are different from the existing function m to a randomly sampled prompt S(k−1) from the
j
data. The specific prompt is as follows: ”You are an expert selected set S(k−1):
insoftwareengineering.Pleasehelpmegeneratesimilardata
basedontheformatprovidedbelow.Thereferencedataformat
P(k) =m(S(k−1)), S(k−1) ∈S(k−1).
is as follows.” This process is repeated K times, resulting i j j
in a total of K generated samples. To ensure correctness,
The transformation function m(·) introduces variations into
eachgeneratedsampleundergoesvalidationthroughtwosteps:
the prompts by adding modifications to the original prompt
(1) executing the code to verify functional integrity, and (2) S(k−1). These changes are designed to explore different exevaluating against model-provided test cases. Only samples j
pressions while preserving the original intent of the prompt.
passing both validation phases are retained. In this paper, we

### The specific prompt is as follows: You are an expert prompt

set K =10. The resulting samples are retained as the content
engineer. Please help me improve the given prompt to get a
of D .
gen more helpful and harmless response.

### The final training set is a combination of these two data

2) Evaluation: The evaluation process systematically assources, denoted as T = D ∪ D . This training set
existing gen sesses the effectiveness of mutated prompts by analyzing
T serves as the foundation for further evaluation of prompt
execution results of their generated code implementations,
quality and performance.
including metrics of functional correctness and runtime performance. This execution-based analysis enables the identifi-
C. Optimization cation of optimal prompt variants in each iteration through
The optimization step of Prochemy focuses on refining quantitative comparisons of code behavior across different
prompts iteratively to maximize their effectiveness for code problem instances.
generation tasks. This phase involves three sub-steps, each To achieve this, Prochemy applies each mutated prompt
designed to progressively enhance the quality of prompts P(k) to every dataset entry T = (T(NL),T(test)) in the
i j i i
through mutation, evaluation, and selection. These iterative generated training set T. It concatenates the prompt P(k)
i
cycles are aimed at continuously improving prompt perfor- with the natural language description T(NL) of each task.
i
mance, adapting to evolving task requirements, and learning Then, Prochemy feeds this concatenated input into the LLM,
frompreviousiterations.Theprocessisdesignedtorepeatfor which produces outputs R(k). Each output R(k) is evaluated
ij ij
a maximum of k max iterations, ensuring thorough exploration against the associated test suite T(test) using specific criteria
while preventing excessive computation. In this paper, k is i
max C, resulting in a score M for each prompt-task pair. This
set to 10. ij
process ensures that the effectiveness of each prompt is
1) Mutation: The primary goal of the mutation process
quantitatively assessed in the context of its ability to generate
is to generate a diverse set of prompts by mutating existing
correct and functional code. Here, C denotes execution-based
ones.Thisapproachfacilitatesthecreationofabroadrangeof
evaluation metrics derived from code runtime verification. In
prompt variations, allowing for a comprehensive exploration
code generation tasks, we employ the pass@1 metric where
and subsequent selection of the most effective prompts to
M ∈ {0,1} is determined through automated test case
enhance task performance. ij
execution - assigning 1 only if the generated code passes all

### This process is achieved by generating a series of modified

ground-truth test cases on initial execution. This executionprompt variants P(k) based on prompts selected from the
i driven paradigm ensures metrics fundamentally reflect funcprevious iteration. In particular, for the first iteration, the
tional correctness rather than surface-level code similarity.
prompt can be set to the simple zero-shot prompt or the wella) Weighted Scoring Mechanism.: To optimize the evaldesigned prompt of existing approaches. Each variant P(k)
i uation process and facilitate informed prompt selection, a
weighted scoring mechanism is employed. This mechanism
1In our experiments, the selected datasets do not overlap with our test
dataset(Dtest),ensuringtheindependenceofourtrainingandtestdatasets. prioritizes the evaluation of each dataset entry T j based on its

<!-- Page 5 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 5

complexity. The underlying principle is that if the code gen- highest weighted score is selected as the final output prompt
erated by a multitude of prompts correctly solves a particular P∗ ∈ S . If there are multiple prompts with equally high
k
dataset entry T , this suggests that the data may be relatively scores, one is chosen at random to be P∗ ∈S .
j k
simple and less critical. Consequently, less weight is assigned
to such data entries, reflecting their lower importance in the

## Iv. Experimentalsetup

overall assessment of prompt effectiveness. This approach
ensures that more complex and challenging tasks, which are In this section, we describe the dataset, large language
harder to solve correctly, have a greater influence on the models, evaluation metrics, and experimental platforms. Our
selection of the most effective prompts. evaluation is designed to answer the following research ques-
Formally, this mechanism assigns weights w to tasks T tions.
j j
based on their complexity and the number of times they are RQ1. How does Prochemy perform compared to other
successfully solved in this iteration: methods? To answer this question, we conduct experiments
on two tasks with seven datasets and compare Prochemy with
|P(k)|
state-of-the-art approaches.
w = ,
j N (T ) RQ2. What effects do each component in the Prochemy
successful j
have? To answer RQ2, we analyze Prochemy by removing
where |P(k)| is the total number of prompts variants, and
each component to discern its specific contribution to the

### N (T )isthenumberoftimesT issuccessfullysolved

successful j j overall effectiveness of Prochemy.
in this iteration.
The overall weighted score for each prompt P(k) is calcu- RQ3.InwhatkeyaspectsandtowhatextentdoesProchemy
i improvemodels’codecapabilitiescomparedtopreviousmethlated as:
ods? To answer this question, we illustrate a case study, ana-
W (P(k))= (cid:88) w ·M . lyzingspecificcodetaskstoassessimprovementsinaccuracy,
S i j ij efficiency, and generalization. We compare these results with
j
previous methods to highlight Prochemy’s key advantages.
3) Selection: After evaluating the performance of each
mutatedprompt,thepromptselectionstepfocusesonchoosing
the most effective prompts to carry forward into subsequent A. Dataset
iterations or to serve as the final output prompt. We evaluate Prochemy on two distinct types of code gen-
In each iteration k, the selection function is applied to the eration tasks. The first type is Natural-Language-Based Code
results of evaluation W S (P). Specifically, the prompt(s) with Generation, which involves generating executable code from
thehighestweightedaveragescoreisselectedasthereference natural language descriptions. This task tests the ability of
for the next round of mutation: Prochemy to accurately interpret human language and produce functional programming code. The second type is Code
S(k) ={P |P =arg max W S (P′)}. Translation, which requires translating a program from one

### P′∈P(k)

programming language, which serves as the input description
If there is a single prompt with the highest score, it is used
in Prochemy, to another. This task assesses the capability
directly. If multiple prompts share the highest score, all are
of Prochemy to maintain logical and syntactical correctness
retained. The selected prompt(s) S(k) serve as the basis for
across different programming languages.
generating new mutations in the next iteration.
1) Natural-Language-Based Code Generation: We eval-
If,uponreachingtheconvergencecriteria,therearemultiple
uate the effectiveness of Prochemy using five widely
prompts with the same highest weighted average score, we
adopted natural-language-based code generation datasets: Hurandomly select one of these prompts as the final result.
manEval [1], MBPP [31] and its enhanced versions, Hua) Convergence Toward Optimal Prompt.: The iterative
manEval+, and MBPP+ [32]. To mitigate data leakage
process continues until one of the following termination conduring large language model training, we also use Liveditions is met: (1) Early Stop: the highest weighted score
CodeBench [33], a code generation dataset that is updated
remainsunchangedforthreeconsecutiveiterations,or(2)Max
over time.

### Iterations: a maximum number of iterations is reached. This

HumanEval and HumanEval+. The HumanEval and Huapproachensuresthatthemethodefficientlyconvergestoward
manEval+ datasets each consist of 164 programming chalthe optimal prompt P∗ without unnecessary computational
lenges designed to assess a model’s problem-solving capaeffort.
bilities in Python. In HumanEval, each problem includes an

### Formally, the convergence condition can be defined as:

average of 7.7 test cases, focusing on fundamental to intermediate concepts. HumanEval+, on the other hand, extends
(W (S(k))=W (S(k−1))=W (S(k−2)) & k ≥3) theoriginaldatasetwithmoreextensivetesting,providingtest

### S j S j S j

cases that exceed the original dataset by an average of 80
or k ≥k .
max
times.Thisincreaseintestcasesraisesthedifficultyandrigor
Here, S(k) ∈ S(k) (the score of any S(k) ∈ S(k) is equal), of the evaluation, making HumanEval+ particularly suitable
j j
and k represents the current iteration number. Upon reaching for benchmarking advanced models with a higher emphasis
one of these termination conditions, the prompt with the on robustness and accuracy across complex scenarios.

<!-- Page 6 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 6

MBPP and MBPP+. These datasets assess a model’s a) Single-Turn Methods: rely on a single prompt-
Python proficiency and ability to handle various coding tasks. response interaction for generating code solutions. This type
MBPPevaluatesfundamentalprogrammingskills,andMBPP+ of method contains: 1) Traditional Methods include baenhancesitbyprovidinganaverageofover35timesmoretest sic approaches like Zero-Shot and Chain-of-Thought (CoT)
casesthantheoriginal,improvingtheevaluationoffunctional prompting, which represent standard prompting techniques
correctness under diverse conditions. without iterative optimization or specialized prompt engi-
LiveCodeBench. This dataset addresses the critical chal- neering. 2) Prompt Optimization includes advanced prompt
lengeofdatacontaminationinLLMevaluationbyexclusively optimization approaches. The Automatic Prompt Engineer
curating time-stamped programming problems collected in (APE) [24] generates candidate instructions via LLMs and
real-time from competitive coding platforms and technical selectsoptimalpromptsthroughiterativescoring.Optimization
interviews. To ensure temporal separation from pre-training by PROmpting (OPRO) [26] leverages LLMs as natural landata,our experimentsutilize theofficialrelease-v4 litesubset, guageoptimizers,iterativelyrefiningsolutionsbasedonhistorcomprising 101 representative tasks systematically sampled ical evaluations. Black-box Prompt Optimization (BPO) [27]
from problems released between May 2023 and Septem- aligns LLMs by optimizing user prompts without parameter
ber 2024. Each challenge integrates dynamically generated updates,usinghumanpreferencestoenhanceintentalignment
test suites encompassing edge cases, explicitly designed to for untrainable models like GPTs. We adopt them due to the
emphasize real-world problem-solving patterns rather than absence of code-specific optimization baselines.
syntheticbenchmarks.Byanchoringevaluationstochronolog- b) Multi-Turn Methods: To better encode the code
icallynovelprogrammingchallengesunavailableduringmodel knowledge.Theseapproachesinvolveiterativeorcollaborative
training, LiveCodeBench establishes a rigorous framework interactions to enhance code generation performance.
for assessing genuine model generalization capabilities while Multi-Turn Methods include Self-Collaboration [30],
mitigating memorization effects inherent in static benchmark AgentCoder [11], CodeCoT [37], MapCoder [38] and
reuse. The lite subset maintains statistical parity with the LDB [12] provide structured interactions between multiple
full 713-problem corpus through stratified sampling across agentstocollaborativelyrefinecodesolutions.Thesemethods
difficulty levels and problem domains. are designed to improve accuracy through the collective input
2) Code Translation: For code translation, we use the Co- of several agents rather than relying on a single response.
deNet and AVATAR dataset to evaluate prompt performance. For our experiments, we select three representative and
CodeNet.TheCodeNetdatasetconsistsofprogramsinvar- high-performing methods in the multi-agent approach: Selfious languages [34], each solving specific tasks. Programs are Collaboration, AgentCoder, and LDB.
labeled as submissions (potentially incomplete or incorrect)
or solutions (accepted, executable, and correct across all test

### C. LLMs

cases). This dataset serves for understanding and improving
For LLMs, we use several widely adopted large language
programming practices and automated code evaluation.
models, including GPT-3.5-Turbo, GPT-4o, o1-mini, Claude-

### AVATAR.AVATARisacorpusof9,515programmingtasks

3-Haiku, Claude-3.5-Sonnet, and DeepSeek-V3, ensuring the
inJavaandPython,with3,391parallelindependentfunctions
method’s transferability across different models.
for training and evaluating program translation tasks [35]. It

### ChatGPT. Based on OpenAI’s GPT architecture, GPT-3.5-

includes problems from platforms like CodeForces, AtCoder,
Turbo offers faster processing and lower costs compared to

### AIZU,CodeJam,GeeksforGeeks,LeetCode,andProjectEuler,

GPT-3.5. GPT-4o-Mini is a smaller, cost-efficient variant of
and supports execution-based program translation evaluation.

### GPT-4, while GPT-4o provides strong language capabilities


### Following [36], we adopt rigorously validated subsets from

with lower computational demands. Additionally, the o1-mini
two established code repositories: (1) The CodeNet subset
model is a compact and lightweight version designed for scecomprises 200 Python and Java programming tasks, each
narios requiring efficient resource utilization, delivering balaccompanied by implementations in both languages, and (2)
anced performance with reduced computational overhead [9],
theAVATARsubsetcontains250algorithmdesignchallenges.
[14], [15].
All implementations are verified to pass their respective test

### Claude. Developed by Anthropic, Claude focuses on safe

cases through automated evaluation pipelines, ensuring funcand controllable AI interactions. Claude-3-Haiku is a spetionalcorrectnesspriortoexperimentalusage.Onaverage,the
cialized version designed for faster, efficient text generation
AVATAR subset has 25.02 test cases per task, while CodeNet
andcomprehension,makingitidealforreal-timeapplications.
has 1 test cases per task.
Additionally, Claude-3.5-Sonnet is an advanced iteration that
enhances the balance between performance and efficiency,
offering improved contextual understanding and nuanced text

### B. Baselines

generation, suitable for more complex and detailed tasks [16],
In our evaluation, we select a set of baseline methods [17].
specificallydesignedforcodegenerationandevaluationtasks. DeepSeek.TheDeepSeekseriesbyDeepSeekTechnologies
These baselines represent state-of-the-art approaches in the excels in natural language processing and code-related tasks.
field, categorized broadly into single-turn and multi-turn (or The latest version, DeepSeek-V3, represents a significant
multi-agent) methods. advancement, integrating and enhancing the capabilities of its

<!-- Page 7 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 7

predecessors into a unified, state-of-the-art model. DeepSeek- F. Experimental Platform
V3deliverssuperiorgeneralandcodingperformance,achieves

### We conduct the experiments on an NF5468M6 server with

better alignment with human preferences, and introduces optwo Intel Xeon Gold 6354 C processors and 512 GB of
timizations for writing tasks and instruction-following scenarmemory (16 x 32 GB DIMM DDR4). The server includes
ios. This version is designed to meet the growing demands of
a 480 GB and a 24 TB logical volume for ample storage.
complex applications, offering improved efficiency, accuracy,
It is equipped with eight NVIDIA RTX 4090 GPUs for
and versatility [20].
high-performance computing and has eight Gigabit Ethernet
interfaces for reliable data transmission.
D. Parameter Settings

## V. Resultsandanalysis

Intheexperiments,thetemperatureparameterissetto0for

### A. RQ1: How does Prochemy perform compared to other

bothcodegenerationandcodetranslation,acommonpractice
methods?
when employing large language models for such tasks [11],
[12], [39]. For the prompt mutation process, the temperature To address the first research question, we assess the perforis set to 1.0 to increase diversity and creativity, allowing for mance of Prochemy on two types of tasks: natural-languagenovel and varied prompt mutations. based code generation and code translation.
The training set consists of 20 data samples, with 10 1) Natural-Language-BasedCodeGeneration: Weevaluate
samples sourced from each of the two primary categories: natural language-based code generation across five bench-
(1) existing data, and (2) LLM-mutated data. For existing marks: HumanEval/MBPP (base functionality), their augdata, to ensure that they are distinct from the test set, we mented versions HumanEval+/MBPP+ (strict correctness and
randomlysample10samplesfromanexternaldataset.Specif- robustness), and LiveCodeBench (dynamically refreshed chalically, for Code Generation tasks: HumanEval uses existing lenges for advanced code generation).
data from MBPP, MBPP uses data from HumanEval, and We first introduce the experimental results of HumanEval,
LiveCodeBench sources its existing data from AVATAR (code HumanEval+, MBPP, and MBPP+, where we select all basegenerationversion).ForCodeTranslationtasks:AVATARuses line methods for evaluation. Subsequently, we provide the
CodeNet data, while CodeNet uses AVATAR as its existing results of LiveCodeBench. Due to the complexity of the
data source. This cross-dataset curation ensures the indepen- problems and the high computational costs associated with
dence of the test set while preserving task relevance. For multi-round iterative approaches, we limited the baselines to
the mutation process, in each iteration, 10 different mutated include only non-iterative versions of single-round and multiprompts are generated. This number is selected to introduce round methods(projected to exceed hundreds of hours for
sufficient diversity into the prompt pool, enabling the explo- full multi-round evaluation). This choice is driven by the
ration of various prompt structures and linguistic variations need to balance evaluation comprehensiveness with resource
without incurring excessive computational costs. Generating constraints.
10 mutated prompts per iteration strikes a balance between Analysis of Prochemy Across Models on HumanEval,
diversity and efficiency. HumanEval+, MBPP, and MBPP+. The results of these
For the parameters in the LLM API calls, including max datasets are shown in Table I. We first examine the perfortokens, top p, and others, are kept at their default settings mance of Prochemy when integrated with zero-shot promptas specified by each model. When extracting code snippets ing. Across all datasets and models, Zero-shot + Prochemy
from the model’s results, we aim to prevent situations where consistently boosts performance, delivering an average gain
multiple code segments in a single response could result in of 4.04%. Notably, for the more challenging HumanEval+
the extraction of non-executable code. To address this, we and MBPP+ variants, Prochemy lifts average performance by
adoptthemethodproposedinpaper[32],extractingthelongest 4.21% and 4.43%, respectively. Such results also outperform
compilable code snippet from each model response. existing prompt optimization approaches by an average of
2.33%.Thisaverageimprovementisconservativelycalculated
by comparing the proposed method with the best-performing

### E. Evaluation Metric

approach among APE, OPRO, and BPO for each model.
Following previous code generation studies [3], [40], [41], Next, we explore the impact of Prochemy when combined
weadoptPass@1asourevaluationmetricforbothgeneration with explicit chain-of-thought reasoning. Here, Prochemy
andtranslationtasks.Inthismetric,thecodegenerationmodel provides an average improvement of 4.55% compared with
generates only one program in response to a given require- standalone CoT method. The synergy between Prochemy and
ment. The requirement is considered solved if the generated CoT is especially evident in complex reasoning tasks such
program passes all predefined test cases. The Pass@1 score is as HumanEval+ and MBPP+, which see gains of 5.52%
thencalculatedasthepercentageofrequirementsforwhichthe and 5.26%, respectively. This partnership also mitigates the
modelsuccessfullygeneratesaprogramthatpassesallthetest occasional instability of standalone CoT methods, which can
cases on the first try. This score provides a direct measure of sometimes decrease performance (e.g., Claude-3’s baseline
a model’s ability to produce fully functional and correct code CoT). By adaptively refining the logic in prompts, Prochemy
in a single attempt, reflecting both its precision and reliability ensuresthatthereasoningstepsremaincoherent.Asaconcrete
in practical applications. example, GPT-4o’s HumanEval+ performance rises by 7.6%

<!-- Page 8 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 8


## Tablei


## Prochemyondifferentmodels(Humanevalandmbpp)


### PromptingMethods HumanEval HumanEval+ MBPP MBPP+

GPT-3.5 GPT-4o Claude-3 DeepSeek-V3 GPT-3.5 GPT-4o Claude-3 DeepSeek-V3 GPT-3.5 GPT-4o Claude-3 DeepSeek-V3 GPT-3.5 GPT-4o Claude-3 DeepSeek-V3

### Single-Turn

Zero-Shot 72.6 90.2 76.8 90.2 68.9 81.7 68.9 84.8 75.9 86.5 80.2 87.6 65.3 72.5 68.8 73.0
Few-shot 75.0 90.2 78.0 90.9 70.1 84.8 68.9 86.6 76.5 88.6 80.2 88.1 68.0 73.0 69.6 73.3
CoT 75.6 91.5 76.2 89.0 70.1 85.4 67.1 82.9 78.8 87.8 79.4 87.8 65.6 73.4 68.5 71.7
APE 73.2 90.2 77.4 90.2 68.9 83.5 69.5 85.3 78.6 88.6 80.7 87.3 64.0 73.0 69.0 72.5
OPRO 75.0 89.0 74.4 89.6 69.5 83.5 67.7 86.0 78.8 88.9 80.4 86.8 65.9 73.3 67.7 72.8
BPO 75.6 90.2 76.8 91.5 69.5 86.0 68.3 86.6 78.6 88.6 79.9 88.4 66.1 72.8 69.3 73.5
Self-Collaboration-noiter 74.4 90.2 77.4 90.9 68.9 86.0 69.5 86.6 80.2 88.1 80.7 91.5 67.5 72.8 69.6 77.5
AgentCoder-noiter 75.6 87.8 78.7 91.5 69.5 84.1 70.7 85.4 79.4 87.8 81.2 90.2 67.5 73.4 70.1 74.9
LDB-noiter 76.2 91.5 78.0 91.5 70.7 84.8 70.1 85.4 80.7 89.7 81.0 90.7 68.3 75.4 69.3 75.1
Zero-shot+Prochemy 76.2 92.1 79.3 92.7 71.3 86.6 72.0 87.2 81.2 89.9 81.7 91.8 68.5 75.4 70.1 78.0
CoT+Prochemy 77.4 92.7 80.5 93.3 72.0 89.3 72.6 88.4 82.5 89.9 82.0 92.3 69.0 75.7 70.9 78.3

### Multi-Turn

Self-Collaboration 78.0 90.9 81.1 92.1 70.1 87.8 71.3 87.2 82.5 88.6 82.3 91.8 69.0 74.1 70.1 77.5
AgentCoder 79.3 92.7 80.5 93.3 73.2 87.2 72.0 85.4 82.2 88.9 82.8 91.5 69.3 75.1 71.1 76.7
LDB 82.3 94.5 81.1 92.7 78.0 88.4 73.2 88.4 83.1 89.9 83.6 92.3 69.3 74.9 70.6 75.7
Self-Collaboration+Prochemy 79.3 92.7 81.7 93.9 72.0 89.6 72.6 90.9 83.3 90.2 83.1 92.3 69.6 76.2 70.9 79.4
AgentCoder+Prochemy 81.1 93.9 83.5 93.3 73.8 89.3 73.8 90.2 82.8 90.7 83.3 92.1 70.1 77.2 71.7 78.3
LDB+Prochemy 83.5 96.3 84.8 94.5 79.3 90.2 73.8 90.9 83.9 92.6 84.1 93.1 70.4 80.7 71.4 78.8

## Tableii


## Prochemyperformanceondifferentmodels(Livecodebench)


### Prompting Methods Models

GPT-3.5-Turbo GPT-4o Claude-3.5-Sonnet DeepSeek-V3
Zero-Shot 10.9 22.8 12.9 24.8
Few-shot 6.9 21.8 11.9 24.8
CoT 11.9 20.8 16.8 22.8

## Ape 9.9 22.8 11.9 25.7


## Opro 9.9 20.8 13.9 23.8


## Bpo 10.9 22.8 11.9 20.8

Self-Collaboration-noiter 7.9 19.8 14.9 19.8
AgentCoder-noiter 11.9 19.8 7.9 16.8

### LDB-noiter 7.9 17.8 7.9 14.9

Zero-shot+Prochemy 12.9 23.8 16.8 25.7
CoT+Prochemy 12.9 24.8 16.8 27.7

## Tableiii


## Prochemyondifferentmodels(Codetranslation)


### PromptingMethods Java2Python Python2Java

GPT-3.5 GPT-4o Claude-3-Haiku DeepSeek-V3 GPT-3.5 GPT-4o Claude-3-Haiku DeepSeek-V3
CodeNet AVATAR CodeNet AVATAR CodeNet AVATAR CodeNet AVATAR CodeNet AVATAR CodeNet AVATAR CodeNet AVATAR CodeNet AVATAR
Zero-Shot 60.5 63.8 63.5 74.5 59.0 63.0 72.0 80.9 76.5 54.4 95.5 66.8 86.0 51.5 91.0 87.7
Few-shot 69.5 64.4 70.0 76.2 60.5 64.4 82.0 81.6 81.0 54.9 96.0 68.1 87.5 53.2 94.0 88.5
CoT 63.0 62.8 63.5 73.2 58.5 61.5 64.0 78.7 81.0 51.9 96.5 64.7 86.5 49.8 92.0 86.0
APE 61.0 64.9 72.0 77.0 60.0 63.6 82.0 83.4 79.0 55.3 96.5 66.0 87.0 56.2 94.0 87.2
OPRO 61.0 63.8 69.5 78.7 59.5 64.9 70.5 80.3 81.5 54.4 96.5 67.7 87.0 51.9 93.5 86.8
BPO 60.5 65.1 64.5 63.8 60.0 60.9 67.5 79.6 80.0 56.9 95.5 65.5 86.0 46.8 91.0 85.7
Zero-shot+Prochemy 73.0 66.0 79.5 84.1 64.0 68.5 86.5 88.9 83.0 57.7 97.0 78.2 88.5 61.9 95.5 91.9
when CoT is augmented by Prochemy—an improvement 2.45 complex multi-stage workflows.
greater than using CoT alone. Beyondtheaboveobservations,itisparticularlynoteworthy
Finally, we investigate Prochemy’s capacity to opti- that Prochemy delivers strictly positive gains for all tested
mize multi-turn code generation approaches such as Self- modelsanddatasetswithoutanyperformanceregressions.The
Collaboration, AgentCoder, and LDB. In these pipelines, consistent upward trend further validates Prochemy’s robust-
LLMs typically draw on domain knowledge over several ness and reliability as a prompting optimization framework.
iterations, but the initial and intermediate prompts can still AnalysisofProchemyAcrossModelsonLiveCodeBench.
be refined. In our experiments, we employ Prochemy to We further validate Prochemy’s transferability on the more
optimize the initial prompt of them, we observe an average challenging LiveCodeBench dataset, as presented in Table II.
improvement of 2.00%. HumanEval-series tasks experience Notably, only single-turn code generation methods are exthegreatestgains(+2.23%),followedbyMBPP-seriesbench- plored here, in part due to cost constraints and also to focus
marks(+1.77%).Thisiterativeoptimizationhelpsreduceerror on how Prochemy performs under more direct prompting
propagation, ultimately improving the seed program’s quality. scenarios. Additionally, the use of a higher-capacity Claude-
Notably, Prochemy-enhanced LDB establishes new state-of- 3.5-Sonnet model reflects the increased difficulty of Livethe-art results across all benchmarks, including 96.3% (GPT- CodeBench, enabling a clearer assessment of Prochemy’s
4o on HumanEval), 90.9% (DeepSeek-V3 on HumanEval+), robustness across varying model strengths.
and 93.1% (DeepSeek-V3 on MBPP). These results under- For all models tested, Prochemy strengthens the baseline
score Prochemy’s strength in refining dynamic prompts for Zero-Shot results, with especially large gains for less ad-

<!-- Page 9 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 9

vanced architectures. After applying the Prochemy method, ation challenges but also highlights its potential as a unifying
the average performance improved by 14.15% compared to prompting framework, bridging the gap between specialized
the zero-shot method. Claude-3.5-Sonnet, for example, im- transformations and more generic LLM-driven development
proves substantially from 12.9 to 16.8 (+30.2%), emphasiz- workflows.
ing Prochemy’s ability to refine underperforming baselines.
Meanwhile, DeepSeek-V3 and GPT-4o shows a smaller but Answer to RQ1: Prochemy delivers consistent perforstill positive improvement (24.8 → 25.7, +3.6%, and 22.8 → mance gains across code generation and translation tasks.
23.8, +4.3%). For code generation, it achieves +4.04% (zero-shot),
Beyond Zero-Shot settings, Prochemy also enhances +4.55% (CoT), and +2.00% (multi-turn) average imreasoning-oriented methods, achieving an average improve- provementsoverbaselines,withHumanEval+/MBPP+seement of 12.28%. For GPT-4o, combining Prochemy with ing+4.21–7.76%gains.Itsetsnewstate-of-the-artresults
chain-of-thought reasoning yields a pass@1 of 24.8, translat- (e.g., 96.3% on HumanEval) through LDB integration.
ing to a 19.2% gain over standalone CoT (20.8). DeepSeek- On LiveCodeBench, Prochemy boosts zero-shot and CoT
V3 demonstrates a similar pattern, where CoT + Prochemy performance by 14.15% and 12.28%. In code translation,
achieves 27.7, representing a 21.5% jump over vanilla CoT itachieves+13.68%averageimprovementonJava-Python
(22.8). These results affirm that Prochemy can often amplify tasks, and +8.25% on Python-Java tasks. These results
structured reasoning, especially in models with well-aligned validate Prochemy as a unified, efficient framework for
CoT capabilities. code-related LLM optimization.
Across all tested architectures, Prochemy consistently surpasses specialized prompt optimization approaches like APE,
OPRO, and BPO. For example, on GPT-4o, Zero-Shot + B. RQ2: What effects do each component in the Prochemy

### Prochemy (23.8) outperforms APE (22.8), OPRO (20.8), have?

and BPO (22.8), underscoring the effectiveness of systematic To thoroughly assess the contributions of individual comprompt refinement over hand-tuned strategies. These findings ponents within Prochemy, we conduct ablation experiments
illustrate that Prochemy’s improvements hold even on ad- by systematically removing specific elements of the iterative
vanced datasets such as LiveCodeBench. process.Specifically,weexaminetheeffectsof(1)eliminating
2) Code Translation: We further extend the evaluation of the iterative optimization to understand its impact on model
Prochemy to code translation tasks, systematically investigat- performance, (2) using a fixed number of iterations (e.g., 10
ing its efficacy in code-to-code generation scenarios beyond iterations)toevaluatethenecessityofadaptiveiterationcounts
conventional natural language-to-programming language set- with early stopping, and (3) removing the weighted scoring
tings. Table III demonstrates Prochemy’s performance across mechanism used for selecting prompts during iterations to
models and datasets. determine its role in accelerating convergence and enhancing
Similar results are observed in code generation tasks, performance. By isolating and analyzing these components,
Prochemy boosts Zero-Shot performance, achieving an av- we aim to understand their individual contributions to the
erage improvement of 13.68% in Java-to-Python translation overall effectiveness of Prochemy in code generation tasks.
tasks, And in Python-to-Java task, this value is 8.25%. For In particular, we conduct this ablation test on the HumanEval
instance,inJava-to-PythontranslationontheAVATARdataset, dataset due to the cost.
GPT-4o scores 84.1 under Zero-Shot + Prochemy, represent- 1) Iteration: Toevaluatetheimpactoftheiterativeprocess
ing a 9.6% absolute gain over standalone Zero-Shot (74.5). inProchemy,weconductexperimentsunderdifferentiteration
TheseresultsunderscorehowProchemy’sadaptiverefinement settings.
strategy enhances clarity and precision, even in cross-lingual a) No Iteration: We begin by conducting experiments
code settings. withoutiterativeprocessing,asshowninTableIV.Acompar-
Across multiple datasets and models, Prochemy outper- ison between the non-iterative (w/o Iter) and original versions
forms specialized prompt optimization techniques such as of Prochemy indicates that the removal of the iterative proce-
APE,OPRO,andBPO.InDeepSeek-V3’sJava-to-Pythontask duregenerallyreducesthemethod’seffectivenessinimproving
on CodeNet, Prochemy + Zero-Shot achieves 86.5, notably modelperformance.ThisdeclinemaybeattributedtothenonexceedingAPE’s82.0andOPRO’s70.5.Moreover,BPOlags iterative method’s limited ability to explore different direcfurtherbehindat67.5.Thisperformancegapalignswithfind- tions, constraining its capacity to identify the most effective
ings in other code generation benchmarks (e.g., HumanEval+ prompts for the given tasks.
and MBPP+), where Prochemy consistently balances speci- b) Fixed Iteration Count of 10: We also conduct exficity and flexibility without over-constraining the output. periments with a fixed iteration count of 10. This choice
The results in code translation extend the evidence of is informed by preliminary findings, which suggest that at
Prochemy’s versatility across diverse programming tasks. By this number of iterations, most models have already produced
dynamically adjusting prompt structures to accommodate dis- results that meet the early stopping criteria.
tinct source–target requirements, Prochemy effectively gener- We evaluate the performance of each model on the
alizes beyond single-language code generation and natural- HumanEval dataset using both the early stopping method
language-to-codemapping.Thisadaptabilitynotonlycements (Prochemy) and the 10-iteration approach (Iter 10). The re-
Prochemyasarobustsolutionforawiderangeofcodegener- sults, as shown in Table IV, demonstrate that Prochemy using

<!-- Page 10 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 10


## Tableiv


## Ablationstudyofiterationeffectsonprochemy’Sperformance

Models Zero-Shot w/o Iter Iter 10 Prochemy
GPT-3.5-Turbo 72.6 73.8 75.0 76.2

### GPT-4o 86.0 89.6 90.2 92.1

Claude-3-Haiku 73.7 76.2 77.4 78.7
DeepSeek-V3 87.2 87.8 89.6 90.2

## Tablev


## Ablationstudyofweightedscoreeffectsonprochemy’Sperformance

Models w/o WS Prochemy Reduction (%) w/o WS Prochemy Improvement (%)
Iterations Iterations Iterations Pass@1 Pass@1 Pass@1
GPT-3.5-Turbo 5.2 4.0 23.1% 70.7 76.2 3.5%

### GPT-4o 4.2 3.3 21.4% 90.2 92.1 2.1%

Claude-3-Haiku 5.4 4.3 20.4% 73.1 78.7 7.7%

### DeepSeek-V3 4.4 3.6 18.2% 87.2 90.2 3.4%

early stopping consistently outperforms the version with a scores.TheintegrationofProchemy’sweightedscoringmechfixed number of iterations. On average, models show an anism results in an average improvement of 4.2% in pass@1
improvement of around 1.50% in pass@1 scores when using scores across models, showcasing substantial enhancement.
early stopping compared to the 10-iteration approach. This This highlights the benefits of employing such a mechanism.
trend is consistent across all models, suggesting that the early Additionally,acrossallmodels,feweriterationsarerequired
stoppingmethodoptimizespromptrefinementmoreeffectively toconvergewhenusingtheweightedscoringmechanismcomand efficiently than extending iterations without significant pared to the unweighted setting. On average, models require
additional gains. 20.8% fewer iterations with weighted scoring compared to
Whencomparingthefixed10-iterationapproach(Iter 10)to the w/o WS setting. This reduction in iterations is consistent
thenon-iterativeversion(w/oIter),itisevidentthatadditional across different models, highlighting the efficiency of the
iterationsleadtonotableimprovementsinmodelperformance, weighted scoring mechanism.
with an average increase of 1.48% across models. This trend These findings emphasize that the inclusion of weighted
confirms that iterative refinement effectively enhances the scoring facilitates a more targeted and efficient optimization
models’ ability to generate more accurate and contextually process. It not only reduces the number of iterations needed
relevant code. but also enhances the final output quality, streamlining the
2) Weighted Score: Another ablation experiment aims to prompt refinement process effectively.
evaluate the effectiveness of the weighted scoring mechanism
in Prochemy.

### Answer to RQ2: Ablation studies show that each com-


### In the w/o WS (without weighted scoring) setting, the

ponent of Prochemy enhances its performance. Iterative
weighting mechanism is not applied; instead, the original
processingimprovespass@1scores,asnon-iterativemethpass@1 values are directly used to select the best prompt for
ods underperform. The early stopping mechanism and the
each iteration. This approach primarily affects both the perweightedscoringmechanismaccelerateconvergencewhile
formance of Prochemy and the number of iterations required
improving the final output.
to optimize the prompts effectively. Without the weighted
scoring, which prioritizes prompts based on their ability to
handlecomplextasks,theoptimizationprocessmaytakemore
iterations to converge to an optimal prompt, as each prompt

### C. RQ3: In what key aspects and to what extent does

is evaluated uniformly regardless of task complexity. This can

### Prochemy improve models’ code capabilities compared to

leadtolessefficientpromptrefinementandpotentiallyincrease
previous methods?
the computational effort required to achieve similar performance levels that are attained more swiftly with weighted To evaluate the improvements of the proposed Prochemy
scoring. over traditional prompting techniques in code generation
The results are shown in Table V. The first two columns withinamorespecificcontext,weconductacasestudybased
represent the number of iterations required to reach the con- on the results of the GPT-3.5-Turbo model.
vergence condition without and with the introduction of the 1) Interpretability of Prochemy: A key advantage of
weightedaveragingmechanism,whereasthelasttwocolumns Prochemyliesinitsenhancedinterpretability.Bydirectlycomrepresent the pass@1 scores. paring the instructions before and after optimization, we can
WeobservethatProchemyconsistentlyoutperformsthever- explicitly examine the mechanisms through which Prochemy
sion without weighted scoring (w/o WS) in terms of pass@1 operates. To analyze and generalize the optimization patterns

<!-- Page 11 -->


### Case 1 Optimized Prompt


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 11


### Code Generation

Zero-Shot Prompt: You are a code generation assistant. Your task is to generate Python code based on the given task
description and complete the work described in the task.
BPO Optimized Prompt: You are a code generation assistant. Your task is to generate Python code based on the given task
description and complete the work described in the task. Please ensure that the generated code is correct and follows the
given task description.
Prochemy Optimized Prompt: You are a code generation assistant specializing in Python programming. Your objective is to
accurately translate natural language task descriptions into executable Python code and ensure that the code passes any
provided test cases. Carefully review the given task description and write Python code that fulfills the specified requirements.
Please consider both efficiency and accuracy in your code generation process. Additionally, provide a detailed explanation of
the code's functionality and how it addresses the given task.
Role Clarification Efficiency and Accuracy Focus Goal Definition Ensuring Task-Specific Adaptation

### Fig.2. Case1forOptimizedPrompt

ofProchemy,wereview300samplesgeneratedduringtraining methods generate incorrect results, while Prochemy produces
and identified several recurring optimization strategies. the correct answer.
As illustrated in Figure 2, using a concrete example of The task requires implementing a function, count nums,
prompt optimization within a code generation task, we iden- which takes an array of integers and returns the number of
tify four frequently employed optimization strategies within elements where the sum of their digits is greater than zero. A
Prochemy: Role Clarification, Goal Definition, Efficiency keydetailisthatfornegativeintegers,theleadingdigitshould
and Accuracy Focus, and Ensuring Task-Specific Adaptation. be treated as negative.
These strategies are not mutually exclusive in practical use, The problem analysis clarifies why the zero-shot and CoT
and this example represents a typical instance where all four methods yield incorrect results. In the count nums zeroshot
are applied concurrently. function, the sum digits function incorrectly treats negative
• Role Clarification ensures that the model remains fo- numbers by converting them to their absolute values (num =
cused on the current software engineering task, rather abs(num)) before summing the digits. Thus, for input [-1, -2,
than responding to general inquiries. This focus enables 0], it computes -1 and -2 as 1 and 2, leading to errors.
the model to fully utilize its coding capabilities acquired Similarly, the CoT’s result mishandles negative numbers
during pre-training. by taking the absolute value (num = -num) and summing
• Goal Definition specifies the ultimate objective of the the digits as positive. This causes the same issue, incorrectly
current task, guiding the assistant to prioritize accuracy calculating -1 and -2 as 1 and 2 for the input [-1, -2, 0].
and correctness in code generation, thereby ensuring that In contrast, the code generated by Prochemy produces
the resulting solution satisfies the task requirements. correct results by using string manipulation to check if a
• Efficiency and Accuracy Focus emphasizes not only number is negative (str n[0] == ’-’). It treats the leading
correctness but also the optimization of code perfor- digit as negative and sums the remaining digits as positive,
mance. By applying this strategy, the model ensures that adhering to the problem’s requirements. This approach shows
the generated code maintains logical integrity, even in that Prochemy better understands the problem specifications.
edge cases or under complex testing conditions. Additionally, the code uses conditional logic, allowing it
• Ensuring Task-Specific Adaptation encourages the to handle inputs of varying lengths and types, accurately
model to take into account the unique nuances and computing the sum of digits and their signs for both positive
requirements of the specific task. During simulated gra- and negative integers.
dient descent, feedback from the training set enables Thisapproachremainsrobustforintegersofanymagnitude,
the model’s prompts to gradually converge towards the correctly handling all valid inputs—even with long integers
optimalcontinuousvectorspace.Inthecontextofdiscrete and complex edge cases from the enhanced HumanEvalvector representations, this process manifests as task- ET dataset. Additionally, code generated by Prochemy often
specific adaptation. The specific implementation of this includes crucial comments that enhance readability by exstrategy varies considerably based on the requirements plaining the logic and intent of each step, making the code’s
of the task. structure clearer and more intuitive—features less common in
In comparison, prompt optimization methods designed for zero-shot and CoT results.
natural language tasks, such as BPO [27], are limited to ad- 3) Case for Code Translation: In Figure 4, we conduct an
dressing only certain aspects of these strategies when applied analysisofthecodetranslationtaskusingatcoder ABC137 D
to code-related tasks. as a case study. The task involves implementing the function
2) Case for Code Generation: Fig. 3 shows the code max total reward, which takes three inputs: the number of
generation results for HumanEval/108 using different prompt- tasks (N), the number of days (M), and two datasets (Ai and
ing methods. The Zero-Shot and Chain of Thought (CoT) Bi). Ai represents the days after which the reward Bi can be

<!-- Page 12 -->

IEEETRANSCAaCseT 2IO HNuSmOanNEvSaOl/F1T0W8AREENGINEERING,VOL.14,NO.8,AUGUST2021 12
Case 3 atcoder_ABC137_D
3 4
4 3
4 1
3 5
2 2
(a) Zero-Shot (b) Prochemy
assert candidate([-1, -2, 0]) == 2 assert candidate([-1, -2, 0]) == 2 assert candidate([-1, -2, 0]) == 0
(Ca)a Zsereo -3Sh o attcoder_ABC137_D (b) CoT (c) Prochemy
Fig.3. Case2HumanEval/108forCodeGeneration
3 5
(a) Zero-Shot (b) Prochemy

### Fig.4. Case3atcoder ABC137 DforCodeTranslation

received if the task is completed. The goal is to return the unliketheoriginalPythoncodethatuses-dayand-salary
maximum total reward obtainable within M days. to simulate a max-heap properly. While the comparator in
The original Python code uses the “heapq” module to man- Java considers negative values, it does not apply them
age tasks in a min-heap (x), ordered by the latest completion consistently for task selection and reward comparison. This
day and reward. To simulate max-heap behavior, it stores leads to a logical inconsistency with the condition r ≥ −d;
negative reward values. A second min-heap (y) holds rewards unlike in Python, the Java version fails to ensure tasks can be
for eligible tasks, with a size limit of M days. completed within the remaining days, resulting in incorrect
The algorithm checks each task’s latest completion day (d). task eligibility determination.
Ifitcanbecompletedwithintheremainingdays(r),itsreward
isaddedtoheapy.Ifnot,therewardisadded,andthesmallest
The Java implementation by zero-shot fails to replicate
isremovedtokeeponlythehighestrewards.Thisensuresthat
the Python code’s core max-heap functionality for selecting
the maximum total reward is selected at each step.
optimal tasks based on rewards, leading to an inconsistencies

### The Zero-Shot method produces incorrect results due to

and incorrect results. In contrast, Prochemy’s code is more
critical issues in code translation. The original Python code
reliableandlogicallyconsistent.ItutilizestwoPriorityQueues:
simulates a max-heap using “heapq” with negative values, but
one to store tasks sorted by descending completion day and
thisismishandledintheJavaversion.InJava,PriorityQueueis
reward, and another as a min-heap for the rewards of eligible
a min-heap by default, requiring either an explicit comparator
tasks. An improvement is the use of the long type for day
or negative values to simulate a max-heap, both of which are
and salary variables, preventing overflow in large number
missing in the Java code.
operations and ensuring the code can handle larger datasets
The Java code’s custom comparator for
safely and efficiently.
PriorityQueue<int[]> mishandles negative values,

<!-- Page 13 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 13


### TABLEVI B. Time and Token Cost Analysis


## Prochemyperformanceono1-Minimodel(Livecodebench)

To systematically evaluate the computational efficiency of
Prochemy, we analyze token consumption and processing

### Prompting Methods o1-mini

overhead across different LLMs on three benchmarks (Hu-

### Zero-Shot 40.6

manEval,MBPP,LiveCodeBench)duringinference.TableVII

### Few-shot 38.6

and Table VIII presents the results with three metrics per

### CoT 36.6

APE 43.6 configuration: mean input tokens (first value), mean output
OPRO 41.6 tokens (second value), and average overhead in seconds (third

## Bpo 41.6

value), measured under controlled hardware settings.

### Self-Collaboration-noiter 37.6

AgentCoder-noiter 34.7 a) Token Cost Analysis: Prochemy achieves task-level
LDB-noiter 41.6 optimization with marginal token overhead compared to base-
Zero-shot+Prochemy 44.6 line methods. On HumanEval with GPT-3.5-Turbo, Zero-shot

### CoT+Prochemy 43.6

+ Prochemy requires 259 input tokens and 483 completion
tokens versus 184/358 for standard Zero-shot. This remains
15.8% more efficient than AgentCoder-noiter’s 304/576 to-
Answer to RQ3: Prochemy enhances model code cakens. For GPT-4o, Zero-shot + Prochemy maintains better
pabilities by improving interpretability through strategies
token economy than both AgentCoder and LDB. On MBPP,
like Role Clarification and Goal Definition, optimizing
the total token consumption of GPT-3.5-Turbo for Zero-shot
prompts, and simplifying debugging. Case studies show
+ Prochemy (251+339=590) shows moderate growth com-
Prochemy generates accurate, well-structured code, adparedtoZero-shot(124+191=315)yetstayscomparableto
vancing the programming capabilities of large language
specialized methods like AgentCoder (248+404=652). The
models.
pattern persists in LiveCodeBench, where Prochemy’s input
tokens (589) align with standard methods while completion
tokens(532)remain8.7%lowerthanAgentCoder-noiter(583).
VI. DISCUSSION Analogous phenomena are also observed in the multi-turn
approach implemented within the Prochemy.

### A. Prochemy on Reasoning Models (o1-mini)


### The marginal increase in Prochemy’s input tokens arises

In this discussion, we include o1-mini in our experi- from its optimized prompts, which incorporate richer contexments both because it is a high-performance model report- tualperspectives(e.g.,errorprevention,taskdecompositionin
edly equipped with built-in chain-of-thought capabilities and Fig. 2) to guide LLMs more comprehensively. Similarly, the
because OpenAI’s recent guidelines suggest that elaborate increase in completion tokens reflects Prochemy’s focus on
prompt engineering may offer less benefit for such advanced generating standardized, logically structured code in Fig. 3,
reasoning models [42]. However, the results in Table VI with additional comments and documentation that improve
(pass@1 column for o1-mini) show that Prochemy still con- code clarity and maintainability, thereby enhancing overall
tributes measurable improvements even for o1-mini. readability.
In single-turn settings, zero-shot prompting achieves a b) Overhead Analysis: For time cost, Prochemy demonpass@1of40.6,whereasfew-shot(38.6)andCoT(36.6)yield strates competitive time efficiency. In GPT-3.5-Turbo Hulower scores. Adding Prochemy leads to zero-shot+Prochemy manEval evaluations, Zero-shot + Prochemy completes in
at 44.6, which not only outperforms well-known techniques 2.79s versus 3.76s for standard Zero-shot - a 25.8% reduction
such as APE (43.6) and LDB-noiter (41.6) but also achieves despitehighertokenusage.Thisefficiencygainbecomesmore
the best overall pass@1 on o1-mini. This result indicates that pronouncedwithcomplexmethods:CoT+Prochemyachieves
Prochemy’s refinement mechanism can enhance code gener- 3.51s latency compared to 3.91s for vanilla CoT (10.2%
ation quality, even when the underlying model is designed improvement). The trend holds across model architectures,
for chain-of-thought reasoning. Interestingly, CoT+Prochemy withClaude-3-Haikushowing4.76sforZero-shot+Prochemy
(43.6) also boosts performance relative to standard CoT but versus 4.95s for AgentCoder-noiter. Multi-turn configurations
is still slightly below zero-shot+Prochemy, suggesting that reveal Prochemy’s scalability - LDB + Prochemy completes
a concise prompting strategy—one that Prochemy inherently HumanEval’s tasks in 11.34s (GPT-3.5-Turbo) versus 14.49s
facilitates—can be more effective for o1-mini. This behav- for standard LDB, demonstrating 21.7% faster execution deior aligns with OpenAI’s technical report, which notes that spite comparable token counts. The computational overhead
reasoning-oriented models like o1-mini often respond best to associated with the Prochemy methodology is found to be
succinct prompts. comparable to the baseline implementation in the majority of
Overall, our findings demonstrate that o1-mini can still experimental scenarios.
benefit from systematic prompt refinements via Prochemy, c) Training: For training, Prochemy’s token and time
despite its built-in chain-of-thought capability and official costs are highly sustainable compared to manual prompt
recommendations favoring minimal prompt engineering. This engineering iterations. The optimization process incurs only
underscores the versatility of Prochemy: it not only elevates a minimal one-time training cost, which does not impact
performance in standard LLMs but also proves valuable for inference overhead, making it especially efficient for batch
next-generation reasoning models. processing. For instance, training on the HumanEval dataset

<!-- Page 14 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 14


## Tablevii


## Timeandcostanalysis(Humaneval&Mbpp)


### PromptingMethods HumanEval MBPP

GPT-3.5-Turbo GPT-4o Claude-3-Haiku DeepSeek-V3 GPT-3.5-Turbo GPT-4o Claude-3-Haiku DeepSeek-V3

### Single-Turn

Zero-Shot 184+358/3.76s 184+526/8.68s 188+372/3.82s 185+544/8.39s 124+191/2.14s 124+354/4.13s 126+273/3.14s 124+374/4.18s
Few-shot 303+425/2.59s 314+484/5.69s 322+437/2.61s 327+487/5.36s 217+254/2.16s 242+316/2.30s 237+285/3.23s 251+364/2.73s
CoT 204+423/3.91s 203+632/11.39s 209+447/4.34s 208+655/9.76s 143+246/2.85s 144+401/4.15s 144+323/3.51s 143+442/5.13s
APE 281+482/3.46s 314+705/5.53s 339+497/4.60s 322+712/9.78s 197+333/2.25s 242+495/4.28s 268+414/3.77s 295+515/4.78s
OPRO 244+402/3.52s 263+657/5.58s 310+513/4.87s 339+654/7.67s 241+248/2.03s 258+464/5.51s 311+356/3.27s 314+482/5.32s
BPO 223+340/2.86s 277+549/8.09s 323+504/4.42s 276+683/8.04s 186+229/2.50s 237+335/3.21s 244+282/2.86s 241+347/3.77s
Self-Collab-noiter 235+403/2.04s 236+551/5.26s 241+411/2.92s 238+566/6.30s 177+160/1.56s 178+278/1.93s 180+219/1.75s 182+281/1.87s
AgentCoder-noiter 304+576/4.93s 307+749/14.38s 309+586/4.95s 308+776/10.43s 248+404/3.13s 250+582/6.17s 248+493/4.65s 254+619/5.86s
LDB-noiter 322+486/3.79s 329+870/6.60s 324+533/4.92s 326+884/11.32s 259+303/2.56s 258+317/2.93s 260+310/2.78s 258+420/3.37s
Zero-shot+Prochemy 259+483/2.79s 312+641/11.45s 317+503/4.76s 322+702/10.08s 251+339/2.94s 307+512/4.23s 295+463/3.28s 337+462/3.91s
CoT+Prochemy 294+462/3.51s 355+728/11.73s 342+542/5.01s 357+743/10.94s 287+392/3.02s 339+537/4.40s 311+479/4.07s 362+499/4.38s

### Multi-Turn

Self-Collaboration 407+813/10.42s 492+1187/16.06s 434+891/12.37s 474+1171/19.28s 447+541/14.17s 527+672/18.36s 428+577/15.62s 547+880/24.01s
AgentCoder 386+962/11.77s 453+1011/14.44s 408+994/11.96s 458+1059/17.41s 477+492/12.64s 486+511/16.07s 473+519/13.37s 496+821/20.11s
LDB 587+1094/14.49s 523+1487/20.91s 548+1169/16.77s 515+1495/30.87s 527+814/18.31s 589+1066/22.16s 559+798/18.76s 541+974/29.55s
Self-Collab+Prochemy 388+844/10.36s 483+1172/15.49s 427+906/12.44s 490+1202/19.64s 436+550/14.43s 586+641/18.82s 419+568/15.27s 532+857/22.17s
AgentCoder+Prochemy 443+1011/11.91s 466+1064/14.61s 489+1071/14.74s 462+1097/18.02s 490+516/13.02s 527+549/16.88s 478+551/13.84s 507+864/20.98s
LDB+Prochemy 467+1057/11.34s 504+1390/20.03s 511+1084/16.48s 501+1447/29.64s 499+786/17.18s 591+1129/22.84s 513+762/17.84s 588+942/29.38s

## Tableviii


## Timeandtokencostanalysis(Livecodebench)


### PromptingMethods LiveCodeBench

GPT-3.5-Turbo GPT-4o Claude-3.5-Sonnet DeepSeek-V3 o1-mini

### Single-Turn

Zero-Shot 544+370/4.28s 533+663/19.01s 584+833/13.31s 525+764/11.47s 587+5947/42.93s
Few-shot 626+278/3.65s 626+595/12.85s 693+819/12.80s 620+760/11.53s 691+3982/25.96s
CoT 540+388/4.39s 540+706/19.79s 591+846/13.99s 532+752/11.37s 594+5308/37.21s
APE 609+388/4.53s 609+714/15.42s 666+842/15.56s 600+830/16.25s 666+4522/45.38s
OPRO 546+396/4.86s 546+702/15.96s 599+852/14.39s 538+812/13.35s 594+5534/52.99s
BPO 548+328/3.99s 548+650/13.47s 599+814/12.83s 540+731/11.33s 605+5551/51.95s
Self-Collab-noiter 658+250/3.24s 659+243/7.57s 716+291/7.14s 650+258/6.56s 723+2473/15.60s
AgentCoder-noiter 548+583/5.99s 548+751/20.22s 602+845/14.57s 540+934/15.87s 601+4981/44.20s
LDB-noiter 548+456/4.87s 517+646/15.24s 568+845/13.36s 509+964/17.55s 560+8684/76.52s
Zero-shot+Prochemy 589+532/5.83s 587+745/19.58s 641+837/13.86s 580+830/12.79s 645+5827/41.60s
CoT+Prochemy 662+436/6.62s 662+750/17.34s 722+989/14.03s 651+834/18.38s 727+4561/41.13s
with GPT-4o consumes approximately 18,000 tokens in total b) Threats to Internal Validity: A key threat to internal
and takes just 60–80 seconds, demonstrating the low training validity is potential data leakage, as large language models
cost.Thisefficiencyisachievedbyconsolidatingoptimization are trained on extensive open-source code that may overlap
knowledge into system prompts, rather than performing per- withourexperimentalbenchmarks.However,thisriskdoesnot
sample tuning, ensuring the method’s practicality for real- significantlycompromisethefairnessofourexperimentssince
world deployment. all methods are consistently validated under the same model
configuration. Therefore, the observed relative improvements
betweenthebaselineandProchemyaredeemedreliableunder

### C. Threats to Validity

these controlled conditions. To further mitigate leakage risks,
a) Threats to External Validity: The main threat to we conducted additional evaluations on LiveCodeBench, a
Prochemy’s external validity is that different model versions dynamically refreshed dataset updated over time to minimize
and architectures might affect its performance. To ensure our historicaltrainingoverlap.Forthetrainingdatausedorgenerapproach is generalizable, we tested it on six diverse large atedinourexperiments,weensurethatnooverlappingoccurs
language models—both proprietary ones like ChatGPT and between the training data and the test sets used to evaluate
Claude, and open-source ones like DeepSeek—to validate its the models. This precaution helps to maintain the integrity
transferability. Although ChatGPT’s o1 model recommends ofourexperimentalresultsandensuresthattheimprovements
using simple, direct prompts [42], this does not conflict reportedareduetotheeffectivenessofProchemyandnotfrom
with Prochemy’s strategy. Prochemy identifies near-optimal the models having prior exposure to the test data.
prompts for each model and task using training feedback
and employs a tailored, iterative prompt mutation process for VII. CONCLUSION
eachmodel,enablingpromptoptimizationthatisbothspecific Inthispaper,weintroduceProchemy,anautomatedprompt
and adaptable. Our experimental results in Table VI further optimization framework that systematically enhances code
demonstrate Prochemy’s compatibility with models adhering generation and translation across diverse large language modto minimalistic prompting guidelines. els (LLMs). By aligning prompts with model capabilities

<!-- Page 15 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 15

and task requirements through iterative refinement, Prochemy [9] A.Radford,J.Wu,R.Child,D.Luan,D.Amodei,I.Sutskeveretal.,
eliminates manual engineering while maintaining compati- “Language models are unsupervised multitask learners,” OpenAI blog,
vol.1,no.8,p.9,2019.
bility with multi-agent and reasoning-driven workflows. The
[10] B.Mann,N.Ryder,M.Subbiah,J.Kaplan,P.Dhariwal,A.Neelakantan,
experimental results show the effectiveness of Prochemy. P. Shyam, G. Sastry, A. Askell, S. Agarwal et al., “Language models
On code generation benchmarks, Prochemy achieves average arefew-shotlearners,”arXivpreprintarXiv:2005.14165,vol.1,2020.
[11] D. Huang, J. M. Zhang, M. Luck, Q. Bu, Y. Qing, and H. Cui,
improvementsof4.04%(zero-shot),4.55%(chain-of-thought),
“Agentcoder: Multi-agent-based code generation with iterative testing
and 2.00% (multi-turn) across four LLMs in four datasets, andoptimisation,”2024.[Online].Available:https://arxiv.org/abs/2312.
setting new state-of-the-art results such as 96.3% accuracy 13010
[12] L. Zhong, Z. Wang, and J. Shang, “Debug like a human: A large
on HumanEval (GPT-4o). The framework demonstrates crosslanguagemodeldebuggerviaverifyingruntimeexecutionstep-by-step,”
model consistency: Claude-3.5-Sonnet achieves 30.2% rela- 2024.[Online].Available:https://arxiv.org/abs/2402.16906
tive improvement on LiveCodeBench’s zero-shot tasks, while [13] T. Ahmed, K. S. Pai, P. Devanbu, and E. Barr, “Automatic semantic
augmentation of language model prompts (for code summarization),”

### DeepSeek-V3 sees 21.5% gains in CoT settings. For code

in Proceedings of the IEEE/ACM 46th International Conference
translation, Prochemy delivers 13.68% and 8.25% average on Software Engineering, ser. ICSE ’24. New York, NY, USA:
improvements on Java-to-Python and Python-to-Java tasks, Association for Computing Machinery, 2024. [Online]. Available:
https://doi.org/10.1145/3597503.3639183
respectively. The further discussion shows that Prochemy also
[14] Radford, Alec, Narasimhan, Karthik, Salimans, Tim, Sutskever, Ilya
demonstratesgoodperformancewhencombiningwiththeo1- et al., “Improving language understanding by generative pre-training,”
minimodel,highlightingitseffectivenessacrossdifferenttasks 2018.
[15] T.Brown,B.Mann,N.Ryder,M.Subbiah,J.D.Kaplan,P.Dhariwal,
and model configurations.

### A.Neelakantan,P.Shyam,G.Sastry,A.Askelletal.,“Languagemod-

Prochemy’s plug-and-play design requires no architectural els are few-shot learners,” Advances in neural information processing
modifications or fine-tuning, ensuring computational effi- systems,vol.33,pp.1877–1901,2020.
[16] Y. Bai, S. Kadavath, S. Kundu, A. Askell, J. Kernion, A. Jones,
ciency. While high-capacity models exhibit diminishing re-

### A.Chen,A.Goldie,A.Mirhoseini,C.McKinnon,C.Chen,C.Olsson,

turns, the framework balances automation and capability ex- C.Olah,D.Hernandez,D.Drain,D.Ganguli,D.Li,E.Tran-Johnson,
ploitation,unifyingoptimizationacrosscodesynthesis,reason- E. Perez, J. Kerr, J. Mueller, J. Ladish, J. Landau, K. Ndousse,
K.Lukosuite,L.Lovitt,M.Sellitto,N.Elhage,N.Schiefer,N.Mercado,
ing, and translation tasks. These results establish Prochemy

### N.DasSarma,R.Lasenby,R.Larson,S.Ringer,S.Johnston,S.Kravec,

as a scalable paradigm for advancing LLM-driven software S. E. Showk, S. Fort, T. Lanham, T. Telleen-Lawton, T. Conerly,
development. T. Henighan, T. Hume, S. R. Bowman, Z. Hatfield-Dodds, B. Mann,
D. Amodei, N. Joseph, S. McCandlish, T. Brown, and J. Kaplan,
“Constitutional ai: Harmlessness from ai feedback,” 2022. [Online].
Available:https://arxiv.org/abs/2212.08073

## Viii. Dataavailability

[17] Y. Bai, A. Jones, K. Ndousse, A. Askell, A. Chen, N. DasSarma,
Our code, data, and results are available at D. Drain, S. Fort, D. Ganguli, T. Henighan, N. Joseph, S. Kadavath,
J. Kernion, T. Conerly, S. El-Showk, N. Elhage, Z. Hatfield-Dodds,
https://github.com/buriyuanyou/Prochemy.
D. Hernandez, T. Hume, S. Johnston, S. Kravec, L. Lovitt, N. Nanda,
C. Olsson, D. Amodei, T. Brown, J. Clark, S. McCandlish, C. Olah,
B. Mann, and J. Kaplan, “Training a helpful and harmless assistant
REFERENCES with reinforcement learning from human feedback,” 2022. [Online].

### Available:https://arxiv.org/abs/2204.05862

[1] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. D. O. Pinto, J. Kaplan, [18] DeepSeek-AI, “Deepseek-v2: A strong, economical, and efficient
H.Edwards,Y.Burda,N.Joseph,G.Brockmanetal.,“Evaluatinglarge mixture-of-experts language model,” 2024. [Online]. Available: https:
language models trained on code,” arXiv preprint arXiv:2107.03374, //arxiv.org/abs/2405.04434
2021. [19] D.Guo,Q.Zhu,D.Yang,Z.Xie,K.Dong,W.Zhang,G.Chen,X.Bi,
[2] A. Svyatkovskiy, S. K. Deng, S. Fu, and N. Sundaresan, “Intellicode Y. Wu, Y. K. Li, F. Luo, Y. Xiong, and W. Liang, “Deepseek-coder:
compose: Code generation using transformer,” in Proceedings of the Whenthelargelanguagemodelmeetsprogramming–theriseofcode
28thACMjointmeetingonEuropeansoftwareengineeringconference intelligence,”2024.[Online].Available:https://arxiv.org/abs/2401.14196
and symposium on the foundations of software engineering, 2020, pp. [20] DeepSeek-AI, A. Liu, B. Feng, B. Xue, B. Wang, B. Wu, C. Lu,
1433–1443. C. Zhao, C. Deng, C. Zhang, C. Ruan, D. Dai, D. Guo, D. Yang,
[3] J.Li,G.Li,Y.Li,andZ.Jin,“Structuredchain-of-thoughtprompting D.Chen,D.Ji,E.Li,F.Lin,F.Dai,F.Luo,G.Hao,G.Chen,G.Li,
for code generation,” ACM Trans. Softw. Eng. Methodol., aug 2024. H. Zhang, H. Bao, H. Xu, H. Wang, H. Zhang, H. Ding, H. Xin,
[Online].Available:https://doi.org/10.1145/3690635 H.Gao,H.Li,H.Qu,J.L.Cai,J.Liang,J.Guo,J.Ni,J.Li,J.Wang,
[4] A. Fan, B. Gokkaya, M. Harman, M. Lyubarskiy, S. Sengupta, J. Chen, J. Chen, J. Yuan, J. Qiu, J. Li, J. Song, K. Dong, K. Hu,
S. Yoo, and J. M. Zhang, “Large language models for software K.Gao,K.Guan,K.Huang,K.Yu,L.Wang,L.Zhang,L.Xu,L.Xia,
engineering: Survey and open problems,” 2023. [Online]. Available: L. Zhao, L. Wang, L. Zhang, M. Li, M. Wang, M. Zhang, M. Zhang,
https://arxiv.org/abs/2310.03533 M. Tang, M. Li, N. Tian, P. Huang, P. Wang, P. Zhang, Q. Wang,
[5] Y.Liu,S.Tao,W.Meng,F.Yao,X.Zhao,andH.Yang,“Logprompt: Q. Zhu, Q. Chen, Q. Du, R. J. Chen, R. L. Jin, R. Ge, R. Zhang,
Promptengineeringtowardszero-shotandinterpretableloganalysis,”in R.Pan,R.Wang,R.Xu,R.Zhang,R.Chen,S.S.Li,S.Lu,S.Zhou,
Proceedings of the 2024 IEEE/ACM 46th International Conference on S.Chen,S.Wu,S.Ye,S.Ye,S.Ma,S.Wang,S.Zhou,S.Yu,S.Zhou,
SoftwareEngineering:CompanionProceedings,2024,pp.364–365. S.Pan,T.Wang,T.Yun,T.Pei,T.Sun,W.L.Xiao,W.Zeng,W.Zhao,
[6] Y. Fu, L. Ou, M. Chen, Y. Wan, H. Peng, and T. Khot, W.An,W.Liu,W.Liang,W.Gao,W.Yu,W.Zhang,X.Q.Li,X.Jin,
“Chain-of-thought hub: A continuous effort to measure large X. Wang, X. Bi, X. Liu, X. Wang, X. Shen, X. Chen, X. Zhang,
language models’ reasoning performance,” 2023. [Online]. Available: X.Chen,X.Nie,X.Sun,X.Wang,X.Cheng,X.Liu,X.Xie,X.Liu,
https://arxiv.org/abs/2305.17306 X. Yu, X. Song, X. Shan, X. Zhou, X. Yang, X. Li, X. Su, X. Lin,
[7] Q. Guo, R. Wang, J. Guo, B. Li, K. Song, X. Tan, G. Liu, Y.K.Li,Y.Q.Wang,Y.X.Wei,Y.X.Zhu,Y.Zhang,Y.Xu,Y.Xu,
J. Bian, and Y. Yang, “Connecting large language models with Y. Huang, Y. Li, Y. Zhao, Y. Sun, Y. Li, Y. Wang, Y. Yu, Y. Zheng,
evolutionary algorithms yields powerful prompt optimizers,” 2024. Y.Zhang,Y.Shi,Y.Xiong,Y.He,Y.Tang,Y.Piao,Y.Wang,Y.Tan,
[Online].Available:https://arxiv.org/abs/2309.08532 Y. Ma, Y. Liu, Y. Guo, Y. Wu, Y. Ou, Y. Zhu, Y. Wang, Y. Gong,
[8] J. Wu, T. Yu, R. Wang, Z. Song, R. Zhang, H. Zhao, C. Lu, S. Li, Y. Zou, Y. He, Y. Zha, Y. Xiong, Y. Ma, Y. Yan, Y. Luo, Y. You,
and R. Henao, “Infoprompt: Information-theoretic soft prompt tuning Y. Liu, Y. Zhou, Z. F. Wu, Z. Z. Ren, Z. Ren, Z. Sha, Z. Fu, Z. Xu,
for natural language understanding,” Advances in Neural Information Z.Huang,Z.Zhang,Z.Xie,Z.Zhang,Z.Hao,Z.Gou,Z.Ma,Z.Yan,
ProcessingSystems,vol.36,2024. Z.Shao,Z.Xu,Z.Wu,Z.Zhang,Z.Li,Z.Gu,Z.Zhu,Z.Liu,Z.Li,

<!-- Page 16 -->


## Ieeetransactionsonsoftwareengineering,Vol.14,No.8,August2021 16

Z. Xie, Z. Song, Z. Gao, and Z. Pan, “Deepseek-v3 technical report,” [38] M. A. Islam, M. E. Ali, and M. R. Parvez, “Mapcoder: Multi-agent
2024.[Online].Available:https://arxiv.org/abs/2412.19437 code generation for competitive problem solving,” 2024. [Online].
[21] F. F. Xu, U. Alon, G. Neubig, and V. J. Hellendoorn, “A systematic Available:https://arxiv.org/abs/2405.11403
evaluation of large language models of code,” in Proceedings [39] S. Ouyang, J. M. Zhang, M. Harman, and M. Wang, “An empirical
of the 6th ACM SIGPLAN International Symposium on Machine study of the non-determinism of chatgpt in code generation,” ACM
Programming, ser. MAPS 2022. New York, NY, USA: Association Trans. Softw. Eng. Methodol., vol. 34, no. 2, Jan. 2025. [Online].
for Computing Machinery, 2022, p. 1–10. [Online]. Available: Available:https://doi.org/10.1145/3697010
https://doi.org/10.1145/3520312.3534862 [40] B. Chen, F. Zhang, A. Nguyen, D. Zan, Z. Lin, J.-G. Lou, and
[22] C. Wang, Y. Yang, C. Gao, Y. Peng, H. Zhang, and M. R. Lyu, W.Chen,“Codet:Codegenerationwithgeneratedtests,”arXivpreprint
“Nomorefine-tuning?anexperimentalevaluationofprompttuningin arXiv:2207.10397,2022.
code intelligence,” in Proceedings of the 30th ACM Joint European [41] E.Nijkamp,B.Pang,H.Hayashi,L.Tu,H.Wang,Y.Zhou,S.Savarese,
Software Engineering Conference and Symposium on the Foundations andC.Xiong,“Codegen:Anopenlargelanguagemodelforcodewith
ofSoftwareEngineering,ser.ESEC/FSE2022. NewYork,NY,USA: multi-turnprogramsynthesis,”arXivpreprintarXiv:2203.13474,2022.
Association for Computing Machinery, 2022, p. 382–394. [Online]. [42] OpenAI, “Learning to reason with large language models,” https://
Available:https://doi.org/10.1145/3540250.3549113 openai.com/index/learning-to-reason-with-llms/,2024.
[23] J.Wei,X.Wang,D.Schuurmans,M.Bosma,F.Xia,E.Chi,Q.V.Le,
D. Zhou et al., “Chain-of-thought prompting elicits reasoning in large
languagemodels,”Advancesinneuralinformationprocessingsystems,
vol.35,pp.24824–24837,2022.
[24] Y. Zhou, A. I. Muresanu, Z. Han, K. Paster, S. Pitis, H. Chan, and
J. Ba, “Large language models are human-level prompt engineers,”
2023.[Online].Available:https://arxiv.org/abs/2211.01910
[25] R.Pryzant,D.Iter,J.Li,Y.T.Lee,C.Zhu,andM.Zeng,“Automatic
prompt optimization with ”gradient descent” and beam search,” 2023.
[Online].Available:https://arxiv.org/abs/2305.03495
[26] C. Yang, X. Wang, Y. Lu, H. Liu, Q. V. Le, D. Zhou, and X. Chen,
“Large language models as optimizers,” 2024. [Online]. Available:
https://arxiv.org/abs/2309.03409
[27] J. Cheng, X. Liu, K. Zheng, P. Ke, H. Wang, Y. Dong,
J. Tang, and M. Huang, “Black-box prompt optimization: Aligning
large language models without model training,” in Proceedings of
the 62nd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), L.-W. Ku, A. Martins, and
V.Srikumar,Eds. Bangkok,Thailand:AssociationforComputational
Linguistics, Aug. 2024, pp. 3201–3219. [Online]. Available: https:
//aclanthology.org/2024.acl-long.176
[28] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov,
“Proximal policy optimization algorithms,” 2017. [Online]. Available:
https://arxiv.org/abs/1707.06347
[29] R. Rafailov, A. Sharma, E. Mitchell, S. Ermon, C. D. Manning,
and C. Finn, “Direct preference optimization: Your language model
is secretly a reward model,” 2024. [Online]. Available: https:
//arxiv.org/abs/2305.18290
[30] Y.Dong,X.Jiang,Z.Jin,andG.Li,“Self-collaborationcodegeneration
viachatgpt,”2024.[Online].Available:https://arxiv.org/abs/2304.07590
[31] J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan,

### E. Jiang, C. Cai, M. Terry, Q. Le, and C. Sutton, “Program

synthesis with large language models,” 2021. [Online]. Available:
https://arxiv.org/abs/2108.07732
[32] J.Liu,C.S.Xia,Y.Wang,andL.Zhang,“Isyourcodegeneratedby
chatgptreallycorrect?rigorousevaluationoflargelanguagemodelsfor
code generation,” in Proceedings of the 37th International Conference
onNeuralInformationProcessingSystems,ser.NIPS’23. RedHook,
NY,USA:CurranAssociatesInc.,2024.
[33] N. Jain, K. Han, A. Gu, W. Li, F. Yan, T. Zhang, S. Wang, A. Solar-
Lezama,K.Sen,andI.Stoica,“Livecodebench:Holisticandcontaminationfreeevaluationoflargelanguagemodelsforcode,”arXivpreprint,
2024.
[34] R.Puri,D.S.Kung,G.Janssen,W.Zhang,G.Domeniconi,V.Zolotov,
J. Dolby, J. Chen, M. Choudhury, L. Decker, V. Thost, L. Buratti,
S. Pujar, S. Ramji, U. Finkler, S. Malaika, and F. Reiss, “Codenet: A
large-scaleaiforcodedatasetforlearningadiversityofcodingtasks,”
2021.[Online].Available:https://arxiv.org/abs/2105.12655
[35] W. U. Ahmad, M. G. R. Tushar, S. Chakraborty, and K.-W. Chang,
“Avatar: A parallel corpus for java-python program translation,” 2023.
[Online].Available:https://arxiv.org/abs/2108.11590
[36] R. Pan, A. R. Ibrahimzada, R. Krishna, D. Sankar, L. P. Wassi,
M. Merler, B. Sobolev, R. Pavuluri, S. Sinha, and R. Jabbarvand,
“Lost in translation: A study of bugs introduced by large language
models while translating code,” in Proceedings of the IEEE/ACM
46th International Conference on Software Engineering, ser. ICSE
’24, vol. 34. ACM, Apr. 2024, p. 1–13. [Online]. Available:
http://dx.doi.org/10.1145/3597503.3639226
[37] D.Huang,Q.Bu,Y.Qing,andH.Cui,“Codecot:Tacklingcodesyntax
errorsincotreasoningforcodegeneration,”2024.[Online].Available:
https://arxiv.org/abs/2308.08784

## Tables

**Table (Page 12):**

| IEEETRANSCAaCseT 2IO HNuSmOanNEvSaOl/F1T0W8AREENGINEERING,VOL.14,NO.8,AUGUST2021 1 |
|---|
| e 3 atcoder_ABC137_D 4 3 1 3 5 2 (a) Zero-Shot (b) Prochemy assert candidate([-1, -2, 0]) == 2 assert candidate([-1, -2, 0]) == 2 assert candidate([-1, -2, 0]) == 0 (Ca)a Zsereo -3Sh o attcoder_ABC137_D (b) CoT (c) Prochemy Fig.3. Case2HumanEval/108forCodeGeneration |


**Table (Page 12):**

| Cas | e 3 atcoder_ABC137_D |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | coder_ABC137_D |  |  |  |  |  |  |  |  |  |  |  |
| 3 4 4 2 | 4 3 1 2 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 5 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | (a) Zer |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 5 |  |
|  |  |  |  |  |  |  |  |  |  | (b) Prochemy |  |  |  |
|  |  | assert candidate([-1, -2, 0]) == 2 assert candidate([-1, -2, 0]) == 2 assert candidate([-1, -2, 0]) == 0 (Ca)a Zsereo -3Sh o attcoder_ABC137_D (b) CoT (c) Prochemy |  |  |  |  |  |  |  |  |  |  |  |
|  |  | assert candidate([-1, -2, 0]) == 2 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | (Ca)a Zsereo -3Sh o attcoder_ABC137_D (b) CoT (c) Prochemy |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
