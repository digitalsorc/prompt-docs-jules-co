---
title: "ReST meets ReAct Self Improvement"
original_file: "./ReST_meets_ReAct_Self_Improvement.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["answer", "search", "str", "thoughts", "self", "example", "solar", "what", "action", "query"]
summary: "<!-- Page 1 -->


## Rest Meets React: Self-Improvement For


## Multi-Step Reasoning Llm Agent

RenatAksitov†1,SobhanMiryoosefi†1,ZonglinLi†1,DaliangLi†1,SheilaBabayan†2,
KavyaKopparapu†2,ZacharyFisher1,RuiqiGuo1,SushantPrakash1,PraneshSrinivasan3,

### ManzilZaheer2,FelixYu1,andSanjivKumar1

1GoogleResearch,2GoogleDeepMind,3Google
†Corecontributors

## Abstract

Answeringcomplexnaturallanguagequestionsoftennecessitatesmulti-stepreasoning and integrating external information. Several systems ha"
related_documents: []
---

# ReST meets ReAct Self Improvement

<!-- Page 1 -->


## Rest Meets React: Self-Improvement For


## Multi-Step Reasoning Llm Agent

RenatAksitov†1,SobhanMiryoosefi†1,ZonglinLi†1,DaliangLi†1,SheilaBabayan†2,
KavyaKopparapu†2,ZacharyFisher1,RuiqiGuo1,SushantPrakash1,PraneshSrinivasan3,

### ManzilZaheer2,FelixYu1,andSanjivKumar1

1GoogleResearch,2GoogleDeepMind,3Google
†Corecontributors

## Abstract

Answeringcomplexnaturallanguagequestionsoftennecessitatesmulti-stepreasoning and integrating external information. Several systems have combined
knowledgeretrievalwithalargelanguagemodel(LLM)toanswersuchquestions.
Thesesystems,however,sufferfromvariousfailurecases,andwecannotdirectly
trainthemend-to-endtofixsuchfailures,asinteractionwithexternalknowledge
isnon-differentiable. Toaddressthesedeficiencies,wedefineaReAct-styleLLM
agent with the ability to reason and act upon external knowledge. We further
refinetheagentthroughaReST-likemethodthatiterativelytrainsonprevioustrajectories, employinggrowing-batchreinforcementlearningwithAIfeedbackfor
continuousself-improvementandself-distillation. Startingfromapromptedlarge
modelandafterjusttwoiterationsofthealgorithm,wecanproduceafine-tuned
smallmodelthatachievescomparableperformanceonchallengingcompositional
question-answeringbenchmarkswithtwoordersofmagnitudefewerparameters.

## 1 Introduction


### For many simple natural language tasks,

like basic question-answering or summarization, we can relatively easily decide
whether the final output is good or bad,
collect large amounts of such data, and
trainthelanguagemodelsusingtheseoutcomesasfeedback. Atthesametime,for
more complex problems, outcome-based
systems are often insufficient, and a process supervision approach has recently
gained much attention as a more promising alternative (Reppert et al. (2023)).

### There is explosive growth in techniques

Figure 1: Agent self-improvement and self-distillation.
(Gaoetal.(2023); Madaanetal.(2023)), Bamboogleauto-eval,meanaccuracyandstandarddeframeworks(Dohanetal.(2022);Khattab viationover10runs,(%)
et al. (2023b)), and libraries (Liu (2022),

### Chase (2022)) for defining process-based

workflowswithLLMsthroughhuman-understandabletaskdecompositions. Manysuchdecompositionsinvolveinteractionwithexternaltools/APIs/environments,inwhichcasethecorresponding
multi-stepworkflowisgenerallyreferredtoasanLLMagent(Xietal.(2023)),asystemcapableof
performingasequenceofactionstoachieveagoal.
Let’sconsiderthetaskofansweringcomplex,open-endedquestions,wheretheagentneedstousea
searchAPItolookupmultiplepiecesofinformationbeforecomposingaparagraph-lengthanswer.
OnepopularapproachforbuildingsuchagentswithLLMsistheReActmethod(Yaoetal.,2022),
which involves interleaving chain-of-thought reasoning with actions and observations during sev-
1
3202
ceD
51
]LC.sc[
1v30001.2132:viXra

<!-- Page 2 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent
eral thought-action-observation rounds. In this work, we follow the general ReAct format for our
SearchAgentwhiledesigningthecorrespondingfew-shotpromptstoproducelong-form,explicitly
attributablefinalanswers(cf. Nakanoetal.(2021)).
It is natural to ask next how to deal with failure cases of such an agent and how to improve its
performance and robustness. For outcome-based systems, the solution is usually straightforward:
wejustcollectmorehuman-labeleddata. However,acquiringsuchdataismuchmorechallenging
and expensive for process-based systems: a significantly larger amount of data is needed (Uesato
etal.(2022);Lightmanetal.(2023)),anditisgenerallyharderforhumanstodetermineanoptimal
multi-steptrajectory.
Toaddressthelackofanddifficultyinobtainingmulti-stephuman-labeleddata,wefocusonimprovingthequalityoftheagentwithself-critique,AIfeedback,andsyntheticdatageneration. Specificallyforthelatter,weadapttherecentlyproposed(Gulcehreetal.(2023))ReinforcedSelf-Training
(ReST) algorithm towards agentic setups. The inner-outer loop flow of ReST remains the same:
in the outer loop (“grow”), the dataset is grown by sampling from the latest policy, and in the innerloop(“improve”),thepolicyisimprovedonafixeddatasetviarankingorfilteringwithreward
model. Inourcase,samplingduring“grow”meansproducingamulti-steptrajectorytocompletion,
andrankingaspartof“improve”isdonedirectlywithLLMcallratherthanwithadistilledreward
modelofhumanpreferences.
WemeasuretheoverallperformanceoftheSearchAgentbyitsabilitytoanswerdiversecompositionalquestionsthatweremanuallyverifiedtobeunanswerabledirectlybyasearchengine(Bamboogledataset(Pressetal.,2023)andasequeldatasetthatweconstructedourselves,BamTwoogle).
Whilebothdatasetsaresmall,theyhaveenoughstatisticalpowertocapturetheeffectsweareinterestedinstudying. Forexample, Figure1providesahigh-leveloverviewoftheagentperformance
onBambooglefordifferentmodelsizesandshowcasestheboostwithmoreiterationsofReST(all
oursyntheticdataisproducedwiththelargemodel,soforsmallermodels,itistheperformanceof
thedistillation).

### Tosummarize,ourcontributionsarethefollowing:

• WebuildaflavorofReActagentwithself-critiqueforthetaskoflong-formquestionanswering.
• WedefineaproxyevaluationmetricfortheagentbasedonBamboogleandBamTwoogle
datasets,withastrongemphasisonauto-eval.
• We demonstrate that the performance of the agent could be effectively improved through
Rest-styleiterativefine-tuningonitsreasoningtraces.
• Furthermore, we do it purely from stepwise AI feedback without using human-labeled
trainingdata.
• Finally, we show that the synthetic data produced as part of this iterative process could
be used for distilling the agent into one or two orders of magnitude smaller models with
performancecomparabletothepre-trainedteacheragent.

## 2 Background: Search Agent

ThissectiondescribesSearchAgent,aflavorofReAct(Yaoetal.,2022)agentwithReflexion(Shinn
etal.,2023). Ituseswebsearchasatooltogeneratelong-form,explicitlyattributableanswersfor
diverseknowledge-seekingopen-endedquestions. Theagent’sflowproceedsasfollows(Figure2):

## Agentreceivesaquestionandstartsexecutingasearchloop:

• Agentdecideswhetheritneedsadditionalinformationtoanswerthequestion.
• If“yes”,itcallsthesearchtool,summarizesthereceivedsnippets,andgoesbackto
thedecisionstep.
• If“no”,itterminatesthesearchloop.

## Basedontheinformationcollectedaspartofthesearchloop,theagentgeneratesthefirst

attempt(draft)oftheanswer.

## Itthenperformstwoadditionalself-revisioncallsbeforeproducingthefinalanswer:

2

<!-- Page 3 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent
• Onetoverifythattheanswerisrelevanttotheoriginalquestion,
• Andanothertocheckthattheanswerisgroundedintheretrievedsnippets.

### ToolCall

IncomingQuestion WebSearch
DecisionStep

### Terminate?

ToolOutputSummarization

### AnswerGeneration


### RelevanceSelf-Check GroundingSelf-Check FinalAnswer

Figure2: AstatemachineoftheSearchAgentflow. EachblueshapecorrespondstoasingleLLM
callanddefinesaseparatetypeofthereasoningstep.

## 3 Methods


## 1 Prompting

WefirstdefinethepromptedflowfortheSearchAgentbymanuallyconstructingfew-shotprompts
for each of the five reasoning steps from Figure 2. Notably, we choose to format our prompts as
Pythoncode(seeAppendixforthepromptsofdifferentsteps,Listings1-6).
Thedecisiontousethe”codeastheprompt”approachismotivatedbythefollowingobservations:
• There is often a need to parse the LLM’s output for integration with other systems and
tools,whichismucheasiertodoifthemodel’sinputandoutputarewell-structured.
• Atthesametime,codeuniquelycombinesastructuredaspect(keywordsandsyntax)with
anaturallanguageaspect(commentsanddescriptivenaming).
• Moreover,LLMsarecapableofbothreadingandwritingcode.
To summarize, since code is naturally structured and easy to parse, it could serve as an excellent
mediumforcommunicationwiththemodel.Accordingly,withinthe”codeastheprompt”paradigm,
LLMisexpectedtounderstandthecodeintheinputandcontinueitasvalidPythonintheoutput,
which turns out to be challenging tasks for the smaller models. Out of the (pre-trained) models
we’vetried,onlythePaLM 2-L(Aniletal.,2023)canperformitconsistentlywell. Hence,thisis
themodelthatweusetoproducereasoningtrajectoriesfromfew-shotprompts.

## 2 Implementationdetails

To run Search Agent, we use PaLM 2 “base” models of different sizes (XS, S and L), both pretrained and fine-tuned. We usually produce multiple samples (with T = 0.5, see Section 4.2 for
detailsontemperatureselection)foreachstepandthenselecttheonewiththelowestperplexity(4
samplesforLandS,16forXS)tocontinuethetrajectoryforward. Asasearchtool,weuseinternal
Google Q&A API that returns top-k snippets, and we typically request top-3 snippets per query
fromit. Wefurtherlimitthenumberoftotalsearchestoatmost10persingleagenttrajectory(via
theREMAINING SEARCHESfieldintheprompts). SearchAgentpreservesthetrajectorystateby
storingalltheactionstakensofarinthePAST ACTIONSfield.
3

<!-- Page 4 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent

## 3 Inputdata

WeusethefollowingfourdatasetstoprovideinitialquestionsforSearchAgenttrajectories:
• HotpotQA(Yangetal.,2018),amulti-hopreasoningQAdataset,wherethesystemhasto
reasonwithinformationtakenfrommorethanonedocumenttoarriveattheanswer.
• Eli5 (Fan et al., 2019), a dataset for long-form question answering (LFQA), a task that
requires elaborate and in-depth answers to open-ended questions. The dataset was built
fromtheRedditforum“ExplainLikeI’mFive”(ELI5),r/explainlikeimfive.
• Eli5-askH(Blagojevic,2022),similartoabove,butbuiltfromtheRedditforumr/askhistorians,asubredditwhereusersmayaskquestionsorstartdiscussionsabouthistory.
• Eli5-askS(Blagojevic,2022),asabove,butfromasubredditr/askscience(“askascience
question,getascienceanswer”).
Werandomlyselected500questionsfromthetrainingsplitsofeachdatasetandendedupwith2000
diverse,challengingquestionsintotal. Wedon’tuseanyotherinformationfromthesedatasets,like
labels(e.g.,wedon’tdoanyfilteringbymatchingthecorrectanswerfromHotpotQA,andwedon’t
usethesedatasets’validationsplitsforhyperparameterstuningorperformanceassessment).

## 4 Fine-Tuning

We simply split each completed Search Agent trajectory into the reasoning steps and build a finetuning mixture with those steps. We use full fine-tuning for all the experiments. Given that finetuning costs increase sharply for larger models, we do as many experiments as possible with XS
model.

## 5 Ranking”Reward”Model

Asmentionedpreviously,weproducemultiplesamplesforeachreasoningstepintheagent’strajectoryandtypicallychoosethesamplethatminimizesperplexitytocontinuethetrajectoryforwardor
tobuildafine-tuningmixture.Atthesametime,wemightbeabletodobetterthanthatbyutilizinga
moresophisticatedwayofselectingthebestsample. Tothiseffect,weemployaninstruction-tuned
PaLM 2-Landpromptitwiththemodelinput,multiplesampledoutputs,andguidanceonhowto
rankthem(thepromptisavailableintheAppendix,Listing8). Wecanthenusethehighest-ranked
sampleforfine-tuninginsteadofthedefaultsamplechosenbasedontheperplexityvalue.
In this part, our approach differs from ReST, which uses threshold-based filtering with a reward
model(RM)trainedonhumanpreferencedata. WhatwedoisclosertoRAFT(Dongetal.,2023),
where the reward model ranks sampled responses to select high-scoring subsets for model finetuning, and the RM rankings matter much more than absolute scores. Notably, we mainly do the
LLM-based selection off-policy, i.e., by updating the current action used for fine-tuning. The onpolicytrajectoryrolloutsuseperplexity.

## 6 Iterativeself-Improvement


### Nowwehaveallthepiecesfortheself-improvementalgorithm:

• StartwithamodelcapableofperformingSearchAgenttaskatacertainlevel,forexample,
withpromptedPaLM 2-Lmodel. Collectreasoningtrajectoriesfromthismodelbasedon
oursetof2000initialquestions(essentiallythe“grow”stageofReST,withthedifference
thatwekeepthesetofinitialquestionsfixed).
• Convertthetrajectoriesintothefine-tuningmixture. Applyre-rankingwithRMduringthe
conversion(thisisroughlyequivalenttothe“improve”stageofReST,thoughweonlydo
oneiterationof“improve”).
• Fine-tunethenewmodel(ofthesamesize)onthismixtureandverifythatit’sperforming
betterthantheoriginalmodel(wewilldiscusshowtodoitinthefollowingsection).Repeat
theprocess,startingwiththisnew,bettermodel.
4

<!-- Page 5 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent
Finally, we can also train smaller models on the fine-tuning data from the different iterations of
self-improvement,whichwillnaturallygiveusaself-distillationalgorithm.

## 4 Evaluation


## 1 Bamboogle

OurprimaryevaluationvehicleistheBamboogledataset(Pressetal.,2023). Itisasemi-adversarial
dataset of 2-hop questions (125 in total) that were selected to be unanswerable by direct Google
search,butwherebothrequiredpiecesofevidencecouldbefoundinWikipedia. WhentheSearch
Agent’sperformanceonBamboogleisimproving, wecanassumethatitgenerallybecomesbetter
inusingsearchasatool.
Given the open-ended nature of the answers generated by the Search Agent (Figure 3), we can’t
reliablyusetheexactmatchasametric. Instead,weeithermanuallyjudgecorrectnessorrunautoevalwithaseparatecalltothePaLM 2-L“base”model.

## 2 Auto-Eval

While strict human evaluations are preferable, they
aretime-consuming. Theyalsodon’tscalewell(do-
Question: What is the maximum airingonehumanevalismucheasierthandoingfive),
speed (in km/h) of the third fastest bird?
which leads to a high variance of such evals in our
case: the agent’s trajectories are stochastic (as a
reminder, we use non-zero temperature when samplingreasoningsteps),butwecan’teasilyreducethe

### Model Answer: The golden eagle

variancebyincreasingthenumberofrepetitionsper
is the third fastest bird. According
questionwithhumanevals.
to [link id=4, 5, 6], its maximum
We solve both of these problems by introducing airspeed is 200mph, which is 320kph.

### LLM-based auto-eval (the full auto-eval prompt is

availableintheAppendix,Listing7)andbyverifying its alignment with human ratings for the Bamboogle trajectories on which we previously con-

### Ground truth: 320 km/h

ducted human evals. We compared the auto-eval
with human evaluations on a diverse set of agents
and found it highly correlated with human evalua- Figure3: A Bamboogle question with an extion scores. Specifically, the Pearson correlation is ampleofthelongformanswerbythemodel
0.98 with p = 6.6 × 10−8 and Spearman correlationis0.83withp = 0.0015. Giventhatitismuch
cheapertorunauto-eval,wecannowusealargenumberofrepetitionstoreducevariance. Wetypicallyaggregateauto-evalovertenrepetitions(i.e., byproducingtendifferenttrajectoriesforeach
Bambooglequestion).
Firstandforemost,weuseBamboogleauto-evaltoestimatethefinalmodelperformancebutalsoto
answervariousquestionsthatonewouldtypicallyuseavalidationsetfor:
• Whatistheoptimalsamplingtemperaturefortheagent? (T =0.5)
• Whichcheckpointsshouldwechoosefordifferentmodelsizes? (step9KforXS,5KforS,
3.5KforL)
• Shouldweproceedwithanotheriterationofself-improvement?
• Whatistheperformanceimpactofusingseveraltrajectoriesperquestiononthefine-tuned
model?
• Shouldweuseself-checks? Aretheyhelpingorhurtingtheresults? (helpingslightly,see

### Figure4)

Importantly,weneveruseBamboogleasatrainingset,asweneithertuneourpromptsonBamboogle
norusequestionsfromittogeneratefine-tuningtrajectories.
5

<!-- Page 6 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent

## 3 Bamtwoogle


### Given the small size of Bamboogle and

our use of it as an analog of the validation set for Search Agent, there is a danger of overfitting. To guard against such
a possibility, we introduce a new dataset,
BamTwoogle, to serve as a test set. We
use BamTwoogle exclusively to measure
thefinalperformanceofthemodels.

### The BamTwoogle dataset was written to

be a complementary, slightly more challenging sequel to Bamboogle. It also addressessomeoftheshortcomingsofBamboogle we discovered while performing
humanevals. Specifically,weensuredthat Figure 4: Agent self-improvement and self-distillation,
all the questions required 2+ steps to an- with and without self-critique steps. Bamboogle autoswer. Due to changes in the search algo- eval, mean accuracy and standard deviation over ten
runs,(%)
rithm, this is no longer the case with all
Bambooglequestions,anditispossibleto
solvesomeofthemwithasinglesearch.
Like Bamboogle, BamTwoogle is a small (100 questions in total), handcrafted collection of
information-seekingquestions. Thetopicsandquestionformatsvary,butingeneral,BamTwoogle
adherestothefollowingguidelines

### Questions

• The majority of questions require two searches or reasoning steps (like Bamboogle), but
someofthemneed3or4
• Musthavebeenmanuallycheckedtoensuretheanswerdoesn’tappearonthefirstpageof
Googlesearchresults

### Expectedanswers

• Shouldnotbeambiguous
• Should not be prone to change over time, either due to the phrasing of the question or to
thenatureoftheanswer
• Shouldaccountformultipleversionsofpropernames,etc.,whereappropriate
• ShouldpreferWikipediaasthesourceoftruthforfacts(preferencegiventotopics/articles
notflaggedforincompleteness,lackofsources,etc.)

## 5 Experiments


## 1 Pilot

Alongside the main selfimprovement setup, described in Table 1: Agent self-improvement and self-distillation,
Section3,wealsogenerateasimpler Bamboogleauto-eval,meanaccuracyandstandardde-
“pilot” data with 500 trajectories, viationover10runs,(%)
where the initial questions are selected from HotpotQA and Eli5 TrainingData XS S L
datasets only (i.e., smaller and without Eli5-askH or Eli5-askS). We use Pre-trained N/A N/A 70.3±3.5
the default (based on a min perplex- Pilot,humanfiltered 44.7±3.1 56.6±3.8 71.5±2.2
ity, no RM re-ranking) best actions
Self-improvement,1stgen 54.4±3.6 61.9±1.9 74.0±3.3
for building the pilot’s fine-tuning
Self-improvement,2ndgen 65.9±2.6 69.7±1.3 76.1±1.3
mixture. Furthermore, we manually
6

<!-- Page 7 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent
review the fine-tuning data and filter
out about 30% of the examples that are ”bad” in some way: an unhelpful query, empty thoughts,
summarymissingimportantinformation,etc. Thispilotdataservesasafine-tuningbaseline.

## 2 Self-Improvementandself-Distillation

ThemainresultsarepresentedinFigure1andTable1.Asdiscussedpreviously,eachcellinthetable
showsamean(withthecorrespondingstd)ofauto-evalover10Bambooglerunsfortheparticular
model.
We start with a pretrained (prompted) PaLM Table2:Humanevals,BamboogleandBamTwoogle,acc(%)
2-L model and use it to
generate both 500 pilot

### Pre-trained(L) 2ndgen(XS) 2ndgen(S) 2ndgen(L)

trajectories and (independently) 2000 trajectories Bamboogle 68.8 67.2 68.0 74.4
for1stiteration(”1stgen”)
BamTwoogle 68.0 63.0 63.0 74.0
of self-improvement. We
thenfine-tunePaLM 2-L,
PaLM 2-S,andPaLM 2-XSmodelsontheresultingmixtures.
Next, weusethePaLM 2-Lmodelfine-tunedon1stgendatatogeneratetrajectoriesforthe2nd
iteration(”2ndgen”)ofself-improvement. Webuild2ndgendatawith8000trajectories(usingthe
same 2000 initial questions, each repeated four times; analogous to a ”grow” stage in ReST). As
previously,wefine-tunedeachofthethreemodelsonthenew2ndgenmixture.
Asafinalverification,wealsodohumanevalsoverasingleBamboogleandBamTwooglerunfor
each of the 2nd gen models (Table 2), as well as the original pre-trained PaLM 2-L model for
comparison.

## 3 Ablations

What is the effect of human filtering? Surprisingly, we have found that fine-tuning on filtered
data results in a small performance drop (2.5%) versus unfiltered pilot mixture (Table 3, pilot
columns). Wehypothesizethatthishappensduetoacombinationof2factors:
• Thereducedsizeofthefilteredmixturemakesitharderforthemodeltolearntheproper
formatoftheprompts,
• Our filtering only affects the immediate ”bad” example, not the whole trajectory; the
”bad” step would often be preserved in the other fine-tuning examples as part of the
PAST ACTIONSfield.
Shouldweusemultipletrajectoriesperquestion? Turnsout,ithelpstousetwotrajectoriesper
question instead of 1 (2.2% gain) in the fine-tuning mixture, but more than that doesn’t improve
performancesignificantly(Table3,2ndgencolumns).
Table3:Impactofthequalityandsizeofthetrainingdataforfine-tunedPaLM 2-XSmodels

### Pilot,human Pilot,

1stgen 2ndgen(1x) 2ndgen(2x) 2ndgen(4x)
filtered unfiltered
Totaltrajectories 500 500 2000 2000x1 2000x2 2000x4

### Trainingexamples 3015 4518 17970 18007 36238 72424

Bamboogleauto-eval 44.7±3.1 47.2±3.1 54.4±3.6 63.4±1.7 65.6±1.8 65.9±2.6
More data vs better data. From the same Table 3, we can conclude that the quality of the data
(e.g.,9%gain,whengoingfrom1stgento2ndgen(1x)whilekeepingthesizeofthedataroughly
thesame)mattersmorethanitsquantity. Notably,betterdataalsoreducesthevarianceofevaluation
trajectories.
7

<!-- Page 8 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent
Effectofself-critique. Themulti-stepsetupoftheagentallowsustoeasilymeasuretheeffectof
theself-critiquestepsontheoverallagentperformance.Todothis,wesimplytakealltheBamboogle
trajectories used for Table 1 and run auto-eval on them, but over the ”Answer Generation” step,
rather than over ”Final Answer”, as we normally do (Figure 2). As seen from Figure 4, the selfcritiqueresultsinasmallbutmeasurablepositiveboost(ontheorderof0.5-1.0%formostmodels).
ThedetailednumbersareprovidedinTable4intheAppendix.

## 6 Discussion

ProcessSupervision. It’simportanttoemphasizeagainthatwedon’tuselabelsfromthetraining
data as a signal during trajectory collection. This is possible due to combining a process-based
approach (i.e., defining agent as a state machine) with high-temperature exploration, AI feedback
(zero-shot”reward”modelusedforactionsre-ranking), andstate-wisefine-tuningovercompleted
trajectories. In other words, in this setup, the model can learn something useful even from the
states that eventually lead to the wrong final answer. More importantly, it learns to handle openendedquestionsthatdon’thaveasinglewell-definedcorrectanswerinthefirstplace,akintomany
questionsfromEli5.
Auto-Eval. Someofthepropertieslistedabove,likenon-greedysamplingandlong-formanswer
generations in particular, bring with them additional challenges in terms of agent evaluation. We
bothneedtomeasurethequalityofthelong-formfinalanswerforaspecifictrajectoryandaccount
for stochasticity between different agent trajectories for the same input. This, on the one hand,
elevatesthevalueofhavingrobustauto-evalalignedwithhumanratersand,ontheother,increases
thecomputationalcostssignificantlyduetotheneedtorunagenttrajectoriesmultipletimes,aswell
astheuseofPaLM 2-Lmodelforauto-eval.
Self-Critique. Despite those computational costs, multiple benefits come from having reliable
auto-eval in terms of measuring the impact of various agent’s hyperparameters. As an example,
let’sconsidertheself-critiquesteps. Withtheaidofauto-eval, wewereabletoestablishthatthey
haveasmallbutpositiveeffectontheoverallperformanceofourmulti-stepreasoningsetup. This
contraststherecentobservations(Huangetal.,2023)thataddingself-critiquehurtstheperformance
in an outcome-based CoT setup. Simultaneously, we can also notice that a positive effect of selfcritiquedependsonthemodelsize(largerforlargermodels)butdoesnotseemtobeaffectedbythe
self-improvementprocess.
Limitations and Future Directions. While this work lays a foundation for reasoning agents’
self-improvement,ithasnumerouslimitationsduetocomputationalandtimeconstraints: manually
constructedprompts,smallevals,alimitedsetofmodels,andonlyasingletool,tonamejustafew.
Futureworkcouldexploreifthesameself-improvementalgorithmappliestomultipletoolsettings
and,especially,iftheabilitytohandleunseentoolscouldbeimprovedinsuchaway. Ifthelatteris
moresimilartoself-critiqueanddoesn’timproveunderReST-likeiterativetraining,whatchanges
arerequiredtoenableself-improvementforboth?
Another open question is a saturation point. How many additional iterations of self-improvement
can we undertake past the 2nd one that still results in non-trivial gains? What does the saturation
looklikeforsmallermodels? Willtheyalleventuallyconvergetothesameperformance,orwillthe
smallermodelsalwaysbecappedbytheperformanceoftheinitialpromptedlargemodel?

## 7 Related Work

FollowingWebGPT(Nakanoetal.,2021),wearetacklingthetaskoflong-formquestionanswering
(Krishna et al., 2021), in which the language agent uses web search as a tool to generate final
answerswithexplicitreferencesfortheretrievedpassages. WhileWebGPTisfocusedonimitation
learningandRLfromalargenumberofhumandemonstrations,ourworkaimstominimizehuman
involvement. Theonlylabeleddemonstrationsweuseaspartofthetrainingarefew-shotexemplars
inthepromptsfortheagent’sreasoningsteps(seeAppendix,A.1).
8

<!-- Page 9 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent
Settinguplanguageagentswithmanuallydesignedfew-shotpromptsisthemostcommonpractice
(Pressetal.(2023);Yaoetal.(2022);Shinnetal.(2023)),buttherearesomeexceptions. Forexample, DSP (Khattab et al., 2023a) tunes the few-shot demonstrations for the prompts automatically,
leveraging some amount of labeled training examples for optimization purposes, and can further
fine-tunespecificcomponentsoftheagent.
Unlike prompting, agent’s fine-tuning is done less often (Nakano et al. (2021); Yao et al. (2022);
Chen et al. (2023)). The closest to our fine-tuning setup is probably FireAct (Chen et al., 2023),
withthemaindifferencebeingthatwedon’tusehumanlabelsfortrainingordatafiltering. Instead,
wearebuildingsyntheticdatawithself-improvementfromAIfeedback.
Somerelevantpapersforself-improvementincludeSTAR(Zelikmanetal.,2022),ReST(Gulcehre
et al., 2023), ReSTEM (Singh et al., 2023), and RAFT (Dong et al., 2023). Unlike STAR and
ReSTEM,wedon’tusethecorrectnessoftheanswerasasignal. And,unlikeReSTandRAFT,we
don’thavetheproperrewardmodeltrainedonhumanpreferences. Moreover,all4ofthesepapers
targetoutcome-basedsystems,whilewefocusonaprocess-basedone.

## 8 Conclusion

ThisworkdemonstratesthattheReST-likeapproachwithAIfeedbackcouldbeeffectivelyapplied
to a multi-step reasoning LLM agent. We show that it is a relatively simple and efficient way to
iterativelybuildhigh-qualitysyntheticdataforagentself-improvement. Moreover,thisincreasingly
higherqualitydatacouldsimultaneouslybeusedfordistillingamulti-stepagentintoseveralmagnitudessmallermodelswhilepreservingmostoftheperformancefromthelargeteachermodel.

## References

Rohan Anil, Andrew M Dai, Orhan Firat, Melvin Johnson, Dmitry Lepikhin, Alexandre Passos,
Siamak Shakeri, Emanuel Taropa, Paige Bailey, Zhifeng Chen, et al. Palm 2 technical report.
arXivpreprintarXiv:2305.10403,2023.
Vladimir Blagojevic. Long-form qa beyond eli5: an updated
dataset and approach, 2022. URL towardsdatascience.com/
long-form-qa-beyond-eli5-an-updated-dataset-and-approach-319cb841aabb.
HarrisonChase. Langchain. https://github.com/hwchase17/langchain,2022.
Baian Chen, Chang Shu, Ehsan Shareghi, Nigel Collier, Karthik Narasimhan, and Shunyu Yao.
Fireact: Towardlanguageagentfine-tuning,2023.
DavidDohan,WinnieXu,AitorLewkowycz,JacobAustin,DavidBieber,RaphaelGontijoLopes,
Yuhuai Wu, Henryk Michalewski, Rif A. Saurous, Jascha Sohl-dickstein, Kevin Murphy, and
CharlesSutton. Languagemodelcascades,2022.
Hanze Dong, Wei Xiong, Deepanshu Goyal, Yihan Zhang, Winnie Chow, Rui Pan, Shizhe Diao,
Jipeng Zhang, Kashun Shum, and Tong Zhang. Raft: Reward ranked finetuning for generative
foundationmodelalignment,2023.
AngelaFan,YacineJernite,EthanPerez,DavidGrangier,JasonWeston,andMichaelAuli. ELI5:
long form question answering. CoRR, abs/1907.09190, 2019. URL http://arxiv.org/
abs/1907.09190.
LuyuGao, AmanMadaan, ShuyanZhou, UriAlon, PengfeiLiu, YimingYang, JamieCallan, and
GrahamNeubig. Pal: Program-aidedlanguagemodels,2023.
CaglarGulcehre,TomLePaine,SrivatsanSrinivasan,KseniaKonyushkova,LotteWeerts,Abhishek
Sharma,AdityaSiddhant,AlexAhern,MiaosenWang,ChenjieGu,etal.Reinforcedself-training
(rest)forlanguagemodeling. arXivpreprintarXiv:2308.08998,2023.
JieHuang,XinyunChen,SwaroopMishra,HuaixiuStevenZheng,AdamsWeiYu,XinyingSong,
andDennyZhou. Largelanguagemodelscannotself-correctreasoningyet,2023.
9

<!-- Page 10 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent
Omar Khattab, Keshav Santhanam, Xiang Lisa Li, David Hall, Percy Liang, Christopher Potts,
and Matei Zaharia. Demonstrate-search-predict: Composing retrieval and language models for
knowledge-intensivenlp,2023a.
OmarKhattab,ArnavSinghvi,ParidhiMaheshwari,ZhiyuanZhang,KeshavSanthanam,SriVardhamanan,SaifulHaq,AshutoshSharma,ThomasT.Joshi,HannaMoazam,HeatherMiller,Matei
Zaharia, and Christopher Potts. Dspy: Compiling declarative language model calls into selfimprovingpipelines,2023b.
KalpeshKrishna,AurkoRoy,andMohitIyyer.Hurdlestoprogressinlong-formquestionanswering,
2021.
Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan
Leike,JohnSchulman,IlyaSutskever,andKarlCobbe. Let’sverifystepbystep,2023.
JerryLiu. Llamaindex. https://github.com/jerryjliu/llama_index,2022.
Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri
Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad
Majumder,KatherineHermann,SeanWelleck,AmirYazdanbakhsh,andPeterClark. Self-refine:
Iterativerefinementwithself-feedback,2023.
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, ChristopherHesse,ShantanuJain,VineetKosaraju,WilliamSaunders,etal. Webgpt: Browser-assisted
question-answeringwithhumanfeedback. arXivpreprintarXiv:2112.09332,2021.
OfirPress,MuruZhang,SewonMin,LudwigSchmidt,NoahA.Smith,andMikeLewis.Measuring
andnarrowingthecompositionalitygapinlanguagemodels,2023.
JustinReppert,BenRachbach,CharlieGeorge,LukeStebbing,JungwonByun,MaggieAppleton,
andAndreasStuhlmu¨ller. Iterateddecomposition:Improvingscienceq&abysupervisingreasoningprocesses,2023.
NoahShinn, BeckLabash, andAshwinGopinath. Reflexion: anautonomousagentwithdynamic
memoryandself-reflection. arXivpreprintarXiv:2303.11366,2023.
AviSingh, JohnD.Co-Reyes, RishabhAgarwal, AnkeshAnand, PiyushPatil, PeterJ.Liu, James
Harrison,JaehoonLee,KelvinXu,AaronParisi,AbhishekKumar,AlexAlemi,AlexRizkowsky,
AzadeNova,BenAdlam,BerndBohnet,GamaleldinElsayed,HanieSedghi,IgorMordatch,Isabelle Simpson, Izzeddin Gur, Jasper Snoek, Jeffrey Pennington, Jiri Hron, Kathleen Kenealy,
Kevin Swersky, Kshiteej Mahajan, Laura Culp, Lechao Xiao, Maxwell L. Bileschi, Noah Constant,RomanNovak,RosanneLiu,TrisWarkentin,YundiQian,EthanDyer,BehnamNeyshabur,
JaschaSohl-Dickstein,andNoahFiedel. Beyondhumandata: Scalingself-trainingforproblemsolvingwithlanguagemodels,2023.
JonathanUesato,NateKushman,RamanaKumar,FrancisSong,NoahSiegel,LisaWang,Antonia
Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process- and
outcome-basedfeedback,2022.
Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, Rui Zheng, Xiaoran Fan, Xiao Wang, Limao Xiong, Yuhao
Zhou,WeiranWang,ChanghaoJiang,YichengZou,XiangyangLiu,ZhangyueYin,ShihanDou,
RongxiangWeng,WensenCheng,QiZhang,WenjuanQin,YongyanZheng,XipengQiu,XuanjingHuang,andTaoGui. Theriseandpotentialoflargelanguagemodelbasedagents: Asurvey,
2023.
ZhilinYang,PengQi,SaizhengZhang,YoshuaBengio,WilliamW.Cohen,RuslanSalakhutdinov,
and Christopher D. Manning. Hotpotqa: A dataset for diverse, explainable multi-hop question
answering. CoRR,abs/1809.09600,2018. URLhttp://arxiv.org/abs/1809.09600.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.
React: Synergizingreasoningandactinginlanguagemodels. arXivpreprintarXiv:2210.03629,
2022.
10

<!-- Page 11 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent
EricZelikman,YuhuaiWu,JesseMu,andNoahD.Goodman. Star: Bootstrappingreasoningwith
reasoning,2022.

## A Appendix


## A.1 Prompts

Reasoningsteps. Allourreasoningpromptsaren-shot(withn > 1),thoughweonlyshowfragments,limitedtothefirstexemplar:
• ThedecisionsteppromptisshowninListing1(thefullpromptis9-shot).
• ThesummarizationpromptispresentedinListing2(thefullpromptis6-shot).
• Theanswergenerationpromptis5-shot,Listing3showsa1-shotfragment.
• Thepromptforrelevanceself-checkispresentedinListing5(thefullpromptis6-shot).
• Finally, the prompt for grounding self-check is shown in Listing 6 (the full prompt is
5-shot).
• Bothself-checksusethecommonprefixfromListing4.
Auto-eval. Thefull5-shotpromptforauto-evalispresentedinListing7.
Ranking”Reward”Model. ThefullpromptoftherewardmodelisshowninListing8. Notice
that this is the only prompt that is 0-shot and doesn’t use ”code as the prompt” approach, as it’s
intendedtobeusedwithaninstruction-tunedmodel.

## A.2 Additionaldata

Table4:Agentself-improvementandself-distillation,Bamboogleauto-eval,meanaccuracyandstandarddeviationover10runs,(%). Evaluationbeforeself-critiquesteps

## Xs S L


### Pre-trained N/A N/A 69.5±2.8(-0.8)

Pilot,humanfiltered 44.3±3.0(-0.4) 54.4±4.1(-2.2) 70.9±3.0(-0.6)
Self-improvement,1stgen 54.8±3.7(+0.4) 61.2±2.5(-0.7) 73.1±3.0(-0.9)
Self-improvement,2ndgen 65.6±3.0(-0.3) 69.2±1.8(-0.5) 75.0±1.3(-1.1)
11

<!-- Page 12 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent

### Listing1:Decisionstepprompt(fragment)

"""Implement an agent capable of answering complex queries by potentially search multiple
times.
"""
import dataclasses
class Action:
"""Base class for different actions."""
...
@dataclasses.dataclass
class ActionWrapper:
"""Encapsulates the reasoning as well as the selected action.

### Attributes:

thoughts: Record your thoughts on why we should do this action.
action: The actually selected action.
"""
thoughts: str
action: Action
@dataclasses.dataclass
class Search(Action):
"""The Google search command.

### Attributes:

query: The query to be sent to Google.
"""
query: str
@dataclasses.dataclass
class Terminate(Action):
"""Command to terminate the search sequence."""
...
#########################
# Example 1:
#########################
ORIGINAL_QUESTION: str = ’I want to buy the Ikea Klippan loveseat, but I\’m not sure whether
it can fit into my 2019 Honda Odyssey. Could you check whether I need to fold down the
seat?’

### PAST_ACTIONS: List[Action] = [


### Search(query=’ikea klippan loveseat dimension’,

thoughts="To answer the ORIGINAL_QUESTION, we need to find the size of the Ikea Klippan
loveseat and the cargo size of the 2019 Honda Odyssey, and then compare them. Let’s start
by finding the size of the Ikea Klippan loveseat.",
),

### SelectLink(selected_links=[

ResultItem(link_id=1, link_text=’KLIPPAN Loveseat, Vissle gray - IKEA’,
snippet=’<lh> Measurements </lh> <ul> <li> Width: 70 7/8 &quot; </li> <li> Depth:
34 5/8 &quot; </li> <li> Height: 26 &quot; </li> <li> Height under
furniture: 4 3/8 &quot; </li> <li> Seat depth: 21 1/4 &quot; </li> <li> Seat
height: 16 7/8 &quot; </li> </ul>’),],
grounded_summarization=’According to [link_id=1] the dimension of the ikea klippan loveseat is

### Width: 70 7/8"; Depth: 34 5/8"; Height: 26".’,

thoughts="We still need to find the cargo size of the 2019 Honda Odyssey to answer the

## Original_Question.",

),
]

### REMAINING_SEARCHES: int = 4

ORIGINAL_QUESTION: str = ’I want to buy the Ikea Klippan loveseat, but I\’m not sure whether
it can fit into my 2019 Honda Odyssey. Could you check whether I need to fold down the
seat?’
ACTION_SELECTED = ActionWrapper(thoughts="The past result gives us the dimension of the love
seat. We indeed need to find the cargo size of the 2019 Honda Odyssey.", action=Search(
query=’2019 Honda Odyssey cargo size’)) # [END]
#########################
# Example 2:
#########################
12

<!-- Page 13 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent

### Listing2:Summarizationprompt(fragment)

"""Implementing step 2 of Search and Answer procedure: Search result filtering and
summarization.
"""
#########################
# Example 1:
#########################
ORIGINAL_QUESTION: str = "What’s the efficiency of the solar panels on the garden solar lights
?"

### PAST_ACTIONS: List[Action] = [


### Search(query=’garden solar light panel efficiency’,

thoughts="Let’s just rephrase the search query a bit. The intention of the original question
is pretty clear.",
),
]

### CURRENT_SEARCH_RESULTS = SearchResult(links=[

ResultItem(link_id=17, link_text=’Use Solar Outdoor Lighting for Energy Efficiency - Sepco

### Solar’,

snippet=’Depending on the type of lighting you install and the wattage of the
fixtures, this can eat up a budget quickly. Instead, going with a solar
outdoor lighting system to provide the required light can greatly reduce the
project costs, help improve the environment, and keep electrical costs in
the bank where it belongs.’),
ResultItem(link_id=18, link_text=’How Do Solar Garden Lights Work? - The OutdoorLights Store
’,
snippet=’The solar panel converts solar energy into electricity<br><br> The
energy absorbed by the photovoltaic cells in the panel creates electrical
charges. These charges move in response to an electrical field in the solar
panel&#39;s cells, which ultimately causes electricity to flow.’),
ResultItem(link_id=19, link_text=’10 things you should know about the garden solar lights’,
snippet=’The solar panels are generally made from two types of cells,
monocrystalline or polycrystalline. Both of them are low cost, however,
different panel technology can lead to different efficiency under different
conditions.’),
])
ORIGINAL_QUESTION: str = "What’s the efficiency of the solar panels on the garden solar lights
?"
# [link_id=17] is an article about garden solar light, which doesn’t have anything specific
about the solar panels. Not selected.
# [link_id=18] is an article on how to best install those solar lights. Not relevant to the
solar panels used. Not selected.
ACTION_SELECTED: LinkSelection = LinkSelection(grounded_summarization=’According to [link_id
=19], there are two types of solar cells used for garden solar lights, the
monocrystalline or polycrystalline panels.’, thoughts="It seems like non of the links
shows the efficiency number. However, link 19 provides some hints on what to search next.
We can look into the efficiency number of those two types of panels.", selected_link_ids

## =[19]) # [End]

#########################
# Example 2:
#########################
13

<!-- Page 14 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent

### Listing3:Answergenerationprompt(fragment)

"""Implementing step 3 of the multi-round search agent: Answer generation based on all the
collected search results.
"""
#########################
# Example 1:
#########################
ORIGINAL_QUESTION: str = "What’s the white powdery residual often found on a humidifier?"

### PAST_ACTIONS: List[Action] = [


### Search(query=’what is humidifier’,

thoughts="Let’s solve this step by step. The person is asking about the residual found in
humidifier. Let’s first define what does humidifier do.",
),

### SelectLink(selected_links=[

ResultItem(link_id=1, link_text=’Humidifiers: What They Do for Health, Uses, Types, and More
’,
snippet=’What is a humidifier? Humidifiers are devices that add moisture to the
air to prevent dryness that can cause irritation in many parts of the body.
Humidifiers can be particularly effective for treating dryness of the skin,
nose, throat, and lips. They can also ease some symptoms caused by the flu
or common cold.’),
ResultItem(link_id=3, link_text=’5 humidifier uses: Benefits and risks - Medical News Today’
,
snippet=’We do the research so you can find trusted products for your health and
wellness. Read more about our vetting process. Humidifiers add moisture to
the air, which can benefit people with respiratory symptoms or dry skin.
There are several ways to use humidifiers in the home or office, but there
are also some risks.’),],
grounded_summarization=’According to [link_id=1] and [link_id=3], humidifier is a device that
adds moisture to the air to prevent dryness that can cause irritation in many parts of
the body.’),
thoughts="Now that we know what humidifier is, we can look into the white powdery residual.",
),

### Search(query=’white powdery residual in humidifier’,

thoughts="Let’s now look into the white powdery residual.",
),

### SelectLink(selected_links=[

ResultItem(link_id=10, link_text=’What is white dust and should I be concerned about it? -

### HVAC.com’,

snippet=’White dust is usually caused by mineral content in the water that goes
into a humidifier. When the mist lands on furniture or other surfaces and
dries, it can sometimes leave behind dried mineral deposits, or "white dust
."’),
link_text=’What is white dust and should I be concerned about it? - HVAC.com’,
snippet=’White dust is usually caused by mineral content in the water that
goes into a humidifier. When the mist lands on furniture or other surfaces
and dries, it can sometimes leave behind dried mineral deposits, or "white
dust."’)
ResultItem(link_id=11, link_text=’Why is White Dust Coming Out of My Humidifier?’,
snippet=’The white dust that you are finding on surfaces around your home is
likely dried-up minerals from water vapor created by the humidifier. These
minerals are natural in our home water supply. If you&#39;ve ever heard of
the term "hard water," it&#39;s referring to water with high levels of
calcium and magnesium.’),],
grounded_summarization=’According to [link_id=10], and [link_id=11], the white powdery
residual is caused by the mineral content in the water.’),
thoughts="We have all the information to answer the question.",
),
Terminate(thoughts="We have all the information to answer the question."),
]
ORIGINAL_QUESTION: str = "What’s the white powdery residual often found on a humidifier?"
ACTION_SELECTED: Answer = Answer(thoughts="The first search (’what is humidifier’) is probably
not what the questioner cares, so let’s omit that in the answer. We can focus more on
the question itself.", answer="The white powdery residue in the humidifier is usually
caused by mineral content in the water, according to [link_id=10]. For example, water may
contain high levels of calcium and magnesium [link_id=11].") # [END]
#########################
# Example 2:
#########################
14

<!-- Page 15 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent

### Listing4:Self-checkprompt(prefix)

"""Check whether the ANSWER addresses the ORIGINAL_QUESTION and whether the ANSWER is based on

### SelectLinks in PAST_ACTIONS."""

from dataclasses import dataclass
from typing import List, Tuple
class Action:
"""Base class for different actions."""
class Check_Answer(Action):
"""Check whether the ANSWER addresses the ORIGINAL_QUESTION."""
def __init__(self, passed: bool) -> None:
self.passed = passed
class Revise_Answer(Action):
"""Revise the answer if it did not pass the check, based on information from SelectLinks in

## Past_Actions."""

def __init__(self, revised_answer: str) -> None:
self.revised_answer = revised_answer
...
@dataclasses.dataclass
class ResultItem:
"""Single search result, with link id, link title and snippet.

### Attributes:

link_id: A unique integer id of this link.
link_text: The title of the link.
snippet: The snippet from the page that’s relevant to the query
"""
link_id: int
link_text: str
snippet: str
15

<!-- Page 16 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent
Listing5:Relevanceself-check(fragment)
#########################
# Example 1:
#########################
ORIGINAL_QUESTION: str = ’How to exclude a website from Google search’

### PAST_ACTIONS: List[Action] = [


### Search(query=’exclude site in google search’,

thoughts="We simply the ORIGINAL_QUESTION to a good search query.",
),

### SelectLink(selected_links=[

ResultItem(link_id=2, link_text=’How to Exclude a Website from Google Search Results -

### Keyword’,

snippet="You can exclude a domain or even a specific page from appearing on

### Google search results. Here’s how ..."),

ResultItem(link_id=3, link_text=’How do I exclude/block specific web sites from search
results?’),
snippet="In the absence of a browser extension, the simplest way is to add -site:
website_name after your search terms. ... I can’t get rid of books.google.
com results. I’ ..."),
ResultItem(link_id=6, link_text="Q&A: Can you exclude a specific website from Google’s
search results?"),
snippet=’Jul 31, 2022 . All you have to do is simply append -site:pinterest.com
to the end of your search query. For example, if you were searching for the
term "paper ...’),
],
grounded_summarization=’[link_id=3] mentions that we can add -site:website_name to the google
search query to exclude a website. [link_id=6] provides an example.’),
thoughts="We found enough info for a good answer to the ORIGINAL_QUESTION.",
),
Terminate(thoughts="This is a good answer to the question.")
Answer(thoughts="We summarize the relevant info found in PAST_ACTIONS.", answer="To exclude a
website from Google search result, you can add -site:website_name after your search terms
according to [link_id=3]. For example, if you want to exclude pinterest.com, you can
simply add -site:pinterest.com according to [link_id=6].")
]
ORIGINAL_QUESTION: str = ’How to exclude a website from Google search’
ANSWER: str = ’To exclude a website from Google search result, you can add -site:website_name
after your search terms according to [link_id=3]. For example, if you want to exclude
pinterest.com, you can simply add -site:pinterest.com according to [link_id=6].’
# The ANSWER is directly addressing the ORIGINAL_QUESTION.
# The ANSWER refers to [link_id=3] which correctly supports the core statement of adding -site
:website_name. The example from the answer is indeed from [link_id=6].
ACTION_SELECTED: Command = Check_Answer(passed=True) # [END]
#########################
# Example 2:
#########################
16

<!-- Page 17 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent
Listing6:Groundingself-check(fragment)
#########################
# Example 1:
#########################
ORIGINAL_QUESTION: str = "What did Jim Betts’ competitor in the 1980 election achieve in 1962?
"

### PAST_ACTIONS: List[Action] = [


### Search(query=’who was Jim Betts competitor in 1980’,

thoughts="This question is asking about the achievement of Jim Betts’ competitor in 1962. Let’
s first search for who this competitor is.",
),

### SelectLink(selected_links=[

ResultItem(link_id=1, link_text=’Jim Betts (politician) - Wikipedia’,
snippet=’Jim Betts is a former member of the Ohio House of Representatives. He
ran against incumbent U.S. Senator John Glenn in 1980. He lost and ran in
1982 for lieutenant governor.’),],
grounded_summarization="According to [link_id=1], Jim Betts’ competitor in 1980 was John Glenn
."),
thoughts="Now that we know who the competitor is, we can search for his achievements in 1962."
,
),

### Search(query=’John Glenn achievements 1982’,

thoughts="Now that we know who the competitor is, we can search for his achievements in 1982."
,
),
SelectLink(selected_links=[
],
grounded_summarization=’Nothing is selected.’),
thoughts="The query ’John Glenn achievements 1982’ is not very good. It should be ’John Glenn
achievements 1962’.",
),

### Search(query=’John Glenn achievements 1962’,

thoughts="John Glenn is the person we are looking for. Let’s change the date to 1962.",
),

### SelectLink(selected_links=[

ResultItem(link_id=19, link_text=’John Glenn | Biography, Accomplishments, & Facts |

### Britannica’,

snippet="Glenn, Jr., (born July 18, 1921, Cambridge, Ohio, U.S.-died December 8,
2016, Columbus, Ohio), the first U.S. astronaut to orbit Earth, completing
three orbits in 1962. (Soviet cosmonaut Yuri Gagarin, the first person in
space, had made a single orbit of Earth in 1961.) Glenn joined the U.S.

### Naval Reserve in 1942."),],

grounded_summarization="According to [link_id=19], John Glenn’s achievement in 1962 was to
become the first American to orbit the Earth."),
thoughts="We have all the information to answer the question.",
),
Terminate(thoughts="We have all the information we need to answer the ORIGINAL_QUESTION. Let’s
stop searching and answer the question.")
Answer(thoughts="We have the answer to the question.", answer="Jim Betts\’ competitor in the
1980 election was John Glenn. And John Glenn\’s achievement in 1962 was to become the
first American to orbit the Earth.")
]
ORIGINAL_QUESTION: str = "What did Jim Betts’ competitor in the 1980 election achieve in 1962?
"
ANSWER: str = ’Jim Betts\’ competitor in the 1980 election was John Glenn [link_id=1]. And
John Glenn\’s achievement in 1962 was to become the first American to orbit the Earth [
link_id=19].’
# ANSWER directly addresses the ORIGINAL_QUESTION.
# [link_id=1] indeed says that Jim Betts\’ run against John Glenn in 1980, consistent with

## Answer.

# [link_id=19] indeed says John Glenn is the first US astronaut to orbit the earth, consistent
with ANSWER.
ACTION_SELECTED: Command = Check_Answer(passed=True) # [END]
#########################
# Example 2:
#########################
17

<!-- Page 18 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent

### Listing7:Auto-eval(fullprompt)

"""Check whether the ANSWER implies the REF_ANSWER to the question."""
def Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER):
"""Check whether the ANSWER implies the REF_ANSWER."""
# todo
#########################
# Example 1:
#########################
ORIGINAL_QUESTION: str = ’Are McIntyre Mines and Copperfields Mine in the same country?’
ANSWER: str = ’According to [link_id=1], Copperfields Mine is in Ontario, Canada. According to
[link_id=4], McIntyre Mines is also in Ontario, Canada. So yes, they are in the same
country.’

### REF_ANSWER: str = ’yes’

# the ANSWER implies the answer to the original question is yes, this is consistent with the

## Ref_Answer.

Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER) = True # [END]
#########################
# Example 2:
#########################
ORIGINAL_QUESTION: str = ’Which Director, James Richard Kelly or Paul L. Stein has a list of
67 films to his credit? ’
ANSWER: str = ’According to [link_id=1] and [link_id=2], James Richard Kelly has 5 films to
his credit.’
REF_ANSWER: str = ’Paul Ludwig Stein (4 February 1892 - 2 May 1951) was an Austrian-born film
director with 67 films to his credit.’
# the ANSWER does not imply the REF_ANSWER because ANSWER does not mention Paul Ludwig Stein.
Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER) = False # [END]
#########################
# Example 3:
#########################
ORIGINAL_QUESTION: str = ’Are the genuses Michelia and Stenomesson in the same family?’
ANSWER: str = ’Based on the information we have, we are not sure whether the genuses Michelia
and Stenomesson are in the same family [link_id=3] does not contain this information.’

### REF_ANSWER: str = ’no’

# The ANSWER did not determine whether or not Michelia and Stenomesson are in the same family.
# The REF_ANSWER implies that they are not in the same family.
# Thus we cannot infer the REF_ANSWER given the ANSWER.
Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER) = False # [END]
#########################
# Example 4:
#########################
ORIGINAL_QUESTION: str = ’In what year was the winner of the 44th edition of the Miss World
competition born?’
ANSWER: str = ’According to [link_id=2], the winner of the 44th edition of the Miss World
competition is Aishwarya Rai.\nAccording to [link_id=4], she was born in 1973.’

### REF_ANSWER: str = ’1973’

# The ANSWER implies 1973 as the final answer to ORIGINAL_QUESTION.
# REF_ANSWER implies 1973 as the final answer to ORIGINAL_QUESTION, too.
Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER) = True # [END]
#########################
# Example 5:
#########################
ORIGINAL_QUESTION: str = ’Skull & Bones is a mini-series by a man that is an editor of what
two comics?’
ANSWER: str = ’The question is ill-formed or out-of-date. We should ask for clarification from
the asker.’

### REF_ANSWER: str = ’Marvel Comics and DC Comics’

# The ANSWER did not provide any answer to ORIGINAL_QUESTION.
Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER) = False # [END]
#########################
# Example 6:
#########################
18

<!-- Page 19 -->

ReSTmeetsReAct: Self-ImprovementforMulti-StepReasoningLLMAgent
Listing8:Rewardmodel(fullprompt)
"""Rater Instructions:
- The goal of this rating is to filter out bad actions, so that they’ll be excluded from the
fine-tuning dataset.
- Overall, we want to the agent to produce relevant and grounded answers with minimal steps.
Anything that deviates from this goal is considered bad.
- If any element (thoughts, comments etc.) is empty, then it’s automatically bad.
#########################################
*** Model Can See:
‘‘‘
{inputs}
‘‘‘
*** Model Output #1:
‘‘‘
{action1}
‘‘‘
*** Model Output #2:
‘‘‘
{action2}
‘‘‘
*** Model Output #3:
‘‘‘
{action3}
‘‘‘
*** Model Output #4:
‘‘‘
{action4}
‘‘‘
#########################################

### Your Instructions:

- Choose the best model output based on the rater’s instructions.
- Don’t assume in your decision that the model knows anything outside of "Model Can See"
section.
- Be specific in your explanation.
Output 3 lines when answering and make sure to follow the precise format.
Explanation: why you think model output #X is the best

### Answer: #X

Ranking: #X > #Y > ...
"""
19

## Tables

**Table (Page 12):**

|  |
|---|
| """Implement an agent capable of answering complex queries by potentially search multiple |
| times. |
| """ |
| import dataclasses |
|  |
|  |
| class Action: |
| """Base class for different actions.""" |
| ... |
|  |
|  |
| @dataclasses.dataclass |
| class ActionWrapper: |
| """Encapsulates the reasoning as well as the selected action. |
|  |
| Attributes: |
| thoughts: Record your thoughts on why we should do this action. |
| action: The actually selected action. |
| """ |
| thoughts: str |
| action: Action |
|  |
| @dataclasses.dataclass |
| class Search(Action): |
| """The Google search command. |
|  |
| Attributes: |
| query: The query to be sent to Google. |
| """ |
| query: str |
|  |
|  |
| @dataclasses.dataclass |
| class Terminate(Action): |
| """Command to terminate the search sequence.""" |
| ... |
|  |
|  |
| ######################### |
| # Example 1: |
| ######################### |
|  |
| ORIGINAL_QUESTION: str = ’I want to buy the Ikea Klippan loveseat, but I\’m not sure whether |
| it can fit into my 2019 Honda Odyssey. Could you check whether I need to fold down the |
| seat?’ |
| PAST_ACTIONS: List[Action] = [ |
| Search(query=’ikea klippan loveseat dimension’, |
| thoughts="To answer the ORIGINAL_QUESTION, we need to find the size of the Ikea Klippan |
| loveseat and the cargo size of the 2019 Honda Odyssey, and then compare them. Let’s start |
| by finding the size of the Ikea Klippan loveseat.", |
| ), |
| SelectLink(selected_links=[ |
| ResultItem(link_id=1, link_text=’KLIPPAN Loveseat, Vissle gray - IKEA’, |
| snippet=’<lh> Measurements </lh> <ul> <li> Width: 70 7/8 &quot; </li> <li> Depth: |
| 34 5/8 &quot; </li> <li> Height: 26 &quot; </li> <li> Height under |
| furniture: 4 3/8 &quot; </li> <li> Seat depth: 21 1/4 &quot; </li> <li> Seat |
| height: 16 7/8 &quot; </li> </ul>’),], |
| grounded_summarization=’According to [link_id=1] the dimension of the ikea klippan loveseat is |
| Width: 70 7/8"; Depth: 34 5/8"; Height: 26".’, |
| thoughts="We still need to find the cargo size of the 2019 Honda Odyssey to answer the |
| ORIGINAL_QUESTION.", |
| ), |
| ] |
| REMAINING_SEARCHES: int = 4 |
| ORIGINAL_QUESTION: str = ’I want to buy the Ikea Klippan loveseat, but I\’m not sure whether |
| it can fit into my 2019 Honda Odyssey. Could you check whether I need to fold down the |
| seat?’ |
|  |
| ACTION_SELECTED = ActionWrapper(thoughts="The past result gives us the dimension of the love |
| seat. We indeed need to find the cargo size of the 2019 Honda Odyssey.", action=Search( |
| query=’2019 Honda Odyssey cargo size’)) # [END] |
|  |
| ######################### |
| # Example 2: |
| ######################### |
|  |


**Table (Page 13):**

|  |
|---|
| """Implementing step 2 of Search and Answer procedure: Search result filtering and |
| summarization. |
| """ |
|  |
| ######################### |
| # Example 1: |
| ######################### |
|  |
| ORIGINAL_QUESTION: str = "What’s the efficiency of the solar panels on the garden solar lights |
| ?" |
| PAST_ACTIONS: List[Action] = [ |
| Search(query=’garden solar light panel efficiency’, |
| thoughts="Let’s just rephrase the search query a bit. The intention of the original question |
| is pretty clear.", |
| ), |
| ] |
| CURRENT_SEARCH_RESULTS = SearchResult(links=[ |
| ResultItem(link_id=17, link_text=’Use Solar Outdoor Lighting for Energy Efficiency - Sepco |
| Solar’, |
| snippet=’Depending on the type of lighting you install and the wattage of the |
| fixtures, this can eat up a budget quickly. Instead, going with a solar |
| outdoor lighting system to provide the required light can greatly reduce the |
| project costs, help improve the environment, and keep electrical costs in |
| the bank where it belongs.’), |
| ResultItem(link_id=18, link_text=’How Do Solar Garden Lights Work? - The OutdoorLights Store |
| ’, |
| snippet=’The solar panel converts solar energy into electricity<br><br> The |
| energy absorbed by the photovoltaic cells in the panel creates electrical |
| charges. These charges move in response to an electrical field in the solar |
| panel&#39;s cells, which ultimately causes electricity to flow.’), |
| ResultItem(link_id=19, link_text=’10 things you should know about the garden solar lights’, |
| snippet=’The solar panels are generally made from two types of cells, |
| monocrystalline or polycrystalline. Both of them are low cost, however, |
| different panel technology can lead to different efficiency under different |
| conditions.’), |
| ]) |
| ORIGINAL_QUESTION: str = "What’s the efficiency of the solar panels on the garden solar lights |
| ?" |
|  |
| # [link_id=17] is an article about garden solar light, which doesn’t have anything specific |
| about the solar panels. Not selected. |
| # [link_id=18] is an article on how to best install those solar lights. Not relevant to the |
| solar panels used. Not selected. |
| ACTION_SELECTED: LinkSelection = LinkSelection(grounded_summarization=’According to [link_id |
| =19], there are two types of solar cells used for garden solar lights, the |
| monocrystalline or polycrystalline panels.’, thoughts="It seems like non of the links |
| shows the efficiency number. However, link 19 provides some hints on what to search next. |
| We can look into the efficiency number of those two types of panels.", selected_link_ids |
| =[19]) # [END] |
|  |
| ######################### |
| # Example 2: |
| ######################### |
|  |


**Table (Page 14):**

|  |
|---|
| """Implementing step 3 of the multi-round search agent: Answer generation based on all the |
| collected search results. |
| """ |
|  |
| ######################### |
| # Example 1: |
| ######################### |
|  |
| ORIGINAL_QUESTION: str = "What’s the white powdery residual often found on a humidifier?" |
| PAST_ACTIONS: List[Action] = [ |
| Search(query=’what is humidifier’, |
| thoughts="Let’s solve this step by step. The person is asking about the residual found in |
| humidifier. Let’s first define what does humidifier do.", |
| ), |
| SelectLink(selected_links=[ |
| ResultItem(link_id=1, link_text=’Humidifiers: What They Do for Health, Uses, Types, and More |
| ’, |
| snippet=’What is a humidifier? Humidifiers are devices that add moisture to the |
| air to prevent dryness that can cause irritation in many parts of the body. |
| Humidifiers can be particularly effective for treating dryness of the skin, |
| nose, throat, and lips. They can also ease some symptoms caused by the flu |
| or common cold.’), |
| ResultItem(link_id=3, link_text=’5 humidifier uses: Benefits and risks - Medical News Today’ |
| , |
| snippet=’We do the research so you can find trusted products for your health and |
| wellness. Read more about our vetting process. Humidifiers add moisture to |
| the air, which can benefit people with respiratory symptoms or dry skin. |
| There are several ways to use humidifiers in the home or office, but there |
| are also some risks.’),], |
| grounded_summarization=’According to [link_id=1] and [link_id=3], humidifier is a device that |
| adds moisture to the air to prevent dryness that can cause irritation in many parts of |
| the body.’), |
| thoughts="Now that we know what humidifier is, we can look into the white powdery residual.", |
| ), |
| Search(query=’white powdery residual in humidifier’, |
| thoughts="Let’s now look into the white powdery residual.", |
| ), |
| SelectLink(selected_links=[ |
| ResultItem(link_id=10, link_text=’What is white dust and should I be concerned about it? - |
| HVAC.com’, |
| snippet=’White dust is usually caused by mineral content in the water that goes |
| into a humidifier. When the mist lands on furniture or other surfaces and |
| dries, it can sometimes leave behind dried mineral deposits, or "white dust |
| ."’), |
| link_text=’What is white dust and should I be concerned about it? - HVAC.com’, |
| snippet=’White dust is usually caused by mineral content in the water that |
| goes into a humidifier. When the mist lands on furniture or other surfaces |
| and dries, it can sometimes leave behind dried mineral deposits, or "white |
| dust."’) |
| ResultItem(link_id=11, link_text=’Why is White Dust Coming Out of My Humidifier?’, |
| snippet=’The white dust that you are finding on surfaces around your home is |
| likely dried-up minerals from water vapor created by the humidifier. These |
| minerals are natural in our home water supply. If you&#39;ve ever heard of |
| the term "hard water," it&#39;s referring to water with high levels of |
| calcium and magnesium.’),], |
| grounded_summarization=’According to [link_id=10], and [link_id=11], the white powdery |
| residual is caused by the mineral content in the water.’), |
| thoughts="We have all the information to answer the question.", |
| ), |
| Terminate(thoughts="We have all the information to answer the question."), |
| ] |
| ORIGINAL_QUESTION: str = "What’s the white powdery residual often found on a humidifier?" |
|  |
| ACTION_SELECTED: Answer = Answer(thoughts="The first search (’what is humidifier’) is probably |
| not what the questioner cares, so let’s omit that in the answer. We can focus more on |
| the question itself.", answer="The white powdery residue in the humidifier is usually |
| caused by mineral content in the water, according to [link_id=10]. For example, water may |
| contain high levels of calcium and magnesium [link_id=11].") # [END] |
|  |
| ######################### |
| # Example 2: |
| ######################### |
|  |


**Table (Page 15):**

|  |
|---|
| """Check whether the ANSWER addresses the ORIGINAL_QUESTION and whether the ANSWER is based on |
| SelectLinks in PAST_ACTIONS.""" |
| from dataclasses import dataclass |
| from typing import List, Tuple |
|  |
|  |
| class Action: |
| """Base class for different actions.""" |
|  |
| class Check_Answer(Action): |
| """Check whether the ANSWER addresses the ORIGINAL_QUESTION.""" |
|  |
| def __init__(self, passed: bool) -> None: |
| self.passed = passed |
|  |
| class Revise_Answer(Action): |
| """Revise the answer if it did not pass the check, based on information from SelectLinks in |
| PAST_ACTIONS.""" |
|  |
| def __init__(self, revised_answer: str) -> None: |
| self.revised_answer = revised_answer |
|  |
| ... |
|  |
|  |
| @dataclasses.dataclass |
| class ResultItem: |
| """Single search result, with link id, link title and snippet. |
|  |
| Attributes: |
| link_id: A unique integer id of this link. |
| link_text: The title of the link. |
| snippet: The snippet from the page that’s relevant to the query |
| """ |
|  |
| link_id: int |
| link_text: str |
| snippet: str |
|  |


**Table (Page 16):**

|  |
|---|
| ######################### |
| # Example 1: |
| ######################### |
|  |
| ORIGINAL_QUESTION: str = ’How to exclude a website from Google search’ |
| PAST_ACTIONS: List[Action] = [ |
| Search(query=’exclude site in google search’, |
| thoughts="We simply the ORIGINAL_QUESTION to a good search query.", |
| ), |
| SelectLink(selected_links=[ |
| ResultItem(link_id=2, link_text=’How to Exclude a Website from Google Search Results - |
| Keyword’, |
| snippet="You can exclude a domain or even a specific page from appearing on |
| Google search results. Here’s how ..."), |
| ResultItem(link_id=3, link_text=’How do I exclude/block specific web sites from search |
| results?’), |
| snippet="In the absence of a browser extension, the simplest way is to add -site: |
| website_name after your search terms. ... I can’t get rid of books.google. |
| com results. I’ ..."), |
| ResultItem(link_id=6, link_text="Q&A: Can you exclude a specific website from Google’s |
| search results?"), |
| snippet=’Jul 31, 2022 . All you have to do is simply append -site:pinterest.com |
| to the end of your search query. For example, if you were searching for the |
| term "paper ...’), |
| ], |
| grounded_summarization=’[link_id=3] mentions that we can add -site:website_name to the google |
| search query to exclude a website. [link_id=6] provides an example.’), |
| thoughts="We found enough info for a good answer to the ORIGINAL_QUESTION.", |
| ), |
| Terminate(thoughts="This is a good answer to the question.") |
| Answer(thoughts="We summarize the relevant info found in PAST_ACTIONS.", answer="To exclude a |
| website from Google search result, you can add -site:website_name after your search terms |
| according to [link_id=3]. For example, if you want to exclude pinterest.com, you can |
| simply add -site:pinterest.com according to [link_id=6].") |
| ] |
| ORIGINAL_QUESTION: str = ’How to exclude a website from Google search’ |
| ANSWER: str = ’To exclude a website from Google search result, you can add -site:website_name |
| after your search terms according to [link_id=3]. For example, if you want to exclude |
| pinterest.com, you can simply add -site:pinterest.com according to [link_id=6].’ |
|  |
| # The ANSWER is directly addressing the ORIGINAL_QUESTION. |
| # The ANSWER refers to [link_id=3] which correctly supports the core statement of adding -site |
| :website_name. The example from the answer is indeed from [link_id=6]. |
| ACTION_SELECTED: Command = Check_Answer(passed=True) # [END] |
|  |
| ######################### |
| # Example 2: |
| ######################### |
|  |


**Table (Page 17):**

|  |
|---|
| ######################### |
| # Example 1: |
| ######################### |
|  |
| ORIGINAL_QUESTION: str = "What did Jim Betts’ competitor in the 1980 election achieve in 1962? |
| " |
| PAST_ACTIONS: List[Action] = [ |
| Search(query=’who was Jim Betts competitor in 1980’, |
| thoughts="This question is asking about the achievement of Jim Betts’ competitor in 1962. Let’ |
| s first search for who this competitor is.", |
| ), |
| SelectLink(selected_links=[ |
| ResultItem(link_id=1, link_text=’Jim Betts (politician) - Wikipedia’, |
| snippet=’Jim Betts is a former member of the Ohio House of Representatives. He |
| ran against incumbent U.S. Senator John Glenn in 1980. He lost and ran in |
| 1982 for lieutenant governor.’),], |
| grounded_summarization="According to [link_id=1], Jim Betts’ competitor in 1980 was John Glenn |
| ."), |
| thoughts="Now that we know who the competitor is, we can search for his achievements in 1962." |
| , |
| ), |
| Search(query=’John Glenn achievements 1982’, |
| thoughts="Now that we know who the competitor is, we can search for his achievements in 1982." |
| , |
| ), |
| SelectLink(selected_links=[ |
| ], |
| grounded_summarization=’Nothing is selected.’), |
| thoughts="The query ’John Glenn achievements 1982’ is not very good. It should be ’John Glenn |
| achievements 1962’.", |
| ), |
| Search(query=’John Glenn achievements 1962’, |
| thoughts="John Glenn is the person we are looking for. Let’s change the date to 1962.", |
| ), |
| SelectLink(selected_links=[ |
| ResultItem(link_id=19, link_text=’John Glenn \| Biography, Accomplishments, & Facts \| |
| Britannica’, |
| snippet="Glenn, Jr., (born July 18, 1921, Cambridge, Ohio, U.S.-died December 8, |
| 2016, Columbus, Ohio), the first U.S. astronaut to orbit Earth, completing |
| three orbits in 1962. (Soviet cosmonaut Yuri Gagarin, the first person in |
| space, had made a single orbit of Earth in 1961.) Glenn joined the U.S. |
| Naval Reserve in 1942."),], |
| grounded_summarization="According to [link_id=19], John Glenn’s achievement in 1962 was to |
| become the first American to orbit the Earth."), |
| thoughts="We have all the information to answer the question.", |
| ), |
| Terminate(thoughts="We have all the information we need to answer the ORIGINAL_QUESTION. Let’s |
| stop searching and answer the question.") |
| Answer(thoughts="We have the answer to the question.", answer="Jim Betts\’ competitor in the |
| 1980 election was John Glenn. And John Glenn\’s achievement in 1962 was to become the |
| first American to orbit the Earth.") |
| ] |
| ORIGINAL_QUESTION: str = "What did Jim Betts’ competitor in the 1980 election achieve in 1962? |
| " |
| ANSWER: str = ’Jim Betts\’ competitor in the 1980 election was John Glenn [link_id=1]. And |
| John Glenn\’s achievement in 1962 was to become the first American to orbit the Earth [ |
| link_id=19].’ |
|  |
| # ANSWER directly addresses the ORIGINAL_QUESTION. |
| # [link_id=1] indeed says that Jim Betts\’ run against John Glenn in 1980, consistent with |
| ANSWER. |
| # [link_id=19] indeed says John Glenn is the first US astronaut to orbit the earth, consistent |
| with ANSWER. |
| ACTION_SELECTED: Command = Check_Answer(passed=True) # [END] |
|  |
| ######################### |
| # Example 2: |
| ######################### |
|  |


**Table (Page 18):**

|  |
|---|
| """Check whether the ANSWER implies the REF_ANSWER to the question.""" |
|  |
| def Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER): |
| """Check whether the ANSWER implies the REF_ANSWER.""" |
| # todo |
|  |
| ######################### |
| # Example 1: |
| ######################### |
|  |
| ORIGINAL_QUESTION: str = ’Are McIntyre Mines and Copperfields Mine in the same country?’ |
| ANSWER: str = ’According to [link_id=1], Copperfields Mine is in Ontario, Canada. According to |
| [link_id=4], McIntyre Mines is also in Ontario, Canada. So yes, they are in the same |
| country.’ |
| REF_ANSWER: str = ’yes’ |
|  |
| # the ANSWER implies the answer to the original question is yes, this is consistent with the |
| REF_ANSWER. |
| Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER) = True # [END] |
|  |
| ######################### |
| # Example 2: |
| ######################### |
|  |
| ORIGINAL_QUESTION: str = ’Which Director, James Richard Kelly or Paul L. Stein has a list of |
| 67 films to his credit? ’ |
| ANSWER: str = ’According to [link_id=1] and [link_id=2], James Richard Kelly has 5 films to |
| his credit.’ |
| REF_ANSWER: str = ’Paul Ludwig Stein (4 February 1892 - 2 May 1951) was an Austrian-born film |
| director with 67 films to his credit.’ |
|  |
| # the ANSWER does not imply the REF_ANSWER because ANSWER does not mention Paul Ludwig Stein. |
| Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER) = False # [END] |
|  |
| ######################### |
| # Example 3: |
| ######################### |
|  |
| ORIGINAL_QUESTION: str = ’Are the genuses Michelia and Stenomesson in the same family?’ |
| ANSWER: str = ’Based on the information we have, we are not sure whether the genuses Michelia |
| and Stenomesson are in the same family [link_id=3] does not contain this information.’ |
| REF_ANSWER: str = ’no’ |
|  |
| # The ANSWER did not determine whether or not Michelia and Stenomesson are in the same family. |
| # The REF_ANSWER implies that they are not in the same family. |
| # Thus we cannot infer the REF_ANSWER given the ANSWER. |
| Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER) = False # [END] |
|  |
| ######################### |
| # Example 4: |
| ######################### |
|  |
| ORIGINAL_QUESTION: str = ’In what year was the winner of the 44th edition of the Miss World |
| competition born?’ |
| ANSWER: str = ’According to [link_id=2], the winner of the 44th edition of the Miss World |
| competition is Aishwarya Rai.\nAccording to [link_id=4], she was born in 1973.’ |
| REF_ANSWER: str = ’1973’ |
|  |
| # The ANSWER implies 1973 as the final answer to ORIGINAL_QUESTION. |
| # REF_ANSWER implies 1973 as the final answer to ORIGINAL_QUESTION, too. |
| Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER) = True # [END] |
|  |
| ######################### |
| # Example 5: |
| ######################### |
|  |
| ORIGINAL_QUESTION: str = ’Skull & Bones is a mini-series by a man that is an editor of what |
| two comics?’ |
| ANSWER: str = ’The question is ill-formed or out-of-date. We should ask for clarification from |
| the asker.’ |
| REF_ANSWER: str = ’Marvel Comics and DC Comics’ |
|  |
| # The ANSWER did not provide any answer to ORIGINAL_QUESTION. |
| Check_Answer(ORIGINAL_QUESTION, ANSWER, REF_ANSWER) = False # [END] |
|  |
| ######################### |
| # Example 6: |
| ######################### |
|  |


**Table (Page 19):**

|  |
|---|
| """Rater Instructions: |
| - The goal of this rating is to filter out bad actions, so that they’ll be excluded from the |
| fine-tuning dataset. |
| - Overall, we want to the agent to produce relevant and grounded answers with minimal steps. |
| Anything that deviates from this goal is considered bad. |
| - If any element (thoughts, comments etc.) is empty, then it’s automatically bad. |
|  |
| ######################################### |
|  |
|  |
|  |
| *** Model Can See: |
| ‘‘‘ |
| {inputs} |
| ‘‘‘ |
|  |
| *** Model Output #1: |
| ‘‘‘ |
| {action1} |
| ‘‘‘ |
|  |
| *** Model Output #2: |
| ‘‘‘ |
| {action2} |
| ‘‘‘ |
|  |
| *** Model Output #3: |
| ‘‘‘ |
| {action3} |
| ‘‘‘ |
|  |
| *** Model Output #4: |
| ‘‘‘ |
| {action4} |
| ‘‘‘ |
|  |
| ######################################### |
|  |
| Your Instructions: |
| - Choose the best model output based on the rater’s instructions. |
| - Don’t assume in your decision that the model knows anything outside of "Model Can See" |
| section. |
| - Be specific in your explanation. |
|  |
| Output 3 lines when answering and make sure to follow the precise format. |
|  |
| Explanation: why you think model output #X is the best |
| Answer: #X |
| Ranking: #X > #Y > ... |
| """ |
|  |
