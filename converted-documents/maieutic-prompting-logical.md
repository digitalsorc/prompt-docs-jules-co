---
title: "Maieutic Prompting Logical"
original_file: "./Maieutic_Prompting_Logical.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "evaluation"]
keywords: ["true", "integral", "prompting", "maieutic", "page", "false", "you", "table", "answer", "model"]
summary: "<!-- Page 1 -->

Maieutic Prompting: Logically Consistent Reasoning with

### Recursive Explanations

JaehunJung LianhuiQin SeanWelleck
† † †‡
FaezeBrahman ChandraBhagavatula RonanLeBras YejinChoi
†‡ ‡ ‡ †‡
PaulG.AllenSchoolofComputerScience&Engineering,UniversityofWashington
†
AllenInstituteforArtificialIntelligence
‡
hoony123@cs.washington.edu

### Abstract Explanation-based Prompting


### Q: Captain Kirk is part of Star Wars? Pre-trained language models (LMs) struggle Input A: Captain Kirk i"
related_documents: []
---

# Maieutic Prompting Logical

<!-- Page 1 -->

Maieutic Prompting: Logically Consistent Reasoning with

### Recursive Explanations

JaehunJung LianhuiQin SeanWelleck
† † †‡
FaezeBrahman ChandraBhagavatula RonanLeBras YejinChoi
†‡ ‡ ‡ †‡
PaulG.AllenSchoolofComputerScience&Engineering,UniversityofWashington
†
AllenInstituteforArtificialIntelligence
‡
hoony123@cs.washington.edu

### Abstract Explanation-based Prompting


### Q: Captain Kirk is part of Star Wars?

Pre-trained language models (LMs) struggle Input A: Captain Kirk is a character in Star Trek. Therefore, the answer is False.

### Prompt …

withconsistentreasoning;recently,prompting Q: At least one mayor is not male?
LMs to generate explanations that self-guide Output A: There are female mayors. Therefore, the answer is True.
the inference has emerged as a promising di- Type I Smoke is not the source of fire?
rection to amend this. However, these ap- (41%) Smoke is a result of fire. Therefore, the statement is False.
proaches are fundamentally bounded by the One is a number that comes before zero?
???
Type II One is ... Therefore, the statement is True.
correctnessofexplanations,whichthemselves
(33%) One is a number that comes after zero?
areoftennoisyandinconsistent. Inthiswork, One is ... Therefore, the statement is True.
we develop MAIEUTIC PROMPTING, which Butterflies fly with 3 wings?
Type III Butterflies have 4 wings. Therefore, the statement is False.
aims to infer a correct answer to a question
(35%) Butterflies have 4 wings?
even from the unreliable generations of LM. Butterflies have 2 wings on each side of their body. Therefore,
the statement is False.
MAIEUTIC PROMPTING induces a tree of explanations abductively (e.g. X is true, be-
Figure 1: Logical errors in explanation-based promptcause...) andrecursively,thenframestheining: (1) explanation does not logically lead to the anference as a satisfiability problem over these
swer, (2) model is invariant to negation, and (3) falsiexplanations and their logical relations. We
fiesitsownexplanation. Weprompt175BGPT-3with
testMAIEUTIC PROMPTINGfortrue/falseQA
100questionssampledfromTalmoretal.(2021).
on three challenging benchmarks that require
complex commonsense reasoning. MAIEU-
lem(Weietal.,2022),ortheintermediatestepsof
TIC PROMPTING achieves up to 20% better
programexecution(Nyeetal.,2021a).
accuracythanstate-of-the-artpromptingmethods,andasafullyunsupervisedapproach,per- Explanation-basedpromptingisintuitivelymoforms competitively with supervised models. tivated by the reasoning steps humans typically
WealsoshowthatMAIEUTICPROMPTINGimemploy to solve a problem (Hausmann and Vanprovesrobustnessininferencewhileproviding
Lehn,2007). However,wefindthatthisintuition
interpretablerationales.1
isfaultyinpractice, asmodel-generatedexplanationsareoftenlogicallyinconsistentandunreliable.
1 Introduction

### Forexample,wemanuallyinspected100samples

Following the remarkable success of few-shot from a QA task (Figure 1) and found that for a
promptingoverlargelanguagemodels(e.g. Brown considerablenumberofcases,(1)theexplanation
et al., 2020), recent studies on prompting meth- doesnotlogicallyleadtotheinferredanswer,(2)
odssuggestthatLMs’reasoningcapabilitycanbe the model infers the same label for a statement
furtherpromotedbygeneratingasequenceofex- anditsnegation(KassnerandSchütze,2020),and
planation for a given problem, prior to inferring (3)falsifiesitsowngeneratedexplanation. These
the answer (Wei et al., 2022; Wang et al., 2022; findingsraisefundamentalquestionsontheroleof
Liuetal.,2021). Theso-calledexplanation-based explanations in LM inference: If the explanation
promptinghelpsanLMbetterelicititsknowledge is correct - is there a guarantee that the LM will
andreasonbyleveragingitsowngeneratedexpla- inferalabelconsistentwiththeexplanation? And
nations - whether it be commonsense knowledge iftheexplanationiswrong-isthereawaytomake
(Liuetal.,2021),asolutionforamathwordprob- useofeventhewrongexplanationininferringthe
correctanswer?
1We share our code at https://github.com/
jaehunjung1/Maieutic-Prompting. To this end, we propose MAIEUTIC PROMPT-
1266
Proceedingsofthe2022ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,pages1266–1279
December7-11,2022©2022AssociationforComputationalLinguistics

<!-- Page 2 -->

Q : War cannot have a tie? Width-wise spanning

## Q


### War cannot have a tie? True, because

In a context of war, there's always a victor and False, because True, because a loser. E E T F In a context of war, there's always a victor and False, because Logically Integral
a loser? False, because
There can be cases where the loser is not clear. E

## Tf

Logically Integral
Depth-wise
spanning
Max-SAT Solver

## Q

E Entail E w w ( ( E E F TF ): ) : 0 0 .9 .9 2 8 , E E T F : : F Tr a u ls e e T F w(E T→Q): 1.00, E TF : True
Contradict w(E F→¬Q): 1.00, Q : False

## E ...


## Tf


### Maieutic tree generation Defining the relations Inference

Figure2: Anoverviewof MAIEUTIC PROMPTING. GivenaquestionQ, wegeneratemaieutictreeconsistingof
abductive and recursive explanations, define the relations between them, and employ MAX-SAT to find the best
truth-valueassignmentstotheexplanationsandQ.
ING, a novel few-shot inference method that in- Ourexperimentsshowthattheperformanceof
fersacorrectanswerbyenumeratingastructureof MAIEUTICPROMPTINGexceedsthatofallthefewexplanations—possiblynoisyandcontradictory shotpromptingbaselines(e.g.,ChainofThought;
— and resolving them with a symbolic inference Wei et al., 2022) in three commonsense reasonalgorithm. Inspired by the maieutic method2 of ingandfactverificationbenchmarks. MAIEUTIC
Socrates,MAIEUTIC PROMPTINGinducestheLM PROMPTINGperformsupto20%betterthanother
togenerateabductiveexplanationsfordiversehy- promptingmethods,andperformsonparoreven
potheses with deep recursive reasoning, then col- better than supervised models. Further analyses
lectively eliminates the contradicting candidates, showthat MAIEUTIC PROMPTING isrobusttoperresultinginconsistentanswers. turbationsinboththequestionsandprompts,and
Figure 2 shows the overview of MAIEUTIC offersaninterpretableinterfacetounderstandthe
PROMPTING. First, we prompt the LM to abduc- rationalebehindthemodel’sinference.
tively (Peirce, 1974) rationalize both possible answers, True and False, rather than generating a 2 ProblemSetupandBackground
single explanation and then connecting it to one

### Our goal is to infer whether a given statement Q

of the answer choices. Moreover, we do not exmakessense,i.e. inferringthetruthvalueAofQ.
pect the 1-hop explanations to be always correct;
Conventionally,thiscanbedonethroughpromptthus,wefurthervalidatetheLM’sconfidenceinits
inganLMwiththefollowingtwomethods:
explanationsbyrecursivelypromptingthemodel
withitsowngenerationasthequestion. Ourgener- Standard Prompting Let Q be a statement we
ationprocessderivesatreestructureofgenerated wanttoinferthetruthvalueof(i.e.,eitherTrueor
propositions,whereonepropositionestablishesa False). Instandardfew-shotprompting,themodellogicalgroundforthecorrectnessofoneanother. inferredanswerAˆ isdefinedas:

### Toinfertheanswerfortheoriginalquestion,we

quantify the strength of the LM’s belief in each Aˆ= argmaxp LM (A | Q,C), (1)

## A T,F

∈{ }
propositionandthelogicalrelationshipsbetween
propositionsinthemaieutictree. Wethenemploy whereC = (q 1 ,a 1 ), ,(q k ,a k ) denotesthek
{ ··· }
the weighted MAX-SAT (Battiti, 2009) solver to examplesforin-contextlearning.
collectivelyinferthetruth-valuesofallthepropo-
Explanation-based Prompting In explanationsitions (including the original question) that best
based prompting, the inference process is factorsatisfythesetofobservedrelations. Thisway,we
izedintotwosteps:
symbolicallyinducethesubsetofgenerationsthat
makesthemostprobableandconsistentinference.
Our proposed method can run completely unsu- Aˆ= argmax p LM (A | Q,E,C)p LM (E | Q,C) (2)

## A

∈{

## T,F

}

## Ze

pervisedwithanyfew-shotpromptableLM(e.g.,
GPT-3;Brownetal.,2020). Here, E denotes the explanation generated
prior to inferring the answer label, and C =
2Maieutic method brings out definitions implicit in the (q ,e ,a ), ,(q ,e ,a ) includes k exam-
1 1 1 k k k
interlocutor’sbeliefs,... isamethodofhypothesiselimina- { ··· }
plesofquestions,explanationsandanswers. Since
tion,steadilyidentifyingandeliminatingthosethatleadto
contradictions(Vlastos,1991). marginalizingoverallE isintractable,priorworks
1267

<!-- Page 3 -->

resorttoasamplingbasedapproximation: 3.1 MaieuticTreeGeneration
3.1.1 AbductiveExplanationGeneration

### Aˆ= argmaxp (AQ,E,C),

LM | Given a question, we require the LM to post-hoc

## A T,F (3)

∈{ }
where E p LM (E Q,C) rationalize both True and False labels. This ab-
∼ |
ductiveexplanationgenerationhasseveraladvantagesoveranad-hocapproachthatfirstgenerates
3 MaieuticPrompting
anexplanation,thenpredictsthelabel. First,inthe
Inthissection,weintroduceMAIEUTIC PROMPT- ad-hoc setting, the model is required to generate
ING,whichperformsinferenceoveramaieutictree a discriminative explanation that helps in choosofgeneratedexplanations. First,weintroducelogi- ingonelabelovertheother. Abductivegeneration
calintegrity,akeyconceptthatisusedtodetermine (Bhagavatulaetal.,2019),onthecontrary,exposes
thereliabilityofpropositions. the model to consider different possible answers
Languagemodelsoftengeneratelogicallyincon- ratherthandiscriminatingone,whichoftenreveals
sistentpropositions;forinstance,inFigure1,the anexplanationthatotherwisewouldnothavebeen
modelinfersTruewhenpromptedwitheither“One generated. Second, the label information would
is a number that comes before zero.” or “One is intuitively help LM elicit more specific explanaa number that comes after zero.”. In this sense, tions, mitigating the issue of a bland and generic
p(True Q)doesnotprovideareliablevaluetode- generation which does not help the inference, a
|
termine whether Q is true or not. We formalize well-knownweaknessofLMs(Adiwardanaetal.,
this idea as logical integrity: a proposition Q is 2020).
logicallyintegralwhentheLMconsistentlyinfers Concretely, we define a function abduction
the truth value of Q and Q (i.e. Q as True and whichgetsthestatementQastheinputandoutputs
¬
QasFalse,orviceversa). Formally,wedefinea a tuple of two abductive explanations with True,
¬
booleanfunctionintegral(E)asfollows:3 Falsegivenastheanswer,respectively:
abduction(Q)=(E ,E )

## T F

1. argmaxp LM (AE,C)=T and (5)
A ∈{ T,F } | where E A ∈{ T,F } ∼ p LM (E | Q,A,C).
argmaxp (A E,C)=F

## Lm

A T,F |¬ Figure2showsaconcreteexampleofgenerating
∈{ }
2. argmaxp LM (A | E,C)=F and (4) E T given Q. With Q, we prompt the model to

## A T,F

∈{ } rationalizeTrueastheanswer: “Warcannothave
argmaxp (A E,C)=T
LM |¬ atie? True,because”,whichtheniscompletedby

## A T,F

∈{ }
anexplanationbyLM“Inacontextofwar,there’s
integral(E)=1 .
1or2issatisfied}
{ alwaysavictorandaloser.”.
Astatementisconsideredtobelogicallyintegral
3.1.2 Depth-wiseKnowledgeSpanning
/Truewhencondition1ismet,andlogicallyinte-

### AsshowninFigure1,LM-generatedexplanations

gral / False when condition 2 is met. Intuitively,
are noisy and inaccurate by nature. Prior works
the truth values of logically integral propositions
indirectly compensate for the untrustworthy genaremorecrediblethannon-integralones,towhich
erationsbyindependentlysamplingmultiplegen-
LMsareinconsistentgivenasimplenegation. For
erationsthenaggregatingthemattheanswerlevel
example,“Oneisanumberthatcomesbeforezero.”
(e.g. throughmajorityvoting;Wangetal.,2022).
inFigure1wouldnotbelogicallyintegral,asthe
Despite better performance, such an aggregation
modelassignssametruthvaluetobothQand Q.
¬ couldstillbebrittle,astheinferencefundamentally
For the rest of section, we first search for logdependsonthecorrectnessof1-hopexplanations.
ically integral propositions by constructing the
Toenhancetherobustnessofreasoning,wehymaieutictree(Section3.1),thenquantifytherelapothesizethattheinferenceprocessshouldentail
tionsbetweenthepropositions(Section3.2),based
notonlythebreadthofreasoning,butalsothedepth
onwhichweinferthefinalanswer(Section3.3).
of reasoning - whether the reasoning paths themselvesarecredibleandconsistentwitheachother.
3GivenE, Ecanbeautomaticallygeneratedsimplyby
¬ To do this, we require the LM itself to validate
insertingaprefix(e.g.Itiswrongtosaythat),orprompting
LMtonegatethegivensentence. itsowngenerations-byrecursivelypromptingthe
1268

<!-- Page 4 -->


## Q

Q : If you travel west far enough from the

### True, because False, because

west coast, you will reach the east cost?

## Q

True, because E T EF : You cannot reach the east True, because False, because
coast by going west?
i E n T a : n T y h e d i E re a c rt t h io i n s r lo o n u g nd e a n n o d u g if h y , o y u o t u r a w ve il l l False, because True, because E T E F
eventually return to where you started. EFT : You can reach the east coast False, because Logically Integral
integral(ET)= 1 by going west by traveling around True, because
the world.
EF :You cannot reach the integral(EFT)= 1 E

## Ft


## E


## Ff

e i a n st t c e o g a r s a t l by ( E g F o ) in = g w 0 est. EFF : If you travel in a specific Logically Integral
straight line, you will eventually
Depth 1 generation Depth 2 generation reach the other side. Prune non-integral Branch
integral(EFF)= 0
Figure3: Illustrativeexampleofmaieutictreegeneration,withthemaxtreedepthsetto2. Forvisualclarity,we
generateonly1E and1E perquestionandomitthewidth-wisespanningofknowledge.

## T F

LM with the generated explanations. As Figure prune the branches leading to leaf nodes that are
2 shows, this corresponds to a depth-wise span- stillnotlogicallyintegral. Thisway,thefinaltree
ningofknowledgethatinducesamaieutictree,a keepsonlythegenerationsthatleadtoalogically
multi-depthstructureofgeneratedpropositionsand integralproposition. Weprovideaformaldescriprelationsbetweenthem. tionofthegenerationprocessinAppendixA.
LetS denotethesetofnodesatdepthiinthe
i
3.2 DefiningtheRelations
maieutictree . EachnodeinS isanexplanation
i

## T

for an answer label (True or False), recursively Nowthatwehavegeneratedthemaieutictree,we
generatedgivenitsparentnodeasthequestion: seek to define the relations between propositions
andquantifytheirstrengthintoscalarweights. For

## S E ,E ,

i lT lF illustration,assumethatanLMhasgeneratedthe
⊆ { }
l ∈{ T[,F } i − 1 (6) followingE F forthegivenQ:
(E ,E )=abduction(E).
lT lF l

### Q:CaptainKirkispartofStarWars?

Notethat isafulltreewhentheequalityholds

### T A: False, because Captain Kirk is a

for all depths. For instance, in Figure 2, E is

## Tf

characterinStarTrek.
generated by prompting the LM with its parent
nodeE T andFalse,i.e. E TF p LM ( E T ,F,C). Thegenerationcanbelogicallyinterpretedasfol-
∼ ·|
In practice, we sample multiple explanations lows: (1) the LM believes that Captain Kirk is a
withthesameQandAthroughnucleussampling character in Star Trek, (2) the LM believes that
(Holtzman et al., 2019). This corresponds to the thepropositionCaptainKirkisacharacterinStar
width-wisespanningofknowledge,enhancingthe Trek canbeareasontodenythatCaptainKirkis
diversityandcoverageofgeneratedexplanations. part of Star Wars. Accordingly, we define belief
andconsistencytorepresentthetwodimensionsof
3.1.3 WhentoStopGenerating
thelogicalrelationship.
Generatingafulltreecouldbecomputationallyexpensive,asthenumberofgenerationgrowsexpo- Beliefw E correspondstotheLM’sbeliefthatthe
nentiallywiththemaximumtreedepth. Therefore, propositionE istrue(andtherefore, E isfalse).
¬
ineachbranch,westopgeneratingfurtheroncewe Toquantifybelief,weprompttheLMwithE and
reach a logically integral proposition; intuitively, E respectivelyasaquestion,thencomparingthe
¬
this aligns with our goal to identify propositions probabilityassignedtoTrue:
thatcanbevalidatedbytheLMwithconfidence.
p (T E,C) p (T E,C)
Figure3illustratesanexampleofmaieutictree w E := p LM (T | E,C)+ − p LM (T |¬ E,C) . (7)

## Lm Lm

| |¬
generation where the maximum depth of the tree
Notethatcalculatingthisdoesnotrequireanyadis set to 2. For visual clarity, we only generate
ditionalprompting,aswealreadygainedaccessto
one explanation per Q and A. Given Q, we first
thesevalueswhilecheckingforthelogicalintegrity
generate E and E , then validate whether each

## T F

ofeachproposition.
ofthemislogicallyintegral. SinceE islogically

## T

integral,westopgeneratinginthisbranch,butcon- Consistency w E,Q,A corresponds to the consistinue generating from E which is not logically tency of the generated E with the given Q and

## F

integral. After reaching the maximum depth, we A. Intuitively,iftheLMislogicallyconsistent,the
1269

<!-- Page 5 -->

likelihood of E being generated given an answer therelationshipsacrossbranches,e.g. E andE

## T F

(e.g., E beinggeneratedgivenFalse)shouldbe inFigure3. Thismotivatesustointroduceasmall

## F

largerthanitslikelihoodgiventheoppositeanswer NLI model as a verifier, which can infer the rela-
(e.g.,E beinggeneratedgivenTrue). Following tionship between an arbitrary pair of nodes in .

## F


## T

thisintuition,wecomputetheconsistencyas: Followingpreviousworks(MinerviniandRiedel,
2018;Wangetal.,2019),weconverttheNLIlabels
p (E Q,A,C)
w E,Q,A := p (E Q,A L , M C)+ | p (E Q, A,C) . (8) intologicalrelationsasfollowing:

## Lm Lm

| | ¬
3.3 Inference Entail(E 1 ,E 2 ):E 1 E 2
→ (13)
Contradict(E ,E ):E E .
Thetwotypesofrelationsformulateasetofunary 1 2 1 →¬ 2
andbinarylogicalconstraints,basedonwhichwe
Forallpairsofnodes(E ,E ) node( )2,E =
1 2 1
assignthetruthvaluestoallnodesinthemaieutic ∈ T 6
E ,weobtaineitherE E orE E ifE
2 1 2 1 2 1
tree ,andinconsequence,infertheanswertothe → → ¬
T entailsorcontradictsE 2 . ForNLI-basedclauses,
originalquestion. First,werepresent astheset
C blf wefixtheweightsto1.4 Whiletheobjectivefuncofunaryconstraints. ForeachleafnodeE in ,
T tion(Eq. 12)staysthesame, con isnowreplaced

## C

with , asetofclausesinducedbytheverifier

### E ifEislogicallyintegral/True C NLI

c blf = ( E ifEislogicallyintegral/False. (9) model.
¬
Notethatalltheleafnodesin arelogicallyinte- 4 Experiments

## T

gral,hencewecancountonthecredibilityofbelief

### Datasets We evaluate MAIEUTIC PROMPTING

forthesenodes. Wenowdefinethesetofallbelief
onthreecommonsensereasoningandfactverificaconstraints as:
blf

### C tionbenchmarksinbinaryQAformat: Com2Sense

blf = c blf for E leaf( ) . (10) (Singh et al., 2021), CSQA 2.0 (Talmor et al.,

## C { ∀ ∈ T }

2021), CREAK (Onoe et al., 2021). Despite the

### For example, the nodes E and E in Figure 2

F TF simple format, these datasets require a substanwouldhaveabeliefconstraintin .
blf tial amount of knowledge and robust reasoning,

## C


### Likewise,forconsistency,wedefine asthe

con makingthemchallengingevenforthebillion-scale

## C

setofbinaryconstraintsusinglogicalimplication.
fine-tunedLMs(Table1).
Foreachedge(E ,E )in ,
l lA

## T


### Baselines Wecompareourmethodwithboththe

c con = ( E E l l A A → →¬ E E l l i i f f A A = = T F r a u ls e e (11) f e e ls w . -s A ho lo t n p g ro w m i p th tin t g he m s e t t a h n o d d a s rd an p d ro su m p p e t r i v n i g s , ed w m e o in d - -
Ccon = { c con for ∀ (E l ,E lA ) ∈ edge( T ) } . clude Chain of Thought (Wei et al., 2022), Self-
Consistency (Wang et al., 2022) and Generated

### OurobjectiveistoassignthetruthvaluesforallEs

Knowledge Prompting (GKP) (Liu et al., 2021).
andtherootnodeQin ,suchthatwemaximize
T Forsupervisedmodels,weconsiderthestrongbasew 1 , lines used for the respective dataset, such as T5
c · { c=True } (12)
c ∈CXblf∪Ccon (Raffel et al., 2020), UnifiedQA (Khashabi et al.,
2020)andUnicorn(Lourieetal.,2021).
whichsumsuptheweightsofsatisfiedconstraints.

### Thisproblemisnaturallyformulatedasweighted

Configuration Details For all prompting meth-

### MAX-SAT, which is a problem of determining

ods,weusethesamesetof6demonstrationexamtruthvaluesofvariablesthatmaximizetheweight
plesandthesameversionofGPT-3(text-davinciofsatisfiedclauses. Theproblemcanbealgorith-
001)astheLM.Wedeterminethehyperparameters
micallysolvedusinganoff-the-shelfsolver.
of MAIEUTIC PROMPTING and baselines based
3.4 VerifierModel on the dev set performance on the benchmarks.

### Inmaieutictreegeneration,wesetthemaximum

OnelimitationoftheconsistencydefinitioninSecdepthto2. Fordepth1,weusenucleussampling
tion 3.2 is that it only considers the relationship
(p = 1.0)(Holtzmanetal.,2019)togenerate3E s
betweenaparentnodeandachildnode. Sincethe T
definitionbuildsuponthelikelihoodofeachgen-
4WealsotriedusingthelabelprobabilityassignedbyNLI
erationfromanLM,wecannottakeintoaccount modelasweight,butfixingitto1yieldedbetterresults.
1270

<!-- Page 6 -->


### Dataset Com2Sense CSQA2.0 CREAK

Model dev test pairwise dev test dev test contrast
desivrepuS
RoBERTa-large(Liuetal.,2019) 62.8 59.4 33.3 - - 80.6 80.3 61.5
T5-large(Raffeletal.,2020) 62.8 60.6 41.8 53.8 54.6 - - -

### T5-3B(Raffeletal.,2020) 73.2 - - - 60.2 85.6 85.1 70.0

UnifiedQA-3B(Khashabietal.,2020) 75.1 71.3 51.3 - - - - -
T5-11B(Raffeletal.,2020) 77.2 - - 68.5 67.8 89.5 - 75.2
Unicorn-11B(Lourieetal.,2021) - - - 69.9 70.2 - - -
gnitpmorP

### Standard 58.1 - - 54.1 - 60.3 - 55.2


### ChainofThought(Weietal.,2022) 61.6 - - 59.6 - 64.8 - 59.4

SelfConsistency(Wangetal.,2022) 61.4 - - 60.8 - 70.5 - 64.8

### GKP(Liuetal.,2021) 61.8 - - 59.7 - 75.4 - 68.2

MAIEUTICPROMPTING(Ours) 72.5 75.0 68.7 69.5 68.3 85.2 85.3 77.4
Table1: ExperimentalresultsofMAIEUTIC PROMPTINGandbaselinemethodsonthreebenchmarkdatasets. We
differentiatesupervisedbaselines(uppersection)frompromptingmethods(lowersection),andboldthebestnumbers for each section. MAIEUTIC PROMPTING with GPT-3 outperforms all prompting baselines with the same
model,whilebeingcompetitiveagainstbillion-scalesupervisedLMs.
and3E sfromQ. Fordepth2,weusegreedyde- 80 Standard Chain of Thought
F Self Consistency Maieutic
75
codingtogenerate1E and1E fromeachparent

## T F

70
node. This constrains the generated tree to have
65
at most 18 nodes excluding the original Q.5 In
60 72.34 71.68

### Section4.3,weconductanablationstudyonthis

55 57.883 60.673 61.2 57.801 61.052 61.544
depth-adaptivedecodingschemeandanalyzethe
50

### Different examples Different orders

effect of the tree size. For the main experiments,
Figure4: RobustnessofpromptingmethodsunderdifweuseRoBERTa(Liuetal.,2019)fine-tunedon
ferent few-shot examples / different order of exam-
MNLI (Williams et al., 2018) as a verifier with
ples. Wecomparethemeanandstandarddeviationof
90.2%accuracyonMNLIdevset,andRC2(Mor-
Com2Sensedevsetaccuracy.
gadoetal.,2014)asaMAX-SATsolver.

### Correct - Perfect Correct - Mixed Correct - None

Incorrect - Perfect Incorrect - Mixed Incorrect - None
4.1 BenchmarkPerformance
provid1e00experiments on StrategyQA (Geva et al.,
2021),toevaluatethegeneralizabilityofMAIEU-
Table 1 presents overall evaluation results of 80
TIC PROMPTINGinmulti-hopsetting.
MAIEUTIC PROMPTINGalongwiththeprompting
60
andsupervisedbaselines. MAIEUTIC PROMPTING 4.2 RobustnessAnalysis
significantly outperforms all prompting methods 40

### Weperformadditionalanalysestounderstandthe

acrossallbenchmarks. Notably,GKPandSelfConworkin2g0 of our method under semantic perturbasistencyensembledmore1-hopexplanationsthan
tionsanddifferentpromptformats.
the maximal size of the maieutic tree; our supe- 0

### Grammatical Relevant Factual Helpful

riorperformancecomparedtothesemethodscon-
Robustnesstosemanticperturbations Inaddifirms the sample efficiency of depth-wise knowltiontothestandardaccuracy,wereporttwoaddiedge spanning. Moreover, MAIEUTIC PROMPT-
tional metrics called pairwise accuracy and con-
ING is the only prompting method that performs trastsetaccuracyinTable1. InCom2Sensetestset
better than even the smallest supervised baseline
andCREAKcontrastset, eachquestionispaired
(RoBERTa-large)inCom2SenseandCREAK.In
withitscomplimentarycounterpart,ofwhichthe
fact, MAIEUTIC PROMPTING allowsustousean
surfaceformissimilarbuttheanswershouldbethe
off-the-shelf LM to achieve comparable perforopposite(e.g. “BarackObamahasdaughters.” vs
mancetoalargefine-tunedLMbysimplyplugging
“BarackObamahasnodaughter.”),testingthemodinourinferencealgorithm. InAppendixCwealso
els’robustnesstosemanticperturbations. Inthese
5Both GKP and Self Consistency employ an ensemble metrics,thegapbetweenMAIEUTIC PROMPTING
strategy,generatingN differentsamplesofexplanationsthen andbaselineswidenssubstantially,indicatingthe
aggregatingtheiranswers.Forafaircomparisonwithours,we
robustnessofourmethodagainstsemanticpertursetN =20forbothmethods,generatingmoreexplanations
thanthemaximalpossiblesizeofthemaieutictree. bations.
1271

<!-- Page 7 -->

80
Standard Chain of Thought
Self Consistency Maieutic
75
70
65
72.34 71.68
60
55 60.673 61.2 61.052 61.544
57.883 57.801
50

### Different examples Different orders

Model Accuracy Set 1 - All Set 1 - Mixed Set 1 - None
Set 2 - All Set 2 - Mixed Set 2 - None
Non-abductivegeneration 68.4
100
Allgreedydecoding(nodepth-adaptive) 67.2 96.67 99.33 23.33 1 4 8 .6 .6 7 7 2 6 8 . . 6 6 7 7 14.67 13.34 34.00
Allnucleussampling(nodepth-adaptive) 72.0 80 42.67 22.00
Likelihood-basedconsistency 65.6
76.67 76.67

### MaieuticPrompting 72.5 60 64.67 64.67 42.67

Table 2: Ablation study on Com2Sense Dev set. The
40 42.67
bestconfigurationiswithabductivegeneration, depthadaptivedecodingandverifier-basedconsistency. 20 23.33
0
Grammatical Relevant Factual Helpful

### Dimension 1 2 3 5 10

Figure 5: Human evaluation results (Krippendorff’s

### Depth 61.3 72.5 72.4 - -

Width 62.4 66.5 72.5 71.5 72.1 alpha = 0.64; substantial inter-annotator agreement).
To minimize subjectivity, we use a strict 3-level scale,

### Table 3: Performance of MAIEUTIC PROMPTING on

where annotators choose All only when all the state-
Com2Sensewithdifferentmaieutictreesizes.
ments in the true Es are desirable (e.g. grammatical)
on its own, Mixed when at least one E is undesirable,
Robustness to different prompts Prior works andNoneotherwise.
revealedthatpromptingperformancecouldbesensitive to few-shot examples and their order (Lu Consistency We ablate the NLI-based clauses
et al., 2021b; Zhao et al., 2021). We investigate andreplacethemwiththeoriginalC con discussed
whether this holds true for MAIEUTIC PROMPT- inSection3.2. Withthelikelihood-basedC con ,the
ING,asshowninFigure4. Wecomparedifferent accuracy reduces by about 7%, but still prevails
promptingmethodsrunwith3differentsetsoffew- overthepromptingbaselinesinTable1. Theverishotexamples(left),and5differentpermutations fiermodelindeedbenefitstheinferenceprocessby
ofthefew-shotexamples(right). Inbothsettings, providingmoreaccuraterelationsbetweengenerwhile Self Consistency and MAIEUTIC PROMPT- atedexplanations,althoughourmethodperforms
ING aremuchmorestablethentheothertwo,our competentlyevenwithouttheaccesstotheverifier.
methodhasslightlylessvariance.
Effect of tree size We also investigate how the
sizeofthemaieutictreeinfluencestheperformance.
4.3 AblationStudy

### InTable3,wepresenttheperformanceofMAIEU-

We ablate different components of MAIEUTIC TIC PROMPTING onCom2Sensedevsetwithvar-
PROMPTING toinvestigatetheirrespectivecontri- ious values of maximal depth and width. In both
butionsasshowninTable2. dimensions,theaccuracysaturatesafteracertain
threshold. We attribute this to (1) the topic drift
Generation First, we consider MAIEUTIC ingenerationwhichintensifiesasthedepthgrows,
PROMPTING withoutabductivegeneration—we (2)largeroverlapsingeneratedknowledgeaswe
generateeachexplanationwithoutprovidinganan- samplemoreexplanationswidth-wise.
swer label, i.e. in an identical fashion to Chain
4.4 HumanEvaluation
of Thought. In this setting, the performance of
MAIEUTIC PROMPTING degradesby4%,alluding We qualitatively analyze actual inference results
totheimportanceofabductivegenerationinelicit- ofMAIEUTIC PROMPTINGthroughhumanevaluingthelatentknowledgefromLM.Next,weablate ation. For each sample, we first retrieve true Es
thedepth-adaptivedecodingmechanism(Section (thesetofgeneratedEsthatareinferredtobeTrue
4),byapplyingeithergreedydecodingornucleus by MAIEUTIC PROMPTING), then evaluate them
sampling for all depths of the maieutic tree. All over the four criteria from Liu et al. (2021): (1)
greedydecodingrestrainswidth-wisespanningof Grammaticalityoftheexplanations,(2)Relevance
knowledge,henceleadstolargedegradationofper- oftheexplanationstothequestion,(3)Factuality:
formance. All nucleus sampling performs much whethertheexplanationsstatesfacts,and(4)Helpmore comparably with our best configuration, al- fulness: whethertheexplanationexplicitlyleadsto
though the stochastic decoding produces slightly thecorrectanswer. SixNLPexpertsscored100exmoreerrorsintheexplanations. amplessampledfromCSQA2.0devset,ofwhich
1272

<!-- Page 8 -->

Maieutic Tree Explanations Max-SAT
Q Q : War cannot have a tie.
E E T T 0 : : I I n n o th r e d e c r o f n o t r e x o t n o e f s a id w e a t r o , t w h i e n r e a i w s a a r l , w th ay e s o a th v e ic r t s o id r e a n m d u a s t lo l s o e s r e . . True Es : E T 2 F 0 , E F 0 , E F 1
integ E ral T / T 0 rue E T 2 integ E ral F / T 0 rue inte E gra F l / 1 True 2 E E T T 2 2 T F 0 0 : : I T n h a e n re y c c a o n n f b li e c t c t a h s e e r s e w is h a e r w e i n b n o e th r a si n d d e s a c lo la s i e m r. victory or where the F alse Es : E T 0 , E T 2 , E T 2 T 0
loser is not clear. Inferred Answer : False
inte E gra T l 2 / T Fa 0 lse int E egr T al 2 / F Tr 0 ue E E F F 0 1 : : H T en h is d e t e o K d r o i c i r n a e l a a ly n d t W r h a e a w r r e a e h n n a d d v e e n d e b i i n e th e a e n m r m s il i a d it n e a y r c y o w a u a r l r d m s c i w s la t h i i c m e e r , e v m i n c e o to a v r n y i i c n . t g o r t h w a a t s t h d e e c w la a r r e d. Ground-Truth : False
Q Q : In football, the top division almost always contains the same clubs.
E T 1 : T re h l e e g F a o t o io tb n a s ll y L st e e a m gu b e e i t s w a e h e i n e r it a s r c m h e ic m al b o e r r g c a l n u i b za s. t ion with a promotion and True Es : E T 1 , E F 0 , E F 1
integ E ral T / T 1 rue E T 2 E F 0 E T 2 : T P h re e m re i e is r l L it e t a le g u m e o , v a e n m d e th n e t o se f c c o lu n b d s d b iv e i t s w io e n e , n k n fo o o w t n b a a l s l's t h to e p C d h i a v m isi p o i n o , n k s n h o ip w . n as the F alse Es : E T 2 , E T 2 T 0
E T 2 T 0 : There is a high level of parity between clubs in the Premier League and Inferred Answer : False
inte E gra T l 2 / T Fa 0 lse int E egr F al 0 / T Tr 0 ue E E F F 0 : : T T h h e e r r e e a a t r r h e e e m m C a a h n n a y y m t t p e e i a a o m m ns s s h t t ip h h . a a t t c g h e a t n re g l e e g d a iv t i e s d io ( n m al o p v l e a c d e o m wn en a t s d i f v r i o s m ion o ) n in e f y o e o a t r b t a o l l t . he next. Ground-Truth : True
1
Figure6: ExamplesofMAIEUTIC PROMPTING,eachwithcorrectandwronganswer. Eveninthelattercase,the
generatedexplanationsmakesensetowardtheinferredanswer. WeprovidemoreexamplesinAppendixD.
50 were answered correctly (Set 1) and 50 were explainsitsinferencepost-hocorinparallelwith
answeredwronglybythemodel(Set2). the answer (Camburu et al., 2018; Narang et al.,
Figure5presentstheevaluationresults. Forboth 2020;Jacovietal.,2021). Unliketheseworks,the
sets,over99%ofthetrueEsaregrammaticallyper- explanationsinourworkaredesignedtobeintrinfect,andmostofthemproviderelevantevidenceto sic(Duetal.,2019);theexplanationsthemselves
thequestion.6 Surprisingly,theLMoftengenerates explicitlyparticipateintheinference.
bothfactualandhelpfulexplanationsevenwhenits

### Meanwhile,recentobservationsrevealthatLM

answerisdifferentfromthegroundtruth: 42%of
explanationsareunreliable,astheyoftenlacklogithetrueEsforincorrectlyansweredexamplesare
calconsistencyandarenotfactuallygrounded(Ye
perfectlyfactual,and23%ofthemarecompletely
and Durrett, 2022; Kassner and Schütze, 2020).
helpful in correctly answering the question. We
This is in part due to the broader limitations of
findthatinmanyofthesecases,thequestionsdid
generativeLMs,whichassignhighprobabilityto
nothaveaclear-cutanswer;asexemplifiedinFigunlikelysentences(Wellecketal.,2020;Holtzman
ure6,theexplanationsgeneratedandvalidatedby
etal.,2021)andaresensitivetosemanticperturba-
MAIEUTIC PROMPTING arecompellingenoughas tions(Elazaretal.,2021). MAIEUTIC PROMPTING
analternativetotheground-truthanswer.
overcomes these limitations by avoiding the use
ofexplanations“as-is”,andmodelingtherelation-
5 RelatedWork
shipsbetweenexplanations.
Prior works have leveraged natural language ex- Anotherlineofworksapplysymbolicmethods
planations (NLEs) to promote model reasoning, ontopofLMstoimprovetheirconsistency,spaneitherbytrainingamodeltoexplain(Rajanietal., ningfromalexicalconstraintonsequencedecod-
2019; Camburu et al., 2018; Chen et al., 2022; ing (Lu et al., 2021a) to a symbolic world model
Wiegreffe and Marasovic´, 2021), or generating (Nyeetal.,2021b)anddiscreteoperations(Chen
answerstotemplatedqueriesanddistantlysuper- etal.,2019;Cobbeetal.,2021). Otherworksexvised rationales (Shwartz et al., 2020; Brahman plorehowtotrainamodelthatsimulatesthesymet al., 2021). Incorporated with in-context learn- bolic reasoning process, such as logical transforing (Brown et al., 2020; inter alia), these efforts mation(Bostrometal.,2021)andconsistentgenerhaveledtoexplanation-basedprompting(Weietal., ationofbeliefs(Kassneretal.,2021;Dalvietal.,
2022;Wangetal.,2022;Liuetal.,2021;Lampinen 2022). However, these models require a curated
et al., 2022). Other works aim to improve model setofhumanannotationsthatlimitstheirapplicainterpretability with NLEs, training a model that tiontospecificdomains. MAIEUTIC PROMPTING
generalizestheseneuro-symbolicapproachesinan
6It is natural that some of the true Es are not directly
unsupervised setup, employing MAX-SAT algorelevanttoQ,butstillcontributetotheinferencebyvalidating
otherEs. rithm to symbolically determine the true subset
1273

<!-- Page 9 -->

fromanoisypoolofneuralgenerations. et al. 2020. Towards a human-like open-domain
chatbot. arXivpreprintarXiv:2001.09977.
6 Conclusion

### RobertoBattiti.2009. Maximumsatisfiabilityproblem,

Inthiswork,weproposeMAIEUTIC PROMPTING, pages2035–2041.SpringerUS,Boston,MA.
anovelfew-shotinferencemethodinspiredbythe

### Chandra Bhagavatula, Ronan Le Bras, Chaitanya

Socratic way of conversation. We systematically Malaviya, Keisuke Sakaguchi, Ari Holtzman, Hangenerate a tree of explanations that bear logical nahRashkin,DougDowney,ScottWen-tauYih,and
Yejin Choi. 2019. Abductive commonsense reasonrelations between each other, then find the truth
ing. arXivpreprintarXiv:1908.05739.
valuesthatmax-satisfytheserelations. Empirical
resultsshowthat MAIEUTIC PROMPTING isboth Kaj Bostrom, Xinyu Zhao, Swarat Chaudhuri, and

### Greg Durrett. 2021. Flexible generation of natural

competitiveandrobustcomparedtodiversebaselanguage deductions. In Proceedings of the 2021
lines,whileprovidingintrinsicinterpretationsover
Conference on Empirical Methods in Natural Lanitsinference. guageProcessing,pages6266–6278.
Limitations FaezeBrahman,VeredShwartz,RachelRudinger,and

### Yejin Choi. 2021. Learning to rationalize for non-

Extension to different task formats In this monotonic reasoning with distant supervision. In
Thirty-Fifth AAAI Conference on Artificial Intelliwork, we limit our experiments to validating a
gence, AAAI 2021, Thirty-Third Conference on Ingiven statement. In future works, we aim to exnovativeApplicationsofArtificialIntelligence,IAAI
tend our method over a broader range of tasks, 2021, The Eleventh Symposium on Educational Ade.g. multiple-choiceQA.Apotentialstrategycould vances in Artificial Intelligence, EAAI 2021, Virbe binarizing multiple-choice options to respec- tualEvent,February2-9,2021,pages12592–12601.
AAAIPress.
tivestatementsandscoringthemwithMAIEUTIC
PROMPTING,e.g. usingthesumofweightofsatis- Tom Brown, Benjamin Mann, Nick Ryder, Melanie
fiedclausesfromMAX-SAT. Subbiah, Jared D Kaplan, Prafulla Dhariwal,

### Arvind Neelakantan, Pranav Shyam, Girish Sastry,

Modelingrelationshipsbetweentrees MAIEU- Amanda Askell, Sandhini Agarwal, Ariel Herbert-
Voss, Gretchen Krueger, Tom Henighan, Rewon

### TIC PROMPTINGmodelstherelationsbetweenthe

Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu,
nodesineachmaieutictreetoinferaconsistentan-

### Clemens Winter, Chris Hesse, Mark Chen, Eric

swer. Thescopeofmodeledrelationships,however, Sigler,MateuszLitwin,ScottGray,BenjaminChess,
couldbefurthergeneralizedbeyondasingletree Jack Clark, Christopher Berner, Sam McCandlish,
-aspanofknowledgegeneratedforonequestion Alec Radford, Ilya Sutskever, and Dario Amodei.

## Language models are few-shot learners. In

could serve as the evidence for another question.

### AdvancesinNeuralInformationProcessingSystems,

Indeed, modeling the relationship between quesvolume 33, pages 1877–1901. Curran Associates,
tions is an active area of research (Kossen et al., Inc.
2021). We envision that the knowledge elicited
Oana-Maria Camburu, Tim Rocktäschel, Thomas
fromMAIEUTIC PROMPTINGcouldfurtherbeen-
Lukasiewicz, and Phil Blunsom. 2018. e-snli: Natrichedthroughthistypeofgeneralization. urallanguageinferencewithnaturallanguageexplanations. Advances in Neural Information Process-
Acknowledgements ingSystems,31.
This work was funded in part by the Natural Sci- Howard Chen, Jacqueline He, Karthik Narasimhan,
andDanqiChen.2022. Canrationalizationimprove
encesandEngineeringResearchCouncilofCanada
robustness? arXivpreprintarXiv:2204.11790.
(NSERC)(fundingreferencenumber401233309),
DARPA MCS program through NIWC Pacific Xinyun Chen, Chen Liang, Adams Wei Yu, Denny

### Zhou, Dawn Song, and Quoc V Le. 2019. Neural

(N66001-19-2-4031), and the Allen Institute for
symbolicreader: Scalableintegrationofdistributed

### AI.WealsothankOpenAIforprovidingaccessto

and symbolic representations for reading compretheGPT-3API. hension. In International Conference on Learning
Representations.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavar-

### References

ian, Jacob Hilton, Reiichiro Nakano, Christopher
Daniel Adiwardana, Minh-Thang Luong, David R So, Hesse, and John Schulman. 2021. Training veri-
JamieHall,NoahFiedel,RomalThoppilan,ZiYang, fiers to solve math word problems. arXiv preprint
Apoorv Kulshreshtha, Gaurav Nemade, Yifeng Lu, arXiv:2110.14168.
1274

<!-- Page 10 -->

Bhavana Dalvi, Oyvind Tafjord, and Peter Clark. JannikKossen,NeilBand,ClareLyle,AidanNGomez,

## Towardsteachablereasoningsystems. arXiv Thomas Rainforth, and Yarin Gal. 2021. SelfpreprintarXiv:2204.13074. attentionbetweendatapoints:Goingbeyondindividualinput-outputpairsindeeplearning. Advancesin

Mengnan Du, Ninghao Liu, and Xia Hu. 2019. Tech- Neural Information Processing Systems, 34:28742–
niques for interpretable machine learning. Commu- 28756.
nicationsoftheACM,63(1):68–77.

### Klaus Krippendorff. 2007. Computing krippendorff’s

Yanai Elazar, Nora Kassner, Shauli Ravfogel, Abhi- alpha-reliability. annenberg school for communicalasha Ravichander, Eduard Hovy, Hinrich Schütze, tiondepartmentalpaper43.
and Yoav Goldberg. 2021. Measuring and im-

### Andrew K Lampinen, Ishita Dasgupta, Stephanie CY

proving consistency in pretrained language models.

### Chan, Kory Matthewson, Michael Henry Tessler,

Transactions of the Association for Computational
Antonia Creswell, James L McClelland, Jane X
Linguistics,9:1012–1031.

### Wang, and Felix Hill. 2022. Can language models

learn from explanations in context? arXiv preprint
MorGeva,DanielKhashabi,EladSegal,TusharKhot,
arXiv:2204.02329.
DanRoth,andJonathanBerant.2021. Didaristotle
usealaptop? aquestionansweringbenchmarkwith
JiachengLiu,AlisaLiu,XimingLu,SeanWelleck,Peimplicitreasoningstrategies. TransactionsoftheAsterWest,RonanLeBras,YejinChoi,andHannaneh
sociationforComputationalLinguistics,9:346–361.
Hajishirzi. 2021. Generated knowledge prompting for commonsense reasoning. arXiv preprint
RobertG.M.HausmannandKurtVanLehn.2007. ExarXiv:2110.08387.
plainingself-explaining:Acontrastbetweencontent
andgeneration. InAIED. YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
AriHoltzman, JanBuys, LiDu, MaxwellForbes, and Luke Zettlemoyer, and Veselin Stoyanov. 2019.
YejinChoi.2019. Thecuriouscaseofneuraltextde- Roberta: A robustly optimized bert pretraining apgeneration. In International Conference on Learn- proach. arXivpreprintarXiv:1907.11692.
ingRepresentations.

### NicholasLourie,RonanLeBras,ChandraBhagavatula,

AriHoltzman,PeterWest,VeredShwartz,YejinChoi, and Yejin Choi. 2021. Unicorn on rainbow: A uniand Luke Zettlemoyer. 2021. Surface form compe- versalcommonsensereasoningmodelonanewmultition: Why the highest probability answer isn’t al- titaskbenchmark. InProceedingsoftheAAAIConwaysright. InProceedingsofthe2021Conference ference on Artificial Intelligence, volume 35, pages
onEmpiricalMethodsinNaturalLanguageProcess- 13480–13488.
ing,pages7038–7051.

### XimingLu,PeterWest,RowanZellers,RonanLeBras,

Alon Jacovi, Swabha Swayamdipta, Shauli Ravfogel, ChandraBhagavatula,andYejinChoi.2021a. Neu-
YanaiElazar,YejinChoi,andYoavGoldberg.2021. rologicdecoding:(un)supervisedneuraltextgenera-
Contrastive explanations for model interpretability. tionwithpredicatelogicconstraints. InProceedings
In Proceedings of the 2021 Conference on Empiri- ofthe2021ConferenceoftheNorthAmericanChapcalMethodsinNaturalLanguageProcessing,pages teroftheAssociationforComputationalLinguistics:
1597–1611. HumanLanguageTechnologies,pages4288–4299.
Yao Lu, Max Bartolo, Alastair Moore, Sebastian

### NoraKassnerandHinrichSchütze.2020. Negatedand

Riedel, and Pontus Stenetorp. 2021b. Fantastically
misprimed probes for pretrained language models:
orderedpromptsandwheretofindthem: Overcom-

### Birdscantalk,butcannotfly. InProceedingsofthe

ingfew-shotpromptordersensitivity. arXivpreprint
58thAnnualMeetingoftheAssociationforCompuarXiv:2104.08786.
tational Linguistics, pages 7811–7818, Online. AssociationforComputationalLinguistics.
Pasquale Minervini and Sebastian Riedel. 2018. Adversarially regularising neural nli models to inte-
Nora Kassner, Oyvind Tafjord, Hinrich Schütze, and
gratelogicalbackgroundknowledge. arXivpreprint
PeterClark.2021. Beliefbank:Addingmemorytoa
arXiv:1808.08609.
pre-trained language model for a systematic notion
ofbelief. InProceedingsofthe2021Conferenceon António Morgado, Carmine Dodaro, and Joao
EmpiricalMethodsinNaturalLanguageProcessing, Marques-Silva.2014. Core-guidedmaxsatwithsoft
pages8849–8861. cardinalityconstraints. InInternationalConference
on Principles and Practice of Constraint Program-
Daniel Khashabi, Sewon Min, Tushar Khot, Ashish ming,pages564–573.Springer.
Sabharwal, Oyvind Tafjord, Peter Clark, and Hannaneh Hajishirzi. 2020. Unifiedqa: Crossing for- Sharan Narang, Colin Raffel, Katherine Lee, Adam
mat boundaries with a single qa system. In Find- Roberts, NoahFiedel, andKarishmaMalkan.2020.
ings of the Association for Computational Linguis- Wt5?! training text-to-text models to explain their
tics: EMNLP2020,pages1896–1907. predictions. arXivpreprintarXiv:2004.14546.
1275

<!-- Page 11 -->

MaxwellNye,AndersJohanAndreassen,GuyGur-Ari, XuezhiWang,JasonWei,DaleSchuurmans,QuocLe,
Henryk Michalewski, Jacob Austin, David Bieber, Ed Chi, and Denny Zhou. 2022. Self-consistency
David Dohan, Aitor Lewkowycz, Maarten Bosma, improves chain of thought reasoning in language
DavidLuan,etal.2021a. Showyourwork: Scratch- models. arXivpreprintarXiv:2203.11171.
pads for intermediate computation with language
models. arXivpreprintarXiv:2112.00114. Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Ed Chi, Quoc Le, and Denny Zhou. 2022.
Maxwell Nye, Michael Tessler, Josh Tenenbaum, and Chainofthoughtpromptingelicitsreasoninginlarge
BrendenMLake.2021b. Improvingcoherenceand languagemodels. arXivpreprintarXiv:2201.11903.
consistency in neural sequence models with dualsystem, neuro-symbolic reasoning. Advances in Sean Welleck, Ilia Kulikov, Jaedeok Kim,
NeuralInformationProcessingSystems,34. Richard Yuanzhe Pang, and Kyunghyun Cho.

## Consistency of a recurrent language model

YasumasaOnoe,MichaelJ.Q.Zhang,EunsolChoi,and with respect to incomplete decoding. In Proceed-
GregDurrett. 2021. Creak: Adatasetfor common- ings of the 2020 Conference on Empirical Methods
sense reasoning over entity knowledge. OpenRe- in Natural Language Processing (EMNLP), pages
view. 5553–5568.
Charles Sanders Peirce. 1974. Collected papers of

### SarahWiegreffeandAnaMarasovic´.2021. Teachme

charles sanders peirce, volume 5. Harvard Univertoexplain: Areviewofdatasetsforexplainablenlp.
sityPress.
arXivpreprintarXiv:2102.12060.
Colin Raffel, Noam Shazeer, Adam Roberts, Kather-
Adina Williams, Nikita Nangia, and Samuel Bowman.
ine Lee, Sharan Narang, Michael Matena, Yanqi

## A broad-coverage challenge corpus for sen-


### Zhou, Wei Li, and Peter J. Liu. 2020. Exploring

tenceunderstandingthroughinference. InProceedthelimitsoftransferlearningwithaunifiedtext-toingsofthe2018ConferenceoftheNorthAmerican
text transformer. Journal of Machine Learning Re-
Chapter of the Association for Computational Linsearch,21(140):1–67.
guistics: Human Language Technologies, Volume 1
Nazneen Fatema Rajani, Bryan McCann, Caiming (LongPapers),pages1112–1122.

### Xiong, and Richard Socher. 2019. Explain your-

Xi Ye and Greg Durrett. 2022. The unreliability of
self! leveraginglanguagemodelsforcommonsense
explanations in few-shot in-context learning. arXiv
reasoning. InProceedingsofthe57thAnnualMeetpreprintarxiv:2205.03401.
ingoftheAssociationforComputationalLinguistics,
pages4932–4942.

### Zihao Zhao, Eric Wallace, Shi Feng, Dan Klein, and

Vered Shwartz, Peter West, Ronan Le Bras, Chandra SameerSingh.2021. Calibratebeforeuse: Improv-
Bhagavatula, and Yejin Choi. 2020. Unsupervised ingfew-shotperformanceoflanguagemodels. InIncommonsensequestionansweringwithself-talk. In ternationalConferenceonMachineLearning,pages
Proceedings of the 2020 Conference on Empirical 12697–12706.PMLR.
MethodsinNaturalLanguageProcessing(EMNLP),
pages4615–4629.
ShikharSingh,NuanWen,YuHou,PegahAlipoormolabashi, Te-lin Wu, Xuezhe Ma, and Nanyun Peng.

## COM2SENSE: A commonsense reasoning

benchmarkwithcomplementarysentences. InFindings of the Association for Computational Linguistics: ACL-IJCNLP 2021, pages 883–898, Online.
AssociationforComputationalLinguistics.
AlonTalmor,OriYoran,RonanLeBras,ChandraBhagavatula, Yoav Goldberg, Yejin Choi, and Jonathan

### Berant.2021. CommonsenseQA2.0: Exposingthe

limits of AI through gamification. In Thirty-fifth
Conference on Neural Information Processing Systems.
Gregory Vlastos. 1991. Socrates, ironist and moral
philosopher,volume50. CornellUniversityPress.

### HaohanWang,DaSun,andEricPXing.2019. Whatif

we simply swap the two text fragments? a straightforward yet effective way to test the robustness of
methods to confounding signals in nature language
inferencetasks. InProceedingsoftheAAAIConferenceonArtificialIntelligence,pages7136–7143.
1276

<!-- Page 12 -->


### A TreeGenerationAlgorithm

Algorithm1Maieutictreegeneration
Input: QuestionQ,MaxtreedepthD
Output: Maieutictree

## T

init(Q) // initialize the tree with Q

## T ←

ford 1, ,D do // generate nodes
∈{ ··· }

## S

i
←∅
forE S i 1do
ifi ∈ nteg−ral(E)=1then
S S abductive(E)
i i
← ∪
endif
endfor
.add(S )
i

## T

endfor
V E;integral(E)=0 forallE leaf( ) // set of non-integral leaf nodes

## ←{ ∈ T }

whileV = do
6 ∅
.remove(V) // prune the non-integral leaf nodes

## T

V E;integral(E)=0 forallE leaf( )

## ←{ ∈ T }

endwhile

### B DatasetDetails


### Dataset Com2Sense CSQA2.0 CREAK

Train/Dev/Testsplitsize 804/402/2779 9282/2544/2517 10176/1371/1371

### Average#oftokens 21 11.3(words) 10.8

Table4: Weevaluate MAIEUTIC PROMPTING inthreecommonsensereasoningandfactverificationbenchmarks
-Com2Sense,CSQA2.0andCREAK.Com2SenseandCSQA2.0consistofadversarialcommonsensequestions
generatedtomisleadaproxymodel. CREAKtestsforacombinationofcommonsensereasoningandaccuratefact
retrieval,consistingoflong-tailquestionssuchas“HarryPottercanteachhowtoflyonabroomstick?”. Table4
presentskeystatisticsofthethreedatasets.

### C Multi-hopReasoningonStrategyQA

Model Standard C-o-T Maieutic C-o-T(Multi-hop) Maieutic(Multi-hop)
Accuracy 56.3 58.2 60.7 57.9 61.4

### Table5: ResultsonStrategyQA

TofurtherevaluatethegeneralizabilityofMAIEUTIC PROMPTING,weconductadditionalexperiments
onmulti-hopreasoningoverStrategyQA(Gevaetal.,2021)devsplit. Notethattheoriginalevaluation
settingforStrategyQApresupposesaccesstoWikipediaarticles,fromwhichthegoldknowledgecould
beretrievedfrom;hencethebenchmarkas-ismaynotrepresentthebestevaluationsettingforfew-shot
promptingmethods.
To better address the multi-hop nature of the dataset, we add a straightforward adjustment to both
C-o-TandMaieuticPrompting,tofirstdecomposetheoriginalquestioninto2-3minorquestionsandthen
generatetheexplanationandanswer. WedenotethisasMulti-hopinTable5.
Consistentwiththeoriginalexperimentalresults,MaieuticPromptingyieldspromisingimprovement
comparedtoboththestandard/C-o-Tprompting. TheresultatteststoboththegeneralizabilityofMaieutic
Promptingtomulti-hopsettingandtheimportanceofreasoningalgorithminchallengingscenarios.
1277

<!-- Page 13 -->


### D InferenceExamples

Q: If you travel west far enough from the west coast, you will reach the east coast.
dir E ec T0t : i o T n h e lo n E g a r e th n
w
o is
h
u
e
r g o
r
h
e
u , n
y
y
o
d o
u
u a
s
n w
t
d
a
i l
r
l i
t
f e
e
y v
d
o e
.
u n t t u ra a v ll e y l r i e n t u a r n n y to EF2 : You can only
e
t
n
ra
d
v
o
el
f
s
th
o
e
f a
e
r
a
b
rt
e
h
f
.
ore you reach the
ET2 : All d

## N

ir
o
e
r
c
t
t
h
io
a
n
n
s
d
e

## S

ve
o
n
u
t
t
u
h
a

## P

lly
o l
m
es
e
.
et at the integral / True EF0 : You cannot reach the east coast by going west.
integral / True

## Et

s1t
:
r a

## T

i
h
g
e
h t
w
li
o
n
r
e
ld
, y
is
o u
ro
w
un
ill
d
e
a
v
n
e
d
nt
i
u
f
a
y
l
o
ly
u
r e
c
a
o
c
n
h
ti n
th
u
e
e
o
to
th
t
e
ra
r
v
s
e
id
l
e
in
.
a EF0T0 : You can
tr a
re
ve
a
l
c
in
h
g
t h
a
e
ro
e
u
a
n
s
d
t c
th
o
e
a s
w
t
o
b
r
y
ld
g
.
oing west by E
in

## F

t
2
e

## F

g
0 :
r a

## T

l
h
/
e

## T


## E

ru
a
e
rth is round.
integral / False
i

## E

nt

## T

e

## 1T

g
0
r
:
a

## A

l /
s

## T

tr
r
a
u
i
e
ght line on a sphere makes a ci

## E

rc

## T

l
1
e

## F

.
0 : The world is not round.
EF1 : If yo
e
u
v e
tr
n
a
t
v
u
e
a
l
l l
f
y
a r
re
e
a
n
c
o
h
u
t
g
h
h
e
i
o
n
p
a
p
n
o
y
s
d
it
i
e
re
c
c
o
ti
a
o
s
n
t
,
.
you will
integral / False
EF1F0 : It is impossible to travel to the other side of the Earth.
integral / False
T rue Es : ET0 , ET1 , ET1T0 , ET2 , EF0T0 , EF1 , EF2F0 / False Es : ET1F0 , EF0 , EF1F0 , EF2

### Inferred Answer : True / Ground-Truth : True

Figure 7: Example of correct inference by MAIEUTIC PROMPTING. We show the generated maieutic tree along
withtheassignedtruth-valuestoeachpropositions.
Q: The Earth is a planet that is made primarily of air and helium.
E in T t1e : g T r h a e l e / a T r r th u e is composed of gas, rocks and metal. E F1 : Air only makes up a small fraction of the Earth's mass.
E T0 : The earth is made primarily of gas. i E nt T e2r : i o A r c is c o c r o d m in p g o t s o e t d h e o f e a m d p e ir n ic s a e l l c y o -b re a , s a e d m m an o t d le e , l a o n f d th a e c E r a u r s t t h . , T t h h e e c E r a u r s th t ' i s s E F1T0 : Th a e b E o a u r t t h 1 ' % s a o tm f t o h s e p E h a e r r t e h ' ( s m m ad a e s s u . p of air) is
made up of the solid rock, the mantle is made of the hot rock, and the integral / False
core is made of the solid metal.

## E

in

## T

t
0
e

## T

g
0 :
r a

## T

l
h e

## / T

e
r
a
u
rt
e
h is made of gas, rocks, and other materials. E F0 : The earth is not made primarily of air and helium.

## E T2F0 :

in

## T

a
h
t e
e
d g e

## E

n r
a
a s
r
l e
t h
/ c
's
F o r a
in
e l ,
t
s
e
m e
ri
a
o
n
r
t
i
l
s
e
n
o
o
r
t
c
c
r
o
u
m
st.
posed of
in E t F e0g T r0a : l A / i r T a r n u d e helium is only a part of the Earth's atmosphere.
is t E he T 2g T e0 : n e T r h a e ll y e m ac p c i e ri p c t a e ll d y - m ba o s d e e d l o m f o th d e e l E o a f r t t h h e 's E in a t r e th ri o r. E F0F0 : The earth is made of a variety of elements including air and helium.
integral / True integral / True
True Es : E T0T0 , E T1 , E T2 , E T2T0 , E F0 , E F0T0 , E F0F0 , E F1 / False Es : E T0 , E T2F0 , E F1T0

### Inferred Answer : False / Ground-Truth : False

Figure8: (continued)ExampleofcorrectinferencebyMAIEUTICPROMPTING.
1278

<!-- Page 14 -->

integral / True
Q: Everyone is capable of moving lower in the food chain.
E T : Every living being is capable of
1
getting energy from lower in the food chain.
integral / True

### E F : Some people are not capable of digesting complex

E T : Humans are omnivores that can consume both carb 1 s and proteins and thus, must eat food from the higher
2 plants and animals. end of the food chain.
integral / True
integral / True
E F : Some people are not able to digest complex proteins,
0
and therefore, need to eat food that is lower in the food chain.
integral / True
True Es : E ,E , E , E

## T T F F

1 2 0 1

### Inferred Answer : True / Ground-Truth : False

Figure9: ExampleofincorrectinferencebyMAIEUTICPROMPTING.
integral / False
integral / True
Q: A city will always have transient traffic.
E T1 : People in a city are always coming and going.
E T0 : People
a l
p
w
a
a
s
y
s
s
in
b
g
e
t h
th
ro
e
u
re
g
.
h a city will integral / True E F2 : A city wil
a
l
n
h
d
a v
lo
e
c
a
a l
m
tr
ix
a ffi
of
c .
both transient
integral / False
E T2 : A city is a
c o
p
m
la
e
c e
a n
w
d
h e
g
r
o
e
.
many people E F2T0 : A ci
p
ty
e o
w
p
il
l
l
e
h
w
av
h
e
o
p
a
e
re
o p
ju
le
s t
w
v
h
is
o
it i
l
n
iv
g
e
.
there and E F
in
0 :
t e

## A

g r
c
a
it
l
n y
/
o w

## T

n
r
i -
u
ll t
e
r h a a n v s e ie b n o t t t h ra t ffi ra c n . sient and
integral / True
E in T te 2T g 0 : r a A l / c T it r y u i e s a place where m E a T n 2F y 0 : p A e o c p ity le i s l iv a e p . lace where people live and work. add E re F s1s : e A s c a it n y d w c i o ll m ha m v u e t e re r s s i d w e h n o t s h w av h e o t e h m av p e o p ra e l r m ad a d n r e e n s t s es.
integral / True integral / True
True Es : E T1 , E T2 , E T2T0 , E T2F0 , E F0 , E F1 , E F2 , E F2T0 / False Es : E T0

### Inferred Answer : False / Ground-Truth : True

Figure10: (continued)ExampleofincorrectinferencebyMAIEUTICPROMPTING.
1279

## Tables

**Table (Page 1):**

| Input Prompt |
|---|
| Output |


**Table (Page 1):**

| Q: Captain Kirk is part of Star Wars? |
|---|
| A: Captain Kirk is a character in Star Trek. Therefore, the answer is False. |


**Table (Page 1):**

| Q: At least one mayor is not male? |
|---|
| A: There are female mayors. Therefore, the answer is True. |


**Table (Page 4):**

|  |
|---|
| ET : The Earth is round and if you travel in any direction long enough, you will eventually return to where you started. |
| integral(ET)= 1 |


**Table (Page 4):**

| EFT : You can reach the east coast by going west by traveling around the world. |
|---|
| integral(EFT)= 1 |


**Table (Page 4):**

|  |  |
|---|---|
| EF :You cannot reach the east coast by going west. |  |
|  |  |
| integral(EF)= 0 |  |


**Table (Page 4):**

| EFF : If you travel in a specific straight line, you will eventually reach the other side. |
|---|
| integral(EFF)= 0 |


**Table (Page 6):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  | 60.673 |  |  |  | 61.2 |  | 72.34 |
|  |  |  |  |  |  |  |  |
| 57.883 |  |  |  |  |  |  |  |


**Table (Page 6):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  | 61.052 |  | 61.544 |  | 71.68 |
|  |  |  |  |  |  |  |  |
| 57.801 |  |  |  |  |  |  |  |


**Table (Page 6):**

|  |
|---|
|  |


**Table (Page 6):**

|  |
|---|
|  |


**Table (Page 6):**

| ev | al | uate | th | e | gen | er | a |  | abi |  | y | o |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | liz |  | lit |  |  |
| P | TIN | Gi |  |  | lti- | ho | p | s | ettin | g | . |  |
|  |  |  | n | mu |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| u | stn | ess | A | na | lysi | s |  |  |  |  |  |  |
| rm | ad | dit | ion | al | ana | ly | s | es | to | un |  | de |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| of | ou | r m | et | ho | d un | d | e | r | sem | an | t | ic |


**Table (Page 7):**

|  | Standard Self Consistency |  |
|---|---|---|
|  |  |  |


**Table (Page 7):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  | 60.673 |  |  |  | 61.2 |  | 72.34 |  |
|  |  |  |  |  |  |  |  |  |
| 57.883 |  |  |  |  |  |  |  |  |


**Table (Page 7):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 61.544 |  | 71.68 |  |
|  |  |  |  |  |  |  |  |  |
| 57.801 |  |  |  |  |  |  |  |  |


**Table (Page 7):**

|  |
|---|
|  |


**Table (Page 7):**

|  |
|---|
|  |


**Table (Page 7):**

|  |
|---|
|  |


**Table (Page 7):**

| 96.6 | 7 | 99.33 |  | 23.33 |  | 4.67 18.67 |  | 6.67 28.67 |  | 14.67 |  | 13.34 |  | 34.00 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | 42.67 |  | 22.00 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | 76.67 |  | 76.67 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 64.67 |  |  |  |  |  | 42.67 |
|  |  |  |  |  |  |  |  |  |  |  |  | 64.67 |  |  |
|  |  |  |  |  |  |  |  |  |  | 42.67 |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | 23.33 |


**Table (Page 13):**

|  | E T0t : T h e E a r th is r o u n d a n d i f y o u t ra v e l i n a n y dir ec i o n lo n g e n o u g h , y o u w i ll e v e n t u a ll y r e t u r n to where you started. |  |
|---|---|---|
| ET2 : All d ir e c t io n s e ve n t u a lly m e et at the N o r t h a n d S o u t h P o l es . |  |  |


**Table (Page 13):**

| EF2 : You can only t ra v el s o f a r b e f ore you reach the e n d o f th e e a rt h . |
|---|
|  |


**Table (Page 14):**

|  | E T1 : People in a city are always coming and going. integral / True |  |
|---|---|---|
| E T0 : People passing through a city will integral / Tr always be there. | integral / Tr |  |
