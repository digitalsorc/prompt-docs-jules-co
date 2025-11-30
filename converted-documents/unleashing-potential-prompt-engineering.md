---
title: "Unleashing Potential Prompt Engineering"
original_file: "./Unleashing_Potential_Prompt_Engineering.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["prompt", "model", "models", "language", "prompts", "engineering", "learning", "llms", "data", "these"]
summary: "<!-- Page 1 -->

Unleashing the potential of prompt engineering: a
comprehensive review
Banghao Chen1, Zhaofeng Zhang1, Nicolas Langren´e1*,

### Shengxin Zhu2,1*

1Guangdong Provincial Key Laboratory of Interdisciplinary Research and
Application for Data Science, BNU-HKBU United International College,
Zhuhai 519087, China. 2Research Center for Mathematics, Beijing Normal University, No.18,
Jingfeng Road, Zhuhai 519087, Guangdong, China. E-mail(s): nicolaslangrene@uic.edu.cn;

### Shengxin.Zhu@b"
related_documents: []
---

# Unleashing Potential Prompt Engineering

<!-- Page 1 -->

Unleashing the potential of prompt engineering: a
comprehensive review
Banghao Chen1, Zhaofeng Zhang1, Nicolas Langren´e1*,

### Shengxin Zhu2,1*

1Guangdong Provincial Key Laboratory of Interdisciplinary Research and
Application for Data Science, BNU-HKBU United International College,
Zhuhai 519087, China.
2Research Center for Mathematics, Beijing Normal University, No.18,
Jingfeng Road, Zhuhai 519087, Guangdong, China.
*Corresponding author(s). E-mail(s): nicolaslangrene@uic.edu.cn;

### Shengxin.Zhu@bnu.edu.cn;

Contributing authors: q030026007@mail.uic.edu.cn;
q030018107@mail.uic.edu.cn;

### Abstract

Thiscomprehensivereviewexploresthetransformativepotentialofpromptengineering within the realm of large language models (LLMs) and multimodal
language models (MMLMs). The development of AI, from its inception in the
1950s to the emergence of neural networks and deep learning architectures, has
culminatedinsophisticatedLLMssuchasGPT-4andBERT,aswellasMMLMs
likeDALL-EandCLIP.Thesemodelshaverevolutionizedtasksindiversefields
such as workplace automation, healthcare, and education. Prompt engineering
emerges as a crucial technique to maximize the utility and accuracy of these
models.Thispaperdelvesintobothfoundationalandadvancedmethodologiesof
promptengineering,includingtechniqueslikeChainofThought,Self-consistency,
and Generated Knowledge, which significantly enhance model performance.
Additionally,itexaminestheintegrationofmultimodaldatathroughinnovative
approachessuchasMulti-modalPromptLearning(MaPLe),ConditionalPrompt
Learning, and Context Optimization. Critical to this discussion is the aspect
of AI security, particularly adversarial attacks that exploit vulnerabilities in
promptengineering.Strategiestomitigatetheserisksandenhancemodelrobustness are thoroughly reviewed. The evaluation of prompt methods is addressed
through both subjective and objective metrics, ensuring a robust analysis of
their efficacy. This review underscores the pivotal role of prompt engineering in
advancing AI capabilities, providing a structured framework for future research
and application.
Keywords:Promptengineering,LLM,Multimodal,AIGC,Adversarialattacks,

### AIagent,GPT-4

1 Introduction
The development of Artificial Intelligence (AI) has been marked by significant milestones that have progressively shaped the interaction between humans and machines.
1
4202
yaM
82
]LC.sc[
3v53741.0132:viXra

<!-- Page 2 -->

TheearlydaysofAIresearchinthe1950sfocusedonfoundationaltheoriesandsimple
problem-solvingprocesses[1].Ascomputationalpowerandalgorithmicsophistication
grew, the 1980s and 1990s saw the emergence of neural networks and the resurgence
of machine learning, laying the groundwork for more complex systems [2].
The introduction of deep learning architectures in the early 2000s, particularly
withthedevelopmentofAlexNetin2012,markedapivotalshifttowardsmodelscapableofhandlingandinterpretingvastamountsofdata[3].Thisperiodsetthestagefor
the evolution of language models, culminating in the creation of transformative modelslikeGPT(GenerativePre-trainedTransformer)andBERT(BidirectionalEncoder
Representations from Transformers), which fundamentally changed how machines
understand and generate human language [4].
In recent years, a significant milestone in artificial intelligence research has been
the progression of natural language processing capabilities, primarily attributed to
large language models (LLMs). Many popular models, rooted in the transformer
architecture [5], undergo training on extensive datasets derived from web-based text.
Central to their design is a self-supervised learning objective, which focuses on predicting subsequent words in incomplete sentences. Those models are called Artificial
Intelligence-Generated Content (AIGC), and their ability to generate coherent and
contextually relevant responses is a result of this training process, where they learn
to associate words and phrases with their typical contexts.
LLMs operate by encoding the input text into a high-dimensional vector space,
where semantic relationships between words and phrases are preserved. The model
then decodes this representation to generate a response, guided by the learned statistical patterns [6]. The quality of the response can be influenced by various factors,
including the prompt provided to the model, the model’s hyperparameters, and the
diversity of the training data.
These models, text-only LLMs such as GPT-3 [7], along with many others (e.g.,
Google’s BARD [8], Anthropic’s Claude2 [9], and Meta’s open-source model LLaMA-
2 [10]), have revolutionized tasks ranging from information extraction to the creation
of engaging content [11]. Parallelly, the development of Multimodal Language Models (MMLMs) has introduced the ability to process and generate not just text, but
also images, audio, and other forms of data. These models integrate multiple data
modalities into a single framework, enabling more comprehensive understanding and
interaction capabilities. Examples of such models include the DALL-E series [12–14],
whichcangenerateimagesfromtextualdescriptions,andCLIP,whichcanunderstand
and relate text and image data in a unified manner [15]. More powerful models such
asGPT-4[16],Google’sGemini-Ultra[17],Meta’sLLaMA-3[18,19],andAnthropic’s
Claude3 [20] excel in multimodal tasks involving text generation and understanding,
integratingnaturallanguageprocessingwithvariousformsofdatatoperformdiverse
and complex language-based tasks. The types of data that Multimodal Language
Models (MMLMs) are capable of processing are illustrated in Figure 1. This diagram
demonstrates that MMLMs can integrate and process data from various modalities, including text, vision, and audio information. This capability allows MMLMs
to excel in tasks involving multimodal inputs, showcasing their flexibility and effectiveness. While numerous advanced models are currently capable of processing audio,
the majority of accessible API interfaces remain focused on text and vision modalities. With the gradual introduction of audio API interfaces, we can expect a broad
and profound expansion of research in this modality [21]. In conclusion, the evolution of LLMs and MMLMs reflects significant strides in AI research, characterized by
increasing model complexity, enhanced training methodologies, and broader applicationpotentials.Theseadvancementsunderscorethecriticalroleofpromptengineering
in maximizing the utility and accuracy of these models, ensuring that they can effectively cater to diverse and dynamic user needs. Since MMLMs are a subset of LMs,
references to LMs in the following content inherently include both MMLMs and
text-only LLMs.
RelatedtoAIsystems,theapplicationofLLMsintheworkplacehasthepotential
toautomateroutinetasks,suchasdataanalysis[22]andtextgeneration[23],thereby
2

<!-- Page 3 -->


### Text

Multimodal Vision

### Audio


### Fig. 1 DataModalitiesofMMLMs

freeinguptimeforemployeestofocusonmorecomplexandrewardingtasks[24].Furthermore, LLMs have the potential to revolutionize the healthcare sector by assisting
inthediagnosisandtreatmentofdiseases.Indeed,byanalyzingvastamountsofmedical literature, these models can provide doctors with insights into rare conditions,
suggest potential treatment pathways, and even predict patient outcomes [25]. In the
realm of education, LLMs can serve as advanced tutoring systems, and promote the
qualityofteachingandlearning[26].ThoseAItoolscananalyzeastudent’sresponse,
identify areas of improvement, and provide constructive feedback in a coherent and
formal manner.
In real applications, the prompt is the input of the model, and its engineering
can result in significant output difference [27]. Modifying the structure (e.g., altering
length, arrangement of instances) and the content (e.g., phrasing, choice of illustrations, directives) can exert a notable influence on the output generated by the model
[28]. Studies show that both the phrasing and the sequence of examples incorporated
within a prompt have been observed to exert a substantial influence on the model’s
behavior [28, 29].
Prompt engineering, evolving alongside LLMs, has transitioned from a fundamental practice into a well-structured research domain. As illustrated in Figure 2, the
historical progression of prompt engineering showcases significant milestones from
the early days of structured inputs to the advanced methodologies developed in
recent years. This figure provides a visual timeline of the evolution from basic structured inputs in the 1950s to the sophisticated techniques such as chain-of-thought
prompting [30] and self-consistency prompting [31] that define the field today. In this
paper, we primarily concentrate on the techniques emerging from the period of rapid
development subsequent to 2017.
Prompt engineering refers to the systematic design and optimization of input
prompts to guide the responses of LLMs, ensuring accuracy, relevance, and coherence in the generated output. This process is crucial in harnessing the full potential
of these models, making them more accessible and applicable across diverse domains.
Contemporary prompt engineering encompasses a spectrum of techniques, ranging
fromfoundationalapproachessuchasrole-prompting[32]tomoresophisticatedmethods such as “chain of thought” prompting [30]. The domain remains dynamic, with
emergent research continually unveiling novel techniques and applications in prompt
engineering. The importance of prompt engineering is accentuated by its ability to
guide model responses, thereby amplifying the versatility and relevance of LLMs in
varioussectors.Importantly,awell-constructedpromptcancounteractchallengessuch
as machine hallucinations, as highlighted in studies by [33] and [34]. The influence of
3

<!-- Page 4 -->


### Early Days of Structured Input (1950s-1980s)

Foundations of Artificial Intelligence: Initial developments in AI were dependent on structured, rule-based inputs, wherein the
accuracy and pertinence of these inputs had a direct impact on system performance. While this did not constitute prompt
engineering in the contemporary sense, it underscored the critical importance of formulating well-defined queries for AI systems.

### The Emergence of Machine Learning (1980s-1990s)

Evolution of Feature Engineering: Concurrent with the advancement of statistical machine learning, emphasis increasingly shifted
towards the manner in which data was presented to models. Effective feature engineering became paramount, as it significantly
influenced a model's ability to learn and extract meaningful patterns from the training data.
Recurrent Neural Networks (RNNs) and Their Significance in Sequential

### Data Processing (Late 1990s-2000s)

During the late 1990s, the adoption of Recurrent Neural Networks (RNNs) underscored the critical importance of sequential data
structures in processing inputs such as text and speech. This era initiated a paradigm shift towards conceptualizing prompts as
strategic guides to shape the responses of models over data sequences.

### Deep Learning and Complex Inputs (2006-2010)

2006: The introduction of deep learning concepts marked a significant advancement in artificial intelligence. The realization that
networks with greater depth could extract intricate patterns directly from raw data led to a renewed focus on optimizing how data is
structured for input, thereby enhancing the networks' learning capabilities.
2010: The deployment of deep neural networks in handling more sophisticated tasks involving unstructured text and image data
highlighted the importance of intelligent input configuration. This period saw the nascent development of what would later be
recognized as prompt engineering, aiming to refine how data inputs could more effectively guide neural network responses.

### Attention Mechanisms and Contextual Inputs (2015-2017)

2015: The development of attention mechanisms, which later became fundamental in models such as Transformers,
marked a pivotal advance in model architecture. These mechanisms enabled models to selectively concentrate on
various segments of the input data, thereby enhancing their ability to understand context. This innovation
underscored the increased importance of carefully designing input structures to maximize the effectiveness of the
attention-driven processing capabilities.
Rise of Transformers and Explicit Prompt Engineering (2017-Present)
2017: The debut of the Transformer model revolutionized input handling in machine learning. This architecture demonstrated that
prompts could effectively condition models, directly influencing their outputs, thereby highlighting the strategic use of input design.
2018: The emergence of models like BERT and GPT extended the use of prompts beyond specific tasks to a broad range of general
applications. This shift turned prompt engineering into an essential competency for leveraging the full potential of these advanced
models.
2020: With the release of GPT-3, the capacity for generating contextually appropriate and nuanced responses based solely on prompts,
without requiring additional training, emphasized the critical importance of meticulous prompt design in achieving desired outcomes.

### Advanced Prompt Engineering Techniques (2020-Present)

2020 onwards: Development of techniques such as prompt programming, chain-of-thought prompting, and systematic prompt
design, which are seen as ways to control and guide AI behavior more effectively.

### Fig. 2 HistoryoftheDevelopmentinPromptEngineering

prompt engineering extends to numerous disciplines. For instance, it has facilitated
thecreationofrobustfeatureextractorsusingLLMs,therebyimprovingtheirefficacy
in tasks such as defect detection and classification [35].
Inthiscomprehensivereview,wedelveintothetransformativepotentialofprompt
engineering within the realm of large language models (LLMs). The structure of the
paper is organized as follows: We begin with Section 2, which explores the foundationalmethodsofpromptengineering,emphasizingtheimportanceofclearandprecise
instructions, role-prompting, and iterative attempts to optimize outputs. In Section
3, advanced methodologies such as Chain of Thought, Self-consistency, and Generated Knowledge are introduced to guide models in generating high-quality content.
We also discuss methodologies specific to multimodal models in Section 4, including
Multi-modal Prompt Learning (MaPLe), Conditional Prompt Learning, and Context
Optimization, which enhance the performance of vision-language models. The efficacy of various prompt methods is assessed through both subjective and objective
evaluations, ensuring a robust analysis of their effectiveness (Section 5). The applications of prompt engineering extend across diverse fields such as education, content
creation, computer programming, and reasoning tasks, highlighting its broad impact
(Section 6). In Section 7, we address the security implications of prompt engineering, identifying common vulnerabilities in LLMs and proposing strategies to enhance
security through adversarial training and robust prompt design. Finally, in section 8,
we explore prospective methodologies, emphasizing the importance of understanding
AImodelstructuresandthepotentialofAIagentsinadvancingAI-generatedcontent
4

<!-- Page 5 -->

tools. This structured framework provides a comprehensive overview of the pivotal
role of prompt engineering in advancing AI capabilities and guiding future research
and applications.
2 Basics of prompt engineering
By incorporating just a few key elements, one can craft a basic prompt that enables
LLMs to produce high-quality answers. In this section, we discuss some essential
components of a well-made prompt.
2.1 Model introduction: GPT-4
All of the output in the following sections are generated by GPT-4, developed by
OpenAI[16].VastamountsoftextdatahavebeenusedtotrainGPT-4,whosenumber
of parameters has been estimated to be several orders of magnitude larger than the
175billionparametersthathadbeenusedfortheearlierGPT-3[7].Thearchitectural
foundation of the model rests on transformers [5], which essentially are attention
mechanisms that assign varying weights to input data based on the context. Similar
to GPT-3, GPT-4 was also fine-tuned to follow a broad class of written instructions
byreinforcementlearningfromhumanfeedback(RLHF)[36,37],whichisatechnique
that uses human preferences as a reward signal to fine-tune models.
WhenGPT-4receivesaninputprompt,theinputtextwillbefirstlyconvertedinto
tokens that the model can interpret and process. These tokens are then managed by
transformerlayers,whichcapturetheirrelationshipsandcontext.Withintheselayers,
attention mechanisms distribute different weights to tokens based on their relevance
andcontext.Afterattentionprocessing,themodelformsitsinternalrenditionsofthe
input data, known as intermediate representations. These representations are then
decoded back into human-readable text [38].
A significant aspect of this process is the randomness function [39]. This function
is influenced by two primary parameters, temperature and top-k sampling. The first
one, temperature [40] balances the randomness and determinism in the output. A
higher temperature value results in more random outputs, while a lower value makes
theoutputmoredeterministic.Thesecondone,top-ksampling[41],limitsthemodel’s
choices to the top k most probable tokens during each step of output generation. The
final stage of this process is the output generation, where the model crafts the final
text.
2.2 Giving instructions
The method of giving instructions, also considered as re-reading [42], refers to the
heuristics of human reading strategy. It has been observed that the output generated by GPT-4, introduced in Section 2.1, tends to be excessively general when
provided with fundamental instructions devoid of any supplementary description
[43, 44]. An example prompt is shown in Figure 3. When the model is prompted with
basic instruction, it faces a plethora of options, which makes the result quite broad.
Hence, a comprehensive description is imperative to elicit more precise and relevant
outputs [45].
2.3 Be clear and precise
The second basic prompt method is “to be clear and precise”. This involves formulating prompts that are unambiguous and specific, which can guide the model toward
generating the desired output.
Most LLM architectures are derived from an extensive array of textual data. It
can be conceptualized as a combination of insights from a myriad of authors. When
presented with a broad or undetailed prompt, its output predominantly exhibits a
generic nature, which, while being applicable across a range of contexts, may not be
optimalforanyspecificapplication.Incontrast,adetailedandprecisepromptenables
5

<!-- Page 6 -->


### Model input

I want to understand some cutting-edge aspects of technology.

### Model output


### Here are some of the key areas:


## Artificial intelligence and machine learning: These technologies are becoming

increasinglysophisticated,withadvancementsinareassuchasnaturallanguageprocessing(likethetechnologyyou’reinteractingwithrightnow),computervision,and
reinforcement learning. Techniques such as transfer learning and federated learning
arebeingusedtomakemachinelearningmodelsmoreefficientandlessdata-hungry.

### Quantumcomputing:Quantumcomputersusetheprinciplesofquantummechanicstoprocessinformation.Theyholdthepotentialtosolvecertaintypesofproblems

much more efficiently than classical computers. Companies like Google, IBM, and
many startups are investing heavily in this area.
3.5Gandbeyond:5Gwirelesstechnologybeganwidespreaddeploymentin2020and
2021, bringing faster speeds, lower latency, and the ability to connect more devices
simultaneously. Research is also being done on 6G, which is expected to integrate
evenmoredeeplywithAIandpotentiallybringaboutmoretransformativechanges.

## Biotechnology: ...

Fig. 3 Giving instructions without extra description.
the model to generate content that is more aligned with the unique requirements of
the given scenario, as it reduces the model’s uncertainty and guides it toward the
correct response.
For instance, as shown in Figure 4, instead of asking a vague requirement such
as “I want to understand the cutting edge of technology.”, a more precise prompt
would be “I want to understand the cutting edge of technology, specifically related to
artificial intelligence and machine learning...”.

### Model input

I want to understand the cutting edge of technology, specifically related to artificial
intelligence and machine learning. Recently, artificial intelligence has become
extremely popular, especially the large language models which have amazed me.
Please analyze the possible reasons behind the rapid advancement of this
technology from at least three perspectives.

### Model output

Absolutely, the rise of AI and machine learning, especially with regard to large language models like GPT-4, can be seen as a convergence of several key factors. I’ll
analyzethisfromthreeperspectives:technologicaladvancements,availabilityofdata,
and socio-economic demand.

## Technological advancements: The growth of AI and machine learning models has

beenfacilitatedbyseveraltechnologicalinnovations.Forstarters,we’veseenincredibleimprovementsincomputationalpower,particularlyinGraphicsProcessingUnits
(GPUs) and now even more specialized AI chips. These advances have made it ...

## Availability of data: ...


## Socio-economic demand: ...

Fig. 4 A clearer and more precise prompt.
2.4 Role-prompting
Role-prompting is another fundamental method in prompt engineering. It involves
givingthemodelaspecificroletoplay,suchasahelpfulassistantoraknowledgeable
6

<!-- Page 7 -->

expert[46].Thismethodcanbeparticularlyeffectiveinguidingthemodel’sresponses
and ensuring that they align with the desired output. For instance, if the model is
promptedtoactasahistorian,itismorelikelytoprovideadetailedandcontextually
accurate response when asked about a historical event [47]. Another brief example is
shown in Figure 5.

### Model output

A role prompt Here are five basic methods to
quicklygetstartedwithlargelan-
You are an expert in artificial
guage models:
intelligence specializing in large

## Experiment with web-based

language models...
interfaces:
...
Fig. 5 Role prompting example.
2.5 Use of triple quotes to separate
Inpromptengineering,theuseoftriplequotesisatechniqueusedtoseparatedifferent
parts of a prompt or to encapsulate multi-line strings. This technique is particularly useful when dealing with complex prompts that include multiple components
or when the prompt itself contains quotes, which makes the model understand one’s
instructions better [48].
2.6 Try several times
Due to the non-deterministic nature of LLMs, it is often beneficial to try several
times when generating responses. This technique, often referred to as “resampling”,
involves running the model multiple times with the same prompt and selecting the
best output. This approach can help overcome the inherent variability in the model’s
responses and increase the chances of obtaining a high-quality output [40].
2.7 One-shot or few-shot prompting
One-shot and few-shot prompting are two important techniques in prompt engineering. One-shot prompting refers to the method where the model is given a single
example to learn from, while few-shot [49] prompting provides the model with multipleexamples[50].Thechoicebetweenone-shotandfew-shotpromptingoftendepends
onthecomplexityofthetaskandthecapabilityofthemodel.Forinstance,forsimple
tasks or highly capable models, one-shot prompting might be sufficient. An example
is shown in Figure 6. However, for more complex tasks or less capable models, fewshot prompting can provide additional context and guidance, thereby improving the
model’s performance.
However,asstatedin[51],“examplesdon’talwayshelp”.[51]investigatedtheintricacies of how large generative language models, such as GPT-3, respond to prompts.
One of the significant findings from this paper is that zero-shot prompts can, in certain scenarios, outperform few-shot prompts. This suggests that the role of few-shot
examplesmightnotbeasmuchaboutteachingthemodelanewtask(meta-learning)
but rather guiding it to recall a task it has already learned. This insight is crucial
as it challenges the conventional wisdom that more examples always lead to better
performance [7]. In the context of one-shot or few-shot prompting, it is essential to
understand that while examples can guide the model, they do not always enhance its
performance. Sometimes, a well-crafted zero-shot prompt can be more effective than
providing multiple examples [52].
7

<!-- Page 8 -->

Standard Prompt

### Model input


### One-shot Prompt

Q: Yes or no: would a pear sink
Model input
in water?
Q: Yes or no: is it common to see
frost during some college
commencements?
Model output A: The answer is yes.
Q: Yes or no: would a pear sink
A: Yes, a pear would typically
in water?
float in water, not sink. The reason for this is that pears, like
many fruits, are composed primarilyofwaterandhaveadensity Model output
that is less than that of water. ✓
Objects that are less dense than
A: The answer is No.
water will float when placed in
×
water.
Fig. 6 Comparison of standard prompt and one-shot prompt.
2.8 LLM settings: temperature and top-p
The settings of LLMs, such as the temperature and top-p, play a crucial role in the
generation of responses. The temperature parameter controls the randomness of the
generated output: a lower temperature leads to more deterministic outputs [53, 54].
The top-p parameter, on the other hand, controls the nucleus sampling [40], which is
a method to add randomness to the model’s output [55]. Adjusting these parameters
cansignificantlyaffectthequalityanddiversityofthemodel’sresponses,makingthem
essentialtoolsinpromptengineering.However,ithasbeennotedthatcertainmodels,
exemplified by ChatGPT, do not permit the configuration of these hyperparameters,
barring instances where the Application Programming Interface (API) is employed.
3 Advanced methodologies
The foundational methods from the previous section can help us produce satisfactory
outputs. However, experiments indicate that when using LLMs for complex tasks
such as analysis or reasoning, the accuracy of the model’s outputs still has room for
improvement.Inthissection,wewillfurtherintroduceadvancedtechniquesinprompt
engineeringtoguidethemodelingeneratingmorespecific,accurate,andhigh-quality
content.
3.1 Chain of thought
Theconceptof“ChainofThought”(CoT)prompting[30]inLLMsisarelativelynew
development in the field of AI, and it has been shown to significantly improve the
accuracy of LLMs on various logical reasoning tasks [56–58]. CoT prompting involves
providing intermediate reasoning steps to guide the model’s responses, which can be
facilitated through simple prompts such as “Let’s think step by step” or through a
series of manual demonstrations, each composed of a question and a reasoning chain
that leads to an answer [59, 60]. It also provides a clear structure for the model’s
reasoning process, making it easier for users to understand how the model arrived at
its conclusions.
[61] illustrates the application of CoT prompting to medical reasoning, showing that it can effectively elicit valid intermediate reasoning steps from LLMs. [62]
introducestheconceptofSelf-EducationviaChain-of-ThoughtReasoning(SECToR),
and argues that, in the spirit of reinforcement learning, LLMs can successfully teach
8

<!-- Page 9 -->

themselves new skills by chain-of-thought reasoning. In another study, [63] used CoT
prompting to train verifiers to solve math word problems, demonstrating the technique’s potential in educational applications. [64] proposed a multimodal version of
CoT,calledMultimodal-CoT,tohandlemorecomplex,multimodaltasksbeyondsimpletext-basedtasks,suchasvisualtasks,furtherexpandingthepotentialapplications
of CoT.
3.1.1 Zero-shot chain of thought
The concept of “Zero-Shot Chain of Thought” (Zero-shot-CoT) prompting is an
advanced iteration of the CoT prompting mechanism, where the “zero-shot” aspect
implies that the model is capable of performing some reasoning without having seen
any examples of the task during training.
Intheirresearch,[65]discoveredthattheaugmentationofquerieswiththephrase
“Let’s think step by step” facilitated the generation of a sequential reasoning chain
by LLMs. This reasoning chain subsequently proved instrumental in deriving more
precise answers. This technique is based on the idea that the model, much like a
human,canbenefitfromhavingmoredetailedandlogicalstepstoprocesstheprompt
and generate a response.
For instance, the standard prompt is illustrated in Figure 7, while the appended
phrase, “Let’s think step by step”, is depicted in Figure 8. Observations indicate that
the incorporation of “Let’s think step by step” enhances the logical coherence and
comprehensiveness of the model’s response.

### Model input

Imagine an infinitely wide entrance, which is more likely to pass through it, a
military tank or a car?

### Model output

Givenan“infinitelywideentrance”,bothamilitarytankandacarcanpassthrough
it without any constraints due to width. Therefore, neither is more likely than the
other based on width alone. Both can pass through with equal likelihood.
However, if other factors such as ground conditions, accessibility, purpose, or authorizationcomeintoplay,thelikelihoodmightchange.Butstrictlybasedonthewidth
of the entrance, both have an equal opportunity to pass.
Fig. 7 Standard prompt.
3.1.2 Golden chain of thought
[66] introduced the “golden chain of thought”, providing an innovative approach to
generatingresponsestoinstruction-basedqueries.Thismethodologyleveragesasetof
“ground-truth chain-of-thought” solutions incorporated within the prompt, considerablysimplifyingthetaskforthemodelasitcircumventsthenecessityforindependent
CoT generation. Concurrently, a novel benchmark comprising detective puzzles has
been designed, to assess the abductive reasoning capacities of LLMs, which is also
consideredanevaluationofthegoldenCoT.Finally,accordingto[66]’sexperiment,in
the context of the golden CoT, GPT-4 exhibits commendable performance, boasting
an 83% solve rate in contrast to the 38% solve rate of the standard CoT.
However,thecharacteristicsoftheGoldenCoTrequiringthe“ground-truthchainof-thought solutions” as an integral part of the prompt also signifies that the Golden
CoT’s contribution to solving such problems is limited, despite its high solve rate of
83%.
9

<!-- Page 10 -->


### Model input

Imagine an infinitely wide entrance, which is more likely to pass through it, a
military tank or a car? Let’s think step by step.

### Model output

Givenaninfinitelywideentrance,bothamilitarytankandacarcouldpassthrough
without any issues related to the width. However, there are still several factors that
could influence which is more likely to pass through:

## Groundsurface:tanksaredesignedtohandleroughterrainsthatcarsmaystruggle

with.Ifthegroundleadingtoandfromtheentranceistooruggedorsteepforacar,
the tank would be more likely to pass through.

## Weight restrictions: if the entrance has a load limit due to the materials used in

its construction, the car, being lighter, could be more likely to pass through. The
average car weighs around 1.5 tons, while a military tank can weigh anywhere from
60 to 70 tons.

## Heightclearance:iftheentranceisinfinitelywidebutnotinfinitelytall,theheight

of the vehicle matters. The average height of a car is around 1.5 meters, while tanks
can be around 2.4 meters. If the entrance is shorter than around 2.4 meters, a car
would be more likely to pass through.

## Regulations and permissions:

...
In conclusion, without specific information about the conditions at the entrance, we
wouldassumethatacarismorelikelytopassthrough,simplybecausecarsaremore
common, more likely to meet potential height and weight restrictions and face fewer
regulatory barriers.
Fig. 8 Adding “Let’s think step by step”.
3.2 Self-consistency
In the assessment of INSTRUCTGPT [67] and GPT-3 [7] on a new synthetic QA
dataset called PRONTOQA, for Proof and Ontology-Generated Question-Answering
[68, 69], it was observed that although the most extensive model exhibited capability
inreasoningtasks,itencounteredchallengesinproofplanningandtheselectionofthe
appropriate proof step amidst multiple options, which caused accuracy uncertainties
[68].Self-consistencyinLLMsisanadvancedpromptingtechniquethataimstoensure
the model’s responses are consistent with each other [30, 31], which greatly increases
the odds of obtaining highly accurate results. The principle of self-consistency in
language models posits that for a complex reasoning problem, there can be multiple
reasoning paths leading to the correct answer. In this approach, a language model
generates a diverse set of reasoning paths for the same problem. The most accurate
andconsistentansweristhendeterminedbyevaluatingandmarginalizingacrossthese
varied paths, ensuring that the final answer reflects the convergence of multiple lines
of thought.
Theself-consistencymethodcontainsthreesteps.Firstly,promptalanguagemodel
using CoT prompting, then replace the “greedy decode” (1-Best) [39, 70] in CoT
prompting by sampling from the language model’s decoder to generate a diverse set
of reasoning paths, and finally, marginalize out the reasoning paths and aggregate by
choosing the most consistent answer in the final answer set.
It is noteworthy that self-consistency can be harmoniously integrated with most
sampling algorithms, including but not limited to, temperature sampling [53, 54],
top-ksampling[39,71,72],andnucleussampling[40].Nevertheless,suchanoperation
may necessitate the invocation of the model’s Application Programming Interface
(API) to fine-tune these hyperparameters. In light of this, an alternative approach
couldbetoallowthemodeltogenerateresultsemployingdiversereasoningpaths,and
thengenerateadiversesetofcandidatereasoningpaths.Theresponsedemonstrating
thehighestdegreeofconsistencyacrossthevariousreasoningtrajectoriesisthenmore
inclined to represent the accurate solution [73].
10

<!-- Page 11 -->

Studies have shown that self-consistency enhances outcomes in arithmetic, commonsense, and symbolic reasoning tasks [6, 74]. Furthermore, in practice, selfconsistency can be combined with other techniques to further enhance the model’s
performance. For example, a study found that combining self-consistency with a
discriminator-guidedmulti-stepreasoningapproachsignificantlyimprovedthemodel’s
reasoning capabilities [75].
3.3 Generated knowledge
The “generated knowledge” [76] approach in prompt engineering is a technique that
leveragestheabilityofLLMstogeneratepotentiallyusefulinformationaboutagiven
question or prompt before generating a final response. This method is particularly
effective in tasks that require commonsense reasoning, as it allows the model to generate and utilize additional context that may not be explicitly present in the initial
prompt.
As exemplified in Figure 7, when posing the query to the model, “Imagine an
infinitely wide entrance, which is more likely to pass through it, a military tank or a
car?”, standard prompts predominantly yield responses that neglect to factor in the
“entrance height”. Conversely, as delineated in Figure 9 and Figure 10, prompting
the model to first generate pertinent information and subsequently utilizing generated information in the query leads to outputs with augmented logical coherence and
comprehensiveness.Notably,thisapproachstimulatesthemodeltoaccountforsalient
factors such as “entrance height”.

### Model input

Generate two key analyses related to detailed size data on military tanks and cars,
and then generate three key influencing factors regarding whether an object can
pass through an infinitely wide entrance.

### Model output


### Detailed size analysis: military tanks vs. cars


## Dimensionsandweight:-Militarytanks:typically,mainbattletanks(liketheM1

Abrams or T-90) have widths ranging from 10 to 13 feet, lengths from 25 to 35 feet
(includingthemaingun),andweightsfrom60to70tons.-Cars:mostconsumercars
haveawidthofabout6to8feet,alengthof12to20feet,andweighbetween1to3
tons.SomelargeSUVsandtruckscanexceedthesefiguresbutarestillsubstantially
smaller and lighter than tanks.

## Maneuverability & design: - Military tanks: tanks are designed to traverse rough

terrains and have tracks that distribute weight and prevent the vehicle from getting
easily stuck in muddy or uneven ground. However, their sheer weight and size limit
their maneuverability in urban or congested settings. - Cars: designed for paved
roads, cars are generally more agile and can navigate tight spaces more efficiently
than tanks. Their design emphasizes aerodynamics and comfort, unlike tanks that
prioritize armor and firepower.
Three key influencing factors on whether an object can pass through an infinitely
wide entrance:

## Height of the object: the height is critical. An infinitely wide entrance does not

give information about its height. If the object is taller than the entrance, it won’t
pass through.

## Structuralintegrity:dependingonthematerialanddesignofanobject,squeezingor

forcingitthroughanentrancecouldcompromiseitsstructuralintegrity.Forinstance,
certain tanks have reactive armor or sensitive equipment that may be damaged if
scraped or bumped forcefully.

## Ground clearance and maneuverability: ...

Fig. 9 Generating knowledge (Step1).
11

<!-- Page 12 -->

Model input
“““
Detailed size analysis: military tanks vs. cars

## Dimensions and weight:

- Military tanks: typically, main battle tanks (like the M1 Abrams or T-90) have
widths ranging from 10 to 13 feet, lengths from 25 to 35 feet (including the main
gun), and weights from 60 to 70 tons.
- Cars: most consumer cars have a width of about 6 to 8 feet, a length of 12 to 20
feet, and weigh between 1 to 3 tons. Some large SUVs and trucks can exceed these
figures but are still substantially smaller and lighter than tanks.

## Maneuverability & design...

”””
Use the above information to answer the following question: Imagine an infinitely
wide entrance, which is more likely to pass through it, a military tank or a car?

### Model output

Given the information provided about the dimensions, design, and the factors influencing whether an object can pass through an infinitely wide entrance, we can infer
the following:

## Height of the object: the height is not specified for either tanks or cars. However, given that tanks are built for rough terrains and often have a turret and other

equipment on top, they generally have a taller profile compared to most cars. If the
entrance had a restrictive height, cars would generally have an advantage here.

## Structural integrity: ...


## Ground clearance and maneuverability:

...
Conclusion: If the entrance height is not restrictive and the surface is rough, a militarytankwouldbemorelikelytopassthroughitwithoutissues.Ontheotherhand,
if the entrance is low-height or has tight squeezes that could compromise the structural integrity of larger, robust vehicles, a car might be at an advantage.
However,givennoheightconstraintsandonlythefactorofwidth(sinceitis“infinitely
wide”),bothamilitarytankandacarwouldeasilypassthroughit.Insuchascenario,
thedistinguishingfactorwouldbetheterrainoftheentrance.Ifitisroughoruneven,
the tank has the advantage. If it is smooth, both would pass with relative ease.
Fig. 10 Combining the generated knowledge with the question (Step2).
3.4 Least-to-most prompting
The concept of “least to most prompting” [77] is an advanced method that involves
startingwithaminimalpromptandgraduallyincreasingitscomplexitytoelicitmore
sophisticated responses from the language model. The foundational premise of this
approach is the decomposition of intricate problems into a succession of more rudimentary subproblems, which are then sequentially addressed. The resolution of each
subproblemisexpeditedbyleveragingsolutionsderivedfromantecedentsubproblems.
Uponrigorousexperimentationindomainsincludingsymbolicmanipulation,compositionalgeneralization,andmathematicalreasoning,findingsfrom[77]substantiate
that the least-to-most prompting paradigm exhibits the capacity to generalize across
challenges of greater complexity than those initially presented in the prompts. They
found that LLMs seem to respond effectively to this method, demonstrating its
potential for enhancing the reasoning capabilities of these models.
3.5 Tree of thoughts
The “tree of thoughts” (ToT) prompting technique in LLMs is an advanced method
that employs a structured approach to guide LLMs in their reasoning and response
generation processes. It enhances problem-solving by exploring multiple reasoning
paths,termed’thoughts’.Unliketraditionallinearprompts,ToTallowsLLMstoconsider various possible solutions and strategies, including looking ahead, backtracking,
12

<!-- Page 13 -->

and self-evaluation, making it more interactive and adaptable to the complexity of
thetaskathand.Thisapproachfostersmoredynamicanddeliberatedecision-making
in complex problem-solving tasks, moving beyond a rigid, hierarchical prompt structure to a more flexible and adaptive reasoning process [78]. The ToT approach, for
instance,whenappliedtocomplexmathematicalproblem-solving,promptsthemodel
to generate various potential solutions and evaluate them, rather than simply asking
for a solution.
[78] demonstrates that this formulation is more versatile and can handle challenging tasks where standard prompts might fall short. Another research by [79] further
emphasizes the potential of this technique in enhancing the performance of LLMs by
structuring their thought processes.
[8] introduces the “tree-of-thought prompting”, an approach that assimilates the
foundational principles of the ToT frameworks and transforms them into a streamlined prompting methodology. This technique enables LLMs to assess intermediate
cognitiveconstructswithinasingularprompt.AnexemplarToTpromptisdelineated
in Figure 11 [8].

### Tree of thoughts prompting

Imagine three different experts answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realizes they’re wrong at any point then they leave.
The question is...
Fig. 11 A sample ToT prompt.
3.6 Graph of thoughts
Unlike the “chain of thoughts” or “tree of thoughts” paradigms, the “graph of
thoughts” (GoT) framework [80] offers a more intricate method of representing the
informationgeneratedbyLLMs.ThecoreconceptbehindGoTistomodelthisinformation as an arbitrary graph. In this graph, individual units of information, termed
“LLM thoughts”, are represented as vertices. The edges of the graph, on the other
hand, depict the dependencies between these vertices. This unique representation
allows for the combination of arbitrary LLM thoughts, thereby creating a synergistic
effect in the model’s outputs.
In the context of addressing intricate challenges, LLMs utilizing the GoT framework might initially produce several autonomous thoughts or solutions. These
individualinsightscansubsequentlybeinterlinkedbasedontheirpertinenceandinterdependencies,culminatinginadetailedgraph.Thisconstructedgraphpermitsdiverse
traversal methods, ensuring the final solution is both precise and comprehensive,
encompassing various dimensions of the challenge.
The efficacy of the GoT framework is anchored in its adaptability and the profound insights it can yield, particularly for intricate issues necessitating multifaceted
resolutions.Nonetheless,itisimperativetorecognizethatwhileGoTfacilitatesasystematic approach to problem-solving, it also necessitates a profound comprehension
of the subject matter and meticulous prompt design to realize optimal outcomes [81].
3.7 Automatic Reasoning and Tool Usage
Automatic Reasoning and Tool Usage (ART) is an advanced prompting technique
that combines the principles of automatic chain-of-thought (CoT) prompting with
the strategic utilization of external tools. This method aims to enhance the reasoning
capabilities of Large Language Models (LLMs) by guiding them through multi-step
reasoning processes and leveraging specialized tools to achieve more accurate and
relevant outputs.
13

<!-- Page 14 -->

ARTbuildsontheCoTpromptingtechnique,whichencouragesmodelstogenerate
intermediatereasoningstepsbeforearrivingatafinalanswer.InART,thesereasoning
steps are augmented by incorporating external tools such as calculators, databases,
or other software applications. The integration of tools helps LLMs perform tasks
that require precise calculations, access to updated information, or specialized data
processing that the model alone may not handle effectively.
Forexample,apromptdesignedusingARTmightguideanLLMtofirstoutlinethe
stepsrequiredtosolveacomplexmathematicalproblemandthenuseacalculatortool
to perform the necessary calculations. This combination of reasoning and tool usage
ensures that the model’s outputs are both logically coherent and computationally
accurate.
RecentadvancementsinpromptengineeringhavehighlightedthepotentialofART
in improving LLM performance. Studies have demonstrated that ART can help models navigate complex problem spaces more effectively by breaking down tasks into
manageable steps and utilizing appropriate tools at each stage [82]. For instance, the
integration of ART in natural language processing tasks has shown promising results
inareassuchasautomatedcustomerservice,wheremodelsneedtoaccessandprocess
information dynamically [83].
Moreover,ART’sapproachalignswithongoingeffortstodevelopmorerobustand
versatile AI systems capable of handling real-world tasks that demand a combination of cognitive and computational skills. Research by Mercity AI (2024) explores
advanced techniques in ART to achieve better accuracy and reliability in AI applications [84]. These findings underscore the importance of ART in enhancing the
functionality and performance of LLMs, making them more adept at handling a
broader range of tasks.
TheapplicationsandbenefitsofARTaresubstantial.Byleveragingexternaltools,
ART can significantly improve the accuracy of the model’s responses, especially for
tasks that require specific and precise outputs, such as financial calculations or data
analysis.Additionally,ARTexpandstherangeoftasksthatLLMscaneffectivelyhandle by integrating specialized tools. This makes it possible for LLMs to perform more
complex and varied tasks, from technical problem-solving to real-time data retrieval.
Forend-users,ARTcanfacilitatemoreintuitiveandefficientinteractionswithLLMs.
Userscanrelyonthemodeltohandlemultifacetedqueriesthatinvolvemultiplesteps
and require the use of different tools, enhancing the overall user experience.
In conclusion, ART represents a significant advancement in prompt engineering,
combininglogicalreasoningwithpracticaltoolusagetoimprovetheperformanceand
reliabilityofLLMs.Asresearchcontinuestoevolve,theintegrationofARTtechniques
islikelytoplayacrucialroleindevelopingmoresophisticatedandcapableAIsystems.
3.8 Active-Prompt
Active-Prompt is an innovative prompt engineering technique that involves dynamically modulating prompts based on responsive feedback from the model or user
interactions. This approach is designed to enhance the engagement between the user
and the Large Language Model (LLM), ensuring that the prompts are continuously
refined to elicit more accurate and contextually relevant responses.
Active-Promptoperatesontheprincipleofinteractivefeedbackloops.Unlikestatic
prompts, which are predetermined and unchanging, active prompts adapt based on
the responses received from the LLM. This dynamic adjustment allows for a more
iterative and responsive interaction, where the model’s preliminary outputs are used
tofine-tunesubsequentprompts.Thisprocesscaninvolvehumanannotatorsorautomated systems that evaluate the responses and provide feedback to improve prompt
effectiveness [85].
For instance, in a customer service application, an active prompt might initially
query the model about a general issue. Based on the model’s response, the prompt
couldthenbeadjustedtoaskmorespecificquestions,guidingtheconversationtowards
a precise resolution. This method ensures that the interaction remains relevant and
14

<!-- Page 15 -->

progressivelynarrowsdownthepossiblesolutions,enhancingtheoverallaccuracyand
satisfaction of the response.
By continuously refining prompts based on feedback, Active-Prompt can significantly improve the accuracy and relevance of the model’s responses. This is
particularly beneficial in complex or nuanced conversations where initial responses
mayrequirefurtherclarification[86].Active-Promptallowsforahighdegreeofpersonalization in interactions. By adapting prompts to user responses, it can create a more
engaging and tailored experience, which is crucial in applications such as customer
support, personalized learning, and interactive AI companions [87]. For end-users,
Active-Prompt facilitates more intuitive and efficient interactions with LLMs. Users
benefit from a model that appears more responsive and capable of understanding
context, leading to more productive and satisfying interactions [88].
Recent studies and practical applications have demonstrated the efficacy of
Active-Prompt in various domains. Research by Spiceworks (2024) highlights how
Active-Prompt can dynamically adjust to user feedback, improving the overall quality of model interactions in real-time. This approach aligns with the broader trend
towards more interactive and adaptive AI systems, emphasizing the importance of
responsive design in prompt engineering. Moreover, the concept of Active-Prompt
alignswithongoingeffortstodevelopmorehuman-likeconversationalagents.Byintegratingfeedbackloopsandinteractiveadjustments,Active-Promptcontributestothe
creation of AI systems that are not only more accurate but also more engaging and
user-friendly.
Inconclusion,Active-Promptrepresentsasignificantadvancementinpromptengineering, offering a dynamic and responsive approach to interacting with LLMs. As
research in this area continues to evolve, the integration of Active-Prompt techniques
islikelytoplayacrucialroleindevelopingmoresophisticatedandeffectiveAIsystems.
3.9 ReAct Framework
The ReAct Framework, short for Reasoning and Acting, represents a cutting-edge
approach in prompt engineering aimed at enhancing the interaction capabilities of
Large Language Models (LLMs). This method synergizes the processes of reasoning
and action to enable LLMs to not only think through problems but also interact
with external tools and environments to achieve more accurate and contextually
appropriate outcomes.
The ReAct Framework operates by prompting LLMs to generate both reasoning
traces and task-specific actions. This dual approach ensures that the model first contemplates the problem, devising a logical sequence of thoughts, and then executes
actionsthatmayinvolvequeryingexternaldatabases,usingcalculators,orinteracting
with other software tools. This method is particularly effective in scenarios requiring detailed reasoning followed by specific actions, thus ensuring the LLM can handle
complex, multi-step tasks efficiently [89].
For example, in a task involving financial analysis, the ReAct framework would
first prompt the LLM to outline the necessary steps to evaluate a portfolio. Subsequently, the model could use financial analysis tools to gather current market data
andperformcalculations,integratingtheseresultsintothefinalanalysis.Thiscombination of reasoning and action leads to more robust and reliable outcomes compared
to using static prompts alone.
TheReActFrameworkoffersseveralnotableadvantages.Byintegratingreasoning
and action, ReAct enables LLMs to make more informed and accurate decisions.
This is particularly valuable in fields such as finance, healthcare, and legal analysis,
where decisions must be based on comprehensive data and logical reasoning [90].
Additionally, the framework’s ability to interact with external tools ensures that the
informationusedindecision-makingisup-to-dateandrelevant,reducingthelikelihood
of errors due to outdated or incomplete data [91]. Furthermore, ReAct expands the
range of tasks LLMs can perform by enabling them to act on their reasoning. This
makes the framework suitable for a variety of applications, from customer service
15

<!-- Page 16 -->

automation to scientific research, where complex, multi-step processes are common
[92].
Research on the ReAct Framework underscores its potential in transforming how
LLMs handle complex tasks. Studies by Yao et al. (2022) highlight how the integration of reasoning and action in prompts can significantly improve task performance
in LLMs. Additionally, practical applications have demonstrated the framework’s
effectiveness in real-world scenarios, such as dynamic data retrieval and interactive
problem-solving [89, 90].
ImplementingtheReActFrameworkinvolvesdevelopingpromptsthatguideLLMs
through both thought processes and actions. This requires a detailed understanding
of the task at hand and the tools available, ensuring that the model can seamlessly
transition from reasoning to action. As the field of prompt engineering evolves, the
ReAct Framework is likely to become an essential tool for developing more versatile
and capable AI systems.
In conclusion, the ReAct Framework represents a significant advancement in
prompt engineering, combining logical reasoning with actionable steps to enhance
the performance and reliability of LLMs. As research continues to expand on this
approach, the framework’s integration into various AI applications promises to drive
further innovation and effectiveness in AI-driven tasks.
3.10 Retrieval augmentation
Another direction of prompt engineering is to aim to reduce hallucinations. When
using AIGC tools such as GPT-4, it is common to face a problem called “hallucinations”, which refer to the presence of unreal or inaccurate information in the model’s
generated output [33, 93]. While these outputs may be grammatically correct, they
can be inconsistent with facts or lack real-world data support. Hallucinations arise
because the model may not have found sufficient evidence in its training data to support its responses, or it may overly generalize certain patterns when attempting to
generate fluent and coherent output [94].
An approach to reduce hallucinations and enhance the effectiveness of prompts is
theso-calledretrievalaugmentationtechnique,whichaimsatincorporatingup-to-date
external knowledge into the model’s input [95, 96]. It is emerging as an AI framework for retrieving facts from external sources. [97] examines the augmentation of
context retrieval through the incorporation of external information. It proposes a
sophisticated operation: the direct concatenation of pertinent information obtained
from an external source to the prompt, which is subsequently treated as foundationalknowledgeforinputintotheexpansivelanguagemodel.Additionally,thepaper
introduces auto-regressive techniques for both retrieval and decoding, facilitating a
more nuanced approach to information retrieval and fusion. This research demonstrates that in-context retrieval-augmented language models [97], when constructed
uponreadilyavailablegeneral-purposeretrievers,yieldsignificantLLMenhancements
across a variety of model dimensions and diverse corpora. In another research, [98]
showedthatGPT-3canreducehallucinationsbystudyingvariousimplementationsof
the retrieval augmentation concept, such as Retrieval Augmented Generation (RAG)
[99],Fusion-in-Decoder(FiD)[100],Seq2seq[101–103]andothers.[104]developedthe
Chain-of-Verification (CoVe) approach to reduce hallucinations, based on letting the
LLM deliberate on its own responses before self-correcting them. They suspect that
extending thisapproach with retrievalaugmentationwould likely bringfurther gains.
3.11 Use plugins to polish the prompts
After introducing the detailed techniques and methods of prompt engineering, we
now explore the use of some external prompt engineering assistants that have been
developed recently and exhibit promising potential. Unlike the methods introduced
previously, these instruments can help us to polish the prompt directly. They are
adept at analyzing user inputs and subsequently producing pertinent outputs within
16

<!-- Page 17 -->

a context that is defined by itself, thereby amplifying the efficacy of prompts. Some
of the plugins provided by OpenAI are good examples of such tools [105].
In certain implementations, the definition of a plugin is incorporated into the
prompt, potentially altering the output [106]. Such integration may impact the manner in which LLMs interpret and react to the prompts, illustrating a connection
between prompt engineering and plugins. Furthermore, the laborious nature of intricatepromptengineeringmaybemitigatedbyplugins,whichenablethemodeltomore
proficiently comprehend or address user inquiries without necessitating excessively
detailed prompts. Consequently, plugins bolster the efficacy of prompt engineering
while promoting enhanced user-centric efficiency. These tools, akin to packages, can
be seamlessly integrated into Python and invoked directly [107, 108]. Such plugins
augment the efficacy of prompts by furnishing responses that are both coherent and
contextuallypertinent.Forinstance,the“PromptEnhancer”pluging[109],developed
by AISEO [110], can be invoked by starting the prompt with the word “AISEO” to
let the AISEO prompt generator automatically enhance the LLM prompt provided.
Similarly,anotherplugincalled“PromptPerfect”,canbeusedbystartingtheprompt
with ‘perfect’ to automatically enhance the prompt, aiming for the “perfect” prompt
for the task at hand [111, 112].
4 Methodologies of Multimodal LM
Multimodallanguagemodels(MMLMs)representasignificantadvancementinartificialintelligence,enablingtheprocessingandgenerationofinformationacrossmultiple
modalities, such as text, images, and audio. This capability enhances the versatility
andapplicabilityofAIsystemsindiversefields,fromcontentcreationtocomplexreasoningtasks.PromptengineeringinMMLMsinvolvesadaptingtraditionaltechniques
used in text-only LLMs to handle the intricacies of multimodal data. These models
must seamlessly integrate and interpret various data types, requiring sophisticated
prompt designs that ensure contextual coherence and accuracy [113].
Challenges such as data alignment, modality integration, and context preservationareaddressedthroughmodularpromptinganddisentangledpromptdesign[114].
These advancements facilitate the effective utilization of MMLMs in various applications,enhancingtheirabilitytogeneratenuancedandcontextuallyrichoutputs[115].
Pioneeringstudieshavedemonstratedthepotentialofthesemethods,highlightingthe
transformative impact of prompt engineering on multimodal AI systems [116].
Promptengineeringformultimodallargelanguagemodels(MLLMs)buildsonthe
foundationaltechniquesusedintext-onlyLLMsbutadaptsthemtoaccommodatethe
complexity of multimodal data. Traditional prompt methods, such as few-shot and
zero-shot learning, are modified to handle diverse data types, including text, images,
and audio. This adaptation is crucial as MLLMs must integrate and process multiple
modalities simultaneously, requiring innovative approaches to ensure coherence and
relevanceingeneratedresponses[117].TheseadvancementsfacilitatetheeffectiveutilizationofMLLMsinvariousapplications,enhancingtheirabilitytogeneratenuanced
and contextually rich outputs [118]. Pioneering studies have demonstrated the potential of these methods, highlighting the transformative impact of prompt engineering
on multimodal AI systems [113, 119].
4.1 Multi-modal Prompt Learning (MaPLe)
Multi-modal Prompt Learning (MaPLe) represents a significant advancement in the
fine-tuning of vision-language models, leveraging the integration of both vision and
language prompts to enhance model performance. This methodology is predicated
on the hierarchical learning of prompts within the transformer layers of the model,
allowingforamorenuancedandcomprehensivecaptureoftask-relevantfeatures.The
coreideabehindMaPLeistointroduceandoptimizepromptsforboththevisionand
languagecomponentssimultaneously.Byembeddingpromptsatvariousstageswithin
the transformer architecture, MaPLe ensures that the model can adaptively learn
17

<!-- Page 18 -->

contextual information pertinent to the specific task at hand [120]). This hierarchical
approachallowsthemodeltoprogressivelyrefineitsunderstandingandintegrationof
multimodal inputs, leading to improved performance across a range of applications.
One of the critical innovations of MaPLe is its ability to enhance task relevance.
Traditional prompt engineering often focuses on either vision or language prompts
in isolation, which can limit the model’s ability to fully leverage the complementary
informationavailableinmultimodaldata.MaPLeovercomesthislimitationbyjointly
optimizing prompts for both modalities, thereby facilitating a more integrated and
coherent representation of the input data [120, 121].
TheeffectivenessofMaPLehasbeendemonstratedinvariousstudies.Forexample,
[120] showed that MaPLe significantly outperforms baseline models in tasks such
as image recognition and visual question answering. Furthermore, [121] highlighted
the importance of multi-modal prompt learning in enhancing the adaptability and
generalization of vision-language models.
AnotherimportantaspectofMaPLeisitshierarchicallearningmechanism,which
allowsthemodeltoprocessandintegrateinformationatmultiplelevelsofabstraction.
This is particularly beneficial for complex tasks that require a deep understanding of
both visual and textual elements. By optimizing prompts at different layers within
thetransformer,MaPLecanbettercapturetheintricatedependenciesbetweenvision
and language inputs [120, 122].
ToillustratethepracticalapplicationofMaPLe,considerthetaskofVisualQuestionAnswering(VQA).InatypicalVQAscenario,amodelisprovidedwithanimage
and a related question, and it must generate a correct and contextually relevant
answer. Using MaPLe, the model can be fine-tuned with multi-modal prompts that
simultaneouslyaddressboththevisualcontentandthetextualquestion.Forinstance,
given an image of a bustling market and the question ”What fruit is the vendor
selling?”, MaPLe would embed prompts at various levels of the transformer’s vision
and language branches. These prompts might include visual prompts that focus on
identifyingobjectsandtextpromptsthatguidethemodeltolookforspecificanswerrelevant details. By processing these prompts hierarchically, the model can effectively
integrate visual cues (like recognizing apples and oranges in the image) with the textual context (understanding the question) to generate an accurate answer (e.g., ”The
vendor is selling apples and oranges”).
This multi-modal approach ensures that the model leverages both the visual and
textual information in a coherent and integrated manner, resulting in improved performance on VQA tasks compared to models that do not utilize such comprehensive
prompt learning strategies.
In conclusion, MaPLe represents a robust and effective methodology for improving the performance of vision-language models. Its ability to integrate and optimize
multi-modal prompts within the transformer architecture ensures that the model can
adaptivelylearnandgeneralizeacrossawiderangeoftasks,makingitavaluabletool
in the field of multimodal AI.
4.2 Context Optimization
Context Optimization (CoOp) is an innovative approach to prompt learning specificallydesignedforvision-languagemodels.CoOpfocusesonenhancingtheadaptability
and performance of these models by optimizing context-specific prompts. This
methodology involves the creation of learnable context vectors that are embedded within the model’s architecture, enabling it to dynamically adjust to different
downstream tasks [123].
CoOp leverages the inherent structure of vision-language models, such as CLIP,
by integrating context optimization directly into the model’s training process. This
integration allows for a seamless adaptation to various tasks without the need for
extensive manual prompt engineering. By utilizing learnable context vectors, CoOp
can fine-tune the prompts based on the specific characteristics of the input data,
leading to improved performance and generalization across different scenarios [124].
18

<!-- Page 19 -->

One of the key benefits of CoOp is its ability to handle diverse and complex data
inputs. Traditional static prompts can be limited in their ability to adapt to new and
unseendata,whereasCoOp’sdynamicapproachallowsthemodeltolearnandadjust
in real-time. This is particularly valuable in applications such as image recognition
and visual question answering, where the context can vary significantly [125].
ToillustratethepracticalapplicationofCoOp,consideraVisualQuestionAnswering (VQA) task. In a VQA scenario, the model is presented with an image and a
corresponding question, and it must generate an accurate answer based on the visual
and textual information. Using CoOp, the model can be trained with context-specific
prompts that enhance its ability to interpret the image and understand the question.
For instance, if the model is shown an image of a beach scene with the question
”What activity are the people engaged in?”, CoOp would utilize learnable context
vectors to focus on relevant aspects of the image, such as identifying people, recognizing activities, and understanding the scene’s context. This enables the model to
generate a precise and contextually relevant answer, such as ”The people are playing
volleyball on the beach” [123].
The effectiveness of CoOp has been demonstrated in various studies. Zhou et
al. (2021) [1] showed that models using CoOp significantly outperform traditional
models in tasks such as image recognition and VQA. Additionally, [125] highlighted
the benefits of ensembling context optimization, which further enhances the model’s
performance by combining multiple context vectors. This approach has been shown
to improve the robustness and generalization of vision-language models in real-world
applications (Unified Adapter and Prompt Learning, 2023) [126].
Insummary,ContextOptimization(CoOp)representsapowerfulmethodologyfor
enhancing the performance and adaptability of vision-language models. By leveraging learnable context vectors, CoOp enables these models to dynamically adjust to
differenttasksanddatainputs,makingitavaluabletoolinthefieldofmultimodalAI.
4.3 Conditional Prompt Learning
Conditional Prompt Learning is a methodology that enhances the adaptability and
performance of vision-language models by tailoring prompts based on specific conditions or contexts. This technique allows models to dynamically adjust their responses
to better fit the requirements of various tasks, thereby improving their overall
effectiveness and versatility.
ThecoreconceptofConditionalPromptLearninginvolvesthecreationofprompts
that are conditionally tailored to the specific input or task context. This method
stands in contrast to static prompts that remain the same regardless of the situation.
By leveraging contextual information, conditional prompts can provide more precise
and relevant guidance to the model, which is particularly useful in complex, multimodalscenarioswheretheinterplaybetweendifferenttypesofdatamustbecarefully
managed [127].
One significant advantage of Conditional Prompt Learning is its ability to adapt
to new and unseen data with minimal fine-tuning. This is achieved by training the
model on a variety of context-specific prompts, which enables it to generalize better
across different tasks. For instance, a vision-language model trained with conditional
prompts can more accurately interpret and respond to images and questions it has
not encountered during training [127]. This capability is critical for applications such
as image captioning, visual question answering, and scene understanding, where the
context can vary widely.
Consider an image captioning task where the goal is to generate descriptive captions for images. Using Conditional Prompt Learning, the model can be trained with
prompts that are specifically designed for different types of scenes. For example, a
promptforanoutdoorscenemightincludecontextualcuesrelatedtonature,weather,
andactivities,whileapromptforanindoorscenemightfocusonobjects,people,and
interactions.
19

<!-- Page 20 -->

In practice, if the model is presented with an image of a bustling market, the
conditional prompt might include cues such as ”Identify the types of products being
sold,” or ”Describe the interactions between vendors and customers.” This allows
the model to generate a caption that is not only accurate but also contextually rich
and informative. For instance, the model might produce a caption such as ”Vendors
selling fresh fruits and vegetables in a crowded market, with customers browsing and
purchasing items” [121].
The effectiveness of Conditional Prompt Learning has been demonstrated in
various studies. [127] showed that models employing this technique significantly
outperform those using static prompts in tasks such as visual question answering
and image classification. Furthermore, these models exhibit improved generalization
capabilities, making them more robust in real-world applications [128].
In summary, Conditional Prompt Learning is a powerful methodology that
enhances the adaptability and performance of vision-language models by leveraging
context-specific prompts. Its ability to dynamically adjust to new and unseen data
makes it an invaluable tool for a wide range of applications in multimodal AI.
4.4 Modular Prompting
Modular prompting is a sophisticated approach used in vision-language models to
handle the complexity of integrating visual and textual data. This method involves
breaking down prompts into modular components that can be individually optimized
and then recombined to handle complex multimodal tasks. By treating each part of
the prompt as a distinct module, the model can better manage and integrate diverse
types of information, leading to improved performance and adaptability.
Modular prompting separates the visual and textual components of the input,
allowingforindependentoptimizationbeforecombiningthem.Thisseparationensures
thateachmodalityisprocessedinthemosteffectivemanner,facilitatingamoreaccurateandefficientintegrationofdata[129].Additionally,eachmodulecanbeenhanced
with contextual embeddings that provide supplementary information relevant to the
task, which helps the model understand the relationships between different pieces of
information [130]. Oncethe individual modules are processed, the modeldynamically
integratestheoutputstogenerateacoherentresponse,adjustingtheintegrationbased
on the specific requirements of the task at hand [131].
Consider an application in open-vocabulary semantic segmentation. In this task,
the goal is to segment an image into regions corresponding to different object categories,evenifthecategorieswerenotseenduringtraining.Usingmodularprompting,
avision-languagemodelcanseparatelyprocessvisualfeaturesandtextualdescriptions
of categories.
For instance, the model can be prompted with specific modules for identifying
visual features like ”urban environment,” ”vehicles,” and ”pedestrians,” along with
textual descriptions for each category. This separation allows the model to optimize
the processing of visual and textual data independently. Once the individual modules
are processed, the model integrates the results to accurately segment the image and
identify the various components, even those it hasn’t seen before [132].
In conclusion, modular prompting is a powerful method for enhancing the performance and adaptability of vision-language models. By independently optimizing
and dynamically integrating visual and textual modules, this approach ensures that
models can handle a wide range of tasks with improved accuracy and efficiency.
4.5 Zero-shot and Few-shot Prompting
Zero-shot and few-shot prompting are pivotal techniques in the realm of visionlanguage models, enabling these models to handle tasks with minimal or no taskspecific training data. Zero-shot prompting allows models to perform tasks without
any specific examples provided during training, relying entirely on their pre-trained
knowledgetogeneralizeacrossnewtasksanddomains.Forexample,amodellikeCLIP
can be prompted with a textual description to classify images into categories it has
20

<!-- Page 21 -->

never explicitly been trained on [7]. On the other hand, few-shot prompting involves
providing the model with a small number of examples during inference, significantly
enhancing the model’s ability to generalize with limited data [15].
An illustrative example of these techniques can be seen in the task of Visual
Question Answering (VQA). In a zero-shot VQA task, the model might be asked,
”What is the object in the image?” without having seen similar examples during
training.Themodelleveragesitsbroadunderstandingderivedfromextensivetraining
ondiversedatasetstogeneratearelevantanswer.Inafew-shotscenario,themodelis
provided with a few example questions and answers related to similar images before
answering the new question, thus refining its accuracy and contextual understanding
[121].
Research supports the effectiveness of these methods: [133] explored various
prompting techniques for zero- and few-shot learning in vision-language models,
demonstrating improved performance on novel tasks. [15] showed the application of
thesetechniquesinCLIP,highlightingthemodel’sabilitytogeneralizeacrossdifferent
domains.Additionally,[134]presentedamethodforadaptingCLIPtofew-shotclassificationtaskswithoutadditionaltraining,emphasizingpracticalbenefitsinreal-world
applications.
In conclusion, zero-shot and few-shot prompting are essential for enhancing the
versatility and adaptability of vision-language models. These methods leverage pretrained knowledge and minimal task-specific examples, enabling models to perform a
wide range of tasks with high accuracy and minimal data, thus proving invaluable in
the field of multimodal AI.
4.6 Reinforcement Learning for Prompt Optimization
Reinforcement Learning (RL) for prompt optimization is an advanced technique
designedtoenhancetheperformanceofvision-languagemodelsbyiterativelyrefining
the prompts used during training and inference. This method utilizes the principles
of reinforcement learning to navigate the complex parameter space of large models,
optimizing the prompts for improved task-specific performance. In RL for prompt
optimization, a reward function is defined to evaluate the effectiveness of different
prompts based on the model’s output. The model then uses this feedback to adjust
and optimize the prompts through a series of iterations, ensuring that the prompts
evolve to maximize performance on the target task by leveraging the model’s ability
to learn from its interactions with the environment [135].
Consider the task of Visual Question Answering (VQA), where the goal is to
generate accurate answers to questions based on visual input. Using RL for prompt
optimization, the model can start with a set of initial prompts and iteratively refine
them based on the accuracy of the generated answers. For instance, if the model is
asked,”Whatisthecolorofthecarintheimage?”theinitialpromptsmightproduce
varied responses. The reward function will assess these responses, favoring prompts
that lead to correct answers. Over multiple iterations, the model learns to generate
more precise prompts, improving its ability to accurately answer similar questions in
the future [133].
Research supports the effectiveness of these methods. [135] explored the use of
reinforcement learning to optimize discrete text prompts for vision-language models,
demonstrating significant improvements in task performance through iterative optimization. [136] introduced gradient-based techniques to simplify the optimization of
hard prompts, providing a robust framework for enhancing vision-language model
performance using reinforcement learning. Additionally, [137] focused on adapting
prompts at test time using reinforcement learning, allowing models to dynamically
adjust prompts based on real-time feedback, thereby improving adaptability. [138]
discussed a black-box approach to prompt tuning using evolutionary strategies in
conjunction with reinforcement learning, highlighting its effectiveness in optimizing
prompts for various vision-language tasks.
21

<!-- Page 22 -->

In conclusion, reinforcement learning for prompt optimization represents a powerful methodology for enhancing the performance and adaptability of vision-language
models.Byiterativelyrefiningpromptsbasedontask-specificfeedback,thisapproach
enables models to achieve higher accuracy and generalization across diverse applications.
4.7 Prompt Pattern Catalog
APromptPatternCatalogisanorganizedcollectionofprompttemplatesandpatterns
designed to enhance the effectiveness of prompt engineering, particularly in visionlanguage models. This methodology involves creating a standardized set of prompt
patternsthatcanbeappliedacrossvarioustasks,ensuringconsistencyandoptimizing
the performance of models through systematic prompt design. By developing a catalogofpromptpatterns,researchersandpractitionerscanensureaconsistentapproach
to prompt engineering, reducing variability and errors from ad hoc prompt creation
[139]. Using pre-defined prompt patterns streamlines the process of prompt engineering, saving time and resources by allowing practitioners to select and adapt patterns
rather than crafting new prompts from scratch [139]. A well-designed prompt pattern catalog includes patterns for various contexts and applications, enabling models
to be quickly adapted to new tasks and domains by selecting the most appropriate
patterns [139]. Systematic use of optimized prompt patterns enhances model performance by providing more effective and contextually appropriate prompts, leading to
better task-specific results [140].
For example, in the task of image captioning, a vision-language model can use
standardizedpatternstailoredfordifferenttypesofimages.Foranimageofabustling
market, the model could use a prompt pattern designed for urban scenes, including
instructionstodescribethesetting,identifykeyobjects,andnoteinteractionsbetween
people. This might result in a detailed and contextually appropriate caption, such as
”Theimageshowsabustlingmarketwithvendorssellingvariousfruitsandvegetables,
and customers browsing and purchasing items” [141].
Research supports the effectiveness of prompt pattern catalogs. [139] outline
the development and use of a prompt pattern catalog to improve the effectiveness
and efficiency of prompt engineering with vision-language models. [140] explore how
structured prompt patterns can enhance user interaction and improve model outputs in conversational AI, providing insights applicable to vision-language models.
[141] investigate the application of prompt engineering patterns in enterprise settings, demonstrating their utility in optimizing model performance across various
tasks. Additionally, [142] highlight the benefits of using structured prompt patterns
in software development, which can be extended to vision-language models.
In conclusion, a prompt pattern catalog is a valuable tool for enhancing the effectivenessandefficiencyofpromptengineeringinvision-languagemodels.Byproviding
standardized, adaptable, and optimized prompt patterns, this methodology ensures
consistent and high-quality model performance across a wide range of tasks.
5 Assessing the efficacy of prompt methods
There are many different ways to evaluate the quality of the output. To assess the
efficacy of current prompt methods in AIGC tools, evaluation methods can generally
be divided into subjective and objective categories.
5.1 Subjective and objective evaluations
Subjectiveevaluationsprimarilyrelyonhumanevaluatorstoassessthequalityofthe
generatedcontent.HumanevaluatorscanreadthetextgeneratedbyLLMsandscore
itforquality.Subjectiveevaluationstypicallyincludeaspectssuchasfluency,accuracy,
novelty, and relevance [40]. However, these evaluation methods are, by definition,
subjective and can be prone to inconsistencies.
22

<!-- Page 23 -->

Objective evaluations, also known as automatic evaluation methods, use machine
learning algorithms to score the quality of text generated by LLMs. Objective evaluations employ automated metrics, such as BiLingual Evaluation Understudy (BLEU)
[143], which assigns a score to system-generated outputs, offering a convenient and
rapid way to compare various systems and monitor their advancements. Other evaluations such as Recall-Oriented Understudy for Gisting Evaluation (ROUGE) [144],
and Metric for Evaluation of Translation with Explicit ORdering (METEOR) [145],
assess the similarity between the generated text and reference text. More recent evaluation methods, such as BERTScore [146], aim to assess at a higher semantic level.
However,theseautomatedmetricsoftenfailtofullycapturetheassessmentresultsof
human evaluators and therefore must be used with caution [147].
Subjectiveevaluationandobjectiveevaluationmethodseachhavetheirownadvantagesanddisadvantages.Subjectiveevaluationtendstobemorereliablethanobjective
evaluation, but it is also more expensive and time-consuming. Objective evaluation is
lessexpensiveandquickerthansubjectiveevaluation.For instance,despite numerous
pieces of research highlighting the limited correlation between BLEU and alternative metrics based on human assessments, their popularity has remained unaltered
[148, 149]. Ultimately, the best way to evaluate the quality of LLM output depends
on the specific application [150]. If quality is the most important factor, then using
humanevaluatorsisthebetterchoice.Ifcostandtimearethemostimportantfactors,
then using automatic evaluation methods is better.
5.2 Comparing different prompt methods
In the field of prompt engineering, previous work has mostly focused on designing
and optimizing specific prompting methods, but evaluating and comparing different
prompting approaches in a systematic manner remains limited. There are some modelsthatareincreasinglyusedtogradetheoutputofothermodels,whichaimto‘check’
the ability of other models [151, 152]. For instance, LLM-Eval [153] was developed to
measuretheopen-domainconversationswithLLMs.Thismethodtriestoevaluatethe
performanceofLLMsonvariousbenchmarkdatasets[154,155]anddemonstratetheir
efficiency. Other studies experiment mainly on certain models or tasks and employ
disparateevaluationmetrics,restrictingcomparabilityacrossmethods[135,156].Nevertheless,recentresearchproposedageneralevaluationframeworkcalledInstructEval
[157] that enables a comprehensive assessment of prompting techniques across multiple models and tasks. The InstructEval study reached the following conclusions:
in few-shot settings, omitting prompts or using generic task-agnostic prompts tends
to outperform other methods, with prompts having little impact on performance; in
zero-shotsettings,expert-writtentask-specificpromptscansignificantlyboostperformance,withautomatedpromptsnotoutperformingsimplebaselines;theperformance
ofautomatedpromptgenerationmethodsisinconsistent,varyingacrossdifferentmodelsandtasktypes,displayingalackofgeneralization.InstructEvalprovidesimportant
references for prompt engineering and demonstrates the need for more universal and
reliable evaluation paradigms to design optimal prompts.
6 Applications improved by prompt engineering
The output enhancements provided by prompt engineering techniques make LLMs
betterapplicabletoreal-worldapplications.Thissectionbrieflydiscussesapplications
of prompt engineering in fields such as teaching, programming, and others.
6.1 Assessment in teaching and learning
The study [158] investigates the application of machine learning methods in young
studenteducation.Insuchacontext,promptengineeringcanfacilitatethecreationof
personalizedlearningenvironments.Byofferingtailoredprompts,LLMscanadaptto
an individual’s learning pace and style. Such an approach can allow for personalized
assessments and educational content, paving the way for a more individual-centric
23

<!-- Page 24 -->


### Principles of Accounting: Course Outline

Group Assignment: Company Financial Analysis

### Duration: 10 weeks

•Description: Groups of 4 students will select a public

### Class Structure:

company and perform a financial statement analysis …
•Lecture: 1 hour per week •Rubrics:
•Workshop/Tutorial: 2 hours per week • Research and Data Collection (20%)
• Correct annual report selected
Week 1: Introduction to Accounting • All relevant data extracted properly
•Lecture: The Importance of Accounting in • Analysis (40%)

### Business • …

•Workshop: Introduction to Financial Statements • Presentation (20%)

### Week 2: Basics of Bookkeeping • …

•Lecture: The Accounting Cycle • …….
•Workshop: Recording Transactions using Double
Entry System
……

### Fig. 12 GuidelineofcoursesgeneratedbyGPT-4

teaching model. Recent advancements in prompt engineering suggest that AI tools
can also cater to students with specific learning needs, thus fostering inclusivity in
education [159]. As a simple example, it is possible for professors to provide rubrics
or guidelines for a future course with the assistance of AI. As Figure 12 shows, when
GPT-4 was required to provide a rubric about a course, with a suitable prompt, it
was able to respond with a specific result that may satisfy the requirement.
The advancements in prompt engineering also bring better potential for automated grading in education. With the help of sophisticated prompts, LLMs can
provide preliminary assessments, reducing the workload for educators while providing instant feedback to students [160]. Similarly, these models, when coupled with
well-designed prompts, can analyze a vast amount of assessment data, thus providing valuable insights into learning patterns and informing educators about areas that
require attention or improvement [161, 162].
6.2 Content creation and editing
With controllable improved input, LLMs have primarily been used in creative works,
such as content creation. Pathways Language Model (PaLM) [70] and prompting approach have been used to facilitate cross-lingual short story generation [23].
The Recursive Reprompting and Revision framework (Re3) [163] employs zero-shot
prompting [65] with GPT-3 to craft a foundational plan including elements such
as settings, characters, and outlines. Subsequently, it adopts a recursive technique,
dynamically prompting GPT-3 to produce extended story continuations. For another
example, Detailed Outline Control (DOC) [164] aims at preserving plot coherence
across extensive texts generated with the assistance of GPT-3. Unlike Re3, DOC
employs a detailed outliner and detailed controller for implementation. The detailed
outliner initially dissects the overarching outline into subsections through a breadthfirstmethod,wherecandidategenerationsforthesesubsectionsaregenerated,filtered,
and subsequently ranked. This process is similar to the method of chain-of-though
(in Section 3.1). Throughout this generation process, an OPT-based Future Discriminators for Generation (FUDGE) [165] detailed controller plays a crucial role in
maintaining relevance.
6.3 Computer programming
PromptengineeringcanhelpLLMsperformbetteratoutputtingprogrammingcodes.
By using a self-debugging prompting approach [60], which contains simple feedback,
unit-test, and code explanation prompts module, the text-to-SQL [166] model is able
to provide a solution it can state as correct unless the maximum number of attempts
has been reached. Another example, Multi-Turn Programming Benchmark (MTPB)
[167], was constructed to implement a program by breaking it into multi-step natural
language prompts.
24

<!-- Page 25 -->

Another approach is provided in [168], which introduced the Repo-Level Prompt
Generator (RLPG) to dynamically retrieve relevant repository context and construct
apromptforagiventask,especiallyoncodeauto-completiontask.Themostsuitable
prompt is selected by a prompt proposal classifier and combined with the default
context to generate the final output.
6.4 Reasoning tasks
AIGC tools have shown promising performance in reasoning tasks. Several previous
researches found that few-shot prompting can enhance the performance in generating accurate reasoning steps for word-based math problems in the GSM8K dataset
[31, 58, 63, 70]. The strategy of including the reasoning traces in such as few-shot
prompts [49], self-talk [169] and chain-of-thought [30], was shown to encourage the
model to generate verbalized reasoning steps. [170] conducted experiments by involving prompting strategies, various fine-tuning techniques, and re-ranking methods to
assess their impact on enhancing the performance of a base LLM. They found that
a customized prompt significantly improved the model’s ability with fine-tuning,
and demonstrated a significant advantage by generating substantially fewer errors
in reasoning. In another research, [65] observed that solely using zero-shot CoT
prompting leads to a significant enhancement in the performance of GPT-3 and
PaLM when compared to the conventional zero-shot and few-shot prompting methods. This improvement is particularly noticeable when evaluating these models on
theMultiArith[171]andGSM8K[63]datasets.[172]alsointroducedanovelprompting approach called Diverse Verifier on Reasoning Step (DIVERSE). This approach
involvesusingadiversesetofpromptsforeachquestionandincorporatesatrainedverifierwithanawarenessofreasoningsteps.TheprimaryaimofDIVERSEistoenhance
the performance of GPT-3 on various reasoning benchmarks, including GSM8K and
others. All these works show that in the application of reasoning tasks, properly
customized prompts can obtain better results from the model.
6.5 Dataset generation
LLMs possess the capability of in-context learning, enabling them to be effectively
prompted to generate synthetic datasets for training smaller, domain-specific models.
[173]putforththreedistinctpromptingapproachesfortrainingdatagenerationusing
GPT-3: unlabeled data annotation, training data generation, and assisted training
data generation. Besides, [174] is designed for the generation of supplementary syntheticdataforclassificationtasks.GPT-3isutilizedinconjunctionwithapromptthat
includes real examples from an existing dataset, along with a task specification. The
goal is to jointly create synthetic examples and pseudo-labels using this combination
of inputs.
7 Exploring and Enhancing LLMs through Insightful

### Prompt Engineering

Promptengineeringistheprocessofdesigningandrefiningtheinputs(prompts)given
toLLMstoelicitdesiredandaccurateresponses.Thistechniqueiscrucialnotonlyfor
optimizing model performance but also for enhancing security. By carefully crafting
prompts,researchersanddeveloperscanidentifyandmitigatevulnerabilitiesinLLMs.
Effective prompt engineering can expose weaknesses that might be exploited through
adversarial attacks, data poisoning, or other malicious activities. Conversely, poorly
designed prompts can inadvertently introduce or exacerbate security risks, making
it easier for attackers to manipulate model outputs or extract sensitive information.
Thus, prompt engineering serves as both a tool for improving LLM functionality and
a critical component of their security framework.
Understanding the interplay between prompt engineering and LLM security is
essential for developing robust models that can safely operate in diverse and critical
applications.Aswedelvedeeperintothevariousvulnerabilitiesandthedualnatureof
25

<!-- Page 26 -->

prompt engineering, it becomes clear that maintaining a balance between enhancing
capabilities and ensuring security is pivotal for the future of LLMs.
This expanded introduction sets the stage for a detailed exploration of the vulnerabilities inherent in LLMs and the dual-edged nature of prompt engineering,
highlightingitssignificanceinbothimprovingperformanceandsafeguardingsecurity.
7.1 Introduction to Security in LLMs
The development and deployment of Large Language Models (LLMs) have significantly advanced natural language processing, enabling applications ranging from
automatedcustomersupporttosophisticatedcontentgeneration.However,withtheir
increasing integration into critical sectors such as healthcare, finance, and cybersecurity, the importance of ensuring robust security measures for LLMs cannot be
overstated.Thesemodels,ifcompromised,canleadtosignificantbreachesofsensitive
information and disrupt essential services.
AsLLMsbecomemoreubiquitous,theirpotentialvulnerabilitiesposesevererisks.
Adversarial attacks, for instance, can manipulate model outputs, leading to harmful or misleading information dissemination [7]. Additionally, data poisoning during
the training phase can introduce malicious data that corrupts the model’s learning
process, resulting in unreliable outputs [15]. These threats highlight the necessity of
comprehensive security protocols to safeguard the integrity and reliability of LLMs.
The increasing reliance on LLMs across various sectors underscores the need for
robust security measures. For example, in healthcare, LLMs analyze medical records
andprovidediagnosticrecommendations.Acompromisedmodelinthiscontextcould
lead to incorrect diagnoses and treatment plans, endangering patient lives. Similarly,
infinance,LLMsassistinfrauddetectionandriskassessment;vulnerabilitiesinthese
systems could result in significant financial losses and undermine trust in automated
financial services [175]. Therefore, ensuring the security of LLMs is critical to their
safe and effective deployment.
7.2 Common Vulnerabilities in LLMs
7.2.1 Adversarial Attacks
Adversarial attacks involve the deliberate manipulation of input data to deceive a
machine learning model into making incorrect predictions. In the context of LLMs,
adversarial attacks can take the form of subtly altered prompts or inputs that cause
the model to produce unintended or harmful outputs. These attacks exploit the
sensitivity of LLMs to small perturbations in input data, revealing significant vulnerabilities [176]. For instance, an adversarial input might include slight alterations in
the text that mislead the model’s natural language understanding capabilities, leading to incorrect or biased responses [7, 177]. The potential for adversarial attacks is
particularly concerning in applications such as automated customer service or legal
document analysis, where the integrity and accuracy of responses are critical [178].
Recent research has highlighted various techniques and impacts of adversarial
attacksonLLMs.Forinstance,adversarialdemonstrationattackscanmisleadmodels
into making incorrect predictions even with subtle changes in the input data [179].
Similarly, methods to automatically generate readable and strategic prompts show
the ease with which adversarial examples can be crafted [180].
Optimization techniques enhance the effectiveness of adversarial attacks, making
it more challenging to defend against these threats [181]. Moreover, a comprehensive overview of these attacks exposes various weaknesses in LLMs, underscoring the
critical need for improved security measures [182].
Real-world examples illustrate the significant impact of adversarial attacks on
LLMs.Forinstance,adversarialinputsinlegaldocumentanalysiscanleadtoincorrect
legal interpretations, potentially affecting case outcomes. In healthcare, adversarial
attacks could mislead models into providing incorrect medical advice, jeopardizing
26

<!-- Page 27 -->

patientsafety.Theseexampleshighlighttheurgentneedforeffectivedefensesagainst
adversarial attacks to ensure the safe and reliable deployment of LLMs.
In summary, adversarial attacks pose a significant threat to the security and reliability of LLMs. These attacks exploit the sensitivity of LLMs to small perturbations
in input data, leading to unintended or harmful outputs. The role of prompt engineering is crucial in identifying and mitigating these vulnerabilities, ensuring that
prompts are carefully crafted to minimize the risk of exploitation. As LLMs become
increasinglyintegratedintocriticalapplications,theneedforrobustpromptengineering practices becomes ever more pressing. Future research and development should
focusonadvancingthesepracticestoprotectLLMsfromemergingthreatsandensure
their safe deployment.
7.2.2 Prompt Hacking
Prompt hacking poses a significant threat to the security and reliability of LLMs.
This type of attack involves manipulating the inputs (prompts) given to LLMs to
provokeunintendedoutcomes,rangingfrombenignerrorstomaliciousactivitiessuch
asmisinformationdisseminationanddatabreaches.Unliketraditionalhacking,which
typically exploits software vulnerabilities, prompt hacking relies on carefully crafting
prompts to deceive the LLM into performing undesired actions [183–188].
Prompt hacking exploits the fundamental way LLMs process and generate
responses. Attackers craft malicious prompts designed to exploit the model’s understanding and generation capabilities. These prompts can cause the model to produce
harmful outputs, leak sensitive information, or behave erratically. For example, a
malicious prompt might subtly alter a request in a way that leads the LLM to generatefalseormisleadinginformation[189].Thisvulnerabilityisparticularlyconcerning
becauseitcanbeexecutedwithouttheneedforsophisticatedtechnicalskills.AsLLMs
become more integrated into various applications, the risk posed by prompt hacking
increases, necessitating robust security measures to prevent such attacks [190].
Understanding prompt hacking is crucial for developing security measures to
protectLLM-basedapplications.Awarenessofthisvulnerabilityencouragestheimplementationofstricterpromptvalidationandmonitoringsystemstodetectandprevent
malicious prompts. By studying prompt hacking techniques, developers can enhance
the robustness of LLMs. Implementing countermeasures such as prompt filtering,
anomaly detection, and response validation helps mitigate the impact of such attacks
and improve overall system security [191]. Additionally, educating users about the
risks of prompt hacking and best practices for secure prompt creation can significantly reduce the likelihood of successful attacks. Training programs and guidelines
for creating secure prompts are essential for maintaining the integrity of LLM-based
systems [192].
Recent studies have highlighted the growing threat of prompt hacking and the
need for comprehensive security strategies. For example, research published by Rise
and Inspire (2024) details various prompt hacking techniques and their implications
for LLM security. Similarly, OWASP’s project on LLM prompt hacking provides
a framework for understanding and mitigating these vulnerabilities [193]. Practical implementations of security measures against prompt hacking include the use of
advancedmonitoringtoolsthatdetectsuspiciouspromptpatternsandtheintegration
of machine learning models trained to identify and block malicious prompts. These
measuresarecrucialforensuringthesafedeploymentofLLMsinsensitiveapplications
such as healthcare, finance, and customer service [194].
In conclusion, prompt hacking represents a critical challenge in the secure deployment of LLMs. By understanding the mechanisms and risks associated with this
vulnerability,researchersanddeveloperscanimplementeffectivesecuritymeasuresto
protect against such attacks. Future research should continue to explore innovative
solutions to enhance the resilience of LLMs against prompt hacking, ensuring their
safe and reliable use in various applications.
27

<!-- Page 28 -->

7.2.3 Threat of Model Stealing
ModelstealingattacksposeasignificantthreattothesecurityofLLMs.Theseattacks
involve an adversary attempting to replicate the functionality or extract proprietary
information from a target model by interacting with it through strategically crafted
prompts. The implications of such attacks are severe, as they can lead to intellectual
property theft, loss of competitive advantage, and potential misuse of the replicated
models [195–197].
Prompts play a crucial role in model stealing attacks. By systematically querying
an LLM with carefully designed prompts, an attacker can infer the model’s behavior
and underlying parameters. This process, known as ”query-based extraction,” allows
theattackertobuildasurrogatemodelthatmimicsthetargetmodel’sresponses.The
effectiveness of this approach relies on the ability to generate diverse and informative
prompts that cover a wide range of inputs the model might encounter [198].
For instance, an attacker might use a series of varied prompts to understand how
the model processes different types of queries. By analyzing the model’s outputs, the
attacker can gradually reconstruct the model’s decision-making process and replicate
its functionality. This method is particularly effective when the target model is a
black-box system, where the attacker has no access to the internal architecture but
can observe the outputs generated in response to the inputs [199].
One notable example of a model stealing attack is the extraction of the projectionmatrixfromOpenAI’slanguagemodels.Researchersdemonstratedhow,through
a series of carefully crafted prompts, they could extract significant portions of the
model’s architecture and parameters, effectively creating a replica of the original
model [200]. Another incident involved adversaries using prompt engineering techniquestoreplicatecommercialLLMsusedincustomerservice,resultinginsubstantial
intellectual property theft and financial losses for the companies involved [201].
Numerous studies have explored the effectiveness of model stealing through
promptengineering.Forinstance,thepaper”PromptStealingAttacksAgainstLarge
Language Models” highlights how attackers can use advanced prompt engineering
techniquestoextracthigh-valueinformationfromLLMs[202].Anotherresearcheffort,
”Stealing the Decoding Algorithms of Language Models,” delves into the technical
intricacies of how prompts can be exploited to steal decoding algorithms, further
showcasing the vulnerability of LLMs to such attacks [202].
The effectivenessof these attacks underscoresthe urgent need for robustdefenses.
Proposed countermeasures include limiting the number of queries a single user can
make, implementing anomaly detection to identify suspicious querying patterns, and
using defensive perturbations to mislead potential attackers [203].
7.2.4 Backdoor Threats
Backdoor threats involve embedding hidden vulnerabilities within a model that can
beactivatedbyspecificprompts.Thesebackdoorscanbeintroducedduringthetraining process, often through manipulated training data, and remain dormant until the
trigger prompt is presented. For LLMs, a backdoor could be a particular phrase or
pattern that, when encountered, causes the model to generate a pre-defined, often
malicious output. This poses a significant security risk, as backdoors can be difficult
to detect and may be exploited to produce harmful responses or leak sensitive information [204–209]. The covert nature of backdoor threats makes them a formidable
challenge, highlighting the need for robust prompt engineering practices to identify
and mitigate these vulnerabilities [210].
Prompt engineering plays a crucial role in both the identification and prevention
of these vulnerabilities. Carefully designed prompts can be used to test LLMs for
susceptibility to adversarial attacks, data poisoning, and backdoor activations, thus
ensuring more secure deployment of these powerful models.
28

<!-- Page 29 -->

7.2.5 Data Poisoning
Data poisoning involves the injection of malicious data into the training set, which
compromises the integrity of the model. This type of attack can significantly distort
the learning process, leading to erroneous outputs once the model is deployed. In
LLMs, data poisoning can be especially insidious as it may go undetected during the
trainingphase.Forinstance,anattackermightinsertmisleadingorharmfuldatainto
thelargecorpususedtotrainanLLM,causingthemodeltolearnandreproducethese
inaccuracies when prompted. The implications of data poisoning are far-reaching,
affectingsectorsthatrelyonaccuratedataanalysisandgeneration,suchashealthcare,
finance, and legal services [211]. Prompt engineering practices must be meticulously
monitored to prevent the inadvertent inclusion of poisoned data that could later be
exploited.
7.3 Prompt Engineering as a Double-Edged Sword
While prompt engineering has significantly enhanced the functionality and versatility of LLMs, it also poses substantial risks if mismanaged. Poorly designed prompts
canintroduceorexacerbatesecurityvulnerabilities,leadingtounintendedandpotentiallyharmfuloutputs[178].Thisdualnatureofpromptengineering—capableofboth
enhancingandcompromisingLLMperformance—highlightsitsroleasadouble-edged
swordinthedeploymentofAItechnologies.Recentadvancementsinpromptengineering have demonstrated its power to unlock new capabilities in LLMs, but they also
underscoretheneedforrobustandsecuredesignpractices.AsLLMsbecomeincreasinglyintegratedintocriticalsystemsandservices,ensuringthatpromptsarecarefully
and securely crafted is essential to mitigating risks and maximizing the benefits of
these advanced models [212].
7.3.1 Impact of Poorly Designed Prompts on Security
PoorlydesignedpromptscansignificantlyexacerbatesecurityvulnerabilitiesinLLMs.
Adversarialprompts,forinstance,canbecraftedtoexploitspecificweaknessesinthe
model,leadingtounintendedorharmfuloutputs.Thesevulnerabilitiesareparticularly
critical in applications where accuracy and reliability are paramount, such as legal
document analysis or automated customer service [7].
Poorly designed prompts can make LLMs susceptible to various types of attacks,
including prompt injection and prompt leaking. Prompt injection attacks involve
inserting malicious inputs into prompts to manipulate the model’s output, which can
result in the generation of harmful or misleading information. For example, a malicious actor could craft a prompt that subtly alters the model’s response in a way
that promotes false information or biases [178]. Prompt leaking, on the other hand,
occurs when sensitive or proprietary information embedded in prompts is exposed,
jeopardizing the security and privacy of applications that rely on LLMs [213].
Prompt engineering plays acrucial rolein both mitigatingand exacerbatingthese
vulnerabilities. Effective prompt engineering involves designing prompts that minimize the risk of exploitation while maximizing the accuracy and reliability of the
model’s outputs. This includes the use of techniques such as input sanitization, context validation, and adversarial training to enhance the model’s robustness against
malicious inputs. Conversely, inadequate prompt engineering can inadvertently introduce vulnerabilities, as poorly structured prompts may fail to account for potential
security risks or edge cases, leaving the model exposed to exploitation [211].
In summary, poorly designed prompts can significantly exacerbate security vulnerabilities in LLMs, leading to adverse outcomes such as adversarial attacks, data
poisoning,andbackdoorthreats.Theroleofpromptengineeringisparamountinmitigatingtheserisks,ensuringthatpromptsarecarefullycraftedtoenhancethemodel’s
security and reliability. As LLMs become increasingly integrated into critical applications,theneedforrobustandsecurepromptengineeringpracticesbecomesevermore
pressing. Future research and development should focus on advancing these practices
to protect LLMs from emerging threats and ensure their safe deployment.
29

<!-- Page 30 -->

7.3.2 Enhancing LLM Security Through Adversarial Training and

### Robust Prompt Design

Adversarial example generation is a fundamental technique in AI security, designed
to test and enhance the robustness of machine learning models. By creating inputs
that intentionally mislead models into making incorrect predictions, researchers can
identifyvulnerabilitiesanddevelopstrategiestomitigatethem.Thisprocessisessentialforensuringthatmodelscanwithstandmaliciousattacksandfunctionreliablyin
real-world scenarios [178]. While direct research on prompt-based adversarial example generation is limited, prompt engineering remains a critical tool in testing model
robustness. By designing prompts that subtly alter input data, researchers can simulateadversarialconditionsandobservehowmodelsrespond.Forexample,ambiguous
or misleading prompts can reveal how susceptible a model is to producing biased or
incorrect outputs, thereby identifying potential weaknesses [214].
Adversarial training, which involves training models on adversarial examples, has
proven effective in enhancing model robustness. Studies have shown that models
exposedtoavarietyofadversarialinputsduringtrainingarebetterequippedtohandle
unexpected or malicious data. This method improves the resilience of models against
attacks and enhances their overall reliability [195].
For instance, research has demonstrated that incorporating adversarial examples generated through prompt manipulation can significantly bolster a model’s
defenses.Bycontinuouslyrefiningpromptsandgeneratingdiverseadversarialscenarios, researchers can develop comprehensive training datasets that prepare models for
a wide range of challenges [215].
To maximize the effectiveness of adversarial training, integrating robust prompt
designisessential.Thisinvolvescreatingpromptsthatnotonlytestthemodel’slimits
but also enhance its ability to learn from adversarial conditions. Techniques such as
mask filling, where portions of text are strategically manipulated, can be used to
generate adversarial examples that expose and address vulnerabilities in the model
[181].
In conclusion, while the direct focus on prompt-based adversarial example generation might be limited, the broader application of adversarial training and robust
prompt design remains critical in enhancing LLM security. Future research should
continue to explore innovative methods for integrating prompt engineering into
adversarial training frameworks to ensure the safe and reliable deployment of LLMs.
8 Prospective methodologies
Several key developments on the horizon promise to substantially advance prompt
engineering capabilities. In the following section, some of the most significant trajectories would be analyzed that are likely to shape the future of prompt engineering.
By anticipating where prompt engineering is headed, developments in this field can
be proactively steered toward broadly beneficial outcomes.
8.1 Better understanding of structures
One significant trajectory about the future of prompt engineering that emerges is
the importance of better understanding the underlying structures of AI models. This
understanding is crucial to effectively guide these models through prompts and to
generate outputs that are more closely aligned with user intent.
At the heart of most AI models, including GPT-4, are complex mechanisms
designed to understand and generate human language. The interplay of these mechanisms forms the “structure” of these models. Understanding this structure involves
unraveling the many layers of neural networks, the various attention mechanisms at
work, and the role of individual nodes and weights in the decision-making process
of these models [216]. Deepening our understanding of these structures could lead to
substantialimprovementsinpromptengineering.Themisunderstandingofthemodel
may cause a lack of reproducibility [217]. By understanding how specific components
30

<!-- Page 31 -->

of the model’s structure influence its outputs, we could design prompts that more
effectively exploit these components.
Furthermore, a comprehensive grasp of these structures could shed light on the
shortcomingsofcertainpromptsandguidetheirenhancement.Frequently,theunderlying causes for a prompt’s inability to yield the anticipated output are intricately
linked to the model’s architecture. For example, [29] found evidence of limitations in
previous prompt models and questioned how much these methods truly understood
the model.
Exploration of AI model architectures remains a vibrant research domain, with
numerous endeavors aimed at comprehending these sophisticated frameworks. A
notableinstanceisDeepMind’s“CausalTransformer”model[218],designedtoexplicitlydelineatecausalrelationshipswithindata.Thisrepresentsastridetowardsamore
profoundunderstandingofAImodelarchitectures,withthepotentialtohelpusdesign
more efficient prompts.
Furthermore, a more comprehensive grasp of AI model architectures would also
yield advancements in explainable AI. Beyond better prompt engineering, this would
also foster greater trust in AI systems and promote their integration across diverse
industries [219]. For example, while AI is transforming the financial sector, encompassing areas such as customer service, fraud detection, risk management, credit
assessments,andhigh-frequencytrading,severalchallenges,particularlythoserelated
to transparency, are emerging alongside these advancements [220, 221]. Another
example is medicine, where AI’s transformative potential faces similar challenges
[222, 223].
Inconclusion,thetrajectorytowardabetterunderstandingofAImodelstructures
promises to bring significant advancements in prompt engineering. As we research
deeperintotheseintricatesystems,weshouldbeabletocraftmoreeffectiveprompts,
understand the reasons behind prompt failures, and enhance the explainability of AI
systems. This path holds the potential for transforming how we interact with and
utilize AI systems, underscoring its importance in the future of prompt engineering.
8.2 Agent for AIGC tools
TheconceptofAIagentshasemergedasapotentialtrajectoryinAIresearch[224].In
this brief section, we explore the relationship between agents and prompt engineering
and project how agents might influence the future trajectory of AI-generated content
(AIGC) tools. By definition, an AI agent comprises large models, memory, active
planning, and tool use. AI agents are capable of remembering and understanding a
vast array of information, actively planning and strategizing, and effectively using
various tools to generate optimal solutions within complex problem spaces [225].
The evolution of AI agents can be delineated into five distinct phases: models, prompt templates, chains, agents, and multi-agents. Each phase carries its
specific implications for prompt engineering. Foundational models, exemplified by
architectures such as GPT-4, underpin the realm of prompt engineering.
In particular, prompt templates offer an effective way of applying prompt engineeringinpractice[30].Byusingthesetemplates,wecancreatestandardizedprompts
to guide large models, making the generated output more aligned with the desired
outcome. The usage of prompt templates is a crucial step towards enabling AI agents
to better understand and execute user instructions.
AIagentsamalgamatethesemethodologiesandtoolsintoanadaptiveframework.
Possessing the capability to autonomously modulate their behaviors and strategies,
they strive to optimize both efficiency and precision in task execution. A salient challenge for prompt engineering emerges: devising and instituting prompts that adeptly
steer AI agents toward self-regulation [29].
Inconclusion,theintroductionofagent-basedparadigmsheraldsanoveltrajectory
for the evolution of AIGC tools. This shift necessitates a reevaluation of established
practices in prompt engineering and ushers in fresh challenges associated with the
design, implementation, and refinement of prompts.
31

<!-- Page 32 -->

9 Conclusion
In conclusion, prompt engineering has established itself as an essential technique for
optimizingtheperformanceofLMs.Byemployingfoundationalmethodssuchasclear
instructionsanditerativerefinement,alongside advancedmethodologieslikeChainof
Thought and Self-consistency, the capabilities of LMs are significantly enhanced. For
multimodal models, innovative strategies such as Multi-modal Prompt Learning and
ContextOptimizationensureeffectiveintegrationandoptimizationofvisualandtextualdata.Theefficacyofthesemethodsisrigorouslyassessedthroughbothsubjective
andobjectiveevaluations,confirmingtheirimpactacrossdiverseapplications,including education, content creation, and programming. Additionally, prompt engineering
plays a crucial role in fortifying LM security, identifying vulnerabilities, and mitigating risks through adversarial training and robust prompt design. Looking ahead,
futureadvancementswillfocusonadeeperunderstandingofAImodelstructuresand
the development of AI agents, further elevating the sophistication and capability of
AI systems. This comprehensive review underscores the transformative potential of
prompt engineering in advancing AI capabilities, providing a structured framework
for future research and applications.
10 Acknowledgement
This work was funded by the Natural Science Foundation of China (12271047);
Guangdong Provincial Key Laboratory of Interdisciplinary Research and Application for Data Science, BNU-HKBU United International College (2022B1212010006);
UIC research grant (R0400001-22; UICR0400008-21; UICR0700041-22; R72021114);
Guangdong College Enhancement and Innovation Program (2021ZDZX1046).

### References

[1] McCarthy J, Minsky ML, Rochester N, Shannon CE. A Proposal for the DartmouthSummerResearchProjectonArtificialIntelligence,August31,1955. AI
Magazine. 2006 Dec;27(4):12. https://doi.org/10.1609/aimag.v27i4.1904.
[2] Rumelhart DE, Hinton GE, Williams RJ. Learning representations by backpropagating errors. Nature. 1986;323:533–536.
[3] Krizhevsky A, Sutskever I, Hinton GE. ImageNet classification with deep convolutional neural networks. Commun ACM. 2017 may;60(6):84–90. https:
//doi.org/10.1145/3065386.
[4] Devlin J, Chang MW, Lee K, Toutanova K. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In: Burstein J, Doran C,
Solorio T, editors. Proceedings of the 2019 Conference of the North American
Chapter of the Association for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers). Minneapolis, Minnesota:
Association for Computational Linguistics; 2019. p. 4171–4186. Available from:
https://aclanthology.org/N19-1423.
[5] Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, et al.
Attention is all you need. In: Proceedings of the 31st International Conference
on Neural Information Processing Systems. NIPS’17; 2017. p. 6000–6010.
[6] Bender EM, Gebru T, McMillan-Major A, Shmitchell S. On the dangers of
stochastic parrots: can language models be too big? In: Proceedings of the
2021 ACM Conference on Fairness, Accountability, and Transparency; 2021. p.
610–623.
32

<!-- Page 33 -->

[7] Brown TB, Mann B, Ryder N, Subbiah M, Kaplan J, Dhariwal P, et al.
language models Are Few-Shot Learners. In: Proceedings of the 34th InternationalConferenceonNeuralInformationProcessingSystems.NIPS’20;2020.p.
1877–1901.
[8] Hulbert D.: Tree of knowledge: ToK aka Tree of Knowledge dataset for Large
Language Models LLM. Accessed: 2023-8-15. figshare https://github.com/
dave1010/tree-of-thought-prompting.
[9] Anthropic.: Claude2. Anthropic. Accessed: 2023-7-11. figshare https://www.
anthropic.com.
[10] Touvron H, Martin L, Stone K, Albert P, Almahairi A, Babaei Y, et al. Llama
2: open foundation and fine-tuned chat models; 2023. ArXiv:2307.09288.
[11] Sarkhel R, Huang B, Lockard C, Shiralkar P. Self-training for label-efficient
information extraction from semi-structured web-pages. Proceedings of the
VLDB Endowment. 2023;16(11):3098–3110.
[12] Ramesh A, Pavlov M, Goh G, Gray S, Voss C, Radford A, et al. Zero-Shot
Text-to-Image Generation. arXiv preprint arXiv:210212092. 2021;.
[13] Marcus G, Davis E, Aaronson S. A very preliminary analysis of DALL-E 2.
arXiv preprint arXiv:220413807. 2022;.
[14] OpenAI.: DALL·E: Creating images from text. https://openai.com/index/
dall-e/.
[15] Radford A, Kim JW, Hallacy C, Ramesh A, Goh G, Agarwal S, et al. Learning
Transferable Visual Models From Natural Language Supervision. In: International Conference on Machine Learning; 2021. Available from: https://api.
semanticscholar.org/CorpusID:231591445.
[16] OpenAI. GPT-4 Technical Report; 2023. ArXiv:2303.08774.
[17] Google.: Google Gemini: Next-Generation Model. Available from: https://blog.
google/technology/ai/google-gemini-next-generation-model-february-2024/
# sundar-note.
[18] AI M.: Llama 3. GitHub. Computer software. Available from: https://github.
com/meta-llama/llama3.
[19] AI M.: Llama 3. Model description. Available from: https://huggingface.co/
meta-llama.
[20] Anthropic.:Claude3Model.Availablefrom:https://www.anthropic.com/news/
claude-3-family.
[21] Moore O.: Announcing GPT-4o in the API! Accessed: 2024-05-22. Available
from: https://community.openai.com/t/announcing-gpt-4o-in-the-api/744700.
[22] ChengL,LiX,BingL. IsGPT-4agooddataanalyst?;2023. ArXiv:2305.15038.
[23] Razumovskaia E, Maynez J, Louis A, Lapata M, Narayan S. Little red riding
hood goes around the globe: crosslingual story planning and generation with
large language models; 2022. ArXiv:2212.10471.
[24] Manning S, Mishkin P, Hadfield G, Eloundou T, Eisner E. A research agenda
for assessing the economic impacts of code generation models; 2022.
33

<!-- Page 34 -->

[25] Choudhury A, Asan O, et al. Role of artificial intelligence in patient
safety outcomes: systematic literature review. JMIR medical informatics.
2020;8(7):e18599.
[26] Baidoo-Anu D, Ansah LO. Education in the era of generative artificial intelligence (AI): understanding the potential benefits of ChatGPT in promoting
teaching and learning. Journal of AI. 2023;7(1):52–62.
[27] KaddourJ,HarrisJ,MozesM,BradleyH,RaileanuR,McHardyR. Challenges
and applications of large language models; 2023. ArXiv:2307.10169.
[28] LuY,BartoloM,MooreA,RiedelS,StenetorpP.Fantasticallyorderedprompts
and where to find them: overcoming few-shot prompt order sensitivity. In:
Proceedings of the 60th Annual Meeting of the Association for Computational
Linguistics; 2022. p. 8086–8098.
[29] Webson A, Pavlick E. Do prompt-based models really understand the meaning
oftheirprompts? In:Proceedingsofthe2022ConferenceoftheNorthAmerican
Chapter of the Association for Computational Linguistics: Human Language
Technologies; 2022. p. 2300–2344.
[30] Wei J, Wang X, Schuurmans D, Bosma M, Ichter B, Xia F, et al. Chain-ofthought prompting elicits reasoning in large language models. In: Advances in
Neural Information Processing Systems. vol. 35; 2022. p. 24824–24837.
[31] Wang X, Wei J, Schuurmans D, Le QV, Chi EH, Narang S, et al. Selfconsistency improves chain of thought reasoning in language models. In:
Eleventh International Conference on Learning Representations; 2023. .
[32] Shanahan M, McDonell K, Reynolds L. Role-play with large language models;

## ArXiv:2305.16367.

[33] Maynez J, Narayan S, Bohnet B, McDonald R. On faithfulness and factuality
in abstractive summarization. In: Proceedings of the 58th Annual Meeting of
the Association for Computational Linguistics; 2020. p. 1906–1919.
[34] Bubeck S, Chandrasekaran V, Eldan R, Gehrke J, Horvitz E, Kamar E, et al.
Sparks of artificial general intelligence: early experiments with GPT-4; 2023.
ArXiv:2303.12712.
[35] Yong G, Jeon K, Gil D, Lee G. Prompt engineering for zero-shot and few-shot
defect detection and classification using a visual-language pretrained model.
Computer-Aided Civil and Infrastructure Engineering. 2022;38(11):1536–1554.
[36] Christiano PF, Leike J, Brown T, Martic M, Legg S, Amodei D. Deep reinforcement learning from human preferences. Advances in neural information
processing systems. 2017;30.
[37] Stiennon N, Ouyang L, Wu J, Ziegler D, Lowe R, Voss C, et al. Learning to
summarize with human feedback. Advances in Neural Information Processing
Systems. 2020;33:3008–3021.
[38] Radford A, Narasimhan K, Salimans T, Sutskever I, et al. Improving language understanding by generative pre-training; 2018.
Https://openai.com/research/language-unsupervised.
[39] Radford A, Wu J, Child R, Luan D, Amodei D, Sutskever I, et al.: Language models are unsupervised multitask learners. Assessed: 2019-02-07.
figshare https://cdn.openai.com/better-language-models/language models are
34

<!-- Page 35 -->

unsupervised multitask learners.pdf.
[40] Holtzman A, Buys J, Du L, Forbes M, Choi Y. The curious case of neural text
degeneration. In:InternationalConferenceonLearningRepresentations;2020..
[41] WelleckS,KulikovI,RollerS,DinanE,ChoK,WestonJ.Neuraltextgeneration
with unlikelihood training; 2019. ArXiv:1908.04319.
[42] XuX,TaoC,ShenT,XuC,XuH,LongG,etal.Re-readingimprovesreasoning
in language models; 2023. ArXiv:2309.06275.
[43] YanSongS,JingLiTencentA. JointlearningembeddingsforChinesewordsand
theircomponentsvialadderstructurednetworks.In:ProceedingsoftheTwenty-
Seventh International Joint Conference on Artifificial Intelligence (IJCAI-18);
2018. p. 4375–4381.
[44] Luo L, Ao X, Song Y, Li J, Yang X, He Q, et al. Unsupervised neural aspect
extraction with sememes. In: IJCAI; 2019. p. 5123–5129.
[45] Yang M, Qu Q, Tu W, Shen Y, Zhao Z, Chen X. Exploring human-like reading strategy for abstractive text summarization. In: Proceedings of the AAAI
conference on artificial intelligence. vol. 33; 2019. p. 7362–7369.
[46] ZhangZ,GaoJ,DhaliwalRS,Jia-JunLiT. VISAR:ahuman-AIargumentative
writing assistant with visual programming and rapid draft prototyping; 2023.
ArXiv:2304.07810.
[47] Buren DV. Guided scenarios with simulated expert personae: a remarkable
strategy to perform cognitive work; 2023. ArXiv:2306.03104.
[48] OpenAI.: Tactic: use delimiters to clearly indicate distinct parts of the input. Accessed: 2023-09-01. figshare
https://platform.openai.com/docs/guides/gpt-best-practices/
tactic-use-delimiters-to-clearly-indicate-distinct-parts-of-the-input.
[49] LoganIVR,Balaˇzevi´cI,WallaceE,PetroniF,SinghS,RiedelS. Cuttingdown
onpromptsandparameters:simplefew-shotlearningwithlanguagemodels. In:
Findings of the Association for Computational Linguistics: ACL 2022; 2022. p.
2824–2835.
[50] Shyr C, Hu Y, Harris PA, Xu H. Identifying and extracting rare disease
phenotypes with Large language models; 2023. ArXiv:2306.12656.
[51] Reynolds L, McDonell K. Prompt programming for large language models: beyond the few-shot paradigm. In: Extended Abstracts of the 2021 CHI
Conference on Human Factors in Computing Systems; 2021. p. 1–7.
[52] LiuJ,GardnerM,CohenSB,LapataM. Multi-stepinferenceforreasoningover
paragraphs; 2020. ArXiv:2004.02995.
[53] Ackley DH, Hinton GE, Sejnowski TJ. A learning algorithm for Boltzmann
machines. Cognitive Science. 1985;9(1):147–169.
[54] Ficler J, Goldberg Y. Controlling linguistic style aspects in neural language
generation. In: Proceedings of the Workshop on Stylistic Variation; 2017. p.
94–104.
[55] Xu C, Guo D, Duan N, McAuley J. RIGA at SemEval-2023 Task 2: NER
enhanced with GPT-3. In: Proceedings of the 17th International Workshop on
Semantic Evaluation (SemEval-2023); 2023. p. 331–339.
35

<!-- Page 36 -->

[56] Wu S, Shen EM, Badrinath C, Ma J, Lakkaraju H. Analyzing chain-of-thought
prompting in Large language models via gradient-based feature Attributions;

## ArXiv:2307.13339.

[57] Zhang Z, Zhang A, Li M, Smola A. Automatic chain of thought prompting
in Large language models. In: Eleventh International Conference on Learning
Representations; 2023. .
[58] Lewkowycz A, Andreassen A, Dohan D, Dyer E, Michalewski H, Ramasesh V,
et al. Solving quantitative reasoning problems with language models. Advances
in Neural Information Processing Systems. 2022;35:3843–3857.
[59] Zhou H, Nova A, Larochelle H, Courville A, Neyshabur B, Sedghi H. Teaching
Algorithmic Reasoning via In-context Learning; 2022. ArXiv:2211.09066.
[60] Lee N, Sreenivasan K, Lee JD, Lee K, Papailiopoulos D. Teaching arithmetic
to small transformers; 2023. ArXiv:2307.03381.
[61] WeiJ,WangX,SchuurmansD,BosmaM,IchterB,XiaF,etal. Largelanguage
models perform diagnostic reasoning. In: Eleventh International Conference on
Learning Representations; 2022. .
[62] Zhang H, Parkes DC. Chain-of-thought reasoning is a policy improvement
operator; 2023. ArXiv:2309.08589.
[63] Cobbe K, Kosaraju V, Bavarian M, Chen M, Jun H, Kaiser L, et al. Training
verifiers to solve math word problems; 2021. ArXiv:2110.14168.
[64] Huang S, Dong L, Wang W, Hao Y, Singhal S, Ma S, et al. Language is not all
you need: aligning perception with language models; 2023. ArXiv:2302.14045.
[65] Kojima T, Gu SS, Reid M, Matsuo Y, Iwasawa Y. Large language models
are zero-shot reasoners. Advances in Neural Information Processing Systems.
2022;35:22199–22213.
[66] Del M, Fishel M. True detective: a deep abductive reasoning benchmark
undoable for GPT-3 and challenging for GPT-4. In: Proceedings of the 12th
JointConferenceonLexicalandComputationalSemantics(*SEM2023);2023..
[67] OuyangL,WuJ,JiangX,AlmeidaD,WainwrightC,MishkinP,etal. Training
languagemodelstofollowinstructionswithhumanfeedback.AdvancesinNeural
Information Processing Systems. 2022;35:27730–27744.
[68] Saparov A, He H. Language models are greedy reasoners: a systematic formal
analysis of chain-of-thought; 2022. ArXiv:2210.01240.
[69] Tafjord O, Dalvi B, Clark P. ProofWriter: generating implications, proofs, and
abductive statementsover natural language. In: Findingsof the Association for
Computational Linguistics: ACL-IJCNLP 2021; 2021. p. 3621–3634.
[70] ChowdheryA,NarangS,DevlinJ,BosmaM,MishraG,RobertsA,etal. Palm:
scaling language modeling with pathways; 2022. ArXiv:2204.02311.
[71] Fan A, Lewis M, Dauphin Y. Hierarchical neural story generation. In: Proceedings of the 56th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers); 2018. p. 889–898.
[72] HoltzmanA,BuysJ,ForbesM,BosselutA,GolubD,ChoiY. Learningtowrite
withcooperativediscriminators. In:Proceedingsofthe56thAnnualMeetingof
the Association for Computational Linguistics (Volume 1: Long Papers); 2018.
36

<!-- Page 37 -->

p. 1638–1649.
[73] Huang J, Gu SS, Hou L, Wu Y, Wang X, Yu H, et al. Large language models
can self-improve; 2022. ArXiv:2210.11610.
[74] ShumK,DiaoS,ZhangT. Automaticpromptaugmentationandselectionwith
chain-of-thought from labeled data; 2023. ArXiv:2302.12822.
[75] Khalifa M, Logeswaran L, Lee M, Lee H, Wang L. Discriminator-guided multistep reasoning with language models; 2023. ArXiv:2305.14934.
[76] Liu J, Liu A, Lu X, Welleck S, West P, Le Bras R, et al. Generated knowledgepromptingforcommonsensereasoning. In:Proceedingsofthe60thAnnual
Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers); 2022. p. 3154–3169.
[77] Zhou D, Sch¨arli N, Hou L, Wei J, Scales N, Wang X, et al. Least-to-most
prompting enables complex reasoning in Large language models. In: Eleventh
International Conference on Learning Representations; 2023. .
[78] Yao S, Yu D, Zhao J, Shafran I, Griffiths TL, Cao Y, et al. Tree of thoughts:
deliberateproblemsolvingwithlargelanguagemodels;2023. ArXiv:2305.10601.
[79] LongJ. Largelanguagemodelguidedtree-of-thought;2023. ArXiv:2305.08291.
[80] Besta M, Blach N, Kubicek A, Gerstenberger R, Gianinazzi L, Gajda J, et al.
Graphofthoughts:solvingelaborateproblemswithlargelanguagemodels;2023.
ArXiv:2308.09687.
[81] Wang L, Ma C, Feng X, Zhang Z, Yang H, Zhang J, et al. A survey on large
language model based autonomous agents; 2023. ArXiv:2308.11432.
[82] Greyling C.: 12 Prompt Engineering Techniques. Available from: https://
cobusgreyling.medium.com/12-prompt-engineering-techniques-644481c857aa.
[83] Vinija.: Prompt Engineering. Available from: https://vinija.ai/nlp/
prompt-engineering/.
[84] Badhan M.: Advanced Prompt Engineering Techniques. Accessed:
2024-05-22. Available from: https://www.mercity.ai/blog-post/
advanced-prompt-engineering-techniques.
[85] Pakhale T.: A Guide to Prompt Engineering: From Zero Shot to
Chain of Thought. Available from: https://www.e2enetworks.com/blog/
a-guide-to-prompt-engineering-from-zero-shot-to-chain-of-thought.
[86] Hedlund A.: Exploring Active Prompting: A Comprehensive Guide for the
FutureofPromptEngineering. Availablefrom:https://my.ai.se/resources/2343.
[87] MathAware.: Revolutionizing AI: The Future of Prompt Engineering with Active-Prompt. Available from: https://www.mathaware.org/
prompt-engineering-active-prompt-2/.
[88] Perdigao L.: Mastering AI Conversations: The Art of Prompt
Engineering. Available from: https://leoneperdigao.medium.com/
mastering-ai-conversations-the-art-of-prompt-engineering-59a148b879fa.
[89] YaoS,ZhaoJ,YuD,DuN,ShafranI,NarasimhanK,etal.:ReAct:Synergizing
Reasoning and Acting in Language Models.
37

<!-- Page 38 -->

[90] Li A.: ReAct: A New Framework for Prompt Engineering in Large
Language Models. Available from: https://www.perxeive.com/blog/
react-a-new-framework-for-prompt-engineering-in-large-language-models.
[91] Roberts A.: How to ReAct To Simple AI Agents. Available from: https://arize.
com/blog-course/react-agent-llm/.
[92] McKenney B.: Teaching LLMs to Think and Act: ReAct Prompt Engineering.
Accessed:2024-05-22. Availablefrom:https://medium.com/@bryan.mckenney/
teaching-llms-to-think-and-act-react-prompt-engineering-eef278555a2e.
[93] Lee K, Firat O, Agarwal A, Fannjiang C, Sussillo D. Hallucinations in neural
machine translation; 2018.
[94] Ji Z, Lee N, Frieske R, Yu T, Su D, Xu Y, et al. Survey of hallucination in
natural language generation. ACM Computing Surveys. 2023;55(12):1–38.
[95] Lazaridou A, Gribovskaya E, Stokowiec W, Grigorev N. Internet-augmented
languagemodelsthroughfew-shotpromptingforopen-domainquestionanswering; 2022. ArXiv:2203.05115.
[96] Jiang Z, Xu FF, Gao L, Sun Z, Liu Q, Dwivedi-Yu J, et al. Active retrieval
augmented generation; 2023. ArXiv:2305.06983.
[97] RamO,LevineY,DalmedigosI,MuhlgayD,ShashuaA,Leyton-BrownK,etal.
In-context retrieval-augmented language models; 2023. ArXiv:2302.00083.
[98] ShusterK,PoffS,ChenM,KielaD,WestonJ. Retrievalaugmentationreduces
hallucination in conversation; 2021. ArXiv:2104.07567.
[99] Lewis P, Perez E, Piktus A, Petroni F, Karpukhin V, Goyal N, et al. Retrievalaugmented generation for knowledge-intensive nlp tasks. Advances in Neural
Information Processing Systems. 2020;33:9459–9474.
[100] Izacard G, Grave E. Leveraging passage retrieval with generative models for
open domain question answering; 2020. ArXiv:2007.01282.
[101] LewisM,LiuY,GoyalN,GhazvininejadM,MohamedA,LevyO,etal. BART:
denoising sequence-to-sequence pre-training for natural language generation,
translation, and comprehension. In: Proceedings of the 58th Annual Meeting of
the Association for Computational Linguistics; 2020. p. 7871–7880.
[102] Raffel C, Shazeer N, Roberts A, Lee K, Narang S, Matena M, et al. Exploring
the limits of transfer learning with a unified text-to-text transformer. Journal
of Machine Learning Research. 2020;21(1):5485–5551.
[103] Roller S, Dinan E, Goyal N, Ju D, Williamson M, Liu Y, et al. Recipes for
building an open-domain chatbot. In: Proceedings of the 16th Conference of
the European Chapter of the Association for Computational Linguistics: Main
Volume; 2021. p. 300–325.
[104] Dhuliawala S, Komeili M, Xu J, Raileanu R, Li X, Celikyilmaz A, et al.
Chain-of-verification reduces hallucination in large language models; 2023.
ArXiv:2309.11495.
[105] OpenAI.: ChatGPT plugins. Accessed: 2023-10-15. figshare https://openai.
com/blog/chatgpt-plugins.
[106] Bisson S.: Microsoft build 2023: Microsoft extends its copilots with open standard plugins. Accessed: 2023-05-25. figshare https://www.techrepublic.com/
38

<!-- Page 39 -->

article/microsoft-extends-copilot-with-open-standard-plugins/.
[107] Ng A.: ChatGPT prompt engineering for developers. Accessed:
2023-07-18. figshare https://www.deeplearning.ai/short-courses/
chatgpt-prompt-engineering-for-developers/.
[108] Roller S, Dinan E, Goyal N, Ju D, Williamson M, Liu Y, et al. Recipes for
building an open-domain chatbot. In: Proceedings of the 16th Conference of
the European Chapter of the Association for Computational Linguistics: Main
Volume; 2021. p. 300–325.
[109] whatplugin.: Prompt enhancer & ChatGPT plugins for AI development tools
like prompt enhancer. Accessed: 2023-09-14. figshare https://www.whatplugin.
ai/plugins/prompt-enhancer.
[110] : AISEO. Accessed: 2023-8-15. figshare https://aiseo.ai/.
[111] forSearchEnginesC.:PromptperfectpluginforChatGPT. Accessed:2023-10-
15. figshare https://chatonai.org/prompt-perfect-chatgpt-plugin.
[112] Prompt Perfect.: Terms of service. Accessed: 2023-09-20. figshare https://
promptperfect.xyz/static/terms.html.
[113] Yin S, Fu C, Zhao S, Li K, Sun X, Xu T, et al.: A Survey on Multimodal Large
Language Models.
[114] Moveworks.: Multimodal Language Models. Available from:
https://www.moveworks.com/us/en/resources/ai-terms-glossary/
multimodal-language-models0.
[115] Miquido.: Multimodal Large Language Models Definition. Available from: https://www.miquido.com/ai-glossary/
multimodal-large-language-models-definition/.
[116] Zapier.: What Is Multimodal AI? Available from: https://zapier.com/blog/
multimodal-ai/.
[117] Moveworks.: What is a Multimodal Language Model? Available
from: https://www.moveworks.com/us/en/resources/ai-terms-glossary/
multimodal-language-models0.
[118] Miquido.: Understanding Multimodal Large Language Models. Available from: https://www.miquido.com/ai-glossary/
multimodal-large-language-models-definition/.
[119] Amanatulla.: The Evolution and Promise of Multimodal Large Language Models. Available from: https://medium.com/@amanatulla1606/
the-evolution-and-promise-of-multimodal-large-language-models-ec76c65246e4.
[120] Khattak MU, Rasheed H, Maaz M, Khan S, Khan FS.: MaPLe: Multi-modal
Prompt Learning.
[121] Ma S, Xie CW, Wei Y, Sun S, Fan J, Bao X, et al.: Understanding the Multimodal Prompts of the Pre-trained Vision-Language Model.
[122] Gu J, Han Z, Chen S, Beirami A, He B, Zhang G, et al.: A Systematic Survey
of Prompt Engineering on Vision-Language Foundation Models.
[123] Zhou K, Yang J, Loy CC, Liu Z. Learning to Prompt for Vision-Language
Models. International Journal of Computer Vision. 2022 Jul;130(9):2337–2348.
39

<!-- Page 40 -->

https://doi.org/10.1007/s11263-022-01653-1.
[124] Ma C, Liu Y, Deng J, Xie L, Dong W, Xu C.: Understanding and Mitigating
Overfitting in Prompt Tuning for Vision-Language Models.
[125] Agnolucci L, Baldrati A, Todino F, Becattini F, Bertini M, Bimbo AD.: ECO:
Ensembling Context Optimization for Vision-Language Models.
[126] Chowdhury S, Nag S, Manocha D. APoLLo : Unified Adapter and Prompt
Learning for Vision Language Models. In: Bouamor H, Pino J, Bali K, editors.
Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing. Singapore: Association for Computational Linguistics; 2023.
p.10173–10187.Availablefrom:https://aclanthology.org/2023.emnlp-main.629.
[127] Zhou K, Yang J, Loy CC, Liu Z.: Conditional Prompt Learning for Vision-
Language Models.
[128] Khattak MU, Wasim ST, Naseer M, Khan S, Yang MH, Khan FS.: Selfregulating Prompts: Foundational Model Adaptation without Forgetting.
[129] Shukor M, Couairon G, Cord M.: Efficient Vision-Language Pretraining with
Visual Concepts and Hierarchical Alignment.
[130] Ma C, Yang Y, Wang Y, Zhang Y, Xie W.: Open-vocabulary Semantic
Segmentation with Frozen Vision-Language Models.
[131] Wang J, Hu X, Zhang P, Li X, Wang L, Zhang L, et al.: MiniVLM: A Smaller
and Faster Vision-Language Model.
[132] Wu J, Li X, Xu S, Yuan H, Ding H, Yang Y, et al.: Towards Open Vocabulary
Learning: A Survey.
[133] Awal R, Zhang L, Agrawal A.: Investigating Prompting Techniques for Zeroand Few-Shot Visual Question Answering.
[134] Zhang R, Wei Z, Fang R, Gao P, Li K, Dai J, et al.: Tip-Adapter: Training-free
Adaption of CLIP for Few-shot Classification.
[135] DengM,WangJ,HsiehCP,WangY,GuoH,ShuT,etal. RLPrompt:optimizing discrete text prompts with reinforcement learning. In: Proceedings of the
2022 Conference on Empirical Methods in Natural Language Processing; 2022.
p. 3369–3391.
[136] Wen Y, Jain N, Kirchenbauer J, Goldblum M, Geiping J, Goldstein
T. Hard Prompts Made Easy: Gradient-Based Discrete Optimization
for Prompt Tuning and Discovery. In: Oh A, Naumann T, Globerson
A, Saenko K, Hardt M, Levine S, editors. Advances in Neural Information Processing Systems. vol. 36. Curran Associates, Inc.; 2023. p. 51008–

## Available from: https://proceedings.neurips.cc/paper files/paper/2023/

file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf.
[137] Ma X, ZHANG J, Guo S, Xu W. SwapPrompt: Test-Time Prompt Adaptation
forVision-LanguageModels. In:Thirty-seventhConferenceonNeuralInformation Processing Systems; 2023. Available from: https://openreview.net/forum?
id=EhdNQiOWgQ.
[138] Yu L, Chen Q, Lin J, He L. Black-box Prompt Tuning for Vision-Language
Model as a Service. In: Elkind E, editor. Proceedings of the Thirty-Second
InternationalJointConferenceonArtificialIntelligence,IJCAI-23.International
40

<!-- Page 41 -->

Joint Conferences on Artificial Intelligence Organization; 2023. p. 1686–1694.
Main Track. Available from: https://doi.org/10.24963/ijcai.2023/187.
[139] White J, Fu Q, Hays S, Sandborn M, Olea C, Gilbert H, et al.: A Prompt
Pattern Catalog to Enhance Prompt Engineering with ChatGPT.
[140] Mondal S, Bappon SD, Roy CK.: Enhancing User Interaction in ChatGPT:
Characterizing and Consolidating Multiple Prompts for Issue Resolution.
[141] Desmond M, Brachman M.: Exploring Prompt Engineering Practices in the
Enterprise.
[142] White J, Hays S, Fu Q, Spencer-Smith J, Schmidt DC.: ChatGPT Prompt
Patterns for Improving Code Quality, Refactoring, Requirements Elicitation,
and Software Design.
[143] Papineni K, Roukos S, Ward T, Zhu WJ. BLEU: a method for automatic
evaluation of machine translation. In: Proceedings of the 40th Annual Meeting
on Association for Computational Linguistics; 2002. p. 311–318.
[144] Chin-Yew L. ROUGE: a package for automatic evaluation of summaries. In:
Text Summarization Branches Out; 2004. p. 74–81.
[145] Banerjee S, Lavie A. METEOR: an automatic metric for MT evaluation with
improvedcorrelationwithhumanjudgments. In:ProceedingsoftheACLWorkshop on Intrinsic and Extrinsic Evaluation Measures for Machine Translation
and/or Summarization; 2005. p. 65–72.
[146] Zhang T, Kishore V, Wu F, Weinberger KQ, Artzi Y. BERTScore: evaluating text generation with BERT. In: International Conference on Learning
Representations; 2020. .
[147] Sai AB, Mohankumar AK, Khapra MM. A survey of evaluation metrics used
for NLG systems. ACM Computing Surveys (CSUR). 2022;55(2):1–39.
[148] Ananthakrishnan R, Bhattacharyya P, Sasikumar M, Shah RM. Some issues in
automatic evaluation of english-hindi mt: more blues for bleu. Icon. 2007;64.
[149] Callison-Burch C, Osborne M, Koehn P. Re-evaluating the role of BLEU in
machine translation research. In: 11th Conference of the European Chapter of
the Association for Computational Linguistics; 2006. p. 249–256.
[150] Stent A, Marge M, Singhai M. Evaluating evaluation methods for generation
in the presence of variation. In: International Conference on Intelligent Text
Processing and Computational Linguistics. Springer; 2005. p. 341–351.
[151] Jain N, Saifullah K, Wen Y, Kirchenbauer J, Shu M, Saha A, et al. Bring
your own data! Self-supervised evaluation for large language models; 2023.
ArXiv:2306.13651.
[152] Wang Y, Yu Z, Zeng Z, Yang L, Wang C, Chen H, et al. PandaLM: an automatic evaluation benchmark for LLM instruction tuning optimization; 2023.
ArXiv:2306.05087.
[153] Lin YT, Chen YN. LLM-eval: unified multi-dimensional automatic evaluation for open-domain conversations with large language models; 2023.
ArXiv:2305.13711.
[154] Kiela D, Bartolo M, Nie Y, Kaushik D, Geiger A, Wu Z, et al. Dynabench:
rethinking benchmarking in NLP; 2021. ArXiv:2104.14337.
41

<!-- Page 42 -->

[155] Dehghani M, Tay Y, Gritsenko AA, Zhao Z, Houlsby N, Diaz F, et al. The
benchmark lottery; 2021. ArXiv:2107.07002.
[156] Zhou Y, Muresanu AI, Han Z, Paster K, Pitis S, Chan H, et al. Large language
modelsarehuman-levelpromptengineers.In:EleventhInternationalConference
on Learning Representations; 2022. .
[157] AjithA,PanC,XiaM,DeshpandeA,NarasimhanK. InstructEval:systematic
evaluation of instruction selection methods; 2023. ArXiv:2307.00259.
[158] TangJ,ZhouX,WanX,DaleyM,BaiZ. ML4STEMprofessionaldevelopment
program: enriching K-12 STEM teaching with machine learning. International
Journal of Artificial Intelligence in Education. 2023;33(1):185–224.
[159] Xie Q, Dai Z, Hovy E, Luong MT, Le QV. Unsupervised data augmentation
forconsistencytraining. In:Advancesinneuralinformationprocessingsystems.
vol. 33; 2020. p. 6256–6268.
[160] ArielyM,NazaretskyT,AlexandronG. MachinelearningandHebrewNLPfor
automatedassessmentofopen-endedquestionsinbiology. InternationalJournal
of Artificial Intelligence in Education. 2023;33(1):1–34.
[161] NilssonF,TuvstedtJ. GPT-4asanautomaticgrader:theaccuracyofgradesset
by GPT-4 on introductory programming assignments [Bachelor Thesis]. KTH
Royal Institute of Technology; 2023.
[162] Schneider J, Richner R, Riser M. Towards trustworthy autograding of short,
multi-lingual,multi-typeanswers. InternationalJournalofArtificialIntelligence
in Education. 2023;33(1):88–118.
[163] YangK,PengN,TianY,KleinD. Re3:generatinglongerstorieswithrecursive
reprompting and revision; 2022. ArXiv:2210.06774.
[164] Yang K, Klein D, Peng N, Tian Y. Doc: improving long story coherence with
detailed outline control; 2022. ArXiv:2212.10077.
[165] YangK,KleinD.FUDGE:controlledtextgenerationwithfuturediscriminators;

## ArXiv:2104.05218.

[166] Elgohary A, Hosseini S, Awadallah AH. Speak to your parser: interactive textto-SQL with natural language feedback. In: Annual Meeting of the Association
for Computational Linguistics; 2020. .
[167] Nijkamp E, Pang B, Hayashi H, Tu L, Wang H, Zhou Y, et al. Codegen: an
open large language model for code with multi-turn program synthesis; 2022.
ArXiv:2203.13474.
[168] Shrivastava D, Larochelle H, Tarlow D. Repository-level prompt generation
for large language models of code. In: International Conference on Machine
Learning; 2023. p. 31693–31715.
[169] Shwartz V, West P, Bras RL, Bhagavatula C, Choi Y. Unsupervised commonsense question answering with self-talk; 2020. ArXiv:2004.05483.
[170] Uesato J, Kushman N, Kumar R, Song F, Siegel N, Wang L, et al. Solving math word problems with process-and outcome-based feedback; 2022.
ArXiv:2211.14275.
[171] Roy S, Roth D. Solving general arithmetic word problems. In: Proceedings of
the 2015 Conference on Empirical Methods in Natural Language Processing;
42

<!-- Page 43 -->

2015. p. 1743–1752.
[172] Li Y, Lin Z, Zhang S, Fu Q, Chen B, Lou JG, et al. Making language models
better reasoners with step-aware Verifier. In: Proceedings of the 61st Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers). Toronto, Canada: Association for Computational Linguistics; 2023. p.
5315–5333. Available from: https://aclanthology.org/2023.acl-long.291.
[173] Ding B, Qin C, Liu L, Bing L, Joty S, Li B. Is GPT-3 a good data annotator?;

## ArXiv:2212.10450.

[174] Yoo KM, Park D, Kang J, Lee SW, Park W. GPT3Mix: leveraging large-scale
language models for text augmentation. In: Findings of the Association for
Computational Linguistics: EMNLP 2021; 2021. p. 2225–2239.
[175] Rawat P.: AI at Risk: OWASP Top 10 Critical Vulnerabilities for Large Language Models (LLMs). Available from: https://www.infosectrain.com/blog/
ai-at-risk-owasp-top-10-critical-vulnerabilities-for-large-language-models-llms/.
[176] Perez F, Ribeiro I.: Ignore Previous Prompt: Attack Techniques For Language
Models.
[177] Yin Z, Ye M, Zhang T, Du T, Zhu J, Liu H, et al.: VLATTACK: Multimodal
Adversarial Attacks on Vision-Language Tasks via Pre-trained Models.
[178] Goodfellow IJ, Shlens J, Szegedy C.: Explaining and Harnessing Adversarial
Examples.
[179] Wang J, Liu Z, Park KH, Jiang Z, Zheng Z, Wu Z, et al.: Adversarial
Demonstration Attacks on Large Language Models.
[180] ZhuS,ZhangR,AnB,WuG,BarrowJ,HuangF,etal.:AutoDAN:Automatic
and Interpretable Adversarial Attacks on Large Language Models. Available
from: https://openreview.net/forum?id=ZuZujQ9LJV.
[181] Kolter Z.: Discrete Optimization for Adversarial Attacks on Large
Language Models. Available from: https://orc.mit.edu/events/
discrete-optimization-adversarial-attacks-large-language-models.
[182] Shayegani E, Mamun MAA, Fu Y, Zaree P, Dong Y, Abu-Ghazaleh N.: Survey
of Vulnerabilities in Large Language Models Revealed by Adversarial Attacks.
[183] Jnr ABJ.: Prompt Hacking of Large Language Models. Available from: https:
//www.comet.com/site/blog/prompt-hacking-of-large-language-models/.
[184] KoschT,FegerS.:RiskorChance?LargeLanguageModelsandReproducibility
in Human-Computer Interaction Research.
[185] ZhanQ,LiangZ,YingZ,KangD.:InjecAgent:BenchmarkingIndirectPrompt
Injections in Tool-Integrated Large Language Model Agents.
[186] Chen K, Wang Z, Mi B, Liu W, Wang S, Ren X, et al.: Machine Unlearning in
Large Language Models.
[187] Wang H, Li H, Huang M, Sha L.: From Noise to Clarity: Unraveling the
Adversarial Suffix of Large Language Model Attacks via Translation of Text
Embeddings.
[188] Gao A. Prompt engineering for large language models. Available at SSRN
4504303. 2023;.
43

<!-- Page 44 -->

[189] Kurusumuthu J.: Prompt Hacking. Available from: https://riseandinspire.co.
in/2024/03/21/prompt-hacking/.
[190] Prompting L.: Introduction to Prompt Hacking. Available from: https://
learnprompting.org/docs/prompt hacking/intro.
[191] Bouchard L.: Hackaprompt: Exposing Systemic Vulnerabilities in LLMs. Available from: https://www.linkedin.com/pulse/
ignore-title-hackaprompt-exposing-systemic-llms-louis-bouchard--v8fme.
[192] Allouin A.: Understanding LLM Prompt Hacking and
Attacks. Available from: https://medium.com/@alexandre.allouin/
understanding-llm-prompt-hacking-and-attacks-8781c313a25b.
[193] Karande C.: OWASP LLM Prompt Hacking. Available from: https://owasp.
org/www-project-llm-prompt-hacking/.
[194] AI T.: Navigating the Challenges of Prompt Hacking in 2024. Available from: https://www.teneo.ai/blog/
navigating-the-challenges-of-prompt-hacking-in-2024.
[195] Tram`erF,ZhangF,JuelsA,ReiterMK,RistenpartT. StealingmachinelearningmodelsviapredictionAPIs. In:Proceedingsofthe25thUSENIXConference
onSecuritySymposium.SEC’16.USA:USENIXAssociation;2016.p.601–618.
[196] Shen X, Qu Y, Backes M, Zhang Y. Prompt stealing attacks against text-toimage generation models. arXiv preprint arXiv:230209923. 2023;.
[197] Zhang S. Defending against model extraction attacks via watermark-based
method with knowledge distillation. 2024;.
[198] Krishna K, Tomar GS, Parikh AP, Papernot N, Iyyer M. Thieves on Sesame
Street!ModelExtractionofBERT-basedAPIs. In:InternationalConferenceon
LearningRepresentations;2020.Availablefrom:https://openreview.net/forum?
id=Byl5NREFDr.
[199] Papernot N, McDaniel P, Sinha A, Wellman MP. SoK: Security and Privacy
in Machine Learning. In: 2018 IEEE European Symposium on Security and
Privacy (EuroS&P); 2018. p. 399–414.
[200] NasehA,KrishnaK,IyyerM,HoumansadrA.StealingtheDecodingAlgorithms
of Language Models. In: Proceedings of the 2023 ACM SIGSAC Conference
on Computer and Communications Security. CCS ’23. New York, NY, USA:
Association for Computing Machinery; 2023. p. 1835–1849. Available from:
https://doi.org/10.1145/3576915.3616652.
[201] Carlini N, Paleka D, Dvijotham KD, Steinke T, Hayase J, Cooper AF, et al.:
Stealing Part of a Production Language Model.
[202] Sha Z, Zhang Y.: Prompt Stealing Attacks Against Large Language Models.
[203] Hu H, Salcic Z, Sun L, Dobbie G, Yu PS, Zhang X.: Membership Inference
Attacks on Machine Learning: A Survey.
[204] Chen X, Liu C, Li B, Lu K, Song D.: Targeted Backdoor Attacks on Deep
Learning Systems Using Data Poisoning.
[205] He D. Cryptographic Schemes and Protocols for Artificial Intelligence;.
44

<!-- Page 45 -->

[206] Shamshiri S, Sohn I. Defense Method Challenges Against Backdoor Attacks in
Neural Networks. In: 2024 International Conference on Artificial Intelligence in
Information and Communication (ICAIIC); 2024. p. 396–400.
[207] Holland R, Pal S, Pan L, Zhang LY. Backdoor Attacks and Generative Model
Fairness: Current Trends and Future Research Directions. In: 2024 16th InternationalConferenceonCOMmunicationSystems&NETworkS(COMSNETS);
2024. p. 31–36.
[208] Khan A, Sharma I. AI-Powered Detection and Mitigation of Backdoor Attacks
on DatabasesServer. In:2024 2nd InternationalConference onIntelligentData
Communication Technologies and Internet of Things (IDCIoT); 2024. p. 374–
379.
[209] Ooi YX. Evaluation of backdoor attacks and defenses to deep neural networks.
2024;.
[210] Gu T, Dolan-Gavitt B, Garg S.: BadNets: Identifying Vulnerabilities in the
Machine Learning Model Supply Chain.
[211] SteinhardtJ,KohPW,LiangP.:CertifiedDefensesforDataPoisoningAttacks.
[212] Eric M.: A Complete Introduction to Prompt Engineering For Large
Language Models. Available from: https://www.mihaileric.com/posts/
a-complete-introduction-to-prompt-engineering/.
[213] Abdali S, Anarfi R, Barberan C, He J.: Securing Large Language Models:
Threats, Vulnerabilities and Responsible Practices.
[214] Kurakin A, Goodfellow I, Bengio S.: Adversarial Machine Learning at Scale.
[215] Yang Y, Huang P, Cao J, Li J, Lin Y, Dong JS, et al.: A Prompting-based
Approach for Adversarial Example Generation and Robustness Enhancement.
[216] Linardatos P, Papastefanopoulos V, Kotsiantis S. Explainable AI: a review of
machine learning interpretability methods. Entropy. 2020;23(1):18.
[217] Recht B, Re C, Wright S, Niu F. Hogwild!: a lock-free approach to parallelizing stochastic gradient descent. In: Advances in neural information processing
systems. vol. 24; 2011. .
[218] MelnychukV,FrauenD,FeuerriegelS. Causaltransformerforestimatingcounterfactual outcomes. In: International Conference on Machine Learning; 2022.
p. 15293–15329.
[219] Novakovsky G, Dexter N, Libbrecht MW, Wasserman WW, Mostafavi S.
Obtaining genetics insights from deep learning via explainable artificial intelligence. Nature Reviews Genetics. 2023;24(2):125–137.
[220] Bertucci L, Bri`ere M, Fliche O, Mikael J, Szpruch L. Deep learning in finance:
from implementation to regulation; 2022. SSRN:4080171.
[221] Maple C, Szpruch L, Epiphaniou G, Staykova K, Singh S, Penwarden W, et al.
The AI revolution: opportunities and challenges for the finance sector; 2023.
ArXiv:2308.16538.
[222] Amann J, Blasimme A, Vayena E, Frey D, Madai VI. Explainability for artificial intelligence in healthcare: a multidisciplinary perspective. BMC Medical
Informatics and Decision Making. 2020;20(1):1–9.
45

<!-- Page 46 -->

[223] RajpurkarP,ChenE,BanerjeeO,TopolEJ. AIinhealthandmedicine. Nature
Medicine. 2022;28(1):31–38.
[224] O¨ztu¨rkD.Whatdoesartificialintelligencemeanfororganizations?Asystematic
review of organization studies research and a way forward. The Impact of
ArtificialIntelligenceonGovernance,EconomicsandFinance,VolumeI.2021;p.
265–289.
[225] Seeamber R, Badea C. If our aim is to build morality into an artificial agent,
how might we begin to go about doing so? IEEE Intelligent Systems. 2023;.
46

## Tables

**Table (Page 6):**

|  |  |  |  |  |  |  |  |  |  |  |  | specif |  |  | ically |  |  | related |  |  | to | arti | fi | cial |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| intel | ligence a | nd machine |  | learn |  | ing. | Recently |  | , arti |  | ficial | intel |  | li | gence |  |  | has |  | becom |  |  |  |  |
| extremely po |  | pular, espec |  | ially |  | the l | arge | lang | uage |  | mod | els | which |  |  |  | have |  |  | amazed |  | me. |  |  |
| Please analyz |  | e the pos | si | ble | re | ason | s behind |  | the | rapid |  | advance |  |  |  | ment |  |  | of | thi |  |  |  |  |
| tech | nology fr | om at least |  | three |  | per | spect | ives. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 6):**

| 2. | Availabilit | y of data: |
|---|---|---|
| 3. | Socio-econ | omic demand: |


**Table (Page 8):**

| Q: | Yes |  | or | no: is | it com |  | mon | to | see |
|---|---|---|---|---|---|---|---|---|---|
| frost |  | duri |  | ng som | e col | lege |  |  |  |
| com |  | menc |  | ements |  |  |  |  |  |
| A: | The |  | answer i |  | s yes. |  |  |  |  |


**Table (Page 11):**

| Detailed |  | size | analysi | s: mi | litary | tanks | vs. | cars |
|---|---|---|---|---|---|---|---|---|
| 1. | Dimen | sion | sandw | eight |  |  |  |  |


**Table (Page 11):**

| Thre |  | e ke | y influ |  | encin | g fac | tors |  | on |  | whether |  | an |  | object |  | can |  | pass |  | through |  | an |  | infinitely |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wide |  | entranc |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1. | Height |  | of | the | obj |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 12):**

| Detailed size analysis: military ta |  |  |  |  |  |
|---|---|---|---|---|---|
| 1. | Dimensions and weight: |  |  |  |  |
| - | Mili | tary tanks: typically, main b | attle tanks (like the M1 Abrams or | T-90) h | ave |
| width |  | s ranging from 10 to 13 feet, | lengths from 25 to 35 feet (includi | ng the m | ain |
| gun), |  | and weights from 60 to 70 t |  |  |  |
| - | Cars | : most consumer cars have a | width of about 6 to 8 feet, a lengt | h of 12 t |  |
| feet, a |  | nd weigh between 1 to 3 ton | s. Some large SUVs and trucks can | exceed | these |
| figure |  | s but are still substantially s |  |  |  |
| 2. |  |  |  |  |  |


**Table (Page 12):**

|  |  |  | is not restrictive and the surface i | s rough, | a mil | i- |
|---|---|---|---|---|---|---|
| taryt |  | ankwouldbemorelikelyto | passthroughitwithoutissues.On | theother | hand, |  |
| if | the | entrance is low-height or ha | s tight squeezes that could compro | mise the | struc | - |
| tural |  | integrity of larger, robust ve | hicles, a car might be at an advant |  |  |  |
