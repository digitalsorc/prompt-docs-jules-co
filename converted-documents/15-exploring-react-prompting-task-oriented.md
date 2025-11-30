---
title: "Exploring ReAct Prompting Task Oriented"
original_file: "./15_Exploring_ReAct_Prompting_Task_Oriented.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "react", "agents"]
keywords: ["system", "user", "input", "domain", "thought", "gpt", "page", "action", "yes", "react"]
summary: "<!-- Page 1 -->

Exploring ReAct Prompting for Task-Oriented Dialogue: Insights and

### Shortcomings

MichelleElizabeth1,2,3,MorganVeyret3,MiguelCouceiro1,

### OndrˇejDušek2,LinaM.Rojas-Barahona3,

1UniversityofLorraine/LORIA,France,2CharlesUniversity,Czechia,
3OrangeInnovation,France
michelle.elizabeth@orange.com,morgan.veyret@orange.com,miguel.couceiro@loria.fr,
odusek@ufal.mff.cuni.cz,lina.rojas@orange.com,
Abstract arigidstructureandrequireaccesstoanexternal
databasetoretrievenecessaryinfo"
related_documents: []
---

# Exploring ReAct Prompting Task Oriented

<!-- Page 1 -->

Exploring ReAct Prompting for Task-Oriented Dialogue: Insights and

### Shortcomings

MichelleElizabeth1,2,3,MorganVeyret3,MiguelCouceiro1,

### OndrˇejDušek2,LinaM.Rojas-Barahona3,

1UniversityofLorraine/LORIA,France,2CharlesUniversity,Czechia,
3OrangeInnovation,France
michelle.elizabeth@orange.com,morgan.veyret@orange.com,miguel.couceiro@loria.fr,
odusek@ufal.mff.cuni.cz,lina.rojas@orange.com,
Abstract arigidstructureandrequireaccesstoanexternal
databasetoretrievenecessaryinformation,suchas
Large language models (LLMs) gained imvenuesorobjectstosearchforandtheirproperties.
mensepopularityduetotheirimpressivecapa-
Recently, synergizing reasoning and acting in
bilitiesinunstructuredconversations. Empow-
LLMs(ReAct)(Yaoetal.,2022)hasshownpromisering LLMs with advanced prompting strategiessuchasreasoningandacting(ReAct)(Yao ing results in controlled tasks that need external
etal.,2022)hasshownpromiseinsolvingcom- informationaccess. ReActemploysfew-shotLLM
plextaskstraditionallyrequiringreinforcement prompting with a sequence of thoughts, actions,
learning.Inthiswork,weapplytheReActstrat- andobservations. ThoughtsrefertointernalreasonegytoguideLLMsperformingtask-orienteddi- ingthatdecomposesaproblemintosub-problems.
alogue(TOD).WeevaluateReAct-basedLLMs
Actions execute external API calls or programs,
(ReAct-LLMs)bothinsimulationandwithreal
and observations analyze the results of actions.
users. WhileReAct-LLMsseverelyunderper-
In this work, we investigate the ability of LLMs
formstate-of-the-artapproachesonsuccessrate
insimulation,thisdifferencebecomeslesspro- guidedbyReActtosolvetask-orienteddialogue.
nouncedinhumanevaluation. Moreover,com- Our contributions are as follows: (i) We imparedtothebaseline,humansreporthighersub- plement a ReAct-based system for TOD, using
jectivesatisfactionwithReAct-LLMdespiteits

### GPT-3.5andGPT-4LLMsrespectively(OpenAI,

lower success rate, most likely thanks to its
2023), for the MultiWOZ tourist information donaturalandconfidentlyphrasedresponses.
mains(Budzianowskietal.,2018). (ii)Weevaluate
1 Introduction ourReAct-LLMsystembothwithasimulateduser
andwithhumans,andweincludeamanualquali-
Task-orientedDialogue(TOD)systemssolvetasks, tativeanalysisofhumandialoguesandaAPIcost
such as accessing information or booking places versusperformancetrade-offassessment. (iii)Our
and tickets, by interacting with humans in natu- results show that ReAct-LLMs clearly underperral language (Budzianowski et al., 2018; Rastogi formstate-of-the-artbaselinesintermsofsuccess
etal.,2020). TraditionalTODpipelinesintegrate rateinsimulation. However,thisdifferenceisless
specialized components for natural language un- pronouncedinhumanevaluation,andhumanseven
derstanding(NLU),dialoguestatetracking(DST), ratetheirsatisfactionwiththeReAct-LLMsystem
dialoguemanagementandnaturallanguagegenera- higherthanthebaseline.
tion(NLG),andoptionallyspeechrecognitionand
synthesis (Ultes et al., 2017). On the other hand, 2 RelatedWork
end-to-endarchitecturesmodelallcomponentsin
a single neural networks (Wen et al., 2017; Zhu Classical approaches for dialogue management
et al., 2020, 2022). Both approaches are costly (Casanuevaetal.,2018;Weiszetal.,2018a),varied
to develop, requiring manual engineering and/or fromhandcrafted(HDC)toreinforcementlearning
collectinglargedialoguecorpora. Largelanguage (RL).ThecombinationofdeepRLwithimitation
models(LLMs)(Ouyangetal.,2022)offeranalter- learning(Cordieretal.,2020)aswellasstructural
nativetothisbygeneralizingfrominstructionsora RLhavealsobeenappliedtomulti-domain,multismallnumberofexamplesandpromisefluentand task dialogue (Chen et al., 2018; Cordier et al.,
naturalreplies. However,unlikestandardLLMuse 2022). However,theseapproachesrequireseparate
scenarios, task-oriented dialogues typically have specializedcomponents,involvingextensiveengi-
1
5202
raM
71
]LC.sc[
2v26210.2142:viXra

<!-- Page 2 -->

neering,theneedforsemanticallyannotateddata cess to external tools to guide it through the
aswellasusersimulatorsoperatingatthesemantic TOD pipeline. We provide few-shot examlevel. ples in the prompt following ReAct (Yao et al.,
Latestend-to-endneuralarchitecturesarebuilt 2022). We give the ReAct-LLM agent a list
ontopofpretrainedlanguagemodels(Pengetal., of tools: list_domains, list_slots, db_query
2021;Linetal.,2020)andinvolvetwo-stepgener- and generate_booking_reference (details in
ation: themodelfirstgeneratesthedialoguestate Appendix A.1), which it can use as actions. The
ordatabasequerybasedonuserinput;then,itgen- exampleprovidedinthepromptshowshowandin
eratesthereplybasedonexternaldatabasesearch. whatorderthetoolsshouldbeused. Thereasoning
Theseapproachesprovidemoreflexibilityandpo- processtobefollowedbytheSAisoutlinedbelow:
tentiallybetterfluency,butrequireevenlargertrain-
Step1: TheSAshouldtrytounderstandtheuser
ingcorpora.
input. Itsfirstthoughtshouldbeexplicitlyplanning

### Recentapproachesexploresimplezero-shotor

out the next course of action, to be executed in
few-shotLLMpromptingforTOD,usingexamples

### Steps 2-5. The SA should plan for identifying

of relevant dialogue turns (Hudecˇek and Dusek,
thedomainandthecorrespondingslotsandvalues
2023), database or API definitions (Stricker and
from the user input, forming the belief state and

### Paroubek,2024),templatedconversationsnippets

usingittoquerythedatabase,retrievingtheresults
(Zhangetal.,2023),ordetailedbehaviorandAPI
andformingthefinalanswerbasedontheresults.
calling instructions (Xu et al., 2024). In contrast,
Step 2: The SA should call list_domains, obin this work we propose to use the ReAct stratserveitsoutputanddecidewhichdomaintheuser
egy(Yaoetal.,2022)toguideLLMstowardstask
requestbelongsto.
oriented dialogue through domain selection, slot
Step 3: Now it needs the list of slots available
detectionandbeliefstatetracking.
in the selected domain to identify the slot values
Since dialogue is dynamic and evaluation on fromtheuserrequest. Thesystemshouldusethe
static data in single-turn replies may not be con- list_slots tool with the domain as input, obsistentwithfulldialogueperformance(Takanobu serve the list of slots available and decide which
et al., 2020), we evaluate the system on full dia- slots have been mentioned in the user input and
logues. First,weevaluateperformanceinasimu- form/updatethebeliefstate.
latedenvironment,which,unlikeXuetal.(2024), Step 4: It should call db_query using the state
utilizes the well established CONVLAB3 bench- asinputtoretrieverecordsfromthedatabasethat
mark(Zhuetal.,2022)toguaranteereproducibility matchtheuserrequest.
andfaircomparisonwithpreviousapproaches. We Step5: Asthefinalstep,itobservestheretrieved
alsoassesstheconversationswithhumans. Unlike
entitiesandgeneratesanappropriateresponse.
previous works on dialogue management (Weisz
We also provide a tool for generating booking
etal.,2018b;Zhuetal.,2020;Cordieretal.,2022),
referencenumberswhentheuserrequestsabookthe simulator and our system do not interact at ing (generate_booking_reference). The agent
the semantic level, instead they interact in natisgivenadetailedexampleinthepromptshowing
ural language. Unlike previous end-to-end and
thesequenceofthoughts,actionsandobservations
LLM-based approaches, which generated delexifortwoconsecutiveuserturns(seeAppendixA).It
calizedresponseswithplaceholdersandreplaced
alsohasaccesstopreviousconversationhistoryas
thesewithvalidentitynamesfromthedatabasein
wellasadescriptionofeachtoolprovided.
arule-basedfashion,wegeneratefullresponsesincludingentitynames. Thisavoidsconstrainingthe 4 ExperimentalSetup
inherentcapabilitiesofLLMsingeneratingnatural
WeusetheLangChain1 libraryforimplementing
language. Instead,weguidetheLLMtowardsthe
ReAct-LLM.ThepromptdetailsaregiveninApdatabaseconstraintsthroughReActprompting.
pendixA,Figure2. WeuseLangfuse2 fordebuggingthereasoningtracesandtokeeptrackofthe
3 ReActforTask-OrientedDialogue
computationalcostsofourexperiments. WeexperimentwithOpenAIGPT-3.5(gpt-3.5-turbo-0301)

### Figure 1 shows the proposed architecture: the

ReAct-LLM system agent (SA) interacts with 1https://www.langchain.com/
a user in natural language. The SA has ac- 2https://langfuse.com/
2

<!-- Page 3 -->

Figure1: TheproposedReAct-LLMsystemagentusesfew-shotexamplesintheprompttoguidetheLLMin
decomposingreasoningintoasequenceofthoughts,actions,andobservations.
andGPT-4(gpt-4-32k)models. Wefirstcoupleour aloguemanagementbaselines: HDCandRL-based,
SAwithasimulateduser,thenproceedtoevaluate suchasproximalpolicyoptimization(PPO)(Schulitwithhumans. manetal.,2017)andstructuredRLwithimitation
learning (ACGOS) (Cordier et al., 2022). These
4.1 SimulatedUser
baselines use CONVLAB’s pipelines with BERT
WeimplementedanLLM-baseduseragent,butit NLUandtemplate-basedNLG.Wesimulated1000
wasnotabletoendtheconversationcorrectlyand dialogues, using a fixed random seed in the goal
occasionally switched its role to play the system, generatorforreproducibility.
whichresultedininappropriateconversations(see Foramorerealisticassessment,wedecidedto
AppendixC).Therefore,weusetheagenda-based invitehumanstoevaluatethesystemforafairasusersimulator(Schatzmannetal.,2007)implemen- sessment. We opt for an in-house evaluation to
tation in CONVLAB 3 (Zhu et al., 2022). A goal ensurehighquality. Finally,wedoadetailedqualgeneratorinagreementwiththeMultiWOZdataset itativeanalysis of asmall sampleof the dialogue
isusedtoinitializetheagenda. Thesimulatorthen logstoidentifythemostfrequenterrorsources.
generatesthesemanticrepresentationandconverts
5 Results
itintonaturallanguage. Thisisfedtothesystem
agentandtheresponsefromthesystemissentto
Wenowassessbothsimulatedandrealusers.
theBERT-basedNLUofthesimulatorthatreturns
its semantic representation. This semantic repre- 5.1 SimulatedEvaluation
sentationisinturnusedtoupdatetheagenda. The
Table 1 compares ReAct-LLM systems with presimulatorthengeneratesthenextutterancebased
vious works in CONVLAB. Note that systems in
onthesystemresponseandtheupdatedagenda.
thefirstsectionofthetableinteractatthesemantic level and hence, the metrics show the upper
4.2 EvaluationSetup
boundoftheperformancethatcanbeachievedby
To measure how well the user goals were satis- afullTODsystem. WeobservethatACGOSperfiedbythesystem,wecomputethestandardmet- formsbestintermsofinformrate. TheHDCpolicy
rics: success, book, inform and complete rates as provestobesuperiortoothermethodswithhigher
wellastheaveragenumberofturns,3 using CON- book,successandcompleteratesandfewerturns.
VLAB 3 (Zhu et al., 2022). A dialogue is suc- Both React-LLMs clearly underperform all basecessful if the system provided the right informa- lines, with the GPT-4 version distinctly ahead of
tion and was able to book the requested entities theGPT-3.5one.
in agreement with the user goal. In addition, we ReAct-LLMsarecostly. Table2showstheperalso measure the cost incurred by using OpenAI tokencostforthetwoGPTmodels,aswellasthe
APIs. WecompareourReAct-LLMstomultipledi- totalnumberoftokensusedandtheapproximate
total experiment cost. The success rate improve-
3Notethatthelowertheaveragenumberofturnsthebetter
sincethismeansthatthesystemachievesthegoalfaster. mentforGPT-4doesnotappeartojustifythecost
3

<!-- Page 4 -->


### InformRate↑

Configuration AvgTurns↓ BookRate↑ SuccessRate↑ CompleteRate↑

## (P/R/F1)


### HDC(semanticlevel) 10.6 87.2/98.6/90.9 98.6 97.3 97.9

ACGOS(semanticlevel) 13.2 94.8/99.0/96.1 98.7 97.0 98.2

### BERTNLU+HDC+Tpl. 12 82.8/94.1/86.2 91.5 83.8 92.7


### BERTNLU+PPO+Tpl. 17.8 69.4/85.8/74.1 86.6 71.7 75.5

BERTNLU+ACGOS+Tpl. 14.8 88.8/92.6/89.5 86.6 81.7 89.1
ReAct-LLM(GPT-3.5) 15.3 59.0/64.9/58.3 40.5 28.2 45.9

### ReAct-LLM(GPT-4) 15.5 62.7/81.3/66.8 58.2 43.6 63.8

Table1: Simulatedevaluationon1000dialogues(Section4.2). Tpl. standsfortemplated-basedNLG.
Cost/1Mtokens 1000sim.dialogues DialogueSystem Avg Satisfaction Success

### Model Input Output #Tokens Totalcost Turn Rate(%) Rate(%)

gpt-3.5-turbo-0301 $1.50 $2.00 40.6M $61.71 BERTNLU+HDC+Tpl. 15.91 54.10 60.00
gpt-4-32k $60.00 $120.00 35.8M $2,258.81 ReAct-LLM(GPT-3.5) 14.42 65.47 50.52
Table2: ExperimentcostforGPT-3.5vs.GPT-4. Table3: Humanevaluationresults,with95dialogues
foreachsystem.
difference.
reasoningtracesmayjustbeimitatingtheexamples
5.2 HumanEvaluation
given in the prompt. This may work for simpler
Volunteers were asked to chat online with a sys- caseswithfewergoalstoachieve. However,when
tem,inordertoachieveadialoguegoalrandomly thegoalsgetlargerwithmultipledomainsandthe
generatedbyConvLab. Theycouldstartaconver- user requests become more complicated, ReActsationasmanytimesastheywishandwerepaired LLM struggles to understand the user and to perwith a randomly chosen system each time, either formtasksaccordingly. Beyondthat,thereasoning
the HDC baseline or our ReAct-LLM (GPT-3.5). isinconsistentandstraysfrominstructionsattimes.
Theywereaskedtogiveascoreforsuccess(ifall Furthermore,theLLMcancomeupwithcreative
thedialoguegoalswereachieved)aswellasasub- responses,butstrugglestostaywithinthebounds
jectivescorefortheiroverallsatisfactionwiththe setbytheinstructions,oftenproducinginvaliddiconversationonascaleof1-5. Wethenconverted aloguestatesornotstickingtothesetofexternal
theratingstopercentagesandreportedtheaverage tools given. Compared to the GPT-3.5 agent, the
ratingprovidedforeachsystem.Wecollected95di- GPT-4agentismoreconsistentwithrespecttothe
aloguesforeachsystem,withthehelpof20users. desired reply format, is better at clarifying, and
Table3showsthatHDCperformsbetterinterms produces more verbose and polite replies. More
ofsuccessrate,butnotbythesamemarginithad detailsareshowninAppendixBandD.
in simulation. We see that the HDC system falls
shortinthehumanevaluationcomparedtotheuser 6 Conclusion
simulation. Contrarytothe simulatedevaluation,
ReAct-LLMperformsmuchbetterwithrealusers. TheperformanceofReAct-LLMfallsshortcom-
Overall,usersaremoresatisfiedwithReAct-LLM pared to HDC and RL baselines, which perform
thanwithHDC,despitethebettersuccessrateof better mainly due to their fine-grained control at
HDC, because ReAct-LLM is self-confident and eachstepinthepipeline. Byrelyingcompletelyon
generateswellstructured,polite,fluentandnatural thereasoningabilitiesofReAct-LLM,welosethe
sentences even though it was not always able to abilitytocontrolitsreasoningtracesandresponse
findwhattheuserwaslookingfor. Wealsoseethat generation. Additionally,difficultyinunderstandtheReact-LLMsystemhasaslightlyloweraverage ingthesystemrequestsbytheusersimulator,due
numberofturnswhencomparedwiththesimulated to BERT-NLU errors,leadstorepeatedutterances
evaluation,whiletheoppositeistrueforHDC. andthusahighernumberofturnsonaverage. The
human evaluation shows that ReAct-LLM is pre-
5.3 QualitativeAnalysis
ferredbyusersovertheHDCbaseline,despiteits
Byinspectingasampleofthegenerateddialogues, lowersuccessrate.
we identify several issues. First, we see that the
4

<!-- Page 5 -->

References Abhinav Rastogi, Xiaoxue Zang, Srinivas Sunkara,

### RaghavGupta,andPranavKhaitan.2020. Towards


### Paweł Budzianowski, Tsung-Hsien Wen, Bo-Hsiang

scalable multi-domain conversational agents: The
Tseng, Iñigo Casanueva, Stefan Ultes, Osman Raschema-guideddialoguedataset. InProceedingsof
madan,andMilicaGašic´.2018. MultiWOZ-alargethe AAAI conference on artificial intelligence, volscale multi-domain Wizard-of-Oz dataset for taskume34,pages8689–8696.
orienteddialoguemodelling. InProceedingsofthe
2018ConferenceonEmpiricalMethodsinNatural

### JostSchatzmann,BlaiseThomson,KarlWeilhammer,

Language Processing, pages 5016–5026, Brussels,

### HuiYe,andSteveYoung.2007. Agenda-baseduser

Belgium.AssociationforComputationalLinguistics.
simulationforbootstrappingaPOMDPdialoguesystem. InHumanLanguageTechnologies2007: The
Iñigo Casanueva, Paweł Budzianowski, Pei-Hao Su,
Conference of the North American Chapter of the

### NikolaMrkšic´,Tsung-HsienWen,StefanUltes,Lina


### AssociationforComputationalLinguistics;Compan-

Rojas-Barahona, Steve Young, and Milica Gašic´.
ionVolume,ShortPapers,pages149–152,Rochester,

## A benchmarking environment for reinforce-

NewYork.AssociationforComputationalLinguismentlearningbasedtaskorienteddialoguemanagement. Preprint,arXiv:1711.11023. tics.
LuChen,BowenTan,SishanLong,andKaiYu.2018. John Schulman, Filip Wolski, Prafulla Dhariwal,
Structured dialogue policy with graph neural net- Alec Radford, and Oleg Klimov. 2017. Proximal
works. InProceedingsofthe27thInternationalCon- Policy Optimization Algorithms. arXiv preprint
ferenceonComputationalLinguistics,pages1257– arXiv:1707.06347.
1268.

### ArmandStrickerandPatrickParoubek.2024. AFew-

ThibaultCordier,TanguyUrvoy,FabriceLefèvre,and
shotApproachtoTask-orientedDialogueEnhanced
Lina M. Rojas-Barahona. 2022. Graph neural net- with Chitchat. In Proceedings of the 25th Annual
workpoliciesandimitationlearningformulti-domain MeetingoftheSpecialInterestGrouponDiscourse
task-orienteddialogues. Preprint,arXiv:2210.05252. andDialogue,pages590–602,Kyoto,Japan.AssociationforComputationalLinguistics.
Thibault Cordier, Tanguy Urvoy, Lina M. Rojas-

### Barahona, and Fabrice Lefèvre. 2020. Diluted

Ryuichi Takanobu, Qi Zhu, Jinchao Li, Baolin Peng,
near-optimal expert demonstrations for guiding di-
JianfengGao,andMinlieHuang.2020. IsYourGoalalogue stochastic policy optimisation. Preprint,
OrientedDialogModelPerformingReallyWell?EmarXiv:2012.04687.
piricalAnalysisofSystem-wiseEvaluation. InSIG-
VojteˇchHudecˇekandOndrejDusek.2023. Arelarge dial,pages297–310,Online.
languagemodelsallyouneedfortask-orienteddialogue? InProceedingsofthe24thAnnualMeeting Stefan Ultes, Lina M Rojas Barahona, Pei-Hao Su,
oftheSpecialInterestGrouponDiscourseandDia- David Vandyke, Dongho Kim, Iñigo Casanueva,
logue,pages216–228,Prague,Czechia.Association PawełBudzianowski,NikolaMrkšic´,Tsung-Hsien
forComputationalLinguistics. Wen, and Milica Gasic. 2017. Pydial: A multidomain statistical dialogue system toolkit. In Pro-
ZhaojiangLin,AndreaMadotto,GentaIndraWinata, ceedingsofACL2017,SystemDemonstrations,pages
andPascaleFung.2020. MinTL:MinimalistTrans- 73–78.
ferLearningforTask-OrientedDialogueSystems. In
Proceedings of the 2020 Conference on Empirical GellértWeisz,PawełBudzianowski,Pei-HaoSu,and
MethodsinNaturalLanguageProcessing(EMNLP), MilicaGašic´.2018a. Sampleefficientdeepreinforcepages3391–3405,Online.AssociationforComputa- mentlearningfordialoguesystemswithlargeaction
tionalLinguistics. spaces. IEEE/ACMTransactionsonAudio,Speech,
andLanguageProcessing,26(11):2083–2097.
OpenAI. 2023. GPT-4 Technical Report. Technical
Report,OpenAI.

### GellertWeisz,PawelBudzianowski,Pei-HaoSu,and


### MilicaGasic.2018b. Sampleefficientdeepreinforce-

LongOuyang,JeffWu,XuJiang,DiogoAlmeida,Carmentlearningfordialoguesystemswithlargeaction
rollL.Wainwright,PamelaMishkin,ChongZhang,
spaces. IEEE/ACMTrans.Audio,SpeechandLang.
SandhiniAgarwal,KatarinaSlama,AlexRay,John
Proc.,26(11):2083–2097.
Schulman,JacobHilton,FraserKelton,LukeMiller,

### Maddie Simens, Amanda Askell, Peter Welinder,


### Tsung-HsienWen,DavidVandyke,NikolaMrkšic´,Mil-

Paul Christiano, Jan Leike, and Ryan Lowe. 2022.
icaGašic´,LinaM.Rojas-Barahona,Pei-HaoSu,Ste-

### Traininglanguagemodelstofollowinstructionswith

humanfeedback. Preprint,arXiv:2203.02155. fanUltes,andSteveYoung.2017. Anetwork-based
end-to-endtrainabletask-orienteddialoguesystem.
BaolinPeng,ChunyuanLi,JinchaoLi,ShahinShayan- InProceedingsofthe15thConferenceoftheEurodeh, Lars Liden, and Jianfeng Gao. 2021. Soloist: peanChapteroftheAssociationforComputational
BuildingTaskBotsatScalewithTransferLearning Linguistics: Volume1,LongPapers,pages438–449,
andMachineTeaching. TransactionsoftheAssocia- Valencia,Spain.AssociationforComputationalLintionforComputationalLinguistics,9:807–824. guistics.
5

<!-- Page 6 -->

Heng-DaXu,Xian-LingMao,PuhaiYang,FanshuSun, accordingtouser’sconstraintsprovidedintheinandHeyanHuang.2024. Rethinkingtask-oriented put. Basedonthelistofslots,theLLM‘reasons’
dialoguesystems: Fromcomplexmodularitytozeroanddecidesontheappropriateslots. Thetoolsand
shotautonomousagent. InProceedingsofthe62nd
descriptionsprovidedtotheLLMareasfollows:

### AnnualMeetingoftheAssociationforComputational

Linguistics (Volume 1: Long Papers), pages 2748–
• list_domains()-Thisfunctionliststhedo-
2763,Bangkok,Thailand.AssociationforComputationalLinguistics. mainsavailableinthedatabase. Usethistool
firsttofindtheavailabledomainsandidentify
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
thecorrectdomainfortheusers´ request.
Shafran,KarthikNarasimhan,andYuanCao.2022.
React: Synergizingreasoningandactinginlanguage
• list_slots(domain) - This function lists
models. arXivpreprintarXiv:2210.03629.
the slot names available for a given domain.
XiaoyingZhang,BaolinPeng,KunLi,JingyanZhou, Usethisfunctionafterlist_domainsandbeandHelenMeng.2023. SGP-TOD:BuildingTask
foreusingdb_querytoidentifytheslotsavail-
BotsEffortlesslyviaSchema-GuidedLLMPromptablefortheselecteddomain.
ing. In Findings of the Association for Computational Linguistics: EMNLP 2023, pages 13348–
• db_query(domain: str, state: dict,
13369, Singapore. Association for Computational
Linguistics. topk=1) - This function is used to query
the database to retrieve information in the
Qi Zhu, Christian Geishauser, Hsien chin Lin, Carel
belief state. Form the belief state with the
van Niekerk, Baolin Peng, Zheng Zhang, Michael
domain and slots that were identified using

### Heck, Nurul Lubis, Dazhen Wan, Xiaochen Zhu,

Jianfeng Gao, Milica Gašic´, and Minlie Huang. list_domainsandlist_slotstools.

## Convlab-3: Aflexibledialoguesystemtoolkit

based on a unified data format. arXiv preprint • get_booking_reference(domain,
arXiv:2211.17148. utterance=None) - This function is
usedtogenerateabookingreferenceforthe

### Qi Zhu, Zheng Zhang, Yan Fang, Xiang Li, Ryuichi

Takanobu, Jinchao Li, Baolin Peng, Jianfeng Gao, serviceselectedbytheuser.

### Xiaoyan Zhu, and Minlie Huang. 2020. Convlab-

2: An open-source toolkit for building, evaluating,

### Fordb_query,theagentveryrarelyusedthetopk

and diagnosing dialogue systems. In Proceedings parametertoretrievemoreresults. Incaseswhere
of the 58th Annual Meeting of the Association for theuserasksformoreoptions,theagentdefaults
ComputationalLinguistics: SystemDemonstrations,
tosayingthatithasonlyoneoptionwheninreality
pages142–149.
thedatabasedoescontainmultipleoptionsforthe
A TheReActPrompt query.
Figure 2 shows an example of the final ReAct B QualitativeAnalysis
prompt,namelyGenericPrompt,inwhichtheex-
Inthissection,welookatthedialoguesgenerated
amplesprovidedintheprompt(Figure3)contained
insimulationtoidentifywhatthesystemdidwell
arandomexamplefromtheMultiWOZdataset. We
and what it lacks when performing task-oriented
alsoexperimentedwithanothervariation(i.e.,Dodialogue. Werandomlyselected50dialoguesfrom
main Specific), in which the examples provided
the 1000 simulations for GPT-3.5 using generic
weredynamicallychangedbasedonthedomains
examples (cf. Appendix A), and we look at the
inthegoal. Weobservethatusingdomain-specific
dialoguesfromtheperspectiveofthesystem.
examples in the prompt has no effect on the performanceofthesystem. Ourresults(seeTable4) System produces creative responses but does
showthatthesysteminfactperformsslightlybetter not stick to the instructions An advantage of
whenthereisonlyonerandomexampleirrespec- using LLMs for dialogue tasks is that the system
tiveofthedomainsoftheusergoal. isabletorephraseitsresponseincaseswherethe
user repeats the request. This can be seen in the

### A.1 ToolDescription

exampleinFigure4. However,afteracertainpoint,
Thetoolsarepythonfunctionsthatweprovidein therepeatedrequestfromtheuserseemstoconfuse
theprompttoguidethemodeltomakegroundedde- the system resulting in a response where it talks
cisionswithrespecttoadatabase. Thus,itchooses about performing actions it does not have access
fromtheavailabledomainsandslotsinthedatabase to. If the system did indeed have access to more
6

<!-- Page 7 -->


### InformRate

PromptType AvgTurns BookRate SuccessRate CompleteRate

## (P/R/F1)


### Generic 14.9 56.2/67.5/58.6 36.8 28.3 48.5


### DomainSpecific 14.0 61.1/63.2/59.1 35.4 22.2 47.4

Table4: EvaluationoftheperformanceoftheReActTODsystemwhendomainspecificexamplesaregiven. This
experimentwasrunusingGPT-3.5for100dialoguesimulations.
Respondtothehumanashelpfullyandaccuratelyaspossible. Reasoning is not always consistent The main
Youhaveaccesstothefollowingtools: factorweareassessinginthissystemisanLLM’s
{tools} capabilities to reason and perform actions based
Usethefollowingformat: on the reasoning. Depending on the complexity
Question:theinputquestionyoumustanswer ofthegoalandtheuserutterance,weseethatthe
Thought:youshouldalwaysthinkaboutwhattodo LLMperformsreasoninginvaryinglevels. While
Action:theactiontotake,shouldbeoneof[{tool_names}] itmayseemthattheLLMisabletoreasonwell,it
Input:theinputtotheaction,shouldbeinJSONobject sometimesdoesnotsticktotheinstructionsgiven,
containingvaluesfor whileatothertimesitfollowstheinstructionsperthetoolparameters fectly,performingthestepsasgiveninthefew-shot
Observation:theresultoftheaction exampleintheprompt,leadingtoaperfectanswer.
...(thisThought/Action/Input/ObservationcanrepeatNtimes)
Thought:Inowknowthefinalanswer Issuesgeneratingthecorrectdialoguestate In
FinalAnswer:thefinalanswertotheoriginalinputquestion TOD,thesystemshouldaccumulatethebeliefstate
Ifyoucan’tfindtheanswerjustsayitasyourfinalanswer. inordertoanswertheuser’squeriescorrectly. We
Youdon’thavetouseatooleverytime,butwhenyoudo see in many cases that the system is not able to
onlyspecifythetoolname generatethecorrectstateastheturnsprogressand
astheAction. theuserprovidesmoreinformation.

### Example: HallucinationsareamajorissueinLLMs. We

{examples} see that this is the case even when using LLMs

### Begin! forTOD.Figure6showsthattheLLMproduces

Chathistory: invalidslots–‘time’insteadof‘arriveBy’inthis
{history} case.

### Question:{input} Anotherissuethatwasfoundwasthatthesystem

{agent_scratchpad} fillsthewrongslotswiththewronginformationas
shownintheexampleinFigure7. Slotidentifica-
Figure2: TheReActpromptusedtoinstructthesystem
tionandfillingisaveryimportantstepinTODand
LLMagentonhowtoperformtask-orienteddialogue.
these errors from the LLM will drastically affect
itsoverallperformance.
toolsformanagingbooking, thisresponsewould
havebeenidealinthissituation, helpingtheuser No clarifying questions from the system In a
confirmthedateofthebooking. complextasksuchastask-orienteddialogue,itis
essential that the system understands the user re-
Smallergoalsareeasiertoachieve Analysing questclearlyinordertobeabletoanswercorrectly.
the conversations, an interesting observation that Hence,incaseswheretheuserinputmightbeinstoodoutwasthattheshorterthegoal, theeasier complete,forexampleiftheuserdidnotgivethe
andquickeritwasforthesystemtoachieve. See destinationwhenaskingforinformationofatrain
the example in Figure 5 where the goal is to re- journey, the system must reason and ask the user
quest the phone and postcode of a police station. forthedestination. Inthedialoguesimulationsgen-
Thesystemisabletoreasoncorrectlybylearning erated,ithasbeennotedthatthesystemproceeds
fromtheexampleinthepromptandgivestheright togeneratethestateforthedatabasequerybased
answersaftergettingthevaluesfromthedatabase. ontheinformationtheuserprovided,anddoesnot
However,itmightalsobethesystemimitatingthe reasonwhethertheinformationprovidedisenough
example. tomakeaninformeddecision.
7

<!-- Page 8 -->

User: Ineedahotelplease.Canyouhelpmefindahotelcalledthe

### Question:arethereany3starhotel-s,guesthouses,

orbedandbreakfaststhathavewifithatyoudon’thavetopayfor? homefromhome?

### Thought:Theuserislookingfor3starhotels,guesthousesor


### System:Ihavefoundthehotelh¨omefromhome¨.Itisaguesthousein

bedandbreakfaststhathavefreewifi.Icanfindthisinformationinthe thenorthwithamoderatepricerangeand4stars.Wouldyoulikemore
database.ForthatIneedtoidentifythedomainandtheslotsandvalues. informationaboutit?
Action:list_domains User:Whatabout2nights?Thatwillwork.Canyoumakeareservation

### Input:{}

for3people,please?Onfridayplease.
Observation:[restaurant,hotel,attraction,train,hospital,taxi,police]

### System:Yourbookingreferenceforareservationfor3peoplefor

Thought:Thedomainhotelmatchestheuser’srequest.NowIneedto
2nightsatthehomefromhomeguesthouseonFridayis00000021.
identifytheslotnamesandvalues.
User:Ineedaroomstartingonfriday.

### Action:list_slots

System:Yourbookingreferenceforaroomatthehomefromhome

### Input:{domain:hotel}

guesthousestartingonFridayis00000021.
Observation:[address,area,internet,parking,id,location,name,phone,
User:Iwanttocheckinonfriday.
postcode,price,pricerange,stars,takesbookings,type]
Thought:Theuserisaskingfor3starhotel-s,guesthouses, System:I’msorry,Icouldn’tfindthecheck-indateforthereservation
orbedandbreakfaststhathavewifithatyoudon’thavetopayfor. madeearlier.PleaseprovidemewiththebookingreferenceagainsoI
Sotheslotsareinternet:freeandstars:3.NowIneedtoquerythedatabase cancheckthedetails.

### Action:db_query


### Figure4: AnexcerptofaconversationwheretheLLM

Input:{domai:hotel,state:{hotel:{internet:yes,stars:3}}}
showscreativewaystohandlerepeateduserrequests.
Observation:[[{address:151hillsroad,area:south,internet:yes,
parking:yes,id:11,location:[52.1725982,0.1112224],name:
bridgeguesthouse,phone:01223247942,postcode:cb28rj,price: OtherObservations
{double:75,family:90,single:50},pricerange:moderate,
• SystemistoohonestattimesIthasbeenobstars:3,takesbookings:yes,type:guesthouse,Ref:00000011},
servedthatthesystemrespondstoohonestly
location:[52.201275,0.129935],name:gonvillehotel,phone:
anddoesnotsticktothetoolsandinstructions
01223366611,postcode:cb11ly,’price’:{double:95,family:119,
providedtoanswertheuserquery. Forexamsingle:79},pricerange:expensive,stars:3,takesbookings:yes,
ple, when asked to book a table at a restautype:hotel,Ref:00000018},{address:156chestertonroad,area:
rant,thesystemrespondedwithI’msorry,but
north,internet:yes,parking:yes,id:19,location:

### I cannot complete the booking as I am not

[52.2309912,0.1295545],name:hamiltonlodge,phone:01223365664,
programmedtointeractwiththerestaurant’s
postcode:cb41da,price:{double:73,family:85,single:50},
booking system. while it was provided with
pricerange:moderate,stars:3,takesbookings:yes,type:
theget_booking_referencetooltoperform
guesthouse,Ref:00000019}]
thebooking.
Thought:Inowknowthefinalanswer.
FinalAnswer:Ihavefound3hotelsmatchingyourcriteria,
• AmericanvsBritishEnglishWeseethatthe
doyouhaveapricerangeinmind?
systemalwaysusesAmericanEnglishwhile
Question:no,butthehotelshouldbeinthenorth.
generatingtheresponseeventhoughtheuser

### Thought:Anewslot’area’withvalue’north’hasbeenidentifiedfrom

inputandthedatasetandexampleswereprotheuserrequestforthesamedomain’hotel’.Ineedtoquerythedatabase
videdinBritishEnglish. Thisshowsthatthe
withtheupdatedslotvalue.
majorityofthedatathattheLLMwastrained

### Action:db_query

onusesAmericanEnglish.
Input:{domain:hotel,state:{hotel:{internet:yes,
stars:3,area:north}}}
• Thesystemperformsadditionalstepswith-
Observation:[{address:156chestertonroad,area:north,internet:yes,
outbeingaskedTheLLMsometimestends
parking:yes,id:19,location:[52.2309912,0.1295545],name:
to get ahead of itself when performing taskhamiltonlodge,phone:01223365664,postcode:cb41da,price:
orienteddialogue. Forinstance,itwouldgen-
{double:73,family:85,single:50},pricerange:moderate,
erateabookingreferenceeventhoughtheuser
stars:3,takesbookings:yes,type:guesthouse,Ref:00000019}]
was only enquiring about an entity in a spe-
FinalAnswer:Ihavefoundthehamiltonlodge.Itisaguesthousein
cificdomain.
thenorth.Wouldyoulikemoreinformationaboutit?

### C LLMUserAgentIssues


### Figure3: TheexampleprovidedintheReActprompt

showingtheLLMthestepstobefollowedforperform-
Thissectionlooksattheconversationfromauser’s
ingTOD.
perspectivetoidentifythereasonstheconversation
8

<!-- Page 9 -->

goal:{police:{info:{},reqt:{postcode:?,address:?,phone:?}}}, User: Iwouldalsoliketobookatrain,please.Iwillleaveonmonday.
User: Hello,Ihavebeenrobbed.Canyoupleasehelpmegetintouch Ineedtobookatraintolondonkingscross.Iwouldliketoleaveafter
withthepolice? 14:15
Thought:Theuserisrequestingassistancetogetintouchwiththepolice. System: TheonlyavailabletrainthatmatchesyourrequestisTR6028
Ineedtoidentifythecorrectdomainforthisrequest. departingfromCambridgeat15:00andarrivingatLondonKingsCross
Action:list_domains at15:51onMonday.Yourbookingreferenceis00000005.Isthere

### Input:{} anythingelseIcanhelpyouwith?

Observation:[restaurant,hotel,attraction,train,hospital,taxi,police] User: Ineedittodepartfromcambridge.
Thought:Thedomainpolicematchestheuser’srequest.Ineedtofindthe Thought:Theuserhasprovidednewinformationthatthetrainshould
availableslotsforthisdomain departfromCambridge.Ineedtoupdatethequerytoincludethis
Action:list_slots information.

### Input:{domain:police} Action:db_query

Observation:[name,address,id,phone,postcode] Input:{domain:train,state:{train:{departure:cambridge,destination:
Thought:Theuserhasnotprovidedanyspecificinformationaboutthe londonkingscross,day:monday,time:after14:15}}}
policestationtheyneedtocontact.Ineedtoaskformoreinformationor

### Figure6: Anexcerptshowingthesystemhallucinating

provideageneralquerytoretrievealistofpolicestations
theslotname.

### Action:db_query


### Input:{domain:police,state:{police:{}}}

Observation:[{name:ParksidePoliceStation,address:Parkside,
User: Howdy,Ineedatrainheadingintolondonkingscross.Ineed

### Cambridge,id:0,phone:01223358966,postcode:cb11jg}]

atrainleavingafter16:30.Thetrainshouldleaveonwednesday

### System:Ihavefoundonepolicestationmatchingyourrequest.The

Thought:Theuserisrequestingforatrainleavingafter16:30heading
ParksidePoliceStationislocatedatParkside,Cambridge.Wouldyou
toLondonKingsCrossonWednesday.Ineedtoidentifythedomainand
likemetoprovideyouwiththeirphonenumber?
andslotsforthisrequest.
User:Canyougivemethephonenumberplease?CanIpleasehavethe

### Action:list_domains

postcodeofthepolicestationaswell?

### Input:{}


### Thought:Theuserisaskingforthephonenumberandpostcodeofthe

Observation:[restaurant,hotel,attraction,train,hospital,taxi,police]
policestation.Icanretrievethisinformationfromthedatabaseusingthe
Thought:Thedomainforthisrequestis’train’.NowIneedtoidentifythe
domain’police’andtheslot’phone’and’postcode’
slotsandvalues

### Action:db_query Action:list_slots

Input:{domain:police,state:{police:{}}} Input:{domain:train}
Observation:[{name:ParksidePoliceStation,address:Parkside, Observation:[’arriveBy’,’day’,’departure’,’destination’,’duration’
Cambridge,id:0,phone:01223358966,postcode:cb11jg}] ’leaveAt’,’price’,’trainID’]
System:ThephonenumberforParksidePoliceStationis01223358966 Thought:Theslotsforthisrequestare’departure’:after16:30,
andthepostcodeiscb11jg. ’destination’:LondonKingsCross,and’day’:Wednesday.Ineedtoquery
User:Youweregreat.Goodbye. thedatabasetofindtheavailabletrains

### System:Goodbye!Haveaniceday!


### Figure7:Anexcerptshowingthewrongslotbeingfilled

Figure5: Afullconversationforasimplegoal. bythesystem. departurereferstothedeparturestation
andleaveAtreferstothedeparturetime.
didnotgowellwhenweusedanLLMastheuser
agent.
up.

### LLMswitchesroleswiththesystem Duringthe

initialexperimentswheretheuseragentwasalso
playedbyanLLM,wenoticedaninterestingphe- Unable to end the conversation based on goal
nomenon. TheuserLLMsometimesswitchesits fulfillment Theuseragentwasnotabletoendthe
roleastheuserandpretendstobethesystem,pro- conversation based on the goal and conversation
vidinghallucinatedvaluesandaskingthesystem history. We also tried updating the goal at every
LLMclarifyingquestionsaboutitsprevioususer turntosteertheconversationintherightdirection.
request. Figure 8 shows two excerpts where the ThisalsodidnothelptheLLMidentifytheendof
userprovidesthesystemwithinformationitmade theconversationandresultedinrepeatedrequests.
9

<!-- Page 10 -->


### User: Whattypeofcardoyouneedforthetaxi? GPT-4

System:I’msorry,butIdon’thaveinformationaboutthetypeofcar User:Iwouldalsoliketobookatrain,please.Iwillleaveon
neededforthetaxi. monday.Ineedtobookatraintolondonkingscross.Iwouldlike
toleaveafter14:15.
User:System:Foryourrestaurantbooking,Icaninformyouthatthe System: Ihavefoundatrainforyou.ItdepartsfromCambridgeat
restaurantisnotavailableat5:30pm,butitisavailableat5:45pm. 15:00onMondayandarrivesatLondonKingsCrossat15:51.The
Wouldyoulikemetobookatablefor8peopleatPizzaHutCityCentre journeywilltake51minutesandtheticketpriceis23.60pounds.
at5:45pm? ThetrainIDisTR6028.Wouldyouliketobookthistrain?
System:I’msorry,Icouldn’tunderstandyourrequest.Pleaseprovide User: Ineedittodepartfromcambridge
avalidinput. System: Ihavefoundatrainforyou.ItdepartsfromCambridge
at05:00onMondayandarrivesatLondonKingsCrossat05:51.

### Figure8: ExcerptsshowingtheLLMpromptedtoplay

Thejourneywilltake51minutesandtheticketpriceis23.60pounds.
theuseractinglikethesystem.
ThetrainIDisTR7075.Wouldyouliketobookthistrain?
User: Iwouldliketoleaveafter14:15.
D ManualAnalysisofGPT-3.5vsGPT-4 System: Ihavefoundatrainforyou.ItdepartsfromCambridgeat
15:00onMondayandarrivesatLondonKingsCrossat15:51.

### WecomparedthegeneratedoutputsforbothGPT-

Thejourneywilltake51minutesandtheticketpriceis23.60pounds.
3.5 (Ouyang et al., 2022) and GPT-4 (OpenAI,
ThetrainIDisTR6028.Wouldyouliketobookthistrain?
2023) for 50 randomly selected goals. We saw
User: Iwouldlike3ticketsplease.
thattheperformanceofGPT-4issuperiortoGPT-3
System: Ihavebooked3ticketsforyou.Yourbookingreference
whenweconsiderthequalityofthereasoningand
is00000005.
generated texts. We explain a few of the reasons

## Gpt-3.5

whywefoundGPT-4tobeabetterconversational
User: Iwouldalsoliketobookatrain,please.Iwillleaveonmonday.
agentthanGPT-3.5below.
Ineedtobookatraintolondonkingscross.Iwouldliketoleaveafter
14:15.

### Parsing Errors GPT-4 is able to generate the

System: Yourbookingreferenceforthetrainserviceis00000106.
output in the required format when compared to
GPT-3.5. This means that even if the reasoning Figure9: ExcerptsofaconversationshowinghowGPT-
is correct, the parsing errors in the agent due to 4clarifiesandcommunicatesbetterthanGPT-3.5.
wrong output format can lead to the final answer
beingverydifferentfromtheintendedanswer. This
Politenessandverbosity Analysingthesystem
leadstomiscommunicationbetweentheuserand
utterances for both models, we saw that GPT-4
the system. GPT-4 is more adept at conforming
producesmoreverboseandpoliteanswers. While
totheprescribedformatthanGPT-3.5resultingin
GPT-3.5answersreasonablywell,itmayseemthat
betterperformance.
itismorealoofwhereastalkingwithGPT-4feels
morepleasant.

### Clarifying and verifying user requests GPT-

4 asks clarifying questions and verifies with the

### E UserInterfaceforHumanEvaluation

user before performing important steps such as
bookingaservice. Ontheotherhand,GPT-3.5does Figure 10 and Figure 11 are screenshots of the
the booking in the same turn without consulting webuserinterfaceprovidedtotheusersforhuman
the user. In these cases, there is a chance that evaluation. In the first step, the user is provided
theuserhasnotconveyedalltherequiredcriteria with instructions and a goal based on which the
for their chosen service. In real-world scenarios, userchatswiththerandomlyassignedsystem. The
thiscouldpotentiallyleadtomisinterpretationof secondstepprovidestheinterfacetoevaluatethe
theuserrequestandwasteofresourceswherethe conversationalongwithguidelines.
systembooksservicesthattheuserdoesnotwant.

### Hence, the ability of the GPT-4 model to ask the

user clarifying questions is a very important trait
inatask-orientedagent. SeeFigure9forasample
conversationonthesamegoalandhowGPT-4and
GPT-3.5differ.
10

<!-- Page 11 -->


### Figure10: Step1ofhumanevaluation: Chattingwiththesystem

Figure11: Step2ofhumanevaluation: Evaluatingtheconversation
11

## Tables

**Table (Page 8):**

| User: Ineedahotelplease.Canyouhelpmefindahotelcalledthe |
|---|
| homefromhome? |
| System:Ihavefoundthehotelh¨omefromhome¨.Itisaguesthousein |
| thenorthwithamoderatepricerangeand4stars.Wouldyoulikemore |
| informationaboutit? |
| User:Whatabout2nights?Thatwillwork.Canyoumakeareservation |
| for3people,please?Onfridayplease. |
| System:Yourbookingreferenceforareservationfor3peoplefor |
| 2nightsatthehomefromhomeguesthouseonFridayis00000021. |
| User:Ineedaroomstartingonfriday. |


**Table (Page 8):**

| Question:arethereany3starhotel-s,guesthouses, |
|---|
| orbedandbreakfaststhathavewifithatyoudon’thavetopayfor? |
| Thought:Theuserislookingfor3starhotels,guesthousesor |
| bedandbreakfaststhathavefreewifi.Icanfindthisinformationinthe |
| database.ForthatIneedtoidentifythedomainandtheslotsandvalues. |
| Action:list_domains |
| Input:{} |
| Observation:[restaurant,hotel,attraction,train,hospital,taxi,police] |
| Thought:Thedomainhotelmatchestheuser’srequest.NowIneedto |
| identifytheslotnamesandvalues. |
| Action:list_slots |
| Input:{domain:hotel} |
| Observation:[address,area,internet,parking,id,location,name,phone, |
| postcode,price,pricerange,stars,takesbookings,type] |
| Thought:Theuserisaskingfor3starhotel-s,guesthouses, |
| orbedandbreakfaststhathavewifithatyoudon’thavetopayfor. |
| Sotheslotsareinternet:freeandstars:3.NowIneedtoquerythedatabase |
| Action:db_query |
| Input:{domai:hotel,state:{hotel:{internet:yes,stars:3}}} |
| Observation:[[{address:151hillsroad,area:south,internet:yes, |
| parking:yes,id:11,location:[52.1725982,0.1112224],name: |
| bridgeguesthouse,phone:01223247942,postcode:cb28rj,price: |
| {double:75,family:90,single:50},pricerange:moderate, |
| stars:3,takesbookings:yes,type:guesthouse,Ref:00000011}, |
| location:[52.201275,0.129935],name:gonvillehotel,phone: |
| 01223366611,postcode:cb11ly,’price’:{double:95,family:119, |
| single:79},pricerange:expensive,stars:3,takesbookings:yes, |
| type:hotel,Ref:00000018},{address:156chestertonroad,area: |
| north,internet:yes,parking:yes,id:19,location: |
| [52.2309912,0.1295545],name:hamiltonlodge,phone:01223365664, |
| postcode:cb41da,price:{double:73,family:85,single:50}, |
| pricerange:moderate,stars:3,takesbookings:yes,type: |
| guesthouse,Ref:00000019}] |
| Thought:Inowknowthefinalanswer. |


**Table (Page 8):**

| guesthousestartingonFridayis00000021. |
|---|
| User:Iwanttocheckinonfriday. |
| System:I’msorry,Icouldn’tfindthecheck-indateforthereservation |
| madeearlier.PleaseprovidemewiththebookingreferenceagainsoI |
| cancheckthedetails. |


**Table (Page 8):**

| doyouhaveapricerangeinmind? |
|---|
| Question:no,butthehotelshouldbeinthenorth. |
| Thought:Anewslot’area’withvalue’north’hasbeenidentifiedfrom |
| theuserrequestforthesamedomain’hotel’.Ineedtoquerythedatabase |
| withtheupdatedslotvalue. |
| Action:db_query |
| Input:{domain:hotel,state:{hotel:{internet:yes, |
| stars:3,area:north}}} |
| Observation:[{address:156chestertonroad,area:north,internet:yes, |
| parking:yes,id:19,location:[52.2309912,0.1295545],name: |
| hamiltonlodge,phone:01223365664,postcode:cb41da,price: |
| {double:73,family:85,single:50},pricerange:moderate, |
| stars:3,takesbookings:yes,type:guesthouse,Ref:00000019}] |
| FinalAnswer:Ihavefoundthehamiltonlodge.Itisaguesthousein |
| thenorth.Wouldyoulikemoreinformationaboutit? |


**Table (Page 9):**

| User: Iwouldalsoliketobookatrain,please.Iwillleaveonmonday. |
|---|
| Ineedtobookatraintolondonkingscross.Iwouldliketoleaveafter |
| 14:15 |
| System: TheonlyavailabletrainthatmatchesyourrequestisTR6028 |
| departingfromCambridgeat15:00andarrivingatLondonKingsCross |
| at15:51onMonday.Yourbookingreferenceis00000005.Isthere |
| anythingelseIcanhelpyouwith? |
| User: Ineedittodepartfromcambridge. |
| Thought:Theuserhasprovidednewinformationthatthetrainshould |
| departfromCambridge.Ineedtoupdatethequerytoincludethis |
| information. |
| Action:db_query |
| Input:{domain:train,state:{train:{departure:cambridge,destination: |
| londonkingscross,day:monday,time:after14:15}}} |


**Table (Page 9):**

| User: Hello,Ihavebeenrobbed.Canyoupleasehelpmegetintouch |
|---|
| withthepolice? |
| Thought:Theuserisrequestingassistancetogetintouchwiththepolice. |
| Ineedtoidentifythecorrectdomainforthisrequest. |
| Action:list_domains |
| Input:{} |
| Observation:[restaurant,hotel,attraction,train,hospital,taxi,police] |
| Thought:Thedomainpolicematchestheuser’srequest.Ineedtofindthe |
| availableslotsforthisdomain |
| Action:list_slots |
| Input:{domain:police} |
| Observation:[name,address,id,phone,postcode] |
| Thought:Theuserhasnotprovidedanyspecificinformationaboutthe |
| policestationtheyneedtocontact.Ineedtoaskformoreinformationor |
| provideageneralquerytoretrievealistofpolicestations |
| Action:db_query |
| Input:{domain:police,state:{police:{}}} |
| Observation:[{name:ParksidePoliceStation,address:Parkside, |
| Cambridge,id:0,phone:01223358966,postcode:cb11jg}] |
| System:Ihavefoundonepolicestationmatchingyourrequest.The |


**Table (Page 9):**

| User: Howdy,Ineedatrainheadingintolondonkingscross.Ineed |
|---|
| atrainleavingafter16:30.Thetrainshouldleaveonwednesday |
| Thought:Theuserisrequestingforatrainleavingafter16:30heading |
| toLondonKingsCrossonWednesday.Ineedtoidentifythedomainand |
| andslotsforthisrequest. |
| Action:list_domains |
| Input:{} |
| Observation:[restaurant,hotel,attraction,train,hospital,taxi,police] |
| Thought:Thedomainforthisrequestis’train’.NowIneedtoidentifythe |
| slotsandvalues |
| Action:list_slots |
| Input:{domain:train} |
| Observation:[’arriveBy’,’day’,’departure’,’destination’,’duration’ |
| ’leaveAt’,’price’,’trainID’] |
| Thought:Theslotsforthisrequestare’departure’:after16:30, |
| ’destination’:LondonKingsCross,and’day’:Wednesday.Ineedtoquery |
| thedatabasetofindtheavailabletrains |


**Table (Page 9):**

| likemetoprovideyouwiththeirphonenumber? |
|---|
| User:Canyougivemethephonenumberplease?CanIpleasehavethe |
| postcodeofthepolicestationaswell? |
| Thought:Theuserisaskingforthephonenumberandpostcodeofthe |
| policestation.Icanretrievethisinformationfromthedatabaseusingthe |
| domain’police’andtheslot’phone’and’postcode’ |
| Action:db_query |
| Input:{domain:police,state:{police:{}}} |
| Observation:[{name:ParksidePoliceStation,address:Parkside, |
| Cambridge,id:0,phone:01223358966,postcode:cb11jg}] |
| System:ThephonenumberforParksidePoliceStationis01223358966 |
| andthepostcodeiscb11jg. |
| User:Youweregreat.Goodbye. |
| System:Goodbye!Haveaniceday! |


**Table (Page 10):**

| User: Whattypeofcardoyouneedforthetaxi? |
|---|
| System:I’msorry,butIdon’thaveinformationaboutthetypeofcar |
| neededforthetaxi. |


**Table (Page 10):**

| User:Iwouldalsoliketobookatrain,please.Iwillleaveon |
|---|
| monday.Ineedtobookatraintolondonkingscross.Iwouldlike |
| toleaveafter14:15. |
| System: Ihavefoundatrainforyou.ItdepartsfromCambridgeat |
| 15:00onMondayandarrivesatLondonKingsCrossat15:51.The |


**Table (Page 10):**

| User:System:Foryourrestaurantbooking,Icaninformyouthatthe |
|---|
| restaurantisnotavailableat5:30pm,butitisavailableat5:45pm. |
| Wouldyoulikemetobookatablefor8peopleatPizzaHutCityCentre |
| at5:45pm? |
| System:I’msorry,Icouldn’tunderstandyourrequest.Pleaseprovide |
| avalidinput. |


**Table (Page 10):**

| ThetrainIDisTR6028.Wouldyouliketobookthistrain? |
|---|
| User: Ineedittodepartfromcambridge |


**Table (Page 10):**

| Thejourneywilltake51minutesandtheticketpriceis23.60pounds. |
|---|
| ThetrainIDisTR7075.Wouldyouliketobookthistrain? |
| User: Iwouldliketoleaveafter14:15. |
| System: Ihavefoundatrainforyou.ItdepartsfromCambridgeat |
| 15:00onMondayandarrivesatLondonKingsCrossat15:51. |
| Thejourneywilltake51minutesandtheticketpriceis23.60pounds. |
| ThetrainIDisTR6028.Wouldyouliketobookthistrain? |
| User: Iwouldlike3ticketsplease. |
| System: Ihavebooked3ticketsforyou.Yourbookingreference |
| is00000005. |


**Table (Page 10):**

| User: Iwouldalsoliketobookatrain,please.Iwillleaveonmonday. |
|---|
| Ineedtobookatraintolondonkingscross.Iwouldliketoleaveafter |
| 14:15. |
| System: Yourbookingreferenceforthetrainserviceis00000106. |
