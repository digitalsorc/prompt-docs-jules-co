---
title: "GraphRAG Knowledge Graphs"
original_file: "./GraphRAG_Knowledge_Graphs.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag", "agents", "evaluation"]
keywords: ["cid", "then", "critical", "each", "proof", "since", "there", "page", "lemma", "solutions"]
summary: "<!-- Page 1 -->

Compactness via monotonicity in nonsmooth critical point theory, with
application to Born-Infeld type equations
Jaeyoung Byeon Norihisa Ikoma Andrea Malchiodi Luciano Mari

### October 10, 2024


### DepartmentofMathematicalSciences,KAIST,

291Daehak-ro,Yuseong-gu,Daejeon305-701,RepublicofKorea

### E-mail: byeon@kaist.ac.kr

DepartmentofMathematics,FacultyofScienceandTechnology,KeioUniversity,
YagamiCampus: 3-14-1Hiyoshi,Kohoku-ku,Yokohama,Kanagawa2238522,Japan
E-mail: ikoma@ma"
related_documents: []
---

# GraphRAG Knowledge Graphs

<!-- Page 1 -->

Compactness via monotonicity in nonsmooth critical point theory, with
application to Born-Infeld type equations
Jaeyoung Byeon Norihisa Ikoma Andrea Malchiodi Luciano Mari

### October 10, 2024


### DepartmentofMathematicalSciences,KAIST,

291Daehak-ro,Yuseong-gu,Daejeon305-701,RepublicofKorea

### E-mail: byeon@kaist.ac.kr

DepartmentofMathematics,FacultyofScienceandTechnology,KeioUniversity,
YagamiCampus: 3-14-1Hiyoshi,Kohoku-ku,Yokohama,Kanagawa2238522,Japan
E-mail: ikoma@math.keio.ac.jp

### ScuolaNormaleSuperiore,

PiazzadeiCavalieri,7,56126Pisa,Italy

### E-mail: andrea.malchiodi@sns.it

DipartimentodiMatematica,Universita`degliStudidiMilano,
ViaSaldini50,20123Milano,Italy
E-mail: luciano.mari@unimi.it

### Abstract

In this paper, we prove new existence and multiplicity results for critical points of lower semicontinuous functionals in Banach spaces, complementing the nonsmooth critical point theory set forth by
Szulkin and avoiding the need of the Palais–Smale condition. We apply our abstract results to get
entire solutions with finite energy to Born-Infeld type autonomous equations. More precisely, under
almost optimal conditions on the nonlinearity, we construct a positive solution and infinitely many
solutions both in the classes of radially symmetric functions and nonradiallly symmetric ones.

## Msc2020: 35A15; 58E05; 58E35; 35B38; 35J62.

Keywords: Nonsmooth critical point theory; Monotonicity trick; critical points; Born–Infeld equations;
Existence and nonexistence of solutions.

### Contents

1 Introduction and main abstract results 2
1.1 Previous related works and novelties of our approach . . . . . . . . . . . . . . . . . . . . . 5
2 Application to the Born-Infeld equation 6
2.1 Critical points of I and weak solutions to (BI ) . . . . . . . . . . . . . . . . . . . . . . . . 10
f
2.2 Proofs of Propositions 2.6 and 2.7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3 Proof of Theorem 2.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3 Deformation lemmas 24
3.1 The Deformation Lemma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.2 Symmetric Deformation Lemma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
1

<!-- Page 2 -->

4 Proof of Theorem 1.6 and Theorem 1.7 36

### A The principle of symmetric criticality 51

B Regularity for the Born-Infeld solution 53
1 Introduction and main abstract results
Let (X,∥·∥) be a Banach space and consider functionals of the type

### I : X → (−∞,∞], I(u) ≡ Ψ(u)−Φ(u),

where we assume that Ψ and Φ satisfy the following properties:
(Ψ ) Ψ : X → [0,∞] is lower semicontinuous and convex, and Ψ(0) = 0;
1

## (Φ ) Φ ∈ C1(X,R).

1

### We denote

D(Ψ) ≡ {u ∈ X | Ψ(u) < ∞}.
This kind of functionals arises, for instance, in some problems involving PDEs with contraints for admissible functions. A typical example we are interested in is the following:
(cid:90)
(cid:112)
 1− 1−|Du|2 if ∥Du∥ ≤ 1, (cid:90)
∞
Ψ(u) ≡ Rn Φ(u) ≡ F(u),
∞ otherwise, Rn
which comes from the prescribed mean curvature problem for space-like hypersurfaces in the Lorentz-
Minkowski space
n
(cid:88)
Ln+1 ≡ R×Rn with metric −dx2+ dx2.
0 j
j=1
In Lorentzian geometry, space-like hypersurfaces with prescribed mean curvature play a major role highlighted, for instance, in Marsden & Tipler [47]. A space-like hypersurface whose mean curvature is a
given function f : Ln+1 → R is described, at least locally, by the graph x = u(x ,...,x ) of a solution
0 1 n
u : Ω → R to
(cid:32) (cid:33)

### Du

div +f(x,u) = 0 in Ω ⊂ Rn. (1)
(cid:112)
1−|Du|2
Formally, (1) is the Euler-Lagrange equation of the action
(cid:90) (cid:90) (cid:90) s
(cid:112)
I(u) ≡ 1− 1−|Du|2− F(x,u), F(x,s) ≡ f(x,t)dt,

## Ω Ω 0

which is non-smooth where |Du| = 1 (in the terminology of [47], where the graph of u goes null).
Therefore, even assuming that critical points of I (in a non-smooth sense) exist, they may not correspond
to solutions to (1), a fact that makes the existence problem quite challenging.
Equation (1) also appears in the framework of the Born-Infeld theory for electromagnetism [18],
according to which the identity describes the interplay between an electrostatic potential u and the
charge density it generates, required, in this specific example, to be f(x,u). If f is independent of u,
includingthecaseoff amereRadonmeasure,inrecentyearsafewauthorsinvestigatedtheexistenceand
regularity properties of solutions to (1). The resulting picture is still fragmentary, and many interesting
2

<!-- Page 3 -->

open problems are yet to be solved, see [15,17,22]. We stress that the Born-Infeld Lagrangian also
appears in other branches of theoretical physics. For more details we recommend the survey [65] and the
references therein.
In a pioneering paper, Bartnik & Simon [9] studied the Dirichlet problem for (1) in bounded domains
withboundarydataφ ∈ C(∂Ω)satisfyingaverymildspace-likecondition, andprovedageneralexistence
theorem when f ∈ C(Ω × R). A candidate solution is produced by minimizing I, in their setting a
consequenceofthedirectmethod. Acorepartoftheirworkistoshowthattheminimizeruactuallysolves
(1) and enjoys nice regularity properties. Remarkably, this is achieved with no regularity requirement on
∂Ω. Uniqueness of solutions holds if f(x,s) is non-increasing in s (since I becomes strictly convex), but
may fail otherwise. Indeed, under suitable conditions on f, for φ = 0 Bereanu, Jebelean & Mawhin [10]
obtained a second solution of mountain pass type to (1). To reach the goal, they exploited a general
nonsmoothcriticalpointtheorydevelopedbySzulkin[63]. HeretheboundednessofΩimpliestheuniform
boundedness in C(Ω) of any admissible function u with ∥Du∥ ≤ 1 attaining the boundary value, an
∞
essential fact to guarantee the validity of the Palais-Smale condition. Szulkin’s nonsmooth critical point
theoryisquiteversatile,andappliestovariousproblemsthatdonotallowforatreatmentviatheclassical
theory by Ambrosetti and Rabinowitz [2].
Our starting point for the present work was the search for solutions to (1) in the autonomous case on
the entire Rn:
(cid:32) (cid:33)

### Du

div +f(u) = 0 in Rn. (BI )
(cid:112) f
1−|Du|2
We focus on solutions u vanishing at infinity. The problem was already considered in the literature, see
below for more details. In this setting, as we shall see, Szulkin’s theory is not sufficient anymore. Seeking
for existence results tailored to (BI ) led us to complement Szulkin’s theory in its general framework.
f
Our goal is to prove two existence theorems for minimax critical points of I, valid under fairly general
conditions for Ψ and Φ that are suited to applications and might be somehow optimal. Differently from
[63], we only require a form of bounded Palais-Smale condition. To find bounded Palais-Smale sequences
(and then, critical points of I), our approach is based on the monotonicity trick due to Struwe [57],
Jeanjean & Toland [38,41], a tool widely used in the literature, see for instance [42]. We adapt the trick
to the family of functionals
I : X → R, I (u) ≡ λΨ(u)−Φ(u)
λ λ
for λ ∈ R+. However, to make it effective for the applications we are considering, the adaptation is far
from trivial. See below for more explanations.

### Following Szulkin [63], we set

Definition 1.1. Let X be a Banach space and I = λΨ−Φ, with Ψ,Φ satisfying (Ψ ),(Φ ) and λ ∈ R+.
λ 1 1
• An element u ∈ X is called a critical point of I if
λ
λ(Ψ(v)−Ψ(u))−Φ′(u)(v−u) ≥ 0 for all v ∈ X. (2)
• A sequence {u }∞ ⊂ X is called a Palais-Smale sequence for I at level c ∈ R if
j j=1 λ
(i) I (u ) → c as j → ∞,
λ j
(ii) there exists {ε }∞ ⊂ R+ with ε → 0 as j → ∞ such that
j j=1 j
λ(Ψ(v)−Ψ(u ))−Φ′(u )(v−u ) ≥ −ε ∥v−u ∥ for all v ∈ X. (3)
j j j j j
Remark 1.2. By choosing v ∈ D(Ψ), notice that any critical point of I belongs to D(Ψ). Also, it is
λ
easy to see that if u ∈ D(Ψ) is a critical point of I and Ψ is differentiable at u, then u is a classical
λ
critical point ofI that is, λΨ′(u)−Φ′(u) = 0.More generally, (2) can be rephrased asλ−1Φ′(u) ∈ ∂Ψ(u),
λ
where ∂Ψ(u) denotes the subdifferential of Ψ at u.
3

<!-- Page 4 -->

To state our results, we need some further conditions on Ψ and Φ.
(Ψ ) Ψ(u) → ∞ as ∥u∥ → ∞.
2
(Ψ ) If{u }∞ ⊂ D(Ψ)andu ∈ D(Ψ)satisfyu ⇀ uweaklyinX andΨ(u ) → Ψ(u),then∥u −u∥ → 0.
3 j j=1 j j j
(Φ ) Any bounded sequence {u } in X has a weakly convergent subsequence {u } to u in X such that
2 l l lj j
liminfΦ′(u )(v−u ) ≥ Φ′(u)(v−u) for any v ∈ X.
j→∞
lj lj
(IB) For any 0 < a ≤ b < ∞ and c ∈ R,
Kc ≡ {u ∈ X | for some λ ∈ [a,b],u is a critical point of I with I (u) ≤ c}
[a,b] λ λ
is bounded in X.
Remark 1.3. Observe that (Φ ) is satisfied if X is reflexive and Φ′ : X → X∗ is compact; in this case,
2
the liminf can be replaced by a limit, and equality holds. Notice however that (Φ ) is a strictly weaker
2
condition: for instance, (Φ ) holds if X is a Hilbert space and Φ(u) = −∥u∥2. This improvement will be
2
useful in our application to the Born-Infeld equation.
Remark 1.4. AsweshallseeinProposition4.1,properties(Ψ )and(Φ )areassumedsothatI satisfies
3 2 λ
a bounded Palais-Smale condition in a strengthened form, namely including a dependence on λ.
Remark 1.5. We assume (IB) as a replacement for the boundedness of Palais-Smale sequences, a condition which may fail for general I. For large classes of interesting functionals arising from nonlinear
elliptic problems, (IB) may be proved via Pohozaev type identities.
Our main achievements are the following minimax theorems. We first suppose that I has a uniform
λ
mountain pass geometry for λ close to 1:

there exist ρ ,α ,ε > 0 and u ∈ X such that
 0 0 0


## (Mp)

  inf I 1−ε (u) ≡ α 0 > 0, ∥u 0 ∥ > ρ 0 , max{I 1+ε (0), I 1+ε (u 0 )} ≤ 0.
∥u∥=ρ0
For λ ∈ [1−ε,1+ε], we define the mountain pass value
c (λ) ≡ inf sup I (γ(t)), where
0 λ
γ∈Γ0t∈[0,1]
(4)
Γ ≡ {γ ∈ C([0,1],X) | γ(0) = 0, γ(1) = u }.
0 0
We shall prove later that Γ ̸= ∅ and 0 < α ≤ c (λ) < ∞ for each λ ∈ [1−ε,1+ε], see Lemma 4.2. We
0 0 0
also note that, since Ψ ≥ 0, c (λ) is nondecreasing in λ.
0
Theorem 1.6. Assume that (Ψ ), (Ψ ), (Ψ ), (Φ ), (Φ ), (IB) and (MP) hold. Then I = I admits a
1 2 3 1 2 1
critical point u ∈ X with I(u) = c (1).
0
The second result concerns the multiplicity of critical points of I when I is even, so we assume

### Ψ(−u) = Ψ(u), Φ(−u) = Φ(u) for any u ∈ X. (E)

For k ∈ N, we let Dk(r) be the closed disk in Rk with center 0 and radius r. The disk Dk(1) is simply
denoted by Dk. We assume that I has the following uniform symmetric mountain pass geometry:
 there exist ρ ,α ,ε > 0 and an odd map π ∈ C(∂Dk,X) for each k ∈ N such that
 0 0 0,k


## (Smp)

inf I (u) ≡ α > 0, min ∥π (ζ)∥ > ρ . sup I (π (ζ)) < 0.
  ∥u∥=ρ0 1−ε 0 ζ∈∂Dk 0,k 0 ζ∈∂Dk 1+ε 0,k
4

<!-- Page 5 -->

For λ ∈ [1−ε,1+ε] and k = 1,2,..., we define the minimax values
c (λ) ≡ inf sup I (γ(ζ)), where
k λ
γ∈Γ kζ∈Dk
(5)
(cid:110) (cid:111)
Γ ≡ γ ∈ C(Dk,X) | γ is odd, γ = π on ∂Dk .
k 0,k
Again, we shall prove that Γ ̸= ∅ and that α ≤ c (λ) < ∞ holds, see Lemma 4.2.
k 0 k
Theorem 1.7. Assume that (Ψ ), (Ψ ), (Ψ ), (Φ ), (Φ ), (IB), (E) and (SMP) hold. Then, I = I
1 2 3 1 2 1
admits infinitely many critical points {u }∞ ⊂ X with I(u ) = c (1) → ∞ as k → ∞.
k k=1 k k
The proofs of Theorems 1.6 and 1.7 will be given in Section 4. Both results crucially rely on the
monotonicitytrickinTheorem4.4below,forwhichwedonotneedproperties(Ψ ),(Φ ),(IB). Comments
3 2
on Theorems 1.6 and 1.7 and their proof, and comparison with the literature, can be found in Subsection
1.1.
In Section 2, we apply Theorems 1.6 and 1.7 to obtain nontrivial solutions to (BI ). Here, it is
f
worth pointing out that the equivalence between critical points of I and (weak) solutions of (BI ) is
f
not immediate, and requires a regularity result for critical points of I of independent interest. To keep
the paper at a reasonable length, we only consider Born-Infeld type equations (BI ), even though our
f
main abstract achievements may be used in other settings: as an example, we mention quasilinear elliptic
problems including (Euclidean) mean curvature type ones [28,42,51], plastoelasticity problems [20,23],
nonlinear obstacle problems [28], solutions to the Lorentz force equation [3,4], see also the references
therein.
1.1 Previous related works and novelties of our approach
Various critical point theories based on nonsmooth analysis (for which we refer to [25]) arose in the past
40 years: for locally Lipschitz functionals we quote [24], for lower semicontinuous functionals in Banach
spaceswestressthealreadymentioned[63], whileforcontinuousfunctionalsinmetricspaceswehighlight
the theory developed independently by Corvellec, Degiovanni & Marzocchi [26–28] and by Katriel [37]
(see also [43] for the Banach space setting). As described in [27, §4], functionals I ≡ Ψ−Φ satisfying
(Ψ ),(Φ ) fit within their framework. However, to get a critical point the authors need the Palais-Smale
1 1
condition, so Theorems 1.6 and 1.7 do not follow from these results.
Regarding the monotonicity trick for nonsmooth functionals, we mention the work by Squassina [62].
Especially, [62, Theorem 3.1] should be compared to our Theorem 4.4 and in this respect the discussion
in [62, p.161–163] is informative. However, the functionals I in [62] are assumed to be continuous on the
λ
whole Banach space where they are defined, and this makes a difference with our results in obtaining a
deformation lemma and a bounded Palais-Smale sequence.
Next, wehighlightthedifferencesbetweenourpaperand[62,63]fromthetechnicalpointofview. Itis
known that the Palais-Smale condition plays a key role in obtaining existence and multiplicity of critical
points; see [2, section 2] and [54, section 9]. Since the condition is weakened in this paper, the assertions
in Theorem 1.7 are highly nontrivial. In fact, even though [62] considers higher minimax values, the
existence of infinitely many critical points is not obtained. In this respect, a new idea is necessary to
prove that the minimax values diverge. We next point out differences from [63]. First, for our purposes
we need to refine a deformation lemma in [63, Lemmas 2.1, 2.2 and Proposition 2.3]; see Lemma 3.1.
The second point regards Ekeland’s variational principle, exploited in [63] to ensure the existence of
Palais–Smale sequences: in our setting, to obtain bounded Palais-Smale sequences we need to consider
two different functionals I and I , a fact that seems to prevent the use of Ekeland’s principle. We thus
λ λ+ε
introduce a new iteration argument for deformations. This method is also useful to prove the divergence
of minimax values without the full Palais-Smale condition.
5

<!-- Page 6 -->

We next describe the issues concerning a variational approach to (BI ). If we consider (1) in a
f
bounded domain Ω, suitably choosing the function space X we may prove that the domain D(Ψ) itself is
bounded in X for any nonlinearity f ∈ C(Ω×R), which leads to the Palais-Smale condition. However,
for (BI ), this is no longer true. The difficulty to obtain the boundedness of Palais–Smale sequences
f
already occurs in the study of the scalar field equation
∆u+f(u) = 0 in Rn, (6)
where the nonlinearity f satisfies the so called Berestycki-Lions conditions (which are almost optimal for
the solvability of (6)). In [12–14] the existence of least energy solutions and minimax solutions to (6)
was proved by constrained minimization and minimax methods. The arguments there strongly depend
on the difference between the homogeneity in λ of
(cid:90) (cid:90)
|Du|2 and of F(u) = Φ(u)

### Rn Rn

with respect to the scaling u(x) → u(λx), which is essential to normalize a Lagrange multiplier. This is
notapplicabletoproblem(BI )since, underthenaturalscalingu(x) → λ−1u(λx)keepingtherestriction
f
|Du| ≤ 1, Ψ and Φ display almost the same homogeneity:
Ψ(u ) = λ−nΨ(u) and Φ(u ) = λ−nΦ(λ−1u).
λ λ
Forthisreason, inoursetting, theuseofaconstrainedproblemseemsmoredifficult. Bythesamereason,
arguments based on the scaling developed in [33–35] are not straightforward to apply to the functional
corresponding to (BI ).
f
Anapproachtorecovertheexistencetheoremsin[12–14]bymeansofunconstrainedminimaxmethods
was due to Struwe in [56], see also [59, section 11 of chapter II]. However, to verify a variant of the Palais-
Smale condition, he still needed to introduce some constraint. It seems to us that even this method may
hardly apply to (BI ). From a different viewpoint, seeking to weaken the regularity of −u+f(u) in (6)
f
we mention [60] and [21]. There, solutions were constructed for nonlinearities of bounded variation and
locally integrable, respectively.
In [5,6,16,50], commented later on in more detail, radial solutions to (BI ) were obtained by either
f
employing the shooting method or approximations of the operators. However, for the above reasons,
nonsmooth critical point theories were never applied to (BI ) in the literature. To our knowledge, the
f
present work is the first attempt to do so.
Finally, we mention the work by Jeanjean & Lu [42] where they employed the monotonicity trick to
obtain infinitely many solutions to (6). To this end, in [42, Section 2], the monotonicity trick is proved
for higher minimax levels as in Theorem 1.7 and in [62]. However, as pointed out in [42, Remark 2.2], the
authors did not obtain the divergence of the minimax levels in an abstract setting, the property was later
shown in [42, Lemma 5.7] by using the specific structure of (6) and a comparison functional (the same
as in [33]). To the authors’ knowledge, Theorem 1.7 seems to be the first abstract result in the literature
(even for smooth functionals) to show the divergence of minimax values under general conditions not
including the Palais-Smale’s one.
2 Application to the Born-Infeld equation
We exploit Theorems 1.6 and 1.7 to investigate the existence of nontrivial solutions to
(cid:32) (cid:33)

### Du

div +f(u) = 0 in Rn, (BI )
(cid:112) f
1−|Du|2
6

<!-- Page 7 -->

in dimension n ≥ 3. In principle, Theorems 1.6 and 1.7 could be applied to the case n = 2, too. However,
some technical details in the functional-analytic setting need a certain care, and for the sake of simplicity
the case n = 2 will be deferred to a future investigation.
Definition 2.1. Given a Radon measure ρ on Rn, a function u ∈ Lip(Rn) is called a weak solution to
(cid:32) (cid:33)

### Du

div +ρ = 0 in Rn
(cid:112)
1−|Du|2
if
1
|Du| ≤ 1 a.e., ∈ L1 (Rn), (7)
(cid:112) loc
1−|Du|2
and
(cid:90)

### Du·Dη

= ⟨ρ,η⟩ for any η ∈ Lip (Rn) ≡ Lip(Rn)∩C (Rn), (8)
(cid:112) c c

### Rn 1−|Du|2

where ⟨ρ,η⟩ stands for the duality pairing.
The definition does not make any assumption at infinity on u. However, we will restrict ourselves to
solutions (with ρ = f(u)) satisfying
u(x) → 0 as |x| → ∞, (9)
and among them solutions lying in the energy space
(cid:18)(cid:90) (cid:19)1
D1,2(Rn) ≡ C∞(Rn) ∥·∥ , ∥ϕ∥ ≡ |Dϕ|2 2 . (10)
c

### Rn

Formally, they are critical points of the functional
(cid:90) (cid:16) (cid:112) (cid:17) (cid:90) t
I(u) ≡ 1− 1−|Du|2−F(u) with F(t) = f(s)ds. (11)

### Rn 0

However, the behavior of the Lagrangian density on {|Du| = 1} prevents the differentiability of I and
calls for care. Nonetheless, in Propositions 2.13 and 2.10 below we prove that a critical point u of I
satisfying (9) is a weak solution of (BI ), and that u belongs to W2,q(Rn) for each q ∈ [2,∞) (hence, to
f loc
C1,α(Rn) for each α ∈ (0,1)) and is strictly spacelike, in the sense that |Du| < 1 on Rn. The regularity,
loc
whose proof needs some subtle arguments, also holds under much more general growth conditions on u
at infinity. We expect it will be a handy tool for future works on Born-Infeld equations.
To the best of our knowledge, so far the existence problem for (BI ) was only considered when
f
restricted to radially symmetric functions. In [6], Azzollini studied positive solutions in the model case
f(t) = |t|p−2t, and showed that the problem
(cid:32) (cid:33)

### Du

div +|u|p−2u = 0 in Rn, lim u(x) = 0, (12)
(cid:112)
1−|Du|2 |x|→∞
- has a radially symmetric positive solution in D1,2(Rn) and infinitely many positive solutions not in
D1,2(Rn) for p ∈ (2∗,∞), where 2∗ = 2n ;
n−2
- does not have radially symmetric positive solutions if p ∈ (1,2∗).
7

<!-- Page 8 -->

On the other hand, for p ∈ (2∗,∞) infinitely many radially symmetric solutions in D1,2(Rn) to (12)
were constructed by Bonheure, De Coster & Derlet in [16] using a constrained minimax argument. In the
same paper, the authors posed the existence problem for p = 2∗ as an interesting question, see [16, page
262].
Other nonlinearities have also been considered. A problem corresponding to the “positive mass case”
of (12), namely,
(cid:32) (cid:33)

### Du

div −u+|u|p−2u = 0, lim u(x) = 0 (13)
(cid:112)
1−|Du|2 |x|→∞
was studied in [5] and it was shown that (13) admits a radially symmetric positive solution in H1(Rn) for
each p ∈ (1,∞). Indeed, the solution therein was obtained by a shooting argument, for a class of locally
Lipschitzfunctionsmuchlargerthan|u|p−2u. Ageneralexistenceresultfor onenontrivialradialsolution,
closely related to our main Theorem 2.2 below, was recently obtained by Mederski & Pomponio [50], and
will be commented in detail in Remark 2.3.
About the existence of solutions, we shall consider both radial and non-radial ones. To construct the
latter, we restrict to n and d ∈ N satisfying
n
n ≥ 4, 2 ≤ d ≤ , and n−2d ̸= 1. (14)
2
Write a point of Rn as x = (x ,x ,x ) ∈ Rd × Rd × Rn−2d and consider the subspace of functions
1 2 3
u ∈ D1,2(Rn) with the following symmetries:
u(Ax ,Bx ,Cx ) = u(x ,x ,x ) for each A,B ∈ O(d), C ∈ O(n−2d),
1 2 3 1 2 3
(15)
u(x ,x ,x ) = −u(x ,x ,x ).
2 1 3 1 2 3
Since Bartsch & Willem [8], the above subspace has been extensively used (we refer to [49] and references
therein). Notice that the only radial function therein is u ≡ 0, whence nontrivial solutions to (BI ) with
f
the symmetries described in (15) must be non-radial. Given a mass parameter m ≥ 0 and p ∈ [2,2∗], we
define
D m 1, , 2 p (Rn) ≡ C c ∞(Rn) ∥·∥ Dm 1, , 2 p, ∥ϕ∥ D1,2 ≡ (cid:113) ∥Dϕ∥2 2 +m∥ϕ∥2 p .
m,p
The exponent p will be related to m according to assumption (f1) below. If m = 0, then D1,2(Rn) =
0,p
D1,2(Rn). In this case, we agree to set p = 2∗. Likewise, by Sobolev’s embedding, for m > 0 and p = 2∗
the space D1,2(Rn) is D1,2(Rn) with an equivalent norm.
m,p

### We are ready to state our main existence theorem:

Theorem 2.2. Assume that n ≥ 3 and that f ∈ C(R), m ≥ 0 satisfy
(f1) either
f(s) f(s)
(f1 ) m = 0, −∞ < liminf ≤ limsup = 0, or
0
s→0
|s|2∗−2s
s→0
|s|2∗−2s
f(s) f(s)
(f1 ) m > 0, −∞ < liminf ≤ limsup ≡ −m for some p ∈ [2,2∗];
m,p s→0 |s|p−2s s→0 |s|p−2s
(f2) there exists t > 0 such that F(t ) ≡
(cid:82)t0f(t)dt
> 0.
0 0 0
Then, (BI ) admits a positive radial weak solution u ∈ D1,2(Rn) with I(u) ∈ (0,∞), where I is defined
f m,p
in (11). Moreover, if f is odd, then (BI ) admits
f
8

<!-- Page 9 -->

- infinitelymanydistinctradialweaksolutions{u } ⊂ D1,2(Rn), possiblysign-changing, withI(u ) ∈
k k m,p k
(0,∞) and I(u ) → ∞ as k → ∞;
k
- infinitely many distinct nonradial, sign-changing weak solutions {u } ⊂ D1,2(Rn) satisfying (15)
k k m,p
with I(u ) ∈ (0,∞) and I(u ) → ∞ as k → ∞, provided that n,d satisfy (14).
k k
Finally, any weak solution v ∈ D1,2(Rn) to (BI ) satisfies v ∈ W2,q(Rn) for each q ∈ [2,∞), and
m,p f loc
∥Dv∥ < 1 in Rn.
∞
Remark 2.3. One main novelty of Theorem 2.2 is the first construction of non-radial solutions to (BI ).
f
Even in the radial case, however, the result is not contained in the previous literature, and indeed,
under the only conditions (f1),(f2), to the best of our knowledge the existence of a radial solution in
D1,2(Rn) was still unknown. The most general existence result we are aware of is [50, Theorem 1.1] by
Mederski & Pomponio, where the authors produce a nontrivial radial solution in dimension n ≥ 3 for
odd nonlinearities f ∈ C(R) satisfying (f2) and either
(i) assumption (f1 ), for m > 0 and some p ∈ [2,∞), or
m,p
(ii) the following assumption:
f(s) f(s)
−∞ < liminf ≤ limsup = 0 for some γ > 2∗
s→0 |s|γ−1 s→0 |s|γ−1
and, if 2∗ < γ ≤ n,
(cid:18) (cid:19)
f(s) nγ nq
limsup = 0 for some q ∈ ,n , where q∗ = .
|s|q∗−1 n+γ n−q
s→∞
Notice that (ii) and (i) for p > 2∗ are stronger than (f1 ), while (i) with p ∈ [2,2∗] corresponds to (f1 ).
0 m,p
Remark 2.4. By appropriately defining Ψ,Φ in Theorem 2.2 so that weak solutions u to (BI ) corref
spond to critical points of I = Ψ−Φ, the symmetry group G of u is chosen to ensure (Φ ) once Φ is
2
restricted to the subspace of G-invariant functions, and to guarantee that the corresponding restriction
of I still has a uniform (symmetric) mountain pass geometry. The method should be flexible enough to
λ
produce other types of nontrivial solutions.
Remark 2.5. In [64], Van Schaftingen described an abstract framework to find G-invariant minimax
critical points without restricting, a priori, the functional I to a G-invariant subspace X (see also [62]).

## G

One advantage of the method is that the minimax values are taken among maps valued in X, not only in
X ; hence, the approach in [64] may help to establish whether the positive, radially symmetric solution

## G

produced in Theorem 2.2 is a ground state, namely, a minimizer for I among all nonzero solutions. The
semilinear case was studied in [40].
The following Pohozaev identity will be crucial to check (IB) for problem (BI ).
f
Proposition 2.6. For f ∈ C(R), let u be a weak solution to (BI ) satisfying
f
 
(cid:90) |Du|2
(cid:113) +F(u) < ∞. (16)

### Rn 1−|Du|2

Then, u ∈ W2,q(Rn) for each q ∈ [2,∞), |Du| < 1 on Rn and
loc
(cid:90) |Du|2 (cid:90) (cid:16) (cid:112) (cid:17)
= n 1− 1−|Du|2−F(u) < ∞. (17)
(cid:112)
Rn 1−|Du|2 Rn
9

<!-- Page 10 -->

As an application of Proposition 2.6, we rule out the existence of finite energy solutions for f not
supercritical. Hence, condition (f1) in Theorem 2.2 is necessary for the existence of a solution to (BI ).
f
On the other hand, condition (f2) is needed to show the mini-max structure (MP) or (SMP) of the energy
functional, and we believe that it is necessary as well. In this respect, it is well known that (f2) is a
necessary condition for the existence of a finite energy solution to (6).
Proposition 2.7. For n ≥ 3 there exist no weak solutions u ̸≡ 0 to
(cid:32) (cid:33)

### Du

div +|u|p−2u = 0 in Rn, p ∈ [2,2∗] (18)
(cid:112)
1−|Du|2
satisfying
(cid:90)
(cid:0) |Du|2+|u|p(cid:1)
< ∞. (19)

### Rn

In particular, (18) for p = 2∗ does not admit any weak solution u ∈ D1,2(Rn)\{0}.
Remark 2.8. Forp = 2∗,wethusanswerinthenegativethequestionraisedin[16,page262]forsolutions
in D1,2(Rn). We expect that there exist no positive weak solutions to (18) for p ∈ (2,2∗) without any
restriction, as shown in [31] for the semilinear case ∆u+|u|p−2u = 0. We also believe that the critical
case p = 2∗ does not admit any positive weak solutions to (18). As a related problem, studying the
behavior of mountain pass solutions to (18) as p ↘ 2∗ seems also a quite interesting issue.
2.1 Critical points of I and weak solutions to (BI )
f
We first discuss the regularity properties of weak solutions in Definition 2.1. Given a Radon measure ρ
on Rn, define the action I on a bounded domain Ω ⋐ Rn as
ρ
(cid:90) (cid:16) (cid:112) (cid:17)
IΩ(ψ) ≡ 1− 1−|Dψ|2 −⟨ρ,ψ⟩ ,
ρ Ω

## Ω

with ⟨, ⟩ the duality pairing and ⟨ρ,ψ⟩ = ⟨ρ ,ψ⟩. For ϕ ∈ C(∂Ω), we consider the convex set

## Ω |Ω

Y ϕ (Ω) ≡ (cid:8) ψ ∈ W1,∞(Ω) (cid:12) (cid:12) |Dψ| ≤ 1, ψ = ϕ on ∂Ω (cid:9) .
Remark 2.9. If ∂Ω is not regular enough to achieve ψ = ϕ in the trace sense, the boundary condition
has to be intended as in [9]. However, by [22, Proposition 3.5] this definition suffices to guarantee that
functions u ∈ Y (Ω) can be extended continuously to ∂Ω with boundary datum ϕ.
ϕ

### We say that

- u minimizes I on Ω with boundary value ϕ ∈ C(∂Ω) if
ρ
IΩ(u) ≤ IΩ(ψ) for each ψ ∈ Y (Ω);
ρ ρ ϕ
- u is a local minimizer for I ifitminimizesIΩ oneachdomainΩ ⋐ Rn withrespecttotheboundary
ρ ρ
value ϕ = u .
|

## ∂Ω

The regularity result we need is encoded in the next proposition of independent interest, proved in
Appendix B.
Proposition 2.10. Let u ∈ Lip(Rn) satisfy |Du| ≤ 1 a.e. on Rn, and let ρ ∈ L∞(Rn).
loc
10

<!-- Page 11 -->

(i) Suppose that there exist c > 0 and a function h : Rn → (0,∞) such that
1
h(x)
h(x) → ∞ as |x| → ∞, lim = 0,
|x|→∞ |x| (20)
|u(x)| ≤ c +|x|−h(x) on Rn.
1
Then, the following are equivalent:
(a) u is a weak solution to
(cid:32) (cid:33)

### Du

div +ρ = 0 in Rn (BI )
(cid:112) ρ
1−|Du|2
as stated in Definition 2.1.
(b) u is a local minimizer for I .
ρ
Furthermore, if any between (a) and (b) occurs then u ∈ W2,q(Rn) for each q ∈ [2,∞), and |Du| < 1
loc
on Rn. Moreover, for each R,c > 0 and q ≥ 2 there exist Rˆ = Rˆ(R,c ,h) and δ = δ(Rˆ,c),
1
C = C(Rˆ,c,q) with the following properties: if
q
∥ρ∥ ≤ c,

## L∞(B (0))


## Rˆ

then
sup |Du| ≤ 1−δ, ∥u∥ ≤ C .
W2,q(BR(0)) q

## Br(0)

(ii) Assume that ρ ∈ L∞(Rn) and u ∈ L∞(Rn) is a weak solution to (BI ) with ∥ρ∥ +∥u∥ ≤ c.
ρ ∞ ∞
Then, there exists δ = δ(c) ∈ (0,1) such that ∥Du∥ ≤ 1−δ.
∞
Remark 2.11. A growth requirement like (20) is necessary for the equivalence (a) ⇔ (b) to hold. To see
this, consider the example ρ ≡ 0 and u an affine function with slope 1. Then, u satisfies (b) but clearly
does not satisfy (7) in the definition of weak solution, and (8) cannot be given a reasonable meaning.
Remark 2.12. Case (ii) in the above proposition improves on [15, Theorem 1.5].
We next specify the above proposition to our case of interest, the equivalence of critical points of I
and solutions of (BI ).
f
Proposition 2.13. Assume that n ≥ 3 and m ≥ 0, that u ∈ D1,2(Rn), and that the functional
m,p
(cid:90)
η ∈ C∞(Rn) (cid:55)→ ⟨f(u),η⟩ ≡ f(u)η (21)
c

### Rn

extends to a continuous one on D1,2(Rn). Then, the following are equivalent:
m,p
(a) u is a weak solution to (BI );
f
(b) u is a local minimizer for I with ρ = f(u);
ρ
(c) The following inequality holds for each ψ ∈ D1,2(Rn) with ∥Dψ∥ ≤ 1:
m,p ∞
(cid:90) (cid:16)(cid:112) (cid:112) (cid:17) (cid:90)
1−|Du|2− 1−|Dψ|2 − f(u)(ψ−u) ≥ 0. (22)
Rn Rn
11

<!-- Page 12 -->

Remark 2.14. Hereafter, we will often employ the following useful properties valid for t ∈ [0,1]:
t2 (cid:112) (cid:112) (cid:88) ∞
≤ 1− 1−t2 ≤ t2, 1− 1−t2 = b t2k with b > 0,
k k
2
k=1
and the pointwise inequality
Du·(Du−Dψ) (cid:112) (cid:112)
≥ 1−|Dψ|2− 1−|Du|2 (23)
(cid:112)
1−|Du|2
on the set of points {|Du| < 1}∩{|Dψ| ≤ 1}, see [22, Remark 3.15].
Proof of Proposition 2.13. (a) ⇔ (b)Sincen ≥ 3,fromtheSobolevembeddingD1,2(Rn) (cid:44)→ L2∗(Rn),
m,p
and from u ∈ D1,2(Rn), ∥Du∥ ≤ 1 we deduce that u(x) → 0 as |x| → ∞. In particular, Proposition
m,p ∞
2.10 ensures that (a) ⇔ (b) and that u ∈ W2,q(Rn) with ∥Du∥ < 1.
loc ∞
(a) ⇒ (c) Given ψ ∈ D1,2(Rn) with ∥Dψ∥ ≤ 1 and a sequence ε → 0, we define
m,p ∞ j

u(x) if |ψ(x)−u(x)| < ε ,
 j


ψ (x) ≡ max{u(x),ψ(x)−ε }+min{u(x),ψ(x)+ε }−u(x) = ψ(x)+ε if u(x) ≥ ψ(x)+ε , (24)
j j j j j


 ψ(x)−ε if u(x) ≤ ψ(x)−ε .
j j
Sincebothuandψ vanishas|x| → ∞, byconstructionu−ψ hascompactsupportforeachj. Noticealso
j
that |ψ (x)| ≤ |u(x)|+|ψ(x)−u(x)| holds for any x ∈ Rn. Thus, the dominated convergence theorem
j
shows that ψ → ψ strongly in D1,2(Rn) as j → ∞ (see [22, Lemma 3.7] for more details in the case
j m,p
m = 0. The case m > 0 follows by minor modifications). Plugging u−ψ ∈ Lip (Rn) in the definition of
j c
weak solution to (BI ) and using (23) we get
f
(cid:90) (cid:16)(cid:113) 1−|Dψ |2− (cid:112) 1−|Du|2 (cid:17) ≤ (cid:90) Du·(Du−Dψ j ) = (cid:90) f(u)(u−ψ ).
j (cid:112) j

### Rn Rn 1−|Du|2 Rn

Rearranging, we infer (22) for the test function ψ . On the other hand, from the definition of ψ and the
j j
first in Remark 2.14 we observe that
(cid:12)(cid:113) (cid:112) (cid:12) (cid:112) (cid:112)
(cid:12) 1−|Dψ |2− 1−|Du|2(cid:12) ≤ 1− 1−|Dψ|2+1− 1−|Du|2 ≤ |Dψ|2+|Du|2.
(cid:12) j (cid:12)
Whence, inequality (22)followsbylettingj → ∞andusingthedominatedconvergencetheoremtogether
with the assumed continuity of (21).
(c) ⇒ (b) Fix Ω ⋐ Rn and ψ ∈ Y (Ω). Up to replacing ψ with ψ as in (24), we can assume that
u j
supp(ψ−u) ⋐ Ω. Extend ψ to Rn by setting ψ = u away from Ω. Inequality (22) implies
(cid:90) (cid:16)(cid:112) (cid:112) (cid:17) (cid:90)
1−|Du|2− 1−|Dψ|2 − f(u)(ψ−u) ≥ 0.

## Ω Ω

Then, setting ρ ≡ f(u) and rearranging we get IΩ(u) ≤ IΩ(ψ), thus u satisfies (b). ■
ρ ρ
2.2 Proofs of Propositions 2.6 and 2.7
Proof of Propositions 2.6. By (16), |Du| ∈ L2(Rn) and the interpolation inequality with |Du| ≤ 1
implies ∥Du∥ < ∞ for each q ≥ 2. Hence, by the proof of Morrey’s embedding theorem (for instance,
q
see [19, Theorem 9.12]), for q > n the C0,1−n/q H¨older seminorm of u on Rn is globally bounded,
12

<!-- Page 13 -->

(cid:16) 1−n(cid:17)
thus |u(x)| = O |x| q as |x| → ∞. Proposition 2.10 guarantees the stated regularity of u. Set for
convenience r(x) = |x|. We prove that for every R ∈ (0,∞)
(cid:40) (cid:41)
(cid:90) |Du|2 (cid:16) (cid:112) (cid:17)
−n 1− 1−|Du|2 +nF(u)
(cid:112)
1−|Du|2

## Br

(25)
(cid:40) (cid:41)
(cid:90) (Du·Dr)2 (cid:16) (cid:112) (cid:17)
= R F(u)+ − 1− 1−|Du|2 dσ,
(cid:112)
1−|Du|2

## ∂Br

where B = B (0). We consider the piecewise affine function

## R R


1 if t ≤ R−ε/2,


τ (t) = 1−ε−1(t−R+ε/2) if R−ε/2 < t < R+ε/2,
ε

 0 if t ≥ R+ε/2.
Because of the regularity of u, by density (8) also holds for W1,q test functions with compact support, so
we can use η ≡ τ (r)rDr·Du in (8) with ρ = f(u) to obtain
ε ε
(cid:90) (cid:90)
Du·Dη
ε
= f(u)η .
(cid:112) ε

### Rn 1−|Du|2 Rn


### From div(rDr) = n we get

f(u)η = div(τ F(u)rDr)−rτ′(r)F(u)−nτ (r)F(u),
ε ε ε ε
hence
(cid:90) (cid:90) (cid:90)
f(u)η = − rτ′(r)F(u)−n τ (r)F(u).
ε ε ε

### Rn Rn Rn


### Notice also that

Du·Dη ε = rτ ε ′(r)(Du·Dr)2 + τ ε (r)|Du|2 +τ (r)rDr·D (cid:16) 1− (cid:112) 1−|Du|2 (cid:17) .
(cid:112) (cid:112) (cid:112) ε
1−|Du|2 1−|Du|2 1−|Du|2
Therefore, integrating by parts yields
(cid:90)
Du·Dη
ε
(cid:112)

### Rn 1−|Du|2

(cid:40) (cid:41)
= (cid:90) rτ ε ′(r)(Du·Dr)2 + τ ε (r)|Du|2 − (cid:8) rτ′(r)+nτ (r) (cid:9) (cid:16) 1− (cid:112) 1−|Du|2 (cid:17)
(cid:112) (cid:112) ε ε
Rn 1−|Du|2 1−|Du|2
and we conclude
(cid:34) (cid:35)
(cid:90) |Du|2 (cid:16) (cid:112) (cid:17)
τ (r) −n 1− 1−|Du|2 +nF(u)
ε (cid:112)
Rn 1−|Du|2
(26)
(cid:34) (cid:35)
(cid:90) (Du·Dr)2
(cid:112)
= rτ′(r) − +1− 1−|Du|2−F(u) .
ε (cid:112)

### Rn 1−|Du|2

The coarea formula guarantees that
(cid:34) (cid:35)
(cid:90) (Du·Dr)2 (cid:16) (cid:112) (cid:17)
t (cid:55)→ h(t) ≡ F(u)+ − 1− 1−|Du|2 dσ ∈ L1 ((0,∞)),
(cid:112) loc
1−|Du|2
∂Bt
13

<!-- Page 14 -->

thus, letting ε → 0 in (26) and using the definition of τ and the fact Du ∈ C(Rn), we obtain (25) for
ε √
any R. Moreover, by the triangle inequality and the observation that 1− 1−t2 ≤ t2, see Remark 2.14,
we get
(cid:34) (cid:35)
(cid:90) |Du|2
|h(t)| ≤ F(u)+ +|Du|2 dσ,
(cid:112)
1−|Du|2
∂Bt
hence from (16) and the coarea formula we infer that h ∈ L1([1,∞)). Therefore, there exists a sequence
{R } such that R → ∞ and R h(R ) → 0 as k → ∞. Observing that (16) and the first in Remark
k k k k
2.14 guarantee the finiteness of the right-hand side of (17), letting R = R → ∞ in (25) we conclude the
k
desired identity. ■
With the aid of the Pohozaev identity in Propositions 2.6, we can show Proposition 2.7.
Proof of Proposition 2.7. Let u be a weak solution to (18) verifying (19). From u ∈ Lp(Rn) and
∥Du∥ ≤ 1, we deduce that u vanishes at infinity, hence u ∈ L∞(Rn). Since f(u(x)) = |u|p−2(x)u(x) ∈
∞
L∞(Rn), Proposition 2.10 (ii) guarantees that ∥Du∥ < 1, and (19) implies
∞
(cid:90) |Du|2 1 (cid:90)
≤ |Du|2 < ∞.
(cid:113) (cid:113)
Rn 1−|Du|2 1−∥Du∥2 Rn
∞
Thus, we apply Proposition 2.6 with f(u) = |u|p−2u to deduce that
(cid:90) |Du|2 (cid:90) (cid:18) (cid:112) 1 (cid:19)
= n 1− 1−|Du|2− |u|p < ∞. (27)
(cid:112)

### Rn 1−|Du|2 Rn p

For ε > 0, we plug the compactly supported test function η = ζ (u) with ζ (t) ≡ (t−ε) −(t+ε) in
ε ε + −
the weak definition of (18) to obtain
(cid:90) (cid:90) |Du|2
|u|p−2uζ (u) = .
ε (cid:112)
1−|Du|2
{|u|>ε} {|u|>ε}
Letting ε → 0, using the dominated convergence theorem, the identity |Du| ≡ 0 a.e. on {u = 0}, and
substituting in (27) we thus get
(cid:40) (cid:41)
(cid:90) p+n |Du|2 (cid:16) (cid:112) (cid:17)
0 = −n 1− 1−|Du|2 .
(cid:112)

### Rn p 1−|Du|2


### Since p ≤ 2∗ and

p+n t (cid:0) √ (cid:1) n (cid:18) t (cid:0) √ (cid:1) (cid:19)
√ −n 1− 1−t ≥ √ −2 1− 1−t > 0 for t ∈ (0,1),
p 1−t 2 1−t
we conclude that |Du| ≡ 0, thus u ≡ 0, a contradiction. ■
2.3 Proof of Theorem 2.2
For convenience, having fixed p > max{n,p}, we define a subspace Y (Rn) of D1,2(Rn) by
1 m,p m,p
(cid:113)
Y (Rn) ≡ C∞(Rn) ∥·∥Ym,p, ∥v∥ ≡ m∥v∥2+∥Dv∥2+∥Dv∥2 ,
m,p c Ym,p p 2 p1
where we agree that p = 2∗ if m = 0. Notice that, by Sobolev’s embedding, Y (Rn) (cid:44)→ Y (Rn).
m,p 0,2∗
14

<!-- Page 15 -->

Lemma 2.15. Let n ≥ 3. Then Y (Rn) is a reflexive Banach space and satisfies
m,p
(i) Y (Rn) (cid:44)→ W1,p(Rn),
m,p
(cid:26) (cid:12) (cid:27) (28)
(ii) Y m,p (Rn) (cid:44)→ C 0 (Rn) ≡ u ∈ C(Rn) (cid:12) (cid:12) lim u(x) = 0 .
(cid:12) |x|→∞
Proof. The norm ∥·∥ is uniformly convex by the uniform convexity of Lq-spaces and [19, Exercise

### Ym,p

3.29], thus Y (Rn) is reflexive. If m = 0, then (i) and (ii) have been shown in [22, Proposition 3.3] (the
m,p
norm used there is equivalent to ∥·∥ ), hence (ii) for m > 0 is a consequence of Y (Rn) (cid:44)→ Y (Rn).

### Y 0,2∗ m,p 0,2∗

On the other hand, interpolation gives
1 θ 1−θ
∥Du∥ ≤ ∥Du∥θ∥Du∥1−θ ≤ ∥u∥ , = + ,
p 2 p1 Ym,p p 2 p
1
thus (i) holds for m > 0 as well. ■
In view of the above Lemma, it will be convenient to use Y (Rn) instead of D1,2(Rn). Notice
m,p m,p
however the following properties: for any constant c > 0,
(a) for u with ∥Du∥ ≤ c, u ∈ D1,2(Rn) ⇐⇒ u ∈ Y (Rn), and
∞ m,p m,p
∥u∥
D m 1, , 2 p
≤ ∥u∥

### Ym,p

≤ ∥u∥

### D m 1, , 2 p

+c 1− p 2 1∥u∥

## D

p 2 1
m 1, , 2 p
;
(29)
(b) if {u } ⊂ Y (Rn), u ∈ Y (Rn) and ∥Du ∥ ≤ c, ∥Du∥ ≤ c, then
j m,p m,p j ∞ ∞
∥u −u∥ → 0 ⇐⇒ ∥u −u∥ → 0.
j Ym,p j D
m
1,
,
2
p
We define Φ,Ψ : Y (Rn) → (−∞,∞] as follows:
m,p

 
(cid:90) (cid:18)
1− (cid:112) 1−|Du|2+
m|u|p(cid:19)
if ∥Du∥ ≤ 1;

### Ψ(u) ≡ Rn 2p ∞

 ∞ if ∥Du∥ > 1, (30)
∞
(cid:90) m
Φ(u) ≡ G(u), with G(s) ≡ F(s)+ |s|p.
2p

### Rn

Because of the first in Remark 2.14 and (a) in (29), the domain of Ψ is
D(Ψ) ≡ {u ∈ Y (Rn) | Ψ(u) < ∞} = {u ∈ Y (Rn) | ∥Du∥ ≤ 1}. (31)
m,p m,p ∞
Remark 2.16. By combining (28), the reflexivity of Y (Rn) and the fact that functions in D(Ψ) are
m,p
equi-Lipschitz, the following holds: from every bounded sequence {u }∞ ⊂ D(Ψ) we can extract a
k k=1
subsequence (still labelled the same) such that u → u weakly in Y (Rn) and locally uniformly in Rn.
k m,p

### Define also

I : Y (Rn) → (−∞,∞], I (u) ≡ λΨ(u)−Φ(u).
λ m,p λ
We first check the conditions for Ψ.
Lemma 2.17. Ψ : Y (Rn) → [0,∞] satisfies (Ψ ), (Ψ ), (Ψ ).
m,p 1 2 3
Proof. Observe first that if {u } ⊂ D(Ψ), u ∈ D(Ψ) and
j j
m∥u∥ ≤ liminfm∥u ∥ , ∥Du∥ ≤ liminf∥Du ∥ for every k ≥ 1, (32)
p j p 2k j 2k
j→∞ j→∞
15

<!-- Page 16 -->

then by the second in Remark 2.14 the following chain of inequalities holds:
m (cid:88) ∞ (cid:90) m (cid:88) ∞ (cid:90)
Ψ(u) = ∥u∥p+ b |Du|2k ≤ ∥u∥p+ b liminf |Du |2k (33)
2p p k Rn 2p p k j→∞ Rn j
k=1 k=1
(cid:34) m (cid:88) ∞ (cid:90) (cid:35)
≤ liminf ∥u ∥p+ b |Du |2k = liminfΨ(u ). (34)
j→∞ 2p j p k Rn j j→∞ j
k=1
√
We prove (Ψ ). Since t (cid:55)→ 1− 1−t2 is convex for t ∈ (0,1), Ψ is convex on Y (Rn). To check that Ψ
1 m,p
is lower-semicontinuous, let u → u in Y (Rn). The claim is obvious if ∥Du ∥ > 1 for all large j. On
j m,p j ∞
the other hand, if ∥Du ∥ ≤ 1 for a subsequence j → ∞, then ∥Du ∥ → ∥Du∥ for all k ≥ 1. Using
ji ∞ i ji 2k 2k
also m∥u ∥ → m∥u∥ , we can apply (33) to deduce that Ψ(u) ≤ liminf Ψ(u ).
ji p p i→∞ ji
For property (Ψ ), if ∥Du∥ ≤ 1, then ∥Du∥q ≤ ∥Du∥2 for each q ≥ 2. Hence, the first in Remark
2 ∞ q 2
2.14 and the definition of Ψ yield
4
∥u∥2

### Ym,p

= m∥u∥2
p
+∥Du∥2
2
+∥Du∥2
p1

## ≤ C

p,m
(Ψ(u))p 2 +∥Du∥2
2
+∥Du∥
2
p1

## ≤ C

p,m
(Ψ(u))p 2 +b−
1
1Ψ(u)+ (cid:0) b−
1
1Ψ(u) (cid:1) p 2 1.
Thus, (Ψ ) holds.
2
Toshow(Ψ ),assumethat{u } ⊂ D(Ψ)andu ∈ D(Ψ)satisfyu ⇀ uinY (Rn)andΨ(u ) → Ψ(u)
3 j j j m,p j
as j → ∞. The weak convergence and u ,u ∈ D(Ψ) yields Du ⇀ Du in L2k(Rn;Rn) as j → ∞ for
j j
each fixed k ≥ 1, hence both of the inequalities in (32) hold. From the uniform convexity of Lq-spaces, it
suffices to prove that m∥u ∥ → m∥u∥ and that ∥Du ∥ → ∥Du∥ for each k ∈ N. By contradiction,
j p p j 2k 2k
if one of these fails, then up to passing to a subsequence one of the inequalities in (32) is strict. As a
consequence, one of the two inequalities in (33) is strict as well (recall: here we use the fact b > 0 for
k
each k), whence we would conclude from (33) that
Ψ(u) < liminfΨ(u ) = Ψ(u),
j
j→∞
a contradiction. ■
Lemma 2.18. If n ≥ 3 and f ∈ C(R) satisfies
(cid:40)
|f(s)| p = 2∗ if m = 0,
limsup < ∞ with (35)
s→0 |s|p−1 p ∈ [2,2∗] if m > 0,
then Φ : Y (Rn) → R satisfies (Φ ).
m,p 1
Proof. By Lemma 2.15, Y (Rn) (cid:44)→ C (Rn). From (35), it is standard to see that Φ ∈ C1(Y (Rn),R).
m,p 0 m,p
■
Next, we check that critical points for I are weak solutions to (BI ). In the positive mass case, this
f
is not entirely trivial due to the asymmetric role of Ψ and Φ in the definition of a critical point. We have
Proposition 2.19. Let Φ,Ψ be as in (30), and assume (35). Then, for each λ ∈ R+ the following are
equivalent:
- u ∈ D1,2(Rn) is critical for I ≡ λΨ−Φ;
m,p λ
16

<!-- Page 17 -->

- u ∈ D1,2(Rn) is a weak solution to
m,p
(cid:32) (cid:33)

### Du m(1−λ)

div + |u|p−2u+λ−1f(u) = 0, (36)
(cid:112)
1−|Du|2 2λ
in particular, u ∈ W2,q(Rn) for q ∈ [2,∞), and ∥Du∥ < 1.
loc ∞
To prove the result, we need the following general lemma.
Lemma 2.20. Let X be a normed space, u ∈ X and Ψˆ, Φˆ satisfy (Ψ ),(Φ ), respectively. Then, the
1 1
following are equivalent:
(i) u is a critical point for Ψˆ −Φˆ;
(ii) for some (or equivalently, every) convex, C1 functional T : X → R, u is a critical point for Ψˆ −Φˆ

## T T

with Ψˆ ≡ Ψˆ +T and Φˆ ≡ Φˆ +T.

## T T

Proof. (i) ⇒ (ii) for each T.
Since T is convex, T(v)−T(u)−T′(u)(v−u) ≥ 0. By combining this inequality with the definition
of u being a critical point for Ψˆ −Φˆ we deduce
Ψˆ (v)−Ψˆ (u)−Φˆ′ (u)(v−u) ≥ 0 for all v ∈ X,

## T T T

thus u is critical for Ψˆ −Φˆ .

## T T

(ii) for some T ⇒ (i).
Assume that there exists a convex functional T ∈ C1(X,R) for which
(cid:0) Ψˆ(w)+T(w) (cid:1) − (cid:0) Ψˆ(u)+T(u) (cid:1) − (cid:0) Φˆ′(u)+T′(u) (cid:1) (w−u) ≥ 0 for all w ∈ X.
Fix v ∈ X and write w = (1−t)u+tv, t ∈ (0,1]. Since Ψˆ is convex and T is of class C1,
Ψˆ(w)−Ψˆ(u) ≤ t(Ψˆ(v)−Ψˆ(u)), T(w)−T(u) = tT′(u)(v−u)+o(t),
which yields
t(Ψˆ(v)−Ψˆ(u))+tT′(u)(v−u)+o(t)−t (cid:0) Φˆ′(u)+T′(u) (cid:1) (v−u) ≥ 0.
Dividing by t and letting t → 0 we conclude
Ψˆ(v)−Ψˆ(u)−Φˆ′(u)(v−u) ≥ 0,
as claimed. ■

### Proof of Proposition 2.19. Applying Lemma 2.20 with

T(u) = mλ ∥u∥p, Ψˆ(u) = λ (cid:90) (cid:16) 1− (cid:112) 1−|Du|2 (cid:17) , Φˆ(u) = (cid:90) (cid:18) F(u)+ m(1−λ) |u|p (cid:19)
2p p 2p

### Rn Rn

we deduce that u is critical for I if and only if it is critical for Ψˆ −Φˆ. In this respect, notice that Φ,Φˆ
λ
and T are of class C1 by Lemma 2.18. Proposition 2.13 then ensures that critical points of Ψˆ−Φˆ coincide
with weak solutions to (36), and enjoy the claimed regularity properties. ■
We next prove that under our assumptions I satisfies (IB).
λ
Lemma 2.21. Assume that f ∈ C(R) satisfies (f1). Then, I : Y (Rn) → R satisfies (IB).
λ m,p
17

<!-- Page 18 -->

Proof. Without loss of generality, we can assume c > 0 in the definition of Kc . By Proposition 2.19,
[a,b]
critical points u ∈ Kc for I are weak solutions to (36). Moreover, u ∈ W2,q(Rn) for q ∈ [2,∞), and
[a,b] λ loc
∥Du∥ < 1. The latter, together with u ∈ Y (Rn) and (f1), imply
∞ m,p
(cid:32) (cid:33)
(cid:90) |Du|2
+m|u|p+|F(u)| < ∞,
(cid:112)

### Rn 1−|Du|2

thus by combining the Pohozaev identity (17) and I (u) ≤ c we deduce
λ
(cid:90) |Du|2 = n (cid:90) (cid:16) 1− (cid:112) 1−|Du|2 (cid:17) − n (cid:90) (cid:26) m(1−λ) |u|p+F(u) (cid:27)
(cid:112)
Rn 1−|Du|2 Rn λ Rn 2p (37)
n nc nc
= I (u) ≤ ≤ .
λ
λ λ a
Therefore, Kc ⊂ D(Ψ) is bounded in D1,2(Rn), hence in Y (Rn) and in C(Rn) because of (28) and
[a,b] 0,2∗
(29). This settles the case m = 0. Assume m > 0, and fix δ such that
m m
f(s)s+ |s|p ≤ − |s|p if |s| ≤ δ.
2 4
This is possible by the definition of m. Choose a constant κ so that ∥u∥ +∥u∥ ≤ κ for each u ∈ Kc .
2∗ ∞ [a,b]
Then, there exists a constant C′ = C′(δ,κ) such that
m m
f(s)s+ |s|p ≤ − |s|p+C′|s|2∗ for each |s| ≤ κ.
2 4
Using this with I (u) ≤ c and Ψ(u) ≥ 0, we get
λ
(cid:90) (cid:26) m (cid:27) m C′
c ≥ I (u) ≥ − F(u)+ |u|p ≥ ∥u∥p− ∥u∥2∗ .
λ 2p 4p p 2∗ 2∗

### Rn

Therefore, Kc is bounded in D1,2(Rn) and, by (29), in Y (Rn). ■
[a,b] m,p m,p
Property (Φ ) does not hold in Y (Rn) because of the translation invariance of Φ, and forces us
2 m,p
to restrict Ψ,Φ to suitable closed subspaces X (cid:44)→ Y (Rn) where (Φ ) is restored. Notice that any
m,p 2
of (Ψ ),(Ψ ),(Ψ ),(Φ ) is inherited by Ψ,Φ when restricted to any closed subspace X. Assume that a
1 2 3 1
topological group G acts continuously by isometries on Y (Rn) with an action · : G×X → X, and
m,p
define the subspace of G-invariant functions
Y (Rn) ≡ {u ∈ Y (Rn) | g·u = u for all g ∈ G}. (38)
m,p G m,p
Example 2.22. Let G be a closed subgroup of the isometry group Iso(Rn) of Rn, and consider the
natural action induced on Y (Rn) by defining (g·u)(x) ≡ u(g−1(x)). The action is continuous and, for
m,p
each g ∈ G, u → g·u is an isometry of Y (Rn).
m,p
In the present paper we shall focus for simplicity on the next two examples:
Example 2.23. Choosing in Example 2.22 the orthogonal group O(n) ≤ Iso(Rn) acting in the standard
way by matrix multiplication on Rn, we obtain the subspace of radially symmetric functions with respect
to the origin.
18

<!-- Page 19 -->

Example 2.24. For n and d ∈ N satisfying
n
n ≥ 4, 2 ≤ d ≤ , and n−2d ̸= 1, (39)
2
write a point of Rn as x = (x ,x ,x ) ∈ Rd×Rd×Rn−2d. Consider the subgroup
1 2 3

### H ≡ O(d)×O(d)×O(n−2d) ≤ O(n)

sitting in O(n) as block-diagonal matrices, and the action induced by that of Example 2.23 on Y (Rn).
m,p
Consideralsothediscretesubgroup⟨τ⟩generatedbytheinvolutionτ ∈ Iso(Rn),τ(x ,x ,x ) ≡ (x ,x ,x ),
1 2 3 2 1 3
and its action on Y (Rn) given by
m,p
(cid:0) (cid:1)
(τ ◦u)(x) ≡ −u τ(x) .
Then, τ induces an action on Y (Rn) , and (cid:0) Y (Rn) (cid:1) is the subspace of H-invariant functions
m,p H m,p H ⟨τ⟩
which are odd with respect to τ. To our knowledge, the idea of considering such symmetries to produce
non-radial solutions was first introduced in [8].
Following [66, §1.5], we describe a sufficient condition on a group G ≤ Iso(Rn), acting on Y (Rn) as
m,p
in Example 2.22, so that Φ restricted to Y (Rn) satisfies (Φ ). Let m(y,r,G) be the maximal number
m,p G 2
of disjoint balls of radius r centered at points in the G-orbit of y, namely:
(cid:40) (cid:12) (cid:41)
(cid:12) there exist g 1 ,...,g ℓ ∈ G such that
m(y,r,G) ≡ sup ℓ ∈ N (cid:12)
(cid:12)
(cid:12) B(g i y,r)∩B(g j y,r) = ∅ if i ̸= j.
The following property is proved in [46, Th´eor`eme III.4] (see also [66, §1.5]). We include the argument
for the sake of completeness.
Proposition 2.25. Let {u }∞ ⊂ Y (Rn) ∩D(Ψ) be bounded in Y (Rn), and assume that for some
k k=1 m,p G m,p
r > 0,
lim m(y,r,G) = ∞. (40)
|y|→∞
Then, there exists u ∈ Y (Rn) such that, up to a subsequence, ∥u −u∥ → 0 holds for any q ∈ (p,∞).
m,p G k q
Remark 2.26. A direct check shows that both of the groups O(n) in Example 2.23 and H in Example
2.24 satisfy (40).

### To prove Proposition 2.25, we need the following lemma:

Lemma 2.27. Let r > 0 and {u }∞ ⊂ D(Ψ) be a bounded sequence in Y (Rn). If
k k=1 m,p
(cid:90)
lim sup |u |p = 0,
k
k→∞y∈Rn B(y,r)
then u → 0 strongly in Lq(Rn) for any q ∈ (p,∞).
k
Proof. First, by (28) we know that {u } is bounded in L∞(Rn). Hence, replacing balls with cubes, our
k k
assumption implies that for each q ∈ [p,∞)
(cid:90)
lim sup |u |q = 0, where Q ≡ [0,1]n. (41)
k
k→∞y∈Rn y+Q
19

<!-- Page 20 -->

Moreover, in view of the L∞ bound and the interpolation inequality, it suffices to show that ∥u ∥ → 0
k q
for some q ∈ (p,p∗). By Sobolev’s embedding W1,p(Q) (cid:44)→ Lq(Q), we compute
∥u ∥q = (cid:88) (cid:90) |u |q ≤ (cid:32) sup (cid:90) |u |q (cid:33)1−p q (cid:88) (cid:18)(cid:90) |u |q (cid:19)p q
k q k k k
y∈Zn y+Q y∈Zn y+Q y∈Zn y+Q
(cid:32) (cid:33)1−p
≤ C sup (cid:90) |u |q q (cid:88) ∥u ∥p
0 k k W1,p(y+Q)
y∈Zn y+Q y∈Zn
(cid:32) (cid:33)1−p
(cid:90) q
= C sup |u |q ∥u ∥p .
0 k k W1,p(Rn)
y∈Zn y+Q
Becauseof (28)(i)andourassumptions,∥u ∥ isbounded,sotheconclusionfollowsfrom(41). ■
k W1,p(Rn)
Proof of Proposition 2.25. Let {u }∞ ⊂ Y (Rn) ∩D(Ψ) be bounded in Y (Rn). By Remark
k k=1 m,p G m,p
2.16, we can assume that u ⇀ u weakly in Y (Rn) and locally uniformly in Rn. The local uniform
k m,p
convergence guarantees that u ∈ Y (Rn) and that ∥Du∥ ≤ 1, whence u ∈ D(Ψ) by (31). Setting
m,p G ∞
v := u −u, the claim follows from Lemma 2.27 once we show that
k k
(cid:90)
lim sup |v |p → 0. (42)
k
k→∞y∈Rn B(y,r)
In fact, for y ∈ Rn, choose g ,...,g ∈ G so that {B(g y,r)} are pairwise disjoint. By (28) (i), in
1 m(y,r,G) i i
our assumptions ∥v ∥ ≤ C for some constant C. On the other hand,
k p
(cid:90) (cid:90)
C ≥ ∥v ∥p ≥ |v |p = m(y,r,G) |v |p.
k p k k
(cid:83)
i
m
=
(
1
y,r,G)B(giy,r) B(y,r)
Let ε > 0 be arbitrary. It follows from (40) that there exists R > 0 such that
ε
(cid:90)
sup |v |p < ε for all |y| ≥ R .
k ε
k≥1 B(y,r)
From v → 0 locally uniformly in Rn,
k
(cid:90)
lim sup |v |p = 0,
k
k→∞|y|≤Rε B(y,r)
which implies
(cid:90)
limsup sup |v |p ≤ ε.
k
k→∞ y∈Rn B(y,r)

### Thus, (42) holds by the arbitrariness of ε. ■

Proposition 2.28. Let G ≤ Iso(Rn) act on Y (Rn) as in Example 2.22, and assume that
m,p
lim m(y,r,G) = ∞ for some r > 0.
|y|→∞
Then, Φ : Y (Rn) → R satisfies (Φ ).
m,p G 2
20

<!-- Page 21 -->

Proof. Assumption (f1) and Lemma 2.18 guarantee that Φ ∈ C1(Y (Rn),R). Let
m,p
{u }∞ ⊂ Y (Rn) ∩D(Ψ)
k k=1 m,p G
be a bounded sequence. By Lemma 2.15 and Remark 2.16, up to a subsequence, we may assume that
u ⇀ u weakly in Y (Rn) and locally uniformly in Rn, and that ∥u ∥ ≤ c for some c > 0. We shall
k m,p k ∞ 0 0
prove that
liminfΦ′(u )(v−u ) ≥ Φ′(u)(v−u). (43)
k k
k→∞
Define
m
g(s) ≡ f(s)+ |s|p−2s.
2
For any fixed ε > 0, choose R > 0 so that ∥v∥ < ε. Since u → u uniformly in B , it holds

### Lp(Rn\BR) k R

(cid:90) (cid:90)
[Φ′(u )−Φ′(u)](v) = [g(u )−g(u)]v = o (1)+ [g(u )−g(u)]v
k k k k

### Rn Rn\BR

as k → ∞. On the other hand, by (f1) there exists a constant C such that |g(s)| ≤ C|s|p−1 for |s| ≤ c ,
0
hence
(cid:12) (cid:12)
(cid:12)(cid:90) (cid:12) (cid:16) (cid:17)
(cid:12) [g(u )−g(u)]v(cid:12) ≤ ∥g(u )∥ +∥g(u)∥ ∥v∥
(cid:12)
(cid:12) Rn\BR
k (cid:12)
(cid:12)
k
p−
p
1 p−
p
1

### Lp(Rn\BR)

(cid:16) (cid:17)
≤ C ∥u ∥p−1+∥u∥p−1 ∥v∥
2 k p p Lp(Rn\BR)
(cid:16) (cid:17)p−1
≤ C ε sup ∥u ∥ .
3 k k Ym,p
Therefore, letting first k → ∞ and then ε → 0, we deduce that Φ′(u )(v) → Φ′(u)(v) as k → ∞. Write
k
g(s)s = g (s)−g (s) where g (s) ≡ max{0,±g(s)s}. Then, (43) follows provided that
(cid:101)+ (cid:101)− (cid:101)±
(cid:90) (cid:90)
liminf (g (u )−g (u )) ≥ (g (u)−g (u)).
(cid:101)− k (cid:101)+ k (cid:101)− (cid:101)+
k→∞ Rn Rn

### We will prove that

(cid:90) (cid:90) (cid:90) (cid:90)
lim g (u ) = g (u), liminf g (u ) ≥ g (u). (44)
(cid:101)+ k (cid:101)+ (cid:101)− k (cid:101)−
k→∞ Rn Rn k→∞ Rn Rn
The second claim follows by Fatou’s lemma. As for the first, fix q > p and ε > 0. By (f1 ), there exists
m
C > 0 such that
ε,q,c0
g (u ) ≤ ε|u |p+C |u |q, g (u) ≤ ε|u|p+C |u|q.
(cid:101)+ k k ε,q,c0 k (cid:101)+ ε,q,c0
Because of Proposition 2.25, we can assume that lim ∥u −u∥ = 0, up to subsequence. Therefore,
k→∞ k q
we can fix R large enough so that
(cid:90)
C (|u |q +|u|q) < ε for all k ∈ N.
ε,q,c0 k

### Rn\BR

Since u → u in L∞(Rn), we compute
k loc
(cid:12)(cid:90) (cid:12) (cid:90)
(cid:12) (cid:12)
(cid:12) (g (cid:101)+ (u k )−g (cid:101)+ (u))(cid:12) ≤ o k (1)+ |g (cid:101)+ (u k )−g (cid:101)+ (u)|
(cid:12) Rn (cid:12) Rn\BR
(cid:90) (cid:90)
≤ o (1)+ε (|u |p+|u|p)+C (|u |q +|u|q)
k k ε,q,c0 k

### Rn\BR Rn\BR

(cid:16) (cid:17)
≤ o (1)+εC ∥u ∥p +∥u∥p +ε
k 3 k Ym,p Ym,p
≤ o (1)+C ε.
k 4
By letting k → ∞ and then ε → 0 we obtain the first in (44), concluding the proof. ■
21

<!-- Page 22 -->

Remark 2.29. By modifying the above argument, in the case m = 0 and if
(cid:16) (cid:17)
f(s) = o
|s|2∗−1
as s → 0,
one can actually show that
Φ′ : Y (Rn) ∩D(Ψ) −→ (cid:0) Y (Rn) (cid:1)∗

## 0 G 0

is compact, a stronger property than (Φ ).
2
We are ready to prove our main existence result.
Proof of Theorem 2.2. Firstofall,byusingProposition2.13andLemma2.15wededucethatanyweak
solution u ∈ Y (Rn) to (BI ) satisfies u ∈ W2,q(Rn) for each q ∈ [2,∞) and ∥Du∥ < 1. Referring to
m,p f loc ∞
Examples 2.23 and 2.24, we set for notational convenience
X ≡ Y (Rn) , X ≡ (cid:0) Y (Rn) (cid:1) . (45)
m,1 m,p O(n) m,2 m,p H ⟨τ⟩
In view of (29), to prove the result we shall construct:
• a positive solution u ∈ X with I(u) ∈ (0,∞);
m,1
• when f is odd, for each j ∈ {1,2}, infinitely many distinct solutions {u } ⊂ X with I(u ) ∈
k k m,j k
(0,∞) and I(u ) → ∞ as k → ∞ (provided n,d verify (14) when j = 2).
k
Define Ψ,Φ as in (30), and let
I ≡ λΨ−Φ : Y (Rn) → R.
λ m,p
Inourstatedassumptions,Lemmas2.17and2.18ensurethevalidityof(Ψ ),(Ψ ),(Ψ ),(Φ )onY (Rn).
1 2 3 1 m,p
In particular, from (Φ ) and the inclusion Y (Rn) (cid:44)→ D1,2(Rn), we can apply Proposition 2.19 and (a)
1 m,p m,p
in (29) to deduce that u ∈ Y (Rn) is a weak solution to (BI ) if and only if
m,p f
Ψ(v)−Ψ(u)−Φ′(u)(v−u) ≥ 0 for each v ∈ D(Ψ).
By the definition of Ψ, the above inequality also holds when ∥Dv∥ > 1 and thus weak solutions to
∞
(BI ) correspond to critical points of I = I in the sense of Szulkin.
f 1
The groups G = O(n),H, respectively, in Examples 2.23 and 2.24, are compact and act continuously
on Y (Rn), and ⟨τ⟩ acts continuously by isometries on Y (Rn) . Moreover, Y (Rn) is reflexive, thus
m,p m,p G m,p
so is Y (Rn) . Therefore, by the principle of nonsmooth symmetric criticality proved in [44, Theorem
m,p G
3.16] (see Proposition A.1 in Appendix A for another proof which does not require reflexivity) a function
u ∈ X is a critical point of I : Y (Rn) → R if and only if it is critical for the restriction of I to
m,j λ m,p λ
X , namely, if and only if
m,j
λ (cid:0) Ψ(v)−Ψ(u) (cid:1) −Φ′(u)(v−u) ≥ 0 for any v ∈ X .
m,j
Moreover, by Proposition 2.28 and Remark 2.26, Φ enjoys (Φ ) provided that we restrict its domain
2
to either X or to Y (Rn) in Example 2.24. In the second case (Φ ) is therefore inherited by the
m,1 m,p H 2
restriction of Φ to X . Lemma 2.21 guarantees that (IB) holds for I : X → R. In summary,
m,2 λ m,j
(Ψ ),(Ψ ),(Ψ ) and (Φ ),(Φ ),(IB) are satisfied. To apply Theorem 1.6 (respectively, Theorem 1.7 if f
1 2 3 1 2
isodd), itisthereforesufficienttochecktheuniformmountainpasscondition(MP)(respectively, (SMP))
for, say, λ ∈ [1/2,2].
In our assumptions, I (0) = 0 for each λ. Set ρ > 0 and consider u with ∥u∥ = ρ . By (28),
λ 0 Ym,p 0
there exists a constant C > 0 such that ∥u∥ ≤ Cρ . Hence, because of (f1), for each ε > 0 there exists
∞ 0
ρ such that the following inequality holds:
0
m
F(u)+ |u|p ≤ ε|u|p for any u ∈ Y (Rn) with ∥u∥ = ρ .
2p m Ym,p 0
22

<!-- Page 23 -->

Moreover, by using Remark 2.14,
m 1
Ψ(u) ≥ ∥u∥p+ ∥Du∥2.
4p p 2 2
We therefore have the following chain of inequalities for each λ ≥ 1/2:
1 (cid:90) (cid:18) m (cid:19)
I (u) ≥ Ψ(u)− F(u)+ |u|p
λ
2 2p

### Rn

(cid:18) (cid:19) (cid:18) (cid:19)
m 1 m 1
≥ −ε ∥u∥p+ ∥Du∥2 ≥ −ε ∥u∥p+c ∥u∥2 + ∥Du∥2,
4p p 4 2 4p p 1 2∗ 8 2
where in the last line Sobolev’s inequality was used. In both cases m = 0 (p = 2∗) and m > 0, by choosing
ε > 0 small enough and ρ accordingly there exists C > 0 such that
0 2
I (u) ≥ C ∥u∥p for each u ∈ Y (Rn) with ∥u∥ = ρ .
λ 2 D1,2 m,p Ym,p 0
m,p
Hence, by (29), there exists α > 0 such that I (u) ≥ α on {u | ∥u∥ = ρ } for each λ ≥ 1/2.
0 λ 0 Ym,p 0
(i) Property (MP).
In the radial case, we choose a radially symmetric function u ∈ C∞(Rn) such that
0 c
(cid:40)
t for |x| ≤ L,
0
u (x) ≡
0
0 for L+3t ≤ |x|
0
and ∥Du ∥ < 1/2, where t is the value in (f2). For sufficiently large L > 0, a direct computation
0 ∞ 0
gives I (u ) < 0, so (MP) holds.
2 0
(ii) Property (SMP).
Intheradialsetting, by[13,Theorem10], foreachk ∈ NthereexistR ,M independentofζ ∈ ∂Dk
k k
and odd maps
π ∈ C (cid:0) ∂Dk,H1 (Rn) (cid:1)
k rad
valued in the set H1 (Rn) of radial functions in H1(Rn) and satisfying
rad
(cid:90)
supp(π (ζ)) ⊂ B(0,R ), ∥Dπ (ζ)∥ ≤ M , F(π (ζ)) ≥ 1 for any ζ ∈ ∂Dk. (46)
k k k ∞ k k

### Rn

Define γ by
0,k
(cid:16)x(cid:17)
γ (ζ)(x) ≡ π (ζ) for L ≫ 1. (47)
0,k k

## L

Notice that for sufficiently large L, ∥Dγ (ζ)∥ ≤ M /L < 1. Thus, by using (29) and (28),
0,k ∞ k
π (∂Dk) is bounded in Y (Rn), hence in C(Rn). From the first in (46) and the dominated conk m,p
vergence theorem, one readily sees that γ ∈ C(∂Dk,X ), and by Remark 2.14
0,k m,1
(cid:90) (cid:16) (cid:113) (cid:17) (cid:90)
I (γ (ζ)) ≤ 2Ln 1− 1−M2/L2 −Ln F(π (ζ))
2 0,k k k
B(0,R ) Rn
k
(cid:20) M2 (cid:21)
≤ Ln 2 k|B(0,R )|−1 < 0,

### L2 k

which implies (SMP). Likewise, in dimension n ≥ 4 and for each 2 ≤ d ≤ n/2, in the argument
of [39, Lemma 4.3] the authors produced, for each k ∈ N, an odd map π ∈ C(∂Dk, (cid:0) H1(Rn) (cid:1) )
k H ⟨τ⟩
such that (46) holds for suitable M ,R independent of ζ. Defining again γ as in (47), the same
k k 0,k
computation as above yields π ∈ C(∂Dk,X ) and sup I (γ (ζ)) < 0, as required.
k m,2 ζ∈∂Dk 2 0,k
23

<!-- Page 24 -->

By applying Theorem 1.6 (resp. Theorem 1.7 if f is odd), we get all of our conclusions apart from the
claim that a positive solution in X can be found. To see this, we consider the problem with continuous
m,1
nonlinearity
(cid:40)
f(s) if s ≥ 0,
fˆ(s) =
−m|s|p−2s if s < 0.
Then, fˆsatisfies (f1 ) and (f2) since so does f, and therefore there exists a solution u ∈ X to
m,p m,1
(cid:32) (cid:33)

### Du

div +fˆ(u) = 0 in Rn.
(cid:112)
1−|Du|2
Moreover, by Proposition 2.10 and Lemma 2.15, u ∈ C1(Rn) and ∥Du∥ < 1. Assume that {u < 0} ≠ ∅.
∞
As in the proof of Theorem 2.2, we may use u (x) ≡ max{−u(x),0} ∈ Y (Rn) to deduce
− m,p
(cid:32) (cid:33)
(cid:90) |Du|2 (cid:90)
+m |u|p = 0,
(cid:112)
1−|Du|2
{u<0} {u<0}
a contradiction. Therefore, u ≥ 0 and thus u solves (BI ). The positivity of u follows from the weak
f
Harnack inequality (see [32, Theorem 8.18]) and the fact that u ≥ 0 satisfies
(cid:18) (cid:19)
f(u(x)) 1
0 = −div(aDu)−f(u(x)) ≤ −div(aDu)+ u(x), a(x) ≡ .
(cid:113)
u(x)
− 1−|Du(x)|2
This concludes the proof. ■
3 Deformation lemmas
The aim of this section is to prove general deformation lemmas in order to establish the monotonicity
method pioneered in [38,41,57,58] for the family {I } . The results below relate to [63, Proposition
λ λ
2.3]. Although our conclusions are slightly weaker, differently from [63] we do not require a priori the
validityofthePalais-Smalecondition(inthisrespect, seealso[1,Theorem3.1]). Letusrecallthatachief
difficulty in proving a deformation lemma for lower semicontinuous functionals is that the closure of a
relatively compact subset contained in a strip I−1([a,b]) may not lie in the same strip. This problem does
λ
not occur for continuous functionals as those treated in [27, Theorems 2.14 and 2.15] and [26, Theorem
2.3], and makes the construction of an energy decreasing flow which produces a bounded Palais-Smale
sequence a challenging task. Notice that in Lemmas 3.1 and 3.5 below, we allow I to increase along the
λ
flow in some regions, albeit in a controlled way.
We introduce some notation: for each λ > 0, we denote by K the set of all critical points of I :
λ λ
K ≡ {u ∈ X | u is a critical point of I }.
λ λ
Also, for a subset C ⊂ X, the symbol C stands for the closure of C in X. We shall prove two results, the
second one by assuming that Ψ,Φ are even.
3.1 The Deformation Lemma
Lemma 3.1. Suppose that (Ψ ) and (Φ ) hold. Fix λ ∈ R+ and let A ⊂ X be a closed and bounded set.
1 1
For c ∈ R and σ > 0, define
A ≡ A∩{c−3σ ≤ I ≤ c+3σ}.
c,3σ λ
24

<!-- Page 25 -->

Assume that there exists δ > 0 such that for each u ∈ A we may find v = v(u) ∈ X \{u} with
0 c,3σ
λ(Ψ(v)−Ψ(u))−Φ′(u)(v−u) < −5δ ∥v−u∥. (48)
0
Then for every set K ⊂ A
c,3σ
which is relatively compact in X there exist small neighborhoods W and W(cid:102)
of K with

### K ⊂ W ⊂ W ⊂ W(cid:102),

s > 0 and η ∈ C([0,∞)×X,X) such that
0
(i) ∥η(s,w)−w∥ ≤ s for (s,w) ∈ [0,∞)×X and η(s,w) = w for s ∈ [0,∞) if w ̸∈ W(cid:102);
(ii) I (η(s,w)) ≤ I (w)+δ s for all (s,w) ∈ [0,s ]×X;
λ λ 0 0
(iii) I (η(s,w)) ≤ I (w)−2δ s for all (s,w) ∈ [0,s ]×W with I (w) ≥ c−σ.
λ λ 0 0 λ
Remark 3.2. Since I is only assumed to be lower semicontinuous, the set A may not be closed and
λ c,3σ
its closure may possibly contain points in {I < c−3σ}. Consequently, (48) may fail at points of K\K,
λ
a major obstacle to construct an energy decreasing deformation flow. This marks one of differences with
the deformation in [63, Proposition 2.3], where it is assumed that the set K in Lemma 3.1 is compact.
Remark 3.3. Observe that Lemma 3.1 holds for a fixed λ ∈ R+, and it seems difficult to control the
deformation for I locally uniformly in λ. As a consequence, in the proof of Theorems 1.6 and 1.7
λ
Ekeland’s variational principle is hardly applicable, and we have to devise a different strategy based on
an iteration method.
Proof of Lemma 3.1. The following argument is adapted from the proof of [63, Lemma 2.2 and
Proposition 2.3]. Let K ⊂ A be relatively compact. Without loss of generality, we may suppose
c,3σ
δ < σ < 1. (49)
0
From the lower semicontinuity of I it follows that
λ
I (u) ≤ c+3σ for each u ∈ A . (50)
λ c,3σ
In particular, since K ⊂ A , the estimate in (50) holds on K.
c,3σ
We divide our arguments into several steps. In Step 1, we identify the building blocks to construct
a pseudogradient vector field in a neighborhood of K, namely, for each u ∈ K we find v = v(u) ∈ X
and a small radius r = r(u) such that, loosely speaking, for w ∈ B(u,r) the vector v − w acts as a
pseudogradient vector: the value of I does not increase too much with respect to I (w) in direction
λ λ
v−w, and decreases at least at a fixed rate whenever I (w) ≥ c−2σ. Notice that the choice v(u) in (48)
λ
is admissible (and works well) only if u ∈ A . However, as A is not closed, this is not always the
c,3σ c,3σ
case and the analysis for points u ∈ K\A is more involved.
c,3σ

### Step 1: The following hold:

(a) Suppose u ∈ K∩A and let v = v(u) ∈ X\{u} be as in (48). Then there exists r = r(u) > 0 such
c,3σ
that B(u,r) ⊂ A +B(0,1), v ̸∈ B(u,r) and
c,3σ
λ(Ψ(v)−Ψ(w))−Φ′(w)(v−w) ≤ −3δ ∥v−w∥ for all w ∈ B(u,r).
0
(cid:0) (cid:1)
(b) Suppose u ∈ K \A ∩K and set v ≡ u. Then there exists r = r(u) > 0 such that B(u,r) ⊂
c,3σ λ
A +B(0,1) and
c,3σ
δ
λ(Ψ(v)−Ψ(w))−Φ′(w)(v−w) ≤ 0 ∥v−w∥ for any w ∈ B(u,r).
2
In addition, if w ∈ B(u,r) satisfies I (w) ≥ c−2σ, then
λ
λ(Ψ(v)−Ψ(w))−Φ′(w)(v−w) ≤ −3δ ∥v−w∥.
0
25

<!-- Page 26 -->

(c) For each u ∈ K \ (A ∪K ), there exist v = v(u) ∈ X \ {u} and r = r(u) > 0 such that
c,3σ λ
B(u,r) ⊂ A +B(0,1), v ̸∈ B(u,r) and
c,3σ
δ
λ(Ψ(v)−Ψ(w))−Φ′(w)(v−w) ≤ 0 ∥v−w∥ for any w ∈ B(u,r).
2
In addition, if w ∈ B(u,r) satisfies I (w) ≥ c−2σ, then
λ
λ(Ψ(v)−Ψ(w))−Φ′(w)(v−w) ≤ −3δ ∥v−w∥.
0
Proof. To prove (a), let u ∈ K ∩A and v be as in (48). By the lower semicontinuity of Ψ and the
c,3σ
fact that v ̸= u, there exists r = r(u) > 0 such that B(u,r) ⊂ A +B(0,1), v ̸∈ B(u,r) and for all
c,3σ
w ∈ B(u,r)
λ(Ψ(v)−Ψ(w))−Φ′(w)(v−w) < −4δ ∥v−w∥.
0
Hence, (a) holds.
To prove (b) and (c), recall K ⊂ A and (50):
c,3σ
I (u) ≤ c+3σ for any u ∈ K.
λ
Therefore, if u ∈ K \A , then the closedness of A and the fact K ⊂ A yield u ∈ A and
c,3σ
I (u) < c−3σ. (51)
λ
(cid:0) (cid:1)
We prove (b). Let u ∈ K \A ∩K and put v ≡ u. By u ∈ K ,
c,3σ λ λ
λ(Ψ(w)−Ψ(v))−Φ′(v)(w−v) ≥ 0 for any w ∈ X.

### Thus,

λ(Ψ(v)−Ψ(w))−Φ′(w)(v−w) ≤ (Φ′(w)−Φ′(v))(w−v)
≤ ∥Φ′(w)−Φ′(v)∥ ∥w−v∥.
∗
By the continuity of Φ′, if r = r(u) > 0 is sufficiently small, then for any w ∈ B(u,r) ⊂ A +B(0,1)
c,3σ
δ
λ(Ψ(v)−Ψ(w))−Φ′(w)(v−w) ≤ 0 ∥w−v∥.
2
Hence, the first inequality in (b) holds.
When w ∈ B(u,r) satisfies I (w) ≥ c−2σ, by recalling (51) and writing I (u) = c−3σ −a with
λ λ u
some a > 0, it follows that
u
σ+a ≤ I (w)−I (u)
u λ λ
= λ(Ψ(w)−Ψ(u))+(Φ(u)−Φ(w))
(52)
(cid:90) 1
= λ(Ψ(w)−Ψ(u))+Φ′(w)(u−w)+ (cid:8) Φ′(w+θ(u−w))−Φ′(w) (cid:9) (u−w)dθ.
0
From the continuity of Φ′ at u, shrinking r = r(u) if necessary, we obtain
σ ≤ λ(Ψ(w)−Ψ(u))+Φ′(w)(u−w) for every w ∈ B(u,r) with I (w) ≥ c−2σ
λ
or equivalently,
λ(Ψ(u)−Ψ(w))−Φ′(w)(u−w) ≤ −σ for every w ∈ B(u,r) with I (w) ≥ c−2σ.
λ
26

<!-- Page 27 -->

Recalling that we have chosen v = u, up to further shrinking r = r(u) > 0 if necessary we infer
λ(Ψ(v)−Ψ(w))−Φ′(w)(v−w) ≤ −σ ≤ −3δ ∥v−w∥ for any w ∈ B(u,r) with I (w) ≥ c−2σ,
0 λ
which completes the proof of (b).
For (c), by u ̸∈ K we may find v = v(u) ∈ X \{u} and b > 0 such that
λ u
λ(Ψ(v)−Ψ(u))−Φ′(u)(v−u) = −2b < 0.
u
We claim that v can be chosen arbitrarily close to u. In fact, consider
v ≡ tv+(1−t)u t ∈ (0,1).
t
From the convexity of Ψ, it follows that
Ψ(v ) ≤ tΨ(v)+(1−t)Ψ(u)
t
and
λ(Ψ(v )−Ψ(u))−Φ′(u)(v −u) ≤ t (cid:8) λ(Ψ(v)−Ψ(u))−Φ′(u)(v−u) (cid:9) = −2b t < 0. (53)
t t u
For each t ∈ (0,1), there exists r > 0 such that B(u,r ) ⊂ A +B(0,1), v ̸∈ B(u,r ) and
t t c,3σ t t
δ
λ(Ψ(v )−Ψ(w))−Φ′(w)(v −w) < −b t ≤ 0 ∥v −w∥ for every w ∈ B(u,r ).
t t u t t
2
Thus, the first inequality in (c) holds.
Let w ∈ B(u,r ) satisfy I (w) ≥ c−2σ. Writing I (u) = c−3σ−a with a > 0, in a similar way
t λ λ u u
to obtain (52), we have
σ+a ≤ λ(Ψ(w)−Ψ(u))−Φ′(u)(w−u)+o(∥w−u∥).
u
By shrinking r > 0 if necessary, we get
t
σ ≤ λ(Ψ(w)−Ψ(u))−Φ′(u)(w−u) for all w ∈ B(u,r ) with I (w) ≥ c−2σ. (54)
t λ
Hence, (53) and (54) imply
λ(Ψ(v )−Ψ(w))−Φ′(w)(v −w)
t t
= λ{Ψ(v )−Ψ(u)+Ψ(u)−Ψ(w)}−Φ′(w)(v −w)+Φ′(u)(w−u)−Φ′(u)(w−u)
t t
≤ λ(Ψ(v )−Ψ(u))−Φ′(w)(v −w)−Φ′(u)(w−u)−σ
t t
< Φ′(u)(v −u)−Φ′(w)(v −w)−Φ′(u)(w−u)−σ
t t
= (cid:0) Φ′(u)−Φ′(w) (cid:1) (v −w)−σ
t
≤ ∥Φ′(u)−Φ′(w)∥ ∥v −w∥−σ
∗ t
(cid:26) (cid:27)
σ
= ∥Φ′(u)−Φ′(w)∥ − ∥v −w∥.
∗ t
∥v −w∥
t
Since t ∈ (0,1) is arbitrary and we may take a smaller r , for sufficiently small t and r , we get
t t
λ(Ψ(v )−Ψ(w))−Φ′(w)(v −w) ≤ −3δ ∥v −w∥ for each w ∈ B(u,r ) with I (w) ≥ c−2σ
t t 0 t t λ
and (c) holds. ■
27

<!-- Page 28 -->

To proceed, since K is compact and Φ′ ∈ C(X,X∗), there exists r > 0 such that
1
sup (cid:8)(cid:13) (cid:13)Φ′(v)−Φ′(u) (cid:13) (cid:13) ∗ (cid:12) (cid:12) u ∈ K, ∥v−u∥ ≤ r 1 (cid:9) ≤ δ 4 0 . (55)
Step 2: Construction of η.
Proof. For each u ∈ K, we have v = v(u) and B(u,r) as in Step 1. Since r = r(u) can be taken small,
we may suppose
r r
1 1
r(u) ≤ , that is, ∥u−w∥ ≤ for all w ∈ B(u,r(u)),
2 2
(cid:83)
with r as in (55). Using the compactness of K, from K ⊂ B(u,r(u)) we infer the existence of
1 u∈K
finitely many distinct points u ,...,u ∈ K so that
1 k
k k
(cid:91) (cid:0) (cid:1) r 1 (cid:91)
K ⊂ B(u ,R ), dist K,w ≤ for all w ∈ B(u ,R ),
i i i i
2
i=1 i=1
where we write R ≡ r(u ). We also use the symbol v = v(u ). Since the u ’s are finite, we may find
i i i i i
r ∈ (0,r ) such that
0 1
B(u ,2r ) ⊂ B(u ,R ) for 1 ≤ i ≤ k,
i 0 i i
B(u ,2r )∩B(u ,2r ) = ∅ for each i,j ∈ {1,...,k} with i ̸= j.
i 0 j 0

### Put

(cid:91)
V ≡ B(u ,R )\ B(u ,r ) for i = 1,...,k,
i i i j 0
j∈{1,...,k},j̸=i
and define
k
(cid:91)
W(cid:102) ≡ V
i
.
i=1
From the definition of V and the choice of r ∈ (0,r ), we observe that
i 0 1
(cid:0) (cid:1) r 1
B(u
i
,2r
0

## ) ⊂ V

i
(1 ≤ i ≤ k), dist K,w ≤ for any w ∈ W(cid:102),
2
k (56)
(cid:91) (cid:16) (cid:17)
K(cid:101) ≡ K ∪ B(u
i
,r
0
) ⊂ W(cid:102), 0 < dist K(cid:101), ∂W(cid:102) .
i=1
Notice that the last property in (56) follows from
(cid:32) k (cid:33)
(cid:16) (cid:17) (cid:91)
dist K, ∂W(cid:102) > 0, dist B(u
i
,r
0
), ∂W(cid:102) > 0.
i=1
Moreover, by the very definition of V ,
j
B(u ,r )∩V = ∅ for each i,j ∈ {1,...,k} with i ̸= j. (57)
i 0 j

### For ε > 0, write

V ≡ {x ∈ V | dist(x,Vc) > ε} for i = 1,...,k.
i,ε i i
28

<!-- Page 29 -->

From (56), there exists ζ > 0 such that
0
k
(cid:91)
B(u
i
,r
0

## ) ⊂ V

i,3ζ0
for 1 ≤ i ≤ k, K(cid:101) ⊂ V
i,3ζ0

## ≡ W

1
.
i=1
We also set
k k
(cid:91) (cid:91)

## W

2

## ≡ V

i,2ζ0

## , W

3

## ≡ V

i,ζ0

## , W

4
≡ W(cid:102).
i=1 i=1

### Then,

W ⊂ W and dist(W ,X \W ) > 0 (1 ≤ j ≤ 3).
j j+1 j j+1

### Define

V ≡ X \W , V ≡ X \W .
0 1 0,ζ0 2
It is easily seen that
k
(cid:0) (cid:1) (cid:91) (cid:0) (cid:1)
X = X \W ∪W = V , dist(V , X \V ) = dist W ,X \W > 0.
2 3 i,ζ0 0,ζ0 0 1 2
i=0
Furthermore, from K(cid:101) ⊂ W
1
, it follows that
V ∩B(u ,r ) = ∅ (1 ≤ i ≤ k). (58)
0 i 0
For i = 0,...,k, pick ρ ∈ C(X,R) so that
(cid:101)i
0 < ρ on V , suppρ ⊂ V , dist(suppρ , X \V ) > 0
(cid:101)i i,ζ0 (cid:101)i i (cid:101)i i
and set
ρ (w)
ρ (w) ≡
(cid:101)i
.
i (cid:80)k
ρ (w)
j=0 (cid:101)j
Then for each i = 0,1,...,k,
k
(cid:88)
ρ ∈ C(X,[0,1]), ρ = 1 on X, suppρ ⊂ V , dist(suppρ ,X \V ) > 0. (59)
i i i i i i
i=0
In particular, ρ = 0 on X \W for every i = 1,...,k.
i 4
To define η(s,w), we consider the decomposition {1,...,k} = J ∪J , where
1 2
J ≡ {i | u ∈ K }, J ≡ {1,...,k}\J . (60)
1 i λ 2 1
By the definition of v and by Step 1,
i
v = u if i ∈ J , v ̸∈ V if i ∈ J . (61)
i i 1 i i 2
For any i ∈ J , we define η ∈ C([0,∞)×X,X) by
1 i
 (cid:20) (cid:21)
v −w
 ρ (w) w+s i if 0 ≤ s < ∥v −w∥,
i i
η i (s,w) ≡ ∥v i −w∥

ρ (w)v if s ≥ ∥v −w∥.
i i i
29

<!-- Page 30 -->

On the other hand, for i ∈ J we put
2
(cid:20) (cid:21)
v −w
i
η (s,w) ≡ ρ (w) w+s .
i i
∥v −w∥
i
By (61), v ̸∈ V ⊃ suppρ , so setting η (s,w) = 0 for w = v yields a continuous map η ∈ C([0,∞)×
i i i i i i
X,X). Finally, for i = 0, define
η (s,w) ≡ ρ (w)w ∈ C([0,∞)×X,X).
0 0
Using these η ’s, we define η(s,w) by
i
k
(cid:88)
η(s,w) ≡ η (s,w) ∈ C([0,∞)×X,X)
i
i=0
and set
k
(cid:91)

## W ≡ W = V .

1 i,3ζ0
i=1
Remark that W is an open set satisfying K ⊂ W ⊂ W ⊂ W(cid:102). Then, we shall prove that η, W and W(cid:102)
satisfy (i)–(iii) in Lemma 3.1. ■
Step 3: η satisfies (i)–(iii).
Proof. We first prove (i). Notice that for each (s,w) ∈ [0,∞)×X and i ∈ J ∪{0},
2
∥η (s,w)−ρ (w)w∥ ≤ ρ (w)s.
i i i
When i ∈ J , if ρ (w) > 0 and 0 ≤ s < ∥v −w∥, then
1 i i
∥η (s,w)−ρ (w)w∥ ≤ ρ (w)s.
i i i
On the other hand, if i ∈ J , ρ (w) > 0 and s ≥ ∥v −w∥, then
1 i i
∥η (s,w)−ρ (w)w∥ ≤ ρ (w)∥v −w∥ ≤ ρ (w)s.
i i i i i
Combining these estimates, we observe that for every (s,w) ∈ [0,∞)×X,
k k
(cid:88) (cid:88)
∥η(s,w)−w∥ ≤ ∥η (s,w)−ρ (w)w∥ ≤ sρ (w) = s.
i i i
i=0 i=0
Thus, the first assertion in (i) holds.
Regarding the second assertion in (i), from the definition of W(cid:102) and (59), it follows that if w ̸∈ W(cid:102),
then ρ (w) = 0 for every j = 1,...,k and ρ (w) = 1. Therefore, η(s,w) = ρ (w)w = w holds for any
j 0 0
(s,w) ∈ [0,∞)×(X \W(cid:102)), as claimed.
It remains to prove (ii) and (iii). Without loss of generality, we may assume w ∈ W(cid:102). We split the
proof into two cases:
First case: assume that
(cid:91)
w ∈ B(u ,r ),
i 0
i∈J1
30

<!-- Page 31 -->

where J is as in (60). Choose an index i ∈ J for which w ∈ B(u ,r ). In this case, by B(u ,r ) ⊂
1 0 1 i0 0 i0 0
V , (57), (58) and (59), we remark that ρ (w) = 0 for any j ∈ {0,...,k} with j ̸= i , hence
i0,3ζ0 j 0
ρ (w) = 1, η(s,w) = η (s,w). (62)
i0 i0
Also, u ∈ K and v = u by (61).
i0 λ i0 i0
If w = v , then by definition we have η (s,w) = w for any s ≥ 0. Also, we claim that I (w) < c−3σ,
i0 i0 λ
which directly implies (ii) and there is nothing to prove for (iii). Indeed, otherwise, by combining (50),
w = v ∈ K ∩ K and the closedness of A, from K ⊂ A we would deduce w ∈ A ∩ {c − 3σ ≤ I ≤
i0 λ λ
c+3σ} = A , which violates (48).
c,3σ
Assumethereforethatw ∈ B(u ,r )\{u }. FromStep1andthedefinitionofη ,if0 ≤ s ≤ ∥w−v ∥,
i0 0 i0 i0 i0
then
s
η(s,w) = η (s,w) = (1−τ )w+τ v where τ = τ (s,w) ≡ ≤ 1
i0 i0 i0 i0 i0 i0
∥w−v ∥
i0
and by the convexity of Ψ,
I (η(s,w)) ≤ λ(1−τ )Ψ(w)+λτ Ψ(v )−Φ(η (s,w))
λ i0 i0 i0 i0
= I (w)+Φ(w)+τ λ(Ψ(v )−Ψ(w))−Φ(η (s,w)).
λ i0 i0 i0
Notice that by v = u ∈ K ∩K, τ ≤ 1 and r < r , on the segment
i0 i0 λ i0 0 1
[0,1] ∋ θ (cid:55)→ w ≡ w+(1−θ)τ (v −w),
θ i0 i0
it holds
∥w −v ∥ = {1−(1−θ)τ }∥w−v ∥ ≤ r < r for any θ ∈ [0,1].
θ i0 i0 i0 0 1

### From (55), we get

(cid:90) 1 d (cid:90) 1
Φ(w)−Φ(η (s,w)) = Φ(w )dθ = −τ (v −w) Φ′(w )dθ
i0
dθ
θ i0 i0 θ
0 0
(cid:26) (cid:90) 1 (cid:27)
= −(τ (v −w)) Φ′(w)+ (cid:2) Φ′(w )−Φ′(v )+Φ′(v )−Φ′(w) (cid:3) dθ .
i0 i0 θ i0 i0
0
≤ −τ
i0
Φ′(w)(v
i0
−w)+2τ
i0
∥v
i0
−w∥ max (cid:13) (cid:13)Φ′(w
θ
)−Φ(v
i0
) (cid:13) (cid:13).
θ∈[0,1]
δ
≤ −τ Φ′(w)(v −w)+ 0 τ ∥v −w∥
i0 i0
2
i0 i0
δ
= −τ Φ′(w)(v −w)+ 0 s.
i0 i0
2
This implies that for all w ∈ B(u ,r )\{u } (i ∈ J ) and s ∈ [0,∥v −w∥],
i0 0 i0 0 1 i0
I (η(s,w)) ≤ I (w)+τ (cid:2) λ{Ψ(v )−Ψ(w)}−Φ′(w)(v −w) (cid:3) + δ 0 s. (63)
λ λ i0 i0 i0
2
Recalling τ ≤ 1 and Step 1 (b), we observe that for every w ∈ B(u ,r ) \ {u } ⊂ V and s ∈
i0 i0 0 i0 i0
[0,∥v −w∥],
i0
δ δ
0 0
I (η(s,w)) ≤ I (w)+τ ∥v −w∥+ s = I (w)+δ s. (64)
λ λ i0
2
i0
2
λ 0
Finally, if s > ∥v −w∥, then η(s,w) = η (s,w) and the definition of η yield
i0 i0 i0
I (η(s,w)) = I (η(∥v −w∥,w)) ≤ I (w)+δ ∥v −w∥ ≤ I (w)+δ s.
λ λ i0 λ 0 i0 λ 0
In conclusion, (ii) is verified for all (s,w) ∈ [0,∞)×B(u ,r ) with i ∈ J .
i0 0 0 1
31

<!-- Page 32 -->

To check (iii), let w ∈ B(u ,r )\{u } satisfy I (w) ≥ c−σ. For any s ∈ [0,∥v −w∥], and taking
i0 0 i0 λ i0
into account the definition of τ , Step 1 (b) and (63) imply
i0
δ
0
I (η(s,w)) ≤ I (w)−τ 3δ ∥v −w∥+ s ≤ I (w)−2δ s.
λ λ i0 0 i0
2
λ 0
On the other hand, when ∥v −w∥ < s, it follows from I (v ) < c−3σ that
i0 λ i0
I (η(s,w)) = I (v ) < c−3σ ≤ I (w)−2σ.
λ µ i0 λ
Since δ < σ holds due to (49), if ∥v −w∥ < s ≤ 1, then
0 i0
I (η(s,w)) < I (w)−2δ s.
λ λ 0
Hence, for every (s,w) ∈ [0,1]×B(u ,r ) with i ∈ J and I (w) ≥ c−σ,
i0 0 0 1 λ
I (η(s,w)) ≤ I (w)−2δ s.
λ λ 0
(cid:83)
Thus, (iii) holds on [0,1]× B(u ,r), too.
i∈J1 i
Second case: assume that
(cid:91)
w ∈ W(cid:102)\ B(u
i
,r
0
).
i∈J1
By the definition of η , for any s ∈ [0,r /2] (so that s < ∥w−v ∥ for each i ∈ J ) we have
i 0 i 1
k k
(cid:88) v j −w (cid:88) v j −w
η(s,w) = w+s ρ (w) = w+sx, x ≡ ρ (w) , ∥x∥ ≤ 1. (65)
j j
∥v −w∥ ∥v −w∥
j j
j=1 j=1
Moreover, it follows from (59) and the second in (61) that
dist(v ,suppρ ) > 0 for every j ∈ J .
j j 2
Also, since v = u for all j ∈ J , we may choose s ∈ (0,r /2) so that
j j 1 1 0
k
(cid:88) ρ j (w) (cid:91)
s ≤ 1 for every s ∈ [0,s
1
] and w ∈ W(cid:102)\ B(u
i
,r
0
).
∥v −w∥
j
j=1 i∈J1
The inequality can be rewritten as
k
(cid:88) ρ j (w)
τ (s,w) ≤ 1, τ (s,w) ≡ s for each 1 ≤ j ≤ k,
j j
∥v −w∥
j
j=1
so that
 
k k
(cid:88) (cid:88)
η(s,w) = 1− τ jw+ τ
j
v
j
.
j=1 j=1
From the convexity of Ψ, we infer
  
k k
(cid:88) (cid:88)

## I

λ
(η(s,w)) ≤ λ1− τ jΨ(w)+ τ
j
Ψ(v
j
)−Φ(η(s,w))
j=1 j=1
(66)
k
(cid:88)
= I (w)+ τ {λ(Ψ(v )−Ψ(w))}+Φ(w)−Φ(η(s,w)).
λ j j
j=1
32

<!-- Page 33 -->

We shall estimate the term Φ(w)−Φ(η(s,w)). Since w ∈ W(cid:102), dist(w,K) ≤ r
1
/2 holds due to (56). The
compactness of K implies that there exists y ∈ K such that
w
r
1
∥w−y ∥ ≤ .
w
2
Therefore, if 0 ≤ s ≤ s and θ ∈ [0,1], then by s < r /2 < r /2,
1 1 0 1
r
1
∥w+(1−θ)sx−y ∥ ≤ +s < r .
w 1
2
By (65) and (55), for every s ∈ [0,s ] we have
1
(cid:90) 1 d
Φ(w)−Φ(η(s,w)) = Φ(w+(1−θ)sx)dθ
dθ
0
(cid:90) 1
= −Φ′(w)sx+ (cid:0) Φ′(w+(1−θ)sx)−Φ′(w) (cid:1) (−sx)dθ
0
(cid:90) 1
= −Φ′(w)sx+ (cid:0) Φ′(w+(1−θ)sx)−Φ′(y ) (cid:1) (−sx)dθ
w
0
(cid:90) 1
+ (cid:0) Φ′(y )−Φ′(w) (cid:1) (−sx)dθ
w
0
k
≤ −Φ′(w)sx+ δ 0 s = − (cid:88) τ Φ′(w)(v −w)+ δ 0 s.
j j
2 2
j=1
Plugging into (66), for s ∈ [0,s ] we get
1
k
I (η(s,w)) ≤ I (w)+ (cid:88) τ (cid:8) λ(Ψ(v )−Ψ(w))−Φ′(w)(v −w) (cid:9) + δ 0 s. (67)
λ λ j j j
2
j=1
Notice that if τ > 0 for some j = 1,...,k, then w ∈ V and thus Step 1 gives
j j
k k
(cid:88) δ 0 δ 0 (cid:88) δ 0 δ 0
I (η(s,w)) ≤ I (w)+ τ ∥v −w∥+ s = I (w)+ ρ (w) s+ s ≤ I (w)+δ s.
λ λ j j λ j λ 0
2 2 2 2
j=1 j=1
(cid:16) (cid:17)
(cid:83)
This concludes the proof of (ii) whenever (s,w) ∈ [0,s
1
]× W(cid:102)\
i∈J1
B(u
i
,r
0
) .
To check the validity of (iii), assume that
(cid:91)
w ∈ W \ B(u ,r ), I (w) ≥ c−σ.
i 0 λ
i∈J1
SinceW ≡ W andV ∩W = ∅,(59)yieldsρ (w) = 0. Thus,from(67)andStep1itfollows
(cid:80)k
ρ (w) =
1 0 0 j=1 j
1 and
k
(cid:88) δ 0
I (η(s,w)) ≤ I (w)+ τ (−3δ ∥v −w∥)+ s
λ λ j 0 j
2
j=1
k
(cid:88) δ 0
= I (w)−3δ ρ (w)s+ s ≤ I (w)−2δ s
λ 0 j λ 0
2
j=1
for each s ∈ [0,s ], and (iii) holds. We have thus shown properties (ii) and (iii) in all cases. ■
1
From Step 3, by choosing s ≡ min{s ,1}, all the conclusions in Lemma 3.1 hold and we complete
0 1
the proof. ■
33

<!-- Page 34 -->

3.2 Symmetric Deformation Lemma
Throughout this subsection we assume condition (E), which is defined as
Ψ(−u) = Ψ(u), Φ(−u) = Φ(u) for any u ∈ X.
For a subset A ⊂ X, we say that A is symmetric if −A = A holds, where −A ≡ {x ∈ X | −x ∈ A}.
Remark 3.4. Under (E) and (Φ ), it is easily seen that Φ′(0) = 0. Moreover, if Ψ satisfies (Ψ ), then
1 1
by Ψ(u) ≥ 0 = Ψ(0) for every u ∈ X, we infer that 0 is a critical point of I .
λ
To establish multiplicity results for even functionals, we need to construct an odd deformation which
is the counterpart of Lemma 3.1.
Lemma 3.5 (Symmetric Deformation Lemma). Assume that (Ψ ), (Φ ) and (E) hold. Fix λ ∈ R+ and
1 1
let A ⊂ X be a bounded, closed and symmetric set and for c ∈ R and σ > 0, define
A ≡ A∩{c−3σ ≤ I ≤ c+3σ}.
c,3σ λ
Suppose that there exists δ > 0 such that for each u ∈ A we may find v = v(u) ∈ X \{u} with
0 c,3σ
λ(Ψ(v)−Ψ(u))−Φ′(u)(v−u) < −5δ ∥v−u∥. (68)
0
Then for every relatively compact and symmetric set K ⊂ A there exist symmetric neighborhoods W
c,3σ
and W(cid:102) of K with

### K ⊂ W ⊂ W ⊂ W(cid:102),

s > 0 and η ∈ C([0,∞)×X,X) such that
0
(i) ∥η(s,w)−w∥ ≤ s and η(s,−w) = −η(s,w) for all (s,w) ∈ [0,∞)×X, and η(s,w) = w for all
s ∈ [0,∞) if w ̸∈ W(cid:102);
(ii) I (η(s,w)) ≤ I (w)+δ s for all (s,w) ∈ [0,s ]×X;
λ λ 0 0
(iii) I (η(s,w)) ≤ I (w)−2δ s for all (s,w) ∈ [0,s ]×W with I (u) ≥ c−σ.
λ λ 0 0 λ
Proof. We follow the same scheme as in the proof of Lemma 3.1, just pointing out the differences needed
to get the oddness of the deformation flow.
By (E), notice that A is symmetric, namely u ∈ A yields −u ∈ A . Therefore, for every
c,3σ c,3σ c,3σ
u ∈ A , (68) and (E) imply
c,3σ
λ(Ψ(−v)−Ψ(−u))−Φ′(−u)(−v−(−u)) < −5δ ∥−v−(−u)∥.
0
For each u ∈ A , by defining v(u) ≡ {v(u)−v(−u)}/2, we see from (E), (68) and the convexity of Ψ
c,3σ (cid:101)
that
λ(Ψ(v(u))−Ψ(u))−Φ′(u)(v(u)−u) ≤ 1 (cid:2) λ{Ψ(v(u))−Ψ(u)}−Φ′(u)(v(u)−u) (cid:3)
(cid:101) (cid:101)
2
+ 1 (cid:2) λ{Ψ(v(−u))−Ψ(−u)}−Φ′(−u)(v(−u)−(−u)) (cid:3)
2
1 1
< (−5δ ∥v(u)−u∥)+ (−5δ ∥v(−u)−(−u)∥)
0 0
2 2
≤ −5δ ∥v(u)−u∥.
0 (cid:101)
Remark that v(u) ̸= u since the second-last inequality is strict. Thus, we may assume that v is odd with
(cid:101)
respect to u ∈ X.
34

<!-- Page 35 -->

For Step 1 in the proof of Lemma 3.1, we remark that K and K are symmetric. Therefore, in (a)
λ
and (b), we can take v(u) and r(u) so that v(−u) = −v(u) and r(−u) = r(u), and prove Step 1 (a) and
(b). For Step 1 (c), if v ∈ X \{u} satisfies
λ(Ψ(v)−Ψ(u))−Φ′(u)(v−u) = −2b < 0,
u
then (E) gives
λ(Ψ(−v)−Ψ(−u))−Φ′(−u)(−v−(−u)) = −2b < 0.
u
Hence, following the proof of Step 1 (c), we can see that the claim in (c) holds with v(−u) = −v(u) and
r(−u) = r(u).
Since K is symmetric and compact, we notice that there are u ,...,u ∈ K such that by setting
1 k
u = 0 when 0 ∈ K,
k+1

k
(cid:91)
  {B(u ,r(u ))∪B(−u ,r(u ))} if 0 ̸∈ K,
 i i i i


i=1

## K ⊂

k
  (cid:91)
   B(u k+1 ,r(0))∪ {B(u i ,r(u i ))∪B(−u i ,r(u i ))} if 0 ∈ K.

i=1
Write u ≡ −u for 1 ≤ j ≤ k+1 and R ≡ r(u ) for 1 ≤ |i| ≤ k+1, and when 0 ̸∈ K define
−j j i i
(cid:91)
V ≡ B(u ,R )\ B(u ,r ) for 1 ≤ |i| ≤ k
i i i j 0
1≤|j|≤k,j̸=i
and when 0 ∈ K,
(cid:91) (cid:91)
V ≡ B(u ,R )\ B(u ,r ) for 1 ≤ |i| ≤ k, V ≡ B(0,R )\ B(u ,r ).
i i i j 0 k+1 k+1 j 0
1≤|j|≤k+1,j̸=i 1≤|j|≤k
In any case, we have
(cid:91) (cid:91)
V = −V for 1 ≤ j ≤ k, −V = V , − V = V .
−j j k+1 k+1 i i
1≤|i|≤k 1≤|i|≤k
Arguing as in the proof of Step 2 of Lemma 3.1, we may find (ρ ) (resp. (ρ ) and ρ )
(cid:101)i 1≤|i|≤k (cid:101)i 1≤|i|≤k (cid:101)k+1
such that 0 < ρ on V , suppρ ⊂ V , ρ (u) = ρ (−u) for 1 ≤ j ≤ k, ρ (−u) = ρ (u) and
(cid:101)i i,ζ0 (cid:101)i i (cid:101)−j (cid:101)j (cid:101)k+1 (cid:101)k+1
ρ (−u) = ρ (u). From this family of functions, we construct the partition of unity (ρ ) (resp.
(cid:101)0 (cid:101)0 i 1≤|i|≤k
(ρ ) and ρ ) as before.
i 1≤|i|≤k k+1

### To define η(s,u), consider

J ≡ {i | 1 ≤ |i| ≤ k, u ∈ K } (resp. {i | 1 ≤ |i| ≤ k or i = k+1, u ∈ K }),
1 i λ i λ
J ≡ {−k,...,−1,1,...,k}\J .
2 1
We remark that k +1 ∈ J if 0 ∈ K and see from the properties of V that for 1 ≤ j ≤ k, j ∈ J if
1 i 1
and only if −j ∈ J . Defining η (s,u) and η(s,u) as in Step 2, we see that η (s,u) = −η (s,−u) for
1 i −j j
1 ≤ j ≤ k, η (s,−u) = −η (s,u) and η (s,−u) = −η (s,u), hence η(s,−u) = −η(s,u).
k+1 k+1 0 0
The rest of the argument is unchanged compared to the proof of Lemma 3.1. ■
35

<!-- Page 36 -->

4 Proof of Theorem 1.6 and Theorem 1.7
In the proof of of Theorems 1.6 and 1.7 we assumed (IB), that is, the boundedness of the set of critical
points Kc for each [a,b] ⊂ (0,∞) and c ∈ R. As a matter of fact, under the further validity of
[a,b]
(Ψ ),(Ψ ),(Φ ) and (Φ ) a stronger property holds: Kc is compact. More precisely, we prove the next
1 3 1 2 [a,b]
Proposition 4.1. Suppose that (Ψ ),(Ψ ),(Φ ),(Φ ) hold. Assume that there exist c ∈ R and sequences
1 3 1 2
{ε },{λ } ⊂ (0,∞) and {u } ⊂ X with
j j j
ε → 0, λ → λ ∈ (0,∞), u ⇀ u weakly in X as j → ∞
j j j
and
λ (Ψ(v)−Ψ(u ))−Φ′(u )(v−u ) ≥ −ε ∥v−u ∥ for each v ∈ X.
j j j j j j

### Then,

lim ∥u −u∥ = 0, u is critical for I , I (u) = lim I(u ) ∈ R. (69)
j λ λ j
j→∞ j→∞

### In particular, in the stated assumptions,

- for each λ ∈ (0,∞) and c ∈ R, I satisfies the bounded Palais-Smale condition at level c, namely
λ
any bounded Palais-Smale sequence for I at level c has a strongly convergent subsequence in X;
λ
- property (IB) implies that the set Kc is compact for each [a,b] ⊂ (0,∞) and c ∈ R.
[a,b]
Proof. We first claim that u ∈ D(Ψ) and u is a critical point of I . Remark that the sequence {u }
λ j
is bounded in X due to the weak convergence. Hence, up to passing to a subsequence, we can assume
that {u } itself satisfies the conclusion in (Φ ). Having fixed v ∈ D(Ψ) and ε ∈ (0,λ), we select j large
j 2 0
enough so that λ > λ−ε for j ≥ j . Since Ψ ≥ 0, if j ≥ j , then we get
j 0 0
λ Ψ(v)−(λ−ε)Ψ(u )−Φ′(u )(v−u ) ≥ λ (Ψ(v)−Ψ(u ))−Φ′(u )(v−u )
j j j j j j j j
≥ −ε ∥v−u ∥ ≥ −Cε
j j j
for some constant C. Taking a limsup as j → ∞ and using (Ψ ) and (Φ ), we infer
1 2
λΨ(v)−(λ−ε)Ψ(u)−Φ′(u)(v−u) ≥ 0 for every v ∈ X.
Hence, Ψ(u) < ∞, and letting ε → 0 we deduce that u is critical for I .
λ
Next, taking the limsup as j → ∞ in the inequality
λ Ψ(u)−Φ′(u )(u−u ) ≥ ε ∥u−u ∥+λ Ψ(u )
j j j j j j j
and using (Φ ) we get limsup Ψ(u ) ≤ Ψ(u). Since Ψ is weakly lower-semicontinuous, it follows that
2 j→∞ j
lim Ψ(u ) = Ψ(u) and thus, by (Ψ ), lim ∥u −u∥ = 0. Hence, by (Φ ), I (u) = lim I (u ),
j→∞ j 3 j→∞ j 1 λ j→∞ λj j
which completes the proof of (69).
To check the bounded Palais-Smale condition, it is enough to extract from a bounded Palais-Smale
sequence {u } at level c a weakly convergent subsequence u ⇀ u by using (Φ ). Applying the above, u
j j 2 j
converges strongly to u, as claimed.
Similarly,if(IB)holds,thenpickanyboundedsequence{u } ⊂ Kc . Becauseof(Φ ),wecanextract
j [a,b] 2
a weakly convergent subsequence and, up to further subsequences, we can assume that λ → λ ∈ [a,b]
j
and u ⇀ u weakly in X as j → ∞. The above guarantees that u → u strongly in X and that u ∈ Kc .
j j [a,b]
Hence, Kc is compact. ■
[a,b]
To proceed, we collect some basic properties of c (λ),k = 0,1,2..., defined in (4) and (5). We first
k
show
36

<!-- Page 37 -->

Lemma4.2. If (MP), (Ψ )and(Φ )hold, thenΓ ̸= ∅and0 < α ≤ c (λ) < ∞foreachλ ∈ [1−ε,1+ε].
1 1 0 0 0
Similarly, Γ ̸= ∅ and α ≤ c (λ) < ∞ hold for every k ≥ 1 and λ ∈ [1−ε,1+ε] under (SMP), (Ψ )
k 0 k 1
and (Φ ).
1
Proof. For Γ and c (λ), consider a path γ (t) ≡ tu (t ∈ [0,1]) where u appears in (MP). It is easily
0 0 0 0 0
seen that γ ∈ Γ , and (Ψ ) and I (u ) ≤ 0 yield u ∈ D(Ψ) and
0 0 1 1+ε 0 0
0 ≤ Ψ(γ (t)) ≤ tΨ(u )+(1−t)Ψ(0) = tΨ(u ) < ∞.
0 0 0
FromI (u ) < 0and(Φ )weinferthatsup I (γ(t)) < ∞andc (λ) < ∞foreveryλ ∈ [1−ε,1+ε].
1+ε 0 1 0≤t≤1 λ 0
The assertion α ≤ c (λ) follows from the fact γ([0,1])∩∂B(0,ρ ) and (MP).
0 0 0
For Γ and c (λ), consider a map γ ∈ C(Dk,X) defined by
k k (cid:101)k
 (cid:18) (cid:19)
ζ
 |ζ|π if 0 < |ζ| ≤ 1,
0,k
γ (ζ) ≡ |ζ|
(cid:101)k

0 if ζ = 0.
Clearly γ ∈ Γ holds. Moreover, (Ψ ), (Φ ) and (SMP) imply
(cid:101)k k 1 1
(cid:18) (cid:18) (cid:19)(cid:19)
ζ
sup Ψ(γ (ζ)) ≤ sup |ζ|Ψ π ≤ sup Ψ(π (ζ))
(cid:101)k 0,k 0,k
|ζ|
ζ∈Dk ζ∈Dk ζ∈∂Dk
= (1+ε)−1 sup {I (π (ζ))+Φ(π (ζ))}
1+ε 0,k 0,k
ζ∈∂Dk
≤ (1+ε)−1 sup Φ(π (ζ)) < ∞.
0,k
ζ∈∂Dk
Hence, c (λ) < ∞ holds for all λ ∈ [1 − ε,1 + ε]. Furthermore, α ≤ c (λ) follows from the fact
k 0 k
∂B(0,ρ )∩γ(Dk) ̸= ∅ for each γ ∈ Γ . ■
0 k
Proposition 4.3. For each k = 0,1..., the function λ (cid:55)→ c (λ) is nondecreasing on [1−ε,1+ε], hence
k
differentiable at almost all λ ∈ [1−ε,1+ε]. Moreover, c is continuous from the right in [1−ε,1+ε);
k
thus, c is upper semicontinuous.
k
Proof. Themonotonicityofc followsfromΨ ≥ 0. Fortherightcontinuityofc , fixλ ∈ [1−ε,1+ε)and
k k
ε ∈ (0,∞) arbitrarily. Choose γ ∈ Γ so that sup I (γ (ζ)) < c (λ)+ε. Since sup Ψ(γ (ζ)) < ∞
ε k ζ∈Dk λ ε k ζ∈Dk ε
due to max |Φ(γ (ζ))| < ∞ and sup I (γ (ζ)) < c (λ) + ε, it follows that 0 ≤ I (γ (ζ)) −
ζ∈Dk ε ζ∈Dk λ ε k µ ε
I (γ (ζ)) < ε for every ζ ∈ Dk if µ−λ > 0 is sufficiently small. Then,
λ ε
c(µ) ≤ sup I (γ (ζ)) ≤ sup I (γ (ζ))+ε ≤ c (λ)+2ε
µ ε λ ε k
ζ∈Dk ζ∈Dk
if µ−λ > 0 is sufficiently small. This implies that c is right continuous. ■
k
Here is our main result on the existence of bounded Palais-Smale sequences.
Theorem 4.4. Suppose that (Ψ ), (Ψ ), (Φ ) and either (MP), or (E) and (SMP), hold. Assume also
1 2 1
that at λ ∈ (1 − ε,1 + ε), c′(λ) exists (with k = 0, under assumption (MP)). Then there exists a
k
Palais-Smale sequence {u }∞ for I such that I (u ) → c (λ) and {u }∞ is bounded in X.
j j=1 λ λ j k j j=1
Proof. For a fixed k ∈ {0,1,...}, assume that c′(λ) exists at some λ ∈ (1−ε,1+ε). We put
k
M ≡ c′(λ)+3.
0 k
37

<!-- Page 38 -->

From now on, we just assume k ≥ 1 since the case k = 0 can be handled in the same manner. From (Ψ ),
2
there exists R > 0 such that
0
{u ∈ X | Ψ(u) ≤ 6M } ⊂ B(0,R ) (70)
0 0
and we set
A ≡ B(0,R +1), A ≡ A∩{c (λ)−3σ ≤ I ≤ c (λ)+3σ}. (71)
0 c (λ),3σ k λ k
k
To complete the proof of Theorem 4.4, it suffices to show that A contains a Palais-Smale sequence
c (λ),3σ
k
of I for every σ ∈ (0,1). For this purpose, we argue by contradiction and suppose that there is no
λ
Palais-Smale sequence in A for some σ ∈ (0,1). Since A shrinks as σ decreases, without
c (λ),3σ c (λ),3σ
k k
loss of generality we may assume that
4σ < α = inf I (u) ≤ c (λ). (72)
0 1−ε1 k
∥u∥=ρ0
Since A does not contain any Palais-Smale sequence of I , we may find δ ∈ (0,σ) such that for
c (λ),3σ λ 0
k
each u ∈ A there exists v = v(u) ∈ X \{u} such that
c (λ),3σ
k
λ(Ψ(v)−Ψ(u))−Φ′(u)(v−u) < −5δ ∥v−u∥.
0
To derive a contradiction, we shall find a suitable relatively compact set K ⊂ A and exploit
c (λ),3σ
k
Lemmas 3.1 and 3.5. Since c′(λ) exists, there exists h > 0 such that
k 1
c (λ+h) < c (λ)+ (cid:0) c′(λ)+1 (cid:1) h = c (λ)+(M −2)h
k k k k 0
(73)
< c (λ)+M h for any h ∈ (0,h ).
k 0 1
In addition, we may also suppose
5M h < δ < σ. (74)
0 1 0
For h ∈ (0,h ), consider the following subclass Γh of Γ
1 k k
(cid:40) (cid:41)
(cid:12)
Γh ≡ γ ∈ Γ (cid:12) sup I (γ(ζ)) ≤ c (λ)+M h .
k k (cid:12) λ+h k 0
ζ∈Dk
Notice that (73) implies Γh ̸= ∅ for each h ∈ (0,h ). For each h ∈ (0,h ) and γ ∈ Γh, if ζ ∈ Dk satisfies
k 1 1 k
I (γ(ζ)) ≥ c (λ)−5M h,
λ k 0
then from γ ∈ Γh we deduce
k
I (γ(ζ))−I (γ(ζ)) c (λ)+M h−(c (λ)−5M h)
λ+h λ k 0 k 0
Ψ(γ(ζ)) = ≤ = 6M .
0
h h
By the choice of R in (70), this means that for any h ∈ (0,h ) and γ ∈ Γh, the set
0 1 k
K ≡ {γ(ζ) | I (γ(ζ)) ≥ c (λ)−5M h}
γ λ k 0
satisfies

## K ⊂ B(0,R ) ⊂ A.

γ 0
Furthermore, since K ⊂ γ(Dk), K is relatively compact in X and (74) yields K ⊂ A . Moreover,
γ γ γ c (λ),3σ
k
since we are considering the case k ≥ 1 (thus, we are assuming (E) and (SMP)), K is symmetric.
γ
Next, we choose any h ∈ (0,h ) and γ ∈ Γh, and write
1 1 k
C ≡ γ (Dk), K ≡ K = {γ (ζ) | I (γ (ζ)) ≥ c (λ)−5M h} ⊂ B(0,R )∩A .
1 1 1 γ1 1 λ 1 k 0 0 c
k
(λ),σ
By Lemma 3.5, there exist τ
(cid:101)
> 0, η ∈ C([0,τ
(cid:101)
]×X,X) and open (symmetric) sets W,W(cid:102) in X such that
38

<!-- Page 39 -->

(a) K
1
⊂ W ⊂ W ⊂ W(cid:102);
(b) ∥η(s,w)−w∥ ≤ s, η(s,−w) = −η(s,w) for every (s,w) ∈ [0,τ]×X and η(s,w) = w for all s ∈ [0,τ]
(cid:101) (cid:101)
if w ̸∈ W(cid:102);
(c) I (η(s,w)) ≤ I (w)+δ s for each (s,w) ∈ [0,τ]×X;
λ λ 0 (cid:101)
(d) I (η(s,w)) ≤ I (w)−2δ s for any (s,w) ∈ [0,τ]×W with I (w) ≥ c (λ)−σ.
λ λ 0 (cid:101) λ k
We briefly explain the issues to overcome and the strategy. First, flowing γ by η may not lead to a
1
map in Γ , as η may not preserve the boundary condition on ∂Dk. For this reason, we have to modify the
k
map γ ≡ η(τ ,γ ) in a neighborhood of ∂Dk to get an element γ ∈ Γ (perhaps, not in Γh) satisfying
(cid:101)2 1 1 2 k k
sup I (γ (ζ)) ≤ c (λ)+M h−2δ τ for some τ ≥ τ > 0.
λ 2 k 0 0 1 1 (cid:101)
ζ∈Dk
A second issue is that the time interval τ might be too small to obtain the following contradiction:
1
sup I (γ (ζ)) < c (λ).
λ 2 k
ζ∈Dk
To remedy, we first choose τ close to the maximal time for which a deformation with properties (a)–(d)
1
exists (for fixed K ,δ ). Next, we proceed inductively to construct Cauchy sequences of maps {γ } ⊂ Γ
1 0 j k
and of almost maximal times {τ } ⊂ (0,∞) with the property
j
j
(cid:88)
sup I (γ (ζ)) ≤ c (λ)+M h−2δ τ .
λ j k 0 0 i
ζ∈Dk
i=1
We shall prove that the relatively compact sets
(cid:40) (cid:12) j−1 (cid:41)
(cid:12) (cid:88)
K ≡ γ (ζ) (cid:12) I (γ (ζ)) ≥ c(λ)−5M h+δ τ
j j (cid:12) λ j 0 0 i
(cid:12)
i=1
of points at which I ◦γ takes higher values are all contained in A , and that their union K ≡
λ j c (λ),3σ ∞
(cid:83)∞
K ⊂ A is relatively compact, too. By choosing a de
k
formation η in Lemma 3.5 with
j=1 j c k (λ),3σ ∞
K = K we are then able to reach our desired contradiction. Here is the point where τ being “almost
∞ j
maximal” plays a role.
Step 1: construction of γ , and its properties.
2
For the given relatively compact symmetric set K , we may consider
1
(cid:110)(cid:16) (cid:17) (cid:12) (cid:111)

## D

1
≡ η,τ,W,W(cid:102) (cid:12)
(cid:12)
η,W,W(cid:102) satisfy (a)–(d) for s ∈ [0,τ] .

### We define

(cid:26) (cid:27)
2M h
0
T(cid:101)1 ≡ sup τ ∈ (0,∞] and T
1
≡ min , T(cid:101)1 .
δ
(η,τ,W,W(cid:102))∈D1 0
RemarkthatD
1
̸= ∅,andthat(74)withh ∈ (0,h
1
)givesT
1

## ≤ 2M

0
h/δ
0
≤ 2/5. Wechoose(η
1
,τ
1

## ,W

1
,W(cid:102)1 ) ∈
D so that
1
3
T < τ < T
1 1 1
4
and define γ ∈ C(Dk,X) by
(cid:101)2
γ (ζ) := η (τ ,γ (ζ)).
(cid:101)2 1 1 1
39

<!-- Page 40 -->

Since γ may not coincide with π on ∂Dk, in order to obtain a map in Γ we define, for θ ∈ (0,1/4),
(cid:101)2 0,k k
the dilation
ζ
L : Dk(1−θ) → Dk, L (ζ) ≡ .
θ θ
1−θ
Notice that
θ
max |L (ζ)−ζ| = .
θ
ζ∈Dk(1−θ) 1−θ
Whenk = 0, weconsiderL : [θ,1−θ] → [0,1]. Bytheuniformcontinuityofγ , wemayfindθ ∈ (0,1/4)
θ 1 1
such that
τ
1
max ∥γ (ζ)−γ (L (ζ))∥+ max ∥γ (ζ)−γ (ζ/|ζ|)∥ ≤ . (75)
|ζ|≤1−θ1
1 1 θ1
1−θ1≤|ζ|≤1
1 1
2
Then we define γ (ζ) by
2

η (τ ,γ (L (ζ))) if |ζ| ≤ 1−θ ,


1 1 1 θ1 1

γ 2 (ζ) ≡ (cid:18) 1−|ζ| (cid:18) ζ (cid:19)(cid:19)
   η 1 τ 1 θ , γ 1 |ζ| if 1−θ 1 ≤ |ζ| ≤ 1.
1
It is easily seen that γ ∈ Γ and
2 k
∥γ (ζ)−γ (ζ)∥ ≤
2 1

∥η (τ ,γ (L (ζ)))−γ (L (ζ))∥+∥γ (L (ζ))−γ (ζ)∥ if |ζ| ≤ 1−θ ,


1 1 1 θ1 1 θ1 1 θ1 1 1

(cid:13) (cid:18) (cid:18) (cid:19)(cid:19) (cid:18) (cid:19)(cid:13) (cid:13) (cid:18) (cid:19) (cid:13)
(cid:13) 1−|ζ| ζ ζ (cid:13) (cid:13) ζ (cid:13)
   (cid:13) (cid:13) η 1 τ 1 θ , γ 1 |ζ| −γ 1 |ζ| (cid:13) (cid:13) +(cid:13) (cid:13) γ 1 |ζ| −γ 1 (ζ)(cid:13) (cid:13) if 1−θ 1 ≤ |ζ| ≤ 1.
1
Therefore, property (b) and (75) yield
3
max∥γ (ζ)−γ (ζ)∥ ≤ τ . (76)
1 2 1
ζ∈Dk 2
It follows from property (c), (SMP), (72) and (74) that if ζ ∈ Dk \Dk(1−θ ), then
1
I (γ (ζ)) ≤ δ τ < δ < σ < c (λ)−3σ < c (λ)−5M h. (77)
λ 2 0 1 0 k k 0
Similarly, whenζ ∈ Dk(1−θ )\(γ ◦L )−1(K ), wehaveI (γ (L (ζ))) < c (λ)−5M hbythedefinition
1 1 θ1 1 λ 1 θ1 k 0
of K , and
1
I (γ (ζ)) ≤ I (γ (L (ζ)))+δ τ < c (λ)+δ τ −5M h. (78)
λ 2 λ 1 θ1 0 1 k 0 1 0
On the other hand, if ζ ∈ (γ ◦L )−1(K ), then γ (L (ζ)) ∈ K , and property (d) with the fact γ ∈ Γh
1 θ1 1 1 θ1 1 1 k
implies
I (γ (ζ)) ≤ I (γ (L (ζ)))−2δ τ ≤ c (λ)+M h−2δ τ .
λ 2 λ 1 θ1 0 1 k 0 0 1
By the properties 3T /4 < τ < T ≤ 2M h/δ , we see that
1 1 1 0 0
δ τ −5M h ≤ M h−2δ τ
0 1 0 0 0 1
and
c (λ) ≤ sup I (γ (ζ)) ≤ c (λ)+M h−2δ τ . (79)
k λ 2 k 0 0 1
ζ∈Dk
Step 2: construction of the sequence {γ }∞ .
j j=1
40

<!-- Page 41 -->


### Next, put

C ≡ γ (Dk), K ≡ {γ (ζ) | I (γ (ζ)) ≥ c (λ)+δ τ −5M h}.
2 2 2 2 λ 2 k 0 1 0
By (76),
3
dist (C ,C ) ≤ τ ,

## H 1 2 1

2
where dist stands for the Hausdorff distance between C and C defined by

## H 1 2

(cid:40) (cid:41)
dist (A,B) ≡ max supdist(x,B), supdist(A,y) .

## H

x∈A y∈B
Moreover, from (77) and (78) we infer that
γ−1(K ) ⊂ (γ ◦L )−1(K ) ⊂ Dk(1−θ ).
2 2 1 θ1 1 1
Hence, if ζ ∈ γ−1(K ), then property (b) yields
2 2
∥γ (ζ)−γ (L (ζ))∥ = ∥η (τ ,γ (L (ζ)))−γ (L (ζ))∥ ≤ τ ,
2 1 θ1 1 1 1 θ1 1 θ1 1
and the fact γ (L (ζ)) ∈ K ⊂ B(0,R ) gives
1 θ1 1 0
K ⊂ B(0, R +τ ).
2 0 1
Combining (79) with τ < T ≤ 2/5, we observe that K ⊂ A is relatively compact. Thus, Lemma
1 1 2 c (λ),3σ
k
3.5 ensures the existence of a deformation (η,τ
(cid:101)

## ,W

2
,W(cid:102)2 ) satisfying (a)–(d) with K
2
replacing K
1
. Then,
we consider
(cid:110)(cid:16) (cid:17) (cid:12) (cid:111)

## D

2
≡ η,τ,W,W(cid:102) (cid:12)
(cid:12)
(η,τ,W,W(cid:102)) satisfies (a)–(d) for s ∈ [0,τ] and K
2
instead of K
1
and define
(cid:26) (cid:27)
2M h
0
T(cid:101)2 ≡ sup τ, T
2
≡ min −τ
1
, T(cid:101)2 .
δ
(η,τ,W,W(cid:102))∈D2 0
Select (η
2
,τ
2

## ,W

2
,W(cid:102)2 ) ∈ D
2
and θ
2
∈ (0,1/4) so that
3
T < τ < T
2 2 2
4
and
τ
2
max ∥γ (ζ)−γ (L (ζ))∥+ max ∥γ (ζ)−γ (ζ/ζ|)∥ ≤ .
|ζ|≤1−θ2
2 2 θ2
1−θ2≤|ζ|≤1
2 2
2
Define γ ∈ Γ by
3 k

η (τ ,γ (L (ζ))) if |ζ| ≤ 1−θ ,


2 2 2 θ2 2

γ 3 (ζ) ≡ (cid:18) 1−|ζ| (cid:18) ζ (cid:19)(cid:19)
   η 2 τ 2 θ , γ 2 |ζ| if 1−θ 2 ≤ |ζ| ≤ 1.
2
Arguing as before, we may prove
3
max∥γ (ζ)−γ (ζ)∥ ≤ τ ,
2 3 2
ζ∈Dk 2
and
(cid:40) ≤ c (λ)+M h−2δ (τ +τ ) if ζ ∈ (γ ◦L )−1(K ),
k 0 0 1 2 2 θ2 2
I (γ (ζ))
λ 3
< c (λ)+δ (τ +τ )−5M h otherwise.
k 0 1 2 0
41

<!-- Page 42 -->

Since τ +τ < 2M h/δ , we see that
1 2 0 0
δ (τ +τ )−5M h < M h−2δ (τ +τ ),
0 1 2 0 0 0 1 2
c (λ) ≤ sup I (γ (ζ)) ≤ c (λ)+M h−2δ (τ +τ ).
k ζ∈Dk λ 3 k 0 0 1 2

### By putting

C ≡ γ (Dk), K ≡ {γ (ζ) | I (γ (ζ)) ≥ c (λ)+δ (τ +τ )−5M h},
3 3 3 3 λ 3 k 0 1 2 0
we see from the same argument as before that
3
dist (C ,C ) ≤ τ , γ−1(K ) ⊂ (γ ◦L )−1(K ) ⊂ Dk(1−θ ),
H 2 3 2 2 3 3 2 θ2 2 2
K ⊂ B(0,R +τ +τ ).
3 0 1 2
Thus, K ⊂ A is relatively compact. We may therefore repeat the same procedure inductively to
3 c (λ),3σ
k
obtain {K
j
}∞
j=1
, {τ
j
}∞
j=1
⊂ (0,∞), (η
j
,τ
j

## ,W

j
,W(cid:102)j ) ∈ D
j
, {θ
j
}∞
j=1

## ⊂ (0,1/4), {L

θj
}∞
j=1
, {γ
j
}∞
j=1

## ⊂ Γ

k
such
that
3τ
C ≡ γ (Dk), dist (C ,C ) ≤ j−1 ,
j j H j−1 j
2
(cid:40) j−1 (cid:41) (cid:32) j−1 (cid:33)
(cid:12) (cid:88) (cid:88)
K ≡ γ (ζ) (cid:12) I (γ (ζ)) ≥ c (λ)−5M h+δ τ ⊂ B 0,R + τ ,
j j (cid:12) λ j k 0 0 i 0 i
i=1 i=1
(cid:40) j−1 (cid:41) (80)
2M 0 h (cid:88) 3
T(cid:101)j ≡ sup τ, T
j
≡ min − τ
i
, T(cid:101)j , T
j
< τ
j

## < T

j
,
δ 4
(η,τ,W,W(cid:102))∈Dj 0 i=1
j j
(cid:88) (cid:88) M 0 h 2
sup I (γ (ζ)) ≤ c (λ)+M h−2δ τ , τ ≤ < ,
λ j+1 k 0 0 i i
2δ 5
ζ∈Dk
i=1 i=1
0
where
 (cid:0) (cid:1)
η τ ,γ (L (ζ)) if |ζ| ≤ 1−θ ,


j j j θj j
 3τ
j
γ j+1 (ζ) ≡    η j (cid:18) τ j 1− θ |ζ| , γ j (cid:18) | ζ ζ| (cid:19)(cid:19) if 1−θ j ≤ |ζ| ≤ 1, m ζ∈ a D x k ∥γ j (ζ)−γ j+1 (ζ)∥ ≤ 2 .
j
Step 3: a compactness argument, and conclusion.

### Consider

S ≡ {K ⊂ X | K ̸= ∅, K is compact}.
It is known that (S,dist ) is a complete metric space (we refer e.g. to [36, Theorem 10.1.6]). Since

## H

(cid:80)∞
τ < ∞ due to (80), we have
i=1 i
ℓ ℓ
(cid:88) (cid:88) 3
dist (C ,C ) ≤ dist (C ,C ) ≤ τ ;
H j j+ℓ H j+i−1 j+i j+i−1
2
i=1 i=1
thus {C }∞ is a Cauchy sequence in (S,dist ). Hence there exists C ∈ S such that
j j=1 H ∞
dist (C ,C ) → 0 as j → ∞.

### H j ∞

Consider
∞
(cid:91)

## K ≡ K .

∞ j
j=1
42

<!-- Page 43 -->

We next claim that K is relatively compact. Indeed, let {u }∞ ⊂ K be a sequence and choose
∞ p p=1 ∞
{j }∞ satisfying u ∈ K . Without loss of generality, we may assume j → ∞ as p → ∞. By recalling
p p=1 p jp p
that K ⊂ C , dist (C ,C ) → 0 and C is compact, lim ∥u −w ∥ = 0 for some {w }∞ ⊂ C .
j j H j ∞ ∞ p→∞ p p p p=1 ∞
From the compactness of C , up to a subsequence w → w ∈ C as p → ∞, whence u → w as
∞ p ∞ ∞ p ∞
p → ∞. This proves that K is relatively compact.
∞
Since K ⊂ A for every j ≥ 1, K ⊂ A holds and Lemma 3.5 can be applied to obtain
j c (λ),3σ ∞ c (λ),3σ
k k
τ
∞
> 0, η
∞
∈ C([0,τ
∞
]×X,X) and open sets W
∞
, W(cid:102)∞ such that K
∞

## ⊂ W

∞

## ⊂ W

∞
⊂ W(cid:103)∞ and (a)–(d)
hold with K instead of K . Since
(cid:80)∞
τ < ∞, there are two alternatives:
∞ 1 i=1 i
∞
(cid:88) 2M 0 h 2
(A) τ = < ;
i
δ 5
0
i=1
∞
(cid:88) 2M 0 h
(B) τ < .
i
δ
0
i=1
In case (A), choose a large j such that M h/δ <
(cid:80)j
τ . Then
0 0 i=1 i
j
(cid:88)
c (λ) ≤ sup I (γ (ζ)) ≤ c (λ)+M h−2δ τ < c (λ)−M h,
k λ j+1 k 0 0 i k 0
ζ∈Dk
i=1
which is a contradiction. In case (B), it follows from the definition of T(cid:101)j and the fact K
j

## ⊂ K

∞
that
T(cid:101)j ≥ τ
∞
. Since (cid:80)∞
i=1
τ
i

## < 2M

δ0
0h, it follows that
(cid:40) j−1 (cid:41) (cid:40) ∞ (cid:41)
2M 0 h (cid:88) 2M 0 h (cid:88)

## T

j
= min − τ
i
, T(cid:101)j ≥ min − τ
i
, τ
∞
> 0.
δ δ
0 0
i=1 i=1
Sinceτ ≥ 3T ,thiscontradictsthefactthat (cid:80)∞ τ ≤ 2 < ∞.Thus,ineithercase,wegetacontradiction
j 4 j i=1 i 5
and A contains a Palais-Smale sequence. This completes the proof of Theorem 4.4. ■
c (λ),3σ
k
We are ready to prove Theorem 1.6 and part of Theorem 1.7, as a direct consequence of the next
Theorem 4.5. Assume that (Ψ ), (Ψ ), (Ψ ), (Φ ), (Φ ) and (IB) hold. Then, c (1) is a critical value
1 2 3 1 2 0
of I = I if (MP) holds, and {c (1)}∞ are critical values of I if (E) and (SMP) hold.
1 k k=1
Proof. We only prove that {c (1)}∞ are critical values of I, the other case being analogous. For k ≥ 1,
k k=1
c (λ) is nondecreasing with respect to λ ∈ (1−ε,1+ε]. Thus, there exists a sequence {λ } ⊂ (1,1+ε)
k l l
such that lim λ = 1 and c′(λ ) exists for each l = 1,2,.... By Theorem 4.4, there exists a bounded
l→∞ l k l
Palais-Smale sequence {u } for I with lim I (u ) = c (λ ). Then, from Proposition 4.1, up to
l,j j λ j→∞ λ l,j k l
l l
a subsequence u converges strongly to some u in X as j → ∞, and u is a critical point of I with
l,j l l λ
l
I (u ) = c (λ ). By Proposition 4.3 and λ > 1, we have c (λ ) → c (1) as l → ∞. Furthermore, by
λ l k l l k l k
l
c (1+ε)+1
using (IB), {u } ⊂ K k is bounded in X. Therefore, applying again Proposition 4.1, we conclude
l [1,1+ε]
that u → u strongly in X, for some u which is critical for I and satisfies I(u) = c (1). This completes
l k
the proof. ■
TheproofofTheorem1.7willbecompletedifweprovethefollowingdivergencepropertyofc = c (1).
k k
Theorem 4.6. Assume that (Ψ ), (Ψ ), (Ψ ), (Φ ), (Φ ), (IB), (E) and (SMP) hold. Then,
1 2 3 1 2
lim c (1) = ∞.
k
k→∞
43

<!-- Page 44 -->

Proof. To prove Theorem 4.6, we combine the arguments in [54, Chapter 9] (cf. [33]) and [63] with the
iteration scheme as in the proof of Theorem 4.4. To this end, we introduce
ERn ≡ {E ⊂ Rn | E is closed, symmetric and 0 ̸∈ E},
E ≡ {F ⊂ X | F is closed, symmetric and 0 ̸∈ F},
G(E) ≡ Krasnoselski’s genus of E.
For k ≥ 1 and λ ∈ [1−ε ,1], we set
1
Λ k ≡ (cid:110) γ (cid:16) Dn\Σ (cid:17) (cid:12) (cid:12) n ≥ k, γ ∈ Γ n , Σ ∈ ERn , Σ∩∂Dn = ∅, G(Σ) ≤ n−k (cid:111) ,
d (λ) ≡ inf supI .
k λ

### B∈Λ ku∈B

By G(∅) = 0, γ(Dk) ∈ Λ holds for all γ ∈ Γ . Moreover, since Λ ⊂ Λ and Ψ ≥ 0, for every k ≥ 1
k k k+1 k
and λ,λ ,λ ∈ [1−ε ,1],
1 2 1
d (λ) ≤ c (λ), d (λ) ≤ d (λ) and d (λ ) ≤ d (λ ) if λ ≤ λ .
k k k k+1 k 1 k 2 1 2
Therefore, it is enough to prove
d (1) → ∞ as k → ∞. (81)
k
Following [54] and [63] (see also [33]), we prove the next result.

### Lemma 4.7. The following properties hold:

(i) if C ∈ Λ and Z ∈ E satisfies G(Z) ≤ s and I | > 0, then C \Z ∈ Λ ;
k+s 1 Z k
(ii) for every k ∈ N and C ∈ Λ , it holds C ∩∂B(0,ρ ) ̸= ∅, hence
k 0
0 < α = inf I (u) ≤ d (1−ε ) ≤ d (λ) for each λ ∈ [1−ε ,1].
0 1−ε1 k 1 k 1
∥u∥=ρ0
Proof. (i) Write C = γ(Dn\Σ) ∈ Λ
k+s
where n ≥ k + s, γ ∈ Γ
n
, Σ ∩ ∂Dn = ∅, Σ ∈ ERn and
G(Σ) ≤ n−(k +s). Let Z ∈ E satisfy G(Z) ≤ s and I
1
|

## Z

> 0. Remark that γ−1(Z) ∈ ERn . We claim
that
(cid:16) (cid:17)
C \Z = γ Dn\(Σ∪γ−1(Z)) . (82)

### Notice that


### C \Z ⊃ C \Z ⊃ γ(Dn\Σ)\Z

= γ (cid:0) (Dn\Σ)\γ−1(Z) (cid:1) = γ (cid:0)Dn\ (cid:0) Σ∪γ−1(Z) (cid:1)(cid:1) .
Hence, it holds that C \Z ⊃ γ(Dn\(Σ∪γ−1(Z))). On the other hand, since γ−1(Z) is closed, we have
Dn\Σ\γ−1(Z) ⊂ Dn\(Σ∪γ−1(Z)),
which implies
(cid:16) (cid:17) (cid:16) (cid:17)
C \Z = γ Dn\Σ\γ−1(Z) ⊂ γ Dn\(Σ∪γ−1(Z)) .
From the compactness of Dn\(Σ∪γ−1(Z)), it follows that C \Z ⊂ γ(Dn\(Σ∪γ−1(Z))). Thus, (82)
holds.
The fact I | > 0 > I | gives ∂Dn∩(Σ∪γ−1(Z)) = ∅. By (82) and the estimate
1 Z 1 π0,n(∂Dn)
G (cid:0) Σ∪γ−1(Z) (cid:1) ≤ G(Σ)+G (cid:0) γ−1(Z) (cid:1) ≤ G(Σ)+G(Z) ≤ n−k,
44

<!-- Page 45 -->

we conclude C \Z ∈ Λ .
k
(ii) Write C = γ(Dn\Σ) ∈ Λ where n ≥ k, γ ∈ Γ , Σ∩∂Dn = ∅ and G(Σ) ≤ n−k. Set
k n
U(cid:98) ≡ {ζ ∈ IntDn | γ(ζ) ∈ B(0,ρ
0
)}.
It is easily seen that 0 ∈ U(cid:98), −U(cid:98) = U(cid:98) and U(cid:98) ⊂ Rn is open. Denote by U the connected component of U(cid:98)
containing 0. SinceU is a symmetricneighborhoodof 0, G(∂U) = nholds. Since∥γ(ζ)∥ = ∥π (ζ)∥ > ρ
0,n 0
for each ζ ∈ ∂Dn, we see that
γ(∂U) ⊂ ∂B(0,ρ ). (83)
0
Define W ≡ {ζ ∈ Dn | γ(ζ) ∈ ∂B(0,ρ
0
)} ∈ ERn . Thanks to (83), we see that ∂U ⊂ W and n =
G(∂U) ≤ G(W). On the other hand, letting ε small enough so that Dn(ε)∩W = ∅, by the properties of
Krasnoselki’s genus, G(W) ≤ G(Dn\Dn(ε)) = G(∂Dn) = n. Summarizing,
(cid:16) (cid:16) (cid:17)(cid:17) (cid:16) (cid:17)
G(W) = n, G γ W \Σ ≥ G W \Σ ≥ G(W)−G(Σ) ≥ k > 0.
In particular, γ(W \Σ) ̸= ∅. Since γ(W \Σ) ⊂ C ∩∂B(0,ρ ), we have ∅ ≠ C ∩∂B(0,ρ ). ■
0 0
To prove (81), we argue by contradiction and suppose that {d (1)} is bounded. From the monok k
tonicity of d (λ) in k and λ, it follows that
k
d (λ) ≡ lim d (λ) ∈ [α ,∞) for every λ ∈ [1−ε ,1].
∞ k 0 1
k→∞
Notice that λ (cid:55)→ d (λ) is nondecreasing on [1−ε ,1].
∞ 1
Claim 1: There exists λ(cid:101)0 ∈ (cid:2) 1−ε
1
, 1− ε
2
1 (cid:3) such that
d′
∞
(λ(cid:101)0 ) exists and d′
∞
(λ(cid:101)0 ) ≤ 3ε−
1
1ν
0
, where ν
0
≡ d
∞
(1)−d
∞
(1−ε
1
) ∈ [0,∞).
Proof. Since d is nondecreasing, we obtain
∞
(cid:90) 1
d′ (λ)dλ ≤ d (1)−d (1−ε ) = ν .
∞ ∞ ∞ 1 0
1−ε1

### Write

J ≡ (cid:8) λ ∈ [1−ε ,1] | d′ (λ) exists and d′ (λ) ≤ 3ε−1ν (cid:9) .
0 1 ∞ ∞ 1 0
When ν > 0, since 0 ≤ d′ (λ) a.e. in [1−ε ,1] and
0 ∞ 1
(cid:90)
ν ≥ d′ (λ)dλ ≥ 3ε−1ν |[1−ε ,1]\J |,
0 ∞ 1 0 1 0
[1−ε1,1]\J0
we obtain the following estimation
2
|J | ≥ ε . (84)
0 1
3
Since (84) also holds when ν = 0, Claim 1 directly follows. ■
0
Choose h ∈ (0,ε /2) so that for any h ∈ [0,h ],
0 1 0
(cid:16) (cid:17)
d
∞
(λ(cid:101)0 +h) ≤ d
∞
(λ(cid:101)0 )+ d′
∞
(λ(cid:101)0 )+1 h ≤ d
∞
(λ(cid:101)0 )+ (cid:0) 3ε−
1
1ν
0
+1 (cid:1) h. (85)
From Proposition 4.1 and I (0) = 0, the set
λ
(cid:110) (cid:12) α (cid:111)
K ≡ u ∈ X (cid:12) u is a critical point of I , 0 ≤ I ≤ d (1)+1
0 (cid:12) λ(cid:101)0 2 λ(cid:101)0 ∞
45

<!-- Page 46 -->

is compact and symmetric with 0 ̸∈ K , hence K ∈ E. Let
0 0
s ≡ G(K ) ∈ N.
∞ 0
Since K is compact and I is lower semicontinuous, we may find r ∈ (0,1) so that
0 λ(cid:101)0 ∞
(cid:16) (cid:17) α
0
K +B(0,3r ) ∈ E, s = G K +B(0,3r ) , < I | ≤ I | . (86)
0 ∞ ∞ 0 ∞ 4 λ(cid:102)0 K0+B(0,3r∞) 1 K0+B(0,3r∞)
According to (Ψ ), for each M > 0 there exists R(M) > 0 so that
2
{u ∈ X | Ψ(u) ≤ M} ⊂ B(0,R(M)).

### In what follows, we shall write

O ≡ K +B(0,r ), O ≡ K +B(0,3r ), M ≡ ε−1ν +1,
r∞ 0 ∞ 3r∞ 0 ∞ 0 1 0
(cid:110)α (cid:111)
0
A ≡ B(0,R(12M )+3r )\O , A ≡ A∩ ≤ I ≤ d (1)+1 .
0 ∞ r∞ 2 λ(cid:101)0 ∞
Notice that A ⊂ X is bounded, closed and symmetric. Furthermore, from Proposition 4.1 and the
definition of O , there is no Palais-Smale sequence in A. Therefore, there exists δ ∈ (0,1) such that
r∞ 0
for every u ∈ A we may find v = v(u) ∈ X \{u} such that
λ(cid:101)0 (Ψ(v)−Ψ(u))−Φ′(u)(v−u) < −5δ
0
∥v−u∥. (87)
We next choose h > 0 so that
1
(cid:26) (cid:27)
ε α 1
0 < h ≤ h < 1 , 12δ−1M h < min r , 0 , ≡ σ (88)
1 0 2 0 0 1 ∞ 6 3
and then, we can find k ∈ N such that
∞
d
∞
(λ(cid:101)0 +h
1
)−d
k
(λ(cid:101)0 +h
1
) ≤ h
1
, d
∞
(λ(cid:101)0 )−d
k
(λ(cid:101)0 ) ≤ h
1
for k ≥ k
∞
. (89)
Claim 2: For every λ(cid:101)0 ≤ λ
1
≤ λ
2
≤ λ(cid:101)0 +h
1
and k
∞
≤ k
1
,k
2
,
d (λ )−d (λ ) ≤ 3h M .
k2 2 k1 1 1 0
Proof. By (85), (88) and (89) with the monotonicity of d (λ) on k and λ,
k
d
k2
(λ
2
)−d
k1
(λ
1
) ≤ d
k2
(λ(cid:101)0 +h
1
)−d
k1
(λ(cid:101)0 ) ≤ d
∞
(λ(cid:101)0 +h
1
)−d
k∞
(λ(cid:101)0 )
≤ d
∞
(λ(cid:101)0 +h
1
)−d
∞
(λ(cid:101)0 )+h
1
≤ (cid:0) 3ε−
1
1ν
0
+1 (cid:1) h
1
+h
1
≤ 3h M . ■
1 0
Recalling (87), we shall apply Lemma 3.5 with
(cid:26) (cid:27)
α 1 (cid:110) (cid:111)
0
σ = min r
∞
,
6
,
3

## , A

d k∞ (λ(cid:101)0),3σ
≡ A∩ d
k∞
(λ(cid:101)0 )−3σ ≤ I
λ(cid:101)0
≤ d
k∞
(λ(cid:101)0 )+3σ ⊂ A.
Therefore, for every relatively compact symmetric set K ⊂ A , we may construct an odd deford
k∞
(λ(cid:101)0),3σ
mation satisfying (i)–(iii) in Lemma 3.5. To find suitable sets K, in what follows we put
µ ≡ λ(cid:101)0 +h
1
.
46

<!-- Page 47 -->

For the given integers k in (89) and s in (86), choose C ∈ Λ so that
∞ ∞ k∞+s∞
supI ≤ d (µ)+h .
µ k∞+s∞ 1

## C

Consequently, Claim 2, (88) and the inequalities δ < 1, r < 1, M ≥ 1 guarantee that
0 ∞ 0
supI
µ
≤ d
k∞
(λ(cid:101)0 )+(3M
0
+1)h
1
≤ d
k∞
(λ(cid:101)0 )+4M
0
h
1
< d
k∞
(λ(cid:101)0 )+σ. (90)

## C

Moreover, if u ∈ C satisfies
d
k∞
(λ(cid:101)0 )−σ < d
k∞
(λ(cid:101)0 )−8M
0
h
1

## ≤ I

λ(cid:101)0
(u),
then (90) yields
(cid:16) (cid:17)
Ψ(u) = I µ (u)−I λ(cid:101)0 (u) ≤ d k∞ (λ(cid:102)0 )+4M 0 h 1 − d k∞ (λ(cid:101)0 )−8M 0 h 1 = 12M . (91)
0
µ−λ(cid:101)0 h 1
From (91) it follows that
(cid:110) (cid:111)

## C ∩ I

λ(cid:101)0
≥ d
k∞
(λ(cid:101)0 )−8M
0
h
1
⊂ {u ∈ X | Ψ(u) ≤ 12M
0

## } ⊂ B(0,R(12M

0
)). (92)

### Set


## C ≡ C \O .

0 3r∞
We infer from (86), (90), (92) and Lemma 4.7 that
(cid:110) (cid:111)

## C

0

## ∈ Λ

k∞

## , K

0

## ≡ C

0
∩ d
k∞
(λ(cid:101)0 )−8M
0
h
1

## ≤ I

λ(cid:101)0

## ⊂ A

d
k∞
(λ(cid:101)0),3σ
.

### Furthermore,

d (C ,O ) ≥ 2r .

### X 0 r∞ ∞

Since C ∈ Λ , we can write C as
0 k∞ 0
(cid:16) (cid:17)

## C

0
= γ
0
Dn\Σ
0
, n ≥ k
∞
, γ
0

## ∈ Γ

n

## , Σ

0
∈ ERn , Σ
0
∩∂Dn = ∅, G(Σ
0
) ≤ n−k
∞
.
Then K is rewritten as
0
K 0 = (cid:110) γ 0 (ζ) (cid:12) (cid:12) ζ ∈ Dn\Σ 0 , I λ(cid:101)0 (γ 0 (ζ)) ≥ d k∞ (λ(cid:101)0 )−8M 0 h 1 (cid:111) .
From now on, we will repeatedly use the following inequality:
−8M h +δ T < 4M h −2δ T for all T ∈ [0,4δ−1M h ). (93)
0 1 0 0 1 0 0 0 1
Since K is relatively compact and symmetric, we may apply Lemma 3.5 and find s > 0, η ∈ C([0,s ]×
0 0 0
X,X) and symmetric open sets W,W(cid:102) such that
(a) K
0
⊂ W ⊂ W ⊂ W(cid:102).
(b) ∥η(s,w)−w∥ ≤ s and η(s,−w) = −η(s,w) for every (s,w) ∈ [0,s ]×X.
0
(c) I (η(s,w)) ≤ I (w)+δ s for every (s,w) ∈ [0,s ]×X.
λ(cid:101)0 λ(cid:101)0 0 0
(d) I
λ(cid:101)0
(η(s,w)) ≤ I
λ(cid:101)0
(w)−2δ
0
s for every (s,w) ∈ [0,s
0
]×W with I
λ(cid:101)0
(w) ≥ d
k∞
(λ(cid:101)0 )−σ.
47

<!-- Page 48 -->

As in the proof of Theorem 4.4, we consider a family of deformations of K :
0
(cid:110)(cid:16) (cid:17) (cid:12) (cid:111)

## D

0
≡ η,τ,W,W(cid:102) (cid:12)
(cid:12)
η,W,W(cid:102) satisfy (a)–(d) for s ∈ [0,τ]
and set
(cid:26) (cid:27)
3M h
0 1
T(cid:101)0 ≡ sup τ ≥ s
0

## , T

0
≡ min , T(cid:101)0 .
δ
(η,τ,W,W(cid:102))∈D0 0
Choose (η
0
,τ
0

## ,W

0
,W(cid:102)0 ) ∈ D
0
so that
3 r
T < τ < T ≤ 3δ−1M h < ∞ ,
4 0 0 0 0 0 1 4
where the last inequality comes from (88). Since for small θ > 0 the dilation map
0
ζ
L : Dn(1−θ ) → Dn, L (ζ) ≡
θ0 0 θ0
1−θ
0
satisfies
τ
0
max ∥γ (ζ)−γ (L (ζ))∥+ max ∥γ (ζ)−γ (ζ/|ζ|)∥ < ,
|ζ|≤1−θ0
0 0 θ0
1−θ0≤|ζ|≤1
0 0
2
we define

η (τ ,γ (L (ζ))) if |ζ| ≤ 1−θ ,


0 0 0 θ0 0
γ (ζ) ≡ (cid:18) (cid:18) (cid:19)(cid:19)
1 1−|ζ| ζ
η τ , γ if 1−θ ≤ |ζ| ≤ 1.
 0 0 0 0
θ |ζ|
0
Then, γ ∈ Γ . Since θ > 0 is small and L is an odd homeomorphism,
1 n 0 θ0

## Σ

1

## ≡ L−

θ0

## 1(Σ

0
) ∈ ERn , Σ
1
∩∂Dn = ∅, G(Σ
1
) ≤ n−k
∞
,
and moreover
3
max∥γ (ζ)−γ (ζ)∥ ≤ τ .
1 0 0
ζ∈Dn 2

### Define

(cid:16) (cid:17)
C ≡ γ Dn\Σ ∈ Λ .
1 1 1 k∞
As in the proofs of Theorem 4.4, it follows from (93) and (90) that
d
k∞
(λ(cid:101)0 ) ≤ s

## C

u
1
pI
λ(cid:101)0
≤ d
k∞
(λ(cid:101)0 )+4M
0
h
1
−2δ
0
τ
0
;
this implies that
r
τ ≤ 2δ−1M h < ∞ .
0 0 0 1 6

### We next claim

dist (C ,C ) ≤ τ . (94)

## H 0 1 0

Let C ∋ u = γ (ζ), where ζ ∈ Dn\Σ . If 1−θ ≤ |ζ| ≤ 1, then by
1 1 1 1 0
γ (ζ/|ζ|) = γ (ζ/|ζ|) = π (ζ/|ζ|) ∈ C ∩C ,
1 0 0,n 0 1
the choice of θ gives ∥u −γ (ζ/|ζ|)∥ ≤ τ . When |ζ| ≤ 1−θ , we find
0 1 0 0 0
L (ζ) ∈ Dn\Σ , γ (L (ζ)) ∈ C , ∥u −γ (L (ζ))∥ ≤ τ .
θ0 0 0 θ0 0 1 0 θ0 0
Thus, d (C ,u ) ≤ τ and since u ∈ C is arbitrary, max d (C ,u ) ≤ τ .
X 0 1 0 1 1 u1∈C1 X 0 1 0
48

<!-- Page 49 -->

On the other hand, let C ∋ u = γ (ζ) where ζ ∈ Dn\Σ . From the property
0 0 0 0
L−1(ζ) ∈ Dn(1−θ )\Σ ,
θ0 0 1
it follows that
(cid:16) (cid:17) (cid:13) (cid:13)
γ L−1(ζ) ∈ C , (cid:13)u −γ (L (ζ))(cid:13) = ∥γ (ζ)−η (τ ,γ (ζ))∥ ≤ τ .
1 θ0 1 (cid:13) 0 1 θ
0
−1 (cid:13) 0 0 0 0 0
Hence, d (u ,C ) ≤ τ and max d (u ,C ) ≤ τ , which yields (94).

### X 0 1 0 u0∈C0 X 0 1 0

Furthermore, (94) and d (C ,O ) ≥ 2r imply the inequality

### X 0 r∞ ∞

d (C ,O ) ≥ 2r −τ .

### X 1 r∞ ∞ 0


### We next consider the set

K 1 ≡ (cid:110) γ 1 (ζ) (cid:12) (cid:12) ζ ∈ Dn\Σ 1 , I λ(cid:101)0 (γ 1 (ζ)) ≥ d k∞ (λ(cid:101)0 )−8M 0 h 1 +δ 0 τ 0 (cid:111) .
Remark that K is symmetric and relatively compact. Moreover, by combining (c) with (ii) in Lemma
1
4.7 and with δ ∈ (0,1), for 1−θ ≤ |ζ| ≤ 1 we have
0 0
I (γ (ζ)) ≤ I (γ (ζ/|ζ|))+δ τ < δ τ
λ(cid:101)0 1 λ(cid:101)0 0 0 0 0 0
≤ α
0

## −8M

0
h
1
+δ
0
τ
0
≤ d
k∞
(λ(cid:101)0 )−8M
0
h
1
+δ
0
τ
0
.

### Hence, we obtain

γ−1(K ) ⊂ (γ ◦L )−1(K ), max ∥γ (ζ)−γ (L (ζ))∥ ≤ τ .
1 1 0 θ0 0 1 0 θ0 0
ζ∈Dn(1−θ0)∩Dn\Σ1
Since K ⊂ B(0,R(12M )) holds due to (92),
0 0
K ⊂ B(0,R(12M )+τ ), d (K ,O ) ≥ 2r −τ , K ⊂ A .
1 0 0 X 1 r∞ ∞ 0 1 d
k∞
(λ(cid:101)0),3σ
By Lemma 3.5, there exist s
1
> 0, an odd map η ∈ C([0,s
1
]×X,X) and symmetric open sets W,W(cid:102) of
K satisfying (a)–(d) with K instead of K . Thus, define
1 1 0
(cid:40) (cid:12) (cid:41)
(cid:16) (cid:17) (cid:12)

## D

1
≡ η,τ,W,W(cid:102) (cid:12)
(cid:12)
η,W,W(cid:102) satisfy (a)–(d) for s ∈ [0,τ]
(cid:12)
and
(cid:26) (cid:27)
3M h
0 1
T(cid:101)1 ≡ sup τ ≥ s
1

## , T

1
≡ min −τ
0
, T(cid:101)1 .
δ
(η,τ,W,W(cid:102))∈D1 0
Select (η
1
,τ
1

## ,W

1
,W(cid:102)1 ) ∈ D
1
and 0 < θ
1
≪ 1 such that
3 M h r
0 1 ∞
T < τ < T ≤ 3 −τ < −τ
1 1 1 0 0
4 δ 4
0
and
τ
1
max ∥γ (ζ)−γ (L (ζ))∥+ max ∥γ (ζ)−γ (ζ/|ζ|)∥ < ,
|ζ|≤1−θ1
1 1 θ1
1−θ1≤|ζ|≤1
1 1
2
where
ζ
L (ζ) ≡ : Dn(1−θ ) → Dn.
θ1
1−θ
1
1
49

<!-- Page 50 -->

Define γ by
2

η (τ ,γ (L (ζ))) if |ζ| ≤ 1−θ ,


1 1 1 θ1 1
Γ ∋ γ (ζ) ≡ (cid:18) (cid:19)
n 2 1−|ζ|
η τ , γ (ζ/|ζ|) if 1−θ ≤ |ζ| ≤ 1.
 1 1 1 1
θ
1
From G(Σ ) ≤ n−k it follows that
1 ∞

## Σ

2

## ≡ L−

θ1

## 1(Σ

1
) ∈ ERn , Σ
2
∩∂Dn = ∅, G(Σ
2
) ≤ n−k
∞
.

### Writing

(cid:16) (cid:17)
C ≡ γ Dn\Σ ∈ Λ ,
2 2 2 k∞
we may prove
d
k∞
(λ(cid:101)0 ) ≤ s

## C

u
2
pI
λ(cid:101)0
≤ d
k∞
(λ(cid:101)0 )+4M
0
h
1
−2δ
0
(τ
0
+τ
1
),
which yields
2M h r
0 1 ∞
τ +τ ≤ < .
0 1
δ 6
0
Furthermore, by an argument analogous to the one we just employed for C and C , we see that
0 1
dist (C ,C ) ≤ τ , d (C ,O ) ≥ 2r −(τ +τ ).
H 1 2 1 X 2 r∞ ∞ 0 1

### We next define

K 2 ≡ (cid:110) γ 2 (ζ) (cid:12) (cid:12) ζ ∈ Dn\Σ 2 , I λ(cid:101)0 (γ 2 (ζ)) ≥ d k∞ (λ(cid:101)0 )−8M 0 h 1 +δ 0 (τ 0 +τ 1 ) (cid:111)
and notice that K is symmetric, relatively compact, γ−1(K ) ⊂ (γ ◦L )−1(K ) and
2 2 2 1 θ1 1
d (K ,O ) ≥ 2r −τ −τ , K ⊂ B(0,R(12M )+τ +τ ), K ⊂ A .
X 2 r∞ ∞ 0 1 2 0 0 1 2 d
k∞
(λ(cid:101)0),3σ
Inductively, weobtain{(η
j
,τ
j

## ,W

j
,W(cid:102)j )}∞
j=0

## , {C

j
}∞
j=0

## , {Σ

j
}∞
j=0
, {γ
j
}∞
j=0

## , {K

j
}∞
j=0
andasequence{D
j
}∞
j=0
of deformations of K such that
j
j
(cid:88)

## C

j
= γ
j
(Dn\Σ
j

## ) ∈ Λ

k∞

## , G(Σ

j
) ≤ n−k
∞
, d
k∞
(λ(cid:101)0 ) ≤ s

## C

u
j
pI
λ(cid:101)0
≤ d
k∞
(λ(cid:101)0 )+4M
0
h
1
−2δ
0
ℓ=0
τ
ℓ
,
j−1 j
(cid:88) (cid:88) 2M 0 h 1 r ∞
dist (C ,C ) ≤ τ , d (C ,O ) ≥ 2r − τ , τ ≤ < ,
H j j+1 j X j r∞ ∞ ℓ ℓ
δ 6
0
ℓ=0 ℓ=0
(cid:40) j−1 (cid:41)
3M 0 h 1 (cid:88) 3
T(cid:101)j ≡ sup τ, T
j
≡ min T(cid:101)j , − τ
ℓ

## , T

j
≤ τ
j

## < T

j
,
δ 4
(η,τ,W,W(cid:102))∈Dj 0 ℓ=0
(cid:40) (cid:12) j−1 (cid:41)
(cid:12) (cid:88)

## K

j
≡ γ
j
(ζ) (cid:12)
(cid:12)
(cid:12)
ζ ∈ Dn\Σ
j

## , I

λ(cid:101)0
(γ
j
(ζ)) ≥ d
k∞
(λ(cid:101)0 )−8M
0
h
1
+δ
0
τ
ℓ
,
ℓ=0
(cid:32) j−1 (cid:33)
(cid:88)
K ⊂ B 0,R(12M )+ τ .
j 0 ℓ
ℓ=0

### In particular,

K ⊂ A for each j ≥ 0.
j d
k∞
(λ(cid:101)0),3σ
50

<!-- Page 51 -->

Recalling that (S,dist ) is a complete metric space and the above properties, we see that {C }∞ is a

### H j j=0

Cauchy sequence in (S,dist ). Therefore, there exists C ∈ S such that dist (C ,C ) → 0 as j → ∞.

### H ∞ H j ∞

As before, a set defined by
∞
(cid:91)

## K ≡ K ⊂ A

∞ j d
k∞
(λ(cid:101)0),3σ
j=0
isrelativelycompactandLemma3.5withK ≡ K
∞
guaranteestheexistenceofdeformation(η
∞
,τ
∞

## ,W

∞
,W(cid:102)∞ )
of K
∞
; then (η
∞
,τ
∞

## ,W

∞
,W(cid:102)∞ ) ∈ D
j
for each j large enough. Thus,
(cid:40) ∞ (cid:41) (cid:26) (cid:27)
3 3M 0 h 1 (cid:88) 3 M 0 h 1
τ ≥ min τ , − τ ≥ min τ , for large enough j,
j ∞ ℓ ∞
4 δ 4 δ
0 0
ℓ=0
which contradicts
∞
(cid:88) r ∞
τ ≤ .
ℓ
6
ℓ=0
Hence, we complete the proof. ■

### Acknowledgements

J.B. was supported by the National Research Foundation of Korea(NRF) grant funded by the Korea government(MSIT)(No. NRF-2023R1A2C1005734). N.I.wassupportedbyJSPSKAKENHIGrantNumbers
JP 19H01797, 19K03590 and 24K06802. A.M. has been supported by the project “Geometric problems
with loss of compactness” from Scuola Normale Superiore, and by the PRIN Project 2022AKNSE4. L.
Mari is supported by the PRIN project no. 20225J97H5 “Differential-geometric aspects of manifolds via

### Global Analysis”

Conflict of Interest. The authors have no conflict of interest.

### A The principle of symmetric criticality

The principle of nonsmooth symmetric criticality due to Kobayashi & Oˆtani [44] considers a vast range
of linear actions of a topological groups G on a Banach space X. In this appendix, we provide a simpler
proof of the principle in a setting which applies to our main theorems. Compared to [44, Theorem 3.16],
notice that Proposition A.1 does not require X to be reflexive.
Let X be a Banach space and G a compact topological group acting on X linearly. Assume that the
map G×X ∋ (g,u) (cid:55)→ g·u ∈ X is continuous, and consider the closed subspace
X ≡ {u ∈ X | g·u = u for all g ∈ G}.

## G


### We consider two functionals Ψ and Φ satisfying

(i) Ψ : X → (−∞,∞] is convex and lower semicontinuous with D(Ψ) ̸= ∅.
(ii) Φ ∈ C1(X,R).
(iii) Ψ and Φ are G-invariant, that is Ψ(g·u) = Ψ(u) and Φ(g·u) = Φ(u) for every g ∈ G and u ∈ X.
Finally, set I(u) ≡ Ψ(u)−Φ(u) : X → (−∞,∞].
Proposition A.1. Assume u ∈ X is a critical point of I| : X → (−∞,∞]. Then u is a critical

## G Xg G

point of I : X → (−∞,∞].
51

<!-- Page 52 -->

Proof. Let u ∈ X be a critical point of I| . Then

## G Xg

Ψ(v)−Ψ(u)−Φ′(u)(v−u) ≥ 0 for each v ∈ X . (95)

## G

Fix any w ∈ X and let µ be a normalized Haar measure on G (µ(G) = 1). Since (g,u) (cid:55)→ g · u is
continuous and G is compact, we set (cf. Rudin [55, Theorems 3.20 and 3.27, and Definition 3.26])
(cid:90)
wˆ ≡ g·wdµ, (96)

## G

that is, wˆ is the unique element satisfying
(cid:90)
Λ(wˆ) = Λ(g·w)dµ for every Λ ∈ X∗.

## G

We first show wˆ ∈ X . To this end, let h ∈ G and write T : X ∋ u (cid:55)→ h·u ∈ X. For each Λ ∈ X∗, it

### G h

follows from Λ◦T ∈ X∗ and the left invariance of µ that
h
(cid:90)
Λ(h·wˆ) = (Λ◦T )(wˆ) = (Λ◦T )(g·w)dµ
h h

## G

(cid:90) (cid:90)
= Λ(hg·w)dµ = Λ(g·w)dµ = Λ(wˆ).

## G G

Since Λ ∈ X∗ is arbitrary, h·wˆ = wˆ holds for each h ∈ G.
We now prove that u is a critical point of I : X → (−∞,∞]. For w ∈ X, consider wˆ in (96).
From [55, Theorem 3.27], wˆ belongs to the closure of the convex hull of the orbit G·w. Therefore, we
can take convex combinations

### Lj Lj

(cid:88) (cid:88)
w ≡ c (g ·w), c ≥ 0, c = 1
j j,k j,k j,k j,k
k=1 k=1
such that ∥w −wˆ∥ → 0. Since Φ ∈ C1(X,R) satisfies Φ(g·u) = Φ(u) for every g ∈ G, it follows that
j
Φ′(g·u)(g·v) = Φ′(u)v for any g ∈ G and v ∈ X.
BytheconvexityandthelowersemicontinuityofΨ, weinferfrom(95)andwˆ,u ∈ X (hence, g ·u = u)
G j,k
that
0 ≤ Ψ(wˆ)−Ψ(u)−Φ′(u)(wˆ−u) ≤ liminfΨ(w )−Ψ(u)− lim Φ′(u)(w −u)
j j
j→∞ j→∞
≤ liminf (cid:2) Ψ(w )−Ψ(u)−Φ′(u)(w −u) (cid:3)
j j
j→∞

### Lj

≤ liminf (cid:88) c (cid:2) Ψ(g ·w)−Ψ(u)−Φ′(u)(g ·w−u) (cid:3)
j,k j,k j,k
j→∞
k=1

### Lj

= liminf (cid:88) c (cid:2) Ψ(w)−Ψ(u)−Φ′(g ·u)(g ·w)+Φ′(u)u) (cid:3)
j,k j,k j,k
j→∞
k=1

### Lj

= liminf (cid:88) c (cid:2) Ψ(w)−Ψ(u)−Φ′(u)(w−u) (cid:3)
j,k
j→∞
k=1
= Ψ(w)−Ψ(u)−Φ′(u)(w−u).
This means that u is a critical point of I : X → (−∞,∞] and the proof is completed. ■
52

<!-- Page 53 -->


### B Regularity for the Born-Infeld solution

In this section, we prove Proposition 2.10.
Proof. We first address the equivalence in item (i).
(a) ⇒ (b).
Assume that u is a weak solution to (BI ) (in the sense of Remark 2.9 if ∂Ω is not smooth). Fix a
ρ
domain Ω ⋐ Rn and a function ψ ∈ Y (Ω). Then, u−ψ ∈ W1,∞(Ω) and has zero boundary value. By
u
a zero extension of u−ψ outside of Ω, we see that u−ψ ∈ Lip (Rn). We then test u−ψ to (BI ) to
c ρ
deduce
(cid:90) (cid:90)
Du·(Du−Dψ)
= ρ(u−ψ).
(cid:112)
1−|Du|2

## Ω Ω

Here, due to the second in (7), the set of points where u is differentiable and |Du| < 1 has full measure
in Ω. Inequality (23) holds therein; thus we see that
(cid:90) (cid:90)
(cid:112) (cid:112)
1−|Dψ|2− 1−|Du|2 ≤ ρ(u−ψ),

## Ω Ω

which implies IΩ(u) ≤ IΩ(ψ).
ρ ρ
(b) ⇒ (a) and u ∈ W2,q(Rn) for each q ∈ [2,∞), |Du| < 1 on Rn.
loc
For a local minimizer u of I , we define a Lorentzian distance ℓ : Rn → R from 0 by
ρ
(cid:112)
ℓ(x) ≡ |x|2−(u(x)−u(0))2.
Since |Du| ≤ 1, we have ℓ ≥ 0 on Rn and moreover, in view of (20), the Lorentzian balls
L ≡ {x ∈ Rn | ℓ(x) < R}

## R

are relatively compact in Rn. Note that L contains the Euclidean ball B (0), which for convenience we

## R R

denote by B . Fix R > 0, define Ω ≡ L and let {ρ } be a sequence of smooth functions converging to

### R 4R j

ρ in L1(Ω). Taking t ∈ (0,1) with lim t = 1, we consider the solution u ∈ Y (Ω) to
j j→∞ j j tju
 (cid:32) (cid:33)

### Du

 −div j = ρ on Ω,
(cid:112) j
1−|Du |2
j


u = t u on ∂Ω.
j j
Since t u is spacelike on ∂Ω, more precisely |t u(y)−t u(x)| < |y −x| for each x,y ∈ ∂Ω with x ̸= y,
j j j
by [9] there exists a solution u , which is smooth and |Du | < 1 on Ω. We claim that u → u strongly in
j j j
C(Ω)andinW1,q(Ω)foreachq ∈ [1,∞). Thiscanbeshownbyadaptinganargumentin[22,Proposition
3.11] in the following way. First, since {t u} is relatively compact in C(∂Ω), by [22, Proposition 3.5] {u }
j j
is relatively compact in C(Ω). In particular, since |Du | ≤ 1 for each j, {u } is bounded in W1,q(Ω) for
j j
any q ∈ [1,∞]. Then there exists v ∈ Y (Ω) such that u → v, up to a subsequence, in C(Ω) and weakly
u j
in W1,q(Ω) for any q ∈ (1,∞). To show that v ≡ u, notice that from the second in Remark 2.14 we get
(cid:90) (cid:16) 1− (cid:112) 1−|Dv|2 (cid:17) = (cid:88) ∞ b ∥Dv∥2k ≤ (cid:88) ∞ b liminf∥Du ∥2k
k 2k,Ω k j 2k,Ω

### Ω j→∞

k=1 k=1
n
(cid:88)
≤ lim liminf b ∥Du ∥2k (97)
n→∞ j→∞ k j 2k,Ω
k=1
(cid:90) (cid:18) (cid:113) (cid:19)
≤ liminf 1− 1−|Du |2 .
j
j→∞ Ω
53

<!-- Page 54 -->

Moreover, since u → v in C(Ω) and ρ → ρ in L1(Ω), it holds (cid:82) ρ u → (cid:82) ρv as j → ∞. Thus we get
j j Ω j j Ω
IΩ(v) ≤ liminfIΩ(u ).
ρ
j→∞
ρj j
On the other hand, u ∈ Y (Ω) minimizes I ; thus IΩ(u ) ≤ IΩ(t u). A simple computation gives
j tju ρj ρj j ρj j
IΩ(t u) → IΩ(u),
ρj j ρ
andthereforeIΩ(v) ≤ IΩ(u). Sincethereverseinequalityholdsbyourassumptiononuandtheminimizer
ρ ρ
for I is unique, we conclude that v = u in Ω, as claimed. The argument to prove the strong convergence
ρ
u → u in W1,q(Ω) for q ∈ [1,∞) then follows verbatim that in [22, Proposition 3.11], see the second half
j
of p.32 therein.
Next, we prove the regularity of u on B . Because of (20) and a direct comparison between the

## R

Euclidean and Lorentzian distances, there exists Rˆ depending on R,c ,h such that
1

## Ω ≡ L ⋐ B . (98)


## 4R Rˆ

Indeed, in our assumption, |u(0)| ≤ c −h(0) and
1
|u(x)−u(0)| ≤ c +|u(0)|+|x|−h(x) ≤ c¯ +|x|−h(x),
1 1
where c¯≡ 2c −h(0). If x ∈ L , then by expanding

## 1 4R

|x|2 ≤ 16R2+(u(x)−u(0))2 ≤ 16R2+(c¯ +|x|−h(x))2
1
and rearranging we get
2|x|(h(x)−c¯ ) ≤ 16R2+(c¯ −h(x))2
1 1
from which the bound |x| ≤ Rˆ follows and recalling our growth assumptions on h. By a simple argument
by contradiction, we deduce from u → u in C(Ω) that for all sufficiently large j,
j
(cid:26) (cid:12) (cid:113) (cid:27)
L ρ 3R j ≡ x ∈ Ω (cid:12) (cid:12) (cid:12) ℓpj(x) ≡ |x2|−(u j (x)−u j (0))2 < 3R ⋐ Ω.
We apply [9, Lemma 2.1] and the reasoning in the proof of Theorem 4.1 therein, to deduce that there
exists a constant δ > 0 depending on the L∞ bounds for u and ρ on L ρj , which are thus uniformly
j j 3R
bounded in terms of
Rˆ, c , h and ∥ρ∥ ,

## 1 L∞(B )


## Rˆ

such that
|Du | < 1−δ on L
ρj
.
j 2R
Remark also that {u } is bounded in W2,2(L ). Since B ⊂ L ρj , we get local uniform estimates for
j 2R 2R 2R
|Du | and for the L2 norm of |D2u | on B . Thus, for any η ∈ Lip (B ), by letting j → ∞ in
j j 2R c 2R
(cid:90) Du ·Dη (cid:90)
j
= ρη,
(cid:113)
Rn 1−|Du |2 Rn
j
the dominated convergence theorem implies that (8) holds.
Finally, for any q ∈ [2,∞) we show the existence of C = C (Rˆ,c,q) such that ∥u∥ ≤ C . To
q q W2,q(BR) q
this goal, we first argue as in [22, Step 5 in Section 5.2] to obtain Du ∈ CαR(B

## R

(0)) for some α

## R

∈ (0,1).
Next, from u ∈ W2,2(Rn) and writing
loc
δ D u(x)D u(x)
a (x) ≡ ij + i j ∈ C(Rn),
ij (cid:113) (cid:16) (cid:17)3/2
1−|Du(x)|2 1−|Du(x)|2
54

<!-- Page 55 -->

we infer that u is a strong solution to
n
(cid:88)
− a (x)D u(x) = ρ(x) in Rn.
ij ij
i,j=1
Since ∥ρ∥ ≤ ∥ρ∥ ≤ c, elliptic regularity yields the desired W2,q estimate in B , see for

## L∞(B2R) L∞(B


## Rˆ


## ) R

instance [32, Chapter 9]. This completes the proof of (i).
(ii) Suppose u ∈ L∞(Rn) and ρ ∈ L∞(Rn) satisfy ∥ρ∥ + ∥u∥ ≤ c. By (i), u ∈ C1(Rn) and
∞ ∞
|Du(x)| < 1 in Rn. We prove the assertion by contradiction and suppose that there exist {ρ } ,{u } ∈
i i i i
L∞(Rn), with u a solution with source ρ , and points {x } ⊂ Rn such that
i i i i
∥ρ ∥ +∥u ∥ ≤ c, |Du(x )| → 1 as i → ∞.
i ∞ i ∞ i

### Define

u¯ (x) ≡ u (x+x ), ρ¯(x) ≡ ρ (x+x ).
i i i i i i
Then, u¯ isa(strong)solutionwithsourceρ¯ onRn, hencealocalminimizerofI . Sinceu¯ is1-Lipschitz,
i i ρ¯i i
we may also assume that u¯ → u¯ in C (Rn), and u¯ is also 1-Lipschitz with ∥u¯∥ ≤ c. The inequality
i ∞ loc ∞ ∞
∥ρ¯∥+∥u¯ ∥ ≤ c and [9, Theorem 3.2] imply that u¯ has no light segments in the following quantitative
i i ∞ i
sense: for each r > 0, there exists R = R(r) > 0 such that for every i ≥ 1,
(cid:26) (cid:12) (cid:113) (cid:27)
Lρ r ¯i ≡ x ∈ Rn (cid:12) (cid:12) ℓρ¯i(x) ≡ |x|2−(u¯ i (x)−u¯ i (0))2 < r ⊂ B R .
(cid:12)
According to the monotonicity formula in [9, Lemma 2.1], we may find α ∈ (0,1/n) and C = C(n) > 0
such that
Cexp (cid:0) r2c2+1 (cid:1) (1−|Du¯ i (0)|) α 2 ≥ r−n (cid:90) (cid:16) 1−|Du¯ i |2 (cid:17)α+1 +r2−n (cid:90) (cid:12) (cid:12)D2u¯ i (cid:12) (cid:12) 2 .

## L

ρ
r
¯i

## L

ρ
r
¯i
From |Du¯ (0)| → 1 and the fact that r > 0 can be arbitrary, it follows that |Du¯ | = 1 and D2u¯ = 0
i ∞ ∞
a.e. in Rn. Thus, u¯ (x) = a · x + b for some a ∈ Rn, b ∈ R with |a| = 1, however, this contradicts
∞
∥u¯ ∥ ≤ c and concludes the proof. ■
∞ ∞

### References

[1] C.O. Alves and D.C. de Morais Filho, Existence and concentration of positive solutions for a
Schr¨odinger logarithmic equation. Z. Angew. Math. Phys. 69 (2018), no. 6, Paper No. 144, 22 pp.
24
[2] A. Ambrosetti and P.H. Rabinowitz, Dual variational methods in critical point theory and applications. J. Funct. Anal. 14 (1973), 349–381. 3, 5
[3] D. Arcoya, C. Bereanu and P.J. Torres, Critical Point Theory for the Lorentz Force Equation. Arch.

### Rational Mech. Anal. 232 (2019), 1685–1724. 5

[4] D. Arcoya, C. Bereanu and P.J. Torres, Lusternik-Schnirelman theory for the action integral of the
Lorentz force equation. Calc. Var. Partial Differential Equations 59 (2020), no.2, Paper No. 50, 32
pp. 5
[5] A. Azzollini, Ground state solution for a problem with mean curvature operator in Minkowski space.
J. Funct. Anal. 266 (2014), 2086–2095. 6, 8
55

<!-- Page 56 -->

[6] A. Azzollini,On a prescribed mean curvature equation in Lorentz-Minkowski space. J. Math. Pures

### Appl. 106 (2016), 1122–1140. 6, 7

[7] T. Bartsch and M. Willem, Infinitely many radial solutions of a semilinear elliptic problem on RN.
Arch. Rational Mech. Anal. 124 (1993), 261–276.
[8] T. Bartsch and M. Willem, Infinitely many nonradial solutions of a Euclidean scalar field equation.

### J. Funct. Anal. 117 (1993), 447–460. 8, 19

[9] R. Bartnik and L. Simon, Spacelike hypersurfaces with prescribed boundary values and mean curvature. Comm. Math. Phys. 87 (1982/83), no. 1, 131–152. 3, 10, 53, 54, 55
[10] C. Bereanu,P. Jebelean and J. Mawhin, The Dirichlet problem with mean curvature operator in
Minkowski space - a variational approach. Adv. Nonlinear Stud. 14 (2014), 315–326. 3
[11] H. Berestycki, T. Gallou¨et and O. Kavian, E´quations de champs scalaires euclidiens non lin´eaires
dans le plan. C. R. Acad. Sci. Paris S´er. I Math. 297 (1983), no.5, 307–310.
[12] H. Berestycki and P.-L. Lions, Nonlinear scalar field equations. I. Existence of a ground state. Arch.

### Rational Mech. Anal. 82 (1983), no. 4, 313–345. 6

[13] H. Berestycki and P.-L. Lions, Nonlinear scalar field equations. II. Existence of infinitely many
solutions. Arch. Rational Mech. Anal. 82 (1983), no. 4, 347–375. 6, 23
[14] H.BerestyckiandP.-L.Lions,Existence d’´etats multiples dans des´equations de champs scalaires non
lin´eaires dans le cas de masse nulle, C. R. Acad. Sci. Paris S´er. I Math. 297(1983), no. 4, 267–270.
6
[15] D. Bonheure, P. d’Avenia and A. Pomponio, On the electrostatic Born-Infeld equation with extended
charges. Comm. Math. Phys. 346 (2016), no. 3, 877–906. 3, 11
[16] D. Bonheure, C. De Coster and A. Derlet, Infinitely many radial solutions of a mean curvature
equation in Lorentz-Minkowski space. Rend. Istit. Mat. Univ. Trieste 44 (2012), 259–284. 6, 8, 10
[17] D.BonheureandA.Iacopetti, A sharp gradient estimate and W2,q regularity for the prescribed mean
curvature equation in Lorentz-Minkovski space. Arch. Rational Mech. Anal. 247 (2023), no. 5, Paper

### No. 87, 44 pp. 3

[18] M. Born and L. Infeld, Foundations of the new field theory. Proc. Roy. Soc. London Ser. A 144
(1934), 425–451. 2
[19] H. Brezis, Functional analysis, Sobolev spaces and partial differential equations. Universitext,

### Springer, New York, 2011, 12, 15

[20] H. Brezis and M. Sibony, E´quivalence de deux in´equations variationnelles et applications. Arch.

### Rational Mech. Anal. 41 (1971), 254–265. 5

[21] J. Byeon, S-H. Choi,Y. Kim, S-H. Moon, Least energy solution for a scalar field equation with a
singular nonlinearity. Proc. Roy. Soc. Edinburgh Sect. A 151 (2021), 93–109. 6
[22] J. Byeon, N. Ikoma, A. Malchiodi and L. Mari, Existence and regularity for prescribed Lorentzian
mean curvature hypersurfaces, and the Born-Infeld model. Ann. PDE 10 (2024), no. 4, 86 pp. 3, 10,
12, 15, 53, 54
[23] A. Cellina, On the regularity of solutions to the plastoelasticity problem. Adv. Calc. Var. 13 (2020),
no.1, 1–14. 5
56

<!-- Page 57 -->

[24] K.C. Chang, Variational methods for non-differentiable functionals and their applications to partial
differential equations. J. Math. Anal. Appl. 80 (1981), 102–129. 5
[25] F.H.Clarke,OptimizationandNonsmoothAnalysis.CanadianMathematicalSocietySeriesofMonographs and Advanced Texts. A Wiley-Interscience Publication, John Wiley & Sons, Inc., New York
(1983). 5
[26] J.N. Corvellec, Quantitative deformation theorems and critical point theory. Pac. J. Math. 187
(1999), 263–279. 5, 24
[27] J.N. Corvellec, M. Degiovanni and M. Marzocchi, Deformation properties for continuous functionals
and critical point theory. Topol. Methods Nonlinear Anal. 1 (1993), 151–171. 5, 24
[28] M. Degiovanni and M. Marzocchi, A critical point theory for nonsmooth functionals. Annali Mat.

### Pura Appl. 167 (1994), 73–100. 5

[29] I. Ekeland, Nonconvex minimization problems, Bull. Amer. Math. Soc. 1 (1979), 443–103.
[30] I.EkelandandJ.M.Lasry, On the number of periodic trajectories for a Hamiltonian flow on a convex
energy surface. Ann. Math. 112 (1980), p. 283–319.
[31] B. Gidas and J. Spruck, Global and local behavior of positive solutions of nonlinear elliptic equations.

### Comm. Pure Appl. Math. 34 (1981), no. 4, 525–598. 10

[32] D. Gilbarg and N.S. Trudinger, Elliptic partial differential equations of second order. Classics Math.

### Springer-Verlag, Berlin, 2001. 24, 55

[33] J. Hirata, N. Ikoma and K. Tanaka, Nonlinear scalar field equations in RN: mountain pass and
symmetric mountain pass approaches. Topol. Methods Nonlinear Anal. 35 (2010), no.2, 253–276. 6,
44
[34] J. Hirata and K. Tanaka, Nonlinear scalar field equations with L2 constraint: mountain pass and
symmetric mountain pass approaches. Adv. Nonlinear Stud. 19 (2019), no.2, 263–290. 6
[35] N. Ikoma, Multiplicity of radial and nonradial solutions to equations with fractional operators. Commun. Pure Appl. Anal. 19 (2020), no.7, 3501–3530. 6
[36] V.I. Istr˘a¸tescu, Fixed point theory. Math. Appl., 7 D. Reidel Publishing Co., Dordrecht-Boston,

### Mass., 1981 42

[37] G. Katriel, Mountain pass theorems and global homeomorphism theorems. Ann. Inst. H. Poincar´e

### Anal. Non Lin´eaire 11 (1994), 189–209. 5

[38] L. Jeanjean, On the existence of bounded Palais-Smale sequences and application to a Landesman-
Lazer-type problem set on RN. Proc. Roy. Soc. Edinburgh Sect. A 129 (1999), no. 4, 787–809. 3,
24
[39] L. Jeanjean and S.-S. Lu, Nonlinear scalar field equations with general nonlinearity, Nonlinear Anal.
190 (2020), 111604, 28. 23
[40] L. Jeanjean and K. Tanaka, a remark on least energy solutions in RN, Proc. Amer. Math. Soc. 131
(2002), no.8, 2399–2408. 9
[41] L.JeanjeanandJ.F.Toland,Bounded Palais-Smale mountain-pass sequences.C.R.Acad.Sci.Paris
S´er. I 327 (1998), 23–28. 3, 24
57

<!-- Page 58 -->

[42] l. Jeanjean and V. Rˇadulescu, Nonhomogeneous quasilinear elliptic problems: linear and sublinear
cases. J. Anal. Math. 146(2022), 327–350. 3, 5, 6
[43] A. Ioffe and E. Schwartzman, Metric critical point theory 1. Morse regularity and homotopic stability
of a minimum. J. Math. Pures Appl. 75 (1996), 125–153. 5
[44] J. Kobayashi and M. Oˆtani, The principle of symmetric criticality for non-differentiable mappings,

### J. Funct. Anal. 214 (2004), 428–449. 22, 51

[45] A. Kristaly, C. Varga, V. Varga, A nonsmooth principle of symmetric criticality and variationalhemivariational inequalities. J. Math. Anal. Appl. 325 (2007), 975–986.
[46] P.-L. Lions, Sym´etrie et compacit´e dans les espaces de Sobolev. [Symmetry and compactness in
Sobolev spaces], J. Funct. Anal. 49 (1982), no.3, 315–334. 19
[47] J.E. Marsden and F.J. Tipler, Maximal hypersurfaces and foliations of constant mean curvature in
general relativity. Phys. Rep. 66 (1980), no. 3, 109–139. 2
[48] M.Marzocchi,Multiple solutions of quasilinear equations involving an area-type term.J.Math.Anal.
Appl. 196(1995), 1093–1104.
[49] J. Mederski, General class of optimal Sobolev inequalities and nonlinear scalar field equations. J.

### Differential Equations 281(2021), 411–441 8

[50] J. Mederski and A. Pomponio, Born-Infeld problem with general nonlinearity. J. Differential Equations 370 (2023), 470–497. 6, 8, 9
[51] B. Pellacci and M. Squassina Unbounded critical points for a class of lower semicontinuous functionals. J. Differential Equations 201 (2004), 25–62 5
[52] B. Pellacci and M. Squassina Mountain Pass solutions for quasi-linear equations via a monotonicity
trick. J. Math. Anal. Appl. 381(2011), 857–865
[53] P. Pucci and J. Serrin, The Maximum Principle. Progress in Nonlinear Differential Equations and
their Applications 73, Birkh¨auser Verlag, Basel, 2007, x+235 pp.
[54] P. H. Rabinowitz, Minimax methods in critical point theory with applications to differential equations. CBMS Regional Conference Series in Math., vol. 65, Amer. Math. Soc., Providence, RI, 1986.
5, 44
[55] W. Rudin, Functional analysis. Internat. Ser. Pure Appl. Math. McGraw-Hill, Inc., New York, 1991.
52
[56] M. Struwe, Multiple solutions of differential equations without the Palais-Smale condition. Math.

### Ann. 261(1982), no.3, 399–412. 6

[57] M. Struwe, The existence of surfaces of constant mean curvature with free boundaries. Acta Math.
160 (1988), 19–64 3, 24
[58] M. Struwe, Critical points of embeddings of H1,n into Orlicz spaces. Ann. Inst. H. Poincar´e Anal.

### Non Lin´eaire 5 (1988), no.5, 425–464. 24

[59] M. Struwe, Variational methods : Applications to nonlinear partial differential equations and Hamiltonian systems. Fourth edition, Springer-Verlag, Berlin, Heidelberg, 2008 6
58

<!-- Page 59 -->

[60] C. A. Stuart, J. F. Toland A variational method for boundary value problems with discontinuous
nonlinearities. Journal of the London Mathematical Society2-21(1980), no. 2, 319–328. 6
[61] M. Squassina, On Palais’ principle for non-smooth functionals. Nonlinear Anal. 74 (2011), 3786–
3804.
[62] M. Squassina, On the Struwe-Jeanjean-Toland monotonicity trick. Proc. Roy. Soc. Edinburgh Sect.

### A 142 (2012), no.1, 155–169. 5, 6, 9

[63] A. Szulkin, Minimax principles for lower semicontinuous functions and applications to nonlinear
boundary value problems. Ann. Inst. H. Poincar´e Anal. Non Lin´eaire 3 (1986), no. 2, 77–109. 3, 5,
24, 25, 44
[64] J. Van Schaftingen, Symmetrization and minimax principles. Comm. Contemp. Math. 7 (2005),
463–481. 9
[65] Y. Yang, Nonlinear problems inspired by the Born-Infeld theory of electrodynamics. Adv. Nonlinear

### Stud. 24 (2024), no.1, 222–246. 3

[66] M. Willem, Minimax theorems. Progress in Nonlinear Differential Equations and their Applications,

## Birkh¨auser Boston, Inc., Boston, MA, 1996. 19

59