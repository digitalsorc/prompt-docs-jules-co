---
title: "Self Agreement Improves Reasoning"
original_file: "./22_Self_Agreement_Improves_Reasoning.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["self", "reasoning", "agreement", "answer", "paths", "consistency", "shotcot", "page", "language", "few"]
summary: "Self-Agreement Improves Reasoning of Language Models
in (Almost) All Scenarios
LeiLin1∗ JiayiFu1∗ PengliLiu1 QingyangLi1 YanGong2∗ JunchenWan1
FuzhengZhang1 ZhongyuanWang1 DiZhang1 KunGai1
1KuaishouTechnology,Beijing,China
2SchoolofComputerScienceandEngineering,NortheasternUniversity,Shenyang,China
{linlei,fujiayi}@kuaishou.com,{wanjunchen,zhangfuzheng}@kuaishou.com
Abstract provides a few examples consisting of reasoning
stepstopromptLLMstogenerateintermediaterea-

### Although chain-of-thought"
related_documents: []
---

# Self Agreement Improves Reasoning

<!-- Page 1 -->


### Just Ask One More Time!

Self-Agreement Improves Reasoning of Language Models
in (Almost) All Scenarios
LeiLin1∗ JiayiFu1∗ PengliLiu1 QingyangLi1 YanGong2∗ JunchenWan1
FuzhengZhang1 ZhongyuanWang1 DiZhang1 KunGai1
1KuaishouTechnology,Beijing,China
2SchoolofComputerScienceandEngineering,NortheasternUniversity,Shenyang,China
{linlei,fujiayi}@kuaishou.com,{wanjunchen,zhangfuzheng}@kuaishou.com
Abstract provides a few examples consisting of reasoning
stepstopromptLLMstogenerateintermediaterea-

### Although chain-of-thought (CoT) prompting

soning steps towards final answers. It has been
combinedwithlanguagemodelshasachieved
demonstratedthatCoTpromptingcanelicitstrong encouraging results on complex reasoning
tasks,thenaivegreedydecodingusedinCoT reasoningcapabilitiesfromLLMs,andachievesupromptingusuallycausestherepetitivenessand periorperformanceinsolvingcomplextasks(Wei
localoptimality. Toaddressthisshortcoming, etal.,2022b). However,thenaivegreedydecoding
ensemble-optimizationtriestoobtainmultiple
strategyusedinCoTpromptingusuallycausesthe
reasoningpathstogetthefinalanswerassemrepetitivenessandlocaloptimality.
bly. However,currentensemble-optimization

### Thisworkstudiesensemble-optimization(Qiao

methodseithersimplyemployrule-basedpostprocessingsuchasself-consistency,ortrainan et al., 2022) in multi-step reasoning situations.
additionalmodelbasedonseveraltask-related Ensemble-optimizationtriestoobtainmultiplereahumanannotationstoselectthebestoneamong soning paths to get the final answer assembly.
multiple reasoning paths, yet fail to general- It avoids the repetitiveness and local optimality
izetorealisticsettingswherethetypeofinput
thatplaguegreedydecoding,whilemitigatingthe
questionsisunknownortheanswerformatof
stochasticity caused by a single sampled generareasoningpathsisunknown. Toavoidtheirlimtion(Wangetal.,2022).
itations, we propose Self-Agreement, a generalizable ensemble-optimization method ap- Current ensemble-optimization methods preplyinginalmostallscenarioswherethetype dominantly fall into two categories, i.e., verifier
of input questions and the answer format of or re-ranker based methods and post-processing
reasoning paths may be known or unknown.
based methods. Verifier or re-ranker based meth-

### Self-agreementfirstlysamplesfromlanguage

odseithertrainanadditionalverifier(Cobbeetal.,
model’s decoder to generate a diverse set of
2021;Lietal.,2023b)ortrainare-rankerbasedon
reasoningpaths,andsubsequentlypromptsthe
task-related human annotations (Thoppilan et al.,
languagemodelonemoretimetodeterminethe
optimalanswerbyselectingthemostagreedan- 2022) to select the best generation among multisweramongthesampledreasoningpaths. Self- ple generations. Post-processing based methods
agreementsimultaneouslyachievesremarkable takeamajorityvoteamongallgeneratedreasoning
performance on six public reasoning bench- paths (Wang et al., 2022; Du et al., 2023; Liang
marksandsuperiorgeneralizationcapabilities.
etal.,2023;Chenetal.,2023a)ortopK complex
reasoningpaths(Fuetal.,2022),andthenchoose
1 Introduction
theoptimalanswerthatreceivesthemostvotes.

### Althoughlargelanguagemodels(LLMs)haverev-


### While the success of ensemble-optimization

olutionizedthenaturallanguageprocessing(NLP)
work, we show that there are two major limitalandscape,theirabilitytosolvechallengingtasks
tions. Figure 1 illustrates the main limitations of
(e.g.,arithmetic,commonsenseandsymbolicreaexistingensemble-optimizationmethods. Onone
soning)isoftenseenasalimitation,whichisdifhand,althoughverifierorre-rankerbasedmethods
ficulttobeovercomesolelybyscalingupthesize
havefavorablegeneralizationabilitytosomeextent
ofLLMs(Raeetal.,2021;Srivastavaetal.,2022).
astheyimposenorestrictionsonanswerformats
Toaddressthisissue,Weietal.(2022b)haveproof reasoning paths, but they can only be applied
posed chain-of-thought (CoT) prompting, which
inscenariowherethetypeofquestionsisalready
∗EqualContribution. known,yetfailtogeneralizetoscenarioswherethe
4202
yaM
42
]LC.sc[
3v45180.1132:viXra

<!-- Page 2 -->


### Sample diverse reasoning paths

(a) Verifier or Re-ranker based methods
1 m . i F le i s rs J t, a m we e s c a ru n n c s a i l n c u a l a w t e e e h k o : w many Verifier Not A C p o p st l l i y cable
\n\n12 miles/day x 5, {...}, time =
Q: James runs 12 miles a day for 5 days a week. 60 miles / 10 miles/hour = 5 hours. Re-ranker
I h f e h ru e n r a u n w s e 1 e 0 k ? m i G le S s M an 8 K hour how many hours does Step 1: Calculate the total distance (b) Post-processing based methods
or Language James runs in a week. \n12 miles per
Q: What island country is ferret popular? model day * 5 days per week = 60 miles, Self-consistency
A (C n ) s g w r e e r a t C h b o r i i c t e a s in : ( ( A D ) ) o h w ut n c h h o ( m E e ) o (B ut ) d n o o o r r t s h C c S ar Q o A lina {...}, James runs for 6 hours a week. Agent-based medthods Not Applicable
...... First, we can calculate how many
miles James runs in a week by
multiplying the number of miles, {...},
James runs for a total of 6 hours.
Figure1: Asimpleexampletoillustratethemainlimitationsofexistingensemble-optimizationmethods. Both
verifierorre-rankerbasedmethodsandpost-processingbasedmethodscanonlysolvethequestionthatbelongstoa
knowntask,yetfailtogeneralizetosituationsoftheunknowntypeofquestions.
typeofquestionsisunknown. Besides,itiscostly commonlyassumethatboththetypeofquestions
to train such an additional model. On the other andanswerformatofreasoningpathsarealready
hand,post-processingbasedmethodscanonlybe known,whichiscontradictorytoreal-worldscenarapplied in scenario where both the type of ques- iosandhaslimitedapplicationvalues. Therefore,
tions and answer formats of reasoning paths are onenaturalquestioncanberaised: howtodesign
alreadyknown. a simple ensemble-optimization method to solve
Nevertheless,inpracticalapplications,language reasoningtasksinalmostallsituations?
modelsoftenencountersituationsofunknowntype To this end, we propose self-agreement, a new
ofquestionsordifferentanswerformats,whereit ensemble-optimization scheme that further imcannot be clearly identified which task the ques- provesreasoningperformanceoflanguagemodels
tionsbelongtoandwhatanswerformatoftherea- inalmostallpossiblescenariosbyalargemargin.
soningpathsappearstobe. Figure2showsasimple Wegetinsightsfromthemajorityvotedesignused
exampletoillustratethreemajorcasescoveringal- inWangetal.(2022),andstartfromtheintuition
mostallpossiblesituations. Briefly,wecategorize thatassessingwhetherornotapersonreallyknows
the types of questions into known and unknown, how to solve a question should depend on multii.e., whether we can identify in advance that the ple reasoning paths generated by themself, since
question belongs to a particular task, and answer a person might acquire the wrong answer due to
formats into with (w/) and without (wo/) trigger carelessnessorotherfactors.
(e.g.,Theansweris).1 So,thefirstcase(a)isthat Figure 3 illustrates the self-agreement method
both the type of question and answer format are with an example. Self-agreement comprises two
unknown, the second one (b) is that the type of phases: Firstly, we prompt the language model
question is unknown while the answer format is withfew-shotCoT (Weietal.,2022b)(w/answer
known,andthethirdone(c)isthatthetypeofques- trigger)orzero-shotCoT (Kojimaetal.,2022)(wo/
tionandanswerformatarealreadyknown. When answertrigger). Then,wesamplefromlanguage
encounteringsituationsofunknowntypeofques- model’sdecodertogenerateadiversesetofreasontionsandanswerformats(i.e., thefirstorsecond ingpaths. Wenamethisphaseaskktimes,wherek
case),itisneitherreasonabletotrainanadditional isthesizeofthediverseset;Secondly,weprompt
model given several task-related human annota- thelanguagemodelonemoretimetodeterminethe
tionsnorpossibletomanuallyidentifywhichtask optimal answer by selecting the most agreed anitrefersto,nottomentionthatthequestionencoun- sweramongthesampledreasoningpaths. Wename
teredinreal-worldscenariosisnotevenfromapre- thisphaseaskonemoretime. Suchanapproachis
defined set of tasks. Besides, the answer formats analogoustothefactthatthemostagreedanswer
ofreasoningpathsinreal-worldareever-changing. selectedfrommultiplereasoningpathsislikelyto
However,existingensemble-optimizationstudies bethecorrectanswer,sincemostreasoningpaths
generated by themself have a high probability to
1Itisnaturaltosimulateifthetypeofquestionsisknown
bywhetherornottomixdifferentreasoningtasks. Besides, arrive at the same correct answer if a person acwesimulatewhetherthereasoningpathhasatriggerviausing tuallyknowshowtosolveit. Therefore,werefer
few-shotCoTorzero-shotCoT.Weemployzero-shotCoT
toourapproachasSelf-Agreement,whichstands
without2ndanswerextractionphasetosimulatethereasoning
pathswithnotrigger. forthefact. Self-agreementissimpleyeteffective,

<!-- Page 3 -->

First, we need to find out how, {...}, (a) wo/ answer trigger
Q: James runs 12 miles a day for 5 days a week.
James runs for 6 hours a week. unknown type of question
If he runs 10 miles an hour how many hours does
he run a week? GSM8K
or Language James runs 12 miles a day for 5 days (b) w/ answer trigger
Q: What island country is ferret popular? model a week, {...}, The answer is 6 hours. unknown type of question

### Answer Choices: (A) own home (B) north carolina

(C) great britain (D) hu . t .. c .. h . (E) outdoors CSQA James runs 12 miles a day for 5 days (c) w/ answer trigger
a week, {...}, The answer is 6. known type of question: GSM8K
Figure2: (a),(b)and(c)representthreemajordifferentcasescoveringalmostallpossiblesituations. Thefirst
scenario(a)isthatboththetypeofquestionandanswerformatareunknown,andthesecondone(b)isthatthetype
ofquestionisunknownwhiletheanswerformatisknown. Thethirdone(c)isthatthetypeofquestionandanswer
formatarealreadyknown(i.e.,thetypeofquestionsbelongstoGSM8K(Cobbeetal.,2021),andtheanswerhas
thetrigger(e.g.,Theansweris)).
completely unsupervised, requires no additional and zero-shot prompting (instructions describing
humanannotationsorauxiliarymodels,andavoids thetaskastheprompt). Promptingallowsasingle
anyadditionaltrainingorfine-tuning. Tothebestof modeltocarryoutvarioustasksuniversally. Due
ourknowledge,wearethefirsttoproposethereal- toitssuperiorbenefits,therearestudies(Liuetal.,
worldscenariosinensemble-optimizationstudies, 2021;Luetal.,2021,2022)furtherinvestigatehow
anddesignasimpleensemble-optimizationmethod toimprovetheperformanceofin-contextlearning.
applyinginalmostallscenarios.2 Specifically,differentwordingororderofgivenex-
To validate the efficacy of self-agreement, we amplesmayleadtoperformancefluctuations(Zhao
conductexperimentsonsixpublicreasoningbench- etal.,2021;WebsonandPavlick,2021). Thiswork
markscoveringarithmetic,commonsenseandsym- takesanimportantstepforwardinmulti-stepreabolic reasoning. Experimental results show that soning by showing the critical role of language
self-agreementimprovesreasoningperformanceof model itself in the process of selecting the most
language models by a striking margin across all agreedanswerbasedonmultiplereasoningpaths.
tasksinallthreescenarios. Moreover,ourmethod

### ReasoningwithLanguageModelsReasoning,the

also exhibits versatility across various language
processofmakinginferencebasedonexistinginmodels and model sizes, task settings, reasoning
formationorknowledge,isthecoreofhumaninpathswithdifferentdiversity,andpromptingmethtelligenceandessentialforsolvingcomplexquesods,highlightingitsbroadapplicability.
tions(Yuetal.,2023a). Incontrasttotheexcellent
2 RelatedWork performance of LLMs in simple and single-step
tasks,languagemodels(even100Bormoreparam-
In-contextLearningLanguagemodelshaverevo- eters)aredemonstratedtostruggleatsolvingchallutionizedawiderangeofNLPtasks,wherescal- lenging tasks required multi-step reasoning (Rae
ing up the model size is one of the key ingredi- et al., 2021; Srivastava et al., 2022). To address
ents(Vaswanietal.,2017;KentonandToutanova, this issue, Nye et al. (2021) have proposed to de-
2019; Raffel et al., 2020; Brown et al., 2020; composemulti-stepreasoningproblemsintointer-
Rae et al., 2021; Chowdhery et al., 2022; Thop- mediatestepsbeforeobtainingfinalanswers. Furpilanetal.,2022). ThesuccessofLLMsisoften thermore,Weietal.(2022b)haveproposedchainattributed to emergent abilities when the model of-thoughtprompting,whichelicitsthisreasoning
reachesasufficientscale(Weietal.,2022a). That processfromlanguagemodels. Sincethen,designis, the model can follow the format of given ingpromptsmanually(Weietal.,2022b;Fuetal.,
prompts (typically a few task-specific examples) 2022;Diaoetal.,2023)orautomatically(Kojima
thussolvingthecorrespondingtasks(alsoreferred etal.,2022;Zhangetal.,2022;Shumetal.,2023),
asin-contextlearning). Themethodofcondition- example selection in CoT prompting (Fu et al.,
ingLLMsiscalled“prompting”(Liuetal.,2023), 2022;Zhangetal.,2022;Shumetal.,2023;Diao
whichcanbecategorizedintotwomaindirections: etal.,2023),anddataaugmentation(Fuetal.,2023;
few-shotprompting(afewexamplesastheprompt) Yueetal.,2023;Yuetal.,2023b)havebecomea
hot topic in NLP. Our work sits in the context of
2Aftercompletionofthiswork,wefindthatChenetal.
zero-shotCoTandfew-shotCoT,andproposesa
(2023b)sharealmostthesameideawithus,whichisarchived
afterourwork.WeprovidediscussionwithitinAppendixC. new ensemble-optimization method that substan-

<!-- Page 4 -->

(1) Ask k Times (2) Ask One More Time

### Sample diverse reasoning paths

Q: James runs 12 miles a day for 5 days a week. 1 m \ 6 . n 0 i F l \ e m i n s r 1 i s l 2 J e t , a s m m w / il e e e 1 s s c 0 / a r m d u n n a i c l s y e a s i x l n c / u 5 h a l , o a w u { t . r e e .. e } = h , k o t 5 : w i m h m o e u a = r n s y . W c d 1. o e U h r t n r a e d e i n l e s e m p r d o s a t n s k a t d i n e n in d p g g s a t : s h m o e l a u Q j t o i u o r e n it s s y t , i { v o . o n .. t : } , e { . f . o . o } n l ; l o m w u l t t h ip e l s e e
I h Q A f e n : s h r W w u e n e h r r a a u t C n w s h is e o 1 l e a i 0 c k n e ? m d s i : c G l e o ( S A s u M n ) a t n o 8 r w K y h n o o i s r u h r f o e m h r o e r w e ( B t m ) p a n o n o p y r u h t la h o r u c ? r a s r o d l o in e a s La m n o g d ua e g l e S J d {. a . a t . y } e m , p * e J s 1 a 5 : m r C d u e a a n s l y s c s r u i u n l p a n e a t s r e w f w t o e h e r e e e k 6 k . t h \ o = n o t 6 1 u a 2 0 l r s d m m i a s i i l t l w e e a s s e n , e c p k e e . r 2 3 4 # . . . # E C S o x e # u t le n r c a t t c t t t h h t e e h V e F o i f t n i e n a s l a : l A { a n .. n . s . } s w ; . w . e e . r r . : . f {. o .. r }. each solution: {...}; La m n o g d ua e g l e T Ja h m e e m s a r j u o n ri s t y f o v r o t 6 e h d o a u n r s s w a e w r e is e : k.
(C) great britain (D) hu.t..c..h. (E) outdoors CSQA
First, we can calculate how many

## Q

So
u
l
e
u
s
t
t
io
io
n
n
1
:
:

## J

1
a
.
m
Fi
e
r
s
s t
r
,
u
w
ns
e
1
c
2
a n
m
c
il
a
e
l
s
c u
a
l a
d
t
a
e
y
h
,
o
{.
w
..}
,
?
{...}.
miles James runs in a week by Solution 2: Step 1: Calculate the total, {...}.
multiplying the number of miles, {...}, Solution 3: First, we can calculate how many, {...}.

### James runs for a total of 6 hours. ###

Figure3: Theself-agreementmethodcontainstwostages: (1)askktimes: samplefromthelanguagemodelitselfk
timestogeneratekdiversereasoningpathsusingfew-shotCoT(Weietal.,2022b)orzero-shotCoT(Kojimaetal.,
2022);and(2)askonemoretime: selectthemostagreedanswerbasedonkreasoningpathsbylanguagemodel
itself. Yellowdenotesthecarefullydesignedpromptproposedinthiswork(seeTable11intheAppendix),andred
denotesthemostagreedanswergeneratedbythelanguagemodelitself.
tiallyoutperformstheoriginalzero-shotCoTand can we allow the language model itself to select
few-shotCoT,respectively. the best generation among multiple generations,
Ensemble-OptimizationinReasoningwithLan- since it has favorable generalization ability, i.e.,
guageModelsEnsemble-optimizationtriestoob- no restrictions on the types of questions and antain multiple reasoning paths to get the final an- swer formats of reasoning paths, and avoids any
swerassembly(Qiaoetal.,2022). Weviewmost additionaltraining,auxiliarymodelsorfine-tuning.
ensemble-optimizationworkasdifferentimplemen- Beforehand,weneedtofigureoutwhatlanguage
tations of the majority voted idea.3 For example, modelsaregoodatfor?
self-consistency(Wangetal.,2022)takesthema-

### Previousworkhasdemonstratedthatlanguage

jority vote over sampled reasoning paths, while
modelsaregoodanswerextractorsgivenspecific
multi-agents(debate)(Duetal.,2023)obtainsthe
prompts (Kojima et al., 2022; Zhou et al., 2022;
majority voted answer over multiple agents’ out-

### Yangetal.,2023a),andalsosuitableforcomparing

puts. It is clear that the essence of them is based
theconsistencyoffinalanswersextractedfrommulon the majority voted design, and our work is in
tiplereasoningpathsgivenspecificprompts(Yang
lineswithit,butweexplorehowtoallowlanguage
et al., 2023b,c), as the extracted final answers in
modelitselftoachievetheoverallprocedure. So,
reasoningtaskstendtobeshortandsemantically
themaindifferencebetweenthemliesintwomastraightforwardsentencesorphrases. Forinstance,
jorstepsconsistingoftheprocessofthemajority
asshowninFigure3,forlanguagemodels,James
vote, i.e., answer extraction and answer comparrunsfor6hoursaweekandJamesrunsforatotal
ison. To be specific, self-consistency and multiof6hoursextractedfromsolution2,3respectively
agents (debate) are rule-based and not generalizrepresentthesamefinalanswer. Suchbehaviors
ablemethodtoextractandcompareanswers. Howareoftenattributedtoemergentabilities(Weietal.,
ever, self-agreement is an entirely generalizable
2022a). Thatis,themodelcanunderstandandfolmethod,whetherextractinganswersorcomparing
lowtheformatofgivenpromptsthussolvingthe
answers.
correspondingtasks.
3 Methodology Motivatedbytheabovefindingsandthemajority
votedesignusedinWangetal.(2022),wepropose

### Existing ensemble-optimization studies (Wang

the following self-agreement method that allows
et al., 2022; Fu et al., 2022) commonly assume
language model itself to extract final answers of
thatboththetypeofquestionsfedtothemodeland
multiple reasoning paths, count the votes of difanswerformatofreasoningpathsoutputtedbythe
ferentanswers,andthenselectthemajorityvoted
modelarealreadyknown,andconductevaluations
answer. Specifically, firstly, we prompt the lanonthequestionsfromthesamedataset. However,
guagemodelwithfew-shotCoT (Weietal.,2022b)
a more realistic setting is that the type of input
(w/answertrigger)orzero-shotCoT (Kojimaetal.,
questions or answer format of reasoning paths is
2022)(wo/answertrigger). Then,wesamplefrom
unknown and they come in an arbitrary manner.
languagemodel’sdecodertogenerateadiverseset

### Toaddresssuchscenarios,onenaturalideaisthat

of reasoning paths. We refer to this stage as ask
3Detailsrefertocorrespondingpapers. k times, where k is is the size of the diverse set.

<!-- Page 5 -->

Model Arithmetic Commonsense Symbolic

### Avg


### GSM8K MultiArith SVAMP CSQA ARC-c Letter

Boththetypeofquestionsandtheanswerformatareunknown(thefirstscenario)

### Zero-ShotCoT 48.5 93.0 73.5 71.0 81.5 81.0 74.8


### GPT-3.5-turbo Self-Consistency N/A N/A N/A N/A N/A N/A N/A

Self-Agreement 58.5(+10.0) 93.4(+0.4) 79.6(+6.1) 77.8(+6.8) 87.7(+6.2) 83.8(+2.8) 80.1(+5.3)

### Zero-ShotCoT 26.0 77.5 50.5 57.5 66.5 31.0 51.5

Llama-2-13B-Chat Self-Consistency N/A N/A N/A N/A N/A N/A N/A
Self-Agreement 31.7(+5.7) 77.8(+0.3) 56.3(+5.8) 65.0(+7.5) 68.5(+2.0) 44.5(+13.5) 57.3(+5.8)
Thetypeofquestionsisunknownandtheanswerformatisknown(thesecondscenario)
Mixed-Few-ShotCoT 69.0 97.5 76.5 71.0 86.0 83.0 80.5
Self-Consistency 68.0 98.1 76.6 71.2 83.1 79.1 79.3

### GPT-3.5-turbo


### Multi-Agents(Debate) 80.2 96.0 76.2 69.0 78.4 61.3 76.9

Self-Agreement 81.3(+12.3) 99.1(+2.6) 83.7(+7.2) 75.4(+4.4) 87.8(+1.8) 88.9(+6.9) 86.0(+5.5)
Mixed-Few-ShotCoT 31.5 84.0 61.0 66.5 68.0 19.0 55.0
Self-Consistency 32.8 83.9 56.7 68.0 68.1 16.0 54.5

### Llama-2-13B-Chat


### Multi-Agents(Debate) 44.0 79.0 54.0 52.0 56.5 27.0 52.1

Self-Agreement 41.5(+10.0) 94.7(+10.7) 66.8(+5.8) 70.2(+3.7) 70.6(+2.6) 23.1(+4.1) 61.2(+6.2)
Table1: Self-agreement,whenappliedonGPT-3.5-turboandLlama-2-13B-Chat. Ourperformancegain(+blue)is
computedoverthemixed-few-shotCoTorzero-shotCoT(Kojimaetal.,2022),whichisourprimarybaseline. Our
methodsubstantiallyincreasestheperformanceovermixed-few-shotCoTandzero-shotCoT.Thebestperformance
acrosseachmodelforeachtaskisshowninbold.
Self-agreementiscompatiblewithreasoningpaths 3.2 AskOneMoreTime
tothequestionswithdifferentdiversity.4 Secondly,

### After sampling multiple reasoning paths z from

we prompt the language model one more time to i
themodel’sdecoder,self-agreementfirstextracts
determinetheoptimalanswerbyselectingthemost
the final answers a of each reasoning path, and
agreedansweramongthesampledreasoningpaths. i
thenselectsthemost“agreed”answeramongthe
We refer to this stage as ask one more time. Figfinalanswersetbytakingamajorityvoteovera .
ure3showstheoverallprocedureofourapproach. i

### Theoverallprocesscanbeachievedbyprompting

language model itself one more time. The care-
3.1 AskkTimes fully designed prompt is given in Table 11 in the
Appendixrespectively. Specifically,wefirstmod-

### Wesimulatewhetherthetypeofquestionsisknown

ifytheinputquestionxanditsmultiplereasoning
or not by whether or not we mix tasks,5 and
pathsz intoaprompts. Promptedtextsisthenfed
i
whether the answer format of reasoning paths is
intolanguagemodelsandgeneratesubsequentsenknownornotbyutilizingfew-shotCoT(Weietal.,
tencev. Wecanuseanydecodingstrategy,butwe
2022b)orzero-shotCoT(Kojimaetal.,2022). In
usegreedydecodinginthisstageforthesimplicity.
thisstage,wefirstmodifytheinputquestionxinto
apromptx′. Thepromptx′ wouldbe“Q:[X].A:
4 Experiments
”withafewhand-craftedexamplesor“Q:[X].A:
Let’s think step by step.” if we employ few-shot
We carry out a series of experiments to confirm

### CoTorzero-shotCoT,where[X]isaninputslot

theefficacyofourmethodonthreescenarios. Our
forx. Thesamepromptedtextx′ isthenfedinto
findingsindicatethatacrossawiderangeoftasks,
languagemodelsandgeneratemultiplesentences
scenarios, models, and prompting methods, selfz via sampling strategies, where i = 1,...,m
i
agreement generally enhances the reasoning perindexesthemcandidateoutputs.
formance of language models. We introduce experimentalsetupin§4.1,mainresultsin§4.2,and
4Forexample,intemperaturesamplingstrategies(Ficler analysisin§4.3. SeeAppendixAandBformore
and Goldberg, 2017), higher values like 0.8 will make the
experimentaldetailsandadditionalexperiments.
outputmorerandom,whilelowervalueslike0.2willmakeit
morefocusedanddeterministic.
5Nearingcompletionofthiswork,wefindthatZouetal.
4.1 ExperimentalSetup
(2023)haveappliedCoTpromptingtomixed-taskscenarios
tosimulatethereal-worldapplications,whichsharethesame

### Tasks and Datasets We evaluate self-agreement

ideawithuswhileweproposeitinensemble-optimization
studies. onsixpublicreasoningbenchmarksforafaircom-

<!-- Page 6 -->


### Model Arithmetic Commonsense Symbolic


### GSM8K MultiArith SVAMP CSQA ARC-c Letter

Boththetypeofquestionsandtheanswerformatareknown(thethirdscenario)
PreviousfinetuningSOTA 55.0a 60.5b 57.4c 91.2d 75.0e N/A
Few-ShotCoT 17.1 51.8 38.9 57.9 55.1 8.2

### LaMDA†

Self-Consistency 27.7 75.7 53.3 63.1 59.8 8.2
Few-ShotCoT 56.5 94.7 79.0 79.0 85.2 65.8

### PaLM†

Self-Consistency 74.4 99.3 86.6 80.7 88.7 70.8
Few-ShotCoT 58.8 - - - - -

### Minerva†


### Self-Consistency 78.5 - - - - -


### Few-ShotCoT 70.0 98.2 82.0 74.5 85.4 80.6

Self-Consistency 80.3 99.2 85.9 79.0 87.0 81.9

### GPT-3.5-turbo


## Usc 76.8 98.2 83.5 48.9 73.9 79.4

Self-Agreement 82.4(+12.4) 99.0(+0.8) 86.0(+4.0) 79.4(+4.9) 86.8(+1.4) 81.0(+0.4)
Table2: Self-agreement,whenappliedonGPT-3.5-turbo. †modelsarenotpubliclyaccessible,andthenumbers
areobtainedfromtheirpapers. Ourperformancegain(+blue)iscomputedoverfew-shotCoT(Weietal.,2022b),
whichisourprimarybaseline. OurmethodssubstantiallyincreasetheperformanceoverWeietal.(2022b),withan
average+4.0gainonGPT-3.5-turbo. ThepreviousfinetuingSOTAbaselinesareobtainedfrom: a: GPT-3175B
finetunedplusanadditional175Bverifier(Cobbeetal.,2021),b: RelevanceandLCAoperationclassifier(Royand
Roth,2015),c:(Pietal.,2022),d: DeBERTaV3-large+KEAR(Xuetal.,2021),e: UnifiedQA-FT(Khashabietal.,
2020). Thebestperformanceforeachtaskisshowninbold.
parisonwithexistingmethods.6 Thesebenchmarks vron et al., 2023) with 13-billion parameters, opcan be divided into three categories of reasoning timizedfordialogueusecasesviaalignmenttechtasks: (i) Arithmetic Reasoning For these tasks, niques. Llama-2-ChatmodelsarecompletelyopenweuseGSM8K(Cobbeetal.,2021),SVAMP(Pa- sourced8 andhavesimilarperformancecompared
tel et al., 2021), and MultiArith (Roy and Roth, with GPT-3 (Brown et al., 2020). For the third
2016);(ii)CommonsenseReasoningWeevaluate scenario,weconsiderthefollowinglanguagemodtwocommonsensereasoningtasks: CommonseQA els: (i)LaMDA-137B(Thoppilanetal.,2022)with
(CSQA)(Talmoretal.,2018)andtheAI2Reason- 137-billion parameters, pre-trained on a mixture
ingChallenge(ARC)(Clarketal.,2018). TheARC of web documents, dialog data and Wikipedia;
datasetisdividedintotwosets: achallengeset(de- (ii) PaLM-540B (Chowdhery et al., 2022) with
notedasARC-c),andaneasyset(denotedasARC- 540-billionparameters,pre-trainedonahighquale). We evaluate the effectiveness of our method ity corpus of 780 billion tokens; (iii) MinervaonARC-c;(iii)SymbolicReasoningWechoose 540B (Lewkowycz et al., 2022) with 540-billion
last letter concatenation (e.g., the input is “Elon parameters,pretrainedongeneralnaturallanguage
Musk” and the output should be “nk”) from Wei dataandfurthertrainedontechnicalcontent;(iv)
et al. (2022b). To simulate the first and second GPT-3.5-turbo.
scenarios,weselect200examplesfromeachrea- BaselinesAsshowninFigure2,therearethreemasoningtaskrandomlyandthenmixthem,sincethe jorscenarioscoveringalmostallpossiblesituations.
costofaskktimesstageisheavilyexpensive. In the first scenario, we compare self-agreement
Language Models We evaluate self-agreement with2baselines: (i)Zero-ShotCoT(Kojimaetal.,
over two transformer-based language models on 2022);(ii)Self-Consistency(Wangetal.,2022). In
thefirstandsecondscenarios,andfourtransformer- the second scenario, we compare self-agreement
basedlanguagemodelsonthethirdscenario. For with 3 baselines: (i) Mixed-Few-Shot CoT. To
thefirstandsecondscenarios,weconsiderthefol- adaptfew-shotCoTtosuchscenario,werandomly
lowing language models: (i) GPT-3.5-turbo. We collects one demonstration from each reasoning
use the public gpt-3.5-turbo version of GPT-3.5 taskusedinWeietal.(2022b)andthenleveragethe
fromOpenAIAPI;7 (ii)Llama-2-13B-Chat(Tou- mixeddemonstrationsforallinputquestions. (ii)

### Self-Consistency (Wang et al., 2022); (iii) Multi-

6Weusethetestsplitforalltasksifthelabelsareavailable
forevaluation.ForCommonsenseQA,weusethedevsplit. 8Model checkpoints and inference code are available
7https://openai.com/blog/openai-api athttps://github.com/facebookresearch/llama.

<!-- Page 7 -->

60
55
50
0 5 10 15 20 25
# Sampled Reasoning Paths
)%(
ycaruccA

## Gsm8K

75
70
0 5 10 15 20 25
# Sampled Reasoning Paths
)%(
ycaruccA
CommonseQA
85.0
82.5
80.0
77.5
75.0
0 5 10 15 20 25
# Sampled Reasoning Paths
)%(
ycaruccA

### Last Letters

T=0.5, no top k
T=0.7, no top k
T=0.9, no top k
p=0.9
p=0.95

### Greedy Decode

Figure4: Self-agreementsignificantlyimprovesaccuracyoverzero-shotCoTwithgreedydecoding(grey)onthe
firstscenarioacrossarithmetic,commonsenseandsymbolicreasoningtasks,overGPT-3.5-turbo. Samplingahigher
numberofdiversereasoningpathsconsistentlyimprovesreasoningaccuracy. Inaddition,self-agreementisrobust
toreasoningpathswithvariousdiversityacrossarithmetic,commonsenseandsymbolicreasoningtasks.
Agents(Debate)(Duetal.,2023). Inthethirdsce- Model GSM8K CSQA Letter

### Zero-ShotCoT 48.5 71.0 81.0

nario,wecompareself-agreementwith3baselines:
Self-Consistency N/A N/A N/A

### GPT-3.5-turbo


### Self-Agreement(w/originalprompt) 58.5 77.8 83.8

(i) Few-Shot CoT (Wei et al., 2022b); (ii) Self- Self-Agreement(w/modifiedprompt) 56.7 77.5 83.4

### Consistency(Wangetal.,2022);(iii)USC(Chen

Table3: Self-agreementworkswithdifferentprompts.
etal.,2023b).

### SamplingSchemesTosamplediversereasoning

pathsintheaskktimesstage,wefollowthesame
the reasoning performance (average absolute acsettings of Wang et al. (2022). In particular, we
curacy +5.5% for GPT-3.5-turbo and +6.2% for
applytemperaturesamplingwithT =0.5andtrun-
Llama-2-13B-Chat)acrossalltwolanguagemodels
catedatthetop-k (k =40)tokenswiththehighest
overmixed-few-shotCoT,whileself-consistency
probabilityforLlama-2-Chatmodelswithvarious
performs even worse (average absolute accuracy
sizes. ForGPT-3.5-turbo,weuseT =0.7without
-1.2% for GPT-3.5-turbo and -0.5% for Llama-2-
top-k truncation.
13B-Chat)thanmixed-few-shotCoT.Becausede-
Evaluation Metrics For all datasets, we use acterminingwhethertwostringsrepresentthesame
curacy to evaluate the model’s reasoning perforfinalanswerisnotapplicableforitwhenthetype
mance.
of input questions is unknown. We provide furtheranalysisinAppendixB.3. Itcanalsobeseen
4.2 MainResults
thatmulti-agents(debate)attainsmorecompetitive
We report the results of self-agreement averaged performancecomparedwithzero-shotCoTwhen
over5runs,wherewesample20outputsfromthe using GPT-3.5-turbo as agents. We qualitatively
modelineachrun. find that it is more difficult for models of small
Theresultsonthefirstscenariowithsixdatasets scaletoarriveatthecorrectanswerasthedebate
from three categories are shown in Table 1. Self- progresseswhenfacingcaseswherealltheagents
agreementimprovesthereasoningperformancein initiallymakeincorrectpredictions(seeTable15
allreasoningtasksacrossalltwolanguagemodels intheAppendix). Theunderlyingreasonisthatthe
overzero-shotCoTwithoutrequiringtheanswer processofdebatingisanemergentabilityofmodel
formatstobesimilar,whileself-consistencyisnot scale (Wei et al., 2022a). That is, stronger modapplicable in this scenario as the reasoning paths els can better understand the debating rules and
havenotrigger(i.e.,Theansweris). Moresurpris- refine other agents’ incorrect outputs for further
ingly,thegainsbroughtbyourmethodarealmost improvement.
thesameacrossdifferentlanguagemodels’scales, Table 2 summarizes accuracy of our method,
furtherdemonstratingthegeneraleffectivenessof few-shotCoT,self-consistencyandUSCforeach
ourmethod. Forexample,wesee+5.8%average dataset. Similarly, self-agreement yields large
absoluteaccuracyimprovementoverLlama-2-13B- gains over few-shot CoT for all reasoning tasks.
Chatand+5.3%forGPT-3.5-turbowhenemploy- Meanwhile, self-agreement achieves almost the
ingself-agreement. same superior performance as self-consistency
Wecanalsodiscernagenerallyconsistentper- across almost all reasoning tasks, which it does
formancetrendinthesecondscenario, mirroring notneedanswerparsingtoperformthevoting. On
thatofthefirstscenario. Self-agreementimproves the contrary, the performance of USC is far infe-

<!-- Page 8 -->

50
40
30
1 5 10 20 40 80
Model size (#param in billions)
)%(
ycaruccA

## Gsm8K

70
65
60
55
1 5 10 20 40 80
Model size (#param in billions)
)%(
ycaruccA
CommonsenseQA
60
40
20
1 5 10 20 40 80
Model size (#param in billions)
)%(
ycaruccA

### Last Letters

Self-Agreement

### Greedy Decode

Figure5: Self-agreementimprovesperformanceacrossdifferentlanguagemodelscales.
rior to self-consistency and self-agreement, indi- mentsthatassessingwhetherornotapersonreally
catingthatself-agreementhasbetterexpandability knowshowtosolveaquestionshoulddependon
and can really approach the performance ceiling a small number of reasoning paths generated by
ofself-consistencywhileUSCcannot. Thisisalso themself,sinceapersonmightacquirethewrong
demonstratedinChenetal.(2023b). Weconsider answerduetocarelessnessorotherfactors.
thereisaninescapablegapbetweenperformance

### Self-Agreement is Robust to Reasoning Paths

andgeneralization. Weprovidedetaileddiscussion
with Different Diversity and Scaling Sampling
with USC in Appendix C. We also find that selfstrategies with different hyperparameters denote
agreementhaslargerperformancegainsformoregenerated reasoning paths with various diversity.
complicatedproblems. Forinstance,inArithmetic

### So, we are curios about whether self-agreement

Reasoning,forGSM8K(thedatasetwiththelowisrobusttoreasoningpathswithvariousdiversity.
est baseline performance), the performance gain

### Toshowtheeffectofreasoningpathswithvarious

(+12.4)ismorethantripledforothertasks. Thisis
diversity, we conduct the experiment by varying
analogoustotheintuitionself-agreementleveraged
T in temperature sampling (Ficler and Goldberg,
thatcomplexreasoningtaskstypicallyadmitmul-
2017)andpinnucleussampling(Holtzmanetal.,
tiple reasoning paths that reach a correct answer.
2019),overGPT-3.5-turbo. AsshowninFigure4,
The more that deliberate thinking and analysis is
wecanseethatself-agreementgraduallyimproves
requiredforaproblem,thegreaterthediversityof
reasoningperformanceregardlessofthediversity
reasoningpathsthatcanrecovertheanswer.
ofreasoningpathsasthenumberofreasoningpaths
4.3 Analysis increases. It also suggests that self-agreement is
robust to reasoning paths with various diversity.

### We conduct a number of additional experiments

Figure 5 shows that self-agreement robustly imto analyze different aspects of our approach. For
provesperformanceinGSM8K,CommonsenseQA
all experiments, we use GPT-3.5-turbo, and conand Last Letters across all scales for the Llamaduct experiments on the first scenario as it is the
2-Chatmodelseries(i.e.,7B,13Band70B).Itis
most relevant to the real-world scenario, unless
worthnotingthatthegainwhenusedwithLlama-2-
otherwisespecified. WeonlymixGSM8K,Com-
7B-Chatisrelativelylowduetothefactthatcertain
monsenseQAandLastLettersselectedfromeach
abilities only emerge when the model reaches a
categorytosimulatethefirstscenario.
sufficientscale(Brownetal.,2020).

### Effects of the Number of Sampled Reasoning

Paths We argue that the most agreed answer se- EffectsofDifferentSelf-AgreementPromptsWe
lectedfrommultiplereasoningpathsislikelytobe furthercarryoutexperimentstoexaminetheinfluthecorrectanswer. So,wearecuriosabouttheef- enceofthepromptusedinaskonemoretimestage
fectofthenumberofsampledreasoningpaths. As ofself-agreement. Specifically,wemodifytheorigshowninFigure4,weobservethattheperformance inalpromptbyfirsttranslatingitintoanotherlanfirstincreasessharplyandthenslowsdownasthe guage and then back again to construct the modnumberofsampledreasoningpathsincreases. This ified prompt. The original and modified prompts
iswhywesample20outputsforallscenariosand aregiveninTable11and13intheAppendix. As
tasks. In addition, sampling a higher number of showninTable3,wecanobserveself-agreement
reasoningpathsleadstoaconsistentlybetterper- (w/modifiedprompt)achievesalmostthesameperformance,butperformancenearlyconvergesatthe formance,indicatingthatself-agreementisrobust
numberof5or10. Thisisconsistentwithourstate- tothepromptswiththesamemeaning.

<!-- Page 9 -->

5 Conclusion References

### Tom Brown, Benjamin Mann, Nick Ryder, Melanie

In this work, we explore a more realistic setting

### Subbiah,JaredDKaplan,PrafullaDhariwal,Arvind

with significant application values in ensemble- Neelakantan,PranavShyam,GirishSastry,Amanda
optimization studies, as shown in Figure 2. To Askell,etal.2020. Languagemodelsarefew-shot
learners. Advancesinneuralinformationprocessing
thisend,weproposeself-agreement,asimpleyet
systems,33:1877–1901.
generalizable ensemble-optimization method applyinginalmostallscenarios. Self-agreementsi- Justin Chih-Yao Chen, Swarnadeep Saha, and Mohit
multaneously achieves remarkable performances Bansal.2023a. Reconcile: Round-tableconference
improves reasoning via consensus among diverse
onsixpublicreasoningbenchmarksandsuperior
llms. arXivpreprintarXiv:2309.13007.
generalization capabilities. Our findings encouragetheresearchcommunitytofocusonadeeper Xinyun Chen, Renat Aksitov, Uri Alon, Jie Ren, Keunderstanding of the role of language model it- fanXiao,PengchengYin,SushantPrakash,Charles
Sutton,XuezhiWang,andDennyZhou.2023b. Uniself in ensemble-optimization studies, which has
versalself-consistencyforlargelanguagemodelgenfavorablegeneralizationabilitiesandsuperiorper- eration. arXivpreprintarXiv:2311.17311.
formance. We hope this work will open new re-

### ZhoujunCheng,JungoKasai,andTaoYu.2023. Batch

searchpossibilitiesinprompting,languagemodels,
prompting: Efficientinferencewithlargelanguage
ensemble-optimizationandmulti-stepreasoning.
modelapis. arXivpreprintarXiv:2301.08721.
AakankshaChowdhery,SharanNarang,JacobDevlin,

### Limitations


### Maarten Bosma, Gaurav Mishra, Adam Roberts,


### Paul Barham, Hyung Won Chung, Charles Sutton,

There are two limitations of our approach. First, Sebastian Gehrmann, et al. 2022. Palm: Scaling
theaskktimesstageofself-agreementincursmore language modeling with pathways. arXiv preprint
computational cost. We suggest people can try a arXiv:2204.02311.
small number of paths (e.g., 5 or 10) to achieve

### PeterClark,IsaacCowhey,OrenEtzioni,TusharKhot,

mostoftheperformancegainswhilenotbringing AshishSabharwal,CarissaSchoenick,andOyvind
too much cost, since we have shown that perfor- Tafjord.2018. Thinkyouhavesolvedquestionanswering? tryarc,theai2reasoningchallenge. arXiv
mancenearlyconvergesatthenumberof5or10.
preprintarXiv:1803.05457.

### Besides,therearesomeworkinvestigatinghowto

enabletheLLMtoruninferenceinbatches(Cheng Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
et al., 2023; Lin et al., 2023). As part of future MarkChen,HeewooJun,LukaszKaiser,Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
work,onecouldmixdifferentquestionsasabatch,
Nakano,etal.2021. Trainingverifierstosolvemath
andruninferenceinabatchonetime. Afterthat,
wordproblems. arXivpreprintarXiv:2110.14168.
self-agreementrequiresonlytwoinferences,thus

### Shizhe Diao, Pengcheng Wang, Yong Lin, and Tong

significantly decreasing computational cost. Sec-
Zhang. 2023. Active prompting with chain-ofond,intheaskonemoretimestage,wemodifythe
thoughtforlargelanguagemodels. arXivpreprint
inputquestionxanditsmultiplereasoningpaths arXiv:2302.12246.
z into a prompt s. This may cause the length of
i
YilunDu,ShuangLi,AntonioTorralba,JoshuaBTenena prompt s exceeds the maximum context length
baum,andIgorMordatch.2023. Improvingfactualof language models. For example, the maximum
ityandreasoninginlanguagemodelsthroughmultiacontextlengthofLlama-2-ChatmodelsandGPT- gentdebate. arXivpreprintarXiv:2305.14325.
3.5-turbois4,096and8,192respectively. Inprac-

### Jessica Ficler and Yoav Goldberg. 2017. Controlling

tice,asshowninFigure4,performancenearlyconlinguisticstyleaspectsinneurallanguagegeneration.
verges at the number of 5 or 10. So, the maxi- arXivpreprintarXiv:1707.02633.
mum context length of language models is likely
JiayiFu,LeiLin,XiaoyangGao,PengliLiu,Zhengzong
tobeenoughforself-agreementinmostsituations.
Chen, Zhirui Yang, Shengnan Zhang, Xue Zheng,

### Meanwhile,therearealsosomeworkfocusingon

YanLi,YuliangLiu,etal.2023. Kwaiyiimath: Techhowtoincreasethecontextlengthoflanguagemod- nicalreport. arXivpreprintarXiv:2310.07488.
els(Lietal.,2023a;Xiongetal.,2023). Therefore,
Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark,
inthefuture,thelimitationsofthecontextlength
andTusharKhot.2022. Complexity-basedpromptwillbecomesmallerandsmaller.
ing for multi-step reasoning. arXiv preprint
arXiv:2210.00720.

<!-- Page 10 -->

AriHoltzman,JanBuys,LiDu,MaxwellForbes,and YaoLu,MaxBartolo,AlastairMoore,SebastianRiedel,
Yejin Choi. 2019. The curious case of neural text and Pontus Stenetorp. 2021. Fantastically ordered
degeneration. arXivpreprintarXiv:1904.09751. prompts and where to find them: Overcoming
few-shot prompt order sensitivity. arXiv preprint
JacobDevlinMing-WeiChangKentonandLeeKristina arXiv:2104.08786.
Toutanova.2019. Bert: Pre-trainingofdeepbidirectionaltransformersforlanguageunderstanding. In
MaxwellNye,AndersJohanAndreassen,GuyGur-Ari,
ProceedingsofnaacL-HLT,volume1,page2.
Henryk Michalewski, Jacob Austin, David Bieber,

### David Dohan, Aitor Lewkowycz, Maarten Bosma,

Daniel Khashabi, Sewon Min, Tushar Khot, Ashish

### DavidLuan,etal.2021. Showyourwork: Scratch-

Sabharwal, Oyvind Tafjord, Peter Clark, and Hanpads for intermediate computation with language
nanehHajishirzi.2020. Unifiedqa: Crossingformat
models. arXivpreprintarXiv:2112.00114.
boundarieswithasingleqasystem. arXivpreprint
arXiv:2005.00700.

### Adam Paszke, Sam Gross, Francisco Massa, Adam

TakeshiKojima,ShixiangShaneGu,MachelReid,Yu- Lerer, James Bradbury, Gregory Chanan, Trevor
takaMatsuo,andYusukeIwasawa.2022. Largelan- Killeen, Zeming Lin, Natalia Gimelshein, Luca
guagemodelsarezero-shotreasoners. Advancesin Antiga, et al. 2019. Pytorch: An imperative style,
neural information processing systems, 35:22199– high-performancedeeplearninglibrary. Advancesin
22213. neuralinformationprocessingsystems,32.
AitorLewkowycz,AndersAndreassen,DavidDohan, Arkil Patel, Satwik Bhattamishra, and Navin Goyal.
EthanDyer,HenrykMichalewski,VinayRamasesh, 2021. Are nlp models really able to solve
Ambrose Slone, Cem Anil, Imanol Schlag, Theo simple math word problems? arXiv preprint
Gutman-Solo,etal.2022. Solvingquantitativerea- arXiv:2103.07191.
soningproblemswithlanguagemodels. Advances
inNeuralInformationProcessingSystems,35:3843– XinyuPi,QianLiu,BeiChen,MortezaZiyadi,ZeqiLin,

## Yan Gao, Qiang Fu, Jian-Guang Lou, and Weizhu

Chen.2022. Reasoninglikeprogramexecutors.
DachengLi,RulinShao,AnzeXie,YingSheng,Lianmin Zheng, and et.al. 2023a. How long can open-
ShuofeiQiao,YixinOu,NingyuZhang,XiangChen,
sourcellmstrulypromiseoncontextlength?

### YunzhiYao,ShuminDeng,ChuanqiTan,FeiHuang,

and Huajun Chen. 2022. Reasoning with lan-
YifeiLi,ZeqiLin,ShizhuoZhang,QiangFu,BeiChen,
guagemodelprompting: Asurvey. arXivpreprint
Jian-GuangLou,andWeizhuChen.2023b. Making
arXiv:2212.09597.
language models better reasoners with step-aware
verifier. In Proceedings of the 61st Annual Meet-
Jack W Rae, Sebastian Borgeaud, Trevor Cai, Katie
ingoftheAssociationforComputationalLinguistics
Millican, Jordan Hoffmann, Francis Song, John
(Volume1: LongPapers),pages5315–5333.

### Aslanides, Sarah Henderson, Roman Ring, Susan-

Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, nah Young, et al. 2021. Scaling language models:
YanWang,RuiWang,YujiuYang,ZhaopengTu,and Methods,analysis&insightsfromtraininggopher.
ShumingShi.2023. Encouragingdivergentthinking arXivpreprintarXiv:2112.11446.
inlargelanguagemodelsthroughmulti-agentdebate.
arXivpreprintarXiv:2305.19118. ColinRaffel,NoamShazeer,AdamRoberts,Katherine

### Lee,SharanNarang,MichaelMatena,YanqiZhou,

Jianzhe Lin, Maurice Diesendruck, Liang Du, and WeiLi,andPeterJLiu.2020. Exploringthelimits
RobinAbraham.2023. Batchprompt: Accomplish oftransferlearningwithaunifiedtext-to-texttransmorewithless. arXivpreprintarXiv:2309.00384. former. TheJournalofMachineLearningResearch,
21(1):5485–5551.
JiachangLiu,DinghanShen,YizheZhang,BillDolan,

### Lawrence Carin, and Weizhu Chen. 2021. What

SubhroRoyandDanRoth.2015. Solvinggeneralarithmakesgoodin-contextexamplesforgpt-3? arXiv
metic word problems. In Proceedings of the 2015
preprintarXiv:2101.06804.
Conference on Empirical Methods in Natural LanguageProcessing,pages1743–1752,Lisbon,Portu-
PengfeiLiu,WeizheYuan,JinlanFu,ZhengbaoJiang,
gal.AssociationforComputationalLinguistics.
Hiroaki Hayashi, and Graham Neubig. 2023. Pretrain, prompt, and predict: A systematic survey of
Subhro Roy and Dan Roth. 2016. Solving genpromptingmethodsinnaturallanguageprocessing.
ACMComputingSurveys,55(9):1–35. eral arithmetic word problems. arXiv preprint
arXiv:1608.01413.

### Pan Lu, Liang Qiu, Kai-Wei Chang, Ying Nian Wu,

Song-Chun Zhu, Tanmay Rajpurohit, Peter Clark, KaShun Shum, Shizhe Diao, and Tong Zhang. 2023.
andAshwinKalyan.2022. Dynamicpromptlearning Automaticpromptaugmentationandselectionwith
viapolicygradientforsemi-structuredmathematical chain-of-thoughtfromlabeleddata. arXivpreprint
reasoning. arXivpreprintarXiv:2209.14610. arXiv:2302.12822.

<!-- Page 11 -->

Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Yichong Xu, Chenguang Zhu, Shuohang Wang, Siqi
AbuAwalMdShoeb,AbubakarAbid,AdamFisch, Sun, Hao Cheng, Xiaodong Liu, Jianfeng Gao,
Adam R Brown, Adam Santoro, Aditya Gupta, PengchengHe,MichaelZeng,andXuedongHuang.
Adrià Garriga-Alonso, et al. 2022. Beyond the 2021. Human parity on commonsenseqa: Augimitation game: Quantifying and extrapolating the mentingself-attentionwithexternalattention. arXiv
capabilities of language models. arXiv preprint preprintarXiv:2112.03254.
arXiv:2206.04615.

### ChengrunYang,XuezhiWang,YifengLu,HanxiaoLiu,

Alon Talmor, Jonathan Herzig, Nicholas Lourie, and QuocVLe,DennyZhou,andXinyunChen.2023a.
JonathanBerant.2018. Commonsenseqa:Aquestion Largelanguagemodelsasoptimizers. arXivpreprint
answeringchallengetargetingcommonsenseknowl- arXiv:2309.03409.
edge. arXivpreprintarXiv:1811.00937.
JingfengYang, HongyeJin, RuixiangTang, Xiaotian

### Han,QizhangFeng,HaomingJiang,BingYin,and


### RomalThoppilan,DanielDeFreitas,JamieHall,Noam

Xia Hu. 2023b. Harnessing the power of llms in

### Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng,

practice: A survey on chatgpt and beyond. arXiv
Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, et al.
preprintarXiv:2304.13712.

## Lamda: Languagemodelsfordialogapplications. arXivpreprintarXiv:2201.08239.

Liu Yang, Haihua Yang, Wenjun Cheng, Lei Lin,

### ChenxiaLi,YifuChen,LunanLiu,JianfeiPan,Tian-

Hugo Touvron, Louis Martin, Kevin Stone, Peter AlwenWei,BiyeLi,LiangZhao,LijieWang,BoZhu,
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Guoliang Li, Xuejie Wu, Xilin Luo, and Rui Hu.

### Bashlykov,SoumyaBatra,PrajjwalBhargava,Shruti

2023c. Skymath: Technicalreport. arXivpreprint
Bhosale, et al. 2023. Llama 2: Open foundaarXiv:2310.16713.
tion and fine-tuned chat models. arXiv preprint
arXiv:2307.09288.
FeiYu,HongboZhang,andBenyouWang.2023a. Nature language reasoning, a survey. arXiv preprint
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
arXiv:2303.14725.

### Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz

Kaiser,andIlliaPolosukhin.2017. Attentionisall Longhui Yu, Weisen Jiang, Han Shi, Jincheng Yu,
youneed. Advancesinneuralinformationprocessing Zhengying Liu, Yu Zhang, James T Kwok, Zhensystems,30. guo Li, Adrian Weller, and Weiyang Liu. 2023b.

### Metamath: Bootstrapyourownmathematicalques-

JiaanWang,YunlongLiang,FandongMeng,Haoxiang tions for large language models. arXiv preprint
Shi,ZhixuLi,JinanXu,JianfengQu,andJieZhou. arXiv:2309.12284.

## Ischatgptagoodnlgevaluator? apreliminary

study. arXivpreprintarXiv:2303.04048. Xiang Yue, Xingwei Qu, Ge Zhang, Yao Fu, Wenhao Huang, Huan Sun, Yu Su, and Wenhu Chen.
XuezhiWang,JasonWei,DaleSchuurmans,QuocLe, 2023. Mammoth: Buildingmathgeneralistmodels
EdChi,SharanNarang,AakankshaChowdhery,and through hybrid instruction tuning. arXiv preprint
DennyZhou.2022. Self-consistencyimproveschain arXiv:2309.05653.
of thought reasoning in language models. arXiv
preprintarXiv:2203.11171. Zhuosheng Zhang, Aston Zhang, Mu Li, and Alex

### Smola. 2022. Automatic chain of thought prompt-

Albert Webson and Ellie Pavlick. 2021. Do prompt- ing in large language models. arXiv preprint
basedmodelsreallyunderstandthemeaningoftheir arXiv:2210.03493.
prompts? arXivpreprintarXiv:2109.01247.
Zihao Zhao, Eric Wallace, Shi Feng, Dan Klein, and

### SameerSingh.2021. Calibratebeforeuse: Improv-

Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel,
ingfew-shotperformanceoflanguagemodels. InIn-
Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
ternationalConferenceonMachineLearning,pages
MaartenBosma,DennyZhou,DonaldMetzler,etal.

## 12697–12706.Pmlr.

2022a. Emergentabilitiesoflargelanguagemodels.
arXivpreprintarXiv:2206.07682.
Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han,
KeiranPaster,SilviuPitis,HarrisChan,andJimmy
JasonWei,XuezhiWang,DaleSchuurmans,Maarten
Ba.2022. Largelanguagemodelsarehuman-level

### Bosma,FeiXia,EdChi,QuocVLe,DennyZhou,

promptengineers. arXivpreprintarXiv:2211.01910.
etal.2022b. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels. AdvancesinNeural
Anni Zou, Zhuosheng Zhang, Hai Zhao, and Xian-
InformationProcessingSystems,35:24824–24837.
gruTang.2023. Meta-cot: Generalizablechain-ofthoughtpromptinginmixed-taskscenarioswithlarge
WenhanXiong,JingyuLiu,IgorMolybog,HejiaZhang, languagemodels. arXivpreprintarXiv:2310.06692.
Prajjwal Bhargava, Rui Hou, Louis Martin, Rashi

### Rungta,KarthikAbinavSankararaman,BarlasOguz,

etal.2023. Effectivelong-contextscalingoffoundationmodels. arXivpreprintarXiv:2309.16039.

<!-- Page 12 -->

A ExperimentalDetails Model Arithmetic Commonsense Symbolic

### GSM8K CSQA Letter

A.1 TasksandDatasets Boththetypeofquestionsandtheanswerformatareunknown(thefirstscenario)
200randomlyselectedexamples
Weevaluateself-agreementonsixpublicreasoning

### Zero-ShotCoT 48.5 71.0 81.0

benchmarks for a fair comparison with existing Self-Agreement58.5(+10.0) 77.8(+6.8) 83.8(+2.8)
400randomlyselectedexamples
methods, covering arithmetic, commonsense and

### GPT-3.5-turbo Zero-ShotCoT 48.8 70.5 77.8

symbolicreasoningtasks. Thedetailedstatisticsof Self-Agreement54.3(+5.5) 77.1(+6.6) 80.4(+3.3)
thedatasetsareshowninTable4. 600randomlyselectedexamples

### Zero-ShotCoT 47.8 69.6 79.6

Self-Agreement54.0(+6.2) 77.1(+7.5) 81.9(+2.3)

### Dataset Numberofsamples AnswerFormat Licence

MultiArith 600 Number Unspecified Table 5: Self-agreement, when applied on GPT-3.5-
GSM8K 1,319 Number MITLicense turbo. Ourperformancegain(+blue)iscomputedover

### SVAMP 1,000 Number MITLicense

CSQA 1,221 Multiplechoice Unspecified thezero-shotCoT(Kojimaetal.,2022),whichisour

### LastLetters 500 String Unspecified

primarybaseline. Ourmethodsubstantiallyincreases
ARC-c 1,172 Multiplechoice CCBY-SA
theperformanceoverzero-shotCoT.
Table4: Detaileddatasetdescription.

### ForGPT-3.5-turbo,wefollowthesameexperi-

A.2 BaselineMethods mentalsettingsofKojimaetal.(2022)andset128,
256maxtokensforaskktimesandaskonemore
Weintroducethebaselinemethodsindetail.
timephasesrespectively,withoutfrequencypenalty
Few-ShotCoT Few-ShotCoT(Weietal.,2022b) orpresencepenalty. ForLlama-2-Chatmodels,we
employs several additional templated demonstra- set 128 max tokens for ask k times without fretions as: “Q: q. A: (r, a).” before the input quencypenaltyorpresencepenalty. Intheaskone
question, where q, r and a are manually crafted more time stage, we continue to generate tokens
questions,rationalesandfinalanswers. untilthestoptoken(e.g.,“</s>”)isgenerated. We
use greedy decoding across all the models in ask

### Zero-Shot CoT Zero-Shot CoT (Kojima et al.,

one more time phase. Our implementation is in
2022)simplyinsertstheprompt“Let’sthinkstep
PyTorch(Paszkeetal.,2019).
bystep”aftertheinputquestion.

### Here,wedescribetheimplementationdetailsof

Self-Consistency Self-Consistency(Wangetal., baselinemethodsindifferentscenarios. Inthefirst
2022) first samples multiple reasoning paths by scenario,toadaptzero-shotCoTtosuchscenario,
usingfew-shotCoT,andthenselectsthemostcon- weusethegeneralprompt(i.e.,Theansweris)for
sistent answer by marginalizing out the sampled answerextraction. Forallensemble-optimization
reasoningpaths. methods,weemployzero-shotCoT(Kojimaetal.,
2022)without2ndanswerextractionphasetosim-
Multi-Agents (Debate) Multi-Agents (Deulate the reasoning paths with no trigger. Selfbate) (Du et al., 2023) takes language models as
consistency is not applicable in this scenario as
multi-agentstoproposeanddebatetheirindividual
the reasoning paths have no trigger. In the secresponses and reasoning processes over multiple
ond scenario, to adapt few-shot CoT to such sceroundstoarriveatacommonfinalanswer.
nario,werandomlyselectonedemonstrationfrom
USC USC(Chenetal.,2023b)leveragesLLMs eachreasoningtaskusedinWeietal.(2022b)and
themselves to select the most consistent answer thenleveragethemixeddemonstrationsforallinamongmultiplecandidates. put questions (called mixed-few-shot CoT). The
demonstrations are given in Table 14, and other

### A.3 ImplementationDetails

experimental settings are the same as Wei et al.
For all language models we evaluated, we per- (2022b). To adapt self-consistency to such sceform prompting-based inference only. For GPT- nario, we extract the strings between the trigger
3.5-turbo,weusethepublicversiongpt-3.5-turbo (i.e., “The answer is”) and full stop (i.e., “.”) of
ofGPT-3.5fromOpenAIAPI.ForLlama-2-Chat thereasoningpaths. Forexample,asshowninFigmodels,weusetheopen-sourcedlibrary,andrun ure2,weobtain6hoursextractedfromtheoutput
experimentsonNVIDIATeslaA800(8x8configu- 2. Toadaptmulti-agents(debate)(Duetal.,2023)
ration,80G). tosuchscenario,wemodifythepromptusedinDu

<!-- Page 13 -->

et al. (2023) for GSM8K to make it applying in
almost all scenarios, since Du et al. (2023) have 80
75 designedaspecificpromptforeachtask,whichis
70 notageneralizablemethod. Themodifiedprompt
65
is given in Table 12. Other experimental settings 60
0 10 20 30 40
arethesameasDuetal.(2023). Inthethirdsce- #Sampled Reasoning Paths
nario, we use the same prompts and experiment
settingsusedinWeietal.(2022b)toemployfewshotCoT,thesameexperimentalsettingsofWang
et al. (2022) to employ self-consistency, and the
sameexperimentalsettingsofChenetal.(2023b)
toemployUSC.

### B AdditionalExperiments

B.1 Are200RandomlySelectedExamples

### Enough?


### As mentioned in Section 4.1, to be economical,

weonlyselect200examplesfromeachpublicreasoningbenchmarkrandomlyandthenmixthemto
simulate situations of the unknown type of input
questions. Tofurthervalidatethesoundnessofexperimentalresultsinthefirstscenarioprovidedin
Table1,weconductexperimentsonGSM8K,CommonsenseQAandLastLettersbyvaryingthenumberofrandomlyselectedexamples(i.e.,200,400
and600).9 AsshowninTable5,theperformance
fluctuates slightly with different number of randomlyselectedexamplesfromeachreasoningtask
over zero-shot CoT and self-agreement. Overall
speaking, self-agreementimprovesthereasoning
performanceinallreasoningtasksoverzero-shot
CoT.
B.2 FurtherAnalysisonSelf-Agreementvs.

### Self-Consistency

To have an entirely fair comparison with selfconsistency, we conduct experiments on 20 and
40sampledreasoningpathsrespectively. Asshown
in Table 6, it is interesting to note that when the
number of sampled reasoning paths is 20, selfagreement achieves an average performance increase of 0.2 over all reasoning tasks compared
toself-consistency,butitinsteaddecreasesby0.3
when the number of sampled reasoning paths is
increasedto40. Toinvestigatethisinfluence, we
conduct experiments on GSM8K and CommonseQAwithself-consistencyandself-agreementby
varying the number of sampled reasoning paths.
9NotethatthetestsetofLastLettersdatasetonlycontains
500 examples. Thus, we useall examples when randomly
selected600examplesfromeachreasoningtask.
)%(
ycaruccA

## Gsm8K

78
76
74
0 10 20 30 40
# Sampled Reasoning Paths
)%(
ycaruccA

### CommonseQA

Self-Consistency Self-Agreement

### Greedy Decode

Figure 6: Self-agreement utilizes sampled reasoning
pathsmoreefficientlythanself-consistencywhenthe
numberofsampledreasoningpathsislessthan20.Samplingaenoughhighnumberofreasoningpathsachieves
essentiallythesameperformanceforself-consistency
andself-agreement.
AsshowninFigure6,self-agreementutilizessampled reasoning paths more efficiently than selfconsistencywhenthenumberofsampledreasoning paths is less than 20. Sampling a enough
high number of reasoning paths achieves essentially the same performance for self-consistency
andself-agreement. Theunderlyingreasonisthat
self-agreementisageneralizableanswerextractor
while self-consistency is a rule-based answer extractor,i.e.,onlyextractthereasoningpathswith
trigger(e.g.,Theansweris). Thiscausesittodrop
reasoningpathswithouttrigger.
B.3 WhySelf-ConsistencyPerformWorsein
theSecondScenario?

### To better figure out this question, we need to

review the theory and implementations of selfconsistency (Wang et al., 2022). In detail, given
aquestion,self-consistencyfirstsamplefromthe
languagemodel’sdecodertogeneratediversemultiplereasoningpaths,extractthefinalanswersof
sampled reasoning paths to form a answer set a ,
i
and then choose the answer with the most occurrences. The overall process is outlined in Alogorithm1. Itisclearthatthemostimportantstep
for the self-consistency method is how to extract
theanswersofreasoningpathsexactly,whilethe
answer_cleaning function is to perform different
extractionrulesaccordingtodifferenttypesofinputquestions. Forinstance,weextractarabicnumeralsforGSM8K,but(A-E)forCommonseQA.
To adapt self-consistency to this scenario, we extract the strings between the trigger (e.g., “The
answeris”)andfullstop(e.g.,“.”) asthefinalanswers. Thisiswhyself-consistencyevenperform
worsethanthebaselinemixed-few-shotCoTinthis
scenario. Becausedeterminingwhethertwostrings
representthesamefinalanswerisnotapplicable
foritwhenthetypeofinputquestionsisunknown.

<!-- Page 14 -->


### Model Arithmetic Commonsense Symbolic


### GSM8K MultiArith SVAMP CSQA ARC-c Letter

Boththetypeofquestionsandtheanswerformatareknown(thethirdscenario)
20sampledreasoningpaths
Self-Consistency 80.3 99.2 85.9 79.0 87.0 81.9

## Usc 76.8 98.2 83.5 48.9 73.9 79.4

Self-Agreement 82.4(+2.1) 99.0(-0.2) 86.0(+0.1) 79.4(+0.4) 86.8(-0.2) 81.0(-0.9)

### GPT-3.5-turbo

40sampledreasoningpaths
Self-Consistency 81.9 99.2 86.5 79.4 87.1 82.4

## Usc 76.0 98.7 82.4 63.7 79.1 73.8

Self-Agreement 82.7(+0.8) 99.0(-0.2) 86.2(-0.3) 79.4(+0.0) 86.9(-0.2) 81.5(-0.9)
Table6: Self-agreement,whenappliedonGPT-3.5-turbo. Ourperformancegain(+blue)iscomputedoverselfconsistency(Wangetal.,2022). Thebestperformanceforeachtaskisshowninbold.
Algorithm1PseudocodeofSelf-ConsistencyinaPython-likestyle.
# answer_cleaning: extract the final answer from a reasoning path to a question that belongs to a known task. We adopt the
code in https://github.com/kojima-takeshi188/zero_shot_cot/blob/main/utils.py
# questions: questions
# groundtruth_answers: groundtruth answers to each question
# diverse_answers: multiple sampled reasoning paths to each question
# maj_ans: return the string with the most occurrences
# judge_ans: return True if two answers are the same or False
correct_counts = 0 # the number of correct answers
for i in range(len(questions)):
pred_lists = [] # collect the final answer extracted from each reasoning path
groundtruth_answer = groundtruth_answers[i]
for j in range(len(diverse_answers[i])):
pred = answer_cleaning(diverse_answers[i][j]) # extract the answer of j reasoning path to i question
if pred:
pred_lists.append(pred)
optimal_answer = maj_ans(pred_lists) # return the string with the most occurrences in pred_list
if judge_ans(groundtruth_answer, optimal_answer):
correct_counts += 1
print(correct_counts / len(questions))
Forinstance,6hoursand6extractedfromoutputs Model GSM8K-Multi
2,3ofFigure2respectivelyrepresenttwodifferent

### Zero-ShotCoT 59.7

answerswhenemployingself-consistencyinthis GPT-3.5-turbo Self-Consistency N/A
scenario. Self-Agreement 64.3(+4.6)
B.4 FurtherExplorationofSelf-Agreement Table 7: Self-agreement achieves better performance
overallstrongbaselinesonGSM8K-Multi.
onOpen-endedReasoningTask

### AsshowninFigure2,weonlycategorizethetypes

ofquestionsintoknownandunknownfromaspe- itsgroundtruthanswer“TheanswerisAandB.”.
cificangle,i.e.,whetherwecanidentifyinadvance Sadly,asfarasweknow,thereisnosuchpublicly
thatthequestionbelongstoaparticulartask. How- availablereasoningdatasettotesttheeffectiveness
ever, we wonder if this is really the case in real- of our proposed self-agreement. We guess that
world scenarios. In practice, there exists another there are two reasons. First, constructing such a
angle of its division. In detail, a reasoning path dataset is more labor intensive. Second, it is difto a question has multiple different sub-answers ficult to assess the accuracy of the final answers
consistingofthefinalanswer. Forinstance,aques- when solving such questions and most likely retion “Axel has 50 silver pesos and 80 gold pesos quireshumanevaluation.
...,HowmanypesosdoesAnnahave? What’sthe Additionally,weconsiderthatourmethodstill
total number of pesos they have together?” and canachievesubstantiallybetterperformanceover
its groundtruth answer “Anna has 140 pesos and baselines when encountering this type of input
theyhaveatotalof270pesostogether.”,oraques- questions. To answer this, we explain the nation “What is Beijing? Answer Choices: (A) a tureofmostensemble-optimizationworkandselfcity (B) the capital of China (C) an island” and agreementintermsofdefinitionsandexperiments.

<!-- Page 15 -->

Model Arithmetic Commonsense Model Arithmetic

## Gsm8K Csqa Gsm8K Svamp

Boththetypeofquestionsandtheanswerformatareknown(thethirdscenario) Boththetypeofquestionsandtheanswerformatareknown(thethirdscenario)

### Few-ShotCoT 48.1 77.1 Few-ShotCoT 70.0 82.0

Llama-2-70B-Chat Self-Consistency 59.7 78.0 Self-Consistency 80.3 85.9
Self-Agreement 61.0(+12.9) 77.7(+0.6) Self-Agreement 82.4(+12.4) 86.0(+4.0)

### GPT-3.5-turbo


### Few-ShotCoT 90.8 86.9 ComplexCoT 82.8 80.3


### GPT-4 Self-Consistency 93.3 88.1 Self-Consistency 88.5 87.3

Self-Agreement 93.9(+3.1) 87.9(+1.0) Self-Agreement 88.3(+5.5) 87.2(+6.9)
Table 8: Our performance gain (+blue) is computed Table9:Ourperformancegain(+blue)iscomputedover
over few-shot CoT (Wei et al., 2022b), which is our few-shotCoT(Weietal.,2022b)orComplexCoT(Fu
primarybaseline. Ourmethodssubstantiallyincrease etal.,2022),whichisourprimarybaseline. OurmeththeperformanceoverWeietal.(2022b). ods substantially increase the performance over Wei
etal.(2022b)and(Fuetal.,2022).

### From the perspective of definitions, we view

ten into the type we need.11 If possible, directly
mostensemble-optimizationworkasdifferentimrewrite the math question and ensure coherence
plementations of the majority voted idea.10 For
betweentwodifferentproblems. Ifnot,discardit.
example,self-consistency(Wangetal.,2022)takes

### Table10providesexamplesoforiginalquestions

the majority vote over sampled reasoning paths,
and rephrased questions of GSM8K. The correwhile multi-agents (debate) (Du et al., 2023) obsponding solutions are also rewritten by them to
tainsthecommonfinalanswerovermultipleagents’
guaranteetheaccuracyofanswers. Wefinallyoboutputs. Itisclearthattheessenceofthemisbased
tain362examplesasthetestsetofGSM8K-Multi.
on the majority voted design, and our work is in
Theentiredatasetwillbereleasedsoon. Thus,to
lineswithit,butweexplorehowtoallowlanguage
validatethestatementthatself-agreementstillcan
modelitselftoachievetheoverallprocedure. So,
achievesubstantiallybetterperformanceoverbasethemaindifferencebetweenthemliesintwomalines, we follow the same experimental settings
jorstepsconsistingoftheprocessofthemajority
usedinthefirstscenarioandconductexperiments
vote, i.e., answer extraction and answer comparon the GSM8K-Multi dataset. As shown in Taison. To be specific, self-consistency and multible 7, overall speaking, self-agreement achieves
agents (debate) are rule-based and not generalizbetter performance over all strong baselines on
ablemethodtoextractandcompareanswers. How-

### GSM8K-Multi, demonstrating that it is entirely

ever, self-agreement is an entirely generalizable
generalizablemethod,whetherextractinganswers
method,whetherextractinganswersorcomparing
orcomparinganswers.12
answers.
In the future, we plan to design an automated
From the perspective of experiments, in order
evaluationmethodtosavelaborcosts. Asfaraswe
to promote the development of this field and test
know, there are some work to investigate how to
thegeneraleffectivenessofourmethod,webuild
useChatGPTorGPT-4asanautomatedevaluation
anopen-endedarithmeticdataset,GSM8K-Multi,
metricforvariousNLPtasks(Wangetal.,2023).
based on GSM8K (Cobbe et al., 2021), where a
reasoningpathtoaquestionhastwodifferentsub- B.5 ExperimentswithMoreLanguageModels
answersconsistingofthefinalanswer. Thereason To further demonstrate the general effectiveness
forbuildingthedatasetinthearithmeticcategory ofself-agreementwithmorelanguagemodels,we
isthatGSM8Kisamorecomplicateddatasetthan conductexperimentsonGSM8KandCSQAwith
others (the dataset with the lowest baseline per- Llama-2-70B-ChatandGPT-4inthethirdscenario.
formance) to better measure the effectiveness of ThereasonwechooseGSM8KandCSQAisthat
different methods. To build this dataset, we only
11Wefollowtwoprinciplestorephrasethequestion.First,
select 500 examples randomly from GSM8K to
keepthedifficultyoftheoriginalquestionasmuchaspossible.
savelaborcosts. Wethenhirecrowd-sourcedwork- Second,addanewproblemundertheoriginalconditionsand
ers who are Chinese-English bilingual speakers itdoesnotconflictwiththeoriginalproblem.
12We hire the same crowd-sourced workers to manually
withenoughmathematicalknowledgetomanually
evaluatetheaccuracyoftheanswers.Wefollowtwoprinciples
determinewhetherthemathquestioncanberewrit- forthefairandstrictevaluation. First,onlytheaccuracyof
thefinalanswerinsteadofthereasoningpathisevaluatedto
savelaborcosts.Second,thesolutioniscorrectonlyifboth
10Detailsrefertocorrespondingpapers. sub-answersconsistingofthefinalanswerarecorrect.

<!-- Page 16 -->

theyaremorecomplicatedthanothers(thedataset ure2. Furthermore,topromptthisfield,webuild
withthelowestbaselineperformance). Asshownin anopen-endedarithmeticdataset,GSM8K-Multi,
Table8,self-agreementconsistentlyimprovesover based on GSM8K (Cobbe et al., 2021), where a
thefew-shotCoT,andtheperformanceisgenerally reasoningpathtoaquestionhastwodifferentsubcomparabletothestandardself-consistency,which answers consisting of the final answer, resulting
self-agreement does not need answer parsing to in a more free-form and complicated answer forperformthevoting. mats. However, they only test the effectiveness
oftheirmethodontwopublicfix-endedreasoning
B.6 ExperimentswithMoreCoTPrompting tasks. Fourthly, the prompt used in this work is
Methods differentfromthatusedinUSC.Wedesignamore
domain-specific prompt to select the optimal re-
Tofurtherdemonstratethegeneraleffectivenessof
sponse,whichcanfurtherboostUSC.Thisisalso
self-agreementonmoreCoTpromptingmethods,
demonstratedinChenetal.(2023b). Fifthly,selfwereproduceoneoftheverypopularCoTpromptagreementachievesbetterperformancethanUSC,
ingwork,i.e.,ComplexCoT(Fuetal.,2022),and
indicating that self-agreement has better expandconductexperimentsonGSM8KandSVAMPwith
ability and can really approach the performance
GPT-3.5-turbointhethirdscenario. Thereasonwe
ceilingofself-consistencywhileUSCcannot. To
chooseGSM8KandSVAMPinarithmeticreasonbespecific,forself-agreement,samplingahigher
ingisthattheyaremorecomplicatedthanothers
numberofreasoningpathsleadstoaconsistently
(thedatasetwiththelowestbaselineperformance).
betterperformance,whiletheoppositeistruefor

### AsshowninTable9,self-agreementconsistently

USC. So, we strongly question the statements in
improvesovertheComplexCoT,indicatingthatit
thispaper,i.e.,theperformanceisgenerallycompais applicable and beneficial to various prompting
rabletothestandardself-consistency,whichUSC
methods.
doesnotneedanswerparsingtoperformthevoting.
C DiscusstionwithUSC Itisunfairtocomparewithself-consistencywhen
thenumberofsampledreasoningpathsis8rather
Aftercompletionofthiswork, wefindthatChen than40(experimentalsettingsinself-consistency
etal.(2023b)sharealmostthesameideawithus, paper). AsshowninTable6,itcanbeseenthatselfwhichisarchivedafterourwork. So,wewouldlike agreement matches the standard self-consistency
todiscussthedifferencesbetweenourworkandit. performancewithoutrequiringtheanswerformats
Firstly, our work was archived on 14 Nov 2023, tobesimilar,however,theperformanceofUSCis
however, they were 29 Nov 2023. So, it is clear farinferiortoself-consistencyandself-agreement.
andcertainthatwearethefirsttoproposethereal- Also,samplingahighernumberofreasoningpaths
worldscenariosinensemble-optimizationstudies, leads to a consistently better performance, while
anddesignasimpleensemble-optimizationmethod the opposite is true for USC. Therefore, we conapplying in almost all scenarios. Secondly, Our siderthereisaninescapablegapbetweenperforworkstudiesensemble-optimizationinmulti-step manceandgeneralization. Wefocusonhowto
reasoningsituations, i.e., open-endedreasoning solveopen-endedreasoningtasks,notopen-ended
tasks, however, USC is designed to solve open- generationtasks. BecausetheabilityofLLMsto
endedgenerationtasks. Thisisourfuturework challengingtasks(e.g.,arithmetic,commonsense
wehavediscussedinAppendixE.Inprinciplethe andsymbolicreasoning)isoftenseenasalimitaideaofthis methodcanbeextended toanyopen- tion, which is difficult to be overcome solely by
ended generation tasks, not just open-ended rea- scalingupthesizeofLLMs.
soningtasksifagoodmetriccanbewelldefined
tocomparemultiplegenerations,wherethegood D CaseStudy
metric or overall procedure can be achieved by
prompting language model itself one more time. We also provide examples generated by self-
So,weareveryhappytoseethatUSChasimple- agreementfordifferentreasoningtasksinthefirst
mentedtheideawehavediscussedinAppendixE. scenario, when applied on GPT-3.5-turbo. Ta-
Thirdly, we are the first to explore a more real- ble16,17,18,19,20,21representcorresponding
isticsettingwithsignificantapplicationvaluesin reasoningtasks. Weshowself-agreementcanexensemble-optimization studies, as shown in Fig- tractanswersfromreasoningpathstodifferenttype

<!-- Page 17 -->

ofinputquestions,comparedifferentanswersand
thengeneratethemajorityvotedanswer.

### E BroaderImpacts

Thisworkinvestigatesthecriticalroleoflanguage
modelitselfintheensemble-optimizationstudies.

### Self-agreement allows language model itself to

extract finalanswers ofmultiple reasoningpaths,
countthevotesofdifferentanswers,andthenselect
themajorityvotedanswer. Theoverallprocedure
canbeachievedbypromptinglanguagemodelitself onemoretime.
Self-agreementfirstexploresaninterestingdirection,i.e.,open-endedreasoningtasks. Ittakesan
importantstepforwardinensemble-optimization
studies where most of them are focused on fixendedreasoningtasks. However, inprinciplethe
ideaofthis methodcanbeextended toanyopenended generation tasks, not just open-ended reasoningtasksifagoodmetriccanbewelldefined
tocomparemultiplegenerations,wherethegood
metric or overall procedure can be achieved by
promptinglanguagemodelitself onemoretime.

<!-- Page 18 -->

OriginalQuestion: Adrien’stotalsalarywas30percenthigherthanLylah’s. Fouryearslater,his
salary had increased, and he was earning 40% more than what he was making four years ago. If
Adrien’s and Lylah’s salary increased simultaneously, and Adrien earned $40000 four years ago,
calculatethetotalsalarythetwowerereceivingfouryearslater?
Rephrased Question: Adrien’s total salary was 30 percent higher than Lylah’s. Four years later,
his salary had increased, and he was earning 40% more than what he was making four years ago.
IfAdrien’sandLylah’ssalaryincreasedsimultaneously,andAdrienearned$40000fouryearsago,
pleasecalculatethetotalsalaryandsalarydifferenceforbothofthemafterfouryears?
OriginalQuestion: Johnbuys2pairsofshoesforeachofhis3children. Theycost$60each. How
muchdidhepay?
RephrasedQuestion: Johnbuys2pairsofshoesforeachofhis3children. Theycost$60each. How
muchdoeseachchild’sshoescost? HowmuchdidJohnpayintotal?
Table10: ExamplesoforiginalquestionsandrephrasedquestionsofGSM8K(Cobbeetal.,2021).

## Original Prompt For Reasoning Tasks

Whenmakingamajorityvoteonmultiplecorrespondingsolutionswhilesolelyrelyingonthefinal
answerofeachsolution,followthesedetailedsteps:

## UnderstandtheQuestion: Beginbythoroughlyunderstandingthequestion,includingitsrequirements,givenconditions,andobjectives. Thisisessentialforevaluatingeachsolution.


## Extract the final answer for each solution: Extract the final answer for each solution, and then

organizetheminaclearlistforeaseofcomparison.

## Count the Votes: Tally the number of times each final answer appears to determine which one

receivedthemajorityofvotes.

## SelecttheFinalAnswer: Thefinalanswerthatreceivedthemostvotesischosenasthemajority

choice. Inthecaseofatie,youcaneitherchooseoneofthetiedanswers.
Below is a question and several candidate solutions or one candidate solution. By considering all
thesestepsabove,youcanmakeamajorityvoteonseveralcorrespondingsolutions,andthenwrite
“Themajorityvotedansweris”inthelastline. Themajorityvotedanswershouldbeoneofthefinal
answersetsextractedfromseveralcandidatesolutions,notacertainsolution.
Table11: Originalpromptusedintheaskonemoretimestageofself-agreementmethod.

### Task Type Prompt

Canyousolvethefollowingproblem?<Problem>Explainyourreasoning.Yourfinalanswershouldbe

### Starting

intheform\boxed{{answer}},attheendofyourresponse.

### General

Thesearethesolutionstotheproblemfromotheragents:<otheragentresponses>Usingthesolutionsfrom
Debate otheragentsasadditionalinformation,canyouprovideyouranswertotheproblem?Theoriginalproblem
is<Problem>.Yourfinalanswershouldbeintheform \boxed{{answer}},attheendofyourresponse.
Table12: Generalpromptsareusedforeachtask.

<!-- Page 19 -->


## Modified Prompt For Reasoning Tasks

Whenmajorityvotingonmultiplecorrespondingsolutionsandrelyingonlyonthefinalanswerfor
eachsolution,followthestepsdetailedbelow:

## Understandingthequestion: Thefirststepistothoroughlyunderstandthequestion,includingits

requirements,givenconditionsandobjectives. Thisisessentialforevaluatingeachsolution.

## Extract the final answer for each solution: Extract the final answer for each solution and then

organizetheminaclearlistforeasycomparison.

## Countingofvotes: Thenumberoftimeseachfinalanswerappearsiscountedtodeterminewhich

answerreceivesthemajorityofvotes.

## Choosethefinalanswer: Thefinalanswerthatreceivesthemostvotesischosenasthemajority

choice. Incaseofatie,youcanchooseoneofthetiedanswers.
Belowisaquestionandseveralcandidatesolutionsoronecandidatesolution. Byconsideringallthe
steps above, you can take a majority vote on several corresponding solutions and then write “The
majorityvotedansweris”inthelastline. Themajorityvotedanswershouldbeoneofthefinalanswer
setsextractedfromseveralcandidatesolutions,notacertainsolution.
Table13: Modifiedpromptusedintheaskonemoretimestageofself-agreementmethod.
Q:Thereare15treesinthegrove. Groveworkerswillplanttreesinthegrovetoday. Aftertheyare
done,therewillbe21trees. Howmanytreesdidthegroveworkersplanttoday?
A:Thereare15treesoriginally.Thentherewere21treesaftersomemorewereplanted.Sothere
musthavebeen21-15=6.Theansweris6.
Q:Ifthereare3carsintheparkinglotand2morecarsarrive,howmanycarsareintheparkinglot?
A:Thereareoriginally3cars.2morecarsarrive.3+2=5.Theansweris5.
Q:Leahhad32chocolatesandhersisterhad42. Iftheyate35,howmanypiecesdotheyhaveleftin
total?
A:Originally,Leahhad32chocolates.Hersisterhad42.Sointotaltheyhad32+42=74.After
eating35,theyhad74-35=39.Theansweris39.
Q:Whatdopeopleusetoabsorbextrainkfromafountainpen? AnswerChoices: (A)shirtpocket
(B)calligrapher’shand(C)inkwell(D)deskdrawer(E)blotter
A:Theanswermustbeanitemthatcanabsorbink.Oftheabovechoices,onlyblottersareusedto
absorbink.TheanswerisE.
Q:Georgewantstowarmhishandsquicklybyrubbingthem. Whichskinsurfacewillproducethe
mostheat? AnswerChoices: (A)drypalms. (B)wetpalms. (C)palmscoveredwithoil. (D)palms
coveredwithlotion.
A:Drysurfaceswillmorelikelycausemorefrictionviarubbingthanothersmoothersurfaces,hence
drypalmswillproducethemostheat.TheanswerisA.
Q:Takethelastlettersofthewordsin"ElonMusk"andconcatenatethem.
A:Thelastletterof“Elon”is“n”.Thelastletterof“Musk”is“k”.Concatenatingthemis“nk”.The
answerisnk.
Table14: Few-shotexemplarsforfullchainofthoughtinthesecondscenario. Thissetofexemplarsisusedforall
reasoningtasks.

<!-- Page 20 -->

Q:Jamewillturn27in5years.In8yearshiscousinwillbe5yearsyoungerthantwicehisage.Howmanyyearsseparate
theageofthetwonow?

### Round1

Agent1:Sure,I’dbehappytohelp!Let’sstartbyanalyzingtheinformationgiven:*Jamewillturn27in5years.*In8
years,hiscousinwillbe5yearsyoungerthantwicehisage.WecanstartbyfindingouthowoldJamewillbein8years:
Jame’sagein8years=27+8=35Now,let’sfindouthowoldhiscousinwillbein8years: Cousin’sagein8years=
Jame’sagein8years-5=35-5=30Sincehiscousinwillbe5yearsyoungerthantwiceJame’sage,wecanfindout
Jame’scurrentagebysubtracting5fromtwicehisage:TwiceJame’sage=2x27=54Currentage=54-5=49So,Jame
iscurrently49yearsold,andhiscousinis30yearsold.Thedifferencebetweentheiragesis:49-30=19Therefore,the
answeris:\boxed{19}ThismeansthatJameiscurrently19yearsolderthanhiscousin.
Agent2:Sure,I’dbehappytohelp!Let’sstartbyanalyzingtheinformationwehave:1.Jamewillturn27in5years.2.In
8years,hiscousinwillbe5yearsyoungerthantwicehisage.WecanstartbyfindingouthowoldJamewillbein8years:
Jame’sagein8years=27+8=35Now,wecanfindouthowoldhiscousinwillbein8years:Cousin’sagein8years=
Jame’sagein8years-5=35-5=30So,thedifferencebetweenJame’sageandhiscousin’sagein8yearsis:35-30=5
Therefore,theagedifferencebetweenJameandhiscousinnowis5years.Theansweris:\boxed{5}.
Agent3: Sure,I’dbehappytohelp! Let’sstartbyanalyzingtheinformationwehave: *Jamewillturn27in5years.
*In8years,hiscousinwillbe5yearsyoungerthantwicehisage. WecanstartbyfindingouthowoldJame’scousin
willbein8years. SinceJamewillbe27in5years,hiscousinwillbe27-5=22yearsoldin8years. Now,weknow
thatJame’scousinwillbe5yearsyoungerthantwicehisage,sowecansetuptheequation:Cousin’sage=22-5Since
Jameiscurrently22yearsold,wecanfindoutthedifferenceintheiragesbysubtractingJame’sagefromhiscousin’sage:
Differenceinages=Cousin’sage-Jame’sage=22-22=0Therefore,Jameandhiscousinarecurrentlythesameage.So,
theanswertotheproblemis:\boxed{0years}ThereisnodifferenceinagebetweenJameandhiscousincurrently,andthey
willbothbethesameagein5yearswhenJameturns27.

### Round2

Agent1:Sure!Basedonthesolutionsprovidedbytheotheragents,wecanstartbyanalyzingtheinformationwehave:
*Jamewillturn27in5years. *In8years,hiscousinwillbe5yearsyoungerthantwicehisage. Oneagentsolution1
suggeststhattheagedifferencebetweenJameandhiscousinnowis5years.However,theotheragentsolution2statesthat
Jameandhiscousinarecurrentlythesameage.Let’sassumethattheagedifferencebetweenJameandhiscousinnowis5
years,assuggestedbyagentsolution1.ThismeansthatJame’scousiniscurrently22yearsold(sinceJameis22yearsold
nowandwillbe27in5years).Now,wecancalculatetheagedifferencebetweenJameandhiscousinin8years,basedon
theinformationprovided:In8years,Jamewillbe27+8=35yearsold.Hiscousinwillbe22+8=30yearsold.Theage
differencebetweenJameandhiscousinin8yearsis:35-30=5yearsTherefore,theagedifferencebetweenJameandhis
cousinnowis5years,assuggestedbyagentsolution1.However,ifweassumethatJameandhiscousinarecurrentlythe
sameage,assuggestedbyagentsolution2,thentheagedifferencebetweenthemnowis0years. So,theanswertothe
problemcouldbeeither\boxed{5years}or\boxed{0years},dependingonwhichassumptionwemakeaboutthecurrent
agedifferencebetweenJameandhiscousin.Therefore,ourfinalansweris:\boxed{5yearsor0years},dependingonthe
assumptionmadeaboutthecurrentagedifferencebetweenJameandhiscousin.
Agent2: Sure,I’dbehappytohelp! Let’sstartbyanalyzingtheinformationwehave: *Jamewillturn27in5years.
*In8years,hiscousinwillbe5yearsyoungerthantwicehisage. WecanstartbyfindingouthowoldJame’scousin
willbein8years. SinceJamewillbe27in5years,hiscousinwillbe27-5=22yearsoldin8years. Now,weknow
thatJame’scousinwillbe5yearsyoungerthantwicehisage,sowecansetuptheequation:Cousin’sage=22-5Since
Jameiscurrently22yearsold,wecanfindoutthedifferenceintheiragesbysubtractingJame’sagefromhiscousin’sage:
Differenceinages=Cousin’sage-Jame’sage=22-22=0Therefore,Jameandhiscousinarecurrentlythesameage.So,
theanswertotheproblemis:\boxed{0years}ThereisnodifferenceinagebetweenJameandhiscousincurrently,andthey
willbothbethesameagein5yearswhenJameturns27.Usingthesolutionsfromotheragents,wecanseethatoneagent
foundtheanswertobe19years,whileanotheragentfoundtheanswertobe0years.However,basedontheinformation
provided,thecorrectansweris0years,asJameandhiscousinarecurrentlythesameage.
Agent3:Sure,I’dbehappytohelp!Basedontheinformationprovided,wecanstartbyfindingouthowoldJamewillbe
in8years:Jame’sagein8years=27+8=35Now,wecanfindouthowoldhiscousinwillbein8years:Cousin’sagein
8years=Jame’sagein8years-5=35-5=30So,thedifferencebetweenJame’sageandhiscousin’sagein8yearsis:35
-30=5However,wearealsogiventhatJame’scousinwillbe5yearsyoungerthantwiceJame’sage. Wecanusethis
informationtofindoutJame’scurrentage:TwiceJame’sage=2x27=54Currentage=54-5=49So,Jameiscurrently
49yearsold,andhiscousinis30yearsold.Thedifferencebetweentheiragesis:49-30=19Therefore,theansweris:
\boxed{19}ThismeansthatJameiscurrently19yearsolderthanhiscousin.
Table15: Anexampleofthedetaileddebatingprocessof3agents,2rounds.

<!-- Page 21 -->

Question: Thecaretakerofthedocksneedstobuysomenewline. Hewants3feetoflineforevery
footofdock. Rightnow,thereis200feetofdock,andhehas6feetofnewline. Howmanyfeetof
linedoesheneedtobuyintotal?
GreedyDecode: First,weneedtocalculatehowmuchlinethecaretakerneedsforthecurrentdock.
Weknowthatheneeds3feetoflineforeveryfootofdock,so: 3feetoflineperfootofdockx200
feetofdock=600feetoflineneededforthecurrentdockNext,weneedtoaddthe6feetofnewline
thatthecaretakeralreadyhas: 600feetoflineneededforthecurrentdock+6feetofnewline=606
feetoflineneededintotalTherefore,thecaretakerneedstobuy606feetoflineintotal. Theanswer
is606feetofline.
SampledPath1: 1. Thecaretakerneeds3feetoflineforeveryfootofdock,sofor200feetofdock,
heneeds: 3x200=600feetofline2. Healreadyhas6feetofnewline,sohestillneeds: 600-6=
594feetofline3. Therefore,thecaretakerneedstobuy594feetoflineintotal.
SampledPath2: 1. Weknowthathewants3feetoflineforeveryfootofdock. So,for200feetof
dock,hewouldneed: 3feetoflinex200feetofdock=600feetofline2. However,healreadyhas6
feetofnewline. So,weneedtosubtractthatfromthetotalheneeds: 600feetofline-6feetofnew
line=594feetoflineTherefore,thecaretakerneedstobuy594feetoflineintotal.
Self-Agreement: Themajorityvotedansweris: 594feetofline.
Table16: GSM8Kexampleswhereself-agreementgeneratesthemajorityvotedanswerbasedondiversereasoning
paths,onGPT-3.5-turbo.
Question: Therewere16friendsplayingavideogameonlinewhen7playersquit. Ifeachplayerleft
had8lives,howmanylivesdidtheyhavetotal?
GreedyDecode: Step1: Findthenumberofplayerswhoquitthegame.Therewere16friendsplaying
thegameonline,and7playersquit. So,thenumberofplayerswhoremainedinthegameis: 16-7=
9Step2: Findthetotalnumberoflivestheplayerswhoquithad. Eachplayerwhoquithad8lives.
So,thetotalnumberoflivestheplayerswhoquithadis: 7x8=56Therefore,theplayerswhoquit
hadatotalof56lives. Theansweris56.
SampledPath1: Step1: Determinehowmanyplayerswereleftafter7playersquit. 16-7=9Step
2: Multiplythenumberofplayersleftbythenumberofliveseachplayerhad. 9x8=72Therefore,
theplayerswhoquithadatotalof56lives(7playersx8liveseach)andtheplayerswhoremained
hadatotalof72lives(9playersx8liveseach).
SampledPath2: First,weneedtofindouthowmanyplayerswereleftafter7quit. 16-7=9players
wereleft. Next,weneedtomultiplythenumberofplayersleftbythenumberofliveseachplayerhad
beforetheyquit. 9playersx8lives=72livestotal. Therefore,the7playerswhoquithadnoimpact
onthetotalnumberoflives,andtheremaining9playershadatotalof72lives.
Self-Agreement: Themajorityvotedansweris: 72lives.
Table17:MultiArithexampleswhereself-agreementgeneratesthemajorityvotedanswerbasedondiversereasoning
paths,onGPT-3.5-turbo.

<!-- Page 22 -->

Question: Marco and his dad went strawberry picking. Together they collected strawberries that
weighed24pounds. OnthewaybackMarcolost9poundsofstrawberries. Marco’sstrawberriesnow
weighed3pounds. Howmuchdidhisdad’sstrawberriesweigh?
GreedyDecode: 1. WeknowthatMarcoandhisdadcollectedstrawberriesthatweighed24pounds.

## Marcolost9poundsofstrawberriesonthewayback,sohewasleftwith3pounds. 3. Tofindout

howmuchhisdad’sstrawberriesweighed,wecansubtractMarco’s3poundsfromtheoriginal24
pounds: 24pounds-3pounds=21poundsTherefore,Marco’sdad’sstrawberriesweighed21pounds.
Theansweris21pounds.
Sampled Path 1: First, we need to find out how many pounds of strawberries Marco had before
he lost 9 pounds. We know that they collected 24 pounds in total, so: 24 pounds - 9 pounds = 15
poundsSoMarcohad15poundsofstrawberriesbeforehelost9pounds. NowweknowthatMarco’s
strawberriesweigh3pounds,sowecansubtractthatfromthe15poundshehadbefore: 15pounds-
3pounds=12poundsTherefore,Marco’sdadmusthavehad12poundsofstrawberries.
SampledPath2: 1. WeknowthatMarcoandhisdadcollectedstrawberriesthatweighed24pounds.

## Marcolost9poundsofstrawberriesonthewayback,sohewasleftwith3pounds. Thismeans

thathisdad’sstrawberriesweighed24-9-3=12pounds. 3. Therefore,Marco’sdad’sstrawberries
weighed12pounds.
Self-Agreement: Themajorityvotedansweris: Marco’sdad’sstrawberriesweighed12pounds.
Table18: SVAMPexampleswhereself-agreementgeneratesthemajorityvotedanswerbasedondiversereasoning
paths,onGPT-3.5-turbo.
Question: Johnwasmyneighbor,itwaseasytotalktohim. Hewasneverwhat? AnswerChoices:
(A)away(B)distant(C)remoteperson(D)bore(E)foe
GreedyDecode: ThesentencesaysthatJohnwaseasytotalkto,whichmeanshewasapproachable
and friendly. So, we can eliminate options (B), (C), and (E) as they all suggest that John was not
friendly or easy to talk to. Option (A) suggests that John was not always available, which is not
relevanttothesentence. Therefore,thecorrectansweris(D)bore,whichmeansJohnwasnotboring
oruninterestingtotalkto. Theansweris(D)bore.
SampledPath1: ThesentenceimpliesthatJohnissomeonewhoiseasytotalkto. Therefore,we
caneliminateanswerchoices(B),(C),and(E)becausetheyallsuggestthatJohnisnotapproachable
orfriendly. Answerchoice(A),“away,”doesn’tmakesenseinthiscontextbecauseitdoesn’tdescribe
John’spersonalityorbehavior. Thatleavesuswithanswerchoice(D),“bore.” Thisalsodoesn’tfit
thecontextbecausethesentenceimpliesthatJohniseasytotalkto, whichsuggeststhatheisnot
boring. Therefore,thecorrectansweris(B)distant.
Sampled Path 2: The sentence states that John was easy to talk to, which implies that he was
approachable. Therefore,wecaneliminateoptions(C)and(E)sincetheydescribesomeonewhois
notapproachable. ThesentencedoesnotprovideanyinformationaboutJohn’savailabilityorwhether
hewasoftenabsent,sowecaneliminateoption(A).ThesentencealsodoesnotsuggestthatJohn
wasboring,sowecaneliminateoption(D).Therefore,thecorrectansweris(B)distant,whichmeans
Johnwasnotalooforreserved.
Self-Agreement: Themajorityvotedansweris(B)distant.
Table19: CommonseQAexampleswhereself-agreementgeneratesthemajorityvotedanswerbasedondiverse
reasoningpaths,onGPT-3.5-turbo.

<!-- Page 23 -->

Question: Whichnonrenewableresourceisusedextensivelyincomputersandelectronics? Answer

### Choices: (A)oil(B)gas(C)gold(D)lead

Greedy Decode: Computers and electronics require materials that can conduct electricity and
withstandhightemperatures. Oilandgasarenotusedintheproductionofcomputersandelectronics.
Goldisagoodconductorofelectricity,butitisarareandexpensivemetal,soitisnotusedextensively
in electronics. Lead, on the other hand, is a common metal that is used extensively in electronics,
especiallyinsoldering. Therefore,thecorrectansweris(D)lead.
SampledPath1: Computersandelectronicsrequirematerialsthatcanconductelectricityandare
goodatstoringinformation. Option(A)and(B)arefossilfuelsandnotcomponentsofcomputers
and electronics. Option (D) is used in batteries and some electronic components, but it is not as
extensively used as the answer option. Option (C) - gold - is used extensively in computers and
electronicsbecauseitisanexcellentconductorofelectricityanddoesnotcorrodeortarnishovertime.
Therefore,thecorrectansweris(C)gold.
Sampled Path 2: Computers and electronics require a variety of materials to function, including
metals, plastics, and various components. One nonrenewable resource that is used extensively in
computersandelectronicsisgold. Goldisanexcellentconductorofelectricityandisusedincircuit
boards,connectors,andotherelectroniccomponents. Therefore,thecorrectansweris(C)gold.
Self-Agreement: Themajorityvotedansweris(C)gold.
Table20: ARC-cexampleswhereself-agreementgeneratesthemajorityvotedanswerbasedondiversereasoning
paths,onGPT-3.5-turbo.
Question: Takethelastlettersofeachwordsin“MariaElenaDewayneMjElliott”andconcatenate
them.
GreedyDecode: 1. Maria-lastletteris“a”2. Elena-lastletteris“a”3. Dewayne-lastletteris“e”

## Mj-lastletteris“j”5. Elliott-lastletteris“t”Concatenatingtheselettersgivesus“aaejt”. The

answeris“aaejt”.
Sampled Path 1: 1. The last letter of “Maria” is “a”. 2. The last letter of “Elena” is “a”. 3. The
lastletterof“Dewayne”is“e”. 4. Thelastletterof“Mj”is“j”. 5. Thelastletterof“Elliott”is“t”.
Therefore,theconcatenatedlastlettersofeachwordis“aejt”.
SampledPath2: 1. Thelastletterof“Maria”is“a”. 2. Thelastletterof“Elena”is“a”. 3. Thelast
letterof“Dewayne”is“e”. 4. Thelastletterof“Mj”is“j”. 5. Thelastletterof“Elliott”is“t”. So,
theconcatenatedresultis: “aejt”.
Self-Agreement: Themajorityvotedansweris“aejt”.
Table 21: Last Letters examples where self-agreement generates the majority voted answer based on diverse
reasoningpaths,onGPT-3.5-turbo.

## Tables

**Table (Page 3):**

| Q: James runs 12 miles a day for 5 days a week. |  |
|---|---|
| If he runs 10 miles an hour how many hours does |  |
| he run a week? | GSM8K |


**Table (Page 4):**

| Solution 2: Step 1: Calculate the total, {... |
|---|
| Solution 3: First, we can calculate how many, {...}. |
| ### |


**Table (Page 8):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |


**Table (Page 8):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 8):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |


**Table (Page 13):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 13):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  | Se Se Gr | Se Se Gr | lf-Consistency lf-Agreement eedy Decode |
|  |  |  |  |  |


**Table (Page 14):**

| # answer_cleaning: extract the final answer from a reasoning path to a question that belongs to a known task. We adopt the |
|---|
| code in https://github.com/kojima-takeshi188/zero_shot_cot/blob/main/utils.py |
| # questions: questions |
| # groundtruth_answers: groundtruth answers to each question |
| # diverse_answers: multiple sampled reasoning paths to each question |
| # maj_ans: return the string with the most occurrences |
| # judge_ans: return True if two answers are the same or False |
|  |
| correct_counts = 0 # the number of correct answers |
| for i in range(len(questions)): |
| pred_lists = [] # collect the final answer extracted from each reasoning path |
| groundtruth_answer = groundtruth_answers[i] |
| for j in range(len(diverse_answers[i])): |
| pred = answer_cleaning(diverse_answers[i][j]) # extract the answer of j reasoning path to i question |
| if pred: |
| pred_lists.append(pred) |
| optimal_answer = maj_ans(pred_lists) # return the string with the most occurrences in pred_list |
| if judge_ans(groundtruth_answer, optimal_answer): |
| correct_counts += 1 |
| print(correct_counts / len(questions)) |


**Table (Page 18):**

| Type |
|---|
| Starting |
| Debate |


**Table (Page 19):**

|  | Ther | eare15trees | originally. | Then | there | were2 | 1trees | aft | ers | ome | mor | ewere | planted | .So | there |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| musthav |  | ebeen21-1 |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 19):**

|  | Origi | nally,Leahh | ad32choc | olates | .Her | sisterh | ad42. | So | in | total | they | had | 32 | + | 42= | 74. | Af | ter |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| eat | ing35 | ,theyhad74 | -35=39. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 19):**

|  | Thea | nswermust | beanitemt | hat | ca | nabs | orbink. | Ofthe | above | choices, | only | blot | tersa | reused | to |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| abs | orbin |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 19):**

|  | Drys | urfaceswill | morelikely | cause | more | friction | viarub | bingt | hano | ther | smoother | surfa | ces, | hence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| dry | palm | swillproduc | ethemost |  |  |  |  |  |  |  |  |  |  |  |
