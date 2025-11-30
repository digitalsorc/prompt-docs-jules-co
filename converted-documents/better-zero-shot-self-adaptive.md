---
title: "Better Zero Shot Self Adaptive"
original_file: "./Better_Zero_Shot_Self_Adaptive.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["shot", "page", "cot", "let", "cosp", "table", "step", "therefore", "consistency", "palm"]
summary: "<!-- Page 1 -->


### Better Zero-Shot Reasoning with Self-Adaptive Prompting

XingchenWan 1,3,RuoxiSun1,HanjunDai2,SercanÖ.Arık1,TomasPfister1
∗
1GoogleCloudAIResearch
2GoogleDeepMind
3DepartmentofEngineeringScience,UniversityofOxford
{xingchenw,ruoxis,hadai,soarik,tpfister}@google.com
Abstract thoughttobedifficultevenformassiveLLMs(Rae
etal.,2021). Thishasbeenmadepossiblebyscal-

### Modernlargelanguagemodels(LLMs)have

ingthemodelsizeandtrainingcorpus,thestrong
demonstratedimpressivecapabilit"
related_documents: []
---

# Better Zero Shot Self Adaptive

<!-- Page 1 -->


### Better Zero-Shot Reasoning with Self-Adaptive Prompting

XingchenWan 1,3,RuoxiSun1,HanjunDai2,SercanÖ.Arık1,TomasPfister1
∗
1GoogleCloudAIResearch
2GoogleDeepMind
3DepartmentofEngineeringScience,UniversityofOxford
{xingchenw,ruoxis,hadai,soarik,tpfister}@google.com
Abstract thoughttobedifficultevenformassiveLLMs(Rae
etal.,2021). Thishasbeenmadepossiblebyscal-

### Modernlargelanguagemodels(LLMs)have

ingthemodelsizeandtrainingcorpus,thestrong
demonstratedimpressivecapabilitiesatsophisfew-shotandzero-shotabilitiesofmodernLLMs,
ticated tasks, often through step-by-step reasoning similar to humans. This is made pos- and new techniques such as the chain-of-thought
sible by their strong few and zero-shot abili- (CoT)methods: Few-shotCoT (Weietal.,2022b)
ties – they can effectively learn from a hand- prependsthetestquerieswithsolvedinput-output
fulofhandcrafted,completedresponses(“in- pairsasin-contextexamplestoprompttheLLMto
contextexamples”),orarepromptedtoreason
generaterationales. Zero-shotCoT (Kojimaetal.,
spontaneouslythroughspeciallydesignedtrig-
2022),ontheotherhand,appendstriggerphrases
gers. Nonetheless,somelimitationshavebeen
aftertestqueriestoelicitreasoning. Thesemethods
observed. First, performance in the few-shot
constituteacompetitivealternativetoconventional
settingissensitivetothechoiceofexamples,
whosedesignrequiressignificanthumaneffort. fine-tuning which can be very costly for modern
Moreover,giventhediversedownstreamtasks LLMs due to their sheer size, and is not possible
of LLMs, it may be difficult or laborious to when the LLMs are available as inference-only
handcraft per-task labels. Second, while the APIs–anincreasinglypopularparadigmforservzero-shotsettingdoesnotrequirehandcrafting,
ingmodelslikeChatGPT(Schulmanetal.,2022).
its performance is limited due to the lack of
guidancetotheLLMs. Toaddresstheselim- Despite these promising advances, numerous
itations, we propose Consistency-based Self- openchallengesremain. AlthoughZero-shotCoT
adaptive Prompting (COSP), a novel prompt istask-agnostic(andthusthemostgenerallyapplidesign method for LLMs. Requiring neither
cableinanyscenario)anddoesnotrequirehuman
handcraftedresponsesnorground-truthlabels,
effortforlabeling,itoftenunderperformsitsfew-
COSP selects and builds the set of examples
shotcounterparts, withLLMs thatare notshown
fromtheLLMzero-shotoutputsviacarefully
designedcriteriathatcombineconsistency,di- with “template rationale” often producing spuriversityandrepetition. Inthezero-shotsetting ous reasoning steps. On the other hand, for FewforthreedifferentLLMs,weshowthatusing shot CoT, the performance has been shown to be
onlyLLMpredictions,COSPimprovesperfor- sensitivetothechoiceofthedemonstrations(Wei
manceupto15%comparedtozero-shotbaseetal.,2022b),andthusimprovingtheperformance
lines and matches or exceeds few-shot basemightrequiresignificanttrial-and-errorsand/orspelinesforarangeofreasoningtasks.
cificrelevantexpertise. Giventhefactthatmodern
1 Introduction LLMsareoftenusedforverydiversedownstream
tasks,selectingevenafewusefulper-taskexamples
Recentadvancesinlargelanguagemodels(LLMs)
canquicklybecomemorelaboriousasthenumber
haveledtostate-of-the-artperformanceinexisting
oftasksincrease. Thisisparticularlytrueforthe
natural language processing (NLP) tasks (Wang

### CoTtaskswherebothrationalesandanswersneed

et al., 2018, 2019; Thoppilan et al., 2022) and to
toprovidedinthedemonstrations. Insomeother
excitingemergentabilities(Weietal.,2022a). A
cases, it could be difficult or simply impossible
prominent example of the latter is the strong pereventohandcraftafewexamplesbeforehand: for
formanceontasksthatrequireanalyticalreasoning
example,theremightbetasksinvolvingtediousand
and/ormethodicalplanning,whichwerepreviously
complicated reasoning or planning and/or novel
*WorkdoneduringinternshipatGoogle. test-timetasksunseenpreviously.
3493
FindingsoftheAssociationforComputationalLinguistics:ACL2023,pages3493–3514
July9-14,2023©2023AssociationforComputationalLinguistics

<!-- Page 2 -->

Inthiswork,ourfocusistoimproveLLMrea- [Question]Henry had 11 dollars. For his birthday he got 18 more
dollars but spent 10 on a new game. How much money does he have
soninginthegeneralzero-shotsetupwithaccess now?
[Demo1]Q: John bought 21 games from a friend and bought 8 more
to input queries but not labels (i.e., transductive
at a garage sale. If 23 of the games didn't work, how many good
zero-shot(Xianetal.,2017)). Weareparticularly games did he end up with? A: Let's think step by step.He bought 21
+ 8 = 29 games in total. He has 29 -23 = 6 good games. ✅
interested in this setup due to its aforementioned
[Demo2]Q: John bought 21 games from a friend and bought 8 more
generality, but it is also a very challenging one at a garage sale. If 23 of the games didn't work, how many good
games did he end up with? A: Let's think step by step. He bought 21 +
giventhelackofexternalguidance. Toaddressthis, 8 = 29 games in total. He bought 21 + 8 = 29 games in total. He
bought 21 + 8 = 29 games in total. He has 29 -23 = 6 good games. He
insteadofrelyingonsimpletriggersorhandcrafted
has 29 -23 = 6 good games. ✅
examples, weproposepromptingtheLLMswith [Demo3] Q: Faye picked 23 and her mother picked 5 carrots from
the garden. If only 12 of the carrots were good, how many carrots
theoutputsgeneratedbytheirown. Toachievethis, were bad? A: Let's think step by step. 23 + 5 = 28 28 -12 = 1616 / 2 = 8
wefirstcollectapoolofrationalesandanswersto 8 / 2 = 4 4 / 2 = 2 2 / 2 = 1 1 / 2 = 0.❌
the test questions that are generated by the LLM Input Output
usingZero-shotCoT,andthenselectthemostsuit- Q:[Question] How much money does he have now?
A: Let’s think step by step. Henry has 11 + 18 -10 =27. ❌
ablequestionsandanswersforin-contextlearning,
[Demo1] He had 11 + 18 = 29 dollars. He spent 10
similartoFew-shotCoT.Thechoiceofwhichself- Q: [Question] dollars on a game, so he has 29 -10 =
generatedrationalestoinclude,however,ishighly A: Let’s think step by step. 19 dollars. ✅
non-trivial, asillustratedinFig. 1: notonlydoes [Demo2] He had 11 dollars. He had 11 dollars. He

### Q:[Question] had 11 dollars. He had 11 dollars….❌

thisprobleminheritallofthechallengesidentified A: Let’s think step by step.
aboveforthefew-shotscenario,italsocarriesthe [Demo3] 11 + 18 = 29 29 -10 = 1919 / 2 = 9 9 / 2 =

### Q:[Question] 4 4 / 2 = 2 2 / 2 = 1 1 / 2 = 0❌

additionaldifficultythattheself-generateddemon-
A: Let’s think step by step.
strationsthemselvesareimperfect. Retrievalmeth- [Demo3][Demo1] 11 + 18 = 29. 29 -10 = 19. ✅
odsassumingperfectlabels(Rubinetal.,2022;Liu Q:[Question]
A: Let’s think step by step.
etal.,2022)areshowntoperformworsethanrandominthissetup(Zhangetal.,2022),andprevious Figure1: Selectingin-contextdemonstrationsforreaworksbypassthisissuebyfocusingonlyonsurface soningtaskscanbeadelicateart. LLMoutputissensitivetoin-contextdemosandtheirreasoning,especially
textsimilarityanddiversityofthequestionembedwhen they are generated and imperfect. Example indings (Zhang et al., 2022), which as we show, in
puts&outputsshownfromtoptobottom(MultiArith
cases when most of the initial generated outputs
dataset&PaLM-62Bmodel):(1)zero-shotCoTwithno
arewrong,canbemisleading.
demo: correctlogicbutwronganswer;(2)correctdemo
Toaddressthesechallenges,weproposeCOSP (Demo1)andcorrectanswer;(3)correctbutrepetitive
demo(Demo2)leadstorepetitiveoutputs;(4)erroneous
(Consistency-based Self-adaptive Prompting), an
demo(Demo3)leadstoawronganswer,but(5)combinalgorithm requiring only unlabelled samples
ingDemo3andDemo1againleadstoacorrectanswer.
(which are typically cheap to obtain, for exam-
Thismotivatestheneedforacarefully-designedselecple,viacontinuous,on-the-flycollectionsofuser
tionprocedureforin-contextdemos,whichisthekey
queries) and no labelled examples for strong per- objectiveofthispaper.
formance, while also providing the capability of
furtherimprovingtheperformancewhenafewlabelledexamplesbecomeavailable. Thealgorithm metic and logical reasoning tasks over Zero-shot
consists of two stages. In the first stage, COSP CoTwithself-consistencybaselineinPaLM-62B
collects the pool of LLM responses to test ques- andGPT-3,and>3%improvementinPaLM-540B.
tions via Zero-shot CoT. We use these responses All of these are achieved with a negligible additocomputetheoutcomeentropyofeachquestion, tional computational cost. In many cases, COSP
ametricinspiredbyself-consistency(Wangetal., performs on par or better than the few-shot base-
2022a). Thismetricisthenusedtoidentifysuitable lineswithhandcraftedin-contextexamples.
question-reasoningpairsinanunsupervisedway.
2 Preliminaries

### In the second stage, we perform another pass

overalltestsamples,butwiththeselectedquestion-

### Chain-of-thought(CoT)Prompting. Few-shot

reasoningpairsasin-contextdemonstrations.

### CoT prompting (Wei et al., 2022b) prepends test

WeexperimentwithCOSPwiththreedifferent questions with a series of in-context demonstra-
LLMsonarangeoftasks. Wedemonstratea10– tionsofrelatedsolvedquestionsasprompts. Gen-
15%improvementinaverageaccuracyfor6arith- eralizingbeyondthefew-shotsetup,Kojimaetal.
3494

<!-- Page 3 -->

1 2
Inputs Stage 1 Outputs Score Generated outputs as in-context demos

## Q: 2.0 Q:

A: Let's think A: Since Therefore the
step by step. 3.0 answer is
n/a Q:
A: Since Therefore the
answer is

## Q: 3.6


### A: Let's think LLM Compute Q:

step by step. score: 3.7 A: Let's think step by step.
(Eq. 8 & 9)
3.5

## Llm


## Q: 1.9


### A: Let's think Stage 2

step by step. 2.1 Outputs

### Majority vote over outputs from

2.0 both stages for  nal prediction
Figure2: TheoverallprocedureofCOSP.InStage1(Left,§3.2),werunZero-shotCoTmultipletimesoneach
questiontogenerateapoolofdemonstrations(eachconsistingofthequestionx(i),generatedrationaler(i)
and
j
predictedansweryˆ(i)
)andassignascoretoeach. Notethatdifferentrationalesleadingtothesamefinalanswerare
j
markedthesamecolorin“Outputs“blocks(describedin§3.2). InStage2(Right,§3.3),weaugmentthecurrent
testquestionforwhichweareinterestedinfindingin-contextexamples(boxesshadedinblue)withanumberof
in-contextdemonstrations. TheseconsistoftestquestionsandselectedStage1outputswhosepredictedanswers
yˆ(i)
arethemajoritypredictionsforthatquestionthatminimizethescoredefinedinEq. (8)withtheprocedure
j
describedin§3.2. TheaugmentedtestquestionisusedtoquerytheLLMasecondtime. Finally,amajorityvote
overoutputsfrombothstagesformsthefinalprediction.
(2022)proposeZero-shotCoT andshowsthateven wherex(i) arethetestquestions,cdenotethegenby simply concatenating a trigger phrase (e.g., eralformatoftheprompttemplate(e.g. thechoice
“Let’s think step by step”) to the test question, ofin-contextdemonstrationsinFew-shotCoTor
LLMscanbepromptedtooutputintermediatesteps thetriggerphraseinZero-shotCoT)andθ denote
inabsenceofhandcraftedexamples(weshowan the weights that parameterize the LLM. The preillustrationofFew-shotandZero-shotCoTinFig. diction with the majority (or more precisely, the
5 in App. A). Our work builds upon on these plurality)voteisthenchosenasthefinalprediction:
worksandimprovesuponthem: weusethesame
m
zero-shotsetupasKojimaetal.(2022),whileenyˆ(i) = argmax I(yˆ (i) = yˆ (i) ), (2)
ablingin-contextlearningintheformatofWeietal. j k
(2022b) through an innovative use of the LLM’s yˆ j (i) X k=1
ownoutputs.
whereI( , )istheindicatorfunction. Weuseand
· ·
extend self-consistency as an integral part of our
Self-consistency. Self-consistency(Wangetal., algorithm. Instead of simply taking the majority
2022a; Li et al., 2022b), which approximates the vote,wealsouseitasakeycriterionforselecting
marginaldistributionsoftheLLMviamajorityvot- thein-contextdemonstrations,whichwediscussin
ingofmultipledecodedreasoningpaths,hasbeen detailin§3.
shown to lead to significant performance boosts
across various tasks. It is compatible with either 3 Consistency-basedSelf-adaptive
Zero- or Few-shot CoT by first introducing prob- Prompting(COSP)
abilistic decoding in the LLM decoding using a
AsdiscussedintheIntroduction,ourgoalistodenon-zero temperature, and then sampling m reavelopamethodthatimproveszero-shotreasoning
soning paths, each consisting a rationale-answer
pair(r(i),yˆ(i))fromtheLLMposterior: abilitiesofLLMsandreducestheneedforhuman
effortbyautomaticallyselectingin-contextdemonstrations from the LLM’s own generated outputs.

### Toeffectivelyachievethis,weproposeCOSP(over-

(r (i) ,yˆ (i) ) m P(r(i),yˆ(i) x(i),c,θ), (1) all procedure shown in Fig. 2 and Algorithm 1).
{ j j }j=1 ∼ |
3495

<!-- Page 4 -->

Inthissection,wepresenttheproblemsetup,fol- the absence of access to ground-truth labels, the
lowed by detailed descriptions of the two stages responsesin arepotentiallyerroneous,andcould

## P

andthekeycomponentsofthealgorithm. bemisleadingtotheLLM.
To address these problems, we propose to use
3.1 Notations&ProblemSetup
self-consistency both (1) to prune the candidate
We assume a test set with = N test exam- pool ,and(2)toselectthedemonstrationsinabples. Given an LLM D and a t | e D st | query x(i) sence P of ground-truth labels. Drawing upon the

## ∈ D

(the test label, y(i) is not available to the LLM), insightfromWangetal.(2022a)that“majoritypreweseektogenerateasetofK demonstrations , dictionsaremorelikelytobecorrect”,foreachtest

## S

whereeachdemonstrations k isaconcatenationof questionx(i) wefirstcomputetheirmajorityvote
another test question x(ik) i , the generated prediction(s) yˆ(i) from all predictions yˆ (i) m
rationale (r(ik)) and final pr ∈ ed D ic \ tion (yˆ(ik)) from with Eq. (2) and retain only the ration { al j es } t j h = a 1 t
theLLM(typicallyviaZero-shotCoT.Thedetails lead to the majority vote prediction (which are
areprovidedin§3.2): morelikelytobecorrect)andprunetherestofthe
rationale-predictionpairs(whicharemorelikelyto
bewrong)from . Followingpreviouswork(Wei
s = Concatenate(x(ik),r(ik),yˆ(ik)). (3) P
k etal.,2022b),wealsousefurtherheuristics,which
we detail in App. B, to remove obviously bad

### Theset isthenprependedasthe“context”tothe

S candidates from (e.g. responses containing no
testquestionx i ,servingasaguidetotheLLM: P
numbersforarithmetictasks,oroverlyshortand/or
x˜(i) = Concatenate(s ,...,s ,x(i)), (4) fragmentedresponses). Formally,afterpruning,for

## 1 K

testquestionx(i),theset isgivenby:
and x˜(i) is queried again (i.e., in-context learn- P
ing). Theobjectiveistobuildthesetofin-context N m¯(i)
demonstrations thatmaximizetheLLMperfor- = x(i),r (i) ,yˆ(i) , (5)

### S P j

mancewithoutaccessingtheground-truthlabels. i [ =1j [ =1(cid:16) (cid:17)
3.2 Stage1: BuildingthePoolofGenerated wherejindexesoverallm¯(i)reasoningpathsinthe
Responses&theDemonstrationSelector i-thquestionthatledtothemajorityvoteprediction
Building the Candidate Pool. We first build a yˆ(i) andarenototherwiseexcluded.
pool of responses to the test questions from The second usage of self-consistency draws

## P D

which demonstrations are selected. Each ele- upon the insight that it approximates the amount

## S

mentof isacandidatedemonstrationinthefor- ofuncertaintyofthemodelforitsprediction. Itis

## P

matdefinedinEq. (3). Toachievethis, welever- conceptuallyrelatedtopseudo-labelling(Leeetal.,
agethezero-shotcapabilitiesofLLMsbyrunning 2013;Shietal.,2018;Rizveetal.,2021)anden-
Zero-shot CoT (Kojima et al., 2022) over all test tropyminimization(GrandvaletandBengio,2004).
questionsForeachtestquestionx(i),wequerythe Intuitively,iftheLLMoutputsthesameprediction
LLMmtimeswithnon-zerotemperaturetoextract repeatedly even under different reasoning paths,
multiplereasoningpaths r (i) m andpotentially it is expected to be more confident in its predic-
{ j }j=1
differentanswers yˆ (i) m accordingtoEq. (1). tion,andweshouldassignastrongerbeliefthatthe
{ j }j=1 predictioniscorrectoratleastplausible(“consis-
SamplingmpathsperquestionyieldsmN cantentpredictionsaremorelikelytobecorrect”). To
didatesatthisstage.
capture the model uncertainty, for a question x(i)
ConsistencyforDemonstrationSelection. With withmfinalanswersfromwhichweassumethat
(i) (i)
thecandidatepoolbuilt,wenowselect fromit. therearen muniqueanswersyˆ ,...,yˆ ,we

### S ≤ 1 n

This selection process is highly non-trivial – not computethenormalizedentropyas:
only is in-context learning known to be sensitive
to the choices of the demonstrations (Wei et al., n p˜(yˆ (i) )logp˜(yˆ (i) )

### H(x(i) yˆ (i) m ) = α=1 α α ,

2022b;Liuetal.,2022),wealsohavetheadditional |{ j }j=1 logm

## P

challengesthat(1)wehavetoselectK (typically (6)
smalland 10)fromalargesetofcandidates , whereαisusedtoindexovertheuniqueanswers,
≤ P (i)
and that (2) the candidate pool is imperfect: in p˜(yˆ )istheempiricalfrequencyofuniqueanswer
α
3496

<!-- Page 5 -->


### Algorithm 1 COSP. Stage 1 (§3.2) and Stage 2

(§3.3) steps marked in orchid and peach respectively. COSP+-specific steps (refer to §3.3) are
markedindarkorange.
1: Input:Testquestions = x(i) N ,LLM,#pathsper

### D { }i=1

samplem,Poolofgeneratedresponses .

## P ←∅

2: Output:Predictions yˆ(i) N . { }i=1
3: for i [1,N] do
∈
4: QuerytheLLMwithZero-shotCoTtoobtainmrationalesandpredictions r(i),yˆ(i) m tox(i).
{ j j }i=1
5: Addcandidatedemos(Eq.(3))thatledtothemajority
votepredictionto .

## P

6: endfor
7: Build theset of demonstrations using theprocedure

## S

describedin§3.2andEq.(8)&(9).
8: fori [1,N]do
∈
9: Concatenatethe tox(i)(Eq.(4))andquerytheLLM
S againtoobtainmnewrationalesandanswers(COSP)
/anadaptivenumberofnewrationalesandanswers
proportionaltotheentropyofx(i)(COSP+).
10: Computethemajorityvoteover2manswersfromboth
stagesasthefinalansweryˆ(i).
11: endfor
(i)
yˆ inallmanswers,andtheentropyisnormalized α
by logm, the (negative) maximum entropy if all
predictionsaredifferentfromeachother,to[0,1].
As shown in Fig. 3, we indeed find that the
normalizedentropyisagoodproxyoveranumber
ofdifferenttaskswherelowentropyispositively
correlatedwithcorrectness.
1.00
0.75
0.50
0.25
0.00
GSM8K MultiArith SingleEq
yportnE
emoctuO
repetitivedemonstrationsoftenleadtoworseperformance, as exemplified in Fig. 1 (see Demo2).

### Wehypothesizethatrepetitiveresponsesactingas

demonstrationscreateastrongbutspuriouspattern
onwhichLLMsarepronetooverfit,oftenleading
tocatastrophicdeteriorationofperformance.

### Toaddressthis,wefirstfilterouttheresponses

thatinvolveself-questioningwhichweobserveoftenleadstorepetitionorpromptstheLLMtoanswerthegeneratedquestionsinsteadoftheoriginal
questions. We also introduce a quantitative measurebysplittingdemonstrationsintophrasesdelimitedbypunctuationmarks(“[.,?!]”). Assuming
that we have Q phrases*, we compute repetitivenessas:

## Q Q 2

(i)

### R (r ) = W , (7) r j Q(Q 1) ab

− (cid:16)X a=1b= X a+1 (cid:17)

## Q Q

where W
∈

### R +× is the similarity matrix over

allpairsofphraseswithW = S (ϕ(q ),ϕ(q )),
ab c a b
whereS ( , )computesthecosinesimilarityand
c
· ·
ϕ(q ) and ϕ(q ) denote the vector embedding of
a b
a-th and b-th phrases, typically obtained through
anauxiliary,smalllanguagemodel. FromEq. (7),
thematrixissummarizedbyaveragingacrossoffdiagonalelements,whichgivesanaveragesimilaritybetweentwoarbitraryphrasesintheresponse.
Wenotethatitispossibleforothertechniquesthat
penalizerepetitionatdecoding-timetobeapplied
in lieu (like hard or soft n-gram blocking (Klein
etal.,2017;Paulusetal.,2017)). Weusethepro-

### Correct

posedmethodasitalsocapturessemantic-levelrep-

### Wrong

etitions, which we find to be more common than
verbatim repetitions, especially when a non-zero
temperatureisused.
Figure3: Entropyoveroutcomesapproximatescorrectness. Distributionsofentropy(Eq. (6))vs. theground-

### OverallDesign&Building . Withmeasuresof

truthaccuracyusingZero-shotCoTofthemajorityvote S
consistency(Eq. (6))andrepetitiveness(Eq. (7))
predictionsoutof7sampledpathsonGSM8K,Multidefined,foracandidatedemonstrationp given

### ArithandSingleEqusingPaLM-62B(Chowdheryetal., ∈ P

2022). Questionsansweredcorrectlyhavesignificantly
bytheconcatenationofquestionx(i),rationaler
j
(i)
lower entropy. Further analyses are provided in App. andthe(majority)predictionyˆ(i),thescoreispro-

### C.1. posedas:

Penalizing Repetitions. Eq. (6) scores the test F
(p
|
x(i),r(i),
{
yˆ
j
(i)
}
m
j=1
) = H(x(i))+λR
r
(r
j
(i)
(
)
8
,
)
questions x(i), but for each x(i), especially for whereλisatrade-offhyperparameterthatissetto
those with a low outcome entropy, there are mul- 0.2inallexperiments. Toensurethatthedifferent
(i)
tiple reasoning paths r for the majority predic- terms of Eq. (8) are of a comparable scale, we
j
tion. Whiletheyleadtothesamefinalanswer,we
*RepetitivenessisundefinedwhenQ=1.Inthiscase,we
findthattheirsuitabilityasin-contextdemonstraassigntheminimumself-repetitionscoreoveralldemonstrationsnonethelessdiffers. Akeyobservationisthat tionswhereitisdefined.
3497

<!-- Page 6 -->

Algorithm2Building forK 2. LLM may require additional demonstrations for

## S ≥

1: Initialize

## S

withtheminimizerofEq. (8): S
←{
p∗0 = thisquestion. Tothisend,wealsoexperimentwith
argmin p (p) a variant of COSP termed COSP+ (Algorithm 1)
2: fork [2∈,PK F ]do }
∈ in§5whichfeaturesanadaptivelyallocatednum-
3: Findtheminimizerofthemodifiedobjective(Eq.(9)):
4:
p

## A

∗k
dd
=
p
a
∗k
r
t
g
o
m

## S

in
an
p
∈dPre G m
k
o
(
v
p
e
).
p∗k fromcandidatepool

## P

.
b
is
e
p
r
r
o
o
f
p
i
o
n
r
-
t
c
i
o
o
n
n
t
a
e
l
x
t
t
o
d
i
e
ts
m
z
o
e
n
r
s
o
t
-
r
s
a
h
ti
o
o
t
n
e
s
n
p
tr
e
o
r
p
q
y
u
i
e
n
st

## S

io
ta
n
g
t
e
ha
1
t
,
5: endfor
withhigher-entropyquestionsgivenmoredemonemployz-scorenormalizationcommonlyusedin strations. Itisworthnotingthatwhileitiseasyto
reinforcement learning (van Hasselt et al., 2016) select more demonstrations in COSP as we only
and NLP (Deng et al., 2022) by replacing each have to greedily optimize (8) until a higher K is
termwiththeirrespectivez-score,withthemean reached,formethodslikeFew-shotCoT,wherethe
and standard deviation computed over . To se- number of demonstrations is also the number of

## P

lect a single in-context demonstration (K = 1), “shots”, increasing it requires handcrafting more
we utilize the minimizer of the scoring function completedexamples.
p = argmin (p). Morecommonly,though,
∗ p ∈PF Extension to Few-shot. While we have built
we would like to select multiple demonstrations,

### COSPinthezero-shotsetup,itcanalsobeadapted

leadingtoacombinatorialselectionproblem. For
to the few-shot setup (which we term COSP-FS)
computationalfeasibility,weuseagreedyforward
where, for example, a small number of labelled
selection procedure (Caruana et al., 2004) as dedemonstrations are available, and we seek to
scribedinAlgorithm2. Weinitialize withp and Q

### S ∗ augmentthemwithmoredemonstrationswithout

in a greedy way and select the minimizer of the
further manual labelling. The key modifications
followingmodifiedobjectivefunction:
are: (1)insteadofqueryingLLMswithzero-shot
CoT in Stage 1 (Line 4 in Algorithm 1), we use
(p) = (p)+λR (p, ) k [2,K], (9)
k q k 1
G F S − ∀ ∈ Few-shotCoT with ;and(2)duringconstruction

## Q

of (§3.2)weinitializewith insteadofanempty
where isthepartiallybuiltdemonstrationset
k 1 S Q
S − set. WeexperimentwithCOSP-FSin§5.
withk 1elementsalreadyselected,and

## S −

RemarksontheTestSetSize. Itisworthnoting
k 1
R q (p, S k − 1 ) = max { S c (ϕ(p),ϕ(s k ′ )) }k− ′ =1 that while we have assumed the entire test set is
(cid:16) (1(cid:17)0) available to COSP and perform experiments unisatermtoencouragediversityinquestiontypes der that assumption (as we will show in §5) for
andreasoningpatternsin bypenalizingdemon- straightforwardcomparisonwiththebaselines,it

## S

strationsthataresimilartopreviousones. Wead- ispossibleforCOSPtoworkwithonlyafraction
ditionallyconstrainthat shouldnotcontainmul- of test data or in an online mode where the unla-

## S

tiple reasoning paths to the same question. The beled data are only collected continuously. One
algorithmisrepeateduntilallK demonstrationsof mayeasilyachievesobyusingtheavailabledatato
areselected. performStage1oftheCOSPprocedure. InStage2,

## S

wemayperformmajorityvotingoverbothstages
3.3 Stage2: QuerywithGeneratedIn-context
only if the test query was available at the start of

### Demonstrations


### Stage1, andmajorityvotingoverStage2onlyis

With selected, in Stage 2, we concatenate and insteadperformedotherwise.

## S

prepend the demonstrations to the test question
(Eq. (3) & (4)) and query the LLM again with 4 RelatedWorks
mmorerepetitions. Thefinalpredictionforeach

### Therehavebeenseveralrecentworksthatalsoaim

questionisthenoutputasthemajorityvoteacross
toimproveLLMreasoningusingthemodels’own
thepredictionsfrombothstages.
outputs. STaR (Zelikman et al., 2022) is one of
OutcomeEntropyasaProxytoDifficulty. We thefirstworkstobootstrapreasoningfromLLMs:
usetheentropy(Eq. (6))toselectdemonstrations startingfromasmallnumberoflabelleddata,STaR
in§3.2. However,itisalsoanaturalgaugeofdif- promptstheLLMstogeneraterationalesoverthe
ficulty of a test question to the LLM, as a higher large corpus of untrained data. However, STaR
entropy(thusahigheruncertainty)impliesthatthe requireshumanverificationonthegeneratedratio-
3498

<!-- Page 7 -->


### Model PaLM-62B PaLM-540B


### Setting 0-shot 5-shot Prev 0-shot 5-shot Prev

Method 0-shot Auto- COSP 5-shot 8-shot 0-shot Auto- COSP 5-shot 8-shot
CoT CoT (Ours) CoT CoT CoT CoT (Ours) CoT CoT
# Paths 14 14 7+7 14 14 14 7+7 14
MultiArith 67.2 9.4 85.0 81.0 - 95.2 99.0 98.8 96.0 99.3b
AddSub 69.1 73.2 78.9 72.4 - 88.9 89.1 89.9 86.6 93.7b

### SingleEq 74.4 77.8 78.7 79.8 - 88.6 85.6 90.4 89.2 -

GSM-8K 20.9 9.2 30.2 30.3 27.4a 68.5 71.4 71.9 64.3 74.4b

### CSQA 46.5 68.2 60.2 66.8 - 74.2 79.4 76.4 80.7 80.7b


### StrategyQA 57.2 59.4 64.7 67.9 - 66.0 75.7 75.2 81.4 81.6b

(Average) 55.88 49.55 66.28 66.37 - 80.25 83.37 83.77 83.03 -
aMadaanandYazdanbakhsh(2022). bWangetal.(2022a): Significantlymore(40)pathssampled.
Table 1: Accuracy on PaLM-62B (Left) and PaLM-540B (Right) (Chowdhery et al., 2022). Methods in the
0-shotcolumnsusenoground-truthlabelguidance,whereasthe5-shotresultsuse5manuallylabelledin-context
demonstrations,randomlyselectedfromtheprovidedexamplesinWeietal.(2022b). Prevcolumnsshowresults
previouslypublishedundersimilarsetupsbutoftenwithsignificantlymoresamplingpathsand/orlabelledexamples.
“#Paths”denotesthenumberofreasoningpathssampledpertestquestion. COSPusesm=7pathsperstageand
2m = 14pathsintotal. Wealsoreportbaselineresultswithoutself-consistency(whichareworse)inApp. C.2.
COSPandAuto-CoTuse5generatedin-contextexamplespertestquestion. Thetoptworesultsforeachmodelare
boldedandrankedbycolor: bestandsecond-best.
nale. Morerecently,Huangetal.(2022)relieson nocontroloverthequalityofthegeneratedratioself-consistencytoimproveLLMsbyfine-tuning nales,andisthuspronetogeneratingerroneousand
on a large number of generated questions and ra- misleading demonstrations; we empirically comtionales. However,bothworksrelyonfine-tuning pare to it in §5. Another concurrent work (Weng
ofmassivemodels,whichrequiresaccesstomodel etal.,2022)proposesself-verification,whichisa
weightsandismuchmoreexpensive. Incontrast, zero-shotreasoningverifiertorecoverconditions
our method can treat the model as a black box fromthepredictions. However,itonlyworkswhen
and only requires forward passes. Other concur- thereisauniquecorrectconditionthatresultsinthe
rentrelatedworksincludeHonovichetal.(2022) correctanswer(suchasarithmeticquestions),but
andWangetal.(2022b). However, while related isnotapplicablewhentherearemultipleplausible
methodologicallytoourmethod,thesepapersfo- conditions.
cus on fundamentally different problems of data
generationandinstructionfollowing. 5 Experiments
Forthein-contextlearningsetup(Brownetal., 5.1 ExperimentalSetup
2020; Wei et al., 2022a; Radford et al.), various
Datasets & Tasks. We consider the following
methodshavebeenproposed,typicallytoretrieve
arithmetic and logical reasoning tasks: AddSub
relevant demonstrations from a relatively large
(Hosseinietal.,2014),MultiArith(RoyandRoth,
numberoflabelledexamples(Rubinetal.,2022;
2016), GSM-8K (Cobbe et al., 2021), SingleEq
Su et al., 2022). However, Zhang et al. (2022)
(Koncel-Kedziorski et al., 2015), CSQA (Talmor
showsthatwithimperfectlabels,nearestneighboret al., 2019) and StrategyQA (Geva et al., 2021).
styleretrievalunderperformsrandomselectionand
ThelicensesofthesedatasetsarelistedinApp. B.
proposeAuto-CoT,oneofthefewexistingworks
that are fully comparable to COSP. Auto-CoT LLMs. Werunexperimentswith3LLMs: PaLM
alsousesmodels’zero-shotoutputsasin-context with 62 billion parameters (PaLM-62B) and
demonstration by selecting the responses to the 540 billion parameters (PaLM-540B) (Chowdhquestionsthatarethek-meanscentroidsintheem- ery et al., 2022) (both quantized to int8 prebedding space from an auxiliary language model cision) and GPT-3 with 175 billion parameters
(a concurrent work, Li et al. (2022a) uses a sim- (code-davinci-001) (Brown et al., 2020; Chen
ilar clustering approach). However, by selecting et al., 2021). The readers are referred to App. B
basedonquestionembeddingonly,Auto-CoThas forfurtherdetails.
3499

<!-- Page 8 -->

Model GPT-3(code-davinci-001) 5.2 Results

### Setting 0-shot 5-shot Prev

Method 0-shot Auto- COSP 5-shot 8-shot DiscussionsonMainResults. Weshowthere-
CoT CoT (Ours) CoT CoT sults on PaLM-62B, PaLM-540B and GPT-3 in
# Paths 14 14 7+7 14
Tables 1, and 2, respectively, and give some ex-

### MultiArith 50.3 78.5 80.7 60.7 82.7b

AddSub 43.5 31.9 61.5 63.3 67.8b amples of the found demonstrations in App. D.
SingleEq 48.8 58.1 64.8 65.9 - Since we find that self-consistency improves per-
GSM-8K 10.2 6.6 8.7 16.7 23.4b formance in all cases, we only report the results

### CSQA 29.2 50.9 55.4 53.0 54.9b

with self-consistency in these tables; the readers

### StrategyQA 47.8 55.8 52.8 55.4 61.7b

(Average) 38.32 46.96 53.98 52.60 - are referred to App. C.2 for results without selfbWangetal.(2022a):Significantlymore(40)pathssampled. consistency. Inallcases,COSPdeliversimprovements over Zero-shot CoT baselines with partic-
Table2: AccuracyonGPT-3(Brownetal.,2020;Chen
ularlylargegainsseenonPaLM-62BandGPT-3,
etal.,2021). RefertoTable1forfurtherexplanations.
achieving10% 15%averageimprovementover
∼
Baselines. We compare against Zero-shot CoT theZero-shotCoTwithself-consistencybaseline.
(Kojima et al., 2022) with and without self- Remarkably,eventhoughCOSPoperatesundera
consistency (Wang et al., 2022a), and Auto-CoT muchmorechallengingsetupwithoutground-truth
(Zhangetal.,2022). Auto-CoTdoesnotuseself- labels,COSPperformsonparorbetterthanFewconsistencyoriginallybutforafaircomparisonand shot CoT in almost all tasks that use labels. We
giventhatself-consistencysignificantlyimproves argue the large gains seen in the smaller models
LLMperformance,wealsoincludeanAuto-CoT that significantly reduced their performance gap
baselineaugmentedwithself-consistency(there- to the very large models (e.g. PaLM-540B), can
sultsoforiginalAuto-CoTwithoutself-consistency, beparticularlypracticallyimpactful,giventheforwhich have worse performance, are reported in mer’sstrongadvantagesincomputationalcostsand
App. C.2). Besides the zero-shot baselines, we generalaccessibility. Furthermore,wefindCOSP
alsoincludeFew-shotCoT(Weietal.,2022b)with to be robust by consistently improving over the
self-consistency as a comparison, where we use zero-shotCoTbaselineinallbutonecase,whereas
5 handcrafted demonstrations randomly chosen Auto-CoTsometimesdeterioratestheperformance.
from the provided lists of examples in Wei et al. We perform a failure analysis in App. C.5, and
(2022b) for all datasets to match the 5 generated showthatbyusingself-consistencyasaproxyof
demonstrationsinCOSPandAuto-CoT.ForCOSP, correctness,inmostcasesCOSPiscapableofidenwe sample m = 7 reasoning paths in the Stage 1 tifyingoutputswithsoundreasoningasin-context
andStage2, respectively, andforZero-shotCoT, examples even when the task is very challenging
Few-shot CoT and Auto-CoT experiments with totheLLMunderthezero-shotsetup. Incontrast,
self-consistency,equivalentlyweuse14reasoning Auto-CoT is more prone to selecting erroneous
paths for each question. In addition to the repro- examples;whileZhangetal.(2022)claimsthese
ducedbaselines,wealsoreferencepreviouslypub- errorsminimallyaffectperformance,wefindtheir
lishedbaselinesunderPrevcolumnsinTables1& effecttobeverymodelandtask-specific,holding
2thatusemorelabelledexamplesand/orsampling trueforlargermodels(e.g. PaLM-540B)andeasier
paths, both of which lead to further performance tasks. However,onmoredifficulttasksorsmaller
gainsbutatanadditionalcost. Weshowin§5.2that models,wefinderroneousdemonstrationstooften
COSPmayalsotakeadvantageofmoresampling leadtoperformancedeterioration.
pathswhenresourcesareavailable. Asmentioned
in §3.2, we use λ = 0.2 (Eq. (8)) for all experi-

### COSP+. We test COSP+ on the PaLM-62B

model(seeApp. C.3). In5outof6cases,COSP+
mentswithoutfurtherhyperparametertuning–this
leadstofurtherperformancegain. Acrossexperivalueischosentoreflectoura-prioribeliefofthe
ments,weuseafixedK whichisshowntoperform
relativeimportanceoftheobjectivefunctionterms.
welloverall,whileCOSP+ resultsshowpromisein
WhileitispossibletoachieveevenfurtherperforadaptivelysettingK;wedeferathoroughinvestimanceimprovementsbytuningthisterm,itisnot
gationtofuturework.
investigatedinthepresentworkforafaircomparisonagainstthebaselines.

### COSP-FS. We test COSP-FS in the few-shot

setting as described in §3.3. We focus on GSM-
3500

<!-- Page 9 -->

90

## S1


## S2 80


## C


## S2 70


## C+D


## Cosp 60


## S1+2,C+D


## Cosp+


## S1+2,C+D 50

0 50 100 7 14 21

### Accuracy # Paths

(a)ComponentsofCOSP.
ycaruccA
Another possible baseline is to select demonstrations randomly from the Stage 1 outputs instead
ofusinganydemonstrationselectionheuristicdescribedin§3.2;wedonotincludethisasthisisin-
COSP cludedinandoutperformedbyAutoCoTinZhang
0-shot
5-shot et al. (2022) – we outperform even AutoCoT as
shown in Tables 1 and 2. Lastly, we also analyze the effect of the number of sampling paths
(b)Effectof#paths inFig. 4b,whereitisclearthattheperformanceof
allmethodsincreaseswithnumberofpaths. This

### Figure4: AblationresultsonMultiArithdatasetusing

demonstratethatthereispotentialforfurtherperthePaLM-62BLLM.
formance gain by scaling COSP when additional
8K,themostchallengingtaskforPaLM-62Band computationalresourcesareavailable.
GPT-3wherewehypothesizethatlabelledsamples
6 Conclusion
would help more. We start with 5 labelled examplesprovidedinWeietal.(2022b)inStage1. In

### We propose COSP, a prompting algorithm to im-

Stage2,weuseCOSP-FStoselect3furtherexamprove zero-shot reasoning abilities of LLMs. It
ples. WeshowtheresultsinTable5inApp. C.4. It
achieves this by selecting in-context demonstraisworthnotingthatwhileinTable2COSPreduced
tions from its own outputs using a novel scoring
theperformancecomparedtoZero-shotCoTdue
function that incorporates consistency, diversity
to the difficulty of this task and selecting correct
and repetitiveness. Across multiple LLMs and
demonstrationsfromthezero-shotoutputs(Table7,
tasks requiring complex reassigning, we demon-
App. D),theadditionoflabelledexamplesrestored
stratelargeimprovementsoverthestateoftheart.
theeffectivenessofCOSP,primarilythroughthe

### Webelievetherearemultiplepromisingdirections

restoration of the predictive value of consistency
forfuturework: first,thepresentworkfocuseson
(Eq6)tocorrectness. WeanalyzethisinApp. C.5.
improvingzero-shotreasoning,butwearguethat
the key principle used in this paper may also be

### AblationStudies. Weperformablationstudies

extendedtomoregeneralNLPtasktypes. Second,
onCOSP,usingthePaLM-62BmodelontheMulbeyondsolvingreasoningproblemsperse,LLMs’
tiArith dataset. We first analyze the relative imreasoningcapabilitiesareincreasinglyusedinother
portanceofvariouscomponentsofCOSPanddifscenariosforplanning&interactionswithexternal
ferent terms in the scoring function Eq. (8) & 9.
environments(Yaoetal.,2023)–extendingCOSP
As shown in Fig. 4a, the results in the following
tothesesetupscouldalsobepromising. Wedefer
settingsdemonstratethatallcomponentsofCOSP
thoroughinvestigationstoafuturework.
positivelycontributetotheperformance:

## S1: Majority vote on Stage 1 outputs only. 7 Limitations


### This is essentially Zero-shot CoT over m

Onelimitationisthattheefficacyofourmethodis
paths.
shownwithmassiveLLMsinthispaper. However,

## S2,C:MajorityvoteonStage2outputsonly we note that our method is based on only model

(i.e. the m predictions from the LLM after inference with them and is already considerably
in-contextlearningwith ). Onlytheentropy cheaperthanotheradaptationmethods.

## S

term(Eq. (6))isusedasthescoringfunction. Furthermore, our method seeks to improve
LLMs: whilethetechnologyitselfisethicallyneu-

## S2,C+D:MajorityvoteonStage2outputsonly

tral,weacknowledgethattherearevarioussocial
withthefullscoringfunction(Eq. (8)&9).
and ethical risks of potential misuse, especially
given the powerful generative capabilities of the

## COSP(S1+2,C+D): Full COSP with majority

LLMsthathavebecomeincreasinglyaccessibleto
votesoverpredictionsfrombothstages.
a broader audience (Weidinger et al., 2021). We

## COSP+(S1+2,C+D):COSP+ from§3.3. Same argue that both the prospective end-users and reas(iv)butwithanadaptivenumberofdemon- searchersshouldbeawareoftheseconcernswhen

strationspersample. usingourmethodinordertomitigatetheserisks.
3501

<!-- Page 10 -->

Methodologically,wenotethatanintegralcom- AakankshaChowdhery,SharanNarang,JacobDevlin,
ponent of our algorithm is self-consistency. We Maarten Bosma, Gaurav Mishra, Adam Roberts,
Paul Barham, Hyung Won Chung, Charles Sutton,
relyontheexpectationthatitreliablypredictsac-
Sebastian Gehrmann, et al. 2022. Palm: Scaling
curacy,whichessentiallyplacesanexpectationthat
language modeling with pathways. arXiv preprint
themodeluncertaintyshouldbereasonablywell- arXiv:2204.02311.
calibrated. While we have indeed found this to
be the case for almost all considered tasks and Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,

### MarkChen,HeewooJun,LukaszKaiser,Matthias

models,additionalinvestigationsmightberequired

### Plappert, Jerry Tworek, Jacob Hilton, Reiichiro

toascertaintheirgeneralapplicability. Givenour Nakano,etal.2021. Trainingverifierstosolvemath
relianceonself-consistency, fortaskswhereself- wordproblems. arXivpreprintarXiv:2110.14168.
consistencydoesnotleadtosignificantgains,the
Mingkai Deng, Jianyu Wang, Cheng-Ping Hsieh, Yiperformanceimprovementswithourmethodmay
hanWang,HanGuo,TianminShu,MengSong,Eric
belimited. Anexampleofthiscouldbetaskswith

### Xing,andZhitingHu.2022. RLPrompt: Optimizing

verysmalllabelspaces(e.g. binaryclassification) discrete text prompts with reinforcement learning.
where“consistency”inoutcomesmaybeachieved In Proceedings of the 2022 Conference on EmpiricalMethodsinNaturalLanguageProcessing,pages
much more easily even if the model simply out-
3369–3391,AbuDhabi,UnitedArabEmirates.Asputsrandompredictions. Apotentialremedy,for
sociationforComputationalLinguistics.
whichwedeferathoroughinvestigationtofuture
work,istonotonlyconsidertheconsistencyover MorGeva,DanielKhashabi,EladSegal,TusharKhot,
outcomesbutalsoovertheintermediaterationales DanRoth,andJonathanBerant.2021. Didaristotle
usealaptop? aquestionansweringbenchmarkwith
whicharegeneratedbutnotcurrentlyusedforselfimplicit reasoning strategies. Transactions of the
consistencycomputation.
Association for Computational Linguistics, 9:346–
Second,whileCOSPimprovesperformancein 361.
anoverwhelmingmajorityofcasesandissignificantlylesssensitivetotheoriginalzero-shotmodel Yves Grandvalet and Yoshua Bengio. 2004. Semisupervised learning by entropy minimization. Adperformance compared to baseline methods like
vancesinneuralinformationprocessingsystems,17.

### AutoCoT,therestillexistexceptionalcaseswhere

it fails to improve, especially when the tasks are OrHonovich,ThomasScialom,OmerLevy,andTimo
toochallenginginzero-shotsetup–wearguethat Schick. 2022. Unnatural instructions: Tuning languagemodelswith(almost)nohumanlabor. arXiv
thisisalsoduetothegeneral,inherentlimitations
preprintarXiv:2212.09689.
of the LLMs. However, both continual improvements on the foundational models and provision

### MohammadJavadHosseini,HannanehHajishirzi,Oren

of some human guidance (e.g., using COSP-FS) Etzioni,andNateKushman.2014. Learningtosolve
shouldalleviatethisissue. arithmeticwordproblemswithverbcategorization.
InProceedingsofthe2014ConferenceonEmpirical
MethodsinNaturalLanguageProcessing(EMNLP),
pages523–533,Doha,Qatar.AssociationforCom-

### References

putationalLinguistics.

### Tom Brown, Benjamin Mann, Nick Ryder, Melanie

Subbiah,JaredDKaplan,PrafullaDhariwal,Arvind JiaxinHuang,ShixiangShaneGu,LeHou,YuexinWu,
Neelakantan,PranavShyam,GirishSastry,Amanda XuezhiWang,HongkunYu,andJiaweiHan.2022.
Askell,etal.2020. Languagemodelsarefew-shot Large language models can self-improve. arXiv
learners. Advancesinneuralinformationprocessing preprintarXiv:2210.11610.
systems,33:1877–1901.

### GuillaumeKlein,YoonKim,YuntianDeng,JeanSenel-


### RichCaruana,AlexandruNiculescu-Mizil,GeoffCrew,

lart,andAlexanderRush.2017. OpenNMT:Openand Alex Ksikes. 2004. Ensemble selection from
sourcetoolkitforneuralmachinetranslation. InProlibraries of models. In Proceedings of the twentyceedingsofACL2017,SystemDemonstrations,pages
firstinternationalconferenceonMachinelearning,
67–72,Vancouver,Canada.AssociationforCompupage18.
tationalLinguistics.

### Mark Chen, Jerry Tworek, Heewoo Jun, Qiming

Yuan,HenriquePondedeOliveiraPinto,JaredKa- TakeshiKojima,ShixiangShaneGu,MachelReid,Yuplan, HarriEdwards, YuriBurda, NicholasJoseph, takaMatsuo,andYusukeIwasawa.2022. Largelan-
Greg Brockman, et al. 2021. Evaluating large guagemodelsarezero-shotreasoners. Advancesin
language models trained on code. arXiv preprint Neural Information Processing Systems (NeurIPS)
arXiv:2107.03374. 35.
3502

<!-- Page 11 -->

Rik Koncel-Kedziorski, Hannaneh Hajishirzi, Ashish Mamshad Nayeem Rizve, Kevin Duarte, Yogesh S
Sabharwal, Oren Etzioni, and Siena Dumas Ang. Rawat, and Mubarak Shah. 2021. In defense of

## Parsing algebraic word problems into equa- pseudo-labeling: Anuncertainty-awarepseudo-label

tions. TransactionsoftheAssociationforComputa- selection framework for semi-supervised learning.
tionalLinguistics,3:585–597. arXivpreprintarXiv:2101.06329.
Dong-HyunLeeetal.2013. Pseudo-label: Thesimple Subhro Roy and Dan Roth. 2016. Solving genand efficient semi-supervised learning method for eral arithmetic word problems. arXiv preprint
deepneuralnetworks. InWorkshoponchallengesin arXiv:1608.01413.
representationlearning,ICML,volume3,page896.
Ohad Rubin, Jonathan Herzig, and Jonathan Berant.

## Learning to retrieve prompts for in-context

Junlong Li, Zhuosheng Zhang, and Hai Zhao. 2022a.
learning. InProceedingsofthe2022Conferenceof
Self-prompting large language models for opentheNorthAmericanChapteroftheAssociationfor
domainqa. arXivpreprintarXiv:2212.08635.
ComputationalLinguistics: HumanLanguageTechnologies, pages 2655–2671, Seattle, United States.
YifeiLi,ZeqiLin,ShizhuoZhang,QiangFu,BeiChen,
AssociationforComputationalLinguistics.

### Jian-GuangLou,andWeizhuChen.2022b. Onthe

advanceofmakinglanguagemodelsbetterreasoners.
JSchulman,BZoph,CKim,JHilton,JMenick,JWeng,
arXivpreprintarXiv:2206.02336.
JFCUribe,LFedus,LMetz,MPokorny,etal.2022.
Chatgpt: Optimizinglanguagemodelsfordialogue.

### JiachangLiu,DinghanShen,YizheZhang,BillDolan,

Lawrence Carin, and Weizhu Chen. 2022. What WeiweiShi,YihongGong,ChrisDing,ZhihengMaXimakes good in-context examples for GPT-3? In aoyuTao,andNanningZheng.2018. Transductive
ProceedingsofDeepLearningInsideOut(DeeLIO semi-supervised deep learning using min-max fea-
2022): The 3rd Workshop on Knowledge Extrac- tures. InProceedingsoftheEuropeanConferenceon
tionandIntegrationforDeepLearningArchitectures, ComputerVision(ECCV),pages299–315.
pages100–114,Dublin,IrelandandOnline.AssociationforComputationalLinguistics. HongjinSu,JungoKasai,ChenHenryWu,WeijiaShi,

### TianluWang,JiayiXin,RuiZhang,MariOstendorf,

Aman Madaan and Amir Yazdanbakhsh. 2022. Text LukeZettlemoyer,NoahASmith,etal.2022. Selecandpatterns: Foreffectivechainofthought,ittakes tiveannotationmakeslanguagemodelsbetterfewtwototango. arXivpreprintarXiv:2209.07686. shotlearners. arXivpreprintarXiv:2209.01975.
JianmoNi,GustavoHernandezAbrego,NoahConstant, Alon Talmor, Jonathan Herzig, Nicholas Lourie, and
JiMa,KeithHall,DanielCer,andYinfeiYang.2022. JonathanBerant.2019. CommonsenseQA:Aques-
Sentence-t5: Scalable sentence encoders from pre- tion answering challenge targeting commonsense
trained text-to-text models. In Findings of the As- knowledge. InProceedingsofthe2019Conference
sociationforComputationalLinguistics: ACL2022, oftheNorthAmericanChapteroftheAssociationfor
pages1864–1874,Dublin,Ireland.Associationfor ComputationalLinguistics: HumanLanguageTech-
ComputationalLinguistics. nologies,Volume1(LongandShortPapers),pages
4149–4158,Minneapolis,Minnesota.Associationfor
Romain Paulus, Caiming Xiong, and Richard Socher. ComputationalLinguistics.

## Adeepreinforcedmodelforabstractivesum-

RomalThoppilan,DanielDeFreitas,JamieHall,Noam
marization. arXivpreprintarXiv:1705.04304.

### Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng,

Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, et al.

### AlecRadford,JeffreyWu,RewonChild,DavidLuan,


## Lamda: Languagemodelsfordialogapplica-

DarioAmodei,IlyaSutskever,etal. Languagemodtions. arXivpreprintarXiv:2201.08239.
elsareunsupervisedmultitasklearners.

### Hado P van Hasselt, Arthur Guez, Matteo Hessel,

Jack W Rae, Sebastian Borgeaud, Trevor Cai, Katie

### VolodymyrMnih,andDavidSilver.2016. Learning

Millican, Jordan Hoffmann, Francis Song, John
valuesacrossmanyordersofmagnitude. Advances
Aslanides, Sarah Henderson, Roman Ring, Susaninneuralinformationprocessingsystems,29.
nah Young, et al. 2021. Scaling language models:
Methods,analysis&insightsfromtraininggopher. AlexWang,YadaPruksachatkun,NikitaNangia,AmanarXivpreprintarXiv:2112.11446. preetSingh,JulianMichael,FelixHill,OmerLevy,
and Samuel Bowman. 2019. Superglue: A stick-
Nils Reimers and Iryna Gurevych. 2019. Sentence- ierbenchmarkforgeneral-purposelanguageunder-
BERT:SentenceembeddingsusingSiameseBERT- standingsystems. Advancesinneuralinformation
networks. InProceedingsofthe2019Conferenceon processingsystems,32.

### EmpiricalMethodsinNaturalLanguageProcessing

andthe9thInternationalJointConferenceonNatu- Alex Wang, Amanpreet Singh, Julian Michael, Felix
ralLanguageProcessing(EMNLP-IJCNLP),pages Hill,OmerLevy,andSamuelBowman.2018. GLUE:
3982–3992,HongKong,China.AssociationforCom- Amulti-taskbenchmarkandanalysisplatformfornatputationalLinguistics. urallanguageunderstanding. InProceedingsofthe
3503

<!-- Page 12 -->

2018 EMNLP Workshop BlackboxNLP: Analyzing
and Interpreting Neural Networks for NLP, pages
353–355,Brussels,Belgium.AssociationforComputationalLinguistics.
XuezhiWang,JasonWei,DaleSchuurmans,QuocLe,

### EdChi,andDennyZhou.2022a. Self-consistency

improves chain of thought reasoning in language
models. arXivpreprintarXiv:2203.11171.
YizhongWang, YeganehKordi, SwaroopMishra, AlisaLiu,NoahASmith,DanielKhashabi,andHannanehHajishirzi.2022b. Self-instruct: Aligninglanguagemodelwithselfgeneratedinstructions. arXiv
preprintarXiv:2212.10560.
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel,
Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
MaartenBosma,DennyZhou,DonaldMetzler,etal.
2022a. Emergentabilitiesoflargelanguagemodels.
arXivpreprintarXiv:2206.07682.
JasonWei,XuezhiWang,DaleSchuurmans,Maarten
Bosma,EdChi,QuocLe,andDennyZhou.2022b.
Chainofthoughtpromptingelicitsreasoninginlarge
languagemodels. AdvancesinNeuralInformation
ProcessingSystems(NeurIPS).
LauraWeidinger,JohnMellor,MaribethRauh,Conor
Griffin, Jonathan Uesato, Po-Sen Huang, Myra

### Cheng,MiaGlaese,BorjaBalle,AtoosaKasirzadeh,

et al. 2021. Ethical and social risks of harm from
languagemodels. arXivpreprintarXiv:2112.04359.
Yixuan Weng, Minjun Zhu, Shizhu He, Kang Liu,
and Jun Zhao. 2022. Large language models are
reasoners with self-verification. arXiv preprint
arXiv:2212.09561.
YongqinXian,BerntSchiele,andZeynepAkata.2017.
Zero-shot learning-the good, the bad and the ugly.

### InProceedingsoftheIEEEconferenceoncomputer

visionandpatternrecognition,pages4582–4591.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran,KarthikNarasimhan,andYuanCao.2023.

### React: Synergizingreasoningandactinginlanguage

models. InternationalConferenceonLearningRepresentations.
Eric Zelikman, Jesse Mu, Noah D Goodman, and

### YuhuaiTonyWu.2022. Star: Self-taughtreasoner

bootstrappingreasoningwithreasoning. Advances
inneuralinformationprocessingsystems.

### Zhuosheng Zhang, Aston Zhang, Mu Li, and Alex

Smola. 2022. Automatic chain of thought prompting in large language models. arXiv preprint
arXiv:2210.03493.
3504

<!-- Page 13 -->

A IllustrationsofZero-shotandFew-shot exceptforGSM-8K,wesetamaximumdecoding
CoT step of 128 tokens. On GSM-8K, we found that
oftenlongresponsesaregeneratedandweincrease
WeshowadditionalillustrationsofCoTprompting
themaximumdecodingstepto256tokens.
techniquesdescribedin§2inFig. 5.

### Wealsodescribetheadditionalheuristicsused

toprunethepoolofcandidatesasdescribedin§3.2.

### Input:

Q: Roger has 5 balls. He Input: Fordemonstrationselection,werejectthefollow-

### Q: Olivia has $23 and

buys 2 more. How many ingquestionsorrationaleswhichareobservedto
balls does he have now? bought 5 bagels for $3
A: He sta ed with 5 and each. How much beinappropriateforourgoals:
buys 2 more. 5 + 2 = 7. The money does she have
(i) Responses that feature no numbers (impleanswer is 7. le ?
Q: Olivia has $23 and A: Let's think step by mented via regular expression matching) for
bought 5 bagels for $3 step. arithmetictasks.
each. How much money
does she have le ? (ii) Responses that involve generated questions.

### A: Whilesometimesuseful,wefindthatingeneral

Query Query self-questioningisconfusing,andoftenmislead

## Llm Llm

the LLMs to answer the generated questions
Output Output insteadoftheactualquestionsbeingasked.
She sta ed with 23. 5 bagels cost $ 15. (iii) Overly short rationales: responses containing
23 - 5 x 3 = 8. the The rest of the fewerthan5tokens.
answer is 8 money is $ 8
(iv) Overlyfragmentedresponses: afterseparating
the rationales into phrases with punctuation
Figure 5: Few-shot (left) and zero-shot (right) CoT. marks as delimiters (“[?!.,]”), we filter out
BothpromptstheLLMtooutputintermediatesteps: in the responses that feature more than 10 fragfew-shot(1-shotshowninthefigure,withoneprovided ments. This is similar to the heuristic used in
completedquestion-rationale-answerset),handcrafted Weietal.(2022b)andZhangetal.(2022)that
in-contextexamplesareprovidedandprependedtothe
removeoverlylongquestionsandresponses.
testquestions. Inthezero-shotsetting,chain-of-thought
Wealsoconductpost-processingoftheLLMoutoutputispromptedbytriggerphrases(“Let’sthinkstep
bystep.” inthefigure). puts for all methods by, for example, cutting off
outputsatstoptokenslike“\n\n\n”and“Q:”(the
latteristopreventtheLLMfromgeneratingfurther

### B AdditionalImplementationDetails

questions). Forotherpre-andpost-processingsteps
In this section, we describe the additional im- and for answer extraction procedures, we follow
plementation details for the experiments: for the
Kojimaetal.(2022)availableathttps://github.
PaLM models, we follow Wang et al. (2022a) to
com/kojima-takeshi188/zero_shot_cot.
useatemperatureof0.7duringdecodingtoextract For the datasets, GSM-8K, CSQA, Stratdifferentreasoningpathswhenself-consistencyis egyQA are licensed under the MIT license
used. On GPT-3 model, we use a temperature of (GSM-8K: https://github.com/openai/
0.4(forexperimentswithoutself-consistency,we grade-school-math/blob/master/LICENSE;
use the default greedy decoding procedure with CSQA:https://github.com/jonathanherzig/
a temperature of 0). Both COSP and Auto-CoT commonsenseqa/issues/5; StrategyQA:
involvetheuseofanauxiliarylanguagemodelto https://github.com/eladsegal/strategyqa/
extract sentence embeddings of questions and/or blob/main/LICENSE). MultiArith, Sinrationales. We use Sentence-T5-large (Ni et al., gleEq and AddSub datasets are licensed
2022)forCOSP.ItisworthnotingthatAuto-CoT under the CC:BY 4.0 license (https:
(Zhangetal.,2022)originallyusesSentenceBERT //www.cs.washington.edu/nlp/arithmetic).
(ReimersandGurevych,2019);forconsistencywe Wenotethatouruseoftheseassetsareconsistent
useSentence-T5forAuto-CoTaswell. Giventhat with their intended use (for research and devel-
Nietal.(2022)showthatSentence-T5outperforms opments), and the use of them for the purpose
SentenceBERTformostsentence-leveltasks,there of evaluating LLMs is well-documented in the
shouldonlybeapositiveimpactonthebaselineper- literature. For all datasets, we use the same data
formancesasaresultofthischange. Foralltasks split as previous works like Kojima et al. (2022).
3505

<!-- Page 14 -->


### Sincenotrainingdataisused,weonlyusethetest 1.0

split(whenthetestlabelsarepubliclyavailable)or 0.8
thevalidation/devsplit(otherwise). 0.6
0.4
C AdditionalResults&Analyses
0.2

### C.1 OutcomeEntropyvsCorrectness 0.0


### MultiArith AddSub SingleEq GSM-8K CSQA StrategyQA

Complementary to Fig. 3, in this section we provide additional experiments that demonstrate the
linkoftheoutcomeentropy(Eq. (6))andgroundtruthcorrectnessovermoretasksandmodels. We
showthefullresultsinFig. 6. Weshowthatfora
vastmajorityofcases,theoutcomeentropyiscorrelatedwithcorrectnessinastatisticallysignificant
way(inallcasesexceptforStrategyQAonGPT-3,
the p-value testing the significance of the Pointbiserial correlation (pbc) coefficient between entropyandaccuracyisbelow10 5. Thepbccoeffi- −
cientonStrategyQA/GPT-3is0.04),withcorrectly
answered questions featuring lower entropy. We
findastrongerseparationinentropydistributionin
arithmetic tasks compared to the logic reasoning
tasks(i.e.,CSQAandStrategyQA).Wearguethat
this is partly due to logic reasoning tasks consideredinthepaperbeingfeaturemuchsmallerlabel
spaces – while the answer to the arithmetic tasks
can be any real number (essentially an infinitelylargelabelspace),CSQAandStrategyQAfeature
multiplechoicequestionswith5(choicesA-E)and
2(Yes/No)classesonly,respectively. Thisisconsistentwithourdiscussionsin§7whereweargue
thattheoutcomeentropyismoreusefulforlarge
label space where it is very unlikely for random
guessingtoleadtocorrectanswers,asopposedto
classification tasks with few possible labels. As
discussedin§7,apromisingfuturedirectionisto
addressthisissueandtoimprovetheeffectiveness
ofconsistencyonthesetypesoftasks.
We further investigate the impact of the incontextdemonstrationsontheentropybyseparating and comparing between Stage 1 and Stage 2
entropy and we show the comparison in Fig. 7,
and we find that along with the improvement of
test accuracy as reported §5, the addition of the
demonstrationssignificantlyalsoreducestheoutcomeentropyacrossalltasksandmodels.

### C.2 ResultswithoutSelf-consistency

Inthissection,wereportbaselineresultsonZeroshot CoT, Few-shot CoT and Auto-CoT without
self-consistencyonPaLMmodels,whichareomittedinTable1inthemaintext. AsshowninTable
yportnE
emoctuO
Correct

### Wrong

(a)PaLM-62B
1.0
0.8
0.6
0.4
0.2
0.0
MultiArith AddSub SingleEq GSM-8K CSQA StrategyQA
yportnE
emoctuO
Correct

### Wrong

(b)PaLM-650B
1.0
0.8
0.6
0.4
0.2
0.0
MultiArith AddSub SingleEq GSM-8K CSQA StrategyQA
yportnE
emoctuO
Correct

### Wrong

(c)GPT-3
Figure6: Distributionofentropy(Eq. (6))vsgroundtruthcorrectnessusingZero-shotCoTformoretaskson
PaLMandGPT-3.
3,wefindself-consistencytoincreaseperformance
acrossallmodelsandtasksconsidered;duetothis,
wealwaysuseself-consistencyinCOSP,andonly
performexperimentswithself-consistencyinthe
GPTmodels.

### C.3 COSP+ Results


### WeperformpreliminaryexperimentsofCOSP+ on

PaLM-62Bmodel,andwereporttheresultsinTable 4. In 5 out of 6 tasks, COSP+ leads to small
improvementsbutitdeterioratestheperformance
on GSM-8K as the additional demonstrations in
thiscasecontainmoreerrorsandbecamemisleading to the LLM. We argue that the results show
promise in more adaptively selecting demonstrations, and we defer a thorough exploration in a
futurework.

### C.4 COSP-FSResults


### WecompareCOSP-FSagainstFew-shotCoTwith

self-consistency using PaLM-62B and GPT-3 on
GSM-8KinTable5.
3506

<!-- Page 15 -->


### Model PaLM-62B PaLM-540B


### Setting 0-shot 5-shot 0-shot 5-shot

Method 0-shot Auto- 5-shot 0-shot Auto- 5-shot
CoT CoT CoT CoT CoT CoT
# Paths 1 1 1 1 1 1
MultiArith 24.5 9.2 63.9 63.5 93.8 83.5

### AddSub 46.7 70.6 67.8 74.4 82.0 83.8

SingleEq 43.2 74.0 75.9 73.6 79.3 84.9

## Gsm-8K 8.6 8.7 22.7 39.8 46.6 41.8


## Csqa 41.8 63.7 57.1 66.9 64.7 80.2


### StrategyQA 57.2 55.1 56.3 53.0 67.6 76.2

(Average) 37.00 46.88 57.28 61.87 72.33 75.05
Table3: BaselineresultsonPaLM-62B(Left)andPaLM-540B(Right)(Chowdheryetal.,2022)withoutusing
self-consistency(i.e. argmaxsampling). Exceptfornotusingself-consistencyandtheuseofthezerotemperature,
allexperimentalsetupisotherwiseidenticaltothatinTable1.
1.0
0.8
0.6
0.4
0.2
0.0
MultiArith AddSub SingleEq GSM-8K CSQA StrategyQA
yportnE
emoctuO
Stage1

### Stage2

(a)PaLM-62B
1.0
0.8
0.6
0.4
0.2
0.0
MultiArith AddSub SingleEq GSM-8K CSQA StrategyQA
yportnE
emoctuO
Model PaLM-62B

### Setting 0-shot

Method COSP COSP+
(Ours) (Ours)
# Paths 7+7 7+7
MultiArith 85.0 86.2

### AddSub 78.9 79.2

SingleEq 78.7 78.9

## Gsm-8K 30.2 28.2


## Csqa 60.2 60.3


### StrategyQA 64.7 65.1

(Average) 66.28 66.32
Stage1 Table 4: Comparison between COSP and COSP+ on
Stage2 PaLM-62B.WhileCOSPuniformlyuses5in-context
demonstrationsperquestion,COSP+ usesanadaptive
(b)PaLM-540B numberofdemonstrationspersampleproportionalto
theoutcomeentropyofthetestquestioninStage1(Eq.
Figure7: Distributionofentropy(Eq. (6))inStage1 (6))andusesaminimumof5andupto8demonstrations
(i.e. firstmsamplingpathswithZero-shotCoTwith- persample. TheCOSPresultsareliftedfromTable1.
outdemonstrations)andinStage2(i.e. thesecondm
weuseself-consistencytoapproximatecorrectness,
samplingpathsafterdemonstrationsareprepended)in
PaLMmodels. thedecisionofAuto-CoTonwhichquestionand
rationale to include entirely hinges on the ques-
C.5 FailureAnalysis tionembedding,andwhentheinitialZero-shotperformanceislow,mostofthegeneratedresponses

### Inthissectionweconductanalysisincaseswhere

would be erroneous. We find that such deteriorademonstrations do not lead to performance imtionindeedhappensmorefrequentlyinthesmaller
provementorevenleadstoperformancedeterioramodelsand/ormoredifficulttaskswheretheLLMs
tion. TheonlycasewhereCOSPperformsworse
relymoreonin-contextexamplesforguidance(we
thantheZero-shotCoTisontheGSM-8Ktaskon
giveanexampleinTable6. Ontheotherhand,in
GPT-3. We show some of the identified demonlargermodelslikePaLM-540BwithstrongZerostrationsonthisparticulartask-modelcombination
shotperformanceandwhoseerrorsaremorelikely
in Table 7 in App. D, and we find that in this
due to minor flaws in reasoning (e.g. arithmetic
case,duetotheextremedifficultyofthetasktothe
mistakesinasinglestep)ratherthanmajorissues
model most of the generated demonstrations are
(e.g. repetitions,gibberishoutputs&majorsemanwrong. Ontheotherhand,competingmethodslike
ticmisunderstanding),wefindthatconsistentwith

### Auto-CoTleadtosuchperformancedeterioration

the arguments in §5.5 of Zhang et al. (2022), the
more frequently. Intuitively, unlike COSP where
3507

<!-- Page 16 -->

Model GPT-3 PaLM-62B

### Setting 5-shot

Method Manual COSP- 5-shot COSP-

### CoT FS CoT FS

# Paths 14 7+7 14 7+7

## Gsm-8K 16.7 17.7 30.3 30.8

Table5: COSP-FSresults.
resultsareindeedlesssensitivetoflaweddemonstrations.
D ExamplesofGenerated

### Demonstrations


### Weshowsomeofthegenerateddemonstrationsin

various datasets in Table 7 (GPT-3) and Table 8
(PaLM).
3508

<!-- Page 17 -->

COSP Q:Irwin’sfamilywentonacampingtripinthemountains.Onthefirstday,theyhikedfromtheircartothe
campsite.First,theyhiked0.2milefromthecartoastream,and0.4milefromthestreamtoameadow.Then
theyhiked0.1milefromthemeadowtothecampsite.HowmanymilesdidIrwin’sfamilyhikeinall?A:Let’s
thinkstepbystep.First,theyhiked0.2milesfromtheircartothestream.Then,theyhiked0.4milesfromthe
streamtothemeadow.Finally,theyhiked0.1milesfromthemeadowtothecampsite. So,thetotaldistanceis
0.2+0.4+0.1=0.7miles. Therefore,theanswer(arabicnumerals)is0.7.✓
Q: Joan purchased a basketball game for $ 5.20 , and a racing game for $ 4.23 . How much did Joan
spendonvideogames?A:Let’sthinkstepbystep.1.Joanpurchasedabasketballgamefor$5.20,andaracing
gamefor$4.23.2.$5.20+$4.23=$9.433.$9.43isthetotalamountspentonvideogames. Therefore,the
answer(arabicnumerals)is9.43.✓
Q: Jason has 7 violet balloons and 4 red balloons . He lost 3 of the violet balloons . How many violetballoonsdoesJasonhavenow?A:Let’sthinkstepbystep.7-3=44=4So,hehas4violetballoonsnow.

### Therefore,theanswer(arabicnumerals)is4.✓

Q: Joan decided to sell all of her old books . She gathered up 33 books to sell . She sold 26 books
inayardsale.HowmanybooksdoesJoannowhave?A:Let’sthinkstepbystep.1.33books-26books=7
books2. Therefore,theanswer(arabicnumerals)is7.✓
Q: Keith grew 6 turnips . Alyssa grew 9 turnips . How many turnips did they grow in all ? A: Let’s
thinkstepbystep.1.Keithgrew6turnips.2.Alyssagrew9turnips.3.Sointotal,theygrew15turnips.

### Therefore,theanswer(arabicnumerals)is15.✓

Auto- Q:Sallypicked7lemonsandMarypicked9lemonsfromthelemontree.Howmanylemonswerepickedin
CoT total?A:Let’sthinkstepbystep. Sallypicked7lemons.Marypicked9lemons.So,14lemonswerepickedin
total.Therefore,theanswer(arabicnumerals)is14.
×
Q: Sally had 27 Pokemon cards . Dan gave her 41 new Pokemon cards . Sally bought 20 Pokemon
cards. HowmanyPokemoncardsdoesSallyhavenow? A:Let’sthinkstepbystep. Sallyhad27Pokemon
cards.Dangaveher41newPokemoncards.Sallybought20Pokemoncards.HowmanyPokemoncardsdoes
Sallyhavenow? Therefore,theanswer(arabicnumerals)is27.
×
Q: Mary had 21 dimes and 38 pennies in her bank . Her dad borrowed 18 pennies from Mary . How
manypenniesdoesshehavenow?A:Let’sthinkstepbystep.Step1:21dimes+38pennies=59pennies Step
2:18pennies-18pennies=0penniesStep3:59-0=59penniesStep4:59pennies=59Step5:59pennies=
59penniesStep6:59pennies=59Step7:59=59Step8:Therefore,Maryhas59pennies. Therefore,the
answer(arabicnumerals)is59.
×
Q: There are 33 oak trees currently in the park . Park workers had to cut down 18 oak trees that were
damaged.Howmanyoaktreeswillbeintheparkwhentheworkersarefinished?A:Let’sthinkstepbystep. -
First,weknowthat18treeswerecutdown.-18treeswerecutdown,sotherewereoriginally15trees. -15-18
=-3trees,sotherewillbe3newoaktreesinthepark.-33-3=30trees,sotherewillbe30oaktreesinthepark
whentheworkersarefinished. Therefore,theanswer(arabicnumerals)is30.
×
Q: When Jake had 1 cat , he needed to serve 0.5 can of cat food each day . Now that Jake has
adoptedasecondcat,heneedstoserveatotalof0.9caneachday.Howmuchextrafoodisneededtofeedthe
secondcat?A:Let’sthinkstepbystep. -First,weneedtofindthetotalnumberofcansneededtofeedboth
cats.-Then,weneedtofindthedifferencebetweenthetotalnumberofcansandthenumberofcansneededto
feedonecat.-Finally,weneedtofindthenumberofcansneededtofeedthesecondcat.-Theansweristhe
numberofcansneededtofeedthesecondcat. Therefore,theanswer(arabicnumerals)is0.9.
×
Table6: ComparisonbetweenthedemonstrationsidentifiedbyCOSPandAuto-CoTontheAddSubtaskusing
GPT-3. Inthiscase,theCOSPdemonstrationsleadto18%improvementoverZero-shotCoTwithself-consistency
whereas AutoCoT demonstration led to performance deterioration. Reasoning steps are highlighted: correct,
questionable/incomplete/repetitive/irrelevantanderroneous,andtheground-truthcorrectnessofthedemonstrations
(unavailabletotheLLM)markedby✓or attheendoftheresponses.
×
3509

<!-- Page 18 -->


### Dataset Demonstrations

Multi Q:Debby’sclassisgoingonafieldtriptothezoo.Ifeachvancanhold4peopleandthereare2studentsand6
Arith adultsgoing,howmanyvanswilltheyneed?A:Let’sthinkstepbystep.First,we’llfigureouthowmanypeople
aregoing.2studentsand6adults.So,8people.Then,wedividethenumberofpeoplebythenumberofpeople
inavan.8peopledividedby4peoplepervan=2vans.Therefore,theanswer(arabicnumerals)is2.✓
Q: Nancy had 80 files on her computer. She deleted 31 of them and put the rest into folders with 7
filesineachone.HowmanyfoldersdidNancyendupwith?A:Let’sthinkstepbystep.Shedeleted31files,so
shehad80-31=49files.Sheput7filesineachfolder,soshehad49/7=7folders. Therefore,theanswer
(arabicnumerals)is7.✓
Q: At the arcade, Tom won 32 tickets playing ’whack a mole’ and 25 tickets playing ’skee ball’. If
hespent7ofhisticketsonahat,howmanyticketsdoesTomhaveleft?A:Let’sthinkstepbystep.Hehas32+
25=57tickets.Hespends7onahat,sohehas50left.Therefore,theanswer(arabicnumerals)is50✓
Q: The schools debate team had 5 boys and 40 girls on it. If they were split into groups of 9 how
manygroupscouldtheymake? A:Let’sthinkstepbystep. 5boysand40girls=45studentsLet’stake9
studentspergroup.Therefore,theanswer(arabicnumerals)is5.✓
SingleEq Q:Mikehas87baseballcards.Sambought13ofMike’sbaseballcards.HowmanybaseballcardsdoesMike
havenow?A:Let’sthinkstepbystep.13ofMike’sbaseballcardsarewithSam.So,87-13=74.Then,Mike
has74baseballcardsnow. Therefore,theanswer(arabicnumerals)is74.✓
Q: Sam had 98 pennies in his bank. He spent 93 of his pennies. How many pennies does he have
now?A:Let’sthinkstepbystep.1.Samhad98penniesinhisbank. 2.Hespent93pennies,sotheamountof
pennieshehasleftis5.3.So,Samhas5penniesnow.""" #Solution#Samhad98penniesinhisbank.#He
spent93pennies,sotheamountofpennieshehasleftis5.#So,Samhas5penniesnow.#2. Therefore,the
answer(arabicnumerals)is5.✓
Q: Nancy goes fishing with Joan. They catch 18 trout. If they equally split up the trout, how many
willeachoneget?A:Let’sthinkstepbystep.First,wedividethetotalnumberoftroutbythenumberofpeople.
Theansweris9.So,eachpersoncatches9trout. Therefore,theanswer(arabicnumerals)is9.✓
Q: Mrs. Hilt baked pies last weekend for a holiday dinner. She baked 16 pecan pies and 14 apples
pies.Ifshewantstoarrangeallofthepiesinrowsof5pieseach,howmanyrowswillshehave?A:Let’sthink
stepbystep. 16pecanpies+14applespies=30pies.30pies/5piesperrow=6rows.So,6rows. Therefore,
theanswer(arabicnumerals)is6.✓
GSM- Q: Two thirds of Jana’s puppies are Pomeranians. One third of the Pomeranians are girls. If there are 6
8K Pomeraniangirls,howmanypuppiesdoesJanahave?A:Let’sthinkstepbystep. First,we’lllookatthefullset
ofoptionsforJana’spuppies:Puppies:Jana’spuppesarePomeraniansandareeithergirlsorboys.Pomeranians:
Jana’spuppiesarePomeranians.Girls:Jana’spuppiesaregirls.Boys:Jana’spuppiesareboys.Let’slookatthe
informationwehave,andseewhatweknowforsure.Janahas6puppies.Jana’spuppiesareallPomeranians.
Therefore,theanswer(arabicnumerals)is6.
×
Q: If one person can paint half a house in 5 days, how many hours would it take for 5 people to paint
awholehouse?A:Let’sthinkstepbystep.1.Halfahousecanbepaintedin5daysby1person. 2.5peoplecan
painthalfahousein5days.3.5peoplecanpaintawholehousein5days.Sotheansweris5days. Therefore,
theanswer(arabicnumerals)is5.
×
Q: The local firefighters are doing a “fill the boot” fundraiser. Their goal is to raise $6300. After the
first3hours,theyhaveraised$2100.Forhowmanyhoursdotheyhavetofundraiseintotaltoreachtheirgoal,
assuminganequalamountraisedineveryhour? A:Let’sthinkstepbystep. Weknowthatthetotalamount
raisedisequaltothetotalnumberofhoursmultipliedbytheamountraisedperhour.Totalamountraised=Total
numberofhours*amountraisedperhour $6300=3*$2100$6300/$2100=3So,thetotalnumberofhours
is3. Therefore,theanswer(arabicnumerals)is3.
×
Q: A glass of milk is 8 ounces of milk. John drinks 2 glasses of milk. If milk has 3 calories per
ouncehowmanycaloriesdidheconsume?A:Let’sthinkstepbystep. Johndrank2glassesofmilk.Eachglass
had8ounces.Eachouncehad3calories.So,Johnconsumed2x8x3=48calories. Therefore,theanswer
(arabicnumerals)is48.✓
3510

<!-- Page 19 -->

CSQA Q:Whatareourbodiesdoingafterhavingfood?AnswerChoices:(A)fallingdown(B)digesting(C)gas(D)
weightgain(E)nothungryA:Let’sthinkstepbystep. Afterhavingfood,ourbodiesaredigestingit.Digestion
istheprocessbywhichfoodisbrokendownintosimplersubstances. Therefore,amongAthroughE,theanswer
isB.✓
Q: The wood was still rough to the touch, what did the woodworker have to do? Answer Choices:
(A)petrify(B)sanded(C)warp(D)composted(E)cleanA:Let’sthinkstepbystep. First,thewoodworkerhad
topetrifytheroughwood.Then,thewoodworkerhadtosandthepetrifiedwood.Finally,thewoodworkerhadto
warpthesandedwood. Therefore,amongAthroughE,theanswerisB.✓
Q: What type of store would have lots of sports equipment? Answer Choices: (A) mall (B) office
supplystore(C)school(D)sportinggoodsstore(E)sportingeventA:Let’sthinkstepbystep.I’masportsfan.I
wouldgotosportingevents,nottomalls. Therefore,amongAthroughE,theanswerisD.✓
Q: What do people aim to do at work? Answer Choices: (A) complete job (B) learn from each other
(C)killanimals(D)wearhats(E)talktoeachotherA:Let’sthinkstepbystep. Peopleaimtodotheirjobs.

### Therefore,amongAthroughE,theanswerisA.✓

Strategy Q:HastheIndianOceangarbagepatchnotcompletedtwofullrotationsofdebrissinceitsdiscovery?A:Let’s
QA thinkstepbystep. TheIndianOceangarbagepatchisapproximately10%ofthesizeoftheNorthPacific
garbagepatch.ThismeansthateveniftheIndianOceangarbagepatchhascompletedtwofullrotationsofdebris,
itwillstillonlybe1/10thofthesizeoftheNorthPacificgarbagepatch. Therefore,theanswer(YesorNo)isno.
×
Q: Was Christina Aguilera born in the forgotten borough? A: Let’s think step by step. 1. Christina 2.
Aguilera3.was4.born5.in6.the7.forgotten8. Therefore,theanswer(YesorNo)isyes.
×
Q: Karachi was a part of Alexander the Great’s success? A: Let’s think step by step. 1. Alexander
theGreathadahugearmy.2.KarachiwasapartoftheempireofAlexandertheGreat.3.Therefore,Alexander
theGreathadahugearmy.4.Therefore,KarachiwasapartofAlexandertheGreat’ssuccess.Therefore,the
answer(YesorNo)isno.✓
Q: Was Jean Valjean imprisoned due to hunger? A: Let’s think step by step. yes 1. Jean Valjean was
imprisonedforstealingbread.2.Hewasimprisonedforstealingbreadbecausehewashungry.3.Therefore,the
answer(YesorNo)isyes.Therefore,theanswer(YesorNo)isyes.✓
Table 7: Annotated examples of generated demonstrations selected by COSP on GPT-3. Similar to Table 6,
reasoning steps are highlighted: correct, questionable/incomplete/repetitive/irrelevant and erroneous, and the
ground-truth correctness of the demonstrations (unavailable to the LLM) marked by ✓ or at the end of the
×
responses.
3511

<!-- Page 20 -->


### Dataset Demonstrations

GSM- Q:Bruceworksfor5hoursonTuesday. OnWednesdayheworkstwicethetimeheworksonTuesday. On
8K Thursdayheworks2hourslessthanthetimeheworksonWednesday.HowmanyhoursdoesBruceworkinall
thesethreedays? A:Let’sthinkstepbystep. OnTuesday,Bruceworksfor5hours.OnWednesday,Bruce
worksfor2*5=10hours.OnThursday,Bruceworksfor10-2=8hours.So,inallthreedays,Bruceworks
for5+10+8=23hours. Therefore,theanswer(arabicnumerals)is23.✓
Q: Mark decides to buy packs of old magic cards and open them to sell. He buys 3 packs for $1800
each. Hegets1cardthatisworth$4000andanothercardworth$1000. Thereare30morecardsworthan
averageof$50each.Howmuchmoneyprofitdidhemake?A:Let’sthinkstepbystep. Hespent$1800*3=
$5400.Hegot$4000+$1000+$50*30=$5500.Sohemade$100profit. Therefore,theanswer(arabic
numerals)is100.✓
CSQA Q:Wherewouldsomeonepurchaseanuprightpiano?AnswerChoices:(A)musicclass(B)college(C)music
store(D)musicroom(E)musicbandA:Let’sthinkstepbystep.Youcan’tbuyapianoinamusicclass,college,
orroom.Andanuprightpianoisnotinamusicband.Thecorrectanswerisamusicstore. Therefore,amongA
throughE,theanswerisC.✓
Q: John got his tax refund back. He treated it like it was what? Answer Choices: (A) candy (B)
deathand(C)freemoney(D)discount(E)creditA:Let’sthinkstepbystep.ThefirstthingJohndidwhenhe
gothistaxrefundwastospenditonhisgirlfriend.Thesecondthinghedidwastospenditonabig-screenTV.

### ThecorrectanswerisC.Therefore,amongAthroughE,theanswerisC.✓

Q: How are the conditions for someone who is living in a homeless shelter? Answer Choices: (A)
sometimesbad(B)happy(C)respiration(D)growingolder(E)deathA:Let’sthinkstepbystep. Theansweris
choiceAbecausethepassagedescribesthathomelesspeoplehavepoorhealth. Therefore,amongAthroughE,
theanswerisA.✓
Table8: AnnotatedexamplesofgenerateddemonstrationsselectedbyCOSPonPaLM-540B.Seeexplanationsof
theannotationsinTable7
3512

<!-- Page 21 -->

ACL2023ResponsibleNLPChecklist
A Foreverysubmission:
3
(cid:3) A1. Didyoudescribethelimitationsofyourwork?
Section7isdedicatedfordiscussionsoflimitations. WealsoincludeFailureAnalysisinAppendix

## C.5.

3
(cid:3) A2. Didyoudiscussanypotentialrisksofyourwork?
WediscusspotentialethicalandsocialrisksinSection7.
3
(cid:3) A3. Dotheabstractandintroductionsummarizethepaper’smainclaims?
AbstractandIntroduction(Section1)summarisemainclaims.
(cid:3) 7 A4. HaveyouusedAIwritingassistantswhenworkingonthispaper?
Leftblank.
3
B (cid:3) Didyouuseorcreatescientificartifacts?
Section5. Usedscientificartefacts.
3
(cid:3) B1. Didyoucitethecreatorsofartifactsyouused?
Section5
3
(cid:3) B2. Didyoudiscussthelicenseortermsforuseand/ordistributionofanyartifacts?
AppendixB
3
(cid:3) B3. Didyoudiscussifyouruseofexistingartifact(s)wasconsistentwiththeirintendeduse,provided
thatitwasspecified? Fortheartifactsyoucreate,doyouspecifyintendeduseandwhetherthatis
compatiblewiththeoriginalaccessconditions(inparticular,derivativesofdataaccessedforresearch
purposesshouldnotbeusedoutsideofresearchcontexts)?

### AppendixB

(cid:3) B4. Didyoudiscussthestepstakentocheckwhetherthedatathatwascollected/usedcontainsany
informationthatnamesoruniquelyidentifiesindividualpeopleoroffensivecontent,andthesteps
takentoprotect/anonymizeit?
Notapplicable. Leftblank.
3
(cid:3) B5. Did you provide documentation of the artifacts, e.g., coverage of domains, languages, and
linguisticphenomena,demographicgroupsrepresented,etc.?
Section 5 and Appendix B. We gave high-level information about these assets: e.g. arithmetic
reasoning,logicalreasoning,etc.
3
(cid:3) B6. Didyoureportrelevantstatisticslikethenumberofexamples,detailsoftrain/test/devsplits,
etc. forthedatathatyouused/created? Evenforcommonly-usedbenchmarkdatasets,includethe
numberofexamplesintrain/validation/testsplits,astheseprovidenecessarycontextforareader
tounderstandexperimentalresults. Forexample,smalldifferencesinaccuracyonlargetestsetsmay
besignificant,whileonsmalltestsetstheymaynotbe.
AppendixB
3
C (cid:3) Didyouruncomputationalexperiments?
Section5&AppendixC.
3
(cid:3) C1. Didyoureportthenumberofparametersinthemodelsused, thetotalcomputationalbudget
(e.g.,GPUhours),andcomputinginfrastructureused?

### Section5&AppendixB

TheResponsibleNLPChecklistusedatACL2023isadoptedfromNAACL2022,withtheadditionofaquestiononAIwriting
assistance.
3513

<!-- Page 22 -->

3
(cid:3) C2. Did you discuss the experimental setup, including hyperparameter search and best-found
hyperparametervalues?
Section5&AppendixB
3
(cid:3) C3. Didyoureportdescriptivestatisticsaboutyourresults(e.g.,errorbarsaroundresults,summary
statisticsfromsetsofexperiments),andisittransparentwhetheryouarereportingthemax,mean,
etc. orjustasinglerun?
Section5&AppendixC.
3
(cid:3) C4. Ifyouusedexistingpackages(e.g.,forpreprocessing,fornormalization,orforevaluation),did
youreporttheimplementation,model,andparametersettingsused(e.g.,NLTK,Spacy,ROUGE,
etc.)?
Section5&AppendixB
7
D (cid:3) Didyouusehumanannotators(e.g.,crowdworkers)orresearchwithhumanparticipants?
Leftblank.
(cid:3) D1. Did you report the full text of instructions given to participants, including e.g., screenshots,
disclaimersofanyriskstoparticipantsorannotators,etc.?
Notapplicable. Leftblank.
(cid:3) D2. Didyoureportinformationabouthowyourecruited(e.g.,crowdsourcingplatform,students)
andpaidparticipants,anddiscussifsuchpaymentisadequategiventheparticipants’demographic
(e.g.,countryofresidence)?
Notapplicable. Leftblank.
(cid:3) D3. Did you discuss whether and how consent was obtained from people whose data you’re
using/curating? For example, if you collected data via crowdsourcing, did your instructions to
crowdworkersexplainhowthedatawouldbeused?
Notapplicable. Leftblank.
(cid:3) D4. Wasthedatacollectionprotocolapproved(ordeterminedexempt)byanethicsreviewboard?
Notapplicable. Leftblank.
(cid:3) D5. Didyoureportthebasicdemographicandgeographiccharacteristicsoftheannotatorpopulation
thatisthesourceofthedata?
Notapplicable. Leftblank.
3514

## Tables

**Table (Page 2):**

| 8 = 29 games in total. He bought 21 + 8 = 29 games in total. He |  |  |  |
|---|---|---|---|
| bought 21 + 8 = 29 games in total. He has 29 - |  |  | 23 = 6 good games. He |
| has 29 | - | 23 = 6 good games. |  |
| [Demo3] |  |  |  |


**Table (Page 2):**

| Input | Output |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Q:[Question] A: Let’s think step by step. | How much money does he have now? Henry has 11 + 18 -10 =27. ❌ |  |  |  |  |  |
|  | Henry has 11 + 1 | 8 - | 10 = |  |  |  |
| [Demo1] Q: [Question] A: Let’s think step by step. | He had 11 + 18 = 29 dollars. He spent 10 |  |  |  |  |  |
|  | dollars on a game, so he has 29 -10 = 19 dollars. ✅ |  | so he has 29 |  | - | 10 = |
|  | 19 dollars. |  |  |  |  |  |
| [Demo2] Q:[Question] A: Let’s think step by step. | He had 11 dollars. He had 11 dollars. He |  |  |  |  |  |
|  | had 11 dollars. He had 11 dollars…. |  |  |  |  |  |
| [Demo3] Q:[Question] A: Let’s think step by step. | 11 + 18 = 29 29 - | 10 = 191 |  | 9 / 2 = 9 9 / 2 = |  |  |
|  | 4 4 / 2 = 2 2 / 2 = 1 1 / 2 = |  |  |  |  |  |
| [Demo3][Demo1] Q:[Question] A: Let’s think step by step. | 11 + 18 = 29. 29 - | 10 = 19. |  |  |  |  |


**Table (Page 5):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 5):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 5):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 7):**

| PaLM-62B |  |  |  |  |
|---|---|---|---|---|
| 0-shot 0-shot Auto- COSP CoT CoT (Ours) 14 14 7+7 | 5-shot 5-shot CoT 14 | Prev 8-shot CoT | 0-shot 0-shot Auto- COSP CoT CoT (Ours) 14 14 7+7 | 5-shot 5-shot CoT 14 |
| 67.2 9.4 85.0 69.1 73.2 78.9 74.4 77.8 78.7 20.9 9.2 30.2 46.5 68.2 60.2 57.2 59.4 64.7 | 81.0 72.4 79.8 30.3 66.8 67.9 | - - - 27.4a - - | 95.2 99.0 98.8 88.9 89.1 89.9 88.6 85.6 90.4 68.5 71.4 71.9 74.2 79.4 76.4 66.0 75.7 75.2 | 96.0 86.6 89.2 64.3 80.7 81.4 |
| 55.88 49.55 66.28 | 66.37 | - | 80.25 83.37 83.77 | 83.03 |


**Table (Page 8):**

| 0-shot 0-shot Auto- COSP CoT CoT (Ours) 14 14 7+7 | 5-shot 5-shot CoT 14 |
|---|---|
| 50.3 78.5 80.7 43.5 31.9 61.5 48.8 58.1 64.8 10.2 6.6 8.7 29.2 50.9 55.4 47.8 55.8 52.8 | 60.7 63.3 65.9 16.7 53.0 55.4 |
| 38.32 46.96 53.98 | 52.60 |


**Table (Page 9):**

|  |
|---|
|  |


**Table (Page 14):**

| Correct Wrong |
|---|
| Correct Wrong |


**Table (Page 14):**

|  |
|---|
|  |


**Table (Page 14):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 14):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 14):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 14):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 14):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |


**Table (Page 14):**

| Correct Wrong |
|---|
| Correct Wrong |


**Table (Page 15):**

| PaLM-62B |  |  |
|---|---|---|
| 0-shot 0-shot Auto- CoT CoT 1 1 | 5-shot 5-shot CoT 1 | 0-shot 0-shot Auto- CoT CoT 1 1 |
| 24.5 9.2 46.7 70.6 43.2 74.0 8.6 8.7 41.8 63.7 57.2 55.1 | 63.9 67.8 75.9 22.7 57.1 56.3 | 63.5 93.8 74.4 82.0 73.6 79.3 39.8 46.6 66.9 64.7 53.0 67.6 |
| 37.00 46.88 | 57.28 | 61.87 72.33 |


**Table (Page 15):**

| Stage1 Stage2 |  |
|---|---|
|  |  |
|  |  |
| S S | tage1 tage2 |


**Table (Page 15):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 15):**

|  |  |
|---|---|
|  |  |


**Table (Page 15):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 15):**

|  |  |
|---|---|
|  |  |


**Table (Page 15):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 15):**

|  |  |
|---|---|
|  |  |


**Table (Page 15):**

|  |  |
|---|---|
|  |  |


**Table (Page 15):**

| Stage1 Stage2 |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
| S S | ta ta | ge1 ge2 |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 15):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 15):**

|  |  |
|---|---|
|  |  |
|  |  |


**Table (Page 15):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |


**Table (Page 16):**

| Manual COSP- CoT FS 14 7+7 |
|---|
| 16.7 17.7 |


**Table (Page 17):**

| cards.Dangav | eher41newPokemoncards | .Sallybought20Pokemoncards.How |
|---|---|---|
| Sallyhavenow |  |  |


**Table (Page 17):**

| 2:18pennies- | 18pennies=0penniesStep | 3:59-0=59penniesStep4:59pennies |
|---|---|---|
| 59penniesSte | p6:59pennies=59Step7 | :59=59Step8:Therefore,Maryhas5 |


**Table (Page 17):**

| First,weknow | that18treeswerecutdown. | -18treeswerecutdown,sotherewereor |
|---|---|---|
| =-3trees,soth | erewillbe3newoaktreesin | thepark.-33-3=30trees,sotherewill |
| whentheworke |  |  |


**Table (Page 17):**

|  |  | First,weneedtofindthetotalnumbero |
|---|---|---|
| cats.-Then,we | needtofindthedifference | betweenthetotalnumberofcansandthe |
| feedonecat.- | Finally,weneedtofindthe | numberofcansneededtofeedthesecon |
| numberofcans | neededtofeedthesecondc |  |


**Table (Page 18):**

| ofoptionsforJana’spuppies:Puppies:Jana’spuppesareP |
|---|
| Jana’spuppiesarePomeranians.Girls:Jana’spuppiesare |
| informationwehave,andseewhatweknowforsure.Jan |


**Table (Page 19):**

|  |  |  |  |  | After | ha | ving | food | ,ourb | odiesaredigesting |
|---|---|---|---|---|---|---|---|---|---|---|
| is | theprocessbyw | hichfoodisbrokend | owninto | simple | rsubs | tances. |  |  |  |  |


**Table (Page 19):**

| to | petrifytherough | wood.Then,thewo | odworker | hadto | sand | the | petri | fied | wood. | Finally,thewood |
|---|---|---|---|---|---|---|---|---|---|---|
| warpthesandedw |  |  |  |  |  |  |  |  |  |  |


**Table (Page 19):**

|  |  |  | garbage | patch | isap | pro | ximately |  | 10%o | fthesizeofthe |
|---|---|---|---|---|---|---|---|---|---|---|
| garbagepatch.This |  | meansthatevenift | heIndian | Ocean | garbage |  | patch | has | compl | etedtwofullrotat |
| it | willstillonlybe1 | /10thofthesizeofth | eNorthP | acific | garbagep |  | atch. |  |  |  |


**Table (Page 19):**

| the | Greathadahug | earmy.2.Karachi | wasapart | ofthe | empireo | fAlexan | der | the | Great.3.Therefo |
|---|---|---|---|---|---|---|---|---|---|
| th | eGreathadahu |  |  |  |  |  |  |  |  |


**Table (Page 19):**

| im | prisonedforstea | lingbread.2.Hewa | simpriso | nedfo | rsteal | ing | brea | dbe | causeh | ewashungry.3. |
|---|---|---|---|---|---|---|---|---|---|---|
| an | swer(YesorNo |  |  |  |  |  |  |  |  |  |


**Table (Page 20):**

|  |  |  |  |  |  |  | nTuesday,B | ruceworksfo | r5hours.O |  | nWednesday, |  | Bruce |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| worksfor2 |  | *5=10 | hour | s.On | Thursd | ay,Bruce | worksfor10 | -2=8hours. | So,in | allthr | eedays, | Bruce | works |
| for | 5+10+ | 8=23hours. |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 20):**

|  |  |  |  |  |  |  |  |  |  | yapi | anoin | amu | sic | class,c | ollege, |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| or | room.An | danuprightp | ianoi | snotin | amu | sicb | and. | Thecorre | ctanswerisa | music | store. |  |  |  |  |


**Table (Page 20):**

|  |  |  |  |  |  |  |  |  |  |  | firstthi | ngJohn |  | didwh | enhe |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| got | histaxr | efundwas | to | spend | itonhi | sgirl | friend | .Thesecond | thinghedid | wasto | spend | iton | ab | ig-scre | enTV. |
