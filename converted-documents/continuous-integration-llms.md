---
title: "Continuous Integration LLMs"
original_file: "./Continuous_Integration_LLMs.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "dialogue"]
keywords: ["gat", "llm", "prediction", "link", "quality", "data", "multivariate", "wireless", "model", "time"]
summary: "<!-- Page 1 -->

Multivariate Wireless Link Quality Prediction Based
on Pre-trained Large Language Models

### Zhuangzhuang Yan1, Xinyu Gu1,2, Shilong Fan1, Zhenyu Liu3

1 Beijing University of Posts and Telecommunications, Beijing , China
2Purple Mountain Laboratories, Nanjing , China
3Institute for Communication Systems, University of Surrey, United Kingdom, Guildford
Email: yanzz, guxinyu, fansl@bupt.edu.cn, zhenyu.liu@surrey.ac.uk
Abstract—Accurateandreliablelinkqualityprediction(LQP) [4] pr"
related_documents: []
---

# Continuous Integration LLMs

<!-- Page 1 -->

Multivariate Wireless Link Quality Prediction Based
on Pre-trained Large Language Models

### Zhuangzhuang Yan1, Xinyu Gu1,2, Shilong Fan1, Zhenyu Liu3

1 Beijing University of Posts and Telecommunications, Beijing , China
2Purple Mountain Laboratories, Nanjing , China
3Institute for Communication Systems, University of Surrey, United Kingdom, Guildford
Email: yanzz, guxinyu, fansl@bupt.edu.cn, zhenyu.liu@surrey.ac.uk
Abstract—Accurateandreliablelinkqualityprediction(LQP) [4] proposed a temporal convolutional network based on an
is crucial for optimizing network performance, ensuring com- improved self-attention mechanism (TCNS), where a selfmunication stability, and enhancing user experience in wireless
attentionmechanism(SAM)isemployedtocaptureshort-term
communications. However, LQP faces significant challenges due
correlationsinlinkquality,therebyenhancingpredictionaccuto the dynamic and lossy nature of wireless links, which are
influenced by interference, multipath effects, fading, and block- racy.Althoughdeeplearning-basedmodelshavedemonstrated
age. In this paper, we propose GAT-LLM, a novel multivariate strong performance in predicting time series for wireless link
wireless link quality prediction model that combines Large quality, they also encounter limitations and challenges. For

### LanguageModels(LLMs)withGraphAttentionNetworks(GAT)

instance, these models typically require a mass of training
to enable accurate and reliable multivariate LQP of wireless
datatoperformeffectively.Incertainapplicationscenarios,accommunications. By framing LQP as a time series prediction
taskandappropriatelypreprocessingtheinputdata,weleverage quiring sufficient data can be problematic. Additionally, deep
LLMs to improve the accuracy of link quality prediction. To learning models may exhibit instability in their predictions
address the limitations of LLMs in multivariate prediction due when exposed to noise or outliers, compromising the model’s
to typically handling one-dimensional data, we integrate GAT
robustness and overall reliability.
to model interdependencies among multiple variables across

### Toaddressthesechallenges,largelanguagemodels(LLMs)

differentprotocollayers,enhancingthemodel’sabilitytohandle
complex dependencies. Experimental results demonstrate that offer a promising alternative. Unlike traditional deep learning
GAT-LLM significantly improves the accuracy and robustness models, LLMs possess strong contextual understanding and
of link quality prediction, particularly in multi-step prediction generalization capabilities, enabling them to perform effecscenarios.
tively with relatively limited training data [5]. Moreover,

### IndexTerms—linkqualityprediction,timeseries,multivariate,

LLMsexcelatprocessingcomplexsequentialdataandcapturlarge language models, Graph Attention Networks
inglong-termdependencies,leveragingtheiradvancedpattern
recognition and reasoning capabilities to facilitate efficient

## I. Introduction

time series prediction [6, 7]. In [6], the authors developed
AS the application scenarios of wireless networks become a foundational model for time series analysis, demonstrating
increasinglydiverseandcomplex,thequalityofwireless strong performance in time series prediction tasks. [7] introlinks significantly impacts network performance, communi- ducedanovelframeworkcalledTime-LLM,whichrepurposes
cation reliability, and user experience. Therefore, efficiently LLMsforgeneraltimeseriespredictionwhilemaintainingthe
and accurately predicting link quality to maintain network underlying integrity of the original language models. Despite
stability and enhance user experience has become a pressing growingevidencethatlargemodelsholdthepotentialtorevochallenge in wireless communications. However, in wireless lutionize wireless communication [8], their direct application
communication networks, factors such as interference, mul- in wireless link quality time series prediction has not been
tipath effects, fading, and blockage can cause fluctuations explored yet.
in wireless signals, resulting in unstable and time-varying Furthermore, multiple parameters across different protocol
wirelesslinks.Additionally,radiopropagationconditionsvary layers influence link quality in communication systems. Alsignificantlyovertimeandspace[1],furthercomplicatinglink though LLMs perform well in time series forecasting tasks,
quality prediction (LQP). they face challenges when handling multivariate time series
Exising LQP traditional methods primarily relied on clas- data. This is because LLMs, based on the transformer archisical statistical models. For example, an autoregressive inte- tecture,typicallyprocessone-dimensionaltimeseriesdata[9],
grated moving average (ARIMA) model was applied in [2] whereas multivariate predicting involves multi-dimensional
to reduce channel congestion through link quality prediction. time series data. [9] employed dimensional multiplexing to
Withtheadventofdeeplearning,moreadvancedmethodshave capture the correlations between dimensions by merging mulemerged.In[3],theauthorsutilizedaconvolutionallongshort- tiple time series dimensions into a single sequence before
term memory (Conv-LSTM) model to predict the link quality inputtingintoLLM,therebyimprovingthemultivariatepredicinpointcloud-basedmillimeter-wavecommunicationsystems. tion accuracy. However, as the number of time series dimen-
5202
naJ
02
]GL.sc[
1v74211.1052:viXra

<!-- Page 2 -->


### TABLEI:NetworkParametersofDataset

Multivariate Input Multivariate Output
DLBw DLBw
••• •••
Layer Parameter Name Notes

## P Ulsinr Ulsinr P

DLBw bps H ••• ••• H

## Y Y


### ULSINR db DLOccupyPRBNum DLOccupyPRBNum


### PHY number,valuerange0-100, ••• Predict •••

DLOccupyPRBNum cellnetworkparameters CellDLMA •• C • Rate Model CellDLMA •• C • Rate

## Llm

CellDLMACRate bit,cellnetworkparameters M DLMACRate DLMACRate M
MAC DLMACRate bit A ••• ••• A

## C C


### MCS valuerange0-28 MCS ••• GAT MCS •••

PDCPOccupyBuffer bit PDCPOccupyBuffer PDCPOccupyBuffer

### PDCP PDCPUnusedBuffer bit ••• •••

DLPDCPSDUNum number P D C PDCPUnuse • d •• Buffer PDCPUnuse • d •• Buffer P D C
P DLPDCPSDUNum DLPDCPSDUNum P
••• •••
Fig.1:Inputandoutputdemonstrationsofpredictionmodel.
sionsincreases,themultiplexinganddemultiplexingprocesses
become increasingly complex, leading to a degradation in
modelperformance.[10]usedamultivariatepatchingstrategy the Physical (PHY) layer, Medium Access Control (MAC)
to extract correlations among multiple variables, which were layer, and Packet Data Convergence Protocol (PDCP) layer.
then input into the LLM through linear transformations to Specificdetailsregardingtheseparametersandtheirassociated
enhance the performance of multivariate prediction. However, layers are presented in Table I.
this approach primarily relies on the linear integration of In wireless systems, the quality of wireless links can be
features, limiting its ability to capture complex nonlinear or assessed through various parameters, each of which will be
higher-order relationships. [11] proposed a new framework described in detail below.
for graph network optimization based on LLM, focusing on
• Downlink Bandwith (DLBw) represents the maximum
optimizing unmanned aerial vehicle (UAV) trajectories and
available data transmission rate from a base station to
communicationresourceallocation.Inspiredbythis,weapply
a user terminal in a wireless communication system.
Graph Attention Networks (GAT) to capture the correlations

### It directly influences link quality by affecting channel

among multiple variables. Unlike [11], we treat the variables
utilization and overall network capacity.
as nodes in the graph.
• Uplink Signal to Interference plus Noise Ratio

### Insummary,weproposeaninnovativemodelthatcombines

(ULSINR) refers to the ratio of signal power to noise
GATwithLLM,termedGAT-LLM.Themodelenablesmultipowerwhenauserdevicesendsasignaltoabasestation
variate prediction of wireless link quality, offering a pathway
in a wireless communication system. It directly affects
to intelligent cross-layer optimization in communication syssignal strength and data transmission rates.
tems. The main contributions of this paper are summarized as
• DLOccupyPRBNum refers to the number of physical
follows.
resource blocks (PRBs) occupied in the downlink of
• This study applies LLMs to wireless link quality predic- a wireless communication system. This metric reflects
tion. By framing link quality prediction as a time series information, such as resource allocation, making it a
task, we fully exploit the pattern recognition and reason- critical factor in determining the quality of the downlink.
ingcapabilitiesoftheLLMstoenhancetheaccuracyand • CellDLMACRate denotes the average downlink data
robustness of wireless link predictions. transmission rate across the entire cell at the MAC layer,
• To address the limitations of LLMs in multivariate pre- providing a crucial indicator of overall network perfordiction, we develop a GAT-LLM model. By constructing mance and cell load. This metric is closely associated
multivariate into a graph and using GAT to extract mul- with link quality.
tivariate correlations, this model enhances its capability • DLMACRate specifically refers to the actual data transto handle complex dependencies, thereby improving link missionrateofauseronthedownlink,directlyreflecting
quality prediction accuracy and facilitating cross-layer link quality.
intelligent optimization in wireless networks. • Modulation and Coding Scheme (MCS) combines
modulation techniques with coding strategies in wire-

## Ii. Datasetanalysisandformulationof

less communication systems. It directly impacts the data

## Multivariatelinkqualityprediction

transmission rate and anti-interference capability.
A. Dataset Analysis • PDCPOccupyBuffer indicates the occupied buffer capacityinthePDCPlayer,whichstoresdatapacketsawait-

### The dataset used in this study is the Wireless Link Quality

Prediction dataset provided by China Mobile 1. With a sam- ing transmission, and PDCPUnusedBuffer denotes the
available buffer capacity. They are closely linked to link
pling frequency of 1 ms, the dataset consists of 22,661 data
quality and significantly influence the data transmission
items.Eachdataitemincludesnineparametersextractedfrom
success rate and retransmission mechanisms.
1https://doi.org/10.12448/3l3e-w818 • DLPDCPSDUnum denotes the number of PDCP data

<!-- Page 3 -->


### Ⅳ Ⅴ Ⅲ LLM Token

Add & Layer Norm Multivariate Sequences
Output Projection
linear
••• transformation

### Feed Forward


### Pre-trained LLM

(Backbone Network) GAT Output

### Add & Layer Norm Flatten & Linear

M A u t l t t e i n -H tio e n ad ⊕ E P m o b s e it d io d n in a g l s aggregation aggregation aggregation

### Multi


### Attention

Input Embedding attention attention attention
coefficient coefficient coefficient

## Ⅰ Ⅱ

Preprocessing Linear

### Instance Norm

Fe C a r t o u s re s- E V x a t r r i a a c b t l i e o n ℎ1 ℎ2 ℎ3 ℎ4 Con G st r r a u p c h tion

### Data Completion ••• (GAT)

(Lagrange interpolation) ℎ0 ℎ5
Multivariate Historical Sequences ℎ8
ℎ7
ℎ6
Fig.2:ThemultivariatepredictionmodelframeworkofGAT-LLM.
units successfully transmitted in the downlink of a wire- III. GAT-LLMFORMULTIVARIATEWIRELESSLINK
less communication system. This metric reflects the effi- QUALITYPREDICTION
ciency and reliability of data transmission and is closely
GAT excels in capturing complex relationships in graphassociated with link quality.
structured data, while LLMs are proficient in processing
Basedontheprecedinganalysis,theseparametersreflectthe complex sequential data. By integrating these approaches, our
link quality from various perspectives. We use the historical proposed GAT-LLM model combines the flexibility of graph
time series of these parameters as input for the prediction structures with the sequential modeling capabilities of LLMs,
model, which generates multi-step predictions, as illustrated enhancing the accuracy and robustness of multivariate link
in Fig. 1. quality prediction. This model, illustrated in Fig. 2, comprises
four primary modules: preprocessing, input embedding, pre-
B. Formulation of Multivariate Link Quality Prediction
trained LLM, and output projection.

### Weformulatethepredictionoflinkqualityasamultivariate

Initially, multivariate historical data undergoes preprocesstime series problem. In this study, we utilize multivariate,
ing, including interpolation and normalization. The data is
represented by the vector Xt, to denote the multidimensional
then embedded to extract cross-variable features and is linparameters at a specific time t as follows,
early transformed. Combined with positional encoding, these
Xt ={xt,xt,··· ,xt }⊂RT×N , (1) embeddedsequencesarepassedthroughapre-trainedLLMto

## 1 2 N

capture temporal correlations. The output projection module
where T represents the duration of the sequence, and N
then applies a linear transformation to generate the final
denotes the number of parameters, respectively.
multivariate link quality predictions. The following sections
Given the RT×N and a fixed window size τ, with τ ⊂ T,
detail each module.
this time series is split into a fixed length input as,

### A. Input Embedding of the GAT-LLM


### A={(X1,X2,··· ,Xτ),(X1+s,X2+s,··· ,Xτ+s),

LLMs excel at processing complex sequential data, making
(2)
··· ,(XT−τ+1,XT−τ+2,··· ,XT)}, them well-suited for time series prediction. However, LLMs
face challenges when processing multivariate time series data,
where s denotes the horizontal sliding stride.
as they typically handle one-dimensional data. To address the
When considering the task of predicting the one step value
challenges, we integrate a GAT to capture the correlations

### Yt+1, the formula is as follows,

among variables, thereby enhancing prediction accuracy. The
Yt+1 =F(Xt−τ+1,Xt−τ+2,··· ,Xt), (3) detailed process is illustrated in Fig. 2 II.
Firstly, a graph G is constructed, comprising nine variables
where (Xt−τ+1,Xt−τ+2,··· ,Xt) represent the input secaptured at the same moment, where each variable is reprequence,whileF(·)denotesthepredictionmodel.Furthermore,
sentedasanode.ThelearnableweightmatrixW isutilizedto
thepredictedvalueisamultivariateoutput,definedasfollows,
linearlytransformthefeaturevectorsF ofallnodes,resulting
Yt+1 ={yt+1,yt+1,··· ,yt+1}⊂R1×M , (4) in a new feature vectors H.

## 1 2 M

Wethencalculatetheattentioncoefficiente betweennode
jk
where M denotes the number of output parameters.
j and its neighbor k,

### When making multi-step predictions, the autoregressive

method is employed to apply formula (3). e =LeakyReLU(aT[h ][h ]), (5)
jk j k

<!-- Page 4 -->


### TABLEII:SimulationParameters

where a is a learnable attention weight vector, LeakyReLU
is an activation function, and [h ][h ] represents the concatej k Parameters Value
nation of two vectors. Layers 12
In order to enhance the comparability and stability of the nembd 768

### Batchsize 512

attention coefficient, the softmax function is employed to

### Epochs 500

normalize e , resulting in the final attention coefficient α .
jk jk Optimizer Adam
Then, node j aggregates its feature vector with those of its Learningrate 0.001
adjacentnodesthroughformula(6),resultinginanewfeature HiddendimensionsofGAT 1024
vector h′, NumberofattentionheadsofGAT 16
j Durationofthesequence(T) 22661(ms)
h ′ = (cid:88) α h , (6) Trainingsteplength 19
j jk j Numberofoutputparameters(N) 9
k∈N(j) Numberofoutputparameters(M) 4
where N(j) represents the set of neighbors of node j, includ- Fixedwindowsize(τ) 20

### Horizontalslidingstride(s) 1

ing node j itself. Stepsizeforpredicting(l) 10
To enhance the expressive capacity of the model, a multihead attention mechanism is employed. Each attention head
performs the above process independently. Then the output
but rather fine-tuned all parameters. This approach enhances
features of each head are connected to get the final feature
the large language model’s suitability for wireless link quality
output,
h ′ =||K (cid:88) αk h k, (7) prediction.
j k=1 jk j
k∈N(j) C. Input and Output of the GAT-LLM
where K is the number of attention heads, || represents the The part includes two parts: preprocessing input and output
concatenation operation. projection.
After the multivariate vector X i passes through the GAT • Preprocessing: In wireless systems, the instability of
layer, the interdependencies between neighboring nodes are wireless channels frequently leads to incomplete data
captured through linear transformations, attention mecha- collection [1], as is the case with the dataset used in this
nisms, and feature integration. This process produces a new study. To address the issue of missing data, we employ
vector representation, X(cid:102)i , which not only retains the intrinsic Lagrangeinterpolationpolynomials.Additionally,weapfeatures of the node but also incorporates information from ply min-max normalization to scale all parameters linother nodes within the graph structure. Consequently, X(cid:102)i early to [0, 1], reducing discrepancies between different
exhibitsenhancedsemanticrichness,makingithighlysuitable features in the dataset, as shown in Fig. 2 I.
for subsequent predictive tasks, as shown in Fig. 2 III. • OutputProjection:Theoutputrepresentationsgenerated
Then, we apply a linear transformation on X(cid:102)i at each by the pre-trained LLM are flattened and subjected to a
moment, converting it into a token that can be recognized linear projection to produce the final prediction, denoted
by the LLM. Subsequently, we process each input token by as Y . In the output projection module, GAT-LLM emi
positional encoding to enhance the capture of time series ploysanon-linearfullyconnectedlayertomapthetokens
information within the sequence. to wireless link quality data, as shown in Fig. 2 V.
B. Fine-tuning of the GAT-LLM

## Iv. Experiments

Thepre-trainedLLMsareprimarilydesignedfortext-based

### A. Experimental Settings

tasks,makingtheirdirectapplicationtolinkqualityprediction
suboptimal. Retraining the entire LLM could address this is- 1) Evaluation Metrics
sue,butthecomputationalcostsareprohibitivelyhigh.Rather We evaluate the performance of the proposed framethan retraining the entire LLM, we fine-tune all parameters to workusingthreecommonmetrics:MeanAbsoluteError
tailor the model for wireless link quality prediction. In this (MAE) and Root Mean Square Error (RMSE). The
study, we leverage the general modeling capabilities of LLMs formula is as follows,
forlinkqualityprediction,usingGPT-2asthebackbone.With n
1 (cid:88)
millions of parameters, GPT-2 provides a robust foundation MAE = |y −yˆ|, (8)
n i i
for the early exploration of LLMs in wireless communication i=1
contexts. (cid:118)
(cid:117) n
The GPT-2 comprises learnable position embedding layers (cid:117)1 (cid:88)
and stacked transformer decoders, with the number of stacks
RMSE =(cid:116)
n
(y
i
−yˆ
i
)2 , (9)
i=1
and feature sizes adjustable as needed. Each layer includes
a multi-head self-attention layer, a feed-forward layer, and where y represents the true value, yˆ denotes the prei i
two layers of normalization layer, as shown in Fig. 2 IV. dicted value, y¯represents the mean of the actual values
During the training process, we do not freeze any parameters and n indicates the number of samples.

<!-- Page 5 -->

TABLEIII:One-steppredictionresultsofGAT-LLMandotherbenchmarkschemes.Black:best.
Multivariate GAT-LLM GPT-2 GAT-Transformer Conv-LSTM VARIMA

### Predicting MAE RMSE MAE RMSE MAE RMSE MAE RMSE MAE RMSE

DLBw 0.0052 0.0073 0.0098 0.0133 0.0534 0.0774 0.0870 0.1246 0.3163 0.5624
ULSINR 0.0029 0.0046 0.0060 0.0078 0.0232 0.0334 0.0308 0.0419 0.0879 0.2965
DLOccupyPRBNum 0.0053 0.0154 0.0105 0.0130 0.1728 0.2752 0.2346 0.2950 0.2708 0.5204
CellDLMACRate 0.0062 0.0081 0.0095 0.0122 0.0581 0.0775 0.0988 0.1331 0.0994 0.3153
DLMACRate 0.0045 0.0071 0.0072 0.0095 0.0602 0.0870 0.1399 0.1895 0.6398 0.7999
MCS 0.0050 0.0070 0.0081 0.0103 0.0462 0.0802 0.0749 0.1320 0.1135 0.3369
PDCPOccupyBuffer 0.0028 0.0043 0.0061 0.0084 0.0213 0.0293 0.0331 0.0445 0.0844 0.2905
PDCPUnusedBuffer 0.0026 0.0053 0.0042 0.0064 0.0183 0.0275 0.0229 0.0315 0.2349 0.4847
DLPDCPSDUNum 0.0045 0.0073 0.0066 0.0087 0.0570 0.0816 0.1288 0.1752 0.1779 0.4218
10
5
0
-5
-10
-15
-20
-25
2 4 6 8 10
Stepsizeforpredicting(ms)
)Bd(EAM
DLBw
10

### GAT-LLM Conv-LSTM

GPT-2 VARIMA GAT-Transformer 5
0
-5
-10
-15
-20
-25
2 4 6 8 10
Stepsizeforpredicting(ms)
)Bd(EAM
DLMACRate
10

### GAT-LLM Conv-LSTM

GPT-2 VARIMA GAT-Transformer 5
0
-5
-10
-15
-20
-25
2 4 6 8 10
Stepsizeforpredicting(ms)
)Bd(EAM

## Mcs

10

### GAT-LLM Conv-LSTM

GPT-2 VARIMA GAT-Transformer 5
0
-5
-10
-15
-20
-25
2 4 6 8 10
Stepsizeforpredicting(ms)
)Bd(EAM

## Ulsinr


### GAT-LLM Conv-LSTM


### GPT-2 VARIMA GAT-Transformer

Fig.3:ComparisonofmultivariatelinkqualitypredictionperformanceamongGAT-LLM,GPT2,GAT-transformer,Conv-LSTMandVARIMA.
Smaller MAE and RMSE values indicate better model multivariaterelationshipsandlong-rangedependenciesin
performance. time series data.
2) Simulation Setup • Conv-LSTM [3]: Conv-LSTM integrates the strengths
We choose GPT-2 as the backbone model due to its of Convolutional Neural Networks (CNNs) and LSTM
effective trade-off between inference speed and pre- networks. It is particularly well-suited for handling spadiction accuracy. Notably, our method is theoretically tiotemporal sequence data, as it effectively captures both
applicable to other LLMs. Additionally, we employ spatial and temporal dependencies in the data.
GAT for cross-variable feature extraction, with specific • VARIMA [2]: The Autoregressive Integrated Moving
parameter details provided in Table II. The GAT-LLM Average (ARIMA) model is a statistical method used
model was implemented using PyTorch 2.0.1, and all for time series analysis and prediction. To support multiexperiments were conducted on a server equipped with variate predicting, we employ its multivariate extension,
2 5318Y CPUs and 2 NVIDIA RTX 4090 GPUs. This Vector ARIMA (VARIMA), designed to handle multiple
model is intended for future deployment on the base interrelated time series.
station side, which is feasible given the base station’s
To ensure the fairness of the experiments, the models of
computational capabilities.
allbenchmarkschemes,exceptVARIMA,areconfiguredwith
consistent parameters such as hidden layer dimension and

### B. Prediction Performance Analysis

number of layers. Table III presents the MAE and RMSE
To evaluate the effectiveness of the GAT-LLM model for results for the one-step prediction across the five schemes. As
multivariate wireless link quality prediction, we compare its shown, GAT-LLM outperforms all other models in predicting
performance with four benchmark schemes: GPT-2, GAT- linkqualityacrossmostvariables,withtwoexceptions:DLOc-
Transformer, Conv-LSTM, and VARIMA. The specific im- cupyPRBNum, which performs worse than the GPT-2 scheme
plementation details of the GAT-LLM model are provided in in terms of RMSE. These results demonstrate the unique
Section III. advantages of the proposed GAT-LLM scheme in handling
• GPT-2 [6]: The GPT-2 is an autoregressive language multivariate link quality prediction.
modelbuiltontheTransformerarchitecture,knownforits Further, we perform 10-step prediction simulations, with
proficiency in processing time series data and capturing each step corresponding to 1 ms. Due to the large number
long-range dependencies. of prediction parameters, we select four key parameters,
• GAT-Transformer [12]: The GAT-Transformer model is DLBW, DLMACRate, MCS, and ULSINR, for performance
a relatively recent scheme that combines GAT with the demonstration. Specifically, DLBW and DLMACRate capture
Transformerarchitecture.Theschemeexcelsincapturing the downlink bandwidth and transmission rate, respectively;

<!-- Page 6 -->

-10
-15
-20
-25
2 4 6 8 10
Stepsizeforpredicting(ms)
)Bd(EAM

### DLBw


## -10 Gat-Llm

Univariate predict -15
-20
-25
2 4 6 8 10
Stepsizeforpredicting(ms)
)Bd(EAM

### DLMACRate


## -10 Gat-Llm

Univariate predict -15
-20
-25
2 4 6 8 10
Stepsizeforpredicting(ms)
)Bd(EAM

## Mcs

-10

## Gat-Llm -15

Univariate predict
-20
-25
2 4 6 8 10
Stepsizeforpredicting(ms)
)Bd(EAM

## Ulsinr


## Gat-Llm


### Univariate predict

Fig.4:ComparisonoflinkqualitypredictionperformancebetweenUnivariatepredictandGAT-LLM.
MCS reflects the modulation and coding characteristics of the GAT, referred to as GAT-LLM. We reformulate the link
physical layer, and ULSINR measures the uplink signal-to- quality prediction task as a time series problem to leverage
noise ratio. These parameters provide a comprehensive link LLMs’ capabilities in handling sequential data. Recognizing
quality assessment from the physical to the transport layer, that link quality is influenced by multiple interdependent
establishing a solid foundation for accurate prediction and parameters, we employ GAT to capture correlations among
analysis. Fig. 3 compares the performance of the proposed these variables. The GAT-LLM model thus combines GAT’s
GAT-LLMschemeagainstotherbenchmarkschemesinmulti- strength in modeling multivariate relationships with LLMs’
step link quality prediction. Firstly, the results demonstrate ability to process rich contextual and historical information,
that the GAT-LLM scheme outperforms the other schemes, effectivelyaddressingthecomplexitiesinherentinmultivariate
which can be attributed to its integration of GAT and LLM, link quality prediction. Experimental results demonstrate that
effectively addressing the complexities of multivariate link GAT-LLMenhancestheaccuracyandrobustnessoflinkqualquality prediction. Additionally, we observe that GPT-2 is ity predictions, particularly in multi-step predicting scenarios.
the suboptimal scheme. This success can be explained by It indicates that GAT-LLM holds significant potential as a
its Transformer-based architecture, which excels at capturing valuable tool for tackling the complexity of wireless link
long-range dependencies. After fine-tuning, GPT-2 proves to prediction in real-world communication systems.
be well-suited for temporal link quality prediction tasks.

## References


### Furthermore, all deep learning-based schemes outperform the

[1] G.Cerar,H.Yetgin,M.Mohorcˇicˇ,andC.Fortuna,“MachineLearning

### VARIMA scheme. This is because deep learning schemes

forWirelessLinkQualityEstimation:ASurvey,”IEEECommunications
excel at capturing intricate nonlinear relationships and au- Surveys&Tutorials,vol.23,no.2,pp.696–728,2021.
tomatically extracting relevant features, thereby improving [2] Z. Sayeed, E. Grinshpun, D. Faucher, and S. Sharma, “Long-term
application-level wireless link quality prediction,” in 2015 36th IEEE
prediction accuracy. In contrast, the VARIMA scheme relies
SarnoffSymposium,2015,pp.40–45.
heavilyonlinearassumptions,whichlimitsitsabilitytohandle [3] S.Ohta,T.Nishio,R.Kudo,K.Takahashi,andH.Nagata,“PointCloudcomplex, multivariate data. BasedProactiveLinkQualityPredictionforMillimeter-WaveCommunications,”IEEETransactionsonMachineLearninginCommunications
andNetworking,vol.1,pp.258–276,2023.

### C. Comparison Between Univariate and Multivariate

[4] Y.WangandL.Liu,“Wirelesslinkqualitypredictionbasedontemporal
The primary advantage of the GAT-LLM model lies in its convolutionalnetworksandself-attentionfusion,”inProceedingsofthe
20245thInternationalConferenceonComputing,NetworksandInternet
capacity to predict multivariate time series data. To assess
ofThings,2024,pp.448–453.
the impact of multivariate data on prediction accuracy, we [5] W.X.Zhao,K.Zhou,J.Li,T.Tang,X.Wang,Y.Hou,Y.Min,B.Zhang,
compared the performance of GAT-LLM with a univariate J. Zhang, Z. Dong et al., “A survey of large language models,” arXiv
preprintarXiv:2303.18223,2023.
predicting scheme. In the univariate prediction scheme, the
[6] T. Zhou, P. Niu, L. Sun, R. Jin et al., “One fits all: Power general
predicting model is the GAT-LLM, but its input is only the timeseriesanalysisbypretrainedlm,”Advancesinneuralinformation
historical data of the target variable. processingsystems,vol.36,pp.43322–43355,2023.
[7] M. Jin, S. Wang, L. Ma, Z. Chu, J. Y. Zhang, X. Shi, P.-Y. Chen,

### Fig. 4 shows a performance comparison between the GAT-

Y. Liang, Y.-F. Li, S. Pan, and Q. Wen, “Time-LLM: Time Series
LLM scheme and a univariate prediction scheme. While the ForecastingbyReprogrammingLargeLanguageModels,”inTheTwelfth
univariate scheme performs marginally better in the first step InternationalConferenceonLearningRepresentations,2024.
[8] H. Zhou, C. Hu, Y. Yuan, Y. Cui, Y. Jin, C. Chen, H. Wu, D. Yuan,
of DLBW prediction, GAT-LLM demonstrates a significant
L. Jiang, D. Wu, X. Liu, C. Zhang, X. Wang, and J. Liu, “Large
advantageasthepredictionhorizonincreases.Thissuperiority Language Model (LLM) for Telecommunications: A Comprehensive
is due to GAT-LLM’s ability to capture interdependencies SurveyonPrinciples,KeyTechniques,andOpportunities,”IEEECommunicationsSurveys&Tutorials,pp.1–1,2024.
acrossmultivariate,providingamorecomprehensiveinforma-
[9] G. Chatzigeorgakidis, K. Lentzos, and D. Skoutas, “MultiCast: Zerotionbaseforfuturepredictions,whichisanadvantagethatthe Shot Multivariate Time Series Forecasting Using LLMs,” in 2024
univariatepredictionschemelacks.Theseresultshighlightthe IEEE 40th International Conference on Data Engineering Workshops
(ICDEW),2024,pp.119–127.
critical role of multivariate prediction in improving long-term
[10] M. L. Wolff, S. Yang, K. Torkkola, and M. W. Mahoney, “Using Preprediction accuracy. trainedLLMsforMultivariateTimeSeriesForecasting,”arXivpreprint
arXiv:2501.06386,2025.
V. CONCLUSION [11] G.Sun,Y.Wang,D.Niyato,J.Wang,X.Wang,H.V.Poor,andK.B.
Letaief, “Large Language Model (LLM)-enabled Graphs in Dynamic
In this paper, recognizing the critical role and challenges Networking,”IEEENetwork,pp.1–1,2024.
[12] J.Huo,L.Wang,Z.Lu,andX.Wen,“VehicularCrowdsensingInference
of wireless link quality prediction, we propose an innovative
andPredictionWithMultiTrainingGraphTransformerNetworks,”IEEE
link quality prediction model that integrates LLMs and the InternetofThingsJournal,vol.11,no.1,pp.217–227,2024.

## Tables

**Table (Page 2):**

| Layer | Parameter Name | Note | s |
|---|---|---|---|
| PHY | DLBw | bps |  |
|  | ULSINR | db |  |
|  | DLOccupyPRBNum CellDLMACRate | number,valuer cellnetworkp bit,cellnetwork | ange0-100, arameters parameters |
| MAC | DLMACRate | bit |  |
| PDCP | MCS PDCPOccupyBuffer | valuerang bit | e0-28 |
|  | PDCPUnusedBuffer | bit |  |
|  | DLPDCPSDUNum | numb | er |


**Table (Page 2):**

| LLM |
|---|
| GAT |


**Table (Page 3):**

|  |  |
|---|---|
| Preprocessing |  |
|  |  |
|  | ••• torical Sequences |


**Table (Page 4):**

| Parameters | Value |
|---|---|
| Layers | 12 |
| nembd | 768 |
| Batchsize | 512 |
| Epochs | 500 |
| Optimizer | Adam |
| Learningrate | 0.001 |
| HiddendimensionsofGAT | 1024 |
| NumberofattentionheadsofGAT | 16 |
| Durationofthesequence(T) | 22661(ms) |
| Trainingsteplength | 19 |
| Numberofoutputparameters(N) | 9 |
| Numberofoutputparameters(M) | 4 |
| Fixedwindowsize(τ) | 20 |
| Horizontalslidingstride(s) | 1 |
| Stepsizeforpredicting(l) | 10 |
