---
title: "Cost Optimization Strategies"
original_file: "./Cost_Optimization_Strategies.pdf"
document_type: "guide"
conversion_date: "2025-11-29"
topics: ["chain-of-thought", "fine-tuning", "multimodal"]
keywords: ["spin", "cid", "waves", "mode", "current", "wave", "coupling", "right", "magnet", "left"]
summary: "<!-- Page 1 -->

Single-mode spin-wave laser driven by spin-orbit torque

### J. Duine1,2

1Institute for Theoretical Physics, Utrecht University, 3584CC Utrecht, The Netherlands
2Department of Applied Physics, Eindhoven University of Technology,

### P.O. Box 513, 5600 MB Eindhoven, The Netherlands

3Fachbereich Physik, Universita¨t Konstanz, D-78457 Konstanz, Germany and
4Institute for Advanced Study in Physics, Zhejiang University, 310027 Hangzhou, China
(Dated: August 28, 2024)
A central goa"
related_documents: []
---

# Cost Optimization Strategies

<!-- Page 1 -->

Single-mode spin-wave laser driven by spin-orbit torque

### J. S. Harms1,3,∗ H. Y. Yuan1,4, and Rembert A. Duine1,2

1Institute for Theoretical Physics, Utrecht University, 3584CC Utrecht, The Netherlands
2Department of Applied Physics, Eindhoven University of Technology,

### P.O. Box 513, 5600 MB Eindhoven, The Netherlands

3Fachbereich Physik, Universita¨t Konstanz, D-78457 Konstanz, Germany and
4Institute for Advanced Study in Physics, Zhejiang University, 310027 Hangzhou, China
(Dated: August 28, 2024)
A central goal in spintronics and magnonics is the use of spin waves rather than electrons for
efficientinformationprocessing. Thekeytointegratesuchspintroniccircuitswithelectroniccircuits
is the ability to inject, control and detect coherent spin waves with charge currents. Here, we
propose a tunable setup consisting of a synthetic antiferromagnet in an inhomogeneous magnetic
field in which one of the magnetic layers is thin and biased by spin-orbit torque. We show that
for appriopriate conditions single-mode coherent spin waves are emitted in this set-up. The set-up
implements coupling of continuum spin waves with a finite region of negative energy spin waves,
such that specific frequencies become self-amplified and thus start lasing. We show there exist a
largeregioninparameterspaceforwhichthecoherentspinwavelaserisstabilizedbynon-linearities
and spin-orbit torques. Our findings may lead to new ways of injecting coherent spin waves with
direct currents.
Introduction.— The emergent fields of magnonics and by the size of the STNO are excited and the frequency
spintronics propose energy efficient circuits and logic de- of excited spin waves depends on the injected current
vicesusingspinwavesasinformationcarriers[1–3]. Spin due non-linearities [11, 12], leading to challenges for its
waves have the advantages of low power-consumption application.
and efficient parallel data processing. Furthermore, spin Another type of STNO uses SOT rather than STT to
waves are promising for unconventional computing ap- injectspinangularmomentumintothemagnet. Theuse
plications, due to their inherent non-linear nature [4–6]. ofSOTratherthanSTThastheadvantagethatthespin
To integrate spintronic circuits with electric circuits, the currentthatisinjectedintothemagneticlayerisperpenability to inject, detect and control magnons using elec- dicular to the charge current. This allows for the injectrical currents is crucial. Although excitation of coher- tion of angular momentum in both insulating and conent spin waves with alternating currents (AC) is rela- ducting magnets, which enables the use of low magnetic
tively straightforward, excitation of coherent spin waves damping material such as yttrium iron garnet (YIG).
using direct currents (DC) is usually more complex and Furthermore,SOTcanbeexertedoveramuchlargerarea
reliesoninjectionofangularmomentumwitheitherspin- ascomparedtoSTT,leavingroomforlargerdevices. On
transfer-torque(STT)orspin-orbit-torque(SOT).While the other hand, SOT-based spin-wave emitters face simexcitation of incoherent (thermal) magnons by SOT has ilardifficultiesforinjectionofcoherentspinwavesasthe
been demonstrated [7], efficient excitation of coherent STNOs proposed by Slonczewki and Berger [20–22].
spin waves by DC current is desirable for the technoloqi- In this Letter, we propose a setup that excites cohercal development of magnonics. ent spin waves via SOT, see Fig. 1. Here, spin waves are
The first proposals to inject coherent spin waves us- coherentlyexcitedbycouplinganormalmagnettoaconing DC currents were put forward by Slonczewki [8] and finedspatialregionwithnegativeenergyspinwaves. This
Berger [9, 10]. In their proposals, they argued that a setuphastheadvantagethatitistunablebytheexternal
spin-polarized current could be used to drive magnetic fieldanddoesnotexperienceanon-linearfrequencyshift
precession or reorient the magnetization. The proposed depending on the injection of angular momentum.
devices are called spin-torque nano oscillators (STNOs) Besides spontaneous emission of coherent spin waves
orspin-waveamplificationbystimulatedemissionofradi- using STT and SOT [8–23], different spin wave laser apation(SWASER).Theinjectionofangularmomentumin proaches have been made that amplify spin waves rather
thesedevicesgivesrisetoanangularprecessionofthefree than spontaneously emitting them. This includes coumagnetization, which in turn stimulates the emission of plingtospinwavestocarrierwaves[24–26],quantumamspin waves [11–13]. Experimentally, the macrospin pre- plification [27, 28] and the creation of a non-equilibrium
cession [14], magnetization reversal [15] and spin wave distribution using rapid cooling [29]. Here, we focus on
emission[16–19]inSTNOsandSWASERshavebeenob- spontaneous emission of coherent spin waves for which
served. Although coherent spin-wave emission using an previous setups are discussed above and rely on STTs or
STNO should be possible, in practice it seems difficult SOTs.
to get single mode coherent spin-wave emission and usu- Fundamentally, the setup discussed here is quite difally a handfull of modes with a wavelength determined ferent from previous STNO or SWASER setups. The
4202
guA
72
]llah-sem.tam-dnoc[
1v75841.8042:viXra

<!-- Page 2 -->

2
functional E [n] in both magnets to be of the form
ν
(cid:90) (cid:26) J (cid:27)
E =M dV (∇ n )2−µ H n , (2)
ν s 2 i ν 0 ν ν,z
with J the exchange constant and H the external mag-
ν
netic field strength. In Eq. (1) α is the dimensionless
GilbertdampingconstantandI characterizestheSOTs
ν
—whichareonlynon-vanishingintherightferromagnet.
Inprinciple,anisotropiescanrelativelystraightforwardly
6
be included in the above energy functional, but we do
5
not expect them to change the qualitative physics and
4
omit them here for brevity.
3
We proceed by defining the canonical coordinate Ψ to
2
(cid:112)
1 be 2−|Ψ|2Ψ=(xˆ∓iyˆ)·nandnoticethatn z =±(1−
0 |Ψ|2) – since the magnetization lives on the sphere. In
-3 -2 -1 0 1 2 3 -3 -2 -1 0 1 2 3
these coordinates the energy functional (2), up to fourth
order in Ψ and Ψ∗, becomes
(cid:90) (cid:26)
FIG. 1. Figure of the setup we propose in this Letter. A E ≃M dV J (cid:0) 1−|Ψ |2/2 (cid:1) (∂ Ψ∗)(∂ Ψ ) (3)
magnet with magnetization direction along the external field ν s ν x ν x ν
on the left is coupled to a magnet with magnetization direc- (cid:27)
tion against the external field on the right. The coupling of + J (cid:0) ∂ |Ψ |2(cid:1)2 ∓µ H (cid:0) 1−|Ψ |2(cid:1) .
spinwavesintheleftmagnettodiscretenegativeenergyspin 4 x ν 0 ν ν
waves in the right magnet facilitates the spin wave laser.

### To incorporate the effect of dissipation, that is, Gilbert

damping and SOT, in these canonical coordinates we introduce the Rayleigh dissipation functional
main difference is that lasing in this setup is induced by
the coupling between the magnets rather than driving of W = M s (cid:90) dV (cid:110)α (∂ n )2−J zˆ·(n ×∂ n ) (cid:111) (4)
the magnet. This instability exists due to mode coales- ν γ 2 t ν ν ν t ν
cence between positive energy modes in the left magnet = M s (cid:90) dV (cid:8) α (cid:2) 1−|Ψ |2/2 (cid:3) (∂ Ψ∗)(∂ Ψ )
and a negative energy mode in the right magnet. The γ ν t ν t ν
negative magnetic energy spin-waves in the right mag- + α (∂ |Ψ |2)2±iI (cid:2) 1−|Ψ |2/2 (cid:3) (Ψ ∂ Ψ∗ −Ψ∗∂ Ψ ) (cid:9) .
net form closed orbits of specific frequencies, which be- 4 t ν ν ν ν t ν ν t ν
comeselfamplifiedandhencestartlasing. TheSTNOsor
The Rayleigh dissipation functional is also expanded up

### SWASERs start lasing due to pumping and thus require

to fourth order in the fields Ψ and Ψ∗. The Eulerdriving for the onset of the lasing instability. Contrary, ν ν

### Lagrange equations with Rayleigh dissipation yield the

the set-up we propose requires the injection of angular
two equations of motion describing the non-linear magmomentumintotherightmagnettostabilizethesystem.
netization dynamics
Model.— We consider a setup of two exchange coupled ferromagnetic thin insulating films subject to an i∂ t Ψ ν ≃−Λ2(1−|Ψ ν |2/2)∂ x 2Ψ ν −Λ2(cid:0) ∂ x 2|Ψ ν |2(cid:1) Ψ ν /2
external magnetic field pointing along the z direction, −Λ2(∂ Ψ∗)(∂ Ψ )Ψ /2±hΨ
x ν x ν ν ν
see Fig. 1. The right film is subject to SOTs keeping +α (cid:2) 1−|Ψ |2/2 (cid:3) (∂ Ψ )+α(∂ |Ψ |2)Ψ /2
the equilibrium magnetization against the direction of ν t ν t ν ν
theexternalmagneticfield. Weassumetemperaturesfar ±iI ν (cid:2) 1−|Ψ ν |2/2 (cid:3) Ψ ν ,
belowtheCurietemperatureforwhichamplitudefluctu- (5)
ations of the magnetization are negligible. Accordingly, wherethesecondequationofmotionisgivenbythecomthe dynamics of the magnetization direction n=M/M plex conjugate of the above. In the above we defined the
s
is well described by the Landau-Lifschitz-Gilbert equa- dimensionless time t → t/γµ 0 M s , the exchange length
(cid:112)
tion (LLG) with spin-orbit torques given by Λ= J/γµ 0 M s , the dimesionless SOT I ν /γµ 0 M s →I ν
and the dimensionless magnetic field h =H /M .
ν ν s
∂ n −αn×∂ n =−γn ×H +I n ×(zˆ×n ), Wefindthelinearspin-waveexcitationsintheleftand
t ν t ν ν eff,ν ν ν ν
(1) right magnet using a plane wave ansatz and linearizing
the equation of motion. This gives the following disperwhere ν ∈ {L,R} denotes the left or right ferromag- sion relation for spin waves
net. The LLG equation describes damped precession ω =Λ2(kL)2+h −iαReω , (6a)

## L L L

around the effective magnetic field strength H =
eff,ν ω =Λ2(kR)2−h −i(I +αReω ), (6b)
−δE /(M δn). Here, we consider the magnetic energy R R R R
ν s

<!-- Page 3 -->

3
whereω givesthedispersionintheleftandrightmag- with Λ =J /Λγµ M .

### L/R c c 0 s

net respectively with kL ∈ R and kR = πm/L with Rather than incorporating the RKKY interaction at
m ∈ N — since the right ferromagnet has finite size. the right interface as a boundary condition, we include
Dynamical stability of the right ferromagnet, at the lin- this interaction as a boundary term in the equation of
ear level, in the absence of coupling between the left and motion of the right ferromagnet after which we substiright magnet, requires Imω < 0. We thus find that tute Eq. (9). The contribution of the RKKY interaction

## R

the SOT should satisfy I > αh for the right magnet to the equation of motion of Ψ then gives

## R R R

to be dynamically stable. This reversal of the magnetization against the external effective field with electric δE int /δΨ∗ = (cid:2) Λ c ΛΨ R −i(Λ2 c /k l L)(1−|Ψ R |2/2)Ψ R (cid:3) δ(x),
currents has been demonstrated experimentally in mag- (10)
netic nanopillars [30]. From this point onward we ignore
which should be added to the equation of motion
Gilbert damping in the left magnet and, for future purinEq.(5). Thefirsttermintheabovedescribesanenerposes,notethatthewavenumberoftheleftmovingmode
geticboundarycontribution,whilethesecondtermgives
intheleftmagnetattheprecessionalfrequencyωisgiven
√
theflowofenergyfromtherightferromagnetictotheleft
by ΛkL =− ω−h .
l L ferromagnet.
Next, we determine the boundary conditions between

### Non-linear analyses of the spin-wave lasing mode.—

the continuum of magnons in the left ferromagnet and

### Because the RKKY coupling between the left and right

the discrete states in the energetically unstable right fermagnet is small compared to their exchange coupling, it
romagnet. The interaction between the magnets is given
is natural to consider a mode expansion which satisfies
by the Ruderman–Kittel–Kasuya–Yosida (RKKY) interthe exchange boundary conditions, ∂ Ψ| = 0, at
action energy x x∈{0,L}
the boundaries in the right magnet
(cid:104)
E int =−J c n L ·n R | x=0 =J c (1−|Ψ L |2)(1−|Ψ R |2) (7) Ψ R = (cid:88) A m (t)eiϕm(t)e−iωmt (cid:114) 2− L δ m,0 cos[k m x], (11)
(cid:112) (cid:105) m

## − (1−|Ψ |2/2)(1−|Ψ |2/2)(Ψ Ψ +Ψ∗Ψ∗) | ,


### L R L R L R x=0

with k = πm/L for m ∈ N and ω = Λ2k2 −h the
m m m R
with J the RKKY interaction strength. From here precessionalfrequencywithoutdampingoftherightmagc
we find the boundary conditions by employing the vari- net. We note that the energetic boundary contribution
ational derivative at the boundaries. This yields the of the RKKY interaction could in principle be included
boundary condition at the interface between left magnet using the Sturm-Liouville expansion. We however disreand the non-magnetic spacer gard this. Since we consider α, I R and Λ2 c to be small,
thereisnoneedtoincludethiscorrectionuptofirstorder
J(1−|Ψ L |2/2)∂ x Ψ L +JΨ L ∂ x |Ψ L |2/2= (8) in these parameters. In the above expansion, we explic-

## J

(cid:104)(cid:112)

## (1−|Ψ |2/2)(1−|Ψ |2/2)Ψ∗ +(1−|Ψ |2)Ψ

itly expect the timescale on which A
n
and ϕ
n
change to
c L R R R L be much larger than the timescale set by ω−1.
n
− (cid:112) (2−|Ψ |2)/(2−|Ψ |2)(Ψ Ψ +Ψ∗Ψ∗)Ψ /4 (cid:105) . We are ultimately interested in the possibility of limit

## R L L R L R L

cycles at finite amplitude because they will correspond,
as we shall see, to lasing or coherent emission of spin

### The boundary condition at the interface between the

waves. We start with the approximation in which only
rightmagnetandthenon-magneticspacerissimilarwith
one non-uniform mode is present. For a non-uniform
Ψ ↔Ψ and ∂ →−∂ .

### L R x x

mode, n̸=0, theequationsofmotioninEq.(5)become
We proceed by treating the spin wave fluctuations in
the left ferromagnet to be much smaller in amplitude
∂ ϕ ≃−α(∂ A )(1+3A2/4L)+2Λ Λ/L, (12a)
thantheamplitudeofthestandingwaveintherightfer- t n T n n c
romagnet. This assumption follows from energy conser- ∂ t A n ≃−(2Λ2 c /k l LL)(1−A2 n /L)A n (12b)
vationattheweaklycoupledinterfaceandbynotingthat −(αω −∂ ϕ +I )(1−3A2/4L)A .
n t n R n n
we only allow for outgoing modes in the left magnet. As
a result we treat the continuum in the left ferromagnet The first equation gives corrections to the precessional
usinglinearspin-wavetheory,whiletreatingtherightfer- frequency due to amplitude fluctuations and the RKKY
romagnetnon-linearly. Wefurthermoreassume−ΛkL ≫ interaction. The second equation describes the dissipal
Λ c , which corresponds to weak coupling. The boundary tive dynamics of the amplitude of the n-th spin-wave
condition in Eq. (8), for weak coupling strengths, be- mode. As we have seen before, the linear equation of
(cid:112)
comesJ∂ x Ψ L | x=0 ≃J c 1−|Ψ R |2/2Ψ∗ R | x=0 .Thisleaves motion in Eq. (6b) predicts that I R > αh R for the
us with spin waves in the right ferromagnetic to be stable to
start with. Furthermore, Eq. (12b) predicts the onset
(cid:112)
iΛkLΨ | ≃Λ 1−|Ψ |2/2Ψ∗| , (9)
l L x=0 c R R x=0 ofalinearinstabilityforcouplingstrengthsΛ c exceeding

<!-- Page 4 -->

4
−2Λ2/kL L > I +αω , where we used the shorthand
c l,n R n √
notationk l L ,n ≡k l L(ω n )=− ω n −h L . Hence,theclosed 0.008
orbitsofnegativeenergyspinwavesbecomeselfamplified
for sufficiently strong coupling strengths. This instabil- 0.006
ity is due to mode coalescence between spin waves in the
left ferromagnet and the negative energy standing waves 0.004
in the right magnet [31]. The mechanism behind this is
similar to the formation of an exceptional point [32]. In- 0.002
cludingthenon-linearcontributionsinEq.(12b),wefind
the amplitude of the self amplified mode to be stabilized 0.000
0.00 0.05 0.10 0.15 0.20 0.25
by the non-linearities and to be given by

### A2 x −1

n ≃ n , (13) FIG. 2. Figure of the current interval presented in Eq. (17),

### L x −3/4

n for h − h = 1/2, L/Λ = 8 and α = 10−2. For these

## R L

parameters,thelasingmodeoccursatn=1. Thesolidcurve
with x =−2Λ2/(αω +I )kL L>1.
n c n R l,n describes the lower bound, while the dashed curve describes

### We may express the emitted spin current in terms

the upper bound. For sufficiently large interaction strengths
of the above spin wave amplitude. This can be done between the magnets we find a large DC current interval in
since the amplitude of emitted spin waves is related whichthissetupisastablesingle-modelaser. Wefurthermore
to the amplitude of the spin wave mode in the right notice a sudden drop in the required current I R for coupling
magnetic via Eq. (9). We further define the dimen- strengthsΛ c >Λ c,critical . Forsmallinteractionstrengths,the
upperandlowerboundswapandhencethereisnopossibility
sionless spin-current in the left ferromagnet by iJ =
spin of a stable single-mode laser in this regime.
Ψ ∂ Ψ∗ −Ψ∗∂ Ψ . This yields that the coherent spin

### L x L L x L

currentcarriedbyspinwavesoffrequencyω emittedby
n
this lasing setup is given by n′. We expect the uniform mode or the first nonuniformbethemostsusceptibletotheinstability. There-
J spin =|A L |2Λk l L ,n , (14) fore we consider n′ → 0 in the following. With use
of Eq. (13), the constraint in Eq. (15) is written as
with |A |2 =2(Λ /ΛkL )2(1−A2/L)A2/L.
In th L e proceed c ing s l, e n ction we n consid n er the DC cur- a quadratic equation in I R − α R + αΛ2k n 2. Namely,
(I − αh + αΛ2k2)2 + (I − αh + αΛ2k2)[5αΛ2k2 +
rentinterval—whichgeneratestheSOT—forwhichthis 5Λ R 2/kL L]+(4Λ2/ n kL L)[2Λ R 2/kL L+3αΛ2k n 2]≳0.Fr n om
single-mode laser remains stable. c l,0 c l,n c l,0 n
the fact that this equation is quadratic we find that all

### Currentintervalforastablesingle-modelaser.—From

currentswithinthelinearlyunstablerange−2Λ2/kL L>
this point onwards we consider the n-th mode to be the c l,n
I +αω >0 are in principle allowed if the discriminant

### R n

linearlymostunstablemodeandtheinteractionbetween
is negative. By assuming 1/kL L to be small compared
this lasing mode and the other modes close to the reso- l,n′
to 1/kL L we find the critical coupling strength to be
nant condition ω = ω −ω∗ +ω , with n , n and l,n
n′ n1 n2 n3 1 2 approximately
n arbitraryforthemoment. Sincebyassumptionthen-
3
thmodeistheonlymodewithnon-vanishingamplitude, Λ2 ≳3αΛ2k2|kL |L/2. (16)
c,critical n l,0
we consider n = n and either n = n and n = n′ or
2 1 3
If Λ , on the other hand, is smaller than this critical
n = n′ and n = n. We therefore consider only modes c
1 3
value, the current interval in which there exists a stable
that appear twice in Eq. (5). To recap, we are interested
one mode laser becomes
in the stability of the situation in which the n-th mode
is lasing and the other modes remain stable, in the sense −2Λ2/kL L≥I −αh+αΛ2k2 ≳5 (cid:0) αΛ2k2 +Λ2/kL L (cid:1)
c l,n R n n c l,0
that their amplitude remains vanishing. The equation of (cid:34)(cid:115) (cid:35)
motion for the amplitude of these other modes follows × 1 1− 48Λ2 c k l L ,0 αΛ2k n 2k l L ,0 L+2Λ2 c /3 −1 . (17)
from Eqs. (5) and (9) as 2 25 kL (αΛ2k2kL L+Λ2)2
l,n n l,0 c
∂ A (2−δ )Λ2 The upper bound in the injected current comes from the
A t n n ′ ′ ≃−αω n′ −I R + k l L ,n n ′ L ′ c (15) l m as a i k n e g s c t o h n e d A ition = − 0 2 a Λ n 2 c / u k n l L s ,n ta L bl ≥ e fi I R xe − d p α o h in + t α in Λ E 2k q n 2 . ( w 1 h 2 i b c ) h .
(cid:34) (cid:35) n
+ αω +I + Λ2k n 2 − 2(2−δ n′ )Λ2 c A2 n <0, In Fig. 2, we plot the electrinic DC current interval
n R 2 k l L ,n′ L L in Eq. (17) as a function of the coupling strength Λ c .

### We like to stress that the lower boundary in the current

where the last equality is the stability requirement. I for Λ > Λ becomes I > α(h −Λ2k2), i.e.

### R c c,critical R R n

Hence, the one mode laser is stable if the amplitude the required current for negative energy spin waves —
in Eq. (13) satisfies the above constraint for arbitrary with frequency ω — to be dynamically stable. We find
n

<!-- Page 5 -->

5
this lowest current to be lower than the current needed left magnet linearly. This approximation becomes less
to stabilize the linear spin waves in Eq. (6a). exact when the resonant frequencies in the right magnet
Furthermore, Eqs. (13), (15) and (17) give a lower are close to the Kittel frequency of the left magnet or
bound in the interfacial coupling strength below which when exploring stronger coupling strengths. Developing
no current interval that stabilizes the one mode laser ex- atheorybeyondthislimitisinprincipleofinterest,since
ists. We find this lower bound in the coupling strength theonsetoflasingiseasiertoachieveforlargecouplings.
to be In future work, one could develop a theory that treats
the non-linear magnetization dynamics of the left mag-
2Λ2 ≳αΛ2k2|kL |L. (18) net. Furthermore, it could useful to consider this setup
c,lower bound n l,n
with two interfaces in the quantum regime. This is due
Let us finish by checking the self-consistency of the as- to the fact that this setup is likely to produce entangled
sumption−Λk l L ,n ≫Λ c ,whichallowsustotreatthespin pairs of magnons. Another direction would be to conwaves in the left domain linearly. This assumption im- sider the coupling between positive and standing wave
plies 1 ≫ Λ2/(ΛkL )2 ≳ αk2L/2|kL |, which is equiva- negativeenergymagnonsinantiferromagnetstocreatea
c l,n n l,n
(cid:112)
lentto(2L/Λ) h −h −n2π2Λ2/L2 ≫αn2π2.Hence, single-mode laser in this class of materials too.

## R L

a single-mode laser is stable if only a few — and most
likely only two or three — energetically unstable modes
are present. ACKNOWLEDGEMENTS

### Conclusion, discussion and outlook.— In this Letter,

we proposed a way to coherently inject spin-waves of a R. A. Duine is member of the D-ITP consortium, a
specific frequency, thereby constituting a spin wave laser program of the Netherlands Organisation for Scientific
driven by a DC current. This realization depended cru- Research (NWO) that is funded by the Dutch Ministry
ciallyonthecouplingofmagnonicexcitationstonegative of Education, Culture and Science (OCW). R.A.D. acenergy magnon excitations in a confined region. Via the knowledges the funding from the European Research
coupling of magnons to these negative energy magnons, Council (ERC) under the European Union’s Horizon
the system can form closed orbits, thereby dynamically 2020 research and innovation programme (Grant No.
destabilizing the system. The formation of the dynami- 725509). This work is part of the Fluid Spintronics recal unstable modes is similar to that of the mode coales- search programme with project number 182.069, which
cence forming an exceptional point. In the literature of isfinancedbytheDutchResearchCouncil(NWO).H.Y.
analoguegravitysuchaset-upisarealizationofablack- YuanissupportedbytheNationalKeyR&DProgramof
hole laser [33]. Since finite many modes start lasing, i.e., China (2022YFA1402700) and Marie Skl(cid:32)odowska-Curie
exponentially growing, non-linearies quickly become im- Grant Agreement SPINCAT (101018193).
portant. Hence, we investigated the non-linear regime
for which the single-mode laser is stable. More specifically, we considered the case in which one mode dominates and analyzed its stability towards instabilities in
∗ joren.harms@uni-konstanz.de
othermodes. Wefoundtheretobearegioninparameter
[1] A. V. Chumak, V. Vasyuchka, A. Serga, and B. Hillespaceforwhichthissingle-modespinwavelaserisstable
brands, Magnon spintronics, 11, 453.
and emits coherent spin waves. We consider typical ex-
[2] S. A. Wolf, D. D. Awschalom, R. A. Buhrman, J. M.
perimental values in Yttrium Iron Garnet (YIG) for the Daughton, S. Von Molna´r, M. L. Roukes, A. Y.
saturation magnetization µ 0 H ∼ µ 0 M s ∼ 0.25 T, the Chtchelkanova, and D. M. Treger, Spintronics: A spingyromagnetic ratio γ/2π ∼ 30GHzT−1 and the Gilbert based electronics vision for the future, 294, 1488.
damping α = 10−4. The SOT is related to the electric [3] H.Y.Yuan,Y.Cao,A.Kamra,R.A.Duine,andP.Yan,
current density J via I ∼ γℏηθ J /2eM d [34], with Quantum magnonics: When magnon spintronics meets
c R SH c s
quantum information science, Physics Reports 965, 1
etheelectroncharge,η ∼O(1)theinterfacialefficiency,
(2022).
d∼2nmthethicknessoftheferromagnetandθ =0.1

### SH [4] G.Csaba,A´.Papp,andW.Porod,Perspectivesofusing

the spin-Hall angle for Platinum [35]. The current necspin waves for computing and signal processing, Physics
essary to keep this setup in the lasing regime is of the Letters A 381, 1471 (2017).
order I /γµ M ∼ αH /M ∼ O(α). Hence, we esti- [5] P. Pirro, V. I. Vasyuchka, A. A. Serga, and B. Hille-

### R 0 s R s

mate the current density needed to stabilize the laser to brands, Advances in coherent magnonics, Nature Rebe of the order J ∼ 108A/m2. Furthermore, the ex- views Materials 6, 1114 (2021).
c
[6] A. V. Chumak, P. Kabos, M. Wu, C. Abert, C. Adelchange length for YIG is approximately Λ ∼ 9 nm and
mann, A. O. Adeyeye, J. ˚Akerman, F. G. Aliev,
the dimensionless RKKY coupling is tunable and of the
A. Anane, A. Awad, C. H. Back, A. Barman, G. E. W.
orderΛ ∼O(1)[36]. TheresultsinthisLetterhavebeen
c Bauer, M. Becherer, E. N. Beginin, V. A. S. V. Bitfound assuming weak coupling between the magnets, i.e. tencourt, Y. M. Blanter, P. Bortolotti, I. Boventer,
−ΛkL ≫ Λ , which allows us to treat spin waves in the D. A. Bozhko, S. A. Bunyaev, J. J. Carmiggelt, R. R.
l c

<!-- Page 6 -->

6
Cheenikundil, F. Ciubotaru, S. Cotofana, G. Csaba, [18] V. E. Demidov, S. Urazhdin, R. Liu, B. Divinskiy,
O. V. Dobrovolskiy, C. Dubs, M. Elyasi, K. G. Fripp, A.Telegin,andS.O.Demokritov,Excitationofcoherent
H. Fulara, I. A. Golovchanskiy, C. Gonzalez-Ballestero, propagating spin waves by pure spin currents, 7, 10446
P. Graczyk, D. Grundler, P. Gruszecki, G. Gubbiotti, (), number: 1 Publisher: Nature Publishing Group.
K. Guslienko, A. Haldar, S. Hamdioui, R. Hertel, [19] M. Madami, S. Bonetti, G. Consolo, S. Tacchi, G. Car-
B. Hillebrands, T. Hioki, A. Houshang, C.-M. Hu, lotti, G. Gubbiotti, F. B. Mancoff, M. A. Yar, and
H. Huebl, M. Huth, E. Iacocca, M. B. Jungfleisch, J. ˚Akerman, Direct observation of a propagating spin
G. N. Kakazei, A. Khitun, R. Khymyn, T. Kikkawa, wave induced by spin-transfer torque, 6, 635, number:
M. Kla¨ui, O. Klein, J. W. K(cid:32)los, S. Knauer, S. Ko- 10 Publisher: Nature Publishing Group.
raltan, M. Kostylev, M. Krawczyk, I. N. Krivorotov, [20] B. Divinskiy, V. E. Demidov, S. Urazhdin, R. Free-
V. V. Kruglyak, D. Lachance-Quirion, S. Ladak, R. Le- man, A. B. Rinkevich, and S. O. Demokribrun, Y. Li, M. Lindner, R. Macˆedo, S. Mayr, G. A. tov, Excitation and amplification of spin waves
Melkov, S. Mieszczak, Y. Nakamura, H. T. Nembach, by spin–orbit torque, 30, 1802837, eprint:
A. A. Nikitin, S. A. Nikitov, V. Novosad, J. A. Ota´lora, https://onlinelibrary.wiley.com/doi/pdf/10.1002/adma.201802837.
Y. Otani, A. Papp, B. Pigeau, P. Pirro, W. Porod, [21] V. E. Demidov, S. Urazhdin, A. Anane, V. Cros, and
F. Porrati, H. Qin, B. Rana, T. Reimann, F. Riente, S. O. Demokritov, Spin–orbit-torque magnonics, 127,
O.Romero-Isart,A.Ross,A.V.Sadovnikov,A.R.Safin, 170901 ().
E. Saitoh, G. Schmidt, H. Schultheiss, K. Schultheiss, [22] M. Collet, X. de Milly, O. d’Allivy Kelly, V. V. Naletov,
A. A. Serga, S. Sharma, J. M. Shaw, D. Suess, R. Bernard, P. Bortolotti, J. Ben Youssef, V. E. Demi-
O. Surzhenko, K. Szulc, T. Taniguchi, M. Urba´nek, dov,S.O.Demokritov,J.L.Prieto,M.Mun˜oz,V.Cros,
K. Usami, A. B. Ustinov, T. van der Sar, S. van Di- A.Anane,G.deLoubens,andO.Klein,Generationofcojken, V. I. Vasyuchka, R. Verba, S. V. Kusminskiy, herentspin-wavemodesinyttriumirongarnetmicrodiscs
Q. Wang, M. Weides, M. Weiler, S. Wintz, S. P. Wol- by spin–orbit torque, 7, 10377, number: 1 Publisher:
ski, and X. Zhang, Advances in Magnetics Roadmap on Nature Publishing Group.
Spin-WaveComputing,IEEETransactionsonMagnetics [23] R. Doornenbal, A. Rold´an-Molina, A. Nunez, and
58, 1 (2022). R. Duine, Spin-wave amplification and lasing driven by
[7] L.J.Cornelissen,K.J.H.Peters,G.E.W.Bauer,R.A. inhomogeneousspin-transfertorques, 122,037203,pub-
Duine,andB.J.vanWees,Magnonspintransportdriven lisher: American Physical Society.
by the magnon chemical potential in a magnetic insula- [24] B.Robinson,B.Vural,andJ.Parekh,Spin-wave/carriertor, Phys. Rev. B 94, 014412 (2016). wave interactions, 17, 224.
[8] J.C.Slonczewski,Current-drivenexcitationofmagnetic [25] O. A. C. Nunes, Spin wave amplification by a radiation
multilayers, 159, L1. field in free-carrier magnetic semiconductors, 44, 1275.
[9] L. Berger, Emission of spin waves by a magnetic mul- [26] E. Souto, O. A. C. Nunes, D. A. Agrello, and A. L. A.
tilayer traversed by a current, 54, 9353 (), publisher: Fonseca, Spin wave amplification in antiferromagnetic
American Physical Society. semiconductors stimulated by infrared laser field, 286,
[10] L. Berger, Spin-wave emitting diodes and spin diffusion 353.
in magnetic multilayers, 34, 3837 (), conference Name: [27] V.V.Danilov,Effectsoftheinteractionbetweensurface
IEEE Transactions on Magnetics. magnetostatic waves and the spin system of a paramag-
[11] M. A. Hoefer, M. J. Ablowitz, B. Ilan, M. R. Pufall, netic crystal, 23, 1006.
and T. J. Silva, Theory of magnetodynamics induced by [28] V. V. Danilov and A. Y. Nechiporuk, Experimental inspin torque in perpendicularly magnetized thin films, vestigation of the quantum amplification effect for mag-
95, 267206. netostatic waves in ferrite-paramagnet structures, 28,
[12] A. Slavin and V. Tiberkevich, Spin wave mode excited 369.
byspin-polarizedcurrentinamagneticnanocontactisa [29] D. Breitbach, M. Schneider, B. Heinz, F. Kohl,
standing self-localized wave bullet, 95, 237201 (). J. Maskill, L. Scheuer, R. Serha, T. Bra¨cher, B. La¨gel,
[13] A. Slavin and V. Tiberkevich, Nonlinear auto-oscillator C. Dubs, V. Tiberkevich, A. Slavin, A. Serga, B. Hilletheoryofmicrowavegenerationbyspin-polarizedcurrent, brands, A. Chumak, and P. Pirro, Stimulated amplifica-
45, 1875 (), conference Name: IEEE Transactions on tion of propagating spin waves, 131, 156701.
Magnetics. [30] B. O¨zyilmaz, A. D. Kent, D. Monsma, J. Z. Sun, M. J.
[14] M. Tsoi, A. G. M. Jansen, J. Bass, W.-C. Chiang, Rooks, and R. H. Koch, Current-induced magnetization
M. Seck, V. Tsoi, and P. Wyder, Excitation of a mag- reversalinhighmagneticfieldsinCo/Cu/Conanopillars,
netic multilayer by an electric current, 80, 4281, pub- Phys. Rev. Lett. 91, 067203 (2003).
lisher: American Physical Society. [31] A. Coutant and R. Parentani, Black hole lasers, a mode
[15] B. O¨zyilmaz, A. D. Kent, D. Monsma, J. Z. Sun, M. J. analysis, 81, 084042.
Rooks, and R. H. Koch, Current-induced magnetization [32] A. Coutant, F. Michel, and R. Parentani, Dynamical inreversalinhighmagneticfieldsinco/cu/conanopil- stabilities and quasi-normal modes, a spectral analysis
lars, 91, 067203. with applications to black-hole physics, 33, 125032.
[16] W.Rippard,M.Pufall,S.Kaka,S.Russek,andT.Silva, [33] S.CorleyandT.Jacobson,Blackholelasers, 59,124011,
Direct-currentinduceddynamicsinco90fe10/ni80 publisher: American Physical Society.
f e 20 point contacts, 92, 027201. [34] A. Manchon, J. Zˇelezny´, I. M. Miron, T. Jungwirth,
[17] V. E. Demidov, S. Urazhdin, and S. O. Demokritov, Di- J. Sinova, A. Thiaville, K. Garello, and P. Gambardella,
rect observation and mapping of spin waves emitted by Current-inducedspin-orbittorquesinferromagneticand
spin-torquenano-oscillators, 9,984(),number: 12Pub- antiferromagnetic systems, Rev. Mod. Phys. 91, 035004
lisher: Nature Publishing Group. (2019).

<!-- Page 7 -->

7
[35] H. Wang, C. Du, Y. Pu, R. Adur, P. C. Hammel, and [36] K.Wang, V.Bheemarasetty,andG.Xiao,Spintextures
F. Yang, Scaling of spin hall angle in 3d, 4d, and 5d insyntheticantiferromagnets: Challenges,opportunities,
metals from y 3 fe 5 o 12/metal spin pumping, Physical and future directions, APL Materials 11 (2023).
review letters 112, 197201 (2014).

## Tables

**Table (Page 2):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 2):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
