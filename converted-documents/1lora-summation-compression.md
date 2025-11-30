---
title: "LoRA Summation Compression"
original_file: "./1LoRA_Summation_Compression.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "multimodal"]
keywords: ["fine", "lora", "tuning", "bitfit", "mora", "page", "method", "memory", "difffit", "parameters"]
summary: "<!-- Page 1 -->

1LoRA: Summation Compression for Very Low-Rank Adaptation
AlessioQuercia1,3 ZhuoCao1 AryaBangun1 RichardD.Paul1,4

### AbigailMorrison2,3 IraAssent1,5 HannoScharr1

1 IAS-82 IAS-6,ForschungszentrumJuelich,Juelich,Germany
3 Dept. ofComputerScience,RWTHAachenUniversity,Aachen,Germany
4 Dept. ofComputerScience,AarhusUniversity,Aarhus,Denmark
{a.quercia,z.cao,a.bangun,r.paul,a.morrison,i.assent,h.scharr}@fz-juelich.de

### Abstract


### Parameter-Efficient Fine-Tuning (PEFT) method"
related_documents: []
---

# LoRA Summation Compression

<!-- Page 1 -->

1LoRA: Summation Compression for Very Low-Rank Adaptation
AlessioQuercia1,3 ZhuoCao1 AryaBangun1 RichardD.Paul1,4

### AbigailMorrison2,3 IraAssent1,5 HannoScharr1

1 IAS-82 IAS-6,ForschungszentrumJuelich,Juelich,Germany
3 Dept. ofComputerScience,RWTHAachenUniversity,Aachen,Germany
4 Dept. ofStatistics,LMUMunich,Munich,Germany
5 Dept. ofComputerScience,AarhusUniversity,Aarhus,Denmark
{a.quercia,z.cao,a.bangun,r.paul,a.morrison,i.assent,h.scharr}@fz-juelich.de

### Abstract


### Parameter-Efficient Fine-Tuning (PEFT) methods have

transformed the approach to fine-tuning large models for
(cid:80)(cid:80)(cid:80)
downstream tasks by enabling the adjustment of signifi- A
cantly fewer parameters than those in the original model

## W0 W0

matrices. In this work, we study the ”very low rank
regime”,wherewefine-tunethelowestamountofparame-

### B b

tersperlinearlayerforeachconsideredPEFTmethod. We
propose1LoRA(SummationLow-RankAdaptation),acompute, parameter and memory efficient fine-tuning method
whichusesthefeaturesumasfixedcompressionandasingle trainable vector as decompression. Differently from
(a)LoRA (b)1LoRA
state-of-the-art PEFT methods like LoRA, VeRA, and the
recent MoRA, 1LoRA uses fewer parameters per layer, re- Figure1. Comparingourmethod1LoRAtoLoRA.Left: LoRA
ducing the memory footprint and the computational cost. learnsthelow-rankdecomposition∆W =BA,whereA∈Rr×k
Weextensivelyevaluateourmethodagainststate-of-the-art and B ∈ Rd×r. Right: 1LoRA replaces the matrices A and B
PEFTmethodsonmultiplefine-tuningtasks,andshowthat withasumovertheinputfeaturesxascompressionandalearnablevectorb∈R1×dasdecompression: ∆W =b1T,wherethe
ourmethodnotonlyoutperformsthem,butisalsomorepafeaturesumis1Tx= (cid:80)k x ,with1beingavectoroflengthk
rameter, memory and computationally efficient. Moreover, i=1 i
containingonlyones. Thisreducesthetrainableparametersfrom
thankstoitsmemoryefficiency, 1LoRAallowstofine-tune
r×k+d×rinLoRAtodperlayerfor1LoRA.
more evenly across layers, instead of focusing on specific
ones(e.g.attentionlayers),improvingperformancefurther.
ments to their parameters, thereby reducing computational
andmemorydemandswhilepreservingperformance.

## Introduction


### AmongvariousPEFTapproaches,BitFit[41]hasgained

In recent years, the rapid development of large models notable attention. It streamlines fine-tuning by updating
hastransformedmultiplefieldsinartificialintelligence,es- only the bias parameters in transformer models, offering a
pecially in natural language processing [1, 33] and com- lightweight alternative achieving competitive performance
puter vision [14, 27, 39]. However, adapting these mod- with minimal resource consumption. DiffFit [36] extends
els for specific tasks often demands significant computa- this method by adding a scaling factor to linear layers and
tional power and extensive labeled data, making their de- also updating normalization layers, enabling rapid adaptaployment challenging for many applications. To mitigate tion of large pre-trained diffusion models to new domains.
theseissues,ParameterEfficientFine-Tuning(PEFT)meth- These methods significantly speed up training and reduce
ods[11,12,15,20,36,41]haveemergedasapromisingap- modelstoragerequirements, allowingpractitionerstofineproach to modify pre-trained models with minimal adjust- tune models effectively without extensive retraining of all
1
5202
raM
11
]VC.sc[
1v33380.3052:viXra

<!-- Page 2 -->

parameters. Yet, because weight matrices are not changed 2.RelatedWork
they may not reach the performance achieved by other
PEFT methods aim to adapt large pre-trained models for
methods,suchasLow-RankAdaptation(LoRA)[11,28].
specific downstream tasks by injecting a small number of
learnable parameters while freezing the majority of the
LoRA [11] and its variants [6, 9, 12, 15, 19, 20] intromodel’s parameters. This approach addresses the resource
duce low-rank matrices for model weight updates during
inefficiencyassociatedwithfullfine-tuningmethods,where
fine-tuning, enabling efficient training with fewer parameallmodelparametersaretunedforthenewtask.
ters, see Figure 1 (left). This approach not only enhances
the adaptability of large models but also reduces training
Variousstrategiesareemployedtointegratelearnablepatime and mitigates overfitting. Compared to BitFit, LoRA
rameters in PEFT. For instance, Adapter [10] methods inachievesstrongerperformanceincertaintasksanddemontroduce small, fine-tunable modules across different layers
stratesrobustgeneralizationcapabilities[31,37]. ThisperofTransformermodels,optimizingonlythesenewmodules
formance boost, however, requires more trainable paramefordownstreamadaptation. Prompt-tuning[17]andPrefixters,whichhasbeenshowntocausetraininginstabilityand
tuning [18] involve inserting a set of trainable tokens into
slowerconvergence[5]. Additionally,Puetal.[28]observe
the input layer of Transformers, focusing training efforts
thatLoRAisrobusttoparameterreductionfortextclassifionthesetokensonly. Morerecently,LoRA[11]reparamecationandgenerationtasks,allowingforreductionsbeyond
terizescertainpre-trainedweightsusinglow-rankmatrices,
theoriginalproposedones.Thisraisesthequestion:canwe
tuningonlytheseadditionalbranchestoadapttonewtasks.
maintain or improve performance while reducing LoRA’s
BitFit[41]proposestofine-tuneonlybiasterms,minimiztrainableparameterstolevelscomparabletoBitFit?
ing the number of trainable parameters. Although updatingonlyafractionoftheparameters, thesePEFTmethods

### Inthiswork,wepropose1LoRA,amethodcenteredon

achieve comparable or even superior performance to full
very low-rank adaptation, as depicted in Figure 1. We refine-tuningapproaches.
ducetheparametercounttomatchthatofBitFit[41],making it significantly lower than that required by other low- WhilePEFTmethodswereinitiallydevelopedwithinthe
rankadaptationmethods. 1LoRAappliesapredefinednon- naturallanguageprocessingdomain,recentworkshaveextrainable function for input compression, i.e. the sum over tendedtheirapplicationtocomputervisiontasks.Forexamallinputfeaturesxandutilizesasingletrainablevectorper
ple,[42]applyLoRAontheSegmentAnythingmodel[14],
layerfordecompression. Aswedemonstrateinourexten- and DiffFit [36] transfers BitFit to fine-tune the diffusion
sive, comparative experiments 1LoRA provides enhanced model. Moreover, PEFTmethodshaverecentlygainedinperformanceandmemoryefficiencyindifferenttasks. terestforsubspaceBayesianinferenceinlarge-scaleTransformers[23,26,38],demonstratingtheeffectivenessofthis

### Ourcontributionscanbesummarizedasfollows:

efficienttuningparadigmacrossmultipledomains.
• Wepropose1LoRA,averylow-rankadaptationmethod

## VeryLow-RankAdaptation

whichfixesthecompressionmechanismtoasimplefeaturesumandavectorofdparametersfordecompression,

### In this section, we first analyze existing PEFT methods in

wheredisthenumberofoutputfeatures,significantlyreregards to their fine-tuning approach and number of trainducingthenumberoftrainableparameters.
able parameters. We then motivate and describe techni-
• Duetoitslowmemoryfootprintattrainingtime,1LoRA
cal details of our memory efficient very-low rank adaptaenables fine-tuning across more layers in larger models tionmethod,1LoRA.Finally,wecompareourmethodwith
(e.g.,LLaMA27and13billioninourexperiments),disother methods in terms of the number of parameters and
tributingadjustmentsacrossmultiplelayersinsteadoffocomputationalandmemoryefficiency,respectively.
cusing solely on limited ones (e.g. the attention layers),
therebyachievingenhancedperformance. 3.1.PEFTmethods
• 1LoRAaddsnooverheadatinferencetime,astheupdate
We start by reviewing the technical details of state-of-the-
∆W canbemergedwiththeinitialweightmatrixW in
0 art PEFT methods, analyzing in particular their computathesamewayase.g.doneinLoRA[11].
tionalandmemoryrequirements. Weprovideanoverview
• Ourmethodissimpletoimplement,makingitaccessible
foreasycomparisoninTable1.
forpracticaldeployment.
• We conduct extensive empirical evaluations demonstrating that 1LoRA outperforms state-of-the-art methods in LoRA [11]wasoneofthefirstmethodsproposedforpatermsofeffectiveness,andparameter,memoryandcom- rameterefficientfine-tuning. Insteadoffine-tuningtheenputationalefficienciesacrossmultipletasksanddatasets. tireparametermatrixW ∈ Rd×k,LoRAfine-tunesanad-
0
2

<!-- Page 3 -->

Table1. AnalysedPEFTmethods: numberoftrainableparame- (RoPEbased)’isaversionaccordingtoEq.9in[12]where
tersinthe”verylo √ w-rankregime”withr =1(LoRA,VeRAand the features are reshaped into a new axis as compression,
DoRA)andrˆ=⌊ d⌋(MoRA).
processed, and then reshaped back. We name these methodsMoRA andMoRA ,respectively.
1 6

### Method Equation #Params×

BitFit [41]isoneofthefirstPEFTmethods,proposingto

### Linear

fine-tuneonlythebiasesβ ∈Rdofapre-trainedmodel.
LoRA[11] W x+BAx k+d
0

### DiffFit [36] extends BitFit to diffusion models by in-

DoRA[20] W 0 x+m ||W W 0 0 + + B B A A ||c x d+k+d troducing a scaling vector γ ∈ Rd. As a result, this
VeRA[15] W x+bBdAx 1+d approach adds an additional parameter that requires fine-
0
tuning. Moreover, DiffFit trains the normalization layers

### MoRA [12] W x+f (Mf (x)) rˆ2

1,6 0 d c andtheclassembedding,ifpresentinthemodel.

### BitFit[41] W x+β d

0 Inthispaper,weexplorethe”verylow-rankregime”,where
DiffFit[36] γ(W x+β),norms >2d weusethesmallestamountofparametersforeachstate-of-
0
the-art method. We notice that BitFit [41] and VeRA [15]
1LoRA W x+b1Tx d
0 are the methods that use the least parameters in this sce-
All W 0 x+β,norms >k×d+d nario,withdand1+dperlayer,whentherankisr =1.All
other methods use more parameters. VeRA smartly shares
theconstantrandommatricesAandBacrossmoduleswith
ditiveshiftmatrix∆W ∈Rd×k asfollows: thesameshapetoreducecomputation,however,itstilluses
considerable memory for matrix storage. BitFit, on the
o=W x+∆Wx=(W +∆W)x (1)
0 0 otherhand, onlyfine-tunesthebiastermsthatremainconstant across inputs and therefore lack generalization capawhere x ∈ Rk and o ∈ Rd are input and output features,
bilities. Furthermore,wenoticethatMoRA[12]hasmemrespectively. Weunderlinesymbolsindicatingtrainablepaory and computational inefficiencies due to the grouping
rameterstodistinguishthemfrompretrained,frozenparamand duplication operations, whereas other state-of-the-art
eters. LoRAdecomposestheshiftmatrix∆W bytworect-
LoRAmethodsheavilyrelyonthedecompositionmatrices
angularmatrices:
AandB,whichrequiresthemtouseadditionalmemory.
∆W =BA, withA∈Rr×k,B ∈Rd×r. (2) 3.2.1LoRA
MatrixAreducestherankofinputfromk tor andmatrix Toreducethememoryconsumptionandtoallowforbetter
Bdecompressesittothesizeofoutputd. scaling to big models, we adopt a very low rank regime.
Concretely, we propose to compress the input features to

### DoRA (weight-decomposed low-rank adaptation) [20]

their sum (cid:80)k x . This sum can be expressed as 1Tx,
builds on LoRA and proposes to decompose the pre- i=1 i
trained matrices into magnitude m ∈ Rd and direction where 1 is the main diagonal of the all-positive quadrant.
Ourintuitionisbasedonthefactthattypicalnon-linearities
(W +BA)/(||W +BA|| ). Here,thenormisdefinedas
0 0 c (e.g.ReLU)movefeaturestowardsthisquadrant. Thus1is
vector-wisenormofamatrixacrosseachcolumn.
a good candidate for a vector strongly correlating with the
VeRA (Vector-based Random-matrix Adaptation) [15] inputswhenwehavethispriorknowledge,anditisasgood
buildsontopofLoRAusingfixedrandomcompressionand asanyotherrandomvectorwhenwedonot.
decompression matrices (A and B), where the only trainable parameters are two vectors (d ∈ Rr and b ∈ Rd), re- OurapproachcanbeviewedanextremecaseofMoRA
[12]whichcompressestheinputfeaturesbycomputingthe
spectivelyafterthecompressionanddecompression.
sum within specific groups of features and decompresses
MoRA [12], similar to VeRA, also uses fixed compres- them by duplicating their outputs. Importantly, in contrast
sionf
c
anddecompressionf
d
schemes,whileonlylearning toMoRA,1LoRAusesasingletrainablevectorbofdpathe inner low-rank squared matrix M ∈ Rrˆ×rˆ, where the rametersfordecompression,therebyretainingperformance
(cid:112)
rankisrˆ=⌊ (k+d)r⌋. Theauthorsof[12]proposetwo in fine-tuning. Using vector 1 of length k containing only
versions, named types 1 and 6 in their Python code1. The ones,theshiftmatrixcanbewrittenas
version’type1(Sharing)’isaccordingtoEq.6in[12]and
usesasumwithingroupsoffeaturesascompressionandthe ∆W =b1T 1∈{1}k×1,b∈Rd×1 (3)
decompression is a copy of learned features. The ’type 6

### Figure 1 depicts 1LoRA in comparison to LoRA [11]. In

1https://github.com/kongds/MoRA/ practice,1LoRAonlyintroducesatrainablevectorofdpa-
3

<!-- Page 4 -->

rameters per layer. The compression can be implemented Table2. RMSE(↓)andAbsRel(↓)ofDepthAnythingmodelprein PyTorch [25] as a sum over the features, removing the trained on KITTI and fine-tuned to NYU using PEFT methods.

### LoRA,VeRAandDoRAwithrankr = 1,MoRAwithrankrˆ=

needforadditionalcompressionanddecompressionmatri- √
⌊ d⌋andd˜=rˆ2parameters.
ces, as in most state-of-the-art methods [11, 12, 15, 20].
Thismakesourmethodmorecomputationallyandmemory

## Kitti→Nyu Nyu→Kitti

efficient. Method

### RMSE(↓) AbsRel(↓) RMSE(↓) AbsRel(↓)

Forfastandmemoryefficientinference,weightscanbe MoRA1 0.248
±0.00066
0.0670
±0.00018
2.509
±0.00455
0.0587
±0.00011
mergedastherightsideinEquation(1),i.e.thefine-tuned MoRA6 0.277 ±0.00021 0.0774 ±0.00009 2.971 ±0.00239 0.0739 ±0.00009

### LoRA 0.250 0.0678 2.353 0.0583

weight matrix W is given as W := W +∆W. In our ±0.00087 ±0.00028 ±0.00315 ±0.00010
ft ft 0 VeRA 0.244 0.0668 2.304 0.0577
experiments,thisefficientimplementationhasbeenapplied DoRA 0.249 ±0.00059 0.0675 ±0.00013 2.345 ±0.00524 0.0581 ±0.00013
±0.00088 ±0.00031 ±0.00275 ±0.00004
tothecompetitorsLoRA,MoRA,andDoRA[11,12,20]. BitFit 0.349 0.1015 4.806 0.1271
±0.00073 ±0.00022 ±0.00392 ±0.00027

### DiffFit 0.314 0.0895 3.904 0.0988

3.3.1LoRAMethodAnalysis 1LoRA0.238 ±0.00078 0.0647 ±0.00030 2.203 ±0.00539 0.0533 ±0.00024
±0.00050 ±0.00010 ±0.00780 ±0.00025

### All 0.210 0.0571 1.916 0.0463

Our method relates to LoRA [11] with rank r = 1 which ±0.00064 ±0.00033 ±0.00303 ±0.00010
fine-tunes the low-rank matrices A and B. Compared to
LoRA, 1LoRA uses k fewer parameters per layer (see Ta-
DepthAnything [39], Image Classification with ViT-Base
ble 1), while removing the need for the matrices A and
[7], Mathematical Reasoning with LLaMA2 7b and 13b
B. MoRA (Eq. 6, [12]) introduces constant, non-trainable
[34], and Image Generation with DiT-XL-2-256x256 [27].
compressionanddecompressionfunctions: asumoverfea-

### For each method we use the lowest amount of parameters

ture groups for compression and a duplication of learned
perlayer. Wecompare1LoRAwithLoRA(r = 1),VeRA
featuresfordecompression. Ourapproachgoestothemost √
(r = 1),DoRA(r = 1),MoRA(rˆ= ⌊ d⌋)types1and6
extremecase,groupingfeaturesbysummingacrossasingle
(see Section 3.1), BitFit and DiffFit. We report results in
group that includes all features. Simultaneously, it elimiformsoftablesandbubbleplots, wherethemeanof4difnates the need for copying learned features by introducing
ferentindependentrunsisreportedforeachmethod.Ineach
the vector b, which scales the feature sum into d parameplot, we report the best mean evaluation metrics as y-axis,
ters during decompression. Although MoRA can be made
comparableto1LoRAintermsofparametersbyusingrank andtheirrequiredtotal(trainingandvalidation)wallclock
√
rˆ = ⌊ d⌋, 1LoRA is more computationally efficient as it time as x-axis, GPU (A100 40GB) memory consumption
as bar plot, and number of trainable parameters as bubble
avoidstheneedforgroupingfeatures,learningtheinnerfeaarea. Note that parameters are only a proxy for memory
tures,andcopyingthembacktomatchtherequiredshape.
consumption,whichcanbehigherdependingoncomputa-
Among low-rank adaptation methods, only VeRA has tionalgraphcomplexity. Wereportmetrics’standarddevia comparable number of parameters. However, it uses ationsinthetableandplots(aserrorbars).
random projection matrices, making the method more
memory-hungry, initialization-dependent, and less inter- 4.1.MonocularDepthEstimation
pretable. Bycontrast,usingthefeaturesumasinputforthe
As first experiment, we investigate the Monocular Depth
trainabledecompression,1LoRAsuggeststhatitsufficesto

### Estimation (MDE) fine-tuning task. Here, we start from a

learn to shift the pre-trained parameters by scaled feature
pre-trained metric depth model and fine-tune it to a new
sumofsamplesdrawnfromadatasettolearnthenewtask.
dataset without introducing new untrained modules like
adapters. We usethe model and training settings of Depth
In comparison to BitFit, which only fine-tunes the biasesβ,1LoRAcanbetterlearnfromthedataasitusesthe Anything [39], which are based on DINOv2 [24], MiDaS
[3, 29], DPT [30] and ZoeDepth [2]. We adopt widely
sum of the features, resulting in better performance, while
usedMDEbenchmarkdatasets: NYU(indoor)[22],KITTI
slightly sacrificing training speed, see experiments in Sec-
(driving) [8] and DIODE (outdoor) [35]. We test the foltion 4. Lastly, our method is complementary to state-oflowingfine-tuningcases:fromNYUtoKITTI,fromKITTI
the-art methods that fine-tune additional terms, like biases
to NYU, from NYU to DIODE Outdoor, from KITTI to
(BitFit [41]) or normalization layers (DiffFit, [36]), and to
DIODE Outdoor. Table 2 shows the Root Mean Squared
methodsbuildingontopofLoRA[6,9,11,19,20].
Error (RMSE) and Absolute Relative Error (AbsRel) for
thefirsttwocases,respectively. Here,1LoRAoutperforms

## Empiricalevaluation

all the competitors and is the closest to fine-tuning the en-
Webenchmark1LoRAagainststate-of-the-artPEFTmeth- tire model. Additionally, Figure 2a and Figure 2b show
ods in the ”very low-rank regime” on multiple fine-tuning thetrainingtime,numberofparametersandGPUmemory
tasks and models: Monocular Depth Estimation with needed to achieve the minimum Root Mean Square Error
4

<!-- Page 5 -->

(a)KITTI→NYU. (b)NYU→KITTI.
(c)KITTI→DIODEOutdoor. (d)NYU→DIODEOutdoor.
Figure2. RMSE(↓)ofpre-trainedDepthAnythingmodelfine-tunedusingPEFTmethods. Bubblesizeisproportionaltothenumberof
parameters,exceptfor”All”,whichiscappedduetospacelimitations.Bottomleft(andsmallestbubble)isbetter.
(RMSE) for each method in the first two cases. From the 4.2.MathematicalReasoning
figure,itemergesthatnotonlyisourmethod theclosest

### We study the Mathematical Reasoning task, fine-tuning 7

to full fine-tuning , but it is also (1) faster than all combillionand13billionparameterspre-trainedLLaMA2[34]
petitors but BitFit , (2) it is the method with the lowest
modelstoMeta-Math[40]. Weusethefine-tuningsettings
memory consumption together with MoRA , (3) it is the
of MoRA [12], where for the 7 billion model we use 16
method fine-tuning the least parameters together with Bit-
GPUs with 4 images each and a total batch size of 128
Fit,MoRAandVeRA .
with gradient accumulation, and for the 13 billion model
weuse64GPUswith2imageseach. Inaddition, wesplit
thedatasetinto80%fortrainingand20%forvalidation.

### Figure2candFigure2dshowresultsforthefine-tuning

cases from KITTI to DIODE Outdoor and from NYU to
DIODEOutdoor,respectively. Thefiguresconfirmthatour Figure 3 shows that 1LoRA outperforms all methmethod outperformsthecompetitorsintermsofefficacy ods, except LoRA , in terms of validation loss, while usand computational efficiency, in terms of memory usage it ingcompetitivecomputationaltime,parameterandmemory
isthebestonparwithMoRA ,andintermsofparameters budgets. LoRA achieves a slightly lower validation loss,
itisagainthebestonparwithBitFit ,MoRAandVeRA . whileusingmorethan90%oftheGPUmemorycompared
5

<!-- Page 6 -->

Figure3.Validationlossofpre-trainedLLaMA-27bfine-tunedto Figure4. Validationlossofpre-trainedLLaMA-213bfine-tuned
Meta-Math.Bubblesizeisproportionaltothenumberofparame- toMeta-Math. Missingcompetitorscannotbefine-tunedwiththe
ters.Bottomleft(andsmallestbubble)isbetter. givenmemorybudget. Bubblesizeisproportionaltothenumber
ofparameters.Bottomleft(andsmallestbubble)isbetter.
tolessthan80%of1LoRA.Ontheotherhand,whenlimiting the memory budget of LoRA by applying it only to Food-101[4]usingthefine-tuningsettingsofDiffFit [36].
the attention layers, here named LoRA (QKV) , 1LoRA Werunallexperimentswitha24htimebudgetandwereresultsinabetterperformancewhilestillusingslightlyless portresultsofasinglerunpermethod,giventhehighcom-
GPU memory, showing that 1LoRA is more memory effi- putationalrequirements.Figure5showsthat1LoRA outcientthanLoRA.Moreover,ourmethodisonlyslowerthan performs all competitors in terms of FID, while being the
BitFit ,DiffFit andLoRA(QKV),whilebeingbetterin most memory efficient method. Notice that 1LoRA also
termsofquality. Intermsoftrainableparameters, 1LoRA converges faster than LoRA and MoRA (6) . In addiisagaincomparabletoBitFitandMoRA ,andonlysecond tion, as for previous experiments, 1LoRA has the lowest
to LoRA (QKV), which is applied to fewer layers. Lastly, numberofparameterstogetherwithBitFit ,MoRA and
in terms of memory, 1LoRA is the second most efficient VeRA . Lastly, DoRA cannot be fine-tuned with the
method,almostonparwiththefirstone,BitFit. samefine-tuningsettingsasitgoesoutofmemory.
Giventhat1LoRAismorememoryefficientthanLoRA 4.4.ImageClassification
and LoRA (QKV), 1LoRA can be applied to more layers
We compare 1LoRA and competitor methods on Image
andmodulesthanLoRAinbiggermodels,allowingamore
Classification. WeuseaViT-Base[7]modelpre-trainedon
fine-grainedfine-tuningthanLoRA,whichneedstobelim-

### ImageNet-21k[32]andwefine-tuneittoCIFAR10andCI-

ited to specific layers. Figure 4 exemplifies this 1LoRA
FAR100[16], respectively, usingAdamW[21]withlearnbenefit for fine-tuning a LLaMA-2 13b. LoRA cannot be
ingrate0.00002,weightdecay0.01,batchsize10,random
appliedtoalllinearlayersasitwouldrequiretoomuchGPU
resizedcropto224andrandomhorizontalflip.
memory,thereforeithastobelimitedtospecificlayers(Q,
K,Vinthiscase).1LoRAcanbeappliedtoalllinearlayers

### Figure6andFigure7showtheresultsforCIFAR10and

withasimilarmemorybudget,whileenablingabetterper-

### CIFAR100, respectively. From the figures, it emerges that

formance. Infact,here,1LoRAoutperformsallapplicable 1LoRA isthesecondfastestmethodafterBitFit ,while
competitorswhileconsumingacomparablememorybudget
being slightly better in terms of accuracy. LoRA and
andonlybeingslightlyslower.Wereportvisualcomparison
DoRA are the methods achieving the closest accuracy
of1LoRAandLoRAQKVinAppendixC.
to fine-tuning the entire model, however they are also the
slowestmethods, evenslowerthanfullfine-tuning. Inthis

### ImageGeneration

experiment,DiffFit isslightlybetterthan1LoRA ,how-
We investigate the use of PEFT methods for diffusion ever it is also slightly slower and it uses more parameters
model fine-tuning for image-generation. We fine-tune an andmemory. Itisworthnotingthat1LoRAiscomplemen-
ImageNet-21k [32] pre-trained DiT-XL-2-256x256 [27] to tary to BitFit and DiffFit . They can be combined in
6

<!-- Page 7 -->

Figure5.FIDofpretrainedDiTfine-tunedtoFood-101.Notethat Figure 7. Accuracy (↑) of ViT-Base model pre-trained on
DoRAismissingasitcannotbefine-tunedwiththegivenmemory ImageNet-21kandfine-tunedtoCIFAR100. Bubblesizeisprobudget. Bubblesizeisproportionaltothenumberofparameters. portionaltothenumberofparameters,exceptfor”All”,whichis
Bottomleft(andsmallestbubble)isbetter. capped.Topleft(andsmallestbubble)isbetter.

## Ablations


### Complementarymethods

We investigate all possible combinations of BitFit, DiffFit
and1LoRA,includingindividualcomponents(thebiasesβ,
thescalingfactorsγ, andthenorms, seeTable1), inorder
tounderstandwhichmodulesimpactfine-tuningmost. We
runexperimentsforImageClassification,fine-tuningaViT-
Base from ImageNet-21k [32] to CIFAR10. We adopt the
trainingconfigurationsdescribedinprevioussections.
Figure8reportsresultsfortheImageClassificationtask
onCIFAR10,wherethereisaclearadvantageinpreferring
fine-tuningofnormalizationlayers overbiases orscalingfactors . Combiningthesemoduleswith1LoRAleads
tothebestresults, comparabletoDiffFit , butwithfewer
parameters,lessmemoryconsumptionandsmallercompu-
Figure 6. Accuracy (↑) of ViT-Base model pre-trained on
tationalcost. Othercombinationsdonotseemtobringad-
ImageNet-21k and fine-tuned to CIFAR10. Bubble size is proditionalperformancegains. Wereportadditionalresultsfor
portionaltothenumberofparameters,exceptfor”All”,whichis
capped.Topleft(andsmallestbubble)isbetter. thisablationontheMDEtaskinAppendixB.1.

### PCAanalysis

many ways, as we study in Section 5.1. Here, the figures WeperformedPCAontheweightupdatesforourMonocadditionally report the most fruitful combination, 1LoRA ular Depth Estimation and Classification experiments. We
(norms) , i.e. 1LoRA and unfrozen normalization layers. compare principal components (PCs) of a full-rank update
This combination is slightly better, being more parameter againstarandom,summation(1LoRA)andlearned(LoRA,
andmemoryefficientthanDiffFit. InSection5.1,westudy r = 1)compressionvectorandpresentresultsinFigure9.
further combinations. Lastly, in order to show that fine- ForMDE,alignmentofallcompressionvectorsintermsof
tuningthebackboneleadstosignificantadvantages,were- absolute cosine similarity to the PCs is mostly low, except
portaccuraciesforthefine-tuningoftheclassificationhead forthesecondMLPlayers. Forclassification,asimilarpatonly,onCIFAR10(90%)andCIFAR100(66%). ternisvisibleexceptthatthelearnedcompressionachieves
7

<!-- Page 8 -->

1
0
Figure 8. Accuracy (↑) of ViT-Base model pre-trained on

### ImageNet-21kandfine-tunedtoCIFAR10,usingallcombinations

of 1LoRA, BitFit and DiffFit, including individual components
(biases β, scaling factors γ and normalization layers, norms).
Bubblesizeisproportionaltothenumberofparameters. Topleft
(andsmallestbubble)isbetter.
notably higher similarity, especially also for the first MLP
layer. Interestingly, the second MLP layer of a ViT block
is the only layer in the architecture, where features went
throughaGELUactivationfunctionrightbefore-hand. Effectively, the GELU activation concentrates the incoming
features towards the positive “quadrant”, thus summation
(i.e. the 1 vector) is unlikely to be orthogonal to those incomingfeatures,andorthogonalitymaybeanissuetoperformanceasitsuppressestheincomingfeature.

### As to why 1LoRA yields good performance, we argue

that summation seems to be a good a priori guess for the
PCsoflinearlayersthatarefedwithGELUorReLUactivations. For the other layers, a fixed summation compressionperformssimilarlytoarandomone. InAppendixB.2
we compare results for 1LoRA with fixed summation and
randomcompression,showingthattheformer(i.e.1LoRA)
is at least as good as a random compression, while being
faster. Ontheotherhand,alearnedcompressiononlyleads
toslightlybetteralignmentwiththePCs(cf.learnedcompressioninFigure9),whilerequiringdoubletheamountof
parametersandmorememory.
Inconclusion,giventhesimilarityincompressionquality, using 1LoRA is preferable for memory and computationalefficiencies.

## Conclusion

PEFT methods have transformed the approach to finetuning large models for downstream tasks by enabling the

## Slc

QKV Proj. MLP L1 MLP L2
1
0
101 103

## Edm

101 103 101 103 101 103
ytiralimiS
.soC
.sbA
Summation Random Learned

### Principal Component

Figure9.AlignmentbetweenPCs(sortedbysingularvalues)ofa
fullweightupdateandourcandidatecompressionvectors.
adjustment of significantly fewer parameters than those in
the original model matrices. In this work, we study the
”very low rank regime”, where we fine-tune the lowest
amount of parameters per layer for each considered PEFT
method. Inspired by LoRA, VeRA, and the recent MoRA,
wepropose1LoRA,acompute,parameterandmemoryefficient fine-tuning method which uses the feature sum as
compression,andatrainablevectorasdecompression. Differently from state-of-the-art PEFT methods, 1LoRA uses
onlydparametersperlayer,reducingthememoryfootprint
andthecomputationalcost.
Moreover, by using the feature sum, instead of random projection, as input for the trainable decompression,
1LoRAmakesonestepforwardininterpretablefine-tuning,
suggestingthatlearningtoshiftthepre-trainedparameters
by scaled feature sum coming from samples drawn from a
newdatasetisenoughtolearnthenewtask.
Weextensivelyevaluateourmethodagainststate-of-theartPEFTmethodsonmultiplefine-tuningtasksandmodels,
namelyMonocularDepthEstimationwithDepthAnything,
ImageClassificationwithViT-Base,MathematicalReasoningwithLLaMA27band13b,andImageGenerationwith

### DiT-XL-2-256x256. We observe that our method not only

outperforms state-of-the-art methods, but is also more parameter,memoryandcomputationallyefficient.

### Byreducingthenumberoftrainableparametersperlayer

to d, 1LoRA enables the fine-tuning of big models (e.g.

### LLMs with billions of parameters), where other methods

cannotbeappliedduetotheirlargermemoryneeds. Additionally, we show that our method can be applied to more
layers on bigger models, outperforming other competitors
whileusingsimilarmemorybudget.
With this paper, we demonstrate the benefit of the very
low-rankregime,wherethelowestamountofparametersis
fine-tuned,whilemaximizingtheperformance.
8

<!-- Page 9 -->

Acknowledgements A.Q.andR.D.P.werefundedbythe [13] StefanKesselheim,AndreasHerten,KaiKrajsek,JanEbert,
Helmholtz School for Data Science in Life, Earth, and Jenia Jitsev, Mehdi Cherti, Michael Langguth, Bing Gong,
Energy (HDS-LEE). The authors gratefully acknowledge ScarletStadtler,AmirpashaMozaffari,etal.Juwelsbooster–
theGaussCentreforSupercomputinge.V.(www.gauss- asupercomputerforlarge-scaleairesearch. InInternational
centre.eu) for funding this project by providing com- Conference on High Performance Computing, pages 453–

### Springer,2021. 9

puting time through the John von Neumann Institute for
[14] AlexanderKirillov,EricMintun,NikhilaRavi,HanziMao,

### Computing (NIC) on the GCS Supercomputer JUWELS

ChloeRolland,LauraGustafson,TeteXiao,SpencerWhite-
[13]atJu¨lichSupercomputingCentre(JSC).
head,AlexanderCBerg,Wan-YenLo,etal. Segmentanything. InProceedingsoftheIEEE/CVFInternationalCon-

### References

ferenceonComputerVision,pages4015–4026,2023. 1,2
[1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ah- [15] DawidJanKopiczko,TijmenBlankevoort,andYukiMarkus
mad,IlgeAkkaya,FlorenciaLeoniAleman,DiogoAlmeida, Asano. Vera:Vector-basedrandommatrixadaptation. arXiv
JankoAltenschmidt, SamAltman, ShyamalAnadkat, etal. preprintarXiv:2310.11454,2023. 1,2,3,4
Gpt-4 technical report. arXiv preprint arXiv:2303.08774, [16] AlexKrizhevsky,GeoffreyHinton,etal. Learningmultiple
2023. 1 layersoffeaturesfromtinyimages. Citeseer,2009. 6
[2] Shariq Farooq Bhat, Reiner Birkl, Diana Wofk, Peter [17] BrianLester,RamiAl-Rfou,andNoahConstant.Thepower
Wonka, and Matthias Mu¨ller. Zoedepth: Zero-shot trans- ofscaleforparameter-efficientprompttuning.arXivpreprint
ferbycombiningrelativeandmetricdepth. arXivpreprint arXiv:2104.08691,2021. 2
arXiv:2302.12288,2023. 4 [18] Xiang Lisa Li and Percy Liang. Prefix-tuning: Optimiz-
[3] ReinerBirkl,DianaWofk,andMatthiasMu¨ller. Midasv3. ing continuous prompts for generation. arXiv preprint
1–a model zoo for robust monocular relative depth estima- arXiv:2101.00190,2021. 2
tion. arXivpreprintarXiv:2307.14460,2023. 4 [19] Yang Li, Shaobo Han, and Shihao Ji. Vb-lora: Extreme
[4] Lukas Bossard, Matthieu Guillaumin, and Luc Van Gool. parameter efficient fine-tuning with vector banks. arXiv
Food-101–miningdiscriminativecomponentswithrandom preprintarXiv:2405.15179,2024. 2,4
forests. InEuropeanConferenceonComputerVision,2014. [20] Shih-Yang Liu, Chien-Yi Wang, Hongxu Yin, Pavlo
6 Molchanov, Yu-Chiang Frank Wang, Kwang-Ting Cheng,
[5] Guanzheng Chen, Fangyu Liu, Zaiqiao Meng, and Shang- andMin-HungChen. Dora: Weight-decomposedlow-rank
song Liang. Revisiting parameter-efficient tuning: Are we adaptation. arXivpreprintarXiv:2402.09353,2024. 1,2,3,
reallythereyet? arXivpreprintarXiv:2202.07962,2022. 2 4
[6] Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke [21] ILoshchilov. Decoupledweightdecayregularization. arXiv
Zettlemoyer. Qlora: Efficientfinetuningofquantizedllms. preprintarXiv:1711.05101,2017. 6
Advances in Neural Information Processing Systems, 36, [22] Pushmeet Kohli Nathan Silberman, Derek Hoiem and Rob
2024. 2,4 Fergus. Indoor segmentation and support inference from
[7] Alexey Dosovitskiy. An image is worth 16x16 words: rgbdimages. InECCV,2012. 4
Transformersforimagerecognitionatscale. arXivpreprint [23] Emre Onal, Klemens Flo¨ge, Emma Caldwell, Arsen
arXiv:2010.11929,2020. 4,6 Sheverdin,andVincentFortuin. Gaussianstochasticweight
[8] AndreasGeiger, PhilipLenz, ChristophStiller, andRaquel averagingforbayesianlow-rankadaptationoflargelanguage
Urtasun. Visionmeetsrobotics: Thekittidataset. Interna- models. In Sixth Symposium on Advances in Approximate
tionalJournalofRoboticsResearch(IJRR),2013. 4 BayesianInference-NonArchivalTrack,2024. 2
[9] Han Guo, Philip Greengard, Eric P Xing, and Yoon Kim. [24] Maxime Oquab, Timothe´e Darcet, The´o Moutakanni, Huy
Lq-lora: Low-rank plus quantized matrix decomposition Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez,
for efficient language model finetuning. arXiv preprint DanielHaziza,FranciscoMassa,AlaaeldinEl-Nouby,etal.
arXiv:2311.12023,2023. 2,4 Dinov2:Learningrobustvisualfeatureswithoutsupervision.
[10] NeilHoulsby,AndreiGiurgiu,StanislawJastrzebski,Bruna arXivpreprintarXiv:2304.07193,2023. 4
Morrone,QuentinDeLaroussilhe,AndreaGesmundo,Mona [25] Adam Paszke, Sam Gross, Soumith Chintala, Gregory
Attariyan, and Sylvain Gelly. Parameter-efficient transfer Chanan, Edward Yang, Zachary DeVito, Zeming Lin, Allearning for nlp. In International conference on machine banDesmaison, LucaAntiga, andAdamLerer. Automatic
learning,pages2790–2799.PMLR,2019. 2 differentiationinpytorch. InNIPS2017AutodiffWorkshop,
[11] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen- 2017. 4
Zhu,YuanzhiLi,SheanWang,LuWang,andWeizhuChen. [26] Richard D. Paul, Alessio Quercia, Vincent Fortuin, Katha-
Lora: Low-rankadaptationoflargelanguagemodels. arXiv rina No¨h, and Hanno Scharr. Parameter-efficient bayesian
preprintarXiv:2106.09685,2021. 1,2,3,4 neural networks for uncertainty-aware depth estimation,
[12] Ting Jiang, Shaohan Huang, Shengyue Luo, Zihan Zhang, 2024. 2
Haizhen Huang, Furu Wei, Weiwei Deng, Feng Sun, Qi [27] WilliamPeeblesandSainingXie. Scalablediffusionmodels
Zhang, Deqing Wang, et al. Mora: High-rank updat- with transformers. In Proceedings of the IEEE/CVF Intering for parameter-efficient fine-tuning. arXiv preprint nationalConferenceonComputerVision,pages4195–4205,
arXiv:2405.12130,2024. 1,2,3,4,5 2023. 1,4,6
9

<!-- Page 10 -->

[28] George Pu, Anirudh Jain, Jihan Yin, and Russell Kaplan. thepoweroflarge-scaleunlabeleddata. arXiv:2401.10891,
Empirical analysis of the strengths and weaknesses of peft 2024. 1,4
techniquesforllms.arXivpreprintarXiv:2304.14999,2023. [40] LonghuiYu,WeisenJiang,HanShi,JinchengYu,Zhengying
2 Liu,YuZhang,JamesTKwok,ZhenguoLi,AdrianWeller,
[29] Rene´ Ranftl, Katrin Lasinger, David Hafner, Konrad and Weiyang Liu. Metamath: Bootstrap your own mathe-
Schindler, and Vladlen Koltun. Towards robust monocular maticalquestionsforlargelanguagemodels. arXivpreprint
depthestimation:Mixingdatasetsforzero-shotcross-dataset arXiv:2309.12284,2023. 5
transfer.IEEEtransactionsonpatternanalysisandmachine [41] EladBenZaken,ShauliRavfogel,andYoavGoldberg.Bitfit:
intelligence,44(3):1623–1637,2020. 4 Simpleparameter-efficientfine-tuningfortransformer-based
[30] Rene´ Ranftl,AlexeyBochkovskiy,andVladlenKoltun. Vi- maskedlanguage-models.arXivpreprintarXiv:2106.10199,
sion transformers for dense prediction. In Proceedings of 2021. 1,2,3,4
theIEEE/CVFinternationalconferenceoncomputervision, [42] Zihan Zhong, Zhiqiang Tang, Tong He, Haoyang Fang,
pages12179–12188,2021. 4 and Chun Yuan. Convolution meets lora: Parameter effi-
[31] Olesya Razuvayevskaya, Ben Wu, Joa˜o A Leite, Freddy cientfinetuningforsegmentanythingmodel. arXivpreprint
Heppell,IvanSrba,CarolinaScarton,KalinaBontcheva,and arXiv:2401.17868,2024. 2
XingyiSong.Comparisonbetweenparameter-efficienttechniques and full fine-tuning: A case study on multilingual
newsarticleclassification. Plosone,19(5):e0301738,2024.
2
[32] Tal Ridnik, Emanuel Ben-Baruch, Asaf Noy, and Lihi
Zelnik-Manor. Imagenet-21k pretraining for the masses,
2021. 6,7
[33] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier

### Martinet,Marie-AnneLachaux,Timothe´eLacroix,Baptiste

Rozie`re, Naman Goyal, Eric Hambro, Faisal Azhar, et al.
Llama: Open and efficient foundation language models.
arXivpreprintarXiv:2302.13971,2023. 1
[34] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert,

### Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov,

Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al.
Llama2:Openfoundationandfine-tunedchatmodels.arXiv
preprintarXiv:2307.09288,2023. 4,5
[35] Igor Vasiljevic, Nick Kolkin, Shanyi Zhang, Ruotian Luo,
HaochenWang,FalconZ.Dai,AndreaF.Daniele,MohammadrezaMostajabi,StevenBasart,MatthewR.Walter,and
GregoryShakhnarovich. DIODE:ADenseIndoorandOutdoorDEpthDataset. arXive-prints,art.arXiv:1908.00463,
2019. 4
[36] Enze Xie, Lewei Yao, Han Shi, Zhili Liu, Daquan Zhou,
Zhaoqiang Liu, Jiawei Li, and Zhenguo Li. Difffit: Unlocking transferability of large diffusion models via simple parameter-efficient fine-tuning. In Proceedings of the
IEEE/CVF International Conference on Computer Vision,
pages4230–4239,2023. 1,2,3,4,6
[37] ChunleiXin, YaojieLu, HongyuLin, ShuhengZhou, Huijia Zhu, Weiqiang Wang, Zhongyi Liu, Xianpei Han, and

### Le Sun. Beyond full fine-tuning: Harnessing the power

of LoRA for multi-task instruction tuning. In Proceedings of the 2024 Joint International Conference on ComputationalLinguistics,LanguageResourcesandEvaluation
(LREC-COLING 2024), pages 2307–2317, Torino, Italia,

### ELRAandICCL. 2

[38] AdamX.Yang, MaximeRobeyns, XiWang, andLaurence

### Aitchison. Bayesianlow-rankadaptationforlargelanguage

models. InTheTwelfthInternationalConferenceonLearningRepresentations,2024. 2
[39] LiheYang,BingyiKang,ZilongHuang,XiaogangXu,Jiashi
Feng, andHengshuangZhao. Depthanything: Unleashing
10

<!-- Page 11 -->


### Supplemental Material

1LoRA: Summation Compression for Very Low-Rank Adaptation

### A.Algorithm


### As stated in the main paper, 1LoRA is straightforward to

implement.WeillustratethepythonimplementationinListing1.Inourwork,weappliedthe1LoRAmoduletoalllinearlayersinthemodel, excludingtheclassificationlayers,
whenpresent.
1 import torch
2 import torch.nn as nn
3
4 class ILoRA(nn.Module):
5 def __init__(self, linear):
6 super().__init__()
7 self.linear = linear
8 self.b = nn.Parameter(torch.zeros(self.
linear.out_features))
9
10 def forward(self, x):
11 ilora = self.b * x.sum(-1, keepdim=True)
12 return self.linear(x) + ilora Figure 10. RMSE (↓) of DepthAnything model pre-trained on
Listing1.Implementationof1LoRAinPython KITTIandfine-tunedtoNYU,usingallcombinationsof1LoRA,
BitFit and DiffFit, including individual components (biases β,
scalingfactorsγandnormalizationlayersnorms).Bubblesizeis
B.Ablations proportionaltothenumberofparameters.Bottomleft(andsmallestbubble)isbetter.

### B.1.Complementarymethods

We investigate all possible combinations of BitFit, DiffFit usingafixedsummationcompressionisatleastasgoodas
and1LoRA,includingindividualcomponents(thebiasesβ,
usingrandomcompression.
thescalingfactorsγ, andthenorms, seeTable1), inorder
tounderstandwhichmodulesimpactfine-tuningmost. We TableS1.(MDE)1LoRA:summationvsrandomcompression.
report experiments for MDE, fine-tuning DepthAnything
fromKITTItoNYU. dataset compression time RMSE(↓)
[min](↓)
Interestingly, Figure 10 shows that, for the MDE case,
summation 63 2.203±0.0078
only fine-tuning the normalization layers (norms, ) leads NYU→KITTI
tosuboptimalresults,whereascombiningitwith1LoRA random 65 2.239±0.0089
allowsittoachievesimilarresultsas1LoRA , butfaster. summation 65 0.238±0.0005

## Kitti→Nyu

Fine-tuning the biases alone (i.e. BitFit, ) achieves be- random 67 0.24±0.0002
low state-of-the-art performance, but combining it with summation 13 4.574±0.1217
1LoRA has the same effect as combining norms with KITTI→DIODEOut random 22 4.573±0.0582
1LoRA . Other combinations seem to lead to no addisummation 42 4.719±0.06
tionalbenefit,andonlyslowdownthefine-tuningprocess. NYU→DIODEOut
random 42 4.725±0.06
In general, any combination also increases the amount of
trainableparameters,and1LoRAalreadyachievesthebest

### B.3.Analysisofedgecases

resultswhileusingtheleastnumberoftrainableparameters
inthisexperiment. To explore edge cases, we analyzed the error distribution
andcalibrationoffullfine-tuning,LoRAr =1and1LoRA

### B.2.Summationvsrandomcompression

forourclassificationexperiments(Fig.11). Contrarytoex-
Here, wereportablationontheMDE(TableS1)taskcom- pectation, full fine-tuning seems to be more heavy-tailed
paring1LoRAwithfixedsummationandrandomcompres- in terms of error distribution than the very low-rank PEFT
sion. Resultsshowthatsummationisoverallslightlybetter methods. As for the calibration, again the very low-rank
in terms of performance or required time, suggesting that PEFT methods seem to slightly improve above full fine-
11

<!-- Page 12 -->

98.3% Acc. 1
98.2% Acc.
97.5% Acc.
2

## 361 Ece


## 365 Ece


## 0 0 0.359 Ece

90.4% Acc. 1
1 8 8 7 4 . . 1 7 % % A A c c c c . .

## 091 Ece


## 075 Ece


## 0 0 0.073 Ece

10 2 100 0.0 0.5 1.0
Log Validation Error Confidence

## 01Rafic


## 001Rafic

ycneuqerF ycaruccA

### LoRAQKV


### Full LoRA 1LoRA

The snowboard was originally priced at $100. The
50%discountbringsthepricedownto$100·0.5 =
$50. The 30% reduction brings the price down further to $50·0.7 = $35. Therefore, the price of the
snowboard afterthe Monday reduction is $35 .The
answeris: 35

### Question&Answer

Figure11. Errordistributionandcalibrationforclassificationexamples.
### Instruction:

### George went to a movie theater to see a movie. He

paid$16fortheticketanddecidedtobuysomenatuning, though the improvement – if any – is very much chos. The nachos were half the price of the ticket.
negligible. HowmuchdidGeorgepayintotalforthevisittothe
movietheater?
### Response:
C.Mathematicalreasoningvisualization Georgepaid$16fortheticket. Thenachoswerehalf
the price of the ticket, so they cost $16/2 = $8. In
WereportvisualizationforLLaMA213bfinetunedon80%
total,Georgepaid$16+$8=$24forthevisittothe
MetaMath, comparing 1LoRA and LoRA QKV. We use
movietheater.
randomsamplesfromourgeneratedvalidationsplit(20%)
ofMetaMath. Weuseblack,oliveandcyanboxestohighlighttheinputprompt(questionandanswer,whereonlythe
1LoRA
questionisgivenasinputandtheanswerservesasground
truth), the 1LoRA and LoRA QKV answers, respectively. Thenachoswerehalfthepriceoftheticket,sothey
Note that we omit “Below is an instruction that describes cost $16/2 = $8. Therefore, George paid a total of
a task. Write a response that appropriately completes the $16+$8=$24forthevisittothemovietheater.
request.”fromQ&Aboxesduetospacelimitations. ####24
Theansweris: 24

### Question&Answer

### Instruction: LoRAQKV

### On Friday, a snowboard originally priced at $100

wasdiscounted50%.OnMonday,thatsalepricewas Thenachoswerehalfthepriceoftheticket,sothey
reducedby30%. Indollars,whatisthepriceofthe cost$16/2=$8Intotal,Georgepaid$16+$8=$24
snowboardaftertheMondayreduction? forthevisittothemovietheater.
### Response: ####24
TheFridaysalepricewas$100×0.50 = $50. The Theansweris: 24

### Monday reduction is 30% of $50, so it is $50 ×

0.30 = $15. Therefore, the price of the snowboard
aftertheMondayreductionis$50−$15= $35 .The Question&Answer
answeris: 35.
### Instruction:
Ifab+bc+cd+da=30andb+d=5,whatisthe
valueofa+c?
1LoRA
### Response:
The Friday discount of 50% reduces the price to Wecanrewritethegivenequationasa(b+d)+c(b+
100−0.5(100)=50.TheMondayreductionof30% d) = 30. Using the second equation, we substitute
b+d = 5toget5a+5c = 30. Dividingbothsides
reducesthepricefurtherto50−0.3(50)= 35 .The
by5,wehavea+c= 6 . Theansweris: 6
answeris: 35
12

<!-- Page 13 -->

1LoRA 1LoRA
Wecanrewritetheequationab+bc+cd+da=30 To solve this problem, we need to determine the
as(a+c)(b+d) = 30. Substitutingb+d = 5,we value of x, which represents Phoebe’s current age.
have(a+c)(5) = 30. Dividingbothsidesby5,we Weknowthatin5years,Ravenwillbe4timesasold
geta+c= 6 . Theansweris: 6 asPhoebe. Therefore,Raven’sagein5yearswillbe
4 times Phoebe’s age in 5 years. Let’s break down
theinformationgiven: Raven’scurrentage: 55years
Phoebe’s current age: x years In 5 years, Raven’s
age: 55 + 5 = 60 years In 5 years, Phoebe’s age:
x + 5 years We can set up the equation as follows:
Raven’sagein5years=4*Phoebe’sagein5years
60=4*(x+5)Let’ssimplifyandsolveforx: 60=

### LoRAQKV

4x+20Toisolatex,wesubtract20frombothsides
Wecanrewritethegivenequationasa(b+d)+c(b+ of the equation: 60 - 20 = 4x + 20 - 20 40 = 4x To
d) = 30. Usingthegiveninformationthatb+d = solve for x, we divide both sides of the equation by
5, we have 2ab + 2cd = 30. We can rewrite this 4: 40/4=4x/410=xThevalueofxis10.
equationasab+cd=15. Sinceab+bc+cd+da= ####10
30, we can subtract ab+cd from both sides to get Theansweris: 10
bc+da = 15. Wecanalsorewritethisequationas
bc+da = 15. Since b+d = 5, we can substitute LoRAQKV
thisintotheequationtogetbc+da = 5. Now, we
To solve this problem, we need to determine the
cansolvefora+cbysubtractingaandcfromboth
value of x, which represents Phoebe’s current age.
sides: a+c=5. Therefore,thevalueofa+cis 5 .
We know that in 5 years, Raven will be 4 times as

### Theansweris: 5

old as Phoebe. Therefore, Raven will be 4x years
oldin5years. WealsoknowthatRaveniscurrently
55yearsold. Wecansetuptheequationasfollows:

### Raven’sagein5years=4*Phoebe’scurrentage55

= 4 * x Let’s simplify and solve for x: 55 = 4x To
isolatex, wedividebothsidesoftheequationby4:
55/4=4x/414=xThevalueofxis14.
Question&Answer
#### 14
### Instruction: Theansweris: 14
In 5 years, Raven will be 4 times as old as Phoebe.
IfPhoebeiscurrentlyxyearsold,Ravenis55years
old. Whatisthevalueofunknownvariablex?
### Response:

### To solve this problem, we need to determine the

value of x, which represents Phoebe’s current age.

### Let’sbreakdowntheinformationgiven: In5years,

Raven will be 4 times as old as Phoebe. Raven is
currently55yearsold. Wecansetuptheequationas
follows: Raven’s age in 5 years = 4 * Phoebe’s age
in5years(Raven’scurrentage+5)=4*(Phoebe’s
current age + 5) 55 + 5 = 4 * (x + 5) 60 = 4 * (x +
5) Let’s simplify and solve for x: 60 = 4x + 20 To
isolatex,wesubtract20frombothsidesoftheequation: 60-20=4x+20-2040=4xTosolveforx,
we divide both sides of the equation by 4: 40 / 4 =
4x/410=xThevalueofxis10.
#### 10
Theansweris: 10.
13

<!-- Page 14 -->


### D.Detailedresults

We report tables (from S2 to S12) illustrating the detailedresultsshowninthemainpaperasbubbleandbar
plots. For each column reporting a result, we highlight
thebestvalueinbold,thesecondbestinunderlinedand
thethirdinitalic.
method time RMSE(↓) memory params
[min](↓) [%](↓) (↓)
MoRA 69 0.248±0.00021 36 220.06K
1
MoRA 73 0.277±0.00066 36 217.44K
6

### BitFit 64 0.349±0.00073 40 221.18K

DiffFit 78 0.314±0.00078 40 321.54K

### LoRA 71 0.25±0.00087 41 393.22K


### VeRA 69 0.244±0.00059 40 221.28K

DoRA 104 0.249±0.00088 54 614.40K
1LoRA 65 0.238±0.0005 36 221.18K
All 83 0.211±0.00064 56 335.32M

### TableS2.TableforFigure2a

method time RMSE(↓) memory params
[min](↓) [%](↓) (↓)
MoRA 67 2.509±0.00455 36 220.06K
1
MoRA 71 2.97±0.00328 36 217.44K
6

### BitFit 61 4.806±0.00392 40 221.18K

DiffFit 66 3.904±0.00539 40 321.54K
LoRA 66 2.253±0.00315 41 393.22K

### VeRA 68 2.304±0.00524 40 221.28K

DoRA 100 2.346±0.00275 54 614.40K
1LoRA 63 2.203±0.0078 36 221.18K
All 85 1.916±0.00303 56 335.32M

### TableS3.TableforFigure2b

method time RMSE(↓) memory params
[min](↓) [%](↓) (↓)
MoRA 52 4.704±0.01546 36 220.06K
1
MoRA 14 4.637±0.00449 36 217.44K
6
BitFit 47 5.158±0.00868 40 221.18K
DiffFit 50 4.955±0.0064 40 321.54K
LoRA 51 4.612±0.00368 41 393.22K

### VeRA 24 4.797±0.0181 40 221.28K

DoRA 74 4.644±0.00405 54 614.40K
1LoRA 13 4.574±0.1217 36 221.18K
All 55 4.59±0.0784 56 335.32M
TableS4.TableforFigure2c
14

<!-- Page 15 -->

method time RMSE(↓) memory params
[min](↓) [%](↓) (↓)
MoRA 51 5.067±0.02273 36 220.06K
1
MoRA 54 6.242±0.0141 36 217.44K
6

### BitFit 47 7.698±0.00293 40 221.18K

DiffFit 50 7.017±0.00998 40 321.54K

### LoRA 67 4.94±0.00776 41 393.22K

VeRA 51 4.839±0.01025 40 221.28K
DoRA 75 4.918±0.00949 54 614.40K
1LoRA 42 4.719±0.066 36 221.18K
All 61 4.53±0.0278 56 335.32M

### TableS5.TableforFigure2d

method time Loss(↓) memory params
[min](↓) [%](↓) (↓)
MoRA 187 0.18±0.000724 80 1.36M
1
MoRA 198 0.19±6.6e-05 91 1.35M
6

### BitFit 130 0.22±0.0047 75 1.36M

DiffFit 132 0.21±0.00411 77 1.66M

### LoRA 154 0.15±0.00202 93 2.50M


### VeRA 159 0.176±0.00192 92 1.36M

1LoRA 152 0.17±0.003768 76 1.36M
LoRA(QKV) 134 0.2±0.002273 79 786.43K

### TableS6.TableforFigure3

method time Loss(↓) memory params
[min](↓) [%](↓) (↓)

### BitFit 66 0.19±0.001738 91 2.13M

DiffFit 71 0.18±0.003334 93 2.58M
1LoRA 77 0.14±0.00152 92 2.13M
LoRA(QKV) 61 0.17±0.005107 92 1.23M

### TableS7.TableforFigure4

method time[h] FID(↓) memory params
(↓) [%](↓) (↓)
MoRA 9.6 13.9004 67 604.41K
1
MoRA 23.5 14.0791 87 596.52K
6
BitFit 13.0 13.8074 66 603.68K
DiffFit 14.3 13.6644 87 1.09M
LoRA 19.5 13.7621 79 864.03K

### VeRA 12.0 13.1129 87 603.82K

1LoRA 17.0 12.8218 65 603.68K
TableS8.TableforFigure5
15

<!-- Page 16 -->

method time Accuracy(↑) memory params
[min](↓) [%](↓) (↓)
MoRA 30 96.55±0.0465 6 333.36K
1
MoRA 31 97.5±0.0544 6 328.13K
6

### BitFit 16 97.0±0.055 6 331.78K

DiffFit 18 97.9±0.0585 8 817.15K

### LoRA 33 98.1±0.058 7 663.55K


### VeRA 29 97.7±0.1631 8 332.06K

DoRA 51 98.2±0.0866 11 995.33K
1LoRA 17 97.7±0.186 6 331.78K
1LoRA(norms) 18 98.0±0.1397 6 485.38K
All 22 98.3±0.0755 10 343.19M

### TableS9.TableforFigure6

method time Accuracy(↑) memory params
[min](↓) [%](↓) (↓)
MoRA 31 82.7±0.3253 6 333.36K
1
MoRA 30 81.2±0.1875 6 328.13K
6

### BitFit 16 83.0±0.204 6 331.78K

DiffFit 18 87.9±0.0775 8 817.15K
LoRA 34 88.4±0.2173 7 663.55K

### VeRA 29 85.3±0.1723 8 332.06K

DoRA 50 87.3±0.2245 11 995.33K

### ILoRA 17 85.0±0.567 6 331.78K

ILoRA(norms) 18 88.2±0.314 6 485.38K
All 22 90.9±0.3251 10 343.19M

### TableS10.TableforFigure7

method time RMSE(↓) memory params
[min](↓) [%](↓) (↓)
norms 65 13.25±0.004751 36 100.35K
β (BitFit) 61 4.806±0.003922 40 221.18K
γ 68 4.17±0.00482 41 221.18K
DiffFit 66 3.904±0.00539 40 321.54K
1LoRA 63 2.203±0.0078 36 221.18K
1LoRA(β) 54 2.203±0.005498 36 442.37K
1LoRA(norms) 54 2.19±0.00655 36 321.54K
1LoRA(γ) 63 12.399±0.006093 41 442.37K
1LoRA(β,norms) 67 2.2±0.0051438 36 542.72K
1LoRA(β,γ) 65 4.166±0.008069 40 663.55K
1LoRA(γ,norms) 73 2.206±0.001668 41 542.72K
1LoRA(β,γ,norms) 75 2.206±0.002445 40 763.90K
TableS11.TableforFigure10
16

<!-- Page 17 -->

method time Accuracy(↑) memory params
[min](↓) [%](↓) (↓)
norms 16 97.7±0.0395 6 153.60K
β (BitFit) 16 97.0±0.055 6 331.78K
γ 17 97.3±0.0457 8 331.78K
DiffFit 18 97.9±0.0585 8 817.15K
1LoRA 17 97.7±0.186 6 331.78K
1LoRA(β) 18 97.8±0.1245 6 663.55K
1LoRA(norms) 18 98.0±0.139 6 485.38K
1LoRA(γ) 19 97.8±0.1043 8 663.55K
1LoRA(β,norms) 19 97.9±0.078 6 817.15K
1LoRA(β,γ) 21 97.8±0.1297 6 995.33K
1LoRA(γ,norms) 20 98.0±0.0837 8 817.15K
1LoRA(β,γ,norms) 22 98.0±0.109 8 1.15M
TableS12.TableforFigure8
17

## Tables

**Table (Page 5):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 5):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 5):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 5):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 6):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 6):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 7):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 7):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 7):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 8):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 11):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 11):**

| import torch.nn as nn |
|---|
|  |
| class ILoRA(nn.Module): def __init__(self, linear): |
| super().__init__() |
| self.linear = linear |
| self.b = nn.Parameter(torch.zeros(self. |
| linear.out_features)) |
|  |
| def forward(self, x): |
| ilora = self.b * x.sum(-1, keepdim=True) |
| return self.linear(x) + ilora |
