---
title: "Multimodal Prompt Engineering"
original_file: "./Multimodal_Prompt_Engineering.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag", "evaluation", "multimodal"]
keywords: ["ris", "snn", "energy", "neuroris", "cid", "vol", "consumption", "where", "neuromorphic", "unit"]
summary: "<!-- Page 1 -->

1

### NeuroRIS: Neuromorphic-Inspired Metasurfaces

Christos G. Tsiftsis
Abstract—Reconfigurable intelligent surfaces (RISs) operate approachusingvaractordiodesandachievedcontinuousphase
similarly to electromagnetic (EM) mirrors and remarkably go shift,whichfurtherincreasedRIS efficiencyintuningtorapid
beyond Snell law to generate an applicable EM environment variations of the wireless environment. allowing for flexible adaptation and fostering sustainability in
From the contro"
related_documents: []
---

# Multimodal Prompt Engineering

<!-- Page 1 -->

1

### NeuroRIS: Neuromorphic-Inspired Metasurfaces

Christos G. Tsinos, Alexandros-Apostolos A. Boulogeorgos, and Theodoros A. Tsiftsis
Abstract—Reconfigurable intelligent surfaces (RISs) operate approachusingvaractordiodesandachievedcontinuousphase
similarly to electromagnetic (EM) mirrors and remarkably go shift,whichfurtherincreasedRIS efficiencyintuningtorapid
beyond Snell law to generate an applicable EM environment variations of the wireless environment.
allowing for flexible adaptation and fostering sustainability in
From the control unit point of view, several different comterms of economic deployment and energy efficiency. However,
puting architectures, including application-specific integrated
the conventional RIS is controlled through high-latency field
circuit (ASIC) low-power (LP) complementary metal-oxide
programmable gate array or micro-controller circuits usually
implementing artificial neural networks (ANNs) for tuning the semiconductor (CMOS) [4], ASIC CMOS [5], ASIC fin field-
RIS phase array that have also very high energy requirements. effect transistor (FinFET) CMOS [6], field programmable
Mostimportantly,conventionalRISareunabletofunctionunder gate array (FPGA) [7], computing processing unit (CPU) [8],
realisticscenariosi.e,high-mobility/low-enduserequipment(UE). and graphical processing unit (GPU) [9], were employed.
In this paper, we benefit from the advanced computing power of However, the aforementioned architectures either experience
neuromorphic processors and design a new type of RIS named highresponsetime,i.e.,intheordersofµstoms,orhavedra-
NeuroRIS, to supporting high mobility UEs through real time
matically high power consumption that may even reach some
adaptation to the ever-changing wireless channel conditions. To
hundreds Watts. Fortunately, a new brain-inspired architecture
thisend,theneuromorphicprocessingunittunesalltheRISmetawasveryrecentlydeveloped,namelyneuromorphiccomputing
elementsintheordersofnsforparticularswitchingcircuitse.g.,
architecture.Accordingto[10]–[12],neuromoprhiccomputing
varactors while exhibiting significantly low energy requirements
since it is based on event-driven processing through spiking processing can achieve significantly low response time, which
neural networks for accurate and efficient phase-shift vector is in the orders of some ns, while their power consumption is
design. Numerical results show that the NeuroRIS achieves very in the order mW.
close rate performance to a conventional RIS-based on ANNs, Despite the important role that brain-inspired architectures
while requiring significantly reduced energy consumption with
can play when integrated in RIS as control units, to the best
the latter.
oftheauthors’knowledgenopublishedcontributionaddresses
Keywords—Spiking neural network (SNN), event-driven, neuro- the topic of designing neuromorphic computing controlled
morphic processing, reconfigurable intelligent surface (RIS). intelligent metasurfaces. A possible reason behind this is that
in order to make the most out of the neuromoprhic computing
I. INTRODUCTION architecture, the conventional methods that are used for beam
RECONFIGURABLE intelligent surfaces (RISs) operate design and beam tracking should be rethought and redesigned
like electromagnetic mirrors that go beyond the conven- to following the spiking neural networks (SNNs) approach.
tional Snell law in order to create a beneficial propagation Motivated by the practical limitations of nowadays convenenvironment with unprecedented excellence in terms of re- tional RISs, the advancements in computing architecture, as
liability, energy and resource efficiency. However, nowadays well as the need of developing a new type of methods for
RIS-enabled wireless systems are unable to support realistic RIS beamforming vector design, in this letter, we present the
wireless networks with mobile user equipment (UE), while following technical contributions:
ensuring low computational power consumption, due to the
• We introduce a new-type of RIS, named NeuroRIS,
high latency of their control units and switching circuits [1].
which uses varactors as the basis of the switching

### Recognizingtheaforementionedproblem,theauthorsof[2]

circuit in order to ensure continuous phase shift, and
replaced the low-response time PIN diodes of the switching
neuromophic computing processor as a control unit to
circuit with varactor diodes. Interesting, this change reduced
importantly reduce the RIS response time, while boostthe response time of the switching circuit from some µs to
ing the processing energy efficiency.
ns [1]. Inspired by this, the authors of [3] followed a similar
• Building upon the NeuroRIS particularities, we formulateandsolveasignal-to-noise-ratio(SNR)optimization
C. G. Tsinos is with the National and Kapodistrian University of Athens,
Greece(e-mail:ctsinos@uoa.gr). problem that returns the optimal beamforming trans-
A.-A.A.BoulogeorgosiswiththeDepartmentofElectricalandComputer mission and RIS phase shift vectors. To address the
Engineering,UniversityofWesternMacedonia,50100Kozani,Greece(e-mail: problem, an unsupervised learning-based SNN method
al.boulogeorgos@ieee.org).
is employed that make the most out of the NeuroRIS
T.A.TsiftsisiswiththeDepartmentofInformatics&Telecommunications,
UniversityofThessaly,35100Lamia,Greece(e-mail:tsiftsis@uth.gr). architecture.
The work of A.-A. A. Boulogeorgos was supported by MINOAS. The • Finally, simulation results that highlight the superiority
research project MINOAS is implemented in the framework of H.F.R.I call
of the NeuroRIS in comparison with conventional RIS,
“Basic research Financing (Horizontal support of all Sciences)” under the
in terms of computational energy efficiency and latency
NationalRecoveryandResiliencePlan“Greece2.0”fundedbytheEuropean
Union–NextGenerationEU(H.F.R.I.ProjectNumber:15857). are presented.
3202
ceD
22
]YS.ssee[
1v84541.2132:viXra

<!-- Page 2 -->

2
Neuromorphic Reconfigurable Intelligent Surface as the weighted sum of spikes generated by the neurons of
(Neuro-RIS) the (l−1)th layer, w j,k,l ∈R are the corresponding weights,

### Switching Mechanism

Hardware components & o denotes the spiking binary output of the jth neuron
wiring j,l−1[t]
Exciting reflecting meta- of the (l−1)th layer at the simulation timestep t, and Θ(·) is

### Elements

Neuromorphic Processor Switching Circuit Board U ... nit cell tuning the Heaviside step function, defined as

### Tunable Meta-Elements RIS Tunable Layer (cid:26) 1 x≥0

P C va a o r s n a s t c i i n t v o u e r o s e u le s m co e n n t t r s ol by Θ(x)= 0 x<0 (2)

### TheLIFneuronworksasfollows:Whenthegiventhreshold

ω is exceeded by its membrane potential, the neuron fire a
t
Fig. 1: NeuroRIS architecture. spike and the membrane potential is reset to a predetermined
valueω .Throughthesimulationwindow1≤t≤T thespike
r
sequences are generated based on the timesteps that the LIF
neurons fire. Based on (1), in the present paper we assume

## Ii. Neurorisarchitecture

that ω =0 without loss of the generality.
r

### The RIS metasurface consists of N unit cells that each one

employ at least one switching circuit. PIN diodes and liquid III. SYSTEMMODEL
crystalswitchingcircuitssupportdiscretephaseshiftandhave
Let us consider the downlink scenario of a system constia response time in the orders of µs and ms [13], respectively.
tuted by a base station (BS) equipped with M antennas, a
On the other hand, varactor diodes support both discrete and
RIS equipped with N unit cells and a single antenna UE, as
continuous phase shift [3] and has a response time in the
shown in Fig. 1. The phase of the unit cells can be adaptive
ordersofns.TheswitchingcircuitoftheRISisresponsiblefor
adjusted by a neuromorphic controller that interconnects the
changing the state of each RIS unit. Each circuit is connected

### BSandRISunit.Theneuromorphiccontrollerisequippedwith

to a micro-controller that is designed according to the ASIC
a neuromorphic processor capable of optimizing the unit cell

### LP CMOS [4], ASIC CMOS [5], ASIC FinFET CMOS [6],

phases via applying learning mechanisms over SNNs. Also, it

### FPGA [7], CPU [8], or GPU [9] principles. Excluding the

coordinates the switching between the channel estimation and
ASIC FinFET CMOS, all the other ASIC architectures have
signal reflection modes.
a response time in the orders of µs and a power consumption

### Let us assume that there are direct transmission paths

in the orders of several decades of mW [14], [15]. The ASIC
between the BS and the UE, the BS-RIS and RIS-UE. Then,
FinFETCMOSarchitectureshaveasimilarresponsetimewith
the baseband received signal can be obtained as
a power consumption in the range of some W [16]. Most
FPGAs support response times in the order of µs, with power y =(GUf +h)Tws+z, (3)
consumption that reach 10.5W [17]. Although, CPUs and where w CM is the transmit beamforming vector, applied at
∈
GPUs provide ns response times, their power consumption the BS side that satisfies a total transmit power constraint,
even reach hundreds of W. Note that the coherence time of i.e., ∥w∥2 ≤ P , where P is the maximum supported
max max
millimeter wave and THz wireless channels is in the orders of transmit power, h ∈ CM is the vector with the fading
some µs [18]; thus, the RIS adaptation to the ever changing coefficientsofthechannelbetweentheBSandtheUE,f ∈CN
channel conditions should be in the orders of some ns. is the channel vector between the RIS component and the
As illustrated in Fig. 1, to ensure a latency in the order UE, G ∈ CM×N channel matrix between the BS and the
of some ns, while minimizing the power consumption of the RIS and z ∈ C is a white complex Gaussian variable with
control unit, NeuroRIS employs brain-inspired neuromorphic variance σ2. It also holds that E{|s|2} = 1. Furthermore, all
z
computingprocessorsforcalculatingitsoptimalphase-shifting thechannelsareassumedtobefrequencyflat-fadingones.The
weights through the solution of in general difficult nonconvex involved channel coefficients can be estimated via different
optimization problems. Such processors have a significantly methods as shown in []. In addition, U = diag{u}, where
lower power consumption, while their operation frequency is u = [u ,...,u ]T ∈ UN and U denotes the set of unit-

## 1 N

in the order to some GHz. In more detail, the neuromorphic modulus complex numbers, i.e., U ={u∈C| |u|=1}.
processor performs all the machine learning (ML)-related Following theabove system model description,the received
calculations through SNNs. The discrete leaky integrate and SNR ratio at the UE is given by
fire (LIF) neuron model proposed in [19] is adopted for the
1 1
stimulation of the membrane potential change. For a N L layer γ = |(UΘf +h)Tw|2 = |(Qu+h)Tw|2, (4)
SNNhavingN l ,1≤l≤Lneuronsperlayer,thedynamicsof σ z 2 σ z 2
the (k,l)th neuron, 1≤k ≤N L are given via the discretized where Q ∈ CM×N is defined as Q =
differential equation, given by
[f G ,f G ,...,f G ], f is the nth element in
1 1 2 2 N N n
ω k,l [t+1]=βω k,l [t]+I k,l [t]−βΘ(ω k,l [t]−ω thr ), (1) and G n is the nth column of G.

### Our aim is to derive the optimal transmit beamforming

where ω k,l [t] is the membrane potential of the (k,l)th neuron, vector w of the BS and the optimal RIS phase shifts such that
at the simulation timestep t, 1 ≤ t ≤ T, β is a decay factor, the UE’s receive SNR is maximized in terms of BS transmit

### I [t] =

(cid:80)Nl−1w
o [t] is the input current calculated power and the unit-modulus constraints at RIS. To that end,
k,l j=1 j,k,l j,l−1

<!-- Page 3 -->

3
the following optimization problem is formulated: where the That is the probability of generating a spike event is proporcovariance matrix Q is defined as tional to the values of v˜.
l
1

### P : max |(Qu+h)Tw|2 (5a)

1 w,u 2 B. Decoding Scheme
s.t. ∥w∥2 ≤P (5b) The generated spiking sequence of T time-steps is fed as
max
input to the SNN and excites the neurons of the network
u∈UN. (5c)
resultinginaspikingsequence attheoutput.Theoutputspike
Problem P is nonconvex due to the coupling of the w and sequence is then converted in real numbers that lie in [0,1] by
1
u variables and the nonconvex unit-modulus constraints on θ. counting mean fire rating rates of the output layer, that is
If we assume that u is given, the optimal solution for w is

## T

g √ iv P en by (Q th u e +h m )H ax . im B u y m pl t u ra g n g s in m g is i s n io to n t r h a e tio ob m je e c t t h i o v d e , f i u .e n . c , t w ion ⋆ T o = f θ˜= T 1 (cid:88) o K (t), (9)
max ∥Qu+h∥ j=1
P , the aforementioned equivalent form, we get an equivalent
1
where o is the N ×1 output spike vector of the SNN’s last
form given by K
layer at time index. Note that the output layer is of size N
1
P : max ∥Qu+h∥2 s.t. u∈UN. (6) and each one of the output neurons correspond to the phase
2 u 2 shift for the nth element in the RIS-array. Since, the entries
Problem P is also nonconvex since the optimal u still lies of θ˜lie in [0,1], a linear transformation is applied in order to
2
in the set of unit-modulus complex numbers. Even though, calculate the actual phases that lie in [0,2π], i.e., θ = 2πθ˜.
P is a relative simpler problem than P since it avoids the Then, the beamforming vector entries are calculated as
2 1
couplingofthewanduvariablesin,itsnowconvex,objective
function,itbelongstoclassofNP-hardproblems,andthusitis
uˆ
n
=ejθn =cos(θ
n
)+jsin(θ
n
), (10)
difficulttoaddress.Tothatend,wewillemployaunsupervised
where uˆ and θ are the nth entries of uˆ and θ, respectively,
n n
learning-based approach based on SNNs.
uˆ is the N × 1 vector of the estimated RIS beamforming
coefficients and 1 ≤ n ≤ N. It is evident that by carefully

## Iv. Unsupervisedlearning-Basedsolutionsnns

setting the loss function and the training procedure, the SNN

### In this section the SNN-based framework for solving P is

2 will be able to calculate RIS beamforming vectors u that
presented.AsSNNscanonlyprocessspikesequences,wefirst
solve P .
introduce a transformation from the feature space to the one 2
ofspikesequencesi.e.,thecodingscheme.Thecorresponding

### C. Loss Function

inverse transformation from the spike sequence space to the
one of unit-modulus beamforming vectors is then given, i.e., The loss function used to train the network is based on
the decoding scheme. Then, the loss function, the network problem P 2 ’s objective function, i.e.,
architecture and the the training procedure is presented in the
subsequent subsections. L=− 1 (cid:88) K (cid:13) (cid:13)Q˜ u˜ +h˜ (cid:13) (cid:13) 2 , (11)
2K (cid:13) k k k(cid:13)

### A. Coding Scheme k=1

FromtheobjectivefunctioninP 2 ,onemayseethattheCSI where K is the batch size, Q˜ = (cid:20) R{Q k } −I{Q k } (cid:21) ,
relatedmatrixQandCSIvectorharesuitableforconstructing k I{Q } R{Q }
k k
the feature vector for the considered SNN. To that end, we u˜ = [R{uˆ },I{uˆ }]T, h˜ = [R{h },I{h }]T, Q and
define the feature space vector v∈R2(NM+M) given by k k k k k k k
h are the CSI related matrices Q and h for the kth training
k
v=[R{qT},I{qT},R{hT},I{hT}]T, (7) sample and uˆ k can be calculated as in (10). From and the
considered decoding scheme in Sec. IV-B, it is clear that the
where q=vec{Q}. SNN calculates a vector uˆ that lies in the feasible solution
k
Now the input data in v should be transformed to spike
set of P and maximizes its objective function.
2
sequences prior fed to the SNN via a coding scheme. Among
the different tested coding schemes in the literature we opt

### D. Network Architecture

for the rate coding one due to its simplicity and robustness
to noise [19]. At first, the entries of v are mapped to [0,1] TheemployedSNNarchitectureisshowninFig.2.Atfirst,
by applying a non-linear transformation through the sigmoid the input feature vector v is fed in on the encoder and the
function v˜ = 1/(1+exp(v )), 1 ≤ l ≤ 2(NM +M) and generated spike sequences are then led to the SNN network,
l l
v is the lth entry of v. Then, spike generator based on the constituted by five layers of 32N, 16N, 8N, 4N and N LIF
l
Bernoulli distribution is employed. In more detail, the spiking neurons, respectively. Following such an approach, it assures
sequence entry r ,1 ≤ t ≤ T that corresponds to the feature that the SNN network has the adequate learning capabilities
lt
entry v˜,1 ≤ l ≤ L presents a spike event at time index j as the NeuroRIS size N scales. Then, the output is used to
l
(r =1) based on the probability calculate the mean fire rate via (9) that is subsequently used
lt
bythedecodertopredicttheoptimalphaseshiftsandevaluate
P(r lj =1)=v˜ l =1−P(r lj =0). (8) the SNN performance through the loss function in (11).

<!-- Page 4 -->

4
10
Input: Feature Vector v Input: Feature Vector v 9
8
Encoder Fully Conn R e E c L t U ed 1, 32xN 7
6
LIF 1, 32xN Batch Normalization 1 5
Fully Connected 2, 16xN 4

### LIF 2, 16xN RELU 3

Batch Normalization 2 2

### LIF 3, 8xN 1

Fully Connected 3, 8xN 0 RELU -20 -15 -10 -5 0 5 10 15 20
Transmit SNR (dB) LIF 4, 4xN

### Batch Normalization 3

LIF 5, N Fully Connected 4, 4xN

## Relu

Output: Mean Fire Rate Batch Normalization 4
Fully Connected 5, N

### Decoder Linear

N Phase-shifts Output: N Phase-shifts
(a) (b)
Fig. 2: Network Architectures for a) SNN, and b) ANN.

### E. Training Procedure


### The training procedure of a SNN is not a straightforward

task. Observe that from (1), the SNN resembles the structure
of a recursive neural network. Hence, the loss function value
at time t is dependent on the past values t′ of the learning
parameters, i.e., ∀t′ ≤ t. Thus, a generalized version of the
backpropagation algorithm has to be applied for the update of
the learning parameters that also captures the aforementioned
temporal dependence, i.e. , backpropagation through time
(BPTT) [20]- [21]. The BPTT method employs a stochastic
gradient descent for updating the learning parameters. The
partial derivative of the loss function with respect to the w i,k,l
learning parameter is given by:
∂L = (cid:88) T (cid:88) t ∂L[t] ∂w i,k,l [t′]
∂w ∂w [t′] ∂w [t] i,k,l i,k,l i,k,l
t=0t′=0
= (cid:88) T (cid:88) t ∂L[t] ∂Θ[t] ∂ω k,l [t] ∂ω k,l [t′] , (12)
∂Θ[t]∂ω [t]∂ω [t′]∂w [t′]
k,l k,l i,k,l
t=0t′=0
where Θ[t]≜Θ(ω [t]−ω ). In (12), the term ∂Θ[t] is
k,l thres ∂ωk,l[t]
the Dirac Delta function which is 0 everywhere apart from
the point ω [t] = ω where it tends to infinity. This
k,l thres
results in a gradient almost always set to 0 or saturated when
the threshold is reached. Thus, no weight updates can be
performed through the stochastic gradient descent method.
This is known as the so-called “dead neuron problem” [19].
This issue can be treated by the surrogate gradient approach
thatkeepstheHeavisidefunctionduringthenetwork’sforward
pass phase and for the backward pass phase, Θ[t] is smoothed
withthearctangentfunction.Thus,theterm ∂Θ[t] isreplaced
∂ωk,l[t]
by ∂Θ˜[t] = 1 .Byusingtheterm ∂Θ˜[t] inplaceof
∂ωk,l[t] π+ω k 2 ,l [t]π3 ∂ωk,l[t]
∂Θ[t] during the BPTT procedure, the dead neuron problem
∂ωk,l[t]
is avoided while the SNN’s performance is not affected since
neural networks are in general robust to such approximations.
The weight update procedure is iteratively executed for a pre-
)zH/s/stib(
etaR
102
101
100
A SN N N N , , N N = = 6 6 4 4 10-1

## Ann, N=32 Snn, N=32


## Ann, N=16 Snn, N=16 10-2 Ann, N=8


## Snn, N=8

10-3 8 16 32 64

## N


## )J(

ygrenE
egarevA

## Snn Ann

(a) (b)
Fig. 3: a) Impact of the NeuroRIS size N on the rate performance for a BS serving M =2 users, and b) Average energy
consumption of ANN and SNN versus N.
determinednumberofepochsperbatchofdata.Sincetheloss
function in (11) is directly used on the training procedure for
evaluating the SNN’s performance without generating labeled
data, the described learning method is an unsupervised one.

## V. Numericalresults

This section focuses on presenting numerical results that
quantify the efficiency of the Neuro-RIS and compares its
energy and data-rate performance to the corresponding performance of a conventional RIS. In more detail, the scenario in [22] is considered where all the channel coefficients follow the Rayleigh model with path loss given by
20.4 log (d/d )dB, where d is the distance between the 10 ref
transmitter and the receiver in meters and d = 1. The ref
distances between BS-UE and RIS-UE can be calculated as
(cid:112) (cid:112)
d = d2+d2 and d = d2 −d2 where d is the BU 0 1 RU BR 0 BR
distancebetweentheBSandtheRIS,d istheverticaldistance 1
fromtheUTtothehorizontalconnectionlineoftheBSandthe
RISandd isthedistancefromtheBStotheintersection.The
0
presented numerical results where generated with d =8m BR
and d and d following the uniform distribution in [0,8] and 0 1
[1,6], respectively. The Adam optimizer with a learning rate
set to 10−5 and momentum parameters set to {0.9,0.99} is
employed for training the SNN [23]. The simulation window
size is set to T =25 and parameter β in (1) is set to 0.99. A
number of 105 samples are used to train the SNN with batch
size equal to K = 100 for 30 epochs. The presented results
are generated from 104 test samples.
Fig. 3a depicts the rate performance of the Neuro-RIS employingSNNtoperformjointtransmissionandreflectionbeam
design in terms of data rate as a function of the transmit SN
fordifferentnumberofRISunit-cells.Therateiscalculatedas
r =log (1+γ)whereγ iscalculatedasin(4).Asbenchmark,
2
thecorrespondingperformanceoftheconventional-RIS,which
usesANNforjointtransmissionandreflectionbeamdesign,is
considered. The ANN network used in the simulation follows
the approach in [24] and it is shown in Fig. 2b. As expected,
for given N and type of RIS, as the transmit SNR increases,
the data rate also increases. For example, for N = 64, when
a NeuroRIS is employed, the data doubles as the transmission

### SNR increases from −20 to −5dB. Moreover, for fixed

transmission SNR and type of RIS, as N increases, the data
rate increases. For instance, in case a NeuroRIS is used, and

<!-- Page 5 -->

5
a transmission SNR equal to −15dB, the data rate increases [4] H.Sarieddeen,M.-S.Alouini,andT.Y.Al-Naffouri,“Anoverviewof
by about four times, as N increases from 8 to 64. Finally, signal processing techniques for terahertz communications,” Proceedwe observe that the NeuroRIS and conventional RIS achieve ingsoftheIEEE,vol.109,no.10,pp.1628–1665,2021.
the same results in terms of data rate. Fig. 3b illustrates the [5] L. Petrou et al., “The first family of application-specific integrated
circuits for programmable and reconfigurable metasurfaces,” Scientific
average energy consumption of the RIS micro-controller as a
Reports,vol.12,no.1,Apr.2022.
functionofN,assumingthatthetransmissionSNRisequalto
[6] S.Amakawaetal.,“WhitePaperonRFenabling6G–opportunitiesand
0dB.Theenergyconsumptioniscalculatedbymultiplyingthe
challengesfromtechnologytospectrum,”p.68,2021.
floating-pointoperations(FLOPS)numberbytheirenergycost
[7] X.Peietal.,“RIS-aidedwirelesscommunications:Prototyping,adapand then summing over the network’s layers. In the present tive beamforming, and indoor/outdoor field trials,” IEEE Trans. Compaper, we rely on the results in [25] for the energy cost mun.,vol.69,no.12,pp.8627–8640,2021.
per operation. There the energy cost per multiplication and [8] M. Usman et al., “Intelligent wireless walls for contactless in-home
addition in a 45nm chip operated at 0.9V that implements a monitoring,” Light: Science & amp; Applications, vol. 11, no. 1, Jul.
2022.
32-bit architecture is given as 3.7pJ and 0.9pJ, respectively.
As expected, for a given micro-controller, as N increases, [9] Y. Dai et al., “Reconfigurable intelligent surface for low-latency edge
computingin6G,”IEEEWirelessCommun.,vol.28,no.6,pp.72–79,
the average energy consumption increases. For NeuroRIS, as
2021.

### N increases from 8 to 64, the average energy consumption

[10] M. Isik, “A survey of spiking neural network accelerator on FPGA,”
increases from 3×10−3 to 3×10−2µJ. On the contrary, if a 2023,arXiv:2307.03910.
conventionalRISisused,forthesameN increase,theaverage [11] B. Rajendran et al., “Low-power neuromorphic hardware for signal
energy consumption increases from 0.2 to 20µJ. Meanwhile, processing applications: A review of architectural and system-level
for the same N, an important energy consumption reduction design approaches,” IEEE Signal Process. Mag., vol. 36, no. 6, pp.
is observed, when neuromorphic computing processor is used 97–110,2019.
instead of a conventional micro-controller. For instance, for [12] M. Davies et al., “Advancing neuromorphic computing with Loihi: A
surveyofresultsandoutlook,”ProceedingsoftheIEEE,vol.109,no.5,
N =64,usingNeuroRISinsteadofconventionalRIScausean
pp.911–934,2021.
energyconsumptionreductionofabout3ordersofmagnitudes.
[13] R.Guiradoetal.,“mm-wavemetasurfaceunitcellsachievingmillisec-
This is the case since the SNNs networks are performing ond response through polymer network liquid crystals,” IEEE Access,
mainlyACoperationswhichconsumemuchlowerenergythat vol.10,pp.127928–127938,2022.
the MAC operations that are the core of ANNs. Furthermore, [14] J. Park, J. Lee, and D. Jeon, “7.6 a 65 nm 236.5 nj/classification
due to the sparsity of the spike events, the AC operations neuromorphic processor with 7.5% energy overhead on-chip learning
in SNNs are much less than the MAC ones in the ANNs. using direct spike-only feedback,” in IEEE International Solid-State
CircuitsConference-(ISSCC),2019,pp.140–142.

### Notice that as demonstrated in Fig. 3a, NeuroRIS and con-

[15] F.N.Buhleretal.,“A3.43TOPS/W48.9pJ/pixel50.1nJ/classification
ventional RIS achieve almost identical performance for the
512analogneuronsparsecodingneuralnetworkwithon-chiplearning
same transmission SNR and N. Hence, the use of NeuroRIS and classification in 40 nm CMOS,” in 2017 Symposium on VLSI
insteadofconventional-RISresultstoanunprecedentedenergy Circuits,2017,pp.C30–C31.
efficiency enhancement. [16] G.Chenetal.,“A4096-neuron1M-synapse3.8-pJ/SOPspikingneural
network with on-chip STDP learning and sparse weights in 10-nm
VI. CONCLUSION FinFETCMOS,”IEEEJ.Solid-StateCircuits,vol.54,no.4,pp.992–
1002,2019.

### In this paper, we introduced a novel RIS paradigm by

[17] S. Yang et al., “Real-time neuromorphic system for large-scale
exploiting the high energy efficiency of neuromorphic procesconductance-based spiking neural networks,” IEEE Trans. Cyber.,
sors. NeuroRIS significantly outperform conventional RIS in
vol.49,no.7,pp.2490–2503,2019.
terms of energy efficiency with same data rate performance.
[18] C. Han et al., “Terahertz wireless channels: A holistic survey on
To highlight the important performance gains of NeuroRIS measurement, modeling, and analysis,” IEEE Commun. Surveys Tuts.,
compared to conventional RISs, we formulated a joint trans- vol.24,no.3,pp.1670–1707,2022.
mission beam and RIS phase shift optimization problem that [19] J. Eshraghian et al., “Training spiking neural networks using lessons
maximizesthereceivedSNR,andwesolveditbyusingSNNs. from deep learning,” Proceedings of the IEEE, vol. 111, no. 9, pp.
1016–1054,2023.

### Asabenchmark,weusetheANNcorrespondingsolution.Our

[20] S.B.ShresthaandG.Orchard,“Slayer:Spikelayererrorreassignment
results revealed the correctness of our hypothesis, i.e., that
intime,”Advancesneuralinf.process.syst.,vol.31,2018.
NeuroRIS is a remarkable energy efficient solution leading to
[21] D. Huh and T. J. Sejnowski, “Gradient descent for spiking neural
important energy saving, especially in large RIS utilizations.
networks,”Advancesneuralinf.process.syst.,vol.31,2018.
[22] C.Huang et al., “Indoor signal focusing with deep learning designed
REFERENCES reconfigurable intelligent surfaces,” in IEEE Int. Workshop Signal
process.advancesWirelessCommun.(SPAWC). IEEE,2019,pp.1–5.
[1] B. Rana, S.-S. Cho, and I.-P. Hong, “Review paper on hardware of
[23] D.P.KingmaandJ.Ba,“Adam:Amethodforstochasticoptimization,”
reconfigurableintelligentsurfaces,”IEEEAccess,vol.11,pp.29614–
arXivpreprintarXiv:1412.6980,2014.
29634,2023.
[24] J. Gao, C. Zhong, X. Chen, H. Lin, and Z. Zhang, “Unsupervised
[2] D. Sievenpiper et al., “Two-dimensional beam steering using an eleclearningforpassivebeamforming,”IEEECommun.Lett.,vol.24,no.5,
trically tunable impedance surface,” IEEE Trans. Antennas Propag.,
pp.1052–1056,2020.
vol.51,no.10,pp.2713–2722,2003.
[25] M. Horowitz, “1.1 computing’s energy problem (and what we can do
[3] R. Fara et al., “A prototype of reconfigurable intelligent surface with
about it),” in IEEE Int. Solid-State Circuits Conf. Dig. Tech. Papers
continuous control of the reflection phase,” IEEE Wireless Commun.,
(ISSCC),2014,pp.10–14.
vol.29,no.1,pp.70–77,2022.

## Tables

**Table (Page 2):**

| Tunable Meta-Elements |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
