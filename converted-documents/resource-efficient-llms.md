---
title: "Resource Efficient LLMs"
original_file: "./Resource_Efficient_LLMs.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["arxiv", "models", "llms", "language", "model", "training", "efficient", "preprint", "data", "memory"]
summary: "<!-- Page 1 -->

4202
ceD
92
]GL.sc[
4v52600.1042:viXra
Beyond Efficiency: A Systematic Survey of

### Resource-Efficient Large Language Models

Guangji Bai1, Zheng Chai2, Chen Ling1, Shiyu Wang1,

### Jiaying Lu1, Nan Zhang3, Tingwei Shi1, Ziyang Yu1,

Mengdan Zhu1, Yifei Zhang1, Xinyuan Song1, Carl Yang1,

### Yue Cheng2, Liang Zhao1*

1*Department of Computer Science, Emory University, 201 Dowman Dr,
Atlanta, 30322, GA, United States. 2School of Data Science and Department of Computer Science"
related_documents: []
---

# Resource Efficient LLMs

<!-- Page 1 -->

4202
ceD
92
]GL.sc[
4v52600.1042:viXra
Beyond Efficiency: A Systematic Survey of

### Resource-Efficient Large Language Models

Guangji Bai1, Zheng Chai2, Chen Ling1, Shiyu Wang1,

### Jiaying Lu1, Nan Zhang3, Tingwei Shi1, Ziyang Yu1,

Mengdan Zhu1, Yifei Zhang1, Xinyuan Song1, Carl Yang1,

### Yue Cheng2, Liang Zhao1*

1*Department of Computer Science, Emory University, 201 Dowman Dr,
Atlanta, 30322, GA, United States.
2School of Data Science and Department of Computer Science,
University of Virginia, 1827 University Avenue, Charlottesville, 22904,
VA, United States.
3College of Information Sciences and Technology, Pennsylvania State
University, 201 Old Main, University Park, 16802, PA, United States.
*Corresponding author(s). E-mail(s): liang.zhao@emory.edu;
Contributing authors: guangji.bai@emory.edu; dub6yh@virginia.edu;
chen.ling@emory.edu; shiyu.wang@emory.edu; jiaying.lu@emory.edu;
njz5124@psu.edu; tshi30@emory.edu; zyu31@emory.edu;
mengdan.zhu@emory.edu; yifei.zhang2@emory.edu; xsong30@emory.edu;
j.carlyang@emory.edu; mrz7dp@virginia.edu;

### Abstract

The burgeoning field of Large Language Models (LLMs), exemplified by sophisticated models like OpenAI’s ChatGPT, represents a significant advancement
in artificial intelligence. These models, however, bring forth substantial challenges in high consumption of computational, memory, energy, and financial
resources, especially in environments with limited resource capabilities. This
surveyaimstosystematicallyaddressthesechallengesbyreviewingabroadspectrum of techniques designed to enhance the resource efficiency of LLMs. We
categorize methods based on their optimization focus—covering computational,
memory,energy,financial, andnetwork resources—and theirapplicability across
various stages of an LLM’s lifecycle, including architecture design, pre-training,
1

<!-- Page 2 -->

fine-tuning,andsystemdesign.Additionally,thesurveyintroducesanuancedcategorizationofresourceefficiencytechniquesbytheirspecificresourcetypes,which
uncoverstheintricaterelationshipsandmappingsbetweenvariousresourcesand
corresponding optimization techniques. A standardized set of evaluation metrics and datasets is also presented to facilitate consistent and fair comparisons
across different models and techniques. By offering a comprehensive overview of
the current state-of-the-art and identifying open research avenues, this survey
serves as a foundational reference for researchers and practitioners, aiding them
in developing more sustainable and efficient LLMs in a rapidly evolving landscape. To make the field more accessible to interested beginners, we not only
makeasystematicreviewofexistingworksandahighlystructuredtaxonomyof
resource-efficientLLMsbutalsoreleaseawebsiteincludingaconstantly-updated
paper list https://github.com/tiingweii-shii/Awesome-Resource-Efficient-LLM-
Papers.
Keywords:LargeLanguageModel,ResourceEfficiency,SustainableAI,Survey.
1 Introduction
In recent years, Large Language Models (LLMs) [1, 2] have achieved significant
advancements, redefining the frontier of artificial intelligence. These models, such as
OpenAI’s GPT-3 with its impressive 175 billion parameters, represent a quantum
leap in complexity and capability [3]. The trend in LLM development is toward everincreasing model sizes, with some recent entrants boasting upwards of hundreds of
billions of parameters [4–6]. This scale amplifies their utility across a spectrum of
applications,fromintelligentchatbotsto intricatedataanalyses,andevenfacilitating
researchin diverse domains. However,the exponential growthin model sizes presents
a huge demand for various resources (e.g., computation, energy, memory) [7–9]. The
immense resource requirements to train or deploy such extensive models can be costprohibitive, particularly in resource-constrained environments like academic labs or
the medical sector, which do not have access to the vast computational resources of
major IT conglomerates. Additionally, the environmental impact is a growing concern, as the extensive GPU usage for training these models translates to significant
electricity consumption and increasing carbon dioxide emissions [7]. Addressing these
challenges requires a focused effort on enhancing the resource efficiency of LLMs at
every stage of their lifecycle.
Defining Resource-Efficient LLMs requires an understanding of the critical
resources involved in the lifecycle of LLMs. In this survey, we systematically categorize the essential resources into five key categories: computation, memory, energy,
money, and communication cost. Computation refers to the processing power necessary to train and run these models; memory encompasses the data storage capacity
required;energydenotestheelectricityconsumedduringoperation;financialresources
pertain to the monetary investment needed for infrastructure and ongoing costs; and
communicationcostinvolvesthebandwidthandlatencyindatatransferduringtraining and inference. Efficiency in this context is characterized by the ratio of these
2

<!-- Page 3 -->

resources invested to the output produced, with a more efficient system being one
that yields the same level of output while consuming fewer resources. A resourceefficient LLM, therefore, is designed to maximize performance and capabilities while
minimizing resource expenditure across all these dimensions, thereby enabling more
sustainable and accessible AI solutions.
ResourceefficiencyinLLMsisacrucialandcomplexareathatdemandsinnovative
solutionstoaddresssignificantchallenges.Thesechallenges,morepronouncedinLLMs
thaninsmallerneuralnetworkslikeCNNsandMLPs,arisefromtheuniquescaleand
complexity of LLMs. We outline these challenges from various key perspectives:
•
[Model] 1. Low parallelism in auto-regressive generation: Auto-regressive token
generation, the predominant method in LLMs, suffers from significant latency due
topoorparallelism[10].Thisisespeciallyproblematicforlargemodelsizesorextensive input lengths, hindering efficient processing in both training and inference. 2.
Quadraticcomplexityinself-attentionlayers:The multi-headself-attentionlayerin
LLMs exhibits quadraticcomplexitywithrespectto the input sequencelength[11].
This complexity creates a computational bottleneck as the input length increases,
limiting the practical input sequence length LLMs can handle efficiently.
•
[Theory] 1. Scaling laws and diminishing returns: theoretical insights into scaling laws for neural networks, particularly LLMs, suggest that as models become
larger,thebenefitsinperformanceimprovementperparameteraddeddiminish[12].
This phenomenon raises questions about the optimal size of LLMs and the balance
between resource investment and performance gain. 2. Generalization and overfitting:Theoreticalworkongeneralizationinmachinelearningisparticularlyrelevant
for LLMs [13, 14]. Understanding the limits of what large models can generalize from training data and the risks of overfitting is crucial for developing more
resource-efficientmodels.
•
[System]Giventhe substantialmodelsizeofLLMsandthe vasttrainingdatasets,
fitting them into the memory of a single GPU/TPU is unfeasible [15, 16]. Consequently, intricate system designs become crucial to optimize the training process
for LLMs and successfully accomplish the task. Furthermore, the system design
gainsincreasedsignificancedue to the latencyandthroughputrequirementsassociated with the inference tasks of LLMs, particularly when taking into account user
experience and the constraints of a limited cost budget [17, 18].
•
[Ethics] 1. Dependence on large and proprietary training data: Many LLMs are
trained on extensive, proprietary datasets, making it challenging to apply certain efficiency improvement techniques that require access to the original training
data [19]. This limitation not only restricts the scope of potential improvements
but also raises ethical questions about transparency and the democratization of
AI advancements. 2. Closed source models and lack of parameter access: Many
advanced LLMs are closed source [1, 20–22], with restricted access to their parameters. This constraint means that efforts to improve efficiency must be conducted
without deep insights into the model’s internal workings, complicating the process
of optimizing resource usage.The closed nature of these models also brings up ethical concerns regarding the concentration of AI capabilities and the openness of
scientific research.
3

<!-- Page 4 -->

•
[Metrics] In the context of LLMs, the development of comprehensive metrics for
evaluatingresourceefficiencyfacesuniquechallengesduetothediverseandcomplex
natureofLLMtasksandarchitectures[10].Unlikesmallermodelswhereoptimizing
one or two resources, such as computation or memory, might be sufficient, LLMs
present a multi-objective problem requiring simultaneous optimization across multiplekeyresources,includingcomputation,memory,energy,monetarycost,etc[23].
Therefore,acomprehensivemetricforLLMsmustprovideaholisticviewthatencapsulatesallthesecriticalresources,quantifyingnotonlytheindividualresourceusage
but also the interdependencies and trade-offs between them [24]. This approach
is crucial for advancing LLMs in a balanced and sustainable manner, significantly
more complex than metric development for smaller models.
In recent years, significant research efforts have been dedicated to developing and
applying resource-efficient LLMs to address the challenges referenced earlier. There
has been a wave of research proposing and deploying new strategies across various
fields,althoughtheconceptofresource-efficientLLMsisrelativelynascent.Mostexisting LLM approaches have been tailored for specific application domains; however,
the underlying principles are often adaptable enough to be utilized in other areas.
Nevertheless, it remains challenging to compare these resource-efficient strategies
across different domains that cater to distinct communities. Furthermore, assessing
the performance of resource-efficient LLMs demands intricate and specialized evaluation strategies due to their distinctive attributes, such as their multi-dimensional
efficiency (e.g., computational, energy,memory usage)and the diverse outcomes they
produce. To date, there is a deficiency in systematic standardization and a comprehensive summarizationframeworkto evaluate the variousmethodologiesproposedfor
resource-efficient LLMs. This lack of a cohesive summary and classification of existing methods and applications in resource-efficient LLMs poses significant issues for
practitioners who need clear information on current limitations, pitfalls, unresolved
questions, and promising directions for future research.
Inresponsetothese gaps,thispaperseekstoofferasystematicreviewofthetechniques, benchmarks, and evaluation metrics that contribute to the resource efficiency
ofLLMs.Toourknowledge,thisconstitutesthefirstdetailedsurveyexplicitlydevoted
toresourceefficiencyinthecontextofLLMs.Inthefollowing,weoutlinetheprincipal
contributions of this survey:
•
Comprehensive overview of resource-efficient LLM techniques: Our
paper makes a significant contribution by offering a comprehensive overview of
techniques aimed at enhancing the resource efficiency of Large Language Models. This overview is extensive, covering the entire range of the LLM lifecycle. It
delves into various methodologies and strategies developed in the field, focusing
on how they contribute to making LLMs more resource-efficient.
•
Systematic categorization and taxonomy of techniques by resource
type: We established a systematic categorization and taxonomy of resourceefficient LLM techniques, organized primarily by the type of resource(s) they
optimize.Thistaxonomysimplifiestheprocessofidentifyingandselectingappropriatemethodsbasedonspecificresourceoptimizationneedsandprovidesaclear
4

<!-- Page 5 -->

and organized framework that aids researchers and practitioners in navigating
the landscape of resource-efficientLLMs.
•
Standardization of evaluation metrics and datasets: We present a standardizedsetofevaluationmetricsanddatasetstailoredforassessingtheresource
efficiency of LLMs. This standardization facilitates consistent and fair comparisonsacrossdifferentmodelsandtechniquesandprovidesabenchmarkforfuture
research in the field.
•
Identification of gaps and future research directions: The paper concludes with a thoughtful discussion of the current bottlenecks and unresolved
challenges in creating resource-efficient LLMs. By examining the limitations of
existing approaches, we shed light on potential avenues for future research.
1.1 Related work
In this section, we discuss the relationship between our survey and some existing
surveysonsimilartopics.Ingeneral,wecandivideexistingsurveysrelatedtothe efficiencyandaccelerationofLLMsintothefollowingcategories:1.fundamentaloverview
of LLMs; 2. survey of model compression for LLMs; and 3. review of techniques of
efficiency and acceleration for general deep neural networks.
•
Fundamental overview of LLMs. With the recent surge in the popularity
and efficacy of LLMs, numerous review papers have surfaced, offering insights
into various aspects of LLMs. Some concentrate on dissecting the fundamental
components of LLMs [25–27], while others delve into the historical context and
potentialapplicationsofgenerativeAI[28–30].Aselectfew[31]explorestrategies
for enhancing LLMs with reasoning capabilities. Nevertheless, a comprehensive
review and technical taxonomy specifically focused on the specialization of LLM
domains remains an unaddressed gap in the current literature.
•
Survey of compression and acceleration for LLMs. Transformer-based
language models have achieved huge success, however, the computational and
memorycostremainsabigconcerndespitethesuperiorperformance.Therehave
been several survey papers on how to compress and accelerate large language
models. For example, some discuss how to accelerate the inference of LLMs [32–
34],byfocusingonmodelcompressiontechniques.Inaddition,aselectfew[35,36]
exploremoreefficientandlightweightarchitecturedesignsfortransformers,which
arethebackboneofmodernLLMs.Furthermore,someworksdiscusstheefficient
training of LLMs [37]. However, those existing surveys either lack comprehensiveness or are not up-to-date, especially considering the large number of papers
published after the birth of ChatGPT, which marks the beginning of the LLMs
era.
•
Review of efficient deep neural networks. How to achieve efficient design
or accelerate the computation of deep neural networks (DNNs) has long been a
popularresearchdirection,andtherehavebeenacoupleofsurveypapersonthis
topic.SomeworksfocusonthemodelcompressionandaccelerationofDNNs[38,
39]. A few others discuss the hardware design and optimization for DNNs [40,
41]. However, due to the very large model size and the special architecture of
5

<!-- Page 6 -->

transformers, there is a big gap in directly applying those techniques for DNNs
onto the LLMs.
1.2 Outline
The remainder of this survey is structured as follows, offering a detailed exploration
of resource-efficientLLMs:
•
Section 2 Preliminary and taxonomy: This section sets the foundation by introducing the fundamental concepts behind transformers and pre-trained LLMs. It
establishes a comprehensive taxonomy of resources essential for LLMs, such as
computation, memory, energy, money, and network communication. This taxonomy serves as a guiding framework for the entire survey, outlining the key areas
of focus for improving resource efficiency in LLMs.
•
Section 3 LLM architecture design: This section delves into the latest developmentsinLLMarchitecture,emphasizingdesignsthatenhanceresourceefficiency.
It discusses both efficient transformer architectures, which optimize traditional
transformermodels,andnon-transformerarchitectureswhichproposealternative
structures for resource optimization.
•
Section 4 LLM pre-training: This section explores the various pre-training techniques for LLMs, highlighting how they contribute to resource efficiency. Key
areas such as memory efficiency, data efficiency, and innovative training pipeline
designsareexamined,illustratinghoweachtechniqueimpactstheoverallresource
utilization during the pre-training phase.
•
Section 5 LLM fine-tuning: This section covers the fine-tuning phase of LLMs,
focusing onmethods that enhanceresourceefficiency.It includes detaileddiscussionsonparameter-efficientfine-tuning,whichminimizesparameterupdates;and
full-parameter fine-tuning, which optimizes the entire parameter set.
•
Section 6 LLM inference: Here, we analyze various inference techniques that
improve resource efficiency in LLMs. The section features discussions on
static methods including pruning, quantization, knowledge distillation, low-rank
approximation, etc. In addition, we also discuss dynamic methods such as
dynamicinference,whichadaptscomputationalresourcesinrealtime,andtoken
parallelism, which optimizes processing at the token level to enhance efficiency
during the inference stage.
•
Section 7 System design: This section addresses system-level strategies for
resource-efficient LLMs, encompassing support infrastructure, which focuses on
leveragingspecializedsystemsforefficiency,anddeploymentoptimization,which
involves strategies for deploying LLMs in a resource-consciousmanner.
•
Section 8 Technique categorization by resources: In this section, we evaluate the
effectiveness of various resource efficiency techniques. The discussion revolves
around real-world applications and how different methods fare in practical
scenarios,providing a bridge between theory and application.
•
Section 9 Benchmark and evaluation metrics: This section presents the benchmarks and metrics used for evaluating the resource efficiency of LLMs. It
highlights the importance of standardized evaluation criteria in assessing the
effectiveness of various techniques and models.
6

<!-- Page 7 -->

•
Section 10 Open Challenges and future directions: Here, we identify the existing
challengesandpotentialfutureresearchdirectionsinthefieldofresource-efficient
LLMs. This section is crucial for understanding the current gaps in the field and
where future efforts may be most beneficial.
•
Section11Conclusion: Thesurveyconcludeswithasummaryofthekeyfindings
and insightspresented,encapsulating the coretakeawaysfrom the explorationof
resource efficiency in LLMs.
2 Preliminary and taxonomy
Inthissection,wefirstprovidesomepreliminariesofthissurvey,includingsomeintroduction about transformers and LLMs. Then, we introduce our proposed taxonomy
of the techniques for the efficiency and acceleration of LLMs.
2.1 Preliminaries
2.1.1 Transformer model
The Transformer model stands as a pivotal milestone in the evolution of deep learning, particularly in the realm of natural language processing (NLP). Introduced
by [11], the Transformer model represents a groundbreaking departure from conventional sequence-to-sequence models, offering an innovative solution to the challenges
of capturing long-range dependencies in sequences.
•
Embedding Layers. The embedding layer is the foundational component of a
Transformer model, serving as the initial step in transforming raw input data
into a format that can be effectively processed. It maps discrete tokens, such
as words or subwords, into continuous vector representations, often referred to
as word embeddings. These embeddings capture semantic relationships between
words and enable the model to understand the meaning of each token.
•
Positional Encoding. Unlike recurrent neural networks (RNNs) or convolutional
neural networks (CNNs), Transformers do not inherently possess knowledge of
theorderorpositionoftokensinasequence.Toaddressthislimitation,positional
encodings are introduced. These encodings are added to the word embeddings
and provide the model with information about the position of each token within
thesequence.Typically,sinusoidalfunctionsareusedtogeneratethesepositional
encodings,ensuring that the model cancapture sequentialdependencies without
relying on recurrence or convolution.
•
Self-Attention. Self-attention is the cornerstone of the Transformer architecture
and allows the model to weigh the importance of different words in the input
sequence when making predictions for a particularword.It computes a weighted
sum of all input words, where the weights are determined dynamically based on
the similarity between words. The self-attention mechanism is computed using a
weighted sum over all words in the sequence, and the weights are determined by
7

<!-- Page 8 -->

the dot product of query, key, and value vectors:

## Qkt

Attention(Q,K,V)=softmax V. (1)
(cid:18) √d (cid:19)
k
Here, Q, K,and V are the query,key,and value matrices,respectively,andd is
k
the dimension of the key vectors. This mechanism allows the model to focus on
relevant information within the input sequence.
•
Multi-Head (Self-)Attention. Multi-head self-attention extends the self-attention
mechanism by performing it multiple times in parallel, with different sets of
learned parameters.This allows the model to capture different types of relationships and dependencies in the input sequence, providing a richer representation.
Mathematically, multi-head self-attention involves computing multiple sets of
query,key,andvaluematrices,andthenconcatenatingtheresultsfromeachhead:
MultiHead(Q,K,V)=Concat head ,head ,...,head WO, (2)
1 2 h
(cid:0) (cid:1)
where head = Attention(QWQ,KWK,VWV) represents the output of the
i i i i
i-th attention head, and WO is a learned linear transformation. Multi-head
self-attention enhances the model’s ability to capture both local and global
dependencies in the data.
In summary, the Transformer architecture consists of these key components, each
playing a crucial role in enabling the model to understand and generate sequences
effectively, making it a powerful tool in natural language processing and other
sequence-to-sequence tasks.
2.1.2 Large Language Models (LLMs)
Pre-trained Language Models (PLMs) constitute a type of neural network that has
been trained on extensive collections of text data. Their purpose is to acquire knowledge of linguistic patterns, structures, and semantics inherent in the language.In the
context of LLMs, the input comprises a text sequence that serves as the context for
comprehension and processing. Often, a prompt or additional sentence is included to
clarify the task. These prompts are tailoredto the specific NLP task at hand, providing a premise or task explanation. For example, in text summarization,a prompt like
“Summarize the key points in the following passage:” can be placed before the input
passage. The output is the generated text sequence or prediction responding to the
input, e.g., the summarized key points of the provided passage. In some cases, postprocessing steps such as token decoding or label extraction may be necessary for the
final presentation.
LLMs typically follow the architectural designs of PLMs and come in three primary flavors: encoder-only, encoder-decoder, and decoder-only architectures. Here’s
an overview of these LLM architectures and their distinctions:
•
Encoder-only Language Models. These models process input text to create vector representations without an explicit decoding phase for generating new text.
8

<!-- Page 9 -->

Instead, they transformand embedtext into a high-dimensionalspace.Encoderonly models are primarily designed to capture and understand patterns and
semanticsinthe inputdata.Theyfindextensiveuseintaskssuchastextclassification,sentimentanalysis,andclustering.AnotableexampleisBERT[42],which
extracts context-rich embeddings for downstream tasks through pre-training on
a masked language modeling objective.
•
Encoder-Decoder Language Models. These models consist of an encoder that
processes input text into vector representations and a decoder that generates
output text based on these representations. They employ cross-entropy loss as
the objective function, comparing the actual and predicted target sequences.
Encoder-Decoder LLMs are often used for sequence-to-sequence tasks such as
machine translation and summarization. T5 [43] is a notable example of this
architecture.
•
Decoder-only Language Models. Examples like GPT [44] are autoregressive languagemodelsthatgeneratethenextwordinasequencebasedonpreviouswords.
They map a sequence of tokens to a vector representation and generate contextually relevant content autoregressively, calculating the probability of the next
tokenbasedon the context.This autoregressiveapproachis particularly suitable
for text-generation tasks.
In summary, LLMs and their variants play a pivotal role in natural language processingtasksbyleveragingpre-trainingonvasttextcorporatofacilitate a wide range
of language understanding and generation tasks.
2.2 Proposed taxonomy
2.2.1 Taxonomy of key resources involved with using LLMs.
The taxonomy for resourceefficiency in LLMs encompasses five key domains: computation, memory, energy, money, and network communication. Each domain addresses
a distinct aspect of resource utilization:
•
Computation: This involves the processing power required for tasks such as
training, fine-tuning, and executing LLMs. Evaluating computational efficiency
includesconsideringthenumberofoperations(likefloating-pointoperations),the
efficiencyofalgorithms,andtheutilizationofprocessingunitslikeGPUsorTPUs.
It is crucial to explore how to maximize output while minimizing computational
requirements.
•
Memory:MemoryefficiencypertainstotheamountofRAMandstorageneeded.
LLMs,especiallythosewithbillionsofparameters,requiresignificantmemoryfor
storing the model weights and for processing large datasets during training and
inference. Optimizing data structures, employing techniques like model pruning,
and exploring memory-efficient architectures are key strategies here.
•
Energy:Thisresourcereferstotheelectricalpowerconsumedduringthemodel’s
lifecycle. Given the environmental impact and operating costs, energy efficiency
is vital. It includes strategies for reducing power consumption, such as optimizing hardware utilization, using energy-efficient hardware, and implementing
algorithms that require less computational power.
9

<!-- Page 10 -->

•
Money: Financial resources are a crucial consideration, especially for smaller
organizationsandresearchers.Thisincludesthecostofhardwareacquisition,electricity for running the models, and potential cloud computing expenses. Finding
ways to make LLMs accessible and viable for a broader range of users without
significant financial investment is another key challenge.
•
Network communication: For distributed training and cloud-based deployment, network bandwidth and latency become significant. Efficient network
communication means reducing the amount of data that needs to be transferred
betweennodesinadistributedsystemorbetweenthecloudandend-users,which
can greatly affect training time and responsiveness in real-time applications.
2.2.2 Taxonomy of techniques for resource-efficient LLMs
As delineated in Figure 1, our survey paper introduces a structured taxonomy that
categorizestechniquesforenhancingtheresourceefficiencyofLLMsintoclear,defined
tiers. We propose five principal categories: Architecture Design, Pre-training, Finetuning, Inference, and System Design. Each of these is selected for its integral role in
the lifecycle of efficient LLM development and deployment.
•
Architecture design. This category examines the structural foundations of
LLMs, branching into Transformer-based and Non-transformer Architectures.
These classifications are intended to highlight architectural variations and
innovations crucial for the models’ efficiency and efficacy.
•
Pre-training. This category inspects the preliminary phases of LLM development, including Memory Efficiency and Data Efficiency. It underscores the
importanceofthepre-trainingenvironmentandstrategiesthatsignificantlyaffect
the models’ future performance and resource utilization.
•
Fine-tuning. Addressing the optimization of pre-trained models, this category
isorganizedintoParameter-efficientFine-tuningandFull-parameterFine-tuning.
These subdivisions represent the range of techniques that refine models for
particular tasks or enhance their overall functionality.
•
Inference. During the operational stage, various strategies under the Inference
category, such as Model Compression and Dynamic Acceleration, are employed.
Thisclassificationacknowledgesthediversetacticsappliedatthemodelinference
phase, impacting efficiency and performance distinctly.
•
System design. Focusing on system-level considerations, this category covers
DeploymentOptimizationandSupport Infrastructure,among others.It explores
hardwareandsystemoptimizationsthatareessentialforimprovingthe practical
performance of LLMs.
Throughthistaxonomy,weaimtofacilitateastructuredandnuancedunderstanding of the diverse methodologies and strategies employed in the quest for enhanced
efficiency and acceleration of LLMs, providing a holistic view of the current research
landscape.
10

<!-- Page 11 -->

sMLL
tneicffiE-ecruoseR
Approximated Attention

### Transformer-based

Architecture Hardware-aware Attention
ArchitectureDesign
Modular Network

### Non-transformer

Architecture OtherArchitecture
Distributed Training

### Memory Efficiency

Mixed Precision Training

### Pre-training


### ImportanceSampling

Data Efficiency Data Augmentation

### Training Objective

Adapter-basedFine-tuning

### Parameter-efficient

Fine-tuning Masking-based Fine-tuning

### Fine-tuning

Full-parameter Fine-tuning Pruning

### Quantization


### Model Compression

Knowledge Distillation
Low-rank Approximation

### Inference


### Early Exit

Dynamic Acceleration InputPruning

### Token Parallelism


### Hardware Offloading

Deployment Optimization
Collaborative Inference
System Design Libraries
SupportInfrastructure
Edge Devices

### OtherSystems

Fig. 1 Ataxonomy oftechniques forachievingresource-efficientLLMs.
3 LLM architecture design
This section explores the advancements in architecture design for LLMs, specifically
focusing on enhancing the efficiency of Transformer models. We examine various
strategies aimed at reducing computational and memory demands, crucial for the
practical deployment of LLMs. The discussion includes innovative approaches like
11

<!-- Page 12 -->

Reformer, Linear Transformer, AFT, and KDEformer, each presenting unique solutions to optimize processing speed and resource usage. Additionally, we touch upon
hardware-optimized attention mechanisms and alternative non-transformer architectures, highlighting their contributions to the evolving landscape of efficient LLM
design.
3.1 Efficient transformer architecture
Efficient transformers focus on creating neural network architectures that are optimized for enhanced throughput. The attention layer significantly influences the
processing speed of transformers,which contributes a lot to the throughput.
3.1.1 Approximate attention.
Onestreamofworksfocusesondesigningattentionoperatorswithapproximationtechniques toachieveless time complexity and/or less memory complexity.Inthe
classicTransformer,the time complexityofthe self-attentionoperatoris (T2d),and

## O

thememorycomplexityis (T2).HereT,ddenotethesequencelengthandhiddenfea-

## O

turedimension,respectively.Reformer[45]replacedot-productattentionbyproposed
locality-sensitive hashing attention, which leads to (TdlogT) time complexity and

## O

(T logT)memorycomplexity.LinearTransformer[46]expressestheself-attentionas

## O

a linear dot-product of kernel feature maps and utilizes the associativity property of
matrix products to reduce the complexity term from T2 to T, thus achieving (Td2)

## O

time complexityand (Td+d2)memorycomplexity.EfficientAttention[47]proposes

## O

anapproximatedattentionoperationbyswitchingtheQKVmultiplicationorderfrom
(QK T )VtoQ(K T V),whichleadstomoreefficient (T2d)timecomplexityandsame

## O

(Td+d2)memorycomplexitywhend<T.AFT[48]proposesanextremelyefficient

## O

variant called AFT-simple, which achieves linear complexity in both time ( (Td))

## O

and memory ( (Td)). In an AFT layer, the key and value are first combined with

## O

a set of learned position biases (s < T), so that the multiplication between the keyvalue andquery is in anelement-wise manner.The introducedlearnedposition bias s
can be eliminated in the AFT-simple variant (i.e. no position bias is learned) so that
AFT-simple completelygets ridofthe needfordotproducts operations.Memoryefficientattention[49]presentsapracticalimplementationforself-attentionthatrequires
only (dlogT)memorywiththesametimecomplexity (T2d).Thecoreideabehind

## O O

memory efficient attention is similar to “lazy softmax” [50] where the denominator of
thesoftmaxforthedotproductofqueriesandkeyscanbecalculatedinthelaterstage.
KDEFormer[51]suggestsreducingthedenominatorofthesoftmaxfunctiontoavariantofthekerneldensityestimation(KDE)problem,andanefficientKDEsolvercanbe
further utilized to acceleratethe multiplicationofthe attentionmatrix withthe value
matrix.The trickis basedonreducingthe number ofcolumns ofthe attentionmatrix
(referredtoasA:=exp(QK⊤/√d))usingimportancesampling.KDEFormerdelivers
a (Tmd) time complexity and (Tm) memory complexity, where m<T is a small

## O O

number.MEGA[52]introducesamovingaverageequippedgatedattentionmechanism
tosolvetheweakinductivebiasandquadraticcomputationalcomplexity.MEGAoffers
12

<!-- Page 13 -->

(cTd) time complexity and (cTd) memory complexity with a theoretical ground-

## O O

ing, where c<T is MEGA’s chunk size of quadratic attention. LoMA [53] introduces
a method for losslessly compressing the memory of transformer-basedlanguage models,allowingforasubstantialincreaseincontextuallengthwithoutalteringthemodel
architecture.Bysegmentinginputsintoreading,memory,andrepetitionareas,LoMA
utilizes a bidirectional attention mask within the memory area to preserve information. The approach achieves up to a 4:1 compression ratio, maintaining the model’s
generative capability through fine-tuning and enabling efficient long-text handling
with minimal data requirements. BiPE [54] introduces a bilevel positional encoding approach that combines intra-segment and inter-segment encodings to enhance
lengthextrapolationcapabilitiesintransformermodels.Thisdesigndisentanglespositionalinformationwithin andbetweensegments,allowingfor moreefficient encoding.
BiPE achieves superior length extrapolation performance with a theoretical advantage, delivering a time complexity of (Td) and memory complexity of (Td) across

## O O

diverse tasks.Simple Linear Attention [55] combines sliding window and linear attention mechanisms, offering a solution to the recall-throughput tradeoff by balancing
memoryconsumptionandtokenrecall.Itdelivers (Td2)timecomplexityandutilizes
a hardware-optimized IO-aware algorithm, achie O ving up to 24× higher throughput
than FlashAttention-2, making it a highly efficient architecture for language generation. Cluster-wise Graph Transformer (Cluster-GT) introduces the Node-to-Cluster
Attention (N2C-Attn) mechanism [56], leveraging Multiple Kernel Learning in a kernelized attention framework to capture node and cluster-level information without
compressing clusters into single embeddings, achieving linear time complexity and
excelling in graph-level tasks by integrating dual-granularity feature maps through
anefficient cluster-wisemessage-passingarchitecture.SageAttention[57]introduces a
novelquantizationmethodspecificallyfortheattentionmechanism,achievingapproximately 2.1× and 2.7× higher OPS than FlashAttention2 and xformers, respectively,
whilemaintainingsuperioraccuracytoFlashAttention3,thusenablingefficientmodel
inferencewithminimalend-to-endperformancelossacrosslargelanguage,image,and
video generationmodels. LocalAttention Mechanism (LAM) [58] leveragesthe continuity of time series data to reduce attention computations, achieving (nlogn) time

## O

and memory complexity, significantly improving upon traditional (n2) complexity,

## O

and demonstrates superior performance in long-horizonforecasting, surpassing stateof-the-art models and addressing the need for new evaluation datasets in time series
forecasting. The proposed Long LoRA Pereceiver (LLP) [59] framework builds upon
the PerceiverAR architecture to effectively cut down the quadratic complexity of
traditional Transformer-based attention, achieving semi-linear time complexity, and
demonstrates notable improvements over existing state-of-the-artmodels, positioning
LLPasacompellingandefficientcorecomponentfornext-generationLargeLanguage
Models. Signformer [60] introduces a from-scratch transformer pipeline with novel
convolution-attention integration, achieving substantial parametric (467-1807x) and
computationalefficiency overcontemporarySOTAs,attaining near-LLM-levelperformance, securing the 2nd place on the leaderboard, and demonstrating the feasibility
of sustainable, edge-deployable sign language translation without reliance on large
pretrained models or extensive datasets
13

<!-- Page 14 -->

Approach Time Complexity Memory Complexity

### Transformer [11] O(T2d) O(T2+Td)


### Reformer [45] O(TdlogT) O(TlogT +Td)

Linear Transformer [46] O(Td2) O(Td+d2)
Efficient Attention[47] O(T2d) O(Td+d2)

### AFT [48] O(Td) O(Td)

Memory Efficient Attention [49] O(T2d) O(dlogT)
KDEformer [51] O(mTd) O(mT)

### MEGA [52] O(cTd) O(cTd)

SimpleLinear Attention[55] O(Td2) O(Td2)

### RWKV[61] O(Td) O(d)

Table 1 Overviewoftimecomplexityandmemorycomplexityimprovementsfor
selectedapproaches overclassicalTransformer.Here,T,ddenote thesequence length
andhiddenfeaturedimension,respectively.musedinKDEformerdenotesmsampled
columnsofattentionmatrix.cusedinMEGAdenotes itschunksizeofquadratic
attention.
3.1.2 Hardware optimized attention.
There is another stream of works focusing on hardware efficient attention operator. Starting from 2021, many works (LightSeq [62], Faster Transformer [63],
xFormers [64]) have been focused on optimizing CUDA implementation of attentions
and transformer layers including kernels fusion, gemm optimization, etc. FlashAttention [65] introduces an IO-aware precise attention algorithm that employs tiling to
minimize thevolumeofmemoryreads/writesbetweenthe highbandwidthmemoryof
theGPUandtheon-chipSRAM.Buildingonthis,FlashAttention-2[66]furtherrefines
FlashAttention by addressing the suboptimal work partitioning concern. vLLM [67]
proposes a novel attention algorithm, PagedAttetion, that mainly optimizes the virtual memoryandpagingtechniques in operatingsystems.MobileLLM[68]introduces
a deep-and-thin modelstructure optimized for on-device use cases,leveragingembedding sharing and grouped-query attention to enhance performance. With innovations
such as block-wise weight sharing, MobileLLM achieves state-of-the-art results for
sub-billionparametermodels,offering (Td)time complexityandmaintainingmodel

## O

efficiency even in memory-constrainedenvironments.
3.2 Non-transformer architecture
WhileTransformers,withtheirself-attentionmechanisms,havedominatedthefieldof
languagemodeling,alternativearchitectureshaveemergedtotacklevariouschallenges
or provide different advantages.
3.2.1 Modular network
Modular Network (also called the Mixture of Experts (MoEs)) [69, 70] technique is
a machine learning approach that combines multiple specialized models, known as
experts,tosolvecomplextasksmoreeffectively.Asweknow,asingledenseLLMitself
contains billions of parameters, which is extremely difficult to be further scaled into
larger parameter sizes. MoE provides a solution to enabling LLM’s parameter size
14

<!-- Page 15 -->

to grow from hundreds of billions into trillions, by sparse routing (also mentioned as
sparse activation, sparse gating). During training, multiple individual expert LLMs
andaroutingfunctionaretrainedsimultaneously.Thelearnedroutingfunctionallows
the MoE system to select a subset of experts according to the input, thus reducing
computational and memory requirements. Switch Transformer [71] follows the principle of “increasing the parameter count while keeping the floating point operations
(FLOPs) per example constant”. Switch Transformer achieves this by replacing the
original dense feed-forward network layer in the Transformer with a sparse Switch
feed-forwardlayer.The Switch layeris essentially similar to [69] architecturebut the
authors simplify the number ofselected experts to 1. GLaM[72] has 1.2T parameters
which is 7X larger than GPT-3 and requires half of the FLOPs for inference. GLaM
is implemented with 64 experts per MoE layer where each input token only activates
96.6B(8%of1.2T)parameters.Differentfromthe SwitchTransformer,itcontainsan
MoE layer interleaved with a traditional Transformer layer in each block of GLaM.
Concurrent works include heterogeneous MoEs [73], MoE-LM [74], Unifed Routing
Network [75].
3.2.2 Other architecture
Researchers have explored more novel dense architectures that are different from the
transformers. Inspired by AFT introduced in Section 3.1, RWKV [61] combines the
efficient parallelizable training of Transformers with the efficient inference of RNNs.
The key idea behind RWKV is to leverage a linear attention mechanism so that the
proposed model can be formulated as a transformer during training and an RNN
duringinference.Ontheotherhand,[76]exploresthepotentialofMulti-LayerPerceptrons trained with the same next-token prediction to achieve non-trivial performance
on text generation and arithmetic tasks. The authors also supply rich theory analysis to connect and compare their proposed architecture to existing transformer-based
architectures, and they argue that the power of LLM can mostly be attributed to
the large-scaleauto-regressivenext-tokentrainingscheme.Hyena[77]proposesa subquadratic drop-in replacement for attention constructed by interleaving implicitly
parametrizedlongconvolutionsanddata-controlledgating.MonarchMixer[78]utilizes
asimpleyetefficientsubquadraticgeneralized matrix multiply algorithms basedarchitecture. Mamba [79] integrates selective state space models into a simple end-to-end
neuralnetworkarchitecturewithoutattentionblocks,achievingcompetitive modeling
powerofTransformerswhilescalinglinearlyinsequencelength.YOCO[80]introduces
a memory-efficient decoder-decoder architecture that caches key-value pairs once,
enabling sublinear scaling in GPU memory consumption and substantially reducing
prefillinglatencyacrosslong-contextlanguagemodels.MatMul-freeLM[81]eliminates
costlymatrixmultiplicationoperationsbyleveragingternaryweightsandelement-wise
Hadamard products, achieving substantial reductions in memory usage and training
latency while scaling to billion-parameter language models. RWKV-edge [82], includinglow-rankapproximation,sparsitypredictors,andclusteringhead,effectivelyreduce
RWKV model size by 4.95–3.8x with a minimal 2.95pp drop in accuracy, facilitating the practical deployment of RNN-based LLMs on resource-constrained devices
15

<!-- Page 16 -->

and demonstratingthe viability ofefficient,high-performing largelanguagemodels in
embedded environments.
4 LLM pre-training
For large-scale LLMs like GPT-4, efficient pre-training is pivotal due to their extensive size and complexity. This efficiency transcends mere speed, focusing on optimal
utilization of computational resources and innovative data management. Combining
advanced hardware, such as GPUs and TPUs, with techniques like data and model
parallelism, the pre-training process is tailored to be resource-efficient. Additionally,
strategieslikeselectivedatasampling,modelpruning,andquantizationplayacrucial
role in minimizing data and memory requirements. These methods collectively contribute tonotonlyacceleratingthetrainingprocessbutalsoensuringsustainableand
cost-effective development of advanced LLMs.
4.1 Memory efficiency
4.1.1 Distributed training
Distributed training proves to be a highly effective approach for accelerating model
training, particularly for machine learning tasks that exceed the memory capacity of
a single accelerator, such as GPU, TPU, and more. In distributed training, the task
oftrainingthe modelisdividedandallocatedto multipleworkingnodes.Thesenodes
concurrentlyexecute localtrainingtasksandcollectively contributeto developingthe
original task.
Data parallelism. Data parallelism (DP) is the most straightforward approach for
distributed training and has been inherently supported by famous machine learning
frameworkslikeTensorFlowandPyTorch.Intheparadigmofdataparallelism,theinitialdatasetisdividedintomultiplepartitions,anddifferentdatapartitionsaretrained
in parallelby multiple accelerators.However,DP has memoryredundancies acrossall
datapartitions,andmodelstatesincludingmodelparameters,gradients,andoptimizer
states are requiredby eachdata partition.Given the substantial size of LLMs,applying DP to LLMs in a naive manner is impractical. To end this, ZeRO [15], PaLM [6]
and Fairscale [83] introduce approaches for enhancing the efficiency of memory utilizationinDP.Insteadofduplicatingtheentiremodelstates,thesetechniquessuggest
partitioning them. Each data partition stores a portion of the model states and can
retrieve additional states from other data partitions with a dynamic communication
schedule when necessary.
Modelparallelism.Modelparallelism(MP)isakindofdistributedtrainingmethod
that aims to minimize a model’s memory footprint by spreading its layers or tensors
acrossmultiple accelerators,while DP primarilyconcernsdata partitioning.Basedon
the partition levels, model parallelism can be categorizedinto two main types: tensor
model parallelism (TMP) and pipeline model parallelism (PMP).
In the context of TMP, tensors can be split along their rows or columns,
enablingconcurrentexecutionofmatrixmultiplicationoperationsacrossallsplitparts.
16

<!-- Page 17 -->

Megatron-lm [16] employs parallelization techniques for matrix multiplication operations within both the multi-layer perceptron (MLP) and the self-attention block of
the transformer layer. In the case of the MLP, the weight matrix is divided along its
columns,while for the self-attentionblock,the Query,Key,and Value parametersare
split in a column-parallel fashion. Alternatively, Mesh-tensorflow [84] split the units
in the hidden layer to achieve tensor MP.
In the case of PMP, a model is divided into multiple layer groups,and eachaccelerator is responsible for handling one of these groups. To minimize inter-accelerator
communication, these groups typically consist of consecutive layers. While naively
implementing PMPcanreduce the memorydemands oneachaccelerator,it is important to note that, due to layer dependencies, most accelerators are idle at any given
time,withonlyoneinactiveoperation.Toenhancetheresourceutilization,GPipe[85]
and PipeDream [86] adopt an approach where a batch is divided into smaller microbatches. PMP is then executed independently on each micro-batch, and gradient
updates occur asynchronously across these micro-batches. BPipe [87] aims to achieve
memorybalanceamongacceleratorsduringthetrainingofPMPbytransferringintermediate activations. Alpa [88] proposes a model-parallel training system for large
deep-learningmodels.Ithasthecapabilitytoautomaticallygenerateparallelexecution
plans that encompass data, operator,and pipeline parallelisms.MegaScale [89] introduces a scalable training systemleveraging3D parallelismand in-depth observability,
achievinghightrainingefficiencyandstabilityacrossover10,000GPUs.ProTrain[90]
executes PMP independently on each micro-batch, allowing asynchronous gradient
updates across these batches, thus enhancing throughput efficiency.
4.1.2 Mixed precision training
Mixedprecisiontrainingisatechniqueusedtoacceleratethetrainingofdeeplearning
models by using both 16-bit and 32-bit floating-point types (as opposed to just using
32-bitor64-bitthroughoutthetrainingprocesssuchasBERT[42]).Thisapproachhas
gainedpopularity,especiallyinthetrainingoflargelanguagemodels,wherecomputationalcostcanbeasignificantbarrier.Recently,topre-trainextremelylargelanguage
models,someworksborrowed16-bitfloating-pointnumbers[91]whichlargelyreduced
memory consumption compared with 32-bit or 64-bit. To mitigate the performance
degradation caused by the quantization with 16-bit floating-point numbers, Scao et
al. [5] proposed Brain Floating Point (i.e., BF16) for training that is able to allocate
more exponent bits and fewer significant bits than FP16.
4.2 Data efficiency
Data efficiency represents how efficiently a training pipeline leverages its data. It
determines the number of iterations (steps) required to complete a training process,
thus affecting the overall training cost. Since existing LLMs such as LLaMA [2] are
usually trained on a large quantity of texts, maximizing the utilization of data offers
a promising solution to reduce training cost.
17

<!-- Page 18 -->

Recent works try to improve data efficiency in various aspects of the training pipeline. We identify three major directions of achieving this goal: importance
sampling, data augmentation, and training objective.
4.2.1 Importance sampling
A current survey [37] notes that importance sampling (data pruning) significantly
influences models’ data efficiency during pre-training.Importance sampling means to
prioritize informative training instances, so it involves estimating per-sample importance. It is also called data pruning. A major solution of importance estimation is
to compute gradient norm [92, 93]. More recent approaches [94, 95] work towards
accelerating the data importance sampling process.
Data-Juicer [96], an LLM data processing system, enables efficient and scalable
dataprocessingto improvethequalityofthe trainingdata.As aresult,the generated
data recipes from Data-Juicer yielded considerable improvements on LLaMA [2] performance in various pre-training and post-tuning cases. Similarly, INGENIOUS [97]
is another system that aims to improve data quality by selecting highly representative subsets of the training corpora. ASTEROID [98], a multi-stage computational
framework, first trains an MLFF (machine learning force fields) model on a large
amount of inaccurate data to captures the sophisticated structures of training data
andthenfine-tunestheobtainedmodelonasmallamountofaccuratedatatoimprove
model performance. Since inaccurate data is cheap while accurate data is much more
expensive,ASTEROIDimprovesdataefficiencybyfullyutilizingthecheapinaccurate
data. LISA [99], a memory-efficient fine-tuning method for LLMs, leverages layerwise
importancesampling toselectivelyupdate modellayers,therebyreducingGPUmemory consumption while outperforming traditional full-parameter tuning and LoRA in
downstream tasks.
4.2.2 Data augmentation
Data augmentation creates modified copies of existing data so that the current data
can be fully utilized. Since it is an effective technique of improving data efficiency,
a joint data augmentation for vision-language representation learning [100] is proposed to improve the existing pre-training pipelines. As an outcome of improving
the data efficiency of pre-training pipelines, researchers of this work also show that
downstreamperformancecanbepositivelyimpacted.Thetrainingofgenerativeadversarialnetworks(GANs) is also benefited by data augmentation[101]. Moreover,work
has been done to augment acoustic data through pseudo acoustic representations of
textual data to improve speech processing [102]. The proposed LLMRec framework
enhancesrecommendersystemsbyleveraginglargelanguagemodelstoaugmentuseritem interaction graphs, item attributes, and user profiles, thereby addressing data
sparsity and improving recommendation accuracy [103]. A novel data augmentation
technique,LLM-DA,leveragesthe textgenerationcapabilities oflargelanguagemodels to enhance few-shot namedentity recognitionby generatingsemantically coherent
and diverse training data [104].
18

<!-- Page 19 -->

4.2.3 Training objective
Arecentsurvey[10]findsthatthechoiceofpre-trainingobjectiveisanotherfactorthat
determinesdataefficiency.Forthedesignofpre-trainingobjective[105],itistypically
a function of model architecture, input/target construction, and masking strategy.
Specifically,representativemaskingstrategiesincludemaskedlanguagemodeling[106],
masked image modeling [107], and language-image pre-training [108]. Researchers of
these worksfind that skipping the processing ofsome maskedtokens cansignificantly
improve training efficiency.
5 LLM fine-tuning
Fine-tuningLargeLanguageModels(LLMs)likeGPT-4forspecializedtasksinvolvesa
criticalbalancebetweenachievingtask-specificperformanceandmaintainingresource
efficiency, given their considerable size and computational demands. This section
discusses various fine-tuning strategies, focusing on optimizing computational load,
memory usage, and energy consumption. Techniques such as parameter-efficient finetuning, which adjusts a limited subset of parameters, offer a resource-conscious
approach, while full-parameter fine-tuning, involving the modification of all parameters, is explored in the context of its higher resource requirements. This exploration
is key to understanding how fine-tuning in LLMs is evolving to address the dual
challenges of performance optimization and resource constraints.
5.1 Parameter-efficient fine-tuning
Parameter-efficientfine-tuning (PEFT) is a technique aimed at making the most out
of an LLM’s vast parameter space without the need to adjust all the parameters
during the fine-tuning process. Given the immense size of modern LLMs, fine-tuning
every parameter can be computationally expensive and may even risk overfitting on
smaller, task-specific datasets. Current PEFT techniques can be categorizedinto two
main streams: 1) Masking-basedFine-tuning and 2) Adapter-based Fine-tuning.
Masking-based fine-tuning.Inthisapproach,onlyasubsetofthemodel’sparametersisupdatedduringthefine-tuningprocess.Therestoftheparametersare“masked”
orfrozen,meaningtheyarenotupdatedduringbackpropagation.Thismaskingcould
be applied to specific layers, certain types of parameters, or parameters identified
throughvariouscriterialikeimportancescores.Previousresearchendeavors[109,110]
have focused on the optimization of fine-tuning procedures for comparatively smaller
language models through the deployment of diverse regularization methodologies.
However,theseapproachesexhibitlimitationswhenappliedtothefine-tuningofLLMs
duetothesignificantlyelevatedcomputationalrequirementsandvoluminousdatasets
essential for the effective training of such models. In addressing these challenges, the
methodknownasCHILD-TUNING[111]employsdatafromthetargettasktoidentify
a subset of parameters—referred to as the “child network”—that are most pertinent
to the task, while preserving the pre-trained values for parameters in the remaining
architecture.Inarelatedvein,alistofmethods[112–114]introducesadynamicparameter selectionpipeline specifically tailoredfor the efficient fine-tuning of LLMs. These
19

<!-- Page 20 -->

works adaptively designate a judicious sub-network for staged updates, leveraging
gradient information from back-propagation, thereby achieving notable performance
enhancements on domain-specific tasks, particularly in resource-constrained environments. To optimize resource usage, MEFT [115] implements sparse activations and a
Mixture of Experts (MoE) approach, dynamically offloading trainable parameters to
the CPUandselectivelytransferringonlythe mostrelevantonestotheGPU,thereby
reducingGPUmemoryloadandcommunicationoverhead.Totackletherankselection
challenge,DyLoRA[116]leveragesadynamic low-rankadaptationapproach,training
LoRA blocks across a spectrum of ranks and enabling rank-specific inference without the need for costly search processes, thus optimizing efficiency while maintaining
performance across a range of model sizes.
Adapter-based fine-tuning. Different from the previous method, in this approach,
additional lightweight layers (adapters) are inserted between existing layers of the
pre-trained model. During fine-tuning, only the parameters of these adapter layers are updated, while the original model parameters are kept fixed [117, 118].
Recent scholarly contributions have focused on Unsupervised Domain Adaptation
(UDA) employing adapter mechanisms to advance the capabilities of pre-trained
models in cross-lingual or multi-task learning contexts. A pioneering approach [119]
involved multi-domain adaptation through a bifurcated strategy: an initial domainfusiontraining phaseemployingMaskedLanguageModel(MLM) lossonacomposite
corpus, followed by task-specific fine-tuning. A subsequent development, UDApter
[120], extended this dual-phase methodology by compartmentalizing it into two distinct adapter modules: a domain adapter for domain-invariant feature extraction,
and a task adapter with static parameters. The underlying architecture was based
onAdapterFusion[121].Another advancement,AdapterSoup[122],further optimized
the adaptation process by utilizing a weight-averaging approach on domain adapters
exclusively during the evaluation stage. Various techniques for domain adapter selectionwereinvestigated,includingexhaustivecombination,textclustering,andsemantic
similarity measures.
Adapters with underlying neural network architectures are commonly referred to
as neural adapters. The seminal design of such adapters is attributed to Houlsby et
al. [117] and consists of a sequential arrangement of down-projection, a GeLU nonlinear activation function [123], and up-projection. These components are integrated
with feed-forward layers to serve as the foundational architecture. Subsequent work
by Bapna et al. [124] streamlined this structure, reducing it to a single hidden-layer
feed-forward network while empirically demonstrating its efficacy in domain adaptation tasks. These adapter modules are strategically positioned after the multi-head
attentionandfeed-forwardlayerswithinthetransformerarchitecture.Variantsofsuch
neuraladaptersarecolloquiallytermedaseitherbottleneckadaptersorserialadapters;
in the present paper, we employ the term ”serialadapters” to refer specifically to the
architecture described in [117].
Finally, Low-rank adaptation (LoRA) [125] is inspired by the observation that
large language models reside on an intrinsic subspace [126], where model parameters
are efficiently updated. Therefore, learning in this subspace significantly reduces the
amount of parameters.LoRA modules implant learnable SVD blocks as the subspace
20

<!-- Page 21 -->

withalowmatrixrankr d,wheredisthedimensionofinputdata.Thematricesare
≪
addedinparalleltothe pre-trainedweights,thuskeepingthemfrozenduringthe finetuning. Notably, LoRA shows superiority in further reducing the number of trained
parameters and introducing no latency during inference.
5.2 Full-Parameter fine-tuning
Asthenamesuggests,intheparadigmoffull-parameterfine-tuning,allmodelparameters are subject to change during training. With a higher training cost than the
PEFT, full-parameter fine-tuning can generally lead to better performance than the
parameter-efficientmethods [127]. However,this phenomenonmay not hold true on a
simple dataset (e.g., a dataset with a lack of language diversity) for a specific downstream task [128]. Since PEFT only trains a relatively small number of parameters,
modelstrainedviafull-parameterfine-tuningmethodshaveagreaterlearningcapacity.
Moreover, the convergence of PEFT is generally not as fast as that of full-parameter
fine-tuning [129]. As for training cost, it is reported [127] that “using full-parameters
fine-tuning requires about 3-5 times the time cost” of LoRA fine-tuning. GPU memory consumption is also a concern because updating all the parameters can be
impractical when dealing with LLMs. The significantly higher training cost of fullparameter fine-tuning poses a challenge for researchers in choosing which method to
use.Asformemorycostduringtraining,severaloptimizationmethodshavebeenproposed, such as Gradient Checkpointing [130], Zero Redundancy Optimizer [15] and
Flashattention [65].
To mitigate the cost of training, many recent works on full-parameter fine-tuning
aim to optimize memory consumption [131, 132], which significantly reduces the barrier of this research. For example, a new optimizer called LOMO (LOw-Memory
Optimization) was proposed [131] to combine gradient computation and parameter
updateinonetrainingstepinordertoimprovememoryefficiency.Stochasticgradient
descent (SGD) was adopted in this method, and a theoretical analysis was provided
to show the effectiveness of SGD on fine-tuning all the parameters of LLMs. As a
result, the full parameter fine-tuning of a 65B model requires less than 192GB GPU
memory (“a single machine with 8×RTX 3090, each with 24GB memory”). LOMO
presentsapracticalsolutiontotrainLLMsinresource-constrainedscenarios.Another
recently proposed optimizer called MeZO [132] estimates gradients using only two
forward passes and fine-tunes LLMs “with the same memory footprint as inference”.
Requiring55GBGPUmemory,itcantraina30Bmodelviafull-parameterfine-tuning.
The HiFT method [133], a hierarchical fine-tuning strategy, addresses GPU memory
constraints in full-parameter fine-tuning of language models by updating only a subset of model parameters at each step. This block-by-block update approach enables
HiFT to achieve comparable performance to conventional full-parameter fine-tuning
with significant memory savings. Notably, HiFT supports the fine-tuning of 7B modelsondeviceswith24GBmemorywithoutadditionalmemory-savingtechniques.This
method,compatiblewithvariousoptimizers,showspotentialasascalableandefficient
solution for large language model adaptation in memory-limited environments.
Researchers are also paying attention to data-centric knowledge injection [134]
when adapting a general-purpose foundation model towards a specific domain such
21

<!-- Page 22 -->

as healthcare. The knowledge injection can be achieved by fine-tuning on domainspecific textbooks, publications, and instructions. As an identified drawback [135] of
full-parameter fine-tuning, trained models can distort their pre-trained features and
underperform on data distributions unseen during fine-tuning.
6 LLM inference
Inference in Large Language Models (LLMs) like the GPT series is a critical stage
wheretrainedmodelsareappliedtogeneratetext,answerquestions,orperformother
language tasks based on their training. With the expansive size and complexity of
thesemodels,enhancingtheefficiencyoftheinferenceprocessisessential.Thissection
examinesvarioustechniquestooptimizeLLMsforinference,focusingonstrategiesthat
reducecomputationalloadandmemoryusagewhilemaintaininghigh-qualityoutputs.
Theapproachesexploredincludemodelcompressionmethodslikepruningandquantization,anddynamicinferencetechniquesthatadaptivelyadjustcomputationbasedon
input data. These methods are crucial for deploying LLMs in real-worldapplications,
where resource constraints and performance requirements are key considerations.
6.1 Model compression
Modelcompressionandaccelerationareprevalenttechniquesinwhicha cumbersome,
slow-performing model is optimized to produce a streamlined version. This refined
model not only requires minimal storage—making it apt for mobile device deployment—but also operates with reduced latency. Moreover, initially training a sizable
modelandsubsequently compressingit canenhance trainingefficiency andbolster its
generalization capabilities.
6.1.1 Pruning
Sparsity, one of the longest-standing concepts in machine learning, was introduced to
the neural network field as early as the 1980s [136]. It was picked up again for “modern”deepnetworksinthelate2010s,firstunderthenameofPruning,withtheprimary
goalofreducinginferencecosts[137].Ingeneral,pruningmethodscanbedividedinto
two categories, i.e., structured pruning and unstructured pruning. Structured pruning targets higher-granularity structures, such as entire neurons, channels, layers, or
rows/columnsofweightmatrices.Structuredpruning results ina modelwith reduced
size thatretainsits originalarchitecturalstructure,makingitmorehardware-friendly
fordeployment.Ontheotherhand,unstructuredpruninginvolvesremovingindividual
weights or connections throughout the model based on certain criteria (e.g., smallest
magnitude weights). Unstructured pruning produces a model with ”holes” or sparse
weight matrices, which require specialized software or hardware for efficient deployment. Recent research efforts have been devoted to combining LLMs with pruning
techniques, aiming to tackle the substantial size and computational costs associated
with LLMs.
Unstructured pruning. Unstructured pruning reduces the complexity of an LLM
by eliminating particular parameters without taking into account its intrinsic organization. This method focuses on individual weights or neurons in the LLM, typically
22

<!-- Page 23 -->

by setting a threshold and nullifying parameters beneath it. Yet, by not respecting the overarching structure of the LLM, it leads to a model with a non-uniform
sparsemakeup.Thisnon-uniformitynecessitatesuniquecompressionmethodstoeffectively store and compute the trimmed model. SparseGPT [138] represents a rapid
unstructured pruning technique designed specifically for LLMs with hundreds of billions of parameters, allowing for operation within mere hours. Remarkably, it can
reduce parameters by as much as 60% without compromising the model’s performance significantly. To address the demanding weight update process of SparseGPT,
Wanda [139] introduces a novelpruning criterion.Wanda assesseseachweightby calculating the product of its magnitude and the norm of its related input activations,
usinganestimationfromaconcisecalibrationdataset.Thiscriterionisusedforintralayer comparisons in linear layer outputs, facilitating the exclusion of less significant
weights in LLMs. In [140], the author proposes a novel dynamic inference scheme,
DynaTran, which prunes activations at runtime with low overhead, which improves
the throughput of transformer inference. The author designed an application-specific
integratedcircuit(ASIC)basedarchitecturecalledAccelTrantoimplementtheDyna-
Tran.Specifically,severalhardware-awaredesignsareproposedincludingmatrixtiling
and various dataflow to improve data reuse. Bai et al proposed SparseLLM [141], a
novelglobalpruning framework for LLMs. Unlike prior methods limited to layer-wise
sparsity, SparseLLM achieves global pruning with a novel optimization design and
demonstrates that global pruning can retain model accuracy while reducing resource
demands, making it advantageous for deployment in large-scale,resource-constrained
environments.
Structured pruning. Structured pruning involves the selective removalof an entire
group of weights. The definition of ‘group’, which makes those amenable to hardware
speedup, could refer to weight blocks, neurons, filters/channels, attention heads, or
otherdedicatedfine-grainedsparsepatterns.[142]introduceLLM-Pruner,apioneering
frameworktailoredforstructuredpruningofLLMsofferingtask-agnosticcompression
and efficient data usage. LLM-Pruner integrates a dependency detection mechanism
to identify interconnected structures in the model. It utilizes an effective importance
estimationapproach,combining bothfirst-orderdataandestimated Hessianinformation. This approach streamlines the selection of prime groups for pruning, enhancing
thecompressionprocedure.[143]proposeLoSparse(Low-RankandSparseapproximation),anovelmodelcompressiontechnique thatapproximatesaweightmatrix bythe
sumof a low-rankmatrix anda sparsematrix.Pruning enhancesthe diversityoflowrank approximations, and low-rank approximation prevents pruning from losing too
many expressive neurons. [144] further considers pruning the hidden dimension (e.g.,
embedding layers, layer normalization) of LLM besides pruning the attention heads
and feed-forward layers. [145] proposed a new structured compression approach for
LLMs,calledZipLM,whichprovidesstate-of-the-artcompression-vs-accuracyresults,
while guaranteeing to match a set of (achievable) target speedups on any given target hardware. Specifically, given a task, a model, an inference environment, as well
as a set of speedup targets, ZipLM identifies and removes redundancies in the model
through iterative structured shrinking of the model’s weight matrices.
23

<!-- Page 24 -->

Contextual pruning While sparsity stands as a viable strategy to mitigate the
burden in LLM inference, existing techniques either necessitate expensive retraining,
compromise the LLM’s intrinsic learning capabilities, or fail to accelerate real-time
performance on contemporary hardware. Zichang Liu et al. [146] postulate that the
applicationofcontextual sparsity — utilizing small,input-dependent sets ofattention
headsandMLPparameterstoapproximatethedensemodel’soutput—canovercome
these challenges.Their investigations confirm the presence of contextual sparsity and
its potential for precise prediction, enabling us to leverage it to hasten LLM inferencewithoutsacrificingmodelqualityorlearningabilitiesincontext.Tocapitalizeon
these findings, they introduce Deja Vu, a system proficient in dynamically predicting
contextualsparsityusingacost-effectivealgorithm.Thissystem,coupledwithanasynchronous and hardware-optimized execution, significantly accelerates LLM inference
times.
6.1.2 Quantization
The quantization-based approach aims to achieve substantial model compression at
the cost of affordable loss of model accuracy. While the conventional method for
representation learning adopts floating-point numbers, quantization converts them
to fewer bits such as integers or other discrete numbers, making models more efficient regardingboth memory and computation, especially suitable for deployment on
resource-constraineddevices. Although this might lead to the loss of model precision
(orquantizationerror)tosomeextent,carefulquantizationtechniquescanachievesubstantial model compressionwith only minimal accuracy degradation.Based on which
module of the model the quantization is applied to, quantization-based methods can
be classified into four scenarios: (1) weight quantization, (2) activation quantization,
and (3) fixed-point quantization.
Weight quantization. The most popular practice for quantizationis weightquantization, which compresses language models by representing model weights using fewer
bits. For example, Lee et al. [147] jointly learned a common quantization grid size
andthedivisionfactorforpre-trainedweightsandperformedelement-wisedivisionon
weights. Instead of quantizing all weights of the model which may lead to moderateto-highquantizationerror,anothernaturalthoughtistoidentifyandquantizeweights
that are not important. Some works perform weight quantization after the training
process.Forinstance,Linetal.[148]identifiedandpreservedonly1%ofsalientweights
by observing activation that can largely reduce the quantization error. Dettmers et
al.[149]andWeietal.[150]identifiedandisolatedoutlierweightsthatpotentiallylead
to large quantization error via different techniques such as filtering sensitivity-based
algorithm [149] or identifying asymmetric presentation and scaling down problematic channels [150]. Some work leverages either activation or model outliers sensitive
to accuracy degrade from weight quantization. For instance, Kim et al. [151] also
employed a sensitivity-based that searches for optimal bit precision assignment and
storesoutliersandsensitiveweightvaluesinanefficientsparseformat.Leeetal.[152]
studiedhowactivationoutlierscanamplifytheerrorinweightquantizationandassign
higher precision to the weights susceptible to quantization caused by activation outliers.Guoetal.[153]handledoutliervalueslocallybysacrificingvaluesnexttooutliers
24

<!-- Page 25 -->

(usually not important) to accommodate those important outliers. Liu et al. [154]
focusedontheweightquantizationofgenerativemodelsbyapplyingdistillationbased
on generations produced by the pre-trained model. Frantar et al. [155] proposed a
one-shot weight quantization method based on approximated second-order information, reducing the bandwidth of the GPT model down to 3 or 4 bits per weight.
Lin et al. [156] proposed DuQuant, a novel quantization strategy that employs rotation and permutation transformations to manage activation outliers more effectively,
achieving state-of-the-art performance for low-bit weight-activation quantization on
variouslargelanguagemodels(LLMs).Shaoetal.[157]proposedOmniQuant,aquantization method leveraging learnable weight clipping and equivalent transformations,
effectively optimizing quantizationforlargelanguagemodels while achievingstate-ofthe-art performance across various low-bit quantization settings. Some works achieve
weightquantizationduringtraining.Forexample,Yangetal.[158]proposeddynamic
stashingquantizationthatdynamicallyquantizestheintermediateresultsbetweenforward and backward processes for a significant reduction of the memory traffic during
training. Yang et al. [159] used low-rank tensor train and tensor-train matrix formatsto representthe embedding tablesandlinearlayersduringtraining.Dettmers et
al. [160] backpropagated gradients through a frozen, 4-bit quantized pre-trained languagemodel into Low-RankAdapters (LoRA) andperformeddouble quantizationby
quantizing quantization constants. Wortsman et al. [161] accelerated and stabilized
large language-visionmodels by reducing the weights to low-bit values, such as using
16-bit precision for weight gradient computation and int8 multiplications for the forward pass and layer input gradient computations. Other works approach to focus on
the pre-trained model. Gong et al. [162] quantized the pre-trained model in a taskagnostic way to obtain a “pre-quantized” model before fine-tuning and froze most of
the quantized weights in the “pre-quantized” model.
Activation quantization. Inadditiontoweightquantization,othertechniquessuch
as activation quantization and fixed-point quantization have been employed to ease
the heavy memory consumption handling LLMs. Activation quantization deals with
quantizingtheintermediatevalues(i.e.,activations)thatariseduringmodelinference.
For instance,Liu et al.[163] proposeda frameworkagnosticto the neuralworkarchitecturebyapproximatingthegradientdescentofactivationcompressiontraining[164]
via a linearized version. Liu et al. [154] not only performed weight quantization but
also quantized activations to 6-bit precision.
Fixed-point quantization. Fixed-point quantization represents weights and activations using fixed-point arithmetic to reduce memory usage and accelerate computations. Yu et al. [165] pruned transformer-based language models to meet the
GPU’saccelerationconstraintofstructuredsparsepatternswithFP16type.Thenthe
floating-point sparse model is quantized into a fixed-point one by quantization-aware
training.
6.1.3 Knowledge distillation
The distillation of domain-specific knowledge from LLMs into more compact neural
networks has emerged as a promising area.Considering the specialty of LLMs, recent
techniques of Knowledge Distillation can be divided into two streams: 1) White-box
25

<!-- Page 26 -->

Knowledge Distillation: the teachermodel’sparametersareavailableto use;2)Blackbox Knowledge Distillation: only the teacher model’s predictions are accessible.
White-box knowledge distillation. This approach not only aims to substantially
decrease inference latency but also to amplify the effectiveness of specialized tasksolving capabilities. A compelling example is the work by Muhamed et al., who
ingeniously compressed a behemoth 1.5 billion-parameter white-box LLM into a far
more manageable 70 million-parameter model. This was specifically engineered for
optimizing Click-Through Rate (CTR) prediction tasks. They introduced an innovative architecture featuring twin-structured BERT-like encoders coupled with a fusion
layer.This allowedfor a seamlesscross-architectureknowledgedistillationfroma singleLLM,yieldingsuperiorperformancemetricsinbothreal-timeonlineandcontrolled
offline environments [166]. In a parallelvein, severalstudies [167–171] havealso made
strides in this field by incorporating a specialized knowledge distillation module during the fine-tuning process of LLMs. This results in a twofold benefit: accelerated
convergence rates and more efficient utilization of computational resources. The distillation module intelligently leverages pre-trained model parameters to expedite the
convergence process, while concurrently training a selective subset of parameters to
effectivelycounteracttheissuesassociatedwithmodelover-parameterization.Extending this concept further, additional works [172, 173] have ventured into the intricate
process of distilling the nuanced chain-of-thought reasoning capabilities inherent in
larger models into their smaller counterparts. This allows the miniaturized models to
inherit a form of cognitive reasoning from their more oversized progenitors, thereby
enhancing their overallutility and performance.
Black-box knowledge distillation. Another line of research on Knowledge Distillation focuses on the somewhat elusive task of distilling knowledge from “black-box”
largelanguagemodels(LLMs)likeChatGPT.Inthesecases,researchersareoftenlimited to interacting only with the model’s predictions, without the luxury of directly
accessing its internal parameters or architecture. This is a particularly challenging
endeavor because the traditional methods of knowledge distillation, which often rely
on structuralsimilarities or parametersharingbetween the teacher and student models,arerenderedinapplicable.Thesetypesofworks[174–178]haveleveragedLLMsas
a query generation machine that directly generate high quality instruction following
queries(andanswers)tofine-tunesmallerLLMs(e.g.,LLaMA).Theobtainedsmaller
LLMs exhibit a stronger instruction-following capability.
6.1.4 Low-rank approximation
Due to low memory cost, low-rank approximation has made the model compression
moreviableandpractical.Acommonapproachissingularvaluedecomposition(SVD).
For a low-rank matrix A Rm×n, where r is the rank of matrix A, there exists
U Rm×r, V Rn×r are ∈ two orthogonal matrices; σ Rr×r is a diagonal matrix
∈ ∈ ∈
with only the non-zero singular values of A. Through SVD, we reduce the memory
cost from O(mn) to O((m+n) r), which is a huge saving in many scenarios.
×
In general, any linear matrix can be approximated through SVD. [179] omit the
diagonal matrix in SVD decomposition and encode the residue of the original matrix
andapproximatedmatrixtoachievebetterperformance.[180]usedlow-rankmatrices
26

<!-- Page 27 -->

to evaluate the parameter importance. They utilize low-rank matrices to formulate
the optimizationproblemandsolveittogetthe approximationofthe originalparameter. [181] applied low-rank approximation to reduce quantization errors. They use
low-rank decomposition to reduce error without a huge impact on the speed of inference of LLM. [182] achieved low-rank approximation through the observation that
data of NLP task is always in low-ranksubspace. They first decompose the matrix of
Feed-forwardpropagationthroughSVDandsolvetheoptimizationproblemtogetthe
needed low-rankmatrices.[183] and [184] use conduct decomposition for layersin the
transformerandGPT-2respectivelythroughtheKroneckerproduct.Itisanewwayof
”multiplication”differentfromthe traditionalmatrixmultiplication.[185]utilizelowrank approximation to reduce the parameters of generative transformers up to 25%.
Thenon-contextualembeddingswillhavefarfewerfeaturescomparedwithcontextual
ones,whichis a hugesavingfor largelanguagemodels.[186]tacklesthe storageproblem of large language models through low-rank approaches. They store embeddings
in low-rank format to reduce the memory cost, making the deployment of LLM in
edgedevicespossible.[187]introducesDLoRA,adistributedfine-tuningframeworkfor
large language models that enhances parameter efficiency and privacy. By offloading
fine-tuning tasks between cloud and edge devices, DLoRA addresses the limitations
of purely cloud or edge-based solutions, ensuring data privacy and reducing computation and communication costs. The Kill and Revive algorithm further optimizes
performance by dynamically tuning only the most responsive parameters, achieving
significant reductions in workload while maintaining accuracy on downstream tasks.
[188]presentsSplitLoRA,anefficientfine-tuningframeworkthatcombinessplitlearning with federated learning to address large model training burdens. By partitioning
the model, SplitLoRA reduces computational demands on client devices while maintaining model accuracy. This framework, which uses LoRA for parameter-efficient
tuning, achieves faster convergence and lower resource use compared to traditional
federated approaches, making it suitable for deployment in resource-limited environments.[189]introduces DEALRec,adata-efficientfine-tuning method forLLM-based
recommendation systems. This approach optimizes few-shot fine-tuning by selecting
influential samples that are representative of full data, balancing both influence and
effort scores to maximize accuracy with minimal data. DEALRec, tested on three
real-world datasets, achieved superior performance over full-data fine-tuning while
significantlyreducingcomputationalcosts,makingiteffectivefordynamicrecommendation environments. [190] explores post-training quantization (PTQ) as a solution
for reducing memory and computational demands of large language models (LLMs).
PTQisappliedacrossthreetypesoftensors—Weights,Activations,andKVCache—to
optimize efficiency while assessing impact on model performance. The study evaluates models from 11 families, such as LLaMA2, Falcon, and Vicuna, across five task
categories, including basic NLP, dialogue, and long-context tasks. Key findings suggestspecificbit-widthquantizationstrategiesthatbalanceperformanceandefficiency,
revealing trends in performance degradation across tensor types and model sizes.
This comprehensive evaluation serves as a guide for selecting quantization methods
suitedto differentLLM applicationsandoffersinsightsinto optimizing modeldeployment under resource constraints. [191] introduces a new post-training quantization
27

<!-- Page 28 -->

(PTQ) method specifically designed for LLMs to run with integer-only operations,
aiming to eliminate floating-point computations. Key components include Fully-
Smooth Block-Reconstruction (FSBR) to stabilize inter-channel variations, Dynamic
Integer-only MatMul (DI-MatMul) for dynamic quantization in matrix multiplication, and specialized integer-only non-linear operators like DI-ClippedSoftmax. This
framework achieves significant inference efficiency while retaining accuracy comparable to floating-point models, demonstrating I-LLM’s potential for resource-limited
deployments on edge devices. [192] introduces an innovative quantization framework
designed to enable high-performance inference for LLMs under various bit-precision
configurations. ABQ-LLM tackles challenges in quantized inference, such as performance degradation at low bit widths and limited support for non-standard precision
formats on GPUs. Key innovations include distribution correctionmethods to handle
quantization-induced distribution shifts and a bit balance strategy to reduce asymmetry issues in low-bit quantization (e.g., INT2). ABQ-LLM outperforms existing
methods like SmoothQuant and I-LLM, demonstrating significant acceleration and
memory efficiency, especially in configurations like W2A8 for LLaMA models.
6.2 Dynamic acceleration
In Section 6.1, we have introduced techniques for reducing the number of parameters in an LLM for inference acceleration. These methods are general and agnostic
to input data, i.e., static for any given input sequence. However, there is another
line of methods that aims to improve the efficiency of LLM inference without reducing the number of parameters. Such methods typically are specific to different input
sequences and we term them as dynamic acceleration methods. In general, existing
dynamic accelerationmethods include 3 categories,i.e., early exit, token pruning,and
token parallelism. Early exist accelerates model inference by terminating inference at
aparticularlayer-basedonsomecriteria,i.e.,makinganLLMshallower.Ontheother
hand, token pruning accelerates inference by skipping some tokens for higher layers
basedontheirimportance,i.e.,makinganLLMinputshorter.Last,tokenparallelism
considers leveraging certain techniques or algorithms to generate multiple tokens in
parallel (opposite to autoregressivefashion that generates each token sequentially).
6.2.1 Early exit
Early exit is an inference acceleration strategy used in neural networks by skipping
the computation of certain layers. The rationale behind early exit is that simper
input samples usually require less calculationto make predictions [193–195]. Pioneering explorations on early exit often rely on defining their own early-exit criterion:
DeeBERT [196] adapts entropy as its exit criterion; RightTool [197] adapts softmax scores of prediction as its exit criterion; PABEE [198] exit inference when the
intermediate predictions of the internal classifiers remain unchanged consecutively.
PCEE-BERT [199] proposes a hybrid early exit criterion that combines confident
scorewithpatiencecounter.Inotherwords,PCEE-BERTwillearlyexitwhenenough
numbers of consecutive intermediate layers are confident. SkipBERT [200] accelerates inference by skipping the computation of shallow layers when precomputed text
28

<!-- Page 29 -->

chunks are met. The Higher layers can be further skipped using the early-exit criterion. Short-Cutting Transformer[201] suggests a linear transformation-basedmethod
tocastintermediaterepresentationsasfinalrepresentations,thusbypassingthetransformer computation in between. Short-Cutting Transformer adapts the same early
exit strategy as in CALM [202], where the LLM early exits when the difference
betweenthehighestandthesecondhighestprobabilitiesisbiggerthanCALM’sconfidencethreshold.MuE[203]extendsdynamicearlyexitstrategytomultimodalLLMs.
Unique challenges arise since existing early exit strategies can not directly apply to
the widely-used unified multimodal architecture with both encoder and decoder, due
to the difficulty of making exit decisions when dependencies between encoder and
decoder exit. MuE proposes its exit criterionbased on the layer-wiseinput similarity,
inspired by the saturation observation [204].
6.2.2 Input pruning
Input Pruning explores the opportunity for the dynamic reduction of input sequence
lengthtoimprovetheTransformer’scomputationalefficiency.Itsintuitionissimilarto
thehumanbeing’sreadingcomprehensioncapabilityitdoesnotreadallwordsequally.
Instead, some words are focused with more interest while others are skimmed. For
Transformermodels,thismeansadoptingadynamiccomputationbudgetfordifferent
input tokens according to their contents.
Existing input pruning works can be categorized into two classes based on token
removal or retention criteria. The first class uses value-based scoring (e.g., attention) to identify unimportant tokens. For instance, SpAtten [205] ranks tokens using
importance scores and retains the top-k highest-scoring tokens. LTP [206] improves
PoWER-BERT by introducing a learnable layer-wise threshold, enabling adaptive
pruning length. ToP [207] overcomes the limitation of inaccurate token importance
ranking in the self-attention mechanism through a ranking-distilled token distillation
technique, which distills effective token rankings from the final layer of unpruned
models to early layers of pruned models.
Thesecondclassoftokenpruningmethodsinsertsapredictionmodulebeforeeach
transformer layer to provide a more accurate token importance score prediction. TR-
BERT [208] introduces a dynamic mechanism for making decisions about skipping
tokens. It is trained with reinforcement learning with a reward that promotes classifier confidence and penalizes the number of retained tokens. Transkimmer [209] is a
notable example that inserts a 2-layer MLP network at each layer as the prediction
module. However, the extra prediction module can also introduce considerable inference latency overhead, which is unfriendly on resource-limited devices. PuMer [210]
proposedatokenreductionframeworkthatusestext-informedpruningandmodalityaware merging strategies to progressively reduce the tokens of input image and text,
improving model inference speed and reducing memory footprint. PuMer learns to
keep salient image tokens related to the input text and merges similar textual and
visual tokens by adding lightweight token reducer modules at several cross-modal
layers in the Vision-Language model. Infor-Coef [211] proposes a model acceleration
approach for large language models that incorporates dynamic token downsampling
and static pruning, optimized by the information bottleneck loss. The token sampler,
29

<!-- Page 30 -->

which is similar to the MLP module of Transkimmer, is trained for downsampling
the token length before the multi-head attention layer. SMART-TRIM [212] incorporates lightweight trimming modules (MLP layers) into the backbone to perform
task-specific pruning on redundant inputs and parameters, without the need for
additional pre-training or data augmentation. LLMLingua-2 [213] proposes a taskagnostic prompt compression method by formulating it as a token classification task.
Despite its small size, it achieves notable speedups, reducing latency by 1.6x-2.9x
with a compression ratio of 2x-5x, while preserving crucial information for effective
promptunderstandingacrossvariousdownstreamtasks.CompressedContextMemory
(CCM)[214]introducesadynamiccontextcompressionmechanismforlanguagemodel
inferencebyintegratinglightweightLoRAduringforwardpasses,achievingamemoryefficientsolutionforexpandingcontextwithoutfine-tuningtheentiremodel.However,
CCM-concat’s higher memory demands at later time steps may be challenging for
memory-constrained environments. GRIFFIN [215], introduced in Prompt-prompted
Adaptive Structured Pruning for Efficient LLM Generation, is a training-free and
calibration-free pruning method targeting transformer feedforward blocks for faster,
memory-efficientLLMinference.Exploitingthephenomenonof“flocking,”whereneuronsshowsimilaractivationsacrosstokensinasequence,GRIFFINselectskeyneurons
during the prompt phase, maintaining model performance even with 50% parameter
reduction. Compared to magnitude pruning and MoEs, GRIFFIN achieves comparable efficiency without training overhead, showing 1.25x-1.29x speed-ups on Llama 2
and Gemma models across classification and generation tasks. LazyLLM [216] is a
dynamic token pruning method aimed at improving LLM inference efficiency for long
contexts. Unlike static pruning, LazyLLM selectively calculates key-value (KV) pairs
only for tokens essentialto predicting the next tokenateachgenerationstep. By progressively pruning tokens during both the prefilling and decoding stages, LazyLLM
reduces time-to-first-token (TTFT) and overall generation time without sacrificing
model accuracy. Tests on the Llama 2 model show a 2.34× TTFT speedup on multidocumentQA,validatingLazyLLM’scapabilitytoaccelerateLLMinferenceefficiently
without fine-tuning
6.2.3 Token parallelism
Inference from large autoregressive models like Transformers is slow - decoding K
tokenstakesKserialrunsofthemodel.Recentworksproposedtoleveragetechniques
such as speculative execution [217] to achieve parallel generation of multiple tokens
instead of a sequential manner. Leviathan et al. [218] introduces “speculative decoding,” an algorithm that accelerates the sampling process from autoregressive models
like Transformers by computing several tokens in parallel without altering the outputdistribution.Thisisachievedbyutilizingapproximationmodels(smallerthanthe
originalLLM)togeneratespeculativeprefixes,whicharethenexpandedbythe larger
target model, thereby accelerating the inference process without compromising the
output quality. SpS [219] follows a similar idea and proposed speculative sampling,
which generates multiple tokens per transformer call and uses a modified rejection
samplingmethod.SpSmaintainstheoutputdistributionwhileacceleratingtheprocess
by 2 to 2.5 times without altering the model itself. Spector et al. [220] introduces an
30

<!-- Page 31 -->

enhanced algorithm called staged speculative decoding to expedite inference in large
languagemodels(LLMs),particularlyinsmall-batch,on-devicescenarios.Themethod
consistsofstructuringthespeculativebatchasatreetodecreasegenerationcostsand
employing an additional stage of speculative decoding to boost performance. These
improvementscollectively yielda 3.16xreductionin single-batchdecoding latency for
a 762M parameter GPT-2-L model without compromising output quality.
7 System design
System design is critical in optimizing Large Language Models (LLMs) like the GPT
series for efficient inference, particularly in resource-constrained environments. This
section explores key strategies such as hardware offloading, which manages computationalresourcesbyleveragingdifferentstoragehierarchies,andcollaborativeinference,
whichpoolsresourcesforenhancedprocessingcapabilities.Italsoexaminesthe adaptation of LLMs for edge devices, highlighting the importance of system design in
maximizingtheefficiencyandscalabilityofLLMsacrossvariousdeploymentscenarios.
7.1 Deployment optimization
Hardwareoffloading.Hardwareoffloadingmeanstransferringtemporarilyunneeded
datainLLMfromfasteracceleratorstosloweryetampleprimaryandsecondarystorage,suchas CPU memory and disk.These data are subsequently reloadedas needed.
ThismethodallowslargeLLMstooperateefficientlyonGPUswithrestrictedmemory
capacity. However, the offloading and reloading processes inherently introduce significant communication overhead.Therefore,effective offloading strategy plays a crucial
role in enhancing overallsystem efficiency. FlexGen [18] can achieve high throughput
bydevelopingalinearprogramming-basedsearchalgorithmthatcanidentifytheoptimal offloading strategy within a defined searchspace of possible offloading strategies.
FlexGenfurtherimprovesthroughputbycompressingboththeweightsandKVcache
for LLMs down to 4 bits. Additionally, FlexGen can be extended to a multi-GPU
setting by adopting pipeline parallelism. DeepSpeed [17] introduced an innovative
technique called ZeRO-Inference to minimize latency and enhance throughput. This
approach involves pining the model weights in either DRAM or NVMe and dynamically streaming each layer into GPU memory for computation as required. For a
multi-GPUs environment, DeepSpeed leverages both tensor parallelism and pipeline
parallelismtoattainoptimalperformance.FastServe[221]designstheoffloadingstrategybasedonthe priorityofthe jobs.Key-valuetensorsassociatedwith lower-priority
jobs are offloaded to host memory, while key-value tensors needed for imminent use
are loaded in advance. LUT Tensor Core [222] introduces a novel software-hardware
co-design to accelerate low-bit LLM inference through a LUT-based mixed-precision
General Matrix Multiplication (mpGEMM) approach. This design leverages operator fusionto minimize precompute overhead,table symmetrizationto reduce memory
storagerequirements, and a bit-serialarchitecture for flexible precisioncombinations,
ultimatelyachievingsuperiorcomputedensityandenergyefficiencycomparedtoconventionalTensorCores.BrainTransformers[223]implementsTransformer-basedLLMs
using Spiking Neural Networks (SNN), introducing SNN-compatible components and
31

<!-- Page 32 -->

synaptic plasticity mechanisms, achieving competitive performance on benchmarks
like MMLU (63.2) and GSM8K (76.3) while offering potential energy efficiency and
biologicalplausibility.Ripple [224]optimizesLLMinference onsmartphonesbyleveragingneuronco-activationtoreorganizeneuronplacementinflashmemory,achieving
up to 5.93× reductions in I/O latency through a two-stage solution combining offline
co-activation pattern analysis and online caching strategies, addressing the intersectionofsparsity-drivenalgorithmsandstorage-levelsystemco-design.TorchTitan[225]
introducesaPyTorch-nativedistributedtrainingsystemwithmodular3Dparallelism,
elastic scaling, and hardware-softwareco-optimization, achieving up to 30
Collaborative inference. Collaborative inference involves the cooperative effort of
multiple users or systems working collectively to conduct inference tasks for LLMs.
Each participant contributes their resources, such as computing power or data. This
collaborativeapproachservestomitigatetheconstraintsofindividualusersorsystems,
ultimately leading to more efficient and accurate inference when dealing with LLMs.
PETALS [226] is a system that facilitates collaborative inference and fine-tuning of
LLMs through online collaboration among multiple users. Each participant in this
system can take on the roles of a server,a client, or both. Servers host specific model
layers and respond to client requests. Also, an 8-bit compression technology is used
for lowering the computational resources requirement and improving efficiency.
7.2 Support infrastructure
Libraries. In this section, we introduce several famous frameworks for LLMs.
Microsoft introduced DeepSpeed [17] as a cutting-edge deep learning optimization
library that incorporates a range of innovative technologies, including ZeRO and 3D
Parallelism. These technologies enable efficient and effective training, inference, and
compressiontasks.Megatron-LM[16],developedbyNVIDIA,isanotherfamousframeworkforLLMs.Itimplementsacombinationofmodelanddataparallelismandfocuses
onmulti-nodepre-trainingoftransformer-basedmodelslikeGPT.DeepSpeedoffersan
enhancedversionofMegatron-LMthatincludesadditionalfeaturessuchasMoEmodel
training and Curriculum Learning. Like DeepSpeed and Megatron-LM, Colossal-
AI [227]providesmulti-levelparallelismstrategiesfor large-scaledistributedtraining.
ThesestrategiesencompassAuto-Parallelism,data,tensor,pipeline,andsequenceparallelism. Additionally, its heterogeneous memory management component enhances
training efficiency in distributed environments with heterogeneous devices. Mesh-
TensorFlow [84] is a user-friendly framework seamlessly integrated with TensorFlow,
specializing in model parallelism with a primary emphasis on distributed tensor computations. GPT-NeoX [228] builds upon Megatron-LM and incorporates innovations
fromDeepSpeed.MaxText1 isanopensourceopen-sourceframeworkthatisdesigned
for Google Cloud TPUs. Alpa [88] can automatically parallelize users’ single-device
code ondistributedclusters with data,operator,andpipeline parallelism.TransformingtheHybridCloudforEmergingAIWorkloads[229]envisionsafull-stackco-design
ofhybridcloudsystemsincorporatinggenerativeandagenticAI,edge-to-cloudintegration,quantumacceleration,andunifiedabstractions,aimingtocreatesecure,efficient,
1https://github.com/google/maxtext
32

<!-- Page 33 -->

and sustainable platforms that foster breakthroughs in AI-driven research and applications across academia, industry, and society.LLMServingSim [230] simulates LLM
inference serving at the granularity of iterations to capture dynamic workload variations, leverages computation redundancies across decoder blocks to avoid repetitive
simulations, and provides a flexible framework for exploring heterogeneous processor
designs, achieving less than 14.7
Edge devices. In recent research, there is a growing interest in deploying LLMs on
edge devices, which typically have limited computational resources. Xu et al. [231]
explore the use of techniques like Low-Rank Adaptation and Noise Contrastive Estimationto reduce the memory demands ofLLMs when running them on edge devices.
Furthermore, they introduce a novel approach for reducing noise by minimizing data
payload size within the setting of Differential Privacy and Federated Learning (FL).
Woisetschl¨ager et al. [232] gives a comprehensive analysis of the feasibility of conducting Federated Learning with LLMs on contemporary edge computing systems,
offering a comparison to traditional data-centralized computing approaches. Shen et
al. [233] leverages cloud-deployed LLMs to coordinate models that meet user needs
and perform training via edge federated learning. EdgeFormer [234] interleave attention modules with a shared feed-forward network in the decoder layer to achieve
cost-effective parameterization. ProFormer [235] utilizes the LSH projection layer to
replacetraditionalembeddinglookuptables,therebymitigatingtheneedforextensive
memory resources.GhostBERT [236] employs1-dimensionalconvolutionsto generate
additionalfeatures,therebymitigatingmemoryandcomputationalexpenses.Squeeze-
BERT[237]adoptsoptimizationtechniquesusedincomputervisionnetworks,suchas
groupedconvolutions,to achievenotable speedups. LiteTransformer[238]reduces the
computation of the transformer base model by isolating local feature extraction from
globalfeatureextraction.MobileLLM[239]achievessignificantaccuracyimprovements
forsub-billionparametermodelsbyprioritizingdepthoverwidthandleveragingtechniques like weight-sharing and grouped-query attention to enhance performance with
minimal memory overhead.EdgeShard[240] optimizes LLM inference by partitioning
models across heterogeneous edge devices and cloud servers, leveraging collaborative
edge computing to reduce latency and increase throughput. Any-PrecisionLLM [241]
leverages post-training quantization and incremental upscaling to minimize deployment costs by supporting multiple quantized LLMs of varying bit-widths, all within
a memory footprint comparable to a single model. The Breakthrough Memory Solutions[242]enhanceLLMperformancebyintegratingprocessing-in-memory(PIM)and
processing-near-memory (PNM) technologies, significantly boosting memory bandwidth and reducing energy consumption for large-scale AI applications. MELTing
point [243] enables efficient mobile execution of LLMs by leveraging a benchmarking
infrastructure that traces memory and energy usage, optimizing for on-device inferenceacrossvariousmobileandedgedevices.Theproposedmodelin [244]reducesthe
communicationoverheadandmemoryconsumptioninfederatedlearningbyintroducing partial embedding updates and low-rank adaptation, enabling efficient training
of large-vocabularymodels on resource-constraineddevices. LLMS [245] reduces context switching latency in mobile LLM services by employing chunk-wise KV cache
compression,recompute pipelining, andlifecycle management,enabling efficient large
33

<!-- Page 34 -->

language model execution on resource-constrained devices. LocMoE [246] optimizes
large language model training by introducing locality-based routing and communication strategies,reducing training time and enhancing loadbalance without sacrificing
modelaccuracy.JetMoE[247]reducesinferencecomputationbyleveragingsparseactivation in both attention and feed-forward layers, activating only a subset of experts
for each input token, leading to a 70% reduction in computation compared to dense
models like Llama2-7B.Baiet alproposedFedSpaLLM [248], an innovative approach
topruninglargelanguagemodelsinfederatedlearningsettings,addressingtheunique
challenges of model and system heterogeneity. Key contributions include an aggregation function based on the ℓ -norm for managing diverse pruning masks across
0
clients and a novel layer-sampling strategy that ensures efficient resource utilization
while maintaining the accuracyof the globalmodel. This frameworkallowsfor a flexible yet robust pruning process, enhancing model personalization and scalability in
federated environments. FusionLLM [249] enables efficient decentralized training of
large DNNs across geo-distributed GPUs by representing models as operator DAGs,
usinganOP-Fencescheduler,andimplementingadaptivecompressionwithAdaTopK,
achieving up to 9.39x speedup in training ResNet-101 and GPT-2 on heterogeneous
networkedenvironments.Chat AI [250] seamlesslyintegrates HPC infrastructure and
cloud-based web services for privacy-preserving, real-time LLM serving, leveraging
Slurm’s batch scheduling to efficiently utilize GPU resources and incorporating an
SSH ForceCommand-based circuit breaker for enhanced security.
7.3 Other systems
Tabi [251] proposes an inference system with a multi-level inference engine to reduce
theinferencelatencyofLLMs.Insteadofusingthesamemodelforallthequeries,Tabi
avoids invoking costly LLMs by employing multiple DNNs to handle heterogeneous
queries within a task. Z. Peng et al. [252] leverage leveraging min-hash technique to
improve the efficiency and scalability of near-duplicate sequence search for LLMs.
8 Technique categorization by resources
In this section, we explore various techniques applied to Large Language Models
(LLMs)toenhancetheirefficiencyinusingdifferentresources.Thefocusisonfivekey
resources: computation, memory, energy, financial cost, and network communication.
Eachtechnique discussedplaysavitalroleinoptimizingresourceefficiencyforLLMs.
The extent oftheir impact,whether director indirect, variesbasedon the resourcein
question. The table 2 provides a comprehensive mapping of these relationships.
8.1 Computation efficiency
Computation efficiency in LLMs is crucial for faster training and inference. Techniquesliketransformerarchitectureswithapproximatedandhardware-awareattention
directly enhance computation efficiency by reducing the complexity of operations.
Approximated attention mechanisms, for instance, simplify the computationally
34

<!-- Page 35 -->

MainCategoryTechnique Sub-Category Computation Memory Energy Money Communication
ApproximatedAttention XXX XXX X X

### TransformerArchitecture§3.1

Hardware-awareAttention XXX XXX XXX X

### ModularNetwork XXX X X X

Non-transformerArchitecture§3.2
OtherArchitecture XXX X X X

### DataParallelism X XXX X

DistributedTraining§4.1.1

### ModelParallelism X XXX X

Mixed-precisionTraining§4.1.2 X XXX X X
TrainingObjective X X

### DataEfficiency§4.2


### DataAugmentation X X

Parameter-efficient Adapter-basedFine-tuning X XXX

### Fine-tuning§5.1


### Masking-basedFine-tuning X XXX

Full-parameterFine-tuning§5.2 X XXX X
UnstructuredPruning XXX XXX X

### Pruning§6.1.1

StructuredPruning XXX XXX XXX

### Contextual Pruning XXX XXX

WeightQuantization X XXX XXX X

### Quantization§6.1.2


### ActivationQuantization X XXX XXX

Fixed-pointQuantization X XXX XXX
White-boxdistillation X XXX
KnowledgeDistillation§6.1.3

### Black-boxdistillation X XXX

Low-rankApproximation§6.1.4 XXX XXX

### EarlyExit XXX X X

DynamicInference§6.2

### InputPruning XXX X


### TokenParallelism XXX X

HardwareOffloading XXX XXX

### DeploymentOptimization§7.1


### CollaborativeInference X XXX X XXX

Table 2 MappingofResourceEfficiencyTechniques toKeyResourcesinLargeLanguageModels:Thistablepresentsadetailed
overview ofvarioustechniques employedintheoptimizationofLLMs,categorizingthem bytheirmainandsub-categories.Bold
checkmarks (XXX)indicatedirectimpactsandregularcheckmarks (X)indicateindirectimpactsontheresources.
35

<!-- Page 36 -->

intensive attention calculations, thus speeding up the process. Hardware-aware optimizations tailor models to exploit specific hardware capabilities, leading to more
efficient computation. Unstructured, structured, and contextual pruning also directly
impacts computation efficiency by eliminating redundant computations through the
removal of less important weights or neurons. Indirect impacts are observed in data
parallelism and parameter-efficient fine-tuning, where the distributed workload and
reducedparameterupdatesrespectivelycontributetooverallcomputationalefficiency,
albeit as a secondary effect.
8.2 Memory efficiency
Memory efficiency is critical, particularly for deployment on resource-constrained
devices. Techniques like pruning and quantization explicitly target memory efficiency
by reducing the model size. Pruning methods eliminate unnecessary weights, and
quantizationreducestheprecisionofweights,bothleadingtosubstantialmemorysavings. Knowledge Distillation, where a smaller model is trained to mimic a larger one,
alsodirectlyimprovesmemoryefficiency.Indirectcontributionscomefromdistributed
training, where data and model parallelism effectively manage memory usage across
multiple devices, reducing the burden on individual units.
8.3 Energy efficiency
Energy efficiency is increasingly important in the context of sustainable AI. Structured pruning and quantization are directly beneficial, as they reduce the number of
operations and the data size, leading to lower energy consumption for both training
and inference. Contextual pruning, which adapts the pruning process based on the
context, also leads to energysavings by minimizing unnecessary computations.While
primarily aimed at computational efficiency, techniques like approximated attention
indirectly contribute to energy savings due to the reduced computational load.
8.4 Financial cost efficiency
Financial cost efficiency is an indirect but significant benefit of various resourceefficient techniques. Data efficiency methods, such as optimized training objectives
and data augmentation, indirectly reduce costs by improving the effectiveness of
the data used, leading to potentially shorter training times and less computational
resource usage. Dynamic inference techniques like early exit and input pruning indirectly contribute to monetary efficiency by reducing the operational demands during
the inference phase, which can lower the overall deployment costs. In addition to
those techniques introducedearlier,some recentworks exclusivelyminimize the monetary cost. For example, SpotServe [253] is a novel system for serving generative
large language models (LLMs) on preemptible GPU instances in the cloud, which
are more cost-effective but less stable than regular instances. SpotServe dynamically
adjustsLLMparallelizationtomanageinstanceavailabilityandworkloadfluctuations,
optimizing for throughput, latency, and cost. It also employs a unique approach for
instance migration, minimizing communication costs, and utilizes stateful inference
36

<!-- Page 37 -->

recoveryto efficiently resume operations after preemptions, ultimately reducing costs
by 54% and improving latency compared to existing systems.
8.5 Network communication efficiency
In distributed training environments,network communicationefficiency becomes crucial. Mixed-precision training explicitly addresses this by reducing the size of data
that needs to be communicated between processors, directly impacting the efficiency
of data transfer. Techniques like weight quantization also have a direct impact by
minimizing the data payloadduring communication. Collaborativeinference, anindirect approach,enhances communication efficiency by distributing inference tasks in a
manner that optimizes data transfer and processing across the network.
9 Benchmark and evaluation metrics
9.1 Evaluation metrics
Evaluating the resourceefficiency oflarge languagemodels (LLMs) involvesconsidering a multifaceted range of metrics. We provide a comprehensive analysis of various
metrics in this section.These metrics collectively offer a holistic understanding of the
resourceefficiencyoflargelanguagemodelsandarecrucialforguidingmodelselection
based on specific application requirements.
9.1.1 Computation
•
FLOPs(Floating-pointoperations)representsthenumberofarithmeticoperations
on floating-point numbers, providing a quantifiable measure of the computation
efficiency. In the context of LLMs, FLOPs capture the complexity of their internal
computations, including attention mechanisms, feed-forward layers, and activation
functions [254, 255].
•
Training time refers to the total duration required to train an LLM, typically
measuredinwall-clockminutes,hours,ordays [46,65].Itreflectsthemodel’scomplexityandrevealstheefficiencyofthetrainingalgorithmsandhardware.Optimized
algorithmsandhardwarecansignificantlyreducetrainingtime,makingLLMsmore
accessible and affordable.
•
Inference time/latency quantifies the time it takes for an LLM to generate
an output after receiving an input. It is typically measured in wall-clock time or
CPU/GPU/TPU clock time in milliseconds or seconds and can be accessed in
two ways: 1) end-to-end latency [67] and 2) next token generation latency [256].
The inference time is crucial for evaluating the practical applicability of LLMs in
real-worldscenarios, particularly those with time-sensitive interactions.
•
Throughput quantifies the model’s efficiency in processing requests. It defines
the rate at which LLMs can generate output tokens or complete tasks, typically
measured in tokens per second (TPS) [67, 226] or queries per second [257, 258].
A high throughput indicates an LLM’s ability to handle multiple requests quickly,
makingitsuitableforhigh-volumeapplicationslikereal-timechatbotsorlarge-scale
content generation.
37

<!-- Page 38 -->

•
Speed-up ratiomeasurestheimprovementininferencespeedcomparedtoabaseline model, typically expressed as a multiple (e.g., 1.2x, 3.5x) [62, 63]. The ratio
is calculated as the quotient of the baseline execution time to the time taken by
the improved LLM or the quotient of the improved LLM’s throughput to that of
the baseline model. The speed-up ratio draws a relative comparison between the
two models, which offers a quantitative measure of progress in optimizing model
architectures, training algorithms, and hardware optimizations.
9.1.2 Memory
•
Number of parameters represents the number of adjustable variables in the
LLM’s neural network.A higher number of model parameters generally indicates a
morecomplexmodelwithagreatercapacitytolearnandrepresentintricatepatterns
in the data [11, 74]. However, this complexity often comes at a cost of increased
computational and memory requirements.
•
Model size of an LLM is determined by the storage space requiredfor storing the
entire model. It directly correlateswith the number of parametersandis also influenced by the model’s architecture, training data size, and any additional resources
itneedstorun.Themodelsizeisoftenmeasuredbythepeakmemoryusageduring
trainingorinference [49,51],whichcanbeeasilyobtainedthroughsystemmonitoring tools. Similar to the number of parameters,largerarchitectures,and more data
have been able to continuously improve transformer models’ performances [42],
but this canbecome a limiting factor,especially when dealing with extremely large
models that may not fit into the memory of standard hardware.
9.1.3 Energy
•
Energy consumption of an LLM is typically expressed in Watt-hours (Wh) or
Joules (J), reflecting the electrical power used during the LLM’s lifecycle. [259]
proposed a method to calculate the total power consumption by combining GPU,
CPU,andDRAMconsumptionandmultiplyingitbythePowerUsageEffectiveness
(PUE),accountingfortheadditionalenergyrequiredtosupporttheentirecompute
infrastructure.
•
Carbon emission captures the greenhouse gas emissions associated with the
model’s energy usage. It can be calculated by multiplying the energy consumption
(kWh) by the carbon intensity, the grams of carbon dioxide or equivalents emitted
per kWh of energy used (gCO /kWh) by the local power grid.
2eq
CodeCarbon [260], carbontracker [261], and experiment-impact-tracker [262]
are availablesoftwarepackagesdesigned for real-time trackingofenergy consumption
and carbon emissions. Other tools like MLCO2 Impact [263] and LLMCarbon [264]
leverage machine learning to predict the energy usage and carbon footprint before
actual training, enabling more informed resource allocation.
However,focusing solely on training overlooksthe full picture. It is encouragedto
report the energy consumption and carbon footprint during all stages of an LLM’s
lifecycle: while energy consumption during the training and development phases can
be substantial, its significance may diminish when compared to the cumulative lifetime costs of inference if the model is utilized intensively in production. BLOOM [5]
38

<!-- Page 39 -->

highlights this holistic perspective, demonstrating the significant impact of life cycle
assessment in accurately quantifying environmental costs.
9.1.4 Financial cost
While the financial cost of developing and deploying LLMs is rarely reported by
researchers,understanding it is valuable for prioritizing researchdirections based on
cost-effectiveness, encouraging collaborationto optimize resource allocation, and
promoting responsible LLM development. We propose a novel metric dollars per
parameter for this measure.
•
Dollars per parameter is a scaled metric for the financial cost of an LLM. It is
obtainedbydividingthetotalcostoftraining(orrunning)theLLMbythe number
of parameters. It accounts for differences in model size and complexity, allowing
for fairer comparisons of cost efficiency between different models. Researchers may
consider reporting not only the cloud compute and electricity cost [259] and the
hardwareand softwareexpenses associated with training and running, but also the
personnel costs involved in data collection, model architecture, and fine-tuning.
9.1.5 Network communication
•
Communication volume refers to the total amount of data (in megabytes, gigabytes, etc.) transmitted across the network during a specific LLM execution or
training run [265]. Measuring it involves monitoring network traffic between connected nodes, often employing dedicated software or system logs. Monitoring the
communication volume is important for distributed LLMs, as high communication
costs can lead to bottlenecks, slowing down training and increasing infrastructure
expenses.
9.1.6 Other metrics
•
Compression ratio quantifiesthe reductionin size ofthe compressedmodelcompared to the original model. It can be expressed in the percentage of size reduced
[137, 144] or the percentage of weights remaining [143]. High compression ratios
without significantly compromising the performance indicate better compression
efficiency, which facilitates deployment across diverse platforms, including those
with limited computational resources.
•
Loyalty andFidelity aretwosimilarmetrics proposedby [266]and [267]respectivelytomeasuretheresemblancebetweentheteacherandstudentmodelsinterms
of both predictions consistency and predicted probability distributions alignment.
Forlargeteachermodels,enhancementsinfidelityleadto improvementsingeneralization:thestudent’sabilitytopredictpreviouslyunseen,in-distributiondata [267].
Achievinga highloyalty(orfidelity)is alsoimportantforpreservinga model’sfairness,asrecentworkshowedthatmodelcompressioncanamplifyexistingalgorithmic
bias [268].
•
Robustnessis another important but rarely reportedmetric. [266] used two metrics: after-attack accuracy and query number to evaluate robustness. After-attack
accuracy measures the model’s post-attack performance, while the query number
39

<!-- Page 40 -->

reflects the complexity of the attack required to succeed. Evaluating the robustnessofLLMsis crucialto ensurereliabilityinreal-worldapplications,especiallyfor
compressed models, as [269] found smaller deep neural networks tend to be more
vulnerable to adversarial attacks, where slight input modifications can manipulate
their output.
•
Pareto optimality [270]is achievedby strikingan optimalbalancebetween variouscompetingfactors.Itoffersasystematicapproachtobalancetrade-offsbetween
resource efficiency and task performance by identifying solutions that reside on
the Pareto frontier [271] — the boundary that delineates optimal trade-offs. This
concept is especially meaningful as it provides a principled framework for decisionmaking,allowingresearchersto navigatethe intricatelandscapeofLLMsandmake
informedchoices.Forexample, [272]examinedthetrade-offsbetweencostandaccuracy with the Paretofrontier, identifying the most practical real-worldinformation
retrievalmodels.[273]exploredtheParetofrontierbetweenperformanceandFLOPs
to determine whether and how much a method achieves Pareto improvement.
9.2 Benchmarks
The evaluations of LLMs’ resource efficiency currently rely heavily on general NLP
benchmarks2,suchasGLUE [275],SuperGLUE [276],WMT [277,278],andSQuAD
[279, 280]. While the existing general NLP benchmarks offer valuable insights into
a model’s performance on various tasks, they often fail to capture the nuances of
resource-efficient approaches. We present a few benchmarks that involve efficiency
considerations; however, there is still a need for more comprehensive and specialized benchmarksfor LLMefficiency evaluations.These benchmarks shouldgobeyond
traditionalmetricsandaddressthe uniquechallengesassociatedwiththeefficientutilization of computational resources,memory, energy consumption, financial cost, and
communication overhead.
•
Dynaboard [258] is anopen-source dynamic benchmark that allows users to submit NLP models to be evaluated in the cloud, enabling real-time interaction and
a more comprehensive assessment of model quality. Submitted models are evaluated on a combination of datasets across four tasks: Natural Language Inference,
Question Answering, Sentiment Analysis, and Hate Speech. In addition to accuracy,Dynaboardalsocollectsadditionalmetricssuchasmemoryusage,throughput,
fairness,androbustness.Modelsarerankedaccordingtoanovelutility-basedaggregation of these metrics called Dynascore, which can be customized by leaderboard
creators by assigning weights that reflect the relative importance of each metric.
•
EfficientQA [281] is an open-domain Question Answering (QA) challenge at
NeurIPS 20203 that focuses on building accurate, memory-efficient QA systems. It
promotes efficient memory usage through three restrained tracks based on model
size and accuracy: the most accurate model under 6 GB, the most accurate model
under 500MB, andthe smallestmodel that achieves25%accuracy.The model size
is measured as the Docker image size that contains the complete, self-contained
question-answering system.
2ForanextensivecollectionofgeneralNLPbenchmarks,refertoacomprehensiveoverviewby [274].
3https://efficientqa.github.io/
40

<!-- Page 41 -->

• SustaiNLP 20204 Shared Task [282]encouragesparticipantstodevelopenergyefficient NLP models. It uses SuperGLUE [276] to access the model’s performance
across eight diverse NLU tasks. In addition to standard SuperGLUE metrics, this
challenge uniquely evaluates the energy consumption of each submission during
inference using [262]’s experiment-impact-tracker.
•
ELUE (Efficient Language Understanding Evaluation) [273] is a benchmark and
platform designed to evaluate and compare the efficiency of various NLP models.
It covers six NLP datasets spanning Sentiment Analysis, Natural Language Inference, Similarity, and Paraphrasetasks.ELUE supports online evaluation for model
performance, average FLOPs, and the number of parameters. While Dynaboard
[258] andEfficientQA [281] submissions requirethe containerizedmodel along with
its required environment, ELUE only requires the model definition file in Python,
which is less costly for users to upload.
•
VLUE (Vision-Language Understanding Evaluation) [283] is a multi-task multidimension benchmark for evaluating vision-language model (VLM)s. It covers a
set of fundamental vision language tasks: Image-Text Retrieval, Visual Question
Answering,VisualReasoning,andVisualGrounding,andmaintainsanonline platformandleaderboardforevaluationandcomparisonofvision-languagepre-training
(VLP) models. Notably, VLUE measures both performance and inference time
andevaluatesthe efficiency-performancetrade-off,providinga morecomprehensive
assessment of VLMs’ practical value.
• Long-Range Arena (LRA)5 [284] is a benchmark suite specifically designed for
evaluating the performance of efficient Transformer models on long-context tasks.
Itfeaturesavarietyoftasksthatrequirereasoningoverlongcontexts,rangingfrom
1,000to16,000tokensinlength.Thesetaskscoverdifferentmodalitiesliketext,naturallanguage,synthetic images,andmathematicalexpressions,andinvolvevarious
reasoningtypes like similarity,structural,and visual-spatialreasoning.Evaluations
can be run under controlled resource constraints like memory budget or execution
time limit. This forces models to be efficient within these limitations, highlighting
their ability to optimize performance under real-worldconstraints.
•
Efficiency-aware MS MARCO is a post-hoc leaderboard created by [272] for
the MS MARCO information retrieval (IR) benchmark [285] to include efficiency
metrics such as average per-query latency and the corresponding cost budget in
addition to accuracy to provide a more holistic evaluation of IR systems. Following
[258], [272] ranked the models using an aggregationof accuracy, latency, and cost,
expressed as a Dynascore.
10 Open challenges and future directions
As the field of Large Language Models (LLMs) continues to advance, it faces a multitude of open challenges that pave the way for promising research directions. This
section elaborates on these challenges and potential avenues for future exploration.
4https://sites.google.com/view/sustainlp2020
5https://github.com/google-research/long-range-arena
41

<!-- Page 42 -->

10.1 Managing resource type disagreements
AcomplexchallengeinoptimizingLargeLanguageModels(LLMs)isthereconciliation
of conflicting resource demands. Various optimization techniques introduce trade-offs
between different performance metrics [146, 155, 173, 180]. For instance, some methods might enhance computational efficiency at the cost of increasing the number of
model parameters or vice versa [125, 160]. Additionally, strategies that reduce computational operations could inadvertently lead to higher memory requirements due
to the complexities involved in managing sparse data structures [138, 146]. The key
challenge,therefore,istodevelopaholisticoptimizationstrategyforLLMs.Thisstrategy should balance multiple objectives, including computational efficiency, parameter
count, and memory usage, ensuring that improvements in one area do not disproportionately compromise performance in another. Achieving this balance is essential
for the advancement of LLMs, making them both efficient and practical for diverse
applications.
10.2 Combining techniques for resource efficiency
In the realm of Large Language Models (LLMs), a significant challenge lies in effectivelyamalgamatingthediversearrayofavailablemethodstoenhanceoverallresource
efficiency. While numerous techniques exist to optimize different aspects of LLMs,
there’s a notable scarcity of research on how these methods can be cohesively combined. For instance, Ford et al. [286] propose a methodology to integrate energy
efficiency analysisinto softwaredevelopmentcycles,whichis relevantfor the development of efficient LLMs. Similarly, Xie et al. [287] discuss the integration of resource
allocation and task assignment for optimizing business processes, a concept that can
be applied to the management of LLM resources. An integrative approach that systematically brings together various strategies could markedly improve the efficiency
of these large models. This approach could draw from the insights of [288], who surveyed computational intelligence-based optimization and game theory approaches for
resourceallocationincomputing environments.This couldinformthe developmentof
strategies for efficient resource utilization in LLMs.
10.3 Standardized and unified evaluation
AcriticalchallengeintherealmofLLMsistheabsenceofuniversallyacceptedbenchmarksspecificallytailoredforevaluatingtheresourceefficiencyofthesemodels.While
several benchmarks exist for assessing aspects like model compression and acceleration [258, 281],they fall shortof providinga comprehensiveandconsistentevaluation
of resource efficiency. This shortcoming is due to varying factors such as differences
in speed-up ratios, the number of parameters, accuracy levels, and even the type of
hardware used in different studies. These discrepancies highlight the urgent need for
standardized benchmarks that are designed with a focus on resource efficiency. Such
benchmarksshouldfacilitatedirectcomparisonsandenablemoreaccurateandholistic
analyses of how various LLMs utilize computational resources, including aspects like
42

<!-- Page 43 -->

energy consumption, memory usage,and processing power.Establishing these benchmarks is essential for advancing the development of more resource-efficient LLMs, a
key priority given the increasing size and complexity of these models.
10.4 Explainability and robustness
ThepursuitofefficiencyinLargeLanguageModels(LLMs)bringstotheforeconcerns
about their explainability and robustness, echoing issues identified in earlier research
on pre-trained language models. For instance, while some techniques significantly
improve performance in reasoning tasks, there is often a lack of clarity regarding the
underlyingreasonsfortheireffectiveness[289,290].Thisobscurityhighlightstheneed
for integrating explainable approaches into the development of efficient LLMs. Such
integrationwouldaddressthe dualneeds ofinterpretability andsimplified evaluation,
thus enhancing the reliability and predictability of LLMs in real-world applications.
The goalis to developmethods thatnot only optimize resourceuse but also maintain
a level of transparency and resilience, ensuring that these models can be trusted and
easily understood in various deployment scenarios.
10.5 AutoML for resource-efficient LLMs
The integration of Automated Machine Learning (AutoML) into the development
of resource-efficient Large Language Models (LLMs) represents a burgeoning field
of interest. Traditional methods for enhancing resource efficiency in LLMs, such as
knowledge distillation, pruning, weight sharing, and low-rank factorization, typically
rely on expert-driven heuristics and intricate manual interventions [146, 159, 180].
For instance, designing effective loss functions for knowledge distillation or determining saliency scores for pruning involves a considerable amount of human judgment
and expertise [138, 173]. To mitigate this reliance on human input, there’s a growing
emphasis on applying techniques like Meta-Learning [291] and Neural Architecture
Search(NAS) [292]. These AutoML strategies showpromise in automating aspects of
model optimization. By doing so, they could significantly reduce the need for manual
hyperparametertuningandbespokemodeldesign,potentiallyleadingtomoreefficient
and easily customizable LLMs. This approach not only streamlines the optimization
process but also opens avenues for more innovative and adaptable efficiency solutions
in the realm of LLMs.
10.6 Edge computing with LLMs
Deploying Large Language Models (LLMs) in edge computing environments presents
unique challenges due to the inherent limitations of edge devices. These devices
often face constraints in terms of battery life, computational power, and memory
resources[293,294].Additionally,issuessuchasdataprivacyandnetworklatencyfurthercomplicatetheir use[295].Toaddressthese challenges,thereis aneedtodevelop
LLM techniques that are not only resource-efficient but also mindful of privacy concerns. Key to this development is the ability to facilitate effective on-device training
and operational capabilities of LLMs, making them viable for a range of practical
applications in edge computing scenarios.
43

<!-- Page 44 -->

10.7 Theoretical insights into scaling laws
A crucial yet underexplored area in the realm of Large Language Models is the theoretical understanding of their scaling laws and generalization capabilities. A deeper
insight into how LLMs’ performance scales with their size and complexity is essential.Suchunderstandingis pivotalindevelopingmethodsthatarenotjustfocusedon
modelcompressionbutaretailoredtoenhancetheoverallresourceefficiencyofLLMs.
Gaining this knowledge is fundamental for researchersto more effectively explore and
innovate within the design space of LLMs, ultimately leading to solutions that are
both powerful and resource-efficient. This theoretical foundation is key to advancing
the field and optimizing LLMs for a wider range of applications and environments.
11 Conclusion
In this survey, we have systematically explored the realm of resource-efficient Large
LanguageModels(LLMs),offeringacomprehensiveviewofthecurrentstate-of-the-art
techniques andmethodologies.We startedby providinga foundationalunderstanding
of the challenges and necessities in developing resource-efficient LLMs in Section 2.
This set the stage for a deeper investigation into various aspects of LLMs, including
architecture design, pre-training, fine-tuning, inference, and system design.
In Section 3, we highlighted innovative approaches in LLM architecture that contribute to resource efficiency, emphasizing the significance of both transformer and
non-transformer architectures. Sections 4, 5, and 6 delved into the nuances of pretraining,fine-tuning,andinferencephasesofLLMs,respectively,showcasinghoweach
stage presents unique opportunities and challenges for resource optimization.
Our explorationin Section 7 underscoredthe importance of holistic systemdesign
in achieving resource efficiency, where both hardware and software aspects play a
crucial role. In Section 8, we examined the practical applications and evaluations of
these techniques, linking them back to the resource taxonomy established earlier in
the survey.
The survey also shed light on the current benchmarks and evaluation metrics in
Section 9, which are crucial for quantifying and comparing the efficiency of various
LLMs.InSection10,weidentifiedkeyopenchallengesandfuture directions,pointing
towardsunexploredareasandpotentialbreakthroughsthatcouldfurther advancethe
field of resource-efficientLLMs.
As we conclude, it is evident that while significant progress has been made in
developing resource-efficient LLMs, there remains a vast landscape of opportunities
for further research and innovation. The insights and discussions presented in this
survey aim to serve as a guiding framework for future work in this rapidly evolving
field,withthe ultimate goalofachievinghighly efficientLLMs thatareaccessibleand
sustainable for a wide range of applications.

### References

[1] OpenAI, R.: Gpt-4 technical report. arxiv 2303.08774. View in Article 2, 13
(2023)
44

<!-- Page 45 -->

[2] Touvron,H., Lavril,T.,Izacard,G., Martinet,X., Lachaux,M.-A., Lacroix,T.,
Rozi`ere,B.,Goyal,N.,Hambro,E.,Azhar,F.,Rodriguez,A.,Joulin,A.,Grave,
E., Lample, G.: LLaMA: Open and Efficient Foundation Language Models
(2023)
[3] Floridi, L., Chiriatti, M.: Gpt-3: Its nature, scope, limits, and consequences.

### Minds and Machines 30, 681–694 (2020)

[4] Zhang, S., Roller, S., Goyal, N., Artetxe, M., Chen, M., Chen, S., Dewan, C.,
Diab, M., Li, X., Lin, X.V., et al.: Opt: Open pre-trained transformer language
models. arXiv preprint arXiv:2205.01068(2022)
[5] Scao, T.L., Fan, A., Akiki, C., Pavlick, E., Ili´c, S., Hesslow, D., Castagn´e, R.,
Luccioni,A.S.,Yvon,F.,Gall´e,M.,etal.:Bloom:A176b-parameteropen-access
multilingual language model. arXiv preprint arXiv:2211.05100(2022)
[6] Chowdhery, A., Narang, S., Devlin, J., Bosma, M., Mishra, G., Roberts, A.,
Barham, P., Chung, H.W., Sutton, C., Gehrmann, S., et al.: Palm: Scaling languagemodeling withpathways.JournalofMachineLearningResearch24(240),
1–113 (2023)
[7] Chien, A.A., Lin, L., Nguyen, H., Rao, V., Sharma, T., Wijayawardana, R.:
Reducing the carbon impact of generative ai inference (today and in 2035). In:
Proceedings of the 2nd Workshop on Sustainable Computer Systems, pp. 1–7
(2023)
[8] Samsi, S., Zhao, D., McDonald, J., Li, B., Michaleas, A., Jones, M., Bergeron,
W., Kepner, J., Tiwari, D., Gadepally, V.: From words to watts: Benchmarking the energy costs of large language model inference. arXiv preprint
arXiv:2310.03003(2023)
[9] Sˇakota, M., Peyrard,M., West, R.: Fly-swat or cannon? cost-effective language
model choice via meta-modeling. arXiv preprint arXiv:2308.06077(2023)
[10] Kaddour, J., Harris, J., Mozes, M., Bradley, H., Raileanu, R., McHardy, R.:

### Challenges and Applications of Large Language Models (2023)

[11] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N.,
Kaiser, L ., Polosukhin, I.: Attention is all you need. Advances in neural
information processing systems 30 (2017)
[12] Kaplan, J., McCandlish, S., Henighan, T., Brown, T.B., Chess, B., Child, R.,
Gray, S., Radford, A., Wu, J., Amodei, D.: Scaling laws for neural language
models. arXiv preprint arXiv:2001.08361(2020)
[13] Ying, X.: An overview of overfitting and its solutions. In: Journal of Physics:
Conference Series, vol. 1168, p. 022022 (2019). IOP Publishing
45

<!-- Page 46 -->

[14] Tirumala, K., Markosyan, A., Zettlemoyer, L., Aghajanyan, A.: Memorization
without overfitting: Analyzing the training dynamics of large language models.
Advances in Neural Information Processing Systems 35, 38274–38290(2022)
[15] Rajbhandari, S., Rasley, J., Ruwase, O., He, Y.: Zero: Memory optimizations
toward training trillion parameter models. In: SC20: International Conference
for High Performance Computing, Networking, Storage and Analysis, pp. 1–16

## (2020). Ieee

[16] Shoeybi, M., Patwary, M., Puri, R., LeGresley, P., Casper, J., Catanzaro, B.:
Megatron-lm: Training multi-billion parameter language models using model
parallelism. arXiv preprint arXiv:1909.08053(2019)
[17] Aminabadi, R.Y., Rajbhandari, S., Awan, A.A., Li, C., Li, D., Zheng, E.,
Ruwase, O., Smith, S., Zhang, M., Rasley, J., et al.: Deepspeed-inference:
enabling efficient inference of transformer models at unprecedented scale. In:
SC22: International Conference for High Performance Computing, Networking,

### Storage and Analysis, pp. 1–15 (2022). IEEE

[18] Sheng, Y., Zheng, L., Yuan, B., Li, Z., Ryabinin, M., Chen, B., Liang, P., R´e,
C.,Stoica,I.,Zhang,C.:Flexgen:High-throughputgenerativeinferenceoflarge
language models with a single gpu. In: International Conference on Machine

### Learning, pp. 31094–31116(2023). PMLR

[19] Deng, L., Li, G., Han, S., Shi, L., Xie, Y.: Model compression and hardware
acceleration for neural networks: A comprehensive survey. Proceedings of the

## Ieee 108(4), 485–532(2020)

[20] Rae,J.W.,Borgeaud,S.,Cai,T.,Millican,K.,Hoffmann,J.,Song,F.,Aslanides,
J., Henderson, S., Ring, R., Young, S., et al.: Scaling language models: Methods, analysis & insights from training gopher. arXiv preprint arXiv:2112.11446
(2021)
[21] Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford,
E.,Casas,D.d.L.,Hendricks,L.A.,Welbl,J.,Clark,A.,etal.:Trainingcomputeoptimal large language models. arXiv preprint arXiv:2203.15556(2022)
[22] Anil,R.,Dai,A.M.,Firat,O.,Johnson,M.,Lepikhin,D.,Passos,A.,Shakeri,S.,
Taropa, E., Bailey, P., Chen, Z., et al.: Palm 2 technical report. arXiv preprint
arXiv:2305.10403(2023)
[23] Gunantara, N.: A review of multi-objective optimization: Methods and its
applications. Cogent Engineering 5(1), 1502242(2018)
[24] Menghani,G.:Efficientdeeplearning:Asurveyonmakingdeeplearningmodels
smaller,faster,andbetter.ACMComputingSurveys(2021)https://doi.org/10.
1145/3578938
46

<!-- Page 47 -->

[25] Liu, Y., Han, T., Ma, S., Zhang, J., Yang, Y., Tian, J., He, H., Li, A., He, M.,
Liu,Z.,etal.:Summaryofchatgpt-relatedresearchandperspectivetowardsthe
future of large language models. Meta-Radiology, 100017 (2023)
[26] Yang, J., Jin, H., Tang, R., Han, X., Feng, Q., Jiang, H., Yin, B., Hu, X.:
Harnessingthepowerofllmsinpractice:Asurveyonchatgptandbeyond.arXiv
preprint arXiv:2304.13712(2023)
[27] Zhao,W.X., Zhou,K., Li, J.,Tang, T., Wang,X., Hou,Y., Min, Y., Zhang,B.,
Zhang, J., Dong, Z., et al.: A survey of large language models. arXiv preprint
arXiv:2303.18223(2023)
[28] Zhang,C.,Zhang,C.,Zheng,S.,Qiao,Y.,Li,C.,Zhang,M.,Dam,S.K.,Thwal,
C.M., Tun, Y.L., Huy, L.L., et al.: A complete survey on generative ai (aigc):
Is chatgpt from gpt-4 to gpt-5 all you need? arXiv preprint arXiv:2303.11717
(2023)
[29] Cao, Y., Li, S., Liu, Y., Yan, Z., Dai, Y., Yu, P.S., Sun, L.: A comprehensive
survey of ai-generated content (aigc): A history of generative ai from gan to
chatgpt. arXiv preprint arXiv:2303.04226(2023)
[30] Ling,C.,Zhao,X.,Lu,J.,Deng,C.,Zheng,C.,Wang,J.,Chowdhury,T.,Li,Y.,
Cui,H.,Zhao,T.,etal.:Domainspecializationasthekeytomakelargelanguage
models disruptive: A comprehensive survey. arXiv preprint arXiv:2305.18703
2305 (2023)
[31] Mialon, G., Dess`ı, R., Lomeli, M., Nalmpantis, C., Pasunuru, R., Raileanu,
R., Rozi`ere, B., Schick, T., Dwivedi-Yu, J., Celikyilmaz, A., et al.: Augmented
language models: a survey. arXiv preprint arXiv:2302.07842(2023)
[32] Xu, C., McAuley, J.: A survey on model compression and acceleration for pretrained language models. In: Proceedings of the AAAI Conference on Artificial

### Intelligence, vol. 37, pp. 10566–10575(2023)

[33] Zhu, X., Li, J., Liu, Y., Ma, C., Wang, W.: A survey on model compression for
large language models. arXiv preprint arXiv:2308.07633(2023)
[34] Chitty-Venkata, K.T., Mittal, S., Emani, M., Vishwanath, V., Somani, A.K.: A
survey of techniques for optimizing transformer inference. Journal of Systems

### Architecture, 102990 (2023)

[35] Tay, Y., Dehghani, M., Bahri,D., Metzler, D.: Efficient transformers:A survey.
arXiv e-prints, 2009 (2020)
[36] Fournier, Q., Caron, G.M., Aloise, D.: A practical survey on faster and lighter
transformers. ACM Computing Surveys 55(14s), 1–40 (2023)
47

<!-- Page 48 -->

[37] Zhuang, B., Liu, J., Pan, Z., He, H., Weng, Y., Shen, C.: A survey on efficient
training of transformers. arXiv preprint arXiv:2302.01107(2023)
[38] Cheng, Y., Wang, D., Zhou, P., Zhang, T.: A survey of model compression and
acceleration for deep neural networks. arXiv preprint arXiv:1710.09282(2017)
[39] Long, X., Ben, Z., Liu, Y.: A survey of related research on compression and
acceleration of deep neural networks. In: Journal of Physics: Conference Series,
vol. 1213, p. 052003 (2019). IOP Publishing
[40] Capra, M., Bussolino, B., Marchisio, A., Shafique, M., Masera, G., Martina,
M.: An updated survey of efficient hardware architectures for accelerating deep
convolutional neural networks. Future Internet 12(7), 113 (2020)
[41] Dhilleswararao, P., Boppu, S., Manikandan, M.S., Cenkeramaddi, L.R.: Efficienthardwarearchitecturesforacceleratingdeepneuralnetworks:Survey.IEEE

### Access (2022)

[42] Kenton,J.D.M.-W.C.,Toutanova,L.K.:Bert:Pre-trainingofdeepbidirectional
transformersfor languageunderstanding.In: Proceedingsof naacL-HLT,vol.1,
p. 2 (2019)
[43] Raffel, C., Shazeer,N., Roberts,A., Lee,K.,Narang,S., Matena,M., Zhou,Y.,
Li,W.,Liu,P.J.:Exploringthe limitsoftransferlearningwithaunifiedtext-totext transformer. The Journal of Machine Learning Research 21(1), 5485–5551
(2020)
[44] Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P.,
Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al.: Language models
are few-shot learners. Advances in neural information processing systems 33,
1877–1901(2020)
[45] Kitaev, N., Kaiser, L., Levskaya, A.: Reformer: The efficient transformer.
In: International Conference on Learning Representations (2020). https://
openreview.net/forum?id=rkgNKkHtvB
[46] Katharopoulos, A., Vyas, A., Pappas, N., Fleuret, F.: Transformers are rnns:
Fastautoregressivetransformerswith linearattention.In:InternationalConference on Machine Learning, pp. 5156–5165(2020). PMLR
[47] Shen, Z.,Zhang,M., Zhao,H., Yi,S., Li, H.:Efficientattention: Attentionwith
linear complexities. In: Proceedings of the IEEE/CVF Winter Conference on

### Applications of Computer Vision, pp. 3531–3539(2021)

[48] Zhai, S., Talbott, W., Srivastava,N., Huang, C., Goh, H., Zhang, R., Susskind,
J.: An attention free transformer. arXiv preprint arXiv:2105.14103(2021)
48

<!-- Page 49 -->

[49] Rabe, M.N., Staats, C.: Self-attention does not need o(n2) memory. arXiv
preprint arXiv:2112.05682(2022)
[50] Jang,H.,Kim,J.,Jo,J.-E.,Lee,J.,Kim,J.:Mnnfast:Afastandscalablesystem
architectureformemory-augmentedneuralnetworks.In:Proceedingsofthe46th
International Symposium on Computer Architecture, pp. 250–263(2019)
[51] Zandieh, A., Han, I., Daliri, M., Karbasi, A.: Kdeformer: Accelerating transformers via kernel density estimation. arXiv preprint arXiv:2302.02451(2023)
[52] Ma,X.,Zhou,C.,Kong,X.,He,J.,Gui,L.,Neubig,G.,May,J.,Zettlemoyer,L.:
Mega:Movingaverageequippedgatedattention.In:TheEleventhInternational
ConferenceonLearningRepresentations(2023).https://openreview.net/forum?
id=qNLe3iq2El
[53] Wang, Y., Xiao, Z.: Loma: Lossless compressed memory attention. arXiv
preprint arXiv:2401.09486(2024)
[54] He, Z., Feng, G., Luo, S., Yang, K., He, D., Xu, J., Zhang, Z., Yang, H.,
Wang,L.: Two stones hit one bird:Bilevelpositionalencoding for better length
extrapolation. arXiv preprint arXiv:2401.16421(2024)
[55] Arora,S., Eyuboglu,S., Zhang,M., Timalsina,A., Alberti, S.,Zinsley, D., Zou,
J.,Rudra,A.,R´e,C.:Simplelinearattentionlanguagemodelsbalancetherecallthroughput tradeoff (2024). https://arxiv.org/abs/2402.18668
[56] Huang, S., Song, Y., Zhou, J., Lin, Z.: Cluster-wise Graph Transformer
withDual-granularityKernelizedAttention(2024).https://arxiv.org/abs/2410.
06746
[57] Zhang,J.,wei,J.,Huang,H.,Zhang,P.,Zhu,J.,Chen,J.:SageAttention:Accurate 8-Bit Attention for Plug-and-play Inference Acceleration (2024). https://
arxiv.org/abs/2410.02367
[58] Aguilera-Martos, I., Herrera-Poyatos,A., Luengo, J., Herrera, F.: Local Attention Mechanism: Boosting the Transformer Architecture for Long-Sequence
Time Series Forecasting (2024). https://arxiv.org/abs/2410.03805
[59] Mahmood, K., Huang, S.: Enhanced Computationally Efficient Long LoRA
InspiredPerceiverArchitecturesforAuto-RegressiveLanguageModeling(2024).
https://arxiv.org/abs/2412.06106
[60] Yang,E.:Signformerisallyouneed:TowardsEdgeAIforSignLanguage(2024).
https://arxiv.org/abs/2411.12901
[61] Peng,B.,Alcaide,E.,Anthony,Q.,Albalak,A.,Arcadinho,S.,Cao,H., Cheng,
X., Chung, M., Grella, M., GV, K.K., et al.: Rwkv: Reinventing rnns for the
49

<!-- Page 50 -->

transformer era. arXiv preprint arXiv:2305.13048(2023)
[62] Wang, X., Xiong, Y., Wei, Y., Wang, M., Li, L.: Lightseq: A high performance
inference library for transformers. NAACL-HLT 2021, 113 (2021)
[63] NVIDIA: FasterTransformer:AFasterTransformerFramework.https://github.
com/NVIDIA/FasterTransformer (2021)
[64] Lefaudeux, B., Massa, F., Liskovich, D., Xiong, W., Caggiano, V., Naren, S.,
Xu, M., Hu, J., Tintore, M., Zhang, S., Labatut, P., Haziza, D.: xFormers:
A modular and hackable Transformer modelling library. https://github.com/
facebookresearch/xformers(2022)
[65] Dao,T.,Fu,D.,Ermon,S.,Rudra,A.,R´e,C.:Flashattention:Fastandmemoryefficient exact attention with io-awareness. Advances in Neural Information

### Processing Systems 35, 16344–16359(2022)

[66] Dao, T.: Flashattention-2: Faster attention with better parallelism and work
partitioning. arXiv preprint arXiv:2307.08691(2023)
[67] Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu, C.H., Gonzalez,
J.E., Zhang, H., Stoica, I.: Efficient memory management for large language
model serving with pagedattention. In: Proceedings of the ACM SIGOPS 29th

### Symposium on Operating Systems Principles (2023)

[68] Liu,Z.,Zhao,C.,Iandola,F.,Lai,C.,Tian,Y.,Fedorov,I.,Xiong,Y.,Chang,E.,
Shi,Y.,Krishnamoorthi,R.,etal.:Mobilellm:Optimizingsub-billionparameter
languagemodelsforon-deviceusecases.arXivpreprintarXiv:2402.14905(2024)
[69] Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., Dean,
J.: Outrageously large neural networks: The sparsely-gated mixture-of-experts
layer. In: International Conference on Learning Representations (2016)
[70] Lepikhin, D., Lee, H., Xu, Y., Chen, D., Firat, O., Huang, Y., Krikun, M.,
Shazeer, N., Chen, Z.: Gshard: Scaling giant models with conditional computation and automatic sharding. In: International Conference on Learning

### Representations (2020)

[71] Fedus,W.,Zoph,B.,Shazeer,N.:Switchtransformers:Scalingtotrillionparameter models withsimple andefficientsparsity.The JournalofMachineLearning

### Research 23(1), 5232–5270(2022)

[72] Du, N., Huang, Y., Dai, A.M., Tong, S., Lepikhin, D., Xu, Y., Krikun, M.,
Zhou,Y.,Yu, A.W.,Firat,O.,et al.: Glam:Efficientscalingoflanguagemodels
with mixture-of-experts.In: InternationalConference onMachineLearning,pp.

## 5547–5569(2022). Pmlr

50

<!-- Page 51 -->

[73] Zhou, Y., Lei, T., Liu, H., Du, N., Huang, Y., Zhao, V., Dai, A.M., Le, Q.V.,
Laudon, J., et al.: Mixture-of-experts with expert choice routing. Advances in

### Neural Information Processing Systems 35, 7103–7114(2022)

[74] Artetxe, M., Bhosale, S., Goyal, N., Mihaylov, T., Ott, M., Shleifer, S., Lin,
X.V.,Du,J.,Iyer,S.,Pasunuru,R.,etal.:Efficientlargescalelanguagemodeling
with mixtures of experts. In: Proceedings of the 2022 Conference on Empirical
Methods in Natural Language Processing, pp. 11699–11732(2022)
[75] Clark, A., De Las Casas, D., Guy, A., Mensch, A., Paganini, M., Hoffmann, J.,
Damoc, B., Hechtman, B., Cai, T., Borgeaud,S., et al.: Unified scaling laws for
routedlanguagemodels.In:InternationalConferenceonMachine Learning,pp.

## 4057–4086(2022). Pmlr

[76] Malach, E.: Auto-regressive next-token predictors are universal learners. arXiv
preprint arXiv:2309.06979(2023)
[77] Poli, M., Massaroli, S., Nguyen, E., Fu, D.Y., Dao, T., Baccus, S., Bengio,
Y., Ermon, S., R´e, C.: Hyena hierarchy: Towards larger convolutional language
models. arXiv preprint arXiv:2302.10866(2023)
[78] Fu,D.Y.,Arora,S.,Grogan,J.,Johnson,I.,Eyuboglu,S.,Thomas,A.W.,Spector, B.F., Poli, M., Rudra, A., Re, C.: Monarch mixer: A simple sub-quadratic
gemm-basedarchitecture.In: Thirty-seventhConference on NeuralInformation

### Processing Systems (2023)

[79] Gu, A., Dao, T.: Mamba: Linear-time sequence modeling with selective state
spaces. arXiv preprint arXiv:2312.00752(2023)
[80] Sun, Y., Dong, L., Zhu, Y., Huang, S., Wang, W., Ma, S., Zhang, Q., Wang,
J., Wei, F.: You only cache once: Decoder-decoder architectures for language
models. arXiv preprint arXiv:2405.05254(2024)
[81] Zhu,R.-J.,Zhang,Y.,Sifferman,E.,Sheaves,T.,Wang,Y.,Richmond,D.,Zhou,
P., Eshraghian, J.K.: Scalable matmul-free language modeling. arXiv preprint
arXiv:2406.02528(2024)
[82] Choe,W.,Ji,Y.,Lin,F.:RWKV-edge:DeeplyCompressedRWKVforResource-
Constrained Devices (2024). https://arxiv.org/abs/2412.10856
[83] Baines,M.,Bhosale,S.,Caggiano,V.,Goyal,N.,Goyal,S.,Ott,M.,Lefaudeux,
B.,Liptchinsky,V.,Rabbat,M.,Sheiffer,S., etal.:Fairscale:Ageneralpurpose
modular pytorch library for high performance and large scale training (2021)
[84] Shazeer, N., Cheng, Y., Parmar, N., Tran, D., Vaswani, A., Koanantakool, P.,
Hawkins, P., Lee, H., Hong, M., Young, C., et al.: Mesh-tensorflow:Deep learning for supercomputers. Advances in neural information processing systems 31
51

<!-- Page 52 -->

(2018)
[85] Huang,Y.,Cheng,Y.,Bapna,A.,Firat,O.,Chen,D.,Chen,M.,Lee,H.,Ngiam,
J., Le, Q.V., Wu, Y., et al.: Gpipe: Efficient training of giant neural networks
using pipeline parallelism. Advances in neural information processing systems
32 (2019)
[86] Narayanan, D., Harlap, A., Phanishayee, A., Seshadri, V., Devanur, N.R.,
Ganger, G.R., Gibbons, P.B., Zaharia, M.: Pipedream: Generalized pipeline
parallelism for dnn training. In: Proceedings of the 27th ACM Symposium on

### Operating Systems Principles, pp. 1–15 (2019)

[87] Kim, T., Kim, H., Yu, G.-I., Chun, B.-G.: Bpipe: memory-balanced pipeline
parallelism for training large language models. In: International Conference on

### Machine Learning, pp. 16639–16653(2023). PMLR

[88] Zheng,L.,Li,Z.,Zhang,H.,Zhuang,Y.,Chen,Z.,Huang,Y.,Wang,Y.,Xu,Y.,
Zhuo,D.,Xing,E.P.,etal.:Alpa:Automatinginter-and Intra-Operator paral-
{ }
lelismfordistributeddeeplearning.In:16thUSENIXSymposiumonOperating
Systems Design and Implementation (OSDI 22), pp. 559–578 (2022)
[89] Jiang, Z., Lin, H., Zhong,Y., Huang, Q., Chen, Y., Zhang,Z., Peng, Y., Li, X.,
Xie, C., Nong, S., et al.: MegaScale :Scaling large language model training to
{ }
morethan10,000 GPUs .In:21stUSENIXSymposiumonNetworkedSystems
{ }

### Design and Implementation (NSDI 24), pp. 745–760(2024)

[90] Yang, H., Zhou, J., Fu, Y., Wang, X., Roane, R., Guan, H., Liu, T.: Protrain: Efficient llm training via memory-aware techniques. arXiv preprint
arXiv:2406.08334(2024)
[91] Micikevicius, P.,Narang,S., Alben, J., Diamos,G., Elsen, E.,Garcia, D., Ginsburg, B., Houston, M., Kuchaiev, O., Venkatesh, G., et al.: Mixed precision
training. The International Conference on Learning Representation (2018)
[92] Johnson, T.B., Guestrin, C.: Training deep models faster with robust, approximateimportancesampling.AdvancesinNeuralInformationProcessingSystems
31 (2018)
[93] Katharopoulos,A.,Fleuret,F.:Notallsamplesarecreatedequal:Deeplearning
with importance sampling. In: International Conference on Machine Learning,
pp. 2525–2534(2018). PMLR
[94] Paul, M., Ganguli, S., Dziugaite, G.K.: Deep learning on a data diet: Finding important examples early in training. Advances in Neural Information

### Processing Systems 34, 20596–20607(2021)

[95] Sorscher, B., Geirhos, R., Shekhar, S., Ganguli, S., Morcos, A.: Beyond neural
52

<!-- Page 53 -->

scaling laws: beating power law scaling via data pruning. Advances in Neural

### Information Processing Systems 35, 19523–19536(2022)

[96] Chen, D., Huang, Y., Ma, Z., Chen, H., Pan, X., Ge, C., Gao, D., Xie, Y., Liu,
Z.,Gao,J.,Li,Y.,Ding,B.,Zhou,J.:Data-Juicer:AOne-StopDataProcessing

### System for Large Language Models (2023)

[97] Renduchintala, H.S.V.N.S.K., Killamsetty, K., Bhatia, S., Aggarwal, M.,
Ramakrishnan,G.,Iyer,R.,Krishnamurthy,B.:INGENIOUS:Usinginformative
datasubsetsforefficientpre-trainingoflanguagemodels.In:Bouamor,H.,Pino,
J., Bali, K. (eds.) Findings of the Association for Computational Linguistics:
EMNLP 2023, pp. 6690–6705. Association for Computational Linguistics, Singapore (2023). https://doi.org/10.18653/v1/2023.findings-emnlp.445 . https://
aclanthology.org/2023.findings-emnlp.445
[98] Bukharin,A., Liu, T., Wang,S., Zuo,S., Gao,W., Yan, W., Zhao,T.: Machine
learning force fields with data cost aware training. In: Proceedings of the 40th
InternationalConferenceonMachineLearning.ICML’23.JMLR.org,???(2023)
[99] Pan, R., Liu, X., Diao, S., Pi, R., Zhang, J., Han, C., Zhang, T.: Lisa: Layerwiseimportancesamplingformemory-efficientlargelanguagemodelfine-tuning.
arXiv preprint arXiv:2403.17919(2024)
[100] Hao,X.,Zhu,Y.,Appalaraju,S.,Zhang,A.,Zhang,W.,Li,B.,Li,M.:Mixgen:A
new multi-modaldataaugmentation.In:Proceedingsofthe IEEE/CVFWinter
Conference on Applications of Computer Vision (WACV) Workshops, pp. 379–
389 (2023)
[101] Hou, L., Cao, Q., Yuan, Y., Zhao, S., Ma, C., Pan, S., Wan, P., Wang, Z.,
Shen, H., Cheng, X.: Augmentation-awareself-supervisionfor data-efficientgan
training. arXiv preprint arXiv:2205.15677(2022)
[102] Lu, J., Huang, W., Zheng, N., Zeng, X., Yeung, Y., Chen, X.: Improving
end-to-end speech processing by efficient text data utilization with latent
synthesis. In: Bouamor, H., Pino, J., Bali, K. (eds.) Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 4916–4928. Association
for Computational Linguistics, Singapore (2023). https://doi.org/10.18653/v1/
2023.findings-emnlp.327. https://aclanthology.org/2023.findings-emnlp.327
[103] Wei, W., Ren, X., Tang, J., Wang, Q., Su, L., Cheng, S., Wang, J., Yin, D.,
Huang,C.:Llmrec:Largelanguagemodels with graphaugmentationfor recommendation. In: Proceedings of the 17th ACM International Conference on Web

### Search and Data Mining, pp. 806–815(2024)

[104] Ye,J.,Xu,N.,Wang,Y.,Zhou,J.,Zhang,Q.,Gui,T.,Huang,X.:Llm-da:Data
augmentation via large language models for few-shot named entity recognition.
arXiv preprint arXiv:2402.14568(2024)
53

<!-- Page 54 -->

[105] Fan,Z.,He,S.:Efficientdatalearningforopeninformationextractionwithpretrained language models. In: Bouamor, H., Pino, J., Bali, K. (eds.) Findings of
the Associationfor ComputationalLinguistics:EMNLP2023,pp.13056–13063.
Association for Computational Linguistics, Singapore (2023). https://doi.org/
10.18653/v1/2023.findings-emnlp.869 . https://aclanthology.org/2023.findingsemnlp.869
[106] Song,K.,Tan,X.,Qin,T.,Lu,J.,Liu,T.-Y.:Mass:Maskedsequencetosequence
pre-training for language generation. In: International Conference on Machine

### Learning, pp. 5926–5936(2019). PMLR

[107] He, K., Chen, X., Xie, S., Li, Y., Dolla´r, P., Girshick, R.: Masked autoencoders
are scalable vision learners. In: Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition, pp. 16000–16009(2022)
[108] Li, Y., Fan, H., Hu, R., Feichtenhofer, C., He, K.: Scaling language-image
pre-training via masking. In: Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition, pp. 23390–23400(2023)
[109] Jiang, H., He, P., Chen, W., Liu, X., Gao, J., Zhao, T.: SMART: Robust and
efficient fine-tuning for pre-trained natural language models through principled
regularized optimization. In: Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, pp. 2177–2190(2020)
[110] Zaken, E.B., Goldberg, Y., Ravfogel, S.: Bitfit: Simple parameter-efficient finetuning for transformer-based masked language-models. In: Proceedings of the
60th Annual Meeting of the Association for ComputationalLinguistics, pp. 1–9
(2022)
[111] Xu, R., Luo, F., Zhang, Z., Tan, C., Chang, B., Huang, S., Huang, F.: Raise a
childinlargelanguagemodel:Towardseffectiveandgeneralizablefine-tuning.In:
Proceedingsofthe 2021ConferenceonEmpiricalMethods inNaturalLanguage

### Processing, pp. 9514–9528(2021)

[112] Zhang, H., Li, G., Li, J., Zhang, Z., Zhu, Y., Jin, Z.: Fine-tuning pre-trained
language models effectively by optimizing subnetworks adaptively. Advances in

### Neural Information Processing Systems 35, 21442–21454(2022)

[113] Yu, C., Jeoung, S., Kasi, A., Yu, P., Ji, H.: Unlearning bias in language models
by partitioning gradients. In: Findings of the Association for Computational

### Linguistics: ACL 2023, pp. 6032–6048(2023)

[114] Abdurrahman, M.S., Elezabi, H., Xu, B.C.: Typhoon: Towards an effective
task-specific masking strategy for pre-trained language models. arXiv preprint
arXiv:2303.15619(2023)
54

<!-- Page 55 -->

[115] Hao,J.,Sun,W.,Xin,X., Meng,Q.,Chen,Z.,Ren,P.,Ren,Z.:Meft: Memoryefficient fine-tuning through sparse adapter. arXiv preprint arXiv:2406.04984
(2024)
[116] Valipour, M., Rezagholizadeh, M., Kobyzev, I., Ghodsi, A.: Dylora: Parameter efficient tuning of pre-trained models using dynamic search-free low-rank
adaptation. arXiv preprint arXiv:2210.07558(2022)
[117] Houlsby, N., Giurgiu, A., Jastrzebski,S., Morrone,B., De Laroussilhe,Q., Gesmundo, A., Attariyan, M., Gelly, S.: Parameter-efficient transfer learning for
nlp. In: International Conference on Machine Learning, pp. 2790–2799 (2019).

## Pmlr

[118] Hu, Z., Lan, Y., Wang, L., Xu, W., Lim, E.-P., Lee, R.K.-W., Bing, L., Poria,
S.: Llm-adapters: An adapter family for parameter-efficient fine-tuning of large
language models. arXiv preprint arXiv:2304.01933(2023)
[119] Zhang, R., Zheng, Y., Mao, X., Huang, M.: Unsupervised domain adaptation
with adapter. arXiv preprint arXiv:2111.00667(2021)
[120] Malik,B.,Kashyap,A.R.,Kan,M.-Y.,Poria,S.:Udapter-efficientdomainadaptation using adapters. In: Proceedings of the 17th Conference of the European
ChapteroftheAssociationforComputationalLinguistics,pp.2241–2255(2023)
[121] Pfeiffer, J., Kamath, A., Ru¨ckl´e, A., Cho, K., Gurevych, I.: AdapterFusion:

### Non-destructive task composition for transfer learning

[122] Chronopoulou, A., Peters, M.E., Fraser, A., Dodge, J.: Adaptersoup: Weight
averagingto improvegeneralizationofpretrainedlanguagemodels. In:Findings
of the Association for Computational Linguistics: EACL 2023, pp. 2009–2018
(2023)
[123] Hendrycks, D., Gimpel, K.: Gaussian error linear units (gelus). arXiv preprint
arXiv:1606.08415(2016)
[124] Bapna, A., Firat, O.: Simple, scalable adaptation for neural machine translation. In: Proceedings of the 2019 Conference on Empirical Methods in Natural
Language Processing and the 9th International Joint Conference on Natural

### Language Processing (EMNLP-IJCNLP), pp. 1538–1548(2019)

[125] Hu, E.J., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., Chen, W.,
et al.: Lora: Low-rank adaptation of large language models. In: International

### Conference on Learning Representations (2021)

[126] Aghajanyan,A.,Gupta,S.,Zettlemoyer,L.:Intrinsicdimensionalityexplainsthe
effectiveness of language model fine-tuning. In: Proceedings of the 59th Annual
55

<!-- Page 56 -->

Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long

### Papers), pp. 7319–7328(2021)

[127] Sun,X.,Ji,Y.,Ma,B.,Li,X.:Acomparativestudybetweenfull-parameterand
lora-basedfine-tuning onchinese instructiondata forinstructionfollowinglarge
language model. arXiv preprint arXiv:2304.08109(2023)
[128] Razuvayevskaya, O., Wu, B., Leite, J.A., Heppell, F., Srba, I., Scarton, C.,
Bontcheva, K., Song, X.: Comparison between parameter-efficient techniques
and full fine-tuning: A case study on multilingual news article classification.
arXiv preprint arXiv:2308.07282(2023)
[129] Ding, N., Qin, Y., Yang, G., Wei, F., Yang, Z., Su, Y., Hu, S., Chen, Y., Chan,
C.-M.,Chen,W.,etal.:Parameter-efficientfine-tuningoflarge-scalepre-trained
language models. Nature Machine Intelligence 5(3), 220–235(2023)
[130] Chen, T., Xu, B., Zhang, C., Guestrin, C.: Training deep nets with sublinear
memory cost. arXiv preprint arXiv:1604.06174(2016)
[131] Lv,K.,Yang,Y.,Liu,T.,Gao,Q.,Guo,Q.,Qiu,X.:FullParameterFine-tuning
for Large Language Models with Limited Resources (2023)
[132] Malladi, S., Gao, T., Nichani, E., Damian, A., Lee, J.D., Chen, D., Arora, S.:

### Fine-Tuning Language Models with Just Forward Passes (2023)

[133] Liu, Y., Zhang, Y., Li, Q., Liu, T., Feng, S., Wang, D., Zhang, Y., Schu¨tze,
H.: Hift: A hierarchical full parameter fine-tuning strategy. arXiv preprint
arXiv:2401.15207(2024)
[134] Wu, C., Lin, W., Zhang, X., Zhang, Y., Wang, Y., Xie, W.: PMC-LLaMA:
Towards Building Open-source Language Models for Medicine (2023)
[135] Kumar,A.,Raghunathan,A.,Jones,R.,Ma,T.,Liang,P.:Fine-tuning candistort pretrained features and underperform out-of-distribution. In: International

### Conference on Learning Representations (2022)

[136] LeCun, Y., Denker, J., Solla, S.: Optimal brain damage. Advances in neural
information processing systems 2 (1989)
[137] Han, S., Mao, H., Dally, W.J.: Deep compression: Compressing deep neural
networkswithpruning,trainedquantizationandhuffmancoding.arXivpreprint
arXiv:1510.00149(2015)
[138] Frantar, E., Alistarh, D.: Massive language models can be accurately pruned in
one-shot. arXiv preprint arXiv:2301.00774(2023)
[139] Sun,M.,Liu,Z.,Bair,A.,Kolter,J.Z.:Asimple andeffectivepruningapproach
56

<!-- Page 57 -->

for large language models. arXiv preprint arXiv:2306.11695(2023)
[140] Tuli,S.,Jha,N.K.:Acceltran:Asparsity-awareacceleratorfordynamicinference
withtransformers.IEEETransactionsonComputer-AidedDesignofIntegrated

### Circuits and Systems (2023)

[141] Bai,G.,Li,Y.,Ling,C.,Kim,K.,Zhao,L.:Gradient-freeadaptiveglobalpruning
for pre-trained language models. arXiv preprint arXiv:2402.17946(2024)
[142] Ma, X., Fang, G., Wang, X.: Llm-pruner: On the structural pruning of large
language models. arXiv preprint arXiv:2305.11627(2023)
[143] Li, Y., Yu, Y., Zhang, Q., Liang, C., He, P., Chen, W., Zhao, T.: Losparse:
Structured compressionof large language models based on low-rank and sparse
approximation. arXiv preprint arXiv:2306.11222(2023)
[144] Tao, C., Hou, L., Bai, H., Wei, J., Jiang, X., Liu, Q., Luo, P., Wong, N.: Structured pruning for efficient generative pre-trained language models. In: Findings
of the Association for Computational Linguistics: ACL 2023, pp. 10880–10895
(2023)
[145] Kurtic,E.,Frantar,E.,Alistarh,D.:Ziplm:Hardware-awarestructuredpruning
of language models. arXiv preprint arXiv:2302.04089(2023)
[146] Liu,Z.,Wang,J.,Dao,T.,Zhou,T.,Yuan,B.,Song,Z.,Shrivastava,A.,Zhang,
C., Tian, Y., Re, C., et al.: Deja vu: Contextual sparsity for efficient llms at
inference time. In: International Conference on Machine Learning, pp. 22137–

## 22176 (2023). Pmlr

[147] Lee, J.H., Kim, J., Kwon, S.J., Lee, D.: Flexround: Learnable rounding based
onelement-wise divisionfor post-trainingquantization.Proceedingsofthe 40th

### International Conference on Machine Learning (2023)

[148] Lin, J., Tang, J., Tang, H., Yang, S., Dang, X., Han, S.: Awq: Activationaware weight quantization for llm compressionand acceleration. arXiv preprint
arXiv:2306.00978(2023)
[149] Dettmers, T., Svirschevski, R., Egiazarian, V., Kuznedelev, D., Frantar,
E., Ashkboos, S., Borzunov, A., Hoefler, T., Alistarh, D.: Spqr: A sparsequantizedrepresentationfornear-losslessllmweightcompression.arXivpreprint
arXiv:2306.03078(2023)
[150] Wei, X., Zhang, Y., Li, Y., Zhang, X., Gong, R., Guo, J., Liu, X.: Outlier suppression+: Accurate quantization of large language models by equivalent and
optimal shifting and scaling. arXiv preprint arXiv:2304.09145(2023)
[151] Kim, S., Hooper, C., Gholami, A., Dong, Z., Li, X., Shen, S., Mahoney,
57

<!-- Page 58 -->

M.W., Keutzer, K.: Squeezellm: Dense-and-sparse quantization. arXiv preprint
arXiv:2306.07629(2023)
[152] Lee, C., Jin, J., Kim, T., Kim, H., Park, E.: Owq: Lessons learned from activation outliers for weightquantization in large language models. arXiv preprint
arXiv:2306.02272(2023)
[153] Guo, C., Tang, J., Hu, W., Leng, J., Zhang, C., Yang, F., Liu, Y., Guo, M.,
Zhu,Y.:Olive:Acceleratinglargelanguagemodelsviahardware-friendlyoutliervictim pair quantization. In: Proceedings of the 50th Annual International

### Symposium on Computer Architecture, pp. 1–15 (2023)

[154] Liu, Z., Oguz, B., Zhao, C., Chang, E., Stock, P., Mehdad, Y., Shi, Y., Krishnamoorthi,R., Chandra,V.: Llm-qat:Data-freequantizationawaretrainingfor
large language models. arXiv preprint arXiv:2305.17888(2023)
[155] Frantar, E., Ashkboos, S., Hoefler, T., Alistarh, D.: Gptq: Accurate posttraining quantizationforgenerativepre-trainedtransformers.The International

### Conference on Learning Representations (2023)

[156] Lin, H., Xu, H., Wu, Y., Cui, J., Zhang, Y., Mou, L., Song, L., Sun, Z., Wei,
Y.: Rotation and permutation for advanced outlier management and efficient
quantization of llms. arXiv preprint arXiv:2406.01721(2024)
[157] Shao, W., Chen, M., Zhang, Z., Xu, P., Zhao, L., Li, Z., Zhang, K., Gao, P.,
Qiao, Y., Luo, P.: Omniquant: Omnidirectionally calibrated quantization for
large language models. arXiv preprint arXiv:2308.13137(2023)
[158] Yang, G., Lo, D., Mullins, R., Zhao, Y.: Dynamic stashing quantization for
efficient transformer training. Findings of the Association for Computational

### Linguistics: EMNLP 2023 (2023)

[159] Yang, Z., Choudhary, S., Kunzmann, S., Zhang, Z.: Quantization-aware and
tensor-compressedtraining of transformersfor natural languageunderstanding.

### Interspeech (2023)

[160] Dettmers, T., Pagnoni, A., Holtzman, A., Zettlemoyer, L.: Qlora: Efficient
finetuning of quantized llms. arXiv preprint arXiv:2305.14314(2023)
[161] Wortsman,M.,Dettmers,T.,Zettlemoyer,L.,Morcos,A.,Farhadi,A.,Schmidt,
L.: Stable and low-precision training for large-scale vision-language models.
arXiv preprint arXiv:2304.13013(2023)
[162] Gong, Z., Liu, J., Wang, Q., Yang, Y., Wang, J., Wu, W., Xian, Y., Zhao,
D., Yan, R.: Prequant: A task-agnostic quantization approach for pre-trained
language models. Findings of the Association for Computational Linguistics:

## Acl 2023 (2023)

58

<!-- Page 59 -->

[163] Liu, X., Zheng, L., Wang, D., Cen, Y., Chen, W., Han, X., Chen, J., Liu, Z.,
Tang, J., Gonzalez, J., et al.: Gact: Activation compressed training for generic
network architectures. In: International Conference on Machine Learning, pp.

## 14139–14152(2022). Pmlr

[164] Evans,R.D., Aamodt, T.: Ac-gc:Lossyactivationcompressionwith guaranteed
convergence. Advances in Neural Information Processing Systems 34, 27434–
27448 (2021)
[165] Yu, C., Chen, T., Gan, Z.: Boost transformer-based language models with
gpu-friendly sparsity and quantization. In: Findings of the Association for

### Computational Linguistics: ACL 2023, pp. 218–235(2023)

[166] Muhamed, A., Keivanloo, I., Perera, S., Mracek, J., Xu, Y., Cui, Q.,
Rajagopalan,S., Zeng, B., Chilimbi, T.: Ctr-bert: Cost-effective knowledge distillation for billion-parameter teacher models. In: NeurIPS Efficient Natural

### Language and Speech Processing Workshop (2021)

[167] Vucetic, D., Tayaranian, M., Ziaeefard, M., Clark, J.J., Meyer, B.H., Gross,
W.J.: Efficient fine-tuning of compressed language models with learners. arXiv
preprint arXiv:2208.02070(2022)
[168] Marjieh, R., Sucholutsky, I., Rijn, P., Jacoby, N., Griffiths, T.L.: What language reveals about perception: Distilling psychophysical knowledge from large
language models. arXiv preprint arXiv:2302.01308(2023)
[169] Azerbayev, Z., Ni, A., Schoelkopf, H., Radev, D.: Explicit knowledge transfer
for weakly-supervisedcode generation.arXiv preprintarXiv:2211.16740(2022)
[170] Gu, Y., Dong, L., Wei, F., Huang, M.: Knowledge distillation of large language
models. arXiv preprint arXiv:2306.08543(2023)
[171] Zhang, R., Shen, J., Liu, T., Liu, J., Bendersky, M., Najork,M., Zhang, C.: Do
not blindly imitate the teacher: Using perturbed loss for knowledge distillation.
arXiv preprint arXiv:2305.05010(2023)
[172] Shridhar, K., Stolfo, A., Sachan, M.: Distilling multi-step reasoning capabilities
oflargelanguagemodelsintosmallermodelsviasemanticdecompositions.arXiv
preprint arXiv:2212.00193(2022)
[173] Hsieh, C.-Y., Li, C.-L., Yeh, C.-K., Nakhost, H., Fujii, Y., Ratner, A., Krishna,
R., Lee, C.-Y., Pfister, T.: Distilling step-by-step! outperforming larger language models with less training data and smaller model sizes. arXiv preprint
arXiv:2305.02301(2023)
[174] Wu, M., Waheed, A., Zhang, C., Abdul-Mageed, M., Aji, A.F.: Lamini-lm: A
diverse herd of distilled models from large-scale instructions. arXiv preprint
59

<!-- Page 60 -->

arXiv:2304.14402(2023)
[175] Peng,B.,Li,C.,He,P.,Galley,M.,Gao,J.:Instructiontuningwithgpt-4.arXiv
preprint arXiv:2304.03277(2023)
[176] Chiang,W.-L.,Li,Z.,Lin,Z.,Sheng,Y.,Wu,Z.,Zhang,H.,Zheng,L.,Zhuang,
S.,Zhuang,Y.,Gonzalez,J.E.,etal.:Vicuna:Anopen-sourcechatbotimpressing
gpt-4 with 90%* chatgpt quality. See https://vicuna. lmsys. org (accessed 14

### April 2023) (2023)

[177] Taori, R., Gulrajani, I., Zhang, T., Dubois, Y., Li, X., Guestrin, C., Liang, P.,
Hashimoto,T.B.:Stanfordalpaca:Aninstruction-followingllamamodel(2023)
[178] Ling, C., Zhang, X., Zhao, X., Liu, Y., Cheng, W., Oishi, M., Osaki, T.,
Matsuda,K.,Chen,H.,Zhao,L.:Open-endedcommonsensereasoningwithunrestricted answer candidates. In: Findings of the Association for Computational

### Linguistics: EMNLP 2023,pp. 8035–8047(2023)

[179] Wang, H., Li, R., Jiang, H., Wang, Z., Tang, X., Bi, B., Cheng, M., Yin, B.,
Wang, Y., Zhao, T., et al.: Lighttoken: A task and model-agnostic lightweight
tokenembeddingframeworkforpre-trainedlanguagemodels.In:Proceedingsof
the 29thACMSIGKDDConferenceonKnowledgeDiscoveryandData Mining,
pp. 2302–2313(2023)
[180] Zhang, M., Shen, C., Yang, Z., Ou, L., Yu, X., Zhuang, B., et al.: Pruning
meetslow-rankparameter-efficientfine-tuning.arXivpreprintarXiv:2305.18403
(2023)
[181] Wu, X., Yao, Z., He, Y.: Zeroquant-fp: A leap forward in llms post-training
w4a8quantizationusingfloating-pointformats.arXivpreprintarXiv:2307.09782
(2023)
[182] Chen, P., Yu, H.-F., Dhillon, I., Hsieh, C.-J.: Drone: Data-awarelow-rankcompressionforlargenlpmodels.Advancesinneuralinformationprocessingsystems
34, 29321–29334(2021)
[183] Tahaei, M.S., Charlaix, E., Nia, V.P., Ghodsi, A., Rezagholizadeh, M.: Kroneckerbert: Learning kronecker decomposition for pre-trained language models
via knowledge distillation. arXiv preprint arXiv:2109.06243(2021)
[184] Edalati, A., Tahaei, M., Rashid, A., Nia, V.P., Clark, J.J., Rezagholizadeh,M.:
Kronecker decomposition for gpt compression.arXiv preprint arXiv:2110.08152
(2021)
[185] Reid, M., Marrese-Taylor, E., Matsuo, Y.: Subformer: Exploring weight
sharing for parameter efficiency in generative transformers. arXiv preprint
arXiv:2101.00234(2021)
60

<!-- Page 61 -->

[186] Xu,M.,Xu,Y.L.,Mandic,D.P.:Tensorgpt:Efficientcompressionoftheembedding layer in llms based on the tensor-train decomposition. arXiv preprint
arXiv:2307.00526(2023)
[187] Gao,C.,Zhang,S.Q.:Dlora:Distributedparameter-efficientfine-tuningsolution
for large language model. arXiv preprint arXiv:2404.05182(2024)
[188] Lin, Z., Hu, X., Zhang, Y., Chen, Z., Fang, Z., Chen, X., Li, A., Vepakomma,
P.,Gao,Y.:Splitlora:Asplitparameter-efficientfine-tuningframeworkforlarge
language models. arXiv preprint arXiv:2407.00952(2024)
[189] Lin,X.,Wang,W.,Li,Y.,Yang,S.,Feng,F.,Wei,Y.,Chua,T.-S.:Data-efficient
fine-tuning for llm-based recommendation. In: Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information

### Retrieval, pp. 365–374 (2024)

[190] Li,S.,Ning,X.,Wang,L.,Liu,T.,Shi,X.,Yan,S.,Dai,G.,Yang,H.,Wang,Y.:
Evaluating Quantized Large Language Models (2024). https://arxiv.org/abs/
2402.18158
[191] Hu,X.,Cheng,Y.,Yang,D.,Yuan,Z.,Yu,J.,Xu,C.,Zhou,S.:I-LLM:Efficient
Integer-Only Inference for Fully-Quantized Low-Bit Large Language Models
(2024). https://arxiv.org/abs/2405.17849
[192] Zeng, C., Liu, S., Xie, Y., Liu, H., Wang, X., Wei, M., Yang, S., Chen, F.,
Mei, X.: ABQ-LLM: Arbitrary-Bit Quantized Inference Acceleration for Large

### Language Models (2024). https://arxiv.org/abs/2408.08554

[193] Teerapittayanon, S., McDanel, B., Kung, H.-T.: Branchynet: Fast inference via
earlyexiting fromdeepneuralnetworks.In:201623rdInternationalConference
on Pattern Recognition (ICPR), pp. 2464–2469(2016). IEEE
[194] Jawahar, G., Sagot, B., Seddah, D.: What does bert learn about the structure of language? In: ACL 2019-57th Annual Meeting of the Association for

### Computational Linguistics (2019)

[195] Rogers, A., Kovaleva, O., Rumshisky, A.: A primer in bertology: What we
knowabouthowbertworks.Transactionsofthe AssociationforComputational

### Linguistics 8, 842–866(2021)

[196] Xin, J., Tang, R., Lee, J., Yu, Y., Lin, J.: Deebert: Dynamic early exiting for
accelerating bert inference. In: Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, pp. 2246–2251(2020)
[197] Schwartz,R.,Stanovsky,G.,Swayamdipta,S.,Dodge,J.,Smith,N.A.:Theright
tool for the job: Matching model and instance complexities. In: Proceedings of
the 58th Annual Meeting of the Association for Computational Linguistics, pp.
61

<!-- Page 62 -->

6640–6651(2020)
[198] Zhou,W.,Xu,C.,Ge,T.,McAuley,J.,Xu,K.,Wei,F.:Bertlosespatience:Fast
androbustinferencewithearlyexit.AdvancesinNeuralInformationProcessing

### Systems 33, 18330–18341(2020)

[199] Zhang, Z., Zhu, W., Zhang, J., Wang, P., Jin, R., Chung, T.-S.: Pcee-bert:
Accelerating bert inference via patient and confident early exiting. In: Findings
of the Association for Computational Linguistics: NAACL 2022, pp. 327–338
(2022)
[200] Wang,J.,Chen,K.,Chen,G.,Shou,L.,McAuley,J.:Skipbert:Efficientinference
with shallow layer skipping. In: Proceedings of the 60th Annual Meeting of
the Association for Computational Linguistics (Volume 1: Long Papers), pp.
7287–7301(2022)
[201] Yom Din, A., Karidi, T., Choshen, L., Geva, M.: Jump to conclusions: Short-cutting transformers with linear transformations. arXiv preprint
arXiv:2303.09435(2023)
[202] Schuster, T., Fisch, A., Gupta, J., Dehghani, M., Bahri, D., Tran, V., Tay,
Y., Metzler, D.: Confident adaptive language modeling. Advances in Neural

### Information Processing Systems 35, 17456–17472(2022)

[203] Tang, S., Wang, Y., Kong, Z., Zhang, T., Li, Y., Ding, C., Wang, Y., Liang,
Y., Xu, D.: You need multiple exiting: Dynamic early exiting for accelerating
unifiedvisionlanguagemodel.In:Proceedingsofthe IEEE/CVFConferenceon
Computer Vision and Pattern Recognition, pp. 10781–10791(2023)
[204] Geva, M., Caciularu, A., Wang, K., Goldberg, Y.: Transformer feed-forward
layersbuildpredictionsbypromotingconceptsinthevocabularyspace.In:Proceedings of the 2022 Conference on Empirical Methods in Natural Language

### Processing, pp. 30–45 (2022)

[205] Wang, H., Zhang, Z., Han, S.: Spatten: Efficient sparse attention architecture
with cascade token and head pruning. In: 2021 IEEE International Symposium
onHigh-PerformanceComputerArchitecture(HPCA),pp.97–110(2021).IEEE
[206] Kim, S., Shen, S., Thorsley, D., Gholami, A., Kwon, W., Hassoun, J., Keutzer,
K.: Learned token pruning for transformers. In: Proceedings of the 28th ACM
SIGKDD Conference on Knowledge Discovery and Data Mining, pp. 784–794
(2022)
[207] Li, J., Zhang, L.L., Xu, J., Wang, Y., Yan, S., Xia, Y., Yang, Y., Cao, T., Sun,
H., Deng, W., et al.: Constraint-aware and ranking-distilled token pruning for
efficient transformer inference. arXiv preprint arXiv:2306.14393(2023)
62

<!-- Page 63 -->

[208] Ye, D., Lin, Y., Huang, Y., Sun, M.: Tr-bert: Dynamic token reduction for
accelerating bert inference. arXiv preprint arXiv:2105.11618(2021)
[209] Guan, Y., Li, Z., Leng, J., Lin, Z., Guo, M.: Transkimmer: Transformer learns
to layer-wise skim. arXiv preprint arXiv:2205.07324(2022)
[210] Cao, Q., Paranjape, B., Hajishirzi, H.: Pumer: Pruning and merging tokens for
efficient vision language models. arXiv preprint arXiv:2305.17530(2023)
[211] Tan, W.: Infor-coef: Information bottleneck-based dynamic token downsamplingforcompactandefficientlanguagemodel.arXivpreprintarXiv:2305.12458
(2023)
[212] Wang, Z., Chen, J., Zhou, W., Liu, M., Qin, B.: Smarttrim: Adaptive tokens
and parameters pruning for efficient vision-language models. arXiv preprint
arXiv:2305.15033(2023)
[213] Pan,Z.,Wu,Q.,Jiang,H.,Xia,M.,Luo,X.,Zhang,J.,Lin,Q.,Ru¨hle,V.,Yang,
Y., Lin, C.-Y., et al.: Llmlingua-2: Data distillation for efficient and faithful
task-agnostic prompt compression. arXiv preprint arXiv:2403.12968(2024)
[214] Kim, J.-H., Yeom, J., Yun, S., Song, H.O.: Compressed context memory for
online language model interaction. arXiv preprint arXiv:2312.03414(2023)
[215] Dong, H., Chen, B., Chi, Y.: Prompt-prompted Adaptive Structured Pruning
for Efficient LLM Generation (2024). https://arxiv.org/abs/2404.01365
[216] Fu, Q., Cho, M., Merth, T., Mehta, S., Rastegari, M., Najibi, M.: LazyLLM:
Dynamic Token Pruning for Efficient Long Context LLM Inference (2024).
https://arxiv.org/abs/2407.14057
[217] Burton, F.W.: Speculative computation, parallelism, and functional programming. IEEE Transactions on Computers 100(12), 1190–1193(1985)
[218] Leviathan, Y., Kalman, M., Matias, Y.: Fast inference from transformers via
speculative decoding. In: International Conference on Machine Learning, pp.

## 19274–19286(2023). Pmlr

[219] Chen,C.,Borgeaud,S.,Irving,G.,Lespiau,J.-B.,Sifre,L.,Jumper,J.:Accelerating large language model decoding with speculative sampling. arXiv preprint
arXiv:2302.01318(2023)
[220] Spector,B.,Re,C.:Acceleratingllminferencewithstagedspeculativedecoding.
arXiv preprint arXiv:2308.04623(2023)
[221] Wu, B., Zhong, Y., Zhang, Z., Huang, G., Liu, X., Jin, X.: Fast distributed
inference serving for large language models. arXiv preprint arXiv:2305.05920
(2023)
63

<!-- Page 64 -->

[222] Mo, Z., Wang, L., Wei, J., Zeng, Z., Cao, S., Ma, L., Jing, N., Cao, T., Xue,
J., Yang, F., et al.: Lut tensor core: Lookup table enables efficient low-bit llm
inference acceleration. arXiv preprint arXiv:2408.06003(2024)
[223] Tang,Z.,Zhu,E.:BrainTransformers:SNN-LLM(2024).https://arxiv.org/abs/
2410.14687
[224] Wang,T.,Fan,R.,Huang,M.,Hao,Z.,Li,K.,Cao,T.,Lu,Y.,Zhang,Y.,Ren,
J.:Ripple:AcceleratingLLMInferenceonSmartphoneswithCorrelation-Aware

### Neuron Management (2024). https://arxiv.org/abs/2410.19274

[225] Liang, W., Liu, T., Wright, L., Constable, W., Gu, A., Huang, C.-C., Zhang,
I., Feng, W., Huang, H., Wang, J., Purandare, S., Nadathur, G., Idreos, S.:
TorchTitan: One-stop PyTorch native solution for production ready LLM pretraining (2024). https://arxiv.org/abs/2410.06511
[226] Borzunov, A., Baranchuk, D., Dettmers, T., Ryabinin, M., Belkada, Y., Chumachenko, A., Samygin, P., Raffel, C.: Petals: Collaborative inference and
fine-tuning of large models. arXiv preprint arXiv:2209.01188(2022)
[227] Li, S., Liu, H., Bian, Z., Fang, J., Huang, H., Liu, Y., Wang, B., You, Y.:
Colossal-ai: A unified deep learning system for large-scale parallel training. In:
Proceedings of the 52nd International Conference on Parallel Processing, pp.
766–775 (2023)
[228] Andonian, A., Anthony, Q., Biderman, S., Black, S., Gali, P., Gao, L., Hallahan, E., Levy-Kramer,J., Leahy, C., Nestler, L., Parker,K., Pieler, M., Phang,
J., Purohit, S., Schoelkopf, H., Stander, D., Songz, T., Tigges, C., Th´erien,
B., Wang, P., Weinbach, S.: GPT-NeoX: Large Scale Autoregressive Language
ModelinginPyTorch(2023).https://doi.org/10.5281/zenodo.5879544.https://
www.github.com/eleutherai/gpt-neox
[229] Chen,D.,Youssef,A.,Pendse,R.,Schleife,A.,Clark,B.K.,Hamann,H.,He,J.,
Laino,T.,Varshney,L.,Wang,Y.,Sil,A.,Jabbarvand,R.,Xu,T.,Kindratenko,
V., Costa, C., Adve, S., Mendis, C., Zhang, M., Nu´n˜ez-Corrales, S., Ganti, R.,
Srivatsa, M., Kim, N.S., Torrellas, J., Huang, J., Seelam, S., Nahrstedt, K.,
Abdelzaher,T.,Eilam,T.,Zhao,H.,Manica,M.,Iyer,R.,Hirzel,M.,Adve,V.,
Marinov, D., Franke, H., Tong, H., Ainsworth, E., Zhao, H., Vasisht, D., Do,
M., Oliveira, F., Pacifici, G., Puri, R., Nagpurkar, P.: Transforming the Hybrid
Cloud for Emerging AI Workloads (2024). https://arxiv.org/abs/2411.13239
[230] Cho, J., Kim, M., Choi, H., Heo, G., Park, J.: Llmservingsim: A hw/sw cosimulation infrastructure for llm inference serving at scale. In: 2024 IEEE
International Symposium on Workload Characterization (IISWC), pp. 15–29.
IEEE, ??? (2024). https://doi.org/10.1109/iiswc63097.2024.00012 . http://dx.
doi.org/10.1109/IISWC63097.2024.00012
64

<!-- Page 65 -->

[231] Xu, M., Song, C., Tian, Y., Agrawal, N., Granqvist, F., Dalen, R., Zhang, X.,
Argueta, A., Han, S., Deng, Y., et al.: Training large-vocabulary neural language models by private federated learning for resource-constraineddevices.In:
ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and

### Signal Processing (ICASSP), pp. 1–5 (2023). IEEE

[232] Woisetschl¨ager,H.,Isenko,A.,Wang,S.,Mayer,R.,Jacobsen,H.-A.:Federated
fine-tuningofllmsontheveryedge:Thegood,thebad,theugly.arXivpreprint
arXiv:2310.03150(2023)
[233] Shen, Y., Shao, J., Zhang, X., Lin, Z., Pan, H., Li, D., Zhang, J., Letaief,
K.B.: Large language models empowered autonomous edge ai for connected
intelligence. arXiv preprint arXiv:2307.02779(2023)
[234] Ge, T., Chen, S.-Q., Wei, F.: Edgeformer: A parameter-efficient transformer
for on-device seq2seq generation. In: Proceedings of the 2022 Conference on
Empirical Methods in Natural Language Processing, pp. 10786–10798(2022)
[235] Sankar,C., Ravi, S., Kozareva,Z.: Proformer:Towardson-device lsh projection
based transformers. In: Proceedings of the 16th Conference of the European
Chapter of the Association for Computational Linguistics: Main Volume, pp.
2823–2828(2021)
[236] Huang, Z., Hou, L., Shang, L., Jiang, X., Chen, X., Liu, Q.: Ghostbert: Generate more features with cheap operations for bert. In: Proceedings of the 59th
Annual Meeting of the Association for Computational Linguistics and the 11th
InternationalJointConferenceonNaturalLanguageProcessing(Volume1:Long

### Papers), pp. 6512–6523(2021)

[237] Iandola, F., Shaw, A., Krishna, R., Keutzer, K.: Squeezebert: What can computer vision teach nlp about efficient neural networks? In: Proceedings of
SustaiNLP: Workshop on Simple and Efficient Natural Language Processing,
pp. 124–135(2020)
[238] Wu, Z.,Liu,Z.,Lin,J.,Lin,Y., Han,S.:Lite transformerwithlong-shortrange
attention. arXiv preprint arXiv:2004.11886(2020)
[239] Liu,Z.,Zhao,C.,Iandola,F.,Lai,C.,Tian,Y.,Fedorov,I.,Xiong,Y.,Chang,E.,
Shi,Y.,Krishnamoorthi,R.,Lai,L.,Chandra,V.:MobileLLM:OptimizingSubbillion Parameter Language Models for On-Device Use Cases (2024). https://
arxiv.org/abs/2402.14905
[240] Zhang, M., Cao, J., Shen, X., Cui, Z.: EdgeShard: Efficient LLM Inference via
Collaborative Edge Computing (2024). https://arxiv.org/abs/2405.14371
[241] Park, Y., Hyun, J., Cho, S., Sim, B., Lee, J.W.: Any-PrecisionLLM: Low-Cost
Deployment of Multiple, Different-Sized LLMs (2024). https://arxiv.org/abs/
65

<!-- Page 66 -->

2402.10517
[242] Kim, B., Cha, S., Park, S., Lee, J., Lee, S., Kang, S.-h., So, J., Kim, K., Jung,
J., Lee, J.-G., Lee, S., Paik, Y., Kim, H., Kim, J.-S., Lee, W.-J., Ro, Y., Cho,
Y., Kim, J.H., Song, J., Yu, J., Lee, S., Cho, J., Sohn, K.: The breakthrough
memorysolutionsforimprovedperformanceonllminference.IEEEMicro44(3),
40–48 (2024) https://doi.org/10.1109/MM.2024.3375352
[243] Laskaridis, S., Katevas, K., Minto, L., Haddadi, H.: MELTing point: Mobile
EvaluationofLanguageTransformers(2024).https://arxiv.org/abs/2403.12844
[244] Xu, M., Song, C., Tian, Y., Agrawal, N., Granqvist, F., Dalen, R., Zhang,
X., Argueta, A., Han, S., Deng, Y., Liu, L., Walia, A., Jin, A.: Training
Large-Vocabulary Neural Language Models by Private Federated Learning for
Resource-ConstrainedDevices (2022). https://arxiv.org/abs/2207.08988
[245] Yin, W., Xu, M., Li, Y., Liu, X.: LLM as a System Service on Mobile Devices
(2024). https://arxiv.org/abs/2403.11805
[246] Li, J., Sun, Z., He, X., Zeng, L., Lin, Y., Li, E., Zheng, B., Zhao, R., Chen,
X.:LocMoE:ALow-OverheadMoEforLargeLanguageModelTraining(2024).
https://arxiv.org/abs/2401.13920
[247] Shen,Y.,Guo,Z.,Cai,T.,Qin,Z.:JetMoE:ReachingLlama2Performancewith
0.1M Dollars (2024). https://arxiv.org/abs/2404.07413
[248] Bai,G., Li, Y.,Li, Z.,Zhao,L., Kim,K.:Fedspallm: Federatedpruning oflarge
language models. arXiv preprint arXiv:2410.14852(2024)
[249] Tang, Z., Kang, X., Yin, Y., Pan, X., Wang, Y., He, X., Wang, Q., Zeng,
R., Zhao, K., Shi, S., Zhou, A.C., Li, B., He, B., Chu, X.: FusionLLM: A
Decentralized LLM Training System on Geo-distributed GPUs with Adaptive

### Compression (2024). https://arxiv.org/abs/2410.12707

[250] Doosthosseini, A., Decker, J., Nolte, H., Kunkel, J.M.: Chat AI: A Seamless
Slurm-Native Solution for HPC-Based Services (2024). https://arxiv.org/abs/
2407.00110
[251] Wang, Y., Chen, K., Tan, H., Guo, K.: Tabi: An efficient multi-level inference
system for large language models. In: Proceedings of the Eighteenth European

### Conference on Computer Systems, pp. 233–248 (2023)

[252] Peng, Z., Wang, Z., Deng, D.: Near-duplicate sequence search at scale for
large language model memorization evaluation. Proceedings of the ACM on
Management of Data 1(2), 1–18 (2023)
66

<!-- Page 67 -->

[253] Miao, X., Shi, C., Duan, J., Xi, X., Lin, D., Cui, B., Jia, Z.: Spotserve: Serving generative large language models on preemptible instances. arXiv preprint
arXiv:2311.15566(2023)
[254] Huang, K., Yin, H., Huang, H., Gao, W.: Towards green ai in fine-tuning large
languagemodelsviaadaptivebackpropagation.arXivpreprintarXiv:2309.13192
(2023)
[255] Jiao, X., Yin, Y., Shang, L., Jiang, X., Chen, X., Li, L., Wang, F., Liu, Q.:
Tinybert: Distilling bert for natural language understanding. arXiv preprint
arXiv:1909.10351(2019)
[256] Shen, H., Hanwen, C., Bo, D., Yu, L., Hengyu, M.: Efficient llm inference on
cpus. arXiv preprint arXiv:2311.00502(2023)
[257] Wu, Y., Zhao, Y., Hu, B., Minervini, P., Stenetorp, P., Riedel, S.: An efficient memory-augmented transformer for knowledge-intensive nlp tasks. arXiv
preprint arXiv:2210.16773(2022)
[258] Ma,Z.,Ethayarajh,K.,Thrush,T.,Jain,S.,Wu,L.,Jia,R.,Potts,C.,Williams,
A., Kiela, D.: Dynaboard: An evaluation-as-a-serviceplatform for holistic nextgeneration benchmarking. Advances in Neural Information Processing Systems
34, 10351–10367(2021)
[259] Strubell, E., Ganesh, A., McCallum, A.: Energy and policy considerations for
deep learning in nlp. arXiv preprint arXiv:1906.02243(2019)
[260] Schmidt, V., Goyal, K., Joshi, A., Feld, B., Conell, L., Laskaris, N., Blank, D.,
Wilson, J., Friedler, S., Luccioni, S.: Codecarbon: estimate and track carbon
emissions from machine learning computing. Cited on, 20 (2021)
[261] Anthony, L.F.W., Kanding, B., Selvan, R.: Carbontracker: Tracking and predicting the carbon footprint of training deep learning models. arXiv preprint
arXiv:2007.03051(2020)
[262] Henderson,P.,Hu,J.,Romoff,J.,Brunskill,E.,Jurafsky,D.,Pineau,J.:Towards
thesystematicreportingoftheenergyandcarbonfootprintsofmachinelearning.
The Journal of Machine Learning Research 21(1), 10039–10081(2020)
[263] Lacoste, A., Luccioni, A., Schmidt, V., Dandres, T.: Quantifying the carbon
emissions of machine learning. arXiv preprint arXiv:1910.09700(2019)
[264] Faiz,A.,Kaneda,S.,Wang,R.,Osi,R.,Sharma,P.,Chen,F.,Jiang,L.:Llmcarbon: Modeling the end-to-end carbon footprint of large language models. arXiv
preprint arXiv:2309.14393(2023)
[265] Wu,C.,Zhang,H.,Ju,L.,Huang,J.,Xiao,Y.,Huan,Z.,Li,S.,Meng,F.,Liang,
67

<!-- Page 68 -->

L., Zhang, X., et al.: Rethinking memory and communication cost for efficient
large language model training. arXiv preprint arXiv:2310.06003(2023)
[266] Xu, C., Zhou, W., Ge, T., Xu, K., McAuley, J., Wei, F.: Beyond preserved
accuracy:Evaluatingloyaltyandrobustnessofbertcompression.arXivpreprint
arXiv:2109.03228(2021)
[267] Stanton, S., Izmailov, P., Kirichenko, P., Alemi, A.A., Wilson, A.G.: Does
knowledge distillation really work? Advances in Neural Information Processing

### Systems 34, 6906–6919(2021)

[268] Hooker, S., Moorosi, N., Clark, G., Bengio, S., Denton, E.: Characterising bias
in compressed models. arXiv preprint arXiv:2010.03058(2020)
[269] Su, D., Zhang, H., Chen, H., Yi, J., Chen, P.-Y., Gao, Y.: Is robustness the
cost of accuracy?–a comprehensive study on the robustness of 18 deep image
classificationmodels. In:Proceedingsofthe EuropeanConferenceonComputer

### Vision (ECCV), pp. 631–648(2018)

[270] Treviso, M., Lee, J.-U., Ji, T., Aken, B.v., Cao, Q., Ciosici, M.R., Hassid, M.,
Heafield, K., Hooker, S., Raffel, C., et al.: Efficient methods for natural language processing: A survey. Transactions of the Association for Computational

### Linguistics 11, 826–860(2023)

[271] Pareto, V.: Cours D’´economie Politique vol. 1. Librairie Droz, ??? (1964)
[272] Santhanam, K., Saad-Falcon, J., Franz, M., Khattab, O., Sil, A., Florian,
R., Sultan, M.A., Roukos, S., Zaharia, M., Potts, C.: Moving beyond downstream task accuracy for information retrieval benchmarking. arXiv preprint
arXiv:2212.01340(2022)
[273] Liu, X., Sun, T., He, J., Wu, J., Wu, L., Zhang, X., Jiang, H., Cao, Z., Huang,
X., Qiu, X.: Towardsefficient nlp: A standard evaluation and a strong baseline.
arXiv preprint arXiv:2110.07038(2021)
[274] Naveed, H., Khan, A.U., Qiu, S., Saqib, M., Anwar,S., Usman, M., Barnes,N.,
Mian, A.: A comprehensive overview of large language models. arXiv preprint
arXiv:2307.06435(2023)
[275] Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., Bowman, S.R.: Glue: A
multi-taskbenchmarkandanalysisplatformfornaturallanguageunderstanding.
arXiv preprint arXiv:1804.07461(2018)
[276] Wang,A.,Pruksachatkun,Y., Nangia,N.,Singh,A.,Michael,J.,Hill, F.,Levy,
O., Bowman, S.: Superglue: A stickier benchmark for general-purposelanguage
understanding systems. Advances in neural information processing systems 32
(2019)
68

<!-- Page 69 -->

[277] Bojar, O., Chatterjee, R., Federmann, C., Graham, Y., Haddow, B., Huck, M.,
Yepes, A.J., Koehn, P., Logacheva, V., Monz, C., et al.: Findings of the 2016
conference on machine translation (wmt16). In: First Conference on Machine
Translation, pp. 131–198 (2016). Association for Computational Linguistics
[278] Barrault,L., Biesialska, M., Bojar,O., Costa-juss`a,M.R., Federmann, C., Graham, Y., Grundkiewicz, R., Haddow, B., Huck, M., Joanis, E., et al.: Findings
of the 2020 conference on machine translation (wmt20). In: Proceedings of the

### Fifth Conference on Machine Translation, pp. 1–55 (2020)

[279] Rajpurkar,P.,Zhang,J.,Lopyrev,K.,Liang,P.:Squad:100,000+questions for
machine comprehension of text. arXiv preprint arXiv:1606.05250(2016)
[280] Rajpurkar, P., Jia, R., Liang, P.: Know what you don’t know: Unanswerable
questions for squad. arXiv preprint arXiv:1806.03822(2018)
[281] Min, S., Boyd-Graber,J., Alberti, C., Chen, D., Choi, E., Collins, M., Guu, K.,
Hajishirzi, H., Lee, K., Palomaki, J., et al.: Neurips 2020 efficientqa competition: Systems, analyses and lessons learned.In: NeurIPS 2020 Competition and

### Demonstration Track, pp. 86–111 (2021). PMLR

[282] Wang,A.,Wolf,T.:Overviewofthesustainlp2020sharedtask.In:Proceedings
of SustaiNLP: Workshopon Simple andEfficient NaturalLanguageProcessing,
pp. 174–178(2020)
[283] Zhou, W., Zeng, Y., Diao, S., Zhang, X.: Vlue: A multi-task benchmark for
evaluating vision-language models. arXiv preprint arXiv:2205.15237(2022)
[284] Tay, Y., Dehghani, M., Abnar, S., Shen, Y., Bahri, D., Pham, P., Rao, J.,
Yang, L., Ruder, S., Metzler, D.: Long range arena: A benchmark for efficient
transformers. arXiv preprint arXiv:2011.04006(2020)
[285] Bajaj, P., Campos, D., Craswell, N., Deng, L., Gao, J., Liu, X., Majumder,
R., McNamara, A., Mitra, B., Nguyen, T., et al.: Ms marco: A human generated machine reading comprehension dataset. arXiv preprint arXiv:1611.09268
(2016)
[286] Ford, B.W., Zong, Z.: Portauthority: Integrating energy efficiency analysis into
cross-platform development cycles via dynamic program analysis. Sustainable

### Computing: Informatics and Systems 30, 100530(2021)

[287] Xie, Y., Chen, S., Ni, Q., Wu, H.: Integration of resource allocation and
task assignment for optimizing the cost and maximum throughput of business
processes. Journal of Intelligent Manufacturing 30(3), 1351–1369(2019)
[288] Shamshirband, S., Joloudari, J.H., Shirkharkolaie, S.K., Mojrian, S., Rahmani,
F., Mostafavi, S., Mansor, Z.: Game theory and evolutionary optimization
69

<!-- Page 70 -->

approachesappliedto resourceallocationproblems in computing environments:

### A survey. Mathematical Biosciences and Engineering (2021)

[289] Wei,J.,Wang,X.,Schuurmans,D.,Bosma,M.,Chi,E.,Le,Q.,Zhou,D.:Chain
of thought prompting elicits reasoningin large language models. arXiv preprint
arXiv:2201.11903(2022)
[290] Diao, S., Wang,P., Lin, Y., Zhang,T.: Active prompting with chain-of-thought
for large language models. arXiv preprint arXiv:2302.12246(2023)
[291] Vilalta,R.,Drissi,Y.:Aperspectiveviewandsurveyofmeta-learning.Artificial
intelligence review 18, 77–95 (2002)
[292] Elsken, T., Metzen, J.H., Hutter, F.: Neural architecture search: A survey. The

### Journal of Machine Learning Research 20(1), 1997–2017(2019)

[293] Murshed,M.S.,Murphy,C.,Hou,D.,Khan,N.,Ananthanarayanan,G.,Hussain,
F.: Machine learning at the network edge: A survey. ACM Computing Surveys

## (Csur) 54(8), 1–37 (2021)

[294] Shi, W., Cao, J., Zhang, Q., Li, Y., Xu, L.: Edge computing: Vision and
challenges. IEEE internet of things journal 3(5), 637–646(2016)
[295] Zhang, C., Xie, Y., Bai, H., Yu, B., Li, W., Gao, Y.: A survey on federated
learning. Knowledge-BasedSystems 216, 106775 (2021)
70