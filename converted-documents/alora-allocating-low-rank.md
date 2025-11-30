---
title: "ALoRA Allocating Low Rank"
original_file: "./ALoRA_Allocating_Low_Rank.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "react", "fine-tuning", "evaluation"]
keywords: ["lora", "tuning", "arxiv", "alora", "set", "zhu", "our", "method", "abs", "page"]
summary: "<!-- Page 1 -->

ALoRA: Allocating Low-Rank Adaptation for Fine-tuning

### Large Language Models

ZequanLiu1 JiawenLyn2 WeiZhu3∗ XingTian4 YvetteGraham2
1 RWTHAachenUniversity,Aachen,Germany
2 TrinityCollegeDublin,Dublin,Ireland
3 EastChinaNormalUniversity,Shanghai,China
4 NiuxinNetworkTechnologyCo.,Ltd. Abstract efficientLLMinferenceandcontrollingthestyle
of the LLMs’ generated contents.1 Fine-tuning

### Parameter-efficient fine-tuning (PEFT) is

suchlargemodelsbyfullparametersisprohibitive
w"
related_documents: []
---

# ALoRA Allocating Low Rank

<!-- Page 1 -->

ALoRA: Allocating Low-Rank Adaptation for Fine-tuning

### Large Language Models

ZequanLiu1 JiawenLyn2 WeiZhu3∗ XingTian4 YvetteGraham2
1 RWTHAachenUniversity,Aachen,Germany
2 TrinityCollegeDublin,Dublin,Ireland
3 EastChinaNormalUniversity,Shanghai,China
4 NiuxinNetworkTechnologyCo.,Ltd.
Abstract efficientLLMinferenceandcontrollingthestyle
of the LLMs’ generated contents.1 Fine-tuning

### Parameter-efficient fine-tuning (PEFT) is

suchlargemodelsbyfullparametersisprohibitive
widely studied for its effectiveness and effisince it requires a large amount of GPU memory
ciency in the era of large language models.
andcomputations. Thus,parameter-efficientfine-

### Low-rankadaptation(LoRA)hasdemonstrated

commendable performance as a popular and tuning (PEFT) (Zhang et al., 2023f; Zhao et al.,
representative method. However, it is imple- 2023;Dingetal.,2022)hasraisedmuchattention
mentedwithafixedintrinsicrankthatmightnot in the research field since in PEFT, the tunable
betheidealsettingforthedownstreamtasks. parameters are often less than 1% of the LLMs
Recognizingtheneedformoreflexibledownandthecomputationcostswillbesignificantlydestreamtaskadaptation,weextendthemethodolcreased.
ogyofLoRAtoaninnovativeapproachwecall

### ManyPEFTmethodshavebeenvalidatedtobe

allocatinglow-rankadaptation(ALoRA)that
enables dynamic adjustments to the intrinsic effective across various models and tasks, often
rankduringtheadaptationprocess. First,we yielding comparable results with full-parameter
proposeanovelmethod,AB-LoRA,thatcanef- fine-tuning (He et al., 2021; Zhu and Tan, 2023;
fectivelyestimatetheimportancescoreofeach Zhang et al., 2023f; Ding et al., 2022). Among

### LoRArank. Second,guidedbyAB-LoRA,we

thesePEFTmethods,thereparameterization-based
gradually prune abundant and negatively immethod low-rank adaptation (LoRA) (Hu et al.,
pacting LoRA ranks and allocate the pruned
2021)isconsideredoneofthemostefficientand
LoRAbudgetstoimportantTransformermodeffective methods at present. LoRA is especially
ulesneedinghigherranks. Wehaveconducted
experiments on various tasks, and the exper- popularafteropen-sourcedLLMsbecomeubiquiimental results demonstrate that our ALoRA tous (Dettmers et al., 2023). LoRA assumes that
method can outperform the recent baselines the change of the model’s parameters for adaptawithcomparabletunableparameters.
tionisintrinsicallylow-dimensionalandperforms
adaptationbyoptimizingthematrixobtainedfrom
1 Introduction
low-rank decomposition. Since it is in the form
Large language models (LLMs) have been ofweightmatrixreparameterization,LoRAparamemergingandachievingstate-of-the-art(SOTA)re- eters can be merged with the original LLMs and
sultsnotonlyonavarietyofnaturallanguagepro- causenoforwardpropagationlatency.
cessingtasks(Qinetal.,2023;Zhuetal.,2023;Zhu AlthoughLoRAiseffectiveandcanbringstable
etal.,2023a,b,2021a;Lietal.,2023b;Zhuetal., performance with the original setting in Hu et al.
2023c;Zhangetal.,2023a;Zhuetal.,2023e;Guo (2021),howtofullyexploititspotentialfordownetal.,2021b;Zhuetal.,2021b;Zhengetal.,2023; stream tasks still needs to be determined. First,
Sunetal.,2020;Zhangetal.,2023d,e;Wangetal., howtodeterminetheintrinsicrankforeachmodel
2023;Zhuetal.,2019a),butalsomanychalleng- weight in the Transformer block is still unclear.
ingevaluationtasks(Huangetal.,2023;Lietal., Moreover, is it reasonable to set the same LoRA
2023a;Cuietal.,2023)likequestionansweringin ranknumberforadaptingthequery,key,andvalue
specialdomains, reasoning, math, safety, instruc- matrix? Second, in practice, the optimal LoRA
tion following. Despite LLMs becoming general
task solvers, fine-tuning still plays a vital role in 1Recently,OpenAIalsoreleasedthefine-tuningAPIfor

### GPT-3.5-turbo.Seeblogpost:https://openai.com/blog/

∗Correspondingauthor:wzhu@stu.ecnu.edu.cn. gpt-3-5-turbo-fine-tuning-and-api-updates.
4202
rpA
51
]LC.sc[
2v78161.3042:viXra

<!-- Page 2 -->

Figure1: SchematicillustrationofourALoRA.Left(a): ALoRAfollowsLoRAtoupdatetheweightmatrixW by
fine-tuningthelow-rankmatricesAandB withintermediaterankk. MatrixGisadiagonalmatrixwhereeach
diagonalelementisthegateunitα foreachLoRAranki<k. Eachα issetto1atinitialization. Rightupper(b):
i i
SomeabundantLoRAranksareprunedbysettingthecorrespondinggateα tozeros. Rightlower(c): Forweight
i
matrixW whoseLoRAranksarenotpruned,wewillassignadditionalLoRArankstoenhancereparameterization.
ranksettingwouldvaryaccordingtomultiplefac- the recent LoRA variants. We also conducted an
tors,suchasthebackbonemodelandthetask. analysis showing that (a) our AB-LoRA method
In order to improve the performance of down- indeedcanreflectthecontributionofeachLoRA
streamtaskadaptationofLoRA,wenowpropose rank;(b)ourmethodcanworkwithdifferentLoRA
the Allocating LoRA (ALoRA) framework (de- rankbudgetsanddifferentbackbonemodels.
picted in Figure 1). First, LoRA modules with Ourcontributionsaresummarizedasfollows:
equalranksizeareinitializedateachTransformer
• We propose a novel method, AB-LoRA, to
weight,withallrankgatessettoone. DuringfineestimatetheimportanceofeachLoRArank.
tuning,were-allocatetheLoRAranksby(a)identifying which LoRA ranks are abundant or have
• Built upon AB-LoRA, we propose our
negativecontributionsandprunethoseranksbyset-

### ALoRAframework,whichcanallocateLoRA

tingtherankgatesto0;(b)addingtheprunedrank
ranksacrossdifferentmodelweightsandenbudgetstomodelweightsthatreceivenopruning,
hancetheadaptationprocess.
thatis,importantmodelweightswillbeassigned
more LoRA ranks. In order to calculate the con-
• Wehaveconductedextensiveexperimentsand
tributionscoreofeachLoRArankefficientlyand
analysisshowingthatourALoRAframework
accurately,weproposeanovelmethod,AB-LoRA.
ispracticalandoutperformsthebaselinesun-
Ourworkingproceduredoesnotrequirere-training
dercomparableparameterbudgets.
anddoesnotrequirehigherLoRArankbudgetsat
initializationorduringtraining. 2 Relatedworks
We conduct extensive experiments on a wide
2.1 Parameter-efficientfine-tuning(PEFT)
collectionoftasks,includingsentimentclassificamethods
tion,naturallanguageinference,questionanswering,naturallanguagegenerationunderconstraint, Parameter-efficientfine-tuning(PEFT)isanapandinstructiontuning,todemonstratetheeffective- proach of optimizing a small portion of paramenessofourmethod. Notably,ourmethodcancon- terswhenfine-tuningalargepretrainedbackbone
sistently outperform strong PEFT baselines with modelandkeepingthebackbonemodeluntouched
comparabletunableparameterbudgets,especially for adaptation (Ding et al., 2022; Zhang et al.,

<!-- Page 3 -->

2023f). A branch of PEFT methods inserts addi- modelperformance. Theselimitationshighlightthe
tionalneuralmodulesorparametersintotheback- importance of upgrading LoRA with an adaptive
bonemodel. Representativeworksinthisdirection strategy.
are Adapter (Houlsby et al., 2019; Rücklé et al., Therearealreadyafewworksinvestigatingthis
2020; Zhang et al., 2023f), Prefix tuning (Li and direction. AdaLoRA (Zhang et al., 2023c) ex-
Liang,2021),Prompttuning(Lesteretal.,2021), pressesthelow-rankmultiplicationofLoRAinthe
P-tuningV2(Liuetal.,2022b). Anotherapproach formofsingularvaluedecomposition(SVD),andit
istospecifytheparticularparameterstobetunable identifiesthemostimportantranksbyasensitivityor prunable (Ben-Zaken et al., 2021; Guo et al., basedimportancescore. SoRA(Dingetal.,2023)
2021a;Zhaoetal.,2020). Thereparameterization- prunes abundant LoRA ranks by imposing a l
0
basedmethodshaveattractedmuchattention(Hu norm and optimizing with proximal gradient deetal.,2021). Thisbranchofapproachestransforms scent. SaLoRA(Huetal.,2023)prunestheLoRA
the adaptive parameters during optimization into ranksviatheLagrangemultipliermethod. Despite
low-rankandparameter-efficientforms. Thistype theserecentefforts,webelieveissuesstillneedto
of PEFT method is closely related to intrinsic di- beinvestigatedforLoRArankallocation: (a)The
mension(Aghajanyanetal.,2021;Lietal.,2018), currentworksinitializealargervalueforeachr
m
that is, full parameter fine-tuning process of pre- andusecertainheuristicstoprunethenumberof
trained models can be reparameterized into opti- ranks to meet a predefined budget. This training
mizationwithinalow-dimensionalsubspace,i.e., processinevitablyrequiresadditionalGPUmemfine-tuninghasalowintrinsicdimension(Huetal., oryconsumption. Inaddition,themaximumLoRA
2021). Intuitively,awellpretrainedmodeldoesnot ranksizeforeachmodelweightislimited,which
needtobealteredsignificantlyfordownstreamtask restrictsthesolutionspaceforLoRArankallocaadaptation. Qin et al. (2021) investigate whether tions. (b) The current works depend on heuristic
we can find a common intrinsic subspace shared importancescores,whichmaynotreliablyreflect
by various NLP tasks. LoRA (Hu et al., 2021) the contribution of each LoRA rank. Our work
is inspired by (Aghajanyan et al., 2021; Li et al., complementstheexistingliteraturebyaddressing
2018)andhypothesizesthatthechangeofweights theaboveissues.
duringmodeltuninghasalowintrinsicrankandoptimizesthelow-rankdecompositionforthechange 3 Methods
of original weight matrices. PEFT methods are
3.1 Preliminaries
widelyapplied,especiallywiththepopularization
ofopen-sourcedlargelanguagemodels(Zhaoetal., Transformer model Currently, most widely
2023)andinstructiontuningwiththesemodelsfor usedopen-sourcedlanguagemodelsandlargelandifferentapplicationscenarios(Taorietal.,2023; guagemodelsadoptthestackedTransformerarchi-
Dettmersetal.,2023). tecture(Vaswanietal.,2017). EachTransformer
blockisprimarilyconstructedusingtwokeysubmodules: amulti-headself-attention(MHA)layer
2.2 TheLoRAmethodanditsvariants
and a fully connected feed-forward (FFN) layer.
LoRA (Hu et al., 2021) is proven to be effec- TheMHAisgivenasfollows:
tiveandyieldstableresultswhenappliedtoboth
relativelysmallpretrainedbackbonesandlargelan- x ′ = MHA(xWQ,xWk,xWV)WO, (1)
guage models (Dettmers et al., 2023; Zhu et al.,
2023). Despite its tractability and effectiveness, where MHA() denotes the multi-head attention
LoRA still has room for improvements in select- operation, x ∈ Rl×d is the input tensor, WO ∈
ingoptimalrankr foreachTransformermodel Rd×d is the output projection layer (denoted as
m
weight m. The rank r takes discrete values; thus, theOutputmodule),andWQ,WK,WV ∈ Rd×d
changingitwilldirectlyalterthemodelstructures. (denoted as the Query, Key, and Value modules).
Theoptimalchoicesofrankscanvaryacrossback- l is the sequence length, d is the hidden dimenbonemodels,tasks,andevenTransformermodel sion. TheFFNmoduleconsistsoflineartransforweights. Settingalargerankvalueforr canwaste mationsandanactivationfunctiong suchasReLU
m
training time and computation resources, while or GELU (Hendrycks and Gimpel, 2016). Take
progressivelysettingasmallr maydegradethe theFFNmoduleintheLlaMA-2models(Touvron
m

<!-- Page 4 -->

etal.,2023)asexample: setΘ),thenetworkwithallthenon-zerogateunits
asthesuper-networkM,anddenotetheparameters
x ′ = (g(xWG)∗xWU)WD, (2) inthedown-projectionandup-projectionmatrices
asΩ,thentheoptimizationobjectiveis:
′
where WG,WU ∈ Rd×d (denoted as Gate and
′ minL(D ,Ω∗,Θ),
Up module) and WD ∈ Rd ×d (denoted as the 2

## Θ

Downmodule),andd′ isusuallylargerthand. For s.t. Ω∗ = argminL(D ,Ω,Θ), (4)
1
notationconvenience,wewillrefertothenumber Ω
ofmodulesinaTransformerblockasN . Thus, whereD andD consistsofasplitofthetraining
mod 1 2
inLlaMA-2,N = 7. set D , L() is the loss function. This work
mod train
Denote the task’s training set as D = uses the cross-entropy loss as the loss function.
train
(x m ,y m ),m = 1,2,...,M, where M represents Note that with discrete values of α i , solving the
thenumberofsamples. Inthiswork,weonlycon- aboveoptimizationproblemischallengingdueto
sider the case where input x and target y are non-differentiability. Thus,followingtheworkof
m m
bothtextsequences. Andweexpectthelanguage differentiable neural architecture search (DNAS)
modeling head of LLMs to decode y m during in- (Liu et al., 2019a), α i is relaxed to a continuous
ference. That is, no additional linear prediction valueinbetween(0,1)andtheequation3becomes:
headsareconsideredforpredictingcategoricalor
z = WBG ′ WAx,
numericalvalues. m m m
′ ′ ′
G = diag(α ,...,α ),
m m,1 m,rm
3.2 Formulation
′ ′ ′
α = 2∗Sigmoid(a ), a ∈ R, (5)
m,i m,i m,i
Ourobjectiveistoefficientlyfine-tunetheLLMs
foraspecificdownstreamtaskunderagivenLoRA
wherea′
isinitializedwithzerovalue. Withthis
m,i
parameter budget Rtarget = (cid:80)N modrtarget . The setting,Equation4becomesdifferentableandcan
m=1 m
previous literature (Ding et al., 2023; Hu et al., be optimized by bi-level optimization (Liu et al.,
2023; Zhang et al., 2023c) usually initialize the 2019a).
LoRA modules with a pre-defined large maxi-
3.3 OurnovelAB-LoRAmethod
mum rank r , consuming extra GPU memomax
ries. Different from the previous works, we now UndertheDNASsetting,itisnaturaltoconsider
initialize each LoRA module with rank rinit = thearchitectureweightα′ astheimportancescore
m i
Rtarget/N . Thatis,uponinitialization,wehave forLoRAranki,andonecanusethesescoresto
mod
mettheLoRArankbudget. Moreover,wewillre- guidethepruningofabundantLoRAranks. Howallocate the LoRA ranks in order to enhance the ever,aspointedoutbytheliterature(Zhangetal.,
fine-tuningperformance. 2023f; Chen et al., 2019), and as will be demon-
In order to adjust the rank allocation of LoRA stratedintheexperiment,thearchitectureweights
modules, we now inject gate units α ∈ {0,1} arenotreliableindicatorsforthefinalLoRAalloi
(i = 1,2,...,r ) to each module m with LoRA cation’sperformance. Thisobservationmotivates
m
rank r . Imitating the formulation of SVD, the us to propose a simple yet effective modification
m
forwardpropagationofALoRAisgivenby: totheDNAS-stylearchitecturesearch. Insteadof
relyingonthearchitectureweights’valuestokeep
z = xWAG WB, thebestLoRAranks,weproposedirectlyevaluatm m m
G = diag(α ,...,α ), (3) ingtheLoRArank’ssuperioritybyitscontribution
m m,1 m,rm
orinfluenceonthesuper-network’sperformances.
where diag() denotes a diagonal matrix, WA ∈ Sinceourmethodmimicsconductingablationstudm
Rd×rm,WB ∈ Rrm×d. Atinitialization,thegate iesofacertainLoRArankfromthesuper-network,
m
unitsareallsetto1. werefertoourmethodastheablation-basedLoRA
Differentfromthepreviousliterature(Dingetal., (AB-LoRA).
2023; Hu et al., 2023; Zhang et al., 2023c), we We now introduce the core of our AB-LoRA
takeanalternativeapproach, thatis, considerthe method: calculatingeachLoRArank’simportance
problemofLoRAallocationasneuralarchitecture score,definedashowmuchitcontributestothepersearch(Whiteetal.,2023). Weconsiderthegate formance of the super-network. Denote the comunitsα asarchitectureparameters(denotedasthe plete super-network as M. Super-network M is
i

<!-- Page 5 -->

Algorithm1:WorkflowofALoRA masksoutasingleoperation,and(b)isnotsuitable
Input: Asuper-networkM,withRtarget forgenerativelanguagemodelfine-tuning.
LoRAranksuniformlydistributedin
modulesofM;
3.4 ThecompleteprocessofALoRA
Output: AnewallocationofRtarget LoRA
ranks.
With the guidance of the importance score in

### Data: TrainingsetD ,abatchof

train Equation6,wecannowformallydefinethewhole
validationdataB
val working process of our ALoRA framework (Fig-

### Trainsuper-networkM onthetrainingset

1 ure1). OurworkingflowofallocatingtheLoRA

### D forK epochs;

train 1 ranksbuildsuponthefollowingintuitions: (a)the
forn = 0;n < N do
2 A pruningandallocationofLoRAranksisconducted
forasingleLoRArankr onM do
3 m,i gradually to avoid performance degradation. (b)

### Calculatetheimportancescore

4 if the LoRA ranks in a Transformer module re-

### IS(r )onB ;

m,i val ceiverelativelyhighimportancescoresandarenot
5 Prunen 0 LoRArankswithlowest pruned,thismoduleisdeemedimportant. Itmay
importancescores; needmoreLoRAranksforadaptationsothatthe
6 iftherearemodulesnotpruned then LoRAparameterscanbetterlearnthetaskknowl-
7 Addn 0 LoRArankstothe edge.
un-prunedmodules;
The framework of ALoRA is centered on our

### FurthertraintheSuper-networkM on

8 AB-LoRA method, which requires the super-

### D forK epochs;

train 2 network to be trained for K epochs on the train
1
set. We freeze the architectural parameters and
train only the model parameters on the train set.
trainedtillconvergenceonthetrainingset. Wenow No bi-level optimization is required, thus saving
consideramodifiedsuper-networkobtainedbyze- trainingtimecosts. Then,foreachLoRArank,we
roingoutasingleLoRArankr whilekeepingall evaluatetheimportancescoreonabatchofsamples
otherLoRAranks. Thisnewsuper-networkisde- B from the development set. Then, n LoRA
val A
notedasM . Wealsoconsideranothermodified ranks with the lowest scores are pruned by zero-
\r
super-networkM inwhichonlyLoRArankr is ingouttheircorrespondinggateunits. Moreover,
r
keptwhileallotherLoRAranksarezeroedout. We ifsomeTransformermodulesdonothavepruned
evaluate the three versions of super-networks on LoRAranks,weallocatetheparameterbudgetsto
thesamebatchofvalidationdataB . Denotethe them to enhance the adaptation further. 23 After
val
metric score as a function of a model M, S(M), thepruningandaddingoperations,wetunethealwiththevalidationdatafixed. Then,theimportance teredsuper-networkforK > 0epochstorecover
2
scoreofLoRArankr isgivenby thelostperformance. Theabovestepsarerepeated
forN times. Formally,wesummarizetheabove

## A

IS(r) = S(M)−S(M \r )+S(M r ). (6) processinAlgorithm1.

### In the above equation, S(M) can be treated as a

constant term. Thus the above equation can be 2NotethatincreasingtheranksizeofaLoRAmodulefrom
′
simplified to CS(o) = −S(M \r )+S(M r ). Intu- r n m ew t l o y r i m nit f ia o l r iz T e r d an p s a f r o a r m m e e t r e m rs o f d o u r l t e h m em in a v tr o ic lv e e s s ,s c o on th c a a t te W na A tin ∈ g
itively,theLoRArankthatresultsinasignificant m
′
performancedropuponzeroingoutmustplayan
Rd×rm andW
m
B ∈ Rrm×d becomesW
m
A ∈ Rd×rm and
′
importantroleinthesuper-network. Similarly,the

## W

m
B ∈ Rrm×d. And the diagonal matrix G
m
is changed
onekeepingmostoftheperformancewhenacting
f
n
r
e
o
w
m
ly
d
a
ia
d
g
d
(
e
α
d m g , a 1 t
,
e
.
u
..
n
,
i
α
ts m a , r r e m i
)
ni
t
t
o
ia
d
li
i
z
a
e
g
d
(α
w m it , h 1
,
o
.
n
..
e
,
s
α
. m,rm
m). The
alone contains important task-related knowledge 3Ifn A isnotdividedbythenumberofun-prunedmodules,
weallocatethen ranksasuniformlyaspossible,withpriority
andshouldbeconsideredimportant. Intheexperi- A
giventomoduleswithhigheraverageimportancescores.For
ments,differentfromChenandHsieh(2020),we example,ifn =8,andmodulem ,m ,m arenotpruned,

## A 1 2 3

set S() as the negative of the cross-entropy (CE) andm 1 hasthehighestaverageimportancescore,m 2 ranks
thesecond,m receivesthelowestaverageimportancescore.
losssincethewidelyappliedmetricslikeaccuracy 3
Thenthreeranksaregiventom andm ,andtworanksare
1 2
orF1: (a)maynotvaryifthesuper-networkonly giventom .
3

<!-- Page 6 -->

4 Experiments wewillalsouseGPT2-largemodel(Radfordetal.,
2019),andRoBERTa-large(Liuetal.,2019b).
In this section, we conduct a series of experi-
Prediction heads When fine-tuning LlaMA-2
mentstoevaluateourALoRAmethod.
7B, we only consider the supervised fine-tuning
(SFT) setting (Ouyang et al., 2022), that is, all
4.1 Baselines
the predictions are generated using the language

### We compare our ALoRA framework with the

modelinghead(LMhead)uponreceivingaprompt
currentSOTAPEFTbaselinemethods.
or an instruction. For decoding during inference,
Adapter-based tuning We consider the followweusebeamsearchwithbeamsize5.
ingadaptertuningbaselines: (1)Houlsby-Adapter

### Hyper-parametersforALoRA Inourexperi-

(Houlsby et al., 2019); (2) Parallel-Adapter proments, unless otherwise specified, we set Rtarget
posedbyHeetal.(2021);(3)AdapterDrop(Rücklé
to 8∗N , and initially all Transformer model
mod
et al., 2020); (4) LST (Sung et al., 2022); (5)
weightsarepairedwithLoRAmoduleswithrank
Learned-Adapter(Zhangetal.,2023f).
rinit = 8. In this setting, ALoRA satisfies the
m

### Prompt-based tuning For prompt-based tuning

LoRArankbudgetuponinitialization,andthusdurmethods, we compare with (a) P-tuning v2 (Liu
ingtrainingandinference.4 Wesetn to1∗N .

### A mod

etal.,2021);(b)SPT(ZhuandTan,2023).
FortrainingwiththeALoRA’sworkflow,wesetthe
LoRAanditsvariants weconsiderthefollowing
batchsizeofB to32,K to1epoch,K to0.25
val 1 2
LoRAvariantsasbaselines: (a)LoRA(Huetal.,
epoch,andtheLoRArankallocationprocedureis
2021); (b) AdaLoRA (Zhang et al., 2023c). (c)
conductedforatmostN = 8times.

## A


### SoRA(Dingetal.,2023);(d)SaLoRA(Huetal.,

Reproducibility We run each task under five
2023).
differentrandomseedsandreportthemedianper-
OtherPEFTmethods Wealsocompare: (1)SSP
formanceonthetestsetofeachtask.
(Huetal.,2022),whichcombinesdifferentPEFT
Due to limited length, other experimental setmethods.
tingsforthebaselinemethodsandthetrainingpro-
ThebaselinesareimplementedusingtheiropencedureareputinAppendixE.
sourced codes. The hyper-parameter settings for
thebaselinesaredetailedinAppendixE.
4.4 Mainresults
4.2 Datasetsandevaluationmetrics Theexperimentalresultsonthethreeclassificationtasksand4questionansweringtasksarepre-

### We compare our approach to the baselines

sentedinTable1. Inthesecondandthirdcolumns
on (a) four benchmark question-answering tasks:
of Table 1, we present the initial number of tun-
SQUAD (Rajpurkar et al., 2016) and three tasks
ableparametersandthefinalones. Table1reveals
from the SuperGLUE benchmark(Wang et al.,
thatourALoRAmethodoutperformsthebaseline
2019)(BoolQ,COPAandReCoRD).(b)threesenmethods across all seven tasks, with comparable
tence level tasks from GLUE benchmark (Wang
orfewertunableparametersthroughoutthetrainetal.,2018),SST-2,RTE,QNLI.(d)Alpacadataset
ingandinferenceprocesses. Inparticular,ALoRA
(Taorietal.,2023)forinstructiontuning,andMT-
successfully outperforms AdaLoRA, SoRA, and

### Bench(Zhengetal.,2023),toevaluatetheinstruc-


### SaLoRA with comparable initial and final LoRA

tiontuningqualityofLLMs. Thedatasetintroducparameters. These results demonstrate that our
tions,statistics,andprompt-responsetemplatesfor
method can better allocate LoRA parameters for
the above tasks are detailed in Appendix B. The
betterdownstreamtaskadaptation.
abovetasks’evaluationmetricsorprotocolsarein
FortheE2Ebenchmark(Novikovaetal.,2017),
AppendixB.5.
the results are reported in Table 2. The results
4.3 ExperimentSettings show that on the E2E task, our ALoRA method
successfullyoutperformsLoRAandSoRAregard-
Computinginfrastures WerunallourexperiingBLEU,ROUGE-L,orMETEORscores.
mentsonNVIDIAA40(48GB)GPUs.
After the LlaMA-2 7B is fine-tuned on the Al-
Pretrained backbones The main experiments
pacadatasetwithourALoRAandSoRAmethods,
usesmostrecentopen-sourcedLLM,LlaMA-27B
releasedbyMeta(Touvronetal.,2023)asthepre-
4NotethatitispossiblethatthetotalLoRAranksafter
trained backbone model. In the ablation studies, trainingissmallerthanthatatinitialization.

<!-- Page 7 -->

AdditionalParams SST-2 RTE QNLI BoolQ COPA ReCoRD Squad

### Method

Initial Final (acc) (acc) (acc) (acc) (acc) (f1-em) (f1-em)

### Baselines

P-tuningv2 20.9M 20.9M 93.4 79.6 92.6 84.7 90.3 89.9 87.6

### Spt 16.8M 16.8M 93.6 80.3 92.8 85.3 90.6 90.2 88.1

Housbly-Adapter 21.0M 21.0M 93.5 81.3 92.9 85.2 91.0 90.4 88.0
Parallel-Adapters 21.0M 21.0M 93.6 81.2 93.0 85.7 90.8 90.6 88.2
AdapterDrop 21.0M 21.0M 93.2 80.7 92.8 85.1 90.6 90.3 87.9

### Lst 21.1M 21.1M 93.4 81.6 93.0 86.2 91.0 90.4 87.9

Learned-Adapter 21.2M 21.2M 94.1 82.1 93.1 87.0 91.1 90.7 88.3

### LoRA 20.0M 20.0M 94.1 83.3 93.1 87.3 91.3 90.8 88.4

AdaLoRA 40.0M 20.0M 94.1 83.5 93.2 87.1 91.6 91.1 88.3

### SoRA 40.0M 20.0M 94.2 83.7 93.3 87.6 91.7 91.0 88.5

SaLoRA 40.0M 20.0M 93.9 83.4 93.2 87.2 91.5 90.9 88.4
SSP 40.0M 20.0M 94.1 83.1 93.1 87.1 91.6 90.6 88.2

### Ourproposedmethods


### ALoRA 20.0M 19.6M 95.0 84.6 93.7 88.0 92.1 91.8 89.2

Table1: TheOverallcomparisonofthethreeGLUEtasksandfourquestion-answeringtasks. Thebackbonemodel
isLlaMA-27B.Wereportthemedianperformanceoverfiverandomseeds. BoldandUnderlineindicatethebest
andthesecond-bestresults. ThemetricforeachtaskisexplainedinAppendixB.5.
(a) BoolQ (b) E2E
Figure2:PerformancesunderdifferentLoRArankbudgets.Thex-axisrepresentsthenumberoftunableparameters,
andthey-axisrepresentstheperformancescore.
Method BLEU ROUGE-L METEOR ofutilizingGPT-4asanunbiasedreviewer(Zheng

### Learned-Adapter 68.9 70.9 45.8

et al., 2023). The protocol of utilizing GPT-4 as

### LoRA 68.9 71.2 46.1

the reviewer and scorer is specified in Appendix

### SoRA 70.0 71.1 46.3

B.5. TheaveragescoreprovidedbyGPT-4ispre-

### ALoRA 70.6 71.8 47.1

sentedinTable3,alongwiththeROUGE-Lscores
Table 2: Results for different PEFT methods on the calculatedbyconsideringtheGPT-4’sanswersas
E2E benchmark. The backbone LM is LlaMA-2 7B.
groundtruth. Consistentwiththepreviousexper-
ThemetricsareexplainedinAppendixB.5.
iments (Table 1 and 2), our ALoRA method outperformstheSoRAmethodintermsoftheGPT-4

### Method AvgGPT-4score(↑) ROUGE-L(↑)

evaluation scores and ROUGE-L, demonstrating

### SoRA 7.16 53.2

that ALoRA can enhance the instruction tuning

### ALoRA 7.47 54.3

quality of large language models. A case study
Table3: Theperformanceofinstructiontuningusing ofanswersgeneratedbydifferentmethodsispretheSoRAandALoRAmethods. Thebackbonemodel sentedinTable9,showcasingthatALoRAleadsto
isLlaMA-27B.↑meansthemetricishigherthebetter. betterinstruction-tunedLLMs.
weutilizethe80instructionsintheMT-Benchas
thetestset. Wefollowthecurrentstandardpractice

<!-- Page 8 -->

Method Memorycost(GB) Speed(it/s) Timecost(h)
LoRA 17.6 5.01 2.68

### SoRA 18.8 4.96 3.63


### ALoRA 18.1 5.01 3.81

Table 4: The memory, speed and time cost for finetuningLlaMA-27BontheE2EtaskwithdifferentPEFT
methods.
4.5 Ablationstudiesandanalysis

### AnalysisofTrainingEfficiency Sofar,wehave

demonstrated that our ALoRA can outperform
LoRA and SoRA on a wide collection of tasks.
Onemightsuspectthisadvantageisachievedwith Figure 3: The final rank allocations of ALoRA after
significanttimeormemorycosts. Wecomparethe fine-tuningtheLlaMA-27BmodelontheE2Etask.
max training GPU memory, training speed, and
trainingtimecostsofALoRA,SoRA,andLoRA
withALoRA’sallocation,SoRAresultsinamore
whenfine-tuningLlaMA-27BwiththeE2Ebenchunbalancedallocation,puttingmorerankbudgets
mark. From Table 4, one can see that ALoRA
totheDownmodulethanourALoRAmethod.
requires less memory costs during training than

### ComparisonsunderdifferentLoRArankbud-

SoRAsinceitdoesnotinitializewithalargerLoRA
getsNotethatinthemainexperiments,wesetthe
rank. Moreover, under early stopping, the total
targetedLoRArankbudgetasRtarget = 8∗N .
trainingtimecostofALoRAremainscomparable mod
Now we vary this budget to any multiplier in 1,
withSoRAandLoRA.
2, 4, 8, 16, 32, 64, 128 times N , and see how
mod
AblationstudyofALoRAframework Wenow

### ALoRA,SoRA,andLoRAperformontheBoolQ

considerthefollowingvariantsofALoRA:(a)inand E2E tasks. The experimental results are presteadofutilizingournovelAB-LoRAmethod,we
sentedinFigure2(a)and2(b). Fromtheresults,we
follow the optimization procedure of Equation 4,
canseethatunderdifferentLoRArankbudgets,our
andusethearchitecturalweightsα′
astheimporm,i ALoRAmethodcanconsistentlyoutperformLoRA
tance scores. This variant is denoted as ALoRA-
andSoRAbyeffectivelyallocatingdifferentLoRA

### DNAS. (b) Use the sensitivity-based metric in

ranks properly to different Transformer modules,
Zhang et al. (2023c) as the importance measurethusenhancingtheperformanceoffine-tuning.
ment. (denotedasALoRA-Sensi). Theexperimen-

### Ablation on the pretrained backbones Our

tal results on the BoolQ, ReCoRD, and SQUAD
main experiments are conducted on the LlaMA-
tasks are reported in Table 6 of Appendix F. The
27Bmodel. Todemonstratethewideapplicability
resultsshowthatALoRAoutperformsthetwovariof our method, we now conduct experiments on
ants,demonstratingthatourAB-LoRAmethodcan
RoBERTa-large and GPT2-large. The results are
providebetterguidanceinallocatingLoRAranks.
reportedinTable7and8. Wecanseethatonthese

### Visualizationofthefinalrankallocations In

two backbones, our method can also outperform
thissection,wevisualizethefinalrankallocations
thebaselinemethods.
of ALoRA after the training process on the E2E
taskinFigure3. WealsocomparetheLoRArank
5 Conclusion
allocations by the SoRA method in Figure 4 of
Appendix H. We can see from Figure 3 that (a) This work presents the Allocating Low-Rank
MoreLoRArankbudgetsareputtoadaptthequery Adaptation (ALoRA), an innovative method for
andkeymodules,whilethevalueandoutputmod- parameter-efficientfine-tuninglargelanguagemodulesintheself-attentionarelessemphasized. (b) els. Upon the hypothesis that the adaptation for
The feed-forward layer in the Transformer block differentTransformermodulescouldbeofdifferrequires fewer LoRA ranks, indicating that this ent tanks, we introduce a novel workflow for allayerstoresgenerallanguageknowledge,whilethe locating LoRA ranks in the fine-tuning process.
attention module will contain more task-specific First, weproposeanovelmethod, AB-DNAS,to
knowledge after ALoRA fine-tuning. Compared accuratelyevaluatetheimportancescoresofLoRA

<!-- Page 9 -->

ranks. Second,guidedbytheAB-DNASmethod, produceinaccurate,biasedorotherobjectionable
our workflow allows the pruning of ranks at spe- responsestouserprompts. However,thiswork’sincificmodulesandconsidersallocatingmoreranks tentistoconductresearchondifferentfine-tuning
to essential modules. Thus, our method does not methods for LLMs, not building applications to
require to set a more significant initial rank. Our generalusers. Inthefuture,wewouldliketoconmethod is convenient to implement and off-the- ductfurthertestingtoseehowourmethodaffects
shelf. Experiments on various tasks demonstrate thesafetyaspectsofLLMs.
thatourALoRAmethodoutperformsthebaseline
methods.

### References

6 Acknowledgements
Armen Aghajanyan, Sonal Gupta, and Luke Zettlemoyer.2021. Intrinsicdimensionalityexplainsthe

### Jiawen Lyn and Yvette Graham’s contribution

effectivenessoflanguagemodelfine-tuning. InProwas conducted with the financial support of the ceedingsofthe59thAnnualMeetingoftheAssocia-
Science Foundation Ireland Centre for Research tionforComputationalLinguisticsandthe11thInternationalJointConferenceonNaturalLanguagePro-
TraininginDigitally-EnhancedReality(d-real)uncessing(Volume1: LongPapers),pages7319–7328,
derGrantNo. 18/CRT/6224andADAPTatTrin-
Online.AssociationforComputationalLinguistics.
ity College Dublin under Grant Agreement No
Elad Ben-Zaken, Shauli Ravfogel, and Yoav Gold-
13/RC/2106_P2. ForthepurposeofOpenAccess,
berg. 2021. Bitfit: Simple parameter-efficient
theauthorhasappliedaCCBYpubliccopyright
fine-tuningfortransformer-basedmaskedlanguagelicencetoanyAuthorAcceptedManuscriptversion models. ArXiv,abs/2106.10199.
arisingfromthissubmission.

### XiangningChenandCho-JuiHsieh.2020. Stabilizing

differentiable architecture search via perturbation-

### Limitations

basedregularization. InInternationalConferenceon
MachineLearning.

### Weshowedthatourproposedmethodcangreatly

improvetheperformanceofparameter-efficienttun- XinChen,LingxiXie,JunWu,andQiTian.2019. Proingondiversetasksanddifferentpretrainedmod- gressivedarts: Bridgingtheoptimizationgapfornas
inthewild. InternationalJournalofComputerViels(i.e.,LlaMA-27B,RoBERTa-largeandGPT2-
sion,129:638–655.
large). However, we acknowledge the following
limitations: (a)themoresuper-sizedopen-sourced Ganqu Cui, Lifan Yuan, Ning Ding, Guanming Yao,
WeiZhu,YuanNi,GuotongXie,ZhiyuanLiu,and

### LLMs,suchasLlaMA-213Band70B,arenotex-

MaosongSun.2023. Ultrafeedback: Boostinglanperimentedduetolimitedcomputationresources.
guage models with high-quality feedback. ArXiv,
(b)Othertasksinnaturallanguageprocessing,like abs/2310.01377.
information extraction, were also not considered.
Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and

### But our framework can be easily transferred to

Luke Zettlemoyer. 2023. QLoRA: Efficient Fineotherbackbonearchitecturesanddifferenttypesof tuning of Quantized LLMs. arXiv e-prints, page
tasks. Itwouldbeofinteresttoinvestigateifthesu- arXiv:2305.14314.
periorityofourmethodholdsforotherlarge-scaled

### Ning Ding, Xingtai Lv, Qiaosen Wang, Yulin Chen,

backbonemodelsandothertypesoftasks. Andwe BowenZhou,ZhiyuanLiu,andMaosongSun.2023.
willexploreitinfuturework. Sparselow-rankadaptationofpre-trainedlanguage
models. In Conference on Empirical Methods in
EthicsStatement NaturalLanguageProcessing.

### Ning Ding, Yujia Qin, Guang Yang, Fu Wei, Zong-

The finding and proposed method aims to imhanYang,YushengSu,ShengdingHu,YulinChen,
provethelow-rankadaptation(LoRA)basedtun- Chi-MinChan, WeizeChen, JingYi, WeilinZhao,
ing in terms of better rank allocations and per- XiaozhiWang,ZhiyuanLiu,HaitaoZheng,Jianfei
formances. The used datasets are widely used Chen, Yang Liu, Jie Tang, Juan Li, and Maosong

### Sun.2022. Deltatuning: Acomprehensivestudyof

in previous work and, to our knowledge, do not
parameterefficientmethodsforpre-trainedlanguage
haveanyattachedprivacyorethicalissues. Inthis
models. ArXiv,abs/2203.06904.
work,wehaveexperimentedwithLlaMA-27B,a
XiangxiangGao,WeiZhu,JiashengGao,andCongrui
modernlargelanguagemodel. AswithallLLMs,
Yin. 2023. F-pabee: Flexible-patience-based early

### LlaMA-2’s potential outputs cannot be predicted

exitingforsingle-labelandmulti-labeltextclassificainadvance,andthemodelmayinsomeinstances tiontasks. ArXiv,abs/2305.11916.

<!-- Page 10 -->

Demi Guo, Alexander Rush, and Yoon Kim. 2021a. BrianLester,RamiAl-Rfou,andNoahConstant.2021.
Parameter-efficienttransferlearningwithdiffprun- The power of scale for parameter-efficient prompt
ing. InProceedingsofthe59thAnnualMeetingofthe tuning. arXivpreprintarXiv:2104.08691.

### Association for Computational Linguistics and the

11thInternationalJointConferenceonNaturalLan- ChunyuanLi,HeeradFarkhoor,RosanneLiu,andJaguageProcessing(Volume1: LongPapers),pages sonYosinski.2018. MeasuringtheIntrinsicDimen-
4884–4896,Online.AssociationforComputational sionofObjectiveLandscapes. arXive-prints,page
Linguistics. arXiv:1804.08838.
Zhao Guo, Yuan Ni, Keqiang Wang, Wei Zhu, and
HaonanLi,YixuanZhang,FajriKoto,YifeiYang,Hai
GuotongXie.2021b. Globalattentiondecoderfor

### Zhao, YeyunGong, NanDuan, andTimothyBald-

Chinese spelling error correction. In Findings of
win.2023a. Cmmlu: Measuringmassivemultitask
theAssociationforComputationalLinguistics: ACL-
languageunderstandinginchinese. arXivpreprint
IJCNLP2021,pages1419–1428,Online.Association
arXiv:2306.09212.
forComputationalLinguistics.
Xiang Lisa Li and Percy Liang. 2021. Prefix-tuning:

### JunxianHe,ChuntingZhou,XuezheMa,TaylorBerg-

Optimizingcontinuouspromptsforgeneration. arXiv
Kirkpatrick,andGrahamNeubig.2021. Towardsa
preprintarXiv:2101.00190.
unifiedviewofparameter-efficienttransferlearning.
ArXiv,abs/2110.04366.

### XiaonanLi,KaiLv,HangYan,TianyaLin,WeiZhu,

Dan Hendrycks and Kevin Gimpel. 2016. Gaussian YuanNi,GuoTongXie,XiaolingWang,andXipeng
errorlinearunits(gelus). arXiv: Learning. Qiu.2023b. Unifieddemonstrationretrieverforincontextlearning. ArXiv,abs/2305.04320.

### Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski,

Bruna Morrone, Quentin De Laroussilhe, Andrea Xiepeng Li, Zhexi Zhang, Wei Zhu, Zheng Li, Yuan
Gesmundo,MonaAttariyan,andSylvainGelly.2019. Ni,PengGao,JunchiYan,andGuotongXie.2019.
Parameter-efficienttransferlearningfornlp. InIn- PingansmarthealthandSJTUatCOIN-sharedtask:
ternationalConferenceonMachineLearning,pages utilizingpre-trainedlanguagemodelsandcommon-
2790–2799.PMLR. senseknowledgeinmachinereadingtasks. InProceedings of the First Workshop on Commonsense
Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan
Inference in Natural Language Processing, pages

### Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,

93–98,HongKong,China.AssociationforComputaand Weizhu Chen. 2021. Lora: Low-rank adaptionalLinguistics.
tation of large language models. arXiv preprint
arXiv:2106.09685.
Hanxiao Liu, Karen Simonyan, and Yiming Yang.
2019a. Darts: Differentiable architecture search.
ShengdingHu,ZhenZhang,NingDing,YadaoWang,
ArXiv,abs/1806.09055.
Yasheng Wang, Zhiyuan Liu, and Maosong Sun.

## Sparsestructuresearchforparameter-efficient

tuning. ArXiv,abs/2206.07382. XiangyangLiu,TianxiangSun,XuanjingHuang,and

### Xipeng Qiu. 2022a. Late prompt tuning: A late

YahaoHu,YifeiXie,TianfengWang,ManChen,and promptcouldbebetterthanmanyprompts. ArXiv,
ZhisongPan.2023. Structure-awarelow-rankadap- abs/2210.11292.
tationforparameter-efficientfine-tuning. Mathematics. XiaoLiu,KaixuanJi,YichengFu,ZhengxiaoDu,Zhilin

### Yang, and Jie Tang. 2021. P-tuning v2: Prompt

Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei tuningcanbecomparabletofine-tuninguniversally
Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu, acrossscalesandtasks. ArXiv,abs/2110.07602.
ChuanchengLv,YikaiZhang,JiayiLei,etal.2023.
C-eval: Amulti-levelmulti-disciplinechineseeval- Xiao Liu, Kaixuan Ji, Yicheng Fu, Weng Lam Tam,
uationsuiteforfoundationmodels. arXivpreprint Zhengxiao Du, Zhilin Yang, and Jie Tang. 2022b.
arXiv:2305.08322.
P-tuning: Prompttuningcanbecomparabletofinetuningacrossscalesandtasks. InAnnualMeetingof
ShiboJieandZhifangDeng.2022. ConvolutionalbytheAssociationforComputationalLinguistics.
passesarebettervisiontransformeradapters. ArXiv,
abs/2207.07039.

### YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Man-

Dawid Jan Kopiczko, Tijmen Blankevoort, and dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
YukiMarkusAsano.2023. Vera: Vector-basedran- Luke Zettlemoyer, and Veselin Stoyanov. 2019b.
dommatrixadaptation. ArXiv,abs/2310.11454. Roberta: A robustly optimized bert pretraining approach. ArXiv,abs/1907.11692.

### TuanLe,MarcoBertolini,FrankNo’e,andDjork-Arné

Clevert.2021. Parameterizedhypercomplexgraph RabeehKarimiMahabadi, JamesHenderson, andSeneuralnetworksforgraphclassification. InInterna- bastianRuder.2021. Compacter: Efficientlow-rank
tionalConferenceonArtificialNeuralNetworks. hypercomplexadapterlayers. InNeurIPS.

<!-- Page 11 -->

SourabMangrulkar,SylvainGugger,LysandreDebut, AndreasRücklé,GregorGeigle,MaxGlockner,Tilman
YounesBelkada,SayakPaul,andBenjaminBossan. Beck, Jonas Pfeiffer, Nils Reimers, and Iryna

## Peft: State-of-the-artparameter-efficientfine- Gurevych. 2020. Adapterdrop: On the efficiency

tuningmethods. https://github.com/huggingface/ ofadaptersintransformers. InConferenceonEmpirpeft. icalMethodsinNaturalLanguageProcessing.
Swaroop Mishra, Daniel Khashabi, Chitta Baral, and VictorSanh,AlbertWebson,ColinRaffel,StephenH.
Hannaneh Hajishirzi. 2021. Cross-task generaliza- Bach, Lintang Sutawika, Zaid Alyafeai, Antoine
tionvianaturallanguagecrowdsourcinginstructions. Chaffin,ArnaudStiegler,TevenLeScao,ArunRaja,
InAnnualMeetingoftheAssociationforComputa- Manan Dey, M Saiful Bari, Canwen Xu, Urmish
tionalLinguistics. Thakker,ShanyaSharmaSharma,ElizaSzczechla,

### TaewoonKim,GunjanChhablani,NihalV.Nayak,

NafiseSadatMoosavi,QuentinDelfosse,KristianKer- Debajyoti Datta, Jonathan D. Chang, Mike Tiansting,andIrynaGurevych.2022. Adaptableadapters. JianJiang,HanWang,MatteoManica,ShengShen,
In North American Chapter of the Association for Zheng-XinYong,HarshitPandey,RachelBawden,
ComputationalLinguistics. ThomasWang,TrishalaNeeraj,JosRozen,Abheesht

### Sharma,AndreaSantilli,ThibaultFévry,JasonAlan

JekaterinaNovikova,OndˇrejDušek,andVerenaRieser. Fries,RyanTeehan,StellaBiderman,LeoGao,Tali

## The E2E dataset: New challenges for end- Bers,ThomasWolf,andAlexanderM.Rush.2021.

to-end generation. In Proceedings of the 18th An- Multitaskpromptedtrainingenableszero-shottask
nual SIGdial Meeting on Discourse and Dialogue, generalization. ArXiv,abs/2110.08207.
pages201–206,Saarbrücken,Germany.Association
forComputationalLinguistics. Haixia Sun, Jin Xiao, Wei Zhu, Yilong He, Sheng

### Zhang,XiaoweiXu,LiHou,JiaoLi,YuanNi,and

OpenAI.2023. GPT-4TechnicalReport. arXive-prints, Guotong Xie. 2020. Medical knowledge graph to
pagearXiv:2303.08774. enhancefraud,waste,andabusedetectiononclaim
data: Modeldevelopmentandperformanceevalua-
LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida, tion. JMIRMedInform,8(7):e17653.

### CarrollWainwright,PamelaMishkin,ChongZhang,

SandhiniAgarwal,KatarinaSlama,AlexRay,etal. TianxiangSun,XiangyangLiu,WeiZhu,ZhichaoGeng,

## Training languagemodelsto followinstruc- LinglingWu,YilongHe,YuanNi,GuotongXie,Xutions with human feedback. Advances in Neural anjing Huang, and Xipeng Qiu. 2022. A simple

InformationProcessingSystems,35:27730–27744. hash-basedearlyexitingapproachforlanguageunderstanding and generation. In Findings of the As-
Jonas Pfeiffer, Aishwarya Kamath, Andreas Rücklé, sociationforComputationalLinguistics: ACL2022,
Kyunghyun Cho, and Iryna Gurevych. 2021. pages2409–2421,Dublin,Ireland.Associationfor
AdapterFusion: Non-destructive task composition ComputationalLinguistics.
fortransferlearning. InProceedingsofthe16thConferenceoftheEuropeanChapteroftheAssociation Yi-Lin Sung, Jaemin Cho, and Mohit Bansal. 2022.
forComputationalLinguistics: MainVolume,pages Lst: Ladderside-tuningforparameterandmemory
487–503,Online.AssociationforComputationalLin- efficienttransferlearning. ArXiv,abs/2206.06522.
guistics.

### Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann

ChengweiQin,AstonZhang,ZhuoshengZhang,Jiaao Dubois,XuechenLi,CarlosGuestrin,PercyLiang,
Chen,MichihiroYasunaga,andDiyiYang.2023. Is and Tatsunori B. Hashimoto. 2023. Stanford alchatgptageneral-purposenaturallanguageprocess- paca: Aninstruction-followingllamamodel. https:
ingtasksolver? arXivpreprintarXiv:2302.06476. //github.com/tatsu-lab/stanford_alpaca.
Yujia Qin, Xiaozhi Wang, Yusheng Su, Yankai Lin, Hugo Touvron, Louis Martin, Kevin R. Stone, Peter
NingDing,ZhiyuanLiu,Juan-ZiLi,LeiHou,Peng Albert, Amjad Almahairi, Yasmine Babaei, Niko-
Li, Maosong Sun, and Jie Zhou. 2021. Exploring lay Bashlykov, Soumya Batra, Prajjwal Bhargava,
low-dimensionalintrinsictasksubspaceviaprompt ShrutiBhosale,DanielM.Bikel,LukasBlecher,Cristuning. ArXiv,abs/2110.07867. tianCantónFerrer, MoyaChen, GuillemCucurull,

### DavidEsiobu,JudeFernandes,JeremyFu,Wenyin

AlecRadford,JeffreyWu,RewonChild,DavidLuan, Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami,
DarioAmodei,IlyaSutskever,etal.2019. Language NamanGoyal, AnthonyS.Hartshorn, SagharHosmodelsareunsupervisedmultitasklearners. OpenAI seini,RuiHou,HakanInan,MarcinKardas,Viktor
blog,1(8):9. Kerkez,MadianKhabsa,IsabelM.Kloumann,A.V.

### Korenev,PunitSinghKoura,Marie-AnneLachaux,

PranavRajpurkar,JianZhang,KonstantinLopyrev,and ThibautLavril,JenyaLee,DianaLiskovich,Yinghai
PercyLiang.2016. SQuAD:100,000+questionsfor Lu,YuningMao,XavierMartinet,TodorMihaylov,
machinecomprehensionoftext. InProceedingsof PushkarMishra,IgorMolybog,YixinNie,Andrew
the2016ConferenceonEmpiricalMethodsinNatu- Poulton,JeremyReizenstein,RashiRungta,Kalyan
ralLanguageProcessing,pages2383–2392,Austin, Saladi, Alan Schelten, Ruan Silva, Eric Michael
Texas.AssociationforComputationalLinguistics. Smith,R.Subramanian,XiaTan,BinhTang,Ross

<!-- Page 12 -->

Taylor, Adina Williams, Jian Xiang Kuan, Puxin Methods in Natural Language Processing: System
Xu,ZhengxuYan,IliyanZarov,YuchenZhang,An- Demonstrations,pages38–45,Online.Association
gelaFan,MelanieKambadur,SharanNarang,Aure- forComputationalLinguistics.
lienRodriguez,RobertStojnic,SergeyEdunov,and
ThomasScialom.2023. Llama2: Openfoundation ZhuofengWu,SinongWang,JiataoGu,RuiHou,Yuxandfine-tunedchatmodels. ArXiv,abs/2307.09288. iao Dong, V. G. Vinod Vydiswaran, and Hao Ma.

## Idpg: An instance-dependent prompt gener-

AshishVaswani,NoamM.Shazeer,NikiParmar,Jakob ation method. In North American Chapter of the
Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz AssociationforComputationalLinguistics.

### Kaiser,andIlliaPolosukhin.2017. Attentionisall

youneed. ArXiv,abs/1706.03762. JingfangZhang,MingTan,PengyuDai,andWei-Guo

### Zhu. 2023a. Leco: Improving early exiting via

AlexWang,YadaPruksachatkun,NikitaNangia,Aman- learned exits and comparison-based exiting mechpreetSingh,JulianMichael,FelixHill,OmerLevy, anism. In Annual Meeting of the Association for
andSamuelR.Bowman.2019. Superglue:Astickier ComputationalLinguistics.
benchmarkforgeneral-purposelanguageunderstand-
LongtengZhang, LinZhang, ShaohuaiShi, Xiaowen
ingsystems. ArXiv,abs/1905.00537.

### Chu,andBoLi.2023b. Lora-fa: Memory-efficient

Alex Wang, Amanpreet Singh, Julian Michael, Felix low-rankadaptationforlargelanguagemodelsfine-
Hill, Omer Levy, and Samuel R. Bowman. 2018. tuning. ArXiv,abs/2308.03303.
Glue: A multi-task benchmark and analysis plat-

### QingruZhang,MinshuoChen,AlexanderW.Bukharin,

formfornaturallanguageunderstanding. InBlack-
Pengcheng He, Yu Cheng, Weizhu Chen, and
boxNLP@EMNLP.
Tuo Zhao. 2023c. Adaptive budget allocation for parameter-efficient fine-tuning. ArXiv,
Li Wang, Wei Zhu, Sihang Jiang, Sheng Zhang, Keabs/2303.10512.
qiangWang,YuanNi,GuoTongXie,andYanghua

### Xiao.2020. Mininginfrequenthigh-qualityphrases

TianyiZhang,FelixWu,ArzooKatiyar,KilianQ.Weinfrom domain-specific corpora. Proceedings of the
berger,andYoavArtzi.2020. Revisitingfew-sample
29thACMInternationalConferenceonInformation
bertfine-tuning. ArXiv,abs/2006.05987.
&KnowledgeManagement.
Xinpeng Zhang, Ming Tan, Jingfan Zhang, and Wei

### XuwuWang,LihanChen,WeiZhu,YuanNi,GuoTong


### Zhu.2023d. Nag-ner: aunifiednon-autoregressive

Xie,DeqingYang,andYanghuaXiao.2023. Multigenerationframeworkforvariousnertasks. InAntask entity linking with supervision from a taxonnualMeetingoftheAssociationforComputational
omy. KnowledgeandInformationSystems,65:4335
Linguistics.
–4358.

### YumingZhang,XiangxiangGao,WeiZhu,andXiaol-

JasonWei,MaartenBosma,VincentZhao,KelvinGuu,
ingWang.2023e. Fastner: Speedingupinferences
Adams Wei Yu, Brian Lester, Nan Du, Andrew M.
fornamedentityrecognitiontasks. InInternational

### Dai,andQuocV.Le.2021. Finetunedlanguagemod-

ConferenceonAdvancedDataMiningandApplicaelsarezero-shotlearners. ArXiv,abs/2109.01652.
tions.
Colin White, Mahmoud Safari, Rhea Sukthanker,

### YumingZhang,PengWang,MingTan,andWei-Guo


### BinxinRu,ThomasElsken,ArberZela,Debadeepta


### Zhu.2023f. Learnedadaptersarebetterthanman-

Dey, and Frank Hutter.2023. Neural Architecture
uallydesignedadapters. InAnnualMeetingofthe
Search: Insightsfrom1000Papers. arXive-prints,
AssociationforComputationalLinguistics.
pagearXiv:2301.08727.

### ZhenZhang,WeiZhu,JinfanZhang,PengWang,Rize

Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Jin, and Tae-Sun Chung. 2022. PCEE-BERT: Ac-
Chaumond,ClementDelangue,AnthonyMoi,Pierric celeratingBERTinferenceviapatientandconfident
Cistac, TimRault, RémiLouf, MorganFuntowicz, earlyexiting. InFindingsoftheAssociationforComet al. 2020a. Transformers: State-of-the-art natu- putationalLinguistics:NAACL2022,pages327–338,
rallanguageprocessing. InProceedingsofthe2020 Seattle,UnitedStates.AssociationforComputational
conferenceonempiricalmethodsinnaturallanguage
Linguistics.
processing: systemdemonstrations,pages38–45.

### ZhexiZhang,WeiZhu,JunchiYan,PengGao,andGuo-

Thomas Wolf, Lysandre Debut, Victor Sanh, Julien tongXie.2021. Automaticstudentnetworksearch
Chaumond,ClementDelangue,AnthonyMoi,Pier- for knowledge distillation. In 2020 25th InternaricCistac,TimRault,RémiLouf,MorganFuntowicz, tional Conference on Pattern Recognition (ICPR),
JoeDavison,SamShleifer,PatrickvonPlaten,Clara pages2446–2453.IEEE.

### Ma,YacineJernite,JulienPlu,CanwenXu,TevenLe

Scao, Sylvain Gugger, Mariama Drame, Quentin MengjieZhao,TaoLin,FeiMi,MartinJaggi,andHin-
Lhoest,andAlexanderM.Rush.2020b. Transform- richSchütze.2020. Maskingasanefficientalternaers: State-of-the-artnaturallanguageprocessing. In tivetofinetuningforpretrainedlanguagemodels. In
Proceedings of the 2020 Conference on Empirical Proceedings of the 2020 Conference on Empirical

<!-- Page 13 -->

MethodsinNaturalLanguageProcessing(EMNLP), HealthInformationProcessing.EvaluationTrackPapages2226–2241,Online.AssociationforComputa- pers,pages89–102,Singapore.SpringerNatureSintionalLinguistics. gapore.
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, WeiZhu,WenfengLi,XiaolingWang,WendiJi,Yuan-
XiaoleiWang,YupengHou,YingqianMin,Beichen bin Wu, Jin Chen, Liang Chen, and Buzhou Tang.
Zhang,JunjieZhang,ZicanDong,YifanDu,Chen 2023b. Extractingdecisiontreesfrommedicaltexts:
Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, An overview of the text2dt track in chip2022. In
Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, HealthInformationProcessing.EvaluationTrackPa-
PeiyuLiu,Jian-YunNie,andJi-RongWen.2023. A pers,pages89–102,Singapore.SpringerNatureSin-
SurveyofLargeLanguageModels. arXive-prints, gapore.
pagearXiv:2303.18223.
WeiZhu,YuanNi,XiaolingWang,andGuotongXie.
Huanran Zheng, Wei Zhu, Pengfei Wang, and Xiaol- 2021b. Discovering better model architectures for
ing Wang. 2023. Candidate soups: Fusing candi- medicalqueryunderstanding. InProceedingsofthe
date results improves translation quality for non- 2021ConferenceoftheNorthAmericanChapterof
autoregressivetranslation. ArXiv,abs/2301.11503. theAssociationforComputationalLinguistics: HumanLanguageTechnologies: IndustryPapers,pages
LianminZheng,Wei-LinChiang,YingSheng,Siyuan 230–237,Online.AssociationforComputationalLin-
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, guistics.

### ZhuohanLi,DachengLi,Eric.PXing,HaoZhang,


### JosephE.Gonzalez,andIonStoica.2023. Judging

Wei Zhu, Yuan Ni, Guo Tong Xie, Xiaofeng Zhou,
LLM-as-a-JudgewithMT-BenchandChatbotArena.
and Cai Chen. 2019a. The dr-kgqa system for auarXive-prints,pagearXiv:2306.05685.
tomaticallyansweringmedicationrelatedquestions
inchinese. 2019IEEEInternationalConferenceon
WeiZhu.2021a. Autonlu: Architecturesearchforsen-
HealthcareInformatics(ICHI),pages1–6.
tenceandcross-sentenceattentionmodelingwithredesignedsearchspace. InNaturalLanguageProcess-
Wei Zhu and Ming Tan. 2023. SPT: Learning to seingandChineseComputing:10thCCFInternational
lectively insert prompts for better prompt tuning.

### Conference,NLPCC2021,Qingdao,China,October

In Proceedings of the 2023 Conference on Empir-
13–17,2021,Proceedings,PartI10,pages155–168.
icalMethodsinNaturalLanguageProcessing,pages
Springer.
11862–11878,Singapore.AssociationforComputationalLinguistics.
WeiZhu.2021b. AutoRC:ImprovingBERTbasedrelationclassificationmodelsviaarchitecturesearch. In

### WeiZhu,PeifengWang,YuanNi,GuoTongXie,and


### Proceedingsofthe59thAnnualMeetingoftheAsso-

Xiaoling Wang. 2023c. Badge: Speeding up bert
ciationforComputationalLinguisticsandthe11th
inferenceafterdeploymentviablock-wisebypasses

### InternationalJointConferenceonNaturalLanguage

anddivergence-basedearlyexiting. InAnnualMeet-

### Processing: StudentResearchWorkshop,pages33–

ingoftheAssociationforComputationalLinguistics.
43,Online.AssociationforComputationalLinguistics.
Wei Zhu, Peng Wang, Xiaoling Wang, Yuan Ni, and

### GuotongXie.2023d. Acf: Alignedcontrastivefine-

Wei Zhu. 2021c. LeeBERT: Learned early exit for
tuningforlanguageandvisiontasks. InICASSP2023
BERTwithcross-leveloptimization. InProceedings
-2023IEEEInternationalConferenceonAcoustics,
of the 59th Annual Meeting of the Association for
SpeechandSignalProcessing(ICASSP),pages1–5.
ComputationalLinguisticsandthe11thInternational

### JointConferenceonNaturalLanguageProcessing

(Volume1: LongPapers),pages2968–2980,Online. Wei Zhu, Xiaoling Wang, Mosha Chen, and Buzhou
AssociationforComputationalLinguistics. Tang.2023e. Overviewofthepromptcblueshared
taskinchip2023. ArXiv,abs/2312.17522.

### WeiZhu.2021d. Mvp-bert: Multi-vocabpre-training

forchinesebert. InAnnualMeetingoftheAssocia- WeiZhu,XiaolingWang,YuanNi,andGuotongXie.
tionforComputationalLinguistics. 2021c. Autotrans: Automatingtransformerdesign
viareinforcedarchitecturesearch. InNaturalLan-
WeiZhu,YilongHe,LingChai,YuanchunFan,YuanNi, guage Processing and Chinese Computing, pages
GuoTongXie,andXiaolingWang.2021a. paht_nlp 169–182,Cham.SpringerInternationalPublishing.
@mediqa2021: Multi-grainedqueryfocusedmultianswersummarization. InWorkshoponBiomedical WeiZhu,XiaolingWang,YuanNi,andGuotongXie.
NaturalLanguageProcessing. 2021d. GAML-BERT:ImprovingBERTearlyexitingbygradientalignedmutuallearning. InProceed-
WeiZhu,WenfengLi,XiaolingWang,WendiJi,Yuan- ingsofthe2021ConferenceonEmpiricalMethods
bin Wu, Jin Chen, Liang Chen, and Buzhou Tang. inNaturalLanguageProcessing,pages3033–3044,
2023a. Extractingdecisiontreesfrommedicaltexts: OnlineandPuntaCana,DominicanRepublic.Asso-
An overview of the text2dt track in chip2022. In ciationforComputationalLinguistics.

<!-- Page 14 -->

WeiZhu,XiaolingWang,HuanranZheng,MoshaChen, to its bottleneck architecture. (Sung et al., 2022;
andBuzhouTang.2023. PromptCBLUE:AChinese JieandDeng,2022)trytoadddifferentencoding
PromptTuningBenchmarkfortheMedicalDomain.
operations,likeself-attentionoperationsandconvoarXive-prints,pagearXiv:2310.14151.
lutionsbetweenthebottleneckstructureofadapters,
Wei Zhu, Xiaofeng Zhou, Keqiang Wang, Xun Luo, andachievebetterperformances. Learned-Adapter
Xiepeng Li, Yuan Ni, and Guotong Xie. 2019b. (Zhangetal.,2023f)buildsupontheaboveadapter-

### PANLP at MEDIQA 2019: Pre-trained language

based methods and enhance the performance of
models,transferlearningandknowledgedistillation.
adaptertuningbyautomaticallylearningbetterar-

### In Proceedings of the 18th BioNLP Workshop and

SharedTask,pages380–388,Florence,Italy.Associ- chitecturesforadapters.
ationforComputationalLinguistics. Prompttuningmethods Prompttuning(Lester
etal.,2021)andP-tuning(Liuetal.,2022b)insert
YuhuiZuo,WeiZhu,andGuoyongGUETCai.2022.
a soft prompt to word embeddings only, and can

### Continuallydetection,rapidlyreact: Unseenrumors

detection based on continual prompt-tuning. In achievecompetitiveresultswhenappliedtosuper-
Proceedings of the 29th International Conference sized PTMs. Prefix-tuning (Li and Liang, 2021)
on Computational Linguistics, pages 3029–3041,
and P-tuning v2 (Liu et al., 2021) insert prompts
Gyeongju, Republic of Korea. International Comto every hidden layer of PTM. IDPG (Wu et al.,
mitteeonComputationalLinguistics.
2022) uses the prompt generator with parameter-
A Additionalrelatedworks izedhypercomplexmultiplication(Leetal.,2021)
togenerateasoftpromptforeveryinstance. LPT
Adapter-basedtuning. Oneofthemostimpor- (Liuetal.,2022a)improvesuponIDPGbyselecttantresearchlinesofPEFTisadapter-basedtuning. inganintermediatelayertostartinsertingprompts.
Adapter(Houlsbyetal.,2019)insertsadaptermod- SPT (Zhu and Tan, 2023) designs a mechanism
ules with bottleneck architecture between every toautomaticallydecidewhichlayerstoinsertnew
consecutiveTransformer(Vaswanietal.,2017)sub- instance-awaresoftprompts.
layers. AdapterFusion(Pfeifferetal.,2021)only LoRA methods Since LoRA is the most popinserts sequential adapters after the feed-forward ular PEFT method in the era of large language
module. Adapter-basedtuningmethodshavecom- models, there are many works that are orthogoparableresultswithmodeltuningwhenonlytun- nal to AdaLoRA, SoRA and our work that are
ing a fraction of the backbone model’s parame- devoted to improve LoRA on many different aster number. Due to their strong performance, a pects. QLoRA (Dettmers et al., 2023) proposes
branch of literature has investigated the architec- anovelquantizationmethodthatcansignificantly
tureofadaptersinsearchoffurtherimprovements. reduce the memory consumptions of LLMs dur-
He et al. (2021) analyze a wide range of PETun- ing LoRA fine-tuning. LoRA-FA (Zhang et al.,
ing methods and show that they are essentially 2023b) freezes parts of the randomly initialized
equivalent. They also propose the general archi- LoRAmatrices. (d)VERA(Kopiczkoetal.,2023)
tecture of PEFT, and derive the Parallel Adapter investigatewhetheronecouldfrozetherandomly
whichconnectstheadaptermodulesinparallelto initializedLoRAmatricesandonlylearnsasetof
theself-attentionandMLPmodulesintheTrans- scalingvectors. TyingLoRAmatricesacrosslayers
former block. AdapterDrop (Rücklé et al., 2020) arealsoinvestigatedbyVERA.
investigates the efficiency of removing adapters
from lower layers. Adaptive adapters (Moosavi B Appendixforthedatsetsandevaluation
etal.,2022)investigatetheactivationfunctionsof metrics
adaptersandproposetolearntheactivationfunc-

### B.1 DatasetsfromGLUEandSuperGLUE

tionsofadaptersviaoptimizingtheparametersof
rationalfunctionsasapartofthemodelparameters. We experiment on three tasks from the GLUE
Compacter(Mahabadietal.,2021)useslow-rank (Wang et al., 2018) benchmark: (a) (a) a sentiparameterized hypercomplex multiplication (Le mentclassificationtask,SST-2. (b)twobenchmark
etal.,2021)tocompressadapters’tunableparame- naturallanguageinferencetasks,RTEandQNLI.
ters. LST(Sungetal.,2022)improvesthememory Wealsoexperimentwiththreequestion-answering
efficiencybyformingtheadaptersasaladderalong tasks: (a)twoquestionansweringtasksintheforstacked Transformer blocks, and it enhances the mat of binary choices, COPA and BoolQ. (b) A
adaptermodulebyaddingaself-attentionmodule Squad (Rajpurkar et al., 2016) style question an-

<!-- Page 15 -->

Datasets #train #dev #test |Y| Type Labels Metrics

### SuperGLUEtasks


### BoolQ 9.4k 1.6k 1.6k 2 QuestionAnswering True,False acc

COPA 0.4k 0.05k 0.05k 2 QuestionAnswering choice1,choice2 acc
ReCoRD 101k 1k 7.4k - QuestionAnswering - f1-em

### GLUEtasks

SST-2 66k 1k 0.8k 2 sentimentclassification positive,negative acc
RTE 2.5k 0.1k 0.1k 2 NLI entailment,notentailment acc
QNLI 104k 1k 5.4k 2 NLI entailment,notentailment acc

### Othertasks

Squad 87k 1k 5.9k - QuestionAnswering - f1-em
E2E 42k 4.6k 4.6k - NLG - BLEU/ROUGE-L/METEOR

### Alpaca 52k - - - Instructiontuning - -


### MT-Bench - - 80 - Instructiontuning - GPT-4scores

Table5: ThedatasetstatisticsoftheGLUEandSuperGLUEbenchmarktasksevaluatedinthiswork. |Y|isthe
numberofclassesforaclassificationtask.
sweringtask,ReCoRD. detailedstatisticsofthistaskispresentedinTable
Sincetheoriginaltestsetsarenotpubliclyavail- 5.
ableforthesetasks,wefollowZhangetal.(2020);
Mahabadi et al. (2021); Zhu et al. (2023d); Gao B.3 Datasets: E2Ebenchmark
etal.(2023);Zhu(2021d,c);Zhangetal.(2022);

### TheE2Ebenchmarkdatasetfortrainingend-to-

Zuo et al. (2022); Sun et al. (2022); Zhu et al.
end, data-drivennaturallanguagegenerationsys-
(2021d);Zhu(2021a);Zhuetal.(2021c);Lietal.
temsintherestaurantdomain. Itasksamodelto
(2019); Zhu et al. (2019b); Zhu (2021b); Zhang
generatenaturalutterancesbasedonasetofgiven
et al. (2021); Wang et al. (2020) to construct the
keycontents. Thisdatasethasa42061/4672/4693
train/dev/testsplitsasfollowstoensureafiarcomtrain/dev/testsplit.
parison: (a)fordatasetswithfewerthan10ksamples(RTE,COPA,BoolQ),wedividetheoriginal B.4 Dataset: Instructiontuning
validationsetinhalf,usingonehalfforvalidation
Instructiontuningisanimportantmethodtoimandtheotherfortesting. (b)forlargerdatasets,we
prove the general capabilities of large language
split1ksamplesfromthetrainingsetasthedevelmodels (Ouyang et al., 2022). With the rise of
opment set, and use the original development set
largelanguagemodelsinthescaleof10Bparamasthetestset. ThedetailedstatisticsoftheGLUE
etersormore,likeGPT-3,T5,PaLM,researchers
andSuperGLUEbenchmarktasksispresentedin
have actively explored the few-shot or zero-shot
Table5.
capabilitiesofthesemodels. (Mishraetal.,2021)
find that fine-tuning these LLMs on a large scale

### B.2 TheSquadtask

datasetscontaininghundredsofNLPtaskssignif-
StanfordQuestionAnsweringDataset(SQuAD) icantly improves the zero-shot performances on
(Rajpurkaretal.,2016)isareadingcomprehension unseen tasks, establishing the scaling law of task
dataset, consisting of questions posed by crowd- numbers. Thepreviousworkslike(Weietal.,2021)
workersonasetofWikipediaarticles, wherethe andT0(Sanhetal.,2021)establishestheinstrucanswer to every question is a segment of text, or tiontuningdatasetsbytransformingthetraditional
span,fromthecorrespondingreadingpassage,or NLPtasksintoaunifiedpromptformat. Instructthequestionmightbeunanswerable. Thistaskis GPT (Ouyang et al., 2022) conducts instruction
oneofthemostwidelystudiedquestionanswering tuningusingthedatasetconstructedbasedtheuser
taskinthefield. queriesfromtheOpenAIAPIusers. Notethatthis
Inthiswork,weusethev1.1versionofSQUAD. work is also a seminal work for human feedback
Since the original test sets are not publicly avail- learningwithreinforcementlearning. However,the
ableforthesetasks,wefollowZhangetal.(2020); completeinstructiontuningdatasetfrom(Ouyang
Mahabadietal.(2021)andsplit1ksamplesfrom et al., 2022) remains closed. With the launch of
the training set as the development set, and use ChatGPT,(Taorietal.,2023)(Alpaca)constructs
the original development set as the test set. The an instruction tuning dataset with diverse topics

<!-- Page 16 -->

usingtheself-instructtechniques. transformallthetasksintoaprompt-responsefor-
For our experiment, we employ the Alpaca mat. Nowwepresenttheprompt-responsetemplate
dataset (Taori et al., 2023) for instruction tuning. foreachtask.
Specifically,weemploysitscleanedversion5. This Templates for RTE and QNLI Since these two
datasetcomprises51Kinstructionsanddemonstra- tasksareNLItasks,thesamplesinthemconsists
tions, and is suitable for instruction tuning. The oftwoinputtext,[sentence1]and[sentence1],and
cleaned version corrects multiple issues such as alabel[label_name](entailmentornotentailment).
hallucinations,mergedinstructions,andemptyout- Thus,weusethefollowingtemplates:
puts. Templateforprompt:
sentence 1: [sentence1]
B.5 Evaluationmetrics/protocols
sentence 2: [sentence1]
ForthethreeGLUEtasksweexperimenton,we Are sentence 1 and sentence 2 have
reportaccuracy(denotedasacc). ForReCoRD,we entailment relation or not?
report the average of the F1 score and the exact

### Templateforresponse:

match score (denoted as f1-em). For the BoolQ
[label_name]
and COPA tasks, we report accuracy. The above
choicesofevaluationmetricsstrictlyfollow(Wang TemplatesforSST-2Thesamplesinthistaskconetal.,2018)and(Wangetal.,2019). sistsofoneinputtext, [sentence], andalabel[la-
FortheSQUADdataset, wealsoreporttheav- bel_name](positiveornegative).
erage of the F1 score and the exact match score Templateforprompt:
(denotedasf1-em).
[sentence]
Following (Novikova et al., 2017), we report

### The sentiment of the given sentence is:

threedifferentmetricsontheE2Etask: (a)BLEU;

### Templateforresponse:

(b)ROUGE-L;(c)METEOR.WerelyontheHuggingFaceEvaluatepackage6 forcomputingthese [label_name]
metrics.

### Templates for BoolQ The samples in this task


### For evaluating the quality of instruction tuned

consists of a reference document, [doc], a query,
LlaMA-27B,wefollowthecurrentcommonprac-
[query],andalabel[label_name](yesorno).
tice of utilizing GPT-4 as a unbiased reviewer

### Templateforprompt:

(Zhengetal.,2023). 80instructionsfromtheMT-

### Reference document:

Bench is set as a test set. We generate model re-
[doc]
sponsesfromafine-tunedmodelwithbeamsize5

### Question:

withthegenerationfunctioninHuggingfaceTrans-
[query]
formers (Wolf et al., 2020a). Then we compare
SoRAandALoRA’sanswerswithGPT-4. Foreach Templateforresponse:
instructioninMT-Bench,GPT-4(OpenAI,2023) [label_name]
is asked to write a review for both answers from
TemplatesforCOPAThesamplesinthistaskconthetwomethods,andassignsaquantitativescore
sistsofapremise,[premise],twochoices,[choice1]
on a scale of 10 to each response. The prompts
and [choice2], a query, [query], and a label [laofinstructingGPT-4forevaluationispresentedin
bel_name](1or2,indicatingwhichchoiceiscon-
AppendixD.ROUGE-Lscorescomputedbyconsistentwiththepremise).
sidering the answers generated by GPT-4 as the
Templateforprompt:
groundtruth.

### Premise:

C Prompttemplatesforfine-tuning [premise]
LlaMA-27B Choice 1: [choice1]

### Choice 2: [choice2]

Since we fine-tune LlaMA-2 7B without intro-

### Question:

ducingtask-specificpredictionheads,weneedto
[query]
5https://huggingface.co/datasets/yahma/
Templateforresponse:
alpaca-cleaned.
6https://huggingface.co/docs/evaluate/index [label_name]

<!-- Page 17 -->


### Templates for ReCoRD and SQUAD The sam- Query:

ples in these two tasks consist of a context docu- [query]
ment,[context],aquestion,[query],andaanswer- Response 1 from assistant 1:
ingspan,[answer]. [response1]
Templateforprompt: Response 2 from assistant 2:
[response2]

### Context:

[context]
E AppendixforExperimentalsettings
Question:
[query]
Here,weprovidemoredetailsforexperimental
Templateforresponse: settings.
Hyper-parametersforthebaselinePEFTmeth-
[answer]
ods ForP-tuningV2,thenumberofpromptto-
TemplatesforE2EThesamplesinthistaskcon- kensateachlayerissetto160. ForSPT,thebotsistsofareference[ref],consistingrequiredinfor- tleneck dimension is set to 256, and the number
mation,andatargetedresponse,[target],whichis of prompt layers is set to 8. For adapter-based
a customer review written according to the refer- methods,thebottleneckdimensionissetto40,and
ence’scontents. theadaptermodulesareaddedontheself-attention

### Templateforprompt: andfeed-forwardmodule. ForLoRAandALoRA,

Reference: the initial rank at each module is set to 8. For
[ref] AdaLoRA, SoRA, and SaLoRA, the initial rank
Generate a customer review following the at each module is set to 16, and half of the rank
given reference. budgetisprunedduringfine-tuning. Weadjustthe
sparsityforSSPsothatthenumberoftunablepa-

### Templateforresponse:

rametersiscomparablewithALoRAandtheother
[target]
baselines.
Training settings for PEFT methods We use

### D PrompttemplatesforGPT-4

theHugginFaceTransformers(Wolfetal.,2020b)
evaluations
andPEFT(Mangrulkaretal.,2022)forimplement-
Inthiswork,weutilizethepowerfulLLMGPT-4 ing all the methods, and for training and making
(OpenAI,2023)astheevaluatorforcomparingthe predictions. For fine-tuning LlaMA-2 7B model,
instruction tuning quality. As a reviewer, GPT-4 themaximumsequencelengthissetto2048. The
will receive a query [query], two responses, [re- maximum training epoch is set to 10. The batch
sponse1]and[response2],fromtwoassistants. We size is setbetween 16 for task withless than 10k
willaskGPT-4towriteareviewforeachresponse, training set, and 128 otherwise. We use AdamW
assessingthequalityoftheresponse,andthenask asthe optimizerwitha linearlearning rate decay
GPT-4 to assign a score on a scale of 10 to each scheduleand6%ofthetrainingstepsforwarm-up.
response. The learning rate is set to 1e-4. The other hyper-
Templateforprompt: parameters are kept the same with (Wolf et al.,
2020b). Inevery200steps,themodelisevaluated

### Task Introduction

on the dev set. Patience is set to 10, that is, if
you will be given a query, and two responses
the model does not achieve a lower development
from two assistants,
set loss for 10 evaluation runs, the training stops.
could you compare the two responses,
The best checkpoint on the dev set is used to run
and do the following:
predictionsonthetestset.
(1) write a concise review for each
assistant's response, on how well the

### F AblationontheALoRAframework

response answers the query, and whether
it will be helpful to humans users, and any WeconsidertwovariantsofALoRA:(a)usethe
issues in the response; architecturalweightsα′ astheimportancescores
m,i
(2) assigns a quantitative score on a scale during bi-level optimization (Liu et al., 2019a).
of 10 to each response, reflecting This variant is denoted as ALoRA-DNAS. (b)
your assessment of the two responses Use the sensitivity-based metric in Zhang et al.

<!-- Page 18 -->

BoolQ ReCoRD Squad

### Method

(acc) (f1-em) (f1-em)

### ALoRA-DNAS 87.6 91.2 88.7

ALoRA-Sensi 87.5 91.3 88.6

### ALoRA 88.0 91.8 89.2

Table 6: The comparison of ALoRA’s variants on
theBoolQ,ReCoRD,andSquadtasks. Thebackbone
modelisLlaMA-27B.
(2023c)astheimportancemeasurement. (denoted
asALoRA-Sensi). TheexperimentsontheBoolQ
andE2Emethodsareprovidedin6
G Ablationonthepretrainedbackbones Figure4: ThefinalrankallocationsofSoRAafterfinetuningtheLlaMA-27BmodelontheE2Etask.
Our main experiments are conducted on the

### LlaMA-2 7B model. To demonstrate that our

the Alpaca dataset. Now we present concrete exmethodworkswellregardlessofthebackbonemodamples in Table 9 to showcase the Superiority of
els,wenowconductexperimentsontheRoBERTa-
ALoRA.
large. Inthisexperiment,sincethelanguagemodelingcapabilitiesoftheseRoBERTa-largecannot
matchLlaMA-27Bmodel,wechangethefollowing setting for the prediction head: (a) we use a
linearlayerasthepredictionheadforclassification
tasks. (b)fortheReCoRDtask,weusetwolinear
layerstopredictthestartingandendingpositions
of a entity span. The other experimental settings
arekeptthesamewiththemainexperiments(Table
1).

### WeconductexperimentsontheBoolQ,ReCoRD

andSquadtasks. TheresultsarereportedinTable

## We can see that on the RoBERTa-large backbone,ourmethodcanalsooutperformthebaseline

methods.

### WealsorunGPT2-largeontheE2Etask,andthe

resultsarereportedinTable8. Theresultsdemonstrate that when the GPT2-large is the backbone
model,ourALoRAmethodalsooutperformsthe
baselines.
H Visualizationofthefinalrank
allocationsofSoRA

### Inthemaincontents,wevisualizethefinalrank

allocationsofALoRAafterthetrainingprocesson
theE2EtaskinFigure3. Ascomparison,wenow
present the LoRA rank allocations by the SoRA
methodinFigure4.

### I CasestudiesofInstructiontuning

IntheSection4.4ofthemaincontent,wepresent
theoverallperformanceofALoRAandSoRAon
the MT-Bench, after fine-tuning LlaMA-2 7B on

<!-- Page 19 -->

AdditionalParams BoolQ ReCoRD Squad

### Method

Initial Final (acc) (f1-em) (f1-em)

### ResultsforRoBERTa-large

Learned-Adapter 366M 354M 86.8 90.2 88.7
LoRA 3.54M 3.54M 86.9 90.0 88.6

### SoRA 708M 3.53M 87.2 90.1 88.7


### ALoRA 3.54M 3.42M 87.6 90.7 89.4

Table7: ThecomparisonontheBoolQ,ReCoRD,andSquadtasks,whenthebackbonemodelisRoBERTa-large.
Wereportthemedianperformanceover5randomseeds. BoldandUnderlineindicatethebestandthesecondbest
results. ThemetricforeachtaskisexplainedinAppendixB.5.

### Method BLEU ROUGE-L METEOR

Learned-Adapter 68.6 69.6 45.2
LoRA 68.7 69.8 45.3

### SoRA 68.9 69.9 45.4


### ALoRA 69.3 70.4 46.0

Table 8: Results for different PEFT methods on the
E2Ebenchmark. ThebackboneLMisGPT2-large. The
metricsareexplainedinAppendixB.5.

<!-- Page 20 -->


### Editthefollowingparagraphtocorrectanygrammaticalerrors:

Shedidn’tremembrewhereisherpurse,soIthinksitsinthecarbuthe’ssay
Query it’sonkitchentablebuthearenotsure,andthentheyaskedmetolookingfor
it,she’ssay,"Canyou?",andIrespondswith,"Maybe,butain’tnosure,"and
henotheardme,and,"What?",heasks,"Didyoufoundit?".

### ALoRA’sresponse

Shedidn’trememberwhereherpursewas,soIthoughtitwasinthecar,buthe
saiditwasonthekitchentable,buthewasn’tsure,andthentheyaskedmeto

### Responses

lookforit,shesaid,"Canyou?"andIrespondedwith,"Maybe,butI’mnot
sure,"andhedidn’thearme,andthenheasked,"Didyoufindit?"
Assistant1’sresponseeffectivelycorrectsallthegrammaticalerrorsinthe
originalparagraph. Theassistanthascorrectlychanged"remembre"to
"remember,"rearrangedtheclauseorderfrom"whereisherpurse"to"where
herpursewas,"andadjustedverbformsforproperagreement(e.g.,changing
"thinks"to"thought"). Quotationmarksandcommasareproperlyused,making

### GPT-4’s

directspeechclearandpunctuatedcorrectly. Theconjunctionsarebetterplaced,
comments
contributingtoamorenaturalflowofsentences. Additionally,allinstancesof
colloquialorincorrectlanguagesuchas“ain’tnosure”havebeenrevisedinto
standardEnglish("I’mnotsure"). Overall,thisresponsewouldbeveryhelpful
tohumanusersasitprovidesagrammaticallysoundversionoftheoriginaltext.

### GPT-4score 9


### SoRA’sresponse

Shedidn’trememberwhereherpursewas,soIthoughtitwasinthecar,buthe
saiditwasonthekitchentable,buthewasn’tsure. Theyaskedmetolookforit,

### Responses

andshesaid,"Canyou?"Irespondedwith,"Maybe,butI’mnotsure."Hedidn’t
hearme,andheasked,"What?"Isaid,"Didyoufindit?"
Assistant2alsodoesanexcellentjobcorrectinggrammaticalmistakesfromthe
initialquery. Thisassistantsimilarlyfixesissueswithverbtenseconsistencyand
subject-verbagreement(e.g.,“he’ssay”correctedto“hesaid”). However,there
isaslightdeviationattheendwhereAssistant2writes: “Isaid,’Didyoufind
it?’”. ThisseemslikeanattemptbyAssistant2tomakesenseofaconfusing

### GPT-4’s

partofdialogueinwhichspeakerroleswereunclearbutresultsinalteringthe
comments
meaningslightlybecauseitsuggeststhat‘I’amaskingif‘he’founditrather
thanhimasking‘me’. Thiscouldbemisleadingorconfusingwithoutadditional
contextindicatingwhoisspeakingatthatmoment. Nevertheless,punctuation
aroundquotationsisaccuratewhichaidsreadability.

### GPT-4score 8

Table9: Anexampleshowcasingthatthefine-tuningqualityofALoRAishigherthanSoRA.