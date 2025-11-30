---
title: "Universal Self Adaptive Prompting"
original_file: "./19_Universal_Self_Adaptive_Prompting.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["shot", "page", "cls", "demos", "zero", "table", "pseudo", "usp", "you", "sfg"]
summary: "<!-- Page 1 -->


### Universal Self-adaptive Prompting

XingchenWan∗1,2,RuoxiSun1,HootanNakhost1,HanjunDai1,
JulianMartinEisenschlos1,SercanÖ.Arık1,TomasPfister1
1Google2UniversityofOxford
{xingchenw,ruoxis,hootan,hadai,eisenjulian,soarik,tpfister}@google.com

### Abstract 80

60 Ahallmarkofmodernlargelanguagemodels
(LLMs) is their impressive general zero-shot 40
and few-shot abilities, often elicited through
20
prompt-basedand/orin-contextlearning. However,whilehighlycovetedandbeingthemost 0

"
related_documents: []
---

# Universal Self Adaptive Prompting

<!-- Page 1 -->


### Universal Self-adaptive Prompting

XingchenWan∗1,2,RuoxiSun1,HootanNakhost1,HanjunDai1,
JulianMartinEisenschlos1,SercanÖ.Arık1,TomasPfister1
1Google2UniversityofOxford
{xingchenw,ruoxis,hootan,hadai,eisenjulian,soarik,tpfister}@google.com

### Abstract 80

60 Ahallmarkofmodernlargelanguagemodels
(LLMs) is their impressive general zero-shot 40
and few-shot abilities, often elicited through
20
prompt-basedand/orin-contextlearning. However,whilehighlycovetedandbeingthemost 0

## Cls Sfg Lfg

general,zero-shotperformancesinLLMsare Task Type
stilltypically weakerdueto thelackofguidanceandthedifficultyofapplyingexistingautomaticpromptdesignmethodsingeneraltasks
when ground-truth labels are unavailable. In
thisstudy,weaddressthisbypresentingUniversalSelf-adaptivePrompting(USP),anautomatic prompt design approach specifically
tailoredforzero-shotlearning(whilecompatible with few-shot). Requiring only a small
amountofunlabeleddata&aninference-only
LLM,USPishighlyversatile: toachieveuniversalprompting,USPcategorizesapossible

### NLP task into one of the three possible task

types, and then uses a corresponding selectortoselectthemostsuitablequeries&zeroshot model-generated responses as pseudodemonstrations, thereby generalizing ICL to
the zero-shot setup in a fully automated way.

### We evaluate zero-shot USP with two PaLM

models,anddemonstrateperformancesthatare
considerablystrongerthanstandardzero-shot
baselinesandarecomparabletoorevensuperiorthanfew-shotbaselinesacrossmorethan
20naturallanguageunderstanding(NLU)and
naturallanguagegeneration(NLG)tasks.
1 Introduction
The recent advancements in large language models(LLMs)areamongthemostastonishingbreakthroughsinthehistoryofartificialintelligence. The
modern,massivetransformer-based(Vaswanietal.,
2017) LLMs not only surpass human and previousmodelsinspecificnaturallanguageprocessing
tasks,buttheyhavealsodemonstratedimpressive
generalcapabilitiesthat,forthefirsttime,aredescribed by some to present an early “spark of ar-
*WorkdoneduringinternshipatGoogle.
ecnamrofreP
PaLM-62B PaLM-540B
80 +8.2%
+4.4% 0-shot
+15.7% USP (Ours)
+11.7% 60
40
+33.0% +27.4%
20
0

## Cls Sfg Lfg


### Task Type

Figure1:WeproposeUSP,aversatilezero-shotprompting method that improves over standard zero-shot
promptingacross15Classification(CLS),5Short-form

### Generation (SFG) and 2 Long-form Generation (LFG)

tasks(see§3.3forfurtherexplanations),respectively,in
PaLM-62BandPaLM-540Bmodels.
tificialgeneralintelligence”(Bubecketal.,2023).
Indeed,oneofthemostprominentandfundamental
emergingabilitiesofmodernLLMsoverprevious
modelsistheirimpressivezero-shotgeneralizability(Weietal.,2022a;Brownetal.,2020)handling
diverseandsophisticatedtasks,evenifthemodels
havenotbeenexplicitlytrainedonthem. Beyond
zero-shotabilities,whenafewdemonstrationsare
available,thefew-shotcapabilitiescantakeadvantage of the information in them with in-context
learning (ICL) (Brown et al., 2020), leading to
furtherimprovements.

### Suchfew-shotcapabilitiesareoftenobservedto

improve as the LLMs scale. Along with careful
prompting (in particular automatic prompt optimization),inmanycasesLLMscanperformsimilarlyto,orevenbetterthanfine-tuning,eventhough
thelatterisbothmorecomputationallyexpensive
(duetogradientback-propagation)andmoredataintensive. As such, in many scenarios, ICL and
prompt-basedlearninghavedrasticallyreducedthe
barrierofuseofeventhemostmassiveLLMs.

### Notwithstandingtheimpressivebreakthroughs,

many open questions remain. While the zeroshotperformancesofLLMsarehighlyvaluedand
widelyusedasakeyyardstickofLLMcapabilities
(Chowdheryetal.,2022;Tayetal.,2022),LLMs
stilloftenshowweakerperformancesand/orlarger
3202
yaM
42
]LC.sc[
1v62941.5032:viXra

<!-- Page 2 -->

Figure 2: Overview of (a) zero-shot setup, (b) few-shot setup with in-context learning, (c) Consistency-based
Self-adaptivePrompting(Wanetal.,2023)and(d)UniversalSelf-adaptivePrompting,orUSP,theproposedmethod
inthiswork. ThequerieswithoutdemoswithwhichLLMsaredirectlyprompted(zero-shot,orStage1inCOSP
andUSP)aremarkedinredarrows,andthequeriesprependedwitheitherthehandcrafteddemos(few-shot)or
model-generatedpseudo-demos(Stage2inCOSPandUSP)aremarkedinbluearrows.
performancefluctuationsinzero-shotcomparedto tile,asunlabeleddataistypicallyreadilyavailable
few-shot because of the lack of guidance or tem- via,e.g.,continuous,on-the-flycollectionsofuser
platesolutions. Whilemanyautomaticprompting queries. Unlike competing methods often requirmethods have been proposed (refer to §4 for de- ingtaskknowledgebeforehand(e.g.,classnames),
tails),fewexistingworkstargetthezero-shotsetup USP requires only the task type information (e.g.
and heuristic manual prompt design is still often natural language understanding (NLU) or generheavilyreliedupon(ReynoldsandMcDonell,2021; ation (NLG) – these need to be known anyway),
Mishraetal.,2022). whileremainingcapableofusingadditionalinformationlikeclassnamesiftheyareindeedavailable

### On the other hand, even though the ICL

(§3.3). ThisenablesUSPtoworkinarbitrary,poparadigm has reduced the cost of data collection
tentially novel tasks at test time and/or tasks that
andlabelingconsiderablycomparedtofinetuning,
given that modern LLMs are typically used for simply cannot be cast as classification problems
an extremely diverse set of tasks, obtaining even (e.g.,open-domainQAandgenerativetasks). USP
is inspired by recent works leveraging confident
a small number of labeled examples per task can
predictionsformodelself-improvementsonchaineasilybecomeexpensiveformanytasks. Furtherof-thoughttasks(Wangetal.,2022;Huangetal.,
more, in some tasks, obtaining even a few examplesbeforehandmightrequireanon-trivialamount 2022; Wan et al., 2023) but inherits the benefits
of human effort (e.g. summarization of long arti- of these works and generalize them considerably
in terms of the scope of applicability: to achieve
cles,translationoflow-resourcelanguages,and/or
so,wederivevariouscriteriacapableofselecting
domain-specific question answering requiring rehigh-qualitypseudo-demosintheabsenceofany
search or expertise), or simply impossible if the
tasksarenovelandareonlyrevealedattesttime. ground-truthlabels. Tosummarize:
To address this, we introduce USP (Universal 1. We propose USP, a versatile and black-box
Self-adaptive Prompting) that specifically gen- automaticpromptingmethodthatcanbefully
eralizes ICL to zero-shot settings (while re- zero-shotusingonlyunlabelleddata.
maining compatible with few-shot) via pseudo-

## To achieve so, we select pseudodemonstrations(pseudo-demos)constructedfrom

demonstrations from model-generated
unlabeled queries and model-generated outputs.
outputs via 3 carefully designed scoring
USP works with fully black-box, inference-only
functionssuitablefordifferenttasktypes.

### LLMs,andtheuseofpseudo-demosensuresthat

USPmayoperateentirelyinthetransductivezero- 3. AsshowninFig. 1,weshowthatUSPrealizes
shotsetup(Xianetal.,2017)whereonlyunlabeled large performance gains over more than 20
queriesareused. ThismakesUSPextremelyversa- NLUandNLGtasksintwoPaLMmodels.

<!-- Page 3 -->

2 Preliminaries usesatwo-stageapproach. InStage1,COSPperformszero-shotinferencewithmultipledecoding
In-contextLearning(ICL). ICLisaprompting
pathsinasimilarmannertoSC,andthenderives
technique that allows LLMs to perform few-shot
normalizedentropy,aquantitativemeasureofthe
learningbyprocessingseverallabeled,exemplary
model confidence and discrepancy in predictions
queries that are similar to the test queries we are
fromthesamequeryondifferentdecodingpaths.
interestedinsolvingasdemonstrations,ordemos

### COSPthenrankstheStage1outputsbasedonthe

(Dongetal.,2022;LoganIVetal.,2022)(Fig. 2b).
entropy (and other metrics such as diversity and
Instead of performing gradient updates like finerepetition),andselectstheconfidentoutputsasthe
tuning, ICL is inference-only yet is shown to be
pseudo-demos. InStage2,thesepseudo-demosare
very competitive in modern LLMs (Brown et al.,
prependedtothetestqueriesagaininamannersim-
2020). Formally,denotingatestqueryasxandif
ilartofew-shotinference,andthefinalpredictions
wehavekpairsofrelatedconcatenatedqueriesand
aregivenbythemajorityvoteoveroutputsinboth
labels s(i) = Concat(x(i),y(i))∀i ∈ {1,...,k}
stages. In multiple commonsense and arithmetic
servingasdemos(a.k.a.,k-shotlearning),weaugreasoning tasks, COSP significantly outperforms
mentthetestquerybyprependingthedemos(and
thezero-shotbaselines.
instructions,ifany)toit:
3 UniversalSelf-adaptivePrompting
C(x)=Concat(s(1),...,s(k),x). (1)
3.1 MotivationandChallengesofUSP

### ICL is achieved by obtaining the prediction yˆby

queryingC(x)insteadofjustx. Inourzero-shot InspiredbythesuccessofCOSP,wearguethatthe
setup,noneoftheground-truthlabels(i.e.,theys) principleofconfidence-basedself-adaptivepromptareavailableandweproposetousetheLLMpre- ing should be universally applicable to all tasks,
dictions themselves as pseudo-demos. Thus, our ratherthanbeingexclusivetoanarrowsetoftasks
zero-shotICLinsteadhastheformof: COSP considered; this forms the motivation and
the goal of this paper. However, a number of

### Cˆ(x)=Concat(sˆ(1),...,sˆ(k),x), (2)

limitations and challenges prohibit a trivial genwhere sˆ = Concat(x(i),yˆ(i)), and the ultimate eralization: first, an universal prompting strategy
i
objectiveofUSPistoidentifythemostsuitableset needs to accommodate numerous, vastly diverse
ofsuchpseudo-demos. tasksthatvarysignificantlyintermsofobjective,
prompting, evaluation and unsurprisingly, confi-

### Consistency. The principle of consistency was

dence/uncertainty quantification. As a result, SC
first applied in semi-supervised learning to reguandthetechniquesdevelopedbyWanetal.(2023)
larizemodelpredictionstoencourageinvariances
maybesub-optimaloreveninapplicableforother
to small input perturbations (Miyato et al., 2018;
tasktypes: forinstance,manyNLPproblemsare
Sajjadi et al., 2016; Clark et al., 2018a). In the
cast as classification where the model logits are
context of LLMs, Wang et al. (2022) introduce
useful for uncertainty quantification, but such inself-consistency (SC) for chain-of-thought (CoT)
formationisnotusedintheoriginalformulationof
reasoning tasks (Wei et al., 2022b) as an effec-

### COSPtoapproximateconfidence. Also,thenotion

tive approximation of the model confidence: SC
of majority voting crucial to COSP and SC may
decodes each test query multiple times, with or
notevenexistforcreativeandgenerativetaskswith
without demos, using a non-zero temperature to
manyplausiblesolutions.
introducestochasticity. Themajorityofthepredictionsarethenchosenasthefinalpredictions. 3.2 OverviewofUSP
COSP. Inspired by the findings of Wang et al. Toaddressthechallenges,wepresentUSP(illus-
(2022)andtheprincipleofentropyminimization trated in Fig. 2d and Algorithm 1). USP shares
(GrandvaletandBengio,2004),Wanetal.(2023) somehigh-levelsimilaritiestotheCOSPformulaproposeConsistency-basedSelf-adaptivePrompt- tion: USPalsoadoptsatwo-stagedapproachwhere
ing (COSP), the prior work that has arguably in- inStage1,theLLMsarepromptedinazero-shot
fluenced our present work the most. The goal of manner to generate a collection of candidate re-
COSP is to further improve the zero-shot reason- sponsesfromwhichafewmodel-generatedpseudoingabilitiesofLLM.AsshowninFig. 2c,COSP demosareselected;inStage2,USPprependsthese

<!-- Page 4 -->

Algorithm1USP.Stage1stepsaremarkedinred iteratethroughD,whichcanbemodestlysized,in
andStage2stepsaremarkedinblue. Stage1.
1: Input:TestsetT ={x(i)}N ,LLM,unlabeleddataset (iii)Droppingrelianceonmajorityvote. Theuse
i=1
fordemogenerationD={d(j)}Nu (canbesameasor of majority vote (as shown in Fig. 2c) is crucial
j=1
asubsetofT,oradifferentbutrelatedsetofunlabeled forCOSP,butasdiscussed, theprocedureisalso
queries),PoolofgeneratedresponsesP ←∅,Tasktype
computationallyexpensiveandinapplicablewhen
t∈{CLS, SFG, LFG}(§3.3).
2: Output:Predictions{yˆ(i)}N . majority itself is ill-defined. To address this, by
i=1
3: for j ∈[1,N u ] do default USP instead only decodes once in Stage
4: [Stage1]QuerytheLLMwithd(j)underthezero-shot
2 with greedy decoding (i.e., temperature = 0)
setuptoobtainasinglepredictionzˆ(j)(if t=CLS),or
querymtimeswithnon-zerotemperaturetoobtainm andusesthemaximumlikelihoodestimated(MLE)
predictions{zˆ(j)}m (otherwise). outputsasthefinalpredictions. Itisworthnoting
k k=1
5: Addeligiblecandidatepseudo-demos{p j }N j= u 1 (from thatUSPremainscompatibletomajorityvoteover
concatenatingd(j)andzˆ(j))toP. multiple decoding (if it can be used) for further
6: endfor
performanceimprovements,butnolongerdepends
7: Buildthepseudo-demosetS ={s ,..,s }(with|S|=

## 1 K

K)fromP withoneoftheselectorsin§3.3depending onthesetofunction.
ont.
8: fori∈[1,N]do
3.3 Task-specificSelector
9: [Stage2]ConcatenatetheStox(i)(Eq.2)andquery
again(withgreedydecodingforgenerative(SFG/LFG) Theobjectiveoftheselector(Step7inAlgorithm
tasks)toobtainthefinalLLMpredictionyˆ(i).
1)is(i)tobuildapoolofcandidatepseudo-demos
10: endfor
P,whoseelementsp(j) arebuiltfromconcatenatpseudo-demostothetestqueriesinafew-shotman- ing dataset queries {d(j)}Nu and their zero-shot
j=1
ner(Eq. (2))andpromptstheLLMagaintoobtain LLMpredictions{zˆ(j)}Nu and(ii)toselectS, a
j=1
thefinalpredictions. However,wehighlightafew subsetofK pseudo-demosfromP tobeprepended
keydesigndecisions,inparticularthosediffering tothetestqueries. WeuseafunctionF : P → R
from COSP, that effectively overcome the afore- (the design of F is explained later in this secmentionedchallengesandenableUSPtogeneral- tion)to“score”eachcandidate. Weselectthefirst
ize: pseudo-demoinSbyfindingthemaximizerofF(·)
(i)Task-specificpseudo-demoselector. Thepseudo- in P. For each of the subsequent pseudo-demos
demo selector, which selects the most suitable k ∈ {2,...,K},weinsteadrepeatedlyfindthemaxquery-responsepairfromthezero-shotoutputsare imizerofF(·)withadiversity-promotingtermto
centraltoUSP.WithreferencetoFig. 2cand2d, penalize candidates that are too similar to any of
whereas COSP only uses the consistency-based thepseudo-demosalreadyselectedandaddtoS:
selectorandhenceisonlyapplicabletoalimited
k−1 (cid:16) (cid:0) (cid:1)(cid:17)
numberoftasks,USPinsteadusesatask-typespe- s k = argmax F(p)−λmax S c ϕ(p),ϕ(s k′) , (3)
cific selector that is key for its versatility – we
p∈P\S1:k−1 k′=1
explainthisindetailin§3.3.
where we follow Wan et al. (2023) to (1) set λ,
(ii) Separating test set and the demo-generating the trade-off parameter, to 0.2 in all experiments
dataset. Unlike COSP which by default uses the without further tuning and (2) use z-score stanfull test set T to generate the pseudo-demos in dardization for the two terms in Eq. (3) over P
Stage1,USPexpectsageneralunlabeleddataset to ensure they are of a comparable magnitude;
D,whichcanbethefulltestsetT,asubsetofit,or S (·,·) denotes the cosine similarity and ϕ(·) is
c
adifferentheld-outunlabelledset;itssolepurpose thesentence-levelembeddinggivenbyanauxiliary
is to generate the pseudo-demos to work even if model, as in COSP. The design of F(·) therefore
the full test set is not known a-priori and/or only encodes our preference on which pseudo-demos
asmallnumberofunlabeledqueriesareavailable. should be prepended to the test queries for ICL,
Indeed,aswewillshowin§5,USPiscapableof andtoachieveuniversalprompting,wecategorize
generating high-quality pseudo-demos with only apossibletaskintooneofthethreegenerictypes,
64unlabeledsamplesperdataset. ThismakesUSP dependingon(i)thenumberofpossibleresponses
more sample efficient, due to the smaller number and (ii) the number of correct responses (shown
of unlabeled samples required, and more compu- in Table 1). We use this categorization to design
tationallyefficient,asthealgorithmonlyneedsto task-specificscoringfunctionsF(·)below,andem-

<!-- Page 5 -->

piricallyvalidatetheeffectivenessofthesedesigns leadtopoorlabelspacecoverageandbiastowards
in§5. these classes; we mitigate this to ensure that the
selected pseudo-demos K feature each class ap-

### Task #possible #correct Logits Score

proximatelyfairly. NotethatitispossiblethatK
type responses responses required? fn.
<|C|ormod(K,|C|) ̸= 0. Inthesecases,wegen-

### CLS Few Single Yes Eq.(4)

erate ⌈K⌉ pseudo-demos per class and prepend

### SFG Many Single/few No Eq.(7) |C|

LFG Many Many No Eq.(8) each test query x(i) ∈ T with K randomly sam-
Table 1: Categorization of the NLP tasks in USP, pled pseudo-demos to ensure fairness in expectanamely Classification (CLS), Short-form Generation tionoverT. Lastly,itispossiblethatsomeclasses
(SFG)andLong-formGeneration(LFG). are never predicted in D, e.g., an over-confident
modelmayneverpredictthe“notsure”optionin
naturallanguageinference(NLI)tasks. Asaresult,
Classification(CLS). WithreferencetoTable1,
thesetP inEq. (5)isemptyfortheseunpredicted
we first consider problems that feature the selec- c
classes. To nevertheless generate the most plaution of a single correct answer from a few possisible pseudo-demos for them, for an unpredicted
bleoptions– weusethedescriptorCLSfor“clasclass c , we pick the top queries in D with the
sification”, as the label space C in this case is u
highestmodel-assignedprobabilityinc :
smallandsometimesknownbeforehand, andthe u
task is to pick the most probable class C: zˆ(j) = Top K (cid:16) P(c=c |d(j)) (cid:17) , (6)
argmax
c∈C

### P(c|d(j)). Since the logits are avail- |C| d(j)∈D u

ableinthiscase,wedonotneedself-consistency noting that the indexing is over the unlabeled
toestimatethepredictionconfidence(althoughwe dataset D. These queries are then concatenated
may still choose to use a self-consistency-based with class label c to form the pseudo-demos for
u
confidence metric and treat the problem as gen- theseunpredictedclasses.
eration if, for example, we believe the model is

### Short-formGeneration(SFG). Wenowfocus

poorlycalibrated,thelogitsareunreliable,orselfon a class of generation problems typically with
consistency could be otherwise more preferable
many possible responses but only one to a few
(e.g.,whenchain-of-thoughtpromptingisusedand
correct, short responses – we use descriptor SFG
generating diverse reasoning paths via multiple-
(forShort-formGeneration),andexamplesinclude
path decoding is beneficial – see the next para-
Question Answering tasks where the possible regraph on SFG for details). Instead, for p(j) =
sponsesspanovertheentirevocabularysetV. Al-

### Concat(d(j),zˆ(j)) ∈ P,wesimplyquerytheLLM

ternatively, as we discussed in the previous paraonceandusethenegativeentropyofthedistribugraph, we may use the SFG formulation for CLS
tionoverC asthefunctionF fortheCLScase:
tasks if we use the text-to-text formulation like
FCLS(p(j)|d(j)):= (cid:88) P˜(c|d(j))logP˜(c|d(j)), (4) T5 (Raffel et al., 2020), have no access or prec∈C fer not to rely on logits, or as discussed, when
whereP˜(c|d(j))isthenormalizedprobability(i.e., self-consistency-stylemultipledecodingisprefer-
(cid:80) P˜(c|d(j)) = 1). WhenmoreknowledgeofC able. Unlike the CLS case we assume access to
c∈C only the model outputs zˆ(j) but not the logit disbeyondthenumberofclassesisknown(e.g.,class
tribution. This covers the case covered in COSP
names), We may also use them to ensure a good
(problemssuchasarithmeticreasoningconsidered
coverageofthelabelspace,whichhasbeenshown
inCOSPfallintothiscategory),andthuswemay
tobeimportantforastrongICLperformance(Min
use the normalized entropy in Wan et al. (2023)
et al., 2022). Specifically, to build S, instead of
to gauge the model confidence, except that for
simply generating K pseudo-demos from P, we
non-CoT prompted tasks, we skip the rationale
generateK/|C|pseudo-demosperclassc ∈ Cfrom
generation step and prompt for answers directly.
asubsetP ⊂ P foreachc:
c
Specifically, for each d(j) ∈ D, we query the
(cid:110) (cid:111)
P = p(j) ∈Pifzˆ(j) =c∀j ∈{1,...,N } . (5) LLM m repetitions, under temperature sampling
c u
toobtainmpredictions{zˆ (j) }m . Whileonlythe
This is because LLMs can be more confident in ℓ ℓ=1
majority predictions of each query are added to
some classes, and simply choosing the most con-

## P :=

(cid:110)
Maj (cid:0) {zˆ (j) }m (cid:1)
(cid:111)Nu
, we use all m prefident predictions overall as pseudo-demos may ℓ ℓ=1
j=1

<!-- Page 6 -->

dictions to score the model confidence for each these outputs often feature an usually high averp(j) ∈ P: age pairwise ROUGE scores (Eq. (8)), we apply
asimplebutempiricallyeffectiveoutlierfiltering
FSFG (cid:0) p(j)(cid:12) (cid:12){zˆ
ℓ
(j)}m
ℓ=1
(cid:1) :=−
(cid:80)µ
α=1
P˜(zˆ
lo
α
(j
g
))
m
logP˜(zˆ
α
(j))
, to remove queries with score > upper quartile +
1.5×interquartilerange(IQR),thecanonicalrule-
(7)
where µ ≤ m is the number of unique answers of-thumbdefiningoutliers(Tukeyetal.,1977).
andP˜(zˆ (j) )istheempiricalfrequencyofanunique
α
4 RelatedWorks
answerzˆ (j) inallmpredictionsford(j).
α

### Besidesthosecoveredin§2,herewediscussother

Long-form Generation (LFG) The final catepriorworksrelatedtoUSPinvariousaspects.
gory features natural language generation tasks
with longer responses and many plausible re-
Bootstrapping LLM knowledge. The promissponses with typical examples being summarizaingabilitiesofLLMshaveledtoeffortstoimprove
tion and translation (hence named LFG for Longthemwiththeirownoutputs: Mengetal.(2020)use
formGeneration). Asdiscussed,Eq. (7)doesnot
classnamesonlyandself-trainingtoimprovetext
effectivelyapproximateconfidence/uncertaintyin
classification;Zelikmanetal.(2022)bootstrapreathiscase,asdecodingthesamequerywithtemperasoningfromLLMs,fromafewlabeleddata;Huang
turesamplingmtimesisunlikelytoyieldidentical
etal.(2022)useself-consistencytogeneratealarge
responsesintermsofsurfacetextsduetothelength
numberofreasoningtracesandfine-tuneonthem;
of generation, even for the confident predictions.

### Zhou et al. (2022) use LLMs themselves to auto-

To measure confidence in this case, we first folmatically program prompts; Wang et al. (2022);
low the SFG case by query each d(j) ∈ D for m

### Honovichetal.(2022)useLLMstogeneratelarge

repetitions {zˆ (j) }m with temperature sampling. instructiondatasetsfordownstreamtasks. Collec-
ℓ ℓ=1
InsteadofusingEq. (7),wecomputetheaverage tively,whileconceptuallyrelatedtoourwork,these
pairwiseROUGEscorebetweenallpairsofthem previousworksdealwithafundamentallydifferent
responses: problem, requiremorecomputationallyintensive
learningprocedure(e.g.,finetuning)orisnotfully
2 (cid:80)m ROUGE(zˆ(j),zˆ(j))
ℓ=1,ℓ′=1 ℓ ℓ′ zero-shot.
FLFG (cid:0) p(j)(cid:12) (cid:12){zˆ
ℓ
(j)}m
ℓ=1
(cid:1) := ℓ′̸=ℓ
m(m−1)
,
(8) Prompt automation & ICL. Numerous methwhereanotheroverlapmetricsuchasthepairwise odshavebeenproposedtoautomatepromptdesign
BLEU(Shenetal.,2019)orthesentence-levelem- – USP also endeavors to achieve so by focusing
beddingcosinesimilarityfromanauxiliarymodel onICL,aspecificcomponentoftheprompt. Soft
may be used instead. Another challenge for LFG promptingmethodsoptimizetheembeddingspace
tasksisthatunlikeSFGwhereP canbesimplybuilt of the LLMs (Li and Liang, 2021; Lester et al.,
frommajoritypredictionsforeachqueryd(j) ∈ D, 2021,interalia)butrequiregradientaccess&prop-
“majority” is not well-defined in this case. We agationthroughmassiveLLMsandaconsiderable
thususeF toranktheconfidenceofthequeries amount of training data. Recently, various hard

## Lfg

in D & determine which queries to be used in S prompting methods, which search for actual disonly. For the response part of the pseudo-demos, cretetokensusingdiscreteoptimization(Shinetal.,
we decode the LLM again for a single time with 2020;Prasadetal.,2022;Wenetal.,2023),reinargmax(orgreedy)decoding(i.e., temperature= forcementlearning(Dengetal.,2022;Zhangetal.,
0) to obtain the MLE predictions on the selected 2023) and gradient estimation (Diao et al., 2022)
queries–thesepredictionsarethenconcatenated have been proposed. While the discrete prompts
withqueriestobuildS. Lastly,giventhatinzero- are more interpretable and (in some cases) comshottextgenerationispurelydrivenbyprompting patible with black-box, inference-only LLMs, to
andinstructions,weobservethattheLLMssome- ourknowledgenoneworksinthezero-shotsetup
times generate extremely confident text comple- and tasks beyond CLS problems (with our definitionsinsteadofactuallycompletingtheinstructed tion in §3.3) are scarcely investigated. Furthertasks (e.g., summarization); selecting these out- more,unlikeUSP,thesemethodsalsooftenrequire
puts as pseudo-demos, as we investigate in §5, hundredsifnotthousandsofLLMqueriesbefore
cansignificantlydegradeperformance. Giventhat converging to good prompts. As for ICL, most

<!-- Page 7 -->


### Model PaLM-62B PaLM-540B

Setting Zero-shot Few-shot Zero-shot Few-shot

### Auto- Random USP Auto- Random USP

Method 0-shot 5-shot 0-shot 5-shot

### CoT demo (Ours) CoT demo (Ours)

winogrande 76.95 80.19 80.19 80.98 77.35 80.51 83.98 85.56 85.48 80.58
piqa 79.87 80.58 80.85 80.74 81.07 81.50 83.19 84.28 83.13 83.84
storycloze 80.28 82.84 82.68 85.03 84.23 82.10 81.40 83.54 85.84 86.26
anlir1 37.20 36.80 40.70 41.90 39.30 48.60 54.10 53.60 58.50 58.30
anlir2 38.10 38.10 39.20 37.00 38.20 43.70 52.00 50.70 54.00 53.00
anlir3 37.17 39.58 42.58 45.75 40.17 46.25 55.58 55.33 59.67 56.67
boolq 84.86 82.84 85.44 85.90 83.82 87.77 89.66 90.15 90.18 89.08
copa 94.00 92.00 93.00 92.00 91.00 93.00 95.00 97.00 94.00 96.00
rte 67.87 79.42 76.53 76.53 76.53 72.56 80.51 81.23 79.78 80.87
wic 49.53 55.33 49.53 49.53 58.13 57.52 56.90 57.37 57.37 62.70
wsc 86.67 87.02 87.02 89.82 83.51 88.42 88.42 87.37 89.47 83.51
arc_e 76.58 81.61 79.62 82.49 80.72 78.77 87.02 85.96 88.16 87.32
arc_c 48.24 51.07 49.61 46.95 51.16 50.64 60.60 56.39 60.17 61.80
raceh∗ 44.77 46.51 44.65 45.60 45.54 45.88 50.20 49.23 50.57 50.00
racem∗ 60.65 64.42 63.44 64.48 63.30 65.95 69.78 69.29 70.61 69.29
Average↑ 64.18 66.55 66.34 66.98 66.31 68.21 72.56 72.47 73.80 73.28
Gainover0-shot(%) 0.00 3.70 3.36 4.36 3.31 0.00 6.37 6.24 8.19 7.43
Averagerank↓ 4.07 2.73 2.60 2.20 2.87 4.53 3.00 2.87 2.00 2.40
Table2: AccuracyonCLStasks(Table1of§3.3)withPaLM-62BandPaLM-540Bmodels(Chowdheryetal.,
2022). MethodsintheZero-shotcolumnsusenoground-truthlabelguidanceandgenerates5pseudo-demosif
applicable,whereasthe5-shotresultsuse5manuallylabeledin-contextdemos. Thetoptworesultsforeachmodel
are bolded and ranked by color: best and second-best. ↑: larger is better. ↓: smaller is better. ∗See notes in
App.B.1.
methodsfocusonretrievingthebestin-contextex- onlygeneratescorrectdemoswithaprobabilityof
amplesfromapoolofgoldenexamplesinsteadof 1 –giventherecentdiscoverythatlargemodels

## |C|

zero-shot(Rubinetal.,2022;Liuetal.,2022);an genuinelylearnfromthedemosandcanbesensiexceptionisAutoCoTwhichwediscussbelow. tivetotheircorrectness(Weietal.,2023),providingmostlywrongdemosissub-optimal. Tonever-
Zero-shot prompting. Several methods have thelessrepresentthisclassofmethods,weprovide
emergedwiththeobjectiveofimprovingzero-shot aRandomdemobaselineinourexperimentsagainst
automaticpromptingandsomeworksalsofocuson whichwecompare(see§5fordetails). Lastly,sevpseudo-demos: AutoCoT(Zhangetal.,2022)simi- eral other prompting approaches like NPPrompt
larlyusesmodel-generatedoutputaspseudo-demos (Zhaoetal.,2022)&NullPrompt(LoganIVetal.,
butdiffersintheselectionprocedure–itcomputes 2022)arealsoproposed,butthesemethodsagain
asentenceembeddingofavailablequeriesanduses onlyworkforCLStasksandareorthogonaltoUSP
clustering to select the centroid queries and their sincetheytargetotheraspectsofpromptingother
modelpredictionsaspseudo-demos. However,un- thanthein-contextexamples.
likeUSP,AutoCoTmakespseudo-demoselection
decisionspurelybasedonthequery(dis)similarity 5 Experiments
rather than the output quality, and the quality of
theselectedpseudo-demosisthus,onexpectation, Setup. We experiment on PaLM-540B and
thesameastheaveragemodelperformance–we PaLM-62B,twovariantsofthePathwaysLanguage
empiricallycompareagainstageneralizedversion Model(PaLM),aleft-to-right,decoder-onlyfamily
ofitin§5,whichisoriginallydesignedforreason- oflanguagemodelspretrained780billiontokens
ingtasksonly(hencethename). Anothermethod, (Chowdheryetal.,2022). Weconsiderawidevari-
Z-ICL(Lyuetal.,2022),generatespseudo-demos etyofcommonNLPtasks: fortheCLStasks,weinwithsynonymsofrandomclassnames. It,however, cludecommonsensereasoning: boolq(Clarketal.,
byassuminglabelknowledge,islimitedtoasub- 2019),copa(Roemmeleetal.,2011),winogrande
setofCLStaskswhereitisreasonabletodolabel (Sakaguchietal.,2021),ARCeasyandchallenge
synonymreplacement(e.g.,single-wordsentiment- (arc_e,arc_c)(Clarketal.,2018b),wsc(Levesque
describinglabels). Randomlyselectinglabelsalso etal.,2012);readingcomprehension: raceh,racem

<!-- Page 8 -->

Model Setting Zero-shot Few-shot

### Auto- Random USP

Method 0-shot 5-shot

### CoT demo (Ours)


### PaLM lambadaa 75.61/- 73.74/- 73.57/- 74.38/- 74.17/-

62B web_questions 12.30/25.98 18.21/36.33 17.96/33.65 20.37/36.62 27.76/42.90
natural_questions 18.45/27.29 21.60/30.80 20.39/29.90 23.85/33.69 27.59/37.39
triviaqa_wiki 67.71/72.85 69.49/74.17 70.43/74.84 69.84/74.14 62.11/67.29
squad∗ 69.59/75.34 85.11/89.14 80.30/84.88 83.63/87.88 79.85/83.96
Average↑ 48.73/55.41b 53.63/60.84b 52.53/59.37b 54.41/61.34b 54.30/61.14b
Gainover0-shot(%) 0.00/0.00b 10.05/9.79b 7.79/7.13b 11.66/10.70b 11.42/10.34b

### Averagerank↓c 4.00 2.80 3.40 2.00 2.80


### PaLM lambadaa 78.71/- 77.70/- 76.13/- 75.01/- 77.91/-

540B web_questions 10.33/23.60 16.04/31.76 20.47/36.55 25.64/43.31 33.61/47.92
natural_questions 20.49/31.04 29.31/39.36 29.00/39.34 32.19/43.56 35.88/46.50
triviaqa_wiki 76.73/81.85 78.73/84.05 80.52/84.89 80.10/84.57 73.78/79.52
squad∗ 75.67/80.85 90.93/94.37 88.47/92.93 90.29/94.06 88.83/92.39
Average↑ 52.39/59.21b 58.54/65.45b 58.92/65.97b 60.64/68.10b 62.00/68.85b
Gainover0-shot(%) 0.00/0.00b 11.75/10.54b 12.47/11.41b 15.76/15.02b 18.36/16.27b

### Averagerank↓c 4.00 2.80 3.20 2.60 2.40

Table3: ExactMatch(EM)/F1onSFGtasks. aOnlyEMshownaslambadaexpectsasinglecorrectanswer.
bUsedlambadaEMfortheaverageF1score. cRankedintermsofEM.∗SeenotesinApp.B.1. RefertoTable2for
furtherexplanations.
(Lai et al., 2017); cloze completion: storycloze themodelpredictionsratherthanpossibleclasses,
(Mostafazadeh et al., 2017), natural language in- the former of which is more likely to yield corference (NLI): anli-r{1,2,3} (Nie et al., 2020), rect pseudo-demos as long as the LLM is better
rte (Wang et al., 2018, 2019), wic (Pilehvar and than random guessing in zero shot; (iv) 5-shot,
Camacho-Collados,2019). FortheSFGtasks,we which uses the standard few-shot prompt with 5
includeopen-domainQA:web_questions(Berant demosrandomlysampledfromthetrainingset,as
etal.,2013),natural_questions(Kwiatkowskietal., inChowdheryetal.(2022)andBrownetal.(2020).
2019)andtriviaqa_wiki(Joshietal.,2017);reading Forafaircomparison,AutoCoT,Randomdemoand
comprehensionQA:squad(Rajpurkaretal.,2018); USPallgenerate5pseudo-demospersamplefrom
word prediction: lambada (Paperno et al., 2016). 64randomlysampled,unlabelledtestqueriesper
FortheLFGtasks,weincludetwosummarization task (i.e., D in §3.3). For SFG and LFG tasks retasks: xsum(Narayanetal.,2018)andwikilingua lyingonconsistency-basedconfidenceestimation,
(en – English only) (Ladhak et al., 2020). Note USP uniformly decode each query m = 6 times
thatwedonotconsidertheCoTreasoningtasks,as with a temperature of 0.7. We include all other
Wanetal.(2023)havealreadydemonstratedtheef- implementationdetailsinApp.B.
ficacyofconfidence-basedself-adaptiveprompting

### Discussionofmainresults. Weshowtheresults

inthesecases. ThereadersarereferredtoApp.A
of CLS, SFG and LFG tasks in Tables 2, 3 and 4,
formoredetailsonthemodelsanddatasetsconsidrespectively(weshowexamplesofthegenerated
ered.
pseudo-demosacrossvariousrepresentativetasks
Intermsofmethodsandbaselines,wecompare inTable9inApp. C.1). WefindthatUSPsignif-
USPagainst4baselines,namely(i)0-shot,which icantlyimprovesuponthestandardzero-shotperusesthestandard,directzero-shotprompting;(ii) formance,outperformsotherzero-shotprompting
AutoCoT,anadaptedversionofAutoCoTproposed methods and in many case is competitive against
inZhangetal.(2022)forgeneralNLPtasks;(iii) orbetterthanstandardfew-shotpromptingusing
Randomdemo,wherewefollowalloftheUSPpro- golden examples, all achieved with only 64 unlacedurebutinsteadofselectingthepseudo-demos belledsamplespertask. Acrossdatasetsandmodvia the scoring functions F(·), the K demos are els,wefindthemarginofimprovementtobelarger
randomly sampled from P – this serves both as in SFG & LFG tasks than CLS tasks, and larger in
an ablation baseline to USP and as a generaliza- PaLM-540BthanPaLM-62B.Ahypothesisforthe
tionformethodslikeZ-ICLdescribedin§4which formerobservationisthatLLMsbenefitmoreon
onlyworkforCLStasks,exceptthatRandomdemo guidance from the demonstration in these generisarguablystrongerasitrandomlysamplesfrom ative tasks, which essentially feature unbounded

<!-- Page 9 -->

Model Setting Zero-shot Few-shot

### Auto- Random USP

Method 0-shot 1-shot

### CoT demo (Ours)

PaLM xsum 17.7/14.1/0.183 19.8/15.5/0.338 19.1/15.3/0.317 21.9/17.1/0.347 24.3/19.1/0.337
62B wikilingua(en) 20.1/16.3/0.416 10.6/9.0/0.333 18.3/14.6/0.396 28.6/23.3/0.486 27.5/22.0/0.488
Average↑ 18.9/15.2/0.299 15.2/12.3/0.336 18.7/14.9/0.357 25.3/20.2/0.417 25.9/20.5/0.413
Gainover0-shot(%) 0.0/0.0/0.0 -19.5/-19.1/12.0 -1.0/-1.5/19.1 34.0/33.0/39.1 37.4/35.3/37.7
PaLM xsum 18.4/14.7/0.186 20.5/15.3/0.347 18.0/14.1/0.301 19.3/14.9/0.329 23.6/18.6/0.337
540B wikilingua(en) 20.1/16.1/0.390 14.1/11.6/0.399 21.2/17.2/0.425 30.5/24.3/0.496 29.7/24.0/0.488
Average↑ 19.3/15.4/0.288 17.3/13.4/0.373 19.6/15.6/0.363 24.9/19.6/0.412 26.7/21.3/0.413
Gainover0-shot(%) 0.0/0.0/0.0 -10.3/-12.6/29.8 1.7/1.8/26.3 29.2/27.4/43.3 38.3/38.5/43.4
Table4: ROUGE-1/ROUGE-Lsum/BLEURT(Sellametal.,2020)scoresonLFGtasks. Notethatdueto
the much longer context length in LFG problems considered, we follow Chowdhery et al. (2022) to generate 1
pseudo-demounderzero-shotsetting(ifapplicable),anduse1demonstrationunderfew-shotsetting(insteadof5in
Tables2and3). RefertoTable2forfurtherexplanations.
100
80
60
40
20
0
1 2 3 4 5 6 7 8 9 10
CLS decile
)%(
ycaruccA
storycloze
100
80
60
40
20
1 2 3 4 5 6 7 8 9 10
CLS decile
)%(
ycaruccA
rte
100
80
60
40
20
1 2 3 4 5 6 7 8 9 10
CLS decile
)%(
ycaruccA
racem
80
60
40
20
0
1 2 3 4 5 6 7 8 9 10
CLS decile
)%(
ycaruccA
anlir2
100
80
60
40
20
0
0.0 0.5 1.0

## Sfg

)%(

## Me

triviaqa_wiki
100
75
50
25
0
0.0 0.5 1.0

## Sfg

)%(

## Me

web_questions
30
20
10
0.2 0.4

## Lfg

muSL-EGUOR
document_wikilingua_en
30
20
10
0
0.0 0.2 0.4

## Lfg

muSL-EGUOR
article_xsum
Figure3: USPpicksconfidentpredictionsthataremorelikelybetter. USPscores(§3.3)againsttheground-truth
performancemetricsinthe64Stage1unlabelledsamples(D)inselectedtasksofvaryingdifficultyinPaLM-540B:
F againstaccuracy(CLS),F againstEM(SFG),andF againstROUGE-LSum(LFG).CLS:single-sample

## Cls Sfg Cls

accuracyisbinaryandwethusdiscretizeF NLU into10deciles&showthemeanaccuracy±1 SEM ineachbin.
SFG:SameasCLS,exceptthatF isalreadydiscrete&nofurtherdiscretizationisperformed;markersizesare

## Sfg

proportionaltonumbersofsamplesofeachF value. LFG:BoththeevaluationmetricandF arecontinuousand

## Sfg Lfg

weplotalldatawithoutaggregation–sincewequeryeachd(j) ∈D6times,weshowthemean±SEMground-truth
ROUGEscoreforeachd(j);gray×markersdenoteoutliers. TheoverallmeanperformanceoverD(graydashed
lines)andlineartrendlines&confidenceintervalsshowninallplots. MoreresultsinApp. C.2.
actionspaces,whereasinCLStheLLMonlyneeds meanperformanceofthemodelonly.
to select a response out of a few. On the latter
observation, we hypothesize that a reason is that HowdoesUSPwork? Weanalyzetheworking
larger models have stronger ICL capabilities to
mechanismofUSP;thatis,howdoespseudo-demo
learnfromthedemosandcanbettertakeadvantage
selection described in §3.3 lead to high-quality
ofthemoreaccurate/betterdemos(thefactthatthe
pseudo-demos & stronger performance? To do
5-shotresults(whosedemosareguaranteedtobe
so,weanalyzetherelationoftheUSPscoresand
correct) is stronger in PaLM-540B also supports the ground-truth performance (accuracy, EM or
this). Inthiscase,themoreaccurate/betterquality

### ROUGE,dependingonthetasktype)ofthequeries

pseudo-demos generated by USP (verified in Fig in unlabeled datasets D (with |D| = 64) for all
3)thusleadstoalargerout-performanceoverbasetasks. WeshowtherepresentativeresultsinFig. 3
lines,whosepseudo-demoqualitydependsonthe
(additionalresultsarereportedinApp.C),andwe

<!-- Page 10 -->

observe that in all task types and across tasks of whether there are potential remedies. We defer
varyingdifficulty(asmeasuredbytheaverageper- thoroughinvestigationstofuturework.
formancemarkedbythegraydashedlinesinFig.
3), the USP scores are generally well-correlated

### References

withtheground-truthperformance. Therecentfindings that larger language models genuinely learn JonathanBerant,AndrewChou,RoyFrostig,andPercy
informationfromin-contextexamples(insteadof Liang. 2013. Semantic parsing on Freebase from
simplyfollowingapromptformat)andthusbene- question-answerpairs. InProceedingsofthe2013
Conference on Empirical Methods in Natural Lanfitmorefromcorrectexamples(Weietal.,2023)
guageProcessing,pages1533–1544,Seattle,Washare consistent with the results of USP, which, as
ington,USA.AssociationforComputationalLinguiswe show, is more likely to generate correct/high- tics.
qualitypseudo-demos.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah,JaredDKaplan,PrafullaDhariwal,Arvind
6 Conclusion
Neelakantan,PranavShyam,GirishSastry,Amanda

### Askell,etal.2020. Languagemodelsarefew-shot

We propose USP, an automatic prompting tech- learners. Advancesinneuralinformationprocessing
niquetailoredforzero-shotlearningthatishighly systems,33:1877–1901.
versatile and applicable to a wide range of NLU
Sébastien Bubeck, Varun Chandrasekaran, Ronen Eland NLG tasks, by carefully selecting zero-shot
dan, Johannes Gehrke, Eric Horvitz, Ece Kamar,
model-generated outputs for in-context learning. Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lund-
We show large improvement over standard zero- berg,etal.2023. Sparksofartificialgeneralintelligence: Earlyexperimentswithgpt-4. arXivpreprint
shotpromptingandotherbaselinesinover20tasks
arXiv:2303.12712.
in2modelLLMs.
We believe that the room for future improve- AakankshaChowdhery,SharanNarang,JacobDevlin,

### Maarten Bosma, Gaurav Mishra, Adam Roberts,

ments is ample: first, the present work specif-

### Paul Barham, Hyung Won Chung, Charles Sutton,

ically targets in-context demonstrations, a sub-

### Sebastian Gehrmann, et al. 2022. Palm: Scaling

componentoftheoverallprompt,anditdoesnot language modeling with pathways. arXiv preprint
attempttooptimizetheothercomponents;afuture arXiv:2204.02311.
workwouldberelaxingthisrestrictionandcombin-

### Christopher Clark, Kenton Lee, Ming-Wei Chang,

ing the current technique with automatic prompt

### Tom Kwiatkowski, Michael Collins, and Kristina

designformoreflexibleprompting. Second,given Toutanova.2019. BoolQ:Exploringthesurprising
theever-improvingcapabilitiesofLLMs,itwould difficultyofnaturalyes/noquestions. InProceedings
bealsointerestingtoapplytheideainmorenovel ofthe2019ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:
setups,includingbutnotlimitedtoplanning(where

### HumanLanguageTechnologies,Volume1(Longand

LLMsactasautonomous,environment-interacting ShortPapers),pages2924–2936,Minneapolis,Minagents)andmulti-modalsettingsbeyondpureNLP nesota.AssociationforComputationalLinguistics.
problems. Lastly, we note that especially for the
KevinClark,Minh-ThangLuong,ChristopherDMangenerativetasks(SFGandLFG),inmanycasesUSP
ning, and Quoc V Le. 2018a. Semi-supervised segreatly improves the zero-shot performance but quence modeling with cross-view training. arXiv
doesnotalwayscompletelyclosethegapcompared preprintarXiv:1809.08370.
to the few-shot baseline using golden examples.
PeterClark,IsaacCowhey,OrenEtzioni,TusharKhot,

### TherearealsocaseswhereUSPdoesnotmeaning-


### AshishSabharwal,CarissaSchoenick,andOyvind

fully improve over zero-shot baselines – we note Tafjord.2018b. ThinkyouhavesolvedquestionanthatwhiletheUSPscoresintroducedaregenerally swering? tryarc,theai2reasoningchallenge. arXiv
well-correlatedwiththeground-truthperformance, preprintarXiv:1803.05457.
suchacorrelationisnotperfectandtherearecases
Mingkai Deng, Jianyu Wang, Cheng-Ping Hsieh, Yiespeciallywhenthezero-shotperformanceisvery hanWang,HanGuo,TianminShu,MengSong,Eric
poororwhenthemodelisill-calibrated,thescores Xing,andZhitingHu.2022. RLPrompt: Optimizing
are less helpful. We believe it would be benefi- discrete text prompts with reinforcement learning.
In Proceedings of the 2022 Conference on Empiricialtoconductathoroughanalysisontheseissues,
calMethodsinNaturalLanguageProcessing,pages
which would inform us on when and when not
3369–3391,AbuDhabi,UnitedArabEmirates.AsapromptingtechniquelikeUSPwouldhelp, and sociationforComputationalLinguistics.

<!-- Page 11 -->

ShizheDiao,ZhichaoHuang,RuijiaXu,XuechunLi, HectorLevesque,ErnestDavis,andLeoraMorgenstern.
YongLin,XiaoZhou,andTongZhang.2022. Black- 2012. The winograd schema challenge. In Thirboxpromptlearningforpre-trainedlanguagemodels. teenthinternationalconferenceontheprinciplesof
arXivpreprintarXiv:2201.08531. knowledgerepresentationandreasoning.
Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiy- Xiang Lisa Li and Percy Liang. 2021. Prefix-tuning:
ongWu,BaobaoChang,XuSun,JingjingXu,and Optimizing continuous prompts for generation. In
ZhifangSui.2022. Asurveyforin-contextlearning. Proceedingsofthe59thAnnualMeetingoftheAssoarXivpreprintarXiv:2301.00234. ciationforComputationalLinguisticsandthe11th

### InternationalJointConferenceonNaturalLanguage

Yves Grandvalet and Yoshua Bengio. 2004. Semi- Processing (Volume 1: Long Papers), pages 4582–
supervised learning by entropy minimization. Ad- 4597, Online. Association for Computational Linvancesinneuralinformationprocessingsystems,17. guistics.
OrHonovich,ThomasScialom,OmerLevy,andTimo JiachangLiu,DinghanShen,YizheZhang,BillDolan,
Schick. 2022. Unnatural instructions: Tuning lan- Lawrence Carin, and Weizhu Chen. 2022. What
guagemodelswith(almost)nohumanlabor. arXiv makes good in-context examples for GPT-3? In
preprintarXiv:2212.09689. ProceedingsofDeepLearningInsideOut(DeeLIO
2022): The 3rd Workshop on Knowledge Extrac-
JiaxinHuang,ShixiangShaneGu,LeHou,YuexinWu, tionandIntegrationforDeepLearningArchitectures,
XuezhiWang,HongkunYu,andJiaweiHan.2022. pages100–114,Dublin,IrelandandOnline.Associa-
Large language models can self-improve. arXiv tionforComputationalLinguistics.
preprintarXiv:2210.11610.
RobertLoganIV,IvanaBalazevic,EricWallace,Fabio
Petroni,SameerSingh,andSebastianRiedel.2022.
Mandar Joshi, Eunsol Choi, Daniel Weld, and Luke

### Cutting down on prompts and parameters: Simple


### Zettlemoyer.2017. TriviaQA:Alargescaledistantly

few-shot learning with language models. In FindsupervisedchallengedatasetforreadingcompreheningsoftheAssociationforComputationalLinguission. InProceedingsofthe55thAnnualMeetingof
tics: ACL2022,pages2824–2835,Dublin,Ireland.
theAssociationforComputationalLinguistics(Vol-
AssociationforComputationalLinguistics.
ume1: LongPapers),pages1601–1611,Vancouver,
Canada.AssociationforComputationalLinguistics.

### XinxiLyu,SewonMin,IzBeltagy,LukeZettlemoyer,

andHannanehHajishirzi.2022. Z-icl: Zero-shotin-
TomKwiatkowski, JennimariaPalomaki, OliviaRedcontextlearningwithpseudo-demonstrations. arXiv
field,MichaelCollins,AnkurParikh,ChrisAlberti,
preprintarXiv:2212.09865.
DanielleEpstein,IlliaPolosukhin,JacobDevlin,KentonLee,KristinaToutanova,LlionJones,Matthew

### YuMeng,YunyiZhang,JiaxinHuang,ChenyanXiong,

Kelcey, Ming-Wei Chang, Andrew M. Dai, Jakob

### HengJi, ChaoZhang, andJiaweiHan.2020. Text

Uszkoreit, Quoc Le, and Slav Petrov. 2019. Natuclassification using label names only: A language
ralquestions: Abenchmarkforquestionanswering
modelself-trainingapproach. InProceedingsofthe
research. TransactionsoftheAssociationforCompu-
2020ConferenceonEmpiricalMethodsinNatural
tationalLinguistics,7:452–466.

### LanguageProcessing(EMNLP),pages9006–9017,

Online.AssociationforComputationalLinguistics.
FaisalLadhak,EsinDurmus,ClaireCardie,andKathleenMcKeown.2020. WikiLingua: Anewbench- SewonMin,XinxiLyu,AriHoltzman,MikelArtetxe,
markdatasetforcross-lingualabstractivesummariza- MikeLewis,HannanehHajishirzi,andLukeZettletion. In Findings of the Association for Computa- moyer.2022. Rethinkingtheroleofdemonstrations:
tionalLinguistics: EMNLP2020,pages4034–4048, Whatmakesin-contextlearningwork? InProceed-
Online.AssociationforComputationalLinguistics. ingsofthe2022ConferenceonEmpiricalMethodsin

### NaturalLanguageProcessing,pages11048–11064,

Guokun Lai, Qizhe Xie, Hanxiao Liu, Yiming Yang, AbuDhabi,UnitedArabEmirates.Associationfor
andEduardHovy.2017. RACE:Large-scaleReAd- ComputationalLinguistics.
ing comprehension dataset from examinations. In
Proceedings of the 2017 Conference on Empirical SwaroopMishra,DanielKhashabi,ChittaBaral,Yejin
MethodsinNaturalLanguageProcessing,pages785– Choi, and Hannaneh Hajishirzi. 2022. Reframing
794,Copenhagen,Denmark.AssociationforCompu- instructionalpromptstoGPTk’slanguage. InFindtationalLinguistics. ingsoftheAssociationforComputationalLinguistics:

### ACL2022,pages589–612,Dublin,Ireland.Associa-

BrianLester,RamiAl-Rfou,andNoahConstant.2021. tionforComputationalLinguistics.

### The power of scale for parameter-efficient prompt

tuning. InProceedingsofthe2021Conferenceon Takeru Miyato, Shin-ichi Maeda, Masanori Koyama,
EmpiricalMethodsinNaturalLanguageProcessing, and Shin Ishii. 2018. Virtual adversarial training:
pages3045–3059,OnlineandPuntaCana,Domini- a regularization method for supervised and semican Republic. Association for Computational Lin- supervisedlearning. IEEEtransactionsonpattern
guistics. analysisandmachineintelligence,41(8):1979–1993.

<!-- Page 12 -->

Nasrin Mostafazadeh, Michael Roth, Annie Louis, Meeting of the Association for Computational Lin-
Nathanael Chambers, and James Allen. 2017. Ls- guistics(Volume2: ShortPapers), pages784–789,
dsem 2017 shared task: The story cloze test. In Melbourne,Australia.AssociationforComputational
Proceedingsofthe2ndWorkshoponLinkingModels Linguistics.
ofLexical,SententialandDiscourse-levelSemantics,
pages46–51. Nils Reimers and Iryna Gurevych. 2019. Sentence-

### BERT:SentenceembeddingsusingSiameseBERT-

Shashi Narayan, Shay B. Cohen, and Mirella Lapata. networks. InProceedingsofthe2019Conferenceon

## Don’tgivemethedetails,justthesummary! EmpiricalMethodsinNaturalLanguageProcessing

topic-aware convolutional neural networks for ex- andthe9thInternationalJointConferenceonNatutreme summarization. In Proceedings of the 2018 ralLanguageProcessing(EMNLP-IJCNLP),pages
Conference on Empirical Methods in Natural Lan- 3982–3992,HongKong,China.AssociationforComguageProcessing,pages1797–1807,Brussels,Bel- putationalLinguistics.
gium.AssociationforComputationalLinguistics.
LariaReynoldsandKyleMcDonell.2021. Promptpro-

### JianmoNi,GustavoHernandezAbrego,NoahConstant,

gramming for large language models: Beyond the
JiMa,KeithHall,DanielCer,andYinfeiYang.2022. few-shot paradigm. In Extended Abstracts of the
Sentence-t5: Scalable sentence encoders from pre- 2021CHIConferenceonHumanFactorsinComputtrained text-to-text models. In Findings of the As- ingSystems,pages1–7.
sociationforComputationalLinguistics: ACL2022,
pages1864–1874,Dublin,Ireland.Associationfor Melissa Roemmele, Cosmin Adrian Bejan, and An-
ComputationalLinguistics. drew S Gordon. 2011. Choice of plausible alternatives: Anevaluationofcommonsensecausalrea-
YixinNie,AdinaWilliams,EmilyDinan,MohitBansal,
soning. InAAAIspringsymposium: logicalformal-
JasonWeston,andDouweKiela.2020. Adversarial
izationsofcommonsensereasoning,pages90–95.
NLI:Anewbenchmarkfornaturallanguageunderstanding. InProceedingsofthe58thAnnualMeet-
Ohad Rubin, Jonathan Herzig, and Jonathan Berant.
ingoftheAssociationforComputationalLinguistics,

## Learning to retrieve prompts for in-context

pages4885–4901,Online.AssociationforComputalearning. InProceedingsofthe2022Conferenceof
tionalLinguistics.
theNorthAmericanChapteroftheAssociationfor

### ComputationalLinguistics: HumanLanguageTech-

DenisPaperno,GermánKruszewski,AngelikiLazarinologies, pages 2655–2671, Seattle, United States.
dou,NgocQuanPham,RaffaellaBernardi,Sandro
AssociationforComputationalLinguistics.
Pezzelle,MarcoBaroni,GemmaBoleda,andRaquel

### Fernández. 2016. The LAMBADA dataset: Word

MehdiSajjadi,MehranJavanmardi,andTolgaTasdizen.
prediction requiring a broad discourse context. In

## Regularizationwithstochastictransformations

Proceedings of the54th Annual Meeting of the Asandperturbationsfordeepsemi-supervisedlearning.
sociationforComputationalLinguistics(Volume1:

### Advancesinneuralinformationprocessingsystems,

Long Papers), pages 1525–1534, Berlin, Germany.
29.
AssociationforComputationalLinguistics.
KeisukeSakaguchi,RonanLeBras,ChandraBhagavat-
MohammadTaherPilehvarandJoseCamacho-Collados.
ula,andYejinChoi.2021. Winogrande: Anadver-

## WiC: the word-in-context dataset for evalusarialwinogradschemachallengeatscale. Commuatingcontext-sensitivemeaningrepresentations. In

nicationsoftheACM,64(9):99–106.
Proceedings of the 2019 Conference of the North

### AmericanChapteroftheAssociationforComputa-

ThibaultSellam,DipanjanDas,andAnkurParikh.2020.
tionalLinguistics: HumanLanguageTechnologies,
BLEURT: Learning robust metrics for text genera-
Volume1(LongandShortPapers),pages1267–1273,
tion. InProceedingsofthe58thAnnualMeetingof
Minneapolis,Minnesota.AssociationforComputatheAssociationforComputationalLinguistics,pages
tionalLinguistics.
7881–7892,Online.AssociationforComputational
Linguistics.

### Archiki Prasad, Peter Hase, Xiang Zhou, and Mohit

Bansal. 2022. Grips: Gradient-free, edit-based in-

### Tianxiao Shen, Myle Ott, Michael Auli, and

structionsearchforpromptinglargelanguagemodels.
Marc’Aurelio Ranzato. 2019. Mixture models for
arXivpreprintarXiv:2203.07281.
diversemachinetranslation: Tricksofthetrade. In
ColinRaffel,NoamShazeer,AdamRoberts,Katherine Internationalconferenceonmachinelearning,pages
Lee,SharanNarang,MichaelMatena,YanqiZhou, 5719–5728.PMLR.

### WeiLi,andPeterJLiu.2020. Exploringthelimits

oftransferlearningwithaunifiedtext-to-texttrans- TaylorShin,YasamanRazeghi,RobertL.LoganIV,Eric
former. TheJournalofMachineLearningResearch, Wallace,andSameerSingh.2020. AutoPrompt:Elic-
21(1):5485–5551. itingKnowledgefromLanguageModelswithAutomaticallyGeneratedPrompts. InProceedingsofthe
Pranav Rajpurkar, Robin Jia, and Percy Liang. 2018. 2020ConferenceonEmpiricalMethodsinNatural
Know what you don’t know: Unanswerable ques- LanguageProcessing(EMNLP),pages4222–4235,
tionsforSQuAD. InProceedingsofthe56thAnnual Online.AssociationforComputationalLinguistics.

<!-- Page 13 -->

YiTay, MostafaDehghani, VinhQTran, XavierGar- YongqinXian,BerntSchiele,andZeynepAkata.2017.
cia, JasonWei, XuezhiWang, HyungWonChung, Zero-shot learning-the good, the bad and the ugly.
DaraBahri,TalSchuster,StevenZheng,etal.2022. InProceedingsoftheIEEEconferenceoncomputer
Ul2: Unifyinglanguagelearningparadigms. InThe visionandpatternrecognition,pages4582–4591.
EleventhInternationalConferenceonLearningRep-
Eric Zelikman, Jesse Mu, Noah D Goodman, and
resentations.

### YuhuaiTonyWu.2022. Star: Self-taughtreasoner

JohnWTukeyetal.1977. Exploratorydataanalysis, bootstrappingreasoningwithreasoning.
volume2. Reading,MA.

### TianjunZhang,XuezhiWang,DennyZhou,DaleSchu-

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob urmans, and Joseph E Gonzalez. 2023. Tempera:
Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Test-timeprompteditingviareinforcementlearning.
Kaiser,andIlliaPolosukhin.2017. Attentionisall InTheEleventhInternationalConferenceonLearnyouneed. Advancesinneuralinformationprocessing ingRepresentations.
systems,30.

### Zhuosheng Zhang, Aston Zhang, Mu Li, and Alex

Smola. 2022. Automatic chain of thought prompt-

### XingchenWan,RuoxiSun,HanjunDai,SercanOArik,

ing in large language models. arXiv preprint
andTomasPfister.2023. Betterzero-shotreasoning
arXiv:2210.03493.
withself-adaptiveprompting. InFindingsoftheAssociationforComputationalLinguistics: ACL2023,

### XuandongZhao, SiqiOuyang, ZhiguoYu, MingWu,

Toronto,Canada.AssociationforComputationalLinand Lei Li. 2022. Pre-trained language models
guistics.
can be fully zero-shot learners. arXiv preprint
arXiv:2212.06950.
AlexWang,YadaPruksachatkun,NikitaNangia,AmanpreetSingh,JulianMichael,FelixHill,OmerLevy, Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han,
and Samuel Bowman. 2019. Superglue: A stick- KeiranPaster,SilviuPitis,HarrisChan,andJimmy
ierbenchmarkforgeneral-purposelanguageunder- Ba.2022. Largelanguagemodelsarehuman-level
standingsystems. Advancesinneuralinformation promptengineers. arXivpreprintarXiv:2211.01910.
processingsystems,32.

### A DatasetsandModels


### Alex Wang, Amanpreet Singh, Julian Michael, Felix

Hill,OmerLevy,andSamuelBowman.2018. GLUE: A.1 Datasets

### Amulti-taskbenchmarkandanalysisplatformfornat-

We outline the details of the datasets used in this
urallanguageunderstanding. InProceedingsofthe
2018 EMNLP Workshop BlackboxNLP: Analyzing studyinTable5.
and Interpreting Neural Networks for NLP, pages
353–355,Brussels,Belgium.AssociationforCom- A.2 Models
putationalLinguistics.

### WeconductexperimentsontwoPaLMmodelvari-

XuezhiWang,JasonWei,DaleSchuurmans,QuocLe, ants – one with 540 billion parameters (PaLM-
EdChi,andDennyZhou.2022. Self-consistencyim- 540B)andonewith62billionparameters(PaLM-
proveschainofthoughtreasoninginlanguagemod- 62B). PaLM is a transformer-based LLM “preels. arXivpreprintarXiv:2203.11171.
trainedonahigh-qualitycorpusof780billionto-
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, kensthatcomprisevariousnaturallanguagetasks
Barret Zoph, Sebastian Borgeaud, Dani Yogatama, andusecases. Thisdatasetincludesfilteredweb-
MaartenBosma,DennyZhou,DonaldMetzler,etal.
pages, books, Wikipedia articles, news articles,
2022a. Emergentabilitiesoflargelanguagemodels.
source code obtained from open source repositoarXivpreprintarXiv:2206.07682.
ries on GitHub, and social media conversations”

### JasonWei,XuezhiWang,DaleSchuurmans,Maarten

(Chowdheryetal.,2022). Forthepretrainingpro-
Bosma,EdChi,QuocLe,andDennyZhou.2022b.
cedure,PaLMwastrainedovertwoTPUv4Pods

### Chainofthoughtpromptingelicitsreasoninginlarge

languagemodels. arXivpreprintarXiv:2201.11903. with3072TPUv4chips(Chowdheryetal.,2022).

### In all experiments, we use the quantized PaLM

Jerry Wei, Jason Wei, Yi Tay, Dustin Tran, Albert
checkpoints(quantizedtoint8precision)forinfer-

### Webson, Yifeng Lu, Xinyun Chen, Hanxiao Liu,

enceonlywithoutfurtherpretrainingorfinetuning.

### DaHuang,DennyZhou,etal.2023. Largerlanguage

models do in-context learning differently. arXiv
preprintarXiv:2303.03846. B ImplementationDetails
YuxinWen,NeelJain,JohnKirchenbauer,MicahGold- B.1 PromptTemplates
blum,JonasGeiping,andTomGoldstein.2023. Hard

### WelargelyadoptthepromptformatusedinGPT-3

prompts made easy: Gradient-based discrete opti-
(Brownetal.,2020)wherepossible,andweshow
mization for prompt tuning and discovery. arXiv
preprintarXiv:2302.03668. thedetailedprompttemplatesinTables6,7and8.

<!-- Page 14 -->

Dataset Tasktype Objective Testsetsize #classes |D|/|T|

## (§3.3) |T| |C| (%)

winogrande CLS commonsensereasoning 1267 2 5.05
piqa CLS commonsensereasoning 1838 2 3.48
storycloze CLS commonsensereasoning 1871 2 3.42
anlir1 CLS NLI 1000 3 6.40
anlir2 CLS NLI 1000 3 6.40
anlir3 CLS NLI 1200 3 4.53
boolq CLS commonsensereasoning 3270 2 1.96
copa CLS commonsensereasoning 100 2 64.0
rte CLS NLI 277 2 23.1
wic CLS contextcomprehension 638 2 10.0
wsc CLS commonsensereasoning 285 2 22.5
arc_e CLS commonsensereasoning 2365 4 2.71
arc_c CLS commonsensereasoning 1165 4 5.49
raceh CLS readingcomprehensionMCQ 3498 4 1.83
racem CLS readingcomprehensionMCQ 1436 4 4.46
lambada SFG wordcompletioncloze 5153 n/a 1.24
web_questions SFG open-domainQA 2032 n/a 3.15
natural_questions SFG open-domainQA 3610 n/a 1.77
triviaqa_wiki SFG open-domainQA 7993 n/a 0.80
xsum LFG summarization 1166 n/a 5.49
wikilingua LFG summarization 15001 n/a 4.27
MCQ:multiplechoicequestion. NLI:naturallanguageinference.
1Usedarandomsubsetof1500articlesinthevalidationset.
Table5: Detailsofthedatasetsusedinthiswork. Notethattestsetherereferstothesplitofthedatasetonwhich
resultsofthispaperisreported–insomedatasetsthetestlabelsarenotpubliclyavailable,andweinsteadreport
performanceonthedev/validationset. Thefinalcolumn(|D|/|T|)denotesthepercentageofthetestsetthatisused
astheunlabelleddatasetDforpseudo-demogenerationofUSP,AutoCoTandRandomdemos.
It is worth noting that some datasets (raceh, prependedtothetestqueriesand(2)evenforthe
racemandsquad)arenotzero-shotintheirstrictest model-generateddemos,theremaybepartsofthe
sense even when no demonstration is provided – pseudo-demos that are guaranteed to be correct
we follow the GPT-3 prompt format (Fig. G.1, simplyduetothepromptingformat. Anothercom-
G.3 and G.28 respectively for raceh, racem and plicationofsuchapromptformatformethodsussquad in Brown et al. (2020)). In these datasets, ingpseudo-demos(AutoCoT,Randomdemo,USP)
each test query consists of a context article and is that since the responses to the a subset of test
several reading comprehension questions in rela- queriesareusedasdemonstrationsthemselves,it
tion to that article, and even in the absence of ispossiblethatasmallnumbersolutionstosome
demonstrations(intheformofoneormoreother questionsarerevealedtotheLLMsintheformof
articles and answered questions associated with solvedquestionsinsomedemonstrations. However,
thosearticles),somequestions(otherthanthetest giventhatonly5pseudo-demonstrationsareused
questionitself)andtheirsolutionstothesamear- perquestion,theimpactisinsignificantasthetest
ticle are included nevertheless. Therefore, even sets of each of these datasets contains thousands
in the zero-shot setup, the LLM is shown with to tens of thousands of queries (detailed in Table
somedemonstrationwhilebeing“zero-shot”inthe 5). Furthermore, no method is given more unfair
sense that the context article itself is novel. Sim- advantageoveranotherone,asallmethods,includilarly, “K pseudo-demos” in these datasets refer ingUSPandkeybaselineswecompareagainst,are
toK (pseudo)-demonstrations,eachofwhichcon- subjecttothesamecomplication,andthusweresistsofasinglearticleandtheirassociatedques- portresultstothesedatasetsneverthelessbutmark
tions (which can be multiple) – in this sense, (1) theimpactedresultsinTables2and3withaspecial
therearetypicallymorethanK solvedquestions note.

<!-- Page 15 -->

100
80
60
40
1 2 3 4 5 6 7 8 910

### CLS decile

)%( ycaruccA
winogrande
100
80
60
40
1 2 3 4 5 6 7 8 910

### CLS decile

)%( ycaruccA
piqa
100
80
60
40
20
1 2 3 4 5 6 7 8 910

### CLS decile

)%( ycaruccA
anlir1
100
80
60
40
20
0
1 2 3 4 5 6 7 8 910

### CLS decile

)%( ycaruccA
anlir3
100
80
60
40
1 2 3 4 5 6 7 8 910
CLS decile
)%(
ycaruccA
copa
100
80
60
40
20
0
1 2 3 4 5 6 7 8 910
CLS decile
)%(
ycaruccA
wic
100
80
60
1 2 3 4 5 6 7 8 910
CLS decile
)%(
ycaruccA
wsc
100
80
60
40
20
1 2 3 4 5 6 7 8 910
CLS decile
)%(
ycaruccA
arc_e
100
80
60
40
20
0
1 2 3 4 5 6 7 8 910
CLS decile
)%(
ycaruccA
raceh
100
80
60
40
20
0
0.0 0.5 1.0

## Sfg

)%(

## Me

lambada
100
80
60
40
20
0
0.0 0.5 1.0

## Sfg

)%(

## Me

squadv2
100
80
60
40
20
0
0.0 0.5 1.0

## Sfg

)%(

## Me

natural_questions
Figure4: ComplementarytoFig. 3,weshowthesameplot(USPscoresvs. ground-truthperformancemetrics)in
additionaltasks. RefertoFig. 3forfurtherexplanations.
+20%
+10%
0
-10%
-20%
1 2 3 4 5 6 7 8 9 10
CLS Decile
.cca
naem
+20%
+10%
0
-10%
-20%
1 2 3 4 5 6 7 8 9 10
CLS Decile
.cca
naem
to signal end of response. Additionally, we also
applyseveraladditionalpost-processingstepsfor
thegenerativetasks,inUSPandallotherbaseline
methods:
1. lambada: retainthefirstoutputword.
2. squad: remove punctuation marks, remove
article words (a, an, the) and retain the

### Figure5: ComparisonbetweentheUSPscoreagainst

accuracy, averaged across all CLS tasks considered in portionoftheoutputsbeforeanynewline(\n).
thispaperforPaLM-62B(left)andPaLM-540B(right).
3. web_questions&natural_questions: replace

### Markersanderrorbarsdenotemean±SEM.Itisevident

thatonexpectation,querieswithhigherUSPscoretend allpunctuationmarkswithawhitespace,retobebetterperformingcomparedtotheaveragemodel movearticlewords(a, an, the)andretain
performance(markedbythegraydashedline). theportionoftheoutputsbeforeanynewline
(\n)

### B.2 AdditionalExperimentalDetails


## LFG(summarization): sinceweusedtheprefix


### USP. USPusesanauxiliarylanguagemodelfor

“Article: ” at the start of each article to be
computingthesimilarityterminEq. (3). Weuse
summarized,wealsoadd“Article: ” tothe
Sentence-T5-large(Nietal.,2022)forallourexlist of stop tokens in addition to the general
periments. We use a maximum decoding step of
onesdescribedabove.
128tokensforallexperiments. Forsummarization
tasks,weapplyanadditionalfilteringruletoretain Baselines. We use the same filtering rule for
answerswhosenumberofwordsisbetween5and thebaselinemethodsasUSP.Asdiscussed,Ran-
90(topruneoutoverlyshortandoverlylongsum- domdemobaselineusesanidenticalprocedureto
marieswhichareobviouslysub-optimal). Forall USP,withthesoleexceptionthatitdoesnotrely
tasks, we use the following stop tokens as marks on the scoring functions in 3.3 to select the set
fortruncation(wordsafteranystoptokens,includ- of pseudo-demos but rather, for each test query
ingthestoptokensthemselves,aretruncated): “Q:, T = {x(i)}N , it samples K pseudo-demos rani=1
A:, \n\n”andotherspecialtokensusedinPaLM domlyfromallStage1responses(notethatforCLS

<!-- Page 16 -->

tasks,itwillalsofollowtheproceduresdescribed
in§3.3toensurefairallocationofpseudo-demos
across classes). For AutoCoT, we adapt from
theofficialimplementationavailableathttps://
github.com/amazon-science/auto-cot with a
fewkeymodifications: (i)followingCOSP,wealso
replacetheSentenceBERT(ReimersandGurevych,
2019)withSentenceT5,amorepowerfulsentenceleveltransformer,forfaircomparisonagainstUSP;
(ii)giventhatAutoCoTisoriginallydesignedfor
chain-of-thought(CoT)tasksonly,wealsomake
necessarymodificationssuchthatitiscompatible
withthegeneralsetup. Thechangesareinfactminimal–weonlyreplacetheoriginalfilteringrulesin

### CoTwiththeoneswedescribedaboveforUSP.For

the few-shot baseline, we closely follow existing
works(Brownetal.,2020;Chowdheryetal.,2022)
tosampleK demonstrationsfromthetrainingsplit
of each dataset considered, which are prepended
tothetestqueries;weperformsamplingforeach
test queries, and thus the choice and order of the
demonstrationsingeneraldifferfromonequeryto
another. Weusetheidenticalpostprocessingrules
as USP mentioned in the previous paragraph for
thebaselines.

### C AdditionalExperiments


### C.1 ExamplesofSelectedPseudo-demos

Weshowsomeexamplesofthepseudo-demosgeneratedbyUSPonavarietyofrepresentativetasks
inTable9.
C.2 AdditionalComparisonBetweenUSP

### ScoresandGround-truthQuality

Complementary to Fig. 3 in §5, we show plots
ofthesamerelationforothertasksconsideredin

### PaLM-540BinFig. 4,andtheaggregatedresults

(acrossCLStasks)inFig. 5. ThesegivefurtherevidencethatUSPheuristicdescribedin§3.3selects
higherqualitydemonstrationsincomparisontothe
averagemodelperformance.

<!-- Page 17 -->


### Dataset Prompttemplate

winogrande The woman avoided the hole but easily stepped over the pit over the {hole / pit},
because the hole was very shallow
piqa Q: To pour hot fudge over ice cream before serving,\nA: { pour the hot fudge over ice
cream that has just been pulled from the freezer and scooped out of it’s container with
an ice cream scoop into a bowl / pour the hot fudge over ice cream that has been pulled
out of the freezer and softened for fifteen minutes, then scooped out of it’s container
with an ice cream scoop into a bowl. }
storycloze Neil wanted to see ancient temples and ruins. He decided Asia was a great place to start.
He flew to Cambodia and went sightseeing. He saw so many old temples in the jungles
there. {Neil was bored of the trip and went home. / Neil was happy he made the trip.}
anlir{1,2,3} Lofar is a Telugu film directed by Puri Jagannadh. It features Varun Tej and Disha Patani
in the lead roles while Revathi and Posani Krishna Murali appear in crucial supporting
roles. The film was officially launched on 8 July 2015 in Hyderabad. Earlier makers
revealed the first look posters and trailer of the movie which received good response
in the social media.\nquestion: Varun Tej had billing over Disha Patani in Lofar. Is it
true, false, or neither?\nanswer: {true / false / neither}
boolq Evil Queen (Disney) – This version of the fairy tale character has been very well
received by film critics and the public, and is considered one of Disney’s most iconic
and menacing villains. Besides in the film, the Evil Queen has made numerous appearances
in Disney attractions and productions, including not only these directly related to
the tale of Snow White, such as Fantasmic!, The Kingdom Keepers and Kingdom Hearts
Birth by Sleep, sometimes appearing in them alongside Maleficent from Sleeping Beauty.
The film’s version of the Queen has also become a popular archetype that influenced a
number of artists and non-Disney works.\nquestion: are maleficent and the evil queen
the same\nanswer: {yes / no}
copa The tree branch landed in the river {so the branch moved downstream. / the river’s
current became stronger.}
rte Tropical Storm Irene on August 11, 2005 at 16:15 UTC. Tropical Storm Irene will increase
in strength over the next several days, possibly developing into a hurricane that will
hit the east coast of the United States, said the National Hurricane Center of Miami,
Florida in a report today. Irene was located approximately 975 kilometers south-southeast
of Bermuda at 16:00 UTC today. Forecasters say that the storm is now moving in a westnorthwest direction with top sustained winds of 40 miles per hour.\nquestion: A storm
called Irene is going to approach the east coast of the US. Is it true or false?\nanswer:
{true / false}
wic Had unusual longevity in the company.\nHer longevity as a star.\nquestion: is the word
’longevity’ used in the same way in the two sentences above?\nanswer: {Yes / No}
wsc {The city councilmen refused the demonstrators a permit because The demonstrators / The
city councilmen refused the demonstrators a permit because The city councilmen} feared
violence.
arc_{c,e} Q: Which tool should be used to measure the stem length of a plant?\nA: {a balance / a
metric ruler / a graduated cylinder / a thermometer}
race{h,m} ’Article: October is getting closer and it also means that the year of 2014 is coming
to an end. "Hooray! It’s a holiday!" While you are thinking of putting textbooks aside
and playing video games, let’s take a look at what children in other continents usually
do during their holidays. Children in America don’t have much homework to do. They
keep themselves busy by playing camp games. A parent says, "My daughter Shirley usually
attends different camps. We don’t ask her to spend plenty of time on maths problems or
spelling tests." Children in Australia take partin activities on over twenty different
themes . They learn painting, dancing, singing, history, culture and so on. Parents
can _ their kids to enjoy the learning process and to build a closer relationship with
them. These are what African kids do: build a boat, have a camel race, make a drum and
make a rag football. Don’t you think it is interesting that kids in other places have
no idea how to make a drum, but kids in Africa do? Plan your holiday well and try what
you want to try. Make a good plan and you will have a lot of fun. Q: Where does Shirley
come from? A: {America, China, Brazil, Australia}
Table6: Prompttemplates(withexamples)oftheCLSdatasetsused. Notethattheanlir{1,2,3},race{m,h},arc_c,e}
datasetsaregroupedtogetherduetosimilarpromptformat. TheLLMisaskedtooutputthelog-likelihoodusing
eachoftheoptionsmarkedinblueasapossibletextcompletion,andtheoptionwiththehighestpredictedprobability
isselectedasthefinalprediction. Notethattherace_{h,m}datasetsarenotstrictlyzero-shotasthepromptalready
containsseveralansweredquestionstothecontextpassageleadinguptothetextquery–seeApp. B.1fordetailed
explanations.

<!-- Page 18 -->


### Dataset Prompttemplate

lambada Yes, I am absolutely sure you did, Cook. I can see the empty egg boxes like you said,
thirteen of them.”\nCaptain Porter was used to getting to the bottom of these sorts of
incidents, especially when it involved some of his boys.\n“Has anyone else been in the
kitchen, Cook
web_questions Q: who were jesus siblings?\nA:{Jude the Apostle / James the Just / Simon (brother of

### Jesus) / Joses}

natural_questions Q: how long is the bridge between new brunswick and prince edward island\nA: 2.9-kilometre
triviaqa_wiki Q: How many medals did the United States win at the 2010 Winter Olympics?\nA:{37 / thirty
seven}
squad Title: Southern_California\n\nBackground: The San Bernardino-Riverside area maintains
the business districts of Downtown San Bernardino, Hospitality Business/Financial Centre,
University Town which are in San Bernardino and Downtown Riverside.\n\nQ: The Sand
Bernardino - Riverside area maintains what kind of district?\n\nA: business\n\nQ:
Other than San Bernardino, what is the name of the other city that maintains the
districts including University Town?\n\nA: Riverside\n\nQ: Other than Downtown San
Bernardino, and University Town, what is the name of another business district in the
San Bernardino-Riverside area?\n\nA: Hospitality Business/Financial Centre\n\Q: What
business districts does the San Bernardino area maintain?\n\nA: no answer\n\nQ: What
business districts does the Riverside area maintain?\n\nA: no answer
Table7: Prompttemplates(withexamples)oftheSFGdatasetsused. Theexpectedresponse(s)aremarkedingreen.
Notethatthesquaddatasetisnotstrictlyzero-shotasthepromptalreadycontainsseveralansweredquestionstothe
contextpassageleadinguptothetextquery–seeApp. B.1fordetailedexplanations.

### Dataset Prompttemplate

xsum Article: Upsetting events often make the news because they don’t happen very often.
\nThis section gives you some tips about what to do if you are feeling sad about
what you’ve seen, heard or read.\nYou can rely on Newsround to tell you the important
facts about a story - but some things you hear might be a bit scary or make you feel
worried.\nRemember that worrying stories are often in the news because they are rare -
they don’t happen very often.\nIt is incredibly unlikely that what you’re reading about
or watching might happen near you.\nDiscuss the stories with your parents or friends.
You’ll feel better that you’re not the only one worried. \nYou could also talk to
your teacher about it - maybe you could have a class discussion which would help you
understand the issue better.\nIf you’re having nightmares or trouble sleeping because
of something you’ve heard in the news: \n\ntl;dr: Some stories reported by Newsround
can make you feel sad - but you are not the only one and it’s OK to have those feelings.
wikilingua Article: The most commonly used classes of OTC pain medications include Acetaminophen
(Tylenol), and a class of drugs called "NSAIDs." NSAIDs stand for "nonsteroidal
anti-inflammatory drugs," and include medications such as Ibuprofen (Advil, Motrin),
and Naproxen sodium (Aleve). Aspirin is also technically an NSAID, although it more
frequently used in the prevention of heart attacks and strokes than it is in easing
chronic pain. [Omitted] This can lead to gastrointestinal bleeding and anemia. Special
care should be taken with those who drink alcohol. Always read the label of cold and
flu medications carefully to see what ingredients are present in the mixture. If you
need OTC drugs for more than 10 days, book an appointment with your physician to do a
more detailed assessment of your pain, and to look into alternative modes of treatment
that may be more effective (and also safer) for you moving forward. Also consult your
doctor if you have other health concerns, such as ongoing heart disease, kidney disease,
or liver disease, prior to using OTC medications for your pain.\n\ntl;dr: Be aware
of acceptable doses of OTC pain medications. Understand the risks of overusing OTC
drugs. Consult your doctor if you are unable to manage your pain without exceeding the
recommended daily dosage of OTC drugs.
Table8: Prompttemplates(withexamples)oftheLFGdatasetsused. Thereferencesummariesaremarkedinorange.
Wetriedvariouspromptstoelicitzero-shotsummarizationabilityinPaLMandfoundthat“\n\ntl;dr: ”works
thebest,likelybecauseitisacommonshorthandusedonlineforumswheremostofthePaLMpretrainingdatawere
obtained.

<!-- Page 19 -->

storycloze ’I love my job more than anything in the world. I work from home as a freelance
artist. I work in my sweatpants and get to draw and paint. People pay a lot of
money for my art and I am high in demand. I enjoy it so much, it doesn’t even feel
like work.
My friend got me a planter as a housewarming gift. It’s small and cute
and fits in nicely with my decor. But I’m still not sure where to put it. I hope
he doesn’t get sad. I’m sure I’ll figure out a place for it eventually.’
anlir3 ’Chinese<br>Sally bought a book from the library. She opened it to page 3. She
read the words but they didn’t make since to her. She looked at the cover. She got
a Chinese book by accident. question: Sally was able to read Chinese. Is it true,
false, or neither? answer: neither.
TORONTO, March 7 (Reuters) - The Canadian dollar weakened to a session low
against the greenback after data showed the domestic economy unexpectedly shed
jobs in February. At the same time, investors were also taking in data south of
the border that showed U.S. job growth accelerated last month. The Canadian dollar
was at C$1.1055 to the greenback, or 90.46 U.S. cents, weaker than Thursday’s
close of C$1.0992, or 90.98 U.S. cents. The loonie hit a session low of C$1.1064
shortly after the data was released. question: Toronto is the most populous city
in Canada. Is it true, false, or neither? answer: true.
A Girl Name Reagan<br>Tim was asked to show the new student around. He was
to wait in the school office for a student named Reagan. Waiting for the student
to arrive he wondered what they would be like. Tim assumed the person would be
tall like him and a boy. When the person finally arrived it was short girl dressed
all in blue. question: Tim assumed the person would be a girl. Is it true, false,
or neither? answer: false.’
natural_questions ’Q: when was rosencrantz and guildenstern are dead written A: 1966.
Q: where was the statue of liberty originally built A: france.
triviaqa_wiki Q: In the 2005 remake of the film ’King Kong’ who played the part of Ann Darrow,
originally played by Fay Wray? A: naomi watts.
Q: In which contact sport do two rikishi compete inside a dohyo ? A: sumo.’
wikilingua ’Article: In order to scan a QR code with your iPhone or iPad camera, you must first
update your iPhone or iPad to iOS 11 or later. Then open Settings . Tap the grey app
with gears on it. You’ll typically find this app on the Home Screen. Scroll down
and tap Camera. This option is about halfway down the Settings page. Tap the white
"Scan QR Codes" switch. It will turn green. Doing so will enabled your iPhone’s or
iPad’s camera’s QR code scanner. If the "Scan QR Codes" switch is already green,
your iPhone or iPad is ready to scan QR codes. Tap the Camera app icon, which
resembles a black camera on a grey background. You can also swipe up from the
bottom of the screen to open the Control Center and then tap the camera icon there.
The QR code should be centered in the middle of the iPhone or iPad screen, with no
edges or pieces off-screen. If your camera opens to the front-facing camera, first
tap the camera with arrows icon in the bottom-right corner of the screen. Once it
does, a grey notification that says something like "Open [website] in Safari" will
appear at the top of the screen. If the code contains a website URL, doing so will
open the QR code’s website in your iPhone’s or iPad’s Safari browser. tl;dr: 1.
Update to iOS 11 or later. 2. Open Settings. 3. Tap Camera. 4. Tap the white "Scan
QR Codes" switch. 5. Open the Camera app. 6. Center the QR code in the camera’s
view. 7. Tap the notification that appears at the top of the screen.’
Table9: Examplesofgeneratedpseudo-demosfromUSPonrepresentativetasks(PaLM-540B).Theresponseparts
ofthepseudo-demosarehighlighted: correctanswers;wronganswers;InLFGproblems,thereisnosingle,correct
answer. Weinsteadsimplyhighlightthesolutioninyellow.

## Tables

**Table (Page 1):**

| +4.4% |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  | +11.7% |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  | +33.0 |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 1):**

| +8.2% |  |  |  |  |  | 0 |  | -shot SP (Ours) |
|---|---|---|---|---|---|---|---|---|
|  |  | +15.7% U |  |  |  | U |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | +27.4 |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 7):**

| PaLM-62B |  |  |
|---|---|---|
| Zero-shot Auto- Random USP 0-shot CoT demo (Ours) | Few-shot 5-shot | Zero-shot Auto- Random USP 0-shot CoT demo (Ours) |
| 76.95 80.19 80.19 80.98 79.87 80.58 80.85 80.74 80.28 82.84 82.68 85.03 37.20 36.80 40.70 41.90 38.10 38.10 39.20 37.00 37.17 39.58 42.58 45.75 84.86 82.84 85.44 85.90 94.00 92.00 93.00 92.00 67.87 79.42 76.53 76.53 49.53 55.33 49.53 49.53 86.67 87.02 87.02 89.82 76.58 81.61 79.62 82.49 48.24 51.07 49.61 46.95 44.77 46.51 44.65 45.60 60.65 64.42 63.44 64.48 64.18 66.55 66.34 66.98 0.00 3.70 3.36 4.36 4.07 2.73 2.60 2.20 | 77.35 81.07 84.23 39.30 38.20 40.17 83.82 91.00 76.53 58.13 83.51 80.72 51.16 45.54 63.30 66.31 3.31 2.87 | 80.51 83.98 85.56 85.48 81.50 83.19 84.28 83.13 82.10 81.40 83.54 85.84 48.60 54.10 53.60 58.50 43.70 52.00 50.70 54.00 46.25 55.58 55.33 59.67 87.77 89.66 90.15 90.18 93.00 95.00 97.00 94.00 72.56 80.51 81.23 79.78 57.52 56.90 57.37 57.37 88.42 88.42 87.37 89.47 78.77 87.02 85.96 88.16 50.64 60.60 56.39 60.17 45.88 50.20 49.23 50.57 65.95 69.78 69.29 70.61 68.21 72.56 72.47 73.80 0.00 6.37 6.24 8.19 4.53 3.00 2.87 2.00 |


**Table (Page 8):**

| Setting Method | Zero-shot Auto- Random USP 0-shot CoT demo (Ours) |
|---|---|
| lambadaa web_questions natural_questions triviaqa_wiki squad∗ Average↑ Gainover0-shot(%) Averagerank↓c | 75.61/- 73.74/- 73.57/- 74.38/- 12.30/25.98 18.21/36.33 17.96/33.65 20.37/36.62 18.45/27.29 21.60/30.80 20.39/29.90 23.85/33.69 67.71/72.85 69.49/74.17 70.43/74.84 69.84/74.14 69.59/75.34 85.11/89.14 80.30/84.88 83.63/87.88 48.73/55.41b 53.63/60.84b 52.53/59.37b 54.41/61.34b 0.00/0.00b 10.05/9.79b 7.79/7.13b 11.66/10.70b 4.00 2.80 3.40 2.00 |
| lambadaa web_questions natural_questions triviaqa_wiki squad∗ Average↑ Gainover0-shot(%) Averagerank↓c | 78.71/- 77.70/- 76.13/- 75.01/- 10.33/23.60 16.04/31.76 20.47/36.55 25.64/43.31 20.49/31.04 29.31/39.36 29.00/39.34 32.19/43.56 76.73/81.85 78.73/84.05 80.52/84.89 80.10/84.57 75.67/80.85 90.93/94.37 88.47/92.93 90.29/94.06 52.39/59.21b 58.54/65.45b 58.92/65.97b 60.64/68.10b 0.00/0.00b 11.75/10.54b 12.47/11.41b 15.76/15.02b 4.00 2.80 3.20 2.60 |


**Table (Page 9):**

| Setting Method | Zero-shot Auto- Random USP 0-shot CoT demo (Ours) |
|---|---|
| xsum wikilingua(en) Average↑ Gainover0-shot(%) | 17.7/14.1/0.183 19.8/15.5/0.338 19.1/15.3/0.317 21.9/17.1/0.347 20.1/16.3/0.416 10.6/9.0/0.333 18.3/14.6/0.396 28.6/23.3/0.486 18.9/15.2/0.299 15.2/12.3/0.336 18.7/14.9/0.357 25.3/20.2/0.417 0.0/0.0/0.0 -19.5/-19.1/12.0 -1.0/-1.5/19.1 34.0/33.0/39.1 |
| xsum wikilingua(en) Average↑ Gainover0-shot(%) | 18.4/14.7/0.186 20.5/15.3/0.347 18.0/14.1/0.301 19.3/14.9/0.329 20.1/16.1/0.390 14.1/11.6/0.399 21.2/17.2/0.425 30.5/24.3/0.496 19.3/15.4/0.288 17.3/13.4/0.373 19.6/15.6/0.363 24.9/19.6/0.412 0.0/0.0/0.0 -10.3/-12.6/29.8 1.7/1.8/26.3 29.2/27.4/43.3 |


**Table (Page 9):**

|  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 9):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 9):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 9):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 9):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 9):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 9):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 9):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 15):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 19):**

| Up | date |  |  |  | to |  | iOS |  |  | 11 | or | later. |  |  | 2. | Open | Set | tings. | 3. Ta | p C | am | era. |  | 4 | . | Tap | the |  |  | white |  |  |  | "Scan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| QR |  | Codes" |  |  |  |  | switch |  |  |  | . 5. | Open |  |  | the | Cam | era | app. 6 | . Cen | ter | t | he | QR |  | code |  | in |  | the |  |  | cam |  | era’s |
| view. |  |  |  | 7. |  |  | Tap |  | the |  | not | ifi | ca | tion |  | that | ap | pears a | t the | top |  | of | the |  | screen. |  |  |  |  |  |  |  |  |  |


**Table (Page 19):**

|  | wron | gan |
|---|---|---|
| yel |  |  |
