---
title: "Enhancing Security Copilot Prompt Engineering"
original_file: "./Enhancing_Security_Copilot_Prompt_Engineering.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["https", "careful", "about", "org", "however", "arxiv", "code", "buffer", "security", "prompt"]
summary: "<!-- Page 1 -->

Enhancing Security of AI-Based Code Synthesis with GitHub
Copilot via Cheap and Efficient Prompt-Engineering

### JakubRes IvanHomoliak MartinPerešíni

iresj@fit.vut.cz ihomoliak@fit.vut.cz iperesini@fit.vut.cz
BrnoUniversityofTechnology, BrnoUniversityofTechnology, BrnoUniversityofTechnology,
FacultyofInformationTechnology FacultyofInformationTechnology FacultyofInformationTechnology
CzechRepublic CzechRepublic CzechRepublic

### AlešSmrčka KamilMalinka PetrHanacek

smrcka@fit."
related_documents: []
---

# Enhancing Security Copilot Prompt Engineering

<!-- Page 1 -->

Enhancing Security of AI-Based Code Synthesis with GitHub
Copilot via Cheap and Efficient Prompt-Engineering

### JakubRes IvanHomoliak MartinPerešíni

iresj@fit.vut.cz ihomoliak@fit.vut.cz iperesini@fit.vut.cz
BrnoUniversityofTechnology, BrnoUniversityofTechnology, BrnoUniversityofTechnology,
FacultyofInformationTechnology FacultyofInformationTechnology FacultyofInformationTechnology
CzechRepublic CzechRepublic CzechRepublic

### AlešSmrčka KamilMalinka PetrHanacek

smrcka@fit.vut.cz malinka@fit.vut.cz hanacek@fit.vut.cz
BrnoUniversityofTechnology, BrnoUniversityofTechnology, BrnoUniversityofTechnology,
FacultyofInformationTechnology FacultyofInformationTechnology FacultyofInformationTechnology
CzechRepublic CzechRepublic CzechRepublic

## Abstract

person *newPerson = (person *)malloc(sizeof(person));
AIassistantsforcodingareontherise.Howeveroneofthereasons newPerson->status = 0;
developersandcompaniesavoidharnessingtheirfullpotentialis
thequestionablesecurityofthegeneratedcode.Thispaperfirst
reviews the current state-of-the-art and identifies areas for im- Fig.1:ExampleofsecurityissuegeneratedbyAI.Thesceprovementonthisissue.Then,weproposeasystematicapproach nariocomesfromthedatasetproposedin[17].
basedonprompt-alteringmethodstoachievebettercodesecurity
of(evenproprietaryblack-box)AI-basedcodegeneratorssuchas
GitHubCopilot,whileminimizingthecomplexityoftheapplicawaysofimprovingit(seeSec.5.2).Whileobservingthevalidity
tionfromtheuserpoint-of-view,thecomputationalresources,and
orcorrectness,manystudiesoverlookthecrucialaspectofcode—
operationalcosts.Insum,weproposeandevaluatethreeprompt
security.
alteringmethods:(1)scenario-specific,(2)iterative,and(3)general
In the motivating example, the AI assistant was tasked with
clause,whilewediscusstheircombination.Contrarytotheaudit
generatingacodesnippettofillagapinthecontextofaCprogram.
ofcodesecurity,thelattertwooftheproposedmethodsrequire
Itsobjectivewastocreateanewinstanceofthestructure"person"
noexpertknowledgefromtheuser.Weassesstheeffectivenessof
andassignastatusvalueofzerotoit.AlthoughtheAIassistant
theproposedmethodsontheGitHubCopilotusingtheOpenVPN
providedareasonablecode(seeFig.1),thesnippetcontainCWE-
projectinrealisticscenarios,andwedemonstratethattheproposed
476[25](themallocfunctioncouldfailtoallocatememory,thus
methodsreducethenumberofinsecuregeneratedcodesamples
resultinginaNULLpointerdereference).
by up to 16% and increase the number of secure code by up to

### Inthisresearch,weaimtostudyvariouswaysofimproving

8%.Sinceourapproachdoesnotrequireaccesstotheinternalsof
codesecuritygeneratedbyanyproprietaryLargeLanguageModtheAImodels,itcanbeingeneralappliedtoanyAI-basedcode
els(LLMs),andwedemonstrateourapproachonthewell-known
synthesizer,notonlyGitHubCopilot.
GitHubCopilot[6].

### There exist a few categories for improving the code synthe-

1 INTRODUCTION sisofAImodels,suchasoutputoptimization,modelfine-tuning,
WiththereleaseofChatGPT[1],publicattentionshiftedtowards and prompt engineering, and each of them has some pros and
AIassistanttools.Theseassistantsareproficientinmanyareas, cons. In this work, we focus on efficiency, generality, and low
includingsoftwareengineeringorcoding.TheadventofAIcoding costs,andthereforepromptengineeringisthemostsuitabletechassistantsmeanstransitioningfromintelligentcode-completion niqueforus.Whileliteratureforpromptengineeringismostly
toolstocode-generatingtools.AlthoughtheseAIassistantsarefar general[14][31][5][4],wearemorespecificanddeterminefourapfromperfect,intermsofsolvingcodingproblems,arecentmodel proachestoit,whichwefurtherinvestigate:(1)scenario-specific
AlphaCode2,proposedbyDeepmind,scoredbetterthanover85% informationandwarningproviding,(2)iterativesecurity-specific
ofhumancompetitors[9]. prompting,(3)generalalignmentshiftingusinginceptionprompt
AccordingtoLiangetal.[11]inthesurveywith410Githubusers’ (i.e.,generalclause),(4)cooperativeagentssystem.Inparticular,
responses,70%ofrespondentswhohadexperienceswithGithub weexperimentwiththeformerthreeapproachesthatareorthogo-
Copilotutilizeitatleastonceinamonthwhile46%utilizetheAI nalintheirprinciples.
assistantdaily.ThemostfrequentreasonsfordevelopersusingAI

### Contributions. Thecontributionsofourpaperareasfollows:

assistantswerefewerkeystrokestowritecodeandfastercoding.
DuetotherapidlyrisingpopularityofAIassistants,researchers (1) Wereviewedtheliteratureandidentifiedthreedifferent
startedtofocusonstudyingthequalityofthesynthesizedcodeand areasofcodesynthesisimprovementsofLLMs,involving
4202
raM
91
]RC.sc[
1v17621.3042:viXra

<!-- Page 2 -->

JakubRes,etal.
optimizingtheoutput,modelfine-tuning,andpromptoptimizations.
(2) Withthefocusongenerality,speed,andlowcosts,weaimed
atpromptengineeringarea,andweproposedasystematic
approachtoenhancingitsgeneratedcodesecuritywith
threemethodsandtheircombinations.
(3) Weevaluatedtheefficiencyofproposedmethodsforprompt
alterationonareal-worldprojectOpenVPNandwemanagedtoincreasetheratioofsecurecodegeneratedbyup
to8%anddecreasetheratioofgeneratedinsecurecodeby
upto16%.
Organization. InSec.2wedefinetheimportanttermsforour
paperandsetadesignspace.InSec.3wedescribetheproposed
methodsofpromptimprovement.InSec.4wedescribethedesign
oftheexperiment,methodology,dataset,andassessmentofsecurity
withmeasuredresults.WerefertotherelatedworkinSec.5.We
discussthelimitationsandareasforfutureresearchinSec.6.In
Sec.7weconcludeourwork.

## 2 Backgroundanddesignspace


### Prompt. Theprompt,inthecontextofthiswork,referstothetuple:

(1)ataskthatcontainsfunctiondeclarationanditsdescription,(2)
codeofthecontext,and(3)theuser-specifiedcodecommentary
relatedtosecurity.
ImprovementsofCodeSynthesis. Ingeneral,theliteraturecontainsthreemainareasofpossibleimprovementstotheLLMcodegeneratingabilities(seeFig.2):
(1) Output optimizing – The first and the most intuitive
approachistopost-processtheoutput.OncetheLLMrespondswitharesult,theobtainedcodeisanalyzedforthe
presenceofsecurityissues.Althoughtheoutputcorrectionisaddressedbymanyworks[28][30][29],verylittle
attentionisgiventothecodesecurity.
Theremaybemultipleimplementationsoftheoutputcorrectionsystems,eitherbydesigninganothermodeltrained
specificallyforfixingsecurityissuesorbycombiningstatic
analyzerswithissue-repairingrules.Snyk[24]isanexampleofanexistingcommercialoutputoptimizerfocusingon
codesecurity.
(2) Modelfine-tuning–Themodelfine-tuningallowsthe
developerstoadaptthepre-trainedlanguagemodeltobetterfitaspecifictask[33].Itisthemostpreferablesolution

### Input

Model Output
(Prompt)
sisehtnys
edoC
stnemevorpmI
enilepip
person *newPerson = NULL;
newPerson = (person *)malloc(sizeof(person));
if (!newPerson) {
printf("Error: Failed to allocate memory for
person");
return EXIT_FAILURE;
}
newPerson->status = 0;
Fig.3:Preliminaryresultsofpromptenhancing.
duetotheuserexperiencesincetheusercandirectlyinteractwiththeimprovedmodelwithoutanyadditionalsteps.
However,thismethodrequiresfullaccesstothemodeland
imposesahighperformanceoverheadforitsre-training.
(3) Promptoptimizing–Thelastwaytoimprovecodesecurityistooptimizetheuserinput.Asshownbyprevious
works[17][32][13][8],theformulationofaninputprompt
couldseverelyaffecttheresultingcodesecurity.Additionally,theresultsofNeilPerry,etal.[18]indicate,thatitis
possibletopositivelyinfluencethegeneratedcodesecurity
byalteringthepromptoraskingtheLLMiteratively.
Apartfromoptimizingtheinputprompt(ordirectlythe
inputsequenceoftokens),theworkofHeandVechev[7]
presentsanapplicationoftheconceptofprefixtuning[10].
However, this concept is only applicable in cases of onpremisemodelssinceaccesstotheinternalhiddenstateof
modelsisneeded.
2.1 DesignSpace

### Althoughmodelfine-tuningmightachievepromisingresults,it

hasseveralconssuchasrequiringaccesstothefullmodelofoften
proprietaryarchitectures,itisexpensiveintermsofcomputation
resources,anditneedshigh-qualitynewdatatotrainitsmodel
(whichisdifficulttocollect/obtain).Outputoptimizingdoesnot
requireaccesstothearchitectureofthemodelnorrequiresexpert
knowledge,butithasmanyconsrelatedtostaticanalysisofthe
code(i.e.,highfalsenegatives/positivesratesorinabilitytoanalyze
incompletecode).Ontheotherhand,prompt-optimizingisfastand
requiresalmostnocomputationalresources(otherthanre-running
theLLM);however,itmightrequirecertainexpertknowledgein
somecases

### Inourresearch,weemphasizedlow-performanceoverhead,low

costs,generality,andavailability.Therefore,wefocusonprompt
optimization techniques as a way of improving the security of
(3) (2) (1) AI-generatedcode.Preliminaryresultsofpromptengineeringtech-

### Prompt Model fine- Output

niques proposed in our research were applied to the same task
optimizing tuning optimizing
asintheintroduction(seeFig.1)butwithanadditionalprompt
specificationtofocusonpropersecuritypractices(seeFig.3)–the
generatedcodedoesnotcontainweaknessCWE-476.

### Whileliteratureforpromptengineeringtechniquesismostly

general[14][31][5][4],weaimtobemorespecificanddetermine
fourapproachestoit,whichwefurtherdetailinSec.3:(1)scenariospecificinformationandwarningproviding,(2)iterativesecurityspecificprompting,(3)generalalignmentshiftingusingincep-
Fig.2:Potentialimprovementsofcodesynthesis.
tionprompt[8],(4)cooperativeagentssystem[19].

<!-- Page 3 -->

EnhancingSecurityofAI-BasedCodeSynthesiswithGitHubCopilotviaCheapandEfficientPrompt-Engineering
(1) FixtheCWE284-ImproperAccessControl
void string_null_terminate(char *str, int len, int
(2) FixtheCWE435-ImproperInteractionBetweenMultipleCorrectlycapacity)

### BehavingEntities

{} (3) FixtheCWE664-ImproperControlofaResourceThroughitsLifetime
Listing1:Originalprompt (4) FixtheCWE682-IncorrectCalculation
(5) FixtheCWE691-InsufficientControlFlowManagement
// Be careful about the buffer overflow, underflow (6) FixtheCWE693-ProtectionMechanismFailure
(7) FixtheCWE697-IncorrectComparison
and null dereference
(8) FixtheCWE703-ImproperCheckorHandlingofExceptionalConvoid string_null_terminate(char *str, int len, int
ditions
capacity) (9) FixtheCWE707-ImproperNeutralization
{} (10) FixtheCWE710-ImproperAdherencetoCodingStandards

### Listing2:Alteredprompt

Fig.5:Rulesetfortheiterativemethod.
Fig.4:Exampleofinputpromptalteration.
andthereforecoverawiderangeofsecurityweaknessesandissues.
3 PROPOSEDAPPROACH Thankstothat,theuserdoesnotrequireexpertknowledgeandcan
beprovidedwithhighersecurity-levelsuggestions.Forevaluation
In this section, we aim to explore the potential of three of the
purposes,weopttoimplementMitre’sResearchconcepts[26]into
determinedmethodsinSec.2.1–thescenario-specific,theiterative,
theruleset,asseeninFig.5.Thisviewconsistsoftenabstract
andthegeneralalignmentshifting(furtherreferredtoasgeneral
classes,eachcoveringafamilyofsecurityweaknesses.Together,
clause). The last determined approach (i.e., cooperating agents)
theclassesaredesignedtocontainallCWEs.
combinesalloftheothermethodsandisthusdependentonthose

### Theiterativemethodinherentlycomeswithafewadvantages,

methods,weconsideritasadedicatedbranchofresearch;therefore,
suchasalmostnorequirementsforsecurityknowledgefromthe
wedonotdealwithitinthecontextofthiswork.Inthefollowing,
sideofauser,easeofautomaticimplementation,orapplication
wedescribetheparticularapproachesindetail.
toalargescopeofmodels.However,thedisadvantages,suchas
thenegativeinfluenceofimproperlydesignedruleset,orrequired
3.1 Scenario-Specific
computationaltimeformultipleiterations,mayoutweightheposi-
Thefirstmethodaimstoprovidespecificinformationaboutthe tivepropertieswithconsiderationofreasonsforapplicationofthis
localcontexttotheAIassistant.Thepromptthusprovidesnotonly methodinthefuture.
requirementsforthecorrectfunctionalityofgeneratedcode,but
alsoforspecificsecurity-relatedcharacteristics. 3.3 GeneralAlignmentShifting
The whole idea lies in enumerating possible issues based on

### Themainideaofthisapproach(a.k.a.,generalclause)isinspiredby

the developer’s experience. As a part of the prompt, numerous
theworkofLi,etal.[8].Theauthorsproposedtheterminception
warningsandadditionalinformationareprovidedtotheAIassistant
promptthatdescribesanalignment-settingpromptatthestartof
accordingtoexpectedfunctionalityandpossiblesecurityissues
aconversationwithamodel.Weuseadifferentterm(i.e.,general
regardingtheparameterscomingtoaparticularblockofcode.
clause)thantheoriginalauthorssinceourapproachprincipally
Themaindownsideofthismethodistheexpertknowledgerediffersbynotfollowingtheconversationpattern.
quirements.Therefore,tosuccessfullyapplythisapproach,usersare

### Theinceptionpromptisaninputmessagethatcomesbefore

expectedtohaveatleastabasicawarenessofsecureprogramming
anyoftheusersentences.Asforthenatureofourapproach,the
andthepotentialrisksposedbyincorrectlyusedprogramming
generalclauseisapartoftheuserprompt(withinthecontext).
structures.Ontheotherhand,inthecaseofthisapproach,many
promptalterationscanbeautomaticallyproposedtotheuserbased
onthecontextanddatatypes,whichmitigatetheexpertknowledge
requirementsoftheuser.TheexampleinFig.4depictsasingle
/**
promptfortheAIassistantalterationusingtheproposedmethod. * Never forget you are a security specialist helping
with coding tasks.
3.2 Iterative * Your job is to generate code that is secure and
safe.
Thesecondmethodappliesanaiverepeatedprocesstoprompt * Never forget that.
alterationbymodifyingcommentaryofpreviouslygeneratedcode * You are not a programmer, you are a security
sample(thatisthepartofthecontextforthecurrentiteration).It specialist.
* You will never generate code that contains security
communicateswiththeAIassistantiteratively,witheachiteration
vulnerabilities.
incorporating the previous output while adding information or
* You will always look for CWEs in the code you would
warning. generate and fix them.
Themostimportantpartofthisapproachistheproperselection **/
ofthesequenceofadditionalinformationpassedtotheLLMinevery
round.Thismethodisagnostictothetaskanditscodecontext.The
Fig.6:Generalclauseusedforexperiments.
listofcommentariesthatisiterativelyappliedshouldbegeneral,

<!-- Page 4 -->

JakubRes,etal.

### Themainadvantageofthismethodisthesimplicityandeaseof

implementation.Asinglewell-craftedcommentaryadditiontothe Dataset Scenario re V n i e r w tu a a b l le LLM results
headerofthefilecouldimprovethesecurityofthegeneratedcode environment cache
inthisparticularfile.

### Open-source

Ontheotherhand,theremaybemajorissueswiththeperfor- Iterative LLM
project
manceoftheclausemethod.Forexample,theLLMmayfilterout
thegeneralclauseasirrelevant(dependingonthedecisionofthe General
model).Anothersignificantlimitationofthisapproachistheclause Clause
itself.Theclauseneedstobepreciselycuratedtoposeanimpacton
thedecisionprocessofLLM.Alikethepreviousmethod,eventhe Security
assesment
generalclausemethodimposesnonetoverylittleexpertknowledge
requirementstotheusers.
Fig.7:Experimentdesignscheme.

## 4 Experiments

Intheupcomingsection,wedescribetheexperimentdesign(see Unalteredprompts,consistingonlyoftaskandcontext,wereused
Fig.7).First,wechosetheopen-sourceprojectOpenVPNinsteadof asabaselineforthefinalcomparison.Tocapturedivergenceincomtheconventionaldatasetbecauseitreflectstherealconditionsfor monresults,weconsecutivelysynthesizedthefivebestsolutions
operatingtheGitHubCopilot(i.e.,providingthetaskswithcontext) foreveryprompttoprovidehigherstatisticalsignificance.1
andthusproducingresultswithhigherimpact.WeusetheGitHub
Copilottoconsecutivelysynthesizethefivebestsolutionsforeach 4.2 Dataset
selectedtasktosetabaseline.Then,weenhancethecontextand
Totesttheproposedmethodsofpromptalterationinrealisticcontaskbyaddingsecurity-relatedcommentaryaccordingtotheproditions,weoptedforacustomexperimentusinganactiveopenposedmethods.Afterthat,werepeatthesynthesisstep,resulting
sourceprojectinsteadofusingtheconventionaldataset(suchas
in100solutions(25pertheenhancementmethod).Attheend,we
HumaEval[3],MBXP[2],SecurityEval[23],orLLMSecEval[27]).
describetheprocessofassessingthesecurityofsynthesizedcode
Wewillreleaseourdatasetuponpublication,includingthesetup
andmeasuredresults.
ofourexperimenttoenablereproducibilityoftheresearch.
TherearemultiplelimitationsofexistingdatasetsforAI-based
codesynthesis.Mostoftheexistingdatasetsarenotfocusedon
4.1 Methodology securityevaluationbutratherontheabilitytosynthesizefunctional
Althoughmanymodelsanddatasetsareavailable,thispaperfo- code.
cusessolelyonprovingtheconceptofsystematicpromptaltering Ontheotherhand,theexistingsecurity-relateddatasetsconsist
toachievebettercodesecurity.Thus,fortheexperimentalpart ofexamplescenariosofvariousCWEswithoutcontext,andthey
ofthiswork,weusethemostpopularAIcodegeneratortoday wereeithergatheredonlineorcraftedbytheauthors.TheCWEs
[11],GitHubCopilot[6].Throughouttheexperiments,theparam- datasetsaremoresuitableforevaluatingthesynthesizedcodeseetersoftheGitHubCopilotmodelwerekepttothedefault.For curity;however,allthesamplesincludedinthedatasetsareshort,
anuntaintedenvironment,acontainerwithapreinstalledGitHub andthuslackingcontext.

### CopilotextensionforVimeditorwassetupandreinitializedafter

OpenVPNProject. Toreflecttherealityofusingtheprogrameachexperimentrun. ming AI assistant,wechose project OpenVPN.2 The OpenVPN

### ThewholeprocessofexperimentsisdepictedinFig.7.Asstated

projectwasselectedduetoitsactivedevelopment,well-documented
before,thestudyaimstoevaluatetheeffectivenessofsuggested
sourcecode,andtheprimaryprogramminglanguage–C,whichis
methodsonanopen-sourceprojectinsteadofwell-knowndatasets
pronetosecurityissues.
forsynthesizedcodeevaluation.Usingtheopensourceprojectcode

### ThefollowingfunctionsfromtheOpenVPNprojectwereselected

base(seeSec.4.2),weselectedfivetasksandalteredthemaccording
astasksfortheexperiment.Eachfunctionwasselectedwithregard
tothemethodspresentedearlier.Eachofthemethodsisapplied
topossiblesecurityissues:
differently:
(1) string_null_terminate()–possiblyvulnerabletobuffer
overflow/underflowandNULLdereference.(/src/openvpn/
(1) Thescenariomethod–theaddedinformationisinserted buffer.c)
insideofthecurlybracketsoftheobservedfunction.
void string_null_terminate
(2) Theiterativemethod–eachiterationisforwardedtothe
(char *str, int len, int capacity) {}
upcomingroundasacommented-outcodewithadditional
informationfollowingtheruleset(seeFig.5).
(3) Thegeneralclausemethod–theclauseisinsertedright 1NotethatGitHubCopilotsynthesizestensolutionsforeachprompt,andwealways
consideredonlythebestone.Ontheotherhand,othersynthesizedoptionsmaycontain
aftertheoriginalfileheadercommentatthestartofeach
moresecurecode.
sourcecode. 2https://github.com/OpenVPN/openvpn

<!-- Page 5 -->

EnhancingSecurityofAI-BasedCodeSynthesiswithGitHubCopilotviaCheapandEfficientPrompt-Engineering
totheassessmentofcodesecurity,bothintheformofautomatic
// Be careful about buffer overflow/underflow
andmanualevaluation:
// Be careful about properly terminating string
// Be careful about NULL dereference • Staticanalysis:analysisofthesourcecode.Thisprocess
doesnotrequireprogramexecution.Therearemanyautomatictoolsforstaticanalysistools[16].
// Be careful about proper handling of file descr. • Dynamicanalysis:analysisoftheexecutedprogramtraces.
// Be careful about NULL dereference

### Themosteffectivetechniqueinanalyzingsecurityisfuzz

testing[15].Thisapproachistypicallyusedincaseswhere
oneneedstofindweaknessesoriginatingfromcomplex
// Be careful about buffer overflow/underflow
programlogic.
// Be careful about NULL dereference
Inourresearch,wechosenottouseauxiliarystaticanalysistool
duetoahighrateoffalsenegatives.Instead,weoptedformanual
// Be careful about integer overflow/underflow codeinspection,giventherelativelysmallsizeofthesampleset.
// Be careful about buffer overflow/underflow Forthesakeofreproducibility,weclassifythegeneratedsnippets
// Be careful about NULL dereference
ofcodeintooneofthefollowingclassesaccordingtotherespective
codeproperties:
// Be careful about proper index validation • Secure:Thegeneratedsampleisconsideredsecureifall
// Be careful about proper memory clearing crucialparameter-checkingconditionsarepresentinany
form,andadditionally,atask-specificsetoffunctionalrequirementsaremet,suchas:
Fig.8:Scenario-basedpromptsrelatedtoselectedfunctions.
(1) thepropernullbyteplacementinedgecases(i.e.,the
off-by-oneerror);
(2) thecorrectverificationofoperationsonthefilede-
(2) buffer_write_file()–possiblyvulnerabletoincorrect
scriptors(e.g.,theinspectionofreturncodesoffilefilehandlemanagementandunknowncustomdatastrucoperatingfunctions);
tureissues.(/src/openvpn/buffer.c)
(3) thecorrectsizeofmemorytransfer(e.g.,memcpy,membool buffer_write_file
move,bcopyfunctions);
(const char *filename, const struct buffer *buf){}
(4) thecorrectadditiontooffsetwithrespecttothetotal
(3) buf_catrunc()–possiblyvulnerabletoout-of-memory
lengthofthebufferandthecorrectcopyofthewhole
write,unknowncustomdatastructureissues,andNULL
stringintothebuffer(includingthenullbyte);
dereference.(/src/openvpn/buffer.c)
(5) propermemorybufferclearanceandcounterresetting
void buf_catrunc topreventout-of-boundsreadvulnerabilities.
(struct buffer *buf, const char *str) {} • Partiallysecure:Thegeneratedsampleisconsideredpar-
(4) buf_prepend()–possiblyvulnerabletobufferoverflow/un- tiallysecureifanyofthecrucialparameter-checkingconderflowandintegeroverflow/underflow.(/src/openvpn/ ditionsarepresentedinanyform.
buffer.h) • Insecure: The generated sample is considered insecure
static inline uint8_t * buf_prepend ifnoneofthecrucialparameter-checkingconditionsare
(struct buffer *buf, int size) {} presentedinanyform.
(5) argv_reset() – possibly vulnerable to improper index
WepresenttheresultsofourexperimentsinTab.1,whichshows
validationandmemoryclearing.(/src/openvpn/argv.c)
thetotalnumberofsynthesizedsamplesinthefirstcolumnand
static void argv_reset thepercentageinthesecond,withaparticularsecuritylevelfor
(struct argv *a) {} eachoftheproposedmethodsvs.thebaseline(i.e.thetaskswithout
Inaccordancewiththeexpectedimplementationissues,thefol- anyadditionsintheformofcodecommentarytotheprompt).The
lowingscenariomethodpromptswereprepared–theyareenumer- resultsindicatethatthebaseline(generatedwithoutanyadditional
atedinFig.8inthesameorderasthefunctionsabove. promptalteration)containsfewersecurity-checkingconditions,
andthusislesssecureinsecurity-sensitivecases.
4.3 AssessmentofCodeSecurity On the other hand, the tasks generated using the additional
code commentary for the prompt alteration contained at least
Assessingthesecurityofcodesamplespresentsmanychallenges.
some security-checking conditions, and thus were more secure
Unlikeaspectslikefunctionalityorcorrectness,whichcanbemeainsecurity-sensitivecases.Accordingtotheresults,theiterative
sured through compilation/interpretation or metrics like Codemethodisthebest-performingonetoincreasethenumberofsecure
BLEU3[20],securityevaluationrequiresadifferentapproach.
solutionssynthesizedandreducethenumberofinsecuresynthe-

### However,nosuchpracticehasbeenestablishedforanalyzing

sizedsamples–thenumberofsecuresampleswasincreasedby8%
thegeneratedcodesecurity.Ingeneral,therearetwoapproaches
incontrasttothebaselinewhilethenumberofinsecuresamples
3Thismetriccombinesn-gramcomparison,syntaxtreeanalysis,andsemanticchecks. wasreducedby12%.Nevertheless,thebestmethodforreducing

<!-- Page 6 -->

JakubRes,etal.
Method Theresultsindicatethatmeaningfulfunctionnamesandtheirde-
Securitylevel Baseline Scenario Iterative Clause scriptionsusingdocstring(i.e.betterpromptformulation)leadto
Secure 10 40%| 10 40%| 12 48%| 11 44% betterresultsthantheothertwoalternatives.

### Partiallysecure 8 32%| 12 48%| 9 36%| 9 36%

AntonioMastropaolo,etal.[13]statethatcodequalityisnotonly

### Insecure 7 28%| 3 12%| 4 16%| 5 20%

affectedbysemanticsbutalsobythesyntaxoftheinputprompt.
Tab.1:Resultsaggregatedoverallofthetasks.
Theirstudyshowedthattheresultsofthequalityanalysisdifferfor
thesetofpromptsbeforeandafterparaphrasinginabout70%ofthe
cases.ImprovingthecapabilitiesofAIbyimplementingmultiple
communicative agents has recently shown promising direction.
thenumberofinsecuresolutionswasthescenario-specificmethod, Usingmultipleagentswithspecificroleswithinaproblem-solving
decreasingthenumberofinsecuresamplesby16%. processcanproducesignificantlybetterresults[8].

## 5 Relatedwork


## 6 Discussion


### Currently,theresearchcommunityonlargelanguagemodelsis

primarilyfocusedonpushingtheboundariesofAIcapabilitiesby Althoughtheachievedresultsdemonstratetheimprovementin
achievingbetterperformanceonvarioustaskswithlargerandmore securityoftheAI-synthesizedcode,thereareseverallimitations
powerfulmodelsorbyachievingsimilarresultstotheircompetitors toourapproach.Weconsidertheselimitationsasareasoffuture
witheversmallermodels.However,themostrecognizedbenchmark researchratherthanthreatstovalidity.
tasksarenotevenmarginallyfocusedonobservingcodesecurity.
Somestudiestrytoaddressthisbycreatingtheirownsecurity-
6.1 Limitations
focusedscenariosandevaluatingsynthesizedcodesecurityusing
them,whichwefurtherreviewinSec.5.1. Thelimitationsofourresearchareasfollows.

### Prompts.Thepromptadditions(inourcase)arealwaysatrade-

5.1 Security off between over-specification and over-generalization. We are
aware of the fact that our prompt enhancements could still be

### Accordingtothemostrecentstudyontheempiricalevaluationof

improved.However,thecurrentstateissufficientfortheproof-oftheaveragesecurityofsynthesizedcode,AIgeneratespotentially
conceptofourmethods.
insecurecodeinapproximately40%ofcases[17].Besidestestingthe
Dataset. In this paper, we choose five cases from one opensecurity,theauthorsalsostudiedtheinfluenceofpromptmisspells.
sourceprojectwritteninC,whichwerecognizeashighlyimpactful

### Theinterestingfindingis,thatalteringthepromptinaspecificway

intermsofsecurity.Thislimitstheresearchtoasinglepoint-ofmaypositivelyinfluencethegeneratedoutput[17].
view,potentiallymissingimportantdetails,eitherresultingfroma

### Sandoval et at. [21] approached the problem from the user’s

limitedintra-classvariability(i.e.inappropriateselectionofcases),
perspectiveandobservedtheimpactofusingAIcodingassistant
orinter-classvariability(singlecode-base,orprogramminglanonthesecurityofClanguagecode.Inascenario,wheredevelopers
guage).Infuturework,weplantoexperimentwithmoreopenweredividedintotwogroups–withandwithoutanAIassistant–
sourceprojectsanddifferentprogramminglanguages.
thedeveloperscodedvariousfunctionstooperateastructureinC

### EnvironmentisprimarilymeantastheclientfortheAIcode

language.Theresultssuggest,thatwhileusingAIassistant,users
generatorandtheAIgeneratoritself.Inourcase,thelimitation
produceonlyupto10%moresecurityissues.
isregardingthecontext,whichissentbythelocalclientandthe

### Siddiq,etal.[22]havefocusedonexaminingthesourceofcode


### GitHubCopilotcachingsystem,creatingdependenciesbetween

issues.Theirworkexploredthepropagationofcodesmellsfromthe
testruns(i.e.,thelocalvs.remotecachingofsynthesizedoptions)–
learningdatasettothemodelandsubsequentlytheoutputs.The
indetail,wecouldcontrolonlythelocalcachingsystem.
resultsshownotonlythatcodeissues,includingthesecuritycode
CodeSynthesizers.Inthiswork,weutilizedonlyGitHubCopismells,doindeedpropagatefromthetrainingdatatotheoutput,
lotasaproof-of-concept.However,wearguethatsinceourapbutthatthisalsohappensforthemostcommerciallyusedservice,
proachisgeneral,itcanbeutilizedonanyothercodesynthesizer
GitHubCopilot.
(i.e.,opensourceorproprietary),whichwillbethesubjectofour
DespitepointingoutthesecurityproblemofAI-generatedcode,
futureresearch.
noneoftheresearchworkssystematicallyfocusedonanymeans
AutomatedInspectionofSecureCodeisaproblemingeneral.
ofimprovement.However,manypapershavealreadymadesig-
Eventhoughtherearenumeroustoolsforstaticanddynamicautonificantimprovementstootheraspectsofsynthesizedcode(be
maticcodeinspection,mostofthemexhibitanexcessivenumberof
itnewmodels,orpapersandguidesfocusingonbetterprompt
falsenegativesand/orfalsepositives.Therefore,weutilizedmanual
formulation[14]orAIcooperation[8]).
inspectioninourwork,whichwasmoreaccuratebutmightbe
expensiveforlargerexperiments.Thismightposeathreattothe
5.2 CodeQuality
reproducibilityoftheresultswithlargerdatasetsinthefuture.
BurakYetistiren,etal.[32]evaluatetheabilityofGithubCopilot PotentialImprovementsofAI-BasedCodeSynthesis.In
togeneratecorrect,valid,andefficientcodeinthreescenariosac- thiswork,wefocusedonlyonpromptalterationmethodssincethey
cordingtotheinputprompt:functionnameanddocstring,function canbeusedevenonproprietarymodels.However,theinteresting
nameonly,anddummyfunctionnamewithdocstringdescription. potentialalsoliesinthemodelfine-tuning[12]methodsandtheir

<!-- Page 7 -->

EnhancingSecurityofAI-BasedCodeSynthesiswithGitHubCopilotviaCheapandEfficientPrompt-Engineering
combinations.However,itcanbeappliedtowhiteboxmodelsonly. ChengqingZong,FeiXia,WenjieLi,andRobertoNavigli(Eds.).Associationfor
Weplantoinvestigatethisareainourfuturework. ComputationalLinguistics,Online,4582–4597. https://doi.org/10.18653/v1/2021.
acl-long.353
[11] JennyT.Liang,ChenyangYang,andBradA.Myers.2023.ALarge-ScaleSur-
7 CONCLUSION veyontheUsabilityofAIProgrammingAssistants:SuccessesandChallenges.
arXiv:2303.17125[cs.SE]

### AIcodegeneratorshaveproventobeapowerfultoolbuttheymust

[12] XinyuLin,WenjieWang,YongqiLi,ShuoYang,FuliFeng,YinweiWei,andTatbeusedcorrectlytofullyutilizetheirpotential.Ourresearchhas SengChua.2024.Data-efficientFine-tuningforLLM-basedRecommendation.
shownhowtosystematicallytackletheproblemofcodesecurity arXivpreprintarXiv:2401.17197(2024).
[13] AntonioMastropaolo,LucaPascarella,EmanuelaGuglielmi,MatteoCiniselli,
whilecommunicatingwithsuchAIservices.Ourresultsindicate SimoneScalabrino,RoccoOliveto,andGabrieleBavota.2023.OntheRobustthatthemethodsproposedinthispapercanenhancethesecurity nessofCodeGenerationTechniques:AnEmpiricalStudyonGitHubCopilot.
arXiv:2302.00438[cs.SE]
ofgeneratedcode.
[14] OpenAI.2023.PromptEngineering.https://platform.openai.com/docs/guides/
Theresultsalsoindicatethattheperformanceintermsofcode prompt-engineering.
securitycanbeenhancedevenforproprietarymodels,whereend [15] OWASP.2024.Fuzzing. https://owasp.org/www-community/Fuzzing
[16] OWASP. 2024. Source Code Analysis Tools. https://owasp.org/wwwuserscannotaccess/modifytheunderlyingarchitectureormodel
community/Source_Code_Analysis_Tools
itself.Thispaperlaysafoundationforourfuturein-depthresearch [17] HammondPearce,BaleeghAhmad,BenjaminTan,BrendanDolan-Gavitt,and
ofintelligentprompt-enhancingsystemsthatweintendtoevaluate RameshKarri.2021.AsleepattheKeyboard?AssessingtheSecurityofGitHub

### Copilot’sCodeContributions. arXiv:2108.09293[cs.CR]

onmultipleAI-basedcodesynthesizersandvariousopen-source [18] Neil Perry, Megha Srivastava, DeepakKumar,and Dan Boneh. 2023. Do
projects. UsersWriteMoreInsecureCodewithAIAssistants?.InProceedingsofthe
2023ACMSIGSACConferenceonComputerandCommunicationsSecurity
(CCS’23).ACM. https://doi.org/10.1145/3576915.3623157

## Acknowledgments

[19] ChenQian,XinCong,WeiLiu,ChengYang,WeizeChen,YushengSu,Yufan
Dang,JiahaoLi,JuyuanXu,DahaiLi,ZhiyuanLiu,andMaosongSun.2023.

### ThisworkwassupportedbytheBrnoUniversityofTechnology

CommunicativeAgentsforSoftwareDevelopment. arXiv:2307.07924[cs.SE]
internalprojectFIT-S-23-8151. [20] ShuoRen,DayaGuo,ShuaiLu,LongZhou,ShujieLiu,DuyuTang,NeelSundaresan,MingZhou,AmbrosioBlanco,andShuaiMa.2020.CodeBLEU:aMethod
REFERENCES forAutomaticEvaluationofCodeSynthesis.arXive-prints(2020),arXiv–2009.
[21] GustavoSandoval,HammondPearce,TeoNys,RameshKarri,SiddharthGarg,
[1] OpenAI.2022.IntroducingChatGPT.OpenAI.https://openai.com/blog/chatgpt andBrendanDolan-Gavitt.2023.LostatC:AUserStudyontheSecurityImpli-
[2] BenAthiwaratkun,SanjayKrishnaGouda,ZijianWang,XiaopengLi,Yuchen cationsofLargeLanguageModelCodeAssistants. arXiv:2208.09727[cs.CR]
Tian,MingTan,WasiUddinAhmad,ShiqiWang,QingSun,MingyueShang, [22] MohammedLatifSiddiq,ShafayatMajumder,MaishaMim,SourovJajodia,and
SujanKumarGonugondla,HantianDing,VarunKumar,NathanFulton,Arash JoannaCeciliadaSilvaSantos.2022. AnEmpiricalStudyofCodeSmellsin
Farahani,SiddharthaJain,RobertGiaquinto,HaifengQian,MuraliKrishnaRa- Transformer-basedCodeGenerationTechniques.71–82. https://doi.org/10.1109/
manathan,RameshNallapati,BaishakhiRay,ParminderBhatia,SudiptaSengupta, SCAM55253.2022.00014
DanRoth,andBingXiang.2023.Multi-lingualEvaluationofCodeGeneration [23] MohammedLatifSiddiqandJoannaC.S.Santos.2022. SecurityEvaldataset:
Models. arXiv:2210.14868[cs.LG] miningvulnerabilityexamplestoevaluatemachinelearning-basedcodegener-
[3] MarkChen,JerryTworek,HeewooJun,QimingYuan,HenriquePondede ationtechniques.InProceedingsofthe1stInternationalWorkshoponMining
OliveiraPinto,JaredKaplan,HarriEdwards,YuriBurda,NicholasJoseph,Greg SoftwareRepositoriesApplicationsforPrivacyandSecurity(Singapore,Singa-
Brockman,AlexRay,RaulPuri,GretchenKrueger,MichaelPetrov,HeidyKhlaaf, pore)(MSR4P&S2022).AssociationforComputingMachinery,NewYork,NY,
GirishSastry,PamelaMishkin,BrookeChan,ScottGray,NickRyder,Mikhail USA,29–33. https://doi.org/10.1145/3549035.3561184
Pavlov,AletheaPower,LukaszKaiser,MohammadBavarian,ClemensWinter, [24] Snyk.2024.SnyksecuresAI-generatedcode.Snyk. https://snyk.io/solutions/
PhilippeTillet,FelipePetroskiSuch,DaveCummings,MatthiasPlappert,Fo- secure-ai-generated-code/
tiosChantzis,ElizabethBarnes,ArielHerbert-Voss,WilliamHebgenGuss,Alex [25] CWEContentTeam.2023.CWE-476:NULLPointerDereference.https://cwe.
Nichol,AlexPaino,NikolasTezak,JieTang,IgorBabuschkin,SuchirBalaji,Shan- mitre.org/data/definitions/476.html.
tanuJain,WilliamSaunders,ChristopherHesse,AndrewN.Carr,JanLeike,Josh [26] CWEContentTeam.2023.CWEVIEW:ResearchConcepts. https://cwe.mitre.
Achiam,VedantMisra,EvanMorikawa,AlecRadford,MatthewKnight,Miles org/data/definitions/1000.html
Brundage,MiraMurati,KatieMayer,PeterWelinder,BobMcGrew,DarioAmodei, [27] CatherineTony,MarkusMutas,NicolásE.DíazFerreyra,andRiccardoScandari-
SamMcCandlish,IlyaSutskever,andWojciechZaremba.2021.EvaluatingLarge ato.2023.LLMSecEval:ADatasetofNaturalLanguagePromptsforSecurityEval-
LanguageModelsTrainedonCode. arXiv:2107.03374[cs.LG] uations.In2023IEEE/ACM20thInternationalConferenceonMiningSoftware
[4] Paul Denny, Viraj Kumar, and Nasser Giacaman. 2023. Conversing with Repositories(MSR).588–592. https://doi.org/10.1109/MSR59073.2023.00084
Copilot:ExploringPromptEngineeringforSolvingCS1ProblemsUsingNat- [28] ShubhamUgare,TarunSuresh,HangooKang,SasaMisailovic,andGagandeep
ural Language. In Proceedings of the 54th ACM Technical Symposium on Singh.2024.ImprovingLLMCodeGenerationwithGrammarAugmentation.
ComputerScienceEducationV.1(<conf-loc>,<city>TorontoON</city>,<coun- arXiv:2403.01632[cs.LG]
try>Canada</country>,</conf-loc>)(SIGCSE2023).AssociationforComputing [29] GiorgosVernikos,ArthurBražinskas,JakubAdamek,JonathanMallinson,Aliak-
Machinery,NewYork,NY,USA,1136–1142. https://doi.org/10.1145/3545945. seiSeveryn,andEricMalmi.2023. Smalllanguagemodelsimprovegiantsby
3569823 rewritingtheiroutputs.arXivpreprintarXiv:2305.13514(2023).
[5] L.Giray.2023.PromptEngineeringwithChatGPT:AGuideforAcademicWriters. [30] YuxiaWang,RevanthGangiReddy,ZainMuhammadMujahid,ArnavArora,
AnnalsofBiomedicalEngineering51(2023).https://doi.org/10.1007/s10439-023- AleksandrRubashevskii,JiahuiGeng,OsamaMohammedAfzal,Liangming
03272-4 Pan,NadavBorenstein,AdityaPillai,IsabelleAugenstein,IrynaGurevych,and
[6] GitHub.2024.GitHubCopilot.https://github.com/features/copilot. PreslavNakov.2023.Factcheck-GPT:End-to-EndFine-GrainedDocument-Level
[7] JingxuanHeandMartinVechev.2023.LargeLanguageModelsforCode:Security Fact-CheckingandCorrectionofLLMOutput. arXiv:2311.09000[cs.CL]
HardeningandAdversarialTesting.InProceedingsofthe2023ACMSIGSAC [31] JulesWhite,QuchenFu,SamHays,MichaelSandborn,CarlosOlea,Henry
ConferenceonComputerandCommunicationsSecurity(CCS’23).ACM. https: Gilbert,AshrafElnashar,JesseSpencer-Smith,andDouglasC.Schmidt.2023.
//doi.org/10.1145/3576915.3623175 APromptPatternCatalogtoEnhancePromptEngineeringwithChatGPT.
[8] GuohaoLi,HasanAbedAlKaderHammoud,HaniItani,DmitriiKhizbullin,and arXiv:2302.11382[cs.SE]
BernardGhanem.2023.CAMEL:CommunicativeAgentsfor"Mind"Exploration [32] BurakYetistiren,IsikOzsoy,andErayTuzun.2022. Assessingthequality
ofLargeLanguageModelSociety. arXiv:2303.17760[cs.AI] ofGitHubcopilot’scodegeneration.InProceedingsofthe18thInternational
[9] ShuangLi,YiXu,AnushaKrishna,TianyuChen,TaifuWu,PengCao,and... ConferenceonPredictiveModelsandDataAnalyticsinSoftwareEngineering

### AlphaCode2TechnicalReport. https://storage.googleapis.com/deepmind- (Singapore,Singapore)(PROMISE2022).AssociationforComputingMachinery,

media/AlphaCode2/AlphaCode2_Tech_Report.pdf NewYork,NY,USA,62–71. https://doi.org/10.1145/3558489.3559072
[10] Xiang Lisa Li and Percy Liang. 2021. Prefix-Tuning: Optimizing Contin- [33] ZhengZhang,ChenZheng,DaTang,KeSun,YukunMa,YingtongBu,Xun
uous Prompts for Generation. In Proceedings of the 59th Annual Meeting Zhou,andLiangZhao.2023. Balancingspecializedandgeneralskillsinllms:
oftheAssociationforComputationalLinguisticsandthe11thInternational Theimpactofmoderntuninganddatastrategy.arXivpreprintarXiv:2310.04945
JointConferenceonNaturalLanguageProcessing(Volume1:LongPapers), (2023).