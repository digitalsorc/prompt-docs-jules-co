---
title: "A B Testing LLM Deployments"
original_file: "./A_B_Testing_LLM_Deployments.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "evaluation"]
keywords: ["cid", "proc", "quantum", "call", "procedure", "page", "program", "circuit", "controlled", "statement"]
summary: "<!-- Page 1 -->

Branch Sequentialization in Quantum Polytime

### Emmanuel Hainry Romain Péchoux Mário Silva

Université de Lorraine, CNRS, Inria, LORIA, F-54000 Nancy, France

### October 8, 2025

{hainry,pechoux,mmachado}@loria.fr

### Abstract

Quantum algorithms leverage the use of quantumly-controlled data in order to achieve computationaladvantage. Thisimpliesthattheprogramsuseconstructsdependingonquantumdata
and not just classical data such as measurement outcomes. Current compilation st"
related_documents: []
---

# A B Testing LLM Deployments

<!-- Page 1 -->

Branch Sequentialization in Quantum Polytime

### Emmanuel Hainry Romain Péchoux Mário Silva

Université de Lorraine, CNRS, Inria, LORIA, F-54000 Nancy, France

### October 8, 2025

{hainry,pechoux,mmachado}@loria.fr

### Abstract

Quantum algorithms leverage the use of quantumly-controlled data in order to achieve computationaladvantage. Thisimpliesthattheprogramsuseconstructsdependingonquantumdata
and not just classical data such as measurement outcomes. Current compilation strategies for
quantum control flow involve compiling the branches of a quantum conditional, either in-depth
or in-width, which in general leads to circuits of exponential size. This problem is coined as the
branch sequentialization problem. We introduce and study a compilation technique for avoiding
branchsequentializationonalanguagethatissoundandcompleteforquantumpolynomialtime,
thus, improving on existing polynomial-size-preserving compilation techniques.
1 Introduction
1.1 Motivation
Quantum computing is an emerging paradigm of computation, where quantum physical phenomena
such as entanglement and superposition are used to obtain an advantage over classical computation.
A testament to the richness of the field is the variety of computational models: quantum Turing
machines [6], quantum circuits [31, 26], measurement-based quantum computation [7, 12], linear
optical circuits [21], among others.
In recent decades, a lot of effort has been put into developing high-level quantum programming
languages that allow programmers to abstract away from the technicalities of these low-level models [27, 3]. Toward that end, several verification techniques such as type systems [15] or categorical
approaches for reasoning about program semantics [4, 19] have been studied and developed to ensure
the physical reality of compiled programs, for example, by ensuring that they satisfy the properties
of quantum mechanics such as the no-cloning theorem [1] and unitarity [14].
An important line of research in this area involves checking polytime termination of quantum
programs [11, 29, 17], by showing that any program can be simulated by a polytime quantum Turing
machine(QTM).AsaconsequenceofYao’sTheorem[31],demonstratingthatpolynomial-timeQTMs
are computationally equivalent to uniform and poly-sized quantum circuit families, such programs
canbeinstantiatedbyauniformfamilyofquantumcircuitsofpolynomialsize,i.e.,withapolynomial
numberofqubitsandgates. However,directcompilationtechniquesoftenfailtoensurethisproperty,
due to the use of quantum branching, where the flow in a conditional is determined by the state of a
qubit.
As an illustrative example, consider a quantum case, of the shape
qcase q 1 ,...,q k of {i→S i } i∈{0,1}k ,
which executes the superposition of the unitary transformations U implemented by statements S ,
i i
depending on the state ∣i⟩ of the control qubits q ,...,q . This statement can be simulated by a
1 k
QTM that, depending on k symbols in its tape, performs the instructions of different QTMs M
i
in superposition. Consequently, its runtime is the maximum runtime among all M ([6, Branching
i
Lemma]). Instantiating this qcase statement on quantum circuits can be done sequentially (indepth) or in parallel (in-width). An in-depth encoding consists in applying each controlled-U gate
i
sequentially, thus implementing the unitary transformation ∑
i∈{0,1}k
∣i⟩⟨i∣⊗U
i
. The depth of the
1
5202
tcO
7
]OL.sc[
3v35190.2142:viXra

<!-- Page 2 -->

resulting circuit is the sum of the depths of all U , which is exponential in the number k of control
i
qubits. An alternative strategy, inspired by QRAM, allows for the execution of each U in parallel in
i
thecircuit,usingcontrolledswapstoperformroutingofqubitaddressesinlineardepthonthenumber
of control qubits. Since in this case the unitaries are parallelized, the circuit depth is the maximum
among the depths of U , but this strategy results in circuits where the width scales as the sum of
i
the complexities of U . Consequently, this parallelization requires a number of ancillas that grows
i
exponentially on the number of control qubits. In summary, any implementation, that is agnostic
about the structure of each U , should incur such an exponential cost, as each qcase corresponds to
i
the preparation of an arbitrary quantum state [34, 16].
Automatic implementations of quantum conditionals therefore produce circuits with a size that
scales with the sum (rather than the maximum) of the complexity of each branch. This problem,
coined branch sequentialization in [32], leads, in many cases, to an exponential blow-up in circuit
complexity, forcing the programmer to rewrite and optimize their code in order to make use of
the program structure and improve the complexity bound. A challenging issue is, therefore, to
developquantumprogramminglanguagesthatavoidbranchsequentializationbyensuringthecorrect
circuit complexity for quantum control statements while providing full use of quantum control to the
programmer [32, 33].
1.2 Contribution
Thispapersolvestheaboveissuebyintroducingaprogramminglanguage,calledpbpforPolynomially
BranchingProgram,withquantumcaseandfirst-orderrecursiveprocedures,onwhichcompilationof
quantum conditional does not lead to an exponential blow-up in circuit size. Our main contributions
are as follows:
• Weintroduceacompilationstrategycompile(Figures7and8)intoquantumcircuits,showits
soundness (Theorem 1), and show that it avoids branch sequentialization on pbp (Theorem 2),
a language with restrictions on recursive calls to procedures. Toward that end, we formally
define the time complexity Time ∶ N → N of a program P (Definition 1) as a map from the

## P

number n of qubits to the maximal number of procedures called during a program execution
on the Hilbert space C2n. The time complexity of a qcase statement is precisely the maximum
of the time complexity of its branches and we show that branch sequentialization is avoided as
the circuits generated by compile have size bounded asymptotically by the time complexity of
the compiled program (Theorem 2).
• A natural question concerns the expressive power of language pbp. We also solve this issue
by showing that pbp is sound and complete for quantum polynomial time (Theorem 3). Consequently, any polytime quantum algorithm can be encoded by a pbp program. We illustrate
the methodology through well-known examples such as the program QFT realizing the quantum
Fourier transform (Example 5).
• Wealsodiscussasymptoticboundsforastrictextensionofpbp,wherethereductionintheinput
sortedsetpassedtoprocedurecallscanbearbitrary. Weshowthatthisextensiononlyincreases
the circuit complexity of the no-branch-sequentialization case by a linear factor (Theorem 4).
• We also show that compile strictly improves on existing compilation strategies on first-order
quantum programs with quantum case [17] by a polynomial speedup of arbitrarily large degree
(Table 1).
1.3 A bird’s-eye view of our compilation strategy
We will now consider a simple illustrating example where branch sequentialization can exponentially
worsen the size complexity of the compiled circuit, and show how our compilation strategy can
preserve a polynomial bound.
The program PAIRS defined in Figure 1 consists in a simple call to procedure pairs (line 10) on
a list q¯ of unique qubits. Let ∣q¯∣ be the number of qubits in q¯. By language design, the procedure
pairs immediately terminates whenever ∣q¯∣=0. The procedure enters a quantum case (line 3) when
∣q¯∣≥2,otherwiseitappliesaNOTgatetothesinglequbit(line9). Online3,theprogramwillbranch
depending on the state q¯[1,2] of the first two qubits in q¯. Out of all four cases (lines 4-7), pairs only
2

<!-- Page 3 -->

(a)in-depth q¯ pairs(q¯) (c)merging
(b)in-width
q¯[1] q¯[1] q¯[1]
q¯[2] q¯[2] q¯[2]
q¯⊖[1,2]
q¯⊖[1,2] pairs(q¯⊖[1,2]) pairs(q¯⊖[1,2]) ∣0⟩ ∣0⟩
r00 pairs(q¯⊖[1,2]) q¯⊖[1,2] pairs(q¯⊖[1,2])
∣0⟩
r11 pairs(q¯⊖[1,2])
Figure 2: Compilation strategies.
performs an operation when the first two qubits are in state ∣00⟩ or ∣11⟩, in which case it performs a
recursive call on q¯⊖[1,2], the list obtained by removing the first and second qubits of q¯.

### Given an input state ∣xy⟩, with x ∈ {0,1}∗ and

y ∈ {0,1}, pairs will apply a NOT gate to the last 1 decl pairs(q¯){
( q 0 u 0 bi ∣ t 1 y 1) i ∗ f . an S d in o c n e ly pa i i f r x s i p s e a rfo st r r m in s g a i t n m th o e st la o n n g e u c a a g l e l 2 if ∣q¯∣≥2 then
per branch, and consumes 2 qubits from its input 3 qcase q¯[1,2] of {
whiledoingso,itstimecomplexityisinO(∣q¯∣),when
4
00→call pairs(q¯⊖[1,2]);
takingtheqcasecomplexityasthemaximumofeach
5
01→skip;
branch.
Wenowdiscussthecircuitcompilationof pairs, 6
10→skip;
when ∣q¯∣ ≥ 2. In Figure 2, we give three strate- 7
11→call pairs(q¯⊖[1,2]);
gies (a), (b), and (c), exemplifying different ap-
8
}
proaches. Strategies(a)and(b)areautomaticcom- 9 else q¯[1] ∗= NOT;}
pilation strategies, which ignore the inner structure
of the program – the fact that the body of the two 10 ∶∶ call pairs(q¯);
non-skip branches of the qcase are identical and Figure 1: Program PAIRS.
therefore encode the same unitary transformation.
Figure 2(a) represents an in-depth strategy, whereas Figure 2(b) implements an in-width strategy,
making use of different registers r and r , both initialized to ∣0 ∣q¯∣−2⟩ to perform each branch in
00 11
parallel and then recombine the results in the same register. These two implementations require two
recursive calls to pairs and, consequently, their size complexity is the sum of the complexities of the
two branches. These two strategies are performing branch sequentialization and, in both cases, the
compiled circuit has size exponential in ∣q¯∣. In contrast, Figure 2(c) avoids this exponential blow-up,
makinguseofthefactthatthetwobranchesareidentical. Thisstrategyisabletomerge therecursive
callsintoasingleprocedurecallwiththeuseofoneancilla. Thisispreciselythetypeofstrategyused
by our compilation algorithm compile (Section 3). Although this example is relatively simple due
tosimilar recursivecalls, compile allows todealwith moreinvolvedsituations, bymerging recursive
calls on different parameters.
1.4 Related work
Resource optimization in low-level models of quantum computation is a well-studied subject. Given
a specific quantum circuit, it is possible to reduce its number of gates (or at least its number of non-
Cliffordgates)viatechniquessuchasgatesubstitutionandgraphrewriting[25,23,20,13]. Thestudy
of resource optimization in the asymptotic scenario is a relatively young research area as it involves
reasoning about families of circuits and program structure. Different implicit characterizations of
quantum complexity classes have been developed using a lambda-calculus [11], function algebras [29,
30] and a first-order programming language [17]. The last of these provided a compilation strategy
into quantum circuits with bounds on the circuit size based on the syntactic restrictions placed on
the programs.
Compilation strategies for the quantum control statement (also called quantum switch case or
quantummultiplexer)havebeenstudied,forinstance,instatepreparation[22],appearinginquantum
machine learning [18] and Hamiltonian simulation [8]. These techniques either focus on optimizing
number of qubits (circuit width) [34] or circuit depth [28], but in all cases correspond to circuits of
exponential size. In order to improve on these bounds, one must restrict the set of programs to those
3

<!-- Page 4 -->

thatadmitanefficientimplementation,whichcanbededucedfromtheprogramstructure. Optimized
compilation techniques in that scenario can then be judged on expressivity and completeness: how
easily can one write a program while ensuring the syntactical restrictions? Do these restrictions
encompass all efficient programs? The field of implicit computational complexity is particularly wellsuited to answer these questions [9, 10].
2 First-Order Programming Language with Quantum Case
In this section, we introduce a programming language with quantum control and first-order recursive procedures. After introducing its syntax and semantics, we introduce a restriction pbp (for
Polynomially Branching Programs) on which branch sequentialization can be avoided.
(Integers) i,j,k ∶∶= x ∣ n ∣ i±n ∣ ∣s∣
(Booleans) b ∶∶= i≥i ∣ ⋯ ∣ b∧b ∣ ⋯
(Qubits) q ∶∶= s[i]
(Sorted sets) s ∶∶= q¯ ∣ s⊖[i]
(Statements) S ∶∶= skip; ∣ q ∗= Uf(j); ∣ S S ∣ if b then S else S
∣ qcase q of {0→S,1→S} ∣ call proc(s);
(Procedure declarations) D ∶∶= ε ∣ decl proc(q¯){S},D
(Programs) P(q¯) ∶∶= D∶∶S
Figure 3: Syntax of programs.
2.1 Syntax of Programs
The language includes four basic datatypes for expressions, whose corresponding expressions are
described in Figure 3. (i) Integers: Integer expressions are variables x, constant n ∈ N, an addition
by a constants i±n, or the size ∣s∣ of a sorted set s. (ii) Booleans: Such expressions b are defined
in a standard way. (iii) Qubit: qubits expressions are of the shape s[i] which denotes the i-th qubit
in sorted set s. (iv) Sorted sets: lists of unique (i.e., non-duplicable) qubit pointers. Sorted-set
expressionssareeithervariablesq¯ ors⊖[i],thesortedsetswherethei-thelementhasbeenremoved.
Let s[i1,...,in ] be a shorthand for s[i1 ],...,s[in ]. We also define syntactic sugar for pointing to the
n-th last qubit in a sorted set, by defining for any n≥1, q¯[−n]≜q¯[∣q¯∣−n+1].
A program P≜D∶∶S is defined in Figure 3 as a list of (possibly recursive) procedure declarations
D, followed by a program statement S.
Let Procedures be an enumerable set of procedure names. We write proc ∈ P to denote that
proc appears in P. Each procedure of name proc∈P is defined by a (unique) procedure declaration
decl proc(q¯){S} ∈ D, which takes a sorted set q¯ as input parameter and executes the procedure
statement S. We sometimes write Sproc to explicitly refer to the procedure statement S of proc.
Statements include the no-op instruction, unitary application, sequences, conditional, quantum
case,andprocedurescalls. Forthesakeofuniversality[5],inaunitaryapplicationq ∗= Uf(j);,Uf(j)
is a unitary transformation that can take an integer j and a polynomial-time approximable [2] total
functionf ∈Z→[0,2π)asoptionalarguments. Thef andicanbeomittedwhentheyarenotuseful,
as in a NOT gate.
Thequantumconditionalqcase s[i] of {0→S
0

## ,1→S

1
}allowsbranchingbyexecutingstatements
S and S in superposition according to the state of qubit s[i]. The procedure call call proc(s); runs
0 1
procedure proc with sorted set expression s. The quantum conditional can be extended to multiple
qubits in a standard way as used in Figure 1.
Wealsomakeuseofsomesyntacticsugartodescribestatementsencodingconstant-timequantum
operations. For instance, the CNOT, SWAP, as well as a controlled-phase shift gate are defined by:
CNOT(q ,q ) ≜ qcase q of {0→skip;,1→q ∗= NOT;}
1 2 1 2
SWAP(q ,q ) ≜ CNOT(q ,q ) CNOT(q ,q ) CNOT(q ,q )
1 2 1 2 2 1 1 2
CPHASE(q ,q ,i)≜ qcase q of {0→skip;,1→q ∗= Phλx.π/2x−1(i);}
1 2 1 2
4

<!-- Page 5 -->

(q,l)⇓ Nn∉A
(skip;,∣ψ⟩,A,l)—0→(⊺,∣ψ⟩,A,l) (q∗=Uf(j);,∣ψ⟩,A,l)—0→((cid:150),∣ψ⟩,A,l)
(q,l)⇓ Nn∈A (j,l)⇓ Zk
(q∗=Uf(j);,∣ψ⟩,A,l)—0→(⊺,I 2n−1 ⊗ U (f)(k)⊗I 2l(∣ψ⟩)−n ∣ψ⟩,A,l)
(S1,∣ψ⟩,A,l)—m→1 (⊺,∣ψ′⟩,A,l) (S2(cid:74) ,∣ψ
(cid:75)
′⟩,A,l)—m→2 (◇,∣ψ′′⟩,A,l)
(S1 S2,∣ψ⟩,A,l)m—1 +→m2(◇,∣ψ′′⟩,A,l)
(S1,∣ψ⟩,A,l)—m→((cid:150),∣ψ⟩,A,l) (b,l)⇓ Bb (Sb,∣ψ⟩,A,l)—m→b (◇,∣ψ′⟩,A,l) ◇∈{⊺,(cid:150)}
(S1 S2,∣ψ⟩,A,l)—m→((cid:150),∣ψ⟩,A,l) (if b then Strue else Sfalse,∣ψ⟩,A,l)—m→b (◇,∣ψ′⟩,A,l)
(q,l)⇓ Nn∈A ∀k∈{0,1}, (Sk,∣ψ⟩,A/{n},l)—m→k (⊺,∣ψk ⟩,A/{n},l)
(qcase q of {0→S0,1→S1 },∣ψ⟩,A,l)maxk—∈{→0,1}mk(⊺,∑
k
∣k⟩
n
⟨k∣
n
∣ψk ⟩,A,l)
(q,l)⇓ Nn∈A ∀k∈{0,1}, (Sk,∣ψ⟩,A/{n},l)—m→k (◇ k,∣ψk ⟩,A/{n},l) (cid:150)∈{◇ 0,◇
1
}
(qcase q of {0→S0,1→S1 },∣ψ⟩,A,l)maxk—∈{→0,1}mk((cid:150),∣ψ⟩,A,l)
(q,l)⇓ Nn∉A (s,l)⇓

## L(N)

[]
(qcase q of {0→S0,1→S1 },∣ψ⟩,A,l)—0→((cid:150),∣ψ⟩,A,l) (call proc(s);,∣ψ⟩,A,l)—1→(⊺,∣ψ⟩,A,l)
(s,l)⇓ L(N)l′≠[] (Sproc,∣ψ⟩,A,l′)—m→(◇,∣ψ′⟩,A,l′) ◇∈{⊺,(cid:150)}
(call proc(s);,∣ψ⟩,A,l)m—→+1(◇,∣ψ′⟩,A,l)
Figure 4: Semantics of statements.
Given a program P ≜ D ∶∶ S, the call relation → ⊆ Procedures×Procedures is defined for any

## P

two procedures proc
1
, proc
2
∈ P as proc
1
→

## P

proc
2
whenever proc
2
∈ Sproc1 . The relation ⪰

## P

is
then the transitive closure of → , and ∼ denotes the equivalence relation where proc ∼ proc if

## P P 1 P 2

proc ⪰ proc andproc ⪰ proc bothhold. Aprocedureprocisrecursive wheneverproc∼ proc

## 1 P 2 2 P 1 P

holds. The strict order ≻ is defined as proc ≻ proc if proc ⪰ proc and proc ∼/ proc both
P 1 P 2 1 P 2 1 P 2
hold.
2.2 Semantics of Programs
Let B denote the set of Booleans and L(N) denote the set of lists of natural numbers, [] being the
empty list. We interpret each basic type as follows:

### Integers ≜Z Booleans ≜B Qubits ≜N Sorted Sets ≜L(N)

Qubits are interpreted as integers (pointers) and sorted sets are interpreted as lists of pointers. For
(cid:74) (cid:75) (cid:74) (cid:75) (cid:74) (cid:75) (cid:74) (cid:75)
each basic type τ, the semantics of expressions is described standardly as a function
⇓ ∈τ ×L(N)→ τ
τ
(cid:74) (cid:75)
(e,l) ⇓ v holds when expression e of type τ evaluates to the value v ∈ τ under the context
τ (cid:74) (cid:75)
l ∈ L(N).(cid:74)l(cid:75)is simply the sorted set of qubit pointers into consideration when evaluating e. For
instance, we have that (q¯[2],[1,4,5]) ⇓ N 4 (the second qubit has index 4), (q¯ (cid:74) ⊖ (cid:75)[4],[1,4,5]) ⇓ L(N) []
([] is used for errors on type L(N)), (q¯[4],[1,4,5]) ⇓ N 0 (index 0 encodes error on type N), and
(q¯⊖[3],[1,4,5])⇓

## L(N)

[1,4] (the third qubit has been removed).
Let H denote the Hilbert space of n qubits C2n, P(N) denote the powerset of N.
2n
A configuration c over n qubits is of the shape (S,∣ψ⟩,A,l), for some statement S∈Statements∪
{⊺,(cid:150)}), ⊺ and (cid:150) being two special symbols denoting termination and error, respectively, ∣ψ⟩ is a
quantum state in H , where A ∈ P(N) is the set of accessible qubit pointers, and where l ∈ L(N)
2n
is the list of qubit pointers under consideration. Let Conf , be the set of configurations over n
n
qubits. The initial configuration in Conf of a program D∶∶S on input state ∣ψ⟩∈H is c (∣ψ⟩)≜
n 2n init
(S,∣ψ⟩,{1,...,n},[1,...,n]). A final configuration can be defined in the same way as c (∣ψ⟩) ≜
final
(⊺,∣ψ⟩,{1,...,n},[1,...,n]).
5

<!-- Page 6 -->

1 decl qft(q¯){ 6 decl rot(q¯){ 11 decl shift(q¯){
2 q¯[1]∗=H; 7 if ∣q¯∣>1 then 12 if ∣q¯∣>1 then
3 call rot(q¯); 8 CPHASE(q¯[−1],q¯[1],∣q¯∣) 13 SWAP(q¯[1],q¯[−1])
4 call shift(q¯); 9 call rot(q¯⊖[−1]); 14 call shift(q¯⊖[−1]);
5 call qft(q¯⊖[−1]);}, 10 else skip;}, 15 else skip;}
∶∶
16
17 call qft(q¯);
shift
H R R R H R R H R H
4 3 2 3 2 2
Figure 5: Program QFT for the quantum Fourier transform.
Each unitary transformation U of a unitary application q¯[i] ∗= Uf(j);, comes with a function U
assigning a unitary matrix U (f)(n) ∈ C2×2 to each integer n and polynomial-time approximable
total function f ∈ Z → [0,2π). For example, the gates of the quantum Fourier transform can be
(cid:74) (cid:75)
defined by R ≜ Ph (λx.π/2x−1)(n) with Ph (f)(n) ≜ (1 0 ). The other basic unary gates are
n (cid:74) (cid:75) 0eif(n)
the NOT and the R gate.

## Y ⋅

The big-step semantics ⋅—→⋅ is defined in Figure 4 as a relation in ⋃ Conf ×N×Conf . Stan-
(cid:74) (cid:75) (cid:74) (cid:75) n∈N n n
dard notations from quantum computation are used such as tensor product ⊗, ⟨ψ∣ for the conjugate
transposeof∣ψ⟩,orgivenadimensionm,∣k⟩
n

## ≜I

2n−1
⊗∣k⟩⊗I
2m−n
fork∈{0,1}. InFigure4,thesetA
ofaccessiblequbitsisusedtoensurethatunitaryoperationsonqubitscanbephysicallyimplemented.
For example, to ensure reversibility, in a quantum branch qcase s[i] of {0→S
0

## ,1→S

1
}, statements

## S

0
and S
1
cannot access s[i].
Definition 1. The time complexity Time ∶N→N of a program P≜D∶∶S is defined by

## P

Time (n)≜ max {m∈N∣∃∣ϕ ′⟩∈H , c (∣ϕ⟩)—m→c (∣ϕ ′⟩)}.
P 2n init final
∣ϕ⟩∈H
2n
Intuitively,whenc—m→c ′holds,thetimecomplexity misanintegercorrespondingtothemaximum
numberofprocedurecallsperformedovereach(classicalandquantum)branchduringtheevaluation
of a configuration c∈Conf . We write P (∣ψ⟩)=∣ψ ′⟩, whenever c (∣ψ⟩)—m→c (∣ψ ′⟩) holds for
n init final
some m. If the program P terminates on any input (i.e., always reaches a final configuration) then
P is a total function on quantum states.
(cid:74) (cid:75)
Example 1. For the program PAIRS of Figure 1, Time (n) = ⌊n⌋+1 since each procedure call
(cid:74) rem (cid:75) oves two qubits until it reaches a sorted set q¯ such tha PA t I ∣ R q¯ S ∣≤1 (de 2 pending on whether n is odd or
even) and for both sizes there are no more procedure calls.
2.3 Polynomial Branching Programs
We define three restrictions on the programming language to consider only a strict subset, called
pbp for Polynomial Branching Programs, on which branch sequentialization can be avoided. First,
we define a well-foundedness criterion to consider only terminating programs. A program P is wellfounded if each recursive procedure call removes at least one qubit in its parameter. wf denotes
the set of well-founded programs. Then, we define a criterion to exclude programs with exponential
runtime. Toward that end, the notion of width of a procedure proc in a program P is introduced.
Definition 2. Given a program P, the width of a procedure proc ∈ P, denoted width (proc), is

## P

defined as width (proc)≜wproc(Sproc), where wproc(S) is defined inductively as follows:

## P P P

6

<!-- Page 7 -->

wproc(skip;)≜0

## P

wproc(q ∗= Uf(i);)≜0,

## P

wproc(S S )≜wproc(S )+wproc(S ),

## P 1 2 P 1 P 2

wproc(if b then S else S )≜max(wproc(S ),wproc(S )),

## P 0 1 P 0 P 1

wproc(qcase q of {0→S ,1→S })≜max(wproc(S ),wproc(S )),

## P 0 1 P 0 P 1

⎧
⎪⎪1 if proc∼ proc’,
wproc(call proc’(s);)≜⎨ P
P ⎪⎪ ⎩0 otherwise.
Let width ≤1 be the set of programs with procedures of width at most 1.
Programs of width 1 are inherently polynomial as they cannot perform an exponential number of
procedure calls in sequence. However the total number of calls in superposition may be exponential
for such programs by definition of the width for conditional and quantum case.
Finally, for the purpose of our compilation process, we impose further syntactical conditions on
programs. Werestrictourattentiontowhatwewillcallbasicprograms. Letbasicdenotethesetof
programs where each call to a procedure is performed either on the variable q¯ or on a unique sorted
set s that is fixed for the whole program.
Definition3(PolynomiallyBranchingPrograms). Thesetpbpof polynomiallybranchingprograms
is defined as pbp≜wf∩width ≤1 ∩basic.
Noticethatpbpisstrictlyincludedintheprogramminglanguageof[17],thatroughlycorresponds
to wf∩width , where procedure calls can take an extra integer parameter.
≤1
Example 2. The QFT program written in Figure 5 is in pbp. Indeed, the program QFT is in basic as
calls are only performed on either q¯ or q¯⊖[−1]. It is also in wf as all recursive calls are performed on
parameterq¯⊖[−1]. Finally, itisinwidth ≤1 aswidth QFT (qft)=width QFT (rot)=width QFT (shift)=1.
The restriction to programs in pbp does not impact negatively the expressive power of our study
from an extensional viewpoint as, by Theorem 3, pbp is sound and complete for the class fbqp of
functions in {0,1}∗ →{0,1}∗, i.e., functions that can be approximated with at least 2/3 probability
by a quantum Turing machine running in polynomial time [6, 29].
3 Compilation Strategy
We now present the compilation algorithm from wf∩width to quantum circuits based on the
≤1
merging strategy of Figure 2(c). Compilation is restricted to programs in wf∩width
≤1
for two
reasons. The well-foundedness criterion wf ensures that the compilation always terminates. The
restriction to width prevents exponential blow-up. Note however that, in Theorem 2, the pbp
≤1
restrictions are required to avoid the branch sequentialization problem.
3.1 Anchoring and Merging
A control structure cs is a partial map in N → {0,1}. Intuitively, cs represents a map from qubit
pointers to their control values for a controlled gate and will also be used as a shorthand notation in
circuits. For n∈N and k ∈{0,1}, let cs[n∶=k] be the control structure obtained from cs by setting
cs anchoring cs cs cs merging cs cs
k callproc l −−−−−−→ ap k roc k Sproc l ap k roc k callproc l −−−−−→ ap k roc k l
Figure 6: Anchoring and merging.
7

<!-- Page 8 -->

cs cs
cs —→ n —→ n U(f)(m) cs —→ cs cs
skip; q¯[n]∗=Uf(m);

## S1S2 S1 S2

(cid:74) (cid:75)
cs —→ cs cs —→ cs cs
n qcaseq¯[n]of n
if bthenS1 elseS0
Sb {0→S0,1→S1 }

## S0 S1

⎧ ⎫
callp c r s oc(s); —→
⎪⎪⎪⎪
⎨ ⎪⎪⎪⎪ Sproc c { s s/q¯} ifw P proc(Sproc)=0, Sproc c { s
p
s
r
/
o
q¯
c
} otherwise.
⎪⎪⎪⎪
⎬ ⎪⎪⎪⎪
⎩ ⎭
Figure 7: Rewrite rules of compile.
cs(n)=k. We denote by dom(cs) the domain of the control structure and by ⋅, the control structure
such that dom(⋅)=∅.
During the compilation of the program statement, every recursive call is handled as follows: if
it is the first call with this procedure name and input size, an ancilla is created and its procedure
statement is compiled under a control on this ancilla (anchoring), otherwise this procedure call has
already been compiled and the control structure of the new call is sent into the corresponding ancilla
(merging). Anchoring and merging are represented in Figure 6 as rewrite rules on quantum circuits
for a procedure call call proc(s), cs denoting the control structure corresponding to the (possibly
nested) quantum cases, where the procedure call occurs. aproc represents the ancilla introduced (in
k
case of anchoring) or reused (in case of merging). The integer k refers to the number ∣s∣ of qubits in
the procedure call. The grey box materializes the controlled statements left to compile.
3.2 The compile Algorithm
Let controlled statements be pairs of the shape (cs,S), for some control structure cs and some statement S. In the compilation process, controlled statements (cs,S) are used to represent a statement S
thatremainstobecompiledintoaquantumcircuitC togetherwithacontrolstructurecs,representing the qubits controlling the compiled circuit C. The compilation algorithm compile is described
by the rewrite rules of Figure 7. Generating the circuit corresponding to the program P = D ∶∶ S
will consist in running compile on the controlled statement (⋅,S) for a fixed list of qubits pointers
[1,...,n] (hence, an input of fixed size n). We denote by compile(P,n) the circuit obtained for
program P on size n. The algorithm standardly generates the quantum circuit corresponding to a
wf∩width
≤1
programinductivelyonthestatementS. Indeed,intherulesofFigure7whencompile
is called on a given controlled statement (cs,S), an inductive call to compile is performed on controlled statements whose statements are sub-statements of S. The two base case are the rules for the
skip statement and the unitary application. In these cases, the compilation just outputs the identity
circuitandacontrolledgatecomputingtheunitary,respectively. Therulesforsequenceandquantum
case perform two inductive calls to compile on each branch of the statement. The rule for quantum
caseistheonlyrulethatdirectlyperformschangesonthecontrolstructure. Intheparticularcaseof
a call to a recursive procedure (i.e., when wproc(Sproc)>0), compile calls the optimize subroutine

## P

to perform anchoring and merging. This call to optimize is highlighted in Figure 7 through the use
of a shaded square , which takes the procedure name proc as superscript. We call this process
the optimization of procedure proc.
The rewrite rules for the subroutine optimize on procedure proc are described in Figure 8. This
subroutine takes two input parameters:
• a first list l of controlled statements, the ones to be optimized,
• a second list of controlled statements, called contextual list and denoted by , consisting in
controlled statements that are orthogonal to those in l and do not contain recursive procedure
calls.
As described by the last rule of Figure 7, each initial call to optimize is performed on the singleton
8

<!-- Page 9 -->

cs
proc ⎧ ⎪⎪⎪⎪⎪
cs
proc
cs cs cs
proc ⎫ ⎪⎪⎪⎪⎪

## S1S2

l —→⎨ ⎪⎪⎪⎪⎪
⎩

## S1

l

## S 2

ifw P proc(S1 )=1,

## S1 S 2

l otherwise. ⎬ ⎪⎪⎪⎪⎪
⎭
⎧ ⎫
ifbthenSt
c
r
s
ue
p
e
r
l
o
s
c
eSfalse
l —→
⎪⎪⎪⎪⎪
⎨ ⎪⎪⎪⎪⎪

## ⎩ S

cs
b
pro
l
c
ifw P proc(S b )=1, l
pro

## S

c
cs
b
otherwise.
⎪⎪⎪⎪⎪
⎬ ⎪⎪⎪⎪⎪
⎭
⎧ ⎫
n { q 0 c → as S e 0 c , q¯ s 1 [
p
n
r
→ ]
o
o
c
S f 1 } l —→
⎪⎪⎪⎪⎪⎪⎪
⎨ ⎪⎪⎪⎪⎪⎪⎪ ⎩ n cs[n S b ∶=b] l
proc
cs[n S ∶= 1− 1 b −b] w i w f P pr P p ∃ o r b c oc ( ∈ ( S S { b 0 ) 1− , = b 1 ) } 1 = s a . 0 n t , . d n S cs 0
p
S c
r
s 1
oc
l otherwise.
⎪⎪⎪⎪⎪⎪⎪
⎬ ⎪⎪⎪⎪⎪⎪⎪ ⎭
proc
proc ap ∣s r ∣ oc’
anchoring: cs —→
l cs cs
callproc’(s); l
Sproc’{s/q¯}
proc proc
ap
∣s
r
∣
oc’ ap
∣s
r
∣
oc’
merging: —→
cs l cs l cs
callproc’(s);
proc
—→
[]
Figure 8: Rewrite rules of optimize.
listcontainingonecontrolledstatement(cs,Sproc{s/q¯})andacontextualcircuitequaltotheidentity
circuit.
In Figure 8, the rules are applied by considering the first controlled statement in the list l. We
just specify the most interesting case below:
• for a controlled statement (cs,S S ), two distinct rules can be applied. In the first scenario,
1 2
where wproc(S )=1, we have that S contains a recursive procedure call and S does not (this

## P 1 1 2

isaconsequenceofthewidth conditioninpbp),ortheconverse. Dependingonthis,therule
≤1
select on which control statement (cs,S ) or (cs,S ) to perform the optimization and, append
1 2
the compiled circuit of the other controlled statement to the left or to the right.
• for a controlled statement with an if statement, we precompute the boolean value b (the value
is computable), and according to whether the corresponding branch contains a recursive call or
not, we either add it to l or concatenate its compiled circuit to the contextual circuit.
• for a controlled statement with a qcase statement, one or two of the branches are added to the
list l depending on whether they are both recursive or not.
• for a controlled statement with a procedure call call proc’(s); we perform either anchoring or
merging depending on whether the ancilla aproc’ exists or not.
∣s∣
• when the list of control statement is empty (i.e., l = []), we compute the contextual list of
controlledstatements. Thislistisrearrangedintolistsofstatementsthataremutuallyrecursive
and compiled by a call to optimize. Such a partition is important to perform merging of
9

<!-- Page 10 -->

procedures with a recursion level lower than that of proc, and we give further explanation on
how it is performed in Appendix B.
3.3 Soundness of the algorithm
In this section, we discuss the validity of the compilation algorithm. One first observation should
be that, given a pbp program, the compilation necessarily terminates. For instance, in compile
(Figure 7), all rules besides the procedure call rewrite the controlled statement into either a circuit
or into instances of compile of smaller statements. In the case a procedure call, the rewriting of the
procedure body produces a finite number of calls to procedures of lower recursive level.
In optimize, a recursive procedure will result in a finite number of calls to mutually recursive
procedures – this is ensured by the well-foundedness condition wf, that requires that recursive procedure calls reduce the size of the input, therefore procedure calls either reduce the level of recursion
or the number of available qubits.
Thesoundnessofthecompilationalgorithmisensuredbyanorthogonalityinvariantinoptimize.
Let cs,cs ′ be two control structures. We say that cs and cs ′ are orthogonal if there exists i ∈
dom(cs)∩dom(cs ′) such that cs(i) = 1−cs ′(i). Two controlled statements are orthogonal if their
control structures are orthogonal.
Lemma 1. During the compilation of a pbp program P, for each optimization of a (recursive)
procedure proc, all controlled statements in the union of list l and the contextual list l are pairwise

## M

orthogonal.
This invariant ensures the validity of optimize, and the soundness of the compilation algorithm.
It is also a consequence of the width restriction in pbp, as by the definition of width, at most one
≤1
recursive call may appear per branch of a recursive procedure. This ensures that two recursive calls
on a given procedure always occur in orthogonal branches and can be simply combined in the same
ancilla. Given a circuit C, we define its semantics C naturally as the composition of the semantics
of each gate.
Theorem 1 (Soundness of compilation). Given a (cid:74)pb(cid:75)p program P and a quantum state ∣ψ⟩∈H we
2n
have that compile(P,n) (∣ψ⟩)= P (∣ψ⟩).
3.4 Illu(cid:74) strating Ex(cid:75)ample(cid:74) (cid:75)
Weillustratethecompilationprocesswiththeprogram 1 decl rec(q¯){
REC, of Figure 9. Notice that REC is in wf∩width 2 if ∣q¯∣>2 then
but does not belong to pbp, as the procedure rec pe ≤ r 1 - 3 qcase q¯[1] of{
formstworecursivecallsondifferentsortedsetsq¯⊖[1] 4
0→call rec(q¯⊖[1]);
and q¯⊖[1,2]. This example thus illustrates that the 5 1→qcase q¯[2] of{
compilation algorithm is not restricted to pbp. 6
0→skip;
Given that rec is a recursive procedure, its com- 7
1→call rec(q¯⊖[1,2]);
}
pilation is performed within optimize. We denote by 8
}
the empty box the procedure statement Srec and 9
10 else q¯[1] ∗= U;}
bythedottedbox thestatementcall rec(s);. Ap- 11 ∶∶ call rec(q¯);
plying rewrite rules to the statement of rec we obtain
the transitions: Figure 9: Program REC.
cs cs cs cs cs cs cs cs cs
q¯ l −→ qc 1 0 a → se q c q¯ a c [ l a 1 l ] s . e o .. f . , . { . l −→ qca 0 seq¯ s [ k 2] ip o ; f { l −→ l −→ l
→ } 1→call... skip;
→ }
The first step is obtained by applying the rule of if statements, where we assume that ∣q¯∣ > 2.
Afterwards, we apply twice the rule for the qcase statement, adding the two qubits q¯[1] and q¯[2]
to the control structure. Finally, the compilation of the skip statement corresponds to the empty
circuit. Wedenoteby—r—e→c theapplicationofthissequenceofrewriterules,whichisusedinFigure10.
OneimportantthingtonoticeinFigure10isthatthecompilationstrategydoesnotavoidbranch
sequentialization locally but rather asymptotically in the construction of the circuit. In other words,
10

<!-- Page 11 -->

q¯[1]
rec
q¯[1]
anch. an 1
q¯ q¯[2] −
−−→ −−−→ q¯[2]
q¯ [1,2]
(cid:9) q¯ [1,2]
(cid:9)
rec
q¯[1] q¯[1] 
an q¯ − [2 1 ] merge an q¯ − [2 1 ] anch. an q¯ − [1 1 ] y
q¯[2]
an − 2 ←−−−− an − 2 ←−−− q¯[3]
q¯[3] q¯[3] q¯ [1 3]
q¯ (cid:9) [1 − 3] q¯ (cid:9) [1 − 3] (cid:9) −
rec
q¯[1]  q¯[1] q¯[1]
an
−
1 y an−1 an−1
q¯[2] q¯[2] q¯[2]
an 2
anch. an−2 merge an−2
− −−−→ q¯[3] −−−−→ q¯[3]
q
q
¯
¯
[
[
3
4
]
]
an−3 an−3
q¯[4] q¯[4]
q¯ (cid:9) [1 − 4] q¯ (cid:9) [1 − 4] q¯ (cid:9) [1 − 4]
rec
q¯[1] q¯[1]
q¯[1] 
an
q¯
−
[2
1
]
an
q¯
−
[2
1
]
an−1 y
q¯[2]
an q¯ − [3 2 ] merge an q¯ − [3 2 ] anch. an−2
q¯[3]
an
q¯
−
[4
3
]
←−−−− an
q¯
−
[4
3
]
←−−− an−3
q¯[4]
an−4 an−4
q¯[5]
q¯[5] q¯[5]
q¯ [1 5]
q¯ [1 5] q¯ [1 5] (cid:9) −
(cid:9) − (cid:9) −
Figure 10: Example of anchoring and merging for the program REC in Figure 9.
theqcasestatementinrulerecdoesgeneratetwoinstancesofSrec inthecircuitinsequence,onefor
each branch. However, the merging of calls to rec on inputs of the same size ensures that only one
instance per input size needs to be compiled, and therefore this strategy achieves linear complexity
in the number of gates.
4 Main Results
4.1 No Branch Sequentialization
First, we show that the problem of branch sequentialization is solved in pbp. For that purpose,
we show that the size of quantum circuit obtained through compiling a pbp program is bounded
asymptotically by the time complexity of the program. As the time complexity is the maximum
of the complexity of the two branches of a quantum case statement, the branch sequentialization
problem is avoided on pbp programs, as the size of the circuit is asymptotically equal to its time
semantics. Given a circuit C, let #C denote its size, i.e., number of gates and wires.
Theorem 2 (No branch sequentialization). Given a program P∈pbp and input n∈N, we have that
# compile(P,n)=O(Time (n)) holds.

## P

One may notice that, in the rules of compile (Figure 7), the compilation of a qcase statement
generatestwocontrolledstatementsinsequence. Similarly,theruleofoptimize(Figure8)forqcase
statements appends two controlled statements to the list l in the case where they are both recursive.
This does not pose a problem as, anchoring and merging will ensure that the asymptotic complexity
of this statement will be given by the maximum complexity of the branches.
11

<!-- Page 12 -->

(cid:117) (cid:125) (cid:117) (cid:125)
(cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:118) ∣ ∣ 0 0 ⟩ ⟩ U U (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:126) = (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:119) (cid:118) ∣ ∣ 0 0 ⟩ ⟩ U (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:126)
Figure 11: Merging orthogonal controlled statements.
u } u }
w w w w w w w w w w w w w w w w w w v | | | 0 0 0 i i i (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) ~ = w w w w w w w w w w w w w w w w w w w v | | | 0 0 0 i i i (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) (cid:127) ~
Figure 12: Implementation of a controlled permutation in log-depth.
Example 3. By Theorem 2 and Example 1, we have that #compile(PAIRS,n)=O(n).
4.2 Polynomial-Time Soundness and Completeness
Having shown in Theorem 2 that pbp programs can avoid branch sequentialization, we now turn to
the question of whether they constitute an interesting fragment of quantum programs, given that it
is restricted by the wf, width and basic conditions. We show that the set of pbp programs is
≤1
sound and complete for quantum polynomial time via an implicit characterization of fbqp, i.e. the
setofclassicalfunctionsthatcanbeapproximatedwithboundederrorbyapolytimequantumTuring
machine [30, 17].
Since the considered programming language does not allow for qubit creation, in order to define
functions where the output is larger than the input, we make use of polytime padding. A polytime
padding function is a function f ∶ {0,1}∗ → {0,1}∗ computable by a (classical) polytime Turing
machine such that f(x)=xy, for some y depending only on the length of x (and not the value of x).
Given a set F of programs, F denotes the set of functions given by P ○f, where P ∈ F, f is a
polytime padding function, and ○ is the standard function composition. For any p∈(1,1], we denote
2
by F
≥p
the set of functions
(cid:74)
in
(cid:75)
F that approximate a classical functio
(cid:74)
n w
(cid:75)
ith probability at least p.
Theorem 3 (Soundness and Completeness). pbp =fbqp.
≥2
(cid:74) (cid:75) (cid:74) (cid:75) 3
4.3 Extension to Programs in wf (cid:74)∩w (cid:75) idth
≤1
The basic restriction of pbp can be thought of as ensuring that qubits are consumed in a uniform
way. As a consequence, any two procedure calls on inputs of size n will correspond to precisely
the same n qubits. This guarantees that two compatible procedure calls can be merged simply by
combining control structures in the same ancilla. Without this constraint (i.e., on wf∩width ),
≤1
merging can be done by control-swapping registers into a single procedure call. For k instances of a
procedure on input size n, this requires k−1 controlled swaps, each requiring O(n) operations in the
worst case. An example of merging two unitary gates U with controlled-swaps is given in Figure 11.
If we allow for parallelization of gates in the circuit, this can be done in logarithmic depth, as shown
in Lemma 2. An example of a controlled permutation is shown in Figure 12, where vertical dashed
lines separate time slices where gates can be applied simultaneously.
Lemma 2. Any controlled permutation on n qubits can be performed with a quantum circuit of size
O(n) and depth O(logn).
12

<!-- Page 13 -->

An extension of compile with controlled-swapping as in Figure 11 used for merging procedures
ensures the following bound for wf∩width programs.
≤1
Theorem 4. For P∈wf∩width ≤1 , compile(P,n) results in a circuit with O(log(n)⋅Time P (n))
depth and O(n⋅Time (n)) size.

## P

4.4 Comparison with Existing Work
The compile algorithm strictly improves upon the size bounds of other compilation algorithms [17],
as illustrated by Table 1. In some cases, such as Examples 5 and 4 given in Appendix D, we find
families of programs where the gap in complexity (i.e. the degree of the polynomial) can be made
arbitrarily large.
In k-Chained Substrings (Example 5), we consider the problem of detecting whether an input
string contains substrings y ,...,y appearing in that order. For a certain choice of substrings y ,
1 k i
we define a pbp program of linear time complexity for which the compilation strategy in [17] results
in circuits of size Θ(n3k). The problem Sum(r), given in Example 6, consists of checking if an input
x=x 1 ...x n satisfies ∑n i=1 x i =r.

### Circuit complexity


### Problem Example [17] compile


### Full Adder Example 4 Θ(n) Θ(n)

Quantum Fourier Transform Example 2 Θ(n2) Θ(n2)
k-Chained Substrings Example 5 Θ(n3k) Θ(n)

### Sum(r), r≥1 Example 6 Θ(nr) Θ(n)

Table 1: Circuit size complexity bounds.
5 Conclusions and Future Work
The quantum control statement, while being a central component of programming languages with
quantum control flow, usually incurs a remarkable slowdown in the program complexity in any automatic implementation, which poses a problem to the quantum programmer. In this paper, we
have demonstrated that such a slowdown can be avoided by restricting the program structure. This
was achieved using techniques from quantum implicit computational complexity, which allow not
only to selectively reason about efficient programs (polytime soundness) but also to ensure that the
techniques are sufficient in principle for any program (polytime completeness).
pbp is then the first quantum programming language with a compilation strategy that ensures
that the quantum control statement can be compiled onto a circuit whose size (i.e., number of gates
andwires)isboundedasymptoticallybythemaximumofthetimecomplexityofitsbranches. While
this language is extensionally complete for fbqp and expressive enough to write quantum algorithms
such as QFT or Full Adder in a natural way, it would be interesting to investigate in what ways its
expressive power can be improved, and how different languages can also be shown to avoid branch
sequentialization.
6 Acknowledgments
This work is supported by the the Plan France 2030 through the PEPR integrated project EPiQ
ANR-22- PETQ-0007 and the HQI platform ANR-22-PNCQ-0002; and by the European projects
NEASQC and HPCQS.

### References

[1] Samson Abramsky. No-cloning in categorical quantum mechanics. Semantic Techniques in
Quantum Computation, pages 1–28, 2009.
13

<!-- Page 14 -->

[2] Leonard M. Adleman, Jonathan DeMarrais, and Ming-Deh A. Huang. Quantum computability. SIAM Journal on Computing, 26(5):1524–1540, 1997. arXiv:https://doi.org/10.1137/
S0097539795293639, doi:10.1137/S0097539795293639.
[3] Thorsten Altenkirch and Jonathan Grattage. A functional quantum programming language. In
20th Annual IEEE Symposium on Logic in Computer Science (LICS’05), pages 249–258. IEEE,
2005.
[4] John Baez. Quantum quandaries: a category-theoretic perspective. The structural foundations
of quantum gravity, pages 240–265, 2006.
[5] Adriano Barenco, Charles H Bennett, Richard Cleve, David P DiVincenzo, Norman Margolus,
PeterShor,TychoSleator,JohnASmolin,andHaraldWeinfurter.Elementarygatesforquantum
computation. Physical review A, 52(5):3457, 1995.
[6] Ethan Bernstein and Umesh Vazirani. Quantum complexity theory. SIAM Journal on Computing, 26(5):1411–1473, 1997. doi:10.1137/S0097539796300921.
[7] Hans J. Briegel, David E. Browne, Wolfgang Dür, Robert Raussendorf, and Maarten Van den
Nest. Measurement-based quantum computation. Nature Physics, 5(1):19–26, 2009. doi:10.
1038/nphys1157.
[8] Andrew M. Childs and Nathan Wiebe. Hamiltonian simulation using linear combinations of
unitary operations. Quantum Information & Computation, 12(11-12):901–924, 2012.
[9] Andrea Colledan and Ugo Dal Lago. Circuit width estimation via effect typing and linear
dependency. In European Symposium on Programming, pages 3–30. Springer, 2024.
[10] AndreaColledanandUgoDalLago. Flexibletype-basedresourceestimationinquantumcircuit
descriptionlanguages.ProceedingsoftheACMonProgrammingLanguages,9(POPL):1386–1416,
2025.
[11] UgoDalLago,AndreaMasini,andMargheritaZorzi. Quantumimplicitcomputationalcomplexity. Theoretical Computer Science, 411(2):377–409, 2010. doi:10.1016/j.tcs.2009.07.045.
[12] Vincent Danos and Elham Kashefi. Determinism in the one-way model. Physical Review A,
74(5):052310, 2006. doi:10.1103/PhysRevA.74.052310.
[13] Niel de Beaudrap, Xiaoning Bian, and Quanlong Wang. Fast and Effective Techniques for T-
CountReductionviaSpiderNestIdentities. SchlossDagstuhl–Leibniz-ZentrumfürInformatik,
2020. doi:10.4230/LIPICS.TQC.2020.11.
[14] Alejandro Díaz-Caro, Mauricio Guillermo, Alexandre Miquel, and Benoît Valiron. Realizability
in the unitary sphere. In 2019 34th Annual ACM/IEEE Symposium on Logic in Computer
Science (LICS), pages 1–13. IEEE, 2019.
[15] Peng Fu, Kohei Kishida, and Peter Selinger. Linear dependent type theory for quantum programming languages. In Proceedings of the 35th Annual ACM/IEEE Symposium on Logic in
Computer Science, pages 440–453, 2020.
[16] DavidGosset,RobinKothari,andKewenWu. QuantumstatepreparationwithoptimalT-count.
arXiv preprint arXiv:2411.04790, 2024.
[17] Emmanuel Hainry, Romain Péchoux, and Mário Silva. A programming language characterizing
quantum polynomial time. In Foundations of Software Science and Computation Structures,
pages 156–175. Springer, 2023. doi:10.1007/978-3-031-30829-1_8.
[18] Aram W. Harrow, Avinatan Hassidim, and Seth Lloyd. Quantum Algorithm for Linear Systems
ofEquations. Physical Review Letters,103(15),October2009. doi:10.1103/physrevlett.103.
150502.
[19] Chris Heunen and Jamie Vicary. Categories for Quantum Theory: an introduction. Oxford
University Press, 2019.
14

<!-- Page 15 -->

[20] Aleks Kissinger and John van de Wetering. Reducing the number of non-Clifford gates in quantum circuits. Phys. Rev. A, 102:022406, Aug 2020. doi:10.1103/PhysRevA.102.022406.
[21] Emanuel Knill, Raymond Laflamme, and Gerard J. Milburn. A scheme for efficient quantum
computation with linear optics. Nature, 409(6816):46–52, Jan 2001. doi:10.1038/35051009.
[22] Gui-LuLongandYangSun. Efficientschemeforinitializingaquantumregisterwithanarbitrary
superposed state. Phys. Rev. A, 64:014303, Jun 2001. URL: https://link.aps.org/doi/10.
1103/PhysRevA.64.014303, doi:10.1103/PhysRevA.64.014303.
[23] D. Maslov, G.W. Dueck, D.M. Miller, and C. Negrevergne. Quantum Circuit Simplification and
Level Compaction. IEEE Transactions on Computer-Aided Design of Integrated Circuits and
Systems, 27(3):436–444, March 2008. doi:10.1109/tcad.2007.911334.
[24] Cristopher Moore and Martin Nilsson. Parallel Quantum Computation and Quantum Codes.
SIAM Journal on Computing, 31(3):799–815, 2001. doi:10.1137/S0097539799355053.
[25] Yunseong Nam, Neil J. Ross, Yuan Su, Andrew M. Childs, and Dmitri Maslov. Automated
optimization of large quantum circuits with continuous parameters. npj Quantum Information,
4(1):23, May 2018. doi:10.1038/s41534-018-0072-4.
[26] Michael A. Nielsen and Isaac L. Chuang. Quantum Computation and Quantum Information:
10th Anniversary Edition. Cambridge University Press, 2011.
[27] Peter Selinger. Towards a quantum programming language. Mathematical Structures in Computer Science, 14(4):527–586, 2004.
[28] Xiaoming Sun, Guojing Tian, Shuai Yang, Pei Yuan, and Shengyu Zhang. Asymptotically
optimalcircuitdepthforquantumstatepreparationandgeneralunitarysynthesis. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 42(10):3301–3314, 2023.
[29] Tomoyuki Yamakami. A Schematic Definition of Quantum Polynomial Time Computability. J.
Symb. Log., 85(4):1546–1587, 2020. doi:10.1017/jsl.2020.45.
[30] Tomoyuki Yamakami. Expressing Power of Elementary Quantum Recursion Schemes for Quantum Logarithmic-Time Computability. In Agata Ciabattoni, Elaine Pimentel, and Ruy J. G. B.
deQueiroz,editors,Logic,Language, Information,andComputation,pages88–104,Cham,2022.
Springer International Publishing. doi:10.1007/978-3-031-15298-6_6.
[31] Andrew Chi-Chih Yao. Quantum circuit complexity. In Proceedings of 1993 IEEE 34th Annual
Foundations of Computer Science, pages 352–361, 1993. doi:10.1109/SFCS.1993.366852.
[32] Charles Yuan and Michael Carbin. Tower: Data Structures in Quantum Superposition. Proceedings of the ACM on Programming Languages, 6(OOPSLA2):259–288, Oct 2022. doi:
10.1145/3563297.
[33] Charles Yuan, Agnes Villanyi, and Michael Carbin. Quantum Control Machine: The Limits of
Control Flow in Quantum Programming. Proceedings of the ACM on Programming Languages,

## 8(Oopsla1):1–28, 2024.

[34] Xiao-MingZhang,TongyangLi,andXiaoYuan. Quantumstatepreparationwithoptimalcircuit
depth: Implementations and applications. Physical Review Letters, 129(23):230504, 2022.
15

<!-- Page 16 -->

A Semantics of expressions
(e,l)⇓
τ1
m (d,l)⇓
τ2
n
(Op)
(i,l)⇓ Zn
(Unit)
(cid:74) (cid:75) (cid:74) (cid:75)
(e op d,l)⇓ op ( τ1 , τ2 ) op (m,n) (Uf(i),l)⇓ C2×2 Uf (n)
(cid:74) (cid:75) (cid:74) (cid:75)(cid:74) (cid:75)
(Cst) ( (cid:74) s,l) (cid:75) ⇓ L(N) [x 1 ,...,x m ] (i,l)⇓ Zk∈[ (cid:74) 1,m (cid:75) ] (Rm )
(n,l)⇓ Zn (s⊖[i],l)⇓ L(N) [x 1 ,...,x k−1 ,x k+1 ,...,x m ] ∈
(s,l)⇓ L(N) [x 1 ,...,x n ] (Size) (s,l)⇓ L(N) [x 1 ,...,x m ] (i,l)⇓ Zk∉[1,m] (Rm )
∉
(∣s∣,l)⇓ Zn (s⊖[i],l)⇓ L(N) []
(q¯,l)⇓ L(N)l (Var) (s,l)⇓ L(N) [x 1 ,.
(
.
s
.
[i
,
]
x
,l
m
)
]
⇓ Nx
(
k
i,l)⇓ Zk∈[1,m] (Qu ∈ )
(s,l)⇓ L(N) [x 1 ,...,x m ] (i,l)⇓ Zk∉[1,m] (Qu )
∉
(s[i],l)⇓ N0
Figure 13: Semantics of expressions.

### B Compilation

In this appendix, we describe the compile and optimize routines in more detail. For simplicity, we
provideherethealgorithmforprogramsinpbp. Theversionforwf∩width usesadditionalcontrol
≥1
swaps in the optimize subroutine and is described in Section 4.3. The full definition of compile
(Algorithm 1) takes four inputs: a program P∈wf∩width ≤1 , a list of qubit pointers l and a control
structure cs. We make use of the following syntactic sugar to denote the initial call to compile:
compile(P,n)≜compile(P,[1,...,n],⋅),
where P is the program to be compiled, [1,...,n] is list of qubit pointers (initially all qubits), ⋅ is an
empty control structure, and {} an empty dictionary.
TheaimofcompileistogeneratethequantumcircuitcorrespondingtoPonnqubitsinductively
ontheprogramstatementofP. Whentheanalyzedstatementisarecursiveprocedurecall, compile
calls the optimize subroutine (Algorithm 2) to perform an optimization of the generated quantum
circuit via anchoring and merging. optimize has the same inputs as compile with the addition of a
list of controlled statements l and the name proc of the procedure under analysis.

### Cst

As described in Subsection 3.2, optimize manages a contextual list l of controlled statements

## M

that do not contain recursive procedure calls. At the end of optimize, we rearrange the contextual
list in the following way. Let l =[(cs ,S ,l ),...,(cs ,S ,l )] be the state of the contextual list at

### M 1 1 1 k k k

theendofoptimize. Wemayrewriteeachcontrolledstatementasalistofitsatomicelements. This
transformation, denoted seq, can be described inductively:
seq(cs,skip;,l)≜ [],
seq(cs,q ∗= Uf(j);,l)≜ [(cs,q ∗= Uf(j);,l)],
seq(cs,S S ,l)≜ seq(cs,S ,l)@seq(cs,S ,l),
1 2 1 1
seq(cs,if b then S
true
else S
false
,l)≜ seq(cs,S
b
,l), if (b,l)⇓ Bb,
seq(cs,qcase q of {0→S
0

## ,1→S

1
},l)≜ seq(cs[n∶=0],S
0
,l)@seq(cs[n∶=1],S
1
,l) if (q,l)⇓ Nn,
seq(cs,call proc(s);,l)≜[(cs,call proc(s);,l)].
16

<!-- Page 17 -->


### Algorithm 1 (compile)

Input: (D∶∶S,l,cs)∈Programs×L(N)×(N→{0,1})
1: if S= skip; then
2: C ←1 ▷ Identity circuit
3:
4: else if S=q ∗= Uf(j); and (q,l)⇓ Nn and (Uf(j),l)⇓ C2×2 M then
5: C ←M(cs,[n]) ▷ Controlled gate
6:
7: else if S=S 1 S 2 then
8: C ←compile(D∶∶S 1 ,l,cs)○compile(D∶∶S 2 ,l,cs) ▷ Composition
9:
10: else if S=if b then S true else S false and (b,l)⇓ Bb then
11: C ←compile(D∶∶S b ,l,cs) ▷ Conditional
12:
13: else if S=qcase s[i] of {0→S 0 ,1→S 1 } and (s[i],l)⇓ Nn then ▷ Quantum case
14: C ←compile(D∶∶S 0 ,l,cs[n∶=0])○ compile(D∶∶S 1 ,l,cs[n∶=1])
15:
16: else if S=call proc(s); and (s,l)⇓ L(N) [] then
17: C ←1 ▷ Nil call
18:
19: else if S=call proc(s); and (s,l)⇓ L(N)l ′=/ [] then
20: if wproc(Sproc)=0 then ▷ Non-recursive procedure call

## P

21: C ←compile(D∶∶Sproc,l ′ ,cs)
22: else
23: C ←optimize(D,[(cs,Sproc,l)],proc)
24: end if
25: end if
26: return C
This separation of statements allows for a partitioning according to the type of procedure call
appearinginthestatement. GivenalistofcontrolledstatementsL,wedenotebyprocedure_split(L)
thelist[L ,L ,...,L ]where,forproc ,...,proc areproceduresthatarenotmutuallyrecursive.
0 1 m 1 m
L ≜{(cs,S,l)∈L∶∃/ proc such that wproc(Sproc)=1 and wproc(S)=1}.

## 0 P P

L ≜{(cs,S,l)∈L∶wproci(S)=1}, i=1,...,m.
proci P
Given our choice of procedures and the controled statements obtained from seq, this partition is
well-defined. Performing these two partitions (first in terms of sequential order of statements, and
then according to procedure calls), we are able to rewrite the list l in the following way:

## M

proc1 procm proc1 procm
cs1 ... csk ... ...
···
1 1 1 t t t
−→ L0 Lproc1 Lprocm L0 Lproc1 Lprocm
S1 ... Sk ... ...
···
The different instances of optimize contain calls to procedures that are mutually recursive, which
will allow for further anchoring and merging.

### C Proofs

Theorem 1 (Soundness of compilation). Given a pbp program P and a quantum state ∣ψ⟩∈H we
2n
have that compile(P,n) (∣ψ⟩)= P (∣ψ⟩).
Proof. By induction on the structure of the pbp program P = D ∶∶ S. One can check by inspection
of each cas(cid:74)e that the com (cid:75) pile rul(cid:74)es(cid:75)for non-recursive statements corresponds to the straightforward
circuit semantics of quantum programs.
Likewise, the rewriting rules of optimize, given in Figure 8, can be easily checked using the
orthogonality invariant of Lemma 1. For instance, consider the case of the sequential statement
17

<!-- Page 18 -->

Algorithm 2 (optimize) Build circuit for recursive procedure proc
Inputs: (D,l ,proc)∈Decl×L(Cst×L(N))×Procedures

### Cst

1: C L ←1; C R ←1;C M ←1; l M ←[]; Anc←{}; P←D∶∶skip;
2: while l Cst ≠[] do
3: (cs,S,l)←hd(l Cst ); l Cst ←tl(l Cst )
4:
5: if S=S 1 S 2 then
6: if w P proc(S 1 )=1 then
7: l Cst ←l Cst @[(cs,S 1 ,l)]; C R ←compile(D∶∶S 1 ,l,cs)○C R
8: else
9: l Cst ←l Cst @[(cs,S 2 ,l)]; C L ←C L ○compile(D∶∶S 1 ,l,cs)
10: end if
11: end if
12:
13: if S=if b then S true else S false and (b,l)⇓ Bb then
14: if w P proc(S b )=1 then
15: l Cst ←l Cst @[(cs,S b ,l)]
16: else
17: l M ←l M @[(cs,S b ,l)]
18: end if
19: end if
20:
21: if S=qcase q of {0→S 0 ,1→S 1 } and (q,l)⇓ Nn then
22: if w P proc(S 0 )=1 and w P proc(S 1 )=1 then
23: l Cst ←l Cst @[(cs[n∶=0],S 0 ,l),(cs[n∶=1],S 1 ,l)]
24: else if w P proc(S 1 )=0 then
25: l Cst ←l Cst @[(cs[n∶=0],S 0 ,l)]; l M ←l M @[(cs[n∶=1],S 1 ,l)]
26: else if w P proc(S 0 )=0 then
27: l Cst ←l Cst @[(cs[n∶=1],S 1 ,l)]; l M ←l M @[(cs[n∶=0],S 0 ,l)]
28: end if
29: end if
30:
31: if S=call proc’(s); and (s,l)⇓ L(N)l ′=/ [] then
32: if (proc’,∣l ′∣)∈Anc then
33: Let a=Anc[proc’,∣l ′∣] in /* compatible procedure exists: merging */
34: C L ←C L ○NOT(cs,a);
35: C R ←NOT(cs,a)○C R ;
36: else
37:
a←new ancilla() /* no compatible procedure: anchoring */
38:

### Anc[proc’,∣l ′∣]←a;

39: C L ←C L ○NOT(cs,a); C R ←NOT(cs,a)○C R ;
40: l Cst ←l Cst @[(⋅[a=1],Sproc’,l ′)]
41: end if
42: end if
43: end while
44: T =max(cs,S,l)∈lM (∣sec(cs,S,l)∣)
45: for 1≤t≤T do
46:

## L←⋃

(cs,S,l)∈lM
sec(cs,S,l)[t]
47:

## L

0

## ,...L

m
=procedure_split(L)/* m= number of recursive procedure families */
48: C M ←C M ○(○ (cs,S,l)∈L 0 compile(D∶∶S,l,cs))○(○m i=1 optimize(D,L i ,proc i ))
49: end for
50: return C L ○C M ○C R
18

<!-- Page 19 -->

S=S S . Inthecasewherewproc(S )=1,wecanderivetheruleforthestatementwiththefollowing

## 1 2 P 1

steps:
proc proc proc proc
cs (a) cs cs (b) cs cs (c) cs cs
l l l l
−−→ −−→ −−→

## S1S2 S1 S2 S1 S2 S1 S2

where(a)correspondstothedefinitionofthesequentialstatement,in(b)wemakeuseofthefactthat
(cs,S ) is orthogonal to all controlled statements in l and therefore can be commuted in the circuit,
2
and in step (c) we likewise make use of orthogonality, in this case with the controlled statements in
thecontextuallist. Othercasecanbeinspectedtofollowashortsequenceofsteps, suchasdescribed
for the sequential statement.
For instance, in the case of anchoring, we consider the following composition of rules
proc proc proc
cs
proc
(a)
ap
|s
r
|
oc’
(b)
ap
|s
r
|
oc’
(c)
ap
|s
r
|
oc’
l cs cs cs cs cs cs
−−→ −−→ −−→
callproc’(s); l l l
Sproc’s/q¯ Sproc’s/q¯ Sproc’s/q¯
{ } { } { }
where, likewise, (a) corresponds to the typical circuit semantics of a procedure call (with an added
anchoring ancilla), and (b) and (c) make use of the orthogonality of cs with the right side of the
circuit. The validity of merging and also be checked:
l
proc proc
aproc’ aproc’
|s| |s|
(a)
cs l0 −−→ cs l0
callproc’(s); Sproc’ s/q¯ Sproc’ s/q¯ Sproc’ s/q¯
{ } { } { }
proc proc proc
(b) ap |s r | oc’ (c) ap |s r | oc’ (d) ap |s r | oc’
−−→ l0 cs −−→ l0 cs cs −−→ cs l0 cs
Sproc’ { s/q¯ } Sproc’ { s/q¯ } Sproc’ { s/q¯ } Sproc’ { s/q¯ }
Step (a) can be seen as the definition of the procedure call. Since we are in the merging scenario,
a similar procedure call has already been performed and is anchored to its corresponding ancilla.
Withoutlossofgenerality(sinceallcontrolledstatementsinl areorthogonalandthereforecommute)
weassumethatthiscallappearsattheendofl(wereusethenamelinthecircuitrewritinghereasan
abuse of notation). Rule (b) simply indicates that since cs is orthogonal to other control structures
in l, we may move the controlled statements so that they are adjacent, and where we apply step
(c) to perform merging. Since cs is orthogonal to ⋅[aproc’ =1] the control is added to the ancilla as
∣s∣
expected. Finally, orthogonalityofcswithothercontrolstructuresmeansthatwemaymovethetwo
controlled-NOTs to the edges of the circuit.
Finally, we consider the validity of the rule for the contextual circuit. Consider a list of mutuallyorthogonal controlled statements, where the sequential form of (cs ,S ) is given by the lists of coni i
trolled statements l (i) ,...,l (i), then we have that:
1 t
cs1 ... csk ... cs2 ... csk cs2 ... csk ...
−→
l1 (1) lt (1)
−→
l1 (1) lt (1)
S1 ... Sk ... S2 ... Sk S2 ... Sk ...
The final step comes from the fact that all l (1) are orthogonal to cs , ..., cs since they include cs .
j 2 k 1
Using the sequential form of (cs ,S ), we perform the following transitions:
2 2
... cs3 ... csk ... cs3 ... csk ...
−→
l1 (2) lt (2) l1 (1) lt (1)
−→
l1 (1) l1 (2) lt (1) lt (2)
... S3 ... Sk ... S3 ... Sk ...
where we make use of the orthogonality between l (1) and l (2). Performing the same transitions for
j j′
(cs ,S ), ..., (cs ,S ), we obtain the following arrangement:
3 3 k k
19

<!-- Page 20 -->

time1 time2 timet
... ... ... ...
l(1) l(k) l(1) l(k) l(1) l(k)
1 1 2 2 t t
... ... ... ...
Given a certain 1 ≤ j ≤ t, we have that all controlled statements in ∪k l (i) (that is, all controlled
i=1 j
statements occurring in time j) are pairwise orthogonal. Therefore, we may rearrange their order
according to their recursivity, and in doing so we may consider each time separately. For instance,
in time 1, let L ≜ ∪k l (i), and let proc ,proc ,...proc denote procedures belonging to different
i=1 1 1 2 m
recursion families. Then, we perform the following partition:
L ≜{(cs,S)∈L∶∃/ proc such that wproc(Sproc)=1 and wproc(S)=1}.

## 0 P P

L ≜{(cs,S)∈L∶wproci(S)=1}, i=1,...,m.
i P
By the definition of the sequential form of each controlled statement, we note that the partition is
well-defined (e.g. there are no statements containing calls to more than one procedure). Therefore,
we are able to rearrange L and perform calls to optimize in the following way:
proc proc
1 m
...
L0 L1 Lm
...
Performingthisoperationoneachtimeblockandcomposingthecircuitsweobtaintherulegiven
in Section 3. This concludes the proof.
We introduce the notion of rank of a procedure for use in the proof of Theorem 2.
Definition 4 (Rank). Setmax(∅)≜0. GivenaprogramP, therankofaprocedureproc∈P, denoted
rk (proc), is defined as follows:

## P

⎧
⎪⎪⎪⎪ 0, if ¬(∃proc’, proc⪰

## P

proc’),
rk P (proc)≜⎨ ⎪⎪⎪⎪
⎩
m
1+
ax
m
pr
a
o
x
c⪰
pr

## P

o
p
c
r
≻
o

## P

c’
pr
{
o
r
c
k
’ {

## P

r
(
k
p

## P

ro
(p
c
r
’
o
)}
c
,
’)},
i
i
f
f
∃
pr
p
o
r
c
oc
∼
′

## P

, p
p
r
r
o
o
c
c.
⪰ P proc’∧¬(proc∼ P proc),
Theorem 2 (No branch sequentialization). Given a program P∈pbp and input n∈N, we have that
# compile(P,n)=O(Time (n)) holds.

## P

Proof. The theorem can be shown by structural induction on the program body. All cases are
straightforward except the one of the quantum control case. We make use of the following two facts
regarding pbp programs:
(a) The size of the circuit is directly proportional to its total number of unique procedure calls (in
the sense required for merging), and
(b) a recursive procedure call results in O(n) unique calls to procedures of the same rank. This is
because unique calls may only differ on procedure name (of which there is a constant amount) or
input size (for which there is a linear number of possibilites).
Consider a quantum control statement S=qcase q of {0→S ,1→S } appearing in optimize
0 1
in the context of a recursive procedure proc. By (a), the circuit size for S and S are proportional
0 1
to the (total) number of procedure calls in each statement, separately. We check that the number of
ancillas created for S is bounded by the maximum number of ancillas between S and S .
0 1
We proceed by induction on the rank r of the procedure. The base case of r =1 is given by (b),
and so we may consider r>1. For the inductive case, we consider two scenarios:
• wP (S ) = wP (S ) = 1. In this case, both S and S are of rank r, and all their recursive
proc 0 proc 1 0 1
procedure calls may be merged. Therefore, the asymptotic number of such calls is bounded
between the maximum between S and S (consider that, if there is no overlap between the
0 1
ancillas needed, their number is still bounded linearly). Applying the IH on the procedures of
rank r−1 we obtain the desired result.
20

<!-- Page 21 -->

• wP (S ) = 0 and wP (S ) = 1. In this case, S contains calls to procedures of rank r ′ < r
proc 0 proc 1 0
whereas S contains calls to procedures of rank r. According to optimize, statement S is
1 0
kept in the contextual circuit until no more statements are recursive relative to proc. The
statements of rank r ′ which are present in S are then merged with the equivalent procedures
0
thatwerederivedfromS andalsoaddedtol . Thenumberofproceduresofrankr ′ isbounded

## 1 M

asymptoticallybythemaximumbetweenthoseinS andS ,thereforeweobtainourresult.
0 1
Theorem 3 (Soundness and Completeness). pbp =fbqp.
≥2
3
Proof. Since pbp ⊊ wf∩width ≤1 ⊊ pfoq, w
(cid:74)
ith p
(cid:75)
foq the language of [17], we have that pbp ⊆
wf∩width ⊆ pfoq and,bypfoqsoundness[17,Theorem3],italsoholdsthat pbp ⊆fbqp.
≤1 ≥2
Completeness can be proven by showing that pbp can simulate the function algebra in [293], known
(cid:74) (cid:75)
to be complete for quantum polynomial time. The proof can be done using the same construction as
(cid:74) (cid:75) (cid:74) (cid:75) (cid:74) (cid:75)
in [17, Theorem 5].
Lemma 2. Any controlled permutation on n qubits can be performed with a quantum circuit of size
O(n) and depth O(logn).
Proof. Any permutation can be written as the composition of two sets of disjoint transpositions, and
therefore any permutation can be performed in constant time, using two time steps [24]. To perform
a controlled permutation, it suffices to create O(n) ancillas with the correct controlled state, which
can be done in O(logn) depth with O(n) gates.

### D Examples of Table 1

Example 4 (Quantum Full Adder). Let ADD denote the following pbp program, where the following
syntactic sugar:
TOF(q ,q ,q )≜qcase q of {0→skip;,1→CNOT(q ,q )}
1 2 3 1 2 3
encodes the Toffoli gate, i.e. the multi-controlled NOT gate.
1 decl fullAdder(q¯){
2 if ∣q¯∣>3 then /* q¯[1]=a, q¯[2]=b, q¯[−2]=∣0⟩ and q¯[−1]=c in */
3
TOF(q¯[1],q¯[2],q¯[−2])
4

### CNOT(q¯[1],q¯[2])

5 TOF(q¯[2],q¯[−1],q¯[−2]) /* c out =(a⋅b)⊕(c in ⋅(a⊕b)) */
6 CNOT(q¯[2],q¯[−1]) /* s=a⊕b⊕c in */
7

### CNOT(q¯[1],q¯[2])

8 call fullAdder(q¯⊖[1,2,−1]);
9 else skip;}
10 ∶∶ call fullAdder(q¯);
Given a carry-in bit c , we have that ADD (∣a b ...a b 0nc ⟩) = ∣a b ...a b c s ...s ⟩, where
in n n 1 1 in n n 1 1 out 1 n
c encodes the carry-out bit and s encodes the i-th sum bit. Given that fullAdder performs one
out i
recursive call to an input containing three fewer qubits, we have that Time (n)=⌊n⌋+1.
(cid:74) (cid:75) ADD 3
Example 5 (k-Chained Substrings). Consider a program for detecting a substring 001 occurring k
times in an input. For the case k=1, we define a program with procedures a , b , c , d and ⊕, with
i i i i
the graph:
1 Fi 0 0
0 0 1 1
a i b i c i d i ⊕
1
The two outgoing edges of a node indicate the two branches of a qcase statement in the corresponding
procedure, controlled on the first input qubit. We denote by F the diagram containing nodes a , b ,
i i i
21

<!-- Page 22 -->

c and d and all edges between them. Procedures consist only of a qcase statement, for the exception
i i
of ⊕:
decl a
i
(q¯){qcase q¯[1] of {0→call b
i
(q¯⊖[1]);,1→call a
i
(q¯⊖[1]);}},
decl b
i
(q¯){qcase q¯[1] of {0→call c
i
(q¯⊖[1]);,1→call b
i
(q¯⊖[1]);}},
decl c
i
(q¯){qcase q¯[1] of {0→call c
i
(q¯⊖[1]);,1→call d
i
(q¯⊖[1]);}},
decl d
i
(q¯){qcase q¯[1] of {0→call d
i
(q¯⊖[1]);,1→call ⊕(q¯⊖[1]);}},
decl ⊕(q¯){q¯[−1] ∗= NOT;}
The program body is a call to procedure a on input q¯, which results in a program that performs the
i
transformation ∣x¯y⟩↦∣x¯(y⊕b)⟩ where b∈{0,1} is 1 if and only if x¯ contains at least 1 instance of
001 as a substring.
For a general k, we consider the program P defined by
k
1 1 1 1

### F1 F2 ··· Fk ⊕

where an arrow from F i to F i+1 indicates an arrow from d i to a i+1 . The final program then consits
of a call to procedure a on input q¯. It is easy to check that P ∈pbp, and that Time (n)=n, for
1 k Pk
any k.
Example 6. Let Sum(r) be the decision problem of checking if an input bitstring x∈{0,1}n satisfies
∑n i=1 x i =r. For instance, if r=3, we may define a program SUM_3 as:
1 decl zero(q¯){qcase q¯[1] of {0→call zero(q¯⊖[1]);,1→call one(q¯⊖[1]);}},
2 decl one(q¯){qcase q¯[1] of {0→call one(q¯⊖[1]);,1→call two(q¯⊖[1]);}},
3 decl two(q¯){qcase q¯[1] of {0→call two(q¯⊖[1]);,1→call three(q¯⊖[1]);}},
4 decl three(q¯){
5 if ∣q¯∣=1 then
6 call ⊕(q¯);
7 else
8 qcase q¯[1] of {0→call three(q¯⊖[1]);,1→skip;}},
9 decl ⊕(q¯){q¯[−1] ∗= NOT;}
10 ∶∶ call zero(q¯);
We have that Time (n)=n.

## Sum_3

22

## Tables

**Table (Page 3):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  | pairs(q¯⊖[ ]) |  |  |  |
|  |  |  | 1,2 |  |  |  |


**Table (Page 3):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 6):**

|  |  |
|---|---|
|  |  |


**Table (Page 7):**

|  | l |
|---|---|
| proc |  |


**Table (Page 7):**

|  |  | l |
|---|---|---|
|  |  |  |


**Table (Page 8):**

| cs callproc(s); |
|---|
|  |


**Table (Page 8):**

| cs proc{/ } |
|---|
| S sq¯ |


**Table (Page 8):**

| cs Sproc{/ } |  |
|---|---|
| sq¯ |  |


**Table (Page 9):**

| cs qcaseq¯[n]of {0→S0,1→S1 } |  | l |
|---|---|---|
| qcaseq¯[n]of {0→S0,1→S1 } |  |  |
|  |  |  |


**Table (Page 9):**

| cs[n∶=b] |  | l | cs[n∶=1−b] S |
|---|---|---|---|
| S |  |  | S |


**Table (Page 9):**

|  |  |  |
|---|---|---|
|  |  |  |
|  | l |  |


**Table (Page 9):**

|  | l |
|---|---|
| cs |  |


**Table (Page 10):**

|  | s | l |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 10):**

| cs |  | l |
|---|---|---|
| qcaseq¯[1]of 0 call...,{ 1→qcase... → } |  |  |
|  |  |  |


**Table (Page 10):**

| s cs |  |  | l |
|---|---|---|---|
|  |  |  |  |
|  | qcaseq¯[2]of 0 skip; { 1→call... |  |  |


**Table (Page 10):**

| cs |  | cs c | s | l |
|---|---|---|---|---|
|  |  |  |  |  |
| skip; |  |  |  |  |


**Table (Page 10):**

| s c | s | l |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 11):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 11):**

|  |  y |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 11):**

|  |  |
|---|---|
|  |  |
|  |  |


**Table (Page 11):**

|  |  |
|---|---|
|  |  |
|  |  |


**Table (Page 11):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 11):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 11):**

|  |  |
|---|---|
|  |  |
|  |  |
|  |  |


**Table (Page 12):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | U |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 12):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 13):**

|  |  | Circuit complexity |  |
|---|---|---|---|
| Problem | Example | [17] | compile |
| Full Adder | Example 4 | Θ(n) | Θ(n) |
| Quantum Fourier Transform | Example 2 | Θ(n2) | Θ(n2) |
| k-Chained Substrings | Example 5 | Θ(n3k) | Θ(n) |
| Sum(r), r≥1 | Example 6 | Θ(nr) | Θ(n) |


**Table (Page 19):**

|  |  |  |  |
|---|---|---|---|
| cs S S | l |  |  |
| 1 2 |  |  |  |


**Table (Page 19):**

|  |  |  |
|---|---|---|
| cs S | cs S | l |
| 1 2 |  |  |


**Table (Page 19):**

|  |  |  |
|---|---|---|
| cs S | l |  |
| 1 |  |  |


**Table (Page 19):**

|  |  |  |
|---|---|---|
| cs proc’ | cs | l |


**Table (Page 19):**

|  |  |
|---|---|
| cs proc’ | c l |


**Table (Page 19):**

|  |  |  |  |
|---|---|---|---|
| proc’ | l |  |  |


**Table (Page 19):**

|  |  |  |
|---|---|---|
| cs l0 callproc’(s); |  |  |
|  | Sproc’ s/q¯ |  |
|  | { } |  |


**Table (Page 19):**

| cs | l0 Sproc’ s/q¯ |  |
|---|---|---|
|  |  |  |


**Table (Page 19):**

| l0 | cs | cs |  |
|---|---|---|---|
|  | proc’ |  |  |


**Table (Page 20):**

| L1 |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 20):**

| Lm |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
