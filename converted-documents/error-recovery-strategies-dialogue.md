---
title: "Error Recovery Strategies Dialogue"
original_file: "./Error_Recovery_Strategies_Dialogue.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag", "dialogue"]
keywords: ["cid", "critical", "theorem", "colors", "coloring", "weakly", "graph", "let", "mpd", "then"]
summary: "<!-- Page 1 -->

4202
guA
92
]OC.htam[
1v93761.8042:viXra

## On Criticality And Additivity Of The


## Pseudoachromatic Number Under Join


## Jonathan Meddaugh, Mark R. Sepanski, Yegnanarayanan


## Venkataraman

Abstract. Avertexcoloringofa graphis saidtobe pseudocomplete if, for any two distinct colors, there exists at least one edge
with those two colors as its end vertices."
related_documents: []
---

# Error Recovery Strategies Dialogue

<!-- Page 1 -->

4202
guA
92
]OC.htam[
1v93761.8042:viXra

## On Criticality And Additivity Of The


## Pseudoachromatic Number Under Join


## Jonathan Meddaugh, Mark R. Sepanski, Yegnanarayanan


## Venkataraman

Abstract. Avertexcoloringofa graphis saidtobe pseudocomplete if, for any two distinct colors, there exists at least one edge
with those two colors as its end vertices. The pseudoachromatic
number of a graph is the greatest number of colors possible used
in a pseudocomplete coloring. This paper studies properties relating to additivity of the pseudoachromatic number under the join.
Errorsfromthe literuature are correctedandthe notionof weakly
critical is introduced in order to study the problem.

### Contents


## Introduction 1


## Initial Definitions and Background 2


## Criticality and Additivity of Ψ Under Joins 4


## Weak Criticality 7


## Remarks on ∇kG 12

Acknowledgments 15

### References 15


## Introduction

Some of the oldest problems in graph theory study colorings subject
to various constraints. A coloring of the vertices of a graph is called
pseudocomplete if every pair of disjoint colors are adjacent via at least
one edge. The maximum possible number of colors used in a pseudocomplete coloring of a graph G is called the pseudoachromatic number,
Date: August 30, 2024.
2020 Mathematics Subject Classification. Primary: 05C15; Secondary: 05C76.
Key words and phrases. pseudocomplete, pseudoachromatic number, critical,
weakly critical, join.
Communicating author: Y. Venkataraman.
1

<!-- Page 2 -->


## 2 Meddaugh,Sepanski,Venkataraman

Ψ(G). Though not studied here, requiring the coloringsbe proper gives
rise to the well studied achromatic number, e.g., [12].
The pseudoachromatic number was first used by Harary et al., [13],
and Gupta, [11]. See [16] for additional comments on the origin of the
name. For some of the history of work on Ψ, see the following: [15],
[8], [6], [21], [10], [17], [18], [9], [19], [20], [14], [3], [4], [1], [2], and [5].
Initial definitions and background results are found in Section §2,
including the definition of criticality, Definition 2.5, which plays a role
in some aspects of Ψ being additive under join.
Section §3 examines additivity of Ψ and preservation of criticality
under the join. On this front, for graphs G and H, there is an error in
the literature that claims that G and H are critical if and only if

## (1.1) Ψ(G∇H) = Ψ(G)+Ψ(H).

Though sufficient (Theorem 3.3), in fact, the converse is not true, see
Remark 3.4. Similarly (Theorem 3.5), when G and H are critical, so
is G∇H, though the converse is also false, see Remark 3.6. Finally
apriori bounds and structural results are given in Theorems 3.1 and
3.7.
Section §4 introduces the notion of weakly critical in Definition 2.5.
A graph invariant equivalence is given in Theorem 4.3 and a structural
equivalence is given in Theorem 4.5. One of the main results of this
paper, Theorem 4.7, shows that Equation 1.1 implies that either G or
H is weakly critical.
Section §5 studies the above topics in the context of ∇kG. For k ≥
2, Theorem 5.3 shows that ∇kG is critical precisely when k(ω(G) +
|V|) is even. More generally, Theorem 5.5 shows that ∇kG is always
weakly critical. Finally, additivity or near-additivity of Ψ on ∇kG is
determined in Theorems 5.4 and 5.6.

## Initial Definitions and Background

We write N for the nonnegative integers and Z+ for the positive
integers. In this paper, G = (V,E) is a simple, finite graph. If multiple
graphs may lead to ambiguity, we will write G = (V ,E ). If the

## G G

vertices of G are equipped with a labeling by some C ⊆ Z, we generally
write ℓ : V ։ C for the coloring. Finally, we write ω for the clique
number and ∇ for the graph theoretic join.
We begin with one of the central definitions of the paper.
Definition 2.1. A pseudocomplete coloring of a graph G is a coloring
of the vertices of G, ℓ : V → C, so that, for any distinct i,j ∈ C, there

<!-- Page 3 -->


## Criticality, Additivity, Join, Pseudoachromatic Number 3

exists uv ∈ E so that {i,j} = {ℓ(u),ℓ(v)}. Note that the coloring here
need not be proper.
The pseudoachromatic number of a graph G, written Ψ(G), is the
greatest possible number of colors employed in a pseudocomplete coloring of G.
If K is a maximal clique of G, then coloring K with distinct colors and the rest of G arbitrarily gives a pseudocomplete coloring. In
addition, the defintion of a pseudocomplete coloring requires at least
Ψ(G) ≤ |E|. As a result,
2
(cid:0) (cid:1)

## 1+ 1+8|E|

ω(G) ≤ Ψ(G) ≤ .
p2
Moreover importantly, the following upper bound is known.
Lemma 2.2 ([7], Lemma 2). Let G be a graph. Then
ω(G)+|V|

## Ψ(G) ≤ .

(cid:22) 2 (cid:23)
In addition, there is a lower bound for Ψ of the join of graphs.
Lemma 2.3 ([7], Corollary 4). Let G and H be graphs. Then

## Ψ(G)+Ψ(H) ≤ Ψ(G∇H).

Determining when the inequalities in Lemmas 2.2 and 2.2 become
equalities leads to the following definitions.
Definition 2.4. Let G be a graph and k ∈ N with k ≤ |V|. Define the
minimal psi-drop function as
mpd (k) = min{Ψ(G)−Ψ(G\X) | X ⊆ G,|X| = k}.

## G

If X ⊆ G satifies |X| = k and mpd (k) = Ψ(G)−Ψ(G\X), we call

## G

X a realizing subgraph for mpd (k).

## G

Note that 0 ≤ mpd (k) ≤ k as Ψ can drop by at most one when

## G

removing a vertex.
The next definition is a reformulation of the one found in [7].
Definition 2.5. We say G is critical if
k
mpd (k) ≥

### G (cid:24)2(cid:25)

for all 0 ≤ k ≤ |G|.
There is a useful known equivalence for criticality in terms of maximizing the inequality in Lemma 2.2 without the floor function.

<!-- Page 4 -->


## 4 Meddaugh,Sepanski,Venkataraman

Lemma 2.6 ([7], Lemma 10). Let G be a graph. Then G is critical if
and only if
ω(G)+|V|

## Ψ(G) = .

2

## Criticality and Additivity of Ψ Under Joins


### We begin with an apriori bound on Ψ(G∇H) between a minimal

sum involving a clique number and vertex count and an average sum
of clique numbers and vertex counts.
Theorem 3.1. Let G and H be graphs. Let
m = min{ω(G)+|V |, ω(H)+|V |}.

## H G


### Then

ω(G)+ω(H) |V |+|V |
m ≤ Ψ(G∇H) ≤ + G H .
(cid:22) 2 2 (cid:23)
Proof. The upper bound comes from Lemma 2.2 and the additivity of
ω under join.
For the lower bound, let K and K be maximal cliques of G and

## G H

H, respectively. Color K and K with ω(G)+ω(H) distinct colors.

## G H

Let X = G\K and X = H\K . After relabeling, we may assume

## G G H H

that
|V |−ω(G) = |X | ≤ |X | = |V |−ω(H).

## G G H H

Color both X and X with an additional identical |V |−ω(G) colors.

## G H G

It is straightforward to verify that this is a pseudocomplete coloring of

### G∇H with

(ω(G)+ω(H))+(|V |−ω(G)) = ω(H)+|V |

## G G

colors. After noting that ω(H)+|V | ≤ ω(G)+|V |, we are done. (cid:3)

## G H

Next we give a criteria for Ψ to be additive over the join.
Theorem 3.2. Let G,H be graphs. Then

## Ψ(G∇H) = Ψ(G)+Ψ(H)

if and only if
mpd (k)+mpd (k) ≥ k

## G H

for all 0 ≤ k ≤ min{|G|,|H|}.
Moreover, in that case, there exists a k, 1 ≤ k ≤ min{|G|,|H|}, so
that
mpd (k)+mpd (k) = k.

## G H


<!-- Page 5 -->


## Criticality, Additivity, Join, Pseudoachromatic Number 5

Proof. Let ℓ be a pseudocomplete coloring of G∇H with Ψ(G∇H)
colors. Let C = ℓ(V ) ∩ ℓ(V ). By recoloring if necessary, we may

## G H

assume that every color in C appears exactly once in G and once in
H. Define induced subgraphs of G and H by X = ℓ−1(C)∩V and

## G G

X = ℓ−1(C)∩V , respectively. We see that |C| = |X | = |X |. Note

## H H G H

thatℓ restricted toG\X ispseudocomplete andsatisfies |ℓ(G\X )| =

## G G

Ψ(G\X ) (and similar for H \X ). By construction, it follows that

## G H


## Ψ(G∇H) = Ψ(G\X )+|C|+Ψ(H \X ).


## G H

From the observations that Ψ(G) ≥ Ψ(G \ X ) + mpd (|C|) and

## G G

Ψ(H) ≥ Ψ(H \X )+mpd (|C|), it follows that

## H H

Ψ(G)+Ψ(H) ≥ Ψ(G\X )+Ψ(H \X )+mpd (|C|)+mpd (|C|)

## G H H G

so that
Ψ(G)+Ψ(H) ≥ Ψ(G∇H)+(mpd (|C|)+mpd (|C|)−|C|).

## H G

From this, we see that the condition mpd (k)+mpd (k) ≥ k for all

## G H

k forces Ψ(G)+Ψ(H) ≥ Ψ(G∇H), with equality for k = |C|, and, by
Lemma 2.3, additivity of Ψ over the join.
Conversely, suppose that mpd (k )+mpd (k ) < k for some 1 ≤

## G 0 H 0 0

k ≤ min{|G|,|H|}. Choose realizing subgraphs for mpd (k ) and

## 0 G 0

mpd (k ), X and X , respectively. It follows that mpd (k ) =

## H 0 G H G 0

Ψ(G) − Ψ(G \ X ), mpd (k ) = Ψ(H) − Ψ(H \ X ), and |X | =

## G H 0 H G

|X | = k . Then

## H 0

Ψ(G)+Ψ(H) < Ψ(G\X )+Ψ(H \X )+k .

## G H 0

We can pseudocompletely color G∇H as follows: color G\X pseu-

## G

docompletely with Ψ(G\X ) colors, color H \X pseudocompletely

## G H

with Ψ(H \X ) additional colors, and color both X and X with k

## H G H 0

further colors. Then we have
Ψ(G\X )+Ψ(H \X )+k ≤ Ψ(G∇H)

## G H 0

and so

## Ψ(G)+Ψ(H) < Ψ(G∇H).

(cid:3)
From Theorem 3.2, we immediately get the following result.
Theorem 3.3. Let G and H be critical graphs. Then

## Ψ(G∇H) = Ψ(G)+Ψ(H).


<!-- Page 6 -->


## 6 Meddaugh,Sepanski,Venkataraman

Remark 3.4. Though erroneously claimed in [7] Corollary 6, the converse of Theorem 3.3 is not true which invalidates some of the results
and proofs in [7]. The failure of the converse can be seen with P and
3
C . Using Lemma 2.6 and the straightforward facts that Ψ(P ) = 2
8 3
andΨ(C ) = 4 , neither P nor C is critical. However, a labeling of the
8 3 8
join using {1,2,3} and {1,4,5,6,4,4,4,4} and Lemma 2.2 show that
Ψ(P ∇C ) = 6 so that Ψ(P ∇C ) = Ψ(P )+Ψ(C ). See Theorem 4.7
3 8 3 8 3 8
below for as close to a converse as possible.
Theorem 3.3 allows us to show that criticality is preserved under
join.
Theorem 3.5. If G and H are critical graphs, then G∇H is also
critical.
Proof. Use Lemma 2.6 and Theorem 3.3 to see that G∇H is critical if
and only if
2(Ψ(G)+Ψ(H)) = (ω(G)+ω(H))+(|V |+|W |)

## G H

(cid:3)
and we are done.
Remark 3.6. The converse of Theorem 3.5 is false. To see this, recall
that P is not critical. However, a labeling of P ∇P with {1,2,3} and
3 3 3
{1,4,5} on each P shows that Ψ(P ∇P ) ≥ 5. Equality and the fact
3 3 3
that P ∇P is critical then follow from Lemma 2.2 and Lemma 2.6.
3 3
Note that this shows that the partial converse to Theorem 3.5 is false
even when restricting to the case of G = H. Of note, see the comment
after Equation 5.1 and Theorem 5.3.
We end this section with a general constraint on critical graphs and
their pseudocomplete coloring.
Theorem 3.7. If G is critical, then there is a pseudocomplete coloring of G in which ω(G) colors are used exactly once on a maximal
clique and |V|−ω colors are used exactly twice on the complement of the
2
maximal clique. Moreover,
(|V|+ω)(|V|+ω −2)

## |E| ≥ .

8
Proof. Let ℓ be a pseudocomplete coloring of G with the colors S =
{1,2,...,Ψ(G)}. For k ∈ Z+, let
m = {i ∈ S | |ℓ−1(i)| = k}
k
and n = |m |. As ℓ is pseudocomplete, K = ℓ−1(i) is a clique
k k i∈m1
of size n 1 . S

<!-- Page 7 -->


## Criticality, Additivity, Join, Pseudoachromatic Number 7

Moreover,
|V| = kn
k
k X ∈Z+
= n +2 n + (k −2)n
1 k k

## X X

k≥2 k≥3
= n +2(Ψ(G)−n )+ (k −2)n
1 1 k

## X

k≥3
= 2Ψ(G)−n + (k −2)n
1 k

## X

k≥3
≥ 2Ψ(G)−n
1
≥ 2Ψ(G)−ω(G).
By Lemma 2.6, G is critical if and only if |V| = 2Ψ(G)−ω(G). From
the equations above, we see G is critical if and only if we have equality
at each step. In particular, if and only if m = ∅ for k ≥ 3 and
k
n = ω(G).
1
As a result, K is a maximal clique and its colors are used exactly
once. In addition, the colors of X = G \ K are used exactly twice.
Therefore X may be broken into two sets of equal size, X and X ,
1 2
with the colors of X used exactly once in X and exactly once in X .
1 1 2
Finally, write X˜ for the contraction of G that identifies each vertex
inX with the vertex in X of thesame color. As ℓ is a pseudocomplete
1 2
coloring,weseethatX˜ isthecompletegraphonω(G)+|V|−ω(G) vertices
2
(cid:3)
and we are done.

## Weak Criticality

As demonstrated in Remark 3.4, criticality is not necessary for additivity of Ψ over the join. Indeed, Theorem 3.2 shows that additivity
of Ψ for a graph pair depends on on subtle structures in both graphs,
rendering a simple characterization of additive pairs out of the question. Despite that, in this section we demonstrate that additivity of Ψ
requires at least one graph to have a weak form of criticality.
The following is a subtle tweak of Definition 2.5. Note the change
from the ceiling function to the floor function.
Definition 4.1. We say G is weakly critical if
k
mpd (k) ≥

### G (cid:22)2(cid:23)

for all 0 ≤ k ≤ |G|.

<!-- Page 8 -->


## 8 Meddaugh,Sepanski,Venkataraman

Note that Definitions 2.5 and 4.1 imply that every critical graph is
weakly critical. The converse to this is not true as P is weakly critical
3
but not critical.
We immediately get the following by applying Theorem 3.2 and noting that k + k = k for all k.
2 2
(cid:4) (cid:5) (cid:6) (cid:7)
Corollary 4.2. Let G and H be graphs with G critical and H weakly
critical. Then

## Ψ(G∇H) = Ψ(G)+Ψ(H).

The following results concerning weak criticality are analogues of
various results for criticality. The first is the analogue of Lemma 2.6
for being weakly critical and avoids the parity constraint of criticality.
Theorem 4.3. Let G be a graph. Then G is weakly critical if and only
if
ω(G)+|V|

## Ψ(G) = .

(cid:22) 2 (cid:23)
Proof. By Lemma 2.2, it suffices to prove that
ω(G)+|V|

## (4.1) Ψ(G) <

(cid:22) 2 (cid:23)
happens if and only if G is not weakly critical.
First suppose that Equation 4.1 holds. Choose K ⊆ G to be a
maximal clique and let X = G\K. Then
ω(G)+|V|

## Ψ(G) <

(cid:22) 2 (cid:23)
|V|−ω(G)
= ω(G)+
(cid:22) 2 (cid:23)

## |X|


## = Ψ(G\X)+ .

(cid:22) 2 (cid:23)
Therefore mpd (|X|) ≤ Ψ(G)−Ψ(G\X) < |X| and G is not weakly

## G 2

j k
critical.
Conversely, suppose there exists G is not weakly critical. Then there
exists k ≤ |G| with mpd (k) < |X| . Let X be a realizing subgraph

## G 2

j k

<!-- Page 9 -->


## Criticality, Additivity, Join, Pseudoachromatic Number 9

for mpd (k). Then, using Lemma 2.2,

## G


## |X|


## Ψ(G) < Ψ(G\X)+

(cid:22) 2 (cid:23)
ω(G\X)+(|V|−|X|) |X|
≤ +
(cid:22) 2 (cid:23) (cid:22) 2 (cid:23)
ω(G)+|V|−|X| |X|
≤ +
(cid:22) 2 (cid:23) (cid:22) 2 (cid:23)
ω(G)+|V|
≤
(cid:22) 2 (cid:23)
(cid:3)
and we are done.
From Theorem 4.3 and Lemma 2.6, observe that if ω(G) + |V| is
even, then G is critical if and only if it is weakly critical. However,
when ω(G)+ |V| is odd, G is not critical, but G may still be weakly
critical. The graph P is such an example.
3
We now give the analogue of Theorem 3.7 for weakly critical.
Theorem 4.4. Let G be weakly critical but not critical. Then there is
a pseudocomplete coloring of G so that either
(1) ω(G) colors are used exactly once on a maximal clique, a single
color is used exactly three times in the complement of the clique,
and |V|−ω−3 colors are used exactly twice on remaining vertices
2
or
(2) ω(G)−1 colors are used exactly once on a clique of size ω(G)−1
and |V|−ω+1 colors are used exactly twice on complement of the
2
clique.

### Moreover,

(|V|+ω −1)(|V|+ω −3)

## |E| ≥ .

8
Proof. This result follows from the proof of Theorem 3.7. As Theorem
4.3 shows that weakly critical in this setting is the same as requiring
|V|+ω(G)−2Ψ(G)−1 = 0,
the proof of Theorem 3.7 shows that n = 0 for k ≥ 4. Moreover,
k
either n = ω and m = 1 or n = ω(G)−1 and m = 0. (cid:3)
1 3 1 3
The remainder of this section is devoted to demonstrating that weak
criticality is required of at least one graph in a Ψ-additive graph pair.
The following result will be an important technical tool.
Theorem 4.5. Let G be a graph. Then G is not weakly critical if and
only if there exists induced subgraphs M ⊆ M ⊆ G so that
1 2

<!-- Page 10 -->


## 10 Meddaugh,Sepanski,Venkataraman


## (1) |V | = 2,


## M2\M1


## (2) Ψ(M ) = Ψ(M ),

1 2

## (3) Ψ(G) = Ψ(M )+


## |Vg\M2 |

.
2 2
j k
Moreover, if ℓ is a maximal pseudocomplete coloring of G, there exists
C ⊆ V with |C| =

## |Vg\M1 |

+1 ≥ 2 and ℓ(G) = ℓ(G\C).

## G 2

j k
Proof. Suppose G is not weakly critical and, by Definition 4.1, choose
M to be a maximal subgraph of G satisfying
1

## |V |


## Ψ(G) ≤ Ψ(M )+


## G\M1

−1.
1
(cid:22) 2 (cid:23)
As Ψ(G) ≥ Ψ(M ), |V | ≥ 2. Choose M to be any induced sub-

## 1 G\M1 2

graph of G satisfying M ⊆ M with |V | = 2.

## 1 2 M2\M1

By maximality, we get

## |V |


## Ψ(G) ≥ Ψ(M )+


## G\M2

2
(cid:22) 2 (cid:23)

## |V |


## = Ψ(M )+


## G\M1

−1
2
(cid:22) 2 (cid:23)

## |V |


## ≥ Ψ(M )+


## G\M1

−1
1
(cid:22) 2 (cid:23)

## ≥ Ψ(G).

Therefore Ψ(M ) = Ψ(M ) and Ψ(G) = Ψ(M )+

## |Vg\M2 |

.
1 2 2 2
j k
For the converse, observe that we would have

## |V |


## Ψ(G) = Ψ(M )+


## G\M2

2
(cid:22) 2 (cid:23)

## |V |


## = Ψ(M )+


## G\M1

−1
1
(cid:22) 2 (cid:23)
so that mpd (|M |) ≤ Ψ(G)−Ψ(M ) <

## |Vg\M1 |

, and therefore G is

## G 1 1 2

j k
not weakly critical.
For the final statement, write ξ =

## |Vg\M1 |

. Observe that
2
j k
Ψ(G) = Ψ(M )+ξ −1 ≤ |M |+ξ −1
1 1
and
|V| = |M |+|V | ≥ |M |+2ξ.

## 1 G\M1 1

If one vertex of each color is selected from G, we see that leaves at least
ξ +1 vertices which may be chosen as C. (cid:3)

<!-- Page 11 -->


## Criticality, Additivity, Join, Pseudoachromatic Number 11

It is worth pointing out that an analogous argument establishes the
following characterization of critical graphs.
Theorem 4.6. Let G be a graph. Then G is not critical if and only if
there exists induced subgraphs M ⊆ M ⊆ G so that
1 2

## (1) 0 < |V | ≤ 2,


## M2\M1


## (2) Ψ(M ) = Ψ(M ),

1 2

## (3) Ψ(G) = Ψ(M )+


## |Vg\M2 |

.
2 2
l m
Moreover, if ℓ is a maximal pseudocomplete coloring of G, there exists
C ⊆ V with |C| =

## |Vg\M2 |

+|V |−1 and ℓ(G) = ℓ(G\C).

## G 2 M2\M1

l m
As a consequence of Theorem 4.5, we are now able to prove the
following, which is as close to a converse of Corollary 3.3 as possible.
Theorem 4.7. Let G and H be graphs. If

## Ψ(G)+Ψ(H) = Ψ(G∇H),

then at least one of G or H is weakly critical. Moreover, if one of G or
H is weakly critical and has a coloring of form (1) as in Theorem 4.4,
then the other is weakly critical and does not have such a coloring.
Proof. Let G and H be graphs with ψ(G∇H) = Ψ(G)+Ψ(H).
Suppose that both G and H are not weakly critical. Using Theorem
4.5, choose induced subgraphs M ⊆ M ⊆ G and N ⊆ N ⊆ H. After
1 2 1 2
possibly relabeling, suppose

## |Vg\M1 |

≤

## |Vh\N1 |

.
2 2
j k j k
Color H with a pseudocomplete coloring with Ψ(H) colors. Choose
C ⊆ H with|C| =

## |Vg\M1 |

sothatallΨ(H)colorsarestillrepresented
2
j k
in H \C.
Write V = P ∐ P with |P | =

## |Vg\M1 |

≤ |P |. Color V

## G\M1 0 1 0 2 1 G\M1

j k
with

## |Vg\M1 |

new colors such that each color appears in both P and
2 0
j k

## P .

1
Finally, swap the colors in P with those in C and color M with a
0 1
pseudocomplete coloring consisting of Ψ(M ) additional new colors.
2
By construction, this gives a pseudocomplete coloring with

## |V |


## Ψ(H)+Ψ(M )+


## G\M2


## +1 = Ψ(H)+Ψ(G)+1

2
(cid:22) 2 (cid:23)
colors. As this is a lower bound for Ψ(G∇H), we get Ψ(G)+Ψ(H) >
Ψ(G∇H) which contradicts addivity of Ψ.
Thus one of G or H must be weakly critical.

<!-- Page 12 -->


## 12 Meddaugh,Sepanski,Venkataraman

Now, assume that G is weakly critical and has a pseudocomplete
coloring of type (1). Let ℓ be such a coloring, i.e. a coloring using Ψ(G) = ω(G)+|VG| many colors with vertices v , v , and v with
2 0 1 2
j k
ℓ(v ) = ℓ(v ) = ℓ(v ). Note that ℓ uses all Ψ(G) colors on G\{v ,v }.
0 1 2 0 1
Assume that H is either not weakly critical or weakly critical with a
coloring of type (1). In either case, we will show that there are distinct
c ,c ∈ V and a pseudocomplete coloring ℓ′ of H so that Ψ(H) many

## 0 1 H

colors appear in the complement of {c ,c }.
0 1
IfH isnotweaklycritical, byTheorem4.5, thereisapseudocomplete
coloring ℓ′ of H using Ψ(H) many colors and a subset C of V with

## H


## |C| =


## Vh\N1

+ 1 ≥ 2 such that each of the Ψ(H) colors appears in
2
j k
the complement of C. Let {c ,c } ⊆ C.
0 1
If H is weakly critical with a coloring of type (1), take ℓ′ to be one
such coloring and let c , c , and c be the three vertices that share a
0 1 2
color. Clearly ℓ′ uses all Ψ(H) colors on H \{c ,c }.
0 1
Now, color G∇H as follows: color G\{v ,v } according to ℓ; color
0 1
H \{c ,c } according to ℓ′; color c with ℓ(v ); v with ℓ′(c ); and use
0 1 0 0 0 0
one additional color to color both v and c . By construction, this is a
1 1
pseudocomplete coloringconsisting ofΨ(G)+Ψ(H)+1 > Ψ(G)+Ψ(H)
manycolors, establishing thatΨ(G∇H) > Ψ(G)+Ψ(H),contradicting
additivity of Ψ. Thus if G is weakly critical and has a pseudocomplete
coloring of type (1), then H is weakly critical and does not have a
(cid:3)
pseudocomplete coloring of type (1).

## Remarks on ∇kG

If we restrict to the case that G = H, we can get a partial converse
to Theorem 3.3 with a stronger conclusion than that of Theorem 4.7.
Theorem 5.1. Let G be a graph. Then G is critical if and only if

## Ψ(G∇G) = 2Ψ(G).

Proof. Theorem 3.2 shows that Ψ(G∇G) = 2Ψ(G) if and only if for
all k ≤ |G|, mpd (k)+mpd (k) ≥ k. Since mpd (k) is an integer for

## G G G

all k, this happens if and only if mpd (k) ≥ k for all k ≤ |G|, i.e.,

## G 2


### G is critical. (cid:6) (cid:7) (cid:3)

Remark 5.2. As noted in Remark 3.6, the converse of Theorem 3.5
fails. Indeed the converse fails even under the assumption that G = H.
Theorem 3.1 immediately implies that
(5.1) Ψ(G∇G) = ω(G)+|V |

## G

for all G, so by Lemma 2.2, G∇G is always critical.

<!-- Page 13 -->


## Criticality, Additivity, Join, Pseudoachromatic Number 13

In fact, more is true.
Theorem 5.3. Let k ∈ Z with k ≥ 2. Then ∇kG is critical if and only
if
k(ω(G)+|V|)
is even.
Proof. If k is even, apply Equation 5.1 with G replaced by ∇k/2G and
then use Lemma 2.2 to get criticality.
If ω(G)+|V| is even with k ≥ 3, begin with a maximal clique, K, of
G and let X = G\K. As ω(G)+|V| is even, so is |X| = |V|−ω(G).
Divide X into sets X and X of equal order, q = |V|−ω(G).
1 2 2
In ∇kG, color ∇kK with kω(G) distinct colors. Next color ∇kX
1
with an additional kq colors. Finally, color ∇kX with a shift of the
2
colors used in ∇kX . More precisely, color the (i+1)st copy of X in
1 2
∇kX , i viewed as an element of Z , with the same colors used on the
2 k
ith copy of X in ∇kX . This ensures that the colors used in each copy
1 1
of X in ∇kX are used in two different copies of X. It is straightforward
to verify that this results in a pseudocomplete coloring of ∇kG. As
|V|−ω(G) ω(G)+|V|
k ω(G)+ = k ,
(cid:18) 2 (cid:19) 2
Lemma 2.2 again gives criticality.
Finally, if k(ω(G)+|V|) is odd, Lemma 2.2 shows that ∇kG is not
(cid:3)
critical.
Notethat, ascriticality of Grequires ω(G)+|V| tobeeven, Theorem
3.1 says that ∇kG is critical whenever parity makes criticality possible.
See Theorem 5.5 below when parity makes criticality impossible.
Theorem 5.3 allows us to generalize Theorem 5.1. See Theorem 5.6
for the analogue when k(ω(G)+|V|) is odd. Note that this, along with
Theorem 5.6 below, gives a correct proof of [7] Corollary 11.
Theorem 5.4. Let k ∈ Z with k ≥ 2 and k(ω(G)+|V|) even. Then
G is critical if and only if
kΨ(G) = Ψ(∇kG).
Proof. As Theorem 5.3 shows that ∇kG is critical, it follows from
Lemma 2.6 that Ψ(∇kG) = kω(G)+|V|. Therefore, kΨ(G) = Ψ(∇kG) if
2
and only if Ψ(G) = ω(G)+|V| if and only if G is critical. (cid:3)
2
Recall that Theorem 5.3 showed that, for k ≥ 2, ∇kG is critical if
and only if k(ω(G) + |V|) is even. We now show that weakly critical
fills in the rest of the range.

<!-- Page 14 -->


## 14 Meddaugh,Sepanski,Venkataraman

Theorem 5.5. Let k ∈ Z with k ≥ 2. Then ∇kG is weakly critical.
Proof. By Theorem 5.3 and the comment following Theorem 4.3, it
remains to show that ∇kG is weakly critical when k(ω(G)+|V|) is odd
with k ≥ 3.

### Begin with a maximal clique, K, of G and let X = G \ K. As

ω(G)+|V| is odd, so is |X| = |V|−ω(G). Divide X into sets X and
1
X of equal order, q = |V|−ω(G)−1, and a singleton vertex, v .
2 2 0
In ∇kG, as in Theorem 5.3, color ∇kK with kω(G) distinct colors,
∇kX with an additional kq colors, and∇kX with a shifted coloring of
1 2
∇kX . Finally color the copies of v in ∇kG with an additional k−1 col-
1 0 2
ors. Itis straightforwardtoverify that thisgenerates apseudocomplete
coloring of ∇kG. As
|V|−ω(G)−1 k −1 ω(G)+|V| 1
k ω(G)+ + = k −
(cid:18) 2 (cid:19) 2 2 2
k(ω(G)+|V|)
= ,
(cid:22) 2 (cid:23)
(cid:3)
Theorem 4.3 gives weak criticality.
Theorem 5.5 now allows us to address the analogue of Theorem 5.4
when k(ω(G)+|V|) is odd.
Theorem 5.6. Let k ∈ Z with k ≥ 3 and k(ω(G)+|V|) odd. Then G
is not critical. However, G is weakly critical if and only if
k
kΨ(G)+ = Ψ(∇kG).
(cid:22)2(cid:23)
Proof. The fact that G is not critical follows by parity from Lemma

### As Theorem 5.5 shows that ∇kG is weakly critical, it follows from

Theorem 4.3 that Ψ(∇kG) = k(ω(G)+|V|) . However, we know that G
2
j k
isweaklycritical iffandonlyifΨ(G) = ω(G)+|V| . Asthisisequivalent
2
j k
to
ω(G)+|V|
kΨ(G) = k
(cid:22) 2 (cid:23)
k(ω(G)+|V|) k
= −
2 2
k(ω(G)+|V|) k
= − ,
(cid:22) 2 (cid:23) (cid:22)2(cid:23)
(cid:3)
we are done.

<!-- Page 15 -->


## Criticality, Additivity, Join, Pseudoachromatic Number 15


### Acknowledgments

The third author and the Kalasalingam Academy of Research and
Education promote the Sustainable Development Goal of ensuring inclusive and equitable quality education and promoting lifelong learning
opportunities for all.
In addition, the third author is thankful to the Department of Mathematics, Baylor University, for the support given during his visit.

### References

[1] O. Aichholzer, G. Araujo-Pardo, N. Garc´ıa-Col´ın, T. Hackl,
D. Lara, C. Rubio-Montiel, and J. Urrutia. Geometric achromatic
and pseudoachromatic indices. Graphs Combin., 32(2):431–451,

## ISSN0911-0119,1435-5914.doi: 10.1007/s00373-015-1610-x.

URL https://doi.org/10.1007/s00373-015-1610-x.
[2] M. G. Araujo-Pardo and C. Rubio-Montiel. Pseudoachromatic and connected-pseudoachromatic indices of the complete graph. Discrete Appl. Math., 231:60–66, 2017. ISSN
0166-218X,1872-6771. doi: 10.1016/j.dam.2017.03.019. URL
https://doi.org/10.1016/j.dam.2017.03.019.
[3] M. G. Araujo-Pardo, J. J. Montellano-Ballesteros, and R. Strausz.
On the pseudoachromatic index of the complete graph. J. Graph
Theory, 66(2):89–97, 2011. ISSN 0364-9024,1097-0118. doi: 10.
1002/jgt.20491. URL https://doi.org/10.1002/jgt.20491.
[4] M. G. Araujo-Pardo, J. J. Montellano-Ballesteros, C. Rubio-
Montiel, and R. Strausz. On the pseudoachromatic index of the
complete graph II. Bol. Soc. Mat. Mex. (3), 20(1):17–28, 2014.
ISSN1405-213X,2296-4495.doi: 10.1007/s40590-014-0007-9.URL
https://doi.org/10.1007/s40590-014-0007-9.
[5] M. G. Araujo-Pardo, J. J. Montellano-Ballesteros, C. Rubio-

### Montiel, and R. Strausz. On the pseudoachromatic index of

the complete graph III. Graphs Combin., 34(2):277–287, 2018.
ISSN 0911-0119,1435-5914. doi: 10.1007/s00373-017-1872-6. URL
https://doi.org/10.1007/s00373-017-1872-6.
[6] R. Balakrishnan, R. Sampathkumar, and V. Yegnanarayanan. Extremal graphs in some coloring
problems. Discret. Math., 186:15–24, 1998. URL
https://api.semanticscholar.org/CorpusID:14070240.
[7] R. Balasubramanian, V. Raman, and V. Yegnanarayanan.
On the pseudoachromatic number of join of graphs. Int.

<!-- Page 16 -->


## 16 Meddaugh,Sepanski,Venkataraman


### J. Comput. Math., 80(9):1131–1137, 2003. ISSN 0020-

7160,1029-0265. doi: 10.1080/00207160310001597206. URL
https://doi.org/10.1080/00207160310001597206.
[8] V. N. Bhave. On the pseudoachromatic number of a
graph. Fund. Math., 102(3):159–164, 1979. ISSN 0016-
2736,1730-6329. doi: 10.4064/fm-102-3-159-164. URL
https://doi.org/10.4064/fm-102-3-159-164.
[9] J. Chen, I. A. Kanj, J. Meng, G. Xia, and
F. Zhang. On the pseudo-achromatic number problem. Theor. Comput. Sci., 410:818–829, 2008. URL
https://api.semanticscholar.org/CorpusID:7927423.
[10] K. J. Edwards. Achromatic number versus pseudoachromatic number: a counterexample to a conjecture of
hedetniemi. Discret. Math., 219:271–274, 2000. URL
https://api.semanticscholar.org/CorpusID:32061614.
[11] R. P. Gupta. Bounds on the chromatic and achromatic numbers
of complementary graphs. In Recent Progress in Combinatorics
(Proc. Third Waterloo Conf. on Combinatorics, 1968), pages 229–

## Academic Press, New York-London, 1969.

[12] F. Harary and S. Hedetniemi. The achromatic number of a graph.
J. Combinatorial Theory, 8:154–161, 1970. ISSN 0021-9800.
[13] F. Harary, S. Hedetniemi, and G. Prins. An interpolation theorem
for graphical homomorphisms. Portugal. Math., 26:453–462, 1967.

## Issn 0032-5155,1662-2758.

[14] M.LiuandB.Liu. Onpseudoachromaticnumberofgraphs. Southeast Asian Bull. Math., 35(3):431–438, 2011. ISSN 0129-2021.
[15] E. Sampathkumar and V. N. Bhave. Partition graphs and coloring numbers of a graph. Discret. Math., 16:57–60, 1976. URL
https://api.semanticscholar.org/CorpusID:34550489.
[16] V. Yegnanarayanan. The pseudoachromatic number of a graph.
Southeast Asian Bulletin of Mathematics, 24:129–136, 2000. URL
https://api.semanticscholar.org/CorpusID:15941791.
[17] V. Yegnanarayanan. Graph colourings and partitions. Theor. Comput. Sci., 263:59–74, 2001. URL
https://api.semanticscholar.org/CorpusID:16789912.
[18] V. Yegnanarayanan. On pseudocoloring of graphs. Util. Math.,

## 62:199–216, 2002. Issn 0315-3681.

[19] V. Yegnanarayanan. Computational complexity of pseudoachromatic number of graphs. Util. Math., 78:159–163, 2009. ISSN
0315-3681.

<!-- Page 17 -->


## Criticality, Additivity, Join, Pseudoachromatic Number 17

[20] V. Yegnanarayanan and B. Logeshwary. On pseudocomplete
and complete coloring of graphs. In Proceedings of the International Conference on Applied Mathematics and Theoretical Computer Science, volume 1, pages 104–109, 2013. URL
https://api.semanticscholar.org/CorpusID:53459602.
[21] V. Yegnanarayanan, R. Balakrishnan, and R. Sampathkumar. On the existence of graphs with prescribed coloring parameters. Discret. Math., 216:293–297, 2000. URL
https://api.semanticscholar.org/CorpusID:44624696.
Meddaugh and Sepanski: Department of Mathematics, Baylor University, Sid Richardson Building, 1410 S. 4th Street, Waco, TX 76706,
USA;, Venkataraman: Kalasalingam Academy of Research and Educatioon, Deemed to be University, Srivilliputhur, Tamil Nadu 626126,

### India

Emailaddress: Jonathan Meddaugh@baylor.edu, Mark Sepanski@baylor.edu,
prof.yegna@gmail.com