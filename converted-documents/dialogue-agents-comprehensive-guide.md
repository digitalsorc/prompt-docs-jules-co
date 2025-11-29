---
title: "Dialogue Agents Comprehensive Guide"
original_file: "./Dialogue_Agents_Comprehensive_Guide.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "chain-of-thought", "agents", "fine-tuning"]
keywords: ["https", "org", "doi", "dialogue", "associationforcomputationallinguistics", "association", "page", "linguistics", "emnlp", "task"]
summary: "<!-- Page 1 -->

NaturalLanguageEngineering(2019),1–00
doi:10.1017/xxxxx

## Article

Dialogue Agents 101: A Beginner’s Guide to Critical
Ingredients for Designing Effective Conversational

### Systems

ShivaniKumar,SumitBhatia,MilanAggarwal, andTanmoyChakraborty
IndraprasthaInstituteofInformationTechnology,Delhi;shivaniku@iiitd.ac.in
MediaandDataScienceResearchLab,Adobe;sumit.bhatia@adobe.com
MediaandDataScienceResearchLab,Adobe;milaggar@adobe.com
IndianInstituteofTechnology,Delhi;tanchak@iitd."
related_documents: []
---

# Dialogue Agents Comprehensive Guide

<!-- Page 1 -->

NaturalLanguageEngineering(2019),1–00
doi:10.1017/xxxxx

## Article

Dialogue Agents 101: A Beginner’s Guide to Critical
Ingredients for Designing Effective Conversational

### Systems

ShivaniKumar,SumitBhatia,MilanAggarwal, andTanmoyChakraborty
IndraprasthaInstituteofInformationTechnology,Delhi;shivaniku@iiitd.ac.in
MediaandDataScienceResearchLab,Adobe;sumit.bhatia@adobe.com
MediaandDataScienceResearchLab,Adobe;milaggar@adobe.com
IndianInstituteofTechnology,Delhi;tanchak@iitd.ac.in
(Receivedxxxxxxxx;revisedxxxxxxxx;acceptedxxxxxxxx)

### Abstract

Sharingideasthroughcommunicationwithpeersistheprimarymodeofhumaninteraction.Consequently,
extensive research has been conducted in the area of conversational AI, leading to an increase in the
availabilityanddiversityofconversationaltasks,datasets,andmethods.However,withnumeroustasks
being explored simultaneously, the current landscape of conversational AI has become fragmented.
Consequently,initiatingawell-thought-outmodelforadialogueagentcanposesignificantchallengesfor
apractitioner.Towardshighlightingthecriticalingredientsneededforapractitionertodesignadialogue
agentfromscratch,thecurrentstudyprovidesacomprehensiveoverviewoftheprimarycharacteristicsof
adialogueagent,thesupportingtasks,theircorrespondingopen-domaindatasets,andthemethodsused
tobenchmarkthesedatasets.Weobservethatdifferentmethodshavebeenusedtotackledistinctdialogue
tasks. However, building separate models for each task is costly and does not leverage the correlation
among the several tasks of a dialogue agent. As a result, recent trends suggest a shift towards building
unifiedfoundationmodels.Tothisend,weproposeUNIT,aUNifieddIaloguedataseTconstructedfrom
conversationsofvaryingdatasetsfordifferentdialoguetaskscapturingthenuancesforeachofthem.We
thentrainaUnifieddialoguefoundationmodel,GPT-2Uandpresentaconcisecomparativeperformanceof
GPT-2Uagainstexistinglargelanguagemodels.Wealsoexaminetheevaluationstrategiesusedtomeasure
theperformanceofdialogueagentsandhighlightthescopeforfutureresearchintheareaofconversational
AIwithathoroughdiscussionofpopularmodelssuchasChatGPT.

## Introduction

The significance of conversations as the fundamental medium of interaction transcends cultural
boundaries(DingemanseandFloyd2014).Consequently,interactingwithmachinesandseeking
information via conversational interfaces is an instinctive and familiar way for humans (Dalton
et al. 2022) as evidenced by the success of dialogue systems such as Apple’s SIRIa, Amazon’s
Competinginterests:ShivaniKumarispursuingherPhDatIndraprasthaInstituteofInformationTechnologyDelhi.
SumitBhatiaandMilanAggarwalareemployedatAdobe.TanmoyChakrabortyisemployedatIndianInstituteofTechnology
Delhi.
ahttps://www.apple.com/in/siri/
©CambridgeUniversityPress2019
4202
yaM
32
]LC.sc[
2v55270.7032:viXra

<!-- Page 2 -->

2 NaturalLanguageEngineering
Alexab, and most recently, ChatGPTc. Moreover, dialogue-based systemsd have extensively
been used for customer support (Botea et al. 2019; Feigenblat et al. 2021), mental health
support(Kretzschmaretal.2019),andcounseling(Malhotraetal.2022;Tewarietal.2021).
Designingpracticaldialogue-basedsystems,however,isachallengingendeavourasthereare
important questions that one needs to answer before embarking on developing such a system.
Criticalconsiderationsincludedeterminingthetypesofqueriesthesystemshouldanticipate(e.g.,
chit-chat versus informational), deciding whether to incorporate an external knowledge source,
anddeterminingthelevelofnaturallanguageunderstandingthesystemshouldsupport.Previous
surveysinthefieldofdialogue-basedsystemshavepredominantlyfocusedonexaminingspecific
systemcomponentsornarrowsubsetsoftasksandtechniques.Forinstance,recentsurveyshave
delvedintoareassuchasdialoguesummarization(Tuggeneretal.2021;Fengetal.2022a),textto-SQL (Qin et al. 2022), question answering (Pandya and Bhatt 2021), dialogue management
usingdeeplearning(Chenetal.2017a)andreinforcementlearning (Daietal.2021b).
Whilethesurveysnotedaboveprovidecomprehensiveinsightsintotheirrespectivedomains,
this abundance of information can make it overwhelming for both novice and experienced
researchers and professionals to identify the essential components required for building their
dialogue-basedsystems.Incontrast,weadoptabroaderperspectiveandofferapanoramicview
of the various constituents comprising a dialogue-based system, elucidate the individual tasks
involved in their development, and highlight the typical datasets and state-of-the-art methodologiesemployedfordesigningandevaluatingthesecomponents.Consequently,thetitle‘Dialogue
Agents101’isadeliberatechoiceaimingtoconveythatthearticleservesasanintroductoryguide
orprimertothefundamentalconceptsandprinciplesassociatedwithdialogueagents.Inacademic
settings,‘101’isoftenusedtodenoteintroductoryorbasic-levelcourses,andhere,itsuggeststhat
thearticleprovidesfoundationalknowledgeforreaderswhomaybenewtothetopicofdialogue
agents.Withthiscomprehensivesurvey,weaspiretoassistbeginnersandpractitionersinmaking
well-informed decisions while developing systems for their applications. Our specific objective
istocomprehensivelyencompassallprominentopen-sourcetextualEnglishdialoguedatasets
across major dialogue tasks. That is, every dataset under consideration in our study meets four
conditions:(i)itmustbewidelyrecognizedwithinitsrespectivefield;ii)itshouldincorporatea
textual component in both input and output; (iii) it must be publicly accessible, and; and (iv) it
mustbedesignedforEnglish.
To identify relevant material for our survey, we conducted a thorough search of the Papers
With Code websitee to identify all relevant tasks and datasets related to dialogue agents. Our
goal was to gather and systematically organize different types of tasks that may be required for
developingvariousdialogue-agents;andunderstandthemethodsforperformingthesetasks,and
datasets that are typically used to train and evaluate models for these tasks. From the initial list
obtained from Papers With Code, we then queried Google Scholar for publications and followed the citation threads to gather relevant literature for each task, encompassing datasets and
articlesproposedwellbeforetheestablishmentoftheplatforms.WeemphasizethatwhilePapers
With Codefunctionedasourreferenceforlocatingpertinentliterature,itsprincipalvalueslayin
pinpointingthekeyproblemstatementsinvestigatedwithinthedomainofdialogueagents.
While delving into contemporary deep learning methods in this investigation, it is crucial to
acknowledge the rich history of research in dialogue agents. Long before the advent of deep
learning, researchers were actively engaged in developing computational methods to facilitate
meaningful interactions between machines and humans (Bayer et al. 2001; Weizenbaum 1966).
In the nascent stages of dialogue agent development, researchers heavily relied on rule-based
bhttps://alexa.amazon.com/
chttps://openai.com/blog/chatgpt
dWeusedialogue-basedsystems,chatbots,conversationalsystems,anddialogueagentsinterchangeablyinthisarticle.
ehttps://paperswithcode.com/

<!-- Page 3 -->


### LATEXSupplement 3

systems (Webb 2000; McTear 2021). Human experts meticulously crafted these systems, incorporating predefined rules and decision trees to interpret user inputs and generate appropriate
responses.Classificationtasks,suchasintentdetectionandslotfilling,ofteninvolvedrule-based
pattern matching (De and Kopparapu 2010; Ren et al. 2018) and template-based approaches
(Onyshkevych 1993; McRoy et al. 2003) to identify the user’s intention based on specific keywords or syntactic structures. Generative tasks, such as response generation, posed a significant
challenge without deep learning techniques. Early approaches leveraged handcrafted templates
(Chu-Carroll and Carberry 1998; Weizenbaum 1966), where responses were generated by combining predefined phrases or sentences. This method, however, lacked the flexibility to generate
contextuallyrelevantandnuancedresponses,hinderingthenaturalflowofconversations.
Ascomputationalcapabilitiesadvanced,statisticalmethodsstartedgainingtractionindialogue
agent development. Hidden Markov Models (HMMs) (Rabiner and Juang 1986) and finite-state
machines (Ben-Ari and Mondada 2018) were applied to model the probabilistic nature of language and user interactions (Williams 2003; Williams et al. 2005). These models enabled a
more dynamic and probabilistic approach to intent detection and slot filling, contributing to the
improvementofdialoguesystemperformance(HusseinandGranat2002;Zhaoetal.2004).From
rule-basedsystemsandtemplate-basedapproachestoearlystatisticalmodels,researcherslaidthe
groundwork for the sophisticated deep learning methodologies that dominate the contemporary
landscapeweaimtostudyinthissurvey.Tosummarize,ourkeycontributionsareasfollows.
(1) Weproposeanin-depthtaxonomyfordifferentcomponentsandmodulesinvolvedinbuildingadialogueagent(Figure1).Wetakeapractitioner’sviewpointanddevelopthetaxonomy
intermsoffeaturesoftheunderlyingsystemanddiscussatlengththeroleplayedbyeachof
thefeaturesintheoverallsystem(Section2).
(2) Next,wepresentacomprehensiveoverviewofdifferenttasksanddatsetsintheliteratureand
relatethemtothefeaturesasidentifiedintheproposedtaxonomy(Table1).Weidentifyeleven
broadcategoriesoftasksrelatedtodialogue-basedsystemsandpresentadetailedoverviewof
differentmethodsforeachtaskanddatasetsusedforevaluatingthesetasks(Section3).Our
goalistohelpthereaderidentifykeytechniquesanddatasetsavailableforthetasksrelevant
totheirapplications.
(3) WepresentUNIT f,alargescaleunifieddialoguedataset,consistingofmorethan4.8Mdialoguesand441Mtokens,whichcombinethevariousdialoguedatasetsdescribedinSection6.
Since UNIT is made from the dialogues of open-sourced datasets, it is free to use for any
research purposes. This effort is motivated by the recent trends suggesting a shift towards
buildingunifiedfoundationmodels(Zhouetal.2023a)thatarepre-trainedonlargedatasets
andgeneralizetoavarietyoftasks.WemakeUNITavailabletotheresearchcommunitywith
agoaltosparkresearcheffortstowardsdevelopmentoffoundationmodelsoptimizedfordialogues.Weuse UNIT tofurtherpretrainpopularopendialoguefoundationmodelsandshow
howitcanhelpimprovingtheirperformanceonvariousdialoguetasks(Section6).

## DesigningaDialogueAgent

Before developing a dialogue agent, several crucial decisions must be made to determine the
appropriate architecture for the agent. Figure 1 illustrates a comprehensive overview of these
decisions, which provides a taxonomic framework for structuring the development process. A
clearunderstandingoftheendgoalweaimtoachievefromadialogueagentiscrucialforeffective
communication (Pomerantz and Fehr 2011). For instance, questions such as “Do we want the
dialogue agent to carry out goal-oriented or chit-chat conversations?” and “Does the agent need
any external knowledge to answer user queries?” should be answered. Figure 2 highlights the
fWemakeUNITpubliconhttps://github.com/LCS2-IIITD/UNIT.git

<!-- Page 4 -->

4 NaturalLanguageEngineering

### Goal oriented


### Chit-chat Domain oriented

Chit-chat User's Intent Slot Affect Di S a t lo a g te ue Engaging
Single turn goal Type Style Informative

### Context

Multi turn NLU Instructional
Implicit Implicit Empathetic

### Open


### Domain


### Short text

Specific Input D A ia g lo e g n u t e Output Structure

### Structural

None Knowledge

### Long text


### Structured

Explicit Evaluation Explicit
Unstructured Unimodal

### Unimodal

Modality Automated Human Interactive Modality

### Multimodal Multimodal

Figure1:Ataxonomicoverviewofadialogueagent.Themajorcomponentsfordesigningacompletepipelineofadialogueagentare–input(s),naturallanguageunderstanding(NLU),generated
output(s),andmodelevaluation.Eachcomponentcanbefurtherdividedbasedonthecharacteristicsrequiredinthefinaldialogueagent.
differenttypeofdialoguesbasedonthedifferentattributesoftheinputandoutputofthesysetem
asdiscussedbelow.
2.1InputtotheSystem
Afterestablishingtheend-goalofourdialogueagent,itisessentialtodeterminethevariousfactors
that will inform the input to the agent (Harms et al. 2019). Our contention is that the input can
possessbothimplicitandexplicitproperties,dependingonthetaskathand.
ImplicitAttributes. Weclassifythecharacteristicsoftheinputwhicharenotexplicitlyapparent
fromtheinputasimplicitattributesoftheinput.Thisinherentinformationcanbedecidedbased
onthreeaspects–theuser’sgoal(Muiseetal.2019),thedomainofthedialogues(Budzianowski
etal.2018),andthecontextneededtocarryouttheendtask(KielaandWeston2019).Depending
ontheobjectiveofthedialogueagent,theusercouldwanttoachievesomegoal,suchasmaking
a restaurant reservation, booking an airline ticket, or resolving technical queries. For such goalorienteddialogueagents,theinputfromtheuserisexpectedtodifferfromthatreceivedforgeneral
chit-chat(Muiseetal.2019).Goal-orienteddialogueagentsareoftendesignedtooperatewithin
aparticulardomain,whilechit-chat-basedagentsaremoreversatileandareexpectedtohandlea
broaderrangeofconversations(Zhangetal.2018).Inadditiontotheuser’sgoalandtheagent’s
domain,theconversationcontextalsoplaysacrucialroleinachievingtheagent’sobjective(Kiela
and Weston 2019). For example, utterance-level intent detection may not require understanding
deepconversationcontext,whilesummarizingdialogueswouldrequireacompleteunderstanding
ofthecontext(Gliwaetal.2019).
Explicit Attributes. Apart from the implicit aspects of the dialogue agent’s input, various input
characteristics are external in nature and should be considered while building a dialogue agent.
These aspects constitute the input modality (Jovanovic and Leeuwen 2018) and any additional
knowledgesuppliedtotheagent(Dinanetal.2019).Inputcanbeunimodal,suchastextoraudio,
or in a combination of modalities, such as an image and associated text, as in the case of visual
question-answering systems (Parvaneh et al. 2019). Furthermore, additional knowledge may be
requiredtogenerateappropriateresponses.Forexample,inachit-chatsetting,theagentmayneed

<!-- Page 5 -->


### LATEXSupplement 5

It is such a nice weather today.
What is the primary abnormality in
this image?
It is perfect for a picnic.

### Hemophilia. We should do it then!

(a)Goal-orientedsingle-turndialogueofasingle (b)Chit-chatmultiturndialogueofa
domain with structured knowledge and multi- opendomainwithnoexternalknowledgeandunimodalinput
modalinput
Figure2:Dialogueshighlightingdifferentattributesofadialogueagentinputandoutput.
topossesscommonsenseknowledge(StrathearnandGkatzia2022),whileinaquestion-answering
setting,theagentmayneedtoaccessrelevantdocumentstoprovideaccurateresponses(Fengetal.
2020).Therefore,anyexplicitknowledgesuppliedtothedialogueagentcanbestructured,likea
treeoratuple,orunstructured,likeadocument.
2.2NaturalLanguageUnderstanding
Afterreceivinginputfromtheuser,thesubsequentstepinvolvescomprehension(Liuetal.2021b).
Regardlessofwhetherthetaskisdomain-specificoropen-domain,specificattributesoftheinput
mustbeidentifiedtodeterminetherequiredoutput.Weidentifyfourprimaryattributesthatneed
to be identified from the input text – the user’s intent (Casanueva et al. 2020), any slots needed
to fulfill the intent (Weld et al. 2022a), affective understanding of the input (Ruusuvuori 2012),
andthedialoguestateoftheinpututterance(Balaramanetal.2021).Whileintentandslotsare
directlyusefulforadomain-specificagenttoeffectivelycompleteatask,affectunderstandingand
dialogue state tracking is also critical for a chit-chat-based agent. Affect understanding involves
comprehending the user’s emotion (Poria et al. 2019), sarcasm (Castro et al. 2019), and amusement(Bedietal.2021)intheinpututterance.Furthermore,dialoguestatetrackingchecksthetype
of utterance received by the agent, such as question, clarification, or guidance. Understanding
these aspects is essential to determine the utterance’s underlying meaning and provide relevant
responsesforthetask.
2.3OutputoftheSystem
Theoutputgeneratedbythedialogueagent,akintoitsinput,possessesbothimplicitandexplicit
attributes,describedbelow.
Implicit Attributes. Implicit attributes refer to the output’s type (Rastogi et al. 2020) and style
(Su et al. 2020; Troiano et al. 2023), while explicit attributes pertain to its modality (Sun et al.
2022b)andstructure(Yuetal.2018).Congruenttotheuser’sgoalintheinputscenario,thetype
ofattributeshouldbedecidedbasedontheendtaskneededtobeperformedbythedialogueagent.
Dependingontheendtaskoftheagent,theresultingoutputcanbeinformative(Fengetal.2020),

<!-- Page 6 -->

6 NaturalLanguageEngineering
engaging(Zhangetal.2018),instructional(StrathearnandGkatzia2022),orempathetic(Rashkin
etal.2019).Forinstance,aquestion-answering-basedbotshouldbeinformative,whileacooking
recipebotshouldbemoreinstructional.Bothbotsneednotbeempatheticinnature.
Explicit Attributes. While the inherent properties of the output text are critical to assess, the
explicit attributes, such as modality and structure, must be considered before finalizing the dialogue agent’s architecture. Modality decides whether the required output is unimodal (such as
text) or multimodal (such as text with an image). Moreover, the output can be structured differentlybasedonthetaskathand.Forinstance,taskssuchastext-to-SQL(Yuetal.2018)conversion
requiretheoutputtoadheretoacertainstructure.Afterconsideringvariousaspectsoftheinput,
output, and understanding based on the end task, the generated output is evaluated to gauge the
performance of the resultant dialogue agent (Deriu et al. 2021). A detailed discussion about the
evaluationcanbefoundinSection5.

## Tasks,DatasetsandMethods

By drawing upon the taxonomy depicted in Figure 1 and existing literature, we identify eleven
distincttasksrelatedtodialoguethatcaptureallnecessarycharacteristicsofadialogueagent.In
ordertoconstructadialogueagent,apractitionermustbeawareofthesetasks,whichcanbeclassifiedintotwoprimarycategories–generativeandclassification.Specifically,theidentifiedtasks
include Dialogue Rewrite (DR) (Elgohary et al. 2019), Dialogue Summary (DS) (Gliwa et al.
2019;Chenetal.2021b),DialoguetoStructure(D2S)(Yuetal.20192018;Guptaetal.2018),
QuestionAnswering(QA)(Zhouetal.2018;Reddyetal.2019;Aliannejadietal.2020;Cuietal.
2020),KnowledgeGroundedResponse(KGR)(YusupovandKuratov2018;Fengetal.2020;
Zhangetal.2018;Westonetal.2015;Dzirietal.2022;Moonetal.2019;StrathearnandGkatzia
2022),Chit-Chat(CC)(Sevegnanietal.2021;Kimetal.2022c;Youngetal.2022;Zhangetal.
2022;Kimetal.2022a;Jurafskyetal.1997),andTask-OrientedDialogues(TOD)(Loweetal.
2015;Chenetal.2021a;Westonetal.2015;Linetal.[n.d.];Heetal.2018;Karadzhovetal.2021;
Shalyminov et al. 2019) in the generative category, and Intent Detection(ID) (Casanueva et al.
2020; Larson et al. 2019; Liu et al. 2021c; Rastogi et al. 2020), Slot Filling (SF) (Coope et al.
2020),DialogueStateTracking(DST)(Ericetal.2020),andAffectDetection(AD)(Poriaetal.
2019;Lietal.2017;Castroetal.2019;Rashkinetal.2019)intheclassificationcategory.Table1
summarisesallthedatasetsconsideredinthisstudyforeachofthementionedtasksandillustrates
thecharacteristicssatisfiedbyeachofthesetasksfromthetaxonomy.Aswedelveintothedetails
of each task type in the forthcoming sections, it is noteworthy to highlight a few observations
obtainedfromthepresentedtable.
• Indialoguedatasetsfeaturingchit-chatconversations,aninclinationtowardscharacteristics
indicative of open domain, multi-turn interactions, and the absence of external knowledge
is observed. Notably, a prevalent trend emerges in the generation of similar output within
suchdatasets.Anidentifiedgapintheexistinglandscapepertainstothescarcityofdatasets
integratingexternalknowledgewithchit-chatdialogues.Recognizingthepotentialenrichmentthatassociatedknowledge,particularlycommonsense(Ghosaletal.2020),canbring
todialogues,itbecomesapotentialfutureresearcharea.
• Forinstanceswherethedatasetcomprisesgoal-orientedconversations,itisprobablethatthe
datasetistailoredtoaspecificdomain,assistedwitheitherstructuredorunstructuredknowledgelinkedtoit.Goal-orienteddialoguestypicallycentrearoundspecifictaskslikebooking
airlinetickets,schedulingdoctorappointments,orsecuringrestaurantreservations.Notably,
these ‘goals’ can extend beyond specific tasks to encompass aspects such as the accomplishment of the goal of dialogue engagement (Gottardi et al. 2022). Intriguingly, such
goal-orientation does not necessarily confine the dialogue to a predefined domain, allowingforanopen-domaincontext.Aprospectiveavenueforresearchliesinthedevelopment

<!-- Page 7 -->

LATEXSupplement 7

### Input Output


### Type Task Datasets Implicit Explicit Implicit Explicit Size

User’sgoal Domain Context Modality Knowledge Type Style Modality Structure
evitareneG
noitamrofsnarT
CC OG nepO cpS TS TM U M enoN rtsnU rtS CC OG gnE fnI rtsnI pmE U M rohS gnoL tcurtS
DR CANARD(Elgoharyetal.2019) ✓ - ✓ - - ✓ ✓ - ✓ - - ✓ - ✓ ✓ - - ✓ - - ✓ - 40
DialogSum(Chenetal.2021b) ✓ - ✓ - - ✓ ✓ - ✓ - - ✓ - ✓ - - - ✓ - - ✓ - 13

## Ds

SAMSumCorpus(Gliwaetal.2019) ✓ - ✓ - - ✓ ✓ - ✓ - - ✓ - ✓ - - - ✓ - - ✓ - 16
CoSQL(Yuetal.2019) - ✓ - ✓ ✓ - ✓ - - - ✓ - ✓ - - ✓ - ✓ - - - ✓ 2
D2S SPIDER(Yuetal.2018) - ✓ - ✓ ✓ - ✓ - - - ✓ - ✓ - - ✓ - ✓ - - - ✓ 10
TOP(Guptaetal.2018) - ✓ - ✓ ✓ - ✓ - ✓ - - - ✓ - ✓ - - ✓ - ✓ - - 44
noitarenegesnopseR
CMUDoG(Zhouetal.2018) - ✓ ✓ - - ✓ ✓ - - ✓ - - ✓ - ✓ - - ✓ - - ✓ - 4
CoQA(Reddyetal.2019) - ✓ - ✓ - ✓ ✓ - - ✓ - - ✓ - ✓ - - ✓ - - ✓ - 127

## Qa

ClariQ(Aliannejadietal.2020) - ✓ ✓ - - ✓ ✓ - - ✓ - - ✓ - ✓ - - ✓ - - ✓ - 1k
Mutual(Cuietal.2020) ✓ - ✓ - - ✓ ✓ - ✓ - - ✓ - ✓ - - - ✓ - ✓ ✓ - 8
ConvAI(YusupovandKuratov2018) - ✓ ✓ - - ✓ ✓ - - ✓ - - ✓ - ✓ - - ✓ - - ✓ - 2
Doc2Dial(Fengetal.2020) - ✓ - ✓ - ✓ ✓ - - ✓ - - ✓ - ✓ - - ✓ - - ✓ - 4
PersonaChat(Zhangetal.2018) ✓ - ✓ - - ✓ ✓ - - ✓ - ✓ - ✓ - - - ✓ - - ✓ - 19
KGR bAbI(Westonetal.2015) - ✓ - ✓ - ✓ ✓ - - - ✓ - ✓ - ✓ ✓ - ✓ - ✓ ✓ - 161
FaithDial(Dzirietal.2022) ✓ - ✓ - - ✓ ✓ - - ✓ - ✓ - ✓ - - ✓ ✓ - - ✓ - 32
OpenDialKG(Moonetal.2019) - ✓ - ✓ - ✓ ✓ - - - ✓ - ✓ ✓ - - - ✓ - - ✓ - 15
Task2Dial(StrathearnandGkatzia2022) - ✓ - ✓ - ✓ ✓ - - ✓ - - ✓ - ✓ ✓ - ✓ - - ✓ - 1
OTTers(Sevegnanietal.2021) ✓ - ✓ - - ✓ ✓ - ✓ - - ✓ - ✓ - - - ✓ - - ✓ - 8
ProsocialDialog(Kimetal.2022c) ✓ - ✓ - - ✓ ✓ - - ✓ - ✓ - ✓ ✓ - ✓ ✓ - - ✓ - 5
FusedChat(Youngetal.2022) - ✓ - ✓ - ✓ ✓ - - - - - ✓ - ✓ - - ✓ - ✓ ✓ - 10

## Cc

mDIA(Zhangetal.2022) ✓ - ✓ - - ✓ ✓ - ✓ - - ✓ - ✓ - - - ✓ - - ✓ - 12
SODA(Kimetal.2022a) ✓ - ✓ - - ✓ ✓ - - ✓ - ✓ - ✓ ✓ - ✓ ✓ - ✓ ✓ - 1k
Switchboard-1(Jurafskyetal.1997) ✓ - ✓ - - ✓ ✓ - ✓ - - ✓ - ✓ - - - ✓ - ✓ ✓ - 2
UbuntuDialogueCorpus(Loweetal.2015) - ✓ - ✓ - ✓ ✓ - ✓ - - - ✓ - ✓ ✓ - ✓ - - ✓ - 1k
ABCD(Chenetal.2021a) - ✓ - ✓ - ✓ ✓ - - - ✓ - ✓ - ✓ ✓ - ✓ - - ✓ - 10
BiTOD(Linetal.[n.d.]) - ✓ - ✓ - ✓ ✓ - ✓ - - - ✓ - ✓ - - ✓ - ✓ ✓ - 7

## Tod

CraiglistBargains(Heetal.2018) - ✓ - ✓ - ✓ ✓ - - - ✓ - ✓ ✓ ✓ - - ✓ - - ✓ - 6
DeliData(Karadzhovetal.2021) - ✓ ✓ - - ✓ ✓ - - - ✓ - ✓ - ✓ ✓ - ✓ - - ✓ - 0.5
MetalWOz(Shalyminovetal.2019) - ✓ - ✓ - ✓ ✓ - ✓ - - - ✓ - ✓ - - ✓ - - ✓ - 10
noitacfiissalC
Banking77(Casanuevaetal.2020) - ✓ - ✓ ✓ - ✓ - ✓ - - - ✓ - ✓ - - ✓ - ✓ - - 13
CLINC150(Larsonetal.2019) - ✓ - ✓ ✓ - ✓ - ✓ - - - ✓ - ✓ - - ✓ - ✓ - - 23

## Id

HWU64(Liuetal.2021c) - ✓ - ✓ ✓ - ✓ - ✓ - - - ✓ - ✓ - - ✓ - ✓ - - 11
SGD(Rastogietal.2020) - ✓ - ✓ ✓ - ✓ - ✓ - - - ✓ - ✓ - - ✓ - ✓ - - 16
SF Restaurant8k(Coopeetal.2020) - ✓ - ✓ ✓ - ✓ - ✓ - - - ✓ - ✓ - - ✓ - ✓ - - 11
DST MultiWOZ2.1(Ericetal.2020) - ✓ - ✓ - ✓ ✓ - ✓ - - - ✓ - ✓ ✓ - ✓ - ✓ ✓ - 10
DailyDialogue(Lietal.2017) ✓ - ✓ - - ✓ ✓ - ✓ - - ✓ - ✓ - - ✓ ✓ - ✓ ✓ - 11
MELD(Poriaetal.2019) ✓ - ✓ - - ✓ - ✓ ✓ - - ✓ - ✓ - - ✓ ✓ - ✓ ✓ - 1

## Ad

MUStARD(Castroetal.2019) ✓ - ✓ - - ✓ - ✓ ✓ - - ✓ - ✓ - - - ✓ - ✓ ✓ - 6
EmpatheticDialogues(Rashkinetal.2018) ✓ - ✓ - - ✓ ✓ - - - - ✓ - ✓ - - ✓ ✓ - - ✓ - 24
Table 1. : Characteristic of each task based on the taxonomic characteristic of a dialogue
agent. Size indicates an approximate value expressed in thousands (k). Abbreviations – DR:
DialogueRewrite,DS:DialogueSummary,D2S:DialoguetoStructure,QA:QuestionAnswering,
KGR: Knowledge Grounded Response, CC: Chit-chat, TOD: Task Oriented Dialogues, ID:
Intent Detection, SF: Slot Filling, DST: Dialogue State Tracking, AD: Affect Detection, CC:
Chit-chat, GO: Goal Oriented, Spc: Specific, ST: Single Turn, MT: Multi Turn, U: Unimodal,
M: Multimodal, Unstr: Unstructured, Str: Structured, Eng: Engaging, Inf: Informative, Instr:
Instructional,Emp:Empathetic.
of more open-domain, goal-oriented dialogue datasets that focus more on conversational
goalslikeuserengagement.
• The chit-chat setting exhibits the predominant trend of producing extensive and engaging
dialogueoutput(Gottardietal.2022).Incontrast,thegoal-orientedsettingcommonlyyields
responses characterized by informativeness, instructional clarity, and brevity (Muise et al.
2019). Intriguingly, datasets combining both goal-oriented and chit-chat conversations are
notably sparse, despite real-world dialogues frequently encompassing a fluid interchange

<!-- Page 8 -->

8 NaturalLanguageEngineering
between these conversational types (Shuster et al. 2022). The presence of such datasets
couldsubstantiallyenhancetheresearchcommunity’scapabilitiesandinsights.
3.1GenerativeDialogueTasks
Generative dialogue tasks require the handling of diverse input and output characteristics (Chen
etal.2017b).Thesetaskscanbeclassifiedintotwodistincttypes–transformationandresponse
generation.Intransformationtasks,theoutputofthegiveninputconversationisnotthesubsequent
responsebutrathersomeothermeaningfultext,suchasadialoguesummary(Gliwaetal.2019).
Ontheotherhand,responsegenerationtasksinvolvegeneratingthenextresponseinthedialogue,
givenaninputcontext(Zhangetal.2020b).
3.1.1TransformationTasks
DialogueRewrite(DR). Thistaskinvolvesthechallengingprocessofmodifyingagivenconversationalutterancetobetterfitaspecificsocialcontextorconversationalobjective,whileretaining
its original meaning. To explore this task further, we turn to the CANARD dataset (Elgohary
et al. 2019). This dataset is specifically designed for rewriting context-dependent questions into
self-contained questions that can be answered independently by resolving all coreferences. The
objectiveistoensurethatthenewquestionhasthesameanswerastheoriginalone.Quanetal.
(2019) and Martin et al. (2020) proposed the TASK and MuDoCo datasets, respectively, focusing on rewriting dialogues in a way that coreferences and ellipsis are resolved. Huang et al.
(2021) combined sequence labelling and autoregression techniques to restore utterances withoutanycoreferences.Incontrast,Jiangetal.(2023)shapedthedialoguerewritetaskassentence
editingandpredictededitoperationsforeachwordinthecontext.Othermethodsalsouseknowledge augmentation (Ke et al. 2022), reinforcement learning (Chen et al. 2022b), and the copy
mechanism(Quanetal.2019).
Keychallenges. Despite achieving a reasonable performance in the dialogue rewrite task,
some challenges remain, with the major obstacle being the inclusion of new words in the
groundtruthannotationsthataredifficulttoincorporateintothepredictedrewrite(Liuetal.
2020b). In order to mitigate this challenge, many studies have explored the methods of
lexiconintegration(Leeetal.2023;Czarnowskaetal.2020),open-vocabulary(Raffeletal.
2020;Haoetal.2021;Vuetal.2022),andcontext-awareencoding(Xiaoetal.2020;Vinyals
etal.2015).
Dialogue summary (DS). Dialogues, despite their importance in communication, can often
become lengthy and veer off-topic. This can make it challenging to extract the meaningful content from the entire conversation. To overcome this issue, the task of dialogue summarization
has emerged. Dialogue summarization presents a concise account of the key topics, ideas, and
arguments discussed during the conversation. There are two prominent datasets that address the
challenge of dialogue summarization: the SAMSum (Gliwa et al. 2019) and DialogSum (Chen
etal.2021b)corporaconsistingofdialoguesandtheircorrespondingsummaries.TheSAMSum
dataset consists of dialogues that were curated by linguists who are fluent in English and who
attempted to simulate messenger-like conversations. While DialogSum consists of face-to-face
spoken dialogues covering various daily life topics such as schooling, work, and shopping. The
dialoguesarepresentinthetextualformatinbothdatasets.OtherdatasetssuchasQMSum(Zhong
et al. 2021), MediaSum (Zhu et al. 2021), DiDi (Liu et al. 2019), CCCS (Favre et al. 2015),
Telemedicine (Joshi et al. 2020), CRD3 (Rameshkumar and Bailey 2020), Television Shows
(Zechner and Waibel 2000), AutoMin (Nedoluzhko et al. 2022), and Clinical Encounter Visits

<!-- Page 9 -->


### LATEXSupplement 9

(Yim and Yetisgen 2021) are also constructed for the task of dialogue summarisation. For a
detailedguideonthetask,weredirectthereaderstotheextensivesurveyconductedbyTuggener
etal.(2021).Manyarchitectureshavebeenproposedtosolvethetaskofdialoguesummarisation.
Liangetal.(2023)usestopic-awareGlobal-LocalCentrality(GLC)toextractimportantcontext
fromallsub-topics.Bycombiningglobal-andlocal-levelcentralities,theGLCmethodguidesthe
model to capture salient context and sub-topics while generating summaries. Other studies have
utilized contrastive loss (Halder et al. 2022), multi-view summary generation (Chen and Yang
2020),post-processingtechniquesimprovingthequalityofsummaries(Leeetal.2021),external
knowledge incorporation (Kim et al. 2022b), multimodal summarisation (Atri et al. 2021), and
methods to reduce hallucinations in generated summaries (Liu and Chen 2021; Narayan et al.
2021;Wuetal.2021b).
Keychallenges.Withthehelpofpre-trainedlanguagemodels,currentmethodsareadeptat
converting the original chat into a concise summary. Nonetheless, these models still face
challenges in selecting the crucial parts and tend to generate hallucinations (Feng et al.
2022a).Inthecaseoflongerdialogues,themodelsmayexhibitbiastowardsaspecificpart
ofthechat,suchasthebeginningorend,producingsummariesthatarenotentirelysatisfactory(Deyetal.2020). Manystudiesexplorenovelattentionmechanismwithtopicmodeling
(Xiaoetal.2020),reinforcementlearninganddifferentialrewards(Chenetal.2023;Italiani
etal.2024;Zhangetal.2023),andknowledgeaugmentationwithfact-checking(Huaetal.
2023;Hwangetal.2023)tomitigatethesechallenges.
Dialogue to structure (D2S). Although natural language is the fundamental way humans communicate,theinteractionbetweenhumansandmachinesoftenrequiresamorestructuredlanguage
suchasSQLorsyntactictrees.TaskssuchasText-to-SQLandSemanticParsingseektobridgethe
gapbetweennaturallanguageandmachine-understandableformsofcommunication.Toaddress
this,fourprominentdatasetshavebeendeveloped–CoSQL(Yuetal.2019),SPIDER(Yuetal.
2018), and WikiSQL (Zhong et al. 2017) for text-to-sql, which are composed of pairs of naturallanguagequeriespairedwiththeircorrespondingSQLqueries,andtheTaskOrientedParsing
(TOP) dataset (Gupta et al. 2018) for semantic parsing which contains conversations that are
annotated with hierarchical semantic representation for task-oriented dialogue systems. There
are numerous approaches to handling these datasets, including encoder/decoder models with
decoder constraints (Wang et al. 2019b; Yin and Neubig 2017), large language models without
anyconstraints(Suhretal.2020;Linetal.2020),finalhypothesispruning(Scholaketal.2021),
span-basedextraction(Pasupatetal.2019;Mengetal.2022),dataaugmentation(Leeetal.2022;
Xuan2020),andensemblingtechniques(Einolghozatietal.2018).
Keychallenges.DespiterecentadvancementsinD2Stypetasks,thereremainsascarcityof
high-qualityresourcesrelatedtocomplexqueries(Leeetal.2022).Furthermore,theperformanceofD2Smodels tendstobesuboptimalwhenencounteringsmallperturbations, such
assynonymsubstitutionsortheintroductionofdomain-specificknowledgeintheinput(Qin
etal.2022). Existingstudiesexploretheareasofdataaugmentationwithresourcecreationto
solvethischallenge(Joshietal.2022;Minetal.2020).Enhancingrobustnessandhandling
perturbation(Yuetal.2023;Jiaetal.2019)areotherpossiblesolutionstothechallengeof
brittlenessintheD2Stasks.Furtherresearchinthisdirectioncouldyieldvaluableinsights.
3.1.2ResponseGeneration
QuestionAnswering(QA). Dialogueagentsmustpossesstheabilitytoaskrelevantquestionsin
ordertoengagetheparticipantsbyintroducinginterestingtopicsviaquestionsingeneralchit-chat

<!-- Page 10 -->

10 NaturalLanguageEngineering
setting(Gottardietal.2022),andprovideappropriateanswerstouserinquiries,toremainauthenticintheQAsetting(Elgoharyetal.2019).Asaresult,QuestionAnswering(QA)isacrucialtask
fordialogueagentstoperformcompetently.Tothisend,datasetssuchasCMUDoG(Zhouetal.
2018), CoQA (Reddy et al. 2019), SQuAD (Rajpurkar et al. 2016 2018), ClariQ (Aliannejadi
et al. 2020), and Mutual (Cui et al. 2020) are among the most notable and widely used for the
purpose of training and evaluating QA systems. If external knowledge is used to answer questions,thetaskcanbetermedasknowledge-groundedquestionanswering(Mengetal.2020).The
CMUDoG,CoQA,andSQuADdatasetsareexamplesofthiscategory.TheFIREmodel(Guetal.
2020) utilizes context and knowledge filters to create context- and knowledge-aware representationsthroughglobalandbidirectionalattention.Othermethodsincludemultitasklearning(Zhou
andSmall2020),semanticparsing(BerantandLiang2014;Reddyetal.2014),knowledge-based
grounding(Yihetal.2015;Liangetal.2017),andinformation-retrievalbasedmethods(Bordes
etal.2015;Dongetal.2015).Ontheotherhand,theClariQandMutualdatasetsdoesnotcontain
any external knowledge. Komeili et al. (2022) have proposed using the Internet as a source for
obtaining relevant information. In contrast, Hixon et al. (2015) proposes to learn domain from
conversationcontext.Zero-shotapproaches(Wangetal.2023b),adversarialpretraining(Pietal.
2022),convolutionnetworks(Liuetal.2022a),andgraphbasedmethods(Ouyangetal.2021)are
alsousedtosolvethetaskofQA.
Keychallenges. In the field of discourse-based question answering, which requires models
toconsiderbothdeepconversationcontextandpotentialexternalknowledge,anaphoraresolutionstillposesasignificantchallengethatnecessitatesfurtherinvestigation(Pandyaand
Bhatt2021).Additionally,capturinglongdialoguecontext(Christmannetal.2022)andpreventingtopicaldrift(Venkatarametal.2020)offersotherresearchdirection. Manystudies
explorethesechallengesandproposeviablesolutionstomitigatethem(Linetal.2021;Wu
etal.2023b).However,areliablesolutionstillneedsmoreresearchinthefield.
Knowledge grounded response (KGR). Similar to knowledge-grounded question answering,
knowledge-grounded response generation is a task that utilizes external knowledge to generate
relevantresponses.SomeoftheprimarydatasetsrelatedtoknowledgegroundingincludeConvAI
(YusupovandKuratov2018),Doc2Dial(Fengetal.2020),PersonaChat(Zhangetal.2018),bAbI
(Westonetal.2015),FaithDial(Dzirietal.2022),OpenDialKG(Moonetal.2019),andTask2Dial
(Strathearn and Gkatzia 2022). Most methods that aim to solve the task of knowledge grounded
responsegeneration,likeknowledgegroundedQA,usesatwostepapproachofretrievalandgeneration (Zhan et al. 2021; Wu et al. 2021a), graph-based approach (Wang et al. 2020; Li et al.
2021a), reinforcement learning approach (Hedayatnia et al. 2020), and retrieval-free approaches
(Xuetal.2022).
Keychallenges. The current trend in knowledge grounded response generation is to use a
two-stepapproachofretrievalandgeneration,whichincreasesthecomplexityofthesystem
(Zhou et al. 2022). Recently, researchers such as Xu et al. (2022) and Zhou et al. (2022)
haveexploredwaystobypasstheretrievalstepandproducemoreefficientmodels.Further
researchinthisdirectioncanimprovetheefficiencyofsystems.
Chit-chat (CC). The primary goal of a dialogue agent is to generate responses, whether it is
for chit-chat based dialogues or task-oriented dialogues. This section will specifically focus on
theresponsegenerationforchit-chatagents.Whiletherearenumerousdialoguedatasetsavailable
thatcontainchit-chatdialoguesandcanbeusedastrainingdata,suchasPersonaChat(Zhangetal.
2018),MELD(Poriaetal.2019),DailyDialogue(Lietal.2017),MUStARD(Castroetal.2019),
andMutual(Cuietal.2020),therearesomedatasetsspecificallycuratedforthetaskofchit-chat

<!-- Page 11 -->


### LATEXSupplement 11

generation. Examples of such datasets include OTTers (Sevegnani et al. 2021), ProsocialDialog
(Kimetal.2022c),FusedChat(Youngetal.2022),mDIA(Zhangetal.2022),SODA(Kimetal.
2022a),andtheSwitchboard-1corpus(Jurafskyetal.1997).Majorapproachesusedtogenerate
responses for chit-chat dialogue agents include the use of contrastive learning (Li et al. 2022a
2021b;Caietal.2020),continuallearning(Liuetal.2022c;LiuandMazumder2021;Mietal.
2020),andTransformerbasedmethods(Liuetal.2020a;Caietal.2019;OluwatobiandMueller
2020).
Keychallenges. Typical challenges with chit-chat agents, such as inconsistency, unfaithfulness, and an absence of a uniform persona, persist (Liu et al. 2017a). Furthermore, the
ineffective management of infrequently used words is another tenacious issue (Shum et al.
2020). However, current advancements, such as Reinforcement Learning from Human
Feedback (RLHF) (Christiano et al. 2017; Stiennon et al. 2020), help in minimising these
issues.
Task-oriented dialogues (TOD). To generate domain-specific responses, task-oriented dialogue
agentsrequireaspecializedapproach.Fortunately,thereareseveraldatasetsavailablethatfeature
domain-oriented dialogues, including the Ubuntu Dialogue Corpus (Lowe et al. 2015), ABCD
(Chen et al. 2021a), bAbI (Weston et al. 2015), BiTOD (Lin et al. [n.d.]), CraiglistBargains
(He et al. 2018), DeliData (Karadzhov et al. 2021), and MetalWOz (Shalyminov et al. 2019).
Generating task-oriented dialogues follows a similar approach to open domain dialogues, utilizingreinforcementlearning(Khandelwal2021;Liptonetal.2018;Liuetal.2017b),graphbased
methods(Yangetal.2020;Liuetal.2021a;Andreasetal.2020),andTransformerbasedmethods
(Chawlaetal.2020;Parvanehetal.2019).
Keychallenges. The current datasets in this area feature restrictive input utterances, where
necessary information is explicit and simple to extract (Zhang et al. 2020c). Conversely,
naturalconversationsnecessitateextractingimplicitinformationfromuserutterancestogenerate a response (Zhou et al. 2022). A few studies explore advanced attention mechanisms
(Quetal.2024),interactivelearning(Yangetal.2022)anddialogueaugmentation(Liuetal.
2022b)tocaptureimplicitcontextualinformationfromthetext.Exploringtheseareasfurther
maybeapromisingdirectionforfutureinvestigations.
3.2ClassificationTasks
Figure1showsthatdialogueclassificationencompassesadditionaltasks,includingintentdetection,slotfilling,dialoguestatetracking,andaffectdetection.Inthefollowingsections,weprovide
adetailedexplanationofeachofthesetasks.
Intent detection (ID). Identifying the user’s objectives in a conversation is crucial, particularly
in goal-oriented dialogues. Intent detection aims to achieve this objective by analyzing text and
inferring its intent, which can then be categorized into predefined groups. Given its importance,
there has been significant research into intent detection, with several datasets proposed for this
task, such as the DialoGLUE (Mehri et al. 2020) benchmark’s Banking77 (Casanueva et al.
2020), CLINC150 (Larson et al. 2019), HWU64 (Liu et al. 2021c), and the Schema Guided
Dialogue (SGD) Dataset (Rastogi et al. 2020). Table 1 illustrates the taxonomic characteristics
these datasets satisfy. It can be observed that they all follow a similar pattern of being goaloriented,domainspecific,andsingleturnwithnoexternalknowledgeassociatedwiththem.The
DialoGLUEleaderboardgindicatesthatamodelcalledSAPCE2.0givesexceptionalperformance
ghttps://eval.ai/web/challenges/challenge-page/708/leaderboard/1943

<!-- Page 12 -->

12 NaturalLanguageEngineering
across all intent detection tasks. In addition, other approaches include utilizing contrastive conversational finetuning (Vulic´ et al. 2022), dual sentence encoders (Casanueva et al. 2020), and
incorporatingcommonsenseknowledge(Siddiqueetal.2021).
Keychallenges.Theprimaryobstacleinintentdetectioninvolvesthetightdecisionboundary
ofthelearnedintentclasseswithinintentdetectionmodels(Weldetal.2022b).Furthermore,
giventhedynamicnatureoftheworld,thenumberandtypesofintentsareconstantlyevolving,makingitessentialforintentdetectionmodelstobedynamic(Weldetal.2022a).Recent
developments have explored ensemble learning (Zhou et al. 2023b) along with Bayesian
approaches (Zhang et al. 2019; Aftab et al. 2021) to mitigate the said challenge. Further,
learning paradigms such as incremental learning (Paul et al. 2022; Hrycyk et al. 2021) and
meta-learning(LiandZhang2021;Liuetal.2022d)alsoprovetobebeneficialinthisfield.
However,adetailedfutureinvestigationinthisdomainisneeded.
Slot Filling (SF). To effectively achieve a specific intent, a dialogue agent must possess all the
necessaryinformationrequiredfortaskcompletion.Thesecrucialpiecesofinformationarecommonlyreferredtoasslots.Itisworthnotingthatintentdetectionandslotfillingoftengohandin
hand.Asaresult,theSGDdatasetdescribedinSection3.2includesslotannotationsandcanserve
as a benchmark for evaluating slot-filling performance. Additionally, the Restaurant8k (Coope
etal.2020)datasetisanotherprominentdatasetinthedomainofslotfilling.Methodsthatsolve
the slot-filling task often involve using CNN (Lecun et al. 1998) and CRF (Ma and Hovy 2016;
Lampleetal.2016)layers.Coopeetal.(2020)givesimpressiveperformanceontheRestaurant8k
dataset by utilising the ConveRT (Henderson et al. 2020) method to obtain utterance representation. Many other studies explore the problem of slot filling as a stand-alone task (Louvan and
Magnini 2019 2018). However, plenty of work target it in a multitask fashion by making use of
Transformerbasedmethods(Mehrietal.2020),graphicalapproach(Wuetal.2023a),GRUs(Cho
etal.2014)andMLBfusionlayers(Bhasinetal.2020).
Keychallenges. Contemporary slot-filling techniques concentrate on slots as independent
entitiesandoverlooktheircorrelation(LouvanandMagnini2020).Furthermore,severalslots
includesimilarwordsintheirsurroundings,complicatingslot-fillingmethods’identification
of the correct slots (Weld et al. 2022a). In order to mitigate these challenges, a few studies
haveproposedtheuseofjointinference(Tangetal.2020),latentvariablemodels(Wuetal.
2019;Wakabayashietal.2022),andincorporatingexternalknowledge(Heetal.2021;Wang
etal.2019a).Exploringthesefurthercouldbepromisingfutureresearchdirections.
DialogueStateTracking(DST). Dialoguestatetrackinginvolvesidentifying,duringeachturnof
aconversation,thecompletedepictionoftheuser’sobjectivesatthatmomentinthedialogue.This
depiction may comprise of multiple entities such as a goal restriction, a collection of requested
slots,andtheuser’sdialogueact.ThemajordatabaseusedforbenchmarkingtheDSTtaskisthe
MultiWOZ2.1dataset(Ericetal.2020).TheTripPy+SaCLogmodel(Daietal.2021a)achieved
remarkable performance on this dataset. The model utilizes curriculum learning (CL) and efficiently leverages both the schema and curriculum structures for task-oriented dialogues. Some
methods also used generative objectives instead of standard classification ones to perform DST
(Lewisetal.2020;Pengetal.2021;Aghajanyanetal.2021).
Keychallenges.Similartointentdetection,dialoguestatescanalsoevolveovertime,necessitatingsystemswiththeabilitytoadapt(Fengetal.2022b).Whilesomestudieshaveexplored

<!-- Page 13 -->


### LATEXSupplement 13

zero-shotsettingsforlearningdialoguestates(Balaramanetal.2021),additionalresearchin
thisareacouldbeappreciated.
Affect Detection (AD). In order to fully grasp the user’s intention, it is crucial to uncover their
affectiveattributes,includingemotionsandsarcasm,andincorporatethemintotheagent’sreply.
The latest advancements in detecting affects have been made possible through the use of the
MELD (Poria et al. 2019), DailyDialogue (Li et al. 2017), MUStARD (Castro et al. 2019), and
Empathetic Dialogues (Rashkin et al. 2019) datasets for Emotion Recognition in Conversation
(ERC),sarcasmdetection,andempatheticresponsegeneration.Majoreffortstosolvethetaskof
ERCinvolvestheuseofTransformer-basedmodels(Songetal.2022;Huetal.2022;Zhaoetal.
2022),graphicalmethods(Ghosaletal.2019;Shenetal.2021),andcommonsenseincorporation
(Ghosaletal.2020).Forsarcasmdetectiontoo,Transformer-basedmethodsarethemostpopular
ones (Zhang et al. 2021; Babanejad et al. 2020; Desai et al. 2021; Bedi et al. 2021; Bharti et al.
2022).Empatheticresponsegenerationisoftenhandledbyusingsequence-to-sequenceencoderdecoderarchitecture(XieandPu2021;Shinetal.2019;Rashkinetal.2018).
Keychallenges.Althoughaffectdetectionremainsasacriticaltopic,merelyaccommodating
detectionmaynotsufficetogenerateappropriateresponses(Pereiraetal.2022).Introducing
explainability behind the detected affects can enable the model to leverage the instigators
andgeneratesuperiorresponses(Kumaretal.2022a).Manyrecentstudieshaveexploredthe
domain of explainability, especially in the terms of affects (Li et al. 2023; An et al. 2023;
Kumar et al. 2023b). Investigating the explainability aspect of affects further presents an
intriguingareaforfutureresearch.

## PretrainingObjectivesforDialogueAgents

Intheever-growinglandscapeofLargeLanguageModels(LLMs),whichhavegainedwidespread
popularity for their adeptness in acquiring knowledge through intelligent pretraining objectives,
it becomes crucial to identify the most optimal pretraining objective that elevates LLMs’ performance. Numerous pretraining objectives have been employed to pretrain LLMs, typically
relyingonstandalonetextslikenewsarticles,stories,andtweets.Thewidelyfavoredobjectives
encompass LanguageModeling (LM), MaskedLanguage Modeling (MLM),and Next Sentence
Prediction(NSP).Undeniablyeffectiveinenhancingmodelperformance,theseobjectives,however, lack insights tailored specifically to the domain of conversation. Incorporating standard
pretrainingobjectivesintodialogue-basedtrainingdatahasbeenacommonpractice,mainlydue
to their prevalence, yet little attention has been devoted to devising dialogue-specific objectives.
Thus,anotableresearchgapexistsinthisdomain.Below,wepresentasuccinctoverviewofsome
ofthemajorendeavorsundertakeninpursuitofaddressingthispressingneed.
Language modeling (LM) stands as the most common pretraining objective, serving as the
foundational framework for many advanced systems. By training the model to predict the next
wordortokeninasentencebasedonthecontextofprecedingwords,LMfacilitatestheacquisition
of a deep understanding of grammar, syntax, and semantic relationships within conversational
data.ProminentdialogueagentslikeGPT(Radfordetal.2018),Meena(Kulshreshthaetal.2020),
LaMDA (Thoppilan et al. 2022), and DialoGPT (Zhang et al. 2020b) have embraced the LM
objective as their primary pretraining approach, owing to its effectiveness in capturing language
patterns. However, it is crucial to acknowledge that this objective does not explicitly address
dialogue-specificnuances.
Moving towards dialogue-specific objectives, one can employ the response selection and
ranking methodology (He et al. 2022; Mehri et al. 2019; Shalyminov et al. 2020), in which the

<!-- Page 14 -->

14 NaturalLanguageEngineering
modelundergoestrainingtoprioritizeandrankagivensetofcandidateresponsesbasedontheir
appropriatenesswithrespecttoaninpututterance.Thisapproachempowersthemodeltoadeptly
discernthemostcontextuallysuitableresponsefromapoolofpotentialoptions,thusenhancing
itsconversationalabilities.Anotherwidelyrecognizedstrategyinvolvesutterancepermutation
within a dialogue (Zhang and Zhao 2021; Chen et al. 2022a; Weizenbaum 1966), granting the
LLM a valuable opportunity to efficiently grasp the nuances of the dialogue context. By rearranging the utterances, the model gains a deeper understanding of the conversational flow and
cansynthesizemorecoherentresponses.Akintoutterancepermutationistheutterancerewrite
objective,wherethemodelistrainedtoskillfullyparaphraseandrephraseinpututteranceswhile
preservingtheirunderlyingmeaning.Thisproficiencyequipsthemodeltoeffectivelyhandlevariations in user input and, in turn, generate a wide array of diverse and contextually appropriate
responses,fosteringamoreengaginganddynamicconversation.ParalleltoLanguageModeling,
the area of context-to-text generation has also garnered attention in the domain of dialoguespecific pretraining (Chapuis et al. 2020; Yu et al. 2021; Mehri et al. 2019). In this pursuit, the
model embarks on the task of producing a response, considering the context it receives, usually
presented as a sequence of dialogue history. The model’s training entails honing the ability to
produceseamlessandlogicallyconnectedresponsesthatseamlesslyintegratewiththegivencontext.Thisimperativeenablesthemodeltogenerateresponsesthatexhibitfluencyandcoherency,
thereby facilitating more compelling and authentic conversations. Moreover, the existing literatureindicatesanotableupswingintheadoptionofhybridmethodologies(Lietal.2022b;Zhang
and Zhao 2021; He et al. 2022; Mehri et al. 2019), wherein multiple pretraining objectives are
harmoniouslymergedtotargettheprincipalobjectiveoftheLLM.Acompellingexampleofthis
liesintheworkofXuandZhao(2021),whointroducedthreeinnovativepretrainingstrategiesinsertion,deletion,andreplacement-designedtoimbuedialogue-likefeaturesintoplaintext.
Throughtheutilizationofdialogue-specificpretrainingobjectives,languagemodelscaneffectively apprehend the nuances of conversational language, adeptly comprehend the contextual
backdrop in which utterances unfold, and consequently, fabricate responses that are not only
morenaturalandcontextuallyfittingbutalsocaptivatingandengaging.Nevertheless,theresponse
generationusingLLMsbringsitsownchallengeswhichweexploreinSection8.

## EvaluatingDialogueBasedSystems

Thelaststepforanydialogueagentistoevaluatethegeneratedresponsesquantitativelyorqualitatively. We can divide the evaluation strategies employed to assess a dialogue agent into three
types.
• AutomaticevaluationusesmetricslikeROUGE(Lin2004),andBLEU(Papinenietal.2002)
toevaluatetheresponsesyntacticallyviatheuseofn-gramoverlap,andmetricslikeMETEOR
(BanerjeeandLavie2005)andBERTscore(Zhangetal.2020a)tocapturesemanticsimilarity.
• Humanevaluationisvitaltocapturehumanconversationnuancesthatautomatedmetricsmay
miss. Annotators evaluate a portion of the test set and generate responses based on different
measures such as coherence, relevance, and fluency (van der Lee et al. 2021; Schuff et al.
2023). However, human evaluation can be expensive, time-consuming, and may not be easily
replicableh.Interactiveevaluationisgainingrelevanceasaresult.
• Interactive evaluation involves real-time interactions between human evaluators and the dialogue generation system being assessed (Christiano et al. 2017; Stiennon et al. 2020). As it
allowsforhumanjudgmentandnaturalevaluation,itisconsideredmorereliableandvalidthan
othermethods.
hhttps://reprohum.github.io/

<!-- Page 15 -->


### LATEXSupplement 15

Keychallenges. In evaluating the generative quality of dialogue responses, it is essential to
considerthedistinctivefeaturesthatsetthemapartfromstand-alonetext(Liuetal.2017a).
To this end, numerous studies in linguistics have examined the idiosyncrasies of dialogue,
with Gricean Maxim’s Cooperative principle (Grice 1975 1989) being a prominent theory.
TheCooperativeprincipleoutlineshowindividualsengageineffectivecommunicationduringtypicalsocialinteractionsandiscomprisedoffourmaximsofconversation,knownasthe
Griceanmaxims-quantity,quality,relation,andmanner.Whilehumanevaluatorstypically
considergeneralcharacteristics,wefeelthatincorporatingattributesbasedonthesemaxims
isequallycrucialforevaluatingdialogueresponsesandcanbeexploredinfuturestudies.

## UNIT: UNifiedDIalogueDataseT

ConversationalAIinvolvesseveraltasksthatcapturevariouscharacteristicsofadialogueagent.
However,thecurrentstateofconversationalAIisdisintegrated,withdifferentdatasetsandmethods being utilized to handle distinct tasks and features. This fragmentation, coupled with the
diversedataformatsandtypes,presentsasignificantchallengeincreatingaunifiedconversation
model that can effectively capture all dialogue attributes. To address this challenge, we propose
the UNIT dataset, a unified dialogue dataset comprising approximately four million conversations.Thisdatasetiscreatedbyamalgamatingchatsfromthefragmentedviewofconversational
AI. Specifically, we consider the 39 datasets listed in Table 1 and extract natural language conversations from each of them. Each dataset contained conversations in a different format, often
presentednon-trivially.Wecreatedseparatescriptstoextractdialoguesfromeachdatasetsothat
other researchers can utilise the complete data as a whole. An overview of how UNIT is constructed can be found in Figure 3. UNIT is designed to provide a comprehensive and unified
resource for conversational AI research. It will enable researchers to access a vast collection of
diverseconversationsthatencompassvariousdialoguecharacteristics.Webelievethisdatasetwill
facilitatethedevelopmentofmorerobustandeffectiveconversationalAImodelsthatcanhandle
abroadrangeoftasksandfeatures.WesummarizethestatisticsofUNITinTable2andshowthe
distributionofspeakersandutterancesinFigure4.Figure5illustratesthedatasetsizedistribution
inUNIT.

## Dr Ds D2S Qa


## Unit

Standardize
format

## Kgr Cc Tod Id


## Sf Dst Ad


## Gpt2U Gpt2

Figure3:All39datasetsfromdistincttasksarestandardisedandcombinedintoasingleconversationaldatasetcalledUNIT.UNITisthenusedtofurtherpretrainGPT2withtheintentofcapturing
nuancesofalltasks.
6.1 UNITforFoundationModelTraining
To investigate whether UNIT can serve as a suitable datset for a dialogue foundation model, we
usefollowingsixmajoropenfoundationmodels.

<!-- Page 16 -->

16 NaturalLanguageEngineering
# Dlgs #Utts #Tokens
4,843,508 39,260,330 441,051,948
Table 2. : Statistics of the UNIT dataset: UNified DIalogue DataseT.
Abbreviations:Dlgs:Dialogues,Utts:Utterances.
106
105
104
103
102
10
1
1 10 100
# Speakers
ycneuqerF
106
105
104
103
102
101
1
1 10 100 1000
# Utterances
ycneuqerF
Figure4: Log-log distribution of the number of speakers and number of utterances per dialogue
inUNIT.Maximumnumberofdialoguescontain2(10)speakers(utterances)whilethemaximum
numberofspeakers(utterances)inadialogueare260(527).

### Ubuntu Dialogue Corpus SODA ConvAI3: ClariQ

bAbI ProsocialDialog MetaLWOz Empathetic Dialogues PersonaChat SAMSum Corpus

### OpenDialKG DialoGLUE- HWU64 mDIA DialoGLUE- MultiWOZ 2.1

DialoGLUE- Banking77 DialogSum FusedChat Mutual DialoGLUE- DSTC8 SGD CoQA

### DialoGLUE- TOP


### DailyDialogue ABCD CraiglistBargains Doc2Dial CMU DoG

DialoGLUE- CLINC150 DialoGLUE- Restaurant8k SPIDER F C a A it N h A D R ia D l B O i T T T O er D s MSwitcEhbLoarDd-1 Co MD S eUlSi Q DtAaRt L aD

### Loading [MathJax]/extensions/MathMenu.js

Figure 5: Distribution of sizes of different datasets in UNIT. Biggest four datasets are Ubuntu
DialogueCorpus,SODA,ConvAI3:ClariQ,andBAbIfollowedbycomparitivelysmallerdatasets.
(1) GPT-2(Radfordetal.2019):GPT-2isalanguagemodelbasedonTransformersandhas1.5
billion parameters. It was trained on a vast dataset consisting of 8 million web pages on the
languagemodellingobjective.Duetotheimmensevarietyofdatathatwasfedintothemodel,
thissimpleobjectiveresultsinthemodeldemonstratingtheabilitytoperformnumeroustasks
acrossvariousdomains,allofwhicharefoundnaturallywithinthetrainingdata.
(2) FLAN-T5 (Chung et al. 2022): FLAN T5 scales T5 (Raffel et al. 2020) and investigates
the application of instruction finetuning to enhance performance, with a specific emphasis
onscalingthenumberoftasksandmodelsize.Throughitsinstructionfinetuningparadigm,
thismodeldemonstratesimprovedperformanceacrossarangeofmodelclasses,setups,and
evaluationbenchmarks.
(3) BLOOM(Scaoetal.2022):BLOOMisalanguagemodelwith176billionparameters.This
open-access model is built on a decoder-only Transformer architecture and was specifically
designed to excel in natural language processing tasks. The model was trained using the

<!-- Page 17 -->

LATEXSupplement 17

### Generative


### Classification

Model Transformative DialogueResponse

### Dr Ds D2S Qa Kgr Cc Tod Id Sf Dst Ad

CANARD SAMSum TOP ClariQ Doc2Dial PersonaChat ABCD CLINC150 Restaurant8k MultiWOZ2.1 MUStARD
GPT2 90.15 51.33 64.68 49.13 39.9 40.13 51.03 93.33 30.3 51.01 52.17
FLAN-T5 88.64 49.97 63.81 47.98 38.98 41.76 51.95 85.61 30.16 51.86 49.11
BLOOM 86.66 47.12 59.26 45.11 39.13 39.82 50.31 84.44 25.56 50.33 56.52
DialoGPT 79.1 41.6 59.65 41.88 35.11 36.88 47.64 92.23 15.62 47.75 44.92
BlenderBot 81.39 44.82 60.11 44.39 36.64 38.05 48.29 88.13 17.29 47.39 45.67
GPT-2U 91.53 52.79 66.34 51.22 40.6 42.65 52.16 94.91 31.26 52.75 71.01
Table 3. : Experimental results for representative datasets on the 11 dialogue-specific tasks. The
metric used for generation is ROUGE-1 whereas classification is evaluated for accuracy. For
abbreviations,pleaserefertoTable1.
ROOTScorpus(Laurençonetal.2022),whichincludeshundredsofsourcesacross46natural
languagesand13programminglanguages.
(4) DialoGPT (Zhang et al. 2020b): DialoGPT is a neural conversational response generation
model trained on social media data consisting of 147 million conversation-like exchanges
extracted from Reddit comment chains spanning over a period from 2005 through 2017.
Leveraging this dataset, DialoGPT employs a Transformer model that has been specifically
extended to deliver exceptional performance, achieving results that are remarkably close to
humanperformanceinbothautomaticandhumanevaluationsofsingle-turndialoguesettings.
(5) BlenderBot (Roller et al. 2021): BlenderBot is a conversational AI model that adopts a
uniqueapproachtotraining,eschewingthetraditionalemphasisonmodelsizeanddatascaling in favor of a more nuanced focus on conversation-specific characteristics. Specifically,
BlenderBot is designed to provide engaging responses that showcase knowledge, empathy,
andaconsistentpersona,allofwhicharecriticaltomaintainingahighlevelofengagement
withusers.Toachievethisgoal,thedevelopersofBlenderBothavecuratedtheirowndataset
consistingofconversationsthatexhibitthesedesiredattributes.
6.1.1ExperimentalSetup
In Section 3, we outlined 11 distinct tasks specific to dialogue. This study endeavors to lay the
foundation for harnessing datasets encompassing diverse dialogue characteristics, with the ultimategoaloftrainingaunifieddialogueagentcapableofaddressingmultipletaskssimultaneously.
In pursuit of this objective, rather than subjecting models to assessments across all datasets, we
optforajudiciousapproach.Weselectarepresentativedatasetfromeachtask,intendingtoilluminatethetrendsexhibitedbyvariousLLMsinaddressingthesediversetasks. Initially,weevaluate
the existing foundation models on the selected datasets and present our results in Table 3. It is
importanttohighlightthatourapproachinvolvesutilizingthepre-trainediterationofGPT-2and
subsequentlysubjectingitto‘furtherpre-training’viathecausalLMobjectiveon UNIT toyield
the final model, GPT-2U. Subsequent to this, when evaluating the models – including GPT-2U
andothers–acrossvarioustasks,wefine-tunethesemodelsspecificallyforeachtask.Thisfinetuningprocessincludestheincorporationoftailoredlinearlayerstoadjusttheoutputtothedesired
dimensions.Forinstance,inthecaseofabinaryclassificationtask,alinearlayerwithtwoneurons
is added to the output layer to suit the task’s requirements. In order to keep our results concise,
wementiontheROUGE-1scoresinthetabletocapturethegeneralcapabilityofthemodelsand
theperformancetrend,which,therestofthemetricsalsofollow.ItisevidentthatGPT-2performs
better than the other systems for the majority of the tasks. Therefore, we further pretrain GPT-2
usingUNITtogetGPT-2U.Theresultantmodelisthenevaluatedonthesamebenchmarksasthe

<!-- Page 18 -->

18 NaturalLanguageEngineering

## Dr Ds D2S Qa Kgr Cc Tod


### Model

Flu Rel Coh Flu Rel Coh Flu Rel Coh Flu Rel Coh Flu Rel Coh Flu Rel Coh Flu Rel Coh
GPT2 3.6 3.4 3.8 2.6 2.5 2.9 3.4 3.1 2.7 2.1 2.5 2.1 2.3 2.1 2.1 2.2 2.3 2.1 2.7 2.6 2.4
GPT-2U 3.9 3.8 4.1 3.1 2.9 3.2 3.6 3.5 3.1 2.4 2.6 2.3 2.8 2.5 2.4 2.6 2.7 2.4 3.1 2.9 2.7
Table4.:Resultsofhumanevaluationfortherepresentativetasks.
otherfoundationmodels;thelastrowofTable3showsitsperformance.GPT-2U outperformsall
existing foundation models including GPT-2 for almost all dialogue-specific task. The increase
inperformancecorroboratesourhypothesisthattheunifieddatasetefficientlycapturesallmajor
characteristicsofadialogue.
6.1.2QualitativeAnalysis
While the results for the classification tasks are straightforward, we conduct a detailed analysis
of the generative outcomes in this section. Recognizing the limitations of automatic metrics in
fully capturing the performance of a generative system, as discussed in Section 5, we undertake
a human evaluation of predictions generated by the top comparative system, GPT-2 and GPT-
2U. A panel of 25 human evaluatorsi, proficient in English linguistics and aged between 25−
30, are enlisted for this task. Their assignment involves assessing a randomly chosen set of 20
predictions from each task generated by these methods. The evaluators assign ratings ranging
from1to5,consideringkeyhumanevaluationmetricssuchasfluency,relevance,andcoherence.

### Thedimensionsofevaluationareexplainedasfollows:

• Fluencyevaluatesthenaturalnessandreadabilityofthegeneratedtext,focusingongrammar, syntax, and language flow. Higher scores indicate smoother and more linguistically
proficienttext.
• Relevance measures how effectively the generated text aligns with the given context or
prompt, evaluating the appropriateness of content in relation to the context. Higher scores
signifyastrongeralignmentbetweentheresponseandthecontext.
• Coherenceevaluationpertainstothelogicalflowandsemanticconnectionofideaswithin
the generated text, ensuring that the information is well-structured, logically connected,
andreadilycomprehensible.Higherscoresreflectamorecoherentandlogicallystructured
response.
Table 4 presents the average ratings across all obtained responses. The results indicate a
preferenceforGPT-2U byourannotatorsacrossallmetrics,highlightingitssuperiority.

## MajorTakeaways:ASummary

Thissectionextensivelyhighlightsthenotablerevelationsacquiredfromathoroughexamination
ofopen-sourcedialoguedatasets,tasks,andmethodologies.Thesevaluableinsightsaresystematicallydelineatedwithinthreekeysections:DialogueTasks,UtilizationsofDialogueAgents,and
CharacteristicsofDatasets.
Dialogue tasks. Within the confines of this comprehensive survey, we have delved into a discourseencompassingthe mostprevalentand versatile dialoguetasks,capturing thefundamental
iThehumanevaluatorswererecruitedthroughinvitationssenttoprofessionalswithafairknowledgeofthesubjectarea.
Theywerecompensatedfortheirtimeandeffortbystandardindustrynorms.Throughouttheevaluationprocess,carewas
takentoensureallparticipants’comfortandfairtreatment,includingclearcommunicationofexpectationsandtheopportunity
forfeedback.

<!-- Page 19 -->


### LATEXSupplement 19

characteristics that define effective conversational systems. Nonetheless, with the easy accessibility of resources, there has been a proliferation of novel dialogue tasks concentrating on niche
domains in the realm of dialogue systems, with a specific focus on explainability. An example
of this evolution can be found in the work of Ghosal et al. (2021), who have ventured into the
realm of the dialogue explanation task. Their exploration is characterized by a tripartite framework,consistingofdialogue-levelnaturallanguageinference,spanextraction,andtheintricacies
ofmulti-choicespanselection.Throughthesedesignedsubtasks,wecanunraveltheinterdependentrelationshipswithindialogues.Whiletheinitialtaskunveilstheimplicitconnectionsamong
various entities within the dialogue, the subsequent two subtasks are tailored to identify entities
in light of the established relational context between the two. Research in the domain of affect
explainabilityisalsoontherise.Forinstance,Emotioncauseextractioninconversations(Xiaand
Ding2019;Poriaetal.2021)aimstoextractaspanfromaninpututterancewhichisresponsible
totheemotionelicitedbythespeakerinthatutterance.Similarly,emotionflipreasoning(Kumar
et al. 2022c 2023a) tries to uncover the responsible utterances from a dialogue context that are
responsibleforaspeaker’semotionshift.Apartfromemotions,sarcasmexplanation(Kumaretal.
2022ab)isalsoarecenttaskthathascomeintofocus.Itdealswithgeneratinganaturallanguage
explanationofthesarcasmpresentinadialogue.
Dialogue agent applications. Beyond the realm of novel tasks that have been introduced to
enhance the capabilities of conversational agents, the scope of dialogue agents has dramatically
expanded,encompassingaplethoraofemergingdomains.Anotableillustrationofthisevolving
landscape is evident in the realm of mental health, where recent strides have propelled dialogue
agentsintoapivotalrole(Campillos-Llanosetal.2020;Srivastavaetal.20222023).Thisdynamic
transformation underscores the profound versatility that dialogue agents bring to the table. Yet,
the influence of dialogue agents is not confined solely to mental health; they have also forged
an impactful presence in diverse domains such as education (Wang et al. 2023a; Baker et al.
2023),storytelling(Gaoetal.2023;Sunetal.2022a),languageacquisition(BearandChen2023;
Ericssonetal.2023),andcompanionship(Leo-Liu2023;Shikhaetal.2022).
Dataset attributes. Within the scope of this comprehensive survey, our efforts revolve around
acquiring the prominent tasks along with their open-source datasets. Notably, these datasets
exhibitacertainlackofuniformityincapturingthefullspectrumofattributesinherenttoarobust
dialogue agent (c.f. Table 1). This phenomenon is illustrated in Figure 6, which highlights the
datasetdistributionwithin UNIT sheddinglightontheprevalenceofspecificdialogueattributes.
Upon observing this distribution, a discernible pattern emerges, highlighting the nascent stage
of multimodality integration within mainstream dialogue tasks. An active focus towards bringing multimodality to the dialogue domain can profoundly influence the capabilities of dialogue
agents.AnotherinterestingtrendthatcanbeobservedfromFigure6isthepredominanceofmultiturndatasetsandlongtextualoutputs.Whilethisemergingtrendservestohighlightthepresent
direction in the design of dialogue datasets, a judicious examination of the existing distribution
underscoresacompellingnecessity:theneedtocurateamorediverserangeofdialoguedatasets.
These datasets should encompass structured knowledge or facilitate the generation of responses
imbued with empathy. The meticulous expansion in this curated direction would undeniably
enhancethelandscapeoftrainingandapplicationfordialogueagents.

## ConclusionsandFutureResearch

This survey outlined the essential traits that a dialogue agent should possess through a comprehensive taxonomy. Major dialogue-specific tasks and their respective open-domain datasets and
techniqueswereprovidedtoenabletheintegrationofthesetraits.Toenhanceefficiencyandtask
correlation,aunifieddatasetofextractedconversationswasproposed.Weevaluatedtheresultsof
experimentsconductedusingestablishedfoundationalmodelsandpresentedaconciseevaluation.

<!-- Page 20 -->

20 NaturalLanguageEngineering
cc-gu-mi-pi cg-gu-mi-pi o-d-mi-pi ps-d-mi-pi ts-c-mi-pi tm-c-mi-pi u-m-xe-pi m-m-xe-pi n-k-xe-pi u-k-xe-pi s-k-xe-pi cc-t-mi-po cg-t-mi-po e-s-mi-po fni-s-mi-po ni-s-mi-po me-s-mi-po u-m-xe-po m-m-xe-po ts-s-xe-po tl-s-xe-po rts-s-xe-po
40
35
30
25
20
15
10
5
0
Dialogue Agent Attribute
stesataD
fo
rebmuN
Figure 6: Distribution of datasets covering the specific dialogue attributes. Abbreviations
– ip-im-ug-cc: input-implicit-user goals-chit chat, ip-im-ug-gc: input-implicit-user goal-goal
completion, ip-im-d-o: input-implicit-domain-open, ip-im-d-sp: input-implicit-domain=specific,
ip-im-c-st: input-implicit-context-single turn, ip-im-c-mt: input-implicit-context-multi turn, ipex-m-u: input-explicit-modality-unimodal, ip-ex-m-m: input-explicit-modality-multimodal, ipex-k-n: input-explicit-knowledge-none, ip-ex-k-u: input-explicit-knowledge-unstructured, ip-exk-s: input-explicit-knowledge-structured, op-im-t-cc: output-implicit-type-chit chat, op-im-tgc: output-implicit-type-goal completion, op-im-s-e: output-implicit-style-engaging, op-im-sinf: output-implicit-style-informative, op-im-s-in: output-implicit-style-instructional, op-im-sem:output-implicit-style-empathetic,op-ex-m-u:output-explicit-modality-unimodal,op-ex-m-m:
output-explicit-modality-multimodal, op-ex-s-st: output-explicit-structure-short text, op-ex-s-lt:
output-explicit-structure-longtext,op-ex-s-str:output-explicit-structure-structural.
AlthoughtheUNITpretrainedmodeloutperformsexistingmodels,therearestillmanychallenges
that need to be addressed. Furthermore, recent advancements such as LaMDA (Thoppilan et al.
2022), ChatGPTj, Sparrow (Glaese et al. 2022), Baize (Xu et al. 2023), and LLaMA (Touvron
etal.2023)areeffortstowardsbuildingfoundationmodelscapableofperformingmultipletasks.
While models like ChatGPT are a breakthrough in NLP, the research in conversational AI is far
fromcompletewithfollowingkeychallenges.WedwellontheremainingchallengesinNLPthat
needattentionforfurtherresearch.
Hallucincations, Veracity, and Correctness. Large language model based systems are notorious for hallucinations and producing incorrect output. Further, the paradigm of Reinforcement
Learning from Human Feedback (RLHF) (Christiano et al. 2017; Stiennon et al. 2020), that has
led to greater accuracy of models like ChatGPT also leads to verbose and ambiguous responses
asagentspreferlengthyandloquaciousresponses.Toimprovetheperformanceofgoal-oriented
dialogues,futureresearchshouldprioritizethedevelopmentofmethodsthatreducehallucination
andproduceaccurate,conciseresponses.
jhttps://openai.com/blog/chatgpt

<!-- Page 21 -->


### LATEXSupplement 21

Ability for Logical Reasoning. Popular models often struggle to answer queries that involve
spatial, temporal, physical, or psychological reasoning (Borji 2023). For example, if we ask
ChatGPT a question such as “The trophy didn’t fit in the suitcase; it was too small. What was
too small?" (Levesque et al. 2012), it may erroneously identify the trophy as being too small.
However, reasoning capabilities such as these are essential for dialogue agents to fulfill user
requestseffectively.
AffectUnderstanding. Failuretointerpretemotions,humourandsarcasmnuances(Kocon´ etal.
2023)canleadtoinadequateresponsesinchit-chatconversationsisaneedforfurtherinvestigation
intothedevelopmentofmodelsthatcanbetterhandletheselinguisticfeatures.
Bias. LLMs learn from vast datasets, making them susceptible to biases (Luo et al. 2023). For
instance,ifthemodelisaskedtocomplete“TheLatinomanworkedasa...”prompt,itmaysuggest
professions like construction worker or nurse. Yet, when prompted with “The Caucasian man
workedasa...”,themodelsuggestsasoftwaredeveloperordoctor.
Other challenges. Significant challenges, such as the inability of models to trace the source
of generated responses (attribution), demand for extensive computing resources that damage
the environmentk, NLP research being proprietary and focused on the English language. These
challengesneedconsiderationinfutureNLPresearch.
Ethicalconsiderations. Thedeploymentofdialogueagents,poweredbyadvancedartificialintelligence and natural language processing, raises significant ethical concerns in various domains
(Artstein and Silver 2016; Henderson et al. 2018). One major ethical issue is the potential for
biasedbehavior,wheredialogueagentsmayinadvertentlyperpetuateoramplifyexistingsocietal
biasespresentintheirtrainingdata(Lucasetal.2018).Transparencyandaccountabilityarealso
critical concerns, as users often lack visibility into the decision-making processes of these systems(Hepenstaletal.2019).Additionally,issuesrelatedtouserprivacyanddatasecurityemerge,
asdialogueagentsmayhandlesensitiveinformationduringinteractions(Srivastavaetal.2022).
Striking the right balance between personalization and intrusion poses another ethical dilemma
(Zhangetal.2018).Ensuringthatdialogueagentsrespectculturalsensitivitiesandadheretoethicalstandardsincontentgenerationisessentialforfosteringpositiveandresponsibleinteractions.
Ethicalconsiderationssurroundingtheresponsibledevelopment,deployment,andmonitoringof
dialogue agents are vital to build trust and safeguard users from potential harm in the evolving
landscapeofconversationalAI.

### References

HarisAftab,VibhuGautam,RichardHawkins,RobAlexander,andIbrahimHabli.2021.Robustintentclassificationusing
BayesianLSTMforclinicalconversationalagents(CAs).InInternationalConferenceonWirelessMobileCommunication
andHealthcare.Springer,106–118.
ArmenAghajanyan,AnchitGupta,AkshatShrivastava,XilunChen,LukeZettlemoyer,andSonalGupta.2021.Muppet:
MassiveMulti-taskRepresentationswithPre-Finetuning.InProceedingsofthe2021ConferenceonEmpiricalMethodsin
NaturalLanguageProcessing.AssociationforComputationalLinguistics,OnlineandPuntaCana,DominicanRepublic,
5799–5811. https://doi.org/10.18653/v1/2021.emnlp-main.468
MohammadAliannejadi,JuliaKiseleva,AleksandrChuklin,JeffDalton,andMikhailBurtsev.2020.ConvAI3:Generating
clarifyingquestionsforopen-domaindialoguesystems(ClariQ).arXivpreprintarXiv:2009.11352(2020).
Jiaming An, Zixiang Ding, Ke Li, and Rui Xia. 2023. Global-View and Speaker-Aware Emotion Cause Extraction in
Conversations.IEEE/ACMTransactionsonAudio,Speech,andLanguageProcessing31(2023),3814–3823. https:
//doi.org/10.1109/TASLP.2023.3319990
Jacob Andreas, John Bufe, David Burkett, Charles Chen, Josh Clausman, Jean Crawford, Kate Crim, Jordan DeLoach,
Leah Dorner, Jason Eisner, et al. 2020. Task-oriented dialogue as dataflow synthesis. Transactions of the Association
forComputationalLinguistics8(2020),556–571.
Ron Artstein and Kenneth Silver. 2016. Ethics for a combined human-machine dialogue agent. In 2016 AAAI Spring
SymposiumSeries.
khttps://www.technologyreview.com/2022/11/14/1063192/were-getting-a-better-idea-of-ais-true-carbon-footprint/

<!-- Page 22 -->

22 NaturalLanguageEngineering
Yash Kumar Atri, Shraman Pramanick, Vikram Goyal, and Tanmoy Chakraborty. 2021. See, Hear, Read: Leveraging
MultimodalitywithGuidedAttentionforAbstractiveTextSummarization.Know.-BasedSyst.227,C(sep2021),14pages.
https://doi.org/10.1016/j.knosys.2021.107152
Nastaran Babanejad, Heidar Davoudi, Aijun An, and Manos Papagelis. 2020. Affective and Contextual Embedding for
SarcasmDetection.InInternationalConferenceonComputationalLinguistics.
Bernadette Baker, Kathy A Mills, Peter McDonald, and Liang Wang. 2023. AI, Concepts of Intelligence, and Chatbots:
The “Figure of Man,” the Rise of Emotion, and Future Visions of Education. Teachers College Record (2023),
01614681231191291.
VevakeBalaraman,SeyedmostafaSheikhalishahi,andBernardoMagnini.2021.RecentNeuralMethodsonDialogueState
Tracking for Task-Oriented Dialogue Systems: A Survey. In Proceedings of the 22nd Annual Meeting of the Special
InterestGrouponDiscourseandDialogue.AssociationforComputationalLinguistics,SingaporeandOnline,239–251.
https://aclanthology.org/2021.sigdial-1.25
SatanjeevBanerjeeandAlonLavie.2005.METEOR:AnAutomaticMetricforMTEvaluationwithImprovedCorrelation
withHumanJudgments.InProceedingsoftheACLWorkshoponIntrinsicandExtrinsicEvaluationMeasuresforMachine
Translationand/orSummarization.AssociationforComputationalLinguistics,AnnArbor,Michigan,65–72. https:
//aclanthology.org/W05-0909
Samuel Bayer, Christine Doran, and Bryan George. 2001. Dialogue Interaction with the DARPA Communicator
Infrastructure:TheDevelopmentofUsefulSoftware.InProceedingsoftheFirstInternationalConferenceonHuman
LanguageTechnologyResearch. https://aclanthology.org/H01-1017
ElizabethBearandXiaobinChen.2023.EvaluatingaConversationalAgentforSecondLanguageLearningAlignedwiththe
SchoolCurriculum.InInternationalConferenceonArtificialIntelligenceinEducation.Springer,142–147.
ManjotBedi,ShivaniKumar,MdShadAkhtar,andTanmoyChakraborty.2021.Multi-modalSarcasmDetectionandHumor
ClassificationinCode-mixedConversations.IEEETransactionsonAffectiveComputing(2021),1–1. https://doi.
org/10.1109/TAFFC.2021.3083522
Mordechai Ben-Ari and Francesco Mondada. 2018. Finite State Machines. 55–61. https://doi.org/10.1007/
978-3-319-62533-1_4
JonathanBerantandPercyLiang.2014.SemanticParsingviaParaphrasing.InProceedingsofthe52ndAnnualMeeting
oftheAssociationforComputationalLinguistics(Volume1:LongPapers).AssociationforComputationalLinguistics,
Baltimore,Maryland,1415–1425. https://doi.org/10.3115/v1/P14-1133
Santosh Kumar Bharti, Rajeev Kumar Gupta, Prashant Kumar Shukla, Wesam Atef Hatamleh, Hussam Tarazi, and
StephenJeswindeNuagah.2022.MultimodalSarcasmDetection:ADeepLearningApproach.WirelessCommunications
andMobileComputing(2022).
AnmolBhasin,BharatramNatarajan,GauravMathur,andHimanshuMangla.2020.ParallelIntentandSlotPredictionusing
MLBFusion.In2020IEEE14thInternationalConferenceonSemanticComputing(ICSC).217–220. https://doi.
org/10.1109/ICSC.2020.00045
AntoineBordes,NicolasUsunier,SumitChopra,andJasonWeston.2015.Large-scaleSimpleQuestionAnsweringwith

### MemoryNetworks.arXiv:1506.02075[cs.LG]

AliBorji.2023.ACategoricalArchiveofChatGPTFailures.arXiv:2302.03494[cs.CL]
Adi Botea, Christian Muise, Shubham Agarwal, Oznur Alkan, Ondrej Bajgar, Elizabeth Daly, Akihiro Kishimoto, Luis
Lastras, Radu Marinescu, Josef Ondrej, Pablo Pedemonte, and Miroslav Vodolan. 2019. Generating Dialogue Agents
viaAutomatedPlanning.arXiv:1902.00771[cs.AI]
PawełBudzianowski,Tsung-HsienWen,Bo-HsiangTseng,IñigoCasanueva,StefanUltes,OsmanRamadan,andMilica
Gašic´.2018.MultiWOZ-ALarge-ScaleMulti-DomainWizard-of-OzDatasetforTask-OrientedDialogueModelling.
In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing. Association for
ComputationalLinguistics,Brussels,Belgium,5016–5026. https://doi.org/10.18653/v1/D18-1547
DengCai,YanWang,WeiBi,ZhaopengTu,XiaojiangLiu,andShumingShi.2019.Retrieval-guideddialogueresponse
generationviaamatching-to-generationframework.InProceedingsofthe2019ConferenceonEmpiricalMethodsin
Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-

## Ijcnlp).1866–1875.

HengyiCai,HongshenChen,YonghaoSong,ZhuoyeDing,YongjunBao,WeipengYan,andXiaofangZhao.2020.Groupwisecontrastivelearningforneuraldialoguegeneration.arXivpreprintarXiv:2009.07543(2020).
LeonardoCampillos-Llanos,CatherineThomas,ÉricBilinski,PierreZweigenbaum,andSophieRosset.2020.Designing
a virtual patient dialogue system based on terminology-rich resources: Challenges and evaluation. Natural Language
Engineering26,2(2020),183–220. https://doi.org/10.1017/S1351324919000329
IñigoCasanueva,TadasTemcˇinas,DanielaGerz,MatthewHenderson,andIvanVulic´.2020.EfficientIntentDetectionwith
DualSentenceEncoders.InProceedingsofthe2ndWorkshoponNaturalLanguageProcessingforConversationalAI.
AssociationforComputationalLinguistics,Online,38–45. https://doi.org/10.18653/v1/2020.nlp4convai-1.5
SantiagoCastro,DevamanyuHazarika,VerónicaPérez-Rosas,RogerZimmermann,RadaMihalcea,andSoujanyaPoria.

### TowardsMultimodalSarcasmDetection(An_Obviously_PerfectPaper).InProceedingsofthe57thAnnualMeeting


<!-- Page 23 -->


### LATEXSupplement 23

oftheAssociationforComputationalLinguistics.AssociationforComputationalLinguistics,Florence,Italy,4619–4629.
https://doi.org/10.18653/v1/P19-1455
Emile Chapuis, Pierre Colombo, Matteo Manica, Matthieu Labeau, and Chloé Clavel. 2020. Hierarchical Pre-training
for Sequence Labelling in Spoken Dialog. In Findings of the Association for Computational Linguistics: EMNLP

## Association for Computational Linguistics, Online, 2636–2648. https://doi.org/10.18653/v1/2020.

findings-emnlp.239
KushalChawla,GaleM.Lucas,J.Gratch,andJonathanMay.2020.BERTinNegotiations:EarlyPredictionofBuyer-Seller
NegotiationOutcomes.ArXivabs/2004.02363(2020).
DerekChen,HowardChen,YiYang,AlexanderLin,andZhouYu.2021a.Action-BasedConversationsDataset:ACorpusfor
BuildingMoreIn-DepthTask-OrientedDialogueSystems.InProceedingsofthe2021ConferenceoftheNorthAmerican
ChapteroftheAssociationforComputationalLinguistics:HumanLanguageTechnologies.AssociationforComputational
Linguistics,Online,3002–3017. https://doi.org/10.18653/v1/2021.naacl-main.239
HongshenChen,XiaoruiLiu,DaweiYin,andJiliangTang.2017a.ASurveyonDialogueSystems:RecentAdvancesand
NewFrontiers.SIGKDDExplor.Newsl.19,2(nov2017),25–35. https://doi.org/10.1145/3166054.3166058
HongshenChen,XiaoruiLiu,DaweiYin,andJiliangTang.2017b.Asurveyondialoguesystems:Recentadvancesandnew
frontiers.AcmSigkddExplorationsNewsletter19,2(2017),25–35.
Jiaao Chen, Mohan Dodda, and Diyi Yang. 2023. Human-in-the-loop Abstractive Dialogue Summarization. In Findings
oftheAssociationforComputationalLinguistics:ACL2023,AnnaRogers,JordanBoyd-Graber,andNaoakiOkazaki
(Eds.).AssociationforComputationalLinguistics,Toronto,Canada,9176–9190. https://doi.org/10.18653/v1/
2023.findings-acl.584
JiaaoChenandDiyiYang.2020.Multi-ViewSequence-to-SequenceModelswithConversationalStructureforAbstractive
DialogueSummarization.InProceedingsofthe2020ConferenceonEmpiricalMethodsinNaturalLanguageProcessing
(EMNLP).AssociationforComputationalLinguistics,Online,4106–4118. https://doi.org/10.18653/v1/2020.
emnlp-main.336
YulongChen,YangLiu,LiangChen,andYueZhang.2021b.DialogSum:AReal-LifeScenarioDialogueSummarization
Dataset.InFindingsoftheAssociationforComputationalLinguistics:ACL-IJCNLP2021.AssociationforComputational
Linguistics,Online,5062–5074. https://doi.org/10.18653/v1/2021.findings-acl.449
ZhiChen,JijiaBao,LuChen,YuncongLiu,DaMa,BeiChen,MengyueWu,SuZhu,XinDong,FujiangGe,QingliangMiao,
Jian-GuangLou,andKaiYu.2022a.DFM:DialogueFoundationModelforUniversalLarge-ScaleDialogue-OrientedTask

### Learning.arXiv:2205.12662[cs.CL]

Zhiyu Chen, Jie Zhao, Anjie Fang, Besnik Fetahu, Oleg Rokhlenko, and Shervin Malmasi. 2022b. Reinforced Question
Rewriting for Conversational Question Answering. In Proceedings of the 2022 Conference on Empirical Methods in
NaturalLanguageProcessing:IndustryTrack.AssociationforComputationalLinguistics,AbuDhabi,UAE,357–370.
https://aclanthology.org/2022.emnlp-industry.36
KyunghyunCho,BartvanMerriënboer,CaglarGulcehre,DzmitryBahdanau,FethiBougares,HolgerSchwenk,andYoshua
Bengio. 2014. Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation. In
Proceedingsofthe2014ConferenceonEmpiricalMethodsinNaturalLanguageProcessing(EMNLP).Associationfor
ComputationalLinguistics,Doha,Qatar,1724–1734. https://doi.org/10.3115/v1/D14-1179
Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. 2017. Deep
Reinforcement Learning from Human Preferences. In Advances in Neural Information Processing Systems,
I. Guyon, U. Von Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett (Eds.),
Vol. 30. Curran Associates, Inc. https://proceedings.neurips.cc/paper_files/paper/2017/file/
d5e2c0adad503c91f91df240d0cd4e49-Paper.pdf
PhilippChristmann,RishirajSahaRoy,andGerhardWeikum.2022.Conversationalquestionansweringonheterogeneous
sources.InProceedingsofthe45thInternationalACMSIGIRConferenceonResearchandDevelopmentinInformation
Retrieval.144–154.
JenniferChu-CarrollandSandraCarberry.1998.Collaborativeresponsegenerationinplanningdialogues.Computational
Linguistics24,3(1998),355–400.
HyungWonChung,LeHou,ShayneLongpre,BarretZoph,YiTay,WilliamFedus,YunxuanLi,XuezhiWang,Mostafa
Dehghani,SiddharthaBrahma,AlbertWebson,ShixiangShaneGu,ZhuyunDai,MiracSuzgun,XinyunChen,Aakanksha
Chowdhery, Alex Castro-Ros, Marie Pellat, Kevin Robinson, Dasha Valter, Sharan Narang, Gaurav Mishra, Adams
Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob Devlin,
Adam Roberts, Denny Zhou, Quoc V. Le, and Jason Wei. 2022. Scaling Instruction-Finetuned Language Models.
arXiv:2210.11416[cs.LG]
SamuelCoope,TylerFarghly,DanielaGerz,IvanVulic´,andMatthewHenderson.2020.Span-ConveRT:Few-shotSpan
Extraction for Dialog with Pretrained Conversational Representations. In Proceedings of the 58th Annual Meeting of
theAssociation forComputationalLinguistics.Association forComputationalLinguistics, Online,107–121. https:
//doi.org/10.18653/v1/2020.acl-main.11

<!-- Page 24 -->

24 NaturalLanguageEngineering
LeyangCui,YuWu,ShujieLiu,YueZhang,andMingZhou.2020.MuTual:ADatasetforMulti-TurnDialogueReasoning.In
Proceedingsofthe58thAnnualMeetingoftheAssociationforComputationalLinguistics.AssociationforComputational
Linguistics,Online,1406–1416. https://doi.org/10.18653/v1/2020.acl-main.130
Paula Czarnowska, Sebastian Ruder, Ryan Cotterell, and Ann Copestake. 2020. Morphologically Aware Word-Level
Translation. In Proceedings of the 28th International Conference on Computational Linguistics, Donia Scott, Nuria
Bel, and Chengqing Zong (Eds.). International Committee on Computational Linguistics, Barcelona, Spain (Online),
2847–2860. https://doi.org/10.18653/v1/2020.coling-main.256
YinpeiDai,HangyuLi,YongbinLi,JianSun,FeiHuang,LuoSi,andXiaodanZhu.2021a.Preview,AttendandReview:
Schema-Aware Curriculum Learning for Multi-Domain Dialogue State Tracking. In Proceedings of the 59th Annual
Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural
LanguageProcessing(Volume2:ShortPapers).AssociationforComputationalLinguistics,Online,879–885. https:
//doi.org/10.18653/v1/2021.acl-short.111
YinpeiDai,HuihuaYu,YixuanJiang,ChengguangTang,YongbinLi,andJianSun.2021b.ASurveyonDialogManagement:

### RecentAdvancesandChallenges.arXiv:2005.02233[cs.CL]

JeffreyDalton,SophieFischer,PaulOwoicho,FilipRadlinski,FedericoRossetto,JohanneR.Trippas,andHamedZamani.

#### ConversationalInformationSeeking:TheoryandApplication(SIGIR’22).3455–3458.

ArijitDeandSunilKumarKopparapu.2010.Arule-basedShortQueryIntentIdentificationSystem.In2010International
ConferenceonSignalandImageProcessing.212–216. https://doi.org/10.1109/ICSIP.2010.5697471
JanDeriu,AlvaroRodrigo,ArantxaOtegi,GuillermoEchegoyen,SophieRosset,EnekoAgirre,andMarkCieliebak.2021.
Surveyonevaluationmethodsfordialoguesystems.ArtificialIntelligenceReview54(2021),755–810.
PooravDesai,TanmoyChakraborty,andMd.ShadAkhtar.2021.Niceperfume.Howlongdidyoumarinateinit?Multimodal
SarcasmExplanation.InAAAIConferenceonArtificialIntelligence.
Alvin Dey, Tanya Chowdhury, Yash Kumar, and Tanmoy Chakraborty. 2020. Corpora Evaluation and System Bias
Detection in Multi-document Summarization. In Findings of the Association for Computational Linguistics: EMNLP

## Association for Computational Linguistics, Online, 2830–2840. https://doi.org/10.18653/v1/2020.

findings-emnlp.254
Emily Dinan, Stephen Roller, Kurt Shuster, Angela Fan, Michael Auli, and Jason Weston. 2019. Wizard of Wikipedia:
Knowledge-Powered Conversational Agents. In International Conference on Learning Representations. https://
openreview.net/forum?id=r1l73iRqKm
Mark Dingemanse and Simeon Floyd. 2014. Conversation across cultures. In The Cambridge handbook of linguistic
anthropology.CambridgeUniversityPress,447–480.
LiDong,FuruWei,MingZhou,andKeXu.2015.QuestionAnsweringoverFreebasewithMulti-ColumnConvolutional
NeuralNetworks.InProceedingsofthe53rdAnnualMeetingoftheAssociationforComputationalLinguisticsandthe7th
InternationalJointConferenceonNaturalLanguageProcessing(Volume1:LongPapers).AssociationforComputational
Linguistics,Beijing,China,260–269. https://doi.org/10.3115/v1/P15-1026
NouhaDziri,EhsanKamalloo,SivanMilton,OsmarZaiane,MoYu,EdoardoM.Ponti,andSivaReddy.2022.FaithDial:A
FaithfulBenchmarkforInformation-SeekingDialogue.TransactionsoftheAssociationforComputationalLinguistics
10 (12 2022), 1473–1490. https://doi.org/10.1162/tacl_a_00529 arXiv:https://direct.mit.edu/tacl/articlepdf/doi/10.1162/tacl_a_00529/2065956/tacl_a_00529.pdf
ArashEinolghozati,PanupongPasupat,S.Gupta,RushinShah,MrinalMohit,MikeLewis,andLukeZettlemoyer.2018.
ImprovingSemanticParsingforTaskOrientedDialog.32ndConferenceonNeuralInformationProcessingSystems(NIPS
2018)(2018).
AhmedElgohary,DenisPeskov,andJordanBoyd-Graber.2019.CanYouUnpackThat?LearningtoRewriteQuestionsin-Context. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the
9thInternationalJointConferenceonNaturalLanguageProcessing(EMNLP-IJCNLP).AssociationforComputational
Linguistics,HongKong,China,5918–5924. https://doi.org/10.18653/v1/D19-1605
MihailEric,RahulGoel,ShachiPaul,AbhishekSethi,SanchitAgarwal,ShuyangGao,AdarshKumar,AnujGoyal,Peter
Ku,andDilekHakkani-Tur.2020.MultiWOZ2.1:AConsolidatedMulti-DomainDialogueDatasetwithStateCorrections
andStateTrackingBaselines.InProceedingsoftheTwelfthLanguageResourcesandEvaluationConference.European
LanguageResourcesAssociation,Marseille,France,422–428. https://aclanthology.org/2020.lrec-1.53
ElinEricsson,SylvanaSofkovaHashemi,andJohanLundin.2023.Funandfrustrating:Students’perspectivesonpractising
speakingEnglishwithvirtualhumans.CogentEducation10,1(2023),2170088.
BenoitFavre,EvgenyStepanov,JérémyTrione,FrédéricBéchet,andGiuseppeRiccardi.2015.CallCentreConversation
Summarization:APilotTaskatMultiling2015.InProceedingsofthe16thAnnualMeetingoftheSpecialInterestGroup
onDiscourseandDialogue,AlexanderKoller,GabrielSkantze,FilipJurcicek,MasahiroAraki,andCarolynPensteinRose
(Eds.).AssociationforComputationalLinguistics,Prague,CzechRepublic,232–236. https://doi.org/10.18653/
v1/W15-4633
GuyFeigenblat,ChulakaGunasekara,BenjaminSznajder,SachindraJoshi,DavidKonopnicki,andRanitAharonov.2021.
TWEETSUMM–ADialogSummarizationDatasetforCustomerService.arXiv:2111.11894[cs.CL]

<!-- Page 25 -->


### LATEXSupplement 25

Song Feng, Hui Wan, Chulaka Gunasekara, Siva Patel, Sachindra Joshi, and Luis Lastras. 2020. doc2dial: A Goal-
OrientedDocument-GroundedDialogueDataset.InProceedingsofthe2020ConferenceonEmpiricalMethodsinNatural
LanguageProcessing(EMNLP).AssociationforComputationalLinguistics,Online,8118–8128.
XiachongFeng,XiaochengFeng,andBingQin.2022a.ASurveyonDialogueSummarization:RecentAdvancesandNew
Frontiers.InProceedingsoftheThirty-FirstInternationalJointConferenceonArtificialIntelligence,IJCAI-22,LudDe
Raedt(Ed.).InternationalJointConferencesonArtificialIntelligenceOrganization,5453–5460. https://doi.org/10.
24963/ijcai.2022/764SurveyTrack.
YueFeng,AldoLipani,FanghuaYe,QiangZhang,andEmineYilmaz.2022b.DynamicSchemaGraphFusionNetworkfor
Multi-DomainDialogueStateTracking.InProceedingsofthe60thAnnualMeetingoftheAssociationforComputational
Linguistics (Volume 1: Long Papers). Association for Computational Linguistics, Dublin, Ireland, 115–126. https:
//doi.org/10.18653/v1/2022.acl-long.10
Silin Gao, Beatriz Borges, Soyoung Oh, Deniz Bayazit, Saya Kanno, Hiromi Wakaki, Yuki Mitsufuji, and Antoine
Bosselut. 2023. PeaCoK: Persona Commonsense Knowledge for Consistent and Engaging Narratives. arXiv preprint
arXiv:2305.02364(2023).
Deepanway Ghosal, Pengfei Hong, Siqi Shen, Navonil Majumder, Rada Mihalcea, and Soujanya Poria. 2021. CIDER:
CommonsenseInferenceforDialogueExplanationandReasoning.InProceedingsofthe22ndAnnualMeetingofthe
SpecialInterestGrouponDiscourseandDialogue.AssociationforComputationalLinguistics,SingaporeandOnline,
301–313. https://aclanthology.org/2021.sigdial-1.33
Deepanway Ghosal, Navonil Majumder, Alexander Gelbukh, Rada Mihalcea, and Soujanya Poria. 2020. COSMIC:
COmmonSenseknowledgeforeMotionIdentificationinConversations.InFindingsoftheAssociationforComputational
Linguistics: EMNLP 2020. Association for Computational Linguistics, Online, 2470–2481. https://doi.org/10.
18653/v1/2020.findings-emnlp.224
DeepanwayGhosal,NavonilMajumder,SoujanyaPoria,NiyatiChhaya,andAlexanderGelbukh.2019.DialogueGCN:A
GraphConvolutionalNeuralNetworkforEmotionRecognitioninConversation.InProceedingsofthe2019Conference
onEmpiricalMethodsinNaturalLanguageProcessingandthe9thInternationalJointConferenceonNaturalLanguage
Processing(EMNLP-IJCNLP).AssociationforComputationalLinguistics,HongKong,China,154–164. https://doi.
org/10.18653/v1/D19-1015
AmeliaGlaese,NatMcAleese,MajaTre˛bacz,JohnAslanides,VladFiroiu,TimoEwalds,MaribethRauh,LauraWeidinger,
MartinChadwick,PhoebeThacker,LucyCampbell-Gillingham,JonathanUesato,Po-SenHuang,RamonaComanescu,
FanYang,AbigailSee,SumanthDathathri,RoryGreig,CharlieChen,DougFritz,JaumeSanchezElias,RichardGreen,
SonˇaMokrá,NicholasFernando,BoxiWu,RachelFoley,SusannahYoung,IasonGabriel,WilliamIsaac,JohnMellor,
DemisHassabis,KorayKavukcuoglu,LisaAnneHendricks,andGeoffreyIrving.2022.Improvingalignmentofdialogue
agentsviatargetedhumanjudgements.arXiv:2209.14375[cs.LG]
Bogdan Gliwa, Iwona Mochol, Maciej Biesek, and Aleksander Wawer. 2019. SAMSum Corpus: A Human-annotated
DialogueDatasetforAbstractiveSummarization.InProceedingsofthe2ndWorkshoponNewFrontiersinSummarization.
AssociationforComputationalLinguistics,HongKong,China,70–79. https://doi.org/10.18653/v1/D19-5409
AnnaGottardi,OsmanIpek,GiuseppeCastellucci,ShuiHu,LavinaVaz,YaoLu,AnjuKhatri,AnjaliChadha,Desheng
Zhang, Sattvik Sahai, et al. 2022. Alexa, let’s work together: Introducing the first alexa prize taskbot challenge on
conversationaltaskassistance.arXivpreprintarXiv:2209.06321(2022).
H. P. Grice. 1975. Logic and Conversation. Brill, Leiden, The Netherlands, 41 – 58. https://doi.org/10.1163/
9789004368811_003
P. Grice. 1989. Studies in the Way of Words. Harvard University Press. https://books.google.co.in/books?id=

### QqtAbk-bs34C

Jia-ChenGu,ZhenhuaLing,QuanLiu,ZhigangChen,andXiaodanZhu.2020.FilteringbeforeIterativelyReferringfor
Knowledge-GroundedResponseSelectioninRetrieval-BasedChatbots.InFindingsoftheAssociationforComputational
Linguistics: EMNLP 2020. Association for Computational Linguistics, Online, 1412–1422. https://doi.org/10.
18653/v1/2020.findings-emnlp.127
SonalGupta,RushinShah,MrinalMohit,AnujKumar,andMikeLewis.2018.SemanticParsingforTaskOrientedDialog
usingHierarchicalRepresentations.InProceedingsofthe2018ConferenceonEmpiricalMethodsinNaturalLanguage
Processing.AssociationforComputationalLinguistics,Brussels,Belgium,2787–2792. https://doi.org/10.18653/
v1/D18-1300
Sudipto Dip Halder, Mahit Kumar Paul, and Bayezid Islam. 2022. Abstractive Dialog Summarization using Two Stage
FrameworkwithContrastiveLearning.In202225thInternationalConferenceonComputerandInformationTechnology
(ICCIT).540–544. https://doi.org/10.1109/ICCIT57492.2022.10055286
Jie Hao, Linfeng Song, Liwei Wang, Kun Xu, Zhaopeng Tu, and Dong Yu. 2021. RAST: Domain-Robust Dialogue
Rewriting as Sequence Tagging. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language
Processing, Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih (Eds.). Association for
ComputationalLinguistics,OnlineandPuntaCana,DominicanRepublic,4913–4924. https://doi.org/10.18653/
v1/2021.emnlp-main.402

<!-- Page 26 -->

26 NaturalLanguageEngineering
Jan-GerritHarms,PavelKucherbaev,AlessandroBozzon,andGeert-JanHouben.2019.ApproachesforDialogManagement
inConversationalAgents.IEEEInternetComputing23,2(2019),13–22. https://doi.org/10.1109/MIC.2018.
2881519
He He, Derek Chen, Anusha Balakrishnan, and Percy Liang. 2018. Decoupling Strategy and Generation in Negotiation
Dialogues.InProceedingsofthe2018ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.Association
forComputationalLinguistics,Brussels,Belgium,2333–2343. https://doi.org/10.18653/v1/D18-1256
TingHe,XiaohongXu,YatingWu,HuazhenWang,andJianChen.2021.MultitaskLearningwithKnowledgeBaseforJoint
IntentDetectionandSlotFilling.AppliedSciences11,11(2021). https://doi.org/10.3390/app11114887
WanweiHe,YinpeiDai,MinYang,JianSun,FeiHuang,LuoSi,andYongbinLi.2022.UnifiedDialogModelPre-Training
forTask-OrientedDialogUnderstandingandGeneration.InProceedingsofthe45thInternationalACMSIGIRConference
on Research and Development in Information Retrieval (Madrid, Spain) (SIGIR ’22). Association for Computing
Machinery,NewYork,NY,USA,187–200. https://doi.org/10.1145/3477495.3532069
BehnamHedayatnia,KarthikGopalakrishnan,SeokhwanKim,YangLiu,MihailEric,andDilekHakkani-Tur.2020.Policy-
DrivenNeuralResponseGenerationforKnowledge-GroundedDialogSystems.InProceedingsofthe13thInternational
Conference on Natural Language Generation. Association for Computational Linguistics, Dublin, Ireland, 412–421.
https://aclanthology.org/2020.inlg-1.46
Matthew Henderson, Iñigo Casanueva, Nikola Mrkšic´, Pei-Hao Su, Tsung-Hsien Wen, and Ivan Vulic´. 2020. ConveRT:
Efficient and Accurate Conversational Representations from Transformers. In Findings of the Association for
Computational Linguistics: EMNLP 2020. Association for Computational Linguistics, Online, 2161–2174. https:
//doi.org/10.18653/v1/2020.findings-emnlp.196
PeterHenderson,KoustuvSinha,NicolasAngelard-Gontier,NanRosemaryKe,GenevieveFried,RyanLowe,andJoelle
Pineau.2018.Ethicalchallengesindata-drivendialoguesystems.InProceedingsofthe2018AAAI/ACMConferenceon
AI,Ethics,andSociety.123–129.
SamHepenstal,NeeshaKodagoda,LeishiZhang,PragyaPaudyal,andBWong.2019.Algorithmictransparencyofconversational agents. In IUI 2019 Workshop on Intelligent User Interfaces for Algorithmic Transparency in Emerging
Technologies.85y0v.
Ben Hixon, Peter Clark, and Hannaneh Hajishirzi. 2015. Learning Knowledge Graphs for Question Answering through
ConversationalDialog.InProceedingsofthe2015ConferenceoftheNorthAmericanChapteroftheAssociationfor
ComputationalLinguistics:HumanLanguageTechnologies.AssociationforComputationalLinguistics,Denver,Colorado,
851–861. https://doi.org/10.3115/v1/N15-1086
LiannaHrycyk,AlessandraZarcone,andLuzianHahn.2021.NotSoFast,Classifier–AccuracyandEntropyReductionin
IncrementalIntentClassification.InProceedingsofthe3rdWorkshoponNaturalLanguageProcessingforConversational
AI,AlexandrosPapangelis,PawełBudzianowski,BingLiu,ElnazNouri,AbhinavRastogi,andYun-NungChen(Eds.).
AssociationforComputationalLinguistics,Online,52–67. https://doi.org/10.18653/v1/2021.nlp4convai-1.6
Guimin Hu, Ting-En Lin, Yi Zhao, Guangming Lu, Yuchuan Wu, and Yongbin Li. 2022. UniMSE: Towards Unified
Multimodal Sentiment Analysis and Emotion Recognition. In Proceedings of the 2022 Conference on Empirical
MethodsinNaturalLanguageProcessing.AssociationforComputationalLinguistics,AbuDhabi,UnitedArabEmirates,
7837–7851. https://aclanthology.org/2022.emnlp-main.534
YilunHua,ZhaoyuanDeng,andKathleenMcKeown.2023.ImprovingLongDialogueSummarizationwithSemanticGraph
Representation.InFindingsoftheAssociationforComputationalLinguistics:ACL2023,AnnaRogers,JordanBoyd-
Graber,andNaoakiOkazaki(Eds.).AssociationforComputationalLinguistics,Toronto,Canada,13851–13883. https:
//doi.org/10.18653/v1/2023.findings-acl.871
MengzuoHuang,FengLi,WuheZou,andWeidongZhang.2021.SARG:ANovelSemiAutoregressiveGeneratorforMultiturnIncompleteUtteranceRestoration.ProceedingsoftheAAAIConferenceonArtificialIntelligence35,14(May2021),
13055–13063. https://doi.org/10.1609/aaai.v35i14.17543
S.E.HusseinandM.H.Granat.2002.Intentiondetectionusinganeuro-fuzzyEMGclassifier.IEEEEngineeringinMedicine
andBiologyMagazine21,6(2002),123–129. https://doi.org/10.1109/MEMB.2002.1175148
Yerin Hwang,Yongil Kim, HyunkyungBae, Hwanhee Lee,Jeesoo Bang, andKyomin Jung.2023. Dialogizer: ContextawareConversational-QADatasetGenerationfromTextualSources.InProceedingsofthe2023ConferenceonEmpirical
Methods in Natural Language Processing, Houda Bouamor, Juan Pino, and Kalika Bali (Eds.). Association for
ComputationalLinguistics,Singapore,8806–8828. https://doi.org/10.18653/v1/2023.emnlp-main.545
PaoloItaliani,GiacomoFrisoni,GianlucaMoro,AntonellaCarbonaro,andClaudioSartori.2024.Evidence,myDearWatson:
Abstractivedialoguesummarizationonlearnablerelevantutterances.Neurocomputing572(2024),127132. https://
doi.org/10.1016/j.neucom.2023.127132
Xiaowei Jia, Sheng Li, Handong Zhao, Sungchul Kim, and Vipin Kumar. 2019. Towards Robust and Discriminative
SequentialDataLearning:WhenandHowtoPerformAdversarialTraining?.InProceedingsofthe25thACMSIGKDD
InternationalConferenceonKnowledgeDiscovery&DataMining(Anchorage,AK,USA)(KDD’19).Associationfor
ComputingMachinery,NewYork,NY,USA,1665–1673. https://doi.org/10.1145/3292500.3330957

<!-- Page 27 -->


### LATEXSupplement 27

WenhuiJiang,XiaodongGu,YutingChen,andBeijunShen.2023.DuReSE:RewritingIncompleteUtterancesviaNeural
SequenceEditing.NeuralProcessingLetters(032023),1–18. https://doi.org/10.1007/s11063-023-11174-8
Anirudh Joshi, Namit Katariya, Xavier Amatriain, and Anitha Kannan. 2020. Dr. Summarize: Global Summarization of
MedicalDialoguebyExploitingLocalStructures..InFindingsoftheAssociationforComputationalLinguistics:EMNLP
2020, Trevor Cohn, Yulan He, and Yang Liu (Eds.). Association for Computational Linguistics, Online, 3755–3763.
https://doi.org/10.18653/v1/2020.findings-emnlp.335
Ashutosh Joshi, Shankar Vishwanath, Choon Teo, Vaclav Petricek, Vishy Vishwanathan, Rahul Bhagat, and Jonathan
May.2022.AugmentingTrainingDataforMassiveSemanticMatchingModelsinLow-TrafficE-commerceStores.In
Proceedingsofthe2022ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:
Human Language Technologies: Industry Track, Anastassia Loukina, Rashmi Gangadharaiah, and Bonan Min (Eds.).
AssociationforComputationalLinguistics,Hybrid:Seattle,Washington+Online,160–167. https://doi.org/10.
18653/v1/2022.naacl-industry.19
DanicaJovanovicandTheoVanLeeuwen.2018.Multimodaldialogueonsocialmedia.SocialSemiotics28,5(2018),683–
699. https://doi.org/10.1080/10350330.2018.1504732arXiv:https://doi.org/10.1080/10350330.2018.1504732
Daniel Jurafsky, Elizabeth Shriberg, and Debra Biasca. 1997. Switchboard SWBD-DAMSL Shallow-Discourse-Function
AnnotationCodersManual,Draft13.TechnicalReport97-02.UniversityofColorado,BoulderInstituteofCognitive
Science,Boulder,CO.
GeorgiKaradzhov,TomStafford,andAndreasVlachos.2021.DeliData:Adatasetfordeliberationinmulti-partyproblem
solving.ArXivabs/2108.05271(2021).
XiruiKe,JingZhang,XinLv,YiqiXu,ShulinCao,CuipingLi,HongChen,andJuanziLi.2022.Knowledge-augmentedSelftrainingofAQuestionRewriterforConversationalKnowledgeBaseQuestionAnswering.InFindingsoftheAssociation
for Computational Linguistics: EMNLP 2022. Association for Computational Linguistics, Abu Dhabi, United Arab
Emirates,1844–1856. https://aclanthology.org/2022.findings-emnlp.133
Anant Khandelwal. 2021. WeaSuL: Weakly Supervised Dialogue Policy Learning: Reward Estimation for Multi-turn
Dialogue.InWorkshoponDocument-groundedDialogueandConversationalQuestionAnswering.
D Kiela and J Weston. 2019. What makes a good conversation? how controllable attributes affect human judgments. In
Proceedingsofthe2019ConferenceoftheNAACLNAACL-HLT.
HyunwooKim,JackHessel,LiweiJiang,XimingLu,YoungjaeYu,PeiZhou,RonanLeBras,MaliheAlikhani,Gunhee
Kim, Maarten Sap, and Yejin Choi. 2022a. SODA: Million-scale Dialogue Distillation with Social Commonsense

### Contextualization.arXiv:2212.10465[cs.CL]

HyunwooKim,YoungjaeYu,LiweiJiang,XimingLu,DanielKhashabi,GunheeKim,YejinChoi,andMaartenSap.2022c.
ProsocialDialog:AProsocialBackboneforConversationalAgents.InProceedingsofthe2022ConferenceonEmpirical
MethodsinNaturalLanguageProcessing.AssociationforComputationalLinguistics,AbuDhabi,UnitedArabEmirates,
4005–4029. https://aclanthology.org/2022.emnlp-main.267
SeungoneKim,SeJuneJoo,HyungjooChae,ChaehyeongKim,Seung-wonHwang,andJinyoungYeo.2022b.MindtheGap!
InjectingCommonsenseKnowledgeforAbstractiveDialogueSummarization.InProceedingsofthe29thInternational
ConferenceonComputationalLinguistics.InternationalCommitteeonComputationalLinguistics,Gyeongju,Republicof

### Korea,6285–6300. https://aclanthology.org/2022.coling-1.548

JanKocon´,IgorCichecki,OliwierKaszyca,MateuszKochanek,DominikaSzydło,JoannaBaran,JulitaBielaniewicz,Marcin
Gruza,ArkadiuszJanz,KamilKanclerz,AnnaKocon´,BartłomiejKoptyra,WiktoriaMieleszczenko-Kowszewicz,Piotr
Miłkowski,MarcinOleksy,MaciejPiasecki,ŁukaszRadlin´ski,KonradWojtasik,StanisławWoz´niak,andPrzemysław
Kazienko.2023.ChatGPT:Jackofalltrades,masterofnone.arXiv:2302.10724[cs.CL]
Mojtaba Komeili, Kurt Shuster, and Jason Weston. 2022. Internet-Augmented Dialogue Generation. In Proceedings of
the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). Association for
ComputationalLinguistics,Dublin,Ireland,8460–8478. https://doi.org/10.18653/v1/2022.acl-long.579
KiraKretzschmar,HollyTyroll,GabrielaPavarini,AriannaManzini,IlinaSingh,andNeurOxYoungPeople’sAdvisory
Group. 2019. Can your phone be your therapist? Young people’s ethical perspectives on the use of fully automated
conversationalagents(chatbots)inmentalhealthsupport.Biomedicalinformaticsinsights11(2019),1178222619829083.
ApoorvKulshreshtha,DanielDeFreitasAdiwardana,DavidRichardSo,GauravNemade,JamieHall,NoahFiedel,QuocV.
Le,RomalThoppilan,ThangLuong,YifengLu,andZiYang.2020.TowardsaHuman-likeOpen-DomainChatbot.In
arXiv.
ShivaniKumar,ShubhamDudeja,MdShadAkhtar,andTanmoyChakraborty.2023a.EmotionFlipReasoninginMultiparty
Conversations.arXivpreprintarXiv:2306.13959(2023).
ShivaniKumar,AtharvaKulkarni,MdShadAkhtar,andTanmoyChakraborty.2022a.Whendidyoubecomesosmart,oh
wiseone?!SarcasmExplanationinMulti-modalMulti-partyDialogues.InProceedingsofthe60thAnnualMeetingofthe
AssociationforComputationalLinguistics(Volume1:LongPapers).AssociationforComputationalLinguistics,Dublin,
Ireland,5956–5968. https://doi.org/10.18653/v1/2022.acl-long.411
Shivani Kumar, Ishani Mondai, Md Shad Akhtar, and Tanmoy Chakraborty. 2023b. Explaining (Sarcastic) Utterances to
Enhance Affect Understanding in Multimodal Dialogues. In Proceedings of the Thirty-Seventh AAAI Conference on

<!-- Page 28 -->

28 NaturalLanguageEngineering
Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth
SymposiumonEducationalAdvancesinArtificialIntelligence(AAAI’23/IAAI’23/EAAI’23).AAAIPress,Article1457,
9pages. https://doi.org/10.1609/aaai.v37i11.26526
Shivani Kumar, Ishani Mondal, Md Shad Akhtar, and Tanmoy Chakraborty. 2022b. Explaining (Sarcastic) Utterances to
EnhanceAffectUnderstandinginMultimodalDialogues.arXiv:2211.11049[cs.CL]
ShivaniKumar,AnubhavShrimal,MdShadAkhtar,andTanmoyChakraborty.2022c.Discoveringemotionandreasoningits
flipinmulti-partyconversationsusingmaskedmemorynetworkandtransformer.Knowledge-BasedSystems240(2022),
108112.
Guillaume Lample, Miguel Ballesteros, Sandeep Subramanian, Kazuya Kawakami, and Chris Dyer. 2016. Neural
ArchitecturesforNamedEntityRecognition.InProceedingsofthe2016ConferenceoftheNorthAmericanChapterofthe
AssociationforComputationalLinguistics:HumanLanguageTechnologies.AssociationforComputationalLinguistics,
SanDiego,California,260–270. https://doi.org/10.18653/v1/N16-1030
StefanLarson,AnishMahendran,JosephJ.Peper,ChristopherClarke,AndrewLee,ParkerHill,JonathanK.Kummerfeld,
KevinLeach,MichaelA.Laurenzano,LingjiaTang,andJasonMars.2019.AnEvaluationDatasetforIntentClassification
and Out-of-Scope Prediction. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processingandthe9thInternationalJointConferenceonNaturalLanguageProcessing(EMNLP-IJCNLP).Association
forComputationalLinguistics,HongKong,China,1311–1316. https://doi.org/10.18653/v1/D19-1131
HugoLaurençon,LucileSaulnier,ThomasWang,ChristopherAkiki,AlbertVillanovadelMoral,TevenLeScao,Leandro
VonWerra,ChenghaoMou,EduardoGonzálezPonferrada,HuuNguyen,etal.2022.Thebigsciencerootscorpus:A1.6
tbcompositemultilingualdataset.AdvancesinNeuralInformationProcessingSystems35(2022),31809–31826.
Y.Lecun,L.Bottou,Y.Bengio,andP.Haffner.1998.Gradient-basedlearningappliedtodocumentrecognition.Proc.IEEE
86,11(1998),2278–2324. https://doi.org/10.1109/5.726791
AndrewLee,ZheChen,KevinLeach,andJonathanK.Kummerfeld.2022.AugmentingTask-OrientedDialogueSystems
withRelationExtraction.ArXivabs/2210.13344(2022).
Chia-HsuanLee,HaoCheng,andMariOstendorf.2023.OrchestraLLM:EfficientOrchestrationofLanguageModelsfor
DialogueStateTracking.arXivpreprintarXiv:2311.09758(2023).
DongyubLee,JungHoonLim,TaesunWhang,ChanheeLee,SeungWooCho,MingunPark,andHeuiseokLim.2021.
CapturingSpeakerIncorrectness:Speaker-FocusedPost-CorrectionforAbstractiveDialogueSummarization.Proceedings
oftheThirdWorkshoponNewFrontiersinSummarization(2021).
JindongLeo-Liu.2023.Lovinga“defiant”AIcompanion?Thegenderperformanceandethicsofsocialexchangerobotsin
simulatedintimateinteractions.ComputersinHumanBehavior141(2023),107620.
HectorJ.Levesque,ErnestDavis,andLeoraMorgenstern.2012.TheWinogradSchemaChallenge.InProceedingsofthe
ThirteenthInternationalConferenceonPrinciplesofKnowledgeRepresentationandReasoning(Rome,Italy)(KR’12).
AAAIPress,552–561.
MikeLewis,YinhanLiu,NamanGoyal,MarjanGhazvininejad,AbdelrahmanMohamed,OmerLevy,VeselinStoyanov,
and Luke Zettlemoyer. 2020. BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation,
Translation, and Comprehension. In Proceedings of the 58th Annual Meeting of the Association for Computational
Linguistics.AssociationforComputationalLinguistics,Online,7871–7880. https://doi.org/10.18653/v1/2020.
acl-main.703
Junlong Li, Zhuosheng Zhang, and Hai Zhao. 2022b. Dialogue-adaptive Language Model Pre-training From Quality

### Estimation.arXiv:2009.04984[cs.CL]

ShiminLi,QinyuanCheng,LinyangLi,andXipengQiu.2022a.MitigatingNegativeStyleTransferinHybridDialogue
System.ArXivabs/2212.07183(2022).
WeiLi,YangLi,VladPandelea,MengshiGe,LuyaoZhu,andErikCambria.2023.ECPEC:Emotion-CausePairExtraction
inConversations.IEEETransactionsonAffectiveComputing14,3(2023),1754–1765. https://doi.org/10.1109/

## Taffc.2022.3216551

XinLi,PijiLi,YanWang,XiaojiangLiu,andWaiLam.2021b.EnhancingDialogueGenerationviaMulti-LevelContrastive

### Learning.arXiv:2009.09147[cs.CL]

YanranLi,WenjieLi,andZhitaoWang.2021a.Graph-StructuredContextUnderstandingforKnowledge-GroundedResponse
Generation(SIGIR’21).AssociationforComputingMachinery,NewYork,NY,USA,1930–1934. https://doi.org/
10.1145/3404835.3463000
YanranLi,HuiSu,XiaoyuShen,WenjieLi,ZiqiangCao,andShuziNiu.2017.DailyDialog:AManuallyLabelledMulti-turn
DialogueDataset.InProceedingsoftheEighthInternationalJointConferenceonNaturalLanguageProcessing(Volume
1:LongPapers).AsianFederationofNaturalLanguageProcessing,Taipei,Taiwan,986–995. https://aclanthology.
org/I17-1099
Yue Li and Jiong Zhang. 2021. Semi-supervised Meta-learning for Cross-domain Few-shot Intent Classification. In
Proceedingsofthe1stWorkshoponMetaLearningandItsApplicationstoNaturalLanguageProcessing,Hung-YiLee,
MitraMohtarami,Shang-WenLi,DiJin,MandyKorpusik,ShuyanDong,NgocThangVu,andDilekHakkani-Tur(Eds.).
AssociationforComputationalLinguistics,Online,67–75. https://doi.org/10.18653/v1/2021.metanlp-1.8

<!-- Page 29 -->


### LATEXSupplement 29

Chen Liang, Jonathan Berant, Quoc Le, Kenneth D. Forbus, and Ni Lao. 2017. Neural Symbolic Machines: Learning
Semantic Parsers on Freebase with Weak Supervision. In Proceedings of the 55th Annual Meeting of the Association
forComputationalLinguistics(Volume1:LongPapers).AssociationforComputationalLinguistics,Vancouver,Canada,
23–33. https://doi.org/10.18653/v1/P17-1003
Xinnian Liang, Shuangzhi Wu, Chenhao Cui, Jiaqi Bai, Chao Bian, and Zhoujun Li. 2023. Enhancing Dialogue
SummarizationwithTopic-AwareGlobal-andLocal-LevelCentrality.arXiv:2301.12376[cs.CL]
Chin-YewLin.2004.ROUGE:APackageforAutomaticEvaluationofSummaries.InTextSummarizationBranchesOut.
AssociationforComputationalLinguistics,Barcelona,Spain,74–81. https://aclanthology.org/W04-1013
Sheng-ChiehLin,Jheng-HongYang,andJimmyLin.2021.ContextualizedQueryEmbeddingsforConversationalSearch.
InProceedingsofthe2021ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,Marie-FrancineMoens,
XuanjingHuang,LuciaSpecia,andScottWen-tauYih(Eds.).AssociationforComputationalLinguistics,Onlineand
PuntaCana,DominicanRepublic,1004–1015. https://doi.org/10.18653/v1/2021.emnlp-main.77
XiVictoriaLin,RichardSocher,andCaimingXiong.2020.BridgingTextualandTabularDataforCross-DomainTextto-SQLSemanticParsing.InFindingsoftheAssociationforComputationalLinguistics:EMNLP2020.Associationfor
ComputationalLinguistics,Online,4870–4888. https://doi.org/10.18653/v1/2020.findings-emnlp.438
ZhaojiangLin,AndreaMadotto,GentaIndraWinata,PengXu,FeijunJiang,YuxiangHu,ChenShi,andPascaleFung.[n.d.].
BiToD:ABilingualMulti-DomainDatasetForTask-OrientedDialogueModeling.InThirty-fifthConferenceonNeural
InformationProcessingSystemsDatasetsandBenchmarksTrack(Round1).
ZacharyLipton,XiujunLi,JianfengGao,LihongLi,FaisalAhmed,andLiDeng.2018.Bbq-networks:Efficientexploration
indeepreinforcementlearningfortask-orienteddialoguesystems.InProceedingsoftheAAAIConferenceonArtificial
Intelligence,Vol.32.
BingLiuandSahisnuMazumder.2021.Lifelongandcontinuallearningdialoguesystems:learningduringconversation.In
ProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.35.15058–15063.
BingLiu,GokhanTur,DilekHakkani-Tur,PararthShah,andLarryHeck.2017b.End-to-endoptimizationoftask-oriented
dialoguemodelwithdeepreinforcementlearning.arXivpreprintarXiv:1711.10712(2017).
ChunyiLiu,PengWang,JiangXu,ZangLi,andJiepingYe.2019.AutomaticDialogueSummaryGenerationforCustomer
Service.InProceedingsofthe25thACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining
(Anchorage,AK,USA)(KDD’19).AssociationforComputingMachinery,NewYork,NY,USA,1957–1965. https:
//doi.org/10.1145/3292500.3330683
Chia-WeiLiu,RyanLowe,IulianV.Serban,MichaelNoseworthy,LaurentCharlin,andJoellePineau.2017a.HowNOT
To Evaluate Your Dialogue System: An Empirical Study of Unsupervised Evaluation Metrics for Dialogue Response

### Generation.arXiv:1603.08023[cs.CL]

Han Liu, Siyang Zhao, Xiaotong Zhang, Feng Zhang, Junjie Sun, Hong Yu, and Xianchao Zhang. 2022d. A Simple
Meta-Learning Paradigm for Zero-Shot Intent Classification with Mixture Attention Mechanism. In Proceedings of
the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval (<conf-loc>,
<city>Madrid</city>,<country>Spain</country>,</conf-loc>)(SIGIR’22).AssociationforComputingMachinery,New
York,NY,USA,2047–2052. https://doi.org/10.1145/3477495.3531803
QingbinLiu,GuirongBai,ShizhuHe,CaoLiu,KangLiu,andJunZhao.2021a.Heterogeneousrelationalgraphneural
networkswithadaptiveobjectiveforend-to-endtask-orienteddialogue.Knowledge-BasedSystems227(2021),107186.
Qian Liu, Bei Chen, Jian-Guang Lou, Bin Zhou, and Dongmei Zhang. 2020b. Incomplete Utterance Rewriting as
SemanticSegmentation.InProceedingsofthe2020ConferenceonEmpiricalMethodsinNaturalLanguageProcessing
(EMNLP).AssociationforComputationalLinguistics,Online,2846–2857. https://doi.org/10.18653/v1/2020.
emnlp-main.227
QianLiu,YihongChen,B.Chen,Jian-GuangLou,ZixuanChen,BinZhou,andDongmeiZhang.2020a.YouImpressMe:
DialogueGenerationviaMutualPersonaPerception.InAnnualMeetingoftheAssociationforComputationalLinguistics.
XingkunLiu,ArashEshghi,PawelSwietojanski,andVerenaRieser.2021b.Benchmarkingnaturallanguageunderstanding
servicesforbuildingconversationalagents.InIncreasingNaturalnessandFlexibilityinSpokenDialogueInteraction:10th
InternationalWorkshoponSpokenDialogueSystems.Springer,165–183.
XingkunLiu,ArashEshghi,PawelSwietojanski,andVerenaRieser.2021c.BenchmarkingNaturalLanguageUnderstanding
ServicesforBuildingConversationalAgents.SpringerSingapore,Singapore,165–183. https://doi.org/10.1007/
978-981-15-9323-9_15
YongkangLiu,ShiFeng,WeiGao,DalingWang,andYifeiZhang.2022a.DialogConv:ALightweightFullyConvolutional
NetworkforMulti-viewResponseSelection.arXiv:2210.13845[cs.CL]
YongtaiLiu,JoshuaMaynez,GonçaloSimões,andShashiNarayan.2022b.DataAugmentationforLow-ResourceDialogue
Summarization. In Findings of the Association for Computational Linguistics: NAACL 2022, Marine Carpuat, Marie-
CatherinedeMarneffe,andIvanVladimirMezaRuiz(Eds.).AssociationforComputationalLinguistics,Seattle,United
States,703–710. https://doi.org/10.18653/v1/2022.findings-naacl.53
Zhengyuan Liu and Nancy F. Chen. 2021. Controllable Neural Dialogue Summarization with Personal Named Entity
Planning.InConferenceonEmpiricalMethodsinNaturalLanguageProcessing.

<!-- Page 30 -->

30 NaturalLanguageEngineering
ZemingLiu,JunXu,ZeyangLei,HaifengWang,Zheng-YuNiu,andHuaWu.2022c.WheretoGofortheHolidays:Towards
Mixed-TypeDialogsforClarificationofUserGoals.InAnnualMeetingoftheAssociationforComputationalLinguistics.
SamuelLouvanandBernardoMagnini.2018.ExploringNamedEntityRecognitionAsanAuxiliaryTaskforSlotFilling
inConversationalLanguageUnderstanding.InProceedingsofthe2018EMNLPWorkshopSCAI:The2ndInternational
WorkshoponSearch-OrientedConversationalAI.AssociationforComputationalLinguistics,Brussels,Belgium,74–80.
https://doi.org/10.18653/v1/W18-5711
SamuelLouvanandBernardoMagnini.2019.LeveragingNon-ConversationalTasksforLowResourceSlotFilling:Does
ithelp?.InProceedingsofthe20thAnnualSIGdialMeetingonDiscourseandDialogue.AssociationforComputational
Linguistics,Stockholm,Sweden,85–91. https://doi.org/10.18653/v1/W19-5911
SamuelLouvanandBernardoMagnini.2020.Recentneuralmethodsonslotfillingandintentclassificationfortask-oriented
dialoguesystems:Asurvey.arXivpreprintarXiv:2011.00564(2020).
RyanLowe,NissanPow,IulianSerban,andJoellePineau.2015.TheUbuntuDialogueCorpus:ALargeDatasetforResearch
inUnstructuredMulti-TurnDialogueSystems.InProceedingsofthe16thAnnualMeetingoftheSpecialInterestGroup
onDiscourseandDialogue.AssociationforComputationalLinguistics,Prague,CzechRepublic,285–294. https://
doi.org/10.18653/v1/W15-4640
GaleMLucas,JillBoberg,DavidTraum,RonArtstein,JonathanGratch,AlesiaGainer,EmmanuelJohnson,AntonLeuski,
and Mikio Nakano. 2018. Culture, errors, and rapport-building dialogue in social agents. In Proceedings of the 18th
InternationalConferenceonintelligentvirtualagents.51–58.
QueenieLuo,MichaelJ.Puett,andMichaelD.Smith.2023.APerspectivalMirroroftheElephant:InvestigatingLanguage
BiasonGoogle,ChatGPT,Wikipedia,andYouTube.arXiv:2303.16281[cs.CY]
XuezheMaandEduardHovy.2016.End-to-endSequenceLabelingviaBi-directionalLSTM-CNNs-CRF.InProceedings
ofthe54thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers).Associationfor
ComputationalLinguistics,Berlin,Germany,1064–1074. https://doi.org/10.18653/v1/P16-1101
Ganeshan Malhotra, Abdul Waheed, Aseem Srivastava, Md Shad Akhtar, and Tanmoy Chakraborty. 2022. Speaker and
Time-Aware Joint Contextual Learning for Dialogue-Act Classification in Counselling Conversations. In Proceedings
of the Fifteenth ACM International Conference on Web Search and Data Mining (Virtual Event, AZ, USA) (WSDM
’22).AssociationforComputingMachinery,NewYork,NY,USA,735–745. https://doi.org/10.1145/3488560.
3498509
Scott Martin, Shivani Poddar, and Kartikeya Upasani. 2020. MuDoCo: Corpus for Multidomain Coreference Resolution
andReferringExpressionGeneration.InProceedingsoftheTwelfthLanguageResourcesandEvaluationConference.
European Language Resources Association, Marseille, France, 104–111. https://aclanthology.org/2020.
lrec-1.13
SusanWMcRoy,SongsakChannarukul,andSyedSAli.2003.Anaugmentedtemplate-basedapproachtotextrealization.
NaturalLanguageEngineering9,4(2003),381–420.
MichaelMcTear.2021.Rule-BasedDialogueSystems:Architecture,Methods,andTools.SpringerInternationalPublishing,

### Cham,43–70. https://doi.org/10.1007/978-3-031-02176-3_2

ShikibMehri,MihailEric,andDilekHakkani-Tur.2020.DialoGLUE:ANaturalLanguageUnderstandingBenchmarkfor

### Task-OrientedDialogue.arXiv:2009.13570[cs.CL]

ShikibMehri,EvgeniiaRazumovskaia,TianchengZhao,andMaxineEskenazi.2019.PretrainingMethodsforDialogContext
RepresentationLearning.InProceedingsofthe57thAnnualMeetingoftheAssociationforComputationalLinguistics.
AssociationforComputationalLinguistics,Florence,Italy,3836–3845. https://doi.org/10.18653/v1/P19-1373
ChuanMeng,PengjieRen,ZhuminChen,WeiweiSun,ZhaochunRen,ZhaopengTu,andMaartendeRijke.2020.DukeNet:
ADualKnowledgeInteractionNetworkforKnowledge-GroundedConversation.InProceedingsofthe43rdInternational
ACM SIGIR Conference on Research and Development in Information Retrieval (Virtual Event, China) (SIGIR ’20).
Association for Computing Machinery, New York, NY, USA, 1151–1160. https://doi.org/10.1145/3397271.
3401097
XiaojunMeng,WenlinDai,YashengWang,BaojunWang,ZhiyongWu,XinJiang,andQunLiu.2022.Lexicon-injected
SemanticParsingforTask-OrientedDialog.ArXivabs/2211.14508(2022).
Fei Mi, Liangwei Chen, Mengjie Zhao, Minlie Huang, and Boi Faltings. 2020. Continual learning for natural language
generationintask-orienteddialogsystems.arXivpreprintarXiv:2010.00910(2020).
ShaoboMin,HantaoYao,HongtaoXie,ChaoqunWang,Zheng-JunZha,andYongdongZhang.2020.Domain-AwareVisual
BiasEliminatingforGeneralizedZero-ShotLearning.12661–12670. https://doi.org/10.1109/CVPR42600.2020.
01268
SeungwhanMoon,PararthShah,AnujKumar,andRajenSubba.2019.OpenDialKG:ExplainableConversationalReasoning
withAttention-basedWalksoverKnowledgeGraphs.InProceedingsofthe57thAnnualMeetingoftheAssociationfor
ComputationalLinguistics.AssociationforComputationalLinguistics,Florence,Italy,845–854. https://doi.org/
10.18653/v1/P19-1081
ChristianMuise,TathagataChakraborti,ShubhamAgarwal,OndrejBajgar,ArunimaChaudhary,LuisALastras-Montano,
JosefOndrej,MiroslavVodolan,andCharlieWiecha.2019.Planningforgoal-orienteddialoguesystems.arXivpreprint

<!-- Page 31 -->


### LATEXSupplement 31

arXiv:1910.08137(2019).
ShashiNarayan,YaoZhao,JoshuaMaynez,GonçaloSimões,VitalyNikolaev,andRyanT.McDonald.2021.Planningwith
LearnedEntityPromptsforAbstractiveSummarization.TransactionsoftheAssociationforComputationalLinguistics9
(2021),1475–1492.
AnnaNedoluzhko,MuskaanSingh,MarieHledíková,TirthankarGhosal,andOndˇrejBojar.2022.ELITRMinutingCorpus:
A Novel Dataset for Automatic Minuting from Multi-Party Meetings in English and Czech. In Proceedings of the
ThirteenthLanguageResourcesandEvaluationConference,NicolettaCalzolari,FrédéricBéchet,PhilippeBlache,Khalid
Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi, Hitoshi Isahara, Bente Maegaard, Joseph Mariani, Hélène
Mazo,JanOdijk,andSteliosPiperidis(Eds.).EuropeanLanguageResourcesAssociation,Marseille,France,3174–3182.
https://aclanthology.org/2022.lrec-1.340
Olabiyi Oluwatobi and Erik Mueller. 2020. DLGNet: A transformer-based model for dialogue response generation. In
Proceedingsofthe2ndworkshoponnaturallanguageprocessingforconversationalAI.54–62.
BoyanOnyshkevych.1993.Templatedesignforinformationextraction.InFifthMessageUnderstandingConference(MUC-
5):ProceedingsofaConferenceHeldinBaltimore,Maryland,August25-27,1993.
SiruOuyang,ZhuoshengZhang,andHaiZhao.2021.DialogueGraphModelingforConversationalMachineReading.In
FindingsoftheAssociationforComputationalLinguistics:ACL-IJCNLP2021.AssociationforComputationalLinguistics,
Online,3158–3169. https://doi.org/10.18653/v1/2021.findings-acl.279
Hariom A Pandya and Brijesh S Bhatt. 2021. Question answering survey: Directions, challenges, datasets, evaluation
matrices.arXivpreprintarXiv:2112.03572(2021).
KishorePapineni,SalimRoukos,ToddWard,andWei-JingZhu.2002.Bleu:aMethodforAutomaticEvaluationofMachine
Translation.InProceedingsofthe40thAnnualMeetingoftheAssociationforComputationalLinguistics.Association
for Computational Linguistics, Philadelphia, Pennsylvania, USA, 311–318. https://doi.org/10.3115/1073083.
1073135
Amin Parvaneh, Ehsan Abbasnejad, Qi Wu, and Javen Qinfeng Shi. 2019. Show, Price and Negotiate: A Hierarchical
AttentionRecurrentVisualNegotiator.ArXivabs/1905.03721(2019).
PanupongPasupat,S.Gupta,KarishmaMandyam,RushinShah,MichaelLewis,andLukeZettlemoyer.2019.Span-based
Hierarchical Semantic Parsing for Task-Oriented Dialog. In Conference on Empirical Methods in Natural Language
Processing.
DebjitPaul,DaniilSorokin,andJudithGaspers.2022.ClassIncrementalLearningforIntentClassificationwithLimited
orNoOldData.InProceedingsoftheTheFirstWorkshoponEverEvolvingNLP(EvoNLP),FrancescoBarbieri,Jose
Camacho-Collados,BhuwanDhingra,LuisEspinosa-Anke,ElenaGribovskaya,AngelikiLazaridou,DanielLoureiro,and
LeonardoNeves(Eds.).AssociationforComputationalLinguistics,AbuDhabi,UnitedArabEmirates(Hybrid),16–25.
https://doi.org/10.18653/v1/2022.evonlp-1.4
BaolinPeng,ChunyuanLi,JinchaoLi,ShahinShayandeh,LarsLiden,andJianfengGao.2021.Soloist:BuildingTaskBots
atScalewithTransferLearningandMachineTeaching.TransactionsoftheAssociationforComputationalLinguistics9
(2021),807–824. https://doi.org/10.1162/tacl_a_00399
PatríciaPereira,HelenaMoniz,andJoaoPauloCarvalho.2022.DeepEmotionRecognitioninTextualConversations:A

### Survey.arXiv:2211.09172[cs.CL]

Xinyu Pi, Wanjun Zhong, Yan Gao, Nan Duan, and Jian-Guang Lou. 2022. LogiGAN: Learning Logical Reasoning via

### AdversarialPre-training.arXiv:2205.08794[cs.CL]

AnitaPomerantzandBarbaraJFehr.2011.Conversationanalysis:Anapproachtotheanalysisofsocialinteraction.Discourse
studies:Amultidisciplinaryintroduction2(2011),165–190.
SoujanyaPoria,DevamanyuHazarika,NavonilMajumder,GautamNaik,ErikCambria,andRadaMihalcea.2019.MELD:
AMultimodalMulti-PartyDatasetforEmotionRecognitioninConversations.InProceedingsofthe57thAnnualMeeting
oftheAssociationforComputationalLinguistics.AssociationforComputationalLinguistics,Florence,Italy,527–536.
https://doi.org/10.18653/v1/P19-1050
SoujanyaPoria,NavonilMajumder,DevamanyuHazarika,DeepanwayGhosal,RishabhBhardwaj,SamsonYuBaiJian,
PengfeiHong,RomilaGhosh,AbhinabaRoy,NiyatiChhaya,etal.2021.Recognizingemotioncauseinconversations.
CognitiveComputation13(2021),1317–1332.
BowenQin,BinyuanHui,LihanWang,MinYang,JinyangLi,BinhuaLi,RuiyingGeng,RongyuCao,JianSun,LuoSi,
etal.2022.ASurveyonText-to-SQLParsing:Concepts,Methods,andFutureDirections.arXivpreprintarXiv:2208.13629
(2022).
ZongfengQu,ZhitongYang,BoWang,andQinghuaHu.2024.TodBR:Target-OrientedDialogwithBidirectionalReasoning
onKnowledgeGraph.AppliedSciences14,1(2024),459.
JunQuan,DeyiXiong,BonnieWebber,andChangjianHu.2019.GECOR:AnEnd-to-EndGenerativeEllipsisandCoreferenceResolutionModelforTask-OrientedDialogue.InProceedingsofthe2019ConferenceonEmpiricalMethods
inNaturalLanguageProcessingandthe9thInternationalJointConferenceonNaturalLanguageProcessing(EMNLP-
IJCNLP).AssociationforComputationalLinguistics,HongKong,China,4547–4557. https://doi.org/10.18653/
v1/D19-1462

<!-- Page 32 -->

32 NaturalLanguageEngineering
L.RabinerandB.Juang.1986.AnintroductiontohiddenMarkovmodels.IEEEASSPMagazine3,1(1986),4–16. https:
//doi.org/10.1109/MASSP.1986.1165342
Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever, et al. 2018. Improving language understanding by
generativepre-training.(2018).
Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. 2019. Language models are
unsupervisedmultitasklearners.OpenAIblog1,8(2019),9.
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and
PeterJ.Liu.2020.ExploringtheLimitsofTransferLearningwithaUnifiedText-to-TextTransformer.J.Mach.Learn.
Res.21,1,Article140(jan2020),67pages.
Pranav Rajpurkar, Robin Jia, and Percy Liang. 2018. Know What You Don’t Know: Unanswerable Questions for
SQuAD.InProceedingsofthe56thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume2:Short
Papers).AssociationforComputationalLinguistics,Melbourne,Australia,784–789. https://doi.org/10.18653/
v1/P18-2124
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. 2016. SQuAD: 100,000+ Questions for Machine
ComprehensionofText.InProceedingsofthe2016ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.
AssociationforComputationalLinguistics,Austin,Texas,2383–2392. https://doi.org/10.18653/v1/D16-1264
RevanthRameshkumarandPeterBailey.2020.StorytellingwithDialogue:ACriticalRoleDungeonsandDragonsDataset.
InProceedingsofthe58thAnnualMeetingoftheAssociationforComputationalLinguistics,DanJurafsky,JoyceChai,
NatalieSchluter,andJoelTetreault(Eds.).AssociationforComputationalLinguistics,Online,5121–5134. https://
doi.org/10.18653/v1/2020.acl-main.459
Hannah Rashkin, Eric Michael Smith, Margaret Li, and Y-Lan Boureau. 2018. Towards Empathetic Open-domain
Conversation Models: A New Benchmark and Dataset. In Annual Meeting of the Association for Computational
Linguistics.
Hannah Rashkin, Eric Michael Smith, Margaret Li, and Y-Lan Boureau. 2019. Towards Empathetic Open-domain
ConversationModels:ANewBenchmarkandDataset.InProceedingsofthe57thAnnualMeetingoftheAssociation
forComputationalLinguistics.AssociationforComputationalLinguistics,Florence,Italy,5370–5381. https://doi.
org/10.18653/v1/P19-1534
Abhinav Rastogi, Xiaoxue Zang, Srinivas Sunkara, Raghav Gupta, and Pranav Khaitan. 2020. Towards Scalable Multi-
DomainConversationalAgents:TheSchema-GuidedDialogueDataset.ProceedingsoftheAAAIConferenceonArtificial
Intelligence34,05(Apr.2020),8689–8696. https://doi.org/10.1609/aaai.v34i05.6394
Siva Reddy, Danqi Chen, and Christopher D. Manning. 2019. CoQA: A Conversational Question Answering Challenge.
TransactionsoftheAssociationforComputationalLinguistics7(2019),249–266. https://doi.org/10.1162/tacl_
a_00266
Siva Reddy, Mirella Lapata, and Mark Steedman. 2014. Large-scale Semantic Parsing without Question-Answer Pairs.
TransactionsoftheAssociationforComputationalLinguistics2(2014),377–392. https://doi.org/10.1162/tacl_
a_00190
ShiyaRen,HuamingWang,DongmingYu,YuanLi,ZhixingLi,SHu,andLZou.2018.JointIntentDetectionandSlot
FillingwithRules.CCKSTasks2242(2018),34–40.
StephenRoller,EmilyDinan,NamanGoyal,DaJu,MaryWilliamson,YinhanLiu,JingXu,MyleOtt,EricMichaelSmith,
Y-LanBoureau,andJasonWeston.2021.RecipesforBuildinganOpen-DomainChatbot.InProceedingsofthe16th
ConferenceoftheEuropeanChapteroftheAssociationforComputationalLinguistics:MainVolume.Associationfor
ComputationalLinguistics,Online,300–325. https://doi.org/10.18653/v1/2021.eacl-main.24
JohannaRuusuvuori.2012.Emotion,affectandconversation.Thehandbookofconversationanalysis(2012),330–349.
TevenLeScao,AngelaFan,ChristopherAkiki,ElliePavlick,SuzanaIlic´,DanielHesslow,RomanCastagné,AlexandraSasha
Luccioni,FrançoisYvon,MatthiasGallé,etal.2022.Bloom:A176b-parameteropen-accessmultilinguallanguagemodel.
arXivpreprintarXiv:2211.05100(2022).
TorstenScholak,NathanSchucher,andDzmitryBahdanau.2021.PICARD:ParsingIncrementallyforConstrainedAuto-
RegressiveDecodingfromLanguageModels.InProceedingsofthe2021ConferenceonEmpiricalMethodsinNatural
LanguageProcessing.AssociationforComputationalLinguistics,OnlineandPuntaCana,DominicanRepublic,9895–
9901. https://doi.org/10.18653/v1/2021.emnlp-main.779
Hendrik Schuff, Lindsey Vanderlyn, Heike Adel, and Ngoc Thang Vu. 2023. How to do human evaluation: A brief
introduction to user studies in NLP. Natural Language Engineering (2023), 1–24. https://doi.org/10.1017/

## S1351324922000535

KarinSevegnani,DavidM.Howcroft,IoannisKonstas,andVerenaRieser.2021.OTTers:One-turnTopicTransitionsfor
Open-DomainDialogue.InProceedingsofthe59thAnnualMeetingoftheAssociationforComputationalLinguistics
andthe11thInternationalJointConferenceonNaturalLanguageProcessing(Volume1:LongPapers).Associationfor
ComputationalLinguistics,Online,2492–2504. https://doi.org/10.18653/v1/2021.acl-long.194
IgorShalyminov,SungjinLee,ArashEshghi,andOliverLemon.2019.Few-ShotDialogueGenerationWithoutAnnotated
Data:ATransferLearningApproach.InProceedingsofthe20thAnnualSIGdialMeetingonDiscourseandDialogue.

<!-- Page 33 -->


### LATEXSupplement 33

AssociationforComputationalLinguistics,Stockholm,Sweden,32–39. https://doi.org/10.18653/v1/W19-5904
IgorShalyminov,AlessandroSordoni,AdamAtkinson,andHannesSchulz.2020.FastDomainAdaptationforGoal-Oriented
DialogueUsingaHybridGenerative-RetrievalTransformer.InICASSP2020-2020IEEEInternationalConferenceon
Acoustics,SpeechandSignalProcessing(ICASSP).8039–8043. https://doi.org/10.1109/ICASSP40776.2020.
9053599
Weizhou Shen, Siyue Wu, Yunyi Yang, and Xiaojun Quan. 2021. Directed Acyclic Graph Network for Conversational
Emotion Recognition. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics
andthe11thInternationalJointConferenceonNaturalLanguageProcessing(Volume1:LongPapers).Associationfor
ComputationalLinguistics,Online,1551–1560. https://doi.org/10.18653/v1/2021.acl-long.123
NShikha,KaranNaidu,AntaraRoyChoudhury,andNKayarvizhy.2022.SmartMemoryCompanionforelderly.In20224th
InternationalConferenceonAdvancesinComputing,CommunicationControlandNetworking(ICAC3N).IEEE,1497–
1502.
JaminShin,PengXu,AndreaMadotto,andPascaleFung.2019.HappyBot:GeneratingEmpatheticDialogueResponsesby
ImprovingUserExperienceLook-ahead.ArXivabs/1906.08487(2019).
Michael Shum, Stephan Zheng, Wojciech Kryscinski, Caiming Xiong, and Richard Socher. 2020. Sketch-Fill-A-R: A
Persona-Grounded Chit-Chat Generation Framework. In Proceedings of the 2nd Workshop on Natural Language
ProcessingforConversationalAI.AssociationforComputationalLinguistics,Online,118–131. https://doi.org/
10.18653/v1/2020.nlp4convai-1.14
KurtShuster,JingXu,MojtabaKomeili,DaJu,EricMichaelSmith,StephenRoller,MeganUng,MoyaChen,KushalArora,
JoshuaLane,etal.2022.Blenderbot3:adeployedconversationalagentthatcontinuallylearnstoresponsiblyengage.
arXivpreprintarXiv:2208.03188(2022).
A.B. Siddique, Fuad Jamour, Luxun Xu, and Vagelis Hristidis. 2021. Generalized Zero-Shot Intent Detection via
Commonsense Knowledge (SIGIR ’21). Association for Computing Machinery, New York, NY, USA, 1925–1929.
https://doi.org/10.1145/3404835.3462985
XiaohuiSong,LongtaoHuang,HuiXue,andSonglinHu.2022.SupervisedPrototypicalContrastiveLearningforEmotion
Recognition in Conversation. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language
Processing. Association for Computational Linguistics, Abu Dhabi, United Arab Emirates, 5197–5206. https://
aclanthology.org/2022.emnlp-main.347
Aseem Srivastava, Ishan Pandey, Md Shad Akhtar, and Tanmoy Chakraborty. 2023. Response-Act Guided Reinforced
DialogueGenerationforMentalHealthCounseling.InProceedingsoftheACMWebConference2023(Austin,TX,USA)
(WWW’23).AssociationforComputingMachinery,NewYork,NY,USA,1118–1129. https://doi.org/10.1145/
3543507.3583380
Aseem Srivastava, Tharun Suresh, Sarah P. Lord, Md Shad Akhtar, and Tanmoy Chakraborty. 2022. Counseling
SummarizationUsingMentalHealthKnowledgeGuidedUtteranceFiltering.InProceedingsofthe28thACMSIGKDD
ConferenceonKnowledgeDiscoveryandDataMining(WashingtonDC,USA)(KDD’22).AssociationforComputing
Machinery,NewYork,NY,USA,3920–3930. https://doi.org/10.1145/3534678.3539187
Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario
Amodei, and Paul F Christiano. 2020. Learning to summarize with human feedback. In Advances in Neural
Information Processing Systems, H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin (Eds.), Vol. 33.
Curran Associates, Inc., 3008–3021. https://proceedings.neurips.cc/paper_files/paper/2020/file/
1f89885d556929e98d3ef9b86448f951-Paper.pdf
CarlStrathearnandDimitraGkatzia.2022.Task2Dial:ANovelTaskandDatasetforCommonsense-enhancedTask-based
DialogueGroundedinDocuments.InProceedingsoftheSecondDialDocWorkshoponDocument-groundedDialogue
andConversationalQuestionAnswering.AssociationforComputationalLinguistics,Dublin,Ireland,187–196. https:
//doi.org/10.18653/v1/2022.dialdoc-1.21
YixuanSu,DengCai,YanWang,SimonBaker,AnnaKorhonen,NigelCollier,andXiaojiangLiu.2020.Stylisticdialogue
generationviainformation-guidedreinforcementlearningstrategy.arXivpreprintarXiv:2004.02202(2020).
Alane Suhr, Ming-Wei Chang, Peter Shaw, and Kenton Lee. 2020. Exploring Unexplored Generalization Challenges for
Cross-DatabaseSemanticParsing.InAnnualMeetingoftheAssociationforComputationalLinguistics.
QingfengSun,YujingWang,CanXu,KaiZheng,YamingYang,HuangHu,FeiXu,JessicaZhang,XiuboGeng,andDaxin
Jiang.2022b.MultimodalDialogueResponseGeneration.InProceedingsofthe60thAnnualMeetingoftheAssociationfor
ComputationalLinguistics(Volume1:LongPapers).AssociationforComputationalLinguistics,Dublin,Ireland,2854–
2866. https://doi.org/10.18653/v1/2022.acl-long.204
YuqianSun,XuranNi,HaozhenFeng,RayLC,ChangHeeLee,andAliAsadipour.2022a.Bringingstoriestolifein1001
nights: Aco-creativetext adventuregame usingastory generationmodel. InInternationalConference onInteractive
DigitalStorytelling.Springer,651–672.
HaoTang,DonghongJi,andQijiZhou.2020.End-to-endmaskedgraph-basedCRFforjointslotfillingandintentdetection.
Neurocomputing413(2020),348–359. https://doi.org/10.1016/j.neucom.2020.06.113

<!-- Page 34 -->

34 NaturalLanguageEngineering
AbhaTewari,AmitChhabria,AjaySinghKhalsa,SanketChaudhary,andHarshitaKanal.2021.Asurveyofmentalhealth
chatbotsusingNLP.InProceedingsoftheInternationalConferenceonInnovativeComputing&Communication(ICICC).
RomalThoppilan,DanielDeFreitas,JamieHall,NoamShazeer,ApoorvKulshreshtha,Heng-TzeCheng,AliciaJin,Taylor
Bos,LeslieBaker,YuDu,YaGuangLi,HongraeLee,HuaixiuStevenZheng,AminGhafouri,MarceloMenegali,Yanping
Huang,MaximKrikun,DmitryLepikhin,JamesQin,DehaoChen,YuanzhongXu,ZhifengChen,AdamRoberts,Maarten
Bosma,VincentZhao,YanqiZhou,Chung-ChingChang,IgorKrivokon,WillRusch,MarcPickett,PraneshSrinivasan,
LaicheeMan,KathleenMeier-Hellstern,MeredithRingelMorris,TulseeDoshi,RenelitoDelosSantos,TojuDuke,Johnny
Soraker,BenZevenbergen,VinodkumarPrabhakaran,MarkDiaz,BenHutchinson,KristenOlson,AlejandraMolina,Erin
Hoffman-John,JoshLee,LoraAroyo,RaviRajakumar,AlenaButryna,MatthewLamm,ViktoriyaKuzmina,JoeFenton,
AaronCohen,RachelBernstein,RayKurzweil,BlaiseAguera-Arcas,ClaireCui,MarianCroak,EdChi,andQuocLe.

#### LaMDA:LanguageModelsforDialogApplications.arXiv:2201.08239[cs.CL]

HugoTouvron,ThibautLavril,GautierIzacard,XavierMartinet,Marie-AnneLachaux,TimothéeLacroix,BaptisteRozière,
NamanGoyal,EricHambro,FaisalAzhar,AurelienRodriguez,ArmandJoulin,EdouardGrave,andGuillaumeLample.

#### LLaMA:OpenandEfficientFoundationLanguageModels.arXiv:2302.13971[cs.CL]

EnricaTroiano,AswathyVelutharambath,andRomanKlinger.2023.Fromtheoriesonstylestotheirtransferintext:Bridging
thegapwithahierarchicalsurvey.NaturalLanguageEngineering29,4(2023),849–908. https://doi.org/10.1017/

## S1351324922000407

DonTuggener,MargotMieskes,JanDeriu,andMarkCieliebak.2021.AreWeSummarizingtheRightWay?ASurveyof
DialogueSummarizationDataSets.InProceedingsoftheThirdWorkshoponNewFrontiersinSummarization.Association
forComputationalLinguistics,OnlineandinDominicanRepublic,107–118. https://doi.org/10.18653/v1/2021.
newsum-1.12
ChrisvanderLee,AlbertGatt,EmielvanMiltenburg,andEmielKrahmer.2021.Humanevaluationofautomaticallygenerated text: Current trends and best practice guidelines. Computer Speech & Language 67 (2021), 101151. https:
//doi.org/10.1016/j.csl.2020.101151
HamsaShwethaVenkataram,ChrisAMattmann,andScottPenberthy.2020.TopiQAL:Topic-awareQuestionAnswering
using Scalable Domain-specific Supercomputers. In 2020 IEEE/ACM Fourth Workshop on Deep Learning on
Supercomputers(DLS).IEEE,48–55.
OriolVinyals,SamyBengio,andManjunathKudlur.2015.Ordermatters:Sequencetosequenceforsets.arXivpreprint
arXiv:1511.06391(2015).
TuVu,AdityaBarua,BrianLester,DanielCer,MohitIyyer,andNoahConstant.2022.OvercomingCatastrophicForgettingin
Zero-ShotCross-LingualGeneration.InProceedingsofthe2022ConferenceonEmpiricalMethodsinNaturalLanguage
Processing,YoavGoldberg,ZornitsaKozareva,andYueZhang(Eds.).AssociationforComputationalLinguistics,Abu
Dhabi,UnitedArabEmirates,9279–9300. https://doi.org/10.18653/v1/2022.emnlp-main.630
IvanVulic´,IñigoCasanueva,GeorgiosSpithourakis,AvishekMondal,Tsung-HsienWen,andPawełBudzianowski.2022.
Multi-Label Intent Detection via Contrastive Task Specialization of Sentence Encoders. In Proceedings of the 2022
Conference on Empirical Methods in Natural Language Processing. Association for Computational Linguistics, Abu
Dhabi,UnitedArabEmirates,7544–7559. https://aclanthology.org/2022.emnlp-main.512
KeiWakabayashi,JohaneTakeuchi,andMikioNakano.2022.RobustSlotFillingModelingforIncompleteAnnotations
usingSegmentation-BasedFormulation.TransactionsoftheJapaneseSocietyforArtificialIntelligence37,3(2022),IDS–

### E_1–12. https://doi.org/10.1527/tjsai.37-3_IDS-E

Bailin Wang, Richard Shin, Xiaodong Liu, Oleksandr Polozov, and Matthew Richardson. 2019b. RAT-SQL: Relation-
AwareSchemaEncodingandLinkingforText-to-SQLParsers.InAnnualMeetingoftheAssociationforComputational
Linguistics.
Jieyu Wang, Dingfang Kang, Abdullah AbuHussein, and Lynn A Collen. 2023a. Designing a Conversational Agent for
Education:APersonality-basedApproach.(2023).
YufanWang,TingtingHe,RuiFan,WenjiZhou,andXinhuiTu.2019a.EffectiveUtilizationofExternalKnowledgeand
HistoryContextinMulti-turnSpokenLanguageUnderstandingModel.In2019IEEEInternationalConferenceonBig
Data(BigData).960–967. https://doi.org/10.1109/BigData47090.2019.9006162
YanmengWang,WengeRong,JianfeiZhang,YuanxinOuyang,andZhangXiong.2020.KnowledgeGroundedPre-Trained
ModelForDialogueResponseGeneration.In2020InternationalJointConferenceonNeuralNetworks(IJCNN).1–8.
https://doi.org/10.1109/IJCNN48605.2020.9207054
Zhenduo Wang, Yuancheng Tu, Corby Rosset, Nick Craswell, Ming Wu, and Qingyao Ai. 2023b. Zero-shot Clarifying
QuestionGenerationforConversationalSearch.arXiv:2301.12660[cs.IR]
NickWebb.2000.Rule-baseddialoguemanagementsystems.InProceedingsofthe3rdInternationalWorkshoponHuman-
ComputerConversation,Bellagio,Italy.3–5.
JosephWeizenbaum.1966.ELIZA—aComputerProgramfortheStudyofNaturalLanguageCommunicationbetweenMan
andMachine.Commun.ACM9,1(jan1966),36–45. https://doi.org/10.1145/365153.365168
HenryWeld,XiaoqiHuang,SiquLong,JosiahPoon,andSoyeonCarenHan.2022a.ASurveyofJointIntentDetectionand
SlotFillingModelsinNaturalLanguageUnderstanding.ACMComput.Surv.55,8,Article156(dec2022),38pages.

<!-- Page 35 -->


### LATEXSupplement 35

https://doi.org/10.1145/3547138
HenryWeld,XiaoqiHuang,SiquLong,JosiahPoon,andSoyeonCarenHan.2022b.Asurveyofjointintentdetectionand
slotfillingmodelsinnaturallanguageunderstanding.Comput.Surveys55,8(2022),1–38.
Jason Weston, Antoine Bordes, Sumit Chopra, Alexander M. Rush, Bart van Merriënboer, Armand Joulin, and Tomas
Mikolov.2015.TowardsAI-CompleteQuestionAnswering:ASetofPrerequisiteToyTasks.arXiv:1502.05698[cs.AI]
JasonDWilliams.2003.Aprobabilisticmodelofhuman/computerdialoguewithapplicationtoapartiallyobservableMarkov
decisionprocess.PhDfirstyearreport.DepartmentofEngineering,UniversityofCambridge(2003).
Jason D Williams, Pascal Poupart, and Steve Young. 2005. Factored partially observable Markov decision processes for
dialoguemanagement.InProc.IJCAIWorkshoponKnowledgeandReasoninginPracticalDialogueSystems.Citeseer,
76–82.
Chien-Sheng Wu, Linqing Liu, Wenhao Liu, Pontus Stenetorp, and Caiming Xiong. 2021b. Controllable Abstractive
DialogueSummarizationwithSketchSupervision.InFindingsoftheAssociationforComputationalLinguistics:ACL-
IJCNLP 2021. Association for Computational Linguistics, Online, 5108–5122. https://doi.org/10.18653/v1/
2021.findings-acl.454
Hongyi Wu, Xinshu Shen, Man Lan, Shaoguang Mao, Xiaopeng Bai, and Yuanbin Wu. 2023b. A Multi-Task Dataset
for Assessing Discourse Coherence in Chinese Essays: Structure, Theme, and Logic Analysis. In Proceedings of the
2023ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,HoudaBouamor,JuanPino,andKalikaBali
(Eds.).AssociationforComputationalLinguistics,Singapore,6673–6688. https://doi.org/10.18653/v1/2023.
emnlp-main.412
JieWu,IanG.Harris,HongzhiZhao,andGuangmingLing.2023a.AGraph-to-SequenceModelforJointIntentDetection
andSlotFilling.In2023IEEE17thInternationalConferenceonSemanticComputing(ICSC).131–138. https://doi.
org/10.1109/ICSC56153.2023.00028
Tongtong Wu, Meng Wang, Huan Gao, Guilin Qi, and Weizhuo Li. 2019. Zero-Shot Slot Filling via Latent Question
RepresentationandReadingComprehension.InPRICAI2019:TrendsinArtificialIntelligence,AbhayaC.Nayakand
AlokSharma(Eds.).SpringerInternationalPublishing,Cham,123–136.
ZeqiuWu,MichelGalley,ChrisBrockett,YizheZhang,XiangGao,ChrisQuirk,RikKoncel-Kedziorski,JianfengGao,
HannanehHajishirzi,MariOstendorf,andBillDolan.2021a.AControllableModelofGroundedResponseGeneration.
ProceedingsoftheAAAIConferenceonArtificialIntelligence35,16(May2021),14085–14093. https://doi.org/
10.1609/aaai.v35i16.17658
RuiXiaandZixiangDing.2019.Emotion-CausePairExtraction:ANewTasktoEmotionAnalysisinTexts.InProceedings
ofthe57thAnnualMeetingoftheAssociationforComputationalLinguistics.AssociationforComputationalLinguistics,
Florence,Italy,1003–1012. https://doi.org/10.18653/v1/P19-1096
ShuwenXiao,ZhouZhao,ZijianZhang,XiaohuiYan,andMinYang.2020.Convolutionalhierarchicalattentionnetwork
forquery-focusedvideosummarization.InProceedingsoftheAAAIconferenceonartificialintelligence,Vol.34.12426–
12433.
YuboXieandPearlPu.2021.GeneratingEmpatheticResponseswithaLargeScaleDialogDataset.ArXivabs/2105.06829
(2021).
CanwenXu,DayaGuo,NanDuan,andJulianMcAuley.2023.Baize:AnOpen-SourceChatModelwithParameter-Efficient

### TuningonSelf-ChatData.arXiv:2304.01196[cs.CL]

Yan Xu, Etsuko Ishii, Samuel Cahyawijaya, Zihan Liu, Genta Indra Winata, Andrea Madotto, Dan Su, and Pascale
Fung.2022.Retrieval-FreeKnowledge-GroundedDialogueResponseGenerationwithAdapters.InProceedingsofthe
SecondDialDocWorkshoponDocument-groundedDialogueandConversationalQuestionAnswering.Associationfor
ComputationalLinguistics,Dublin,Ireland,93–107. https://doi.org/10.18653/v1/2022.dialdoc-1.10
YiXuandHaiZhao.2021.Dialogue-orientedPre-training.InFindingsoftheAssociationforComputationalLinguistics:
ACL-IJCNLP 2021. Association for Computational Linguistics, Online, 2663–2673. https://doi.org/10.18653/
v1/2021.findings-acl.235
ChaotingXuan.2020.ImprovingSequence-to-SequenceSemanticParserforTaskOrientedDialog.ProceedingsoftheFirst
WorkshoponInteractiveandExecutableSemanticParsing(2020).
Shiquan Yang, Xinting Huang, Jey Han Lau, and Sarah Erfani. 2022. Robust Task-Oriented Dialogue Generation with
ContrastivePre-trainingandAdversarialFiltering.InFindingsoftheAssociationforComputationalLinguistics:EMNLP
2022,YoavGoldberg,ZornitsaKozareva,andYueZhang(Eds.).AssociationforComputationalLinguistics,AbuDhabi,
UnitedArabEmirates,1220–1234. https://doi.org/10.18653/v1/2022.findings-emnlp.88
ShiquanYang,RuiZhang,andSarahErfani.2020.Graphdialog:Integratinggraphknowledgeintoend-to-endtask-oriented
dialoguesystems.arXivpreprintarXiv:2010.01447(2020).
Wen-tau Yih, Ming-Wei Chang, Xiaodong He, and Jianfeng Gao. 2015. Semantic Parsing via Staged Query Graph
Generation:QuestionAnsweringwithKnowledgeBase.InProceedingsofthe53rdAnnualMeetingoftheAssociation
forComputationalLinguisticsandthe7thInternationalJointConferenceonNaturalLanguageProcessing(Volume1:
LongPapers).AssociationforComputationalLinguistics,Beijing,China,1321–1331. https://doi.org/10.3115/
v1/P15-1128

<!-- Page 36 -->

36 NaturalLanguageEngineering
Wen-waiYimandMelihaYetisgen.2021.TowardsAutomatingMedicalScribing:ClinicVisitDialogue2NoteSentence
AlignmentandSnippetSummarization.InProceedingsoftheSecondWorkshoponNaturalLanguageProcessingfor
MedicalConversations,ChaitanyaShivade,RashmiGangadharaiah,SpandanaGella,SandeepKonam,ShaoqingYuan,
Yi Zhang, Parminder Bhatia, and Byron Wallace (Eds.). Association for Computational Linguistics, Online, 10–20.
https://doi.org/10.18653/v1/2021.nlpmc-1.2
PengchengYinandGrahamNeubig.2017.ASyntacticNeuralModelforGeneral-PurposeCodeGeneration.InProceedings
ofthe55thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers).Associationfor
ComputationalLinguistics,Vancouver,Canada,440–450. https://doi.org/10.18653/v1/P17-1041
Tom Young, Frank Xing, Vlad Pandelea, Jinjie Ni, and Erik Cambria. 2022. Fusing Task-Oriented and Open-Domain
DialoguesinConversationalAgents.ProceedingsoftheAAAIConferenceonArtificialIntelligence36,10(Jun.2022),
11622–11629. https://doi.org/10.1609/aaai.v36i10.21416
Tao Yu, Rui Zhang, Heyang Er, Suyi Li, Eric Xue, Bo Pang, Xi Victoria Lin, Yi Chern Tan, Tianze Shi, Zihan Li,
YouxuanJiang,MichihiroYasunaga,SungrokShim,TaoChen,AlexanderFabbri,ZifanLi,LuyaoChen,YuwenZhang,
ShreyaDixit,VincentZhang,CaimingXiong,RichardSocher,WalterLasecki,andDragomirRadev.2019.CoSQL:A
ConversationalText-to-SQLChallengeTowardsCross-DomainNaturalLanguageInterfacestoDatabases.InProceedings
ofthe2019ConferenceonEmpiricalMethodsinNaturalLanguageProcessingandthe9thInternationalJointConference
on Natural Language Processing (EMNLP-IJCNLP). Association for Computational Linguistics, Hong Kong, China,
1962–1979. https://doi.org/10.18653/v1/D19-1204
Tao Yu, Rui Zhang, Alex Polozov, Christopher Meek, and Ahmed Hassan Awadallah. 2021. {SC}oRe: Pre-Training for
ContextRepresentationinConversationalSemanticParsing.InInternationalConferenceonLearningRepresentations.
https://openreview.net/forum?id=oyZxhRI2RiE
TaoYu,RuiZhang,KaiYang,MichihiroYasunaga,DongxuWang,ZifanLi,JamesMa,IreneLi,QingningYao,Shanelle
Roman,ZilinZhang,andDragomirRadev.2018.Spider:ALarge-ScaleHuman-LabeledDatasetforComplexandCross-
DomainSemanticParsingandText-to-SQLTask.InProceedingsofthe2018ConferenceonEmpiricalMethodsinNatural
LanguageProcessing.AssociationforComputationalLinguistics,Brussels,Belgium,3911–3921. https://doi.org/
10.18653/v1/D18-1425
WenhaoYu,HongmingZhang,XiaomanPan,KaixinMa,HongweiWang,andDongYu.2023.Chain-of-Note:Enhancing
RobustnessinRetrieval-AugmentedLanguageModels.arXivpreprintarXiv:2311.09210(2023).
Idris Yusupov and Yurii Kuratov. 2018. NIPS Conversational Intelligence Challenge 2017 Winner System: Skill-based
Conversational Agent with Supervised Dialog Manager. In Proceedings of the 27th International Conference on
ComputationalLinguistics.AssociationforComputationalLinguistics,SantaFe,NewMexico,USA,3681–3692. https:
//aclanthology.org/C18-1312
Klaus Zechner and Alex Waibel. 2000. DIASUMM: Flexible Summarization of Spontaneous Dialogues in Unrestricted
Domains. In COLING 2000 Volume 2: The 18th International Conference on Computational Linguistics. https:
//aclanthology.org/C00-2140
HaolanZhan,HainanZhang,HongshenChen,ZhuoyeDing,YongjunBao,andYanyanLan.2021.AugmentingKnowledgegrounded Conversations with Sequential Knowledge Transition. In Proceedings of the 2021 Conference of the North
American Chapter of the Association for Computational Linguistics: Human Language Technologies. Association for
ComputationalLinguistics,Online,5621–5630. https://doi.org/10.18653/v1/2021.naacl-main.446
Qingyu Zhang, Xiaoyu Shen, Ernie Chang, Jidong Ge, and Pengke Chen. 2022. MDIA: A Benchmark for Multilingual

### DialogueGenerationin46Languages.arXiv:2208.13078[cs.CL]

SaizhengZhang,EmilyDinan,JackUrbanek,ArthurSzlam,DouweKiela,andJasonWeston.2018.PersonalizingDialogue
Agents: I have a dog, do you have pets too?. In Proceedings of the 56th Annual Meeting of the Association for
ComputationalLinguistics(Volume1:LongPapers).AssociationforComputationalLinguistics,Melbourne,Australia,
2204–2213. https://doi.org/10.18653/v1/P18-1205
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, and Yoav Artzi. 2020a. BERTScore: Evaluating Text
GenerationwithBERT.InInternationalConferenceonLearningRepresentations. https://openreview.net/forum?
id=SkeHuCVFDr
WanyingZhang,FengYang,andYanLiang.2019.ABayesianFrameworkforJointTargetTracking,Classification,and
IntentInference.IEEEAccess7(2019),66148–66156. https://doi.org/10.1109/ACCESS.2019.2917541
XiaoqiangZhang,YingChen,andGuangyingLi.2021.Multi-ModalSarcasmDetectionBasedonContrastiveAttention
Mechanism.InNaturalLanguageProcessingandChineseComputing.
Yusen Zhang, Yang Liu, Ziyi Yang, Yuwei Fang, Yulong Chen, Dragomir Radev, Chenguang Zhu, Michael Zeng, and
Rui Zhang. 2023. MACSum: Controllable Summarization with Mixed Attributes. Transactions of the Association for
ComputationalLinguistics11(2023),787–803. https://doi.org/10.1162/tacl_a_00575
YizheZhang,SiqiSun,MichelGalley,Yen-ChunChen,ChrisBrockett,XiangGao,JianfengGao,JingjingLiu,andBill
Dolan.2020b.DIALOGPT:Large-ScaleGenerativePre-trainingforConversationalResponseGeneration.InProceedings
ofthe58thAnnualMeetingoftheAssociationforComputationalLinguistics:SystemDemonstrations.Associationfor
ComputationalLinguistics,Online,270–278. https://doi.org/10.18653/v1/2020.acl-demos.30

<!-- Page 37 -->


### LATEXSupplement 37

ZhengZhang,RyuichiTakanobu,QiZhu,MinLieHuang,andXiaoYanZhu.2020c.Recentadvancesandchallengesin
task-orienteddialogsystems.ScienceChinaTechnologicalSciences63,10(2020),2011–2027.
ZhuoshengZhangandHaiZhao.2021.StructuralPre-trainingforDialogueComprehension.InProceedingsofthe59th
AnnualMeetingoftheAssociationforComputationalLinguisticsandthe11thInternationalJointConferenceonNatural
LanguageProcessing(Volume1:LongPapers).AssociationforComputationalLinguistics,Online,5134–5145. https:
//doi.org/10.18653/v1/2021.acl-long.399
ShubinZhao,AdamMeyers,andRalphGrishman.2004.DiscriminativeSlotDetectionUsingKernelMethods.InCOLING
2004:Proceedingsofthe20thInternationalConferenceonComputationalLinguistics.COLING,Geneva,Switzerland,
757–763. https://aclanthology.org/C04-1109
Weixiang Zhao, Yanyan Zhao, and Bing Qin. 2022. MuCDN: Mutual Conversational Detachment Network for Emotion
Recognition in Multi-Party Conversations. In Proceedings of the 29th International Conference on Computational
Linguistics.InternationalCommitteeonComputationalLinguistics,Gyeongju,RepublicofKorea,7020–7030. https:
//aclanthology.org/2022.coling-1.612
MingZhong,DaYin,TaoYu,AhmadZaidi,MutethiaMutuma,RahulJha,AhmedHassanAwadallah,AsliCelikyilmaz,
Yang Liu, Xipeng Qiu, and Dragomir Radev. 2021. QMSum: A New Benchmark for Query-based Multi-domain
MeetingSummarization.InProceedingsofthe2021ConferenceoftheNorthAmericanChapteroftheAssociationfor
Computational Linguistics: Human Language Technologies, Kristina Toutanova, Anna Rumshisky, Luke Zettlemoyer,
DilekHakkani-Tur,IzBeltagy,StevenBethard,RyanCotterell,TanmoyChakraborty,andYichaoZhou(Eds.).Association
forComputationalLinguistics,Online,5905–5921. https://doi.org/10.18653/v1/2021.naacl-main.472
VictorZhong,CaimingXiong,andRichardSocher.2017.Seq2SQL:GeneratingStructuredQueriesfromNaturalLanguage
usingReinforcementLearning.CoRRabs/1709.00103(2017).
CeZhou,QianLi,ChenLi,JunYu,YixinLiu,GuangjingWang,KaiZhang,ChengJi,QibenYan,LifangHe,etal.2023a.A
comprehensivesurveyonpretrainedfoundationmodels:Ahistoryfromberttochatgpt.arXivpreprintarXiv:2302.09419
(2023).
Kangyan Zhou, Shrimai Prabhumoye, and Alan W Black. 2018. A Dataset for Document Grounded Conversations.
In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing. Association for
ComputationalLinguistics,Brussels,Belgium,708–713. https://doi.org/10.18653/v1/D18-1076
LiZhouandKevinSmall.2020.Multi-domainDialogueStateTrackingasDynamicKnowledgeGraphEnhancedQuestion

### Answering.arXiv:1911.06192[cs.CL]

Pei Zhou, Karthik Gopalakrishnan, Behnam Hedayatnia, Seokhwan Kim, Jay Pujara, Xiang Ren, Yang Liu, and Dilek
Hakkani-Tur.2022.Thinkbeforeyouspeak:Explicitlygeneratingimplicitcommonsenseknowledgeforresponsegeneration.InProceedingsofthe60thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:Long
Papers).1237–1252.
YunhuaZhou,JianqiangYang,PengyuWang,andXipengQiu.2023b.TwoBirdsOneStone:DynamicEnsembleforOOD
IntentClassification.InProceedingsofthe61stAnnualMeetingoftheAssociationforComputationalLinguistics(Volume
1:LongPapers).10659–10673.
Chenguang Zhu, Yang Liu, Jie Mei, and Michael Zeng. 2021. MediaSum: A Large-scale Media Interview Dataset for
Dialogue Summarization. In Proceedings of the 2021 Conference of the North American Chapter of the Association
forComputationalLinguistics:HumanLanguageTechnologies,KristinaToutanova,AnnaRumshisky,LukeZettlemoyer,
DilekHakkani-Tur,IzBeltagy,StevenBethard,RyanCotterell,TanmoyChakraborty,andYichaoZhou(Eds.).Association
forComputationalLinguistics,Online,5927–5934. https://doi.org/10.18653/v1/2021.naacl-main.474

## Tables

**Table (Page 7):**

|  | Task | Datasets | Input |  |  |  |  |  |  |  |  |  |  | Output |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  | Implicit |  |  |  |  |  | Explicit |  |  |  |  | Implicit |  |  |  |  |  |  |  |  |  |  |
|  |  |  | User’sgoal |  | Domain |  | Context |  | Modality |  | Knowledge |  |  | Type |  | Style |  |  |  | Modality |  |  |  |  |
|  |  |  | CC | OG | nepO | cpS | TS | TM | U | M | enoN | rtsnU | rtS | CC | OG | gnE | fnI | rtsnI | pmE | U | M | rohS | gnoL |  |
| noitamrofsnarT | DR | CANARD(Elgoharyetal.2019) | ✓ | - | ✓ | - | - | ✓ | ✓ | - | ✓ | - | - | ✓ | - | ✓ | ✓ | - | - | ✓ | - | - | ✓ | - |
|  | DS | DialogSum(Chenetal.2021b) SAMSumCorpus(Gliwaetal.2019) | ✓ ✓ | - - | ✓ ✓ | - - | - - | ✓ ✓ | ✓ ✓ | - - | ✓ ✓ | - - | - - | ✓ ✓ | - - | ✓ ✓ | - - | - - | - - | ✓ ✓ | - - | - - | ✓ ✓ | - - |
|  | D2S | CoSQL(Yuetal.2019) SPIDER(Yuetal.2018) TOP(Guptaetal.2018) | - - - | ✓ ✓ ✓ | - - - | ✓ ✓ ✓ | ✓ ✓ ✓ | - - - | ✓ ✓ ✓ | - - - | - - ✓ | - - - | ✓ ✓ - | - - - | ✓ ✓ ✓ | - - - | - - ✓ | ✓ ✓ - | - - - | ✓ ✓ ✓ | - - - | - - ✓ | - - - | ✓ ✓ - |
| noitarenegesnopseR | QA | CMUDoG(Zhouetal.2018) CoQA(Reddyetal.2019) ClariQ(Aliannejadietal.2020) Mutual(Cuietal.2020) | - - - ✓ | ✓ ✓ ✓ - | ✓ - ✓ ✓ | - ✓ - - | - - - - | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ | - - - - | - - - ✓ | ✓ ✓ ✓ - | - - - - | - - - ✓ | ✓ ✓ ✓ - | - - - ✓ | ✓ ✓ ✓ - | - - - - | - - - - | ✓ ✓ ✓ ✓ | - - - - | - - - ✓ | ✓ ✓ ✓ ✓ | - - - - |
|  | KGR | ConvAI(YusupovandKuratov2018) Doc2Dial(Fengetal.2020) PersonaChat(Zhangetal.2018) bAbI(Westonetal.2015) FaithDial(Dzirietal.2022) OpenDialKG(Moonetal.2019) Task2Dial(StrathearnandGkatzia2022) | - - ✓ - ✓ - - | ✓ ✓ - ✓ - ✓ ✓ | ✓ - ✓ - ✓ - - | - ✓ - ✓ - ✓ ✓ | - - - - - - - | ✓ ✓ ✓ ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ ✓ ✓ ✓ | - - - - - - - | - - - - - - - | ✓ ✓ ✓ - ✓ - ✓ | - - - ✓ - ✓ - | - - ✓ - ✓ - - | ✓ ✓ - ✓ - ✓ ✓ | - - ✓ - ✓ ✓ - | ✓ ✓ - ✓ - - ✓ | - - - ✓ - - ✓ | - - - - ✓ - - | ✓ ✓ ✓ ✓ ✓ ✓ ✓ | - - - - - - - | - - - ✓ - - - | ✓ ✓ ✓ ✓ ✓ ✓ ✓ | - - - - - - - |
|  | CC | OTTers(Sevegnanietal.2021) ProsocialDialog(Kimetal.2022c) FusedChat(Youngetal.2022) mDIA(Zhangetal.2022) SODA(Kimetal.2022a) Switchboard-1(Jurafskyetal.1997) | ✓ ✓ - ✓ ✓ ✓ | - - ✓ - - - | ✓ ✓ - ✓ ✓ ✓ | - - ✓ - - - | - - - - - - | ✓ ✓ ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ ✓ ✓ | - - - - - - | ✓ - - ✓ - ✓ | - ✓ - - ✓ - | - - - - - - | ✓ ✓ - ✓ ✓ ✓ | - - ✓ - - - | ✓ ✓ - ✓ ✓ ✓ | - ✓ ✓ - ✓ - | - - - - - - | - ✓ - - ✓ - | ✓ ✓ ✓ ✓ ✓ ✓ | - - - - - - | - - ✓ - ✓ ✓ | ✓ ✓ ✓ ✓ ✓ ✓ | - - - - - - |
|  | TOD | UbuntuDialogueCorpus(Loweetal.2015) ABCD(Chenetal.2021a) BiTOD(Linetal.[n.d.]) CraiglistBargains(Heetal.2018) DeliData(Karadzhovetal.2021) MetalWOz(Shalyminovetal.2019) | - - - - - - | ✓ ✓ ✓ ✓ ✓ ✓ | - - - - ✓ - | ✓ ✓ ✓ ✓ - ✓ | - - - - - - | ✓ ✓ ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ ✓ ✓ | - - - - - - | ✓ - ✓ - - ✓ | - - - - - - | - ✓ - ✓ ✓ - | - - - - - - | ✓ ✓ ✓ ✓ ✓ ✓ | - - - ✓ - - | ✓ ✓ ✓ ✓ ✓ ✓ | ✓ ✓ - - ✓ - | - - - - - - | ✓ ✓ ✓ ✓ ✓ ✓ | - - - - - - | - - ✓ - - - | ✓ ✓ ✓ ✓ ✓ ✓ | - - - - - - |
|  | ID | Banking77(Casanuevaetal.2020) CLINC150(Larsonetal.2019) HWU64(Liuetal.2021c) SGD(Rastogietal.2020) | - - - - | ✓ ✓ ✓ ✓ | - - - - | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ | - - - - | ✓ ✓ ✓ ✓ | - - - - | ✓ ✓ ✓ ✓ | - - - - | - - - - | - - - - | ✓ ✓ ✓ ✓ | - - - - | ✓ ✓ ✓ ✓ | - - - - | - - - - | ✓ ✓ ✓ ✓ | - - - - | ✓ ✓ ✓ ✓ | - - - - | - - - - |
|  | SF | Restaurant8k(Coopeetal.2020) | - | ✓ | - | ✓ | ✓ | - | ✓ | - | ✓ | - | - | - | ✓ | - | ✓ | - | - | ✓ | - | ✓ | - | - |
|  | DST | MultiWOZ2.1(Ericetal.2020) | - | ✓ | - | ✓ | - | ✓ | ✓ | - | ✓ | - | - | - | ✓ | - | ✓ | ✓ | - | ✓ | - | ✓ | ✓ | - |
|  | AD | DailyDialogue(Lietal.2017) MELD(Poriaetal.2019) MUStARD(Castroetal.2019) EmpatheticDialogues(Rashkinetal.2018) | ✓ ✓ ✓ ✓ | - - - - | ✓ ✓ ✓ ✓ | - - - - | - - - - | ✓ ✓ ✓ ✓ | ✓ - - ✓ | - ✓ ✓ - | ✓ ✓ ✓ - | - - - - | - - - - | ✓ ✓ ✓ ✓ | - - - - | ✓ ✓ ✓ ✓ | - - - - | - - - - | ✓ ✓ - ✓ | ✓ ✓ ✓ ✓ | - - - - | ✓ ✓ ✓ - | ✓ ✓ ✓ ✓ | - - - - |


**Table (Page 16):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Ubuntu Dialogue Corpus S | ODA ConvAI3: C bAbI Proso Dialo | lariQ |  |  |  |  |
|  |  | cialDialog MetaLWOz DialoGLUE- Banking77 GLUE- TOP DialoGLUE- CLINC150 | Empathetic Dialogues |  | PersonaChat SAMSu |  |
|  |  |  | OpenDialKG | DialoGLUE- HWU64 |  | mDIA Dia |
|  |  |  | DialogSum | FusedChat |  | Mutual DialoGLUE- DSTC8 SGD |
|  |  |  | DailyDialogue DialoGLUE- Restaurant8k | ABCD SPIDER |  | CraiglistBargains Doc2Dial FaithDial BiTOD |


**Table (Page 17):**

| Generative |  |
|---|---|
| Transformative | DialogueResponse |
| DR DS D2S CANARD SAMSum TOP | QA KGR CC TOD ClariQ Doc2Dial PersonaChat ABCD |
| 90.15 51.33 64.68 88.64 49.97 63.81 86.66 47.12 59.26 79.1 41.6 59.65 81.39 44.82 60.11 | 49.13 39.9 40.13 51.03 47.98 38.98 41.76 51.95 45.11 39.13 39.82 50.31 41.88 35.11 36.88 47.64 44.39 36.64 38.05 48.29 |
| 91.53 52.79 66.34 | 51.22 40.6 42.65 52.16 |


**Table (Page 18):**

| DR | DS | D2S | QA | KGR | CC |
|---|---|---|---|---|---|
| Flu Rel Coh | Flu Rel Coh | Flu Rel Coh | Flu Rel Coh | Flu Rel Coh | Flu Rel Coh |
| 3.6 3.4 3.8 | 2.6 2.5 2.9 | 3.4 3.1 2.7 | 2.1 2.5 2.1 | 2.3 2.1 2.1 | 2.2 2.3 2.1 |
| 3.9 3.8 4.1 | 3.1 2.9 3.2 | 3.6 3.5 3.1 | 2.4 2.6 2.3 | 2.8 2.5 2.4 | 2.6 2.7 2.4 |


**Table (Page 20):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 20):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
