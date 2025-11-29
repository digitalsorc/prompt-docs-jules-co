---
title: "Data Analysis SQL Generation"
original_file: "./Data_Analysis_SQL_Generation.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "react", "evaluation"]
keywords: ["cid", "quantum", "spacetime", "https", "org", "states", "doi", "black", "field", "sum"]
summary: "<!-- Page 1 -->


### Hawking radiation with pure states


### K. Sravan Kumar1* and João Marto2††

1*Institute of Cosmology and Gravitation, U. Portsmouth, Dennis
Sciama Building, Burnaby Road, United Kingdom, Portsmouth, PO1
3FX, United Kingdom."
related_documents: []
---

# Data Analysis SQL Generation

<!-- Page 1 -->


### Hawking radiation with pure states


### K. Sravan Kumar1* and João Marto2††

1*Institute of Cosmology and Gravitation, U. Portsmouth, Dennis
Sciama Building, Burnaby Road, United Kingdom, Portsmouth, PO1
3FX, United Kingdom.
2Departamento de Física, Centro de Matemática e Aplicações
(CMA-UBI), Universidade da Beira Interior, Rua Marquês D Ávila e
Bolama, Covilhã, 6200-001, Portugal.
*Corresponding author(s). E-mail(s): sravan.kumar@port.ac.uk;

### Contributing authors: jmarto@ubi.pt;

†These authors contributed equally to this work.

### Abstract

Hawking’s seminal work on black hole radiation highlights a critical issue in our
understanding of quantum field theory in curved spacetime (QFTCS), specifically the problem of unitarity loss (where pure states evolve into mixed states).
In this paper, we examine a recent proposal for a direct-sum QFTCS, which
maintainsunitaritythroughanovelquantizationmethodthatemploysgeometric
superselection rules based on discrete spacetime transformations. This approach
describes a quantum state in terms of components that evolve within geometric superselection sectors of the complete Hilbert space, adhering to the discrete
symmetries of a Schwarzschild black hole. Consequently, it represents a maximallyentangledpurestateasadirect-sumoftwocomponentsintheinteriorand
exterior regions of the black hole, thereby preserving the unitarity of Hawking
radiation by keeping it in the form of pure states.
Keywords:Quantumfieldtheoryincurvedspacetime,Blackholes,Hawking
radiation,Quantumgravity
1 Introduction
The seminal papers of Hawking’s on black hole (BH) radiation [1, 2] have exposed
explicitlytheincompatibilityinourunderstandingofgravityandquantummechanics.
1
4202
ceD
21
]cq-rg[
3v25681.7042:viXra

<!-- Page 2 -->

To be precise, the issue of understanding the behavior of fields in black hole spacetime was first discussed by Einstein and Rosen in 1935 [3], even before the formal
development of quantum field theory (QFT). The important conundrum is the loss
of unitarity, which involves the evolution of pure states into mixed states. In other
words, Hawking radiation is formed by mixed states, and the (maximally) entangled
partner is always left behind the Schwarzschild black hole (SBH) horizon [4, 5]. This
would mean an observer outside the SBH would access states whose fate depends on
what happens to the partner states behind the horizon. This opens a serious conceptualconundrum:theobserver’squantumphysicsdependsonwhatishappeninginthe
region of spacetime to which the observer has no causal access. Since an asymptotic
observer would never witness any particle (quantum state) crossing the horizon, the
violation of unitarity results in an incomplete understanding of quantum physics for
the asymptotic observer. Often, it is interpreted as an acceptable outcome to treat
black holes as special objects in the Universe that would violate unitarity [6]. But
this interpretation is not the solution [7], and even if it is, one is left with the prediction, by D. Page, that the entanglement entropy of Hawking quanta would at some
pointexceedthethermodynamicentropyoftheblackhole[8–10].Often(Planckscale)
quantumgravityproponentstakesolaceinanunknownultraviolet(UV)completetheory to resolve the problem of unitarity in black hole physics [11, 12]. This raises the
logical question of why Planck-scale quantum gravity is necessary to address a fundamental problem that arises from understanding quantum fields in curved spacetime.
Along with unitarity loss, there is also a related issue of information loss, which carries an additional question on the universal nature of Hawking radiation that leaves
no knowledge of what has formed the black hole. Understanding the formation of a
black hole (quantum mechanically) is another hard question that requires a robust
formulation of QFT in a dynamically collapsing geometry, which we do not have yet.
Hawking’s actual calculation involves quantization in Schwarzschild spacetime, even
though he framed the discussion in the context of a black hole formed by collapse.
Despitenumerousattempts[13,14]toaddresstheinformationparadoxissue,Einstein-
Rosen’s initial question of particle problem in general relativity remains and needs to
be taken very seriously. Recent ongoing efforts by Gerard ’t Hooft[15–22], building on
the work of Norma G. Sanchez and B. F. Whiting [23] and the gravitational backreaction calculations by Dray and ’t Hooft [24], underscore the importance of resolving
the information paradox through fundamental physics before turning to an unknown
theory of quantum gravity.
The recently proposed direct-sum quantum field theory in curved spacetime
(QFTCS) presents an elegant new approach to addressing the issues of unitarity and
information loss in black hole physics [25–27]. The direct-sum QFTCS has also led
to the promising explanation for the long-standing CMB anomalies in the context of
inflationary cosmology [28, 29]. The framework of direct-sum QFTCS is based on the
intricateunderstandingofdiscretespacetimesymmetriesandseparatingthenotionsof
classicalandquantummechanicaltime.Inthisreview,weexplorehowthisframework
providesaunitarydescriptionofHawkingradiationandofferssignificantinsightsinto
extractinginformationabouttheblackholeinteriorthroughafundamentalapproach.
Black holes and de Sitter spacetime share certain analogies related to event horizons,
2

<!-- Page 3 -->

asexploredbyGibbonsandHawking[30].Thus,webrieflyaddressasimilarunitarity
issue in de Sitter space and the potential resolution offered by direct-sum QFTCS.
This review is organized as follows: in Sec. 2, we discuss the parity (P) and time
reversal(T)symmetriesinquantummechanicsandMinkowskiQFT.Wethenpresent
thefoundationalframeworkofdirect-sumQFT.InSec.3,wediscusstheSchwarzchild
BH spacetime and the basic assumptions in Hawking’s original calculation. We then
present the details of ’t Hooft’s quantum algebra that emerges from the effects of
gravitational backreaction. In Sec. 4, we summarize the results of direct-sum QFT in
BH spacetime and its approach to obtaining Hawking radiation in the form of pure
states.WealsoshowtheQFTextensionof’tHooftquantumalgebraandtheresulting
guidelinestoextractinformationfromHawkingradiation.InSec.5,weconcludewith
a qualitative discussion and present outlook for future investigations.
Throughout the manuscript, we use the metric signature mostly positive
(−, +, +, +) and ℏ=c=1.
2 PT symmetry and direct-sum quantum theory
Quantum mechanics is recognized for its time symmetry [31, 32], a property linked
to the anti-unitary nature of the time reflection operation. In quantum theory, time
is treated as a parameter rather than an operator, unlike spatial position. This distinct treatment of time sets it apart in quantum theory compared to classical theory.
Quantum Field Theory (QFT) in Minkowski spacetime represents a unification of
special relativity and quantum mechanics, achieved by enforcing the commutation of
field operators at space-like separations. In the context of Klein-Gordon field this is
expressed as
(cid:104) (cid:105)
ϕˆ(x), ϕˆ(y) =0, (x−y)2 >0. (1)
TheaboveconditiontogetherwithLorentzinvariancedictatestheexpansionofKlien-
Gordon (KG) (real scalar) field operator as
(cid:90) d3k 1 (cid:104) (cid:105)
ϕˆ(x)= a eik·x+a†e−ik·x (2)
(2π)3/2(cid:112) 2|k | k k
0
where k·x = −k t+k·x. The connection with quantum mechanics stems from the
0
positive energy state definition, defined by
|Ψ⟩ =e−iEt|Ψ⟩ (3)
t 0
assuming the arrow of time to be t:−∞→∞. We can see that the expression of KG
field operator (2) is a combination of positive and negative energy solutions. These
(cid:16) (cid:17)
are associated with creation and annihilation operators a , a† which satisfy the
k k
canonical commutation relations and the Minkowski vacuum is defined by
(cid:104) (cid:105)
a , a† =1, a |0 ⟩=0. (4)
k k k M
3

<!-- Page 4 -->

Another equivalent way of defining a positive energy state (3) is
|Ψ⟩ =eiEt|Ψ⟩ (5)
t 0
with the presumption on the arrow of time t:∞→−∞. Usually, the entire quantum
theoryisconstructedbasedontheconvention(3).Asnotedin[33],onecanredefinethe
entire framework ofquantum theory bychangingthe definition ofpositive energy (5),
which means reversing the convention on the arrow of time and effectively replacing i
with −i throughout the quantum (field) theory.
Direct-sum quantum theory starts with a construction that combines both arrows
of time together with parity operation to express a single quantum state. According
to this, a single quantum state is expressed by joining two components through a
direct-sum operation
(cid:18) (cid:19)

## 1 1 |Ψ ⟩


## |Ψ⟩= √ ( |Ψ ⟩⊕|Ψ ⟩)= √ + (6)


## 2 + − 2 |Ψ − ⟩

|Ψ ⟩ are orthogonal states [34] of the direct-sum Hilbert space
±

## H=H ⊕H (7)

+ −
Here,H arecalledthegeometricsuperselectionsectors1;statesinthesesectorscannot
±
besuperposedcoherentlywitheachother,andastatecorrespondingtoonesectordoes
not evolve to the other. Here ± mean the parity conjugate regions of physical space.
The states |Ψ ⟩ evolve according the following direct-sum Schrödinger equation
±
∂|Ψ⟩ (cid:18) Hˆ 0 (cid:19)
i = + |Ψ⟩ (8)
∂t 0 −Hˆ
p −
where Hˆ (xˆ , pˆ ) give the Hamiltonians of the system Hˆ = Hˆ ⊕Hˆ , which are
± ± ± + −
functions of position and momenta operators of the target space defined by
d
pˆ =−i , x =x≳0
+ dx +
+ (9)
d
pˆ =i , x =x≲0.
− dx −
−
where the eigenvalues of xˆ are parity conjugate points which mean x ∈(0, ∞] and
± +
x ∈[−∞, 0).
−
The canonical non-zero commutation relations are2
[xˆ , pˆ ]=i, [xˆ , pˆ ]=−i, (10)
+ + − −
1ThenomenclaturegeometricsuperselectionsectorsisbecausetheHilbertspacesH±areassociatedwith
the physical states in the parity conjugate regions, which means we attach the Hilbert space to describe
statesinaparticularregionofphysicalspace.
2Theremainingrelationsare[xˆ+,xˆ−]=[pˆ+,pˆ−]=[xˆ+,pˆ−]=[pˆ+,xˆ−]=0.
4

<!-- Page 5 -->

Fig. 1 This is a pictorial description of how a quantum harmonic oscillator is described by directsumquantumtheorybymeansoftwoquantumstates,evolvingwithtwooppositearrowsoftimeat
parityconjugatepointsinphysicalspace.
The complete description of a quantum state, in the entire physical space, is given by

## |Ψ⟩

Ψ(x)= √ 1 (cid:0) ⟨x | ⟨x | (cid:1) (cid:18) |Ψ + ⟩ 0 e−iEt(cid:19) =⇒ (cid:40) √1 2 Ψ + (x + )e−iEt, x + =x≳0
2 + − |Ψ − ⟩ 0 eiEt √1 Ψ − (x − )eiEt, x − =x≲0.
2
(11)
The square integrability and the probabilities of states are given by
(cid:90) ∞ 1(cid:90) 0 1(cid:90) ∞
dx⟨Ψ|Ψ⟩= dx ⟨Ψ |Ψ ⟩+ dx ⟨Ψ |Ψ ⟩=1. (12)
2 − − − 2 + + +
−∞ −∞ 0
Thedescriptionofaharmonicoscillator,inthecurrentapproach,canbehintedfrom
Fig. 1. The wave function of the parity conjugate region is described by

Ψ (x)=⟨x|Ψ ⟩≡ √ 2n 1 +1n! (cid:0) π 1(cid:1)1/4 e− 2 1x2 +H n (x + )e−iEntp, x + ≳0 (13)
n n √ 2n 1 +1n! (cid:0) π 1(cid:1)1/4 e− 2 1x2 −H n (x − )eiEntp, x − ≲0
where E corresponds to energy state for each n of the Hermite polynomials H . We
n n
can see that in the limit x → 0 , the two-component states |Ψ ⟩ match automati-
± ± ±
cally.Thepointx=0isnotaspecialpointsinceunderthetranslationx→x+L,the
construction remains the same because it is based on PT, a discrete transformation.
5

<!-- Page 6 -->

The orthogonality of states corresponding to different energy levels is given by
(cid:90) ∞ (cid:90) ∞ (cid:90) 0
⟨Ψ |Ψ ⟩dx= dx ⟨Ψ |Ψ ⟩+ dx ⟨Ψ |Ψ ⟩dx =δ (14)
n m + n+ m+ − n− m− − n,m
−∞ 0 −∞
Furthermore, an observer can only measure the quantum state in either of the parity
conjugate points, and the arrow of time in quantum theory is not observable for any
classical observer.
Minkowski spacetime ds2 =−dt2+dx2 is PT symmetric (i.e., metric is invariant
undert→−tandx→−x).Thus,onecanextendthedirect-sumSchrödingerequation
(6) to the relativistic case by direct-sum QFT where a KG field operator is expressed
as direct-sum of two components as a function of PT conjugate points
1 (cid:18) ϕˆ 0 (cid:19)
ϕˆ(x)= √ + (15)
2 0 ϕˆ
−
where
(cid:90) d3k 1 (cid:104) (cid:105)
ϕˆ (x)= a eik·x+a† e−ik·x
+ (2π)3/2(cid:112) 2|k | (+)k (+)k
0 (16)
(cid:90) d3k 1 (cid:104) (cid:105)
ϕˆ (−x)= a e−ik·x+a† eik·x
− (2π)3/2(cid:112) 2|k | (−)k (−)k
0

### The creation and annihilation operators obey

(cid:104) a , a† (cid:105) =1, (cid:104) a , a† (cid:105) = (cid:2) a , a (cid:3) =0. (17)
(±)k (±)k (±)k (∓)k (±)k (∓)k
which imply a new causality condition
(cid:104) (cid:105)
ϕˆ (x), ϕˆ (−y) =0. (18)
+ −
Herewenoticethat,inournotation,ϕˆ arefieldoperatorsdefinedforparityconjugate
±
pointsinphysicalspace,whichmeanthefirstlinein(16)isdefinedonlyforx≳0where
asthesecondlineisdefinedonlyforx≲0,thedirect-sumofthesetwooperatorsdefine
the quantum field (15) everywhere in Minkowski spacetime. Since the construction
is based on PT, any Lorentz transformation on (15) preserve the structure of PT
symmetric Minkowski vacuum given by
(cid:18) (cid:19)
1 |0 ⟩
|0 ⟩= √ M+ , a |0 ⟩=0, a |0 ⟩=0. (19)
M 2 |0 M− ⟩ (+)k M+ (−)k M−
6

<!-- Page 7 -->

The two-point function and propagator in direct-sum QFT are given by
1 1
⟨0|ϕˆ(x)ϕˆ(x′)|0⟩= ⟨0 |ϕˆ (x)ϕˆ (x′)|0 ⟩+ ⟨0 |ϕˆ (−x)ϕˆ (−x′)|0 ⟩
2 + + + + 2 − − − −
1 1
⟨0|Tϕˆ(x)ϕˆ(x′)0|⟩= ⟨0 |Tϕˆ (x)ϕˆ (x′)|0 ⟩+ ⟨0 |Tϕˆ (−x)ϕˆ (−x′)|0 ⟩,
2 + + + + 2 − − − −
(20)
where T represents time ordering. All the interactions are divided into direct-sum
components. For example, cubic interaction like the following
λ λ (cid:18) ϕˆ3 0 (cid:19)
ϕˆ3 = + (21)
3 3 0 ϕˆ3
−
shows that there will never be any mixing between ϕˆ and ϕˆ . Therefore, all the
+ −
standard QFT calculations can be straightforwardly extended to DQFT but we do
not see any change in results because Minkowski spacetime is PT symmetric (See
[25, 27, 35] for more details). According to the DQFT standard model, vacuum and
thedegreesoffreedomofparticles(|SM⟩)andantiparticles(|SM⟩arerepresentedby
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)

## |0 ⟩ 1 |Sm ⟩ 1 |Sm ⟩

|0 ⟩= SM+ |SM⟩= √ + |SM⟩= √ + (22)

### Sm |0 Sm− ⟩ 2 |Sm − ⟩ 2 |Sm − ⟩

Note that we apply the same geometric super-selection-rule based on PT for all Fock
spacesofthestandardmodeldegrees offreedom,i.e.,theparityconjugateregionsare
uniquelydefinedforalltheparticleandantiparticlestatesofthestandardmodel.Note
that when we include charge conjugation operation C, every quantum field is again
expressed as a direct-sum of components in geometric superselection sectors of Fock
space defined by PT. The standard understanding of CPT symmetry in QFT holds
separately in both the geometric superselection sectors, as further explained below.
While this work primarily addressed the DQFT quantization of a real scalar field,
the approach naturally extends to complex scalars, fermions, and gauge fields [35].
In the DQFT framework, each quantum field is expressed as a direct-sum of two
components,actingasPT mirrorreflectionsofeachother,spanningthefullMinkowski
spacetime. Consequently, the conventional methods of field quantization can be easily
adapted to fit within the DQFT structure.
(cid:16) (cid:17)
• Complex scalar field operator ϕˆ
c
= √1 ϕˆ
c+
⊕ϕˆ
c−
in DQFT is expanded as
2
(cid:34) (cid:35)
(cid:90) d3k 1
ϕˆ = a e±ik·x+b† e∓ik·x
c± (2π)3/2(cid:112) 2|k | (±)k (±)k (23)
0
(cid:104) (cid:105)
ϕˆ , ϕˆ =0,
c+ c−
where a , a† and b , b† are canonical creation and annihilation oper-
(±)k (±)k (±)k (±)k
ators of the parity conjugate regions (denoted by subscripts ) attached with
(±)
7

<!-- Page 8 -->

geometric superselection sector. All the cross commutation relations of a , a†
(±) (±)
and b , b† vanish.
(±) (±)
(cid:16) (cid:17)
• Fermionic field operator ψˆ= √1 ψˆ
+
⊕ψˆ
−
in DQFT becomes
2
(cid:34) (cid:35)
ψˆ = (cid:88) (cid:90) d3k c u (k)e±ik·x+d† v (k)e∓ik·x (24)
± (2π)3/2(cid:112)
2|k |
s˜(±)k s˜ s˜(±)k s˜
s˜ 0
where s˜= 1,2 correspond to the two independent solutions of (k/+m)u = 0 and
s
(−k/+m)v = 0 corresponding to spin-±1. The creation and annihilation operas 2
tors,oftheFockspacegeometricsuperselectionsector,satisfytheanti-commutation
(cid:110) (cid:111) (cid:110) (cid:111) (cid:110) (cid:111)
relations c , c† = 1, c , c† = c , c = 0 leading to
s(±)k s(±)k s(∓)k s(±)k s(∓)k s(±)k
(cid:110) (cid:111)
the new causality condition ψˆ , ψˆ =0.
+ −
(cid:16) (cid:17)
• The vector field operator Aˆ
µ

## = √1 Aˆ

+µ

## ⊕Aˆ

−µ
in DQFT expressed as
2
(cid:34) (cid:35)
(cid:90) d3k
Aˆ = e(λ) c e±ik·x+c† e∓ik·x (25)
±µ (2π)3/2(cid:112)
2|k |
µ (±λ)k (±λ)k
0
where e(λ) is the polarization vector satisfying the transverse and traceless con-
µ
ditions. The creation and annihilation operators c , c† satisfy the similar
(±λ)k (±λ)k
relations as (16).
All the Standard model calculations remain the same because all the interactions
terms become
(cid:18)O3 0 (cid:19) (cid:18)O4 0 (cid:19)

## L ∼O3 = Sm+ L ∼O4 = Sm+ (26)

c SM 0 O3 q SM 0 O4

## Sm− Sm−

whereO isanyoperatorintheStandardModelinvolvingquantumfieldsandtheir

## Sm

derivatives. Therefore, direct-sum QFT is a framework that does not alter the QFT
calculations in Minkowski due to the spacetime being PT symmetric. For example,
when calculating a scattering amplitude, such as the transition from N particles to
M particles, the outcome under DQFT remains identical to that of standard QFT,
namely
AN→M(p ,−p )+AN→M(−p ,p )
A = + a b − a b

## N→M 2 (27)

AN→M(p ,−p )=AN→M(−p ,p ),
+ a b − a b
where p , p with a = 1,···N and b = 1,···M represent the 4-momenta of all the
a b
statesinvolvedinthescattering.A representamplitudesasafunctionof4-momenta
±
ofinitialandfinalstatescomputedinbothvacuums|0 ⟩.Notethattheinandout

## Sm±

statesin|0 ⟩haveoppositesigns,aconsequenceofthereversedarrowoftimeinthe

## Sm±

twovacuums.TheamplitudesA remainequalatallordersofperturbationtheory,as
±
aresultofthePT symmetryinherenttoMinkowskispacetime.Thewell-knownCPT
8

<!-- Page 9 -->

invariance(chargeconjugation,parity,andtimereversal)ofscatteringamplitudes[36]
remains valid in both vacuums as well, ensuring the symmetry is preserved across all
states, which means
AN→M(p ,−p )=AM→N(−p ,p )
+ a b + a b (28)
AN→M(−p ,p )=AM→N(p ,−p ).
− a b − a b
This is attributed to the fact that the CPT operation of any scattering process would
turn the outgoing anti-particles into in-going particles and vice-versa [36].
However, this new understanding provides a fresh perspective on QFT in curved
spacetime,ultimatelyleadingtounitarityandobservercomplementarityinblackhole
spacetime, as proposed by Susskind [37]. What was previously only a hypothesis is
now supported by our framework, offering a fundamental approach to achieving these
principles.
3 On the assumptions behind Hawking’s calculation
and ’t Hooft Gravitational backreaction
In this section, we discuss the crucial observations of Hawking calculation [1, 2] that
has lead to the unitarity loss and information paradox [26]. Hawking’s calculation is
concernedwiththequantizationofscalarfieldinSchwarzschildBHspacetimegivenby
(cid:18) (cid:19)

## 2Gm 1

ds2 =− 1− dt2+ dr2+r2dΩ2, (29)
r
(cid:0)
1−
2GM(cid:1)
r
SBH spacetime is static and spherically symmetric and invariant under the discrete
transformations

### T :t→−t, P :(θ, ϕ)→(π−θ, π+φ) (30)

and asymptotically Minkowski i.e., r → ∞. The coordinate singularity at r = 2GM
makes the Schwarzschild coordinates unfit for understanding quantum fields (which
was first found by Einstein-Rosen in 1935 [3]). This is why Kruskal-Szekers (KS)
coordinates are often used in the literature instead. In those coordinates, the SBH
metric is given by

## 2Gm

ds2 =− e− 2G r MdUdV +r2dΩ2, (31)
r
where
(cid:16) r (cid:17)
UV =16G2M2e2G r M 1− (32)

## 2Gm

TherelationbetweenKScoordinates(U,V)andtheSchwarzschildcoordinatesisgiven
by
(cid:40)
r >2GM =⇒ U =−4GMe− 4G u M <0 V =4GMe4G v M >0 (33)
U =4GMe− 4G u M >0 V =−4GMe4G v M <0.
and
(cid:40)
r <2GM =⇒ U =4GMe− 4G u M >0 V =4GMe4G v M >0 (34)
U =−4GMe− 4G u M <0 V =−4GMe4G v M <0.
9

<!-- Page 10 -->

(cid:12) (cid:12)
(cid:12) (cid:12)
where u=t−r and v =t+r with r =r+2GMln(cid:12) r −1(cid:12) being the so-called
∗ ∗ ∗ (cid:12)2GM (cid:12)
(cid:12) (cid:12)
tortoise coordinate which asymptote to r →−∞ as r →2GM. Thus
∗
(cid:40)
U →0∓ V →0±for r >2GM
r →2GM =⇒ (35)

### U →0± V →0±for r <2GM

As (29) coincides with Minkowski spacetime in the limit r → ∞, and if one assumes
an arrow of time t : −∞ → ∞ for the quantum fields in this asymptotic Minkowski
spacetime,wefindthatHawkingconsidersU <0, V >0tobetheonlyphysicalregion
in the exterior r > 2GM. Thus, the other possibility U > 0, V < 0 is considered
to be a parallel or an unphysical Universe. In a similar way, U < 0, V < 0 (often
called a white hole) of r <2GM is declared to be unphysical too. This is because the
spacetime,longbeforetheblackholehasformed,isassumedtobeMinkowskiwithan
arrow of time t:−∞→∞. Thus, the formation of spacetime with U <0, V <0 and
U > 0, V < 0 was thought to be an impossible scenario from a collapsing geometry.

### There are two caveats in these assumptions

• Wemustbeverycarefulwithtakingclassicalintuitionsintoformulatingthedescription of quantum fields in curved spacetime. Historically, quantum physics is known
to be a counterintuitive formulation.
• UnderstandingtheformationofBHquantummechanicallyisaprofoundopenquestion; thus, declaring U < 0, V < 0 and U > 0, V < 0 as irrelevant for quantum
fields in SBH spacetime has to be taken with great care.
• Symmetries are a guiding concept in physics, and one must be careful in discarding
them (by hand). Given that the following (discrete) spacetime transformations on

### SBH metric (32)

(U, V)→(−U, −V), (θ, φ)→(π−θ, π+φ) (36)
leavethemetric(31)invariant,thereisanambiguityonthechoiceofthesignofthe
coordinates, and it was pointed out by Einstein and Rosen as an important ordeal
for combining gravity and quantum mechanics (See [35]).
Unitarity loss is the hypothetical result of restricting quantum fields to only certain regions of the KS coordinates (U <0, V >0) and (U >0, V >0) whereas the
other regions (U >0, V <0) and (U <0, V <0) are equally allowed by symmetry.
Indeed,theHartle-Hawkingvacuum,obtainedfromthegravitationalpathintegral(in
Euclidean time), gives the relation between the quantum states connecting the previously omitted regions (U >0, V <0) and (U <0, V <0) [38]. It is not a surprising
revelation because allowing a complex time coordinate t→it would render all arrows
of time possible.
Another assumption in the Hawking calculation is the commutation between the
ingoing and outgoing quantum states. Following Eq. (2.4) of [2] the radial component
10

<!-- Page 11 -->

of KG field operator3 is expanded as the sum of interior and exterior parts as

## Φˆ =Φˆ +Φˆ =

(cid:88)(cid:16)
p b +p∗b†
(cid:17)
+
(cid:16)
q c +q∗c†
(cid:17)
(38)
in out i i i i i i i i
i
where p describe purely outgoing states (r > 2GM) and q describe purely ingoing
i i
states, that end up inside r < 2GM. In [2], the following commutation relations are
assumed
(cid:104) (cid:105) (cid:104) (cid:105)
Φˆ , Φˆ =0 =⇒ [b , c ]= b , c† =0, (39)
in out i i i i

### The points worth to be paid attention here are:

• The commutation relation (39) is driven by the intuition that an interior state
cannot affect the exterior state.
• Theexpansion(38)treatstheinteriorandexteriorstatesaspartofthesameHilbert
space, with the same notion of time (in the QFT language), therefore ingoing and
outgoing quanta belong to the same Fock space where time is uniquely defined.

### There are caveats in the above assumptions

• FollowingDrayand’tHooft’sgravitationalbackreaction[24],aningoingparticlein
Schwarzschild spacetime moving along the direction V with momentum P creates
i
a shock wave (transverse field which is a function of θ, φ) that causes a shift in the
positionoftheoutgoingparticlethatisapproachingintheU direction.Theposition
of the outgoing particle (V ) is affected by ingoing momenta (P ), and the position
e i
of the ingoing particle (U ) is affected by outgoing momenta (P ) in the following
i e
way4 [15, 39, 40] (See [26] for more details)
8πG 8πG

## U =− P , V = P . (40)

i R2(ℓ2+ℓ+1) e e R2(ℓ2+ℓ+1) i
where the subscripts P , P and V , U represent (dimensionless) interior and extei e e i
rior (or ingoing and outgoing) momentum and positions (after the gravitational
shift) that are defined by spherical harmonics (See Eq. (5.1) of [39])
(cid:88) (cid:88)
V → V Y (θ, ϕ), U → U Y (θ, ϕ)
e e ℓm i i ℓm
ℓ,m ℓ,m (41)
(cid:88) (cid:88)
P → P Y (θ, ϕ), P → P Y (θ, ϕ)
e e ℓm i i ℓm
ℓ,m ℓm
3Definedbyexpansionintermsofsphericalharmonics
(cid:88) Φ(U,V)
ϕ(U,V)=
r
Yℓm(θ,φ) (37)
ℓ,m
4We note that the ’tHooft considerations ignore interior region of black hole spacetime [17, 22]. In our
approach, we consider both interior and exterior regions of SBH in the near horizon approximation (as
schematicallydepictedinFig.2),andwetakeintoaccountthegravitationalbackreactioneffectsbetween
interiorandexteriorquanta[26]todefineourdirect-sumQFTthatleadstounitarity.Thus,ourconstruction
istechnicallyandconceptuallyverydifferentfromthatof’tHooft[39]andalsotheworksfollowedbyother
authors[40–44].
11

<!-- Page 12 -->

Fig. 2 In the above picture, we depict the Dray and ’tHooft’s gravitational backreaction effect
associated with ingoing and outgoing particles. A (classical) particle in the interior (r ≲2GM, i.e.,
r<2GM butweapplynearhorizonapproximation)withmomentumP¯ igravitationallycauseashift
(∆V¯ e)inthepositionoftheexterioroutgoing(r≳2GM,i.e.,r>2GM butweapplynearhorizon
approximation)particle.Similarly,anexterior(classical)particlewithmomentumP¯ e gravitationally
shifts(∆Ui)theinteriorclassicalparticleposition.
It is important to note that U is the position of the ingoing state (or the interior
i
state at r ≲ 2GM) defined for the KS coordinates U < 0, V > 0 where V is
e
the position of the outgoing state (or the exterior state at r ≳ 2GM) for the KS
coordinates U >0, V >0. Similarly, V , U can be equally defined for the choice of
i e
KS coordinates U >0, V <0 and U <0, V >0.
One can now apply position and momentum uncertainty relations to the operators
of interior and exterior states as [39]
(cid:104) (cid:105) (cid:104) (cid:105)
Vˆ , Pˆ = Uˆ , Pˆ =i (42)
e e i i
Substituting (40) in (42) yields us
(cid:104) (cid:105) 8πG
Uˆ , Vˆ =i (43)
i e R2(ℓ2+ℓ+1)
Note that (43) is the result of combining gravitational backreaction (40) between
the interior and exterior states (See Fig. 2) and the canonical non-commutative relations (42). This is the first quantization (i.e., description of a single quantum state
in Schwarzshild spacetime) together with consideration of gravitational backreaction.
For the second quantization5, i.e., the description of quantum fields in Schwarzschild
spacetime, we uplift the above relations and apply them to the interior and exterior
field operators as [26]
(cid:104) (cid:105) 8πG
Φˆ , Φˆ =i , (44)
in out R2(ℓ2+ℓ+1)
whereR=2GM.Thus(39)isvalidonlyifweignoretheeffectsofgravitationalbackreactionorconsideraninfinitelylargeBHi.e.,R→∞.Inthenextsection,wediscuss
the construction of direct-sum QFTCS, which takes into account the discrete symmetries of SBH metric (36) and the result of gravitational backreaction algebra (44).
5Note that we uplift position and momentum non-commutative relations of first quantization to the
field and its conjugate momenta operatorsin the second quantization.On top of this, we demand all the
operatorscommuteforspace-likedistances,whichisthestepwhereweimplementtherelativisticprinciple.
12

<!-- Page 13 -->

We emphasize that our consideration of gravitational backreaction effect is between
interior and exterior state, which is different from ’t Hooft [16, 17]. Note that the
exterior r ≳ 2GM regions in our picture are parity conjugate regions with opposite
arrows of time (See Fig. 3). Furthermore, there cannot be any gravitational backreactionI , II regionsinourpicturebecausethepoints(θ, φ)and(π−θ, π+φ)are
ext ext
causally separated points for r ≳ 2GM. Also, our construction is different from [43],
where authors do not take into account the quantization of the field in the interior
and exterior regions of Schwarzschild spacetime.
4 Direct-sum QFT in curved spacetime and Hawking
radiation with pure states
Direct-sum quantum theory, presented in Sec. 2, forms a new basis for understanding
quantumfieldsinSBHspacetime.Withthedirect-sumQFTinMinkowskispacetime,
we can address the issue of two arrows of time associated with U < 0, V > 0 and
U > 0, V < 0 of SBH metric (31) and the asymptotic limit r → ∞. A simple thumb
rule of direct-sum QFT is to form geometric superselection sectors for the Hilbert
space (or Fock space) subjected to all the discrete spacetime transformations. In the
context of SBH, the metric (31) and the discrete symmetries (36) form guidelines
for the description of quantum fields in the sectorial Fock spaces represented by the
regions in the conformal diagram in Fig. 3.
In our framework, we expand the field operator as direct-sum of interior ("int")
and exterior ("ext") components as

## Φˆ =Φˆ ⊕Φˆ

int ext
1 (cid:16) (cid:17) 1 (cid:16) (cid:17) (45)

## = √ ΦˆI ⊕ΦˆIi ⊕ √ ΦˆI ⊕ΦˆIi

int int ext ext
2 2
which are defined in the total Fock space, which is a direct-sum of geometric superselection sectors corresponding to the different spatial regions and notions of time
(r ≲2GM and r ≳2GM) (See Fig. 3)

## F =(F ⊕F )⊕(F ⊕F ) (46)


### BH Iint IIint Iext IIext

Foranasymptoticobserveratr →∞(r →∞)ofSBHspace-time(29),thequantum
∗
field is in Minkowski space-time and it becomes
1 (cid:16) (cid:17)

## Φˆ = √ Φˆ ⊕Φˆ , (47)

ext I∞ II∞
2
corresponding to an asymptotic vacuum
|0⟩ =|0⟩ ⊕|0⟩ , (48)

## ∞ I∞ Ii∞

13

<!-- Page 14 -->

Fig. 3 This is conformal diagram of direct-sum QFTCS in SBH spacetime (31) in the Kruskal
coordinates(U,V).Theyellowandgreensharedregionsindicateparityconjugatepoints(θ,φ)and
(π−θ,π+φ)respectively.TheregionslabeledIext,IIext representr>2GM wherequantumfield
components lead to states evolving forward (T :−∞→∞) and backward (T :∞→−∞) in time

## T = U+

2
V whereas Iint,IIint represent interior r < 2GM where quantum field components lead
to the states with opposite time evolutions. The red lines indicate the Schwarzchild singularity at
r = 0, which are identified in the regions Iint and IIint. This conformal diagram does not contain
anywhiteholeorparallelUniverse.Alltheregionsarephysical;theyquantummechanicallyindicate
theevolutionofquantumfieldsinSBHspacetime.
defined by the annihilation operators
aˆ |0⟩ =0, aˆ |0⟩ =0. (49)

### Iω˜ I∞ IIω˜ II∞

The vacuum for quantum field Φˆ in the near horizon approximation r →2GM is
ext
|0⟩ =|0⟩ ⊕|0⟩ (50)
ext Iext IIext
defined by the annihilation operators
ˆb |0⟩ =0, ˆb |0⟩ =0. (51)

### Iω Iext IIω IIext

By applying the technique of Bogoliubov transformation, we obtain the number
densityofparticlescreatedbyoperatorsaˆ† , aˆ† inthevacuum|0⟩ whichiswhat

### Ik IIk BH

exactly asymptotic observer see as Hawking particles. Following [45] we can compute
(cid:90) ∞ (cid:16) (cid:17)
a = dω α b +β b†
Iω˜ ωω˜ Iω ωω˜ Iω
0 (52)
(cid:90) ∞ (cid:16) (cid:17)
a = dω α˜ b +β˜ b†
IIω˜ ωω˜ IIω ωω˜ IIω
0
14

<!-- Page 15 -->

where
(cid:114) ω˜ (cid:90) ∞ du (cid:114) ω˜ (cid:90) ∞ du
α = eiω˜u−iω˜U, β = eiω˜u+iω˜U
ωω˜ ω 2π ωω˜ ω 2π
0 0 (53)
(cid:114) ω˜ (cid:90) ∞ du (cid:114) ω˜ (cid:90) ∞ du
α˜ = e−iω˜u+iω˜U, β˜ = e−iω˜u−iω˜U
ωω˜ ω 2π ωω˜ ω 2π
0 0
Thus, the asymptotic observer witness Hawking radiation by the follow number of
quanta
1 (cid:16) (cid:17)
N = ⟨0| aˆ† ⊕aˆ† (aˆ ⊕aˆ )|0⟩
ω˜ 2BH Iω˜ IIω˜ Iω˜ IIω˜ BH
1(cid:90) ∞ (cid:16) (cid:17)
= dω |β |2+|β˜ |2 (54)
2 ωω˜ ωω˜
0
1
= ,
e8πGMω˜/ℏ−1
whichisthermaldistributionwithatemperatureT = ℏ .Buthere,inourcontext,
8πGM
Hawking radiation is in the form of pure states. Because of the direct-sum structure
of exterior and interior field operators (45), which is different from the one of Hawking’s consideration (38), any maximally entangled non-separable pure state becomes
a direct-sum of two pure state components
|ψ˜ ⟩= (cid:88) c˜ |ϕ˜ ⟩⊗|ϕ˜ ⟩= √ 1 (cid:88) c˜ (cid:16) |ϕ˜ext⟩⊗ϕ˜ext⟩ (cid:17) ⊕ (cid:16) |ϕ˜int⟩⊗ϕ˜int⟩ (cid:17)
12 mn m1 n2 mn m1 n2 m1 n2
2
m,n m,n (55)
1 (cid:18) |ψ˜ext⟩ (cid:19)
= √ 12
2
|ψ˜int⟩
12
where c˜ ̸= c˜ c˜ , |ϕ ⟩ = (cid:80) c˜ |ϕ ⟩ and |ϕ ⟩ = (cid:80) c˜ |ϕ ⟩. This would render
mn n m 1 m m m1 2 n n n2
any density matrix of pure states to become two direct-sum counterparts which are
pure states on their own.
ρ ρ
ρ= ext ⊕ int. (56)
2 2
The Von Neumann entropies of exterior and interior (pure) state components
(S , S ) vanish since exterior and interior are geometric superselection sectors
ext int
S =−Tr(ρ lnρ )=0, S =−Tr(ρ lnρ )=0, S =S +S =0,
ext ext ext int int int H ext int
(57)
This means any asymptotic observer, irrespective of what is beyond the horizon, would witness the pure states evolving into pure states in his/her geometric
superselection-sector of the total Hilbert space. Since states behind the horizon are
related by discrete spacetime transformation UV < 0 → UV > 0 (See region
Fig. 3), one can reconstruct the interior state of SBH. Furthermore, because of noncommutative relation (44), the exterior hawking quanta are not independent of the
interior counterparts, which leads to information reconstruction. This forms the first
step towards resolving the information paradox.
15

<!-- Page 16 -->

5 Conclusions and outlook
Evenafterdecadesofdevelopmentsinquantumgravityresearch,thedeepestproblem
in theoretical physics is at a scale much below the Planck scale, which is the unitarity
problem at the gravitational horizons [46]. Quantum field theory in curved spacetime
requires much stronger foundations, which would help to improve our efforts toward
building quantum gravity at the Planck scales.
DrawingonfoundationalworkbyHawkingand’tHooft,weproposeaQFTframework that incorporates discrete spacetime transformations, acknowledging the status
oftimeasaparameter(i.e.,notanoperatorinquantumtheory).Thisapproach,tested
in various spacetimes such as Rindler [27], de Sitter, Minkowski, and inflationary universe [25, 29, 47]. The framework has been successful in explaining the long-standing
CMB anomalies, which are largely associated with parity asymmetry [29]. In this
paper,wepresentedadiscussionofhowdirect-sumQFTCSpromisesnewinsightsinto
BHphysics[26].Theproposedquantizationapproach,incorporating’tHooft’sgravitationalbackreactioneffects,hasunveiledanovelframeworkforunderstandingquantum
fields in black hole spacetime, specifically within the context of Schwarzschild black
holes. In this review, we contemplated the idea that the black hole under the rules of
direct-sum QFTCS allows us to redefine entanglement between interior and exterior
Hawking quanta in the form of pure states. Concurrently, we observed that exterior
radiation is intrinsically linked to the interior due to new non-commutative relations
resultingfrom’tHooft’sgravitationalbackreactionalgebra.Thisphenomenon,absent
from Hawking’s original 1975 paper, marks a significant departure from traditional
understandings.
We have explored how direct-sum QFT provides a robust framework for maintaining unitarity and observer complementarity (by means of pure states evolving
into pure states) in the presence of spacetime horizons. By decomposing the Hilbert
space into a direct sum of sectorial Hilbert spaces, each associated with different
geometric superselection sectors (linked to PT symmetry), DQFT allows for a more
nuancedunderstandingofinformationconservation.ThisframeworkcouldallowinformationretrievalbeyondthehorizonsbysplittingHilbertorFockspaceintogeometric
superselection sectors.
In conclusion, the study of Hawking radiation with pure states remains a profoundareaofresearchwithintheoreticalphysics,particularlyconcerningtheinterplay
between quantum mechanics and gravity. Hawking’s initial proposal highlighted the
intrinsic challenges, such as the information paradox, unitarity violation, and predictabilitybreakdown,whicharisefromquantizingascalarfieldinSchwarzschildblack
hole spacetime. These issues, traceable to early observations made by Einstein and
Rosen on the fundamental conflict between gravity and quantum mechanics [3, 35],
continue to spur significant advancements in the field of quantum gravity. Direct-sum
quantum theory in curved spacetime by reinstating the unitarity would initiate a new
foundational approach towards quantum gravity.
16

<!-- Page 17 -->


### Acknowledgements

KSKthanksthesupportoftheRoyalSocietyfortheNewtonInternationalFellowship.
This research was funded by Fundação para a Ciência e a Tecnologia grant number
UIDB/MAT/00212/2020. KSK would like to thank the organizers of the EREP 2023
for the kind invitation and opportunity to give a talk on the subject related to this
paper. Authors would like to thank E. Gaztanaga and Mathew Hull for the useful
discussions.

### References

[1] Hawking,S.W.:Blackholeexplosions.Nature248,30–31(1974)https://doi.org/
10.1038/248030a0
[2] Hawking, S.W.: Particle Creation by Black Holes. Commun. Math. Phys.
43, 199–220 (1975) https://doi.org/10.1007/BF02345020 . [Erratum: Commun.Math.Phys. 46, 206 (1976)]
[3] Einstein,A.,Rosen,N.:TheParticleProblemintheGeneralTheoryofRelativity.
Phys. Rev. 48, 73–77 (1935) https://doi.org/10.1103/PhysRev.48.73
[4] Mathur, S.D.: Fuzzballs and the information paradox: A Summary and conjectures (2008) arXiv:0810.4525 [hep-th]
[5] Calmet, X., Hsu, S.D.H.: A brief history of Hawking’s information paradox. EPL 139(4), 49001 (2022) https://doi.org/10.1209/0295-5075/ac81e8
arXiv:2207.08671 [hep-th]
[6] Wald,R.M.:QuantumFieldTheoryinCurvedSpace-TimeandBlackHoleThermodynamics. Chicago Lectures in Physics. University of Chicago Press, Chicago,

## Il (1995)

[7] Kiefer, C.: Hawking radiation from decoherence. Classical and Quantum Gravity
18(22), 151–154 (2001) https://doi.org/10.1088/0264-9381/18/22/101
[8] Page, D.N.: Information in black hole radiation. Phys. Rev. Lett. 71, 3743–3746
(1993) https://doi.org/10.1103/PhysRevLett.71.3743 arXiv:hep-th/9306083
[9] Page, D.N.: Time Dependence of Hawking Radiation Entropy. JCAP 09, 028
(2013) https://doi.org/10.1088/1475-7516/2013/09/028 arXiv:1301.4995 [hepth]
[10] Buoninfante, L., Di Filippo, F., Mukohyama, S.: On the assumptions leading
to the information loss paradox. JHEP 10, 081 (2021) https://doi.org/10.1007/
JHEP10(2021)081 arXiv:2107.05662 [hep-th]
17

<!-- Page 18 -->

[11] Almheiri, A., Hartman, T., Maldacena, J., Shaghoulian, E., Tajdini, A.: The
entropyofHawkingradiation.Rev.Mod.Phys.93(3),035002(2021)https://doi.
org/10.1103/RevModPhys.93.035002 arXiv:2006.06872 [hep-th]
[12] Haggard, H.M., Rovelli, C.: Quantum-gravity effects outside the horizon spark
black to white hole tunneling. Phys. Rev. D 92(10), 104020 (2015) https://doi.
org/10.1103/PhysRevD.92.104020 arXiv:1407.0989 [gr-qc]
[13] Raju, S.: Lessons from the information paradox. Phys. Rept. 943, 1–80 (2022)
https://doi.org/10.1016/j.physrep.2021.10.001 arXiv:2012.05770 [hep-th]
[14] Raju, S.: Failure of the split property in gravity and the information paradox.
Class. Quant. Grav. 39(6), 064002 (2022) https://doi.org/10.1088/1361-6382/
ac482b arXiv:2110.05470 [hep-th]
[15] Hooft, G.: Diagonalizing the Black Hole Information Retrieval Process (2015)
arXiv:1509.01695 [gr-qc]
[16] Hooft, G.: Black hole unitarity and antipodal entanglement. Found. Phys. 46(9),
1185–1198 (2016) https://doi.org/10.1007/s10701-016-0014-y arXiv:1601.03447
[gr-qc]
[17] Hooft, G.: The Firewall Transformation for Black Holes and Some of Its
Implications. Found. Phys. 47(12), 1503–1542 (2017) https://doi.org/10.1007/
s10701-017-0122-3 arXiv:1612.08640 [gr-qc]
[18] Hooft, G.: The Quantum Black Hole as a Hydrogen Atom: Microstates Without

### Strings Attached (2016) arXiv:1605.05119 [gr-qc]

[19] Hooft, G.: Virtual Black Holes and Space–Time Structure. Found. Phys. 48(10),
1134–1149 (2018) https://doi.org/10.1007/s10701-017-0133-0
[20] Hooft, G.: The Big Questions in Elementary Particle Physics. Acta Phys. Polon.

### B 52, 841 (2021) https://doi.org/10.5506/APhysPolB.52.841

[21] Hooft, G.: The Black Hole Firewall Transformation and Realism in Quantum
Mechanics. Universe 7(8), 298 (2021) https://doi.org/10.3390/universe7080298
arXiv:2106.11152 [gr-qc]
[22] Hooft,G.:QuantumClonesinsideBlackHoles.Universe8(10),537(2022)https:
//doi.org/10.3390/universe8100537
[23] Sanchez, N.G., Whiting, B.F.: Quantum Field Theory and the Antipodal Identification of Black Holes. Nucl. Phys. B 283, 605–623 (1987) https://doi.org/10.
1016/0550-3213(87)90289-6
[24] Dray, T., Hooft, G.: The Gravitational Shock Wave of a Massless Particle. Nucl.
Phys. B 253, 173–188 (1985) https://doi.org/10.1016/0550-3213(85)90525-5
18

<!-- Page 19 -->

[25] Kumar, K.S., Marto, J.: Towards a unitary formulation of quantum field theory
in curved spacetime: the case of de Sitter spacetime (2023) arXiv:2305.06046
[hep-th]
[26] Kumar,K.S.,Marto,J.:Towardsaunitaryformulationofquantumfieldtheoryin
curved space-time: the case of Schwarzschild black hole. PTEP ptae, 176 (2023)
https://doi.org/10.1093/ptep/ptae176 arXiv:2307.10345 [hep-th]
[27] Kumar, K.S., Marto, J.: Revisiting Quantum Field Theory in Rindler Spacetime
with Superselection Rules. Universe 10(8), 320 (2024) https://doi.org/10.3390/
universe10080320 arXiv:2405.20995 [gr-qc]
[28] Gaztañaga,E.,Kumar,K.S.:FindingoriginsofCMBanomaliesintheinflationary
quantumfluctuations.JCAP06,001(2004)https://doi.org/10.1088/1475-7516/
2024/06/001 arXiv:2401.08288 [astro-ph.CO]
[29] Gaztañaga, E., Kumar, K.S.: Unitary quantum gravitational physics and the
CMB parity asymmetry (2024) arXiv:2403.05587 [physics.gen-ph]
[30] Gibbons,G.W.,Hawking,S.W.:CosmologicalEventHorizons,Thermodynamics,
and Particle Creation. Phys. Rev. D 15, 2738–2751 (1977) https://doi.org/10.
1103/PhysRevD.15.2738
[31] Hooft,G.:Time,theArrowofTime,andQuantumMechanics.Front.inPhys.6,
81 (2018) https://doi.org/10.3389/fphy.2018.00081 arXiv:1804.01383 [quant-ph]
[32] Donoghue, J.F., Menezes, G.: Arrow of Causality and Quantum Gravity. Phys.
Rev. Lett. 123(17), 171601 (2019) https://doi.org/10.1103/PhysRevLett.123.
171601 arXiv:1908.04170 [hep-th]
[33] Donoghue, J.F., Menezes, G.: Quantum causality and the arrows of time and
thermodynamics.Prog.Part.Nucl.Phys.115,103812(2020)https://doi.org/10.
1016/j.ppnp.2020.103812 arXiv:2003.09047 [quant-ph]
[34] Conway, J.B.: A Course in Functional Analysis / John B. Conway., 2nd ed. edn.
Graduate texts in mathematics ; 96. Springer, New York (2010)
[35] Gaztañaga, E., Kumar, K.S., Marto, J.: A New Understanding of Einstein-
Rosen Bridges. Preprint (2024) https://doi.org/10.20944/preprints202410.0190.
v1 preprint:https://www.preprints.org/manuscript/202410.0190/v1 [Theoretical
physics]
[36] Coleman, S.: Lectures of Sidney Coleman on Quantum Field Theory. WSP,

### Hackensack (2018). https://doi.org/10.1142/9371

[37] Susskind, L., Thorlacius, L., Uglum, J.: The Stretched horizon and black hole
complementarity. Phys. Rev. D 48, 3743–3761 (1993) https://doi.org/10.1103/
19

<!-- Page 20 -->


### PhysRevD.48.3743 arXiv:hep-th/9306069

[38] Hartle, J.B., Hawking, S.W.: Path Integral Derivation of Black Hole Radiance.
Phys. Rev. D 13, 2188–2203 (1976) https://doi.org/10.1103/PhysRevD.13.2188
[39] Hooft, G.: How studying black hole theory may help us to quantise gravity. In: International Conference on Eternity Between Space and Time: From

### Consciousness to the Cosmos (2022)

[40] Betzios, P., Gaddam, N., Papadoulaki, O.: The Black Hole S-Matrix from QuantumMechanics.JHEP11,131(2016)https://doi.org/10.1007/JHEP11(2016)131
arXiv:1607.07885 [hep-th]
[41] Betzios, P., Gaddam, N., Papadoulaki, O.: Black holes, quantum chaos, and the
Riemannhypothesis.SciPostPhys.Core4,032(2021)https://doi.org/10.21468/

### SciPostPhysCore.4.4.032 arXiv:2004.09523 [hep-th]

[42] Betzios, P., Gaddam, N., Papadoulaki, O.: Black hole S-matrix for a
scalar field. JHEP 07, 017 (2021) https://doi.org/10.1007/JHEP07(2021)017
arXiv:2012.09834 [hep-th]
[43] Gaddam,N.,Groenenboom,N.:Softgravitonexchangeandtheinformationparadox.Phys.Rev.D109(2),026007(2024)https://doi.org/10.1103/PhysRevD.109.
026007 arXiv:2012.02355 [hep-th]
[44] Gaddam, N., Groenenboom, N., Hooft, G.: Quantum gravity on the black
hole horizon. JHEP 01, 023 (2022) https://doi.org/10.1007/JHEP01(2022)023
arXiv:2012.02357 [hep-th]
[45] Mukhanov, V., Winitzki, S.: Introduction to Quantum Effects in Gravity.

### Cambridge University Press, ??? (2007)

[46] Giddings, S.B.: The deepest problem: some perspectives on quantum gravity
(2022) arXiv:2202.08292 [hep-th]
[47] Kumar,K.S.,Marto,J.:Parityasymmetryofprimordialscalarandtensorpower
spectra (2022) arXiv:2209.03928 [gr-qc]
20