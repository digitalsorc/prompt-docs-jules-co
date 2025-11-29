---
title: "PromptChainer Visual Programming"
original_file: "./PromptChainer_Visual_Programming.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "evaluation"]
keywords: ["music", "sting", "flies", "generate", "few", "page", "usa", "eating", "but", "what"]
summary: "<!-- Page 1 -->

PromptChainer: Chaining Large Language Model Prompts
through Visual Programming

### TongshuangWu∗† EllenJiang† AaronDonsbach

wtshuang@cs.washington.edu ellenj@google.com donsbach@google.com
UniversityofWashington GoogleResearch GoogleResearch

## Usa Usa Usa


### JeffGray AlejandraMolina MichaelTerry

jeffgray@google.com alemolinata@google.com michaelterry@google.com
GoogleResearch GoogleResearch GoogleResearch

## Usa Usa Usa


### CarrieJ.Cai

cjcai@google.com
GoogleResearc"
related_documents: []
---

# PromptChainer Visual Programming

<!-- Page 1 -->

PromptChainer: Chaining Large Language Model Prompts
through Visual Programming

### TongshuangWu∗† EllenJiang† AaronDonsbach

wtshuang@cs.washington.edu ellenj@google.com donsbach@google.com
UniversityofWashington GoogleResearch GoogleResearch

## Usa Usa Usa


### JeffGray AlejandraMolina MichaelTerry

jeffgray@google.com alemolinata@google.com michaelterry@google.com
GoogleResearch GoogleResearch GoogleResearch

## Usa Usa Usa


### CarrieJ.Cai

cjcai@google.com
GoogleResearch

## Usa


### ABSTRACT ACMReferenceFormat:

WhileLLMshavemadeitpossibletorapidlyprototypenewML TongshuangWu,EllenJiang,AaronDonsbach,JeffGray,AlejandraMolina,
MichaelTerry,andCarrieJ.Cai.2022.PromptChainer:ChainingLargeLanfunctionalities,manyreal-worldapplicationsinvolvecomplextasks
guageModelPromptsthroughVisualProgramming.InCHIConferenceon
thatcannotbeeasilyhandledviaasinglerunofanLLM.Recent
HumanFactorsinComputingSystemsExtendedAbstracts(CHI’22Extended
workhasfoundthatchainingmultipleLLMrunstogether(withthe
Abstracts),April29-May5,2022,NewOrleans,LA,USA.ACM,NewYork,
outputofonestepbeingtheinputtothenext)canhelpusersaccom-

### NY,USA,10pages.https://doi.org/10.1145/3491101.3519729

plishthesemorecomplextasks,andinawaythatisperceivedtobe
moretransparentandcontrollable.However,itremainsunknown
whatusersneedwhenauthoringtheirownLLMchains–akeystep 1 INTRODUCTION
toloweringthebarriersfornon-AI-expertstoprototypeAI-infused
Largelanguagemodels(LLMs)haveintroducednewpossibilities
applications.Inthiswork,weexploretheLLMchainauthoring
forprototypingwithAI[18].Pre-trainedonalargeamountoftext
process.Wefindfrompilotstudiesthatusersneedsupporttransdata,modelslikeGPT-3[3]andJurassic-1[10]encodeenoughinforformingdatabetweenstepsofachain,aswellasdebuggingthe
mationtosupportin-contextlearning:theycanbeeasilycustomized
chainatmultiplegranularities.Toaddresstheseneeds,wedesigned
atruntime(withoutanyre-trainingneeded)tohandlenewtasks,
PromptChainer,aninteractiveinterfaceforvisuallyprogramming
simplybytakinginnaturallanguageinstructionscalledprompts.
chains.Throughcasestudieswithfourdesignersanddevelopers,
Forexample,ausercouldcustomizeapre-trained,generalpurpose
weshowthatPromptChainersupportsbuildingprototypesfora

### LLMtocreateanad-hocsearchengineformusiciansbygivingit

rangeofapplications,andconcludewithopenquestionsonscaling
thepromptstring:“Genre:Jazz;Artist:LouisArmstrong.Genre:
chainstoevenmorecomplextasks,aswellassupportinglow-fi
Country;Artist:”.AnLLMwouldlikelycontinuethepromptwith
chainprototyping.
thenameofacountryartist,e.g.“GarthBrooks.”Beyondthistoy
example,non-MLexpertshaveusedpromptingtoachievevarious
CCSCONCEPTS MLfunctionalitiesinreal-time,includingcodegeneration,ques-
•Human-centeredcomputing→EmpiricalstudiesinHCI; tionanswering,creativewriting,etc.[3,13,15].Recentworkon
Interactivesystemsandools;•Computingmethodologies→Ma- prompt-basedprototyping[8]foundthat,withLLMs’fluidadapchinelearning. tationtonaturallanguageprompts,non-MLexperts(e.g.designers,
productmanagers,front-enddevelopers)cannowprototypecustomMLfunctionalitywithlowereffortandlesstime,astheybypass
∗TheworkwasdonewhentheauthorwasaninternatGoogleInc.
theotherwisenecessarybutexpensiveprocessofcollectingdata
†Equalcontribution.
andtrainingmodelsupfront[2,8].

### DespitethedemonstratedversatilityofLLMs,manyreal-world

Permissiontomakedigitalorhardcopiesofpartorallofthisworkforpersonalor applicationsinvolvecomplexormulti-steptasksthatarenontrivial
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed forasinglerunofanLLM.Forexample,amusic-orientedchatbot
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
(whichwebuildinFigure2)mayrequireanAItofirstdeterminea
onthefirstpage.Copyrightsforthird-partycomponentsofthisworkmustbehonored.
Forallotheruses,contacttheowner/author(s). user’squerytype(e.g.,findartistsbygenreasshownabove,orfind
CHI’22ExtendedAbstracts,April29-May5,2022,NewOrleans,LA,USA songsgivenartists,etc.),beforegeneratingaresponsebasedon
©2022Copyrightheldbytheowner/author(s).
thequerytype.Asaresult,designersanddevelopersmaystruggle

## Acmisbn978-1-4503-9156-6/22/04.

https://doi.org/10.1145/3491101.3519729 toprototyperealisticapplicationswithonlyasingleLLMprompt.
2202
raM
31
]CH.sc[
1v66560.3022:viXra

<!-- Page 2 -->

CHI’22ExtendedAbstracts,April29-May5,2022,NewOrleans,LA,USA WuandJiangetal.

## C


## D


## A


## B

Figure1:ThePromptChainerinterface.(A)TheChainViewvisualizesthechainstructurewithnode-edgediagrams(enlarged
inFigure2),andallowsuserstoeditthechainbyadding,removing,orreconnectingnodes.(B)TheNodeView supportsimplementing,improving,andtestingeachindividualnode,e.g.,editingpromptsforLLMnodes.PromptChaineralsosupports
runningthechainend-to-end(C).
Inresponse,wepreviouslyproposedChainingmultipleLLMruns prototypemultiplealternativechains,withoutinvestingtoomuch
together[17],i.e.,decomposinganoverarchingtaskintoaseries timedesigninganysingleprompt?
ofhighlytargetedsub-tasks,mappingeachtoadistinctLLMstep,
andusingtheoutputfromonestepasaninputtothenext.They 2 BACKGROUND:LARGELANGUAGE
observedthatpeoplecaneffectivelyuseChaining:theycouldcom- MODELS,PROMPTINGANDCHAINING
pletemorecomplextasksinamoretransparentandcontrollable
Agenerativelanguagemodelisdesignedtocontinueitsinputwith
way.However,itremainsanopenquestionhowtosupportusers
plausible output (e.g., given a prompt “I went to the”, it might
inauthoringtheirownLLMchains.Fordesignersanddevelopers
auto-completewith“coffeeshop”).However,whenpre-trainedon
toapplychainingtotheirownprototypes,theyneedtonotonly
billionsofsamplesfromtheInternet,recentLLMscanbeadapted
promptwithineachindividualLLMstep,butalsodesigntheoveraron-the-flytosupportuser-definedusecaseslikecodegeneration,
chingtaskdecomposition.Suchaprocessrequirestargetedtooling,
questionanswering,creativewriting,etc.[3,15].Toinvokethe
akintoend-userprogramming[4,5].
desired functionalities, users need to write prompts [1, 11, 12]

### Inthiswork,weexaminetheuserexperienceofauthoringLLM

thatareappropriateforthetask.Themostcommonpatternsfor
chains.Throughformativestudies,wedistillthreeuniquechalprompting are either zero-shot or few-shot prompts. Zero-shot
lengesthatemergefromtheextremeversatilityofLLMs:(1)the
prompts directly describe what ought to happen in a task. For
overheadoffullyutilizingLLMcapabilities,(2)thetendencyof
example, we can enact Classification in Figure 4 with a prompt
inadvertentlyintroducingerrorstothechainwhenprompting,and
suchas“Isthestatement:‘heythere,what’sup’aboutmusic?”In
(3)thecascadingerrorscausedbyblackboxandunstableLLMgencontrast,few-shotpromptsshowtheLLMwhatpatterntofollow
erations.Addressingthesechallenges,weproposePromptChainer,
byfeedingitexamplesofdesiredinputsandoutputs:“[Dialog]Play
achainauthoringinterfacethatprovidesscaffoldsforbuildinga
somemusicIlike.[Class]is_music[Dialog]heythere,what’sup
mentalmodelofLLM’scapabilities,handlingarbitraryLLMdata
[Class]”.Giventhisprompt,theLLMmayrespondwith“not_music”
formats,defininga“functionsignature"foreachLLMstep,and
(fullpromptinFigure4).
debuggingcascadingerrors.Weconductcasestudieswithfour
While a singleLLM enables people toprototype specific ML
designersanddevelopers,whoproposedandbuiltchainsfortheir
features[8],theirinherentlimitations(e.g.,lackofmulti-stepreaownrealisticapplicationideas(e.g.,chatbots,writingassistants,
soningcapabilities)makethemlesscapableofprototypingcomplex
etc.)Ourqualitativeanalysisrevealspatternsinhowusersbuild
applications.Inresponse,wepreviouslyproposedproposedthenoanddebugchains:(1)usersbuildchainsnotonlyforaddressing
tionofchainingmultipleLLMpromptstogether,anddemonstrated
LLMlimitations,butalsoformakingtheirprototypesextensible;
theutilitiesofusing chains[17].Wefollowupontheirworkto
(2)someusersconstructedonestepofachainatatime,whereas
explorehowuserscanauthoreffectivechainsforprototyping.
otherssketchedoutabstractplaceholdersforallstepsbeforefilling
themin;(3)theinteractionsbetweenmultipleLLMpromptscanbe 3 PROMPTCHAINER:INTERFACE
complex,requiringbothlocalandglobaldebuggingofprompts.

## Requirementanalysis&Design


### Wealsoobservedsomeadditionalopenchallenges,andconclude

withdiscussiononfuturedirections:First,howcanwescalechains 3.1 RequirementAnalysis
totaskswithhighinterdependencyorlogicalcomplexity,while ToinformthedesignofPromptChainer,weconductedaseriesof
stillpreservingglobalcontextandcoherence?Second,howcanwe formativestudieswithateamoftwosoftwareengineersandthree
finda“sweetspot”forpromptingsuchthatuserscanquicklylow-fi
1FromTensorflow.jshttps://github.com/tensorflow/tfjs-models/tree/master/toxicity

<!-- Page 3 -->

PromptChainer:ChainingLargeLanguageModelPromptsthroughVisualProgramming CHI’22ExtendedAbstracts,April29-May5,2022,NewOrleans,LA,USA
4 Get factual answers 5 Parse the list
3 Branch: music intention
8 Format the response
1 Input utterances 2 Branch: music relevance
6 Extract entities
7 Call YouTube API
9 Generate response 10Filter: toxic response
Music chatbot: Respond to unstructured
statements about music

### For artist-The Beatles,

Play music by 3 Music I found 1. Get back
the Beatles. search 2. Hey Jude 8

## Love me Do!

W C h o o u n a t r r e y s a o r m t e i sts? 3 M in u f s o i . c [ G D e o G o l a r l r g y t e h P S a B t r r r t o a o o i n k t s , ] , 5
Hey! what up? 2 Not I'm chillin', what can
Music I do for you? 9

### Not

You suck! 2 You also suck! 10

### Music

Figure2:Anexamplechainforprototypingmusicchatbot,modifiedfromapilotuser’schain(itsoverviewisinFigure1).We
provideprimaryinput-outputexamples,andannotatethenodefunctionalitiesareannotatedinline.

### NodeType Description ExampleinFigure2

MLL GenericLLM UsetheLLMoutputdirectlyasthenodeoutput. 4 6 9

### LLMClassifier UseLLMoutputtofilterandbranchoutinputs. 2 3

repleH Evaluation Filterorre-rankLLMoutputsbyhuman-designedcriteria,e.g.,politeness. 10 Toxicityclassifier1
Processing Pre-implementedJavaScriptfunctionsfortypicaldatatransformation. 5 Splitbynumber
GenericJavaScript User-definedJSfunctions,incasepre-definedhelpersareinsufficient. 8 Formatthequery
.mmoC DataInput Definetheinputtoachain. 1
UserAction Enablesexternal(enduser)editingonintermediatedatapoints. (Figure5 11)
APICall CallexternalfunctionstoconnectprofessionalserviceswithLLMs. 6 CallYouTubeAPI
Figure3:Asummaryofnodetypes,includingthecoreLLMnodes,helpernodesfordatatransformationandevaluation,and
communicationnodesforexchangingLLMdatawithexternalusersorservices.
designersoverthecourseofthreemonths.Theseformativestudies chainsfrompilotstudiesareinAppendixA).Wesummarizeour
includedsessionsreflectingontheirexperiencesauthoringLLM observationsintothefollowingauthoringchallenges:
chainswithoutanyassistance,aswellasiterativedesignsessions C.1 TheversatilityofLLMsandneedfordatatransformawhere they proposed and built their chains-of-interest in early tions: The versatility of LLMs means that users need to
prototypesforseveralrounds,reportingbacktheirpainpoints(the developamentalmodeloftheircapabilities.LLMsalsoproduceoutputsinarbitrarystringformats,makingitnontrivial

<!-- Page 4 -->

CHI’22ExtendedAbstracts,April29-May5,2022,NewOrleans,LA,USA WuandJiangetal.
sweiverp
ataD
gniggubed
evitcaretni
,level-itluM
[Dialog] Good weather!
[Class] not_music
[Dialog] Play some music I like.
[Class] is_music
[Dialog] How tall is Barak Obama?
[Class] not_music
[Dialog] Hey Sophia, play
yesterday by the Marvin Gaye.
[Class] is_music
[Dialog] [[user]]
[Class] is_music / not_music
tomorP
stuptuo
ledoM
A B C a1
a2
c1
a3
c2
a4
b3 c3
Figure4:AnexpansionofFigure2,is about music:(A)Nodevisualization:thenodehasanstatusicon(𝑎 1),alistofnamedinput
(𝑎 2)andoutputhandles(𝑎 3),aswellasdetaileddatapreviews(𝑎 4).(B)Implementation:thehandlenamesaresynchronized
withtheunderlyingprompttemplate(𝑏 1).(C)Wecandebugthenodeatmultiplelevels.
totransformtheoutputofupstreamLLMstepstobecom- nodedefinitionsandexamplesinFigure3).Userscanimplement
patiblewiththeinputtodownstreamsteps. thesenodesbyprovidinganaturallanguageprompt,callanLLM
C.2 TheinstabilityofLLMfunctionsignatures:LLMsalso withthepromptasinput,andusetheLLMoutputsaccordingly.
lackstablefunctionsignatures,i.e.,thesemantictypesoftheir PromptChaineralsoprovideshelpernodesthataddresscommon
outputseasilyvarywithLLMprompts.Thiscomplicateslo- datatransformation(C.1inSection3.1)andevaluationneeds(C.3),
calchainiterations:forexample,ifauser’seditsonaprompt ortoallowuserstoimplementtheirowncustomJavaScript(JS)
unintentionallymakeanLLMstepoutputnumberedlists nodes.Finally,tosupportusersinprototypingAI-infusedappliinsteadofshortphrases,thiswouldintroduceinputerrorsto cations,PromptChainerprovidescommunicationnodesforexthefollowingsteps,andtherebybreaktheentirechain. changingdatawiththeexternalworld(e.g.,externalAPIcalls).
C.3 Thelikelihoodofcascadingerrors:Theblack-boxnature Examplegallery.ToaddresstheversatilitychallengeofLLMs
ofLLMsmeansthatsub-optimalorevenunsafeoutputina (C.1),PromptChainerprovidesexamplesoffrequentlycomposed
singlestepcouldpotentiallyleadtocascadingerrorsacross (sub-)chains,tohelpusersdevelopamentalmodelofwhichcapaanLLMchain(see[14]forasimilarobservationintraditional bilitiesarelikelytobeuseful.Theseexamplesalsoserveasasoft
machinelearningpipelines). nudgetowardsasetofpromptingpatterns,suchthatusers’prompts
aremorelikelytobecompatiblewithpredefinedprocessingnodes.
3.2 InterfaceDesign Forexample,Figure2 4 isforkedfromanIdeationexamplethat
returnsnumberedlists“1)GarthBrooks2)GeorgeStrait...”,which
WedesigntheinterfaceinFigure1inresponsetothechallenges,
isparsablewiththeprovided 5 Split by numbernode.
withaChainView(Figure1A)forauthoringthechainstructure,
The Node View allows users to inspect, implement, and
aNodeView(Figure1B)forauthoringasinglestep(node)ofthe
testindividualnodes(Figure1B).Whenanodeisselected,the
chain,andsupportforchaindebugging.
panelchangesinaccordancewiththeNodeType.PromptChainer
TheChainViewisthevisualpanelforbuildingandviewautomaticallyparsestheinputnamesofanodebasedontheLLM
ingchains.AsinFigure1A,eachrectangledepictsanode,which
promptforthatnode(or,forJavaScripthelpernodes,basedonthe
representsasinglestepinthechain,withtheedgesbetweenthem
denotinghowthesenodesareconnected,orhowtheoutputofone
functionsignature).Forexample,inFigure4,theinputhandle𝑎
1
“user”issynchronizedwiththeboldedplaceholderstring[[user]]
nodegetsusedastheinputtothenext.

### Nodevisualization.AsshowninFigure4(azoomed-innodeof

(𝑏 1)initscorrespondingprompttemplate,meaningthattheinput
F an ig d ur o e ut 2 pu 2 ts ), ( e 𝑎 a 3 c ) h , w no h d ic e h c a a r n e h u a s v e e d o t n o e c o o r n m ne o c r t e n n o a d m es e . d In in s p p u ir t e s d (𝑎 b 2 y ) t to o𝑎 e. 1 g. w ,[ il [ l s b e e nt u e se n d ce t ] o ] fi , l 𝑎 l 1 in w 𝑏 o 1 ul i d n g th et e r p e r n o a m m p e t d .I t f o a “s u e s n er te c n h c a e n ,” ge s s uc 𝑏 h 1
severalexistingnode-edge-basedvisualprogrammingplatforms2, thattherewillbenooutdatedhandles.Assuch,PromptChainer
automaticallyupdatestheglobalchaintobeconsistentwithusers’
weprovidenodepreviewstoincreasechainingtransparency,inlocaledits(addressingC.2).
cludingastatusiconhighlightingwhetherthenodecontainserrors
(Figure4𝑎 1),aswellasinlineanddetaileddataviews(𝑎 3and𝑎 4). Interactivedebuggingfunctionalities.Toaddressthecascadingerrorchallenge(C.3),PromptChainersupportschaindebugging

### NodeTypes.AssummarizedinFigure3,wedefineseveraltypes

atvariouslevelsofgranularity:First,tounittesteachnode,users
ofnodestocoverdiverseuserneeds.Atitscorearetwotypesof

### LLMnodes:GenericLLMnodesandLLMClassifiernodes(Seethe

canusetheprovidedtestingblock(Figure4𝑐 1)totesteachnode,
withexamplesindependentoftheremainingchain.Second,toperformend-to-endassessment,userscanruntheentirechainandlog
2e.g.,Maya:https://www.autodesk.com/products/maya/overview;Node-RED:https:
theoutputspernode,suchthattheultimatechainoutputiseasyto
//nodered.org/

<!-- Page 5 -->

PromptChainer:ChainingLargeLanguageModelPromptsthroughVisualProgramming CHI’22ExtendedAbstracts,April29-May5,2022,NewOrleans,LA,USA
retrieve(Figure4𝑐 2).Third,tohelpusersmapglobalerrorstolocal adsgenerator,towritingassistants.Theirchainstructuresreflect
causes,PromptChainersupportsbreakpointdebugging(Figure4𝑐 3), differenthigh-levelpatterns:(1)P1andP2builtchainswithparalandallowsuserstodirectlyedittheoutputofanodebeforeitisfed lellogicbranches,similartodecisiontrees[7].Forexample,P2’s
intothenextnode.Byfixingintermediatenodeoutputs,userscan chainsoughttogeneratespecializeddescriptionsfordifferentkinds
testasubsetofdownstreamnodesindependentofearliererrors. ofproductreviewattributes.Theyfirstclassifiedwhetherattributes
were“highend”,“discount”,or“generic”with 4,whichdetermined
4 USERFEEDBACKSESSIONS whichdownstreamnode(specializedLLMdescriptiongenerator)
Weconductedapreliminarystudytounderstandwhatkindsof wouldrun.(2)P3andP4builtchainsthatincrementallyiterate
chainswoulduserswanttobuild,theextenttowhichPromptChainer oncontent.Thesechainsusuallytakeadivide-and-conquerstratsupportstheirneeds,andwhatadditionalchallengesusersface. egy[9].Forexample,P4wroteonestorybyfirstgeneratingalistof
storyoutlines 10,thengeneratingparagraphsperpoint 12,and
4.1 Studydesign finallymergingthemback 13.
BecauseChainauthoringgoesbeyondsinglepromptstochaining Chainingrationales.Whileweprimarilyexpectedparticipants
multiplepromptstogether,werecruitedfourparticipants(3de- toauthorchainsforthepurposeofcombatingLLMlimitations
signers,1developerwithinGoogle)whohadatleastsomeprior (aswepreviouslyobserved[17]),interestingly,participantsalso
experiencewithnon-chainedprompts:P1andP2hadpriorexpe- insertedchainingstepstomaketheirprototypesmoregenerriencewritingprompts,andP3hadseensomeLLMdemos.We alizable.Forexample,thoughP3knewtheycoulddirectlybuild
personallyreachedouttotheseparticipantsindifferentproduct an ideation node for “summer vacation activities”, they instead
teams, to prioritize interests and experience in a wide range of chosetobuildamoregeneralideator 6 combinedwithasummer
domains.Beforethestudysession,participantsspent30minutes activityclassifier 7,suchthattheycould“switchtheclassifierfor
onpreparation:Theywatcheda10-minutetutorialoninterfacefea- anyothertimeorvariables,forvariabilityandflexibility.”Further,P4
tures.Theywerealsoaskedtoprepareataskbeforehandthatthey mentionedthedesirefortakingintermediatecontrol.Because
believedwouldrequiremultiplerunsoftheLLM,envisiontheLLM henoticedthetop-1LLMgenerationswerenotnecessarilytheir
callforeachstep,anddrafteachofthoseprompts.Thisway,the favorite, he built a chain to make active interventions: He first
studycouldfocusonchainingpromptstogetherratherthanwrit- over-generatedthreecandidatestoryspinesin 10,fromwhichhe
ingtheinitialprompts.Inthehour-longactualstudy,participants wouldselectandrefineoneofthemin 11 forsubsequentparagraph
loadedtheirpromptsandauthoredtheirenvisionedChainwhile expansions.
thinkingaloud.ToobservetheextenttowhichPromptChainer
couldsupportiteration,weaskedparticipantstodescribedeficien- Q:TowhatextentdoesPromptChainersupportusersiniteracies(ifany)intheirChain,andmodifytheirChains.Weobserved tivelyauthoringandimprovingtheirchains?
andrecordedtheirentiretaskcompletionsessions,andlatertran- A:PromptChainersupportedavarietyofchainconstruction
scribedtheircommentsforqualitativeanalysis.Intotal,participant strategiesandenabledmulti-leveldebugging.
spentapproximately90minutes,andreceiveda$75giftcreditfor
Chainconstruction. Participantsappliedvariouschaincontheirtime.
structionstrategies.P1performedatop-downapproach,i.e.,they

### UnderlyingLLM.Allofourexperiments(includingpilotstudy)

connectedblank,placeholdernodesfirsttoillustratetheimaginary
relyonthesameunderlyingLLMcalledLaMDA[16]3:a137biltaskdecompositionbeforefillingintheprompts.Incontrast,the
lionparameter,general-purposelanguagemodel.Thismodelis
otherthreeparticipantsworkedoneachnodeoneatatime,beroughlyequivalenttotheGPT-3modelintermsofsizeandcapaforemovingontothenextnode:whereasP2carefullyranand
bility:itistrainedwithmorethan1.5Twordsoftextdata,inan
testedeachnode,otherscreated“roughdrafts”,startingwithbasic
auto-regressivemannerusingadecoder-onlyTransformerstrucpromptsanddeferringdetailedrefinementofpromptsuntilafter
ture.IthascomparableperformanceswithGPT-3onavarietyof
a draft chain was finished (P3: “I should probably move on with
tasks,andbehavessimilarlyinitsabilitytofollowprompts.
this,Iwanttofine-tunemyLLMpromptlater.”).Thesevariedchain
constructionstrategiesindicatethatPromptChainercansupport
4.2 StudyResults
differentpathwaysforchainprototyping,butthatacommonuser
Weanalyzeourstudytoanswerthethreequestionslistedbelow.
tendencymaybetoworkonenodeatatime.
Q:Whatkindsofchainswoulduserswanttobuild? Tofurthercharacterizethenodeutilities,weanalyzedthenode
A:Usersproposeddiversetasks,somethatusedbranchinglogic, distributionsinboththeuserstudychainsandthosefrompilot
andsomethatiteratedoncontent.Theyusedchainingnotonly users (8 in total). We found that pre-defined helpers could cover
to address single-prompt limitations, but also to make their mostofthechainingneeds:participantsusedthreetimesasmany
prototypesextensible. pre-definedhelpers(13intotal)ascustomizedJSnodes(4).One
authorfurthercodifiedalltheLLMnodesaccordingtotheprimitive
Chainingpatterns.Allparticipantssuccessfullybuilttheirde-

### LLMoperationspreviouslyidentified[17],andfoundthatoutof

siredchainsduringthestudysession,withthechainscontaining
onaverage5.5±0.9nodes.AsshowninFigure5,participantsbuilt the27LLMnodes,7wereforcategorizinginputs,13forsourcing
informationfromtheLLM,and7forre-organizingtheinput.This
chainsforvariouskindsoftasks,rangingfrommusicchatbot,to
varietyinutilizationmayhaveresultedfromthePromptChainer’s
3Weusedanon-dialogversionofthemodel. examplegalleries.Forexample,P4successfullycreatedtheirown

<!-- Page 6 -->

CHI’22ExtendedAbstracts,April29-May5,2022,NewOrleans,LA,USA WuandJiangetal.
Extract mentioned entities Parse the entity list Classify the entity Format the query Call external YouTube API
2
1
Music chatbot: respond to unstructured, music statements 3
i love the 1. Sting - Shape of My Heart
song by Sting, 2. Sting - Desert Rose P1
so cool 3. Sting - Fields Of Gold
Classify review themes Generate specified blurbs Ideate vacation activities Classify & filter activities for summer

## P3

6 Generate descriptions
5 8
Ideate destinations

## P2 4

Ads generator: Generate editorial 7
9
blurbs from review attributes
mall, food court, deals, brands
Image query generator: Generate descriptions

### Discount

for imaginary summer vacation photos

### Sprawling outlet mall featuring

discounted name-brand clothing &
accessories, plus a food court. (N/A) People looking at art in the The San Diego Museum of Art
Ideate story spine bullet points Select the best option Parse the list Write paragraphs per point Join paragraphs together Add “The End”
10 11 12 13
Writing assistant: Generate full stories from a character desc.
A frog name Morris who Once upon a time, there was a frog named...Morris was a small green amphibian with bulging eyes and a wide grin. He P4
lives in a pond and hated eating flies, but he had no choice. Eating flies is what frogs do...he started trying to catch other animals.
hates eating flies He caught a few birds, a few squirrels, and even a few cats. But none of them tasted as good as flies. The End.
Figure5:Fourdifferentchainsbuiltbyuserstudyparticipants.P1andP2’schainsusedparallelbranchinglogic,whereasP3
andP4’schainsdepictiterativecontentprocessing.ThefulldetailsareinFigure6,AppendixA.
LLMclassifierbyforkingasimpledefaultexample,eventhough generatedstory.Theyfirsttriedtoalwaysgenerate“TheEnd”as
theywerelessfamiliarwithprompting. thefinalbulletpointinthestoryoutline(“StorySpine")in 10,but
Chain debugging. When they completed constructing their realizedthatthiswouldcauseparagraphgenerator 12 toproduce
chains,allparticipantsranthechainend-to-end(Figure4𝐶 2)asan aparagraphrepeating“TheEndTheEndTheEnd.”Theytherefore
“initialdebuggingstrategy”(P1andP4).Afterwards,theyusually
removedthisgenerationfrom 10,andinstead(withsomehelpfrom
attributedchainfailuretoparticularLLMnodes(P1:“easytopinthestudyfacilitator)madeafinalJavaScripthelpernode 13 for
pointunexpectedoutputsfromthedatapreview”),andperformed
appendingthetext“TheEnd”.ThissuggeststhatPromptChainer
localdebugging.P1appreciatedthebreakpointfunctionality(Figcanhelpusersdiscovererrors,thoughfutureresearchisneededin
ure4𝐶 3),astheydidnotneedtotakethechainapartinorderto
supportingthemtoresolveidentifiedproblemsthroughalternative
debugoneofthenodes;P3,ontheotherhand,reliedontheindepensolutions.
denttestingblock(Figure4𝑐 1)whendebuggingtheDescription
Generator 9,asawaytoavoidexpensiveexecutionsonmultiple Q:Whatareremainingchallengesinchainauthoring?
inputscomingfrompriornodes. A:Ensuringcoherencebetweeninterdependentsub-tasks;track-
Interestingly,mostparticipantsmadesomenon-trivialrefine- ingchainswithcomplexlogic.
mentstotheirpre-builtpromptsintheinterface,eventhoughthey
Chainswithinterdependentparalleltaskscanleadtodehadspentafairamountoftimedoingpromptengineeringbefore
creased coherence. Because P4’s story writing chain indepenthestudy.Wehypothesizethatbeingabletoobservetheinteraction
dentlygeneratedaparagraphforeachpointintheoutline,thefinal
effectsbetweennodesaffectedtheirunderstandingandexpectations
essaylackedcoherence:thoughthefirstseveralsentencesfollowed
ofeachlocalnode.Forexample,whenconstructingthestorycretheinputdescription(“Morris...hateseatingflies”),thefinalsenationchain,P4wantedtoaddafinalending,“TheEnd”,tothe
tenceinsteadhintedthatMorrislikesflies(“noneofthemtasted

<!-- Page 7 -->

PromptChainer:ChainingLargeLanguageModelPromptsthroughVisualProgramming CHI’22ExtendedAbstracts,April29-May5,2022,NewOrleans,LA,USA
asgoodasflies”).Onepilotstudyuserfacedasimilarchallenge, REFERENCES
andcreatedanotherinputnodetomanuallytrackpreviousoutputs. [1] GregorBetz,KyleRichardson,andChristianVoigt.2021.ThinkingAloud:Dy-
Inthefuture,itmaybeworthwhiletofurtherinvestigatemethods namicContextGenerationImprovesZero-ShotReasoningPerformanceofGPT-2.
ArXivpreprintabs/2103.13033(2021). https://arxiv.org/abs/2103.13033
thatconsiderinter-dependencybetweenparallelsub-tasks[15].
[2] RishiBommasani,DrewA.Hudson,EhsanAdeli,RussAltman,SimranArora,
Chainsthatinvolvemorecomplexdecompositioncanbe SydneyvonArx,MichaelS.Bernstein,JeannetteBohg,AntoineBosselut,Emma
overwhelmingtotrack.InP1’smusicchatbotchain,theextractor Brunskill,ErikBrynjolfsson,ShyamalBuch,DallasCard,RodrigoCastellon,
NiladriChatterji,AnnieChen,KathleenCreel,JaredQuincyDavis,DoraDemnode 2 producesalistof candidateentitiesperinput.Thus,it szky,ChrisDonahue,MoussaDoumbouya,EsinDurmus,StefanoErmon,John
becameunclearhowtheentitiesfedintotheclassifier 3 mapped Etchemendy,KawinEthayarajh,LiFei-Fei,ChelseaFinn,TrevorGale,Lauren
Gillespie,KaranGoel,NoahGoodman,ShelbyGrossman,NeelGuha,Tatsunori
to the original input node 1. We hope to enhance the tracing
Hashimoto,PeterHenderson,JohnHewitt,DanielE.Ho,JennyHong,KyleHsu,
capabilities of PromptChainer. For example, future work could JingHuang,ThomasIcard,SaahilJain,DanJurafsky,PratyushaKalluri,Siddharth
enablecustomizedchaingrouping:Insteadofrunningoneorall Karamcheti,GeoffKeeling,FereshteKhani,OmarKhattab,PangWeiKohd,Mark
Krass,RanjayKrishna,RohithKuditipudi,AnanyaKumar,FaisalLadhak,Mina
ofthenodes,participantscanexplicitlyselectasubsettorun.We
Lee,TonyLee,JureLeskovec,IsabelleLevent,XiangLisaLi,XuechenLi,Tengyu
mayalsoaddexecutionvisualizations(e.g.,takinginspirationfrom Ma,AliMalik,ChristopherD.Manning,SuvirMirchandani,EricMitchell,Zanele
PythonTutor4),tohighlightthemappingfromtheoriginalinput Munyikwa,SurajNair,AvanikaNarayan,DeepakNarayanan,BenNewman,
AllenNie,JuanCarlosNiebles,HamedNilforoshan,JulianNyarko,GirayOgut,
allthewaytothefinaloutput. LaurelOrr,IsabelPapadimitriou,JoonSungPark,ChrisPiech,EvaPortelance,
ChristopherPotts,AditiRaghunathan,RobReich,HongyuRen,FriedaRong,
YusufRoohani,CamiloRuiz,JackRyan,ChristopherRé,DorsaSadigh,Shiori
4.3 DiscussionandLimitations Sagawa,KeshavSanthanam,AndyShih,KrishnanSrinivasan,AlexTamkin,RohanTaori,ArminW.Thomas,FlorianTramèr,RoseE.Wang,WilliamWang,
Becauseparticipantswereaskedtopre-createsomeLLMprompts BohanWu,JiajunWu,YuhuaiWu,SangMichaelXie,MichihiroYasunaga,Jifortheirdesiredsub-taskspriortothestudy,thismayhaveun- axuanYou,MateiZaharia,MichaelZhang,TianyiZhang,XikunZhang,Yuhui
Zhang,LuciaZheng,KaitlynZhou,andPercyLiang.2021.OntheOpportunities
intentionallyledtoparticipantsfeelinginvestedintheirprompts
andRisksofFoundationModels. arXiv:2108.07258[cs.LG]
and their particular chain decomposition, making them less in- [3] TomB.Brown,BenjaminMann,NickRyder,MelanieSubbiah,JaredKaplan,
clinedtoconsiderotherchainstructuresorscrapthepromptsthey PrafullaDhariwal,ArvindNeelakantan,PranavShyam,GirishSastry,Amanda
Askell,SandhiniAgarwal,ArielHerbert-Voss,GretchenKrueger,TomHenighan,
hadalreadycreated.Yet,priorworkinprototypingindicatesthat RewonChild,AdityaRamesh,DanielM.Ziegler,JeffreyWu,ClemensWinter,
concurrentlyconsideringmultiplealternatives(e.g.,parallelproto- ChristopherHesse,MarkChen,EricSigler,MateuszLitwin,ScottGray,Benjamin
Chess,JackClark,ChristopherBerner,SamMcCandlish,AlecRadford,Ilya
typing[6])canleadtobetteroutcomes.Thus,futureworkcould
Sutskever,andDarioAmodei.2020.LanguageModelsareFew-ShotLearners.
explorehowtoencouragelow-fiprototypingofmultiplepossible InAdvancesinNeuralInformationProcessingSystems33:AnnualConferenceon
chains:inotherwords,howcanuserscreatehalf-bakedprompts NeuralInformationProcessingSystems2020,NeurIPS2020,December6-12,2020,
virtual,HugoLarochelle,Marc’AurelioRanzato,RaiaHadsell,Maria-Florina
foreachstep,suchthatthefeasibilityofanentirechaincanbe
Balcan,andHsuan-TienLin(Eds.). https://proceedings.neurips.cc/paper/2020/
rapidlytested,withoutinvestingtoomuchtimedesigningeach hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html
prompt?Forexample,PromptChainercouldperhapsencourage [4] MargaretBurnett.2010. End-usersoftwareengineeringandwhyitmatters.
JournalofOrganizationalandEndUserComputing(JOEUC)22,1(2010),1–22.
userstostartwithonlyoneortwoexamplesinafew-shotprompt, [5] MargaretM.Burnett,CurtisR.Cook,andGreggRothermel.2004. End-user
orstartwithaverysimplezero-shotprompt(eveniftheydon’t softwareengineering.Commun.ACM47(2004),53–58.
[6] StevenPDow,AlanaGlassco,JonathanKass,MelissaSchwarz,DanielLSchwartz,
initiallyperformreliably)toreduceinitialtimeinvestedineach
andScottRKlemmer.2010.Parallelprototypingleadstobetterdesignresults,
prompt. moredivergence,andincreasedself-efficacy. ACMTransactionsonComputer-
Giventimeconstraintsinthestudy,usersmayhavealsopicked HumanInteraction(TOCHI)17,4(2010),1–24.
[7] BaochengGeng,QunweiLi,andPramodKVarshney.2018.Decisiontreedesign
tasksthatwerenaturallyeasytodecompose.Inthefuture,itwould
forclassificationincrowdsourcingsystems.In201852ndAsilomarConferenceon
beworthwhiletoexploretaskdecompositionstrategiesforeven Signals,Systems,andComputers.IEEE,859–863.
largerandmorecomplextasks.Forexample,PromptChainercould [8] EllenJiang,KristenOlson,EdwinToh,AlejandraMolina,AaronDonsbach,
MichaelTerry,andCarrieJ.Cai.2022. Prompt-basedPrototypingwithLarge
helpencourageuserstofurtherdecomposeanodeinthechaininto LanguageModels.InExtendedAbstractsofthe2022CHIConferenceonHuman
morenodes,ifextensivepromptingeffortsappearunsuccessful. FactorsinComputingSystems.
[9] AniketKittur,BorisSmus,SusheelKhamkar,andRobertE.Kraut.2011.Crowd-
Forge:CrowdsourcingComplexWork.InProceedingsofthe24thAnnualACM
5 CONCLUSION SymposiumonUserInterfaceSoftwareandTechnology(SantaBarbara,California,
USA)(UIST’11).AssociationforComputingMachinery,NewYork,NY,USA,
WeidentifiedthreeuniquechallengesforLLMchainauthoring, 43–52. https://doi.org/10.1145/2047196.2047202
[10] OpherLieber,OrSharir,BarakLenz,andYoavShoham.2021.Jurassic-1:Technical
broughtonbythehighlyversatileandopen-endedcapabilitiesof DetailsAndEvaluation.TechnicalReport.AI21Labs.
LLMs.WedesignedPromptChainer,andfoundthatithelpedusers [11] JiachangLiu,DinghanShen,YizheZhang,BillDolan,LawrenceCarin,and
WeizhuChen.2021.WhatMakesGoodIn-ContextExamplesforGPT-3?ArXiv
transformintermediateLLMoutput,aswellasdebugthechain
preprintabs/2101.06804(2021). https://arxiv.org/abs/2101.06804
whenLLMstepshadinteractingeffects.Ourstudyalsorevealed [12] YaoLu,MaxBartolo,AlastairMoore,SebastianRiedel,andPontusStenetorp.
interestingfuturedirections,includingsupportingmorecomplex 2021. FantasticallyOrderedPromptsandWheretoFindThem:Overcoming
Few-ShotPromptOrderSensitivity.ArXivpreprintabs/2104.08786(2021). https:
chains,aswellasmoreexplicitlysupporting“half-baked"chain
//arxiv.org/abs/2104.08786
construction,sothatuserscaneasilysketchoutachainstructure [13] SwaroopMishra,DanielKhashabi,ChittaBaral,andHannanehHajishirzi.2021.
withoutinvestingtoomuchtimepromptingupfront. Cross-TaskGeneralizationviaNaturalLanguageCrowdsourcingInstructions.
ArXivpreprintabs/2104.08773(2021). https://arxiv.org/abs/2104.08773
[14] D.Sculley,GaryHolt,DanielGolovin,EugeneDavydov,ToddPhillips,Dietmar
Ebner,VinayChaudhary,andMichaelYoung.2014. MachineLearning:The
HighInterestCreditCardofTechnicalDebt.InSE4ML:SoftwareEngineeringfor
MachineLearning(NIPS2014Workshop).
4https://pythontutor.com/

<!-- Page 8 -->

CHI’22ExtendedAbstracts,April29-May5,2022,NewOrleans,LA,USA WuandJiangetal.
[15] BenSwanson,KoryMathewson,BenPietrzak,SherolChen,andMonicaDi- Prompts.InProceedingsofthe2022CHIConferenceonHumanFactorsinComputing
nalescu.2021. StoryCentaur:LargeLanguageModelFewShotLearningas Systems(NewOrleans,LA,USA)(CHI’21).AssociationforComputingMachinery,
aCreativeWritingTool.InProceedingsofthe16thConferenceoftheEuro- NewYork,NY,USA. https://doi.org/10.1145/3491102.3517582
peanChapteroftheAssociationforComputationalLinguistics:SystemDemon- [18] QianYang,AaronSteinfeld,CarolynRosé,andJohnZimmerman.2020. Restrations.AssociationforComputationalLinguistics,Online,244–256. https: ExaminingWhether,Why,andHowHuman-AIInteractionIsUniquelyDifficult
//aclanthology.org/2021.eacl-demos.29 toDesign. AssociationforComputingMachinery,NewYork,NY,USA,1–13.
[16] RomalThoppilan,DanielDeFreitas,JamieHall,NoamShazeer,ApoorvKul- https://doi.org/10.1145/3313831.3376301
shreshtha,Heng-TzeCheng,AliciaJin,TaylorBos,LeslieBaker,YuDu,etal.2022.
LaMDA:LanguageModelsforDialogApplications.ArXivpreprintabs/2201.08239 A SAMPLECHAINSFROMPILOTUSERS
(2022). https://arxiv.org/abs/2201.08239
[17] TongshuangWu,MichaelTerry,andCarrieJCai.2022.AIChains:Transparent
andControllableHuman-AIInteractionbyChainingLargeLanguageModel

<!-- Page 9 -->

PromptChainer:ChainingLargeLanguageModelPromptsthroughVisualProgramming CHI’22ExtendedAbstracts,April29-May5,2022,NewOrleans,LA,USA
Extract mentioned entities Parse the entity list Classify the entity Format the query Call external YouTube API
1
2
3

## P1

Music chatbot: Respond to unstructured
statements about music
i love the 1. Sting - Shape of My Heart
song by Sting, 2. Sting - Desert Rose
so cool 3. Sting - Fields Of Gold
Classify review themes Generate specified blurbs Ideate vacation activities Classify & filter activities for summer Generate descriptions
5
6
Ideate destinations
4
8

## P2

7
Ads generator: Generate editorial 9
blurbs from review attributes
mall, food court, deals, brands
Image query generator: Generate descriptions P3

### Discount

for imaginary summer vacation photos

### Sprawling outlet mall featuring

discounted name-brand clothing &
accessories, plus a food court. (N/A) People looking at art [in the The San Diego Museum of Art]
Ideate story spine Select the best option Parse the list Write paragraphs per spine Join paragraphs together Add “The End”
10 11
13
Writing assistant: Generate full stories from a character desc. 12 P4
A frog name Once upon a time, there was a frog named...Morris was a small green
Morris who amphibian with bulging eyes and a wide grin. He hated eating flies,
lives in a but he had no choice. Eating flies is what frogs do...he started
pond and hates trying to catch other animals. He caught a few birds, a few squirrels,
eating flies and even a few cats. But none of them tasted as good as flies.
Figure6:Thefulldetailsofuserstudychains.

<!-- Page 10 -->

CHI’22ExtendedAbstracts,April29-May5,2022,NewOrleans,LA,USA WuandJiangetal.

## A


### Music chatbot

find some song by sting
Here are some songs by Sting
starting with 1. Shape of My
Heart, 2. Desert Rose, and

## Fields of Gold.

Classifier on whether a msg is
crucial enough to interrupt
current user action
Msg I had to leave in a hurry.
Could you make sure my
oven is off?
Source Facebook Messenger
User sitting in a cafe
Oven is off.

## B


## C


### Reading assistant: Summarize long essay

E c a h c o h o s y e e a t r o , s t p h e o n u d s a t n h d e s i r o f v a p c e a o t p i l o e n s t h c r a o m u p g i h n o g u t i n t h t e h e U n g i r t e e a d t States A c n o n e s s s o a n y t a e b n o t u t c a p m r p o i s n g a . nd Description
outdoors... These three types of camping troubles can
strike campers almost anywhere…[1000+ words] A how-to essay Style
Figure7:Thechainsbuiltbypilotusers.

## Tables

**Table (Page 3):**

| 4 Get factual answers 5 Parse the list 3 Branch: music intention 8 Format the response 1 Input utterances 2 Branch: music relevance 6 Extract entities 7 Call YouTube API 9 Generate response 10Filter: toxic response Music chatbot: Respond to unstructured statements about music For artist-The Beatles, Play music by 3 Music I found 1. Get back the Beatles. search 2. Hey Jude 8 3. Love me Do! W C h o o u n a t r r e y s a o r m t e i sts? 3 M in u f s o i . c [ G D e o G o l a r l r g y t e h P S a B t r r r t o a o o i n k t s , ] , 5 Hey! what up? 2 Not I'm chillin', what can Music I do for you? 9 Not You suck! 2 You also suck! 10 Music |  |
|---|---|
|  | Music chatbot: Respond to unstructured statements about music For artist-The Beatles, Play music by 3 Music I found 1. Get back the Beatles. search 2. Hey Jude 8 3. Love me Do! W C h o o u n a t r r e y s a o r m t e i sts? 3 M in u f s o i . c [ G D e o G o l a r l r g y t e h P S a B t r r r t o a o o i n k t s , ] , 5 Hey! what up? 2 Not I'm chillin', what can Music I do for you? 9 Not You suck! 2 You also suck! 10 Music |


**Table (Page 3):**

| Enablesexternal(enduser)editingonintermediatedatapoints. |
|---|
| CallexternalfunctionstoconnectprofessionalserviceswithLLMs. |


**Table (Page 4):**

| C c c c hasanstatusicon(𝑎 1),alis ation:thehandlenames evels. |  | C |  |  |
|---|---|---|---|---|
|  | c |  |  | 1 |
|  |  |  |  |  |
|  | c |  |  | 2 |
|  |  |  |  |  |
|  | c |  |  | 3 |
|  |  |  |  |  |


**Table (Page 6):**

| Extract mentioned entities Parse the entity list Classify the entity Format the query Call external YouTube API 2 1 Music chatbot: respond to unstructured, music statements 3 i love the 1. Sting - Shape of My Heart song by Sting, 2. Sting - Desert Rose P1 so cool 3. Sting - Fields Of Gold |  |  |
|---|---|---|
| Music chatbot: respond to unstructured, music statements i love the 1. Sting - Shape of My Heart song by Sting, 2. Sting - Desert Rose so cool 3. Sting - Fields Of Gold |  |  |
| i love the song by Sting, so cool |  | 1. Sting - Shape of My Heart 2. Sting - Desert Rose 3. Sting - Fields Of Gold |
|  |  |  |


**Table (Page 6):**

| Classify review themes Generate specified blurbs 5 P2 4 Ads generator: Generate editorial blurbs from review attributes mall, food court, deals, brands Discount Sprawling outlet mall featuring discounted name-brand clothing & accessories, plus a food court. |
|---|
| Ads generator: Generate editorial blurbs from review attributes |
| mall, food court, deals, brands |
| Discount |
| Sprawling outlet mall featuring discounted name-brand clothing & accessories, plus a food court. |


**Table (Page 6):**

| Ideate vacation activities Classify & filter activities for summer P3 6 Generate descriptions 8 Ideate destinations 7 9 Image query generator: Generate descriptions for imaginary summer vacation photos (N/A) People looking at art in the The San Diego Museum of Art |  |
|---|---|
| Image query generator: Generate descriptions for imaginary summer vacation photos (N/A) People looking at art in the The San Diego Museum of Art |  |
| (N/A) | People looking at art in the The San Diego Museum of Art |


**Table (Page 6):**

| Ideate story spine bullet points Select the best option Parse the list Write paragraphs per point Join paragraphs together Add “The End” 10 11 12 13 Writing assistant: Generate full stories from a character desc. A frog name Morris who Once upon a time, there was a frog named...Morris was a small green amphibian with bulging eyes and a wide grin. He P4 lives in a pond and hated eating flies, but he had no choice. Eating flies is what frogs do...he started trying to catch other animals. hates eating flies He caught a few birds, a few squirrels, and even a few cats. But none of them tasted as good as flies. The End. |  |
|---|---|
| Writing assistant: Generate full stories from a character desc. A frog name Morris who Once upon a time, there was a frog named...Morris was a small green amphibian with bulging eyes and a wide grin. He lives in a pond and hated eating flies, but he had no choice. Eating flies is what frogs do...he started trying to catch other animals. hates eating flies He caught a few birds, a few squirrels, and even a few cats. But none of them tasted as good as flies. The End. |  |
| A frog name Morris who lives in a pond and hates eating flies | Once upon a time, there was a frog named...Morris was a small green amphibian with bulging eyes and a wide grin. He hated eating flies, but he had no choice. Eating flies is what frogs do...he started trying to catch other animals. He caught a few birds, a few squirrels, and even a few cats. But none of them tasted as good as flies. The End. |


**Table (Page 9):**

| Extract mentioned entities Parse the entity list Classify the entity Format the query Call external YouTube API 1 2 3 P1 Music chatbot: Respond to unstructured statements about music i love the 1. Sting - Shape of My Heart song by Sting, 2. Sting - Desert Rose so cool 3. Sting - Fields Of Gold |  |  |
|---|---|---|
| Music chatbot: Respond to unstructured statements about music i love the 1. Sting - Shape of My Heart song by Sting, 2. Sting - Desert Rose so cool 3. Sting - Fields Of Gold |  |  |
| i love the song by Sting, so cool |  | 1. Sting - Shape of My Heart 2. Sting - Desert Rose 3. Sting - Fields Of Gold |
|  |  |  |


**Table (Page 9):**

| Classify review themes Generate specified blurbs 5 4 P2 Ads generator: Generate editorial blurbs from review attributes mall, food court, deals, brands Discount Sprawling outlet mall featuring discounted name-brand clothing & accessories, plus a food court. |
|---|
| Ads generator: Generate editorial blurbs from review attributes |
| mall, food court, deals, brands |
| Discount |
| Sprawling outlet mall featuring discounted name-brand clothing & accessories, plus a food court. |


**Table (Page 9):**

| Ideate vacation activities Classify & filter activities for summer Generate descriptions 6 Ideate destinations 8 7 9 Image query generator: Generate descriptions P3 for imaginary summer vacation photos (N/A) People looking at art [in the The San Diego Museum of Art] |  |
|---|---|
| Image query generator: Generate descriptions for imaginary summer vacation photos (N/A) People looking at art [in the The San Diego Museum of Art] |  |
| (N/A) | People looking at art [in the The San Diego Museum of Art] |


**Table (Page 9):**

| Ideate story spine Select the best option Parse the list Write paragraphs per spine Join paragraphs together Add “The End” 10 11 13 Writing assistant: Generate full stories from a character desc. 12 P4 A frog name Once upon a time, there was a frog named...Morris was a small green Morris who amphibian with bulging eyes and a wide grin. He hated eating flies, lives in a but he had no choice. Eating flies is what frogs do...he started pond and hates trying to catch other animals. He caught a few birds, a few squirrels, eating flies and even a few cats. But none of them tasted as good as flies. |  |  |
|---|---|---|
| Writing assistant: Generate full stories from a character desc. A frog name Once upon a time, there was a frog named...Morris was a small green Morris who amphibian with bulging eyes and a wide grin. He hated eating flies, lives in a but he had no choice. Eating flies is what frogs do...he started pond and hates trying to catch other animals. He caught a few birds, a few squirrels, eating flies and even a few cats. But none of them tasted as good as flies. |  |  |
| A frog name Morris who lives in a pond and hates eating flies |  | Once upon a time, there was a frog named...Morris was a small green amphibian with bulging eyes and a wide grin. He hated eating flies, but he had no choice. Eating flies is what frogs do...he started trying to catch other animals. He caught a few birds, a few squirrels, and even a few cats. But none of them tasted as good as flies. |
|  |  |  |


**Table (Page 10):**

| A Music chatbot find some song by sting Here are some songs by Sting starting with 1. Shape of My Heart, 2. Desert Rose, and 3. Fields of Gold. |
|---|
| Music chatbot |
| find some song by sting |
|  |
| Here are some songs by Sting starting with 1. Shape of My Heart, 2. Desert Rose, and 3. Fields of Gold. |


**Table (Page 10):**

| I had to leave in a hurry. Could you make sure my oven is off? |  |
|---|---|
| Facebook Messenger |  |
| sitting in a cafe |  |
|  |  |
| Oven is off. |  |


**Table (Page 10):**

| C |
|---|
| Reading assistant: Summarize long essay E c a h c o h o s y e e a t r o , s t p h e o n u d s a t n h d e s i r o f v a p c e a o t p i l o e n s t h c r a o m u p g i h n o g u t i n t h t e h e U n g i r t e e a d t States A c n o n e s s s o a n y t a e b n o t u t c a p m r p o i s n g a . nd Description outdoors... These three types of camping troubles can strike campers almost anywhere…[1000+ words] A how-to essay Style |
| Each year, thousands of people throughout the United States choose to spend their vacations camping in the great outdoors... These three types of camping troubles can strike campers almost anywhere…[1000+ words] |
