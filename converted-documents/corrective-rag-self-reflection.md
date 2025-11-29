---
title: "Corrective RAG Self Reflection"
original_file: "./Corrective_RAG_Self_Reflection.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "chain-of-thought", "react", "agents"]
keywords: ["jump", "time", "switch", "gillespie", "flow", "method", "jsf", "page", "model", "doob"]
summary: "<!-- Page 1 -->

A hybrid framework for compartmental models enabling
simulation-based inference
Domenic P.J. Zarebski a,c,*, Sophie Hautphenne a, Robert

### Moss d, Jennifer A. Flegg e

aThe School of Mathematics and Statistics, The University of Melbourne, Parkville, VIC, Australia
bThe School of Mathematics and Statistics, The University of Sydney, Camperdown, NSW, Australia
cPandemic Sciences Institute, University of Oxford, Oxford, United Kingdom
dMelbourne School of Population and Global "
related_documents: []
---

# Corrective RAG Self Reflection

<!-- Page 1 -->

A hybrid framework for compartmental models enabling
simulation-based inference
Domenic P.J. Germano a,b,*, Alexander E. Zarebski a,c,*, Sophie Hautphenne a, Robert

### Moss d, Jennifer A. Flegg a, and Mark B. Flegg e

aThe School of Mathematics and Statistics, The University of Melbourne, Parkville, VIC, Australia
bThe School of Mathematics and Statistics, The University of Sydney, Camperdown, NSW, Australia
cPandemic Sciences Institute, University of Oxford, Oxford, United Kingdom
dMelbourne School of Population and Global Health, The University of Melbourne, Parkville, Vic, Australia
eSchool of Mathematics, Monash University, Clayton, VIC, Australia
Keywords—Hybridsimulation—stochasticmodelling—viralclearance—extinction—compartmentalmodelling

### Abstract

Multi-scalesystemsoftenexhibitacombinationofstochasticanddeterministicdynamics. Incompartmental
models,lowoccupancycompartmentstendtoexhibitstochasticdynamicswhilehighoccupancycompartments
tend to follow deterministic dynamics. Representing both dynamics with existing methods is challenging.
Failing to account for stochasticity in small populations can produce “atto-foxes”, for example in the Lotka-
Volterraordinarydifferentialequation(ODE)model. Thislimitationbecomesproblematicwhenstudyingthe
extinctionofspeciesortheclearanceofinfection,butitcanbeovercomebyusingdiscretestochasticmodels,
suchascontinuoustimeMarkovchains(CTMCs). Unfortunately,simulatingCTMCsisimpracticalformany
realisticmodels,wherediscreteeventshaveveryhighfrequencies.
Inthiswork,wedevelopanovelmathematicalframeworktocouplecontinuousODEsanddiscreteCTMCs:
“Jump-Switch-Flow” (JSF). In this framework, compartments can reach extinct states (“absorbing states”),
thereby resolving atto-fox-type problems. JSF has the desired behaviours of exact CTMC simulation, but is
substantially computationally faster than existing alternatives, by at least one order of magnitude, and can
evenobtainconstantscaling,irrespectiveofcompartmentoccupancy.
WedemonstrateJSF’sutilityforsimulation-basedinference,particularlymulti-scaleproblems,withseveral
case-studies. In a simulation study, we demonstrate how JSF can enable a more nuanced analysis of the
efficacyofpublichealthinterventions. Wealsocarryoutanovelanalysisoflongitudinalwithin-hostdatafrom
SARS-CoV-2infectionstoquantifythetimingofviralclearance. Inthiswork,weshowhowJSFoffersanovel
approachtocompartmentalmodelsimulation.

### Introduction

Dynamical systems are a powerful method for describing the world, and have successfully been applied in many fields.
However, modelling populations which change in size across multiple scales remains a challenge Fowler, 2021. Population
sizes in biological processes often change over orders of magnitude, e.g. the spread of infectious disease (Anderson et al.,
1991);theboom-and-bustofinsectpopulations(Ludwigetal.,1978);andtheimmuneresponsetoinfections,suchasHIV
(Perelson,2002),andinfluenzavirus(Baccametal.,2006).
The dynamics of small populations can be heavily influenced by stochastic effects, while for larger populations these
fluctuationsoftenaverageout,justifyingtheuseofcontinuummodels. Whenthepopulationunderconsiderationdoesnot
changeinsizeoverordersofmagnitude,thereisusuallyanatural(andobvious)choicebetweenastochasticordeterministic
model. However,formulti-scalemodels,thisdecisionremainsachallenge,anddevelopingmodellingmethodsthatcanbridge
thesescaleshasbeenalong-standinggoalofappliedmathematics(Cotteretal.,2016;Fleggetal.,2014;Isaacson,2013).
Compartmental models describe how quantities (e.g. the number of molecule, cells, or people) change in a dynamical
system. Twopopularwaystorepresentcompartmentalmodelsareordinarydifferentialequations(ODEs)andcontinuous
time Markov chains (CTMCs). Many ODEs one encounters are actually ensemble averages of CTMCs, although the
mathematicaljustificationofthisisnotalwaysstraightforward(Kurtz,1970;Kurtz,1971;Kurtz,1972).
In ODEs, the state of the system changes continuously, which can lead to “atto-fox problems” where populations shrink
to infeasibly small sizes, i.e. where a real population would likely have gone extinct (Fowler, 2021; Mollison, 1991; Lobry
et al., 2015). In CTMCs, the discrete state changes stochastically and there may be absorbing states e.g. extinction of
a population. As a result, CTMCs offer a more natural description of small populations sizes, however applying them to
largepopulationscanbecomputationallychallenging. Moreover,arangeofpowerfultechniquescanbebroughttobearon
*Theseauthorscontributedequallytothiswork
1
5202
luJ
03
]EP.oib-q[
3v93231.5042:viXra

<!-- Page 2 -->

ODEs, enabling more thorough analysis. This raises a natural question about what to do when compartment occupancy
changesacrossordersofmagnitude.
ExactandapproximatealgorithmstosimulateCTMCsexistGillespie,1976;Simonietal.,2019. Exactmethods(e.g.Doob-
Gillespie,first/nextreaction,andrejectionbasedmethods)arecomputationallyexpensivewhenstatetransitionsoccurat
a high rate (Sanft et al., 2015). Approximate methods (e.g. Tau-leaping (Gillespie, 2001; Cao et al., 2006) and the use
of chemical Langevin equations (Rao et al., 2003; Gillespie, 2000; Gibson et al., 2000)) scale to high transition rates but
can have unacceptable approximation error. To overcome the limitations of classical approximate methods, over the past
two decades, there has been a concerted effort to develop hybrid stochastic-deterministic approaches (Simoni et al., 2019;
Kregeretal.,2021;Bressloffetal.,2014;Rebulietal.,2017).
SomehybridmodellingapproachesinvolvepartitioningthetransitionsinaCTMCintofastandslowtransitions. Despite
having significant implementation bookkeeping and overheads, these approaches can be sampled individually and subsequently synchronised in an efficient manner Simoni et al., 2019. Jump-diffusion differential equations partition the model
compartmentsintofluid anddiscretecompartments,toconstructhybridswitchingjumpdiffusion processesBuckwaretal.,
2011; Angius et al., 2015. Other hybrid simulation techniques have been developed in the context of within-host viral
infection Kreger et al., 2021. However, this implementation is not generalised, but tailored to a single system, and does
notallowswitchingbetweenstochasticanddeterministicregimes. Inthecontextofdeterminingthehybridisationbetween
stochastic and deterministic couplings, path-integrals have been utilised, Bressloff et al., 2014, which permit analysis of
hybrid processes. Recently, Kynaston et al. considered extended systems that represent each compartment with both a
continuousandadiscreteversionandallowtheforconversionbetweenthemKynastonetal.,2023.
Essentialforthereal-worldutilityofmanymathematicalmodelsistheirabilitytobecalibratedtodata. Fordeterministic
compartment models, standard parameter inference methods, such as maximum likelihood and posterior sampling via
Markov chain Monte Carlo (MCMC), can readily be applied (Ionides et al., 2006). For stochastic models these inference
problems are usually much harder. Simulation-based inference has emerged as a way to handle these problems, e.g. the
particlefilter(Arulampalametal.,2002;Kitagawa,1996)andapproximateBayesiancomputation(Alahmadietal.,2020).
Calibrated multi-scale simulations of ODE (compartment) models is an important milestone towards accurate predictive
modelsthataddressstochasticbehaviour. Inarecentpaper,TrindadeandZygalakisdevelopahybridschemeforchemical
kinetics over different scales with the goal of demonstrating the utility for parameter estimation (Trindade et al., 2024).
In this paper, a CTMC is used to model reaction events on small populations (below a threshold I1 > 0) and for better
efficiencyTau-leapingisusedforreactionsthatonlyimpactlargepopulations(aboveathresholdI2>I1). Betweenthese
two thresholds, a “blending function” is used to create a linear transition between an accurate CTMC and efficient Tauleapingtreatmentofthereactions. ThehybridadoptionofCTMCandTau-leapingregimeshasthepropertyofmaintaining
appropriatelevelsofnoiseatlargepopulationsbutstrugglesaspopulationsgrowmuchlargerwhereaChemicalLangevin
ordeterministicODEdescriptionmaybemorecomputationallyappropriate.
In this paper, we present a simple and efficient hybrid simulation method which we call Jump-Switch-Flow (JSF). This
method enables adaptive transitions between stochastic and deterministic regimes across compartments, while ensuring
conservation principles are maintained. In this approach, compartments can individually switch regimes, allowing for
the compartments to be split into stochastic and deterministic subsets, while remaining coupled. This regime switching
presentsuniquechallengesinmatchingatinterfaces: ensuringthatthedeterministicregimerepresentstheexpectedstate
under transition between regimes and that mass is conserved. Conservation is not always essential when it pertains to
smallpopulationsizes,howeverinmanycasessustainedsmallpopulationshaveasignificantimpactonlargerpopulations
(e.g.enzymesinchemicalprocessesandviruseswithinhosts.) WedemonstratetheutilityandpropertiesoftheJSFmethod
throughsimulationstudies,andacasestudyinwhichwereanalyseexistinglongitudinalSARS-CoV-2viralloaddatasets.
Two simulation studies are presented to explore the properties of JSF and demonstrate its use in an inference setting. In
the first simulation study, we compare the computational efficiency and accuracy of JSF with the exact Doob-Gillespie
methodandtheTau-leapingmethod. Inthesecondsimulationstudy, wedemonstratethetypesofinsightavailablewhen
usinganapproachthatsupportsabsorbing(extinction)states.
In the case study, we demonstrate The significance of being able to perform inference with models with absorbing states
(i.e. models in which one of the compartments can go extinct.) In the case study we reanalyse longitudinal SARS-CoV-2
viralloaddata(Keetal.,2022)usingJSFtosimulateaTEIRV(Targetcells–Eclipsedcell–Infectiouscells–Refractory
cell–Virions)modelandinferthestateofhostandvirusacrosstheinfection. Understandinghowaviralinfectioniscleared
has important ramifications for both treatment and prevention. For example, the initial exposure may fail to initiate a
systematic infection, and understanding the conditions under which this happens is important for infection prevention
Pearson et al., 2011. Moreover, the infection may reach low levels, potentially escaping detection, but the virus may
reboundandcausedisease. Understandingwhenthevirushasbeenclearedisimportantforoptimisingtreatmentduration.
Inferringviralclearancecanbecomputationallychallenging(Yanetal.,2016),andthiscasestudydemonstrateshowJSF
enablesthetractableestimationofviralclearance.

### Methods


### Jump-Switch-Flow mathematical framework

Consider a compartmental model with n compartments, V⃗ =(v1,...,vn), where the state variable, vi :=vi(t), represents
the value of the ith compartment at time t. For example, vi could be the number of people infected with a pathogen, or
the copy number of a molecule in a cell. The state variables vi may take values from different domains, depending upon
theresolutionneeded,forexampleinanODE, vi willhaverealvaluesandinaCTMC vi mighthaveintegervalues.
2

<!-- Page 3 -->

When the variables represent quantities, typically, discrete values are used to represent small populations, while larger
populationsarerepresentedwithacontinuum. Toaccommodatebothscales,letthedomainofvibetheset{0,1,...,Ωi}∪
(Ωi,∞). The switching threshold parameter, Ωi ∈ Z
≥0
, is where the ith compartment transitions between discrete and
continuous dynamics. If a compartment vi ∈{0,1,...,Ωi}, we call it discrete (or jumping), and if vi ∈(Ωi,∞), we call
itcontinuous (orflowing). Whiletheswitchingthresholdcanbecompartmentspecific,foreaseofexposition,wewillonly
considerasinglethresholdsharedbetweenallcompartments,i.e.Ωi=Ω.
Ateachtimet,thecomponentsofV⃗ canbepartitionedintoV⃗ F andV⃗ J,whereV⃗ F containstheflowingvariablesvi >Ω,
and V⃗ J contains the jumping variables vi ≤ Ω. Therefore, at any moment in time dim(V⃗ F) of the n compartments are
flowing,anddim(V⃗ J)ofthencompartmentsarejumping,withdim(V⃗ F)+dim(V⃗ J)=n.
The dynamics of each compartment vi are described by a set of m reactions R = {r
k
}m
k=1
. Each reaction r
k
is defined
by two properties: the rate (per unit time) at which it occurs, λ , which (usually) is a function of the state V⃗; and the
k
reaction’seffectonthestate,i.e.thechangeη
ik
tothesizeofcompartmentviwhenreactionr
k
occurs. Asavector,⃗λ∈Rm
isreferredtoasthepropensity vector. Asamatrix,η∈Zn,m isreferredtoasthestoichiometric matrix. ForODEmodels
thatonlycontainflowingvariables,thesereactionsoccurcontinuouslyandarewrittenintheform:
dV⃗
=η⃗λ(t,V⃗). (1)
dt
ForCTMCmodels,reactionsinthesystemRoccurasdiscreteevents. Inthelattercase,eachreactionr hasaseparate
k
propensitydescribedbyλ (t,V⃗). Thispropensityremainsconstantbetweenreactions,butwhenareactionr occurs,there
k k
isachangeinV⃗ (asspecifiedbytheelementsofη ),andthereforein⃗λ(t,V⃗).
·k
Asanexample,considertheSIRmodelofepidemics,which,inordinarydifferentialequations,hastheform dS =− βSI ,
dt S+I+R
d
d

## I

t
=

## S+

β

## I


## S

+

## I


## R

−γI,and d
d

## R

t
=γI. ThestateofthismodelisV⃗ =(S,I,R)⊺,andtherearetwo“reactions”: infections(r1)
andrecoveries(r2). Forinfections,therateofreactionmaybemodelledbyλ1 =βSI/(S+I+R),andtheentriesofthe
associated column of the stoichiometric matrix are η1,1 =−1, η2,1 =1 and η3,1 =0. For recoveries, the rate of reaction
maybemodelledbyλ2=γI,andtheentriesoftheassociatedcolumnofthestoichiometricmatrixare,η1,2=0,η2,2=−1,
andη3,2=1.
WedefineRJ ⊆Rasthesubsetofreactionstreatedasstochasticjumpevents. ThesetRJ canbedefinedmorepreciselyin
twoways. Whileweuseonlythesecondinthismanuscript,botharedescribedforclarity. ThefirstwaytodefineRJ isas:
(cid:110) (cid:111)
RJ = r k :∃is.t. vi∈V⃗ J andη ik ̸=0 . Inthisdefinition,areactionr k isincludedinRJ ifandonlyifthereactionhas
somematerialeffectonajumping(discrete)compartmentvi∈V⃗ J. Thisisaminimumrequirement;areactionshouldnot
bepermittedtoevokeacontinuouschangeinadiscretecompartment. However,whereitmakessensetodoso,itispossible
toallowreactionstomakediscretechangestoflowing(continuous)compartments. ThesecondwaytodefineRJ,whichwe
(cid:110) (cid:111)
usethroughoutthismanuscript,capturesalargersetofreactions: RJ = r k :∃is.t. vi∈V⃗ J and (η ik ̸=0or∂vi λ k ̸=0) .
Inthisdefinition,areactionisincludedinRJ ifeither(1)itcausesamaterialchangeinjumping(discrete)compartments
or (2)itisinfluenced/causedbyadiscretecompartment(e.g.ascatalystofsomereaction.)
Reactions in RJ are simulated using stochastically sampled times, similar to CTMC models (and described below in the
section on ‘Jump events’). It is important to note that unlike time homogeneous CTMC models, the propensities are not
constant because the state V⃗ (and therefore⃗λ) are continuously varying. When any reaction r
k
∈RJ occurs, we say the
systemhasjumped andaninstantaneouschangeofη ik foreachcompartmentvi occurs(irrespectiveofwhethervi∈V⃗ J or
vi∈V⃗ F,toensuretheconservationofmass). WethereforerefertoreactionsinRJ asjumps. ThereactionsinRF =R\RJ
representthecontinuouschangeofvalueoftherelevantcompartments,allofwhicharedeterministic(seesectionon‘Flow
events’ above.) We therefore refer to reactions in RF as flows. At any moment in time |RF| is the number of reactions
whichareflowing,and|RJ|isthenumberofreactionswhicharejumping,suchthat|RF|+|RJ|=m.
Finally,thehybridmodelthatweproposeiscapableofswitching. Switchingeventsoccurwhenthesizeofacompartment
vi crossesthethresholdΩandthereforechangesmembershipbetweentheflowingV⃗ F andjumpingV⃗ J sets(seesectionson
‘Jump clock updates’ and ‘Switching events’). Importantly, switching events may also impact which reactions are jumps,
RJ. Assuch,switchesareparadigm-definingeventswhichoughttooccurinfrequentlyincomparisontojumps(whichmay
occurfrequently)andflows(whichoccurcontinuously).
Due to the way that R is partitioned, it is possible to order the rows and columns of η into the upper-triangular block
form:
(cid:18) (cid:19)
η=
ηFF ηFJ
, (2)
0 ηJJ
whereηFF ∈Zdim(V⃗ F),|RF|,ηJJ ∈Zdim(V⃗ J),|RJ| andηFJ ∈Zdim(V⃗ F),|RJ| refertostoichiometriccoefficientsforchanges
in flowing compartments under flows, jumping compartments under jumps, and flowing compartments under jumps, respectively. Note that, the lower left corner is zeros because, by definition, flowing reactions cannot influence the state of
jumpingvariables. Writtenasasystemofequationsanalogousto(1),thehybridJSFframeworkweproposeformallytakes
thefollowingform. Foranytimeintervalti<t<ti+1 betweenswitchingeventsiandi+1:
dV⃗
F =ηFF ⃗λF(t,V⃗)+ηFJΛ⃗ J(t,V⃗), (3)
dt
(cid:90) t
V⃗ J(t)=V⃗ J(ti)+ηJJ Λ⃗ J(s,V⃗)ds, (4)
ti
3

<!-- Page 4 -->

where⃗λF ∈R|RF| arethereactionratesofflowsandΛ⃗ J isastochasticvectorof|RJ|delta-functionspiketrainsthatare
derivedfromtherealisationsof|RJ|differentjumpssampledatrateswhicharedependentonthedynamicchangesinthe
propensities⃗λJ ∈R|RJ| forthesejumps(see‘Jumpevents’).
Figure 1: JSF provides a way to capture both the continuous deterministic dynamics of large populations and the
discrete stochastic dynamics of small populations. A A compartmental model representation of the Lotka-Volterra
system (5): prey (v , depicted as red rabbits which, in reaction r , reproduce at rate α), predators (v , depicted as
1 1 2
purplefoxeswhich,inreactionr ,dieatrateγ),andtheirinteraction(predationofrabbitsbutfoxes,inreactionr ,ata
2 3
rateproportionaltoβ). BThecompartmentalmodelcanbeformalisedasareactionnetworkviaastoichiometrymatrix
η which details each species role in the reactions. The reactants consumed η− and the products produced η+ can be
writtenexplicitlywithη=η+−η−. CAhypotheticalJSFtrajectorydemonstratinghowtherepresentationcapturesthe
continuousvariationofsomecompartment-reactionpairs(flow)andthediscretestochasticchanges(jumps)inothers.
Transitioning (switching) between a continuous and discrete state occurs at a threshold Ω which is indicated with a
horizontal dashed line. D An example trajectory from the Lotka-Volterra model exhibiting the characteristic cyclical
behaviour with additional stochasticity influencing the dynamics at low population sizes. E An example trajectory
showing the possibility for the predator species to go extinct and the subsequent growth of the prey species.

### Example: Lotka-Volterra model

TheLotka-Volterramodeldescribesthepopulationsoftwospecies: prey,v1,andpredators,v2. Thepreyreproduceatrate
α, the predators die at rate γ and new predators are produced through predation at rate β. When modelled with ODEs,
thisgivesusthefollowingsystem:
dv1
=αv1−βv1v2,
dt
(5)
dv2
=βv1v2−γv2.
dt
Theperiodicsolutionsto(5)persistevenwhenthepredatorspeciesreachesinfeasiblepopulationsizes: populationsoforder
10−18 givingus“atto-foxes”.
Figure1AshowsacompartmentaldiagramoftheLotka-Volterramodelwiththereaction: r1,birthofv1;r2,deathofv2;
andr3,conversionofv1 intov2. Figure1Bshowsarepresentationofthereactionsandtheircorrespondingstoichiometric
matrix.
Figure 1C depicts a hypothetical trajectory of the Lotka-Volterra model when represented as a JSF process. There are
4

<!-- Page 5 -->

three switching events (at t1, t2 and t3), and each configuration of discrete (jumping) and continuous (flowing) states are
featured:

## Beforet1,therepresentationisV⃗ F =v1 andV⃗ J =v2 andthereactionsareRJ ={r2,r3}(hybridregime).


## During[t1,t2),therepresentationisV⃗ F =(v1,v2)⊺ andV⃗ J =∅andthereactionsareRJ =∅(ODEregime).


## During[t2,t3),therepresentationisV⃗ F =v2 andV⃗ J =v1 andthereactionsareRJ ={r1,r3}(hybridregime).


## Fromt3 onwardstherepresentationisV⃗ F =∅andV⃗ J =(v1,v2)⊺ andthereactionsareRJ =R(CTMCregime).

Figures1DandEshowtwoinstancesofrandomtrajectoriessampledfromtheLotka-Volterraprocessasrepresentedwith
JSF with a switching threshold of Ω=30. In the trajectory in Figure 1D the populations undergo several cycles while in
Figure1E,withtheinclusionofdiscretestochasticbehaviour,thepredatorspeciesgoesextinct,allowingthepreytogrow
exponentially.

### Mathematical detail

Here we provide the mathematical details of JSF: the evolution and computation of values for flowing compartments (see
‘Flow events’); the evolution and computation of values for jumping compartments (see ‘Jump events’); the sampling of
jump times (see ‘Jump clock updates’); and the switching of compartments between jumping and flowing regimes (see
‘Switchingevents’). Furtherdetails,includingpseudo-codelistingsofthealgorithmsusedtosamplefromtheJSFprocess,
aregiveninSISection1.

### Flow events

Equation (3) contains the differential equations describing the evolution of the flowing compartments. If we consider an
interval of time between jumps, [t0,t1], then V⃗ J(t) remains constant and therefore, Λ⃗ J(t,V⃗) = ⃗0 across this interval.
Therefore,thedifferentialequationsfortheflowingcompartmentsare:
dV⃗
F =ηFF ⃗λF(t,V⃗). (6)
dt
ThisisastandarddynamicalsystemofODEs, whichwenumericallyintegrateforwardintimeoverdiscretetimestepsof
size∆t. Whileanarbitraryordermethodmaybeused,weuseasimpleForwardEulermethod:

### V⃗ F(t+∆t)=V⃗ F(t)+∆V⃗ F(t) (7)

=V⃗ F(t)+∆tηFF ⃗λF(t,V⃗)+O(∆t2). (8)
Figures2Aand2Bdepictexamplesofaflowingcompartmentandajumpingcompartment,respectively. Flowupdatesare
givenatintervalsofdiscretetimestep∆tasindicated. IntheJump-Switch-Flowalgorithm,flowingtimestepsarebounded
abovebyafinite,butsmall,∆t. Flowingtimestepshavethismaximumdurationifnojumpsarefoundonthistimeinterval
(thatis,if(6)remainsvalid). Ifajumpoccursat∆τ <∆tfromanygiventime(seeSection‘Jumpevents’)thenaflowing
timestepof∆τ isusedinsteadof∆tinEquation(7). Inthiscase,ajumpisinstantaneouslyappliedaftertheflowevent
and the next interval of time is associated with new flow rates⃗λF (which are therefore updated at the exact moment of
time of the jump event). We note therefore that error associated with the ODE solver is determined by the size of the
finitecappedtimeintervalsize∆taccordingtoclassicalODEerroranalysis. InthiscasesinceweuseForwardEuler,the
errorscalelikeO(∆t2). UsingEquation(7),overeachtimestep(flowinginterval),floweventsonlydirectlyaffectflowing
compartmentsascanbeseeninFigure2A.JumpingcompartmentslikethatshowninFigure2Bareunaffecteddirectlyby
flowingeventsbecausethemomentsofajumpingeventarepre-determinedaccordingtoapproximationsinthetrajectories
of the flowing compartments which have the same accuracy as the ODE solver (for example, we assume a linear changes
in the flowing compartments as consistent with Forward Euler method used in Equation (7) – see Section ‘Jump events’
fordetails. AsindicatedbydiscontinuitiesinbothFigure2AandFigure2B,jumpeventsmaybeappliedtoflowingand
jumpingcompartmentsalikeinordertoconservemassinamannerwhichweshallnowdescribe.

### Jump events

The reactions in RJ produce discontinuous jumps in the state vector V⃗. In Equations (3) and (4), each element in the
vectorΛ⃗ J correspondstoareactioninRJ. Consider,forexample,r k ∈RJ. Thekth elementofΛ⃗ J is:
Λ(k)= (cid:88) δ (cid:16) t−t(k)(cid:17) , (9)
J i
i
where δ is the Dirac delta function and t(k) is the time at which the reaction r occurs for the ith time. In this way,
i k
the term Λ⃗ J in Equations (3) and (4) manifests as discrete jumps in both V⃗ F and V⃗ J at each jump. For the sake of the
simulation,thecomputationofthejumptimest(
i
k) foreachinstanceiofeachreactionr
k
∈RJ isallthatisrequired. The
stoichiometricmatrixdescribesthechangetoeachcompartmentwhenthatjumpeventoccurs.
5

<!-- Page 6 -->

Figure 2: The JSF process can be numerically integrated. A and B: Dynamic changes in flowing compartments (A)
and jumping compartments (B). Flows are computed using the time step ∆t. If a jump occurs within a flow update,
the flows are adjusted up until the corresponding time ∆τ as a time step instead of ∆t (indicated by a discontinuity
in both A and B). Jumps occur when a jump clock reaches zero. C: The jump clock J for reaction k counts down
k
until event k occurs when J = 0, i.e. between t when J > 0 and t+∆t when J < 0. The time of the jump
k k k
is found by interpolating for t+∆τ using Equation (16), where ∆τ < ∆t. Once the jump has occurred and jumps
implemented according to the respective stoichiometric updates, J is reinitialised by sampling J =−log(u ) where
k k k
u ∼Unif(0,1), and thencounts down withsuccessivetime steps∆tuntil the next jumpk isrealised. D A switching
k
eventoftype1occurswhenadiscretecompartmentjumpsabovetheswitchingthreshold,Ω. Thisisshownhereafter
the jump time step ∆τ . E A switching event of type 2 occurs when a flowing compartment reaches the switching
2
threshold, Ω. Here, the time at which the switch occurs is found using continuation. F A switching event of type
3 occurs when a flowing compartment is caused to go below the switching threshold, Ω, due to a jump in another
compartment. Here the jump has caused the flowing compartment to end at the dotted circle (which we denote as
vˆ). Thiscompartmentisthenre-labelledasjumping. Sincejumpingcompartmentsrequireintegerstates,thestateis
i
re-initialised to take the value ⌈vˆ⌉ with probability v −⌊vˆ⌋, and otherwise ⌊vˆ⌋ such that the expected value of the
i i i i
state is at the dotted circle (in the example presented here, the variable was rounded down). For all switching events,
membership of V and V is recomputed after switching.

## F J

The rate of reaction r , λ (t,V⃗), may be state dependent so can change due to the continuous change caused by flows.
k k
Figures 2A and 2B depict an example of flowing and jumping compartment (respectively) experiencing a jump event. In
thisillustration,wenotethatifλ
k
dependsonv2 theeventtimetk
i
isnotsampledfromanexponentialdistributionwhich
requires a constant propensity/rate between events. Formally, the jump times form an inhomogeneous Poisson process.
Therearemultiplewaystosamplethejumptimest(k),seeKleinetal.,1984foradetaileddiscussion. Weuseavariantof
i
theNextReactionMethodGibsonetal.,2000(whichisanoptimisedvariantoftheDoob-GillespiemethodGillespie,1976)
to sample jump times. We first note that the propensity for a jump is dependent only on the instantaneous state V⃗, and
thereforeattimet0 iftherehasbeeni−1jumpsassociatedwithreactionr
k
,ithasnobearingonthedistributionofthe
time t(k). Therefore, we shall simply denote t(k) =t as the next jump time for reaction r . The cumulative probability
i i k k
functionfromwhicht
k
issampleddependsonthecurrenttime, t0, andtheevolutionofthestatevariablesintime, V⃗(t).
Thecumulativedistributionforthetimeofthenexteventassociatedwithr is:
k
(cid:26) (cid:90) t (cid:27)
CDF(t;k)=1−exp − λ (s,V⃗(s))ds . (10)
k
t0
Tosamplet ,inversetransformsamplingisusedKleinetal.,1984,i.e.sampleu ∼Unif(0,1)andthensolveCDF(t ;k)=u
k k k k
for t . To account for the varying state, we define a new function, J (t) the jump clock for reaction r , using Equation
k k k
(10),andsolvingforwhenCDF(t ;k)=u (inversetransformsampling). Thejumpclockactsasatimer,identifyingthe
k k
timet forwhenr nextoccurs,whenJ (t )=0. ThefunctionJ isdefinedby:
k k k k k
J (t )=−log(u )−
(cid:90) tk
λ (s,V⃗(s))ds, (11)
k k k k
t0
noting that u and 1−u have the same distribution. In general, we cannot solve directly for t , so we solve for it
k k k
numericallybytrackingthevalueofJ (t)asV⃗ evolvesthroughflows,jumpsandswitches.
k
For each reaction r , at some initial time, for example t(k), being the continuous time of the (i−1)th jump associated
k i−1
withreactionr
k
,wesampleu
k
andinitialiset0=t(
i−
k)
1
. TheinitialvalueofJ
k
(t)isthereforeequaltothepositivenumber
log(u−1) (since u ∼ Unif(0,1)). As time progresses, J (t) decreases according to (11) since λ ≥ 0. The value of J (t)
k k k k k
6

<!-- Page 7 -->

decreases to zero over time and when J (t) = 0, a jump associated with r is triggered (hence the name “jump clock”).
k k
Onceajumpclockreaches0andajumpistriggered,theclockisresetbysamplinganewrandomnumber,u ∼Unif(0,1).
k
SeeFigure2Cforaschematicillustrationofhowthejumpclockisupdated.
Toupdatethejumpclock,werequirenumericalintegrationofλ (t,V⃗(t))forwardintime. Fortunately,wealsohavepiecek
wise polynomial approximations for V⃗ F(t) as a result of our numerical treatment of the continuous flows (see Subsection
‘Flow events’), combined with piece-wise constant values for V⃗ J(t) which only change when jumps occur. We discuss the
numericalintegrationofthejumpclockbelow.

### Jump clock updates

Foragivenjumpreactionr
k
,ajumpclockisinitialisedattimet0 withu
k
∼Unif(0,1)givingJ
k
=log(u−
k
1). Fromtimet
tot+∆t,witht>t0,Equation(11)tellsustheclockticksdownfromJ
k
toJ
k

## −∆J

k
,where∆J
k
is
(cid:90) ∆t
∆J = λ (t+s,V⃗(t+s))ds. (12)
k k
0
Ingeneralthisintegralisintractable,butwecanapproximateitasfollows: considertheTaylorexpansionofλ (t+s,V⃗(t+s))
k
abouts=0,whichgives
(cid:90) ∆t ∂λ dV⃗⊺ (cid:90) ∆t
∆J = λ (t,V⃗)+ k s+O(s2)ds= α+βs+O(s2)ds, (13)
k 0 k ∂V⃗ dt 0
∂λ dV⃗⊺
where we write α = λ (t,V⃗), and β = k . Since (i) our numerical evaluation of V⃗ is piece-wise linear across the
k ∂V⃗ dt
timeinterval,byvirtueofthefactthatweuseaForwardEulerapproximationtosolvingEquation(6),and(ii)∆tissmall,
∆J isapproximatedtotheprecisionofouralgorithmbytaking
k
∆t
∆J ≈ (2α+β∆t), (14)
k 2
noting that since V⃗ is piece-wise linear across the time interval, the convergence of the integration of the Jump-clock
also behaves as ∆t. Importantly, we know that between jumps
dV⃗
F is given by Equation (6) whilst
dV⃗
J = 0. Thus,
dt dt
∂λ (cid:16) (cid:17)⊺
β =

## ∂V⃗


## F

k ηFF ⃗λF(t,V⃗) (evaluated at t). To calculate the updated jump clock, we compute J
k
(t+∆t)=J
k
(t)−∆J
k
astheprovisionalvalue. Wethenhavetwodistinctcases: (i)J (t)−∆J >0,thennojumpoccurredduringtheinterval
k k
(t,t+∆t) and we have the jump clock J (t+∆t):=J (t)−∆J : (ii) J (t)−∆J <0, then a jump occurred (i.e. a r
k k k k k k
reaction)duringtheinterval(t,t+∆t), thatweneedtoaccountforintheupdatedjumpclock. Inthecase(ii)wherea
jumpoccurswithintheinterval(t,t+∆t),lett+∆τ,where0<∆τ <∆t,denotethetimeatwhichthisjumpoccurs. We
canfind∆τ byinterpolationandsolvingthefollowingfor∆τ:
2∆J −∆τ(2α+β∆τ)=0, (15)
k
where∆J istheresidualofthejumpclockfromttot+∆τ. ∆τ isthengivenby
k
√
 α2+2β∆Jk−α, β̸=0,
∆τ = β (16)
 α , β=0.
∆Jk
Ifthereisajump,ratherthanusing∆ttoforwardcomputetheflowingcompartmentsinEquation(7)weinsteaduse∆τ
to take part of a flow step and then implement the jump after the flow to get the state at time t+∆τ. After this, we
reinitialisethejumpclockJ asdescribedabove. ThisprocedureisillustratedinFigure2C.
k

### Switching events

The way in which we handle switching is one of the main contributions of this manuscript. Switching events occur when
variablestransitionbetweenV⃗ J andV⃗ F,i.e. betweendiscreteorcontinuousvalues. Asaconsequence,thecontentsofRJ
and RF may change. There are three types of switching events. The first involves a compartment moving from V⃗ J to
V⃗ F. This transition is straightforward as a new equation is added to Equation (6), and the state V⃗ F is initialised at the
switchingtime, withthenew flowingcompartmentatΩ. Figure2Ddepictsan exampleofatype 1switching event. The
secondtypeinvolvesaflowingcompartmentmovingfromV⃗ F toV⃗ J. Here,theflowingcompartmentreachestheswitching
threshold, Ω, and becomes discrete and no longer follows the flowing dynamics (of Equation (6)). The time at which this
occursisfoundbycontinuation,andcomputationisresumed. Figure2Edepictsanexampleofatype2switchingevent.
The third type of switching event involves a compartment jumping from V⃗ F to V⃗ J. In this case, a flowing compartment
jumpsdowntotheswitchingthresholdΩ,andbecomesdiscrete. Tohighlighthowthethirdtypeofswitcheventisnecessary,
we propose considering a simple model where two species, X and Y, interact to produce a third species, Z, with X also
undergoing a death dominated birth-death process. Suppose that the switching threshold is set as Ω = 1000, and that
X(0) = 1001, Y(0) = 10 and Z(0) = 0. Due to the death reaction of X, suppose that within the first (Flow) step, X
experiences some decay ε < 1. Therefore, X(t1) = 1001−ε > Ω = 1000 is in a flowing (continuous) regime. Now let’s
supposethatinthenextinstance,X andY combinetoproduceoneZ. Atthisinstance,X mustexperiencesomeinteger
loss (which we can assume to be 1, but in general may be any positive value). In this case, producing Z will result in
X(t2)<Ωbutnoninteger. Therefore,toaccountfortypethreeswitchevents, letvi bethecompartmentswitchingfrom
7

<!-- Page 8 -->

V⃗ F to V⃗ J due to a jump. In general, these types of jumps result in vi being non-integer, i.e. vi ∈/ {0,1,...,Ω}∪(Ω,∞).
To ensure the values of vi stay in {0,1,...,Ω}∪(Ω,∞), we add another constraint to the process, initially proposed by
Rebuli et al. Rebuli et al., 2017. The idea is to randomly round the compartment value up or down to an integer in a
waythatconservestheaveragebehaviouroftheprocess. Letvˆi bethevalueoftheflowingcompartmentvi afterjumping
downacrossthethresholdΩbutbeforebeingroundedinto{0,1,...,Ω}∪(Ω,∞). Weapplythefollowingruletoroundvi
after the switch. We take vi =⌈vˆi⌉ with probability vˆi−⌊vˆi⌋, and otherwise we round down by setting vi =⌊vˆi⌋. This
ensures the expected value of the variable after the switch is vˆi as described under the flowing paradigm from which this
compartmenthascomeandthatthevariableremainsinthedomain{0,1,...,Ω}∪(Ω,∞). Figure2Fdepictsanexample
ofatype3switchingevent.

### Results


### Effects of interventions to reduce transmission

Simulation based inference (e.g. the particle filter) relies on being able to efficiently simulate from the generative process.
TodemonstratehowJSFcanbeusedinthissetting,wefirstpresentasimulationstudyofforecastingtheeliminationofa
infectiouspathogen.

### SIRS model with demography

The SIRS model with demography is an extension of the classic susceptible-infectious-removed (SIR) model. In the SIR
modelsusceptible individualsmaybeinfectedbycontactwithinfectious individuals; infectedindividualseventuallycease
to be infectious and transition to the removed compartment. The SIRS model with demography extends the SIR model
by allowing removed individuals to transition back to being susceptible to infection, for individuals to give birth to new
(susceptible)individuals,andtoallowfordeathofindividuals(atequalrates). TheSIRSmodelwithdemographycanbe
writtenasthefollowingODEsystem,withsusceptible(S),infectious(I),andrecovered(R)individuals:
dS IS
=−β +ωR+κN−µS,
dt N
dI IS
=β −γI−µI, (17)
dt N
dR
=γI−ωR−µR,
dt
where N(t) = S(t)+I(t)+R(t) is the total population size, β the infection rate, γ the recovery rate, ω the immunity
waning rate, κ the birth rate, and µ the death rate. Figure 3A shows a compartmental diagram of the SIRS model with
demography.
Figure3Bshowsoursimulated(viatheDoob-Gillespiealgorithm)timeseriesofdailynoisymeasurementsoftheprevalence
ofinfection. ThetrueparametersusedinthesimulationareshowninFigure3C;thesevaluesarebroadlyconsistentwith
existingestimatesforinfluenzaorSARS-CoV-2. Weassumethatthesemeasurementsaredrawnfromanegativebinomial
distributionwheretheexpectedvalueisequaltothetrueprevalenceofinfectionandthereisaconstant(known)dispersion
parameter,k=100.

### Estimating elimination probabilities

CombiningtheSIRSmodelwithaparticlefilter(Moss,2024;Kitagawa,1996)weusedthefirst100daysofthetimeseries
toforecasttheremaining150days. Figure3Bshowstheestimatedtrueprevalenceacrossthefirst100daysandforecasts
theprevalenceforthesubsequent150days. Includedintheforecastisadailyestimateoftheprobabilitythatthepathogen
has been eliminated (in the simulation the pathogen was eliminated on day 250). It is important to note that there is an
endemicequilibriuminthismodel,soitisreasonablefortheprobabilitytoplateauasitdoes.
To demonstrate the utility of the posterior distribution (i.e. the capacity of the particle filter to forecast the epidemic
after the 100 days of observed data), we considered the impact of a possible intervention. This intervention, introduced
on day 100, reduces the force of infection (and hence the effective reproduction number) by a factor of α. Figure 3D
shows how the probability of eliminating the pathogen increases substantially as we decrease α from 1 (no intervention)
to 0.7 (a 30% reduction in transmission). The fade-out probability is calculated as the proportion of sampled (hybrid
stochastic-deterministic)trajectoriesthatgoextinct(viaI=0)ofthetotalnumberofsampledtrajectories.
The full details of the configuration of the particle filter, and the marginal posterior distributions are given in SI Section

## 2E.


### Computational properties

To further investigate the computational properties of JSF and to compare it with exact (Doob-Gillespie) simulation and
(approximate)tau-leapingsimulationweusedrepeatedsimulationsfromtheSIRSmodelwithdemography. Wepartitioned
8

<!-- Page 9 -->

Figure 3: JSF enables us to forecast when a pathogen will be eliminated from a population, i.e. when we can claim
that an epidemic has “ended”, and quantify the likely impact of varying levels of intervention. A A compartmental
model representation of the SIRS with demography. B A simulated time series of noisy measurements of prevalence
along with inferred prevalence trajectories and forecasts of future prevalence with associated uncertainty bands. The
dashed vertical line indicates the date up until which we have data. The solid blue line indicates an estimate of the
probabilitythatthepathogenhasbeeneliminatedfromthepopulation(asopposedtopersistingatverylowlevels). C
The true parameters used in the simulation along with their posterior estimates and the associated priors used. Each
of the marginal posterior distributions peaks tightly about the true value. D The probability of pathogen elimination
increases with the strength of the intervention against transmission. Near certainty of elimination is achieved with a
30% reduction of transmission.
thesimulationsintothreeclasses: earlystochasticextinction,fade-outafterasingleepidemic,andsustainedtransmission
(SI Section 2.) As seen in Table SI 3, JSF and exact simulation generate very similar proportions of samples in each of
theseclasses. Twoaspectsofthissystemofpracticalimportancearethetimingandmagnitudeofpeakinfections,andthe
total number of infections. As can be seen in Figure SI 7 the distribution of peak timing and total number of infections
areingoodagreementbetweenJSFandexactsimulation. Forthemagnitudeofpeakinfections,thereissubstantiallyless
variabilityintheJSFsamplesthantheexactsamples,buttheproportionaldifferenceissmall.
With regards to computational efficiency, Figure SI 10B shows the average time required per simulation using JSF, exact
simulation (Doob-Gillespie), tau-leaping, and the efficient Tau-hybrid method Matthew et al., 2023 for the SIRS model
for populations of different sizes. For populations of size above about 105 (i.e. approximately the size of a small city),
JSFissubstantiallycomputationallyfasterthaneitherexactsimulationortau-leaping,therebeingadifferenceofatleast
one order of magnitude in the amount of time needed, and (if a suitable Switching threshold is specified) a constant
scaling, irrespective of compartment occupancy, may be obtained. To simplify the interpretation of the results in Figure
SI 10B, each of the methods were implemented in the same interpreted language so that the observed differences can be
attributedtothealgorithmratherthantheplatformonwhichitisimplemented. Wehavealsoincludedacomprehensive
simulationcasestudyofthesimplebirth-deathprocess(seeSectionSI2ofthesupplementaryinformation),whichexhibits
JSfcomputationalefficiencyforbothbirthdominatedanddeathdominatedregimes,withcomparableresultstotheexact
stochastic process. We also demonstrate JSF’s accuracy for particularly difficult to solve stochastic simulations which
exhibitmultipletimescales(seeSectionSI3ofthesupplementaryinformation),whereweseethatJSFproducessummary
statisticsandtrajectoriescomparabletotheexactstochasticprocess,outperformingcurrenthybridmethods.

### SARS-CoV-2 virus clearance informed by longitudinal data

Understanding viral clearance is important when deciding how long treatment must be maintained. This case study
demonstrateshowJSFenablesinferenceofvirusclearance,whichhasbeencomputationallychallengingtodateYanetal.,
2016;Farrukeeetal.,2018. Inparticular,weuseamathematicalmodel—theTEIRVmodeldescribedbelow—tostudy
viralclearanceusinglongitudinaldatafrom6individualsinfectedwithSARS-CoV-2Keetal.,2022.

### TEIRV model of within-host viral dynamics

TheTEIRVmodelisanextensionoftheclassictarget-infected-virus(TIV)modelPerelson,2002. IntheTIVmodeltarget
cellsmaybeinfected bythevirus;beforedying,infectedcellsproducevirus;andtheviruscandegradeorinfectremaining
target cells. The TEIRV extends the TIV model through the inclusion of an eclipsed compartment, to model the delay
betweeninfectionofatargetcellandthesubsequentproductionofvirus,andarefractorycompartment,tomodelheightened
antiviraldefencesoftargetcells,e.g.throughtheeffectsofinterferonsKeetal.,2022;Blanco-Meloetal.,2020. Tosimplify
9

<!-- Page 10 -->

Figure 4: The TEIRV model describes the within-host dynamics of host cells and virus during infection. The model
accountsfordelaysinvirusproductionpostcellularinfectionandthecapabilityoftargetcellstoenterarefractorystate
as a defence against infection. A A compartmental diagram of the TEIRV model showing the interactions between:
Target cells (T), Refractory cells (R), cells in the Eclipsed phase of infection (E) and Infectious cells (I); and the
(Total) Virions (V). Total Virion particles are utilised as to not distinguish between intra- and extra-cellular Virions.
Solid arrows represent the exchange of mass (cells or virions) through compartments, while dashed lines represent the
influenceofacompartmentonareaction’srateofoccurrence. BTherepresentationofthismodelasareactionnetwork
with a stoichiometric matrix. This formalises the dependency on different variables indicated by the dashed arrows in
the compartmental diagram. C An example trajectory showing the exponential growth and decline in the amount of
freevirusacrossthedurationoftheinfection,thisprocessterminatesinthevirus,eclispseandinfectedcellpopulations
reaching zero (shortly before time 12). Reaching zero which is possible in this hybrid continuous/discrete stochastic
model but does not occur in a purely ODE based representation.
theuseofthismodelaquasi-steady-stateapproximationforinterferonproductionisemployed. Thisapproximationallows
ustoavoidtheneedtoexplicitlymodeltheamountofinterferonpresent.
Figure 4A shows a compartmental diagram of the TEIRV model. Target cells becoming infected by virions at rate β,
whichthenentertheeclipsedphase. Theseeclipsedcellsthenbecomeinfectiousatratek. Infectiouscellsareclearedfrom
the population at rate δ, and produce virions at rate π. Virions are themselves cleared at rate c. We note that V is the
total number of virion particles, and therefore this model does not distinguish between intra- and extra-cellular virions.
As a result, following the infection of a target cell (T), no virion particles are lost, in this model. The infectious cells
recruitinterferon,whichcausethetargetcellstobecomerefractory(andhenceprotectedagainstinfection)atrateΦ. The
refractorycellsreturntoanaivestateastargetcellsatrateρ. TheseassumptionsarerepresentedwiththefollowingODE
system:
dT
=−βVT −ΦIT +ρR,
dt
dE
=βVT −kE,
dt
dI
=kE−δI, (18)
dt
dV
=πI−cV,
dt
dR
=ΦIT −ρR.
dt
ThestoichiometricmatrixcorrespondingtotheseassumptionsisshowninFigure4B.Figure4C,whichshowsatrajectory
sampledfromtheTEIRVmodelwhenrepresentedwithJSF;theclassicboom-bustdynamicsoftheviralpopulationscan
be seen in the exponential growth and decline of the V compartment. Unlike solutions of the ODE model in (18), we see
thatbytimet=14,thepopulationsofeclipsedandinfectedcells,andthevirushavegoneextinct,indicatingadefinitive
endtotheinfection.
The basic reproduction number, R0 is a fundamental quantity of epidemiological models. For the TEIRV model, R0 can
becalculatedfromthenext-generationmatrixDiekmannetal.,2010:
πβT(0)

## R0= . (19)

δc
10

<!-- Page 11 -->


### Observation model linking virus to time series

The longitudinal data contains cycle number (CN) values from nasal samples. The CN values are inversely proportional
to the number of virions present. In our analysis we used an existing (empirical) model to link the cycle numbers to the
(logarithmic)viralgenomeloadKeetal.,2022: log V =11.35−0.25CN. Weassumetheobservedvaluesaredrawnfrom
10
a normal distribution with mean log V and unit standard deviation, and that the values are truncated at the detection
10
limitof−0.65.

### Estimating virus reproduction and clearance

Recallthattheparticlefilteriscapableofcombiningamechanisticmodelofthewithin-hostdynamics,suchastheTEIRV,
andanobservationmodel,suchastheviralloadmeasurements,andwillreturna(Bayesian)posteriorsampleofboththe
parameters of the process and the trajectory of virus and cell populations through time. We assume that the infection
begins with a single exposed target cell (in a population of 8×107 target cells) Ke et al., 2022. This gives us an initial
conditionfortheprocess: T(0)=8×107,E(0)=1,I(0)=0,R(0)=0. Weleavetheinitialviralload,V(0),asaparameter
tobefittothedata.
WeselectedsixpatienttimeseriesKeetal.,2022,choosingonesthatcontainedafull14datapoints,forbothconsistency
and simplicity. Two of the model parameters were fixed as in previous analysis Ke et al., 2022: c = 10, k = 4. See SI
Section3forfulldetailsoftheparticlefilterandJSFconfiguration.
Figure 5A shows our model fits to the first 10 days of viral load data for the six selected patients. After day 10, using
the estimated parameters, we generate and predict the distribution of subsequent viral load until day 20. The estimated
viral peak coincides with the data for each of the patients and the predicted viral trajectories closely match subsequent
observations.
We estimate the probability of viral clearance over time (right blue axis of in the panels of Figure 5A). Viral clearance is
definedbythepointatwhichthevirion,eclipsed,andinfectedcellpopulationsallreachextinction. Wenotethatthisisa
conservativemeasureifonewereonlyinterestedinwhenapatient’sinfectiousness becomesnegligible. However,forproof
ofconceptofinferringsuchquantities,wehavechosentoestimatetheprobabilityofcompleteviralclearance.
There is clear heterogeneity in the amount of time required to clear the virus (Figure 5A). We estimate that with high
certainty patients 423192, 443108 and 445602 clear the virus within 20 days. In contrast, for patients 444332, 444391
and 451152 we infer that they have not cleared the virus within that time frame. Within those who did clear the virus,
we observe that different patients require different amounts of time to clear the virus. Specifically, patient 432192 (5A)
is inferred to have cleared the virus first. Patients 443108 and 445602 both require an estimated 16 days to obtain viral
clearance.
The posterior distributions of the parameters (Figure SI 11) and priors (Table SI 5), are given in SI Section 5. Because
ofpotentialidentifiabilityissueswiththerateparameters,weinsteadcomparetheestimatedreproductionnumber,R0,to
results from previous analysis (Ke et al., 2022). Figure 5B shows the posterior distributions of R0, as well as the point
estimates from Ke et al., 2022. Since the previous analysis, (Ke et al., 2022), reports identical estimates for π, β and
δ across these patients, we only include a single point estimate for their work. Our estimate is consistent with previous
results (Ke et al., 2022) for patients 432192, 445602 and 451152. However, patients 443108, 444332 and 444391 all have
higherR0estimatesinourresults. OurR0estimatesareconsistentwithsimilarwithin-hostviralinfectionanalysesofother
respiratorypathogens(Baccametal.,2006;Hernandez-Vargasetal.,2020;Gubbins,2024).
11

<!-- Page 12 -->

Figure 5: JSFenablestheinferenceoftheviralloadthroughtimeandtheprobabilitythatthevirushasbeencleared
from longitudinal data of SARS-CoV-2 viral load measurements. A Model fits to viral load data based on nasal swabs
of six patients from Ke et al., 2022 using a refractory cell within-host model, using our Jump-Switch-Flow method.
Nasalviralloaddataisshownassoliddots,andthelimitofdetectionisshownasadottedline. Weshowtheswitching
threshold, Ω=102 by a dashed line. The red and purple bands show mean (0%), 25%, 50%, 75% and 95% credible
intervals (from dark to light) for the inference and prediction, respectively. We also estimate the probability of viral
clearanceatagivenpointintime,basedonthepreviousdatatothatpoint,inblue(light). BTheposteriordistribution
ofviralR foreachpatient,alongwiththemedian(whitecircle),Thesepatientspecificestimatesarecontrastedwith
0
the single point estimate from previous analysis Ke et al., 2022.

### Discussion

Wehavepresentedasimplehybridsimulationmethodforcompartmentalmodels: Jump-Switch-Flow (JSF).Thismethod
facilitates efficient simulation of multi-scale models. Via simulation studies and an analysis of longitudinal data from
SARS-CoV-2 infections we demonstrated the desirable computational properties of this method and the types of novel
analyseswhichitenables. JSFallowscompartmentstodynamicallychangebetweenstochasticanddeterministicbehaviour.
Combining JSF with a simulation based inference method, e.g. a particle filter, enables inference for multi-scale models,
andinsituationswhereabsorbingstates(suchasapopulationgoingextinct)areimportant.
SimulationsshowsJSFproducestrajectorieslargelyconsistentwithgoldstandardexactsimulationtechniques,e.g.Doob-
Gillespie algorithm (see for example Figures SI 1–SI 4 and SI 6 – SI 9). We demonstrate how JSF is highly accurate at
producing summary statistics comparable to gold standard exact simulation techniques (see Figures SI 1 – SI 4), with a
significant improvement in accuracy for problems with multiple time scales when compared to currently available hybrid
methods (see Figure SI 3 and SI 4) However, JSF is also much faster for realistic population sizes (as can be seen in the
comparisonofcomputationalspeedinFigureSI10B).Wedemonstratehowourapproachcanbeincorporatedintoaparticle
filter(Moss,2024),toperformparameterandstateestimationandprediction(seeFigure3).
12

<!-- Page 13 -->

AstrengthofJSFisthecapacitytoinferwhenaprocesshasreachedanabsorbingstate,forexample,anepidemicfadingout, or a virus being cleared. The ability to infer when an absorbing state has been reached is important for calibrating
interventionmeasures(Paragetal.,2020)andunderstandingimmuneresponse(Yanetal.,2016). ODEbasedmodelsrarely
have absorbing states that can be reached in finite time, which fundamentally limits their capacity to describe extinction
andclearanceprocesses.
WeanalysedviralloadforSARS-CoV-2infectionsusingtheJSFwithinaparticlefilterwithaTEIRV,refractorycellmodel
(Ke et al., 2022). In the subset of the data considered, we find consistent parameter values between patients (SI Section
3). In a novel analysis, we estimated the probability of viral clearance through time, finding substantial heterogeneity in
the timeuntil viralclearance (see Figure5A). This isimportant as anaccurate quantification of whenthe virushas been
clearediscrucialfordeterminingappropriatetreatmentregimes.
AkeyadvantageofJSFistheabilitytocombinethestochasticityofdiscretesmallpopulationswithconvenientdeterministic
modelsforlargepopulations. Thepointatwhichacompartmentwilltransitionbetweenthesedescriptionsisspecifiedby
thethresholdparametersΩi (oneforeachcompartment). Settingtheseparameterstolowvaluesspeedsupcomputation,
while setting them higher captures more of the stochasticity in the process. As demonstrated in the simulation studies,
an appropriate value can be determined through some preliminary simulations (see SI 4 for an example of preliminary
simulationanalysisfortheSIRSmodelexample). Animportantconsiderationinselectingthisparameterisensuringthat
theabsorbingstatescanstillbereached(e.g.compartmentextinction),andthatstableandsteadystatescanbeperturbed
byrandomfluctuations. PotentialconsiderationswhenspecifyingthevaluesΩi mayalsoincludepreliminarysimulations,
increasingΩiandobservinghowthecomputationalcomplexityscales(seeFigureSI10). Furthermore,developingtheoryto
betterunderstandwhenaCTMCiswellapproximatedbyanODEisatthecoretodeterminehowtheswitchingthreshold
shouldbechosen. UnderstandingintothenumericalpropertiesoftheJump-Switch-Flowprocess,andhowconvergenceof
the method behaves for arbitrary choices of Flow event solvers will also prove to be an exciting area of further research.
However,theseliesoutsidethescopeofthiswork.
ExtensionsincludetheincorporationofanintermittentStochasticDifferentialEquationapproximationbetweentheCTMC
andODEregimes,andextensiontospatialprocesseswhichexhibitbothstochasticanddeterministicbehaviours.
Themodellingframeworkpresentedinthispaperhasthepotentialtochangethewaycompartmentalmodelsaredeveloped
and calibrated, moving us towards more accurate and more efficient hybrid methods. These models will help to form the
basisofinformeddecisionmaking,basedonrealisticandaccuratedescriptionsofthesystem. Thishasbroadapplicability,
fromecologicalmodels,chemicalsystemsandsinglecellmodels,toinfectiousdiseasesandwithin-hostmodels.

### Acknowledgement

WethankAdaYanforhelpfuldiscussionsregardingwithin-hostmodelling. J.A.F.’sresearchissupportedbytheAustralian
Research Council (FT210100034, CE230100001) and the National Health and Medical Research Council (APP2019093).
S.H.’sresearchissupportedbytheAustralianResearchCouncil(DP200101281).

### Data Availability

The manuscript has associated data in a data repository available at https://github.com/DGermano8/JSFGermano2024.
OriginaldatarelatedtoSARS-CoV-2viralloadmeasurementscanalsobefoundatKeetal.,2022.

### Code Availability

All code to reproduce our results is available at https://github.com/DGermano8/JSFGermano2024. A Python package
implementingtheJump-Switch-Flowmethodisavailableathttps://DGermano8.github.io/JSF.

### Author Contributions

J.A.F and M.B.F conceptualised research; D.P.J.G, A.E.Z, S.H., R.M, J.A.F and M.B.F designed research; D.P.J.G and
A.E.Z performed research; D.P.J.G, A.E.Z and R.M contributed software tools; D.P.J.G and A.E.Z analyzed data; J.A.F
andM.B.Fsupervisedresearch;D.P.J.GandA.E.Zwrotethepaper;D.P.J.G,A.E.Z,S.H.,R.M,J.A.FandM.B.Freviewed
thepaper;J.A.Facquiredfunding.

### References

Alahmadi,A.A.,J.A.Flegg,D.G.Cochrane,C.C.Drovandi,andJ.M.Keith(2020).“Acomparisonofapproximate
versus exact techniques for Bayesian parameter inference in nonlinear ordinary differential equation models”.
In: Royal Society Open Science 7.3, p. 191315. doi: 10.1098/rsos.191315.
13

<!-- Page 14 -->

Anderson, R.M. and R.M. May (1991). Infectious diseases of humans: dynamics and control. Oxford University
Press.
Angius, A., G. Balbo, M. Beccuti, E. Bibbona, A. Horvath, and R. Sirovich (2015). “Approximate analysis of
biologicalsystemsbyhybridswitchingjumpdiffusion”.In:TheoreticalComputerScience 587,pp.49–72.doi:
10.1016/j.tcs.2015.03.015.
Arulampalam, M.S., S. Maskell, N. Gordon, and T. Clapp (2002). “A tutorial on particle filters for online
nonlinear/non-Gaussian Bayesian tracking”. In: IEEE Transactions on Signal Processing 50.2, pp. 174–188.
doi: 10.1109/78.978374.
Baccam,P.,C.Beauchemin,C.A.Macken,F.G.Hayden,andA.S.Perelson(2006).“KineticsofInfluenzaAVirus
Infection in Humans”. In: Journal of Virology 80.15, pp. 7590–7599. doi: 10.1128/jvi.01623-05.
Blanco-Melo,D.,B.E.Nilsson-Payant,W.C.Liu,S.Uhl,D.Hoagland,R.Møller,T.X.Jordan,K.Oishi,M.Panis,
D. Sachs, T.T. Wang, R.E. Schwartz, J.K. Lim, R.A. Albrecht, and B.R. tenOever (2020). “Imbalanced Host
ResponsetoSARS-CoV-2DrivesDevelopmentofCOVID-19”.In:Cell 181.5,1036–1045.e9.doi:10.1016/j.
cell.2020.04.026.
Bressloff, P.C. and J.M. Newby (2014). “Path integrals and large deviations in stochastic hybrid systems”. In:
Physical Review E 89.4, p. 042701.
Buckwar, E. and M.G. Riedler (2011). “Runge–Kutta methods for jump-diffusion differential equations”. In:
Journal of Computational and Applied Mathematics 236.6,pp.1155–1182.doi:10.1016/j.cam.2011.08.001.
Cao, Y., D.T. Gillespie, and L.R. Petzold (2006). “Efficient step size selection for the tau-leaping simulation
method”. In: The Journal of Chemical Physics 124.4, p. 044109. doi: 10.1063/1.2159468.
Cotter, S.L. and R. Erban (2016). “Error Analysis of Diffusion Approximation Methods for Multiscale Systems
inReactionKinetics”.In:SIAMJournalonScientificComputing 38.1,B144–B163.doi:10.1137/14100052X.
Diekmann, O., J.A.P. Heesterbeek, and M.G. Roberts (2010). “The construction of next-generation matrices
for compartmental epidemic models”. In: Journal of The Royal Society Interface 7.47, pp. 873–885. doi:
10.1098/rsif.2009.0386.
Farrukee,R.,A.E.Zarebski,J.M.McCaw,J.D.Bloom,P.C.Reading,andA.C.Hurt(2018).“Characterizationof
Influenza B Virus Variants with Reduced Neuraminidase Inhibitor Susceptibility”. In: Antimicrobial Agents
and Chemotherapy 62.11, 10.1128/aac.01081–18. doi: 10.1128/aac.01081-18.
Flegg, M.B., S.J. Chapman, L. Zheng, and R. Erban (2014). “Analysis of the Two-Regime Method on Square
Meshes”. In: SIAM Journal on Scientific Computing 36.3, B561–B588. doi: 10.1137/130915844.
Fowler, A.C. (2021). “Atto-Foxes and Other Minutiae”. In: Bulletin of Mathematical Biology 83.10, p. 104. doi:
10.1007/s11538-021-00936-x.
Gibson,M.A.andJ.Bruck(2000).“EfficientExactStochasticSimulationofChemicalSystemswithManySpecies
andManyChannels”.In:TheJournalofPhysicalChemistryA104.9,pp.1876–1889.doi:10.1021/jp993732q.
Gillespie, D.T. (1976). “A general method for numerically simulating the stochastic time evolution of coupled
chemical reactions”. In: Journal of Computational Physics 22.4, pp. 403–434. doi: 10.1016/0021-9991(76)
90041-3.
— (2000). “The chemical Langevin equation”. In: The Journal of Chemical Physics 113.1, pp. 297–306. doi:
10.1063/1.481811.
— (2001). “Approximate accelerated stochastic simulation of chemically reacting systems”. In: The Journal of
chemical physics 115.4, pp. 1716–1733.
Gubbins,S.(2024).“Quantifyingtherelationshipbetweenwithin-hostdynamicsandtransmissionforviraldiseases
of livestock”. In: Journal of the Royal Society Interface 21.211, p. 20230445. doi: 10.1098/rsif.2023.0445.
Hernandez-Vargas, E.A. and J.X. Velasco-Hernandez (2020). “In-host Mathematical Modelling of COVID-19 in
Humans”. In: Annual Reviews in Control 50, pp. 448–456. doi: 10.1016/j.arcontrol.2020.09.006.
Ionides, E.L., C. Breto´, and A.A. King (2006). “Inference for nonlinear dynamical systems”. In: Proceedings of
the National Academy of Sciences 103.49, pp. 18438–18443. doi: 10.1073/pnas.0603181103.
Isaacson, S.A. (2013). “A convergent reaction-diffusion master equation”. In: The Journal of Chemical Physics
139.5, p. 054101. doi: 10.1063/1.4816377.
Ke,R.,P.P.Martinez,R.L.Smith,L.L.Gibson,A.Mirza,M.Conte,N.Gallagher,CH.Luo,J.Jarrett,R.Zhou,A.
Conte, T. Liu, M. Farjo, K.K.O. Walden, G. Rendon, C.J. Fields, L. Wang, R. Fredrickson, D.C. Edmonson,
M.E. Baughman, K.K. Chiu, H. Choi, K.R. Scardina, S. Bradley, S.L. Gloss, C. Reinhart, J. Yedetore, J.
Quicksall, A.N. Owens, J. Broach, B. Barton, P. Lazar, W.J. Heetderks, M.L. Robinson, H.H. Mostafa, Y.C.
Manabe, A. Pekosz, D.D. McManus, and C.B. Brooke (2022). “Daily longitudinal sampling of SARS-CoV-2
infection reveals substantial heterogeneity in infectiousness”. In: Nature Microbiology 7.5, pp. 640–652. doi:
10.1038/s41564-022-01105-z.
Kitagawa, G. (1996). “Monte Carlo Filter and Smoother for Non-Gaussian Nonlinear State Space Models”. In:
Journal of Computational and Graphical Statistics 5.1, pp. 1–25. doi: 10.1080/10618600.1996.10474692.
Klein, R.W. and S.D. Roberts (1984). “A time-varying Poisson arrival process generator”. In: Simulation 43.4,
pp. 193–195. doi: 10.1177/003754978404300406.
Kreger,J.,N.L.Komarova,andD.Wodarz(2021).“Ahybridstochastic-deterministicapproachtoexploremultiple
infection and evolution in HIV”. In: PLOS Computational Biology 17.12, e1009713.
Kurtz, T.G. (1970). “Solutions of ordinary differential equations as limits of pure jump Markov processes”. In:
Journal of Applied Probability 7.1, pp. 49–58. doi: 10.2307/3212147.
14

<!-- Page 15 -->

Kurtz,T.G.(1971).“LimittheoremsforsequencesofjumpMarkovprocessesapproximatingordinarydifferential
processes”. In: Journal of Applied Probability 8.2, pp. 344–356. doi: 10.2307/3211904.
— (1972). “The Relationship between Stochastic and Deterministic Models for Chemical Reactions”. In: The
Journal of Chemical Physics 57.7, pp. 2976–2978. doi: 10.1063/1.1678692.
Kynaston, J.C., C.A. Yates, A.V.F. Hekkink, and C. Guiver (2023). “The regime-conversion method: a hybrid
technique for simulating well-mixed chemical reaction networks”. In: Frontiers in Applied Mathematics and
Statistics 9. doi: 10.3389/fams.2023.1107441.
Lobry,C.andT.Sari(2015).“MigrationsintheRosenzweig-MacArthurmodelandthe“atto-fox”problem”.In:
Revue Africaine de la Recherche en Informatique et Math´ematiques Appliqu´ees 20, pp. 95–125.
Ludwig, D., D.D. Jones, and C.S. Holling (1978). “Qualitative analysis of insect outbreak systems: the spruce
budworm and forest”. In: Journal of Animal Ecology 47.1, pp. 315–332.
Matthew, S., F. Carter, J. Cooper, M. Dippel, E. Green, S. Hodges, M. Kidwell, D. Nickerson, B. Rumsey, J.
Reeve, L.R. Petzold, K.R. Sanft, and B. Drawert (2023). “GillesPy2: a biochemical modeling framework for
simulation driven biological discovery”. In: Letters in biomathematics 10.1, p. 87.
Mollison, D. (1991). “Dependence of epidemic and population velocities on basic parameters”. In: Mathematical
Biosciences 107.2, pp. 255–287. doi: 10.1016/0025-5564(91)90009-8.
Moss, R. (2024). “pypfilt: a particle filter for Python”. In: Journal of Open Source Software 9.96, p. 6276. doi:
10.21105/joss.06276. url: 10.21105/joss.06276.
Parag, Kris V., Christl A. Donnelly, Rahul Jha, and Robin N. Thompson (Nov. 2020). “An exact method for
quantifying the reliability of end-of-epidemic declarations in real time”. In: PLOS Computational Biology
16.11, pp. 1–21. doi: 10.1371/journal.pcbi.1008478.
Pearson, J.E., P. Krapivsky, and A.S. Perelson (2011). “Stochastic Theory of Early Viral Infection: Continuous
versus Burst Productionof Virions”. In: PLOS Computational Biology 7.2, pp. 1–17. doi: 10.1371/journal.
pcbi.1001058.
Perelson, A.S. (2002). “Modelling viral and immune system dynamics”. In: Nature Reviews Immunology 2.1,
pp. 28–36. doi: 10.1038/nri700.
Rao,C.V.andA.P.Arkin(2003).“Stochasticchemicalkineticsandthequasi-steady-stateassumption:Application
to the Gillespie algorithm”. In: The Journal of Chemical Physics 118.11, pp. 4999–5010. doi: 10.1063/1.
1545446.
Rebuli, N.P., N.G. Bean, and J.V. Ross (2017). “Hybrid Markov chain models of S–I–R disease dynamics”. In:
Journal of Mathematical Biology 75, pp. 521–541.
Sanft, K.R. and H.G. Othmer (2015). “Constant-complexity stochastic simulation algorithm with optimal binning”. In: The Journal of Chemical Physics 143.7, p. 074108. doi: 10.1063/1.4928635.
Simoni, G., F. Reali, C. Priami, and L. Marchetti (2019). “Stochastic simulation algorithms for computational
systems biology: Exact, approximate, and hybrid methods”. In: WIREs Systems Biology and Medicine 11.6,
e1459. doi: 10.1002/wsbm.1459.
Trindade, T.T. and K.C. Zygalakis (2024). “A hybrid tau-leap for simulating chemical kinetics with applications
to parameter estimation”. In: Royal Society Open Science 11.12, p. 240157. doi: 10.1098/rsos.240157.
Yan,A.W.C.,P.Cao,andJ.M.McCaw(2016).“Ontheextinctionprobabilityinmodelsofwithin-hostinfection:
the role of latency and immunity”. In: Journal of Mathematical Biology 73.4, pp. 787–813. doi: 10.1007/
s00285-015-0961-5.
15

<!-- Page 16 -->

Supplementary Information: A hybrid framework for compartmental
models enabling simulation-based inference
Domenic P.J. Germano a,b,*, Alexander E. Zarebski a,c,*, Sophie Hautphenne a, Robert

### Moss d, Jennifer A. Flegg a, and Mark B. Flegg e

aThe School of Mathematics and Statistics, The University of Melbourne, Parkville, VIC, Australia
bThe School of Mathematics and Statistics, The University of Sydney, Camperdown, NSW, Australia
cPandemic Sciences Institute, University of Oxford, Oxford, United Kingdom
dMelbourne School of Population and Global Health, The University of Melbourne, Parkville, Vic, Australia
eSchool of Mathematics, Monash University, Clayton, VIC, Australia

### SI1 Jump-Switch-Flow: implementation details

To draw exact samples from the JSF process requires solving the differential equations for the flowing variables V⃗ F. For
nonlinearsystemsthesedifferentialequationsareusuallyintractable,sotheyarenumericallyintegrated. Herewedescribe
an algorithm for approximately sampling trajectories, assuming we have a numerical solver for the differential equations
(whenviewedasaninitialvalueproblem(IVP)),toapproximatethesolutions.

### SI1.1 Jump-clock

We implement the JSF algorithm with a slightly different jump clock as defined by J in Section . In particular, equate
k
u =CDF(t ;k) but do not take the log of this expression before defining J in Equation (11). As a result, in our codes
k k k
weconsiderthejumpclockJ˜:
k
(cid:18) (cid:26) (cid:90) t (cid:27)(cid:19)
J˜(t)=u − 1−exp − λ (V⃗(s))ds , (SI1)
k k k
t0
where u
k
∼ Unif(0,1) and the time of the previous jump event t0. Computing the times for the jump events follows a
similar process as above. We compute the jump clock on the regular ODE mesh used to solve V⃗ F in Equation (6). From
Equation(SI1)wecanwriteJ˜(t+∆t)intermsofJ˜(t)andanintegralofthereactionrate:
k k
(cid:18) (cid:26) (cid:90) t+∆t (cid:27) (cid:19)(cid:16) (cid:17)
J˜(t+∆t)=J˜(t)+ exp − λ (V⃗(s))ds −1 J˜(t)+1−u . (SI2)
k k k k k
t
For steps where J˜(t+∆t)>0 we can do a single step of this process to get the updated jump clock values. However, if
k
J˜(t+∆t)<0ajumphasoccurredatsometimet+∆τ ∈(t,t+∆t),andweneedtosolveJ˜(t+∆τ)=0tofindwhen
k k
the jump occurred. Therefore, we require a method to find ∆τ, where 0<∆τ <∆t. To do this, we start by letting the
righthandsideofEquation(SI2)equalzeroandrearrangetoget:
(cid:90) t+∆τ (cid:40) J˜(t)+1−u (cid:41)
λ (V⃗(s))ds=ln k k . (SI3)
t k 1−u k
Ifλ isapositiveconstantthen:
k
1 (cid:40) J˜(t)+1−u (cid:41)
∆τ = ln k k . (SI4)
λ 1−u
k k
If λ
k
is not constant, we approximate λ
k
, which we call λ(cid:98)k , using the integration of V⃗(t), as per Equation (6), since we
knowV⃗(t)andV⃗(t+∆t). Therefore,wealsoknowλ
k
attandt+∆t. Wethenwriteλ(cid:98)k ,att+∆τ betweentimestimest
andt+∆tvialinearinterpolation:
(cid:18) ∆τ(cid:19) ∆τ
λ(cid:98)k (t+∆τ)≈ 1−
∆t
λ
k
(V⃗(t))+
∆t
λ
k
(V⃗(t+∆t)). (SI5)
*Theseauthorscontributedequallytothiswork
16

<!-- Page 17 -->

We can now substitute this approximation into Equation (SI3), solve it, and rearrange for ∆τ. This gives a quadratic in
∆τ withthefollowingsolution:
(cid:114)
(cid:16) (cid:17)2
∆tλ(cid:98)k (t) +2α∆t∆λ
k
−∆tλ(cid:98)k (t)
∆τ = , (SI6)
∆λ
k
wherewehaveintroducedtheshorthand∆λ =λ (V⃗(t+∆t))−λ (V⃗(t)).
k k k

### SI1.2 Pseudocode details

AswithatypicalIVP,werequirethefollowingdata:
• theinitialconditionofthesystem,V⃗(0);
• thefinaltimeTmax>0;
• thestoichiometricReactant,η−,andProduct,η+,matrices,fromwhichwederivetheExchangematrix,η=η+−η−;
• asetoftheassociatedpropensitiesofthereactions,R;
• atimestepsizeforthenumericalintegrator,∆t;
• avectorofswitchingthresholds,Ω;
TosampletheJump-Switch-Flowprocess,wehaveidentifiedbothanexact sampler,thatsamplestheprocessexactly,and
anoperator-splitting sampler,thatusessomesimplifyingapproximationsthatmakessamplingsubstantiallyfaster.

### Exact Jump-Switch-Flow sampler

Here, we describe an exact algorithm for sampling trajectories from Jump-Switch-Flow. The algorithm to sample exactly
fromJump-Switch-FlowisgiveninAlgorithmSI1. First,initialisethejumpclocks(line3). Oneachiterationthroughthe
ODEloop,wefirstpartitionthereactionsbasedoninclusioninS (line6). WeusetheIVPsolvertocompute∆V⃗ F(t)based
on the flowing reactions (line 7). For each step of the ODE loop, we update the jump clocks (line 9). On lines 10–12, we
determineifajumpeventhasoccurredbasedonthesignofthetheJump-clock. Ifajumpeventhasoccurred,computethe
corresponding event time. On line 13 we then rewind the state (and jump clocks) to when the jump occurred. Resample
the appropriate jump clock (line 14), and update the state to account for the jump (line 15). Repeat until the time has
reachedthemaximumdesiredtime.
Algorithm SI1 An algorithmic description of the Exact Jump-Switch-Flow sampler.
Require: V⃗(0), ∆t>0 and T >0
max
1: Initialise model state
2: t←0
3: Initialise jump clocks u i ∼Unif(0,1) for i=1,...,N
4: (▷ Start ODE loop)
5: while t<T max do
6: Compute Jumping reactions S(t)
7: Compute flow event, ∆V⃗ F (t)
8: (▷ Perform jump loop for ODE mesh step)
9: Update jump clocks, J˜ k , to t+∆t (▷ As per Equation (14))
10: if any J˜ k ≤0 (▷ Reaction Occurred) then
11: Identify first fired Reaction, j
12: Compute time of jump event, ∆τ (▷ As per Equation (16))
13: Reverse jump clocks to time t+∆τ
14: Resample u j ∼Unif(0,1)
15: Update both: V⃗ J (t+∆τ)=V⃗ J (t)+η j and V⃗ F (t+∆τ)=V⃗ F (t)+∆τ∆V⃗ F (t)+η j
16: t←t+∆τ
17: else if J˜ k >0,∀k then
18: Update: V⃗ F (t+∆t)=V⃗ F (t)+∆t∆V⃗ F (t)
19: t←t+∆t
20: end if
21: end while
17

<!-- Page 18 -->


### Operator Splitting Jump-Switch-Flow sampler

Here, we describe the algorithm for the operator-splitting algorithm, for sampling trajectories from Jump-Switch-Flow,
whichutilisessomesimplifyingapproximationstoimprovesamplingperformance.
The Operator Splitting Jump-Switch-Flow sampler is described in Algorithm SI2. Unlike the Exact JSF sampler, when a
jumpeventoccurs,wecontinuetointegratethesystemwiththesameflowevent,∆V⃗ F(t),insteadofresamplingitasbefore.
This,inturn,ensuresthattheODEisnotcontinuallybeingresampled. Whilethisaddscomplexityattheimplementation
stage,significantcomputationaltimesavingisachieved.
WefirstinitialisetheJump-Switch-Flowprocessbyinitialisingallthejumpclocks(line3). Oneachiterationthroughthe
ODEloop,wefirstpartitionthereactionsbasedoninclusioninS (line6). WeusetheIVPsolvertocompute∆V⃗ F(t)based
on the flowing reactions (line 7). We now iterate through this current time-step, ∆t, checking if any jump events occur
(lines10–24),namedthejumploop. First,wetrackhowmuch“relativetime”(δt)passesthroughthisjumploop(line9).
Wethenupdatethejumpclockstotheendofthejumploop,accountingforanyrelativetimethathasoccurred(line11).
As with the Exact JSF sampler, on lines 12 – 14, we determine if a jump event has occurred using the Jump-clock. This
gives us which Reaction has occurred, and at what time, t+∆τ. On line 15 we then reverse the system to the time the
jump event occurs, noting that we must reverse the excess between when the jump event occurred and the remainder of
thetime-step. Wethenresampletheassociatedjumpclockthatjustfired(line16),andupdatethewholestate(i.e. both
flowingandJumpingvariables)tothecurrenttime(line17). Weupdatethecurrenttimetotimet+∆τ (line18)andtrack
therelativetimeinthejumploop(line19). Wethencontinuethroughthejumplook. Ifnojumpeventshaveoccurred,we
leavetheloop(line21). Wethensimplyupdatethewholestateaccordingtothefloweventcalculated,accountingforany
timespentinsidethejumploop(line24).
Algorithm SI2 An algorithmic description of the Operator Splitting Jump-Switch-Flow sampler .
Require: V⃗(0), ∆t>0 and T >0
max
1: Initialise model state
2: t←0
3: Initialise jump clocks u i ∼Unif(0,1) for i=1,...,N
4: (▷ Start ODE loop)
5: while t<T max do
6: Compute jumping reactions S(t)
7: Compute flow event, ∆V⃗ F (t)
8: (▷ Perform jump loop for ODE mesh step)
9: Set δt←0
10: while ∆t>δt do
11: Update jump clocks, J˜ k , to t+(∆t−δt)
12: if any J˜ k ≤0 (▷ Reaction Occurred) then
13: Identify first fired Reaction, j
14: Compute time of jump event, t+∆τ
15: Reverse jump clocks to time t+∆τ
16: Resample u j ∼Unif(0,1)
17: Update both: V⃗ J (t+∆τ)=V⃗ J (t)+η j and V⃗ F (t+∆τ)=V⃗ F (t)+∆τ∆V⃗ F (t)+η j
18: t←t+∆τ
19: δt←δt+∆τ
20: else if J˜ k >0,∀k then
21: Leave while loop
22: end if
23: end while
24: Update: V⃗ F (t+(∆t−δt))=V⃗ F (t)+(∆t−δt)∆V⃗ F (t)
25: t←t+(∆t−δt)
26: end while

### SI2 Simulation Study: Birth-death processes

Fundamentally, one can conceptualise any compartmental model as a collection of interacting birth-death processes. For
this reason, we will consider two very simple such processes: 1) a birth dominated birth-death process, and 2) a death
dominated birth-death process. In this section, we will perform a simulation study to highlight the advantages of our
Jump-Switch-Flow method, and compare the results to the gold standard, Doob-Gillespie Exact method, and the highly
computationallyefficientTau-hybridmethod,whichisprovidedbyGillesPy2,writteninbothC++andPython.
Theexactmodelwewillutiliseisasinglespecies,X,experiencingbirthwithrateα,whichresultsinX→2X,anddeath
withrateβ,whichresultsinX→∅.
18

<!-- Page 19 -->


### A birth dominated birth-death process

For the birth dominated process, we require α > β. Therefore, we specify α = 1, and β = 0.5. We also choose the
initial species population X(0)=1, and a simulation time of t=20. The quantities of interest to test the accuracy and
efficiency of the methods are (i) the CPU time for a particular simulation instance, (ii) the simulation time required to
reachaparticularvalue,X =200,and(iii)theaccuracyofthemethodtoexperienceinitialpopulationextinction. Figure
SI1 shows results for each of the three quantities of interest for the Tau-hybrid method (red), Doo-Gillespie (yellow) and
threedifferentJump-Switch-Flowexamples(purple)withvaryingswitchingthresholdsofΩ=101,Ω=102,andΩ=103,
respectively. Here,1000uniquetrajectoriesareconsideredforeachmethod.
100
101
102
Tau-Hybr T
i
a
d
u
:
-

## C


## H

+
y
+
br J
i

## S

d

## F

:
:
P yt
=
ho 1

## J

n

## S

0

## F:

1
=
1

## Js

0

## F:

2
=
1

## D

0
oo
3
b-Gillespie
)s(
emiT

## Upc

20
18
16
14
12
10
8
6
Tau-Hybr T
id
a
:
u

## C


## -H

+
y
+
bri J
d

## S

:

## F :

P yt
=
ho 1

## J

n

## S

0

## F:

1
=
1

## Js

0

## F:

2
=
1

## D

0
oo
3
b-Gillespie
002
=
X hcaer
ot
emiT
1.0
0.8
0.6
0.4
0.2
0.0
Tau-Hybrid T
:
a u

## C

-
+

## H

+
ybrid JS
:

## F


## P

:
y th
=
on 10

## Jsf

1
: =
10

## Jsf

2
: =
10
Do
3
ob-Gillespie
ytilibaborP
noitcnitxE
Figure SI1: Summary statistics for the birth dominated birth-death process for the Tau-hybrid (red) JSF for various
switching thresholds, Ω, (purple) and the Doob-Gillespie (yellow) methods. Left: CPU time required. We observe
that as Ω increases, the computational time increases, but remains the computationally least expensive. Middle:
DistributionsintimetoreachX =200. WeobservethatJSFresultsincomparabledistributionstotheexactprocess,
withdiminishingreturnsforΩ>102. Right: Extinctionprobability. Weobservethatallpointestimatesarecomparable
to that of the exact method.
Considering the CPU time, we can observe as we increase the switching threshold, JSF requires more CPU time, since
more of the simulation is in a discrete, Jumping regime. We also observe that the CPU time is, at worst, around two
ordersofmagnitudeless,comparedtothatofDoob-Gillespie. Incomparison,weobservethattheC++implementationof
Tau-hybrid method requires at best three times the computational time to simulate the equivalent process as JSF, while
thePythonimplementationisatleastoneorderofmagnitudeslower,indicatingthatJSFismuchmoreefficient. Toassess
the accuracy of each method, we now compare the (simulation) time for the species to reach 200. Here, both Tau-hybrid
and JSF with switching thresholds of Ω=102, and Ω=103 result in distributions and median value comparable to that
of Doob-Gillespie. The only exception is that of JSF with a switching threshold of Ω = 101. Lastly, we observe that all
methodsresultinaninitialextinctionprobabilitycomparabletothatofDoob-Gillespie.
These results suggest that JSF is capable of recovering the key quantities of the exact stochastic method, while being
computationallycheaperthancurrenthybridmethodsandtheexactmethod,forthebirthdominatedbirth-deathprocess.

### A death dominated birth-death process

For the birth dominated process, we require α < β. Therefore, we specify α = 0.5, and β = 1. We choose the initial
species population X(0)=100, and a simulation time of t=30. As before, the quantities of interest to test the accuracy
and efficiency of the methods are (i) the CPU time for a particular simulation instance, (ii) the simulation time required
to reach a particular value, X =50, and (iii) the simulation time require for the species to go extinct. Figure SI2 shows
resultsforeachofthethreequantitiesofinterestfortheTau-hybridmethod(red),Doo-Gillespie(yellow)andthreedifferent
Jump-Switch-Flow examples (purple) with varying switching thresholds of Ω=101, Ω=102, and Ω=103, respectively.
Again, 1000 unique trajectories are considered for each method. Unlike in the previous example, here we observe that all
JSFexamplesrequiremoreCPUtimetocompletetheequivalentcomputation,despitethisbeingadecayingdeathprocess.
However,westillobservethatallJSFmethodsrequirelessCPUtimewhencomparedtotheC++implementationofthe
Tau-hybridmethod,thistimeconsumingatleast1.5timeslesscomputationtime,andstillatleastoneorderofmagnitude
quickerwhencomparedtothePythonimplementation. WealsonotethatJSFrequiresatmosthalfthecomputationaltime
ofthatoftheexactDoob-Gillespiemethod. WenowconsiderthetimeforthespeciestoreachapopulationofsizeX=50.
Inthisexample, weseethatJSFwithΩ=101 doesnotcapturethedistributionoftheexactmethod, butonlyreportsa
single value. This is due to trajectories from this example all being deterministic at this value. If we consider JSF with
Ω=102,weseethatwhilethemedianiscomparabletotheexactmethod,thedistributionisnotasbroad. Thisisbecause
themethodonlybecomesstochasticatX=100,resultinginvarianceinthetrajectorypriortothisvaluebeinglost. Aswe
increasetheswitchingthresholdtoΩ=103,weobservethatdistributionintheTimetoreachX=50becomecomparable
tothatoftheeexactmethod. Thisprovidesaclearguideforhowtheswitchingthresholdmaybechosen,givensomeprior
knowledge of the system. Lastly, we observe that extinction time for the JSF with Ω = 102 and Ω = 103 resulting in a
19

<!-- Page 20 -->

101
102
Tau-Hybr T
id
a
:
u

## C


## -H

+
y
+
br

## J

i

## S

d

## F

:
:
P yt
=
ho
1

## J

n

## S

0

## F:

1
=
1

## Js

0

## F:

2
=
1

## D

0
oo
3
b-Gillespie
)s(
emiT

## Upc

7.5
7.0
6.5
6.0
5.5
5.0
Tau-Hybri T
d
a
:
u

## C


## -H

+
y
+
bri

## J

d

## S

:

## F


## P

:
yth
=
o
1
n

## Js

0

## F

1
:
=
1

## J

0

## Sf

2
:
=
1

## D

0
oo
3
b-Gillespie
05
=

## X

hcaer
ot
emiT
27.5
25.0
22.5
20.0
17.5
15.0
12.5
10.0
7.5
Tau-Hybri T
d
a
:
u

## C


## -H

+
y
+
bri

## J

d

## S

:

## F


## P

:
yth
=
o
1
n

## Js

0

## F

1
:
=
1

## J

0

## Sf

2
:
=
1

## D

0
oo
3
b-Gillespie
noitcnitxe
ot emiT
Figure SI2: Summary statistics for the death dominated birth-death process for the Tau-hybrid (red) JSF for various
switchingthresholds,Ω,(purple)andtheDoob-Gillespie(yellow)methods. Left: CPUtimerequired. Weagainobserve
that as Ω increases, the computational time increases, but still remains the computationally least expensive. Middle:
DistributionsintimetoreachX =50. WeobservethataswitchingthresholdofΩ=103 isrequiredforJSFtoresult
in comparable distributions to the exact process, Right: Distribution in the time to extinction. We observe that for
Ω>101, JSf results in comparable distributions to that of the exact method.
comparabledistributiontothatoftheDoob-Gillespiemethod. Again,wealsoobservethatJSFwithΩ=101 resultsina
truncateddistributiontothatoftheexactmethod.
TheseresultsalsosuggestthatJSFiscapableofrecoveringthekeyquantitiesoftheexactstochasticmethod,whilebeing
computationallycheaperthancurrenthybridmethods,forthedeathdominatedbirth-deathprocess. Throughthisexample,
wealsoshowhowJSFmayexhibitsensitivityinthevalueoftheswitchingthresholdchosen,andhowtocircumventthese
sensitivities.

### SI3 Simulation study: Multiple time-scales in autocatalysis

ToemphasisetheutilityandaccuracyofourJump-Switch-Flowmethod,wewillconsiderasimpleautocatalysisexample,
withmultipletime-scales. Considertwospecies,X,andY,whichreacttogetherviathefollowingreactions: X+Y →2X+Y,
with rate α, X → 2X, with rate β, X → ∅, with rate γ, and Y → ∅ with rate δ. To demonstrate the ability of JSF to
simulatethetrajectorieswithmultipletime-scales,butimportantly,simulatethemaccurately,wechoosethefollowingrate
parameters:
1. amoderategrowthrateofX: β=10,
2. alargedeathrateofY,toensurewecannotassumeaconstantY: δ=100,
3. alargedeathrateofX,meaningX quicklyvanishes: γ=50,
4. andlastlyasmallautocatalysisrate,resultinginX varyingdrasticallyinscale: α=1.
Despitebeingarelativelysimplemodel,withananalyticdeterministicdescription,simulatingstochastictrajectoriesrequires
carefulconsiderationofthepartitioningbetweenthestochasticreactionstoensureanaccuraterepresentation,asthereare
reactionsthatareoccurringamultipledifferenttimescales. Forexample,autocatalysisoccursinitiallyrelativelyfrequently,
duetothelargenumberofspeciesY,despitethesmallrateα. However,followingtherapiddeclineofY,X willexperience
moderate decay. Therefore, we expect to observe two different timescales in the species X: a rapid increase, followed by
gradualdecline.
WeassigntheinitialspeciessizesX(0)=10,andY(0)=102,andsample1000trajectoriesusingtheexactDoob-Gillesie
method,GillesPy2’sC++hybridmethod(Tau-hybrid)andJSFwithaswitchingthresholdofΩ=102. FigureSI3shows
the1000trajectoriesforTau-hybrid,JSF(withΩ=102),andDoob-Gillespie. WealsopresenttheanalyticODEsolutions
(dashedblack)andthemedianvalueatapoint(solidblack).
20

<!-- Page 21 -->

105
104
103
102
101
100
0.00 0.05 0.10 0.15 0.20 0.25

### Time


### X seicepS

Tau-hybrid
105
104
103
102
101
100
0.00 0.05 0.10 0.15 0.20 0.25

### Time

X seicepS

## Jsf: =103

105
104
103
102
101
100
0.00 0.05 0.10 0.15 0.20 0.25

### Time


### X seicepS

Doob-Gillespie
103
102
101
100
0.00 0.05 0.10 0.15 0.20 0.25
Time

## Y

seicepS
Tau-hybrid
103
102
101
100
0.00 0.05 0.10 0.15 0.20 0.25
Time

## Y

seicepS

## Jsf: =103

103
102
101
100
0.00 0.05 0.10 0.15 0.20 0.25
Time

## Y

seicepS

### Doob-Gillespie

FigureSI3:1000trajectoriesforthemultiscaleautocatalystexamplefortheTau-hybridmethod(left),theJSFmethod
(middle) and the exact Doob-Gillespie method (right). Top shows species X, and bottom shows species Y. We also
show the median species value (solid black line) and the analytic ODE solution (dashed black line). We see that the
mediantrajectoryofTau-hybridislessthantheanalyticsolution,whilebothDoob-GillespieandJSFmatchtheanalytic
solution.
Here, we can see that all Y species solutions match the analytic solution, since species Y undergoes constant decay only.
However,weclearlyseethat,whilethemediantrajectoriesofJSFandDoob-Gillespiematchthatoftheanalyticdescription,
the Tau-hybrid method median is less than the analytic solution. We can further quantify these discrepancies by looking
at the distributions of the time for species X to reach a particular value, the distributions of the maximum X value, and
also the relative point error between the median of the particular approach, and the analytic solution. We present these
quantitiesinFigureSI4.
0.24
0.22
0.20
0.18
0.16
Tau-Hybrid JSF: =103 Doob-Gillespie
kaep
gniwollof
,05
=

## X

hcaer
ot
emiT
140000
120000
100000
80000
60000
40000
20000
0
Tau-Hybrid JSF: =103 Doob-Gillespie
eulaV

## X

mumixaM
100
101
102
103
104
0.00 0.05 0.10 0.15 0.20 0.25 0.30

### Time

citylanA
ot
rorrE
evitaleR
Tau-hybrid

## Jsf: =103


## Ssa

Figure SI4: Summary statistics for the multiscale autocatalyst example for the Tau-hybrid (red), JSF with Ω = 103
(purple) and Doob-Gillespie (yellow). Left: time to reach X =50 following initial peak. We see that the distributions
ofDoob-GillespieandJSFarecomparable,whiletau-hybridisskeweddownwardwithadifferentmedianvalue. Middle:
MaximumX value. Again,weobserveJSFandDoob-Gillespieresultinginmatchingdistributions,whileTau-hybridis
skewed downwards. Right: relative error to analytic solution. JSF and Doob-Gillespie display similarly small error, an
order of magnitude less than Tau-hybrid.
FigureSI4showsthedistributionsfortimetoreachX=50followingthepeak,whereweseethatJSFandDoob-Gillespie
produce comparable results. However we also observe that the Tau-hybrid method under-performs, and results in earlier
hitting times. We observe a similar trend in in the maximum X value, with Tau-hybrid producing a skewed downwards
distribution, and JSF and Doob-Gillespie producing comparable distributions. Lastly, the relative point error of JSF and
Doob-Gillespiearecomparable,withTau-hybridanorderofmagnitudegreater.
Fromtheresultspresentedhere,weseethatourJump-Switch-Flowmethodiscapableofproducinghighlyaccuratehybrid
trajectories, even with highly multiscale systems, as the one presented here. We also observe the summary statistics
21

<!-- Page 22 -->

produced by JSF being comparable to those of the exact Doob-Gillespie method, and outperforming the highly efficient
andsophisticatedTau-hybridmethod.

### SI4 Simulation study: SIRS with demography

We first present how the SIRS model with demography can be expressed with the Jump-Switch-Flow method. For the
Jump-Switch-Flowmethodtobeausefulmethod,itmustreproducebehaviourthatisrepresentativeoftheexactprocess
(i.e. the CTMC). That is, given some summary statistic, distributions produced via sampling the JSF process should be
comparabletothoseobtainedviasamplingtheCTMC.Moreover,werequirethatitdoessowithacceptablecomputational
efficiency. Weshow,throughsimulationexperiments,howtheJump-Switch-FlowmethodcomparestotheDoob-Gillespie
method (Gillespie, 1976) for accuracy, and how our approach can exhibit sensitivity with respect to model inputs. We
presenthowourJump-Switch-FlowmethodcomparestoboththeDoob-GillespieandTau-Leapingmethods.
FigureSI5ashowsthemainreactionsoftheSIRSmodelwithdemography: individualsfallintooneofthreecompartments:
susceptible (S), infectious (I) and recovered (R). Here, arrows represent how individuals move and progress through
compartments. Specifically, individuals are born into the susceptible compartment. Births occur from individuals in
the S, I and R compartments, and therefore depend explicitly on the populations (discrete or continuous) in each of
these compartments. Individuals can die within each of the compartments. Finally, individuals may progress through
compartments via susceptible individuals experiencing infection, infected individuals experiencing recovery, and recovered
individualsexperiencingwaningimmunity.
InordertorepresenttheSIRSmodelwithdemographyasaJump-Switch-Flowprocess,weneedtoassociaterates,reactants
andproductstoeachofthearrows(seeFigureSI5b). Notethatthebirthsarrowissplitintothreearrowsdependingupon
the compartment of the parent. Moreover, one of the key assumptions of any SIR-type model is that the population is
homogeneously mixed, which enables us to describe how individuals interact with one another. This enables us to say
thatsusceptibleindividualsinteractwithinfectiousindividualswitharateinverselyproportionaltothewholepopulation.
However, there are likewise infectious individuals interacting with other infectious individuals, and also with recovered
individuals. However, these last two interactions (as shown in blue in Figure SI5b) do not result in any exchange of
individualsbetweencompartments.
Figure SI5c shows the SIRS model with demography as a Jump-Switch-Flow process. In this example figure, the S
and R compartments are continuous (flowing), while the I compartment is discrete (jumping). To decide which of the
arrows/reactions are jumping, i.e. in S, and which are flowing, i.e. in S′, we consider the reactants and products of the
arrows: ifanarrowhasanydiscretereactantorproduct,thenthatarrowisalsojumping,otherwiseitisflowing. TableSI1
showsthereactantsandproductsoftheSIRSmodelwithdemography.
(a) (b) (c)
Figure SI5: (a) The labelled compartmental SIRS model with demography. (b) The SIRS model with demography
wherethearrowsdescribetheinteractionsbetweenthereactantsandproducts. Here,bluearrowsdonotresultinany
flowthroughthesystem,andcanbeignored. (c)ThemodelasaJump-Switch-Flowsystemwithcontinuous(flowing)
SandR(black),anddiscrete(jumping)I(purple). SinceIisjumping,thereactionsinvolvingIaremodelledasdiscrete,
jumping reactions.
Fortheremainderofthissection,wesupposeparametervaluesfortheSIRSmodelwithdemographythatwouldbetypical
foranewlyintroduced,yearlyseasonalcommunicabledisease,aspresentedinTableSI2. Withtheseparametervalues,on
average,weexpectaninfectedindividualtoinfect2otherpeopleperweek(duringtheinitialoutbreak),andbeinfectious
for1week,withimmunitytothediseaselastingfor1year. Forthepopulationturnover,weassumeindividualslivefor,on
average,85years. Initiallytherearetwoinfectiousindividuals(i.e. I(0)=2),norecoveredindividuals(i.e. R(0)=0),and
theremainderofthepopulationissusceptible(i.e. S(0)=N(0)−I(0)).
As well as being computationally efficient, our Jump-Switch-Flow method is capable of capturing the inherent stochastic
natureofthesampledprocess. FortheSIRSmodelwithdemography,thisisrealisedbythreekeydifferentscenarios:

## Extinction: alloftheindividualsrecoverbeforethediseasemanagestospreadsignificantlythroughoutthepopulation

(seeFigureSI6aandSI6d);

## Fade-out: thediseasespreadsthroughoutthepopulation,howeveritfades-outinthetroughproceedingthefirstwave

(seeFigureSI6bandSI6e);

## Endemic: thediseasepersistsindefinitelywithinthepopulation(seeFigureSI6candSI6f).

22

<!-- Page 23 -->


### Reactants, η− Products, η+ η

Reaction Rate S I R S I R S I R

### Birth by S κ 1 · · 2 · · 1 · ·

∗Birth by I κ · 1 · 1 1 · 1 · ·

### Birth by R κ · · 1 1 · 1 1 · ·

∗Infection of S β /N 1 1 · · 2 · -1 1 ·

## S

∗Infection of I β /N · 2 · · 2 · · · ·

## I

∗Infection of R β /N · 1 1 · 1 1 · · ·

## R

∗Recovery of I γ · 1 · · · 1 · -1 1
Waning of R ω · · 1 1 · · 1 · -1

### Death of S µ 1 · · · · · -1 · ·

∗Death of I µ · 1 · · · · · -1 ·

### Death of R µ · · 1 · · · · · -1

Table SI1: The stoichiometric matrices for the SIRS model with demography. The (*) indicates reactions that are
jumpingwhenI isdiscreteandS andRarecontinuous. Therowswithbluecolouredentriesdonotaltertheexchange
through the system, and so need not be represented.

### Parameter β γ ω κ µ

Rate description Infection Recovery Immunity Waning Birth Death

### Value 2/7 1/7 1/365 1/(85×365) 1/(85×365)

Table SI2: Parameter values used for SIRS model with demography.
Extinction Fade-out Endemic
(a) (b) (c)
(d) (e) (f)
Figure SI6: PossiblesimulatedtrajectoriesofSIRSmodelwithdemographyforaninitialpopulationsizeN(0)=105,
from Doob-Gillespie (yellow) and Jump-Switch-Flow (purple, Ω = 103) methods: (a) two examples of extinction
trajectories of the infectious compartment, with associated S−I phase plane in (d); (b) two examples of fade-out
trajectories of the infectious compartment, with associated S −I phase plane in (e); (c) two examples of endemic
trajectories of the infectious compartment, with associated S−I phase plane in (f).
SI4.1 Simulation experiments: Comparing Jump-Switch-Flow and Doob-Gillespie
We compare our Jump-Switch-Flow method to the gold standard approach for simulating exact solutions to CTMCs, the
Doob-Gillespiemethod. To doso, we firstspecifiedan initialpopulationsize of N(0)=105, and aswitchingthreshold of
eachcompartmentofΩ=103. Wethengenerated5,000simulationsusingtheparametersinTableSI2.
Tocapturethedynamicsofthemodel,wetracktheinfectiouscompartmentasakeycompartmentofinterest. Indoingso,
we then obtain distributions for the peak number of infectious individuals and also the time for the infection to peak, for
the fade-out scenario. We also track the cumulative number of infected individuals after a certain amount of time for the
23

<!-- Page 24 -->

endemicscenario. TheseresultsarepresentedinFigureSI8.
Jump-Switch-Flow
-
1
0 50 100 150
Peakinfectiontime(days)
(a)
)
5
0
15 1
) #
3 0 (15
# 1 s n
( o
e10 it
v c10
it
c
e fn
e I
fn e
i k 5 v it 5
a a
e

## P

lu
m
0 u C 0
1 1
- -
(b) (c) (d) (e)
Doob-Gillespie
-
1
0 50 100 150
Peakinfectiontime(days)
(f)
)
5
0
15 1
) #
3 0 (15
# 1 s n
( o
e10 it
v c10
it
c
e fn
e I
fn e
i k 5 v it 5
a a
e

## P

lu
m
0 u C 0
1 1
- -
(g) (h) (i) (j)
Figure SI7: We compare the infectious compartment from realisations for Jump-Switch-Flow (b) and Doob-Gillespie
(g) solutions, for a population size of N(0) = 105. We use a switching threshold of Ω = 103. We also show the
distributions of the time to infectious peak ((a) and (f)), and infectious peak values ((c) and (h)). We compare the
cumulative infections over the simulations for Jump-Switch-Flow (d) and Doob-Gillespie (i) solutions and the final
distributions ((e) and (j)). Point averages are also presented as a solid line.
ComparingFiguresSI7aandSI7f,wecanimmediatelyobservethatthedistributionsfortimetopeakforJump-Switch-Flow
methodappearstoberepresentativeofthatfortheDoob-Gillespiemethod. Thisisbecausethedelayintheepidemictake
offatlowpopulationisfullycaptured withthissufficientlylargechoiceofswitchingthreshold, Ω=103, enablingthefull
stochasticeffectstobeaccuratelyrepresented.
However,ifwecomparethedistributionsforthepeaknumberofinfectiousindividuals(SI7candSI7h),wecanseethatthey
differ significantly, for this chosen switching threshold. This difference can be understood if we consider how the process
isbehaving. OncetheinfectiouscompartmentissufficientlylargefortheJump-Switch-Flowmethod,themethodswitches
from a stochastic representation to a deterministic representation. Therefore, once the infectious compartment becomes
deterministic, given that the susceptible population is also deterministic, its peak value is determined by the number of
both infectious and susceptible individuals at this time. Since the number of infectious people at this time will always be
thesame, I =Ω=103 people, anyvariationinpeakvalueisduetothenumberofsusceptibleindividuals, S, atthetime
ofswitching.
Ifthesummarystatisticweinsteadcompareisthedistributionofthecumulativenumberofinfectedindividualsafterfour
yearsofepidemiccirculation,weobservethat,evenforarelativelylowswitchingthreshold,theJump-Switch-Flowmethod
performswellcomparativelytotheDoob-Gillespiemethod,seeFiguresSI7eandSI7j. Wealsonotethatfortheseparameter
choices and switching threshold, the infectious compartment switches between jumping and flowing states multiple times,
yettheJump-Switch-FlowmethodproducesacumulativedistributioncomparabletothatofDoob-Gillespie. Thisindicates
thattheJump-Switch-Flowmethodisrobustforlongtermsimulations.
24

<!-- Page 25 -->

Thefinalsummarystatisticsweareinterestedinaretheprobabilitiesofextinction,fade-outandendemicscenarios. Table
SI3 shows the probability of each scenario computed from 5,000 simulated samples. Here, we see that both methods
produce comparatively similar results, which indicates that the Jump-Switch-Flow method is capable of capturing the
inherentstochasticityintheexactsimulationofthesystemviatheDoob-Gillespiemethod.

### Method Extinction Fade-out Endemic

Jump-Switch-Flow 0.2476±0.0120 0.4774±0.0138 0.2750±0.0124

### Doob-Gillespie 0.2520±0.0120 0.4668±0.0138 0.2812±0.0125

Table SI3: Probabilities (with associated 95% confidence interval) of scenario outcomes for Jump-Switch-Flow and
Doob-Gillespie, from 5,000 simulations.
We also compare the Jump-Switch-Flow and Doob-Gillespie methods where the switching threshold has been set to the
populationsize,resultinginnocompartmentsswitchingintotheflowingstate. TheseresultsarefurtherdiscussedinSI4.2,
whereweshowthetwomethodsareindistinguishable.
SI4.2 Simulation experiments: Comparing Jump-Switch-Flow (with no switching) and

### Doob-Gillespie

WecomparetheJump-Switch-FlowmethodtotheDoob-Gillespiemethod. Toimplementthelatter,wesettheswitching
threshold to be the total population size, to ensure no compartments switch into a flowing regime, and therefore all
compartmentsarecompletelystochastic. WecanthereforeinvestigatehowourJumpingprocesscomparestoexactsolutions
oftheContinuousTimeMarkovChains.
25

<!-- Page 26 -->

Jump-Switch-Flow
-
1
0 50 100 150
Peakinfectiontime(days)
(a)
)
5
0
15 1
) #
3 0 (15
# 1 s n
( o
e10 it
v c10
it
c
e fn
e I
fn e
i k 5 v it 5
a a
e

## P

lu
m
0 u C 0
1 1
- -
(b) (c) (d) (e)
Doob-Gillespie
-
1
0 50 100 150
Peakinfectiontime(days)
(f)
)
5
0
15 1
) #
3 0 (15
# 1 s n
( o
e10 it
v c10
it
c
e fn
e I
fn e
i k 5 v it 5
a a
e

## P

lu
m
0 u C 0
1 1
- -
(g) (h) (i) (j)
Figure SI8: We compare the infectious compartment from realisations for Jump-Switch-Flow (b) and Doob-Gillespie
(g) solutions, for a population size of N = 105. We use a switching threshold of Ω = 103. We also show the
0
distributions of the time to infectious peak ((a) and (f)), and infectious peak values ((c) and (h)). We compare the
cumulative infections over the simulations for Jump-Switch-Flow (d) and Doob-Gillespie (i) solutions and the final
distributions ((e) and (j)). Point averages are also presented as a solid line.
Using parameter values in Table 3 of the main text, we generated 5,000 simulations, tracking the same quantities of
interest. As with the case with compartment switching, the peak infection time distribution of JSF (Figure SI8a) and
Doob-Gillespie (Figure SI8f) are comparable. However, this time, as well as a similar median peak infective individuals,
thedistributionsofbothJSF(FigureSI8c)andDoob-Gillespie(FigureSI8h)arealsocomparable. Lastly,aswesawwith
compartment switching, the distributions of cumulative infections after four years are comparable for both JSF (Figure
SI8e)andDoob-Gillespie(FigureSI8j).
Table SI4 shows that the probabilities of scenario outcomes are also comparable for both Jump-Switch-Flow (with no
switching)andDoob-Gillespie.

### Method Extinction Fade-out Endemic

Jump-Switch-Flow 0.2512±0.0120 0.4700±0.0139 0.2788±0.0123

### Doob-Gillespie 0.2520±0.0120 0.4668±0.0139 0.2812±0.0125

Table SI4: Probabilities (with associated 95% confidence interval) of scenario outcomes for Jump-Switch-Flow (with
no switching) and Doob-Gillespie, from 5,000 simulations.
26

<!-- Page 27 -->

SI4.3 Simulation experiments: Sensitivity of Jump-Switch-Flow to switching threshold
Inthissection,wedemonstratehowtheaccuracyoftheJump-Switch-Flowmethodcanexhibitsensitivitywithrespectto
theswitchingthreshold(FigureSI9). InFigureSI9a,wecanseethatthedistributionofpeaknumberofinfectiveindividuals
forthefade-outscenarioishighlysensitivetotheswitchingthreshold. Forasmallswitchingthreshold(Ω=101),weseethat
thedistributionexhibitslowvariance,isrepresentativeofthedeterministicexpectation,andisnotcapturingthedistribution
obtainedwiththeDoob-Gillespiemethod. Astheswitchingthresholdisincreased,weseethatthedistributionofthepeak
numberofinfectiveindividualsincreasesinvariance. However,theJump-Switch-Flowmethodisnotrepresentativeofthe
Doob-Gillespie method until a large switching threshold (Ω = N(0) = 105), where all compartments are in the jumping
state.
(a) (b)
(c) (d)
Figure SI9: Summary statistics of interest to observe the sensitivity of the Jump-Switch-Flow method with respect
to the switching threshold. (a) Sensitivity to the distribution of peak number of infective individuals for the fade-out
scenario. (c) Sensitivity to the distribution of peak infection time for the fade-out scenario. (b) Sensitivity to the
distribution of the cumulative number of infected individuals after four years for the endemic scenario. (d) Sensitivity
tothe probabilityofeach scenario occurring. Ineach ofthe plots(a)-(c) grey topurple shadeddistributionsrepresent
resultsobtainedwiththeJump-Switch-FlowmethodwhilsttheyellowdistributionsarethegoldstandardDoob-Gillespie
algorithm (for which the placeholder ‘G’ is used to signify) which exhibit exact stochasticity but at the cost of high
computational requirements.
FigureSI9cpresentsthedistributionofpeakinfectiontimeforthefade-outscenarioforvariousswitchingthresholds,and
comparingtotheDoob-Gillespiemethod. Here,weseethattheJump-Switch-Flowmethodwitharelativelysmallswitching
threshold(Ω=102)iscapableofcapturingarepresentativedistributionoftheDoob-Gillespiemethod.
Similarly, Figure SI9b presents the distribution of the cumulative number of infected individuals after four years for the
endemic scenario. Here, we again see that the Jump-Switch-Flow method with a relatively small switching threshold
(Ω=103)isalsorepresentativeoftheDoob-Gillespiemethod.
Lastly,FigureSI9dshowstheprobabilityofeachscenariooccurring(extinction,fade-out,endemic). Here,weseethatthe
Jump-Switch-FlowmethodwithaswitchingthresholdofΩ≤101over-representstheendemicscenario. However,increasing
theswitchingthreshold,weobservethattheprobabilityofeachscenariooccurringquicklybecomesrepresentativeofthose
foundbytheDoob-Gillespiemethod.
SI4.4 Simulation experiments: Computational efficiency of Jump-Switch-Flow
We now present the computational efficiency of the Jump-Switch-Flow method, and compare it to the Doob-Gillespie
method and Tau-Leaping method (which is regarded as a computationally efficient, approximate, method), and the Tauhybridmethod,providedbyGillesPy2Matthewetal.,2023. WeimplementtwovariantsofTau-leapingwithafixedstepsize
of ∆τ =0.01 days, and ∆τ =0.1 days respectively, two variants of the C++ implementation of the Tau-hybrid method,
with time steps of size ∆t = 0.01 days and ∆t = 0.1 days respectively, one implementation of the Python Tau-hybrid
27

<!-- Page 28 -->

method, with time steps of size ∆t = 0.1 days, and the Jump-Switch-Flow method with a time step size of ∆t = 0.01
days.
Figure SI10a shows how the computational efficiency varies with the switching thresholds, Ω, for the SIRS model with
demographypresentedintheprevioussection,andcomparesittotheDoob-Gillespiemethod. Weseethatasweincrease
the switching threshold, the Jump-Switch-Flow method requires more computational time to simulate the scenario for
four years, but is always more efficient than the Doob-Gillespie method. This increased efficiency is because the Jump-
Switch-Flow method utilises the Next Reaction Method to compute the stochastic events, a method known to be more
computationallymoreefficientthanthedirect,firstreaction,Doob-Gillespiemethod.
102
101
100
101
102

## 0 1.0 2.0 3.0 4.0 5.0 G

log10( )
)sdnoces(
emit
nur

## Upc

102
101
100
101
102
102 103 104 105 106
Population size - log scale
(a)
elacs
gol
-
)sdnoces(
emit
nur

## Upc

Tau-Leaping: =0.01 Doob-Gillespie

### Tau-Leaping: =0.1 JSF: =101

Tau-Hybrid C++: t=0.01 JSF: =103
Tau-Hybrid C++: t=0.1 JSF: =105
Tau-Hybrid Python: t=0.1
(b)
Figure SI10: (a)TherunningtimetosimulatethescenarioforfouryearsforaninitialpopulationsizeofN(0)=105,
with varying switching threshold, Ω (grey to purple), compared with the Doob-Gillespie (‘G’) method (yellow). The
endemicsteadystatenumberofinfectiousindividuals(verticaldashedline),susceptibleindividuals(verticalsolidline),
andrecoveredindividuals(verticaldottedline)arepresented. (b)TherunningtimefortheJump-Switch-Flowmethod
for an appropriate threshold choice is approximately constant as the population size varies (for example Ω=103). If
a poor switching threshold is chosen, the running time begins to scale exponentially (for example Ω = 105). For the
Tau-Leaping method, the running time is constant, as we use fixed step size of ∆τ =0.01 (solid line) and ∆τ =0.1
(dashed line). We also present the Tau-hybrid method, in both Python and C++, with various different time meshes,
C++withafinemesh(δt=0.01,blacksolidline)andacorsemesh(δt=0.1,blackdashedline),andPythonwitha
corse mesh (δt=0.1, grey dotted line).
To observe how the computational efficiency of our Jump-Switch-Flow method varies with the total (population) size of
the system, we consider three switching thresholds: Ω = 101 (dotted purple), Ω = 103 (dashed purple), and Ω = 105
(solid purple). Figure SI10b compares the Jump-Switch-Flow method (purple) to the Doob-Gillespie method (yellow),
to the computationally more efficient approximation Tau-Leaping method (∆τ = 0.01, dashed red, and ∆τ = 0.1, solid
red), and to the Tau-hybrid method (∆t = 0.01 solid black, and ∆t = 0.1 dashed black) provided by GillesPy2, noting
the log-log scale. We simulate the SIRS system described above, for a total time of 4×365 days. We can see that the
computationalefficiencyoftheDoob-Gillespiemethodscalesexponentiallywithsystemsize,asexpected. TheTau-Leaping
method initially has constant computational time scaling. In contrast, our Jump-Switch-Flow method is constant in time
up to an initial system size of N(0) = 105, after which it begins to slowly decrease (for Ω = 101 and Ω = 103). This
decreaseiscausedbymoreofthescenariobeingsimulatedintheflowingstate,asthesystembecomeshighlydeterministic
withalargerpopulation. WealsoobserveourJump-Switch-FlowmethodincreasingexponentiallybetweenN(0)=104,for
the largest switching threshold of Ω = 105 (solid purple). We observe our Jump-Switch-Flow method performing better,
in comparison to Doob-Gillespie exact method, as we use the Next Reaction Method to sample the Jump times. This
isdespiteourimplementationbeingrequiredtoperformextracomputationtochecktheregimeoftheJump-Switch-Flow
process,andimplementanyrelevantregimechanges(eventhoughtheyarenotrequiredinthisparticularinstance). Wealso
observethatforlarge,realisticpopulationsizes(i.e. N(0)≥105),theTau-hybridmethodwiththecorsetimemesh(black
dashedline)performsatbestcomparableto,orworsethantheJump-Switch-Flowmethod,ifasuitableΩischosen(such
asΩ=103. Moreover,aswespecifyafinertimemesh(solidblackline)weobservethattheTau-hybridmethodperforms
worse across all population sizes. We anticipate this is due to the Tau-hybrid method utilising an arbitrary ODE solver,
an adaptive ∆τ that is calculated at each step, and also due to the dynamic switching behaviour between stochastic and
deterministicregimesthatrequiresextracomputationofthepropensitiestodetermineifaswitchingeventshouldoccur.
SI4.5 Simulation experiments: Inference with simulated data, parameter estimates
TotesthowtheJump-Switch-Flowmethodbehaveswhenusedtoperformparameterestimation,wefirstgeneratedsynthetic
dataofaknownSIRSmodewithdemography. Wesimulatedatafor400daysusingtheparametervaluesgiveninFigure
2C, with the Doob-Gillespie algorithm, and select a trajectory which experiences epidemic fade-out (at day 250), and an
initial condition of two infected individuals (I(0) = 2), no recovered individuals (R(0) = 0), and a total population of
28

<!-- Page 29 -->

N(0)=105 individuals. Wetrackthenumberofinfectiousindividualswithinthepopulationeachday,anduseatruncated
binomialdistributiontoaddnoiseintothedataset,reflectingarealisticmeasurementprocess. WethencoupleourJump-
Switch-Flow method, using a switching threshold of Ω = 103, with the open-source particle filter package pypfilt (Moss,
2024),using2,000particles. Wefirstfixthedemographicparameterstoκ=µ=1/(85×365)(sincetheseareassumedto
bestandardwithinagivenpopulation). Weperformtheinferenceonthedatasetforthefirst100daysoftheepidemicto
estimate β, γ and ω, and then use our parameter estimates to predict forward in time the possible trajectories based on
theobtainedpredictions. Usingthesepredictions,wealsoestimatetheprobabilityofepidemicfade-outoccurringattimes
t=100tot=400days.
Figure SI11 shows the posterior distributions of parameters. The dotted black lines show the true value used to produce
thesimulateddata,andthedashedredlinesindicatetheinitialboundsonthepriorestimates. Weseethatbothβ andγ
arewellestimated, withtheposteriorscenteredaroundthetruevalues. Howeverω notwellestimated. Thisisbecauseω
actsontheorderof1year,whilethewindowofdatausedtofittheparameterstothedatais100days(≈0.3years).
1 1 1
0 1 2 3 4 0 1 2 3 0 0.5 1 1.5 2 2.5
- . !
Figure SI11: Posterior distributions of parameters for the SIRS model with demography, obtained via a particle filter
with 2,000 particles, and the Jump-Switch-Flow sampler. The red dashed lines indicate the initial bounds on prior
samples. The vertical dotted black lines indicate the true value used to produce the simulated data.
SI5 Inference Study: Estimating TEIRV model parameters using a particle filter
We implemented the Refractory Cell Model described by the authors for the viral load data obtained from nasal swabs,
using our Jump-Switch-Flow method with a switching threshold on all compartments Ω = 102. We implemented this in
particlefilterpypfiltMoss,2024toestimatethemodelparameters,using6,000particlespersimulation. Inpreviousanalysis
Ke et al., 2022, the decay of virion was fixed at c=10 virions/day, and the eclipse of cells to become infectious as k=4
cells/day, leaving the remaining parameters to be estimated. Therefore, we similarly fix c = 10 virions/day and k = 4
cells/day. ThepriordistributionsusedfortheanalysiswiththeTEIRVmodelaregiveninTableSI5.

### SI5.1 Parameter Estimation and Viral Clearance Prediction

Figure9ofthemaintexthighlightshowtheestimatedviralloadscloselyresemblethedatacollectedfromthe6patients.
WealsoshowhowtheestimatedR0 valuesforthepatientsvary. TheseR0 estimatesareconsistentwiththeoriginalstudy
by Ke et al., 2022. However, understanding how the parameter estimates vary between patients assists in understanding
howthefittingprocessbehaves.
The posterior distributions for each of the 6 patient’s parameter estimates are provided in Figure SI12. These posterior
distributions are found by fitting a violin envelope from the 6,000 estimates obtained from the particle filtering process.
We also show the prior distributions, as red dashed lines, which show the lower and upper bounds for the uniform initial
guesses.
Wecanseethat,often,parametersρandΦarenotidentifiedhere,astheposteriordistributionscloselyresemblethepriors
(excludingpatient451152). Wealsoobservedthatforallpatients,β appearstobewellestimated. Theparameterπisalso
well estimated for patients 443108, 444332, 444391 and 451152, however patients 432192 and 445602 provide less insight.
Theparameterδ isverywellestimatedbyallpatients,excludingpatient451152. Lastly,theinitialviralloads,log
10

## (V0),

areallestimatedwell,andalsoestimatedtotakealargevalue.

### Parameter Prior

log (V ) Uniform(0,5)
e 0
c Fixed at 10.0
k Fixed at 4.0
β×107 Uniform(0,20)
Φ×105 Uniform(0,15)
ρ Uniform(0,1)
δ Uniform(1,10)
π Uniform(200,400)
Table SI5: The prior distributions used for the analysis with the TEIRV model.
29

<!-- Page 30 -->

2
9
1
2
3
4
1 1 1 1 1 1
0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2
- #10-8 ; : ) #10-5 / log
10

## (V

0
)
(a)
8
0
1
3
4
4
1 1 1 1 1 1
0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2
- #10-8 ; : ) #10-5 / log
10

## (V

0
)
(b)
2
3
3
4
4
4
1 1 1 1 1 1
0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2
- #10-8 ; : ) #10-5 / log
10

## (V

0
)
(c)
1
9
3
4
4
4
1 1 1 1 1 1
0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2
- #10-8 ; : ) #10-5 / log
10

## (V

0
)
(d)
2
0
6
5
4
4
1 1 1 1 1 1
0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2
- #10-8 ; : ) #10-5 / log
10

## (V

0
)
(e)
2
5
1
1
5
4
1 1 1 1 1 1
0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2
- #10-8 ; : ) #10-5 / log
10

## (V

0
)
(f)
FigureSI12:PosteriordistributionsofthemodelparametersandinitialviralloadforeachoftheselectedSARS-CoV-2
infections. The red dashed lines indicate the initial (uniform) bounds on prior samples.
30

## Tables

**Table (Page 19):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tau |  | - | Tau Hybrid: |  | - C | JSF Hybrid: + + |  | : P | JSF = 10 ython |  | : 1 | JSF = 10 |  | : 2 | Do = 10 |  |  |
|  | I1: th Ω i ions nis f th ng he ma id ni acy wit Gill resu ult ion do irth opu enc a pa ea itch 00 ple we idm hen the am ue. we odo he th e of |  |  | Sum esh cre int ing ex he imu nitu eth ple of e sw spie tin sug lly ina do atio of rtic hof Flo niq req till eth com exa le, Thi eet nly witc eex the |  |  | mar lds ses, me etu ct PU atio del d r men ch tchi T an gest hea ted ina X he lar the ex e t uire obs d,t pare tD es is at eco hing ct syst |  |  | y st Ω, the tor nsf et tim n is ss, qui atio met g t e o niti tha ert birt ed 0)= eth alu hre mp ajec mor rve ist dto ob- eth ue hil mes thr eth em. |  |  | tist (pu co ach orΩ od. e, w in om es a nis od, res ly e lex JS an h-d roc 10 ods , X qu es ( ori CP hat me the Gill atJ o t the toc sho od. Las |  |  | cs f ple pu X > e ca dis are be atle we old xcep inc F is urr ath ss, , an are =5 ntit pur s ar Ut all ons Pyt spie SF ajec me ast dto This ly, |  |  |


**Table (Page 19):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 19):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 20):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tau |  | - | Tau Hybrid: |  | - C | JSF Hybrid: + + |  | : P | JSF = 10 ython |  | : 1 | JSF = 10 |  | : 2 | Do = 10 |  |  |
|  | I2: thr in ons rab JS led dis ults ion ow es. mu sise iple α, the rs: od rge rge las eing nsid tha ela dec ecli th Gill traj lac |  |  | um esho rea int e di res stri rib also llyc how ati the tim X → raje rate dea dea lya are erat are gen ay. e. ini sPy cto )an |  |  | mar ds, es, me trib lts uti tion sug hea JSF n util -sca 2X tor gro hra hra sm ativ on occ mb The ial ’sC esf dth |  |  | st Ω,( he or tio n c nto tot est ert ma tu ya es. wi esw th eo eo lla lys fth rrin rof efor peci ++ rT me |  |  | tisti urp om ach s t mp tha hat hat an ex y: da ons h ra th ate Y, X, toc mpl pa a spe , w ssi hyb u-h dian |  |  | s f e)a uta X th rabl of fth JSF urre ibit Mu cur der te β ulti fX oe mea taly mo titio ulti ies ex es id bri val |  |  |


**Table (Page 20):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 20):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 21):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 21):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 21):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 21):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 21):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 21):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 21):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 21):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 21):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| T J S | au-hybrid SF: =10 SA | 3 |  |  |  |


**Table (Page 23):**

| Parameter | β | γ | ω | κ | µ |
|---|---|---|---|---|---|
| Rate description | Infection | Recovery | Immunity Waning | Birth | Death |
| Value | 2/7 | 1/7 | 1/365 | 1/(85×365) | 1/(85×365) |


**Table (Page 24):**

|  | 15 ) |  |  |  |
|---|---|---|---|---|
|  | 3 0 1 # ( e10 v it c e fn i 5 k a e P 0 1 - (c) Doob-Gillespie |  |  |  |
| - 1 0 50 100 150 Peakinfectiontime(days) (f) |  |  |  |  |
|  | 15 ) 3 |  |  |  |
|  |  |  |  |  |
|  | 0 1 # ( e10 v i |  |  |  |
|  | t c e fn i 5 k a e P 0 1 - (h) ment from realisatio 05. We use a switc and (f)), and infecti ump-Switch-Flow (d o presented as a soli elyobservethatthed Doob-Gillespiemeth fficientlylargechoice |  |  |  |


**Table (Page 24):**

| ) 5 0 1 # (15 s n o it c10 e fn I e v it 5 a lu m u C 0 1 - (e) |
|---|
| ) 5 0 1 # (15 s n o it c10 e |
| fn I e v it 5 a lu m u C 0 1 - (j) (b) and Doob-Gillesp 03. We also show t (h)). We compare t olutions and the fin kforJump-Switch-Flo ayintheepidemicta =103, enablingthef |


**Table (Page 24):**

|  |
|---|
|  |


**Table (Page 24):**

|  |
|---|
|  |


**Table (Page 25):**

| Method | Extinction | Fade-out | Endemic |
|---|---|---|---|
| Jump-Switch-Flow Doob-Gillespie | 0.2476±0.0120 0.2520±0.0120 | 0.4774±0.0138 0.4668±0.0138 | 0.2750±0.0124 0.2812±0.0125 |


**Table (Page 26):**

|  | 15 ) |  |  |  |
|---|---|---|---|---|
|  | 3 0 1 # ( e10 v it c e fn i 5 k a e P 0 1 - (c) Doob-Gillespie |  |  |  |
| - 1 0 50 100 150 Peakinfectiontime(days) (f) |  |  |  |  |
|  | 15 ) 3 |  |  |  |
|  |  |  |  |  |
|  | 0 1 # ( e10 v i |  |  |  |
|  | t c e fn i 5 k a e P 0 1 - (h) ment from realisatio 5. We use a switc and (f)), and infecti ump-Switch-Flow (d o presented as a soli ext, we generated 5, tching, the peak infe ever, this time, as w ob-Gillespie(Figure |  |  |  |


**Table (Page 26):**

| ) 5 0 1 # (15 s n o it c10 e fn I e v it 5 a lu m u C 0 1 - (e) |
|---|
| ) 5 0 1 # (15 s n o it c10 e |
| fn I e v it 5 a lu m u C 0 1 - (j) (b) and Doob-Gillesp 3. We also show t (h)). We compare t olutions and the fin the same quantities JSF (Figure SI8a) a k infective individua Lastly,aswesawwi |


**Table (Page 26):**

|  |
|---|
|  |


**Table (Page 26):**

|  |
|---|
|  |


**Table (Page 26):**

| Method | Extinction | Fade-out | Endemic |
|---|---|---|---|
| Jump-Switch-Flow Doob-Gillespie | 0.2512±0.0120 0.2520±0.0120 | 0.4700±0.0139 0.4668±0.0139 | 0.2788±0.0123 0.2812±0.0125 |


**Table (Page 28):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 28):**

|  | Tau-Leaping: Tau-Leaping: Tau-Hybrid C+ Tau-Hybrid C+ Tau-Hybrid Pyt | =0.01 =0.1 +: t=0.01 +: t=0.1 hon: t=0.1 | Doob-Gillespie JSF: =101 JSF: =103 JSF: =105 |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 30):**

| 2 9 1 2 3 4 1 1 1 1 1 1 0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2 - #10-8 ; : ) #10-5 / log (V ) 10 0 (a) |
|---|
| 8 0 1 3 4 4 1 1 1 1 1 1 0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2 |
| - #10-8 ; : ) #10-5 / log (V ) 10 0 (b) |
| 2 3 3 4 4 4 1 1 1 1 1 1 0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2 |
| - #10-8 ; : ) #10-5 / log (V ) 10 0 (c) |
| 1 9 3 4 4 4 1 1 1 1 1 1 0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2 |
| - #10-8 ; : ) #10-5 / log (V ) 10 0 (d) |
| 2 0 6 5 4 4 1 1 1 1 1 1 0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2 |
| - #10-8 ; : ) #10-5 / log (V ) 10 0 (e) |
| 2 5 1 1 5 4 1 1 1 1 1 1 0 1 2 0 0.5 1 200 400 600 0 5 10 15 0 5 10 0 1 2 |
| - #10-8 ; : ) #10-5 / log (V ) 10 0 (f) gureSI12:PosteriordistributionsofthemodelparametersandinitialviralloadforeachoftheselectedSARS-CoV-2 fections. The red dashed lines indicate the initial (uniform) bounds on prior samples. |
