---
title: "Task Oriented Dialogue Systems"
original_file: "./Task_Oriented_Dialogue_Systems.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag", "evaluation", "dialogue"]
keywords: ["cid", "jfnk", "gmres", "newton", "solver", "raphson", "bicgstab", "method", "krylov", "jacobian"]
summary: "<!-- Page 1 -->

Astronomy&Astrophysicsmanuscriptno.aanda ©ESO2024

### August8,2024

Jacobian-Free Newton-Krylov method for multilevel NLTE radiative
transfer problems

### D.Arramy,J.delaCruzRodríguez,andJ.Leenaarts

InstituteforSolarPhysics,Dept.ofAstronomy,StockholmUniversity,AlbaNovaUniversityCentre,SE-10691Stockholm,Sweden
e-mail:dimitri.arramy@astro.su.se
Received;accepted

## Abstract

Context.Thecalculationoftheemergingradiationfromamodelatmosphererequiresknowledgeoftheemissivityandabso"
related_documents: []
---

# Task Oriented Dialogue Systems

<!-- Page 1 -->

Astronomy&Astrophysicsmanuscriptno.aanda ©ESO2024

### August8,2024

Jacobian-Free Newton-Krylov method for multilevel NLTE radiative
transfer problems

### D.Arramy,J.delaCruzRodríguez,andJ.Leenaarts

InstituteforSolarPhysics,Dept.ofAstronomy,StockholmUniversity,AlbaNovaUniversityCentre,SE-10691Stockholm,Sweden
e-mail:dimitri.arramy@astro.su.se
Received;accepted

## Abstract

Context.Thecalculationoftheemergingradiationfromamodelatmosphererequiresknowledgeoftheemissivityandabsorption
coefficients, which are proportional to the atomic level population densities of the levels involved in each transition. Due to the
intricateinterdependencyoftheradiationfieldandthephysicalstateoftheatoms,iterativemethodsarerequiredinordertocalculate
theatomiclevelpopulationdensities.Avarietyofdifferentmethodshavebeenproposedtosolvethisproblem,whichisknownasthe
Non-LocalThermodynamicalEquilibrium(NLTE)problem.
Aims.OurgoalistodevelopanefficientandrapidlyconvergingmethodtosolvetheNLTEproblemundertheassumptionofstatistical
equilibrium. In particular,we explore theusability ofa Jacobian-Free Newton-Krylov(JFNK) method,which does notrequire an
explicitconstructionoftheJacobianmatrix,byestimatingthenewcorrectionwithaKrylov-subspacemethod.
Methods. WehaveimplementedaNLTEradiativetransfercodewithoverlappingbound-boundandbound-freetransitions,which
solvesthestatisticalequilibriumequationsusingaJFNKmethod,assumingadepth-stratifiedplane-parallelatmosphere.Asareference,wehavealsoimplementedtheRybicki&Hummer(1992)methodbasedonlinearizationandoperatorsplitting.
Results.OurtestswiththeFAL-Cmodelatmosphere(Fontenlaetal.1993)andtwodifferent6-levelCaiiandHiatomsshowthatthe
JFNKmethodcanconvergefasterthanourreferencecase,byuptoafactor2.Thisnumberisevaluatedintermsofthetotalnumber
ofevaluationsoftheformalsolutionoftheradiativetransferequationforallfrequenciesanddirections.Thismethodisalsocapable
ofreachingalowerresidualerrorcomparedtothereferencecase.
Conclusions.TheJFNKmethoddevelopedinthisstudyposesanewalternativetosolvetheNLTEproblem.Becauseitisnotbased
onoperatorsplittingwithalocalapproximateoperator,itcanimprovetheconvergenceoftheNLTEprobleminhighlyscattering
cases.Onemajoradvantageofthismethodisthatitshouldallowforadirectimplementationofmorecomplexproblems,suchas
havingoverlappingtransitionsfromdifferentactiveatoms,chargeconservationoramoreefficienttreatmentofpartialredistribution,
withouthavingtoexplicitlylinearizetheequations.
Keywords. Radiativetransfer–Sun:atmosphere–Methods:numerical–Line:profiles

## Introduction mentationtradedoffphysicalaccuracyinordertomaketheproblem computationally tractable, but it inspired future develop-

The statistical equilibrium equations describe the radiative and mentsinthefield(seebelow).Adifferentapproach,introduced
collisional transitions between the different levels of a model
byRybicki(1972),utilizedthecoresaturationapproximationto
atom(see,e.g.,Hubeny&Mihalas2014).Whenthecollisional
eliminatepassivephotonscatteringsinthelinecore,whileonly
termsdominatetherateequations,theassumptionofLocalTher- keeping the much more efficient scatterings in the line wings.
modynamical Equilibrium (LTE) is usually adequate and the
The latter improved the conditioning of the rate equations, alatomiclevelpopulationdensities(hereafterpopulationdensities)
lowingtraditionalLambdaiterationtoconvergeinareasonable
can be obtained analytically using the Saha-Boltzmann equa-
(yetlarge)numberofiterations.
tions. But when the radiative terms become relevant, the radiationfieldgreatlyinfluencesthepopulationdensities(NLTE).Be- The most successful methods to solve the statistical equicauseofthiscross-dependenceofthepopulationdensitieswith librium equations are based on the operator splitting technique
theradiationfield,theNLTEproblemmustbesolvediteratively (Cannon 1973) combined with a linearization of the problem
inordertomakethemconsistentwitheachother.Moreover,the (e.g., Auer & Mihalas 1969; Scharmer & Carlsson 1985; Rynon-localityoftheradiationfieldincreasesthecomplexityofthe bicki&Hummer1992).Scharmer&Carlsson(1985)linearized
problemanditscomplexitybecauseallgridcellsmustbesolved the first order radiative transfer equation and the rate equations
simultaneously. with respect to the population densities until they could derive
EarlyattemptssolvedtherateequationsusingLambdaitera- a linear system to estimate a correction. (Rybicki & Hummer
tion,whichisbasedonthefixedpointiterationmethod(see,e.g., 1992, RH92 hereafter) followed a slightly different approach,
Hubeny&Mihalas2014).However,suchschemepresentsvery replacing some of the quantities that depend on the population
poorconvergenceproperties,anditisunusableinpractice.Auer densitieswiththevaluefromthepreviousiteration.Thefunda-
&Mihalas(1969)proposedacompletelinearizationmethod(of mental difference between these two methods is that the comthesecondordertransferequation)tosolvethestructureandra- plete linearization method of Scharmer & Carlsson (1985) is a
diation emerging from static stellar atmospheres. Their imple- minimizationmethodoftheerrorintherateequations,whereas
Articlenumber,page1of18
4202
guA
7
]MI.hp-ortsa[
2v43271.6042:viXra

<!-- Page 2 -->


### A&Aproofs:manuscriptno.aanda

the RH92 method is closer to the fixed point iteration method whereas upper indices refer to depth points within the atmobut uses the operator splitting technique to drive the solution. sphere.TheRH92notationelegantlyunifiestheexpressionsfor
Furthermore,thecompletelinearizationmethodofScharmer& bound-bound and bound-free transitions, allowing for a very
Carlsson (1985) operates on the source function whereas the clean implementation of the rate equations. For a bound-bound
RH92methodoperatesontheemissivity,allowingforasimpler transitionbetweenalowerleveliandupperlevel j,wecandetreatmentofoverlapping(active)transitionsandpartialredistri- fine:
bution effects (Uitenbroek 2001; Leenaarts et al. 2012; Sukho- hν
rukov&Leenaarts2017). V ij = 4π B ij ϕ ij (ν,µ), (1)
Theperformanceofthesemethodsislargelydeterminedby
hν
the choice of the approximate operator. The simplest block- V = B ψ (ν,µ), (2)
ji 4π ji ij
diagonal (local) operator (Olson et al. 1986) decouples the exhν
plicitdependenceoftherateequationswithrespecttospaceand U = A ψ (ν,µ), (3)
itrequiresaminimalamountofstorageandoperations,making ji 4π ji ij
itagreatchoiceformulti-dimensionalproblems(e.g.,Leenaarts where A , B and B are the Einstein coefficients, ϕ and ψ
ji ji ij ij ij
&Carlsson2009;Amarsietal.2018).Thetradeoffisthatitig- arethelineabsorptionandemissionprofiles.νisthefrequency
noresinformationaboutthenon-localcontributiontotheinten- and µ the line-of-sight angle cosine. Similarly, for bound-free
sityandwhereitoriginatesfrom.Abetterpredictionofthemean transitionwecandefine:
intensity can be attained by using the single-point quadrature

### V = α (ν), (4)

global operator (Scharmer 1981; Scharmer & Nordlund 1982), ij ij
(cid:40) (cid:41)
greatlyinspiredbytheEddington-Barbierapproximation(Milne hν

### V = n Φ (T)exp − α (ν), (5)

1921;Eddington1926;Barbier1943).Althoughitonlyrequires ji e ij k T ij

## B

one coefficient per ray and direction (two if linear interpola- (cid:32) (cid:33)
2hν3
tionisused),theequationsbecomespatially-coupledagainand U = V , (6)
ji ji c2
theymustbesolvedtogether.Schemesusingtheglobaloperator
generally converge in less iterations than those using the local whereα isthephotoionizationcross-section,n istheelectron
ij e
operator. Several codes with implementations of the complete densityandΦ (T)istheSaha-Boltzmannfunctionevaluatedat
ij
linearization(Carlsson1986;Hubeny&Lites1995)andRH92 temperatureT:
(Uitenbroek2001;Leenaarts&Carlsson2009;Pereira&Uiteng (cid:18) h2 (cid:19)3/2 (cid:26)E −E (cid:27)
broek2015;Socas-Navarroetal.2015;Amarsietal.2018;Milic´ Φ (T) = i exp j i , (7)
&vanNoort2018;Osborne&Milic´ 2021)methodshavebeen ij 2g j 2πm e k B T k B T
extensivelyusedbythesolarandstellarcommunities.
where g denotes the level statistical weight, E the level energy
A common way of solving non-linear systems of equations andm isthemassoftheelectron.Inpractice,theseexpressions
e
istheNewton-Raphsonmethod(Raphson1690;Newton1736).
can be further simplified using the Einstein relations between
The main limitation to applying it to the statistical equilibrium coefficientstoobtain:
equationsistheexpensivecalculationoftheJacobianmatrixthat
is required in each iteration. In this paper, we propose to use V ji = g ij V ij , (8)
(cid:32) (cid:33)
a modification of the Newton-Raphson method known as the 2hν3
Jacobian-Free Newton-Krylov method (Knoll & Keyes 2004), U ji = g ij c2 V ij . (9)
to solve the radiative transfer problem. In this method, the Jacobian matrices are neither inverted nor built or stored. Instead For bound-bound transitions, assuming complete-redistribution
aniterativeinversionsolverbasedonKrylovsubspaces(Krylov ofscatteredphotons,g ij =g i /g j .Forbound-freetransitions:
1931)isusedtoestimatetheNewton-Raphsoncorrectiontothe (cid:40) hν (cid:41) n∗ (cid:40) hν (cid:41)
unknowns.Thismethodhasalreadyprovedtobeefficientinsev- g =n Φ (T)exp − = i exp − , (10)
ij e ij k T n∗ k T
eral fields such as hydrodynamics or neutron scattering prob- B j B
lems.ComparedtothemethodofScharmer&Carlsson(1985), wherethe∗-superscriptdenotestheLTEatomiclevelpopulation.
ourmethoddoesnotrequireanyexplicitlinearizationoftherate WecannowwritetherateequationsasafunctionofV ,reij
andradiativetransferequationsanditdoesnotutilizetheopera- gardlessofwhetherweareconsideringbound-boundorboundtorsplitting. free transitions. Let us recall the rate equation for the atomic
InSect.2weintroducethenumericalproblemunderconsid- leveliatdepthindexk:
erationandtheproposednumericalmethodforitsresolution,in (cid:88)(cid:26) (cid:27) (cid:88)(cid:26) (cid:27)
Sect.3wediscussourresultsandinSect.4wesummarizeour nk(Ck +Rk ) = nk(Ck +Rk ) , (11)
p pi pi i ip ip
conclusionsanddiscusspotentiallyinterestingdevelopmentsfor
p p
futurestudies.
wherenk isthepopulationdensityoftheatomicleveliatdepth
i
indexk.Ck andRk arerespectivelythecollisionalandradiative
ij ij

## Problemandmethods rate coefficients of the transition i → j at depth index k with

Ck = Rk = 0. The radiative rate coefficients can be expressed
ii ii

### Mathematicaldescriptionoftheproblem as a double integral over angle and frequency of the intensity

(Uitenbroek2001):

#### Theory

1 (cid:90) 1 (cid:90) ∞ dν
In this paper, we adopt the notation used in Uitenbroek (2001) Rk = dµ VkIk (n) i< j (12)
ij 2 hν ij µν
toexpressthestatisticalequilibriumequations.Wefurthermore −1 0
assume plane-parallel geometry hereafter. In all equations, un- 1 (cid:90) 1 (cid:90) ∞ dν(cid:20)(cid:18)2hν3(cid:19) (cid:21)

### Rk = dµ +Ik (n) gkVk i< j (13)

less mentioned otherwise, lower indices refer to atomic levels ji 2 hν c2 µν ij ij
−1 0
Articlenumber,page2of18

<!-- Page 3 -->

D.Arramyetal.:Jacobian-FreeNewton-KrylovmethodformultilevelNLTEradiativetransferproblems
for a plane-parallel atmosphere. Expressions for Vk and gk are formassconservationequations.Altogether,Eqs.21-22forma
ij ij
giveninEqs.1-10forbound-boundandbound-freetransitions. residualvector F(n)withthesamedimensionas n.Solvingthe
ThelastcomponentIk istheintensityindirectionµatfrequency system of equations for the vector of population densities nis
µν
ν and at depth index k. The vector n contains the population thereforeequivalenttofindingtherootoftheresidualvector F.
densities with the chosen structure (n1,...,n1 , ... ,nNz,...,nNz)T ThecalculationofFforagivenatmosphereandpopulationden-
1 Nℓ 1 Nℓ sitiesisdetailedinalgorithm1.Theresidualvectoristhecentral
whereN andN arerespectivelythenumberofdepthpointsand
z ℓ part of the solving process and constitutes the major computaactiveatomiclevels.Whilealltheotherquantitiesdonotdepend
tional cost of it. Thus, we evaluate the performance of a solver
of the population densities, the intensity involves them all in a
bythenumberofcomputationscalculationsofF(hereaftercalls)
non-linear and non-local fashion through the radiative transfer
neededtosolvetheproblemtoagivenprecision.
equation(RTE):

## I

µν
(τ
µν
) = (cid:82)
τ
∞
µν

## S

µν
(t)e−(t−τµν)dt µ>0 (14)
Algorithm1:CalculationoftheresidualvectorF

## I

µν
(τ
µν
) = (cid:82)
τ
0
µν

## S

µν
(t)e−(τµν −t)dt µ<0 (15)

## R


## D

e
a
s
t
u
a:
lt
a
:
p

## F

o
(
p
n
u
),
la
p
t
o
io
s
n
sib
d
l
e
y
ns
a
it
n
ie
e
s
w
v
e
e
s
c
t
t
i
o
m
r
a
n
ti
,
o
a
n
n
o
e
f
st

## J

imationof J
whereS = η /χ isthesourcefunction,χ andη arere- forν=ν ,...,ν do
µν µν µν µν µν 1 Nν
spectively thetotal opacityand emissivity,which canbe calcu- J† ← J ;
ν ν
latedthrough: if updatingJthen

## J ←0;

(cid:88)(cid:88) (cid:18) (cid:19) ν
χ = χ +χ + V n −g n (16) end
µν c sca ij i ij j
forµ=µ ,...,µ do
i j>i 1 Nµ
(cid:88)(cid:88)(cid:18)2hν3(cid:19) χ µν ←Eq.16;
η = η +χ J + g V n (17) η ←Eq.17;
µν c sca ν c2 ij ij j µν
j i<j S ←η /χ ;
µν µν µν

### I ←Eq.23and24;

wherethesubscript"c"referstothebackgroundcontinuumcon- µν
fortransitionsi→ jwith j<i,forallzdo
tributionand"sca"indicatesthebackgroundscatteringcontribu-

### R ← R +(µ,ν)-contributionofEq.12;

tion, which are assumed to be independent with respect to the ij ij

### R ← R +(µ,ν)-contributionofEq.13;

active population densities. The mean intensity J can be com- ji ji
ν
putedusing: end
if updatingJthen
1 (cid:90) 1 J ← J +ω I ;
J = I (n)dµ (18) ν ν µ µν
ν µν end
2
−1
end
The presence of J ν in the scattering term of Eq. 17 could com- end
plexify the calculations as it depends of the intensity, which in F←0;
turndependsonopacitiesandemissivities.Butsincethosescat- fortransitionsi→ jwith j<ido
teringtermsdonotoriginatefromactivetransitionsoftheatom, κ← n(C +R )−n(C +R );
weuseapreviousestimationofthemeanintensity J ν † insteadof F i ← F i i + ij κ; ij j ji ji
J ν inEq.17.Theopticalthicknessτ µν isobtainedbyintegrating F j ← F j −κ;
theopacityoverdepth: end
1 (cid:90) z fork=1,...,N z do
τ (z)= χ (z′)dz′ >0. (19) i←{j; nk =max (nk)};
µν |µ| 0 µν Fk ←nk − j (cid:80) nk; p p
i tot p p
Equation 11 describes a system of N × N equations and end
ℓ z
variablesnk inwhich N equationsareredundant.Thereforewe
i z
replaceonerateequationbyaparticleconservationequationper
depth-point:
(cid:88)
nk =nk , (20) 2.1.2. DiscretizationoftheRTE
p tot
p

### In practice when computing the radiative rates, the angular

wherenk isthetotalatomdensityatdepthindexk andiskept and frequency integrals are discretized according to quadratot tureschemesandyieldquadraturecoefficients(ω ,ω )foreach
constant.Thereplacementisdoneonthemostpopulatedatomic µ ν
set (µ,ν). Equations 14 and 15 are discretized along the depth
level,ateachdepthpointfornumericalstabilitypurposes.
axis and the involved integrals can be calculated assuming a

### Finally,thesystemofequationsisreformulatedas:

depth dependent profile for S . Such profile is usually taken
µν

### Fk(n) d=ef

(cid:88)(cid:26)
nk(Ck +Rk )−nk(Ck +Rk )
(cid:27)
. (21) assimplepiecewisepolynomialfunctions.Inthispaper,weconi i ip ip p pi pi siderpiece-wiselinearfunctions(Olson&Kunasz1987)which
p yields:
forradiativerateequationsand:
(cid:88) Ik = Ik+1e−∆τk µν +akSk +bkSk+1 µ>0 (23)

### Fk(n) d=ef nk − nk (22) µν µν µν µν

i tot p Ik = Ik−1e−∆τk µ − ν 1 +ak−1Sk +bk−1Sk−1 µ<0 (24)
p µν µν µν µν
Articlenumber,page3of18

<!-- Page 4 -->


### A&Aproofs:manuscriptno.aanda

wherethecoefficientsak andbk aregiveninappendixA.1and A second problem deals with the possibility to produce solution estimations with negative entries. While mathematically
1
∆τk ≈ |zk−zk+1|(χk +χk+1) (25) correct,asolutionestimationwithnegativepopulationdensities
µν 2|µ| µν µν is physically incorrect and the solver may even overflow when
solvingtheRTE.Apossiblesolutiontopreventnegativeentries
istheopticalthicknessoftheslab.
consistsinlimitingthecorrectionateachdepthindependently.
At the top of the atmosphere, we assume that there is no

### A third and inherent problem of the Newton-Raphson

incoming radiation. The deepest point in the atmosphere is asmethod deals with the quality of the initial guess. The initial
sumed to be thermalized so that the intensity at this location is
guessisusuallyanimportantfactorinthemethod’sconvergence
thePlanckfunctionB atthelocaltemperatureT:
ν rateoreventhemethod’sfailure.Themethodwillnotconverge

## I

µ

## N

ν
z = B
ν
(TNz) µ>0 (26) orventuresoutsidethedomainofdefinitionof Fifapoorstarting point is given. The method may also be trapped in a local
I µ 1 ν = 0 µ<0 (27) minimum of the residual vector, which can be difficult to spot.
Severaltoolssuchascontinuationmethodscanbeusedtobuild

### TheangularintegralsareevaluatedusingaGauss-Legendre

arobustsolverbasedontheNewton-Raphsonmethod.Moredequadraturedefinedin]0,1[.Ateachdepthindexktheincoming
tailsaregiveninKnoll&Keyes(2004).
andoutgoingraysareconsideredinthecalculationofthemean

### TheNewton-Raphsonrequirestheknowledgeoftheinverse

intensity J.Thenumberofquadraturepointsisaparameterset
ofaJacobianmatrixJ−1ateachiterativestep.Severalissuescan
by the user. We normally run with five quadrature points with F
potentiallyarisewhencomputingsuchquantities:
tworaysperangle.

## Implementation: most problems do not have an analytical

expression for J and an approximation needs to be given

## F

(forinstance,byfinitedifferences).Hencetheconvergenceis

### TheNewton-Raphsonmethod

likelytobelessthanquadratic.Intheworstcasethemethod

#### Basics mayfailiftheapproximationistoocoarse.


## Storage:forlargeproblems,storingJ canbeproblematic.

Solving the system of non-linear equations F(n) = 0 for the F

## Time consumption: inversion of J quickly becomes time

vector n may be achieved through several numerical iterative F
consumingasthesizeoftheproblemincreases,considering
methods. The Newton-Raphson method is one of the simplest
traditionalinversionroutinessuchasGauss-Jordaneliminaand most powerful ones (e.g., Press et al. 2002). If n(p) is the
tion.ThecomputationofthefullJacobianmightalsobeexestimation of the solution on the pth iteration, the next iterate
n(p+1) is sought such that F(n(p+1)) = 0. If we further define pensive.
δn(p) = n(p+1)−n(p)asthe pthincremental,theNewton-Raphson
methodreliesonalinearizationofF(n(p+1)):
0= F(n(p+1))= F(n(p)+δn(p))≈ F(n(p))+J (n(p))δn(p) (28)

## F

wherewehaveintroducedtheJacobianmatrixJ associatedto

## F

theresidualvector Fandevaluatedat n(p).ApossiblerepresentationofJ isgiveninFig.1.Solvingthelatterlinearsystemfor

## F

δn(p)yields:
δn(p) =−J−1(n(p))F(n(p)), (29)

## F

from which one may compute the next iterate n(p+1). This new
estimationisapriorinotasolutionto F(n)=0,althoughtheit-

### Fig.1.TheJacobianmatrixstructurefora N -levelatomproblem.J

erativeprocessensuresinthebestcasesaquadraticconvergence ℓ F
isa(N N)×(N N)matrixthatcontainsthederivativeoftheresidual
ℓ z ℓ z
to a solution (e.g., Dennis & Schnabel 1996). The initial guess
vectorcomponentswithrespecttothepopulationdensities.Thismatrix
n(0) mightbegivenforinstancebytheLTEortheradiation-free couldbeseenasaN ×N blockmatrixwhereeachblockJkℓisaN ×N
z z ℓ ℓ
predictions of the population densities. The linearization intro- matrix.Jkℓ storesthederivativesof Fatdepthindexkwithrespectto
ducedbytheNewton-Raphsonmethodonlyconsistsinamean thepopulationdensitiesatdepthindexℓ.
tosolvetherawstatisticalequationswhereasRH92solvesalinearized,approximatedversionoftheproblem. Theradiativetransferproblemweareconsideringdisqualifiesa
classical Newton-Raphson method mainly because of the computationalcostderivedfrombuildingofJ ,evenwhenusingan-

#### LimitationsoftheNewton-Raphsonmethod F

alytical expressions. Using the Newton-Raphson method there-
Wenotethatδn(p) mightalsoleadtoapoorerestimationofthe fore requires the information of the Jacobian matrices without
solution.Thisbehaviorcanoccurwhenthecorrectionδn(p) lies or partially building them in order to keep an efficient solver.
beyondthedomainoflinearityoftheresidualvectoraroundthe Thenextsectionswillprogressivelydetailawaytobypassthis
evaluationvector n(p).Asimplewaytoovercomethisbehavior thornyproblem.
istolimittheincrementalvectorwithadampeningfactorαand
tryα = 1,0.5,0.25,...until||F(n(p)+αδn(p))|| < ||F(n(p))||.This

### Iterativeinversion:Krylovmethods

procedureisthesimplestoftheso-calledlinesearchmethods,althoughmoreelaboratedonesexist(seeDennis&Schnabel1996, Equation29isequivalenttoalinearsystemoftheformAx= b
forinstance). where A = J (n(p)), x = δn(p) and b = −F(n(p)). This linear

## F

Articlenumber,page4of18

<!-- Page 5 -->

D.Arramyetal.:Jacobian-FreeNewton-KrylovmethodformultilevelNLTEradiativetransferproblems
system can be solved for x without inverting A using iterative 2.4. Jacobian-FreeNewton-Krylovmethods
approaches such as Krylov methods. In short, Krylov methods

#### Setup

areusedtosolvelargelinearsystemsthroughprojectionsontoa

### KrylovsubspaceK :

s We still have not addressed the problem of the Jacobian matrixestimationandthepotentialhighcomputationalcostitrep-

### K =span(r ,Ar ,A2r ,...,As−1r ),

s 0 0 0 0 resents. Fortunately, Krylov methods applied to the Newton-
Raphson iteration (Eq. 29) only require the action of the Jacowhere r = b−Ax isthe initialresidualvector builtfrom the
0 0 bian matrix J onto a generic vector v (see Sect. 2.3). It turns
initialguessx .SincexismeanttorepresentaNewton-Raphson F
0 outthattheoperationJ (n(p))vcanbeapproximatedusingfinite
correction, a typical initial guess would be zero and thus r 0 = differences(e.g.,Knoll F &Keyes2004):
b (we are considering that no correction is required initially).
AnotherinitialconditionmightbegivenbythesolutiontoPx =
bwherePisapreconditioner(Sect.2.4.3).Then,thesolution
0
is J (n(p))v=
F(n(p)+ϵ
||v
v
||2
)−F(n(p))
+O(ϵ) forward (31)

### F ϵ

estimatedas:
J (n(p))v= F(n(p))−F(n(p)−ϵ ||v v ||2 ) +O(ϵ) backward (32)
(cid:88)s F ϵ
x−x 0 = κ i q i , (30) J F (n(p))v= F(n(p)+ϵ ||v v ||2 ) 2 − ϵ F(n(p)−ϵ ||v v ||2 ) +O(ϵ2) central (33)
i=1
whereϵisthedifferencestep.SuchschemesdonotusetheJacowherethesetofvectors(q ,...,q )isabasisofK and(κ ,...,κ )
1 s s 1 s bian matrix but rather extra calls of F, which is a huge comare the corresponding coordinates. The purpose of a Krylov
putational and storage gain especially for large problems but
methodisthereforetoconstructabasisofK thendeterminethe
s at the cost of precision. This is the keystone of Jacobian-Free
corresponding scalars κ through projection methods. This coni Newton-Krylov solvers (hereafter JFNK). Such methods were
structionisdoneiterativelyinsiterations(oneiterationperbasis
firstpresentedbyKnoll&Keyes(2004).Sincetheresidualvecvector).Eachiterationaddsanewcomponenttothesolutionestor F(n(p))isalreadycomputedandpassedtotheKrylovsolver,
timation. The solution is sought such that ||r|| = ||b−Ax|| <
2 2 first order schemes (forward and backward) only require one
δ||r || whereδisarelativetolerancesetbytheuser.Wenotethat
0 2 freshcallofF.Incomparison,thesecondorderscheme(central)
thegiventolerancemightbeachievedinlessthansiterations.
requirestwofreshcallsof Fwhichisamajordrawback.Inour

### The size of the Krylov subspace is related to the precision

problem,everyevaluationof Ftranslatesintosolvingtheradiaofthesolutiononecanachieve,thelatteralsodependingofthe
tivetransferequationforallraysatallfrequenciesforagivenn.
method employed. If s is too small, the desired tolerance level Wealsonotethatthefinite-differencescalculationsinEq.31-33,
might not be achieved. On the other hand, if s is chosen to be
do not estimate the individual elements of the Jacobian matrix,
equaltothesizeofA,aKrylovmethodwilleventuallyconverge
butratherareusedtodirectlyestimatethematrix-vectorproduct.
to the exact solution in theory. In practice, round-off and trun-
Since the Newton-Raphson method is iterative, the matrixcation errors will limit the maximum precision one can expect.
vector products estimations are only needed to be accurate

### FromthedefinitionofK ,onemaynotethatonlymatrix-vector

s enough to guarantee convergence. This is the main reason why
productsarerequiredinsuchmethods,whichisthekeystoneof
thevastmajorityofJFNKsolversareusingfirstorderschemes
Sect.2.4.
ratherthanhigherorderones(Knoll&Keyes2004).Inpractice,
A plethora of Krylov methods has been developed over the
round-offandtruncationerrorsmayoccurandanoptimalchoice
pastdecadesamongwhichtwopopulartechniquesandtheirreofϵ ishardtofind.Thefirstsourceoferroriscausedbythefispectivevariantsarebroadlyusedinvariousphysicsproblems:
nite arithmetic precision of computers while the second source
of error is due to the limited accuracy of the scheme. Several

## The Generalized Minimal RESidual method (GMRES) is

yetempiricalchoicesforϵarefurtherdetailedinKnoll&Keyes
usuallybasedontheArnoldiprocessorHouseholdertrans-
(2004)tominimizebothsourcesoferror.
forms to produce orthonormalized bases. It was first developed in Saad & Schultz (1986) as an improvement and an
extensiontononsymmetricmatricesoftheMINRESmethod 2.4.2. Augmentationofnumericalprecisionwithcomplex
developedbyPaige&Saunders(1975).Itisaveryversatile numbers
linearsystemsolver.

## The Bi-Conjugate Gradient STABilized (BiCGSTAB) is


### Fortheconsideredproblem,thecomponentsofn(p)coverawide

basedontheLanczosbi-orthogonalizationprocedurewhich range of values: for instance, considering a two level hydrogen
generates non-orthogonal bases. It was first developed in atominaFAL-Catmosphere,theLTEpopulationdensitiescover
van der Vorst (1992) as a variant of the biconjugate gradi- the range 104 up to 1017 cm−3. This leads to large values of ϵ
entmethod(BiCG). consideringtheempiricalchoices.Arescalingofthedensitiesis
possibletokeepreasonableϵ values.Howeverthelargespanof
Both methods can be used with any invertible matrix. GMRES densitiesremainsproblematicwithintheresidualvector Fitself
requiresonematrix-vectorproductperiterationwhereastwoare andleadstoroundofferrors.Thus,theusualnumericalderivaneededwithBiCGSTABbutthelatterrequireslessmemorythan tiveschemesarenotsuitedforthegivenproblem.Luckily,there
GMRES. This is especially true whenever the number of itera- isanalternativeschemethatusescomplexnumberstoincrease
tions required for convergence is large, since BiCGSTAB uses the precision and dynamic range of the calculations, which is
a constant amount of memory per iteration and GMRES does farlessaffectedbyroundofferrorsorsubstractivecancellations
not. The most crucial feature of GMRES is a strict decrease of (e.g.,Kanetal.2022;Martins&Ning2021):
theresidualnorm||r|| throughouttheiterativeprocesswhereas
2
theconvergencebehaviorofBiCGSTABislessregular(vander Im[F(n(p)+iϵv)]
Vorst1992). J F (n(p))v= ϵ +O(ϵ2) (34)
Articlenumber,page5of18

<!-- Page 6 -->


### A&Aproofs:manuscriptno.aanda

whereiistheimaginaryunit.Thisspecialschemeonlyrequires Sect. 2.1 and Sect. 2.5.2). We note however that other physicsone fresh call of F and is second-order accurate as the cen- basedpreconditionerscouldbeveryrelevantforourcase,aspretral difference scheme. It however requires to set up the main sented in Janett et al. (2024) for solving linear problems. The
routines for complex arithmetic operations. We used the linear calculationofsuchapreconditionercanbeperformedwhencalpiecewise source function scheme described in Sect. 2.1 to in- culating F(n(p)),thusreusingmostofthevariablesthatwerealtegrate the radiative transfer equation along rays, for which the readycomputedtoobtaintheresidualvector.Algorithm2illusmodificationsarestraightforward.Theremainingtruncationer- tratesthefinalJFNKsolvingroutine.
rorcanbegreatlyattenuatedbyselectingatinyϵ value.Martins
&Ning(2021)recommendatypicalvalueϵ ∼10−200fordouble-

### Algorithm2:JFNKsolver

precisionfunctions.Notethattheimaginarypartisonlyusedfor
the Krylov solver, otherwise only the (unperturbed) real part is Data:aninitialpopulationdensitiesvectorn(0),an
considered.Sincetheimaginarypartistypicallyverysmallcom- initialestimationof J,aNewton-Raphson
paredtotherealpart,oneshouldlinearizeequationsthatinvolve tolerance ftol,aKrylovrelativetolerancer ,a
tol
theperturbations(e.g.computingthesourcefunction).Thispre- maximumnumberofiterationsmaxiter
vents introducing undesired arithmetic errors. Fig. 2 points out Result:Asolutionvectorn,ameanintensity
atypicalaccuracyissueinthecomputationoftheJacobianma- estimation J
trices when using traditional schemes. The complex scheme is niter←0;
the only one that can provide accurate estimations of Jacobian err←1+ ftol;
matricesforourgivenNLTEproblem.Forthissolereason,the f ← F(n(0)) ▷updatethepreconditionerP;
complexschemeistheonethatweuseinourJFNKsolvers. whileniter<maxiteranderr> ftoldo
x ←0orx ←−P−1f ▷initialguess;
0 0
δn←solutionofEq.36withaKrylovsolverusing

#### Preconditioning


### Eq.34;

Although we have introduced an accurate method to evaluate n ← n;
prev
the matrix-vector products J (n(p))v, the Jacobian matrix may n← n+δn;

## F

potentially be ill-conditioned. Consequently, the Krylov solver f ← F(n) ▷update J andP;
mayrequiremanyiterationstoconvergetothedesiredtolerance err←||(n−n prev )/(n+n prev )|| ∞ ;
becauseofthehighconditionnumberofJ (n(p)).Thereforewe niter←niter+1;

## F

proposetopreconditiontheKrylovsolverinordertoincreaseits end
efficiency. The preconditioning process consists in using a preconditioningmatrixP(thepreconditioner)suchthatJ (n(p))P−1

## F

(rightpreconditioning)orP−1J (n(p))(leftpreconditioning)has

## F

alowerconditionnumberthanJ (n(p)).Thesystemtobesolved

### F 2.5. AnalyticalJacobianmatrix

bytheKrylovsolverisnotgivenbyEq.29anymorebutrather
by: 2.5.1. Derivation
(J (n(p))P−1)(Pδn(p))=−F(n(p)) (35) In this part, we derive the expressions of the Jacobian matrix

## F

elements as a function of the population densities. In principle,
forrightpreconditioningand: these equations could be used to compute the fully analytical
Jacobian matrix. While the calculation of the full Jacobian is
(P−1J (n(p)))δn(p) =−P−1F(n(p)) (36) expensive, it is at least important to detail such derivations for

## F

preconditioningpurposes(Sect.2.4).Amoregeneralderivation
forleftpreconditioning.Thepreconditionedsystemisexpected is provided in Milic´, I. & van Noort, M. (2017) for derivatives
tobesolvedinlessiterationsthantheoriginalsystem.Equation according to any atmospheric parameter. The Jacobian element
35 is solved for y = Pδn(p) first then for δn(p). If the right pre- Jkℓ canbecalculatedasfollows:
ij
conditioningisused,thematrix-vectorproductscheme(Eq.34)
canbeadaptedforEq.35andreads: (cid:18)∂Fk(cid:19) ∂ (cid:32) (cid:88)(cid:26) (cid:27)(cid:33)
Jkℓ = i = nk(Ck +Rk )−nk(Ck +Rk ) (38)

### J (n(p))(P−1v)=

Im[F(n(p)+iϵ(P−1v))]
+O(ϵ2). (37)
ij ∂nℓ
j
∂nℓ
j p
i ip ip p pi pi

### F ϵ

unless Fk is a particle conservation equation in which case the
Iftheleftpreconditioningischosen,Eq.34isuseddirectlythen i

### Jacobianelementissimplygivenby:

the result is left-multiplied by P−1. The second member passed
to the Krylov solver in this case is −P−1F(n(p)). In our JFNK (cid:32) (cid:33)
∂ (cid:88)
solvers,wewillusetheleftpreconditioning,sincetherightpre- Jkℓ = nk − nk =−δ (39)
conditioning involves an extra inversion step. Because the pre- ij ∂nℓ tot p kℓ
j p
conditioner is meant to improve the overall performance of the
inversion process, P should be easy to calculate and invert. A
whereweusedthefactthatthepopulationdensitiesnk areconcommonlyusedalgebraicpreconditionerisgivenbythediago- i
sideredtobeindependentvariablesandthatnk iskeptconstant,
nalorblockdiagonalofthematrixoneattemptstoinvert(easy tot
therefore:
inversion and matrix-vector multiplication). This simple matrix
isalsoknownasaJacobi(orblock-Jacobi)preconditioner.This
∂nk
choice is particularly interesting in our case because the block i =δ δ . (40)
diagonal of J (n(p)) is as costly to compute as a call of F (see ∂nℓ kℓ ij

### F j

Articlenumber,page6of18

<!-- Page 7 -->

D.Arramyetal.:Jacobian-FreeNewton-KrylovmethodformultilevelNLTEradiativetransferproblems
Complex scheme 1st order / 1 1st order / 2 2nd order / 1 2nd order / 2
Top : -6.14 Top : 7.69 Top : 5.28 Top : 7.46 Top : 4.94
15 10 5 0 5
absolute error magnitude
Fig.2.TheJacobianmatrixestimationerrorforthe3-levelCaiisetup,evaluatedattheLTEpopulationsandforthedifferentschemes.Thefirstorder
schemeistheforwardone.Thedifferencestepsϵ andϵ arecommonchoices(Knoll&Keyes2004)andread:ϵ =(cid:80)Nℓ,Nzb|(nk)(p)|/(N N||v|| )+b
(cid:112) 1 2 1 i,k=1 i ℓ z 2
whereb=10−6andϵ =ϵ1/r 1+||n(p)|| /||v|| whereϵ isthemachineepsilonfordoubleprecisionnumbers,r=2forforwardandbackward
schemesandr=3for 2 the m ce ac n h tralscheme. 2 Thel 2 ogarithm m o ac f h theabsoluteerror(colorbar)isclippedbelow−16.Firstandsecondorder(i.e.forward
/backwardandcentral)schemesareterribleatevaluatingtheJacobianmatrixwhereasthecomplexalternativehighlightsaremarkableprecision.
InEq.38,thecollisionalcoefficientsdonotdependonthepop- where:
ulationdensities.ApplyingthechainruletoEq.38yields: (cid:88)
βℓ = Vℓ(1− gℓ ) (48)
(cid:18)∂Fk(cid:19) j js js
Jkℓ = i =δ Γk +Akℓ (41) s>j
ij ∂nℓ
j
kℓ ij ij
γℓ =
(cid:88)(cid:18)2hν3(cid:19)

### Vℓgℓ (49)

where: j c2 sj sj
s<j
(cid:88)

### Γk = δ (Ck +Rk )−(Ck +Rk) (42)

ij ij ip ip ji ji sothatEq.45thereforereducesto:
p

### Akℓ =

1 (cid:90) 1
dµ
(cid:90) ∞ dν
αk
(cid:18)∂I
µ
k
ν
(cid:19)
(43)
(cid:18)∂I
µ
k
ν
(cid:19)
=βℓ
(cid:18)∂I
µ
k
ν
(cid:19)
+γℓ
(cid:18)∂I
µ
k
ν
(cid:19)
+
(cid:88)
χp
(cid:18)∂J
ν
p(cid:19)(cid:18)∂I
µ
k
ν
(cid:19)
(50)
ij 2 −1 0 hν i ∂nℓ j ∂nℓ j j ∂χℓ µν j ∂ηℓ µν p sca ∂nℓ j ∂η µ p ν
(cid:88)(cid:26) (cid:27) (cid:88)(cid:26) (cid:27)
αk = Vk(nk−gk nk) − Vk(nk −gk nk) (44)
i ip i ip p pi p pi i Equation 50 consists in a linear contribution of the intenp>i p<i sityandasummationofnon-linearcrosstermsduetothebackbynoticingthatthederivativeoftheradiativeratesonlyinvolves ground scattering. Both derivatives involving Ik depend of the
µν
thederivativeoftheintensity Ik withrespecttonℓ.Theextinc- schemeonewillchoosetosolvetheRTE.Sinceweusethelin-
µν j
tionprofilewithineachcoefficientVk isconsideredtobeinde- ear piecewise source function scheme detailed in Sect. 2.1, the
ip correspondingexpressionsforthederivativesare:
pendent with respect to the population densities. Then, we can
expandthederivativeandfurtherwrite: (cid:18)∂Ik (cid:19) (cid:18)∂Ik+1(cid:19)
(cid:18)∂I µ k ν (cid:19) = (cid:88) (cid:40)(cid:18)∂I µ k ν (cid:19)(cid:18)∂χ µ p ν (cid:19) + (cid:18)∂I µ k ν (cid:19)(cid:18)∂η µ p ν (cid:19)(cid:41) (45) ∂χ µ ℓ µ ν ν = ∂χ µ ℓ µ ν ν e−∆τk µν +ak χ δ kℓ +bk χ δ k+1ℓ , (51)
be ∂ c n a ℓ j usethe p inte ∂ n χ si µ p t ν y,th ∂ r n o ℓ u j ghthe ∂η R µ p T ν E, ∂ is nℓ o j nlyafunctionofthe (cid:18) ∂ ∂ η I µ k ℓ ν (cid:19) = (cid:18)∂ ∂ I η µ k ℓ + ν 1(cid:19) e−∆τk µν +ak η δ kℓ +bk η δ k+1ℓ , (52)
µν µν
opticaldepthandthesourcefunction.Onemayfurtherdevelop
equation45andwrite: foroutgoingrays(µ>0),and:
(cid:18)∂ ∂ χ n µ p ℓ ν (cid:19) = δ pℓ βℓ j (46) (cid:18) ∂ ∂ χ I µ k ℓ ν (cid:19) = (cid:18)∂ ∂ I χ µ k ℓ − ν 1(cid:19) e−∆τk µ − ν 1 +ck χ δ kℓ +d χ kδ k−1ℓ , (53)
j µν µν
(cid:18)∂ηp (cid:19) (cid:18)∂Jp(cid:19) (cid:18)∂Ik (cid:19) (cid:18)∂Ik−1(cid:19)
∂n µ ℓ ν = δ pℓ γℓ j +χ s p ca ∂n ν ℓ (47) ∂η µ ℓ ν = ∂η µ ℓ ν e−∆τk µ − ν 1 +ck η δ kℓ +d η kδ k−1ℓ , (54)
j j µν µν
Articlenumber,page7of18

<!-- Page 8 -->


### A&Aproofs:manuscriptno.aanda

for ingoing rays (µ < 0) where the expressions of the different Therefore, only an approximate Jacobi preconditioner can be
involved coefficients are given in appendix A.2. These coeffi- used at a cost of precision and potentially convergence rate of
cientscanbeconstructedfromthevariablesusedwhensolving theKrylovsolver.Inthispaper,wegivethreesimplesolutionsto
the RTE to save computational time. The boundary conditions overcome both problems and still provide a preconditioner that
forthisscheme(Sect.2.1)implythat: dramaticallyimprovestheconvergencepropertiesoftheKrylov
solver:
(cid:18)∂INz(cid:19) (cid:18)∂INz(cid:19)
µν =0, µν =0 µ>0 (55) – The very first solution consists in disregarding the back-
∂χℓ
µν
∂ηℓ
µν groundscatteringcontribution.Inthiscase,Eq.50becomes
(cid:18)∂I1 (cid:19) (cid:18)∂I1 (cid:19) fork=ℓ:
µν =0, µν =0 µ<0 (56)
∂χℓ ∂ηℓ (cid:18)∂Ik (cid:19) (cid:18)∂Ik (cid:19) (cid:18)∂Ik (cid:19)
µν µν µν =βk µν +γk µν (60)
∂nk j ∂χk j ∂ηk
foreachvalueofℓ.ItcanbeshownthatEq.51to54definetwo j µν µν
upper(µ>0)andtwolower(µ<0)triangularmatrices:
– The second solution consists in discarding all of the cross
 termstoonlykeepthelocalone.Thepreconditionerfurther
(cid:18)∂I
µ
k
ν
(cid:19)
=
 0
a
,
k,
ℓ
ℓ=
<k
k (57)
reducestoalocaloperatorifoneuses:
∂χℓ µν (b χ ℓ χ −1+aℓ χ e−∆τℓ µ − ν 1) (cid:81)ℓ i= − k 2e−∆τi µν ℓ>k (cid:18)∂I µ k ν (cid:19) =βk (cid:18)∂I µ k ν (cid:19) + (cid:20) γk+χk (cid:18)∂J ν k(cid:19)†(cid:21)(cid:18)∂I µ k ν (cid:19) (61)
∂nk j ∂χk j sca ∂nk ∂ηk
j µν j µν
forµ>0and:
whereapreviousestimationofthederivativeofthemeanin-
(cid:18)∂I
µ
k
ν
(cid:19)
=
  0
ck
,
,
ℓ
ℓ
>
=
k
k (58)
t
i
e
s
n
e
s
a
i
s
ty
ily
is
c
u
o
s
m
ed
pu
in
te
s
d
te
f
a
o
d
r
o
th
f
e
th
n
e
e
c
x
u
t
r
i
r
t
e
e
n
ra
t
t
o
io
n
n
e.
b

## S

y
u
a
c
n
h
i
a
n
n
te
e
g
s
r
t
a
im
tio
a
n
tio
o
n
f
∂χℓ µν (d χ χ ℓ+1+cℓ χ e−∆τℓ µν) (cid:81)k i= − ℓ 1 +1 e−∆τi µν ℓ<k E tit q y . t 6 o 1 ze o r v o er (z a e l r l o a r n a g d l i e a s t . io O n n in e i c ti a a n lg s u im es p s l ) y or in c i a ti l a c l u iz la e te th th is e q m u e a a n n -
intensitygivenbytheLTEsolution.
forµ < 0.Theseexpressionsarevalidforinternaldepthpoints. – Thelastsolution,whichistheleastconstrainingbutrequires
Thematricesrelatedtothederivativeswithrespecttotheemis- additionaloperations,usesthesolutiongivenbyEq.59while
sivities are obtained by using the associated coefficients. Such consideringonlythelocalterms.Thecorrespondingoperator
matricescanbeunderstoodasJacobianmatricesoftheintensity thenhas:
withrespecttoopacitiesandemissivities.
Thelastparttodetaildealswiththederivativeofthemeanin-
(cid:18)∂I
µ
k
ν
(cid:19)
=βk
(cid:18)∂I
µ
k
ν
(cid:19)
+
(cid:20)
γk+χk r
(cid:21)(cid:18)∂I
µ
k
ν
(cid:19)
(62)
tensityterm.Throughitsdefinition,onemaynotethatthisquan- ∂nk j ∂χk j sca k ∂ηk
tityinvolvesderivativesoftheintensitywithrespecttothepop- j µν µν
ulation densities. Shortly, the full expansion of Eq. 50 consists wherethecoefficientr is:
k
in an intricate, self-consistent yet linear system of the deriva-
(cid:20) (cid:18) (cid:19) (cid:18) (cid:19)(cid:21)
tivesoftheintensitywithrespecttothepopulationdensities. It (cid:80) ω βk ∂I µ k ν +γk ∂I µ k ν
is however possible to find a solution to this system which can r k = µ µ j ∂χk µν (cid:18) j ∂ (cid:19) ηk µν (63)
bewrittenas: 1− (cid:80) ω χk ∂Iµ k ν
µ µ sca ∂ηk
µν
(cid:18)∂Ik (cid:19) (cid:18)∂Ik (cid:19) (cid:18)∂Ik (cid:19) (cid:88) (cid:18)∂Ik (cid:19)
µν =βℓ µν +γℓ µν + χp r µν , (59) Apreconditionerthatfollowsoneofthethreesolutionsonlyre-
∂nℓ j j ∂χℓ µν j ∂ηℓ µν p sca p ∂η µ p ν quires the calculation of ℓ = k terms in Eq. 50, which are only
built from the coefficients ak, ak, ck and ck given in appendix
χ η χ η
wherethecoefficientsr andthesolutionderivationcanbefound A.2.Furthermoreitscalculationcanbecarriedoutinacompap
in appendix B. In practice, the background scattering contribu- rable amount of operations than computing the residual vector
tiontothederivativesisusuallyveryweakandthereforecanbe F. In our JFNK solvers, we will use the first solution to calcuneglected. late the preconditioner since the scattering terms are negligible
in Eq. 59 compared to the other contributions, at least with the
consideredsetups(Sect.3.1).

#### PreconditioningofJFNKwiththeanalyticalJacobian

matrix

## Resultsanddiscussion


### PreconditioningtheJFNKsolveristroublesomeifoneusesthe

analyticalderivationoftheJacobianmatrix.Indeed,computing We have ported a simplified version of the excellent RH code
Eq. 50 is expensive if one is only interested in the Jacobi pre- (Uitenbroek 2001) to Python. The latter solves the statistical
conditioner,becausealloff-diagonaltermsneedtobecalculated. equilibriumequationsusingtheRH92method,butwiththepos-
Suchanissuearisesfromthebackgroundscatteringcontribution sibility of including partial redistribution effects of scattered
andonethereforehastodealwiththefollowinginordertoob- photons (PRD). This python version does not include PRD eftainthepreconditioner: fects and it is significantly slower than the C-version of RH.

### Butitisimplementedusingmodernprogrammingconstructions

– The summation in Eq. 50 involves all cross terms (k (cid:44) p suchas classesand inheritance,whichhas beenextremely useterms). ful in the implementation of our proof-of-concept JFNK solver
– Thepresenceofthemeanintensityinthescatteringtermalso as we could reuse most of the atom structures, opacity calculainvolvesallcrossterms(Sect.2.5). tion routines and formal solvers of the transport equation. We
Articlenumber,page8of18

<!-- Page 9 -->

D.Arramyetal.:Jacobian-FreeNewton-KrylovmethodformultilevelNLTEradiativetransferproblems
use the RH92 method as a reference in order to evaluate the
performance of our JFNK method. Given that we are analyzingtheconvergencepropertiesofdifferentschemes,wehavenot
included Ng-acceleration in our calculations (Ng 1974), which
isimplementedintheRHcode.

### Setup

AlltheresultspresentedinthispaperarecomputedusingaFAL-

### Cmodelatmosphereofthesolarphotosphere,chromosphereand

transitionregion(Fontenlaetal.1993),thatconsistsin82depths
pointscoveringtheintervalτ = [10−10,23]whereτ isthe
500 500
opticaldepthatλ = 500nm.Figure3depictsthestratifications
ofthegastemperature,electrondensityandtotalhydrogendensity.Theatmospheredoesnothaveanativeline-of-sightvelocity
profile.
105
104
0.0 0.5 1.0 1.5 2.0
Height [Mm]

## ]K[

erutarepmeT
Temperature 1017
1016
1015
1014
1013
1012
1011
1010
]3
mc[
ytisneD

### Krylovsolvertoleranceimpact

The Krylov solver that is internally used in the JFNK method
cangenerallyhaveanumberofparametersthatmustbechosen
for a given run (such as the size of the subspace or the convergence criteria). In the case of simple solvers such as GMRES
orBiCGSTAB,thissetofparametersreducestotheaccuracyto
which the solution is desired. This single parameter steers the
behavior of the JFNK method and its convergence properties.
Thus, we have investigated the impact of the Krylov solver accuracyonthestabilityandtheefficiencyoftheJFNKmethod.

### OurfirsttestistoassesstheabilityofaJFNKsolvertomatch

theNewton-Raphsonsolution.WewouldexpectminimaldifferencesbetweenbothsolversastheaccuracyoftheKrylovsolver
increases. Figure 4 shows the convergence properties of our
solversinthecaseofthe6-levelHiatomsetup.Severalaccuracy
levelsaredisplayedtohighlighttheevolutionofthediscrepanciesbetweenthedifferentmethods.TheNewton-Raphsonsolver
outperforms JFNK solversin every situation. By truncating the
precision of the correction provided by the Krylov solver, each
log 500 JFNK iteration becomes less accurate, usually leading to extra
2 0 -2 -4 -6 -8
iterations (compared to the standard Newton-Raphson case) in
nH ordertoachieveagivenconvergencelevelinthepopulationdenne sities.Thedifferencesbetweenthetwomethodsdecreasewhen
the precision of the Krylov solver is substantially increased.
Both JFNK solvers display similar results and converge to the
samesolution.TheydomatchthesamebehaviorastheNewton-
Raphsonsolverwhenr ∼10−4,validatingtheimplementation
tol
ofoursolvers.

### AsecondchartispresentedinFig.5anddirectlycompares

ouriterativesolverswiththeRH92solver.IntheJFNKmethod,
wewouldexpectarangeoftolerancesforwhichthemethodis
optimal(withrespecttotheresidualfunctioncalls):
– Smaller tolerances result in more precise estimations of the
inverseoftheJacobian.TheJFNKmethodthereforerequires
less Newton-Raphson iterations but the overall number of
calls to F is nonetheless higher. This is due to the extra
Fig.3.TheFAL-Catmosphereusedinthispaper.Thetemperature,the
accuracynotbeingimpactfulenoughontheconvergenceof
totalhydrogenandelectrondensitiesareshown.Theheightdimension
origin(z=0)correspondstoτ =1. theJFNKmethod.
500
– Highertolerancesresultincoarseestimationsoftheinverse
Three different atomic setups are used consisting in Hi of the Jacobian. Even though the number of calls to F is
and Caii. The different transitions are listed in table 1. Each reduced, Newton-Raphson iterations usually yield poorer
corrections. Therefore, the JFNK method requires extra
setup also include collisional and bound-free transitions (Shull
Newton-Raphson iterations to converge. Overall, the solver
&vanSteenberg1982;Burgess&Chidichimo1983;Arnaud&
willrequiremorecallstoF.
Rothenflug1985).Theabsorptionandemissionprofilesofeach
lineateachlocationaremodeledwiththeVoigtfunctionwhich
– The optimal range thus consists in a trade-off between the
dependsontheDopplerwidthandthedampingparameter.The
accuracy of the inverse of the Jacobian and the calls to F
latterincludesradiative,Stark,linearStark(incalculationswith
neededtoobtainthem.
H atoms) and van der Waals broadening. The angular integrals
arediscretizedusinga5-pointsGauss-Legendrequadrature.

### Wenotethatoverlycoarseestimationsoftheinverseofthe

We have performed our calculations using the Newton- Jacobian can yield an unstable behavior throughout Newton-
Raphson, two JFNK (using GMRES and BiCGSTAB respec- Raphsoniterations.Wehavefoundafewsituationsinwhichthis
tively)andtheRH92methods.BothJFNKsolversaresystemat- feature can be helpful to escape potential local minima of the
icallyusingtheanalyticalJacobileftpreconditioner(Sect.2.4.3 residual vector, and the method can even converge in less calls
and Sect. 2.5.2). All solvers require an exit condition that de- to F. But more likely, such inaccurate corrections will not lead
fines a good convergence. In our case, we keep track of the totheconvergenceoftheJFNKmethod.Forthesakeofstabilresidual norm ||F|| as well as the population relative change ity,itisrecommendedtouseaKrylovrelativetolerancesmaller
∞
norm||δn/n¯|| = 1||(n −n )/(n +n )|| .Unlessmen- than∼10−2.
∞ 2 new prev new prev ∞
tionedotherwise,weassumethatamethodhasconvergedwhen Figure 5 (top) highlights for the 3-level Caii setup an opti-
||δn/n¯|| <10−4.Thisconditionismostofthetimesufficiental- mal range spanning from r ∼ 3×10−4 to ∼ 3×10−2. In this
∞ tol
thoughwealsoimposeaminimaldropof||F|| by2magnitudes range,theJFNK(GMRES)solveroutperformstheRH92solver
∞
toavoidprematureexits. whereas the JFNK (BiCGSTAB) solver outperforms the latter
Articlenumber,page9of18

<!-- Page 10 -->


### A&Aproofs:manuscriptno.aanda

Table1.Asummaryofthedifferentatomsetupsusedinthispaper.
Configuration Lineswavelength[Å] Frequencypoints

### Caii(2levels+continuum) 3934 100

Caii(5levels+continuum) 3934-3968-8498-8542-8662 100-100-40-40-80
Hi(5levels+continuum) Ly(α,β,γ,δ)Ba(α,β,γ)Pa(α,β)Brα (150,50,20,20)(70,40,40),(20,20),20
Notes.Thelinesofeachsetupareindicatedaswellasthenumberoffrequencypointsusedperline.TheCaiisetupsconsistsoftheKline(3-level)
andtheH,KaswellastheIRtripletlines(6-level).TheHisetupconsistsofasetofLyman,Balmer,PaschenandBrackettlines.
1019
1016
1013
1010
107

## ||F||

rtol = 10 1 rtol = 10 2

## Jfnk (Gmres) Jfnk (Gmres)

JFNK (BiCGSTAB) JFNK (BiCGSTAB)
Newton-Raphson Newton-Raphson
1019
1016
1013
1010
107
0 10 20 30
Newton iteration

## ||F||

100
10 1
10 2
10 3
10 4
rtol = 10 3 rtol = 10 4

## Jfnk (Gmres) Jfnk (Gmres)

JFNK (BiCGSTAB) JFNK (BiCGSTAB)
Newton-Raphson Newton-Raphson
0 10 20 30
Newton iteration
||n
||
n
rtol = 10 1 rtol = 10 2

## Jfnk (Gmres) Jfnk (Gmres)

JFNK (BiCGSTAB) JFNK (BiCGSTAB)
Newton-Raphson Newton-Raphson
100
10 1
10 2
10 3
10 4
0 10 20 30
Newton iteration
||n
||
n
rtol = 10 3 rtol = 10 4

## Jfnk (Gmres) Jfnk (Gmres)

JFNK (BiCGSTAB) JFNK (BiCGSTAB)
Newton-Raphson Newton-Raphson
0 10 20 30

### Newton iteration

Fig.4.ComparisonoftheNewton-RaphsonmethodwithJFNKroutinesforthe6-levelHisetup(zeroradiationinitialguess).AstheKrylovsolver
relativetolerancer becomessmall,thediscrepancybetweenthedifferentmethodsreducestotruncationandround-offerrors.
tol
in a much narrower range. It is also possible to witness the ir- 3.3. Performanceofthesolver
regularconvergencebehavioroftheJFNK(BiCGSTAB)solver
asthecorrespondingcurveislesssmooththantheJFNK(GM- Table2showstheaverageexecutiontimepercalltoF(orequiv-
RES)solverone.Inthecaseofa6-levelsetup(Fig.5bottom), alentfortheRH92solver)fordifferentsetups.Thepurecallto
onemaynoticethereisnosuchoptimalrange.Instead,thenum- FisalwaysslightlyfastertoexecutebytheJFNKsolversthan
berofresidualvectorcallsdecreasesalmostmonotonicallywith the RH92 solver equivalent. This is due to the RH92 solver’s
theKrylovsolvertolerance.BothJFNKsolversoutperformthe methoditselfrequiringthecomputationofcross-couplingterms
RH92solverforKrylovrelativetoleranceshigherthan∼3×10−3 and the rest of the rate matrix elements in order to update the
(GMRES)and∼ 1×10−2 (BiCGSTAB).TheJFNK(GMRES) populationdensities.Ontheotherhand,computingtheresidual
solverhasalwaysproventooutperformtheJFNK(BiCGSTAB) vectorandupdatingthepreconditioner(JFNK)requiresapproxisolverformostKrylovtolerancesandvarioussetups,aswellas matelytwicethetimeofapureFcall(byaJFNKsolver),which
outperforming the RH92 solver in a wider range of Krylov tol- was expected. The preconditioner update call, while more time
erancesthantheBiCGSTABcounterpart.Notehoweverthatthe consuming than the RH92 solver equivalent, is only performed
residual vector calls from the JFNK / Newton-Raphson solvers once per Newton-Raphson iteration. The main contribution to
and the iterations of the RH92 solver are different. Therefore the execution time is due to the Krylov solver calls, therefore
Fig.5onlymakessenseifbotharecomparableinoperationsor pureresidualvectorestimations.Asaresultitcanbeshownthat
executiontime,whichisthecaseforoursetups(seeSect.3.3). the JFNK solver calls, as implemented in our proof-of-concept
Thus, one can deduce that the Jacobi preconditioner allows the code, do require slightly less time on average than RH92 calls
JFNK method to be more efficient than the RH92 one when evenforextremesuboptimalKrylovtolerances.
usedoptimally.Although,thepreconditionerislessefficientfor
asetupconsistingofmanyfrequenciessuchasthe6-levelCaiior Inthefollowingpart,wecomparethequalityofthesolutions
Hiones.Moreover,thelackofanoptimalrangeofKrylovtoler- provided by JFNK solvers with the reference RH92 case. The
convergence condition is usually given by a sufficiently small
ancespointsoutthattheJacobipreconditionerisnotenoughfor
changeinthepopulationdensities.Forthatpurpose,weusethe
suchsetups.Thisstatementalsoincludeeverysetupwithstrong
JFNK residual norm ||F|| as the metric because it is derived
scattering. ∞
from the raw equations we are attempting to solve, although
the RH92 solver is not designed to minimize the raw resid-
Articlenumber,page10of18

<!-- Page 11 -->

D.Arramyetal.:Jacobian-FreeNewton-KrylovmethodformultilevelNLTEradiativetransferproblems
Table2.AverageexecutiontimepercallfortheJFNKandtheRH92solvers.
Setup JFNK[ms/call] JFNK(withpreconditioner)[ms/call] RH92[ms/call]

### Caii(2levels+continuum) 55 121 65

Caii(5levels+continuum) 254 672 310

### Hi(5levels+continuum) 510 1160 631

Notes. Each call consists of the operations required to update the population densities once (and optionally the preconditioner for the JFNK
solvers).Allcodeswerenotdesignedtobeoptimal.TheJFNKsolversareslightlymoreefficientthantheRH92solver(withoutthepreconditioner
update).RunswereexecutedonaMacBookProprovidedwithaAppleM1Prochip.
100
80
60
40
sllac
noitcnuf
laudiseR

## Jfnk (Gmres)

JFNK (BiCGSTAB)

## Rh92

120
100
80
60
40
10 5 10 4 10 3 10 2 10 1
rtol
sllac
noitcnuf
laudiseR
thesuccessconditionisdictatedbythepopulationchangenorm
andnotbytheresidualnorm.
The size of the population change norm is not a good criterionforconvergence.Figure8showsthatthemaximumerror
in the rate equations for the JFNK solver is lower than in the

### RH92caseforasamecorrectionsize.TheJFNKsolverachieves

a lower absolute error in the residual norm than RH92 for any
given convergence condition set on the size of the population
changenorm.Thisisnotentirelyunexpected,asthesizeofthe
correctionperiterationisaffectedbytheefficiencyofthesolver:
forexample,intheextremecaseoftraditionallambdaiteration
JFNK (GMRES) leadstoverysmallcorrectionswithaverylargeerrorintherate
JFNK (BiCGSTAB) equations(i.e.residualnorm),whereasinacceleratedlambdait-

## Rh92

erationtheconvergenceiscomparativelymoreefficient.
1010
109
108
107
Fig.5.Residualvectorcallsrequiredforconvergenceasafunctionof
the Krylov solver relative tolerance. Top: 3-level Caii setup. Bottom: 106
6-levelCaiisetup.BothsetupsusetheLTEinitialcondition.
105
ual norm. Moreover, the residual norm might stall when using
RH92 because of the deepest layers of the atmosphere. Indeed,
themediumbecomesstronglycollisional,thereforetheradiative
contributionandthechangesthatmayoccurduringthesolving
process do not have a significant impact. Nevertheless, we can
disregardsuchlayersintheestimationoftheresidualnormbecausetheyareclosetoLTE.Inthefollowing,theresidualnorm
isevaluatedconsideringonlythefirst50points(z>700km)of
our atmosphere where the chromosphere is located. Not doing
thisleadstoaverylargeerrorintheRH92curve,mostlydriven
bydeeperlayerswhereLTEshouldhold.Suchbehaviorwasnot
presentintheJFNKcalculations.

### Figures6and7pointsoutthisclampedresidualnormaswell

asthepopulationchangenormfortheCaiiandtheHisetupsrespectively.ItisclearthattheRH92solverdisplaysasmallerconvergence rate for the biggest part of the solving process. JFNK
solversontheotherhandareoutperformedatthebeginningbefore the convergence rate surpasses the one of RH92 (Caii) or
equalsthelatter(Hi).Asanoutcome,JFNKsolverscanbebetterperformingthantheRH92one,especiallyiftheinitialguess
iscloseenoughtothesolution.Moreover,bothfiguresshowthat
the solution provided by the JFNK solvers is a hundred times
moreprecisethantheRH92one.Oneshouldkeepinmindthat

## ||F||


## Gmres

BiCGSTAB

## Rh92

10 1
10 3
10 5
0 10 20 30 40 50 60
Residual function calls
||n
||
n

## Gmres

BiCGSTAB

## Rh92

Fig.6.Residualandpopulationchangenormsduringthesolvingprocess of the 6-level Caii setup. The initial population densities are the

### LTEones.BothJFNKsolversareusingaKrylovrelativetoleranceof

10−2.EachcrossmarkercorrespondstoaNewton-Raphsoniteration.
Finally, we provide in Figs. 9-10 the spectra of the 6-level
Caiiand6-levelHisetupsrespectively.Inbothcases,theemergingspectrapredictedbytheRH92andtheJFNKsolversareessentiallyidentical.Wenotethattheextraaccuracyofthesolution
providedbyaJFNKsolverdoesnotyieldnoticeablechangesin
theemergingintensity,andwecanthereforedecidetoterminate
thesolvingprocessearlierandstilloutputasimilarresult.
Articlenumber,page11of18

<!-- Page 12 -->

A&Aproofs:manuscriptno.aanda
1010
109
108
107
106

## ||F||


## Gmres

BiCGSTAB

## Rh92

100
10 1
10 2
10 3
10 4
0 20 40 60 80 100 120 140 160
Residual function calls
||n
||
n

## Gmres

BiCGSTAB

## Rh92

10 1
10 3
10 5
Fig.7.1R0es7idualandpopulationchangenormsduringthesolvingprocess of the 6-level Hi setup. The initial population densities are the
zerorad1i0ati 9 oninitialguessones.BothJFNKsolversareusingaKrylov
relativetoleranceof10−2.EachcrossmarkercorrespondstoaNewton-
102 105 108
Raphsoniteration.

## ||F||


## ||I

ferI
||
ferI

## Jfnk (Gmres) Jfnk (Gmres)


## Rh92 Rh92

10 8 10 5 10 2
|| n||
n
1012
1010
108
106
104
102
100
10 9 10 7 10 5 10 3 10 1
|| n||
n

## ||F||

caldepthorline-of-sightvelocityarelarge.Allquantitieswere
interpolated to the new depth grid by linear interpolation. The
totalnumberofdepthpointswaskeptequaltothatintheoriginalmodel.ThismethodisessentiallyanextensionofthedepthoptimizationincludedintheMulticode(Carlsson1986),which
nowalsoaccountsforthepresenceofvelocitygradients.TheupperleftpanelinFig.11illustratestheartificialvelocitygradient
representedintheoptimizedgrid.
If the velocity gradient is properly sampled with sufficient
depthpoints,thereisnofundamentalreasonwhyanyofthealgorithmswouldperformverydifferentlythaninthestaticcase.
Our convergence plots in Fig. 11 show a very similar behavior
thanthoseinFig.6fortheCaiiatom.Afterafewiterations,the
residualnorm||F|| islowerthanintheRH92curve,whereasthe ∞
populationchangenorm||δn/n|| islarger.Afterapproximately
∞
80iterations,theRH92methodhasachievedaconvergence(in
theresidualnorm)thatissimilartothatoftheGMRESafter50
iterations.
The emerging intensity spectrum shows now strong asymmetries around the core of all chromospheric lines, which become progressively more blue-shifted by the presence of the
positive velocity gradient at the base of the chromosphere. The
CaiiH&Klines(3968Åand3934Å)showthewellknownenhancementofoneofthek2peaks(inthecaseontheredwing),
astheblue-shiftedlineprofileinthecorefrequenciesleavesan
opacitygapintheredwingofthelinewherephotonscanescape
moreefficientlycomparedtothestaticcase(Scharmer1984).

### Prospects


## Jfnk (Gmres)

The proposed JFNK method can be upgraded for a better ef-

## Rh92

ficiency and there are several ways of doing so. The external
Newton-Raphsonupdatedoesnotleavemuchspaceforimprovement,howeveritmightbeinterestingtoimplementacontinuationoralinesearchmethodtopotentiallyreducethenumberof
Newton-Raphsoniterations.AnicesurveyofcontinuationmethodsisgiveninAllgower&Georg(1993).Apotentiallysimple
but robust modification would be to implement a hybrid solver
mixing the RH92 and the JFNK solvers. Starting with a few

### RH92iterationsbeforeswitchingtoJFNKoneswouldallowthis

hybrid solver to avoid the usual Newton methods deficiencies,
Fig.8.Residualnormoftherateequations(6-levelHisetup)asafunc- aswellasprovidingabetterinitialguessfortheNewton-based
tionofthepopulationchangenormfortheJFNK(blue)andRH92(red) solver.Suchbehaviorwasencounteredwhenattemptingtosolve
schemes.TheKrylovrelativetolerancewassetto10−2.Thepopulation theproblemforinstancewiththe6-levelHisetupstartingwith
densitieswereinitializedusingthezeroradiationapproximation.Each
the LTE population densities. The performance of our JFNK
solver was run in order to achieve several Newton relative tolerances solversotherwisereducestohowefficienttheKrylovsolvercan
inthepopulationchangenorm(e.g.,10−1,10−2).Wethenrecordedthe
be,thereforedictatedbythequalityofthepreconditionerandthe
finalresidualandpopulationchangenorms.
solveritself.

### The Jacobi preconditioner used in the present study has


### Calculationswithvelocitygradients proven to be relatively inefficient in several of our setups and

therefore it could be improved. In our implementation, the lo-
InthissectionweshowthattheJFNKsolvercanproperlyhandle calpreconditionerisablock-diagonalmatrix.Whenitmultiplies
non-static atmospheres with velocity gradients as a function of theJacobian,itdestroysthenon-localderivativesintheleft-hand
depth.WehavemodifiedtheFAL-Cmodelatmosphereintroduc- sideofEq.36,andthereforeithasasimilareffectastheadopingasharpvelocitygradientaroundz=1000km,corresponding
tionofalocalapproximateoperatorintheRH92method.Howto the lower chromosphere. Velocity gradients can be problem- ever,oneshouldbearinmindthatthepreconditionershouldbe
aticifthevelocityjumpbetweenconsecutivegridcellsislarger kepttobeeasilyinvertibleandcalculablethusleavinganarrow
than approximately one third of the Doppler width (Ibgui et al. spaceforimprovement.Forthatmatterweprovidetwopossible
2013). Under those circumstances, the discretization of the ra- routes to calculate a more suitable preconditioner. The first opdiativetransferequationcanleadtoartifactsintheintensity. tiondealswiththesinglepointquadratureapproximationofthe
In order to avoid numerical artifacts in the calculation of RTE from Scharmer & Carlsson (1985). An approximation of
the intensity, we have performed a depth optimization by plac- thiskindcouldgreatlysimplifythecalculationsofthenonlocal
ing more points where gradients in temperature, density, opti- partoftheJacobianmatricesthereforeprovidingamoreaccurate
Articlenumber,page12of18

<!-- Page 13 -->

D.Arramyetal.:Jacobian-FreeNewton-KrylovmethodformultilevelNLTEradiativetransferproblems
4
3
2
1
0
0 2000 4000 6000 8000
wavelength [Å]
1e 6 1e 6 1e 5 1e 5 1e 5
5 3 3
3 3
4
2 2
2 2 3
2
1 1 1 1
1
3933.661 3968.467 8498.018 8542.089 8662.14
]1
rets
1
zH
2
mc
1
s
gre[
ytisnetnI
1e 5
Fig.9.Caii(6levels)spectrum.Inblack:outputfromtheRH92solver.Inblue:outputfromtheJFNKsolver(GMRES)withaKrylovrelative
toleranceof10−2.
4
3
2
1
0
0 5000 10000 15000 20000 25000 30000 35000 40000
wavelength [Å]
1e 8 1e 5 1e 5 1e 5
2.5 3 4
3
2.0
3
1.5 2
2
1.0 2
1
0.5 1
1
0.0
1215.67 4340.46 4861.28 6562.72
]1
rets
1
zH
2
mc
1
s
gre[
ytisnetnI
1e 5
Fig. 10. 6-level Hi spectrum. In black: output from the RH92 solver. In blue: output from the JFNK solver (GMRES) with a Krylov relative
toleranceof10−2.
preconditionerthantheJacobione.Thesecond,morerelatedto possibleinitialguesseswhicharetheLTEandthezeroradiation
the JFNK formalism is presented in Chen & Shen (2006) and ones.However,theremightbeotherpossibilitiesmoresuitedfor
deals with an adaptive preconditioning technique. Shortly, one aNewton-basedmethodappliedtotheradiativetransferproblem
can take advantage of the matrix vector products calculated by suchastheJFNKone.Forinstance,thepopulationdensitiescan
a Krylov solver to iteratively update the preconditioner. It also beinitializedwiththeonesderivedfromtheescapeprobability
allows the computation of a non local contribution to the pre- theory(e.g.,Hubeny&Mihalas2014;Judge2017).
conditioner.

### In this paper we have only considered 1D plane-parallel

Another upgrade one may implement deals with the initial NLTEproblems.Theextensionto3Dgeometrycouldbepossiguess provided to the JFNK solver. In this paper, we used two blewithsomeconsiderations.First,3Dradiativetransfercodes
Articlenumber,page13of18

<!-- Page 14 -->

A&Aproofs:manuscriptno.aanda
6
5
4
3
2
1
0
0.0 0.5 1.0 1.5 2.0
Height [Mm]
]s/mk[
solv
log 500
2 0 -2 -4 -6 -8 1010
108
106

## ||F||


## Gmres

BiCGSTAB

## Rh92

10 1
10 3
10 5
0 20 40 60 80
Residual function calls
||n
||
n

## Gmres

BiCGSTAB

## Rh92

4
3
2
1
0
0 2000 4000 6000 8000
wavelength [Å]
1e 6 1e 6 1e 5 1e 5 1e 5
5 5 3 3
4 4
4
2 2
3
3
2
2
2
1 1
1
1
3933.661 3968.467 8498.018 8542.089 8662.14
]1
rets
1
zH
2
mc
1
s
gre[
ytisnetnI
1e 5
Fig.11.Velocitygradientconvergencetestforthedifferentsolvers.Topleftpanel:theline-of-sightvelocityprofileusedforthetest.Topright
panel:theassociatedconvergenceplotforthe6-levelCaiisetupwithaKrylovrelativetoleranceof10−2 andinitialLTEpopulationdensities.
NotethatallthesolversrequiremoreiterationstoconvergethaninthecaseshowninFig.6.Bottompanel:convergedspectrumincludingthe
velocitygradientforRH92(black)andJFNK(GMRES)(blue).AJFNK(GMRES)velocity-freereferencespectrum(dashedblack)isalsoshown.
Thereisclearlyablueshiftoccurringnearthelinescenterduetothepositivevelocitygradientatthebaseofthechromosphere,resultinginvery
asymmetricoutputlines.
are usually domain-decomposed for parallelization purposes manager would need to propagate the relevant perturbed popu-
(Leenaarts&Carlsson2009),whereeachprocessorormachine lationdensitiestoeachsubdomain,butthecalculationof J can
has only access to the properties of the atmosphere, opacities, bedonethesamedomain-decomposedway.Thecostisoneextra
emissivities and population densities within one subdomain. In communicationfromthemanagertotheworkertasksperKrylov
order to implement the inner Krylov solver we would need to iteration.Bytodaymemorystandardsinhigh-performancecomcollect all population densities from all subdomains and keep putingcenters,thisapproachshouldbereasonablydoable.
the vector basis of the Krylov subspace in one manager task.
The key part is the evaluation of Eq. 34, which applies a perturbationtothepopulationdensitiesovertheentiredomain.The
Articlenumber,page14of18

<!-- Page 15 -->

D.Arramyetal.:Jacobian-FreeNewton-KrylovmethodformultilevelNLTEradiativetransferproblems

## Conclusion Acknowledgements. Weareverythankfultotherefereeforhis/herconstructive

suggestions and careful evaluation of our manuscript. The Institute for Solar
WepresentaJacobian-FreeNewton-Krylovmethodtosolvethe Physicsissupportedbyagrantforresearchinfrastructuresofnationalimpormulti-levelNLTEradiativetransferproblemassumingstatistical tance from the Swedish Research Council (registration number 2021-00169).
JL acknowledges financial support from the Swedish Research council (VR,
equilibrium. Our implementation shows a similar convergence
project number 2022-03535). No animals were harmed in the making of this
as the Newton-Raphson method, without ever building the full
manuscript.ThisprojecthasbeenfundedbytheEuropeanUnionthroughthe
Jacobian matrix explicitly. As benchmark, we have solved the EuropeanResearchCouncil(ERC)undertheHorizon2020researchandinno-
NLTEproblemassumingplane-parallelgeometryandtheFAL- vationprogram(SUNMAG,grantagreement759548)andtheHorizonEurope
Cmodelfora3-levelCaiiaswellas6-levelCaiiandHiatoms, program(MAGHEAT,grantagreement101088184).Partofourcomputations
wereenabledbyresourcesprovidedbytheNationalAcademicInfrastructurefor
which have been commonly used in solar physics applications.
SupercomputinginSweden(NAISS),partiallyfundedbytheSwedishResearch
Inthisstudy,wehaveshownthatoursolvercanconvergefaster Councilthroughgrantagreementno.2022-06725,atthePDCCenterforHigh
than other methods based on linearization, such as RH92. The PerformanceComputing,KTHRoyalInstituteofTechnology(projectnumbers
improvementintheconvergencerateisatomdependent,butitis
NAISS2023/1-15andNAISS2024/1-14).
usuallyafactor1.5−2inthebestcases.Thelatterisevaluated
in terms of the number of formal solutions needed to converge
the problem. However,we note that theJFNK formal solutions References
arefasterasnocross-termssummationsarerequiredcompared
toRH92.Thedownsidetoourmethodisthatitreliesonanap- Allgower,E.L.&Georg,K.1993,ActaNumerica,2,1–64
Amarsi,A.M.,Nordlander,T.,Barklem,P.S.,etal.2018,A&A,615,A139
propriate election of the convergence tolerance for the Krylov
Anusha,L.S.,Nagendra,K.N.,Paletou,F.,&Léger,L.2009,ApJ,704,661
innersolver.Oursensitivitystudyseemtoindicatethatanopti- Arnaud,M.&Rothenflug,R.1985,A&AS,60,425
malperformancecanbeattainedwhenthetoleranceissetinthe Auer,L.H.&Mihalas,D.1969,ApJ,158,641
rangeof10−3−10−2. Barbier,D.1943,Annalesd’Astrophysique,6,113
Benedusi,P.,Janett,G.,Belluzzi,L.,&Krause,R.2021,A&A,655,A88

### In order to increment the accuracy of the Newton-Raphson

Benedusi,P.,Janett,G.,Riva,G.,Belluzzi,L.,&Krause,R.2022,A&A,664,
correctionperiteration,wehaveaugmentedtheprecisionofthe A197
formalsolverusingcomplexnumbers.Thischangewasrequired Bjørgen,J.P.2019,PhDthesis,StockholmUniversity
given the enormous dynamic range of the atomic level popula- Burgess,A.&Chidichimo,M.C.1983,MNRAS,203,1269

### Cannon,C.J.1973,ApJ,185,621

tiondensitiesfromthephotospheretothetransitionregion.

### Carlsson,M.1986,UppsalaAstronomicalObservatoryReports,33

Compared to other studies that have used Krylov-subspace Chen,Y.&Shen,C.2006,PowerSystems,IEEETransactionson,21,1096
methodstoiterativelysolvethelinear2-levelatomproblem(e.g., Dennis,J.E.&Schnabel,R.B.1996,NumericalMethodsforUnconstrained
Hubeny & Burrows 2007; Anusha et al. 2009; Benedusi et al. Optimization and Nonlinear Equations (Society for Industrial and Applied

### Mathematics)

2021, 2022), our method handles multi-level non-linear prob-

### Eddington,A.S.1926,TheInternalConstitutionoftheStars

lems.GiventhattheJacobianmatrixdoesnotneedtobeexplic-

### Fontenla,J.M.,Avrett,E.H.,&Loeser,R.1993,ApJ,406,319

itlycomputedineachiteration,thismethodbecomesparticularly Hubeny,I.&Burrows,A.2007,ApJ,659,1458
interestingformorecomplexproblems,whichwebrieflydiscuss Hubeny,I.&Lites,B.W.1995,ApJ,455,376
hereafterasfutureprospects. Hubeny,I.&Mihalas,D.2014,TheoryofStellarAtmospheres:AnIntroductiontoAstrophysicalNon-equilibriumQuantitativeSpectroscopicAnalysis,

### The more obvious application relates to problems where


### PrincetonSeriesinAstrophysics(PrincetonUniversityPress)

partial redistribution effects of scattered photons are important. Ibgui,L.,Hubeny,I.,Lanz,T.,&Stehlé,C.2013,A&A,549,A126
While several efficient solutions are available for the 2-level Janett,G.,Benedusi,P.,&Riva,F.2024,A&A,682,A68
atom problem (e.g., Scharmer 1983; Paletou & Auer 1995), Judge,P.G.2017,ApJ,851,5
similarmethodsformulti-levelproblemssufferfromimportant Kan,Z.,Song,N.,Peng,H.,&Chen,B.2022,JournalofComputationaland

### AppliedMathematics,399,113732

limitations. For example, Hubeny & Lites (1995) presented a Knoll,D.&Keyes,D.2004,JournalofComputationalPhysics,193,357
PRD method based on the complete linearization approach of Krylov,A.N.1931,Izv.Akad.NaukSSSRSer.Fiz.-Mat,4,491
Scharmer&Carlsson(1985),whichdoesnotconsideroverlap- Leenaarts, J. & Carlsson, M. 2009, in Astronomical Society of the Pacific
Conference Series, Vol. 415, The Second Hinode Science Meeting: Beping active transitions. Uitenbroek (2001) overcomes that limiyondDiscovery-TowardUnderstanding,ed.B.Lites,M.Cheung,T.Magara,
tation by using the RH92 formalism and performing two itera-

### J.Mariska,&K.Reeves,87

tive cycles, separating the correction to the atomic level popu- Leenaarts,J.,Carlsson,M.,Hansteen,V.,&Rutten,R.J.2007,A&A,473,625
lationdensitiesandthecorrectiontotheemissivityprofile.The Leenaarts,J.,Pereira,T.,&Uitenbroek,H.2012,A&A,543,A109
method converges, but it requires several evaluations of the re- Martins,J.R.R.A.&Ning,A.2021,EngineeringDesignOptimization(CambridgeUniversityPress)
distribution integral per iteration. The method presented in this

### Milic´,I.&vanNoort,M.2018,A&A,617,A24

manuscript shows great potential to accelerate the convergence

### Milic´,I.&vanNoort,M.2017,A&A,601,A100

ofPRDproblems,sinceitdoesnotrequireanyexplicitlineariza- Milne,E.A.1921,MNRAS,81,361
tionoftheproblem. Newton,I.1736,TheMethodofFluxionsandInfiniteSeries:WithItsApplicationtotheGeometryofCurve-lines.By...SirIsaacNewton,...Translated
AnotherextensioncouldbetheinclusionofchargeconservafromtheAuthor’sLatinOriginalNotYetMadePublick.TowhichisSubtionwhenHatomsaresolved.Theideawouldbetoaddanother
join’d,aPerpetualCommentUpontheWholeWork,...ByJohnColson,...
conservation equation and update the electron density in each (HenryWoodfall;andsoldbyJohnNourse)
iterationastheionizationofHisusuallydominantinthechro- Ng,K.C.1974,J.Chem.Phys.,61,2680
mosphere. Previous studies have included such corrections, but Olson,G.L.,Auer,L.H.,&Buchler,J.R.1986,J.Quant.Spectr.Rad.Transf.,
35,431
needed to perform Newton-Raphson iterations due to the non-
Olson,G.L.&Kunasz,P.B.1987,J.Quant.Spectr.Rad.Transf.,38,325
lineardependenciesoftheSahaequationandtherateequations Osborne,C.M.J.&Milic´,I.2021,ApJ,917,14
with the electron density (e.g., Leenaarts et al. 2007; Bjørgen Paige,C.C.&Saunders,M.A.1975,SIAMJournalonNumericalAnalysis,12,
2019).Sincewedonotperformanyexplicitlinearizationofthe 617

### Paletou,F.&Auer,L.H.1995,A&A,297,771

rateequationsorthetransferequation,andwearealreadyusing

### Pereira,T.M.D.&Uitenbroek,H.2015,A&A,574,A3


### Newton-Raphsoniterations,theinclusionofchargeconservation

Press,W.H.,Teukolsky,S.A.,Vetterling,W.T.,&Flannery,B.P.2002,Numercouldbeveryefficientandrelativelystraight-forward. icalrecipesinC++:theartofscientificcomputing
Articlenumber,page15of18

<!-- Page 16 -->


### A&Aproofs:manuscriptno.aanda

Raphson,J.1690,AnalysisAequationumUniversalisSeuAdAequationesAlgebraicasResolvendasMethodusGeneralis,&Expedita,ExNovaInfinitarum

### SerierumMethodo,DeductaAcDemonstrata

Rybicki,G.B.1972,inLineFormationinthePresenceofMagneticFields,145

### Rybicki,G.B.&Hummer,D.G.1992,A&A,262,209

Saad,Y.&Schultz,M.H.1986,SIAMJournalonScientificandStatisticalComputing,7,856
Scharmer,G.&Carlsson,M.1985,JournalofComputationalPhysics,59,56
Scharmer,G.B.1981,ApJ,249,720

### Scharmer,G.B.1983,A&A,117,83


### Scharmer,G.B.1984,inMethodsinRadiativeTransfer,173–210

Scharmer,G.B.&Nordlund,Å.1982,StockholmsObservatoriumsReports,19

### Shull,J.M.&vanSteenberg,M.1982,ApJS,48,95

Socas-Navarro,H.,delaCruzRodríguez,J.,AsensioRamos,A.,TrujilloBueno,

### J.,&RuizCobo,B.2015,A&A,577,A7


### Sukhorukov,A.V.&Leenaarts,J.2017,A&A,597,A46


### Uitenbroek,H.2001,TheAstrophysicalJournal,557,389

vanderVorst,H.A.1992,SIAMJournalonScientificandStatisticalComputing,
13,631
Articlenumber,page16of18

<!-- Page 17 -->

D.Arramyetal.:Jacobian-FreeNewton-KrylovmethodformultilevelNLTEradiativetransferproblems
AppendixA: Discretizationcoefficients
AppendixA.1: PiecewiselinearRTE
ak =1−
1−e−∆τk
µν bk =
1−e−∆τk
µν −e−∆τk µν (A.1)
∆τk ∆τk
µν µν
AppendixA.2: Derivativesoftheintensity

### Foroutgoingrays(µ>0):

ak = − S µ k ν ak+ |z k+1 −z k |(cid:20) e−∆τk µν(Sk+1−Ik+1)− S µ k+ ν 1−S µ k ν bk (cid:21) (A.2)
χ χk 2µ µν µν ∆τk
µν µν
bk = − S µ k+ ν 1 bk+ |z k+1 −z k |(cid:20) e−∆τk µν(Sk+1−Ik+1)− S µ k+ ν 1−S µ k ν bk (cid:21) (A.3)
χ χk+1 2µ µν µν ∆τk
µν µν

### Sk

ak = µν ak (A.4)
η ηk
µν

### Sk+1

bk = µν bk (A.5)
η ηk+1
µν
whenk< N −1otherwiseonecansetthecoefficientstozero.Foringoingrays(µ<0):
z

### Sk |z −z |(cid:20) Sk−1−Sk (cid:21)

ck = − µν ak−1+ k−1 k e−∆τk µ − ν 1(Sk−1−Ik−1)− µν µν bk−1 (A.6)
χ χk 2µ µν µν ∆τk−1
µν µν

### Sk−1 |z −z |(cid:20) Sk−1−Sk (cid:21)

dk = − µν bk−1+ k−1 k e−∆τk µ − ν 1(Sk−1−Ik−1)− µν µν bk−1 (A.7)
χ χk−1 2µ µν µν ∆τk−1
µν µν

### Sk

ck = µν ak−1 (A.8)
η ηk
µν

### Sk−1

dk = µν bk−1 (A.9)
η ηk−1
µν
whenk>1otherwiseonecansetthecoefficientstozero.
Articlenumber,page17of18

<!-- Page 18 -->


### A&Aproofs:manuscriptno.aanda

AppendixB: FullJacobianwithbackground if the background scattering is weak. Introducing this result in
scatteringterms equationB.7givesthefinalsolution:
(cid:88)
LetusrecallEq.50withdifferentindices: x = b + r (Qi) ⊺ e (B.12)
i i p p
(cid:18)∂Ii (cid:19) (cid:18)∂Ii (cid:19) (cid:18)∂Ii (cid:19) (cid:88) (cid:18)∂Jp(cid:19)(cid:18)∂Ii (cid:19) p
jν =βℓ jν +γℓ jν + χp ν jν (B.1)
∂nℓ r ∂χℓ r ∂ηℓ sca ∂nℓ ∂ηp andifthebackgroundscatteringisweak:
r jν jν p r jν
(cid:88)
Ifwedevelopthemeanintensitytermusingtheangularquadrax
i
≈ b
i
+ bΩ,p (Qi) ⊺ e
p

## (B.13)

tureschemewithweightsω ,onecanwrite: p
µ
(cid:18)∂Ii (cid:19) (cid:18)∂Ii (cid:19) (cid:18)∂Ii (cid:19) (cid:88) (cid:18)∂Ii (cid:19)(cid:88) (cid:18)∂Ip (cid:19)
jν =βℓ jν +γℓ jν + χp jν ω qν
∂nℓ r ∂χℓ r ∂ηℓ sca ∂ηp q ∂nℓ
r jν jν p jν q r

## (B.2)

Going any further requires to simplify the notations to keep as
muchclarityaspossible.Letusdefinethefollowingquantities:
(cid:18)∂Ii (cid:19)
M = jν (B.3)
ij ∂nℓ
r
(cid:18)∂Ii (cid:19) (cid:18)∂Ii (cid:19)
B = βℓ jν +γℓ jν (B.4)
ij r ∂χℓ r ∂ηℓ
jν jν
(cid:18)∂Ik (cid:19)
Qk = χi jν (B.5)
ij sca ∂ηi
jν
werewehaveomittedtheindicesr,ℓ,ν.Fromthispoint,wewill
no more mention nor write these indices, however it should be
notedthatthefinalsolutionshouldbecomputedforthemaswell.
EquationB.2cannowbeexpressedas:
(cid:88) (cid:88)
M − Qi ω M = B (B.6)
ij pj q pq ij
p q
In the latter equation the unknowns one is seeking for are the
coefficientsM .EquationB.6canalsobeexpressedas:
ij
(cid:88)
x − ⟨x ,Ω⟩(Qi) ⊺ e = b (B.7)
i p p i
p
where x = (M ,...,M )⊺, b = (B ,...,B )⊺, Ω =
i i1 iNµ i i1 iNµ
(ω ,...,ω )⊺andQithematrixassociatedtothecoefficientsQi .
1 Nµ kl
Thevectore isthe pth canonicalbasisvector.Atthispoint,the
p
unknownsaregatheredintothevectors x.Itshouldbemention
i
thatifthebackgroundscatteringisignored, x = b andthesoi i
lutionisthereforesimple.Otherwise,letusdotproductEq.B.7
withΩtoobtain:
(cid:88)
r
i

## − A

ip
r
p
=bΩ,i (B.8)
p
wherer
i
= ⟨x
i
,Ω⟩,bΩ,i = ⟨b
i
,Ω⟩and A
ij
= [QiΩ]
j
.Theequationcanalsobewrittenusingmatrixnotationstoobtain:
(I−A)r= bΩ (B.9)
were I is the identity matrix. This is a simple linear system of
unknownrforwhichthesolutionis:
r=(I−A)−1bΩ (B.10)
butcanbesimplifiedinto:
r≈(I+A)bΩ (B.11)
Articlenumber,page18of18

## Tables

**Table (Page 10):**

| Configuration | Lineswavelength[Å] | Frequencypoints |
|---|---|---|
| Caii(2levels+continuum) Caii(5levels+continuum) 3934 Hi(5levels+continuum) Ly(α,β | 3934 -3968-8498-8542-8662 ,γ,δ)Ba(α,β,γ)Pa(α,β)Brα (150,50 | 100 100-100-40-40-80 ,20,20)(70,40,40),(20,20) |


**Table (Page 10):**

| JFNK (GMRES) JFNK (BiCGSTAB) Newton-Raphson |
|---|
|  |


**Table (Page 10):**

| JFNK (GMRES) JFNK (BiCGSTAB) Newton-Raphson |
|---|
|  |


**Table (Page 10):**

| JFNK (GMRES) JFNK (BiCGSTAB) Newton-Raphson |
|---|
|  |


**Table (Page 10):**

| JFNK (GMRES) JFNK (BiCGSTAB) Newton-Raphson |
|---|
|  |


**Table (Page 11):**

| Setup | JFNK[ms/call | ] JFNK(withpreconditioner)[ms/call] | RH92[ms/call] |
|---|---|---|---|
| Caii(2levels+continuum) Caii(5levels+continuum) Hi(5levels+continuum) | 55 254 510 | 121 672 1160 | 65 310 631 |


**Table (Page 11):**

| JFNK (GMRES) JFNK (BiCGSTAB) RH92 | JFNK (GMRES) JFNK (BiCGSTAB) RH92 |
|---|---|
|  |  |


**Table (Page 12):**

| GMRES 1010 BiCGSTAB RH92 109 108 \|\|F\|\| 107 106 100 GMRES BiCGSTAB RH92 10 1 10 2 \|\|n n \|\| 10 3 |  |  |  |  |  |
|---|---|---|---|---|---|
|  | GMRES BiCGSTAB RH92 |  |  |  |  |
| 110041 JFNK (GMRES) JFNK (GMRES) RH92 RH92 10 3 0 20 40 60 80 100 120 140 160 Residual function calls \|\|I 10 5 ferI f | JFNK (GMRES) JFNK (GMRES) |  |  |  |  |
|  |  |  | 80 func |  |  |
| erI Fig.7.1R0es7idualandpopulationchangenormsduringthesolvingpro- \|\| cess of the 6-level Hi setup. The initial population densities are the zerorad1i0ati 9 oninitialguessones.BothJFNKsolversareusingaKrylov relativetoleranceof10−2.EachcrossmarkercorrespondstoaNewton- 102 105 108 10 8 10 5 10 2 Raphsoniteration. \|\|F\|\| \|\| n\|\| n 1012 JFNK (GMRES) 1010 RH92 108 106 \|\|F\|\| 104 102 100 10 9 10 7 10 5 10 3 10 1 \|\| n\|\| n |  | andpopulationchang vel Hi setup. The init itialguessones.BothJ |  | rmsduringthesolvingpr opulation densities are t KsolversareusingaKryl |  |
