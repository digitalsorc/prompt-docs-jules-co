---
title: "Repository Level Prompt Generation"
original_file: "./27_Repository_Level_Prompt_Generation.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["rlpg", "prompt", "code", "wise", "context", "page", "hole", "repository", "proposal", "repo"]
summary: "<!-- Page 1 -->

Repository-Level Prompt Generation for Large Language Models of Code

### DishaShrivastava12 HugoLarochelle1234 DanielTarlow153


### Abstract Asopposedtothepretrain-finetuneparadigm, prompting

With the success of large language models these LLMs have been found to yield good performance
(LLMs)ofcodeandtheiruseascodeassistants evenwithfew-examples(Liuetal.,2023). Codex (Chen et al., 2021) used in GitHub ing a mechanism to control and evaluate a LM, prompts
Copilot), techniques "
related_documents: []
---

# Repository Level Prompt Generation

<!-- Page 1 -->

Repository-Level Prompt Generation for Large Language Models of Code

### DishaShrivastava12 HugoLarochelle1234 DanielTarlow153


### Abstract Asopposedtothepretrain-finetuneparadigm, prompting

With the success of large language models these LLMs have been found to yield good performance
(LLMs)ofcodeandtheiruseascodeassistants evenwithfew-examples(Liuetal.,2023). Besidesprovid-
(e.g. Codex (Chen et al., 2021) used in GitHub ing a mechanism to control and evaluate a LM, prompts
Copilot), techniques for introducing domain- havebeenshowntoelicitemergentbehaviouraswell. Exspecificknowledgeinthepromptdesignprocess amplesofthisbehaviorincludeGPT-3(Brownetal.,2020)
become important. In this work, we propose a doingbetterintasksithasneverseenduringtrainingand
frameworkcalledRepo-LevelPromptGenerator improvedreasoningcapabilitieswithfew-shot(Weietal.,
thatlearnstogenerateexample-specificprompts 2022)andzero-shot(Kojimaetal.,2022)promptsthatenusing prompt proposals. The prompt proposals courage a chain of thoughts. These factors highlight the
take context from the entire repository, thereby importanceofdesigninganeffectivetask-specificprompt.
incorporatingboththestructureoftherepository However,currentlywehavealimitedunderstandingofhow
and the context from other relevant files (e.g. todothis(Reynolds&McDonell,2021). LLMshavealso
imports,parentclassfiles). Ourtechniquedoesn’t been used for modeling source code with impressive rerequire any access to the weights of the LLM, sults(Austinetal.,2021;Friedetal.,2022;Xuetal.,2022a).
making it applicable in cases where we only Inparticular,oneofthebestperformingLLM,Codex(Chen
haveblack-boxaccesstotheLLM.Weconduct
etal.,2021),hasbeendeployedaspartofGitHubCopilot1,
experiments on the task of single-line code astate-of-the-artin-IDEcodeassistant. Despitethegrowing
auto-completion using code repositories taken popularityofLLMsofcode,thereisnoworkthatsystemfrom Google Code archives. We demonstrate atically tackles different aspects of prompt generation in
that an oracle constructed from our prompt relation to source code. One such aspect is that when it
proposals gives a relative improvement of comestocode,therelevantcontexttobeputintheprompt
36% over Codex, showing the quality of these cancomefromnotjustthecurrentfile,butalsofromoutproposals. Further, we show that when we side,suchasimports,parentclasses,fileswithinthesame
train a model to predict a prompt proposal, we directory,andAPIdocumentation. Also,dependingonthe
can achieve significant performance gains over scenario,therelevantcontextcanbescatteredacrossmulti-
Codex and other baselines. We release our plelocations. SincetheLLMshavealimitedcontextlength
code, data, and trained checkpoints at https: availablefortheprompt,itbecomesincreasinglycrucialfor
//github.com/shrivastavadisha/ our domain-specific understanding to guide the selection
repo_level_prompt_generation. of relevant context. Currently, it is not clear how to integratethisdomainknowledgeofwhatconstitutesarelevant
context, into the generation of prompts. Addressing this

## Introduction question has potential benefits in other domains such as

questionanswering(Liuetal.,2022)andmulti-document
Large Language Models (LLMs) have demonstrated resummarization(Xiaoetal.,2022),wheredomain-specific
markable performance in natural language processing
structuredretrievalofcontextcanbeuseful.
tasks (Brown et al., 2020; Chowdhery et al., 2022), textto-imagegeneration(Rameshetal.,2022;Rombachetal.,

### Inthiswork,weaddressthisproblembyproposingRepo-

2022)andevenasageneralizedagent(Reedetal.,2022).

### LevelPromptGenerator(RLPG),aframeworkthatwhile

generatingtheprompt,incorporatesboththestructureofthe
1Mila 2Université de Montréal 3Google 4CIFAR Associate repositoryaswellastherelevantcontextinthefilesinthe
Fellow5McGillUniversity.Correspondenceto:DishaShrivastava
repository. InRLPG,thechoiceofwherefromandwhat
<dishu.905@gmail.com>.
totakefromtherepositoryisspecifiedbyasetofprompt
Proceedings of the 40th International Conference on Machine proposals. Forexample,oneofthepromptproposalscanbe
Learning,Honolulu,Hawaii,USA.PMLR202,2023.Copyright
2023bytheauthor(s).
1https://copilot.github.com/
1
3202
nuJ
5
]GL.sc[
3v93821.6022:viXra

<!-- Page 2 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
Figure1.Repo-LevelPromptGenerator: Givenalistofpromptproposalsandthetargetholepositionalongwiththeassociated
repositoryasinput,thepromptproposalclassifierpredictsapromptproposal.Thecontextfromthepredictedpromptproposalp=14,
i.e.,methodnamesandbodiesfromtheimportedfile(highlightedinviolet)isthencombinedwiththedefaultCodexcontextorcontext
priortothepositionoftheholeinthecurrentfile(highlightedingray)tocomposeaprompt.PromptingCodexwiththegeneratedprompt
producesapredictionforthetargethole(highlightedindarkred).
totakealltheidentifiersusedinthefirstimportfile. These //openai.com/blog/openai-codex/ and no acpromptproposalsallowthepromptengineerstoinducetheir cesstomodelweightsanddataisprovided),makingthese
domain expertise in the prompt-designing process. With techniqueslessusefulunderthisscenario. RLPGaddresses
theincreasinguseofLLMsasassistiveagentstohumans, thislimitationbygeneratingpromptsassumingonlyblackthedemandfortransparency,andthedesireofsoftwareen- boxaccesstotheLLM.Evenforcaseswherewehaveaccess
gineerstotailorpromptstosuittheirrequirements(Jiang tothemodelweights,RLPGprovidesawaytoadapttothe
etal.,2022;Sunetal.,2022),thiscapabilitybecomesim- repository-level context without having the need to fineportant. Similar to some previous works in NLP (Shin tunethemodelrepeatedly. Thiscanbeparticularlyuseful
etal.,2020;Schick&Schütze,2021),ourpromptpropos- whenadaptingtoarepositorythatcontainsproprietaryor
alsarediscrete. However,ratherthanfixingoneparticular nichesoftware,thatthemodelhaslimitedchancesofseeing
promptproposalforeachexample,weinsteadpredictthe duringtraining.
bestpromptproposalconditionedontheexample. Wedo
We focus on the task of single-line code autocompletion
this by coming up with a neural network called Prompt
in an IDE, where the objective is to predict the blanked-
ProposalClassifier(PPC)thatlearnstoselectapromptproout portion (or target hole) starting from the position of
posalsuchthattheresultingpromptislikelytoproducethe
an imagined cursor to the end of the line (highlighted in
desiredoutput. Therefore,RLPGallowstheintroductionof
blue in Figure 1). We operate under the line-level maindomainexpertise,andatthesametimefacilitatesautomatic
tenance setting (Shrivastava et al., 2020; Hellendoorn &
example-specific prompt generation via a learned neural
Devanbu, 2017) that reflects the scenario where a user is
network. Notethattherearesometechniquesforautomatic
editinganexistingfile. Thismeansthattherecanbecode
promptgenerationinNLP(Li&Liang,2021;Shinetal.,
followingtheline. Figure1providesanillustrationofour
2020;Lesteretal.,2021)thatrequireupdatingsomeorall
approach. Thepromptproposalclassifiertakesinthehole
oftheweightsoftheLLM.However,thestrongestLLMs
position(positionofthecursor)inthecurrentfile,thereposarenotpubliclyavailable(e.g. OpenAIprovidesaccessonly
itory to which the current file belongs, and a set of repoto the generated output from Codex via an API https:
levelpromptproposalsasinput,andpredictsapromptpro-
2

<!-- Page 3 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
posal. Inourillustratedexample,thepredictedpromptpro- byapromptsourceandapromptcontexttype. Wemention
posalcorrespondstotakingthemethodnamesandbodies eachofthesealongwiththeirmotivationbelow.
fromMaximizingGibbsSampler.java(mg.before
PromptSource: Foratargetholeposition,apromptsource
theholepositionindicatesthatamethodfromtheimported
determinesfromwhereshouldwetakecodethatwillbepart
fileislikelytobeinvoked). ThePromptComposerusesthe
ofthepromptproposalcontext. Weproposetendifferent
contextfromthepredictedpromptproposalandcombinesit
promptsources:
withthedefaultCodexcontext,i.e.,codepriortotheposition
of the hole in the current file. The resulting prompt consistsofthemethodnameInitializeToAssignment 1. Current: takecodefromthecurrentfileexcludingthe
(from the prompt proposal context) and the method contentsofthetargethole. Thecurrentfileisthefile
CurrentAssignments()(fromthedefaultCodexcon- thatcontainsthetargethole. Thecodeinthecurrent
text),resultinginasuccessfulprediction(brownboxonthe file(e.g.thelinesaftertheholeposition)canbevery
top)ofthetargethole. Ourkeycontributionsareasfollows: usefulinpredictingthetargethole.

## Parent Class: take code from the file that contains

theparentoftheclasstowhichthetargetholebelongs.
• WeproposeaframeworkcalledtheRepo-LevelPrompt Theintuitionbehindthisistoaccountforcaseswhere
Generator(RLPG)thatlearnstogeneratepromptsconamethodpresentintheparentclassisinvokedinthe
ditionedontheexample,withoutrequiringaccesstothe currentfile(i.e.thechildclass).
weightsoftheLLM. 3. Import: take code from the import files used in the
• RLPGallowsustouseboththestructureofthereposi- currentfile. The dependenciesspecified viaimports
tory as well as the relevant context from all files in the canprovideusefulcuestopredictthetargethole.
repository,therebyprovidingamechanismtoincorporate 4. Sibling: takecodefromthefilesthatareinthesame
domainknowledgeinthepromptgenerationprocess. directoryasthecurrentfile. Filesinthesamedirectory
• Onthetaskofsingle-linecode-autocompletion,weshow tendtosharecodevariables(e.g.identifiers).
thatanoracleconstructedfromourproposedpromptpro- 5. SimilarName: takecodefromfilesthathaveasimilar
posalsgivesupto36%relativeimprovementoverCodex. nameasthecurrentfile. Similarnamesaredetermined
ThisimprovementispleasantlysurprisingasCodexhas bysplittingthefilenamebasedonunderscoreorcamelneverseen prompts made fromthese prompt proposals caseformattingandthenmatchingpartsofthefilename.
duringtraining. Further,weshowthatwhenweuseour Ifoneormorepartsmatches,twofilesareconsidered
promptproposalclassifiertopredictthebestpromptpro- tohavesimilarnames. Theintuitionbehindthisisthat
posal, we can achieve up to 17% relative improvement software developers tend to name files based on the
overCodex,aswellasimproveoverotherbaselines. functionalityofthecodewritteninthatfile. Therefore,
asimilarnamefilemightcontainsomeportionofthe

## Repo-LevelPromptGenerator(RLPG) codethatiscommonwiththecurrentfileandhence

mightbeusefulforpredictingthetargethole.
Inthissection, weprovidedetailsofourframework. We 6. ChildClass: takecodefromfilesthathavethecurrent
startbydescribingourpromptproposalsandthendiscuss fileastheirparentclassfile.
ourpromptproposalclassifierwhichisfollowedbyade- 7. ImportofParentClass: takecodefromtheimport
scriptionofthepromptcomposer. filesusedintheparentclassfiles.

## Import of Sibling: take code from the import files


### Repo-LevelPromptProposals usedinthesiblingfiles.


## ImportofSimilarName: takecodefromtheimport

ThecoreideaofRLPGconsistsofsubstitutingpartofthedefilesusedinthesimilarnamefiles.
faultcontextusedbyCodexwithcontextcomingfromsome-

## Import of Child Class: take code from the import

whereelseintherepository. Thedecisionofwhattotake
filesusedinthechildclassfiles.
andfromwhereintherepositorytotakefromisgoverned
byasetofpromptproposals. Thesepromptproposalswere
decided based on manual inspection of our training data The last four prompt sources are useful when the target
andintendtocapturecommoncodingpatterns(butmore hole occurs at the very beginning of the current file. In
generallycanalsoincludeproject/organization-specificcod- thesecases,therewouldbelesscontextcomingfromother
ingpractices). Apromptproposalcanbethoughtofasa promptsources. Foreachpromptsource,wecangeteither
functionthattakesasinputatargethole’spositionandthe asinglefileorarankedlistoffiles(seeAppendixB.1). In
repository that the hole is a part of, and that returns the the latter case, we will take context fromthese files until
promptproposalcontext(astringconstitutedbythecontext we exhaust the maximum context length allocated to the
fromthepromptproposal). Apromptproposalisspecified promptproposal.
3

<!-- Page 4 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
Prompt Context Type: The prompt context type deter- and leads to success, yh = 1 and will be zero otherwise.
p
mineswhatcodetotakefromthepromptsource. Wepro- Foreachholeh,weobtainamaskThwhereTh =1when
p
posesevendifferentpromptcontexttypes(AppendixB.2 pisapplicableorzerootherwise. Theoveralltrainingloss
hasexamplesofeachtype): LcanbeexpressedasthesumofindividualholelossesLh:

## PostLines(PL):Takeallthelinesafterthetargethole N N Mh

1 (cid:88) 1 (cid:88) 1 (cid:88)
linetilltheendofthecurrentfile2. L= Lh = BCE(yˆh,yh)∗Th

### N N Mh p p p


## Identifiers (I): Take all the identifiers used in the h=1 h=1 p=1

promptsource.

## TypeIdentifiers(TI):Takeallthetypeidentifiersused Intheaboveequation,Mh = (cid:80) p T p hdenotesthetotalnuminthepromptsource. ber of applicable prompt proposals for h, N is the total


## Field Declarations (FD): Take all the field declara- numberofholesencounteredwhiletrainingandBCE cortionsusedinthepromptsource. respondstothebinarycrossentropyloss. Maskingensures


## StringLiterals(SL):Takeallthestringliteralsused thatweconsideronlythepromptproposalsthatareapplicainthepromptsource. ble. Next,wedescribeourtwovariantsofPPCthatcanbe


## Method Names (MN): Take all the method names usedtoobtainthepredictionyˆ p h.

alongwiththeirsignaturesusedinthepromptsource.

### RLPG-H:LetHh betheholewindowthatincludescode


## Method Names and Bodies (MNB): Take all the

presentaroundtheholehexcludingtheholeitself. Inour
methodnamesalongwiththeirsignaturesandcorrework,wetaketwolinesbeforetheholeposition,thecodeup
spondingbodiesusedinthepromptsource.
totheholepositionandtwolinesaftertheholeposition. We
useapretrainedmodelF toobtainacontextrepresentation
Bycombiningpromptsourceswithpromptcontexttypes, ϕ
vectorofsizeZ, whereZ isthedimensionofthehidden
wegetatotalof63promptproposals(seeAppendixB.4
state of the model. Specifically, we take the hidden state
for details). Note that depending on the target hole, not
at the first position, i.e. the representation of the [CLS]
allpromptproposalswouldbeapplicable(e.g.ifthereare
token. TomaketrainingofPPCcomputationallyefficient,
noparentclassesinthecurrentfile,promptproposalswith
theparametersϕarefrozenduringtraining. TheRLPG-H
promptsourceasparentclassfilewon’tbeapplicable). In
modeltakesthecontextrepresentationoftheholewindow
Figure1,thepredictedpromptproposalcorrespondstotakand projects it to the prompt proposal space of size M
ingpromptsourceImportandpromptcontexttypeMNB.
viatwodenselayerswithanon-linearityinbetween(see

### Weaimedforasetofpromptproposalsthatoffermorediver-

Equation 1). Taking the sigmoid of this output gives the
sityratherthanasetofpromptproposalsthatareallgood.
predictionofthepromptproposal.

### Thisinturnensuresthatforanyholeposition,asignificant

numberofpromptproposalsareapplicable. yˆh =P(yh =1|Hh)
p p
=sigmoid(W2(relu(W1(F (Hh))+b1))+b2) (1)

### PromptProposalClassifier(PPC) ϕ

Givenaholeposition,thegoalofthepromptproposalclas- RLPG-R:Themotivationbehindthisvariantistousethe
sifier is to predict the prompt proposal p that will lead to similarityoftheholewindowandthepromptproposalconsuccess,wheresuccesshappenswhenthepredictedholehˆ text to determine which prompt proposal can be useful.
exactlymatchesthetargetholeh. Thistaskisformulated Given a particular hole h, let Ch denote the prompt prop
as a multi-label binary classification problem since for a posal context from prompt proposal p. Intuitively, if the
giventargethole,morethanonepromptproposalscanlead hole window contains variables (e.g. identifiers) that are
tosuccess. Inthisformulation,wetreatthedefaultCodex similartothevariablesinthepromptproposalcontext,then
contextasoneofthepromptproposals. Next,wedescribe therearechancesthathmightoccursomewhereinCh. The
p
thetrainingprocedureforPPC. similarityismodeledusingamultiheadedattentionmechanism(Vaswanietal.,2017),bytreatingtheprojectedhole
Training: Foreachtargetholeh,wegenerateagroundwindow representation as a query Qh and the projected
truthvectorYh = [yh]M whichisamulti-hotvectorof
p p=1 promptproposalcontextrepresentationKh asakey. The
sizeM,whereM isthetotalnumberofpromptproposals. p
valueVhisthesameasthekey.
This vector is obtained by feeding the prompt generated p
frompromptproposalpintoCodexandthenseeingwhether
hˆ =h.Ifthereisamatch,wesaythatthepromptproposalp Qh =F ϕ (Hh), K p h =F ϕ (C p h), V p h =F ϕ (C p h)
issuccessful.Forholeh,ifapromptproposalpisapplicable

### The output from the multi-headed attention module,

2Wealsoconductedexperiments(AppendixD.3)wherewe MultiHead(Qh,K
p
h,V
p
h) is fed to module G consisting
takelinesstartingfromthe4thlineafterthehole. oftwolayersofafeedforwardnetworkwithreluactivation
4

<!-- Page 5 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
inbetween(seeAppendixCformoredetails). Theresulting
Table1. Statisticsofourdataset.
outputisthenlinearlyprojectedandasigmoidisappliedto

### Feature Train Val Test Total

getthepredictedpromptproposal.
# Repositories 19 14 14 47
yˆh =P(yh =1|Hh,Ch) #Files 2655 1060 1308 4757
p p p
(cid:16) (cid:17) #Holes 92721 48548 48288 189557
=sigmoid W G(MultiHead(Qh,Kh,Vh))+b
p p p p

### PromptComposer and omit all of them when creating target holes for our

dataset. Further,wefoundthattherepositorieswerequite
The prompt composer combines the context from the seuneven in terms of their size. To avoid large repositories
lected prompt proposal (given by PPC) with the context
dominatingthetrainingofPPC,wecappedthemaximum
normallyusedbyCodex(defaultCodexcontext)togenerate
contributionofholesfromarepositoryto10000,i.e.ifthe
the prompt. Since the total length that can be used for a
totalnumberofholesintherepositoryexceeded10000,we
promptisfixed,weadoptedadynamiccontextallocation
selected10000holesrandomlyfromthetotalholes. Please
strategywhereifthepromptproposalcontextisshorterthan
seeTable1forstatisticsofourdataset.The#Holesrepresent
itsallocatedlength,weassigntheremainingportionfrom
theholesafterdeduplicationandcapping. Forsomeofour
thepromptproposalcontexttothedefaultCodexcontext.
promptproposals,werequiresemanticinformationthatcan
The prompt proposal context is always added before the
beobtainedwithaparsetree.Weusedthetree-sitterAPIfor
defaultCodexcontext. Forallpromptproposals,weassign
Java3 thatenablesustogettheASTofafileandqueryit.
halfofthetotalcontextlengthtothepromptproposalcon-

### Sinceourpromptproposalsneedinformationatarepository

text and the remaining to the default Codex context. For
level,westoredsomeextrainformationthatallowedusto
postlines,inaddition,wealsoassignone-fourthandthreecollatetheinformationfromindividualfilesaccordingtothe
fourthsofthetotalcontextlengthtothepromptproposal
directorystructureinsidetherepository(seeAppendix3.1
context. IfthepromptproposalcontextorthedefaultCodex
formoredetails).
contextisgreaterthanthecontextlengthallocatedtoit,we
truncateit(seeAppendixB.3forourtruncationstrategies).

### ExperimentalDetails


## ExperimentsandResults PromptGeneration: WeusedtheOpenAICodexCompletionsAPIforgeneratingthepredictedholefromtheCodex

In this section, we describe how we created the dataset, model. Inparticular,weusedthecode-davinci-001
details of experiments along with different methods and enginewiththetemperaturesetto0.0andstopcriteriaasa
theirresults,andinterestingablationstudies. newline. Thecompletionlengthwas24andthemaximum
prompt length was 4072. To allow for fast computation,

### DatasetCreation weusedsimplemodelslikeCodeBERT(Fengetal.,2020)

andGraphCodeBERT(Guoetal.,2020)asourpretrained
To mitigate the effects caused by potential memorizamodels. Oneofthelimitationsofthesepretrainedmodels
tion of the code present in the dataset used for training
is that the maximum context length that can be taken as
Codex,weavoidedcoderepositoriesfromGitHub(Chen
inputbythesemodelsismuchsmallerthanthemaximum
et al., 2021). Instead, we scraped Google Code https:
contextlengthallowedbyCodex. Therefore,inPPCwhen
//code.google.com/archive/ for repositories in
weobtaintherepresentationofthepromptproposalcontext,
Java (removing the ones that matched with a repository
weneedtotruncatethecontext. Thismightleadtoomitting
on GitHub with the same name). We selected the reposiimportant parts of the prompt proposal context in certain
toriesthathadapermissivelicensegivingusatotalof47
cases. Using pretrained models that allow larger context
repositories. Wedividedtherepositoriesintotrain,validalengthormodelsthataugmentthecontext(Wuetal.,2022)
tion,andtestsplits,whereeachrepositoryinitsentiretyis
offeravenuesforfuturework. SeeAppendixD.5forresults
partofasplit. Ineachfilewithinarepository,weremove
whenweuseasmallercontextlengthwithCodex.
linesthatareeitherblankorpartofcommentsandsetthe
holepositiontobethemiddlecharacterintheline. Allthe ComputationalComplexityandScalabilityofRLPG:To
charactersfromthemiddlepositiontotheendoftheline collect the ground-truth data for training our prompt proconstitutethetargethole. posalclassifier,wequeriedtheCodexAPIforeachapplicablepromptproposalperhole(withbatchingof20queries,
Since code duplication has been shown to have adverse
wegetamaximumratelimitof400holesperminute). This
effects(Allamanis,2019),withinarepository,welookfor
amounts to ∼150k queries to get the labels for the trainfiles that are exact replicas of each other but placed in a
different folder. We mark all such copies as duplicates 3https://github.com/tree-sitter/tree-sitter-java
5

<!-- Page 6 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
ingdata,∼80kqueriestogetthelabelsforthevalidation
Table2. PerformanceoftheoraclerelativetoCodex.
data, making a total of ∼ 230k queries for training, i.e.,

### Data SuccessRate SuccessRate Rel.↑

1.63queriespertargethole. Thecomputationalcomplexity

### Split Codex(%) Oracle(%) overCodex(%)

of training our larger RLPG-R variant (3.6M parameters,
141269holes,and9.19minutesperepochonasingleTesla Train 59.78 80.29 34.31
V100GPU)ismuchsmallerthanfinetuningallorsomepart Val 62.10 79.05 27.28
ofCodex(175Bparameters). Duringinference,weneedto Test 58.73 79.63 35.58
calculatetherepo-levelstatisticsjustonceandallthesubsequentholecompletionsintherepocanutilizethiscached
information, incurring no additional computational comdocuments. This serves as a non-learned retrieval
plexity. BesidestrainingthePPC,allourexperimentswere
methodthatmakesuseofourpromptproposals.
performedonaCPUwith8GBRAM.Ourpromptproposals

## File-levelBM25: Sameasabove,exceptthatinstead

arebasedonconceptssuchaspostlines,imports,similar
of using our prompt proposal contexts, search docunamefiles,methodnames,andidentifiersthatarequitegenments consist of full context from other files in the
eral and applicable to other programming languages. In
repository.
additiontotheexistingpromptproposals,ourframework

## Random: For each target hole, select a context ranprovidestheflexibilitytoincorporatenewpromptproposdomlyfromanywhereintherepository.

als. SincethecostofretrainingRLPGwiththeextended

## RandomNN:SameasRandom,exceptthatamongst

promptproposalsisextremelylow(muchlowerthanfinetunthe randomly chosen contexts, we take the nearest
ingCodexwiththenewpromptproposals),ourframework
neighboursoftheholewindowintherepresentation
canbeusedtomakeinterventionsontheLLMtoaddress
spaceofapretrainedmodel. Thisisanalogoustothe
observedweaknessesaslongastheinterventioncanbeextechniqueusedinLiuetal.(2022).
pressedasapromptproposalthataddsthemissingcontext

## Identifier Usage: For each target hole, we take the

totheLLM.Asopposedtotechniquesthatperformprompt
closestidentifierandtakeusagewindowsofthatidenengineering in the latent space and require access to the
tifier from everywhere in the repository. The usage
weightsoftheLLMsuchasLi&Liang(2021),RLPGfawindowconsistsoftwolinesaboveandtwolinesbecilitatesexpressingintentintheformofpromptproposals
lowtheusageline,includingtheusageline. Wecan
thatareintuitiveforhumans,easytounderstand,anddonot
ranktheusagewindowseitherrandomly(random)or
requireaccesstotheweightsoftheLLM.
based on the nearest neighbour distance to the hole
Methods: Weexperimentedwiththefollowingmethodsfor windowintherepresentationspace(NN).
generatingtheprompt:

## Codex: UsingthedefaultcontextfromCodexasthe Thelastfourmethodshelpusunderstandtheperformance

entireprompt. whenacontextotherthanthepromptproposalcontextis

## Oracle: Usingtheground-truthvectorYh(mentioned used. Togenerateapromptusingthesemethods,wetake

in Section 2.2). The prompt generated corresponds 50%ofthecontextfromthesefollowedbythedefaultCodex
tousinganyofthesuccessfulpromptproposals(i.e., contextthattakesuptheremainingcontextlength. Forthe
yh = 1). Since this information is not available at NNbaselines,weuseCodeBERT(Fengetal.,2020)asthe
p
inference,theoraclerepresentsanupperbound. pretrainedmodel. Thecontextsaretakenintheincreasing

## FixedPromptProposal: Usingthemostsuccessful orderofthenearestneighbourdistancesuntilweexhaustthe

promptproposalforalltargetholes. Thiswaschosen allocatedcontextlength. RLPG-BM25helpsusunderstand
based on the performance on the validation set and theroleofPPC.SeeAppendixC.3formoredetailsonthe
correspondedtotaking75%ofthetotalcontextlength implementationofthesemethods.
frompostlinesinthecurrentfile.
EvaluationMetric: AsmentionedinSection2.2,tomea-

## RLPG-HandRLPG-R:Usingthepromptproposal

suresuccess,weuseanexactmatchbetweenthepredicted
predicted by the RLPG-H and RLPG-H variants of
holestringgeneratedbyCodexandthetargetholestring.

### PPC. The selected prompt proposal corresponds to

Inourexperiments,wereportthepercentageofsuccessful
takingtheargmaxofthepredictedprobabilitiesover
holesdividedbythetotalnumberofholesforeachsplit. We
differentpromptproposals.
willcallthissuccessrate(SR)goingforward.

## RLPG-BM25: InsteadofusingPPCtorankprompt

proposals, use the scores obtained by BM25 (Jones

### Results

etal.,2000)toselectthebestpromptproposal. The
scoresarecalculatedwiththeholewindowbeingthe Inthissection,wepresenttheresultsofthefollowingtwo
queryandpromptproposalcontextsbeingthesearch researchquestionsexploredinthepaper:
6

<!-- Page 7 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
Table3.SuccessRate(SR)ofdifferentmethodsonthetestdata
whenaveragedacrossallholes.
78
Method SuccessRate(%) Rel.↑(%)
76
Codex(Chenetal.,2021) 58.73 -
Oracle 79.63 35.58 74
Random 58.13 -1.02 72
RandomNN 58.98 0.43
70

### File-levelBM25 63.14 7.51

IdentifierUsage(Random) 64.93 10.55 1 2 3 4 5 6 7 8 9 1011121314151617181920
k
IdentifierUsage(NN) 64.91 10.52
FixedPromptProposal 65.78 12.00

## Rlpg-Bm25 66.41 13.07


## Rlpg-H 68.51 16.65


## Rlpg-R 67.80 15.44

• [RQ1]-Isitusefultogenerateapromptthatiscomposed
ofcodecontextthatisdifferentfromthedefaultCodex
context? Ifyes,whatcontextcanbeuseful?
• [RQ2]-Foreachtargethole,isthereawayofautomaticallyselectingtheprompt? Ifyes,howdoesthissystem
performrelativetoCodex?

### RQ1-PerformanceofPromptProposals: Wefoundthat

combiningthepromptproposalcontext(contextfromother
filesintherepository)withthedefaultCodexcontextled
tosubstantialimprovementinperformance. Table2shows
theperformanceofanoracleconstructedfromourprompt
proposals. We see that across all data splits, the prompt
proposals contribute to significantly large improvements
overCodex(upto36%fortestsplit). Theseresultsmight
seemsurprisingasCodexhasnotbeentrainedonprompts
thatconsistofcontextotherthanthedefaultCodexcontext.

### Whatmakesthisresultmoresurprisingisthatinmostof

thecases,thepromptconsistsofmashed-upcontextwithout
logicalorderingthatmaynotevenlooklikeasemantically
meaningfulchunkofcode(e.g. listofstringliteralsfrom
asiblingfilefollowedbythedefaultCodexcontextorpost
linesplacedbeforethedefaultCodexcontextasopposed
to after). These results might suggest that as long as the
relevant context (in our case repo-level knowledge in the
form of prompt proposals) is present in any form in the
prompt,itcanbequiteeffective.

### RQ2-PerformanceofPPC:Havingseenpromiseinour

promptproposals,next,wepresenttheresultsofRLPG.Table3presentsthesuccessratesalongwiththepercentageof
relativeimprovementsforthetestdata. Thesuccessrateis
calculatedbyaveragingacrossallholesinthetestdata(holewise). Ascanbeseenfromthetable,alltheRLPGvariants
as well as the fixed prompt proposal improve the performancesignificantlyoverCodex. Therandombaselinesare
either worse or on par with Codex. Identifier usage is a
)%(
etaR
sseccuS
laV Fixed Prompt Proposal (repo-wise)

### RLPG-R (repo-wise)

Fixed Prompt Proposal (hole-wise)
RLPG-R (hole-wise)
60 Cur Sib
50 SimN

### ImpSimN

40 ImpSib

### Imp

30 PaCl
ImpPaCl
20 ChCl
ImpChCl
10
0
Figure2.(Top) Variation of RLPG and Fixed Prompt Proposal
with#attempts(k), whenaveragedoverindividualrepositories
(repo-wise)andallholes(hole-wise);(Bottom)Meansuccessrates
ofdifferentpromptsourceswhentheyareapplicable.
goodbaselinebutstillperformsworsethaneitherthefixed
prompt proposal or RLPG. We see that File-level BM25
showsthateventhoughbetterthanCodex,itperformsinferiortothemethodsthatusesomesemanticallymeaningful
notionofcontext(e.g. methodbodiesorfielddeclarations).

### However,whenwecombineBM25withpromptproposal

contexts (RLPG-BM25), the performance improves a lot.
AllRLPG-basedmethodsarebetterthanfixedpromptproposal, showing the value of generating example-specific
promptsusingRLPG.However,boththelearnedvariantsof

### RLPG,i.e.,RLPG-HandRLPG-RoutperformtheRLPG-


### BM25, highlightingtheimportanceoflearningPPC.See

Appendix D.1 and Appendix D.7 for the performance of
allmethodsacrossindividualrepositories. Notethateven
thoughweconsideridentifierusageasaseparatebaseline,
onecouldconsideritasoneofthepromptproposalsleading
tofurtherimprovedperformanceofRLPG.

### Despiteoureffortsofavoidingoverlap,sincethetraining

dataforCodexisnotexactlyknown,theremightbeapossibility that part of our Google Code data is part of the
trainingdataforCodex. Eveniftherewereanoverlap,we
want to point out that since Codex has been trained with
the default Codex context, during inference, it would be
morebeneficialforittousethedefaultCodexcontextinthe
prompt(ratherthanthecontextfromthepromptproposals
oranyothercontextfromothermethods). Thismeansthat
7

<!-- Page 8 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
underthisscenario,ourevaluationwouldbemoregenerous 26.62%relativeimprovement.
totheCodexbaseline,leadingtoresultsmoreinfavorof
Experimentswithcode-cushman-001: Toinvestigate
theCodexbaselinethanothermethodswehaveused.
whethertheimprovementsachievedwithRLPGareappli-
Variationwith#attempts: Imagineascenariowherewe cabletoadifferentcodemodel,weconductedexperiments
haveahuman-in-the-loopwhohasbeengivenkattemptsto onthecode-cushman-001modelfromOpenAI5.This
prompttheLLMandthenchooseoneofthekpredictions. modelsupportsacontextlengthofupto2048tokens,which
Wewantedtoseehowtheperformanceofourframework is half the context length of code-davinci-001 and
varieswith#attemptsunderthissetting. Thiscorrespondsto isexpectedtoberelativelysmaller(seeAppendixA.2of
usingkpromptsgeneratedwithtop-kpromptproposals(one Rajkumaretal.,2022).
promptperproposal)andmarkingsuccessifanyofthek
For evaluating RLPG, we choose the prompt propromptsleadtosuccess. ThetoppartofFigure2showsthe
posal contexts based on the predictions from our
variationofSRoverthevalidationdatawiththevalueofk.
trained RLPG models (trained on labels obtained from

### ForRLPG,thetop-kpromptproposalswerechosenbased

code-davinci-001). These contexts are then used
onthedecreasingorderofprobabilitiesgivenbyPPC.For
aspromptsforcode-cushman-001inordertogetthe
thefixedpromptproposal,thetop-kpromptproposalswere
completions. AsshowninTable5,onthetestset,RLPG-
decided based on decreasing order of success rate of the

### H gets a relative improvement of 10.87% and RLPG-R

individualpromptproposalsonthevalidationdataset. From
getsarelativeimprovementof10.95%overusingtheprior
thefigure,wenoticethatasweincreasethevalueofk,the
context in the file. These results suggest that RLPG has
performanceincreasesgraduallyatfirstandthensaturates
thepotentialtoshowimprovementsacrossdifferentcode
towardstheoracleperformance(79.05%forvaldata). This
completion models. We expect that having RLPG modbehaviour is observed for both fixed prompt proposal as
els trained on labels from code-cushman-001 would
wellasRLPG.However,weseethatforthesamevalueof
improve the results even further. However, in our opink,thesuccessrateforRLPGishigherindicatingthatPPC
ion,thefactthatwecanuseasingleRLPGmodel(trained
learnsausefulrankingofthepromptproposalcontextsthat
on code-davinci-001) to get improvements for two
canscalewellwiththe#attempts.
differentcodecompletionmodels(code-cushman-001
Performance based on Prompt Proposals: The bottom andcode-davinci-001)isquiteinteresting.
part of Figure 2 shows the mean success rate of prompt
sources, where success is counted only when the correspondingpromptsourceisapplicable. Fromthefigure,we Table5. SuccessRate(SR)withcode-cushman-001.
seethatthecurrentfileisthemostimportantpromptsource. Method SuccessRate(%) Rel.↑(%)
Closelyfollowingaresibling filesandsimilar namefiles. code-cushman-001 58.40 -
We see that all prompt sources have non-zero chances of

## Rlpg-H 64.74 10.87

success,highlightingtheusefulnessofeachpromptsource.

## Rlpg-R 64.79 10.95

SeeAppendixD.2forasimilarbreakdownbasedonprompt
contexttypeandAppendixEforanalysisofsamplecases
thatleadtosuccessandfailureforRLPG.

## RelatedWork

Table4. Editdistancebasedperformanceevaluation. LLMs for Code: Recently, there has been a lot of work
Method NormalizedEditDistance(%) Rel.↑(%) aroundlargelanguagemodelsofcode. Decoder-onlymodelscorrespondtogeneratingcodefromlefttoright(Chen

### Codex 30.73 -

et al., 2021; Austin et al., 2021; Wang & Komatsuzaki,
RLPG-H 22.55 26.62 2021;Blacketal.,2022;Xuetal.,2022a;Friedetal.,2022).

## Rlpg-R 23.00 25.14

Encoder-onlymodelsuseamaskedlanguagemodelingobjective(Fengetal.,2020;Guoetal.,2020;Kanadeetal.,
2020). Wealsohaveencoder-decodermodelsthatgenerally
EditDistanceasaMetric: Inadditiontomeasuringstring
useabidirectionalencodingofacontexttodecodeaseries
exactmatch,wealsoassesstheperformanceofRLPGusing
ofmaskedtokens(Wangetal.,2021b;Lietal.,2022).
thecharacter-leveleditdistance4asametric.Table4reports
theaveragecharacter-leveleditdistancenormalizedbythe Repo-LevelInfo: Hellendoorn&Devanbu(2017)propose
totalnumberofcharactersinthetargethole(lowerisbetter). anestedn-grammodelthatutilizesalocality-basedcache
WeseethatbothRLPGvariantsshowsignificantrelative wherethelocalityconsistsofalldirectoriesfromtherootof
improvementsoverCodexwithRLPG-Hgettingashighas theproject(inclusiveofthecurrentfile). Zhangetal.(2021)
4https://pypi.org/project/editdistance/ 5https://platform.openai.com/docs/models/codex
8

<!-- Page 9 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
usestheparentclasstogeneratethecommentsforthechild 5.Discussion
class. Pashakhanloo et al. (2022b;a) convert the reposi-

### Wenotethatcode-completionsystemsusedinconjunction

tory into a relational database and propose a graph-walk
with LLM should be deployed with caution (Chen et al.,
basedmechanismforpruningtheunrelatedcontextwhereas
2021). Blindtrustinthesesystemsmayleadtopotential
Wangetal.(2021a)proposesamulti-relationalgraphneunegativeimpact,astheremightbecaseswherethegenerated
ralnetworkthatusesinter-classandintra-classcontextsto
code is insecure (Perry et al., 2022) or contains sensitive
obtaincodesummaries. Lyuetal.(2021)incorporatesthe
information. Afterthesubmissionofthispaper,LLMswith

### API-dependencygraphinaLSTM-basedSeq2Seqmodelto

largerinputcontextlengthshavebeenintroduced,suchas
assistincodegenerationwhereas,Zhouetal.(2023)trainsa
GPT-4 6 which supports 32k tokens. With this expanded
modeltoaugmentcodedocumentationtoanaturallanguage
contextlength,onemightconsiderincludingtheentireconintent.Xuetal.(2022b)incorporatethreetypesofstructural
tentoftherepositoryintheprompt. However,inpractice,
localityfeatureswhiletrainingthekNN-LM(Khandelwal
softwarerepositoriesareoftenmuchlonger. Inourdataset
etal.,2020). Thesefeaturesarebinaryvariablesthatcor-
(afterdeduplication),weobservedthat70.22%ofrepositorespondtothepresenceorabsenceofasimilarhierarchy.
riescontainmorethan32ktokens. Itisworthnotingthat

### Thethreelevelsofhierarchyare(a)siblingfile,(b)filein

apart from the current repository, there are other sources
thesamerepo(c)nohierarchy. Incontrast,wehaveamuch
ofrelevantcontext,suchasAPIdocumentation,tutorials,
richersetofpromptproposalsincorporatingthesemantics
orrelatedrepositories,thatcanaidincodeautocompletion.
andstructureoftherepository. Also,weassumeblack-box

### RLPGoffersamechanismtoincorporatetheseadditional

access to the model and generate a prompt for the LLM
sourcesofcontextthroughnewpromptproposals. TherewithoutperforminganyfinetuningoftheLLM.
fore,regardlessofthecontextlengthofthecode-generating
Prompt Generation: There have been promising works model,RLPGprovidesavaluableapproachtodetermining
aroundpromptgenerationtechniquesinNLP.Broadly,there whichcontextsarerelevanttoincludeintheprompt. With
are two categories of automatic prompt generation tech- the increased context length in GPT-4, we anticipate less
niques. Thefirstcategorycorrespondstoproducingcontinu- truncationofpromptproposalcontexts,potentiallyleading
ous/softpromptswherethepromptisdescribedinthelatent toevengreaterimprovementswithRLPG.
spaceofalanguagemodel(Li&Liang,2021;Qin&Eisner,

### Inconclusion,wepresentRLPG,aframeworkthatlearns

2021;Braggetal.,2021;Lesteretal.,2021;Liuetal.,2021).
to automatically generate prompts conditioned on the ex-
Forexample,Prefix-Tuning(Li&Liang,2021)addsaprefix
ample,withoutrequiringaccesstotheweightsoftheLLM.
totheLMthatcanbelearnedbyfinetuningonexamples
RLPGutilizesthestructureoftherepositoryaswellasthe
fromthedownstreamtask. Thesecondcategoryproduces
contextfromotherfilesintherepositoryusingasetofeasydiscretepromptswherethepromptisatextstringthatcanbe
to-understandpromptproposals. Inthiswork,wearetaking
interpretedbyahuman(Shinetal.,2020;Gaoetal.,2021;
contextfromonlyonepromptproposal. Forfuturework,
Schick&Schütze,2021). Forexample,Autoprompt(Shin
wewanttolearnamodelthatcanautomaticallycomposea
etal.,2020)generatespromptusingafixedtemplateconsistpromptfrommultiplepromptproposals(seeAppendixD.4
ingoftriggertokens. Thetriggertokensaresharedacross
forpromisinginitialresults). Otherinterestingdirections
allinputsanddetermined byagradient-guidedsearchinincludeincorporatingtheuser’sfeedbackinRLPGandexvolvingtheLM.Ourworkfallsinthecategoryofdiscrete
tendingRLPGtomulti-linecodeauto-completion.
promptgenerationtechniquesasweproduceapromptconsisting of code tokens that can be easily interpreted by a
human. However,incontrasttopriorworksthatuseaset Acknowledgements
of fixed templates for all examples, we learn to produce
Hugo Larochelle would like to acknowledge the support
promptsconditionedoneachexample. Anotherimportant
of Canada CIFAR AI Chairs for research funding. The
distinctionisthatwedonotrequireaccesstotheweights
authors would like to thank Google Cloud for providing
oftheLM.Aconcurrentworkasours,(Wangetal.,2022)
computeresourcesrequiredforthisproject. Wewouldalso
studiestheroleofprompt-tuningwhencomparedtofineliketoextendourthankstoBreandanConsidineforhelpin
tuning for code translation, defect localization, and code
crawlingtheGoogleCodedataarchives,toJustineGehring,
summarization. However,theirtechniquerequiresaccess
Avinash Bhat, and Breandan Considine for helping with
totheweightsoftheLLMandtheyperformexperiments
resources for running experiments; and David Bieber for
overmodelsthataremuchsmallerinscalethanCodex. To
feedbackandcommentsonthedraftthathelpedusimprove
thebestofourknowledge,ourworkisthefirsttoexplore
writing. Finally,wewouldliketoacknowledgeOpenAIfor
automaticpromptgenerationinablack-boxaccesssetting
providingaccesstotheCodexAPI.
inthedomainofsourcecode.
6https://openai.com/product/gpt-4
9

<!-- Page 10 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
References Gao,T.,Fisch,A.,andChen,D. Makingpre-trainedlanguagemodelsbetterfew-shotlearners. InProceedings
Allamanis,M.Theadverseeffectsofcodeduplicationinmaofthe59thAnnualMeetingoftheAssociationforComchinelearningmodelsofcode.InProceedingsofthe2019
putational Linguistics and the 11th International Joint

### ACMSIGPLANInternationalSymposiumonNewIdeas,


### ConferenceonNaturalLanguageProcessing(Volume1:

New Paradigms, and Reflections on Programming and
LongPapers),2021.
Software.AssociationforComputingMachinery,2019.
Guo,D.,Ren,S.,Lu,S.,Feng,Z.,Tang,D.,Liu,S.,Zhou,

### Austin,J.,Odena,A.,Nye,M.,Bosma,M.,Michalewski,

L.,Duan,N.,Svyatkovskiy,A.,Fu,S.,etal. Graphcode-
H.,Dohan,D.,Jiang,E.,Cai,C.,Terry,M.,Le,Q.,etal.
bert: Pre-training code representations with data flow.
Program synthesis with large language models. arXiv
arXivpreprintarXiv:2009.08366,2020.
preprintarXiv:2108.07732,2021.

### He,K.,Zhang,X.,Ren,S.,andSun,J. Deepresiduallearn-

Ba,J.L.,Kiros,J.R.,andHinton,G.E.Layernormalization.
ingforimagerecognition. InProceedingsoftheIEEE
arXivpreprintarXiv:1607.06450,2016.
conferenceoncomputervisionandpatternrecognition,
Black, S., Biderman, S., Hallahan, E., Anthony, Q., Gao, 2016.

### L.,Golding,L.,He,H.,Leahy,C.,McDonell,K.,Phang,

Hellendoorn, V. J. and Devanbu, P. Are deep neural net-
J.,Pieler,M.,Prashanth,U.S.,Purohit,S.,Reynolds,L.,
works the best choice for modeling source code? In

### Tow,J.,Wang,B.,andWeinbach,S. GPT-NeoX-20B:An

Proceedingsofthe201711thJointMeetingonFoundaopen-sourceautoregressivelanguagemodel. InProceedtionsofSoftwareEngineering,2017.
ingsoftheACLWorkshoponChallenges&Perspectives
inCreatingLargeLanguageModels,2022.

### Jiang, E., Toh, E., Molina, A., Olson, K., Kayacik, C.,

Bragg,J.,Cohan,A.,Lo,K.,andBeltagy,I. FLEX:Unify- Donsbach,A.,Cai,C.J.,andTerry,M. Discoveringthe
ingevaluationforfew-shotNLP. InAdvancesinNeural syntaxandstrategiesofnaturallanguageprogramming
InformationProcessingSystems,2021. withgenerativelanguagemodels. InProceedingsofthe
2022CHIConferenceonHumanFactorsinComputing
Brown,T.,Mann,B.,Ryder,N.,Subbiah,M.,Kaplan,J.D., Systems,2022.

### Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G.,

Askell,A.,Agarwal,S.,Herbert-Voss,A.,Krueger,G., Jones, K. S., Walker, S., and Robertson, S. E. A proba-
Henighan,T.,Child,R.,Ramesh,A.,Ziegler,D.,Wu,J., bilisticmodelofinformationretrieval: developmentand
Winter,C.,Hesse,C.,Chen,M.,Sigler,E.,Litwin,M., comparativeexperiments-part1. Inf.Process.Manag.,
Gray, S., Chess, B., Clark, J., Berner, C., McCandlish, 2000.

### S.,Radford,A.,Sutskever,I.,andAmodei,D. Language

Kanade, A., Maniatis, P., Balakrishnan, G., and Shi, K.
models are few-shot learners. In Advances in Neural
Learningandevaluatingcontextualembeddingofsource
InformationProcessingSystems,2020.
code. InProceedingsofthe37thInternationalConfer-
Chen,M.,Tworek,J.,Jun,H.,Yuan,Q.,Pinto,H.P.d.O., enceonMachineLearning,2020.

### Kaplan,J.,Edwards,H.,Burda,Y.,Joseph,N.,Brockman,

G., etal. Evaluatinglargelanguagemodelstrainedon Khandelwal,U.,Levy,O.,Jurafsky,D.,Zettlemoyer,L.,and
code. arXivpreprintarXiv:2107.03374,2021. Lewis,M.Generalizationthroughmemorization:Nearest
neighborlanguagemodels. InInternationalConference
Chowdhery,A.,Narang,S.,Devlin,J.,Bosma,M.,Mishra, onLearningRepresentations,2020.

### G., Roberts, A., Barham, P., Chung, H.W., Sutton, C.,

Gehrmann,S.,etal. Palm: Scalinglanguagemodeling Kingma,D.P.andBa,J. Adam: Amethodforstochastic
withpathways. arXivpreprintarXiv:2204.02311,2022. optimization. InInternationalConferenceonLearning
Representations,2015.

### Feng, Z., Guo, D., Tang, D., Duan, N., Feng, X., Gong,

M., Shou, L., Qin, B., Liu, T., Jiang, D., et al. Code- Kojima,T.,Gu,S.S.,Reid,M.,Matsuo,Y.,andIwasawa,
bert: Apre-trainedmodelforprogrammingandnatural Y. Largelanguagemodelsarezero-shotreasoners. arXiv
languages. arXivpreprintarXiv:2002.08155,2020. preprintarXiv:2205.11916,2022.
Fried,D.,Aghajanyan,A.,Lin,J.,Wang,S.,Wallace,E., Lester,B.,Al-Rfou,R.,andConstant,N.Thepowerofscale
Shi,F.,Zhong,R.,Yih,W.-t.,Zettlemoyer,L.,andLewis, forparameter-efficientprompttuning. InProceedingsof
M. Incoder: Agenerativemodelforcodeinfillingand the2021ConferenceonEmpiricalMethodsinNatural
synthesis. arXivpreprintarXiv:2204.05999,2022. LanguageProcessing,2021.
10

<!-- Page 11 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
Li,X.L.andLiang,P. Prefix-tuning: Optimizingcontinu- Reynolds,L.andMcDonell,K. Promptprogrammingfor
ouspromptsforgeneration. InProceedingsofthe59th largelanguagemodels: Beyondthefew-shotparadigm.
AnnualMeetingoftheAssociationforComputationalLin- In Extended Abstracts of the 2021 CHI Conference on
guisticsandthe11thInternationalJointConferenceon HumanFactorsinComputingSystems,2021.

### NaturalLanguageProcessing(Volume1: LongPapers),

Rombach, R., Blattmann, A., Lorenz, D., Esser, P., and
2021.

### Ommer,B. High-resolutionimagesynthesiswithlatent

Li,Y.,Choi,D.,Chung,J.,Kushman,N.,Schrittwieser,J., diffusionmodels. InProceedingsoftheIEEE/CVFCon-
Leblond,R.,Eccles,T.,Keeling,J.,Gimeno,F.,DalLago, ference on Computer Vision and Pattern Recognition,
A.,etal. Competition-levelcodegenerationwithalpha- 2022.
code. Science,2022.

### Schick,T.andSchütze,H. Exploitingcloze-questionsfor

few-shot text classification and natural language infer-
Liu,J.,Shen,D.,Zhang,Y.,Dolan,B.,Carin,L.,andChen,
ence. InProceedingsofthe16thConferenceoftheEu-

### W. Whatmakesgoodin-contextexamplesforGPT-3?

ropean Chapter of the Association for Computational
In Proceedings of Deep Learning Inside Out (DeeLIO
2022): The3rdWorkshoponKnowledgeExtractionand
Linguistics: MainVolume,2021.
IntegrationforDeepLearningArchitectures.Association
Shin,T.,Razeghi,Y.,IV,R.L.L.,Wallace,E.,andSingh,S.
forComputationalLinguistics,2022.

### AutoPrompt: Elicitingknowledgefromlanguagemodels

withautomaticallygeneratedprompts.InEmpiricalMeth-
Liu,P.,Yuan,W.,Fu,J.,Jiang,Z.,Hayashi,H.,andNeubig,
odsinNaturalLanguageProcessing(EMNLP),2020.

### G. Pre-train,prompt,andpredict: Asystematicsurveyof

promptingmethodsinnaturallanguageprocessing. ACM Shrivastava, D., Larochelle, H., and Tarlow, D. On-the-
ComputingSurveys,2023. flyadaptationofsourcecodemodels. InNeurIPS2020
WorkshoponComputer-AssistedProgramming,2020.

### Liu,X.,Zheng,Y.,Du,Z.,Ding,M.,Qian,Y.,Yang,Z.,and

Tang,J. Gptunderstands,too. arXiv:2103.10385,2021. Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I.,
andSalakhutdinov,R. Dropout: asimplewaytoprevent
Lyu,C.,Wang,R.,Zhang,H.,Zhang,H.,andHu,S. Emneuralnetworksfromoverfitting. Thejournalofmachine
beddingapidependencygraphforneuralcodegeneration.
learningresearch,2014.
EmpiricalSoftw.Engg.,2021.

### Sun,J., Liao,Q.V.,Muller,M., Agarwal,M.,Houde, S.,

Pashakhanloo,P.,Naik,A.,Dai,H.,Maniatis,P.,andNaik, Talamadupula,K.,andWeisz,J.D. Investigatingexplain-
M. Learning to walk over relational graphs of source abilityofgenerativeaiforcodethroughscenario-based
code. InDeepLearningforCodeWorkshop,2022a. design. In27thInternationalConferenceonIntelligent
UserInterfaces,2022.

### Pashakhanloo,P.,Naik,A.,Wang,Y.,Dai,H.,Maniatis,P.,

andNaik,M. Codetrek: Flexiblemodelingofcodeusing Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,
anextensiblerelationalrepresentation. InInternational L.,Gomez,A.N.,Kaiser,u.,andPolosukhin,I.Attention
ConferenceonLearningRepresentations,2022b. isallyouneed. InProceedingsofthe31stInternational

### ConferenceonNeuralInformationProcessingSystems,

Perry, N., Srivastava, M., Kumar, D., and Boneh, D. Do
2017.
userswritemoreinsecurecodewithaiassistants? arXiv
preprintarXiv:2211.03622,2022. Wang, B. and Komatsuzaki, A. GPT-J-6B: A 6 Billion Parameter Autoregressive Language Model.
Qin, G. and Eisner, J. Learning how to ask: Querying https://github.com/kingoflolz/mesh-
LMswithmixturesofsoftprompts. InProceedingsof transformer-jax,2021.
the2021ConferenceoftheNorthAmericanChapterof
theAssociationforComputationalLinguistics: Human Wang,C.,Yang,Y.,Gao,C.,Peng,Y.,Zhang,H.,andLyu,
LanguageTechnologies,2021. M.R. Nomorefine-tuning? anexperimentalevaluation
ofprompttuningincodeintelligence. InProceedingsof
Ramesh,A.,Dhariwal,P.,Nichol,A.,Chu,C.,andChen, the30thACMJointEuropeanSoftwareEngineeringCon-
M. Hierarchicaltext-conditionalimagegenerationwith ferenceandSymposiumontheFoundationsofSoftware
cliplatents. arXivpreprintarXiv:2204.06125,2022. Engineering,2022.
Reed, S., Zolna, K., Parisotto, E., Colmenarejo, S. G., Wang,Y.,Shi,E.,Du,L.,Yang,X.,Hu,Y.,Han,S.,Zhang,
Novikov, A., Barth-Maron, G., Gimenez, M., Sulsky, H.,andZhang,D. Cocosum: Contextualcodesumma-
Y.,Kay,J.,Springenberg,J.T.,etal. Ageneralistagent. rizationwithmulti-relationalgraphneuralnetwork.arXiv
arXivpreprintarXiv:2205.06175,2022. preprintarXiv:2107.01933,2021a.
11

<!-- Page 12 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode

### Wang, Y., Wang, W., Joty, S., and Hoi, S. C. Codet5:

Identifier-awareunifiedpre-trainedencoder-decodermodelsforcodeunderstandingandgeneration.InProceedings
ofthe2021ConferenceonEmpiricalMethodsinNatural
LanguageProcessing,2021b.

### Wei, J., Wang, X., Schuurmans, D., Bosma, M., Chi, E.,

Le,Q.,andZhou,D. Chainofthoughtpromptingelicitsreasoninginlargelanguagemodels. arXivpreprint
arXiv:2201.11903,2022.
Wu,Y.,Rabe,M.N.,Hutchins,D.,andSzegedy,C. Memorizing transformers. In International Conference on
LearningRepresentations,2022.
Xiao, W., Beltagy, I., Carenini, G., and Cohan, A.

### PRIMERA:Pyramid-basedmaskedsentencepre-training

for multi-document summarization. In Proceedings of
the60thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1: LongPapers),2022.

### Xu,F.F.,Alon,U.,Neubig,G.,andHellendoorn,V.J. A

systematicevaluationoflargelanguagemodelsofcode.
arXivpreprintarXiv:2202.13169,2022a.
Xu,F.F.,He,J.,Neubig,G.,andHellendoorn,V.J. Capturingstructurallocalityinnon-parametriclanguagemodels.
InInternationalConferenceonLearningRepresentations,
2022b.
Zhang,J.,Panthaplackel,S.,Nie,P.,Mooney,R.J.,Li,J.J.,
andGligoric,M. Learningtogeneratecodecomments
fromclasshierarchies. arXivpreprintarXiv:2103.13426,
2021.
Zhou, S., Alon, U., Xu, F. F., Jiang, Z., and Neubig, G.
Docprompting: Generatingcodebyretrievingthedocs.
InInternationalConferenceonLearningRepresentations,
2023.
12

<!-- Page 13 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode

### A.DatasetCreationDetails


### A.1.CreationofHoleCompletionData

Tocollecttheholecompletiondata,wescrapedGoogleCode7forrepositoriestaggedwiththelanguage“Java”. Thenwe
deduplicatedrepositoriesbysearchingforamatchingrepositorywiththesamenameonGitHub. Forthoserepositories
withzeromatchingnamesonGitHub,wedownloadedthearchiveandextractedthesourcecode(preservingthedirectory
structure). Next,wetriedtodeterminethelicensesofallrepositoriesbyeitherlookingforaLICENSEfileormatchingwith
keywords"license","copyright","mit",etc. Forreposforwhichourprocesswasabletocomeupwithaknownlicense,we
selectedtheoneshavingapermissivelicense,i.e.,MIT,ApacheV2andBSD.Thiswasfollowedbyremovingfilesthatare
exactduplicatesofeachotherwithinarepo. Oneofthereasonswefoundthisinter-repositoryduplicationmaybebecause
sometimesdevelopersadoptlousypractiseswhereinsteadofdeclaringapackageandimportingfunctions,theysimply
copy-pastethedesiredfileintothecurrentfolder. Thetargetholescomingfromanyoftheduplicatefilesdonotformpartof
theholecompletiondataset. However,thesefilesmightbeusedtocontributetopromptproposalcontextforcompletinga
targetholeinanon-duplicatefile. Wefeltcomfortablewiththischoicesincewewouldn’twanttopredictatargetholeina
duplicatefile,butwecanstillusethecontextfromtheduplicatefiletopredicttheholeinafilethatisnotitsduplicate(e.g.
inasiblingfile). Fortheremainingfiles,wetookeachlinethatisnotablankedlineoracommentandchosethemiddle
characterastheholeposition,i.e.,allthecharactersfromthemiddleofthelinetotheendofthelineformthetargethole. To
avoidlargereposhavingstrongbiasonourpromptproposalclassifier,wecappedthecontributionfromeachrepotobea
maximumof10000holes. Ifthenumberofholesintherepoexceeds10000,werandomlyselect10000holes. Tokenization
wasdoneusingthesuggestedtokenizerfromOpenAI8.

### A.2.CreationofDataforRepo-LevelPromptProposals

Weusedthetree-sitterAPIforJava9togettheparse-treeofanindividualfileinarepo. Togetinformationatarepo-level,
foreachfileintherepo,westoredthefollowinginformation:
1. listofallclassnamesinthefile. Thishelpedustogettheparentorchildclassfilecorrespondingtoagivenparentor
childclass.
2. thefilecorrespondingtoeachimportstatement.
3. foreachimportstatementinthefile,thepositioninthefilewheretheimportisused. Thisisusedforrankingthefiles
basedontheheuristicsmentionedinTable6.
4. listofsiblingfiles
5. listofsimilarnamefiles. Thiswasdonebysplittingthefilenamesbasedoneithercamel-caseorunderscore. Ifthe
sub-partsoftwofilesmatch,thentheyaresaidtohavesimilarname.
Theabovemeta-datawascalculatedonlyonceforeachrepo. Thesubsequentholecompletionscanusethesamecached
information. Inpractise,wecanuseahashtostoreandretrievethisinfoefficiently. Forapromptproposal,giventheprompt
source,wefirstobtainasinglefileorrankedlistoffiles(seeTable6)usingtheinfointheparsetreeinconjugationwith
theaboverepo-levelmeta-data. Allthepromptproposalcontexttypeinformation(MN,MNB,SL,I,TI,FD)canthenbe
obtainedbyqueryingtheparsetreeoftheselectedfile.

### B.PromptProposalDetails


### B.1.Rankingoffilesbasedonpromptsource

InTable6,weprovidedetailsofhowweselectfilesforagivenpromptsource. Dependingonthepromptproposal,weget
eitherasinglefileoralistoffilesrankedbasedonsomecriteria. Forexample,ifthepromptsourceisImport,wetakeallthe
importstatementsusedinthecurrentfileandidentifythelocationinthecurrentfilewherethecorrespondingimportshave
beenused. Accordingtoourheuristic,thecloseristheimportusagetotheholeposition,themorelikelyitisfortheprompt
proposalcontextcomingfromthecorrespondingimportfiletobemorerelevant(topredictthetargethole). Wegetaranked
listofimportfilessortedbasedonincreasingorderofdistance(i.e.,numberoflines)betweentheimportusageandthehole
7https://code.google.com/archive/
8https://huggingface.co/docs/transformers/model_doc/gpt2#transformers.GPT2TokenizerFast
9https://github.com/tree-sitter/tree-sitter-java
13

<!-- Page 14 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
position. Westartbytakingallofthepromptproposalcontextfromthefirstfileintherankedlistandthenkeepiteratingthe
rankedlistuntileitherthetotalcontextlengthallocatedtothepromptproposalgetsexhaustedorwereachtheendofthe
rankedlist.
Table6. Selectingfilesforapromptsource

### PromptSource FileRanking

Current filewiththetargethole. Returnsasinglefile.
ParentClass filethatcontainstheparentclassthatoccursclosesttothetargethole. Returnsasingle
file.
Import files with the corresponding import usage ranked based on the proximity to the hole.
Returnsarankedlistoffiles.
Sibling fileswithimportusagecommontothecurrentfileandthesiblingfile,rankedbasedon
theproximitytothehole. Thetotalnumberofcommonimportsbetweenthecurrentand
thesiblingfileisusedasatie-breaker. Returnsarankedlistoffiles.
SimilarName fileswithimportusagecommontothecurrentfileandthesimilarnamefile,rankedbased
ontheproximitytothehole. Thetotalnumberofcommonimportsbetweenthecurrent
andthesimilarnamefileisusedasatie-breaker. Returnsarankedlistoffiles.
ChildClass fileswithimportusagecommontothecurrentfileandthechildfile,rankedbasedonthe
proximitytothehole. Thetotalnumberofcommonimportsbetweenthecurrentandthe
childclassfileisusedasatie-breaker. Returnsarankedlistoffiles.
ImportofSibling import files ranked based on the frequency of usage in all the sibling files. Returns a
rankedlistoffiles.
ImportofSimilarName importfilerankedonthebasisoffrequencyofusageinallthesimilarnamefiles. Returns
arankedlistoffiles.
ImportofParentClass importfilerankedonthebasisoffrequencyofusageinalltheparentclassfiles. Returns
arankedlistoffiles.
ImportofChildClass importfilerankedonthebasisoffrequencyofusageinallthechildclassfiles. Returnsa
rankedlistoffiles.

### B.2.ExamplesofPromptContextType


### Weprovideexamplesofeachofourpromptcontexttypebelow:


## Post Lines (PL) : For the example shown in Figure 1 of the main paper, post lines will take all the lines after the line mg.InitializeToAssignment(CurrentAssignments()) till we reach the end of the file

(AffinityPropagation.java).

## Identifiers (I): Identifiers are the names of variables used in the code. For example, for the prompt proposal

context taken from the imported file shown in Figure 1 in the main paper (highlighted in violet), identifiers are
InitializeToAssignment(line1), a (line1), currentAssignment_ (line2), a(line2), clone(line
2), alreadyInitialized_ (line3), justOneRound_(line4).

## Type Identifiers (TI): Type Identifiers define the type of an identifier. For example, in the code snippet class

DPAffinityPropagation extends AffinityPropagation , [AffinityPropagation is labeledasatypeidentifier. SimilarlyinthesnippetDPAPParameters parameters_;, DPAPParameters isa
typeidentifier.

## Field Declarations (FD): The variables of a class type are introduced by field declarations. For example,

double[][] mHijMujT_; and MessageValuePair[][] sortedMHijMujTs_; are examples of
fielddeclarations.

## String Literals (SL): A string literal is the sequence of characters enclosed in double-quotes. For

example, in the code snippet, System.err.println("DPAP load Warning: unknown
parameter " + entries[0] + ", value = " + entries[1]);, we have two string literals:
(a) "DPAP load Warning: unknown parameter " ;(b) ", value = " .

## Method Names (MN): For the example shown in Figure 1 of the main paper,

14

<!-- Page 15 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
public void InitializeToAssignment(int[] a) isthemethodnamepromptcontexttype.

## MethodNamesandBodies(MNB):FortheexampleshowninFigure1ofthemainpaper,theparthighlightedinviolet

representsthemethodnamesandbodies.

### B.3.TruncationStrategiesforPromptProposalContext

Ifthepromptproposalcontextisgreaterthanthecontextlengthallocatedtoit,thenweneedtotruncatethepromptproposal
context. Wefollowedthebelowtwoschemesfortruncatingcontext:
• front: Wetruncatethecontextfromthefront. ThisisusedforallpromptsourcesexceptParentClassandwhenwetake
PLfromCurrent.
• back: Wetruncatethecontextfromtheback. ThisisusedwhenthepromptsourceisParentClassandwhenwetake
promptcontexttypesotherthanPLfromCurrent.
Thetruncationstrategiesforeachcasewereselectedbasedonresultsonasmallvalidationset. Forthepromptsource
Current,exceptwhenthepromptcontexttypeisPL,wealwaysstartbytakingcodeofpromptcontexttypefromafterthe
holeposition. ThismakessenseasthedefaultCodexcontextwillanywayscontaincodebeforethehole. Onlyifthisturns
outtobeblank,wewillusethecodeofcontexttypefrombeforethehole.

### B.4.ListofPromptProposals

Table7. Listofourproposedrepo-levelpromptproposals
PromptProposalID PromptSource PromptContextType
0,1,2,3,4 Current MN,I,TI,SL,FD
5,6,7 Current PL(taking25%,50%and75%contributiontothetotalcontextlength)
8,9,10,11,12,13 ParentClass MNB,MN,I,TI,SL,FD
14,15,16,17,18,19 Import MNB,MN,I,TI,SL,FD
20,21,22,23,24,25 Sibling MNB,MN,I,TI,SL,FD
26,27,28,29,30,31 SimilarName MNB,MN,I,TI,SL,FD
32,33,34,35,36,37 ChildClass MNB,MN,I,TI,SL,FD
38,39,40,41,42,43 ImportofSibling MNB,MN,I,TI,SL,FD
44,45,46,47,48,49 ImportofSimilarName MNB,MN,I,TI,SL,FD
50,51,52,53,54,55 ImportofParentClass MNB,MN,I,TI,SL,FD
56,57,58,59,60,61 ImportofChildClass MNB,MN,I,TI,SL,FD
62 Codex -

### B.5.OtherPromptProposalVariations

Weexperimentedwithothervariationsthatinclude: (a)appendingclassnamesatthebeginningofthepromptproposal
context,(b)usingnewlineorspacetojointhepromptproposalcontextandthedefaultCodexcontext,(c)takingallorthe
top-kofthepromptcontexttypes,(d)orderingoftop-k.
• ContextSeparator: ThisdefineshowwejointhepromptproposalcontextstringtothedefaultCodexcontextstring. We
experimentedwithspaceandnewlineascontextseparators.
• Prompt Proposal Context Formatting: We can format the prompt proposal context before giving it to the Prompt

### Composer. Weexperimentedwiththefollowingoptions:

1. class_name: append[classnameofthefile]atthebeginningofthepromptproposalcontexttakenfromeachfilethat
ispartofthepromptsource. Forexample,ifwearetakingpromptproposalcontextfromtwoimportfilesf1andf2,
thepromptproposalcontextwillbeformattedas: [classnameoff1]promptproposalcontextfromf1+space+
[classnameoff2]promptproposalcontextfromf2. WeusethiswhenthepromptproposalcontexttypesareMN,I,
TI,FDandSL.
15

<!-- Page 16 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
2. class_method_name: weapplythisonlywhenthepromptproposalcontexttypeisMNB.Weappendmethodnames
atthebeginningofeachofthecorrespondingmethodbodies. Wealsoappendthepromptproposalcontextfroma
filewiththenameoftheclassasdescribedinthepreviousitem.
3. comment: Addinginthepromptproposalcontextasacomment,i.e.,formattingitas: /**promptproposalcontext*/.
Thiswasn’tfoundtobemuchuseful.
4. none: passingthepromptproposalcontextasitis. WeusethiswhenthepromptproposalcontexttypeisPL.
• Top-kType: Foreachofthepromptproposalcontexttypes,exceptPL,weexperimentedwithtakingthe(a)first(b)last
and(c)allofthepromptproposalcontexttypes,i.e.,wecantakefirst-10identifiers. Wefound’all’tobethebestamong
all.
• Top-k: Weexperimentwithkvaluesof(a)10(b)20and(c)all. Wefound’all’toworkbestforallpromptcontexttypes.
C.ImplementationDetails

## C.1.Rlpg-H

WeusedAdam(Kingma&Ba,2015)optimizerwithalearningrateof3e-4andbatchsizeof64. WeusedCodeBERT(Feng
et al., 2020) as our pretrained model F to obtain the representation of hole window. The size of the representation
ϕ
(correspondingtothehiddendimensionofthe[CLS]token)is768. W1 ∈R512×768,b1 =512,W2 ∈R63×512,b2 =63.

## C.2.Rlpg-R

WeusedAdam(Kingma&Ba,2015)optimizerwithalearningrateof3e-4andbatchsizeof64. WeusedCodeBERT(Feng
etal.,2020)asourpretrainedmodelF toobtaintherepresentationofholewindowandpromptproposalcontext.Thesizeof
ϕ
therepresentation(correspondingtothehiddendimensionofthe[CLS]token)is768. Themultiheadedattention(Vaswani
etal.,2017)ismodeledasfollows:
Qh =F (Hh), Kh =F (Ch), Vh =F (Ch)
ϕ p ϕ p p ϕ p
(cid:16)Qh⊤ Kh(cid:17)
Att(Qh,Kh,Vh)=Vhsoftmax √ p
p p p d
k
MultiHead(Qh,Kh,Vh)=WOconcat(head ,...head )
p p 1 τ
where head =Att(WQQh,WKKh,WVVh)
i i i p i p
Intheaboveequations,d isthedimensionofthekey,WQ,WK,WV arethequery,keyandvalueprojectionmatrices,τ is
k i i i
thenumberofheadsandWO isthelinearprojectionthatcombinestheheads. TheprojectionmatricesWQ ∈Rdq×dmodel,
i

## W

i
K ∈ Rdk×dmodel,W
i
V ∈ Rdv×dmodel,WO ∈ Rdmodel×τdv. Forthemultiheadattention,weusedd
k
= d
q
= d
v
= 32,
τ = 4 and d = 768, W ∈ R63×768 and b = 63. For each head, we perform a scaled dot-product attention. G
model r p
moduleconsistsofadropout(Srivastavaetal.,2014)layer,aresidualconnection(Heetal.,2016),alayernorm(Baetal.,
2016),followedbyasequenceof(a)denselayerofweights=2048×768,bias=768,(b)reluactivation,(c)denselayerof
weights=768×2048,bias=2048,(d)dropoutlayer,(e)residualconnection,(f)layernorm. Adropoutvalueof0.25was
usedwhiletraining. Ourmodelresemblesonelayerofthetransformerencoderblock(Vaswanietal.,2017).

### C.3.Baselines

Randombaselinefirstselectsafilerandomlyfromthecurrentrepositoryfollowedbyselectingarandomlinewithinthatfile.
Wechooseallthelinesstartingfromthatlinetotheendlineofthechosenfileascontext(excludingtheholewindowifthe
chosenfileisthecurrentfile). Thenearestneighboursimilarityisbasedonthedotproductbetweentherepresentationofthe
holewindowandtherepresentationofthecontext,whereweuseapretrainedCodeBERT(Fengetal.,2020)modeltoobtain
therepresentations. FortheIdentifierUsagebaseline,ifthenearestidentifiertotheholedoesn’treturnanyusagewindow,
weproceedtothenextnearestidentifier. Forfastercomputationandtoavoidmemoryissueswhenrunningonourhardware,
forNNbaselines,wecollect64randomneighboursandthenrankbasedonthenearestneighbourdistance. TheBM25-based
baselinesusetheOkapiBM25implementationwithdefaultparametersgivenbythepippackage rank-bm25 0.2.2 10.
Forfile-levelBM25,ifthefilecontextexceedstheallocatedcontextlength,wetruncatefromtheback.
10https://pypi.org/project/rank-bm25/
16

<!-- Page 17 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode

### D.AdditionalResults


### D.1.Hole-wiseandRepo-wiseresults

Table3showstheperformanceofallmethodswhenaveragedacrossallholes(hole-wise)andacrossindividualrepositories
(repo-wise). Notethatthelattermetricisindependentofthesizeoftherepository.
Table8. Hole-wiseandRepo-wiseSuccessRate(SR)ofdifferentmethodsonthetestdata.
SuccessRate(%) Rel. ↑(%) SuccessRate(%) Rel. ↑(%)

### Method

(hole-wise) (hole-wise) (repo-wise) (repo-wise)
Codex(Chenetal.,2021) 58.73 - 60.64 -
Oracle 79.63 35.58 80.24 32.31

### Random 58.13 -1.02 58.95 -2.79


### RandomNN 58.98 0.43 60.04 -0.99


### File-levelBM25 63.14 7.51 64.28 6.00

IdentifierUsage(Random) 64.93 10.55 67.83 11.85
IdentifierUsage(NN) 64.91 10.52 67.94 12.03
FixedPromptProposal 65.78 12.00 68.01 12.15

## Rlpg-Bm25 66.41 13.07 68.15 12.39


## Rlpg-H 68.51 16.65 69.26 14.21


## Rlpg-R 67.80 15.44 69.28 14.26


### D.2.AblationonPerformancebasedonPromptProposal

Figure3showsthemeansuccessrateofpromptcontexttypeswhensuccessiscountedonlyforthecaseswhentheseprompt
contextsareapplicable. Ascanbeseenfromthefigure,postlinesisthemostusefulpromptcontexttypeonanaverage. The
contributionfromotherpromptcontexttypesthoughsmallerthanpostlinesisstillsignificanthighlightingtheimportanceof
eachpromptcontexttype.
17

<!-- Page 18 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
70

## Pl


## I

60

## Ti


## 50 Mn


## Mnb

40

## Sl


## Fd

30
20
10
0
Figure3. Meansuccessrateonvalidationdatabasedonpromptcontexttypewhentheyareapplicable.
25 Cur

### Sib

20 SimN 16 P I L

### ImpSimN 14 T M I N

15 I I m m p p Sib 12 M S FD L NB
10

### PaCl

10 ImpPaCl 8

### ChCl 6

5 ImpChCl 4
2
0 0
Figure4.(Left)Normalizedsuccessrateofpromptsourceswhenapplicable,(Right)Normalizedsuccessrateofpromptcontexttypes
whenapplicable
Figure4showsthenormalizedsuccessrateswherethenormalizationisperformedacrossthepromptproposals. Thishelps
usunderstandtherelativeperformanceofpromptproposalsourcesandcontexttypes. Theleftpartofthefigurebreaks
downtheperformancebasedonpromptsourcesandtherightpartbreaksdownbasedonpromptcontexttypes. Onethingto
notefromtheplotofpromptcontexttypesisthatwhenweconsiderrelativeperformance,postlinesisnolongerthemost
dominantcontexttype. Thisisbecausepostlinesistiedtoonlywhenthepromptsourcecorrespondstothecurrentfile,
therebycontributingtolowernumberswhencomparedtomostoftheothercontexttypesthataretiedtoallpromptsources.

### D.3.Performanceonnon-immediatePostLines

Table9showstheperformanceofpostlineswhenstartingfromthefourthlineafterthetargetholeline(i.e.,skippingthree
linesafterthetargethole)asopposedtostartingfromthelinethatimmediatelyfollowsthetargethole. Thisexperiment
helpsusunderstandtheperformancewhenweareinterestedindoingamuchhardertaskofmulti-linecodeautocompletion,
18

<!-- Page 19 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
whereintheobjectiveistopredictnotjusttheblankedoutportioninthecurrentlinebutalsothenextthreelineswhichcan
correspondtocompletingablockofcodelikeafunctionbody. Fromthetable,weseethatwhenstartingfromthefourth
line,aslightdeteriorationinperformanceoccurs. Thisisexpectedbecausethefartherawaywemovefromthetargethole,
thelessrelevantthepostlinescontextwouldbe. However,theperformancedropisnotsignificantsuggestingthatpostlines
isstillaveryusefulpromptcontexttypethatcanbeusedunderthesettingofmulti-linecode-autocompletion. Equivalently,
wecanincludethisasoneofthepromptproposalsinourframeworkalongwiththecurrentversionofpostlines.
Table9. SuccessRate(SR)whentakingdifferentversionsofpostlines.
SuccessRate(%) Rel. ↑(%) SuccessRate(%) Rel. ↑(%)

### Method

(hole-wise) (hole-wise) (repo-wise) (repo-wise)

### Codex(Chenetal.,2021) 58.73 - 60.64 -

PostLines(immediatelineafterthehole) 65.78 12.00 68.01 12.15
PostLines(skippingthreelinesafterthehole) 65.11 10.86 66.42 9.53

### D.4.Compositionofpromptproposals

Table10showstheperformanceofthetwoversionsofRLPGwhenwecomposethepromptproposalcontextfromlprompt
proposals. Wetakethetop-lpromptproposalsgivenbyRLPGbasedondecreasingorderofprobability. Todecidehow
muchcontextshouldbeusedforeachpromptproposal,wedividethetotalcontextlengthinproportiontothenormalized
probabilitiesofthetop-lpromptproposals. Ascanbeseenfromthetable,eventhoughPPCisnotexplicitlytrainedto
perform composition (both the ground-truth vector and the representation of prompt proposal context involve a single
promptproposal),allthecompositionsleadtosignificantimprovementsoverCodex. However,asexpectedthebestresults
correspondtotakingcontextfromasinglepromptproposal(i.e.,thetrainingsetting). Thedropinsuccessratewithl=2
andl=5isnotthatsignificant,whichsuggeststhatexplicitlytrainingRLPGtolearntocomposecontextsfromdifferent
promptproposalscanleadtopromisingresultsandhenceoffersaninterestingfuturedirection.
Table10. SuccessRate(SR)ofdifferentcompositionsofthepromptproposalsonthetestset.
SuccessRate(%) Rel. ↑(%) SuccessRate(%) Rel. ↑(%)

### Method

(hole-wise) (hole-wise) (repo-wise) (repo-wise)
Codex(Chenetal.,2021) 58.73 - 60.64 -
RLPG-H(l=1) 68.51 16.65 69.26 14.21
RLPG-R(l=1) 67.80 15.44 69.28 14.26
RLPG-H(l=2) 67.07 14.20 67.87 11.91
RLPG-R(l=2) 66.57 13.35 67.88 11.94
RLPG-H(l=5) 66.60 13.40 67.91 11.98

### RLPG-R(l=5) 65.78 12.01 67.69 11.62

RLPG-H(l=10) 65.53 11.58 67.24 10.88
RLPG-R(l=10) 63.59 8.27 65.98 8.79

### D.5.EffectofContextLength

Tounderstandtheeffectofcontextlengthontheperformanceofourpromptproposals,wetookhalfofthecontextlength
availableforapromptinCodexandobservedtheperformanceoftheoracleandfixedpromptproposal. Asbefore,wesaw
thatanoracleconstructedfromourpromptproposalsshowsremarkableimprovementoverCodexhighlightingthevalueof
ourpromptproposals. However,whencomparedtoalargercontextlength,therelativegainsaresmaller. Thisisexpectedas
asmallercontextlengthmeansthattherelevantcontextcomingfromapromptproposalneedstobetruncatedtomakeitfit
insidetheprompt,therebyleadingtolossofinformation.
19

<!-- Page 20 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode
Table11. SuccessRate(SR)ofCodexandoracleoverthetestsetwhenthetotalcontextlength=2048.
SuccessRate(%) Rel. ↑(%) SuccessRate(%) Rel. ↑(%)

### Method

(hole-wise) (hole-wise) (repo-wise) (repo-wise)
Codex(Chenetal.,2021) 57.77 - 58.90 -
Oracle 61.90 7.15 67.18 14.07

### D.6.EffectofTruncation

Wecalculatedthepercentageoftimesthecontextincludedinthepromptgetstruncated. InTable12,thesecond,third,
fourth,andfifthcolumnsrepresentthepercentagetruncationwiththedefaultcodexcontext,thepromptproposalcontext,
witheitherofthemandwithbothofthem,respectively. Thetruncationnumberssuggestthatacodecompletionmodelthat
allowsalongercontextlengthcanbeuseful. Wedonotexplicitlyencouragethesyntacticcorrectnessoftheincludedcode
snippet. Sincethecontextlengthislimited,itisquitepossiblethattheincludedcontextinthepromptisnotsyntactically
correctasawhole. However,onplottingtherepository-wisenumbers,wedidn’tobserveanyparticularcorrelationbetween
theamountoftruncationandperformance. Thismakesusbelievethatthecontentoftheincludedcontext(whetheritcomes
fromaselectedpromptproposal)iswhatmattersmoreratherthanwhetheritissyntacticallycorrectornot.
Table12. Percentagetruncationwhenusingdifferentcontextsintheprompt.

### DefaultCodex PromptProposal

Method Either Both SuccessRate

### Context Context


## Rlpg-H 26.95 30.95 39.22 18.68 68.51


## Rlpg-R 26.82 31.31 38.88 19.24 67.80


### D.7.Performanceonindividualrepositories


### Table13. SuccessRateofdifferentmethodsontrainingdata

Reponame #TotalHoles Oracle Codex Fixedpromptproposal RLPG-H RLPG-R
largemail 1653 75.38 55.11 62.73 63.94 63.28
ftpserverremoteadmin 7323 86.44 66.11 76.09 76.21 76.76
myt5lib 838 91.65 53.58 61.34 73.51 74.46
seamlets 4890 92.74 62.25 62.72 71.55 74.27
gloodb 10000 91.07 57.50 57.50 70.32 72.31
jjskit 9043 80.36 65.61 72.18 72.00 72.44
mobileexpensetracker 2298 75.94 57.88 67.28 66.84 66.97
gfsfa 10000 80.55 57.33 57.33 59.28 65.24
swe574-group3 2029 76.79 54.46 66.19 65.16 64.91
strudem-sicsa 6131 77.83 64.96 72.55 73.25 73.32
soap-dtc 1370 81.24 64.82 70.73 71.61 72.70
openprocesslogger 7191 81.06 62.19 71.77 72.22 72.62
tapestry-sesame 397 72.54 45.84 61.21 60.71 63.98
exogdx 735 84.76 63.81 75.51 75.92 76.60
designpatternjavapedro 1069 78.30 54.82 64.36 63.99 68.57
quidsee 3020 81.66 60.79 69.50 70.36 70.26
healpix-rangeset 4734 63.54 48.71 54.67 54.94 55.07
sol-agent-platform 10000 73.76 58.22 65.72 65.65 65.94
rsbotownversion 10000 75.23 57.89 65.58 66.22 66.31
20

<!-- Page 21 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode

### Table14. SuccessRateofdifferentmethodsonvalidationdata

Reponame #TotalHoles Oracle Codex Fixedpromptproposal RLPG-H RLPG-R
tyrond 721 83.91 60.33 71.15 71.57 72.68
math-mech-eshop 2225 83.46 62.20 72.76 73.53 73.17
infinispan-storage-service 373 82.31 71.85 78.55 76.94 77.75
teammates-shakthi 7665 82.02 63.74 72.38 72.47 72.46
javasummerframework 10000 79.27 55.92 65.30 65.74 65.55
tinwiki 10000 73.67 69.27 69.27 69.12 69.58
jloogle 3145 84.55 73.16 77.87 77.17 77.36
jcontenedor 5464 81.26 58.99 67.77 67.95 68.32
sohocms 772 76.68 57.90 67.10 67.49 67.62
affinity_propagation_java 1466 79.54 59.14 70.33 70.26 70.26
jata4test 1921 71.06 44.09 54.92 55.91 57.47
swinagile 2595 79.69 63.01 72.29 72.49 72.68
navigablep2p 1322 75.72 59.76 65.43 65.13 65.28
springlime 879 83.50 62.34 74.18 74.86 74.40

### Table15. SuccessRateofdifferentmethodsontestdata

Repo #Total Fixed Random IdenUsage IdenUsage File-Level RLPG-

### Oracle Codex RLPG-H RLPG-R Random


### Name Holes PP NN (Random) (NN) BM25 BM25

dovetaildb 10000 76.89 57.12 66.45 66.06 66.25 57.45 57.58 61.39 60.77 59.39 66.09
project-pt-diaoc 10000 82.01 52.67 52.81 65.08 61.25 51.58 52.93 55.54 56.21 57.04 58.29
realtimegc 2513 77.64 57.58 67.01 67.85 68.48 57.78 58.89 63.51 63.99 61.84 66.69
fswuniceubtemplates 2070 77.44 55.7 58.89 66.81 65.8 55.22 55.89 65.7 66.43 59.28 66.71
qwikioffice-java 1138 76.45 70.21 70.21 69.86 70.56 46.13 48.15 60.37 62.92 64.41 58.17
glperaudsimon 1766 78.65 53.57 62.51 62.4 61.66 55.66 57.76 69.42 68.4 69.14 61.55
xiaonei-java-ap 839 73.42 57.57 62.1 62.69 63.29 57.09 57.21 71.28 72.35 63.77 63.29
ircrpgbot 6591 83.67 69.67 77.24 76.71 76.65 69.55 70.54 74.68 74.43 69.32 75.75
robotsimulator2009w 7514 75.63 56.28 67.55 67.53 67.55 56.4 56.18 64.61 64.71 62.96 66.12
gwt-plugindetect 73 84.93 60.27 68.49 65.75 68.49 58.9 57.53 63.01 63.01 50.68 75.34
apiitfriends 1385 85.05 65.05 74.8 75.67 75.31 65.7 68.59 70.25 70.11 66.93 73.57
wicketbits 754 83.02 59.81 72.94 72.81 73.08 60.21 61.94 81.96 79.31 84.48 73.47
hucourses 590 84.41 70.68 77.46 77.63 77.97 70 72.2 70.68 72.54 53.39 75.08
xfuze 3055 84.09 62.82 73.62 72.73 73.62 63.67 65.17 77.25 75.97 77.32 74.01
Table13,Table14andTable15presentthesuccessratesofdifferentmethodsoverindividualrepositoriesinthetraining,
validation and test splits, respectively. The repo-wise averages in Table 2 in the main paper were calculated by taking
theaverageofnumberscorrespondingtoeachcolumn. Thehole-wiseaveragescorrespondtomultiplyingtherepo-wise
numbersofeachmethodbythetotalholesintherepotogetthetotalnumberofsuccessfulholesbythatmethodforthat
repo. Wethenaddthetotalnumberofsuccessfulholesacrossreposanddivideitbythetotalnumberofholesintheentire
datasplittogetthehole-wiseaverages.

### E.AnalysisofSampleCases

InFigure1,RLPGselectsthepromptproposalthatcorrespondstotakingmethodnamesandbodiesfromtheimported
file(i.e. MaximizingGibbsSampler.java). Notethat mg. beforetheholepositionindicatesthatamethodused
intheimportedfileislikelytobeinvoked. Inthiscase,thepromptproposalcontext(highlightedinviolet)containsthe
methodname InitializeToAssignment(partoftargethole). ThisinconjunctionwiththedefaultCodexcontext
whichcontainsthemethod CurrentAssignments()(partoftargethole)leadstogenerationofasuccessfulprompt.
Ontheotherhand,thepromptcreatedfromthedefaultCodexcontextfailstopredictthetargetholeinthiscase. Ingeneral,
weobservedthatintheabsenceofastrongsignal,Codexhasatendencytogivepreferencetonaturallanguagecomments
occurringbeforetheholeposition,e.g.namingthemethodbasedonthecomment. Thisincertaincasesmighthurt. We
provideinsatncesofpositiveandnegativesamplescasesforRLPGbelow:
21

<!-- Page 22 -->

Repository-LevelPromptGenerationforLargeLanguageModelsofCode

### E.1.PositiveCases

WeprovidesomeexamplesofcaseswhereRLPGledtothecorrectpredictionandCodexfailed.

## Caseswherepartofthetargetholeisfoundexactlyinthepromptproposalcontext.

• RLPG= Propagation(int numVars) vsCodex= Propagation()
• RLPG= tersFromFile(String filename) { vsCodex= ters(String filename) {
• RLPG= als("dampingFactor")) { vsCodex= als("numVars")) {
• RLPG= ] + ", value = " + entries[1]); vsCodex= ]);
• RLPG= stem.exit(1); vsCodex= stem.err.println("DPAP load error: " + ex.get

## Cases where Codex takes strong hint from the preceding natural language comment, thereby producing incorrect

predictions.
• RLPG= d PassMessages() vsCodex= d DoOneRoundOfMessagePassing()
• RLPG= teger> CurrentExemplars() { vsCodex= teger> ChooseExemplars() {
• RLPG= ring FileName() { vsCodex= ring GetAlgorithmFilename() {

### E.2.NegativeCases

Incertaincases,extrainformationfrompromptproposal-contextmightleadtoconfusionandproduceincorrectpredictions.
• RLPG= an hasConverged_; vsCodex= an converged_;
• RLPG= _[i][j] = -Double.MAX_VALUE; vsCodex= _[i][j] = 0;
22

## Tables

**Table (Page 7):**

| 78 )%( 76 etaR sseccuS 74 72 laV Fixed Prompt Proposal (repo-wise) RLPG-R (repo-wise) Fixed Prompt Proposal (hole-wise) 70 RLPG-R (hole-wise) 1 2 3 4 5 6 7 8 9 1011121314151617181920 k |
|---|
| 60 Cur Sib 50 SimN ImpSimN 40 ImpSib Imp 30 PaCl ImpPaCl 20 ChCl ImpChCl 10 0 |


**Table (Page 7):**

| Fixed Prompt Proposal (repo-wise) RLPG-R (repo-wise) Fixed Prompt Proposal (hole-wise) RLPG-R (hole-wise) |  |
|---|---|
|  | Fixed Prompt Proposal (repo-wise) RLPG-R (repo-wise) Fixed Prompt Proposal (hole-wise) RLPG-R (hole-wise) |


**Table (Page 7):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 7):**

|  |
|---|
|  |


**Table (Page 14):**

| a |
|---|
| justOneRound_ |


**Table (Page 18):**

| 25 Cur Sib 20 SimN ImpSimN ImpSib 15 Imp PaCl 10 ImpPaCl ChCl 5 ImpChCl 0 |  |
|---|---|
|  | 16 P I L TI 14 MN MNB 12 SL FD 10 8 6 4 2 0 |


**Table (Page 18):**

|  |  |
|---|---|
|  |  |


**Table (Page 21):**

| Repo Name | #Total Holes | Oracle | Codex | Fixed PP | RLPG-H | RLPG-R | Random | Random NN | IdenUsage (Random) | IdenUsage (NN) | File-Level BM25 | RLPG- BM25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| dovetaildb project-pt-diaoc realtimegc fswuniceubtemplates qwikioffice-java glperaudsimon xiaonei-java-ap ircrpgbot robotsimulator2009w gwt-plugindetect apiitfriends wicketbits hucourses xfuze | 10000 10000 2513 2070 1138 1766 839 6591 7514 73 1385 754 590 3055 | 76.89 82.01 77.64 77.44 76.45 78.65 73.42 83.67 75.63 84.93 85.05 83.02 84.41 84.09 | 57.12 52.67 57.58 55.7 70.21 53.57 57.57 69.67 56.28 60.27 65.05 59.81 70.68 62.82 | 66.45 52.81 67.01 58.89 70.21 62.51 62.1 77.24 67.55 68.49 74.8 72.94 77.46 73.62 | 66.06 65.08 67.85 66.81 69.86 62.4 62.69 76.71 67.53 65.75 75.67 72.81 77.63 72.73 | 66.25 61.25 68.48 65.8 70.56 61.66 63.29 76.65 67.55 68.49 75.31 73.08 77.97 73.62 | 57.45 51.58 57.78 55.22 46.13 55.66 57.09 69.55 56.4 58.9 65.7 60.21 70 63.67 | 57.58 52.93 58.89 55.89 48.15 57.76 57.21 70.54 56.18 57.53 68.59 61.94 72.2 65.17 | 61.39 55.54 63.51 65.7 60.37 69.42 71.28 74.68 64.61 63.01 70.25 81.96 70.68 77.25 | 60.77 56.21 63.99 66.43 62.92 68.4 72.35 74.43 64.71 63.01 70.11 79.31 72.54 75.97 | 59.39 57.04 61.84 59.28 64.41 69.14 63.77 69.32 62.96 50.68 66.93 84.48 53.39 77.32 | 66.09 58.29 66.69 66.71 58.17 61.55 63.29 75.75 66.12 75.34 73.57 73.47 75.08 74.01 |


**Table (Page 22):**

| Propagation(int numVars) |  |  |  |
|---|---|---|---|
| tersFromFile(String filename) { |  |  |  |
| als("dampingFactor")) { | vsCodex= | als("numVars")) { |  |
| ] + ", value = " + entries[1]); |  | vsCodex= | ]); |
| stem.exit(1); |  |  |  |


**Table (Page 22):**

| d PassMessages() |  |  |
|---|---|---|
| teger> CurrentExemplars() { | vsCodex= | teger> ChooseExemplars() { |
| ring FileName() { |  |  |


**Table (Page 22):**

| an hasConverged_; |
|---|
| _[i][j] = -Double.MAX_VALUE; |
