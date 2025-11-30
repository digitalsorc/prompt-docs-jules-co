---
title: "Improving ChatGPT Prompt Code Generation"
original_file: "./Improving_ChatGPT_Prompt_Code_Generation.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "fine-tuning"]
keywords: ["code", "generation", "chatgpt", "prompt", "task", "prompts", "tasks", "codebleu", "bleu", "performance"]
summary: "<!-- Page 1 -->


### Improving ChatGPT Prompt for Code Generation

Chao Liu1, Xuanlin Bao1, Hongyu Zhang1, Neng Zhang2, Haibo Hu1, Xiaohong Zhang1, Meng Yan1
1School of Big Data and Software engineering, Chongqing University, China
{liu.chao, baoxuanlin, hyzhang, haibo.hu, xhongz, mengy}@cqu.edu.cn
2School of Software Engineering, Sun Yat-sen University, China
zhangn279@mail.sysu.edu.cn
Abstract—Automated code generation can be a powerful tech- developed CodeBERT, an LLM that has a similar arch"
related_documents: []
---

# Improving ChatGPT Prompt Code Generation

<!-- Page 1 -->


### Improving ChatGPT Prompt for Code Generation

Chao Liu1, Xuanlin Bao1, Hongyu Zhang1, Neng Zhang2, Haibo Hu1, Xiaohong Zhang1, Meng Yan1
1School of Big Data and Software engineering, Chongqing University, China
{liu.chao, baoxuanlin, hyzhang, haibo.hu, xhongz, mengy}@cqu.edu.cn
2School of Software Engineering, Sun Yat-sen University, China
zhangn279@mail.sysu.edu.cn
Abstract—Automated code generation can be a powerful tech- developed CodeBERT, an LLM that has a similar architecture
niqueforsoftwaredevelopment,significantlyreducingdevelopers’ toBERT[12]andispre-trainedonsixprogramminglanguages
efforts and time required to create new code by generating
[12]. CodeBERT can be used for various SE tasks, such
it automatically based on requirements. Recently, OpenAI’s
as code search and summarization, with good performance.
language model ChatGPT has emerged as a powerful tool for
generating human-like responses to a wide range of textual Another notable model is CodeGPT developed by Lu et al. [5].
inputs (i.e., prompts), including those related to code generation. CodeGPT is pre-trained on Python and Java datasets using the
However,theeffectivenessofChatGPTforcodegenerationisnot GPT-2 [13] architecture, and fine-tuned for a variety of SE
wellunderstood,andthegenerationperformancecouldbeheavily
tasks, such as code generation and code translation.
influenced by the choice of prompt. To answer these questions,

### Recently,OpenAIintroducedChatGPT,arevolutionaryLLM

we conducted experiments using the CodeXGlue dataset to
evaluate ChatGPT’s capabilities for two code generation tasks, based on the GPT-3.5 architecture [14], which can work
including text-to-code and code-to-code generation. We designed on various tasks including code generation [15]. Different
prompts by leveraging the chain-of-thought strategy with multi- from existing LLMs, ChatGPT is able to generate human-like
stepoptimizations.Ourresultsshowedthatbycarefullydesigning responses through reinforcement learning [16] based on users’
prompts to guide ChatGPT, the generation performance can
textual inputs (i.e., prompts). Owing to its effectiveness on
be improved substantially. We also analyzed the factors that
influenced the prompt design and provided insights that could various tasks, ChatGPT has attracted 100 million active users
guide future research. worldwide within just two months after its initial release [17].
Index Terms—ChatGPT, code generation, prompt engineering However, the performance of ChatGPT is highly dependent on
the quality of prompts used. Designing better prompts, which
is called prompt engineering [18], is under active investigation.

## I. Introduction

In this paper, we investigate the code generation performance
Code generation is a technique that aims to automatically of ChatGPT with various prompt engineering methods.
generate code based on developers’ requirements [1], [2]. It We conducted an evaluation of ChatGPT’s code generation
can reduce repetitive coding efforts and improve software capabilities using the widely used CodeXGlue [5] dataset for
development productivity [3], [4]. These requirements can both T2C and C2C generation tasks. Initially, we employed
be expressed as natural language (NL) descriptions, allowing basic prompts for the tasks: ”write a Java method that” + NL
developers to specify their needs in an intuitive way. For description for T2C task, and ”translated C# code into Java
instance,adevelopercanaskacodegenerationtoolto”convert code:” + code for C2C task. Experimental results showed that
an integer variable n to a string in Java”, and the tool will these prompts (ChatGPT-task) achieved CodeBLEU scores of
generate an appropriate code example such as: ”String s = 22.76 and 39.37, respectively, where CodeBLEU is a widely
Integer.toString(n)”. This process is known as Text-to-Code used overall evaluation metric [19]. To improve the generation
(T2C) generation [5], [6]. Another type of code generation is performance, we leveraged the chain-of-thought strategy with
Code-to-Code (C2C) generation, which translates an existing manual construction [20] to augment the prompts for different
code snippet from one programming language to another [5], tasks. This approach conducts multi-step optimizations based
[7]. For instance, the C# code ”String s = n.ToString()” can on the feedback from ChatGPT. Our experimental results
be translated to the above Java code. The C2C generation can showed that: 1) adding more specific requirements to the
be useful when porting existing code to a new programming prompts improved the CodeBLEU of ChatGPT-task by 73.58%
language [7]. and 3.45% for the two tasks, respectively; 2) directly asking
Large language models (LLMs) have emerged as a powerful ChatGPT to generate concise code in the prompt (e.g., ”write
tool for natural language processing (NLP) tasks, such as aconciseJavamethodthat”+NL)ledtofurtherimprovement
sentiment analysis [8], [9] and language translation [10], inCodeBLEUfortheT2Ctask,reachingto50.18;3)sharinga
thanks to their ability to be pre-trained on massive amounts of ChatGPT session for a number of prompt testing also boosted
massive unsupervised textual data and fine-tuned on domain- theCodeBLEUoftheC2Ctaskto48.80;and4)thegeneration
specific datasets. This ”pre-train, fine-tune” paradigm has randomness of ChatGPT had little effect on the generation
been applied to software engineering (SE) tasks, such as code performance due to the specific instructions in the prompt.
generation,withpromisingresults.Forinstance,Fengetal.[11] Furthermore, we compared the performance with state-of-the-
3202
yaM
51
]ES.sc[
1v06380.5032:viXra

<!-- Page 2 -->

art fine-tuned LLMs and analyzed the correctness and quality presentsafamilyofarchitecturessimilartoGPT-3designedfor
of the generated code. multi-turn program synthesis. CodeX [37] fine-tuned GPT-3 on
In summary, the major contributions of this paper are as publiclyavailablecodefromGitHub,whosedistinctproduction
follows: version powers the GitHub Copilot [38].
• EvaluatingChatGPTonawidely-useddatasetCodeXGlue
B. ChatGPT and Prompt Engineering
for two code generation tasks.
ChatGPT is an LM developed by OpenAI and it is designed
• Proposing prompt design and optimization methods to
for conversational tasks (e.g., question-answering and code
guide ChatGPT to generate better code with prompt
generation) [14]. ChatGPT is built on the GPT-3.5 series with
engineering.
175 billion parameters and optimized by using reinforcement
• Releasing a replication package1 for future exploration in learningfromhumanfeedback[16].Itcangeneratehuman-like
this research community.
responses to the user’s textual prompt based on its context
II. BACKGROUNDANDRELATEDWORK understanding and conversation history. Besides, OpenAI is
improving ChatGPT by keeping optimizing GPT-4 [39].

### A. Large Language Model for Code Generation


### As LM (e.g., ChatGPT [14]) with a large number of


### Many language models (LMs) have been proposed, which

parameters (>100 million) emerges with advanced textual
are pre-trained with a special objective (e.g., masked language
generation capability, prompt engineering (PE) becomes a
modeling[21])andappliedtodownstreamtasksbyfine-tuning.
new paradigm for NLP [28]. The goal of PE is to design

### Generally, there are three types of LMs: 1) Masked LM, a

an appropriate prompt for a pre-trained model and conduct
model is trained to predict a masked word in a sentence given
prediction as expected with good performance, leading to the
itssurroundingcontexts,suchasBERT[12]andRoBERTa[22].
”pre-train, prompt, predict” paradigm. Specifically, the PE
2) Encoder-Decoder, a model works for sentence-to-sentence creates a prompt x(cid:48) = f (x) ∈ X for a textual input
prompt
takes like translation and summarization, where an encoder
x (e.g., ”write a Java code for converting int to string”) that
encodes the input into a fixed-length vector and a decoder
describes a downstream task (e.g., code generation). With the
generates output from the encoded vector, such as T5 [13], prompt x, LLM performs prediction y =f (x(cid:48))∈Y. Two

## Llm


### BART [23], and MASS [24]. 3) Left-to-Right LM, a model

basic PE tasks are: 1) Prompt Template Engineering, it designs
is trained to predict the next word in a sentence given the anappropriatetemplatex(cid:48) fortheLMinput(e.g.,”writeaJava
previous words, such as GPT [25], GPT-2 [13], and GPT-3
code for [x]”, where ”[x]” is a variable for NL description), as
[26]. For these LMs, Transformer [27] is used as the base
the performance of LM prediction y is sensitive to sentence(s)
model because its self-attention layers can efficiently process
designed in the template. 2) Prompt Answer Engineering, it
input with long-term memory and effectively adapt itself to
aimstodesignananswerspaceZ inthepromptsothatabetter
various downstream tasks [28].
answer y could be generated from a limited scope y ∈Z (e.g.,
Researchers have proposed many LM-based models that
”Whichcodeisbetter?AorB”).MoreadvancedPEtasksintend
can be used for code generation tasks. The representatives
tomanipulatemulti-prompt,suchaspromptaugmentation[40],
are: 1) BERT-Based. CodeBERT [11] trained a BERT-like
composition, etc. [28]
model with six programming languages. GraphCodeBERT [4]
The prompt (x(cid:48)) can be generated in four ways (f )
prompt
is an improved model that considers the inherent structure
[28], [41]: 1) Manual Construction, it is suitable for templateof code instead of plain text as CodeBERT. UniXcoder
based prompts and few-shot prompting where the prompt is
[29] addressed the difficulty in learning code structure by
uncomplicated [40], [42]. 2) LM Generation, it leverages LM
transforming the code into a sequence but retaining the
to generate customized prompt (x(cid:48)) for each textual input
structural information. ContraBERT [30] leveraged contrastive
(x), which can make up for the shortcomings of the manual
learning [31] to improve the robustness of CodeBERT and
construction [43]. 3) Retrieval-Based Prompt, it relies on well-

### GraphCodeBERT.2)T5-Based.Mastropaoloetal.[32]showed

annotated external resources (e.g., Wikipedia) to alleviate the
that fine-tuning T5 is possible to work on SE tasks. CodeT5
unstable issue of generation [44]. 4) Prompt Learning, it
[33] is an identifier-aware T5 model that can distinguish which
builds a supervised model to automatically update the prompt
code tokens are identifiers and recover them when they are
according to the LM’s generation and the associated groundmasked.3)BART-Based.PLBART[34]isconstructedonBART
truth [28]. In this study, we leveraged the manual construction
pre-trained with an extensive collection of Java and Python
toexplorethepossibilitytoguideChatGPTforcodegeneration
functions and associated NL text via denoising autoencoding.
tasks, investigate the influential factors in prompt design, and
CommitBART [7] pre-trained BART using data collected from
provide researchers with insights for future works.

### GitHub commits. 4) GPT-Based. GPT-C [35] is a variant

of GPT-2 pre-trained on a large unsupervised multilingual III. STUDYSUBJECTS
sourcecodedataset.CodeGPT[5]pre-trainedGPT-2onPython
To apply ChatGPT to code generation, this section presents
and Java corpora from the CodeSearchNet [36]. CodeGen [6]
the study subjects. Specifically, Section III-A describes two
investigated code generation tasks. Section III-B presents the
1ReplicationPackage:https://anonymous.4open.science/r/guiding-chatgptfor-code-generation-0B0E used dataset and Section III-C lists the evaluation metrics.
2

<!-- Page 3 -->

A. Code Generation Tasks between the bags of i-grams appearing in the generated code
and the ground-truth.

### Code generation is the process of automatically generating

code according to a requirement specification. Code generation CodeBLEU, a variant of BLEU, which also considers the
can save time and efforts for developers by automating repeti- syntacticandsemanticdataflowcorrectnessofcodegeneration.
tive programming tasks. The specification can be expressed in It is similar to BLEU, but it calculates precision scores based
differentways.Inthisstudy,weinvestigatedtworepresentative on a set of code tokens, rather than natural language n-grams.
tasks: 1) Text-to-Code (T2C) Generation. It takes a textual Generally, CodeBLEU is a weighted average of the lexical,
description written in natural language (NL) as a functional abstractsyntaxtree,anddataflowmatchbetweenthegenerated
specification. A code generation model generates code (e.g., code and the ground-truth [19].

### Java) according to the textual description. 2) Code-to-Code

(C2C)Generation.Ittakesacodesnippet(e.g.,C#)asinputand IV. METHODOLOGY
an NL model generates code written in another programming This section describes prompt engineering for two code genlanguage (e.g., Java) with the same functionality. This task is eration tasks. Specifically, Section IV-A describes the general
also called a code translation due to its similarity to language methodforpromptdesign.SectionsIV-BandIV-Celaborateon
translation. In the following two subsections, we will introduce the specific prompt design for two tasks, respectively. Finally,
the related models. SectionIV-Dpresentstheinvestigatedresearchquestions(RQs)
in this study.

### B. Datasets


### A. Methods for Prompt Design

Here we present the datasets for testing the investigated two
types of code generation tasks. TheperformanceofChatGPTisoftensensitivetothedesign
of prompts [28]. To augment the prompt, Wei et al. [42]

### T2C Dataset. We chose the widely used dataset CONCODE

indicated that Chain-of-Thought (CoT) prompting is the key
[45], which is collected in CodeXGLUE [5]. This dataset
strategy, which enables an LLM to solve problems by guiding
collected about 33k Java repositories from GitHub, consisting
themtoproduceasequenceofintermediatestepsbeforegiving
of 100k training data, 2k valid data, and 2k test data. Each
the final answer. Due to its effectiveness, the CoT strategy is
instanceinthedataisatupleofthreeelements:1)CodeSnippet,
widely investigated and applied [20], [47].
itistheground-truthforcodegeneration;2)NaturalLanguage
Generally, to guide ChatGPT for code generation tasks, we

### Description,itisextractedfromtheJavadocofthecodesnippet

designed the prompt with the CoT strategy in two steps: 1)
forgenerationinput;3)CodeEnvironment,itdescribestheclass

### Prompt Description, we first analyze the requirement of a

file (i.e., the programmatic context) where the code snippet
code generation task, and design a basic prompt in a natural
works,includingclass name, classpath,membervariables,and
way. Then, we provide the basic prompt for ChatGPT and
signatures of member functions.
ask ”how to improve the prompt?”, and further improve the
C2C Dataset. We used the C2C dataset from CodeXGLUE prompt according to ChatGPT’s suggestions. 2) Multi-Step
[5], a popular benchmark dataset for code understanding and Optimizations, we test the prompt in the first step on some
generation. The C2C dataset collected data from several open- samples from training data of the related dataset, analyze
source repositories, including Lucene, POI, JGit, and Antlr. the generation performance with the ground-truth, and keep
Totally,itcontains10ktrainingdata,0.5kvaliddata,and1ktest optimizing the generation results by providing ChatGPT with
data. Each instance in a data contains a pair of code snippets a series of new prompts.
written in C# and Java, which shared the same function but are Based on the knowledge of the prompt design process,
implementedindifferentprogramminglanguages.Inthisstudy, we generated some baseline prompts and evaluated them on
we regarded the Java code snippet as the generation target of the testing data, which can be found in Section V-A. Fig.
T2C dataset, and used the C# code snippet as the input. 1 illustrates the overview of prompt design and verification.
During the prompt design and testing, we work with ChatGPT

### C. Evaluation Metrics

by invoking its API [48] with default settings (e.g., using
Toanalyzetheeffectivenessofcodegeneration,wemeasured the GPT-3.5-Turbo model). Table II shows the generation
the performance with the widely used metrics for code performance of ChatGPT using different combinations of
generation task [5], including BLEU [46] and CodeBLEU prompts designed in Table I. The following two sections
[19]. Details are described as follows. Following Lu et al. [5], elaborate on how we design prompts for two code generation
we used the CodeBLEU as the overall evaluation metric. tasks, respectively, where the discussed prompts are listed in
Table I.

### BLEU, a popular metric to measure the generation accuracy

forthecodesnippetswithvariouslengths[5],[46].Specifically, B. Prompt Design for Text-to-Code Generation

### BLEU =BP ∗e(logP1+...+logPn)/n where BP is the brevity

penalty value, which equals 1 if the generated code is longer Prompt Description. As described by Lu et al. [5], the T2C
than the ground-truth. Otherwise, it equals the ratio between generation task takes an NL description as a textual input (e.g.,
the lengths of two code. P is the metric for the overlapping ”convert int to String”) and expects a correct generation of
i
3

<!-- Page 4 -->


## Tablei

DIFFERENTTYPESOFPROMPTSDESIGNEDFORTWOCODEGENERATIONTASKS.NOTETHAT#{NL},#{CN},#{MV},#{MF},AND#{CODE}STANDFOR
THEVARIABLESOFACLASSNAME,MEMBERVARIABLE,MEMBERFUNCTION,ANDCODE,WHICHWILLBEFILLEDINACTUALINPUTSFROMTHEDATASET.
No. PromptType Text-to-CodeGenerationTask Code-to-CodeGenerationTask
P1 TaskPrompt writeaJavamethodthat+#{NL} translateC#codeintoJavacode:#{Code}
P2 ContextPrompt rememberyouhaveaJavaclassnamed+’#{CN}’,member -
variables+’#{MV}’,memberfunctions+’#{MF}’
P3 ProcessingPrompt removecomments;removesummary;removethrows;re- donotprovideannotation
move function modifiers; change method name to ”function”;changeargumentnamesto”arg0”,”arg1”...;change
localvariablenamesto”loc0”,”loc1”...
P4 UpdatedTaskPrompt - translate C# code delimited by triple backticks into Java
code:”’#{Code}”’
P5 BehaviourPrompt write a Java method #{that calls ...} with[out] exception translateC#codeintoJavacode:”’#{Code}”’#{thatcalls
handlingto#{NL} ...}with[out]exceptionhandling
a more clear and more informative prompt that helps guide the
generation of a well-designed Java method. We notice that the
programming environment provided in the dataset as described
in Section III-B can be used as additional context information.
To reach the goal, we added a context prompt before the task
prompt: ”remember you have a Java class named + ’#{CN}’,
member variables + ’#{MV}’, member functions + ’#{MF}’
(Table I-P2). In the prompt, the cloze #... will be filled by
Fig.1. Overviewofthemethod corresponding information given in the dataset. Note that we
tellChatGPTtoremembertheclassbecauseitwillgeneratethe
wholeclassifwedonotguideChatGPTwithclearinstructions.

## Tableii

TESTINGDIFFERENTPROMPTCOMBINATIONSINTABLEION100SAMPLES By adding the context prompt, the accuracy of the samples
RANDOMLYSELECTEDFROMTRAININGDATAOFEACHGENERATIONTASK. can be improved with BLEU=10.42 and CodeBLEU=25.05.

## Notethatp5(Api)Indicatesthatweonlyusedtheapipartof

THEPROMPTP5. Afteranalyzingtheground-truth,weobservethatthegroundtruth were pre-processed in four aspects: 1) all comments,
Task Model BLEU CodeBLEU throws,andmethodmodifiersareremoved;2)themethodname
P1 05.29 22.76 is changed to ”function”; 3) all the arguments are renamed to
P2+P1 10.42(+96.98%) 25.05(+10.06%) ”arg0”, ”arg1”, etc.; 4) all the local variables are renamed to

## T2C P2+P1+P3 13.11(+147.83%) 36.00(+58.17%)

”loc0”, ”loc1”, etc. Following these observations, we thus add

## P2+P5(Api)+P3 22.14(+318.53%) 44.18(+94.11%)

P2+P5+P3 27.48(+419.47%) 46.78(+105.54%) a processing prompt with a series of instructions after the task
prompt: ”remove comments; remove summary; remove throws;

## P1 09.76 39.37

remove function modifiers; change method name to ”function”;

## P1+P3 08.55(-12.40%) 45.28(+15.01%)

P4+P3 15.44(+58.20%) 45.00(+14.30%) change argument names to ”arg0”, ”arg1”...; change local

## C2C

P5(API)+P3 13.37(+36.99%) 46.17(+17.27%) variable names to ”loc0”, ”loc1”...” (Table I-P3). Note that

## P5+P3 08.90(-08.81%) 46.88(+19.08%)

some summaries generated for part of code snippets cannot be
removed by the prompt ”remove comments” but the ”remove
summary”; we used the ellipsis ”...” in the prompt instead
Java code method, which matches the intent of the description.
of ”etc.”, because ChatGPT cannot do the renaming actions
According to the task description, we naturally present a basic
with the command ”etc.”. The evaluation shows a further
task prompt: ”write a Java method that + #{NL}” (Table
improvement with BLEU=13.11 and CodeBLEU=36.00.
I-P1). To assess the effectiveness of the prompts, we randomly

### By comparing the generated code with the ground-truth,

sample 100 instances from training data and ask ChatGPT to
we notice that ChatGPT may generate code with different
generate code given the prompt. We obtain a low generation
APIs and settings of exception handling. It is natural to ask
accuracy of BLEU=5.29 and CodeBLEU=22.76.

### ChatGPT to regenerate the code according to its responses

Multi-Step Optimizations. With this prompt template (Table and users’ specific requirements. To extract the requirement
I-P1), we asked ChatGPT: ”how to improve the prompt: write of the APIs and exception handling, we input the ChatGPT
a Java method that converts int to string”. ChatGPT told that with the prompts ”list the used methods with names only in
by providing more specific details of the method behaviour, the following Java methods and do not explain: #{Code}”
programmingcontext,andinput/outputexamples,wecancreate and ”does the code contain exception handling? + #{Code}”
4

<!-- Page 5 -->

for the ground-truth, respectively. Afterward, we write scripts ChatGPT can understand translation context and generate good
to analyze the responses for the requirements of APIs (i.e., results. But adding more requests may bring uncertainty to
name list) and exception handling (i.e., true or false). With the generation. Therefore, this behaviour prompt likely has
these two requirements, we replace the task prompt with a negative effects on the C2C generation task.
behaviour prompt: ”write a Java method #{that calls ...}

### D. Research Questions

with[out] exception handling to #{NL}” (Table I-P5). Note
that if the API list is empty, we remove the ”#{that calls In this study, we propose a method to guide ChatGPT for
...}”, otherwise we replace ”...” with the name list. For the two code generation tasks. To verify the effectiveness of the
”with[out]”, we determine whether it is ”with” or ”without” methodandanalyzetheassociatedinfluentialfactors,thisstudy
according to the actual demand. We find that considering the investigates the following RQs:
API requirement, the generation accuracy can be enhanced RQ1: How effective is the designed prompt for ChatGPT?
(BLEU=22.14 and CodeBLEU=44.18). Meanwhile, using the As described in Sections IV-B and IV-B, we leveraged CoT
whole behaviour prompt (i.e., API + exception handling), the strategy [42] to manually augment prompts for two code
performance can be further boosted with BLEU=27.48 and generation tasks with multi-step optimizations. The first RQ
CodeBLEU=46.78. intends to evaluate the effectiveness of the designed prompts
on the corresponding testing datasets, and verifies the validity
C. Prompt Design for Code-to-Code Generation
of our design methods.

### AstheC2Cgenerationhasasimilarprocessofpromptdesign


### RQ2: How does the conciseness request affect ChatGPT?

as the T2C generation, we mainly show their key differences
In the prompt design, we observed that ChatGPT often
in this subsection.
generates detailed code, much more complex than the ground
Prompt Description. According to the task description in truth.Thus,onegoalofthemulti-stepoptimizationsistoguide
Section III-B, our C2C generation task aims to generate a ChatGPT to generate concise code with a series of prompts.
Java code method according to a given C# code function. It is worth investigating whether the generation performance
Based on the task requirement, we form the task prompt: can be further improved by directly requesting ChatGPT for a
”translate C# code into Java code: #{Code}” (Table I-P1). concise generation.
For the randomly selected 100 samples from training data, the

### RQ3: How does the session setting affect ChatGPT?When

generation performance is BLEU=9.76 and CodeBLEU=39.37.
communicating with ChatGPT, we started one individual
Multi-Step Optimizations. Comparing with the T2C genera- session for each prompt. Meanwhile, it is widely known that
tion, we can find many differences in the C2C generation ChatGPT can learn the session context and generate better
task: the C2C dataset does not involve the related class; responses from the context [42], [49]. Therefore, this RQ
ChatGPT does not generate comments and throws to the code; intends to answer whether ChatGPT can generate better code
the ground-truth are not pre-processed for the method name, by inputting a session with a number of prompts.
modifiers,argumentnames,andlocalvariablenames.However,

### RQ4: How does the generation randomness affect Chat-

ChatGPT will generate annotation following the C# code but

### GPT? It is known that ChatGPT may generate code with

theground-truthremovedalltheannotations.Therefore,weadd
slightdifferenceseverytimeforthesameprompt[50],[51].To
asimpleprocessingprompttothetaskprompt:”donotprovide
investigatehowrandomnessaffectsthegenerationperformance,
annotation” (Table I-P3). Moreover, we find that ChatGPT
we rerun the guided-ChatGPT multiple times and analyze the
has the ability to understand the markdown syntax in the
stability of the generation performance.
prompt. Thus, in the task prompt, we change #{Code} to
”’#{Code}”’asanupdatedtaskprompt(TableI-P4).Testingon V. RESULTS
thesampleswiththeprocessingprompt,thegenerationaccuracy
This section presents the experimental settings and results
is improved on CodeBLEU (45.28) but not on BLEU (8.55).
for the four RQs described in Section IV-D.
After updating the code format in the task prompt, we achieve
furtherenhancementwithBLEU=15.44andCodeBLEU=45.00. A. Effectiveness of the Designed Prompt (RQ1)
Same to T2C generation, we extract the requirement of the

### Objective.Toassesstheeffectivenessofthedesignedprompts,

API usage and exception handling from the ground-truth code.
we intend to present some baselines, test them on the testing

### Subsequently, we added this information to the task prompt

data of corresponding code generation tasks, and analyze the
as a behaviour prompt: ”translate C# code into Java code:
effectiveness in terms of prediction accuracy.
”’#{Code}”’ #{that calls ...} with[out] exception handling”
(Table I-P5). Experimental results on the samples show that Method. This study presents three baselines that can generate
by adding the requirements of API usage (BLEU=13.37 and code by using ChatGPT with three levels of prompts: 1)
CodeBLEU=46.17), the generation accuracy will be slightly ChatGPT-task, we used the task prompts in Table I(P1) as
improved in terms of CodeBLEU. Moreover, using the whole the input of ChatGPT, because they can represent the common
behaviour prompt also showed a reduction in BLEU (8.90) chatting conditions with a direct request of code generation.
and a minor increase in CodeBLEU (46.88). We observed that 2) ChatGPT-detail, we merged the prompts of task, context,
5

<!-- Page 6 -->

processing, and updated task for two tasks in Table I(P1-P4). B. Impacts of Conciseness Request (RQ2)
Note that the T2C generation has no updated task prompt (P4)
while the C2C generation contains no context prompt (P2). 3) Objective. In our prompt design, we guided ChatGPT to
ChatGPT-behaviour, based on the baseline ChatGPT-detail, we removeirrelevantcodecomponents.However,weobservedthat
the generated code is still more complex than the ground-truth.
further updated the task prompt with the behaviour prompt
Without more information, we cannot design better prompts.
(Table I-P5) to provide more guidance on the code generation.

### Therefore,thisRQintendstoinvestigatewhetherwecanchange

Although Section IV-C showed that P5 has negative effects
thetaskpromptbydirectlyaskingChatGPTtogenerateamore
on the C2C generation task for the sampled data, we still set
concise code, instead of manually adding specific instructions.
up this baseline for C2C generation to further confirm the
previous observation. The testing data and evaluation metrics Method. RQ1 showed that ChatGPT-behaviour and ChatGPT-
were elaborated in Section III. detail are the best baselines for T2C and C2C generation tasks,
respectively. To add conciseness requests to their prompts,
we found one viable and simple way to add the word

## Tableiii

”concise” before the generation targets. Specifically, for the

## Testingthreebaselinesont2Candc2Cgenerationtasks.


### T2C generation, the behaviour prompt of ChatGPT-behaviour

Task Model BLEU CodeBLEU is changed to ”write a concise Java method ...” (Table I-P5).
Likewise, for the C2C generation task, the task prompt of

### ChatGPT-task 05.63 28.05

T2C ChatGPT-detail 14.09(+140.27%) 39.90(+42.25%) ChatGPT-detail is updated: ”translate C# code into concise
ChatGPT-behaviour 21.59(+283.48%) 48.69(+73.58%) Java code ...” (Table I-P4). To evaluate the impacts of the
ChatGPT-task 10.61 46.12 conciseness request, we tested the modified prompts on the
C2C ChatGPT-detail 15.79(+48.82%) 47.71(+03.45%) testing data.
ChatGPT-behaviour 09.47(-10.74%) 47.38(+02.32%)

## Tableiv


## Testingthebestbaselinesinrq1With(Orwithout)The


## Concisenessrequest(C)Ont2Candc2Cgenerationtasks.


### Result. On the T2C generation task, Table III shows that

ChatGPT-task achieves an generation accuracy of BLEU=5.63

### Task Model BLEU CodeBLEU

and CodeBLEU=28.05. For the ChatGPT-detail with a num-

### ChatGPT-behaviour 21.59 48.69

ber of extended prompts, its generation performance is T2C

### ChatGPT-behaviour-C 26.86(+24.41%) 50.18(+03.06%)

BLEU=14.09 and CodeBLEU=39.90, outperforming ChatGPT-

### ChatGPT-detail 15.79 47.71

task by 140.27% and 42.25% in terms of BLEU and Code- C2C

### ChatGPT-detail-C 16.75(+06.08%) 46.62(-02.28%)

BLEU respectively. Additionally, the last baseline ChatGPT-
behaviour gained a better performance of T2C generation
with BLEU=21.59 and CodeBLEU=48.69. We can notice Result. For the T2C generation task, Table IV shows that the
that ChatGPT-behaviour improved the performance of the conciseness request is helpful (ChatGPT-behaviour-C) with
ChatGPT-task by 283.48% and 73.58% in terms of BLEU BLEU=26.86 and CodeBLEU=50.18. Compared with the best
and CodeBLEU, respectively. These results indicate that our baseline in RQ1 (ChatGPT-behaviour), these two evaluation
designed prompts associated with the design method can metricsarefurtherenhancedby24.41%and3.06%,respectively.
substantially improve the T2C generation for ChatGPT. Meanwhile, we notice that by adding the conciseness request
to the C2C generation task, the generation performance of
In terms of the C2C generation task, Table III shows that
ChatGPT-detail-C shows a slight decrease in terms of the
ChatGPT-tasks can obtain better performance (BLEU=10.61
CodeBLEU (46.62) compared with the ChatGPT-detail (best
andCodeBLEU=46.12)comparedwiththeT2Cgenerationtask.
baseline in RQ1), although the BLUE score is improved by
Furthermore, the ChatGPT-detail shows better generation accu-
6.08%. These results suggest that the conciseness request is
racy with BLEU=15.79 and CodeBLEU=47.71, outperforming
useful for T2C generation but not for C2C generation.
thoseofChatGPTby48.82%and3.45%respectively.However,
wecanfindthatChatGPT-behaviourshowspoorerperformance
with BLEU=9.47 and CodeBLEU=47.38, increased those of Answer to RQ2: Adding conciseness request to the
ChatGPT-task by -10.74% and 2.32%. Therefore, ChatGPT- prompt can further improve the performance of the T2C
detail shows better performance than ChatGPT-behaviour. generation, but show minor negative effects on the C2C
These results imply that for the C2C task, the designed prompt generation.
can also improve the generation performance for ChatGPT.

### C. Impacts of Session Setting (RQ3)

Answer to RQ1: Our prompt design method can substantiallyimprovetheperformanceofT2CandC2Cgeneration Objective. By default, we opened an individual session for
tasks by guiding ChatGPT with better prompts. eachprompt andcommunicated withChatGPT.In contrast,the
communication can be worked with a continuous session that
6

<!-- Page 7 -->

generates responses for a number of prompts. In this way, the TABLEVI
ChatGPT can learn from the context and may generate better TESTINGTHEBESTBASELINESINRQ3ONT2CANDC2CGENERATION

## Tasksinfiverounds(Rq1-R5),Where”Min”,”Max”,”Avg”,

responses for the code generation tasks. Thus, this RQ aims

## ”Std”Standfortheminimum,Maximum,Averageandstandard

to analyze the effects of the session setting. DEVIATIONOFTHEGENERATIONACCURACY.
Method. During the communication with ChatGPT, we used

### Task Model BLEU CodeBLEU

one session to generate code for a number of prompts. When

## R1 26.86 50.18

the number reaches the maximum limit, a further prompt will

## R2 26.85 50.07

receive no response. Then, we started another new session. In R3 27.02 50.18
this way, we can ensure that each session is fully utilized and R4 26.92 50.20

## T2C R5 27.00 50.17


### ChatGPT can better understand the context. We know that the

amount of contextual information would be lower for the prior MIN 26.86 50.07

## Max 27.02 50.20

promptswithinasession.Itisworthnothingtoinvestigatehow

## Avg 26.93 50.16

the session setting affects the code generation performance. STD 00.08 00.05

## R1 16.82 48.80


## Tablev R2 17.34 49.17


## Testingthebestbaselineinrq2With(Orwithout)Thesession R3 17.23 48.38


## Setting(S)Ont2Candc2Cgenerationtasks. R4 17.32 49.15


## C2C R5 17.21 48.80

Task Model BLEU CodeBLEU MIN 16.82 48.80

## Max 17.34 49.17

ChatGPT-behaviour-C 26.86 50.18

## T2C Avg 17.18 48.86

ChatGPT-behaviour-CS 29.29(+09.05%) 49.74(-00.88%)

## Std 00.21 00.33

ChatGPT-detail 15.79 47.71

## C2C


### ChatGPT-detail-S 16.82(+06.52%) 48.80(+02.28%)

standard deviation (STD) of the performance of these multiple
Result. As shown in Table V, using the continuous session generation results. Based on these measurements, we analyzed
(ChatGPT-behaviour-CS) showed no overall improvement for the generation stability and the effects of the randomness.
the T2C generation with BLEU=29.29 and CodeBLEU=49.74.

### Result. From Table VI, we can observe that the five rounds

Compared with the best baseline in RQ2 (ChatGPT-behaviourof T2C generation show a stable performance, where BLEU
C), the BLEU score is improved by 9.05% but the CodeBLEU
rangesfrom26.86to27.02withaverage=26.93andSTD=0.08;
is decreased by 0.88%. On the other hand, the continuous

### CodeBLEUrangesfrom50.07to50.20withaverage=50.16and

session can present improvement for the C2C generation task
STD=0.05. Meanwhile, the multiple runs of C2C generation
(ChatGPT-detail-S) with BLEU=16.82 and CodeBLEU=48.80.
also show a stable prediction accuracy, where BLEU ranges
Compared with the best baseline ChatGPT-detail in RQ2,
from 16.82 to 17.34 with average=17.18 and STD=0.21;
the evaluation metrics are further improved by 6.52% and

### CodeBLEUrangesfrom48.80to49.17withaverage=48.86and

2.28%, respectively. These experimental results indicate that

### STD=0.33.TheseresultsindicatethattestingChatGPTwithour

thecontinuoussessionisbeneficialfortheC2Cgenerationtask
designed prompts will generate stable responses. We observed
buthasnoimprovementfortheT2Cgenerationtask.Therefore,
that the major reason is that the instructions in the prompts
the individual session is more suitable for the T2C generation
are specific so that the generation randomness is limited. As
with the designed prompts.
we observed that the effect of the randomness is negligible,
we did not extend this RQ with more rounds of experiments.

### Answer to RQ3: The continuous session is helpful for

the T2C generation task while the individual session is
Answer to RQ4: The generation randomness shows little
suitable for the C2C generation task.
effect on the code generation tasks due to the specific
instructions described in the designed prompts.

### D. Impacts of Generation Randomness (RQ4)


### Objective. Commonly, ChatGPT generates responses with

slight differences to balance the accuracy and creativity. Thus, VI. DISCUSSION
the generation randomness may affect the performance of code
generation. This RQ investigates how randomness affects the
This section provides some qualitative analysis of the
effectiveness of the designed prompts.
designed prompts. Specifically, Section VI-A compares our
Method. To reach the goal, we ran the best baselines (i.e., code generation performance with existing fine-tuned models.
ChatGPT-behaviour-C and ChatGPT-detail-S) in RQ3 five Sections VI-B and VI-C analyze the correctness and quality
times, respectively. We computed the average (AVG) and of the code generated by ChatGPT with our designed prompts.
7

<!-- Page 8 -->

A. Comparison with Fine-Tuned Models Method.Werandomlyselected100samplesfromthegenerated
code of each code generation task (T2C and C2C). The
Objective. Section V indicates that the designed prompts can correctness is measured by functional equivalency between
guideChatGPTtogeneratesubstantiallybettercode.Thisresult the generated code and the ground-truth. The relevancy is
implies the effectiveness of the ”pre-train, prompt, predict” voted by three authors (the first, second, and fourth), where
paradigm for LLMs as described in Section II-B. However, relevancy is determined when the number of votes is larger
many LLMs based on the ”pre-train, fine-tune” paradigm than or equal to two.
have been successfully applied in the code generation tasks

### Result.TableVIIIshowsthatamongthe100samples,theT2C

as exemplified in Section II-A. Therefore, we would like to
task only generated 31 equivalent code as the ground-truth in
compare the performance of these two paradigms. Specifically,
functional behaviours. We observed that higher CodeBLEU
we investigate how effective is our method compared with the
only indicates correct lexical match, syntactic match, and data
existing fine-tuned LLMs on code generation tasks.
flow match, but does not necessarily suggest functional equiva-
Method. In this study, we tested our method on the widely lency. Meanwhile, the NL descriptions for T2C generation are
used dataset CodeXGlue [5], which provides a number of usuallynotspecific,andChatGPTislikelytomisunderstandthe
benchmark models. We used the experimental results reported requirement.Asimpleexampleisthatfortheground-truthcode
by Lu et al. [5] as comparisons. Moreover, we went through ”Stringfunction(){returnnamespaceURI;}”whichmeansreturn
all the related works presented in Section II-A. We found that the variable namespaceURI, but the NL description provided
Wang et al. [33] also tested their proposed model CodeT5 and in the dataset is ”Get the WS-ReliableMessaging namespace to
baseline model PLBART [34] on CodeXGlue, so we included be used for encoding and decoding messages”. Therefore, for
thesemodelsinourcomparisons.Weexcludedtheotherreports the prompt of T2C generation, the NL description may need
in the related work because they did not use the CodeXGlue to be refined in some ways.
dataset or did not report the CodeBLEU metric following [5]. For the C2C generation task, we found 59 generated code
snippets that are functionally equivalent to their ground-truth,

### Result. Table VII illustrated the included fine-tuned LLMs

much better than that for the T2C task. We noticed that the
for two code generation tasks, the description and reference
translation from C# code provides many useful contexts so
of the related LLM, and the reported scores of BLEU and
that ChatGPT can generate the corresponding Java code line

### CodeBLEU.Wealsoplacedourbestpromptsettings(ChatGPT-

by line. However, the T2C generation works only for the code
best) in the table. We can find that ChatGPT-best shows the
with commonly used APIs.
best performance on the T2C generation tasks in terms of

### CodeBLEU. This result implies that guiding ChatGPT with

our designed prompts outperforms the other state-of-the-art Finding 2: ChatGPT with the best prompt shows better
fine-tuned LLMs. However, for the C2C generation task, the correctnessontheC2CtaskthanontheT2Ctask,because
ChatGPT-best achieved the fifth rank, only outperforming the NL descriptions are not rigorous.

### PBSMT [54]. This poorer performance on the C2C task may

result from the limited contextual information, so we cannot

### C. Quality of Code Generation

extend the designed prompt with more specific instructions as
showninSectionV-A.Moreover,theseresultscandemonstrate
Objective. Quality is an important feature of a good generated
the potential capabilities of the ”pre-train, prompt, predict”
code, in spite of the correctness of code generation. In this
paradigm, because the performance could be further improved
study, we also investigated the quality of the code generated
by providing prompts with more specific instructions or fineby ChatGPT with our designed prompts. Meanwhile, we also
tuning ChatGPT with related training data.
checked the quality of the ground-truth code to compare its
quality with the generated code.

### Finding 1: Guiding ChatGPT with our designed prompt

Method. To measure the quality of the code generation, we
outperforms the state-of-the-art fine-tuned LLMs for the
utilized the SonarQube (version 9.8) [55], a widely used open-

### T2C generation, but it shows a poorer rank on the

source platform for analyzing and tracking the quality of

### C2C generation due to the limited contextual information

code [56], [57]. It can check three types of quality issues
expressed in the prompt.
(bug, vulnerability, and code smell) in five severity levels (i.e.,
blocker, critical, major, minor, and info) [55]. In this study,
we measured the quality of code generation by counting the

### B. Correctness of Code Generation

number of code that contain critical or blocker issues. This is
because these two severity levels have strong impacts which
Objective. CodeBLEU (or BLEU) is an effective and widely
are commonly considered by developers, where the blocker
used metric for automated evaluations. But a generated code
level has a higher likelihood than the critical.
with a high score may not be correct. Therefore, we would
like to investigate the correctness of the code generated from Result. Table IX shows that for the T2C generation the code
our best prompt settings. generated by ChatGPT-best shows lightly better quality than
8

<!-- Page 9 -->


## Tablevii

COMPARISONSBETWEENTHEBESTPROMPTS(CHATGPT-BEST)ANDTHESTATE-OF-THE-ARTFINE-TUNEDLLMSREPORTEDIN[5]AND[33]ONT2CAND

## C2Cgenerationtasks.


### Task Model Description BLEU CodeBLEU


### Seq2Seq AnRNN-basedsequencetosequencemodel[52]. 21.31 26.39

Acontext-awareencoder-decodermodethatleveragesmodel-agnostic
Seq2Action+MAML 24.40 29.46
meta-learning(MAML)[53].
Generative Pre-trained Transformer 2 (GPT-2) pre-trained on a very

## Gpt-2 25.37 29.69

largecorpusofEnglishdatainaself-supervisedfashion[25].

### ATransformer-basedlanguagemodelthathasthesamemodelarchitec-

CodeGPT tureandtrainingobjectiveofGPT-2andpre-trainedontheprogramming 28.69 32.71
language(PL)[5].
T2C CodeGPT-adapted CodeGPTiscontinuallytrainedonthecodecorpus[5]. 32.79 35.98
Asequence-to-sequencemodelcapableofperformingabroadspectrum

## Plbart 36.69 38.52

ofprogramandlanguageunderstandingandgenerationtasks[34].
A unified pre-trained encoder-decoder Transformer model that better
CodeT5 leverages the code semantics conveyed from the developer-assigned 41.48 44.10
identifiers[33].
ChatGPT-behaviour-C, the ChatGPT works with context prompt, be-

### ChatGPT-best 26.86 50.18

haviourprompt,processingprompt,andconcisenessrequest.
Atraditionalphase-basedmachinetranslationmethodthatusesstatistical

## Pbsmt 40.06 43.48

modelstotranslatetextfromonelanguagetoanother.[54]
ChatGPT-detail-S, the ChatGPT works with an updated task prompt,

### ChatGPT-best 16.82 48.80

processingprompt,andcontinuoussession.
A sequence-to-sequence encoder-decoder model with self-attention
C2C Transformer 50.47 61.59
mechanism[27].
Abidirectionalencoderrepresentationsfromtransformers(BERT)model

### CodeBERT 72.14 79.41

withpre-trainedwithsixprogramminglanguages[11].
ItisbasedonthearchitectureoftheBERTmodelandispre-trainedon

### RoBERTa 71.99 80.18

alargecorpusoftextusingamaskedlanguagemodelingobjective[53].
Asequence-to-sequencemodelcapableofperformingabroadspectrum

## Plbart 65.00 85.27

ofprogramandlanguageunderstandingandgenerationtasks[34].
TABLEVIII method; 5) renaming method to prevent misunderstanding; and
NUMBEROFCODEGENERATEDBYCHATGPT-BESTTHATHAVE 6) using a copy constructor or copy factory instead of ”clone”

## Functionalequivalencywiththecorrespondingground-Truth

implementation. We believe that it is worthy of addressing

## Amongthe100Samples.

the bug and code smells detected by SonarQube, although the
Task T2C C2C number is not large compared to the total count of the dataset.
Therefore, ChatGPT may be not able to ensure the quality of
# Relevancy 31 59
the generated code, which require further investigations.
the ground-truth. Specifically, SonarQube found one critical Finding 3: The code generated by ChatGPT contains no
bug that reminds us of making sure a local variable is not zero severe bug or vulnerability on the experimented datasets
beforedoingthedivision.Andtheother29issuesbelongtothe but they contain many code smells, which should be
critical code smell that requires further attention. In contrast, addressed by developers.
the associated ground-truth contain 35 code smells. For the
C2C generation, the generated code possess 62 code smells,

## Vii. Implication

much higher than the number of the related ground-truth (17

### Basedonourexperimentalresultsanddiscussion,thissection

code smells). In these two tasks, the generated code involve
provides implications for developers and researchers.
no severe bug or vulnerability.
We found that the identified code smells mainly provide six Tips of Using ChatGPT Prompts for Developers. Our
kinds of suggestions: 1) defining a constant instead of dupli- experimental results showed that guiding ChatGPT with
cating a String; 2) replacing the call of ”replaceAll()” by ”re- carefully crafted prompts can substantially improve the code
place()”;3)reducingcognitivecomplexityofacode;4)adding generation performance. To make the most of ChatGPT’s
default case to a switch, not overriding the Object.finalize() capabilities, developers are suggested to provide prompts with
9

<!-- Page 10 -->


## Tableix

QUALITYANALYSISOFTHECODEGENERATEDBYCHATGPT-BESTANDTHECORRESPONDINGGROUND-TRUTHONT2CANDC2CGENERATIONTASKS.
# Bug #Vulnerability #CodeSmell

### Task Data Total

Blocker Critical Blocker Critical Blocker Critical
GeneratedCode 0 1 0 0 0 29 30

## T2C


### Ground-Truth 0 0 0 0 1 34 35

GeneratedCode 0 0 0 0 56 6 62

## C2C


### Ground-Truth 0 0 0 0 10 7 17

rich programming context, including relevant classes, member Manual Prompt Design. Same as other prompt engineering
variables,andfunctions.Additionally,ChatGPTcanunderstand studies with manual construction, the prompt design and
code, so developers can instruct it to preprocess code, such as multi-step optimizations are conducted according to human
removing summaries and changing variable names. Enclosing understandingandobservations.Theknowledgeofthedesigner
codesnippetsin”’couldalsohelpChatGTPbettercomprehend may affect the performance of the used prompts. Moreover,
code blocks with markdown syntax. To generate code with our design and combination choices were based on the 100
expected APIs or in a concise form, developers can directly randomly selected samples, and the size and randomness of
request ChatGPT. Chatting with ChatGPT in one continuous the sampling may bring in different choices. However, this
session may also be beneficial because it can understand the study aims to explore the viability of prompt design and
context and refine its responses. With the chain-of-thoughts investigate some related influential factors. Our experimental
feature, developers can optimize their prompts step-by-step by results demonstrate the effectiveness of the designed prompts.
considering ChatGPT’s feedback. However, developers should In the future, we would like to investigate prompt engineering
remain cautious about the quality of the generated code, even with automated construction methods [28], [41].
if the function-level generation appears free of severe bugs or
Limited Testing.Inourstudy,weconductedalimitednumber
vulnerabilities in our experiments.
of testing as presented in Section V, such as the combinations
PotentialFutureResearchDirectionsforResearchers.This of prompt selection and combinations, conciseness request and
study demonstrates that providing ChatGPT with improved session settings, and multiple runs for generation randomness.
promptscanenhancecodegenerationperformance,outperform- We suppose that more tests may help us further improve the
ing that of state-of-the-art fine-tuned LLMs. Future studies designed prompts and strengthen our conclusions and findings.
could investigate methods for automatically designing and However,invokingChatGPTAPIonthewholedatasetrequires
optimizing prompts for code generation tasks; design a better a high cost. Therefore, we only tested a limited number of
evaluation metric to automatically assess the correctness of the choices that are likely to improve the generation performance,
generated code; and further assess and improve the quality of so that we can demonstrate the importance of prompt design
the code generation. Our study also highlights the potential of for ChatGPT.
LLMs like ChatGPT, utilizing the ”pre-train, prompt, predict”

### HumanEvaluation.Toassessthecorrectnessofthegenerated

paradigm and prompt engineering, to impact the field of SE
code, we randomly selected 100 samples to analyze the
research.
relevancy between the generated code and ground-truth. The
relevancy was determined by human evaluations. To mitigate

## Viii. Threatstovalidity

the effects of the subjective bias, the determinations are based
There are some potential threats affecting the validity of our onthevotingofthreeauthors.Althoughthenumberofsamples
experimental results and conclusions. is limited, the correctness analysis of these random samples
provided some useful insights for further studies.

### Limited Tasks and Dataset. This study proposed a method

for prompt design on two code generation tasks. The method IX. CONCLUSION
may not be suitable for other generation tasks, such as Inthispaper,wedesignedandimprovedpromptsforguiding
code completion [58] and test case generation [59]. For the ChatGPT on two code generation tasks, including text-toinvestigated T2C and C2C generation tasks, we only chose codegenerationandcode-to-codegeneration.Ourexperimental
one dataset CodeXGlue [5] as our study subject, although it is results showed the effectiveness of our prompts when asking
a widely used dataset. On the C2C generation task, we tested ChatGPTtogeneratecodeonawidelyuseddatasetCodeXGlue.
the generation from C# to Java. It is uncertain whether our Moreover, we investigated the influential factors for designing
experimental results and findings could be extended to other prompts on code generation tasks. Besides, we compared the
languages (e.g., Python and Go) and the reverse generation performance of the best prompts with the state-of-the-art fine-
(i.e.,fromJavatoC#).Inthenearfuture,weplantoinvestigate tuned LLMs, and assessed the correctness and quality of the
our designed prompts on more programming languages, other codegeneratedbyChatGPT.Basedonourfindings,wepresent
datasets, and more types of code generation tasks. the potential future research directions.
10

<!-- Page 11 -->

REFERENCES [25] A.Radford,J.Wu,R.Child,D.Luan,D.Amodei,I.Sutskeveretal.,
“Languagemodelsareunsupervisedmultitasklearners,”OpenAIblog,
vol.1,no.8,p.9,2019.
[1] J.Herrington,Codegenerationinaction. ManningPublicationsCo.,
[26] T.Brown,B.Mann,N.Ryder,M.Subbiah,J.D.Kaplan,P.Dhariwal,
2003.
A.Neelakantan,P.Shyam,G.Sastry,A.Askelletal.,“Languagemodels
[2] G. Poesia, O. Polozov, V. Le, A. Tiwari, G. Soares, C. Meek, and
arefew-shotlearners,”Advancesinneuralinformationprocessingsystems,
S.Gulwani,“Synchromesh:Reliablecodegenerationfrompre-trained
vol.33,pp.1877–1901,2020.
languagemodels,”arXivpreprintarXiv:2201.11227,2022.
[27] A.Vaswani,N.Shazeer,N.Parmar,J.Uszkoreit,L.Jones,A.N.Gomez,
[3] F.F.Xu,Z.Jiang,P.Yin,B.Vasilescu,andG.Neubig,“Incorporating

### Ł.Kaiser,andI.Polosukhin,“Attentionisallyouneed,”Advancesin

external knowledge through pre-training for natural language to code
neuralinformationprocessingsystems,vol.30,2017.
generation,”arXivpreprintarXiv:2004.09015,2020.
[28] P.Liu,W.Yuan,J.Fu,Z.Jiang,H.Hayashi,andG.Neubig,“Pre-train,
[4] D. Guo, S. Ren, S. Lu, Z. Feng, D. Tang, S. Liu, L. Zhou, N. Duan, prompt,andpredict:Asystematicsurveyofpromptingmethodsinnatural
A. Svyatkovskiy, S. Fu et al., “Graphcodebert: Pre-training code languageprocessing,”ACMComputingSurveys,vol.55,no.9,pp.1–35,
representationswithdataflow,”arXivpreprintarXiv:2009.08366,2020. 2023.
[5] S.Lu,D.Guo,S.Ren,J.Huang,A.Svyatkovskiy,A.Blanco,C.Clement, [29] D.Guo,S.Lu,N.Duan,Y.Wang,M.Zhou,andJ.Yin,“Unixcoder:
D. Drain, D. Jiang, D. Tang et al., “Codexglue: A machine learning Unifiedcross-modalpre-trainingforcoderepresentation,”arXivpreprint
benchmarkdatasetforcodeunderstandingandgeneration,”arXivpreprint arXiv:2203.03850,2022.
arXiv:2102.04664,2021. [30] S. Liu, B. Wu, X. Xie, G. Meng, and Y. Liu, “Contrabert: Enhanc-
[6] E.Nijkamp,B.Pang,H.Hayashi,L.Tu,H.Wang,Y.Zhou,S.Savarese, ing code pre-trained models via contrastive learning,” arXiv preprint
andC.Xiong,“Codegen:Anopenlargelanguagemodelforcodewith arXiv:2301.09072,2023.
multi-turnprogramsynthesis,”arXivpreprintarXiv:2203.13474,2022. [31] P.Jain,A.Jain,T.Zhang,P.Abbeel,J.E.Gonzalez,andI.Stoica,“Con-
[7] S.Liu,Y.Li,andY.Liu,“Commitbart:Alargepre-trainedmodelfor trastivecoderepresentationlearning,”arXivpreprintarXiv:2007.04973,
githubcommits,”arXivpreprintarXiv:2208.08100,2022. 2020.
[8] D.Araci,“Finbert:Financialsentimentanalysiswithpre-trainedlanguage [32] A.Mastropaolo,S.Scalabrino,N.Cooper,D.N.Palacio,D.Poshyvanyk,
models,”arXivpreprintarXiv:1908.10063,2019. R.Oliveto,andG.Bavota,“Studyingtheusageoftext-to-texttransfer
[9] J. Zhou, J. Tian, R. Wang, Y. Wu, W. Xiao, and L. He, “Sentix: A transformer to support code-related tasks,” in 2021 IEEE/ACM 43rd
sentiment-awarepre-trainedmodelforcross-domainsentimentanalysis,” InternationalConferenceonSoftwareEngineering(ICSE). IEEE,2021,
inProceedingsofthe28thinternationalconferenceoncomputational pp.336–347.
linguistics,2020,pp.568–579. [33] Y.Wang,W.Wang,S.Joty,andS.C.Hoi,“Codet5:Identifier-aware
[10] B.Gunel,J.Du,A.Conneau,andV.Stoyanov,“Supervisedcontrastive unifiedpre-trainedencoder-decodermodelsforcodeunderstandingand
learning for pre-trained language model fine-tuning,” arXiv preprint generation,”arXivpreprintarXiv:2109.00859,2021.
arXiv:2011.01403,2020. [34] W. U. Ahmad, S. Chakraborty, B. Ray, and K.-W. Chang, “Unified
[11] Z.Feng,D.Guo,D.Tang,N.Duan,X.Feng,M.Gong,L.Shou,B.Qin, pre-trainingforprogramunderstandingandgeneration,”arXivpreprint
T.Liu,D.Jiangetal.,“Codebert:Apre-trainedmodelforprogramming arXiv:2103.06333,2021.
andnaturallanguages,”arXivpreprintarXiv:2002.08155,2020. [35] A. Svyatkovskiy, S. K. Deng, S. Fu, and N. Sundaresan, “Intellicode
[12] J.Devlin,M.-W.Chang,K.Lee,andK.Toutanova,“Bert:Pre-training compose: Code generation using transformer,” in Proceedings of the
ofdeepbidirectionaltransformersforlanguageunderstanding,”arXiv 28thACMJointMeetingonEuropeanSoftwareEngineeringConference
preprintarXiv:1810.04805,2018. andSymposiumontheFoundationsofSoftwareEngineering,2020,pp.
[13] C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, 1433–1443.
Y.Zhou,W.Li,andP.J.Liu,“Exploringthelimitsoftransferlearning [36] H.Husain,H.-H.Wu,T.Gazit,M.Allamanis,andM.Brockschmidt,
withaunifiedtext-to-texttransformer,”TheJournalofMachineLearning “Codesearchnetchallenge:Evaluatingthestateofsemanticcodesearch,”
Research,vol.21,no.1,pp.5485–5551,2020. arXivpreprintarXiv:1909.09436,2019.
[37] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. d. O. Pinto, J. Kaplan,
[14] OpenAI,“Chatgptofficialblog,”https://openai.com/blog/chatgpt,2023.

### H.Edwards,Y.Burda,N.Joseph,G.Brockmanetal.,“Evaluatinglarge

[15] R.Khoury,A.R.Avila,J.Brunelle,andB.M.Camara,“Howsecureis
language models trained on code,” arXiv preprint arXiv:2107.03374,
codegeneratedbychatgpt?”arXivpreprintarXiv:2304.09655,2023.
2021.
[16] L.Ouyang,J.Wu,X.Jiang,D.Almeida,C.Wainwright,P.Mishkin,
[38] G.Inc.,“Copilot,”https://github.com/features/copilot,2023.
C. Zhang, S. Agarwal, K. Slama, A. Ray et al., “Training language
[39] OpenAI,“Gpt-4technicalreport,”https://doi.org/10.48550/arXiv.2303.
modelstofollowinstructionswithhumanfeedback,”AdvancesinNeural
08774,2023.
InformationProcessingSystems,vol.35,pp.27730–27744,2022.
[40] D. Rajagopal, V. Khetan, B. Sacaleanu, A. Gershman, A. Fano, and
[17] A.Kothari,“Chatgpt,largelanguagemodels,andgenerativeaiasfuture
E. Hovy, “Template filling for controllable commonsense reasoning,”
augmentsofsurgicalcancercare,”AnnalsofSurgicalOncology,pp.1–3,
arXivpreprintarXiv:2111.00539,2021.
2023.
[41] S.Qiao,Y.Ou,N.Zhang,X.Chen,Y.Yao,S.Deng,C.Tan,F.Huang,
[18] V.LiuandL.B.Chilton,“DesignguidelinesforpromptengineeringtextandH.Chen,“Reasoningwithlanguagemodelprompting:Asurvey,”
to-imagegenerativemodels,”inProceedingsofthe2022CHIConference
arXivpreprintarXiv:2212.09597,2022.
onHumanFactorsinComputingSystems,2022,pp.1–23.
[42] J. Wei, Y. Tay, R. Bommasani, C. Raffel, B. Zoph, S. Borgeaud,
[19] S.Ren,D.Guo,S.Lu,L.Zhou,S.Liu,D.Tang,N.Sundaresan,M.Zhou, D.Yogatama,M.Bosma,D.Zhou,D.Metzleretal.,“Emergentabilities
A.Blanco,andS.Ma,“Codebleu:amethodforautomaticevaluationof oflargelanguagemodels,”arXivpreprintarXiv:2206.07682,2022.
codesynthesis,”arXivpreprintarXiv:2009.10297,2020.
[43] Z.Zhang,A.Zhang,M.Li,andA.Smola,“Automaticchainofthought
[20] J.Wei,X.Wang,D.Schuurmans,M.Bosma,E.Chi,Q.Le,andD.Zhou, promptinginlargelanguagemodels,”arXivpreprintarXiv:2210.03493,
“Chainofthoughtpromptingelicitsreasoninginlargelanguagemodels,” 2022.
arXivpreprintarXiv:2201.11903,2022. [44] S. Mishra, A. Mitra, N. Varshney, B. Sachdeva, P. Clark, C. Baral,
[21] J.Salazar,D.Liang,T.Q.Nguyen,andK.Kirchhoff,“Maskedlanguage and A. Kalyan, “Numglue: A suite of fundamental yet challenging
modelscoring,”arXivpreprintarXiv:1910.14659,2019. mathematicalreasoningtasks,”arXivpreprintarXiv:2204.05660,2022.
[22] Y.Liu,M.Ott,N.Goyal,J.Du,M.Joshi,D.Chen,O.Levy,M.Lewis, [45] S.Iyer,I.Konstas,A.Cheung,andL.Zettlemoyer,“Mappinglanguageto
L.Zettlemoyer,andV.Stoyanov,“Roberta:Arobustlyoptimizedbert codeinprogrammaticcontext,”arXivpreprintarXiv:1808.09588,2018.
pretrainingapproach,”arXivpreprintarXiv:1907.11692,2019. [46] K.Papineni,S.Roukos,T.Ward,andW.-J.Zhu,“Bleu:amethodfor
[23] A.Alokla,W.Gad,W.Nazih,M.Aref,andA.-b.Salem,“Pseudocode automaticevaluationofmachinetranslation,”inProceedingsofthe40th
generationfromsourcecodeusingthebartmodel,”Mathematics,vol.10, annualmeetingoftheAssociationforComputationalLinguistics,2002,
no.21,p.3967,2022. pp.311–318.
[24] C.Niu,C.Li,V.Ng,J.Ge,L.Huang,andB.Luo,“Spt-code:sequence- [47] M.Suzgun,N.Scales,N.Scha¨rli,S.Gehrmann,Y.Tay,H.W.Chung,
to-sequence pre-training for learning source code representations,” in A.Chowdhery,Q.V.Le,E.H.Chi,D.Zhouetal.,“Challengingbig-
Proceedingsofthe44thInternationalConferenceonSoftwareEngineer- benchtasksandwhetherchain-of-thoughtcansolvethem,”arXivpreprint
ing,2022,pp.2006–2018. arXiv:2210.09261,2022.
11

<!-- Page 12 -->

[48] OpenAI,“Chatgptapi,”https://platform.openai.com/docs/api-reference, GermanConferenceonAI,KI2002Aachen,Germany,September16–20,
2023. 2002Proceedings25. Springer,2002,pp.18–32.
[49] P.P.Ray,“Chatgpt:Acomprehensivereviewonbackground,applications, [55] Sonar,“Sonarqube9.8,”https://docs.sonarqube.org/9.8/user-guide/rules/
key challenges, bias, ethics, limitations and future scope,” Internet of overview/,2023.
ThingsandCyber-PhysicalSystems,2023.
[56] V. Lenarduzzi, F. Lomio, H. Huttunen, and D. Taibi, “Are sonarqube
[50] Q.Lyu,J.Tan,M.E.Zapadka,J.Ponnatapuram,C.Niu,G.Wang,and
rulesinducingbugs?”in2020IEEE27thInternationalConferenceon
C.T.Whitlow,“Translatingradiologyreportsintoplainlanguageusing
SoftwareAnalysis,EvolutionandReengineering(SANER). IEEE,2020,
chatgptandgpt-4withpromptlearning:Promisingresults,limitations,
pp.501–511.
andpotential,”arXivpreprintarXiv:2303.09038,2023.
[57] D.Marcilio,R.Bonifa´cio,E.Monteiro,E.Canedo,W.Luz,andG.Pinto,
[51] M.V.Reiss,“Testingthereliabilityofchatgptfortextannotationand
“Arestaticanalysisviolationsreallyfixed?acloserlookatrealisticusage
classification:Acautionaryremark,”arXivpreprintarXiv:2304.11085,
of sonarqube,” in 2019 IEEE/ACM 27th International Conference on
2023.
ProgramComprehension(ICPC). IEEE,2019,pp.209–219.
[52] I.Sutskever,O.Vinyals,andQ.V.Le,“Sequencetosequencelearning
withneuralnetworks,”Advancesinneuralinformationprocessingsystems, [58] A.Ziegler,E.Kalliamvakou,X.A.Li,A.Rice,D.Rifkin,S.Simister,
vol.27,2014. G.Sittampalam,andE.Aftandilian,“Productivityassessmentofneural
[53] D.Guo,D.Tang,N.Duan,M.Zhou,andJ.Yin,“Couplingretrievaland codecompletion,”inProceedingsofthe6thACMSIGPLANInternational
meta-learningforcontext-dependentsemanticparsing,”arXivpreprint SymposiumonMachineProgramming,2022,pp.21–29.
arXiv:1906.07108,2019. [59] S.Lukasczyk,F.Kroiß,andG.Fraser,“Anempiricalstudyofautomated
[54] R. Zens, F. J. Och, and H. Ney, “Phrase-based statistical machine unittestgenerationforpython,”EmpiricalSoftwareEngineering,vol.28,
translation,”inKI2002:AdvancesinArtificialIntelligence:25thAnnual no.2,p.36,2023.
12