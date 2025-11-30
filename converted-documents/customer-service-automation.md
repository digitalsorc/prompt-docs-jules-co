---
title: "Customer Service Automation"
original_file: "./Customer_Service_Automation.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag", "agents", "fine-tuning", "evaluation"]
keywords: ["cid", "connectivity", "multi", "dbss", "conn", "performance", "ieee", "probability", "coverage", "communication"]
summary: "<!-- Page 1 -->

1
Performance Analysis for Downlink Transmission
in Multi-Connectivity Cellular V2X Networks
Luofang Jiao, Member, IEEE, Jiwei Zhao, Member, IEEE, Yunting Xu, Member, IEEE, Tianqi Zhang, Member,
IEEE, Haibo Zhou, Senior Member, IEEE and Dongmei Zhao, Senior Member, IEEE
Abstract—Withtheever-increasingnumberofconnectedvehi- other network entities such as base stations (BS), roadside
clesinthefifth-generationmobilecommunicationnetworks(5G) units,pedestrians,andcloudservers(V2I)[4]"
related_documents: []
---

# Customer Service Automation

<!-- Page 1 -->

1
Performance Analysis for Downlink Transmission
in Multi-Connectivity Cellular V2X Networks
Luofang Jiao, Member, IEEE, Jiwei Zhao, Member, IEEE, Yunting Xu, Member, IEEE, Tianqi Zhang, Member,
IEEE, Haibo Zhou, Senior Member, IEEE and Dongmei Zhao, Senior Member, IEEE
Abstract—Withtheever-increasingnumberofconnectedvehi- other network entities such as base stations (BS), roadside
clesinthefifth-generationmobilecommunicationnetworks(5G) units,pedestrians,andcloudservers(V2I)[4].Thistechnology
and beyond 5G (B5G), ensuring the reliability and high-speed
aims to enhance the efficiency and safety of vehicular traffic
demandofcellularvehicle-to-everything(C-V2X)communication
while enabling various applications such as collision avoidin scenarios where vehicles are moving at high speeds poses a
significantchallenge.Recently,multi-connectivitytechnologyhas ance,trafficmanagement,cooperativedriving,platooning,and
becomeapromisingnetworkaccessparadigmforimprovingnet- autonomous driving, that require high-speed and low-latency
workperformanceandreliabilityforC-V2Xinthe5GandB5G communication in ITS [5], [6]. However, as the number of
era. To this end, this paper proposes an analytical framework
connected vehicles continues to increase, C-V2X is rapidly
for the performance of downlink in multi-connectivity C-V2X
developing towards ultra-dense, whcih poses challenges such
networks.Specifically,bymodelingthevehiclesandbasestations
as one-dimensional Poisson point processes, we first derive and as interference management, security, and energy efficiency,
analyzethejointdistancedistributionofmulti-connectivity.Then andrequirefurtherresearchanddevelopmenttoenablereliable
throughleveragingthetoolsofstochasticgeometry,thecoverage and efficient vehicular communication. C-V2X also faces sigprobability and spectral efficiency are obtained based on the
nificantchallengesduetothehigh-speedmobilityanddynamic
previous results for general multi-connectivity cases in C-V2X.
topologyofvehicles,whichmaycauserapidfluctuationsinthe
Additionally, we evaluate the effect of path loss exponent and
the density of downlink base station on system performance quality of wireless links, frequent handovers, and increased
indicators. We demonstrate through extensive Monte Carlo signaling overhead. These challenges is severely impacting
simulations that multi-connectivity technology can effectively the communication performance and influence the quality
enhance network performance in C-V2X. Our findings have
of experience (QoE) and quality of service (QoS) of ITS
importantimplicationsfortheresearchandapplicationofmultiapplications.
connectivity C-V2X in the 5G and B5G era.
In recent years, multi-connectivity technology has attracted

### IndexTerms—C-V2X,multi-connectivity,coverageprobability,

significant attention to address these aforementioned chalspectral efficiency, stochastic geometry.
lenges [7]. Multi-connectivity enables a vehicle to establish
multiple simultaneous connections with different BSs us-
I. INTRODUCTION ing various radio access technologies (RATs), access points
WITH the evolution of the fifth-generation mobile com- (APs), or channels, thus taking advantage of the diversity
and availability of wireless resources in the cellular network
munication networks (5G) and beyond 5G (B5G), re-
[3]. The multi-connectivity technology, as compared to the
liable and high-performance wireless communication systems
traditional point-to-point communication, offers substantial
have become essential to fully exploit the potential of intelliadvantages in terms of various communication performance
gent transportation systems (ITS) [1]–[3]. Cellular vehicle-tometrics, e.g., enhanced reliability [8], improved coverage [9],
everything (C-V2X) has emerged as a promising technology
and enabled seamless mobility and handover [10]. Through
that utilizes the existing cellular network infrastructure and
accessing multiple BSs, vehicles can switch between availspectrum to provide efficient and reliable communication
able connections without disrupting ongoing communication,
between vehicles (V2V), as well as between vehicles and
providinguninterruptedconnectivityevenwhenmovingacross
ThisworkissupportedinpartbytheNationalNaturalScienceFoundation network boundaries or transiting under different coverage of
Original Exploration Project of China under Grant 62250004, the National networks. In additions, based on the specific requirements
Natural Science Foundation of China under Grant 62271244, the Natural
of the application or user preferences, multi-connectivity is
Science Fund for Distinguished Young Scholars of Jiangsu Province under
Grant BK20220067, the High-level Innovation and Entrepreneurship Talent capable of offering flexibility for choosing the most suitable
IntroductionProgramTeamofJiangsuProvinceunderGrantJSSCTD202202. network connections and providing better spectral efficiency
L. Jiao, J. Zhao, Y. Xu, T, Zhang, and H. Zhou (Corresponding author)
by dynamic adaptation to changing network conditions [11].
are with the School of Electronic Science and Engineering, Nanjing
University, Nanjing 210023, China (e-mail: luofang jiao@smail.nju.edu.cn; Thus, applying multi-connectivity to C-V2X is of remarkable
jw zhao@smail.nju.edu.cn; yuntingxu@smail.nju.edu.cn; tian- significance for improving communication performance and
qizhang@smail.nju.edu.cn;haibozhou@nju.edu.cn).
makes it more suitable for ITS applications.
D. Zhao is with the Department of Electrical and Computer Engineering, McMaster University, Hamilton, ON L8S 4L, Canada (e-mail: In the context of multi-connectivity in C-V2X, coverage
dzhao@mcmaster.ca). probability and spectral efficiency are two important perfor-
Copyright (c) 2023 IEEE. Personal use of this material is permitted.
mance metrics for evaluating wireless communication system
However, permission to use this material for any other purposes must be
obtainedfromtheIEEEbysendingarequesttopubs-permissions@ieee.org. performance [9]. However, establishing a comprehensive ana-
4202
rpA
72
]PS.ssee[
1v32871.4042:viXra

<!-- Page 2 -->

2
lytical framework with regard to these performance metrics mance. Section IV conducts a performance analysis of the
is challenging and holds significant academic importance. system, including the joint distance distribution, coverage
following a spatial point process [12], [13]. System modeling probabilityandspectralefficiency.InSectionV,thesimulation
and analytical performance evaluation based on stochastic setup and results obtained from extensive Monte Carlo simgeometryhaveproventobeapowerfulmethodformonitoring ulations are presented, providing verification of the proposed
theeffectsofimportantsystemparametersaswellasoptimiz- framework and evaluation of the system performance. Section
ing system configurations, all without the need for compu- VI presents the concluding remarks of this paper.
tationally expensive and resource-intensive computer simulations [14]. Moreover, there is a research gap in the analysis

## Ii. Relatedwork

of uplink and downlink performance for multi-connectivity
C-V2X communication. While most of the existing studies The adoption of C-V2X has emerged as a critical network
primarilyfocusedontheuplinktransmissionandperformance paradigm for enabling vehicular communication with other
optimization [9], [15], the downlink transmission based on an vehicles and the infrastructure, offering diversified safety and
analytical framework has not been sufficiently explored. This efficiency applications for ITS [16]. However, despite of its
is a significant limitation since downlink transmission plays significant potential, the implementation of C-V2X communia crucial role in supporting various ITS applications that rely cation is confronted with numerous challenges, such as high
onreceivingdownlinkinformationfrominfrastructures.There- mobility,dynamictopology,heterogeneousnetwork,andstrinfore,conductingin-depthstudiesonthedownlinkperformance gent QoS requirements [12]. In high-speed C-V2X scenarios,
ofmulti-connectivityC-V2Xcommunicationissubstantialfor single connectivity with just one base station frequently leads
filling this existing gap and ensuring a holistic analysis of the tohandoverissues[7],[9],resultinginarapiddeclineincomsystem’s capabilities for supporting diverse ITS applications. munication speed and reliability, thus no longer meeting C-
Therefore, this paper considers multi-connectivity as an V2X’s QoS requirements. In recent years, multi-connectivity
effective solution to resolve the challenges faced by C-V2X has been considered to be a promising technology to tackle
communication,aimingtoenhancethecommunicationperfor- these challenges in C-V2X through enhancing reliability, remance for ITS applications. A feasible analytical framework ducing latency, and boosting overall network performance.
for downlink transmission in multi-connectivity C-V2X net- With multiple BSs access, multi-connectivity supports
works is proposed by modeling the vehicles and downlink seamless mobility and handover between different BS coverbase stations (DBSs) as one-dimensional (1-D) Poisson point age. Exploiting simultaneous connections, multi-connectivity
processes (PPPs), the tools of stochastic geometry are used to offersconsiderableavailabilityfortheimprovementofspectral
derive crucial performance indicators, including joint distance efficiency [17]. A number of studies have investigated the
distribution, coverage probability, and spectral efficiency. The potential benefits of applying multi-connectivity in C-V2X
key contributions of this paper are summarized below: and wireless networks. Numerous studies have delved into
the potential advantages of implementing multi-connectivity
• We present a novel multi-connectivity performance ana- within C-V2X and wireless networks. These investigations
lytical framework for C-V2X, which enables the evalucover various aspects, ranging from resource optimization in
ation of network performance in the 5G/B5G era. This
C-V2Xmulti-connectivitytoperformanceanalysesinwireless
frameworkprovidesafoundationforfurtherresearchand
networks.
potentialperformanceimprovementofmulti-connectivity
In the context of C-V2X, some studies concentrate on optitechnology in C-V2X systems.
mizing communication resources. Rabitsch et al. [8] explored
• Wederivepreciseexpressionsofcoverageprobabilityand multi-connectivity algorithms tailored to meet the stringent
spectral efficiency for general multi-connectivity cases in
requirements for communication availability and latency in
C-V2X based on the joint distance distribution. We also

### V2I networks. Lu et al. [7] introduced a novel approach

provide important insights into the design and optimizato reduce duplication rates in DBSs in fully-decoupled C-
tion of C-V2X networks by analyzing the effect of path
V2Xnetworks.Theyachievedthisbyformulatingandsolving
loss exponent and DBS density on system performance
optimizationproblemsusingLyapunovstochasticoptimization
indicators.
techniques to help vehicles select access BSs for multi-
• We conduct comprehensive Monte Carlo simulations connectivity and optimize bandwidth resources to meet user
to confirm the effectiveness of the presented multicommunication requirements. Kousaridas et al. [18] analyzed
connectivity performance analytical framework, which
multi-connectivitymanagementinaManhattanmodelforV2X
shows that multi-connectivity technology can significommunication.
cantly improve network performance in C-V2X. This
Other studies aim to evaluate the performance of multifinding has important implications for the practical apconnectivity in both wireless networks and C-V2X scenarplications of multi-connectivity C-V2X in the 5G/B5G
ios. Moltchanov et al. [19] provided a closed-form upper
era.
bound on the probability density function (PDF) for multi-
The subsequent sections of this paper are structured as connectivity, shedding light on its statistical characteristics.
follows. We briefly introduce the existing research works Weedage et al. [3] scrutinized the downlink performance of
related to our work in Section II. Section III presents the multi-connectivityinwirelessnetworks.Wuetal.[9]proposed
proposed framework for analyzing multi-connectivity perfor- a multi-connectivity scheme for uplink C-V2X communica-

<!-- Page 3 -->

3
tions, deriving precise expressions for the outage probability door communication systems using ultra-wideband terahertz
using stochastic geometry tools. (THz) technology, focusing on average ergodic capacity and
Numerous performance metrics have been employed in re- connectivitylikelihood.Chenetal.[12]employedcoordinated
searchworksthatexploretheapplicationofmulti-connectivity multipoint techniques to enhance spectral efficiency, while
technology in cellular communication scenarios. In 5G and Giordani et al. [22] and Kamble et al. [26] aimed to optibeyond 5G networks, Sylla et al. [20] provided a comparable mize the Signal-to-Interference-Plus-Noise Ratio (SINR) and
cellular communication analysis for multi-connectivity. Pupi- outage probability in single-frequency networks. Weedage et
ales et al. [2] focused on the multi-connectivity architectures al.[3]delvedintotheanalysisofchannelcapacityandoutage
and protocols for 5G network and they described the differ- probability in wireless networks’ downlink scenarios.
ent network entities and protocol layers involved in multiconnectivity, such as multi-connectivity coordinator, multiconnectivity agent, multi-connectivity manager and packet III. SYSTEMMODEL
data. Petrov et al. [21] studied the dynamic characteristics
When analyzing the overall performance of a multiof multi-connectivity technology, whereas Giordani et al. [22]
connectivity C-V2X network, a specific vehicle is considinvestigated its application in 5G mmWave cellular networks.
ered as a typical analysis object. Therefore, the multiple

### Inthispaper,wemainlyfocusontheperformanceindicator

roads model can still be simplified and analyzed as a single
of coverage probability and spectral efficiency based on disroad situation. Moreover, it has been proven that the single
tancedistribution.Coverageprobabilityandspectralefficiency
road model can effectively reflect the performance of multiaretwoofthemostimportantmetricsthatholdsignificancefor
connectivity in C-V2X [7], [9]. Therefore, to investigate the
evaluating the wireless networks. Firstly, coverage probability
downlink multi-connectivity in C-V2X scenario, we introduce
determines the reliability of C-V2X communication in differa simplified 1-D system model in this paper. A coordination
ent geographical areas and network densities [13]. By leverscheme called Single Frequency Networks (SFN) as in [27]
aging multi-connectivity technology, the coverage probability
are leveraged for spectrum allocation. SFN enables the transcan be improved and the risk of communication interruptions
missionofincoherentjointsignalsonthesameradioresources
can be reduced. With multiple connections simultaneously reinfrequencyandtime,whichrequiresBSstocoordinatewhen
ceiving and transmitting data, even if one connection encouncreating signals and to strictly synchronize their timing. Our
ters interruption issues, the others can maintain communicafocusinthispaperisontheintra-frequencymulti-connectivity,
tion,therebyenhancingoverallcoverageprobability.Secondly,
which requires simultaneous transmission of multiple DBSs
spectral efficiency is extremely crucial for the transmission
operating at the same carrier frequency to the same vehicle.
capacity of C-V2X. C-V2X communication involves handling
This is an important issue to address in the C-V2X scenario,
a substantial amount of traffic-related information, including
where high data rates and reliable communication are need
vehicle sensor data and traffic management instructions [23].
for safety-critical applications. The following of this section
Additional spectrum resources can be utilized in parallel or
introduces the channel model, association policy, interference
through multiplexing, thus improving spectral efficiency to
model, and performance metrics utilized in this study. Table I
support higher data transmission rates and faster response
lists the key symbols used throughout this paper.
times through multi-connectivity [24]. Further improvements

### A. Modeling of C-V2X Network

incoverageprobabilityandspectralefficiencycanbeachieved

### Fig.1showsthedownlinkmulti-connectivityscenarioinC-

by optimizing load balancing and resource allocation among

### V2X networks. The vehicles are randomly distributed on an

the connections. Research in this area is of paramount imporurban freeway segment, and the DBSs are densely distributed
tance to achieve efficient and reliable C-V2X communication,
alongtheroad.Tosimplifytheanalysis,wemaketheassumpproviding a more robust and efficient foundation for critical
tion that both the DBSs and vehicles utilize a single antenna,
applications such as real-time vehicle communication, traffic
and denote the height difference between the antenna of the
management, and vehicular safety in ITS.
DBS and the vehicle as h.

### To obtain the exact analytical expression of performance


### For the tractability of the downlink performance analysis,

metrics for multi-connectivity in C-V2X, leveraging the tools
we consider a 1-D scenario on a road including vehicles,
ofstochasticgeometryisregardedasanefficientapproachand
DBSs, and interference DBSs as shown in Fig. 1, as in [6],
ithasbeenincreasinglypopularinrecentyearsfortheperfor-
[9]. From a statistical perspective, the spatial distributions of
mance analysis in multi-connectivity scenarios. For instance,
vehiclesandDBSsconformto1-DPPPdistributions[13],and
Moltchanovetal.[19]wereamongthepioneersinderivingthe
we use the 1-D PPPs φ ,φ with density λ ,λ to denote
PDF for multi-connectivity, laying essential groundwork for V D v d
the locations of vehicles and DBSs on the road, respectively,
further investigations. Building upon this foundation, Kibria
where φ ,φ can be expressed as
et al. [25] assessed the viability of employing dual connec- V D
tivity and coordinated multiple points (CoMP) transmission φ = △(cid:8) x ∈R2 :i∈N (cid:9) ,j ={V,D}.
j i,j +
in wireless communication systems, expanding the scope of
multi-connectivity applications. AllofthevehiclesandDBSsaredistributedalongaroadwith
Moreover, the utilization of stochastic geometry in various length l. As per Slivnyak’s theorem, the distribution of point
multi-connectivity scenarios has witnessed extensive explo- processes remains unchanged even after adding a node at the
ration. Shafie et al. [24] explored multi-connectivity in in- origin [28], and in order not to lose generality and eliminate

<!-- Page 4 -->

4

## Tablei


## Alistofmajorsymbols


### Notation Description

λ;xi ThedensityofthevehiclesandDBSsona1-Droad;ThedistanceofithnearestDBStothetypicalvehicle.
P d;α d ThetransmitpowerofDBS;Thedownlinkpathlossexponentparameter.
g d;χ d ThechannelgainbetweentheDBSandvehicle;TheNakagami-mfadinggain.
τD ;µ Thespectralefficiencyofdownlink;Themeanofexponentialfunction.
ω d;δ
d
2 Themeanofthelogarithmofχ d;Thevarianceofthelogarithmofχ d.
φV,φD ThePoissonpointprocessesofvehiclesandDBSs.
φt ;t TheDBSssetafterbeingexecutedrandomdisplacement;Thepredeterminedthresholdtofcoverageprobability.

## D

φc;Θd

## I

ThecollaborativeDBSsetofmulti-connectivity;TheinterferenceDBSsetofmulti-connectivity.
I d;σ
d
2 Thereceivedinterferenceofthetypicalvehicle;Thenoiseofchannel.
E(·) Theexpectationofarandomvariable.
P(·) Theprobabilityofarandomvariable.
F(·) Thecumulativedistributionfunctionofarandomvariable.
f(·) Theprobabilitydensityfunctionofarandomvariable.
ζI(·) TheLaplacetransformofinterferenceI.
Γ(·) Thegammadistributionfunctionofarandomvariable.
represents the variance of the logarithm of χ [29]. Hence,

### Downlink d

2nd 2nd 3rd the received signal power of the typical vehicle from the i-th
DBS in the downlink is [30]

## Ddll Bbss


## P

r,v
(x
i

## )=P

d
g
d
χ
d
x
i
−αd, i∈φ

## D

, (3)
1st 3rd 1st where P d is the transmitting power of the DBS and assumed
to be the same for all DBSs.

### Interference Downlink


### Base Station Interference

Fig. 1. An example of a practical 1-D scenario for downlink transmission B. Association policy
inmulti-connectivityC-V2Xisillustrated.Inthisscenario,thetargetvehicle
receives messages from the three closest DBSs, while transmissions from Thetypicalvehicleisassumedtobeconnectedtonnearest
DBSs located beyond the collaboration distance can lead to interference to
DBSs by measuring all the receiving power from the nearby
thetargetvehicle.

### DBSs, finding the DBSs with the maximum receiving power

(MRP) in turn [9]. Since the received power P is not exr,v
segmentation due to boundary effects, we place the typical ponentially distributed for the modeling of the shadow fading
vehicle at the origin v = (0,0), i.e. which represents the [16],thelemmaofrandomdisplacementtheoremisconsidered
o
center of the road [9]. tosolvethisissue[31].Thus,P
r,v
(x
i

## )=P

d
g
d
χ
d
x
i
−αd canbe
eac

## I

h
n
v
re
e
l
h
a
i
t
c
io
le
n
is
to
co
th
n
e
ne
f
c
o
t
r
e
m
d
a
t
t
o
io
t
n
he
o
n
f v
n
i
e
r
a
tu
re
a
s
l
t
c

## D

el

## B

ls

## S

,
s
w
o
e
n
a
a
s

## E

su
u
m
cl
e
id
t
e
h
a
a
n
t transformed to P
r,v
(y
i

## ) = P

d
g
d
y
i
−αd, where y
i
= χ
d
− α 1 dx
i
.

### The 1-D PPP transformed converges to a 1-D homogeneous

plane. The 1-D distance between the typical vehicle v o with (cid:20) − 1 (cid:21)

### PPP and the intensity λ is transformed to E χ αd λ , and

thei-th(i≤n)DBSisr i ,thustheactualdistancex i between d d d
the transmit antenna of DBS to receive antenna of the typical (cid:20) − 2 (cid:21)
the intensity of the 2-D PPP is E χ αd λ after executvehicle is d d
(cid:113)
x = r2+h2. (1) ing the procedure of random displacement [13]. Specifically,
i i (cid:20) (cid:21)
− 1

### E χ αd λ can be calculated as


### We adopt a common power-law pathloss and Rayleigh d

fading model with a decay rate of x−αd, where x denotes the
distance between the DBS and the typical vehicle. The down- E (cid:20) χ − α 1 d (cid:21) λ =exp (cid:32) ω d ln10 + 1 (cid:18) σ d ln10 (cid:19)2 (cid:33) λ . (4)
link pathloss exponent parameter is denoted as α d (α d > 2). d d 10α d 2 10α d d
g is used to denote the power gain of Rayleigh fading and it
d
ismodeledbyanexponentialdistributionwithameanof1/µ. Then we use 1-D PPP φt to denote the transformed set of
g The i r s efore,wehaveg d ∼exp(µ).Thedistributionfunctionof DBS and λ D = E (cid:104) χ− α 1 d D(cid:105) λ d denotes the transformed DBS
d
intensity. To facilitate performance analysis in the following
f(g
d
)=µe−µgd. (2) sections,weusethesymbolφt

## D

,d todenotethesetofdistances
between the DBSs and the typical vehicle,
Furthermore, we use random variable χ to model the effects
d
of shadowing between the DBS and the typical vehicle in the φt,d ={x ,x ,...,x },i∈N , (5)

### D 1 2 i +

downlink, and χ follows a log-normal distribution given by
d
10log χ ∼ℵ
(cid:0)
ω
,δ2(cid:1)
, where ω represents the mean of the where x denotes the distance between the typical vehicle v
10 d d d d i o
logarithm of χ (i.e., the geometric mean of χ ), while δ2 and the i-th nearest DBS ∈ φt . Thus the candidate serving
d d d D

<!-- Page 5 -->

5
DBSs is changed to the n nearest DBSs ∈ φt in turn, and among all vehicles in the simulation scenario. Since

## D

this can be expressed as the cumulative distribution function (CDF) of SINR

## D

is P (t) = P(SINR <t), the coverage probability
x = argmax x−αd,i>m (6) cov D
i i can also be expressed as the complementary cumulative
xi∈φt

## D

,d\φd
c distributionfunction(CCDF)oftheSINR atthetypical

## D

where we use φd = {x ,x ,...,x } to denote the set vehicle from the DBSs.
c 1 2 m
of the distances between the connected collaborative DBSs • The spectral efficiency of the typical vehicle v o is the
and the typical vehcle v at the origin, m is the number of amount of data transmitted per unit of bandwidth [33].
o
DBSs that the typical vehicle has already connected to, and According to the Shannon Theory, the spectral efficiency
x ,i∈{m+1,m+2,···} denotes the distance between the of the downlink is
i
DBS outside φd and the typical vehicle. Let φ to denote the
c c τ =E[ln(1+SINR )], (10)
set of the connected collaborative DBSs. This means that to D D
expand the set φ c , we need to find the nearest DBS among where E(·) is the expectation function. The spectral
DBSs in φt D \φ c . efficiency describes the likelihood of a wireless communication system achieving a specific information amount
C. Interference withinacertaintimeperiodandspacerangeduringactual
use [23]. It can help evaluate the performance of C-
In the collaboration DBSs set φ , all DBSs will transmit
c

### V2X in a multi-connectivity environment and determine

the control and data signals simultaneously on the same
whether system optimization or adjustments are needed
subband [7]. Since the signal components of the DBSs are
[33].
withinthecyclicprefix,theresultingmulti-connectivitySINR
experienced by the typical vehicle v in the downlink is
o
defined as follows:

## Iv. Performanceanalysis

(cid:80) P g x−αd We first derive the expression for the joint distance disd d i

## Sinr =

i∈φc
, (7)
tribution from x
1
to x
n
in this section. To optimize system
D I D +σ d 2 configurations without the need for time-consuming computer
where (cid:80) P g x−αd represents the sum of received signal simulations,weleveragethestochasticgeometry.Specifically,
d d i by using the tools provided by stochastic geometry, we utilize
i∈φc
power from the DBSs in φ . We use σ2 to denote the power the results obtained from previous sections to derive the
c d
of the additive white Gaussian noise (AWGN) [14]. I is the coverage probability and spectral efficiency of C-V2X in a

## D

power of aggregate interference from the DBSs outside of φ multi-connectivity scenario.
c
and I can be expressed as

## D

(cid:88)

### I = P g x−αd. (8)

D d d i A. The joint distance distribution of the typical vehicle to n
i∈{φt D \φc } service DBSs

### Since the typical vehicle is connected to the n nearest


### DBSs in multi-connectivity, no other DBSs are closer than

distance x . And it also means that all interference DBSs are

### D. Performance Metrics n

farther than x . The above definition can be expressed by

### In order to enable advanced C-V2X applications such as n

f(x ,x ,··· ,x ), and we call it joint distance distribution
automated driving applications and stream media [4], [16], 1 2 n
for x ,x ,··· ,x .
it is crucial to ensure that the downlink transmission is both 1 2 n

### Lemma1. Thejointdistancedistributionofthetypicalvehicle

reliable and capable of transmitting data at a high rate. This
to its service DBSs in set φ from x to x is
is important not only from the perspective of a single vehicle c 1 n
but also from the perspective of the whole C-V2X network. f(x ,x ,··· ,x )=(2λ )ne−2λDxn, (11)
1 2 n D
To this end, this paper conducts an analytical evaluation of
wherex denotesthedistancebetweenthetypicalvehicleand
twoperformancemetrics,i.e.coverageprobabilityandspectral n
the n-th closest DBS in φ .
efficiency as follows. c
• The coverage probability of the typical vehicle v o in Proof:ThenullprobabilityofaPPPinanareaAise−λA,
downlink, is defined as the probability that the received where A = 2λx in 1-D PPP and A = πx2 in 2-D PPP, thus
SINR outperforms a predetermined threshold t [32]. It the CCDF of x 1 is [14]
can be expressed as P[x>x ]=P[no DBS closer than x ]
1 1

### P cov (t)=P(SINR D >t). (9) =e−2λDx1. (12)

It can also be calculated as the proportion of vehicles Because the CDF =1−CCDF, the CDF of x is
1
that have the received SINR above a threshold t, i.e.,
establish a successful connec

## D

tion with the DBSs in φ ,
F (x
1
)=1−e−2λDx1. (13)
c

<!-- Page 6 -->

6
Since the PDF f(x)= ∂F(x) [28], the PDF of x is Proof:Theproofofcoverageprobabilityinthedownlink
∂x 1
is
f(x )=2λ e−2λDx1. (14)

## 1 D


### P(SINR >t)

According to the definition of Section 3.3 in [34], let D
 m 
f(x 2 |x 1 ) denote the probability that the 2nd closest DBS is (cid:80) P d g d x− i αd
at x 2 given that the closest one is at the distance of x 1 . Thus ( = a)P  i=1 >t  
the probability of having no DBSs between the distances x 1  I D +σ d 2 
and x can be calculated as follows
2
 
According to f( t x h 2 e |x c 1 o ) n = dit 2 io λ n D al e− p 2 r λ o D b ( a x b 2 i − li x ty 1). Bayes theo ( r 1 e 5 m ) =P   g d > (cid:80) t m (cid:0) I P D + x σ − d 2 α (cid:1) d   

### D i

[35], f(x 2 ,x 1 ) denotes the joint distance distribution to the i=1
  
two nearest distances, i.e., the probability of having at least
i o s ne point in x 2 +△x, where △x is an infinitesimal quantity, ( = b)E xi,ID    exp    − µ (cid:80) m t (cid:0) I P D x + − σ α d 2 d (cid:1)      
d i
f(x
1
,x
2
)=f(x
2
|x
1
)f(x
1
)=(2λ

## D

)2e−2λDx2. (16)
 
i=1
 
B th y e f j o o l i l n o t w d i i n s g tan th c e e s d i i m st i r l i a b r u p ti r o o n ce f du (x re 1 s ,x in 2 · E · q · . x ( n 1 ) 5) fr a o n m d x E 1 q. to (1 x 6) n , ( = c)E xi    exp    − (cid:80) m µ P tσ x d 2 −αd    ζ I D (j)   
is d i
i=1
 
To co
f
m
(
p
x
a
1
re
,x
2
,·
t
·
h
·
e
,x
n
)
jo
=
int
(2λ

## D

d
)
i
n
s
e
ta
−
n
2
c
λ
e
Dxn.
distribu
(
t
1
io
7
n
)
= (cid:90) 0<x1<x2<···<xm<∞ ζ I D (j)exp    − (cid:80) m µ P t
d
σ x d 2 −
i
αd    ×
i=1
f(x 1 ,x 2 ,··· ,x n ) and the PDF of x n , we provide the f(x 1 ,x 2 ,··· ,x m )dx 1 dx 2 ···dx m , (21)
PDF of x in Eq. (18) as
n
(2λ x )n where(a)isobtainedbysubstitutingtheexpressionofSINR D
f(x
n
)=
x Γ
b
(
n
n)
e−2λbxn, (18) in Eq. (7). (b) is obtained by finding the CCDF of g
d
n which is exponentially distributed with parameter µ. ζ (j)

## I


## D

where Γ(n)=(n−1)! when n is a positive integer. is the Laplace transform of interference I D in (c), and j =
µt . Based on the definition of the Laplace transform,
(cid:80)m Pdx
i
−αd
B. Coverage Probability i=1
the derivation of ζ (j) is

## I


## D

A general expression for the coverage probability of multiconnectivity in C-V2X is calculated in this subsection. ζ ID (j)=E ID (cid:2) e−jID (cid:3)
  
a

## T

r
h
e
e
a
o
i
r
f
e
i
m
ts
1

## S

.

## In


## A


## R

v

## D

eh
v
ic
a
l
l
e
ue
is
f
c
ro
o
m
nsi
t
d
h
e
e
r
n
ed
ea
t
r
o
es
b
t
e
b
w
a
i
s
t
e
hi
s
n
ta
t
t
h
io
e
n
co
e
v
x
e
c
r
e
a
e
g
d
e
s
( = a)E

## Id

exp−j (cid:88) P
d
g
d
x−
i
αd
a certain threshold value t. On the other hand, if the SINR D i∈φt D \φc
 
falls below t, the vehicle is dropped from the network. Thus,
the coverage probability of downlink for multi-connectivity C-
(
=
b)E
Θd

## I

,{gd}
(cid:89) e−jPdgdx−
i
αd

V2X is i∈Θd

## I

(cid:20) (cid:90) ∞
P(SINR D >t) ( = c) exp −2λ D 1−
  xm
= (cid:90) 0<x1<x2<···<xm<∞ ζ I D (j)exp    − (cid:80) m µ P t d σ x d 2 − i αd    × ( E = d) gd ex (cid:2) p ex (cid:20) p − (cid:0) 2 − λ j D P (cid:90) d g ∞ d x 1 − i α − d (cid:1) j (cid:3) P dx x i − (cid:3) µ αd +µ dx i (cid:21) , (22)
i=1 xm d i
f(x ,x ,··· ,x )dx dx ···dx , (19)
1 2 m 1 2 m where we use Θd =φt \φ to denote the interference DBSs,

### I D c

where j = (cid:80)m P µ d t x− i αd , m is the number of cooperating DBSs i fi n n te d r i f n e g re th n e ce C I C D DF ca o n f b g e d o w b h t i a c i h ne i d se in xp E o q n . en (8 ti ) a . ll ( y b) di i s s tr o i b b t u a t i e n d ed wi b t y h
i=1
in the cooperative set, ζ (j) is the Laplace transform of parameter µ. (c) is derived from the probability generating

## I


## D

randomvariableinterferenceI evaluatedatj andζ (j)is functional (PGFL) of the PPP [36], i.e.,

## D I


## D

(cid:20) (cid:90) ∞ µ (cid:21) (cid:16)(cid:89) (cid:17) (cid:18) (cid:90) (cid:19)
ζ ID (j)=exp −2λ D 1− jP x−αd +µ dx i . (20) E f(x) =exp −λ (1−f(x))dx . (23)
xm d i R2

<!-- Page 7 -->

7
E (cid:2) exp (cid:0) −jP g x−αd (cid:1)(cid:3) in (d) can be derived as Proof: The proof of spectral efficiency of downlink is
gd d d i
E (cid:2) exp (cid:0) −jP g x−αd (cid:1)(cid:3) τ =E[ln(1+SINR )]
gd d d i D D
(cid:90) ∞ (cid:90)
=
e−jPdgdx−
i
αdµe−µgddg
d = f(x 1 ,x 2 ,··· ,x m )×
0 0<x1<x2<···<xm<∞
µe −j (cid:16) Pdx− i αd+µ (cid:17) gd   (cid:80) m P g x−αd 
=− |∞ d d i
jP µ d x− i αd +µ 0 E   ln    1+ i=1 I D +σ d 2       dx 1 dx 2 ···dx m
= . (24)
jP x−αd +µ
d i (cid:90)
(a)
= f(x ,x ,··· ,x )×
1 2 m
Since the farthest cooperation DBS is at a distance of x , the
m 0<x1<x2<···<xm<∞
integration limits are from x to ∞ in (d).   m  
m (cid:80) P g x−αd
(cid:90) d d i
t>0 P   ln    1+ i=1 I D +σ d 2    >t    dtdx 1 dx 2 ···dx m ,

### C. Spectral efficiency (29)

Thissubsectionderivestheexpressionofspectralefficiency
where t is the predetermined threshold. As a positive
forthedownlinkbyusingthetoolsofstochasticgeometryfor
random variable X is considered, it follows that E(X)
C-V2X in multi-connectivity. We computed the spectral effican be calculated as
(cid:82)∞P(X
> t)dt [14], thus the
ciency in units of nats/s/Hz (1 bit = ln(2) = 0.693 nats) 0

### E[ln(1+SINR )] can be calculated in (a). Furthermore,

for the typical vehicle. (cid:20) (cid:18) m D (cid:19) (cid:21)

### P ln 1+ (cid:80) P g x−αd/(I +σ2) >t is

Theorem 2. The spectral efficiency of the downlink in multi- d d i D d
i=1
connectivity C-V2X is
  m  
(cid:90) (cid:80) P d g d x i −αd
τ D = f(x 1 ,x 2 ,··· ,x m )× P ln  1+ i=1  >t  
0<x1<x2<···<xm<∞   I D +σ d 2  
E[ln(1+SINR )]dx dx ···dx , (25)
D 1 2 m
 m 
(cid:80) P g x−αd
where m is the number of cooperating DBSs. d d i
E[ln(1+SINR )] is ( = a)P  i=1 >et−1  
D  I +σ2 

### D d

E[ln(1+SINR )]=

## D  

(cid:90) t>0 P     ln     1+ i (cid:80) = m 1 I P D d + g d x σ − i d 2 αd     >t     dt, (26) ( = b)E gd    g d > (et− i (cid:80) = m 1 1 ) P (cid:0) d I x D i −α + d σ d 2(cid:1)   
  
where   (cid:80) m P d g d x− i αd   ( = c)E ID    exp    − µ(et i (cid:80) = m − 1 P 1) d (cid:0) x I − i D α + d σ d 2(cid:1)      

### P ln  1+ i=1  >t    

   I D +σ d 2    ( = d) exp    − (cid:80) m P βσ x d 2 −αd    ζ I D (j), (30)
d i
=exp    − (cid:80) m P βσ x d 2 −αd    ζ I D (j), (27) where (a) first solves i= t 1 he logarithm, then calculate the exd i pectation of the channel gain g in (b), and g follows the
i=1 d d
exponential distribution with mean 1/µ in (c). Since some
where β = µ(et−1) and j = β . ζ (j) is the variables have nothing to do with I , they can be treated as
(cid:80)m Pdx−
i
αd I D
constants and remain unchanged in

## D

(d). For the simplicity of
i=1
Laplace transform of interference I D , and ζ I (j) is the same the formula, we use β =µ(et−1) and j = β . The
as in Eq. (22), D (cid:80)m Pdx−
i
αd
i=1
Laplacetransformζ isthesamewithEq.(22)andisomitted
(cid:20) (cid:90) ∞(cid:18) µ (cid:19) (cid:21) ID
here.
ζ (j)=exp −2λ 1− dx .
I D D jP x−αd +µ i
xm d i
(28)

<!-- Page 8 -->

8
40
30
20
10
0
-10
-20
-2500 -2000 -1500 -1000 -500 0 500 1000 1500 2000 2500
Distance (m)
)m(
ecnatsiD
Proof: Given the similarity in the proof to that of Theorem 1, we omit the specific steps here.
DBS The spectral efficiency of cellular single-connectivity for
Vehicles downlink is
(cid:90) ∞
τD = f(x)E (cid:2) ln (cid:0) 1+SINRD(cid:1) >t (cid:3) dx, (36)
c c
0
where
E(cid:2) ln (cid:0) 1+SINR c D(cid:1) >t (cid:3) = (cid:90) ∞ e− µ(et− P 1) d xαdσd 2 ζ Ic (j)dt,
d
0
(37)
where j =µ(et−1)xαd/P d , the ζ Ic (j) is
d
ζ (j)=
Ic
d
(cid:20) (cid:90) ∞(cid:18) µ (cid:19) (cid:21)
exp −2λ 1− dx S
D x (et−1)xαdx− i αd +µ i
(38)
Fig.2. Simulationscenarioofmulti-connectivityinC-V2X. Proof: The proof of spectral efficiency of downlink
for cellular single-connectivity is similar to Theorem 2, the
specific steps are omitted here.

### D. Special case: Single-connectivity

Inordertocomparetheperformancewithmulti-connectivity Simulation 1: Simulation for multi-connectivity in C-
in C-V2X, this subsection focuses on the calculation of V2X
the coverage probability and spectral efficiency in a cellular Input: simulation number n, road length l, threshold t,
single-connectivity scenario, which represents the most basic DBS density λ , vehicle density λ ;
d v
approach. In this scenario, the typical vehicle associates with Output: Coverage probability CP, spectral efficiency
the cellular base station (CBS) whit the MRP. τ ;

## D

As the single-connectivity is a special case of multi- 1 Initialize τ o ←0 n×λvl , P←0 n×λvl , CP n ←0 1×n ,
connectivity, we model the similar channel model as in multi- τ ←0
n 1×n
connectivity scenario, and use λ C to denote the transformed 2 for i=1;i≤n;i++ do
intensity λ c of CBS ϱt after executing the procedures of ran- 3 Generate the locations m, V of DBSs and vehicles

## C

dom displacement, and λ C >λ D . As the CBS are distributed following 1-D PPP, respectively;
along the road following a 1-D PPP, the PDF of distance 4 for v =1;v ≤λ v l;v++ do
distribution is 5 Select collaborative DBSs according to Eq. (6);
f(x)=2λ e−2λCx, (31) 6 Calculate SINR D of DL according to Eq. (7);

### C 7 τ o (i,v)=ln(1+SINR D ), P(i,v)=SINR D ;

where x is the distance between the nearest CBS and the 8 end
typical vehicle. 9 CP n (i)= (cid:80)λ i= v 1 l(P(i,:)>t)/(λ v l);
Thecoverageprobabilityofthedownlinkincellularsingle- 10 τ n (i) = (cid:80)λ i= v 1 lτ o (i,:) /(λ v l);
connectivity is 11 end
P (cid:0) SINRD >t (cid:1) 12 Return τ D =
(cid:80)n
i=1 τ n (i)/n, CP =
(cid:80)n
i=1 CP n (i)/n;
cov c
(cid:90) ∞
= 2λ C e−µtσ d 2xαd/Pde−2λCxζ Ic (j)dx, (32)
d

## 0 V. Numericalandsimulationresults

where j =µtxαd/P
d
, the SINR
c

### D is


### A two-tier communication scenario on a straight urban

P g x−αd freewayisconsideredinthissection.Thelengthofthefreeway
SINR c D = d Ic d +σ i 2 , (33) is set as 30 km. The specific simulation scenario is shown
d d in Fig. 2. We first verify the proposed theoretical derivation
where the interference I d c is in previous sections over 10,000 Monte Carlo simulations
(cid:88) of the DBSs and vehicles following 1-D PPPs. The detailed

### Ic = P g x−αd. (34)

d d d i steps of the simulation are in Simulation 1. We use ‘Cellu
i∈ϱt
C 1’, ‘Conn 2’, and ‘Conn 3’ to abbreviate single-connectivity,
The Laplace transform of Ic is dual-connectivity, and triple-connectivity, respectively, in the
d
legends of the figures. According to [37]–[39], Table II sum-
(cid:20) (cid:90) ∞ µ (cid:21)
ζ I d c (j)=exp −2λ C x 1− jP d x− i αd +µ dx i . (35) m pa a p r e iz r. es the system simulation parameters employed in this

<!-- Page 9 -->

9
40
35
30
25
20
15
10
5
0
0 0.05 0.1 0.15 0.2 0.25 0.3
Distance(km)

## Fdp

7
xx 11 xx 22 6
xx 33
0.4 5
0.2
4
0 -0.2 3
0.26 0.262 0.264
2
1
0
0 0.05 0.1 0.15 0.2 0.25 0.3
Distance(km)
(a) a

## Fdp

tnioJ
104 1800
f(x) 1 1600 f(x, x) 1 2
f(x, x, x) 1400 1 2 3
1200
1 1000
0.5 800
0 0.2753440.2753460.275348 600
400
200
0
0 0.05 0.1 0.15 0.2 0.25 0.3
Distance(km)
(b) b

## Fdp

tnioJ
f(x) 1 f(x, x) 1 2
50
40
30
20
10
0 0 0.1 0.2 0.3
(c) c
Fig. 3. The distance distributions f(xi) and joint distance distribution f(x1,x2,···,xm) under different distances. (a) Distance distribution for nearest
distances x1,x2 and x3. (b) The joint distance distribution of f(x1),f(x1,x2) and f(x1,x2,x3). (c) Since f(x1) and f(x1,x2) is much smaller than
f(x1,x2,x3),thetwofunctionsarehighlightedhere.

## Tableii


## Mainparameters 1


### ChannelParameters Value 0.9

DBStransmittingpowerP d (dBm) 23
Pathlossexponentfordownlinkα
d
2.1∼6 0.8

### Noisepowerσ2 (dBm) -96

Meanoflog-no d rmalshadowinggain(dB) 0 0.7
StdofshadowinggainforMBS(dB) 2
0.6
Simulationparameters Value
Thelengthofroad(km) 30
0.5

### Thenumberofiteration 10,000

Densityofvehicleonroadλv (nodes/km) 20 0.4
DensityofDBSλ d (nodes/km) 0.05∼5.7
Threshold(dB) 0∼40 0.3
0.2

### A. Joint distance distribution 0.1

Fig. 3(a) shows the distance distribution of x 1 , x 2 , and x 3 . 0
0 5 10 15 20 25 30 35 40
We can see that the peak is gradually moving away from the

### Threshold(dB)

origin from x to x . Fig. 3(b) and Fig. 3(c) depict the joint
1 3
distance distribution for f(x ,x ) and f(x ,x ,x ). We can
1 2 1 2 3
see that the peak of f(x ,x ,x ) is closest to the origin, fol- 1 2 3
lowedbyf(x ,x ),andthefurthestisf(x ).Comparedwith
1 2 1
distance distributions in Fig. 3(a), the peak of joint distance
distributionhasahugeboost.Thecloserthedistancebetween
the peak and the origin, the better the performance. It can
be observed that in single-connectivity, f(x ) exhibits better
1
performance. Compared to a single-connectivity, a greater
number of DBSs connections in multi-connectivity lead to a
more significant performance improvement.

### B. Coverage probability

Thecoverageprobabilityvariationofdownlinkwiththreshold t is illustrated in Fig. 4. It is apparent that the simulation
values closely match the theoretical values, which further
verifies the validity of the theoretical derivation results. The
density of BS λ in single-connectivity is set as 3 nodes/km,
c
and the density λ of DBSs in multi-connectivity is set
d
as 6 nodes/km. Though λ > λ , we can see that the
c d
dual-connectivity and triple-connectivity still have a greater
coverage probability than single-connectivity. This suggests
that multi-connectivity performs better than cellular singleytilibaborP
egarevoC

### Simul: Conn 1

Analyt: Conn 1

### Simul: Conn 2

Analyt: Conn 2

### Simul: Conn 3


### Analyt: Conn 3

Fig. 4. Coverage probability variation with threshold t t ∈ [0,40] (λ d =
3nodes/km,λc=6nodes/km).
connectivity in C-V2X and multi-connectivity enhances the
coverage area of communications.
Fig. 5 illustrates the coverage probability as a function of
path loss exponent α . It can be seen that the Monte Carlo
d
simulation data and analytical data fit well. Considering the
dense deployment of DBSs in the simulation, vehicles are in
an interference-limited state. At this moment, the interference
power will decrease in accordance with the increase of α ,
d
which in turn lead to a promotion of SINR. Therefore, the
coverageprobabilitywillbeimprovedevenifthechannelgain
decrease.

### Forabetterinvestigationoftheimpactofpathlossexponent

α on the coverage probability under different densities of
d
DBSs,weplotFig.6inadual-connectivityscenario.Asshown
inFig.6,whenthedensityofDBSsisinadensedeployment,
the system is an interference-limited network. The distance
between the signal DBSs ∈ φ and the interference DBSs is
c
close to the typical vehicle, so the increase of α leads to
d
a greater impact on the interference signal power, resulting

<!-- Page 10 -->

10
1
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
2 2.5 3 3.5 4 4.5 5 5.5 6
Path loss exponent
d
ytilibaborP
egarevoC Simul: Conn 1
Analyt: Conn 1

### Simul: Conn 2

Analyt: Conn 2

### Simul: Conn 3


### Analyt: Conn 3

Fig. 5. The effect of path loss exponent on coverage probability( α d ∈
[2.1,6]).
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
2 2.5 3 3.5 4 4.5 5 5.5
Path loss exponent
d
ytilibaborP
egarevoC
0.25
0.2
0.15
0.1
0.05
0
0 5 10 15 20 25 30 35 40
Threshold(dB)
=1
d
=0.005
d
=0.00005
d
0.6708
0.6706
0.6704
3.599 3.6 3.601
Fig.6. Coverageprobabilityofdual-connectivityvarieswithdifferentpath
lossexponentindifferentdensitiesofDBSsα
d
(2.1∼5.7).
in an increase in the coverage probability. However, when the
densityislowenough,thesystemcanbeconsideredasanoiselimited network. Both the signal DBSs and the interference
DBSs are far away from the typical vehicle, so the increase
of α has a greater impact on the receiving signal power,
d
leading to a continuous decrease in the coverage probability.
When the density λ is at an appropriate size, such as λ
d d
= 0.005 nodes/km, the coverage probability first increases
and then decreases with the increase of α .
d

### The coverage probability of all cases decreases as the

threshold t increases, while the difference between singleconnectivity and multi-connectivity first increases and then
decreases in Fig. 7. This is mainly because the coverage
probability is respectively high and low at small and large
thresholds, respectively. Only when the threshold value is
in the middle range, the difference in coverage probability
is large, and the advantage of applying multi-connectivity
is also demonstrated. It can be observed that increasing the
number of connected DBSs does not result in a proportional
increaseinthecoverageprobabilitygain.Hence,ataparticular
threshold, there exists a balance tradeoff between the number
of corporation DBSs that are connected and the associated
ecnereffiD
2-1
3-2
Fig. 7. Coverage probability differences variation with threshold t (0 ∼
40dB).
1
0.95
0.9
0.85
0.8
0.75
0.7
0.65
0.6
0.55
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Density
d
ytilibaborP
egarevoC
stable
Analyt: Conn 1
Analyt: Conn 2
Analyt: Conn 3
Simul: Conn 1
Simul: Conn 2

### Simul: Conn 3

Fig.8. Coverageprobabilityvariationwithbasestationdensityλ d (0.1∼1
nodes/km).
cost.
As shown in Fig. 8, the coverage probability varies with
the density λ of DBSs. The coverage probability goes
d
up first and then stays relatively constant for both cellular
single-connectivity and multi-connectivity when the density
λ increases. It can also be seen that the growth rate of
d
multi-connection is faster than that of single-connection, and
it also reaches a stable point later. At the same time, it
can be seen that the coverage probability does not increase
significantly when comparing triple-connectivity to dualconnectivity. Therefore, increasing the number of cooperative

### BSs can improve communication coverage area, but it may

also incur high costs. By observing the horizontal axis, it can
benotedthatthechangeinDBSdensityλ isrelativelysmall
d
in magnitude. This implies that the coverage probability is
sensitivetochangesinλ ,andsuggeststhatsimplyincreasing
d
λ does not necessarily lead to an improvement in coverage
d
probability.

### C. Spectral efficiency


### The spectral efficiency varies with the path loss exponent

α is illustrated in Fig. 9. The simulation data is represented
d

<!-- Page 11 -->

11
11

### Simul: Conn 1

10 Analyt: Conn 1
9 Simul: Conn 2 Analyt: Conn 2
8 Simul: Conn 3
7 Analyt: Conn 3
6
5
4
3
2
1
2 2.5 3 3.5 4 4.5 5 5.5 6
Path loss exponent
d
Fig.9. Spectralefficiencyvariationwiththepathlossexponentα d (2.1∼5.9).
5.5
5
4.5
4
3.5
3
2.5
2
1.5
1
0.5
0
2 2.2 2.4 2.6 2.8 3 3.2 3.4 3.6 3.8
Path loss exponent
d
)zH/s/stan(
ycneiciffE
lartcepS
90
80
70 2-1
60 3-1
50
40
30
20
10
0
2.5 3 3.5 4 4.5 5 5.5
Path loss exponent
d
Fig.11. Spectralefficiencypercentageincreaseofmulti-connectivitycompared
tosingle-connectivity.
18
3.256
3.254
16
2.7
14
12
=1 10
d
=0.0005 d
=0.00005 8
d
6
0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5
Density
d
Fig.10. Spectralefficiencyofdual-connectivityvarieswithdifferentpathloss
exponentindifferentdensitiesofDBSsα
d
(2.1∼3.9).
by the points and the theoretical data is represented by the
dashed line in Fig. 9. We can observe that the simulation
data matches the theoretical data well, demonstrating the
correctness of the theoretical derivation. The increase of path
lossexponentleadstoagradualincreaseinspectralefficiency
andanapproximatelylinearrelationship.Thereasonisthat,as
the dense deployment of DBSs, vehicles are in a interferencelimited state, with the increase of path loss exponent α , the
d
interference signals weaken more than the signals transmitted
by the cooperative BSs, resulting in an increase in SINR and
consequently spectral efficiency. It appears that there exists
a close-to-linear relationship between the path loss exponent
α , mainly because after dividing the received signal power
d
(cid:80) P g x−αd into the denominator of Eq. (9), since the
d d i
i∈φc
thermalnoiseismuchsmallerthanthereceivedsignalandthus
σ2/ (cid:80) P g x−αd ≈ 0, then after logarithmic calculation,
d d d i
i∈φc
it approximates to a linear relationship. Fig. 12 depicts the
spectral efficiency of dual-connectivity as a function of α
d
in different densities of DBSs. Since the spectral efficiency
is mainly affected by SINR, it can be seen that the trend of
)zH/s/stan(
ycneicffE
lartcepS
stable Analyt: Conn 1
Analyt: Conn 2
Analyt: Conn 3
Simul: Conn 1
Simul: Conn 2

### Simul: Conn 3

Fig.12. Spectralefficiencyasafunctionofbasestationdensityλ d(0.05∼0.5
nodes/km).
spectral efficiency is similar to that of coverage probability in
Fig. 6 when the DBSs layout changes from extremely dense
to extremely sparse.

### Fig. 11 plots the spectral efficiency improvements between

the multi-connectivity and single-connectivity. It can be observed that the application of multi-connectivity technology
greatly improves the spectral efficiency in C-V2X. The improvement achieved by dual-connectivity can reach up to
40%, and that achieved by triple-connectivity can increase to
more than 75%. With the increase of path loss exponent α , d
the performance improvement of spectral efficiency does not
increase significantly. This indicates that multi-connectivity
technology has a stable performance gain.

### Fig.12illustratesthespectralefficiencyvarieswiththeDBS

densityλ .Withtheincreaseofλ ,thespectralefficiencyfirst
d d
improvesandthenremainsstable.Moreover,theimprovement
ofmulti-connectivityisgreaterthanthatofsingle-connectivity,
andthestablepointisalsofurtherback.Thismeansthatmulticonnectivity has a larger range of performance improvement.

### SimilartoFig.8,addingtoomanyDBSsdoesnotcontinuously

improve spectral efficiency. Additionally, it can be observed

<!-- Page 12 -->

12
that the stable point of spectral efficiency arrives earlier than [13] V. V. Chetlur and H. S. Dhillon, “Coverage analysis of a vehicular
thestablepointofcoverageprobability.Thus,whenincreasing networkmodeledasCoxprocessdrivenbyPoissonlineprocess,”IEEE
Transactions on Wireless Communications, vol. 17, no. 7, pp. 4401–
the density of DBSs λ , it is necessary to comprehensively
d 4416,2018.
considerthedemandsbetweenspectralefficiencyandcoverage [14] J. G. Andrews, F. Baccelli, and R. K. Ganti, “A tractable approach
probability. to coverage and rate in cellular networks,” IEEE Transactions on
communications,vol.59,no.11,pp.3122–3134,2011.
VI. CONCLUSION [15] L. P. Qian, Y. Wu, H. Zhou, and X. Shen, “Non-orthogonal multiple
accessvehicularsmallcellnetworks:Architectureandsolution,”IEEE
This paper has demonstrated the potential of enhancing Network,vol.31,no.4,pp.15–21,2017.
network performance in C-V2X by using the proposed multi- [16] K. Yu, H. Zhou, Z. Tang, X. Shen, and F. Hou, “Deep reinforcement
learning-basedRANslicingforUL/DLdecoupledcellularV2X,”IEEE
connectivity performance analysis framework. By analyzing
Transactions on Wireless Communications, vol. 21, no. 5, pp. 3523–
performanceindicatorssuchascoverageprobabilityandspec- 3535,2021.
tralefficiencyinthedownlink,thispaperhasprovidedinsights [17] Y.Xu,B.Qian,K.Yu,T.Ma,L.Zhao,andH.Zhou,“FederatedLearning Over Fully-Decoupled RAN Architecture for Two-tier Computing
intotheeffectofpathlossexponentandthedensityofDBSon
Acceleration,” IEEE Journal on Selected Areas in Communications,
thesystemperformanceindicators.TheextensiveMonteCarlo 2023.
simulationshaveeffectivelyvalidatedtheproposedframework [18] A. Kousaridas, C. Zhou, D. Mart´ın-Sacrista´n, D. Garcia-Roger, J. F.
anddemonstratedtheeffectivenessofmulti-connectivitytech- Monserrat,andS.Roger,“Multi-connectivitymanagementfor5GV2X
communication,”in2019IEEE30thAnnualInternationalSymposiumon
nology in enhancing the performance of C-V2X networks. Personal,IndoorandMobileRadioCommunications(PIMRC). IEEE,
The results of this paper have important implications for the 2019,pp.1–7.
research and practical applications of multi-connectivity C- [19] D. Moltchanov, A. Ometov, S. Andreev, and Y. Koucheryavy, “Upper
bound on capacity of 5G mmWave cellular with multi-connectivity

### V2X in the 5G and B5G era, and further investigations are

capabilities,”ElectronicsLetters,vol.54,no.11,pp.724–726,2018.
warranted to explore the full potential of this technology for [20] T. Sylla, L. Mendiboure, S. Maaloul, H. Aniss, M. A. Chalouf, and
next-generation communication systems. S. Delbruel, “Multi-Connectivity for 5G Networks and Beyond: A
Survey,”Sensors,vol.22,no.19,p.7591,2022.
[21] V. Petrov, D. Solomitckii, A. Samuylov, M. A. Lema, M. Gapeyenko,

## References


### D.Moltchanov,S.Andreev,V.Naumov,K.Samouylov,M.Dohleretal.,

[1] A. Wolf, P. Schulz, M. Do¨rpinghaus, J. C. S. Santos Filho, and “Dynamicmulti-connectivityperformanceinultra-denseurbanmmWave
G. Fettweis, “How reliable and capable is multi-connectivity?” IEEE deployments,” IEEE Journal on Selected Areas in Communications,
TransactionsonCommunications,vol.67,no.2,pp.1506–1520,2018. vol.35,no.9,pp.2038–2055,2017.
[2] C. Pupiales, D. Laselva, Q. De Coninck, A. Jain, and I. Demirkol, [22] M. Giordani, M. Mezzavilla, S. Rangan, and M. Zorzi, “Multi-
“Multi-connectivityinmobilenetworks:Challengesandbenefits,”IEEE connectivityin5GmmWavecellularnetworks,”in2016Mediterranean
CommunicationsMagazine,vol.59,no.11,pp.116–122,2021. AdHocNetworkingWorkshop(Med-Hoc-Net). IEEE,2016,pp.1–7.
[3] L.Weedage,C.Stegehuis,andS.Bayhan,“Impactofmulti-connectivity [23] Z. Sattar, J. V. Evangelista, G. Kaddoum, and N. Batani, “Spectral
onchannelcapacityandoutageprobabilityinwirelessnetworks,”IEEE efficiencyanalysisofthedecoupledaccessfordownlinkanduplinkin
TransactionsonVehicularTechnology,2023. two-tiernetwork,”IEEETransactionsonVehicularTechnology,vol.68,
[4] Y. Xu, H. Zhou, T. Ma, J. Zhao, B. Qian, and X. Shen, “Leveraging no.5,pp.4871–4883,2019.
multiagentlearningforautomatedvehiclesschedulingatnonsignalized [24] A.Shafie,N.Yang,andC.Han,“Multi-connectivityforindoorterahertz
intersections,” IEEE Internet of Things Journal, vol. 8, no. 14, pp. communication with self and dynamic blockage,” in ICC 2020-2020
11427–11439,2021. IEEEInternationalConferenceonCommunications(ICC). IEEE,2020,
[5] S.Chen,J.Hu,Y.Shi,Y.Peng,J.Fang,R.Zhao,andL.Zhao,“Vehicle- pp.1–7.
to-everything(V2X)servicessupportedbyLTE-basedsystemsand5G,” [25] M. G. Kibria, K. Nguyen, G. P. Villardi, W.-S. Liao, K. Ishizu, and
IEEE Communications Standards Magazine, vol. 1, no. 2, pp. 70–76, F. Kojima, “A stochastic geometry analysis of multiconnectivity in
2017. heterogeneous wireless networks,” IEEE Transactions on Vehicular
[6] J. Chen, G. Mao, C. Li, W. Liang, and D.-g. Zhang, “Capacity of Technology,vol.67,no.10,pp.9734–9746,2018.
cooperative vehicular networks with infrastructure support: Multiuser
[26] V. Kamble, S. Kalyanasundaram, V. Ramachandran, and R. Agrawal,
case,” IEEE Transactions on Vehicular Technology, vol. 67, no. 2, pp.
“Efficientresourceallocationstrategiesformulticast/broadcastservices
1546–1560,2017.
in3GPPlongtermevolutionsinglefrequencynetworks,”in2009IEEE
[7] Z. Lu, T. Zhang, X. Ji, B. Qian, L. Jiao, and H. Zhou, “Person-
Wireless Communications and Networking Conference. IEEE, 2009,
alized Wireless Resource Allocation in Multi-Connectivity B5G C-
pp.1–6.
V2X Networks,” in 2022 14th International Conference on Wireless
[27] M. Simsek, T. Ho¨ßler, E. Jorswieck, H. Klessig, and G. Fettweis,
CommunicationsandSignalProcessing(WCSP). IEEE,2022,pp.1–6.
“Multiconnectivity in multicellular, multiuser systems: A matching-
[8] A. Rabitsch, K.-J. Grinnemo, A. Brunstrom, H. Abrahamsson, F. B.
basedapproach,”ProceedingsoftheIEEE,vol.107,no.2,pp.394–413,
Abdesslem,S.Alfredsson,andB.Ahlgren,“Utilizingmulti-connectivity
2019.
to reduce latency and enhance availability for vehicle to infrastructure
[28] S.N.Chiu,D.Stoyan,W.S.Kendall,andJ.Mecke,Stochasticgeometry
communication,” IEEE Transactions on Mobile Computing, vol. 21,
anditsapplications. JohnWiley&Sons,2013.
no.5,pp.1874–1891,2020.
[9] P. Wu, L. Ding, Y. Wang, L. Li, H. Zheng, and J. Zhang, “Perfor- [29] A.AbdulqaderHussein,T.A.Rahman,andC.Y.Leow,“Performance
mance analysis for uplink transmission in user-centric ultra-dense V2I evaluation of localization accuracy for a log-normal shadow fading
networks,”IEEETransactionsonVehicularTechnology,vol.69,no.9, wirelesssensornetworkunderphysicalbarrierattacks,”Sensors,vol.15,
pp.9342–9355,2020. no.12,pp.30545–30570,2015.
[10] F.B.Tesema,A.Awada,I.Viering,M.Simsek,andG.Fettweis,“Eval- [30] Chetlur, Vishnu Vardhan and Dhillon, Harpreet S, “Coverage and rate
uation of context-aware mobility robustness optimization and multi- analysisofdownlinkcellularvehicle-to-everything(C-V2X)communiconnectivityinintra-frequency5Gultradensenetworks,”IEEEWireless cation,”IEEETransactionsonWirelessCommunications,vol.19,no.3,
CommunicationsLetters,vol.5,no.6,pp.608–611,2016. pp.1738–1753,2019.
[11] L. Diez, A. Garcia-Saavedra, V. Valls, X. Li, X. Costa-Perez, and [31] C. Xu, M. Sheng, V. S. Varma, T. Q. Quek, and J. Li, “Wireless
R.Agu¨ero,“LaSR:Asupplemulti-connectivityschedulerformulti-RAT service provider selection and bandwidth resource allocation in multi-
OFDMA systems,” IEEE Transactions on Mobile Computing, vol. 19, tierHCNs,”IEEETransactionsonCommunications,vol.64,no.12,pp.
no.3,pp.624–639,2018. 5108–5124,2016.
[12] S. Chen, T. Zhao, H.-H. Chen, Z. Lu, and W. Meng, “Performance [32] X. Yang and A. O. Fapojuwo, “Coverage probability analysis of hetanalysisofdownlinkcoordinatedmultipointjointtransmissioninultra- erogeneouscellularnetworksinRician/Rayleighfadingenvironments,”
densenetworks,”IEEENetwork,vol.31,no.5,pp.106–114,2017. IEEECommunicationsLetters,vol.19,no.7,pp.1197–1200,2015.

<!-- Page 13 -->

13
[33] M. Jia, Z. Yin, Q. Guo, G. Liu, and X. Gu, “Downlink design for
spectrumefficientIoTnetwork,”IEEEInternetofThingsJournal,vol.5,
no.5,pp.3397–3404,2017.
[34] D. Moltchanov, “Distance distributions in random networks,” Ad Hoc
Networks,vol.10,no.6,pp.1146–1166,2012.
[35] D.Berrar,“Bayes’theoremandnaivebayesclassifier,”Encyclopediaof
BioinformaticsandComputationalBiology:ABCofBioinformatics,vol.
403,p.412,2018.
[36] D.Stoyan,W.S.Kendall,S.N.Chiu,andJ.Mecke,Stochasticgeometry
anditsapplications. JohnWiley&Sons,2013.
[37] “Studyonevaluationmethodologyofnewvehicle-to-everything(V2X)
use cases for LTE and NR,” Sophia Antipolis Cedex, France, 3GPP,
Tech.Rep.37.885v15.2.0,Dec2018.

### Haibo Zhou (Senior Member, IEEE) received the

[38] “Coordinated multi-point operation for LTE physical layer aspects,”

### Ph.D. degree in information and communication

SophiaAntipolisCedex,France,3GPP,Tech.Rep.36.819v11.2.0,Sep
engineering from Shanghai Jiao Tong University,
2013.

### Shanghai, China, in 2014. From 2014 to 2017,

[39] H.Elshaer,M.N.Kulkarni,F.Boccardi,J.G.Andrews,andM.Dohler,
he was a Postdoctoral Fellow with the Broadband
“Downlink and uplink cell association with traditional macrocells and

### Communications Research Group, Department of

millimeterwavesmallcells,”IEEETransactionsonWirelessCommuni-
ElectricalandComputerEngineering,Universityof
cations,vol.15,no.9,pp.6244–6258,2016.

### Waterloo. He is currently a Full Professor with

the School of Electronic Science and Engineering,
NanjingUniversity,Nanjing,China.Hewaselected
asanIETfellowin2022,highlycitedresearcherby
Clarivate Analytics in 2022 & 2020. He was a recipient of the 2019 IEEE
LuofangJiao(StudentMember,IEEE)receivedthe ComSocAsia–PacificOutstandingYoungResearcherAward,2023-2024IEEE
B.S.degreeindetectionguidanceandcontroltech- ComSoc Distinguished Lecturer, and 2023-2025 IEEE VTS Distinguished
nology from the University of Electronic Science Lecturer.HeservedasTrack/SymposiumCoChairforIEEE/CICICCC2019,
andTechnologyofChina,Chengdu,China,in2020. IEEEVTC-Fall2020,IEEEVTC-Fall2021,WCSP2022,IEEEGLOBECOM
He is currently working toward the Ph.D. degree 2022, IEEE ICC 2024. He is currently an Associate Editor of the IEEE
with the School of Electronic Science and Engi- TransactionsonWirelessCommunications,IEEEInternetofThingsJournal,
neering,NanjingUniversity,Nanjing,China.Hisre- IEEE Network Magazine, and Journal of Communications and Information
search interests include uplink/downlink decoupled Networks. His research interests include resource management and protocol
access,C-V2X,andheterogeneousnetworks. designinB5G/6Gnetworks,vehicularadhocnetworks,andspace-air-ground
integratednetworks.

### Tianqi Zhang (Student Member, IEEE) received

the B.S. degree in electronic information science
and technology from Nanjing University, Nanjing,
China, in 2021, where he is currently pursuing the

### Ph.D.degreewiththeSchoolofElectronicScience

and Engineering. He mainly focuses on the FD-

### RAN, V2X, and machine learning in the field of

emergingwirelessnetworks. DongmeiZhao(SeniorMember,IEEE)receivedthe
B.S.degree in wireless communication from Northern Jiaotong University (currently, Beijing Jiaotong
University), Beijing, China, in 1992, and the Ph.D
degreefromtheDepartmentofElectricalandCom-
Jiwei Zhao (Student Member, IEEE) received the puter Engineering, University of Waterloo, Water-
M.S. degree in information and communication loo, ON, Canada, in June 2002. In July 2002, she
system from Xidian University, Xi’an, China, in joined the Department of Electrical and Computer

## He is currently working toward the Ph.D. Engineering, McMaster University, where she is a

degree with the School of Electronic Science and Full Professor. From April 2004 to March 2009,
Engineering, Nanjing University, Nanjing, China. she was an Adjunct Assistant Professor with the
He won the first prize in the 2016 CCF (China DepartmentofElectricalandComputerEngineering,UniversityofWaterloo.
Computer Federation) China Big Data and Cloud Her current research areas are mainly in mobile computation offloading,
Computing Intelligence Contest. His research in- energyefficientwirelessnetworking,andvehicularcommunicationnetworks.
terests include fully-decoupled RAN architecture, She is a Co-Chair of the Mobile and Wireless Networks Symposium of
coordinated multi-point, and machine learning ap- IEEE GLOBECOMConference 2020, the WirelessNetworking Symposium
plicationsforwirelesscommunication. inIEEEGLOBECOMConference2007,theGreenComputing,Networking,
andCommunicationsSymposiuminInternationalConferenceonComputing,
NetworkingandCommunications2020,thetechnicalprogramcommitteefor
IEEE International Workshop on Computer Aided Modeling and Design of
Communication Links and Networks 2016, the General Symposium of the
Yunting Xu (Student Member, IEEE) received the International Wireless Communications and Mobile Computing (IWCMC)
B.S. degree in communication engineering from Conference 2007, and a co-chair of the Vehicular Networks Symposium
NanjingUniversity,Nanjing,China,in2017,where of IWCMC from 2012 to 2019. He is an Associate Editor of the IEEE
he is currently pursuing the Ph.D. degree with the INTERNET OF THINGS JOURNAL. She served as an Associate Editor
School of Electronic Science and Engineering. He for the IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY from
mainly focuses on the dynamic resource manage- 2007 to 2017. She also served as an Editor for EURASIP Journal on
ment and networking optimization in the field of Wireless Communications and Networking and Journal of Communications
emergingwirelessnetworks. and Networks. She has been in Technical Program Committee of many
international conferences in her fields. She is a Professional Engineer of
Ontario.

## Tables

**Table (Page 4):**

| Downlink 2nd 2nd 3rd DDLL BBSS |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| 1st 3rd 1st Interference Downlink Base Station Interference |  |  |  |  |  |  |  |  |  |  |


**Table (Page 8):**

|  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | DBS |  |
|  |  |  |  |  |  |  |  |  | Veh | icles |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 9):**

|  |
|---|
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |


**Table (Page 10):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  | S A | imul: nalyt: | Conn 1 Conn 1 |
|  |  |  |  |  | S A S | imul: nalyt: imul: | Conn 2 Conn 2 Conn 3 |
|  |  |  |  |  | A | nalyt: | Conn 3 |
|  |  |  |  |  |  |  |  |


**Table (Page 10):**

|  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | 2-1 3-2 |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |


**Table (Page 10):**

|  |  | =1 d =0.00 d =0.00 | 5 005 |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | d |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 0. |  | 6708 |  |  |  |  |
|  |  |  |  |  | 0. |  | 6706 |  |  |  |  |
|  |  |  |  |  | 0. |  | 6704 |  |  |  |  |
|  |  |  |  |  |  |  | 3.599 |  | 3.6 3.6 | 01 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 10):**

|  |  |  |  |  | sta | ble |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Ana | lyt: Co | nn 1 |  |
|  |  |  |  |  | Ana Ana | lyt: Co lyt: Co | nn 2 nn 3 |  |
|  |  |  |  |  | Sim | ul: Co | nn 1 |  |
|  |  |  |  |  | Sim | ul: Co | nn 2 |  |
|  |  |  |  |  | Sim | ul: Co | nn 3 |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 11):**

| Simul: C Analyt: C | onn 1 onn 1 |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Simul: C Analyt: C Simul: C Analyt: C | onn 2 onn 2 onn 3 onn 3 |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 11):**

|  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  | 2 3 |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 11):**

| 256 |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| 254 |  |  |  |  |  |  |  |  |  |
| 2. | 7 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
| = | 1 |  |  |  |  |  |  |  |  |
| d = | 0.000 |  | 5 |  |  |  |  |  |  |
| d = d | 0.000 |  | 05 |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |


**Table (Page 11):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  | stab | le |  | Analyt: | Conn | 1 |
|  |  |  |  |  |  | Analyt: Analyt: | Conn Conn | 2 3 |
|  |  |  |  |  |  | Simul: Simul: | Conn Conn | 1 2 |
|  |  |  |  |  |  | Simul: | Conn | 3 |
