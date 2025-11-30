---
title: "PathOCL Path Based Prompt OCL"
original_file: "./PathOCL_Path_Based_Prompt_OCL.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "fine-tuning"]
keywords: ["pathocl", "uml", "ocl", "page", "flight", "path", "augmentation", "airline", "passenger", "however"]
summary: "<!-- Page 1 -->


## Pathocl: Path-Based Prompt Augmentation For Ocl


## Generation With Gpt-4


### SeifAbukhalaf MohammadHamdaqa

SoftwareandEmergingTechnologiesLab(SAET) SoftwareandEmergingTechnologiesLab(SAET)
PolytechniqueMontréal PolytechniqueMontréal

### Montréal,Canada Montréal,Canada

seif.abukhalaf@polymtl.ca mhamdaqa@polymtl.ca

### FoutseKhomh

SoftWareAnalyticsandTechnologiesLab(SWAT)
PolytechniqueMontréal

### Montréal,Canada

foutse.khomh@polymtl.ca

## Abstract

Therapidprogres"
related_documents: []
---

# PathOCL Path Based Prompt OCL

<!-- Page 1 -->


## Pathocl: Path-Based Prompt Augmentation For Ocl


## Generation With Gpt-4


### SeifAbukhalaf MohammadHamdaqa

SoftwareandEmergingTechnologiesLab(SAET) SoftwareandEmergingTechnologiesLab(SAET)
PolytechniqueMontréal PolytechniqueMontréal

### Montréal,Canada Montréal,Canada

seif.abukhalaf@polymtl.ca mhamdaqa@polymtl.ca

### FoutseKhomh

SoftWareAnalyticsandTechnologiesLab(SWAT)
PolytechniqueMontréal

### Montréal,Canada

foutse.khomh@polymtl.ca

## Abstract

TherapidprogressofAI-poweredprogrammingassistants,suchasGitHubCopilot,hasfacilitated
thedevelopmentofsoftwareapplications. Theseassistantsrelyonlargelanguagemodels(LLMs),
whicharefoundationmodels(FMs)thatsupportawiderangeoftasksrelatedtounderstandingand
generatinglanguage. LLMshavedemonstratedtheirabilitytoexpressUMLmodelspecifications
usingformallanguagesliketheObjectConstraintLanguage(OCL).However,thecontextsizeofthe
promptislimitedbythenumberoftokensanLLMcanprocess. Thislimitationbecomessignificant
asthesizeofUMLclassmodelsincreases. Inthisstudy,weintroducePathOCL,anovelpath-based
prompt augmentation technique designed to facilitate OCL generation. PathOCL addresses the
limitationsofLLMs,specificallytheirtokenprocessinglimitandthechallengesposedbylargeUML
classmodels. PathOCLisbasedontheconceptofchunking,whichselectivelyaugmentstheprompts
withasubsetofUMLclassesrelevanttotheEnglishspecification. Ourfindingsdemonstratethat
PathOCL,comparedtoaugmentingthecompleteUMLclassmodel(UML-Augmentation),generates
ahighernumberofvalidandcorrectOCLconstraintsusingtheGPT-4model. Moreover,theaverage
promptsizecraftedusingPathOCLsignificantlydecreaseswhenscalingthesizeoftheUMLclass
models.
Keywords ObjectConstraintLanguage(OCL),SimplePath,PromptEngineering,LargeLanguageModel(LLM),
GenerativePre-TrainedTransformer(GPT),FoundationModel(FM)
1 Introduction
Thewidespreaduseofartificialintelligence(AI)-poweredprogrammingassistants,suchasGitHubCopilot[1]and
ChatGPT, has introduced a paradigm shift in the ways we build software applications [2]. At the heart of their
intelligenceliethefoundationmodels(FMs)-AImodelsdesignedtosupportawidespectrumoftasksindifferent
modalities,empoweringthemodern-daychatbotsandgenerativeAI[3].
Largelanguagemodels(LLMs)areonetypeofFMsnotablefortheirabilitytoachievegeneral-purposelanguage
understandingandgeneration. LLMshaveenabledAIassistantstounderstandandinterpretourpromptsdescribed
innaturallanguage(e.g.,English). Suchemergentpropertieshaveattractedtheinterestofsoftwarepractitionersto
investigateLLMapplicationsinfacilitatingmodel-basedsoftwaredevelopmenttasks[4,5,6].
One challenging task that software practitioners often encounter is expressing model specifications using formal
languages such as the Object Constraint Language (OCL). Writing OCL constraints can be challenging and not
4202
nuJ
6
]ES.sc[
2v05421.5042:viXra

<!-- Page 2 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4
straightforward,especiallyfornovicepractitioners,duetotheunfamiliarsyntaxofthelanguageitself[7,8]. Therefore,
manuallyexpressingspecificationsbecomestime-consumingwheninvolvinglargeUMLclassmodelsandcomplex
specificationswithmanyentitiesthatdemandcarefulattentionbythesoftwarepractitionertodeterminetheproper
UMLclassesandrelations. Inaddition, thefactthataspecificationcanbeexpressedindifferentOCLconstraints
withequivalentsemanticsmaypresentfurtherchallengesforsoftwarepractitionerswhenchoosingtheoptimalOCL
constraint[9,10].Therefore,LLMshavethepotentialtofacilitatemodeldevelopmentbyassistingsoftwarepractitioners
inimplementing,validating,andreviewingtheirOCLconstraints[4,11,5].
DifferentpromptingtechniqueshavebeenproposedtoemployLLMsforUMLandOCLmodeling[5]. Inourprevious
study[4],wedemonstratedthatrelyingsolelyonEnglishspecificationsinthepromptisinsufficientforgenerating
reliableOCLconstraints,andaugmentingthepromptwiththecompleteUMLclassmodelascontextsignificantly
impactstheresults. However,currentLLMscanonlyprocessacertainnumberoftokens. Thislimitationbecomes
significantwhenthesizeoftheUMLclassmodelsgrowslargeenoughtoexceedthelimitedcontextwindowofthe

## Llm.

To overcome this limitation, we draw inspiration from human problem-solving techniques for tackling complex
problems. ExperiencedsoftwarepractitionersoftenbreakdownUMLclassmodelsintosub-models. Thisapproach
narrows the scope, allowing them to effectively analyze different classes and semantically map elements from the
EnglishspecificationtotheirequivalentOCLexpressions.
In this research, we propose PathOCL: a path-based prompt augmentation technique for OCL generation.
PathOCL is a prompting technique that adapts the concept of chunking. It reduces the context of the prompt by
selectivelyaugmentingthesubsetofUMLclassesrelevanttotheEnglishspecification.
We designed PathOCL as a three-step process, illustrated in Figure 1. In the first step, we preprocess the English
specificationtoextracttheUMLelements. Inthesecondstep,werepresenttheUMLclassmodelsasUMLgraphs
andgenerateasetofsimplepaths[12,13]thatcoveralltheUMLclassesintheUMLgraph. WeuseJaccard[14]and
cosinesimilaritytorankthesimplepathsbasedonthelikelihoodthatthesetofextractedUMLelementsexistsinthe
UMLclassesalongthechosenpath. Inthefinalstage,wecraftpromptsaugmentedwiththesubsetofUMLclasses
basedonthesimplepathandgenerateOCLconstraintsusingtheGPT-4model. Inthisstudy,weaimtoaddressthe
followingresearchquestions:
• RQ1. HoweffectiveisPathOCLpromptingtechniqueingeneratingvalidandcorrectOCLconstraints?
OurstudyaimstoempiricallyevaluatetheeffectivenessofprovidingaselectivesubsetofUMLclassesascontext
(PathOCL),comparedtoaugmentingtheentireUMLmodel(UML-Augmentation)[4]. Weproposethefollowing
hypothesesbasedontwoevaluationmetrics: validityandcorrectnessscores.
Validity. Theinitialnullhypothesis(H0-Validity)statesthatthereisnoimprovementinthevalidityscoreswhen
comparingthePathOCLandUML-Augmentationtechniques. Incontrast,thealternativehypothesis(H1-Validity)
statesthatthereisanimprovementinthevalidityscoresbetweenthetwotechniques.
Correctness. Thesecondnullhypothesis(H0-Correctness)statesthatthereisnoimprovementinthecorrectness
scoresbetweenthePathOCLandUML-Augmentationtechniques. Inthealternativehypothesis(H1-Correctness),we
statethatthereisanimprovementinthecorrectnessscoresbetweenthetwotechniques.
• RQ2. HowdoestheinferencecostcomparebetweenPathOCLandUML-Augmentationprompting
techniques?
Inthisresearchquestion,weassesstheinferencecostsassociatedwiththepromptsusedinboththePathOCLand
UML-Augmentationtechniques. ThecostsarecalculatedbasedonthepricingmodelprovidedbyOpenAIfortheir
GPT-4model1. Inaddition,weanalyzethescalabilityofthepromptscraftedusingbothtechniquesfordifferentUML
classmodels,includingsmall,medium,andlarge-sizedmodels.
The remaining sections of this paper are organized as follows: Section 2 provides the necessary background and
terminology. Section3describesourmethodology. Section4presentstheempiricalevaluationofPathOCL.Section5
discussesourfindings. Section6introducesrelatedworks. Section7outlinesthethreatstothestudy,andSection8
concludesthepaper.
1https://openai.com/pricing
2

<!-- Page 3 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4

### Inputs


### English


### Specification


### UML Elements Set

Specification Preprocessing
UML Class Simple Path
Ranked Simple

Model Generation

### Paths

UML Class

Augmentation
Output
Prompt

LLM (GPT-4) OCL Constraint

### Template

Figure1: OverviewofthePathOCLpromptingprocess.
2 BackgroundandTerminology
ObjectConstraintLanguage(OCL)isaformallanguageusedtospecifyrulesonthestructureandbehaviorofMOF
models,includingUMLmodels[15]. OCLisadeclarativelanguage;whenanOCLconstraintisevaluated,itdoesnot
impactthestateofthemodel. OCLexpressionscanbeinvariants,whichareappliedtotheattributesandassociationsof
UMLclassesandmustbeevaluatedtotrueforallinstancesoftheUMLmodel. OthertypesofOCLexpressionscanbe
appliedtotheoperationsofUMLclasses,knownaspre-conditionsandpost-conditions.
Inthecontextofmodel-drivendevelopment(MDD),OCLconstraintsplayacrucialroleinensuringformalismand
consistencyduringsoftwaredevelopment[16]. TheOCLmeta-modeldefinestheabstractsyntaxandsemanticsof
OCLexpressions. ByformalizingconstraintsusingtheOCLmeta-model,toolsliketheUML-basedSpecifications
Environment(USE)[17]canautomaticallyverifyifaspecifiedOCLconstraintconformstotheUMLclassmodeland
canprovidefeedbacktotheuserregardingruleviolationsorerrors. TheOCLabstractsyntaxdefinesthegrammarand
structureofthelanguage,includingOCLtypesandexpressions. OCLtypesincludedatatypes,collectiontypes,and
messagetypes. OCLexpressionscanalsoincludepropertyexpressions,ifexpressions,iteratorexpressions,variable
expressions,andotherexpressions.
PromptengineeringisasystematicapproachindesigningpromptsthateffectivelygeneratearesponsefromLLMs.
ThedesignandimplementationofpromptshaveacriticalimpactontheperformanceofLLMs,andseveralprompting
techniques have been proposed and proven to be effective [18]. One commonly used type of prompt is zero-shot
prompting,wherethepromptcontextdoesnotincludeexamplesfortheLLMtofollow. Incontrast,few-shotprompting
involvesprovidinginput-outputpairexamplesinthecontexttoguideandcustomizetheresponseformatoftheLLM.
Advancedreasoningtechniques,suchasChain-of-Thoughts(CoT)[19],wheretheLLMispromptedthroughstep-bystepreasoning,havealsobeenusedtoimproveproblem-solvingabilitiesinlogicaltasks,criticalthinking,andcomplex
programming[20]. Anotherpromptingtechniqueinvolvesretrievingchunksofrelevantdocumentsbasedonthegiven
queryandincorporatingthemascontext,whichplaysapivotalroleinreducinghallucinationsbygroundingtheLLM
ontheaugmentedinformation[21].
3

<!-- Page 4 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4
Graphsarefundamentaldatastructuresusedtorepresentrelationshipsbetweenentities. Agraphconsistsofnodes
(vertices)andedgesthatconnectpairsofnodes. Formally[12],agraphGis:
• AsetofN nodes,whereN ̸=ϕ.
• AsetofN initialnodes,whereN ⊆N andN ̸=ϕ.
0 0 0
• AsetofN finalnodes,whereN ⊆N andN ̸=ϕ.
f f f
• AsetofEedges,whereEisasubsetofN ×N.
Agraphisdirectedwhenedgeshaveadefineddirectionfromonenoden toanothern ,denotedas(n ,n ). Apathisa
i j i j
sequence[n ,n ,...,n ]ofnodes,whereeachpairofadjacentnodes,(n ,n +1),1≤i≤M,isinthesetEofedges.
1 2 M i i
Simplepaths[12]refertosequencesofedgesfromnoden tonoden wherenonodeisrepeated. Inotherwords,a
i j
simplepathisapaththroughagraphthatdoesnotrevisitanynode.
3 Methodology
Inthissection,wepresentPathOCL,ourapproachforgeneratingOCLconstraintsgivenaUMLclassmodelandthe
naturallanguagespecificationinEnglish. TheprimaryobjectiveofPathOCListoovercomethelimitationsinthe
numberoftokensanLLMcanprocess,whichcanoccurwhenthesizeoftheUMLclassmodelexceedsthecontext
sizeoftheprompt. PathOCLattemptstoemulatetheprocessthatanexperiencedsoftwarepractitionerfollowswhen
formulatingOCLconstraints. TheexperttypicallystartsbyreducingtheUMLclassmodelintoasubsetofclasses
relevanttothecontextofthegivenEnglishspecification.
PathOCLrequirestwoinputs: (a)theOCLspecificationwritteninnaturallanguage(i.e.,English)and(b)theUML
classmodel. Figure1providesanoverviewofthePathOCLpromptingapproach. PathOCLconsistsofthreemainsteps:
(a)Englishspecificationpreprocessing,(b)simplepathsgenerationandranking,and(c)promptaugmentationwith
theselectivesubsetofUMLclassestogenerateOCLconstraint. Wepresenttheairportdomainmodelasarunning
exampletomotivatePathOCLandexplaineachstepoftheapproachindetail.
3.1 CaseStudy
Theairportdomainmodel,showninFigure2,representstheorganizationandfunctionalityofafictionalairlinesystem.
Theairportclassplaysavitalroleasdepartureandarrivalpointsforflights. Theflightclass,withaspecificnumberof
passengers,originatesfromanairportandtravelstodesignatedairports. Theairlineclassisresponsibleforoperating
andsupervisingtheseflights. ItiscommonforairlinestohaveaChiefExecutiveOfficer(CEO)whomaintainsaclose
affiliationwiththecompany. WewillruntheexamplebyintroducingthefollowingEnglishspecification:
“Themaximumnumberofpassengersonanyflightmaynotexceed1000.”
3.2 SpecificationPreprocessing
ThefirststepinPathOCListoextractUMLelementsfromtheprovidedEnglishspecification. Theseelementsserveas
theheuristictorankthesetofsimplepathsgeneratedfromtheUMLgraph. Specificationpreprocessingconsistsof
threesteps: (a)tokenization,(b)part-of-speech(PoS)tagging,and(c)lemmatization. WeusespaCytrainedEnglish
pipeline“en_core_web_sm”, whichincludestherequiredcomponentsforextractingtheUMLelements. spaCyis
widelyadoptedforitsrobustpre-trainedstatisticalmodelsthatdeliverexceptionalperformanceandreliabilityinnatural
languageprocessing(NLP)[22].
InthepreviousstudyconductedbySalemietal. [23],theauthorsestablishedmappingrulestoextractUMLelements
fromtheirdefinedEnglishmetamodel. AspresentedinTable1,weusethesamerulestoidentifytheUMLelements
fromtheEnglishspecification.
AccordingtotheirEnglishmetamodel,IsPropertyOfSignisasub-phrasethatlinkstwosemanticelementsusing“of”.
PrefixElementisasemanticelementplacedimmediatelybeforeanothersemanticelement. TransitiveVerbisaverbthat
takesoneormoreobjects. PrepositionConjunctionisapreposition,suchas“in”and“with”,describingarelationship
betweentwosub-phrasesinasentence. PossessiveDeterminerisasub-phraseofdeterminersthatmodifyanounby
attributingpossessiontosomeoneorsomething. TheexamplesprovidedinTable1areappliedtotheRoyal&Loyal
domainmodelpresentedinFigure3.
4

<!-- Page 5 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4

### Airport

name: String
origin 1 destination 1
departingFlights * arrivingFlights *

### Flight

departTime: Date
arrivalTime: Date
duration: Date
maxNrPassenger: Integer
flights * flight 1
passengers *

### Passenger

minAge: Integer
age: Integer
needsAssistance: Boolean
book(f: Flight)

## Ceo 0..1

airline 1 airline 0..1

### Airline

name: String
Figure2: TheUMLclassdiagramoftheairportdomainmodel.
WhenweappliedspaCytoEnglishspecifications,weobservedthatthePOStaggeridentifiestheEnglishelementsfrom
Table1asnounsandadjectives. Therefore,weextractthenounsandadjectivesfromtheEnglishspecificationandadd
themtotheUMLelementsset. Continuingwiththerunningexample,weobtainthefollowingsetofUMLelements:
Nouns→{number,passengers,flight}

### Adjective→{maximum}

Inthefinalstep,weemployspaCyforlemmatization. ThisprocesstransformstheextractedUMLelementsintotheir
baseform(lemma)byremovinginflectionalendings,suchasthe“-ing”suffix[22]. WestoretheUMLelementsinsets,
whichallowsustoeliminateanyduplicates. Thesesetsformthebasisforrankingthesimplepaths. Afterprocessing
thepreviouslyobtainedset,wegetthefollowingresult:

### UMLelements→{number,passenger,flight,maximum}

Table1: MappingrulesbetweentheUMLelementsfromtheEnglishspecificationtotheequivalentOCLexpression.
Rule EnglishElement EnglishExample OCLElement OCLExample

### Rule2 IsPropertyOfSign Nameofcustomer Customer.name

Rule4 PrefixElement ValidCustomerCard CustomerCard.valid

### AttributeCallExp


### Rule6 TransitiveVerb Customerhasnames Customer.name

Rule7 PrepositionConjunction Transactionwithpoints Transaction.point
Rule3 PossessiveDeterminer Customer’scards Customer.cards

### NavigationCallExp

Rule10 Noun(mappedtoattribute/roles) CustomerCardowner CustomerCard.owner
Rule11 Noun(mappedtoClass) Service UMLElement Service
5

<!-- Page 6 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4
3.3 SimplePathGeneration
Inourpreviousstudy,weintroducedapromptingtechnique,UML-Augmentation,thataugmentsthepromptwiththe
completeUMLclassmodeltogenerateOCLconstraints[4]. However,thistechniqueencounterslimitationswhenthe
UMLclassmodelsizeexceedsthecontextsizethattheLLMcanprocess.
WeaddressthislimitationbydecomposingtheUMLclassmodelintosub-models. Toachievethis,werepresentthe
UMLclassmodelsasgraphstocoverthesimplepathsintheequivalentUMLgraph. TheUMLgraphservesasan
abstract representation of the UML class diagram. The relationship between two UML classes can be directional,
resultinginadirectedgraphrepresentationoftheUMLgraph. Inthisrepresentation,eachnodedenotesaUMLclass,
andeachedgerepresentstherelationshipbetweentwoUMLclasses.
InPathOCL,wegeneratesimplepathsthatcoveralltheUMLclassesintheUMLgraph. Thisisduetothepossibility
thatanEnglishspecificationcanhavemultiplesemanticallyequivalentOCLconstraintsexpresseddifferently[10]. To
accomplishthis,weapplythebruteforcesolutionproposedbyLietal. [13]tocoverallthesimplepathsforagiven
graph. Theirsolutionconsistsofthreealgorithmsthattakethegraphandthesetofinitialandfinalnodesasinputto
generatethesimplepaths.
InthecurrentsettingofPathOCL,weincludealltheUMLclassesintheinitialandfinalinputsets. Asaresult,we
obtainasetofsimplepathsthatcoverallUMLclassesintheUMLgraph. Inaddition,wealsoincludetheUMLclasses
asindividualnodesintheset,asitispossibletoexpressanOCLconstraintusingjustasingleUMLclass,withoutthe
needtonavigatethroughassociations.
ApplyingthesolutiontotheairportdomainmodelinFigure2,wegenerateasetofsimplepathsthatcoverallUML
classes,inadditiontotheindividualUMLclasses. AsubsetofthesimplepathsisshowninListing1.
3.4 SimplePathRanking
Covering all simple paths in a UML graph would result in a significant number of prompts for generating OCL
constraints. Tomanagethis,werankthesimplepathsbasedonthelikelihoodthattheEnglishspecificationappliesto
thesubsetofUMLclasseswithineachsimplepath. Wethenchoosethetop-kpromptsforgeneratingOCLconstraints.
Weachievethisbyassigningeachsimplepathasimilarityscore. Thisscoremeasuresthetextualsimilaritybetweentwo
setsofwords: (a)theUMLelementsextractedfromtheEnglishspecification,and(b)thepropertiesoftheUMLclasses
inthesimplepath. NotethatweonlyconsiderthenameoftheUMLclassproperties,nottheirdatatypeorcardinality.
SimilartotheUMLelementsset,weapplylemmatizationtotheUMLclasspropertiestoobtainthesamebaseformof
words. Furthermore,weonlychoosetherolesattheendofthenextUMLclassinthesimplepath. Forinstance,inthe
simplepath“[Airline,Flight]”fromListing1,weonlyconsidertherole“flights”betweenthe“Airline”and“Flight”
classes. ForasingleUMLclass,suchas“[Airport]”,weonlyincludeitsproperties. StoringtheUMLpropertiesassets
allowsustoremoveanyduplicatesthatmightoccurwhentheinitialUMLclassappearsasthefinalnode,asinthelast
simplepathinListing1. ThefollowingUMLpropertiessetisextractedforthesimplepath“[Airline,Flight]”:
UMLPropertiesSet→{Airline,Flight,name,flight,departtime,arrivaltime,duration,maxnrpassenger}
Now,weusetwosimilaritymetricstoassignscoresforeachsimplepath: (a)Jaccardsimilarityand(b)cosinesimilarity.
[Airport]
[Flight]
[Passenger]
[Airline]
...
[Airline,Flight]
[Passenger,Airline]
[Airline,Passenger]
...
[Passenger,Airline,Flight,Airport]
[Airline,Passenger,Flight,Airport]
[Passenger,Airline,Flight,Passenger]
Listing1: Thesubsetofsimplepathsgeneratedfortheairportdomainmodel.
6

<!-- Page 7 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4
[’Flight’, ’Passenger’] -> 0.25
[’Flight’] -> 0.12
...
[’Passenger’, ’Airline’, ’Passenger’] -> 0.0
[’Airport’] -> 0.0
Listing2: TherankedsubsetofsimplepathsobtainedbyapplyingJaccardsimilarity.
[’Airline’, ’Passenger’] -> 0.40
[’Airline’, ’Flight’, ’Passenger’] -> 0.37
...
[’Flight’] -> 0.31
[’Passenger’] -> 0.30
Listing3: Therankedsubsetofsimplepathsobtainedbyapplyingcosinesimilarity.
3.4.1 JaccardSimilarity
TheJaccardindexisausefulandefficientmethodformeasuringtheoverlapofelementsintwosets[14]. Itiscomputed
usingthegivenequation:

## |E∩P|

Jaccard(E,P)= (1)

## |E∪P|

Here, E represents the set of UML elements extracted from the English specification, and P represents the set of
propertiesfortheUMLclassesinthesimplepath. ItisimportanttonotethattheJaccardsimilarityscoreisbasedon
theexactmatchingbetweenthesetsofwordsanddoesnottakeintoaccountsynonymsandwordcontext. Thisimplies
thatdifferencesinwords,suchasabbreviations(e.g.,serviceNr),arenotaccountedfor.
WhenJaccardsimilarityisappliedtothegeneratedsimplepathsinListing1,theoutcomeistherankedlistshownin
Listing2. Asanticipated,thetop-rankedsimplepathsincludetheUMLclassesrelevanttotheEnglishspecification.
3.4.2 CosineSimilarity
Incertaincases,exactmatchingmaynotbethemosteffectivemethodtoranksimplepaths. Thisissuebecomesclear
whenUMLclasselementsarenotlabeledfollowingaspecificconvention. Forexample,theattribute“maxNrPassenger”
fromFigure2, couldleadtomismatchesduetominorvariationsinthename. Asaresult, weexpandourranking
metricsbymatchingwordembeddingsandassigningsimilarityscoresusingthecosinesimilaritymetric. Thecosine
scoreismeasuredusingthegivenequation:
e·p
Cosine(e,p)= (2)
|e||p|
Here,erepresentstheembeddingvectorofoneelementfromtheUMLelementssetE,andprepresentstheembedding
vectorofonepropertyfromtheUMLclasspropertiessetP.Wecomputethecosinesimilaritybetweenthevectorsof
eachelement,resultinginamatrixforallpossiblepairsinthetwosets. Wetaketheaverageofthematrixandassignit
asthesimilarityscoreforthecorrespondingsimplepath.
WealsoapplycosinesimilaritytothesamesetofsimplepathsgeneratedfromtheairportdomainmodelinListing1.
AsshowninListing3,thetop-ksimplepathsandtheirrankingscoresaredifferentfromtheresultsobtainedusing
Jaccardsimilarity. Thisisattributedtothefactthatwordembeddingsincorporatethesemanticsofthewords,enabling
themtotakeintoaccountsynonymsandvariations.
3.5 OCLConstraintGeneration
PathOCLisversatileandcanbeusedwithanyLLM.Inthisstudy,weconsidertheGPT-4modelbyOpenAI.The
behaviorofGPT-4modelscanbeguidedbysettinginstructionsasthesystemprompts[24]. Ourtemplateforthe
systempromptisshowninListing4.
Inaddition,wehavedesignedafixedprompttemplatethatservesastheuserpromptforgeneratingOCLconstraints.
Thepromptisdividedintotwoparts: (a)theEnglishspecification,and(b)theUMLclassesinthesimplepath. For
7

<!-- Page 8 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4
As a system designer with expertise in UML modeling and OCL constraints, your role is to assist the user in writing OCL
constraints. The user will provide you with the following information:
(1) The specification in natural language.
(2) The UML classes and their properties (attributes, operations, associations).
Your objective is to generate a valid OCL constraint according to the provided UML classes. Please do not provide
explanation. Put your solution in a <OCL> tag.
Listing4: ThesystemprompttemplatetoinstructGPT-4.
-- OCL specification
<English specification>
-- UML properties of class <class name>
{
"attributes":
[
{
<attribute name>: <data type>
}
],
"operations":
]
{
<operation name>: <data type>
}
],
"associations":
[
{
"target": <associated class>,
"role": <association name>,
"multiplicity": <cardinality>
}
]
}
-- OCL constraint
Listing5: TheuserprompttemplatetogenerateOCLconstraints.
eachclassintheselectedpath,weaugmentthepromptwithitsattributes,operations,androleswiththeircardinality.
ThiscontextisformattedinJSON,asshowninListing5.
Toconcludetherunningexample,weapplytheusertemplatetothetop-1simplepathfromListing2. Theproperties
ofboththe“Flight”and“Passenger”classesareaugmentedintheprompt. BelowisacorrectOCLimplementation
successfullygeneratedbytheGPT-4model:
contextFlightinv: self.passengers->size()<=1000
4 EmpiricalEvaluation
ThedatasetusedinourexperimentsispubliclyavailableonZenodo2. Itcontains15UMLclassmodels,withatotalof
168Englishspecifications. WepresenttheRoyal&Loyaldomainmodelforadetailedanalysisofourexperiments.
TheRoyal&Loyalmodelisahypotheticalcompanythatmanagesloyaltyprogramsforbusinesses[25,8]. Figure3
illustratestheUMLclassdiagramofthecasestudy.
4.1 ModelsandConfigurations
WeusetheGPT-4modelastheLLMtogenerateOCLconstraints. Thismodelisconfiguredwithdefaultparameters:
(a)amaximumoutputtokenlimitof256,and(b)atemperaturesettingofzerotoenablereproducingtheresults[24].
Togeneratethewordembeddings,weemploythe“all-MiniLM-L6-v2”modelprovidedbySentence-BERT[26].
2https://zenodo.org/doi/10.5281/zenodo.10841785
8

<!-- Page 9 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4
Figure3: TheUMLclassdiagramoftheRoyal&Loyaldomainmodel.
4.2 EvaluationMetrics
4.2.1 Validity@K
AnOCLconstraintisconsideredvalidifitconformswiththesyntacticalstructureandformattingrulesofOCL[15].
Therefore,thevalidityscore(Validity)representsthepercentageofvalidOCLconstraintsgenerated. Thisscoreis
calculatedbydividingthenumberofOCLconstraints,successfullycompiledbytheUSEtool,bythetotalnumberof
OCLconstraints. Theformulaisasfollows:
ValidOCLConstraints

### Validity = (3)

TotalOCLConstraints
4.2.2 Correctness@K
AcorrectOCLconstraintmustensurethattheexpressionisvalidandaccuratelyimplementstheconstraintsandrules
oftheEnglishspecificationwithinthecontextofitstargetUMLclasses. Thus,thecorrectnessscore(Ccorrectness)
representsthepercentageofcorrectOCLconstraintsgenerated. ThisscoreiscalculatedbydividingthenumberofOCL
constraintsdeemedcorrectbythesoftwaremodeler,usingtheUSEtool,bythetotalnumberofOCLconstraints. The
formulaisasfollows:
CorrectOCLConstraints

### Correctness= (4)

TotalOCLConstraints
4.2.3 McNemar’sTest
Each generated OCL constraint is evaluated to verify its validity and correctness, resulting in the OCL constraint
being classified as either valid or invalid, and correct or incorrect. In our study, we used the same dataset across
allexperiments. Therefore,weapplyMcNemar’stest[27]tostatisticallytestournullhypothesesandcomparethe
PathOCLandUML-Augmentationpromptingtechniques. Thistestiscommonlyusedforpairednominaldatabasedon
a2x2contingencymatrix.
9

<!-- Page 10 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4
Table2: OverallvalidityandcorrectnessscoresforPathOCLandUML-Augmentationpromptingtechniques.
PromptingTechniques Validity(%) Correctness(%)
UML-Aug. &Zero-Shot(Codex) 48.5 35.1
UML-Aug. &Zero-Shot(GPT-4) 47.8 44.0

### PathOCL-Cosine(GPT-4) 57.7 47.6


### PathOCL-Jaccard(GPT-4) 61.9 46.4

4.3 RQ1. HoweffectiveisPathOCLpromptingtechniqueingeneratingvalidandcorrectOCLconstraints?
In our hypotheses, we stated that there is no improvement in both the validity and correctness scores when using
PathOCLasopposedtoUML-Augmentation. However,inourpreviousstudy[4],weusedtheUML-Augmentation
promptingtechniquewithCodexastheLLM.Therefore,ourfirststepistoapplyUML-AugmentationwiththeGPT-4
model,whichwillenableustostatisticallyevaluatethehypotheses.
4.3.1 GPT-4vs. Codex
UsingtheUML-Augmentationpromptingtechnique,wefoundthatGPT-4maintainedsimilarscoresingenerating
validOCLconstraintscomparedtoCodex. However,GPT-4showedasignificant26.5%improvementingenerating
correctOCLconstraints. ThecomparisonofCodexandGPT-4resultsisdisplayedinthetopsectionofTable2.
OurfindingsindicatethattheadvancementsinreasoningabilitiesofGPT-4haveimproveditsunderstandingofEnglish
specifications. ThisleadstoabetteralignmentofOCLconstraintswiththesemanticsofUMLclassmodels. However,
thesyntaxvalidityofOCLconstraintsremainsunchanged. ThisimpliesthatusingtheentireUMLclassmodelas
contextcouldpotentiallyhindertheabilityoftheGPTmodelstorecallthecorrectUMLproperties.
4.3.2 PathOCLEvaluation
We deem an OCL constraint as valid and correct if it is successfully generated by GPT-4 using the top-k prompt.
However, covering all simplepaths could lead to asubstantial set of promptsto evaluate. Therefore, welimit our
experimentstoonlyconsiderthetop-10prompts.Ouranalysisbeginswithevaluatingthesyntaxvalidityofthegenerated
OCLconstraints. AsshowninTable3,wenoticedaconsistentincreaseinthenumberofvalidOCLconstraintswhen
testingvariouspromptsthatcoverdifferentpathsofUMLclasses,usingbothJaccardandcosinerankingmetrics.
TogaininsightsintothemaincausesofGPT-4generatinginvalidOCLconstraints,weusedtheOCLcompilerfrom
theUSEtooltodetectandsummarizethesyntaxerrors. WefoundthatthemostcommonerrorintheinvalidOCL
constraintsoccurredwhentheGPT-4modelreferredtoundefinedandincorrectpropertiesfromtheUMLclasses. The
USEtoolreportedthissyntaxerrorasan“undefinedoperation”,whichcanhavedifferentinterpretationsincertain
cases.
AnexampleisdemonstratedinListing6,wheretheGPT-4modelreferredtotherole“programs”thatisnotdefinedas
apropertyofthe“Transaction”class. However,weobservedthatwhenGPT-4waspromptedwithadditionalprompts
of paths involving different UML classes, it successfully generated a valid OCL constraint for the same example.
ThisalignswiththefactthatanOCLconstraintcanhavealargenumberofalternativeandsemanticallyequivalent
implementations[9,10]. Therefore,exposingtheGPT-4modeltodifferentsetsofUMLclassesallowsforexploring
variationsofuniqueOCLconstraintsthatwouldresultinvalidandcorrectimplementations.
Table3: OverallvalidityandcorrectnessscoresforPathOCLwithtop-kprompts.
Validity(%) Correctness(%)

### RankingMetrics

top-3 top-5 top-10 top-3 top-5 top-10
Jaccard 44.6 50.0 61.9 36.3 39.8 46.4
Cosine 46.4 50.0 57.7 38.0 40.4 47.6
10

<!-- Page 11 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4
Table4: OverallpercentageofthesyntaxerrorcategoriesforPathOCL(Jaccard)andUML-Augmentationprompting
techniques.
PromptingMethod UndefinedOperation ParsingError IterExpInvalidSource SignatureMismatch
UMLInfo.&Zero-Shot 80.5% 15.2% 4.1% 0.2%
PathOCL(Jaccard) 82.5% 9.6% 5.7% 2.2%

### English specification:

The owner of a customer card must participate in at least one loyalty program.

### OCL constraint:

context CustomerCard
inv: self.transactions->exists(t | t.programs->notEmpty())

### Syntax error:

Undefined operation named ’programs’ in expression ’Transaction.programs()’.
Listing6: Anexampleofthe“undefinedoperation”error.
AnothercategoryoferrorsidentifiedisrelatedtothestructureoftheOCLconstraintitself. Parsingerrorsoccurwhen
theOCLparseroftheUSEtoolencountersanOCLconstraintthatdoesnotconformwiththedefinedsyntaxbytheOCL
grammarandrules[15]. AcloserinvestigationrevealedthatsomeoftheOCLconstraintswereimproperlyformatted,
ascanbeseeninListing7,wherethekeyword“inv”hadbeenusedinsteadof“pre”,“post”,or“body”.
InadditiontotheerrorsrelatedtotheUMLpropertiesandtheOCLsyntax,wehaveidentifiedanerrorwiththeiterator
expressions,whicharecommonlyusedinOCLconstraints. Forexample,the“select”iteratorinListing8isbeing
appliedonasingleobjectoftype“CustomerCard”insteadofasetofobjects. Thisisattributedtothefactthatthe
association“card”betweentheclass“Membership”and“CustomerCard”hasacardinalityofone. Anothererroroccurs
whentheoperationreferencedintheOCLconstraintdoesnotmatchitssignatureasdefinedintheUMLclass. Listing
9providesanexamplewheretheoperation“enroll()”isreferencedwithanextrainputparameterthatdoesnotmatch
thedefinitioninthe“LoyaltyProgram”class.
Table4summarizesthepercentagesofeacherrorcategory. WechosePathOCLwiththeJaccardmetricasitisthe
best-performingsettingtopresenttheresults. Wecanobserveamarginaldifferenceinthesyntaxerrorcategories
betweenthePathOCLandUML-Augmentationpromptingtechniques. Thissuggeststhat,regardlessoftheprompting
techniqueused,theGPT-4modelstillfaceslimitationsinaccuratelyreferencingtheUMLpropertiesaccordingtothe
Englishspecification.
4.3.3 PathOCLvs. UML-Augmentation.
Inournullhypothesis(H0-Validity),westatedthatprovidingaselectivesubsetofUMLclasseshasnoimprovement
inthevalidityscorecomparedtoaugmentingtheentireUMLclassmodel. However,ourempiricalresultsinTable
2showthatthePathOCLpromptingtechniquedemonstratesasubstantialimprovementinthevalidityscoreby30%
usingJaccardandby20%usingcosinewhencomparedtotheUML-augmentationtechnique.
Tomeasuretheimprovementstatistically,weuseMcNemar’stesttocomparethevalidityscoresofbothPathOCLand
UML-Augmentationtechniques. McNemar’stestisappliedtothe2x2contingencytable(a)showninFigure4. The
highlightednumbersinthistablearetheoff-diagonalcellsastheyindicatethedifferencesingeneratingvalidOCL
constraintsbetweenthepromptingtechniques. WeusethefollowingequationtocalculateMcNemar’sstatistic(χ2):

### English specification:

The maximum age of participants in loyalty programs is 70.

### OCL constraint:

context Transaction::programs()
inv: self.participants->forAll(p | p.age <= 70)

### Syntax error:

No viable alternative at input ’inv’.
Listing7: Anexampleoftheparsingerror.
11

<!-- Page 12 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4

### English specification:

The number of valid cards for every customer must be equal to the number of programs in which the customer participates.

### OCL constraint:

context Membership
inv: self.card->select(c | c.valid = true)->size() = self.programs->size()

### Syntax error:

Source of ’select’ expression must be a collection, found source expression of type ’CustomerCard’.
Listing8: Anexampleofthe“IterExpInvalidSource”error.

### English specification:

Every customer who enters a loyalty program must be of legal age.

### OCL constraint:

context LoyaltyProgram::enroll(c: Customer)
pre: c.age >= 18

### Syntax error:

This signature of operation ’enroll’ does not match its previous declaration in class ’LoyaltyProgram’.
Listing9: Anexampleofthe“SignatureMismatch”error.

## (B−C)2

χ2 = (5)

## B+C

WhereBisthesecondcellfromthefirstrow,andCisthefirstcellfromthesecondrow. Weset(α=0.05)asthe
significancethresholdtomatchwiththep-valueanddecideonthenullhypothesis. SinceMcNemar’stestfollows
the(χ2)distributionwithonedegreeoffreedom,welookuptheone-tailp-valueviathe(χ2)distribution. Fortable
(a),(χ2)isequalto13.71,andthereforeweobtainap-valueof0.0002,whichisbelowthesignificancethreshold(α
=0.05). Asaresult, weconfidentlyrejectthenullhypothesis(H0-Validity)andacceptthealternativehypothesis
(H1-Validity). Thus,weconcludethatusingthePathOCLpromptingtechniqueimprovesthenumberofvalidOCL
constraintsgeneratedwhencomparedtotheUML-Augmentationtechnique.
Similarly,weproposethatthereisnoimprovementinthecorrectnessscore(H0-Correctness)whenusingPathOCL
comparedtoUML-Augmentation. Tostatisticallytestournullhypothesis,wealsoapplyMcNemar’stesttocompare
theempiricalresultsfromtable(b)inFigure4. Usingequation5,wecalculateMcNemar’sstatistic(χ2)tobeequalto
1.00,resultinginap-valueof.317. Thisvalueishigherthanoursignificancethreshold(α=0.05),therefore,wecannot
confidentlyrejectthenullhypothesis(H0-Correctness)andcannotacceptthealternativehypothesis(H1-Correctness).
Regardless, evenifthestatisticaldifferencemaynotbesignificant, thereisstillaslightincreaseinthenumberof
correctlygeneratedOCLconstraints,asobservedinTable2.
Invalid Valid
dilavnI
dilaV
PathOCL (Jaccard@10)
noitatnemguA-LMU
Incorrect Correct
55 33
9 71
McNemar’s statistic (χ2) = 13.71
p < .001
(a)
tcerrocnI
tcerroC
PathOCL (Cosine@10)
noitatnemguA-LMU
73 21
15 59
McNemar’s statistic (χ2) = 1.00
p = .317
(b)
Figure4: TheMcNemar’s2x2contingencytablesareusedtoevaluateboththePathOCLandUML-Augmentation
promptingtechniques. Table(a)forthevalidityscoresandTable(b)forthecorrectnessscores.
12

<!-- Page 13 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4

## Inference Cost: Pathocl Vs. Uml-


## Augmentation

PathOCL (Jaccard) UML-Augmentation
$10.00
$9.00
$8.00
$7.00
)$
(

## T $6.00


## S


## O


## C


## E $5.00


## C


## N


## E


## R $4.00


## E


## F


## N


## I $3.00

$2.00
$1.00
$-

### K = 1 K = 3 K = 5 K = 10


## Number Of Prompts (Top-K)

Figure5: ComparativeinferencecostanalysisforPathOCL(Jaccard)vs. UML-Augmentation
4.4 RQ2. HowdoestheinferencecostcomparebetweenPathOCLandUML-Augmentationprompting
techniques?
Inthisresearchquestion,weanalyzethecomputationalcostsassociatedwithusingboththePathOCLandtheUML-
AugmentationtechniquestoprompttheGPT-4model. WespecificallyanalyzePathOCLwiththeJaccardmetricasit
overalloutperformswhencomparedwiththecosinemetric.
TheinferencecostsarecalculatedbasedonthepricingmodelofOpenAIfortheirGPT-4model,whichcharged$0.003
per1Kinputtokensconsumedatthetimeofthisstudy3. Thesecostsonlyaccountforthepromptsthatgeneratedvalid
andcorrectOCLconstraints.
Figure5showsthatthetop-1promptcraftedusingPathOCLismorecost-effectivethanUML-Augmentation. Thisis
evidentfromthefactthattheaveragepromptsizeinPathOCLissmaller,asshowninFigure6. However,PathOCL
presentsatrade-off: theinferencecostsincreasesubstantiallywhenachievingimprovedvalidityandcorrectnessscores
bycoveringtop-kpromptswithdifferentsimplepaths,asconfirmedbytheresultsofourexperimentsinTable3.
Now,toinvestigatethescalabilityoftheprompts,wecategorizedtheUMLclassmodelsfromourdatasetintothree
groupsbasedonthenumberofUMLclasses: small,medium,andlarge,asshowninFigure6. Ourdatasetcontains
15UMLclassmodelsintotal,withthesmallestUMLclassmodelhaving2classesandthelargestonecontaining14
classes.
BasedontheresultsshowninFigure6,wecanobservethattheaveragesizeofpromptscraftedusingbothPathOCL
andUML-Augmentationtechniquesisminimalforsmall-sizedUMLclassmodels. However,thescalingtrendbecomes
evidentasthesizeoftheUMLclassmodelgrowslarger. Inaddition,thedifferencebecomessignificantforlargerUML
classmodels,withthesizeofthepromptcraftedusingPathOCLreachingnearlyhalfthesizeoftheUML-Augmentation
prompt.
3November,2023
13

<!-- Page 14 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4

## Prompt Scalability: Pathocl Vs. Uml-


## Augmentation

PathOCL (Jaccard) UML-Augmentation
600
500

## )S


## N


## E


## K


## O400


## T

(

## E


## Z


## Is


## T

300

## P


## M


## O


## R200


## P


## .G


## V


## A100

0

## Small (<= 4) Medium (5-7) Large (>= 8)


## Uml Class Model Size (Number Of Classes)

Figure6: TrendanalysisofthepromptsizescalabilityforPathOCL(Jaccard)vs. UML-Augmentationwithdifferent
UMLclassmodelsizes.
5 Discussion
Ourproposedpromptingtechnique,PathOCL,hasshownasignificantimprovementwhenusedwiththeGPT-4model
to express OCL constraints for UML class models. The improvement can be attributed to the core mechanism of
PathOCL,whichmimicstheapproachtakenbyexperiencedsoftwarepractitionerswhenwritingOCLconstraints. Our
researchshowsthatbyaugmentingaselectivesubsetofUMLclassesrelevanttotheEnglishspecificationascontext,
theGPT-4modelismorelikelytogeneratesyntacticallyvalidandsemanticallycorrectOCLconstraints.
Also,weobservedthatbycoveringthesimplepaths,usingthePathOCLtechniquecouldpotentiallygenerateunique
anddistinctOCLconstraintsforthesameEnglishspecification. However,scalabilitylimitationsmightoccurasthe
complexity and size of theUML classmodels increase, deeming the bruteforce generationinefficient and raising
concernsoverthecomputationalcomplexityofcoveringallsimplepaths. Therefore,furtheroptimizationsinthepath
coveragealgorithmarenecessaryforthePathOCLtechniquetobeappliedinlarge-scaledomainapplicationswhere
computationalresourcesarelimited.
PathOCLhasdemonstrateditsadvantageinchunkingtheUMLclassmodeltosub-modelstoreducethecontextsizeof
theprompt. ThisaddressesalimitationfacedbytheUML-AugmentationtechniquewhenthesizeoftheUMLclass
modelexceedsthecontextwindowofLLMswithsmallercontext,suchasLlama2,whichhasalimitof4096tokens
[28]. ThisimpactisevidentinFigure6,wheretheaveragepromptsoflargerUMLclassmodels(e.g.,theRoyal&
Loyalcase)arealmosthalfthesizeincomparisontoUML-Augmentationprompts. Thisadvantageisbeneficialfor
large-sizeddomainmodelsandiscrucialforefficienton-deviceinferenceinresource-limitedenvironments.
However,theUMLclassmodelsinourdataset,primarilycompiledfromeducationalresources,varyinsizeandmay
notaccuratelyrepresentreal-worldapplications. Therefore,anexhaustivedatasetisrequiredtoensuretheapplicability
ofPathOCLacrossdiversedomainmodels.
Despite the marginal difference in the correctness of the generated OCL constraints between the two prompting
techniques, this behavior can be expected from the GPT-4 model as a generalist model with the ability to achieve
general-purposelanguageunderstandingandgeneration[24]. Therefore,theperformanceofGPT-4islimitedwhenit
comestosoftwaremodelingtasks,suchasunderstandingandexpressingOCLconstraintsforUMLclassmodels. This
limitationcanserveasmotivationforthesoftwaremodelingcommunitytoadapttheintelligenceoffoundationmodels
fordomainmodelingtasks[5,11,4].
14

<!-- Page 15 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4
6 RelatedWork
DifferentNLPandmodeltransformationtechniqueshavebeenusedtoaddressthetranslationofnaturallanguage(i.e.,
English)specificationstoOCLconstraints. Oneapproach,knownasCOPACABANA[7],isasemi-automaticpatternbasedapproachthatrequireshumaninterventionduringthetranslationprocess. AnotherapproachisNL2OCLviaSBVR
[8], an MDA-based tool that automatically transforms English specifications to an intermediate representation in
SemanticsofBusinessVocabularyandRules(SBVR),andthentoOCLconstraints. Salemietal. [23]proposedanother
approachcalledEnglish2OCL(En2OCL).TheirapproachtakestheEnglishspecificationandtheUMLclassmodelas
inputtogeneratetherequiredOCLconstraint. ItalsoincludesthedefinitionofmappingrulestoanalyzetheEnglish
specificationandextracttheUMLelementsthatcanbemappedtotheirequivalentOCLexpression.
RecentstudiesexploredthereliabilityofLLMsinthemodel-drivendevelopmentdomain. Inourpreviousstudy[4],
weevaluatedCodexingeneratingOCLconstraintsfromEnglishspecificationsusingdifferentprompttemplatesand
techniques. WeaugmentedtheentireUMLclassmodelinthepromptandassessedbothzero-andfew-shotprompting
settings. TheresultsdemonstratedthatprovidingtheUMLclassmodelascontextsignificantlyimprovedthereliability
oftheOCLconstraints. AnotherstudybyCamaraetal. [5]exploredthecapabilitiesofChatGPTinsupportingdomain
modeling tasks. Their findings demonstrated that ChatGPT performed well in dealing with small domain models,
althoughithadsomelimitationsinbasicmodelingconcepts. Additionally,theyalsoobservedremarkableperformance
ingeneratingOCLconstraints.
7 ThreatstoValidity
Largelanguagemodel. TheprimaryconcernrevolvesaroundanypotentialbiaseswithintheGPT-4modelitself. As
thetrainingdatasetofGPT-4isnotpubliclydisclosed,theremaybeariskofbias. Thedatasetweusedinourstudywas
curatedfromeducationalresourcesthatarepubliclyavailableontheinternetandGitHub. Hence,thereisapossibility
thatUMLclassmodels,Englishspecifications,andtheirOCLconstraintscouldbepresentinthetrainingdataset. In
addition, OpenAIhoststheGPT-4modelandoffersitasanAPIservice. However, itisimportanttonotethatthe
performancemayvaryandresultsmightnotbereproducedidentically,evenwithazerotemperaturesetting. Therefore,
consistentbehaviorcannotalwaysbeguaranteed.
Qualityofthedataset. TheUMLclassmodelsinourdatasetaresourcedfromeducationalresources. Assuch,itis
importanttoacknowledgethattheEnglishspecificationsandtheirOCLconstraintsmaynotbeexhaustive. Therefore,
our findings may not entirely reflect real-world applications. A more diverse dataset would lead to a robust and
comprehensiveevaluationofPathOCLandotherpromptingtechniques.
USEmodelingtool. TheUSEmodelingtool,asstatedonitsGitHubrepository,isprimarilydesignedasaresearch
prototype[17]. Asaresult,itmaynotbefullydeveloped,thoroughlytested,orstable. Thiscouldleadtounexpected
behaviorsorlimitationsthatmayimpactourstudyresultswhenevaluatingtheOCLconstraints.
8 Conclusion
Inthisstudy,wepresentPathOCL,apath-basedpromptingtechniquethatcombinesnaturallanguageprocessingwith
simple path coverage to selectively augment a subset of UML classes relevant to the specified requirements. Our
researchdemonstratesthatPathOCLimprovesthevalidityandcorrectnessoftheOCLconstraintsgeneratedbythe
GPT-4modelcomparedtotheUML-Augmentationtechnique.
Overall,thePathOCLtechniquesignificantlyimprovedthevalidityscore. However,therewasaslightincreaseinthe
numberofcorrectlygeneratedconstraints,suggestingaminimalimpactonsemanticcorrectness. Thisalignswiththe
general-purposenatureofGPT-4,whichfaceslimitationsinspecializeddomainssuchassoftwaremodelingandOCL
constraints.
Additionally,weevaluatedtheinferencecostsandthescalabilityofpromptscraftedwhenusingthePathOCLtechnique.
ThecurrentimplementationofPathOCLhasshownitseffectivenessinreducingthecontextsizeofpromptsbynearly
halfwhenscalingUMLclassmodels. However,testingpromptswithdistinctsimplepathsisnecessarytoachieve
improved scores over the UML-Augmentation technique. This represents a trade-off decision when adopting the
PathOCLtechnique.
In conclusion, PathOCL emerges as a promising technique that can improve the effectiveness of LLMs, such as
GPT-4,ingeneratingreliableOCLconstraints. AlthoughitsignifiesprogressinautomatedOCLgeneration,further
optimizationofthePathOCLapproachandadaptationoffoundationmodelsforsoftwaremodelingtaskscouldleadto
morewidespreaduseoftheOCLlanguage.
15

<!-- Page 16 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4

### References

[1] GitHub. Githubcopilot: Youraipairprogrammer. https://github.com/features/copilot,2023.
[2] AngelaFan,BelizGokkaya,MarkHarman,MityaLyubarskiy,ShubhoSengupta,ShinYoo,andJieM.Zhang.
Largelanguagemodelsforsoftwareengineering: Surveyandopenproblems,2023.
[3] CeZhou,QianLi,ChenLi,JunYu,YixinLiu,GuangjingWang,KaiZhang,ChengJi,QibenYan,LifangHe,
HaoPeng,JianxinLi,JiaWu,ZiweiLiu,PengtaoXie,CaimingXiong,JianPei,PhilipS.Yu,andLichaoSun. A
comprehensivesurveyonpretrainedfoundationmodels: Ahistoryfromberttochatgpt,2023.
[4] S.Abukhalaf,M.Hamdaqa,andF.Khomh. Oncodexpromptengineeringforoclgeneration: Anempiricalstudy.
In2023IEEE/ACM20thInternationalConferenceonMiningSoftwareRepositories(MSR),pages148–157,Los
Alamitos,CA,USA,may2023.IEEEComputerSociety.
[5] Javier Cámara, Javier Troya, Lola Burgueño, and Antonio Vallecillo. On the assessment of generative ai in
modelingtasks: Anexperiencereportwithchatgptanduml. Softw.Syst.Model.,22(3):781–793,may2023.
[6] M. Chaaben, L. Burgueno, and H. Sahraoui. Towards using few-shot prompt learning for automating model
completion.In2023IEEE/ACM45thInternationalConferenceonSoftwareEngineering:NewIdeasandEmerging
Results(ICSE-NIER),pages7–12,LosAlamitos,CA,USA,may2023.IEEEComputerSociety.
[7] MichaelS.Wahler. Usingpatternstodevelopconsistentdesignconstraints. Doctoralthesis,ETHZurich,Zürich,
2008.
[8] B.Bordbar,M.G.Lee,andI.Bajwa. Oclconstraintsgenerationfromnaturallanguagespecification. In201317th
IEEEInternationalEnterpriseDistributedObjectComputingConference,pages204–213,LosAlamitos,CA,
USA,oct2010.IEEEComputerSociety.
[9] JordiCabotandErnestTeniente.Transformationtechniquesforoclconstraints.ScienceofComputerProgramming,
68(3):179–195,2007.
[10] HongLu,ShuaiWang,TaoYue,shaukatAli,andJanF.Nygård. Automatedrefactoringofoclconstraintswith
search. IEEETransactionsonSoftwareEngineering,45(2):148–170,2019.
[11] JordiCabot,DavidDelgado,andLolaBurgueño. Combiningoclandnaturallanguage: acallforacommunity
effort. InProceedingsofthe25thInternationalConferenceonModelDrivenEngineeringLanguagesandSystems:
CompanionProceedings,MODELS’22,page908–912,NewYork,NY,USA,2022.AssociationforComputing
Machinery.
[12] PaulAmmannandJeffOffutt. Introductiontosoftwaretesting,May2018.
[13] NanLi,FeiLi,andJeffOffutt. Betteralgorithmstominimizethecostoftestpaths. InProceedingsofthe2012
IEEEFifthInternationalConferenceonSoftwareTesting,VerificationandValidation,ICST’12,page280–289,
USA,2012.IEEEComputerSociety.
[14] PaulJaccard. Thedistributionoftheflorainthealpinezone. TheNewPhytologist,11(2):37–50,1912.
[15] ObjectManagementGroup(OMG). ObjectConstraintLanguageSpecificationsVersion2.4. 2014.
[16] JordiCabotandMartinGogolla. ObjectConstraintLanguage(OCL):ADefinitiveGuide,pages58–90. Springer
BerlinHeidelberg,Berlin,Heidelberg,2012.
[17] MartinGogolla,FabianBüttner,andMarkRichters. Use: Auml-basedspecificationenvironmentforvalidating
umlandocl. ScienceofComputerProgramming,69(1):27–34,2007. SpecialissueonExperimentalSoftwareand
Toolkits.
[18] PengfeiLiu,WeizheYuan,JinlanFu,ZhengbaoJiang,HiroakiHayashi,andGrahamNeubig. Pre-train,prompt,
andpredict: Asystematicsurveyofpromptingmethodsinnaturallanguageprocessing,2021.
[19] JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,BrianIchter,FeiXia,EdChi,QuocLe,andDenny
Zhou. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels,2023.
[20] HungLe,HailinChen,AmritaSaha,AkashGokul,DoyenSahoo,andShafiqJoty. Codechain: Towardsmodular
codegenerationthroughchainofself-revisionswithrepresentativesub-modules,2023.
[21] OriRam,YoavLevine,ItayDalmedigos,DorMuhlgay,AmnonShashua,KevinLeyton-Brown,andYoavShoham.
In-contextretrieval-augmentedlanguagemodels,2023.
[22] InesMontani,MatthewHonnibal,MatthewHonnibal,AdrianeBoyd,SofieVanLandeghem,andHenningPeters.
explosion/spaCy: v3.7.2: FixesforAPIsandrequirements,October2023.
[23] SaminSalemi,AliSelamat,andMarekPenhaker. Amodeltransformationframeworktoincreaseoclusability.
JournalofKingSaudUniversity-ComputerandInformationSciences,28(1):13–26,2016.
16

<!-- Page 17 -->

PathOCL:Path-BasedPromptAugmentationforOCLGenerationwithGPT-4
[24] OpenAI. Gpt-openaiapi. https://platform.openai.com/docs/guides/gpt, 2023. [Online; accessed
23-October-2023].
[25] CharlesAshbacher. Theobjectconstraintlanguagesecondedition,gettingyourmodelsreadyformda,byjos
warmerandannekekleppe. TheJournalofObjectTechnology,2:139,2003.
[26] NilsReimersandIrynaGurevych. Sentence-bert: Sentenceembeddingsusingsiamesebert-networks,2019.
[27] QuinnMcNemar. Noteonthesamplingerrorofthedifferencebetweencorrelatedproportionsorpercentages.
Psychometrika,12(2):153–157,1947.
[28] HugoTouvron,LouisMartin,KevinStone,PeterAlbert,AmjadAlmahairi,YasmineBabaei,NikolayBashlykov,
Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya
Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao,
VedanujGoswami,NamanGoyal,AnthonyHartshorn,SagharHosseini,RuiHou,HakanInan,MarcinKardas,
ViktorKerkez,MadianKhabsa,IsabelKloumann,ArtemKorenev,PunitSinghKoura,Marie-AnneLachaux,
ThibautLavril,JenyaLee,DianaLiskovich,YinghaiLu,YuningMao,XavierMartinet,TodorMihaylov,Pushkar
Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan
Schelten,RuanSilva,EricMichaelSmith,RanjanSubramanian,XiaoqingEllenTan,BinhTang,RossTaylor,
AdinaWilliams, JianXiangKuan, PuxinXu, ZhengYan, IliyanZarov, YuchenZhang, AngelaFan, Melanie
Kambadur,SharanNarang,AurelienRodriguez,RobertStojnic,SergeyEdunov,andThomasScialom. Llama2:
Openfoundationandfine-tunedchatmodels,2023.
17

## Tables

**Table (Page 5):**

| Airport |
|---|
| name: String |
|  |


**Table (Page 5):**

| Flight |
|---|
| departTime: Date arrivalTime: Date duration: Date maxNrPassenger: Integer |
|  |


**Table (Page 5):**

| Passenger |
|---|
| minAge: Integer age: Integer needsAssistance: Boolean |
| book(f: Flight) |


**Table (Page 5):**

| Airline |
|---|
| name: String |
|  |


**Table (Page 13):**

|  |  |
|---|---|
|  |  |
