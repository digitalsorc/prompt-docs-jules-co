---
title: "LLM Production Best Practices"
original_file: "./LLM_Production_Best_Practices.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "dialogue"]
keywords: ["cid", "tnl", "page", "attention", "onchip", "dkv", "intra", "inter", "models", "model"]
summary: "<!-- Page 1 -->

Various Lengths, Constant Speed: Efficient Language Modeling with Lightning

### Attention

ZhenQin1 WeigaoSun2 DongLi2 XuyangShen2 WeixuanSun2 YiranZhong2
Abstract However,despiteitspromise,noneofthecurrentleading
largelanguagemodels(Touvronetal.,2023a;b;Zengetal.,

### WepresentLightningAttention,thefirstlinearat-

2022; Black et al., 2022; Almazrouei et al., 2023; Team
tentionimplementationthatmaintainsaconstant
etal.,2023;Wang&Komatsuzaki,2021;Baichuan,2023;
trainingspeedfor"
related_documents: []
---

# LLM Production Best Practices

<!-- Page 1 -->

Various Lengths, Constant Speed: Efficient Language Modeling with Lightning

### Attention

ZhenQin1 WeigaoSun2 DongLi2 XuyangShen2 WeixuanSun2 YiranZhong2
Abstract However,despiteitspromise,noneofthecurrentleading
largelanguagemodels(Touvronetal.,2023a;b;Zengetal.,

### WepresentLightningAttention,thefirstlinearat-

2022; Black et al., 2022; Almazrouei et al., 2023; Team
tentionimplementationthatmaintainsaconstant
etal.,2023;Wang&Komatsuzaki,2021;Baichuan,2023;
trainingspeedforvarioussequencelengthsunder
Jiangetal.,2023)haveadoptedlinearattentionmechanisms.
fixedmemoryconsumption. Duetotheissuewith
Therearetwopossiblereasonsforthat: 1).Inferiorperforcumulativesummationoperations(cumsum),premance:Thereisanotableperformancegapbetweenexisting
vious linear attention implementations cannot
linearattention-basedmodels(Katharopoulosetal.,2020;
achieve their theoretical advantage in a casual
Qin et al., 2022b) and state-of-the-art softmax attentionsetting. However, this issue can be effectively
basedmodels(Touvronetal.,2023a;b)inlanguagemodelsolvedbyutilizingdifferentattentioncalculation
ing. 2).Slowtrainingspeed: Existinglinearattentionmodstrategies to compute the different parts of atelsfrequentlystrugglewithslowtrainingspeedsduetothe
tention. Specifically, we split the attention caluseofcumulativesummationoperations(cumsum)(Hua
culation into intra-blocks and inter-blocks and
etal.,2022). Asaresult,thesemodels(Huaetal.,2022)ofuseconventionalattentioncomputationforintratenadoptconventionalattentioncomputationduringpractiblocksandlinearattentionkerneltricksforintercaluse,losingthetheoreticaladvantagesoflinearattention.
blocks. This eliminates the need for cumsum
inthelinearattentioncalculation. Furthermore, Inthispaper,weaddresstheaforementionedissuesoflinear
a tiling technique is adopted through both for- attentionandproposeanewlinearattention-basedmodel
ward and backward procedures to take full ad- thatoutperformssoftmaxattention-basedmodelsinterms
vantage of the GPU hardware. To enhance ac- ofaccuracyandefficiencyinlanguagemodeling.
curacy while preserving efficacy, we introduce
Trainingspeed. WeintroduceLightningAttention,thefirst

### TransNormerLLM(TNL),anewarchitecturethat

linearattentionimplementationthatenableslinearattention
istailoredtoourlightningattention. Weconduct
torealizeitstheoreticalcomputationalbenefits. Toachieve
rigorous testing on standard and self-collected
the linear computational complexities, the core idea is to
datasetswithvaryingmodelsizesandsequence
leveragethe"kerneltrick"toacceleratetheattentionmatrix
lengths. TNLisnotablymoreefficientthanother
computation,i.e., computetheproductofkeysandvalues
language models. In addition, benchmark refirsttocircumventthen×nquery-keymatrixmultiplication.
sults indicate that TNL performs on par with
Theslowoperationcumsumisneededduringthecalculastate-of-the-artLLMsutilizingconventionaltranstionincausallanguagemodeling. Tosolvethisdilemma,
formerstructures. Thesourcecodeisreleasedat
weapplytheconceptof"divideandconquer"toperform
github.com/OpenNLPLab/TransnormerLLM.
the calculation. Specifically, our attention calculation is
dividedintointra-blocksandinter-blocks. Theconventional
attention calculation is applied to intra-blocks, while the

## Introduction

"kerneltrick"isutilizedforinter-blocks. Wealsoleverage
tilingtechniquesinbothforwardandbackwardprocessesto
LinearattentionhasemergedasapotentiallyviablealtermaximizeGPUhardwareperformanceandtailorthetechnativetoconventionalsoftmaxattentionoverthelastfive
niqueusedinFlashAttention(Daoetal.,2022a;Dao,2023)
years(Bahdanauetal.,2016;deBrébisson&Vincent,2016).
to our Lightning Attention to make it IO-friendly. As a
1TapTap2OpenNLPLab,ShanghaiAILab.Correspondenceto: result, Lightning Attention maintains a constant training
YiranZhong<zhongyiran@gmail.com>. speedwithincreasingsequencelengthunderfixedmemory
consumption,asshowninFig.1.

### Proceedings of the 41st International Conference on Machine

Learning,Vienna,Austria.PMLR235,2024.Copyright2024by Accuracy. Astheadagegoes,agoodhorseoftenneedsa
theauthor(s).
1
4202
nuJ
02
]LC.sc[
2v18371.5042:viXra

<!-- Page 2 -->

TNLwithLightningAttention
TGS on 3B Models
8,000
7,000
6,000
5,000
4,000

## 3,000 Hgrn


## 2,000 Tnn

1,000 LLaMA-FA2

## Tnl-La

0 1024 2048 4096 8192 16384 32768
ssoL
TGS on 1B Models Loss on 1B Models Loss on 3B Models

## 0 4.0 Hgrn Hgrn

20,000

## 8 Tnn 3.8 Tnn

17,500 LLaMA-FA2 LLaMA-FA2 15,000 3.6 TNL-LA 3.6 TNL-LA
12,500 3.4 3.4
10,000 3.2 3.2

## 7,500 Hgrn 3.0 3.0


## 5,000 Tnn

2,500 LLaMA-FA2 2.8 2.8

## Tnl-La

0 1024 2048 4096 8192 16384 32768 65536 131072 2.6 0 5 10 15 20 25 30 2.6 0 5 10 15 20 25 30 B
Sequence Length Sequence Length Billion Tokens Billion Tokens
Figure1.Trainingspeedandaccuracycomparison. WecompareTNL’strainingspeedandlosseswithstate-of-the-arttransformer
models(LLaMAwithFlashAttention-2)andefficientnon-transformermodels(HGRN(Qinetal.,2023c)andTNN(Qinetal.,2023a)).
TNLachievesthelowesttraininglossesandmaintainsconsistenttrainingspeedregardlessofsequencelength.
goodspur. Weproposeanovelarchitecture,TransNormer- structure.Fourpromisingalternatives,includinglineartrans-
LLM (TNL), which is specifically designed for Light- formers,statespacemodels,longconvolution,andlinear
ningAttentioninordertoenhanceitsperformance. TNL recurrence, are being developed to replace self-attention
evolves from the previous linear attention architecture modulesforlongsequencemodeling.

### TransNormer(Qinetal.,2022a)bymakingadvancedmod-


### Linear Attention Linear attention decomposes Softmax

ifications that include positional embedding, linear atten-

### Attentionintotheinnerproductofhiddenrepresentations,

tionacceleration,gatingmechanism,tensornormalization.
allowing it to use the "Kernel Trick", where the product
Specifically,weuseLRPE(Qinetal.,2023b)togetherwith
ofkeysandvaluesiscomputedfirsttoavoidthequadratic
anexponentialdecaytoavoidattentiondilutionissueswhile
n × n matrix. Different methods utilize various hidden
allowingthemodeltoretainglobalinteractionsbetweentorepresentations. Forexample, Katharopoulosetal.(2020)
kens.Agatingmechanismisutilizedtosmoothtraining,and
use1+eluasanactivationfunction, Qinetal.(2022b)use
anewtensornormalizationschemeisproposedtoaccelerate
the cosine function to approximate the properties of softthemodelwhilepreservingitsaccuracy. Wealsoimplement
max,and Choromanskietal.(2021);Zhengetal.(2022;
anefficientmodelparallelschemaforTransNormerLLM,
2023)approximatesoftmaxthroughtheoreticalapproaches.
enablingseamlessdeploymentonlarge-scaleclustersand
AlthoughitstheoreticalcomplexityisO(nd2), theactual
facilitatingexpansiontoevenmoreextensivemodels. As
computational efficiency of linear attention becomes low
shown in Fig. 1, TNL achieves the lowest training loss
whenusedincausalattentionduetotheneedforcumsum
among the existing efficient transformer structures (Qin
operations(Huaetal.,2022). Moreover,mostlinearattenetal.,2023a;c)aswellasSOTAtransformermodels(Toution still exhibits a certain performance gap compared to
vronetal.,2023b).
traditionalTransformers(Katharopoulosetal.,2020;Liu
WeperformacomprehensiveevaluationofLightningAtten- etal.,2022).
tionacrossadiverserangeofsequencelengthstoassessits

### StateSpaceModelStateSpaceModelisbasedontheState

accuracyandcompareitscomputationalspeedandmemory

### SpaceEquationforsequencemodeling(Guetal.,2022b),

utilizationwithFlashAttention-2 (Dao,2023). Lightning
usingspecialinitialization(Guetal.,2020;2022c), diag-
Attention exhibits a notable advantage in computational
onalization assumptions (Gupta et al., 2022), and mixed
speedandmemoryconsumptioncomparedtoitscountertechniques(Daoetal.,2022b)toachieveperformancecompartswithoutcompromisingperformance. Wealsovalidate
parabletoTransformers. Duetothecharacteristicsofthe
ourmodeldesignthroughaseriesofablationsandtrainmodstatespaceequation,inferencecanbeconductedwithconelswithsizesof44M,385M,1B,7B,and15Bonstandard
stant complexity (Gu et al., 2022b), whereas the training
or our self-collected datasets. Benchmark results demonspeedcanbeslowcomparedwithFlashAttention.
stratethatTNLnotonlymatchestheperformanceofSOTA
LLMswithTransformerbutisalsosignificantlyfaster. Long Convolution Long convolution models (Qin et al.,
2023a; Fu et al., 2023) utilize a kernel size equal to the
input sequence length, facilitating a wider context com-

## RelatedWork

pared to traditional convolutions. Training these models

### EfficientLanguageModeling involvesFastFourierTransforms(FFT)algorithm,reducing

the computational complexities to O(nlogn). However,
Newefficientmodelarchitecturesarebeingexploredtoadlongconvolutionmodelsneedtocacheallhistoricalcompudressthehightimecomplexityofthetraditionaltransformer
tationsforcausalconvolutioninference,makingthemless
2

<!-- Page 3 -->


### TNLwithLightningAttention

Algorithm1LinearAttentionLeftProduct Algorithm2LinearAttentionRightProduct
Input:Q,K,V∈Rn×d. Input:Q,K,V∈Rn×d.
InitializemaskM∈Rn×n,whereM =1,ift≥s,else0. Initializekv=0∈Rd×d.
ts
LoadQ,K,MfromHBM,computeS=(QK⊤)⊙M,write fort=1,...,ndo
StoHBM. Loadq ,k ,v ∈Rd×1fromHBMtoon-chipSRAM.
t t t
LoadS,VfromHBM,computeO=SV,writeOtoHBM. Onchip,computekv=kv+k v⊤.
t t
ReturnO. Onchip,computeo =q⊤kv.
t t
Writeo⊤toHBMasthet-throwofO.
idealforprocessinglongsequencescomparedtoRNNs. t
endfor
ReturnO.

### LinearRNNLinearRNNs(Orvietoetal.,2023a;Qinetal.,

2023c),incontrast,standoutasmoresuitablereplacements O(nd2)duringinference.
for transformers in long-sequence modeling. A notable
Nevertheless,whendealingwithcausalpredictiontasks,the
exampleistheHGRN(Qinetal.,2023c)model, alinear
effectivenessoftherightproductiscompromised,leading

### RNN-basedLLMthathasshowncompetitiveperformance

to the requirement for the computation of cumsum (Hua
againstsimilarlyscaledGPTmodels.
et al., 2022). This impediment hinders the potential for
highly efficient parallel computation. In this section, we

### IO-awareAttention

show that the requirement of cumsum can be eliminated
The FlashAttention series (Dao et al., 2022a; Dao, 2023) byleveragingtheconceptof"divideandconquer"inlinear
focusesonsystem-leveloptimizationsfortheefficientim- attention calculation. For the convenience of discussion,
plementation of the standard attention operator on GPU Normwillbeignoredinthesubsequentdiscussion.
platforms. These approaches employ tiling strategies to
There are two computational approaches to handling the
minimizethevolumeofmemoryreads/writesbetweenthe
causalscenario. Oneisusingconventionalattentioncompu-
GPU’shighbandwidthmemory(HBM)andon-chipSRAM. tation(theLeftProduct),whichinvolvescomputingQK⊤
AlthoughthesemethodsoptimizetheIOcommunicationin
first. Thecompletecalculationformulaisasfollows:
attentioncalculationandarefasterthanprevioussoftmax

## O=[(Qk⊤)⊙M]V (3)

attention implementations, their theoretical computation
complexity remains O(n2d), making them unsuitable for whereM ts = 1ift ≥ s,otherwise0. Thecompletealgolongsequencelanguagemodeling. rithmisdetailedinAlgorithm1. Notethatthisalgorithmis
parallelizable,butitstimecomplexityisO(n2d). Theother
option is to compute the k v⊤ first (the Right Product),

## LightningAttention t t

whichleveragesarecursiveformulaforcomputation:

### Preliminary kv =0,kv =kv +k v⊤,o⊤ =q⊤kv . (4)

0 t t−1 t t t t t
Wefirstrecalltheformulationoflinearattentionandthen The complete algorithm is detailed in Algorithm 2. This
introduce our proposed Lightning Attention. In the case algorithm has a time complexity of O(nd2), but it is not
ofNormAttentionwithinTransNormer(Qinetal.,2022a), GPU-friendly,makingitslowerthanthefirstapproach.
attentioncomputationdeviatesfromtheconventionalTransformer structure (Vaswani et al., 2017) by eschewing the 3.2.LinearAttentionwithTiling
costlysoftmaxandscalingoperations. TheNormAttention
Weuseatilingtechniquetocomputelinearattentionina
mechanismcanbeexpressedasfollows:
causal setting. Specifically, we first divide Q,K,V into
O=Norm((QK⊤)V), (1)
twoblocksbyrows:
whereQ,K,andV ∈Rn×d arethequery,key,andvalue (cid:20) X (cid:21)

### X= 1 ,X ∈Rm×d,X ∈R(n−m)×d,

matrices,respectively,withnforsequencelengthanddfor X 1 2
2
featuredimension. Theequationcanbetransformedintoits

## X∈{Q,K,V}.

linearvariantusingrightmatrixmultiplication:
Then,byunfoldingEq.3,weget(notethatkv =0):
O=Norm(Q(K⊤V)), (2) 0
s
(cid:88)
The linear formulation enables efficient recurrent predic- kv =kv + k v⊤,s=1,...,m.
s 0 j j
tionwithO(nd2)complexityduringtraining. Additionally,
j=1
(5)
linear attention guarantees a constant computation com- s
(cid:88)
plexity of O(d2) regardless of the sequence length. This o⊤ =q⊤kv =q⊤kv +q⊤ k v⊤.
s s s s 0 s j j
isachievedbyrecurrentlyupdatingK⊤V,eliminatingthe
j=1
needforrepeatedcomputationoftheentireattentionmatrix.
Incontrast,standardsoftmaxattentionhasacomplexityof
3

<!-- Page 4 -->


### TNLwithLightningAttention

Algorithm3LightningAttentionForwardPass
𝑡 𝑸∈ℝ𝐧×𝐝
Input:Q,K,V∈Rn×d,blocksizesB.
DivideXintoT = n blocksX ,X ,...X ofsizeB ×d 𝒕 𝑲∈ℝ𝒏×𝒅

## B 1 2 T

each,whereX∈{Q,K,V,O}. 𝒕 𝑽∈ℝ𝑛×𝑑
InitializemaskM∈RB×B,whereM =1,ift≥s,else0. store in HBM
ts
InitializeKV=0∈Rd×d. C
t
o
o
p

## S

y

## R


## B


## A

lo

## M

ck
fort=1,...,T do
LoadQ ,K ,V ∈RB×dfromHBMtoon-chipSRAM.
Onchip t ,com t put t eO =[(Q K⊤)⊙M]V . 𝑶 𝒊𝒏𝒕𝒓𝒂 =(𝑸 𝒕 𝑲 𝒕 𝑻⨀𝑴)𝑽 𝒕 𝑶 𝒊𝒏𝒕𝒆𝒓 =𝑸 𝒕 ∙𝑲𝑽
intra t t t
Onchip,computeO =Q (KV). Intra block Inter block
inter t
Onchip,computeKV=KV+K⊤V .
t t 𝑶 𝒕 = 𝑶 𝒊𝒏𝒕𝒓𝒂+ 𝑶 𝒊𝒏𝒕𝒆𝒓
WriteO =O +O toHBMasthet-thblockofO.
endfor
t intra inter 𝑲𝑽=𝑲𝑽+𝑲𝒕 𝑻𝑽𝒕
on-chip SRAM
ReturnO.
Output
to HBM

### Inblockform,wehave:

O =Q kv +[(Q K⊤)⊙M]V 𝒕 𝑶∈ℝ𝑛×𝑑
1 1 0 1 1 1 store in HBM
(6)
≜Q KV +[(Q K⊤)⊙M]V . loop over 𝑛 dim
1 0 1 1 1

### The above formula shows that the forward causal linear

attentioncanbedividedintotwoparts: Figure2.StructuralframeworkofLightningAttentionisdetailedinitsalgorithmicschematic. Duringthet-thiteration,the
• Thecomputationwithintheblock[(Q K⊤)⊙M]V
1 1 1 tilingblocksofmatricesQ t ,K t ,V t aretransferredfromHigh
(intrablocks)canusetheLeftProduct;

### BandwidthMemory(HBM)toStaticRandom-AccessMemory

• The computation between blocks Q 1 KV 0 (inter (SRAM).WithintheSRAM,theoutputsO intra andO inter are
blocks)canusetheRightProduct. computedindependently,followedbyanupdatetotheKVmatrix.

### Subsequently,thefinaloutputO ,whichisthesumofO and

Itisworthnotingthatthesecondblockcanbecomputed t intra
O ,iswrittenbackfromSRAMtoHBM.
inter
usingthesameideaasfollows:
m+t
kv =kv + (cid:88) k v⊤,t=1,...,n−m, 3.3.Complexityanalysis
m+t m j j
j=m+1 Theorem3.1. ThetimecomplexityofLightningAttention
o⊤ =q⊤ kv , (7) isO(nd2+nBd)1.
m+t m+t m+t
O =Q kv +[(Q K⊤)⊙M]V
2 2 m 2 2 2
ProofofTheorem3.1. Fortheforwardpass, accordingto

## ≜Q Kv +[(Q K⊤)⊙M]V .

2 1 2 2 2 Algorithm3,eachintrapart’stimecomplexityisO(B2d),
Note that to compute the second block, we have to use each inter part’s time complexity is O(Bd2), the time
KV 1 =kv m ,whichcanbecomputedby: complexityofupdatingKV isO(Bd2),soeachthetime
(cid:88) m complexity in each loop is O(B2d + Bd2), since we

### KV =KV + k v⊤ =KV +K⊤V . (8)

1 0 m m 0 1 1 loop for T = n/B times, the total time complexity is
j=1 O((B2d + Bd2)n/B) = O(nd2 + nBd). Because the
whereKV 0 =kv 0 . Byusingtheabovestrategytodivide computationofthebackwardpassissimilartothatofthe
the matrix into multiple blocks, we obtain the Lightning forwardpass,thetimecomplexityofthebackwardpassis
Attention Forward Pass. More detailed derivation can be alsoO(nd2+nBd).
foundintheAppendixC.
Forthebackwardpropagation,accordingto(Katharopoulos 3.4.ExactIO-awareImplementation
etal.,2020),wecanrewritetheprocessas:

### LightningAttentionemploystheabovetilingmethodology

dq⊤ t =do⊤ t kv t ⊤,dk⊤ t =v t ⊤dkv t ⊤,dv⊤ t =k⊤ t dkv t , throughout its whole computation process and leverages
dkv =0∈Rd×d,dkv =dkv +q do⊤ . distinctapproachestooptimizetheutilizationofmemory
n+1 t−1 t t−1 t−1
bandwidthbetweenHBMandSRAMwithinaGPU.Specif-

### Therefore,thecalculationofthebackwardpropagationis

ically,ineachiterationt,matricesQ ,K ,V undergosegconsistentwiththeforwardEq.4,andtheLightningAtten- t t t
mentationintoblocks,subsequentlytransferredtoSRAM
tion Backward Pass can also be obtained using the tiling
forcomputation. Theintra-andinter-blockoperationsare
technique. AdetailedproofcanbefoundintheAppendixC.
segregated, with intra-blocks employing the left product
andinter-blocksutilizingtherightproduct. Thisapproach
1wechooseB ≈dinpractice,thetimecomplexityisO(nd2).
4

<!-- Page 5 -->


### TNLwithLightningAttention


### Algorithm4LightningAttentionBackwardPass


### Input:Q,K,V,dO∈Rn×d,blocksizesB. Add SGLU

DivideXintoT = n blocksX ,X ,...X ofsizeB ×d

## B 1 2 T

each,whereX∈{Q,K,V}. 𝑈 𝑉

## Sglu

Divide dX into T = n blocks dX ,dX ,...dX of size

## B 1 2 T

B×deach,whereX∈{Q,K,V,O}.
InitializemaskM∈RB×B,whereM =1,ift≥s,else0. SRMSNorm
ts
InitializeKV=0,dKV=0∈Rd×d.
fort=1,...,T do
Load K t ,V t ,O t ,dO t ∈ RB×d from HBM to on-chip Add GLA

### SRAM. SRMSNorm

Onchip,computedQ intra =[(dO t V t ⊤)⊙M]K t . *
Onchip,computedQ inter =dO t KV⊤. GLA *
Onchip,computeKV=KV+K⊤V .
t t
WritedQ t =dQ intra +dQ inter toHBMasthet-thblock 𝑈 𝑄 𝐾 𝑉
ofdQ. SRMSNorm
endfor
fort=T,...,1do
LoadQ t ,K t ,V t ,O t ,dO t ∈RB×dfromHBMtoon-chip 𝑋

## Sram.

Onchip,computedK intra =[(dO t V t ⊤)⊙M]⊤Q t . Figure3.Architecture overview of TransNormerLLM (TNL).
Onchip,computedK inter =V t dKV⊤. EachtransformerblockiscomposedofaGatedLinearAttention
Onchip,computedV intra =[(Q t K⊤ t )⊙M]⊤dO t . (GLA)fortokenmixingandaSimpleGatedLinearUnit(SGLU)
Onchip,computedV inter =K t dKV. forchannelmixing.WeapplyPre-normforbothmodules.
Onchip,computedKV=dKV+Q⊤dO .
t t
Write dK = dK + dK ,dV = dV +
t intra inter t intra
dV toHBMasthet-thblockofdK,dV. coding,gatingmechanisms,andtensornormalization.
inter
endfor
PositionEncodingInTransNormer,DiagAttentionisused
ReturndQ,dK,dV.
atthelowerlayerstoavoiddilutionissues. However,this
optimallyexploitsthecomputationalandmemoryefficien- leadstoalackofglobalinteractionbetweentokens.InTNL,
cies associated with the right product, enhancing overall we leverage LRPE (Qin et al., 2023b) with exponential
executionspeed. TheintermediateactivationKVisitera- decay (Press et al., 2022; Qin et al., 2023a; Peng et al.,
tivelysavedandaccumulatedwithinSRAM.Subsequently, 2023b)toaddressthisissue,retainingfullattentionatthe
the outputs of intra-blocks and inter-blocks are summed lowerlayers. Theexpressionofourpositionencodingisas
withinSRAM,andtheresultsarewrittenbacktoHBM.The follows:
structureofLightningAttentionisillustratedinFig.2. The a ts =q⊤ t k s λt−sexpiθ(t−s). (9)
intricatedetailsoftheLightningAttentionimplementation whichwecallLRPE-d-LinearizedRelativePositionalEnareexplainedthroughAlgorithm3fortheforwardpassand codingwithexponentialdecay.SimilartotheoriginalLRPE,
Algorithm4forthebackwardpass. wesetθtobelearnable. Weempiricallyfindthatratherthan
applyingLRPE-dtoeverylayer,applyingittothefirstlayer
andkeepingotherlayerswithexponentialdecaycanspeed

## TransNormerLLM

uptrainingbyapproximately15-20%butonlywithasubtle

### TheOverallStructure effectontheperformance.

OurstructureisbasedonthefindingsofTransNormer(Qin Note that this position encoding is fully compatible with
etal.,2022a)buthascustommodificationstobalanceeffi- LinearAttention,asitcanbedecomposedwithrespecttos
ciencyandperformance. Weillustratetheoverallstructure andtseparately. Thevalueofλfortheh-thheadinthel-th
inFig.3. TheinputXisupdatedthroughtwoconsecutive layer(assumingthereareatotalofH headsandLlayers)
steps: 1). ItundergoesGatedLinearAttention(GLA)with isgivenby:
theapplicationofSimpleRMSNorm(SRMSNorm)normal- λ=exp (cid:0) −8h × (cid:0) 1− l(cid:1)(cid:1) . (10)

## H L

ization. 2). ItgoesthroughtheSimpleGatedLinearUnit
Here, 8h corresponds to the decay rate of the h-th head,
(SGLU) with SRMSNorm normalization. We apply the H
while
(cid:0)
1−
l(cid:1)
corresponds to the decay rate of the l-th
Pre-normforbothmodules. L
layer. The term
(cid:0)
1−
l(cid:1)
ensures that the Theoretical Re-

## L

ceptiveFields(TRF)(Qinetal.,2024)atthelowerlayers

### CustomModification

issmallercomparedtothehigherlayers,whichalignswith
Inthissection,weoutlinethekeydesignsandinspiration TransNormer’smotivation.Wechooseλtobenon-learnable
behindeachcustommodification,includingpositionalen- sinceweempiricallyfoundthatgradientsbecomeunstable
5

<!-- Page 6 -->


### TNLwithLightningAttention

whenλislearnable,leadingtoNaNvalues. Notethatthis Table1.ResultsonWikitext-103(TNN(Qinetal.,2023a)’ssetpositionalencodingisstillcompatiblewithLightningAtten- ting).↓meanslowerisbetter.
tion,withthespecificalgorithmdetailedinAppendixAB. PPL PPL Params

### Model

(val)↓ (test)↓ (M)
GatingMechanismGatecanenhancetheperformanceof

### Transformer 24.40 24.78 44.65

the model and smooth the training process. In TNL, we FLASH 25.92 26.70 42.17
adopttheapproachfromFlash(Huaetal.,2022)anduse 1+elu 27.44 28.05 44.65
GatedLinearAttention(GLA)intokenmixing: Attn-based Performer 62.50 63.16 44.65
cosFormer 26.53 27.06 44.65
O=Norm(QK⊤V)⊙U,Q=ϕ(XW ),
q TN1 24.43 25.00 44.64
(11)
K=ϕ(XW ),V=XW ,U=XW . TN2 24.50 25.05 44.64
k v u

### Syn(D) 31.31 32.43 46.75

WechooseϕtobeSwish(Ramachandranetal.,2017)ac-

### MLP-based Syn(R) 33.68 34.78 44.65

tivationfunctionasweempiricallyfindthatitoutperforms gMLP 28.08 29.13 47.83
otheractivationfunctions. S4 38.34 39.66 45.69

## Dss 39.39 41.07 45.73

Tofurtheracceleratethemodel,weproposeSimpleGLU GSS 29.61 30.74 43.84

### RNN-based

(SGLU), which removes the activation function from the RWKV 24.31 25.07 46.23
originalGLUstructureasthegateitselfcanintroducenon- LRU 29.86 31.12 46.24

## Hgrn 24.14 24.82 46.25

linearity. Therefore,ourchannelmixingbecomes:

### FFT-based TNN 23.98 24.67 48.68

O=[V⊙U]W o ,V=XW v ,U=XW u . (12) Ours TNL 23.46 24.03 45.45

### Weempiricallyfindthatnotusinganactivationfunctionin

GLUwillnotleadtoanyperformanceloss. mentation(namedVanilla)andourLightningAttention. As
areference,wehavealsoincludedFlashAttention-2(Dao,

### Tensor Normalization The origin NormAttention intro-

2023) (named Flash2), which is currently the SOTA imducedinTransNormer(Qinetal.,2022a)isasfollows:
plementation of softmax attention. As shown in Fig. 4,

### O=Norm(QK⊤V) (13)


### LightningAttentionshowsremarkablelineargrowthofpro-

In TransNormerLLM, we replace the origin RMSNorm cessingtimeinbothforwardandbackwardpasses,whereas
with a new simple normalization function called Sim- Vanilla and Flash2 exhibit quadratic growth. In terms of
pleRMSNorm,abbreviatedasSRMSNorm: memoryfootprint,Vanillatendstorapidlyexhaustmemory
SRMSNorm(x)= x√ . (14) resources. Lightning Attention shows a similar trend to
∥x∥2/ d
Flash2butrequireslessmemory.
WeempiricallyfindthatusingSRMSNormdoesnotleadto
anyperformanceloss.

### TNLEvaluation


## Experiments PerformanceEvaluationInTable1,wepresentanevaluationacrossvarious40Mmodelsonastandarddataset. This

We carried out thorough experiments on TNL models includesmodelsbasedonattention/linearattentionmechaand lightning attention. We implemented our models nisms(Vaswanietal.,2017;Daoetal.,2022a;Katharopouon the Metaseq framework (Zhang et al., 2022) with Py- los et al., 2020; Qin et al., 2022b;a), MLPs (Multi-Layer
torch (Paszke et al., 2019). The Lightning Attention was Perceptrons)(Tayetal.,2021;Liuetal.,2021),RNNs(ReexecutedthroughTriton(Tilletetal.,2019). Alltheexper- current Neural Networks) (Gu et al., 2022a; Gupta et al.,
imentswereconductedonA10080GGPUclusters. The 2022;Mehtaetal.,2022;Pengetal.,2023b;Orvietoetal.,
assessmentofourworkisdividedintothreemainsections: 2023b),FFTs(FastFourierTransforms)(Qinetal.,2023a),
I)WeevaluatedtheefficiencyandaccuracyoftheLightning andourmodel. TNLrecordsthelowestperplexityontest
Attention module; II) We further benchmarked our TNL setaftertrainedontheWikitext-103dataset.
models’performanceonstandardsmall-scalecorpusand
We also scaled up our model to 1B and 3B parameters

### LLMbenchmarksandcomparedtheirtrainingandinference

andcompareditstraininglosswithtop-tierLLMstructures
speedswithSTOAmodels;III)Wealsoprovideanablation
suchasLLaMA-FA2(Touvronetal.,2023a;Dao,2023),
studyonthedesignofTNL.
HGRN(Qinetal.,2023c),andTNN(Qinetal.,2023a). For
afaircomparison,weretrainallmodelsonthesame30B

### LightningAttentionEvaluation

corpusandplotthetraininglossesinFig.1. TNLachieved
SinceourLightningAttentionisanexactimplementationof thelowesttraininglossesinboth1Band3Bparameters.
normlinearattention(Qinetal.,2022a),wecomparedthe
Efficiency Evaluation In Fig. 1, we present a comparaspeedandmemoryusagebetweenitsoriginalpytorchimpletiveanalysisoftrainingspeedsunderthesamecorporaand
6

<!-- Page 7 -->


### TNLwithLightningAttention

Forward Pass Backward Pass Forward Memory Footprint Backward Memory Footprint
1 1 1 2 , , , , 4 6 8 0 0 0 0 0 0 0 0 0 V F L l i a a g n s h i h t ll n 2 a ing 1 1 1 2 , , , , 4 6 8 0 0 0 0 0 0 0 0 0 V F L l i a a g n s h i h t ll n 2 a ing 1 1 1 2 4 6 8 0 V F L l i a a g n s h i h t ll n 2 a ing 3 4 4 5 5 0 5 0 V F L l i a a g n s h i h t ll n 2 a ing 1,200 1,200 12 30
1,000 1,000 10 25
800 800 8 20
600 600 6 15
400 400 4 10
200 200 2 5
0 0 0 0
1024 2048 4096 8192 16384 32768 65536 131072 1024 2048 4096 8192 16384 32768 65536 131072 1024 2048 4096 8192 16384 32768 65536 131072 1024 2048 4096 8192 16384 32768 65536 131072
)sm(
emitnuR
)BG( tnirptooF
yromeM
Sequence Length Sequence Length Sequence Length Sequence Length
Figure4.ComparativeAnalysisofSpeedandMemoryUsage:Vanillarepresentsnormlinearattentioninpytorch(Qinetal.,2022a),
Flash2representsFlashAttention-2.Lefttwosub-figures:Runtimeinmillisecondsfortheforwardandbackwardpassacrossvarying
sequencelengths.Righttwosub-figures:Memoryutilization(inGB)duringtheforwardandbackwardpassatdifferentsequencelengths.
Inference Throughput on 7B Models
3000.0 2819.6
2500.0
2000.0
1500.0
1000.0 967.17 961.93
500.0 506.77 455.36 537.8 537.97
252.12
0.0
)s/nekoT(
tuphguorhT
selectedseveralopen-sourcemodelsascompetitors,includingTransformer-basedmodelssuchasOPT(Zhangetal.,
2022),Pythia(Bidermanetal.,2023),BLOOM(Workshop
et al., 2023), GPT-Neo (Black et al., 2022), Falcon (Almazroueietal.,2023),LLaMA(Touvronetal.,2023a;b),

### OpenLLAMA (Geng&Liu,2023),Baichuan(Baichuan,

2023),ChatGLM(Zengetal.,2022;Duetal.,2022),and
non-TransformermodelRWKV(Pengetal.,2023a). Itcan
beobservedinTable2andTable3that,comparedtothese
Pythia Baichuan Baichuan2 LLaMA LLaMA2 ChatGLM2ChatGLM3 TNL models,TNLremainshighlycompetitive.

## 9B 7B 7B 7B 7B 6B 6B 7B

• WereportBoolQ(Clarketal.,2019),PIQA(Bisketal.,

### Figure5.InferenceThroughputComparison.Wemeasurethe

inferencethroughputofvarious7BLLMmodelsonaA10080G 2019), SIQA (Sap et al., 2019), HellaSwag (Zellers
GPU.BatchsizesformodelsarechosentooptimizeGPUutiliza- et al., 2019), WinoGrande (Sakaguchi et al., 2019),
tionwithoutexceedingmemorylimits.Eachmodelistestedwith ARCeasyandchallenge(Clarketal.,2018)andOpena512-tokeninputpromptandcangenerateupto1024newtokens. BookQA(Mihaylovetal.,2018). Wereport0-shotre-
Reportedthroughputisaveragedfrom20attempts. sultsforallbenchmarksusingLM-Eval-Harness(Gao
etal.,2021).Allofourmodelsachievecompetitiveperhardwaresetups. Thiscomparisonencompassesfourvariformancecomparedtoexistingstate-of-the-artLLMs,
ants:TNL,LLaMA-FA2(Touvronetal.,2023a;Dao,2023),
showcasingaremarkableabilitytocomprehendand
HGRN(Qinetal.,2023c) , andTNN (Qin etal.,2023a).
applycommonsensereasoning.
Ourfindingsshowthatduringboththeforwardandback-
• WereporttheoverallresultsforMMLU(Hendrycks
wardpasses,theTGS(tokensperGPUpersecond)forTNL
et al., 2021), C-Eval (Huang et al., 2023). Official
remainsconsistentlyhigh,whiletheotherthreemodelsexscriptswereusedforevaluatingMMLUandC-Eval,
hibitarapiddeclinewhensequencelengthisscaledfrom
with all evaluation results being conducted with a 5-
1Kto128K.ThispatternsuggeststhatLightningAttention
shotsetup. Incomparisontotop-tieropen-sourcemodoffers a significant advancement in managing extremely
elsavailableintheindustry,ourmodelshavedemonlongsequencelengthsinLLM.
stratedmatchedperformanceinbothEnglishandChi-
InferenceEvaluationWeconductaninferencethroughput nesebenchmarks.
comparisononvarious7Blargelanguagemodelsusingtheir • OnSCROLLS(Shahametal.,2022)benchmark,we
standardcodebasefromHuggingface,asdetailedinFig.5. assessthelargelanguagemodelstrainedona1billion
TNLwithLightningAttentiondemonstratesasignificant parameterandpre-trainedusingasequencelengthof
advantage,achievingathroughputratethatupto11×higher 2048. Wepresentzero-shotperformanceresultsforall
thantransformerstructuremodels. benchmarks using the LM-Eval-Harness (Gao et al.,
2021). For generation tasks within SCROLLS, we
BenchmarkResultsInordertovalidatetheeffectiveness
employagreedysearchwithhyper-parameterstop_k
of TNL, we pretraining 385M, 1B, 7B, and 15B models
set to 5 and top_p set to 1. Our models consistently
onself-collecteddatasets,thedetailsofthedataareinthe
matchorsurpasstheperformanceofexistingstate-of-
AppendixD,andtestedonCommonsenseReasoningTask,
the-artLLMsinthesetasks.
MMLU(Hendrycksetal.,2021),C-Eval(Huangetal.,2023),
andSCROLLS(Shahametal.,2022). Forcomparison,we
7

<!-- Page 8 -->


### TNLwithLightningAttention

Table2.PerformanceComparisononCommonsenseReasoningandAggregatedBenchmarks. Forafaircomparison,wereport
competingmethods’resultsreproducedbyususingtheirreleasedmodels. Officialresultsaredenotedinitalics. PS:parametersize
(billion).T:tokens(billion).HS:HellaSwag.WG:WinoGrande.

### Model PS T BoolQ PIQA HS WG ARC-e ARC-c OBQA MMLU C-Eval

B B acc acc acc_norm acc acc acc_norm acc_norm acc-5shot acc-5shot
OPT 0.35 0.30 57.74 64.58 36.69 52.49 44.02 23.89 28.20 26.02 25.71
Pythia 0.40 0.30 60.40 67.08 40.52 53.59 51.81 24.15 29.40 25.99 24.81

### Rwkv 0.43 - - 67.52 40.90 51.14 52.86 25.17 32.40 24.85 -

TNL 0.39 1.0 62.14 66.70 46.27 54.46 55.43 27.99 32.40 25.90 25.24
OPT 1.3 0.3 57.77 71.71 53.70 59.35 57.24 29.69 33.20 24.96 25.32
Pythia 1.4 0.3 60.73 70.67 47.18 53.51 56.99 26.88 31.40 26.55 24.25

### Rwkv 1.5 - - 72.36 52.48 54.62 60.48 29.44 34.00 25.77 -

Falcon 1.0 0.35 61.38 75.14 61.50 60.30 63.38 32.17 35.60 25.28 25.66
TNL 1.0 1.2 63.27 72.09 56.49 60.38 63.68 35.24 36.60 27.10 26.01
OPT 6.7 0.3 66.18 76.22 67.21 65.19 65.66 34.64 37.20 24.57 25.32
Pythia 6.9 0.3 63.46 75.14 63.92 60.77 67.34 35.41 37.00 24.64 26.40

### Rwkv 7.4 - - 76.06 65.51 61.01 67.80 37.46 40.20 24.96 -

Falcon 7.2 1.5 73.73 79.38 76.3 67.17 74.62 43.60 43.80 27.79 22.92
Baichuan2 7.0 2.6 72.72 76.50 72.17 68.35 75.17 42.32 39.60 54.16 54.00
ChatGLM2 7.1 1.4 77.65 69.37 50.51 57.62 59.13 34.30 37.00 45.46 52.55
OpenLLaMAv2 6.7 1.0 72.20 78.84 74.51 65.67 72.39 41.30 41.00 41.29 30.01
LLaMA1 6.7 1.0 76.50 79.80 76.10 70.10 72.80 47.60 57.20 35.10 25.72
LLaMA2 6.7 2.0 77.68 78.07 76.02 68.98 76.30 46.33 44.20 45.30 33.20
TNL 6.8 1.4 75.87 80.09 75.21 66.06 75.42 44.40 63.40 43.10 43.18
OPT 13 0.3 65.93 75.84 69.83 65.19 67.00 35.75 38.80 24.68 22.23
Pythia 12 0.3 65.72 76.17 68.85 66.22 70.62 38.23 41.00 25.51 22.99
RWKV 14 - 70.12 78.51 71.49 64.48 72.35 40.87 41.00 26.49 26.49
Baichuan2 13 2.6 79.20 77.31 75.27 70.01 77.36 47.01 43.80 57.02 59.63
OpenLLaMAv2 13 1.0 72.29 77.58 72.07 70.09 75.42 43.86 43.00 43.43 25.95
LLaMA1 13 1.0 77.95 79.16 79.06 72.61 77.40 47.70 44.80 47.62 32.13
LLaMA2 13 2.0 80.61 79.11 79.35 72.38 79.34 48.98 35.20 55.70 38.34
TNL 15 2.0 76.64 81.56 82.18 75.61 77.61 50.51 46.40 60.06 53.01

### TNLAblation


### Table5.Ablationsondecaytemperature.Theresultsofdecay

We conducted an extensive ablation analysis on various
temperatureprovedtobesuperior.
componentsofTNL,includingpositionalencoding,gating
mechanisms, GLA activation functions, GLU activation Temperature Params Updates Loss PPL
w/temperature 385M 100K 2.248 4.770
functions,andnormalizationfunctions.
w/otemperature 385M 100K 2.258 4.804

### Table4.ExplorationofPositionalEncoding. LRPE-dleadsto

themostoptimaloutcome. We also perform ablations on the decay temperature
(cid:0)
1−
l(cid:1)
inEq.10. TheperplexityoftheTNLisreduced

### PEMethods Params Updates Loss PPL L

Mix 385M 100K 2.248 4.770 byaddingthedecaytemperature,asshowninTable5.

## Ape 386M 100K 2.387 5.253

Exp-Decay 385M 100K 2.267 4.834 Table6.Ablationsongatingmechanism.Theperformancewith

## Lrpe 385M 100K 2.287 4.899

thegateprovedtobesuperior.
LRPE-d 385M 100K 2.236 4.728
Gate Params Updates Loss PPL
w/gate 385M 100K 2.248 4.770
w/ogate 379M 100K 2.263 4.820
PositionalEncoding: inourexperimentcomparingvarious

### PEstrategies—Mix,AbsolutePositionalEncoding(APE),

LRPE,ExponentialDecay,andLRPE-d—ourapproachand GatingMechanism: wefurtherinvestigatetheimpactof
LRPE-ddemonstratedsuperiorperformance. Wechosethe integrating a gating mechanism. According to the data
Mixmethodforitsabilitytoenhancetrainingspeedbyup presentedinTable6,enablingthegatedecreasedtheloss
to20%,despitebeingslightlylesseffectivethanLRPE-d. valuefrom2.263to2.248.
8

<!-- Page 9 -->


### TNLwithLightningAttention

Table3.PerformanceComparisononSCROLLS(Shahametal.,2022): Areviewofmodelsupto1billionparameterson2048
pre-trainingsequencelength.PS:parametersize(billion).T:tokens(billion).
Model PS T GovRep SumScr QMSum Qspr Nrtv QALT CNLI Avg

## B B Rouge-1/2/L Rouge-1/2/L Rouge-1/2/L F1 F1 Em Em

OPT 0.35 0.30 2.52/0.53/2.24 7.72/0.68/6.52 8.05/1.79/6.6 13.13 10.13 29.05 9.16 7.55
Pythia 0.40 0.30 4.96/1.19/4.06 2.03/0.2/1.79 7.51/1.43/6.08 15.27 8.24 28.57 15.24 7.43
RWKV 0.43 - 1.63/0.4/1.49 0.94/0.11/0.76 10.19/2.26/8.06 13.16 9.76 26.32 16.49 7.04
TNL 0.39 1.0 3.67/1.16/3.14 8.27/0.82/6.91 13.62/3.29/10.95 14.29 11.69 28.14 17.36 9.48
OPT 1.3 0.3 5.7/2.09/4.41 10.17/0.82/8.29 12.36/3.15/9.85 18.37 13.42 29.15 12.44 10.02
Pythia 1.4 0.3 4.03/1.25/3.33 8.34/0.87/6.97 13.17/3.4/10.92 16.09 11.91 28.72 9.06 9.08
Falcon 1.0 0.35 2.74/0.67/2.37 10.95/1.28/8.66 13.29/3.09/10.58 16.17 12.91 29.19 14.75 9.74
TNL 1.0 1.2 6.81/2.30/5.25 12.28/1.23/9.27 14.60/3.51/11.62 15.02 14.66 28.72 37.32 12.51
Table7.ExplorationofNormalizationFunction.Thedeviation 6.Conclusion
inresultsamongthebellowingnormalizationfunctionsisminimal.

### WeintroducedLightningAttention,thefirstlinearattention

NormType Params Updates Loss PPL implementationthatunleashedthefullpoweroflinearat-

### SRMSNorm 385M 100K 2.248 4.770

tention. As a result, our Lightning Attention can handle

### RMSNorm 385M 100K 2.247 4.766

varioussequencelengthswithaconstantspeedunderacon-

### LayerNorm 385M 100K 2.247 4.765

stantmemoryfootprint. Themainconceptistodividethe
calculationofattentionintointro-blocksandinter-blocks,
NormalizationFunctions: ourstudyinvolvedtestingvarwhileapplyingdistinctcomputationtechniquestoperform
iousnormalizationtechniques—SRMSNorm,RMSNorm,
thecalculation. Anewarchitecture,TNL,thatistailoredfor
andLayerNorm—onTNL,findinglittledifferenceintheir
LightningAttentionispresented. TNLoutperformsexisting
effectiveness. However, we enhanced SRMSNorm using
efficientlanguagemodelsintermsofbothefficiencyand
Triton, resulting in notable improvements in processing
accuracyandachievescompetitiveperformancecompared
speedforlargerdimensions.
tostate-of-the-artlargelanguagemodelsusingconventional
transformerarchitectures.

### GLA Activation Functions: in our study on the GLA

(GatedLinearAttention)mechanism,weevaluatedactivationfunctions,findingSwishand1+elutoperformsimilarly, Acknowledgement
asdetailedinTable 8. However,duetoNaNissueswith
1+eluinour7Bmodel,weoptedforSwish. This work is partially supported by the National Key

### R&DProgramofChina(NO.2022ZD0160100). Wethank

Table8.AblationsonGLAactivationfunctions.Theresultsob- SonglinYangforthehelpfuldiscussions.
tainedfromdifferentactivationfunctionswerevirtuallyidentical.

### GLAAct Params Updates Loss PPL

Swish 385M 100K 2.248 4.770 ImpactStatement

### NoAct 385M 100K 2.283 4.882

1+elu 385M 100K 2.252 4.767 TheintroductionofLightningAttentionanditsaccompanyingarchitectureTNL,heraldssignificantshiftsinmachine
learning,particularlyinlanguagemodelefficiencyandac-

### GLUActivationFunctions: ourexperimentadditionally

cessibility. By addressing the limitations of linear atteninvolvedremovingtheactivationfunctionfromtheGated
tioninvaryingsequencelengthswithoutincreasingmem-

### LinearUnits(GLU),showingminimaleffectonoutcomes

oryconsumption,thisadvancementdemocratizesaccessto
asperTable9. Therefore,weoptedfortheSimpleGated
state-of-the-artlanguagemodels,potentiallyreducingthe
LinearUnits(SGLU)configurationinourmodel.
computationaland environmentalfootprint oflarge-scale

### AIsystems. Ethically,itunderscoresamovetowardsmore


### Table9.AblationsonGLUactivationfunctions.Theexclusion

oftheactivationfunctionhadnonegativeimpactontheresults. sustainableAIpractices,yetraisesquestionsabouttheproliferation of powerful language models and their societal

### GLUAct Params Updates Loss PPL

impacts,includingconcernsoverprivacy,misinformation,

### NoAct 385M 100K 2.248 4.770

Swish 385M 100K 2.254 4.788 andthedigitaldivide.
9

<!-- Page 10 -->


### TNLwithLightningAttention

References Dao, T., Fu, D. Y., Saab, K. K., Thomas, A. W.,

### Rudra, A., and Ré, C. Hungry hungry hippos: To-

Almazrouei,E.,Alobeidli,H.,Alshamsi,A.,Cappelli,A.,
wards language modeling with state space models.

### Cojocaru,R.,Debbah,M.,Goffinet,E.,Heslow,D.,Lau-

CoRR, abs/2212.14052, 2022b. doi: 10.48550/arXiv.
nay, J., Malartic, Q., et al. Falcon-40b: an open large

### URLhttps://doi.org/10.48550/

languagemodelwithstate-of-the-artperformance. TecharXiv.2212.14052.
nical report, Technical report, Technology Innovation
Institute,2023. deBrébisson,A.andVincent,P. Acheaplinearattention
mechanismwithfastlookupsandfixed-sizerepresenta-
Bahdanau, D., Cho, K., and Bengio, Y. Neural machine tions,2016.
translationbyjointlylearningtoalignandtranslate,2016.

### Du,Z.,Qian,Y.,Liu,X.,Ding,M.,Qiu,J.,Yang,Z.,and

Baichuan. Baichuan2: Openlarge-scalelanguagemodels. Tang,J. Glm: Generallanguagemodelpretrainingwith
arXivpreprintarXiv:2309.10305,2023. URLhttps: autoregressiveblankinfilling,2022.
//arxiv.org/abs/2309.10305.
Fu, D. Y., Epstein, E. L., Nguyen, E., Thomas, A. W.,

### Zhang, M., Dao, T., Rudra, A., and Ré, C. Simple

Biderman, S., Schoelkopf, H., Anthony, Q., Bradley, H.,
hardware-efficientlongconvolutionsforsequencemodel-
O’Brien, K., Hallahan, E., Khan, M. A., Purohit, S.,
ing. CoRR,abs/2302.06646,2023. doi: 10.48550/arXiv.
Prashanth, U. S., Raff, E., Skowron, A., Sutawika, L.,

### URLhttps://doi.org/10.48550/

andvanderWal,O. Pythia: Asuiteforanalyzinglarge
arXiv.2302.06646.
languagemodelsacrosstrainingandscaling,2023.

### Gao,L.,Tow,J.,Biderman,S.,Black,S.,DiPofi,A.,Foster,

Bisk, Y., Zellers, R., Bras, R. L., Gao, J., and Choi, Y.
C., Golding, L., Hsu, J., McDonell, K., Muennighoff,

### Piqa: Reasoningaboutphysicalcommonsenseinnatural

N., et al. A framework for few-shot language model
language,2019.
evaluation. Versionv0.0.1.Sept,2021.
Black, S., Biderman, S., Hallahan, E., Anthony, Q., Gao, Geng, X. and Liu, H. Openllama: An open repro-
L.,Golding,L.,He,H.,Leahy,C.,McDonell,K.,Phang, duction of llama. URL: https://github. com/openlm-
J.,etal. Gpt-neox-20b: Anopen-sourceautoregressive research/open_llama,2023.
languagemodel. arXivpreprintarXiv:2204.06745,2022.

### Gu,A.,Dao,T.,Ermon,S.,Rudra,A.,andRe,C. Hippo:

Choromanski,K.M.,Likhosherstov,V.,Dohan,D.,Song, Recurrentmemorywithoptimalpolynomialprojections,
X.,Gane,A.,Sarlos,T.,Hawkins,P.,Davis,J.Q.,Mo- 2020.
hiuddin,A.,Kaiser,L.,Belanger,D.B.,Colwell,L.J.,
Gu,A.,Goel,K.,andRé,C. EfficientlymodelinglongseandWeller,A. Rethinkingattentionwithperformers. In
quenceswithstructuredstatespaces.InTheInternational
InternationalConferenceonLearningRepresentations,
ConferenceonLearningRepresentations(ICLR),2022a.

## URLhttps://openreview.net/forum?

id=Ua6zuk0WRH. Gu, A., Goel, K., and Ré, C. Efficiently modeling long
sequences with structured state spaces. In The Tenth
Clark,C.,Lee,K.,Chang,M.-W.,Kwiatkowski,T.,Collins, InternationalConferenceonLearningRepresentations,
M.,andToutanova,K. Boolq: Exploringthesurprising ICLR2022,VirtualEvent,April25-29,2022.OpenRedifficultyofnaturalyes/noquestions,2019. view.net,2022b.URLhttps://openreview.net/
forum?id=uYLFoz1vlAC.

### Clark,P.,Cowhey,I.,Etzioni,O.,Khot,T.,Sabharwal,A.,

Schoenick, C., andTafjord, O. Thinkyouhavesolved Gu,A.,Gupta,A.,Goel,K.,andRé,C. Ontheparameteriquestionanswering? tryarc,theai2reasoningchallenge, zationandinitializationofdiagonalstatespacemodels,
2018. 2022c.

### Gupta,A.,Gu,A.,andBerant,J. Diagonalstatespacesare

Dao, T. Flashattention-2: Faster attention with betaseffectiveasstructuredstatespaces,2022.
ter parallelism and work partitioning. arXiv preprint
arXiv:2307.08691,2023.
Hendrycks,D.,Burns,C.,Basart,S.,Zou,A.,Mazeika,M.,

### Song,D.,andSteinhardt,J. Measuringmassivemultitask

Dao,T.,Fu,D.Y.,Ermon,S.,Rudra,A.,andRé,C.FlashAtlanguageunderstanding,2021.
tention: Fastandmemory-efficientexactattentionwith
IO-awareness. InAdvancesinNeuralInformationPro- Hua,W.,Dai,Z.,Liu,H.,andLe,Q.V. Transformerquality
cessingSystems,2022a. inlineartime. arXivpreprintarXiv:2202.10447,2022.
10

<!-- Page 11 -->


### TNLwithLightningAttention

Huang,Y.,Bai,Y.,Zhu,Z.,Zhang,J.,Zhang,J.,Su,T.,Liu, Peng,B.,Alcaide,E.,Anthony,Q.,Albalak,A.,Arcadinho,
J.,Lv,C.,Zhang,Y.,Lei,J.,Fu,Y.,Sun,M.,andHe,J. S.,Cao,H.,Cheng,X.,Chung,M.,Grella,M.,GV,K.K.,
C-eval: Amulti-levelmulti-disciplinechineseevaluation He,X.,Hou,H.,Kazienko,P.,Kocon,J.,Kong,J.,Kopsuiteforfoundationmodels,2023. tyra, B., Lau, H., Mantri, K. S. I., Mom, F., Saito, A.,

### Tang,X.,Wang,B.,Wind,J.S.,Wozniak,S.,Zhang,R.,

Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C.,
Zhang, Z., Zhao, Q., Zhou, P., Zhu, J., and Zhu, R.-J.

### Chaplot,D.S.,delasCasas,D.,Bressand,F.,Lengyel,

Rwkv: Reinventingrnnsforthetransformerera,2023a.

### G.,Lample,G.,Saulnier,L.,Lavaud,L.R.,Lachaux,M.-

A.,Stock,P.,Scao,T.L.,Lavril,T.,Wang,T.,Lacroix, Peng,B.,Alcaide,E.,Anthony,Q.,Albalak,A.,Arcadinho,
T.,andSayed,W.E. Mistral7b,2023. S.,Cao,H.,Cheng,X.,Chung,M.,Grella,M.,GV,K.K.,

### He,X.,Hou,H.,Kazienko,P.,Kocon,J.,Kong,J.,Kop-


### Kalamkar, D., Mudigere, D., Mellempudi, N., Das, D.,

tyra, B., Lau, H., Mantri, K. S. I., Mom, F., Saito, A.,
Banerjee, K., Avancha, S., Vooturi, D. T., Jammala-

### Tang,X.,Wang,B.,Wind,J.S.,Wozniak,S.,Zhang,R.,

madaka, N., Huang, J., Yuen, H., et al. A study of
Zhang, Z., Zhao, Q., Zhou, P., Zhu, J., and Zhu, R.-J.
bfloat16 for deep learning training. arXiv preprint
Rwkv: Reinventingrnnsforthetransformerera,2023b.
arXiv:1905.12322,2019.

### Press,O.,Smith,N.,andLewis,M. Trainshort,testlong:

Katharopoulos, A., Vyas, A., Pappas, N., and Fleuret, F.
Attentionwithlinearbiasesenablesinputlengthextrapo-

### Transformersarernns: Fastautoregressivetransformers

lation.InInternationalConferenceonLearningRepresenwith linear attention. In International Conference on
tations, 2022. URL https://openreview.net/
MachineLearning,pp.5156–5165.PMLR,2020.
forum?id=R8sQPpGCv0.
Liu,H.,Dai,Z.,So,D.,andLe,Q.V. Payattentiontomlps.
Qin, Z., Han, X., Sun, W., Li, D., Kong, L., Barnes, N.,
AdvancesinNeuralInformationProcessingSystems,34:
andZhong, Y. Thedevilinlineartransformer. InPro-
9204–9215,2021.
ceedingsofthe2022ConferenceonEmpiricalMethods
Liu,Z.,Li,D.,Lu,K.,Qin,Z.,Sun,W.,Xu,J.,andZhong, in Natural Language Processing, pp. 7025–7041, Abu
Y. Neuralarchitecturesearchonefficienttransformers Dhabi,UnitedArabEmirates,December2022a.Associandbeyond. arXivpreprintarXiv:2207.13955,2022. ationforComputationalLinguistics. URLhttps://
aclanthology.org/2022.emnlp-main.473.
Mehta, H., Gupta, A., Cutkosky, A., and Neyshabur, B.
Long range language modeling via gated state spaces. Qin, Z., Sun, W., Deng, H., Li, D., Wei, Y., Lv, B.,
arXivpreprintarXiv:2206.13947,2022. Yan, J., Kong, L., and Zhong, Y. cosformer: Rethinking softmax in attention. In International Conference
Micikevicius,P.,Narang,S.,Alben,J.,Diamos,G.,Elsen, on Learning Representations, 2022b. URL https:
E.,Garcia,D.,Ginsburg,B.,Houston,M.,Kuchaiev,O., //openreview.net/forum?id=Bl8CQrx2Up4.

### Venkatesh, G., et al. Mixed precision training. arXiv

preprintarXiv:1710.03740,2017. Qin, Z., Han, X., Sun, W., He, B., Li, D., Li, D., Dai, Y.,

### Kong,L.,andZhong,Y. Toeplitzneuralnetworkforse-

Mihaylov,T.,Clark,P.,Khot,T.,andSabharwal,A. Cana quencemodeling. InTheEleventhInternationalConfersuitofarmorconductelectricity? anewdatasetforopen enceonLearningRepresentations,2023a. URLhttps:
bookquestionanswering,2018. //openreview.net/forum?id=IxmWsm4xrua.
Orvieto,A.,Smith,S.L.,Gu,A.,Fernando,A.,Gulcehre, Qin,Z.,Sun,W.,Lu,K.,Deng,H.,Li,D.,Han,X.,Dai,Y.,
C.,Pascanu,R.,andDe,S. Resurrectingrecurrentneural Kong,L.,andZhong,Y. Linearizedrelativepositional
networksforlongsequences,2023a. encoding. TransactionsonMachineLearningResearch,
2023b.

### Orvieto,A.,Smith,S.L.,Gu,A.,Fernando,A.,Gülçehre,


### Ç.,Pascanu,R.,andDe,S. Resurrectingrecurrentneural

Qin,Z.,Yang,S.,andZhong,Y. Hierarchicallygatedrecurnetworks for long sequences. CoRR, abs/2303.06349, rentneuralnetworkforsequencemodeling. InNeurIPS,
2023b. doi: 10.48550/arXiv.2303.06349. URLhttps:
2023c.
//doi.org/10.48550/arXiv.2303.06349.

### Qin, Z., Zhong, Y., and Deng, H. Exploring transformer

Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J.,
extrapolation. InProceedingsoftheAAAIConferenceon
Chanan,G.,Killeen,T.,Lin,Z.,Gimelshein,N.,Antiga,
ArtificialIntelligence,2024.

### L.,etal. Pytorch: Animperativestyle,high-performance

deep learning library. Advances in neural information Ramachandran,P.,Zoph,B.,andLe,Q.V. Searchingfor
processingsystems,32,2019. activationfunctions,2017.
11

<!-- Page 12 -->


### TNLwithLightningAttention

Sakaguchi,K.,Bras,R.L.,Bhagavatula,C.,andChoi,Y. Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,
Winogrande: Anadversarialwinogradschemachallenge L., Gomez, A. N., Kaiser, Ł., and Polosukhin, I. Atatscale,2019. tentionisallyouneed. Advancesinneuralinformation
processingsystems,30,2017.
Sap,M.,Rashkin,H.,Chen,D.,LeBras,R.,andChoi,Y.
Socialiqa: Commonsensereasoningaboutsocialinterac- Wang,B.andKomatsuzaki,A. Gpt-j-6b: A6billionparamtions,2019. eterautoregressivelanguagemodel,2021.
Workshop,B.,:,Scao,T.L.,Fan,A.,Akiki,C.,Pavlick,E.,
Shaham,U.,Segal,E.,Ivgi,M.,Efrat,A.,Yoran,O.,Haviv,

### Ilic´,S.,Hesslow,D.,Castagné,R.,Luccioni,A.S.,Yvon,

A., Gupta, A., Xiong, W., Geva, M., Berant, J., et al.

### F.,Gallé,M.,Tow,J.,Rush,A.M.,Biderman,S.,Webson,


### Scrolls: Standardized comparison over long language

A., Ammanamanchi, P.S., Wang, T., Sagot, B., Muensequences. arXivpreprintarXiv:2201.03533,2022.
nighoff,N.,delMoral,A.V.,Ruwase,O.,Bawden,R.,
Bekman, S.,McMillan-Major, A., Beltagy, I., Nguyen,

### Shoeybi,M.,Patwary,M.,Puri,R.,LeGresley,P.,Casper,


### H., Saulnier, L., Tan, S., Suarez, P. O., Sanh, V., Lau-

J., and Catanzaro, B. Megatron-lm: Training multirençon,H.,Jernite,Y.,Launay,J.,Mitchell,M.,Raffel,
billion parameter language models using model paral-
C.,Gokaslan,A.,Simhi,A.,Soroa,A.,Aji,A.F.,Alfassy,
lelism. arXivpreprintarXiv:1909.08053,2019.

### A.,Rogers,A.,Nitzav,A.K.,Xu,C.,Mou,C.,Emezue,


### C.,Klamm,C.,Leong,C.,vanStrien,D.,Adelani,D.I.,


### Tay,Y.,Bahri,D.,Metzler,D.,Juan,D.-C.,Zhao,Z.,and

Radev, D., Ponferrada, E. G., Levkovizh, E., Kim, E.,

### Zheng, C. Synthesizer: Rethinking self-attention for

Natan, E. B., Toni, F. D., Dupont, G., Kruszewski, G.,
transformermodels. InInternationalconferenceonma-
Pistilli, G., Elsahar, H., Benyamina, H., Tran, H., Yu,
chinelearning,pp.10183–10192.PMLR,2021.

### I.,Abdulmumin,I.,Johnson,I.,Gonzalez-Dios,I.,dela

Team,M.N.etal. Introducingmpt-7b: Anewstandardfor Rosa, J., Chim, J., Dodge, J., Zhu, J., Chang, J., Froopen-source,commerciallyusablellms,2023. URLwww. hberg, J., Tobing, J., Bhattacharjee, J., Almubarak, K.,
mosaicml.com/blog/mpt-7b.Accessed,pp.05–05,2023. Chen,K.,Lo,K.,Werra,L.V.,Weber,L.,Phan,L.,allal,L.B.,Tanguy,L.,Dey,M.,Muñoz,M.R.,Masoud,
Tillet, P., Kung, H.-T., and Cox, D. D. Triton: an inter- M.,Grandury,M.,Šaško,M.,Huang,M.,Coavoux,M.,
mediatelanguageandcompilerfortiledneuralnetwork Singh, M., Jiang, M. T.-J., Vu, M. C., Jauhar, M. A.,
computations. Proceedings of the 3rd ACM SIGPLAN Ghaleb, M., Subramani, N., Kassner, N., Khamis, N.,
InternationalWorkshoponMachineLearningandPro- Nguyen,O.,Espejel,O.,deGibert,O.,Villegas,P.,HengrammingLanguages,2019. derson, P., Colombo, P., Amuok, P., Lhoest, Q., Harliman, R., Bommasani, R., López, R. L., Ribeiro, R.,
Touvron,H.,Lavril,T.,Izacard,G.,Martinet,X.,Lachaux, Osei, S., Pyysalo, S., Nagel, S., Bose, S., Muhammad,
M.-A.,Lacroix,T.,Rozière,B.,Goyal,N.,Hambro,E., S.H.,Sharma,S.,Longpre,S.,Nikpoor,S.,Silberberg,
Azhar,F.,Rodriguez,A.,Joulin,A.,Grave,E.,andLam- S., Pai, S., Zink, S., Torrent, T. T., Schick, T., Thrush,
ple,G. Llama: Openandefficientfoundationlanguage T., Danchev, V., Nikoulina, V., Laippala, V., Lepercq,
models. arXivpreprintarXiv:2302.13971,2023a. V.,Prabhu,V.,Alyafeai,Z.,Talat,Z.,Raja,A.,Heinzerling, B., Si, C., Tas¸ar, D.E., Salesky, E., Mielke, S.J.,
Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, Lee,W.Y.,Sharma,A.,Santilli,A.,Chaffin,A.,Stiegler,
A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P., A., Datta, D., Szczechla, E., Chhablani, G., Wang, H.,
Bhosale,S.,Bikel,D.,Blecher,L.,Ferrer,C.C.,Chen, Pandey,H.,Strobelt,H.,Fries,J.A.,Rozen,J.,Gao,L.,
M.,Cucurull,G.,Esiobu,D.,Fernandes,J.,Fu,J.,Fu,W., Sutawika,L.,Bari,M.S.,Al-shaibani,M.S.,Manica,M.,
Fuller,B.,Gao,C.,Goswami,V.,Goyal,N.,Hartshorn, Nayak,N.,Teehan,R.,Albanie,S.,Shen,S.,Ben-David,
A.,Hosseini,S.,Hou,R.,Inan,H.,Kardas,M.,Kerkez, S.,Bach,S.H.,Kim,T.,Bers,T.,Fevry,T.,Neeraj,T.,
V.,Khabsa,M.,Kloumann,I.,Korenev,A.,Koura,P.S., Thakker, U., Raunak, V., Tang, X., Yong, Z.-X., Sun,
Lachaux,M.-A.,Lavril,T.,Lee,J.,Liskovich,D.,Lu,Y., Z.,Brody,S.,Uri,Y.,Tojarieh,H.,Roberts,A.,Chung,
Mao,Y.,Martinet,X.,Mihaylov,T.,Mishra,P.,Molybog, H. W., Tae, J., Phang, J., Press, O., Li, C., Narayanan,
I.,Nie,Y.,Poulton,A.,Reizenstein,J.,Rungta,R.,Saladi, D.,Bourfoune,H.,Casper,J.,Rasley,J.,Ryabinin,M.,
K.,Schelten,A.,Silva,R.,Smith,E.M.,Subramanian,R., Mishra, M., Zhang, M., Shoeybi, M., Peyrounette, M.,
Tan,X.E.,Tang,B.,Taylor,R.,Williams,A.,Kuan,J.X., Patry, N., Tazi, N., Sanseviero, O., vonPlaten, P., Cor-
Xu,P.,Yan,Z.,Zarov,I.,Zhang,Y.,Fan,A.,Kambadur, nette, P., Lavallée, P. F., Lacroix, R., Rajbhandari, S.,
M.,Narang,S.,Rodriguez,A.,Stojnic,R.,Edunov,S., Gandhi, S., Smith, S., Requena, S., Patil, S., Dettmers,
andScialom,T.Llama2:Openfoundationandfine-tuned T.,Baruwa,A.,Singh,A.,Cheveleva,A.,Ligozat,A.-L.,
chatmodels,2023b. Subramonian,A.,Névéol,A.,Lovering,C.,Garrette,D.,
12

<!-- Page 13 -->


### TNLwithLightningAttention

Tunuguntla,D.,Reiter,E.,Taktasheva,E.,Voloshina,E., haylov,T.,Ott,M.,Shleifer,S.,Shuster,K.,Simig,D.,
Bogdanov,E.,Winata,G.I.,Schoelkopf,H.,Kalo,J.-C., Koura, P. S., Sridhar, A., Wang, T., and Zettlemoyer,
Novikova,J.,Forde,J.Z.,Clive,J.,Kasai,J.,Kawamura, L. Opt: Openpre-trainedtransformerlanguagemodels,
K.,Hazan,L.,Carpuat,M.,Clinciu,M.,Kim,N.,Cheng, 2022.
N., Serikov, O., Antverg, O., van der Wal, O., Zhang,
Zhao,Y.,Gu,A.,Varma,R.,Luo,L.,Huang,C.-C.,Xu,M.,

### R.,Zhang,R.,Gehrmann,S.,Mirkin,S.,Pais,S.,Shav-

Wright, L., Shojanazeri, H., Ott, M., Shleifer, S., et al.
rina,T.,Scialom,T.,Yun,T.,Limisiewicz,T.,Rieser,V.,

### Pytorchfsdp: experiencesonscalingfullyshardeddata

Protasov,V.,Mikhailov,V.,Pruksachatkun,Y.,Belinkov,
parallel. arXivpreprintarXiv:2304.11277,2023.
Y., Bamberger, Z., Kasner, Z., Rueda, A., Pestana, A.,

### Feizpour,A.,Khan,A.,Faranak,A.,Santos,A.,Hevia,

Zheng,L.,Wang,C.,andKong,L. Linearcomplexityran-

### A.,Unldreaj,A.,Aghagol,A.,Abdollahi,A.,Tammour,

domizedself-attentionmechanism. InInternationalCon-
A.,HajiHosseini,A.,Behroozi,B.,Ajibade,B.,Saxena,
ferenceonMachineLearning,pp.27011–27041.PMLR,
B.,Ferrandis,C.M.,McDuff,D.,Contractor,D.,Lansky,
2022.
D., David, D., Kiela, D., Nguyen, D.A., Tan, E., Baylor, E., Ozoani, E., Mirza, F., Ononiwu, F., Rezanejad, Zheng, L., Yuan, J., Wang, C., and Kong, L. Efficient
H.,Jones,H.,Bhattacharya,I.,Solaiman,I.,Sedenko,I., attentionviacontrolvariates.InInternationalConference
Nejadgholi,I.,Passmore,J.,Seltzer,J.,Sanz,J.B.,Dutra, on Learning Representations, 2023. URL https://
L.,Samagaio,M.,Elbadri,M.,Mieskes,M.,Gerchick, openreview.net/forum?id=G-uNfHKrj46.
M., Akinlolu, M., McKenna, M., Qiu, M., Ghauri, M.,
Burynok,M.,Abrar,N.,Rajani,N.,Elkott,N.,Fahmy,

### N.,Samuel,O.,An,R.,Kromann,R.,Hao,R.,Alizadeh,

S., Shubber, S., Wang, S., Roy, S., Viguier, S., Le, T.,
Oyebade, T., Le, T., Yang, Y., Nguyen, Z., Kashyap,

### A.R.,Palasciano,A.,Callahan,A.,Shukla,A.,Miranda-


### Escalada,A.,Singh,A.,Beilharz,B.,Wang,B.,Brito,C.,

Zhou, C.,Jain, C., Xu,C., Fourrier, C.,Periñán, D.L.,
Molano,D.,Yu,D.,Manjavacas,E.,Barth,F.,Fuhrimann,

### F.,Altay,G.,Bayrak,G.,Burns,G.,Vrabec,H.U.,Bello,

I.,Dash,I.,Kang,J.,Giorgi,J.,Golde,J.,Posada,J.D.,
Sivaraman,K.R.,Bulchandani,L.,Liu,L.,Shinzato,L.,
deBykhovetz,M.H.,Takeuchi,M.,Pàmies,M.,Castillo,
M.A.,Nezhurina,M.,Sänger,M.,Samwald,M.,Cullan,

### M.,Weinberg,M.,Wolf,M.D.,Mihaljcic,M.,Liu,M.,


### Freidank,M.,Kang,M.,Seelam,N.,Dahlberg,N.,Broad,

N.M.,Muellner,N.,Fung,P.,Haller,P.,Chandrasekhar,

### R.,Eisenberg,R.,Martin,R.,Canalli,R.,Su,R.,Su,R.,


### Cahyawijaya, S., Garda, S., Deshmukh, S. S., Mishra,

S., Kiblawi, S., Ott, S., Sang-aroonsiri, S., Kumar, S.,
Schweter,S.,Bharati,S.,Laud,T.,Gigant,T.,Kainuma,

### T.,Kusa,W.,Labrak,Y.,Bajaj,Y.S.,Venkatraman,Y.,

Xu, Y., Xu, Y., Xu, Y., Tan, Z., Xie, Z., Ye, Z., Bras,
M.,Belkada,Y.,andWolf,T. Bloom: A176b-parameter
open-accessmultilinguallanguagemodel,2023.
Zellers,R.,Holtzman,A.,Bisk,Y.,Farhadi,A.,andChoi,Y.
Hellaswag: Canamachinereallyfinishyoursentence?,
2019.
Zeng, A., Liu, X., Du, Z., Wang, Z., Lai, H., Ding, M.,

### Yang,Z.,Xu,Y.,Zheng,W.,Xia,X.,etal. Glm-130b:

An open bilingual pre-trained model. arXiv preprint
arXiv:2210.02414,2022.
Zhang, S., Roller, S., Goyal, N., Artetxe, M., Chen, M.,
Chen, S., Dewan, C., Diab, M., Li, X., Lin, X. V., Mi-
13

<!-- Page 14 -->


### TNLwithLightningAttention

Appendix Algorithm5LightningAttention(withdecay)ForwardPass
Input:Q,K,V∈Rn×d,decayrateλ∈R+,blocksizesB.
A.LinearAttentionwithdecay DivideXintoT = n blocksX ,X ,...X ofsizeB ×d

## B 1 2 T

each,whereX∈{Q,K,V,O}.
TransNormerLLMusesLRPE-dpositionalencoding,which InitializemaskM∈RB×B,whereM =λt−s,ift≥s,else
ts
hasthefollowingformat: 0.
InitializeΛ=diag{λ,λ2,...,λB}∈RB×B.
a ts =q⊤ t k s λt−sexpiθ(t−s). (15) InitializeKV=0∈Rd×d.
Accordingto(Qinetal.,2023b),Lrpecanbedecomposed fort=1,...,T do
intoqandk,soweconsiderthefollowingsimplifiedform: LoadQ t ,K t ,V t ∈RB×dfromHBMtoon-chipSRAM.
Onchip,computeO =[(Q K⊤)⊙M]V .
a ts =q⊤ t k s λt−s, Onchip,computeO i i n n t t r e a r =ΛQ t t (K t V). t
t Onchip,computeKV=λBKV+(λBΛ−1K )⊤V .
o⊤ t = (cid:88) a ts v t ⊤ WriteO t =O intra +O inter toHBMasthet-th t block t ofO.
s=1 endfor
t returnO.
= (cid:88) q⊤k λt−sv⊤ (16)
t s s C.0.1.FORWARDPASS
s=1
=q⊤(cid:88) t k λt−sv⊤ DuringforwardpassofLinearattentionwithdecay,thet-th
t s s outputcanbeformulatedas
s=1 (cid:88)
≜q⊤ t kv t . o⊤ t =q⊤ t λt−sk s v s ⊤. (20)
s≤t

### We call this Linear Attention with decay and prove it’s

equivalenttotherecurrenceform: Inarecursiveform,theaboveequationcanberewrittenas
kv 0 =0,kv t =λkv t−1 +k t v t ⊤,o⊤ t =q⊤ t kv t . (17) kv 0 =0∈Rd×d,
Wewilluseinductiontoprovekv t =kv t . kv t =λkv t−1 +k t v t ⊤, (21)
o⊤ =q⊤(kv ),

### BaseCase(n=1): t t t

kv 1 =k 1 v 1 ⊤ =kv 1 . (18) where kv = (cid:88) λt−sk v⊤. (22)
t s s
Assume the statement holds for n = m−1, i.e., kv =
m−1 s≤t
kv .Then,whenn=m:
m−1 Toperformtiling,letuswritetheequationsinblockform.
m
kv = (cid:88) k λm−sv⊤ Given the total sequence length n and block size B, X
m s s
s=1 is divided into T = B n blocks {X 1 ,X 2 ,...,X T } of size
m−1 B×deach,whereX∈{Q,K,V,O}.
=λ (cid:88) k λm−1−sv⊤+k v⊤
s s m m (19) Wefirstdefine
s=1
(cid:88)
=λkv m−1 +k m v m ⊤ KV 0 =0∈Rd×d,KV t = λtB−sk s v s ⊤. (23)
=λkv +k v⊤ s≤tB
m−1 m m
=kv m ,
GivenKV
t
,theoutputof(t+1)-thblock,i.e.,tB+r,with
1≤r ≤Bis
thestatementholds. Therefore,byinduction,thestatement
o⊤
holdsforalln≥1. tB+r
(cid:88)
=q⊤ λtB+r−sk v⊤
tB+r s s
B.LightningAttentionwithdecay s≤tB+r
 
tB+r
WeextendedLightningAttentiontoaccommodateLinear (cid:88) (cid:88)
Attentionwithdecay. Thecompletealgorithmcanbefound =q⊤ tB+r λtB+r−sk s v s ⊤+λr λtB−sk s v s ⊤ 
s=tB+1 s≤tB
inAlgorithm5,6,andtheproofofcorrectnessisprovided
tB+r
inC. (cid:88)
=q⊤ λtB+r−sk v⊤+λrq kv⊤ .
tB+r s s tB+r tB
s=tB+1

### C.Proofs (24)

Herewediscusslinearattentionwithdecaydirectly,because
vanillalinearattentionisthecaseofλ=1.
14

<!-- Page 15 -->


### TNLwithLightningAttention

Algorithm 6 Lightning Attention(with decay) Backward C.0.2.BACKWARDPASS

### Pass

Forbackwardpass,letusconsiderthereverseprocess. First
Input:Q,K,V,dO∈Rn×d,decayrateλ∈R+,blocksizes
givendo ,wehave

### B. t

DivideXintoT = n blocksX ,X ,...X ofsizeB ×d dq⊤ =do⊤kv⊤ ∈R1×d,

### B 1 2 T t t t

each,whereX∈{Q,K,V}.
dk⊤ =v⊤dkv⊤ ∈R1×d,
Divide dX into T = n blocks dX ,dX ,...dX of size t t t

## B 1 2 T


### B×deach,whereX∈{Q,K,V,O}. dv⊤ =k⊤dkv ∈R1×d, (28)

InitializemaskM∈RB×B,whereM =λt−s,ift≥s,else t t t
ts (cid:88)
0. dkv t = λs−tq s do⊤ s ∈Rd×d.
InitializeΛ=diag{λ,λ2,...,λB}∈RB×B .
s≥t
InitializeKV=0,dKV=0∈Rd×d.
Bywritingdkv inarecursiveform,weget
fort=1,...,T do t
Load K t ,V t ,O t ,dO t ∈ RB×d from HBM to on-chip dkv n+1 =0∈Rd×d,
(29)

## Sram.

dkv =λdkv +q do⊤ .
Onchip,computedQ =[(dO V⊤)⊙M]K . t−1 t t−1 t−1
intra t t t
Onchip,computedQ =ΛdO (KV)⊤. To facilitate the understanding of tiling, let us consider
inter t
Onchip,computeKV=λBKV+(λBΛ−1K )⊤V . the above equations in block style. Given the total set t
WritedQ t =dQ intra +dQ inter toHBMasthet-thblock quence length n and block size B, X is divided into
ofdQ. T = n blocks {X ,X ,...,X } of size B × d each,
endfor B 1 2 T
whereX∈{Q,K,V,O,dO}.
fort=T,...,1do
LoadQ ,K ,V ,O ,dO ∈RB×dfromHBMtoon-chip
t t t t t Wefirstdefine

## Sram.

Onchip,computedK =[(dO V⊤)⊙M]⊤Q . dKV T+1 =0∈Rd×d,
intra t t t
Onchip,computedK inter =(λBΛ−1V t )(dKV)⊤. dKV = (cid:88) λs−tBq do⊤. (30)
Onchip,computedV =[(Q K⊤)⊙M]⊤dO . t s s
intra t t t s>tB
Onchip,computedV =(λBΛ−1K )dKV.
inter t
Onchip,computedKV=λBdKV+(ΛQ t )⊤dO t . Thenforthe(t+1)-thblock,i.e.,tB+r,0≤r <B,we

### WritedK =K +K ,dV =V +V to

t intra inter t intra inter have
HBMasthet-thblockofdK,dV.
dq⊤
endfor tB+r
returndQ,dK,dV. =do⊤ (cid:88) λtB+r−sv k⊤
tB+r s s

### Rewritteninmatrixform,wehave s≤tB+r


### O t+1 =[(Q t+1 K⊤ t+1 )⊙M]V t+1  t (cid:88) B+r (cid:88) 

(cid:124) Intra (cid:123)(cid:122) Block (cid:125) (25) =do⊤ tB+r λtB+r−sv s k⊤ s +λr λtB−sv s k⊤ s
s=tB+1 s≤tB

## +Λq (Kv ),

t+1 t
(cid:124) (cid:123)(cid:122) (cid:125) tB+r
InterBlock =do⊤ (cid:88) λtB+r−sv k⊤+λrdo kv⊤ .
tB+r s s tB+r tB
where (cid:40)
λt−s t≥s s=tB+1

## M = , (31)

ts
0 t<s (26) Inmatrixform,wehave
Λ=diag{1,...,λB−1}. dQ =[(dO V⊤ )⊙M]K
t+1 t+1 t+1 t+1
(cid:124) (cid:123)(cid:122) (cid:125)
AndtheKVat(t+1)-thblockcanbewrittenas
IntraBlock
(32)
KV = (cid:88) λ(t+1)B−sk⊤v +ΛdO (KV⊤).
t+1 s s t+1 t
(cid:124) (cid:123)(cid:122) (cid:125)
s≤(t+1)B InterBlock
(t+1)B Since the recursion of dK steps from t+1 to t, given
(cid:88) (cid:88) t
=λB λtB−sk⊤ s v s + λ(t+1)B−sk⊤ s v s KV t+1 ,dK t forthet-thblock,i.e.,atpositions(t−1)B+
s≤tB s=tB+1
=λBKV + (cid:0) diag{λB−1,...,1}K (cid:1)⊤ V
t t t
=λBKV + (cid:0) λBΛ−1K (cid:1)⊤ V .
t t t
(27)
ThecompleteexpressionoftheforwardpassofLightning
AttentionwithdecaycanbefoundinAlgorithm5.
15

<!-- Page 16 -->


### TNLwithLightningAttention

r,0<r ≤Bis Finally,therecursiverelationfordKV is
t
dk⊤ dKV = (cid:88) λs−tBq do⊤
(t−1)B+r t s s
=v⊤ (cid:88) λs−(t−1)B−rdo q⊤ s>tB
(t−1)B+r s s (cid:88)
=λB λs−(t+1)Bq do⊤
s≥(t−1)B+r s s
  s>(t+1)B
tB (37)
(cid:88)
=v ( ⊤ t−1)B+r  λtB+r−sdo s q⊤ s + (t (cid:88) +1)B λs−tBq do⊤
s=(t−1)B+r s s
(cid:32) (cid:33) (33) s=tB+1
(cid:88)
+v⊤ λB−r λs−tBdo q⊤ =λBdKV +(ΛQ )⊤dO .
(t−1)B+r s s t+1 t t
s>tB Algorithm6describesthebackwardpassofLightningAt-
(cid:88) tB tentionwithdecayinmoredetail.
=v⊤ λtB+r−sdo q⊤
(t−1)B+r s s
s=(t−1)B+r

### D.Corpus

+λB−rv⊤ dKV⊤.
(t−1)B+r t
Wegatheranextensivecorpusofpubliclyaccessibletext

### Inmatrixform,weget

fromtheinternet,totalingover700TBinsize.Thecollected
dK =[(dO V⊤ )⊙M]⊤Q
t−1 t−1 t−1 t−1 dataareprocessedbyourdatapreprocessingprocedureas
(cid:124) (cid:123)(cid:122) (cid:125)
IntraBlock showninFig.6,leavinga6TBcleanedcorpuswithroughly
(34)
+λBΛ−1V (dKV⊤). 2trilliontokens. Wecategorizeourdatasourcestoprovide
t−1 t
(cid:124) (cid:123)(cid:122) (cid:125) better transparency and understanding. The specifics of

### InterBlock

thesecategoriesareoutlinedinTable10.
ConsideringdV forthet-thblock,i.e.,atpositions(t−
t
1)B+r,0<r ≤B,wehave D.1.DataPreprocessing
dv⊤
(t−1)B+r Our data preprocessing procedure consists of three steps:
(cid:88)
=k⊤ λs−(t−1)B−rq do⊤ 1). rule-based filtering, 2). deduplication, and 3). a self-
(t−1)B+r s s
cleaningscheme. Beforebeingaddedtothetrainingcorpus,
s≥(t−1)B+r
  thecleanedcorpusneedstobeevaluatedbyhumans.
tB
(cid:88)
=k⊤ (t−1)B+r  λtB+r−sq⊤ s do s Rule-basedfiltering Therulesweusedtofilterourcols=(t−1)B+r
(cid:32) (cid:33) (35) lecteddataarelistedasfollows:
(cid:88)
+k⊤ λB−r λs−tBq do⊤
(t−1)B+r s s • RemovalofHTMLTagsandURLs: Theinitialstepin
s>tB
ourprocessistheeliminationofHTMLtagsandweb
tB
(cid:88) URLsfromthetext. Thisisachievedthroughregular
=k⊤ λtB+r−sq do⊤
(t−1)B+r s s expressiontechniquesthatidentifythesepatternsand
s=(t−1)B+r
removethem,ensuringthelanguagemodelfocuseson
+λB−rk⊤ (t−1)B+r dKV t . meaningfultextualcontent.

### Inmatrixform,weget

• Elimination of Useless or Abnormal Strings: SubsedV =[(Q K⊤ )⊙M]⊤dO
t−1 t−1 t−1 t quently,thecleaneddatasetundergoesasecondlayer
(cid:124) (cid:123)(cid:122) (cid:125)
ofrefinementwherestringsthatdonotprovidevalue,

### IntraBlock (36)

+λBΛ−1K (dKV ). such as aberrant strings or garbled text, are identit−1 t
(cid:124) (cid:123)(cid:122) (cid:125) fied and excised. This process relies on predefined

### InterBlock

rules that categorize certain string patterns as noncontributingelements.
• DeduplicationofPunctuationMarks: Weaddressthe
problemofredundantpunctuationmarksinthedata.
Multipleconsecutivepunctuationmarkscandistortthe
naturalflowandstructureofsentenceswhentraining
themodel. Weemployarule-basedsystemthattrims
these duplications down to a single instance of each
punctuationmark.
16

<!-- Page 17 -->

TNLwithLightningAttention
Academic
writings

### Model-based Human


### Filtering Evaluation

Books Rule-based Self-Clean x N
Filtering

### Scheme

Training data

### Code

Deduplication

### Web

Evaluation Model
…
Figure6.DataPreprocessProcedure.Thecollecteddataundergoesaprocessofrule-basedfilteringanddeduplication,followedbyour
self-cleandataprocessingstrategy:model-basedfiltering,humanevaluation,andevaluationmodel.Afterseveraliterationsoftheabove
cycle,weobtainhigh-qualitytrainingdataataround2Ttokens.
• HandlingSpecialCharacters: Unusualorspecialchar- which may have a significant impact on the diversity of
actersthatarenotcommonlypartofthelanguage’stext the training data. Assuming that the majority of the precorpusareidentifiedandeitherremovedorreplaced processeddataisofhighquality,wecantrainanevaluation
withastandardizedrepresentation. modelontheentiresetofpre-processeddata,andthemodel
willautomaticallysmooththedatamanifolddistributionand
• NumberStandardization: Numericalfiguresmaybe outletlow-qualitydatawhileretainingthemajorityofthe
presented in various formats across different texts. diversities.
Thesenumbersarestandardizedintoacommonformat
Theself-cleaningschemeunfoldsasfollows:
tomaintainconsistency.
• PreservationofMarkdown/LaTeXFormats: Whilere- • Evaluation Model: We train a 385M model on the
movingnon-textualelements,exceptionsaremadefor pre-processedcorpustoactasadataqualityfilter.
texts in Markdown and LaTeX formats. Given their
structurednatureandubiquitoususeinacademiaand • Model-Based Data Filtering: We use the evaluation
documentation,preservingtheseformatscanenhance model to assess each piece of data with perplexity.
themodel’sabilitytounderstandandgeneratesimilarly Onlydataachievingascoreaboveacertainthreshold
formattedtext. is preserved for the next step. Low-quality data are
weededoutatthisstage.
Deduplication Toensuretheuniquenessofourdataand
• HumanEvaluation: Wesampleasmallportionofthe
avert the risk of overfitting, we employ an efficient defiltereddataandmanuallyevaluatethequality.
duplication strategy at the document or line level using
MinHashandLocality-SensitiveHashing(LSH)algorithms.
Thesestepsarerepeatedincycles,witheachiterationim-

### ThiscombinationofMinHashandLSHensuresabalance

provingtheoverallqualityofthedataandensuringtherebetweencomputationalefficiencyandaccuracyinthededusultingmodelistrainedonrelevant,high-qualitytext. This
plication process, providing a robust mechanism for data
self-cleaningprocessprovidesarobustmechanismformaindeduplicationandtextwatermarkremoval.
tainingdataintegrity,therebyenhancingtheperformanceof
theresultinglanguagemodel.
Self-cleaningscheme Ourdataself-cleaningprocessinvolvesaniterativeloopofthefollowingthreestepstocon-

### D.2.Tokenization

tinuouslyrefineandenhancethequalityofourdataset. An
issue of using model-based data filters is that the filtered We tokenize the data with the Byte-Pair Encoding (BPE)
datawillhaveasimilardistributionastheevaluationmodel, algorithm. Notably,toenhancecompatibilitywithChinese
17

<!-- Page 18 -->


### TNLwithLightningAttention

proceduresplitsthreegeneralmatrixmultiplies(GEMMs)
Table10.Statistics of our corpus. For each category, we list
insidetheSGLUblockacrossmultipleGPUsandonlyinthenumberofepochsperformedonthesubsetwhentrainingon
troducesasingleall-reducecollectivecommunicationoperthe 2 trillion tokens, as well as the number of tokens and disk
ationinboththeforwardandbackwardpasses,respectively.
sizes.Wealsolistthetableontherightaccordingtothelanguage
distribution. GLAModelParallelismRecalltheGLAblockin(11),its
Dataset Epochs Tokens Disksize
modelparallelismversionis:

### AcademicWritings 1.53 200B 672GB

Books 2.49 198B 723GB [O 1 ,O 2 ]=SRMSNorm(QK⊤V)⊙U, (41)

### Code 0.44 689B 1.4TB where:

Encyclopedia 1.51 5B 18GB Q=[ϕ(XW1),ϕ(XW2)],K=[ϕ(XW1),ϕ(XW2)],
FilteredWebpages 1.00 882B 3.1TB q q q q (42)
Others 0.63 52B 154GB V=X[W1,W2],U=X[W1,W2],
v v u u

### Total - 2026B 6TB


### Note that in our implementation, we use the combined

Language Tokens Disksize QKVU projection to improve computation efficiency for
English 743B 2.9TB linearattention. Theobtainedsplitoutputmatrix[O 1 ,O 2 ]
Chinese 555B 1.7TB againismultipliedbyaweightmatrixsplitalongitscolumns
Code 689B 1.4TB whichissimilarto(40).
Others 39B 89GB

### Total 2026B 6TB


### F.AdditionalTNLAblation

language content, a significant number of common and
uncommonChinesecharactershavebeenincorporatedinto TransformervsTNL Wecarriedoutameticulousseries
our vocabulary. In cases where vocabulary items are not of comparative tests between our TNL and Transformer,
presentinthedictionary,thewordsarebrokendowninto spanning over an array of disparate sizes. The comparatheirconstituentUTF-8characters. Thisstrategyensures tive performance of these models is clearly illustrated in
comprehensivecoverageandflexibilityfordiverselinguistic Table11.Underidenticalconfigurations,itbecomesevident
inputduringmodeltraining. thatourTNLexhibitsasuperiorperformanceprofilecomparedtoTransformer. WeobservedthatTNLoutperformed
E.DistributedSystemOptimization Transformerbyaremarkable5%atthesizeof385M.More
importantly,asthesizereached1B,thissuperioritybecame
Weoptimizeoursystemtoexecutelarge-scalepre-training evenmorepronounced,withanadvantageof9%forTNL
forTNLeffectively. Weemployfullyshardeddataparal- overTransformer.
lelism (FSDP) (Zhao et al., 2023), activation checkpoint-
Table11.TransformervsTNL.TNLperformsbetterthanTransing(Shoeybietal.,2019),andautomaticmixedprecision
formerinsizeof385Mand1Bunderidenticalconfigurationsby
(AMP) (Micikevicius et al., 2017) techniques to reduce
5%and9%,respectively.
memoryfootprintandexpeditecomputationalspeed. We
usedBFloat16(Kalamkaretal.,2019)toenhancetraining Method Updates Loss PPL
stability. We implemented model parallelism tailored to Transformer-385M 100K 2.362 5.160

## Tnl-385M 100K 2.248 4.770

LightningAttention. InspiredbyMegatron-LM(Shoeybi

### Transformer-1B 100K 2.061 4.765

et al., 2019) model parallelism, which independently ad-

## Tnl-1B 100K 1.896 3.729

dresses self-attention and MLP blocks, we apply model
parallelismtoSGLUandGLAseparately. Thedetailsof Table12.TransNormer vs TNL. TNL performs better than
TransNormer.
ourmodelparallelismstrategiesareelaboratedbelow.

### Method Params Updates Loss PPL

SGLUModelParallelismRecallSGLUstructurein(12):

## Tnl 385M 100K 2.248 4.770

O=[(XW v )⊙(XW u )]W o , (38) TransNormer-T1 379M 100K 2.290 4.910
ThemodelparallelismadaptationofSGLUisasfollows: TransNormer-T2 379M 100K 2.274 4.858

## [O′,O′]=X[W1,W2]⊙X[W1,W2]

1 2 v v u u We compare the original TransNormer and the improved
(39)
=[XW1,XW2]⊙[XW1,XW2], TNLandtheresultsareshowninTable12. TNLexhibited
v v u u
whichsplitstheweightmatricesW andW alongtheir anenhancementof2%and1%respectively.
v u
columns and obtains an output matrix splitting along its
columnstoo. Thenthesplitoutput[O ,O ]ismultiplied Speed Normalization Fucntions We enhanced SRM-
1 2
byanothermatrixwhichissplitalongitsrowsas: SNorm using Triton, resulting in notable improvements
O=[O′,O′][W1,W2]⊤ =O′W1+O′W2 (40) inprocessingspeedforlargerdimensions,asshowninFig.
1 2 o o 1 o 2 o
7,outperformingconventionalPyTorchimplementations.
SimilartomodelparallelisminMegatron-LM,thiswhole
18

<!-- Page 19 -->

TNLwithLightningAttention
2.4
2.1
1.8
1.5
1.2
0.9
0.6
0.3
0.0
128 256 512 1024 2048 4096 8192 16384 32768
)s(
emitnuR
Forward Pass
5.4
Triton SRMSNorm PyTorch SRMSNorm 4.8
4.2
3.6
3.0
2.4
1.8
1.2
0.6
0.0
128 256 512 1024 2048 4096 8192 16384 32768
Sequence length
)s(
emitnuR

### Backward Pass

Triton SRMSNorm PyTorch SRMSNorm
Sequence length
1.4
1.2
1.0
0.8
0.6
0.4
0.2
0.0
512 1024 2048 4096 8192 16384
)s(
emitnuR
Forward Pass
3.5
Triton SRMSNorm PyTorch SRMSNorm 3.0
2.5
2.0
1.5
1.0
0.5
0.0
512 1024 2048 4096 8192 16384
Feature dimension
)s(
emitnuR

### Backward Pass

Triton SRMSNorm PyTorch SRMSNorm

### Feature dimension

Figure7.PerformanceEvaluationofSRMSNormImplementation.Theupperfiguresexhibittheruntimecomparisonoftheforward
pass(leftsection)andbackwardpass(rightsection)fordifferentsequencelengths,withafixedfeaturedimensionof3072.Thelowertwo
figuresillustratetheruntimecomparisonforvariousfeaturedimensions,withafixedsequencelengthof4096.
19

## Tables

**Table (Page 2):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
| HGR | N |  |  |  |
|  |  |  |  |  |
| TNN LLa | MA-FA2 |  |  |  |


**Table (Page 2):**

|  |  |  |  | HGR TNN | N |
|---|---|---|---|---|---|
|  |  |  |  | LLaM TNL- | A-FA2 LA |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 2):**

|  |  |  |  | HGR TNN | N |
|---|---|---|---|---|---|
|  |  |  |  | LLa TNL | MA-FA2 -LA |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 2):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
| HG | RN |  |  |  |  |  |
| TN | N |  |  |  |  |  |


**Table (Page 4):**

| 𝑡 𝑸∈ℝ𝐧×𝐝 𝒕 𝑲∈ℝ𝒏×𝒅 𝒕 𝑽∈ℝ𝑛×𝑑 store in HBM |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | 𝒕 |  |  |  | 𝑽∈ℝ𝑛×𝑑 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | Copy Block to SRAM |  |  |  |  |  |  |  |  |  |


**Table (Page 5):**

|  |  |
|---|---|
|  |  |


**Table (Page 5):**

|  |  |
|---|---|
|  |  |


**Table (Page 7):**

| L | ightni | ng |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 7):**

| Li | ghtning |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 7):**

| F L | lash2 ightni | ng |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 7):**

| Li | ghtnin | g |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 7):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2819.6 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | 967.17 |  |  | 961.93 |  |  |  |  |  |
|  | 506.77 |  |  | 455.36 |  |  | 537.8 |  |  | 537.97 |  |  |  |  |  |  |  |  |  |  |  |
| 252.12 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 8):**

| TNL | 0.39 | 1.0 | 62.14 | 66.70 | 46.27 | 54.46 | 55.43 | 27.99 | 32.40 | 25.90 | 25.24 |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | 1.3 0.3 1.4 0.3 1.5 - 1.0 0.35 |  | 57.77 71.71 53.70 59.35 57.24 29.69 33.20 60.73 70.67 47.18 53.51 56.99 26.88 31.40 - 72.36 52.48 54.62 60.48 29.44 34.00 61.38 75.14 61.50 60.30 63.38 32.17 35.60 |  |  |  |  |  |  |  |  |
| TNL | 1.0 | 1.2 | 63.27 | 72.09 | 56.49 | 60.38 | 63.68 | 35.24 | 36.60 | 27.10 | 26.01 |
|  | 6.7 0.3 6.9 0.3 7.4 - 7.2 1.5 7.0 2.6 7.1 1.4 6.7 1.0 6.7 1.0 6.7 2.0 |  | 66.18 76.22 67.21 65.19 65.66 34.64 37.20 63.46 75.14 63.92 60.77 67.34 35.41 37.00 - 76.06 65.51 61.01 67.80 37.46 40.20 73.73 79.38 76.3 67.17 74.62 43.60 43.80 72.72 76.50 72.17 68.35 75.17 42.32 39.60 77.65 69.37 50.51 57.62 59.13 34.30 37.00 72.20 78.84 74.51 65.67 72.39 41.30 41.00 76.50 79.80 76.10 70.10 72.80 47.60 57.20 77.68 78.07 76.02 68.98 76.30 46.33 44.20 |  |  |  |  |  |  |  |  |
| TNL | 6.8 | 1.4 | 75.87 | 80.09 | 75.21 | 66.06 | 75.42 | 44.40 | 63.40 | 43.10 | 43.18 |
|  | 13 0.3 12 0.3 14 - 13 2.6 13 1.0 13 1.0 13 2.0 |  | 65.93 75.84 69.83 65.19 67.00 35.75 38.80 65.72 76.17 68.85 66.22 70.62 38.23 41.00 70.12 78.51 71.49 64.48 72.35 40.87 41.00 79.20 77.31 75.27 70.01 77.36 47.01 43.80 72.29 77.58 72.07 70.09 75.42 43.86 43.00 77.95 79.16 79.06 72.61 77.40 47.70 44.80 80.61 79.11 79.35 72.38 79.34 48.98 35.20 |  |  |  |  |  |  |  |  |
| TNL | 15 | 2.0 | 76.64 | 81.56 | 82.18 | 75.61 | 77.61 | 50.51 | 46.40 | 60.06 | 53.01 |


**Table (Page 9):**

| TNL | 0.39 | 1.0 | 3.67/1.16/3.14 | 8.27/0.82/6.91 | 13.62/3.29/10.95 | 14.29 | 11.69 | 28.14 | 17.36 | 9.48 |
|---|---|---|---|---|---|---|---|---|---|---|
|  | 1.3 0.3 1.4 0.3 1.0 0.35 |  | 5.7/2.09/4.41 10.17/0.82/8.29 12.36/3.15/9.85 18.37 13.42 29.15 12.44 4.03/1.25/3.33 8.34/0.87/6.97 13.17/3.4/10.92 16.09 11.91 28.72 9.06 2.74/0.67/2.37 10.95/1.28/8.66 13.29/3.09/10.58 16.17 12.91 29.19 14.75 |  |  |  |  |  |  |  |
| TNL | 1.0 | 1.2 | 6.81/2.30/5.25 | 12.28/1.23/9.27 | 14.60/3.51/11.62 | 15.02 | 14.66 | 28.72 | 37.32 | 12.51 |


**Table (Page 19):**

| T | riton S | RMSNo | rm | PyTorch | SRMS | Norm |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 19):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 19):**

| Trito | n SRMSNo | rm P | yTorch SR | MSNorm |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 19):**

| Trito | n SRMSNo | rm | PyTorch SR | MSNorm |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
