---
title: "Boosted Prompt Ensembles LLMs"
original_file: "./23_Boosted_Prompt_Ensembles_LLMs.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["answer", "total", "she", "prompt", "page", "each", "time", "how", "number", "arxiv"]
summary: "<!-- Page 1 -->

Boosted Prompt Ensembles for Large Language Models
SilviuPitis MichaelR.Zhang AndrewWang JimmyBa

### UniversityofToronto,VectorInstitute

Abstract etal.,2022;Baietal.,2022).Inbothcases,weseekthehighestpossiblefewshotperformancefromthebasefoundation

### Methodssuchaschain-of-thoughtpromptingand

model(Lietal.,2022b;Wangetal.,2022b). Onewaytodo
self-consistencyhavepushedthefrontieroflanthisistocarefullyselecttheinitialfewshotsamples(and
guagemodelreasoningperformancewithnoaddich"
related_documents: []
---

# Boosted Prompt Ensembles LLMs

<!-- Page 1 -->

Boosted Prompt Ensembles for Large Language Models
SilviuPitis MichaelR.Zhang AndrewWang JimmyBa

### UniversityofToronto,VectorInstitute

Abstract etal.,2022;Baietal.,2022).Inbothcases,weseekthehighestpossiblefewshotperformancefromthebasefoundation

### Methodssuchaschain-of-thoughtpromptingand

model(Lietal.,2022b;Wangetal.,2022b). Onewaytodo
self-consistencyhavepushedthefrontieroflanthisistocarefullyselecttheinitialfewshotsamples(and
guagemodelreasoningperformancewithnoaddichainofthought,whereapplicable)foreachtargettask.This
tionaltraining. Tofurtherimproveperformance,
“promptengineering”canentailsubstantialmanualeffort
weproposeapromptensemblingmethodforlarge
foreachindividualtask,andthereisuncertaintyabouthow
languagemodels, whichusesasmalldatasetto
choicesimpactperformance(Zhouetal.,2022). Forexamconstructasetoffewshotpromptsthattogether
ple,onerecentworkrecommendspromptswiththe“longest
comprisea“boostedpromptensemble”. Thefew
questions”andmost“complexreasoning”(Fuetal.,2022)
shot examples for each prompt are chosen in a
whileanothersuggests“onlyconsideringshorterquestions
stepwisefashiontobe“hard”examplesonwhich
withshorterrationales”(Zhangetal.,2022). the previous step’s ensemble is uncertain. We
showthatthisoutperformssingle-promptoutput- Toimprovebaselineperformanceandreducethemanualefspaceensemblesandbaggedprompt-spaceensem- fortinvolvedinconstructingfewshotsamples,wepropose
blesontheGSM8kandAQuAdatasets,among anewtechnique,“boostedprompting,”whichleveragesa
others. Weproposebothtrain-timeandtest-time small dataset to construct a set of few shot prompts that
versionsofboostedpromptingthatusedifferent progressivelysolvemoreoftheproblems. Boostedpromptlevelsofavailableannotationandconductade- ing,inspiredbyclassicalboostingalgorithms(Freundetal.,
tailedempiricalstudyofouralgorithm. 1999),isastagewiseensemblemethodthatiterativelyadds
toasetofpromptssoastoimproveperformanceonproblemsjustoutsidethefrontierofwhatthemodelcancurrently
solve(Baranes&Oudeyer,2013). SeeFigure1foracon-

## Introduction

ceptual illustration. The final output of our algorithm is
When prompted with a few examples of a target behav- an accumulated set of LLM prompts with representation
ior,LargeLanguageModels(LLMs)areabletosolvean throughoutthedifficultpartsoftheproblemspace. Weproimpressive array of tasks, often with superhuman perfor- posebothtrain-time(inductive)andtest-time(transductive)
mance(Brownetal.,2020;Srivastavaetal.,2022). When versions of our algorithm. We show that the former can
theexamplesincludereasoningstepsleadingtotheanswer improveperformancewithasfewas100labeledtraining
(a“chainofthought”),e.g.,formulti-stepmathproblems, examples,andfindsomeevidencethatthelatterallowsthe
LLMsdemonstratesimilarstep-by-stepreasoningduring LLMtoadapttochangesintheproblemdistribution. The
inference,whichgreatlyimprovestheiraccuracy(Nyeetal., contributionsofourworkinclude:
2021;Weietal.,2022). Combinedwithoutputspaceen-

## A algorithm that constructs a boosted ensemble of

sembling,whereseveralchainsofthoughtaregeneratedfor
fewshotpromptsinastagewiseiterativeprocess. It
asingleprompt,thisachievesstrongperformanceonawide
is complementary to prior techniques for improving
arrayoftasks(Wangetal.,2022c).
reasoningperformance.
ThestrongbaselineperformanceofLLMsinthefewshot 2. Our proposed algorithm obtains strong results on
settingallowsthemtobeusednotonlyforimmediateper- AQUA,GSM8K,andotherchallengingdatasets,outformanceondownstreamtasks,butalsotogeneraterelevant, performingthestrongbaselineperformanceofsingle
highqualitydatasetsonwhichtheLLMsthemselvescanbe promptoutputspaceensembles(Wangetal.,2022c)
furthertrainedorfinetuned(Zelikmanetal.,2022;Huang andbaggedensembles(Lietal.,2022b).
Correspondenceto:SilviuPitis<spitis@cs.toronto.edu>. 3. Adetailedempiricalstudythatinvestigatesdifferent
annotationsettingsanddesignchoices.
3202
rpA
21
]LC.sc[
1v07950.4032:viXra

<!-- Page 2 -->

BoostedPromptEnsemblesforLargeLanguageModels
Complexity
elytS
tnemugrA

## Initial Prompt

prompt
correct
incorrect
Complexity
elytS
tnemugrA

## Select "Hard" Examples

prompt
hard
correct
incorrect
Complexity
elytS
tnemugrA

## Boosted Prompt Ensemble

prompt 1
prompt 2
correct
incorrect
Figure1.ConceptualDiagramofBoostedPrompting.Inthisdiagram(datacraftedforillustrativepurposes),weseetheintuitionof
boostedpromptinginasimplified2Dspace.Theoriginalpromptconsistsofexampleproblems((cid:70))andgeneralizestopartsofthetarget
·
problemspace( ),butfailsinothers(×).Ouralgorithmselectsthe“Hard”examples((cid:13))—overallincorrectexamplesforwhichthe
modelgeneratedatleastonecorrectsolution(outofseveralgenerationscombinedviaself-consistency(Wangetal.,2022c)).TheHard
examplesareusedtoformanewfew-shotprompt((cid:74)),whichisaddedtotheensemble,increasingoverallcoverageoftheproblemspace.
Whenappliedattraintime,theHardexamplestypicallylieoutsidethemodel’ssolutionfrontier,asdepicted,sincegroundtruthlabelsare
available.Whennolabelsareavailable,themodelusesitsowngeneratedlabelsandHardexamplesarerestrictedtolabelswithsufficient
confidence.

## PriorWork Automatic Prompt Engineering It has been observed

that language model performance can be sensitive to the
LargeLanguageModels Large,transformer-basedlanchosenprompt(Zhaoetal.,2021),whichhasledtoin-depth
guagemodels(LLMs)haveproventobeextremelycapable
studiesofpromptingmethodology(Liuetal.,2023;Wang
few shot learners in a wide variety of different contexts
etal.,2022a)andthedevelopmentofseveralapproachesto
(Vaswanietal.,2017;Brownetal.,2020). Theirgeneral
automaticpromptgeneration(Shinetal.,2020;Gaoetal.,
purposenaturehascreatedsomethingofa“paradigmshift”
2020). Whilesomeoftheseapproachesaregradient-based
intheAIlandscape, wherebymanydownstreamtasksre-
(Li&Liang,2021;Qin&Eisner,2021),requiringaccess
quiringlanguagewillmakeuseofanLLMasafoundation
tothemodelgradients,othersarebasedonsampling(Zhou
model,eitherdirectlyorbyfinetuning(Bommasanietal.,
et al., 2022) or elicited via a prompt-based algorithm (Li
2021). Ourworkconsidersoneapproachtoimprovingbaseetal.,2022a). Forpurposesofcollectingchainofthought
line, untuned LLM performance, which builds on and is
annotations,ahandfulofpastworkshaveconsideredselfcomplementarytoanumberofrecenttechniques.
generatingthechainofthought(Zhangetal.,2022;Huang
ChainofThought Weietal.(2022)showthatprompt- etal.,2022)andpossiblyvalidatingthemusingtheground
ingLLMswithintermediaryreasoningsteps,calledchain truthanswers(Zelikmanetal.,2022). Wedrawinspiration
ofthought(CoT)prompting,cansignificantlyincreasethe fromtheseworksandusemodelgeneratedchainsofthought
abilityoftheLLMtoperformcomplexityreasoningtasks. whenformingboostedprompts.

### Wangetal.(2022c)furtherimprovereasoningperformance

Example Selection Few shot performance can be imby introducing self-consistency (SC), which replaces the
provedbyretrievingrelevantexamplesfromalargedataset
standardgreedydecodingoftheLLMoutputwithastochas-
(Liuetal.,2021;Rubinetal.,2021),whichmayitselfby
ticoutputspaceensemblethatmarginalizesovermultiple
generatedbythelanguagemodelviaacarefullyguidedproreasoningpathsbysamplingwithpositivetemperature(e.g.,
cess(Lietal.,2022a). Forchainofthoughtprompting,it

### T =0.7)andchoosingthefinalpredictionp∗withhighest

hasbeenobservedthatrelevanceandcoherence(orderingof
agreement:
reasoningsteps)areimportantforperformance(Wangetal.,
(cid:88) 2022c) and further, that choosing examples that require
p∗ =argmax I(p =p)
p i i morereasoningstepscanimproveperformance(Fuetal.,
2022). Inourworkweusedisagreementamongensemble
Thisexploitsthefactthatdiversereasoningpathsthatlead
membersbothasaproxyforexampleinformativenessand,
tothesameansweraremorelikelytobecorrect. Ourwork
forthetest-timeversionofouralgorithm,asameasureof
buildsonself-consistencybyusingtheagreementamong
confidenceinthecorrectnessofthemodel’sprediction.
reasoningpathstodeterminethesetof“Hard”problemsand,
forthetest-timeversionofouralgorithm,thesetofLLM EnsembleMethods Ensemblesreliablyimproveperforgeneratedanswersthatarelikelytobecorrect. Thislatter manceinanumberofcontexts(Lakshminarayananetal.,
usageissimilartothatofHuangetal.(2022),whoshow 2017; Ganaie et al., 2022), including language modeling
that by finetuning LLMs on self generated answers with (Wangetal.,2022b). Boosting(Freundetal.,1999)itera-
“highagreement,”largelanguagemodelscanselfimprove.

<!-- Page 3 -->


### BoostedPromptEnsemblesforLargeLanguageModels

Algorithm1BoostedPrompting. WeassumeaccesstoalanguagemodelLLM thatgeneratesanswerswhenprompted
withfew-shotexamplespandquestionq. Ouralgorithmprogressivelygrowspreds,thesetofanswerstoeachquestion,
andgeneratespromptsconsistingofquestionsofintermediatedifficultyandtheiranswers.
functionBOOSTEDPROMPTING(modelLLM,initialpromptp, functionNEWPROMPT(T,preds,[answersA]):
problemsetT,itersn,num candidatesm,[answersA]): ifAthen (cid:46)train-timeboosting
preds←{q:[]forqinT} C←[qforqinTifA[q]inpreds[q]]
prompts←{p} else (cid:46)test-timeboosting
for in0...n−1do C←[qforqinTifthereis“sufficientagreement”for
forqinTdo themajoritypredictioninpreds[q]]
preds[q].append([LLM(p,q)for inrange(m)]) C←choose8ofthequestionsforwhichthemajority
p←NEWPROMPT(T,preds,[answersA]) predictioninpreds[q]hasminimalagreement
prompts.add(p) p←foreachquestionqinCchooseoneCoTfrom
returnprompts, preds preds[q]thatledtotheanswer/prediction
returnp
tivelyconstructsanensembletooptimizeperformanceon Howwedeterminecorrectnessdependsonthesetting,and
difficultexamples,andcanbeunderstoodasaformofcur- leadstotwodifferentinstancesofouralgorithm: train-time
riculumlearning(Bengioetal.,2009). Weadaptboosting boosting,forthecasewherethereisasmalllabeledtraining
totheprompt-basedLLMsettingbyforminganewprompt setorsomehuman-in-the-loopsupervisionavailable,and
of“Hard”examplesateachiteration. test-timeboosting,forthecasewherenosupervisionisavailableandthemodelmustrelysolelyonitsownpredictions.
Inaconcurrentwork,(Houetal.,2022)alsoadaptboosted

### BotharesummarizedinAlgorithm1(thedifferencebeing

ensembles to LLM classifiers. Their work focuses on a
whethertheoptionalargumentanswersAisprovided).
differentsettingthanours,inwhichclassificationisdone
viasingletokens,asopposedtoasolutionfollowingachain Theoutputofourtrain-timealgorithmisasetofprompts,
ofthought. Ratherthanchoosethepromptexamplessoas which are then applied to the test set. The output of our
toimproveperformance,Houetal.(2022)chooserandom test-timealgorithmisasetofpromptstogetherwithasetof
examplesforeachprompt,butchangetheweightingofthe testpredictions.
trainingexamplesasinclassicalboostingwhenoptimizing
Train-timeBoosting Inthiscase,weassumeaccesstoa
a“verbalizer”thatmapsmodeloutputstoclasses.
smalllabeleddataset,D =(T,A)=(q ,a )N ,where

### Train i i i=1

a arefinalanswerlabels(wedonotrequirechainofthought
i

## BoostedPromptEnsembles annotations,aswegeneratethechainofthoughtusingthe

model). Wealsoassumethereisaninitialpromptp ,which

### Our goal is to construct a set of few shot prompts for a 0

mayeithercontainmanuallyannotatedexamplesorbegenpretrained language model that work well together as an
eratedwithzeroshotchainofthought(Kojimaetal.,2022;
ensemble,inthesensethattheircombinedpredictionsdo
Zhangetal.,2022).
betterthanthepredictionsofasinglepromptoutputspace
ensemble (Wang et al., 2022c) or a multi-prompt bagged Ouralgorithmisappliedforniterations,startingwiththe
ensemble(Wangetal.,2022b;Lietal.,2022b). initial prompt set {p }. At the kth iteration we aim to
0
createanewpromptwhichgeneralizestoaregionofthe
Todothis,weadoptastagewiseapproachinspiredbyclassitarget problem space to which our previous prompt set
calboostingalgorithmsthatiterativelyaddsaninformative
{p ...p } performs poorly. To do this, we first samprompttoanexistingsetofprompts. Ateachiteration,a 0 k−1
pleasetofmcandidatereasoningpathsandanswersfor
new informative prompt is added, thereby expanding the
eachprobleminD usingthemostrecentprompt,andaprangeofproblemsthatthecurrentensemblesolves. Train
pendthemreasoningpathstothem(k−1)reasoningpaths
Asaproxyforinformativeness,weproposetousetheagree- thathavealreadybeensampledbytheboostedensemble.
mentbetweenseveralsolutionssampledfromthemodel. If
Then, motivated by curriculum learning, we form a new
allsolutionsagree,themodelalreadyknowshowtosolve
promptbyselectingcorrectreasoningpathsfromthoseprobthegivensample,anditisnotparticularlyinformative. On
lemsofintermediatedifficulty,wherethecurrentboosted
theotherhand,ifthereisdisagreementamongstthemodel’s
ensembleonlysometimesgetsthecorrectanswer. Specifsolutions,thenweassumethatthemodelisunsureabout
ically, we sort the problems where at least one reasoning
theexample, andthatincludingacorrectsolutionforthe
pathledtothecorrectanswerbythenumberofcorrectreaexampleinafewshotpromptwouldbeinformative.
soningpaths,andselect(problem,correctreasoningpath)

<!-- Page 4 -->


### BoostedPromptEnsemblesforLargeLanguageModels

pairs from amongst the hardest problems. Following Fu 4.Experiments
etal.(2022)’sdiscoverythatlongerreasoningpathsimprove
Weevaluatethesupervised(“traintimeboosting”)andselfin-contextreasoningperformance,foreachhardproblem
supervised / transductive (“test time boosting”) versions
chosen, wechoosefromthereasoningpathsthatledtoa
ofouralgorithmonaselectionofmoredifficultreasoning
correctanswerbyusingacomplexityheuristic,measuredby
benchmarkswithvaryingamountsofannotation. Boosted
thenumberofsentencesinreasoningpath(Fuetal.,2022).
prompting outperforms baselines on all five datasets we
Concatenatingthissetof(problem,correctreasoningpath)
evaluatedinourexperiments.
pairsformsanewprompt,whichweuseforthenextiteration of the algorithm, until we have a set of n prompts Ourexperimentsseektoanswerthefollowingquestions:
comprisingaboostedensemble.
• Do boosted prompt ensembles offer a performance
To perform inference at test time, we use our language advantageoversinglepromptandbaggedpromptenmodeltogeneratemchainofthoughtanswersforeachof sembles?
thenpromptinourboostedensemble,andtakeamajority • How does our method’s performance vary with the
voteoverthenmpredictions. Intuitively,eachpromptin amountofannotationavailable?
{p 0 ,...,p n−1 } covers a part of the target problem space. • Howsensitiveisboostingtotheinitialprompt?
Thosethatdonotcoverthetargetproblemspaceinwhich • Howdoesvaryingthenumberofensemblemembers/
the test question resides will lead the language model to samplesperensemblememberimpactresults?
failatansweringcorrectlyinlikelydifferentways, while • Howdoesthelevelof“sufficientagreement”fordeterprompts covering the target problem space in which the miningcorrectnessimpacttest-timeboosting?
testquestionresideswilllikelyanswercorrectly. Westudy • Can we further improve performance by applying
theeffectofvaryingnandmunderafixedcomputational weightstotheensemblemembers?
budgetintheexperiments. • Does choosing from the most complex generated
chainsofthoughtaidperformance?
Test-timeBoosting Intheabsenceoftraininglabels,our
• Does the choice of LLM model impact the relative
algorithm can be adapted to the transductive (where the
performanceofboostedprompting?
entireunlabeledtestsetisavailable;seeAlgorithm1)and
online(wheretestproblemscomeoneatatime;seeAlgo- Model Our primary experiments are carried out with
rithm 2 in Appendix B) settings. We call this “test-time thecode-davinci-002(“Codex”)modelviatheOpeboosting”. Inthiscase,wesubstitutegroundtruthanswer nAI API (Chen et al., 2021). As demonstrated by other
labelswithmodelpredictions,usingasimilarmotivationas papers(Wangetal.,2022b;Fuetal.,2022),performance
(Huangetal.,2022),wherebypredictionswith“sufficient trends between methods are consistent across models of
agreement”aretreatedascorrect. Thedefinitionofsuffi- similarsizes,andCodexisthehighestperformingmodelon
cientagreementisahyperparameter.Inourexperiments,we ourtesteddatasets,outperformingthelargerPaLM-540B
considersufficientagreementtobeachievedforquestionq (Chowdheryetal.,2022). WethankOpenAIforfreeaccess
withmostcommonpredictionp∗ifΣ p∈pred[q] I(p=p∗)/nm to this model as part of their beta program but note that,
ishigherthansomesufficientagreementhyperparameter∆. unfortunately,ithasbeendiscontinued. Wealsoverifythat
our results generalize to other models (text-davinci
The algorithm is otherwise the same as the train-time alandgpt-3.5-turbo). Wedescribeourimplementation
gorithm. Note that since agreement is also used to deterdetailsandlinktoourcodeintheappendix.
mine problem difficulty for prompt generation, a natural
tensionarises,andtest-timeboostingchooseseasiersam- Datasets Weconsiderthefollowingdatasets:
plesthanthetrain-timeversion. Forthisreason,onewould
• AQUA (Algebra QA with Rationales), a dataset of
notgenerallyexpecttest-timeboostingtoperformaswell
roughly 100,000 algebraic word problems and 254
astrain-timeboosting.
testquestions,whichissometimesreferredtoasthe
Test-time boosting has one notable advantage over train- MATHQAdatasetduetoafollow-upwork(Lingetal.,
timeboosting:incaseofdistributionshiftbetweentrainand 2017;Aminietal.,2019). Werandomlysample200
testsets,test-timeboostinghasanopportunitytoadaptto trainingproblemsforourlabeledtrainingset.
out-of-distributionproblemsbyincludingtheminitsprompt
• GSM8K(GradeSchoolMath8k),adatasetof1319
set. Intheory,thisallowsittodoaformofonline“prompt
mathematicalwordproblemscuratedbyhumanprobspace exploration”, whereby the boosted prompt adapts
lemwriters(Cobbeetal.,2021). Werandomlysample
tothecurrentproblemdistribution. Ourexperimentsfind
200trainingproblemsforourlabeledtrainingset.
someevidenceofthispossibility,butweleaveathorough
• MMLU570,astratifiedsubsampleoftheMassiveMulinvestigationtofuturework.
titaskLanguageUnderstanding(MMLU)datasetwith

<!-- Page 5 -->

BoostedPromptEnsemblesforLargeLanguageModels
Table1.ResultsTable:Codex.
Summary:Ateachlevelofannotation,boostedpromptingimprovesperformanceovertheself-consistencybaselineatthatsamelevelof
annotation.Withasmalltrainingset,boostedpromptingscoreshighestonalltesteddatasets.
Details: Resultsaregroupedbylevelofannotationused,withrowscorrespondingtoourmethodinlightgreen. Allbaselinesused
self-consistency.Sincewenoticedsomevarianceinresultsduetoself-consistency,weranmultipleseedsofcertainrows(showninthe
secondcolumn).Thesecondrowshowsthestandarddeviationofa3seedsamplemean,assumingallmethodshavethesamevariance.
Cellsmarkedwith“-”havenodataavailable.SeemaintextandAppendixAforimplementationdetails.
# Seeds AQUA GSM8K MMLU570 CMATH420 SVAMP
±0.58 ±0.27 ±0.40 ±0.34 ±0.15

### LargeDataset/Manual


## Lmsi(Palm540B) 1 - 82.1 - - -


### Minerva(PALM540B) 1 - 78.5 - - -


### Complexity+SC(reported) 1 58.6 82.6 - - -


### Complexity+SC(ourimplementation) 3 60.7 85.1 70.6 40.4 -

BoostedPromptingw/Complexity(ours) 3 61.2 85.6 70.1 40.0 -

### SmallTrainingSet


### DiVeRSeBagging(reported) 1 - 80 - - 87

Bagging(ourimplementation) 3 61.3 83.2 70.4 36.5 -
BoostedPrompting(ours) 3 63.4 85.2 71.2 38.7 -

### FewShotPrompt


### SC(reported) 1 52 78 - - 86.8


### SC(ourimplementation) 3 57.0 81.0 70.2 36.8 86.5

BoostedPrompting(ours) 3 61.7 83.3 68.1 39.0 88.6

### NoAnnotation(zeroshot)


### AutoCoT+SC 1 55.1 78.9 67.7 30.2 86.2

BoostedPromptingw/AutoCoT(ours) 1 57.1 82.3 68.1 29.8 86.6

### NonsenseAnnotation


### NonsensePrompt+SC 1 48 70.3 64.6 30 84.3


### BoostedPromptingw/Nonsense(ours) 1 54.7 79.7 66.8 35.7 86.8

570multiplechoicequestionscomposedof10ques- an ensemblein outputspace, bytaking the pluralityof n
tions sampled from each of the 57 MMLU subjects positivetemperaturegenerations.
(Hendrycksetal.,2020). Weusethe285(5x57)sam-
For alternative annotation settings (see next Section), we
pledevsetforourlabeledtrainingset.
combineself-consistencywithvariousapproachestochoos-
• CMATH420,astratifiedsubsampleofthechallenging
ing the few-shot prompt, including as baselines: (a) self-

### CompetitionMathdatasetwith12testsamplesfrom

consistencywithautoCoT(Zhangetal.,2022),whichbooteach of the 35 subject-level pairs (Hendrycks et al.,
strapsthemodel’sownzero-shotCoTtoformafew-shot
2021). Weuse71Level1Prealgebraproblemsfrom
prompt,(b)self-consistencywithcomplexityprompting(Fu
thetrainingset(allsuchproblemsthatmeetoursubetal.,2022),whichchoosesthefewshotexamplestousea
samplingcriteria)forourlabeledtrainingset.
maximalnumberofreasoningsteps,and(c)self-consistency
• SVAMP(SimpleVariationsonArithmeticMathword withbaggedprompts(Lietal.,2022b),whichchoosessev-
Problems),asetof1000algebraicwordproblemsde- eralfewshotpromptsatrandom. Theself-consistencyausignedtotestdifferentaspectsofreasoning(Pateletal., thors also considered bagged and random prompt order
2021). Wedonothavealabeledtrainingsetanddo ensembles, but found that neither had a noticeable effect
notdotrain-timeboostingforthisdataset. onresultsrelativetosingle-promptoutput-spaceensembles
(self-consistency)(Wangetal.,2022b).

### Baselines Our main baseline is self-consistency (SC)

(Wangetal.,2022c),whichusesasinglepromptandcreates Toensureafaircomparison,were-implementeachbaseline

<!-- Page 6 -->


### BoostedPromptEnsemblesforLargeLanguageModels

inourcodebase,whichusesslightlydifferentformattingand ortargetedmanualannotation. TheMinerva(Lewkowycz
answerandpredictionextractionforGSM8K(seeAppendix etal.,2022)andLMSI(Huangetal.,2022)baselinesfine-
A for details). In our implementation, we also extend all tune PALM 540B (Chowdhery et al., 2022). PALM has
baselinestouse100-pathself-consistency. Forthebaselines worse baseline performance than Codex, which explains
thatreportedresultswithself-consistency,wereportboth whyunfinetunedboostedpromptingoutperformsthesefinetheresultsfromtheoriginalworksaswellasthosefromour tuned baselines. Our method is compatible with finetunimplementation. ing (see gpt-3.5-turbo results below), and could be
used together with LMSI to further improve their self-

### Results annotations.

The main results are reported in Table 1, grouped by the At each level of annotation considered, boosted prompttypeofannotationusedbythemethod. Asself-consistency ing improves performance over the corresponding selfintroduces some stochasticity in small datasets, we aver- consistencybaseline. Weseethatboostedpromptingisable
ageresultsoverseveralseedsforbothourmethodandour totakeadvantageofthesmalltrainingsetwhenitisavailimplementations of the baselines (see table caption). All able, withthetrain-timeversiongenerallyoutperforming
ofourTable1resultsconsider100ensemblegenerations thetest-timeversion. TheoneexceptionisonCMATH420,
sampledat temperatureT= 0.7, whichcomes outto100 wherethetrainingsetisquitesmall(71)andthereissignifisinglepromptsamplesforself-consistency,andforbagging cantdistributionalshiftbetweentrainandtest.Thisprovides
andboosting,10samplesfromeachof10prompts. somesupportforthehypothesisthattest-timeboostingcan
doonline“promptspaceexploration”,althoughweleavea
Do boosted prompt ensembles offer a performance adthoroughinvestigationofthistofuturework.
vantageoversinglepromptandbaggedensembles?

### Howsensitiveisboostingtotheinitialprompt?


### Yes, in all cases, when a small training dataset (50-300

samples)isavailable, wefindthatboostingissuperiorto FromTable1,wenoticethatasthequalityoftheprompt
randomlybaggingfewshotexamplesaswellastosingle- deteriorates,fromtheoriginal,manuallyannotatedfewshot
promptself-consistency. Thedifferencetothelattercanbe setting,tothezeroshotsetting,tothenonsensesetting,so
quitelargeiftheinitialpromptissuboptimal,asobserved toodoestheperformanceofboostedprompting. ThisisunincaseofAQUA,wheretraintimeboostingobtains63.5% derstandable,becauseboostedpromptingusesthemodelto
as compared to the 57% obtained by single prompt self- provideselfsupervisedchainsofthoughtforallsubsequent
consistency. ensemblemembersandaworseinitialpromptmeansworse
selfsupervision. Theperformanceoftheoriginalpromptis

### How does our method’s performance vary with the

alsoadirectfactorsincewekeeptheoriginalpromptasone
amountofannotationavailable?
ofthetenensemblemembers.

### Weconsiderfourlevelsofannotation:


### How does varying the number of ensemble members /

• Smalltrainingset(50-300samples)withgroundtruth samplesperensemblememberimpactresults?
labels. See“Datasets”abovefordetails.

### InTable2,wereportresultsonAQUAwherewevarythe

• AfewshotCoTpromptof≤8examples. Inthiscase, numberofpromptsgeneratedandreasoningpathswetake
weusethepromptsfrompastworkwhereavailable,or fromeachpromptsuchthatthetotalcomputationalbudget
makeourown. SeeAppendixDforexactprompts. is fixed. We found the impact to be relatively small: all
• Norelevantannotation(zeroshot). FollowingZhang settingsoutperformbaggingandself-consistencybaselines.
et al. (2022), we assume access to the entire test set
(transductive setting) when forming predictions, but Table2.BoostedEnsembleComposition.Varyingtheensemble
notethatboostedpromptingcouldalsobeappliedon- compositionhasonlyminorperformanceimpact. Forasimilar
line. WeusetheAutoCoTmethod(Zhangetal.,2022) ablationre:baggedensemblecomposition,seeLietal.(2022b),
toformafewshotpromptbyapplyingzeroshotCoT Table4.Weuse3seedsfor10x10 . and1seedfortheothersettings.
(Kojimaetal.,2022)toasamplefromthetestset. This
nxm 10x10 20x5 33x3 50x2
approach has been validated by Huang et al. (2022),
so we do not also consider a direct zero shot + SC AQUA 63.4 62.6 63.0 62.6
baseline.
• Apseudo-adversarialcase,wherethesamenonsense
twoshotpromptisprovidedforalldatasets. How does the level of “sufficient agreement” for determiningcorrectnessimpacttest-timeboosting?
Wealsolistfourbaselinesthatrequirealargertrainingset
Intheabsenceoftraininglabels,ouralgorithmsubstitutes

<!-- Page 7 -->

BoostedPromptEnsemblesforLargeLanguageModels
Table3.ResultsTable:Curie/Davinci/GPT-3.5.
Summary:BoostedpromptingimprovesuponbaselinesforthemorecapableDavinciandGPT-3.5models.OnthelesscapableCurie
model,boostedpromptingdoesnotappeartohelp.
Details:Eachresultinthistableconsiders40ensemblegenerationssampledattemperatureT=0.7(4samplesfromeachof10prompts
inthecaseofbaggingandboosting).Eachresultisasingleseed.
text-curie-001 text-davinci-003 gpt-3.5-turbo

## Aqua Gsm8K Aqua Gsm8K Aqua Gsm8K


### SmallTrainingSet

Bagging(ourimplementation) 18.5 3.0 53.9 69.9 75.2 87.7
BoostedPrompting(ours) 14.2 3.2 55.9 71.7 76.4 88.2

### FewShotPrompt


### SC(ourimplementation) 18.1 3.9 53.1 69.6 72.0 86.7

BoostedPrompting(ours) 13.0 3.1 55.1 71.6 72.8 87.1
groundtruthanswerlabelswithmodelpredictions,using
asimilarmotivationas(Huangetal.,2022),wherebypredictionswith“sufficientagreement”aretreatedascorrect.
Thereisaninherenttradeoff: settingsufficientagreement
highermeansthepredictionsaremorelikelycorrect,butthe
selectedproblemsmaybelessusefulasaprompt,sincethe
modelalreadyknowshowtosolvetheseproblems. Figure2
showstheAQUAperformanceandaveragepromptaccuracy
aswevarytheminimumagreementhyperparameter,which
indicatesthethresholdatwhichweconsidermodelgener-
64
62
60
58
56
54
52
50
0.3 0.4 0.5 0.6 0.7 0.8 0.9
Minimum Agreement Deemed "Suitable"
ecnamrofreP

## Auqa

Suitable Agreement Ablation
0.9
0.8
0.7
0.6
0.5
0.4
0.3

### AQUA Performance

Average Prompt Accuracy 0.2
ycaruccA
tpmorP
egarevA
ated answers to be correct. Setting minimum agreement
toolowgreatlyreducesaveragepromptaccuracy,sincewe
might form prompts by choosing questions and answers
pairs the model believes to be correct but are in fact not.
Thiscanthenleadtoadecreaseintest-timeperformance,as
theboostedpromptsmaycontainmoreincorrectexamples.
Can we further improve performance by applying
weightstotheensemblemembers?

### Classicalboostingappliesweightstotheensemblemembers

(Freundetal.,1999). Thoughlackinginmathematicalmotivation,weconsiderapplyingweightstoboostedprompt
ensemblesviatheK-classAdaboostformulafromHastie
etal.(2009):
w =log[(1−err )/err ]+log(K−1)
i i i
exceptthatwereplacelog(K−1)withanon-negativeparametricoffsetthatweoptimizeoverusingthetrainingset.
The results are shown in Table 4. We find the overall resultsunremarkableandreminiscentoftheweightingresults
of Wang et al. (2022c), who found that weighted voting
providedlittleadvantageoverasimpleaverage.
Table4.WeightedBoosting. 3seedseach. Applyingweightsto
theboostedensemblehasonlyminorperformanceimpact.
Unweighted Weighted

## Gsm8K 85.2 85.5


## Aqua 63.4 63.8


## Mmlu570 71.2 70.7


## Cmath420 38.7 38.4


### Figure2.Suitable Agreement for Test-Time Boosting. The

levelofsuitableagreementrequiredformodelgeneratedanswers
tobedeemed“correct”,forpurposesofnewpromptformation,
cangreatlyreducetheperformanceoftest-timeboostingifitistoo Doeschoosingfromthemostcomplexgeneratedchains
low.Inourmainresultsweusearelativelyhighvalueof0.8for ofthoughtaidperformance?
multiplechoicedatasets(AQUAandMMLU570)andavalueof

### Whenformingboostedprompts,theCoTischosenfromthe

0.7foropen-endeddatasets.WeusedoneseedonAQUAtostudy
severalmodelsamplesthatledtothecorrect(ormajority)
theeffectofthishyperparameter.

<!-- Page 8 -->


### BoostedPromptEnsemblesforLargeLanguageModels

answer.FollowingFuetal.(2022),wesamplefromamongst

### Evolution of First Five Boosted

the5mostcomplex,whichwedeterminebythecombined Prompt Embeddings on GSM8K
numberof“\n”and“. ” substrings. Table5suggestthat
thischoiceimprovesperformance.
40

### Table5.Choosing Complex vs Random CoTs. Sampling

randomly from model-generated CoTs (1 seed), instead of 20
sampling from amongst the most complex CoTs (3 seeds),
performsslightlyworse,butstill . betterthanbaselines. 0
ComplexCoT RandomCoT
20

### AQUA(train-time) 63.4 62.2


### AQUA(test-time) 61.7 60.2 40

HowdoesthechoiceofbaseLLMmodelimpactrelative
40 20 0 20 40
performance?
Table3containstheresultsofasubsetoftheexperiments Figure3.t-SNEVisualizationofembeddingson(question,reasonfromTable1onthreeothermodels: text-curie-001, ing)tuplesonGSM8Kdataset.Theembeddingsofthetestsetare
which is smaller than code-davinci-002; scatteredasfadedbluedots. Thepromptsareshownwithstars.
text-davinci-003 model, which is the same Theblackstarsaretheinitialprompt,andthenextfourpromptsare
showninred,orange,yellow,andwhite,respectively. Although
size;andgpt-3.5-turbo,whichisaneffectivemodel
theinitialpromptisbiasedtowardtheupperleftside,laterprompts
of unknown size that been finetuned on related data.
explorethespace,sothattheensemblehasgoodcoverageoverall.
We see that boosted prompting is similarly effective for
strongerdavinciandgpt-3.5models,butnotforthe
andperformtest-timeadaptationviaonlinepromptspace
weaker curie model. We hypothesize this is because a exploration. Thoughweprovidedsomeempiricalevidence
minimal level of accuracy is needed to self-generate the ofthis,weleaveathoroughinvestigationofthistofuture
boostedprompts(seeFigure2, whichshowsanearly1:1 work. Weobservedinourexperimentsthattheperformance
correlationbetweenaveragepromptaccuracyandAQUA oftest-timeboostingisstronglycorrelatedwithpromptacperformance). curacy. To further improve the effectiveness of test-time
boosting and allow for prompt space exploration, future
4.2.t-SNEvisualization workmayconsiderbetteroptionsforverifyingpromptaccuracy,suchastheuseofaverifier(Cobbeetal.,2021;Li
In Figure 3, we show a visualization of the first five
etal.,2022b),ordebate(Irvingetal.,2018).
boosted prompts found by our train-time algorithm on
the 1319 question GSM8K test set. We used OpenAI’s
text-embedding-ada-002 model to generate 1536- Acknowledgements
dimensionalembeddingsfor(question,reasoning)tupleson

### WethankHarrisChan,KeiranPaster,andYongchaoZhou

the test set and the prompts (from the training set) found
forhelpfulcommentsanddiscussions. WethankOpenAI
by our algorithm. After applying t-SNE, we see that the
foraccesstotheCodexmodelaspartoftheirbetaprogram.
coverageofboostedpromptsetgrowstocoverthespace.
Resourcesusedinpreparingthisresearchwereprovided,in
part,bytheProvinceofOntario,theGovernmentofCanada,

## Conclusion

andcompaniessponsoringtheVectorInstitute.

### Inthispaper,weadaptedclassicalboostingtothelanguage

modelsettingandproposedafewshotboostedprompten- References
semblingalgorithm. Onseveralreasoningbenchmarks,we
Amini,A.,Gabriel,S.,Lin,P.,Koncel-Kedziorski,R.,Choi,
showedthatboostedpromptensemblesoutperformsingle
Y.,andHajishirzi,H.Mathqa:Towardsinterpretablemath
promptandbaggedensembles,especiallywhentheinitial
wordproblemsolvingwithoperation-basedformalisms.
promptissuboptimal.
arXivpreprintarXiv:1905.13319,2019.
Weproposedtwovariantsofthealgorithm,atrain-timealgorithm that uses training labels to select Hard problems Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J.,
and a test-time version that substitutes labels with model Jones,A.,Chen,A.,Goldie,A.,Mirhoseini,A.,McKinpredictions. We hypothesized that our test-time boosting non, C., etal. Constitutionalai: Harmlessnessfromai
algorithmcanfunctionasaformofself-guidedcurriculum feedback. arXivpreprintarXiv:2212.08073,2022.

<!-- Page 9 -->


### BoostedPromptEnsemblesforLargeLanguageModels

Baranes,A.andOudeyer,P.-Y. Activelearningofinverse Hendrycks,D.,Burns,C.,Kadavath,S.,Arora,A.,Basart,
modelswithintrinsicallymotivatedgoalexplorationin S.,Tang,E.,Song,D.,andSteinhardt,J.Measuringmathrobots. RoboticsandAutonomousSystems,61(1):49–73, ematicalproblemsolvingwiththemathdataset. NeurIPS,
2013. 2021.
Bengio, Y., Louradour, J., Collobert, R., and Weston, J. Hou,B.,O’Connor,J.,Andreas,J.,Chang,S.,andZhang,
Curriculumlearning. InProceedingsofthe26thannual Y. Promptboosting: Black-boxtextclassificationwithten
internationalconferenceonmachinelearning,pp.41–48, forwardpasses. arXivpreprintarXiv:2212.09257,2022.
2009.

### Huang,J.,Gu,S.S.,Hou,L.,Wu,Y.,Wang,X.,Yu,H.,and

Bommasani, R., Hudson, D. A., Adeli, E., Altman, R.,

### Han,J. Largelanguagemodelscanself-improve. arXiv

Arora,S.,vonArx,S.,Bernstein,M.S.,Bohg,J.,BossepreprintarXiv:2210.11610,2022.
lut,A.,Brunskill,E.,etal. Ontheopportunitiesandrisks
offoundationmodels. arXivpreprintarXiv:2108.07258,
Irving, G., Christiano, P., and Amodei, D. Ai safety via
2021.
debate. arXivpreprintarXiv:1805.00899,2018.
Brown,T.,Mann,B.,Ryder,N.,Subbiah,M.,Kaplan,J.D.,

### Kojima,T.,Gu,S.S.,Reid,M.,Matsuo,Y.,andIwasawa,

Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G.,
Y. Largelanguagemodelsarezero-shotreasoners. arXiv
Askell,A.,etal. Languagemodelsarefew-shotlearners.
preprintarXiv:2205.11916,2022.
Advancesinneuralinformationprocessingsystems,33:
1877–1901,2020.

### Lakshminarayanan,B.,Pritzel,A.,andBlundell,C. Simple

Chen,M.,Tworek,J.,Jun,H.,Yuan,Q.,Pinto,H.P.d.O., andscalablepredictiveuncertaintyestimationusingdeep
Kaplan,J.,Edwards,H.,Burda,Y.,Joseph,N.,Brockman, ensembles. Advancesinneuralinformationprocessing
G., etal. Evaluatinglargelanguagemodelstrainedon systems,30,2017.
code. arXivpreprintarXiv:2107.03374,2021.

### Lewkowycz, A., Andreassen, A., Dohan, D., Dyer, E.,

Chowdhery,A.,Narang,S.,Devlin,J.,Bosma,M.,Mishra, Michalewski, H., Ramasesh, V., Slone, A., Anil, C.,
G., Roberts, A., Barham, P., Chung, H.W., Sutton, C., Schlag,I.,Gutman-Solo,T.,etal. Solvingquantitative
Gehrmann,S.,etal. Palm: Scalinglanguagemodeling reasoningproblemswithlanguagemodels.arXivpreprint
withpathways. arXivpreprintarXiv:2204.02311,2022. arXiv:2206.14858,2022.

### Cobbe,K.,Kosaraju,V.,Bavarian,M.,Chen,M.,Jun,H.,

Li, J., Zhang, Z., and Zhao, H. Self-prompting large

### Kaiser,L.,Plappert,M.,Tworek,J.,Hilton,J.,Nakano,

language models for open-domain qa. arXiv preprint
R.,etal. Trainingverifierstosolvemathwordproblems.
arXiv:2212.08635,2022a.
arXivpreprintarXiv:2110.14168,2021.

### Li,X.L.andLiang,P.Prefix-tuning:Optimizingcontinuous

Freund, Y., Schapire, R., and Abe, N. A short introducpromptsforgeneration.arXivpreprintarXiv:2101.00190,
tiontoboosting. Journal-JapaneseSocietyForArtificial
2021.
Intelligence,14(771-780):1612,1999.
Fu, Y., Peng, H., Sabharwal, A., Clark, P., and Khot, T. Li, Y., Lin, Z., Zhang, S., Fu, Q., Chen, B., Lou, J.-G.,
Complexity-based prompting for multi-step reasoning. andChen,W. OntheadvanceofmakinglanguagemodarXivpreprintarXiv:2210.00720,2022. els better reasoners. arXiv preprint arXiv:2206.02336,
2022b.
Ganaie,M.A.,Hu,M.,Malik,A.,Tanveer,M.,andSuganthan,P. Ensembledeeplearning: Areview. Engineering Ling, W., Yogatama, D., Dyer, C., and Blunsom, P. Pro-
ApplicationsofArtificialIntelligence,115:105151,2022. graminductionbyrationalegeneration:Learningtosolve
and explain algebraic word problems. arXiv preprint
Gao,T.,Fisch,A.,andChen,D. Makingpre-trainedlanarXiv:1705.04146,2017.
guage models better few-shot learners. arXiv preprint
arXiv:2012.15723,2020.

### Liu,J.,Shen,D.,Zhang,Y.,Dolan,B.,Carin,L.,andChen,

Hastie, T., Rosset, S., Zhu, J., and Zou, H. Multi-class W. What makes good in-context examples for gpt-3?
adaboost. StatisticsanditsInterface,2(3):349–360,2009. arXivpreprintarXiv:2101.06804,2021.
Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, Liu,P.,Yuan,W.,Fu,J.,Jiang,Z.,Hayashi,H.,andNeubig,
M., Song, D., and Steinhardt, J. Measuring mas- G. Pre-train,prompt,andpredict: Asystematicsurveyof
sive multitask language understanding. arXiv preprint promptingmethodsinnaturallanguageprocessing. ACM
arXiv:2009.03300,2020. ComputingSurveys,55(9):1–35,2023.

<!-- Page 10 -->


### BoostedPromptEnsemblesforLargeLanguageModels

Nye,M.,Andreassen,A.J.,Gur-Ari,G.,Michalewski,H., Zhang, Z., Zhang, A., Li, M., and Smola, A. Automatic
Austin,J.,Bieber,D.,Dohan,D.,Lewkowycz,A.,Bosma, chain of thought prompting in large language models.
M., Luan, D., et al. Show your work: Scratchpads for arXivpreprintarXiv:2210.03493,2022.
intermediatecomputationwithlanguagemodels. arXiv
Zhao, Z., Wallace, E., Feng, S., Klein, D., and Singh, S.
preprintarXiv:2112.00114,2021.

### Calibratebeforeuse: Improvingfew-shotperformance

Patel,A.,Bhattamishra,S.,andGoyal,N. Arenlpmodels of language models. In International Conference on
reallyabletosolvesimplemathwordproblems? arXiv MachineLearning,pp.12697–12706.PMLR,2021.
preprintarXiv:2103.07191,2021.
Zhou, Y., Muresanu, A. I., Han, Z., Paster, K., Pitis, S.,

### Chan,H.,andBa,J. Largelanguagemodelsarehuman-

Qin, G. and Eisner, J. Learning how to ask: Querylevelpromptengineers.arXivpreprintarXiv:2211.01910,
ing lms with mixtures of soft prompts. arXiv preprint
2022.
arXiv:2104.06599,2021.
Rubin, O., Herzig, J., and Berant, J. Learning to retrieve prompts for in-context learning. arXiv preprint
arXiv:2112.08633,2021.

### Shin, T., Razeghi, Y., Logan IV, R. L., Wallace, E., and

Singh, S. Autoprompt: Eliciting knowledge from language models with automatically generated prompts.
arXivpreprintarXiv:2010.15980,2020.

### Srivastava,A.,Rastogi,A.,Rao,A.,Shoeb,A.A.M.,Abid,


### A., Fisch, A., Brown, A. R., Santoro, A., Gupta, A.,

Garriga-Alonso, A., et al. Beyond the imitation game:
Quantifyingandextrapolatingthecapabilitiesoflanguage
models. arXivpreprintarXiv:2206.04615,2022.

### Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,

L., Gomez, A. N., Kaiser, Ł., and Polosukhin, I. Attentionisallyouneed. Advancesinneuralinformation
processingsystems,30,2017.
Wang,B.,Min,S.,Deng,X.,Shen,J.,Wu,Y.,Zettlemoyer,
L.,andSun,H. Towardsunderstandingchain-of-thought
prompting: Anempiricalstudyofwhatmatters. arXiv
preprintarXiv:2212.10001,2022a.
Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., and
Zhou,D. Rationale-augmentedensemblesinlanguage
models. arXivpreprintarXiv:2207.00747,2022b.
Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E.,
and Zhou, D. Self-consistency improves chain of
thought reasoning in language models. arXiv preprint
arXiv:2203.11171,2022c.

### Wei, J., Wang, X., Schuurmans, D., Bosma, M., Chi, E.,

Le,Q.,andZhou,D. Chainofthoughtpromptingelicitsreasoninginlargelanguagemodels. arXivpreprint
arXiv:2201.11903,2022.
Zelikman, E., Wu, Y., and Goodman, N. D. Star: Bootstrapping reasoning with reasoning. arXiv preprint
arXiv:2203.14465,2022.

<!-- Page 11 -->

BoostedPromptEnsemblesforLargeLanguageModels

### A.ImplementationDetails

We use certain functions from the existing implementations of Kojima et al. (2022) (available at https://github.
com/kojima-takeshi188/zero_shot_cot)andWangetal.(2022c)(availableviatheirICLRsupplement),but
largely build out our own implementation, which we have made available at https://github.com/awwang10/
llmpromptboosting.
OurresultsonGSM8Kdifferslightlyfrompastworkduetoaminorchangeinanswer/predictionextractionandformatting:
• GSM8K:Weapplytheanswercleansingfunctiontotheanswers,whereaspastworkapplieditonlytotheprediction.
Wedidthisafternoticingthatsometimesanswercleansingonthepredictionwouldchangewhatshouldhavebeena
correctanswer(e.g.,“200,000”)toadifferentformat(e.g.,“200000”)afterwhichitwascountedasincorrect. This
changeimprovesresultsby0.6-0.9%:
GSM8Kresultsw/ocleaninganswers

### Bagging 82.4(-0.6)

TrainTimeBoosting 84.3(-0.9)
TestTimeBoosting 82.5(-0.8)

### SelfConsistency 80.2(-0.8)

Weuse100-shotself-consistencyforallimplementations. Aswenoticedsomevariance,especiallyinAQUAresults(dueto
arelativelysmalltestsetof254samples),weranmultipleseedsofthemainresultsandbaselines,asshowninTable1.
Tochoosewhichquestionstouseforbaggedprompts,wesamplerandomlywithreplacementfromthetrainingset.
Tochoosewhichquestionstouseforboostedprompts,wesortthe“suitable”question/answerpairsinascendingorderof
agreementwithrespecttothedesiredanswer(thecorrectanswerforthetrain-timealgorithm,orthemajorityanswerforthe
test-timealgorithm),andsample8questionsfromthe24suitablequestion/answerpairswithlowestagreement(wespeculate
thatsomerandomnesshelps,soastonotrepeatpromptsifnothingchangesbetweeniterations,butwedidnotspecifically
ablateourchoiceof“24”). “Suitable”isdefinedashavingatleast1correctgenerationforthetrain-timealgorithm,and
havingatleast“minimumagreement”agreementwithrespecttothepredictedanswerattest-time. Ourtest-timeboosting
usesaminimumagreementof0.7foropen-endeddatasets(GSM8K,CMATH420,SVAMP),andaslightlyhigherminimum
agreementof0.8formultiplechoicedatasets(AQUA,MMLU570)becausetheanswerdistributionhaslowerentropy. The
initialvalue(andthealgorithmgenerally)wasdevelopedona300questionsubsetoftheGSM8Ktrainingset, butnot
extensivelytuned.
Havingselectedwhichquestionsandanswerstouseforourboosted(orbagged)prompts,weselectthechainofthought
fromthemodel-generatedchainsofthoughtbysamplingitrandomlyfromthe5mostcomplexchainofthoughtsthatledto
thedesiredanswer(onceagain,wespeciulatethatsomerandomnesshelps,butwedidnotspecificiallyablateourchoiceof
“5”). Forthispurpose,complexitywasmeasuredas:
len(cot.replace(’\n’,’. ’).split(’. ’))
Toreducecomputationalcomplexityattest-time,wemoveallpredictionsthathavemetthebarfor“suitableagreement”to
a“solvedset”,andconsidertheirpredictionsfinal. Weonlycontinuetogeneratepredictionswithnewerpromptsonthe
remainingunsolvedquestions. Whendoingtest-timeboostingonGSM8Kwithasuitableagreementparameterof0.7,the
unsolvedsetisonly280samplesoftheoriginal1319. Thus,thetotalnumberofgenerationsrequiredismuchsmallerthan
100*1319. ThebreakdownofperformanceonGSM8Katthe10thsuchiterationofthefirstseedis:
Count Agreement Performance

### Unsolved 280 27% 46%

“Solved” 1039 83% 92%

### Overall 1319 71% 83%

Whenapplyingboostedensembleslearnedattraintimetothetestdataset,weuseasuitableagreementparameterof0.9for

<!-- Page 12 -->


### BoostedPromptEnsemblesforLargeLanguageModels

alldatasets. Thisshouldnotinfluencefinalpredictionsmuch,whilestillsavingnon-negligiblecomputation. Thebreakdown
ofperformanceonGSM8Katthe10thsuchiterationofthefirstseedis:
Count Agreement Performance
Unsolved 593 38% 72%
“Solved” 726 94% 96%

### Overall 1319 69% 85%

ThesamplemeanstandarddeviationsshowninTable1arebasedonthe12seedsfromBagging,BoostedPrompting(Small
TrainingSet),SelfConsistency,andBoostedPrompting(FewShotPrompt),byassumingthatallmethodshavethesame
√
variance. Wefirstcomputethesamplestandarddeviationusing12samplesofx−xˆ,andthendivideby 3toestimatethe
standarddeviationofthe3seedsamplemean.

### B.OnlineBoostedPrompting

WecanrunBoostedPromptingonlinebyaddingtooursetofpromptswheneveranewdiversepromptbecomesavailable.
Forthefirstfewquestions,therewillonlybeoneprompt,andBoostedPromptingwillbeidenticaltoSelfConsistency. Once
afewquestionshavebeenansweredwithsufficientagreement,anewpromptcanbeaddedtotheensembleandapplied
goingforward. ThismodifiedalgorithmisshowninAlgorithm2.
Algorithm2BoostedPrompting(Online). The BOOSTEDPROMPTING functionismeanttobecalledeachtimeanew
problemorbatchofproblemsisaddedtoT. Pastpredictionsarecachedviapastp,andm/nareadjustedautomatically.
function BOOSTEDPROMPTING(model LLM, prompt set functionNEWPROMPT(T,preds):
prompts, past predictions pastp, cumulative problem set C←[qforqinTifthereis“sufficientagreement”for

### T,totalgenerationsN): themajoritypredictioninpreds[q]]

preds←{q:pastp[q]forqinT}#[]ifqisnew C←choose8ofthequestionsforwhichthemajority
n,m←len(prompts),N/m predictioninpreds[q]hasminimalagreement,
for inrange(n)do ifcannot,returnNone
forqinTdo p←foreachquestionqinCchooseoneCoTfrom
for inrange(m)iflen(preds[q])<Ndo preds[q]thatledtotheanswer/prediction
preds[q].append([LLM(p,q)]) (cid:46)futurework:ensurenewpromptissufficientlydifferent
p←NEWPROMPT(T,preds) frompastprompts,and/orremoveoldpromptsthataren’t
# evaluatestoTrueifnewpromptisgenerated diverseenough
ifpthen returnp
prompts.add(p)
n,m←len(prompts),N/m
returnprompts, preds

### C.Furtherresults


### C.1.Qualitativeexampledifficulty

We investigate whether a measure of example difficulty can be identified via our ensemble of prompts and multiple
generations for each prompt on AQUA. At test-time, we compute the empirical distribution over answer choices from
running ten rounds of our algorithm (with ten generated responses at each iteration). Responses with no answers are
removed. Wethensortedtheproblemsbytheprobabilityassignedtotheoptionthemodelismostconfidentandreportthe
5mostextremeprobabilitiesandtheircorrespondingquestionsinTable6andTable7. Qualitatively,questionswithlow
confidenceappeartobemorechallenging,ambiguous,orcontainspellingerrors. Theoppositeistrueforquestionswith
highconfidence.

### C.2.t-SNEVisualizationonAQUA

InFigure4,weshowavisualizationofthepromptsfoundbyouralgorithmonthe200questionAQUAtrainingset. We
usedOpenAI’s“text-embedding-ada-002,”togenerate1536-dimensionalembeddingsfor(question,reasoning)tupleson

<!-- Page 13 -->


### BoostedPromptEnsemblesforLargeLanguageModels

Table6. Testquestionswherethemodelisleastconfident.Questionstendtobemorechallenging,ambiguous,orcontainspellingerrors.
Maxprobabilityiscomputedbytheempiricaldistributionfromrunningtenroundsofouralgorithm(withtengeneratedresponsesateach
iteration).Wecopythequestionsverbatimhere(includingtypos).
QUESTION: Ofthethree-digitintegersgreaterthan700,howmanyhavetwodigitsTthatareequaltoeachotherandthe
remainingdigitdifferentfromtheothertwo?

## Answers: [’A)90’,’B)82’,’C)80’,’D)45’,’E)36’]


## Maxprobability: 0.255

QUESTION: WhatannualpaymentdischargeadebitofRs.12900,duein4yrs.At5%rate?

## Answers: [’A)2000’,’B)1300’,’C)3000’,’D)4300’,’E)4500’]


## Maxprobability: 0.255


## Question: 81,162,49,98,25,50,55


## Answers: [’A)110’,’B)127’,’C)129’,’D)128’,’E)131’]


## Maxprobability: 0.255

QUESTION: Twodicearethrowntogether.Whatistheprobabilitythatthesumofthenumberonthetwofacesisdivided
by4or6

## Answers: [’A)5/7’,’B)3/4’,’C)7/18’,’D)5/17’,’E)7/9’]


## Maxprobability: 0.258

QUESTION: TheCoenfamilyconsistsofafather,amother,twochildrenandadog. Aphotographerisabouttotakethe
family’spicture. Howmanydifferentarrangements(ofstandinginarow)doesthephotographerhave,ifitisknownthatthe
fatherinsistsofstandingbyhiswoman,asthesongsays?

## Answers: [’A)12’,’B)24’,’C)48’,’D)60’,’E)120’]


## Maxprobability: 0.260

thetrainingsetandthepromptsfoundbyouralgorithm. Afterapplyingt-SNE,weseethattheboostedpromptsachieve
coverageoverthespaceandaretypicallyfoundnearincorrectquestions.

<!-- Page 14 -->


### BoostedPromptEnsemblesforLargeLanguageModels

Table7. Testquestionswherethemodelismostconfident.Maxprobabilityiscomputedbytheempiricaldistributionfromrunningten
roundsofouralgorithm(withtengeneratedresponsesateachiteration).Wecopythequestionsverbatimhere(includingtypos).

## Question: 200+8×4=?

ANSWERS: [’A)232’,’B)202’,’C)420’,’D)209’,’E)Noneofthese’]

## Maxprobability: 0.917

QUESTION: Thepriceofabookisincreasedfrom300to330. Whatisthe%ofincreaseinitsprice?

## Answers: [’A)10%’,’B)20%’,’C)40%’,’D)50%’,’E)60%’]


## Maxprobability: 0.919

QUESTION: Whatistheproductofalltheprimefactorsof13?

## Answers: [’A)12’,’B)11’,’C)13’,’D)15’,’E)18’]


## Maxprobability: 0.930

QUESTION: TwobrotherXandYappearedforanexam. TheprobabilityofselectionofXis1/5andthatofBis2/3. Find
theprobabilitythatbothofthemareselected.

## Answers: [’A)2/69’,’B)2/20’,’C)2/18’,’D)2/29’,’E)2/15’]


## Maxprobability: 0.969

QUESTION: Amanbuysanarticlefor100.andsellsitfor110. Findthegainpercent?

## Answers: [’A)10%’,’B)15%’,’C)25%’,’D)20%’,’E)30%’]


## Maxprobability: 0.970

1
correct
30 wrong
prompts
20
10
0
10
20
0
20 10 0 10 20
Figure4.Visualizationofpromptembeddingson(question,reasoning)tuplesonAQUA.Thedarkershadesofblueindicateprompts
generatedatlateriterations.Ourboostingalgorithmgeneratespromptswhichcoverlocationsadjacenttoincorrectanswers.

<!-- Page 15 -->

BoostedPromptEnsemblesforLargeLanguageModels

### D.Prompts


### D.1.ExampleBoostedPrompt

Anexampleboostedprompt,onGSM8K,constructedduringtesttimeboostingisbelow. Theanswersaregeneratedbythe
model,andsomeareincorrect,astheoverallaccuracyofthepromptisonly75%.

### Info:

New prompt accuracy: [ True True True False False True True True] 0.75
Answers: [’144’ ’3000’ ’98’ ’10’ ’105’ ’10’ ’5’ ’1520’]

### Theprompt:

Q: A local town is expanding and wants to build several new homes across the
next three years. In the first year, they will build 12 homes. In the next
year, they will build three times this many homes. In the third year,
they will count how many homes they have built and double the amount. How
many homes will the town have built over the next three years?
A: In the first year, 12 homes will be built. In the second year, 3 times this
many homes will be built, so that is 3 * 12 = 36 homes. In the third year,
the town will count how many homes they have built so far and double the
amount, so that is 2 * (12 + 36) = 2 * 48 = 96 homes. In total, they will
build 12 + 36 + 96 = 144 homes. The answer is 144.
Q: Stanley was standing on the side of the mountain, at an elevation of 10,000
feet, when a gust air blew the comb out of his pocket, causing the comb
to fall 4,000 feet to a ledge below. Stanley’s brother, Oliver, was also
on the mountain, but he was at an elevation of 3,000 feet. Stanley called
Oliver on his cellphone and asked Oliver to find Stanley’s comb. How many
feet must Oliver climb to reach the elevation of Stanley’s comb?
A: Stanley was on the top of the mountain, at an elevation of 10,000 feet. The
comb fell 4,000 feet, so the comb is now at an elevation of 10,000 -
4,000 = 6,000 feet. Oliver is at an elevation of 3,000 feet. To get to the
comb, Oliver must climb 6,000 - 3,000 = 3,000 feet. The answer is 3,000.
Q: Janet had 22 green pens and 10 yellow pens. Then she bought 6 bags of blue
pens and 2 bags of red pens. There were 9 pens in each bag of blue and 6
pens in each bag of red. How many pens does Janet have now?
A: She initially had 22 green and 10 yellow pens, so in total she had 22 + 10
= 32 pens. She bought 6 bags of blue and 2 bags of red. There were 9 pens
in each bag of blue, so in total she got 6 * 9 = 54 blue pens. There were
6 pens in each bag of red, so in total she got 2 * 6 = 12 red pens. In
total she got 54 + 12 = 66 pens. So after buying, she has 32 + 66 = 98
pens in total. The answer is 98.
Q: Sara wants to buy herself a new jacket and 2 pairs of shoes. The jacket she
wants costs $30 and each pair of shoes cost $20. Sara babysits the
neighbor’s kids 4 times, earning $5 each time she babysits them. Her
parents pay her $4 each time she mows the lawn. If Sara already had $10
saved before she started babysitting, how many times must she mow the lawn
before she can afford the jacket and shoes?
A: The jacket costs $30 and the shoes cost $20 each. That means she needs $30
+ $20 + $20 = $70 to buy them all. She already has $10 saved. To buy the
jacket and shoes, she needs to save another $70 - $10 = $60. She earns $5
each time she babysits and $4 each time she mows the lawn. To earn $60,
she must mow the lawn 15 times: $60 / $4 = 15. The answer is 15.
Q: Elijah has one dog that is one-fourth the weight of Kory’s dog and another
dog that is half the weight of Kory’s dog. If Kory’s dog is 60 pounds, how
much do Elijah and Kory’s dogs weigh altogether, in pounds?
A: We are told that Kory’s dog weighs 60 pounds. We are also told that Elijah
has two dogs. One of his dogs weighs 1/4 of Kory’s dog and the other is
half as heavy as Kory’s dog. That means that Elijah has a dog that weighs
1/4 * 60 = 15 pounds and another dog that weighs 1/2 * 60 = 30 pounds. In

<!-- Page 16 -->


### BoostedPromptEnsemblesforLargeLanguageModels

total, he has a dog that weighs 15 + 30 = 45 pounds. The answer is 45.
Q: A clothing store has 40 white shirts and 50 floral shirts. Half of the
white shirts have collars, and 20 of the floral shirts have buttons. How
many more floral shirts with no buttons are there than white shirts with
no collars?
A: Half of the white shirts have collars, so the rest have no collars. That
means white shirts with no collars are 40 / 2 = 20. 20 of the floral
shirts have buttons. That means the rest have no buttons. The total number
of floral shirts is 50. So floral shirts with no buttons must be 50 - 20
= 30. The difference is 30 - 20 = 10. The answer is 10.
Q: Gary likes to walk around the edge of the local park, which is a rectangle
that measures 1.5 miles by 6 miles. If he walks at 3 miles/hour, how many
hours does he spend walking?
A: The perimeter of a rectangle is the sum of its sides. Here the perimeter
must be 1.5 + 6 + 1.5 + 6 = 15 miles. He walks at 3 miles/hour. So in 15 /
3 = 5 hours he will complete the walk. The answer is 5 hours.
Q: While working at the restaurant, each of the forty customers who came into
the restaurant gave Rafaela a $20 tip. Julieta received 10% less money in
tips than Rafaela. How much money did Julieta and Rafaela receive as tips
altogether?
A: There were 40 customers. They gave Rafaela $20 each, so in total she
received 40 * $20 = $800. Julieta received 10% less, so she received $800 -
10% of $800 = $720. In total, Rafaela and Julieta received $800 + $720 =
$1520. The answer is 1520.

### D.2.InitialPrompts

FewShot Thefollowingpromptsareusedinthe“fewshot”annotationsetting:

## Gsm8K

Q:Thereare15treesinthegrove.Groveworkerswillplanttreesinthegrovetoday.Aftertheyaredone,therewillbe21trees.

### Howmanytreesdidthegroveworkersplanttoday?

A:Westartwith15trees.Laterwehave21trees.Thedifferencemustbethenumberoftreestheyplanted.So,theymusthave
planted21-15=6trees.Theansweris6.
Q:Ifthereare3carsintheparkinglotand2morecarsarrive,howmanycarsareintheparkinglot?
A:Thereare3carsintheparkinglotalready.2morearrive.Nowthereare3+2=5cars.Theansweris5.
Q:Leahhad32chocolatesandhersisterhad42.Iftheyate35,howmanypiecesdotheyhaveleftintotal?
A:Leahhad32chocolatesandLeah’ssisterhad42.Thatmeanstherewereoriginally32+42=74chocolates.35havebeen
eaten.Sointotaltheystillhave74-35=39chocolates.Theansweris39.
Q:Jasonhad20lollipops.HegaveDennysomelollipops.NowJasonhas12lollipops.HowmanylollipopsdidJasongiveto

### Denny?

A:Jasonhad20lollipops.Sinceheonlyhas12now,hemusthavegiventheresttoDenny.Thenumberoflollipopshehas
giventoDennymusthavebeen20-12=8lollipops.Theansweris8.
Q:Shawnhasfivetoys.ForChristmas,hegottwotoyseachfromhismomanddad.Howmanytoysdoeshehavenow?
A:Hehas5toys.Hegot2frommom,soafterthathehas5+2=7toys.Thenhegot2morefromdad,sointotalhehas7+2
=9toys.Theansweris9.
Q:Therewereninecomputersintheserverroom.Fivemorecomputerswereinstalledeachday,frommondaytothursday.

### Howmanycomputersarenowintheserverroom?

A:Thereare4daysfrommondaytothursday.5computerswereaddedeachday.Thatmeansintotal4*5=20computers
wereadded.Therewere9computersinthebeginning,sonowthereare9+20=29computers.Theansweris29.
Q:Michaelhad58golfballs.Ontuesday,helost23golfballs.Onwednesday,helost2more.Howmanygolfballsdidhe
haveattheendofwednesday?
A:Michaelinitiallyhad58balls.Helost23onTuesday,soafterthathehas58-23=35balls.OnWednesdayhelost2more
sonowhehas35-2=33balls.Theansweris33.
Q:Oliviahas$23.Sheboughtfivebagelsfor$3each.Howmuchmoneydoesshehaveleft?
A:Shebought5bagelsfor$3each.Thismeansshespent5*$3=$15onthebagels.Shehad$23inbeginning,sonowshe
has$23-$15=$8.Theansweris8.

## Aqua


<!-- Page 17 -->


### BoostedPromptEnsemblesforLargeLanguageModels

Q:Johnfoundthattheaverageof15numbersis40.If10isaddedtoeachnumberthenthemeanofthenumbersis?Answer

### Choices:(a)50(b)45(c)65(d)78(e)64

A:If10isaddedtoeachnumber,thenthemeanofthenumbersalsoincreasesby10. Sothenewmeanwouldbe50. The
answeris(a).
Q:Ifa/b=3/4and8a+5b=22,thenfindthevalueofa.AnswerChoices:(a)1/2(b)3/2(c)5/2(d)4/2(e)7/2
A:Ifa/b=3/4,thenb=4a/3.So8a+5(4a/3)=22.Thissimplifiesto8a+20a/3=22,whichmeans44a/3=22.Soais
equalto3/2.Theansweris(b).
Q:Apersonistravelingat20km/hrandreachedhisdestinyin2.5hrthenfindthedistance?AnswerChoices:(a)53km(b)
55km(c)52km(d)60km(e)50km
A:Thedistancethatthepersontraveledwouldhavebeen20km/hr*2.5hrs=50km.Theansweris(e).
Q:Howmanykeystrokesareneededtotypethenumbersfrom1to500?AnswerChoices:(a)1156(b)1392(c)1480(d)1562
(e)1788
A:Thereare9one-digitnumbersfrom1to9. Thereare90two-digitnumbersfrom10to99. Thereare401three-digit
numbersfrom100to500.9+90(2)+401(3)=1392.Theansweris(b).

## Mmlu570

Q:Whichofthefollowingrepresentsanaccuratestatementconcerningarthropods?(a)Theypossessanexoskeletoncomposed
primarilyofpeptidoglycan. (b)Theypossessanopencirculatorysystemwithadorsalheart. (c)Theyaremembersofa
biologicallyunsuccessfulphylumincapableofexploitingdiversehabitatsandnutritionsources.(d)Theylackpaired,jointed
appendages.
A:Arthropodshaveanexoskeleton.Thisexoskeletonisnotcomposedprimarilyofpeptidoglycan.Arthropodshaveanopen
circulatorysystemwithadorsalheart. Arthropodsareverysuccessfulinexploitingdiversehabitatsandnutritionsources.
Arthropodshavepaired,jointedappendages.Theansweris(b).
Q:Theenergyforallformsofmusclecontractionisprovidedby: (a)ATP.(b)ADP.(c)phosphocreatine. (d)oxidative
phosphorylation.
A:TheenergyforallformsofmusclecontractionisprovidedbyATP.Theansweris(a).
Q: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong,
accordingtoordinarymoralstandardsintheUSasof2020?Scenario1—Iaskedforacigarettefromtheguyoutsidethe
store.Scenario2—Whenthesecurityguardlefthispost,Ipocketedararecoin.(a)Wrong,Wrong(b)Wrong,Notwrong(c)

### Notwrong,Wrong(d)Notwrong,Notwrong

A:ThemaincharacterinScenario1doesnotdosomethingmorallywrong,accordingtoordinarymoralstandardsintheUSas
of2020.InScenario2,themaincharacterdoessomethingclearlymorallywrong,accordingtoordinarymoralstandardsinthe
USasof2020.Theansweris(c).
Q:ConsiderthefollowingAR(1)modelwiththedisturbanceshavingzeromeanandunitvariance
yt=0.2+0.4yt-1+ut
The(unconditional)meanofywillbegivenby(a)0.2(b)0.4(c)0.5(d)0.33
A:Westartwiththeunconditionalmeanofy,whichistheaveragevalueofyacrossallpossiblevaluesoftime. Sincethe
disturbanceshavezeromeanandunitvariance,themeanofyisdeterminedonlybythecoefficientsoftheAR(1)model.We
haveyt=0.2+0.4yt-1.So,themeanofy(i.e.theunconditionalmean)isgivenby0.2+0.4*(meanofy).Thisisarecursive
equation,sowecansolveitbyiteration.Westartwiththeinitialguessof0.2,thenwerepeattheequationandsetthemeanof
ytobe0.2+0.4*(0.2)=0.33.Werepeattheequationagainandsetthemeanofytobe0.2+0.4*(0.33)=0.33.Wecansee
thatthemeanofyisconvergingto0.33,sotheansweris(d).

## Cmath420

Q: Compute $\left(\sqrt{625681}\right)ˆ2$.
A: For any nonnegative number $n$, the value of $\sqrt{n}$ is the
number whose square is $n$. So, when we square $\sqrt{n}$, we get
$n$. Therefore, $\left(\sqrt{625681}\right)ˆ2 = \boxed{625681}$.
The answer is 625681.
Q: Find $160\div \left(10+11\cdot 2\right)$.
A: Recall that we must perform the operations inside the parentheses
first. So, we must simplify $10+11\cdot 2$ first. Of these
operations, we must do the multiplication and then the addition
because multiplication and division must be done before addition
and subtraction. We get \begin{align*}10+11\cdot 2 &=10+22 \\
&=32.\end{align*}Now, we substitute back into the original
expression and do the division. Therefore, \begin{align*}160\div \
left(10+11\cdot 2\right)&=160\div 32 \\ &=\boxed{5}.\end{align*}
The answer is 5.

<!-- Page 18 -->


### BoostedPromptEnsemblesforLargeLanguageModels

Q: What number, when divided by 2, gives the same result as when 2 is
subtracted from it?
A: If we let $x =$ the number that we want to find, we know that $x/2$
must equal $x-2$. Multiplying both sides of the equation $x/2=x-2$
by $2$, we have that $x=2x-4$, so $x=\boxed{4}$. The answer is 4.
Q: What is the result when we compute $$1ˆ3 + 2ˆ3 + 3ˆ3 + 4ˆ3 + \dots +
99ˆ3 + 100ˆ3 $$and $$(-1)ˆ3 + (-2)ˆ3 + (-3)ˆ3 + (-4)ˆ3 + \dots +
(-99)ˆ3 + (-100)ˆ3,$$and then add the two results?
A: Recall that $(-a)ˆ3=-aˆ3$. Thus, our second sum can be rewritten as
$$ (-1ˆ3) + (-2ˆ3) + (-3ˆ3) + (-4ˆ3) + \dots + (-99ˆ3) + (-100ˆ3).
$$When we add this with $$1ˆ3 + 2ˆ3 + 3ˆ3 + 4ˆ3 + \dots + 99ˆ3 +
100ˆ3, $$we can pair the terms conveniently: \[1ˆ3 + (-1ˆ3) + 2ˆ3 +
(-2ˆ3)+ 3ˆ3 + (-3ˆ3) + \dots + 100ˆ3 + (-100ˆ3). \]Because any
number plus its negation is zero, each of these pairs of terms sum
to zero, and the sum of the entire sequence is $\boxed{0}$. The
answer is 0.
Q: A particular triangle has sides of length 14 cm, 8 cm and 9 cm. In
centimeters, what is the perimeter of the triangle?
A: The perimeter of a polygon is defined to be the sum of the measures
of the sides of the polygon. Therefore, the perimeter of a
triangle whose sides measure 14 cm, 8 cm, and 9 cm is $\boxed{31}$
centimeters. The answer is 31.
Q: A basketball player made the following number of free throws in 8
successive games: 6, 18, 15, 14, 19, 12, 19, and 15. What is the
median number of successful free throws?
A: To find the median, we first arrange the number of successful free
throws in increasing numerical order: $$6,12,14,15,15,18,19,19.$$
Since there is an even number of terms, the median can be found the
by averaging the middle two (the fourth and the fifth) terms. Both
the fourth and the fifth terms are $15$, so the median number of
successful free throws that the basketball player made is $\boxed
{15}$. The answer is 15.
Q: Find $1ˆ{234} + 4ˆ6 \div 4ˆ4$.
A: Since 1 raised to any power is 1, the expression equals $1 + 4ˆ6 \
div 4ˆ4$. Also recall that $\frac{aˆm}{aˆn}=aˆ{m-n}$, so we can
simplify the last term to get $1+4ˆ{6-4}=1+4ˆ2=1+16=\boxed{17}$.
The answer is 17.
Q: Marty wants to paint a box. He can choose to use either blue, green,
yellow, or black paint. Also, he can style the paint by painting
with a brush, a roller, or a sponge. How many different
combinations of color and painting method can Marty choose?
A: Marty can choose his paint in 4 ways and his style in 3 ways. Thus
there are a total of $4\cdot 3 = \boxed{12}$ different combinations
he can choose. The answer is 12.

## Svamp


## Sameasgsm8K

ComplexityPrompting Thefollowingpromptsareusedforourimplementationofcomplexity-basedprompting:

## Gsm8K

Q: You can buy 4 apples or 1 watermelon for the same price. You bought
36 fruits evenly split between oranges, apples and watermelons,
and the price of 1 orange is $0.50. How much does 1 apple cost if
your total bill was $66?
A: If 36 fruits were evenly split between 3 types of fruits, then I
bought 36/3 = <<36/3=12>>12 units of each fruit

<!-- Page 19 -->


### BoostedPromptEnsemblesforLargeLanguageModels

If 1 orange costs $0.50 then 12 oranges will cost $0.50 * 12 = $
<<0.5*12=6>>6
If my total bill was $66 and I spent $6 on oranges then I spent $66 -
$6 = $<<66-6=60>>60 on the other 2 fruit types.
Assuming the price of watermelon is W, and knowing that you can buy 4
apples for the same price and that the price of one apple is A,
then 1W=4A1
If we know we bought 12 watermelons and 12 apples for $60, then we
know that $60 = 12W + 12A
Knowing that 1W=4A, then we can convert the above to $60 = 12(4A) + 12

## A


## $60 = 48A + 12A


## $60 = <<60=60>>60A

Then we know the price of one apple (A) is $60/60= $<<60/60=1>>1. The
answer is 1.
Q: Bella has two times as many marbles as frisbees. She also has 20
more frisbees than deck cards. If she buys 2/5 times more of each
item, what would be the total number of the items she will have if
she currently has 60 marbles?
A: When Bella buys 2/5 times more marbles, she’ll have increased the
number of marbles by 2/5*60 = <<2/5*60=24>>24
The total number of marbles she’ll have is 60+24 = <<60+24=84>>84
If Bella currently has 60 marbles, and she has two times as many
marbles as frisbees, she has 60/2 = <<60/2=30>>30 frisbees.
If Bella buys 2/5 times more frisbees, she’ll have 2/5*30 =
<<2/5*30=12>>12 more frisbees.
The total number of frisbees she’ll have will increase to 30+12 =
<<30+12=42>>42
Bella also has 20 more frisbees than deck cards, meaning she has 30-20
= <<20-10=10>>10 deck cards
If she buys 2/5 times more deck cards, she’ll have 2/5*10 =
<<2/5*10=4>>4 more deck cards.
The total number of deck cards she’ll have is 10+4 = <<10+4=14>>14
Together, Bella will have a total of 14+42+84 = <<14+42+84=140>>140
items. The answer is 140.
Q: Susy goes to a large school with 800 students, while Sarah goes to
a smaller school with only 300 students. At the start of the school
year, Susy had 100 social media followers. She gained 40 new
followers in the first week of the school year, half that in the
second week, and half of that in the third week. Sarah only had 50
social media followers at the start of the year, but she gained 90
new followers the first week, a third of that in the second week,
and a third of that in the third week. After three weeks, how many
social media followers did the girl with the most total followers
have?
A: After one week, Susy has 100+40 = <<100+40=140>>140 followers.
In the second week, Susy gains 40/2 = <<40/2=20>>20 new followers.
In the third week, Susy gains 20/2 = <<20/2=10>>10 new followers.
In total, Susy finishes the three weeks with 140+20+10 =
<<140+20+10=170>>170 total followers.
After one week, Sarah has 50+90 = <<50+90=140>>140 followers.
After the second week, Sarah gains 90/3 = <<90/3=30>>30 followers.
After the third week, Sarah gains 30/3 = <<30/3=10>>10 followers.
So, Sarah finishes the three weeks with 140+30+10 =
<<140+30+10=180>>180 total followers.
Thus, Sarah is the girl with the most total followers with a total of

## The answer is 180.

Q: Mark’s basketball team scores 25 2 pointers, 8 3 pointers and 10
free throws. Their opponents score double the 2 pointers but half
the 3 pointers and free throws. What’s the total number of points
scored by both teams added together?
A: Mark’s team scores 25 2 pointers, meaning they scored 25*2=

<!-- Page 20 -->

BoostedPromptEnsemblesforLargeLanguageModels
<<25*2=50>>50 points in 2 pointers.
His team also scores 6 3 pointers, meaning they scored 8*3= 24 points
in 3 pointers
They scored 10 free throws, and free throws count as one point so they
scored 10*1=<<10*1=10>>10 points in free throws.
All together his team scored 50+24+10= <<50+24+10=84>>84 points
Mark’s opponents scored double his team’s number of 2 pointers,
meaning they scored 50*2=<<50*2=100>>100 points in 2 pointers.
His opponents scored half his team’s number of 3 pointers, meaning
they scored 24/2= <<24/2=12>>12 points in 3 pointers.
They also scored half Mark’s team’s points in free throws, meaning
they scored 10/2=<<10/2=5>>5 points in free throws.
All together Mark’s opponents scored 100+12+5=<<100+12+5=117>>117
points
The total score for the game is both team’s scores added together, so
it is 84+117=<<84+117=201>>201 points. The answer is 201.
Q: The total average age of three friends is 40. Jared is ten years
older than Hakimi, and Molly’s age is 30. How old is Hakimi?
A: The total age for the three friends is 40*3 = <<40*3=120>>120
If Molly’s age is 30, then Jared and Hakimi have a total age of 120-30
= 90.
Let’s say the age of Hakimi is x.
Since Jared is 10 years older than Hakimi, Jared is x+10 years old.
Jared and Hakimi’s total age is x+(x+10) = 90
This translates to 2x=90-10
2x=80

### Hakimi’s age is x=80/2

This gives us x=<<40=40>>40, which is Hamkimi’s age. The answer is 40.
Q: Together 3 friends watched 411 short videos. Kelsey watched 43 more
than Ekon. Ekon watched 17 less than Uma. How many videos did

### Kelsey watch?

A: Let U = the number of videos Uma watched

### Ekon = U - 17

Kelsey = (U - 17) + 43 = U + <<(-17)+43=26>>26
U + U - 17 + U + 26 = 411

## 3U + 9 = 411


## 3U = 402


## U = <<134=134>>134


### Kelsey = 134 + 26 = <<134+26=160>>160 videos

Kelsey watched 160 videos. The answer is 160.
Q: Sam bought a dozen boxes, each with 30 highlighter pens inside, for
$10 each box. He rearranged five of these boxes into packages of
six highlighters each and sold them for $3 per package. He sold the
rest of the highlighters separately at the rate of three pens for
$2. How much profit did he make in total, in dollars?
A: Sam bought 12 boxes x $10 = $<<12*10=120>>120 worth of highlighters.
He bought 12 * 30 = <<12*30=360>>360 highlighters in total.
Sam then took 5 boxes x 6 highlighters/box = <<5*6=30>>30 highlighters.

### He sold these boxes for 5 * $3 = $<<5*3=15>>15

After selling these 5 boxes there were 360 - 30 = <<360-30=330>>330
highlighters remaining.
These form 330 / 3 = <<330/3=110>>110 groups of three pens.
He sold each of these groups for $2 each, so made 110 * 2 = $
<<110*2=220>>220 from them.
In total, then, he earned $220 + $15 = $<<220+15=235>>235.
Since his original cost was $120, he earned $235 - $120 = $
<<235-120=115>>115 in profit. The answer is 115.
Q: Megan pays $16 for a shirt that costs $22 before sales. What is the
amount of the discount?

<!-- Page 21 -->

BoostedPromptEnsemblesforLargeLanguageModels
A: Let x be the amount of the discount.

### We have, 22 - x = $16

We change the writing of the equation:
22 - x + x = 16 + x

### So, 22 = 16 + x

We then Remove 16 from both sides:
22 - 16 = 16 + x - 16

### So, 22 - 16 = x

So, the amount of the discount is x = $<<6=6>>6. The answer is 6.

## Aqua

Q: The sum of the terms of an infinite G.P is 7 and the sum of the
cubes of the terms is 1,225. Find the first term of the series.
Answer Choices: (a) 35/3 (b) 35/2 (c) 15/2 (d) 9/4 (e) 7/4

### A: S a = a/ ( 1 - r ) = 7 ..... (1)

Sum to infinity of the cubes = a 3 / 1 -r 3 = 1,225

### From (1) a 3 / ( 1 - r ) 3 = 7 3 = 343

Therefore, ( 1 - r ) 3 / 1 - r 3 = 1225/343,
(1+ r 2 -2r)/ ( 1 + r 2 + r ) = 25/7
7 + 7 r 2 -14r = 25 + 25 r + 25 r 2
18 r 2 +39r + 18 = 0, on solving r = -3/2 or -2/3
for an infinite G.P | r | < 1, r = - 2/3
Therefore, a / [ 1 - ( - 2/3 ) ] = 7, a = 7 * 5/3 = 35/3 ANSWER: a.
The answer is (a).
Q: A factory has three types of machines, each of which works at its
own constant rate. If 7 Machine As and 11 Machine Bs can produce
261 widgets per hour, and if 8 Machine As and 22 Machine Cs can
produce 600 widgets per hour, how many widgets could one machine A,
one Machine B, and one Machine C produce in one 8-hour day? Answer

### Choices: (a) 408 (b) 475 (c) 550 (d) 625 (e) 700

A: Let Machine A produce A widgets per hour. B produce B widgets per
hour and C produce C widgets per hour.

## 7A+11B=261 ---(1)


## 8A+22C=600 ---(2)


### Dividing (2) by 2


## 4A+11C=300.....(3)


### Adding (1)(3)


## 11A+11B+11C = 561


### A+B+C=51 per hour

So for eight hrs = 51*8 = 408 = Answer = a. The answer is (a).
Q: Three boys are ages 4, 6 and 7 respectively. Three girls are ages 5,
8 and 9, respectively. If two of the boys and two of the girls are
randomly selected and the sum of the selected children’s ages is e
, what is the difference between the probability that e is even and
the probability that e is odd? Answer Choices: (a) 1/9 (b) 1/6 (c)
2/9 (d) 1/4 (e) 1/2

### A: Age of Boys e:4, 6, 7

Sum of ages taken 2 at a time: 10,13,11

### Ages of Girls:5, 8, 9


### Sum of ages taken 2 at a time: 13,17,14

9 Combinations of sum between sets(10,12,11)(13,17,14)
=23,27,24- 16,30,17- 24,28,25
Prob(Even)= 5/9

### Prob(Odd) =4/9

Answer=5/9 - 4/9 = 1/9. The answer is (a).
Q: The weights of one liter vegetable ghee packet of two brands ’A’
and ’B’ are 800 gm and 850 gm respectively. If they are mixed in
the ratio of 3 : 2 by volumes to form a mixture of 3 liters, what
is the weight (in kg) of the mixture? Answer Choices: (a) 3.84 (b)
1.75 (c) 3.52 (d) 2.46 (e) None of these

<!-- Page 22 -->


### BoostedPromptEnsemblesforLargeLanguageModels

A: Here’s how I did it. My notes from reading the problem were:
1L A = 800 gm
1L B = 850 gm
We are mixing five parts (3 parts A plus 2 parts B, 5 parts total) to
get 3L, so 5x = 3 ---> x = 3/5. Each part is 3/5 of a liter.
So if we have 3 parts A, we have 800*3*(3/5) = 1440
If we have 2 parts B, we have 850*2*(3/5) = 1020
1440 + 1020 = 2460

### Solving for units gives us 2.46

So the answer is d. The answer is (d).
Q: What is the total number of X integers between 100 and 200 that are
divisible by 3? Answer Choices: (a) 33 (b) 32 (c) 31 (d) 30 (e) 29
A: yes there is a different way of arriving at that answer ....
u can also use airthmetic progression to get the answer
since the first term to be divisble by 3 is 102 ..take that as A ..
the starting no
and since 198 is the last digit to be divisible by 3 take that as N ...
since the difference is 3 take that as D
no u have to find what term is 198 take that as nth term
the formula for that is N = A + (n-1) * d
198 = 102 +(n-1) * 3
from this u get n =33. The answer is (a).
Q: An automobile parts supplier charges $25 per package of gaskets.
When a customer orders more than 10 packages of gaskets, the
supplier charges 4/5 the price for each package in excess of 10.
During a certain week, the supplier sold 60 packages of gaskets. If
30 percent of the gaskets went to Company X, 15 percent to Company

### Y, and the rest to Company Z, what was the total amount, in

dollars, that the parts supplier received in payment for the
gaskets? Answer Choices: (a) 1305 (b) 1375 (c) 1345 (d) 1415 (e)
1455
A: $25 per packet of gasket in case a customer orders less than 10
in case a customer orders > 10 price per gasket = 25*4/5=20
a certain week the supplier sold 60 gasket
1.he sold 30 % of the gaskets to X = 18 gaskets = 25*10 + 20 *8 = 250 +
160 = 410
2.he sold 15 % of the gaskets to Y = 9 gaskets = 25*9= 225
3.he sold remaining 55% to z =33 gaskets = 25*10 =250 + 20*23=710
thus ,total money earned
410+225+710 = 1345
The answer is (c).
Q: A company spends an average of $500 for its 20 employees’s salaries
and an average of $100 for its 5 drivers’ salaries. What is the
average expenditure of the company? Answer Choices: (a) $360 (b)
$290 (c) $420 (d) $600 (e) $240
A: Number of employees is 20
Their average salary is $500

### Number of drivers is 5


### Their average salary is $100

Total salary of the employees is 20*500=$10,000

### Total salary of the drivers is 5*100=$500

Total expenditure for company is 10,000+500=$10,500
Average expenditure is 10,500/20+5=$420
The answer is (c).
Q: The minute hand of a clock overtakes the hour hand at intervals of
65 minutes of the correct time. How much a day does the clock gain
or lose? Answer Choices: (a) (10 + 10/143 )min (b) (10 + 10/843 )
min (c) (10 + 19/143 )min (d) (90 + 10/143 )min (e) (10 + 10/193 )
min
A: In a correct clock, the minute hand gains 55 min. spaces over the

<!-- Page 23 -->

BoostedPromptEnsemblesforLargeLanguageModels
hour hand in 60 minutes.
To be together again, the minute hand must gain 60 minutes over the
hour hand.
55 minutes are gained in 60 min.
60 min. are gained in [(60/55) * 60] min = min.
But they are together after 65 min.
Therefore, gain in 65 minutes = = min.
Gain in 24 hours = = 1440/143 min.
Therefore, the clock gains (10 + 10/143 )minutes in 24 hours.
Answer: (a) (10 + 10/143 )min. The answer is (a).
AutoCoTPrompting ThefollowingAutoCoTpromptsareusedforthezeroshotsetting:

## Gsm8K

Q:Jackdecidestovisitamuseum150milesfromhome.Hedrives75mphthereandback.Hespends6hoursatthemuseum.

### Howlongishegonefromhome?

A:Let’sthinkstepbystep.Jackdrives75mphthere.Thiswilltakehim2hours.Hespends6hoursatthemuseum.Hedrives
75mphback.Thiswilltakehim2hours.SoJackisgoneforatotalof6hours.Theansweris6.
Q:Roberthad3poundsofcandy,Cindyhad5poundsofcandy,andAaronhad4poundsofcandyafterHalloween.Ifthey
decidetopoolandsharetheircandyequallywitheachother,howmuchcandywouldeachofthemhave?
A:Let’sthinkstepbystep.Roberthad3poundsofcandy,Cindyhad5poundsofcandy,andAaronhad4poundsofcandy
afterHalloween.Thatmeansthattherewasatotalof3+5+4=12poundsofcandy.Iftheydecidetopoolandsharetheir
candyequallywitheachother,thatmeansthateachpersonwouldget12/3=4poundsofcandy.Theansweris4.
Q:Susanmade100cookiesforChristmasandwasgoingtoequallydividethembetweenher6nephews.BeforeSusancould
packagethem,herhusbandsnuck4cookiesforhimself.HowmanycookieswilleachofSusan’snephewsget?
A:Let’sthinkstepbystep.Susanmade100cookies.Thenherhusbandsnuck4cookies.Thatmeansthatnowsheonlyhas96
cookies.Sinceshewantstodividethemequallybetweenher6nephews,eachnephewwillget16cookies.Theansweris16.
Q:Tombuysabedroomsetfor$3000.Hesellshisoldbedroomfor$1000andusesthattopayforpartofthebedroomset.He
thenhastopay10%amonthforthebedroomset.Howmuchdoeshehavetopaypermonth?
A:Let’sthinkstepbystep.Tombuysabedroomsetfor$3000.Hesellshisoldbedroomfor$1000andusesthattopayfor
partofthebedroomset.Tomhastopay$2000forthenewbedroomset.Hethenhastopay10%amonthforthebedroomset.
Thismeansthateverymonth,Tomhastopay$200forhisnewbedroomset.Theansweris200.
Q:Ifaclassroomhas3timesasmanygirlsastheydoboys,and1/10asmanynongenderedchildrenastheydoboys,andthe
classroomhas30boys.Howmanytotalchildrendoesithave?
A:Let’sthinkstepbystep.Thereare3timesasmanygirlsasboys,soifthereare30boys,thereare3*30=90girls.Thereare
1/10asmanynongenderedchildrenasthereareboys,soifthereare30boys,thereare30/10=3nongenderedchildren.Nowwe
canaddtheseup:90+30+3=123totalchildren.Theansweris123.
Q:Annaistryingtobuybooksforherlocallibrary.Shehadabudgetof$16,andshehasalreadyspent$4.Shealsobought2
bookstoday,andbothbookscostherthesameamountofmoney.IfAnnahas$2leftinherbudget,howmuchdideachofthe
bookscost?
A:Let’sthinkstepbystep.Annahasabudgetof$16.Shespends$4,soshehas$12left.Shebuys2books,soshehas$2left.
Thatmeansthateachbookcosther$5.Theansweris5.
Q:Jimspends2hourswatchingTVandthendecidestogotobedandreadsforhalfaslong.Hedoesthis3timesaweek.How
manyhoursdoeshespendonTVandreadingin4weeks?
A:Let’sthinkstepbystep.Inoneweek,Jimspends6hourswatchingTVand3hoursreading.In4weeks,hespends24hours
watchingTVand12hoursreading.Theansweris24.
Q:IfAnnis9yearsoldandherbrotheristwiceherage,howoldwillherbrotherbein3years?
A:Let’sthinkstepbystep.Annis9yearsold.Herbrotheristwiceherage.Thatmeansherbrotheris9*2=18yearsold.In
3years,herbrotherwillbe18+3=21yearsold.Theansweris21.

## Aqua

Q:Julie’syardisrectangular.Onesideoftheyardis100feetwide.Thetotalareaoftheyardis3,000squarefeet.Whatisthe
lengthoftheothersideoftheyard?AnswerChoices:(a)30feet(b)20feet(c)10feet(d)50feet(e)60feet
A:Let’sthinkstepbystep.Weknowthattheyardisrectangular,soithasfoursides.Wealsoknowthatonesideoftheyardis
100feetwide.Thetotalareaoftheyardis3,000squarefeet.Wecansetuptheequation:3,000=100xx=30So,thelengthof
theothersideoftheyardis30feet.Theansweris(a).
Q:Inasurveyofstudents,eachstudentselectedfromalistof10songsthe2songsthatthestudentlikedbest.Ifeachsongwas
selected5times,howmanystudentsweresurveyed?AnswerChoices:(a)96(b)48(c)32(d)25(e)18
A:Let’sthinkstepbystep.Thereare10songs,andeachsongisselected5times.Thatmeansthatthereare50selectionsin
total.Eachstudentmakes2selections,sotheremustbe25students.Theansweris(d).

<!-- Page 24 -->


### BoostedPromptEnsemblesforLargeLanguageModels

Q:MarktoldJohn”IfyougivemehalfyourmoneyIwillhaveRs.75”.Johnsaid,”ifyougivemeonethirdofyourmoney,I
willhaveRs.75”.HowmuchmoneydidJohnhave?AnswerChoices:(a)22(b)60(c)28(d)26(e)18
A:Let’sthinkstepbystep.IfMarkhasRs.75,thenJohnhasRs.75aswell.IfMarkgivesJohnhalfhismoney,thenMarkwill
haveRs.37.50andJohnwillhaveRs.112.50.However,thisisn’toneoftheanswerchoices.IfMarkgivesJohnonethirdof
hismoney,thenMarkwillhaveRs.50andJohnwillhaveRs.100.Thisisoneoftheanswerchoices,soJohnmusthavehad
Rs.100tobeginwith.Theansweris(d).
Q:Acarfinishesajourneyin20hoursatthespeedof60km/hr.Ifthesamedistanceistobecoveredin10hours,howmuch
speeddoesthecargain?AnswerChoices:(a)80kmph(b)50kmph(c)120kmph(d)70kmph(e)80kmph
A:Let’sthinkstepbystep.Thecariscurrentlytravellingat60km/hr.Inordertotravelthesamedistancein10hours,thecar
wouldneedtotravelat6timesthespeed,or360km/hr.Therefore,thecarwouldneedtogain300km/hr.Theansweris(c).

## Mmlu570


## Sameasaqua


## Cmath420


## Sameasgsm8K


## Svamp


## Sameasgsm8K

NonsensePrompting Thefollowingtwosamplenonsenseprompt,createdbyaskingChatGPTfornonsensequestions
andanswers(onemultiplechoice,oneopen-endedwithintegersolution),isusedforALLdatasets:

### NonsensePrompt

Q:WhatisthecapitalofthecountryofFlibbertigibbet?AnswerChoices:(a)Gigglemug(b)Snickerdoodle(c)Wibblewobble
(d)FlibbertigibbetCity
A:WewillpretendthatFlibbertigibbetCityisthecapitalofFlibbertigibbet.Theansweris(d).

### Q:Howmanylollipopsareinapileoffluffernutter?

A:Let’sconsiderapileoffluffernutterisholdinglollipops. Itseemsreasonablethatapileoffluffernuttercouldhold17
lollipops.Theansweris17.

## Tables

**Table (Page 2):**

| prompt correct incorrect |
|---|
| prompt correct incorrect |


**Table (Page 2):**

| prompt hard correct incorrect |
|---|
| prompt hard correct incorrect |


**Table (Page 2):**

| prompt 1 prompt 2 correct incorrect |
|---|
| prompt 1 prompt 2 correct incorrect |


**Table (Page 7):**

| BoostedPrompting(ours) | 14.2 | 3.2 | 55.9 | 71.7 | 76.4 | 88.2 |
|---|---|---|---|---|---|---|
|  | 18.1 3.9 |  | 53.1 69.6 |  |  |  |
| BoostedPrompting(ours) | 13.0 | 3.1 | 55.1 | 71.6 | 72.8 | 87.1 |


**Table (Page 14):**

|  |  |  |  | co | rrect |
|---|---|---|---|---|---|
|  |  |  |  | w pr | rong ompts |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
