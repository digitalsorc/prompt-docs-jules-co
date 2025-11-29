---
title: "Latency Optimization Techniques"
original_file: "./Latency_Optimization_Techniques.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag", "chain-of-thought", "evaluation", "multimodal", "dialogue"]
keywords: ["cid", "theory", "frozen", "gauge", "form", "singularities", "singularity", "see", "hep", "arxiv"]
summary: "<!-- Page 1 -->


## Upr-1332-T


## Lmu-Asc 16/24


## Cern-Th-2024-145


### Frozen Generalized Symmetries

Mirjam Cvetiˇc1,2,3, Markus Dierigl4,7, Ling Lin5,6,

### Ethan Torres7, and Hao Y. Zhang8

1Department of Physics and Astronomy, University of Pennsylvania, Philadelphia, PA 19104, USA
2Department of Mathematics, University of Pennsylvania, Philadelphia, PA 19104, USA
3Center for Applied Mathematics and Theoretical Physics, University of Maribor, Maribor, Slovenia
4Arnold Sommerfeld Cen"
related_documents: []
---

# Latency Optimization Techniques

<!-- Page 1 -->


## Upr-1332-T


## Lmu-Asc 16/24


## Cern-Th-2024-145


### Frozen Generalized Symmetries

Mirjam Cvetiˇc1,2,3, Markus Dierigl4,7, Ling Lin5,6,

### Ethan Torres7, and Hao Y. Zhang8

1Department of Physics and Astronomy, University of Pennsylvania, Philadelphia, PA 19104, USA
2Department of Mathematics, University of Pennsylvania, Philadelphia, PA 19104, USA
3Center for Applied Mathematics and Theoretical Physics, University of Maribor, Maribor, Slovenia
4Arnold Sommerfeld Center for Theoretical Physics, LMU, Munich, 80333, Germany
5Dipartimento di Fisica e Astronomia, Universita di Bologna, via Irnerio 46, Bologna, Italy
6INFN, Sezione di Bologna, viale Berti Pichat 6/2, Bologna, Italy
7Theoretical Physics Department, CERN, 1211 Geneva 23, Switzerland
8Kavli IPMU, University of Tokyo, Kashiwa, Chiba 277-8583, Japan

### Abstract

M-theory frozen singularities are (locally) D- or E-type orbifold singularities with a background fractional C -monodromy surrounding them. In this paper, we revisit such back-
3
grounds and address several puzzling features of their physics. We first give a top-down
derivation of how the D- or E-type 7D N = 1 gauge theory directly “freezes” to a lower
rank gauge theory due to the C -background. This relies on a Hanany–Witten effect of
3
fractional M5 branes and the presence of a gauge anomaly of fractional Dp probes in the
circle reduction. Additionally, we compute defect groups and 8D symmetry topological field
theories (SymTFTs) of the 7D frozen theories in several duality frames. We apply our results
to understanding the evenness condition of strings ending on O7+-planes, and calculating
the global forms of supergravity gauge groups of M-theory compactified on T4/Γ with frozen
singularities. In an Appendix, we also revisit IIA ADE singularities with a C -monodromy
1
along a 1-cycle in the boundary lens space and show that this freezes the gauge degrees-offreedom via confinement.
October 2024
4202
tcO
9
]ht-peh[
1v81370.0142:viXra

<!-- Page 2 -->


### Contents

1 Introduction 2
2 Review of Frozen Singularities 6
2.1 Unfrozen Singularities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 Frozen Singularities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3 M-theory on Frozen ADE Singularities 10
3.1 A Local Freezing Map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.2 Top-Down Derivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
4 Defect Groups of Frozen Singularities 23
4.1 Defect Groups from Freezing Map . . . . . . . . . . . . . . . . . . . . . . . . 24
4.2 Review of Duality to Twisted F-theory Compactifications . . . . . . . . . . . 33
4.3 Calculation of Defect Groups in Twisted F-theory Frame . . . . . . . . . . . 35
5 SymTFTs of Frozen Singularities 48
5.1 Unfrozen SymTFTs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
5.2 Frozen SymTFTs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
5.3
e(1/2)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
6
5.4
e(1/4)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
8
6 Applications 60
6.1 Only Even Charge Strings Can End on an O7+ Plane . . . . . . . . . . . . . 61
6.2 M-theory on a Compact K3 with Frozen Singularities . . . . . . . . . . . . . 63
7 Conclusions 67
A Freezing ADE Singularities with 2-Form RR Flux 69

### B Counterterm for Frozen Theories 72

C Consistency with Resolving Singularities 75
1

<!-- Page 3 -->

1 Introduction
Frozensingularitiespresentaninterestingcornerofconsistentstringtheorybackgroundsthat
remains relatively unexplored compared to their unfrozen cousins. In their M-theory description, frozen singularities are realized as fractional G fluxes stuck at geometric singularities,
4
which can be detected via their non-trivial C holonomy at the asymptotic boundary [1–3].
3
Dimensional reduction on these geometrical singularities typically engineer non-Abelian supersymmetric gauge theories, but the presence of the fractional fluxes freezes some of the
original gauge degrees of freedom [1–11]. While this freezing mechanism is more apparent from other string duality frames, a detailed explanation directly in M-theory remained
mysterious. Furthermore, it has become apparent in recent years that studying the local
dynamics of gauge theories only captures part of the theory, with more refined data encoded
in the generalized (categorical) symmetries of the system [12,13], see also [14–18] for reviews.
The goal of this work is to address both these aspects, by explicitly deriving the freezing of
ADE singularities in M-theory as a consequence of the background holonomy/flux
(cid:90) (cid:90)
n
r ≡ C = G = mod 1, gcd(n,d) = 1, (1.1)
3 4
d

## S3/Γ C2/Γ

and additionally understand how this affects the 1-/4-form symmetries of the associated 7D
super-Yang–Mills (SYM) theory.
To extract the global symmetries of a geometrically engineered gauge sector in string
and M-theory one heavily utilizes the properties of the geometrical background, see , e.g.,
[19–48]. In particular, the branes of the underlying theory wrapped on various cycles of
the geometry (which can be more general than singular homology cycles, e.g., K-theory
cycles [49–51]) produce the topological symmetry operators as well as the charged objects
[52–55], whose properties are encoded in the symmetry topological field theory (SymTFT)
[56,52,57]. The study of this more general framework has found much attention within string
compactifications as well, see [58–73] in addition to the references above.
The SymTFT of a D-dimensional system is a topological theory in (D +1)-dimensions,
where the extra dimension is taken to be an interval. One end of the interval contains the
gapless modes, e.g., the degrees of freedom of a g gauge theory, whose generalized global
symmetries are encoded on the other end of the interval, the topological boundary, via the
implementation of gapped boundary conditions. These boundary conditions fix which of
the topological operators of the SymTFT can end on the boundary and which have to be
parallel to it. These, in turn, encode the ending charged operators, that stretch along the
extra dimension, and the symmetry operators, localized on a point in the extra direction,
respectively. In geometrically engineered gauge theories, i.e., a dimensional reduction of
string or M-theory on a local neighborhood X of the singularity, the SymTFT is dimensional
reductionontheasymptoticboundary∂X [52]. Forthispaper, weareinterestedin(D+1) =
8 since we obtain the SymTFT by reducing M-theory on S3/Γ. The interval direction is
2

<!-- Page 4 -->

Figure 1: On the left, we illustrate an 8D SymTFT construction which has a non-topological
boundary T (M)[g(n/d)] and a topological boundary condition B . The boundary condition
top.
is such that there exist and operators W and U which respectively produce a Wilson line
e
and Z(1) symmetry operator in the 7D gauge theory. On the right, we show the M-theory
2
frozen singularity geometry where W is engineered from an M2 brane on a relative 2-cycle
and U from an M5 brane on a boundary 1-cycle.
e
described by the radial coordinate R in X = C2/Γ with respect to the singularity. The
gapless boundary at R = 0 describes the g ≡ g degrees of freedom associated with the

## Γ

singularity, and the topological boundary conditions are implemented at the asymptotic
boundary at R = ∞, see Figure 1.
For 7D SYM theories one expects a class of invertible generalized symmetries encoded in
the spectrum of electric Wilson line operators and their magnetically dual four-dimensional
’t Hooft operators. In the M-theory realization, these originate from M2 and M5 branes
wrapping relative 2-cycles in X, i.e., they stretch from the asymptotic boundary all the way
to the singularity. These lead to 1-form and 4-form symmetries given by the center Z(G) of
the simply-connected group G associated to the gauge dynamics. The topological symmetry
operators on the other hand are described by M5 and M2 branes wrapping boundary 1-
cycles. The SymTFT additionally captures the ’t Hooft anomaly between them related to
the mutual non-locality between Wilson and ’t Hooft operators, which can be derived from
reduction of the kinetic term of the 11D M-theory action [72].
An application of this general recipe to frozen singularities raises an immediate problem.
Sincefrozensingularitiessharethegeometricalbackgroundswiththeirunfrozenversions(i.e.,
r = 0), all conclusions about the generalized symmetries extracted purely from geometry
should be identical. However, when r ̸= 0 the gauge sector changes (see Table 1), and one
would expect the generalized symmetries to be modified as well.
Toillustratethemismatchbetweenourexpectationsandgeometry,itiseasiesttoconsider
3

<!-- Page 5 -->

g so(2k +8) e e e e e e e e e e

### Γ 6 6 7 7 7 8 8 8 8 8

r = n 1 1 1, 2 1 1, 2 1, 3 1 1, 2 1, 3 1, 2, 3, 4 1, 5
d 2 2 3 3 2 3 3 4 4 2 3 3 4 4 5 5 5 5 6 6
h sp(k) su(3) ∅ so(7) su(2) ∅ f g su(2) ∅ ∅

### Γ,d 4 2

Table 1: Frozen half-BPS M-theory singularities of the form C2/Γ [2,4]. The top-line gives
the Lie algebra g of the 7D SYM with no frozen flux, and h is the frozen gauge algebra.

### Γ Γ,d

a fully frozen singularity, i.e., a singularity whose frozen version hosts no continuous gauge
degreesoffreedom. Ifwedenotean(un)frozensingularitybyg(n/d) toindicatetheADE-type
with flux (n/d), then e(1/3) is an instance of such a fully frozen singularity. In such cases, we
6
then do not expect any non-trivial 1-form and 4-form symmetries associated to the gauge
theory as described above. Nevertheless the asymptotic geometry allows the definition of the
associated topological operators, suggesting 1-form and 4-form symmetries identical to the
unfrozen gauge theory. In the following we resolve this mismatch using two complementary
techniques.
One approach uses the definition of a local freezing map that specifies which M2 and
M5 brane states are allowed after the inclusion of the fractional flux.1 We show how these
freezing rules come about from a top-down perspective using the relation between M2 branes
within the 7D theory and gauge instantons, in cases the frozen gauge algebra is non-trivial.
However, it can equally be applied in the case of fully frozen gauge dynamics. Extending the
freezing map to the charged extended operators allows the identification of the higher-form
symmetries of the frozen singularities, which can be elegantly captured in terms of the charge
lattices of the unfrozen singularities. We find that while the magnetic 4-form symmetries
are identical to the unfrozen theory, the 1-form symmetry sector is modified. For the fully
frozen theories the 1-form symmetries are broken completely, while for other models they
can be partially broken (D-type singularities). Throughout this derivation the only duality
we use is a circle reduction to IIA so one can view our top-down derivation of why the C
3
holonomy at infinity freezes the ADE singularity in IIA without appealing to the long chain
of dualities currently invoked to argue to the freezing in the literature, e.g. [2,3,79].
Naively, this result leads to a puzzle for the SymTFT: since the singularity and the
boundary topology are not modified, the 8D bulk theory should not change, especially since
the flux responsible for the freezing is localized at the singularity. To accommodate the
reduction of the 1-form symmetry in the 7D theory, we therefore expect a modification of
the physical boundary. While it is clear that this modification must trace back to the non-
1Ananalogousmaphasbeenpreviouslyconstructedfor8Dtheoriesrealizedon7-braneswithO7±-planes
in type IIB [74]. Furthermore, “global” freezing maps for theories with dynamical gravity, i.e., compact
internal spaces, which were derived in dual heterotic compactifications, have appeared in [75–77,6,78]. Note
that the construction of these “global” maps are inherently tied to the presence of dynamical gravity in
these models, and they do not inform the most general local freezings that are possible in M-theory on
non-compact internal spaces.
4

<!-- Page 6 -->

trivial flux in the M-theory realization, it is not immediately clear how to extract this using
the methods we use to derive the local freezing rules.
To clarify how the flux changes the physical boundary of the SymTFT, we utilize the duality between frozen M-theory singularities and twisted circle compactifications of F-theory,
see [2,4]. This complementary derivation precisely recovers the 1- and 4-form symmetries
of the frozen singularities and identifies the charged states in terms of strings and 5-brane
states that behave appropriately under an automorphism of the central elliptic fiber. Again,
we find that the 4-form symmetries are identical to the unfrozen setting while the 1-form
symmetries will in general be modified. This translates into the fact that while the M2 brane
configurations are restricted in the presence of fractional fluxes the M5 brane states are not,
which corroborates our construction of the freezing maps directly in the M-theory setting.
The main advantage of this second approach is that we now have a purely geometric
background Z ∼ = (Y ×S1)/Z on which M-theory compactifies to the 6D theory that is the
d
(untwisted) circle compactification of the frozen M-theory model. For this 6D theory, we
can apply the usual machinery to derive the SymTFT and the boundary conditions. In this
approach we can clearly trace the modification of the 1-form symmetry to a topological term
on the physical boundary at R = 0 that arises from compact torsional 1-cycles in Z. The
physical implications of this sector, which apply also to fully frozen cases, are consistent with
the interpretation of compact torsion cycles in previous works [64,67].
These techniques provide evidence for the existence of a topological counterterm on the
physical boundary, which we also relate to modifications in correlation functions of the
extended operators in the case of the e(1/2) frozen singularity and to modified boundary con-
6
ditions for the 8D SymTFT operators on the R = 0 boundary. The case of E singularity
8
with flux r = 1, which we denote by e(1/4) in our nomenclature, has perhaps the most myste-
4 8
rious symmetry properties. The geometrical structure, both in the frozen M-theory and the
twisted circle compactification description, does not allow for the construction of symmetry
operators, suggesting a trivial 1- and 4-form symmetry sector. Yet, the frozen gauge algebra
is su(2) and one expects Wilson and ’t Hooft operators accounting for Z(SU(2)) = Z 1-
2
and 4-form symmetries. Motivated by the other examples where we find from top-down a
topological term that modifies the 1-form symmetry, we suggest a similar solution to this
mismatch from the bottom-up. Namely, we propose the existence of a counterterm on the
gapless physical boundary which breaks both 1- and 4-form symmetries, explaining why they
cannot be recovered from geometry. Moreover, the counterterm arises as a boundary term
of an 8D TFT sector which trivializes the SymTFT of the 7D frozen gauge theory, thus
resolving the discrepancy.
To summarize, in our analysis of frozen M-theory singularities we obtain the following
results:
• A top-down derivation of how the frozen flux (1.1) causes the g ≡ g gauge theory

## Γ

degrees of freedom localized on C2/Γ to freeze to a lower rank algebra h .
Γ,d
5

<!-- Page 7 -->

• Freezing maps that are used to extract the generalized symmetries of frozen singularities.
• A geometric derivation of the same generalized symmetries using twisted circle compactifications in the F-theory dual.
• A top-down derivation of SymTFT descriptions of the invertible 1- and 4-form symmetry sector of the frozen gauge theories.
• A bottom-up solution to the frozen su(2) theory originating from an E singularity via
8
a local counterterm on the gapless boundary that trivializes the SymTFT, which can
have wider field theory applications.
All of these results demonstrate that frozen singularities not only modify the local gauge
dynamics captured in terms of the gauge algebra, but also the generalized symmetries of the
system in a non-intuitive fashion.
The manuscript is organized as follows: In Section 2 we recall known facts about frozen
singularitiesinM-theoryandhowtheirgaugealgebracanbeextractedfromtheprecisevalue
of the fractional localized flux. We define and motivate the local freezing map, producing
the correct gauge degrees of freedom, in Section 3. This freezing map is then applied to
extract the generalized symmetries of the frozen 7D SYM theory in Section 4. The results
are confirmed geometrically in the F-theory dual description. Section 5 reformulates the
realization of these symmetries at the level of the 8D SymTFT, and discusses a solution to
themysterioussituationofthee(1/4) frozensingularitywhichengineersansu(2)gaugealgebra
8
without 1- and 4-form symmetries. These general results can be used in order to understand
predicted properties of O7+ branes in type IIB and the construction of gravitational 7D
theories in the presence of frozen fluxes, which we summarize in Section 6. We conclude
in Section 7 and point towards some interesting questions for future work. In Appendix A
we give an argument for how the gauge algebras of IIA ADE singularities with a 2-form
(cid:82)
RR flux, i.e., C ̸= 0 for a boundary 1-cycle γ ∈ H (S3/Γ), freeze via a confinement
γ1 1 1 1
mechanism. This argument is independent of (and is consistent with) the argument of [2]
which relies on a dual version of the Freed–Witten anamoly. In Appendix B, we give a
geometrical derivation of the presence of a counterterm for fully frozen singularities. Finally,
Appendix C gives homology computations of the twisted F-theory geometry under resolution
of the singularities.
2 Review of Frozen Singularities
In this section we recall the construction and known properties of frozen singularities in
M-theory. We will mainly recall the facts from [2–4], but see also [1,5–11] for other works
on frozen singularities, possibly in other duality frames.
6

<!-- Page 8 -->

2.1 Unfrozen Singularities
The starting point of a frozen singularity in M-theory is an ADE singularity, [2,3], described
by the quotient C2/Γ. The discrete groups Γ are subgroups of SU(2) and allow for an ADE
classification. The A-series corresponds to Γ = Z , the D-series to the binary dihedral
n
group, and the exceptional groups are given by the binary tetrahedral group for E , the
6
binary octahedral group for E , and the binary icosahedral group for E , respectively. In
7 8
the following we will specify which group we refer to by the notation Γ .

## G

Each of the unfrozen ADE singularities can be resolved into a smooth asymptotic locally
Euclidean (ALE) space, which we will denote by X(cid:101) . This involves the blow-up of a number

## Γ

rank(g ) curves E , which topologically are 2-spheres S2 ≃ P1, where g is the non-Abelian

### Γ i Γ

Lie algebra associated to Γ. These curves intersect according to the associated Dynkin
diagram, producing the (negative of) the Cartan matrix C of g :
ij Γ

## E ·E = −C . (2.1)

i j ij
The asymptotic geometry of such a singularity is described by

## ∂(C2/Γ) = S3/Γ, (2.2)

a generalized lens space whose homology (we consider integer valued (co)homology in this
work unless stated otherwise) is
H (S3/Γ) = {Z,Ab(Γ),0,Z} , (2.3)
∗
where Ab(Γ) := Γ/[Γ,Γ] denotes the Abelianization of Γ.
Putting M-theory on such a singular background produces an N = 1 super-Yang–Mills
(SYM) gauge theory with gauge algebra given by g . Going to the resolution X(cid:101) corresponds

## Γ Γ

to an adjoint Higgs mechanism breaking the gauge theory to its maximal torus, the Cartan
subalgebra. This identifies the Cartan generators to be associated to the reduction of the
M-theory 3-form C with respect to the harmonic forms dual to the blow-up curves E , which
3 i
we denote by ω . This can be written as the decomposition
i
√ rank(gΓ)
(cid:88)
C = −1 A ∧ω +... , (2.4)
3 i i
i=1
where we omit the other components such as the resulting 7D 3-form field. We will use a
quantization condition for C , such that (cid:72) dC ∈ Z is an integer, at least in the absence of
3 3
7

<!-- Page 9 -->

a shifted quantization condition [80]. The topological term in M-theory given by2
(cid:90)
2π
Stop. = C ∧G ∧G , (2.5)

## 11D 6 3 4 4

produces a 7D coupling, on the Coulomb branch of the gauge theory, given by
(cid:90)
2π
Stop. ⊃ C C ∧F ∧F , (2.6)
7D 2 ij 3 i j
where we used the duality of ω to E with intersection matrix given by (2.1). In the singular
i i
limit, i.e., in the limit of vanishing volumes for the curves E one obtains more massless
i
states originating from wrapped M2 branes on E . These provide the W-bosons necessary
i
for the non-Abelian gauge enhancement to gauge algebra g on C2/Γ. In this limit the term

## Γ

(2.6) enhances to
(cid:90)
1
Stop. ⊃ 2π C ∧ Tr F2, (2.7)

## 7D 3 4 Gγ

where the trace Tr = 1 Tr is normalized in such a way that a unit G instanton on
Gγ h∨ adjoint Γ

## G

R4 satisfies
(cid:90)
1
Tr F2 = 1. (2.8)
4

## Gγ


## R4

Here, G denotes the simply-connected Lie group associated to the Lie algebra g . Recall

## Γ Γ

that a unit instanton configuration in R4 implies that the gauge field along the asymptotic
boundary ∂R4 = S3 is A = g−1dg where g : S3 → G has a homotopy class 1 ∈ π (G ). For

## Γ 3 Γ

more details on deriving topological terms on ADE singularities see Appendix B of [81].
2.2 Frozen Singularities
The frozen singularities have the identical spacetime geometry, given by C2/Γ, with the only
difference that one includes a non-trivial holonomy of C on the asymptotic boundary S3/Γ
3
(cid:90)
n
r ≡ C = mod 1, gcd(n,d) = 1. (2.9)
3
d

## S3/Γ

(cid:82)
Extending this to the interior, we can equivalently write r = G and will often refer

## C2/Γ 4

to the value of r as the frozen flux of the singularity. More generally, one can consider a
(cid:82)
non-compact K3 manifold X, such that C = n/d. For example, X can be a type I∗

## ∂X 3 0

(cid:82)
Kodaira surface with C = 1/2.

## ∂X 3

The inclusion of this flux has drastic consequences. In particular it produces a potential
energy which obstructs the full resolution of the singularity to X(cid:101) , i.e., some of the moduli

## Γ

fields are frozen at their singular value. Considering the identification of the moduli space
2Throughout this paper, we use conventions where path-integral integrand is exp(iS).
8

<!-- Page 10 -->

with the Coulomb branch, this indicates a modification of the gauge theory sector localized
on the frozen singularities. This is indeed the case as argued for in [2,3], and we provide the
frozen gauge algebras in Table 2.
g so(2k +8) e e e e e e e e e e

### Γ 6 6 7 7 7 8 8 8 8 8

r = n 1 1 1, 2 1 1, 2 1, 3 1 1, 2 1, 3 1, 2, 3, 4 1, 5
d 2 2 3 3 2 3 3 4 4 2 3 3 4 4 5 5 5 5 6 6
h sp(k) su(3) ∅ so(7) su(2) ∅ f g su(2) ∅ ∅

### Γ,d 4 2

Table 2: Frozen half-BPS M-theory singularities of the form C2/Γ as they appeared in [4]
(note, however, that in our conventions sp(k) denotes the rank k C-series).
We denote the frozen gauge algebra, which can be empty, by h . The associated 7D

### Γ,d

N = 1 SYM sectors localized on the frozen singularity are denoted by T (M)[D(1/2)] for the
k
D-type cases and T (M)[e(n/d)] for the E-type cases.3
k
We see from Table 2 that the allowed values of r depend on the type of singularity
determined by Γ, [2,3]. A necessary and sufficient condition for a fraction r to be a valid
monodromy for a given g according to [2] is for d to be a co-mark (also known as a dual

## Γ

Coxeter label) of the Lie algebra g . Since r is defined modulo integers, d must be bigger

## Γ

than one, which means that A-type Lie algebras cannot appear as frozen backgrounds as
A has co-marks given by 1 for all of its nodes. The possible frozen singularity backgrounds
n
come from enumerating all possible n and d subject to this condition (see Figure 2 for the
co-marks of nodes for D- and E-type Lie algebras).
To illustrate this rank reduction let us recall the example of the frozen D-type singularity as discussed in [3]. There it was noted that if one embeds the M-theory D frozen
4+k
singularity into an Atiyah–Hitchin manifold, one can reduce on a transverse circle to go to a
type IIA description. In particular, one finds a type IIA configuration with k D6 branes and
an O6+ plane, as opposed to an O6− plane, due to the B holonomy induced by the C field
2 3
in M-theory. Indeed, such a system has a perturbative gauge algebra given by sp(k). The
same argument, however, does not apply for the E-type singularities for which one needs to
go to dual descriptions.
One way of doing so, described in [2], is to use duality between the heterotic string
on T3 and M-theory on a compact K3 manifold. In case the K3 manifold contains frozen
ADE singularities the dual heterotic theory contains non-trivial gauge configurations of the
heterotic gauge fields on T3, so-called triples, which induce the required rank reduction.
However, it is not clear how to extend this to non-compact backgrounds. Perhaps one hint
is that d always divides the order of |Γ| but this does not account for the intricacies of the
Lie algebras in Table 2. Another alternative to extract the frozen gauge algebras is discussed
3We are using different fonts for aesthetic reasons only.
9

<!-- Page 11 -->

in[4],seealso[79]. Forthatoneneedstoreducethe7DgaugetheoryonT3 tofourdimensions
and T-dualize along all three circle directions. The frozen flux is then captured by a triple
for g gauge fields on T3, whose Chern–Simons invariant precisely reproduces the allowed

## Γ

values of r in Table 2. The vacuum expectation values for the gauge fields on T3 break the
gauge algebra to h∨ , the commutant of the triple, which translates to its Langlands dual

### Γ,d

h after the three T-dualities, producing the entries in Table 2.

### Γ,d

We see that the extraction of the frozen gauge dynamics is rather indirect and makes
heavy use of several dualities. In the next section we provide a more direct path to obtaining
these using a local freezing map and motivate it from a top-down perspective.
3 M-theory on Frozen ADE Singularities
In this section we present our so-called freezing map which takes as input a Lie algebra g

## Γ

corresponding to the ADE singularity C2/Γ, an integer d which appears in the denominator
(cid:82)
of the frozen flux r ≡ C = n/d, and outputs the Lie algebra h of the theory

### S3/Γ 3 Γ,d

associated to the frozen singularity. While the specific type of frozen theory also depends on
the numerator n, this does not affect the frozen gauge algebra h as long as n and d are

### Γ,d

co-prime. Global versions of such freezing maps have appeared in the literature as far back
as[2,3]byrelatingM-theoryfrozensingularities(embeddedinsideofacompactK3manifold)
to heterotic/CHL strings on T3, possibly without vector structure [1]4. Additionally, a
local picture of the freezing g → h can be argued by relating the frozen backgrounds

### Γ Γ,d

compactified on T3 to a Higgsing of g after a T-duality transformation on T3 (see [79] for
moredetails), asmentionedabove. Eachoftheseargumentsare, insomeway, indirectforthe
purpose of understanding why the C -monodromy modifies the gauge algebra. In particular,
3
given a background C monodromy why should M2 brane states wrapped on exceptional
3
cycles be restricted?
Our freezing map, while following from a fairly simple ansatz, recovers each of the frozen
algebras in Table 2 and gives an explicit embedding of the root/weight lattices of h into

### Γ,d

the respective lattices of g . We then give an argument for how this rule comes about from

## Γ

a top-down perspective in Section 3.2.
3.1 A Local Freezing Map
To describe this freezing rule, first recall that a resolved ADE singularity X(cid:101) contains a

## Γ

collection of curves E intersecting according to the negative Cartan matrix, see (2.1) above.
i
Denoting the root lattice of g by Λg we can choose a basis of roots, {α }, such that
Γ root i
(α ,α )
i j
2 = (α ,α ) = +C . (3.1)
i j ij
(α ,α )
i i
4See also [77,6,7,78] for more recent analyses of freezing maps for heterotic strings on tori.
10

<!-- Page 12 -->

Here, (−,−) is a norm on Λg , and we have used the convention that the norm-squared of
root
all of the simple roots of g are 2. That they can be given the same norm is possible because

## Γ

g is simply-laced. This means that we can identify the homology lattice H (X(cid:101) ,Z) with

## Γ 2 Γ

Λg , the lattice pairing with the intersection product, (v,w) = −v · w, and we will often
root
write E and α interchangeably.
i i
In Figure 2, we denote the affine Dynkin diagrams for the D- and E-type simple Lie
algebras. The nodes are labeled by certain integers called dual Coxeter labels (also known
as co-marks) which we denote by d , i = 0,...,rank(g ). These integers appear in several
i Γ
algebraic identities (for a helpful review see [82]) and play a central role in our freezing map.
Recall first that for a non-affine Lie algebra g , we can identify the affine node of the affine

## Γ

Dynkin diagram with the highest root vector θ(g ) ∈ Λg . Such a vector is the highest

### Γ root

weight vector of the adjoint representation of g and it has an expansion in the α-basis as

## Γ

rank(gΓ)
(cid:88)
θ(g ) = d α . (3.2)
Γ i i
i=1
Strictly speaking, (3.2) defines the Coxeter labels but these are identical to the dual Coxeter
labels because g is simply-laced. If we define α ≡ −θ(g ) then we have an identity

## Γ 0 Γ

rank(gΓ)
(cid:88)
d α = 0, (3.3)
i i
i=0
which has a natural geometric interpretation when C2/Γ is included in an elliptic fibration
over C. Namely, (3.3) relates the homology class of the generic elliptic torus to a linear
combination of the exceptional cycles. Additionally, the dual Coxeter labels of g are related

## Γ

to its dual Coxeter number, h∨ , by
gΓ
rank(gΓ)
(cid:88)
h∨ = d . (3.4)
gΓ i
i=0
It has been previously noted (see for instance Section 4.6.6 of [2] and Section 6.4 of [3]) that
when turning on a frozen flux r = n ̸= 0, the algebra h can intuitively be obtained by
d Γ,d
dividing the dual Coxeter labels of g by d and throwing away the nodes in the affine Dynkin

## Γ

diagramwhosedualCoxeterlabelsarenotdivisiblebyd. Thisintuitionwasmotivatedbythe
fact that M-theory on a compact singular K3 with frozen localized fluxes is dual to heterotic
string theory on T3 with a background e , e , e , or so(8 + 2k) connection whose Chern–
8 7 6
Simons invariant evaluates to the fraction r. The algebras h arise as the commutator

### Γ,d

subgroups of such connections and the dependence on the dual Coxeter labels follows from
the properties of such flat connections on T3 [83].
Determining the frozen algebras as a commutator subgroup is a bit roundabout from
11

<!-- Page 13 -->

Figure 2: D- and E-type affine Dynkin diagrams. The dual Coxeter labels, d , are written in
i
the center of the corresponding node. We also label the simple roots α , i = 0,1,...,rank(g).
i
We note for completeness that A-type affine Dynkin diagram nodes all have a dual Coxeter
label d = 1.
i
12

<!-- Page 14 -->

the M-theory point-of-view however, and is not even technically possible for non-compact
frozen singularities since there is no duality to heterotic string theory without a compact
embedding. In the M-theory frame, the W-bosons of the h vector multiplet will still arise

### Γ,d

from M2 branes wrapping some of the exceptional cycles of X(cid:101) . This is clear from the fact

## Γ

that on a generic point of the Coulomb branch of the 7D h gauge theory, the resolution

### Γ,d

X(cid:101) → X contains rank(h ) independent exceptional cycles (one for each low-energy U(1)

### Γ Γ,d

gauge factor) and X(cid:101) contains the minimal frozen singularity for a given value of r. From

## Γ

Table 2 the minimal singularity is D for r = 1/2, E for r = ±1/3, and E for r = ±1/4.
4 6 7
Values of r = ±1/5 and ±1/6 always fix the gauge algebra to be trivial. Since M2 branes
wrapping exceptional cycles fill out the root lattices of g and h and the unfrozen case

### Γ,d

includes all possible hyper-K¨ahler resolutions on its Coulomb branch we can conclude that
that
Λh ⊂ Λg . (3.5)
root root
We can then formalize the intuition of “throwing away Dynkin nodes whose dual Coxeter
labels are not divisible by d” by the following ansatz:
Freezing Rule: β ∈ Λh ⇐⇒ β ·α = 0 whenever d ̸ | d (i = 0,...,rank(g)). (3.6)
root i i
Together with requirement that the norm of long roots β is (β,β) = 2d, something which
we prove in Section 3.2, this ansatz recovers all of the root lattices for the frozen algebras
with just the input of g and the integer d. We list the root systems for all of the non-trivial

## Γ

frozen algebras obtained this way in Table 3. The trivial frozen algebras lattices are also
(cid:80)
recovered in the sense that the minimal solution to (3.6) is the sum β = d α which
0 i i i
equals 0 by (3.3).
One can also perform a similar freezing on the weight lattice of g , Λg ⊃ Λg , to

### Γ wt root

obtain the weight lattice of h . Physically, Λg corresponds to M2 branes wrapping relative

### Γ,d wt

homology 2-cycles H (X(cid:101) ,∂X(cid:101) ) which include non-compact 2-cycles with non-trivial image

## 2 Γ Γ

in H (∂X(cid:101) ) in addition to the compact exceptional 2-cycles. We will have more to say

## 1 Γ

about such non-compact cycles in Section 4 where they will play a central role in calculating
the defect groups/higher-form symmetries of the frozen theories T (M)[g(n/d)]. One can also
generalize the freezing rule (3.6) to solve for the coroot and coweight lattices of h for which

### Γ,d

we will have more to say in Section 3.2. Physically, such lattices capture the charges of M5
branes wrapped on exceptional 2-cycles and relative 2-cycles, respectively, and are also key
in calculating the 7D defect groups.
3.2 Top-Down Derivation
We now give a top-down argument for how to obtain the frozen algebras which relies directly
(cid:82)
on the physical effects resulting from frozen flux r = G in the M-theory or type IIA

## C2/Γ 4

frame after compactifying on a circle. Outlining the discussion, we will first argue that
13

<!-- Page 15 -->

Figure 3: Non-Simply laced affine Dynkin diagrams which arise from M-theory frozen singularities. The dual Coxeter labels, d , are written in the center of its corresponding node.
i
We also label the simple roots β , i = 0,1,...,rank(h).
i
the Coulomb branch of an M2 brane probing a frozen singularity is a moduli space of d
instantons in R4 with gauge algebra h , whatever h may be. This statement gives a

### Γ,d Γ,d

constraint on the index of the sublattice Λh ⊂ Λg which fixes h in certain cases. After
root root Γ,d
reducing on a circle to IIA, we find that the frozen flux causes some of the U(1) gauge factors
in the quiver gauge theories of D2 and D0 probes to be anomalous. Such anomalous U(1)
factors do not survive at low-energies which allows us to write down a general formula for
rank(g )−rank(h ) and to solve to for h in general.

### Γ Γ,d Γ,d

Instanton Fractionalization RememberthereductionofM-theoryonADE singularities
discussed in Section 2.1, which produced the term
(cid:90)
1
Stop. ⊃ 2π C ∧ Tr F2, (3.7)

## 7D 3 4 Gγ

in the singular limit. It tells us that integer instantons in the gauge theory sector have an
integer M2 brane charge, since they couple to the 3-form field C .
3
Turning now to frozen singularities, we naively cannot use the same argument to derive
(3.7) because we suspect that the rules for blowing up the ADE singularity are restricted by
a potential energy in the presence of the G flux. What we can do, however, is to understand
4
what kind of object a single M2 brane probe is from the point-of-view of the frozen gauge
theory. When h ̸= ∅, we can perform a partial blowup of C2/Γ and obtain a topological

### Γ,d

term proportional to (2.6). Blowing down the singularity and using h gauge invariance,
Γ,d
14

<!-- Page 16 -->

Frozen Singularity Frozen Algebra Frozen Root System
D(1/2) sp(1) β = α +α +2α
5 0 0 1 2
β = 2α +α +α
1 3 4 5
D(1/2) (k > 1) sp(k) β = α +α +2α
4+k 0 0 1 2
β = α (1 ≤ i ≤ k −1)
i i+2
β = 2α +α +α
k k+2 k+3 k+4
e(1/2) su(3) β = α +α +2α
6 0 0 3 6
β = α +2α +α
1 1 2 3
β = α +2α +α
2 3 4 5
e(1/2) so(7) β = α +2α +α
7 0 0 1 2
β = α +2α +α
1 4 5 6
β = α +2α +α
2 2 3 4
β = α
3 7
e(1/3) su(2) β = α +2α +3α +2α +α
7 0 0 1 2 3 7
β = α +2α +3α +2α +α
1 7 3 4 5 6
e(1/2) f β = α +2α +α
8 4 0 0 1 2
β = α +2α +α
1 2 3 4
β = α +2α +α
2 4 5 8
β = α
3 6
β = α
4 7
e(1/3) g β = α +2α +3α +2α +α
8 2 0 0 1 2 3 4
β = α +2α +3α +2α +α
1 3 4 5 6 7
β = α
2 8
e(1/4) su(2) β = α +2α +3α +4α +2α
8 0 0 1 2 3 4
β = 2×(α +2α +2α +α +α )
1 4 5 6 7 8
Table 3: Here we list the vectors in the affine root system for the non-trivial frozen algebras
which we label by β . For labeling conventions, see Figure 2 and 3. In each case, the noni
affine vectors (i ̸= 0) span the frozen root lattice Λh which is a solution to the freezing
root
rule (3.6). These are the maximal lattices which satisfy such a constraint with the exception
of the e(1/4) frozen theory. The overall factor of 2 in β for this case is required for later
8 1
considerations of instanton fractionalization in Section 3.2.
we obtain
(cid:90)
1
Stop. ⊃ 2πK C ∧ Tr F2. (3.8)
7D Γ,d 3 4 HΓ

## M7

where the constant K is the M2 brane charge of a unit charge instanton of the h gauge

### Γ,d Γ,d

theory5. As mentioned previously, we know that the root lattice of a frozen gauge theory
is a sublattice of the corresponding unfrozen theory (3.5). We can express K in terms of

### Γ,d

5We know that K ̸= 0 because if h ̸= ∅, one can partially resolve the singularity and obtain a

### Γ,d Γ,d

C ∧F ∧F term again from reducing the C ∧G ∧G on the resolved 2-cycles.
3 3 4 4
15

<!-- Page 17 -->

this data as
(θ(g ),θ(g ))

## Γ Γ


## K = , (3.9)


### Γ,d

(θ(h ),θ(h ))

### Γ,d Γ,d

where θ(g ),θ(h ) ∈ Λg are respectively the highest root vectors of g , and h and

### Γ Γ,d root Γ Γ,d

(−,−) is the norm on Λg mentioned in (3.1). To understand how equation (3.9) follows
root
from (3.7) and (3.8), we see that roughly K Tr F2 = Tr F2. Such a relation is sensible

### Γ,d HΓ GΓ

if one restricts to gauge configurations in the maximal torus of the frozen gauge algebra.
Equation (3.9) then follows from the fact that the Killing form of a Lie algebra is fixed by
the normalization of ( , ) (see for instance Chapter 18 of [82]). The frozen roots β obtained
i
from the freezing rule in Table 3 suggests that
1

## K = , (3.10)

Γ,d
d
as one can check using the fact that θ(h ) is a long root and computing the norm squared

### Γ,d

of any one of the long frozen roots.
Our goal now is to show why K = 1/d from a stringy perspective. Physically, this

### Γ,d

means that M2 branes can fractionate into d fractional M2 branes on frozen singularities
as one can always consider a unit instanton configuration of the frozen gauge theory. In
other words, the 3D N = 4 Coulomb branch of the probe M2 brane is the moduli space of d
H -instantons in R4. Such a fractionalization is apparent in various dual frames. As noted

### Γ,d

in [3], embedding a D(1/2) singularity into an Atiyah–Hitchin manifold produces k D6 branes
4+k
probing an O6+ plane and the fractionalization follows from the fact that the enhancement
due to the orientifold plane, u(k) (cid:44)→ sp(k), specifies a group embedding of Dynkin index
two. By definition [84], we have a relation of the traces 2Tr = Tr which implies that

### U(k) Sp(k)

a D2 can fractionate in two on the O6+ plane. Our goal here is to not appeal to dualities.
One can first consider the scenario depicted in Figure 4. On both sides of the Figure
we have a 1M5 brane acting as a interface separating a non-frozen D- or E-type singularity
d
with gauge algebra g from a frozen singularity with gauge algebra h ; for details on the

### Γ Γ,d

worldvolume theories of such fractional M5 branes see [85]. If we place an M5 brane with
worldvolume Σ ×C2/Γ on the unfrozen singularity and drag it across the 1M5 brane domain
2 d
wall to the frozen singularity, then a 1M2 brane is created due to the Hanany–Witten (HW)
d
effect6 [86]. The table below indicates where the branes in this setup are located (the 7D
theory spacetime directions are 0,1,...,6):
0 1 2 3 4 5 6 7 8 9 10

## 1M5 × × × × × ×

d (3.11)

## M5 × × × × × ×


## 1M2 × × ×

d
6Recall that in M-theory, the HW effect is just a consequence of the 11D bulk equation of motion
dG =G ∧G .
7 4 4
16

<!-- Page 18 -->

Figure 4: A Hanany–Witten transition between an M5 brane filling the space C2/Γ and a
1M5 filling a codimension-one subspace of the ADE singularity which creates a 1M2 brane
d d
(solid black line). The C2/Γ singularity is illustrated by the blue dotted line and to the left
of the 1M5 the gauge algebra is g and is h to the right of it.
d Γ Γ,d
Importantly, notice that it is not possible to place an M5 brane filling C2/Γ to the right
of the 1M5 domain wall and create a 1M2 to the left of the domain wall because of the M5
2 d
(cid:82)
worldvolume coupling C ∧db where b couples to an M2 brane ending on the M5. From

## M5 3 2 2

(cid:90) (cid:90) (cid:90)
1
C ∧db = G ∧b = b , (3.12)
3 2 4 2 2
d

## M5 M5 Σ2

we see that the M5 brane with worldvolume Σ ×C2/Γ is forced to have a 1M2-brane ending
2 d
on it. This addresses a conjecture of [2] (see Section 4.6.6) that only a multiple of d M5
branes can fill all four real directions of a frozen ADE singularity with flux r = n/d. We see
that this condition can be relaxed provided we include the fractional r ×M2 ending on the

## M5.

Now consider a frozen singularity by itself without any domain wall to an unfrozen
singularity. If we have an M5 and an anti-M5 brane on the frozen singularity both with
worldvolumes Σ ×C2/Γ, albeit separated along a transverse direction, one then has a 1M2
2 d
brane stretched between them. We can then send these M5 endpoints to infinity to see
that we can simply have a probe 1M2 brane localized on the frozen singularity. Putting d
d
of these fractional branes together just produces an M2 brane and of course reversing the
process shows that it can fractionate. This shows that (3.10) holds. More generally, for
frozen singularities of type g(n/d), for n ̸= 1, the previous argument shows that an M5 with
worldvolume Σ × C2/Γ has a nM2 brane attached to it. Since n and d are coprime, one
2 d
can bring a sufficient number of these fractional branes together to create a 1M2 plus some
d
17

<!-- Page 19 -->

integer amount of M2 branes which we can separate away.
Consequences of Instanton Fractionalization Given the instanton fractionalization
statement, we are left with the following mathematical question: given a simply-laced Lie
algebra g , what are the sublattices of Λg which are the root lattice for a Lie algebra h

### Γ root Γ,d

such that the highest weight vector of h satisfies (θ(h ),θ(h )) = d·(θ(g ),θ(g )) = 2d?

### Γ,d Γ,d Γ,d Γ Γ

Note that if d > 1, such sublattices cannot be obtained from taking subalgebras of g .

## Γ

This is because if k ⊂ g , then

## Γ

(θ(g ),θ(g ))

## Γ Γ


## N = (3.13)

(θ(k),θ(k))
where N is the Dynkin index of the subalgebra7 (see [82]). Because N ∈ N , this means
+
that a frozen algebra h cannot be a subalgebra of g as it would be inconsistent with the

### Γ,d Γ

instanton fractionalization.
It turns out that we can characterize root/weight sublattices with the correct instanton
fractionalization in a simple manner by their coroot/coweight lattice. Recall that a vector v
of the root system of any Lie algebra can be transformed into an element v∨ of the coroot
system by
2v
v∨ := . (3.14)
(v,v)
The generators of the coroot lattice Λ are obtained from applying (3.14) to the simple
coroot
roots in Λ . We see that the choice of norm (3.1) is convenient in the sense that it specifies
root
a lattice isomorphism Λg ≃ Λg because g is simply-laced. On the other hand, acting
root coroot Γ
by (3.14) on the simple roots of h, i.e., the generators of the frozen sublattice Λh will not
root
specify a lattice isomorphism, simply because the norm-squared of θ(h ) is larger than 2.

### Γ,d

It is well-known that the lattice Λh can be thought of as a root lattice for an algebra h∨
coroot
which is Langlands dual to h. We emphasize that even if h and h∨ are isomorphic to the
same simple Lie algebra, their root lattices will be distinct as sublattices of Λg .
wt
The upshot of studying Λh = Λh∨ is that it specifies a subalgebra h∨ ⊂ g. Specifically,
cowt wt
from
Λh∨ ≃ Hom(Λh ,Z)
wt root
v∨ (cid:55)→ (−,v∨)
we see that the embedding Λh ⊂ Λg can dually be presented as a projection map
root root
π : Λg ↠ Λh∨ (3.15)
wt wt
7One way to define the Dynkin index of a subgroup of a Lie group (which descends to the definition of
Dynkin index at the Lie algebra level) is that H (cid:44)→G induces a map H3(BG,Z)→H3(BH,Z). Assuming
G and H are simple groups, then we have a map Z→Z and the Dynkin index is the image of 1∈Z.
18

<!-- Page 20 -->

To see the utility of (3.15), recall that for a given Lie algebra f with t∗ := Span Λf as the
f R wt
weight space of f, the Cartan subalgebra of f is the dual of this, (t∗)∗ = t . By taking the real
f f
span and the dual of (3.15), we have an explicit embedding of the Cartan subalgebra of h∨
into the Cartan subalgebra of g. This data is enough to specify the full embedding h∨ ⊂ g
because(3.15)alsospecifieshowg-representationsdecomposesintoh∨-representations. That
we can characterize the frozen algebra by its Langlands dual is not new as one can explicitly
understandhowh∨ arisesasaHiggsingofgafterplacingthe7DtheoryonT3 andperforming
three T-dualities, see [79] for details.
Let us now compute the Dynkin index of the embedding h∨ ⊂ g. This can be done
straightforwardly by applying (3.9) and (3.14):
(θ(g ),θ(g )) 1 (θ(g ),θ(g )) d2 (θ(g ),θ(g )) d

## Γ Γ Γ Γ Γ Γ

= · = · = . (3.16)
(cid:0) (cid:1)
θ(h∨ ),θ(h∨ ) N (θ(h )∨,θ(h )∨) N (θ(h ),θ(h )) N

### Γ,d Γ,d h Γ,d Γ,d h Γ,d Γ,d h

Here we have defined the integer N as the ratio between the norm-squared of θ(h∨ ) and
h Γ,d
that of θ(h )∨. The highest weight vector is always a long root which means that θ(h )∨

### Γ,d Γ,d

is a short coroot of h or, equivalently a short root of h∨. So N is simply the ratio between
h
the norm-squares of the long and short roots of h∨ (which is the same ratio for h) so

  1, h Γ,d is simply-laced

N = 2, h is a B- or C-type, or f algebra (3.17)
h Γ,d 4


3, h a g algebra

### Γ,d 2


### Therefore we arrive at the statement:

Given a frozen algebra h , there exists a subalgebra h∨ ⊂ g of Dynkin index d/N

### Γ,d Γ,d Γ h

For a given frozen flux r = n/d, there may a priori be several possible h∨ ⊂ g which

### Γ,d Γ

satisfy such a statement. We know that h∨ ⊂ g cannot be a regular subalgebra because a

### Γ,d Γ

regularsubalgebraofasimply-lacedLiealgebrahasDynkinindex1andisitselfsimply-laced.
A subalgebra that is not regular is a special subalgebra (also referred to as an S-subalgebra)
and in Table 4 we list all possible special subalgebras of g for the minimal D-type and the

## Γ

E-type cases. We see from this table that we have some spurious candidates. For instance,
we see for the frozen D singularity that, up to taking further subgroups, there are three
4
candidate non-trivial (Langlands duals of) frozen algebras even though we suspect from
dualities and compute from the freezing rule that h = ∅ in this case. For the e(1/2) case,

## Γ,2 7

we have two candidate subalgebras from Table 4 namely sp(3) and f . The former is correct
4
as (h∨ )∨ = (sp(3))∨ = so(7) while we still cannot eliminate the latter from our instanton

## Γ,2

fractionalization argument alone. Note that for the e(1/4) case, one can obtain the correct
8
index-4 subgroup su(2) ⊂ e because there is a Dynkin index-4 subgroup su(2) ⊂ g and
8 2
19

<!-- Page 21 -->

Frozen Singularity Relevant Maximal S-Subalgebras
D(1/2) so(7)[1], so(5)[1], su(2)[2]
4
e(n/d) sp(4)[1], f[1], su(3)[2] ⊕g[1]
6 4 2
e(n/d) su(2)[3] ⊕f[1], sp(3)[1] ⊕g[1], su(2)[7] ⊕g[1]
7 4 2 2
e(n/d) f[1] ⊕g[1]
8 4 2
Table 4: Here we list the maximal special (S) subalgebras of g relevant to our discussion,

## Γ

see [82]. The superscript denotes the Dynkin index of the subgroup. Simple subgroups of
these with index d/N are candidates for Langlands dual to the frozen algebras.
h
Dynkin indices are multiplicative under taking sequences of subgroups8.
Aside on D-brane Quivers Given the limitations on the constraint of having the correct
instanton fractionalization on the frozen singularity, we now seek to derive a formula for the
rank and dual Coxeter number of the frozen algebra. Our approach will be to reduce on a
transverse circle to the IIA frozen background
(cid:18) (cid:90) (cid:19)
n

## Iia X = C2/Γ, C = , (3.18)

3
d

## ∂X

and study the quiver gauge theories living on BPS Dp probes of this frozen singularity.
Recall that the low-energy physics of Dp probes of unfrozen ADE singularities are described
by (p+1)-dimensional gauge theories with 8 supercharges whose gauge/matter content are
summarized by a quiver given by the affine ADE Dynkin diagram [89,90]. While we expect
in the frozen cases that the Douglas–Moore quivers of such theories will be in the shape of
the affine Dynkin diagrams of h , such a derivation is outside of the scope of this work

### Γ,d

and would in principle require one to understand how open strings behave on non-trivial RR
backgrounds. Our goal will be more modest. We will show that certain simple gauge theory
factors that appear for the Dp probe branes for the unfrozen singularity develop a gauge
anomaly in the presence of the frozen flux.
For concreteness, let us consider a D0 probing the e(1/2) IIA frozen singularity. Without
6
the frozen flux, the 1D field theory content consists of the gauge group

## G = U(1)3 ×U(2)3 ×U(3), (3.19)

quiv.
and N = 8 bifundamental hypermultiplets associated with each of the links of the affine
e quiver, see Figure 2. The Coulomb branch of this theory parameterizes the motion of
6
fractional D0 branes along the R6 parallel to the singularity of the D0 brane along the R6
parallel to the singularity. In general the real dimension of this Coulomb branch is 5×h∨.9
g
8For physicist-friendly resources on special subalgebras, see [87] and [88].
9The factor of 5 is from the transverse directions, while the dual Coxeter number is related to the quiver
20

<!-- Page 22 -->

For instance, the scalars in the U(k) vector multiplets correspond to positions of k D0 branes
24
where the 1/24 fraction is due to the fact that |Γ | = 24. The U(k) gauge factor in total

## E6

then describes k coincident k D0 branes.
24
Let us denote the 1-form gauge potentials for each factor of (3.19) by a(i), b(j), and c
(cid:82)
where i,j = 1,2,3. In the presence of the frozen flux G = 1/2, we claim that we

## C2/Γe6 4

have the additional topological terms
(cid:32) (cid:33)
(cid:90)
1 (cid:88) (cid:88)
a(i) +2 Tr(b(i))+3Tr(c) (3.20)
2

## L

i i
where L is the D0 brane worldvolume. These terms are neither invariant under U(1) nor
U(3) large gauge transformations due to their fractional coefficients. To see how such terms
can arise, consider the flux background in flat space
(cid:18) (cid:90) (cid:19)

## Iia X = C2, G = 12 . (3.21)

4

## X

Orbifolding such a background by the binary tetrahedral group Γ produces the e(1/2) frozen

## E6 6

singularity because of the normalization of the volume forms:
(cid:90) (cid:90)
= 24 . (3.22)

## C2 C2/Γe6

Also, a single D0 brane at the origin of C2 becomes a 1 D0-brane at the origin of C2/Γ

## 24 E6

upon oribifolding. Notice that a D0 brane can be formed by taking a D4 and D4 pair along
C2×L and turning on an Abelian instanton background localized at the origin10. Explicitly,
we have a Wess-Zumino coupling
(cid:90)
C ∧(f −f )2, (3.23)
1 + −

## C2×L

where f are the field strengths for the U(1) ×U(1) gauge group of the D4/D4 stack. This
± + −
couplingimpliesthataD0braneembeddedinsideoftheD4/D4stackcanbeengineeredfrom
(cid:82)
a singular Abelian instanton background (f −f )2 ∼ δ as this localizes to C [92]. As

## + − L L 1

standardinrealizingbranesfromhigher-dimensionalbranes,theU(1)gaugegroupassociated
with the D0 is a subgroup of U(1) ×U(1) with potential a := (a −a ). The key point
+ − + −
is that the 4-brane stack also contains the term
(cid:90) (cid:90) (cid:90)
C ∧(f −f ) = G ∧(a −a ) = 12 a (3.24)
3 + − 4 + −

## C2×L C2×L L

gauge group (cid:81)rank(g)U(n ) as h∨ = (cid:80)rank(g)n .
i=0 i g i=0 i
10Note that one can more rigorously treat a U(1) instanton localized in R4 by turning on a small B-field
background, where the U(1) instanton is smooth in a non-commutative deformation of R4 [91].
21

<!-- Page 23 -->

which localizes to a 1D Chern–Simons term on the D0 with level 12. After orbifolding, the
Wess-Zumino action of this D0 brane is multiplied by 1/24 so its action is now
(cid:90)
1
(C +12a) (3.25)
1
24

## L

where now the second term is not gauge invariant under the large gauge transformation11
(cid:82)
a → a + λ where dλ = 0 and λ = 2π. This argument reproduces all of the a(i) terms

## L

in (3.20). As for the U(3) factor in G , we can consider going unto its Coulomb branch
quiv.
whereby the 3 coincident 1D0 branes are separated from each other at a generic point. Each
8
of these 1D0 branes is associated with a U(1) ⊂ U(3), k = 1,2,3. Now the only thing we
8 k
change is that prior to taking the orbifold we place a charge-3 instanton in the D4/D4 stack
localized at the origin of C2 which engineers 3 D0 branes there. After orbifolding, the analog
of (3.25) is
(cid:90)
3
(cid:0) (cid:1)
C +12c(k) (3.26)
1
24

## L

where c(k) := a(k) −a(k) which is not gauge invariant due to the fractional level 12/8 = 3/2.
+ −
If we take these 1D0 branes to be coincident, then we obtain the 3/2Tr(c) term in (3.20)
8
from the fact that Tr(c) = (cid:80)3 c(k). We note that for D2 and D4 fractional probes, we
k=1
would obtain similar conclusions but with 3D and 5D Chern–Simons terms being non-gauge
invariant due to a fractional level. One can derive these terms from realizing these branes
as instantons inside a D6/D6 pair and a D8/D8 pair, respectively.
What can we conclude then from the fact that the U(1)3 × U(3) ⊂ G subgroup is
quiv.
inconsistent and thus must be projected out of the low-energy degrees of freedom of Dp
probe of e(1/2)? We know generally that the geometric deformations/resolutions of an ADE
6
singularity correspond to Fayet–Iliopoulos (FI) parameters of the quiver gauge theory living
on the Dp probe [89,90]. There is a SU(2) triplet of FI parameters associated to each factor

## R

of G which of course correspond to the blow-ups of the of the ADE singularity. Given
quiv.
that theU(1)3×U(3) gauge factor cannot bepresent, we see that number of possible blow-up
modes of e(1/2) is reduced by 4. In 7D terms, this means that the rank is now 6 − 4 = 2,
6
which singles out the correct frozen gauge algebra h = su(3). It is not difficult to see that

## E6,2

if we repeat the above calculations for any frozen singularity we have the general statement
rank(g )−rank(h ) = # of dual Coxeter labels of g such that d ̸ | d

### Γ Γ,d Γ i

This statement is implied by the freezing rule of Section 3.1, and carries the general spirit of
the dependence on the dual Coxeter labels which, from the point-of-view of gauge anomalies
on the Dp brane probes, arises due to the ranks of the gauge factors in the quiver gauge
group. These ranks ultimately arise from the dimensions of the irreducible representations
of Γ and it would be interesting to understand if there is a full derivation of the frozen

## E6

11We take the worldvolume fluxes to be normalized as (cid:82) f =2πn.
±
22

<!-- Page 24 -->

quiver in terms of this data, similar to how discrete torsion affects quiver representations
(see for instance [93]). In particular, we do not see from this gauge anomaly argument why
the non-anomalous U(2)3 ⊂ G reduces to the expected U(1)3 of the frozen quiver. It
quiv.
would also be desirable to have an anomaly argument directly in the M-theory frame which,
however, seems to be hard to achieve since we heavily used the string theory specific branes
within branes construction associated to gauge fields on Dp branes.
Summarizing our results, we have shown directly in M-theory that the frozen flux implies
an instanton fractionalization condition which gives a restriction on the possible h , which

### Γ,d

can be compactly phrased in terms of the Langlands dual h∨ , and that we can solve for the

### Γ,d

rank of h using Dp probes after circle compactification. These arguments are “duality-

### Γ,d

(cid:82)
free” in the sense that the frozen flux r = C and the orbifold geometry are not changed in
3
any way. What is striking about these two conditions is that they are enough to completely
determine h in all cases. Given the rank reduction formula, the only cases that are

### Γ,d

ambiguous before applying the instanton fractionalization statement are when rank(h ) ≥

### Γ,d

2 and one can check explicitly that the ambiguity goes away. For example, in the case
e(1/2) we know from the Dp probe anomaly statement that rank(h ) = 4 and we know

## 8 E8,2

from the instanton fractionalization that h∨ ⊂ g is a maximal subalgebra with index

## Γ,2 Γ

1 if doubly-laced and 2 if simply-laced. From Table 4 this uniquely fixes h∨ = f which

## E8,2 4

means h = f∨ = f . Finally, notice that the while this freezing leaves M2 branes wrapping

## E8,2 4 4

exceptional2-cyclesoutofthespectrumsimplybecausetheyareinthesamevectormultiplet
as the resolution scalars, we see that there is no such restriction on the lattice of M5 brane
states, a behavior we will confirm in the twisted F-theory duality frame in the next section.
4 Defect Groups of Frozen Singularities
Having established how the G flux reduces the gauge symmetry on ADE singularities, we
4
now turn our attention to defects charged under generalized symmetries in frozen backgrounds. Specifically, we are interested in the group D of defects charged under 1- and
4-form symmetries of T (M)[g(n/d)] [19]. In the non-frozen cases, T (M)[g] has a defect group
D = Z(G)(1) ⊕ Z(G)(4) for the Wilson and ’t Hooft operators, where Z(G) is the center
of the simply-connected Lie group G associated to g. Geometrically, if we let X(cid:101) → C2/Γ

## Γ

denote the fully resolved space, these defects arise from M2 and M5 branes, respectively,
wrapping relative 2-cycles in H (X(cid:101) ,∂X(cid:101) ) ∼ = Hom(H (X(cid:101) ),Z) ∼ = Λg ∼ = Λg , and their
2 Γ Γ 2 Γ cowt wt
charge (screened by M2/M5 branes wrapping compact 2-cycles) is precisely given by [21,22]
Z(G) = Λg /Λg =

## H

2
(X(cid:101)

## Γ

,∂X(cid:101)

## Γ

)
∼ = H (∂X(cid:101) ). (4.1)
wt root 1 Γ
H (X(cid:101) )

## 2 Γ

We have listed the relevant details in Table 5.
For the frozen theories, the relationship between the various group-theoretic and geomet-
23

<!-- Page 25 -->

Singularity Z(G ) Generator(s)

## Γ

A Z w ≡ 1 (cid:80)k−1jα mod ⟨α ⟩
k−1 k 1 k j=1 j i Z
D (k = 4n) Z ×Z w ≡ 1 (cid:80)k+2jα + 1α mod ⟨α ⟩
4+k 2 2 k+3 2 j=1 j 2 k+4 i Z
w ≡ 1 (cid:80)k+2jα + 1α mod ⟨α ⟩
k+4 2 j=1 j 2 k+3 i Z
D (k = 4n+2) Z ×Z w ≡ 1 (cid:80)k+2jα + 1α mod ⟨α ⟩
4+k 2 2 k+3 2 j=1 j 2 k+3 i Z
w ≡ 1 (cid:80)k+2jα + 1α mod ⟨α ⟩
k+4 2 j=1 j 2 k+4 i Z
D (k = 2n+1) Z w ≡ 1 (cid:80)2+kjα + kα + k−2α mod ⟨α ⟩
4+k 4 k+3 2 i=1 j 4 k+3 4 k+4 i Z
e Z w ≡ 1(α +2α +α +2α ) mod ⟨α ⟩
6 3 1 3 1 2 4 5 i Z
e Z w ≡ 1(α +α +α ) mod ⟨α ⟩
7 2 1 2 4 6 7 i Z
e ∅ w ≡ 0 mod ⟨α ⟩
8 1 i Z
Table 5: We list the generators w for the group Z(G ) for each of the ADE singularities/Lie
ℓ Γ
algebras as fractional linear combinations of the simple roots α , which are identified up to
i
integer linear combinations of the α (denoted as ⟨α ⟩ ). The w are fundamental weights
i i Z ℓ
(satisfying (α ,w ) = δ ) known to generate the center, so their coefficients are given by rows
i ℓ iℓ
of the inverse Cartan matrix (modulo 1). Our conventions for the enumeration of α s for the
i
D- and E-type cases follow from Figure 2 and we use the obvious ordering for A-type.
ric lattices are more delicate. As we will see in detail, the freezing rule leads to a non-trivial
identification of the Wilson and ’t Hooft defects of the frozen gauge sector with elements
of H (∂C2/Γ), which in turn will become important for the discussion of the SymTFT in
1
Section 5. This procedure leads to two surprising results. First, we see that, while the line
defects, i.e., wrapped M2 branes, generally suffers a reduction compatible with the rank
reduction of the gauge algebra, the 4-manifold defects from wrapped M5 branes remain
identical to the unfrozen case even though they may not have a clear description as ’t Hooft
defect of the frozen gauge theory. Second, in the specific case of T (M)[e(1/4)] which has an
8
h = su(2) gauge algebra, there are neither line nor 4-manifold defects, as expected from
geometry. We list these results in Table 6.
To corroborate these findings, we perform a geometric analysis of twisted circle compactifications of F-theory on Kodaira singularities that are (essentially) double-T-dual to the
frozen M-theory backgrounds [2,4] which verifies the direct application of the freezing map.
We will suggest a physical interpretation of these results in the next section.
4.1 Defect Groups from Freezing Map
To incorporate the coroot and (co-)weight lattices within the freezing map, it will be convenient to understand the freezing rule (3.6) as follows. First, we indicate the “bad” simple
24

<!-- Page 26 -->

Frozen Singularity D(1) D(4) Z(G ) Z(H )

### Γ Γ,d


## D(1/2) 0 Z2 Z2 0

4 2 2
D(1/2) (k = 2n) Z Z2 Z2 Z
k≥5 2 2 2 2
D(1/2) (k = 2n+1) Z Z Z Z
k≥5 2 4 4 2
e(1/2) Z Z Z Z
6 3 3 3 3
e(1/3) 0 Z Z 0
6 3 3
e(1/2) and e(1/3) Z Z Z Z
7 7 2 2 2 2
e(1/4) 0 Z Z 0
7 2 2
e(r) 0 0 0 0
8
Table 6: Our results for defect groups of M-theory frozen singularities, D = D(1) ⊕D(4).
roots of g, i.e., those α with d ̸ |d , with a tilde. Then we construct the hyperplane E via
i i
H (C2/Γ;R) = Λg ⊗R ⊃ E := (cid:8) v = (cid:80) λ α |λ ∈ R,(v,α ) = 0 (cid:9) . (4.2)
2 root i≥1 i i i (cid:101)j
The arguments of the previous section imply that the M2 branes are only allowed to wrap
2-cycles in
H (X(cid:101) )∩E = Λg ∩E = Λh , (4.3)
2 Γ root root
the restriction of the unfrozen roots to E. As the line defects are M2’s wrapping relative
2-cycles which can be interpreted as fractional linear combination of compact cycles, the
same arguments can be extended to also restrict the weight lattice,
H (X(cid:101) ,∂X(cid:101) )∩E = Λg ∩E =: Λh ⊃ Λh . (4.4)
2 Γ Γ wt w root
Practically, this is most easily computed by first re-expressing the “good” simple roots of g,
i.e., those α with d|d , in terms of (possibly fractional) linear combinations of the “bad”
i i
simple roots α and the frozen simple roots β , allowing us to write the g-weights as w =
(cid:101)j i ℓ
(cid:80) (cid:80)
λ β + µ α . Then the orthogonal weights are integer linear combinations of these
i i i j j(cid:101)j
weights such that the coefficients of α are integer. We will see below that Λh = Λh , the
(cid:101)j w wt
frozen weight lattice, for all cases except for T (M)(e(1/4)).
8
Conversely, the M5 branes wrapped on 2-cycles do not experience any restrictions from
the freezing flux. Hence, we still expect the full set of four-dimensional defects that exist in
the unfrozen theory (and fill out Λg = Λg ⊃ Λg ) to be also present in T (M)(g(n/d)).
cowt wt (co)root
These are generally magnetically charged defects of h, with the charges determined by their
pairing with the roots Λh . Denoting by π the orthogonal projection
root E
π : Λg ↠ E, (4.5)
E wt
25

<!-- Page 27 -->

we clearly have
(u,v) = (π (u),v) ∀u ∈ Λg ,∀v ∈ Λh ⊂ E. (4.6)

### E wt w


### From this, we will verify case by case that

π (Λg ) = Λh , and π (Λg ) = Λh (except for T (M)(e(1/4))), (4.7)

### E root coroot E wt cowt 8

and thus find that π is equivalent to π in (3.15). Together, this will further allow us to

## E

determine the geometric representatives for
Z(H)(1) = Λh /Λh and Z(H)(4) = Λh /Λh (4.8)
wt root cowt coroot
in the boundary homology H (S3/Γ) = Λg /Λg .
1 wt root
Note that while the lattices can be all thought of as embedded into one Euclidean vector
space, it is important for the M-theory interpretation to separate the vectors that correspond
to wrapped M2 vs. M5 branes. In our notation, the lattices Λh and Λh are associated
wt root
with M2 branes, while Λh and Λh are associated with M5 branes.
cowt coroot
(1/2)

## 1 D

4+k
The root lattice of the frozen algebra h = sp(k) is given in Table 3, with the long roots
satisfying (β ,β ) = 4 = 2d and (β ,β ) = 2δ for j ̸= k. It is easy to verify that we have
k k k j k,j−1
(cid:32) (cid:33)
k−1
1 (cid:88) 1
α = − α +α +2 β +β , α = (β −α −α ),
2 0 1 i k k+2 k k+3 k+4
2 2 (4.9)
i=1
α = β , i = 1,...,k −1,
i+2 i
where the “bad” roots of g = so(2k + 8) (those with Coxeter label d = 1) are α ∈
j (cid:101)
{α ,α ,α ,α } which are orthogonal to the β . The orthogonal projection onto E,
0 1 k+3 k+4 i
which is spanned by β as a vector space, is obtained by simply dropping any term propori
tional to any α. This gives π (α ) = − (cid:80)k−1β − 1β , π (α ) = 1β , and π (α ) = β
(cid:101) E 2 i=1 i 2 k E k+2 2 k E i i−2
or 0 for the others. Thus we see that the projection of the unfrozen root lattice is indeed
the coroot lattice Λh with generators
coroot
(cid:40)
2β β , i < k
β∨ = i = i (4.10)
i (β i ,β i ) 1 2 β k , i = k.
To obtain the weight and coweight lattice, we orthogonalize and project the unfrozen weight
lattice, respectively.
26

<!-- Page 28 -->

k > 0 even In this case Λg is generated by w and w (in Table 5) together with the
wt k+3 k+4
roots. Using (4.9), we have for both
(cid:32) (cid:33)
k−1
1 (cid:88) 1
w = α +2α + (j +2)β +(k +2)α + (α or α )
k+(3or4) 1 2 j k+2 k+3 k+4
2 2
j=1
(cid:32) (cid:33)
k−1
1 (cid:88) k +2 1
= −α + jβ −β + (β −α −α ) + (α or α ),
0 j k k k+3 k+4 k+3 k+4
2 2 2
j=1
(4.11)
which due to the α terms are not in the plane E. To orthogonalize, observe that
0
Λg ∋w +w −(k +1)α +α
wt k+3 k+4 k+2 0
k−1
(cid:88) 1
= jβ −β +α + (α +α )
j k k+2 k+3 k+4
2
(4.12)
j=1
k−1
(cid:88) 1
= jβ − β ∈ E.
j k
2
j=1
So we have
1
Λh := Λg ∩E = ⟨β ⟩ + β =: ⟨β ⟩ +w. (4.13)
w wt i Z 2 k i Z
From (4.11) the projections are:
(cid:32) (cid:33)
k−1 k−1
1 (cid:88) 1 (cid:88)
π (w ) = π (w ) = jβ −β ≡ jβ∨ mod ⟨β∨⟩ , (4.14)
E k+3 E k+4 2 j k 2 j i Z
j=1 j=1
(cid:124) (cid:123)(cid:122) (cid:125)
=:u
and we define Λh := π (Λg ) = ⟨β∨⟩ +u.
cw E wt i Z
It is easy to see that Λh/Λh = Λh /Λh = Z(Sp(k)) = Z . Moreover, it is straightw root cw coroot 2
forward to verify that
∀i = 1,...,k : (w,β∨) ∈ Z, (u,β ) ∈ Z. (4.15)
i i
This shows that we indeed have Λh = Λh and Λh = Λh .
w wt cw cowt
Notice that w +w ∈ Λg = H (X(cid:101) ,∂X(cid:101) ) is still a valid relative cycle wrapped by
k+3 k+4 wt 2 Γ Γ
M5 branes, which projects trivially onto Λh /Λh . Therefore these (unscreened) fourcowt coroot
dimensional defects are not charged under the magnetic center symmetry of the sp gauge
sector and also link trivially with M2 defects in Λh that survived the freezing, but neverwt
theless give rise to a Z (4)-symmetry independent of the center symmetries. Geometrically
2
27

<!-- Page 29 -->

this Z is the diagonal of Z ×Z = H (∂X(cid:101) ).

## 2 2 2 1 Γ

k odd In this case Λg is generated by
wt
(cid:32) (cid:33)
k−1
1 (cid:88) k k −2
w = −α + jβ −β +(k +2)α + α + α . (4.16)
k+3 0 j k k+2 k+3 k+4
2 4 4
j=1
To obtain a weight vector lying in E, we need
k
Λg ∋2w +α ≡ kα + (α +α ) mod ⟨β ⟩
wt k+3 0 k+2 2 k+3 k+4 i Z
k
= (2α +α +α ) mod ⟨β ⟩ (4.17)
k+2 k+3 k+4 i Z
2
1 1
= β mod ⟨β ⟩ ⇒ Λh = ⟨β ⟩ + β .
2 k i Z w i Z 2 k
On the other hand, the projection (using π (α ) = 1β ) becomes
E k+2 2 k
k−1 k−1
1 (cid:88) 1 k +2 1 (cid:88)
π (w ) = jβ − β + β = jβ∨+kβ∨
E k+3 2 j 2 k 2 k 2 j k
j=1 j=1 (4.18)
(cid:124) (cid:123)(cid:122) (cid:125)
=:u
⇒ Λh := π (Λg ) = ⟨β∨⟩ +u.
cw E cowt i Z
We again find Λh/Λh = Λh /Λh = Z(Sp(k)) = Z , as well as
w root cw coroot 2
∀i = 1,...,k : (w,β∨) ∈ Z, (u,β ) ∈ Z, (4.19)
i i
so Λh = Λh and Λh = Λh , as claimed.
w wt cw cowt
Notice again that we have unscreened M5 brane defects that are uncharged under the
Z(Sp(k))(4)-symmetry, comingfromM5braneswrapping2w whichprojectsontoacoroot.
k+3
Thus, they again link trivially with M2 brane defects, and are uncharged under the magnetic
center symmetry. They are charged under a Z 4-form symmetry, which is the Z ⊂ Z =
2 2 4
H (S3/Γ) subgroup.
1
k = 0 In this special case, the freezing leaves no wrapped M2 branes, so there is no 1-form
symmetry. On the other hand, there are no restrictions on the M5 branes, so we again expect
a Z ×Z = H (∂C2/Γ) 4-form symmetry without the presence of a gauge sector.
2 2 1
4.1.2
e(1/d)
6
d = 2 For T (M)[e(1/2)] the roots β of h = su(3) satisfy (β ,β ) = dCsu(3), where Csu(3) is
6 i i j ij
the standard su(3) Cartan matrix. The “good” roots of e , expressed in terms of the roots
6
28

<!-- Page 30 -->

of h = su(3) and the “bad” nodes α ∈ {α ,α ,α ,α } are
(cid:101) 0 1 3 5
1 1 1
α = (β −α −α ), α = (β −α −α ), α = − (α +α +β +β ). (4.20)
2 1 1 3 4 2 3 5 6 0 3 1 2
2 2 2
Thus we have
1
π (α ) = β = β∨, π (α ) = β∨, π (α ) = −β∨ −β∨, (4.21)
E 2 2 1 1 E 4 2 E 6 1 2
which indeed span Λh .
coroot
Proceeding with the weight lattice, we have
1 1 1
w = (α +2α +α +2α ) = (2β +β )+ (α −α )
1 1 2 4 5 1 2 5 3
3 6 2
(4.22)
1
⇒ 2w −(α −α ) = (2β +β ) =: w ∈ Λg ∩E = Λh ,
1 5 3 3 1 2 wt w
and verify that this is indeed the weight lattice Λh of h = su(3) using (w,β ) = δ ∈ Z and
wt i i,1
Λh/Λh = Z .
w root 3
The projection yields
1 1 1
π (w ) = β + β = (2β∨ +β∨) =: u Λh = ⟨β∨⟩ +u, (4.23)

### E 1 3 1 6 2 3 1 2 cw i Z

which is the su(3) coweight lattice Λh , by (u,β∨) = δ ) ∈ Z and Λh /Λh = Z .
cowt i i,1 cw coroot 3
Note that in this case, there are no (unscreened) M5 branes wrapping coweights of g = e
6
which project onto something that is uncharged under the center of h, so there is no left-over
4-form symmetry.
d = 3 In this case the freezing forbids M2 branes to wrap any 2-cycles, so there is no 1-
form symmetry charges. However, the M5 branes are still present, and form defects charged
under a Z(4) symmetry.
3
4.1.3
e(1/d)
7
d = 2 The frozen algebra in this case is h = so(7) with Z(Spin(7)) = Z = Λh /Λh =
2 wt root
Λh /Λh . The simple roots β satisfy (see Table 3)
cowt coroot i=1,2,3
 
4 −2 0
1 1
(β
i
,β
j
) = −2 4 −2 ⇒ β
1
∨ =
2
β
1
, β
2
∨ =
2
β
2
, β
3
∨ = β
3
. (4.24)
0 −2 2
29

<!-- Page 31 -->

Inparticular,thelongrootshavelength-squared2d. The“bad”g-rootsareα ∈ {α ,α ,α ,α },
(cid:101) 0 2 4 6
and the others can be expressed as
1 1
α = − (α +α +β +2β +2β ), α = (β −α −α ),
1 0 2 1 2 3 3 2 2 4
2 2
(4.25)
1
α = (β −α −α ), α = β .
5 1 4 6 7 3
2
From this we have the projections
1
π (α ) = β = β∨, π (α ) = β∨, π (α ) = β∨ +2β∨ +β∨
E 5 2 1 1 E 3 2 E 1 1 2 3 (4.26)
⇒ π (Λg ) = Λh .

### E root coroot

The e weight lattice is generated by the roots and w from Table 5. Rewritten in the
7 1
basis {β ,α }, we have
i (cid:101)j
1 1 1
w = (α +α +β ) = β −α + β
1 4 6 3 1 5 3
2 2 2
(4.27)
1
⇒ w := w +α = (β +β ) ∈ E ∩Λg .
1 5 2 1 3 wt
So 2w ∈ Λh , and we easily verify (w,β∨) = (1,−1,1) , so Λh +w = Λh . The projection
root j j root wt
produces
1 1
π (w ) = β = β∨ =: u, (4.28)

## E 1 3

2 2
which is indeed an so(7) coweight, since 2u ∈ Λh and (u,β ) = (0,−1,1) , so π (Λg ) =
coroot j j E wt
Λh .
cowt
Justasinthecaseofe(1/2), therearenounscreenedM5branedefectswhichareuncharged
6
under the magnetic center symmetry of h.
d = 3 The frozen algebra in this case is h = su(2) with Z(SU(2)) = Z = Λh /Λh =
2 wt root
Λh /Λh . Λh and Λh are generated by the simple (co-)roots (cf. Table 3)
cowt coroot root coroot
1
β = 2α +3α +2α +α +α with (β,β) = 6 = 2d ⇒ β∨ = β, (4.29)
3 4 5 6 7
3
which are orthogonal to the e roots α ∈ {α ,α ,α ,α ,α ,α }. We then have
7 (cid:101) 0 1 3 5 6 7
1 1
α = (α −2α −2α −α −β), α = (β −2α −2α −α −α ), (4.30)
2 0 1 3 7 4 3 5 6 7
3 3
30

<!-- Page 32 -->

which yields
1
π (α ) = −π (α ) = − β = −β∨ ⇒ π (Λg ) = Λh . (4.31)

### E 2 E 4 3 E root coroot

Proceeding with the weights, we have
1 1
w = β + (α +α −α −α )
1 6 7 3 5
6 3
(4.32)
1
⇒ w := w +α +α +α = β ∈ E ∩Λg ,
1 4 3 5 2 wt
which is indeed an h = su(2) weight, since (w,β∨) = 1, and 2w ∈ Λh . The projection is
root
1 1
π (w ) = β = β∨ =: u, (4.33)

## E 1

6 2
which is also an h = su(2) coweight since (u,β) = 1 and 2u ∈ Λh . All unscreened M5
coroot
brane defects are charged under the magnetic Z center symmetry of h.
2
d = 4 This is again a completely frozen setting, so the theory has no gauge symmetry and
consequently no 1-form symmetry charges from M2 branes on 2-cycles. On the other hand,
the unscreened M5 branes are charged under the Z = H (∂S3/Γ) 4-form symmetry.
2 1
4.1.4
e(1/d)
8
d = 2 Orthogonalizing the g = e root lattice with respect to the “bad” roots α ∈
8 (cid:101)
{α ,α ,α ,α } gives the root lattice of h = f with generators β given in Table 3,
0 2 4 8 4 i=1,...,4
satisfying
 
4 −2 0 0
−2 4 −2 0  1 1
(β ,β ) =   ⇒ β∨ = β , β∨ = β , β∨ = β , β∨ = β ,
i j  0 −2 2 −1 1 2 1 2 2 2 3 3 4 4
 
0 0 −1 2
(4.34)
with the long roots satisfying (β,β) = 2d. The “good” roots of g are
1 1
α = − (α +α +2β +3β +4β +2β ), α = (β −α −α ),
1 0 2 1 2 3 4 3 1 2 4
2 2
(4.35)
1
α = (β −α −α ), α = β , α = β .
5 2 4 8 6 3 7 4
2
31

<!-- Page 33 -->


### From this we immediately see that

π (α ) = β∨, π (α ) = β∨, π (α ) = β∨, π (α ) = β∨,

### E 3 1 E 5 2 E 6 3 E 7 4

π (α ) = −(2β∨ +3β∨ +2β∨ +β∨) (4.36)

## E 1 1 2 3 4

⇒ π (Λg ) = Λh .

### E root coroot

Now, since Λg = Λg for g = e , this means
wt root 8
Λh := Λg ∩E = Λg ∩E = Λh , Λh := π (Λg ) = π (Λg ) = Λh . (4.37)
w wt root root cw E wt E root coroot
This again agrees with the fact that h = f has trivial center, so (co-)roots and (co-)weights
4
are identical, i.e., Λh = Λh and Λh = Λh . So there are no unscreened defects charged
w wt cw cowt
under the 1- and 4-form symmetries at all, which is anyway the naive expectation for an f
4
gauge theory.
d = 3 In this case the “bad” roots are α = {α ,α ,α ,α ,α ,α }, leaving the roots β
(cid:101) 0 1 3 4 6 7 i=1,2
of h = g with
2
(cid:18) (cid:19)
6 −3 1
(β ,β ) = ⇒ β∨ = β , β∨ = β , (4.38)
i j −3 2 1 3 1 2 2
with long root having length-squared 6 = 2d. For the “good” g-roots we have α = β and
8 2
1 1
α = − (α +2α +2α +α +2β +3β ), α = (β −α −2α −2α −α )
2 0 1 3 4 1 2 5 1 3 4 6 7
3 3
⇒ π (α ) = β∨, π (α ) = β∨, π (α ) = −2β∨ −β∨.
E 8 2 E 5 1 E 2 1 2
(4.39)
So we have Λh = π (Λg ) = π (Λg ) = Λh and Λh = Λg ∩E = Λg ∩E = Λg ,
coroot E root E wt cowt wt wt root root
as expected for the centerless algebra h = g .
2
d = 4 Applying the freezing rule to g = e with flux r = 1/4 gives rise to some peculiarities
8
that we will now detail. In this case the “bad” roots are α ∈ {α ,α ,α ,α ,α ,α ,α }. If
(cid:101) 0 1 2 4 5 7 8
we seek for integer linear combinations of all g roots α such that they are orthogonal to α,
j (cid:101)
then we find that they are all integer multiples of the vector b = α +2α +2α +α +α .
4 5 6 7 8
However, it turns out that (b,b) = 2 ̸= 2d = 8.
In order to confirm with the instanton fractionalization, as discussed in Section 3, we
must therefore consider the lattice generated by β = 2b, as listed in Table 3, to be the frozen
root lattice Λh . Consequently, the coroot lattice is generated by β∨ = 1β. The “good” e
root 4 8
32

<!-- Page 34 -->

roots are
1 1
α = − (α +2α +3α +3α +2α +α +β), α = (β −2α −4α −2α −2α ),
3 0 1 2 4 5 8 6 4 5 7 8
4 4
(4.40)
which project to the coroot,
1
π (α ) = −π (α ) = − β = −β∨. (4.41)

## E 3 E 4

4
However, given that the weight lattice of g is the same as its root lattice, we cannot
obtain the naively expected (co-)weights which would be generated by w = 1β ∈ Λh and
2 wt
u = 1β∨ ∈ Λh . This means that this h = su(2) gauge theory does not have any unscreened
2 cowt
defectsfromM2orM5braneswrappingrelative2-cycleswhicharechargedundertheelectric
or magnetic center symmetries.
We will present a bottom-up explanation of this somewhat surprising result in Section

## For now, we would like to crosscheck this finding, as well as the “additional” 4-manifold

defects charged under the 4-form symmetry we encountered in the other cases above, from
a dual F-theory perspective.
4.2 Review of Duality to Twisted F-theory Compactifications
This subsection serves to briefly review the chain of dualities that relate M-theory frozen
singularities to twisted compactifications of F-theory. Readers familiar with [2] and [4] can
safely skip this subsection. For reviews on F-theory see [94,95].
Up until this point, we have implicitly considered the M-theory frozen singularity geometries to have a metric asymptotic to the conical metric
ds2 = dR2 +R2dΩ2 , (4.42)

## S3/Γ

where dΩ2 is the metric of S3/Γ inherited from an S3 metric of constant curvature. Such

## S3/Γ

hyper-Ka¨hler manifolds are known as asymptotically locally Euclidean (ALE). To perform
the aforementioned duality chain, we first need to embed the ALE frozen singularities into
a non-compact elliptic K3 manifold, with so-called Kodaira singularities. For each D- and
E-type ALE singularity there is essentially a unique way of doing this
D (cid:44)→ I∗, e (cid:44)→ IV∗, e (cid:44)→ III∗, e (cid:44)→ II∗, (4.43)
4+k k 6 7 8
where we have used the standard notation for Kodaira singularity types (for a review aimed
at physicists see for instance [94]).
Let X denote one of the Kodaira singularities appearing in (4.43) which is ellipticallyell.
fibered E → X → C . Our starting point is M-theory with (cid:82) C = n/d which we will
ell. w ∂X 3
ell.
33

<!-- Page 35 -->

write as
(cid:18) (cid:90) (cid:19)
n

## M X , C = . (4.44)

ell. 3
d

## ∂X

ell.
Here, the asymptotic boundary ∂X is the elliptic fibration over the bounding circle of C .
ell. w
If we compactify on an S1 transverse to X then we have IIA string theory on the same
ell.
background where now C is the RR monodromy:
3
(cid:18) (cid:90) (cid:19) (cid:18) (cid:90) (cid:19)
n S1 comp. n
M X , C = −−−−−→ IIA X , C = . (4.45)
ell. 3 ell. 3
d d

## ∂X ∂X

ell. ell.
Then we can perform two T-dualities, one for each of the circles of the elliptic fiber of X :
ell.
(cid:32) (cid:33)
(cid:18) (cid:90) (cid:19) (cid:90)
n n
doubleT-duality
IIA X , C = −−−−−−−−−→ IIA X(cid:98) , C = . (4.46)
ell. 3 ell. 1
d d

## ∂X S1

ell. φ
Here X(cid:98) , the mirror dual12 of X , is also elliptically-fibered over C whose asymptotic
ell. ell. w
boundary we denote by S1 = ∂C where φ := arg(w). We see that the background C has
φ w 3
turned into a C background and we can in fact lift the RHS of (4.46) to M-theory where
1
the C potential implies a non-trivial fibration of the IIA/M-theory circle. This lift takes
1
the form [2,4]
(cid:32) (cid:33)
(cid:90)
n
IIA X(cid:98) , C = − g −s→ − ∞ → M (cid:0) (Y ×S1)/Z (cid:1) , (4.47)
ell. 1 d ell. θ d

## S1

φ
where Y is a Kodaira singularity, i.e., a local K3, such that Y /Z = X(cid:98) and g is the
ell. ell. d ell. s
IIA string coupling. If we let C denote the base of Y , then the Z quotient is defined as
z ell. d
2π 2πn
θ ∼ θ+ , ϕ ∼ ϕ+ , E ∼ ρ(E ). (4.48)
z z
d d
where ϕ = arg(z), E is the elliptic fiber of Y at z, and ρ acts by the SL(2,Z) monodromy
z ell.
matrix of X(cid:98) . Finally, if we take a limit such that the volume of the generic elliptic fiber
ell.
of Y shrinks to zero, then we arrive at F-theory compactified on (Y ×S1)/Z :
ell. ell. θ d
M (cid:0) (Y ×S1)/Z (cid:1) − V − o − l( − E z− )→ −→ 0 F (cid:0) (Y ×S1)/Z (cid:1) . (4.49)
ell. θ d ell. θ d
In summary, we have the following duality
(cid:18) (cid:90) (cid:19)
n
M X, C = ⇔ F (cid:0) (Y ×S1)/Z (cid:1) (4.50)
3 d θ d

## ∂X

12From the CFT analysis of [96], one can conclude that the Kodaira singularities I∗, IV∗, III∗, II∗ are
0
mirror dual to birationally equivalent K3 manifolds with the same SL(2,Z) monodromy as before but with
a central fiber of the form T2/Z for k =2,3,4 and 6 respectively. Such results were conjectured in Section
k
4.6.1 of [2].
34

<!-- Page 36 -->

Frozen Singularity Y X Z ρ | Outer g h
d 1 ell. Y Γ,d
(cid:18) (cid:19)
−1 −k
D(1/2) I I∗ Z Z su(2k) sp(k)
4+k 2k k 2 0 −1 2
(cid:18) (cid:19)
−1 −1
e(1/2) IV IV∗ Z ∅ su(3) su(3)
6 2 1 0
(cid:18) (cid:19)
−1 −1
e(1/3) I IV∗ Z ∅ ∅ ∅
6 0 3 1 0
(cid:18) (cid:19)
0 −1
e(1/2) I∗ III∗ Z Z so(8) so(7)
7 0 2 1 0 2
(cid:18) (cid:19)
0 −1
e(1/3) III III∗ Z ∅ su(2) su(2)
7 3 1 0
(cid:18) (cid:19)
0 −1
e(1/4) I III∗ Z ∅ ∅ ∅
7 0 4 1 0
(cid:18) (cid:19)
0 −1
e(1/2) IV∗ II∗ Z Z e f
8 2 1 1 2 6 4
(cid:18) (cid:19)
0 −1
e(1/3) I∗ II∗ Z Z so(8) g
8 0 3 1 1 3 2
(cid:18) (cid:19)
0 −1
e(1/4) IV II∗ Z Z su(3) su(2)
8 4 1 1 2
(cid:18) (cid:19)
0 −1
e(1/5) II II∗ Z ∅ ∅ ∅
8 5 1 1
(cid:18) (cid:19)
0 −1
e1/6 I II∗ Z ∅ ∅ ∅
8 0 6 1 1
Table 7: M-theory frozen singularities X whose F-theory dual involves map ρ | which
1 ell.
non-trivially acts on the 1-cycles of the elliptic fiber. The column “Outer” denotes the group
action that it generates at the level of H (∂Y); it is the action on g whose quotient gives

## 1 Y

h .

### Γ,d

where we have dropped the (ell.) subscript to not overload the notation. In Table 7, we list
examples of Kodaira singularities Y and their corresponding M-theory frozen singularity (for
a full list see Table 3 of [4]).
4.3 Calculation of Defect Groups in Twisted F-theory Frame
Our goal in this section is to compute the defect groups of the M-theory frozen singularities
on the LHS of the F-/M-theory duality (4.50) by appealing to the relation to twisted F-
theory compactifications on the RHS of (4.50). See Table 7 for the details on the F-theory
geometry for each frozen singularity.
To understand how to calculate the defect groups of F-theory on Z = (Y ×S1)/Z , first
d
we recall how one may calculate the defect group for F-theory on some Kodaira singularity
Y. This engineers an 8D SYM with some gauge algebra g and has a defect group made up

## Y

35

<!-- Page 37 -->

Figure 5: On the left, we illustrate a (p,q)-string (black arrow) ending on a 7-brane (red
dot) that generates monodromy ρ (we signify a cut crossing which produces this monodromy
action by the dotted red line). For certain (p,q) charges, we can dynamically resolve this
configuration to the right figure where p′,q′ ∈ Z. Such (p,q)-strings are trivial in the defect
group because this process implies that the line operators they generate in the 8D gauge
theory can terminate in the 8D 7-brane worldvolume. Similar remarks apply for (p,q)-5-
branes.
of the electric 1-form symmetry and the magnetic 5-form symmetry D = D(1)⊕D(5). While

## 8D

it turns out that simply D = (Z(G ))(1) ⊕ (Z(G ))(5), the string theoretic approach to

## 8D Y Y

derivingthiswassystematizedin[31]wherebythedefectgroupsofthe7-branespecifiedbyY
are related to the charged of string and 5-brane states that can end on the 7-brane localized
at the fiber singularity. These string/5-brane charges are valued in a freely generated lattice,
and the defect group is equivalent to this lattice modulo string/5-brane states ending on
the 7-branes that can be resolved into so-called integer null junctions13, see Figure 5. The
reason for this is that such states can be dynamically radiated away from the 7-brane, and
thus do not realize a defect in the 8D gauge theory charged under a global symmetry.
For the case of F-theory on Z = (Y ×S1)/Z , states charged under the 1-form symmetry
θ d
of the 7D KK theory are strings ending on the 7-brane which are localized at a specific value
of θ ∈ S1. For a given (p,q)-string which is able to end on the 7-brane, we have a charge
0
vector14 [p,−q]T and the monodromy around S1/Z identifies
θ d
(cid:20) (cid:21) (cid:20) (cid:21)
p p
ρ ∼ . (4.51)
−q −q
This means that the 1-form piece of the defect group is given by

### D(1) = coker(ρ−1). (4.52)

13Inpreciseterms,a(p,q)-string/5-braneadmitsanintegernulljunctionifthereexistssolutionstoρ p′+
11
ρ q′+p=p′ and ρ p′+ρ q′+q =q′ such that p′,q′ ∈Z.
12 21 22
14Using the conventions of [94] where the minus sign is due to the SL(2,Z)-invariant epsilon tensor.
36

<!-- Page 38 -->

Figure 6: F-theory compactified on Z = (Y × S1)/Z which is dual to M-theory on an
(cid:82) I 0 ∗ θ 2
III∗ singularity with C =1/2 frozen flux. The gray planes are the bases of Y with the

## ∂X 3 I 0 ∗

I∗ 7-brane located at the origin. The green line indicates a ρ monodromy action cut and
0
acts on long string junctions as shown. Note that the (p,q) long strings have a defect group
charge (p mod 2,q mod 2) which is well-defined up to screening of dynamical states on the
7-brane. The monodromy action ρ then enforces that (1,0) and (0,1) strings are in the same
equivalence class of the defect group (i.e. they have indistinguishable charges at the level of
the 7D KK theory). This reduces the defect group from Z ×Z to Z with the generator
2 2 2
(1,1) = (1,0)+(0,1) being equivalent to (0,0).
See Figure 6 for an illustration/explanation in the case of the twisted compactification Z =
(Y × S1)/Z . As for 5-branes, these give rise to the 4-form part of the defect group by

### I 0 ∗ θ 2

wrapping15 S1/Z . Such 5-branes must be invariant under the monodromy (which now acts
θ d
as an automorphism on (Z(G ))(5)) to consistently wrap S1/Z so therefore we have that

### Y θ d


### D(4) = ker(ρ−1). (4.53)

Similar to (4.52), the (ρ−1) operator is understood to act on (p,q) charges of 5-branes which
are able to end on the 7-brane. Notice also that we can consider the consistent charges of
strings wrapped on S1/Z to generate 0-dimensional defects in a 0-form defect group, D(0)
θ d
or similarly 5-branes not wrapped on the circle to generate 5-manifold defect operators in
D(5) for the 7D theory. Since these operators do not play a role in the global structure of
the 7D gauge group, we will not consider them further in this work but their presence may
be interesting to study in future work.
15Thisisduetothefamiliarfactthatthe’tHooftoperatorsofa(D+1)-dimensionalgaugetheoryreduceto
’tHooftoperatorsinaD-dimensionalgaugetheoryuponcirclereductionbywrappingthecircle. Meanwhile
Wilson operators do not wrap the circle.
37

<!-- Page 39 -->

A convenient way to compute the defect group D = D(1)⊕D(4) is done by compactifying
the twisted F-theory compactifcation on a further S1 to arrive at M-theory compactified
extra
on Z = (Y ×S1)/Z :
θ d
F (cid:0) (Y ×S1)/Z ×S1 (cid:1) ⇔ M (cid:0) (Y ×S1)/Z (cid:1) . (4.54)
θ d extra θ d
This allows us to easily package (4.52) and (4.53) in terms of homology groups of Z relative
to its asymptotic boundary ∂Z as
(cid:18) (cid:19)

## H (Z,∂Z)

D(1) = D(1) = Tor 2 , (4.55)

## 7D 6D H (Z)


## 2 M2

(cid:18) (cid:19)

## H (Z,∂Z)

D(4) = D(3) = Tor 3 , (4.56)

## 7D 6D H (Z)


## 3 M5

wherethe6Dsubscriptreferstothe6Dsystemin(4.54)andtheMpsubscriptsindicatewhich
M-theory brane we are wrapping on these relative cycles. We restrict to torsion in order to
isolate the charges that can arise from strings/5-branes. From the long exact sequence which
defines relative homology, we arrive at another presentation of these groups
(cid:18) (cid:19)

## H (Z,∂Z)

i (cid:0) (cid:1) (cid:0) (cid:1)
Tor ≃ Tor Ker(H (∂Z) → H (Z)) =: Tor H (∂Z) | (4.57)
i−1 i−1 i−1 triv.

## H (Z)

i
(cid:0) (cid:1) (cid:0) (cid:1)
wherethesubscript‘ ’indicatesthatTor H (∂Z) | isthesubgroupofTor H (∂Z)
triv. i−1 triv. i−1
that trivializes when embedded as (i − 1)-cycles into the bulk Z. Intuitively, the groups
H (∂Z) (of appropriate degree) encode the possible string/5-brane charges that may coni
sistently be measured at spatial infinity while the restriction | identifies those charges
triv.
that may actually end on the 7-brane. Such a restriction is non-trivial when Y is a type I

## N

7-brane because H (Y) ̸= 0 in this case which physically can be understood as the inability
1
for D1 strings to end on D7 branes, see Figure 7 for a illustration of the F-theory geometry.
In Section 5, we will see that in cases where this restriction is non-trivial and give a SymTFT
picture of what is going on.
Calculating the groups in (4.56) is a fairly straightforward task as Z and ∂Z have the
structure of a fibration over a circle and the action of Z on the cycles of H (Z) and H (∂Z)
d ∗ ∗
can be derived as follows. From (4.48) we have a fibration structure of Z and ∂Z over a
circle:
Y (cid:44)→ Z →− π S1/Z (4.58)
d
∂Y (cid:44)→ ∂Z →− π S1/Z . (4.59)
d
See Figure 8 for an illustration of this fibration structure for ∂Z. We immediately see that
the 1-cycle associated to the ϕ direction in ∂Y is not acted upon when encircling the base of
(4.59) since the quotient (4.48) simply acts by a rotation. However, cycles in Y and ∂Y will
38

<!-- Page 40 -->

Figure 7: Illustration of a I Kodaira surface. The singular, central fiber is depicted on

## N

the left while the generic smooth fiber is shown on the right. At the central fiber the acycle, γ , of the elliptic fiber degenerates while γ does not. This mean that the γ cycle on
a b b
the asymptotic boundary ∂Y does not trivialize. This means that D1/D5 branes dual to

## In

M2/M5 branes wrapping γ cannot end on a stack of N D7s.
b
Figure 8: Illustration of ∂Z regarded a fibration of ∂Y over S1/Z . We also show the
θ d
fibration structure of ∂Y itself over a circle S1 with elliptic fiber E . The green dotted line
ϕ ϕ
denotes a cut for the monodromy action ρ.
generically transform due to the action of ρ in (4.48) which we will detail in the examples
below. Notice from Table 7 that the action of ρ on H (Y) and H (Y) is trivial for the e(1/2)
1 2 6
and e(1/3) cases so their defect groups will be identical to that of Y, so we omit these trivial
7
cases from our calculations.
Another geometric detail that will be useful in what follows are the homology groups for
Y and ∂Y. The former homology groups are given as follows (∗ = 0,...,4)

## H (Y) = {Z,H (Y),Z,0,0}, (4.60)

∗ 1
39

<!-- Page 41 -->


##  Z2 Y = I 

 0 

## H (Y) = Z Y = I . (4.61)


## 1 N>0

 
0 Otherwise
which can be derived from deformation retracting Y to the central fiber E whose topology
0
followsfromtheKodairatypeofY. Meanwhile,thehomologygroupsfor∂Y dependcrucially
on the ADE-type of the singularity located in the central fiber E . A local patch of the ADE
0
is diffeomorphic to C2/Γ for a finite subgroup Γ ⊂ SU(2). H (∂Y) is then given as follows
∗
(see [31] for more details)

## H (∂Y) = {Z,H (∂Y),H (∂Y),Z}, (4.62)

∗ 1 2

##  Z⊕Z2 Y = I 

 0 

## H (∂Y) = Z⊕Z⊕Z Y = I , (4.63)


## 1 N N>0

 Z⊕Ab(Γ ) Otherwise 

## Y


##  Z⊕Z2 Y = I 

 0 

## H (∂Y) = Z⊕Z Y = I , (4.64)


## 2 N>0

 Z Otherwise 
whereΓ denotestheADE subgroupofSU(2)forwhichC2/Γ isthelocalADE singularity

## Y Y

of Y. The first Z summand for H (∂Y) and H (∂Y) are, respectively, the asymptotic circle
1 2
S1 ≡ ∂C and the generic E ≃ T2 fiber of Y along S1, which exist for all geometries.
ϕ z z ϕ
For readers that wish to skip the details of the geometric computations, we list in Table 6
our results for the defect groups. These follow from the homologies for Z and ∂Z whose
results we state below:

## H (Z) = {Z,H (Z),Z,Z,0,0}, (4.65)

∗ 1
(cid:26) Z⊕Z Z = (I ×S1)/Z (cid:27)

## H (Z) = 2 N>0 2 , (4.66)

1 Z⊕Ab(Γ ) Otherwise

## X


## H (∂Z) = {Z,H (∂Z),H (∂Z),Z2,Z}, (4.67)

∗ 1 2
 Z2 ⊕Z2 Z = (I ×S1)/Z (k even) 
  2 2k 2  
  Z2 ⊕Z Z = (I ×S1)/Z (k odd)  
  4 2k 2  
  Z2 ⊕Z Z = (I ×S1)/Z  
H (∂Z) = H (∂Z) = 3 0 3 . (4.68)

## 1 2 Z2 ⊕Z Z = (I∗ ×S1)/Z

  2 0 2  
    Z2 ⊕Z 2 Z = (I 0 ×S1)/Z 4    
 
 Z2 Otherwise 
Here Γ denotes the ADE subgroup of SU(2) for which C2/Γ is the local ADE singularity

## X X

of X, see Table 7.
40

<!-- Page 42 -->

D-Type Frozen Singularities We now study the topology of Z and ∂Z relevant to the
(cid:82)
D-type singularities with C = 1/2. We find it best to separate the cases D and D .
∂X 3 4 4+k≥5
Starting with D , then Y is has an I Kodaira fiber, i.e. is topologically C × T2, and
4 0
∂Y ≃ T3. We have a fibration
∂Y (cid:44)→ ∂Z →− π S1/Z , (4.69)
2
so the first and second homologies can be calculated from the short exact sequences
0 → coker(ρ −1) → H (∂Z) → ker(ρ −1) → 0, (4.70)
1 1 0
0 → coker(ρ −1) → H (∂Z) → ker(ρ −1) → 0, (4.71)
2 2 1
where ρ : H (∂Y) → H (∂Y) is the action of the monodromy on H (∂Y) which is induced
k k k k
from the action ρ appearing in (4.48). From Table 7, we see that the action ρ on H (∂Y) =
1 1

### Z⊕Z2 is given as

(cid:18) (cid:19)
−1 0
ρ = 1⊕ . (4.72)
1
0 −1
Additionally, the action of ρ on H (∂Y) = Z⊕Z2 is exactly the same as in (4.72) since the
2 2
action of ρ preserves the 2-cycle of the generic fiber16 [E ], while the Z2 factor in H (∂Y)
z 2
are generated by [(A cycle of E )×S1] and [(B cycle of E )×S1]. We see then that
z ϕ z ϕ

## H (∂Z) = Z⊕Z ⊕Z ⊕Z, (4.73)

1 2 2

## H (∂Z) = Z⊕Z ⊕Z ⊕Z, (4.74)

2 2 2
where now the last Z factor for H is generated by the base circle of the fibration (4.69), and
1
the last Z factor for H is generated by the product of this circle with S1. Similarly, we can
2 ϕ
use the following short exact sequences to solve for H (Z) and H (Z):
1 2
0 → coker(ρ −1) → H (Z) → ker(ρ −1) → 0, (4.75)
1 1 0
0 → coker(ρ −1) → H (Z) → ker(ρ −1) → 0. (4.76)
2 2 1
Now ρ is acts as the (2 × 2) matrix appearing in (4.72) on H (Y) = Z2 while ρ acts on
1 1 2
H (Y) = Z by the identity. This implies that
2
H (Z) = Z ⊕Z ⊕Z, H (Z) = Z. (4.77)
1 2 2 2
To finally compute the 1-form symmetry piece of the defect group, D(1), we just need to

## 7D

understand the kernel of the inclusion map H (∂Z) → H (Z) which is an isomorphism on
1 1
16This amounts to the statement that an SL(2,Z) matrix is determinant 1 so preserves the volume form
of the elliptic fiber.
41

<!-- Page 43 -->

the Z2 factor as well as the Z factor generated by [S1/Z ]. Therefore
2 2
D(1/2) : H (∂Z)| = Z =⇒ D(1) = 0, (4.78)
4 1 triv. 7D
after taking the torsion part. Additionally, we see that the kernel of H (∂Z) → H (Z) must
2 2
be Z⊕Z2 which means that
2

## D(1/2) : D(4) = Z2. (4.79)


## 4 7D 2

The fact that this group is non-trivial will have impications for our application to O7+ planes
in Section 6.1.
Moving on to D with k ≥ 1, we again first solve for H (∂Z) and H (∂Z). Recall that
4+k 1 2
for an I singularity we have H (∂Y) = Z ⊕ Z ⊕ Z where the second two factors follow
2k 1 2k
from the fact that
(cid:18) (cid:19)
0 2k
coker ≃ Z ⊕Z, (4.80)
2k
0 0
since the above matrix is the monodromy matrix for the I singularity minus the identity.
2k
This motivates explicitly presenting the elements of Z ⊕Z as
2k
(cid:18) (cid:19)
x mod 2k
, x, y ∈ Z. (4.81)
y
From Table 7, the action of ρ on H (∂Y) = Z⊕Z is then given as multiplication by
1 1 2k
(cid:18) (cid:19)
−1 −k
ρ = 1⊕ . (4.82)
1
0 −1
If k is even, then we can perform a coordinate change x′ mod 2k = (x−ky) mod 2k, y′ = −y
2
after which
(cid:18) (cid:19)
2 0
ρ −1 = 0⊕ . (4.83)
1
0 2
Then it is straightforward to see that
(k even): H (∂Z) = Z⊕Z2 ⊕Z. (4.84)
1 2
Similarly, if k is odd then we can perform coordinate changes17 in both the domain and
codomain of (ρ −1) to arrive at
1
(cid:18) (cid:19)
1 0
ρ −1 = 0⊕ , (4.85)
1
0 4
(cid:18) (cid:19) (cid:18) (cid:19)(cid:18) (cid:19)(cid:18) (cid:19)
1 0 −1 (k−1)/2 −2 −k 0 −1
17These follow from the Smith normal decomposition =
0 4 2 −k 0 −2 1 2
when k is odd.
42

<!-- Page 44 -->

which implies that
(k odd): H (∂Z) = Z⊕Z ⊕Z. (4.86)
1 4
Now solving for H (∂Z), we see first that ker(ρ −1) = Z⊕Z . The Z factor is generated
2 1 2
by [S1 × S1/Z ] while the torsion factor is generated by k times the generator of Z ⊂
ϕ θ 2 2k
H (∂Y) fibered over S1. Meanwhile, we have that the action of ρ on H (∂Y) = Z⊕Z =
1 θ 2 2
⟨[E ],[(B-cycle of E )×S1]⟩ is given by
z z ϕ
(cid:18) (cid:19)
1 0
, (4.87)
0 −1
where we recall from (4.81) that the B-cycle of E has coordinate y so the minus sign in
z
(4.87) follows from the bottom-right entry of the I∗ monodromy matrix (4.82). We then
k
have that coker(ρ −1) = Z⊕Z leading to
2 2
H (∂Z) = Z⊕Ext(Z ,Z )⊕Z, (4.88)
2 2 2
where Ext(Z ,Z ) is an extension of Z by Z that we a a priori do not know from the
2 2 2 2
short exact sequence alone. We can fix this extension using Poincar´e duality because
(cid:0) (cid:1) (cid:0) (cid:1)
∂Z is smooth. This implies Tor H (∂Z) = Tor H (∂Z) which means that
i dim(∂X)−i−1
(cid:0) (cid:1) (cid:0) (cid:1)
Tor H (∂Z) = Tor H (∂Z) . Therefore, the extension is trivial for k even and non-trivial
1 2
for k odd. Since the integer factors also match we have that H (∂Z) = H (∂Z).
2 1

### We now show that

H (Z) = Z ⊕Z, H (Z) = Z, (4.89)
1 2 2
wheretheZ factorfollowsfromthepreviouslymentionedeffectoftheI∗ monodromymatrix
2 k
flipping the B-cycle, and we have that Z in H (Z) is generated by [S1/Z ] while the Z in
1 θ 2
H (Z) is generated by [E ].
2 z
We are finally in a position to derive H (∂Z)| and H (∂Z)| . We show the former
1 triv. 2 triv.
is
H (∂Z)| = ker(H (∂Z) → H (Z)) = Z⊕Z . (4.90)
1 triv. 1 1 2
The Z is simply the extra factor of Z that H (∂Z) has compared to H (Z) which is generated
1 1
by [S1]. As for the torsion factors, we more interestingly have that
ϕ
(cid:26) ker(Z2 → Z ) k even (cid:27)

## Z = 2 2 , (4.91)

2 ker(Z → Z ) k odd
4 2
where the map in the top line is simply
(cid:18) (cid:19)
x mod 2
(cid:55)→ y mod 2, (4.92)
y mod 2
43

<!-- Page 45 -->

while the map in the bottom line is
(cid:18) (cid:19)
0
(cid:55)→ y mod 2, (4.93)
y mod 4
which clearly satisfy the claimed (4.91). In summary then, the 1-form part of the defect
group for the D(1/2) frozen singularity for any k is
4+k
(cid:26) (cid:27)
D(1)(cid:0) D(1/2)(cid:1)
=
0, k = 0
. (4.94)
7D 4+k Z , k ≥ 1
2

### We additionally have that

(cid:26) Z⊕Z2, k even (cid:27)
H (∂Z)| = ker(H (∂Z) → H (Z)) = 2 , (4.95)
2 triv. 2 2 Z⊕Z , k odd
4
(cid:0) (cid:1)
which is immediately clear given that Tor H (Z) = 0. We then conclude that
2
D(4)(cid:0) D(1/2)(cid:1)
=
(cid:26) Z2
2
, k even (cid:27)
. (4.96)
7D 4+k Z , k odd
4
Notice that we see that the 4-manifold defect charges, arising from M5 branes wrapped on
relative 2-cycles, are indeed more numerous in than the line defect charges as we found in
Section 4.1. Confirmation of this feature will persist for the fully frozen examples below.
e(1/3) Frozen Singularity In this case Y is a type I surface, so H (∂Y) = Z ⊕ Z2 and
6 0 1
the monodromy action around S1/Z is
θ 3
(cid:18) (cid:19)
−1 −1
ρ = 1⊕ . (4.97)
1
1 0
We can calculate the kernel and cokernel of (ρ −1) from its Smith normal form
1
(cid:18) (cid:19)
1 0
SNF(ρ −1) = 0⊕ , (4.98)
1
0 3
which makes it clear that ker(ρ −1) = Z and coker(ρ −1) = Z . From this we have that
1 1 3
H (∂Z) = H (∂Z) = Z⊕Z . This is not quite the defect group because H (Z) is non-trivial.
1 2 3 1
This follows from the fact that the action of ρ on H (Y) = Z2 has the same Smith normal
1 1
form as the (2 × 2) matrix in (4.98) which means that H (Z) = Z . This means that the
1 3
1-form piece of the defect group is
D(1)(e(1/3)) = H (Z,∂Z)/H (Z) = (Z⊕Z )/(Z⊕Z ) = 0, (4.99)

## 7D 6 2 2 3 3

44

<!-- Page 46 -->

while the 4-form piece is
D(4)(e(1/3)) = H (Z,∂Z)/H (Z) = (Z⊕Z )/Z = Z . (4.100)

## 7D 6 3 3 3 3

e(1/2) Frozen Singularity In this case, Y is an I∗ surface so we have H (∂Y) = Z⊕Z2,
7 0 1 2
with the monodromy action around S1/Z being given by
θ 2
(cid:18) (cid:19)
0 1
ρ = 1⊕ , (4.101)
1
1 0
with the (2×2) matrix being the modulo-2 reduction of the monodromy matrix of an III∗
singularity, see Table 7. It is straightforward to calculate18 that coker(ρ −1) = Z⊕Z which
1 2
gives

## H (∂Z) = Z⊕Z ⊕Z, (4.102)

1 2
after combining with ker(ρ −1) = Z whose generator is given by [S1/Z ]. Similar consider-
0 θ 2
ations yield H (∂Z) = H (∂Z). Meanwhile from (4.61) we see that since H (Y) = 0, (4.75)
2 1 1
implies that H (Z) = ker(ρ −1) = Z and (4.76) implies that H (Z) = coker(ρ −1) = Z.
1 0 2 2

### We therefore have that


## H (∂Z)| = Z⊕Z . (4.103)

1 triv. 2
which after taking the torsion part gives the 1-form part of the defect group
D(1)(e(1/2)) = Z . (4.104)

## 7D 7 2

As for the 4-form part, this follows from homology groups quoted above to simply be
D(4)(e(1/2)) = Z . (4.105)

## 7D 7 2

e(1/4) Frozen Singularity This case is similar to the e(1/3) above, where again H (∂Y) =
7 6 1
Z⊕Z2. The monodromy action on H (Y) around S1/Z is
1 θ 4
(cid:18) (cid:19)
0 −1
ρ = 1⊕ , (4.106)
1
1 0
and (ρ −1) has a Smith normal form
1
(cid:18) (cid:19)
1 0
SNF(ρ −1) = 0⊕ . (4.107)
1
0 2
(cid:18) (cid:19)
xmod2
18Explicitly deriving the Z part of the cokernel, we indeed find that the Z2 vector is now
2 2 y mod2
(cid:18) (cid:19)
1
considered modulo which means we are left with the quotient Z2/Z =Z generated by (x+y)mod2.
1 2 2 2
These considerations also make it clear that ker(ρ −1)=Z⊕Z .
1 2
45

<!-- Page 47 -->

It follows thatker(ρ −1) = Zand coker(ρ −1) = Z which meansthat H (∂Z) = H (∂Z) =
1 1 2 1 2
Z ⊕ Z . Once more, this is not quite the defect group because H (Z) is non-trivial since
2 1
the action of ρ on H (Y) = Z2 has the same Smith normal form as the (2×2) matrix in
1 1
(4.107). We see then that H (Z) = Z which makes 1-form piece of the defect group
1 2
D(1)(cid:0) e(1/4)(cid:1) = H (Z,∂Z)/H (Z) = (Z⊕Z )/(Z⊕Z ) = 0, (4.108)

## 7D 7 2 2 2 2

while the 4-form piece is
D(4)(cid:0) e(1/4)(cid:1) = H (Z,∂Z)/H (Z) = (Z⊕Z )/Z = Z . (4.109)

## 7D 7 3 3 2 2

e(r)
Frozen Singularities with r = 1/2,1/3 and 1/4 Following similar remarks from
8
the previous paragraph, H (Z) = H (Z) = Z for all of the e(r) cases as well which, as for the
1 2 8
e(1/2), gives the relations
7
D(1) = Tor (cid:0) H (∂Z) (cid:1) | = Tor (cid:0) H (∂Z) (cid:1) , (4.110)
7D 1 triv. 1
D(4) = Tor (cid:0) H (∂Z) (cid:1) | = Tor (cid:0) H (∂Z) (cid:1) , (4.111)
7D 2 triv. 2

## =⇒ D(1) = D(4), (4.112)


## 7D 7D

where the last line follows from Poincar´e duality of ∂Z. This means that we are left with
(cid:0) (cid:1)
the simpler task of just calculating Tor H (Z) to derive the higher-form symmetries. Note
1
that in all of these examples, we will have H (Z) = Z = ⟨[E ]⟩ since H (Y) is trivial and the
2 z 1
monodromy action ρ on H (Y) is the identity.
2 2
For r = 1/2, Y is a IV∗ surface which satisfies Tor (cid:0) H (∂Y) (cid:1) = Z . Ones sees this from
1 3
(cid:18) (cid:19)
−2 −1
coker(ρ −1) = coker = Z , (4.113)
1 3
1 −1
whereby we can choose to represent the generator of the Z in any of the following ways:
3
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)

## 1 0 −1 1+3M

∼ ∼ ∼ ≡ 1 mod 3 ∈ Z . (4.114)
3
0 −1 1 0
The action of ρ is then
1
(cid:18) (cid:19)(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
0 −1 1 0 2
= ∼ ≡ 2 mod 3, (4.115)
1 1 0 1 0
which means that the Z in the quotient Z = (Y ×S1)/Z acts by an automorphism on Z .
2 θ 2 3
This means that (ρ −1) is the identity map which has trivial cokernel therefore
1
D(1)(cid:0) e(1/2)(cid:1)
=
D(4)(cid:0) e(1/2)(cid:1)
= 0. (4.116)

## 7D 8 7D 8

46

<!-- Page 48 -->

When r = 1/3, Y is an I∗ and Tor (cid:0) H (Y) (cid:1) = Z2. The Z action of ρ is given by
0 1 2 3 1
(cid:18) (cid:19)(cid:18) (cid:19) (cid:18) (cid:19)
0 −1 x mod 2 −y mod 2
= , (4.117)
1 1 y mod 2 x+y mod 2
which is none other than the well-known triality automorphism on the Kleinian group. One
can easily see that im(ρ −1) = Z2 so coker(ρ −1) = 0 and thus
1 2 1
D(1)(cid:0) e(1/3)(cid:1)
=
D(4)(cid:0) e(1/3)(cid:1)
= 0. (4.118)

## 7D 8 7D 8

When r = 1/4, Y is a IV surface which means that Tor (cid:0) H (∂Y) (cid:1) = Z . The discussion
1 3
is identical with that of the r = 1/2 case since the monodromy matrices satisfy ρ ρ = 1

## Iv Iv∗

which in particular implies that ρ and ρ are related by similarity transformations so all

## Iv Iv∗

of the linear algebra analysis in the r = 1/2 case carries over. Therefore we have that
D(1)(cid:0) e(1/4)(cid:1)
=
D(4)(cid:0) e(1/4)(cid:1)
= 0. (4.119)

## 7D 8 7D 8

The only geometric caveat is that Z ≃ Z /Z of the Z quotient in Z = (Y ×S1)/Z acts
2 4 2 4 θ 4
effectively on Tor (cid:0) H (∂Y) = Z (cid:1) but this does not affect the topology at all19.
1 3
Finally, when r = 1/6, Y is a type I surface and our defect group calculation is similar
0
to the e(1/3) and e(1/4) cases above. The monodromy action on H (Y) around S1/Z is
6 7 1 θ 6
(cid:18) (cid:19)
0 −1
ρ = 1⊕ , (4.120)
1
1 1
and (ρ −1) has a Smith normal form
1
(cid:18) (cid:19)
1 0
SNF(ρ −1) = 0⊕ . (4.121)
1
0 1
It follows that ker(ρ −1) = Z and coker(ρ −1) = 0 which means that H (∂Z) = H (∂Z) =
1 1 1 2
Z. The defect group is thus trivial in this case:
D(1)(cid:0) e(1/6)(cid:1)
=
D(4)(cid:0) e(1/6)(cid:1)
= 0. (4.122)

## 7D 8 7D 8

We see that the geometrical calculation in the dual F-theory frame perfectly reproduces
the 1- and 4-form symmetries predicted by an application of the local freezing map in Section
4.1.
19I.e. wecangetanidenticaltopologicalspacebyinsteadquotientingtheIV singularityY bytherelations
θ ∼θ+ 2π, ϕ∼ϕ+ 2π, E ∼ρ(E )
2 2 z z
47

<!-- Page 49 -->

5 SymTFTs of Frozen Singularities
Having given a detailed analysis of defects charged under 1-form and 4-form symmetries of
7D theories on frozen singularities, T (M)[g(n/d)], we now turn to the more refined information
present in their 8D SymTFTs. Such a topological theory of one higher dimension, whereby
T (M)[g(n/d)] lives on a boundary, captures the ’t Hooft anomalies of the higher-form symmetries. Indeed, such a SymTFT analysis for M-theory on unfrozen ADE singularities was
carried out in [52] and leads to the usual mixed electric 1-form/magnetic 4-form anomaly
(or, mutual non-locality of Wilson and ’t Hooft operators) expected of 7D gauge theories
(coupled to adjoint gauginos), whose results we will review below.
When applied to frozen singularities, the discrepancy between the topological defects
present in the SymTFT and the charged defects we have computed above signals that the
boundary degrees of freedom T (M)[g(n/d)] comprises more than just a simple SYM sector.

### The novelties we will see come in two flavors:


## Amodificationintheusual8DSymTFTboundaryconditionsalongthe7DT (M)[g(n/d)]

boundary.

## Additional 7D counterterms20 localized on the T (M)[g(n/d)] boundary required for consistency with ’t Hooft anomalies.

The first type of modification can be derived explicitly in the twisted F-theory frame, using
the geometric description on Z. There, the mismatch between H (∂Z)| and H (∂Z) re-
∗ triv. ∗
(cid:0) (cid:1)
sulting from a non-trivial Tor H (Z) can be translated into a topological term on the physi-
∗
cal boundary which imposes Neumann boundary conditions for some or all of the SymTFT’s
1-formsymmetryoperators. Wewillfindthatthesecasesofthefirsttypealsohaveadditional
counterterms which is explained in Appendix B.
We propose topological modifications of the second type for the e(1/2) and e(1/4) singular-
6 8
ities. The former is due to the fact that the term in the SymTFT action which characterizes
the mixed 1-/4-form ’t Hooft anomaly has the opposite sign from what would naively be
expectedfromthe7Dgaugetheory. Asforthelattercase, suchatopologicalmodificationfor
the 7D theory T (M)[e(1/4)] appears to have a trivial 1-form/4-form ’t Hooft anomaly, and in
8
fact no notion of global structure for its gauge group despite hosting a su(2) gauge multiplet.
Such a gauge theory with no notion of global structure is a new field theory phenomenon as
far as we are aware.
The SymTFTs considered here are topological theories in 8D with one boundary hosting
the 7D theory T (M)[g(n/d)], and a gapped topological boundary which we call B . The
top
T (M)[g(n/d)] boundary is of course gapless when g(n/d) is a partially frozen singularity and is
20A perhaps modern way of phrasing the procedure of adding topological counterterms is tensoring the
7D theory by a symmetry protected topological (SPT) phase.
48

<!-- Page 50 -->

Figure 9: 8D SymTFT sandwich construction for the 7D theories localized on the g(n/d)
frozen singularity.
gapped when it is fully frozen. The worldvolume of this 8D theory is X ×[0,1] where we
7
take21 the interval direction to be related to the physical radial direction by
πT = 2arctan(R), (5.1)
see Figure 9 for an illustration. One obtains an absolute 7D theory by compactifying the
SymTFT on the interval direction, whose partition function is given schematically as
Z (Btop) (X ) = ⟨T (M)[g(n/d)]|B ⟩ . (5.2)
7D 7 top
Roughly speaking, the data of B determines the global structure of the 7D gauge group
top
which, as we will review shortly, is precisely true for unfrozen singularities.
The 8D bulk topological theory is in principle derived by compactifying M-theory on
∂X and truncating to the topological terms which are the leading contributions in the large

## Γ

volume limit22 of ∂X . When X is elliptically-fibered over C, one can identify the radial

## Γ Γ

direction with the radial direction of the base but this will not matter for our purposes
because in cases where we need to appeal to the twisted F-theory dual, the volume of the
generic fiber of X is taken to infinity so it is essentially an ADE singularity.

## Γ

21The precise relation is immaterial since the 8D SymTFT is topological.
22There is a small neighborhood of the singularity where this large volume limit of ∂X breaks down, but

## Γ

these corrections, which include for instance 11D graviton scattering with the 7D degrees of freedom, vanish
in the deep IR limit of the 7D field theory.
49

<!-- Page 51 -->

5.1 Unfrozen SymTFTs
Let us first analyze what we expect from a bottom-up field theory perspective for the frozen
singularities. In other words, let us just assume we have a 7D SYM theory with some simple
gauge algebra g. This will doubly serve as a review of the SymTFT construction for 7D
gauge theories. If we let G denote the associated simply-connected group, then this gauge
theory is a priori a relative theory with a defect group [56,12,19,22]

## D = Z(G)(1) ⊕Z(G)(4), (5.3)

whose charged objects are Wilson/’t Hooft defects whose representations have non-trivial
highest weights/coweights in the quotients Λg /Λg and Λg /Λg , respectively. These
wt root cowt coroot
objects are charged under 1-form/4-form symmetries which can be coupled to background
Z(G)-valued gauge fields b and b , respectively. These symmetries have a mixed ’t Hooft
2 5
anomaly which is captured by a term in the 8D SymTFT action of the form
(cid:90)
S = 2π(L ) bi ∪δbj . (5.4)
BF Γ ij 2 5

## 8D

Note that for g = so(4k) the center symmetry has two factors and one needs two linearly
independent background fields with a (2×2) matrix (L ) . In all other cases, to which we

### Γ ij

will restrict not to clutter notation, i = j and L becomes a number.

## Γ

The coefficients L have a natural interpretation in the 8D SymTFT as the link pairing

## Γ

of Wilson surface operators for the b and b dynamical gauge fields. These are defined by
2 5
(cid:18) (cid:90) (cid:19) (cid:18) (cid:90) (cid:19)
U (Σ ) = exp i b , U (Σ ) = exp i b , (5.5)
m 2 2 e 5 5

## Σ2 Σ5

and have the algebraic relation
(cid:0) (cid:1)
U (Σ )U (Σ ) = exp 2πiL Link(Σ ,Σ ) U (Σ )U (Σ ), (5.6)
m 2 e 5 Γ 2 5 e 5 m 2
withLink(Σ ,Σ )definedasthelinkingnumberofΣ andΣ intheeight-dimensionaltheory
2 5 2 5
with worldvolume X ×[0,1]. A key feature of the SymTFT paradigm is that these Wilson
7
surface operators can appear as either topological symmetry operators or (generally nontopological) defect operators depending on whether Σ /Σ are along the interval direction
2 5
or not, see Figure 10. For example, when Σ = L ×[0,1] ⊂ X ×[0,1] and Σ ⊂ X ×{T },
2 1 7 5 7 0
then the linking amounts to the statement that a codimension-two topological symmetry
operators acts on the Wilson line charged under Z(G)(1).
While the U and U operators are both free to end on the T = 0 boundary because they
e m
end on gauge theoretic defect operators of the 7D gauge theory, on the B boundary at
top
T = 1, onemustchooseaconsistentcombinationofNeumann/Dirichletboundaryconditions
for b and b . This is easiest to see if we quantize the SymTFT on constant T slices (or
2 5
50

<!-- Page 52 -->

Figure 10: Illustration of the T (M)[g(n/d)] boundary at T = R = 0. The U (green) and U
m e
(purple) operators of the SymTFT can both end on this boundary on a Wilson line and ’t
Hooft defect, respectively. When U / U are placed parallel to the T = 0 boundary they
m e
appear as topological symmetry operators for the 4-form/1-form global symmetries.
equivalently constant R slices) whereby the possible boundary states |B ⟩ transform under
top
the algebra (5.6). In particular one cannot simultaneously diagonalize U and U but rather
e m
a combination of Uℓ and Uk for some powers ℓ and k such that their linking vanishes. For
e m
simplicity, we illustrate in Figure 11 the cases where (ℓ,k) = (1,0) and (0,1). When U
m
is diagonalized on |B ⟩, then b | has a definite value (up to gauge transformations)
top 2 Btop
so we identify this with Dirichlet boundary conditions, moreover the algebra (5.6) implies
that b | has Neumann boundary conditions. Such a scenario is specifies an “electric
5 Btop
polarization” for the gauge algebra which means that the gauge group is simply-connected.
From a top-down point of view, these gauge theoretic objects can also be constructed
directly from M-theory for frozen and unfrozen ADE singularities. The U and U opere m
ators are associated with M5 branes and M2 branes, respectively, and they correspond to
defects/symmetry operators in the gauge theory depending on whether or not the branes
have support along the radial direction or remain far away from the singularity [52,55], see
also [54,53]. Indeed the SymTFT action follows from reducing the 11D action of M-theory
on S3/Γ and truncating to the topological degrees of freedom, see Appendix B of [65]. The
coefficients L are then deduced from the geometry of the M-theory background, namely by

## Γ

the link pairing on H (S3/Γ,Z), which is summarized for the ADE cases in Table 8 which
1
we borrow from [52].
51

<!-- Page 53 -->

Figure 11: Here we show two possible boundary conditions on B . The top-half showcases
top
“fully electric” boundary conditions while the bottom-half shows “fully magnetic” boundary
conditions. For all unfrozen SymTFTs these respectively lead to a simply-connected gauge
group or 7D gauge group where the full center 1-form symmetry is gauged.
5.2 Frozen SymTFTs
With the review material of the previous subsection in place, we are now ready to address a
puzzle that arose in our defect group calculations for some of the frozen singularities:
Whenever g(n/d) = {D(1/2),e(1/3),e(1/4)}, we have the expected line defects from the frozen
k 6 7
gauge algebra D(1) = Z(H )(1), but an “excess” of four-dimensional defects, i.e.,

### Γ,d


## |D(4)| > |Z(H )(4)|. (5.7)


### Γ,d

To understand the SymTFT interpretation of what is going on, let us for concreteness
focus on the e(1/4) case. Similar remarks will carry over for D(1/2) and e(1/3), and we discuss
7 4 6
the D(1/2) cases at the end. In this case then, h = ∅ so clearly the defect group would be
k>4 e7,4
trivial if one were only considering the gauge degrees of freedom. However, as calculated in

### Section 4.3, the defect group is

D(cid:0) e(1/4)(cid:1) = D(cid:0) e(1/4)(cid:1)(1) ⊕D(cid:0) e(1/4)(cid:1)(4) = 0(1) ⊕Z(4). (5.8)
7 7 7 2
Wecanunderstandthismismatchbytabulatingthesymmetryoperatorsanddefectoperators
in the twisted F-theory frame. Recall that the twisted F-theory background further reduced
on an S1 leads to M-theory on Z = (I × S1)/Z where Z acts on the I fiber as an
0 θ 4 4 0
S ∈ SL(2,Z) transformation. An M5 brane on a relative 3-cycle Σ ∈ H (Z,∂Z) whose
3 3
boundary ∂Σ is the generator of Tor (cid:0) H (∂Z) (cid:1) = Z engineers the defect operator charged
3 2 2
52

<!-- Page 54 -->

under the 4-form symmetry Z(4) (albeit reduced on the M-/F-theory circle). From the
2
homology computations in Section 4.3, we can conclude that that this relative 3-cycle has a
boundary in H (∂Z) which wraps the base circle S1 of ∂I and a 1-cycle in the boundary.
2 ϕ 0
The precise 1-cycle is only important modulo (ρ −1) acting on the 2-cycles of H (∂I ) with
2 2 0
one leg along the base which span a sublattice Z2 ⊂ H (∂I ). In this case
2 0
(cid:18) (cid:19)
0 −1
ρ = . (5.9)
2
1 0
In F-theory language this defect is a (p,q)-fivebrane wrapping the C base of I whose (p,q)
0
charge is non-trivial modulo23
(cid:18) (cid:19)
−1 −1
. (5.10)
1 −1
Meanwhile, as mentioned in Section 4.3, there is no electric defect operator because the
putative one would arise from wrapping M2 branes on H (Z,∂Z)/H (Z) = (Z⊕Z )/(Z⊕
2 2 2
Z ) = 0. All together this means for the SymTFT that while U (Σ ) can end on the
2 e 5
T (M)[e(1/4)] boundary in Figure 10 as expected, the U (Σ ) operator cannot. In fact, because
7 m 2
the T (M)[e(1/4)] boundary is gapped, in perfect analogy to B boundary at T = 1, we simply
7 top
have another set of topological boundary conditions and the geometry enforces that b |

## 2 T=0

is Neumann and b | is Dirichlet, see Figure 12.

## 5 T=0

Such boundary conditions at T = 0 are less surprising when we explicitly perform the
dimensionalreductionofM-theoryonZ whichisapurelygeometricalbackground; thisyields
a6DtheorywhichistheS1-reductionofthe7Dtheoryofinterest. Themainingredientisthe
fact that Tor (cid:0) H2(Z) (cid:1) = Tor (cid:0) H1(Z;U(1)) (cid:1) = Z ̸= 0, which leads to a dynamical Z -valued
2 2
(cid:0) (cid:1)
2-formb6D fromexpandingC onTor H1(Z;U(1)) . Fromthelongexactsequenceofrelative
2 3
(cid:0) (cid:1) (cid:0) (cid:1)
(co-)homology, we have a map Tor H2(Z) → Tor H2(∂Z) from restriction of forms, so
this 2-form field of the 6D theory is identified with the 2-form field b7D of the 7D SymTFT
2
(cid:0) (cid:1) (cid:0) (cid:1)
which is the reduction of C on Tor H2(∂Z) = Tor H1(∂Z,U(1)) , i.e. b6D = b7D| . We

## 3 2 2 T=0

drop the 7D / 6D superscripts below whenever the context is clear.
(cid:0) (cid:1)
On the other hand since Tor H3(Z) = 0, we cannot expand C to get a dynamical
6
Z -valued 4-form which would have been the F-/M-theory circle reduction of a b7D|

## 2 5 T=0

with Neumann boundary conditions if that cohomology were non-vanishing. We leave more
technical details of this reduction to Appendix B, where we also explicitly derive a 7D
“counterterm”
(cid:90)
Sc.t. = π b ∪b , (5.11)

## 7D 2 5


## T=0

localized on the T (M)[e(1/4)] boundary. In fact, it is easy to see that the equations of motion
7
(cid:82)
for the bulk-boundary system S = Sc.t. + S , with S = π b ∪ δb the SymTFT

## 7D Bf Bf 8D 2 5

derived from the geometry of ∂Z, sets b8D| = b7D. So this counterterm “implements” the

## 5 T=0 5

23(p,q)=(1,1) is one representative one can use for the Z generator.
2
53

<!-- Page 55 -->

Figure 12: The two possible B boundary conditions for the e(1/4) SymTFT. For the fully
top 7
magnetic boundary condition (left), the 7D theory has a magnetic defect and 4-form symmetry operator, while the fully electric boundary condition (right) admits 1-form symmetry
operators which do not act on any defects.
boundary conditions at T = 0 given the Neumann boundary conditions of b .24
2
Addressing now the symmetry operators, in terms of M-theory on Z, the electric 1-
form symmetry operators are given by wrapping M5 branes on Tor (cid:0) H (∂Z) (cid:1) = Z and the
2 2
magnetic 6D 3-form (which lifts to a 7D 4-form in F-theory) symmetry is given by an M2
branes wrapping Tor (cid:0) H (∂Z) (cid:1) = Z . These operators are topological from the point of view
2 2
of the field theory because they are formerly infinitely far away from the interior of Z [55].
These respectively lift to (p,q)-fivebranes wrapping the base of ∂I and (p,q)-strings placed
0
on a point in in the circle base of ∂I . This picture of symmetry operators is not qualitatively
0
different from the unfrozen singularities: the SymTFT implies that we still have a algebra
(5.6) acting on the boundary state |B ⟩ which means we have to pick a consistent set of
top
boundary conditions for the topological operators. In this case, because Z has no non-trivial
2
subgroups, there are only two either fully electric, or fully magnetic. See Figure 12, where we
illustrate the two possible boundary conditions for B . Notably, the fully electric boundary
top
conditions implies that there is a 1-forms symmetry defect which does not faithfully act on
any operators in the 7D theory.
Our discussion of the e(1/4) singularity applies equally well to D(1/2) and e(1/3) cases if one
7 4 6
replaces Z with Z2 and Z throughout and with the counterterm in (5.11) generally taking
2 2 3
24Analogous conclusions also apply to unfrozen M-theory models on complex surfaces X◦ with
Tor (cid:0) H (X◦) (cid:1) ̸= 0, which was relevant in understanding the SymTFT in the context of 7D supergravity
1
models and their global structure [64,67].
54

<!-- Page 56 -->


## Γ Z(G ) = H (S3/Γ) L


## Γ 1 Γ

Z Z 1/k
k k
(cid:32) (cid:33)
k k −1

## D Z ×Z 1

2k 2 2 2 k −1 k
D Z 2k−1
2k+1 4 4

## Γ Z −1/3


## E6 3


## Γ Z 1/2


## E7 2


## Γ ∅ 0


## E8

Table 8: Linking invariants for the 3-manifolds S3/Γ. The numerical values in the L column

## Γ

are well-defined in Q/Z.
the form
(cid:90)
Sc.t. = 2π(L ) bi ∪bj . (5.12)
7D Γ ij 2 5

## 7D

As for the D-type cases with a non-trivial gauge algebra, D(1/2), recall that the defect groups
k>4
are
D(D(1/2)) = (Z )(1) ⊕(Z2)(4) (k even), or (Z )(1) ⊕(Z )(4) (k odd). (5.13)
k>4 2 2 2 4
For k even or odd, there is a (Z )(4) subgroup which behaves similarly to the fully frozen
2
cases: for one choice of B boundary condition, there exists a 4-manifold defect charged
top
under this 4-form symmetry group and for another choice there exists a (Z )(1) symmetry
2
operator which does not act on any defect. Additionally, there is a (Z )(1)⊕(Z )(4) quotient
2 2
subgroup of

### D(cid:0) D(1/2)(cid:1)

for which the expect fundamental Wilson / ’t Hooft defects for a
k>4
sp(k) gauge theory are valued in. Generally speaking, this subtlety is required when the
(cid:0) (cid:1)
5-manifold Z has non-trivial torsion in first homology, Tor H (Z) ̸= 0.
1
(1/2)
5.3 e
6
One interesting feature of (5.4) for the T (M)[e(1/2)] theory, which is an su(3) gauge theory,
6
is that the ’t Hooft anomaly coefficient differs from the su(3) gauge theory engineered from
M-theory on C2/Z . We can denote the latter theory by T (M)[A(0)], and we see from Table 8
3 2
that its coefficient for the mixed electric 1-form/magnetic 4-form ’t Hooft anomaly is 1/3
while T (M)[e(1/2)] has a coefficient of −1/3.
6
To account for this difference, T (M)[e(1/2)] must differ from T (M)[A(0)] by some additional
6 2
topologicaldegreesoffreedom. Notethatafieldtheoristwouldsaythatthe’tHooftanomaly
coefficient of D-dimensional su(3) gauge theory would canonically be 1/3 since this fixes the
55

<!-- Page 57 -->

action a generator, say, the generator of (Z )(1) which is U (M ) in our notation, to act
3 e D−2
on a Wilson line in the fundamental representation by a phase exp(2πi/3). A phase of
exp(−2πi/3) would mean that the fundamental Wilson line appears as the anti-fundamental
Wilson line25. This difference just amounts to a shift in the counterterm
(cid:90)
2π
Sc.t. = b ∪b . (5.14)

## 7D 3 2 5


## 7D

which indeed inflows into the 8D bulk to give the correct difference in SymTFTs between the
T (M)[e(1/2)] theory and the T (M)[A(0)]. In more modern field theory language, two theories
6 2
that differ by a local topological counterterm differ by a stacking of a symmetry-protected
topological (SPT) phase so our conclusion can then be written schematically as
T (M)[A(0)] = T (M)[e(1/2)]⊗ (cid:0) SPT(b ,b ) (cid:1) ⊗(...), (5.15)
2 6 2 5
where SPT(b ,b ) has the action (5.14)26. We have added (...) to (5.15) to signify that we are
2 5
ignoring other possible topological sectors which may appear on the (un)frozen singularities
such as 7D fractional quantum Hall phases [98].
(1/4)
5.4 e
8
Since the frozen singularity hosts a 7D SYM theory with gauge algebra su(2) one expects a
SymTFT capturing the mixed ’t Hooft anomaly between Z 1-form and 4-from symmetries.
2
However, the geometrical and F-theory calculation shows that the actual SymTFT is trivial,
see Table 6. This means that the 7D su(2) theory localized at the singularity must somehow
forbid the existence of genuine Wilson and ’t Hooft operators in half-integer spin representations of SU(2). We can reconcile these two observations by the inclusion of an additional
topological theory in the 8D bulk of the form
(cid:90)
∆S = π b ∪δb . (5.16)
2 5
This term combines with the SymTFT of the su(2) gauge theory to produce
(cid:90) (cid:90) (cid:90)
S +∆S = π b ∪δb +π b ∪δb = 2π b ∪δb . (5.17)

## Bf 2 5 2 5 2 5

25One can of course act by charge conjugation (i.e. su(3) outer automorphism) to go between these two
scenarios. Considering the remarks on the counterterm (5.14), performing a charge conjugation would then
appear to shift the theory by this term. This means that these theories have a mixed ’t Hooft anomaly
between charge conjugation, the electric 1-form, and magnetic 4-form symmetries. Such an anomaly can be
derived directly from M-theory from the considerations of [97].
26Note that the fact that an SPT is by definition an invertible topological theory, one could invert this
equation to T(M)[A(0)]⊗ (cid:0) SPT(b ,b ) (cid:1)∗ =T(M)[e(1/2)]⊗(...).
2 2 5 6
56

<!-- Page 58 -->

But this term is trivial, in the sense that it does not produce any phases in linking the
extended operators (5.6). At the same time it produces a boundary term on the physical
boundary, that takes the form of a counterterm only depending on background fields
(cid:90)
Sc.t. = π b ∪b . (5.18)

## 7D 2 5


## 7D

This counterterm is responsible for breaking the 1- and 4-form symmetries. For that one
simply realizes, that the system of boundary theory and SymTFT is invariant under 1-
form and 4-form gauge transformations, thus after the inclusion of Sc.t. the variation of

## 7D

the complete system can be deduced by the properties of the counterterm alone. With the
variations given by
b → δλ , b → δλ , (5.19)
2 1 5 4
weseethat(5.18)isnotinvariantunder4-formsymmetriesfornon-trivialb andnotinvariant
2
under 1-form symmetries for non-trivial b .
5
To better understand the effect of adding such a counterterm to the su(2) gauge theory,
let us consider a similar such counterterm in a U(2) gauge theory as well as what happens
after decoupling the overall U(1)27. We parameterize the U(2) connection in terms of its
SU(2) and U(1) parts as28
A = A+ 1a1 , (5.20)
2 2×2
where f = da = Tr(F) is quantized such that (cid:82) f ∈ Z. The (bosonic) action for the SYM

## Σ2

theory is
(cid:90)
S = 2π Tr(F ∧∗F)+2C ∧f +2B ∧∗f , (5.21)

## Ym 5 2

where we have turned on the background fields for the U(1)(1) electric and U(1)(4) magnetic
e m
symmetries. The former acts on the fields as
a → a−2λ , (5.22)
1
B → B +dλ . (5.23)
2 2 1
The latter meanwhile can be expressed in terms of the electromagnetic dual 4-form of the
U(1) connection, da ≡ ∗f, as
(cid:101)
a → a−2λ , (5.24)
(cid:101) (cid:101) 4
C → C +dλ . (5.25)
5 5 4
The electric and magnetic topological symmetry operators are U(e) = exp(iη (cid:82) ∗f) and
η
27Thisissimilartotheapproachof[99]and[13]whichalsostudiedgaugetheorieswithasu(N)Liealgebra
via a U(N) gauge theory.
28In terms of the equivalence U(2)=(SU(2)×U(1))/Z , a/2 is the connection for the U(1) factor in the
2
numerator.
57

<!-- Page 59 -->

U(m) = exp(iθ (cid:82) f), respectively.
θ
The fact that the Lagrangian (5.21) is neither invariant under U(1)(1) gauge transfore
mations when C ̸= 0 nor under U(1)(4) gauge transformations when B ̸= 0 is of course
5 m 2
due to the mixed U(1)(1)-U(1)(4) anomaly with a 9-form anomaly polynomial proportional
e m
to dB ∧dC . In 8D SymTFT terms, this means we can consider a coupled 7D-8D system
2 5
with action
(cid:90)
S + (2B ∧dC ) , (5.26)

## Ym 2 5


## M7×[0,1]

which is simultaneously invariant under U(1)(1) and U(1)(4) gauge transformations. The
e m
action of the 8D piece reproduces the 9-form anomaly polynomial after taking an exterior
derivative and contributes to anomaly in-flow via a 7D term
(cid:90)

## S = 2 B ∧C , (5.27)

inflow 2 5

## M7

which means S +S is invariant. Adding a counterterm
YM inflow
(cid:90)

## S = −2 B ∧C , (5.28)

c.t. 2 5

## M7

would mean that S +S +S is no longer invariant under generic gauge transforma-
YM inflow c.t.
tions of the U(1) higher-form global symmetries.
If we now make B dynamical, i.e., the transformations (5.22) and (5.23) become gauged,
2
we obtain an SO(3) gauge theory because 1a can be now be trivialized. The theory with
2
action S +S now has a Z valued background field C since the equations of motion for

### YM sym 2 5

the, now dynamical field, B is 2dC = 0. C is of course the background field form the usual
2 5 5
magnetic Z(4) symmetry for a SO(3) gauge theory. The generating topological operator for
2
this symmetry is given by
(cid:18) (cid:90) (cid:19) (cid:18) (cid:90) (cid:19)
i
U(m) = exp f = exp i B , (5.29)
−1 2 2
where the last equality follows from from the ∗f equations of motion df = 2dB . On
2
the other hand, the theory with action S + S + S is not invariant under C gauge

### YM sym c.t. 5

transformations and therefore does not have a magnetic Z(4) symmetry.
2
A natural question is then: what defects are allowed in the SU(2) 7D SYM theory with
the counterterm S ? Without the counterterm, the SU(2) gauge theory has a genuine
c.t.
Wilson line in the fundamental representation: W . We claim that this operator cannot
2
appear in the theory with the added counterterm, and the lattice of genuine Wilson lines is
instead generated by W . In terms of the U(2) gauge fields, the fundamental Wilson line
3
58

<!-- Page 60 -->

can be expressed as
(cid:18) (cid:90) (cid:19)
i
WU(2) = WSU(2)exp a , (5.30)
2 1/2 2 2
so we see that under U(1)(1):
e
(cid:18) (cid:90) (cid:19)
WU(2) → WU(2)exp −i λ . (5.31)
2 2 1
1/2 1/2
On the other hand, the bosonic action with the counterterm transforms as
δ (S +S +S ) = −2B ∧dλ , (5.32)
m YM sym c.t. 5 1
which introduces an extra sign in the braiding between exp(i (cid:82) B ) and WU(2). More pre-
5 2
1/2
cisely, recall that the term B ∧f = B ∧da gives the braiding relation29
5 5
(cid:18) (cid:90) (cid:19) (cid:18) (cid:90) (cid:19)
exp i B WU(2)(Σ ) = eiπLink(Σ5,Σ1)WU(2)(Σ )exp i B , (5.33)
5 2 1 2 1 5
1/2 1/2

## Σ5 Σ5

where Link(σ ,Σ ) ∈ Z is the linking number. However, the gauge non-invariance (5.32)
5 1
implies that we cannot fix the overall sign:
(cid:18) (cid:90) (cid:19) (cid:18) (cid:90) (cid:19)
exp i B WU(2)(Σ ) = ±eiπLink(Σ5,Σ1)WU(2)(Σ )exp i B (5.34)
5 2 1 2 1 5
1/2 1/2

## Σ5 Σ5

(cid:82)
From (5.29), we see that we cannot unambiguously define a linking between exp((i/2) ∗f)
and WU(2), but this is contradictory since WU(2) should satisfy (cid:82) ∗f = 1/2 for any S5 that

## 2 1/2 2 1/2 S5

links with it. Therefore we see that WU(2) cannot be consistently included in the spectrum
2
1/2
of extended operators of the theory.30
Similar considerations follow for the non-genuine minimal charge ’t Hooft defects of the
SU(2) theory, as well as the non-genuine fundamental Wilson/genuine minimal charge ’t
Hooft operators of the SO(3) theory with the added counterterm. In fact, we expect an
equivalence of theories
T (M)[e(1/4)] = (SO(3) 7D SYM + S ) = (SU(2) 7D SYM + S ) , (5.35)
8 c.t. c.t.
as they cannot be distinguished either at the level of their extended operators in flat space
or their global symmetry operators. We leave the understanding this equivalence on more
general manifolds as well as how one proper treatment of the difference in topological sum
over different principle bundles to future work.
Finally, we comment that we can apply this same procedure of adding a counterterm to
29We have now restored notation indicating the manifolds that the operators are supported on.
30Onecouldequivalentlyphrasethisintermsofthequantizationofthis7Dtheoryonaspatialworldvolume
S5×R1,wherewecannotdefinea (cid:82) ∗f =1/2sectoroftheHilbertspaceinthepresenceofthecounterterm.

## S5

59

<!-- Page 61 -->

pure non-Abelian gauge theories to completely break their higher-form symmetries. This
applies regardless of the dimension or the amount of supersymmetry. Explicitly, consider a
D-dimensional pure gauge theory (possibly coupled to adjoint matter) with gauge group G.
We have the higher-form symmetries
Z(G)(1) ⊕π (G)(D−3). (5.36)
1
If we denote G(cid:101) as the simply-connected cover of G(cid:101), then the (D+1)-dimensional SymTFT
has an Lagrangian term proportional to (L ) bi∪δbj where bi are p-forms valued in Z(G(cid:101))
g ij 2 D−2 p
with the index i running over the simple factors of Z(G(cid:101)). Here (L ) are physically the 1-/4-
g ij
form mixed ’t Hooft anomaly coefficients which depends solely on g. The symmetries (5.36)
are completely broken if we add a counterterm
(cid:90)
(L ) bi ∪bj . (5.37)
g ij 2 D−2

## Xd

As before this makes the lattice of genuine Wilson / ’t Hooft defects such that they have
trivial charge under higher-form symmetries, or more specifically, their (co)weight labels are
(co)roots. Such a situation could be called a “trivial polarization” of the gauge algebra.
6 Applications
Having understood the defect groups, higher-form symmetries, and SymTFTs of M-theory
frozensingularities,wenowturntoapplyingthisdatatobetterunderstandmorecomplicated
M-theory backgrounds.
Asourfirstapplication, wewillstudyM-theoryonaI∗ Kodairasurfacewithtwofrozen
4+k
D-type singularities. Such a geometry, when lifted to F-theory by taking the elliptic fiber to
zero size, becomes equivalent to a k D7-branes probing a O7+ singularity. For k = 0, it was
conjectured in [74], that there is a so-called “evenness condition” whereby a (p,q)-string can
endontheO7+ planeonlyifpandq areeven. Thisconditionwascrucialin[74]forproviding
consistent lattices of electric/magnetic charges for 8D N = 1 supergravity theories with nonmaximal rank. We will see how this condition arises from the defect group calculation of
D(1/2) and how this condition is relaxed when k > 0.
4
As a second application, we study M-theory on compact K3 manifolds with frozen singularities. From understanding the defect groups, one can understand the global structure
of the 7D N = 1 gauge group, or equivalently, what representations electric particles and
magnetic 3-branes can take with respect to the 7D gauge algebra
g = g ⊕u(1)b2 = (⊕ g )⊕u(1)b2. (6.1)
full ADE i i
Here each g corresponds to a singularity in the K3 of the form C2/Γ , g is the noni gi ADE
60

<!-- Page 62 -->

Abelian part of g , and b is the second Betti number of the K3. The corresponding 7D
full 2
gauge group can then generally be of the form
G /Z ×U(1)b2

## Ade


## G = (6.2)

full Z′
forsomesimply-connectednon-AbeliangroupG , andfinitegroupsZ andZ′. Concretely

## Ade

we will discuss M-theory on T4/Γ for all cases of Γ where frozen singularities appear, as well
as an elliptically-fibered K3 with two II∗ singularities.
Note that in both of these examples we will requires that the total flux vanishes, i.e.,
(cid:90)

## G = 0. (6.3)

4

## X

For the first application, this is required in order to have a well-defined F-theory uplift since
otherwise the G flux becomes a “KK-flux” with respect to the F-theory circle direction
4
whose radius is inversely proportional to the volume of the M-theory elliptic fiber. For the
second this is required in order to have a 7D N = 1 background which has a vanishing
cosmological constant31. Therefore given some collection of N frozen singularities each
sing.
with their own fractional flux labels r , we require32
i
Nsing.
(cid:88)
r = 0 mod 1, (6.4)
i
i=1
such that the total flux can vanish.
6.1 Only Even Charge Strings Can End on an O7+ Plane
As mentioned above, an O7+ in F-theory compactified on a circle is equivalent to M-theory
on a type I∗ Kodaira surface with two D(1/2) frozen singularities as shown in Figure 13.
4 4
Recall from Table 6 that the defect group of a frozen D(1/2) singularity is
4

## D(D(1/2)) = (Z ×Z )(4), (6.5)

4 2 2
which only has a magnetic 4-form piece while the electric 1-form symmetry is trivial. This
means that while M5 branes are free to wrap the two generating relative 2-cycles in Table 5,
M2 branes are forbidden to wrap such relative 2-cycles.
We already see intuitively that for the I∗ fiber in Figure 13, there can be no M2 branes
4
wrapping the relative 2-cycles of I∗ fiber which generate the group Z2 since they are made
4 2
of linear combination of the two D relative 2-cycles. Upon lifting to F-theory, this then
4
31Relaxing this condition would also relax the Ricci-flatness condition of the internal four-manifold.
32We implicitly consider rational lifts rˆ which satisfy (cid:80)Nsing.rˆ =0.
i i=1 i
61

<!-- Page 63 -->

reproduces the statement that (p,q)-strings of odd p or q cannot end on the O7+ plane.
More rigorously, the relative 2-cycles of the I∗ fiber which generate Z2 are given by (using
4 2
the notation of Figure 2):
T = 1(α +α +α +α ), (6.6)
s 2 1 3 5 7
T = 1(α +α +α +α ). (6.7)
c 2 1 3 5 8
ConsideringthedecompositionoftheD affineDynkindiagramintotwoD Dynkindiagrams
8 4
connected by a node (whose corresponding cycle is α ), we have that the relative 2-cycles
4
for one of the D singularities is33
4
T(1) = 1(α +α ), (6.8)
s 2 1 3
T(1) = 1(α +α ), (6.9)
c 2 1 0
while for the second D singularity it is
4
T(2) = 1(α +α ), (6.10)
s 2 5 7
T(2) = 1(α +α ). (6.11)
c 2 5 8
By the defect group calculation before, M2 branes are forbidden to wrap T(i) or T(i). We
s c
then obtain the evenness from the relation T = T(1) +T(2) and T = T(1) +T(2).
s s s c s c
If one instead considers an M-theory compactification on a I∗ singularity where k > 0,
4+k
then we can consider a central fiber with D(1/2) and D(1/2) frozen singularities34. In F-
4 4+k
theory this system consists of k D7-branes probing the O7+. Using the fact that the D(1/2)
4+k
singularity has a non-trivial 1-form symmetry piece when k > 0, we see that the evenness
condition no longer holds as an M2 brane can wrap a I∗ relative 2-cycle that ends on the
4+k
D(1/2) singularity. Concretely, let us take k to be even, then the relative 2-cycles for the
4+k
D(1/2) singularity are
4+k
T(2) = 1(α +α +...+α +α ), (6.12)
s 2 5 7 k+1 k+3
T(2) = 1(α +α +...+α +α ). (6.13)
c 2 5 7 k+1 k+4
The I∗ relative 2-cycles T and T are given as in Table 5, and we have the relation
4+k s c
T +T = T(2)+T(2). Therefore, M2 branes are allowed to wrap a Z subgroup of the possible
s c s c 2
Z2 group of I∗ relative 2-cycles. These are none other than the invariant combination of
2 4+k
(p,q) strings which end on this 7-brane system which appear as Wilson lines for the sp(k)
33Note that α can be expressed as a linear combination of the other α because the elliptic fiber class
0 i
vanishes: [E]∼0∈H (X ,∂X )/H (X ).

## 2 I∗ I∗ 2 I∗

4 4 4
34If we more generally consider, a D(1/2) and D(1/2) singularity where k +k = 8+k then in F-theory
k1 k2 1 2
language this involves turning on Wilson lines along the F-theory circle direction for the D7 brane stack
probing the O7+ [4].
62

<!-- Page 64 -->

Figure 13: Illustration of the elliptic F-theory geometry corresponding to an O7+. Here the
I∗ fiber is such that its central P1 is resolved (the α cycle in the notation of Figure 2).
4 4
There are then two D -type singularities, each with a frozen flux.
4
gauge theory with a non-trivial charge under Z(1), which is consistent with [74].
2
In the M-theory frame the M5 branes are not restricted and can end on the frozen
singularities. For F-theory this lifts to the fact that the (p,q)-5-branes do not have to satisfy
anevennesscondition, whichwascrucialforthecorootandcoweightlatticesdiscussedin[74].
We therefore find a microscopic derivation of the evenness conditions from our results about
defects groups on frozen M-theory singularities.
Finally, we comment that while we have understood how the defect groups of the individual frozen singularities “glue together” to understand the defect group of a larger one,
we can also apply the SymTree formalism of [65] to glue together the SymTFT data of the
individual singularities. This may be useful for understanding the topological sectors and
SymTFT of F-theory 7-branes, but we leave this for future work.
6.2 M-theory on a Compact K3 with Frozen Singularities
We first cover the cases of M-theory compactified on a compact K3 manifold of the form X =
T4/Γ with frozen singularities. Since we require X to have D- and/or E-type singularities,
we are restricted to the cases of Γ being non-Abelian which are classified to be D , D ,
4 5
or Γ (the binary tetrahedral group) [100]. There are, however, three different consistent

## E6

choices for the action of D , only one for D , and two for Γ . The ADE singularities

## 4 5 E6

present in each of these cases is tabulated in Table 9. Due to the requirement that the total
flux vanishes (6.3) and the lack of A-type frozen singularities, there are essentially only four
possible configurations of frozen singularities which we also list in Table 9.
Firstly, note that M2 and M5 branes wrapped on H (X) are stable electric/magnetic
2
states under the full 7D gauge group G . In our conventions we take G to include
full full
the U(1) factors from graviphotons so it will be of rank 22 for M-theory on K3 with no
63

<!-- Page 65 -->

X ADE Singularities Frozen Singularity Configuration(s)

## T4/D D2 ⊕A3 ⊕A2 D(1/2) ⊕D(1/2) ⊕A3 ⊕A2

4 4 3 1 4 4 3 1

## T4/D′ D4 ⊕A3 D(1/2) ⊕D(1/2) ⊕D2 ⊕A3

4 4 1 4 4 4 1
(cid:16) (cid:17)4

## D(1/2) ⊕A3

4 1
T4/D′′ A6 ⊕A None
4 3 1
T4/D D ⊕A3 ⊕A2 ⊕A None
5 5 3 2 1
T4/Γ e ⊕D ⊕A4 ⊕A e(1/2) ⊕D(1/2) ⊕A4 ⊕A

## E6 6 4 2 1 6 4 2 1

T4/Γ′ A ⊕A2 ⊕A4 None

## E6 5 3 2

Table 9: Collection of ADE singularities for each possible T4/Γ such that Γ is non-Abelian
and their possible configuration of frozen singularities. The primes are used to differentiate
the different groups actions on T4.
frozen singularities, see [64] for more details. The fact that these M2 brane states lead
to the complete set of electrically charge particle states implies that Z(G )∨ = H (X),
full 2
where the ∨ denotes Pontryagin dual. The analogous statement for M5 branes implies35
π (G ) = H (X) using the fact that π (G ) = 1.
1 full 2 0 full
While these relations give us some information on the global structure of the 7D gauge
groups,forderivingthefulldata,weemploythemethodsof[64]whichaddressesthisproblem
for M-theory on K3 manifolds and spells out the details for X = T4/Γ in particular36. The
general procedure of [64] is to consider the decomposition of X into open sets X◦ := X\S
and U where S is the collection of singular points of the K3 manifold and U is a disjoint

## S S

union of open patches around each singularity. Topologically ∂U is equivalent to a disjoint

## S

union of spaces of the form S3/Γ where each Γ characterizes an ADE singularity in the
i i
K3. Next, consider the Mayer–Vietoris (MV) sequence with respect to this decomposition:
0 → H (X◦) −→ j2 H (X) − ∂ →2 ⊕ H (S3/Γ ) −→ ι1 H (X◦) −→ j1 0, (6.14)
2 2 i 1 i 1
where we have implicitly used the fact that H (X) = 0 and H (U ) = 0 for k > 0. The maps
1 k S
on the homology groups descend from the embeddings j : X◦ (cid:44)→ X and ι : ∂U (cid:44)→ X◦, as

## S

well as the boundary map on k-cycles, ∂ . The main idea of [64] was to extract Z and Z′ of
k
(6.2) from the various maps of this exact sequence. Namely, we have that
Z ≃ coker(∂ ) = im(ι ), Z′ ≃ im(∂ )| = ker(ι ), (6.15)
2 1 2 free 1
where we have used the symbol ≃ as those isomorphisms are not generally canonical. The
map ∂ then contains the information of how M2/M5 branes wrapping classes in H (X) are
2 2
35Togetherthismeansthatthe7DgaugegroupsatisfiestheparticularrelationZ(G )∨ =π (G )which
full 1 full
is called a “maximally mixed polarization” [64,67]. We will see that in the frozen cases, this relation need
not hold in general.
36See also [67] for similar work in the context of IIB.
64

<!-- Page 66 -->

charged under g , and | denotes the restriction to the free part of H (X). In particular,

### ADE free 2

the image of ∂ on M2 brane states tells us what possible charges of the center Z(G /Z)

## 2 Ade

that the electric particles may take. Conversely, the image of ∂ on M5 brane states tell us
2
the possible monopole charges which are valued in π (G /Z). Together this is enough

## 1 Ade

to fully fix Z by charge completeness37 [101], as well as the group Z′ which tells us how
G /Z mixes with the U(1) factors.

## Ade

For compact K3 manifolds with frozen singularities, all we have to do is essentially
modify the defect groups of the D- and E-type frozen singularities according to Table 6.
From the frozen configurations in Table 9, we see that all of these cases involve at least
one D(1/2) singularity which forbids38 M2 branes from wrapping 2-cycles in H (X) which,
4 2
in a local neighborhood of D(1/2), appear as a relative 2-cycle whose boundary is valued in
4
H (S3/D ) = Z2. In other words, by forbidding cycles in H (S3/D ) ⊂ ⊕ H (S3/Γ ) that
1 4 2 1 4 i 1 i
an M2 branes can wrap, the representations of electric states of the 7D gauge group will be
restricted modifying the center Z(G ), as well as Z and/or Z′ in (6.2). Since we are not
full
restricting M5 branes in any way, we still see that
π (G ) = H (X), (6.16)
1 full 2
whenever39 π (G ) = 1, which holds for all of the T4/Γ cases. As we will see, the relation
0 full
(6.16) will be quite useful in lieu of full knowledge of the full presentation of the all the maps
in the MV sequence.
For concreteness, let us work through the derivation of G in the case of T4/Γ . The
full E6

### MV sequence (6.14) in this case is40

0 → Z3 −→ j2 Z3 ⊕Z − ∂ →2 Z ⊕Z2 ⊕Z4 ⊕Z ≃ Z2 ⊕Z3 −→ ι1 Z −→ j1 0, (6.17)
3 3 2 3 2 3 6 3
where we have decomposed the H (∂U ) entry as Z(E ) ⊕ Z(Spin(8)) ⊕ Z(SU(3))4 ⊕

## 1 S 6

Z(SU(2)). From Appendix C of [64], we have that in the unfrozen case the full gauge
group is:
(E ×Spin(8)×SU(3)4 ×SU(2))/Z ×U(1)3
(cid:0) T4/Γ (cid:1) : G = 6 3 . (6.18)
E6 unfrozen full Z3
6
Which from (6.15) tells us that coker(∂ ) = Z and Im(∂ )| = Z3. The freezing of the D
2 3 2 free 6 4
37This is not a conjectural statement as one can derive this statement simply from the careful reduction
of the C field and analyzing the Mayer–Vietoris sequence for cohomology.
3
38Notethatane(1/2) singularityalsoappearsbutthisdoesnotcauseanymodificationasthedefectgroup
6
is the same as the unfrozen e singularity.
6
39One may have π (G ) ̸= 1 when X contains e(1/3) or e(1/4) frozen singularities because their defect
0 full 6 7
groups are non-trivial, are not modified by the frozen flux, and reduce a simple Lie algebra to zero rank
which possibly leaves a discrete gauge group factor in G depending on the geometric details.
full
40For details on how to calculate each of the homology groups appearing in the MV sequence for each of
the torus quotient K3 manifolds see [64].
65

<!-- Page 67 -->

informsusthatM2branescannotwrapacycleinaZ2 subgroupofZ2⊕Z3. Byexactness, the
2 3 6
image of the map j is given by (63,0) in Z3⊕Z where the superscript denotes multiplicity.
2 3
Therefore the freezing must restrict M2 branes to wrap states in Z2 ⊂ H (X) with even
2
charge. This implies that the frozen gauge group is given by

## (Su(3)×Su(3)4 ×Su(2))/Z ×U(1)3

(cid:0) T4/Γ (cid:1) : G = 3 (6.19)
E6 frozen full Z2 ×Z
3 6
which is consistent with (6.16).
Performing these steps for the other frozen singularity configurations of the various T4/Γ
we arrive at

## (Su(4)3 ×Su(2)2)/Z4 ×U(1)3

T4/D (with 2×D(1/2)) : G = 2 , (6.20)
4 4 full Z4
2
(Spin(8)2 ×SU(4)3 ×SU(2))/Z4 ×U(1)3
T4/D′ (with 2×D(1/2)) : G = 2 , (6.21)
4 4 full Z3
2
T4/D′ (with 4×D(1/2)) : G = (cid:0) SU(2)3/Z3 (cid:1) ×U(1)3. (6.22)
4 4 full 2
Inthecontextofaheteroticdualofthese7Dsupergravitytheories, severalhundredexamples
of the torsion part of π (G ) were calculated in [77]. We see from entry 140 of their Table
1 full
5, our answer indeed matches Tor (cid:0) π (G ) (cid:1) = Z4 for (6.21). However entry 1 of their Table
1 full 2
5 appears to disagree with (6.20) as our answer is Z4 while theirs is Z3. These mismatch may
2 2
have to do with mixing with the U(1) factors which was not covered in [77]. The remaining
cases (6.19) and (6.22) do not appear in the list of possible Lie algebras in [77], however we
point out that this list is not completely exhaustive.
Finally, we mention M-theory on a K3 which is not a torus quotient but rather is an
elliptic fibration over P1 with two type II∗ singularities with each host an e gauge algebra.
8
If we take projective coordinates [u,v] on the P1 base, then the following Weierstrass model
y2 = x3 +u4v4x+u5v7 +u7v5, (6.23)
is an example of such a K3. In this case we can consider frozen configuration e(1/4) ⊕e(3/4)
8 8
which engineers a gauge algebra
g = su(2)⊕su(2)⊕u(1)6. (6.24)
full
From our remarks in Section 5.4 we see that the gauge group of the non-Abelian factors can
be presented as either SO(3) or SU(2) but with the additional counterterm of (5.16) which
forbids electric/magnetically charged states in the fundamental of either su(2) factor. Its
heterotic dual is a T3 compactification with a Z almost-commuting triple for which there do
4
exist non-BPS perturbative states transforming under the fundamental representation of an
66

<!-- Page 68 -->

SU(2)41. Onepossibilityisthatmassesofthesenon-BPSstatesdivergeintheM-theorylimit
where the string coupling is taken to infinity. Such a scenario would match our M-theory
prediction, but we leave such an understanding of this subtle aspect of heterotic/M-theory
duality for future work.
7 Conclusions
In this paper, we have studied several aspects of M-theory frozen ADE singularities and
have seen an interesting interplay between the geometry and the flux data. In contrast to
previous works, we have argued how the flux directly reduces the rank of the gauge algebra
without appealing to a long-chain of string dualities. We have also studied how the frozen
flux can alter the simple dictionary relating the ADE geometry to the symmetries of the
7D theory. In particular, a general feature we found is that while the frozen flux can reduce
the amount of line operators with conserved 1-form symmetry charge, the magnetic dual
defect operators charged under 4-form symmetries are preserved. We have confirmed such
features in multiple dualities frames, and provided a natural description for them in terms
of symmetry breaking boundary conditions of an 8D SymTFT.
We also applied the SymTFT framework to understanding subtle symmetry features of
of the e(1/2) and e(1/4) singularities. In particular, the latter engineers a 7D su(2) gauge
6 8
theory with neither fundamental Wilson nor ’t Hooft operators which is a new feature of a
pure gauge theory in any dimensions. We made sense of such an exotic theory by adding a
countertermwhichexplicitlybrokethehigher-formsymmetries. Suchaprocedure, whichcan
be done for any non-Abelian gauge theory of any dimension to reduce the number of naively
expected higher-form symmetries, may have pure QFT applications. Additionally, for such
theories coupled to gravity, it would be interesting to properly understand the connection
between charge completeness and lack of global symmetries, generalizing the considerations
in [102].
We also considered geometries with multiple singularites and have applied this symmetry
data above to understanding the curious “evenness condition”, a property of O7+ planes, as
well as to calculating the global gauge groups of 7D N = 1 supergravities for certain points
in the rank-reduced moduli space of M-theory on K3 manifolds. In Appendix A we also
(cid:82)
clarified why IIA ADE singularities with a boundary C monodromy freeze, in contrast to
1
the a conjectural Freed–Witten-like anomaly mentioned in [2], via a confinement mechanism.
There are numerous examples of singular string theory backgrounds which would presumably freeze via a similar mechanisms described in this paper, and considering that there
are more p-form potentials in string theory, it is clear frozen singularities occupy an understudied yet ubiquitous corner of the string theory landscape. Such backgrounds are in
some sense vast generalizations of discrete torsion orbifolds [103]. A particular realm of ap-
41We thank Hector Parra de Freitas for pointing this out to us.
67

<!-- Page 69 -->

plications that we hope to apply some of our insights is in better understanding the string
landscape of asymptotically Minkowski vacua. In the context of backgrounds with sixteen
supercharges, it is not fully known whether all D ≤ 7 vacua have been discovered or whether
there are connected components of moduli space yet to be discovered. In particular, it would
be interesting to know if such frozen M-theory/IIA vacua can be realized as strong coupling
limits of exotic string vacua such as asymmetric orbifolds (see for instance the recent studies [104,105]) or string islands [106]. Since frozen ADE singularities can be embedded in
higher dimensional special holonomy manifolds, we also expect applications to vacua with
lower amounts of supercharges. One could also embed such frozen singularities in AdS flux
vacua where the rank reduction caused by the flux can be useful in moduli stabilization.
Finally, we mention that while were able to extract some of the IIA quiver data of the
frozen singularity, it would be interesting if there was a procedure for deriving the full frozen
(cid:82)
quiver which generalizes the Douglas–Moore construction [89] to the presence of the C
3
monodromy.

### Acknowledgments

MC,LL,ET,andHYZthanktheHarvardSwamplandInitiativeandthe2024SimonsPhysics
Summer Workshop for hospitality during the completion of this work. MD and ET thank
the ESI in Vienna, in particular the program “The Landscape vs. the Swampland”, for their
hospitality during part of the time in which this work was completed. We thank F. Baume,
P. Cheng, J.J. Heckman, M. Hu¨bner, C. Lawrie, M. Montero, H. Parra De Freitas, and A.
Tomasiello for helpful discussions. The work of ET is supported in part by the ERC Starting
Grant QGuide-101042568 - StG 2021. MC is supported by the by DOE Award (HEP)
DE-SC0013528, the Simons Foundation Collaboration grant #724069, Slovenian Research
Agency (ARRS No. P1-0306) and Fay R. and Eugene L. Langberg Endowed Chair funds.
68

<!-- Page 70 -->


### A Freezing ADE Singularities with 2-Form RR Flux

In this Appendix, we study another class of frozen ADE singularities that exist in IIA where
we take a non-zero monodromy for the C RR potential:
1
(cid:18) (cid:90) (cid:19)
IIA R1,5 ×C2/Γ , C ̸= 0, where γ ∈ H (S3/Γ) = Ab(Γ) . (A.1)
1 1 1
γ1
Such vacua were mentioned in Section 4 of [2] and are related to the IIA frozen singularities
(cid:82)
with C frozen flux if one embeds the ADE singularity into an elliptically-fibered K3 and
3
performs a double T-duality. According to [2], these singularities freeze or partially freeze
because the D2 branes that wrap the blown-up exceptional cycles suffer from a dual version
of a Freed–Witten anomaly due to a G -flux along the exceptional cycle. Such an anomaly
2
is still only conjectured to exist as far as we are aware, so we rather appeal to a IIA 10D
coupling to argue that the 6D SYM theory freezes to a lower rank gauge group due to
confinement.
For concreteness, let us consider the following IIA background
(cid:18) (cid:90) (cid:19)

## Iia R1,5 ×C2/Z , C = 1/2 . (A.2)

2 1
γ1
(cid:82)
If we instead chose C = 0 then this would simply engineer a 6D N = (1,1) su(2)
γ1 1
gauge theory. As noted in [107,2], the background C field implies a non-trivial S1 fibration
1
structure in the uplift to M-theory. In particular, the background (A.2) is dual to
M-theory (cid:0)R1,5 ×(C2 ×S1)/Z (cid:1) . (A.3)
2
We now see that low-energy 6D theory we obtain in the presence of the background C flux
1
is a trivial theory as it is the dimensional reduction of a trivial 7D. To get a more hands-on
perspective of this freezing, consider the blow-up X(cid:101) → C2/Z . X(cid:101) is a smooth hyper-K¨ahler
2
space (also known as the Eguchi-Hanson space) with a generating exceptional 2-cycle which
we denote by E ∈ H (X(cid:101)). Geometrically, the long exact sequence of relative homology
2
contains the short exact sequence42
∂
0 → H (X(cid:101)) → H (X(cid:101),∂X(cid:101)) →− H (∂X(cid:101)) → 0, (A.4)
2 2 1
0 → Z → Z →− ∂ Z → 0, (A.5)
2
which motivates denoting the generator of H (X(cid:101),∂X(cid:101)) by 1E. Concretely, the class 1E can
2 2 2
be represented by a non-compact 2-cycle Γ such that ∂Γ = γ . Let G := dC , then from
2 2 1 2 1
(cid:82) C = 1/2 mod 1, we see that (cid:82) G = 1/2+M for some M ∈ Z which then implies that
γ1 1 Γ2 2
42The homology coefficients are taken to be Z implicitly.
69

<!-- Page 71 -->

there is non-zero RR flux along the exceptional cycle:
(cid:90)

## G = 1+2M ̸= 0. (A.6)

2

## E

We now explain why the flux (A.6) leads to the freezing of the su(2) gauge algebra to
a trivial gauge algebra. Recall that in the absence of the boundary monodromy, a generic
point on the Coulomb branch of the 6D su(2) gauge theory corresponds to blowing up the
singularity, i.e. taking Vol(E) ̸= 0. Since the adjoint scalar has a vacuum expectation value,
the gauge algebra is Higgsed as su(2) → u(1) and the off-diagonal vector modes are now
massive W-bosons. The IIA interpretation of such massive modes are D2 branes that wrap
E. Recall also that such D2 branes contain a topological worldvolume term
(cid:90) (cid:90)
S ⊃ a ∧G → a , (A.7)

## D2 1 2 1


## E×L L

where a is the U(1) gauge field on the D2 brane, which means that the flux (A.6) generates
1
a Wilson line defect along some line L ∈ R1,5. Such a defect corresponds to an F1 string
attachedtotheD2withaworldvolumeΣ suchthat∂Σ = L. Thisisduetothefactthatthe
2 2
combination f −B is gauge invariant. Now such an F1 string can have a second endpoint
2 2
if we wrap a D2 on −E, or equivalently an anti-D2 on E, which means that W-bosons of
opposite charge under u(1) are attached to each other by a string whose expectation value
obeys an area law at leading order. In equations, this W-boson is a charge-2 Wilson line of
the 6D u(1) theory with a 1D worldvolume L has expectation value
⟨W (L)⟩ = ⟨W (L)⟩ ·exp(−Area(Σ )/ℓ2), (A.8)
+2 +2 u(1) 2 s
where ⟨W ⟩ denotes the usual evaluation of the Wilson line in a 6D N = (1,1) u(1)
+2 u(1)
gauge theory and the dominating exponential term comes from evaluating the F1 string
action, and ℓ is the string length scale. This means that the W-bosons are confined which
s
is true even as we take Area(Σ ) → 0 because the term (A.7) is topological. Having shown
2
the off-diagonal components of the original su(2) gauge algebra confine, what about the u(1)
factor? We can argue for this by reducing the 10D topological term
(cid:90)

## G ∧C ∧H , (A.9)

2 5 3

## 10D

to 6D under the decomposition G = ω and (ω the dual to E) C = A(cid:101) ∧ω which produces
2 2 5 3 2
a term
(cid:90)
A(cid:101) ∧H . (A.10)
3 3

## 6D

where A(cid:101) is just the electromagnetic dual to the u(1) gauge potential. Since (A.10) is a
3
Stu¨ckelberg term for A(cid:101) we see that the dual U(1) potential is Higgsed or, equivalently, the
3
70

<!-- Page 72 -->

original gauge potential is confined. We have now showed that the full su(2) vector multiplet
is confined due to the C boundary monodromy.
1
We close by mentioning a more non-trivial example. consider the following duality43:
(cid:18) (cid:90) (cid:19)
M-theory (cid:0)R1,5 ×(C2/Z ×S1)/Z (cid:1) ≃ IIA R1,5 ×C2/Z , C = 1/2 . (A.11)
2 2 4 1
γ1
We expect then that the RR monodromy at the boundary partially freezes the gauge algebra
as su(4) → su(2). To see how this works, consider first the full blow-up of X(cid:101) → C2/Z where
4
X(cid:101) has three exceptional 2-cycles E . The short exact sequence of (relative) homology
i=1,2,3
groups is
∂
0 → H (X(cid:101)) → H (X(cid:101),∂X(cid:101)) →− H (∂X(cid:101)) → 0, (A.12)
2 2 1
0 → Z3 → Z3 →− ∂ Z → 0, (A.13)
4
where the pullback of the generator of Z can be given as
4

## [Γ ] = 1(E +2E +3E ), (A.14)

2 4 1 2 3
i.e. ∂Γ = γ . The boundary RR-monodromy then tells us that
2 1
(cid:90)
G = 2+4M, for some M ∈ Z, (A.15)
2

## E1+2E2+3E3

(cid:82) (cid:82) (cid:82)
which can be solved, for example, by taking G = 1, G = 0, G = −1, and

## E1 2 E2 2 E3 2

M = −1. Focusing on this solution for concreteness, although each solution will give the
same physics, we see from the previous example that D2 branes wrapping the E and E
1 3
cycles are confined. We thus keep E and E blown down and do not associated gauge
1 3
algebras with them, and see that (when Vol(E ) ̸= 0) that we have a pair of frozen A
2 1
(cid:82)
singularities each with C = 1/2 where α(1) and α(3) denote 1-cycles in the boundary
α(i) 1
1
of a local neighborhood (S3/Z )(i) surrounding the A singularity gotten by blowing-down
2 1
E and E respectively. This agrees with our RR flux values because 1E restricts to α(i)
1 3 2 i 1
along (S3/Z )(i). Finally, notice now that since E ·E = E ·E = 1, the G flux vanishes
2 1 2 3 2 2
automatically on E thus allowing it to not be frozen and leaving an su(2) gauge algebra.
2
One can repeat these arguments for more general ADE singularities by using the generalizations of the expressions of the relative 2-cycles in terms of rational linear combinations
of compact exceptional cycles which can be found in [39].
43Recall that we are assuming that γ is a generating element of H (S3/Z ).
1 1 4
71

<!-- Page 73 -->


### B Counterterm for Frozen Theories

This appendix is dedicated to deriving the claim of equation (5.12) that for the frozen 7D
theories with D(h ) ̸= D(g(1/d)), there exists a counterterm of the form

### Γ,d

(cid:90)
Sc.t. = 2π(L ) bi ∪bj , (B.1)
7D Γ ij 2 5

## 7D

localized on the T (M)[g(n/d)] boundary of the 8D SymTFT. Recall that the fully frozen
singularities are D(1/2), e(1/3), e(1/4), e(1/5), and e(1/6), where the 2-form and 5-form potentials
4 6 7 8 8
are respectively valued in Z2, Z , Z , 0, and 0. On its own, the above action would not be
2 3 2
invariant under gauge transformations of bi and bi without in-flowing from the 8D SymTFT
2 5
action
(cid:90)
2π(L ) bi ∪δbj . (B.2)
Γ ij 2 5

## 8D

On one level, it may be obvious that because the 7D theory localized on ADE singularity
has trivial gauge dynamics, which normally have a mixed 1-form/4-form anomaly one must
include such a 7D counterterm to correctly produce to the 8D anomaly theory. Clear as this
may be to some readers, we find it enlightening to understand how the counterterm appears
from the geometric reduction of the 11D supergravity action.
Our derivation will closely follow Appendix B of [65] where the action (B.2) was derived
for the unfrozen ADE singularities by reducing the kinetic term of the 11D supergravity
action, see also [72]. Intuitively, this SymTFT action carries the topological data of the
linkingofM2andM5braneswrappedonthetorsion1-cyclesofS3/Γdespiteoriginatingfrom
a non-topological kinetic term. A key difference with our approach is that we will be working
in a dual frame where the frozen singularity is realizes as an F-theory compactification on
Z = (I × S1)/Z (the action of Z on the Kodaira surface I can be found in the main
0 d d 0
text). Or more specifically, we will work in a further circle compactification of this where we
discuss M-theory on Z. We will obtain a 7D SymTFT action which is a circle reduction of
(B.2) by reducing the M-theory kinetic term on ∂Z, and obtain the counterterm by reducing
on Z. The latter is a little subtle because Z has an asymptotic boundary, which requires
properly understanding the integration of forms on Z which we will untangle.
We first reduce M-theory on ∂Z, recall that its (integer) homology groups in this case
are (recall that in these sets we are listing the entries as ∗ = 0,...,4, see Section 4.3)
H (∂Z) = {Z,Z2 ⊕Ab[Γ ],Z2 ⊕Z ,Z2,Z}, (B.3)

## ∗ X 2

which, from Poincar´e duality, means that the integer cohomology is
H∗(∂Z) = {Z,Z2,Z2 ⊕Ab[Γ ],Z2 ⊕Z ,Z}, (B.4)

## X 2

where Ab[Γ ] = Z(G ) is the center of the unfrozen gauge group, equipped with the linking

## X Γ

72

<!-- Page 74 -->

pairing L .

## Γ

For ease of notation, we will focus on the e(1/4) case, where L = 1/2 and the potentials

## 7 Γ

are Z -valued. We can regard the torsional generators of Z = Tor (cid:0) Hk(∂Z) (cid:1) (k = 2,3) as
2 2
pairs of differential forms (α ,β ) which satisfy44 (d† = ∗d∗)
k k−1
2α = dβ , d†β = 0. (B.5)
k k−1 k−1
We can expand the G and G M-theory fluxes on these cocycles as:
4 7
G ⊃ (dA +2B )∧α +dB ∧β +(dA +2B )∧α +dB ∧β , (B.6)
4 1 2 2 2 1 0 1 3 1 2
G ⊃ (dA +2B )∧α +dB ∧β +(dA +2B )∧α +dB ∧β . (B.7)
7 4 5 2 5 1 3 4 3 4 2
Expanding the kinetic terms and keeping relevant terms:
(cid:90)
1
−2πS = G ∧G (B.8)

## 11D 4 7

2

## 11D

(cid:18)(cid:90) (cid:19)(cid:90) (cid:18)(cid:90) (cid:19)(cid:90)
⊃ 2 α ∧β B ∧dB +2 α ∧β B ∧dB . (B.9)
2 2 2 4 3 1 1 5

## ∂Z 7D ∂Z 7D

Notice that each of these terms are topological as opposed to, say, terms proportional to
dA ∧ dB which depend explicitly on the 7D metric because ∗ dA = dB . Also the

## 1 4 7D 1 4

integrals over ∂Z are in fact equal to 1 mod 2 (in this normalization) as they are both valid
integral representations of the torsional pairing [108]:
L : TorH2(∂Z)×TorH3(∂Z) → Q/Z. (B.10)

## Γ

In all we have the 7D action
(cid:90)
1
×(2) (B ∧dB +B ∧dB ) , (B.11)
2 4 1 5
2π

## 7D

which can of course be presented as the circle reduction of
(cid:90)
1
×(2) (B ∧dB ) . (B.12)
2 5
2π

## 8D

As is standard for a BF-theory, because the observables of this 8D SymTFT are Z -valued,
2
we can trade off the action for Z valued potentials via 2 B = b to arrive at the action
2 2π i i
(B.2) for the e(1/4) case.
7
Toderivethe7Dcounterterm, wenowperformasimilarreductionofthe11Dkineticterm
but over Z. We first mention that, because Z has non-zero boundary, the correct pairing
44Such an approach to KK-reducing string theory p-form potentials was notably explored in [108]. See
also[52]forarelativelyrecentintroductiontousingdifferentialcohomologywhichisanalternativeapproach
to dealing with torsional cocycles.
73

<!-- Page 75 -->

to integrate forms uses Poincar´e–Lefschetz duality Hp(Z,∂Z) ≃ H (Z) which results from
5−p
the cap product with the fundamental class [Z] ∈ H (Z,∂Z):
5
∩ : H (Z,∂Z)×Hp(Z,∂Z) → H (Z). (B.13)
5 5−p
(cid:0) (cid:1) (cid:0) (cid:1)
Additionally, we have Tor H (Z,∂Z) ≃ Tor Hp+1(Z,∂Z) from the Universal Coefficient
p

### Theorem, which follows from a similar pairing

Tor (cid:0) H (Z,∂Z) (cid:1) ×Tor (cid:0) Hp+1(Z,∂Z) (cid:1) → H (Z,Q/Z) ≃ Q/Z, (B.14)
p 0
from integrating torsion cocycles over their dual cycles45. Putting these together, we have a
perfect pairing
Tor (cid:0) H5−p(Z) (cid:1) ×Tor (cid:0) Hp+1(Z,∂Z) (cid:1) → Q/Z. (B.15)
What (B.15) implies is that if we wedge a torsional (5 − p)-form of Z with a relative
torsional (p + 1)-form, we can integrate over Z. Relevant to our case is p = 3 where
(cid:0) (cid:1) (cid:0) (cid:1) (cid:0) (cid:1)
Tor H2(Z) ≃ Tor H4(Z,∂Z) ≃ Tor H (Z) are the only non-trivial torsion pieces in
1
H∗(Z) and H∗(Z,∂Z). This is precisely the case whenever D(h ) ̸= D(g(1/d)), and the

### Γ,d

arguments spelled out for e(1/4) below apply mutatis mutandis to all of them.
7
Before expanding G and G on these cocycles, we note the relation of these forms to
4 7
forms in H∗(∂Z). In particular, we have the isomorphisms which follow from the long exact
sequence of relative cohomology:
Tor (cid:0) H2(Z) (cid:1) − re − s − tr − ict − io → n Tor (cid:0) H2(∂Z) (cid:1) , (B.16)
Tor (cid:0) H3(∂Z) (cid:1) →− δ Tor (cid:0) H4(Z,∂Z) (cid:1) . (B.17)
The top line means that the class (α ,β ) generating Z = Tor (cid:0) H2(∂Z) (cid:1) can be extended to
2 1 2
the Z bulk as (α ,β(cid:101) ) which are related simply by α = α | and β = β(cid:101) | . Meanwhile
(cid:101)2 1 2 (cid:101)2 ∂Z 1 1 ∂Z
the bottom line means that (α ,β ) generating Z = Tor (cid:0) H3(∂Z) (cid:1) when extended to the Z
3 2 2
bulk as (α ,β(cid:101) ) are related to the torsion generator of H4(Z,∂Z), (α ,β(cid:101) ), as
(cid:101)3 2 (cid:101)4 3
dα = α | , dβ(cid:101) = β(cid:101) | . (B.18)
(cid:101)3 (cid:101)4 ∂Z 2 3 ∂Z
This means we can write the torsion pairing as an integral
(cid:90) (cid:90)
α ∧β(cid:101) = α ∧β(cid:101) . (B.19)
(cid:101)4 1 (cid:101)2 3

## Z Z

45TheappearanceoftheQ/Zcoefficientscanbederivedmorecarefullyusingthelongexactsequencewith
respect to the short exact sequence on the coefficients 0 → Z → Q → Q/Z → 0. See for instance [109] for
more details.
74

<!-- Page 76 -->

From the expansion (B.9) we see that we can rewrite, say the first term, as
(cid:18)(cid:90) (cid:19)(cid:90) (cid:18)(cid:90) (cid:19)(cid:90)
2 α ∧β B ∧dB = 2 α ∧β(cid:101) B ∧B , (B.20)
2 2 2 4 (cid:101)2 3 2 4

## ∂Z 7D Z 6D

by using the identities (B.18) and the fact that the 7D spacetime in the SymTFT action
in (B.9) contains the radial direction of the base of Z. Essentially we are just moving the
exterior derivative in the 7D action to the link pairing piece in a sensible fashion. Doing this
with the second term in (B.9) gives in total
(cid:90)
1

## ×(2) (B ∧B +B ∧B ) , (B.21)

2 4 1 5
2π

## 6D

which can be taken as the circle reduction of the 7D counterterm
(cid:90)
1

## ×(2) (B ∧B ) . (B.22)

2 5
2π

## 7D


### C Consistency with Resolving Singularities

In Section 4, we calculated the defect group of F-theory on a twisted circle compactification
Z ≡ (Y ×S )/Z where Y is a Kodaira singularity. We did this by calculating the groups
1 d
H (Z,∂Z)/H (Z) which by exactness is equivalent to ker(H (∂Z) → H (Z)) where the
k k k−1 k−1
map is induced from the inclusion ∂Z (cid:44)→ Z. These groups specify k-cycles in Z which
restrict in ∂Z to a non-trivial (k − 1)-cycles in ∂Z. For k = 2, this tells us physically
distinct string junctions charges in 7D since if we consider F-theory on Z × S1, and these
string junction equivalence classes are equivalently phrased in terms of M-theory on Z as M2
branes wrapped on classes of H (Z,∂Z)/H (Z) which wrap a 1-cycle in the elliptic fiber.
2 2
In this Appendix, we complement these results by computing how the homology groups
of Z change when resolving the Kodaira singularity. Namely, resolving the fiber introduces
extra P1 2-cycles in Y which thus adds 2- and 3-cycles to Z. We denote the fully resolved
manifolds as Y(cid:101) and Z(cid:101). By exactness and the fact that ∂Z = ∂Z(cid:101), we see that H (Z(cid:101),∂Z(cid:101)) will
2
gain numerous free factors from resolving, while the defect group does not change:
D(1)(Z) = H (Z(cid:101),∂Z(cid:101))/H (Z(cid:101)) = H (Z,∂Z)/H (Z). (C.1)
2 2 2 2
We will find in general that H (Z(cid:101)) is a free lattice whose rank is reduced from that of
2
H (Y(cid:101)), provided we are considering a case where ρ acts non-trivially on the elliptic fiber.
2
Conceptually, this is just due to the fact that one can only switch on hyperka¨hler parameters
of Y(cid:101) that are invariant under ρ.
Similar to Section 4, we can calculate H (Z(cid:101)) and H (Z(cid:101)) by knowing the monodromy
2 3
75

<!-- Page 77 -->

action on the k-cycles ρ : H (Y(cid:101)) → H (Y(cid:101)) and using the following short exact sequences
k k k
0 → coker(ρ −1) → H (Z(cid:101)) → 0 → 0, (C.2)
2 2
0 → 0 → H (Z(cid:101)) → ker(ρ −1) → 0. (C.3)
3 2
In (C.3), we have used the fact that H (Y(cid:101)) = 0 because Y(cid:101) is contractible to its central
3
elliptic fiber at z = 0, and in (C.2) we used ker(ρ − 1) = 0 following explicit calculations
1
in Section 4. In previous sections, ρ was simply the identity which is now no longer the
2
case in general. Since the data of ρ is unchanged after the resolution, the key quantities we
1
compute in this section are coker(ρ −1) (from which H (Z(cid:101)) follows from the calculation of
2 2
ker(ρ −1) in Section 4) and ker(ρ −1) = H (Z(cid:101)).
2 2 3
To understand the action of ρ on H (Y(cid:101)), we first recall the fact that H (Y(cid:101)) is generated
2 2 2
by cycles E , i = 0,...,rank(g) where g is the Lie algebra associated with the Kodaira
i
singularity. The elliptic fiber 2-cycle homology class [E ] away from z = 0 decomposes into
z
these P1 cycles as
rank(g)
(cid:88)

## [E ] = E . (C.4)

z i
i=0
The action of ρ on the elliptic fiber E away from z = 0 is specified by an element ρ ∈
z 1
SL(2,Z) acting on its 1-cycles, which is given in all cases of interest in Section 4.3. Note that
a common phenomenon we found across section 4.3 was that the order of ρ as an element of
1
SL(2,Z)maynotmatchtheorderofρ regardedasanautomorphismρ : D(1)(Y(cid:101)) → D(1)(Y(cid:101))
1 1
which is given in the “Outer” column of Table 7. These Z or Z actions on the resolved
2 3
central fiber of Y is then equivalent to the usual involution of an affine Dynkin diagram
associated to an outer-automorphism of a Lie algebra. These are summarized in Figure 14.
As a sanity check, we can see that these actions are consistent with the actions on
D(1)(Y(cid:101)) = H (Y(cid:101),∂Y(cid:101))/H (Y(cid:101)) as these can be regarded as fractional linear combinations of
2 2
2-cycles in H (Y(cid:101)) modulo integer 2-cycles. For example, in the case of Y being an IV
2
singularity, the generator of D(1)(Y(cid:101)) = Z can be presented as (for more general Kodaira
3
singularities see Section 3 of [39])
1
Generator of D(1)(Y(cid:101)): (E +2E ) , (C.5)
1 2
3
where E denote the exceptional cycles as in Figure 14. We see that the automorphism
i
exchanges E and E which sends the above torsional element to
1 2
1 1 1
ρ : (E +2E ) (cid:55)→ (E +2E ) ≃ − (E +2E ) (C.6)
1 2 2 1 1 2
3 3 3
where the last equation follows from adding −E − E to the LHS. Thus, we see that the
1 2
automorphism on H (Y(cid:101)) in Figure 14 induces the Z automorphism of Tor (cid:0) H (∂Y(cid:101)) (cid:1) = Z .
2 2 1 3
76

<!-- Page 78 -->

Figure 14: Z (orange) and Z (green) actions on the resolved central fiber of a Kodaira
2 3
surface Y. Physically these actions become outer automorphisms of the gauge algebra in
the singular limit. On the right column, we denote the Kodaira classification of Y and what
it would be if we were to quotient it by ρ. In terms of equation (4.50), this just means the
Kodaira type of the surface X.
We are now in a position to calculate H (Z(cid:101)) and H (Z(cid:101)) using (C.2) and (C.3) which we
2 3
handle case-by-case. In general we find that
H (Z(cid:101)) = H (Z(cid:101)) = ZR f +1. (C.7)
2 3
where R is the rank of the frozen gauge algebra listed in the “h ” column in Table 7.
f Γ,d
Physically, this is consistent with the duality (4.50) as the number of possible moduli match:
from (C.7), we have 3R +3 moduli which in terms of the frozen elliptic fibration X consists
f
of 3R Coulomb branch parameters of the frozen gauge algebra as well as the hyper-K¨ahler
f
parameters of the elliptic fiber.
D-Type Frozen Singularities Our task is to compute the kernel and cokernel of the
permutation matrix associated with the top row in Figure 14 minus the identity. For 2k = 4,
77

<!-- Page 79 -->

this is (using the ordering E , E , ..., E )
0 1 4
 
0 0 0 0 0
0 −1 0 0 1 
 
ρ −1 = 0 0 −1 1 0  , (C.8)
2  
 
0 0 1 −1 0
 
0 1 0 0 −1
which has a Smith normal form
 
1 0 0 0 0
0 1 0 0 0
 
SNF(ρ −1) = 0 0 0 0 0 . (C.9)
2  
 
0 0 0 0 0
 
0 0 0 0 0
For general 2k, the Smith normal form is
SNF(ρ −1) = diag(1k,0k+1), (C.10)
2
where superscript denotes multiplicity. This means that coker(ρ −1) = ker(ρ −1) = Zk+1
2 2
so we have
H (Z(cid:101)) = H (Z(cid:101)) = Zk+1. (C.11)
2 3
e(1/2) Frozen Singularity From the second row in Figure 14 (in orange) we have that
7
 
0 0 0 0 0
0 0 0 0 0 
 
ρ −1 = 0 0 0 0 0  , (C.12)
2  
 
0 0 0 −1 1
 
0 0 0 1 −1
 
1 0 0 0 0
0 0 0 0 0
 
SNF(ρ −1) = 0 0 0 0 0 , (C.13)
2  
 
0 0 0 0 0
 
0 0 0 0 0
which gives
H (Z(cid:101)) = H (Z(cid:101)) = Z4. (C.14)
2 3
78

<!-- Page 80 -->

e(n/d) Frozen Singularities Beginning with Z(cid:101) dual to the e(1/2) singularity, the relevant
8 8
matrices follow from the third row of Figure 14 to be
 
0 0 0 0 0 0 0
0 −1 0 0 0 1 0
 
0 0 −1 0 1 0 0
 
ρ −1 = 0 0 0 0 0 0 0 , (C.15)
2  
 
0 0 1 0 −1 0 0
 
 
0 1 0 0 0 −1 0
0 0 0 0 0 0 0
 
1 0 0 0 0 0 0
0 1 0 0 0 0 0
 
0 0 0 0 0 0 0
 
SNF(ρ −1) = 0 0 0 0 0 0 0 , (C.16)
2  
 
0 0 0 0 0 0 0
 
 
0 0 0 0 0 0 0
0 0 0 0 0 0 0
from which it follows that
H (Z(cid:101)) = H (Z(cid:101)) = Z5. (C.17)
2 3
As for e(1/3) we have (from the second row of Figure 14 in green)
8
 
0 0 0 0 0
0 −1 0 1 0 
 
ρ −1 = 0 0 0 0 0  , (C.18)
2  
 
0 0 0 −1 1
 
0 1 0 0 −1
 
1 0 0 0 0
0 1 0 0 0
 
SNF(ρ −1) = 0 0 0 0 0 , (C.19)
2  
 
0 0 0 0 0
 
0 0 0 0 0
which yields
H (Z(cid:101)) = H (Z(cid:101)) = Z3. (C.20)
2 3
Finally, the calculation of H (Z(cid:101)) and H (Z(cid:101)) in the e(1/4) case follows from the 2k = 2
2 3 8
79

<!-- Page 81 -->


### D-type example. Therefore

H (Z(cid:101)) = H (Z(cid:101)) = Z2. (C.21)
2 3
80

<!-- Page 82 -->


### References

[1] E. Witten, “Toroidal compactification without vector structure,” JHEP 02 (1998)
006, arXiv:hep-th/9712028 [hep-th].
[2] J. de Boer, R. Dijkgraaf, K. Hori, A. Keurentjes, J. Morgan, D. R. Morrison, and
S. Sethi, “Triples, fluxes, and strings,” Adv. Theor. Math. Phys. 4 (2002) 995–1186,
arXiv:hep-th/0103170.
[3] M. Atiyah and E. Witten, “M theory dynamics on a manifold of G(2) holonomy,”
Adv. Theor. Math. Phys. 6 (2003) 1–106, arXiv:hep-th/0107177.
[4] Y. Tachikawa, “Frozen singularities in M and F theory,” JHEP 06 (2016) 128,
arXiv:1508.06679 [hep-th].
[5] L. Bhardwaj, D. R. Morrison, Y. Tachikawa, and A. Tomasiello, “The frozen phase of
F-theory,” JHEP 08 (2018) 138, arXiv:1805.09070 [hep-th].
[6] B. Fraiman and H. P. de Freitas, “Freezing of gauge symmetries in the heterotic
string on T4,” JHEP 04 (2022) 007, arXiv:2111.09966 [hep-th].
[7] H. Parra De Freitas, “New supersymmetric string moduli spaces from frozen
singularities,” JHEP 01 (2023) 170, arXiv:2209.03451 [hep-th].
[8] S. Cecotti, “Hwang-Oguiso invariants and frozen singularities in special geometry,”
JHEP 04 (2024) 012, arXiv:2304.04481 [hep-th].
[9] D. R. Morrison and B. Sung, “On the frozen F-theory landscape,” JHEP 05 (2024)
126, arXiv:2310.11432 [hep-th].
[10] R. Donagi and M. Wijnholt, “The M-Theory Three-Form and Singular Geometries,”
arXiv:2310.05838 [hep-th].
[11] P.-K. Oehlmann, F. Ruehle, and B. Sung, “The frozen phase of heterotic F-theory
duality,” JHEP 07 (2024) 295, arXiv:2404.02191 [hep-th].
[12] O. Aharony, N. Seiberg, and Y. Tachikawa, “Reading between the lines of
four-dimensional gauge theories,” JHEP 08 (2013) 115, arXiv:1305.0318 [hep-th].
[13] D. Gaiotto, A. Kapustin, N. Seiberg, and B. Willett, “Generalized Global
Symmetries,” JHEP 02 (2015) 172, arXiv:1412.5148 [hep-th].
[14] C. Cordova, T. T. Dumitrescu, K. Intriligator, and S.-H. Shao, “Snowmass White
Paper: Generalized Symmetries in Quantum Field Theory and Beyond,” in
Snowmass 2021. 5, 2022. arXiv:2205.09545 [hep-th].
81

<!-- Page 83 -->

[15] S. Schafer-Nameki, “ICTP lectures on (non-)invertible generalized symmetries,”
Phys. Rept. 1063 (2024) 1–55, arXiv:2305.18296 [hep-th].
[16] L. Bhardwaj, L. E. Bottini, L. Fraser-Taliente, L. Gladden, D. S. W. Gould,
A. Platschorre, and H. Tillim, “Lectures on generalized symmetries,” Phys. Rept.
1051 (2024) 1–87, arXiv:2307.07547 [hep-th].
[17] R. Luo, Q.-R. Wang, and Y.-N. Wang, “Lecture notes on generalized symmetries and
applications,” Phys. Rept. 1065 (2024) 1–43, arXiv:2307.09215 [hep-th].
[18] S.-H. Shao, “What’s Done Cannot Be Undone: TASI Lectures on Non-Invertible
Symmetry,” arXiv:2308.00747 [hep-th].
[19] M. Del Zotto, J. J. Heckman, D. S. Park, and T. Rudelius, “On the Defect Group of
a 6D SCFT,” Lett. Math. Phys. 106 no. 6, (2016) 765–786, arXiv:1503.04806
[hep-th].
[20] I. Garc´ıa Etxebarria, B. Heidenreich, and D. Regalado, “IIB flux non-commutativity
and the global structure of field theories,” JHEP 10 (2019) 169, arXiv:1908.08027
[hep-th].
[21] D. R. Morrison, S. Schafer-Nameki, and B. Willett, “Higher-Form Symmetries in 5d,”
JHEP 09 (2020) 024, arXiv:2005.12296 [hep-th].
[22] F. Albertini, M. Del Zotto, I. Garc´ıa Etxebarria, and S. S. Hosseini, “Higher Form
Symmetries and M-theory,” JHEP 12 (2020) 203, arXiv:2005.12831 [hep-th].
[23] I. Bah, F. Bonetti, and R. Minasian, “Discrete and higher-form symmetries in SCFTs
from wrapped M5-branes,” JHEP 03 (2021) 196, arXiv:2007.15003 [hep-th].
[24] M. Del Zotto, I. Garcia Etxebarria, and S. S. Hosseini, “Higher form symmetries of
Argyres-Douglas theories,” JHEP 10 (2020) 056, arXiv:2007.15603 [hep-th].
[25] F. Apruzzi, M. Dierigl, and L. Lin, “The Fate of Discrete 1-Form Symmetries in 6d,”
SciPost Phys. 12 (2022) 047, arXiv:2008.09117 [hep-th].
[26] L. Bhardwaj and S. Scha¨fer-Nameki, “Higher-form symmetries of 6d and 5d
theories,” JHEP 02 (2021) 159, arXiv:2008.09600 [hep-th].
[27] M. Cvetiˇc, M. Dierigl, L. Lin, and H. Y. Zhang, “String Universality and
Non-Simply-Connected Gauge Groups in 8d,” Phys. Rev. Lett. 125 no. 21, (2020)
211602, arXiv:2008.10605 [hep-th].
[28] M. Del Zotto and K. Ohmori, “2-Group Symmetries of 6D Little String Theories and
T-Duality,” Annales Henri Poincare 22 no. 7, (2021) 2451–2474, arXiv:2009.03489
[hep-th].
82

<!-- Page 84 -->

[29] L. Bhardwaj, M. Hubner, and S. Schafer-Nameki, “1-form Symmetries of 4d N=2
Class S Theories,” arXiv:2102.01693 [hep-th].
[30] F. Apruzzi, L. Bhardwaj, J. Oh, and S. Schafer-Nameki, “The Global Form of Flavor
Symmetries and 2-Group Symmetries in 5d SCFTs,” arXiv:2105.08724 [hep-th].
[31] M. Cvetiˇc, M. Dierigl, L. Lin, and H. Y. Zhang, “Higher-form symmetries and their
anomalies in M-/F-theory duality,” Phys. Rev. D 104 no. 12, (2021) 126019,
arXiv:2106.07654 [hep-th].
[32] A. P. Braun, M. Larfors, and P.-K. Oehlmann, “Gauged 2-form symmetries in 6D
SCFTs coupled to gravity,” JHEP 12 (2021) 132, arXiv:2106.13198 [hep-th].
[33] L. Bhardwaj, “2-Group symmetries in class S,” SciPost Phys. 12 no. 5, (2022) 152,
arXiv:2107.06816 [hep-th].
[34] J. Tian and Y.-N. Wang, “5D and 6D SCFTs from C3 orbifolds,” SciPost Phys. 12
no. 4, (2022) 127, arXiv:2110.15129 [hep-th].
[35] L. Bhardwaj, S. Giacomelli, M. Hu¨bner, and S. Sch¨afer-Nameki, “Relative Defects in
Relative Theories: Trapped Higher-Form Symmetries and Irregular Punctures in
Class S,” arXiv:2201.00018 [hep-th].
[36] M. Del Zotto, J. J. Heckman, S. N. Meynet, R. Moscrop, and H. Y. Zhang, “Higher
symmetries of 5D orbifold SCFTs,” Phys. Rev. D 106 no. 4, (2022) 046010,
arXiv:2201.08372 [hep-th].
[37] M. Cvetiˇc, J. J. Heckman, M. Hu¨bner, and E. Torres, “0-form, 1-form, and 2-group
symmetries via cutting and gluing of orbifolds,” Phys. Rev. D 106 no. 10, (2022)
106003, arXiv:2203.10102 [hep-th].
[38] M. Del Zotto, I. Garc´ıa Etxebarria, and S. Schafer-Nameki, “2-Group Symmetries
and M-Theory,” SciPost Phys. 13 (2022) 105, arXiv:2203.10097 [hep-th].
[39] M. Hubner, D. R. Morrison, S. Schafer-Nameki, and Y.-N. Wang, “Generalized
Symmetries in F-theory and the Topology of Elliptic Fibrations,” SciPost Phys. 13
no. 2, (2022) 030, arXiv:2203.10022 [hep-th].
[40] V. Bashmakov, M. Del Zotto, and A. Hasan, “On the 6d origin of non-invertible
symmetries in 4d,” JHEP 09 (2023) 161, arXiv:2206.07073 [hep-th].
[41] M. van Beest, D. S. W. Gould, S. Schafer-Nameki, and Y.-N. Wang, “Symmetry
TFTs for 3d QFTs from M-theory,” JHEP 02 (2023) 226, arXiv:2210.03703
[hep-th].
83

<!-- Page 85 -->

[42] V. Bashmakov, M. Del Zotto, A. Hasan, and J. Kaidi, “Non-invertible symmetries of
class S theories,” JHEP 05 (2023) 225, arXiv:2211.05138 [hep-th].
[43] B. S. Acharya, M. Del Zotto, J. J. Heckman, M. Hubner, and E. Torres, “Junctions,
Edge Modes, and G -Holonomy Orbifolds,” arXiv:2304.03300 [hep-th].
2
[44] M. Dierigl, J. J. Heckman, M. Montero, and E. Torres, “R7-branes as charge
conjugation operators,” Phys. Rev. D 109 no. 4, (2024) 046004, arXiv:2305.05689
[hep-th].
[45] M. Cvetiˇc, J. J. Heckman, M. Hu¨bner, and E. Torres, “Fluxbranes, generalized
symmetries, and Verlinde’s metastable monopole,” Phys. Rev. D 109 no. 4, (2024)
046007, arXiv:2305.09665 [hep-th].
[46] V. Bashmakov, M. Del Zotto, and A. Hasan, “Four-manifolds and Symmetry
Categories of 2d CFTs,” arXiv:2305.10422 [hep-th].
[47] F. Apruzzi, F. Bonetti, D. S. W. Gould, and S. Schafer-Nameki, “Aspects of
categorical symmetries from branes: SymTFTs and generalized charges,” SciPost
Phys. 17 no. 1, (2024) 025, arXiv:2306.16405 [hep-th].
[48] C. Closset and H. Magureanu, “Reading between the rational sections: Global
structures of 4d N = 2 KK theories,” SciPost Phys. 16 no. 5, (2024) 137,
arXiv:2308.10225 [hep-th].
[49] J. J. Heckman, M. Hubner, E. Torres, X. Yu, and H. Y. Zhang, “Top down approach
to topological duality defects,” Phys. Rev. D 108 no. 4, (2023) 046015,
arXiv:2212.09743 [hep-th].
[50] H. Y. Zhang, “K-theoretic Global Symmetry in String-constructed QFT and
T-duality,” arXiv:2404.16097 [hep-th].
[51] E. Torres, “Giving a KO to 8D Gauge Anomalies,” arXiv:2405.08809 [hep-th].
[52] F. Apruzzi, F. Bonetti, I. Garc´ıa Etxebarria, S. S. Hosseini, and S. Schafer-Nameki,
“Symmetry TFTs from String Theory,” Commun. Math. Phys. 402 no. 1, (2023)
895–949, arXiv:2112.02092 [hep-th].
[53] F. Apruzzi, I. Bah, F. Bonetti, and S. Schafer-Nameki, “Noninvertible Symmetries
from Holography and Branes,” Phys. Rev. Lett. 130 no. 12, (2023) 121601,
arXiv:2208.07373 [hep-th].
[54] I. Garc´ıa Etxebarria, “Branes and Non-Invertible Symmetries,” Fortsch. Phys. 70
no. 11, (2022) 2200154, arXiv:2208.07508 [hep-th].
84

<!-- Page 86 -->

[55] J. J. Heckman, M. Hu¨bner, E. Torres, and H. Y. Zhang, “The Branes Behind
Generalized Symmetry Operators,” Fortsch. Phys. 71 no. 1, (2023) 2200180,
arXiv:2209.03343 [hep-th].
[56] D. S. Freed and C. Teleman, “Relative quantum field theory,” Commun. Math. Phys.
326 (2014) 459–476, arXiv:1212.1692 [hep-th].
[57] D. S. Freed, G. W. Moore, and C. Teleman, “Topological symmetry in quantum field
theory,” arXiv:2209.07471 [hep-th].
[58] E. Witten, “AdS / CFT correspondence and topological field theory,” JHEP 12
(1998) 012, arXiv:hep-th/9812012.
[59] D. M. Belov and G. W. Moore, “Type II Actions from 11-Dimensional Chern-Simons
Theories,” arXiv:hep-th/0611020.
[60] S. Gukov, P.-S. Hsin, and D. Pei, “Generalized Global Symmetries of T[M] Theories.
I,” arXiv:2010.15890 [hep-th].
[61] F. Apruzzi, “Higher Form Symmetries TFT in 6d,” arXiv:2203.10063 [hep-th].
[62] O. Bergman and S. Hirano, “The holography of duality in N = 4 Super-Yang-Mills
theory,” JHEP 11 (2022) 069, arXiv:2208.09396 [hep-th].
[63] C. Lawrie, X. Yu, and H. Y. Zhang, “Intermediate defect groups, polarization pairs,
and noninvertible duality defects,” Phys. Rev. D 109 no. 2, (2024) 026005,
arXiv:2306.11783 [hep-th].
[64] M. Cvetiˇc, J. J. Heckman, M. Hu¨bner, and E. Torres, “Generalized symmetries,
gravity, and the swampland,” Phys. Rev. D 109 no. 2, (2024) 026012,
arXiv:2307.13027 [hep-th].
[65] F. Baume, J. J. Heckman, M. Hu¨bner, E. Torres, A. P. Turner, and X. Yu,
“SymTrees and Multi-Sector QFTs,” Phys. Rev. D 109 no. 10, (2024) 106013,
arXiv:2310.12980 [hep-th].
[66] X. Yu, “Noninvertible symmetries in 2D from type IIB string theory,” Phys. Rev. D
110 no. 6, (2024) 065008, arXiv:2310.15339 [hep-th].
[67] D. S. W. Gould, L. Lin, and E. Sabag, “Swampland constraints on the SymTFT of
supergravity,” Phys. Rev. D 109 no. 12, (2024) 126005, arXiv:2312.02131
[hep-th].
[68] J. J. Heckman, M. Hu¨bner, and C. Murdia, “On the holographic dual of a topological
symmetry operator,” Phys. Rev. D 110 no. 4, (2024) 046007, arXiv:2401.09538
[hep-th].
85

<!-- Page 87 -->

[69] N. Braeger, V. Chakrabhavi, J. J. Heckman, and M. Hubner, “Generalized
Symmetries of Non-Supersymmetric Orbifolds,” arXiv:2404.17639 [hep-th].
[70] M. Cvetiˇc, R. Donagi, J. J. Heckman, M. Hu¨bner, and E. Torres, “Cornering Relative
Symmetry Theories,” arXiv:2408.12600 [hep-th].
[71] F. Apruzzi, F. Bedogna, and N. Dondi, “SymTh for non-finite symmetries,”
arXiv:2402.14813 [hep-th].
[72] I. Garc´ıa Etxebarria and S. S. Hosseini, “Some aspects of symmetry descent,”
arXiv:2404.16028 [hep-th].
[73] J. J. Heckman and M. Hu¨bner, “Celestial Topology, Symmetry Theories, and
Evidence for a Non-SUSY D3-Brane CFT,” arXiv:2406.08485 [hep-th].
[74] M. Cvetiˇc, M. Dierigl, L. Lin, and H. Y. Zhang, “All eight- and nine-dimensional
string vacua from junctions,” Phys. Rev. D 106 no. 2, (2022) 026007,
arXiv:2203.03644 [hep-th].
[75] A. Font, B. Fraiman, M. Gran˜a, C. A. Nu´n˜ez, and H. Parra De Freitas, “Exploring
the landscape of CHL strings on Td,” JHEP 08 (2021) 095, arXiv:2104.07131
[hep-th].
[76] M. Cvetiˇc, M. Dierigl, L. Lin, and H. Y. Zhang, “Gauge group topology of 8D
Chaudhuri-Hockney-Lykken vacua,” Phys. Rev. D 104 no. 8, (2021) 086018,
arXiv:2107.04031 [hep-th].
[77] B. Fraiman and H. P. De Freitas, “Symmetry enhancements in 7d heterotic strings,”
JHEP 10 (2021) 002, arXiv:2106.08189 [hep-th].
[78] B. Fraiman and H. Parra De Freitas, “Unifying the 6D N = (1, 1) string landscape,”
JHEP 02 (2023) 204, arXiv:2209.06214 [hep-th].
[79] Y. Tachikawa, “On fractional M5 branes and frozen singularities,” 2015.
https://member.ipmu.jp/yuji.tachikawa/transp/kiastalk.pdf.
[80] E. Witten, “On flux quantization in M theory and the effective action,” J. Geom.
Phys. 22 (1997) 1–13, arXiv:hep-th/9609122.
[81] K. Ohmori, H. Shimizu, Y. Tachikawa, and K. Yonekura, “Anomaly polynomial of
general 6d SCFTs,” PTEP 2014 no. 10, (2014) 103B07, arXiv:1408.5572
[hep-th].
[82] J. Fuchs and C. Schweigert, Symmetries, Lie algebras and representations: A
graduate course for physicists. Cambridge University Press, 10, 2003.
86

<!-- Page 88 -->

[83] A. Borel, R. Friedman, and J. W. Morgan, “Almost commuting elements in compact
Lie groups,” arXiv:math/9907007.
[84] C. Meyers, M. De Roo, and P. Sorba, “GROUP THEORETICAL ASPECTS OF
INSTANTONS,” Nuovo Cim. A 52 (1979) 519–530.
[85] M. Del Zotto, J. J. Heckman, A. Tomasiello, and C. Vafa, “6d Conformal Matter,”
JHEP 02 (2015) 054, arXiv:1407.6359 [hep-th].
[86] A. Hanany and E. Witten, “Type IIB superstrings, BPS monopoles, and
three-dimensional gauge dynamics,” Nucl. Phys. B 492 (1997) 152–190,
arXiv:hep-th/9611230.
[87] M. Esole and M. J. Kang, “Matter representations from geometry: under the spell of
Dynkin,” arXiv:2012.13401 [hep-th].
[88] N. Yamatsu, “Finite-Dimensional Lie Algebras and Their Representations for Unified
Model Building,” arXiv:1511.08771 [hep-ph].
[89] M. R. Douglas and G. W. Moore, “D-branes, quivers, and ALE instantons,”
arXiv:hep-th/9603167.
[90] C. V. Johnson and R. C. Myers, “Aspects of type IIB theory on ALE spaces,” Phys.
Rev. D 55 (1997) 6382–6393, arXiv:hep-th/9610140.
[91] D. J. Gross and N. A. Nekrasov, “Monopoles and strings in noncommutative gauge
theory,” JHEP 07 (2000) 034, arXiv:hep-th/0005204.
[92] M. R. Douglas, “Branes within branes,” NATO Sci. Ser. C 520 (1999) 267–275,
arXiv:hep-th/9512077.
[93] P. S. Aspinwall and M. R. Plesser, “D-branes, discrete torsion and the McKay
correspondence,” JHEP 02 (2001) 009, arXiv:hep-th/0009042.
[94] T. Weigand, “F-theory,” PoS TASI2017 (2018) 016, arXiv:1806.01854 [hep-th].
[95] M. Cvetiˇc and L. Lin, “TASI Lectures on Abelian and Discrete Symmetries in
F-theory,” PoS TASI2017 (2018) 020, arXiv:1809.00012 [hep-th].
[96] W. Nahm and K. Wendland, “Mirror symmetry on Kummer type K3 surfaces,”
Commun. Math. Phys. 243 (2003) 557–582, arXiv:hep-th/0106104.
[97] M. Cvetiˇc, J. J. Heckman, E. Torres, and G. Zoccarato, “Reflections on the matter of
3D N=1 vacua and local Spin(7) compactifications,” Phys. Rev. D 105 no. 2, (2022)
026008, arXiv:2107.00025 [hep-th].
87

<!-- Page 89 -->

[98] J. J. Heckman and L. Tizzano, “6D Fractional Quantum Hall Effect,” JHEP 05
(2018) 120, arXiv:1708.02250 [hep-th].
[99] A. Kapustin and N. Seiberg, “Coupling a QFT to a TQFT and Duality,” JHEP 04
(2014) 001, arXiv:1401.0740 [hep-th].
[100] A. Fujiki, “Finite automorphism groups of complex tori of dimension two,”
Publications of the Research Institute for Mathematical Sciences 24 no. 1, (1988)
1–97.
[101] J. Polchinski, “Monopoles, duality, and string theory,” Int. J. Mod. Phys. A 19S1
(2004) 145–156, arXiv:hep-th/0304042.
[102] B. Heidenreich, J. McNamara, M. Montero, M. Reece, T. Rudelius, and
I. Valenzuela, “Non-invertible global symmetries and completeness of the spectrum,”
JHEP 09 (2021) 203, arXiv:2104.07036 [hep-th].
[103] C. Vafa and E. Witten, “On orbifolds with discrete torsion,” J. Geom. Phys. 15
(1995) 189–214, arXiv:hep-th/9409188.
[104] Z. K. Baykara, Y. Hamada, H.-C. Tarazi, and C. Vafa, “On the string landscape
without hypermultiplets,” JHEP 04 (2024) 121, arXiv:2309.15152 [hep-th].
[105] Z. K. Baykara, H.-C. Tarazi, and C. Vafa, “The Quasicrystalline String Landscape,”
arXiv:2406.00129 [hep-th].
[106] A. Dabholkar and J. A. Harvey, “String islands,” JHEP 02 (1999) 006,
arXiv:hep-th/9809122.
[107] E. Witten, “New ’gauge’ theories in six-dimensions,” JHEP 01 (1998) 001,
arXiv:hep-th/9710065.
[108] P. G. Camara, L. E. Ibanez, and F. Marchesano, “RR photons,” JHEP 09 (2011)
110, arXiv:1106.0060 [hep-th].
[109] T. M. A. Project. http://www.map.mpim-bonn.mpg.de/Linking_form.
88

## Tables

**Table (Page 16):**

| Frozen Singularity | Frozen Algebra | Frozen Root System |
|---|---|---|
| D(1/2) 5 | sp(1) | β = α +α +2α 0 0 1 2 β = 2α +α +α 1 3 4 5 |
| D(1/2) (k > 1) 4+k | sp(k) | β = α +α +2α 0 0 1 2 β = α (1 ≤ i ≤ k −1) i i+2 β = 2α +α +α k k+2 k+3 k+4 |
| e(1/2) 6 | su(3) | β = α +α +2α 0 0 3 6 β = α +2α +α 1 1 2 3 β = α +2α +α 2 3 4 5 |
| e(1/2) 7 | so(7) | β = α +2α +α 0 0 1 2 β = α +2α +α 1 4 5 6 β = α +2α +α 2 2 3 4 β = α 3 7 |
| e(1/3) 7 | su(2) | β = α +2α +3α +2α +α 0 0 1 2 3 7 β = α +2α +3α +2α +α 1 7 3 4 5 6 |
| e(1/2) 8 | f 4 | β = α +2α +α 0 0 1 2 β = α +2α +α 1 2 3 4 β = α +2α +α 2 4 5 8 β = α 3 6 β = α 4 7 |
| e(1/3) 8 | g 2 | β = α +2α +3α +2α +α 0 0 1 2 3 4 β = α +2α +3α +2α +α 1 3 4 5 6 7 β = α 2 8 |
| e(1/4) 8 | su(2) | β = α +2α +3α +4α +2α 0 0 1 2 3 4 β = 2×(α +2α +2α +α +α ) 1 4 5 6 7 8 |


**Table (Page 21):**

| Frozen Singularity | Relevant Maximal S-Subalgebras |
|---|---|
| D(1/2) 4 e(n/d) 6 e(n/d) 7 e(n/d) 8 | so(7)[1], so(5)[1], su(2)[2] sp(4)[1], f[1], su(3)[2] ⊕g[1] 4 2 su(2)[3] ⊕f[1], sp(3)[1] ⊕g[1], su(2)[7] ⊕g[1] 4 2 2 f[1] ⊕g[1] 4 2 |


**Table (Page 25):**

| Z k |
|---|
| Z ×Z 2 2 |
| Z ×Z 2 2 |
| Z 4 |
| Z 3 |
| Z 2 |


**Table (Page 26):**

| 0 | Z2 2 | Z2 2 |
|---|---|---|
| Z 2 | Z2 2 | Z2 2 |
| Z 2 | Z 4 | Z 4 |
| Z 3 | Z 3 | Z 3 |
| 0 | Z 3 | Z 3 |
| Z 2 | Z 2 | Z 2 |
| 0 | Z 2 | Z 2 |


**Table (Page 36):**

| I 2k | I∗ k | Z 2 | (cid:18) (cid:19) −1 −k 0 −1 | Z 2 | su(2k) |
|---|---|---|---|---|---|
| IV | IV∗ | Z 2 | (cid:18) (cid:19) −1 −1 1 0 | ∅ | su(3) |
| I 0 | IV∗ | Z 3 | (cid:18) (cid:19) −1 −1 1 0 | ∅ | ∅ |
| I∗ 0 | III∗ | Z 2 | (cid:18) (cid:19) 0 −1 1 0 | Z 2 | so(8) |
| III | III∗ | Z 3 | (cid:18) (cid:19) 0 −1 1 0 | ∅ | su(2) |
| I 0 | III∗ | Z 4 | (cid:18) (cid:19) 0 −1 1 0 | ∅ | ∅ |
| IV∗ | II∗ | Z 2 | (cid:18) (cid:19) 0 −1 1 1 | Z 2 | e 6 |
| I∗ 0 | II∗ | Z 3 | (cid:18) (cid:19) 0 −1 1 1 | Z 3 | so(8) |
| IV | II∗ | Z 4 | (cid:18) (cid:19) 0 −1 1 1 | Z 2 | su(3) |
| II | II∗ | Z 5 | (cid:18) (cid:19) 0 −1 1 1 | ∅ | ∅ |


**Table (Page 56):**

| Γ | Z(G ) = H (S3/Γ) Γ 1 | L Γ |
|---|---|---|
| Z k | Z k | 1/k |
| D 2k | Z ×Z 2 2 | (cid:32) (cid:33) k k −1 1 2 k −1 k |
| D 2k+1 | Z 4 | 2k−1 4 |
| Γ E6 | Z 3 | −1/3 |
| Γ E7 | Z 2 | 1/2 |
| Γ E8 | ∅ | 0 |


**Table (Page 65):**

| X | ADE Singularities | Frozen Singularity Configuration(s) |
|---|---|---|
| T4/D 4 | D2 ⊕A3 ⊕A2 4 3 1 | D(1/2) ⊕D(1/2) ⊕A3 ⊕A2 4 4 3 1 |
| T4/D′ 4 | D4 ⊕A3 4 1 | D(1/2) ⊕D(1/2) ⊕D2 ⊕A3 4 4 4 1 (cid:16) (cid:17)4 D(1/2) ⊕A3 4 1 |
| T4/D′′ 4 | A6 ⊕A 3 1 | None |
| T4/D 5 | D ⊕A3 ⊕A2 ⊕A 5 3 2 1 | None |
| T4/Γ E6 | e ⊕D ⊕A4 ⊕A 6 4 2 1 | e(1/2) ⊕D(1/2) ⊕A4 ⊕A 6 4 2 1 |
| T4/Γ′ E6 | A ⊕A2 ⊕A4 5 3 2 | None |


**Table (Page 78):**

|  |  |
|---|---|
|  |  |
|  |  |
|  |  |
