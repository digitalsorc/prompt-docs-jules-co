---
title: "Code Understanding Generation"
original_file: "./Code_Understanding_Generation.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "chain-of-thought", "evaluation", "multimodal"]
keywords: ["mass", "cid", "profile", "overdensity", "density", "our", "etal", "page", "scaling", "pavlidou"]
summary: "<!-- Page 1 -->

Astronomy&Astrophysicsmanuscriptno.aanda ©ESO2024

### December2,2024


### Mass scaling relations for dark halos

from an analytic universal outer density profile

### GiorgosKorkidis1,2, andVasilikiPavlidou1,2

1 DepartmentofPhysicsandInstituteforTheoreticalandComputationalPhysics,UniversityofCrete,GR-70013Heraklio,Greece
email:gkorkidis@physics.uoc.gr;pavlidou@physics.uoc.gr
2 InstituteofAstrophysics,FoundationforResearchandTechnology–Hellas,VassilikaVouton,GR-70013Heraklio,G"
related_documents: []
---

# Code Understanding Generation

<!-- Page 1 -->

Astronomy&Astrophysicsmanuscriptno.aanda ©ESO2024

### December2,2024


### Mass scaling relations for dark halos

from an analytic universal outer density profile

### GiorgosKorkidis1,2, andVasilikiPavlidou1,2

1 DepartmentofPhysicsandInstituteforTheoreticalandComputationalPhysics,UniversityofCrete,GR-70013Heraklio,Greece
email:gkorkidis@physics.uoc.gr;pavlidou@physics.uoc.gr
2 InstituteofAstrophysics,FoundationforResearchandTechnology–Hellas,VassilikaVouton,GR-70013Heraklio,Greece

## Abstract

Context. Theaveragematterdensitywithintheturnaroundscale,whichdemarcateswheregalaxiesshiftfromclusteringarounda
structuretojoiningtheexpansionoftheUniverse,isanimportantcosmologicalprobe.However,ameasurementofthemassenclosed
bytheturnaroundradiusisdifficult.Analysesoftheturnaroundscaleinsimulatedgalaxyclustersplacetheturnaroundradiusatabout
threetimesthevirialradiusinaΛCDM universeandata(present-day)densitycontrastwiththebackgroundmatterdensityofthe
Universeofδ∼11.Assessingthemassatsuchextendeddistancesfromacluster’scenterisachallengeforcurrentmassmeasurement
techniques.Consequently,thereisaneedtodevelopandvalidatenewmass-scalingrelations,toconnectobservablemassesatcluster
interiorswithmassesatgreaterdistances.
Aims.Ourresearchaimstoestablishananalyticalframeworkforthemostprobablemassprofileofgalaxyclusters,leadingtonovel
massscalingrelations,allowingustoestimatemassesatlargerscales.Wederivesuchanalyticalmassprofilesandcomparethemwith
thosefromcosmologicalsimulations.
Methods.Weusedexcursionsettheory,whichprovidesastatisticalframeworkforthedensityandlocalenvironmentofdarkmatter
halos,andcomplementitwiththesphericalcollapsemodeltofollowthenon-lineargrowthofthesehalos.
Results.Theprofilewedevelopedanalyticallyshowedgoodagreement(betterthan30%,anddependentonhalomass)withthemass
profiles of simulated galaxy clusters. Mass scaling relations were obtained from the analytical profile with offset better than 15%
fromthesimulatedones.Thislevelofprecisionhighlightsthepotentialofourmodelforprobingstructureformationdynamicsatthe
outskirtsofgalaxyclusters.
Keywords. large-scalestructureofUniverse–Methods:analytical,numerical–Galaxies:clusters:general

## Introduction overallmattercontentoftheuniverse,andthatitsevolutionwith

time is influenced by the existence of a cosmological constant.
Galaxy clusters, the largest gravitationally bound structures in Theturnaroundscalehasthusthepotentialtoprovidenewconthe universe, have long been recognized as valuable cosmo- straintsoncosmologicalparameters,complementarytotheones
logical laboratories. During the past three decades, significant obtainedfromtheCosmicMicrowaveBackground(CMB)(e.g.,
advances have been made in understanding their composition, Komatsuetal.2011),BaryonAcousticOscillations(BAO)(e.g.,
dynamics, and integral role within the cosmic web. The well- Eisensteinetal.2005),andTypeIaSupernovae(e.g.,Amanullah
studied interiors of these clusters, particularly their relaxed re- etal.2010).
gions, have laid the foundations for our concordance model of
Our subsequent studies (Korkidis et al. 2020, 2023) conhierarchicalstructureformation.Thisprogresshasnowextended
firmed the utility of ρ for testing cosmological models usbeyond the traditionally studied virialization regime to include ta
ing N-body cosmological simulations. However, measuring the
the kinetically driven splashback regions (Diemer & Kravtsov
turnaround density in actual observations using current as-
2014;Adhikarietal.2014;Moreetal.2015,2016;O’Neiletal.
tronomical surveys presents significant challenges. The radius
2021). However, the potential of the outer regions of galaxy
wheregalaxiesjointheHubbleflowhasthusfarbeenmeasured
clusters, extending outside the splashback radius, into the inforonlyafewnearbysuperclusters(Karachentsev&Nasonova
fallingregionandbeyond,remainslargelyuntapped.Theseouter
2010; Nasonova et al. 2011; Lee 2018). Accurately measuring
reachesholdsubstantialpromisefordeepeningourunderstandthetotalmassofgalaxiesatthesescalespresentsanevenmore
ingofstructureformationandcosmology.
formidable challenge. Several issues complicate such observa-
Recently,theturnaroundscalehasreceivedsignificantatten- tionsonacluster-by-clusterbasis,makingtheassociatederrors
tion in cosmological studies (Pavlidou & Tomaras 2014; Lee unsuitableforprecisecosmologicalanalysis:(a)Accuratemea-
& Li 2017; Fong et al. 2022; Lopes et al. 2019; Capozziello surement of the mass at the turnaround scale would necessitate
et al. 2019). This scale represents the point at which galax- extensivespectroscopicandgravitationallensingsurveys,mapies transition from infall towards the central cluster to expan- pingthegalaxydistributiononverylargescalesaroundclusters.
sion with the background Universe. In previous work (Pavli- (b)Inthecontextofthecolddarkmatter(CDM)modelofstrucdou et al. 2020), we identified the turnaround scale as a novel ture formation, it is well-acknowledged that most of the mass
cosmological probe. We showed that the present average mat- surroundinggalaxiesisdarkand,forsuchsmallobjectsasgalacter density on this scale (the turnaround density ρ ) probes the tic halos, largely inaccessible; (c) Foreground and background
ta
Articlenumber,page1of10
4202
voN
82
]OC.hp-ortsa[
2v43681.2042:viXra

<!-- Page 2 -->


### A&Aproofs:manuscriptno.aanda

galaxy contamination at these scales is non-negligible and can 2. Ananalyticclosed-formprofileforcluster
skewobservations. exteriors
In this context, developing scaling relations that would Tobuildamodelofthedensitydistributionaroundcosmicstrucallow us to infer the mass at turnaround scales from well- tures of varying masses, Pavlidou & Fields (2005) used excurestablishedobservablemassesbecomesparamount.Currentob- sion set theory to derive a joint distribution of structures with
servationaltechniques,suchasX-ray,Sunyaev-Zel’dovich,and respect to mass and surrounding overdensity, thus providing a
weak-lensing surveys (Andrade-Santos et al. 2021; Bahar et al. general, two-parameter statistical description. This double dis-
2022;PlanckCollaborationetal.2013;Sifónetal.2016;Hilton tribution extends the Press-Schechter formalism by introducing
et al. 2021; Ruppin et al. 2018; Hilton et al. 2018; Gruen aclusteringscaleparameter,β,whichquantitativelydefinesthe
etal.2014),inconjunctionwithmachinelearningmethods(see, "environment" around a structure of mass m to be a scale that
e.g., Ho et al. 2019; Gupta & Reichardt 2020, 2021; Armitage includes mass βm (including the structure itself, so β > 1). By
et al. 2019a,b), routinely identify clusters and measure fixed- providing the statistics of the overdensity field as a function of
overdensity masses (masses on a scale where the average den- enclosed mass, the double distribution offers a path to deriving
sityoftheclusterisasetmultipleofthethemeanmatterdensity the most probable density profile at large distances away from
intheuniverse).Theseoverdensitymassesscalewellwitheach cosmic structures - in other words, to understanding how inteother, leading to the plausible hypothesis that a straightforward rior cluster profiles merge into the background density of the
scaling relation might exist among all overdensity masses. The expandingUniverse.
turnaround mass is also a fixed-overdensity mass (for instance, Modelsoftheouteraveragedensityprofileofclustersfrom
in a ΛCDM cosmology at z = 0, the turnaround mass corre- first principles were pioneered by Barkana (2004); Prada et al.
sponds to an overdensity of δ = 11, see for example Korkidis (2006a); Betancort-Rijo et al. (2006); Tavio et al. (2008). Our
et al. 2020). Identifying the origin of these scalings could thus methodology, while not fundamentally divergent from theirs,
provideastraightforwardpathtowardsestablishingscalingsfor differs in four key choices. Firstly, in contrast to their use of a
theturnaroundmassaswell. ’Lagrangianvariableq’—essentiallytheenclosedmassinunits
of radius— as an independent variable, we use the enclosed
Onepathtodevelopingapredictivemodelforthesescaling massitself.Thischoicenotonlyallowsforamoreintuitiveunrelationsmaypassthroughthethemassprofileofclusterhalos. derstanding of our derivations, but, most importantly, straight-
Much of the effort in this field focuses on the cluster interior, forwardly leads to usable mass scaling relations. Secondly, we
resulting in the widespread use of common profiles like NFW employ a much simpler, while still accurate, approximation for
or Einasto (Navarro et al. 1996; Einasto 1965). These profiles the transformation of linear-theory overdensities to sphericalweredevelopedtodescribetheinnermostpartsofsuchstructures collapseones,whichwasproposedbyPavlidou&Fields(2005).
throughextensivestudiesincosmologicalsimulations.Morere- This choice simplifies the calculations and results in a more
cently,Diemer(2023)hasproposedamodelthatfitsrobustlythe transparentclosed-formexpression.Thirdly,ourfocusisprimarentirestackeddensityprofileofsimulatedclusters,bothinteriors ily on the largest structures. This specificity allows us to omit,
andexteriors.Inpractice,suchcomprehensiveprofilescouldbe withminimalerror,correctionsforstructuresengulfedbylarger
leveragedtoconstructscalingrelations. ones, given the immense size and rarity of our targeted structures.Finally,weapproximatethevarianceofthedensityfield,
Inthisstudy,wedoexactlythis,makinguseofamodelfor S(m), with a power law of the smoothing mass scale, m. This
the mass profile of cluster exteriors derived analytically from approximation holds when concentrating on a limited range of
first principles. The advantages of using an analytic model for masses, as we do in our study, and it is critical in demonstratthe profile are twofold. First, the derivation process elucidates ing the (quasi-)universality of our derived profile. The cumulathephysicalprocessesthatshapetheprofile.Second,theprofile
tiveeffectofthesemodificationsisasignificantsimplificationof
parameters are directly and causally relatable to cosmological the mathematical framework without a significant compromise
andstructure-formationparameters,withouttheneedforexpen- inpredictivepower.
siverunsoflargesuitsofcosmologicalsimulations. BuildingupontheworkbyPavlidou&Fields(2005),weextendtheiranalysisbyderivingthemostprobabledensityprofile
To derive an analytic relation for the (most probable) outer asafunctionofcollapsedmassfromthedoubledistribution.In
densityprofileofgalaxyclusters,wemakeuseofthemodelfor what follows, we summarize the mathematical formalism and
the density distribution around dark matter halos proposed by theassumptionsemployedinthisderivation.
Pavlidou&Fields(2005).Ouraimistoarrivetoanexplicitrelationbetweentheoverdensitymassintheinner,relaxedportions

### Thedoubledistribution

ofcluster-sizedhalosandtheoverdensitymassintheirouterregions,includingtheturnaroundscale. In Pavlidou & Fields (2005), a joint distribution is constructed
to describe the frequency, within a given volume, of collapsed
Thispaperisorganizedasfollows:Insection2,wedevelop structures in specific intervals of mass and local overdensity.
ananalyticformulationforthemost-probableoutermassprofile The overdensity is defined as the density contrast with respect
of galaxy clusters, and we illustrate how mass scaling relations to the average matter-density of the background Universe, calcan be directly derived from this formulation. In section 3, we culatedonasmoothingscaleenclosingmassβm(includingthe
detail the cosmological simulations employed in our study to central structure itself). It is labelled by the corresponding lintest our analytic profile, and describe the methodology used to early extrapolated to the present time overdensity, denoted by
evaluatetheperformanceofouranalyticalmodels.Insection4 δ˜ . Mathematically, then, the distribution provides the comov-
ℓ
wecompareourderivedprofilewiththoseobtainedfromsimu- ing number density of collapsed, relaxed halos with mass belations and test the validity of the associated mass scaling rela- tween[m,m+dm],residingwithinlocaloverdensityintherange
tions.Finally,insection5,wesummarizeourfindings. [δ˜ ,δ˜ +dδ˜ ].Thelinearlyextrapolatedoverdensityfieldδ˜ corre-
ℓ ℓ ℓ ℓ
Articlenumber,page2of10

<!-- Page 3 -->

Korkidis&Pavlidou:Massscalingrelationsfromananalyticuniversalouterclusterdensityprofile
spondstotheoverdensityfieldthatwouldresultifallstructures Simplification1:droppingthestructure-in-structurecorcontinued to grow according to linear theory until the present rection.InEq.(1),thefactor:
time. The mathematical representation for the double distribu- (cid:20) (cid:21) (cid:20) (cid:21)
tionisthefollowing: exp −
δ˜2
ℓ −exp
(δ˜
ℓ
−2δ˜ 0,c(a))2
2S(βm) 2S(βm)
(cid:112)
2πS(βm)
(cid:20) (cid:21) (cid:20) (cid:21)
exp −
δ˜2
ℓ −exp
(δ˜
ℓ
−2δ˜ 0,c(a))2 represents the fraction of points in space that, when smoothed
dm d d n δ˜ ℓ (m,δ˜ ℓ ,β,a)= ρ m m,0 2S(βm (cid:112) ) 2πS(βm) 2S(βm) (1) o ex n p a on s e c n a t l i e al β i m n , th h e av f e rac a ti o o v n er is de t n o s c it o y rr δ˜ e ℓ c . t T fo h r e p r o o i l n e ts o i f n th sp e a s c e e co th n a d t
(cid:104) δ˜ (a)−δ˜ (cid:105) exp (cid:20) − (δ˜ 0,c(a)−δ˜ ℓ )2 (cid:21) (cid:12) (cid:12) a la r r e ge in rt f h a a c n t β p m ar . t I o n f ra a n c d o o l m lap w se a d lk s t t h r e u o c r tu y, re th o is n is a r s e m fe o rr o e t d hi t n o g a s s c t a h le e
× 0,c √ 2π (cid:2) S ℓ (m)−S 2 ( [ β S m (m ) ) (cid:3) − 3 S /2 (βm)] (cid:12) (cid:12) (cid:12) (cid:12)d d m S (cid:12) (cid:12) (cid:12) (cid:12) m . e δ˜ x 0, i c s ( t a e ) n . c F e o o r f sc a a n le a s bs m o u rb c i h ng lar b g o e u r n t d h a a r n y g a a t la th x e y c c o lu ll s a t p e s r e s t o h v e e m rd s e e n lv s e it s y ,
itcanbeshownthatthesecondexponential,alreadyforβ> 1.2
Inthisexpression,δ˜ (a)isthelinearlyextrapolatedoverdensity (for reference, turnaround is predicted to be around β > 1.6)
0,c
ofastructurecollapsingatredshiftz(scalefactora=1/(1+z)), is less than 20% of the first term. Dropping it can significantly
extrapolated to today; δ˜ is the linearly extrapolated overden- simplifythefinalexpression,andwedosofortheremainderof
ℓ
thispaper.
sity of a sphere enclosing the central collapsed structure, ex-
Simplification 2: first differentiate, then convert to nontrapolated to the present time; and S(m) is the variance of the
linear overdensities. As discussed earlier, Eq. (1) depends on
density field when smoothed on a scale that encloses mass m.
the linearly extrapolated overdensity. Strictly speaking, in or-

### OneimplicitassumptionmadeinEq.1isthatforstepsinmass

∆m,thedensityvariance∆S(m)(andhence,thedensitycontrasts der to derive the most probable profile, we must first perform
∆δ˜ (m))areuncorrelated(seeAppendix A,foramoreinvolved achangeofvariablesusingEq.(2)torecastthedoubledistribu-
ℓ tionintermsofδ ,andthendifferentiatetoobtainthevalueofδ
discussion). ℓ ℓ
asafunctionofβmwherethedistributionreachesitsmaximum.

### Theuseoflinearlyextrapolatingoverdensitiesinthederiva-

HoweverthatwouldsignificantlycomplicateboththealgebraintionofEq.(1)isnecessaryforthetreatmentofhalostatisticsto
volved,andthefinalresultingexpression.Instead,wewilladopt
remain analytically tractable. However, before Eq. (1) can betheapproximatepathoffirstcalculatingamost-probableprofile
come predictive for structures residing in the real, non-linear
oflinearlyextrapolatedover-densitiesbydifferentiatingEq.(1),
densityfield,wehavetorelatetheselinearlyextrapolatedoverandthenusetheconversionrelation(eq. (2))toconverttheprodensities to their non-linear counterparts. To this end, we use
file of linearly extrapolated overdensity to profile of non-linear
a relation introduced in Pavlidou & Fields (2005) which connectslinearlyextrapolatedoverdensitiesδ˜ tooverdensitiesδde- overdensity. Physically, this would be equivalent to determining what the most probable density profile around a structure
terminedusingthesphericalcollapsemodel:
thathascollapsedtodaylookedlikeintheearlyUniverse,when
the density field was still in the linear regime; and then, evolv-
(cid:104) (cid:105)
δ˜ a ≈δ˜ c 1−(1+δ a )−1/δ˜ c , (2) ing that early most-probable profile forward in time, using the
spherical collapse model. We expect some inaccuracy - which
wewillevaluatethroughcomparisonwithsimulations-tostem

### InEq.(2),δ˜ isanoverdensitylinearlyextrapolatedtotimea,δ

a a fromthischoice,sincethe“most-probableprofile”isastatistical
istherealoverdensityatthatsametimea,andδ˜ istheoverdenc quantity and does not represent, as a whole, the density profile
sityofacollapsingstructurelinearlyextrapolatedtothetimeof
aroundasinglerealstructure(seediscussionofthe"typicalprocollapse.Thecentralassumptionofthesphericalcollapsemodel
file"inBetancort-Rijoetal.2006,andalsoinBarkana2004for
in that the matter surrounding each overdensity is distributed
adiscussionofsimilarstrategies).
isotropicallyandfollowsradialmotionduringitscollapse.This
Differentiating Eq. (1) with respect to δ˜ , using the simplirelation is universal for all structures and all times of collapse. ℓ
fications discussed above, and setting the result equal to zero

### Eq.(2)hasthecorrectasymptoticbehaviorbothatlowandhigh

returns the following simple expression for the most probable
values of δ , and is accurate to few percent throughout its doa profileofoverdensitylinearlyextrapolatedtothepresentcosmic
main.
time:

### S(βm)

δ˜ =δ˜ (a) . (3)

### Fromthedoubledistributiontothemostprobableprofile ℓ 0,c S(m)

Another way to state the content of Eq.(1) is that, for a given We note that δ˜ (a) is the overdensity of a structure collapsing
0,c
central collapsed structure of mass m at a cosmic epoch a, the at time a, linerarly extrapolated to a = 1 (today). It is related
doubledistributiondescribestheprobabilitydistributionofover- toδ˜ (theoverdensityofastructurecollapsingataextrapolated
c
densities δ˜ around structures of that mass m, in spheres of in- to time a, a universal value for all epochs a) through δ˜ (a) =
ℓ 0,c
creasing mass βm. We can then derive a profile (a function of δ˜ D(1)/D(a),whereD(a)isthelineargrowthfactoratredshifta.
c
βm)ofmaximum-probability(linearlyextrapolated)overdensity Usingthisrelation,wecanrewriteEq.(3)intermsofquantities
- the maximum probability profile. Mathematically, this profile extrapolatedtothetimeofcollapseofthecentralstructurea:
issimplyderivedbydifferentiatingthedoubledistributionwith

### S(βm)

respecttooverdensity,andsettingthatderivativetozero. δ˜ =δ,˜c . (4)
ℓ,a S(m)

### Inwhatfollows,wedescribeaseriesofsimplifications,both

tothedoubledistributionitself,andtotheprofilederivationpro- Finally, we use Eq. (2) to convert the δ˜ to δ (a). This is now
ℓa ℓ
cess,thatresultinasimple,intuitive,closed-formprofile,with- possible,becauseboththelinearlyextrapolatedandthenonlinoutsignificantlossofaccuracy. ear(sphericalcollapse)overdensitiesarecalculatedatthesame
Articlenumber,page3of10

<!-- Page 4 -->


### A&Aproofs:manuscriptno.aanda

timea.Thisyields And thus the sphere of average overdensity ρ = Xρ (a) will

### X m

most probably contain a mass β m ("most probably" because
(cid:104) (cid:105) S(βm) X
δ˜ c 1−(1+δ ℓ )−1/δ˜ c =δ˜ c S(m) . (5) o T u h r en fo , r t m he al m ism ost y p ie r l o d b s a t b h l e e m sc o a s l t in p g ro o b f ab m lea w v i e t r h ag m e ( d i e .e n . s , i m ty o p s r t o c fi o l m e) - .

## X


### Solvingforδ ℓ weget monly,withM 200 ),willbe

1+δ = (cid:34) 1− S(βm) (cid:35)−δ˜ c , (6) m x =β X m= (cid:104) 1−X−1/δ˜ c (cid:105)−1/γ m. (11)
ℓ S(m)

### Thiswillalsoholdfortheturnaroundmass,sincetheturnaround

whichwecanconfirmhasthecorrectasymptoticbehavior,going densityisaconstantforagivencosmologyandagivenredshift
to ∞ when β = 1, and going to 1 (i.e., δ
ℓ
= 0, average matter- (forexample,fortheconcordanceΛCDMcosmologytoday,X =
densityoftheuniverse)whenβ → ∞.Wecanalsoexpressthis 11fortheturnaroundmass).
equationintermsofaveragedensitieswithinasphereincluding
massβm(insteadofoverdensities), M =
(cid:104)
1−X−1/δ˜ c
(cid:105)−1/γ

## M . (12)

ta ta 200
(cid:34)

### S(βm)

(cid:35)−δ˜
c
ρ (β)=ρ 1− , (7) This means that we have a theoretically predictable scaling beavg m S(m) tween M and M ,foranycosmology.Becauseγhasaslight
200 ta
dependenceonmass,thelogarithmicscalingbetweenmassesis
where ρ is the average matter-density of the Universe at the
m expectedtohavesometiltcomparedtothetheM ∝ M line.
desiredredshift. ta 200

### Similarly,wecanderiveascalingbetweenanytwooverden-

We can simplify Eq. (7) even further if the variance of the
sity masses, say m and m , defined as the masses of spheres
density field can be approximated as a power law in mass, X Y
S(m) = m−γ, with −γ = dlnS/dlnm (in Appendix A we ex- with average matter density Xρ m (a) and Yρ m (a), respectively,
providedthatboth X andY arelowerthan200(orwhateverthe
plorethelegitimacyofthisassumption).Withthissubstitution,
thresholdforthevirializedpartoftheclusteristakentobe):
weobtain
ρ

## P

a
u
v
t
g
in
=
w
ρ
o
m
r
(cid:2)
d
1
s,
−
u
β
p
−
t
γ
o
(cid:3)−
th
δ˜ c
ev
=
al
ρ
id
m
i
,0
ty
a−
o
3
f
(cid:2)
a
1
ll
−
th
β
e
−
a
γ
p
(cid:3)−
p
δ˜
r
c
o
.
ximationsweha
(
v
8
e
) m

## X

=   1
1
−

## −Y


## X

−
−
1
1
/
/
δ
δ
˜
˜
c
c   −1/γ m

## Y

. (13)
discussedsofar,theaveragematterdensityofasphereenclosing

### Detailedrecipesforderivingthevaluesofγ andδ˜ usedinthis

mass β times central galaxy cluster mass (so β > 1 always), c
workaregiveninappendicesAandB,respectively.
normalizedtothemeanmatter-densityoftheuniverseatthetime
of observation, is universal, and equal to (1−β−γ)−δ˜ c. For very
large β, this profile asymptotes to 1 (i.e., eventually the matter 3. Simulationsandmethods
density of increasingly large spheres encompassing the cluster
eventuallytendstotheaveragematter-densityoftheUniverseat In this section, we discuss the simulations used for testing the
the time of observation). For β → 1, the profile asymptotes to validity and accuracy of the analytic profile and the predicted
∞, as is the expectation in the spherical collapse model, where mass scalings. We present the criteria we adopted to select our
astructurecollapsestoasingularity.Inpractice,thismeansthat halosample,andthemethodologyweusedtoconstructthemostthevalidityofthis(outer-region)profilewillbreakdownatsome probableaveragemassprofilesforthesehalos.
β>1,tobedeterminedbycomparisonwithsimulations.

### Simulationoverview


### Massscalings


### Tovalidateouranalyticalmodelsagainstrealistic,simulatedav-

Theveryexistenceofauniversalaveragedensityprofiledepen- eragemassprofilesofdarkmatterhalosincluster-sizedsystems,
dent only on β (and not on m) implies that the virial mass will weusedthesamecosmologicalsimulationsasinourpriorwork
scale with any other "constant overdensity" mass that is larger (Korkidisetal.(2023);amoreindepthpresentationofthesimuthanthevirialmassitself.If,then,wetakethevirial(collapsed, lationcanbefoundtherein).Thisincludesthelarge-boxconcorrelaxed) mass of the central cluster to be the usually-assumed danceΛCDMMDPL2simulation(1000h−1 comovingMpcon
m 200 (i.e.,amassenclosedwithinaspherewhichis,onaverage, aside,particlemass1.51×109h−1M ⊙ ),andtheVirgoconsortium
200timesdenserthantheaveragebackground-matterdensityof
simulations,withidentical239.5h−1Mpc-sidedboxesforthree
the Universe), and m X to be a different fixed-overdensity mass differentcosmologies[aconcordanceΛCDM,ano-ΛΩ m =0.3
(amassenclosedinasphere X timesoverdensewithrespectto
(OCDM),anda"standard"Ω
m
=1flatCDM(SCDM)],andparthebackgroundUniverse,withX <200),itisstraightforwardto
ticlemassesequalto6.86×1010h−1M
⊙
fortheΛCDM/OCDM,
derive a scaling between the two. In order to see this we solve and22.7×1010h−1M ⊙ fortheSCDMrespectively.
Eq.(8)forβtoget:
β=

 1−
(cid:32)
ρ
ρ a
(
v
a
g
)
(cid:33)−1/δ˜
c


−1/γ
. (9)
3

## T

.
h
2
e

## . B

pr
u
o
il
fi
d
l
i
e
ng
th
t
a
h
t
e
w
pr
e
ofi
d
l
e
e
r
s
ived in Section 2, described the most
m
probable profile of the average matter density within concen-
So now any constant overdensity criterion ρ = Xρ (a) will tric spheres of increasing enclosed mass, as a function of that

### X m

yield a specific value for β (a value independent of m, and so enclosed mass. To compare the analytical predictions against
thesameforclustersofallmasses): the simulated data, we analyzed the matter distribution around
1000/900 randomly selected galaxy-cluster-sized (M ≥ 8×
β X =
(cid:104)
1−X−1/δ˜ c
(cid:105)−1/γ
. (10) 1013 M ⊙ )darkmatterstructuresfromeachoftheMDP
20

## L

0
2/Virgo
Articlenumber,page4of10

<!-- Page 5 -->

Korkidis&Pavlidou:Massscalingrelationsfromananalyticuniversalouterclusterdensityprofile
simulations,respectively.Giventhatinhierarchicalstructureformationcosmologiesthehalodistributionfollowsamassfunction
inwhichlargerstructuresaremorerare,duringoursamplingwe
divided the halo catalog in 30 mass bins, and from each bin,
we selected 40 random clusters. We segmented the region surrounding the center of each galaxy cluster into 500 concentric
spheresextendingupto10×R inradius,ensuringthateach
200,m
halo was contained within the simulation’s boundaries. Within
each sphere, we computed the enclosed mass, and, dividing by
thevolumeofthesphere,thecorrespondingdarkmatterdensity.
Thechosennumberandsizeofbinsweresufficientlylargetoaccuratelyrepresenttheprofilesatallenclosedoverdensitymasses
for both group and cluster-sized halos. Finally, we normalized
the enclosed mass for each individual halo profile to its virial
mass,specificallyM .
200

## Results


### Massdensityprofileofsimulatedhalos

We first confirmed that the type of profiles examined here do
cluster around a most probable behavior which our analytical
profile aims to model. Figure 1 presents the compiled profiles
from the MDPL2 simulation at z = 0. The colorbar indicates
thedensityoflinesontheplot.Thisvisualizationclearlyshows
thatmostprofilestendtoconvergearoundacommonprofile.In
Fig.1theindependentvariableM˜ =M/M isequivalenttoβin
200
theanalyticprofileofEq.8,assumingthatM isareasonable 200
approximationofthetruerelaxedmassmofthecentralcluster.
104
103
102
101
100
100

## M=M/M 200

e
¯ρ/)M<(ρ m
e
102
101
100
ytisneDelfiorP
probability density function (PDF) of densities in the bin, and
subsequentlyidentifyingthedensityforwhichthePDFismaximum.Theresultingmodeprofileisdepictedbytheredsolidline
in Fig. A.1, closely tracking regions with high profile density,
asanticipated.
103
102
101
100
Fig.1.Averagematterdensity(inunitsofthebackground-Universeaveragematterdensity)withinconcentricspheresaroundMDPL2z = 0
cluster-sizedhalos,asafunctionofmassthatisenclosedineachsphere.
Thecolorscaleencodesthenumberoflinesperpixelontheplot.The
enclosedmassisnormalizedtoM ,soallprofilesconvergeatanav-
200
eragedensity200perthedefinitionofM .Theredsolidlinedepicts 200
theprofilemode.Theindependentvariable M˜ = M/M isequivalent
200
toβintheanalyticprofileofEq.8.

### To formally capture and represent this pattern, we grouped

these normalized profiles into 40 linear mass bins, from 0 to
4×M .Foreachbin,wedeterminedthemostprobablevalue 200
(mode)ofthedensity.ThiswasachievedbyemployingaGaussiankerneldensityestimator1(Virtanenetal.2020)tomodelthe
1 For the bandwidth determination the algorithm that we employed
usedScott’srule(Scott1992).
m¯ρ/)M<(ρ
e
z=0
z=1
2 100
×
100
6 × 10− 1 1.0 1.5 2.0 2.5 3.0 3.5

## M=M/M200

e
citylanaρ/)M<(ρ
e
Fig.2.Performanceofouranalyticdensityprofilefordifferentredshifts.
Upper panel: most probable (mode) average matter density within
spheresofenclosedmass M asafunctionof M (normalizedto M ;
200
M˜ isequivalenttoβinEq.(8)),fromouranalyticresult(Eq.8,dashed
lines),andfromtheMDPL2simulationhalos(solidlines;theshaded
regionincludes68%ofthedensitiesPDF),forz = 0(blue)andz = 1
(green).Lowerpanel:ratioofMDPL2overanalyticmodeprofileasa
functionofenclosedmass.Inthebottompanel,theratioofthemodeto
theanalyticprofilesisdisplayed.
We next tested the extent to which our analytic profile
matchesthemostprobableprofileseeninsimulations.InFig.2,
weoverlaytheanalyticalprofilewiththemodeoftheprofilesderivedfromtheMDPL2simulation.Differentcurvecolorsstand
fordifferentredshiftsofourhalosamples.Fortheanalyticalprofile,weincorporatethecosmologicalparametersfromthesimulation(Ω m ,Ω Λ,h 0 ,n s )andthemedianvalueofM 200 forthehalo
sample (6.3×1014 M for z = 0 halos and 1.2×1014 M for
z = 1). The lower pan ⊙ el compares the simulated and analy ⊙ tical
profilesbyexaminingtheirratio.
The analytical profiles, developed using the spherical collapse model to evolve linearly extrapolated overdensities into
the non-linear regime, tend to infinity as the enclosed mass approaches M 2. For M˜ ≡ β ≥ 1, the analytical profile shows 200
an excellent alignment with the mode profile; fluctuations are
within 15%. The profile exhibits little variation with redshift,
beyondwhatisencodedintheoverallincreaseofaveragebackgroundmatterdensitywithincreasingredshift.

### Simulationsconsistentlyshowthatthedensityprofilearound

clustersexhibitsnear-universalcharacteristicswhennormalized
2 Under our assumptions, the model assumes virialization for simulatedclusterswhenthedensityis200timesthebackgroundmassdensity,aconsequenceofemployingsphericaltophatthresholds;forarecentdiscussionseeDelos(2023).
Articlenumber,page5of10

<!-- Page 6 -->

A&Aproofs:manuscriptno.aanda
102
101
1.00 1.25 1.50 1.75 2.00 2.25

## M

e
¯ρ/)M<(ρ m
e
effectsthatpartlycontributetotheoffsetobservedinFig. 3be-
MedianM200=1.3E+14, γ=0.4 tweenthesolidandthedashedbluecurves.
MedianM200=5.0E+14, γ=0.5 This effect would also be exaggerated by the underlying
MedianM200=1.7E+15, γ=0.6 assumption in Eq. 1 that steps in enclosed mass result in uncorrelatedcorrespondingstepsinenclosedunderdensity(implementedformallybytheadoptionofasharp-in-kfilterforS(m);
seealsodiscussioninAppendixA).Thisassumptionisrequired
fortheexcursion-setformalismusedtoderiveEq.1tobestrictly
applicable; however, in the analysis of simulations, successive
stepsinoverdensitycorrespondingtosuccessivestepsenclosed
mass are correlated (they are calculated using a top-hat, rather
than a sharp-in-k, filter). The extent of this mismatch would be
dependentonthemassaccretionrate.
Finally,anotherfactortoconsideristhefiniteaccuracywith
whichwedeterminethemodedensityineverysphereofagiven

### M˜:themodeprofileremainsreasonablywithinuncertaintiesof

thesimulatedmodeacrossmassbins,simulations,andredshifts.
Fig.3.Mostprobableaveragematter-densityprofilefromouranalytical
model (dashed lines) and MDPl2 (solid lines), for different ranges of 4.2. Massscalings
clustermasses M .Theindependentvariable M˜ isequivalenttoβin
200
Eq.(8).
16.0
againstaconstantoverdensityradiusormassrelativetothebackground.ThisbehaviorisreplicatedinFigure3,where,withsolid 15.5
lines, we plot the mode density profiles of MDPL2 clusters at
z = 0, against their enclosed mass in concentric spheres of increasingradius.Differentcolorscorrespondtodifferentaverage
15.0
masses of the halo sample. The consistency of the profiles betweendifferentmassbinsisevenstrongerinsimulationsthanin
ouranalyticalprofiles(shownwithdashedlines),withdeviations
14.5
betweensimulationsandanalyticprofileforthethesmallerand
largermassbinsreaching25%.Thisvariationoftheanalyticprofilewithclustermassoriginatesinthemilddependenceofγon
mass(eachprofileinthefigurehasadifferentγvalueasshown 14.0
14.0 14.5 15.0 15.5
inthelegend;also,seeappendixAandFig.A.1).Wehavecon-

### Log M [M ]

firmed that the expected mild mass-dependence of the analytic 200 (cid:12)
mode profile is real, and not a result of our approximations: it
persistswhenthefullexpressionforS(m)isusedratherthanthe
power-law approximation: the deviation between the two profilesisnegligiblefortherangeofM˜ consideredhere,whenγis
takentobeequalto−dlnS/dlnm| m=M200 (aswedoinallcases,usingthemedianM ofoursampleeachtime).Formuchhigher
200
M˜, of course, when the transfer function T(k) → 1, S(m) does
asymptotetoapower-law(seeEq.A.3),andthefulluniversality
ofthemodeprofileisrecovered;howeverthisbecomesrelevant
formassscalesmuchlargerthanthoseconsideredinthispaper.
The dependence of the mode profile also persists if we replace
the approximation of Eq. (2) with the more accurate but also
morecumbersomeEq.(8)ofSheth&Tormen(2002),alsoused
byPradaetal.(2006b).
The lack of such dependence in simulations is plausibly an
effectofthesomewhatfuzzycorrespondencebetweenM and
200
the true "collapsed mass" entering the analytical mode profile.

### Even under the assumption of spherical symmetry, the SCM is

onlyapplicableforshellsthathaveneverundergoneshellcrossing.Inthiscontext,theappropriatecollapsedmassissomewhat
ambiguous. Here we have taken it to be M . However, if one
200
weretorequirethatallmassthathasundergoneshellcrossingis
consideredtobepartofthecollapsedmass,thenthesplashback
mass (Diemer & Kravtsov 2014; Adhikari et al. 2014; Diemer
etal.2017)shouldalsobeconsidered.Thisislikelyoneofthe
]

## M[


## M

goL
lautca,at
(cid:12)
mode
16thand84thpercentiles

### Xta=11, eq.11

Fig. 4. Correlation between turnaround mass M and collapsed ta,actual
massM fortheMDPL2clustersampleatz = 0.Theredsolidline 200
depictsthetheoreticalscalingrelationofEq.11.Thebluesolidlinerepresents the mode value of the blue points in bins of M . The blue
200
shadedregioncorrespondstothe16thand84thpercentiles
We now turn to evaluate the performance of our scaling relation between different overdensity masses (Eq. 11)
for our halo samples. As detailed in our prior works (Korkidis et al. 2020, 2023), the kinematically-defined turnaround
mass M (the mass enclosed within the kinematicallyta,kinematic
identified turnaround radius) corresponds well to an overdensity mass, consistent with the prediction of the spherical collapsemodel.ForconcordanceΛCDMandz = 0,sphericalcollapse predicts that X = 11. We also set the collapsed mass
ta
m = M . For each halo, employing Eq.(11), we can predict
200
theturnaroundmassM ≡M fromitsM and
ta,predicted 11,predicted 200
also calculate its actual mass within that overdensity (X = 11,

## M ≈M ).

11,actual ta,actual
Wefirsttestthatsuchascalingrelationdoesexistinsimulations,forthecasethatisofmostinteresttous(scalingofM
200
withtheturnaroundmass).InFig.4weplottheturnaroundmass
ofeachclusterinourMDPL2sample,M ,asafunctionof
ta,actual
itsM .Themodealongwiththe16thand84thpercentilesof
200
thisscalinginbinsofM isshownwiththesolidbluelineand
200
Articlenumber,page6of10

<!-- Page 7 -->

Korkidis&Pavlidou:Massscalingrelationsfromananalyticuniversalouterclusterdensityprofile
0.014
0.012
0.010
0.008
0.006
0.004
0.002
0.000
0 50 100 150
%fractionaldifference
ytisnedytilibaborP

### M VsM M VsM

ta,actual ta,predicted ta,actual ta,predicted

## Mdpl2

0.020
0.015
0.010
0.005
0.000
0 50 100 150
%fractionaldifference
ytisnedytilibaborP
MedianM200=1.3E+14
MedianM200=5.0E+14

### MedianM200=1.7E+15

Fig.5.Probabilitydensityofthefractional(percentage)differencebetweentheturnaroundmass(here M )predictedfromthescalingrelation
11
ofEq.(11)anditsactualvalue,forthefullMDPL2simulatedclustersampleatz = 0(leftpanel),andforhalosubsamplesofdifferentmedian
M (rightpanel).Ineachcase,thesolidlineshowsaGaussiankernelestimatoroftheprobabilitydensityfunction,andtheverticallinemarks
200
themodeoftheerrordistribution.ThescalingrelationtendstooverpredictM forlowerM andunderpredictitforhigherM .
11 200 200
Mδ,actualVsMδ,predicted
δ=150 δ=100 δ=50
0.125
0.100
0.075
0.050
0.025
0.000
0 10 20 30 0 20 40 60 0 20 40 60 80
%fractionaldifference
ytisnedytilibaborP
Fig.6. Performanceofourscalingrelationformassescorrespondingtodifferentoverdensityvaluesδ(equivalenttoXinEq.11)intheMDPL2
sample. The solid curves and vertical lines are the same as in Fig. 5.As δ decreases (left to right), the most probable offset decreases, while
high-errortailsbecomemorepronounced.Bothbehaviorscanbetracedtotheperformanceoftheanalyticprofile(seetextfordiscussion).
0.020
0.015
0.010
0.005
0.000
0 50 100 150
ytisnedytilibaborP

### Mta,actualVsMta,predicted

VirgoLCDM VirgoOCDM VirgoSCDM
0 50 100 150 0 50 100 150
%fractionaldifference
Fig. 7. Performance of our scaling relation for three different Virgo simulations cosmologies. All panels correspond to z = 0 snapshots. The
medianM ofthehalosamplesare1.2×1014M forVirgoLCDM/VirgoOCDMand1.7×1014M forVirgoSCDM.Dashedredlinescorrespond
200 ⊙ ⊙
to±15%error.
theshadedregion,respectively,andtheydoconfirmthatatight To further quantify the performance of our scaling we plot,
scalingbetweenthetwomassesisindeedpresentintheMDPL2 withthehistogramintheleftpanelofFigure5,thefractionaldifsample,althoughoutliersdoexist.Forcomparison,weoverplot, ference,asapercentage,betweentheturnaroundmassM
11,actual
withtheredline,themodescalingpredictedbyEq.(11),andit measured from the simulation data, and the turnaround mass
isalreadyobviousthattheanalyticmodescalingisinexcellent M predicted by our scaling relation using M as in-
11,predicted 200
agreementwiththemodescalingseeninsimulations. put.Thehistogramhasapronouncedpeaknearzero,suggesting
thatthescalingrelationpredictstheturnaroundmasswell.How-
Articlenumber,page7of10

<!-- Page 8 -->


### A&Aproofs:manuscriptno.aanda

ever,thedistributionofresidualsdoesfeaturealongtail,sothe istighteraroundzero-aresultoftheanalyticprofileperforming
meanofthisdistributionhasanon-negligiblebias(upto20%). betterawayfromitsdivergencepointatthecollapsemass.
Anotherfactoraffectingtheperformanceofthescalingrelationisthemassrangeofthesample.Thisisexploredintheright
panelofFigure5.Here,differentcolorscorrespondtosubsamplesofdifferentmassranges,withthemedianmassineachsubsampleshowninthelegend.Althoughthequalitativefeaturesof 0.0175
thehistogramsremainconsistent,weobserveasystematictrend
from negative to positive offsets of the peak of the distribution 0.0150
asthemediansamplemassincreases.Theabsolutevalueofthis
0.0125
offsetisupto15%fortherangeofmassesconsideredhere.This
behaviorisanticipatedbasedontheperformanceoftheanalytic 0.0100
profilefordifferentsamplemassrangesseeninFig.3.
0.0075

### In Fig. 6 we evaluate again the performance of our mass

scaling for different values of overdensity δ at which the mass 0.0050
is evaluated (corresponding to X in Eq. 11). Each panel corresponds to a different value of δ, which decreases from left to 0.0025
right,andwhichisdisplayedinthelegendofeachpanel.Inall
0.0000
scenarios,thedistributionpeaksat<10%error.Themostprob- 0 50 100 150
able error increases with increasing overdensity, a behavior we %fractionaldifference
anticipate due to the analytic profile diverging at the assumed
collapse overdensity δ = 200. However, the high-error outlier
tailsdecreasewithincreasingoverdensity,abehavioralsoanticipated from Fig. 1: closer to M individual profiles are more 200
clusteredaroundthemodeprofile.Forthisreason,deviationsof
individualoutliersfromtheanalyticmodeprofile,andtheassociated deviations from the mass scaling derived from the mode
profile,aremorepronouncedforhighermassscales(loweroverdensityvalues).
The same analysis for X ≡ X (turnaround mass) is then
ta
conductedinFigure7forhalosamplesfromthreeVirgosimulations,eachcorrespondingtoadifferentsetofcosmologicalparameters:Ω
m

## =0.3,Ω


## Λ

=0.7(VirgoLCDM);Ω
m

## =0.3,Ω


## Λ

=0
(VirgoOCDM);andΩ
m

## =1,Ω


## Λ

=0(VirgoSCDM).Inallcases,
weanalyzedz = 0snapshots.Thebehaviorinthefirsttwocosmologies,featuringthesamedarkmattercontentatthepresent
cosmicepoch,isverysimilar.Thisisconsistentwithourfindings
both analytically in the context of the spherical collapse model
(Pavlidou et al. 2020) and in simulations (Korkidis et al. 2023)
thatthebehavioronturnaroundscalesatsomespecificredshift
dependsprimarilyontheaveragematterdensityatthatsameredshift. The mild difference of the most-probable error compared
totheMDPL2sample(Fig.5)likelystemsfromthesmallerbox
sizeintheVirgosimulations,whichresultstoasmallermedian
massofthehalosample.AsalsoseeninFigure5,inthisrangeof
halomassesthescalingtendstooverpredicttheturnaroundmass
(negative mode error). In the VirgoSCDM box, where the medianmassofthesampleislarger,theerrormodeisalmostzero,
andamorepronouncedhigh-errortailispresent,alsoconsistent
with our findings for different cluster mass ranges in MDPL2.

### Itwouldappearthatsamplemassdrivestheperformanceofthe

scaling relation of Eq. (11), more than the variation in cosmologicalparameters,whichappeartobeaccountedforsufficiently
bythemodel.

### Finally, we also test the performance of Eq. 13 - a scaling

relationship between any two overdensity masses m and m . X Y
We employ this scaling relation to estimate the actual value of
the turnaround mass M (X = 11) using an overdensity
ta,actual
massM (Y=100),andplotthedistributionofitspercentage
100
difference from M in Fig. 8. In the same figure, we also
ta,actual
overplot the same distribution for the prediction derived from
Eq.(11).Thecomparisonindicatesanalmostidenticalposition
forthepeakofthedistributions;however,whentheturnaround
massisderivedfromM ratherthanM theerrordistribution
100 200
ytisned
ytilibaborP

### M VsM

ta,actual ta,predicted
Eq.11&M200

### Eq.13&M100

Fig.8.ComparisonbetweenthescalingrelationsdelineatedinEq.13
andEq.11.Thebluehistogramdepictedhereincorrespondstothatof
theleftpanelinFig.5.Superimposedonthishistogramisthefractional
differencebetweentheactualvalueofM (X = 11)anditspredicted
ta
counterpartassumingapriorknowledgeofM (thatis,ifwesetY= 100
100).

## Conclusions

In this study, we derived a theoretical model for the mostprobable outer average density profile of large galaxy clusters
asafunctionofenclosedmass,usingexcursionsettheory.This
model,basedonGaussianearlyuniversestatisticsandthespherical collapse framework, has two parameters, γ and δ˜ , both of c
whichcanbeanalyticallyderivedfromthecosmologicalparameters (Ω m , Ω Λ, and power spectrum slope n), and the median
virialmassofthesampleunderconsideration.Wecomparedour
profilewithprofilesaroundgalaxy-cluster–sizedhalosinΛCDM
simulations,andfoundgoodagreementacrossmassrangesand
redshifts.
Fromtheprofilewederivedascalingrelationthatlinksdifferentoverdensitymasses,andfoundthatitperformswellwith
the the peak of the error distribution remaining below 15% for
allcosmologies,samplemasses,andoverdensitieswetested.We
have traced residual inaccuracies of the scaling relation to two
factors.
The offset from zero of the maximum of the error is dependent on the exact cluster mass range considered. In particular, the mode profile in simulations appears to be more universal(similaracrossmassranges)thantheanalyticmodelpredicts. This is plausibly an effect of an imperfect identification
between the collapsed mass m of the analytic profile and the
overdensity-200 mass M in simulated clusters, leading to a 200
cross-contaminationofmassranges.
The tail of the error distribution tends to grow as the mass
scale we consider grows (or, equivalently, as the overdensity
wherethemassiscalculateddecreases).Thisisduetheincreasing spread of the profile distribution with increasing scale. As
aresult,massesatoverdensitiescloserto200(say,150or100)
scalemoretightlywith M thantheturnaroundmass(M for
200 11
z=0inconcordanceΛCDM).
Articlenumber,page8of10

<!-- Page 9 -->

Korkidis&Pavlidou:Massscalingrelationsfromananalyticuniversalouterclusterdensityprofile
Our analytical model demonstrates the existence, in princi- Lacey,C.&Cole,S.1993,MNRAS,262,627
ple,ofascalingbetweenanytwooverdensitymasses,dependent Lee,J.2018,ApJ,856,57
oncosmologyandredshift,anditprovidesareasonableapprox- Lee,J.&Li,B.2017,ApJ,842,2
Lopes,R.C.C.,Voivodic,R.,Abramo,L.R.,&Sodré,Laerte,J.2019,J.Cosimation to this scaling directly from these parameters. A fit of
mologyAstropart.Phys.,2019,026
theparameterγtoaparticularsimulatedsampleofclusterswith More,S.,Diemer,B.,&Kravtsov,A.V.2015,ApJ,810,36
massesintherangeofinterestcanprovideanevenmoreaccurate More,S.,Miyatake,H.,Takada,M.,etal.2016,ApJ,825,39
scalingshouldoneberequired.Wehaveconfirmedthatsuchfits Nasonova,O.G.,deFreitasPacheco,J.A.,&Karachentsev,I.D.2011,A&A,

## 532,A104

returnvaluesofγthatalwaysfallwithinthosepredictedtheoret-

### Navarro,J.F.,Frenk,C.S.,&White,S.D.M.1996,ApJ,462,563

ically (see appendix A and Fig. A.1) for masses in the galaxy-
O’Neil,S.,Barnes,D.J.,Vogelsberger,M.,&Diemer,B.2021,MNRAS,504,
clusterrange. 4649

### Pavlidou,V.&Fields,B.D.2005,Phys.Rev.D,71,043510

Acknowledgements. Wewouldliketothanktheanonymousrefereeforhiscon-
Pavlidou,V.,Korkidis,G.,Tomaras,T.N.,&Tanoglidis,D.2020,A&A,638,
structivereport.WeacknowledgesupportbytheHellenicFoundationforRe-

## L8

search and Innovation under the “First Call for H.F.R.I. Research Projects to
Pavlidou,V.&Tomaras,T.N.2014,J.CosmologyAstropart.Phys.,2014,020
support Faculty members and Researchers and the procurement of high-cost
PlanckCollaboration,Ade,P.A.R.,Aghanim,N.,etal.2013,A&A,550,A129
researchequipmentgrant”,Project1552CIRCE(GK,VP);andbytheFoun-

### Prada,F.,Klypin,A.A.,Simonneau,E.,etal.2006a,ApJ,645,1001

dationofResearchandTechnology–HellasSynergyGrantsProgram(project

### Prada,F.,Klypin,A.A.,Simonneau,E.,etal.2006b,ApJ,645,1001

MagMASim, VP). The research leading to these results has received funding

### Ruppin,F.,Mayet,F.,Pratt,G.W.,etal.2018,A&A,615,A112

fromtheEuropeanUnion’sHorizon2020researchandinnovationprogramme

### Scott,D.W.1992,MultivariateDensityEstimation

undertheMarieSkłodowska-CurieRISEaction,GrantAgreementn.873089

### Sheth,R.K.&Tormen,G.2002,MNRAS,329,61

(ASTROSTAT-II).TheCosmoSimdatabaseusedinthispaperisaserviceby
Sifón,C.,Battaglia,N.,Hasselfield,M.,etal.2016,MNRAS,461,248
theLeibniz-InstituteforAstrophysicsPotsdam(AIP).TheMultiDarkdatabase
Tavio,H.,Cuesta,A.J.,Prada,F.,Klypin,A.A.,&Sanchez-Conde,M.A.2008,
wasdevelopedincooperationwiththeSpanishMultiDarkConsoliderProject
arXive-prints,arXiv:0807.3027
CSD2009-00064.TheauthorsgratefullyacknowledgetheGaussCentreforSu-
Virtanen,P.,Gommers,R.,Oliphant,T.E.,etal.2020,NatureMethods,17,261
percomputinge.V.(www.gauss-centre.eu)andthePartnershipforAdvancedSupercomputinginEurope(PRACE,www.prace-ri.eu)forfundingtheMultiDark
simulationprojectbyprovidingcomputingtimeontheGCSSupercomputerSuperMUC at Leibniz Supercomputing Centre (LRZ, www.lrz.de). The Bolshoi
simulationshavebeenperformedwithintheBolshoiprojectoftheUniversityof
CaliforniaHigh-PerformanceAstroComputingCenter(UC-HiPACC)andwere
runattheNASAAmesResearchCenter.TheVirgoConsortiumsimulationsused
inthispaperwerecarriedoutbytheVirgoSupercomputingConsortiumusing
computersbasedatComputingCentreoftheMax-PlanckSocietyinGarching
andattheEdinburghParallelComputingCentre.Thedataarepubliclyavailable
atwww.mpa-garching.mpg.de/galform/virgo/int_sims.Throughoutthisworkwe
reliedextensivelyonthePYTHONpackagesNumpy(Harrisetal.2020),Scipy
(Virtanenetal.2020)andMatplotlib(Hunter2007).

### References

Adhikari,S.,Dalal,N.,&Chamberlain,R.T.2014,J.CosmologyAstropart.

### Phys.,2014,019


### Amanullah,R.,Lidman,C.,Rubin,D.,etal.2010,ApJ,716,712

Andrade-Santos,F.,Pratt,G.W.,Melin,J.-B.,etal.2021,ApJ,914,58

### Armitage,T.J.,Kay,S.T.,&Barnes,D.J.2019a,MNRAS,484,1526

Armitage, T. J., Kay, S. T., Barnes, D. J., Bahé, Y. M., & Dalla Vecchia, C.
2019b,MNRAS,482,3308

### Bahar,Y.E.,Bulbul,E.,Clerc,N.,etal.2022,A&A,661,A7

Bardeen,J.M.,Bond,J.R.,Kaiser,N.,&Szalay,A.S.1986,ApJ,304,15

### Barkana,R.2004,MNRAS,347,59

Betancort-Rijo,J.E.,Sanchez-Conde,M.A.,Prada,F.,&Patiri,S.G.2006,

### ApJ,649,579


### Bond,J.R.,Cole,S.,Efstathiou,G.,&Kaiser,N.1991,ApJ,379,440

Capozziello,S.,Dialektopoulos,K.F.,&Luongo,O.2019,InternationalJournal
ofModernPhysicsD,28,1950058
Carroll,S.M.,Press,W.H.,&Turner,E.L.1992,ARA&A,30,499
Delos,M.S.2023,arXive-prints,arXiv:2311.17986

### Diemer,B.2023,MNRAS,519,3292


### Diemer,B.&Kravtsov,A.V.2014,ApJ,789,1

Diemer,B.,Mansfield,P.,Kravtsov,A.V.,&More,S.2017,ApJ,843,140
Einasto,J.1965,TrudyAstrofizicheskogoInstitutaAlma-Ata,5,87

### Eisenstein,D.J.&Hu,W.1998,ApJ,496,605

Eisenstein,D.J.,Zehavi,I.,Hogg,D.W.,etal.2005,ApJ,633,560

### Fong,M.,Han,J.,Zhang,J.,etal.2022,MNRAS,513,4754

Gruen,D.,Seitz,S.,Brimioulle,F.,etal.2014,MNRAS,442,1507
Gupta,N.&Reichardt,C.L.2020,ApJ,900,110

### Gupta,N.&Reichardt,C.L.2021,ApJ,923,96

Harris,C.R.,Millman,K.J.,vanderWalt,S.J.,etal.2020,Nature,585,357
Hilton,M.,Hasselfield,M.,Sifón,C.,etal.2018,ApJS,235,20
Hilton,M.,Sifón,C.,Naess,S.,etal.2021,ApJS,253,3

### Ho,M.,Rau,M.M.,Ntampaka,M.,etal.2019,ApJ,887,25

Hunter,J.D.2007,ComputinginScienceandEngineering,9,90

### Karachentsev,I.D.&Nasonova,O.G.2010,MNRAS,405,1075


### Komatsu,E.,Smith,K.M.,Dunkley,J.,etal.2011,ApJS,192,18

Korkidis,G.,Pavlidou,V.,&Tassis,K.2023,arXive-prints,arXiv:2304.14434
Korkidis,G.,Pavlidou,V.,Tassis,K.,etal.2020,A&A,639,A122
Articlenumber,page9of10

<!-- Page 10 -->


### A&Aproofs:manuscriptno.aanda


### AppendixA: Densityfieldvariance

In deriving Eq. (8) from Eq. (7) we assumed that, for a limited
rangeofmasses,S(m)canbeapproximatedbyapowerlaw,that
0.45
is −

### S(βm) 0.50

≈β−γ (A.1) −

### S(m)

where
0.55
−
dlnS
−γ= . (A.2)
dlnm
0.60

### Here, we evaluate the validity of this assumption, and we −

providearecipefortheevaluationofγ.Thevarianceoftheden- 1014 1015
sityfieldisgivenby m[M ]
(cid:12)
(cid:90) k(m)
(cid:82)k(m)

### T2(k)kn+2dk

S(m)= k2dk|δ |2 =σ2 k=0 (A.3)
k=0
k 8(cid:82)k(m8)
T2(k)kn+2dk
k=0

### Inthisequation,wehavemadetwoassumptions.First,thatright

after matter-radiation equality, ⟨|δ |2⟩ can be simply described
k
in terms of a power-law in k modified by a transfer function,
⟨|δ |2⟩ ∝ T2(k)kn.Second,thatthewindowfunctionforthecalk
culationofthevarianceissharpink−space.Thisassumptionis
necessary for random-walk formalism (used to derive Eq. 1) to
bestrictlyapplicable:each"step"inthetime-likevariable(here
S(m)) should produce a step in the space-like variable (here,
theoverdensitycorrespondingtothemassscalem)thatiscompletelyindependentfromthepreviousstep.Thisrequiresthatthe
k-modesproducingachangeinthespacelikevariablenotappear
in any of the previous steps. A sharp-in-k window function enforces this condition. For a more extensive discussion on this
assumptionanditsconsequencesseeBondetal.(1991);Lacey
&Cole(1993);Pavlidou&Fields(2005).

### Thevarianceofthefieldhasbeennormalizedtothepresent

time at scale of 8 comoving Mpc (σ ). For T(k) we adopt the 8
fitting formulae of Bardeen et al. (1986) for the adiabatic cold
darkmattertransferfunction(Eq.G3).Wehaveverifiedthatusingotherapproximations(e.g.,perEisenstein&Hu1998)does
notaltersubstantiallyanyoftheresultspresentedinthiswork.
Toobtaink(m),weintegratethesharp-in-kwindowfunction
overallspaceandmultiplyingbyρ weobtain
m,0
(cid:32) 6π2ρ (cid:33)1/3
k (m)= m,0 . (A.4)
c m

### Then,fromEq.(A.3),wecancalculateS(m)anditslogarithmic

slope,whichweplotinFig.A.1.Clearly,thisslopeisnotconstant over the range of masses of interest (as it should be for a
power law), but it does not vary wildly either. As a result, for
asmallrangeofmasses,S(m)canbeapproximatedreasonably
wellbyapowerlaw.Ofcourseasm → ∞thetransferfunction
T → 1 and S(m) asymptotes to ∝ m−(n+3)/3, but this occurs on
scalesmuchlargerthanthoseofinterestinthiswork.
AppendixB: Calculatingδ˜
c
Foragivencosmology,thatis,asetofΩ
m
,Ω Λ,wefirstcalculate
theparameters
ω=Ω Λ/Ω m (B.1)
mgold/Sgold
Fig.A.1.VariationinthelogarithmicslopeofthedensityfielddispersionS fordiversevaluesofthecollapsedmassm.Thefunction’sminimalcurvatureindicatesnear-consistencywithastraightlineacrosseach
orderofmagnitudeinmass.Thispatternsuggeststhatapproximating
thevarianceofthedensityprofilewithapower-lawmodelcouldbea
plausibleapproach.
and
ϕ=(Ω
m

## +Ω Λ−1)/Ω

m

## . (B.2)

Note that for a flat cosmology, ϕ = 0, while for a cosmology
withoutΛ,ω=0.
Nowleta bethe(evolving)radiusofaninitiallyoverdense
p
region(densityperturbation)normalizedsothat,hadthespecific
regionbegunitsevolutionatthesamedensityasthebacground
Universe,a atthepresentcosmicepochwouldhavebeenequal
p
to 1. The size of this perturbation at turnaround, a , that is
pta
reaching collapse today (i.e. at scale factor of the background
Universe equal to 1; note that this structure must have reached
turnaroundatsometimeinthepast),canbefoundthrough(e.g.,
Pavlidou&Fields2005;Pavlidouetal.2020)
√ √
(cid:90) 1 ydy (cid:90) 1 zdz
0 (cid:112) ωy3−ϕy+1 =2a3 p / ta 2 0 (cid:113) ωa3 z3−(ωa3 +1)z+1 .
pta pta
Then, the extrapolated overdensity δ˜ to the time of collapse3
c
willbe(Pavlidou&Fields2005):
3Ω [(ωa3 +1)/a −ϕ]
δ˜ = m pta pta D(a ), (B.3)
c 0
2
where D(a ) is the linear growth factor for the present cosmic
0
epocha =1(Carrolletal.1992)
0
(cid:112) (cid:90) 1 (cid:34) x (cid:35)3/2
D(a )=Ω−1/2 1+ω−ϕ dx. (B.4) 0 m 1+ωx3−ϕx
0
Overall, the variations in δ˜ in different cosmologies are small.
c
For concordance ΛCDM (Ω m = 0.3, Ω Λ = 0.7), δ˜ c = 1.6757.
ForSCDM(Ω
m

## =1,Ω


## Λ

=0),δ˜
c
=1.6865.
3 In the case considered, which is of a structure achieving collapse
today,thattimeisthetimeofscalefactorequalto1.
Articlenumber,page10of10

## Tables

**Table (Page 5):**

| e |
|---|
|  |


**Table (Page 7):**

|  |  |  | MDPL2 |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 7):**

|  |  |  |  | MedianM200=1.3E+14 MedianM200=5.0E+14 MedianM200=1.7E+15 |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 7):**

|  |  |
|---|---|
|  |  |


**Table (Page 7):**

|  |  |  | δ=150 |
|---|---|---|---|
|  |  |  |  |


**Table (Page 7):**

|  | δ=100 |
|---|---|
|  |  |


**Table (Page 7):**

|  |  |  | VirgoLCDM | VirgoLCDM |  |
|---|---|---|---|---|---|
|  |  |  |  |  | VirgoLCDM |
|  |  |  |  |  |  |


**Table (Page 7):**

|  |  | VirgoOCDM |
|---|---|---|
|  |  |  |


**Table (Page 7):**

|  | VirgoSCDM |
|---|---|
|  |  |


**Table (Page 8):**

|  |  |  |  |  |  | Eq.11&M200 Eq.13&M100 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
