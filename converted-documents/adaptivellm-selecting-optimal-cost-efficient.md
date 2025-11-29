---
title: "AdaptiveLLM Selecting Optimal Cost Efficient"
original_file: "./AdaptiveLLM_Selecting_Optimal_Cost_Efficient.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "chain-of-thought", "fine-tuning", "evaluation"]
keywords: ["coder", "deepseek", "instruct", "qwen", "https", "etal", "distill", "pass", "arxivpreprintarxiv", "page"]
summary: "<!-- Page 1 -->

5202
nuJ
21
]ES.sc[
1v52501.6052:viXra
AdaptiveLLM: A Framework for Selecting Optimal Cost-Efficient
LLM for Code-Generation Based on CoT Length

### JunhangCheng,FangLiu∗,ChengruWu,LiZhang

StateKeyLaboratoryofComplex&CriticalSoftwareEnvironment,SchoolofComputerScienceandEngineering

### BeihangUniversity,Beijing,China

chengjunhang7@gmail.com,{fangliu,23230618,lily}@buaa.edu.cn

### Abstract ACMReferenceFormat:


### WhileLargeLanguageModels(LLMs)havesignificantlyadvanced


## Introduction
related_documents: []
---

# AdaptiveLLM Selecting Optimal Cost Efficient

<!-- Page 1 -->

5202
nuJ
21
]ES.sc[
1v52501.6052:viXra
AdaptiveLLM: A Framework for Selecting Optimal Cost-Efficient
LLM for Code-Generation Based on CoT Length

### JunhangCheng,FangLiu∗,ChengruWu,LiZhang

StateKeyLaboratoryofComplex&CriticalSoftwareEnvironment,SchoolofComputerScienceandEngineering

### BeihangUniversity,Beijing,China

chengjunhang7@gmail.com,{fangliu,23230618,lily}@buaa.edu.cn

### Abstract ACMReferenceFormat:


### WhileLargeLanguageModels(LLMs)havesignificantlyadvanced


### JunhangCheng,FangLiu∗,ChengruWu,LiZhang.2018.AdaptiveLLM:A

FrameworkforSelectingOptimalCost-EfficientLLMforCode-Generation
codegenerationefficiency,theyfaceinherentchallengesinbalanc-
BasedonCoTLength.InProceedingsofMakesuretoenterthecorrectconingperformanceandinferencecostsacrossdiverseprogramming
ferencetitlefromyourrightsconfirmationemail(Conferenceacronym’XX).
tasks.DynamicallyselectingtheoptimalLLMbasedontaskdif-

### ACM,NewYork,NY,USA,13pages.https://doi.org/XXXXXXX.XXXXXXX

ficulty and resource constraints offers a promising approach to
achieveanoptimalbalancebetweenefficiencyandperformance.
However,existingmodelselectionmethodsareresource-intensive Core: CoT
andoftenneglectcostefficiency.Moreover,theseapproachesrely User Input: Coding Problem …
onhuman-annotateddifficultylabelsthatarefrequentlyinaccessi-

### Problem Difficulty?

bleinreal-worldsettingsandmaynotalignwiththeLLM’sown
assessmentoftaskdifficulty.Inthispaper,weintroduceAdaptiv- Cost Used?
eLLM,aframeworkthatdynamicallyselectsoptimalLLMsfora

### LLM Capacity?

givencodingtaskbyautomaticallyassessingtaskdifficulty.Our
frameworkfirstestimatestaskdifficultyusingChain-of-Thought
lengthsgeneratedbyreasoningmodel,clusterstheseintothree

### Optimal LLM

difficultylevelsviak-means,andfine-tunesCodeBERTtoembed
difficulty-awarefeatures.AtrainedXGBoostclassifierthenselects Figure1:TheUseofAdaptiveLLM.
thebestmodelforeachproblem,optimizingtheperformance-cost
trade-off.ExperimentalresultsshowthatAdaptiveLLMachievesa 1 Introduction
7.86%improvementinpass@1scorewhilereducingresourcecon-
LargeLanguageModelshaveemergedastransformativetoolsin
sumptionby88.9%comparedtobaselinemethodComplexityNet.
codeunderstandingandgeneration,drivingsignificantadvance-

### Whencomparedtoasinglemodel,AdaptiveLLMdemonstratesan

ments in programming efficiency through intelligent assistants
approximately15%accuracyimprovement,whilemaintainingthe
suchasGitHubCopilot[17]andCursor[4].Thesesystemsleversame level of cost consumption. Apart from that, the difficulty
ageLLM’scontextualreasoningcapabilitiestopredictandautoassessment using CoT provides more reliable selection criteria
complete code snippets, reducing development time and effort.
than human evaluation. Our replication package is available at
However,expandingapplicationscenariosrevealtwocriticalchalhttps://github.com/cjhCoder7/AdaptiveLLM.
lenges:❶LLMexhibitvaryingperformanceacrossprogramming
tasksofdifferentcomplexities,and❷theirhighcomputationalcosts

### CCSConcepts

forinferenceandtrainingnecessitateoptimizedresourceallocation.
•Softwareanditsengineering;•Computingmethodologies Specifically,SWE-Bench[27]hasdemonstratedthatdifferenttypes
→Artificialintelligence; ofcodeLLMspossessvaryingcapabilitiesinsolvingdifferenttypes
ofcodeproblems.Similarly,codeLLMswithdifferentparameter
Keywords sizesalsoshowdistinctabilitiesinaddressingcodeproblemsof
LargeLanguageModel,CodeGeneration,ModelSelection varyingdifficulties.Whilelargermodelsgenerallyexhibitstronger
problem-solvingcapabilities,smallermodelscanachievecomparableresultsonsimplertasks.Giventhatlargermodelsincurhigher
∗Correspondingauthor.
operationalcostsandareoverqualifiedforsimplerproblems,dynamicallyselectingtheoptimalLLMbasedontaskcomplexityand
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
resourceconstraintspresentsapromisingstrategytobalanceefficiency
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation andperformance.
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe Toaddressthischallenge,researchershavedevelopedvarious
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
model selection approaches, which generally fall into two caterepublish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. gories.Thefirstcategorycomprisesrouter-basedapproaches[10,
Conferenceacronym’XX,Woodstock,NY 12,21,26,56].Forexample,RouterDC[12]introducesanovelrout-
©2018Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ingmechanismthatdiffersfromtraditionalselectionmethodsby

## Acmisbn978-1-4503-Xxxx-X/2018/06

https://doi.org/XXXXXXX.XXXXXXX embeddingtheproblem-LLMmatchingintoavectorspace.This

<!-- Page 2 -->

Conferenceacronym’XX,June03–05,2018,Woodstock,NY Chengetal.
approachallowsforasingleLLMinvocationtosolvetheproblem, performancewithsignificantlylowerresourceconsumption.Adreducingresourceconsumptioncomparedtopreviousstrategies ditionally,ouranalysisoftheCoTdifficultyassessmentmethod
thatrequiredgeneratingandscreeningresponsesfromallLLMs revealsthatCoTmoreaccuratelyreflectsLLMs’perceptionof
inadvance.However,RouterDCoverlooksthedifficultylevelsof problemdifficultycomparedtohumanlabels.
theproblemsthemselvesandreliessolelyonmodelresponsesduringtheframeworkconstructiontocreateproblem-LLMmatches,
2 RelatedWork
whichcanberesource-intensive.ThesecondcategoryselectsdifferentLLMsbasedonthedifficultylevelsofproblems[6,25,36]. 2.1 LLMsforCodeGeneration
Forinstance,ComplexityNet[6]usesdifficultytagstoguidethe LargeLanguageModelshaveachievedsignificantbreakthroughs
selectionofoptimalmodels.However,thisapproachoverlookscost innaturallanguageprocessing,particularlydemonstratingexcepconsiderationsduringmodelinvocation,frequentlyrelyingonhigh- tionalcapabilitiesincodeunderstandingandgeneration[1,18,19,
performancebutexpensiveclosed-sourcemodelslikeGPT-3.5and 31,44–46,48,52].Previousworksfocusedonfine-tuningpretrained
GPT-4.Additionally,ComplexityNetreliesonannotateddifficulty LLMstoaddresstasksofvaryingtypesandcomplexities.Forexamtags,whichareoftenunavailableinreal-worldsettings,andthey ple,mathematicalreasoningtaskshavebeenaddressedthroughspemaynotaccuratelyreflectanLLM’sintrinsicperceptionoftask cializedfine-tuningofmodelssuchasWizardMath[35],Qwen2.5-
difficulty.Furthermore,directlyestimatingdifficultyusingLLMs Math[53]andMetaMath[55].Similarly,codegenerationcapabilhasprovenunreliableduetotherandomnessintheirpredictions. itieshavebeenimprovedthroughfine-tuning,asdemonstrated
Recentadvancesinreasoningmodelshaveopenednewpossibil- bymodelssuchasQwen2.5-Coder[24]andDeepSeek-Coder-V2
itiesforautomatingproblemdifficultyassessment[19,39,40,46]. [58].Thesemodelsexhibitsignificantperformancegainsintheir
Thesemodelsproducestep-by-stepChains-of-Thought(CoT)rea- respectivetargetdomains.
soningprocess,wherelongerreasoningsequencesoftencorrelate CodegenerationbenchmarkshaveevolvedtoassessLLM’scapawith higher problem complexity. This method not only mimics bilitiesacrosscomplexitylevels.HumanEval[11]isapopularbenchhumancognitivepatternsbutalsoprovidesasystematicframe- mark,whitchthenextendedtomultilingualadaptations[9,41,57],
workforevaluatingdifficulty.Byintegratingreasoningmodelsinto novelcodecompletionparadigms[37],andenhancedtestingframetheframeworkandconsideringmodelcosts,wecanpotentially works[32].High-complexityevaluationleveragesCodeContests
overcomethelimitationsofbothRouter-basedanddifficulty-based [29]foralgorithmicchallengesandSWE-Bench[27]forreal-world
methodsforcodegenerationtasks. softwareengineeringscenarios.FullStackBench[33]furtherenables
Tothisend,weproposeAdaptiveLLM,aframeworkthatdynam- cross-domainevaluationspanning16programminglanguageswith
icallyselectsoptimalcodegenerationmodelsbasedonautomated SandboxFusionexecution.
difficultyassessment.AdaptiveLLMfirstestimatesthedifficultyof Ourstudyselectsthreedatasets:HumanEval,LeetCodeSample,
eachcodingproblemaccordingtotheCoTlengthgeneratedfrom andCodeContests.Additionally,wechooseeightcodeLLMsand
LLMswithenhancedreasoningcapabilities.TheseCoTlengthsare DeepSeekR1reasoningmodel.
clusteredintothreedifficultylevelsusingk-means,andtheresultinglabelsareusedtofine-tunetheCodeBERTembeddingmodel
2.2 EvaluationofCodingProblems
[16].Thisfine-tuningprocessenrichestheproblemembeddings
withdifficulty-awarefeatures.Subsequently,wetrainanXGBoost Thedifficultyofprogrammingproblemsisacrucialfactorinselectclassifiertoselectthebest-performingmodelforeachproblem,con- ingtheoptimalmodel.Variousapproacheshavebeenproposedfor
sideringbothresponsequalityandresourceefficiencytogenerate assessingthedifficultyofprogrammingproblems.
abalancedranking.Bydynamicallymatchingproblemswiththe LeetCodeSample[33]andCodeContests[29]extractedfromcommostsuitablemodels,AdaptiveLLMoptimizesthetrade-offbetween petitiveprogrammingplatforms,suchasLeetCode[3]andCodeperformanceandcost.Experimentalresultsonthreedatasets forces[2],oftenrelyonuserperformancedatatoquantifyproblem
ofvaryingdifficultyshowthatAdaptiveLLMachievesa7.86% difficulty.However,thesemetricssufferfromcross-platforminimprovementincapabilityandan88.9%reductionincost comparabilityanddependenceonuserperformancedata.Another
comparedtobaselinemethods. approachinvolvesanalyzingthecomplexityofsolutions.Wang
Ourcontributionsaresummarizedasfollows: etal.[49]evaluatedproblemdifficultyusingfivecodecomplexity
metrics:LineComplexity,CyclomaticComplexity[15],Halstead

### Complexity[22],CognitiveComplexity[8],andMaintainability

• WepresentAdaptiveLLM,aframeworkforselectingthemost Index[51].However,notalltheproblemshavestandardsolutions.
cost-effectiveLLMbasedonproblemdifficulty,modelcapability, Furthermore,forproblemswithmultiplevalidsolutions,thevariandmodelcost.Itenablespersonalizedselectionoftheoptimal abilityincodecomplexityacrossdifferentimplementationswill
LLMforeachproblem. influenceit.Baeetal.[6]andJeongetal.[25]evaluatedifficulty
• We propose a novel programming task difficulty assessment basedonthenumberofinteractionsbetweentheproblemanda
methodbasedonCoTofreasoningmodels.Thisautomatedap- modeltoachieveacorrectsolution.Itdoesnotdifferentiatewellbeproacheliminatestheneedforhumaninterventionbyusingthe tweenhighlevelproblems,becausenomatterhowmanyiterations
lengthofCoTtoestimateproblemcomplexity. aredoneitfailstogeneratethecorrectcode.
• WeevaluateAdaptiveLLMandthebaselinemethodonbench- Inthisstudy,weproposeanovelapproachtoevaluateproblem
markdatasets.ResultsshowthatAdaptiveLLMachievessuperior difficultybasedontheCoTlengthgeneratedbyreasoningLLMs.

<!-- Page 3 -->

AdaptiveLLM:AFrameworkforSelectingOptimalCost-EfficientLLMforCode-GenerationBasedonCoTLength Conferenceacronym’XX,June03–05,2018,Woodstock,NY

##  3 D V V #   3 D V V # 

 & R G H / O D P D   %  , Q V W U X F W  & R G H / O D P D   %  , Q V W U X F W
 ' H H S V H H N  & R G H U  9   / L W H  , Q V W U X F W  4 Z H Q     & R G H U     %  , Q V W U X F W  ' H H S V H H N  & R G H U  9   / L W H  , Q V W U X F W  4 Z H Q     & R G H U     %  , Q V W U X F W
0.8 0.8
0.6 0.6
0.4 0.4
0.2 0.2
 & R G H V W U D O    %  < L  & R G H U     %  & K D W  & R G H V W U D O    %  < L  & R G H U     %  & K D W
 6 W D U F R G H U     %  , Q V W U X F W  4 Z H Q %     & R G H U    %  , Q V W U X F W  6 W D U F R G H U     %  , Q V W U X F W  4 Z H Q     & R G H U    %  , Q V W U X F W

##  + P D Q ( Y D O

 ' H H S V H H N  & R G H U    %  , Q V W U X F W  ' H H S V H H N  & R G H U    %  , Q V W U X F W  / H H W & R G H 6 D P S O H

##  & R G H & R Q W H V W B W H V W

Figure2:TheperformanceofeightcodeLLMsonHumanEval,LeetCodeSampleandCodeContests.
2.3 ModelSelection evaluated on three benchmark datasets: HumanEval [11], Leet-
DifferentLLMsexhibitdistinctstrengthsandweaknessesandno CodeSample[33],andCodeContests[29].Figure2illustratesthe
singleLLMcurrentlydominatesacrossalltasks.Forsuchissues, evaluationresults,whileFigure3showsthecomparisonofcost
theprevalentsolutioncurrentlyistoselecttheoptimalLLMbased ($/MTokens)andHumanEvalpass@1scoreacrosseightmodels.
onthespecifictask. Ourkeyfindingsaresummarizedbelow.
Jiang et al. [26] introduced PairRanker and GenFuser, which DatasetDifficultyAnalysis:Theevaluateddatasetsexhibita
generateimprovedoutputsbysynthesizingresultsfromallLLMs. cleargradientofcomplexity:HumanEval<LeetCodeSample<
However,thismethodrequiresinvokingLLMs𝑂(𝑇2)times,where CodeContests.HumanEvalfocusesonfundamentalprogramming
𝑇 representsthenumberofmodels.Tooptimizebothperformance taskswith164Pythonproblemsthatrequiresfunction-levelcode
andefficiencyinLLMselection,researchershaveproposedvarious completionbasedonsignatureandfunctionaldescriptions.Leetmethods.Cascadingstrategies[10,21,56]sequentiallyinvokea CodeSample,sourcedfromtheLeetCode,presentsmorecomplex
seriesofpre-rankedmodels,typicallyorderedbycapacityfrom algorithmicchallengeswithlongerproblemdescriptions.Codesmallesttolargest.Thisprocessstopswhenamodel’soutputmeets Contests,derivedfromCodeforcescompetitions,whichproblems
apredefinedconfidencethreshold.Nevertheless,thesemethodsstill involvingadvancedalgorithmicparadigmssuchasdynamicprorequiresatleast𝑂(𝑇)modelinvocationsduringinference.Building gramming, graph theory, and combinatorial optimization. And
ontheseefforts,Chenetal.[12]proposedRouterDC,whichemploys Theseproblemshavestricttime/spaceconstraintsandrequirefullaroutingmechanismtopreciselyidentifytheoptimalmodelfora filecodegenerationratherthanfunctioncompletion.Additionally,
giventask.Meanwhile,Baeetal.[6]introducedComplexityNet,a CodeContestsincludeschallengeswithimage-basedproblemdemethodthatinvolvesfine-tuninganembeddedmodel,DaVinci-002
scriptions(<image>tags),posingadditionalcomprehensionbar-
[7],toselectmodels.Italsorequiresonlyasinglecalltotheselected riersfortext-onlymodels.AsshowninFigure2,onHumanEval,
modeltocompletethetask. mostmodelsachievepass@1scoreabove60%,whileperformance
However,modelselectionisnotonlyinfluencedbyLLM’scapa- dropssignificantlyonCodeContests(averagepass@1<3%).
bilitybutalsobyadditionalfactorssuchascomputationalcostand ParameterSizeEffects:Weobserveastrongpositivecorreproblemdifficulty.So,weproposeAdaptiveLLM,whichintegrates lationbetweenmodelparametersizeandcodegenerationperformultiplefactors,includingmodelperformance,computationalcost, mance.Forexample,increasingtheparametersfrom1.5B(Yi-Coder)
andproblemdifficulty,intoitsdecision-makingprocess. to32B(Qwen2.5-Coder)yieldsa59%improvementintheLeetCode-

### Samplepass@5scoreand56%improvementinLeetCodeSample

pass@1score.Similarly,onCodeContests,Yi-Coderonlyachieved
3 PreliminaryStudy
0.61%inpass@1scoreand1.21%inpass@5score,indicatingthat
ToinvestigatethecapabilitiesdifferencesamongvariousLLMsand itonlysolvedasmallnumberofproblems.Incontrast,Qwen2.5-
comparetheircapabilitiesagainstpricing,weconductaprelimi- Coderobtained4.85%pass@1scoreand11.52%pass@5score,renarystudyinthissection.WeselecteightcodeLLMs:Yi-Coder- flecting a notable improvement. After conducting a correlation
1.5B-Chat[54],Qwen2.5-Coder-1.5B-Instruct[24],CodeLlama-7B- analysisbetweenparametersizeandHumanEvalpass@1scores,
Instruct[43],Starcoder2-15B-Instruct[34],DeepSeek-Coder-V2- wefoundthatthecorrelationcoefficientwas0.72,whichexceeds0.7.
Lite-Instruct[58],Codestral-22B[47],DeepSeek-Coder-33B-Instruct Thisshowsthatincreasingtheparametersizebringsabout
[20]andQwen2.5-Coder-32B-Instruct[24].Allthesemodelsare

<!-- Page 4 -->

Conferenceacronym’XX,June03–05,2018,Woodstock,NY Chengetal.
significantchangesinamodelperformance.However,itis
worthnotingthatformodelslikethe7BCodeLlama,itsaverage
performanceacrossthethreedatasetsissignificantlylowerthan
that of the two 1.5B models (Yi-Coder-1.5B-Chat and Qwen2.5-
Coder-1.5B-Instruct).Weattributethistocontinuousarchitectural
optimizations.Newermodelsoftenhaveadvancedarchitectures
andtrainingtechniques,enablingthemtooutperformoldermodels.
1.4
1.2
1.0
0.8
0.6
0.4
0.2
 < L  & R  4  G  Z  H U  H    Q          0   .  % 0   &   &  R  K  G  D  H  W  U     %  &   ,  R  Q  G  V  H  W  /  U X  O D  F  P  W  D   %  6    W  ,  D  Q  U  V  F  W  R  '  U  G  X  H  H  H  F  U  S  W    V    H    H    N  %   &   ,  R  Q  G  V W  H  U  U  X   9  F W    / L W H  , Q V W U X F W  4  &  Z  R G  H  H  Q  V    W    U    D    O  &     R    G  %  H  '  U  H     H S   %  V H    H  ,  N  Q    V  &  W U  R  X  G  F  H  W  U    %  , Q V W U X F W

##   V Q H N R 7  0     W V R &

1.0

##        0  7 R N H Q V       0  7 R N H Q V 0.9


##        0  7 R N H Q V 0.8


##        0  7 R N H Q V       0  7 R N H Q V 0.7

0.6

##        0  7 R N H Q V

0.5

##        0  7 R N H Q V       0  7 R N H Q V

0.4

##    # V V D 3  O D Y ( Q D P X +

4 Methodology

### Figure4illustratestheoverallarchitectureofAdaptiveLLM.Asa

supervisedlearningapproach,AdaptiveLLMfirstrequiresreconstructing the three datasets (Section 4.1) due to the absence of
learningobjectivesintheiroriginalform.Theframeworkconsists
oftwocorecomponents:anembeddinglayer(Section4.2)andaclassificationlayer(Section4.3).Finally,weconductacomprehensive
evaluationoftheAdaptiveLLMframework.

### Pass Rate

4.1 ConstructionofLLMRankingDatasets
ToconstructtheAdaptiveLLMframework,wefirstconductaresearchstudytoidentifydatasetsandlargemodelsappliedtothe
AdaptiveLLM framework and ranked the models used for each
questionbasedontheperformanceandcostofthemodelanswers.

### DuetothevarietyofcodeLLMs,withtheirdifferentparameters,

architectures,andinferencecosts,toensurethatthepoolofmodels
intheAdaptiveLLMframeworkcancovermostoftheLLMs,we
selecteightrepresentativeLLMsamongmodelswithdifferentparametersizesandwithdifferentarchitectures.Abriefdescription
oftheseLLMsisprovidedinSection5.1.1.Theconstructionprocess
ofLLMrankingdatasetisshowninFigure5.ConstructingtheLLM
rankingdatasetrequiresatotaloftwosteps.Thefirststepistofirst havethemodelsinthemodelcandidatepoolanswerthequestions intheselecteddataset,andthenrecordmetricssuchascorrectness, tokenspend,andcost.ThesecondstepistoselecttheoptimalLLM
Figure3:TherelationshipbetweenCostandPerformance.
foreachquestionbasedontherecordedmetrics,andthisstepwill
ranktheLLMsusedineachquestionbasedonthemetrics.Finally,
Cost-PerformanceTrade-offs:Figure3revealsagrowthin theconstructeddatasetwillbedividedintotrainingandtestsets,
computationaloverheadasLLM’scapacityandparametersizein- andtheproblem-optimalLLMpairsinthetrainingsetwillbeused
creases.Qwen2.5-Coder-1.5B-Instructhasthehighestperformance totraintheXGBOOSTclassifierinSection4.3.
aswellasthelargestnumberofparameters,anditalsohasthe
highestcostat$1.26/MTokens.Incontrast,CodeLlama-7B-Instruct 4.1.1 Recording of test result metrics. In Section 3, we conduct
onlyneed$0.42/MTokensandithastheworstperformancein experimentsonthreedatasetsforeightlargemodels.Toensure
HumanEvalwithonly7Bparameters,lessthanQwen’sparameters. consistencyintestingthegeneratedcodefiles,weimplementthe
Largermodelsneedmorememoryrequirements,with30B+models testvalidationinSandboxFusionsandboxenvironment[33]and
likeQwen2.5-Coder-32B-Instructneedingmorethan60GBVRAM recordtheaccuracyofeachanswerforeachmodel.Atthesame
forBF16inference–requiringatleastfourNVIDIARTX4090GPUs time, we also record the resource consumption metrics of the
(24GBeach).Cloudcostsamplifydisparities:modelswith16.1B+pa- models,andthepriceofLLMisprovidedbySiliconFlow(https:
rametersneedcoststhatare9×higherthanthosewith0-4Bparam- //cloud.siliconflow.cn/models),acloudinterfacingplatform.HowetersonFireworks(https://fireworks.ai/pricing).Althoughlarger ever,giventhatnotalloftheselectedmodelsaredeployedonthe
modelsachievesuperiorcodegenerationperformance,theiroper- platform,weusetheconsumptiondataofamodelwiththesamepaationalcostsbecomeprohibitiveforbudget-constrainedprojects. rametersizeasaproxyforthenon-deployedmodels.Followingthis
Thus,thecost-performancetrade-offunderscorestheneed step,weobtainadatasetcomprisingHumanEval,LeetCodeSample,
toselectanoptimalLLM,balancingparameterscalewith andCodeContests.Foreachprobleminthedataset,itincludesfive
financialresources. responsesfromeachoftheeightLLMs,alongwiththeircorrespond-
Basedonabovefindings,thedesignofaframeworkthatcan ingcorrectnessresults,accuracyrates,andtokencostsforallfive
maintainmodelperformancewhileeffectivelyreducinginference responses.
costshasbecomeacriticalissue.Toaddressthis,weproposea
novelframeworkthataimstoleveragethestrengthsofmultiple 4.1.2 LLMranking. SinceAdaptiveLLMoperatesasasupervised
largemodels.Thecoreprincipleofthisframeworkistodynamically learningframework,foreachproblem,weneedtopredefinean
allocatecodetaskstothemostsuitablemodelbasedonspecific optimalLLM.ThisoptimalLLMshouldachievebothhighaccuracy
taskrequirements.Forexample,simplertasksareprioritizedto insolvingtheproblemandminimalcomputationalcosts.Toacsmallerparameter-scalemodelstominimizeinferencecosts,while complishthis,foreveryproblem,weranktheperformanceofthe
complextasksaredelegatedtolargerparameter-scalemodelsto eightLLMsoneachproblemandselectthetop-rankedmodelas
ensuretaskcompletionquality.Inthefollowingsection,wewill theoptimalLLM.So,weselectLLMwiththehighestScore𝑖 asthe
provideadetailedexplanationoftheframework. optimalmodelforeachproblem.Score𝑖 iscalculatedasfollows:

<!-- Page 5 -->

AdaptiveLLM:AFrameworkforSelectingOptimalCost-EfficientLLMforCode-GenerationBasedonCoTLength Conferenceacronym’XX,June03–05,2018,Woodstock,NY
Construction of LLM Ranking Datasets Fine-tuning of CodeBERT Training of XGBOOST Classifier
LeetCodeSample HumanEval CodeContests

### TrainingData

DeepSeek-R1-Distill-Qwen-32B Embedding

### CoTRecord

K Clustering

### TestData

Fine-tuning

### CodeBERT


### ModelSelect

Figure4:TheoverallarchitectureofAdaptiveLLM.
forallcandidatemodels,themodelwiththehighestscoreisse-
LLMGeneration ×8 FileExecute lectedastheoptimalsolutionmodelfortheproblem.Duetothe
jointoptimizationof𝑇𝑜𝑘𝑒𝑛𝑠 𝑖and𝑃𝑟𝑖𝑐𝑒 𝑖intheformula,theselected

### LeetCodeSample ×2 ×2

modelcansatisfythetwoobjectivesofcodecorrectnessandcost

### PythonFile

controlatthesametime.Theresultdatasetcoversthecomplete
HumanEval problemdescription,model-generatedcode,tokenconsumption
records,inferencepricedetails,andoptimalmodellabelsbasedon
CodeContests 𝑆𝑐𝑜𝑟𝑒 𝑖.Youcanfinddetailedinformationaboutthedatasetinthe
publicrepositorythatwehaveprovided.

### CostRecord

4.2 Fine-tuningofCodeBERT
InthepreliminarystudyinSection3,wefindthatsomemodelsperformbetterwhendealingwithmorecomplexproblems,butatthe
sametime,thesemodelshavelargerparametersizesandconsume
Figure5:TheprocessofLLMrankingdatasetconstruction.
moreresources.Giventhisfinding,wewouldliketoincorporate
thedifficultyoftheproblemintoAdaptiveLLMframeworktoobtainthebestpredictionresults.However,inreal-worldscenarios,
codeproblemsoftenlackdifficultyannotations.Evenwhensuch
𝑆𝑐𝑜𝑟𝑒 𝑖 =log(max 𝑁 𝑗=1 (𝑇𝑜𝑘𝑒𝑛𝑠 𝑗)×𝑀𝑎𝑥𝑃𝑟𝑖𝑐𝑒)×𝑝𝑎𝑠𝑠 𝑖 annotationsareavailable,theymaynotalignwiththeperceptionof
−log(𝑇𝑜𝑘𝑒𝑛𝑠 𝑖 ×𝑃𝑟𝑖𝑐𝑒 𝑖) (1) difficultyasunderstoodbyLLMs[28,42].Toaddressthischallenge,
weproposeleveragingthelengthofCoTgeneratedbyinference
Theformulareachestheoptimizationofmodelselectionwith models,suchasDeepSeekR1,asaproxyforproblemdifficulty.This
doubleconstraints.First,𝑝𝑎𝑠𝑠 𝑖 isthetestpassratevariable,which ismotivatedbytheobservationthatlongerCoTlengthsgenerally
reflectstheproportionofthemodelthatpassesallthetestcases correspondtohigherproblemcomplexity,providingareliableand
infiveresponses.Second,theresourceconsumption(theproduct automatedwaytoestimatedifficultywithoutrelyingonmanual
ofthenumberofTokenandtheinferenceprice)istransformed annotations.SowefirstuseDeepSeek-R1-Distill-Qwen-32B,adisintoapenaltytermbyintroducingalogarithmicoperation.This tilledversionofthereasoningmodelDeepSeekR1,toassessthe
makesthemodel’sscorehigherthemoreefficientandlesscostly difficultyofeachproblem,andthenfine-tunetheCodeBERT[16]
itsinferenceisbasedontheguaranteeofcorrectnessofanswers. embeddingmodelusingtripletcontrastloss.
Specially,𝑀𝑎𝑥𝑃𝑟𝑖𝑐𝑒selectsthehighestunitpriceamongallmodels Itisimportanttonotethatwedonotrecordcostwhenusing
asthenormalizedbenchmark,amovethateliminatesthequantita- DeepSeek-R1-Distill-Qwen-32B.Thisisbecauseweonlyneedto
tiveeffectsarisingfromthedifferencesinthepricingsystemsof evaluatethecostofthemodelselectedinthemodelcandidatepool
differentmodels. specificallywhenansweringthequestion,notthecostofusing
Basedonthisscoringformula,wecanconstructamodelrecom- themodelinthetrainingframeworkphase.UsingDeepSeekR1
mendationsystem.Foreachcodeproblem,aftercalculating𝑆𝑐𝑜𝑟𝑒 𝑖 issothatthequestiondifficultyinformationisembeddedinthe

<!-- Page 6 -->

Conferenceacronym’XX,June03–05,2018,Woodstock,NY Chengetal.
finalembeddingvectorrepresentation.Andtheinvolvementof

### HumanEval/0 CodeContests/28

DeepSeekR1isnotrequiredwhenusingAdaptiveLLM.
Okay, I need to solve this problem where Okay, I need to solve this programming
4.2.1 Labelingproblemdifficulty. Fortheconstructeddataset,we I l i h s a t v e a r t e o c c l h o e s c e k r i t f o a e n a y c h t w o o t h n e u r m b t e h r a s n i a n a p c r a o r b e l f e u m l . l y L . et's read the problem statement
given threshold. The function is called
willuseDeepSeek-R1-Distill-Qwen-32Btorecordthereasoning has_close_elementsand takes a list of ...
floats and a threshold float as inputs
lengthforeachproblem.AsseeninFigure6,problemsofdifferent and returns a boolean. For each test case:
difficultylevelsshowsignificantdifferencesinthereasoninglength. ... Read a,b,c.
Thereasoninglengthofasimpleproblemmaybeinalowerorderof Yes, that's correct. sum_S= a + 2*b + 3*c.
magnitude,whilethereasoninglengthofacomplexproblemjumps So the code seems correct. If sum_S%2 ==1:
toahigherorderofmagnitude.Forexample,thereasoninglength So now, let me write the code accordingly. print(1).
ofCodeContests/28problemis41058,thatofLeetCode/22prob- Else:

### LeetCode/22

lemis24806,andthatof HumanEval/0problemisonly6832.This s_even= sum_S//2.
differencereflectsthefactthatwhensolvingcomplexproblems, O c k o a u y n , t I t h h e a v n e u m t b o e r s o o l f v i e n c t r h e i m s o v p a r b o l b e le s m u b w a h r e r r a e y s I sum_13 = a + 3*c.
thereasoningmodelneedsmorecomplexreasoningstepsandlogi- in a given array. Hmm, let's break it down. remainder = (sum_13) % 3.
... # Not sure anymore.
calprocessestoreachasolution.Incontrast,theanswerlengths
So, code seems correct. Finally, The code is as follows, based on
remainlargelyconsistentacrossproblemsofvaryingdifficulty.We certain observations.

### So the code seems to handle all cases

useDeepSeek-R1-Distill-Qwen-32Bandcounttheaverageofthe correctly.
reasoninglengthsandanswerlengthsoneachdataset.Thedetailed So, I think this solution should be correct.
dataisshowninTable1.Thisimpliesthatthesizeofthecontent

### HumanEval/0 DifficultyLabel

outputbythemodelisrelativelystablewhengeneratingthefinal

### Reasoning Length: 6832

codeanswer,despitethedifferentcomplexityofthequestions. AnsweringLength: 2069

### LeetCode/22


### Reasoning Length: 24806

Table1:ComparisonofDeepSeek-R1-Distill-Qwen-32B’sav-

### AnsweringLength: 2320

eragesofreasoninglengthsandanswerlengthsondifferent

### CodeContests/28

datasetsshowsalargevariabilityinreasoninglengths,while Reasoning Length: 41058 K-means Clustering
answerlengthsarenotdiscriminatory. AnsweringLength: 2386
AvgLength HumanEval LeetCode CodeContests Figure6:TheprocessofCoTdifficultylabeling.

### ReasoningLen 7837.46 24606.85 40882.77

AnsweringLen 1985.59 2676.79 3192.45 • Positivesample:RandomlyselectaproblemwithasimilarCoT
lengthfromthedifficultycluster𝐶 𝑖 thatisthesameastheanchoredsample.
Consideringthis,wedecidedtousethek-meansclusteringalgo-
• Negativesample:Randomlychooseoneofthetwoclusters𝐶 𝑗
rithmtoclusterandanalyzethereasoninglengthsofallquestions.
and𝐶 𝑘 withdifferentdifficulties,andthenrandomlyselecta
Following the clustering process, three distinct difficulty levels,
problemwithadifferentCoTlengthfromthiscluster.
labeledas1,2,and3,wereidentified.Thatis,wewilllettheCoT
lengthsrecordedbyDeepSeekR1beusedasinputsinallproblems, Then,wecanusetripletdatatofine-tunetheCodeBERTemandusingthek-meansalgorithm,wewillclassifytheproblemsinto bedding model. The core objective of contrastive learning is to
3categoriesrepresentingthreedifferentlevelsofdifficulty:easy, bringquerieswithsimilarfeaturesandcomplexitiesclosertogether
medium,andhard.Andthen,theseclassificationresultswillbe whilepushingunrelatedquerieswithdifferentcomplexitiesfurther
incorporatedintothesubsequentCodeBERTfine-tuningprocess. apart[38].Thedesignoftripletdataenablesthemodeltolearn
semantic representations by associating the anchor query with
4.2.2 Contrastlosslearning. Thepurposeofcontrastlearningisto itspositivecounterparts,positioningthemcloserintheembedallowtheCodeBERTembeddertolearnthedifficultyinformation dingvectorspace.Onthecontrary,weexpectthemodeltopush
of the problem. After contrast learning process, the problem is unrelatedqueriesfartherawayfromtheanchorquery.
transformed into an embedding vector that will have difficulty Specifically,first,weuseCodeBERTtoextracttheembedding
information,whichisusefulforoursubsequentLLMselection. representations of each word in every query. These word-level
Incontrastlearning,optimizationprocessisdrivenbytriplet embeddingsareaggregatedthroughapoolinglayertogenerate
loss,whereeachtripletcomprisesananchorsample,apositivesam- fixed-sizesentence-levelembeddings.Wedenotethemappingof
ple,andanegativesample[23,50].Specifically,anchoredsamples problem𝑥 𝑖 into the embedding space R𝑝 by CodeBERT before
areproblemsthatrequireoptimizationoftheembeddingspace, fine-tuning as E(𝑥 𝑖;w). Based on this, we define the following
positivesamplesaresemanticallyofthesamedifficultyasanchored contrastivelossformula:
samples,andnegativesamplesaresemanticallyofadifferentdifficulty than anchored and positive samples. At this point three (cid:18) a·n a·p (cid:19)
clusters(𝐶 1 ,𝐶 2 ,𝐶 3)havebeenobtainedafterlabeling,representing 𝐿𝑜𝑠𝑠 =max 0, ∥a∥∥n∥ − ∥a∥∥p∥ +𝑚𝑎𝑟𝑔𝑖𝑛
thethreedifferentdifficultiesoftheproblem.Foreachanchored
=max(0,a·n−a·p+𝑚𝑎𝑟𝑔𝑖𝑛) (2)
problem𝑥 𝑖,thefollowingsamplingmethodisusedtoconstruct
pairsofpositiveandnegativesamples: • a=E(𝑥 ;w):Theembeddingoftheanchorsample.
anchor

<!-- Page 7 -->

AdaptiveLLM:AFrameworkforSelectingOptimalCost-EfficientLLMforCode-GenerationBasedonCoTLength Conferenceacronym’XX,June03–05,2018,Woodstock,NY
• p=E(𝑥 positive;w):Theembeddingofthepositivesample. orlarger.Sinceinferencespeedisnotaconsiderationinourevalu-
• n=E(𝑥 negative;w):Theembeddingofthenegativesample. ationframeworkandcostmetricsarestandardizedthroughcloud
serviceproviderplatforms,theuseofsinglevs.multi-GPUconfig-

### Thegoalofthislossformulaistolearnanembeddingspace

urationsdoesnotaffecttheexperimentaloutcomes.Considering
wheresemanticallysimilarsentencesareclosetoeachother,while
thattherearedifferencesinthedefaultparametersettingsofdiffersemanticallydifferentsentencesarefarfromeachother.The𝑚𝑎𝑟𝑔𝑖𝑛
entcodemodels,toensuretheconsistencyoftheexperiments,we
intheformulaisapositivevalue(bydefaultsetto1),whichis
standardizethemodelsettings:formodelswiththeirowndefault
usedtodefinetheminimumgapbetweenthedistancebetweenthe
parameters,theparametersettingsrecommendedbytheofficial
anchorandthepositivesampleandthedistancebetweentheanchor
areadopted;formodelswithoutprovideddefaultparameters,we
and the negative sample. This parameter ensures that negative
uniformlyset𝑑𝑜_𝑠𝑎𝑚𝑝𝑙𝑒 =𝑇𝑟𝑢𝑒,𝑡𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑒 =0.3,𝑡𝑜𝑝_𝑝 =0.95,
samplesarenotjustsimplypushedawayfrompositivesamplesbut
and𝑡𝑜𝑝_𝑘 =20.Additionally,allmodelsareimplementedusingthe
maintainameaningfuldistance.Inaddition,max(0,·)ensuresthat
HuggingFaceTransformerslibraryinPythonforloadingLLMs.
thelossvalueisnon-negative.Thismeansthatwhenthedistance
betweenthenegativesampleandtheanchorisalreadylargeenough, 5.1.2 Reasoning model used in experiments. Table 2 shows the
thelosswillbezero,indicatingthatthecurrenttripletdoesnot reasoningmodelsusedinourexperiments.Duringtheconstrucneedfurtherupdate. tionofAdaptiveLLM,weemployDeepSeek-R1-Distill-Qwen-32B
tomeasureandrecordtheCoTlength.Tovalidatetherationale
4.3 TrainingofXGBOOSTClassifier ofusingCoTlengthasaproxyforproblemcomplexity,weconductexperimentsinRQ1inSection6.1usingmultipleDeepSeek

### OnceCodeBERTisfine-tuned,itwillserveasafeatureextractor

R1variantswithdifferentparameterscales.Formodelswithrelafortheembeddinglayer,assistingtheXGBoostclassifier[13]in
tivelysmallerparametersizes,suchasDeepSeek-R1-Distill-QwensupervisedlearningusingtheLLMrankingdatasetconstructedin
1.5BandDeepSeek-R1-Distill-Qwen-7B,asingleRTX4090GPU
Section4.1.
isdeployedforinference.Conversely,modelswithlargerparame-
TherationaleforselectingXGBoostasthefinalclassifierisevitersizes,includingDeepSeek-R1-Distill-Qwen-14BandDeepSeekdent.Ourobjectiveistoconstructaframeworkforselectingthe

### R1-Distill-Qwen-32B,areusedviaAPI,withtheAPIservicealso

optimal code LLM that ensures both accuracy and minimal reprovidedbySiliconCloud(https://api.siliconflow.cn/v1).Although
sourceconsumption.Directlyincorporatinganeuralnetwork(NN)
weutilizedbothlocalandcloudservicedeploymentmethodsfor
intoCodeBERT’soutputlayerwouldcontradictourgoaldueto

### DeepSeek,weassumethattheirimpactonthefinalCoTlengthis

itssubstantialcomputationaldemands.Therefore,weoptedfor
negligible.Thisisbecausethedifferenceindeploymentonlyaffects
thelightweightclassifierarchitectureXGBoost,whichhasbeen
thespeedofinferencing,notthequalityoftheanswer.
validatedaseffectiveinpriorresearch[5,14].
Inourframework,theinputfeaturesaretheembeddingvectors
5.2 MetricsandBaselines
generatedbythefine-tunedCodeBERT,andthetargetlabelsarethe
optimalmodellabelscorrespondingtoeachproblem(specifically, 5.2.1 Metrics.
themodelthatattainsthehighestscorecalculatedbyScore𝑖 in • pass@k_score.Thismetricmeasurestheprobabilitythatatleast
Section4.1.2).Itshouldbenotedthatduringthetrainingprocess,
onecorrectsolutionisgeneratedamongthetopKanswers.Itis
theclassifierneverhasaccesstothetestsettoavoiddataleakage.
commonlyusedtoevaluatetheperformanceofcodegeneration
models.Ahigherpass@kindicatesabetterabilityofthemodel
5 ExperimentalSetups togeneratecorrectcodewithinthetopKresponses.
• pass@k_token.Thismetricrepresentstheaveragenumberof
5.1 StudiedModels
tokensconsumedperproblemduringthepass@ktest.Tokens
5.1.1 Modelcandidatepool. Table2showsthecodemodelsused
arethebasicunitsofinputandoutputinthemodel,andthequaninourframework.Toensurethatthemodelpoolcancovermodels
tityoftokensuseddirectlyreflectsthecomputationalresources
withdifferentparametersizes,weselectmultiplemodelsranging
requiredforthetest.
fromaminimumof1.5billionparameterstoamaximumof33 • pass@k_price.Thismetricindicatestheaveragecostperprobbillionparameters.Thisselectionaimstoprovidesuitablecode
lemincurredduringthepass@ktestandiscalculatedbymultiplymodelsinresponsetoproblemsofvaryingdifficulties.Theinferingthepass@k_tokenbytheinferencepricepertoken.Different
ence prices of the large language models listed in the table are
modelsmayhavedifferentpricingfortheirtokens,meaningthat
sourced from the SiliconCloud cloud inference platform (https:
thesamenumberoftokenscouldresultinsignificantlydifferent
//www.siliconflow.com/en/pricing).However,sincesomemodels
costsdependingonthemodel.Byusingpass@k_price,wecan
(suchasStarcoder2-15B-InstructandCodeLlama-7B-Instruct)have
more accurately reflect the true resource cost of running the
notbeenlistedonthisplatformyet,forthesemodelsthatarenot
pass@ktestforeachmodel.
covered,weassumethattheircostsareclosetothoseofmodels
withsimilarparametersizes.Therefore,weusethepricesofmodels 5.2.2 Baselines. Inourexperiments,wechooseComplexityNet
withsimilarparametersizesasalternativeestimates.ForcodeLLM [6]asthebaselinemethodforcomparison.Itscoremechanism
using,weuseRTX4090locallytodeploythesemodels.Asfaraswe involvespre-interactionsbetweenLLMsandtaskstodeterminethe
know,theNVIDIARTX4090GPUoffersonly24GBofVRAM,ne- complexityofthetasks.Specifically,theframeworkallowsLLMs
cessitatingmulti-GPUdeploymentformodelswith15Bparameters with varying capabilities (Code Llama, GPT-3.5, and GPT-4) to

<!-- Page 8 -->

Conferenceacronym’XX,June03–05,2018,Woodstock,NY Chengetal.
Table2:DetailedinformationofLLMsusedinourexperiments.WedonotreporttheAPIpriceforReasoningModelsbecause
thesemodelsareusedtoassessthedifficultyofcodingproblemsthroughCoTlengthratherthanbeingpartofthecandidate
modelsforselection.

### Type Model Size ModelLink APIPrice($/Mtokens)

Yi-Coder-1.5B 1.5B https://hf.co/01-ai/Yi-Coder-1.5B-Chat 0.14
Qwen2.5-Coder-1.5B-Instruct 1.5B https://hf.co/Qwen/Qwen2.5-Coder-1.5B-Instruct 0.14
CodeLlama-7B-Instruct 7B https://hf.co/meta-llama/CodeLlama-7b-Instruct-hf 0.42
Candidate Starcoder2-15B-Instruct 15B https://hf.co/bigcode/starcoder2-15b-instruct-v0.1 0.72
Pool DeepSeek-Coder-V2-Lite-Instruct 16B https://hf.co/deepseek-ai/DeepSeek-Coder-V2-Lite-instruct 0.72
Codestral-22B 22B https://hf.co/mistralai/Codestral-22B-v0.1 0.95
DeepSeek-Coder-33B-Instruct 33B https://hf.co/deepseek-ai/deepseek-coder-33b-instruct 1.26
Qwen2.5-Coder-32B-Instruct 32B https://hf.co/Qwen/Qwen2.5-Coder-32B-Instruct 1.26
DeepSeek-R1-Distill-Qwen-1.5B 1.5B https://hf.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B -
Reasoning DeepSeek-R1-Distill-Qwen-7B 7B https://hf.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B -
Models DeepSeek-R1-Distill-Qwen-14B 14B https://hf.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B -
DeepSeek-R1-Distill-Qwen-32B 32B https://hf.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B -
attemptsolvingthetasksmultipletimes.Basedonthecorrectness 70% to 30%. Specifically, the training set consists of 411 coding
ofthemodeloutputs,tasksareassigneddifficultylabels.These problems,whilethetestingsetincludes178codingproblems.For
labelsarethenusedbyasmallermodel,DaVinci-002[7],toclassify theimplementationofXGBoost,weutilizedtheXGBClassifierclass
andallocatetaskstothemostsuitablemodels. from the xgboost library to train the XGBoost model. Detailed
GiventhepotentialunavailabilityofcertainLLMs,wehaveim- parameterconfigurationsaredocumentedinourrepository.
plementedsubstitutionsinourexperimentalsetup.Specifically,we
haveemployedgpt-4o-2024-11-20asanalternativeforGPT-4and
6 ExperimentalResultsandAnalysis
Qwen2.5-7B-InstructasanalternativetoDaVinci-002.Thesealter-
ToassesstheeffectivenessofAdaptiveLLM,weconductathorough
nativemodelsarechosentocloselyapproximatetheperformance
evaluationaddressingthefollowingresearchquestions:
ofthemodelsthatweusedinAdaptiveLLM,therebyensuringthe
reliability,fairnessandvalidityoftheexperimentalresults.
• RQ1:RationalityAnalysis-Howdoesthedifficultyassessed
bytheCoTlengthgeneratedbyreasoningmodelscomparewith
thetruedifficultylabels?Isitreasonable?Isitaffectedbythe
5.3 ImplementationDetails
parametersizeofthereasoningmodels?
InSection4.2,duringthefine-tuningofCodeBERT,weemployed • RQ2:OverallPerformance-HowdoesAdaptiveLLMperform
theAutoTokenizerandAutoModelclassesfromtheHuggingFace
onthetestsetmetricscomparedtoasingleLLMandbaseline
Transformerslibrary.Andforencoder-onlyarchitectureslikeBERT,
method?
themaximuminputsequencelengthis512.Consequently,weap- • RQ3:AblationStudy-Whatistheimpactoftheembedding
pliedtruncationtoinputsexceedingthislimit,withimplementation
layerfine-tuninginAdaptiveLLMontheoverallperformance?
detailsdocumentedinourrepository.Thisstrategyisrational.Becauseproblemdescriptionstypicallyappearatthebeginningof
6.1 RQ1:RationalityAnalysis
inputsequences,ensuringthattheessentialsemanticinformation
remainspreservedingeneratedembeddingvectors. 6.1.1 RQ1-1:Isthereasignificantdifferencebetweenthedifficulty
InSection4.2.1,welogtheoptimalCoTlengthforreasoning assessedbyCoTlengthandthetruedifficultylabels? IntheLeetCodemodels.GiventhevariabilityinthelengthsofCoT,weemploythe SampleandCodeContestsdatasets,difficultylabelsareassigned
DeepSeek-R1-Distill-Qwen-32Bmodeltogeneratetenresponses basedonhumanperformance.Specifically,thedifficultyinLeetforeachproblem.Themedianlengthoftheseresponsesisselected CodeSampleisdeterminedbytheacceptancerate(acRate),and
astheoptimalCoTlengthforeachproblem.Thisapproachensures CodeContestsreliesoncompetitionratings(cf_rating).Thesemetthatthechosenlengthreflectsthecomplexityoftheproblem.The ricsreflecttheactualperformanceofhumansolversintermsof
samemethodologyisappliedinSection6.1togetCoTlengthsfor successrates.
reasoningmodelswithvaryingparametersizes. Toenablecomparativeanalysis,weemploytheK-meansclus-
Wecapthemaximumnumberoftokensgeneratedbyreasoning teringalgorithmoneachdatasettoclassifyproblemswithactual
modelsat16384.Thissettingallowsmostproblemstogenerate difficultylabelsintotwocategories:easyandhard.Wethenapply
completeCoT.However,forexceptionallycomplexproblemswhere thesamebinaryclassificationtothedifficultylabelsgeneratedby
theCoTlengthexceedsthislimit,werecordthelengthas0and theDeepSeek-R1-Distill-Qwen-32Bmodel,whicharebasedonthe
excludetheseinstancesfromourdataset.Forcodemodelsinmodel CoTlength.Throughthisprocess,wecomparethemodel’sprecandidatepool,wesetthemaximumnumberoftokensto2048, dicteddifficultyagainstthetruedifficultyandconstructaconfusion
ensuringcompleteresponsesforallproblemswithouttruncation. matrixtoanalyze.
InSection4.3,duringXGBoosttrainingprocess,thedatasetis AsshowninFigure7,evenunderthebinaryclustering,there
randomlydividedintotrainingandtestingsubsetsataratioof isasignificantdifferencebetweenthedifficultyassessedbyCoT

<!-- Page 9 -->

AdaptiveLLM:AFrameworkforSelectingOptimalCost-EfficientLLMforCode-GenerationBasedonCoTLength Conferenceacronym’XX,June03–05,2018,Woodstock,NY
0 1
Human Label
lebaL
B23-newQ-llitsiD-1R-keeSpeeD
0
1
60
44 23
50
40
34 64
30
0 1

### Human Label

(a) Confusion Matrix of CodeContests
lebaL
B23-newQ-llitsiD-1R-keeSpeeD
0
1
99 77 80  
60
40  
11 73
20
 
(b) Confusion Matrix of LeetCodeSample
Figure7:TheconfusionmatrixbetweenCoTdifficultyand
truedifficulty.
  
lengthandthetruedifficultylabels.Specifically,intheCodeContestsdataset,atotalof57problemswereclassifiedintodifferent   
difficultycategoriesbythetwomethods,whileintheLeetCodeSam-
 + X P D Q  ' L I I L F X O W \  ' H H S 6 H H N  5   ' L V W L O O  4 Z H Q    %  7 K L Q N L Q J  / H Q J W K
pledataset,thisnumberreached88.Notably,intheLeetCodeSample
dataset,77problemslabeledas"hard"(label1)bythetruelabels
wereclassifiedas"easy"(label0)bytheCoTlengthassessment.
ThisfindingindicatesasubstantialdifferencebetweenthedifficultylabelsassignedbytheR1modelbasedonCoTlengthandthe
originaldifficultylabelsinthedataset.

### Theoriginaldifficultylabelswerecreatedbyhumans,butthe

actualproblem-solvingisdonebyLLMs.Ifweusethedifficulty
withwhichhumansviewaquestiontoguideLLMinansweringthe
question,itmaybebiased.So,isLLM’sperceptionofthedifficulty
ofthequestionismoreinlinewithLLM’sperspectiveofanswering
thequestion?
6.1.2 RQ1-2:WhichdifficultyassessmentmethodismorepracticalforLLM?. Giventheinconsistencyindifficultyassessment,we
designandconductthefollowingexperiment.Afterloggingthe
CoT lengths, we normalized the extracted CoT lengths using a
normaldistributionnormalizationtoensurecomparabilityofthe
data. Meanwhile, each problem in the LeetCodeSample dataset
isaccompaniedbyadifficultylabelbasedonhumanperception,
which is defined as 1−𝑎𝑐𝑅𝑎𝑡𝑒. Problems with higher difficulty
haveloweracceptancerates,resultinginhigherdifficultyscores.

### TofacilitatecomparisonwiththeCoTlength,wealsonormalize

thesehumanperception-baseddifficultylabelsusingthesamenormaldistributionnormalization.Finally,weextractproblemsfrom
LeetCodeSample that could be correctly answered by Qwen2.5-
Coder-32B-Instructandcreatboxplotfortheseproblemsbasedon
thenormalizeddifficultydatafrombothmethods.

### TheboxplotisshowninFigure8.Giventhattheselecteddata

arefromproblemsthatthelargemodelcananswercorrectly,itis
expectedthatthedifficultylabelsoftheseproblemswouldgenerally
below.Meanwhile,thecorrespondingCoTlengthsofthereasoning
modelwouldberelativelyshort.Asobservedfromtheboxplot,
approximately75%oftheproblemshaveCoTlengthslessthan0.
Thisindicatesthatthemajorityofthedifficultylabelsbasedonthe
reasoningmodel’sCoTlengthsarerelativelysimple,whichaligns
withourselectionofproblemsthatLLMscancorrectlyanswer.

### However,forthehumanlabeleddata,manyscoresareabove0,

indicatingthattheactualprogrammersstillconsidertheseselected
problemstohaveacertainlevelofdifficulty.Thisisinconsistent

##  V H X O D 9  G H ] L O D P U R 1

Figure8:TheboxplotforcomparisonofCoTdifficultyand
truedifficulty.
withtheperformanceofLLMsonthequestions,asLLMsanswer
allofthesequestionscorrectly.
Moreover,theoveralldistributionofthedifficultylabelsbased
onCoTlengthismoreconcentratedcomparedtothosebasedon
humanperception.ThisimpliesthatCoTlengthtendstoreflectthat
thesepromblemsaregenerallysimple.However,therearesome
outliersintheCoTlengthdata.Theseoutliersexhibitsignificantly
longerCoTlengthsthatdeviatefromthemajorityofthedistribution.

### ThisobservationunderscoresthatCoTstilldemonstratesadegree

ofuncertainty,potentiallyovercomplicatingsomeotherwisesimple
problems.ButitisstillreasonabletoapplyCoTlengthforthefew
caseswhichcanbeignored.

### TheresultsoverallindicatethatusingCoTlengthasacriterion

for classifying problem difficulty is rational. More importantly,
comparedtothehumandifficultylabels,itmaymoreaccurately
reflecttheactualperformanceofLLMsincodegenerationtasks.
Forexample,certainlogicalreasoningproblemsthatarecomplex
forhumansmayberelativelystraightforwardforLLMs,whilesome
challengesthataredifficultforLLMsmightbeeasyforhumans.

### Suchphenomenaarenotuncommoninthereasoningprocessesof

LLMs.Webelievethisfindingprovidesvaluableinsightsandopens
newperspectivesforfutureresearch.
Table3:ThecomparisonofCoTlengthgeneratedbymodels
withdifferentparametersizes.

### ModelGroup ARI FMI


## 5B-14B 0.4650 0.6538


## 7B-14B 0.6540↑0.189 0.7778↑0.124


## 5B-32B 0.3476 0.5845


## 7B-32B 0.4845↑0.1369 0.6741↑0.0896


## 14B-32B 0.5711↑0.2235 0.7271↑0.1426

6.1.3 RQ1-3:WhatarethedifferencesinCoTlengthsgeneratedby
reasoningmodelsofdifferentparametersizes? WefurtherinvestigatewhetherthesizeofmodelparametersaffectstheCoTlength

<!-- Page 10 -->

Conferenceacronym’XX,June03–05,2018,Woodstock,NY Chengetal.
Table4:PerformancecomparisonbetweenAdaptiveLLMandbaselines.
pass@1 pass@5

### Model

score token price($) score token price($)
Yi-Coder-1.5B 26.41% 329.02 4.61e-05 35.96% 1659.47 23.23e-05
Qwen2.5-Coder-1.5B-Instruct 29.78% 390.71 5.47e-05 39.33% 1904.76 26.67e-05
CodeLlama-7B-Instruct 17.98% 522.68 21.95e-05 29.21% 2472.89 103.86e-05
Starcoder2-15B-Instruct 29.21% 193.47 13.93e-05 39.89% 957.97 68.97e-05
DeepSeek-Coder-V2-Lite-Instruct 49.44% 563.68 40.58e-05 58.43% 2837.76 204.32e-05
Codestral-22B 44.38% 476.48 45.27e-05 52.81% 2383.47 226.43e-05
DeepSeek-Coder-33B-Instruct 39.89% 359.61 45.31e-05 49.44% 1839.34 231.76e-05
Qwen2.5-Coder-32B-Instruct 57.87% 763.57 96.21e-05 71.35% 3834.90 483.20e-05

### GPT3.5 35.39% 130.42 19.56e-05 45.51% 646.28 96.94e-05


### GPT4o 60.67% 551.62 551.62e-05 72.47% 2741.79 2741.79e-05

ComplexityNet 37.08% 380.30 256.83e-05 50.56% 1951.39 1306.66e-05
AdaptiveLLM 44.94%↑7.86 428.80↑48.5 28.49e-05↓228.34 56.18%↑5.62 2094.98↑143.59 140.07e-05↓1166.59
AdaptiveLLM(w/ofinetune) 43.82%↓1.12 411.84↓16.96 26.74e-05↓1.75 55.62%↓0.56 2037.09↓57.89 133.99e-05↓6.08
anditscorrespondingdifficultyclassification.Toaddressthisques- ResultsdemonstratethatAdaptiveLLMframeworkexhibitssigtion, we select DeepSeek-R1-Distill-Qwen models with varying nificantperformanceadvantages.Intermsofaccuracy,theAdapparametersizes(1.5B,7B,14B,and32B),extracttheCoTlengths tiveLLMframeworkachievespass@1scoreof44.94%andpass@5
generatedbyeachmodel,andconductclusteringanalysisonthese scoreof56.18%.TheseresultsnotonlysurpassthoseoftheCodestraldata.Subsequently,wecomparethedifficultyclassificationsofdif- 22Bmodelwith22Bparameters(pass@1scoreof44.38%andpass@5
ferentparametersizemodelsinapairwisemanner. scoreof55.28%),butalsoshowaclearsuperioritycomparedto
Theresultsrevealthattheconsistencyofdifficultyclassification thelarger-parameterDeepSeek-Coder-33B-Instructmodel(pass@1
significantlyincreasesasthemodelparametersizegrows.Inthe scoreof39.89%andpass@5scoreof49.44%).Notably,whilemainclusteringcomparisonamongthe1.5B,7B,14B,and32Breasoning taining a high level of accuracy, the token consumption of the
models,itisobservedthatastheparametersizeincreases,their AdaptiveLLMframework(pass@1:428.80andpass@5:2094.98)
classificationresultsgraduallyconvergewiththoseofthe32BR1 issignificantlylowerthanthatofmostlarger-parametermodels,
reasoningmodel.ThistrendisquantifiedusingtheAdjustedRand suchasQwen2.5-Coder-32B-Instruct(pass@1:763.57andpass@5:
Index(ARI)andFowlkes-MallowsIndex(FMI),asshowninTable3. 3834.90).
Thesemetricsmeasurethesimilaritybetweentheclusteringresults Intermsofcost-effectiveness,AdaptiveLLMframeworkdemonofmodelswithdifferentparametersizes.Resultsshowthatmodel stratesremarkableeconomicefficiency.Itsinferencecost(pass@1:
group with closer parameter sizes achieve higher ARI and FMI 28.49e-05$andpass@5:140.07e-05$)iscomparabletoCodeLlamavalues,indicatingstrongerconsistencyindifficultyclassification. 7B-Instructmodel(pass@1:21.95e-05$andpass@5:103.86e-05$),
Forexample,theARIandFMIvaluesbetweenthe14Band32B whileachievingsignificantlyhigheraccuracy.Comparedtolargermodelsare0.5711and0.7271,respectively,whilethecorresponding parametermodels,thecostcontroladvantageoftheAdaptiveLLM
valuesbetweenthe1.5Band32Bmodelsareonly0.3476and0.5845. frameworkisevenmoreevident.Forexample,comparedtothe
Thisfindingsuggeststhatsmallermodelsexhibitrandomnessin Codestral-22Bmodel(pass@1:45.27e-05$andpass@5:226.43e-05$),
CoTlength,leadingtolessstableclassifications.Incontrast,larger theAdaptiveLLMframeworkreducesinferencecostbyapproximodelsshowastrongercorrelationbetweenCoTlengthandactual mately37%whilemaintainingacertainlevelofaccuracy.
difficulty,improvingclassificationstabilityandreliability.
AnswertoRQ1:ThedifficultyassessmentbasedonCoTlength 6.2.2 RQ2-2:HowdoestheoverallperformanceofAdativeLLMcomofreasoningmodelsdiffersfromhuman.Nevertheless,theCoT parewithsotabaselinemethod? TocomprehensivelyevaluateAdaplengthmethodseemstobetterreflecttheactualperformanceof tiveLLMagainstthestate-of-the-artbaselinemethodComplexi-
LLMswhensolvingproblems.Andreasoningmodelswithlarger tyNet[6],weanalyzebothaccuracyandcost-efficiencymetrics.
parametersizestendtogeneratemorestableandconsistentCoT. AdaptiveLLMachievesapass@1scoreof44.94%,outperforming
ComplexityNetby7.86%,whileconsumingmoderatelymoretokens(428.80vs.380.30).Thisaccuracygainismaintainedinpass@5,
whereAdaptiveLLMscores56.18%,surpassingComplexityNetby
6.2 RQ2:OverallPerformance
5.62%.Thetokenincrease(143.59tokensforpass@5)isstrategically
6.2.1 RQ2-1:HowdoestheoverallperformanceofAdativeLLMcom- offsetbytheframework’sdynamicmodelselection,whichprioriparewithsingleLLM?. Table4presentsadetailedcomparisonof tizescost-effectiveinferencewithoutcompromisingperformance.
keymetrics,includingpass@1andpass@5score,tokenconsump- Themoststrikingadvantageliesincostreduction.Forpass@1,
tion,andinferencecost,foreightcodeLLMsandtheAdaptiveLLM AdaptiveLLMreducesinferencecostsby88.3%comparedtoComframeworkonthebenchmarkdataset. plexityNet,achievedthroughadaptiveroutingoftaskstosmaller

<!-- Page 11 -->

AdaptiveLLM:AFrameworkforSelectingOptimalCost-EfficientLLMforCode-GenerationBasedonCoTLength Conferenceacronym’XX,June03–05,2018,Woodstock,NY
LLMs(e.g.,Yi-Coder-1.5B)forsimplecasesandreservinglarger AnswertoRQ3:Theexperimentalresultsconfirmedtheeffectivemodels(e.g.,Qwen2.5-Coder-32B)forcomplexscenarios.Inpass@5, nessofthefine-tuningstrategybasedonCodeBERT.Byincorpothecostreductionreaches88.9%. ratingproblemdifficultylabelinformation,theframeworkwas
FurtheranalysisrevealsthatAdaptiveLLMachieves82.5%costre- abletobetterunderstandtaskcharacteristicsandmakemore
ductioncomparedtoGPT-4o(28.49e-05$vs.551.62e-05$inpass@1) optimalmodelselectiondecisions.
whileretaining73.6%ofGPT-4o’saccuracy(44.94%vs.60.67%).This
explainswhyComplexityNetincurssignificantlyhigherresource
7 ThreatstoValidity
consumption—itreliesheavilyonclosed-sourcemodelslikeGPT,
whosehighAPIpricingdrivesupinferencecostscomparedtoAdap- Internalvalidity.Onepotentialthreatistherandomnessinthe
tiveLLM.Whileclosed-sourcemodelsdemonstratebetteraccuracy generationofCoTbyreasoningLLMs.Tomitigatethis,wegenerperformance compared with high-parameter open-source mod- atedtenresponsesforeachproblemandusedthemedianlength
els,theirinferencecostsaresubstantiallyhigher.Thisdifference oftheseresponsesastheCoTlengthforthatproblem.Another
highlightsacriticalinsightforfuturemodelselection:prioritizing concernisthat,duetoresourceconstraints,forasmallnumberof
open-sourcemodelsincandidatepoolscanachievecompetitive extremelycomplexproblems,theCoTlengthexceededthemaxperformanceatafractionofthecost,offeringamoresustainable imumtokenlimitsetformodelgeneration.However,sincesuch
approachtobalancingaccuracyandeconomicefficiency. sampleswererare,theywereexcludedfromthedataset.Whilethis
AnswertoRQ2:AdaptiveLLMachievesperformancewith44.94% exclusionmayintroducesomebias,itsimpactisminimalgiventhe
pass@1and56.18%pass@5scores,outperformingbothsingle smallproportionofaffectedsamples.
largeLLMandComplexityNetbaselineby+7.86%inpass@1.It Externalvalidity.InourCoTdifficultyassessmentmethod,the
significantlyreducesinferencecostscomparedtoComplexityNet, datasetsweselectedareprimarilyfocusedonsingle-filecodegendemonstratingexceptionalcost-effectiveness. erationtasksanddonotinvolvemulti-fileinteractionsorcollaborations.Asaresult,ourmethodmayfacechallengeswhenapplied
toproject-levelcodegenerationtasks.
6.3 RQ3:AblationStudy Constructvalidity.Inourexperiments,modelcostsweresourced
from the SiliconFlow cloud platform. For models not deployed
Throughthedesignofablationexperiments,wecomparedandanaonthisplatform,weapproximatedtheircostsusingmodelswith
lyzedtheperformancedifferencesoftheAdaptiveLLMframework
similarparametersizes.However,inferencecostsdependnotonly
intermsofpass@1andpass@5accuracy,tokenconsumption,and
onparametersizebutalsoonarchitectureandinferencestrategies.
inferencecostbeforeandafterCodeBERTfine-tuning.Asshown

### Forinstance,underthesameparametersize,Mixture-of-Experts

inTable4,theAdaptiveLLMframeworkfine-tunedwithdifficulty-
(MoE)models[30,31]typicallyhavelowerinferencecostsdueto
awaretuningexhibitedsignificantimprovementsacrossallmetrics.
theirreducednumberofactiveparametersduringruntime.Despite

### Intermsofaccuracy,thefine-tunedframeworkachieveda1.12

theselimitations,parametersizeisstillapracticalproxyforcost
percentagepointincreaseinthepass@1metric(from43.82%to
estimation,acknowledgingthepotentialforminorbias.
44.94%)anda0.56percentagepointincreaseinthepass@5metric
(from55.62%to56.18%).Thisimprovementindicatesthatdifficulty-
8 Conclusion
aware fine-tuning effectively enhanced the framework’s ability
tounderstandthecomplexityofproblems,therebyenablingitto Inthispaper,weproposeAdaptiveLLM,aframeworkthatuses
moreaccuratelyselectappropriatemodelsforhandlingproblems theCoTlengthofreasoningmodelstoevaluateproblemcomplexofvaryingdifficultylevels. ityanddynamicallyselectcodeLLMs.Toconstructthedataset,
Regardingcomputationalefficiencyandcost-effectiveness,the we integrate samples of varying difficulty levels and employ a
fine-tunedframeworkdemonstratedsuperiortokenconsumption scoringformulatoidentifytheoptimalLLMforeachproblemas
andinferencecostefficiency.Althoughtherewasaslightincrease ground-truthannotations.Forcomplexitylabeling,weutilizethe
intokenconsumption(pass@1from411.84to428.80,pass@5from reasoningmodelDeepSeek-R1-Distill-Qwen-32BtogenerateCoT
2037.09to2094.98)andamarginalriseininferencecost(pass@1 sequences,recordtheirlengths,andapplyk-meansclusteringto
from26.74e-05to28.49e-05,pass@5from133.99e-05to140.07e-05), categorizeproblemsintothreedifficultytiers.Basedonthesedifthisincreasewaspositivelycorrelatedwiththeimprovementin ficulty labels,we perform tripletcontrastivefine-tuning on the
accuracy,indicatingthattheadditionaltokenandinferencecost embeddinglayerofCodeBERT,enablingproblemembeddingsto
expenditurebroughtabouteffectiveperformancegains.Further- encodecomplexity-awarefeaturesthatenhancemodelselection.
more,in-depthanalysisrevealedthatformoredifficultproblems, Finally,wesplittheconstructeddatasetintotrainingandtestsets
theAdaptiveLLMframeworkwithoutfine-tuningstilltendedto totrainanXGBoostclassifier.Experimentalresultsvalidatethe
selectsmaller-parametermodelssuchasYi-Coder-1.5B-Chatand rationalityofdifficultyassessmentmethodbasedonCoTlength
Qwen2.5-Coder-1.5B-Instruct,whichmayhaveledtoinsufficientca- andeffectivenessofAdaptiveLLMframework.Wereleaseallcode
pabilityinhandlingcomplexproblems.Incontrast,theframework publiclyathttps://github.com/cjhCoder7/AdaptiveLLM.
fine-tunedwithdifficulty-awaretuningwasabletomoreaccurately
identifyproblemdifficultyandaccordinglyselectlarger-parameter Acknowledgments
modelssuitableforcomplexproblems,therebysignificantlyen-
ThisworkissupportedbytheNationalNaturalScienceFoundation
hancingoverallperformance.
ofChinaGrantsNo.62302021.

<!-- Page 12 -->

Conferenceacronym’XX,June03–05,2018,Woodstock,NY Chengetal.

### References

[26] DongfuJiang,XiangRen,andBillYuchenLin.2023.Llm-blender:Ensembling
[1] JoshAchiam,StevenAdler,SandhiniAgarwal,LamaAhmad,IlgeAkkaya,Floren- largelanguagemodelswithpairwiserankingandgenerativefusion. arXiv
ciaLeoniAleman,DiogoAlmeida,JankoAltenschmidt,SamAltman,Shyamal preprintarXiv:2306.02561(2023).
Anadkat,etal.2023. Gpt-4technicalreport. arXivpreprintarXiv:2303.08774 [27] CarlosEJimenez,JohnYang,AlexanderWettig,ShunyuYao,KexinPei,Ofir
(2023). Press,andKarthikNarasimhan.2023.Swe-bench:Canlanguagemodelsresolve
[2] Anysphere.2009.Codeforces. https://codeforces.com/ real-worldgithubissues?arXivpreprintarXiv:2310.06770(2023).
[3] Anysphere.2015.LeetCode. https://leetcode.com/ [28] BonanKou,ShengmaiChen,ZhijieWang,LeiMa,andTianyiZhang.2023.Is
[4] Anysphere.2023.Cursor. https://www.cursor.com/ modelattentionalignedwithhumanattention?anempiricalstudyonlarge
[5] ZelihaErgulAydinandZehraKamisliOzturk.2021. Performanceanalysisof languagemodelsforcodegeneration.arXivpreprintarXiv:2306.01220(2023).
XGBoostclassifierwithmissingdata.ManchesterJournalofArtificialIntelligence [29] YujiaLi,DavidChoi,JunyoungChung,NateKushman,JulianSchrittwieser,Rémi
andAppliedSciences(MJAIAS)2,02(2021),2021. Leblond,TomEccles,JamesKeeling,FelixGimeno,AgustinDalLago,etal.2022.
[6] HenryBae,AghyadDeeb,AlexFleury,andKehangZhu.2023.Complexitynet: Competition-levelcodegenerationwithalphacode. Science378,6624(2022),
Increasingllminferenceefficiencybylearningtaskcomplexity.arXivpreprint 1092–1097.
arXiv:2312.11511(2023). [30] AixinLiu,BeiFeng,BinWang,BingxuanWang,BoLiu,ChenggangZhao,
[7] TomBrown,BenjaminMann,NickRyder,MelanieSubbiah,JaredDKaplan, ChengqiDengr,ChongRuan,DamaiDai,DayaGuo,etal.2024. Deepseek-
PrafullaDhariwal,ArvindNeelakantan,PranavShyam,GirishSastry,Amanda v2:Astrong,economical,andefficientmixture-of-expertslanguagemodel.arXiv
Askell,etal.2020.Languagemodelsarefew-shotlearners.Advancesinneural preprintarXiv:2405.04434(2024).
informationprocessingsystems33(2020),1877–1901. [31] AixinLiu,BeiFeng,BingXue,BingxuanWang,BochaoWu,ChengdaLu,Cheng-
[8] GAnnCampbell.2018.CognitiveComplexity-Anewwayofmeasuringunder- gangZhao,ChengqiDeng,ChenyuZhang,ChongRuan,etal.2024.Deepseek-v3
standability.SonarSourceSA10(2018). technicalreport.arXivpreprintarXiv:2412.19437(2024).
[9] FedericoCassano,JohnGouwar,DanielNguyen,SydneyNguyen,LunaPhipps- [32] JiaweiLiu,ChunqiuStevenXia,YuyaoWang,andLingmingZhang.2023.Isyour
Costin,DonaldPinckney,Ming-HoYee,YangtianZi,CarolynJaneAnderson, codegeneratedbychatgptreallycorrect?rigorousevaluationoflargelanguage
MollyQFeldman,etal.2022.Multipl-e:Ascalableandextensibleapproachto modelsforcodegeneration.AdvancesinNeuralInformationProcessingSystems
benchmarkingneuralcodegeneration.arXivpreprintarXiv:2208.08227(2022). 36(2023),21558–21572.
[10] LingjiaoChen,MateiZaharia,andJamesZou.2023.Frugalgpt:Howtouselarge [33] SiyaoLiu,HeZhu,JerryLiu,ShulinXin,AoyanLi,RuiLong,LiChen,JackYang,
languagemodelswhilereducingcostandimprovingperformance.arXivpreprint JinxiangXia,ZYPeng,etal.2024.Fullstackbench:Evaluatingllmsasfullstack
arXiv:2305.05176(2023). coder.arXivpreprintarXiv:2412.00535(2024).
[11] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde [34] AntonLozhkov,RaymondLi,LoubnaBenAllal,FedericoCassano,JoelLamy-
DeOliveiraPinto,JaredKaplan,HarriEdwards,YuriBurda,NicholasJoseph, Poirier,NouamaneTazi,AoTang,DmytroPykhtar,JiaweiLiu,YuxiangWei,
GregBrockman,etal.2021.Evaluatinglargelanguagemodelstrainedoncode. etal.2024. Starcoder2andthestackv2:Thenextgeneration. arXivpreprint
arXivpreprintarXiv:2107.03374(2021). arXiv:2402.19173(2024).
[12] ShuhaoChen,WeisenJiang,BaijiongLin,JamesKwok,andYuZhang.2024. [35] HaipengLuo,QingfengSun,CanXu,PuZhao,JianguangLou,ChongyangTao,
RouterDC:Query-basedrouterbydualcontrastivelearningforassemblinglarge XiuboGeng,QingweiLin,ShifengChen,andDongmeiZhang.2023.Wizardmath:
languagemodels.AdvancesinNeuralInformationProcessingSystems37(2024), Empoweringmathematicalreasoningforlargelanguagemodelsviareinforced
66305–66328. evol-instruct.arXivpreprintarXiv:2308.09583(2023).
[13] TianqiChenandCarlosGuestrin.2016.Xgboost:Ascalabletreeboostingsystem. [36] AlexMallen,AkariAsai,VictorZhong,RajarshiDas,DanielKhashabi,and
InProceedingsofthe22ndacmsigkddinternationalconferenceonknowledge HannanehHajishirzi.2022. Whennottotrustlanguagemodels:Investigatdiscoveryanddatamining.785–794. ingeffectivenessofparametricandnon-parametricmemories. arXivpreprint
[14] ZhuoChen,FuJiang,YijunCheng,XinGu,WeirongLiu,andJunPeng.2018. arXiv:2212.10511(2022).
XGBoostclassifierforDDoSattackdetectionandanalysisinSDN-basedcloud. [37] NiklasMuennighoff,QianLiu,ArmelZebaze,QinkaiZheng,BinyuanHui,
In2018IEEEinternationalconferenceonbigdataandsmartcomputing(bigcomp). TerryYueZhuo,SwayamSingh,XiangruTang,LeandroVonWerra,andShayne
IEEE,251–256. Longpre.2023. Octopack:Instructiontuningcodelargelanguagemodels.In
[15] ChristofEbert,JamesCain,GiulianoAntoniol,SteveCounsell,andPhillipLa- NeurIPS2023WorkshoponInstructionTuningandInstructionFollowing.
plante.2016.Cyclomaticcomplexity.IEEEsoftware33,6(2016),27–29. [38] AaronvandenOord,YazheLi,andOriolVinyals.2018.Representationlearning
[16] ZhangyinFeng,DayaGuo,DuyuTang,NanDuan,XiaochengFeng,MingGong, withcontrastivepredictivecoding.arXivpreprintarXiv:1807.03748(2018).
LinjunShou,BingQin,TingLiu,DaxinJiang,etal.2020.Codebert:Apre-trained [39] OpenAI.2024.OpenAIo1. https://openai.com/o1/
modelforprogrammingandnaturallanguages.arXivpreprintarXiv:2002.08155 [40] OpenAI.2025.OpenAIo3mini. https://openai.com/index/openai-o3-mini/
(2020). [41] Gabriel Orlanski, Kefan Xiao, Xavier Garcia, Jeffrey Hui, Joshua Howland,
[17] Github.2021.GithubCopilot. https://github.com/features/copilot JonathanMalmaud,JacobAustin,RishabhSingh,andMicheleCatasta.2023.
[18] AaronGrattafiori,AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,Abhishek Measuringtheimpactofprogramminglanguagedistribution.InInternational
Kadian,AhmadAl-Dahle,AieshaLetman,AkhilMathur,AlanSchelten,Alex ConferenceonMachineLearning.PMLR,26619–26645.
Vaughan,etal.2024.Thellama3herdofmodels.arXivpreprintarXiv:2407.21783 [42] ShuyinOuyang,JieMZhang,MarkHarman,andMengWang.2025.Anempirical
(2024). studyofthenon-determinismofchatgptincodegeneration.ACMTransactions
[19] DayaGuo,DejianYang,HaoweiZhang,JunxiaoSong,RuoyuZhang,Runxin onSoftwareEngineeringandMethodology34,2(2025),1–28.
Xu,QihaoZhu,ShirongMa,PeiyiWang,XiaoBi,etal.2025. Deepseek-r1: [43] BaptisteRoziere,JonasGehring,FabianGloeckle,StenSootla,ItaiGat,Xiao-
Incentivizingreasoningcapabilityinllmsviareinforcementlearning. arXiv qingEllenTan,YossiAdi,JingyuLiu,RomainSauvestre,TalRemez,etal.2023.
preprintarXiv:2501.12948(2025). Codellama:Openfoundationmodelsforcode.arXivpreprintarXiv:2308.12950
[20] DayaGuo,QihaoZhu,DejianYang,ZhendaXie,KaiDong,WentaoZhang, (2023).
GuantingChen,XiaoBi,YuWu,YKLi,etal.2024.DeepSeek-Coder:Whenthe [44] GeminiTeam,PetkoGeorgiev,VingIanLei,RyanBurnell,LibinBai,Anmol
LargeLanguageModelMeetsProgramming–TheRiseofCodeIntelligence.arXiv Gulati,GarrettTanzer,DamienVincent,ZhufengPan,ShiboWang,etal.2024.
preprintarXiv:2401.14196(2024). Gemini1.5:Unlockingmultimodalunderstandingacrossmillionsoftokensof
[21] NehaGupta,HarikrishnaNarasimhan,WittawatJitkrittum,AnkitSinghRawat, context.arXivpreprintarXiv:2403.05530(2024).
AdityaKrishnaMenon,andSanjivKumar.2024. Languagemodelcascades: [45] GemmaTeam,ThomasMesnard,CassidyHardin,RobertDadashi,SuryaBhupati-
Token-leveluncertaintyandbeyond.arXivpreprintarXiv:2404.10136(2024). raju,ShreyaPathak,LaurentSifre,MorganeRivière,MihirSanjayKale,Juliette
[22] THariprasad,GVidhyagaran,KSeenu,andChandrasegarThirumalai.2017.Soft- Love,etal.2024.Gemma:Openmodelsbasedongeminiresearchandtechnology.
warecomplexityanalysisusinghalsteadmetrics.In2017internationalconference arXivpreprintarXiv:2403.08295(2024).
ontrendsinelectronicsandinformatics(ICEI).IEEE,1109–1113. [46] KimiTeam,AngangDu,BofeiGao,BoweiXing,ChangjiuJiang,ChengChen,
[23] EladHofferandNirAilon.2015.Deepmetriclearningusingtripletnetwork.In ChengLi,ChenjunXiao,ChenzhuangDu,ChonghuaLiao,etal.2025.Kimik1.5:
Similarity-basedpatternrecognition:thirdinternationalworkshop,SIMBAD2015, Scalingreinforcementlearningwithllms.arXivpreprintarXiv:2501.12599(2025).
Copenhagen,Denmark,October12-14,2015.Proceedings3.Springer,84–92. [47] MistralAIteam.2024.Codestral. https://mistral.ai/news/codestral
[24] BinyuanHui,JianYang,ZeyuCui,JiaxiYang,DayihengLiu,LeiZhang,Tianyu [48] HugoTouvron,LouisMartin,KevinStone,PeterAlbert,AmjadAlmahairi,Yas-
Liu,JiajunZhang,BowenYu,KemingLu,etal.2024.Qwen2.5-codertechnical mineBabaei,NikolayBashlykov,SoumyaBatra,PrajjwalBhargava,ShrutiBhosreport.arXivpreprintarXiv:2409.12186(2024). ale,etal.2023. Llama2:Openfoundationandfine-tunedchatmodels. arXiv
[25] SoyeongJeong,JinheonBaek,SukminCho,SungJuHwang,andJongCPark. preprintarXiv:2307.09288(2023).

## Adaptive-rag:Learningtoadaptretrieval-augmentedlargelanguagemodels [49] Chung-YuWang,AlirezaDaghighFarsoodeh,andHungVietPham.2024.Selecthroughquestioncomplexity.arXivpreprintarXiv:2403.14403(2024). tionofPromptEngineeringTechniquesforCodeGenerationthroughPredicting

CodeComplexity.arXivpreprintarXiv:2409.16416(2024).

<!-- Page 13 -->

AdaptiveLLM:AFrameworkforSelectingOptimalCost-EfficientLLMforCode-GenerationBasedonCoTLength Conferenceacronym’XX,June03–05,2018,Woodstock,NY
[50] MoshiWei,NimaShiriHarzevili,YuchaoHuang,JunjieWang,andSongWang. [55] LonghuiYu,WeisenJiang,HanShi,JinchengYu,ZhengyingLiu,YuZhang,

### Clear:contrastivelearningforapirecommendation.InProceedingsofthe JamesTKwok,ZhenguoLi,AdrianWeller,andWeiyangLiu.2023.Metamath:

44thInternationalConferenceonSoftwareEngineering.376–387. Bootstrapyourownmathematicalquestionsforlargelanguagemodels.arXiv
[51] KurtDWelker.2001.Thesoftwaremaintainabilityindexrevisited.CrossTalk14 preprintarXiv:2309.12284(2023).
(2001),18–21. [56] MurongYue,JieZhao,MinZhang,LiangDu,andZiyuYao.2023. Largelan-
[52] AnYang,BaosongYang,BeichenZhang,BinyuanHui,BoZheng,BowenYu, guagemodelcascadeswithmixtureofthoughtsrepresentationsforcost-efficient
ChengyuanLi,DayihengLiu,FeiHuang,HaoranWei,etal.2024. Qwen2.5 reasoning.arXivpreprintarXiv:2310.03094(2023).
technicalreport.arXivpreprintarXiv:2412.15115(2024). [57] QinkaiZheng,XiaoXia,XuZou,YuxiaoDong,ShanWang,YufeiXue,LeiShen,
[53] AnYang,BeichenZhang,BinyuanHui,BofeiGao,BowenYu,ChengpengLi, ZihanWang,AndiWang,YangLi,etal.2023.Codegeex:Apre-trainedmodelfor
DayihengLiu,JianhongTu,JingrenZhou,JunyangLin,etal.2024.Qwen2.5- codegenerationwithmultilingualbenchmarkingonhumaneval-x.InProceedings
mathtechnicalreport:Towardmathematicalexpertmodelviaself-improvement. ofthe29thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining.
arXivpreprintarXiv:2409.12122(2024). 5673–5684.
[54] AlexYoung,BeiChen,ChaoLi,ChengenHuang,GeZhang,GuanweiZhang, [58] QihaoZhu,DayaGuo,ZhihongShao,DejianYang,PeiyiWang,RunxinXu,
GuoyinWang,HengLi,JiangchengZhu,JianqunChen,etal.2024. Yi:Open YWu,YukunLi,HuazuoGao,ShirongMa,etal.2024. Deepseek-coder-v2:
foundationmodelsby01.ai.arXivpreprintarXiv:2403.04652(2024). Breakingthebarrierofclosed-sourcemodelsincodeintelligence.arXivpreprint
arXiv:2406.11931(2024).

## Tables

**Table (Page 3):**

|  3 D V V #   3 D V V #   & R G H / O D P D   %  , Q V W U X F W  & R G H / O D P D   %  , Q V W U X F W  ' H H S V H H N  & R G H U  9   / L W H  , Q V W U X F W  4 Z H Q     & R G H U     %  , Q V W U X F W  ' H H S V H H N  & R G H U  9   / L W H  , Q V W U X F W  4 Z H Q     & R G H U     %  , Q V W U X F W 0.8 0.8 0.6 0.6 0.4 0.4 0.2 0.2  & R G H V W U D O    %  < L  & R G H U     %  & K D W  & R G H V W U D O    %  < L  & R G H U     %  & K D W  6 W D U F R G H U     %  , Q V W U X F W  4 Z H Q %     & R G H U    %  , Q V W U X F W  6 W D U F R G H U     %  , Q V W U X F W  4 Z H Q     & R G H U    %  , Q V W U X F W  + P D Q ( Y D O  ' H H S V H H N  & R G H U    %  , Q V W U X F W  ' H H S V H H N  & R G H U    %  , Q V W U X F W  / H H W & R G H 6 D P S O H  & R G H & R Q W H V W B W H V W |  |
|---|---|
|  |  + P D Q ( Y D O  / H H W & R G H 6 D P S O H  & R G H & R Q W H V W B W H V W |


**Table (Page 4):**

| Pass Rate        0  7 R N H Q V       0  7 R N H Q V        0  7 R N H Q V        0  7 R N H Q V       0  7 R N H Q V        0  7 R N H Q V        0  7 R N H Q V       0  7 R N H Q V |  |
|---|---|
|  |  |
|  |  |


**Table (Page 5):**

|  | AdaptiveLLM:AFrameworkforSelectingOptimalCost-EfficientLLMforCode-GenerationBasedonCoTLength Conferenceacronym’XX,June03–05,2018,Woodstock,NY Construction of LLM Ranking Datasets Fine-tuning of CodeBERT Training of XGBOOST Classifier LeetCodeSample HumanEval CodeContests TrainingData DeepSeek-R1-Distill-Qwen-32B Embedding CoTRecord K Clustering TestData Fine-tuning CodeBERT ModelSelect Figure4:TheoverallarchitectureofAdaptiveLLM. forallcandidatemodels,themodelwiththehighestscoreisse- LLMGeneration ×8 FileExecute lectedastheoptimalsolutionmodelfortheproblem.Duetothe jointoptimizationof𝑇𝑜𝑘𝑒𝑛𝑠 𝑖and𝑃𝑟𝑖𝑐𝑒 𝑖intheformula,theselected LeetCodeSample ×2 ×2 modelcansatisfythetwoobjectivesofcodecorrectnessandcost PythonFile controlatthesametime.Theresultdatasetcoversthecomplete HumanEval problemdescription,model-generatedcode,tokenconsumption |
|---|---|
| forall LLMGeneration ×8 FileExecute lecteda jointop LeetCodeSample ×2 ×2 model PythonFile control HumanEval proble records CodeContests 𝑆𝑐𝑜𝑟𝑒 𝑖. publicr CostRecord 4.2 Inthep formbe sameti Figure5:TheprocessofLLMrankingdatasetconstruction. morere | forall LLMGeneration ×8 FileExecute lecteda jointop LeetCodeSample ×2 ×2 model PythonFile control HumanEval proble |


**Table (Page 5):**

|  |
|---|
| Fine-tuning of CodeBERT |


**Table (Page 6):**

|  | ck,NY Chengetal. Andtheinvolvementof HumanEval/0 CodeContests/28 AdaptiveLLM. Okay, I need to solve this problem where Okay, I need to solve this programming constructeddataset,we I l i h s a t v e a r t e o c c l h o e s c e k r i t f o a e n a y c h t w o o t h n e u r m b t e h r a s n i a n a p c r a o r b e l f e u m l . l y L . et's read the problem statement given threshold. The function is called torecordthereasoning has_close_elementsand takes a list of ... floats and a threshold float as inputs e6,problemsofdifferent and returns a boolean. For each test case: sinthereasoninglength. ... Read a,b,c. maybeinalowerorderof Yes, that's correct. sum_S= a + 2*b + 3*c. complexproblemjumps So the code seems correct. If sum_S%2 ==1: ple,thereasoninglength So now, let me write the code accordingly. print(1). atofLeetCode/22prob- Else: LeetCode/22 oblemisonly6832.This s_even= sum_S//2. vingcomplexproblems, O c k o a u y n , t I t h h e a v n e u m t b o e r s o o l f v i e n c t r h e i m s o v p a r b o l b e le s m u b w a h r e r r a e y s I sum_13 = a + 3*c. reasoningstepsandlogi- in a given array. Hmm, let's break it down. remainder = (sum_13) % 3. ... # Not sure anymore. rast,theanswerlengths So, code seems correct. Finally, The code is as follows, based on ofvaryingdifficulty.We certain observations. So the code seems to handle all cases counttheaverageofthe correctly. achdataset.Thedetailed So, I think this solution should be correct. tthesizeofthecontent HumanEval/0 DifficultyLabel hengeneratingthefinal Reasoning Length: 6832 xityofthequestions. AnsweringLength: 2069 LeetCode/22 Reasoning Length: 24806 Distill-Qwen-32B’sav- AnsweringLength: 2320 erlengthsondifferent CodeContests/28 asoninglengths,while Reasoning Length: 41058 K-means Clustering y. AnsweringLength: 2386 ode CodeContests Figure6:TheprocessofCoTdifficultylabeling. 6.85 40882.77 .79 3192.45 • Positivesample:RandomlyselectaproblemwithasimilarCoT 𝐶 |
|---|---|
| HumanEval LeetC |  |
| 7837.46 2460 1985.59 2676 |  |


**Table (Page 9):**

| 44 | 23 |
|---|---|
| 34 | 64 |


**Table (Page 9):**

| 99 | 77 |
|---|---|
| 11 | 73 |


**Table (Page 9):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 10):**

| 26.41% 329.02 4.61e-05 29.78% 390.71 5.47e-05 17.98% 522.68 21.95e-05 29.21% 193.47 13.93e-05 49.44% 563.68 40.58e-05 44.38% 476.48 45.27e-05 39.89% 359.61 45.31e-05 57.87% 763.57 96.21e-05 |
|---|
| 35.39% 130.42 19.56e-05 60.67% 551.62 551.62e-05 |
| 37.08% 380.30 256.83e-05 44.94%↑7.86 428.80↑48.5 28.49e-05↓228.34 43.82%↓1.12 411.84↓16.96 26.74e-05↓1.75 |
