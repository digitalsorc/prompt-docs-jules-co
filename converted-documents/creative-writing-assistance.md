---
title: "Creative Writing Assistance"
original_file: "./Creative_Writing_Assistance.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["multimodal"]
keywords: ["cid", "each", "then", "decoupling", "let", "dec", "lqn", "theorem", "lemma", "write"]
summary: "<!-- Page 1 -->

Restricted projections and Fourier decoupling in
Qn
p
Ben Johnsrude, Zuo Lin

### Abstract

We prove a restricted projection theorem for Borel subsets of Qn in the regime p > n. p
This generalizes results of Gan-Guo-Wang in the real setting. 1 Introduction
Let 1 ≤ m < n, and V = (v ,...,v ) be a tuple of vectors in Qn."
related_documents: []
---

# Creative Writing Assistance

<!-- Page 1 -->

Restricted projections and Fourier decoupling in
Qn
p
Ben Johnsrude, Zuo Lin

### Abstract

We prove a restricted projection theorem for Borel subsets of Qn in the regime p > n.
p
This generalizes results of Gan-Guo-Wang in the real setting.
1 Introduction
Let 1 ≤ m < n, and V = (v ,...,v ) be a tuple of vectors in Qn. Write P : Qn → Qm for
1 k p V p p
the function
  
v⊥ x
1 1
. .
P V (x) =   . .     . .  
v⊥ x
m n
We will be interested in the problem of determining the relation between the sizes of a Borel
set A ⊆ Qn and its projection P [A], for various choices of V and A. In real Euclidean space
p V
Rn, much work has been done: Marstrand’s projection theorem [11] states that
dim(P [A]) = min(dim(A),m) for a.e. V such that |v ∧···∧v | ∼ 1.

### V 1 k

Recent developments in Fourier analysis have permitted analogous results to be proved when
the tuple of vectors V is set to range over a much more sparse set, e.g. a curve. Again in the
real case, [4] demonstrated that, for γ any smooth nondegenerate curve in Rn and A ⊆ Rn
a Borel set of dimension dim(A), it holds that for almost every t and each 1 ≤ m < n, the
orthogonal projection of A onto the span of γ(1)(t),...,γ(m)(t) has dimension min(dim(A),m).
Theorems of this form are termed restricted projection theorems.
We now state our main result.
Theorem 1.1. Let A be a Borel subset of Qn. For each t ∈ Z , let V = (γ(1)(t),...,γ(m)(t)),
p p
where γ(t) = (t,..., tn) is the moment curve. Then, for almost every t ∈ Z , it holds that
1! n! p
dim (P [A]) = min(m,dim (A)).

## H V H

Here and throughout dim denotes the Hausdorff dimension of a metric space.

## H

1
4202
nuJ
72
]AC.htam[
1v37491.6042:viXra

<!-- Page 2 -->

The restricted projection theorem has applications in homogeneous dynamics, see [8], [9]
and [10]. Using the (m,n) = (1,3) case, Lindenstrauss–Mohammadi and Lindenstrauss–
Mohammadi–Wang proved effective density and equidistribution for certain 1-parameterized
unipotent flow in quotient of SL (C) and SL (R) × SL (R) with finite volume. Using the
2 2 2
(m,n) = (2,5) case, Lindenstrauss–Mohammadi–Wang–Yang proved effective equidistribution
for certain unipotent flow in SL (R)/SL (Z).
3 3
The equidistribution results on certain unipotent flow in compact quotient of SL (Q ) ×
2 p
SL (Q ) has some important applications in number theory. It plays a crucial role in the
2 p
proofs of uniform distribution of Heegner points by Vatsal, and Mazur conjecture on Heegner
points by C. Cornut; and their generalizations in their joint work on CM-points and quaternion
algebras[13, 3, 2]. Motivated by these applications, we seek to prove an effective density and
equidistribution result on certain unipotent flow in compact quotient of SL (Q ) × SL (Q ),
2 p 2 p
which lead us to prove a restricted projection in the p-adic setting.
The purpose of this paper is to generalize the results of [4] to the p-adic setting. One of the
motivations is an application to homogeneous dynamics; see Theorem 1.3.
We set out the following notation and convention:
• γ(t) = (t, t2,..., tn) is a curve Z → Qn;
2! n! p p
• for each t ∈ Z and 1 ≤ m < n, we set Π(m) be the following projection from Qn to Qm:
p t p p
tn−1 tn−m
Π(m)(x ,...,x ) = (x +tx +...+ x ,...,x +tx +...+ x ),
t 1 n 1 2 (n−1)! n m m+1 (n−m)! n
i.e.
   
γ(1)(t)⊤ x
1
Π( t m)(x 1 ,...,x n ) =   . . .   .  . . .   ;
γ(m)(t)⊤ x
n
• µ is the Haar measure on Qn with normalized measure µ(Zn) = 1;
p p
• |·| covering number or packing number (which agree in Q );
b p
• # cardinality of a finite set;
• ν will always be the uniform probability measure on a finite set F, unless otherwise
specified;
• 1 will always be the characteristic function on the set A.

## A

The following projection theorem is the one needed in the proof of effective equidistribution
of unipotent flow on quotient of SL (Q )×SL (Q ). The statement of the following theorem is
2 p 2 p
a generalized verision of the same as Theorem 5.1 in [8] in p-adic setting. By an application of
Frostman’s lemma, it implies Theorem 1.1.
Theorem 1.2. For t ∈ Z , Let α ∈ (0,m), b < b ∈ (0,1) be three parameters. Suppose
p 0 1
F ⊆ Zn is a finite subset satisfying the following α-dimensional condition at scales ≥ b :
p 0
#(F ∩B(x,b))
≤ C(b/b )α ∀x ∈ Zn ∀b ≥ b . (1.1)
# F 1 p 0
2

<!-- Page 3 -->

Let ν be the uniform probability measure on F and ν =
(cid:0) Π(m)(cid:1)
ν be the pushforward measure.
t t ∗
Then, for all ε ∈ (0, α ), there exists C > 0 such that ∀b ≥ b , there exists J s.t.
100 ϵ 0 b
µ(Z \J ) ≤ C bε s.t. ∀t ∈ J , there exists F ⊆ F with ν(F\F ) ≤ C bε s.t., ∀w ∈ F ,
p b ε b b,t b,t ε b,t
√
ν (cid:0) B(Π(m)(w),b) (cid:1) ≤ C (cid:16) b (cid:17)α−O( ε) .
t t ε b
1
√ √
The term O( ε) can be taken to be 4·1010n ε. The constant C (c) can be chosen as
n,p,ε
(cid:16) (cid:17)
C = 4max(1,C)exp 104(logp)ε−5nlognn20n2 .
ε
We now present the following application of Theorem 1.2 to the setting of homogeneous
dynamics on quotient of SL (Q )×SL (Q ). We first set out some notation. Let r = sl (Q ) be
2 p 2 p 2 p
the trace-zero 2×2 matrices over Q , and equip r with the maximum-entry norm, with respect
p
to | · | . For each r ∈ Z , we write ξ : r → Q for the map
p p r p
ξ (w) = w −2rw −w r2,
r 12 11 21
where w denotes the corresponding matrix entry of w.
ij
Theorem 1.3. Let 0 < α < 1,0 < b = p−l0 < b = p−l1 < 1 be three parameters. Let
0 1
F ⊆ B (0,b ) (the closed ball in r centered at 0 of radius b ) be such that
r 1 1
#(F ∩B (w,b))
r ≤ D′(b/b )α,
1

## #F

for all w ∈ r and all b ≥ b , and some D′ ≥ 1. Let 0 < ε < 0.01 and let J be a metric ball in
0

## Z .

p
Then there exists J′ ⊆ J such that µ(J′) ≥ (1− 1)µ(J) satisfying the following. For each
p
r ∈ J′, there exists a subset F ⊆ F with
r
(cid:18) (cid:19)
1

## #F ≥ 1− #F

r
p
such that for all w ∈ F and b ≥ b we have
r 0
#{w′ ∈ F : |ξ (w′)−ξ (w)| ≤ b}
r r p ≤ C (b/b )α−ε, (1.2)
ε 1

## #F

where C depends on ε,#J, and D′.
ε
(cid:0) (cid:1)
Remark 1.4. The maps ξ may alternately be written as ξ (w) = Ad (w) , where u =
r r ur 12 r
(cid:18) (cid:19)
1 r
and Ad is the adjoint action of SL (Q ) on its Lie algebra sl (Q ).
0 1 2 p 2 p
Proof of Theorem 1.3 from Theorem 1.2. Let ε = (10−30ε)2. Identifying r = sl (Q ) with Q3
1 2 p p
(with the latter equipped with the usual ℓ∞ norm), we may appeal to the (m,n) = (1,3) case
of Theorem 1.2 with this ε . Choose l such that
1 2
∞
(cid:88) 1
C p−ε1l < µ(J).
ε1
p
l=l2
3

<!-- Page 4 -->

If l > l , let
2 0
C′ = (pl2)α−ε,
ε1
which depends only on ε and µ(J). We then have
√
1 ≤ C′ (b )(p−l2)α−O( ε)
ε1 0
≤ C′ (b )α−ε.
ε1 0
Thus we may take J′ = J and F = F, and 1.2 holds trivially.
r
Now we assume l ≤ l . Let J′ = (cid:84)l0 J ∩J, where J is the set obtained from Theorem
2 0 l=l2 p−l p−l

### We compute:

∞
(cid:88)
µ(J′) ≥ µ(J)− µ(Z \J )
p p−l
l=l2
∞
(cid:88)
≥ µ(J)− C p−ε1l
ε1
l=l2
(cid:18) (cid:19)
1
≥ 1− µ(J).
p
For all r ∈ J′, let F = (cid:84)l0 F , where the sets F are as obtained from Theorem
r l=l2 p−l,r p−l,r

### From the choice of l and the union bound, we conclude that #(F \ F ) ≤ 1#F, so

2 r p

## #F ≥ (1− 1)#F.

r p
Now, for all w ∈ F and l ≤ l ≤ l , by Theorem 1.2, we have
r 2 0
#{w′ ∈ F : |ξ (w′)−ξ (w)| ≤ p−l} ≤ C (b/b )(α−ε)(l1−l)#F.
r r p ε1 1
so that 1.2 holds.
√
Finally, we consider scales p−l > p−l2, i.e. l < l . In this scale, we let C′ ≥ pl2(α−O( ε)). We
2 ε
have
1 ≤ C′ p−l2(α−ε) ≤ C′ (b/b )(α−ε)(l1−l),
ε1 ε1 1
so that 1.2 holds trivially.
Proof of Theorem 1.1 from Theorem 1.2. Identicaltothe“ProofofTheorem1.2assumingTheorem 2.1,” from [4]. Note that the Frostman lemma holds for Borel sets in compact metric
spaces, and that dim (Zm) = m. Note also that the relevant covering lemma is valid in

### H p

separable metric spaces, and that µ is doubling.
We mention one final result of this paper. In the interest of obtaining explicit bounds
for the projection theorems, motivated by the problem of producing effective estimates in the
homogeneous dynamics application, we have in particular needed a fully explicit bound on padic decoupling for the moment curve; this is proved in Theorem 6.1 below. To our knowledge,
this gives the first fully explicit bound for the main conjecture of Vinogoradov’s mean value
theorem in the range n ≥ 3, which we state here.
4

<!-- Page 5 -->

Theorem 1.5 (Explicit Vinogradov bound). For n ≥ 2,s ≥ 2, and N ≥ 2, we write
(cid:40) (cid:41)
s
(cid:88)
J (N) = # a,b ∈ [N]n : (ad −bd) = 0 ∀1 ≤ d ≤ n ,
s,n j j
j=1
which is the number of solutions to the Vinogradov system of Diophantine equations. For each
such s,n, and each N ≥ exp(exp(3n(4nlogn+1))), we have
(cid:16) (cid:17)
J s,n (N) ≤ exp 105se3n(logN)1− 4nlo 1 gn+1 (Ns +N2s−n(n 2 +1) ).
Proof of Theorem 1.5, assuming Theorem 6.1. We will first show the inequality
(cid:16) (cid:17)
J (N) ≤ exp 6·104sε−4nlognn12n2 N2sε(Ns +N2s−n(n+1) ) (1.3)
s,n 2
for each ε ∈ (0,1). Subsequently, we will optimize this estimate over ε.
Let p ∈ [n,2n] be a prime. Assume temporarily that N = pℓ for some ℓ ∈ N. For each
1 ≤ a ≤ N integral, we write I = a+pℓZ ; these form a partition of Z . Let {U } be the
a p p Ia,a a∈[N]
associated family of anisotropic boxes adapted to the n-dimensional moment curve, as defined
in Section 6.1 below. By Theorem 6.1,
(cid:16) (cid:17)
Dec ({U } ) ≤ exp 104(logp)ε−4nlognn10n2 pεℓ,
ℓ2Ln(n+1) Ia,a a∈[N]
for each ε ∈ 1. By Lemma 5.1, we have

## N

(cid:16) (cid:17)
Dec ({U } ) ≤ exp 104(logp)ε−4nlognn10n2 pεℓ(1+p ℓ(1−n(n+1)))
ℓ2L2s Ia,a a∈[N] 2 2s
For each 1 ≤ a ≤ N integral, write g : Qk → C for the function
a p
g (x) = χ(x·γ(a))1 (x).
a p−ℓnZn
p
Then the Fourier support of g is γ(a)+pℓnZn ⊆ U . Thus, by decoupling,
a p Ia,a
(cid:13) (cid:13)2s
(cid:13) (cid:13) (cid:88) N g (cid:13) (cid:13) ≤ 22sexp (cid:16) 2·104s(logp)ε−4nlognn10n2 (cid:17) p2sℓε(1+pℓ(s−n(n+1)))p(n+s)ℓ.
(cid:13) a(cid:13) 2
(cid:13) (cid:13)
a=1 L2s(Qn)
p
By a standard manipulation, the left-hand side is pℓnJ (N). Thus, in this case, we obtain
s,n
(cid:16) (cid:17)
J (N) ≤ 22sexp 2·104s(logp)ε−4nlognn10n2 N2sε(Ns +N2s−n(n+1) )
s,n 2
If instead pℓ < N < pℓ′, then the preceding implies
(cid:16) (cid:17)
J (N) ≤ 22sp2s(1+ε)exp 2·104s(logp)ε−4nlognn10n2 N2sε(Ns +N2s−n(n+1) ).
s,n 2
Finally, appealing to n ≤ p ≤ 2n, and various elementary estimates, we conclude that
(cid:16) (cid:17)
J (N) ≤ exp 6·104sε−4nlognn11n2 N2sε(Ns +N2s−n(n+1) ).
s,n 2
5

<!-- Page 6 -->

Finally, interpolating between the cases 1 < ε < 1, we obtain 1.3.
ℓ+1 ℓ
Finally, we select ε = e3n(logN)− 4nlo 1 gn+1 in 1.3, using the lower bound on N. It transpires
that
(cid:18) (cid:19)

## J (N)

log s,n ≤ 6·104s(logN)4n 4n lo l g og n+ n 1 +2e3ns(logN)4n 4n lo l g og n+ n 1.

### Ns

+N2s−n(n+1)
2
By trivial estimates, we conclude.
Finally, we outline the remaining sections. In Section 2, we reduce the proof of Theorem 1.2
to a problem of covering sets with tubes, which we refer to as a Kakeya estimate. In Section 3,
we demonstrate that the Kakeya estimate may be proved with a suitable decoupling theorem.
In Section 4, we prove the decoupling theorem, assuming that the usual Bourgain-Demeter-
Guth decoupling theorem for the moment curve may be extended to the p-adic setting. Finally,
in the appendices, we discuss the proof of moment curve decoupling in the p-adic setting, by
modifying an argument of [5].
1.1 Acknowledgements
We would like to thank Amir Mohammadi and Hong Wang for suggesting this problem. We
would also like to thank Terence Tao and Zane Kun Li for helpful suggestions and comments.
2 Discretization
In this section, we reduce the projection theorem 1.2 to a Kakeya estimate, whose proof will
be established by Fourier analysis in following sections.
Let δ = p−l and let D(m) = {x+plZm : x ∈ {0,...,pl −1}m} be the set of δ-balls in Zm.
p p
Let T(m) = Zn ∩ {(Π(m))−1(D) : D ∈ D(m)}. Elements in T are tilted δm × 1n−m boxes. We
t p t t
will use T(m) to denote elements in T . We will drop the superscript if it is clear that we are
t t
dealing with the (m,n) case.
Theorem 2.1 (Kakeya estimate). Let δ,δ ∈ p−N with δ > δ . Let Λ be a maximal δ-separted
0 0 δ
set of Z . Given ε > 0 and α ∈ (0,m), let ν be a finite non-zero Borel measure supported in Zn
p p
with cδ
α
0(ν) = sup
x∈Qn p ,r>δ0
ν(B
r
(
α
x,r)) < ∞. Take W
θ

## ⊂ T

θ
arbitrary and denote W := ∪
θ∈Λ δ

## W

θ
.
Suppose that
(cid:88)
1 (x) ≥ cδε−1, ∀x ∈ supp(ν).

## T


## T∈W

Then
√
# W ⩾ C (c)·ν(Qn)cδ0(ν)−1δ−1−αδO( ϵ)
n,p,ε p α
√
Here it is important that the constant C (c) does not depend on δ. The term O( ε) can be
√ n,p,ε
taken to be 1010n ε. The constant C (c) can be chosen as
n,p,ε
(cid:16) (cid:17)
C (c) = min(1,cε−1)exp −104(logp)ε−5nlognn20n2 .
n,p,ε
6

<!-- Page 7 -->

Proof of Theorem 1.2 assuming Theorem 2.1.
√
The proof is a finitary version of the one in section 2 of [4]. Let ε = 1010n 2ε. Fix
0
s = α−2ε < α. Note that s < α−2ε−ε . For each b ≥ b and each b-separated set Λ ⊆ Z ,
0 0 0 b p
we define the set
(cid:110) (cid:111)
Fbad = w ∈ F : ν({w′ ∈ F : |Π(m)(w)−Π(m)(w′)| ≤ b}) > cb0(ν)bs
b,t t t α
for all t ∈ Λ .
b
We will first demonstrate that there exists C(α,s) such that
(cid:88)
ν(Fbad) ≤ C(α,s)b2ε−1.
b,t
t∈Λ
b
Suppose not, we have that
(cid:88)
ν(Fbad) > Cb2ε−1.
b,t
t∈Λ
b
Note that for all t, (cid:12) (cid:12)Π(m)(Fbad) (cid:12) (cid:12) ≤ 1 b−s. Hence we could cover it by a collection D of
balls D where #D ≤ 1 t b−s. b,t Let b W c = b α 0( { ν) p−1(D) (cid:84)Zn : D ∈ D }, W = (cid:83) W . Consider t the
t cb
α
0(ν) t t p t t t
following set
A = {(t,w) ∈ Λ ×F : w ∈ Fbad}.
b b,t
Let λ denote the counting measure on Λ . We have
b
(cid:88)
(λ⊗ν)(A) = ν(Fbad) > Cb2ε−1.
b,t
t∈Λ
b

### Therefore ˆ

#{t ∈ Λ : w ∈ Fbad}dν(w) > Cb2ε−1,
b b,t
sothat,dividingtheintegralintothedomainswheretheintegrandislarger/smallerthan Cb2ε−1,
2
b−1ν (cid:16) (cid:8) w ∈ F : (cid:88) 1 (x) > C b2εb−1 (cid:9) (cid:17) + C b2ε−1 > Cb2ε−1,

## T

2 2

## T∈W

i.e.
ν (cid:16) (cid:8) w ∈ F : (cid:88) 1 (x) > C b2ε−1 (cid:9) (cid:17) > C b2ε.

## T

2 2

## T∈W

Let Fbad = (cid:8) w ∈ F : (cid:80) 1 (x) > Cb2ε−1 (cid:9) , so that ν(Fbad) > Cb2ε. Note that for all
x ∈ Fbad, b (cid:80) 1 (x) > Cb2 T ε ∈ − W 1. T 2 b 2
b T∈W T 2
We apply Theorem 2.1 to ν| , scale b and 2ε. There exists C
Fbad 2ε,α
b

## C

# W ≥ C · b2εcb0(ν)−1b−1−αbε0.
2ε,α 2 α
By pigeonholing, this implies that there exists t ∈ Λ such that
b

## C

# W ≥ C · b2εcb0(ν)−1b−αbϵ0.
t 2ε,α 2 α
7

<!-- Page 8 -->

This is a contradiction to the assumption that #W < 1 b−s if C > 2 . Therefore,
t cb
α
0(ν) C2ε,α
(cid:88) 4
ν(Fbad) ≤ b2ε ·b−1.
b,t C
2ε,α
t∈Λ
b
Now let E be the ‘exceptional’ set of parameters t ∈ Z where Fbad is large, namely,
b p b,t
4
E = {t ∈ Z : ν(Fbad) > bε}.
b p b,t C
2ε,α
Pick a maximal b-separated set of E and extend it to be a maximal b-separated set Λ in Z ,
b b p
we have
4 4
b−1 ·µ(E )· b ε ≤ #(Λ ∩E )· b ε
b 2 b b 2

## C C

2ε,α 2ε,α
(cid:88)
≤ ν(Fbad)
b,t
t∈Λ (cid:84)E
b b
4
≤ bε ·b−1.

## C

2ε,α
Therefore, µ(E ) < bε. Let C = max{cb0(ν), 4 } and J = Z \E , we complete the
b ε α C2ε,α b p b
proof.
3 Kakeya estimate via decoupling cones over moment
curves
In this section, we formulate the decoupling estimate Proposition 3.1, and indicate how it may
be used to prove Theorem 2.1. We begin by setting out some notation that will be helpful in
studying the wave packet expansions of functions with restricted Fourier support.
For each θ ∈ Λ and α,β ∈ p−Z, write
δ
A = [α−1γ(1)(θ),...,α−1γ(m)(θ),β−1γ(m+1)(θ),...,β−1γ(n)(θ)]. (3.1)
θ,α,β
When the third subscript is supressed, we will understand it to be 1. Write also
τ = A [Zn].
θ θ,δ−1 p
Notice in particular that τ has dimensions δ−1 ×···×δ−1 ×1×···×1, with m copies of δ−1
θ
and (n − m) copies of 1. If f has Fourier support within τ , then f may be expanded into
θ θ θ
wave packets of the form a χ(x·γ(θ))1 (x) for a ∈ C and T a translate of A−⊤ Zn. Note in

### T T T θ,δ−1 p

particular that each T has p-adic volume δ−(n−m).
It will be convenient to observe that

## A−1 = A (3.2)

θ,1 −θ,1

### Indeed, when i ≥ j,

(cid:88) n (cid:88) i (−1)k−j
(A A ) = (A ) (A ) = θi−j
θ,1 −θ,1 i,j θ,1 i,k −θ,1 k,j
(i−k)!(k −j)!
k=1 k=j
8

<!-- Page 9 -->


### The sum may be rewritten as

(cid:88) k (−1)k−j 1 (cid:88) i−j (cid:18) i−j (cid:19) 1
= (−1)h = (1−1)i−j,
(i−k)!(k −j)! (2r)! h (i−j)!
k=j h=0
and the claim follows.
Proposition 3.1 (Decoupling estimate). For each ε ∈ (0,1) and n ∈ N, we may find D ≥ 1
n,p,ε
such that the following holds. Suppose δ ∈ p−N and Λ is a δ-separated subset of Z . For each
δ p
θ ∈ Λ , let f have Fourier support in the set δ−1τ ∩(Zn \pZn). Write q = n(n+1). Then
δ θ θ p p n
(cid:13) (cid:13) (cid:32) (cid:33)1/qn
(cid:13) (cid:13) (cid:13) (cid:88) f θ (cid:13) (cid:13) (cid:13) ≤ D n,p,ε δ−1+n− q m n +1−ε (cid:88) ∥f θ ∥q L n qn(Qn) .
(cid:13) (cid:13) p
θ∈Λ δ Lqn(Qn) θ∈Λ δ
p
for each ε > 0. We may choose D to be the quantity
n,p,ε
(cid:16) (cid:17)
D = exp 104(logp)ε−5nlognn10n2 .
n,p,ε
Before proving Prop. 3.1, we indicate how it implies Theorem 2.1.
Proof of Theorem 2.1 using Proposition 3.1.
We claim the particular inequality
√
# W ≥ C(cid:101) (c )ν(Qn)cδ0(ν)−1δ−α−1+1010n ε k,
n,p,ε k 0 p α
for the particular sequence {ε }∞ , defined by
k k=1
1 1
(cid:18)(cid:113) (cid:19)
ε = , ε = ε2 +4ε −ε , k ∈ N.
1 2 k+1 4 k k k
Then 0 < ε < ε for all k, and ε = ε , where
k+1 k (cid:103)k+1 k
ε
ε˜= √ .
1− ε
We have also written c = min(1,c) and
0
C(cid:101) (c ) = (10−2ε)qn(c /4p)ε−1D−qn .
n,p,ε 0 0 n,p,ε
From Prop. 3.1, and observing that ε˜−1 + 1 ≤ ε−1, the original claim holds for each ε . By
k
trivial inequalities, the full result holds.
Following [4], we proceed by induction on ε > 0. By a trivial estimate when ε = ε = 1, we
1 2
have the base case. It suffices to show that, if Theorem 2.1 holds for ε˜= ε √ , then it holds
1− ε
for ε.
Proceeding to the induction, we assume the result for ε˜. The tiles in T of Qn have dimen-
θ p
sions δ × ··· × δ × 1 × ··· × 1. We further have, for each θ, a subfamily W ⊆ T such that
θ θ
(cid:80) 1 (x) ≥ c δε−1 for all x in the support of a special measure ν. We wish to demonstrate

## T∈W T 0

a suitable lower bound on #W.
9

<!-- Page 10 -->

To this end, first observe the calculation
 
δ−1 0 ··· 0 0 ··· 0


 0 δ−1 ··· 0 0 ··· 0  
Π( θ m)A− θ,δ ⊤ −1 =   . . . . . . ... . . . . . . ... . . .   k ;
 


0 0 ··· δ−1 0 ··· 0 
(cid:124) (cid:123)(cid:122) (cid:125)
n
consequently, for each x ∈ Zm,
p
Zn ∩(Π(m))−1[x+δ−1Zm] = A−⊤ [δ(x,0)+Zm ×Zn−m].
p θ p θ,δ−1 p p
Thus, we will write members of T as translates c +A−⊤ [Zn] for various choices of c ∈ Qn.
θ T θ,δ−1 p T p
For each T = c +A−⊤ Zn ∈ T , consider the function 1 . If we recall that τ = A [Zn],
T θ,δ−1 p θ T θ θ,δ−1 p
then we may verify that
1ˆ (ξ) = χ(−c ·ξ)δm1 (ξ).
T T τ
θ
Observe that τ has dimensions δ−1 × ··· × δ−1 × 1 × ··· × 1, with long sides parallel to
θ
γ(1)(θ),...,γ(m)(θ); observe also that τ is symmetric about the origin.
θ √ √
Let κ be a positive integer such that δ− ε ≤ pκ ≤ pδ− ε, and write ψ = 1 . Then,
δ B(0,δ−1p−κ)
for some subset F ⊆ Qn with ν(F) ≥ 1ν(Qn), we either have
p 2 p
(cid:12) (cid:12)
c (cid:12)(cid:88) (cid:12)
0 δ−1+ε ≤ (cid:12) 1 ∗ψ∨(x)(cid:12) ∀x ∈ F, (3.3)
2 (cid:12) T δ (cid:12)
(cid:12) (cid:12)

## T∈W

or
(cid:12) (cid:12)
c (cid:12)(cid:88) (cid:12)
0 δ−1+ε ≤ (cid:12) 1 ∗(1 −ψ )∨(x)(cid:12) ∀x ∈ F. (3.4)
2 (cid:12) T δZn p δ (cid:12)
(cid:12) (cid:12)

## T∈W

Observe from the outset that
ψ∨ = δ−np−nκ1 .
δ B(0,δpκ)
We consider case 3.3 first. For each fixed T, we may compute
1 ∗ψ∨ = p−mκ1 ,

### T δ T(cid:101)

where T(cid:101) = c +A−⊤ [Zn], recalling that T = c +A−⊤ (Zn).

### T θ,p−κδ−1 p T θ,δ−1 p

Observe that T(cid:101) is the (δpκ ×···×δpκ ×1×···×1)-plate with the same center as T and
the same short directions. As such, for each θ ∈ Λ we fix the tiling T of Qn by translates of
δ θ p
A−⊤ [Zn].
θ,p−κδ−1 p
We investigate the relationship between T and T . Suppose T ∈ T
θ′
and T(cid:101) ∈ T
θ
are such
that T ⊆ T(cid:101). Let q ∈ Qn be the unique element such that {q } = q for all 1 ≤ j ≤ n and such
p j p j
that T(cid:101) = A−⊤ [q +Zn]. Then −q +A⊤ [T] =: B is a subset of Zn. Moreover, writing
θ,p−κδ−1 p θ,p−κδ−1 p
T = A−⊤ [b+Zn] for the unique b ∈ Qn satisfying the preceding equality and {b } = b for
θ′,δ−1 p p j p j
all 1 ≤ j ≤ n, we see that
B = −q +A⊤ A−⊤ b+A⊤ A−⊤ [Zn].
θ,p−κδ−1 θ′,δ−1 θ,p−κδ−1 θ′,δ−1 p
10

<!-- Page 11 -->

We will bound, for each θ ∈ Z , the number of θ′ ∈ Z such that A⊤ A−⊤ [Zn] ⊆ Zn.
p p θ,p−κδ−1 θ′,δ−1 p p
We begin by noticing that

## A⊤ A−⊤ = A⊤ ,

θ,1 θ′,1 θ−θ′,1
so that for each j ≤ k
(θ−θ′)k−j
(cid:0) (cid:1)

## A⊤ A⊤ = .

θ,1 −θ′,1 jk (k −j)!
If θ,θ′ are such that we have the inequality
|θ−θ′| > pκδ,
p
then it follows that
(A⊤ A⊤ )(e ) ̸∈ p−κδ−1Zm ×Zn−m,
θ,1 −θ′,1 m p p
and hence
diag(pκδ,...,pκδ,1,...,1)A⊤ A−⊤diag(δ−1,...,δ−1,1,...,1)[Zn] ̸⊆ Zn,
θ,1 θ′,1 p p
whereas the left-hand side is just A⊤ A−⊤ [Zn]. It follows that, for each T(cid:101),
θ,p−κδ−1 θ′,δ−1 p
# (cid:8) T ∈ W : T ⊆ T(cid:101) (cid:9) ≤ pκ(m+1). (3.5)
On the other hand, if |θ−θ′| ≤ pκδ, we note that
p

### A⊤ A−⊤ [Zn] ⊆ Zn,

θ,p−κδ−1 θ′,p−κδ−1 p p
so A−⊤ and A−⊤ define the same thick wave packets unless |θ−θ′| > pκδ.
θ,p−κδ−1 θ′,p−κδ−1 p
(cid:83)
Now, writing T = T , it holds that
θ∈Λ θ
δ
(cid:88) (cid:88)
1 ∗ψ∨ ≤ p−mκ (#{T ∈ W : T ⊆ T(cid:101)})1 .
T δ T(cid:101)

## T∈W

T(cid:101)∈T

### If we set

(cid:110) c (cid:111)
T = T(cid:101) ∈ T : #{T ∈ W : T ⊆ T(cid:101)} ≤ 0 δεp(m+1)κ ,
θ,light θ
4
and T = T \T , then
θ,heavy θ θ,light
(cid:13) (cid:13)
(cid:13) (cid:13)
p−mκ (cid:13) (cid:13) (cid:88) (cid:88) (cid:0) #{T ∈ W : T ⊆ T(cid:101)} (cid:1)1 (cid:13) (cid:13) ≤ c 0 δ−1+ε,
(cid:13) T(cid:101)(cid:13) 4
(cid:13)θ∈Λ
δT(cid:101)∈T θ,light
(cid:13)
L∞(Qn)
p
which implies, comparing with 3.3,
c (cid:88) (cid:88)
0 δ−1+ε ≤ p−mκ (#{T ∈ W : T ⊆ T(cid:101)})1 (x), x ∈ F.
4 θ T(cid:101)
θ∈Λ δT(cid:101)∈T
θ,heavy
From the upper bound 3.5, we have on F
√ 4 (cid:88) (cid:88)
δ−1+ε+ ε ≤ pδ−1+εp−κ ≤ p 1 (x), x ∈ F. (3.6)
c

## T˜

0
θ∈Λ δT˜∈T
θ,heavy
11

<!-- Page 12 -->


### Observe that

δ−1+ε+ √ ε = (δ1− √ ε)−1+ 1− ε√ ε,
so that the dilated arrangement {T(cid:101) ∈ T : θ ∈ Λ } satisfies our Kakeya hypothesis with ε
θ√,heavy δ
replaced by ε˜= ε √ , δ replaced by δ1− ε, and constant c0. By the induction hypothesis, we
1− ε 4p
obtain the estimate
√
# (cid:91) T ≥ C(cid:101) (c )ν(Qn)cδ0(ν)−1δ(1− √ ε)(−1−α)δ 1010(1− √ ε)( 1− ε√ ε ) .
θ,heavy n,p,ε 0 p α
θ
Recall that, if T(cid:101) ∈ T and T(cid:101) ∈ T and T ∈ W are such that T ⊆ T(cid:101) ∩ T(cid:101) , then
1 θ1,heavy 2 θ2,heavy 1 2
|θ −θ | ≤ pkδ. Thus we may bound
1 2 p
c (cid:91)
# W ≥ pκmδε 0 # T .
θ,heavy
4p
θ∈Λ
δ
Combining the previous two displays,
√
√ √ √
# W ≥ C(cid:101) (c )ν(Qn)cδ0(ν)−1δ(1− ε)(−1−α)δε−m εδ1010n ε−ε ε
n,p,ε 0 p α
√
√ √
= C(cid:101) (c )ν(Qn)cδ0(ν)−1δ−1−αδ(α−m) εδε+1010n ε−ε ε .
n,p,ε 0 p α
√ √
≥ C(cid:101) (c )ν(Qn)cδ0(ν)−1δ−1−αδ(α−m) εδ1010n ε
n,p,ε 0 p α
Since α < m, we obtain
√
# W ≥ C(cid:101) (c )ν(Qn)cδ0(ν)−1δ−1−α+1010n ε.
n,p,ε 0 p α
Recalling the form of C(cid:101) (c ), we are done.
n,p,ε 0
Next, we assume 3.4 holds. For each θ write g = (cid:80) (1 ∗(1 −ψ )∨)(x). Then
θ T∈W
θ
T δZn
p
δ
(cid:88)
gˆ (ξ) = δm χ(−c ·ξ)1 (ξ)(1 −ψ )(ξ).
θ T τ δZn δ
θ p

## T∈W

θ
Write f (x) = g (δ−1x). Then the preceding display shows that f ˆ is supported in δ−1τ \pkZ .
θ θ θ θ p
If we further decompose
k−1
(cid:88)
f = f ∗1∨ ,
θ θ pjZn\pj+1Zn
p p
j=0
and notice that each x (cid:55)→ (f ∗1∨ )(p−jx) satisfies the hypotheses of Prop. 3.1, then
θ pjZn\pj+1Zn
p p
we conclude
(cid:13) (cid:13) (cid:32) (cid:33)1/qn
(cid:13) (cid:13) (cid:13)
(cid:13)
(cid:88) f θ ∗1∨ pjZn
p
\pj+1Zn
p
(cid:13) (cid:13) (cid:13)
(cid:13)
≤ D n,p,ε/2 δ−1+n− q m n +1−ε/2 (cid:88) ∥f θ ∗1∨ pjZn
p
\pj+1Zn
p
∥q L n qn(Qn
p
) .
θ∈Λ δ Lqn(Qn) θ∈Λ δ
p
By the triangle inequality and Young’s convolution inequality, we see that
(cid:13) (cid:13) (cid:32) (cid:33)1/qn
(cid:13) (cid:13) (cid:13) (cid:13) (cid:88) f θ (cid:13) (cid:13) (cid:13) (cid:13) ≤ 4 ε D n,p,ε/2 δ−1+n− q m n +1−ε (cid:88) ∥f θ ∥q L n qn(Qn p ) ,
θ∈Λ δ Lqn(Qn) θ∈Λ δ
p
12

<!-- Page 13 -->

using k = −log δ ≤ 2δ−ε/2.
p ε
Rescaling both sides of the previous display, we reach the estimate
(cid:13) (cid:13) (cid:32) (cid:33)1/qn
(cid:13) (cid:13) (cid:13) (cid:13) (cid:88) g θ (cid:13) (cid:13) (cid:13) (cid:13) ≤ 4 ε D n,p,ε/2 δ−1+n− q m n +1−ε (cid:88) ∥g θ ∥ L qn qn(Qn p ) . (3.7)
θ∈Λ δ Lqn(Qn) θ∈Λ δ
p
For each θ ∈ Λ ,
δ
(cid:13) (cid:13) (cid:13) (cid:13)
(cid:13) (cid:88) (cid:13) (cid:13) (cid:88) (cid:13)
∥g ∥ = (cid:13)(1 −ψ )∨ ∗ 1 (cid:13) ≤ ∥(1 −ψ )∨∥ (cid:13) 1 (cid:13) .
θ Lqn(Qn) (cid:13) δZn δ T(cid:13) δZn δ L1(Qn)(cid:13) T(cid:13)
p p p p
(cid:13) (cid:13) (cid:13) (cid:13)

## T∈W

θ Lqn(Qn)

## T∈W

θ Lqn(Qn)
p p
By the definition of the family W ,
θ
(cid:13) (cid:13)
(cid:13) (cid:13)
(cid:13)
(cid:88) 1

## T

(cid:13) (cid:13)
(cid:13)

## = (#W

θ
)q 1
n
δq m
n
.
(cid:13) (cid:13)

## T∈W

θ Lqn(Qn)
p
Since ψ (ξ) = 1 (δ−1ξ) and 1 (ξ) = 1 (δ−1ξ), an application of change-of-variable
δ B(0,p−κ) δZn Zn
p p
reveals
∥(1 −ψ )∨∥ ≤ 2,
δZn δ L1(Qn)
p p
and thus
(cid:32) (cid:33)1/qn
(cid:88) ∥g
θ
∥q

## L

n
qn(Qn)
≤ 2δq m
n
(#W)q 1
n
. (3.8)
p
θ∈Λ
δ
Since c
2
0δ−1+ε ≤ | (cid:80)

## T∈W

1

## T

∗(1
δZn p
−ψ
δ
)∨(x)| for all x ∈ F, we have that
(cid:12) (cid:12)
c (cid:12)(cid:88) (cid:12)
0 δ−1+ε ≤ (cid:12) g (x)(cid:12), ∀x ∈ F,
2 (cid:12) θ (cid:12)
(cid:12) (cid:12)
θ∈Λ
δ
so that
ˆ (cid:12) (cid:12)qn
(cid:12)(cid:88) (cid:12)
(c /2)qnδ−qn+qnεν(F) ≤ (cid:12) g (cid:12) dν.
0 (cid:12) θ(cid:12)
(cid:12) (cid:12)
θ∈Λ
δ
Note that | (cid:80) g | is constant on balls of radius δ; thus, using 0 < cδ0(ν) < ∞ and δ > δ ,
θ∈Λ θ α 0
δ
ˆ (cid:12) (cid:12)qn ˆ (cid:12) (cid:12)qn
(cid:12)(cid:88) (cid:12) (cid:12)(cid:88) (cid:12)
(cid:12) g (cid:12) dν ≤ cδ0(ν)δα−n (cid:12) f (cid:12) dµ,
(cid:12) θ(cid:12) α (cid:12) θ(cid:12)
(cid:12) (cid:12) (cid:12) (cid:12)
θ∈Λ θ∈Λ
δ δ
so that, using also ν(F) ≳ ν(Qn),
p
ˆ (cid:12) (cid:12)qn
(cid:12)(cid:88) (cid:12)
2−qn−1cqncδ0(ν)−1ν(Qn)δ−qn+qnε ≤ δα−n (cid:12) g (cid:12) . (3.9)
0 α p (cid:12) θ(cid:12)
(cid:12) (cid:12)
θ∈Λ
δ
Collecting estimates 3.7, 3.8, and 3.9, we conclude
# W ≥ 2−4qn−1εqnD−qn cqnν(Qn)cδ0(ν)−1δ−α−1+2qnε.
n,p,ε/2 0 p α
√
As 2q ε ≤ 1010n ε for every 0 < ε ≤ 1, we are done.
n
13

<!-- Page 14 -->

4 Decoupling bound for restricted projections
In this section we prove Prop. 3.1. We will do so by adapting the decoupling procedure of [4] to
the p-adic setting. We will take for granted p-adic decoupling for moment curves in dimensions
n < p; for a proof of the latter, see Corollary 6.22 in Appendix B. We emphasize that this
decoupling theorem (together with elementary rescaling arguments) will be the only Fourieranalytic inputs for this section. Instead, we will be primarily concerned with a decomposition
(cid:80)
of the Fourier support of f into subsets over which the decoupling theorem may be used.
θ∈Λ θ
δ
The decoupling procedure described in this section is virtually identical to the real setting.
As a consequence, we will present a very terse accounting of the analysis; the interested reader
may compare with [4] for motivation. At the end, we state the output of the algorithm and
observe that the estimate obtained suffices to prove Proposition 3.1.
We may assume that δ is restricted to sufficiently regular powers of p, to facilitate taking
various roots; similarly, we assume that ε is a sufficiently divisible reciprocal of an integer. To
this end, write κ = (n!)2n and assume that ε = 1 for some ℓ ∈ N . We assume also that
ℓκ ≥2
δ ∈ p−κ2N. After we have established this special case, we will be able to conclude the general
statement via trivial estimates.
We begin by defining a decomposition of frequency space which will facilitate the proof of
Proposition 3.1. These are adapted to the support of the Fourier transform of f, the function
to be estimated. See Figure 1 for an illustration of the geometry, when regarded over R.
For each subset J ⊆ Z and 1 ≤ m ≤ m, define
p 1
n
(cid:110)(cid:88) (cid:111)
Ω = λ γ(j)(θ) : θ ∈ J ∩Λ ,λ ∈ Z ∀j, max |λ | = 1, |λ | ≤ δ ∀j ∈ (m,n] ⊆ Qn
J j δ j p j p j p p
1≤j≤n
j=1
and
n
(cid:110)(cid:88) (cid:111)
Ω = λ γ(j)(θ) ∈ Ω : |λ | = 1,|λ | < 1 ∀j ∈ (m ,m] ,
J,m1 j J m1 p j p 1
j=1
so that {Ω } partition Ω for each J.
J,m1 1≤m1≤m J
For each s
1
∈ p−ε−1N with δn− 1 m1 ≤ s
1
< 1, write
n

## Ω

J,m1,s1
=
(cid:110)(cid:88)
λ
j
γ(j)(θ) ∈ Ω
J,m1
: (s
1
= δn− 1 m1 or ∃ι ∈ [1,m−m
1
] s.t. sι
1
≤ |λ
m1+ι
|
p
),
j=1
(cid:111)
∀ι ∈ [1,m−m ]pιε−1sι > |λ |
1 1 m1+ι p
so that
(cid:91)

## Ω = Ω .

J,m1 J,m1,s1
1
δn−m1≤s1<p−1
We remark that Ω is essentially a segment of the rim of a thick cone over an (n − m )-

### J,m1 1

dimensionalmomentcurve, andeachΩ isathinsliceofthatconetofacilitatethestandard

### J,m1,s1

cone-decoupling trick of comparing with a cylinder. See Figure 1 for an illustration. We
further decompose Ω by: for each tuple R = (R ,...,R ) ∈ P(Z ,sε)m1−1 and each
J,m1,s1 1 m1−1 p 1
14

<!-- Page 15 -->

B ∈ P(Z \pZ ,sε),
p p 1
n
(cid:110)(cid:88) (cid:111)
ΩB,R = λ γ(j)(θ) : λ ∈ R ∀j ∈ [1,m ),λ ∈ B .
J,m1,s1 j j j 1 m1
j=1
We will eventually decouple along these regions; to this end, for each k ∈ N, write
k(k +1)+2

## D = ,

k
2
so that the ℓqnLqn decoupling constant for the k-dimensional moment curve at scale δ has size
≲ ε δ−(1− D qn k)−ε for each k ≤ n.
With this established, we now proceed to describing the proof of Prop. 3.1.
Proof of Prop. 3.1. We first observe that the sets above describe the Fourier support of f.
ˆ
Indeed, f is supported in the set
θ
A−⊤ (Zn)\pZn
θ,1,δ p p
where we again are adopting the notation
A = [α−1γ(1)(θ),...,α−1γ(m)(θ),β−1γ(m+1)(θ),...,β−1γ(n)(θ)], (θ ∈ Z ,α,β ∈ Q ).
θ,α,β p p
ˆ
Consequently, f is supported in Ω , so the preceding decomposition applies.
θ {θ}
1
By Ho¨lder,1 we have that one of the following holds: either there exists m
1
< m, δn−m1 ≤
s ∈ p−ε−1N, J ∈ P(Z ,sε), B ∈ P(Z \pZ ,sε), R ∈ P(Z ,sε)m1−1 such that
1 p 1 p p 1 p 1
(cid:13) (cid:13) (cid:13) (cid:13)
(cid:13)(cid:88) (cid:13) (cid:13) (cid:88) (cid:13)
(cid:13) f (cid:13) ≤ m(log δ−1)s−(m1+1)ε(cid:13) P f (cid:13) (4.1)
(cid:13) θ(cid:13) p 1 (cid:13) ΩB,R θ(cid:13)
(cid:13) (cid:13) (cid:13) J,m1,s1 (cid:13)
θ∈Λ δ Lqn(Qn) θ∈J∩Λ δ Lqn(Qn)
p p
or else we set m
1
= m,s
1
= δn− 1 m1 , and there is J ∈ P(Z
p
,sε
1
) such that
(cid:13) (cid:13) (cid:13) (cid:13)
(cid:13)(cid:88) (cid:13) (cid:13) (cid:88) (cid:13)
(cid:13) f (cid:13) ≤ m(log δ−1)s−(m1+1)ε(cid:13) P f (cid:13) . (4.2)
(cid:13) θ(cid:13) p 1 (cid:13) ΩJ,m θ(cid:13)
(cid:13) (cid:13) (cid:13) (cid:13)
θ∈Λ δ Lqn(Qn) θ∈J∩Λ δ Lqn(Qn)
p p
(cid:80)
We will focus on the case that (4.1) holds, and abbreviate F = P f . We will
θ∈J∩Λ
δ

## Ωb


## J,

,
m

## R

1,s1
θ
demonstrate the following:
Lemma 4.1. Suppose that s = p−ℓε−1 for some ℓ ≥ 2. For any
1
ε−1
0 ≤ k ≤ k := (n−m )⌊ε−1 −2− ⌋
∗ 1
ℓ
(1+ k )ε
and any L ∈ P(J,s n−m1 ), we have that
1
 1/qn
(cid:13)
(cid:13) (cid:88)
(cid:13)
(cid:13) − ε2 − ε (1− Dn−m1)  (cid:88)
(cid:13)
(cid:13) (cid:88)
(cid:13)
(cid:13)
qn

(cid:13) F (cid:13) ≤ C s n−m1s n−m1 qn  (cid:13) F (cid:13)  ,
(cid:13) θ(cid:13) n−m1,(n−m1)ε 1 1  (cid:13) θ(cid:13) 
(cid:13) θ∈L∩Λ δ (cid:13) Lqn(Qn p )  I∈P (cid:16) L,s (1+n k − + m 1 1 )ε (cid:17)(cid:13) θ∈I∩Λ δ (cid:13) Lqn(Qn p ) 
1
where C is as in Remark 6.23.
n−m1,(n−m1)ε
1Indeed, consider the weighting of each particular configuration by sm1+1.
1
15

<!-- Page 16 -->

(1+ k )ε
Proof of Lemma 4.1. Byapplyingparabolicrescaling,itsufficestoassumethatL = B(0,s n−m1 )
1
and B = B(1,sε). Then, for any θ,λ ,...,λ as in the definition of ΩB,R , we have the rela-
1 1 n L,m1,s1
tions
(cid:88) n (cid:88) ι θι−j
λ γ(j)(θ) = λ (1 ≤ ι ≤ m ),
j ι j (ι−j)! 1
j=1 j=1
(cid:12) (cid:12)
(cid:12) (cid:12) (cid:88) n λ γ(j)(θ)− (λ m1 θ)ι−m1(cid:12) (cid:12) ≤ s (1+ n− k m1 )ε(ι−m1)+ε (m < ι ≤ n).
(cid:12) j ι (ι−m )! (cid:12) 1 1
(cid:12) 1 (cid:12)
j=1
p
(1+ k )ε(ι−j)
The second of these follows from the inequality |θι−j| ≤ s n−m1 for j ≤ ι, the inequality
p 1
|λ −(λ )ι−m1| ≤ sε, the inequality |λ | ≤ pε−1(j−m1)sj−m1 for m < j ≤ ι, the ultrametric
m1 m1 p 1 j p 1 1
triangle inequality, and the fact that (1+ k∗ )ε ≤ 1−ε− 1.
n−m1 ℓ

### Consequently, it holds that

(cid:110)(cid:88) m1 (cid:88) n (cid:18) θι−m1 (cid:19)
Ωi,r ⊆ ρ e + +ρ e : ρ ∈ B(b ,sε) (ι < m ),ρ ∈ B(1,sε),
L,m1,s1 ι ι (ι−m )! ι ι ι rι 1 1 m1 1
1
ι=1 ι=m1+1
|ρ | ≤ s
(1+
n−
k
m1
)ε(ι−m1)+ε
(ι > m ),θ ∈ L∩Λ
(cid:111)
.
ι p 1 1 δ
(1+ k )ε
Applyingtimerescalingθ (cid:55)→ s n−m1 θ (n.b. thatthisisregardedasaproductoftwoelements
1
of Q ), and decoupling over the (n−m )-dimensional moment curve, we conclude
p 1
 1/qn
(cid:13) (cid:13)
(cid:13) (cid:13) (cid:88) F (cid:13) (cid:13) ≤ C s − n− ε2 m1s − n− ε m1 (1− Dn q − n m1)  (cid:88) (cid:13) (cid:13) (cid:88) F (cid:13) (cid:13) qn   .
(cid:13) (cid:13) θ(cid:13) (cid:13) n−m1,(n−m1)ε 1 1  θ Lqn(Qn p )
θ∈L Lqn(Qn p ) I∈P(L,s (1+n k − + m 1 1 )ε ) θ∈I
1
Since decoupling constants are sub-multiplicative, we may repeatedly apply Lemma 4.1 to
conclude
 1/qn
∥F∥ Lqn(Qn p ) ≤ C n n − − ε m m1 1,(n−m1)ε s 1 −ε−(1− Dn q − n m1)   (cid:88) ∥F I ∥q L n qn(Qn p )    .
I∈P(Z p,s (
1
1+n k − ∗+ m 1 1 )ε )
By the triangle inequality and Cauchy-Schwarz, we arrive at the estimate
 1/qn
∥F∥ Lqn(Qn p ) ≤ C n n − − ε m m1 1,(n−m1)ε pε−1s 1 −2ε−(1− Dn q − n m1)  (cid:88) ∥F I ∥q L n qn(Qn p )  ,

### I∈P(Z p,s1)

valid whenever we had s ∈ p−ε−1N ≥2. If instead s = p−ε−1, then trivial estimates supply
1 1
 1/qn
(cid:88)
∥F∥ Lqn(Qn p ) ≤ pε−1  ∥F I ∥q L n qn(Qn p )  .
I∈P(Z p,s1)
16

<!-- Page 17 -->

Figure 1: Left: the union of the truncated plates δ−1τ ∩ (Zn \ pZn) is contained in a thick
θ p p
neighborhood Ω of a cone over a lower-dimensional nondegenerate curve. Right: the decom-

## I

position Ω = (cid:83) Ω in the case (m ,m,n) = (1,2,3) over R.

### J,m1 J,m1,s1 1

The remainder of the algorithm involves rescaling each F and repeating the above procedure,

## I

by finding a new parameter s to treat the Fourier support of F as the cylinder over a moment

## 2 I

curve. We summarize the inductive step in Lemma 4.3 below. Prior, we adopt the following
notation, largely identical to that of [4]. For any m ∈ [1,m] and n ∈ [m,n], and any
1 1
s ∈ p−ε−1N, we set
1
L (ξ) = (ξ ,...,ξ ,s−1ξ ,...,sm1−nξ ),
m1,s1 1 m1 1 m1+1 1 n
R (ξ) = (s1−1ξ ,s1−2ξ ,...,s1−m1ξ ,s1−m1ξ ...,s1−m1ξ ),
m1,s1 1 1 1 2 1 m1 1 m1+1 1 n
and
 sj−1ξ 1 ≤ j ≤ m ,
 1 j 1

 p−(j−m1)ε−1sm1−1ξ m < j ≤ m,
Ds1 (ξ) = 1 j 1
m1,n1 j
 
sm
1
1−1ξ
j
m < j ≤ n
1
,


ξ n < j ≤ n.
j 1
If s = (s ,...,s ),m = (m ,...,m ), and n = (n ,...,n ) are entrywise as abovve, then
J 1 J j 1 J J 1 J
we write

## L = L ◦···◦L ,

mJ,sJ mJ,sJ m1,s1

## R = R ◦···◦R ,

mJ,sJ mJ,sJ m1,s1
DsJ = DsJ ◦···◦Ds1 .
mJ,nJ mJ,nJ m1,n1
We will use the abbreviations

## J

(cid:89)
s◦ = s , s−◦ = (s◦)−1.
J j J J
j=1
When a given tuple s is already understood and 0 ≤ j < J, we’ll write s for the corresponding

### J j

initial segment of s . We’ll also write

## J

γ = R ◦γ,
m1,s1 m1,s1
17

<!-- Page 18 -->

and
γ = R ◦γ;
mJ,sJ mJ,sJ
observe then that
(cid:0) (cid:1)
γ (θ) = s◦L−1 γ s−◦θ . (4.3)
mJ,sJ J mJ,sJ J
Thetupleswillneedtosatisfythefollowingcompatibilityrelation: wewrites ∈ AdapsJ

### J+1 mJ+1,nJ+1

for quantities s ∈ p−ε−1N, and call them adapted, if

## J+1

(cid:32) (cid:33) 1
(cid:89)
J nJ+1−mJ+1
δ s
−(nJ−1−mj)
≤ s < 1. (4.4)
j J+1
j=1
We also set out the following regions in frequency space: given tuples s ,m ,n , and θ ∈ Z

### J J J p

with |θ| ≤ s◦, we write
p J
(cid:110) (cid:104) (cid:105)
(cid:0) (cid:1) (cid:0) (cid:1)
Ωres = γ(1) s θ ,...,γ(n) s θ ·Ds1 (λ) :
θ,m1,s1 m1,s1 1 m1,s1 1 m1,n
∀ι ∈ [1,n] |λ | ≤ 1,|λ | = 1,
ι p m1 p
∃ι ∈ [1,m−m ] s.t. p−ιε−1 < |λ | ,
1 m1+ι p
∀ι ∈ [1,m−m ] |λ | ≤ 1,
1 m1+ι p
(cid:111)
∀ι ∈ [1,n−m] |λ | ≤ δs−ι .
m+ι p 1
Here, we emphasize the convention that each γ(j) is a column vector, [γ(1),...,γ(n)] denotes the
matrix whose jth column is γ(j), λ is the column vector (λ ,...,λ ), and the · denotes matrix
1 n
multiplication. We similarly write
(cid:110) (cid:104) (cid:105)
(cid:0) (cid:1) (cid:0) (cid:1)
Ωres = γ(1) s◦θ ,...,γ(n) s◦θ ·DsJ (λ) :
θ,mJ,sJ,nJ mJ,sJ J mJ,sJ J mJ,nJ
∀ι ∈ [1,n] |λ | ≤ 1,|λ | = 1,
ι p mJ p
∃ι ∈ [1,m−m ] s.t. p−ιε−1 < |λ | ,

### J mJ+ι p

∀ι ∈ [1,m−m ] |λ | ≤ 1,
J mJ+ι p

## J

(cid:89) (cid:111)
∀ι ∈ [1,n −m] |λ | ≤ δ s
−(m+ι−mj)
,
J m+ι p j
j=1
and, for each choice of s ,m ,n , we write

## J+1 J+1 J+1

(cid:110) (cid:104) (cid:105)
Ω res,mJ+1,sJ+1,nJ+1 = γ(1) (cid:0) s◦θ (cid:1) ,...,γ(n) (cid:0) s◦θ (cid:1) ·DsJ (λ) ∈ Ωres :
θ,mJ,sJ,nJ mJ,sJ J mJ,sJ J mJ,nJ θ,mJ,sJ,nJ
|λ | = 1,
mJ+1 p
(cid:32) (cid:33) 1
(cid:16) (cid:89) J nJ+1−mJ+1
s = δ s
−(nJ−1−mj)
J+1 j
j=1
(cid:17)
or ∃ι ∈ [1,m−m ] s.t. 1 ≤ |λ | ,
J+1 mJ+1+ι p
(cid:111)
∀ι ∈ [1,m−m ] |λ | < sι pιε−1 .

### J+1 mJ+1+ι p J+1

We immediately motivate the definition of these regions by the following lemma.
18

<!-- Page 19 -->

Lemma 4.2. Suppose h has Fourier support in Ω , and |θ| ≤ s . Then h ◦ L has
θ,m1,s1 p 1 m1,s1
FouriersupportinΩres . Moregenerally, ifh◦L hasFouriersupportinΩ res,mJ+1,sJ+1,nJ+1,
θ,m1,s1 mJ,sJ θ,mJ,sJ,nJ
then h◦L has Fourier support in Ωres .
mJ+1,sJ+1 θ,mJ+1,sJ+1,nJ+1
Proof. By induction on J. Consider the base case J = 1. Relabelling λ (cid:55)→ sιλ , we see
m1+ι 1 m1+ι
that h◦L is Fourier supported in the set
m1,s1
(cid:110)
(cid:2) (cid:3)
L−1 · γ(1)(θ),...,γ(n)(θ) ·L (λ) : |λ | ≤ 1∀j < m , |λ | = 1,
m1,s1 m1,s1 j 1 m1 p
1
(s
1
= δn−m1 or ∃ι ∈ [1,m−m
1
] s.t. 1 ≤ |λ
m1+ι
|
p
),
∀ι ∈ [1,m−m ]|λ | < pιε−1,
1 m1+ι p
(cid:111)
∀ι ∈ [1,n−m]|λ | ≤ s−ιδ
m+ι 1
For a particular (column) vector λ, we may manipulate the corresponding sum via 4.3 as
(cid:2) (cid:3) (cid:2) (cid:3)
L−1 · γ(1)(θ),...,γ(n)(θ) ·L (λ) = s1−1γ(1) (s θ),...,sn−1γ(n) (s θ) ·L (λ),
m1,s1 m1,s1 1 m1,s1 1 1 m1,s1 1 m1,s1
which we may write as
(cid:2) (cid:3)
γ(1) (s θ),...,γ(n) (s θ) ·R−1 (λ).
m1,s1 1 m1,s1 1 m1,s1
Finally, for each ι ∈ [1,m − m ], we relabel again λ (cid:55)→ pιε−1λ ; from the definition of
1 m1+ι m1+ι
Ds1 , the desired result follows.
m1,n
In the general case, relabelling λ (cid:55)→ sι λ , we see that h◦L is Fourier
mJ+1+ι J+1 mJ+1ι mJ+1,sJ+1
supported in the set
(cid:110)
(cid:2) (cid:3)
L−1 · γ(1) (s◦θ),...,γ(n) (s◦θ) ·L (DsJ (λ)) :
mJ+1,sJ+1 mJ,sJ J mJ,sJ J mJ+1,sJ+1 mJ,nJ
|λ | ≤ 1∀j < m , |λ | = 1,
j J+1 mJ+1 p
(cid:32) (cid:33) 1
(cid:16) (cid:89) J nJ+1−mJ+1 (cid:17)
s = δ s
−(nJ−1−mj)
or ∃ι ∈ [1,m−m ] s.t. 1 ≤ |λ | ,
J+1 j J+1 mJ+1+ι p
j=1
∀ι ∈ [1,m−m ]|λ | < pιε−1,
J+1 mJ+1+ι p

## J+1

(cid:89) (cid:111)
∀ι ∈ [1,n −m] |λ | ≤ δ s
−(m+ι−mj)
.
J+1 m+ι p j
j=1
Again, we may manipulate the corresponding sum via 4.3 as
(cid:2) (cid:3)
L−1 · γ(1) (s◦θ),...,γ(n) (s◦θ) ·L (DsJ (λ))
mJ+1,sJ+1 mJ,sJ J mJ,sJ J mJ+1,sJ+1 mJ,nJ
(cid:104) (cid:105)
= s1−1γ(1) (s◦ θ),...,sn−1γ(n) (s◦ θ) ·L (DsJ (λ)),
J+1 mJ+1,sJ+1 J+1 J+1 mJ+1,sJ+1 J+1 mJ+1,sJ+1 mJ,nJ
which we may write as
(cid:2) (cid:3)
γ(1) (s θ),...,γ(n) (s θ) ·R−1 (DsJ (λ)).
m1,s1 1 m1,s1 1 mJ+1,sJ+1 mJ,nJ
Finally, for each ι ∈ [1,m−m ], we relabel again λ (cid:55)→ pιε−1λ ; from the definition
J+1 mJ+1+ι mJ+1+ι
of D
sJ+1
, the desired result follows.
mJ+1,nJ+1
19

<!-- Page 20 -->

Lemma 4.3 (Inductive localization step). Assume we have an integer J ≥ 1, a rooted tree
T composed of sequences (Θ ,...,Θ ), (j ≤ J), of metric balls Θ in Z , such that the set of
0 j i p
children of Θ , (i < J), is a set of the form P(Θ ,s ) with s ∈ p−ε−1N ∪{1}, together with
i i Θi Θi
labels n ,m of each Θ , for which the following axioms are satisfied.

### Θi Θi i

• n = n,m = m.

## Θ0 Θ0

• If (Θ ,...,Θ ) ∈ T, then the associated tuples {s = s }J , {n = n }J ,{m =
0 J j Θj−1 j=1 j Θj j=0 j
m }J are such that:
Θj j=0

n = n −1 and m ≥ m
 j+1 j j+1 j

     and s n j+ j− 1 mj = δ (cid:81)j η=1 s − η (nj−1−mη) ,






or n = n and m > m ,
j+1 j j+1 j
∀j ∈ [0,J) : either (4.5)
and s
nj−mj
≥ δ
(cid:81)j
s
−(nj−1−mη)
,
  j+1 η=1 η






 or n = n = m+1 and m = m = m
  j+1 j j+1 j
  and (cid:81)j s nj−mη = δ and s = 1.
η=1 η j+1
• In the setting above, we also have
suppF(cid:98) ⊆ Ω . (4.6)

### ΘJ ΘJ,mJ,sJ,nJ

Fors ,m ,n , wewillwriteT forthesetoftuples(Θ ,...,Θ ) ∈ T withthatassociated

### J J J sJ,mJ,nJ 0 J

tuple, as in the second bullet point above. We assume also that we have the upper bound
(cid:34) (cid:35)
∥F∥ Lqn(Qn p ) ≤ pJ2nε−1 (cid:88) (cid:89) J C n n j j − − ε m mj j,(nj−mj)ε s − j (mj+3)ε−(1− Dnj q − n mj)
sJ,mJ,nJ j=1

(cid:13) (cid:13)qn
1/qn (4.7)
(cid:88) (cid:13) (cid:88) (cid:13)
× (cid:13) (cid:13) F θ (cid:13) (cid:13)  .
(cid:13) (cid:13)
(Θ0,...,ΘJ)∈TsJ,mJ,nJ θ∈ΘJ∩Λ δ Lqn(Qn
p
)
Let (Θ ,...,Θ ) ∈ T be such that

## 0 J


## J

(cid:89)
n > m+1 or s
nJ−mj
> δ. (4.8)
J j
j=1
Then we may find m ∈ [m ,m], n ∈ (m,n ], and s ∈ p−ε−1N, such that

## J+1 J J+1 J J+1

(cid:16) (cid:17)
∥F ΘJ ∥ Lqn(Qn p ) ≤ pJnε−1(log p δ−1)C n n J J + + 1 1 − − ε m mJ J + + 1 1,(nJ+1−mJ+1)ε s − J+ (m 1 J+1+3)ε− 1−
DnJ+1
q
−
n
mJ+1

(cid:13) (cid:13)qn
1/qn
(cid:88) (cid:13) (cid:88) (cid:13)
× (cid:13) (cid:13) F θ (cid:13) (cid:13)  .
(cid:13) (cid:13)
Θ′∈P(Θ,s◦ J+1 ) θ∈Θ∩Λ δ Lqn(Qn p )
20

<!-- Page 21 -->

Proof. We assume Θ = B(0,s◦). For each θ ∈ Θ∩Λ , we write

### J δ

(cid:92)
g = F ◦L .
(cid:98)θ θ mJ,sJ
Thus, g is supported in the set Ω . Suppose the second option of 4.8 holds. Fix
(cid:98)θ Θ,mJ,sJ,nJ
n = n . Define, for each m ≥ m > m and θ ∈ Θ,

## J+1 J J+1 J

(cid:110) (cid:104) (cid:105)
Ω res,mJ+1 = γ(1) (cid:0) s◦θ (cid:1) ,...,γ(n) (cid:0) s◦θ (cid:1) ·DsJ (λ) :
θ,mJ,sJ,nJ mJ,sJ J mJ,sJ J mJ,nJ
∀j ∈ [1,n] |λ | ≤ 1,
j
|λ | = 1,
mJ+1 p
(cid:111)
∀ι ∈ (m ,n ] |λ | < 1 .

### J+1 J+1 ι p

For each s ∈ AdapsJ , we write

### J+1 mJ+1,nJ+1

(cid:110) (cid:104) (cid:105)
Ω res,mJ+1,sJ+1 = γ(1) (cid:0) s◦θ (cid:1) ,...,γ(n) (cid:0) s◦θ (cid:1) ·DsJ (λ) ∈ Ω res,mJ+1 :
θ,mJ,sJ,nJ mJ,sJ J mJ,sJ J mJ,nJ θ,mJ,sJ,nJ
∃ι ∈ [1,m−m ] s.t. sι ≤ |λ | ,
J+1 J+1 mJ+1+ι p
(cid:111)
∀ι ∈ [1,m−m ] |λ | < sι pιε−1 .

### J+1 mJ+1+ι p J+1

Finally, for each m ,s and each R = (R ,...,R ) ∈ P(Z ,sε )mJ+1−1 and each

### J+1 J+1 1 mJ+1−1 p J+1

B ∈ P(Z p \pZ p ,p−ε−1(JmJ+1−(cid:80)J j=1 mj)sε J+1 ), we collapse notation and write
(cid:110) (cid:104) (cid:105)
Ω(cid:101) B,R = γ(1) (cid:0) s◦θ (cid:1) ,...,γ(n) (cid:0) s◦θ (cid:1) ·DsJ (λ) ∈ Ω res,mJ+1,sJ+1 :
θ,mJ+1,sJ+1,nJ+1 mJ,sJ J mJ,sJ J mJ,nJ θ,mJ,sJ,nJ
(cid:111)
λ ∈ R (j < m ),λ ∈ B .
j j J+1 mJ+1
If we omit the B,R, then we assume that the λ range over all of Z (for j < m ), and the
j p J+1
λ range over Z \pZ . For each I ∈ P(Θ,sε ), we write
mJ+1 p p J+1
(cid:91)
Ω(cid:101) B,R = Ω(cid:101) B,R .
I,mJ+1,sJ+1,nJ+1 θ,mJ+1,sJ+1,nJ+1
θ∈I
By H¨older as before, one of the following holds: either there exists m < m < m, s ∈

## J J+1 J+1

Adaps m J J+1,nJ+1 ,I ∈ P(Θ,s◦ J sε J+1 ),B ∈ P(Z p \pZ p ,p−ε−1(JmJ+1−(cid:80)J j=1 mj)sε J+1 ),andR ∈ P(Z p ,sε J+1 )mJ+1−1
such that
(cid:13) (cid:13) (cid:13) (cid:13)
(cid:13) (cid:13) (cid:13) (cid:88) g θ (cid:13) (cid:13) (cid:13) ≤ mpε−1(JmJ+1−(cid:80)J j=1 mj)(log p δ−1)s J − + (m 1 J+1+1)ε (cid:13) (cid:13) (cid:13) (cid:88) P Ω(cid:101) B,R g θ (cid:13) (cid:13) (cid:13) ,
(cid:13) (cid:13) (cid:13) I,mJ+1,sJ+1,nJ+1 (cid:13)
θ∈Λ δ Lqn(Qn) θ∈I∩Λ δ Lqn(Qn)
p p
(4.9)
(cid:16) (cid:17) 1
or else we set m = m,s = δ (cid:81)J s −(nJ−1−mj) nJ+1−mJ+1, and there is I ∈ P(Θ,s◦sε )
J+1 J+1 j=1 j J J+1
such that
(cid:13) (cid:13) (cid:13) (cid:13)
(cid:13)(cid:88) (cid:13) (cid:13) (cid:88) (cid:13)
(cid:13) g (cid:13) ≤ m(log δ−1)s −(mJ+1+1)ε(cid:13) P g (cid:13) . (4.10)
(cid:13)
(cid:13)
θ(cid:13)
(cid:13)
p J+1 (cid:13)
(cid:13)
Ω(cid:101)I,mJ+1,sJ+1,nJ+1 θ(cid:13)
(cid:13)
θ∈Λ δ Lqn(Qn) θ∈I∩Λ δ Lqn(Qn)
p p
21

<!-- Page 22 -->

Wewillfocusonthecasethat(4.9)holds, thoughthesameargumentwillapplyineachscenario.
We abbreviate G = (cid:80) P g . For simplicity, we take I = B(0,s◦sε ) and
θ∈I∩Λ δ Ω(cid:101) B I, , m R J+1,sJ+1,nJ+1 θ J J+1
B = B(1,p−ε−1(JmJ+1−(cid:80)J j=1 mj)sε ). Then we have

## J+1

(cid:12)
(cid:12)
(cid:16)(cid:104)
γ(1) (cid:0) s◦θ (cid:1) ,...,γ(n) (cid:0) s◦θ (cid:1)
(cid:105)
·DsJ (λ)
(cid:17)
−
(λ
mJ+1
s◦

## J

θ)ι−mJ+1
p−ε−1(JmJ+1−(cid:80)J ℓ=1 m ℓ )
(cid:12)
(cid:12)
(cid:12) mJ,sJ J mJ,sJ J mJ,nJ
ι
(ι−m

## J+1

)! (cid:12)
p
≤ pε−1(JmJ+1−(cid:80)J ℓ=1 m ℓ )s ε J ( + ι− 1 mJ+1)+ε , (m J+1 < ι ≤ n J+1 ).

### The curve

s◦θ (cid:55)→
(cid:16)
p−ε−1(JmJ+1−(cid:80)J ℓ=1 m ℓ )
(λ
mJ+1
s◦

## J

θ)
,...,p−ε−1(JmJ+1−(cid:80)J ℓ=1 m ℓ )
(λ
mJ+1
s◦

## J

θ)nJ+1−mJ+1(cid:17)
J 1! (n −m )!

## J+1 J+1

is rescaled moment curve over B(0,1) of degree n −m ; thus, the decoupling inequality

## J+1 J+1

provides
(cid:13) (cid:13)
(cid:13) (cid:88) (cid:13) − ε (1−

### DnJ+1−mJ+1+ε)

(cid:13) g (cid:13) ≤C s nJ+1−mJ+1 qn
(cid:13) θ(cid:13) nJ+1−mJ+1,(nJ+1−mJ+1)ε J+1
(cid:13) (cid:13)
θ∈I∩Λ δ Lqn(Qn)
p
 1/qn

(cid:13) (cid:13)qn

 (cid:88) (cid:13) (cid:88) (cid:13) 
× (cid:13) g (cid:13)  .
(cid:13) θ(cid:13)
 
 Θ′∈P (cid:16) Θ,s◦s (1+nJ+1− 1 mJ+1 )ε (cid:17)(cid:13) θ∈Θ′∩Λ δ (cid:13) Lqn(Qn p ) 

## J J+1

Iterating as in Lemma 4.1 over 1 ≤ k ≤ nJ+1−mJ+1, together with a terminal triangle inequality
ε
and Cauchy-Schwarz, we obtain
(cid:13) (cid:13)
(cid:13) (cid:13) (cid:88) g (cid:13) (cid:13) ≤pε−1Jn(log δ−1)C nJ+1− ε mJ+1 s −(mJ+1+3)ε−(1− DnJ+1 q − n mJ+1)
(cid:13)
(cid:13)
θ(cid:13)
(cid:13)
p nJ+1−mJ+1,(nJ+1−mJ+1)ε J+1
θ∈Θ∩Λ δ Lqn(Qn)
p

(cid:13) (cid:13)qn
1/qn
(cid:88) (cid:13) (cid:88) (cid:13)
× (cid:13) (cid:13) g θ (cid:13) (cid:13)  .
(cid:13) (cid:13)

### Θ′∈P(Θ,s◦ J+1 ) θ∈Θ′∩Λ δ Lqn(Qn p )

Undoing the change-of-variable, we achieve the desired result.
If instead the first option of 4.8 holds, we set n = n − 1 and, for each choice m ≤

## J+1 J J

m ≤ m and s ∈ p−ε−1N with

## J+1 J+1

(cid:32) (cid:33) 1
(cid:89)
J nJ+1−mJ+1
δ s
−(nJ−mj)
≤ s < 1,
j J+1
j=1
we set
(cid:110) (cid:104) (cid:105)
(cid:0) (cid:1) (cid:0) (cid:1)
Ω = γ(1) s◦θ ,...,γ(n) s◦θ ·DsJ (λ) ∈ Ω :
θ,mJ+1,sJ+1 mJ,sJ J mJ,sJ J mJ,nJ θ,mJ+1
∃ι ∈ [1,m−m ] s.t. sι ≤ |λ | ,
J+1 J+1 mJ+1+ι p
(cid:111)
∀ι ∈ [1,m−m ]|λ | < sι pιε−1 .
J+1 mJ+1+ι p J+1
22

<!-- Page 23 -->

By an identical argument to the previous case (pigeonholing the ranges of λ, comparing with
a cylinder, decoupling and iteration), we obtain that there are some m and s as above

## J+1 J+1

such that
(cid:13) (cid:13) (cid:13) (cid:88) g (cid:13) (cid:13) (cid:13) ≤pJnε−1(log δ−1)C nJ+1− ε mJ+1 s −(mJ+1+3)ε− (cid:0) 1− DnJ+1 q − n mJ+1 (cid:1)
(cid:13)
(cid:13)
θ(cid:13)
(cid:13)
p nJ+1−mJ+1,(nJ+1−mJ+1)ε J+1
θ∈Θ∩Λ δ Lqn(Qn)
p

(cid:13) (cid:13)qn
1/qn
(cid:88) (cid:13) (cid:88) (cid:13)
× (cid:13) (cid:13) g θ (cid:13) (cid:13)  ,
(cid:13) (cid:13)

### Θ′∈P(Θ,s◦ J+1 ) θ∈Θ′∩Λ δ Lqn(Qn p )

and once again by changing variables we are done.
Observe that, for each iteration of Lemma 4.3, we obtain a new decoupling of F into
frequency-localized pieces indexed by parameters s ,m ,n with the condition that, when J

## J J J

increases by 1, either m increases by at least 1 or n decreases by at least 1, or already s has

## J J J

localized all the way to δ. Since n = n and 0 ≤ m ≤ m, we see that after J ≤ 2n steps the
1 1
output of Lemma 4.3 is an estimate of the form
∥F∥ Lqn(Qn p ) ≤ pJ2nε−1 (cid:88) (cid:89) J (cid:20) C n n J J − − ε m mJ J,(nJ−mJ)ε s − J ε−(1− DnJ q − n mJ) (cid:21)
sJ,mJ,nJJ=1

(cid:13) (cid:13)qn
1/qn
(cid:13) (cid:13)
(cid:88) (cid:13) (cid:88) (cid:13)
× (cid:13) F (cid:13)  .
 θ 
(cid:13) (cid:13)
(Θ0,...,ΘJ)∈TsJ,mJ,nJ (cid:13)θ∈ΘJ∩Λ δ (cid:13) Lqn(Qn)
p
Note also that there are ≤ (log (δ−1)mn)2n choices of tuples s ,m ,n in the initial sum.
p J J J
Pigeonholing, we obtain that for some choice s ,m ,n , we have the upper bound

## J J J

∥f∥ Lqn(Qn p ) ≤ pJ2nε−1(log(δ−1)n)4n (cid:89) J (cid:20) C n n J J − − ε m mJ J,(nJ−mJ)ε s − J ε−(1− DnJ q − n mJ) (cid:21)

## J=1


(cid:13) (cid:13)qn
1/qn
(cid:88) (cid:13) (cid:88) (cid:13)
× (cid:13) (cid:13) f θ (cid:13) (cid:13)  .
(cid:13) (cid:13)

### Θ∈P(Z p,s◦ J ) θ∈Θ∩Λ δ Lqn(Qn p )

By the triangle inequality and H¨older, we reach our terminal decoupling
∥f∥ Lqn(Qn p ) ≤ pJ2nε−1(log(δ−1)n)4n (cid:89) J (cid:20) C n n J J − − ε m mJ J,(nJ−mJ)ε s − J ε−(1− DnJ q − n mJ) (cid:21)

## J=1

(cid:32) (cid:33)1/qn
×(δ−1s◦ J )1− q 1 n (cid:88) ∥f θ ∥ L qn qn(Qn) .
p
θ∈Λ
δ
It remains to analyze the losses we have incurred. Rearranging factors, we have
(cid:34)
(cid:89) J s − J ε−(1− DnJ q − n mJ)
(cid:35)
(s◦ J )1− q 1 n = (s◦ J )−ε
(cid:34)
(cid:89) J s1 J +...+(nJ−mJ)
(cid:35)1/qn
.

## J=1 J=1

23

<!-- Page 24 -->

Note that n = n and n = m+1. Let j ,...,j be the indices such that n = n −1.
1 J 1 n−m j +1 j
k k
At each such index, we have the identity
j
s
njk −mjk
(cid:89)k
s
(njk −1−mη)
= δ.
j +1 η
k
η=1
Multiplying these identities together, we obtain

## J

(cid:89)
s1+...+(nJ−mJ) ≤ δn−m.

## J


## J=1

Thus, we have demonstrated
(cid:34)

## J

(cid:35) (cid:32) (cid:33)1/qn
∥f∥ Lqn(Qn p ) ≤ pJ2nε−1(log(δ−1)n)4n (cid:89) C n n J J − − ε m mJ J,(nJ−mJ)ε (s◦ J )−εδ−1+n− q m n +1 (cid:88) ∥f θ ∥q L n qn(Qn p ) ,
J=1 θ∈Λ
δ
and by the trivial bound s◦ ≥ δ and Theorem 6.1, together with Remark 6.23, we have the

## J

upper bound
(cid:32) (cid:33)1/qn
∥f∥ Lqn(Qn p ) ≤ exp (cid:16) 104ε−4nlogn−1n4n2+4n(logp) (cid:17) δ−1+n− q m n +1−ε (cid:88) ∥f θ ∥q L n qn(Qn p ) .
θ∈Λ
δ
It remains only to remove the special assumptions on δ and ε. Fix ε = 1 for some ℓ ∈ N,
ℓκ
and suppose that δ ∈ p−N is such that
p−κ2(K+1) < δ < p−κ2K, K ∈ N.
Then, by what we have proven for δ′ = p−κ2K, if Λ ⊆ Λ is any δ′-separated subset,
δ′ δ
(cid:13) (cid:13)  1/qn
(cid:13) (cid:13)
(cid:13) (cid:13) (cid:13) (cid:88) f θ (cid:13) (cid:13) (cid:13) ≤ exp (cid:16) 104ε−4nlogn−1n4n2+4n(logp) (cid:17) (δ′)−1+n− q m n +1−ε  (cid:88) ∥f θ ∥q L n qn(Qn p )  .
(cid:13)θ∈Λ δ′ (cid:13) Lqn(Qn) θ∈Λ δ′
p
Controlling f by a sum over δ′/δ-many subsets Λ , we conclude that
δ′
(cid:32) (cid:33)1/qn
∥f∥ Lqn(Qn p ) ≤ exp (cid:16) 104ε−4nlogn−1n6n2+4n(logp) (cid:17) δ−1+n− q m n +1−ε (cid:88) ∥f θ ∥q L n qn(Qn p ) .
θ∈Λ
δ
In the case p−κ2 < δ ≤ p−1, a trivial inequality suffices to get the same result.
Next, we remove the special assumption on ε. If ℓ ∈ N is such that
(n!)−2n (n!)−2n
< ε < ,
ℓ+1 ℓ
then for any δ ∈ p−N, using (ℓ+1)(n!)2n ≤ 2ε−1, we have shown that
(cid:32) (cid:33)1/qn
∥f∥ Lqn(Qn p ) ≤ exp (cid:16) 104ε−4nlogn−1n6n2+6n(logp) (cid:17) δ−1+n− q m n +1−ε (cid:88) ∥f θ ∥q L n qn(Qn p ) ,
θ∈Λ
δ
and we are done (noting that a trivial inequality suffices for the same result when ε > (n!)−2n).
24

<!-- Page 25 -->


## Q

5 Appendix A: Decoupling lemmas over
p
In this section, we record various elementary lemmas regarding Fourier decoupling over Q .
p
Each of these is a cousin of a standard result over R, and some of ours will be even stronger.
Several of these lemmas have already been demonstrated in [7].
Throughout this section, Ω will denote a subset of Qd and Θ will denote a family of subsets
p
(cid:83)
ofΩ, suchthatΩ = θ. Wewillalsoemphasizethatall functions f are locally constant and
θ∈Θ θ
of compact support, and indicate the corresponding class via S(Qd). We emphasize that “locally
p
constant” means that there is some scale λ ∈ pZ such that ∥x−y∥ ≤ λ implies f (x) = f (y).
θ θ
The class S(Qd) is the appropriate replacement for Schwartz functions in the p-adic setting;
p
they are precisely the “Schwartz-Bruhat functions” over Qd.
p
For exponents 2 ≤ q ≤ r ≤ ∞, q < ∞, define Dec (Θ) to be the infimal C > 0 such that,
ℓqLr
ˆ
for any family {f : θ ∈ Θ} such that f is supported in θ, for each θ,
θ θ
(cid:13) (cid:13) (cid:32) (cid:33)1/q
(cid:13)(cid:88) (cid:13) (cid:88)
(cid:13) f (cid:13) ≤ C ∥f ∥q .
(cid:13) θ(cid:13) θ Lr(Qd)
(cid:13) (cid:13) p
θ∈Θ Lr(Qd) θ∈Θ
p
Observe that we have not insisted that the sets θ ∈ Θ are pairwise disjoint; in applications,
this will often be true, but for many technical results it is convenient to allow O(1) overlap
between the caps.
The following is demonstrated in [7], Prop. 4.4, in the case q = 2 and for specific choices of
θ. The proof of this version is identical.
Lemma 5.1 (Interpolation of decoupling constants). If 1 = α + 1−α, α ∈ [0,1], and 1 ≤ q ≤
min(r ,r ), then for any partition Ω = (cid:83) θ with every r θ a r0 sepa r r 1 ate affine image of Zd, we
0 1 θ∈Θ p
have
Dec (Θ) ≤ Dec (Θ)αDec (Θ)1−α.
ℓqLr ℓqLr0 ℓqLr1
As a consequence, we obtain the following. Observe that we do not need to assume that
the θ are all congruent, in contrast to the Euclidean case.
Lemma 5.2 (Flat decoupling). For any Ω ⊆ Qd and any partition Θ of Ω composed of affine
p
images θ ∈ Θ of Zd and any q,r ≥ 2,
p
Dec ℓqLp (Θ) ≤ (#Θ)1− r 1−1 q.
Proof. Fixanyfamily{f : θ ∈ Θ}. Then,byPlancherel,theseelementsarepairwiseorthogonal
θ
in L2(Qd); thus
p
(cid:13) (cid:13) (cid:32) (cid:33)1/2
(cid:13)(cid:88) (cid:13) (cid:88)
(cid:13) f (cid:13) ≤ ∥f ∥2 , (5.1)
(cid:13) θ(cid:13) θ L2(Qd)
(cid:13) (cid:13) p
θ∈Θ L2(Qd) θ∈Θ
p
so Dec (Θ) ≤ 1. By the triangle inequality and Cauchy-Schwarz,
ℓ2L2
(cid:13) (cid:13) (cid:32) (cid:33)1/2
(cid:13)(cid:88) (cid:13) (cid:88)
(cid:13) f (cid:13) ≤ (#Θ)1/2 ∥f ∥2 . (5.2)
(cid:13) θ(cid:13) θ L∞(Qd)
(cid:13) (cid:13) p
θ∈Θ L∞(Qd) θ∈Θ
p
25

<!-- Page 26 -->

By Lemma 5.1, the statements 5.1 and 5.2 give
Dec (Θ) ≤ Dec (Θ)
r−2

## ≤ (#Θ)

1−1
.
ℓ2Lr ℓ2L∞ r 2 r

### By H¨older,

(cid:32) (cid:33)1/2 (cid:32) (cid:33)1/q
(cid:88) ∥f θ ∥2 Lr(Qd p ) ≤ (#Θ) 1 2 −1 q (cid:88) ∥f θ ∥q Lr(Qd p ) .
θ∈Θ θ∈Θ

### Thus

(cid:13) (cid:13) (cid:32) (cid:33)1/2 (cid:32) (cid:33)1/q
(cid:13) (cid:13) (cid:13) (cid:13) (cid:88) f θ (cid:13) (cid:13) (cid:13) (cid:13) ≤ (#Θ) 1 2 − r 1 (cid:88) ∥f θ ∥2 Lr(Qd p ) ≤ (#Θ)1− r 1−1 q (cid:88) ∥f θ ∥q Lr(Qd p ) ,
θ∈Θ Lr(Qd) θ∈Θ θ∈Θ
p
and so Dec ℓqLr (Θ) ≤ (#Θ)1− r 1−1 q, as claimed.
Lemma 5.3 (Affine invariance of decoupling constants). Suppose A is an invertible affine map
Qd → Qd. Then Dec (AΘ) = Dec (Θ), where AΘ = {Aθ : θ ∈ Θ}.
p p ℓqLr ℓqLr
ˆ
Proof. We first take A to be linear for simplicity. Suppose {f : θ ∈ Θ} are such that f is
θ θ
supported in θ. Define g = (f ˆ ◦A−1)∨. Then gˆ is supported in Aθ, so
θ θ θ
(cid:13) (cid:13) (cid:32) (cid:33)1/q
(cid:13)(cid:88) (cid:13) (cid:88)
(cid:13) g (cid:13) ≤ Dec (AΘ) ∥g ∥q . (5.3)
(cid:13) θ(cid:13) ℓqLr θ Lr(Qd)
(cid:13) (cid:13) p
θ∈Θ Lr(Qd) θ∈Θ
p
Observe that the following change-of-variables holds:
ˆ ˆ
1 1
g (x) = f ˆ (A(ξ))χ(x·ξ)dξ = f ˆ (ω)χ(A−⊤(x)·ω)dω = f(A−⊤(x)),
θ θ µ(A[Zd]) θ µ(A[Zd])
Qd p Qd p
p p
so that
∥g ∥ =
µ(A[Zd])−1+1
∥f ∥ .
θ Lr(Qd p ) p r θ Lr(Qd p )

### In particular, 5.3 rearranges to

(cid:13) (cid:13) (cid:32) (cid:33)1/q
(cid:13)(cid:88) (cid:13) (cid:88)
(cid:13) f (cid:13) ≤ Dec (AΘ) ∥f ∥q .
(cid:13) θ(cid:13) ℓqLr θ Lr(Qd)
(cid:13) (cid:13) p
θ∈Θ Lr(Qd) θ∈Θ
p
Since the {f : θ ∈ Θ} were arbitrary, we conclude that
θ
Dec (Θ) ≤ Dec (AΘ).
ℓqLr ℓqLr
Since this holds for all invertible linear A, we conclude that Dec (Θ) = Dec (AΘ) for all
ℓqLr ℓqLr
invertible linear A.
Finally, we note that decoupling constants are trivially invariant under translation, as
Fourier translation is equivalent to spatial modulation, which does not affect absolute values.
Thus the claim holds.
26

<!-- Page 27 -->

Lemma 5.4 (Local decoupling). Suppose every θ ∈ Θ is of the form A [Zd] + v for linear
θ p θ
isomorphisms A : Qd → Qd. Set
θ p p
η := max∥A−1∥,
θ
θ∈Θ
where ∥ · ∥ is the usual ℓ∞ → ℓ∞ operator norm. Write Decloc (Θ) for the infimal C > 0 such
ℓqLr
that, for any family {f : θ ∈ Θ} such that f ˆ is supported in θ, and for any x ∈ Qd, we have
θ θ p
(cid:13) (cid:13) (cid:32) (cid:33)1/q
(cid:13)(cid:88) (cid:13) (cid:88)
(cid:13) f (cid:13) ≤ C ∥f ∥q .
(cid:13) θ(cid:13) θ Lr(B(x,η))
(cid:13) (cid:13)
θ∈Θ Lr(B(x,η)) θ∈Θ

### Then we have

Dec (Θ) = Decloc (Θ).
ℓqLr ℓqLr
Proof. Let {f } be any family as stated. Let x ∈ Qd be arbitrary. Write
θ θ∈Θ p
g(y) = 1 (y), gˆ(ξ) = χ(−x·ξ)1 (ξ).
B(x,η) B(0,η−1)

### Then we have

(cid:13) (cid:13) (cid:13) (cid:13)
(cid:13)(cid:88) (cid:13) (cid:13)(cid:88) (cid:13)
(cid:13) f (cid:13) = (cid:13) gf (cid:13) ,
(cid:13) θ(cid:13) (cid:13) θ(cid:13)
(cid:13) (cid:13) (cid:13) (cid:13)
θ∈Θ Lr(B(x,η)) θ∈Θ Lr(Qd)
p
and
g(cid:99)f
θ
(ξ) = [χ(−x·)1
B(0,η−1)
]∗f ˆ
θ
(ξ),
which is still supported in θ. Thus
(cid:13) (cid:13) (cid:32) (cid:33)1/q
(cid:13)(cid:88) (cid:13) (cid:88)
(cid:13) gf (cid:13) ≤ Dec (Θ) ∥gf ∥q .
(cid:13) θ(cid:13) ℓqLr θ Lr(Qd)
(cid:13) (cid:13) p
θ∈Θ Lr(Qd) θ∈Θ
p
Thus we have Decloc (Θ) ≤ Dec (Θ).
ℓqLr ℓqLr
We consider the reverse inequality. We redefine g = 1 . Let X be the set of standard

### B(0,η)

representatives of Qd/B(0,η); i.e. we represent x + B(0,η) by y when η−1y has zero integer
p
part. Then we have:
ˆ (cid:12) (cid:12)r ˆ (cid:12) (cid:12)r
(cid:12)(cid:88) (cid:12) (cid:88) (cid:12) (cid:88) (cid:12)
(cid:12) f (cid:12) = (cid:12)g(y −x) f (y)(cid:12) dµ(y)
(cid:12) θ(cid:12) (cid:12) θ (cid:12)
Qd(cid:12) (cid:12) B(x,η)(cid:12) (cid:12)
p θ∈Θ x∈X θ∈Θ
ˆ
(cid:32)
(cid:20) (cid:21)q/r
(cid:33)r/q
(cid:88) (cid:88)
≤ Decloc (Θ)r |f (y)|rdµ(y) .
ℓqLr θ

### B(x,η)

x∈X θ∈Θ
By Minkowski, we have
(cid:32)
(cid:20)
ˆ
(cid:21)q/r
(cid:33)r/q

(cid:32)
ˆ
(cid:33)q/r
r
(cid:88) (cid:88) (cid:88) (cid:88)
|f θ (y)|rdµ(y) ≤  |f θ (y)|rdµ(y)  .

### B(x,η) B(x,η)

x∈X θ∈Θ θ∈Θ x∈X
Taking rth roots, we obtain the inequality Dec (Θ) ≤ Decloc (Θ).
ℓqLr ℓqLr
27

<!-- Page 28 -->

Lemma 5.5 (Decoupling tensorizes). Let Ω ⊆ Qd,Ω ⊆ Qe be any sets and let Θ ,Θ be any
1 p 2 p 1 2
partitions of Ω ,Ω , respectively. Write Θ for the partition of Ω ×Ω by sets of the form θ×τ
1 2 1 2
(θ ∈ Θ ,τ ∈ Θ ). Suppose q ≤ r. Then
1 2
Dec (Θ) = Dec (Θ )Dec (Θ )
ℓqLr ℓqLr 1 ℓqLr 2
Proof. First consider any family {f1 : θ ∈ Θ } and {f2 : τ ∈ Θ } with f ˆ1 supported in θ and
θ 1 τ 2 θ
f ˆ2 supported in τ. Define g : Qd+e → C by
τ (θ,τ) p
g (x,y) = f1(x)f2(y)
(θ,τ) θ τ
Then gˆ (ξ,ω) = f
ˆ1(ξ)f ˆ2(ω)
is supported in θ×τ. In particular,
(θ,τ) θ τ
(cid:13) (cid:13) (cid:32) (cid:33)1/q
(cid:13) (cid:88) (cid:13) (cid:88)
(cid:13) g (cid:13) ≤ Dec (Θ) ∥g ∥q
(cid:13)
(cid:13)
(θ,τ)(cid:13)
(cid:13)
ℓqLr (θ,τ) Lr(Q
p
d+e)
θ×τ∈Θ Lr(Qd
p
+e) θ×τ∈Θ

### Processing both sides of this, observe that

(cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13)
(cid:13) (cid:88) (cid:13) (cid:13)(cid:88) (cid:13) (cid:13)(cid:88) (cid:13)
(cid:13) g (cid:13) = (cid:13) f1(cid:13) (cid:13) f2(cid:13)
(cid:13) (θ,τ)(cid:13) (cid:13) θ(cid:13) (cid:13) τ(cid:13)
(cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13)
θ×τ∈Θ Lr(Qd p +e) θ∈Θ1 Lr(Qd p ) τ∈Θ2 Lr(Qe p )
and
(cid:32) (cid:33)1/q (cid:32) (cid:33)1/q(cid:32) (cid:33)1/q
(cid:88) (cid:88) (cid:88)
∥g ∥q = ∥f1∥q ∥f2∥q
(θ,τ) Lr(Qd
p
+e) θ Lr(Qd
p
) τ Lr(Qe
p
)
θ×τ∈Θ θ∈Θ1 τ∈Θ2
Picking {f1} and {f2} , not all zero, such that
θ θ∈Θ1 τ τ∈Θ2
(cid:13) (cid:13) (cid:32) (cid:33)1/q
(cid:13)(cid:88) (cid:13) (cid:88)
(cid:13) f1(cid:13) ≥ (1−ε)Dec (Θ ) ∥f1∥q ,
(cid:13) θ(cid:13) ℓqLr 1 θ Lr(Qd)
(cid:13) (cid:13) p
θ∈Θ1 Lr(Qd) θ∈Θ1
p
(cid:13) (cid:13) (cid:32) (cid:33)1/q
(cid:13)(cid:88) (cid:13) (cid:88)
(cid:13) f2(cid:13) ≥ (1−ε)Dec (Θ ) ∥f1∥q
(cid:13) τ(cid:13) ℓqLr 2 τ Lr(Qd)
(cid:13) (cid:13) p
τ∈Θ2 Lr(Qd) τ∈Θ2
p
we see that
(1−ε)2Dec (Θ )Dec (Θ ) ≤ Dec (Θ).
ℓqLr 1 ℓqLr 2 ℓqLr
Taking ε → 0 we obtain the inequality
Dec (Θ )Dec (Θ ) ≤ Dec (Θ)
ℓqLr 1 ℓqLr 2 ℓqLr
It remains to establish the reverse inequality.
Let {g } be a family with gˆ supported in θ ×τ. Then, for each fixed y ∈ Qe,
(θ,τ) (θ,τ)∈Θ (θ,τ) p
observe that x (cid:55)→ g (x,y) has Fourier support contained in the set θ. Thus
(θ,τ)
ˆ ˆ (cid:12) (cid:12)r ˆ  (cid:32) ˆ (cid:12) (cid:12)r (cid:33)q/r r/q
(cid:12)(cid:88) (cid:88) (cid:12) (cid:88) (cid:12)(cid:88) (cid:12)
(cid:12) (cid:12) g (θ,τ) (x,y)(cid:12) (cid:12) dxdy ≤ Dec ℓqLr (Θ 1 )r  (cid:12) (cid:12) g (θ,τ) (x,y)(cid:12) (cid:12) dx  dy
Qe Qd(cid:12) (cid:12) Qe Qd(cid:12) (cid:12)
p p θ∈Θ1τ∈Θ2 p θ∈Θ1 p τ∈Θ2
28

<!-- Page 29 -->

By Minkowski, using q ≤ r,
ˆ ˆ
(cid:104) (cid:88) (cid:16) (cid:12) (cid:88) (cid:12)r (cid:17)q/r(cid:105)r/q
(cid:12) g (x,y)(cid:12) dx dy
(cid:12) (θ,τ) (cid:12)

### Qe Qd

p θ∈Θ1 p τ∈Θ2 ˆ ˆ
(cid:104) (cid:88) (cid:16) (cid:12) (cid:88) (cid:12)r (cid:17)q/r(cid:105)r/q
≤ (cid:12) g (x,y)(cid:12) dxdy ,
(cid:12) (θ,τ) (cid:12)

### Qe Qd

θ∈Θ1 p p τ∈Θ2
and we may apply Fubini and decouple further to obtain for each θ
ˆ ˆ (cid:12) (cid:12)r ˆ ˆ
(cid:12)(cid:88) (cid:12) (cid:104) (cid:88) (cid:16) (cid:17)q/r(cid:105)r/q
(cid:12) g (x,y)(cid:12) dxdy ≤ Dec (Θ )r |g (x,y)|rdy dx.
(cid:12) (θ,τ) (cid:12) ℓqLr 2 (θ,τ)
Qe Qd(cid:12) (cid:12) Qd Qe
p p τ∈Θ2 p τ∈Θ2 p

### Collecting all the preceding,

(cid:13) (cid:88) (cid:88) (cid:13)
(cid:13) g (cid:13) ≤ Dec (Θ )Dec (Θ )
(cid:13) (θ,τ)(cid:13) ℓqLr 1 ℓqLr 2
θ∈Θ1τ∈Θ2
Lr(Qd
p
+e)
ˆ ˆ
×
(cid:110) (cid:88) (cid:104) (cid:16) (cid:88) (cid:0)
|g (x,y)|rdy
(cid:1)q/r (cid:17)r/q
dx
(cid:105)q/r(cid:111)1/q
(θ,τ)

### Qd Qe

θ∈Θ1 p τ∈Θ2 p
Applying Minkowski again,
ˆ ˆ
(cid:110) (cid:88)(cid:104) (cid:16) (cid:88) (cid:0)
|g (x,y)|rdy
(cid:1)q/r (cid:17)r/q
dx
(cid:105)q/r(cid:111)1/q
(θ,τ)

### Qd Qe

θ∈Θ1 p τ∈Θ2 ˆp ˆ
(cid:104) (cid:88) (cid:88) (cid:16) (cid:17)q/r(cid:105)1/q
≤ |g (x,y)|rdydx ,
(θ,τ)

### Qd Qe

θ∈Θ1τ∈Θ2 p p
from which we obtain the estimate
(cid:13) (cid:88) (cid:13) (cid:16) (cid:88) (cid:17)1/q
(cid:13) g (cid:13) ≤ Dec (Θ )Dec (Θ ) ∥g ∥q .
(cid:13) θ×τ∈Θ (θ,τ)(cid:13) Lr(Qd p +e) ℓqLr 1 ℓqLr 2 θ×τ∈Θ (θ,τ) Lr(Qd p +e)
Since this holds for all arrangements {g } as in the definition of the decoupling constant
(θ,τ) θ,τ
for Θ, we conclude that
Dec (Θ) ≤ Dec (Θ )Dec (Θ ),
ℓqLr ℓqLr 1 ℓqLr 2
so we have equality, as claimed.

### A special case of the previous lemma is the following:

Lemma 5.6 (Cylindrical decoupling). Let Ω ⊆ Qd be any set and Θ be a partition of Ω. Write
p
Θ(cid:101) for the partition of Ω×Qe by Θ ˜ = {θ×Qe : θ ∈ Θ}. Suppose q ≤ r. Then
p p

### Dec

ℓqLr
(Θ(cid:101)) = Dec
ℓqLr

## (Θ).

The following is at least as ubiquitous in decoupling methods as affine invariance.
29

<!-- Page 30 -->

Lemma 5.7 (Multiplicativity of decoupling constants). Let 2 ≤ q,r ≤ ∞ and q < ∞. Let Θ
be a finite set-family in Qd. Suppose that, for each θ ∈ Θ, there is a further set-family Θ with
p θ
(cid:83)
the property that ψ = θ. Then it holds that
ψ∈Θ
θ
(cid:0) (cid:71) (cid:1)
Dec Θ ≤ Dec (Θ)×maxDec (Θ ).
ℓqLr θ ℓqLr ℓqLr θ
θ∈Θ
θ∈Θ
Proof. Immediate from the structure of decoupling inequalities.
The following lemma is sometimes helpful.
Lemma 5.8 (ℓ2Lr recoupling). Let 2 ≤ r ≤ ∞, and assume that θ ∈ Θ are pairwise disjoint
affine images of Zn. Then, for any family {f : θ ∈ Θ} such that f ˆ is supported in θ, we have
p θ θ
(cid:32) (cid:33)1/2 (cid:13) (cid:13)
(cid:88) (cid:13)(cid:88) (cid:13)
∥f ∥2 ≤ (#Θ) 1−1 (cid:13) f (cid:13) .
θ Lr(Qd) 2 r (cid:13) θ(cid:13)
p (cid:13) (cid:13)
θ∈Θ θ∈Θ Lr(Qd)
p
Proof. The special cases r = 2,r = ∞ are trivial. For the rest, we interpolate.

### We also recall the main result of [7]:

Theorem 5.9. Fix any δ ∈ p−N. Consider the region Ω defined by
Ω = {(x,y) ∈ Q2 : |x| ≤ 1,|y −x2| ≤ δ2}.
p p p
We let T = P(Z ,δ) to be the partition of Z into closed balls of radius δ. For each τ ∈ T ,
p p
define
θ = {(x,y) ∈ Q2 : x ∈ τ,|y −x2| ≤ δ2}.
τ p p
Clearly {θ } form a decomposition Θ of Ω. Then we have
τ τ∈T
Dec (Θ) ≲ δ−ε(1+δ−(1−3)).
ℓ2Lr ε,p,r 2 r
6 Appendix B: Decoupling for the p-adic moment curve
We sketch a proof of ℓ2Ln(n+1) decoupling for the moment curve t (cid:55)→ γ(t) in Qn by modifying
p
an existing argument for the same result in Rn. This fact is of interest in its own right; however,
the proof is nearly identical to the proof over R for most approaches, so we have suppressed it
to this appendix. One slight novelty is the tracking of constants throughout, for the purpose
of achieving an explicit effective bound for our main application.

### The result to be shown is the following:

Theorem 6.1 (ℓ2Ln(n+1) decoupling for the moment curve in Qn). Let n ∈ N. For every ε > 0
p
there is a constant C ≥ 1 such that for all δ ∈ p−N, one has the estimate
n,ε

### Dec ({U } ) ≤ C δ−ε,

ℓ2Ln(n+1) I I∈P(Z p,δ) n,ε
where P(Z ,δ) is a partition of Z into balls of radius δ, and U is the standard anisotropic
p p I
neighborhood of the moment curve over I; see the start of the next section. Moreover, the
constant C may be taken to be
n,ε
(cid:16) (cid:17)
C = exp 104(logp)ε−4nlognn10n2 .
n,ε
30

<!-- Page 31 -->

Remark 6.2. Optimizing over ε, one can show that the decoupling constant is bounded by
something of the form exp(C (logδ−1)1−cn), for suitable explicit C ≥ 1,c ∈ (0,1). See
n n n
Theorem 1.5 for details, in the application to solution counting.
Most of the tools used in the standard approaches to decoupling are identical between Rn
and Qn, with some caveats: for one, over Q many heuristic uncertainty statements from the
p p
Euclideansettingbecomeliterallytrue, whichallowsonetodispenseofvarioustechnicalweights
and convolutions; for another, some of the induction-on-dimension steps require some special
geometric observations (via projections), which require modification in the p-adic setting.
To be more precise about the latter: it is a classical fact that bilinear forms generally, and
the dot product in particular, possess isotropy on Qn for n sufficiently large. We recall two
p
results in particular:
Theorem 6.3 (Chapter 4, Lemma 2.7 of [1]). Let n ≥ 5 and p arbitrary. Then every quadratic
form over Qn has isotropy.
p
Theorem 6.4. Let p be odd and n ≥ 3. Then the dot product (x ,...,x ) · (y ,...,y ) =
1 n 1 n
x y +...+x y has isotropy.
1 1 n n
We briefly recall a proof of Theorem 6.4. We first instead study q(x,y,z) = x2 + y2 + z2
over F . The set of values {x2 : x ∈ F } and {−y2 − 1 : y ∈ F } each have cardinality p+1,
p p p 2
while #F = p, so the two sets must intersect at a value where x2 + y2 + 12 = 0, which
p
establishes isotropy over F . Consequently, the representatives of x,y in {0,...,p − 1} in Z
p
solve q(x,y,1) ≡ 0 mod p. On the other hand, formally differentiating q with respect to x and
y,
∂ q(x,y,1) = 2x, ∂ q(x,y,1) = 2y.
x y
Since x2+y2+1 ≡ 0 mod p, we may assume without loss of generality that x ̸≡ 0 mod p. Since
p is odd,
∂ q(x,y,1) ̸≡ 0 mod p.
x
By Hensel’s lemma (see Chapter 3, Lemma 4.1 of [1]), there is a root of t (cid:55)→ q(t,y,1) in Z ,
p
which establishes Theorem 6.4.
As a consequence, some of the proofs of induction on dimension-type estimates fail. As
it turns out, the differences are entirely superficial; when the arguments are converted into
linear-algebraic manipulations, the proofs hold as usual.
As many of the arguments in the proof of decoupling require little modification, we will
simply review the short proof of moment-curve decoupling in [5] and supply the needed modifications. In particular, our argument will not be completely self-contained, and will instead
point to the latter paper for the proofs of certain technical steps for which no modification is
needed.
Weinsistattheoutsetthatwewillonlyconsiderthecasep > n, toavoidcertaintechnicalissues. Ithappensthatthesameresultholdsforgeneralp(indeed, forarbitrarynon-Archimedean
local fields of characteristic 0), though the argument requires attending to certain additional
technicalities that we are able to avoid.
We will write throughout |·| for the p-adic norm on Q , and |·| for the usual Euclidean
p p
norm on R and C. We will also equip Qn with the usual choice of norm, ∥x∥ = max |x | .
p 1≤i≤n i p
This notation will overlap with the Lebesgue norm ∥·∥ . In each case, it will be clear from
Lq(Qn)
p
context which is intended.
31

<!-- Page 32 -->

6.1 Bilinear-to-linear reduction
For δ ∈ p−N and a ball U, write P(U,δ) for the partition of U into (closed) balls of radius δ;
more generally, if δ ∈ (0,1) is not necessarily a power of p, then we understand P(U,δ) to be
a partition into balls of radius ρ, where ρ is the greatest number in p−N below δ. For a convex
Cn curve ζ with bounded derivatives, as defined in Appendix C, we define the systems of boxes
Uζ , for I ⊆ Z a metric ball of radius ρ and t ∈ I, as
I,t p
n n
(cid:110) (cid:89) (cid:88) (cid:111)
Uζ := x ∈ Qn : ∃{λ }n ∈ B (0) s.t. x = ζ(t)+ λ ζ(k)(t) .
I,t p k k=1 ρk k
k=1 k=1
Throughout this section, when the ζ superscript on U is suppressed, it will be assumed that

### I,t

U = Uγ where γ(t) = (t,..., tn) is the moment curve. We will write as well
I,t I,t 1! n!
(cid:91)
Uζ = Uζ .
I I,t
t∈I
This choice of caps is useful for technical reasons that appear in the proof below; in practice,
they can generally be compared with other natural caps at slightly coarser scales.
Our goal will be to bound the linear decoupling constant Dec ({U } ). We record
ℓ2Lqn I I∈P(Z p,δ)
for later reference an abbreviation:
Definition 6.5. For δ ∈ p−N, define D (δ) = Dec ({U } ).
n ℓ2Lqn I I∈P(Z p,δ)

### We will need a bilinear analogue as well:

Definition 6.6 (Symmetric bilinear decoupling constant). Fix δ ∈ p−N. We define the symmetric bilinear decoupling constant B (δ) to be the infimal (real) constant C such that the
n
following holds. Suppose I,J ∈ P(Z ,p−1) are distinct. For each I ∈ P(I,δ), let f ∈ S(Qn)
p i i p
be such that f ˆ is supported in U ; similarly, for each J ∈ P(J,δ), let g ∈ S(Qn) be such that
i Ii i i p
gˆ is supported in U . Then
i Ji
ˆ
(cid:32) (cid:33)qn/4(cid:32) (cid:33)qn/4
(cid:88) (cid:88)
|f |qn/2|g |qn/2 ≤ Cqn ∥f ∥2 ∥g ∥2 .
I J i Lqn(Qn) i Lqn(Qn)
Qn p p
p i i
By H¨older we have the trivial B (δ) ≤ D (δ). Before proceeding, we record the following
n n
standard converse, adapted to the p-adic setting:
Proposition 6.7 (Bilinear-to-linear reduction). If δ = p−N, then

## N

(cid:16) (cid:88) (cid:17)1/2
D (δ) ≤ p1/2 1+ B (pj−1δ)2 . (6.1)
n n
j=1
Proof. We formulate a Whitney cube decomposition for Zn; due to the ultrametric on Z , this
p p
will be simpler than the Euclidean analogue. For each j ≥ 1, define W as
j
(cid:110) (cid:111)
W := B (x)×B (y) : x,y ∈ Z ,|x−y| = p−j+1 .
j p−j p−j p p
32

<!-- Page 33 -->

Observe that, if |x − x′| ≤ p−j, then B (x) = B (x′), so W contains exactly pj(pj − 1)
p−j p−j j
elements. Additionally note that (cid:83) W defines a partition of Z2 \ ∆, where ∆ ⊆ Z × Z
j≥1 j p p p
denotes the diagonal.
ˆ
To verify the estimate 6.1, let {f } be a tuple with f supported in U . Then we
I I∈P(Z p,δ) I I
may write
(cid:13) (cid:88) (cid:13) (cid:13) (cid:88) (cid:13)1/2
(cid:13) f (cid:13) = (cid:13) f f (cid:13)
(cid:13) I(cid:13) (cid:13) I I′(cid:13)

### Lqn(Qn) Lqn/2(Qn)

I∈P(Z p,δ) p I,I′∈P(Z p,δ) p

## N

(cid:104) (cid:88) (cid:13) (cid:13)2 (cid:88) (cid:88) (cid:13) (cid:13) (cid:105)1/2
≤ (cid:13)f (cid:13) + (cid:13)f f (cid:13) .
I Lqn(Qn) J0 J1 Lqn/2(Qn)
p p

### I∈P(Z p,δ) j=1 J=J0×J1∈Wj

For each 1 ≤ j ≤ N and J = J ×J ∈ W , by decoupling and affine rescaling we have
0 1 j
 1/2 1/2
(cid:13) (cid:13) (cid:88) (cid:88)
(cid:13) (cid:13) f J0 f J1 (cid:13) (cid:13)

### Lqn/2(Qn)

≤ B n (pj−1δ)2  ∥f K ∥2 Lqn(Qn
p
)   ∥f K ∥2 Lqn(Qn
p
)  ,
p K∈P(J0,δ) K∈P(J1,δ)
so that (appealing to the AM-GM inequality)
(cid:13) (cid:13)  1/2
(cid:13) (cid:13) N
(cid:13) (cid:13) (cid:13) (cid:88) f I (cid:13) (cid:13) (cid:13) ≤ (cid:16) 1+(p−1) (cid:88) B n (pj−1δ)2 (cid:17)1/2  (cid:88) (cid:13) (cid:13)f I (cid:13) (cid:13) 2 Lqn(Qn p )  ,
(cid:13)I∈P(Z p,δ) (cid:13) Lqn(Qn) j=1 I∈P(Z p,δ)
p
which implies

## N

(cid:16) (cid:88) (cid:17)1/2
D (δ) ≤ p1/2 1+ B (pj−1δ)2 ,
n n
j=1
as was to be shown.
We also will need a system of asymmetric bilinear decoupling constants.
Definition 6.8 (Asymmetric bilinear decoupling constant). Fix δ = p−β ∈ p−N. For s,t ∈ [0,1]
with sβ,tβ ∈ Z, define the asymmetric bilinear decoupling constant B (δ) to be the infimal
n,k,s,t
(real) constant C such that the following holds. Suppose I,J are distinct balls of radius at
most δs,δt, respectively, contained in distinct members of P(Z ,p−1). For each I ∈ P(I,δ), let
p i
f ∈ S(Qn) be such that f ˆ is supported in U ; similarly, for each J ∈ P(J,δ), let g ∈ S(Qn)
i p i Ii i i p
be such that gˆ is supported in U . Then
i Ji
ˆ (cid:32) (cid:33)qk (cid:32) (cid:33)qn−qk
2 2
(cid:88) (cid:88)
|f |q k|g |qn−q k ≤ Cqn ∥f ∥2 ∥g ∥2 .
I J i Lqn(Qn) i Lqn(Qn)
Qn p p
p i i
We control the symmetric bilinear decoupling constant by the asymmetric bilinear decoupling constants:
Lemma 6.9. Let 0 ≤ k < n, δ = p−β ∈ p−N, and s,t ∈ [0,1] such that sβ,tβ ∈ Z. Then
B (δ) ≤ δ−sq k /qnδ−t(qn−q k )/qnB (δ).
n n,k,s,t
33

<!-- Page 34 -->

Proof. Identical to the proof of Lemma 3.4 of [5]; we validate the particular constant. Let
I,I′ ∈ P(Z ,p−1)bedistinct. Fix{f } beatupleasinthestatementofDefinition
p K K∈P(I,δ)∪P(I′,δ)

### Suppose k ̸= 0. By several applications of Ho¨lder,

ˆ ˆ ˆ
(cid:32) (cid:33)1/2(cid:32) (cid:33)1/2
|f |qn/2|f |qn/2 ≤ |f |q k|f |qn−q k |f |qn−q k|f |q k , (6.2)

## I I′ I I′ I I′

Qn Qn Qn
p p p
and considering the first factor:
ˆ ˆ
(cid:88)
|f |q k|f |qn−q k ≤ [#P(I,δs)]q k −1[#P(I′,δt)]qn−q k −1 |f |q k|f |qn−q k,

## I I′ J J′


### Qn Qn

p J∈P(I,δs) p

### J′∈P(I′,δt)

and recalling Definition 6.8 we have
ˆ  q
k
/2 (qn−q
k
)/2
(cid:88) (cid:88)
|f J |q k|f J′ |qn−q k ≤ B n,k,s,t (δ)qn ∥f K ∥2 qn   ∥f K ∥2 qn  .

### Qn

p K∈P(J,δ) K∈P(J′,δ)
Applying the trivial bounds #P(I,δs),#P(I′,δt) and on the operator norms of the inclusions
ℓ2 (cid:44)→ ℓq k,ℓqn−q k, we conclude that
ˆ
|f |q k|f |qn−q k ≤ p2−qnδ−s(q k −1)−t(qn−q k −1)B (δ)qn
I I′ n,k,s,t
Qn
p
 q
k
/2 (qn−q
k
)/2
(cid:88) (cid:88)
× ∥f K ∥2 qn   ∥f K ∥2 qn 

### K∈P(I,δ) K∈P(I′,δ)

Considering the other factor in 6.2, we break f into δ−t-many pieces and f into δ−s-many

## I I′

pieces and apply Ho¨lder, and we obtain an identical estimate. Since s,t ≥ 0 and q ≥ 2, the
n
result follows.
Finally, we observe that when k = 0, the same calculation (disregarding the terms involving
a k) may be done to obtain an estimate of the form
ˆ  qn/4 qn/4
(cid:88) (cid:88)
|f I |qn/2|f I′ |qn/2 ≤ p2−qnδs+tδ−tqnB n,k,s,t (δ)qn ∥f K ∥2 qn   ∥f K ∥2 qn 

### Qn

p K∈P(I,δ) K∈P(I′,δ)
and we are done.
We also record that the asymmetric bilinear decoupling constants can be controlled by the
linear decoupling constants:
Lemma 6.10. If 1 ≤ k ≤ n−1, δ = p−β ∈ p−N, and s,t ∈ [0,1] are such that βt,βtn−k+1 ∈ Z,
k
then
B n,k,n−k+1t,t (δ) ≤ D n (δ1−n− k k+1t)q k /qnD n (δ1−t)(qn−q k )/qn
k
Proof. Immediate from H¨older; see also thecalculation in the“Proof of Theorem1.2” in [5].
34

<!-- Page 35 -->

For k ≤ n and ω ∈ Z , write Vk(ω) = span {γ(1)(ω),...,γ(k)(ω)}. The following is
p Qn
p
superficially identical to an estimate in [5], but we emphasize that we are considering the p-adic
norm on both sides.
Lemma 6.11 (p-adic Vandermonde determinant). Under the assumption p > n, we have
|det[γ(1)(t),...,γ(k)(t),γ(1)(s),...,γ(n−k)(s)]| = |s−t|k(n−k) (6.3)
p p
Proof. We have, for 1 ≤ i ≤ n−k,
n
(cid:88) 1
γ(i)(s) = γ(j)(t)(t−s)j−i
(j −i)!
j=i

### Plugging in to the left-hand side of 6.3,

det[γ(1)(t),...,γ(k)(t),γ(1)(s),...,γ(n−k)(s)]
(cid:88) n (cid:89) −k (t−s)ja−a
= det[γ(1)(t),...,γ(k)(t),γ(j1)(t),...,γ(j n−k )(t)]
(j −a)!
a
j1,...,j
n−k
:n≥ja≥a a=1
Observe that the determinant summand vanishes when (j ,...,j ) is not a permutation of
1 n−k
(k + 1,...,n). On the other hand, when (j ,...,j ) is a permutation of (k + 1,...,n), we
1 n−k
see that
n−k
(cid:89)
(t−s)ja−a = (t−s)k(n−k)
a=1
so that
det[γ(1)(t),...,γ(k)(t),γ′(s),...,γ(n−k)(s)]
n−k
(cid:88) (cid:89) 1
= (t−s)k(n−k) sgn(j ,...,j ) .
1 n−k
(j −a)!
a
(j1,...,j
n−k
)∼(k+1,...,n) a=1
ja≥a
Here ∼ denotes permutation, and sgn denotes the sign of the implied permutation.
Finally, observe that
n−k
(cid:88) (cid:89) 1
det[γ(1)(0),...,γ(k)(0),γ(1)(1),...,γ(n−k)(1)] = sgn(j ,...,j )
1 n−k
(j −a)!
a
(j1,...,j
n−k
)∼(k+1,...,n) a=1
ja≥a
whereas the left-hand side may be computed (c.f. [6], display (14)) as
(cid:34) (cid:35)(cid:34) (cid:35)(cid:34) (cid:35)
n k n−k
(cid:89) 1 (cid:89) (cid:89)
j! j! (1−0)k(n−k)
j!
j=1 j=1 j=1
so that, since p > n,
|det[γ(1)(t),...,γ(k)(t),γ(1)(s),...,γ(n−k)(s)]| = |s−t|k(n−k)
p p
and we may conclude 6.3.
35

<!-- Page 36 -->

Before reaching the main estimate of the theorem, we demonstrate an equivalence between
the model decoupling constant D (δ) = Dγ(δ) and that of general convex curves. We first need
n n
a technical lemma:
Lemma 6.12 (Stability of linear decoupling constants). Let n ≥ 2. Suppose ζ : Z → Qn is
p p
Cn. Suppose δ,δ′ ∈ p−N are such that δ < δ′. Then we have the estimate
Dζ(δ) ≤ (δ′/δ)1/2Dζ(δ′).
n n
Proof. For any choice of functions {f } with f ˆ supported in Uζ, then we have

### I I∈P(Z p,δ) I I

(cid:13) (cid:13)  (cid:13) (cid:13)2 1/2
(cid:13) (cid:13) (cid:13) (cid:13)
(cid:13) (cid:88) (cid:13) (cid:88) (cid:13) (cid:88) (cid:13)
(cid:13) (cid:13) f I (cid:13) (cid:13) ≤ D n ζ(δ′) (cid:13) (cid:13) f I (cid:13) (cid:13)  ,
(cid:13)I∈P(Z p,δ) (cid:13)

### Lqn

J∈P(Z p,δ′)(cid:13)I∈P(J,δ) (cid:13)

### Lqn

and the desired estimate follows from the triangle inequality and Cauchy-Schwarz.
Proposition 6.13 (Decoupling for convex curves). Let k ≥ 2. Suppose ζ : Z → Qk is a
p p
Ck+1 curve that is convex and has bounded derivatives, in the sense that it satisfies 7.2 and

### For each δ ∈ p−N, write Dζ(δ) for the ℓ2Lq k decoupling constant associated to the partition

k
{Uζ} . Suppose D (ρ) ≤ C ρ−ε for all ε = 1,ℓ ∈ N, and ρ ∈ p−N. Then, for each

### I I∈P(Z p,δ) k k,ε ℓ

δ ∈ p−N and each ε = 4 with ℓ ∈ N, we have the estimate
ℓ
Dζ(δ) ≤ Eζ δ−ε,
k k,ε
where the constant Eζ may be taken as
k,ε
Eζ = C2k⌈log(4ε−1)⌉p(1+ε−1)k2k⌈log(8ε−1)⌉ ×max(1,c−1Ck−1∥ζ∥ ).
k,ε k,ε/4 Ck ◦ +1
Proof. This is essentially identical to the proof of Lemma 3.6 of [5]; we highlight the needed
modificationstoproducethep-adicanalogue. Fixε = 4 forsomeℓ ∈ N,andwriteZ = k2k⌈log2ℓ⌉.
ℓ
Write α = max(1,c−1Ck−1∥ζ∥ ), where c,C are the constants from 7.2 and 7.3. Write r ∈ N
Ck+1
◦
for the smallest integer such that α ≤ prZ. Choose any δ ∈ p−ℓZN such that δ−ε/2 > prZ. Fix
κ = δεprZ, so that κ < α−1 and κ < δε/2. Furthermore, writing
(cid:24) log(4ε−1) (cid:25)
m = ≤ 2k⌈log(4ε−1)⌉,
∗ log(1+k−1)
we see that, for each 1 ≤ m ≤ m , we have
∗
κ(k+1)m
∈
p−N
,
k
and we have the inequalities
κ(k+
k
1)m∗−1
≤ δk+
k
1 < κ.
With these parameters chosen, suppose I ∈ P(Z ,κ), and {f } are such that f
p I′ k+1 I′

### I′∈P(I,κ k )

has Fourier support in Uζ. If c ∈ I, then for any other ξ ∈ I we may write

## I′ I

(cid:88) k ζ(j)(c )
ζ (ξ) = ζ (c )+ i I (ξ −c )j +(c −ξ)k+1Λi (c ,ξ)
i i I k! I I k+1 I
j=1
36

<!-- Page 37 -->

where Λi is continuous and vanishes along the diagonal. Write A = Aζ . By Lemma 7.2,
k+1 I cI
A−1 has ≤ c−1Ck−1 operator norm. Then the curve

## I

η(ξ) = A−1(ζ(ξ +c )−ζ(c ))

## I I I

satisfies
ξi
η (ξ) = +ξk+1Λi (c ,ξ),
i i! k+1 I
and
∥η∥ ≤ c−1Ck−1∥ζ∥ .
Ck+1 Ck+1
◦ ◦
By Lemma 7.1(c), it further holds that
j+1
ξi−j (cid:88)
η(j)(ξ) = δ +ξ Φ η (0,...,0,ξ,...,ξ),
i (i−j)! i≥j j+1 i
ι=1
where Φ is defined in Appendix C, and there are ι-many 0’s. By the affine invariance of
j+1
decoupling constants,
D ({Uζ} ) = D ({Uη } )
k I′
I′∈P(I,κ
k+
k
1
)
k I′−cI
I′∈P(I,κ
k+
k
1
)
We claim that the boxes Uη and Uγ are comparable. Indeed, if x ∈ Uη , then there are

### I′−cI I′−cI I′−cI

{λ }n ∈ (cid:81)k B(0,κjk+1) and ξ ∈ I′ −c ⊆ B (0) such that
j j=1 j=1 k I′−cI I κ
k
(cid:88)
x = η(ξ )+ η(j)(ξ )λ ,
I′−cI I′−cI j
j=1
so that
k
(cid:88)
x = γ (ξ )+ γ(j)(ξ )λ +E,
i i I′−cI i I′−cI j
j=1
where|E| ≤ c−1Ck−1∥ζ∥ κ2+1,i.e. Uη iscontainedinac−1Ck−1∥ζ∥ κ2+1-neighborhood
p Ck
◦
+1 k I′−cI Ck
◦
+1 k
of Uγ . Since the family {Uγ } are κk+1-separated, we obtain
I′−cI I′−cI
I′∈P(I,κ
k+
k
1
)
k
(cid:16) (cid:17) (cid:16) (cid:17)
Dec {Uη } ≤ Dec {Uγ } ,
ℓ2Lqk I′−cI
I′∈P(I,κ
k+
k
1
)
ℓ2Lqk I′−cI
I′∈P(I,κ
k+
k
1
)
because c−1Ck−1∥ζ∥ < κ−1, so that (using the affine invariance to compare ζ to η, and the
Ck+1
◦
affine rescaling of ζ),
(cid:16) (cid:17) (cid:16) (cid:17)
Dec {Uζ} ≤ Dec {Uγ} .
ℓ2Lqk I′
I′∈P(I,κ
k+
k
1
)
ℓ2Lqk I′
I′∈P(I,κ
k+
k
1
)
On the other hand, affine rescaling implies
(cid:16) (cid:17)
Dec {Uγ} ≤ D (κ1/k),
ℓ2Lqk I′
I′∈P(I,κ
k+
k
1
)
k
37

<!-- Page 38 -->

so that
(cid:16) (cid:17)
Dec {Uζ} ≤ D (κ1/k).
ℓ2Lqk I′
I′∈P(I,κ
k+
k
1
)
k
We have established this whenever κ > δk+ k 1 and I ∈ P(Z p ,κ). If we iterate this m-many
times, where κ(k+
k
1)m > δk+ k 1, we obtain
m
(cid:16) (cid:17) (cid:89)
Dec {Uζ} ≤ D (κ(k+1)j−1/k).
ℓ2Lqk I′ I′∈P(I,κmk+
k
1
)
k k
j=1
Observe that #P(Z ,κ) ≤ κ−1, so by flat decoupling we have
p
(cid:16) (cid:17)

### Dec

ℓ2Lqk

## {U


## I

ζ}
I∈P(Z p,κ)
≤ κq 1
k
−1 2.
If κ(k+ k 1)m+1 ≤ δk+ k 1 as well, then for each I′ ∈ P(Z p ,κ(k+ k 1)m) we have
(cid:16) (cid:17)
Dec ℓ2Lqk {U J ζ} J∈P(I,δ) ≤ (δκ−(k+ k 1)m) 1 2 − q 1 k ≤ (κ−(k+ k 1)2) 1 2 − q 1 k .
Finally, from the hypothesis that D (ρ) ≤ C ρ−ε for all ε > 0 and all ρ ∈ p−N, we obtain
k k,ε
D k ζ(δ) ≤ C k m ,ε/4 κ (−(k+ k 1)2−1)(1 2 − q 1 k )− 4 ε[(k+ k 1)m−1] .
Observe that m < m . Recalling that κ > α−1p−Zδε, we conclude
∗
Dζ(δ) ≤ C2k⌈log(4ε−1)⌉p2k2k⌈log(4ε−1)⌉ ×max(1,c−1Ck−1∥ζ∥ )×δ−ε.
k k,ε/4 Ck ◦ +1
It remains to remove the special assumptions on the value of δ. Take ε = 4 for some ℓ ∈ N.
ℓ
Suppose first that δ ∈ p−N is such that δ > p−ε−1Zα−1, where α is as above. Then we may
trivially bound
Dζ(δ) ≤ δ−1δ−ε,
k
and
δ−1 ≤
pε−1k2k⌈log(4ε−1)⌉max(1,c−1Ck−1∥ζ∥
).
Ck+1)
◦
We are done in this case, thanks to C ≥ 1. Suppose instead that δ ∈ p−N satisfies the
k,ε
inequalities
p−ℓk2k⌈log2ℓ⌉(K+1) < δ < p−ℓk2k⌈log2ℓ⌉K, K ∈ N.
Comparing Dζ(δ) to Dζ(δ′), where δ′ = p−ℓk2k⌈log2ℓ⌉K, we obtain the estimate
k k
Dζ(δ) ≤ C2k⌈log(4ε−1)⌉p(1+ε−1)k2k⌈log(8ε−1)⌉ ×max(1,c−1Ck−1∥ζ∥ )×δ−ε.
k k,ε/4 Ck ◦ +1
38

<!-- Page 39 -->

6.2 Lower dimensional estimates
We next establish the induction-on-dimension estimates in the p-adic setting. This is the
componentoftheargumentthatrequiresthemostcarefulrewriting; thecorestepsforinducting
on dimension are essentially the same, but are usually phrased essentially in the language of
Euclidean geometry. We choose instead to phrase things via matrix algebra, and the difficulties
disappear.
A critical input of these estimates in the Euclidean setting is the Fourier slicing theorem,
which requires some slight rewording in our setting; the dot product · : Qn × Qn → Q is
p p p
isotropic for every n ≥ 3 and odd p (see the start of this section of the appendix). A near
relative is available, which we produce now.
Lemma 6.14 (p-adic Fourier slicing). Suppose that f : Qn has Fourier support inside of
p
Ω ⊆ Qn. Let H ⊆ Qn be a k-dimensional linear subspace, B : Qk → Qn a linear isomorphism
p p p p
onto H, and z ∈ Qn arbitrary. Write fz for the function H → C, fz(x) = f(x + z). Then
p
fz ◦B has Fourier support in the set B⊤Ω.
Proof. By extension of bases, we may write B = B′ ◦ ι where ι : Qk (cid:44)→ Qn is the inclusion
p p
into the first k coordinates and B′ : Qn → Qn is a linear isomorphism. By the usual change-ofp p
variable,
f (cid:92) ◦B′ = |detB′|−1 ·f ˆ ◦(B′)−⊤.
p
It follows that we may assume that H is the subspace {x = ... = x = 0}, for which
k+1 n
H⊥ = {x = ... = x = 0}. Then, for y ∈ H and z ∈ H⊥,
1 k
ˆ
fz(y) = χ((y +z)·ξ)f ˆ (ξ)dξ
ˆ ˆ
= χ(y ·ξ′) χ(z ·ξ′′)f ˆ (ξ′,ξ′′)dξ′′dξ′.

## H H⊥

It follows that f(cid:98)z is supported in the set {ξ′ ∈ H : ∃ξ′′ s.t. ξ′ +ξ′′ ∈ Ω}. The result follows.
We apply this to decouple functions using lower-dimensional estimates.
Lemma 6.15. Let k < n and assume that D (δ) ≤ C δ−ε for all ε = 1,ℓ ∈ N, and δ ∈ p−N.
k k,ε ℓ
Let δ = δ−β ∈ p−N and {f } have Fourier support in {U } . If 0 ≤ s,t ≤ 1 satisfy

### I I∈P(Z p,δ) I I∈P(Z p,δ)

0 ≤ s ≤ (n−k+1)t/k andsβ,tβ,tβ(n−k+1)/k ∈ Z, thenforanyJ ∈ P(Z ,δs),J ∈ P(Z ,δt)
1 p 2 p
in distinct cosets of pZ , and for any ε = 4 with ℓ ∈ N , we have
p ℓ ≥4
ˆ
|f |q k|f |qn−q k ≤ C2kq k ⌈log(4ε−1)⌉p(1+ε−1)k2k⌈log(8ε−1)⌉+2

### J1 J2 k,ε/4

 (cid:32) ˆ (cid:33)2/q q k /2 (6.4)
k
×δ−q k [(n−k k +1)t−s]ε  (cid:88) |f J |q k|f J2 |qn−q k  .

### Qn


### J∈P(J1,δ(n−k+1)t/k) p

Proof. Pick any ω ∈ J and write V = span(γ(1)(ω),...,γ(n−k)(ω)). Let H = V⊥ be the orthog-
2
onal space to V in Qn; observe that dimH = k, since the dot product is still nondegenerate.
p
Set t′ = (n−k +1)t/k.
39

<!-- Page 40 -->


### Define

(cid:20) (cid:21)
0

## B = A⊤ ;

−ω I
k
it follows that B defines a linear isomorphism Qk → H. Write µ = B µ .
p H ∗ Qk p
We use Lemma 6.14 to estimate integrals of f along H +z. Let B be a linear isomorphism
Qk → H. Observe that fz ◦B has Fourier support in UB⊤γ. By Fubini,
p J1 J1
ˆ ˆ
|f

## J1

|q k|f

## J2

|qn−q kdµ = |f

## J1

|q k(x)|f

## J2

|qn−q k(x)dµ

## H

(x)dµ
Qn
p
(z)
Qn
p
z∈Qn
p
x∈BH(z,δ−t′k)
Note B (z,δ−t′k) = B (z,δ−(n−k+1)t). Write A for the matrix with j’th column γ(j)(ω), 1 ≤

## H H

j ≤ n. By uncertainty, f is constant on translates of the set

## J2

U∗ = A−⊤ ·diag (cid:0) δt,...,δnt (cid:1) [Zn]

### J2 ω p

If y ∈ B (0,δ−t′k), then

## H

 0 
.
 . . 
 
diag (cid:0) δ−t,...,δ−nt (cid:1) (A⊤y) =   0   ∈ Zn,
ω δ−(n−k+1)tγ(n−k+1)(ω)·y p
 
 . . 
 . 
δ−ntγ(n)(ω)·y
(cid:12) (cid:12)
since (cid:12)δ−rtγ(r)(ω)·y(cid:12) ≤ δrt−(n−k+1)t ≤ 1 for each r ≥ n − k + 1. Consequently, we have
p
B (0,δ−t′k) ⊆ U∗ , and so by uncertainty we have that |f |qn−q k is constant on B (z,δ−t′ℓ).

## H J2 J2 H

Thus
ˆ
|f |q k(x)|f |qn−q k(x)

## J1 J2

z∈Qn
p
x∈ˆBH(z,δ−t′k)
= |f |qn−q k(z) |f |q k(x)

## J2 J1

z∈Qn
p
x∈BH(z,δ−t′k)
Then
ˆ ˆ
|f (x)|q kdµ (x) = |fz (x)|q kdµ
x∈BH(z,δ−t′ℓ)

## J1 H

ˆx∈BH(0,δ−t′ℓ)

## J1 H

=
y∈B−1[BH(0,δ−t′ℓ)]
|f

## J

z
1
(B(y))|q
p
kdµ
Qk p
(y),
where we have used that B µ = µ . By Lemma 6.14, for each J ∈ P(J ,δt′), the function
∗ Qk H 1
p
f ◦B is supported in the set UB⊤γ. By Lemma 6.3, the curve B⊤γ : Z → Qk satisfies

### J J p p

max max sup|B⊤γ(r)(θ)| ≤ 1
j p
1≤j≤k1≤r≤kθ∈J1
40

<!-- Page 41 -->

and
inf |det[B⊤γ(1)(θ),...,B⊤γ(k)(θ)]| ≥ 1.
p
θ∈J1
By Lemma 5.4, Prop. 6.13, and the inductive assumption,
ˆ
|f |q k(x) ≤ C2kq k ⌈log(4ε−1)⌉p(1+ε−1)k2k⌈log(8ε−1)⌉+2

### J1 k,ε/4

x∈BH(z,δ−t′k)
 q /2
k
(cid:88)
×(#P(J 1 ,δt′))q k ε  ∥f J ∥2 Lqk(BH(z′,δ−b′k))  .

### J∈P(J1,δt′)

Consequently,
ˆ
|f |q k|f |qn−q k ≤C2kq k ⌈log(4ε−1)⌉p(1+ε−1)k2k⌈log(8ε−1)⌉+2δtk(n−k+1)−q k ε(t′−s)
J1 J2 k,ε/4
Qn
p
ˆ  q /2
k
×
z∈Qn
p
|f J2 | 2
qn
q
−
k
qk
(z)

## J∈P

(cid:88)
(J1,δt′)
∥f J ∥2 Lqk(BH(z,δ−t′k))  ,
which by Minkowski is bounded by
C2kq
k
⌈log(4ε−1)⌉p(1+ε−1)k2k⌈log(8ε−1)⌉+2δtk(n−k+1)−q
k
ε(t′−s)
k,ε/4
 (cid:32) ˆ (cid:33)2/q q k /2
k
(cid:88)
×
J∈P(J1,δt′)
z∈Qn
p
|f J2 |qn−q k(z)∥f J ∥q L k qk(BH(z,δ−t′k))  .
Finally,
ˆ ˆ ˆ
|f |qn−q k(z)∥f ∥q k = |f (z)|qn−q k |f (x)|q k
z∈Qn
p
J2 J Lqk(BH(z,δ−t′k))
z∈Qn
p

## J2

ˆ
x∈BH(z,δ−t′k)

## J

= δ−t(n−k+1)k |f (z)|qn−q k|f (z)|q k,

## J2 J

z∈Qn
p
by virtue of local constancy; hence we have shown
ˆ
|f |q k|f |qn−q k ≤ C2kq k ⌈log(4ε−1)⌉p(1+ε−1)k2k⌈log(8ε−1)⌉+2

### J1 J2 k,ε/4

 (cid:32) ˆ (cid:33)2/q q k /2
k
(cid:88)
×δ−q k ε(t′−s)  |f J |q k|f J2 |qn−q k  ,

### Qn


### J∈P(J1,δ(n−k+1)t/k) p

as was to be verified.
Corollary 6.16. If k < n and D (δ) ≤ C δ−ε for all ε = 1,ℓ ∈ N, then for any δ,s,t satisfying
k k,ε ℓ
the hypotheses of Lemma 6.15,
B n,k,s,t (δ) ≤ C k 2 , k ε q / k 4 qn −1⌈log(4ε−1)⌉p(1+ε−1)qn −1k2k⌈log(8ε−1)⌉+2δ− q q n k[(n−k k +1)t−s]εB n,k,n−k+1t,t (δ).
k
41

<!-- Page 42 -->

We record another application of Ho¨lder; here we are able to go without an application of
the uncertainty principle.
Lemma 6.17. If 1 ≤ k ≤ n−1, and if δ ∈ (0,1) and s,t ∈ (0,1) are as above, then
1 n−k

## B

n,k,s,t
(δ) ≤ B
n,n−k,t,s
(δ)n−k+1B
n,k−1,s,t
(δ)n−k+1.
Proof. Let {f } ,{g } be families as in Def. 6.8. Then, writing θ = 1/(n−k+1), we see that
i i i i k
ˆ ˆ
(cid:88) (cid:88) (cid:88) (cid:88) (cid:88) (cid:88)
| f |q k| g |qn−q k = | f |θ k (qn−q n−k )| f |(1−θ k )q k−1| g |θ k q n−k| g |(1−θ k )(qn−q k−1 )
i j i i i i

### Qn Qn

p i i p i i i i
ˆ ˆ
(cid:32) (cid:33)θ (cid:32) (cid:33)1−θ
k k
(cid:88) (cid:88) (cid:88) (cid:88)
≤ | f |qn−q n−k| g |q n−k | f |q k−1| g |qn−q k−1
i i i i

### Qn Qn

p i i p i i
from which the result is clear.

### The following consequence is identical to Lemma 4.2 of [5]:

Lemma 6.18. Suppose D (δ) ≤ C δ−ε for all 1 ≤ k ≤ n − 1 and all δ,ε > 0. Suppose
k k,ε
1 ≤ k ≤ n−1andletε = 4 forsomeℓ ∈ N . Then,foreveryt ∈ [0,1]suchthatt ≤ k(n−k)
ℓ ≥4 (k+1)(n−k+1)
and either k = 1 or t ≤ k−1 , we have, for each δ ∈ p−N for which δt,δn−k+1t ∈ p−N,
k
n−k+2
B n,k,n−k+1t,t (δ) ≤ p8ε−4nlognC n 2⌈ − lo k g ,ε ( / 4 4 ε−1)⌉C k 2 − k⌈ 1 l , o ε g / ( 4 4ε−1)⌉δ−n− n kk− ( 1 k + + (k 1) + (n 1) − (n k − + k 1) +1)tε
k
1 n−k

## ×B

n,n−k,k+1n−k+1t,n−k+1t
(δ)n−k+1B
n,k−1,n−k+2t,t
(δ)n−k+1.
k n−k k k−1

### We also record the following:

Lemma 6.19. For any δ ∈ p−N and any s,t such that B (δ) is defined,
n,0,s,t
B (δ) = D (δ1−t).
n,0,s,t n
Proof. For any particular tuples {f } ,{g } , the inequality in Def. 6.8 is just the linear decoui i i i
pling inequality for the tuple {g } . The result follows by parabolic rescaling.
i i
6.3 Induction on scales
InthissectionwerunaninductiononscalesargumentinordertoproveTheorem6.1. Wemirror
the arguments in Section 4 of [5]; however, in order to verify the appropriate quantitative
estimate, we produce a modified version. The former runs an analysis on the tropicalized
quantities η,{A } , defined as the optimal exponents on various decoupling constants; the
k k
resulting analysis is clean, but does not admit estimates on the corresponding constants. We
run a suitable finitary version of this argument, which gives somewhat loose (but explicit)
estimates on the constant.
For the reader’s convenience, we state in our current notation the statement we will prove.
42

<!-- Page 43 -->

Theorem 6.20 (Moment curve decoupling). For each ε > 0 and n ∈ N, there is a constant
C such that
n,ε
D (δ) ≤ C δ−ε,
n n,ε
for all δ ∈ p−N. Moreover, the constant C may be taken to be
n,ε
(cid:16) (cid:17)
C = exp 104(logp)ε−4nlognn10n2 .
n,ε
Proof of Theorem 6.20. By induction, we will establish

### We will instead prove the stronger inequality

D (δ) ≤ exp(104(logp)(ε/48n)−4nlogn(48n)n2n4+5n)δ−ε,
n
for each ε = 1 for some ℓ ∈ N. We have spelled out a constant in a useful inductive form; after
ℓ
proving this for all n, we will go back and prove the original statement.
We argue by induction on n. The case n = 1 is trivial, so we assume that n ≥ 2 and the
estimate holds for all D , k = 1,...,n−1. First take ε = (48n)−n2ℓ, for some ℓ ∈ N; we will
k
later remove this assumption. For each H ∈ N, we write
(cid:40) (cid:41)

## H

a (cid:89)
T H = ∈ (0,1)∩Q : a ∈ Z,b = k for some (k ,...,k ) ∈ [n]H
j 1 H
b
j=1
for the rational numbers t of “depth” ≤ H. We writeN =
⌊5(n−1)2
⌋, which will control the
nlogn
number of steps in our analysis. We will assume that δ ∈ p−(n!)NN and δ < n−3000n4ε−1. We
write
logD (δ)
ηδ = n ,
log(δ−1)
and, when 0 ≤ k ≤ n−1 and t ∈ T N,
log(B (δ))
Aδ(t) =
n,k,n−
k
k+1t,t
.
k log(δ−1)
By Lemma 6.19, we have Aδ(t) = (1−t)ηδ1−t. We adopt the abbreviation
0
8(logp)(ε/48n)−4nlogn (cid:16) (cid:17)
q (δ) = 1+2500n⌈log((48n)2ε−1)⌉(ε/48n)4logn(48n)n2n4+n ,
ε log(δ−1)
a quantity controlling the logarithm of the prefactors in Lemma 6.18 for each 1 ≤ k ≤ n−1,
divided by log(δ−1), using the inductive hypothesis. It will be important that, for every n ≥ 2
and our choice of ε, the second factor is ≤ 2.
By Lemma 6.18, selecting ε for the statement’s ε, and the inductive hypothesis, for each
12n
1 ≤ k ≤ n−1, and for each t ∈ T N−1 with t ≤ k(n−k) , and either k = 1 or t ≤ k−1 ,
(k+1)(n−k+1) n−k+2
(cid:18) (cid:19)
1 n−k +1 n−k tε
Aδ(t) ≤ Aδ t + Aδ (t)+ +q (δ).
k n−k +1 n−k k n−k +1 k−1 6n ε
43

<!-- Page 44 -->

We write, for 0 ≤ k ≤ n−1,
ηδ −Aδ(t)
aδ(t) = k , t ∈ T N,
k t
so that
(cid:18) (cid:19)
1 n−k +1 n−k ε q (δ)
aδ(t) ≥ aδ t + aδ (t)− − ε , t ∈ T N−1.
k k n−k k n−k +1 k−1 6n t
We note as well the trivial bounds
1
0 ≤ aδ(t) ≤ ,
k 2tlogδ−1
arising from the triangle inequality, Cauchy-Schwartz, and the fact that decoupling constants
are at least 1. Note that aδ(t) = ηδ1−t. We write aδ(t) for the (n−1)×1 row vector composed
0
of the aδ(t). Define M to be the (n−1)×(n−1) matrix
k

 n−j i = j +1 ̸= n−j
 n−j+1

1 i = n−j ̸= j +1
M = i .
i,j
1 i = n−j = j +1




0 otherwise
Trivially, for each choice 0 < ρ < c < 1 and each 0 ≤ ι ≤ N −1,
2n
min aδ(t) ≤ min aδ(t).
k k
t∈Tι+1∩(1ρ,nc) t∈Tι∩(ρ,c)
n
Let c = 10−2n−2. Observe that c satisfies the inequality
0 0
60(n−1)2ε−1 1 1
n c0logδ−1c
0
< .
2n
It follows that, for some 0 ≤ ι ≤ N, the numbers ρ = n−ιc ,c = nιc satisfy
0 0
ε
min aδ(t) > − + min aδ(t), ∀1 ≤ k ≤ n−1,
t∈Tι+1(1ρ,nc) k 12n t∈Tι∩(ρ,c) k
n
and
1
c < .
2n

### Define, for each 0 ≤ k ≤ n−1,

mδ = min aδ(t), m˜δ = min aδ(t).
k k k k
t∈Tι∩(ρ,c) t∈Tι+1∩(1ρ,nc)
n
We see that the vectors (mδ)n−1 satisfy
k k=1
ε
m˜δ ≥ mδ − 1
12n
44

<!-- Page 45 -->

and
(cid:110) ε (cid:111)
mδ ≥ m˜δ.M − +ρ−1q (δ) 1.
ε
6n
Combining, and taking a matrix multiplication on the right with the column vector 1⊤, we
obtain
n−1 n−1
(cid:88) (cid:88) n−1 ε ρ
m˜δ ≥ m˜δ + ηδ1−t − −nρ−1q (δ), for some t ∈ T N ∩( ,cn),
k k n 4 ε n
k=1 k=1
which may be written as
ε 1
ηδα ≤ +2nρ−1q (δ), for some α ∈ T N ∩( ,1).
ε
2 2

### It follows from a short calculation that

D (δ) ≤ exp(6400(logp)(ε/48n)−4nlognn4+5n)δ−ε.
n
It remains to remove the special size and arithmetic assumptions on δ and ε. We have shown
the estimate for all δ ∈ p−(n!)NN with δ < n−3000n4ε−1. Suppose instead that K ∈ N is such that
p−(n!)N(K+1) < δ < p−(n!)NK.
Then, by stability of D , Lemma 6.12 with δ′ = p−(n!)NK, we obtain the bound
n
D (δ) ≤ p(n!)N exp(6400(logp)(ε/48n)−4nlognn4+5n)δ−ε.
n
But since ε ≤ (48n)−n2, it is quick to see via Stirling that
p(n!)N exp(6400(logp)(ε/48n)−4nlognn4+5n) ≤ exp(7000(logp)(ε/48n)−4nlognn4+5n).
We have proven the bound for all δ ∈ p−N with δ < min(p−(n!)N,n−3000n4ε−1). By a trivial
estimate, the same holds for all δ ∈ p−N.
Thus we are done in the case ε = (48n)−n2ℓ for some ℓ ∈ N. Suppose instead ε = 1 for some
ℓ
ℓ ∈ N. We have two cases. In the first case, there is ℓ′ ∈ N so that
(48n)−n2(ℓ′+1) ≤ ε ≤ (48n)−n2ℓ′

### Then we conclude, for each δ ∈ p−N,

D (δ) ≤ exp(7000(logp)(ε/48n)−4nlogn(48n)n2n4+5n)δ−ε,
n
which fits in the estimate we wished to conclude. In the second case, we have ε > (48n)−n2,
and again a trivial estimate suffices.
Remark 6.21. One may compare the above analysis with the problem of bounding a constant
quantity η, given that it relates to a system as
(cid:40)
q(t) ∈ [0, C ], 0 ≤ t ≤ T,

### T−t

q˙ ≤ −η +O( ε ).
T−t
45

<!-- Page 46 -->

We conclude by recording the following standard corollary.
Corollary 6.22. Suppose ζ : Z → Qn is a Cn+1-curve that is convex and has bounded
p p
derivatives, as defined in section 7. Then
Dec ({Uζ} ) ≲ δ−ε ∀ε > 0,δ ∈ p−N .
ℓ2Lqn I I∈P(Z p,δ) γ,ε
Proof. Follows from Thm. 6.1 and Prop. 6.13.
Remark 6.23. If we consider the alternate set-family {U′} , defined by

### I I∈P(Z p,δ)

U′ = (cid:8) x ∈ Qn : |x −γ (θ)| ≤ δj∀1 ≤ j ≤ n (cid:9) , (θ ∈ I),
I,θ p j j p
and
(cid:91)

## U′ = U′ ,

I I,θ
θ∈I
then, for any δ ∈ p−nN, J ∈ P(Z ,δ) and I ∈ P(Z ,δ1/n) with J ⊆ I, it holds that
p p

## U′ ⊆ U .


## J I

Consequently, we have the decoupling estimate
 
(cid:110) (cid:91) (cid:111)
Dec ℓ2Ln(n+1) U J ′  ≤ C n,nε δε,
I∈P(Z p,δ1/n)

### J∈P(I,δ)

for each ε and δ.
7 Appendix C: Curves in
Qn
p
We take as a reference [12].
The curves ζ : Z → Qn under consideration will be assumed to be Ck, for various k ∈
p p
N∪{∞}; as such, we recall some of the basics of ultrametric calculus. Consider an arbitrary
function f : Z → Q . If k ∈ N and a ,...,a ∈ Z are distinct, we write Φ for the Newton
p p 1 k+1 p k
quotient
k+1
(cid:88) f(a )
j
Φ f(a ,...,a ) = .
k 1 k+1 (cid:81)
(a −a )
j=1 i̸=j j i
We will also write Φ f = f. A function f is said to be Ck if, for every 0 ≤ j ≤ k, the function
0
Φ f extends to a continuous function Φ : Zk+1 → Q . f is said to be C∞ if f ∈ Ck for every
j j p p
k. This definition is extended to curves ζ : Z → Qn in the obvious way.
p p
The following summarizes the basic facts about the mappings Φ that we will need.
k
Proposition 7.1. Let f : Z → Q be a Cn function. Then each of the following holds.
p p
(a) If f is Cn, then for each 1 ≤ k ≤ n and a ∈ Z , we have
p
f(k)(a) = Φ f(a,...,a),
k
where f(k)(a) is the usual kth derivative of f at a.
46

<!-- Page 47 -->

(b) f admits Taylor expansions
(cid:88) n f(j)(y)
f(x) = f(y)+ (x−y)j +(x−y)nΛ (x,y) ∀x,y ∈ Z , (7.1)
n+1 p
j!
j=1
where the remainder term Λ (x,y) is of the form
n+1
Λ (x,y) = Φ f(x,y,y,...,y)−f(n)(y).
n+1 n
(c) For any elements x ,...,x ,y ,...,y ∈ Z , we have
1 k+1 1 k+1 p
k+1
(cid:88)
Φ f(x ,...,x )−Φ f(y ,...,y ) = (x −y )Φ (x ,...,x ,y ,...,y ).
k 1 k+1 k 1 k+1 j j k+1 1 j j k+1
j=1
Proof. Taken from [12]; (a) is Theorem 29.5, (b) is Theorem 29.4, and (c) is Lemma 29.2(iii).
Note that our definition of Φ is equivalent to that of [12], by the latter’s Exercise 29.A.
We define the Ck norm of a Ck function f by
∥f∥ = max sup |Φ f(x)| .

### Ck k p

0≤j≤k x∈Zj
p
+1
We similarly define the Ck seminorm of a Ck function f by
∥f∥ = max sup |Φ f(x)| .

### Ck k p

◦ 1≤j≤k x∈Zj
p
+1
If ζ : Z → Qn is a Ck curve, then we write
p p
∥ζ∥ = max ∥ζ ∥ , ∥ζ∥ = max ∥ζ ∥
Ck i Ck Ck i Ck
1≤i≤k ◦ 1≤i≤k ◦
In particular, |ζ(j)(x)| ≤ ∥ζ∥ for each 1 ≤ i ≤ n and 0 ≤ j ≤ k. We note in passing that,
i p Ck
for any linear transformation B of Qn, we have the bound
p
∥Bζ∥ ≤ ∥B∥·∥ζ∥ .

### Ck Ck

We also note that our definition of ∥·∥ is strictly stronger than the simpler quantity

### Ck

∥f∥⋆ = max sup |f(k)(x)| .

### Ck p

0≤k≤nx∈Z
p
Indeed, if f = 1 is the indicator of the ball of radius p−N, then f ∈ C∞ and

### B(0,p−N)

sup |f(x)| = 1, max sup |f(k)(x)| = 0.
p p
x∈Z
p
j∈N x∈Z
p
On the other hand,
(cid:12) (cid:12)
(cid:12)f(pN−1)−f(0)(cid:12)
(cid:12) (cid:12) = pN−1,
(cid:12) pN−1 −0 (cid:12)
p
47

<!-- Page 48 -->

so ∥f∥ ≥ pN−1. It follows that ∥f∥ ≥ pN−1∥f∥⋆ , for each k ≥ 1; thus, ∥·∥ defines a

### C1 Ck Ck Ck

strictly finer topology on C∞ than ∥·∥⋆ .

### Ck

We will want our curves ζ to be convex and of bounded derivatives; the former condition
amounts to
(cid:12) (cid:12)
inf (cid:12)det[ζ(1)(t),...,ζ(n)(t)](cid:12) ≥ c, (7.2)
t∈Z
p
p
and the latter condition is that
max sup (cid:12) (cid:12)ζ(j)(t) (cid:12) (cid:12) ≤ C. (7.3)
1≤i,j≤nt∈Z
p
i p
for various choices c ≳ 1,C ≲ 1; we name these bounds so as to track quantitative dependence
in the sequel.

### As an immediate consequence, we have:

Lemma 7.2. Suppose ζ : Z → Qn is Cn. Suppose further that ζ satisfies 7.2 and 7.3. Then,
p p
for each t ∈ Z , one has
p
∥[ζ(1)(t),...,ζ(n)(t)]−1∥ ≤ c−1Cn−1.
and
∥[ζ(1)(t),...,ζ(n)(t)]∥ ≤ Cn
Here ∥·∥ is operator norm with respect to the max-norm on Qn.
p
Proof. We only verify the first estimate; the second will follow by identical arrangements. The
matrix norm is given by
(cid:12) (cid:12)
(cid:12)(cid:88) n
(cid:0) (cid:1)
(cid:12)
max max (cid:12) [ζ(1)(t),...,ζ(n)(t)]−1 u (cid:12)
1≤j≤nu1,...,un∈Z
p
(cid:12)
(cid:12)
j,k k(cid:12)
(cid:12)
k=1 p
(cid:12) (cid:12)
(cid:0) (cid:1)
= max max max (cid:12) [ζ(1)(t),...,ζ(n)(t)]−1 u (cid:12)
1≤j≤nu1,...,un∈Z p1≤k≤n (cid:12) j,k k(cid:12) p
(cid:12) (cid:12)
(cid:0) (cid:1)
= max (cid:12) [ζ(1)(t),...,ζ(n)(t)]−1 (cid:12)
1≤j,k≤n
(cid:12) j,k(cid:12)
p
By the cofactor form of matrix inverses, for each 1 ≤ j,k ≤ n,
(cid:12) (cid:12)
(cid:0) (cid:1)
(cid:12) [ζ(1)(t),...,ζ(n)(t)]−1 (cid:12) = |det[ζ(1)(t),...,ζ(n)(t)]|−1|C |
(cid:12) j,k(cid:12) p k,j p
p
where C is the (k,j)-cofactor. To estimate the latter, we simply use the (ultrametric) triangle
k,j
inequality via
|C | ≤ max |ζ(j)(t)|n−1
k,j p i p
1≤i,j≤n
Remark 7.3. When ζ = γ is the moment curve t (cid:55)→ (t,..., tn) in Qn, the constants in 7.2 and
n! p
7.3 are c = C = 1.
48

<!-- Page 49 -->

Next, we consider the local comparison between curves ζ that are convex and with bounded
derivatives to the model curve γ(t) = (t,..., tn). Recall the notation
n!
Aζ = [ζ(1)(θ),...,ζ(n)(θ)]·diag(λ,...,λn)
θ,λ
If ζ is suppressed, then we understand A to refer to the matrix Aγ. For fixed θ ∈ Z and
t t p
λ ∈ pZ , define ζ to be the rescaled curve
p θ,λ
ζ (t) = [Aζ ]−1(ζ(θ+λt)−ζ(θ))
θ,λ θ,λ
The rescaling is motivated by the fact that the degree n Taylor approximation of the function
t (cid:55)→ ζ(θ+λt) near t = 0 is
ζ(θ+λt) ≈ ζ(θ)+Aζ ·γ(t), (|t| ≪ 1)
θ,λ p
Of course, if ζ is a polynomial of degree ≤ n, the Taylor approximation is an identity. In
particular, for such a ζ, ζ = γ is our moment curve; a trivial observation is the special case
θ,λ
γ = γ for each θ,λ.
θ,λ

### Note in particular the identity

Φ (ζ ) (a ,...,a ) = λkΦ ζ (c+λa ,...,c+λa ), k ≥ 1,
k λ,θ i 1 k+1 k i 1 k+1
which implies the scaling relations
∥ζ ∥ ≤ ∥ζ∥ , k ≥ 1,λ ∈ pZ ,
λ,θ Ck(λZ p) Ck p
∥ζ ∥ ≤ |λ|−1∥ζ∥ , k ≥ 1,λ ∈ pZ .
λ,θ Ck ◦ (λZ p) p Ck ◦ p

### References

[1] J.W.S Cassels. Rational Quadratic Forms. Academic Press Inc. (London) Ltd., 1978.
[2] C. Cornut and V. Vatsal. “CM points and quaternion algebras”. In: Doc. Math. 10 (2005),
pp. 263–309. issn: 1431-0635,1431-0643.
[3] Christophe Cornut. “Mazur’s conjecture on higher Heegner points”. In: Invent. Math.
148.3 (2002), pp. 495–523. issn: 0020-9910,1432-1297. doi: 10.1007/s002220100199.
url: https://doi.org/10.1007/s002220100199.
[4] Shengwen Gan, Shaoming Guo, and Hong Wang. “A restricted projection problem for
fractal sets in Rn”. In: arXiv preprint arXiv:2211.09508 (2022).
[5] Shaoming Guo et al. “A short proof of ℓ2 decoupling for the moment curve”. In: American
Journal of Mathematics 143.6 (2021), pp. 1983–1998.
[6] Dan Kalman. “The generalized Vandermonde matrix”. In: Mathematics Magazine 57.1
(1984), pp. 15–21.
[7] Zane Kun Li. “An introduction to decoupling and harmonic analysis over Q ”. In: arXiv
p
preprint arXiv:2209.01644 (2022).
49

<!-- Page 50 -->

[8] Elon Lindenstrauss and A. Mohammadi. “Polynomial effective density in quotients of H3
and H2 ×H2”. In: Inventiones mathematicae 231 (2021), pp. 1141–1237.
[9] Elon Lindenstrauss, Amir Mohammadi, and Zhiren Wang. Effective equidistribution for
some one parameter unipotent flows. 2022. arXiv: 2211.11099 [math.NT].
[10] Elon Lindenstrauss et al. An effective version of the Oppenheim conjecture with a polynomial error rate. 2023. arXiv: 2305.18271 [math.DS].
[11] J. M. Marstrand. “Some fundamental geometrical properties of plane sets of fractional
dimensions”.In:Proc. London Math. Soc. (3) 4(1954),pp.257–302.issn:0024-6115,1460-
244X. doi: 10.1112/plms/s3-4.1.257. url: https://doi.org/10.1112/plms/s3-
4.1.257.
[12] W. H. Schikhof. Ultrametric Calculus: An Introduction to p-Adic Analysis. Cambridge
Studies in Advanced Mathematics. Cambridge University Press, 1985. doi: 10.1017/

## Cbo9780511623844.

[13] V.Vatsal.“UniformdistributionofHeegnerpoints”.In:Invent. Math.148.1(2002),pp.1–
46. issn: 0020-9910,1432-1297. doi: 10.1007/s002220100183. url: https://doi.org/
10.1007/s002220100183.
50