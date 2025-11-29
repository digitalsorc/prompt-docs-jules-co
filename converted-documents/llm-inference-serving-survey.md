---
title: "LLM Inference Serving Survey"
original_file: "./LLM_Inference_Serving_Survey.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "fine-tuning", "multimodal"]
keywords: ["llm", "inference", "memory", "cache", "serving", "arxivpreprintarxiv", "model", "decoding", "attention", "gpu"]
summary: "<!-- Page 1 -->

LLM Inference Serving: Survey of Recent

### Advances and Opportunities

Baolin Li∗, Yankai Jiang∗, Vijay Gadepally†, Devesh Tiwari∗
∗ Northeastern University, † MIT
Abstract—This survey offers a comprehensive overview of enhancements that maintain the integrity of standard LLM
recent advancements in Large Language Model (LLM) serving decoding processes. systems,focusingonresearchsincetheyear2023.Wespecifically

### While a few prior LLM inference system surveys exist [4],

exam"
related_documents: []
---

# LLM Inference Serving Survey

<!-- Page 1 -->

LLM Inference Serving: Survey of Recent

### Advances and Opportunities

Baolin Li∗, Yankai Jiang∗, Vijay Gadepally†, Devesh Tiwari∗
∗ Northeastern University, † MIT
Abstract—This survey offers a comprehensive overview of enhancements that maintain the integrity of standard LLM
recent advancements in Large Language Model (LLM) serving decoding processes.
systems,focusingonresearchsincetheyear2023.Wespecifically

### While a few prior LLM inference system surveys exist [4],

examine system-level enhancements that improve performance
[5], [6], these generally cover a broader scope and do not
and efficiency without altering the core LLM decoding mechanisms. By selecting and reviewing high-quality papers from specificallyemphasizesystemresearch.Additionally,manyof
prestigious ML and system venues, we highlight key innovations the papers discussed in those surveys involve decoding algoand practical considerations for deploying and scaling LLMs rithmmodificationsthatcanaffectmodelaccuracy.Oursurvey,
in real-world production environments. This survey serves as a
incontrast,explicitlyfocusesonsystem-levelsolutionsthatdo
valuable resource for LLM practitioners seeking to stay abreast
not alter the core LLM decoding mechanisms. Moreover, our
of the latest developments in this rapidly evolving field.
survey encompasses a significant body of research published
I. INTRODUCTION afterthereleaseoftheseearliersurveys,thusprovidingamore
Large language models (LLMs) have rapidly gained im- comprehensive and up-to-date overview of the field.
mense popularity since the release of ChatGPT. However, We have organized the recent advances in LLM serving
deployingandscalingthesepowerfulAImodelsinproduction systems into four distinct categories, each with its own set of
environments has presented significant challenges. The sub- challenges and opportunities, which we will delve into in the
stantial computational and memory demands of LLMs often following sections.
necessitatetheuseofhigh-performanceGPUservers,yeteven KV cache and memory management. Efficient memory
theseresourcescanbestrainedbythesheersizeofthemodels management is crucial to handle the dynamic growth of
and the lengthy text sequences they process. KV caches, which store previous key-value pairs to acceler-
The growing demand for LLM-powered applications has ate LLM inference. Recent research explores non-contiguous
fueled a surge of research into LLM serving systems. In this memory allocation, distributed management, and intelligent
paper, we present a comprehensive survey of these systems, caching strategies to optimize memory utilization. Compresfocusing on advancements since 2023. While previous LLM siontechniquesarealsobeinginvestigatedtoreducetheoversystemresearchexisted,thelandscapehasdramaticallyshifted allmemoryfootprint,ultimatelyenhancingLLMperformance
within the last year. Nearly every major system conference and scalability by allowing for longer context lengths and
now features dedicated sessions on LLMs, with a particular lower memory overhead.
emphasis on serving systems due to their widespread deploy-

### LLM computation optimization. Efforts to optimize LLM

ment and the importance of low-latency performance for user
computation focus on request batching to maximize resource
experience.
utilization. Additionally, disaggregating the inference process
Thesheervolumeofresearchpublishedinsuchashorttimeinto prefill and decode phases enables independent optimizaframe makes it difficult for LLM practitioners to stay abreast
tion and hardware specialization. Model parallelism, employof developments and identify the most promising approaches
ing various techniques, facilitates efficient execution across
for real-world deployment. This survey aims to provide a
multiple GPUs. These strategies collectively enhance LLM
clear overview of the current state of the art, highlighting key
execution efficiency and hardware utilization.
areasofinnovationandpracticalconsiderationsforproduction
Cloud LLM deployment. Cloudplatformsprovideascalable
environments.
In this survey, we have meticulously selected all the high- and cost-effective foundation for LLM inference. However,
quality research papers focused exclusively on LLM serving challenges remain in optimizing costs and resource utilizasystems, published between January 2023 and June 2024. tion. Research is addressing this through techniques such as
Our selection criteria prioritized publications from prestigious spotinstancemanagement,serverlessoptimizations,intelligent
machine learning (ML) and system venues (e.g., ASPLOS, resource allocation, and power management. Additionally,
MLSys, OSDI), as well as impactful arXiv submissions from strategies like cloud task co-location and token delivery optiestablished industry and academic research groups. Notably, mizationenhanceuserexperienceandoverallcloudefficiency.
we exclude studies that modify LLM decoding algorithms Emerging research fields. Emerging areas in LLM serving
(e.g., multiple decoding head [1], lookahead decoding [2], include retrieval-augmented generation (RAG) and mixturekey token selection [3]) and solely focus on system-level of-experts (MoE) inference. RAG faces challenges related to
4202
luJ
71
]CD.sc[
1v19321.7042:viXra

<!-- Page 2 -->

Concatenation, Projection WW00
Self-attention Calculation
Norm Layer

## Qq Kk Vv


## Wwqq Wwkk Wwvv Nff

Block
1
Block
2
Block

## N

Prefill Phase Decoding Phase

### KV-Cache

Iteration 1 a Iteration 2 Iteration 3 Iteration 4
“Computer discipline . <EOS>
science is”

### Encoded Input Prompt X Output

Fig. 2: Prefill and decoding phase in the LLM inference.

### Fig.1:Transformer-basedLLMarchitectureincludingboththe

decoding phase handles the generation of subsequent tokens.
multi-head attention mechanism and feed-forward network.
We visualize this process in Fig. 2.
the computational overhead of increased input lengths due to The prefill phase starts with a tokenized and encoded
retrieved documents, while MoE inference grapples with effi- representation of the prompt going through layers of the
cient communication and load balancing between distributed transformers. Note that the generated key-value (KV) pairs
experts. Other research efforts address ethical concerns in of all transformer blocks are cached during the prefill phase,
LLM serving, such as fairness and environmental sustainabil- referred to as KV cache [9]. It ensures that the model can
ity, for which we provide a comprehensive list of relevant generate tokens more efficiently without recomputing the
studies. KV vectors of all previous tokens. Let the input prompt
P = [p ,p ,...,p ], during the prefill phase, a new token is
1 2 n

## Ii. Background

generated,denotedasP ,andthenewK andV arecached
n+1
A. Overview of Transformer-based LLM Architecture as [(k ,v ),(k ,v ),...,(k ,v )].
1 1 2 2 n n
Mainstream LLMs are built on multiple transformer The decoding phase is where the model generates new
blocks [7]. Each identical transformer primarily consists of tokens autoregressively. The LLM predicts the next token,
self-attention-based Multi-head Attention (MHA) operations appendsthenewlygeneratedtokenp n+1 totheoriginalprompt
and Feed-Forward Networks (FFN). Initially, the transformer P, and updates the KV cache. Note that the KV cache grows
applies three weight matrices (WQ,WK,WV) to the input linearly with the number of tokens generated. The autoregres-
X (encodedrepresentationofinputtextsequence)tocompute sive LLM inference process is outlined in Algorithm 1.
queries Q, keys K, and values V. Then, the Self-attention is Algorithm 1 Autoregressive LLM Inference
calculated as:
Input P: encoded input sequence [p ,p ,...,p ]
1 2 n
Q=XWQ;K =XWK;V =XWV Output X: generated new sequence [].
QKT 1: Forward Pass ([p 1 ,p 2 ,...,p n ])

### Attention(Q,K,V)=softmax( √ )V

d k 2: Store the KV cache: [(k 1 ,v 1 ),(k 2 ,v 2 ),...,(k n ,v n )]
This is the calculation of one attention head (H ), and 3: for i from 1 to M do
i
multiple heads are concatenated and linearly projected into 4: Predict the next token p n+i using the KV cache.
the final attention result: 5: Store (k n+i ,v n+i ) to the KV cache.

### H =Attention(XWQ,XWK,XWQ) 6: X ←X∪{p n+i }

i i i i 7: if p n+i is EOS token or len(X)>max length then
Multi-Head Attention=Concat(H 1 ,H 2 ,...,H h )WO 8: break

### MHA makes transformers focus on different parts of the

sequence in different representational spaces. Next, following

## Iii. Memorymanagementandcaching

the MHA block, the normalized output is fed into a position-

### Inthissection,weexplorememorymanagementtechniques

wise FFN, which consists of two linear transformations with
to mitigate memory footprint and access overhead during
a ReLU activation.
LLM inference. While model parameters remain constant and
FFN(x)=max(0,xW +b )W +b
1 1 2 2
intermediate activations are relatively small, the KV cache –
TheFFNcanbeappliedseparatelytoeachposition,further used to store attention information – grows substantially with
refining the information captured by the MHA block. The thenumberofgeneratedtokens.Therefore,recentresearchhas
output will have the same dimension as the input X. Fig. 1 focused on efficient KV cache management to enable larger
provides a visualization of the LLM architecture. batch sizes and longer context processing.
B. Overview of LLM Inference A. Efficient Management of KV Cache
LLMinferencegeneratesoutputtokensautoregressively[8] PagedAttention [10] identifies that the KV cache dynambasedontheinitialinputsequencesP,referredtoasPrompts. ically grows and shrinks over time as the model generates
This process is divided into two major phases: the prefill new tokens, but the request generation lifetime and length
phase and the decoding phase. The prefill phase is essential are not known a priori. Thus, it proposes to manage the
for setting up the model to generate text efficiently, while the KV cache as non-contiguous memory blocks. Compared to

<!-- Page 3 -->

contiguousKVcache,non-contiguousKVcachemanagement byrehearsingtheattentioncomputationofthecurrentlayerin
significantly reduces the memory waste on pre-allocation and the preceding layer and prefetches only the essential entries
fragmentation.Duetoitsefficientmemorymanagementusing to the GPU, thereby reducing the data transfer overhead.
pages, PagedAttention has become an industry norm in LLM LoongServe[20]introducesanewparallelismparadigmcalled
serving frameworks, supported by TGI [11], vLLM [10] and Elastic Sequence Parallelism (ESP) to dynamically adapt to
TensorRT-LLM [12]. resource usage variance between requests and phases (pre-
Despite its success, researchers still identify its weakness filling and decoding) of a request. It reduces KV cache
as PagedAttention requires rewriting attention kernels to ac- migrationoverheadandKVcachefragmentationwhenserving
commodate the non-contiguous memory blocks, its memory long sequences.
manageraddssoftwarecomplexityandredundancy,andintro-

### C. Compression of KV Cache

duces performance overhead. Recently, vAttention [13] was
proposedtoretaintheKVcacheincontiguousvirtualmemory. Due to the large memory footprint of LLM serving, some
It leverages pre-existing low-level system calls for demand systems have resorted to compressing the KV cache. On
paging, which is a standard operating system feature to re- top of memory aggregation and communication scheduling,
duce the software complexity. vAttention overlaps memory FlexGen [21] uses fine-grained groupwise quantization to
allocation with computation, pre-allocates memory ahead of compress the weights and KV cache to 4 bits. KIVI [22]
time, and defers memory reclamation to hide the latency of analyzes the element distribution of the LLM KV cache
memoryallocationandimprovetheoverallperformanceofthe and applies asymmetric quantization of the Key and Value
system. cache. KIVI quantizes the key cache per-channel (grouping
Besides system memory management, other efforts have elements along the channel dimension) and the value cache
addressed application-specific KV cache efficiency. Prompt per-token to achieve minimum quantization error. Gear [23]
Cache[14]designsspecificpromptschemaforuserstosubmit achieves near-lossless high-ratio KV cache compression by
their requests, so that attention states from these pre-defined quantizing the majority of entries of similar magnitudes and
modules (e.g., system prompt) can be reused across multiple employs a low-rank matrix to approximate the quantization
prompts.AttentionStore[15]identifiesthathumaninteractions error. MiniCache [24] observes that the KV cache states
with applications such as ChatGPT are mostly multi-turn exhibit high similarity between adjacent layers in the middleconversations. However, LLM engines would discard the KV to-deep portion of LLMs. Based on this insight, MiniCache
cachewhentheusersessionbecomesinactivetofreeupHBM leverages this high similarity to merge them into a shared
space for other active sessions and re-compute the whole KV representation to reduce redundancy, while also identifying
cacheagainwhenthesessionbecomesactive,leadingtoextra and retaining distinct states that are crucial for maintaining
pre-filling costs. AttentionStore utilizes slower-mediums (e.g., the model’s performance, preventing information loss during
CPU memory and disk), overlaps KV cache loading with compression.
computation, and designs intelligent pre-fetching and eviction
policies.

## Iv. Computationtaskscheduling

Besides memory and KV cache management, the compu-

### B. Support for Long-Context Applications

tation of LLM also presents significant system challenges.
Serving long-context LLM applications is particularly chal- Due to the sequential dependency between tokens during the
lenging as the size of the KV cache scales with the number autoregressive generation, LLM can only generate one token
of tokens. The limited memory limits LLM’s ability to handle at a time for each request. Thus, LLM inference workloads
long sequences, demanding more memory-efficient solutions. are less resource-efficient than training workloads on GPU
Ring attention [16] is a novel distributed approach that lever- hardware that is designed for massively parallel execution.
ages blockwise computation of attention and feedforward of Following this incentive, we investigate system solutions that
long sequences across multiple devices. It efficiently overlaps optimize the scheduling of computation tasks during the
KV cache communication with computation and extends the inference process.
context length by the device count times. Infinite-LLM [17]

### A. Request Batching

is another distributed solution, it breaks down KV cache into
smaller manageable units called rBlocks across GPUs/CPUs, When a single request cannot efficiently utilize the GPU,
and efficiently manages them with dynamic memory sharing it is intuitive to batch multiple inference requests together to
and coordination. MemServe [18] unifies handling of inter- boost the occupancy of GPU cores. However, as responses to
request and intra-request optimizations for LLM serving by differentpromptscanhavesignificantlyvariablelengths,when
introducing MemPool, a distributed memory pool to manage batched together, the shorter responses are forced to wait for
KV cache across all cluster memory and employs a global thelongeronestocomplete,resultingincomputationalwaste.
scheduler to maximize KV cache reuse. Response Length Perception and Sequence Scheduling [25]
WhenthecontextgrowslargerthantheGPUmemorylimit, instructstheLLMtopredicttheresponselengthbeforestarting
mostsystemsoffloadtheKVcachetotheCPU.InfiniGen[19] to generate the actual response, and batches queries with
is a solution that speculates the important KV cache entries similar predicted response lengths to reduce computational

<!-- Page 4 -->

waste. A similar approach, S3 [26], finetunes a Distillbert C. Model Parallelism
model for sequence length prediction. Upon mispredictions,
LLMs can have hundreds of billions of parameters, reit preempts sequences that exceed their allocated memory and
quiring model parallel execution on multiple GPUs. Pope et
retrain the predictor to learn from its mistakes.
al. [9] develop an analytical model for inference efficiency,
Generationlengthpredictionbasedbatchingislesspractical enabling the selection of optimal multi-dimensional partitionduetothestrongrelianceonthepredictor.Orca[27]proposes ing techniques tailored for TPU v4 slices based on specific
continuous batching at the token level rather than the request application needs. HeteGen [33] introduces a framework for
level.Itcontinuouslyschedulesnewrequestsintothebatchas heterogeneous parallel computing using CPUs and GPUs.
soon as a request in the current batch completes. Continuous It employs a heterogeneous parallel computing algorithm
batchingnowhasbecomeanindustrystandardinLLMserving to distribute computation within its hybrid heterogeneous
frameworks,incorporatedintothesoftwareofTGI,vLLM,and parallelism framework and enables asynchronous overlap to
TensorRT-LLM. Based on continuous batching, DeepSpeed- mitigate I/O bottlenecks between the CPU and GPU.
FastGen [28] proposes a dynamic SplitFuse mechanism that ExeGPT [34] can find an optimal schedule control variable
decomposes long prompts into smaller chunks scheduled ofthebatchsizeandtensorparallelismdegreethatmaximizes
acrossmultipleiterationsandcomposesshortpromptstogether inference throughput while adhering to a given latency limit.
to maintain the inference running at high throughput region It leverages the distribution of input and output sequence
(boundedbyGPUcomputenotmemorybandwidth).Asimilar lengthstoallocateresourcesefficientlyanddeterminethebest
idea was explored in Sarathi-Serve [29], which splits prefill parallelism configuration. Helix [35] is designed to partition
requests into smaller chunks and schedules them alongside an LLM across heterogeneous GPUs and different types of
ongoing decode requests without causing stalls (stall-free networkconnections.Itformulatesitsmodelpartitionscenario
batching). This allows new requests to join a running batch as a max-flow problem of a directed, weighted graph whose
withoutpausingongoingdecodes,leadingtominimalpipeline nodes represent GPU instances and edges capture both GPU
bubbles. andnetworkheterogeneitythroughtheircapacitiesinthemaxflow problem.
B. Disaggregated Inference

## V. Llmsinthecloud

LLM inference goes through a prefill stage to process the LLM deployments are computationally intensive and often
prompt, populate the KV cache, and start the decoding stage require significant infrastructure to run effectively. Cloud
to generate tokens (Sec. II). Existing LLM serving systems platforms offer a scalable and cost-effective solution for decolocate the two phases and batch the computation of prefill ploying LLMs, eliminating the need for expensive hardware
and decoding across all users and requests. However, these investments. The flexibility of cloud deployment allows ortwo phases display distinct characteristics and can interfere ganizations to easily adjust resources as needed, ensuring
with each other when requests at the prefill stage are batched optimalperformanceandminimizingdowntime.However,the
with requests at the decoding stage. TetriInfer [30] separates significant costs associated with cloud computing resources
prefill and decode instances, allowing each phase to run and the challenge of ensuring their efficient utilization can be
independently and preventing interference between batch-like major obstacles for LLM service providers.
prefill jobs and latency-critical decode tasks. It employs a
two-level scheduling algorithm that incorporates predicted A. Cloud Deployment Cost
resourceusagetoavoidschedulinghotspotsduringthedecode Modern clouds offer a variety of spot instances (e.g., AWS
phase, ensuring efficient resource allocation and minimizing EC2 Spot Instance, Azure Spot Virtual Machines, Google
contention. Cloud Spot VMs). These instances run on spare capacity and
Splitwise [31] extensively characterizes the differences in are offered at highly discounted prices, but may be preempted
the execution and utilization patterns of the prefill and de- at any time when other instances need the capacity. SpotcodingstageondifferentgenerationsofGPUs(heterogeneous Serve [36] addresses the challenges of using these instances
hardware). Splitwise proposes to split these two phases into for LLM serving, such as how to quickly adapt to changes in
separatemachines,allowingforspecializedhardwareforeach available instances and how to minimize the cost of migrating
phasetoachievebetterutilization,reducehardwareownership instanceswheninterruptionsoccur.Italsointroducesastateful
costs, and save energy. DistServe [32] designs a placement inference recovery mechanism for inference engines to comalgorithm to schedule the prefill and decoding stage compu- mit their progress at the token level and efficiently resume
tation tasks. In clusters with high-speed cross-node networks, interrupted requests.
DistServe optimizes parallelism configurations for prefill and Serverlessisarecentlyemergedcloudcomputingparadigm,
decodinginstancesindependentlytoachievethebestper-GPU where inference service users can submit their model to the
goodput; In clusters with limited cross-node bandwidth, it cloud and the cloud provider takes care of all infrastructure
ensures that prefill and decoding instances of the same stage provision and scaling with varying inference request load,
are co-located within a single node and optimizes parallelism and saves unused hardware costs for customers. A major
configurations within the node. challengeinserverlessismitigatingcoldstart,whereaservice

<!-- Page 5 -->

instancewouldbeshutdownafternotbeingaccessedforsome for each token generation. In contrast, PEFT, which processes
time, and once a new request arrives, it would experience all tokens of a request simultaneously, is mainly constrained
a latency spike associated with re-initializing the service by compute resources, such as the tensor cores on GPUs.
instance. ServerlessLLM [37] addresses these latency issues FlexLLM introduces a token-level fine-tuning mechanism that
by utilizing the underutilized storage and memory resources breaks down the fine-tuning process into smaller, more manavailable on GPU servers. It introduces a new checkpoint ageable token-level computations to minimize memory usage
format and loading system to speed up LLM model loading, and inference latency, making co-serving feasible.
a live migration mechanism to avoid interrupting ongoing AsLLMinferencefollowstoken-by-tokengeneration,users
inferences, and a locality-aware server allocation strategy to also read the response word-by-word. Andes [43] defines a
minimize LLM inference cold start latency. userexperiencemetricofQualityofExperience(QoE)fortext
Cloud providers often offer a wide range of heterogeneous streaming services. It is formulated by comparing the actual
instance selections labeled at different prices. Me´lange [38] token delivery timeline (TDT) of a request with its expected
is a cloud resource allocation framework that considers three TDT. The expected TDT is determined by the expected time
key LLM service characteristics: request size, request rate, to first token (TTFT) and the expected token delivery speed
and service-level objective. It automatically navigates through (TDS), which can vary depending on factors like the user’s
the GPU option space to determine the most cost-efficient typical reading speed. The intuition is generating text too fast
heterogeneous GPU allocation for a given LLM service. With (thanuserreadingspeed)doesnotyieldQoEbenefits,wasting
theresourcesallocatedandmodelhostedontheGPUs,Llum- cloud resources. Andes addresses this by strategically allocatnix[39]isadynamicschedulingsystemforLLMservingthat ing GPU resources among multiple requests to optimize QoE.
addresses the challenges of heterogeneous and unpredictable Itemploysadynamicpriority-basedpreemptiveschedulerthat
requestsbyreschedulingthemacrossmultiplemodelinstances operates at the token level, prioritizing urgent requests and
at runtime – similar to how OS context switches across cores. preempting those that have been sufficiently served. Andes
Llumnix introduces an efficient live migration mechanism for improves average QoE and can handle higher request rates
requests and their in-memory states, minimizing downtime while maintaining similar token generation throughput.
during rescheduling, and employs a dynamic scheduling policy that unifies various rescheduling scenarios, such as load
balancing, de-fragmentation, prioritization, and auto-scaling. VI. EMERGINGRESEARCHFIELDS
This efficiency has resulted in significant cost savings while
achieving similar tail latency. A. Retrieval Augmented Generation
B. Cloud Efficiency Retrieval-AugmentedGeneration(RAG)[44]isatechnique
A key bottleneck resource in cloud datacenters is power, that enhances LLMs by incorporating external information
which LLMs are quickly saturating due to their growing sources. It addresses the limitations of LLMs in retaining
computation demand. POLCA [40] characterizes the power factual knowledge and their tendency to generate inaccurate
consumption patterns of LLMs in the cloud and finds that or fabricated information (hallucinations). RAG operates in
whiletrainingLLMsdemandsalotofpowerandcanstrainthe two stages: retrieval and generation. During retrieval, the
data center’s power infrastructure, inference tasks offer more system identifies the most relevant contexts from an external
flexibility for power management due to their less predictable knowledge base or corpus based on the given query. Once
power demands. POLCA devises a framework to manage the relevant contexts are retrieved, they are integrated into the
power in LLM inference clusters by dynamically applying LLM’sgenerationprocessindifferentprocessesincludingcontechniquessuchasGPUfrequencylockingandpowercapping. catenation (where the retrieved contexts are simply appended
PerLLM [41] takes the LLM inference to an edge-cloud to the query) and cross-attention (where the LLM attends to
collaboration scenario, where it leverages the strengths of the retrieved contexts during generation).
edgecomputing(lowlatency,reducedenergycosts)andcloud SparseRAG[45]observesthatRAGcanbecomputationally
computing (high processing power) to handle LLM inference expensive due to the increased input length from retrieved
tasks efficiently. PerLLM employs a Constraint Satisfaction documents. It first encodes retrieved documents in parallel
Upper Confidence Bound (CS-UCB) algorithm to optimize to eliminate latency caused by long-range attention, then
service scheduling and resource allocation while adhering to selectively decodes the output by attending only to highly
constraints like processing time, bandwidth, and computing relevant caches chosen via prompting the LLM with special
power – achieving energy LLM efficiency. control tokens. RAGCache [46] caches intermediate states of
Workloads often get co-located in the cloud environment. external knowledge with a knowledge tree to organize and
FlexLLM [42] is a system designed to efficiently service storeintermediatestates.Thecachedknowledgecanbeshared
LLM inference and parameter-efficient fine-tuning (PEFT) across multiple queries to reduce the redundant computation.
requests in the same iteration. LLM inference, which involves Another knowledge caching technique is CacheBlend [47],
generatingtexttokenbytoken,isprimarilylimitedbymemory whichselectivelyrecomputesasmallportionoftheKVcache
bandwidth due to the need to access all model parameters based on the preceding text in the input.

<!-- Page 6 -->

B. Mixture-of-Experts Inference consumption. (ii) Expert buffering leverages the observation
that expert activation is often sparse and exhibits temporal
The mixture of Experts (MoE) is used in LLMs to imlocality. By caching frequently used (hot) experts in GPU
prove efficiency and performance. It divides the model into
memory and buffering less active experts in CPU memory,
specialized sub-networks, called “experts”, each focusing on
expertbufferingreducesthestaticmemoryallocationonGPU.
a specific task. A “gating” network then directs input to the
(iii) Imbalanced token assignments to experts can lead to botmostsuitableexpert.IntheinferenceprocessofanMoEtranstlenecks and performance degradation. Expert load balancing
former,theinputisfirstpassedthroughagatingnetwork.This
ensures a more even distribution of workload across devices.
networkdetermineswhichexpert,oracombinationofexperts,
is best suited to process the specific input. MoE’s sparsely

### C. Miscellaneous Fields

activatedsubsetofexpertsavoidsthelargecomputationalneed
to process the entire model for every inference. Ethics and environmental sustainability. Sheng et. al [54]
MoE Communication. Lina [48] is a system designed to ensure fairness in serving LLMs by introducing a Virtual
address the all-to-all communication bottleneck in distributed Token Counter (VTC). VTC defines LLM serving fairness
MoE. The all-to-all communication occurs when distributed based on a cost function that accounts for the number of
MoE sends tokens to their selected experts for processing and input and output tokens processed. It achieves fairness by
then sends the results back to the original devices. During tracking the services received by each client and prioritizing
inference, Lina dynamically schedules resources based on thosewiththeleastservice,whilealsoconsideringthevarying
expert popularity, balancing the transfer size and bandwidth costs of processing input and output tokens. Sprout [55] adof all-to-all communication across devices. ExFlow [49] is dresses the environmental sustainability of LLMs and designs
an optimization technique to accelerate the inference of dis- a framework to reduce the carbon footprint of LLM inference
tributedMoE.Itleveragestheinter-layerexpertaffinity,which services. Sprout introduces “generation directives” to guide
is the correlation between expert selection across different the autoregressive generation process, balancing the need for
MoElayers.ByplacingexpertsoncorrespondingGPUsbased sustainability with the demand for high-quality generation.
on their affinity, ExFlow reduces cross-GPU routing latency Inferencepipelineoptimization. FlashDecoding++[56]conand improves inference throughput. ducts inference engine performance optimization, addressing
Expert offloading. SiDA-MoE [50] (Sparsity-inspired Data- several issues in softmax synchronization, GPU kernel, and
Aware) leverages both main memory and GPU memory by dataflow. For example, the decoding phase performs linear
exploiting the inherent sparsity of expert activation in MoE GEMM operations with flat shapes where the batch size
models.SiDA-MoEincludestwoparallelthreads:aninference dimension involved in the multiplication is much smaller
thread and a hash-building thread. The hash-building thread than the others. FlashDecoding++ accelerates flat GEMM
predicts which experts will be activated for each token at with double buffering that overlaps computation and data
each layer, storing these predictions in a hash table. The transfer and hides the memory latency in loading input mainference thread then uses this information to dynamically trices. Parrot [57] is designed to optimize the performance
load activated experts onto the GPU and offload inactive of LLM-based applications that involve multiple LLM reexpertstomainmemory,maximizingGPUmemoryutilization. quests with complex workflows. Parrot performs data flow
MoE-Infinity [51] takes a different approach toward expert analysis and uncovers correlations across multiple LLM reoffloading. The system leverages the observation that MoE quests, and introduces a series of optimizations to improve
models exhibit sparse activation and temporal locality during performance. FlashAttention-3 [58] is a method to speed up
inference,meaningonlyafewexpertsarerepeatedlyactivated attention for large language models and long-context applifor processing a specific sequence. MoE-Infinity traces expert cations. It introduces techniques like warp specialization and
activation at the sequence level, enabling it to predict which asynchronous block-wise operations to optimize GPU utilizaexperts will be needed and prefetch them accordingly. tion.FlashAttention-3achievessignificantspeeduponHopper
GPUs compared to its predecessor and reduces numerical
MoE Efficiency. Fiddler [52] is a system designed to
errors in FP8 computations.
efficiently run these models on a limited number of GPUs,
evenwhenthemodel’ssizewouldtypicallyexceedtheGPU’s Frugalinference. FrugalGPT[59]proposesseveralsolutions
memory capacity. Fiddler strategically distributes the model’s to reduce the inference cost, such as prompt caching and
components.Non-expertlayers,whichareusedfrequently,are LLM cascading which uses a sequence of LLMs, starting
kept on the GPU. A subset of expert layers, chosen based withcheaperonesandmovingtomoreexpensiveonesonlyif
on how often they’re used, are also placed on the GPU. necessary. SpecInfer [60] applies speculative decoding using
The rest remain in the CPU’s memory. Huang et al. [53] smaller, speculative models to predict the LLM’s output,
introduce three optimization techniques to address the MoE reducing the computational resources. These predictions are
inferenceinefficiencies.(i)Dynamicgatingallowsthenumber organizedintoatreestructure,andtheiraccuracyisverifiedin
of tokens processed by each expert to vary, which avoids the parallelagainsttheLLM.RouteLLM[61]dynamicallyselects
over-provisioning of resources in static gating and reduces between a stronger and a weaker LLM during inference to
computational waste, communication overhead, and memory optimize the balance between cost and response quality.

<!-- Page 7 -->

VII. CONCLUSION [14] I. Gim, G. Chen, S.-s. Lee, N. Sarda, A. Khandelwal, and L. Zhong,
“Prompt cache: Modular attention reuse for low-latency inference,”
This survey has presented a comprehensive overview of Proceedings of Machine Learning and Systems, vol. 6, pp. 325–338,
recent advancements in LLM serving systems, emphasizing 2024.
[15] B. Gao, Z. He, P. Sharma, Q. Kang, D. Jevdjic, J. Deng, X. Yang,
the importance of system-level solutions for enhancing per-
Z. Yu, and P. Zuo, “Cost-Efficient large language model serving
formance and efficiency. We have highlighted key innovations for multi-turn conversations with CachedAttention,” in 2024 USENIX
fordeployingandscalingLLMs,pavingthewayforthefuture Annual Technical Conference (USENIX ATC 24). Santa Clara, CA:
USENIX Association, Jul. 2024, pp. 111–126. [Online]. Available:
development of LLM serving systems.
https://www.usenix.org/conference/atc24/presentation/gao-bin-cost
[16] H. Liu, M. Zaharia, and P. Abbeel, “Ring attention with blockwise
transformersfornear-infinitecontext,”arXivpreprintarXiv:2310.01889,
2023.

## Acknowledgments

[17] B. Lin, T. Peng, C. Zhang, M. Sun, L. Li, H. Zhao, W. Xiao,
Q. Xu, X. Qiu, S. Li et al., “Infinite-llm: Efficient llm service for

### ThismaterialisbaseduponworksupportedbytheAssistant

longcontextwithdistattentionanddistributedkvcache,”arXivpreprint
Secretary of Defense for Research and Engineering under Air arXiv:2401.02669,2024.
ForceContractNo.FA8702-15-D-0001,andUnitedStatesAir [18] C. Hu, H. Huang, J. Hu, J. Xu, X. Chen, T. Xie, C. Wang, S. Wang,
Y. Bao, N. Sun et al., “Memserve: Context caching for disaggregated

### Force Research Laboratory Cooperative Agreement Number

llmservingwithelasticmemorypool,”arXivpreprintarXiv:2406.17565,
FA8750-19-2-1000. Any opinions, findings, conclusions, or 2024.
recommendations expressed in this material are those of the [19] W. Lee, J. Lee, J. Seo, and J. Sim, “Infinigen: Efficient generative inferenceoflargelanguagemodelswithdynamickvcachemanagement,”
author(s) and do not necessarily reflect the views of the
arXivpreprintarXiv:2406.19707,2024.
Assistant Secretary of Defense for Research and Engineering, [20] B. Wu, S. Liu, Y. Zhong, P. Sun, X. Liu, and X. Jin, “Loongserve:
or the United States Air Force. The U.S. Government is Efficiently serving long-context large language models with elastic
sequenceparallelism,”arXivpreprintarXiv:2404.09526,2024.
authorizedtoreproduceanddistributereprintsforGovernment
[21] Y. Sheng, L. Zheng, B. Yuan, Z. Li, M. Ryabinin, B. Chen, P. Liang,
purposes notwithstanding any copyright notation herein. C. Re´, I. Stoica, and C. Zhang, “Flexgen: High-throughput generative
inferenceoflargelanguagemodelswithasinglegpu,”inInternational
ConferenceonMachineLearning. PMLR,2023,pp.31094–31116.

## References

[22] Z.Liu,J.Yuan,H.Jin,S.Zhong,Z.Xu,V.Braverman,B.Chen,and
X.Hu,“Kivi:Atuning-freeasymmetric2bitquantizationforkvcache,”
[1] T. Cai, Y. Li, Z. Geng, H. Peng, J. D. Lee, D. Chen, and T. Dao, arXivpreprintarXiv:2402.02750,2024.
“Medusa: Simple llm inference acceleration framework with multiple [23] H. Kang, Q. Zhang, S. Kundu, G. Jeong, Z. Liu, T. Krishna, and
decodingheads,”arXivpreprintarXiv:2401.10774,2024. T. Zhao, “Gear: An efficient kv cache compression recipefor near-
[2] Y. Fu, P. Bailis, I. Stoica, and H. Zhang, “Break the sequential de- losslessgenerativeinferenceofllm,”arXivpreprintarXiv:2403.05527,
pendency of llm inference using lookahead decoding,” arXiv preprint 2024.
arXiv:2402.02057,2024. [24] A.Liu,J.Liu,Z.Pan,Y.He,G.Haffari,andB.Zhuang,“Minicache:
[3] M.Adnan,A.Arunkumar,G.Jain,P.Nair,I.Soloveychik,andP.Ka- Kvcachecompressionindepthdimensionforlargelanguagemodels,”
math,“Keyformer:Kvcachereductionthroughkeytokensselectionfor arXivpreprintarXiv:2405.14366,2024.
efficient generative inference,” Proceedings of Machine Learning and [25] Z. Zheng, X. Ren, F. Xue, Y. Luo, X. Jiang, and Y. You, “Response
Systems,vol.6,pp.114–127,2024. length perception and sequence scheduling: An llm-empowered llm
[4] X. Miao, G. Oliaro, Z. Zhang, X. Cheng, H. Jin, T. Chen, and Z. Jia, inferencepipeline,”AdvancesinNeuralInformationProcessingSystems,
“Towards efficient generative large language model serving: A survey vol.36,2024.
fromalgorithmstosystems,”arXivpreprintarXiv:2312.15234,2023. [26] Y. Jin, C.-F. Wu, D. Brooks, and G.-Y. Wei, “S3: Increasing gpu
[5] Z. Yuan, Y. Shang, Y. Zhou, Z. Dong, C. Xue, B. Wu, Z. Li, Q. Gu, utilizationduringgenerativeinferenceforhigherthroughput,”Advances
Y. J. Lee, Y. Yan et al., “Llm inference unveiled: Survey and roofline inNeuralInformationProcessingSystems,vol.36,pp.18015–18027,
modelinsights,”arXivpreprintarXiv:2402.16363,2024. 2023.
[6] Z. Zhou, X. Ning, K. Hong, T. Fu, J. Xu, S. Li, Y. Lou, L. Wang, [27] G.-I. Yu, J. S. Jeong, G.-W. Kim, S. Kim, and B.-G. Chun, “Orca: A
Z.Yuan,X.Lietal.,“Asurveyonefficientinferenceforlargelanguage distributedservingsystemfor{Transformer-Based}generativemodels,”
models,”arXivpreprintarXiv:2404.14294,2024. in 16th USENIX Symposium on Operating Systems Design and Imple-
[7] A.Vaswani,N.Shazeer,N.Parmar,J.Uszkoreit,L.Jones,A.N.Gomez, mentation(OSDI22),2022,pp.521–538.
Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in [28] C.Holmes,M.Tanaka,M.Wyatt,A.A.Awan,J.Rasley,S.Rajbhandari,
neuralinformationprocessingsystems,vol.30,2017. R.Y.Aminabadi,H.Qin,A.Bakhtiari,L.Kurilenkoetal.,“Deepspeed-
[8] A.Radford,K.Narasimhan,T.Salimans,I.Sutskeveretal.,“Improving fastgen:High-throughputtextgenerationforllmsviamiianddeepspeedlanguageunderstandingbygenerativepre-training,”2018. inference,”arXivpreprintarXiv:2401.08671,2024.
[9] R. Pope, S. Douglas, A. Chowdhery, J. Devlin, J. Bradbury, J. Heek, [29] A.Agrawal,N.Kedia,A.Panwar,J.Mohan,N.Kwatra,B.S.Gulavani,
K. Xiao, S. Agrawal, and J. Dean, “Efficiently scaling transformer A.Tumanov,andR.Ramjee,“Tamingthroughput-latencytradeoffinllm
inference,” Proceedings of Machine Learning and Systems, vol. 5, pp. inferencewithsarathi-serve,”arXivpreprintarXiv:2403.02310,2024.
606–624,2023. [30] C.Hu,H.Huang,L.Xu,X.Chen,J.Xu,S.Chen,H.Feng,C.Wang,
[10] W.Kwon,Z.Li,S.Zhuang,Y.Sheng,L.Zheng,C.H.Yu,J.Gonzalez, S. Wang, Y. Bao et al., “Inference without interference: Disaggre-
H. Zhang, and I. Stoica, “Efficient memory management for large gate llm inference for mixed downstream workloads,” arXiv preprint
languagemodelservingwithpagedattention,”inProceedingsofthe29th arXiv:2401.11181,2024.
SymposiumonOperatingSystemsPrinciples,2023,pp.611–626. [31] P. Patel, E. Choukse, C. Zhang, ´I. Goiri, A. Shah, S. Maleki, and
[11] “Text generation inference: A rust, python and grpc server for R.Bianchini,“Splitwise:Efficientgenerativellminferenceusingphase
text generation inference.” [Online]. Available: https://github.com/ splitting,”arXivpreprintarXiv:2311.18677,2023.
huggingface/text-generation-inference [32] Y.Zhong,S.Liu,J.Chen,J.Hu,Y.Zhu,X.Liu,X.Jin,andH.Zhang,
[12] “Tensorrt-llm: A tensorrt toolbox for optimized large language “Distserve: Disaggregating prefill and decoding for goodput-optimized
model inference.” [Online]. Available: https://github.com/NVIDIA/ largelanguagemodelserving,”arXivpreprintarXiv:2401.09670,2024.
TensorRT-LLM [33] Z.XUANLEI,B.Jia,H.Zhou,Z.Liu,S.Cheng,andY.You,“Hetegen:
[13] R.Prabhu,A.Nayak,J.Mohan,R.Ramjee,andA.Panwar,“vattention: Efficientheterogeneousparallelinferenceforlargelanguagemodelson
Dynamicmemorymanagementforservingllmswithoutpagedattention,” resource-constrained devices,” Proceedings of Machine Learning and
arXivpreprintarXiv:2405.04437,2024. Systems,vol.6,pp.162–172,2024.

<!-- Page 8 -->

[34] H.Oh,K.Kim,J.Kim,S.Kim,J.Lee,D.-s.Chang,andJ.Seo,“Exegpt: [55] B.Li,Y.Jiang,V.Gadepally,andD.Tiwari,“Towardsustainablegenai
Constraint-awareresourceschedulingforllminference,”inProceedings using generation directives for carbon-friendly large language model
ofthe29thACMInternationalConferenceonArchitecturalSupportfor inference,”arXivpreprintarXiv:2403.12900,2024.
Programming Languages and Operating Systems, Volume 2, 2024, pp. [56] K. Hong, G. Dai, J. Xu, Q. Mao, X. Li, J. Liu, Y. Dong, Y. Wang
369–384. et al., “Flashdecoding++: Faster large language model inference with
[35] Y. Mei, Y. Zhuang, X. Miao, J. Yang, Z. Jia, and R. Vinayak, “Helix: asynchronization,flatgemmoptimization,andheuristics,”Proceedings
Distributed serving of large language models via max-flow on hetero- ofMachineLearningandSystems,vol.6,pp.148–161,2024.
geneousgpus,”arXivpreprintarXiv:2406.01566,2024. [57] C.Lin,Z.Han,C.Zhang,Y.Yang,F.Yang,C.Chen,andL.Qiu,“Parrot:
[36] X.Miao,C.Shi,J.Duan,X.Xi,D.Lin,B.Cui,andZ.Jia,“Spotserve: Efficientservingofllm-basedapplicationswithsemanticvariable,”arXiv
Servinggenerativelargelanguagemodelsonpreemptibleinstances,”in preprintarXiv:2405.19888,2024.
Proceedingsofthe29thACMInternationalConferenceonArchitectural [58] J. Shah, G. Bikshandi, Y. Zhang, V. Thakkar, P. Ramani, and T. Dao,
SupportforProgrammingLanguagesandOperatingSystems,Volume2, “Flashattention-3:Fastandaccurateattentionwithasynchronyandlow-
2024,pp.1112–1127. precision,”arXivpreprintarXiv:2407.08608,2024.
[37] Y. Fu, L. Xue, Y. Huang, A.-O. Brabete, D. Ustiugov, Y. Patel, and [59] L.Chen,M.Zaharia,andJ.Zou,“Frugalgpt:Howtouselargelanguage
L.Mai,“Serverlessllm:Locality-enhancedserverlessinferenceforlarge modelswhilereducingcostandimprovingperformance,”arXivpreprint
languagemodels,”arXivpreprintarXiv:2401.14351,2024. arXiv:2305.05176,2023.
[38] T.Griggs,X.Liu,J.Yu,D.Kim,W.-L.Chiang,A.Cheung,andI.Stoica, [60] X.Miao,G.Oliaro,Z.Zhang,X.Cheng,Z.Wang,Z.Zhang,R.Y.Y.
“M\’elange:Costefficientlargelanguagemodelservingbyexploiting Wong, A. Zhu, L. Yang, X. Shi et al., “Specinfer: Accelerating large
gpuheterogeneity,”arXivpreprintarXiv:2404.14527,2024. language model serving with tree-based speculative inference and ver-
[39] B. Sun, Z. Huang, H. Zhao, W. Xiao, X. Zhang, Y. Li, and W. Lin, ification,” in Proceedings of the 29th ACM International Conference
“Llumnix:Dynamicschedulingforlargelanguagemodelserving,”arXiv on Architectural Support for Programming Languages and Operating
preprintarXiv:2406.03243,2024. Systems,Volume3,2024,pp.932–949.
[40] P.Patel,E.Choukse,C.Zhang,´I.Goiri,B.Warrier,N.Mahalingam,and [61] I. Ong, A. Almahairi, V. Wu, W.-L. Chiang, T. Wu, J. E. Gonzalez,
R.Bianchini,“Characterizingpowermanagementopportunitiesforllms M. W. Kadous, and I. Stoica, “Routellm: Learning to route llms with
inthecloud,”inProceedingsofthe29thACMInternationalConference preferencedata,”arXivpreprintarXiv:2406.18665,2024.
on Architectural Support for Programming Languages and Operating
Systems,Volume3,2024,pp.207–222.
[41] Z. Yang, Y. Yang, C. Zhao, Q. Guo, W. He, and W. Ji, “Perllm:
Personalized inference scheduling with edge-cloud collaboration for
diversellmservices,”arXivpreprintarXiv:2405.14636,2024.
[42] X.Miao,G.Oliaro,X.Cheng,M.Wu,C.Unger,andZ.Jia,“Flexllm:
Asystemforco-servinglargelanguagemodelinferenceandparameterefficientfinetuning,”arXivpreprintarXiv:2402.18789,2024.
[43] J. Liu, Z. Wu, J.-W. Chung, F. Lai, M. Lee, and M. Chowdhury,
“Andes:Definingandenhancingquality-of-experienceinllm-basedtext
streamingservices,”arXivpreprintarXiv:2404.16283,2024.
[44] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal,
H. Ku¨ttler, M. Lewis, W.-t. Yih, T. Rockta¨schel et al., “Retrievalaugmented generation for knowledge-intensive nlp tasks,” Advances in
NeuralInformationProcessingSystems,vol.33,pp.9459–9474,2020.
[45] Y. Zhu, J.-C. Gu, C. Sikora, H. Ko, Y. Liu, C.-C. Lin, L. Shu,
L. Luo, L. Meng, B. Liu et al., “Accelerating inference of retrievalaugmented generation via sparse context selection,” arXiv preprint
arXiv:2405.16178,2024.
[46] C.Jin,Z.Zhang,X.Jiang,F.Liu,X.Liu,X.Liu,andX.Jin,“Ragcache:
Efficientknowledgecachingforretrieval-augmentedgeneration,”arXiv
preprintarXiv:2404.12457,2024.
[47] J.Yao, H.Li, Y.Liu, S.Ray,Y. Cheng,Q. Zhang,K. Du,S. Lu,and
J. Jiang, “Cacheblend: Fast large language model serving with cached
knowledgefusion,”arXivpreprintarXiv:2405.16444,2024.
[48] J.Li,Y.Jiang,Y.Zhu,C.Wang,andH.Xu,“Acceleratingdistributed
{MoE} training and inference with lina,” in 2023 USENIX Annual
TechnicalConference(USENIXATC23),2023,pp.945–959.
[49] J. Yao, Q. Anthony, A. Shafi, H. Subramoni, and D. K. D. Panda,
“Exploitinginter-layerexpertaffinityforacceleratingmixture-of-experts
modelinference,”in2024IEEEInternationalParallelandDistributed
ProcessingSymposium(IPDPS). IEEE,2024,pp.915–925.
[50] Z.Du,S.Li,Y.Wu,X.Jiang,J.Sun,Q.Zheng,Y.Wu,A.Li,H.Li,
and Y. Chen, “Sida: Sparsity-inspired data-aware serving for efficient
andscalablelargemixture-of-expertsmodels,”ProceedingsofMachine
LearningandSystems,vol.6,pp.224–238,2024.
[51] L.Xue,Y.Fu,Z.Lu,L.Mai,andM.Marina,“Moe-infinity:Activationaware expert offloading for efficient moe serving,” arXiv preprint
arXiv:2401.14361,2024.
[52] K. Kamahori, Y. Gu, K. Zhu, and B. Kasikci, “Fiddler: Cpu-gpu
orchestration for fast inference of mixture-of-experts models,” arXiv
preprintarXiv:2402.07033,2024.
[53] H. Huang, N. Ardalani, A. Sun, L. Ke, H.-H. S. Lee, A. Sridhar,

### S.Bhosale,C.-J.Wu,andB.Lee,“Towardsmoedeployment:Mitigating

inefficiencies in mixture-of-expert (moe) inference,” arXiv preprint
arXiv:2303.06182,2023.
[54] Y. Sheng, S. Cao, D. Li, B. Zhu, Z. Li, D. Zhuo, J. E. Gonzalez, and
I. Stoica, “Fairness in serving large language models,” arXiv preprint
arXiv:2401.00588,2023.

## Tables

**Table (Page 2):**

| Sel |  | Block Block Block Concatenation, Projection WW00 1 2 N f-attention Calculation Norm Layer KK VV WWKK WWVV N |  |  |
|---|---|---|---|---|
| QQ | WWQQ |  |  |  |
