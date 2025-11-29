---
title: "Causal Explanations Sequential Decision"
original_file: "./Causal_Explanations_Sequential_Decision.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["exit", "right", "causes", "page", "decelerate", "left", "accelerate", "faster", "future", "present"]
summary: "<!-- Page 1 -->


### Causal Explanations for Sequential


### Decision-Making in Multi-Agent Systems


### BalintGyevnar ChengWang ChristopherG.Lucas

UniversityofEdinburgh UniversityofEdinburgh UniversityofEdinburgh
Edinburgh,UnitedKingdom Edinburgh,UnitedKingdom Edinburgh,UnitedKingdom
balint.gyevnar@ed.ac.uk cheng.wang@ed.ac.uk c.lucas@ed.ac.uk

### ShayB.Cohen StefanoV.Albrecht


### UniversityofEdinburgh UniversityofEdinburgh

Edinburgh,UnitedKingdom Edinburgh,UnitedKingdom
scohen@inf.ed.a"
related_documents: []
---

# Causal Explanations Sequential Decision

<!-- Page 1 -->


### Causal Explanations for Sequential


### Decision-Making in Multi-Agent Systems


### BalintGyevnar ChengWang ChristopherG.Lucas

UniversityofEdinburgh UniversityofEdinburgh UniversityofEdinburgh
Edinburgh,UnitedKingdom Edinburgh,UnitedKingdom Edinburgh,UnitedKingdom
balint.gyevnar@ed.ac.uk cheng.wang@ed.ac.uk c.lucas@ed.ac.uk

### ShayB.Cohen StefanoV.Albrecht


### UniversityofEdinburgh UniversityofEdinburgh

Edinburgh,UnitedKingdom Edinburgh,UnitedKingdom
scohen@inf.ed.ac.uk s.albrecht@ed.ac.uk

## Abstract


### WepresentCEMA:CausalExplanationsinMulti-Agentsystems;

aframeworkforcreatingcausalnaturallanguageexplanationsof
anagent’sdecisionsindynamicsequentialmulti-agentsystemsto
buildmoretrustworthyautonomousagents.Unlikepriorworkthat
assumesafixedcausalstructure,CEMAonlyrequiresaprobabilisticmodelforforward-simulatingthestateofthesystem.Usingsuch Figure1:Theautonomousvehicle(𝜀)isheadingtotheblue
amodel,CEMAsimulatescounterfactualworldsthatidentifythe goal.Itdecidedtochangelanesaftertheothervehicle(1)
salientcausesbehindtheagent’sdecisions.WeevaluateCEMAon cutinfrontofitandbegantoslowdown.Apassengerasks:
thetaskofmotionplanningforautonomousdrivingandtestitin Whydidyouchangelanes? “Todecreasethetimetoreach
diversesimulatedscenarios.WeshowthatCEMAcorrectlyandro- thegoal.”[teleological]Whywaschanginglanesfaster?“Bebustlyidentifiesthecausesbehindtheagent’sdecisions,evenwhen causetheothervehicleisslowerthanusandisdecelerating.”
alargenumberofotheragentsispresent,andshowviaauserstudy [mechanistic]–ActualexplanationsbyCEMAwithexplanathatCEMA’sexplanationshaveapositiveeffectonparticipants’ tiontypesinbrackets.Blue/orangelinesillustrateforward
trustinautonomousvehiclesandareratedashighashigh-quality simulationsusingtheprobabilisticforwardmodel.
baselineexplanationselicitedfromotherparticipants.Werelease
thecollectedexplanationswithannotationsastheHEADDdataset.
MostXAImethodsfocusonexplanationsforsupervisedlearning

## Keywords

usingtabularorimagedata[8].However,theseexplanationsare
ExplainableAI;human-centricXAI;multi-agentsystems;autonomous oftenpurelynumeric,andalonehavelittleutilityfornon-experts
vehicles;causalexplanations;dataset wholackdomainknowledgetounderstandthesystem’sinternal
representations[13].Toaddressthis,XAIisincreasinglydrawing

### ACMReferenceFormat:

inspirationfromphilosophyandthesocialsciences[28]whichhas
BalintGyevnar,ChengWang,ChristopherG.Lucas,ShayB.Cohen,andStefanoV.Albrecht.2024.CausalExplanationsforSequentialDecision-Making createdwhatwecallthesubfieldofsocialXAI.
inMulti-AgentSystems.InProc.ofthe23rdInternationalConferenceon AnessentialpartofsocialXAIistheabilitytogeneratecausal
AutonomousAgentsandMultiagentSystems(AAMAS2024),Auckland,New explanations.Thereareseveralmethodsforthistask[39]andsome
Zealand,May6–10,2024,IFAAMAS,31pages. wereproposedforcausallyexplainingsequentialdecision-making
insingle-agentsystems[9,40].However,complexanddynamic
1 INTRODUCTION multi-agent systems, such as the case with AD, involve tightly
ArtificialIntelligence(AI)issubjecttoheightenedsocialandregu- coupledinteractionsamongagentswherethedecisionsofanyone
latoryscrutinywheretrust,oralackthereof,hasprovenabarrier agentmaybedifficulttoexplainevenforhumans,andtherehave
topublicadoption[22],especiallyinsafety-criticalsystemssuchas been few works in XAI addressing this problem. An additional
autonomousdriving(AD)[18].Thisisinpartattributedtotheinher- importantfeatureofsocialXAIistheabilitytocommunicatethe
entlackoftransparencyofcurrentblackboxdeeplearning-based extractedcausesintheformofintelligibleandeasytounderstand
systems[3].Inresponse,explainableAI(XAI)hasgainedpopularity. naturallanguageexplanations(NLE)aspartofaconversational
process.Aconversationletsuserstargetthepertinentorunclear
actions of the agent, while a social XAI system can adjust the

### ThisworkislicensedunderaCreativeCommonsAttribution

International4.0License. user’smentalmodelwithoutexcessivecognitiveoverhead,thereby
contributingtomoretrustworthyinteractionswithpeople[11].
Proc.ofthe23rdInternationalConferenceonAutonomousAgentsandMultiagentSystems Toadvancethesocialexplainabilityofmulti-agentsystems,we
(AAMAS2024),N.Alechina,V.Dignum,M.Dastani,J.S.Sichman(eds.),May6–10,2024,
introduceanewmethodcalledCEMA,whichstandsforCausal
Auckland,NewZealand.©2024InternationalFoundationforAutonomousAgentsand
MultiagentSystems(www.ifaamas.org). ExplanationsinMulti-Agentsystems.AsillustratedinFigure1,
4202
beF
41
]IA.sc[
4v90801.2032:viXra

<!-- Page 2 -->

CEMAisasocialXAImethodthatgeneratesintelligiblecausalNLEs First,itischallengingtomodelallcausalfactorsinthesystem,such
aboutanegoagent’sdecisionsinsequentialmulti-agentsystems asthestate,action,orrewardinfluences,whilekeepingtheSCM
bothintermsoftheego’sintrinsicmotivations(i.e.,teleological interpretableandusefulforendusers.Second,theSCMmaygrowto
explanation)andtheactionsofotheragentsintheego’sneigh- intractablesizesdependingonthedesiredcoverageofcausalfactors
borhood(i.e.,mechanisticexplanation).AtthecoreofCEMAisa andthecomplexityofthesystem.Third,duetothetemporaland
novelcausalselectionalgorithmbasedontheCounterfactualEffect non-stationarynatureofdynamicsystems,anSCMmayfrequently
SizeModel[34],whichbuildsonalargebodyofresearchintohow needtoberecomputedtoadapttochanges.Thus,existingwork
peopleselectcausesforexplanations.Insteadofcreatingaspecific hasappliedSCMsonlyinsimplersingle-agentsystemswhere,e.g.,
fixedcausalstructure,CEMAonlyreliesonaprobabilisticmodel theagentistrainedwithaspecificalgorithm[27,29].
forforward-simulatingthejointstateofthesystem,whichmakes Inaddition,AImodelshavegrowncomplexenoughthatgenitgenerallyapplicablewheresuchmodelsareavailable.Bycreating eratingexplanationsby“openingtheblackbox”,i.e.,relyingon
counterfactualsimulationsofwhathasoccurred,CEMAranksthe anunderstandingoftheintrinsiccausalpropertiesofthetrained
salientcausesbehindtheego’sactionsbasedonwhichcausesare model,isofteninfeasible[42].Instead,wecanrelyonthecountermostcorrelatedwiththeego’sactionsacrosscounterfactualworlds. factualmodelofcausation,whichisawell-understoodformulation
Causalselectionfollowsathree-stepprocess: of causation in philosophical literature [19, 24]. Counterfactual
(1) Rollbackthecurrentfactualstateofthesystemtoaprevi- casesuncovercausesinrelationtothefactualcasebyhighlighting
ouspointintime,suchthattheactionsoftheegothatwe eventswhoseabsenceresultedinthecounterfactualcaserather
wouldliketoexplainhavenotyetoccurred; thanthefactualcase.Implementingthecounterfactualmodelof
(2) Simulateasetofcounterfactualworldsfromthispasttime causationforcomplexmulti-agentsystemsischallenginginpracpointusingaprobabilisticforwardmodelofthesystem; tice.WerelyonQuillienandLucas[34]’sCounterfactualEffect
(3) Calculatethecounterfactualcausaleffectsizebycorrelating SizeModelwhichisanempiricallyvalidatedmodeltooperationaltheego’sactionswithchangesinitsrewardsandactionsof izecausalselectionbasedontwoassumptionsabouthowhumans
otheragentsacrosscounterfactuals. themselvesmightselectcausesforexplanations.First,peoplecognitivelysimulatecounterfactualworldsbysamplingfromadistribu-
WeevaluateCEMAonADusingdiversesimulateddrivingscetionoverpossiblealternativeworldsthataregroundedin,i.e.,not
nariosfromtheliteraturewithexpertexplanations[1],weshow
toodifferentfromthefactualworld.Second,peopleapproximate
thatCEMAcorrectlyselectscausesoftheego’sdecisionsthatare
causaleffectsizesbycorrelatingvariables(i.e.,potentialcauses)in
congruentwiththeexpertexplanations,evenwhenalargenumber
theworldwiththepresenceofanoutcomeacrosscounterfactual
ofagentsarepresent.WeshowthatCEMAisrobusttochangesin
simulations.Thismeansthatifwehaveaprobabilisticmodelfor
thenumberofcounterfactualsimulationsandtheaccuracyofthe
forward-simulatingamulti-agentsystemthenwecanrankand
predictiveforwardmodel.Wealsoperformauserstudytomeasure
selectthemostimportantcausesbehindtheegoagent’sactionsby
theperceivedqualityandeffectsofCEMA’sexplanationsonpeople.
simulatingcounterfactuals.
First,wecollectasetofhigh-qualityhuman-writtenexplanations
Furthermore,howacauseisusedfortheexplanationdetermines
asourbaseline.WethenshowthatCEMA’sexplanationsarerated
itsexplanatorymode.WeconsiderAristotle’ssystemasitstoodthe
onaverageatleastashighasthisbaselinewhilepositivelyaffecting
participants’trustinAD.Insummary,ourcontributionsare:1 testoftimeandisstillfrequentlyusedinthemoderndiscourseof
philosophyofexplanations[26].Aristotlearguedforfourmodes:
• CEMA:aframeworktogenerateintelligiblecausalexplanamechanistic,teleological,material,andformal[16].Themechanistionsofthedecisionsofanegoagentindynamicmulti-agent
ticmodegivesanexplanationdescribingthemechanismsofthe
systemsbasedontheCounterfactualEffectSizeModel[34];
causeofachange,whiletheteleological modeexplainstowhat
• EvaluationofCEMAonmotionplanningforAD,showing
endorgoalachangehasoccurred.ForexampleinFigure1,“other
itsabilitytorobustlyidentifycorrectcausesevenwhena
vehicleslowingdown”isamechanisticcausewhile“reachinggoal
largenumberofagentsarepresent;
faster”isateleologicalcausebehindthedecisionoftheblueau-
• HEADD:adatasetofHumanExplanationsforAutonomous
tonomousvehicletochangelanes.Thematerialandformalmodes

### DrivingDecisionsconsistingofhuman-writtenexplanations

stayconstantinthesystemswestudy,sowedonotconsiderthem.
withaminimumof5uniqueannotationsregardingthecausal
Anincreasingbodyofliteraturestudiesthegenerationofexplacontentandtrustworthinessoftheexplanations[15];
nationsforsequentialdecision-making.However,mostmethods
• User study showing CEMA’s explanations are ranked at
focusondeterministicplanninginwell-defineddomains[9].Prior
leastashighashumanexplanationsandapositiveeffectof
workinexplainablereinforcementlearningdoesaddresssingleand
CEMA’sexplanationsontrustinAD.
multi-agentsettingsindynamicsystems[33],butcausalmethods
aresparser.Madumaletal.[27]isthefirsttotakeacausalapproach

## 2 Backgroundandrelatedwork

bybuildinganSCMfortheaction-influenceofagentsinmodel-free
Causalityisacornerstoneofusefulhuman-centricexplanations.A RL,whileNashedetal.[29]generatesexplanationbymappingthe
commonapproachforcausalselectionistofirstmodelthesystem algorithmicprocessofsolvingaMarkovDecisionProcessintoan
intheformofastructuralcausalmodel(SCM)[32],butthishas SCM.Othersusesurrogateinterpretablerepresentationsofagents’
somedrawbacksforcomplexanddynamicallyevolvingsystems. policieswith,e.g.,decisiontrees[38]andprograms[41].Weare
1CEMAavailableat:https://github.com/uoe-agents/cema notawareofmethodsforsocialXAIinmulti-agentsystems.
HEADDavailableat:https://datashare.ed.ac.uk/handle/10283/8714

<!-- Page 3 -->


### WeuseADforevaluation,whereprobabilisticmodelsforfor-

Human-Agent Interface Environment Human-Agent Interface Environment
wardsimulatingthesystemarewidelyavailable[5].GoalrecognitionmethodspredCicotuonttheerrfaagcetunatsl ’Cfuatuusreals tSaetelesc[6ti,o7n],whilemotion Counterfactual Causal Selection
planninggeneratesoptimalbehaviorforagents[1,17].SocialXAI
alsoreceivedsomQeuaettreyntioninAFiDlte.rForexOambspelrev,aZtihoannsgetal.[44] Query Filter Observations
foundthatexplanationsintermsofpurelyhigh-leveltacticalcauses

### Rollback Rollback

(e.g.,lanechange,turn)hadlittleeffectondrivers’trust,therefore,
morefine-grai P n r e o d ba in b s il i i g st h ic t sareSraemqpuliered, C e. o g u ., n i te n rf t a e c r t m ua s l ofrelative Probabilistic Model Simulate Cnt.factual Worlds

### Model Worlds

positionoracceleration.Howe C v a e l r c , u p la ri t o e rmethodsforsocialXAIin Calculate
ADdonotconsiderthesequentialnatureofdecision-making[30], Cnt.factual Causal

### Causal Select Explanatory Rank Features

relyonacomplexneuralmodelwhichisimpossibletocertifyfor Effect Size

### Attributions & Rank Features

safety[23],oronlyprovidehigh-levelexplanations[14].
Figure2:First,irrelevantobservationsarefilteredoutbased

## 3 Cema:Causalexplanationsin

onthequery.Second,CEMArollsbackthefilteredobser-

## Multi-Agentsystems

vationstoaprevioustimestepsothatthequeriedactionis
WeassumethatCEMAfunctionsingoal-basedsequentialmulti- erased.Fromthen,CEMAsimulatescounterfactualworldsto
agentsystemswithpartialobservability,andfollowthesystem calculatethecounterfactualcausaleffectsizeforthequeried
definitionofAlbrechtetal.[1].LetIbethesetofindexedagents actions,whichareusedtorankthefeaturesofthesystem.
in the environment. At timestep𝑡 ∈ N, each agent𝑖 ∈ I is in
localstate𝑠 𝑡 𝑖 ∈ S𝑖 andreceivesalocalobservation𝑜 𝑡 𝑖 ∈ O𝑖 that
probabilisticallydependson𝑠
𝑡
𝑖 through𝑝(𝑜
𝑡
𝑖 |𝑠
𝑡
𝑖).Inaddition,agent Thequestionisparsedbyanexternalhuman-agentinterfaceintoa
𝑖 selectsanaction𝑎𝑖 𝑡 ∈ A𝑖 inreactiontoobservationsthrough machine-readablequery,denoted𝑞,encodingadescriptionofthe
𝑝 S t ( h 𝑜 ( a 𝑎 𝑖 𝑎 = t , 𝑖 𝑡 . a × | . g 𝑖 . 𝑜 e S , 𝑖 1 n 𝑜 : 𝑖 𝑡 t 𝑏 𝑖 ) a 𝑖 ) , n . i w s d T h a h s i e i e m m re j i i o n l t a i h g n r e l t t y o n s o f t r o a t e a r t a e t 𝑜 c io h 𝑡 o n f a ∈ 𝑜 a g 𝑎 𝑖 O l o l :𝑏 a a a l d g n 𝐺 e e d n n 𝑖 𝑎 o t ⊂ s 𝑡 te i ∈ S s s a 𝑖 A d t e d u . n e p F fi o l u n e t r e e f t d o d h r e 𝑠 a 𝑡 t r s h , ∈ w a e n s e S y e a q p w s u s a h e u r n e t m i c r a e e e l s H a s p t t c a a e a t s t r i t t o e e e ( s n , 𝑣 s 𝑢 𝑠 . e 1 < I i q : r s 𝑡 r u 𝑡 t e b e ) h l a , e n e s t v c h e s a e d t e n a n 𝑠 o ˆ t r 𝑢 t n w s :𝑣 t t 𝑠ˆ i e a 𝑢 m t t c : h e 𝑣 e a s a . s n t F t m e o i c g p a r o n y a e r o r x n b r e a d e e s m p 𝑣 t s h p o t i a e s l n e t n t d e , h s i s fi e f a l t 𝑠ˆ t fi f o 𝑢 e t n : r e 𝑣 t e a r h d r l t e e t i o i f m m e e u g r e t e s s o s f t t ’ r t e o s e o p p m a q 𝑣 n u o . t e f a h T r t c e h i h t e i e e o o d b q q n a s u u i e c e e n r t r r v i t i i o h e e e n d d d e .
𝐺 lo 𝑖 ca m l a s y ta n te ot d b es e c o ri b p s t e io rv n a , b s l u e c t h o a o s th d e e r st a in ge a n ti t o s n .I c f o a o s r t d a i t n e a s te e s q . u T e h n e ce g 𝑠 o 1 a :𝑡 l a h c y t p io o n th 𝑠ˆ e 𝑢 t : i 𝑣 ca n l e s e e d q n u o e t n b c e e a th s a u t b a s p e p qu ea e r n s c , e e o .g f ., 𝑠 1 in :𝑡, a in c s o t u e n ad te i r t fa c c a t n u a a l l s w o o b r e ld a .
achieves𝐺𝑖 foragent𝑖,itreceivesreward𝑅𝑖(𝑠 1:𝑡) ∈R𝑑 whichisa
Thisallowstheusertoaskcontrastivequestions,forexampleofthe
𝑑-dimensionalvectorofrewardvalueswhereeachelementin𝑅𝑖
form“WhydidyounotdoYinsteadofX?”Thefilteredobservations
isindexedbyalabelfromasetRofrewardcomponents,suchas
andthequeryarethenpassedtothecounterfactualcausalselection
thetimetakentoreachthedestination.Wedefinetheproblemof
modulediscussedindetailinSection3.2.
explainingtheactionsofaparticularegoagent𝜀 ∈Iascreating

### AsthefocusofCEMAistogenerateintelligibleexplanationsfor

the explanatory function 𝑓: (O𝜀)∗ × (A𝜀)∗ → H that maps a
endusers,inthisframeworkexplanationsarecomposedfromaset
sequenceoflocalobservationsandactionstoanexplanationfrom
offeaturesF whichdescribesemanticallymeaningfulpropertiesof
asetofpossibleexplanationsH.Forexample,onecoulddefine
astateand/oractionsequence.FordiscreetSandAwithinherent
H ⊂A∗,sothatanexplanationisapartialsequenceofactions.We
interpretations,thesetoffeaturesmightsimplyequalS∪A.For
use𝑠ˆ𝑎:𝑏 toindicatethatthesequencemaycontaincounterfactual
continuousspaces,suchasinAD,F mightincludeadiscretized
states.Wewrite𝑠 𝑥:𝑦 ≺𝑠 𝑎:𝑏 if𝑠 𝑥:𝑦 isasubsequenceof𝑠 𝑎:𝑏. summaryofactions,suchasaverageaccelerationordistanceto

### Wealsoassumetheexistenceofaprobabilisticmodelthatcanbe

the leading vehicle. The set of reward components R ⊂ F are
usedtostochasticallyforwardsimulatethesystem.Thesearereadalsoconsideredfeatures.Forexampleinautonomousdriving,these
ilyavailableinexistingmulti-agentliterature,forexample,inthe
mightbetimetodestinationorpresenceofcollisions.CEMAdoes
formofplannersortrainedreinforcementlearningpolicies[2,21].
notassumeanythingabouttheactualmeaningorpropertiesof
Suchprobabilisticmodelsdefineaconditionalprobabilitydistribu- featuresexceptthatthereissomefeaturefunction𝜙 :S∗×A∗→F
tionoversubsequentjointstatesofthesystemgivenpreviousobserconvertingastateandactionsequencetofeatures.Giventheabove,
vationsandactions.Wedenotethismodelwith𝑝(𝑆ˆ 𝑡+1:𝑛 |𝑜𝜀 1:𝑡 ,𝑎𝜀 1:𝑡 ), forCEMAwedefinethesetofallexplanationsasH =(F ×R)∗,
where𝑛 isthelasttimestep.Inthecasewhenthelocalstateis
sothattheoutputofthecounterfactualcausalselectionprocessisa
fullyobservabletotheegoagent(suchasinourevaluation),this
subsetoffeaturesF withcorrespondingrankingbycounterfactual
modelcanbereplacedwith𝑝(𝑆ˆ 𝑡+1:𝑛 |𝑠 1 𝜀 :𝑡 ,𝑎𝜀 1:𝑡 ),dropping𝑎𝜀 1:𝑡 for causaleffectsize.Finally,theexplanationisconvertedintoanNLE
notationalsimplicity.Note,thatthegoalsofotheragentsremain
andreturnedtotheuserviathehuman-agentinterface.
unobservableevenunderthisassumption.
3.2 CounterfactualCausalSelection
3.1 SocialXAIFramework
Thecounterfactualcausalselectionprocesshasthreemainsteps.
TheprocessofCEMA(Figure2)beginswiththeuseraskingaques- First,itrollsbacktimebeforethestarttimestep𝑢ofthequeriedactionaboutanegoagent𝜀andanactiontheywouldlikeexplained. tion,erasingthequeriedaction(Algorithm1).Second,thisrollback

<!-- Page 4 -->

Algorithm1Counterfactualdatasetsimulation bycuttingsequencesinto|𝑃|slicesdefinedbytheirend-points𝑃 =
Input: Parsedquery𝑞;observedjointstatesequence𝑠 1:𝑡. (𝑝 1 ,...,𝑝 |𝑃| )with𝑝 0 =𝜏+1assumedimplicitly.Eachsliceisthen
Output: CounterfactualdatasetD ={(𝑠ˆ (𝑘) ,𝑦(𝑘),𝑟(𝑘))}𝐾 . convertedtoasetoffeaturesusingthefeaturefunction𝜙.Following
𝜏+1:𝑛 𝑘=1 QuillienandLucas[34],featuresthatco-occurmorefrequentlywith

## 1: D ←∅.

3 2 : : 𝜏 fo ← r𝐾 D i e t t e e r r a m tio in n e s f d ro o m𝑠 1:𝑡 assuringthat𝑞.𝑠ˆ𝑢:𝑣 iserased. t a h s e a q s u a e li r e i n ed tc a a c u ti s o e n b a y cr h o u s m s a co n u s. n T te h r e fa re c f t o u r a e l , s f s o h r o e u a l c d h b s e li r c a e n 𝑝 k 𝑗 ed ∈ h 𝑃 ig o h f e a r
4: Get𝑠ˆ𝜏+1:𝑛 ∼𝑝(𝑆ˆ 𝜏+1:𝑛 |𝑠 1:𝜏)viaforwardsimulation. counterfactualsimulation,Algorithm2measuresthecounterfactual
6 5 : : P D r e e t s e e r n m c i e n o e f r q ew ue a r r y d 𝑦 fo ← reg 1 o if 𝑟 𝑞 ← .𝑠ˆ𝑢: 𝑅 𝑣 𝜀 ≺ (𝑠ˆ 𝑠 𝜏 ˆ𝜏 + + 1 1 :𝑛 :𝑛 ). else0. 𝑦 ca b u y sa c l o e r ff r e e c la t t s i i n z g e f o e f a f t e u a r t e u s re w s i o th n t t h he e p p r r e e s s e e n n c c e e o o f f t t h h e e q a u c e t r i i o e n d a a c c r ti o o s n s
7: D ←D∪{(𝑠ˆ𝜏+1:𝑛 ,𝑦,𝑟)}. t

## M

he
(
s
e
i
.
m
g.
u
,l
l
o
at
g
e
i
d
sti
c
c
o
r
u
e
n
g
t
r
e
e
r
s
f
s
a
i
c
o
t
n
u
)
al
i
s
s
.
u

## F

s
o
e
r
d
th
to
is
p
,
r
a
e
n
d
i
i
n
ct
te
t
r
h
p
e
re
p
t
r
a
e
b
s
l
e
e
n
c
c
l
e
as
o
s
f
ifi
th
e
e
r
8: endfor queriedaction𝑦fromthefeatures.Thecounterfactualcausaleffect
sizesaregivenbyimportanceattributionsforfeaturesfromM,
Algorithm2Calculatecounterfactualcausaleffectsize givingamechanisticselectionandrankingoffeaturesF
𝑗
𝑚 ∈H.
Input: CounterfactualdatasetD. Teleologicalexplanationsareformulatedintermsoftheintrinsic
Output: Mechanistic(F𝑚 )orteleological(R𝑡 )explanation. rewardcomponentsoftheegoagent.Forthisexplanatorymode,
Mechanisticexplanation thecounterfactualsimulationsinformushowtherewardsofthe
1: F𝑚 ← []. ego,asmeasuredbytherewardvector𝑟 ∈R𝑑 ,changedepending
2: forintervalend-point𝑝 𝑗 ∈𝑃 do onthepresence𝑦ofthequeriedactionoftheego.Forbinary𝑦,this
4 3 : : X D , 𝑗 Y ← ← Sl c ic o e nv 𝑠ˆ 𝜏 e (𝑘 + r 1 t ) : D 𝑛 ∈ 𝑗t D ofe fr a o tu m re 𝑝 s 𝑗 𝜙 − ( 1 𝑠ˆ𝑝 t ( o 𝑘 𝑗− ) 𝑝 1: 𝑗 𝑝𝑗 g ) iv a i n n d g t 𝑠 a ˆ𝑝 ( r 𝑘 𝑗 g − ) e 1 t :𝑝 s 𝑗 𝑦 . (𝑘). ( m t 𝑦 h e e a = q n u s 0 e ) t r . h i F e a o d t l A l a o c l w g ti o o i r n n i g th w t m h as e 2 o a s b v p s e l e i r r t a s v g e D e d t ( i r 𝑦 n e t a = o tm t 1 w ) e a o n n t d d i e s ff o jo n e i e c n t w t f s o h e r e ts r r : e a o n it n d e w o w m as h iz n e e o r d e t
5: M ←FitaninterpretableclassifiertoXpredictingY. controlledtrials[4]wetakethedifferencebetweentheexpected
6: 𝑤,𝐼 ←Featureimportanceattributions𝑤 ofMindexedin rewardvectorsofeachset,thenordertheelementsofthedifference
descendingorderby𝐼.
decreasinglybyabsolutevalue,givingateleologicalorderingof
7: AppendF 𝑗 𝑚 ={(F𝑖 ,𝑤 𝑖) |𝑖 ∈𝐼}toF𝑚 . rewardcomponentsR𝑡 ∈H bythecausaleffectof𝑦.
8: endfor
Teleologicalexplanation
9:

### X←FilterDby𝑦(𝑘)

=1formatchwithquery.

## 4 Applicationtomotionplanning

10: Y ←D\X,allsamplesnotmatchingthequery. WegiveafulldemonstrationofCEMA’scapabilitiesbyapplyingit
11: 𝑤,𝐼 ←E X [𝑟]−E Y [𝑟]indexedby𝐼 inabsolutedesc.order. totheproblemofmotionplanningforADwhichisachallenging
12: R𝑡 ←{(R𝑖 ,𝑤 𝑖) |𝑖 ∈𝐼}. reasoning task due to the tightly coupled interactions of many
agentsinadynamicallyevolvingsystem[37].Specifically,weuse

### CEMAtoautomaticallyexplainthedecisionsoftheInterpretable

allowsCEMAtosimulatecounterfactualalternativestothequeried Goal-basedPredictionandPlanning(IGP2)systemforAD[1].We
action(Algorithm1).Third,thecounterfactualsimulationsinform giveasummaryofIGP2totheextentnecessaryforthefollowing
usaboutwhichfeaturesofthesystemaremostimportantforthe sections,butforfulldetailspleaserefertotheoriginalpaper.
queriedactiontooccurandweusethisinformationtocalculatethe Thelocalstate𝑠𝑖 ofavehicle𝑖 containsitspose(positionand
counterfactualcausaleffectsizeforboththeteleologicalandthe heading),velocity,andaccelerationAsequenceoftemporallyadjamechanisticexplanatorymodepresentedinSection2(Algorithm2). centlocalstatesiscalledatrajectory.Localobservation𝑜𝑖 contain
Algorithm1startsbyrollingbackthejointstatesequence𝑠 1:𝑡 thelocalstatesofnearbytrafficparticipants.Actions𝑎𝑖 setlow-level
toatimestep𝜏,suchthat𝜏 ≤𝑢,resultinginatruncatedsequence controlssuchasaccelerationandsteering,whilegoals𝐺𝑖 arespatial
𝑠 1:𝜏 thatassuresthatthequeriedaction𝑠ˆ𝑢:𝑣iserasedfrom𝑠 1:𝑡.The destinations.RewardcomponentsR arelongitudinalandlateral
valueof𝜏 canbeafixeddistancefrom𝑢oritcanbedeterminedto, acceleration,presenceofcollisions,timetoreachadestination,and
forexample,correspondtothestartofadistinctqualitativechange goalcompletion.IGP2usesahierarchyofsystemsratherthanan
intheego’sbehaviorpriorto𝑢.Thealgorithmthenperforms𝐾 end-to-endarchitecture.Itdefinesasetofactionsequencetemplates
numberofforwardsimulationsofthesystemfromtime𝜏according calledmaneuverswithdynamicallygeneratedtrajectoriesforvehitotheprobabilisticmodel𝑝(𝑆ˆ 𝜏+1:𝑛 |𝑠 1:𝜏).Foreachsimulation,we clestofollow,includinglane-follow,lane-change-{left,right},
obtainasequenceoffuturejointstatesofthesystemdenoted𝑠ˆ𝜏+1:𝑛, turn-{left,right}, give-way, and stop. Common sequences of
determinethereward𝑟 ∈R𝑑 fortheego,andwhetherthequeried maneuversarethenfurtherchainedintohigh-levelmacroactions:
action𝑠ˆ𝑢:𝑣 oftheegowaspresentinthesimulation(𝑦 ∈ {0,1}). Continue,Change-{Left,Right},Exit,andStop.
ThisprocessgivesadatasetofsimulationsdenotedD. IGP2usesmacroactionstopredictforeachnon-egovehicle𝑖a
Algorithm2hastwoparts,oneforeachmodeofexplanation. jointdistributionoverpossiblegoalsandfuturetrajectoriesgiven
Mechanisticexplanationsareformulatedintermsoftheactions theobservedjointlocalstates𝑠 1:𝑡.MonteCarloTreeSearch(MCTS)
ofotheragentsintheneighborhoodoftheegovehicle.Actions is then used to forward simulate the world and obtain driving
oftheotheragentscanhavedifferentcausaleffectsontheegoat trajectories for the ego vehicle. In every MCTS simulation, the
differenttimes,sowefirstincreasethegranularityofexplanations previouslypredictedjointgoalandtrajectorydistributionisusedto

<!-- Page 5 -->

Table1:BinaryfeaturesF todescribethefundamentalmo- logisticregressiontoworkbestasitissimple,inherentlyintertionsandhigh-levelactionsofvehicles(includingego).For pretable,andallfeaturesarebinarysotheirscaledoesnotaffect
continuousvalues,themeanvalueiscalculatedalongthe theimportancevalues.
lengthofthetrajectoryandthresholdedwithsmallvalue𝛿.

## 5 Computationalevaluation


### Feature Calculation Explanation


### WeevaluateCEMAonthefourscenarios(S1–S4)usedbyAlbrecht

Acceleration 𝑎𝑖 >𝛿 𝑎 Accelerate etal.[1].ThescenariosareshowninFigure3withexpertexplana-
𝑎𝑖 <−𝛿 𝑎 Decelerate tionsoftheego’sbehaviorbyAlbrechtetal.[1]Inlinewithour
𝑎𝑖 ∈ [−𝛿 𝑎 ,𝛿 𝑎] Maintainvelocity focusonsocialXAI,wetestCEMAonmanyuserqueriesregard-
Relative 𝑣𝑖 −𝑣𝜀 >𝛿 𝑣 Fasterthanego ingdifferentegoagentsandbehaviors,andthegeneratedoutputs
speed 𝑣𝑖 −𝑣𝜀 <−𝛿 𝑣 Slowerthanego ofCEMAarepresentedthroughfivesimulatedconversations(Ta-
𝑣𝑖 −𝑣𝜀 ∈ [−𝛿 𝑣 ,𝛿 𝑣] Samespeedasego ble2),highlightingCEMA’sabilitytocorrectlyidentifythecauses
Stop 𝑣𝑖 ∈ [0,𝛿 𝑠] Doesitstop behindeachqueriedaction.Forallqueries,wesimulate𝐾 =100
Maneuver One-hotencode Longestmaneuver counterfactualworldswithasmoothingweight𝛼 =0.1.Further
MacroAction One-hotencode Longestmacroaction detailsabouttheexperimentalsetuparegiveninAppendixB.We
focusonS1forpresentation,butallresultsareconfirmedacrossall
scenariosandallpresentedinAppendixC.Weshowthat:
(1) CEMAcorrectlyfindsandrankstherelevantcausesofthe
randomlysampleagoalandcorrespondingtrajectoryforeachnon- ego’sactionsthatarecongruentwithexpertexplanations;
egovehicle.MCTSgeneratesatrajectoryfortheegoinasimulation (2) Itcorrectlyidentifiestherelevantcauseseveninthepresence
bysequentiallychoosingmacroactionsbasedonbackpropagated ofalargenumberofagents;
preferencevalues(i.e.,Q-values)untiltheegoreachesitsgoal. (3) Thecausalselectionprocessisrobusttochangesinthesamplingsize𝐾 andtheaccuracyoftheprobabilisticmodel.
4.1 ImplementingCEMA
5.1 CorrectnessofCausalSelection

### WedefineoursetoffeaturesF inTable1,whichwerechosento

describebothfundamentalmotionsandhigh-levelmaneuversofall As shown in Table 2, CEMA correctly selects causes which are
vehiclesincludingtheego.Featuresaveragealongthelengthofthe congruentwiththeexpertexplanationsofAlbrechtetal.[1].
trajectoryandmayencountertheissuethatatonetimestepthey InconversationS1-A,thecausesbehindthefactuallanechange
haveapositivecausaleffect,whileatalatertimestep,theyhavea oftheegoarequeried.ThetopplotinFigure4showsthatCEMA
negativecausaleffect,resultinginaggregatezerocausaleffect.The correctlyfindsthatadecreaseintime-to-goalisthemostsignificant
slicingoperationinAlgorithm2assuresthatthisissueisavoided. teleologicalcause.AsthebottomplotinFigure4shows,CEMA
Tofocusoncausalselectionandavoidtheambiguitiesofnatural correctlyidentifiesthatthenon-egoslowingdownisamechanistic
language,wehand-codeeachquery𝑞tocontainadescriptionof causeoftheego’slanechange.CEMAalsodeterminesthatthis
thequeriedsubsequence𝑠ˆ𝑢:𝑣 givenasasubsetoffeaturesfromF. slowingdownisduetothenon-egovehicledeceleratinginorder
Fornaturallanguagegeneration,weuseadeterministicrealization toturnright.ThemiddleplotofFigure4confirmsthattheinitially
enginecalledSimpleNLG[12],whichgeneratesagrammatically fasternon-egovehiclecuttinginfrontoftheegoisalsoamechacorrectEnglishsentencefromacontentspecification,e.g.,subject nisticcauseoftheego’slanechange.Thisshowstheimportance
andverb.Thisabetterfitthanneuralgenerationalgorithms,due ofslicingthetrajectoriesintosegmentsasCEMAproducesmore
toalackofannotateddataandhallucinationsinneuralmodels. fine-grainedcausesthatfocusonactioninaparticulartimeinterval.
SinceIGP2canassigntosome(reachable)goalsandtrajectories InconversationsS1-BtoS4,wealsoseethatCEMAcorrectly
near-zeroprobabilities,weuseadditivesmoothing–detailedin identifiescausesforcontrastivequestions–forexample,“Why
AppendixA.3–withparameter𝛼 tomakesureeverygoalandtra- aren’tyougoingstraight?” –inwhichtheuserasksaboutanalterjectorycanbesampledforthenon-egovehicles.Wethengenerate nativeaction(i.e.,foil)thattheegocouldhavedoneasopposedto
twodatasetswithAlgorithm1.Forteleologicalexplanations,we thefactualobservedactions(i.e.,fact).Leveragingthecounterfacset𝜏 =𝑢,rollingbacktimejustbeforethequeriedactionofthe tualsimulations,CEMAcontraststhesimulationscontainingthe
ego.Thisisbecauseteleologicalexplanationsaredeterminedby foiltosimulationscontainingthefactandderivestheappropriate
theMCTSrewardcomponentswhichonlydependontheego’s teleologicalcauses.CEMAdeliversconsistentexplanationseven
presentandfutureactions.Formechanisticexplanations,weset whenqueriestargetthesameactionbutarephraseddifferently.
𝜏 tothestarttimeofthelastactionpriorto𝑢,erasingboththe Forexample,“Whywillyouchangelanes?” isadirectquestion,
queriedactionoftheegoandtheactionthatcamebeforeit.For while“Whyaren’tyougoingstraight?” iscontrastive,yettheyboth
slicingthetrajectoriesinAlgorithm2,weset𝑃 ← (𝑢,𝑛) which refertothesamechanginglaneactionoftheegoandCEMAfinds
slicesthetrajectory𝑠ˆ𝜏+1:𝑛intoapast𝑠ˆ𝜏+1:𝑢 andpresent-future𝑠ˆ𝑢:𝑛 consistentcausesforbothqueries.InS4,CEMAcorrectlyfindsthat
subsequenceinreferencetothestartoftheego’squeriedaction. thestoppingofnon-ego3isthemostrelevantcausebehindthe
We use feature weights from logistic regression with K-fold ego’searlymergingbehavioranditalsofindsotherintuitivecauses.
cross-validationtodeterminefeatureimportancevalues.Wefound Forexample,thevehicleatthefrontofthewaitinglineofcarsis

<!-- Page 6 -->

(S1)Thenon-egoinfrontofthe (S2)Theegoisturningrightbut (S3)Theegoobservesthenon-ego (S4)Non-ego3isslowingdownto
egochangeslanesandbeginsto mustgiveway.Itobservestheve- changinglanestotheright.Thisis stop.Oncenon-ego4drivespastas
slowdown.Thisisindicativeofits hicleontheleftstopping.Thisis onlyrationalifthenon-egoisleav- indicatedbyitsmaintainedhigh
intentiontoturnrightatthejunc- onlyrationalifitistryingtoturn ingtheroundaboutatthenextexit. speed,thestoppingofnon-ego3
tion.Toavoidbeingsloweddown, leftandisgivingwayfortheon- The ego can therefore enter the staysrationalonlyifitistoallow
theegodecidestochangelanesas comingvehicle.Theegocanuse roundaboutfasterwithoutwaiting theegotomergewithoutwaiting
itisheadingstraight. thistoentertheroadearlier. togiveway. fornon-ego4topass.
Figure3:ThefourscenariosusedforevaluationbasedonAlbrechtetal.[1].Coloredcirclesaregoals.Solidlinesarepredicted
trajectoriesofnon-egoswiththicknesscorrespondingtopredictedprobability.Blackdottedlinesareobservations.
stopped.Wouldthisvehiclemove,thewaitinglineofcarswould variouseffectsonhumanswithactualparticipantsviaauserstudy.
beginmovingandnon-ego3couldnotallowtheegotomerge. Weaimtoanswerthefollowingresearchquestions:

### CEMAcanalsocorrectlyfindtherelevantcausesevenwhena

(1) HowdopeopleperceivethequalityofCEMA’sexplanations
largenumberofagentsarepresent.Forthis,wegreatlyincreasethe
ascomparedtoahumanbaseline?
numberofagentsinallscenariosandrerunCEMA.Forexample,
(2) WhataretheeffectsofCEMA’sexplanationsonpeople’s
weextendS1,addingtwoextralanestotheeast-westroadand
trustinautonomousvehicles?
increasingthenumberofagentsto20.Thisgave180features,most

### WeusedProlifictorecruitparticipantsfromtheUSAwhose

ofwhichhadnocausalinfluenceontheego,butCEMAcouldstill
firstlanguageisEnglish.Asmostpeoplehavenothadfirst-hand
identifythemostimportantcausesasintheoriginalscenario.
experiencewithautonomousvehicles(AV),weengagedthemvia
animatedvideosofthescenarios.Wedesigntwosurveysandsum-
5.2 RobustnessofCausalSelection marizeourmethodologybelowwithfulldetailsinAppendixD.
Inthefirstsurvey(N=54;Male=25,Female=29),participantswere

### Wedemonstraterobustnesstochangesin(a)thesamplingsize𝐾,

askedtodescribeandexplainintheirownwordsthebehaviorofthe
and(b)intheaccuracyoftheprobabilisticsimulationmodel,to
AVinallfourscenarios.Thisgave408explanationsacrossscenarshowthatcorrectexplanationsaregeneratedevenwhensampling
ios,ofwhichweexcluded26vacuousresponses(e.g.,“Idon’tknow",
islimitedbyresourcesandthatoursystemworkswithpredictional-
“None",etc.),andannotatedtheremainingexplanationswithadiffergorithmsofvaryingperformance.Forsizerobustness,werandomly
entsetofparticipantsregardingtheircausalcontent,overallquality
sampleadatasetof𝐾 ∈ {5,10,...,100}sequences50timesand
andcomplexity,andtrustworthiness.Wereleaseanextendedvercalculatethecausalattributionsforeachdataset.Forrobustness,we
sionofthisannotateddatasetofnaturallanguageexplanations,
interpolatebetweenthetruepredictedanduniformlydistributed
calledtheHumanExplanationsforAutonomousDrivingDecisions
behaviorsbyincreasingthesmoothingstrength𝛼 onalogscale.
(HEADD)dataset,containing14scenarioswithseveralagentsand

### ThetopplotinFigure5showstheevolutionofcausalattributions

environmental elements, including occlusions, pedestrians, and
asweincrease𝐾 inS1.WeseethatCEMAbecomesincreasingly
1308explanations.Wecollectedexplanationsaswearenotaware
confidentinitsattributionsas𝐾 increases,whileconfidenceinterofanyreproducibleandpubliclyavailablemethodsforADthat
valsremaintight.Evenwithfewsamples,CEMAidentifiescauses wouldallowforameaningfulcomparisontoCEMA’sexplanations.2
correctly.ThebottomplotofFigure5showshowcausalattributions

### ComparingagainstahumanbaselineisalsoabetterfitforCEMAas

changeas𝛼increaseswhichcorrespondstoincreasinguncertainty
itsexplanationsareintendedtohavelowcognitiveoverheadandbe
inbehaviorpredictions.Weseethatfeatureimportancevaluesare
easytounderstand.Incontrast,morecomplexexpertexplanations
littleaffectedbychangesinthesampledistributionsastheyfluctuwouldlikelybelesseffectiveforendusers[11].
atearoundthesamevalues.Similarpatternsareobservedacross

### Inthesecondsurvey(N=200;M=99,F=101),wedesignedtwo

scenarios,whichdemonstratesthatCEMAisrobusttochangesin
tasks,oneforeachresearchquestion.First,tomeasurethequality
boththesamplingsizeandtheaccuracyofexternalpredictions.
ofexplanations,weaskedparticipantstoratearandomsample
of10explanationsfromasetof30explanations(5fromCEMA
and25fromHEADDwiththehighestqualityratings)foreach

## 6 Userstudy

scenarioona5-pointLikertscale.With50%chance,wehighlighted

### Sofar,wehavefocusedonthetechnicaldetailsofCEMA.Ultimately,

however,theprimarytargetofCEMAisnon-expertendusers,so 2WeexploredChatGPTasabaseline,butitwasinadequateasitsresponseswerevery
wemustevaluatethequalityofCEMA’sexplanationsandtheir inconsistentandonlysometimescorrect(seeAppendixD.4fordetails).

<!-- Page 7 -->

Table2:ActualresponsesofCEMAtoqueries(initalic).(S1- Collision possible: No
A)Thepassengerseesonanonboarddisplay,thattheegois Always reaches goal: Yes
planningtochangetotheleftlane.Theyfindthisunexpected

### Curvature

andinquire.(S1-B)Thepassengerobservestheegochanging (1/m)
lanesandasksforthereasonsbehindthemaneuverwhile Jerk
itisongoing.(S2)Thepassengerobservedthattheegohad (m/s3)
enteredthejunctionwithoutstoppingtogiveway,which Angular velocity
could be dangerous. (S3) The passenger sees that the ego (rad/s)
willturnrightattheroundaboutwithoutstoppingdespite Time to goal
(s)
theoncomingvehicle.(S4)Oncenon-ego4haspassed,the
egomergesontothemainroadwhichmakesthepassenger −1.4 −1.2 −1.0 −0.8 −0.6 −0.4 −0.2 0.0
wonderwhytheegodidnotgivewaytonon-ego3. Past causes

### Faster

Scenario1(S1-A) Scenario1(S1-B)

### Change right

Whywillyouchangelanes? Whyaren’tyougoingstraight?

### Exit straight

Itwilldecreasethetimetogoal. Itwouldincreasethetimeto
Whydoesitdecreasethetimeto thegoal. Slower
thegoal? Whyisitslowertogostraight?
Same vel.
Becausevehicle1willbeslower Becausevehicle1isslowing
thanus. down. Rest of 4

### Whywillitbeslower? Anyotherreasons? −0.5 0.0 0.5 1.0 1.5

Itwilldecelerateandturnright. Itisslowerthanus. Present-future causes
Whatifithadn’tchangedlanes Whatwillyoudoafterthis?

### Slower

before? Wewillgostraightandaccel-

### Decelerate

Wewould’vegonestraight. erate.

### Exit right

Scenario2(S2) Scenario3(S3) Change left

### Exit straight

Why did you not stop to give Whatwillyoudoattheround-

### Accelerate

way? about? Faster
Itwould’veincreasedthetime Wewillturnrightandacceler- Same vel.
tothegoal. ate. Rest of 2
Couldn’tithavecausedacolli- Wouldnotstoppingleadtoa −0.50 −0.25 0.00 0.25 0.50 0.75 1.00
sion? collision?
Acollisionwouldnothaveoc- Not stopping doesn’t cause Figure4:[Top]Signeddifferencesbetweenexpectedreward
curred. a collision, but stopping in- componentscorrectlyidentifytime-to-goalasthemostsig-
Howdidyouknow? creasesthetimetoreachthe nificant teleological cause. [Mid/Bot] Feature importance
Vehicle1wasturningleftand goal. attributionsfortheslicebeforeandduring/afterthequeried
stopped. Howdoyouknowwewon’tcol- subsequencecorrectlyrankmechanisticcauses.Violinplots
Whatifitwentstraight? lidewiththeoncomingcar?
show5-foldcross-validationrepeated7times.
We would’ve given way and It has been changing lanes
sloweddown. rightandisturningright.
Scenario4(S4) andtheotherhalfafterhavingrankedexplanations.Wealsoasked
Whyareyounotstoppingtogiveway? participantsabouttheirdrivingexperienceandpreviousexposure
Stoppingandgivingwaywouldincreaseourtimetoreach toAVsusingtheSAEautomationscale[36].Wehypothesizethat
thegoal. H1:theexplanationsgeneratedbyCEMAarescoredonaverageas
Isitsafetoturnleftearly? highlyasthehumanbaselineexplanations;H2participantswho
Acceleratingandturningleftdoesnotcauseacollision. sawexplanationsfromCEMAhaveonaveragehigherlevelsof
Whynot? trustthanthosewhohavenot.Weanalyzeourdatabyfittinglinear
Becausevehicle3stops. mixed-effectsmodelsforeachhypothesis.Wereporttheestimated
Whatifvehicle3wentstraight? means(𝛽ˆ)andstandarderrors(𝜎)foreachvariableandusethe
Wewouldslowdownandgiveway. Waldtest[43]todeterminewhethertheeffectsofavariableare
statisticallysignificantontheoutcome.
ForH1,wefoundthatCEMA’sexplanationswereratedsignifiinboldtheexplanationsfromCEMA.Second,tomeasuretrust, cantlyhigherwhenitsexplanationswerenothighlightedandwere
weusethe9trustscalesproposedbyHoffmanetal.[20]adapted notsignificantlyworsewhentheywerehighlighted.Onaverage,
to the AD domain. We use a between-subjects design: half the explanationratings(𝛽ˆ 0=3.31,𝜎=0.08)weremarginallylowerfor
participantsareshownthetrustscalespriortorankingexplanations, human-writtenexplanations(𝛽ˆ=−0.16,𝜎=0.08,𝑝=0.21),andratings

<!-- Page 8 -->

1.0
0.5
0.0
−0.5
20 40 60 80 100
Number of samples (K)
thgiew
erutaeF

### Slower

Decelerate

### Exit right

Exit straight

### Faster

Accelerate
Same vel.
1.0
0.5
0.0
−0.5
0 100 101
Smoothing weight (α)
thgiew
erutaeF
notuniquetoCEMAbutisanecessarystepforanyautomatedexplanationgenerationsysteminsocialXAI.WithCEMA,weassumed
thatthereisafeaturefunction𝜙 whichperformsthetranslation
fromtherawrepresentationsofstateandactionspacestothemore
abstractsemanticfeaturespace.Thistranslationfromstatetofeaturespaceisdomain-dependentandshouldbeconsideredacrucial
stepduringthedeploymentofsocialXAIsystems.However,CEMA
isfeature-agnosticsothatcounterfactualcausalselectiondoesnot
dependon𝜙 ortheinterpretationsoffeatures.
CEMAalsodoesnotrelyonafixedcausalgraphtomodeldynamicmulti-agentsystems.Instead,itassumesthatthereisaprobabilisticmodel,suchasastochasticplanner,trainedjointpolicy,or
autoregressivemodeltrainedonobservationaldata,whichcanbe
usedtoforwardsimulatethestateofthesystem.Basedonthework
ofQuillienandLucas[34]andthecounterfactualmodelofcausation[19,24],CEMAcanderivecausestoanegoagent’sactionsin
anysystemwheresuchamodelisobtainable.Theassumptionhere
isthatthesemodelscoveralternativesthataregroundedinfactualobservationswithanon-zeroprobability,andanyreasonably
expressivealgorithmwouldfulfillthesecriteria.
Figure5:Changestocausalattributionswith[Top]differ-

### Theuserstudysuggeststhatpeoplemaypreferexplanations

ent sample sizes and [Bot] different smoothing weights
generatedbyCEMA,however,trustlevelsarestilllow.Thismaybe
forpresent-futuremechanisticcausesinconversationS1-
–asseveralparticipantsindicatedintheirfeedback–becausepeople
A.Shadedregionsarebootstrapped95%confidenceintervals.
prefertoseeagentsactmoreconservatively,withoutexploitingpotentiallyriskierbutmoreefficientactions.Explanationsthatjustify
efficientbutlesssafedecisionsthenhavetoovercometheinherent
weresignificantlylowerforhumanexplanationswhenCEMA’s warinessofpeople,whichwasindeedhighamongparticipants,
explanationswerenothighlightedtoparticipants(𝛽ˆ=−0.22,𝜎=0.08, thoughitsomewhatdecreasedafterseeingexplanations.
𝑝 < 0.05).Variationsacrossscenarioswerenegligible(𝑆𝐷=0.07). WedesignedCEMAtobeusedinconversationswithusers,but
WealsofoundthatpeopletendtorankCEMA’sexplanationshigher wedidnotfocusonnaturallanguageprocessinginthiswork.ForexwhentheyhadexposuretoAVspreviously(𝛽ˆ=0.1,𝜎=0.06,𝑝 =0.09). ample,weassumethatqueriesunambiguouslydescribethetiming
ForH2,wefoundthat,onaverage,participants’trustratings ofactions–allowingustofocusoncausalselection–butactualnat-
(𝛽ˆ 0=1.53,𝜎=0.5)weresignificantlyhigherafterseeingexplanations urallanguagequeriesarefuzzyandimprecise.Bybuildingmodern
(𝛽ˆ=0.11,𝜎=0.05,𝑝 < 0.05),whichalignswithexpectationsfrom NLPcomponents,wecanstrengthenthesocialandconversational
aspectsofCEMA.Futureworkwillinvolvetheintegrationoflanliterature[30].Participants’trustalsoincreasedsignificantlywhen
theyratedCEMA’sexplanationshigher(𝛽ˆ=0.35,𝜎=0.15,𝑝 ≈0)or guageparsing[25]anddialoguesystems[10]leveragingmodern
whentheyhadpreviousexposuretoAVs(𝛽ˆ=0.33,𝜎=0.05,𝑝 ≈0),but neurallanguagemodelstodeliverexplanations.
trustremainedlargelyunchangedbyhumanexplanations(𝛽ˆ=0.12, Our implementation of CEMA for AD improves on existing
socialXAImethodsforADinseveralaspects.IncontrasttoOmeiza
𝜎=0.15,𝑝=0.85).Trustratingswerenotsignificantlyaffectedby
etal.[30],weavoidusingasurrogatemodelandgeneratecausal
whetherCEMA’sexplanationswerehighlighted(𝛽ˆ=0.02,𝜎=0.05,
explanationsthattakethetemporalnatureofdrivingintoaccount.
𝑝 =0.66)andtherewerenosignificantinteractioneffectsbetween

### ComparedtoGyevnaretal.[14],CEMAsupportsmultiplemodes

the average ratings of explanations and highlighting (𝛽ˆ=−0.04,
ofexplanationswithbothhigh-levelandlow-levelfeatures.
𝜎=0.04, 𝑝 = 0.36). The estimated trust levels varied across the

### Toconclude,ourgoalistoaddresssomeofthetransparency-

9trustscales(𝑆𝐷=0.53)butnottheobservedtendencies.OurrerelatedsocialconcernsofAI.CEMAfillsagapinsocialXAIby
sultssuggestthatpeoplewhohadsomeexposuretoAVsorhada
enablingcausalexplanationgenerationindynamicsequentialmultipreferenceforCEMA’sexplanationsweremorelikelytotrustAVs
agentsystems.Asweexpecttoseeautonomousagentsproliferate
ingeneral,regardlessofwhethertheyknewwhichexplanations
ineverydayenvironments,socialexplanationswillbecrucialfor
camefromCEMA.TakentogetherwiththeresultforH1,thissugbuildingusertrustandfortheacceptanceofnewtechnologies.
geststhatCEMA’sexplanationsmaybemoreeffectiveatimproving
people’strustinAVsthannon-experthumanexplanations.

## Acknowledgments


## 7 Discussionandfuturework


### TheauthorsthankC.Brewitt,M.Tamborski,andY.Ziserfortheir

OurprimarygoalwithCEMAistoadvancethefieldofsocialXAI helpfulcommentsonearlierdrafts.Thisworkwassupportedin
appliedtodynamicmulti-agentsystems.Acrucialcomponentof partbytheUKRICentreforDoctoralTraininginNaturalLanguage
intelligibleexplanationsistheuseofsemanticallymeaningfulfea- Processing(grantEP/S022481/1)andtheEdinburghLaboratoryfor
tures[11].Importantly,thechallengeofdesigningusefulfeaturesis IntegratedArtificialIntelligence.

<!-- Page 9 -->


## References

Press,NewYork,NY,US,33–65.
[1] StefanoV.Albrecht,CillianBrewitt,JohnWilhelm,BalintGyevnar,Francisco [20] RobertR.Hoffman,ShaneT.Mueller,GaryKlein,andJordanLitman.2019.
Eiras,MihaiDobre,andSubramanianRamamoorthy.2021.InterpretableGoal- MetricsforExplainableAI:ChallengesandProspects.arXiv:1812.04608[cs](Feb.
basedPredictionandPlanningforAutonomousDriving.InIEEEInternational 2019).arXiv:1812.04608[cs]
ConferenceonRoboticsandAutomation(ICRA). [21] RenhaoHuang,HaoXue,MauricePagnucco,FloraSalim,andYangSong.2023.
[2] StefanoV.AlbrechtandPeterStone.2018.Autonomousagentsmodellingother MultimodalTrajectoryPrediction:ASurvey. arXiv:2302.10463[cs.RO]
agents:Acomprehensivesurveyandopenproblems.ArtificialIntelligence258 [22] DavinderKaur,SuleymanUslu,KaleyJ.Rittichier,andArjanDurresi.2022.Trust-
(2018),66–95. https://doi.org/10.1016/j.artint.2018.01.002 worthyArtificialIntelligence:AReview. Comput.Surveys55,2(Jan.2022),
[3] SajidAli,TamerAbuhmed,ShakerEl-Sappagh,KhanMuhammad,JoseM.Alonso- 39:1–39:38. https://doi.org/10.1145/3491209
Moral,RobertoConfalonieri,RiccardoGuidotti,JavierDelSer,NataliaDíaz- [23] JinkyuKim,AnnaRohrbach,TrevorDarrell,JohnCanny,andZeynepAkata.
Rodríguez,andFranciscoHerrera.2023.ExplainableArtificialIntelligence(XAI): 2018.TextualExplanationsforSelf-DrivingVehicles.InComputerVision–ECCV
WhatWeKnowandWhatIsLefttoAttainTrustworthyArtificialIntelligence. 2018(LectureNotesinComputerScience),VittorioFerrari,MartialHebert,Cristian
InformationFusion(April2023),101805. https://doi.org/10.1016/j.inffus.2023. Sminchisescu,andYairWeiss(Eds.).SpringerInternationalPublishing,Cham,
101805 577–593. https://doi.org/10.1007/978-3-030-01216-8_35
[4] PeterC.Austin.2011.AnIntroductiontoPropensityScoreMethodsforReducing [24] DavidLewis.1973. Causation. JournalofPhilosophy70,17(1973),556–567.
theEffectsofConfoundinginObservationalStudies. MultivariateBehavioral https://doi.org/10.2307/2025310
Research46,3(May2011),399–424. https://doi.org/10.1080/00273171.2011.568786 [25] JiaqiLi,MingLiu,BingQin,andTingLiu.2022.ASurveyofDiscourseParsing.
[5] ClaudineBadue,RânikGuidolini,RaphaelVivacquaCarneiro,PedroAzevedo, FrontiersofComputerScience16,5(Jan.2022),165329. https://doi.org/10.1007/
ViniciusB.Cardoso,AvelinoForechi,LuanJesus,RodrigoBerriel,ThiagoM. s11704-021-0500-z
Paixão,FilipeMutz,LucasdePaulaVeronese,ThiagoOliveira-Santos,andAl- [26] TaniaLombrozoandSusanCarey.2006.FunctionalExplanationandtheFunction
bertoF.DeSouza.2021.Self-DrivingCars:ASurvey.ExpertSystemswithAppli- ofExplanation.Cognition99,2(March2006),167–204. https://doi.org/10.1016/j.
cations165(March2021),113816. https://doi.org/10.1016/j.eswa.2020.113816 cognition.2004.12.009
[6] CillianBrewitt,BalintGyevnar,SamuelGarcin,andStefanoV.Albrecht.2021. [27] PrashanMadumal,TimMiller,LizSonenberg,andFrankVetere.2020. Ex-
GRIT:Fast,Interpretable,andVerifiableGoalRecognitionwithLearnedDeci- plainable Reinforcement Learning through a Causal Lens. Proceedings of
sionTreesforAutonomousDriving.In2021IEEE/RSJInternationalConference theAAAIConferenceonArtificialIntelligence34,03(April2020),2493–2500.
onIntelligentRobotsandSystems(IROS).1023–1030. https://doi.org/10.1109/ https://doi.org/10.1609/aaai.v34i03.5631
IROS51168.2021.9636279 [28] TimMiller.2019.ExplanationinArtificialIntelligence:InsightsfromtheSocial
[7] CillianBrewitt,MassimilianoTamborski,ChengWang,andStefanoV.Albrecht. Sciences.ArtificialIntelligence267(Feb.2019),1–38. https://doi.org/10.1016/j.

### VerifiableGoalRecognitionforAutonomousDrivingwithOcclusions.In artint.2018.07.007

IEEE/RSJInternationalConferenceonIntelligentRobotsandSystems. [29] SamerB.Nashed,SaaduddinMahmud,ClaudiaV.Goldman,andShlomoZilber-
[8] NadiaBurkartandMarcoF.Huber.2021. ASurveyontheExplainabilityof stein.2023.CausalExplanationsforSequentialDecisionMakingUnderUncer-
SupervisedMachineLearning.JournalofArtificialIntelligenceResearch70(May tainty.InProceedingsofthe2023InternationalConferenceonAutonomousAgents
2021),245–317. https://doi.org/10.1613/jair.1.12228 andMultiagentSystems(AAMAS’23).InternationalFoundationforAutonomous
[9] TathagataChakraborti,SarathSreedharan,andSubbaraoKambhampati.2020. AgentsandMultiagentSystems,Richland,SC,2307–2309.
TheEmergingLandscapeofExplainableAutomatedPlanning&DecisionMaking. [30] DanielOmeiza,HelenaWeb,MarinaJirotka,andLarsKunze.2021. Towards
InProceedingsoftheTwenty-NinthInternationalJointConferenceonArtificial Accountability:ProvidingIntelligibleExplanationsinAutonomousDriving.Pro-
Intelligence,IJCAI-20,ChristianBessiere(Ed.).InternationalJointConferences ceedingsofthe32ndIEEEIntelligentVehiclesSymposium(2021).
onArtificialIntelligenceOrganization,4803–4811. https://doi.org/10.24963/ijcai. [31] OpenAI. 2022. ChatGPT: Optimizing Language Models for Dialogue.
2020/669Surveytrack. https://openai.com/blog/chatgpt/.
[10] HongshenChen,XiaoruiLiu,DaweiYin,andJiliangTang.2017.ASurveyonDi- [32] JudeaPearl.2009.Causality(seconded.).CambridgeUniversityPress,Cambridge.
alogueSystems:RecentAdvancesandNewFrontiers.ACMSIGKDDExplorations https://doi.org/10.1017/CBO9780511803161
Newsletter19,2(Nov.2017),25–35. https://doi.org/10.1145/3166054.3166058 [33] Yunpeng Qing, Shunyu Liu, Jie Song, and Mingli Song. 2022. A Survey
[11] RichardDazeley,PeterVamplew,CameronFoale,CharlotteYoung,SunilAryal, onExplainableReinforcementLearning:Concepts,Algorithms,Challenges.
andFranciscoCruz.2021.LevelsofExplainableArtificialIntelligenceforHuman- arXiv:2211.06665[cs]
AlignedConversationalExplanations. ArtificialIntelligence299(Oct.2021), [34] TadegQuillienandChristopherG.Lucas.2023.CounterfactualsandtheLogic
103525. https://doi.org/10.1016/j.artint.2021.103525 ofCausalSelection. PsychologicalReviewAdvanceonlinepublication(2023).
[12] AlbertGattandEhudReiter.2009.SimpleNLG:ARealisationEngineforPractical https://doi.org/10.1037/rev0000428
Applications.InProceedingsofthe12thEuropeanWorkshoponNaturalLanguage [35] RCoreTeam.2023.R:ALanguageandEnvironmentforStatisticalComputing.R
Generation(ENLG2009).AssociationforComputationalLinguistics,Athens, FoundationforStatisticalComputing,Vienna,Austria. https://www.R-project.

### Greece,90–93. org

[13] BalintGyevnar,NickFerguson,andBurkhardSchafer.2023.BridgingtheTrans- [36] SAEInternational.2021.TaxonomyandDefinitionsforTermsRelatedtoDriving
parencyGap:WhatCanExplainableAILearnFromtheAIAct?.InProceedings AutomationSystemsforOn-RoadMotorVehicles.TechnicalReport.UnitedStates.
ofthe26thEuropeanConferenceonArtificialIntelligence(ECAI2023).IOSPress, [37] WilkoSchwarting,JavierAlonso-Mora,andDanielaRus.2018. Planningand
964–971. https://doi.org/10.3233/FAIA230367 Decision-MakingforAutonomousVehicles.AnnualReviewofControl,Robotics,
[14] BalintGyevnar,MassimilianoTamborski,ChengWang,ChristopherG.Lucas, andAutonomousSystems1,1(2018),187–210. https://doi.org/10.1146/annurev-
ShayB.Cohen,andStefanoV.Albrecht.2022. AHuman-CentricMethodfor control-060117-105157
GeneratingCausalExplanationsinNaturalLanguageforAutonomousVehicle [38] AndrewSilva,MatthewGombolay,TaylorKillian,IvanJimenez,andSung-Hyun
MotionPlanning.InWorkshoponArtificialIntelligenceforAutonomousDriving. Son.2020.OptimizationMethodsforInterpretableDifferentiableDecisionTrees
InternationalJointConferenceonArtificialIntelligence.https://doi.org/10.48550/ AppliedtoReinforcementLearning.InProceedingsoftheTwentyThirdInternaarXiv.2206.08783arXiv:2206.08783[cs] tionalConferenceonArtificialIntelligenceandStatistics.PMLR,1855–1865.
[15] BalintGyevnar,ChengWang,ChristopherG.Lucas,ShayB.Cohen,andStefanoV. [39] IliaStepin,JoseM.Alonso,AlejandroCatala,andMartínPereira-Fariña.2021.
Albrecht.2024.HEADD:HumanExplanationsforAutonomousDrivingDecisions. ASurveyofContrastiveandCounterfactualExplanationGenerationMethods
https://doi.org/10.7488/ds/7676 forExplainableArtificialIntelligence.IEEEAccess9(2021),11974–12001. https:
[16] R.J.Hankinson.1998.CauseandExplanationinAncientGreekThought.Clarendon //doi.org/10.1109/ACCESS.2021.3051315
Press. [40] StratisTsirtsis,AbirDe,andManuelRodriguez.2021.CounterfactualExplana-
[17] JosiahP.Hanna,ArrasyRahman,ElliotFosong,FranciscoEiras,MihaiDobre, tionsinSequentialDecisionMakingUnderUncertainty.InAdvancesinNeural
JohnRedford,SubramanianRamamoorthy,andStefanoV.Albrecht.2021.Inter- InformationProcessingSystems,Vol.34.CurranAssociates,Inc.,30127–30139.
pretableGoalRecognitioninthePresenceofOccludedFactorsforAutonomous [41] AbhinavVerma,VijayaraghavanMurali,RishabhSingh,PushmeetKohli,and
Vehicles.InIEEE/RSJInternationalConferenceonIntelligentRobotsandSystems SwaratChaudhuri.2019.ProgrammaticallyInterpretableReinforcementLearning.
(IROS). arXiv:1804.02477[cs,stat](April2019).arXiv:1804.02477[cs,stat]
[18] JacobHaspiel,NaDu,JillMeyerson,LionelP.RobertJr.,DawnTilbury,X.Jessie [42] SandraWachter,BrentMittelstadt,andChrisRussell.2017. Counterfactual
Yang,andAnujK.Pradhan.2018.ExplanationsandExpectations:TrustBuilding ExplanationswithoutOpeningtheBlackBox:AutomatedDecisionsandthe
inAutomatedVehicles.InCompanionofthe2018ACM/IEEEInternationalConfer- GDPR.HarvardJournalofLaw&Technology(HarvardJOLT)31,2(2017),841–
enceonHuman-RobotInteraction(HRI’18).AssociationforComputingMachinery, 888.
NewYork,NY,USA,119–120. https://doi.org/10.1145/3173386.3177057 [43] AbrahamWald.1943.TestsofStatisticalHypothesesConcerningSeveralParam-
[19] DenisJ.Hilton.1988.LogicandCausalAttribution.InContemporaryScienceand etersWhentheNumberofObservationsisLarge.Trans.Amer.Math.Soc.54,3
NaturalExplanation:CommonsenseConceptionsofCausality.NewYorkUniversity (1943),426–482. http://www.jstor.org/stable/1990256

<!-- Page 10 -->


### A.2 QueryTypes

[44] YiwenZhang,WenjiaWang,XinyanZhou,QiWang,andXiaohuaSun.2022.
Tactical-Level Explanation Is Not Enough: Effect of Explaining AV’s Lane-

### Wealsodefinethreequerytypes:what,whatif,andwhyqueries,

ChangingDecisionsonDrivers’Decision-Making,Trust,andEmotionalExperience.InternationalJournalofHuman–ComputerInteraction0,0(Aug.2022), whichalsoaffecttheselectedstatesequence𝑠ˆ𝑢:𝑣.
1–17. https://doi.org/10.1080/10447318.2022.2098965 Awhy-queryaskswhyalistoffactualactionsisexecuted.For
example,“Whydidyouchangelanestotheleft?” Itfollowstheprocessdescribedabovetodetermine𝑠ˆ𝑢:𝑣.Weconcurrentlygenerate

## A Implementationdetails

bothteleologicalandmechanisticexplanationsforthisquerytype.
A.1 UserQueries A what if-query asks about the actions of𝜀 had some other
vehicle𝑖 executed a different counterfactual list of actions. For

### AsweourfocusisoncausalselectionandNLP,wedonotuseNLU

example,“Whatifvehicle1hadstopped(insteadofgoingstraight)?”
systemstoparseusers’questions.Instead,wedefineastandard
Therefore,whatif-queriesencodeacontrastiveuserquestion.We
querytemplateandcodequeriesasastructuredJSONfile.The
assumethatthe(counterfactual)listofactionsdirectlyreplaces
templateisgiveninTable3witheachfieldandthecorresponding
somefactuallistofactionsthatisalsogivenforvehicle𝑖aspart
type.Thequeriesaregivenintermsofthreemaincomponents:
oftheuser’squery.However,wecannotdirectlyapplytheprocess
aquerytype(Type),alistofactions(Actions),andtenseofthe
inAppendixA.1tothislistofactionstodetermine𝑠ˆ𝑢:𝑣 asthese
question(Tense);withanoptionallistoffactualactions(Factuals).
actions have never been observed. Instead, we sample a set of

### Alistofactionsisgivenasacombinationofmaneuversandmacro

actionsofIGP2.Weidentifyforeachtimestepofatrajectorywhich
alternativetrajectoriesfromthegenerativemodel𝑝(𝑆ˆ 𝑡+1:𝑛|𝑠 1:𝑡)and
findthecounterfactualtrajectorywherevehicle𝑖wasexecutingthe
maneuverandmacroactionareexecutedallowingforatimestepcounterfactuallistofactions.WeapplytheprocessinAppendixA.1
by-timestepcomparisontothequeriedlistofactions.
totheselectedcounterfactualtrajectorywhichfiltersoutallaction
The above information is used to infer the start 𝑢 and end
groupsthatdonotcorrespondtothecounterfactuallistofactions.
timestep𝑣 necessarytodeterminethestatesequence𝑠ˆ𝑢:𝑣.First,

### Ifmultipleactiongroupsremain,thenwelookattheadditional

weusetensetofilteroutthosetimestepsoftheobservedtrajectory
𝑠𝜀
thatdonotmatchthetenseofthequestion.Forexample,ifthe
factuallistofactionsfromthequeryWeusetheobservedtrajectory
1:𝑡 andthefactuallistofactionstothenfindthefactualactiongroupof
questionisinfuturetense,thenallpastandpresenttimestepsare
greatestoverlapwithanyremainingcounterfactualactiongroups.
removed.Wethengroupconsecutivetimestepsbyactionsandfilter
Thevalues𝑢and𝑣areselectedasthestartandendtimestepsofthis
outthoseactiongroupsthatdonotmatchtheuser-givenlistof
overlappingregion.Thisprocessguaranteesthat𝑢and𝑣happen
actions.Ifafterthisprocess,westillendupwithmultiplegroups,
attimeswhenboththecounterfactualandfactuallistofactions
thenthefirsttimestepofthegroupclosesttothecurrenttimestep𝑡
wereexecutedinsomepossibleworlds.Weusethetermassociative
ispickedas𝑢fortheexplanation.Theendtimestep𝑣isthengiven
explanationtorefertoanexplanationthatdescribesthealternative
bythelasttimestepoftheactiongrouptowhich𝑢belongs.
actionsofvehicle𝜀hadvehicle𝑖executedthecounterfactuallistof
actions.Wegenerateteleologicalandmechanisticexplanationsfor
whyvehicle𝜀wouldhaveexecutedthoseactions.
Awhat-queryaskswhatvehicle𝜀isdoingatsomegiventimestep.
Thus,italwaysresultsinanassociativeexplanation.Here,wedo

### Table 3: The format template to encode queries. Types

nothaveaccesstothelistofactionssincethatiswhatwearetrying
markedwithastarareoptional.
todetermine.Instead,weassumethatthetimestep𝑢ofthestartof
theaction(ActionTime)isgiven.
Field Type Explanation Users’questionscanbenegated(Negated)sentences.Theeffect
Type str Typeoftheuser’squestion. ofnegationisflippingthevalueofthebooleanoutcomevariable
VID(VID) int TheVIDentifierfor𝜀. 𝑦 inAlgorithm1,butitalsoaffectshowwedetermine𝑢 and𝑣.
Tense str Grammaticaltenseofthe Negationturnsawhy-questionintoawhynotquestion,asin“Why
user’squestion didyounotturnright?” Wetreatthisasawhatif queryasking
(past,present,future).
aboutacounterfactuallistofactionsaboutvehicle𝜀itself.Forwhat
Actions List[str] Alistofactionstheuser if queries,negationmeansthatafactuallistofactionsisalready
isinterestedin. given,asin“Whatifyouhadn’tstopped?”Therefore,wecandirectly

### QueryTime int Timestepoftheuser

applytheprocessinAppendixA.1todetermine𝑢and𝑣.
askingthequestion. Finally,theusercanquerythefuture(e.g.,futureegoplancan
ActionTime int* Starttimeofqueriedactions. beshownonascreen).Forthis,weconcatenatetheobservedjoint
Onlygivenforwhat states𝑠 1:𝑡withthemaximumaposteriori-predictionsof𝑝(𝑆ˆ 𝑡+1:𝑛|𝑠 1:𝑡)
querytype.
giving𝑠ˆ1:𝑛.Ifthequeriedsequenceishypothetical,i.e.,𝑠ˆ𝑢:𝑣 ⊀𝑠ˆ1:𝑛,
Negated bool* Whethertheuser’s thenweassumethatwearegivenacorrespondingfactualsubsequestionisnegated.
quencetoallowfortheinferenceofthetimings𝑢and𝑣.
Factuals List[str]* Thefactualactionsof𝜀.
OnlyusedifActionsis
counterfactual.

<!-- Page 11 -->


### A.3 AdditiveSmoothing 20

SinceIGP2canassigntosome(reachable)goalsandtrajectories 17 18 7 15 6
near-zeroprobabilities,weuseadditivesmoothingwithparameter 10 9 16 1 12 19 14 5
𝛼tomakesureeverytrajectorycangetsampledfrom𝑝(𝑆ˆ 𝑡+1:𝑛|𝑠 1:𝑡). 0 13 4 0 3 20
Givenadiscreteprobabilitydistribution𝑝
𝜃
:Ω↦→ [0,1]parametrised
by𝜃 = [𝜃
1
,...,𝜃 𝑑]whereΩisafinitenon-emptysetofeventswith 11
size𝑑,additivesmoothingcreatesanewdiscreteprobabilitydistri- −20
bution𝑝 𝜙 :Ω↦→ [0,1]withnewparametervector𝜙 = [𝜙 1 ,...,𝜙 𝑑] 2
definedas:
𝜃
𝑖
+𝛼 −40
𝜙 𝑖 = , (𝑖 =1,...,𝑑),
1+𝑑𝛼
whereweassumedthat(cid:205) 𝑖 𝜃 𝑖 =1.
−60

## B Experimentalsetup

8
WeimplementCEMAusingPython,buildingonthepubliclyavail-
−80
ablecoderepositoryofIGP2.3ThesourcecodeforCEMAisavail- −100 −75 −50 −25 0 25 50 75 100
ableassupplementarymaterial,iswell-documented,andcontains
detailedinstructionsonhowtoreproduceourresults.Ourexperi- Figure6:ExtendedS1with20spawnlocationsforagents.
mentswererunonamodernWindows10PCwith32GiBofRAM
anda12-coreCPU.CEMAdoesnotneedaGPU.
Eachscenarioisdefinedusingasemanticroadlayoutinthe
60
ASAMOpenDrive1.6format,andusingaconfigurationfilethat
9
describesthebehaviourandstartingregionsofagentsontheroad.
40
Scenariosareexecutedinasimple,discrete-timesimulationen-
14
vironment with an execution rate of 20 frames per second. For
20 13
reproducingourresultsexactly,arandomseedof21shouldbe
usedwheneverthealgorithmusesrandomness.Note,theresults
12 8 5 4 2
wereconfirmedwithmultipleseeds,weonlyfixedtheseedfor 0 1 7 3 6 10
presentationinthepaper.
Ourscenariosareusuallyonlyafewsecondslong(insimulation −20 15
time),therefore,toavoidfindingirrelevantcausesandtospeed
160
upourimplementation,weremoveallstatesthataremorethan5 −40 11
secondsawayfromthecurrenttimestep𝑡 ofthesimulation.For
allscenarios,wesample𝐾 = 100counterfactualsequenceswith −60
asmoothingweight𝛼 =0.1,andlimitsof𝜏 𝑚𝑖𝑛 =2and𝜏 𝑚𝑎𝑥 =5
seconds. We picked 𝐾 so that it is large enough that a diverse −60 −40 −20 0 20 40 60
rangeoftrajectoriesissampledconsideringthatIGP2predictsup
to3distincttrajectoriesforeachagent.Thevaluefor𝜏 𝑚𝑖𝑛 isthe Figure7:S2with16spawnlocationsforagents.
planningperiodofIGP2(i.e.,thenumberofsecondsbetweentwo
callstoIGP2),while𝜏 𝑚𝑎𝑥 isthemaximumtemporaldistanceas
allowformoreagentswithoutasignificantchangetothebehaviour
describedabove.Wedonotrelyonanyexternaldatasetsandno
oftheego.Figures6to9showthespawnregionsofeachagent,in
pre-processingstepsareneededtorunourcode.
whichtheyareplacedrandomly.
B.1 ScalingwiththeNumberofAgents

### B.2 SizeandSamplingRobustness


### CEMAcanscaletoalargenumberofagents,whichmeansthatit

Wetestthesizerobustnessofmechanisticexplanationsbysamcanidentifytherelevantcausesbehindtheactionsoftheegoagent,
plingincreasinglylargerdatasetsusingAlgorithm1andforeach
eveniftherearenumerousirrelevantagentsaround,whichdidnot
datasetwererunAlgorithm2todeterminecausalattributions.We
haveacausaleffectontheactionsoftheego.Toshowthatthisis randomlysample𝐾 ∈{5,10,...,100}differentsamplesizes.Fora
true,weincreasethenumberofagentsinallfourscenarioswhile given𝐾,werepeatthesamplingprocess50times.Weplotthemean
makingsurethattheegoexecutesthesameactionsWethenshow
and95%bootstrappedconfidenceintervalsofthecausalattributions
thatthesamerelevantcauses,bothteleologicalandmechanistic, against𝐾.
arefoundbyCEMAbehindtheego’sactions. Usingthefactthatlim𝛼→∞ 𝜙 𝑖 = 𝑑 1 forall𝑖,weseethatinthe
Wealterthenumberoftotalagentsineachscenarioasfollows: limitas𝛼approachesinfinity,𝑝 𝜙approachesauniformdistribution

### S1:20agents;S2:16agents;S3:4agents;S4:16agents.Weonly

withprobability 1 forallelementsinΩ.Thuswecaninterpolate
increaseS3to5agents,asthescenariomapwastoocompactto 𝑑
betweentheoriginal𝑝 𝜃 andanapproximatelyuniformdistribution
3IGP2availableathttps://uoe-agents.github.io/IGP2/. bysetting𝛼 tolargerandlargervalues.

<!-- Page 12 -->


## C Computationalevaluation

20 1
WepresentourfullcomputationalresultsforallqueriesinFigures10and12to19.Figure19showsallassociative(i.e.,descriptive)
3 2
0 queries.Figures20to23showthecausalselectionresultsforthe
scalingexperimentsdescribedinAppendixB.1Eachfiguregives
−20 naturallanguagequestionsandthecorrespondingquerycontent.
Wealsogivethefullplotofcausalattributionsaswellastheresultsforrobustnessexperiments.Intheplotsofmechanisticcauses,
−40
numbersinparenthesesidentifytheIDofnon-egovehicles,ifthere
ismorethanonenon-ego.Thecodetoreproducetheseresultsis
−60 partofthesupplementarymaterial.
Detailsabouttheuserstudyfollowstheresultsofthissection.
−80 0
−100
−100 −75 −50 −25 0 25 50 75 100
Figure8:S3with4spawnlocationsforagents.
40
20
7 145 6
0 12 11 10 4 8
1
2
−20
9
−40 0
13
−60
3
−80
−100
−100 −75 −50 −25 0 25 50 75 100
Figure9:S4with16spawnlocationsforagents.
Table4:Thelistof𝛼 valuesusedforinterpolationinthe
samplingrobustnessexperiments.
0,0.1,0.14,0.18,0.25,0.34,0.45,0.62,0.83,1.13,1.53,
2.07,2.8,3.79,5.13,6.95,9.41,12.74,17.25,23.36,31.62

### Using the above, we perform our experiment for testing the

robustnessofoursystemagainstincreasinguncertaintyinexternal
predictionsofothervehicles’goalsandtrajectories.Wedefinea
list of twenty𝛼 values spaced on a logarithmic scale plus zero
givingintotal21distinctalphas(Table4).Foreach𝛼inthislist,we
sampleadatasetofsize𝐾 =50anddeterminecausalattributions
formechanisticcauses.

<!-- Page 13 -->

(a)Correspondingquestions:“Whywillyouchangelanes?”;“Whydoesitdecreasethetimetothegoal?”;“Whywillitbeslower?”
Conv. Type VID Tense Actions QueryTime ActionTime Negated Factuals
S1-A Why 0(AV) Future Changeleft 40 — No —

### Collision possible: No

Always reaches goal: Yes Past causes Present-future causes
Slower

### Faster


### Curvature

(1/m) Decelerate
Change right
Exit right

### Jerk

(m/s3) Exit straight Change left

### Exit straight

Angular velocity Slower Accelerate
(rad/s)

### Faster

Same vel.
Time to goal Same vel.
(s)
Rest of 4

### Rest of 2

1.4 1.2 1.0 0.8 0.6 0.4 0.2 0.0 0.5 0.0 0.5 1.0 1.5 0.50 0.25 0.00 0.25 0.50 0.75 1.00
(a) Reward difference (b) Coefficient importance (c) Coefficient importance
1.5
1.0
0.5
0.0
0.5
20 40 60 80 100
Number of samples (K)
thgiew
erutaeF
Past causes
Faster
1.0

### Change right

Exit straight
Slower
0.5
Same vel.
0.0
0.5
20 40 60 80 100
Number of samples (K)
thgiew
erutaeF
Present-future causes

### Slower

Decelerate
Exit right

### Faster

Accelerate
Same vel.
1.0
0.5
0.0
0.5
0 100 101
Smoothing weight ( )
thgiew
erutaeF
Past causes
1.0
0.5
0.0
0.5
0 100 101
Smoothing weight ( )
thgiew
erutaeF

### Present-future causes

Figure10:ResultsforthefirstthreequestionsinconversationS1-A.

<!-- Page 14 -->

Figure11:Correspondingquestion:“Whatifvehicle1hadn’tchangedlanestotherightbefore?”
Conv. Type VID Tense Actions QueryTime ActionTime Negated Factuals
S1-A Whatif 1 Past Changeright 75 — Yes —

### Collision possible: No

Always reaches goal: Yes Present-future causes
1.0
Exit straight
Curvature
(1/m) 0.8
Accelerate

### Jerk

(m/s3) 0.6 Decelerate

### No past causes because

this is a what-if query.
Angular velocity 0.4 Exit straight
(rad/s)

### Exit right

Time to goal 0.2
(s)
Rest of 5
0.0
0.6 0.5 0.4 0.3 0.2 0.1 0.0 0.0 0.2 0.4 0.6 0.8 1.0 1.0 0.5 0.0 0.5 1.0
(a) Reward difference (c) Coefficient importance
0.5
0.0
0.5
5 10 15 20 25 30 35 40
Number of samples (K)
thgiew
erutaeF
Present-future causes
Exit straight
Accelerate
Decelerate
Exit right
0.5
0.0
0.5
0 100 101
Smoothing weight ( )
thgiew
erutaeF

### Present-future causes

Figure12:ResultsforthelastquestioninconversationS1-A.

<!-- Page 15 -->

(a)Correspondingquestions:“Whyareyounotgoingstraight?”,“Whyisitslowertogostraightthen?”,“Anyotherreasons?”
Conv. Type VID Tense Actions QueryTime ActionTime Negated Factuals
S1-B Why 0 Present Gostraight 45 — Yes Changeleft

### Collision possible: No

Always reaches goal: No Past causes Present-future causes
Decelerate

### Faster


### Curvature

(1/m) Slower

### Change right

Exit straight

### Jerk

(m/s3) Exit straight Faster

### Exit right

Angular velocity Slower Change left
(rad/s)
Accelerate
Same vel.
Time to goal Same vel.
(s)
Rest of 4

### Rest of 2

0.00 0.25 0.50 0.75 1.00 1.25 1.50 1.75 0.5 0.0 0.5 1.0 1.5 0.8 0.6 0.4 0.2 0.0 0.2 0.4 0.6
(a) Reward difference (b) Coefficient importance (c) Coefficient importance
1.5
1.0
0.5
0.0
0.5
20 40 60 80 100
Number of samples (K)
thgiew
erutaeF
Past causes
Faster
0.50

### Change right

Exit straight
0.25 Slower
Same vel.
0.00
0.25
0.50
20 40 60 80 100
Number of samples (K)
thgiew
erutaeF
Present-future causes
Decelerate

### Slower

Exit straight

### Faster


### Exit right

Change left
Accelerate
Same vel.
1.0
0.5
0.0
0.5
1.0
0 100 101
Smoothing weight ( )
thgiew
erutaeF
Past causes
0.5
0.0
0.5
0 100 101
Smoothing weight ( )
thgiew
erutaeF

### Present-future causes

Figure13:ResultsforthefirstthreequestionsinconversationS1-B.

<!-- Page 16 -->

(a)Correspondingquestions:“Whydidn’tyoustoptogiveway?”,“Couldn’tithavecausedacollision?”,“Howdidyouknow?”
Conv. Type VID Tense Actions QueryTime ActionTime Negated Factuals
S2 Why 0 Past Giveway&stop 160 — Yes Giveway&accelerate

### Collision possible: No

Always reaches goal: No Past causes Present-future causes

### Exit left (1) Slower (1)

Curvature Exit straight (1) Exit left (1)
(1/m)

### Accelerate (1) Stops (1)

Exit straight (2) Exit left (2)

### Angular velocity

(rad/s) Maintain (2) Continue (2)

### Exit right (2) Maintain (2)

Jerk Decelerate (2) Decelerate (2)
(m/s3)
Exit left (2) Exit right (2)
Decelerate (1) Continue (1)

### Time to goal

(s) Exit right (1) Faster (1)

### Rest of 10 Rest of 9

0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 1.5 1.0 0.5 0.0 0.5 1.0 0.8 0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.8
(a) Reward difference (b) Coefficient importance (c) Coefficient importance
1.0
0.5
0.0
0.5
1.0
20 40 60 80 100
Number of samples (K)
thgiew
erutaeF

### Past causes


### Exit left (1)

Exit straight (1) 0.50

### Accelerate (1)

Exit right (2) 0.25

### Exit left (2)

Decelerate (1) 0.00
Exit right (1)
0.25
0.50
20 40 60 80 100
Number of samples (K)
thgiew
erutaeF
Present-future causes

### Slower (1)

Exit left (1)

### Stops (1)


### Exit left (2)

Exit right (2)
Continue (1)
Faster (1)
1.0
0.5
0.0
0.5
0 100 101
Smoothing weight ( )
thgiew
erutaeF
Past causes
0.5
0.0
0.5
0 100 101
Smoothing weight ( )
thgiew
erutaeF

### Present-future causes

Figure14:ResultsforthefirstthreequestionsinconversationS2.

<!-- Page 17 -->

(a)Correspondingquestion:“Whatifitwentstraightinstead?”
Conv. Type VID Tense Actions QueryTime ActionTime Negated Factuals
S2 Whatif 1 Past Gostraight 110 — No Turnleft

### Collision possible: No

Always reaches goal: Yes Present-future causes
1.0

### Continue (1)

Curvature Maintain (1)
(1/m) 0.8 Faster (1)
Exit straight (2)

### Maintain (2)


### Angular velocity

(rad/s) 0.6 Exit left (2)

### No past causes because Decelerate (2)

this is a what-if query. Exit right (2)
Jerk 0.4 Stops (1)
(m/s3)

### Slower (1)


### Exit left (1)

Time to goal 0.2 Exit right (1)
(s) Decelerate (1)
Rest of 7
0.0
0.0 0.5 1.0 1.5 2.0 0.0 0.2 0.4 0.6 0.8 1.0 0.8 0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.8
(a) Reward difference (c) Coefficient importance
0.5
0.0
0.5
10 20 30 40 50 60 70 80 90
Number of samples (K)
thgiew
erutaeF
Present-future causes
Maintain (1)

### Continue (1)

Exit right (1)
Decelerate (1)
0.5
0.0
0.5
0 100 101
Smoothing weight ( )
thgiew
erutaeF

### Present-future causes

Figure15:ResultsforthelastquestioninconversationS2.

<!-- Page 18 -->

(a)Correspondingquestions:“Willyoustoptogiveway?”,“Howdoyouknowwewon’tcollidewiththeoncomingcar?”
Conv. Type VID Tense Actions QueryTime ActionTime Negated Factuals
S3 Why 0 Present Giveway&stop 90 — Yes Giveway&accelerate

### Collision possible: No

Always reaches goal: Yes Past causes Present-future causes

### Exit right

Change right

### Curvature

(1/m) Accelerate

### Accelerate


### Change right

Angular velocity

### Decelerate

(rad/s) Maintain

### Maintain

(m J / e s r 3 k ) Decelerate Change left
Change left

### Exit left

Time to goal Change left
(s)
Rest of 4

### Rest of 4

0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.0 0.5 0.0 0.5 1.0 0.5 0.0 0.5 1.0 1.5
(a) Reward difference (b) Coefficient importance (c) Coefficient importance
1.0
0.5
0.0
0.5
1.0
20 40 60 80 100
Number of samples (K)
thgiew
erutaeF

### Past causes


### Change right (1)

Accelerate (1) 1.5

### Maintain (1)

Decelerate (1) 1.0
Exit left (1)
0.5
0.0
0.5
20 40 60 80 100
Number of samples (K)
thgiew
erutaeF
Present-future causes
Exit right (1)

### Accelerate (1)

Change left (1)
Maintain (1)
1.0
0.5
0.0
0.5
1.0
0 100 101
Smoothing weight ( )
thgiew
erutaeF
Past causes
1.0
0.5
0.0
0 100 101
Smoothing weight ( )
thgiew
erutaeF

### Present-future causes

Figure16:ResultsforthelasttwoquestionsinconversationS3.Therearemultiple“changeleft”amongthepresent-future
causesasthenon-egocouldchangelanesleftatmanypointsintheroundabout.CEMAdifferentiatesbetweenallofthem,we
onlyshowitherethiswayforbrevity.

<!-- Page 19 -->

(a)Correspondingquestions:“Whyareyounotstoppingtogiveway?”,“Whyisitsafetoturnleft?”
Conv. Type VID Tense Actions QueryTime ActionTime Negated Factuals
S4 Why 0 Present Giveway&stop 140 — Yes Turnleft&accelerate

### Collision possible: No

Always reaches goal: No Past causes Present-future causes
Exit left (3) StopMA (3)

### Decelerate (3) Stops (3)

Curvature Slower (3) Decelerate (3)
(1/m) Faster (4) Faster (3)
E M x a it i n ri t g a h in t ( ( 1 1 ) ) Faster (1)

### StopMA (1) StopMA (1)


### Angular velocity Stops (1) Stops (1)

(rad/s) Exit straight (4) Maintain (1)

### Maintain (4) Same vel. (1)


### Decelerate (4) Exit left (3)

Jerk Exit right (4) Continue (1)
(m/s3)
Ex

## A

i
c
t
c
s
e
tr
le
a
r
ig
a
h
te
t
(
(
1
1
)
) Acc

## E

e
x
le
it
r a
le
t
f
e
t
(
(
1
1
)
)
E S x l i o t w le e f r t ( ( 4 1 ) ) Slower (1)
Time to goal Faster (3) Slower (3)
(s) Exit straight (3) Continue (3)
Accelerate (3) Accelerate (3)

### Rest of 18 Rest of 19

0.0 0.5 1.0 1.5 2.0 2.5 3.0 0.8 0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.8 0.6 0.4 0.2 0.0 0.2 0.4 0.6
(a) Reward difference (b) Coefficient importance (c) Coefficient importance
0.5
0.0
0.5
20 40 60 80 100
Number of samples (K)
thgiew
erutaeF

### Past causes


### Decelerate (3)

Exit left (3) 0.50

### Slower (3)

Exit right (1) 0.25

### Exit straight (1)

Exit left (1) 0.00

### Faster (3)

Accelerate (3) 0.25
Exit straight (3)
0.50
20 40 60 80 100
Number of samples (K)
thgiew
erutaeF
Present-future causes
Decelerate (3)

### Stops (3)

StopMA (3)
Faster (3)
Slower (1)

### Slower (3)


### Continue (3)

Accelerate (3)
0.5
0.0
0.5
0 100 101
Smoothing weight ( )
thgiew
erutaeF
0.50
0.25
0.00
0.25
0.50
0 100 101
Smoothing weight ( )
thgiew
erutaeF
Figure17:ResultsforthefirsttwoquestionsinconversationS4.

<!-- Page 20 -->

(a)Correspondingquestions:“Whatifvehicle3wentstraight?”
Conv. Type VID Tense Actions QueryTime ActionTime Negated Factuals
S4 Whatif 3 Future Gostraight 100 — No Stop

### Collision possible: No

Always reaches goal: Yes Present-future causes
1.0

### Accelerate (3)

Curvature Continue (3)
(1/m) 0.8 Continue (1)
Maintain (1)

### Slower (1)


### Angular velocity

(rad/s) 0.6 Faster (1)

### No past causes because Same vel. (1)

this is a what-if query. Accelerate (1)
Jerk 0.4 Stops (1)
(m/s3)
StopMA (1)

### StopMA (3)

Time to goal 0.2 Decelerate (3)
(s) Stops (3)
Rest of 13
0.0
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.6 0.4 0.2 0.0 0.2 0.4 0.6
(a) Reward difference (c) Coefficient importance
0.5
0.0
0.5
10 20 30 40 50 60 70 80
Number of samples (K)
thgiew
erutaeF
Present-future causes
Decelerate (3)

### Stops (3)


### StopMA (3)

Accelerate (3)
Continue (3)
0.50
0.25
0.00
0.25
0.50
0 100 101
Smoothing weight ( )
thgiew
erutaeF

### Feature

Decelerate (3)

### Stops (3)


### StopMA (3)

Accelerate (3)

### Continue (3)

Figure18:ResultsforthelastquestioninconversationS4.
Figure19:Allqueriesthatprovideanassociativeexplanation;acrossallconversations.
Conv. Type VID Tense Actions QueryTime ActionTime Negated Factuals
S1-A Whatif 1 Past Changeright 75 — Yes —

### S1-B What 0 — — 45 70 No —

S2 Whatif 0 Past Gostraight 110 — No Turnleft

### S3 What 0 — — 105 80 No —

S4 Whatif 1 Future Gostraight 100 — No Stop

<!-- Page 21 -->


### Collision possible: Yes

Always reaches goal: Yes Past causes Present-future causes

### Slower (13) Slower (1)

Curvature Slower (11) Slower (3)
(1/m)

### Maintain (4) Decelerate (10)

Angular velocity Exit right (13) Change left (3)
(rad/s)
Exit right (1) Exit right (1)
Maintain (13) Slower (12)

### Jerk

(m/s3) Decelerate (10) Decelerate (4)
Exit straight (10) Change right (12)

### Time to goal

(s) Slower (1) Decelerate (5)

### Accelerate (12) Change right (10)

2.0 1.5 1.0 0.5 0.0 0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.8
Figure20:Top10causalimportancesintheextendedscenario1with20agents.

### Collision possible: No

Always reaches goal: Yes Past causes Present-future causes

### Exit straight (1) Faster (2)

Curvature Exit left (2) Stops (1)
(1/m)

### Accelerate (1) Exit left (1)

Angular velocity Exit right (5) Faster (1)
(rad/s) Decelerate (5) Faster (9)
Exit right (4) Accelerate (2)

### Jerk

(m/s3) Exit left (9) Accelerate (9)

### Exit left (5) Faster (4)

Time to goal Exit right (2) Exit right (9)
(s)

### Exit straight (4) Continue (2)

0 2 4 6 8 10 0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.8 0.3 0.2 0.1 0.0 0.1 0.2 0.3
Figure21:Top10causalimportancesintheextendedscenario2with16agents.

### Collision possible: No

Always reaches goal: Yes Past causes Present-future causes

### Change right (1)

Accelerate (1) Change right (1)

### Curvature

(1/m) Accelerate (1)
Decelerate (1) Exit right (2)

### Accelerate (2)


### Angular velocity Change right (1)

(rad/s) Change right (1) Change right (1)

### Maintain (2)

Jerk Exit left (1) Decelerate (2)
(m/s3) Change right (1)

### Continue (2)


### Maintain (1) Decelerate (1)


### Time to goal Change left (1)

(s) Rest of 12 Change left (1)

### Rest of 9

0.0 0.5 1.0 1.5 2.0 2.5 3.0 1.251.000.750.500.250.000.250.500.75 1.0 0.5 0.0 0.5 1.0
(a) Cost difference (b) Coefficient importance (c) Coefficient importance
Figure22:Top10causalimportancesintheextendedscenario3with4agents.

### Collision possible: Yes

Always reaches goal: No Past causes Present-future causes

### Decelerate (14) Stops (3)

Curvature Exit right (11) StopMA (3)
(1/m)

### Exit right (12) Decelerate (3)

Angular velocity Faster (3) Faster (6)
(rad/s) Exit left (6) Accelerate (12)
Slower (11) Faster (12)

### Jerk

(m/s3) Exit straight (1) Faster (3)

### Decelerate (3) Stops (6)

Time to go (s a ) l Exit left (3) Exit right (12)

### Maintain (4) Accelerate (1)

2.5 2.0 1.5 1.0 0.5 0.0 0.4 0.2 0.0 0.2 0.4 0.6 0.6 0.4 0.2 0.0 0.2 0.4 0.6
Figure23:Top10causalimportancesintheextendedscenario4with16agents.

<!-- Page 22 -->

D USERSTUDY D.1.3 Creating the Baseline Dataset. Having collected explanationsinSurvey1,weneededtoassembleausefulandhigh-quality

### D.1 SurveyMethodology

baselinedatasetforthesecondsurvey.Asthesecondsurveyisonly

### Weperformedtwosurveysaspartoftheuserstudy.Thefirstelicited

concernedwithourfourmainscenarios,weexcludedallexplanahigh-qualityexplanationsfromparticipantsaboutthebehaviour
tionsfromSurvey1thatwerenotaboutscenariosS1-4.Thislefta
oftheautonomousvehicleasshowninpre-recordedvideoclips.
totalof408explanations.Fromthis,wefurtherremovedanother

### ThesecondsurveywasusedtocomparetheexplanationsofCEMA

26explanationswhichwerevacuous,thatis,theydidnotcontain
againstthiscollectedbaselinedatasetofhuman-writtenexplanaanyusefulinformationaboutthescenario,ortheyexpressedhighly
tions.Weincludethedatasetofhigh-qualityhumanexplanations,
personalorobviouslyincorrectopinions.
responsestothesecondsurvey,andcodetoreproduceourstatis-
ToselectexplanationsforthebaselinedatasetforSurvey2,we
ticalanalysisofthesecondsurveyaspartofthesupplementary
setupanannotationschemewiththefollowingelements:
materials.
• Overquality:Scaleon1to5.Theoverallqualityofanex-
D.1.1 Participants. Weusedthecrowd-sourcingplatformProlific planationasdeterminedbyitsrelevancytothescenario,its
torecruitparticipants.WerecruitedfromtheUSA,asthevideo linguisticcorrectness,andsubjectiveclarity;
recordingswereinright-handedtraffic,andfilteredforparticipants • Complexity:Scaleon1to5.ThecomplexityoftheexplanawhosefirstlanguagewasEnglish.Participantswerepaidanaverage tionasdeterminedbyitslengthandthenumberofcausal
of£11/handwereshownourethicsapprovalandaconsentform relationshipsmentionedinit;
whichtheyhadtoacceptbeforebeingallowedtofilloutthesurveys. • Type:Whethertheexplanationisateleological(1),mecha-
Regardingthefirstsurvey,54participantsfilleditoutwitha nistic(2),orassociative(i.e.,descriptive)(3)explanation,or
mediandurationofcompletionof25minutesand37seconds.The somecombinationofallthree;
sexdistributionwas25malesand29females.Theparticipants’ • Counterfactual:Boolean.Whethertheexplanationisconagerangedbetween19to73years,withamedianof36years.No trastiveornot.
participantswereexcludedforfailingattentionchecksinthefirst Weannotatedallremaining382explanationswiththisschemeand
survey. randomlypicked25explanationsforeachofthefourscenarios
Regardingthesecondsurvey,200participantsfilleditoutwitha S1-4.Wealsocorrectedanyobvioustyposineachexplanation.Our
mediandurationofcompletionof9minutesand34seconds.Sexes selectioncriteriaincludedonlythehighestqualityexplanations
weredistributedas99malesand101females.Theparticipants’ (level4or5)andawiderangeofcombinationsofcomplexities,
agerangedbetween19to77yearswithamedianof35years.One types,andcounterfactualswascoveredaswell.Thisprocessinthe
participantwasexcludedforfailingattentionchecksinthesecond endresultedinaselecteddatasetofhigh-qualitybaselinehumansurvey. writtenexplanationswithatotalsizeof100explanations.
D.1.2 Survey1:DesignandProcedure. Inthefirstsurvey,people D.1.4 Survey2:DesignandProcedure. WeusedSurvey2tomeawereshown7scenariosoutofacollectionof14includingthefour suretheeffectsofexplanationsontrustandtounderstandwhat
scenariosusedintheevaluationofCEMA.Foreachscenario,people kindofexplanationspeoplepreferred:theonesgeneratedbyCEMA
weretoldwhatthegoaloftheegoagentis,andthentheywere orthehuman-writtenbaselineexplanations.Werandomisedsevshownashort(about5to15-second-long)videoofthescenario.The eralpartsofthissurvey,soforlaterreference,wewillgivenames
videosweretop-downanimationsrecordedinthesoftwareRoad- torandomvariablesstartingwithanuppercaseletter(shownin
Runner2023abyMathWorks.Weincludethevideosforthefour italicsinparentheses),forexample,Type.
scenariosusedinourevaluationinthemainpaper.Afterwatching Beforethestartofthesurvey(aftergivingconsent),weasked
thevideos,participantswereaskedtoanswerthefollowingfour participantstoanswerthreequestionstomeasuretheirpreviousexquestions: posuretoautonomousdrivingsystems(AVExperience),asclassified
(1) Describetheactionsofthebluecar,self-drivingcar. bytheSAEautomationscale[36].Thequestionwere:
(2) Explainwhythebluecar,self-drivingcartooktheseactions •“Haveyoueverusedadriver-assistancesystem?Examples
overdifferentactionstoreachitsgoal. ofdriver-assistancesystemsareadaptivecruisecontrol,lane
(3) Explainhowthebluecar,self-drivingcarwasinfluencedin keepingassistance,andparkingassistance.”(SAEL1-2);
thescenariototaketheseactions. •“Haveyoueverusedapartiallyautonomousself-drivingcar?
(4) Describechangestothescenariosothatthebluecar,self- Apartiallyautonomousself-drivingcarisonewhichcan
drivingcartakesdifferentactions?(Thenewactionsneednot driveonitsown,butstillrequiresanattentivehumandriver.
bethebestactionsintheoriginalscenario) AnexampleistheTeslaAutopilot.”(SAEL3);
•“Haveyoueverusedafullyautonomousself-drivingcar?
With50%chance,participantswereshowneither“car”or“self-

### Afullyautonomousself-drivingcarisonewhichdoesnot

driving”car.Wedidthisinordertogetwidecoverageofexplarequireahumandriver.AnexampleistheWaymoOneridenations,incasepeoplewereaprioribiasedagainstautonomous
hailingservice.”(SAEL4).
vehicles.Participantshadtoanswerallfourquestionsintheirown
words,enteringtheirresponsesintounconstrainedfree-textboxes. ThecoreofSurvey2wastheexplanationratingscales.Foreach
Wealsointroducedtwoattentionchecksattheendofthepageof participant,werandomlyandwithequalchancepickedtwoofthe
randomscenarios#3and#6. fourscenarios(Scenario),aswellas10explanationstoberanked.

<!-- Page 23 -->

Theexplanationswerepickedfromasetof30totalexplanations ofthesurveydata.Forouranalysis,weusedtheRprogramming
per scenario consisting of 5 CEMA-generated explanations the language[35].
25selectedexplanationsfromSurvey1(Type).Foreachscenario,
D.2.1 Pre-processing. Wepre-processedtherawsurveydatato
similarlytoSurvey1,wefirstshowedeachparticipantthevideo
makeitmoreamenabletoanalysiswithR.Thisinvolvedcalcurecordingofthescenario,thoughthistimewedidnottellthem
latingthemeanratingsforeachparticipantgroupedbythetype
what the goal of the ego vehicle was to avoid biasing people’s
ofexplanation(CEMAorHuman)andthescenario(Scenario).It
ratings.Wethenaskedparticipantstorateeachexplanationona
alsoinvolvedcollatingthetrustresponsesacrossparticipantsinto
5-pointLikertscalebasedonhowwelleachstatementexplained
asinglecolumngroupedbythetrustscale(TrustQuestion)and
theactionsoftheegovehicle(MeanRating).With50%chance,we
turningthedataintolongformat.Finally,inadditiontotherawexalsohighlightedtoparticipantsinboldtypefacetheexplanations
planationratings,wealsoincludedfieldsforthemeanexplanation
thatweregeneratedbyCEMA(Highlight),andmadesurethatthey
ratingsofparticipantsgroupedbytheirType(MeanCEMARating
wereinformedthattheseexplanationsweregeneratedbytheego
andMeanHumanRating).
agentitself.
Tomeasurechangestotrustlevels,wecreatedthesecondsur- D.2.2 Modelling. WeusedGaussian-familymixed-effectslinear
veywithabetween-subjectsdesign,wherethe“treatment”was modelstounderstandtherelationshipsbetweenthevariousvarishowingtheparticipantstheexplanationsandhavingthemen- ables.
gagewiththeexplanationsthroughtheirratings.Therefore,we Tounderstandhowparticipants’ratingsofexplanationsvaried
assignedeachparticipantrandomlywitha50%chanceintooneof withdifferentvariables(correspondingtotestingH1),wefitteda
twogroups:eitheransweringthetrustquestionsbeforeseeingthe modeltoourdatapredictingthemeanexplanationratings(Meanexplanationsorafter(PreExplanation).Toactuallymeasurepeople’s Rating)ofparticipants.WeincludedthecrossingbetweenHighlightrust(TrustRating)inAVs,weusedthetrustscalesrecommended tAVandType,andAVExperienceasindependentvariablesencoding
byHoffmanetal.[20]adaptedtotheADdomain.Peoplewereasked themusingdummycoding.Wesetthereferencelevels:Highlighthefollowingninequestionsinsomerandomorder(TrustQuestion) tAV=TRUE,Type=CEMA,AVExperience=0(noexperience).The
andaskedtoratethemona5-pointLikertscale: modelalsoincludedvaryinginterceptsforeachscenario.

### Tounderstandhowparticipants’trustlevelschangedaftersee-

(1)“Iamconfidentinself-drivingcars.Ifeelthattheyworkwell”
ingexplanations(correspondingtotestingH2),wepredictedthe
(confidenceinAVs).
meantrustratings(TrustRating)ofparticipants.Weincludedasfac-
(2)“Thedecisionsofself-drivingcarsarepredictable.”(AVdecitors,PreExplanation,HighlightAV,AVExperience,andthecrossing
sionsarepredictable)
betweenMeanCEMARatingandMeanHumanRating.Weencoded
(3)“Self-driving cars are reliable. I can count on them to be
thecategoricalfactorswithdummycoding,settingthereference
correctatalltimes.”(AVsarereliable)
levelsasfollows:PreExplanation=TRUE,HighlightAV=TRUE,AV-
(4)“Ifeelsaferelyingonaself-drivingcar.Itwillmaketheright
Experience=0. We also included varying intercepts grouped by
decisions.”(AVsarealwayscorrect)
TrustQuestion.
(5)“Self-drivingcarsareefficient,inthattheymakedecisions
Wehavealsotestedmorecomplexmodelswithmorevariables,
veryquickly.”(AVsareefficient)
however,therewasnosignificantchangeinresultsbyincluding
(6)“Iamwaryofself-drivingcars.”(WaryofAVs)
these,andthemodelwouldoftennotconverge,soweoptedto
(7)“Self-drivingcarsmakebetterdecisionsthannovicedrivers.”
usetheleastcomplexbutmostexpressivemodel,whichwehave
(AVsbetterthannovice)
reportedhere.
(8)“Self-drivingcarsmakebetterdecisionsthanexperienced
drivers.”(AVsbetterthanexpert) D.3 Results
(9)“Iwouldliketouseself-drivingcarsfordecisionmaking.”
Thefollowingsectionpresentsadetailedviewofthequantitative
(WillingtoAVs)
resultsofouranalysisofSurvey2.
D.1.5 Post-SurveyQuestions. Attheendofbothsurveys,partici- D.3.1 SummaryStatistics. WepresentinTables5and6thesumpantswereaskedtofilloutabriefsurveyabouttheirdrivingex- marystatisticsforthetrustlevels.InTables7to10,wegivethe
perienceaboutwhethertheyholdavaliddriver’slicense(License), summarystatisticsoftheratingsofall30questionsforeachscehowmanyyearsofdrivingexperiencetheyhave(Experience),how nario.ThequestionsinboldweregeneratedbyCEMA.Wealso
manydaysaweektheydrive(Frequency),andhowmanymileson plotthedistributionsoftrustbeforeandafterseeingexplanations
averagetheydriveinayear(Distance).Wealsoaskedthemvolun- inFigures24and25.
tarydemographicquestionsabouttheiragerange(Age),gender
(Gender),andeducationlevel(Education).Finally,participantshad
theopportunityattheendofeachsurveytogiveanymannerof
feedbacktheythoughtworthyofmentioning.

### D.2 Analysis

Tounderstandtheeffectsofexplanationsandtheratingsofdifferent
typesofexplanations,weconductedadetailedstatisticalanalysis

<!-- Page 24 -->

Table5:Trustlevelsbeforeseeingexplanations(PreExplanation=TRUE).Trustscalecorrespondingtotheenumerationin
AppendixD.1.4.
trustscale count mean std min 25% 50% 75% max
1 101.0 2.653465 1.117458 1.0 2.00 2.0 4.00 5.0
2 101.0 3.099010 1.081711 1.0 2.00 3.0 4.00 5.0
3 101.0 2.297030 1.072796 1.0 1.00 2.0 3.00 5.0
4 101.0 2.425743 1.116661 1.0 2.00 2.0 3.00 5.0
5 101.0 3.297030 1.091280 1.0 3.00 3.0 4.00 5.0
6 101.0 3.881188 1.022616 1.0 3.00 4.0 5.00 5.0
7 101.0 3.217822 1.109991 1.0 3.00 3.0 4.00 5.0
8 101.0 2.376238 1.164916 1.0 1.00 2.0 3.00 5.0
9 101.0 2.415842 1.168480 1.0 2.00 2.0 3.00 5.0
Table6:Trustlevelsafterseeingexplanations(PreExplanation=FALSE).Trustscalecorrespondingtotheenumerationin
AppendixD.1.4.
trustscale count mean std min 25% 50% 75% max
1 99.0 2.696970 1.092222 1.0 2.00 2.0 3.00 5.0
2 99.0 3.333333 1.133893 1.0 3.00 4.0 4.00 5.0
3 99.0 2.323232 1.095709 1.0 1.50 2.0 3.00 5.0
4 99.0 2.575758 1.107405 1.0 2.00 2.0 4.00 5.0
5 99.0 3.434343 0.949346 1.0 3.00 4.0 4.00 5.0
6 99.0 3.838384 1.037138 1.0 3.00 4.0 5.00 5.0
8 99.0 3.303030 1.063826 1.0 3.00 3.0 4.00 5.0
9 99.0 2.545455 1.032855 1.0 2.00 3.0 3.00 5.0
10 99.0 2.595960 1.105821 1.0 2.00 2.0 3.50 5.0
Confidence AV decisions AVs are AVs are AVs are Wary of AVs AVs better AVs better Willing to
in AVs are predictable reliable always correct efficient (lower better) than novice than expert use AVs
4.0
3.5
3.0
2.5
2.0
Before After Before After Before After Before After Before After Before After Before After Before After Before After
gnitaR
tsurT
Figure24:Meanratingsofparticipantsonthe9trustscalesbeforeandafterhavingseenexplanationswithstandarderror.
Scenario 1 Scenario 2 Scenario 3 Scenario 4
5
Type
4

## 3 Cema

2 Human
1
Highlight No highlight Highlight No highlight Highlight No highlight Highlight No highlight
Figure25:RatingsofCEMA’sandhumanexplanationswithbootstrapped95%confidenceinterval(CI)groupedbywhether
CEMA’sexplanationswerehighlighted.Theeffectofhighlightingissignificantunderourmixed-effectsmodel(𝑝 <0.05).

<!-- Page 25 -->

Table7:Basestatisticsofexplanationratingsfortheselected30questionsinScenario1.
question count mean std min 25% 50% 75% max
1 100.0 2.640000 1.267464 1.0 1.0 3.0 3.00 5.0
2 26.0 3.461538 1.103839 1.0 3.0 4.0 4.00 5.0
3 100.0 3.730000 1.081105 1.0 3.0 4.0 5.00 5.0
4 26.0 2.807692 1.059027 1.0 2.0 3.0 3.75 5.0
5 100.0 4.100000 1.010051 2.0 3.0 4.0 5.00 5.0
6 26.0 3.384615 0.803837 2.0 3.0 3.0 4.00 5.0
7 23.0 3.217391 1.241572 1.0 2.5 3.0 4.00 5.0
8 26.0 3.153846 1.255143 1.0 2.0 3.0 4.00 5.0
9 25.0 3.400000 1.118034 1.0 3.0 3.0 4.00 5.0
10 26.0 2.653846 1.198075 1.0 2.0 3.0 3.00 5.0
11 27.0 3.259259 1.163304 1.0 2.0 3.0 4.00 5.0
12 27.0 3.777778 1.012739 2.0 3.0 4.0 4.50 5.0
13 24.0 2.541667 1.062367 1.0 2.0 2.0 3.25 4.0
14 24.0 2.958333 1.334465 1.0 2.0 3.0 4.00 5.0
15 26.0 3.076923 1.262476 1.0 2.0 3.0 4.00 5.0
16 27.0 3.518519 1.087353 1.0 3.0 4.0 4.00 5.0
17 28.0 3.428571 0.997351 1.0 3.0 3.0 4.00 5.0
18 26.0 2.923077 1.293772 1.0 2.0 3.0 4.00 5.0
19 27.0 3.333333 1.176697 1.0 2.0 3.0 4.00 5.0
20 24.0 2.958333 1.122078 1.0 2.0 3.0 4.00 5.0
21 27.0 2.851852 0.988538 1.0 2.0 3.0 3.00 5.0
22 26.0 3.384615 1.202561 1.0 3.0 3.5 4.00 5.0
23 27.0 3.962963 0.939782 2.0 3.0 4.0 5.00 5.0
24 27.0 4.111111 1.219500 1.0 3.5 5.0 5.00 5.0
25 26.0 3.153846 1.120439 1.0 3.0 3.0 4.00 5.0
26 27.0 3.740741 0.813000 2.0 3.0 4.0 4.00 5.0
27 25.0 2.800000 1.258306 1.0 2.0 3.0 3.00 5.0
28 27.0 3.629630 1.005682 2.0 3.0 4.0 4.00 5.0
29 25.0 3.560000 0.916515 1.0 3.0 4.0 4.00 5.0
30 25.0 1.800000 0.912871 1.0 1.0 2.0 2.00 4.0

<!-- Page 26 -->

Table8:Basestatisticsofexplanationratingsfortheselected30questionsinScenario2.
question count mean std min 25% 50% 75% max
1 101.0 2.861386 1.191887 1.0 2.00 3.0 4.00 5.0
2 27.0 3.555556 1.250641 1.0 3.00 4.0 4.00 5.0
3 101.0 3.316832 1.264363 1.0 2.00 4.0 4.00 5.0
4 27.0 2.740741 1.163304 1.0 2.00 3.0 4.00 5.0
5 101.0 3.386139 1.288179 1.0 2.00 4.0 4.00 5.0
6 24.0 1.750000 1.032094 1.0 1.00 1.0 2.25 4.0
7 25.0 2.640000 1.319091 1.0 1.00 3.0 3.00 5.0
8 25.0 3.440000 1.157584 1.0 3.00 4.0 4.00 5.0
9 26.0 3.769231 1.274604 1.0 3.00 4.0 5.00 5.0
10 27.0 3.740741 1.195909 1.0 3.50 4.0 4.50 5.0
11 26.0 3.076923 1.293772 1.0 2.00 3.0 4.00 5.0
12 25.0 3.160000 1.312758 1.0 2.00 3.0 4.00 5.0
13 27.0 3.222222 1.368136 1.0 2.50 3.0 4.00 5.0
14 26.0 2.884615 1.423430 1.0 2.00 3.0 4.00 5.0
15 26.0 3.846154 0.967153 1.0 3.25 4.0 4.00 5.0
16 27.0 2.851852 1.199478 1.0 2.00 3.0 4.00 5.0
17 26.0 3.153846 1.461296 1.0 2.00 3.5 4.00 5.0
18 27.0 3.518519 1.369176 1.0 2.00 4.0 4.50 5.0
19 26.0 1.538462 0.859338 1.0 1.00 1.0 2.00 3.0
20 25.0 2.960000 1.513275 1.0 2.00 3.0 5.00 5.0
21 26.0 2.923077 1.262476 1.0 2.00 3.0 4.00 5.0
22 26.0 3.269231 1.372813 1.0 2.00 3.5 4.00 5.0
23 25.0 3.080000 1.222020 1.0 2.00 3.0 4.00 5.0
24 27.0 2.555556 1.527525 1.0 1.00 2.0 4.00 5.0
25 26.0 3.500000 0.948683 2.0 3.00 3.5 4.00 5.0
26 27.0 2.925926 1.327981 1.0 2.00 3.0 4.00 5.0
27 27.0 3.740741 1.403090 1.0 3.00 4.0 5.00 5.0
28 27.0 3.222222 1.086042 1.0 2.00 4.0 4.00 5.0
29 27.0 2.925926 1.412198 1.0 2.00 3.0 4.00 5.0
30 27.0 3.111111 1.476309 1.0 2.00 3.0 4.00 5.0

<!-- Page 27 -->

Table9:Basestatisticsofexplanationratingsfortheselected30questionsinScenario3.
question count mean std min 25% 50% 75% max
1 98.0 2.857143 1.192762 1.0 2.00 3.0 4.00 5.0
2 26.0 3.307692 1.123182 1.0 3.00 3.0 4.00 5.0
3 98.0 3.693878 1.106757 1.0 3.00 4.0 5.00 5.0
4 25.0 2.600000 1.258306 1.0 2.00 3.0 3.00 5.0
5 98.0 3.163265 1.289880 1.0 2.00 3.0 4.00 5.0
6 23.0 2.478261 1.591728 1.0 1.00 3.0 3.50 5.0
7 26.0 3.346154 1.263085 1.0 2.00 4.0 4.00 5.0
8 26.0 3.884615 1.275207 1.0 3.00 4.0 5.00 5.0
9 26.0 3.653846 1.354764 1.0 3.00 4.0 5.00 5.0
10 25.0 3.320000 1.314027 1.0 2.00 3.0 4.00 5.0
11 25.0 3.360000 1.254326 1.0 3.00 3.0 5.00 5.0
12 24.0 3.458333 1.215092 1.0 3.00 4.0 4.00 5.0
13 25.0 3.160000 1.247664 1.0 2.00 3.0 4.00 5.0
14 26.0 2.192308 1.414757 1.0 1.00 2.0 3.00 5.0
15 26.0 3.692308 1.378963 1.0 3.00 4.0 5.00 5.0
16 26.0 2.730769 1.457606 1.0 1.00 3.0 4.00 5.0
17 26.0 2.807692 1.497177 1.0 1.25 3.0 4.00 5.0
18 26.0 3.692308 1.225373 1.0 3.00 4.0 5.00 5.0
19 24.0 2.333333 1.403928 1.0 1.00 2.0 3.25 5.0
20 23.0 3.478261 1.441892 1.0 2.50 4.0 5.00 5.0
21 26.0 2.692308 1.257592 1.0 2.00 3.0 3.00 5.0
22 27.0 3.925926 1.106829 1.0 3.00 4.0 5.00 5.0
23 25.0 3.760000 1.267544 1.0 3.00 4.0 5.00 5.0
24 25.0 3.040000 1.171893 1.0 2.00 3.0 4.00 5.0
25 27.0 3.814815 1.075498 1.0 3.00 4.0 5.00 5.0
26 26.0 2.730769 1.218448 1.0 2.00 3.0 3.75 5.0
27 26.0 2.538462 1.475961 1.0 1.00 2.0 4.00 5.0
28 25.0 2.520000 1.326650 1.0 1.00 2.0 3.00 5.0
29 26.0 2.115385 1.107318 1.0 1.00 2.0 3.00 4.0
30 25.0 3.680000 1.069268 2.0 3.00 4.0 5.00 5.0

<!-- Page 28 -->

Table10:Basestatisticsofexplanationratingsfortheselected30questionsinScenario4.
question count mean std min 25% 50% 75% max
1 101.0 2.871287 1.270145 1.0 2.00 3.0 4.00 5.0
2 27.0 3.629630 1.079464 1.0 3.00 4.0 4.00 5.0
3 25.0 3.560000 1.083205 2.0 3.00 3.0 5.00 5.0
4 101.0 2.900990 1.360183 1.0 2.00 3.0 4.00 5.0
5 101.0 3.722772 1.078136 1.0 3.00 4.0 5.00 5.0
6 27.0 2.777778 1.154701 1.0 2.00 3.0 3.00 5.0
7 24.0 3.833333 0.868115 2.0 3.00 4.0 4.25 5.0
8 26.0 3.346154 1.324909 1.0 2.00 3.0 4.75 5.0
9 27.0 3.074074 1.639088 1.0 1.00 3.0 4.50 5.0
10 26.0 3.076923 1.440085 1.0 2.00 3.0 4.00 5.0
11 27.0 3.925926 1.141050 1.0 3.50 4.0 5.00 5.0
12 26.0 3.269231 1.250846 1.0 3.00 3.0 4.00 5.0
13 26.0 3.730769 1.041449 1.0 3.00 4.0 4.00 5.0
14 26.0 3.346154 1.383974 1.0 2.00 3.0 5.00 5.0
15 26.0 3.730769 1.401647 1.0 3.00 4.0 5.00 5.0
16 26.0 3.269231 1.401647 1.0 2.25 3.0 4.75 5.0
17 25.0 2.520000 1.084743 1.0 2.00 3.0 3.00 5.0
18 27.0 3.148148 1.166972 1.0 2.00 4.0 4.00 5.0
19 27.0 2.555556 1.187542 1.0 2.00 3.0 3.00 5.0
20 27.0 3.518519 1.155934 1.0 3.00 4.0 4.00 5.0
21 27.0 3.000000 1.441153 1.0 2.00 3.0 4.00 5.0
22 25.0 3.840000 1.027943 2.0 3.00 4.0 5.00 5.0
23 27.0 2.555556 1.187542 1.0 2.00 2.0 3.50 5.0
24 26.0 3.461538 1.475961 1.0 2.25 4.0 4.75 5.0
25 26.0 2.846154 1.461296 1.0 2.00 3.0 4.00 5.0
26 26.0 3.269231 1.250846 1.0 2.00 3.0 4.00 5.0
27 26.0 3.923077 0.934797 2.0 3.00 4.0 5.00 5.0
28 26.0 3.230769 1.242826 1.0 2.25 3.0 4.00 5.0
29 26.0 3.346154 1.294366 1.0 2.25 4.0 4.00 5.0
30 27.0 4.074074 0.916764 2.0 4.00 4.0 5.00 5.0

<!-- Page 29 -->

Table11:Estimatedcoefficients(𝛽ˆ)ofthefixedeffectsofthe Table16:Variationofinterceptsbytrustscalesofthemixedmixed-effectsmodelpredictingexplanationratings. effectsmodelpredictingtrustratings.

### Estimate Std.Error tvalue (Intercept)

(Intercept) 3.31082 0.07517 44.044 (Intercept)
HighlightAVFALSE -0.22321 0.08054 -2.771 Question1 1.3028370

### TypeHuman -0.15920 0.08038 -1.981 Question2 1.8321074

AVExperienceTRUE 0.09922 0.05926 1.674 Question3 0.9450894
HighlightAVFALSE 0.17437 0.11367 1.534 Question4 1.1313141
:TypeHuman Question5 1.9791269

### Question6 2.4642915

Table12:Variationofinterceptsbyscenarioofthemixed- Question7 1.8762132
effectsmodelpredictingexplanationratings. Question8 1.0921089
Question9 1.1362148
(Intercept)

### Table17:Estimatedvariationoftherandomeffects,inthis

Scenario1 3.376390 casejustthetrustscales,ofthemixed-effectsmodelpredict-
Scenario2 3.259917 ingtrustratings.
Scenario3 3.279770

### Scenario4 3.327218

Groups Name Variance Std.Dev.
Table13:Estimatedvariationoftherandomeffects,inthis TrustQuestion (Intercept) 0.2787 0.5279
casejusttheScenario,ofthemixed-effectsmodelpredicting Residual 1.1299 1.0630
explanationratings.

### Table18:AnalysisofDevianceTable(TypeIIWaldchi-square

tests)withresponsevariableoftrustratings.Significance
Groups Name Variance Std.Dev.
codes:0‘***’0.001‘**’0.01‘*’0.05‘.’0.1‘’1
Scenario (Intercept) 0.004611 0.0679
Residual 0.646100 0.8038

### Chisq Df Pr(>Chisq)

Table14:AnalysisofDevianceTable(TypeIIWaldchi-square MeanCEMARank 21.8790 1 ***2.904e-06
tests)withresponsevariableofexplanationratings.Signifi- MeanHumanRank 0.0379 1 0.84563
cancecodes:0‘***’0.001‘**’0.01‘*’0.05‘.’0.1‘’1 PreExplanation 4.5852 1 *0.03225

### HighlightAV 0.1970 1 0.65719

Chisq Df Pr(>Chisq) AVExperience 39.9520 1 ***2.603e-10

### MeanCEMARank 0.8202 1 0.36511

HighlightAV 5.6826 1 *0.01713 :MeanHumanRank

### Type 1.6055 1 0.20513


### AVExperience 2.8032 1 .0.09408


### HighlightAV:Type 2.3529 1 0.12505

Table15:Estimatedcoefficients(𝛽ˆ)ofthefixedeffectsofthe
mixed-effectsmodelpredictingtrustratings.

### Estimate Std.Error tvalue

(Intercept) 1.52881 0.50029 3.056

### MeanCEMARank 0.35401 0.15279 2.317


### MeanHumanRank 0.11929 0.15360 0.777

PreExplanationFALSE 0.11044 0.05158 2.141
HighlightAVFALSE 0.02302 0.05186 0.444
AVExperienceTRUE 0.33170 0.05248 6.321
MeanCEMARank -0.04054 0.04477 -0.906
:MeanHumanRank

<!-- Page 30 -->

D.3.2 ResultsofStatisticalAnalysis. Wepresentintheprevious (1) Overtaking:Thebluevehiclemayhavewantedtoovertake
page the full results of our statistical analysis using the mixed- anotherslower-movingvehicleinfrontofit,andchanging
effectsmodelforboththeexplanationratings-relatedandtrust lanestotheleftprovidedaclearpathtodoso.
ratings-relatedexperimentsInTables11and15,wereporttheesti- (2) Obstruction:Theremayhavebeenanobstructioninthe
matedmeansandstandarderrorsofthefixedeffects.InTables12 rightlanethatthebluevehiclewantedtoavoid,suchas
and16,wereportthechangestotheestimatedmeanoftheinter- debris,apothole,oraparkedvehicle.
ceptsduetothegroupingbytherandomeffectsvariablesinthe (3) Turningleft:Thebluevehiclemayhavebeenplanningto
model.InTables13and17,wereportthevariationintherandom turnleftattheT-junction,andchanginglanestotheleft
effectsvariables.Finally,inTables14and18,wereportthesignifi- putitinthecorrectpositionfortheturn.
canceofeachfixedeffectsvariableonthepredictedvalueofthe (4) Personalpreference:Thedriverofthebluevehiclemay
outcomevariable. havesimplypreferreddrivingintheleftlaneforpersonal
reasons,suchasfeelingmorecomfortableorhavingbetter
D.4 ChatGPTPromptsandReplies visibility.
Onepossibleadditionalbaselinethathasrecentlyemergedisthe However,withoutmorecontextaboutthespecificsituation,
familyoflargelanguagemodelsandtheirpublic-facingdemonstra- it’simpossibletoknowforsurewhythebluevehiclechanged
tionssuchasChatGPT[31].Whileitisstronglydebatedwhether lanestotheleft.[ThislastsentenceisalsobyChatGPT]
thesesystemshaveagrasponcausality,nonetheless,theirimpres-
D.4.2 Scenario2. ChatGPTcannotidentifythecorrectcausesbesivefluencyandapparentreasoningabilitiesshouldnotbeignored.
hindthebluevehicle’sactions(ego)evenwhenwegivealarge

### Therefore,wehavealsoexploredthekindofexplanationsthat

numberofcontextualclues.Itgivescompletelyincorrectguesses

### ChatGPTcangivebydescribingeachscenarioandthenprompting

aboutwhythebluevehiclemightnotgivewaytotheorangevehicle
itforanexplanation.Forallscenarios,tediousprompteditingand
(non-ego).
re-promptingwererequiredtoproduceusefulresponses.Wefound
thatChatGPTcouldidentifycausescorrectlybehindS1andS4,and Prompt:Abluevehicleisapproachingajunctionwithout
failedtoexplainS2andS3.However,itisimpossibletodetermine trafficlightsfromthesouthonasecondaryroad.Thereis
howandwhyspecificcausesareselectedbyChatGPT.Itisaclosed anorangevehiclecomingfromtheleftandagreenvehicle
systemwhichchangesfrequentlyanditsresponsesvaryforthe comingfromtherightonamainroad.Thegreenvehicleis
samepromptsmakingitdifficulttouseasabaseline. maintainingahighspeedandisheadingstraightthrough
Wegivethepromptsandtheobtainedresponsesfromourexplo- thejunction,andtheorangevehicleisslowingdowntoa
rationofChatGPT’sabilitytoexplainbehaviourinourscenarios. stoplikelytoturnleftandwaitingforthegreenvehicleto
WeusedGPT-3.5fortheseexplanations. pass.Inresponse,thebluevehicleturnsrightontothemain
roadwithoutgivingwaytotheorangevehicle.Whydidthe
D.4.1 Scenario1. ChatGPTidentifiesasafetyriskintheorange
bluevehiclenotgiveway?
vehicle(non-ego)cuttinginfrontofthebluevehicle(ego).After

### Response:Basedonthescenarioyoudescribed,theblue

additionalprompting,itgivesfurthercorrectandplausiblereasons
vehicleshouldhavegivenwaytotheorangevehiclebefore
towhytheegowouldchangelanesleftinthisscenario.
turning right onto the main road. Failing to give way to

### Prompt:Thereisabluevehicleandanorangevehicleon

theorangevehiclewouldbeaviolationoftrafficlawsin
atwo-lanedroad.Theorangevehicleisintheleftlane20
mostjurisdictions,andcouldresultinacollisionorother
metersaheadofthebluevehiclewhichisintherightlane.
dangeroussituation.

### TheroadisapproachingaT-junctionwithanexitonthe


### Withoutfurtherinformationaboutthespecificcircumstances

right. The orange vehicle changes lanes to the right and
andtheactionsofthedriversinvolved,it’sdifficulttodeterbeginstoslowdown.Inresponse,thebluevehiclechanges
minewhythebluevehicledidnotgiveway.However,some
lanestotheleft.Whydidthebluevehiclechangelanesto
possiblereasonscouldincludethedrivernotbeingaware
theleft?
oftheorangevehicle’spresenceorintentiontoturnleft,or

### Response:Thebluevehiclemostlikelychangedlanesto

misjudgingthedistanceandspeedoftheorangevehicle.It’s
thelefttoavoidapotentialcollisionwiththeorangevehicle,
importantfordriverstoalwaysbeawareoftheirsurroundwhichwasslowingdownandchanginglanestotheright.
ingsandgivewaytoothervehicleswhenrequiredbytraffic
Changinglanestotheleftwouldgivethebluevehiclemore
lawsandcommonsense.
spaceanddistancefromtheorangevehicle,reducingthe
riskofacollisionastheroadapproachestheT-junctionwith Atthispoint,furtherprompting(e.g.,tellingChatGPTexplicitly
anexitontheright.It’sadefensivedrivingtechniqueto thatitissafenottogiveway)doesnotchangetheresponsesof
maintainasafedistancefromothervehiclesandanticipate ChatGPTsignificantly.
anypotentialhazardsorobstaclesontheroad.
Prompt:Besidesavoidingacollision,whatelsecouldhave D.4.3 Scenario3. ChatGPTcannotidentifythecorrectcausesbepromptedthebluevehicletochangelanesleft? hindthebluevehicle’sactions(ego)evenwhenwegivealarge
Response:Therecouldbeseveralotherreasonswhythe numberofcontextualclues.Furtherprompting(e.g.,tellingChatblue vehicle changed lanes to the left besides avoiding a GPTexplicitlythatitissafenottogiveway)doesnotchangethe
collisionwiththeorangevehicle.Herearesomepossibilities: responsesofChatGPTsignificantly.

<!-- Page 31 -->

Prompt:Thereisabluevehicleandanorangevehicle.The Thismayhavepromptedthebluevehicleonthesecondary
orangevehicleisinatwo-lanedroundaboutandithasjust roadtotakeadvantageoftheopportunitytoturnleftonto
changedlanesfromtheinnerlanetotheouterlane.Theblue themainroadandjointhewaitinglineofcars,ratherthan
vehicleisonaroadthatenterstheroundaboutandithas waitingforthetrafficlighttoturngreen.
togivewaytotheorangevehicle.Onobservingtheorange Alternatively,itispossiblethatthebluevehiclewasalready
vehiclechangelanes,thebluevehicledecidestoenterthe intendingtoturnleftontothemainroad,andthestopping
roundaboutwithoutgivingwaytotheorangevehicle.Why oftheorangevehiclesimplyprovidedaclearopeningfor
wasitsafetoentertheroundabout? thebluevehicletomaketheturnsafely.Withoutfurther
Response:AsanAIlanguagemodel,Idonothaveaccess information,itisdifficulttodeterminetheexactreasonwhy
toreal-timeinformationaboutthetrafficconditionsinyour thebluevehicleturnedleftontothemainroad.
specificlocation.However,basedonthescenarioyouhave Prompt:Therearenoobstaclesontheroadsotheorange
described, it is not safe for the blue vehicle to enter the vehiclecouldhavejustjoinedthelineofwaitingcars,thus
roundaboutwithoutgivingwaytotheorangevehicle,even blockingthewayofthebluevehicle.Yetitdidnot.Inlight
iftheorangevehiclehadjustchangedlanes. ofthis,whycouldthebluevehicleturnleft?
Failingtogivewaytoavehiclethathasalreadyentereda Respose:Iftherewerenoobstaclesontheroadandthe
roundaboutcancauseacollision,particularlyiftheother orangevehiclecouldhavejoinedthelineofwaitingcars,but
vehicleisalreadyinthedriver’sblindspot.Itisimportantto didnot,itispossiblethattheorangevehicledriverintenrememberthatalldriversontheroadhavearesponsibility tionallystoppedbeforetheT-junctiontoletthebluevehicle
todrivesafelyandfollowtrafficlawstopreventaccidents. turnleftontothemainroad.Thiscouldhavebeenacourtesy
Therefore,itisrecommendedthatthebluevehiclewaituntil gestureonthepartoftheorangevehicledriver,particularly
theorangevehiclehaspassed ifthebluevehiclehadbeenwaitingforawhileorifthe
Prompt:However,theorangevehicleisalsoslowingdown orangevehicledrivernoticedthatthebluevehiclewasina
which indicates that it will exit the roundabout without hurry.
crossingthepathofthebluevehicle.Whywasitsafeto Alternatively,itispossiblethatthebluevehiclehadtheright
entertheroundaboutforthebluevehiclenow? ofwaytoturnleftontothemainroadandtheorangevehicle
Response: If the orange vehicle is slowing down and is driverrecognizedthis,andthereforestoppedtoallowthe
abouttoexittheroundaboutwithoutcrossingthepathof bluevehicletoturnsafely.
thebluevehicle,thenitmaybesafeforthebluevehicleto Withoutfurtherinformation,itisdifficulttodeterminethe
entertheroundabout. exactreasonwhythebluevehicleturnedleftontothemain
However,itisimportanttonotethatthebluevehicleshould road.However,itispossiblethattheactionsoftheorange
onlyentertheroundaboutifitissafetodoso,andafter vehicledriverplayedaroleinallowingthebluevehicleto
ensuringthattherearenoothervehiclesenteringorexiting maketheturn.
theroundaboutthatcouldpotentiallycrossitspath.
Additionally,thebluevehicleshouldalwaysfollowtraffic
lawsandsignals,andshouldbepreparedtostoporyieldto
othervehiclesifnecessary.
Therefore,ifthebluevehicledeterminesthatitissafeto
entertheroundaboutandthatitwillnotimpedetheflowof
trafficorcauseapotentialcollision,thenitmayproceedto
entertheroundabout.

### D.4.4 Scenario4. Initially,ChatGPTassumescertainfactsabout

theenvironmentwhicharenottrue,butonsomefurtherclarifications,itcanidentifythecorrectcausesbehindtheorangevehicle
stoppingatthejunction.

### Prompt:Thereisawaitinglineofcarsbehindaredtraffic

light.Justbehindthislineofcarsisasecondaryroadthat
entersthemainroadinaT-junction.Thereisabluevehicle
onthesecondaryroadwaitingtoturnleftontothemain
road.Anorangevehicleonthemainroadstopsbeforethe
T-junction.Inreaction,thebluevehicleturnsleftontothe
mainroadandjoinsthewaitinglineofcars.Whydidthe
bluevehicleturnleft?
Response:Basedontheinformationprovided,itseemsthat
theorangevehicleonthemainroadhasstoppedbeforethe
T-junction,potentiallyindicatingthatthereisanobstruction
orsomeotherreasonpreventingitfromcontinuingforward.

## Tables

**Table (Page 1):**

|  |  |
|---|---|
|  |  |


**Table (Page 3):**

| Human-Agent Interface | Environment |
|---|---|
| Counterfactual Causal Selection Query Filter Observations Rollback Probabilistic Model Simulate Cnt.factual Worlds Calculate Cnt.factual Causal Rank Features Effect Size |  |


**Table (Page 7):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 8):**

| 1.0 Slower thgiew Decelerate Exit right 0.5 Exit straight Faster erutaeF Accelerate 0.0 Same vel. −0.5 20 40 60 80 100 Number of samples (K) |
|---|
|  |
| 1.0 thgiew 0.5 erutaeF 0.0 −0.5 0 100 101 Smoothing weight (α) |


**Table (Page 8):**

|  |  |  |  |  | Slower |
|---|---|---|---|---|---|
|  |  |  |  |  | Decelerate Exit right Exit straight |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  | Faster Accelerate Same vel. |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 8):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 11):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 1 | 7 |  |  |  |  | 1 | 8 | 7 |  |  |  |  | 15 |  | 6 |  |  |  |
|  |  |  |  |  | 9 |  | 1 | 6 |  |  |  |  | 1 | 2 |  |  |  |  | 5 |  |
|  |  |  |  | 1 | 0 |  |  |  |  |  |  | 1 |  |  |  | 19 | 14 |  |  |  |
|  | 1 | 3 |  |  |  | 4 |  |  |  | 0 3 |  |  |  |  |  |  | 20 |  |  |  |
| 11 2 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 11):**

|  |  |  |  | 4 3 |  |  |
|---|---|---|---|---|---|---|
|  |  | 9 |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  | 1 |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  | 1 |  |  |  |
|  |  |  |  |  |  |  |
| 12 8 |  |  |  |  |  | 5 4 2 |
| 1 |  |  |  |  |  | 7 3 6 10 |
|  |  | 1 | 5 |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  | 60 |  |  |  |
|  |  | 1 |  |  |  |  |
|  |  | 1 |  |  |  |  |
|  |  |  | 1 |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 12):**

|  | 3 |
|---|---|
|  |  |


**Table (Page 12):**

|  | 2 |  |
|---|---|---|
|  |  |  |


**Table (Page 12):**

|  |  |  |  |
|---|---|---|---|
| 7 |  |  | 145 6 |
| 12 11 10 | 4 |  | 8 |
|  |  | 1 2 |  |
| 9 |  |  |  |
| 0 |  |  |  |
|  | 1 | 3 3 |  |


**Table (Page 14):**

|  |  |
|---|---|
|  |  |


**Table (Page 20):**

|  |
|---|
|  |


**Table (Page 21):**

|  |
|---|
|  |
|  |


**Table (Page 21):**

|  |
|---|
|  |
|  |


**Table (Page 21):**

|  |
|---|
|  |
|  |


**Table (Page 24):**

|  | Confidence in AVs |  |  |  |  |  |  |  | AV decisions are predictable |  |  |  |  | AVs are reliable |  |  |  |  | AVs are always correct |  |  |  |  |  |  | AVs are efficient |  |  |  |  |  | Wary of AVs (lower better) |  |  |  |  |  | AVs better than novice |  |  |  |  |  |  |  |  |  |  |  |  |  | Willing to use AVs |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Before |  |  |  | After |  |  | Before |  | After |  |  | Before |  | After |  |  |  | Before |  |  | After |  |  |  | Before |  | After |  |  | Before |  |  | After |  |  |  | Before |  |  | After |  |  |  | Before |  | After |  |  |  | Before |  |  | After |  |  |
|  |  | e24: |  |  |  | Mean |  | ra | tings |  | ofpa |  | rti | cipan |  | tson |  | th |  | e9tru |  |  | stsca |  | le |  | sbefo |  | rean |  | d | afterh |  |  | aving |  | s |  | eenex |  |  | plan |  | ati |  | onsw |  | ithst |  |  | a | ndard |  |  | error. |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | S |  |  |  | cenar |  | io | 1 |  |  |  |  |  |  | Scena |  | rio |  | 2 |  |  |  |  |  |  |  |  | Scen |  | ar | io 3 |  |  |  |  |  |  |  |  |  | Sce |  | nar |  | io 4 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | pe |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
