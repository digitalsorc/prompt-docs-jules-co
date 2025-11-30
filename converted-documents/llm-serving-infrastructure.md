---
title: "LLM Serving Infrastructure"
original_file: "./LLM_Serving_Infrastructure.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "multimodal"]
keywords: ["cid", "splitting", "maximal", "agol", "proof", "figure", "pseudo", "anosov", "train", "lemma"]
summary: "<!-- Page 1 -->

4202
peS
42
]TG.htam[
1v32461.9042:viXra

## Agol Cycles Of Pseudo-Anosov Maps On The


## 2-Punctured Torus And 5-Punctured Sphere


## Jean-Baptiste Bellynck And Eiko Kin

Abstract. Given a periodic splitting sequence of a measured train track, an Agol cycle is the part that constitutes a period up to the action of a pseudo-Anosov map and
the rescaling by its dilatation. We consider a family of pseudo-Anosov maps on the 2-
punctured torus and on the 5-punctured sphere."
related_documents: []
---

# LLM Serving Infrastructure

<!-- Page 1 -->

4202
peS
42
]TG.htam[
1v32461.9042:viXra

## Agol Cycles Of Pseudo-Anosov Maps On The


## 2-Punctured Torus And 5-Punctured Sphere


## Jean-Baptiste Bellynck And Eiko Kin

Abstract. Given a periodic splitting sequence of a measured train track, an Agol cycle is the part that constitutes a period up to the action of a pseudo-Anosov map and
the rescaling by its dilatation. We consider a family of pseudo-Anosov maps on the 2-
punctured torus and on the 5-punctured sphere. We present measured train tracks and
compute their Agol cycles. We give a condition under which two maps in the defined
family are conjugate or not. In theprocess, we find a new formula for thedilatation.

## Introduction

LetΣ = Σ beanorientablesurfacewithgenusg andnpunctures. LetMCG(Σ)bethe
g,n
mapping class group of Σ. According to the Nielsen-Thurston-classification, every element
of MCG(Σ) falls into 3 types: periodic, reducible and pseudo-Anosov. If φ: Σ Σ is a
→
pseudo-Anosov map, then there exist associated stable and unstable measured laminations
( s,νs) and ( u,νu) and the dilatation λ = λ(φ) > 1 such that

## L L

φ( s,νs)= ( s,λνs) and φ( u,νu)= ( u,λ 1νu).
−

## L L L L

A measured train track (τ,µ) is a train track τ with a transverse measure µ. Edges of a
train track are called branches and vertices are called switches. A branch that locally looks
like the central branch in Figure 1(1) is called a large branch. A splitting at a large branch
is an operation that gives a new measured train track. There are two kinds of splitting,
left and right splitting at a large branch (Figure 1(2)(3)). See Definition 2.1.
A maximal splitting (τ ,µ ) ⇀ (τ ,µ ) is an operation on the measured train track
0 0 1 1
(τ ,µ ) that splits all the large branches that carry maximal µ -weight and (τ ,µ ) is the
0 0 0 1 1
resulting measured train track. If all the splittings in a maximal splitting are left (resp.
l r
right) splittings, the maximal splitting is denoted by ⇀ (resp. ⇀) and called a left (resp.
right) maximal splitting.
It was proven by Agol that after enough maximal splittings the measured train track
(τ,µ)suitedtothestablemeasuredlaminationofapseudo-Anosovmapφwillhavechanged
to φ(τ,λ 1µ) := (φ(τ),λ 1φ (µ)), where the measure φ (µ) is defined by φ (µ)(e) :=
− −
∗ ∗ ∗
Date: September26, 2024.
Key words and phrases. pseudo-Anosov,periodic splitting sequences, Agol cycle length.
1

<!-- Page 2 -->


## 2 Jean-Baptistebellynckandeikokin

x z x
x+y
z x z
left splitting =z+w right splitting
z-x=y-w x-z=w-y
folding large branch folding
y w y w y w
(2) (1) (3)
Figure 1. (1) A large branch. (2) Left splitting when z > x ( y > w),
⇔
(3) right splitting when x > z ( w > y) at the large branch.
⇔
µ(φ 1(e))forabrancheinthetraintrack φ(τ). Tostate Agol’s resultprecisely, asequence
−
of consecutive n maximal splittings (τ ,µ ) ⇀ ⇀ (τ ,µ ) is denoted by (τ ,µ ) ⇀n
0 0 n n 0 0
···
(τ ,µ ).
n n
Theorem 1.1 (Agol [1]. See also Agol-Tsang [2]). Let φ: Σ Σ be a pseudo-Anosov
→
map with dilatation λ. Let (τ,µ) be a measured train track suited to the stable measured
lamination of φ. Then there exist n 0 and m > 0 such that
≥
(τ,µ) ⇀n (τ ,µ ) ⇀m (τ ,µ ) = φ(τ ,λ 1µ ).
n n n+m n+m n − n
For the terminology suited to, see Definition 2.2. We call the maximal splitting sequence
(τ ,µ ) ⇀m (τ ,µ )⇀m (τ ,µ ) ⇀m
n n n+m n+m n+2m n+2m
···
a periodic splitting sequence of φ. We call the finite subsequence (τ ,µ ) ⇀m (τ ,µ )
n n n+m n+m
anAgol cycleof φandcall mtheAgol cycle lengthof φ, denotedby ℓ(φ). Thetotal splitting
number of an Agol cycle of φ, denoted by N(φ), is the number of large branches that are
split in the Agol cycle (Definition 2.3(3)).
An equivalence class of an Agol cycle is a conjugacy invariant of pseudo-Anosov maps
(Section 2.1). TheAgol cycle length ℓ(φ)andtotal splitting numberN(φ) areconjugacy invariantsaswell. Ifφ :Σ Σisfully-punctured(i.e.,thesingularitiesofthestable/unstable
→
foliations of φ lie on the punctures of Σ), N(φ) equals the number of ideal tetrahedra in
the veering triangulation of the mapping torus of φ. See [1] for more details.
ItisnaturaltoaskhowtheAgolcyclelengthℓ(φ)andtotal splittingnumberN(φ)relate
to other invariants of pseudo-Anosov maps. In [6] it was proven that for every pseudo-
Anosov 3-braid β, its Agol cycle length, the Garside canonical length of any element in the
super summit set of β are the same. Agol-Tsang [2] proved that the total splitting number
N(φ) for a fully puncturedpseudo-Anosov φ: Σ Σ is boundedfrom above by a constant
→
depending on the normalized dilatation λ χ(Σ), where χ(Σ) is the Euler characteristic of
−

## Σ.

The main goal of this paper is to give an explicit description of an Agol cycle of every
pseudo-Anosov map in the two semigroups F MCG(Σ ) and F MCG(Σ ) which

## T 1,2 D 0,5

⊂ ⊂
will be defined below. On the 2-punctured torus Σ , let δ be the right-handed Dehn
1,2 i
twist about the simple closed curve c Σ for i 1,2,3 shown in Figure 2(1). The
i 1,2
⊂ ∈ { }
hyperelliptic involution exchanges the two punctures of the torus and induces a 2-fold

<!-- Page 3 -->


## Agol Cycles Of Pseudo-Anosov Maps 3

branched cover Σ Σ of the 5-puncturedsphere. Then δ descends to σ , the positive
1,2 0,5 i i
→
half-twist about the segment α connecting the punctures i and i+1 (Figure 2(5)).
i
y
2 4 2 4
c x
1 c α α
c c 2 y 1 α 3
1 c 3 2
2 c z 1 3 1 3
3
x
(1) (2) (3) (5)
y y
z
x
z
(4)
Figure 2. (1)(2) Simple closed curves c ,c and c in Σ . (3) (b,x) in
1 2 3 1,2
x
Σ 1,2 and (4) (b L ,x) in Σ 0,5 for x = y . (5) Segments α i in Σ 0,5 .
z
(cid:16) (cid:17)

### We study pseudo-Anosov maps in the semigroups

F := F(δ ,δ ,δ 1) MCG(Σ ) and F := F(σ ,σ ,σ 1) MCG(Σ )

## T 1 3 2−

⊂

## 1,2 D 1 3 2−

⊂
0,5
generated by δ , δ and δ 1 and by σ , σ and σ 1. Each σ for i 1,2,3 fixes the
1 3 2− 1 3 2− i
∈ { }
fifth puncture of Σ . Hence, one can regard an element of F as a mapping class on the

## 0,5 D

4-punctureddisk. Thesubset N3n, whereN = N 0 , will beusefulfor our study of

### I n ⊂ 0 0 ∪{ }

pseudo-AnosovmapsinF andF (Definition2.9). Foreachp = (p ,p ,q ,...,p ,p ,q )
T D n ′n n 1 ′1 1
∈
n

## I

Φ p := δ 1
pnδ
3
p′
nδ 2−
qn
··· δ 1
p1δ
3
p′
1δ 2−
q1
∈ F T and φ p := σ 1
pnσ
3
p′
nσ 2−
qn
··· σ 1
p1σ
3
p′
1σ 2−
q1

## ∈ F D

1 10 1 0 0 10 0
are pseudo-Anosov maps. We take matrices M 1 = 0 10 , M 3 = 0 1 0 , M 2 = 11 1 .
0 01 0 1 1 00 1
For each p n the matrix (cid:16) (cid:17) (cid:16) (cid:17) (cid:16) (cid:17)

## ∈I


## M := M

pnM p′
nM
qn

## M

p1M p′

## 1M

q1
p 1 3 2 ··· 1 3 2
isPerron-Frobenius. ThePerron-Frobeniuseigenvalueλ isequaltothedilatationsofmaps
p
Φ and φ . In Theorem 2.13 we present an explicit description of the Perron-Frobenius
p p
eigenvalue λ and the normalized eigenvector v . As a consequence we see that λ is a
p p p
quadratic irrational (Remark 2.15). Let b Σ (resp. (b Σ ) be train track as in

## 1,2 L 0,5

⊂ ∈
Figure2(3)(resp. Figure2(4)). AssigningthecoefficientsofaPerron-Frobeniuseigenvector
x of M to the branches of the train track makes the measured train track (b,x) (resp.
p
(b ,x)).

## L

We say that p is symmetric if p = p for all i 1,...,n . Otherwise, p is

## ∈ I

n i ′i
l n ∈ { r n }
asymmetric. To state our results, we use the symbol ⇀ (resp. ⇀ ) for n consecutive left
(resp. right) maximal splittings.
Theorem 1.2. For p = (p ,p ,q ,...,p ,p ,q ) let Φ F be the pseudo-Anosov
n ′n n 1 ′1 1

## ∈ I

n p
∈

## T

map and M be the Perron-Frobenius matrix associated with p. Let v > 0 be an eigenvector
p

<!-- Page 4 -->


## 4 Jean-Baptistebellynckandeikokin

with respect to the Perron-Frobenius eigenvalue λ of M . Then the Agol cycle length ℓ of
p p
Φ is
p
n (p +2q ) if p is symmetric,
ℓ = i=1 i i
n (p +p +3q ) if p is asymmetric.
(cid:26) P i=1 i ′i i
Moreover, starting with the measured train track (τ ,µ ) = (b,λ v), a finite subsequence

### P 0 0 p

of the maximal splitting sequence
(τ ,µ )⇀
r pn
⇀
l 2qn
⇀
r p1⇀ l 2q1
(τ ,µ ) if p is symmetric,
0 0 ℓ ℓ
···
(τ ,µ )⇀ r
pn+p′
n⇀ l
3qn
⇀ r
p1+p′
1⇀ l
3q1
(τ ,µ ) if p is asymmetric
0 0 ℓ ℓ
···
forms an Agol cycle of Φ .
p
We later prove an analogous statement for the pseudo-Anosov maps φ F inside the
p D
∈
semi-group F (See Theorem 4.1).

## D

As applications, we give formulas on the total splitting numbers N(Φ ) and N(φ ) for
p p
each p (Theorems 3.4, 4.8). We also classify conjugacy classes of pseudo-Anosov
n

## ∈ I

maps in F and F (Theorem 5.1). The total splitting numbers N(Φ ) and N(φ ) have

### T D p p

the following additive property.
Theorem 1.3. For p = (p ,p ,q ,...,p ,p ,q ) and t = (t ,t ,u ,...,t ,t ,u )
n ′n n 1 ′1 1

## ∈ I

n m ′m m 1 ′1 1
∈
, we set pt := (p ,p ,q ,...,p ,p ,q ,t ,t ,u ,...,t ,t ,u ) . The total split-

## I

m n ′n n 1 ′1 1 m ′m m 1 ′1 1

## ∈ I

n+m
ting number of Φ F satisfies N(Φ ) = N(Φ )+N(Φ ). A parallel statement holds
pt T pt p t
∈
for φ F .
pt D
∈
The paper is organized as follows. In Section 2 we recall basic definitions and prove
lemmas. In Sections 3 and 4 we compute Agol cycles of pseudo-Anosov maps in F and

## T

F . In Section 5 we classify pseudo-Anosov conjugacy classes in F and F .

## D T D


## Preliminaries

ThemappingclassgroupMCG(Σ)ofasurfaceΣ = Σ isthegroupofisotopyclasses of
g,n
orientation preserving homeomorphisms of Σ preserving the punctures setwise. We apply
elements of the mapping class group from right to left; i.e., the product fg means that we
applyg, thenf. For simplicity wedonotdistinguishbetweenahomeomorphismφ: Σ Σ
→
and its mapping class [φ] MCG(Σ).
∈

### Measuredtraintracks. Atraintrackτ ΣisafiniteC1-embeddedgraph,equipped

⊂
with a well-defined tangent line at each vertex, also satisfying some additional properties
as stated in Penner-Harer [8]. In this paper we assume our train tracks to be trivalent. A
measured train track (τ,µ) is a train track τ with a measure µ. This is a function that
assigns a positive weight to each branch. Measured train tracks are required to satisfy the
switch condition. This means that if two branches a,b merge into one branch c, then the
weights satisfy µ(a)+µ(b) = µ(c). See Figure 3(1).

<!-- Page 5 -->


## Agol Cycles Of Pseudo-Anosov Maps 5

μ(c)
μ(a) x x
=μ(a)+μ(b) x+z x+y+z x+y+z
z z y+z
μ(b) y y
(1) (2)
Figure 3. (1) Switch condition. (2) Shifting.
Definition 2.1. WeconsideralargebranchasinFigure1(1). Dependingonweightsx,y,z
and w in Figure 1(1), a splitting divides a large branch into two branches and connects
the two parts with either a left-facing or right-facing branch, thereby preserving the switch
condition. Depending on the type of a branch inserted, the splitting is called a left or right
splitting at a large branch (Figure 1(2)(3)). Similarly, we can produce new measured train
tracks through the use of folding (Figure 1) and shifting (Figure 3(2)).
Recall that if all the splittings in a maximal splitting (τ ,µ ) ⇀ (τ ,µ ) are left (resp.
0 0 1 1
l r
right) splittings, the maximal splitting is denoted by ⇀ (resp. ⇀) and called a left (resp.
right) maximal splitting. If there exist both left and right splittings, the maximal splitting
lr
is denoted by ⇀ and called a mixed maximal splitting.
Measured train tracks (τ,µ), (τ ,µ) in Σ are equal (and write (τ,µ) = (τ ,µ)) if there
′ ′ ′ ′
exists a diffeomorphism f : Σ Σ isotopic to the identity map such that f(τ,µ) = (τ ,µ).
′ ′
→
Measured train tracks (τ,µ), (τ ,µ) in Σ are equivalent if they are related to each other
′ ′
by a sequence of splittings, foldings, shiftings and isotopies. Thus measured train tracks
in a splitting sequence are equivalent. Equivalence classes of measured train tracks are in
one-to-one correspondence with measured laminations [8, Theorem 2.8.5].
Definition 2.2. Let ( ,ν) be a measured lamination in Σ, and let (τ,µ) be a measured

## L

traintrackinΣ. Then(τ,µ)issuitedto( ,ν)ifthereexistsadifferentiablemapf : Σ Σ

## L →

homotopic to the identity map on Σ with the following conditions:
f( )= τ.

## • L

f is nonsingular on the tangent spaces to the leaves of .

## • L

If p is an interior point of a branch e of τ then ν(f 1(p)) = µ(e).
−
•
Definition 2.3.
(1) The splitting number of a maximal splitting (τ ,µ ) ⇀ (τ ,µ ) is the number of
0 0 1 1
large branches split, i.e., the number of the large branches of (τ ,µ ) with maximal
0 0
weight.
(2) The total splitting number of a finite sequence of maximal splittings (τ,µ) ⇀n
(τ ,µ ) is the sum of the splitting numbers over all maximal splittings in the finite
n n
sequence.
(3) The total splitting number of an Agol cycle (τ ,µ ) ⇀m (τ ,µ ) of φ, den n n+m n+m
noted by N(φ), is the sum of the splitting numbers over all maximal splittings

<!-- Page 6 -->


## 6 Jean-Baptistebellynckandeikokin

(τ ,µ ) ⇀ (τ ,µ ) in the Agol cycle. The Agol cycle length ℓ(φ) is
n+i n+i n+i+1 n+i+1
less than or equal to N(φ). The equality holds if and only if the splitting number
of each maximal splitting in the Agol cycle is exactly 1.
Definition 2.4. Let φ,φ : Σ Σ be pseudo-Anosov maps with periodic splitting se-
′
→
quences
P :(τ ,µ ) ⇀m (τ ,µ ) = φ(τ ,λ 1µ ) ⇀
n n n+m n+m n − n
···
of φ and

## P

′
:(τ n′′,µ ′n′) ⇀m′ (τ n′′+m′,µ ′n′+m′) = φ
′
(τ n′′,(λ
′
)
−
1µ ′n′) ⇀
···
of φ. We say that P and P are combinatorially isomorphic ([5]) if m = m is fulfilled
′ ′ ′
and there exist an orientation-preserving diffeomorphism h: Σ Σ, integers p,q Z
0
and c R such that the following conditions (1) and (2) hold. → ∈ ≥
>0
∈
(1) φ = h φ h 1.
′ −
(2) h(τ , ◦ µ ◦ )= (τ ,cµ ) for all i Z .
i+p i+p i′+q ′i+q
∈ ≥
0
WesaythattwoAgolcycles(τ ,µ )⇀m (τ ,µ )ofφand(τ ,µ )⇀m′ (τ ,µ )
n n n+m n+m n′′ ′n′ n′′+m′ ′n′+m′
of φ are equivalent if m = m is fulfilled and there exist an orientation-preserving dif-
′ ′
feomorphism h: Σ Σ, integers p,p Z and c R such that h(τ ,µ ) =
′ 0 >0 n+p n+p
→ ∈ ≥ ∈
(τ ,cµ ). The condition for equivalent Agol cycles implies condition (2). See [6,
n′′+p′ ′n′+p′
Lemma 2.2].
Theorem2.5(Theorem5.3inHodgson-Issa-Segerman[5]). Pseudo-Anosovmapsφ,φ : Σ
′
Σ are conjugate in MCG(Σ) if and only if P and P are combinatorially isomorphic. →
′
As a consequence, the equivalence class of an Agol cycle of φ is a conjugacy invariant.
The Agol cycle length ℓ(φ) and total splitting number N(φ) are conjugacy invariants as
well, since they are equal for equivalent Agol cycles.
When we regard a maximal splitting (τ,µ) ⇀ (τ ,µ) as an operation on the measured
′ ′
train track, we write (τ ,µ) = ⇀ (τ,µ). We write n consecutive left (resp. right) max-
′ ′
l n r n l n
imal splittings (τ,µ)⇀ (τ ,µ ) (resp. (τ,µ)⇀ (τ ,µ )) as (τ ,µ ) = ⇀ (τ,µ) (resp.
n n n n n n
r n l n r m
(τ ,µ ) = ⇀ (τ,µ)).We also write a finite sequence (τ,µ)⇀ (τ ,µ )⇀ (τ ,µ ) as
n n n n n+m n+m
r m l n
(τ ,µ ) = ⇀ ⇀ (τ,µ).
n+m n+m
◦
The operation ⇀ and a diffeomorphism φ: Σ Σ commute on measured train tracks:
→
Lemma 2.6 (Lemma 2.1 in [6]). Let (τ,µ) be a measured train track in Σ and φ : Σ
→
Σ an orientation-preserving diffeomorphism. If (τ,µ) admits consecutive n left maximal
l n l n r n
splittings, then we have (φ ⇀ )(τ,µ) = (⇀ φ)(τ,µ). A parallel statement holds for ⇀ .
◦ ◦

<!-- Page 7 -->


## Agol Cycles Of Pseudo-Anosov Maps 7

Remark 2.7. (This remark is used for the proof of Theorem 5.1.) By Lemma 2.6 we have
the following commutative diagram:
(τ,µ) ⇀ (τ ,µ ) ⇀ ⇀ (τ ,µ )
1 1 n n
···
↓ ↓ ↓
φ(τ,µ) ⇀ φ(τ ,µ ) ⇀ ⇀ φ(τ ,µ )
1 1 n n
···
Lemma 2.6 tells us that the (left, right, mixed) type of the maximal splitting φ(τ ,µ ) ⇀
i i
φ(τ ,µ ) is the same as that of (τ ,µ ) ⇀ (τ ,µ ).
i+1 i+1 i i i+1 i+1

### Perron-Frobenius matrices. we write A B if a b for all r,s. Suppose

rs rs
≥ ≥
that M is an n by n square matrix with nonnegative integer entries. We say that M is
Perron-Frobenius if some power of M is a positive matrix. Perron-Frobenius matrices have
the following properties.
Theorem 2.8 (Perron-Frobenius). A Perron-Frobenius M has a real eigenvalue λ >
1which exceeds the moduli of all other eigenvalues. There exists a strictly positive eigenvector v associated with λ. Moreover, v is the unique positive eigenvector of M (up to positive
multiples), and λ is a simple root of the characteristic equation of M.
For the proof, see [4]. We call λ = λ(M) > 1 the Perron-Frobenius eigenvalue of M and
call v a Perron-Frobenius eigenvector.
Definition 2.9. For each n N the subset N3n is defined as follows.
∈ I n ⊂ 0
j, k 1,...,n such that p ,p > 0

### I n :=

(cid:26)
p = (p n ,p ′n ,q n ,...,p 1 ,p ′1 ,q 1 ) ∈ N3 0 n
(cid:12)
p ∃ i + ∃ p ′i ,q ∈ i { > 0 for e } ach i
∈ {
1,.. j .,n ′k
} (cid:27)
For example, (1,0,2,0,1,1)
2
, (1,0,2,1,0 (cid:12) (cid:12),1)
2
. By definition,
1

## = N3.

∈ I (cid:12) 6∈ I I
We recall the matrix M = M pnM p′ nM qn M p1M p′ 1M q1 for p .
p 1 3 2 ··· 1 3 2 ∈ I n
Lemma 2.10. For each p , M is Perron-Frobenius.
n p

## ∈ I

Proof. A computation shows that M i n ≥ M i ≥ 1 0 0 0 1 0 0 0 1 for n ∈ N and i = 1,2,3. By
definition of
n
, all the matrices M
1

## ,M

2
and M
3
(cid:16)appear(cid:17)in the product M
p
at least once.

## I

We can check that M M M M = M M M > 0. This means that M is positive. In
p 1 3 2 3 1 2 p
≥
particular, M is Perron-Frobenius. (This fact also follows from [9, Theorem 3.1].) (cid:3)
p
In this section we give an explicit description of a Perron-Frobenius eigenvector of M
p
andits eigenvalue λ . Todothis,wefirstconsidertheinfinitecontinued fraction expansion
p
of an irrational number a.
1
a = a + = [a ,a , ,a , ]
0 0 1 k
1 ··· ···
a +
1
...
+
1
a +
k
···

<!-- Page 8 -->


## 8 Jean-Baptistebellynckandeikokin

with a Z and a > 0 for i 1. By Lagrange’s theorem, a is a quadratic irrational if and
i i
∈ ≥
only if the expansion is eventually periodic; i.e., there exists t 1 with a = a for all
i i+t
≥
i 1. We write a quadratic irrational a = [a , ,a ,b , ,b ,b , ,b , ] as
0 k 1 0 t 1 0 t 1
≫ ··· − ··· − ··· − ···
[a , ,a ,b , ,b ].
0 k 1 0 t 1
··· − ··· −
Given p , we next define the width w and height h for each j N as follows.
n p,j p,j 0

## ∈ I ∈

For j = 0, w =1 and h = [0,p +p ,q ,...,p +p ,q ].
p,0 p,0 n ′n n 1 ′1 1
For j > 0, w = w (p +p )h and h = h q w .
p,j p,j
−
1
−
n
−
j+1 ′n
−
j+1 p,j
−
1 p,j p,j
−
1
−
n
−
j+1 p,j
The split ratio s (0 < s < 1) is defined by
p p
∞
s = p h ,
p i p,i
−
i=0

## X

where the index of p is understood to be mod n.
i
−
p p' n squares n squares
qn
squares
p p' n-1 n-1
q w n-1squares
p,1
hp,0
h p,1
w =1 p,0
(1) (2)
hT(p),0
p n-1 squares p n-2 p n ' -2 p n ' -1 squares
w T(p),0=1
qn-1squares
hp,1
rescale by1/w p,1 w
p,1
h T(p),1 q
n-2squares
w

### T(p),1

s s p T(p)
Figure 4. Partitioned rectangles (1) rect(p), (2) rect(T(p)) for p =
(1,1,2,2,1,1), T(p) = (2,1,1,1,1,2) .
2

## ∈ I

a 1squares
a2
squares
a
3
squares
a4squares
(cid:0) (cid:1)(cid:2) (cid:3) (cid:4)
p p' n squares n squares
fle
1
qn
squares
p p' n-1 n-1
h
p,1 q
w
n-1squares
p,1
1
(1) (2)
Figure 5. (1) Rectangle model for [0,a ,a ,...] = [0,2,2,3,1,...]. (2)
1 2
Reshuffling squares when [0,a ,a ,a ,a ] = [0,1+1,2,2+1,1].
1 2 3 4

<!-- Page 9 -->


## Agol Cycles Of Pseudo-Anosov Maps 9

Definition 2.11. (Partitioned rectangle.) For p = (p ,p ,q ,...,p ,p ,q ) we define
n ′n n 1 ′1 1

## ∈ I

n
a partitioned rectangle rect(p) as in Figure 4. We start out with a rectangle of width
1 and height h = [0,p +p ,q ,...,p +p ,q ]. We then partition the rectangle into
p,0 n ′n n 1 ′1 1
squares by the following procedure. First, we insert p squares from the left. In the
n
remaining rectangle, we insert p from the right and then q from the bottom. We do
′n n
the same for p ,p ,q ,...,p ,p ,q ,p ,p ,q ,..., repeating the insertion pattern
n 1 ′n 1 n 1 1 ′1 1 n ′n n
cyclically, infinit − ely m−any t − imes. Rectangles for the example p = (1,1,2,2,1,1) and T(p)
are illustrated in Figure 4.
Lemma 2.12. The partitioned rectangle rect(p) is well defined.
Proof. Weintroduceausefultoolforinfinitecontinuedfractions. (Seealso[7].) Wedefinea
rectangle whose width is 1 and whose height is [0,a ,a ,...] for a N. Then it is possible
1 2 i
∈
to iteratively fill in a ,a ,... squares as in Figure 5(1). Suppose that [0,a ,a ,...,a ]=
1 2 1 2 2n
[0,p +p ,q ,...,p +p ,q ]. We reshuffle the squares such that p squares are filled from
n ′n n 1 ′1 1 i
theleftandp squaresarefilledfromtheright(see Figure4). Thisshowsthatthepartition
′i
into squares for p is well defined. (cid:3)
n

## ∈ I

The values w , h can be thought of as the widths and heights of the rectangles
p,0 p,0
obtainedwhenweiteratively deleteoutsidesquaresasinFigure4. Thevaluesareindicated
in the picture.
Theorem 2.13. For p = (p ,p ,q ,...,p ,p ,q ) the Perron-Frobenius eigenvalue
n ′n n 1 ′1 1

## ∈ I

n
λ of M and its eigenvector v > 0 are given by
p p
1 sp
λ
p
= and v = hp,0 .
w p,n
(cid:18)
1
−
sp(cid:19)
We call v = v the normalized eigenvector with respect to λ .
p p
Proof. Recall that T: N3n N3n is the shift as in Section 1. For p we define
scaling factors λ := w 0 / → w 0 for i N . The scaling factors fulfi ∈ ll I th n e property
p,i p,i p,i+1 0
∈
i n =−0 1λ p,i = 1/w p,n . We will prove
Q λ p,0 M 2− qnM 1− pnM 3 − p′ n h s p p ,0 = h s T T ( ( p p ) ) ,0 . (2.1)
(cid:18) 1 − sp(cid:19) (cid:18) 1 − s T(p)(cid:19)
Using this, we can then inductively deduce the following statement:
( n i= − 0 1 λ p,i )(M 1 pnM 3 p′ nM 2 qn ··· M 1 p1M 3 p′ 1M 2 q1) − 1 (cid:18) 1 h − s p p s ,0 p(cid:19) = (cid:18) 1 h − s T T s n n T ( ( n p p ) ( ) , p 0 )(cid:19) = (cid:18) 1 h − s p p s ,0 p(cid:19) (2.2)

## Y

The definitions of w and h are such that they line up with the lengths of the line
p,i p,i
segments in rect(p) as in Figure 4. Adding up the widths of all the squares on the left side,

<!-- Page 10 -->


## 10 Jean-Baptistebellynckandeikokin

we get s p (= ∞i=0 p i h p,i ). Using Figure 4, we observe that for
−
(cid:16) y y y 1 2 3 (cid:17) := M 2− PqnM 1− pnM 3 − p′ n (cid:18) 1 h − s p p s ,0 p(cid:19) = M 2− qn (cid:18) 1 s − p s ,0 p − h − p p p , n 0 ′ n h h p p ,0 ,0(cid:19) = (cid:18) hp,0 − q 1 n − s ( p s 1 − p − − p ( n p p h n ′ n p + h , p 0 p , ′ n 0 )hp,0) (cid:19) ,
we have w = 1 (p +p )h = y +y and h = h q w = y .
p,1 n ′n p,0 1 3 p,1 p,0 n p,1 2
− −
Remove (p +p ) squares with height h and q squares with height w from rect(p).
n ′n p,0 n p,1
If we then scale the remaining small rectangle by λ = 1/w , its width becomes 1 and
p,0 p,1
therectanglebecomesapartitionedrectangle. Bymovingallsquarestotheleft,weseethat
its height must be [0,p +p ,q ,...,p +p ,q ,p +p ,q ]= h . Its partition
n 1 ′n 1 n 1 1 ′1 1 n ′n n T(p),0
into squares then tells u − s that t−he res − ulting partitioned rectangle is rect(T(p)). The value
y is the sum of the widths of all squares sitting on the left of the small rectangle. When
1
scaling up y by λ , the value λ y continues to be the sum of square widths. This
1 p,0 p,0 1
shows λ y = s . (See Figure 4.) This proves statement (2.1).
p,0 1 T(p)
Statement (2.2) follows from applying statement (2.1) n times. The value w 1 =
p−,n
sp
i n =−0 1λ p,i then becomes the eigenvalue of the eigenvector hp,0 of M p . Because the vec-
(cid:18)
1
−
sp(cid:19)
tQor entries are all positive and M
p
is Perron-Frobenius, w
p−,
1
n
must be the Perron-Frobenius
eigenvalue λ by Theorem 2.8. (cid:3)
p
Corollary 2.14. The splitting ratio s can be written as follows.
p
∞ p n h p,0 +p n 1 h p,1 + +p 1 h p,n 1
s p = p i h p,i = − ··· − .

### X i=0

− (p n +p ′n )h p,0 +(p n
−
1 +p ′n+1 )h p,1 +
···
+(p 1 +p ′1 )h p,n
−
1
Proof. Thesplit ratio s can be interpreted as a ratio dividing the width of the partitioned
p
rectangle in two parts. Since the partitioned rectangle rect(p) is self-similar, it contains
a rectangle that after rescaling by the factor λ is partitioned and equal to rect(p). To
p
calculate s , we can therefore ignore the width of the small self-similar rectangle and only
p
use the ratio in the statement instead. (cid:3)
Remark 2.15. For p the height h is a quadratic irrational since the continued
n p,0

## ∈ I

fraction expansion is eventually periodic. One can prove inductively that the width w is
p,j
a quadratic irrational for each j N . Thus λ = w 1 is also a quadratic irrational.
0 p p−,n
∈
Corollary 2.16. Let p = (p ,p ,q ,...,p ,p ,q ) and t = (t ,t ,u ,...,t ,t ,u )
n ′n n 1 ′1 1

## ∈ I

n n ′n n 1 ′1 1
∈
. If p +p = t +t and q = u hold for all i 1,...,n , then we have the following.

## I

n i ′i i ′i i i
∈ { }
(1) λ = λ .
p t
(2) If t = f(p), then s +s = 1, where f :N3n N3n is the flip.
p f(p) 0 → 0
(3) If (p ,p ,...,p ) (t ,t ,...,t ), then s < s , where is the lexicographic
n n 1 1 n n 1 1 p t
ordering − of Nn. ≺ − ≺
0
Proof. Claim (1) follows from Theorem 2.13 since w = w holds for all n N . Exp,n t,n 0
∈
changing p and p for all i 1,...,n , flips the partitioned rectangle rect(p) horizontally.
i ′i
∈ { }

<!-- Page 11 -->


## Agol Cycles Of Pseudo-Anosov Maps 11

This means that s = 1 s . The proof of (2) is done. For each p and all i N ,
f(p) p n 0

## − ∈ I ∈

we have the property w < h . Using the definition of the partitioned rectangle, this
p,i+1 p,i
implies claim (3). (cid:3)
For a vector v = (v ) Rn, we denote by v the i-th coordinate v of v. When M is an
i i i
∈ |
n by n square matrix, we also use the symbol Mv which returns the i-th coordinate of
i
|
the vector Mv.
Corollary 2.17. For p let v > 0 be a Perron-Frobenius eigenvector of M . Then
n p

## ∈ I

v = v holds if and only if p is symmetric.
1 3
| |
Proof. Corollary 2.16(2)(3) implies that s = 1 holds if and only if f(p) = p holds; i.e.,
p 2
p is symmetric. By Theorem 2.13 the Perron-Frobenius eigenvector v = v satisfies the
p
desired property. (cid:3)
Example 2.18. Let us apply Theorem 2.13 and Corollary 2.14 to compute s and λ .
p p
(1) Let p =(p,p,q) . Then h = [0,p+p,q ]. We have
′ 1 p,0 ′

## ∈ I

ph p 1 1
p,0
s = = , λ = = .
p p
(p+p)h p+p w 1 (p+p)h
′ p,0 ′ p,1 ′ p,0
−
(2) Let p = (1,0,1,0,1,1) . We have h = [0,1] = 1+√5, w = 1 h ,
∈ I 2 p,0 − 2 p,1 − p,0
h = h w , and w = w h . Hence, s and λ are given by
p,1 p,0 p,1 p,2 p,1 p,1 p p
− −
h h 1 1 7+3√5
p,0 p,0
s = = , λ = = = .
p p
h +h 3h 1 w 2 3h 2
p,0 p,1 p,0 p,2 p,0
− −
By a calculation we have the following lemma.
x
Lemma 2.19. Let q N and p,p N . Let x = y > 0.
′ 0
∈ ∈ z
(cid:16) (cid:17)

## (1) M

p

## M

p

## M

qx

## M

p

## M

p

## M

qx
if and only if x z.
(2) Su 1 ppo 3 se t 2 hat | 1 p ≤ > p 1 3 0. T 2 he | n 3 M p M p′ M qx > ≤ M p M p′ M qx for any x > 0.
(3) Suppose that 0 p ′ < ≥ p. Then M 1 p M 3 p′ M 2 qx | 1 < M 1 p M 3 p′ M 2 qx | 3 for any x > 0.
≤ ′ 1 3 2 | 1 1 3 2 | 3
As a corollary of Lemma 2.19, we immediately have the following result.
Corollary 2.20. If x = x y is a positive vector with x = z, then M p M p′ M qx =
z 6 1 3 2 | 1 6
M p M p′ M qx for any q N(cid:16) a(cid:17)nd p,p N (possibly p = p).
1 3 2 | 3 ∈ ′ ∈ 0 ′

### Pseudo-Anosov maps in the semigroup F = F(σ ,σ ,σ 1). We write h = σ ,


## D 1 3 2− 1 1

h = σ and h = σ 1. For a map h = h h F (n 1,2,3 ) we set M :=
3 3 2 2− n k··· n1 ∈ D i ∈ { } h
M M . The following is a well-known result.
n
k···
n1

<!-- Page 12 -->


## 12 Jean-Baptistebellynckandeikokin

Proposition 2.21. The product h = h h F is pseudo-Anosov if all σ ,σ and
n k··· n1 ∈ D 1 3
σ 1 appear in the product at least once. In this case the dilatation λ(h) of h equals the
2−
Perron-Frobenius eigenvalue λ(M ).
h
For the convenience of the reader, we give an outline of the proof. We use a criterion by
Bestvina-Handel algorithm [3] to determine when a mapping class is pseudo-Anosov. We
first choose a finite graph G Σ that is homotopy equivalent to Σ as in Figure 6(2).
0,5 0,5
⊂
The graph G has four vertices 1,...,4 and four loop edges, each of which encircles a
puncture. Let P be the set of four loop edges of G.
Given a mapping class ψ MCG(Σ ), one can pick an induced graph map g : G G
0,5
∈ →
homotopic to ψ. We require that g sends vertices to vertices, edges to edge paths and
fulfills g(P) = P. (See [3, Section 1].) We may suppose that g has no backtracks; i.e., g
maps each oriented edge of G to an edge path which does not contain an oriented edge e
followed by the same edge e with the opposite orientation. This map g defines a 3 by 3
transition matrix M (with respect to the 3 non-loop edges). For r,s 1,2,3 the entry
∈ { }
M is the number of times that the g-image of the s-th edge runs the r-th edge in either
rs
direction. We say that g :G G is efficient if gn :G G has no backtracks for all n > 0.
→ →
Notice that h for i 1,2,3 induces a graph map g : G G which has no backtracks
i i
∈{ } →
as shown Figure 6(1)–(4). The transition matrix of g is given by the matrix M as in
i i
Section 1.
e'
2
e' e 3 ' g 1 2 4 g 3 e 2 ' y x 1 e' e'
1 3 1 3 1 2 1
(1) (2) sm o (4) x x
g
o th
in
y y
2 g
z z
2 4
e'
3 z z
4 3 4
e
1
' x y
y
1 3
(3) (5) (6) (7)
(cid:5)
e e 2 e 1 3

## G

( , v )
(cid:6)
( , v ) -1 ( , v )
Figure 6. (1)–(4) The graph maps g : G G. e := g (e ). (5) (n,v =
i
→
′j i j
x
y ) in Σ 0,5 . (6)(7) The 2-fold branched cover π: Σ 1,2 Σ 0,5 .
z →
(cid:16) (cid:17)
The composition g := g g : G G is an induced graph map of h = h h .
h n k··· n1 → n k··· n1
(A priori, g could have backtracks.) We call k the length of the graph map g . By
h h
induction on the length k, it can be shown that g : G G has no backtracks for any
h
→
h F . In particular, gn : G G has no backtracks for any n > 0; i.e., g : G G
∈ D h → h →

<!-- Page 13 -->


## Agol Cycles Of Pseudo-Anosov Maps 13

is efficient, because gn is an induced graph map of hn F . Since g : G G has no
h ∈ D h →
backtracks, the transition matrix with respect to the non-loop edges of g is given by M .
h h
If all σ , σ and σ 1 appear in the product h at least once, then M is Perron-Frobenius
1 3 2− h
by Lemma 2.10. By the Bestvina-Handel algorithm [3], the two conditions (g : G G is
h
→
efficient, andthetransitionmatrixM isPerron-Frobenius)ensurethathispseudo-Anosov
h
with dilatation λ(M ).
h
Remark 2.22. Let g : G G be an efficient graph map. We obtain a trivalent train
h
track n in Σ (Figure 6(5)) → by graph smoothing near the vertices of G. See [3, Section 3.3]
0,5
for more details. Denote by v the Perron-Frobenius eigenvector of M . We assign the
h
weight v (that is the i-th coordinate of v) to the i-th branch and we obtain the measured
i
train trac | k (n,v) (also described in Figure 6(5)). This measured train track (n,v) is suited
to the stable measured lamination of h by [3, Section 3.4].

### Pseudo-Anosov maps in the semigroup F = F(δ ,δ ,δ 1). Theunionof curves


## T 1 3 2−

c c c (Figure 2(1)) fills the surface Σ . A construction of pseudo-Anosov maps by
1 2 3 1,2
∪ ∪
Penner [9, Theorem 3.1] tells us that the product of δ , δ and δ 1 is pseudo-Anosov if all
1 3 2−
the Dehn twists δ , δ and δ 1 appear in the product at least once. Thus for each p ,
1 3 2−

## ∈ I

n
the map Φ F is pseudo-Anosov by the definition of (Definition 2.9). The map
p T n

## ∈ I

φ F is also pseudo-Anosov for each p by Proposition 2.21. Additionally, each
p D n

## ∈ ∈ I

pseudo-Anosov map in F (resp. F ) is conjugate to Φ (resp. φ ) for some p . The
T D p p n

## ∈ I

link between the maps Φ and φ can be found in the following lemma.
p p
Lemma 2.23. For p let v > 0 be an eigenvector for the Perron-Frobenius eigenvalue
n
λ of M . Then the ∈ m I easured train tracks (b ,v) in Σ and (b,v) in Σ defined in
p p L 0,5 1,2
Section1aresuitedtothestablemeasured laminations ofφ F andΦ F respectively.
p D p T
∈ ∈
Moreover, it holds λ(φ ) = λ(Φ ) =λ , where λ is a quadratic irrational.
p p p p
Proof. By Remark 2.22 (n,2v) is suited to the stable measured lamination of φ . Figure 7
p
illustrates that(n,2v) isequivalent to(b ,v). Therefore, (b ,v)isalso suitedtothestable

## L L

measured lamination of φ .
p
z x+y z x+y z
2y 2z y y
2x
x y+z x y+z x
2 (cid:7)
x+y z
2 (cid:7)
x+y z
y y
y y
x y+z x y+z
x (cid:8) (cid:9) (cid:10)
(cid:9) (cid:10) (cid:8) (cid:11)
x
(cid:7) (cid:12) (cid:13)
z
s(cid:15) (cid:16)(cid:17)(cid:18)
(cid:7)
(cid:14) (cid:12)
x
(cid:7)
(cid:8) (cid:9) (cid:10) (cid:8) (cid:11)
(cid:7)
(cid:14) (cid:12)
(cid:14)
(cid:7)
(cid:12) (cid:13)
(cid:7) (cid:12) (cid:13)
l
(cid:17)f (cid:19)(cid:20) (cid:17)f (cid:19)(cid:20) r
( , 2 v ) ( , v )
l r
Figure 7. (resp. ) denotes the left (resp. right) splittings at the
highlighted l → arge branc → hes. (n,2v) is equivalent to (b ,v).

## L


<!-- Page 14 -->


## 14 Jean-Baptistebellynckandeikokin

We regard Σ as the once punctured spherewith four marked points p (i 1,...,4 ).
0,5 i
∈ { }
Consider a 2-fold branched cover π: Σ Σ branched over the four marked points and
1,2 0,5
→
induced by the hyperelliptic involution of Σ , exchanging the two punctures. Notice that
1,2
δ := δ MCG(Σ ) is a lift of σ MCG(Σ ). Hence, Φ F is a lift of φ F . It
j cj
∈
1,2 j
∈
0,5 p
∈
T p
∈

## D

follows that Φ and φ have the same dilatation. By Proposition 2.21 we have λ(φ ) = λ .
p p p p
Thus λ(Φ )= λ(φ )= λ . By Remark 2.15 λ is a quadratic irrational.
p p p p
Let s and u be the stable and unstable foliations with respect to φ . The preimages
p

## F F

π 1( s) and π 1( u) give the stable and unstable foliations with respect to Φ . Since p
− − p i

## F F

is a 1-pronged singular point of s and u, the preimage π 1(p ) is a regular point (i.e.,
− i
a 2-pronged point) of π 1( s) an F d π 1( F u). Notice that π 1(n) admits four bigons each
− − −

## F F

of which contains a regular point π 1(p ). See Figure 6(6)(7). Then the measured train
− i
track (b,v) in Σ is obtained from π 1(n,v) by collapsing each bigon. As a result, (b,v)
1,2 −
is suited to the stable measured lamination of Φ . (cid:3)
p
We will choose (b,λ v) (resp. (b ,λ v)) as the start of the maximal splitting sequence
p L p
in the proof of Theorem 1.2 (resp. Theorem 4.1).

## Agol cycles of pseudo-Anosov maps in F


## T

The goal of this section is to prove Theorem 1.2. To do this, we first construct finite
sequences of maximal splittings (Lemma 3.1, Proposition 3.2). Then we concatenate some
finite sequences to produce an Agol cycle of the pseudo-Anosov map Φ .
p
When p is symmetric, the normalized eigenvector v with respect to λ fulfills v =
p p p 1
|
v (Corollary 2.17). This extra symmetry gives simpler maximal splitting sequences.
p 3
|
Hence, the measured train tracks with symmetric weights (i.e. x = z) and asymmetric
weights (i.e. x = z) will be treated differently in the following lemma.
6
x
Lemma 3.1. Let q N and p,p N . Let x = y > 0.
′ 0
∈ ∈ z
(cid:16) (cid:17)
(1) Suppose that p > 0. Then
(δ 1δ 1 ⇀ r )(b,M p M p M qx) if x = z,
(b,M 1 p − 1 M 3 p − 1 M 2 qx)= ( (δ 1 1 − − 1δ 3 3 − − 1 ◦ ◦ ⇀ r 2 )(b,M 1 1 p M 3 3 p M 2 2 qx) if x 6 = z.
(2) Suppose that p > p 0. Then
′
≥
(b,M 1 p − 1 M 3 p′ M 2 qx)= (δ 1− 1 ◦ ⇀ r )(b,M 1 p M 3 p′ M 2 qx).
(3) Suppose that 0 p < p. Then
′
≤
(b,M 1 p M 3 p′ − 1 M 2 qx)= (δ 3− 1 ◦ ⇀ r )(b,M 1 p M 3 p′ M 2 qx).
2
(δ ⇀ l )(b,M qx) if x = z,
(4) (b,M 2 q − 1x) =  (δ 2 ◦ ⇀ l 3 )(b,M 2 qx) if x = z.
 2 ◦ 2 6


<!-- Page 15 -->


## Agol Cycles Of Pseudo-Anosov Maps 15

Proof. AcalculationM
2
qx = qx+ x
z
y+qz showsthatx
| 1

## = M

2
qx
| 1
= xandx
| 3

## = M

2
qx
| 3
= z.
For the proof of claims (1)–(4(cid:16)), it is su(cid:17)ffices to prove them for q = 1. In fact, once we prove
claims (1)–(4) for q = 1, we can apply them to the positive vector x ′ = M 2 q − 1x.
We have M 1 p M 3 p M 2 x y z = x py + y ′ p + ′ y z ′ , where y ′ = x+y +z. The measured train track
(τ ,µ ):= (b,M p M p M(cid:16)x)(cid:17)has (cid:18) twolar (cid:19) gebrancheswithweightsx+(p+1)y and(p+1)y +z.
0 0 1 3 2 ′ ′
We first consider the case x = z. We may suppose that x < z. Applying 2 maximal
6
splittings (see Figure 8), we obtain 2 right maximal splittings
(τ 0 ,µ 0 )= (b,M 1 p M 3 p M 2 x)⇀ r 2 (τ 2 ,µ 2 )= δ 1 δ 3 (b,M 1 p − 1 M 3 p − 1 M 2 x).
In other words, (b,M 1 p − 1 M 3 p − 1 M 2 x) = (δ 1− 1δ 3− 1 ◦ ⇀ r 2 )(b,M 1 p M 3 p M 2 x). This gives claim (1)
when x < z.
y'
x+py'
r r
y'
py'+z
( (cid:21) (cid:22) ( (cid:23) (cid:22)
y' y' x+(p-1)y'
x+py'
y' y'
(p-1)y'+z (p-1)y'+z
( , μ ) ( , μ ) (3)( , μ )
0 0 1 1 2 2
(cid:24)
1
(cid:25)
y'
-1-1 x+(p-1)y'
3
y'
δδ
1 3
(p-1)y'+z
τ τ τ (4)
Figure 8. Proof of Lemma 3.1(1) when x < z. (1) (b,M p M p M x). (4)
1 3 2
(b,M 1 p − 1 M 3 p − 1 M 2 x).
In the case x = z, the two large branches of the measured train track (b,M p M p M x)
1 3 2
have the same maximal weight. Applying the maximal splitting, we obtain the right
maximal splitting
(τ 0 ,µ 0 ) = (b,M 1 p M 3 p M 2 x)⇀ r (τ 1 ,µ 1 ) = δ 1 δ 3 (b,M 1 p − 1 M 3 p − 1 M 2 x).
This completes the proof of claim (1).
We turn to claim (2). Suppose that p > p ′ ≥ 0. We have M 1 p M 3 p′ M 2 x y z = p x ′ + y y ′ p ′ + y z ′ ,
where y = x+y+z. By a calculation we have M p M p′ M x = x+py > (cid:16) M (cid:17)p M p (cid:18)′ M x (cid:19) =
py +z. ′ The measured train track (τ ,µ ) := (b,M 1 p M 3 p′ M 2 | x 1 ) has two ′ large 1 bra 3 nche 2 s w | 3 ith
′ ′ 0 0 1 3 2
weights x+(p+1)y and (p +1)y +z. Applying a maximal splitting (see Figure 9), we
′ ′ ′
obtain a right maximal splitting
(τ 0 ,µ 0 ) = (b,M 1 p M 3 p′ M 2 x)⇀ r (τ 1 ,µ 1 ) = δ 1 (b,M 1 p − 1 M 3 p′ M 2 x).

<!-- Page 16 -->


## 16 Jean-Baptistebellynckandeikokin

y'
x+py'
r
y'
p'y'+z
(cid:26) (cid:27) (cid:28) (cid:26) (cid:29) (cid:28)
y' x+(p-1)y' y'
x+(p-1)y'
δ-1
1
y' y'
δ
1
p'y'+z p'y'+z
( τ , μ ) ( τ , μ ) (3)
0 0 1 1
Figure 9. Proof of Lemma 3.1(2). (1) (b,M p M p′ M x). (3)
1 3 2
(b,M 1 p − 1 M 3 p′ M 2 x).
The proof of claim (2) is done. One can prove claim (3) in a similar way.
x
We now prove claim (4). We set (τ
0
,µ
0
) = (b,M
2
x = x+y+z ). Consider the case
z
x = z. We may suppose that x < z. Applying 3 maximal(cid:16)splittin(cid:17)gs (see Figure 10), we
6
obtain 3 left maximal splittings
(τ ,µ ) = (b,M x)⇀ l (τ ,µ )⇀ l (τ ,µ )⇀ l (τ ,µ ) = δ 1(b,x).
0 0 2 1 1 2 2 3 3 2−
This gives claim (4) for x < z.
x
x+y+z
z
(cid:30) (cid:31) !
l
(cid:30) " !
l l
(3) (4)
z
x+y+z x+y+z y
y+z y+z
x x x x x x
x+y+z δ
2
y δ-1 y
2
x+y x+y x+y z
z z z
y
( τ , μ ) ( τ , μ ) ( τ , μ ) ( τ , μ ) (5)
0 0 1 1 2 2 3 3
Figure 10. Proof of Lemma 3.1(4) when x < z. (1) (b,M x). (5) (b,x).
2
In the case x = z, the two large branches of (b,M x) have the same maximal weight.
2
2
Applying 2 maximal splittings, we obtain 2 left maximal splittings (b,M x)⇀ l δ 1(b,x).
2 2−
This completes the proof. (cid:3)
x
Proposition 3.2. Let q N and p,p N . Let x = y > 0.
′ 0
∈ ∈ z
(cid:16) (cid:17)

<!-- Page 17 -->


## Agol Cycles Of Pseudo-Anosov Maps 17

(1) (Symmetric case.) Suppose that p > 0. Then
(b,x) = (δ 2 q δ 1− p δ 3− p ◦ ⇀ l 2q ◦ ⇀ r p )(b,M 1 p M 3 p M 2 qx) if x = z.
(2) (Asymmetric case.) Suppose that p+p > 0 (possibly p = p > 0). Then
′ ′
(b,x) = (δ 2 q δ 1− p δ 3− p′ ◦ ⇀ l 3q ◦ ⇀ r p+p′ )(b,M 1 p M 3 p′ M 2 qx) if x 6 = z.
Proof. We first prove claim (2) in the special case p = p > 0. Applying Lemma 3.1(1) in
′
the latter case x = z, we have
6
(b,M 1 p − 1 M 3 p − 1 M 2 qx)= ((δ 1 δ 3 ) − 1 ◦ ⇀ r 2 )(b,M 1 p M 3 p M 2 qx). (3.1)

### Then applying Lemma 3.1(1) again, we obtain

(b,M 1 p − 2 M 3 p − 2 M 2 qx) = ((δ 1 δ 3 ) − 1 ◦ ⇀ r 2 )(b,M 1 p − 1 M 3 p − 1 M 2 qx)
= ((δ δ ) 1 ⇀ r 2 ) ((δ δ ) 1 ⇀ r 2 )(b,M p M p M qx) (∵ (3.1))
1 3 − ◦ ◦ 1 3 − ◦ 1 3 2
= ((δ δ ) 2 ⇀ r 4 )(b,M p M p M qx). (∵ Lemma 2.6).
1 3 − ◦ 1 3 2

### Repeating this argument, we have

(b,M qx) = ((δ δ ) p ⇀ r 2p )(b,M p M p M qx). (3.2)
2 1 3 − ◦ 1 3 2
Applying Lemma 3.1(4) in the case x = z repeatedly, we have
6
3q
(b,x) = (δ q ⇀ l )(b,M qx). (3.3)
2 ◦ 2
The above equalities (3.2) and (3.3) give us
3q
(b,x) = (δ q ⇀ l )(b,M qx) (∵ (3.3))
2 ◦ 2
= (δ q ⇀ l 3q ) ((δ δ ) p ⇀ r 2p )(b,M p M p M qx) (∵ (3.2))
2 ◦ ◦ 1 3 − ◦ 1 3 2
= (δ 2 q δ 1− p δ 3− p ◦ ⇀ l 3q ◦ ⇀ r 2p )(b,M 1 p M 3 p M 2 qx). (∵ Lemma 2.6, δ 1 δ 3 = δ 3 δ 1 )
This is the desired equality in the case p = p. Next we prove claim (2) in the general case.
′
We may suppose that 0 p < p. Applying Lemma 3.1(3) repeatedly, we have
′
≤
(b,M p M p M qx) = (δ− (p′ − p) ⇀ r p′ − p )(b,M p M p′ M qx). (3.4)
1 3 2 3 ◦ 1 3 2
This together with the equalities (3.2) and (3.3) implies that
3q
(b,x) = (δ q ⇀ l )(b,M qx) (∵ (3.3))
2 ◦ 2
= (δ q ⇀ l 3q ) ((δ δ ) p ⇀ r 2p )(b,M p M p M qx) (∵ (3.2))
2 ◦ ◦ 1 3 − ◦ 1 3 2
= (δ 2 q ◦ ⇀ l 3q ) ◦ ((δ 1 δ 3 ) − p ◦ ⇀ r 2p ) ◦ (δ 3 − (p′ − p) ◦ ⇀ r p′ − p )(b,M 1 p M 3 p′ M 2 qx) (∵ (3.4))
= (δ 2 q δ 1− p δ 3− p′ ◦ ⇀ l 3q ◦ ⇀ r p+p′ )(b,M 1 p M 3 p′ M 2 qx) (∵ Lemma 2.6).

<!-- Page 18 -->


## 18 Jean-Baptistebellynckandeikokin

The proof of claim (2) is done. For the proof of claim (1), we assume x = z and use
Lemma 3.1(1)(4). This completes the proof. (cid:3)
We are ready to prove Theorem 1.2.
Proof of Theorem 1.2. Let M = M
pnM p′
nM
qn

## M

p1M p′

## 1M

q1
be the Perron-Frobenius
p 1 3 2 ··· 1 3 2
matrix associated with p . For a Perron-Frobenius eigenvector v of M , we define
n p
positive vectors x(0) := v
∈
an

## I

d x(i) := M piM
p′
iM qix(i 1) for i 1,...,n . Then x(n) =
1 3 2 − ∈ { }
M v = λ v.
p p
Suppose that p is asymmetric. By Corollaries 2.17 and 2.20, we can inductively prove
that x(i) = x(i) for all i 0,...,n . Proposition 3.2(2) tells us that
1 3
| 6 | ∈ { }
(b,x(i − 1)) = (δ 2 qiδ 1− piδ 3 − p′ i ◦ ⇀ l 3qi ◦ ⇀ r pi+p′ i)(b,x(i)) for i ∈ { 1,...,n } .

### By the above equality for i =1,2, we obtain

(b,v) = (δ 2 q1δ 1− p1δ 3 − p′ 1 ◦ ⇀ l 3q1 ◦ ⇀ r p1+p′ 1)(b,x(1))
= (δ 2 q1δ 1− p1δ 3 − p′ 1 ◦ ⇀ l 3q1 ◦ ⇀ r p1+p′ 1) ◦ (δ 2 q2δ 1− p2δ 3 − p′ 2 ◦ ⇀ l 3q2 ◦ ⇀ r p2+p′ 2)(b,x(2))
= (δ 2 q1δ 1− p1δ 3 − p′ 1δ 2 q2δ 1− p2δ 3 − p′ 2 ◦ ⇀ l 3q1 ◦ ⇀ r p1+p′ 1 ◦ ⇀ l 3q2 ◦ ⇀ r p2+p′ 2)(b,x(2)).
Repeating this argument, we finally obtain
(b,v) = (Φ 1 ⇀ l
3q1
⇀ r
p1+p′
1 ⇀ l
3qn
⇀ r
pn+p′
n)(b,λ v = x(n)).
−p p
◦ ◦ ◦···◦ ◦
This means that
(b,λ v)⇀ r
pn+p′
n⇀ l
3qn
⇀ r
p1+p′
1⇀ l
3q1
Φ (b,v),
p p
···
n
which is an Agol cycle of Φ with length (p +p +3q ).
p i=1 i ′i i
Suppose that p is symmetric. By CoroPllary 2.17 v
1
= v
3
holds. A calculation shows
| |
that x(i) = x(i) for all i 0,...,n . Applying Proposition 3.2(1), we have
1 3
| | ∈ { }
(b,x(i − 1))= (δ 2 qiδ 1− piδ 3− pi ◦ ⇀ l 2qi ◦ ⇀ r pi)(b,x(i)) for i ∈ { 1,...,n } . (3.5)
Putting the above equalities (3.5) for each i 1, ,n together, we can obtain
∈ { ··· }
(b,v) = (Φ 1 ⇀ l 2q1 ⇀ r p1 ⇀ l 2qn ⇀ r pn )(b,λ v).
−p p
◦ ◦ ◦···◦ ◦
This gives an Agol cycle of Φ with length n (p +2q ). We finished the proof. (cid:3)
p i=1 i i
Example 3.3. We present 2 examples forPAgol cycles and their total splitting numbers.
Recall that v is the normalized eigenvector with respect to λ .
p p
x
(1) For p = (1,1,1) 1 symmetric, we have v p = y for some x,y > 0 and M p v p =
∈ I x
M 1 M 3 M 2 v p = 3 2 x x + + y y . Figure11illustratesan (cid:16) Ag (cid:17) olcycle(b,λ p v p )⇀ r ⇀ l 2 Φ p (b,v p )
3x+y
(cid:18) (cid:19)

<!-- Page 19 -->


## Agol Cycles Of Pseudo-Anosov Maps 19

of Φ = δ δ δ 1 with length 3. The splitting number of each maximal splitting in
p 1 3 2−
the Agol cycle is exactly 2. Hence, we have N(Φ ) = 2 3= 6.
p
·
(2) For p = (1,2,1) asymmetric, (b,λ v )⇀ r 3 ⇀ l 3 Φ (b,v ) is an Agol cycle of
1 p p p p

## ∈ I

Φ = δ δ2δ 1 withlength6byTheorem1.2. Thesplittingnumberofeach maximal
p 1 3 2−
l
splitting in the Agol cycle is 1, except for the last maximal splitting ⇀ with the
splitting number 2. (See Figure 10(3)(4).) Hence, we have N(Φ )= 7.
p
2x+y
3x+y
r
# $ % # & %
2x+y 2x+y y
x x x x+y x x x+y x x
δ-1δ-1 δ
1 3 l l 2
2x+y 2x+y 2x+y y y
3x+y x x x x+y x x x+y x
y
(3) (4) (5) (6)
Figure 11. An Agol cycle of Φ for p = (1,1,1). (1) (b,M M M v ). (3)
p 1 3 2 p
(b,M v ). (6) (b,v ).
2 p p
Theorem 3.4. For p = (p ,p ,q ,...,p ,p ,q ) the total splitting number of an
n ′n n
n
1 ′1 1

## ∈ I

n
Agol cycle of Φ is given by N(Φ ) = (p +p +4q ).
p p i=1 i ′i i

## P

Proof. By Proposition 3.2(2) in the case of asymmetric weights, i.e. x = z, we have a
finite sequence (b,M 1 p M 3 p′ M 2 qx)⇀ r p+p′ ⇀ l 3q δ 1 p δ 3 p′ δ 2− q (b,x). The total split 6 ting number of
the finite sequence (Definition 2.3(2)) is p+p +4q. The coefficient 4 of 4q comes from
′
3
the total splitting number of a finite sequence (b,M 2 qx)⇀ l δ 2− 1(b,M 2 q − 1x) when x 6 = z.
See Figure 10. In the case of symmetric weights, i.e. x = z, Proposition 3.2(1) tells us
that there exists a finite sequence (b,M 1 p M 3 p M 2 qx)⇀ r p ⇀ l 2q δ 1 p δ 3 p δ 2− q (b,x). Its total splitting
number is 2(p+2q) = p+p+4q since the splitting number of a maximal splitting in this
finite sequence is exactly 2.
The weight of (b,M v ) is given by M v = M pnM p′ nM qn M p1M p′ 1M q1v . By the
repetition of the above
p
ar
p
gument, we can
p
pro
p
ve tha
1
t N(
3

## Φ )

2
=
···n 1
(p +
3
p +
2
4q
p
). (cid:3)
p i=1 i ′i i

## P


## Agol cycles of pseudo-Anosov maps in F


## D

We introduce positive integers S (p) and A (p) for p as follows.
i i n

## ∈ I

2p if p = 0,
i ′i
S (p)= p +2 and A (p)= 2p if p = 0,
i i i

′i i
p +p +2 otherwise.
 i ′i


<!-- Page 20 -->


## 20 Jean-Baptistebellynckandeikokin

In this section, we prove the following result.
Theorem 4.1. For p let φ F be the pseudo-Anosov map and M be the Perronn p D p

## ∈ I ∈

Frobenius matrix associated with p. Let v > 0 be an eigenvector with respect to the Perron-
Frobenius eigenvalue λ of M . Then the Agol cycle length ℓ of φ is
p p p
n (S (p)+2q ) if p is symmetric,
ℓ = i=1 i i
n (A (p)+3q ) if p is asymmetric.
(cid:26) P i=1 i i
Moreover, starting with the mPeasured train track (b
0
,µ
0
) = (b

## L

,λ
p
v), a finite subsequence
of the maximal splitting sequence
(b ,µ ) ⇀Sn(p)+2qn ⇀S1(p)+2q1 (b ,µ ) if p is symmetric,
0 0 ℓ ℓ
···
(b ,µ ) ⇀An(p)+3qn ⇀A1(p)+3q1 (b ,µ ) if p is asymmetric
0 0 ℓ ℓ
···
forms an Agol cycle of φ . The consecutive maximal splittings consist of the following left,
p
right and mixed maximal splittings
⇀Si(p)+2qi = ⇀ r ⇀ l ⇀ r pi − 1 ⇀ l ⇀ r ⇀ l 2qi − 1 ,
⇀
lr
⇀
r 2pi
−
1
⇀
l 3qi
if p = 0,
′i
⇀Ai(p)+3qi =  ⇀ lr ⇀ r 2p′ i− 1 ⇀ l 3qi if p = 0,
i
   ⇀ r ⇀ l ⇀ r pi+p′ i− 2 ⇀ l 2 ⇀ r ⇀ l 3qi − 1 otherwise.


Figure12(1)showsthemeas  uredtraintrack(b ,x)thatwasdefinedinSection1. Recall

## L

that the vector x reflects the weights of specific branches. Due to the switch condition, the
weights on all remaining branches are determined. We introduce the measured train tracks
(b ,x), (a ,x) and (s,x) in Σ as in Figure 12(2), (4) and (5) respectively. Figure 12(3)

## R ′R 0,5

gives the measured train track ∆(a ,x), where ∆ = σ σ σ σ σ σ MCG(Σ ) is the

## ′R 1 2 3 1 2 1

∈
0,5
π-rotation (Figure 12(6)).
For φ p = σ 1 pnσ 3 p′ nσ 2− qn...σ 1 p1σ 3 p′ 1σ 2− q1 ∈ F D we call the product σ 1 pjσ 3 p′ jσ 2 − qj the (j-th)
block of φ and say that the block is of type A (resp. A’) if p = 0 (resp. p = 0).
p ′j j
Otherwise, we call it a type B block.
For the proof of Theorem 4.1 we consider each block σ 1 pjσ 3
p′
jσ 2 − qj of φ p . The transition
matrix induced by σ pjσ
p′
jσ− qj is M pjM
p′
jM qj. Depending on the type of the block, con-
1 3 2 1 3 2
secutive maximal splittings of (b ,M pjM
p′
jM qjx) will result in different finite sequences.

## L 1 3 2

Figure 13 is the central tool in this paper. It illustrates how finite sequences of maximal
splittings transition one measured train track into another. The details are given in Lemmas 4.2, 4.4 and 4.5. We will see that the concatenation of suitable finite sequences gives
an Agol cycle of the pseudo-Anosov map φ .
p
x
Lemma 4.2. Let q N and p,p N . Let x = y > 0.
′ 0
∈ ∈ z
(cid:16) (cid:17)

<!-- Page 21 -->


## Agol Cycles Of Pseudo-Anosov Maps 21

y
y-x
y
’
2 4
1
(4)
1
2 4
3 1
2 4
) * + ) * +
y y
l
y
3 3 y
(3) (5)
1
, - .
2 4
y y
3
x
/
, 0 .
y y
x
/
/
x
x
/
x
/
(6)
1
2 4
3
5
’
2y
Figure 12. (1) (b ,x), (2) (b ,x), (3) ∆(a ,x), (4) (a ,x), (5) (s,x) for

## L R ′R ′R

x
x = y . (6) ∆ = σ 1 σ 2 σ 3 σ 1 σ 2 σ 1 MCG(Σ 0,5 ). Figures (4)(5) illustrate a
z ∈
left m (cid:16) ax (cid:17) imal splitting (a ,x)⇀ l (s,x) for z < y.

## ′R

(6)
(a2) (a1) 2 4 (a'3) (a'2)
(a3) 1 3 (a'1)

## A A'

(b1) (b5)
(b2) (b4)
(b3)
3
2 4
3
3
2 4
3
3
2 4
3
Figure 13. “Automaton” illustrating how the train tracks move between
topological types under the operations in Lemmas 4.2, 4.4 and 4.5. Box B
displaysLemma4.2. BoxAandA’displayLemmas4.5and4.4respectively.
(b1) Suppose that p,p > 0. Then
′
(b R ,M 1 p − 1 M 3 p′ − 1 M 2 qx)= (σ 1− 1σ 3− 1 ◦ ⇀ l ◦ ⇀ r )(b L ,M 1 p M 3 p′ M 2 qx).
(b2) Suppose that p > 0. Then
(σ 1σ 1 ⇀ r )(b ,M p M p M qx) if x = z,
(b R ,M 1 p − 1 M 3 p − 1 M 2 qx) = ( (σ 1 1 − − 1σ 3 3 − − 1 ◦ ◦ ⇀ r 2 )(b R R ,M 1 1 p M 3 3 p M 2 2 qx) if x 6 = z.
(b3) Suppose that p > p 0. Then
′
≥
(b R ,M 1 p − 1 M 3 p′ M 2 qx) = (σ 1− 1 ◦ ⇀ r )(b R ,M 1 p M 3 p′ M 2 qx).

<!-- Page 22 -->


## 22 Jean-Baptistebellynckandeikokin

(b4) Suppose that 0 p < p. Then
′
≤
(b R ,M 1 p M 3 p′ − 1 M 2 qx) = (σ 3− 1 ◦ ⇀ r )(b R ,M 1 p M 3 p′ M 2 qx).
(σ ⇀ l ⇀ r ⇀ l )(b ,M qx) if x = z,
(b5) (b L ,M 2 q − 1x)= ( (σ 2 ◦ ⇀ l 2 ◦ ⇀ r ◦ ⇀ l 2 )( R b ,M 2 qx) if x = z.

## 2 ◦ ◦ ◦ R 2 6

2
(σ ⇀ l )(b ,M qx) if x = z,
(6) (b L ,M 2 q − 1x)=  (σ 2 ◦ ⇀ l 3 )(b L ,M 2 qx) if x = z.

##  2 ◦ L 2 6


Proof. Figure 14 shows that (b L ,M 1 M 3 a = a+ b b )⇀ r ⇀ l σ 1 σ 3 (b R ,a) for a = a b > 0. In
b+c c
other words, (b R ,a) = (σ 1− 1σ 3− 1 ◦ ⇀ l ◦ ⇀ r )(b L (cid:16) ,M 1 M (cid:17) 3 a). Choosing a = M 1 p − 1 M (cid:16) 3 p′ − (cid:17)1 M 2 qx as
a positive vector, we obtain claim (b1).
a
6
4 6
6 4
6
b
7
l 1 3
a 4 ; 6
; 6 4 b
a
a
4
6
4
;
6
6
6
a
6 4 b
6
; 6 4 b
6
a
< = b
6 :
89
:
89
6
a < =
b
6
(1) (2) (3) (4)
Figure 14. Proof of Lemma 4.2(b1). (1) (b ,M M a). (4) (b ,a).

## L 1 3 R

It is enough to prove the remaining claims when q = 1. For claim (b2), we set (b ,µ )=
0 0
(b ,M p M p M x). The proof is similar to that of Lemma 3.1(1). Figure 15 illustrates the

## R 1 3 2

proof of (b2) when x < z. In the case x = z, the two large branches of (b ,M p M p M x)

## R 1 3 2

have the same weight. (c.f. Figure 15(1).) Applying a maximal splitting, we obtain the
right maximal splitting (b R ,M 1 p M 3 p M 2 x)⇀ r σ 1 σ 3 (b R ,M 1 p − 1 M 3 p − 1 M 2 x). This completes the
proof of claim (b2).
Theproofofclaim(b3)(resp. (b4))issimilartothatofLemma3.1(2)(resp. Lemma3.1(3))
and we omit the proof.
Beforeprovingclaim (b5),wefirstproveclaim(6). Weconsiderthemeasuredtraintrack
x
(b 0 ,µ 0 ) = (b L ,M 2 x = x+y+z ) when x = z. We may suppose that x < z. Applying 3
z 6
maximal splittings (see(cid:16)Figure(cid:17)16(1)–(4)), we have 3 left maximal splittings
(b ,µ )= (b ,M x)⇀ l (b ,µ )= (s,M x)⇀ l (b ,µ )⇀ l (b ,µ )= σ 1(b ,x). (4.1)
0 0 L 2 1 1 2 2 2 3 3 2− L
This gives claim (6) when x <z.

<!-- Page 23 -->


## Agol Cycles Of Pseudo-Anosov Maps 23

py'+z
-1 -1
y' r r 1 3
y'
2y' x+py'
(1)
> >
(p-1)y'+z
py'+z (p-1)y'+z (p-1)y'+z
y' y' y'
y' y' y'
x+py' 2y' (p+1)y'+z 2y' x+(p-1)y' 2y'
x+(p-1)y'
(2) (3) (4)
Figure 15. Proof of Lemma 4.2(b2) when x < z. (1) (b ,M p M p M x).

## R 1 3 2

(4) (b R ,M 1 p − 1 M 3 p − 1 M 2 x).
We turn to the case x = z. Applying 2 maximal splittings, we obtain 2 left maximal
splittings
(b ,µ )= (b ,M x)⇀ l (b ,µ )= (s,M x)⇀ l (b ,µ ) = σ 1(b ,x).
0 0 L 2 1 1 2 2 2 2− L
This gives the proof of claim (6) when x = z.
We finally prove claim (b5). Consider the measured train track (b ,µ ) = (b ,M x)

## 0 0 R 2

when x = z. We may suppose that x < z. Figures 16(1’)–(3’) and (2) show that (b ,µ )=
0 0
6
2
(b ,M x)⇀ l ⇀ r (s,M x). Taking the last two maximal splittings from the finite sequence

## R 2 2

2
(4.1), we have (s,M x)⇀ l σ 1(b ,x). Putting them together, we have

## 2 2− L

2 2
(b ,µ ) = (b ,M x)⇀ l ⇀ r (s,M x) ⇀ l σ 1(b ,x).

## 0 0 R 2 2 2− L

This gives claim (b5) when x < z.
In the case x = z, the measured train track (b ,M x) has two large branches with

## R 2

maximal weight. This gives the finite sequence (b ,M x)⇀ l ⇀ r (s,M x) ⇀ l σ 1(b ,x).

## L 2 2 2− L


### This completes the proof. (cid:3)

Let (b ,M p M p M qx) be a measured train track, where the measure M p M p M qx is pre-

## L 1 3 2 1 3 2

ceded by a type B block. By repeatedly applying the last lemma, we now compute the
maximal splittings of (b ,M p M p M qx).

## L 1 3 2

x
Proposition 4.3 (Type B block). Let p,p,q N. Let x = y > 0.
′
∈ z
(cid:16) (cid:17)
(1) (Symmetric case.) (b L ,x) = (σ 2 q σ 1− p σ 3− p ◦ ⇀p+2+2q)(b L ,M 1 p M 3 p M 2 qx) if x = z.
The consecutive maximal splittings consist of the following left and right maximal
splittings
⇀p+2+2q = ⇀ l 2q − 1 ⇀ r ⇀ l ⇀ r p − 1 ⇀ l ⇀ r .
◦ ◦ ◦ ◦ ◦

<!-- Page 24 -->


## 24 Jean-Baptistebellynckandeikokin

z z
x+y+z l l l
x+y+z y y
x x x
(1) (2) (3) (4) (5)
?
2

## E F G


## Ab


## Cb


## D


## H G I


## F


## Ab


## Cb D


## G H G E I

@
x

## E F G H G I ?

y

## Ab


## Cb D

x y
?
y

## E F G H G I


## F G H G E I


## J K L

x
x+y x+y

## H M


## H M

(1')

## E F G H G I


## E H M F


## I


## G H G E I

l
(2')

## H M


## N O P F


## I


## H M


## G H G E I

x+y

## E F G H G I

l
x
(3')

## H M


## I


## H M

y+x
x+y
2y

## E F G H G I


## F G H G E I

r
Figure 16. (1)–(5) Proof of Lemma 4.2(6) when x < z. (1’)–(3’)(2)–(5)
Proof of Lemma 4.2(b5) when x < z.
(2) (Asymmetric case.) (b L ,x) = (σ 2 q σ 1− p σ 3− p′ ◦ ⇀p+p′+2+3q)(b L ,M 1 p M 3 p′ M 2 qx) if x 6 = z,
possibly p = p. The consecutive maximal splittings consist of the following left and
′
right maximal splittings
⇀p+p′+2+3q = ⇀ l 3q − 1 ⇀ r ⇀ l 2 ⇀ r p+p′ − 2 ⇀ l ⇀ r .
◦ ◦ ◦ ◦ ◦
Proof. We prove claim (2). Suppose that x = z. We may assume that p < p. (The proof
′
6
for the case p p can be treated in the same manner.) We have
′
≥
(b R ,M 1 p − 1 M 3 p′ − 1 M 2 qx) = (σ 1− 1σ 3− 1 ◦ ⇀ l ◦ ⇀ r )(b L ,M 1 p M 3 p′ M 2 qx) (Lemma 4.2(b1)),
(b R ,M 1 p − 1 M 3 p − 1 M 2 qx) = (σ 3 − (p′ − p) ◦ ⇀ r p′ − p )(b R ,M 1 p − 1 M 3 p′ − 1 M 2 qx) (Lemma 4.2(b4)),
(b R ,M 2 qx) = ((σ 1 σ 3 ) − (p − 1) ◦ ⇀ r 2p − 2 )(b R ,M 1 p − 1 M 3 p − 1 M 2 qx) (Lemma 4.2(b2)),
3(q 1) 2 2
(b ,x) = (σ q ⇀ l − ⇀ l ⇀ r ⇀ l )(b ,M qx) (Lemma 4.2(b5),(6)).

## L 2 ◦ ◦ ◦ ◦ R 2


### By the above equalities together with Lemma 2.6, we obtain

(b L ,x) = (σ 2 q σ 1− p σ 3− p′ ◦ ⇀ l 3q − 1 ◦ ⇀ r ◦ ⇀ l 2 ◦ ⇀ r p+p′ − 2 ◦ ⇀ l ◦ ⇀ r )(b L ,M 1 p M 3 p′ M 2 qx).
This completes the proof of (2). The proof of claim (1) is left to the reader. (cid:3)
x
Lemma 4.4. Let q,s N. Let x = y > 0.
∈ z
(cid:16) (cid:17)
(a’1) (a ,Ms 1M qx)= (σ 1 ⇀ r ⇀ lr )(b ,MsM qx).

## ′R 3− 2 3− ◦ ◦ L 3 2


<!-- Page 25 -->


## Agol Cycles Of Pseudo-Anosov Maps 25

(a’2) (a ,Ms 1M qx)= (σ 1 ⇀ r 2 )(a ,MsM qx).

## ′R 3− 2 3− ◦ ′R 3 2

3
(a’3) (b L ,M 2 q − 1x)= (σ 2 ◦ ⇀ l )(a ′R ,M 2 qx) if x 6 = z.
Proof. It is sufficient to prove the lemma when q = 1. Consider the maximal splitting
x
starting from (b ,MsM x = y′ ), where y = x+y+z. Figure 17 shows that

### L 3 2 sy′+z ′

(cid:18) (cid:19)
sy'+z
y' σ 3 -1 r
y'
x

## Q

(s-1)y'+z
y'
y'
y'
y+z
(1) (2) (3) (4)

## Q

sy'+z (s-1)y'+z
y'
y+z
y'

## Q

(s-1)y'+z
lr
y'
sy'+z
Figure 17. Proof of Lemma 4.4(a’1). (1) (b ,MsM x).

## L 3 2

(4) (a ,Ms 1M x).

## ′R 3− 2

(a ,Ms 1M x) = (⇀ r σ 1 ⇀ lr )(b ,MsM x)= (σ 1 ⇀ r ⇀ lr )(b ,MsM x).
′R 3− 2 ◦ 3− ◦ L 3 2 3− ◦ ◦ L 3 2
The proof of claim (a’1) is done. For the proof of claim (a’2), see Figure 18.
(s-1)y'+z (s-1)y'+z
sy'+z sy'+z sy'+z (s-1)y'+z
y' r y' r y' σ 3 -1 y'
y' y' y' y'
x x x x
(1) (2) (3) (4)
x
Figure 18. ProofofLemma4.4(a’2). (1)(a ,MsM x = y′ ), where
′R 3 2 sy′+z
(cid:18) (cid:19)
y = x+y+z. (4) (a ,Ms 1M x).

## ′ ′R 3− 2

We prove claim (a’3). Consider the measured train track (a ,M x). We may suppose

## ′R 2

thatx < z. Applying3maximalsplittingsconsecutively,weobtain3leftmaximalsplittings
2
(a ,M x)⇀ l (s,M x)⇀ l σ 1(b ,x). See Figure 19. We finished the proof. (cid:3)

## ′R 2 2 2− L

Recall that ∆ = σ σ σ σ σ σ is the π-rotation (Figure 12(6)).
1 2 3 1 2 1
Lemma 4.5. Let q,s N. Let x = x y > 0 and J = 0 0 0 1 1 0 .
∈ z 1 0 0
(cid:16) (cid:17) (cid:16) (cid:17)

<!-- Page 26 -->


## 26 Jean-Baptistebellynckandeikokin

z 2x+y+z z 2x+y+z z y z z
x+
y+ l
x+
y+
x+y
l
x+y
l σ 2
zx+
y+
z
y+z
z x+
y+
z
x+
y+
z
y y
x x x+y+2z x y x y x
(1) (2) (3) (4) (5)
Figure 19. Proof of Lemma 4.4(a’3). (1) (a ,M x). (2) (s,M x). (4)

## ′R 2 2

(b ,x).

## L

(a1) ∆(a ,Ms 1M q Jx)= (σ 1 ⇀ r ⇀ lr )(b ,MsM qx).

## ′R 3− 2 1− ◦ ◦ L 1 2

(a2) ∆(a ,Ms 1M q Jx)= (σ 1 ⇀ r 2 ∆)(a ,MsM q Jx).

## ′R 3− 2 1− ◦ ◦ ′R 3 2

3
(a3) (b L ,M 2 q − 1x)= (σ 2 ◦ ⇀ l ◦ ∆)(a ′R ,M 2 q Jx) if x 6 = z.
Proof. Observe that ∆(b ,MsM q Jx) = (b ,MsM qx). By ∆σ 1 = σ 1∆ for the pair

### L 3 2 L 1 2 i± j±

(i,j) = (1,3) or (3,1), the proof is analogous to that of Lemma 4.4. (cid:3)
Let (b ,MsM qx) or (b ,MsM qx) be a measured train track, where the measures are

## L 1 2 L 3 2

preceded by a type A and A’ block respectively. We now compute the maximal splittings
of the measured train tracks.
x
Proposition 4.6 (Type A/A’ block for (1)/(2)). Let q,s N. Let x = y > 0.
∈ z
(cid:16) (cid:17)
(1) (b L ,x) = (σ 2 q σ 1− s ◦ ⇀ l 3q ◦ ⇀ r 2s − 1 ◦ ⇀ lr )(b L ,M 1 sM 2 qx).
(2) (b ,x) = (σ q σ s ⇀ l 3q ⇀ r 2s − 1 ⇀ lr )(b ,MsM qx).

## L 2 3− ◦ ◦ ◦ L 3 2

Proof. By a similar argument as in the proof of Proposition 4.3, one can prove claims (1)
and (2). In the case of Proposition 4.3, we used Lemma 4.2. For the proof of (1) (resp.
(2)), we use Lemma 4.5 (resp. Lemma 4.4) together with Lemma 4.2(6). (cid:3)
Proof of Theorem 4.1. AsintheproofofTheorem1.2,foraPerron-Frobeniuseigenvectorv
of M we define positive vectors x(0) := v and x(i) := M piM
p′
iM qix(i 1) for i 1,...,n .
p 1 3 2 − ∈{ }
Suppose that p is asymmetric. By Propositions 4.3(2) and 4.6, we have
(b L ,x(i − 1)) = (σ 2 qiσ 1− piσ 3 −
p′
i ◦ ⇀Ai+3qi)(b L ,x(i)) for i ∈{ 1,...,n } ,
where A = A (p) is the positive integer defined in Section 1. This gives us
i i
(b ,v = x(0)) = (φ 1 ⇀A1+3q1 ⇀An+3qn)(b ,λ v = x(n)).
L −p L p
◦ ◦···◦

### This means that

(b ,µ ) = (b ,λ v) ⇀An+3qn ⇀A1+3q1 φ (b ,v) = (b ,µ )
0 0 L p p L ℓ ℓ
···

<!-- Page 27 -->


## Agol Cycles Of Pseudo-Anosov Maps 27

is an Agol cycle of φ
p
with length ℓ. The consecutive A
i
+3q
i
maximal splittings ⇀Ai+3qi
are given by Proposition 4.3(2) when the i-th block of φ is of type B. The maximal
p
splittings are given by Propositions 4.6 when the i-th block is of type A or A.
′
The proof of the theorem when p is symmetric is left to the reader. (cid:3)
Example 4.7. We present 2 examples for Agol cycles and their total splitting numbers.
(1) For p = (1,2,1) asymmetric, an Agol cycle of φ is given by
1 p

## ∈ I

2 2
(b ,λ v )⇀ r ⇀ l ⇀ r ⇀ l ⇀ r ⇀ l φ (b ,v )

### L p p p L p

whose length is 8. The splitting number of each maximal splitting is 1, except for
r
the firstmaximal splitting ⇀ whose splitting numberis 2 (Figure 14(1)(2)). Hence,
we have N(φ ) = 9.
p
(2) For p = (1,0,1,0,1,1) asymmetric, an Agol cycle of φ is given by
2 p

## ∈ I

3 3
(b ,λ v )⇀ lr ⇀ r ⇀ l ⇀ lr ⇀ r ⇀ l φ (b ,v ),

### L p p p L p

whose length is 10. The splitting number of each maximal splitting is 1, except for
lr
the 2 mixed maximal splittings ⇀, whose splitting number is 2 (Figure 17(1)(2)).
Hence, we have N(φ ) =12.
p
Theorem 4.8. For p the total splitting number of an Agol cycle of φ is given by
n p
We have N(φ )= n ∈ (A I (p)+4q ).
p i=1 i i

## P

Proof. For each finite sequence of maximal splittings given by Propositions 4.3 and 4.6, we
compute its total splitting number. For instance, take a finite sequence
(b L ,M 1 piM 2 qix)⇀ lr ⇀ r 2pi − 1 ⇀ l 3qi σ 1 piσ 2− qi(b L ,x)
given by Proposition 4.6(1). Counting the large branches with maximal weight in each
maximal splitting, one sees that its total splitting number is 2p +4q (= A (p)+4q ). One
i i i i
can prove the total splitting number of the Agol cycle for φ given by Theorem 4.1 equals
p
the sum of A (p)+4q over i, that is n (A (p)+4q ). (cid:3)
i i i=1 i i

## P

Proof of Theorem 1.3. Theorems 3.4 and 4.8 immediately give the desired statement. (cid:3)

## Conjugacy classes of pseudo-Anosov maps in F and F


## T D

In the final section we classify conjugacy classes of pseudo-Anosov maps in the semigroups F and F . To do this, we define maps T : N3n N3n, called the shift, and
f :N3n T N3n, ca D lled the flip, as follows. For p = (p ,p , 0 q , → ...,p 0 ,p ,q ) N3n
0 → 0 n ′n n 1 ′1 1 ∈ 0
T(p) = (p ,p ,q ,...,p ,p ,q ,p ,p ,q ),
n 1 ′n 1 n 1 1 ′1 1 n ′n n
− − −
f(p) = (p ,p ,q ,...,p ,p ,q ).
′n n n ′1 1 1

<!-- Page 28 -->


## 28 Jean-Baptistebellynckandeikokin

The shift T permutes by three entries and the flip f interchanges p and p for all i
i ′i
∈
1,...,n . Note that p is symmetric if and only if the flip f preserves p, i.e. f(p) = p.
{ }
Let p and t . We write p t if n = m and Tk(p) t,f(t) for some k 0.
n m

## ∈ I ∈ I ∼ ∈ { } ≥

Theorem 5.1. Let p and t . The following are equivalent.
n m

## ∈ I ∈ I

(1) p t.
∼
(2) Φ and Φ are conjugate in MCG(Σ ).
p t 1,2
(3) φ and φ are conjugate in MCG(Σ ).
p t 0,5
Proof. Suppose that p t. This means that Tk(p) = t or Tk(p) = f(t) for some k 0.
∼ ≥
By the definition of the shift T, Φ and Φ (resp. φ and φ ) are conjugate. Note
p T(p) p T(p)
that Φ and Φ (resp. φ and φ ) are also conjugate. In this case, a conjugacy is
p f(p) p f(p)
given by F (resp. ∆), where F : Σ Σ is the π-rotation along the simple closed
1,2 1,2
→
curve c (Figure 2(1)).
2
Thus the condition (1) implies the conditions (2) and (3).
To see the that (2) implies (1), suppose that Φ and Φ are conjugate in MCG(Σ ).
p t 1,2
By Theorem2.5 their periodicsplitting sequences arecombinatorially isomorphicandtheir
Agol cycle lengths are equal. Notice that by Theorem 1.2 p is symmetric if and only if t
is symmetric. We now prove that p t when both p and t are asymmetric. (The proof
∼
for the symmetric case is analogous.) Let ℓ be the Agol cycle lengths of Φ and Φ . For
p t
p = (p ,p ,q ,...,p ,p ,q ) and t = (t ,t ,u ,...,t ,t ,u ) , Theorem 1.2
n ′n n 1 ′1 1

## ∈ I

n m ′m m 1 ′1 1

## ∈ I

m
tells us that
(b,λ v )⇀ r
pn+p′
n⇀ l
3qn
⇀ r
p1+p′
1⇀ l
3q1
Φ (b,v ),
p p p p
···
(b,λ v )⇀ r
tm+t′
m⇀ l
3um
⇀ r
t1+t′
1⇀ l
3u1
Φ (b,v )
t t t t
···
form Agol cycles of Φ and Φ respectively. This together with Remark 2.7 implies that
p t
the cyclically ordered sets (p +p ,3q ),...,(p +p ,3q ) and (t +t ,3u ),...,(t +
{
n ′n n 1 ′1 1
} {
m ′m m 1
t ,3u ) have to be equal. In particular, n = m. Up to the shift T, we may assume that
′1 1
}
( ) p,t satisfy p +p = t +t and q = u for i= 1,...,n.

## ∗ ∈ I

n i ′i i ′i i i
The following three cases can occur.
Case 1. p = t (and p = t ) for i = 1,...,n.
i i ′i ′i
Case 2. p = t (and p = t ) for i = 1,...,n.
i ′i ′i i
Case 3. Otherwise,.
In case 1 (resp. case 2) we have p = t (resp. p = f(t)). In both cases it holds p t. We
∼
will later show that case 3 cannot occur.
Claim 1. Let(b,x)beameasuredtraintrackinΣ asinFigure2(3). Leth :Σ Σ
1,2 1,2 1,2
be an orientation-preserving diffeomorphism preserving the train track b. Then h(b→ ,x) =
(b,x) or h(b,x) = (b,Jx), where J is the matrix as in Lemma 4.5.

<!-- Page 29 -->


## Agol Cycles Of Pseudo-Anosov Maps 29

Proof of Claim 1. Let ι : Σ Σ be the hyperelliptic involution, exchanging the two
1,2 1,2
punctures. LetF : Σ Σ → betheπ-rotationasabove. Thenι(b,x) = (b,x),F(b,x) =
1,2 1,2
(b,Jx) and F ι(b,x) → = (b,Jx). Consider any orientation-preserving diffeomorphism
h : Σ Σ ◦ preserving the train track b. Since large branches are mapped to large
1,2 1,2
→
branches under h, we observe that h is either the identity map 1, ι, F or F ι = ι F.
◦ ◦
This completes the proof.
We turn to case 3. For p let v be the normalized eigenvector of M given in
n p p

## ∈ I

Theorem 2.13. If case 3 occurs, we have s +s = 1 by Corollary 2.16(2) and s = s by
p t p t
6 6
Corollary 2.16(3). In particular, v = Jv and v = v . But since by Claim 1, the only
p t p t
6 6
possible diffeomorphisms are 1, ι, F or F ι = ι F, a diffeomorphism h :Σ Σ with
1,2 1,2
h(b,v ) = (b,cv ) for some constant c > ◦ 0 cann ◦ ot exist. The periodic splittin → g sequences
p t
of Φ and Φ are not combinatorially isomorphic because they do not satisfy the condition
p t
(2) in Definition 2.4. Therefore, Φ and Φ arenot conjugate to each other by Theorem 2.5.
p t
This contradicts the assumption that Φ and Φ are conjugate. Thus case 3 does not occur
p t
and the condition (2) implies the condition (1).
To see that (3) implies (1), suppose that φ and φ are conjugate in MCG(Σ ). For
p t 0,5
the 2-fold branched cover Σ Σ their lifts Φ and Φ are conjugate in MCG(Σ ).
1,2 0,5 p t 1,2
→
Then p t by the above argument. This completes the proof. (cid:3)
∼

### Acknowledgement

Thefirstauthor would like to thank the organizers of the FrontierLab program at Osaka
University. The program made it possible for the author to conduct research in Japan.
Without it, the paper could not have been written. The second author’s research was
supported by JSPS KAKENHI Grant Numbers JP21K03247, JP22H01125, JP23H0101.

### References

[1] Ian Agol, Ideal triangulations of pseudo-Anosov mapping tori, Topology and geometry
in dimension three, Contemp. Math., vol. 560, Amer. Math. Soc., Providence, RI, 2011,
arXiv:1008.1606, doi:10.1090/conm/560/11087, pp. 1–17.
[2] Ian Agol and Chi Cheuk Tsang, Dynamics of veering triangulations: infinitesimal components of their flow graphs and applications, Algebraic and Geometric Topology, to
appear, arXiv:2201.02706.
[3] M. Bestvina and M. Handel, Train-tracks for surface homeomorphisms, Topology 34
(1995), no. 1, 109–140, doi:110.1016/0040-9383(94)E0009-9.
[4] F. R. Gantmacher, The theory of matrices. Vols. 2, Chelsea Publishing Co., New York,
1959, doi:110.1007/978-3-642-99234-6.
[5] Craig D. Hodgson, Ahmad Issa, and Henry Segerman, Non-geometric veering triangulations, Exp. Math. 25 (2016), no. 1, 17–45, arXiv:1406.6439.
[6] Keiko Kawamuro and Eiko Kin, Complete description of agol cycles of pseudo-anosov
3-braids, preprint: arXiv:2312.04486v1.

<!-- Page 30 -->


## 30 Jean-Baptistebellynckandeikokin

[7] Ron. Knott, An introduction to continued fractions,
https://r-knott.surrey.ac.uk/Fibonacci/cfINTRO.html.
[8] R. C. Penner and J. L. Harer, Combinatorics of train tracks, Annals of Mathematics Studies, vol. 125, Princeton University Press, Princeton, NJ, 1992,
doi:10.1515/9781400882458.
[9] Robert C. Penner, A construction of pseudo-Anosov homeomorphisms, Trans. Amer.
Math. Soc. 310 (1988), no. 1, 179–197, doi:10.1090/S0002-9947-1988-0930079-9.
DepartmentofMathematics,Ludwig-Maximilians-UniversityMunich,80333Munich,Theresienstr. 39, Germany

### Email address: j.bellynck@campus.lmu.de

Center for Education in Liberal Arts and Sciences, Osaka University, Toyonaka, Osaka
560-0043, Japan
Email address: kin.eiko.celas@osaka-u.ac.jp

## Tables

**Table (Page 3):**

|  |  |
|---|---|
| c 1 | c 2 |
| c 3 |  |


**Table (Page 8):**

| h p,1 qn squares | w p,1 |  | q n-1squares |
|---|---|---|---|
|  |  |  |  |


**Table (Page 8):**

|  | h T(p),1 qn-1squares |  |  |  | q n-2squares |
|---|---|---|---|---|---|
|  |  | w T |  | (p),1 |  |


**Table (Page 8):**

|  | a2 squares | a 3 squares |
|---|---|---|
|  |  |  |


**Table (Page 8):**

| h p,1 qn squares | w p,1 | q n-1squares |
|---|---|---|
|  |  |  |


**Table (Page 12):**

| y x |
|---|
| x y z z y |


**Table (Page 15):**

| y' x+py' y' |
|---|
| )y'+z |


**Table (Page 15):**

| y' x+(p- |  |  |
|---|---|---|
|  | x+(p- | 1)y' |
| y' |  |  |
| )y'+z |  |  |


**Table (Page 16):**

| y' x+(p- |  |  |
|---|---|---|
|  | +(p- | 1)y' |
| y' p'y'+z |  |  |


**Table (Page 19):**

| 2x+y x |
|---|
| 2x+y |
| x |


**Table (Page 21):**

|  |  |
|---|---|
| (6) 2 4 1 3 |  |
|  |  |
