---
title: "Prompt Tuning Soft Prompts"
original_file: "./Prompt_Tuning_Soft_Prompts.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "fine-tuning"]
keywords: ["prompt", "model", "task", "tuning", "text", "page", "training", "parameters", "table", "language"]
summary: "<!-- Page 1 -->

The Power of Scale for Parameter-Efficient Prompt Tuning
BrianLester∗ RamiAl-Rfou NoahConstant

### GoogleResearch

{brianlester,rmyeid,nconstant}@google.com

### Abstract


### In this work, we explore “prompt tuning,” 100

a simple yet effective mechanism for learning “soft prompts” to condition frozen lan- 90
guagemodelstoperformspecificdownstream
tasks.Unlikethediscretetextpromptsusedby 80
GPT-3,softpromptsarelearnedthroughbackpropagation and can be tuned to incorporate 70
s"
related_documents: []
---

# Prompt Tuning Soft Prompts

<!-- Page 1 -->

The Power of Scale for Parameter-Efficient Prompt Tuning
BrianLester∗ RamiAl-Rfou NoahConstant

### GoogleResearch

{brianlester,rmyeid,nconstant}@google.com

### Abstract


### In this work, we explore “prompt tuning,” 100

a simple yet effective mechanism for learning “soft prompts” to condition frozen lan- 90
guagemodelstoperformspecificdownstream
tasks.Unlikethediscretetextpromptsusedby 80
GPT-3,softpromptsarelearnedthroughbackpropagation and can be tuned to incorporate 70
signalsfromanynumberoflabeledexamples.
Ourend-to-endlearnedapproachoutperforms
60
GPT-3’s few-shot learning by a large margin.
Moreremarkably,throughablationsonmodel
50
sizeusingT5,weshowthatprompttuningbe- 108 109 1010 1011
comes more competitive with scale: as mod- Model Parameters
elsexceedbillionsofparameters, ourmethod
“closes the gap” and matches the strong performance of model tuning (where all model
weights are tuned). This finding is especially
relevant because large models are costly to
share and serve and the ability to reuse one
frozen model for multiple downstream tasks
caneasethisburden. Ourmethodcanbeseen
as a simplification of the recently proposed
“prefixtuning”ofLiandLiang(2021)andwe
provideacomparisontothisandothersimilar
approaches. Finally, we show that conditioning a frozen model with soft prompts confers
benefits in robustness to domain transfer and
enablesefficient“promptensembling.”
1 Introduction
With the wide success of pre-trained large languagemodels,arangeoftechniqueshasarisento
adaptthesegeneral-purposemodelstodownstream
tasks. ELMo(Petersetal.,2018)proposedfreezing
thepre-trainedmodelandlearningatask-specific
weighting of its per-layer representations. However,sinceGPT(Radfordetal.,2018)andBERT
(Devlinetal.,2019),thedominantadaptationtechnique has been model tuning (or “fine-tuning”),
whereallmodelparametersaretunedduringadaptation,asproposedbyHowardandRuder(2018).
∗ WorkdoneasaGoogleAIResident.
erocS

### EULGrepuS


### Model Tuning Prompt Design


### Model Tuning (Multi-task) Prompt Tuning


### Figure1:StandardmodeltuningofT5achievesstrong

performance,butrequiresstoringseparatecopiesofthe
model for each end task. Our prompt tuning of T5
matches the quality of model tuning as size increases,
while enabling the reuse of a single frozen model for
alltasks. OurapproachsignificantlyoutperformsfewshotpromptdesignusingGPT-3. Weshowmeanand
standarddeviationacross3runsfortuningmethods.

### Morerecently,Brownetal.(2020)showedthat

promptdesign(or“priming”)issurprisinglyeffectiveatmodulatingafrozenGPT-3model’sbehavior
throughtextprompts. Promptsaretypicallycomposedofataskdescriptionand/orseveralcanonical
examples. This return to “freezing” pre-trained
modelsisappealing,especiallyasmodelsizecontinuestoincrease. Ratherthanrequiringaseparate
copy of the model for each downstream task, a
singlegeneralistmodelcansimultaneouslyserve
manydifferenttasks.
Unfortunately,prompt-basedadaptationhasseveralkeydrawbacks. Taskdescriptioniserror-prone
andrequireshumaninvolvement,andtheeffectivenessofapromptislimitedbyhowmuchconditioningtextcanfitintothemodel’sinput. Asaresult,
downstream task quality still lags far behind that
of tuned models. For instance, GPT-3 175B fewshotperformanceonSuperGLUEis17.5pointsbe-
1202
peS
2
]LC.sc[
2v19680.4012:viXra

<!-- Page 2 -->

Pre-trained with Li and Liang (2021) and Hambardzumyan

### Model Tuning Model Prompt Tuning

(11B params) etal.(2021),wearethefirsttoshowthatprompt
a1 Mixed-task tuningalone(withnointermediate-layerprefixesor

### Task A a2 Task A Model Batch

Batch (11B params) A A a1 task-specificoutputlayers)issufficienttobecom-

### C c1 Pre-trained

Task B b1 Task B Model B B A b a 1 2 (11B M p o a d r e a l ms) petitive with model tuning. Through detailed ex-
Batch (11B params) C C c2 perimentsinsections2–3,wedemonstratethatlan-

### Task Prompts

c1 (20K params each) guagemodelcapacityisakeyingredientforthese

### Task C c2 Task C Model

Batch (11B params) approachestosucceed. AsFigure1shows,prompt
tuningbecomesmorecompetitivewithscale.

### Figure 2: Model tuning requires making a task-

We compare with similar approaches in Secspecific copy of the entire pre-trained model for each
tion 4. Explicitly separating task-specific paramdownstream task and inference must be performed in
etersfromthe“generalist”parametersneededfor
separate batches. Prompt tuning only requires storing a small task-specific prompt for each task, and generallanguage-understandinghasarangeofadenables mixed-task inference using the original pre- ditional benefits. We show in Section 5 that by
trained model. With a T5 “XXL” model, each copy capturing the task definition in the prompt while
ofthetunedmodelrequires11billionparameters. By keepingthegeneralistparametersfixed,weareable
contrast,ourtunedpromptswouldonlyrequire20,480
toachievebetterresiliencetodomainshifts. InSecparameterspertask—areductionofoverfiveordersof
tion6,weshowthat“promptensembling”,learnmagnitude—assumingapromptlengthof5tokens.
ingmultiplepromptsforthesametask,canboost
qualityandismoreefficientthanclassicmodelensembling. Finally,inSection7,weinvestigatethe
lowfine-tunedT5-XXL(Raffeletal.,2020)(71.8
interpretabilityofourlearnedsoftprompts. Insum,
vs.89.3)despiteusing16timesmoreparameters.
ourkeycontributionsare:

### Severaleffortstoautomatepromptdesignhave

beenrecentlyproposed. Shinetal.(2020)propose 1. Proposingprompttuningandshowingitscomasearchalgorithmoverthediscretespaceofwords, petitivenesswithmodeltuningintheregime
guidedbythedownstreamapplicationtrainingdata. oflargelanguagemodels.
Whilethistechniqueoutperformsmanualprompt 2. Ablatingmanydesignchoices,andshowing
design,thereisstillagaprelativetomodeltuning. qualityandrobustnessimprovewithscale.
Li and Liang (2021) propose “prefix tuning” 3. Showing prompt tuning outperforms model
andshowstrongresultsongenerativetasks. This tuningondomainshiftproblems.
method freezes the model parameters and back- 4. Proposing“promptensembling”andshowing
propagates the error during tuning to prefix ac- itseffectiveness.
tivations prepended to each layer in the encoder
2 PromptTuning
stack,includingtheinputlayer. Hambardzumyan
etal.(2021)simplifythisrecipebyrestrictingthe

### Followingthe“text-to-text”approachofT5(Raffel

trainable parameters to the input and output subet al., 2020), we cast all tasks as text generation.
networksofamaskedlanguagemodel,andshow
Insteadofmodelingclassificationastheprobabilreasonableresultsonclassificationstasks.
ityofanoutputclassgivensomeinput,Pr(y|X),
In this paper, we propose prompt tuning as a whereX isaseriesoftokensandyisasingleclass
furthersimplificationforadaptinglanguagemodels. label,wenowmodelitasconditionalgeneration,
Wefreezetheentirepre-trainedmodelandonlyal- where Y is a sequence of tokens that represent a
lowanadditionalk tunabletokensperdownstream classlabel. T5modelsclassificationasPr (Y|X),
θ
task to be prepended to the input text. This “soft parameterizedbytheweights,θ,ofthetransformprompt” is trained end-to-end and can condense ers(Vaswanietal.,2017)thatmakeupitsencoder
thesignalfromafulllabeleddataset,allowingour anddecoder.
methodtooutperformfew-shotpromptsandclose Prompting is the approach of adding extra inthe quality gap with model tuning (Figure 1). At formationforthemodeltoconditiononduringits
thesametime,sinceasinglepre-trainedmodelis generation of Y. Normally, prompting is done
recycledforalldownstreamtasks,weretaintheef- by prepending a series of tokens, P, to the inficientservingbenefitsoffrozenmodels(Figure2). put X, such that the model maximizes the likeli-
While we developed our method concurrently hoodofthecorrectY,Pr (Y|[P;X]),whilekeep-
θ

<!-- Page 3 -->

ing the model parameters, θ, fixed. In GPT-3, prompt. TheparametercostofourmethodisEP,
the representations of the prompt tokens, P = whereE isthetokenembeddingdimensionandP
{p ,p ,...,p }, are part of the model’s embed- isthepromptlength. Theshortertheprompt,the
1 2 n
ding table, parameterized by the frozen θ. Find- fewernewparametersmustbetuned,soweaimto
inganoptimalpromptthusrequirestheselection findaminimallengththatstillperformswell.
of prompt tokens, through either manual search
ornon-differentiablesearchmethods(Jiangetal., 2.2 UnlearningSpanCorruption
2020; Shin et al., 2020). Prompt tuning removes
UnlikeautoregressivelanguagemodelslikeGPT-3,
therestrictionthatthepromptP beparameterized
theT5modelsweexperimentwithuseanencoderbyθ;insteadtheprompthasitsowndedicatedpadecoder architecture and pre-train on a span corrameters, θ , thatcanbeupdated. Whileprompt

## P

ruption objective. Specifically, T5 is tasked with
design involves selecting prompt tokens from a
“reconstructing” masked spans in the input text,
fixed vocabulary of frozen embeddings, prompt
whicharemarkedwithuniquesentineltokens. The
tuning can be thought of as using a fixed prompt
target output text consists of all the masked conof special tokens, where only the embeddings of
tent, separated by sentinels, plus a final sentinel.
theseprompttokenscanbeupdated. Ournewcon-
Forinstance,fromthetext“Thankyouforinviting
ditional generation is now Pr (Y|[P;X]) and
θ;θP
me to your party last week” we might construct
canbetrainedbymaximizingthelikelihoodofY
apre-trainingexamplewheretheinputis“Thank
viabackpropagation,whileonlyapplyinggradient
you(cid:104)X(cid:105)metoyourparty(cid:104)Y(cid:105)week”andthetarget
updatestoθ .

## P

outputis“(cid:104)X(cid:105)forinviting(cid:104)Y(cid:105)last(cid:104)Z(cid:105)”.
Givenaseriesofntokens,{x ,x ,...,x },the
1 2 n

### WhileRaffeletal.(2020)findthisarchitecture

first thing T5 does is embed the tokens, forming
amatrixX ∈ Rn×e whereeisthedimensionof andpre-trainingobjectivemoreeffectivethantradie
tionallanguagemodeling,wehypothesizethatthis
theembeddingspace. Oursoft-promptsarerepresented as a parameter P ∈ Rp×e, where p is the setupisnotagoodfitforproducingafrozenmodel
e
thatcanbereadilycontrolledthroughprompttunlengthoftheprompt. Ourpromptisthenconcateing. In particular, a T5 model pre-trained exclunatedtotheembeddedinputformingasinglematrix[P ;X ] ∈ R(p+n)×e whichthenflowsthough sivelyonspancorruption,suchasT5.1.1,hasnever
e e
seen truly natural input text (free of sentinel tothe encoder-decoder as normal. Our models are
kens), nor has it ever been asked to predict truly
trainedtomaximizetheprobabilityofY,butonly
natural targets. In fact, due to the details of T5’s
thepromptparametersP areupdated.
e
spancorruptionpreprocessing,everypre-training
targetwillbeginwithasentinel. Whilethis“unnat-
2.1 DesignDecisions
ural”tendencytooutputsentinelsiseasytoover-
There are many possible ways to initialize the comethroughfine-tuning,wesuspectthatitwould
prompt representations. The simplest is to train bemuchhardertooverridethroughapromptalone,
fromscratch,usingrandominitialization. Amore asthedecoderpriorscannotbeadjusted.
sophisticated option is to initialize each prompt Given these concerns, we experiment with T5
token to an embedding drawn from the model’s models in three settings. (1) “Span Corruption”:
vocabulary. Conceptually, our soft-prompt mod- Weusepre-trainedT5off-the-shelfasourfrozen
ulates the frozen network’s behavior in the same model, and test its ability to output the expected
wayastextprecedingtheinput,soitfollowsthat text for downstream tasks. (2) “Span Corruption
a word-like representation might serve as a good +Sentinel”: Weusethesamemodel,butprepend
initializationspot. Forclassificationtasks,athird all downstream targets with a sentinel, so as to
optionistoinitializethepromptwithembeddings more closely resemble the targets seen in prethat enumerate the output classes, similar to the training. (3)“LMAdaptation”: WecontinueT5’s
“verbalizers”ofSchickandSchütze(2021). Since self-supervisedtrainingforasmallnumberofadwewantthemodeltoproducethesetokensinthe ditional steps, but using the “LM” objective disoutput,initializingthepromptwiththeembeddings cussedbyRaffeletal.(2020);givenanaturaltext
ofthevalidtargettokensshouldprimethemodel prefixasinput,themodelmustproducethenatural
torestrictitsoutputtothelegaloutputclasses. textcontinuationasoutput. Crucially,thisadapta-
Anotherdesignconsiderationisthelengthofthe tionhappensonlyonce,producingasinglefrozen

<!-- Page 4 -->

modelthatwecanreuseforprompttuningacross ingrateof0.3andabatchsizeof32. Checkpoints
anynumberofdownstreamtasks. areselectedviaearlystoppingonthedevelopment
Through LM adaptation, we hope to “quickly” set, where the stopping metric is the default mettransformT5intoamodelmoresimilartoGPT-3, ric for the dataset, or the average of metrics for
whichalwaysoutputsrealistictext,andisknownto datasets evaluated with multiple metrics. All exrespondwelltopromptsasa“few-shotlearner”. It perimentswereruninJAX(Bradburyetal.,2018)
isnotobvioushowsuccessfulthislate-stagetrans- usingtheAdafactoroptimizer(ShazeerandStern,
formation will be compared to pre-training from 2018)withweightdecay1e−5,β decay0.8,and
2
scratch,andithasnotbeeninvestigatedpreviously parameter scaling off. The models were impleto our knowledge. As such, we experiment with mented in Flax (Heek et al., 2020). More details
variouslengthsofadaptationupto100Ksteps. areavailableinAppendixA.
3 Results 3.1 ClosingtheGap

### Tocompareourmethodwithstandardmodeltun-


### Ourfrozenmodelsarebuiltontopofpre-trained

ing, we tune the public T5.1.1 checkpoints on
T5checkpointsofallsizes(Small,Base,Large,XL,
SuperGLUE using the default hyperparameters

### XXL).WeleveragethepublicT5.1.1checkpoints,

specified in the T5 library (learning rate 0.001,
whichincludeimprovementsovertheoriginalT5.1
andAdafactoroptimizerwithpre-trainingparam-

### Our“default”configuration,plottedwithagreen

eter states restored). We consider two baselines.
‘×’( )throughout,usesanLM-adaptedversion
(1)“ModelTuning”: Foranapples-to-applescomof T5 trained for an additional 100K steps, iniparison,wetuneoneachtaskseparately,asinour
tializes using class labels (see Section 3.2), and
prompttuningsetup.3 (2)“ModelTuning(Multiuses a prompt length of 100 tokens. While this
task)”: We use T5’s multi-task tuning setup to
islongerthanthedefault10-tokenprefixusedby
achieveamorecompetitivebaseline.4 Inthiscase,
Li and Liang (2021), our method still uses fewer
asinglemodelistunedonalltasksjointly,witha
task-specificparameters,asweonlytunetheinput
textprefixindicatingthetaskname.
layer,asopposedtooverwritingactivationsinall

### In Figure 1 (p. 1), we see that prompt tuning

network layers. See Figure 4 for a detailed combecomes more competitive with model tuning as
parison. We will also see shortly that even much
scaleincreases. AttheXXLsize(11billionparamshorterpromptsareviableasmodelsizeincreases.
eters), prompt tuning matches even the stronger

### We measure performance on the SuperGLUE

multi-task model tuning baseline, despite having
benchmark (Wang et al., 2019a), a collection of
over20,000timesfewertask-specificparameters.
eightchallengingEnglishlanguageunderstanding

### To compare with prompt design, we include

tasks.2 Wereportmetricsonthedevelopmentset
GPT-3few-shotperformanceontheSuperGLUE
associatedwitheachdataset.
dev split, as reported by Brown et al. (2020).5

### Each of our prompts train on a single Super-


### Figure 1 shows that prompt tuning beats GPT-3

GLUEtask;therewasnomulti-tasksetupormixprompt design by a large margin, with promptingoftrainingdataacrosstasks. Wetranslateeach
tuned T5-Small matching GPT-3 XL (over 16
SuperGLUEdatasetintoatext-to-textformatfoltimeslarger),andprompt-tunedT5-Largebeating
lowingRaffeletal.(2020),exceptthatweomitthe
GPT-3175B(over220timeslarger).
task namesprepended toinputs indicating which
SuperGLUEtaskanexamplebelongsto. 3Toimprovethisbaseline,weperformedasweepoverthe
batchsizehyperparameterandselected216tokensperbatch.

### Wetrainourpromptsfor30,000stepsusingT5’s

4TheT5SuperGLUEsubmissionusedamorecomplex
standardcross-entropyloss,withaconstantlearn- setup,firstmixingmulti-tasksuperviseddataintopre-training,
andthenperformingsingle-taskfine-tuning. Sinceweuse
1Theseimprovementsare(1)theremovalofallsupervised T5.1.1throughout,thissetupisunavailable,asthepre-training
datafrompre-training, (2)adjustmentstohyperparameters phaseisfullyself-supervised.WefollowRaffeletal.(2020)
d and d , and (3) the use of GeGLU (Shazeer, 2020) in using 220 tokens per batch and including DPR data in
model ff
overReLU(NairandHinton,2010)activations. themulti-taskmixture,whichisknowntoboostWSCtask
2ThetasksareBoolQ(Clarketal.,2019),CB(DeMarn- performance(Kocijanetal.,2019).
effetal.,2019), COPA(Roemmeleetal.,2011), MultiRC 5WealsoexperimentedwithusingGPT-3’smanualtext
(Khashabietal.,2018),ReCoRD(Zhangetal.,2018),RTE promptsdirectlywithourLM-adaptedT5checkpoints.How-
(Daganetal.,2005;Bar-Haimetal.,2006;Giampiccoloetal., everperformancewasfarbelowGPT-3forcomparablemodel
2007;Bentivoglietal.,2009),WiC(PilehvarandCamacho- sizes.Thismaybeduetodifferencesinpre-trainingdataand
Collados,2018),andWSC(Levesqueetal.,2012). modelarchitecture,aswellasT5’sshortersequencelength.

<!-- Page 5 -->

100
90
80
70
60
50
108 109 1010
Model Parameters
erocS
EULGrepuS
100
1
5
20 90
100
150
80
70
60
50
108 109 1010
Model Parameters
(a)Promptlength
erocS

### EULGrepuS

Random Uniform
Sampled Vocab

### Class Label

(b)Promptinitialization
100
90
80
70
60
50
40
30
20
10
108 109 1010
Model Parameters
erocS
EULGrepuS
100

### Span Corruption


### Span Corruption 90

+ Sentinel LM Adaptation 80

## (100K) 70

60
50
40
30
20
10
108 109 1010

### Model Parameters

(c)Pre-trainingmethod
erocS
EULGrepuS

## 0K


## 10K


## 50K 100K

(d)LMadaptationsteps
Figure3:Ablationsofvarioushyperparametersonprompttuningperformance(meanandstddevacross3runs).In
our“default”( )configuration,qualityimprovesstablywithmodelsize. Acrossallablations,thelargest(XXL)
modelisthemostrobusttohyperparameterchoice.(a)Promptlength:Increasingto20+tokensgenerallyconfers
alargeboost,butXXLperformswellevenwithsingle-tokenprompts.(b)Promptinitialization:Randomuniform
initializationlagsbehindmore“advanced”initializationsusingsampledvocabularyorclasslabelembeddings,but
thedifferencevanishesatXXLsize.(c)Pre-trainingobjective:LMadaptationoutperformsspancorruption,even
whenasentinelisaddedtodownstreamtasktargets,butXXLworkswellwithanymethod. (d)LMadaptation:
Longeradaptationgenerallygiveslargergains,butXXLisrobusttoevenshortadaptation.
3.2 AblationStudy formly from the range [−0.5, 0.5]. When initializingfromsampledvocabulary,werestricttothe

### Prompt Length We train prompts for each

5,000 most “common” tokens in T5’s Sentencemodel size while varying the prompt length in
Piece vocabulary (Kudo and Richardson, 2018),
{1,5,20,100,150}andfixingothersettingstoour
whichisorderedbylikelihoodinthepre-training
default configuration. Figure 3(a) shows that for
corpus. For “class label” initialization, we take
mostmodelsizes,increasingpromptlengthbeyond
the embeddings for the string representations of
a single token is critical to achieve good perforeachclassinthedownstreamtaskandusethemto
mance. Notably,theXXLmodelstillgivesstrong
initialize one of the tokens in the prompt. When
resultswithasingle-tokenprompt,suggestingthat
aclasslabelismulti-token,weaveragethetoken
the larger the model, the less conditioning signal
embeddings. At longerpromptlengths, we often
isneededtoachieveatargetbehavior. Acrossall
runoutofclasslabelsbeforewehaveinitializedall
models, increasing beyond 20 tokens only yields
oftheprompttokens. Inthiscasewefallbackto
marginalgains.6
oursampledvocabstrategytofillintheprompt.7
Prompt Initialization We ablate the effect of Figure3(b)showsourablationofinitialization
promptinitializationbytrainingmodelsatallsizes strategy across model sizes, where we find that
whilefixingotherhyperparameterstotheirdefault
values. Forrandominitialization,wesampleuni- 7T5’shandlingoftheReCoRDandWSCtasksrequires
themodeltogenerateshort,free-formtext.Inthesecases,we
6Going past 100 tokens appears mildly detrimental for initializethepromptswithwordsrelatedtothetask:commonlargermodels.Asimilarpatternofdiminishingperformance sense,reasoning,reading,andcomprehensionforReCoRD
pastacertainprefixlengthisobservedbyLiandLiang(2021). andcommonsense,pronoun,andresolutionforWSC.

<!-- Page 6 -->

the class based initialization performs best. At
smallermodelsizes,therearelargegapsbetween
thedifferentinitializations,butoncethemodelis
scaledtoXXLsize,thosedifferencesdisappear.
109

### With“classlabel”initialization,weobservethat

the class labels typically persist in the learned
107
prompts, such that the nearest token embeddings
(incosinedistance)matchthetokensusedforini-
105
tialization. Beyondthis,wedidnotfindourlearned
promptstobeinterpretable,similartothoseofShin
103
etal.(2020). SeeSection7fordetails.
Pre-trainingObjective InFigures3(c)and3(d), 108 109 1010

### Model Parameters

weseepre-trainingobjectivehasacleareffecton
prompt tuning quality. As hypothesized in Section2.2,T5’sdefault“spancorruption”objective
isnotwell-suitedfortrainingfrozenmodelstobe
laterconditionedbyprompts. Intuitively,models
pre-trained to read and write sentinel tokens are
hardtoapplydirectlytotasksofreadingandwritingtextwithoutsentinels. AsseeninFigure3(c),
eventhe“workaround”ofaddingasentineltothe
downstream targets has little benefit. While LM
adaptation adds value across all model sizes, we
noteourlargestXXLmodelisthemostforgiving
andgivesstrongresultsevenwithspancorruption.

### Given the benefit of LM adaptation, we also

explorehowlongofanadaptationishelpful. Figure3(d)showsthatlongeradaptationprovidesadditional gains, up to 100K steps. This suggests
thatthe“transition”fromspancorruptiontoalanguage modeling objective is not a trivial change,
andmakinganeffectiveswitchtakesaninvestment
oftrainingresources(10%ofthestepsoftheoriginalT5pre-training). Atthesametime,asinour
other ablations, we observe that the XXL model
isrobusttoevennon-idealconfigurations. Atthis
size,thegainsfromadaptationarequitemodest.

### Inthenon-optimal“spancorruption”setting,we

observe instability across model sizes, with the

### SmallmodeloutperformingthelargerBase,Large,

and XL models. On inspection, we find that for
manytasks,thesemid-sizedmodelsneverlearnto
outputalegalclasslabelandthusscore0%. The
two most common error modes are copying subspansfromtheinputandpredictinganemptystring.
Furthermore, thispoorperformanceisnotdueto
randomvarianceinprompttuning,asweobserve
low variance across 3 runs for each size. These
resultsindicatethatusingmodelspre-trainedwith
the“spancorruption”objectivecanbeunreliable,
withonly2outof5modelsworkingwell,whereas
sretemaraP
ksaT

### Model Tuning WARP

Prefix Tuning (Train) Prompt Tuning
Prefix Tuning (Infer) Prompt Design
100%
10%
1%
0.1%
0.01%
0.001%

### Task

Parameters
(%)
Figure 4: Parameter usage of various adaptation techniques,fixingarchitecturetoT5.1.1andprompt/prefix
lengthto1–100tokens(bandsshowmeanandstddev).
Model Tuning: All parameters are task-specific. PrefixTuning: Activationsaretunedintheprefixofeach
layer,requiring0.1–1%task-specificparametersforinference, but more are used for training. WARP: Task
parameters are reduced to under 0.1% by only tuning
inputandoutputlayers. PromptTuning:Onlyprompt
embeddingsaretuned,reachingunder0.01%formost
model sizes. Prompt Design: Only a sequence of
promptIDs(500–2000tokens)isrequired.
theLMadapatedversionsworkreliablyacrossall
modelsizes.
We have released T5 1.1 checkpoints adapted
usingtheLMobjectivefor100Kstepsforallmodel
sizes.8
4 ComparisontoSimilarApproaches
In this section, we review recent work on learning continuous prompts, and draw comparisons
withourmethod. Oneimportantaxisofcomparisonisthenumberoftask-specificparameterseach
method requires, as shown in Figure 4. Among
methodswithlearnableparameters,prompttuning
isthemostparameterefficient,requiringlessthan
0.01%task-specificparametersformodelsovera
billionparameters.9
Li and Liang (2021) propose “prefix tuning”:
learningasequenceofprefixesthatareprepended
8https://github.com/google-research/
text-to-text-transfer-transformer/
blob/main/released_checkpoints.md#
lm-adapted-t511lm100k
9To compare with prompt design, we count each token
ID in the prompt as a parameter, and assume a prompt of
between500–2000tokenstomatchtheGPT-3setting.While
thistechniqueisbyfarthemostparameterefficient,itcomes
atthecostoftaskquality.

<!-- Page 7 -->

ateverytransformerlayer. Thisisakintolearning Dataset Domain Model Prompt ∆
transformeractivationsthatarefixedacrossexam- SQuAD Wiki 94.9±0.2 94.8±0.1 −0.1
ples at every network layer. In contrast, prompt TextbookQA Book 54.3±3.7 66.8±2.9 +12.5

### BioASQ Bio 77.9±0.4 79.1±0.3 +1.2

tuning uses a single prompt representation that RACE Exam 59.8±0.6 60.7±0.5 +0.9
is prepended to the embedded input. Beyond re- RE Wiki 88.4±0.1 88.8±0.2 +0.4

### DuoRC Movie 68.9±0.7 67.7±1.1 −1.2

quiringfewerparameters,ourapproachallowsthe DROP Wiki 68.9±1.7 67.1±1.9 −1.8
transformer to update the intermediate-layer task
Table 1: F1 mean and stddev for models trained on
representations,ascontextualizedbyaninputex-
SQuADandevaluatedonout-of-domaindatasetsfrom
ample. TheirworkbuildsonGPT-2(Radfordetal.,
the MRQA 2019 shared task. Prompt tuning tends to
2019)andBART(Lewisetal.,2020),whileoursfogive stronger zero-shot performance than model tuncusesonT5andexamineschangesinperformance ing,especiallyondatasetswithlargedomainshiftslike
androbustnesstodesignchoicesasmodelsizein- TextbookQA.
creases. WhenusingBART,prefixtuningincludes
prefixesonboththeencoderanddecodernetwork,

### Logeswaran et al. (2020) use a learnable

whileprompttuningonlyrequirespromptsonthe
prependedtokentoadapttransformermodelstovarencoder. LiandLiang(2021)alsorelyonarepaioustasks,butfocusonsmallsyntheticdatasetsderameterization of the prefix to stabilize learning,
signedtoaccommodateacompositionaltaskreprewhich adds a large number of parameters during
sentation,asopposedtolargerreal-worlddatasets.
training, whereas our configuration does not re-

### Theirbasemodelsaresmalltransformerstrained

quirethisreparameterizationandisrobustacross
fromscratchjointlywiththetaskrepresentations,
SuperGLUEtasksandmodelsizes.
whereaswekeepthebasemodelfrozenandinves-

### Hambardzumyanetal.(2021)propose“WARP”,

tigatescalinglawsusinglargertransformers.
where prompt parameters are added to the input

### Moregenerally,workontaskpromptsisclosely

layer. This method works with masked language
aligned with work on “adapters” (Rebuffi et al.,
models, relying on a [MASK] token and a learn-
2017;Houlsbyetal.,2019),smallbottlenecklayableoutputlayertoprojectthemasktoclasslogits.
ers inserted between frozen pre-trained network

### Thisformulationrestrictsthemodeltoproducinga

layers. Adapters offer another means of reducsingleoutput,limitingittoclassification. Prompt
ing task-specific parameters, with Houlsby et al.
tuningdoesnotrequireanychangestotheinputor
(2019)achievingGLUEperformanceclosetofull
atask-specifichead. Theperformanceofprompt
modeltuningwhenfreezingBERT-Largeandonly
tuningisalsoconsiderablyclosertothestrongperadding2–4%additionalparameters. Pfeifferetal.
formanceofmodeltuning.
(2020)usemultipleadaptersinamultilingualcon-
Liuetal.(2021)propose“P-tuning”wherelearntexttoexplicitlyseparatelanguageunderstanding
ablecontinuouspromptsareinterleavedthroughout
fromtaskspecification,similartoourapproach. A
theembeddedinput,usingpatternsbasedonhuman
coredifferencebetweenadaptersandprompttundesign. Our approach removes this complication
ingishowtheapproacheschangemodelbehavior.
bysimplyprependingtheprompttotheinput. To
Adaptersmodifytheactualfunctionthatactsonthe
achievestrongSuperGLUEresults,P-tuninghasto
inputrepresentation,parameterizedbytheneural
beusedinconjunctionwithmodeltuning,thatis,
network,byallowingtherewritingofactivationsat
modelsjointlyupdateboththepromptandthemain
anygivenlayer. Prompttuningmodifiesbehavior
modelparameters,whereasourapproachkeepsthe
by leaving the function fixed and adding new inoriginallanguagemodelfrozen.10
putrepresentationsthatcanaffecthowsubsequent
QinandEisner(2021)use“softwords”tolearn
inputisprocessed.
prompts to extract knowledge from pre-trained
LMs. Prompts are positioned in relation to the 5 ResiliencetoDomainShift
inputbasedonhand-designedpromptprototypes,
and a learned ∆(cid:96) parameter is included for each Byfreezingthecorelanguagemodelparameters,
i
prompt tuning prevents the model from modifylayer,soparametercostscaleswithmodeldepth.
ingitsgeneralunderstandingoflanguage. Instead,
10Asanotherdifference,P-tuningrequirestheadditionof promptrepresentationsindirectlymodulatetherep-
“anchor”tokensintheinput(e.g.aquestionmarkfollowing
resentationoftheinput. Thisreducesthemodel’s
thehypothesisintheRTEtask)toachievestrongperformance,
whileprompttuningleavesinputsuntouched. ability to overfit to a dataset by memorizing spe-

<!-- Page 8 -->

Train Eval Tuning Accuracy F1 Dataset Metric Average Best Ensemble

### QQP MRPC Model 73.1±0.9 81.2±2.1 BoolQ acc. 91.1 91.3 91.7

Prompt 76.3±0.1 84.3±0.3 CB acc./F1 99.3/99.0 100.00/100.00 100.0/100.0

### COPA acc. 98.8 100.0 100.0

MRPC QQP Model 74.9±1.3 70.9±1.2 MultiRC EM/F1a 65.7/88.7 66.3/89.0 67.1/89.4
Prompt 75.4±0.8 69.7±0.3 ReCoRD EM/F1 92.7/93.4 92.9/93.5 93.2/93.9

### RTE acc. 92.6 93.5 93.5

Table2: Meanandstddevofzero-shotdomaintransfer WiC acc. 76.2 76.6 77.4

### WSC acc. 95.8 96.2 96.2

betweentwoparaphrasedetectiontasks.

### SuperGLUE(dev) 90.5 91.0 91.3


### Table 3: Performance of a five-prompt ensemble built

cificlexicalcuesandspuriouscorrelations. Thisrefrom a single frozen T5-XXL model exceeds both the
strictionsuggeststhatprompttuningmayimprove
averageandthebestamongthefiveprompts.
robustnesstodomainshifts,wherethedistribution
ofinputsdiffersbetweentrainingandevaluation.
Weinvestigatezero-shotdomaintransferontwo model (+3.2 accuracy and +3.1 F1). The results
tasks: questionanswering(QA)andparaphrasede- aremuchcloserintheotherdirection,withprompt
tection. Forquestionanswering,weusetheMRQA tuningshowingasmallimprovementinaccuracy
2019 shared task on generalization (Fisch et al., andasmalldropinF1. Theseresultssupportthe
2019). This task collects extractive QA datasets viewthatmodeltuningmaybeover-parameterized
in a unified format and tests how models trained andmorepronetooverfitthetrainingtask,tothe
on“in-domain”datasetsperformwhenevaluated detrimentofsimilartasksindifferentdomains.
on“out-of-domain”datasets. Forourexperiments,
6 PromptEnsembling
we train on SQuAD (Rajpurkar et al., 2016) and
evaluateoneachoftheout-of-domaindatasets.11

### Ensemblesofneuralmodelstrainedfromdifferent


### Table 1 shows that prompt tuning outperforms

initializationsonthesamedataarewidelyobserved
model tuning on the majority of out-of-domain
toimprovetaskperformance(HansenandSalamon,
datasets,witharemarkable12.5pointF1gapbe-
1990) and are useful for estimating model uncertweenthetwoapproachesonTextbookQA.Weobtainty(Lakshminarayananetal.,2017). However,
servelargergainsfromprompttuningincasesof
as model size increases, ensembling can become
largerdomainshifts(e.g.toBiomedicalinBioASQ
impractical. BeyondthespacerequiredtostoreN
ortoTextbooksinTextbookQA).Ofthedatasets
models (e.g. 42 GiB for each copy of T5-XXL),
where model tuning is better, we see that DROP
thereisasubstantialinferencecosttorunningN
sharesadomain(Wikipedia)withSQuADandis
distinctmodels,whetherinparallelorinseries.
thusoneofthesmallestdomaintransfers.

### Prompttuningprovidesamoreefficientwayto


### As a second test of robustness to domain shift,

ensemblemultipleadaptationsofapre-trainedlanweexploretransferbetweentwoparaphrasedetecguagemodel. BytrainingN promptsonthesame
tiontasksfromGLUE(Wangetal.,2019b). The
task, we create N separate “models” for a task,
first task is QQP (Iyer et al., 2017), which asks
whilestillsharingthecorelanguagemodelingpaif two questions from the community Q&A site
rametersthroughout. Beyonddrasticallyreducing

### Quoraare“duplicates”. ThesecondtaskisMRPC

storage costs, the prompt ensemble makes infer-
(DolanandBrockett,2005),whichasksiftwosenencemoreefficient. Toprocessoneexample,rather
tences drawn from news articles are paraphrases.
thancomputingforwardpassesofN differentmod-
Wetesttransferinbothdirections(QQP⇔MRPC).
els, we can execute a single forward pass with a

### Asbefore,wetrainonthe“in-domain”task,select

batch size of N, replicating the example across
checkpointsusingin-domainvalidation,andevaluthe batch and varying the prompt. These savings
atezero-shotonthe“out-of-domain”task.
mirrorthoseseenformulti-taskinginFigure2.

### Table2showsthattrainingalightweightprompt

To demonstrate the viability of prompt ensemon the QQP data and evaluating on MRPC gives
bling,wetrainfivepromptsforeachSuperGLUE
much better performance than tuning the entire
task, using a single frozen T5-XXL model with
11WeselectcheckpointsbasedonSQuADvalidationF1. ourdefaulthyperparameters. Weusesimplemajor-
Theout-of-domaindatasetsareTextbookQA(Kembhavietal., ityvotingtocomputepredictionsfromtheensem-
2017),RACE(Laietal.,2017),BioASQ(http://bioasq.
ble. Table3showsthatacrossalltasks,theensemorg/),RE(Levyetal.,2017),DuoRC(Sahaetal.,2018),
andDROP(Duaetal.,2019). blebeatsthesingle-promptaverageandbeats, or

<!-- Page 9 -->

matches,thebestindividualprompt. show little interpretability, we do observe a high
frequency of words like science, technology and
7 Interpretability engineeringasthenearestneighborsforprompts
trained on the BoolQ dataset and approximately
An ideally interpretable prompt would consist of
20% of the questions are in the “Nature/Science”
naturallanguagethatclearlydescribesthetaskat
category. Whilemoreinvestigationisneeded,this
hand,explicitlyasksthemodelforsomeresultor
suggests that one role of the prompt may be to
action, and makes it easy to understand why the
prime the model to interpret inputs in a specific
promptelicitedsuchbehaviorfromthemodel.
domainorcontext(e.g.“scientific”).
Asprompttuningworksinthecontinuousembeddingspaceratherthanthediscretetokenspace, 8 Conclusion
interpreting prompts becomes more difficult. To

### In this paper, we showed that prompt tuning is

testtheinterpretabilityofourlearnedsoftprompts,
a competitive technique for adapting frozen prewecomputethenearestneighborstoeachprompt
trainedlanguagemodelstodownstreamtasks. On
tokenfromthefrozenmodel’svocabulary. Weuse
thepopularSuperGLUEbenchmark,itstaskperforcosinedistancebetweenthevocabularyembedding
mancerivalsthatoftraditionalmodeltuning,with
vectorandtheprompttokenrepresentationasthe
thegapvanishingasmodelsizeincreases. Onzerosimilaritymetric.
shotdomaintransfer,wefoundthatprompttuning
Weobservethat for agiven learnedprompt toleadstoimprovedgeneralization. Thisplausiblyinken,thetop-5nearestneighborsformtightsemandicatesthatfreezinggeneral-purposelanguageunticclusters. Forexample,weseelexicallysimilar
derstandingparametersandrestrictingdownstream
clusterssuchas{Technology/technology/Techlearning to a lightweight parameter footprint can
nologies / technological / technologies }, as well
helptoavoidoverfittingtoaspecificdomain.
as more diverse but still strongly related clusters
Beyond task quality metrics, we discussed the
suchas{entirely/completely/totally/altogether
appealofmovingtofrozenpre-trainedmodelsin
/100%}. Thenatureoftheseclusterssuggeststhat
terms of storage and serving costs. This move
thepromptsareinfactlearning“word-like”repreenables both efficient multi-task serving, as well
sentations. We found that random vectors drawn
as efficient high-performing prompt ensembling.
fromtheembeddingspacedonotshowthissortof
Looking forward, we believe that factoring out
semanticclustering.
task-definingparametersasdistinctfromgeneral
Wheninitializingthepromptsusingthe“classlanguage-modelingparametersisanexcitingstep
label”strategy,weoftenfindthattheclasslabels
thatopensupmanyavenuesfornewresearch.
persistthroughtraining. Specifically,ifaprompt
token is initialized to a given label, that label is

### Acknowledgements

oftenamongthelearnedtoken’snearestneighbors
aftertuning. Wheninitializingwiththe“Random We thank Lucas Dixon, Waleed Ammar, Slav
Uniform”or“SampledVocab”methods,theclass Petrov and Sebastian Ruder for comments on an
labels can also be found in the nearest neighbors earlierdraft,andthefollowingpeopleforhelpful
of the prompts; however they tend to appear as discussion: ColinRaffel,AdamRoberts,andNoam
neighborstomultipleprompttokens. Thissuggests Shazeer. WethankLintingXueforhelpwiththe
that the model is learning to store the expected LMadaptationtraining.
output classes in the prompts as reference, and
initializing the prompt to outputs classes makes

### References

thiseasierandmorecentralized.
Whenexamininglongerprompts(e.g.size100), Roy Bar-Haim, Ido Dagan, Bill Dolan, Lisa Ferro,
Danilo Giampiccolo, Bernardo Magnini, and Idan
weoftenfindseveralprompttokenswiththesame

### Szpektor. 2006. The second PASCAL recognising

nearest neighbors. This suggests there is either
textualentailmentchallenge. InProceedingsofthe
excess capacity in the prompt, or that the lack of second PASCAL challenges workshop on recognissequential structure in the prompt representation ingtextualentailment,volume6,pages6–4.Venice.
makesitdifficultforthemodeltolocalizeinforma-
Luisa Bentivogli, Peter Clark, Ido Dagan, and Danilo
tiontoaspecificposition.

### Giampiccolo.2009. ThefifthPASCALrecognizing

While the learned prompts taken as sequences textualentailmentchallenge. InTAC.

<!-- Page 10 -->

James Bradbury, Roy Frostig, Peter Hawkins, (Long and Short Papers), pages 2368–2378, Min-
Matthew James Johnson, Chris Leary, Dougal neapolis,Minnesota.AssociationforComputational
Maclaurin, George Necula, Adam Paszke, Jake Linguistics.

### VanderPlas, Skye Wanderman-Milne, and Qiao

Zhang. 2018. JAX: composable transformations of AdamFisch,AlonTalmor,RobinJia,MinjoonSeo,Eu-
Python+NumPyprograms. nsol Choi, and Danqi Chen. 2019. MRQA 2019
shared task: Evaluating generalization in reading
Tom Brown, Benjamin Mann, Nick Ryder, Melanie comprehension. In Proceedings of 2nd Machine
Subbiah, Jared D Kaplan, Prafulla Dhariwal, ReadingforReadingComprehension(MRQA)Work-
Arvind Neelakantan, Pranav Shyam, Girish Sastry, shopatEMNLP.

### Amanda Askell, Sandhini Agarwal, Ariel Herbert-

Voss, Gretchen Krueger, Tom Henighan, Rewon Danilo Giampiccolo, Bernardo Magnini, Ido Dagan,
Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, and Bill Dolan. 2007. The third PASCAL recog-
Clemens Winter, Chris Hesse, Mark Chen, Eric nizingtextualentailmentchallenge. InProceedings
oftheACL-PASCALworkshopontextualentailment

### Sigler,MateuszLitwin,ScottGray,BenjaminChess,

Jack Clark, Christopher Berner, Sam McCandlish,
andparaphrasing,pages1–9.AssociationforCom-
Alec Radford, Ilya Sutskever, and Dario Amodei. putationalLinguistics.

## Language models are few-shot learners. In


### Karen Hambardzumyan, Hrant Khachatrian, and


### AdvancesinNeuralInformationProcessingSystems,

JonathanMay.2021. WARP:Word-levelAdversarvolume 33, pages 1877–1901. Curran Associates,
ialReProgramming. InProceedingsofthe59thAn-
Inc.
nual Meeting of the Association for Computational
Linguisticsandthe11thInternationalJointConfer-
Christopher Clark, Kenton Lee, Ming-Wei Chang,
ence on Natural Language Processing (Volume 1:

### Tom Kwiatkowski, Michael Collins, and Kristina


### Long Papers), pages 4921–4933, Online. Associa-

Toutanova. 2019. BoolQ: Exploring the surprising
tionforComputationalLinguistics.
difficulty of natural yes/no questions. In Proceedingsofthe2019ConferenceoftheNorthAmerican

### L. K. Hansen and P. Salamon. 1990. Neural network

Chapter of the Association for Computational Linensembles. IEEE Transactions on Pattern Analysis
guistics: Human Language Technologies, Volume 1
andMachineIntelligence,12(10):993–1001.
(Long and Short Papers), pages 2924–2936, Minneapolis,Minnesota.AssociationforComputational Jonathan Heek, Anselm Levskaya, Avital Oliver, Mar-
Linguistics. vin Ritter, Bertrand Rondepierre, Andreas Steiner,
and Marc van Zee. 2020. Flax: A neural network
Ido Dagan, Oren Glickman, and Bernardo Magnini.
libraryandecosystemforJAX.

## ThePASCALrecognisingtextualentailment

challenge. In Machine Learning Challenges Work- Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski,
shop,pages177–190.Springer. Bruna Morrone, Quentin De Laroussilhe, Andrea
Gesmundo, Mona Attariyan, and Sylvain Gelly.
Marie-Catherine De Marneff, Mandy Simons, and Ju-

## Parameter-efficienttransferlearningforNLP.

dith Tonhauser. 2019. The CommitmentBank: In-

### InProceedingsofthe36thInternationalConference

vestigating projection in naturally occurring dison Machine Learning, volume 97 of Proceedings
course. ProceedingsofSinnundBedeutung23.
of Machine Learning Research, pages 2790–2799.

## Pmlr.


### Jacob Devlin, Ming-Wei Chang, Kenton Lee, and

Kristina Toutanova. 2019. BERT: Pre-training of

### JeremyHowardandSebastianRuder.2018. Universal

deep bidirectional transformers for language underlanguagemodelfine-tuningfortextclassification. In
standing. In Proceedings of the 2019 Conference
Proceedings of the 56th Annual Meeting of the Asof the North American Chapter of the Association
sociation for Computational Linguistics (Volume 1:
for Computational Linguistics: Human Language
LongPapers),pages328–339,Melbourne,Australia.
Technologies, Volume 1 (Long and Short Papers),
AssociationforComputationalLinguistics.
pages4171–4186,Minneapolis,Minnesota.AssociationforComputationalLinguistics. Shankar Iyer, Nikhil Dandekar, and Kornel Csernai.

## FirstQuoradatasetrelease: Questionpairs.

WilliamBDolanandChrisBrockett.2005. Automaticallyconstructingacorpusofsententialparaphrases. ZhengbaoJiang, FrankF.Xu, JunAraki, andGraham
InProceedingsoftheThirdInternationalWorkshop Neubig. 2020. How can we know what language
onParaphrasing(IWP2005). models know? Transactions of the Association for
ComputationalLinguistics,8:423–438.

### Dheeru Dua, Yizhong Wang, Pradeep Dasigi, Gabriel

Stanovsky, Sameer Singh, and Matt Gardner. 2019. A.Kembhavi,M.Seo,D.Schwenk,J.Choi,A.Farhadi,
DROP:Areadingcomprehensionbenchmarkrequir- and H. Hajishirzi. 2017. Are you smarter than a
ingdiscretereasoningoverparagraphs. InProceed- sixthgrader? textbookquestionansweringformultiingsofthe2019ConferenceoftheNorthAmerican modalmachinecomprehension. In2017IEEECon-
Chapter of the Association for Computational Lin- ferenceonComputerVisionandPatternRecognition
guistics: Human Language Technologies, Volume 1 (CVPR),pages5376–5384.

<!-- Page 11 -->

Daniel Khashabi, Snigdha Chaturvedi, Michael Roth, 4582–4597, Online. Association for Computational
ShyamUpadhyay,andDanRoth.2018. Lookingbe- Linguistics.
yond the surface: A challenge set for reading comprehensionovermultiplesentences. InProceedings Xiao Liu, Yanan Zheng, Zhengxiao Du, Ming Ding,
of North American Chapter of the Association for Yujie Qian, Zhilin Yang, and Jie Tang. 2021. GPT
ComputationalLinguistics(NAACL). understands,too. CoRR,abs/2103.10385.
Vid Kocijan, Ana-Maria Cretu, Oana-Maria Camburu, Lajanugen Logeswaran, Ann Lee, Myle Ott, Honglak
Yordan Yordanov, and Thomas Lukasiewicz. 2019. Lee, Marc’Aurelio Ranzato, and Arthur Szlam.
AsurprisinglyrobusttrickfortheWinogradschema 2020. Few-shot sequence learning with transformchallenge. InProceedingsofthe57thAnnualMeet- ers. CoRR,abs/2012.09543.
ingoftheAssociationforComputationalLinguistics,
pages 4837–4842, Florence, Italy. Association for Vinod Nair and Geoffrey E. Hinton. 2010. Rectified
ComputationalLinguistics. linearunitsimproverestrictedBoltzmannmachines.

### InProceedingsofthe27thInternationalConference

TakuKudoandJohnRichardson.2018. SentencePiece: on International Conference on Machine Learning,
A simple and language independent subword tok- ICML’10, page 807–814, Madison, WI, USA. Omenizeranddetokenizerforneuraltextprocessing. In nipress.

### Proceedings of the 2018 Conference on Empirical

Methods in Natural Language Processing: System Matthew Peters, Mark Neumann, Mohit Iyyer, Matt
Demonstrations, pages 66–71, Brussels, Belgium. Gardner, Christopher Clark, Kenton Lee, and Luke
AssociationforComputationalLinguistics. Zettlemoyer. 2018. Deep contextualized word representations. In Proceedings of the 2018 Confer-

### Guokun Lai, Qizhe Xie, Hanxiao Liu, Yiming Yang,

ence of the North American Chapter of the AssociandEduardHovy.2017. RACE:Large-scaleReAdation for Computational Linguistics: Human Laning comprehension dataset from examinations. In
guageTechnologies,Volume1(LongPapers),pages
Proceedings of the 2017 Conference on Empirical
2227–2237, New Orleans, Louisiana. Association
Methods in Natural Language Processing, pages
forComputationalLinguistics.
785–794, Copenhagen, Denmark. Association for
ComputationalLinguistics. Jonas Pfeiffer, Ivan Vulic´, Iryna Gurevych, and Sebastian Ruder. 2020. MAD-X: An Adapter-Based

### Balaji Lakshminarayanan, Alexander Pritzel, and

Framework for Multi-Task Cross-Lingual Transfer.
CharlesBlundell.2017. Simpleandscalablepredic-

### InProceedingsofthe2020ConferenceonEmpirical

tiveuncertaintyestimationusingdeepensembles. In

### MethodsinNaturalLanguageProcessing(EMNLP),


### AdvancesinNeuralInformationProcessingSystems,

pages7654–7673,Online.AssociationforComputavolume30.CurranAssociates,Inc.
tionalLinguistics.

### Hector Levesque, Ernest Davis, and Leora Morgen-

Mohammad Taher Pilehvar and Jose Camachostern. 2012. The Winograd schema challenge. In

### Collados. 2018. WiC: 10,000 example pairs for

Thirteenth International Conference on the Princievaluating context-sensitive representations. CoRR,
plesofKnowledgeRepresentationandReasoning.
abs/1808.09121.

### Omer Levy, Minjoon Seo, Eunsol Choi, and Luke

Zettlemoyer.2017. Zero-shotrelationextractionvia Guanghui Qin and Jason Eisner. 2021. Learning how
readingcomprehension. InProceedingsofthe21st toask:QueryingLMswithmixturesofsoftprompts.
Conference on Computational Natural Language InProceedingsofthe2021ConferenceoftheNorth
Learning (CoNLL 2017), pages 333–342, Vancou- American Chapter of the Association for Computaver,Canada.AssociationforComputationalLinguis- tional Linguistics: Human Language Technologies,
tics. pages 5203–5212, Online. Association for ComputationalLinguistics.
Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer AlecRadford,KarthikNarasimhan,TimSalimans,and
Levy, Veselin Stoyanov, and Luke Zettlemoyer. Ilya Sutskever. 2018. Improving language under-

## BART:Denoisingsequence-to-sequencepre- standingbygenerativepre-training.

trainingfornaturallanguagegeneration,translation,
andcomprehension. InProceedingsofthe58thAn- Alec Radford, Jeff Wu, Rewon Child, David Luan,
nual Meeting of the Association for Computational DarioAmodei,andIlyaSutskever.2019. Language
Linguistics, pages 7871–7880, Online. Association modelsareunsupervisedmultitasklearners. OpenAI
forComputationalLinguistics. Blog.
Xiang Lisa Li and Percy Liang. 2021. Prefix-tuning: Colin Raffel, Noam Shazeer, Adam Roberts, Kather-
Optimizing continuous prompts for generation. In ine Lee, Sharan Narang, Michael Matena, Yanqi
Proceedings of the 59th Annual Meeting of the Zhou, Wei Li, and Peter J. Liu. 2020. Exploring
Association for Computational Linguistics and the thelimitsoftransferlearningwithaunifiedtext-to-
11thInternationalJointConferenceonNaturalLan- text transformer. Journal of Machine Learning Reguage Processing (Volume 1: Long Papers), pages search,21(140):1–67.

<!-- Page 12 -->

PranavRajpurkar,JianZhang,KonstantinLopyrev,and Alex Wang, Amanpreet Singh, Julian Michael, Felix
PercyLiang.2016. SQuAD:100,000+questionsfor Hill, Omer Levy, and Samuel R. Bowman. 2019b.
machine comprehension of text. In Proceedings of GLUE: A multi-task benchmark and analysis platthe2016ConferenceonEmpiricalMethodsinNatu- formfornaturallanguageunderstanding. IntheProralLanguageProcessing,pages2383–2392,Austin, ceedingsofICLR.
Texas.AssociationforComputationalLinguistics.

### Michael L. Waskom. 2021. seaborn: statistical data

Sylvestre-Alvise Rebuffi, Hakan Bilen, and Andrea visualization. Journal of Open Source Software,
Vedaldi. 2017. Learning multiple visual domains 6(60):3021.
withresidualadapters. InAdvancesinNeuralInformation Processing Systems, volume 30. Curran As- Sheng Zhang, Xiaodong Liu, Jingjing Liu, Jianfeng
sociates,Inc. Gao, Kevin Duh, and Benjamin Van Durme. 2018.

### ReCoRD:Bridgingthegapbetweenhumanandma-

Melissa Roemmele, Cosmin Adrian Bejan, and Anchinecommonsensereadingcomprehension. CoRR,
drew S Gordon. 2011. Choice of plausible alternaabs/1810.12885.
tives: Anevaluationofcommonsensecausalreasoning. In2011AAAISpringSymposiumSeries.
AmritaSaha,RahulAralikatte,MiteshM.Khapra,and

### KarthikSankaranarayanan.2018. DuoRC:Towards

complex language understanding with paraphrased
readingcomprehension. InProceedingsofthe56th
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages
1683–1693, Melbourne, Australia. Association for
ComputationalLinguistics.

### Timo Schick and Hinrich Schütze. 2021. Exploiting

cloze-questions for few-shot text classification and
natural language inference. In Proceedings of the
16thConferenceoftheEuropeanChapteroftheAssociation for Computational Linguistics: Main Volume, pages 255–269, Online. Association for ComputationalLinguistics.
Noam Shazeer. 2020. GLU variants improve transformer. CoRR,abs/2002.05202.
Noam Shazeer and Mitchell Stern. 2018. Adafactor:
Adaptivelearningrateswithsublinearmemorycost.
InProceedingsofthe35thInternationalConference
on Machine Learning, volume 80 of Proceedings
of Machine Learning Research, pages 4596–4604.

## Pmlr.

Taylor Shin, Yasaman Razeghi, Robert L. Logan IV,

### EricWallace,andSameerSingh.2020. AutoPrompt:


### Eliciting Knowledge from Language Models with

Automatically Generated Prompts. In Proceedings of the 2020 Conference on Empirical Methods
in Natural Language Processing (EMNLP), pages
4222–4235, Online. Association for Computational
Linguistics.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob

### Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz


### Kaiser, and Illia Polosukhin. 2017. Attention is all

you need. In Advances in Neural Information ProcessingSystems,volume30,pages5998–6008.

### Alex Wang, Yada Pruksachatkun, Nikita Nangia,

AmanpreetSingh, JulianMichael, FelixHill, Omer

### Levy,andSamuelBowman.2019a. SuperGLUE:A

stickierbenchmarkforgeneral-purposelanguageunderstanding systems. In Advances in Neural Information Processing Systems, volume 32. Curran Associates,Inc.

<!-- Page 13 -->

A Reproducibility ishiddenbehindthelineitself,suchas“ModelTuning(Multi-task)”inFigure1andtheBase,Large,

### A.1 ExperimentalSettings

andXLpromptstrainedonthe“SpanCorruption”
WeevaluateeachGLUEandSuperGLUEdataset pretrainingobjectiveinFigure3(b). Figure4also
using the metric specified in the benchmark. We shows mean and standard deviation for the numreusetheevaluationcodefromthepubliclyavail- berofparameterseachmethodusesastheprompt
ableT5open-sourcereleasetocomputemetrics.12 length varies from 1–100. The “Prefix Tuning
FortheSQuADandMRQAdatasets,weevaluate (Train)” curves appears to have no standard deusingF1, oneofthemetricsusedbytheSQuAD viationbecausetheparametercountissostrongly
benchmark,wherepartialanswerspansareconsid- dominated by the cost of the reparameterization
ered. Again,weusetheT5open-sourcereleasefor parameters that the standard deviation bands are
metriccalculation.13 AllofourmodelsuseT51.1 occluded. Forourexperimentsondomaintransfer,
asthebasefrozenmodel,additionaldetailsandpre- wereportmeanandstandarddeviationover3runs.
trainedcheckpointscanbefoundonGitHub.1415

### A.3 Datasets


### AllpromptsforT5SmallandBasemodelswere

trainedon4TPUv2chips,whilepromptsforlarger AlldatasetsusedareinEnglish. FortheGLUE16,17
modelsweretrainedon16TPUv3chips. andSuperGLUE18 datasets,weusedthetraining,
Parametercountsforeachpromptcanbefound validation,andtestsplitsthatshipwithTensorFlow
inTable4. Averageruntimesuntilconvergencecan Datasets. Weusedversion1.0.0forGLUEand
befoundinTable5. 1.0.2 for SuperGLUE datasets. For SQuAD19
weusedv1.1:3.0.0fromTensorflowDatasets
A.2 HyperparameterSearch and follow the provided training, validation, and
testsplits. Fortheout-of-domaindatasetsweused

### This work used 77 hyperparameter search trials

the development splits distributed as part of the
(40forprompttuningand37forsingle-taskmodel

### MRQAsharedtask.20 Datasetsizescanbefound

tuning),and3trainingruns(withvalidationevaluinTable7. Thelabeldistributionsforeachdataset
ation)foreachbaselineconfigurationandablation
can be found in Table 8 (BoolQ), Table 9 (CB),
setting,foratotalof195runsforourmainresult
Table 10 (COPA), Table 11 (MultiRC), Table 14
andablations. Therewereanadditional18runsfor
(RTE),Table12(WiC),Table13(WSC),Table15
thedomainshiftexperimentsand24extrarunsto
(MRPC)andTable16(QQP).
createtheensemble. Hyperparameterboundscan
be found in Table 6. Hyperparameter tuning was Thequestionansweringdatasetsareextractive
doneviamanualtuningandsettingswereselected datasetswithavarietyofanswers,sothereisn’ta
basedontheSuperGLUEscore. Allexperimentsin labeldistributiontoreport. Similarly,theReCoRD
thiswork,outsideofthehyperparameterbeingab- datasetisamultiplechoicedatasetwherethemodel
lated,useourdefaultconfigurationof100Ksteps must predict the masked out entity from a list of
of LM Adapation, a prompt length of 100, and possibleentities. Duetothisformulationthereisn’t
“class-label”initialization. ameaningfullabeldistribution.

### We followed the open-source T5 preprocess-


### All graphs of our experimental results plot the

ing procedure21 for each dataset, except that we
mean and standard deviation over 3 runs as comomitthedatasetprefixdenotingwhichSuperGLUE
putedbySeaborn(Waskom,2021). Somesettings
datasetanexamplebelongsto. FortheSQuADand
havesuchlowvariancethatthestandarddeviation
12https://github.com/google-research/ 16https://www.tensorflow.org/datasets/
text-to-text-transfer-transformer/blob/ catalog/glue#gluemrpc
master/t5/evaluation/metrics.py 17https://www.tensorflow.org/datasets/
13https://github.com/google-research/ catalog/glue#glueqqp
text-to-text-transfer-transformer/blob/ 18https://www.tensorflow.org/datasets/
master/t5/evaluation/metrics.py#L151 catalog/super_glue
14https://github.com/google-research/ 19https://www.tensorflow.org/datasets/
text-to-text-transfer-transformer/blob/ catalog/squad#squadv11_default_config
master/released_checkpoints.md#t511 20https://github.com/mrqa/
15https://github.com/google-research/ MRQA-Shared-Task-2019#out-of-domain
text-to-text-transfer-transformer/ 21https://github.com/google-research/
blob/main/released_checkpoints.md# text-to-text-transfer-transformer/blob/
lm-adapted-t511lm100k master/t5/data/preprocessors.py

<!-- Page 14 -->

T5Size PromptLength TrainableParameters TotalParameters PercentTrainable
Small 1 512 76,961,664 0.00067%
5 2,560 76,963,712 0.00333%
20 10,420 76,971,572 0.01330%
50 25,600 76,986,752 0.03325%
100 51,200 77,012,352 0.06648%
150 76,800 77,037,952 0.09969%
Base 1 768 247,578,624 0.00031%
5 3,840 247,581,696 0.00155%
20 15,360 247,593,216 0.00620%
50 38,400 247,616,256 0.01551%
100 76,800 247,654,656 0.03101%
150 115,200 247,693,056 0.04651%
Large 1 1,024 783,151,104 0.00013%
5 5,120 783,155,200 0.00065%
20 20,480 783,170,560 0.00262%
50 51,200 783,201,280 0.00654%
100 102,400 783,252,480 0.01907%
150 153,600 783,303,680 0.01961%

## Xl 1 2,048 2,849,759,232 0.00007%

5 10,240 2,849,767,424 0.00036%
20 40,960 2,849,798,144 0.00143%
50 102,400 2,849,859,584 0.00359%
100 204,800 2,849,961,984 0.00718%
150 307,200 2,850,064,384 0.01078%

## Xxl 1 4,096 11,135,336,448 0.00004%

5 20,480 11,135,352,832 0.00018%
20 81,920 11,135,414,272 0.00074%
50 204,800 11,137,380,352 0.00184%
100 409,600 11,135,741,952 0.00368%
150 614,400 11,135,946,752 0.00552%
Table 4: Number of parameters used for various prompt lengths and T5 model sizes. Trainable parameters is
the number of parameters in the prompt itself, while total parameters includes the prompt plus the original T5
parameters. TheT5parametersarefrozenandsharedacrossalltasks,andincludetheSentencePiecelookuptable
parameters. Thefinalcolumnisthepercentageoftotalparametersthataretrainable.
MRQA datasets we used the T5 SQuAD preprocessingcode22. ByfollowingtheT5preprocessing

### PromptLength T5Size Time

andtext-to-textformat,werecasttheWSCdataset
1 Large 3:17±02:10
as a text generation task. Instead of predicting

## Xl 3:37±02:11

whether a supplied referent is correct for a high- XXL 21:23±01:54
lightedspan,ourmodelpredictsthecorrectreferent 20 XL 49:08±18:53

## Xxl 53:03±16:25

directly. Assuch,wecanonlylearnfromtraining
50 Small 09:05±05:07
examples where the referent is correct, so WSC Base 55:01±27:48

### Large 1:14:16±13:12

trainingdatawherethesuppliedreferentisincor-

## Xl 2:30:10±25:40

rectareomitted. XXL 3:13:13±23:08
Nonewdatawascollectedforthiswork. 100 Small 16:25±01:15

### Base 29:57±00:18

Large 1:23:36±10:21

## Xl 3:35:00±54:42


## Xxl 3:51:15±45:53

Table 5: Mean and standard deviation of the runtime
until convergence for the BoolQ dataset and various
prompt lengths and model sizes. Convergence is definedasreachingaperformancewithin1%ofthemean
value for that model configuration. A few configurations have been omitted because their runtimes were
22https://github.com/google-research/ artificiallyextendedduetopreemption.
text-to-text-transfer-transformer/blob/
master/t5/data/preprocessors.py#L264

<!-- Page 15 -->


### Hyperparameter SearchSpace

LearningRate 0.001–0.5 Split False True
ParameterScaling {True,False}

### Training 55.9 44.1

BatchSize {32,64,126,256,512}

### Validation 57.2 42.8

NumberofSteps {10,000,20,000,30,000}

### WarmupSteps {off,2,000,3,000}

DecayFactor {off,0.1,0.5} Table11: LabeldistributionfortheMultiRCdataset.

### StepsperDecay {off,4,000,6,000,8,000}

Table6: Searchspaceforeachhyperparameterconsidered. ParameterScalingreferstotheAdafactorsetting

### Split False True

whereanupdateisscaledbythenormoftheparameter
it will be applied to. Warmup Steps is the number of Training 50.0 50.0
stepsbeforealinearlyincreasinglearningratereaches Validation 50.0 50.0
theLearningRatevalue,startingfromzero.DecayFactor is the reduction in Learning Rate size that occurs Table12: LabeldistributionfortheWiCdataset.
every“StepsperDecay”steps.

### Dataset Training Validation Testing

BoolQ 9,427 3,270 3,245 Split False True

## Cb 250 56 250

Training 0.0 100.0

## Copa 400 100 500


### Validation 63.5 36.5


### MultiRC 27,243 4,848 9,693


### ReCoRD 100,730 10,000 10,000

RTE 2,490 277 3,000 Table13: LabeldistributionfortheWSCdataset. Fol-
WiC 5,428 638 1,400 lowingT5,wecasttheWSCdatasettoafree-formtext
WSC 259∗ 104 146 generationtaskwherethemodelgeneratesthereferent

## Mrpc 3,668 408 1,725

to the highlighted span instead predicting if the sup-

## Qqp 363,849 40,430 390,965

SQuAD 87,599 10,570 - plied entity is the correct referent of the highlighted
TextbookQA - 1,504 - span. Thus, we only use training data where the sup-
RACE - 1,503 - plied referent is correct making our training label dis-
BioASQ - 1,501 - tributionfocusedentirelyonTrue.

## Re - 674 -

DuoRC - 2,948 -

## Drop - 1,503 -

Table7:Sizesfortraining,validation,andtestingsplits

### Split entailment not_entailment

of each dataset used. ∗Following T5, our casting of

### Training 51.2 49.8

WSCasatextgenerationproblemsmeanswecanonly

### Validation 52.7 47.3

trainonexampleswherethesuppliedreferentiscorrect.
Thismeansourtrainingdatasetissmallerthanthenor-
Table14: LabeldistributionfortheRTEdataset.
malWSCtrainingdataset,whichhas554examples.

### Split False True


### Training 37.7 62.3

Validation 37.8 62.2 Split equivalent not_equivalent

### Training 67.4 32.6

Table8: LabeldistributionfortheBoolQdataset. Validation 68.4 31.6
Split contradiction entailment neutral Table15: LabeldistributionfortheMRPCdataset.

### Training 47.6 46.0 6.4


### Validation 50.0 41.1 8.9

Table9: LabeldistributionfortheCBdataset.

### Split duplicate not_duplicate

Split choice1 choice2 Training 36.9 63.1
Validation 36.8 63.2

### Training 48.8 51.2


### Validation 55.0 45.0

Table16: LabeldistributionfortheQQPdataset.
Table10: LabeldistributionfortheCOPAdataset.

## Tables

**Table (Page 1):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 2):**

| Task A Batch |  | a1 |
|---|---|---|
|  |  | a2 |
|  |  |  |


**Table (Page 2):**

|  | C |  |
|---|---|---|
|  | Task Prompts (20K params eac | h) |


**Table (Page 2):**

| Task C Batch |  | c1 |
|---|---|---|
|  |  | c2 |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 5):**

| 1 5 |  |  |  |
|---|---|---|---|
| 20 100 150 |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 5):**

| Random Uniform Sampled Vocab |  |  |  |
|---|---|---|---|
| Class Label |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 5):**

| Span Corruption |  |  |  |
|---|---|---|---|
| Span Corruption + Sentinel |  |  |  |
| LM Adaptation (100K) |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 5):**

| 0K |  |  |  |
|---|---|---|---|
| 10K |  |  |  |
| 50K 100K |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 6):**

|  |  |  | 1 1 1 0. 0. 0. |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
