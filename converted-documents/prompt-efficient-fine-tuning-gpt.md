---
title: "Prompt Efficient Fine Tuning GPT"
original_file: "./Prompt_Efficient_Fine_Tuning_GPT.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag"]
keywords: ["matching", "graph", "bipartite", "covered", "let", "minimal", "theorem", "each", "edge", "obtained"]
summary: "<!-- Page 1 -->

Extremal minimal
∗
bipartite matching covered graphs

### Amit Kumar Mallik Ajit A. Diwan

Indian Institute of Technology Bombay Indian Institute of Technology Bombay
amit.km287@gmail.com aad@cse.iitb.ac.in

### Nishad Kothari

Indian Institute of Technology Madras
nishadkothari@gmail.com

### July 14, 2025

The first and last authors dedicate this work to their coauthor,
the late Ajit A. Diwan

### Abstract

Aconnectedgraph, onfourormorevertices, ismatching covered (aka1-extend"
related_documents: []
---

# Prompt Efficient Fine Tuning GPT

<!-- Page 1 -->

Extremal minimal
∗
bipartite matching covered graphs

### Amit Kumar Mallik Ajit A. Diwan

Indian Institute of Technology Bombay Indian Institute of Technology Bombay
amit.km287@gmail.com aad@cse.iitb.ac.in

### Nishad Kothari

Indian Institute of Technology Madras
nishadkothari@gmail.com

### July 14, 2025

The first and last authors dedicate this work to their coauthor,
the late Ajit A. Diwan

### Abstract

Aconnectedgraph, onfourormorevertices, ismatching covered (aka1-extendable)
if every edge is present in some perfect matching. An ear decomposition theorem
(similartotheonefor2-connectedgraphs)existsforbipartitematchingcoveredgraphs
due to Hetyei. From the results and proofs of Lov´asz and Plummer [Matching Theory,
Annals of Discrete Math. 29, 1986], that rely on Hetyei’s Theorem, one may deduce
that any minimal bipartite matching covered graph has at least 2(m−n+2) vertices
of degree two (where minimal means that deleting any edge results in a graph that is
not matching covered); such a graph is extremal if it attains the stated bound.
In this paper, we provide a complete characterization of the class of extremal minimalbipartitematchingcoveredgraphs. Inparticular,weprovethateverysuchgraphG
is obtained from two copies of a tree devoid of degree two vertices, say T and T′, by
adding edges — each of which joins a leaf of T with the corresponding leaf of T′.
Apart from the aforementioned bound, there are four other bounds that appear in,
ormaybededucedfrom, theworkofLov´aszandPlummer. Eachoftheseboundsleads
to a notion of extremality. In this paper, we obtain a complete characterization of all
of these extremal classes and also establish relationships between them. Two of our
characterizations are in the same spirit as the one stated above. For the remaining two
extremal classes, we reduce each of them to one of the already characterized extremal
classes using standard matching theoretic operations.
Aconnectedgraphisk-extendableifithasamatchingofcardinalityk andeachsuch
matchingextendstoaperfectmatching. WealsodiscussboundsprovedbyLou[On the
structure of minimally n-extendable bipartite graphs, Discrete Math. 202 (1), 1999] for
minimal k-extendable bipartite graphs (where minimal means that deleting any edge
resultsinagraphthatisnotk-extendable). Weconjecturestrongerboundsandprovide
∗Supported by IC&SR IIT Madras
1
5202
luJ
11
]OC.htam[
3v54460.4042:viXra

<!-- Page 2 -->

evidence for our conjectures by constructing tight examples that are straightforward
generalizations of the ones that appear in the 1-extendable case.
1 Introduction and summary
All graphs considered here are loopless; however, we allow parallel/multiple edges. For
notation and terminology, we largely follow Bondy and Murty [1]. For a graph G := (V,E),
its order is the number of vertices denoted by n, and its size is the number of edges denoted
by m. We use the notation G[A,B] to denote a bipartite graph with specified color classes
A and B.
A graph is matchable if it has a perfect matching and an edge is matchable if it belongs
to some perfect matching. A subgraph H of a graph G is conformal if G−H is matchable.
A connected graph of order four or more is matching covered if every edge is matchable;
these graphs are also referred to as 1-extendable in the literature since each edge extends to
a perfect matching; see Lova´sz and Plummer [11]. There is an elegant ear decomposition
theory for the class of bipartite matching covered graphs, due to Hetyei [6], that may be
viewed as a refinement of the more well-known ear decomposition theory for the larger class
of 2-connected graphs due to Whitney [16]. We describe this below.
An ear of H in G is an odd path of G whose ends are in H but is otherwise disjoint from H.
For a bipartite graph G, a sequence of subgraphs (G ,G ,...,G ) is an ear decomposition
0 1 r
of G if: (i) C := G is an (even) cycle, (ii) G = G ∪P where P is an ear of G for
0 i+1 i i+1 i+1 i
each i ∈ {0,1,...,r−1}, and (iii) G = G. It is easy to observe that each subgraph G is a
r i
conformal matching covered subgraph of G, and that r = m−n. We refer to (C,P ,...,P )
1 r
as the associated ear sequence, or simply an ear sequence of G. Figure 1 shows a bipartite
matching covered graph and an ear sequence for the same.

## C P

2

## P

1

## P


## P 4

3
Figure 1: a bipartite matching covered graph and its ear decomposition
The following is the aforementioned result by Hetyei that we will find useful in order to
establish that certain bipartite graphs are indeed matching covered.

### Theorem 1.1. [Ear Decomposition Theorem]

A bipartite graph is matching covered if and only if it admits an ear decomposition.
There is also a generalization of the above theorem for nonbipartite matching covered
graphs due to Lova´sz and Plummer [11]. However, we do not describe this here since our
work focuses on bipartite matching covered graphs.
2

<!-- Page 3 -->

1.1 Minimality, bounds and corresponding notions of extremality
A matching covered graph is minimal if deletion of any edge results in a graph that is not
matching covered. We use H to denote the class of minimal bipartite matching covered
graphs. Using the ear decomposition theory, Lova´sz and Plummer [11] proved that each
member of H has at least m−n+2 pairwise nonadjacent 2-edges — where a 2-edge is an
edge whose each end has degree two. Thus, such a graph has at least 2(m−n+2) degree
two vertices. Furthermore, for each of these invariants, one may also deduce lower bounds
solely in terms of n; in particular, that each member of H has at least n+10 2-edges and at
6
least n + 2 vertices of degree two; see Corollaries 7.9 and 7.1. They also proved an upper
2
bound — namely, that each member of H, distinct from C , has at most 3n−6 edges.
4 2
Each of the bounds stated in the above paragraph leads to a notion of extremality for
minimal bipartite matching covered graphs. As we have five different bounds, we have five
notions of extremality as defined in Table 1. For instance, H denotes the class of 2-vertex
2
extremal minimal bipartite matching covered graphs — that is, those members of H that
satisfy |V | = 2(m−n+2) where V is the set of degree two vertices. Likewise, we use E
2 2 2
to denote the set of 2-edges.

### Class Property Notation

2-edge extremal |E | = m−n+2 H
2 0
2-edge n-extremal |E | = n+10 H
2 6 1
2-vertex extremal |V | = 2(m−n+2) H
2 2
2-vertex n-extremal |V | = n +2 H
2 2 3
edge extremal |E| = 3n−6 H
2 4
Table 1: Definitions of different notions of extremality within H
In this paper, we completely characterize all of the five classes of “extremal” minimal bipartite matching covered graphs in terms of special trees. Our characterizations are reminiscent
of similar characterization(s) of “extremal” minimal 2-connected graphs — where minimality is defined with respect to edge deletion; we briefly describe some of these results below
before stating our characterizations.
Dirac [3] proved that a minimal 2-connected graph has at least n+4 vertices of degree
3
two. A minimal 2-connected graph is extremal if it satisfies this lower bound with equality.
Oxley [13] gave a generation theorem for extremal minimal 2-connected graphs. Karpov [8]
then characterized this class of graphs in terms of special trees. In particular, they proved
that a graph is extremal minimal 2-connected if and only if it can be obtained from two
copies of a tree, each of whose non-leaves is of degree three, by identifying the corresponding
leaves as per some fixed isomorphism; see Figure 2 for an example.
A tree is said to be a Halin tree if all of its non-leaves have degree at least three, or
equivalently, if it has no vertices of degree two; see Figure 3 for an example. We call
them halin trees because a Halin graph is a (planar) graph that is obtained from a planar
embedding of such a tree by adding a cycle each of whose edges joins two leaves that appear
consecutivelyinthecyclicorder(aspertheplanarembedding). Halingraphs,firstintroduced
3

<!-- Page 4 -->

Figure 2: illustration of Karpov’s characterization of extremal minimal 2-connected graphs
by Halin [5], as examples of minimal 3-connected graphs, have been studied extensively in
the literature. Halin trees are precisely the “homeomorphically irreducible” trees; finding
such spanning trees in a cubic graph is a well-studied problem; see [7]. A Halin tree is cubic
if the corresponding Halin graph is cubic. To put it differently, a tree is a cubic Halin tree
if all of its non-leaves have degree exactly three; see Figure 2 for an example. Thus, the
aforementioned Karpov’s characterization of extremal minimal 2-connected graphs draws a
bijection between this graph class and cubic halin trees.
1.2 Characterizations of H ,H and H using halin trees
2 3 4
We are now ready to state our characterizations of “extremal” minimal bipartite matching
covered graphs — that are similar to Karpov’s characterization. However, in our case,
identifying the corresponding leaves is not the correct operation.
For two disjoint copies of a Halin tree, say T and T′, let H be the (bipartite) graph obtained
fromT∪T′ byaddingamatchingeachofwhoseedgesjoinsaleafofT withthecorresponding
leaf of T′ as per some fixed isomorphism between T and T′. We say that H is obtained from
T and T′ by isomorphic leaf matching, or simply, that H is obtained from T by isomorphic
leaf matching.
Notethat, sinceK isthesmallestHalintree, C isthesmallestgraphthatmaybeobtained
2 4
using the operation defined above. The following observation is easily proved and it implies
that, for every other graph obtained using this operation, one may recover the two copies of
the Halin tree by simply deleting the set of 2-edges.
Proposition 1.2. If a graph H, distinct from C , is obtained from a Halin tree T by isomor-
4
phic leaf matching, then H −E has precisely two components, each of which is isomorphic
2
to T.
We first focus on the 2-vertex extremal class H (see Table 1) and obtain the following char-
2
acterization establishing a bijection between 2-vertex extremal bipartite matching covered
graphs and Halin trees.
Theorem 1.3. [Main Theorem: Characterization of H ]
2
A graph is a 2-vertex extremal minimal bipartite matching covered graph if and only if it is
obtained from a Halin tree by isomorphic leaf matching.
4

<!-- Page 5 -->

Figure 3: a member of H — deleting the 2-edges results in two copies of a Halin tree
2
Figure 3 shows an illustration of the above theorem. In this figure, and relevant figures
henceforth, we adopt the following color conventions: the red vertices have degree three or
more, the green vertices are of degree two, and the cyan edges are precisely the 2-edges.
Thereafter, we will use our Main Theorem (1.3) to derive characterizations of the extremal
classes H and H as stated below; see Figure 4 for an example of each.
3 4
Theorem 1.4. [Characterization of H ]
3
A graph is a 2-vertex n-extremal minimal bipartite matching covered graph if and only if it
is obtained from a cubic Halin tree by isomorphic leaf matching.
Byastar, wemeanK wherep ⩾ 2. Observethatthese, exceptK , comprisearestricted
1,p 1,2
subclass of Halin trees; they play a crucial role in our characterization of H stated below.
4
Theorem 1.5. [Characterization of H ]
4
A graph is an edge extremal minimal bipartite matching covered graph if and only if it is
obtained from a star by isomorphic leaf matching.
(a) (b)
Figure 4: (a) a member of H : deleting the 2-edges results in two copies of a cubic Halin tree
3
(b) a member of H : deleting the 2-edges results in two copies of a star
4
5

<!-- Page 6 -->

In the next subsection, we prove the easier implications of the characterizations stated
above (that is, Theorems 1.3, 1.4 and 1.5).
1.3 Proofs of easier implications
We begin by proving that any graph obtained from a nontrivial tree by isomorphic leaf
matching is a minimal bipartite matching covered graph. We shall find ear decompositions
useful to establish the matching covered property; however, for minimality, we need an easy
observation pertaining to cuts.
Given a graph G := (V,E), for any W ⊆ V, the cut comprising the edges joining W
and its complement W := V − W is denoted by ∂(W). A cut ∂(W) is trivial if either W
or W comprises at most one vertex, and nontrivial otherwise. A k-cut refers to a cut of
cardinality k. We use abbreviated notations ∂(v) := ∂({v}) for a vertex v, and ∂(H) :=
∂(V(H)) for a subgraph H.
An edge e of a matching covered graph G is removable if G−e is also matching covered.
Thus, a matching covered graph is minimal if and only if it has no removable edges. Since
matching covered graphs are 2-connected, we immediately observe the following.
Lemma 1.6. In a matching covered graph, any edge that participates in a 2-cut is not
removable.
Theabovelemmaistheaforementionedobservationthathelpsusinestablishingminimality
in the proof of the following result; we shall find it useful later as well.
Proposition 1.7. Any graph obtained from a nontrivial tree by isomorphic leaf matching is
a minimal bipartite matching covered graph.
Proof. Let G be a graph obtained from two copies of a nontrivial tree, say T and T′, by
isomorphic leaf matching. We will first prove, by induction on the order of T, that G is a
bipartite matching covered graph. If T is a path then G is a even cycle, and we are done.
Now, let T be a tree that is not a path and let v denote a leaf. Let P be the maximal
path starting at v, each of whose internal vertices has degree two in T. Let u be the end of
P distinct from v. Observe that d (u) ⩾ 3. Let v′P′u′ be the path corresponding to vPu

## T

in T′. Let H := G − V(P − u) − V(P′ − u′). Observe that H is obtained from the tree
T −V(P −u) by isomorphic leaf matching. By the induction hypothesis, H is a bipartite
matching covered graph. Note that G may be obtained from H by adding the ear uPvv′P′u′.
By the ear decomposition theorem (1.1), G is a bipartite matching covered graph.
Now, we prove minimality. Observe that any edge e of G, whose each end has degree at
least three, either belongs to T or belongs to T′. Adjust notation so that e ∈ T. Let e′ be the
copy of e in T′. Note that {e,e′} is a 2-cut of G. Thus, by Lemma 1.6, e is not removable.
We thus infer that G is minimal.
We note that the converse of the above proposition does not hold. The graph G, shown in
Figure 5, is a minimal bipartite matching covered graph that can not be obtained from a tree
6

<!-- Page 7 -->

e
Figure 5: a counterexample to the converse of Proposition 1.7
by isomorphic leaf matching. To see this, suppose to the contrary that G is obtained from
two copies of a tree, say T and T′, by isomorphic leaf matching. Then, as per the proof of
Proposition 1.7, the labeled edge e belongs either to T or to T′ as both ends of e have degree
greater than two; furthermore, e belongs to a 2-cut of G. However, G − e is 2-connected.
This is a contradiction. We shall revisit this example in Section 4.1.
In light of Proposition 1.7, in order to prove the easier implications of Theorems 1.3, 1.4
and 1.5, we simply need to argue that if we choose a tree T from the corresponding class (as
in that theorem’s statement), then the resulting minimal bipartite matching covered graph
G (obtained by isomorphic leaf matching) satisfies the desired extremality notion. We first
note that if T is the star K then G = C is an edge extremal minimal bipartite matching
1,2 6
covered graph. All of the remaining cases are handled by the following theorem — which we
prove using straightforward counting arguments.
Theorem 1.8. Any graph G obtained from a Halin tree T by isomorphic leaf matching is a
minimal bipartite matching covered graph that is 2-vertex extremal. Furthermore:
(i) if T is a cubic Halin tree then G is also 2-vertex n-extremal, whereas
(ii) if T is a star then G is also edge extremal.
Proof. Let G := (V,E) be a graph obtained from two copies of a Halin tree, say T and T′,
by isomorphic leaf matching. By Proposition 1.7, G is a minimal bipartite matching covered
graph. It remains to prove “extremality”. We use V and E to denote V (G) and E (G),
2 2 2 2
respectively.
Since T is a Halin tree, the non-leaves of T and T′ comprise those vertices of G that
have degree at least three, whereas the leaves of T and T′ comprise the remaining vertices
of G (that is, its vertices of degree two). In particular, there are no 2-edges in T ∪T′, and

## T ∪T′ = G−E .

2
Now, |E(T)| = |V(T)| − 1. So, |E(T ∪ T′)| = n − 2. On the other hand, |E(T ∪ T′)| =
|E| − |E | = m − |E |. Thus, |E | = m − n + 2. Since E is a matching of G, and the
2 2 2 2
corresponding matched vertices comprise the set V , we get |V | = 2|E | = 2(m − n + 2).
2 2 2
Hence, G is 2-vertex extremal. It remains to prove statements (i) and (ii).
First, suppose that T is a cubic Halin tree. So, T ∪T′ has |V | leaves and n−|V | vertices
2 2
of degree three. By handshaking lemma, 3(n−|V |)+|V | = 2|E(T ∪T′)| = 2(n−2). By
2 2
simplifying, we get |V | = n +2; whence G is 2-vertex n-extremal.
2 2
7

<!-- Page 8 -->

Now, suppose that T is a star K , where p ⩾ 3. Then, n = 2(p + 1). Observe that
1,p
m = 3p = 3n−6. Ergo, G is edge extremal.
2
We now switch our attention to the remaining “extremal” classes H and H .
0 1
1.4 Characterizations of H and H
0 1
In general, members of H and H may not be obtained from a tree by isomorphic leaf
0 1
matching, unlike the members of H ,H and H . To see this, we discuss a couple of examples
2 3 4
that are shown in Figure 6; using the ear decomposition theorem (1.1) and Lemma 1.6, the
reader may easily verify that both graphs belong to H. By counting, one may infer these
graphs belong to H and H , respectively. For the graph shown in Figure 6a, deleting
0 1
all of the 2-edges (displayed in blue) results in precisely two components that are trees
but nonisomorphic. On the other hand, for the graph shown in Figure 6b, deleting all of
the 2-edges results in two isomorphic trees; however, the resultant graph is not obtained
by isomorphic leaf matching operation. Interestingly, we are able to reduce members of
H and H to members of H and H , respectively, using the notion of “partial retract” that
0 1 2 4
we describe next.
(a) a member of H (b) a member of H
0 1
Figure 6: extremal graphs that may not be obtained from a tree by isomorphic leaf matching
Let G be a graph and v be a vertex of degree two that has two distinct neighbours, say
v and v . Let G′ denote the graph obtained from G by contracting the two edges vv
1 2 1
and vv . We say that G′ is obtained from G by bicontraction (of v), and we denote it by
2
G′ := G/v; see Figure 15. Furthermore, if each of v and v has degree at least three in G,
1 2
we say that G′ is obtained from G by restricted bicontraction (of v); see Figure 16. Note
that restricted bicontraction may be performed if and only if the subgraph of G induced by
its degree two vertices has an isolated vertex.
We define the partial retract of G as the graph G(cid:98) obtained by repeatedly applying the restricted bicontraction operation until the resulting graph has the property that the subgraph
induced by its degree two vertices has no isolated vertex. Observe that given a graph G, its
partial retract G(cid:98) is unique; Figure 7 shows an example.
Using the notion of partial retract, we are able to relate the extremal class H with the
0
extremal class H , as stated below.
2
8

<!-- Page 9 -->

Theorem 1.9. [Characterization of H ]
0
A graph G, distinct from C , is a 2-edge extremal minimal bipartite matching covered graph
4
if and only if its partial retract G(cid:98) is a 2-vertex extremal minimal bipartite matching covered
graph.
(a) G ∈ H
0
(b) G(cid:98) ∈ H
2
Figure 7: an illustration of Theorem 1.9 that relates H and H
0 2
To see an example of the above theorem, consider the graph G shown in Figure 7a and
its partial retract G(cid:98) shown in Figure 7b. The reader may verify using Theorem 1.1 and
Lemma 1.6 that G and G(cid:98) belong to H. Note that G ∈ H as |E (G)| = m−n+2. On the
0 2
other hand, G(cid:98) ∈ H as |V (G(cid:98))| = 2(m−n+2).
2 2
Likewise, using the notion of partial retract, we are able to relate the extremal class H
1
with the extremal class H , as stated below.
4
Theorem 1.10. [Characterization of H ]
1
A graph G is a 2-edge n-extremal minimal bipartite matching covered graph if and only if its
partial retract G(cid:98) is an edge extremal minimal bipartite matching covered graph and ∆(G) = 3.
(a) G ∈ H
1
(b) G(cid:98) ∈ H
4
Figure 8: an illustration of Theorem 1.10 that relates H and H
1 4
To see an example of the above theorem, consider the graph G shown in Figure 8a and
its partial retract G(cid:98) shown in Figure 8b. The reader may verify using Theorem 1.1 and
Lemma 1.6 that G and G(cid:98) belong to H. Note that G ∈ H as |E (G)| = n+10. On the other
1 2 6
hand, G(cid:98) ∈ H as |E(G(cid:98))| = 3n−6.
4 2
We have thus stated our characterizations for all of the extremal classes shown in Table 1.
We now proceed to discuss further relations between them.
9

<!-- Page 10 -->

1.5 Containment poset for the extremal classes
In order to discuss the containment relationships between different extremal classes, we shall
find it convenient to exclude the cycle graphs. Following Lucchesi and Murty [12], for an
element t and a set S, we use S − t to denote the set obtained from S by deleting t. It
follows from the definitions of the extremal classes (see Table 1) that neither of H and H
0 1
contains any cycle graph, that C is the only cycle in H as well as in H , whereas C is the
4 2 3 6
only cycle in H . In light of this, we let H∗ := H −C , H∗ := H −C and H∗ := H −C .
4 2 2 4 3 3 4 4 4 6

## H

0
4.2
7.11

## H∗

2
7.2

## H H∗ 7.4

1 3

## H∗

4

### Figure 9: The Θ graph {Θ}


### Figure 10: Containment poset

Figure 10 shows the containment poset for all of the extremal classes. For instance, the
arrow from H to H , labelled as 7.11, is to be read as follows: Corollary 7.11 states that
1 0
H ⊂ H . Additionally, our characterizations imply that H ∩H = H ∩H = {Θ} where
1 0 1 2 3 4
Θ is the graph shown in Figure 9; see Corollaries 7.5 and 7.12.
1.6 Organization of the rest of this paper
In the rest of the paper (except the last section), we will prove the difficult directions of
Theorems 1.3, 1.4 and 1.5, and we will also prove Theorems 1.9 and 1.10.
We first focus on the class H . In order to prove the Main Theorem (1.3), we need some
2
known properties of bipartite matching covered graphs and minimal bipartite matching covered graphs; these are discussed in Sections 2 and 3. In particular, in Section 3, we state and
prove the lower bound on the number of 2-edges due to Lova´sz and Plummer [11], and we
deduce an easy lower bound on the number of degree two vertices. In Section 4, we enforce
equality in its proof to infer some useful properties of members of H — one of which is the
2
existence of “balanced” 2-cuts. We then develop an induction tool using balanced 2-cuts in
Section 5. In Section 6, we prove the Main Theorem (1.3).
InSection7, weaddresstheothernotionsofextremality. InSubsections7.1and7.2, wefirst
state and prove the bounds corresponding to the classes H and H , respectively; thereafter,
3 4
10

<!-- Page 11 -->

we enforce equality in their proofs to deduce their characterizations (Theorems 1.4 and 1.5)
using the Main Theorem (1.3). In Subsection 7.3, we prove our characterization of H
0
(Theorem1.9). Lastly, inSubsection7.4, weproveourcharacterizationofH (Theorem1.10)
1
using the characterization of H .
0
Finally, inSection8, weconsiderproblemssimilartothosesolvedbyCorollaries3.5, 7.1and
7.3 in the context of “minimal k-extendable” bipartite graphs. We first discuss the bounds
established by Lou [10] and then proceed to conjecture stronger bounds; see Conjectures
8.9, 8.10 and 8.11. In the rest of that section, we provide evidence for our conjectures by
constructing tight examples that are straightforward generalizations of the ones that appear
in the 1-extendable case.
2 Ear decomposition theory
Recall that a subgraph H of a graph G is conformal if G−H is matchable. It is easy to see
that, in a matching covered graph, there is a conformal cycle containing any two adjacent
edges. As an immediate consequence, we get the following.
Proposition 2.1. Let G be a matching covered graph, let u be a vertex of degree at least
three and let e ∈ ∂(u). Then there is a conformal cycle C such that u ∈ C but e ∈/ C.
In fact, Little [9] proved the stronger statement that any two edges (not necessarily adjacent) lie in a conformal cycle; we will not require this.
Recall that an ear of a subgraph H in a graph G is an odd path of G whose ends are in H
but is otherwise disjoint from H. We will now discuss the proof of the Ear Decomposition
Theorem (1.1) as it appears in Lova´sz and Plummer [11, Theorem 4.1.6]. In particular, we
extract a couple of lemma statements that are implicit in their proof. The first of these
shows that “adding an ear” preserves the matching covered property. For a subgraph H and
an ear P of H, the subgraph H ∪P is said to be obtained by adding the ear P to H.
Lemma 2.2. Let G be a bipartite graph, H be a matching covered subgraph and P be an ear
of H in G. Then H ∪P is matching covered.
The second lemma establishes the existence of an ear of any conformal matching covered
proper subgraphH with the additional constraint that any specified edge “stickingout of H”
is included in the ear.
Lemma 2.3. Let G be a bipartite matching covered graph, H be any conformal matching
covered subgraph and e ∈/ H denote an edge that has at least one end in H. Then there exists
an ear of H, say P , containing e such that H∪P is a conformal matching covered subgraph
e e
of G.
The reader may verify that the above two lemmas imply the following stronger version of
the Ear Decomposition Theorem (1.1) that is also stated in Lova´sz and Plummer [11, pg
126].
Theorem 2.4. For any conformal matching covered subgraph H of a bipartite matching
11

<!-- Page 12 -->

covered graph G, there exists an ear decomposition of G in which H appears as one of the
subgraphs.
In the next section, we discuss the proofs of the lower bounds on the number of 2-edges
due to Lov´asz and Plummer [11, Theorem 4.2.7]. These proofs rely heavily on the ear
decomposition theory, and we will need some of their details to prove our results.
3 Lower bounds established by Lov´asz and Plummer
Recall that, for a matching covered graph G, an edge e is removable if G − e is matching
covered. Thus, G is minimal if and only if it has no removable edges. It follows from
Theorem 1.1 that, given any ear decomposition of a bipartite matching covered graph G,
every trivial ear (that is, an ear comprising a single edge) is a removable edge in G. This
observation, coupled with Theorem 2.4, yields the following; see Lova´sz and Plummer [11,
Theorem 4.2.1].
Lemma 3.1. Every conformal matching covered subgraph of a minimal bipartite matching
covered graph is an induced subgraph.
In order to establish their lower bound on the number of 2-edges in a minimal bipartite
matching covered graph, Lova´sz and Plummer proved a lower bound for each element (the
starting conformal cycle and each ear) of an ear sequence. The following is their lemma for
ears.
Lemma 3.2. Let G be a minimal bipartite matching covered graph and let (C,P ,P ,...,P )
1 2 r
be any ear sequence. Then each ear P contains a 2-edge of G.
i
Note that the above lemma (see Lova´sz and Plummer [11, Lemma 4.2.4]) refers to degrees
in the original graph G. Adding a nontrivial ear P clearly creates a 2-edge in the resultant
i
subgraph. However, onemayaddearslatertherebyincreasingthedegreesofinternalvertices
of P and possibly destroying all 2-edges of P in the final graph G. The above lemma states
i i
that at least one such 2-edge survives in G. We now switch our attention to conformal cycles.
Let G be a minimal bipartite matching covered graph that is not a cycle. Using Lemma 3.2
and some standard ear decomposition tricks, one may infer that each conformal cycle C of G
contains a pair of 2-edges that are separated in C by vertices that have degree at least three
(in G). Interestingly, the same holds even for cycles that are not conformal; see Lov´asz and
Plummer [11, Corollary 4.2.5].
A matching M is induced if the subgraph induced by V(M) contains precisely the edges
of M. The facts stated in the above paragraph, along with Lemma 3.1, imply the following
(that is easily verified in the case in which the graph itself is a cycle of order six or more).
Corollary 3.3. In a minimal bipartite matching covered graph, distinct from C , each con-
4
formal cycle contains a pair of 2-edges that comprise an induced matching.
We now invoke Lemma 3.2 and Corollary 3.3, and the fact that the length of any ear
sequence is m−n+1, to deduce the following lower bound result that is a mild strengthening
12

<!-- Page 13 -->

of what is stated in Lov´asz and Plummer; see [11, Theorem 4.2.7].
Theorem 3.4. A minimal bipartite matching covered graph, distinct from C , has an induced
4
matching of size at least m−n+2, each of whose members is a 2-edge.
Proof. Let G be a minimal bipartite matching covered graph and (C,P ,...,P ) be any ear
1 r
sequence. By Corollary 3.3, the conformal cycle C has a pair of 2-edges, say e and e′, that
compriseaninducedmatchingofG. ByLemma3.2, eachearP hasa2-edge, saye . Observe
i i
that each end of e and e′ has both its neighbours in C. Likewise, each end of e has both its
i
neighbours in P . Furthermore, the ends of each ear P have degree at least three in G. All
i i
of these observations imply that the set F := {e,e′,e ,e ,...,e } is an induced matching of
1 2 r
G and each of its members is a 2-edge. Also, r = m−n. Thus, |F| = m−n+2.
The following lower bound on the number of vertices of degree two comes for free.
Corollary 3.5. In a minimal bipartite matching covered graph, |V | ⩾ 2(m−n+2).
2
Proof. The statement clearly holds for C . Now, let G be a minimal bipartite matching
4
covered graph, distinct from C , and let F denote a maximum induced matching, each of
4
whose members is a 2-edge. Clearly, |V | ⩾ 2|F|. By Theorem 3.4, |F| ⩾ m−n+2. Thus,
2
|V | ⩾ 2(m−n+2).
2
Throughout the next three sections, for the sake of brevity, we shall use the term extremal
to refer to 2-vertex extremal — that is, those minimal bipartite matching covered graphs
that satisfy the bound in Corollary 3.5 with equality.
4 Properties of extremal graphs
In this section, we establish some useful properties of this class including the “balanced
2-cut” property that is crucial for our inductive proof of Theorem 1.3 that characterizes this
class. To this end, we shall enforce equality in the proofs of Corollary 3.5 and Theorem 3.4.
Lemma 4.1. Every extremal minimal bipartite matching covered graph, distinct from C ,
4
satisfies the following:
(i) E is a perfect matching of G[V ] and |E | = m−n+2,
2 2 2
(ii) each ear in any ear decomposition has exactly one 2-edge, and
(iii) each conformal cycle has precisely two 2-edges.
Proof. Let G be an extremal minimal bipartite matching covered graph, distinct from C ,
4
and let F denote an induced matching of maximum cardinality, each of whose members is a
2-edge, as in the proof of Corollary 3.5. Since, by definition, |V | = 2(m−n+2), equality
2
holds everywhere in the proof of Corollary 3.5. In particular, |F| = m−n+2 and |V | = 2|F|;
2
thus V = V(F). Observe that, since F is an induced matching, E = F. Consequently, E
2 2 2
is a perfect matching of G[V ] and |E | = m−n+2. This proves (i).
2 2
13

<!-- Page 14 -->

Now, let (C,P ,...,P ) be any ear sequence of G. Since |F| = m−n+2, equality holds
1 r
everywhereintheproofofTheorem3.4. Furthermore, usingthefactthat|E | = m−n+2, we
2
infer that the conformal cycle C contributes exactly two 2-edges, and each ear P contributes
i
precisely one 2-edge, to the set E . This proves (ii) and (iii).
2
Using Lemma 4.1 (i), we immediately deduce the following containment.
Corollary 4.2. H −C ⊂ H .
2 4 0
We now derive, using the above lemma and simple counting arguments, a few additional
properties of this extremal class. In order to do so, we need some notation and terminology
that we define next.
Following Lova´sz and Plummer [11], we call an edge (of a graph G) a 3-edge if each of
its ends has degree at least three, and we use E (G) to denote the set comprising these
3
edges. In the same spirit, we use V (G) to denote the set of vertices of degree at least three.
3
Technically, it should be denoted by V (G). However, throughout this paper, we distinguish
⩾3
between vertices of degree two and the rest — that is, vertices of degree three or more. So,
for the sake of brevity, we drop “⩾” from the notation. Finally, we use E (G) to denote
3,2
the set of those edges that join a vertex of degree two with a vertex of degree at least three.
As usual, if the graph G is clear from the context, we shall drop G from these notations.
Note that E = ∂(V ) = ∂(V ).
3,2 3 2
Now, let G be an extremal minimal bipartite matching covered graph distinct from C . By
4
definition, |V | = n − |V | = 3n − 2m − 4. By Lemma 4.1, each vertex of degree two has
3 2
exactly one neighbour of degree at least three; consequently, |E | = |V | = 2(m−n+2).
3,2 2
Lastly, |E | = m−|E |−|E | = 3n−2m−6. Also, since |V | = 3n−2m−4, it follows
3 2 3,2 3
that |E | = |V |−2. This proves the following.
3 3
Corollary 4.3. Every extremal minimal bipartite matching covered graph, distinct from C ,
4
satisfies the following:
(i) |V | = 3n−2m−4,
3
(ii) |E | = 2m−2n+4, and
3,2
(iii) |E | = 3n−2m−6 = |V |−2.
3 3
We shall now use Lemma 4.1 to prove the “balanced 2-cut” property of extremal minimal
bipartite matching covered graphs that was alluded to at the beginning of this section.
4.1 Balanced 2-cut property
For a cut ∂(W) of a bipartite graph G[A,B], we classify the edges of ∂(W) into two types,
depending upon the color classes of their ends in W. We use ∂A(W) to denote those edges of
∂(W) whose end in W belongs to A. The set ∂B(W) is defined analogously. The cut ∂(W)
is balanced if |∂A(W)| = |∂B(W)|. In our work, balanced 2-cuts play a crucial role. Note
that a 2-cut ∂(W) is balanced if |∂A(W)| = |∂B(W)| = 1. We are now ready to prove the
balanced 2-cut property stated below.
14

<!-- Page 15 -->


### Theorem 4.4. [Balanced 2-cut Property]

In an extremal minimal bipartite matching covered graph, each 3-edge participates in a balanced 2-cut with some other 3-edge.
Proof. Let G[A,B] denote an extremal minimal bipartite matching covered graph and let
e := ab denote any 3-edge so that a ∈ A. We intend to show the existence of another 3-edge,
say f, such that {e,f} is a balanced 2-cut.
By Proposition 2.1, there is a conformal cycle C such that a ∈ C and e ∈/ C. Now, let
H be a maximal conformal matching covered subgraph of G such that a ∈ H and e ∈/ H.
By Lemma 3.1, H is induced; thus b ∈/ H. In particular, e ∈ ∂A(H). We shall demonstrate
that ∂(H) is the desired balanced 2-cut. In order to do so, we state and prove specific
claims; within their proofs, we shall invoke ear decomposition results (namely, Lemma 2.3
and Theorem 2.4) several times without mentioning it explicitly.
4.4.1. ∂A(H) = {e}.
Proof. Suppose not; then there is an edge f ̸= e in ∂A(H). Now, there is an ear P of
f
H containing f. Observe that e ∈/ P since P is odd. Thus, H′ := H ∪ P is a larger
f f f
conformal matching covered subgraph of G such that a ∈ H′ and e ∈/ H′; this contradicts
the maximality of H. This proves that ∂A(H) = {e}.
In the proofs of the next two claims, every instance of 2-edge refers to the condition of being
a 2-edge in the graph G similar to our earlier discussion (after the proof of Lemma 3.2).

## |∂B(H)| = 1.

Proof. Since G is 2-connected, |∂B(H)| ⩾ 1. Now suppose that f and f are distinct edges
1 2
in ∂B(H) and let b and b denote their (not necessarily distinct) ends in H, respectively.
1 2
Now, there is an ear P′ of H containing f (which must also contain e). Furthermore, there
1
is an ear P of H ∪ P′ containing f . Let x ∈ A be the end of P distinct from b (see
2 2 2 2
Figure 11a). Observe that x ∈/ H since ∂A(H) = {e} and e ∈ P′. Thus, x is an internal
vertex of P′. Consequently, x splits P′ into two paths, say P := aP′x and P := xP′b . Note
1 1
that P is an ear of H ∪ (P + P ) = H ∪ P′; likewise, P is an ear of H ∪ (P + P ). By
2 1 1 2
Lemma 4.1 (ii), each of P′, P and P has exactly one 2-edge. Since P is a subpath of P′,
1 2 1
we conclude that P is free of 2-edges. Furthermore, by Lemma 4.1 (i), each vertex of P has
degree at least three in G.
Now, let y be the neighbour of x in P. As discussed above, d (y) ⩾ 3. So, there is an ear

## G

P of H ∪(P +P )∪P starting from y. Let z be the other end of P . Observe that z ∈/ H
y 1 2 y
as ∂A(H) = {e}.
Now, suppose that z ∈ P (see Figure 11b). Note that the conformal matching covered
subgraph H ∪(P +P )∪P can also be obtained from H by adding the ears aPzP yxP b
1 y y 1 1
and yPz in that order. However, yPz has no 2-edges since, as noted earlier, each vertex of
P has degree at least three in G. This contradicts Lemma 4.1 (ii). Thus, z ∈/ P.
15

<!-- Page 16 -->

e e
a P a P
z

## H H P

y y
f P f P
b 1 1 b 1 1
1 xx 1 xx
b b
2 f P 2 f P
2 2 2 2
(a) illustration of H ∪(P +P )∪P (b) illustration of P when z ∈ P
1 2 y
e e
a P a Q

## H P H

y y y
f P z f z
b 1 1 b 1
1 xx 1 xx
b b
2 f 2 P 2 2 f 2 Q′
(c) illustration of P when z ∈ P (d) illustration of the ears Q,Q′ and xy
y 1

### Figure 11: illustrations for the proof of statement 4.4.2

Thus, z ∈ P ∪P . Adjust notation so that z ∈ P (see Figure 11c). Let Q := aPyP zP b
1 2 1 y 1 1
andQ′ := zP xP b (seeFigure11d). Observethattheconformalmatchingcoveredsubgraph
1 2 2
H∪(P +P )∪P ∪P can also be obtained from H by adding the ears Q, Q′ and xy in that
1 2 y
order. In particular, H ∪Q∪Q′ is a conformal matching covered subgraph of G that is not
induced. This contradicts Lemma 3.1. Thus, |∂B(H)| = 1.
Let f denote the unique edge of ∂B(H). Note that ∂(H) = {e,f} is indeed a balanced
2-cut. It remains to prove the following claim.
4.4.3. f is a 3-edge.
Proof. We let f := uv where v ∈ V(H) ∩ B. As H is matching covered, d (v) ⩾ 2; thus

## H

d (v) ⩾ 3. Suppose to the contrary that d (u) = 2. By Lemma 4.1 (i), the neighbour of u

## G G

distinct from v, say w, has degree two in G. Let P be an ear of H containing f. Observe that
uw,e ∈ P. By Lemma 4.1 (ii), uw is the only 2-edge of P. Furthermore, by Lemma 4.1 (i),
each internal vertex of P, distinct from u and w, has degree at least three in G.
Since d (b) ⩾ 3, there is an ear P′ of H ∪P starting from b (see Figure 12a). Let x ∈ A

## G

be the other end of P′. Observe that x is an internal vertex of P that is distinct from u.
Let Q := abP′xPv and Q′ := bPx (see Figure 12b). Observe that the conformal matching
covered subgraph H ∪ P ∪ P′ can also be obtained from H by adding the ears Q and Q′
in that order. It follows from the preceding paragraph that each vertex of Q′ has degree at
least three in G. Consequently, the ear Q′ has no 2-edges. This contradicts Lemma 4.1 (ii).
Thus, d (u) ⩾ 3 and f is indeed a 3-edge.

## G

16

<!-- Page 17 -->

e e
a b a b

## P′ Q′


## H P H Q

x x
v v
u w u w
f f
(a) illustration of H ∪P ∪P′ (b) illustration of the ears Q and Q′
Figure 12: illustrations for the proof of statement 4.4.3
This completes the proof of Theorem 4.4.
Note that Theorem 4.4 does not hold for all minimal bipartite matching covered graphs —
that is, it requires the extremality hypothesis. As we noted in Section 1, the graph G shown
in Figure 5 is a minimal bipartite matching covered graph. Observe that e is a 3-edge that
is not contained in any 2-cut since G−e is 2-connected.
In the next section, we establish an induction tool based on balanced 2-cuts. This tool,
coupled with Theorem 4.4, will be used in Section 6 to prove the Main Theorem (1.3).
5 An induction tool using balanced 2-cuts
We begin this section by defining an operation that “breaks” a given bipartite graph, that
has a balanced 2-cut, into “smaller” bipartite graphs, and its converse operation.
Let G[A,B] denote a bipartite graph that has a balanced 2-cut, say F := ∂(X). Let
H := G[X] and H := G[X]. As F is balanced, for each i ∈ {1,2}, let a ∈ A and b ∈ B
1 2 i i
denote the ends of the edges of F in H , as shown in Figure 13a. Let G be the graph
i 1
obtained from H by adding the ear a v u b (of length three), as shown in Figure 13b. The
1 1 1 1 1
graph G is obtained from H analogously. We say that the (bipartite) graphs G and G
2 2 1 2
are obtained from G by a balanced 2-cut decomposition, or simply by a 2-cut decomposition,
across the 2-cut F. Note that u v is a 2-edge in G ; likewise, u v is a 2-edge in G .
1 1 1 2 2 2
Conversely, let G and G be disjoint bipartite graphs, each of which has a 2-edge, say u v
1 2 1 1
and u v , respectively. Let a denote the neighbour of v that is distinct from u , and let b
2 2 1 1 1 1
denote the neighbour of u that is distinct from v , as shown in Figure 13b. The vertices a
1 1 2
and b are defined analogously. Let G be the graph obtained from G ∪G by deleting the
2 1 2
vertices u ,v ,u and v , and adding the edges a b and a b , as shown in Figure 13a. We
1 1 2 2 1 2 2 1
say that the (bipartite) graph G is obtained from G and G by 2-edge splicing across the
1 2
pair of 2-edges {u v ,u v }. Note that {a b ,a b } is a balanced 2-cut of G.
1 1 2 2 1 2 2 1
Observe that the 2-cut decomposition operation is the “inverse” of the 2-edge splicing
operation — that is, G and G are obtained from G by 2-cut decomposition across a
1 2
17

<!-- Page 18 -->

balanced 2-cut if and only if G is obtained from G and G by 2-edge splicing across a pair
1 2
of 2-edges. We now show that these operations preserve the matching covered, minimality
and extremality properties.
a 1 b 2 a 1 b 2
v u
1 2
u v
1 2
b 1 a 2 b 1 a 2
H 1 := G[X] H 2 := G[X] G 1 G 2
(a) G (b) G and G
1 2
Figure 13: illustration of balanced 2-cut decomposition and 2-edge splicing

### Theorem 5.1. [Balanced 2-cut Induction Tool]

Let G be a bipartite graph that has a balanced 2-cut F, and let G and G be the (bipartite)
1 2
graphs obtained from G by a 2-cut decomposition across F. Then the following statements
hold:
(i) G is matching covered if and only if G and G are both matching covered;
1 2
(ii) furthermore, G is minimal if and only if G and G are both minimal; and
1 2
(iii) finally, G is extremal if and only if G and G are both extremal.
1 2
Proof. We adopt all of the notations from the above definition of 2-cut decomposition, as
shown in Figure 13. We will prove the three statements one by one.

#### G is matching covered if and only if G and G are both matching covered.

1 2
Proof. First suppose that G is matching covered. Let C denote a conformal cycle containing
a b . Note that a b ∈ C as well. Let (C,P ,...,P ) be an ear sequence of G; its existence
1 2 2 1 1 r
is guaranteed by Theorem 2.4. Observe that each ear P is a subgraph of exactly one of
i
H and H . Let P ,P ,...,P denote those ears that are subgraphs of H and appear
1 2 11 12 1r1 1
in that order in the ear sequence (C,P ,...,P ). Let C := (C ∩H )+a v u b . Observe
1 r 1 1 1 1 1 1
that (C ,P ,P ,...,P ) is an ear sequence of G . Thus, by the Ear Decomposition
1 11 12 1r1 1
Theorem (1.1), the bipartite graph G is matching covered. An analogous argument proves
1
that G is matching covered.
2
Conversely,supposethatG andG arematchingcovered. LetC beaconformalcycleofG
1 2 i i
containingthe2-edgeu v fori ∈ {1,2}. Let(C ,P ,P ,...,P )and(C ,P ,P ,...,P )
i i 1 11 12 1r1 2 21 22 2r2
be ear sequences of G and G , respectively; these exist due to Theorem 2.4. Let C :=
1 2
(C −u −v )+(C −u −v )+a b +a b . Observethat(C,P ,P ,...P ,P ,P ,...,P )
1 1 1 2 2 2 1 2 2 1 11 12 1r1 21 22 2r2
is an ear sequence of G. Thus, by the Ear Decomposition Theorem (1.1), G is matching
covered.
18

<!-- Page 19 -->

Henceforth, we assume that G is matching covered, or equivalently that G and G are
1 2
both matching covered.

#### G is minimal if and only if G and G are both minimal.

1 2
Proof. First suppose that G is minimal. We claim that G is also minimal. Suppose not, and
1
let e be a removable edge of G . Note that e ∈ H since each of the remaining three edges
1 1
has an end of degree two. Observe that G −e and G are obtained by a 2-cut decomposition
1 2
of G−e. Consequently, by 5.1.1, the graph G−e is matching covered; this contradicts the
minimality of G. Thus, G is minimal. Likewise, G is minimal.
1 2
Conversely, suppose that G and G are both minimal. We claim that G is minimal.
1 2
Suppose not, and let e be a removable edge of G. Note that, since F is 2-cut, e belongs to
exactly one of H and H . Adjust notation so that e ∈ H . As in the preceding paragraph,
1 2 1
G −e and G are obtained by a 2-cut decomposition of G−e. Thus, by 5.1.1, the graph
1 2
G −e is matching covered; this contradicts the minimality of G . Hence, G is minimal.
1 1
Henceforth, we assume that G is a minimal bipartite matching covered graph, or equivalently that G and G are both minimal bipartite matching covered graphs.
1 2

#### G is extremal if and only if G and G are both extremal.

1 2
Proof. In order to argue extremality, we find it convenient to use λ := |V (G)|−2(m−n+2)
2
to denote the “surplus” vertices of degree two in G. Analogously, we define λ and λ for
1 2
the graphs G and G , respectively. By Corollary 3.5, since all three graphs are minimal
1 2
bipartite matching covered graphs, the quantities λ, λ and λ are non-negative. Note that
1 2
G is extremal if and only if λ = 0. Likewise, for i ∈ {1,2}, the graph G is extremal if and
i
only if λ = 0. Thus, it suffices to prove that λ = 0 if and only if λ = 0 and λ = 0.
i 1 2
For i ∈ {1,2}, we let n := |V(G )| and m := |E(G )|. The reader may find it useful to
i i i i
look at Figure 13. Note that n + n = n + 4 and m + m = m + 4. Observe that each
1 2 1 2
vertex w of G corresponds to a vertex of G or of G (that is distinct from u ,v ,u and v )
1 2 1 1 2 2
whose degree is the same as that of w. This implies that |V (G )|+|V (G )| = |V (G)|+4.
2 1 2 2 2
Using these three equalities, and the definitions of λ,λ and λ :
1 2
λ +λ =|V (G )|+|V (G )|−2(m +m −n −n +4)
1 2 2 1 2 2 1 2 1 2
=|V (G)|+4−2(m−n+4)
2
=|V (G)|−2(m−n+2) = λ
2
Thus, since λ,λ ,λ are non-negative, λ = 0 if and only if λ = 0 as well as λ = 0.
1 2 1 2
This completes the proof of Theorem 5.1.
19

<!-- Page 20 -->

6 Main Theorem: Characterization of H
2
Inthissection, weproveourMainTheorem(1.3)thatprovidesacharacterizationofextremal
minimal bipartite matching covered graphs. Before doing so, we prove a lemma that will be
used in the base case of our inductive proof.
Lemma 6.1. Every extremal minimal bipartite matching covered graph, that has precisely
two vertices of degree at least three, is obtained from a star by isomorphic leaf matching.
Proof. Let G be an extremal minimal bipartite matching covered graph with precisely two
vertices of degree at least three, say a and b. Let (C,P ,...,P ) be an ear sequence. Clearly,
1 r
G is not a cycle; thus r ⩾ 1. Also, each end of each ear P has degree at least three in
i
G. Thus, every ear is an ab-path. Consequently, a,b ∈ C. By Lemma 4.1 (ii), each P has
i
length three. Furthermore, by Lemma 4.1 (iii), the vertices a and b split C into two paths
— each of length three. In particular, C is a 6-cycle. Observe that G is indeed obtained
from the star K by isomorphic leaf matching.
1,r+2
We will now use the balanced 2-cut property (Theorem 4.4) and the balanced 2-cut induction tool (Theorem 5.1), along with the above lemma, to prove our characterization of the
class of extremal minimal bipartite matching covered graphs.
Theorem 1.3. [Main Theorem: Characterization of H ]
2
A graph G belongs to H if and only if it is obtained from a Halin tree by isomorphic leaf
2
matching.
Proof. The reverse implication is simply the main statement of Theorem 1.8 that we have
already proved.
For the forward direction, we let G[A,B] denote a member of H , and we proceed by
2
induction on the order of G. First suppose that |V | ⩽ 2. Since |A| = |B|, it follows that
3
|V | ∈ {0,2}. If |V | = 0, then G is a cycle and |V| = |V | = 2(m−n+2) = 4; thus G is C .
3 3 2 4
On the other hand, if |V | = 2, we invoke Lemma 6.1. In either case, we conclude that G is
3
obtained from a Halin tree by isomorphic leaf matching.
Now, suppose that |V | ⩾ 3. By Corollary 4.3 (iii), we note that |E | = |V |−2 ⩾ 1, and
3 3 3
we let a b denote a 3-edge. By Theorem 4.4, there exists another 3-edge b a such that
1 2 1 2
{a b ,b a } is a balanced 2-cut, say ∂(X), where {a ,b } ⊆ X ⊂ V(G). Now, let G and G
1 2 1 2 1 1 1 2
be the graphs obtained by 2-cut decomposition across ∂(X) = {a b ,b a }. In particular,
1 2 1 2
G is obtained from G[X] by adding the ear a v u b ; likewise, G is obtained from G[X] by
1 1 1 1 1 2
adding the ear a v u b . See Figure 13 for an illustration.
2 2 2 2
By Theorem 5.1, each of G and G belongs to H . Since each of a ,b ,a and b has degree
1 2 2 1 1 2 2
at least three in G, it follows that each of X and X has at least four vertices. This implies
that 6 ⩽ |V(G )| < |V(G)| for each i ∈ {1,2}. Thus, by the induction hypothesis, each of
i
G and G is obtained from a Halin tree by isomorphic leaf matching; also, neither of them is
1 2
isomorphic to C . By Proposition 1.2, for each i ∈ {1,2}, the graph G −E (G ) has precisely
4 i 2 i
20

<!-- Page 21 -->

two components that are isomorphic Halin trees, say T and T′. We let ϕ : V(T ) (cid:55)→ V(T′)
i i i i i
denotethecorrespondingisomorphismaspertheisomorphicleafmatchingusedtoobtainG .
i
T 1 a 1 v u b 2 T 2 T a 1 b 2
1 2
u v
1 2

## T

1
′ b
1
a
2

## T

2
′ T′ b
1
a
2
(a) G (b) G (c) G
1 2

### Figure 14: illustration for the proof of the Main Theorem

Since u v is a 2-edge of G , we may adjust notation so that v ,a ∈ T and u ,b ∈ T′.
1 1 1 1 1 1 1 1 1
See Figure 14. Likewise, we adjust notation so that u ,b ∈ T and v ,a ∈ T′. Note that
2 2 2 2 2 2
ϕ (v ) = u . Consequently, ϕ (a ) = b . Likewise, ϕ (b ) = a . We let T := (T − v ) +
1 1 1 1 1 1 2 2 2 1 1
(T −u )+a b and T′ := (T′ −u )+(T′ −v )+a b . Note that T and T′ are Halin trees.
2 2 1 2 1 1 2 2 2 1
Observe that ϕ : V(T) (cid:55)→ V(T′), as defined below, is an isomorphism between T and T′.
(cid:40)
ϕ (v) if v ∈ V(T )
1 1
ϕ(v) :=
ϕ (v) if v ∈ V(T )
2 2
Finally, note that G is obtained from T and T′ by isomorphic leaf matching as per the
above defined isomorphism. This completes the proof of the Main Theorem.
7 Other notions of extremality
We now shift our focus to the remaining notions of extremality — that is, the extremal
classes H , H , H and H — in that order.
3 4 0 1
7.1 Characterization of H
3
We begin by deducing the lower bound on the number of degree two vertices in a minimal
bipartite matching covered graph solely in terms of n, that was stated in Subsection 1.1,
from the lower bound of Lova´sz and Plummer (Corollary 3.5).
Corollary 7.1. In a minimal bipartite matching covered graph, |V | ⩾ n +2.
2 2
Proof. Using the fact that n = |V |+|V |, and the handshaking lemma:
2 3
(cid:32) (cid:33) (cid:32) (cid:33)
(cid:88) d(v) 3 1
m−n = +|V | −n ⩾ |V |+|V | −n = |V |
2 3 2 3
2 2 2
v∈V3
21

<!-- Page 22 -->

We invoke Corollary 3.5 to infer that |V | ⩾ 2(m − n + 2) ⩾ |V | + 4 = n − |V | + 4.
2 3 2
Consequently, |V | ⩾ n +2.
2 2
We are now ready to prove our characterization for H . To this end, we shall enforce
3
equality in the proof of the above corollary.
Theorem 1.4. [Characterization of H ]
3
A graph G belongs to H if and only if it is obtained from a cubic Halin tree by isomorphic
3
leaf matching.
Proof. The reverse implication is simply statement (i) of Theorem 1.8 that we have already
proved. It remains to prove the forward implication.
Let G be a member of H . That is, G is a minimal bipartite matching covered graph such
3
that |V | = n+2. Thus, G satisfies each inequality in the proof of Corollary 7.1 with equality.
2 2
Firstly, |V | = 2(m−n+2); thus G ∈ H . By the Main Theorem (1.3), G is obtained from
2 2
a Halin tree T by isomorphic leaf matching. Secondly, each vertex in V has degree precisely
3
three in G. This implies that each non-leaf of T is cubic. Thus, T is a cubic Halin tree.
We end this section by noting the following proper containment that is established within
the above proof.
Corollary 7.2. H ⊂ H .
3 2
7.2 Characterization of H
4
We will follow the same approach as in the previous subsection. We begin by deducing the
upper bound |E| ⩽ 3n−6 (see Lova´sz and Plummer [11, Theorem 4.2.3]), that was stated in
2
Subsection 1.1, from the lower bound of Lova´sz and Plummer (Corollary 3.5).
Corollary 7.3. A minimal bipartite matching covered graph, distinct from C , has at most
4
3n−6 edges.
2
Proof. Let G[A,B] denote a minimal bipartite matching covered graph distinct from C .
4
Note that n ⩾ 6 if and only if n ⩽ 3n−6. Consequently, if G is a cycle, m = n ⩽ 3n−6.
2 2
Now suppose that G is not a cycle; in other words, |V | ⩾ 1. Since |A| = |B|, we infer
3
|V | ⩾ 2. Using Corollary 3.5 and the fact that n = |V | + |V |, we have 2(m − n + 2) ⩽
3 2 3
|V | = n−|V |. Since |V | ⩾ 2, we get 2(m−n+2) ⩽ n−2. On simplifying, we conclude
2 3 3
m ⩽ 3n−6.
2
We shall now enforce equality in the proof of the above corollary to prove our characterization of H .
4
Theorem 1.5. [Characterization of H ]
4
A graph G belongs to H if and only if it is obtained from a star by isomorphic leaf matching.
4
22

<!-- Page 23 -->

Proof. Thereverseimplicationissettledbystatement(ii) ofTheorem1.8forstarsK where
1,p
p ⩾ 3, and the paragraph above it for K . It remains to prove the forward implication.
1,2
Let G be a member of H . That is, G is a minimal bipartite matching covered graph such
4
that |E| = 3n−6. If G is a cycle, then n = 6 and G is C which is obtained from the star
2 6
K by isomorphic leaf matching.
1,2
Now, suppose that G is not a cycle. Consequently, G satisfies all of the inequalities in the
last paragraph of the proof of Corollary 7.3 with equality. In particular, |V | = 2(m−n+2)
2
and |V | = 2. In other words, G is a member of H that has precisely two vertices of degree at
3 2
least three. Thus, by Lemma 6.1, we conclude that G is obtained from a star by isomorphic
leaf matching.
Weendthissubsectionwithacoupleofeasyconsequences. Thefirstofthemisthefollowing
proper containment that is already established within the above proof.
Corollary 7.4. H −C ⊂ H .
4 6 2
Note that Θ, shown in Figure 9, belongs to H as well as H . Conversely, let G be any
3 4
graph in H ∩H . Since G ∈ H , by Theorem 1.5, G is obtained from a star T := K by
3 4 4 1,p
isomorphic leaf matching. On the other hand, since G ∈ H , by Theorem 1.4, T is a cubic
3
Halin tree. Thus p = 3; in other words, G is Θ. This proves the following.
Corollary 7.5. H ∩H = {Θ}.
4 3
7.3 Characterization of H
0
Recall the bicontraction and the restricted bicontraction operations as defined in Subsection 1.4. In this subsection, we will first show that restricted bicontraction preserves 2-edge
extremality. Then, we will use this to deduce our characterization of H .
0
In order to achieve the above, we first define the inverse of restricted bicontraction as
well as of bicontraction. Observe that the bicontraction operation (when applicable) results
in a vertex of degree at least two, whereas the restricted bicontraction operation (when
applicable) results in a vertex of degree at least four.
Let G′ be a graph with a vertex v′ of degree two or more. We partition the edges of ∂(v′)
into two sets F and F each of size at least one. Let G be obtained from G′ − v′ by
1 2
(i) introducing three new vertices v,v and v , (ii) adding two edges vv and vv , and (iii) for
1 2 1 2
each i ∈ {1,2}, adding an edge joining u and v for each uv ∈ F . See Figure 15 for an
i i
illustration. We say that G is obtained from G′ by bisplitting the vertex v′. Observe that,
in G, the vertex v has degree two and each of its neighbours v and v has degree at least
1 2
two.
Furthermore, if v′ has degree at least four and each of the sets F and F has size at least
1 2
two, we say that G is obtained from G′ by restricted bisplitting of the vertex v′. In this case,
note that the vertex v has degree two and each of its neighbours v and v has degree at
1 2
least three. See Figure 16 for an illustration.
23

<!-- Page 24 -->

v
v′
v v
1 2
(a) G (b) G′

### Figure 15: an illustration of bicontracton and bisplitting

Observe that G′ is obtained from G by bicontraction if and only if G may be obtained from
G′ by bisplitting. Likewise, G′ is obtained from G by restricted bicontraction if and only
if G may be obtained from G′ by restricted bisplitting. The following lemma pertaining to
bicontraction/bisplitting is easily proved, and may also be deduced from [2, Propositions 2.1
and 2.3].
Lemma 7.6. [Bicontraction preserves Matching Covered property]
Let G be a graph that has a vertex of degree two, say v, that has two distinct neighbours each
of which has degree two or more, and let G′ := G/v. Then G is matching covered if and only
if G′ is matching covered.
v
v′
v v
1 2
(a) G (b) G′
Figure 16: an illustration of restricted bicontraction and restricted bisplitting
However, bicontraction may not preserve minimality. For instance, the graph shown in Figure 3 belongs to H, but any application of the bicontraction operation results in a graph that
has a removable edge. On the other hand, the restricted bicontraction operation preserves
minimality as well as 2-edge extremality, as proved below.
Theorem 7.7. [Restricted Bicontraction preserves 2-edge Extremality]
Let G be a bipartite graph that has a vertex of degree two, say v, each of whose neighbours
has degree three or more, and let G′ := G/v. Then the following statements hold:
(i) G is matching covered if and only if G′ is matching covered;
(ii) furthermore, G is minimal if and only if G′ is minimal; and
(iii) finally, G belongs to H if and only if G′ belongs to H .
0 0
Proof. We adopt notation from the definition of restricted bisplitting, as shown in Figure 16.
Observe that (i) follows immediately from Lemma 7.6. Henceforth, we assume that G is
24

<!-- Page 25 -->

matching covered, or equivalently, that G′ is matching covered. We will prove the other two
statements one-by-one.

#### G is minimal if and only if G′ is minimal.

Proof. First suppose that G′ is not minimal, and let e be a removable edge. Note that
d (v ) ⩾ d (v ) − 1 ⩾ 2 since the operation is a restricted bicontraction. Consequently,

### G−e i G i

G′ −e is obtained from G−e by bicontracting v. Thus, by Lemma 7.6, G−e is matching
covered. In other words, G is not minimal.
Conversely, suppose that G is not minimal, and let e be a removable edge. Note that
e ∈/ ∂(v) since d(v) = 2. Now, observe that G′−e is obtained from G−e by bicontracting v.
Thus, by Lemma 7.6, G′ −e is matching covered. Consequently, G′ is not minimal.
Henceforth, we assume that G is a minimal bipartite matching covered graph, or equivalently, that G′ is a minimal bipartite matching covered graph. Recall that G belongs to H
0
if |E (G)| = m−n+2.
2

#### G belongs to H if and only if G′ belongs to H .

0 0
Proof. Let n′ := |V(G′)| and m′ := |E(G′)|. Note that m′ = m − 2 and n′ = n − 2.
Thus, m′ −n′ = m−n. By definition of restricted bicontraction operation, d (v ) ⩾ 3 and

## G 1

d (v ) ⩾ 3; subsequently d (v′) ⩾ 3. These observations imply that |E (G′)| = |E (G)|.

## G 2 G′ 2 2


### This completes the proof of Theorem 7.7

Recall the definition of partial retract from Subsection 1.4. The following is an immediate
consequence of the above theorem.
Corollary 7.8. A graph G belongs to H if and only if its partial retract G(cid:98) belongs to H .
0 0
We are now ready to prove our characterization of the extremal class H in terms of the
0
extremal class H , as restated below.
2
Theorem 1.9. [Characterization of H ]
0
A graph G, distinct from C , belongs to H if and only if its partial retract G(cid:98) belongs to H .
4 0 2
Proof. First suppose that G(cid:98) belongs to H . Observe that either G(cid:98) = G or G(cid:98) has a vertex of
2
degree at least four. In either case, G(cid:98) ̸= C . By the containment established in Corollary 4.2,
4
we infer that G(cid:98) ∈ H . Now, by Corollary 7.8, we conclude that G ∈ H .
0 0
NowsupposethatGbelongstoH . WeinvokeCorollary7.8toinferthatG(cid:98) ∈ H . Thus, by
0 0
definition, |E (G(cid:98))| = m−n+2, where n := |V(G(cid:98))| and m := |E(G(cid:98))|. By definition of partial
2 (cid:98) (cid:98) (cid:98) (cid:98)
retract, thesubgraphofG(cid:98) inducedbyitsdegreetwoverticeshasnoisolatedvertex. Applying
the handshaking lemma to this subgraph gives us: |V (G(cid:98))| ⩽ 2|E (G(cid:98))| = 2(m − n + 2).
2 2 (cid:98) (cid:98)
However, by the lower bound established in Corollary 3.5, |V (G(cid:98))| ⩾ 2(m − n + 2). Thus,
2 (cid:98) (cid:98)
|V (G(cid:98))| = 2(m−n+2); by definition, G(cid:98) ∈ H .
2 (cid:98) (cid:98) 2
25

<!-- Page 26 -->

We now switch our attention to the only remaining extremal class.
7.4 Characterization of H
1
We begin by deducing a lower bound on the number of 2-edges in a minimal bipartite
matching covered graph solely in terms of n (see Lova´sz and Plummer [11, Lemma 4.2.4
(b)]), that was stated in Subsection 1.1, from the lower bound of Lova´sz and Plummer
(Theorem 3.4).
Corollary 7.9. In a minimal bipartite matching covered graph, |E | ⩾ n+10.
2 6
Proof. Let G be a minimal bipartite matching covered graph. By Theorem 3.4:
|E | ⩾ m−n+2 (1)
2
Now, using the handshaking lemma, and the fact that d(v) ⩾ 3 for each v ∈ V , we have:
3
2m ⩾ 3|V |+2|V | = 3n−|V |. In particular:
3 2 2
2m ⩾ 3n−|V | (2)
2
By counting the edges incident with vertices of degree two in two different ways, we have:
2|V | = 2|E |+|E | = |E |+m−|E |. Now, using the fact that |E | ⩾ 0, we have:
2 2 23 2 3 3
|E |+m ⩾ 2|V | (3)
2 2
Now, by scaling and adding the above inequalities as (1)×5+(2)×2+(3)×1, we arrive
at the desired inequality: 6|E | ⩾ n+10.
2
Next, we invite the reader to make a simple observation pertaining to the restricted bicontraction operation.
Lemma 7.10. If a graph G has a vertex of degree two, say v, each of whose neighbours has
degree at least three, then |E (G)| = |E (G/v)|. Consequently, |E (G)| = |E (G(cid:98))|.
3 3 3 3
We are now ready to prove our characterization of the extremal class H in terms of the
1
extremal class H , as restated below.
4
Theorem 1.10. [Characterization of H ]
1
A graph G belongs to H if and only if its partial retract G(cid:98) belongs to H and ∆(G) = 3.
1 4
Proof. For the reverse direction, let G be a graph such that G(cid:98) ∈ H and ∆(G) = 3. In
4
what follows, we shall demonstrate that all of the inequalities that appear in the proof of
Corollary 7.3 hold with equality. Firstly, by the characterization of H obtained in Theo-
4
rem 1.5, we infer that |E (G(cid:98))| = 0. Thus, by Lemma 7.10, |E (G)| = |E (G(cid:98))| = 0. Secondly,
3 3 3
by the containment established in Corollary 7.4, G(cid:98) ∈ H . By Theorem 1.9, G ∈ H . In
2 0
particular, |E (G)| = m−n+2. Lastly, as ∆(G) = 3, clearly d (v) = 3 for each v ∈ V . The

## 2 G 3

reader may thus verify that equality holds in all of the inequalities discussed in the proof of
Corollary 7.9. Hence, |E (G)| = n+10 and G ∈ H .
2 6 1
26

<!-- Page 27 -->

For the forward direction, let G be a graph in H . Consequently, G satisfies all of the
1
inequalities that appear in the proof of Corollary 7.9 with equality. Firstly, |E (G)| =
2
m−n+2; thus G ∈ H . Consequently, by Theorem 1.9, G(cid:98) ∈ H . Secondly, |E (G)| = 0.
0 2 3
Thus, by Lemma 7.10, |E (G(cid:98))| = 0. By Corollary 4.3 (iii), we deduce that |V (G(cid:98))| = 2.
3 3
Hence, by Lemma 6.1 and Theorem 1.8 (ii), we conclude that G(cid:98) ∈ H . Finally, d (v) = 3

## 4 G

for each v ∈ V (G). Thus, ∆(G) ⩽ 3. Note that if G is a cycle then n = m = E = n+10
3 2 6
which implies that n = 2; a contradiction. Thus, G is not a cycle; whence ∆(G) = 3.
We end this subsection, with a couple of easy consequences. The first of them is the
following proper containment that is already established within the above proof.
Corollary 7.11. H ⊂ H .
1 0
Note that Θ, shown in Figure 9, belongs to H as well as H . Conversely, let G ∈ H ∩H .
1 2 1 2
Since G ∈ H , by Lemma 4.1 (i), E is a perfect matching of G[V ] which implies that there
2 2 2
is no vertex of degree two each of whose neighbours has degree three or more. Thus, G(cid:98) = G.
On the other hand, since G ∈ H , by Theorem 1.10, G ∈ H . Furthermore, ∆(G) = 3.
1 4
Observe that Θ is the only graph in H with maximum degree three. Thus, G = Θ; this
4
proves the following.
Corollary 7.12. H ∩H = {Θ}.
1 2
In the final section, we present conjectures that are natural generalizations of Theorems
1.3, 1.4 and 1.5 to k-extendable bipartite graphs — that we proceed to define.
8 Generalization to k-extendable bipartite graphs
For a positive integer k, a connected graph, of order least 2k +2, is k-extendable if it has a
matching of size k and each such matching extends to a perfect matching. This notion was
first introduced by Plummer [14], and has been studied extensively by various authors since
then; we impose the additional technical condition of order at least 2k +2 since otherwise
most of our results admit small counterexamples. Observe that a graph is k-extendable if
and only if its underlying simple graph is k-extendable.
Note that matching covered graphs are precisely the 1-extendable graphs. For the sake
of completeness, we also use the term 0-extendable graphs to refer to (not necessarily connected) matchable graphs. Plummer [15] proved the following regarding the connectedness
of k-extendable graphs.
Theorem 8.1. For k ⩾ 1, every k-extendable graph is (k +1)-connected.
This immediately yields the following.
Corollary 8.2. In a k-extendable graph, each vertex has degree at least k +1.
A k-extendable graph G is minimal if G − e is not k-extendable for each edge e. We
emphasize that the notion of minimality is tied with the value of k. For instance, it is easily
27

<!-- Page 28 -->

verified (using Theorem 8.3) that every 2-extendable bipartite cubic graph is a minimal
2-extendable graph, but is not minimal 1-extendable.
InlightofCorollary8.2, itisnaturaltoaskwhetherthereisalowerboundonthenumberof
degree k+1 vertices in a minimal k-extendable graph. Henceforth, we restrict our attention
to bipartite graphs.
We begin by recalling the well-known Hall’s Theorem which states that a bipartite graph
G[A,B], where |A| = |B|, is 0-extendable if and only if |N(S)| ⩾ |S| for each S ⊆ A, where
N(S) denotes the neighbourhood of S. Using this, Plummer [15] established the following
characterization of k-extendable bipartite graphs.
Theorem 8.3. [Characterization of k-extendable Bipartite Graphs]
For a bipartite graph G[A,B] of order at least 2k + 2, where |A| = |B|, the following are
equivalent:
(i) G is k-extendable,
(ii) for every nonempty subset S ⊆ A, either N(S) = B or |N(S)| ⩾ |S|+k, and
(iii) G−X −Y is matchable for all X ⊆ A and Y ⊆ B such that |X| = |Y| = k.
Note that statement (ii) in the above theorem is equivalent to enforcing |N(S)| ⩾ |S|+k
for every nonempty subset S ⊂ A such that |S| ⩽ |A|−k; the latter is the more commonly
used condition in Plummer’s work. We also state an immediate corollary of statement (iii).
Corollary 8.4. If G[A,B] is a k-extendable bipartite graph, where k ⩾ 1, then G−a−b is
(k −1)-extendable for each pair a ∈ A and b ∈ B.
We now proceed to discuss a few bounds established by Lou [10], and our conjectures
pertinent to these.
8.1 Lou’s bounds and our conjectures
In the same spirit as in Section 4, with respect to a fixed value of k, for a k-extendable
bipartite graph G, we let V (G) denote the set of vertices that have degree precisely k+1,
k+1
and we let V (G) denote the set of vertices that have degree at least k + 2. We drop G
k+2
from the notation when the graph is clear from the context. For the sake of brevity, we use
E := E(G[V ]) and E := E(G[V ]).
k+1 k+1 k+2 k+2
Note that a minimal 0-extendable bipartite graph is precisely a perfect matching. Thus,
|V | = n and |E| = n. Henceforth, we shall be interested in bounds for k ⩾ 1. Lou [10]
1 2
proved the following.
Theorem 8.5. In a minimal k-extendable bipartite graph G, the induced subgraph G[V ]
k+2
is a forest.
Using the above, Lou [10] deduced the following lower bound on the number of vertices of
degree k +1 in terms of n.
Corollary 8.6. In a minimal k-extendable bipartite graph, |V | ⩾ kn+2.
k+1 2k+1
28

<!-- Page 29 -->

We now use Lou’s Theorem (8.5) to infer another lower bound in terms of m and n.
Corollary 8.7. For k ⩾ 1, in a minimal k-extendable bipartite graph, |V | ⩾ 1(m−n+1).
k+1 k
Proof. Note the (k +1)|V | = |∂(V )|+2|E | ⩾ |∂(V )|+|E |. Furthermore, by
k+1 k+1 k+1 k+1 k+1
Theorem 8.5, |E | ⩽ |V | − 1. Combining these, m = |E | + |E | + |∂(V )| ⩽
k+2 k+2 k+2 k+1 k+1
|V |−1+(k +1)|V | = n−1+k|V |. By rearranging, |V | ⩾ 1(m−n+1).
k+2 k+1 k+1 k+1 k
Using Theorem 8.5, Lou also deduced the following upper bound on the size.
Corollary 8.8. In a minimal k-extendable bipartite graph, |E| ⩽ (k +1)n−1.
It is worth noting that Lou did not provide examples that satisfy any of the aforementioned
bounds tightly. We are also unable to construct such examples. Thus, we conjecture stronger
bounds that are generalizations of the corresponding bounds that appear in Table 1.

### Conjecture 8.9. [Main Conjecture]

In a minimal k-extendable bipartite graph, |V | ⩾ 2 (m−n+2k).
k+1 2k−1
As we shall see soon, one may prove the following two conjectures assuming the above
conjecture.
Conjecture 8.10. In a minimal k-extendable bipartite graph, where k ⩾ 1, |V | ⩾ n +2.
k+1 2
For our final conjecture, we are able to construct small counterexamples, and thus impose
a lower bound on the order. This is reminiscent of Corollary 7.3 wherein C appears as the
4
only counterexample.
Conjecture8.11. ThereexistsanintegerN ⩽ 4k2+2k suchthateveryminimalk-extendable
k
bipartite graph, on N or more vertices, satisfies |E| ⩽ (2k+1)(n−2k).
k 2
Asevidencefortheaboveconjecture,wementionthefollowingresultduetoFabres,Kothari
and Carvalho [4] whose bound coincides exactly with our conjecture.
Theorem 8.12. Every minimal 2-extendable bipartite graph, on twelve or more vertices,
satisfies |E| ⩽ 5n−20.
2
For each of the above three conjectures, we shall provide tight examples that attain the
corresponding bounds, in Subsection 8.3. Our examples may be viewed as straightforward
generalizations of the characterizations of the corresponding extremal classes that appear
in Theorems 1.3, 1.4 and 1.5. Below, we prove that our Main Conjecture (8.9) implies the
other two.
Theorem 8.13. Conjecture 8.9 implies Conjecture 8.10.
Proof. Using the fact that n = |V |+|V |, and the handshaking lemma:
k+1 k+2
(cid:88)
2m = d(v)+(k +1)|V | ⩾ (k +2)|V |+(k +1)|V | = (k +2)n−|V |
k+1 k+2 k+1 k+1
v∈V
k+2
By substituting the above in Conjecture 8.9, we infer that (2k−1)|V | ⩾ 2(m−n+2k) ⩾
k+1
kn−|V |+4k. By rearranging, |V | ⩾ n +2.
k+1 k+1 2
29

<!-- Page 30 -->

Note that Conjecture 8.11 already holds when k = 1 due to Corollary 7.3. Now, we prove
Conjecture 8.11 assuming the Main Conjecture (8.9) for k ⩾ 2.
Theorem 8.14. Conjecture 8.9 implies Conjecture 8.11.
Proof. LetG[A,B]denoteaminimalk-extendablebipartitegraph,wherek ⩾ 2,thatsatisfies
Conjecture 8.9. Using the fact that n = |V | + |V |, we deduce that 2(m − n + 2k) ⩽
k+1 k+2
(2k−1)|V | = (2k−1)(n−|V |). If |V | ⩾ 2k then 2(m−n+2k) ⩽ (2k−1)(n−2k),
k+1 k+2 k+2
and by rearranging, we arrive at the desired conclusion: m ⩽ 2k+1(n − 2k). It remains to
2
deal with the case: |V | < 2k. Before that, we make a few easy observations.
k+2
Note that m = |E |+|∂(V )|+|E | and also |∂(V )| = (k+1)|V |−2|E |. We
k+1 k+1 k+2 k+1 k+1 k+1
deduce that m = (k+1)|V |−|E |+|E |. Now, by Theorem 8.5, |E | ⩽ |V |−1.
k+1 k+1 k+2 k+2 k+2

### Combining these:

m ⩽ (k +1)|V |−|E |+|V |−1 (4)
k+1 k+1 k+2
In what follows, we shall lower bound |E | in order to obtain an upper bound on m. For
k+1
convenience, we use VA to denote the set V ∩A, and likewise for VA and VB .
k+2 k+2 k+1 k+1
Henceforth, we assume that |V | < 2k and adjust notation so that |VA | ⩽ k − 1.
k+2 k+2
Consequently, each vertex in VB has at least two neighbours in VA . As a result, |E | ⩾
k+1 k+1 k+1
2|VB | = 2(n −|VB |) ⩾ 2(n −|V |) = n−2|V |. Combining this with Equation 4, and
k+1 2 k+2 2 k+2 k+2
replacing |V | by n−|V |:
k+1 k+2
m ⩽ (k +1)|V |−n+2|V |+|V |−1 = kn−(k −2)|V |−1
k+1 k+2 k+2 k+2
Since k ⩾ 2, we conclude that m ⩽ kn−1 < kn. Finally, observe that kn ⩽ (2k+1)(n−2k) if
2
and only if n ⩾ 2k(2k +1) = 4k2 +2k; this completes the proof of Theorem 8.14.
We now proceed to establish a result on the connectedness of k-extendable bipartite graphs
that will help us in deducing that the graphs yielded by our constructions, described in
Subsection 8.3, are indeed minimal.
8.2 A result on connectedness of k-extendable bipartite graphs
Asdiscussedearlier, Plummer[15]provedthatk-extendablegraphsare(k +1)-connectedfor
k ⩾ 1; see Theorem 8.1. In this subsection, we prove another interesting property pertaining
to the connectedness of k-extendable bipartite graphs. We first prove the following technical
inequality that surprisingly shows up in our proof of Theorem 8.16.
Lemma 8.15. Let p and q be nonnegative real numbers where p < q, let D := [p,q], and let
f : D2 (cid:55)→ R be the function f(x,y) := y(p+q −x)+x(p+q −y). Then f(x,y) ⩾ 2pq for
each (x,y) ∈ D2.
30

<!-- Page 31 -->

Proof. Let (x,y) ∈ D2. We begin by observing a couple of symmetries: f(y,x) = f(x,y) =
f(p+q −x,p+q −y). Consequently, we may adjust notation so that y ⩽ p+q. Note that
2
f(x ,y)−f(x ,y) = (x −x )(p+q −2y). Thus, f(x,y) ⩾ f(p,y) ⩾ f(p,p) = 2pq.
1 2 1 2
A graph of order four or more is essentially r-edge-connected if each nontrivial cut has size
at least r.
Theorem 8.16. Every k-extendable bipartite graph is essentially 2k-edge-connected.
Proof. Let ∂(W) be a nontrivial cut in a k-extendable bipartite graph G[A,B]; clearly, we
may assume G to be simple. We let W := W ∩A, and define W ,W and W analogously,

## A B A B

and adjust notation so that W is a smallest set among the four. We now consider three

## A

cases based on |W |, and argue that |∂(W)| ⩾ 2k in each case.

## A

First, suppose that W = ∅. By Corollary 8.2, |∂(W)| = (cid:80) d(b) ⩾ (k+1)|W |. Now,
|W | = |W| ⩾ 2 as ∂(W A ) is nontrivial. Thus, |∂(W)| ⩾ 2k + b 2 ∈W ⩾B 2k. B

## B

Next, suppose that |W | ⩾ k; thus, |W | ⩾ k. Consequently, |W | = |A|−|W | ⩽ |A|−k.

## A A A A

Thus, by Theorem 8.3, |N(W )| ⩾ |W |+k. An analogous argument proves that |N(W )| ⩾

## A A B

|W |+k. Combining all of these,

## B

|∂(W)| ⩾ |N(W )−W |+|N(W )−W | ⩾ |N(W )|−|W |+|N(W )|−|W | ⩾ 2k

## A B B A A A B B

In order to deal with the remaining case, we let x := |W | and y := |W |, and make

## A B

some observations. Each vertex in W has at most x edges going to W . Consequently,

## B A

by Corollary 8.2, each vertex in W has at least (k + 1 − x) edges going to W . Thus,

## B A

|∂(W)| ⩾ y(k + 1 − x). Using analogous arguments, |∂(W)| ⩾ x(k + 1 − y). Since these
inequalities are referring to disjoint sets of edges, |∂(W)| ⩾ y(k +1−x)+x(k +1−y).
Finally, suppose that 1 ⩽ x ⩽ k−1. If y ⩾ k, then |∂(W)| ⩾ y(k+1−x) ⩾ 2k. Otherwise
1 ⩽ y ⩽ k −1. Since x,y ∈ [1,k], we invoke Lemma 8.15 to conclude:
|∂(W)| ⩾ y(k +1−x)+x(k +1−y) ⩾ 2k
This completes the proof of Theorem 8.16.
Following the terminology of [4], an edge e in a k-extendable graph G is superfluous if
G − e is also k-extendable. Note that, only for k = 1, superfluous edges are precisely the
removable edges. However, for general k, we prefer to use the term superfluous since the
notion of removability appears in the literature extensively; see Lucchesi and Murty [12].
Thus, to rephrase, a k-extendable graph is minimal if and only if it is free of superfluous
edges. Finally, we record the following easy consequence of Corollary 8.2 and Theorem 8.16.
Corollary 8.17. An edge e of a k-extendable bipartite graph is not superfluous if either of
the following holds:
(i) either an end of e has degree k +1,
(ii) or e belongs to a nontrivial 2k-cut.
31

<!-- Page 32 -->

We shall find the above useful in establishing minimality of the k-extendable bipartite
graphs obtained by our constructions.
8.3 Constructing tight examples for our conjectures
We begin by generalizing Halin trees. A tree is an r-tree if all of its non-leaves have degree
at least r, and it is a regular r-tree if all of its non-leaves have degree exactly r. As per
this, Halin trees are precisely the 3-trees, whereas cubic Halin trees are precisely the regular
3-trees. Next, we generalize the isomorphic leaf matching operation.

### Definition 8.18. [Isomorphic k-leaf Matching]

Let T denote a nontrivial tree, and L its set of leaves. For a positive integer k, let H denote
the (bipartite) graph obtained from the disjoint union of k copies of T, say T ,T ,...T , by
1 2 k
identifying, for each member of L, all of its k copies into a single vertex; we let L(H) := L.
Now, let H′ denote a copy of H. The (bipartite) graph G obtained from H ∪H′ by adding
a matching, each of whose edges joins a member of L(H) with the corresponding member of
L(H′) as per some fixed isomorphism between H and H′, is said to be obtained from T by
isomorphic k-leaf matching; furthermore, we let L(G) := L(H)∪L(H′).
(a) tree T (b) G obtained from T by isomorphic 2-leaf matching
Figure 17: an example of isomorphic k-leaf matching operation
For instance, the graph G shown in Figure 17b is obtained from the tree T shown in
Figure 17a by isomorphic 2-leaf matching; the green coloured vertices represent L(G) and
L(T), respectively. Figures 18 and 19 also depict examples of the isomorphic k-leaf matching
operation. The reader may verify that the isomorphic leaf matching operation defined in
Subsection 1.2 is precisely the isomorphic 1-leaf matching operation. We now invite the
reader to observe the following that will be used later, together with Corollary 8.17, to prove
minimality of our examples.
Proposition 8.19. Let G be a graph obtained from a tree T by isomorphic k-leaf matching
where k ⩾ 1; adopt notation from Definition 8.18. For an edge e of H ∪ H′, let e and e′
i i
denote the copies of e in T and T′, respectively, for each i ∈ {1,2,...,k}. Then, the set
i i
{e ,e ,...,e ,e′,e′,...,e′} is a 2k-cut of G containing the edge e.
1 2 k 1 2 k
32

<!-- Page 33 -->

We will prove a generalization (namely, Proposition 8.24) of Proposition 1.7 in terms of
(k +1)-trees and the isomorphic k-leaf matching operation. In its proof, we induct on the
number of non-leaves of the (k + 1)-tree, say T, to prove that the constructed graphs are
indeed k-extendable. The base case is when the number of non-leaves is at most two. If
T has precisely one non-leaf then T is a star. On the other hand, if T has precisely two
non-leaves, we call it a double star and denote it as D where p and q are the degrees of the
p,q
non-leaves. The induction step of the proof of Proposition 8.24 will be handled by Lemma

### However, before that, we prove a couple of lemmas to address the base case.

We define J , where r ⩾ p ⩾ 1, as the graph obtained from K by isomorphic p-leaf
p,r 1,r
matching; see Figure 18. The graph J , where r ⩾ 0, is defined to be the disjoint union of
0,r
r copies of K . The reader may easily observe that J is matchable for all r ⩾ p ⩾ 0. For
2 p,r
the graph J [A,B] where r ⩾ p ⩾ 1, we adopt notation from Definition 8.18, and we let
p,r
A := L(J )∩A and B := L(J )∩B; on the other hand, for J [A,B], we let A := A
r p,r r p,r 0,r r
and B := B. Note that |A | = |B | = r. We now prove the following stronger property.
r r r
Lemma 8.20. The bipartite graph J [A,B], where r ⩾ k ⩾ 0, is min{k,r−k}-extendable.
k,r
Proof. Let S be a nonempty subset of A. Note that |A−A | = k. Observe that if S contains
r
a vertex from each of A − A and A , then N(S) = B. Otherwise, either S ⊆ A − A or
r r r
S ⊆ A . In the former case, |N(S)| = r ⩾ |S|+r−k and in the latter case, |N(S)| = |S|+k.
r
Thus, by Theorem 8.3, J is min{k,r−k}-extendable.
k,r

## A B

u v

## B A

r r
Figure 18: J obtained from K by isomorphic 3-leaf matching
3,4 1,4
Now, let G be the graph obtained from a double star D , where p,q ⩾ 2, by isomorphic
p,q
k-leaf matching. We provide an alternative viewpoint for constructing G. Let M ,M ,M
1 2 3
and M be the graphs obtained from the disjoint union of p − 1,k,q − 1 and k copies of
4
K , respectively, and let A and B denote fixed color classes of M for each i ∈ {1,2,3,4}.
2 i i i
Now, G may be obtained from M ∪M ∪M ∪M by joining, for each i ∈ {1,2,3,4}, each
1 2 3 4
vertex of A with every vertex of B , where arithmetic is modulo four; see Figure 19. The
i i+1
following lemma addresses the double star base case.
33

<!-- Page 34 -->

Lemma 8.21. For any positive integer k, the bipartite graph G[A,B] obtained from a double
star D , where p,q ⩾ k +1, by isomorphic k-leaf matching is k-extendable.
p,q

## M

4

## M

3

## M

1

## M

2
Figure 19: The graph obtained from D by isomorphic 2-leaf matching
4,5
Proof. We use the alternative viewpoint that was described in the paragraph preceding the
lemma statement, and the notation defined therein. Let A := A ∪A ∪A ∪A , and likewise
1 2 3 4
for B. Let S be any nonempty subset of A. If S meets each A , where i ∈ {1,2,3,4}, then
i
N(S) = B. Otherwise, there exists an i ∈ {1,2,3,4} such that S∩A ̸= ∅ but S∩A = ∅.
i i+1
Now, note that the graph H := G − V(M ) is matchable. As a result, |N (S)| ⩾ |S|.
i+1 H
Furthermore, since S ∩A is nonempty, B ⊆ N(S). Thus, |N (S)| = |N (S)|+|B | ⩾
i i+1 G H i+1
|S|+k. Consequently, by Theorem 8.3, G is k-extendable.
Before proving Lemma 8.23, we state and prove an easy consequence of Theorem 8.3.
Corollary 8.22. If G[A,B] is a k-extendable bipartite graph, where k ⩾ 1, then G−e−e′ is
(k −1)-extendable for any two nonadjacent edges e and e′ such that an end of e is adjacent
with an end of e′.
Proof. Let e := ab and e′ := a′b′, where a,a′ ∈ A and b,b′ ∈ B, so that ab′ ∈ E(G). We let
H := G−e−e′. For any S ⊆ A, observe that |N (S)| ⩾ |N (S)|−2 and equality holds

## H G

only if a,a′ ∈ S and b,b′ ∈/ N (S). However, since ab′ ∈ E(H), equality does not hold and

## H

|N (S)| ⩾ |N (S)|−1. We intend to show that H satisfies statement (ii) of Theorem 8.3

## H G

with k −1 playing the role of k.
Now, by applying Theorem 8.3 to G, either |N (S)| ⩾ |S|+k or N (S) = B. If |N (S)| ⩾

## G G G

|S|+k then |N (S)| ⩾ |S|+k −1, and we are done. Now, suppose that N (S) = B and

## H G

|N (S)| ⩽ |S|+k −1; these imply that |S| ⩾ |A|−k +1. Since d (b) = d (b)−1 ⩾ k, we

## G H G

infer that b ∈ N (S); likewise, b′ ∈ N (S). Consequently, N (S) = N (S) = B. Thus, by

## H H H G

Theorem 8.3, H is (k −1)-extendable.
Next, we describe an operation that appears in the induction step of the proof of Proposition 8.24. Let G be a simple bipartite graph and uv be an edge such that d(u) = d(v) = p+1.
Recall the definition of J that appears in the paragraph preceding Lemma 8.20, and the
p,r
notation therein; let A := A − A and B := B − B . Now, the (bipartite) graph G′ —
u r v r
34

<!-- Page 35 -->

constructed from the disjoint union of H := G−u−v and J by adding two matchings, each
p,r
of size p, one between N (u)−v and A , and another between N (v)−u and B — is said

### G u G v

to be obtained from G by replacing the edge uv with J . See Figure 20 for an illustration.
p,r
We now show that this operation preserves k-extendability.
Lemma 8.23. The bipartite graph G′ obtained from a k-extendable bipartite graph G by
replacing an edge uv, where d(u) = d(v) = p+1, with J is also k-extendable.
p,r
Proof. We adopt notation from the paragraph preceding the lemma statement, and we let
y ,u ,v and x , for each i ∈ {1,2,...,p}, denote the vertices in the sets N (u)−v,A ,B
i i i i G u v
and N (v)−u, respectively. We let a and b , for each i ∈ {1,2,...,r}, denote the vertices

### G i i

in A and B , respectively; see Figure 20. We proceed by induction on k; the following
r r
observation proves the statement for k = 0, and will also come in handy later.

#### For each perfect matching M of G, the restriction of M to G−u−v extends to a

perfect matching of G′.
Proof. First, suppose that uv ∈ M. Then, let M′ be any perfect matching of J ; see
p,r
Lemma 8.20. Then, M −uv +M′ is the desired perfect matching of G′.
Otherwise, p ⩾ 1. Adjust notation so that uy ,vx ∈ M. Now, let M′ be any perfect
1 1
matching of J −u −v ∼ = J ; see Lemma 8.20. Then, M−uy −vx +M′+u y +v x
p,r 1 1 p−1,r 1 1 1 1 1 1
is the desired perfect matching of G′.
We use J to denote the subgraph of G′ induced by the vertices of J . For disjoint sets
p,r
of vertices of G′, say X and Y, we let ∂(X,Y) denote the set of those edges whose one
end is in X and the other end is in Y. We let M ,M and M denote the matchings
u r v
∂(N (u)−v,A ),∂(A ,B ) and ∂(B ,N (v)−u), respectively, and adjust notation so that

### G u r r v G

both ends of each edge in M ∪M ∪M have the same subscript.
u r v
Now, let k ⩾ 1 and M be a matching of size k in G′. We consider two cases depending
on whether M is a subset of E(G′ −J) or not. In each case, we argue that M extends to a
perfect matching of G′.
Firstly, suppose that M ⊆ E(G′−J). As G is k-extendable, there is a perfect matching M′
of G containing M. Note that the restriction of M′ to G−u−v also contains M; by 8.23.1,
this extends to a perfect matching of G′, and we are done.
Secondly, suppose that M ̸⊆ E(G′ − J). In other words, M contains at least one edge,
say e, from E(J)∪∂(J). Observe that (M ,M ,M ,∂(A ,B ),∂(B ,A )) is a partition of
u v r u r v r
E(J) ∪ ∂(J). We now consider two subcases depending on whether e ∈ M ∪ M ∪ M or
u r v
not.
First, suppose that e ∈ M ∪M ∪M . Note that r ⩾ p ⩾ k; consequently, M ,M and M
u r v u r v
are disjoint induced matchings of size at least k. Using this fact, we choose one edge from
each of these sets as follows. For each F ∈ {M ,M ,M }, we pick e if e ∈ F; otherwise, we
u r v
pick any edge e′ whose both ends are M-exposed; let u y ,v x and a b denote these three
i i j j ℓ ℓ
edges. By Corollary 8.4, the graph H := G − y − x is (k −1)-extendable. Also, observe
i j
35

<!-- Page 36 -->

that the graph H′ := G′−u −y −v −x −a −b is obtained from H by replacing uv by
i i j j ℓ ℓ
J . Thus, by the induction hypothesis, H′ is (k −1)-extendable. Consequently, there
p−1,r−1
is a perfect matching M′ of H′ containing M −e. Thus, M′+u y +v x +a b is a perfect
i i j j ℓ ℓ
matching of G′ containing M.

## M

r

## M M

u b a 1 v
1
y u v x
1 1 1 1
a
b 2
2
y u v x
2 2 2 2
y 1 x 1 b a 3
3
y u v x
3 3 3 3
y 2 u v x 2 b a 4
4
N (u)−v A B N (v)−u
G u v G
y x B A
3 3 r r
(a) G (b) G′
Figure 20: an illustration of replacing uv by J
3,4
Now, suppose that e ∈/ M ∪ M ∪ M ; consequently, e ∈ ∂(A ,B ) ∪ ∂(B ,A ). Adjust
u r v u r v r
notation so that e := u b . If a is matched in M then let v ∈ B denote its matched
i j j ℓ v
neighbour; otherwise, since p ⩾ k, let v denote any unmatched vertex in B ; we shall define
ℓ v
a perfect matching M′′ of G′ that contains M in both cases. By Corollary 8.22, the graph
H := G−uy −vx is (k −1)-extendable. Also, observe that H′ := G′ −u −b −a −v
i ℓ i j j ℓ
is obtained from H by replacing uv by J . Thus, by the induction hypothesis, H′ is
p−1,r−1
(k −1)-extendable. Consequently, M − e − a v extends to a perfect matching M′ of H′.
j ℓ
Observe that M′′ := M′ +u b +a v is the desired perfect matching of G′.
i j j ℓ
This completes the proof of Lemma 8.23.
We are now ready to prove the following generalization of Proposition 1.7.
Proposition 8.24. For a positive integer k, any graph G — obtained from a (k+1)-tree T,
that is neither K nor a star K where p < 2k, by isomorphic k-leaf matching — is a
2 1,p
minimal k-extendable bipartite graph.
Proof. We will induct on the number of non-leaves of T. Firstly, if T has exactly one nonleaf, then it is a star and we are done by Lemma 8.20 as p−k ⩾ k. Secondly, if T has exactly
two non-leaves, then it is a double star with p,q ⩾ k +1 and we are done by Lemma 8.21.
Now, suppose that T has at least three non-leaves. Let u be a leaf of the tree obtained
from T by deleting all of its leaves. Observe that, in T, each neighbour of u, except one, is
a leaf. Let T′ be the tree obtained from T by deleting those leaves that are neighbours of u.
Let us relate the leaves and non-leaves of T and T′ with each other.
36

<!-- Page 37 -->

Note that u is a leaf in T′. Furthermore, for each vertex w ∈ V(T′)−u, we have N (w) =

## T′

N (w). Thus, the non-leaves of T′ are precisely the non-leaves of T minus u. Also, each leaf

## T

of T′, except u, is a leaf of T. Ergo, T′ is also a (k+1)-tree with precisely one non-leaf fewer
than T; in particular, T′ has at least two non-leaves. Hence, by the induction hypothesis,
the graph G′ obtained from T′ by isomorphic k-leaf matching is k-extendable.
As u is a leaf in T′, let u and v be the two vertices corresponding to u in G′. Now, observe
that G may be obtained from G′ by replacing the edge uv by J , where r := d (u)−1 ⩾ k.
k,r T
Since G′ is k-extendable, by Lemma 8.23, G is also k-extendable.
Next, we prove minimality of G. By Corollary 8.17 (i), we only need to inspect those
edges of G each of whose ends has degree at least k + 2; let e denote such an edge. We
adopt notation from Definition 8.18, and observe that e ∈ H ∪ H′. By Proposition 8.19,
the set of edges {e ,e ,...,e ,e′,e′,...,e′} is a 2k-cut (of G) that contains e. Thus, by
1 2 k 1 2 k
Corollary 8.17 (ii), e is not superfluous. We thus infer that G is minimal.
Finally, we provide our constructions of the promised tight examples, and use the above
proposition to validate them. The reader may compare the statement to Theorem 1.8.
Theorem 8.25. For a positive integer k, any graph G obtained from a (k +2)-tree T, that
is neither K nor a star K where p < 2k, by isomorphic k-leaf matching is a minimal
2 1,p
k-extendable bipartite graph that satisfies the bound in Conjecture 8.9 with equality. Furthermore:
(i) if T is a regular (k+2)-tree then G satisfies the bound in Conjecture 8.10 with equality,
whereas
(ii) if T is a star then G satisfies the bound in Conjecture 8.11 with equality.
Proof. ByProposition8.24, Gisaminimalk-extendablebipartitegraph. Weadoptallofthe
notation present in Definition 8.18. We first argue that G satisfies the bound in Conjecture
8.9 with equality.
Since T is a (k + 2)-tree, V (G) = L(G). Note that |E | = 1|L(G)| = 1|V | and
k+1 k+1 2 2 k+1
|∂(V )| = k|V |. Consequently, |E | = m−|E |−|∂(V )| = m− 2k+1|V |.
k+1 k+1 k+2 k+1 k+1 2 k+1
On the other hand, observe that G[V ] = G−V is a forest with 2k components. So,
k+2 k+1
|E | = |V |−2k = n−|V |−2k.
k+2 k+2 k+1
It follows from the preceding two paragraphs that m− 2k+1|V | = n−|V |−2k. By
2 k+1 k+1
rearranging, 2k−1|V | = m − n + 2k which is precisely the bound in Conjecture 8.9. It
2 k+1
remains to prove statements (i) and (ii).
(cid:80)
First,supposethatT isaregular(k+2)-tree. Bydoublecounting, d(v) = 2|E |+
v∈V k+2
k+2
|∂(V )|. As noted earlier, |E | = |V |−2k and |∂(V )| = k|V |. By substituting,
k+2 k+2 k+2 k+2 k+1
(k+2)|V | = 2(|V |−2k)+k|V |. By rearranging and dividing by k, |V | = |V |−4.
k+2 k+2 k+1 k+2 k+1
Now, by plugging |V | = n−|V | and rearranging, |V | = n +2 which is precisely the
k+2 k+1 k+1 2
bound in Conjecture 8.10.
37

<!-- Page 38 -->

Finally, suppose that T is a star K , where p ⩾ 2k. Note that n = 2p + 2k. Observe
1,p
that m = (2k + 1)p = (2k+1)(n−2k) which is precisely the bound in Conjecture 8.11. This
2
completes the proof of Theorem 8.25.
We are unable to construct any examples, apart from the ones described in the above
theorem statement, that satisfy the bounds in Conjectures 8.9, 8.10 or 8.11 with equality,
and are thus tempted to further conjecture that these are the only such examples.

### References

[1] J. A. Bondy and U. S. R. Murty. Graph Theory. Springer, 2008.
[2] M. H. Carvalho, C. L. Lucchesi, and U. S. R. Murty. Graphs with independent perfect
matchings. J. Graph Theory, 48:19–50, 2005.
[3] G. A. Dirac. Minimally 2-connected graphs. 1967.
[4] P. A. Fabres, N. Kothari, and M. H. Carvalho. Minimal braces. Journal of Graph
Theory, 96(4):490–509, 2021.
[5] R. Halin. Studies on minimally n-connected graphs. In Combinatorial Mathematics and
its Applications (Proc. Conf., Oxford, 1969), pages 129–136, 1971.
[6] G. Hetyei. Rectangular configurations which can be covered by 2× 1 rectangles. P´ecsi
Tan. Foisk. K¨ozl, 8:351–367, 1964.
[7] A. Hoffmann-Ostenhof, K. Noguchi, and K. Ozeki. On homeomorphically irreducible
spanning trees in cubic graphs. Journal of Graph Theory, 89(2):93–100, 2018.
[8] D. V. Karpov. Minimal k-connected graphs with minimal number of vertices of degree
k. Journal of Mathematical Sciences, 212:666–682, 2016.
[9] C. H. C. Little. A theorem on connected graphs in which every edge belongs to a
1-factor. Journal of the Australian Mathematical Society, 18(4):450–452, 1974.
[10] D. Lou. On the structure of minimally n-extendable bipartite graphs. Discrete Mathematics, 202(1):173–181, 1999.
[11] L. Lova´sz and M. D. Plummer. Matching Theory. Number 29 in Annals of Discrete
Mathematics. Elsevier Science, 1986.
[12] C. L. Lucchesi and U. S. R. Murty. Perfect Matchings: A Theory of Matching Covered
Graphs. Algorithms and Computation in Mathematics. Springer Nature Switzerland,
Imprint: Springer, 2024.
[13] J. G. Oxley. On some extremal connectivity results for graphs and matroids. Discrete
Mathematics, 41(2):181–198, 1982.
[14] M. D. Plummer. On n-extendable graphs. Discrete Mathematics, 31(2):201–210, 1980.
[15] M. D. Plummer. Matching extension in bipartite graphs. Technical report, 1986.
38

<!-- Page 39 -->

[16] H. Whitney. 2-isomorphic graphs. American Journal of Mathematics, 57:245–254, 1933.
39

## Tables

**Table (Page 3):**

| Class | Property | Notation |
|---|---|---|
| 2-edge extremal | \|E \| = m−n+2 2 | H 0 |
| 2-edge n-extremal | \|E \| = n+10 2 6 | H 1 |
| 2-vertex extremal | \|V \| = 2(m−n+2) 2 | H 2 |
| 2-vertex n-extremal | \|V \| = n +2 2 2 | H 3 |
| edge extremal | \|E\| = 3n−6 2 | H 4 |


**Table (Page 21):**

| T a 1 1 |  |  |  |  |  | v 1 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
| T′ b 1 1 |  |  |  |  |  | u 1 |


**Table (Page 21):**

| u 2 |  | b T 2 2 |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
| v 2 |  | a T′ 2 2 |  |  |


**Table (Page 21):**

| T a 1 |  |  |  |  |  |  | b 2 |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
| T′ b 1 |  |  |  |  |  |  | a 2 |  |  |
|  |  |  |  |  |  |  |  |  |  |


**Table (Page 33):**

|  |  |
|---|---|
|  |  |
|  |  |


**Table (Page 36):**

|  |  |
|---|---|
|  | u |
|  | u |


**Table (Page 36):**

|  | a |
|---|---|
|  | a |
|  | a |


**Table (Page 36):**

|  |
|---|
|  |
