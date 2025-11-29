---
title: "Financial Document Analysis"
original_file: "./Financial_Document_Analysis.pdf"
document_type: "guide"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "chain-of-thought", "multimodal"]
keywords: ["cid", "ray", "pump", "energy", "fig", "probe", "delay", "where", "pulse", "signal"]
summary: "<!-- Page 1 -->

Hard X-ray Generation and Detection of Nanometer-Scale Localized Coherent
Acoustic Wave Packets in SrTiO and KTaO
3 3
Yijing Huang,1,2,3,4,∗ Peihao Sun,2,5,† Samuel W. Teitelbaum,2,6 Haoyuan Li,7 Yanwen Sun,7 Nan Wang,7
Sanghoon Song,7 Takahiro Sato,7 Matthieu Chollet,7 Taito Osaka,8 Ichiro Inoue,8 Ryan A. Shin,9 Johann Haber,2 Jinjian Zhou,10 Marco Bernardi,10 Mingqiang Gu,11 James M."
related_documents: []
---

# Financial Document Analysis

<!-- Page 1 -->

Hard X-ray Generation and Detection of Nanometer-Scale Localized Coherent
Acoustic Wave Packets in SrTiO and KTaO
3 3
Yijing Huang,1,2,3,4,∗ Peihao Sun,2,5,† Samuel W. Teitelbaum,2,6 Haoyuan Li,7 Yanwen Sun,7 Nan Wang,7
Sanghoon Song,7 Takahiro Sato,7 Matthieu Chollet,7 Taito Osaka,8 Ichiro Inoue,8 Ryan A. Duncan,2,4 Hyun D.
Shin,9 Johann Haber,2 Jinjian Zhou,10 Marco Bernardi,10 Mingqiang Gu,11 James M. Rondinelli,12 Mariano
Trigo,2,4 Makina Yabashi,8 Alexei A. Maznev,9 Keith A. Nelson,9 Diling Zhu,7 and David A. Reis2,3,4,‡
1Department of Physics, University of Illinois at Urbana-Champaign, Urbana, IL 61801, USA
2Stanford PULSE Institute, SLAC National Accelerator Laboratory, Menlo Park, CA 94025, USA
3Department of Applied Physics, Stanford University, Stanford, CA 94305, USA
4Stanford Institute for Materials and Energy Sciences,
SLAC National Accelerator Laboratory, Menlo Park, CA 94025, USA
5Dipartimento di Fisica e Astronomia “Galileo Galilei”,

### Universita` degli Studi di Padova, Padova 35131, Italy

6Department of Physics, Arizona State University, Tempe, AZ 85287, USA
7Linear Coherent Light Source, SLAC National Accelerator Laboratory, Menlo Park, CA 94025, USA
8RIKEN SPring-8 Center, 1-1-1 Kouto, Sayo-cho, Sayo-gun, Hyogo 679-5148, Japan
9Department of Chemistry, Massachusetts Institute of Technology, Cambridge, MA 02139, USA
10Department of Applied Physics and Materials Science,

### California Institute of Technology, Pasadena, CA 91125, USA

11Department of Physics, Southern University of Science and Technology (SUSTech), Shenzhen, Guangdong, China, 518055
12Department of Materials Science and Engineering,
Northwestern University, Evanston, IL 60208-3108, USA
(Dated: January 4, 2024)
Wedemonstratethattheabsorptionoffemtosecondhardx-raypulsescanexcitequasi-spherical,
high-amplitude and high-wavevector coherent acoustic phonon wavepackets using an all hard-x-ray
pump-probe scattering experiment. The time- and momentum-resolved diffuse scattering signal is
consistentwithstrainpulsesinducedbytherapidelectroncascadedynamicsfollowingphotoionization at uncorrelated excitation centers. We quantify key parameters of this process, including the
localizationsizeofthestrainwavepacketandthephotonenergyconversionefficiencyintoelasticenergy. TheparametersaredeterminedbythephotoelectronandAugerelectroncascadedynamics,as
wellastheelectron-phononinteraction. Inparticular,weobtainthelocalizationsizeoftheobserved
strain wave packet to be 1.5 and 2.5 nm for bulk SrTiO and KTaO single crystals, even though
3 3
there are no nanoscale structures or light-intensity patterns that would ordinarily be required to
generateacousticwavesofwavelengthsmuchshorterthanthepenetrationdepth. WhereasinGaAs
and GaP we do not observe a signal above background. The results provide crucial information
on the mechanism of x-ray energy deposition into matter and shed light on the shortest collective
length scales accessible to coherent acoustic phonon generation using x-ray excitation, facilitating
future x-ray study of high-wavevector acoustic phonons and thermal transport at the nanoscale.
I. INTRODUCTION complexprocessofsecondaryinteractionsservestoeither
induce or avoid radiation damage depending on how effectively it dissipates the high energy density associated
Fundamental x-ray-matter interactions are typically
with localized x-ray excitation.
dominated by photoionization of core electrons creating highly-excited states that initially decay on the fem- Thus, it is important to understand experimentally
tosecond time-scale through Auger-Meitner decay and the energy relaxation processes and subsequent struccharacteristic florescence[1]. The subsequent cascade of turaldynamicsfollowingx-rayionizationontherelevant
secondary excited states involves the inelastic scattering length and time scales. This is particularly critical for
of high-energy electrons and to a lesser extent photons. experiments that utilize the high flux and short pulse
Thiscreatesadditionalcoreexcitedstates,andaplethora duration of x-ray free electron lasers (XFELs) to create
of both single-particle and collective excitations includ- and/or probe atomic-scale dynamics. Even the most roingelectron-holepairs, plasmons, polarons, andphonons bust materials are not immune to single-shot radiation
[2]inhardcondensedmattersystems. Thisexponentially damage in the focused beam of an XFEL where intensities can be high enough to saturate the photoionization cross-section [3, 4] as well as induce multi-photon

### K-shell absorption [5–7], and Compton scattering[8]. In

∗ huangyj@illinois.edu recentx-raypump, x-rayprobeexperimentsondiamond
† peihao.sun@unipd.it excited beyond the single-shot damage threshold, the
‡ dreis@stanford.edu atomicmotionappearedfrozenforthefirst20fs[9],while
4202
naJ
3
]ics-lrtm.tam-dnoc[
2v35461.2132:viXra

<!-- Page 2 -->

2
inproteinsdense-environmenteffectshavebeenfoundto Due to imperfections in the translation stages, the anstronglyaffectlocalradiationdamageinducedstructural gles of crystals C and C vary slightly as the delays is
2 3
dynamics[10]. It is equally important to understand the scanned. While the magnitude of the angular deviation
structural dynamics induced by x-ray absorption below issmallcomparedtothe∼16µradDarwinwidth(forthe
the single-shot damage threshold. p-polarized x rays), this “wobble” nonetheless results in
Here we present the results of x-ray pump, x-ray slight variation of the pointing between the two pulses.
probestructuraldynamicsexperimentsontheoxideper- Since the wobbling motion is correlated with the moovskites, SrTiO and KTaO excited at high densities, torpositions(whichcorrespondtodifferentdelaytimes),
3 3
but below the multi-shot damage threshold. We find the variations in the pointing are repeatable and thus
thatthephotoionizationleadstothesuddenexcitationof are partially corrected by changing the angles of crys-
3-dimensional (3D) coherent acoustic phonon wavepack- tals C and C as a function of delay. The remaining
2 3
etswithcharacteristicwavelengthsontheorderofsingle variations are well characterized, and the effect on the
nanometerscale,throughanalysisoftheevolutionofdif- signal is accounted for using an overlap correction factor
fusescatteringintimeandmomentum(inducingchanges as a function of the delay; more details are provided in
inthesignalofover100%withmoderatepulsefluences). Appendix B1.
We model the strain generation and propagation as due The pulse energies are measured shot-to-shot at the
to the in-phase addition of coherent acoustic wavepack- 120 Hz repetition rate of the FEL by intensity monitors
etsoriginatingfromalargecollectionofnanometerstress shown as green dots in Fig. 1A. Specifically, the pulse
centersfollowinglocalizedphotoionizationeventsatran- energies in the individual branches are measured by the
dom uncorrelated sites. We do not observe signatures of x-raydiodesd andd placedrightbeforetherecombi-
03 34
acoustic phonon generation above noise in semiconduct- nation of the branches, while the overall pulse intensity
ing GaAs or GaP indicating that there are significant is measured by the intensity monitor i placed between
5
differences in the cascade process and in particular the the Be lens stack and the sample. The conversion from
dissipation of electronic energy to the lattice. diodereadingtopulseenergyiscalibrated,asdetailedin
The results have fundamental implications for our un- Appendix B2.
derstanding of x-ray matter interactions at modest in- The experimental geometry is shown in Fig. 1B. The
tensities below the damage threshold. In particular, the samples are placed in reflection geometry at room temstructuraldynamicsinitiatedbytheelectroncascadepro- perature, with the beam incident angle on the sample
cess has practical implications for developing a micro- fixedto5°grazing. Theincidentx-rayfluenceiskeptbescopic understanding of condensed matter dynamics, for low the multiple pulse damage threshold of the sample.
example, using high wavevector x-ray transient grating The x rays scattered by the sample are collected by an
spectroscopy[11] to study nanoscale thermal transport areadetector(Jungfrau-1M,pixelsize75µm×75µm)[16]
[12, 13]. placedaround130mmawayfromthesample. Intheelastic scattering limit, each pixel on the detector maps to
a Q = k −k , where k and k are the incoming
out in in out
II. METHODS andoutgoingwavevectors,respectively,withamplitudes
|k | = |k | = 2π/λ where λ is the x-ray wavelength
in out
1.26˚A. The sample is rotated around its surface nor-
The experiment is carried out at the x-ray correlation
mal nˆ until the Bragg condition for a low-order Bragg
spectroscopy (XCS) endstation at the Linac Coherent
peak was found, and then rotated by at most 1° to tune

### Light Source (LCLS) [14]. The photon energy is set to

off the Bragg peak to access the diffuse scattering about
9.828keV, slightly below the Ta L3 edge. A schematic
the peak. For the cubic perovskite samples SrTiO and
diagramofthesplit-delaysetupisshowninFig.1A.The 3

### KTaO with surface normal (001), the targeted Bragg

hardx-raysplit-delay(HXRSD)unit[15]isinsertedinto 3
peak was (¯1¯12).
the x-ray beam path, splitting each x-ray pulse into two
branches, afixed-delaybranch(redlines)andavariabledelaybranch(bluelines). Therelativedelaybetweenthe
pulse from the two branches is adjusted by changing the

## Iii. Results

path length in the variable-delay branch, as indicated by
the blue double-headed arrows; in this work, the delay

### A. Extraction of the pump-probe signal

is changed between -2ps and 10ps in 0.1ps steps. After
the crystal C , the pulses from the two branches, each
4
approximately 30fs in duration, become nearly collinear We begin by examining the general features of the
and are focused by a beryllium (Be) lens stack of focal pump-probe signal, taking SrTiO 3 as an example. The
length3.5mtoapproximately20µm×20µmatthesam- detectormeasuresxraysfrombothpulses, suchthatthe
ple position. The spatial overlap between the two pulses scattered intensity detected,
isoptimizedwiththehelpofabeamprofilemonitorconsisting of a Ce:YAG scintillator screen positioned in the I(Q,t;E ,E )=E S (Q)+E S (Q)+∆I(Q,t;E ,E ),
1 2 1 0 2 0 1 2
same plane as the sample and a microscope objective. (1)

<!-- Page 3 -->

3
FIG. 1. The split-delay setup and experimental geometry. (A) Schematic diagram of the split-delay setup. After the FEL
x-ray pulse passes through an upstream double-crystal, diamond (111) monochromator, it arrives at the HRXSD unit and
is split into two branches by a silicon crystal with a polished edge (C ): the fixed-delay branch (red lines) consisting of two
1
channel-cut crystals (CC and CC ), and the variable-delay branch (blue lines) consisting of four crystals (C to C ). Silicon
1 2 1 4
(220) reflections were used for all crystals of the HRXSD unit. X rays from the two branches are combined after crystal C
4
and are focused by a Be lens stack onto the sample. The relative delay between the two branches is adjusted by changing the
path length in the variable-delay branch, specifically by changing the positions of C and C using linear translation stages
2 3
aligned along the blue double-headed arrows. The black circles around the crystals denote the rotation motor stages. Green
dots indicate X-ray intensity monitors. (B) Schematic diagram of the experimental geometry. X rays from the two branches,
denoted with red and blue pulses, separated by t in time, are focused onto the same position on the sample at an incidence
angle of 5°. The sample is rotated around its surface normal nˆ to go on and off the Bragg condition. The scattered x-rays are
collected by an area detector.
where t is the time delay. E and E denote the pulse pump-probe signal should be large. These ranges are in-
1 2
energies in the variable-delay and fixed-delay branches, dicatedbythesolidanddashedboxesinthehistogramin
respectively, which are measured separately as shown in Fig.2A.Wethencalculatethenormalizedimageforeach
Fig. 1A. Here and in the rest of the text, Q denotes category by dividing the summed image by the summed
the scattering wavevector, G the nearest reciprocal lat- pulse intensities.
tice vector (i.e., the Bragg peak), and q ≡ Q−G the

### The normalized low- and high-intensity images for

reduced wave vector (i.e., the deviation from the Bragg
SrTiO at t = 4.0ps are shown in Fig. 2B-C. Note
3
peak). The first two terms on the right-hand side of
that the long white streaks are due to scattering from
Eq. (1) represent the intensities of diffuse scattering in
the tails of the Bragg peak (from the surface truncation
thermal equilibrium, which are proportional to the pulse
rod). Comparing these two images, one can see moduenergies, and S (Q) is the diffuse scattering structure
0 lations away from the central region appear in the highfactor independent of the pulse energies. The last term,
intensityimage,whichbecomesclearerwhendividingthe
∆I(Q,t;E ,E ), represents the pump-probe signal which
1 2 high-intensity image by the low-intensity one as shown
depends onboth the pump andprobe pulse energies and
in Fig. 2D. These modulations appear like ripples emathe relative delay between the two pulses.
nating from the center, which corresponds to the closest
point to the (¯1¯12) Bragg peak on the detector (i.e., on
To extract the pump-probe signal ∆I(Q,t;E ,E ), we
1 2
the Ewald sphere), reflecting the acoustic phonon excifirstnotethatthex-raypulseintensitydeliveredontothe
tation in the sample. Note that the relative signal level
sample varies shot-to-shot due to the fluctuating overlap
is rather high: the modulations reach more than 100%
between the x-ray spectrum coming into the split-andofthediffusescatteringbackgroundapproximatedbythe
delay system and the band-pass of the crystals in the
low-intensityimageinFig.2B.Incomparison,thepumpsystem [17]. The ratio between the intensities in the two
probe signal appears negligible around zero time delay:
branches, E /E ,alsofluctuatesduetojitterinthebeam
1 2

### Fig.2Eshowstheresultsfordelayt=0.0ps,whichdoes

position at the splitting crystal C . Therefore, through-
1
not contain any modulation like in Fig. 2D. Therefore,
out the measurement, we collect a large set of images
we use the data at time zero as the background diffuse
with a wide distribution of pulse energies E and E . As
1 2
scattering, as will be further detailed below.
an example, a histogram of the distribution of (E ,E )
1 2
at delay t = 4.0ps is shown in Fig. 2A. The distribu- Having observed the general features of the pumptions at other time delays are similar. This wide dis- probe signal, we next demonstrate that it is bi-linear
tribution of (E ,E ) helps isolate the pump-probe signal in the pump and probe pulse energies. Because the
1 2
∆I(Q,t;E ,E ): from all shots at time delay t, we select pump-probe signal, ∆I(Q,t;E ,E ), should be propor-
1 2 1 2
“lowintensity”ones(0.1µJ<E ,E <0.25µJ)wherethe tional to both the probe pulse energy and the amount
1 2
pump-probe signal is expected to be small, and “high of lattice distortion created by the pump pulse, the biintensity” ones (0.85µJ < E ,E < 1.6µJ) where the linearity is expected if the latter is proportional to the
1 2

<!-- Page 4 -->

4
1.5
1.0
0.5
0.5 1.0 1.5

## [ J]

1

## ]J

[
2

## A

50
40
30
20
0.0 0.2 0.4 0.6

## /( + ) [ J]

1 2 1 2

## ]J


## /Uda[

)
+
(/

## I

2
1

## Ior

102
B t=4.0ps C t=4.0ps
101
100
low intensity high intensity
F D t=4.0ps
4.0 ps
0.0 ps
high/low
stnuoc
200
150
100
50
0
E t=0.0ps
high/low

## ]J


## /Uda[


## I

2.0
1.75
1.5
1.25
1.0
oitar
FIG. 2. General features of the pump-probe signal. (A) 2D histogram of the distribution of (E ,E ) at t = 4.0ps; the
1 2
solid (dashed) box indicates the range corresponding to the low (high) intensity image. (B) and (C) show the normalized
low-intensity and high-intensity images at t=4.0 ps, whose ratio is shown in (D). (E) shows the ratio at t=0.0ps following
the same procedure, which does not exhibit the ripple-like feature in (D). (F) shows the sum over the ROI indicated by the
dashed red line in (D), plotted against the value of E E /(E +E ) at the two delays. Only bins with at least 5 counts are
1 2 1 2
considered. Red lines show linear fits fixing the intercept to be the average value for t=0.0ps.
number of photons in the pump. In this case, we may Since we have demonstrated that the pump-probe sigwrite ∆I(Q,t;E ,E ) = C(Q,t)E E , where C(Q,t) is nalisnegligiblearoundzerodelay,toincreasethesignal-
1 2 1 2
the pump-probe response coefficient independent of the to-noise ratio, we use the normalized intensity includpulse energies. In this case, the normalized scattered in- ing all valid shots at t = 0.0ps, Inorm(Q,t = 0), as the
tensity, equilibrium diffuse scattering structure factor S (Q), in
0
the absence of the effect of the pump. Using Eq. (2),
I(Q,t;E 1 ,E 2 ) =S (Q)+C(Q,t) E 1 E 2 . (2) thepump-probecoefficientatdelaytisthusbeobtained
E +E 0 E +E from the experimental data set as:
1 2 1 2
We now test the validity of Eq. (2). Using the ex- C(Q,t) (cid:20) Inorm(Q,t) (cid:21)(cid:80) (E(s)+E(s))
tracted pump-probe signal in Fig. 2D, we select a region = −1 s 1 2 [O(t)]−1,
of interest (ROI) with a clear signal, as indicated by the

## S

0
(Q) Inorm(Q,t=0) (cid:80) E(s)E(s)
s 1 2
red dashed line. Fig. 2F shows the summed intensity (3)
within this region, I , normalized by the total pulse where the sum is over all shots s at delay t. Here, O(t)

## Roi

energy E +E , plotted as a function of E E /(E +E ). denotes the correction factor of order unity which ac-
1 2 1 2 1 2
The results for delay t = 4.0ps and 0.0ps are shown as countsforchangesintheoverlapbetweenthetwobeams
blueandgreencircles,respectively,whereeachcirclecor- on the sample during the delay scan due to the aforeresponds to the average over a bin in the histogram in mentioned wobbling motion of the delay scan stages (see
Fig. 2A with at least 5 shots. These data are consistent Appendix B1).
with a linear trend with the same intercept at E E =0, An example of the pump-probe signal, obtained using
1 2
which supports the validity of Eq. (2) and hence the bi- Eq. (3) for t = 7.0ps, is shown in Fig. 3A. The green
linearityofthepump-probesignal. Therefore,theresults line shows the direction q∥G, which coincides with the
verify our expectation that the total lattice distortion is direction of the largest intensity modulation. Along this
proportional to the pump pulse energy. Moreover, while line, we take several q points (indicated by the colored
the data for t = 4.0ps shows a clear slope, the data for dots) and plot the time dependence of the pump-probe
t=0.0appearindependentfromthepulseenergies, con- signalinFig.3B,wherethelabelsindicatethemagnitude
firming the absence of pump-probe signal at zero time q ≡ |q| for each trace. These curves exhibit damped osdelay. cillations, whose frequency increases with increasing q.

<!-- Page 5 -->

5
4

## A

q G
3
q G
2

## G=(112)

1
t=7.0ps
0
]1

## J

[

## )Q(

S/)t,Q(C
0
1.2
1.0
0.8
0.6
0.4
0.2
2 4 6
|q| [10 32 Å 1]
]zHT[
ycneuqerf
0.7

## C

0.6
LA 2nd harmonic
0.5
0.4
0.3
0.2

## La

0.1
0.0
]stinu
.bra[
edutilpma
lartceps
25
20
15
10
5
0
0 2 4 6 8 10
t [ps]
]1

## J

[

## )Q(

S/)t,Q(C
0
B |q|=7.0×10 3 2 Å 1
6.0
5.0
4.0
3.0
2.0
FIG.3. Measuredx-raypump,x-rayprobesignalC(Q,t)/S (Q)inSrTiO . (A)C(Q,t)/S (Q)att=7.0ps. Thegreenline
0 3 0
showsthedirectionQ∥G,whichcoincideswiththedirectionofthelargestintensitymodulation. (B)Thetimedependenceof
C(Q,t)/S (Q) at selected wavevectors q along the red line in (A). The corresponding locations on the detector are indicated
0
as colored dots in (A). An offset is added between traces of different |q| values for clarity; C(Q,t)/S (Q) is zero at t=0. The
0
blacklinesarefitresults,tobediscussedinthe“Model”section. (C)Fouriertransformspectralamplitudesalongthedirection
oftheredlinein(A).TheredandbluelinesshowthedispersionoftheLAphononandtheLAsecondharmonicobtainedfrom
DFT calculations.
The curves do not resemble a perfect sinusoidal func- B. Model
tion but feature flat minima, suggesting the existence of
even-order frequency overtones. With a Fourier trans-
We present a model that is consistent with our obserformation, we obtain the spectral weights along this q
vations and describes quantitatively the time evolution
direction, which are shown in Fig. 3C.
ofthepump-probesignal. Themodelisbasedonthefollowing physical picture. First, the stochastic absorption
The results indicate that the excited modes are pre- of x-ray photons from the pump pulse causes the credominantly LA phonons. Firstly, the direction of the ation of a large number of uncorrelated photoelectrons
strongest modulation (green line in Fig. 3A) coincides and core holes, each of which relaxes generating a caswith the direction q ∥ G, while the modulation van- cade of lower-energy electrons. This process is mostly
ishes in the perpendicular direction, consistent with the complete within 100fs [18], much faster than the period
|Q·ϵ|2 dependence in the scattering intensity where ϵ is of the acoustic phonons that we detect. After this prothephononpolarizationvector. Secondly,weoverlaythe cess,alargenumberofelectroncloudsareformedwithin
spectral weights in Fig. 3C with the LA phonon disper- the sample. These clouds are expected to have a core
sion in the direction q∥G [using v =8.2km/s, which is region, on the order of several nanometers, with a high
calculated by density-functional theory (DFT) along the electrondensity[18,19],whichservesasarandomcollecselected q direction] and its second-harmonic overtone, tionofexcitationcenters. Thehighconcentrationofsecshowing good agreement with the data. ondary photoelectrons about each center leads to a sud-

<!-- Page 6 -->

6
den local stress that produces a propagating strain pulse data in Fig 3C, e−t/τ is a phenomonological decay dein the form of a coherent longitudinal acoustic phonon cay factor added to account for the observed decay of
wavepacket with a typical phonon period given by the the oscillations (see Fig. 3B), and qˆ is the unit vector in
time it takes for sound to propagate across the core re- the direction of q. Here, u˜(q,t) has the unit of length.
gion of the cascade. The [1−cos(qvt)] term is typical of displacive-like exci-
The probability of absorption about any given atomic tation, where the equilibrium position of the lattice sudsite is much less than one and is given by the prod- denly shifts and atoms oscillate around the newequilibuct of the photon fluence and the photoionization cross- rium [20]. We take a common decay time τ, for both
section. For SrTiO at 9.828 keV, it is dominated by the decay of the new equilibrium back to the original
3
absorption on the Sr sites with a mean distance be- equilibrium, and the oscillation amplitude.
tween absorption events on order of 30nm, for 0.5 µJ Since we observe that the modulations of the diffuse
in a 20µm × 20µm spot. This is an order of mag- scattering (see Fig. 3) happen at the regime of relatively
nitude larger than the inverse of the maximum q in small q ≡|q|≪|G|, and we assume that the spatial dis-
Fig.3Awithobservable“ripple”feature,whichisaround tribution of excitation centers is sparse and random, the
1/(5×10−32π˚A −1 ) ≈ 3nm. Therefore, we assume that change in diffuse scattering intensity due to the distortions is derived as for the Huang diffuse scattering due
the interference between strain waves from the individto static defects [21]. Hence the intensity modulation,
ual random photoabsorption events largely averages out.
Furthermore, since x-ray photoabsorption is a stochastic
∆I(Q,t)∝c|G·u˜(q,t)|2E , (5)
process, we assume that the spatial distribution of these 1
excitation centers across the different unit cells is given where E is the probe pulse energy; c ≪ 1 is the con-
1
by a binomial probability distribution. centration (number per unit cell) of excitation centers
Since we measure the incoherent sum of their scatter- that are expected to be proportional to the pump pulse
ing amplitudes (more details below and in Appendix A), energy E . Thus, ∆I(Q,t) is proportional to E E as ex-
2 1 2
it is justified to take the ensemble average limit when pected. The full expression for ∆I(Q,t) considering all
describing the strain generation and propagation. Al- geometric factors is provided in SI. Note that in Eq. (5),
though individual photoelectrons may create anisotropic the term |G·u˜(q,t)|2 gives rise to the angular dependistributions of secondary electrons [19], it is expected dence ∆I(Q,t) ∝ |G · qˆ|2, in agreement with the extobecomesmallby100fs[18],andthedistributionisas- perimental observation in Fig. 3, even for an isotropic
sumed to be isotropic in the ensemble average limit [19]. u˜(q,t) = u˜(|q|,t). The thermal-equilibrium diffuse scat-
Taking into account the arguments above, we build a teringI (Q,t),ontheotherhand,ispresumedtobedom-
0
modelassumingthat: 1)Thepumppulsecreatesanum- inated by thermal phonons, for simplicity. The expresber of excitation centers that are randomly and sparsely sion for thermal diffuse scattering is given in Eq. (A44).
distributedwithintheilluminatedvolume,andthenum- Based on this model, the pump-probe signal is (see
ber of these centers is proportional to the pump fluence. Appendix A for detailed derivations),
2)Aroundeachexcitationcenter,astep-function-like(in
(cid:18) (cid:19)
time) stress field causes a sudden change in the equilib- C(Q,t) =Fσ3 U p e−σ2
2
q2 [1−cos(qvt)]2e−2
τ
t |G·qˆ|2,
rium lattice constant and therefore a sudden strain. We S 0 (Q) U d
assume the excitation is instantaneous compared to the (6)
phonon periods which are on the order of picoseconds wherethepre-factorF takesintoaccount(seeEq.(A65)
(see Fig. 3C), so at t = 0 the atomic displacements are forthefullexpression): geometricfactors(e.g.,thebeam
zero. 3)ThestrainfieldisisotropicandassumesaGaus- size), the x-ray linear absorption coefficient, thermal difsian spatial profile in the ensemble average limit. 4) The fuse scattering background assuming phonon frequencies
strain field can be treated in the continuum limit, since and eigenvectors as obtained from DFT, as well as other
the smallest length scales considered (several nanome- known constants (e.g., x-ray atomic scattering form facters, corresponding to the inverse of the maximum q tors at the given q and photon energy), all of which
range of visible ripples) are still significantly larger than are independent of parameters of the model. Thus, the
the size of the unit cell. Furthurmore for simplicitly, we pre-factor F can be calculated for any given Q. We
approximate the material as elastically isotropic. Under only explicitly write out in Eq. (6) the following terms:
these assumptions, the Fourier transform of the average the time dependence [1−cos(qvt)]2e−2t/τ, the angudisplacement field for a single excitation center is (see lar dependence |G·qˆ|2 (which determines the intensity
Appendix A for detailed derivations): anisotropy of the “ripples” in Figure 3A), the size of the
distortion field σ, and the energy conversion coefficient
u˜(q,t)= iπ3/2Aσ2 e−σ2q2/4[1−cos(qvt)]e−t/τqˆ, (4) U p /U d . Here U d is the absorbed energy density and U p
Vq is the energy density of the launched acoustic phonons,
both defined in the bulk average limit.
where A describes the amplitude of the displacement Using Eq. (6), we fit our model to the experimentally
field, σ is the rms extent of the distortion field, v = measured C(Q,t)/S (Q) to extract the main physical
0
8.2km/s is the velocity of the LA wave obtained from quantities of interest: the size of the distortion field, σ,

<!-- Page 7 -->

7
and the energy conversion efficiency, U /U . The fit is shorter than both the x-ray spot size and the penetrap d
done in the following way: first, we estimate the decay tion depth, pointing to the fact that X-ray excitation
constant τ with the time-dependent C(Q,t)/S (Q), the induces much more localized electron distribution than
0
colorfultracesinFig.3B,assumingthatτ isindependent optical pump and the potentially dramatically different
ofq(i.e.,aglobalestimatetoalltracesinFig.3B).Then, electron-phonon coupling mechanism. The generation
wevarytheparametersσandU /U tobestfitthemodel anddetectionofcoherenthigh-wavevectoracousticwaves
p d
to the data in the q-range from 2 to 7 × 10−3 2π˚A −1 as reported here do not involve engineered interfaces or
inhomogeneities, such as a transducer layer [22–24] or a
along the direction q ∥ G (i.e., the green line cut in
superlattice structure [25–27], which would normally be
Fig.3A)andintheavailabledelayrangefrom0to10ps.
Data at q > 7×10−3 2π˚A −1 are excluded because of required for generation and detection of high-wavevector
acoustic waves using optical pulses.
low signal levels, while data at q < 2 × 10−3 2π˚A −1

### In the case of SrTiO , we find σ = 1.5 nm and

are excluded because of their sensitivity to inaccuracies 3
U /U = 7×10−3. As pointed out in the Model secin q-space calibration and in the modeling of the dif- p d
tion,fromU /U onecanobtaintheproductofthestrain
fuse scattering, which may contain a background from p d
amplitude and concentration of localized excitation censtaticdisorderbesidesthethermaldiffusescatteringconters cA2. If we assume the concentration of excitation
sidered above. The results are presented in Fig. 4, which
sites is equal to the initial density of photoexcited atoms
shows the measured pump-probe signal C(Q,t)/S (Q)
0 (∼1017 cm−3), the amplitude is 0.15 nm corresponding
(colored lines) and fit results (black lines) as a function
to a dilation at the excitation center of ∼10%. Notably,
of q at different delays. The extracted fit parameters
while we find similar results for the oxide perovskites,
are σ = 1.5nm, U /U = 7×10−3, and τ = 12ps for
p d SrTiO and KTaO , we do not detect an observable sig-
SrTiO . The fits are shown as black lines in Fig. 3 A. 3 3
3 nal for the tetrahedral semiconductors GaAs and GaP

### Fig. 4B shows C(Q,t)/S (Q) data on the selected area

0 over a similar q-range. We expect the effective source
of the detector (top row) and model predictions using
sizes to be similar for the materials if they were solely
the fit parameters (bottom row), at delays of 4, 7, and
based on the dependence of the cascade-electron distri-
10ps. Basedonthegeneralagreementbetweenthemodel
butions on the atomic constituents [28]. Moreover, the
predictions and the experimental data, we consider our
concentrations of initial ionization sites should also be
few-parameter model to be robust. Note, however, that
similar based on the photoelectron cross-sections. Thus,
σ is model-dependent, and it may change if one assumes
weestimateanupperlimitforthestrainamplitudetobe
a different form of the source profile other than a Gausabout 30 times smaller than for oxides.
sianone(e.g.,anexponentialdecayprofileinrealspace).
In KTaO , the extracted fit parameters are σ = 2.5nm The dramatic difference in the response between these
3
and U /U = 2×10−3; more detailed results are shown materialsdependsonthemicroscopicdetailsofthestrain
p d
in Appendix C. generationandhowitdependsonthecomplexdynamics
of the relaxation of the highly excited states and how it
couplestothelattice. Intheopticalregime,ultrafastexcitationoflow-energyelectrons(andholes)inopaquema-

## Iv. Discussion

terials leads to coherent strain generation through both
thermoelastic and deformation potential mechanisms. If
It is remarkable that our simple model, which only a similar process were to dominate the x-ray case, the
assumes that spherical strain waves are launched from differences in the material’s properties would also not
random, uncorrelated, and three-dimensionally localized be sufficient to explain the differences. However, the
sources of electrons, reproduces our experimental data detailed spatio-temporal profile of the stress and resuland allows for the quantification of key parameters of tantstrainfieldsdependsnotjustonthethermalexpanthis process, including the localization size σ of strain sion coefficient and deformation potentials, but also on
wavepackets,andthephotonenergyconversionefficiency the electron cooling rate and whether there is significant
U /U into the elastic waves. The model is in stark con- transport across the initial excitation region during the
p d
trast to ultrafast optical excitation in opaque materials sound propagation time[23]. Even in the optical regime,
where the energy absorbed is distributed uniformly over this can reshape the coherent acoustic phonon pulse enthe illuminated area and exponentially along a distance hancing the lower frequency components and suppress-
(ofabsorptionlength)muchshorterthanthewavelength ing the higher ones, as seen for example in x-ray diffracand the beam size that typically leads to an effective tion experiments from photoexcited Ge[29, 30]. In the
1D strain wave propagating into the bulk with charac- x-rayregime,thelengthscalesaremuchsmaller,andthe
teristic wavelength given by the penetration depth. In electron energies are initially much higher, such that the
theall-x-rayexperimentreportedhere,coherentacoustic details of the energy deposition rates and in particular
phononspropagatein3D.Eventhoughtheabsorptionof thecouplingtoplasmonsandpolaronscouldbecomeimthe x-ray on average leads to an exponentially decaying portant given the high polarizability of the oxides. In
density profile into the bulk, the typical wavelength of particular,polaronsfeaturelocalelectron-latticeinteraccoherent acoustic phonons is many orders of magnitude tionsthatmayexplainthehigh-wave-vectorexcitationof

<!-- Page 8 -->

8
40
35
30
25
20
15
10
5
0
2 4 6
|q| [10 32 Å 1]
]1

## J

[

## )Q(

S/)t,Q(C
0
A 10 ps

## B

4
9 ps 4 ps 7 ps 10 ps
3
8 ps
2
7 ps 1
6 ps 0
5 ps 4 ps 7 ps 10 ps
4 ps
3 ps
2 ps
]1

## J

[

## )Q(

S/)t,Q(C 0
4
3
2
1
0
]1

## J

[

## )Q(

S/)t,Q(C
0
FIG. 4. Time-dependence of the pump-probe signal in SrTiO , and its model predictions using fit parameters. (A) The
3
pump-probesignalC(Q,t)/S (Q)alongtheqlinecutinFig.3A,atselecteddelaytimes. Coloredlinesshowtheexperimental
0
data,whileblacklinesarepredictionsbythemodel. (B)C(Q,t)/S (Q)ontheareadetectorcomparedbetweentheexperiment
0
(top row) and the model predictions (bottom row) at t=4,7,10ps.
coherent strain waves [31–33]. per one. The spherical wave packet center concentration
c can indeed be lower than solely determined by the ma-
The average size of the strain field around each exciterial photoabsorption cross-section, due to Auger electation center is linked with the distribution of secondary
tronsfrommultipleelements(e.g.,bothTiandSratoms
electrons and their coupling to the lattice. The spatial
in SrTiO ), re-absorption of fluorescence photons, and
3
distributionisdeterminedbytheenergyandmomentum
ionization by secondary electrons.
relaxationchannelsofthephotoelectronsandAugerelectrons [19, 28, 34–36]. For reference, in SrTiO where Sr Wenotethatcoherentphononscanbeselectivelygen-
3
dominates the photoabsorption, a photoelectron ionized erated with light by spatial patterning of the radiation.
fromSr2sis∼7.6keV,whilethesubsequentAugerelec- One such case is the transient grating (TG) technique
tron is ∼ 1.6 keV [37]. The secondary electron cascade where two crossed laser pulses create a standing wave
initiated by a multi-keV electron is expected on average interference pattern that excites phonons with the same
to have a size on the order of hundreds of nanometers. period. The TG technique has recently been extended
Lower energy electrons, i.e., < 1 keV, are expected to from the optical to extreme ultraviolet (EUV) waveinitiate cascades that end up with a localized secondary lengths[11,43–50]andhasbeenabletoselectivelyexcite
electron distribution with a characteristic size on the or- phonons with wavelength as small as 24nm [11]. With
der of nanometers and a high peak density near the ex- hard x-ray laser pulses, the period of the standing waves
citation center [18, 19, 28, 36, 38]. The former, while can be reduced to well below the sub-1nm scales due to
possessing an extended overall dimension, features more the short x-ray photon wavelength[43, 51]. It has been
localized centers of a few nanometers in size [19]. The suggested that the fundamental limit of the wavelength
latter has a general length scale consistent with our ex- of coherent acoustic phonon generated by such gratings
perimentally measured σ. Therefore, given the inelastic is determined by the inelastic mean free path of elecmean free path of multi-keV electrons is on the order of trons [50, 52] leading to significant signal degradation in
tens of nanometers [39–42], much longer than the exper- the sub-10nm length scales. The results here show that
imentally measured σ, implies that c exceeds the initial during the electronic cascade process, significant phonon
excitation density, and thus our estimate for A is an up- generation can occur at nanometer length scales before

<!-- Page 9 -->

9
the electronic and thermal excitation homogenizes. ACKNOWLEDGMENTS
The authors thank J. B. Hastings for useful discussions. This work was supported by the U.S. Department of Energy, Office of Science, Office of Basic Energy
Sciences through the Division of Materials Sciences and

## V. Conclusion

Engineering under Contract No. DE-AC02-76SF00515.

### Measurements were carried out at the Linac Coherent

In summary, we report hard x-ray generation and Light Source, a national user facility operated by Standetection of high-wavevector, large amplitude coherent ford University on behalf of the U.S. Department of Enacoustic strain pulses in oxide insulators. We anticipate ergy,OfficeofBasicEnergySciencesunderContractNo.
future experiments with higher signal sensitivity and q DE AC02- 76SF00515. Preliminary experiments were
resolution to definitively clarify the speculations above. performed at SACLA with the approval of the Japan
The key is to directly extract σ and A in X-ray-pumped SynchrotronRadiationResearchInstitute(JASRI)(Prosemiconductors. If indeed σ is confirmed to be of simi- posal No.2017B8046) P. Sun acknowledges funding from
lar magnitude as SrTiO , it will support the mechanism theEuropeanUnion’sHorizon2020researchandinnova-
3
of direct local electron-phonon coupling. On the other tionprogrammeundertheMarieSkl(cid:32)odowska-Curiegrant
hand, if σ turns out to be much larger compared with agreement No. 101023787. The participants from MIT
SrTiO , it will prompt a more detailed look at the elec- were supported by the Department of Energy, Office of
3
troniccascadeanddiffusionprocess. Thoughtheelectron Science, Office of Basic Energy Sciences, under Award
cascade upon hard x-ray photoabsorption is relatively Number DE-SC0019126. M.G. and J.M.R. were supwell understood based on simulations [18, 19, 28, 34– ported by the U.S. Department of Energy (DOE) under
36, 38], additional simulations of the electron-phonon Grant No. DE-SC0012375.
couplingtogetherwiththeelectroncascadeprocessafter Y.H., P.S., and S.W.T. contributed equally to this
photoabsorptionofhardx-rayphotonwillgreatlyhelpin work.
understandingthefullprocessofhighq coherentphonon
generation.
The spectral content of the coherent acoustic phonons Appendix A: Derivations for the model
that make up the strain wave is consistent with a large
collection of localized sources of sudden stress with size 1. Spherical wave solution
on the order of a few nanometers. The size is expected
to be determined by the complex dynamics of the high-
Inthissection,wepresentthederivationofthespherienergy electron cascade and is significantly shorter than
calstrainwavemodelwhichisusedinthemaintext. Two
thex-raypenetrationdepth. Theobservedexcitationsite
main assumptions are made. Firstly, we take the contindimension of 1.5nm (in SrTiO ) is significantly shorter
3 uum limit, which is appropriate given that we are conthanthelow-energyelectroninelasticmeanfreepath[39–
sidering lengths scales of tens of nanometers and above,
42,52]. Whileamoresystematicstudyisrequiredtodewhich is large compared with the size of the unit cell.
termine the excitation mechanism of phonons from the

### Secondly,weassumethatthematerialisisotropic,which

x-ray-inducedchargedistribution, thegenerationofhigh
greatly simplifies the mathematical form of the results.
amplitude coherent phonon wavepackets with nm-scale
The second assumption is not strictly true in reality, but
characteristic extent substantiates that high amplitude
the analysis and final results are not significantly influmonochromatic acoustic phonons can be generated with
enced by the anisotropy of the materials, so we keep
sub-10nm scale wavelengths using x-ray transient gratthis assumption. Furthermore, we start the derivation
ings methods, addressing an important length scale for
withoutconsideringdissipation,todemonstratethemain
the thermal transport in modern integrated circuits and
features of the propagating spherical waves (the oscillatits power management.
ing patterns in reciprocal space that are observed in our
The fraction of x-ray energy deposited in acoustic data). At the end of the section, we take into account
waves, U /U on the order of ∼ 10−3 (We obtain that the effects that lead to decay over time.
p d
the energy conversion efficiency U /U ∼ 7×10−3 for In our model, an X-ray photon excitation event leads
p d
SrTiO ,and∼2×10−3forKTaO ),asobtainedfromour to a distortion in the equilibrium position at time t=0.
3 3
model, mayhelpquantifyanenergytransferchannelrel- This distortion is assumed to be spherically symmetric,
evant to radiation damage processes relevant to all FEL and it launches longitudinal spherical waves for t > 0.
based pump-probe measurements for condensed matter Since the material is assumed to be isotropic, the spherphysics. Besidescrystallinematerials,thereportedmeth- ical symmetry is preserved during the wave propagation;
ods will also be beneficial for studying the x-ray-induced in other words, the displacement field in the material afstructuralchangesinamorphousmaterialsonshorttimes tertheexcitation, u(r,t), shouldbecurl-free. Therefore,
scales [53–55]. we may write u(r,t)=∇ϕ(r,t), where ϕ(r,t) is a scalar

<!-- Page 10 -->

10
field which satisfies the wave equation [56]: where qˆ denotes the unit vector in the direction of q.
If one is interested in the distortion in real space, an
1 ∂2
∇2ϕ(r,t)− ϕ(r,t)=s(r)H(t), (A1) inverse spherical Fourier transform can be applied tothe
v2∂t2
results above to obtain:
where v is the longitudinal sound speed and H(t) is the √
πAσ2 (cid:20) (cid:16)r(cid:17) (cid:18) r−vt (cid:19)
Heaviside step function. s(r) represents the distortion
ϕ(r,t)=− 2erf −erf
field of the new equilibrium, whose form is not specified 8r σ σ
at this point. In reciprocal space, Eq. (A1) becomes (cid:18) r+vt (cid:19)(cid:21)
−erf , (A12)
(cid:18) 1 ∂2 (cid:19) σ
− q2+ v2∂t2 ϕ˜(q,t)=s˜(q)H(t). (A2) √ πAσ2 (cid:20) (cid:16)r(cid:17) (cid:18) r−vt (cid:19)
u(r,t)= 2erf −erf
8r2 σ σ
Eq. (A2) is a standard wave equation whose general
(cid:18) (cid:19)(cid:21)
solution for t>0 is r+vt
−erf ˆr
σ
ϕ˜(q,t)=ϕ˜ (q)+F(q)eiqvt+G(q)e−iqvt, (A3)
0

### Aσ (cid:104) (cid:105)

where ϕ˜ 0 (q)=−s˜(q)/q2 is the equilibrium solution, and − 4r 2e−r2/σ2 −e−(r−vt)2/σ2 −e−(r+vt)2/σ2 ˆr,
F(q)andG(q)arearbitraryfunctionsofq. Notethatwe (A13)
have now dropped the dependence on the direction of q
because of spherical symmetry. where
Now we impose the initial conditions that, at t = 0, 2 (cid:90) z
there is no displacement or movement of the atoms: erf(z)≡ √ e−x2 dx (A14)
π
ϕ˜(q,t=0)=0, (A4) 0
(cid:12) is the error function. The terms containing (r −vt)/σ
∂ϕ˜(q,t)(cid:12)
(cid:12) =0. (A5) and(r+vt)/σ representoutgoingandincomingspherical
∂t (cid:12) (cid:12) waves, respectively.
t=0
Thederivationsabovehavenotconsidereddissipation.

### This leads to F(q)=G(q)=−ϕ˜ (q)/2. Hence, the solu-

0 In reality, the equilibrium distortion field s(r) decays totion, Eq. (A3), becomes
gether with the excited electron cloud, and the phonon
ϕ˜(q,t)=ϕ˜ (q)[1−cos(qvt)]. (A6) modes are damped as well. The time scales of these two
0
processes are not necessarily the same, but in this work,
The displacement field in reciprocal space is thus the data is consistent with the two time constants beu˜(q,t)=−iϕ˜ (q)[1−cos(qvt)]q. (A7) ing close to each other. For example, in Fig. 3B in the
0 main text, the experimental data can be described with
The functional form of ϕ is given by the physical an overall exponential decay with time. Therefore, we
0
mechanism that leads to the distortion. In our model, it assume that both processes have the same decay time
isassumedthatthedilatationfield(i.e.,thedivergenceof constant, τ. Thus, we may modify the wave equation,
thedisplacement)ofthenewequilibriumaftertheexcita- Eq. (A2) into the following form:
tion is proportional to the concentration of electron-hole
pairs [57]. The latter is assumed to follow a spherical (cid:18) 2 ∂ 1 ∂2 (cid:19) π3/2Aσ2
Gaussian distribution. Therefore, we may write − q2+ v2τ ∂t + v2∂t2 ϕ˜(q,t)= V e−σ2q2/4e− τ tH(t),
∇·u (r)=∇2ϕ (r)=σ−1Ae−r2/σ2 , (A8) (A15)
0 0 where the term −(2v−2τ−1)(∂ϕ˜(q,t)/∂t) accounts for
where A is the amplitude of the distortion with units phonon damping, and the term e−t/τ accounts for the
of length and σ is the localization size of the electron- decay of the distortion field. The solution of this equahole distribution. With a spherical Fourier transform tion, with the initial conditions (Eqs. [A4, A5]), is
(see more details in the next section), we can obtain, in
reciprocal space, π3/2Aσ2
ϕ˜(q,t)=− e−σ2q2/4
π3/2Aσ2

### V(q2−v−2τ−2)

−q2ϕ˜ 0 (q)= V e−σ2q2/4, (A9) × (cid:20) 1−cos (cid:18) qt (cid:114) v2− 1 (cid:19)(cid:21) e− τ t, (A16)
where V is a normalization volume which we take to be
q2τ2
the volume of the unit cell. Therefore, for t>0, iπ3/2Aqσ2
u˜(q,t)= e−σ2q2/4
π3/2Aσ2 V(q2−v−2τ−2)
ϕ˜(q,t)=− e−σ2q2/4[1−cos(qvt)], (A10) (cid:20) (cid:18) (cid:114) (cid:19)(cid:21)

### Vq2

× 1−cos qt v2−
1
e− τ tqˆ. (A17)
iπ3/2Aσ2 q2τ2
u˜(q,t)= e−σ2q2/4[1−cos(qvt)]qˆ, (A11)
Vq (A18)

<!-- Page 11 -->

11
These results may be simplified under the condition For vectors u(r) = u(r)ˆr and u˜(q) = u˜(q)qˆ, note the
that extra factor of cosθ when projecting onto the direction
of ˆr or qˆ:
q2v2τ2 ≫1, (A19)
1 (cid:90) ∞ (cid:90) π (cid:90) 2π
u˜(q)= r2dr sinθdθ dφu(r)cosθeiqrcosθ
which holds true in our study: for example, with q = V 0 0 0
0.004 × 2π˚A −1 , v = 8970m/s (for SrTiO ), and τ ≈ (A26)
3
10ps, we have q2v2τ2 ≈500. Therefore, we may approx- 4πi (cid:90) ∞
= u(r)[sin(qr)−qrcos(qr)]dr, (A27)
imate the results above with Vq2
0
iV (cid:90) ∞
π3/2Aσ2 u(r)=− u˜(q)[sin(qr)−qrcos(qr)]dq.
ϕ˜(q,t)=− Vq2 e−σ2q2/4[1−cos(qvt)]e− τ t, (A20) 2π2r2 0

## (A28)

iπ3/2Aσ2
u˜(q,t)= e−σ2q2/4[1−cos(qvt)]e− τ tqˆ, (A21)

### Vq


## Energy in the excited strain field

which are simply the solution in the undamped case,
Eqs. [A10, A11], multiplied by the exponential decay The total energy deposited to the LA phonon fields
term e−t/τ. Similarly, the solution in real space is given can be calculated from the momentum-resolved LA disby placements by integrating over all modes. The energy
per mode is
π1/2Aσ2
ϕ(r,t)=− e−t/τ
8r 1 1
(cid:20) (cid:16)r(cid:17) (cid:18) r−vt (cid:19) (cid:18) r+vt (cid:19)(cid:21) W˜(q)= 2 cNmω2(q)|u˜(q)|2 = 2 cNmv2q2|u˜(q)|2,
× 2erf −erf −erf ,
σ σ σ (A29)
(A22) where v is the speed of sound, q is the magnitude of the
wavevector, misthetotalmassofatomsintheunitcell,
π1/2Aσ2
u(r,t)= e−t/τˆr and
8r2
(cid:20) (cid:16)r(cid:17) (cid:18) r−vt (cid:19) (cid:18) r+vt (cid:19)(cid:21) |u˜(q)|= π3/2Aσ2 e−σ2q2/4 (A30)
× 2erf −erf −erf Vq
σ σ σ

### Aσ is the maximum mode displacement at a given wavevec-

− e−t/τˆr tor; see Eq. (A21). Since we take into account an expo-
4r
(cid:104) (cid:105) nential decay in time, W˜(q) thus represents the phonon
×
2e−r2/σ2 −e−(r−vt)2/σ2 −e−(r+vt)2/σ2
,
energy at t = 0. Integrating over all wavevectors and
(A23) dividing by the total volume NV, we obtain the energy
density:
where ˆr denotes the unit vector in the direction of r. 1 V (cid:90) ∞
U = 4πq2dqW˜(q) (A31)
p NV (2π)3
0

## Spherical Fourier transforms = 1 (cid:90) ∞ 4πq2dq· 1 cNmv2q2 (cid:18) π3/2Aσ2(cid:19)2 e−σ2q2/2

8π3N 2 Vq
0
In this section we show the formulae forFourier trans- (A32)
form pairs in spherical coordinates. πcmv2A2σ4 (cid:90) ∞
For scalars ϕ(r) and ϕ˜(q): =
q2e−σ2q2/2dq

## (A33)


## 4V2

0
ϕ˜(q)= 1 (cid:90) ∞ r2dr (cid:90) π sinθdθ (cid:90) 2π dφϕ(r)eiqrcosθ = π3/2 4 c √ m 2 v V 2 2 A2σ . (A34)

## V

0 0 0
4π (cid:90) ∞ The same result can be obtained via calculations in
= ϕ(r)rsin(qr)dr, (A24) real space. Because there is no shear, the elastic energy
qV
0 density of the distortion field is [56]:

### V (cid:90) ∞

ϕ(r)= ϕ˜(q)qsin(qr)dq. (A25)
1
2π2r 0 W = 2 (λ L +2µ L )(ε 11 +ε 22 +ε 33 )2
Again,hereV isanormalizationvolumesothatϕ˜(q)and −2µ L (ε 11 ε 22 +ε 22 ε 33 +ε 33 ε 11 ) (A35)
ϕ(r) have the same units. In general, the value of V is 1
= (λ +2µ )(∇·u)2−2µ (ε ε +ε ε +ε ε ),
arbitrary. For simplicity, in our derivations it is taken to 2 L L L 11 22 22 33 33 11
be the unit cell volume. (A36)

<!-- Page 12 -->

12
where ε are the diagonal elements of the strain X-ray linear attenuation coefficient. Since we work in
11,22,33
tensor; λ and µ are the material’s Lam´e parameters, grazing geometry, let α denote the grazing angle, and β

## L L

which are related to the longitudinal sound speed by the angle of the outgoing wave (see Fig. 5). As in the
m
λ +2µ = v2. (A37)

## L L V

The amplitude profile in q corresponds to the amplitude of the time-independent term in Eq. (A23):
(cid:20) π1/2Aσ2 Aσ (cid:21)
u (r)= erf(r/σ)− e−r2/σ2 ˆr. (A38)
0 4r2 2r FIG.5. Schematicdiagramshowingthegeometricparameters
used in the derivations. Note that the coordinates x,y are
Thuswecaneasilyobtainthestraintensorduetoasingle transverse to the beam axis, while the coordinate z is in the
direction normal to the sample surface.
defect:
du
ε =ε = 0, (A39)
11 rr dr main text, we use Q to denote the scattering wavevec-
ε =ε = u 0, (A40) tor, G the reciprocal lattice vector, and q ≡ Q−G the
22 θθ r deviation from the Bragg peak which corresponds to the
ε =ε = u 0. (A41) phononwavevector. Then,thethermaldiffusescattering
33 ϕϕ r to the first order can be written as [58]:
Therefore, the energy density of the excitations in the
(cid:12) (cid:12)2
system c i N s (cid:90) ∞ I 0 (Q)= ℏ 2 (cid:88) i ω 1 q,i coth (cid:18) 2 ℏ k ω B q T ,i (cid:19)(cid:12) (cid:12) (cid:12) (cid:12) (cid:12) (cid:88) j F j (G) (cid:18) Q· √ ϵ i, m q,j j (cid:19)(cid:12) (cid:12) (cid:12) (cid:12) (cid:12)

### U = 4πr2Wdr

p NV (cid:90) ∞ (cid:90) ∞ dxdy (cid:90) ∞ (cid:18) µz (cid:19)
0
4πc(cid:90) ∞(cid:20) 1 × sinα dzexp − sinβ I e n,
= (λ +2µ )r2(∇·u )2 −∞ −∞ 0

## V 2 L L 0 (A44)

0
(cid:18) (cid:19)(cid:21)
du
− 2µ 2ru 0 +u2 dr where n is the number density of the unit cell, k is

### L 0 dr 0 B

the Boltzmann constant, and T = 300K is the sample
= 4 V πc (cid:20)(cid:90) ∞ 2 m V v σ 2 2 r2A2e−2r2/σ2 dr− (2µ L u2 0 r) (cid:12) (cid:12) ∞ r=0 (cid:21) t a e t m te p nu er a a t t io u n re. of T t h h e e e o x u p t ( g − oi µ n z g / b si e n a β m ) . t T er h m e a su cc m ou (cid:80) nts f i o s r o t v h e e r
0 j
(A42) all atoms in a unit cell; m is the mass of atom j, and
j
the structure factor of atom j is defined as
π3/2cmv2A2σ

## = √ . (A43)

4 2V2 F (G)≡f e−Mje−iG·τj, (A45)
j j
where f
j
is the form factor, e−Mj the Debye-Waller fac-

## Obtaining the energy conversion efficiency

tor, and τ the position of the atom in the unit cell. The
j
(cid:80)
sum isoverallphononmodes; ω istheangularfrei q,i
In this section, we present detailed derivations of how quency and ϵ the eigenvector of phonon mode i. z is
i,q,j
the conversion efficiency (from deposited X-ray energies the penetration depth into the sample (see Fig. 5). I is
e
to phonon energies) can be obtained by fitting the data thescatteringfromasingleelectron; itcanbere-written
with the model described above. The only additional as
assumption is that the term cA2, which describes the
concentration and amplitude of the excitations, is pro- I =Φ (x,y,z)S , (A46)
e inc e
portional to the fluence of the pump pulse at any point
in the sample. As will be shown, this is expected given where Φ (x,y,z) is the total incident fluence at coordiinc
the bi-linearity of the pump-probe signal demonstrated nate (x,y,z), and S is a scattering strength taking into
e
in the main text. account X-ray polarization and detector solid angle; see
We begin by considering the scattering from a single Ref. [58]. Taking into account the spatial profile of the
pair of pump-probe pulses. Assuming that, at the sam- X-ray beams as well as their attenuation in the sample
ple position, the probe and pump beams have transverse giving rise to a factor of exp(−µz/sinα), the equation
fluence profiles Φ (x,y) and Φ (x,y). Let µ denote the above becomes:
1 2

<!-- Page 13 -->

13
(cid:12) (cid:12)2
I 0 (Q)= ℏn 2 S e (cid:88) ω 1 coth (cid:18) 2 ℏ k ω q T ,i (cid:19)(cid:12) (cid:12) (cid:12) (cid:12) (cid:88) F j (G) (cid:18) Q· √ ϵ i, m q,j (cid:19)(cid:12) (cid:12) (cid:12) (cid:12)
i q,i B (cid:12) j j (cid:12) (A47)
(cid:90) ∞ (cid:90) ∞ dxdy (cid:90) ∞ (cid:18) µz µz (cid:19)
× dz[Φ (x,y)+Φ (x,y)]exp − − .
sinα 1 2 sinα sinβ
−∞ −∞ 0
Notingthattheintegralofthefluenceisthepulseenergy, results can be written as:
(cid:90) ∞ (cid:90) ∞ dxdy (cid:90) ∞ (cid:18) µz (cid:19)
∆I(Q,t)≈ n dzcI exp −
sinα e sinβ
(cid:90) ∞ (cid:90) ∞ −∞ −∞ 0
dxdyΦ 1,2 (x,y)=E 1,2 , (A48) (cid:12) (cid:12) (cid:12) (cid:12) 2
−∞ −∞ × (cid:12) (cid:12) (cid:88) F j (G) (cid:12) (cid:12) |G·u˜(q,t)|2 (A50)
(cid:12) (cid:12)
(cid:12) j (cid:12)
(cid:90) ∞ (cid:90) ∞ dxdy (cid:90) ∞
= n dzcS Φ (x,y)
we may re-write Eq. (A47) as sinα e 1
−∞ −∞ 0
(cid:12) (cid:12)2
(cid:18) (cid:19)(cid:12) (cid:12)
µz µz (cid:12)(cid:88) (cid:12)
I (Q)= ℏnS e(E +E ) (cid:88) 1 coth (cid:18)ℏω q,i (cid:19) ×exp − sinα − sinβ (cid:12) (cid:12) (cid:12) j F j (G)(G·qˆ)(cid:12) (cid:12) (cid:12)
0 2µ 1 2 ω 2k T
(cid:12) i q,i (cid:12)2 B × π V 3A 2 2 q σ 2 4 e−σ2 2 q2 [1−cos(qvt)]2e−2 τ t,
×
(cid:12)
(cid:12) (cid:12) (cid:12) (cid:88) F j (G)
(cid:18)

### Q· √ ϵ i, m q,j

(cid:19)(cid:12)
(cid:12) (cid:12) (cid:12)
(cid:18)
1+ s s i i n n α β
(cid:19)−1

## . (A51)

(cid:12) j j (cid:12)
where in the second step we have used the results from

## (A49)

the model, Eq. (A21). Note that here the incident fluence Φ includes only the probe beam, Φ . As meninc 1
tioned above, the effect of the pump pulse on the sample
isreflectedinthetermcA2,whichvarieswiththespatial
As expected, I (Q) is proportional to the summed pulse
0
coordinates(x,y,z)andisassumedtobeproportionalto
energy E +E . As in Eq. (1), we may write I (Q) =
1 2 0
the pump fluence:
S (Q)(E +E ), where S (Q) is independent of E .
0 1 2 0 1,2
(cid:16) µz (cid:17)
The change in diffuse scattering intensity due to the cA2 =κΦ pump =κΦ 2 (x,y)exp − sinα , (A52)
distortions can be derived in a similar way as for the
Huang diffuse scattering due to static defects [21]. The where κ is a conversion coefficient. Thus,
∆I(Q,t)= π3κσ4nS ee−σ2 2 q2 [1−cos(qvt)]2e−2 τ t

### V2q2

(cid:12) (cid:12)2 (A53)
(cid:90) ∞ (cid:90) ∞ dxdy (cid:90) ∞ (cid:18) 2µz µz (cid:19)(cid:12) (cid:12)(cid:88) (cid:12) (cid:12)
× sinα dzΦ 1 (x,y)Φ 2 (x,y)exp − sinα − sinβ (cid:12) (cid:12) F j (G)(G·qˆ)(cid:12) (cid:12) .
−∞ −∞ 0 (cid:12) j (cid:12)
As will be discussed in the section “Overlap correction” define the overlap factor:
below,thebeamprofilesmaychangeduringadelayscan
(cid:90) ∞ (cid:90) ∞
due to motor movements. However, at a given delay, O(t)≡4πσ2 ϕ (x,y)ϕ (x,y)dxdy. (A54)
we may assume that the spatial profiles of the beams b 1 2
−∞ −∞
remain the same for all shots. In other words, we may
write Φ (x,y) = E ϕ (x,y), where ϕ (x,y) do not The prefactor 4πσ2 represents the area of the beam and
1,2 1,2 1,2 1,2 b
vary between shots and (cid:82)(cid:82) ϕ 1,2 (x,y)dxdy =1. Then, we makes O(t) a unitless quantity. σ b represents the size of
the beam and, in case of a Gaussian beam, it is taken to
be the standard deviation of the Gaussian (see the section “Overlap correction” below). Now, we can rewrite

<!-- Page 14 -->

14
Eq. (A53) as: then the summed intensity is
allshots allshots
∆I(Q,t)= 4 π σ 2κ 2V σ4 2 n q2 S µ ee−σ2q2/2[1−cos(qvt)]2e−2t/τE 1 E 2 (cid:88) I(Q,t)=S 0 (Q) (cid:88) (E 1 (s)+E 2 (s))
b s s (A56)
(cid:12) (cid:12)2 allshots
(cid:12) (cid:12)(cid:88) (cid:12) (cid:12) (cid:18) sinα (cid:19)−1 +C(Q,t)O(t) (cid:88) E(s)E(s).
×(cid:12) (cid:12) F j (G)(G·qˆ)(cid:12) (cid:12) O(t) 2+ sinβ . s 1 2
(cid:12) j (cid:12)
(A55) Then, we normalize it by the summed pulse energies:
(cid:44)
As expected, this pump-probe signal is bi-linear in the Inorm(Q,t)≡ (cid:88) I(Q,t) (cid:88) (E(s)+E(s))
pump and probe pulse energies. As in the main text, we 1 2
may write ∆I(Q,t)=C(Q,t)O(t)E E , where C(Q,t) is s s
independent of E . We have also
1
is
2
olated the overlap
(cid:80) E(s)E(s)
1,2 =S (Q)+C(Q,t)O(t) s 1 2 .
correction factor O(t), a purely geometrical effect due 0 (cid:80) (E(s)+E(s))
to experimental conditions, from the physically relevant s 1 2

## (A57)

quantity C(Q,t).
Experimentally, we measure the total intensity As shown in the main text, there is no pump-probe sig-
I(Q,t) = I (Q)+∆I(Q,t) together with the pulse en- nal at t = 0, so the term S (Q) may be replaced by
0 0
ergies E , E for each shot. Let s be the index of a shot, Inorm(Q,t=0). Hence,
1 2
(cid:20) Inorm(Q,t) −1 (cid:21)(cid:34) (cid:88) (E(s)+E(s)) (cid:44) (cid:88) E(s)E(s) (cid:35) [O(t)]−1 (A58)
Inorm(Q,t=0) 1 2 1 2
s s
=C(Q,t)/S (Q) (A59)
0
= 4 π σ 2κ 2V σ4 2 n q2 S µ ee−σ2 2 q2 [1−cos(qvt)]2e−2 τ t (cid:12) (cid:12) (cid:12) (cid:12) (cid:12) (cid:88) F j (G)(G·qˆ) (cid:12) (cid:12) (cid:12) (cid:12) (cid:12) 2 (cid:18) 2+ s s i i n n α β (cid:19)−1 (cid:44)
b (cid:12) j (cid:12)
(cid:12) (cid:12)2
ℏ 2 n µ S e (cid:88) ω 1 coth (cid:18) 2 ℏ k ω q T ,i (cid:19)(cid:12) (cid:12) (cid:12) (cid:12) (cid:88) F j (G) (cid:18) Q· √ ϵ i, m q,j (cid:19)(cid:12) (cid:12) (cid:12) (cid:12) (cid:18) 1+ s s i i n n α β (cid:19)−1 (A60)
i q,i B (cid:12) j j (cid:12)
(cid:12) (cid:12)2
= 2ℏ π σ 2 b 2 κ V σ 2 4 q2 e−σ2 2 q2 [1−cos(qvt)]2e−2 τ t (cid:80) i ω q − , 1 i coth (cid:16) (cid:12) (cid:12) (cid:80) 2 ℏ k ω j B q F , T i j (cid:17) (G (cid:12) (cid:12) (cid:12) (cid:80) )( j G F j · ( qˆ G )(cid:12) (cid:12) ) (cid:16) Q· ϵ √i, m q, j j (cid:17)(cid:12) (cid:12) (cid:12) 2 (cid:32) 1 2 + + s s s s i i i i n n n n α α β β (cid:33) (A61)
(cid:12) (cid:12)2
≈ 4ℏ π σ 2 b 2 κ V σ 2 4 q2 e−σ2 2 q2 [1−cos(qvt)]2e−2 τ t (cid:80)
i
ω
q
−
,
1
i
coth (cid:16) (cid:12) (cid:12) (cid:80)
2
ℏ
k
ω j

## B

q F ,

## T

i j (cid:17) (G (cid:12) (cid:12)
(cid:12)
(cid:80) )(
j

## G F

j
· ( qˆ G )(cid:12) (cid:12) ) (cid:16) Q· ϵ √i,
m
q,
j
j (cid:17)(cid:12) (cid:12)
(cid:12)

## 2 (A62)

whereinthelaststepwehaveusedapproximationsgiven density,U . TheformerissimplyU =µ Φ ,where
p d pe pump
that sinα/sinβ ≪1. µ is the x-ray photoelectric absorption coefficient [1].
pe
The physical quantity of interest is the ratio between Thus, combining Eqs. [A52, A34, A62], we obtain
thedepositedenergydensity, U , andthephononenergy
d

<!-- Page 15 -->

15
(cid:20) Inorm(Q,t) −1 (cid:21)(cid:34) (cid:88) (E(s)+E(s)) (cid:44) (cid:88) E(s)E(s) (cid:35) [O(t)]−1 (A63)
Inorm(Q,t=0) 1 2 1 2
s s
(cid:12) (cid:12)2
= (2 ℏ π σ ) b 2 1 m /2 v µ 2 p q e 2 σ3 (cid:18) U U d p (cid:19) e−σ2 2 q2 [1−cos(qvt)]2e−2 τ t (cid:80)
i
ω
q
−
,
1
i
coth (cid:16) (cid:12) (cid:12) (cid:80)
2
ℏ
k
ω j

## B

q F ,

## T

i j (cid:17) (G (cid:12) (cid:12)
(cid:12)
(cid:80) )(
j

## G F

j
· ( qˆ G )(cid:12) (cid:12) ) (cid:16) Q· ϵ √i,
m
q,
j
j (cid:17)(cid:12) (cid:12)
(cid:12)

## 2 . (A64)

Therefore, by calculating the pump-probe signal in 2. Theangularerrorsoftheexitbeamfromthedelay
Eq. (A63) from experimental data, and fitting it with branch should be sufficiently small so that the two
Eq. (A64), we can extract the localization size σ and the output beams remain focused and overlapped at
conversion coefficient U /U . Specifically, we may define the sample location. Note that in this experiment,
p d
a pre-factor F: with a focal size of 20µm and a focal length of
3.3m, angular errors on the order of 6µrad would
(cid:12) (cid:12)2
F ≡ (2π)1 2µ pe (cid:12) (cid:12) (cid:80) j F j (G)(cid:12) (cid:12) , l t e w a o d b t e o am th s e . complete loss of overlap between the
ℏσ b 2mv2q2(cid:80)
i
ω
q
−
,
1
i
coth (cid:16)
2
ℏ
k
ω

## B

q,

## T

i (cid:17)(cid:12) (cid:12)
(cid:12)
(cid:80)
j

## F

j
(G) (cid:16) Q· ϵ √i,
m
q,
j
j (cid:17)(cid:12) (cid:12)
(cid:12)
2

### Although the planar air-bearing-based mechanism used

(A65) for the linear motion [15] meets the first requirement, it
whichincludes: geometricfactors(e.g.,thebeamsizeand is still difficult to achieve a sub-µrad level straightness
the pump-probe overlap factor), known constants (e.g., required by the second one. On the other hand, the anthex-raylinearabsorptioncoefficient),DFTresults(e.g., gularerrorsoftheseair-bearing-basedlinearmotionsare
phonon mode frequencies), all of which are independent repeatable on the sub-µrad level. Therefore, the followfrom parameters of the model. Thus, the pre-factor F ingcalibrationroutinehasbeenimplementedtopartially
can be calculated for any given q,t and is fixed during correct for the angular errors:
thedatafitting. Wecanthenre-writetheequationabove
as 1. First, we measure changes in the horizontal and
vertical position of the beam due to the angular
(cid:20) Inorm(Q,t) −1 (cid:21)(cid:34)(cid:80) s (E 1 (s)+E 2 (s)) (cid:35) [O(t)]−1 movements during the delay scan. This is done
Inorm(Q,t=0) (cid:80) E(s)E(s) using the high-resolution beam profile monitor at
s 1 2
the sample location.
C(Q,t)
=
S (Q) 2. Then,wecalibratetherelationbetweentheθandχ
0
(cid:18) (cid:19) motionofcrystalC andthehorizontalandvertical
=Fσ3 U p e−σ2 2 q2 [1−cos(qvt)]2e−2 τ t |G·qˆ|2, movementofthebe 4 amatthesamplelocationusing

## U

d the profile monitor.

## (A66)


## Next, we build a lookup table for θ and χ values

and fit the data by tuning the parameters τ, σ, and
to compensate for the angular motion measured in

## U /U .

p d step 1.

## Finally,weperformthedelayscanandateachtime

Appendix B: Additional experimental methods point, using the values of θ and χ in the lookup
table.

## Overlap correction


### ShowninFig.6Aisthemovementofthefocusedbeam

from the delay branch measured at the sample position
The time delay between the two pulses is adjusted via
usingthebeamprofilemonitorwhilethedelayisscanned
two symmetric linear motions in the delay branch which
from −2ps to 10ps after the angular error correction.
change the distance between the inner crystals (i.e., C
1 Limited by the resolution of the θ and χ motions, we
andC inFig.1Ainthemaintext)andtheoutercrystals
4 can only correct the angular errors to some extent. Dur-
(C and C ). In order to perform a continuous scan of
2 3 ing the experiment, the overlap is optimized at the most
the delay, the straightness of the linear stages needs to
negative delay, t = −2ps, so the change in the centroid
meet two requirements:
positioniscalculatedwithrespecttoitspositionat−2ps.

## The orientation errors of the outer crystals caused To calculate the overlap correction factor, O(t), debythislinearmotionshouldbewellbelowtheDar- fined in Eq. (A54), we assume that the two beams are

win width of the Bragg reflection, 17µrad in this both Gaussian in shape. Since the full-width at halfcase, to maintain the photon throughput. maximum (FWHM) of the beams are measured to be

<!-- Page 16 -->

16
10
0
10
)m
(
tfird
diortnec

## A

vertical horizontal
1.0
0.9
0.8
0.7
2 0 2 4 6 8 10
t [ps]
)t(
5
4
3
2

## B

1
0
0 10000 20000 30000
d reading
03

### FIG. 6. (A) Measured drifts in the beam center position as

a function of delay t between the two X-ray pulses after the
overlap correction. The dots are data points at each delay,
which are then smoothed using a Savitzky–Golay filter and
the results are shown as the curves. (B) The overlap correctionfactor,O(t),calculatedwithEq.(B2)usingthevaluesin

## (A).

20µm, the standard deviation of the Gaussian is thus
σ = 8.49µm. Let D denote the distance between the
b
centroids of the two beams. We may choose the coordinate system so that the centroids are located at
(x,y)=(±D/2,0). Hence, the overlap factor is
(cid:34) (cid:35) (cid:90) ∞ (cid:90) ∞ 1 (x+ D)2+y2
O(t)=4πσ2 dxdy exp − 2
b 2πσ2 2σ2
−∞ −∞ b b
(cid:34) (cid:35)
1 (x− D)2+y2
× exp − 2 (B1)
2πσ2 2σ2
b b
(cid:18) D2(cid:19)
=exp − (B2)
4σ2
b

### This factor is calculated and plotted in Fig. 6B and

is taken into account for further analyses on the timeresolved signal.

## Diode calibration

Figure 7 shows the calibration for the diode readings.
Theintensitymonitori ,whichisplacedbeforethesam-
5
ple,iscalibratedseparatelyandthereadingsareinunits
of µJ. We use the reading to calibrate the diodes d
03
and d in the following way: In one scan, we block the
34

## ]J

[
i
5
c =1.420e-04
1
6
4
2
0
0 25000 50000 75000
d reading
34

## ]J

[
d
c
i
30
1
5
102
101
100
c =8.54e-05
2
stnuoc
103
102
101
100
stnuoc
FIG. 7. Diode calibration. Top panel: we obtain the coefficient c which converts d reading (variable-delay branch) 1 03
to pulse energy onto the sample by blocking the fixed-delay
branchandfittingthecorrelationbetweend andi readings.
03 5
Bottompanel: weobtainthecoefficientc whichconvertsd
2 34
reading (fixed-delay branch) to pulse energy onto the sample
byleavingbothbranchesopenandfittingthecorrelationbetween d and i −c d .
34 5 1 03
fixed-delaybranchandobtainthecoefficientc thatcon-
1
verts d reading (i.e., intensity from the variable-delay
03
branch) into i reading, as shown in the top panel of
5
Fig. 7. In another scan, we leave both branches open
and,knowningthecoefficientc ,obtainthecoefficientc
1 2
that converts d reading (i.e., intensity from the fixed-
34
delay branch) into i reading, as shown in the bottom
5
panelofFig.7. Inthisway,wecanobtaintheenergydelivered onto the sample in units of µJ from each branch,
E =c d and E =c d .
1 1 03 2 2 34

<!-- Page 17 -->

17

### Appendix C: Additional data

Figures 8 and 9 present data on KTaO , in the same
3
format as Figs. 3 and 4 in the main text for SrTiO .
3

### Appendix D: Estimated amplitude of strain waves

If we assume that the coupling is only through deformation potential and that one photon creates one spherical wave, then each photon will lead to a uniform electron band shift of the amount ∆E in the excited volume
Ω = NV = 4πσ3. V is the unit cell volume and N is
3 e
the number of unit cells excited. σ is the radius of the
e
electron cloud, which is allowed to be different from σ.
The photon of energy hν injects a number of carriers
∆N = hν/E and leads to a change in the chemical
gap
potential ∆E = ∆NE /N where N the total numgap
ber of unit cells in the excited volume Ω or the number
of electrons within one single band is defined through
Ω=NV = 4πσ3. We then have ∆E = hν. The induced
3 e N
strain is determined by ∆E = Ξε where Ξ is the deformation potential, Therefore, the uniform strain ε, which
is incurred by the incident photon, satisfies the relation
ε = V = 3V . The signal [C(Q,t)/S0(Q)]STO ≈ ε2 STO
hν ΞΩ 4πΞσ
e
3 [C(Q,t)/S0(Q)]GaAs ε2

### GaAs

under a similar scattering geometry, and
ε2

## Sto ≈


## Ξ2


### GaAs

ε2 Ξ2

### GaAs STO

if σ is assumed to be similar in the two materials. Such
e
assumption is not unreasonable because the heaviest elements in these materials are not far off in the atomic
number and we are not hitting X-ray resonance in between their edges.

### Now we consider thermoelastic coupling as the

electron-lattice coupling mechanism. The temperature
rise caused by the absorption of one X-ray photon is
∆T = hν whereC istheheatcapacityinJ/(K·mol),

## Cn/Na

N is the Avocadaro number. Due to thermal expan-

## A

sion, the strain caused by temperature rise is ε = α∆T,
where α is the thermal expansion coefficient. Therefore
ε = αNAV = 3αNAV. Tocompareεinthetwomaterials
hν CΩ 4πCσ3
e
we only need to compare their α/C. [C(Q,t)/S0(Q)]STO ≈
[C(Q,t)/S0(Q)]GaAs
ε ε 2 2 STO = ( ( α α / / C C ) ) 2 2 STO For SrTiO 3 , α = 3.23 × 10−5K−1,

### GaAs GaAs


### C = 98J/(K· mol) [59]. For GaAs, α = 6×10−6K−1,

C = 45 J/(K· mol) [60]. This results in only a factor of
6 larger signal in SrTiO .
3

<!-- Page 18 -->

18
4
A q G
3
q G
2

## G=(112)

1
t=7.0ps
0
]1

## J

[

## )Q(

S/)t,Q(C
0
1.2
1.0
0.8
0.6
0.4
0.2
4 6 8
|q| [10 32 Å 1]
]zHT[
ycneuqerf
0.7

## C

LA 2nd harmonic 0.6
0.5
0.4
0.3
0.2

## La

0.1
0.0
]stinu
.bra[
edutilpma
lartceps
25
20
15
10
5
0
0 2 4 6 8 10
t [ps]
]1

## J

[

## )Q(

S/)t,Q(C
0
B |q|=8.5×10 3 2 Å 1
7.5
6.5
5.5
4.5
3.5
FIG. 8. Measured x-ray pump x-ray probe signal C(Q,t)/S (Q) in KTaO . (A) C(Q,t)/S (Q) at t=7.0 ps. The green line
0 3 0
showsthedirectionq∥G,whichcoincideswiththedirectionofthelargestintensitymodulation. (B)Thetimedependenceof
C(Q,t)/S (Q) at selected wavevectors q along the red line in (A). The corresponding locations on the detector are indicated
0
as colored dots in (A). An offset is added between traces of different |q| values for clarity; C(Q,t)/S (Q) is zero at t=0. The
0
black lines are fit results. (C) Fourier transform spectral amplitudes along the direction of the red line in (A). The red and
blue lines show the dispersion of the LA phonon and the LA second harmonic obtained from DFT calculations.

<!-- Page 19 -->

19
40
35
30
25
20
15
10
5
0
4 6 8
|q| [10 32 Å 1]
]1

## J

[

## )Q(

S/)t,Q(C
0
A 10 ps

## B

4
9 ps 4 ps 7 ps 10 ps
3
8 ps
2
7 ps 1
6 ps 0
5 ps 4 ps 7 ps 10 ps
4 ps
3 ps
2 ps
]1

## J

[

## )Q(

S/)t,Q(C 0
4
3
2
1
0
]1

## J

[

## )Q(

S/)t,Q(C
0
FIG. 9. Fit results for KTaO . (A) The pump-probe signal C(Q,t)/S (Q) along the q linecut in Fig. 8A, at selected delay
3 0
times. Black lines are the simulations, colored lines are the data. (B) C(Q,t)/S (Q) on the detector image (at t=4,7,10ps)
0
are compared between the experiment (first row) and the simulations (second row).

<!-- Page 20 -->

20
[1] A.C.Thomspon,D.T.Attwood,E.M.Gullikson,etal., [10] K. Nass, A. Gorel, M. M. Abdullah, A. V. Martin,
X-raydatabooklet,LawrenceBerkeleyNationalLabora- M. Kloos, A. Marinelli, A. Aquila, T. R. M. Barends,
tory, Univ. California (2001). F.-J. Decker, R. Bruce Doak, L. Foucar, E. Hartmann,
[2] R. F. Egerton, Electron energy-loss spectroscopy in the M.Hilpert,M.S.Hunter,Z.Jurek,J.E.Koglin,A.Koelectronmicroscope (SpringerScience&BusinessMedia, zlov, A. A. Lutman, G. N. Kovacs, C. M. Roome, R. L.
2011). Shoeman, R. Santra, H. M. Quiney, B. Ziaja, S. Boutet,
[3] L.Young,E.P.Kanter,B.Kra¨ssig,Y.Li,A.M.March, and I. Schlichting, Structural dynamics in proteins in-
S. T. Pratt, R. Santra, S. H. Southworth, N. Rohringer, ducedbyandprobedwithx-rayfree-electronlaserpulses,
L. F. DiMauro, G. Doumy, C. A. Roedig, N. Berrah, Nature Communications 11, 1814 (2020).
L. Fang, M. Hoener, P. H. Bucksbaum, J. P. Cryan, [11] L.Foglia,R.Mincigrucci,A.Maznev,G.Baldi,F.Capo-
S. Ghimire, J. M. Glownia, D. A. Reis, J. D. Bozek, tondi,F.Caporaletti,R.Comin,D.DeAngelis,R.Dun-
C. Bostedt, and M. Messerschmidt, Femtosecond elec- can, D. Fainozzi, et al., Extreme ultraviolet transient
tronic response of atoms to ultra-intense x-rays, Nature gratings: A tool for nanoscale photoacoustics, Photoa-
466, 56 (2010). coustics 29, 100453 (2023).
[4] B. Nagler, U. Zastrau, R. R. Fa¨ustlin, S. M. Vinko, [12] D.G.Cahill,W.K.Ford,K.E.Goodson,G.D.Mahan,
T.Whitcher,A.J.Nelson,R.Sobierajski,J.Krzywinski, A.Majumdar,H.J.Maris,R.Merlin,andS.R.Phillpot,
J.Chalupsky,E.Abreu,S.Bajt,T.Bornath,T.Burian, Nanoscale thermal transport, Journal of applied physics
H. Chapman, J. Cihelka, T. Do¨ppner, S. Du¨sterer, 93, 793 (2003).
T. Dzelzainis, M. Fajardo, E. Fo¨rster, C. Fortmann, [13] D.G.Cahill,P.V.Braun,G.Chen,D.R.Clarke,S.Fan,
E. Galtier, S. H. Glenzer, S. Go¨de, G. Gregori, V. Ha- K. E. Goodson, P. Keblinski, W. P. King, G. D. Majkova, P. Heimann, L. Juha, M. Jurek, F. Y. Khat- han, A. Majumdar, et al., Nanoscale thermal transport.
tak, A. R. Khorsand, D. Klinger, M. Kozlova, T. Laar- ii. 2003–2012, Applied physics reviews 1 (2014).
mann, H. J. Lee, R. W. Lee, K.-H. Meiwes-Broer, [14] A. Robert, R. Curtis, D. Flath, A. Gray, M. Sikorski,
P. Mercere, W. J. Murphy, A. Przystawik, R. Redmer, S. Song, V. Srinivasan, and D. Stefanescu, The X-ray
H. Reinholz, D. Riley, G. Ro¨pke, F. Rosmej, K. Saksl, CorrelationSpectroscopyinstrumentattheLinacCoher-
R. Schott, R. Thiele, J. Tiggesba¨umker, S. Toleikis, ent Light Source, Journal of Physics: Conference Series
T.Tschentscher,I.Uschmann,H.J.Vollmer,J.S.Wark, 425, 212009 (2013).
andB.N.etal.,Turningsolidaluminiumtransparentby [15] D. Zhu, Y. Sun, D. W. Schafer, H. Shi, J. H. James,
intensesoftx-rayphotoionization,NaturePhysics5,693 K. L. Gumerlock, T. O. Osier, R. Whitney, L. Zhang,
(2009). J. Nicolas, B. Smith, A. H. Barada, and A. Robert, De-
[5] G. Doumy, C. Roedig, S.-K. Son, C. I. Blaga, A. D. velopmentofahardx-raysplit-delaysystematthelinac
DiChiara,R.Santra,N.Berrah,C.Bostedt,J.D.Bozek, coherent light source (SPIE, 2017) p. 102370R.
P. H. Bucksbaum, J. P. Cryan, L. Fang, S. Ghimire, [16] A. Mozzanica, A. Bergamaschi, S. Cartier, R. Dinapoli,
J. M. Glownia, M. Hoener, E. P. Kanter, B. Kr¨assig, D. Greiffenberg, I. Johnson, J. Jungmann, D. Mali-
M.Kuebel,M.Messerschmidt,G.G.Paulus,D.A.Reis, akal, D. Mezza, C. Ruder, L. Schaedler, B. Schmitt,
N.Rohringer,L.Young,P.Agostini,andL.F.DiMauro, X. Shi, and G. Tinti, Prototype characterization of the
Nonlinear atomic response to intense ultrashort x rays, JUNGFRAUpixeldetectorforSwissFEL,JournalofIn-
Phys. Rev. Lett. 106, 083002 (2011). strumentation 9 (5).
[6] K.Tamasaku,E.Shigemasa,Y.Inubushi,T.Katayama, [17] D. Zhu, Y. Feng, S. Stoupin, S. A. Terentyev, H. T.
K. Sawada, H. Yumoto, H. Ohashi, H. Mimura, Lemke, D. M. Fritz, M. Chollet, J. Glownia, R. Alonso-
M. Yabashi, K. Yamauchi, et al., X-ray two-photon ab- Mori, M. Sikorski, et al., Performance of a beamsorption competing against single and sequential multi- multiplexing diamond crystal monochromator at the
photon processes, Nature Photonics 8, 313 (2014). linac coherent light source, Review of Scientific Instru-
[7] S.Ghimire,M.Fuchs,J.Hastings,S.C.Herrmann,Y.In- ments 85, 063106 (2014).
ubushi,J.Pines,S.Shwartz,M.Yabashi,andD.A.Reis, [18] B. Ziaja, R. A. London, and J. Hajdu, Uni-
Nonsequentialtwo-photonabsorptionfromthekshellin fied model of secondary electron cascades in disolid zirconium, Physical Review A 94, 043418 (2016). amond, Journal of Applied Physics 97, 064905
[8] M. Fuchs, M. Trigo, J. Chen, S. Ghimire, S. Shwartz, (2005), https://pubs.aip.org/aip/jap/article-
M. Kozina, M. Jiang, T. Henighan, C. Bray, G. Nd- pdf/doi/10.1063/1.1853494/14943355/064905 1 online.pdf.
abashimiye, P. H. Bucksbaum, Y. Feng, S. Herrmann, [19] A. Gibrekhterman, A. Akkerman, A. Breskin, and
G. A. Carini, J. Pines, P. Hart, C. Kenney, S. Guillet, R. Chechik, The spatial characteristics of electron-and
S.Boutet,G.J.Williams,M.Messerschmidt,M.M.Seib- photon-inducedsecondaryelectroncascadesinCsI,Tech.
ert, S. Moeller, J. B. Hastings, and D. A. Reis, Anoma- Rep. (P00021073, 1993).
lous nonlinear x-ray compton scattering, Nat Phys 11, [20] H.J.Zeiger,J.Vidal,T.K.Cheng,E.P.Ippen,G.Dres-
964 (2015). selhaus, and M. S. Dresselhaus, Theory for displacive
[9] I. Inoue, Y. Inubushi, T. Sato, K. Tono, T. Katayama, excitation of coherent phonons, Phys. Rev. B 45, 768
T. Kameshima, K. Ogawa, T. Togashi, S. Owada, (1992).
Y.Amemiya,etal.,Observationoffemtosecondx-rayin- [21] P. H. Dederichs, The theory of diffuse x-ray scattering
teractionswithmatterusinganx-ray–x-raypump–probe and its application to the study of point defects and
scheme,ProceedingsoftheNationalAcademyofSciences theirclusters,JournalofPhysicsF:MetalPhysics3,471
113, 1492 (2016). (1973).

<!-- Page 21 -->

21
[22] G.TasandH.J.Maris,Electrondiffusioninmetalsstud- tons, The European Physical Journal D 71, 1 (2017).
ied by picosecond ultrasonics, Phys. Rev. B 49, 15046 [37] T. A. Sasaki, Y. Baba, K. Yoshii, and H. Yamamoto,
(1994). Spectator auger transitions of resonantly-excited sr 2p
[23] C.Thomsen,H.T.Grahn,H.J.Maris,andJ.Tauc,Sur- core-holesinionicstrontiumcompounds,Journalofelecface generation and detection of phonons by picosecond tronspectroscopyandrelatedphenomena79,229(1996).
light pulses, Phys. Rev. B 34, 4129 (1986), publisher: [38] C. Merlet and X. Llovet, Uncertainty and capability
American Physical Society. of quantitative epma at low voltage–a review, in IOP
[24] T. Henighan, M. Trigo, S. Bonetti, P. Granitzka, Conference Series: Materials Science and Engineering,
D. Higley, Z. Chen, M. Jiang, R. Kukreja, A. Gray, Vol. 32 (IOP Publishing, 2012) p. 012016.
A. Reid, et al., Generation mechanism of terahertz co- [39] R.J.Stein,Electrontransmissionmeasurementsofelecherent acoustic phonons in fe, Physical Review B 93, tronmeanfreepathinsupportedthinfilmsfrom1-5keV,
220301 (2016). Surface Science 60, 436 (1976).
[25] P.Hawker,A.J.Kent,L.J.Challis,A.Bartels,T.Deko- [40] F.Salvat,J.D.Martinez,R.Mayol,andJ.Parellada,A
rsy, H. Kurz, and K. Ko¨hler, Observation of coher- simple model for electron scattering: Inelastic collisions,
ent zone-folded acoustic phonons generated by Raman Journal of Physics D: Applied Physics 18, 299 (1985).
scattering in a superlattice, Applied Physics Letters [41] T.Reich,V.Yarzhemski,andV.Nefedov,Calculationof
77, 3209 (2000), https://pubs.aip.org/aip/apl/article- inelasticmeanfreepathofphotoelectronsinsomesolids,
pdf/77/20/3209/7815326/3209 1 online.pdf. Journal of Electron Spectroscopy and Related Phenom-
[26] T.-H. Chou, L. Lindsay, A. A. Maznev, J. S. Gandhi, ena 46, 255 (1988).
D. W. Stokes, R. L. Forrest, A. Bensaoula, K. A. Nel- [42] A. Akkerman, M. Murat, and J. Barak, Monte carlo
son, and C.-K. Sun, Long mean free paths of room- calculations of electron transport in silicon and related
temperaturethzacousticphononsinahighthermalcon- effects for energies of 0.02–200 kev, Journal of Applied
ductivity material, Phys. Rev. B 100, 094302 (2019). Physics 106 (2009).
[27] M.Trigo,Y.M.Sheu,D.A.Arms,J.Chen,S.Ghimire, [43] B.W.Batterman,Effectofdynamicaldiffractioninx-ray
R. S. Goldman, E. Landahl, R. Merlin, E. Peterson, fluorescence scattering, Phys. Rev. 133, A759 (1964).
M. Reason, and D. A. Reis, Probing unfolded acous- [44] M. J. Bedzyk, G. M. Bommarito, and J. S. Schildkraut,
tic phonons with x rays, Phys. Rev. Lett. 101, 025505 X-raystandingwavesatareflectingmirrorsurface,Phys.
(2008). Rev. Lett. 62, 1376 (1989).
[28] V. Lipp, I. Milov, and N. Medvedev, Quantifying elec- [45] C. Svetina, R. Mankowsky, G. Knopp, F. Koch, G. Setroncascadesizeinvariousirradiatedmaterialsforfree- niutinas, B. Ro¨sner, A. Kubec, M. Lebugle, I. Mochi,
electronlaserapplications,Journalofsynchrotronradia- M. Beck, C. Cirelli, J. Krempasky, C. Pradervand,
tion 29, 323 (2022). J.Rouxel,G.F.Mancini,S.Zerdane,B.Pedrini,V.Es-
[29] M. F. DeCamp, D. A. Reis, A. Cavalieri, P. H. Bucks- posito, G. Ingold, U. Wagner, U. Flechsig, R. Follath,
baum,R.Clarke,R.Merlin,E.M.Dufresne,D.A.Arms, M. Chergui, C. Milne, H. T. Lemke, C. David, and
A. M. Lindenberg, A. G. MacPhee, Z. Chang, B. Lings, P. Beaud, Towards x-ray transient grating spectroscopy,
J. S. Wark, and S. Fahy, Transient strain driven by a Opt. Lett. 44, 574 (2019).
dense electron-hole plasma, Phys. Rev. Lett. 91, 165502 [46] J. R. Rouxel, D. Fainozzi, R. Mankowsky, B. Ro¨sner,
(2003). G. Seniutinas, R. Mincigrucci, S. Catalini, L. Foglia,
[30] M. F. DeCamp, D. A. Reis, D. M. Fritz, P. H. Bucks- R. Cucini, F. Do¨ring, A. Kubec, F. Koch, F. Benbaum,E.M.Dufresne,andR.Clarke,X-raysynchrotron civenga, A. A. Haddad, A. Gessini, A. A. Maznev,
studies of ultrafast crystalline dynamics, Journal of syn- C. Cirelli, S. Gerber, B. Pedrini, G. F. Mancini, E. Razchrotron radiation 12, 177 (2005). zoli, M. Burian, H. Ueda, G. Pamfilidis, E. Ferrari,
[31] F. Ellinger, M. Shafiq, I. Ahmad, M. Reticcioli, and Y. Deng, A. Mozzanica, P. J. M. Johnson, D. Ozerov,
C. Franchini, Small polaron formation on the nb-doped M.G.Izzo,C.Bottari,C.Arrell,E.J.Divall,S.Zerdane,
srtio (001) surface, Phys. Rev. Mater. 7, 064602 (2023). M. Sander, G. Knopp, P. Beaud, H. T. Lemke, C. J.
3
[32] X. Hao, Z. Wang, M. Schmid, U. Diebold, and C. Fran- Milne, C. David, R. Torre, M. Chergui, K. A. Nelson,
chini,Coexistenceoftrappedandfreeexcesselectronsin C. Masciovecchio, U. Staub, L. Patthey, and C. Svetina,
srtio , Phys. Rev. B 91, 085204 (2015). Hard x-ray transient grating spectroscopy on bismuth
3
[33] H. O. Jeschke, J. Shen, and R. Valent´ı, Localized versus germanate, Nature Photonics 15, 499 (2021).
itinerant states created by multiple oxygen vacancies in [47] F. Bencivenga, R. Cucini, F. Capotondi, A. Battistoni,
srtio3, New Journal of Physics 17, 023034 (2015). R. Mincigrucci, E. Giangrisostomi, A. Gessini, M. Man-
[34] A. Akkerman and G. Y. Chernov, Monte-carlo calcula- fredda,I.P.Nikolov,E.Pedersoli,E.Principi,C.Svetina,
tion of the electron transmission, reflection, and absorp- P. Parisse, F. Casolari, M. B. Danailov, M. Kiskinova,
tion in solids in the energy range up to 10 kev, Physica and C. Masciovecchio, Four-wave mixing experiments
Status Solidi. B, Basic Research 101, 109 (1980). with extreme ultraviolet transient gratings, Nature 520,
[35] A.AkkermanandA.Gibrekhterman,Comparisonofvar- 205 EP (2015), publisher: Nature Publishing Group, a
ious monte carlo schemes for simulation of low-energy divisionofMacmillanPublishersLimited.AllRightsReelectron transport in matter, Nuclear Instruments and served. SN -.
Methods in Physics Research Section B: Beam Interac- [48] F. Bencivenga, A. Calvi, F. Capotondi, R. Cucini,
tions with Materials and Atoms 6, 496 (1985). R. Mincigrucci, A. Simoncig, M. Manfredda, E. Ped-
[36] A. N. Grum-Grzhimailo, T. Pikuz, A. Faenov, T. Mat- ersoli, E. Principi, F. Dallari, R. A. Duncan, M. G.
suoka, N. Ozaki, B. Albertazzi, S. Pikuz, Y. Inubushi, Izzo, G. Knopp, A. A. Maznev, G. Monaco, S. Di Mitri,
M.Yabashi,K.Tono,etal.,Onthesizeofthesecondary A.Gessini,L.Giannessi,N.Mahne,I.P.Nikolov,R.Paselectron cloud in crystals irradiated by hard x-ray pho- suello, L. Raimondi, M. Zangrando, and C. Masciovec-

<!-- Page 22 -->

22
chio, Four-wave-mixing experiments with seeded free Reports 7, 3962 (2017).
electron lasers, Faraday Discuss. 194, 283 (2016), pub- [54] F. Dallari, A. Martinelli, F. Caporaletti, M. Sprung,
lisher: The Royal Society of Chemistry. G. Baldi, and G. Monaco, Stochastic atomic accelera-
[49] F. Bencivenga, R. Mincigrucci, F. Capotondi, L. Foglia, tionduringthex-ray-inducedfluidizationofasilicaglass,
D. Naumenko, A. Maznev, E. Pedersoli, A. Simoncig, Proceedings of the National Academy of Sciences 120,
F. Caporaletti, V. Chiloyan, et al., Nanoscale transient 10.1073/pnas.2213182120 (2023).
gratings excited and probed by extreme ultraviolet fem- [55] A. Martinelli, F. Caporaletti, F. Dallari, M. Sprung,
tosecond pulses, Science advances 5, eaaw5805 (2019). F.Westermeier, G.Baldi,andG.Monaco,Reachingthe
[50] F. Bencivenga, F. Capotondi, L. Foglia, R. Minci- yieldpointofaglassduringx-rayirradiation,Phys.Rev.
grucci, and C. Masciovecchio, Extreme ultraviolet tran- X 13, 041031 (2023).
sientgratings,AdvancesinPhysics: X8,2220363(2023), [56] D. S. Chandrasekharaiah and L. Debnath, Continuum
https://doi.org/10.1080/23746149.2023.2220363. Mechanics (Elsevier, 1994).
[51] M.J.BedzykandL.Cheng,X-raystandingwavestudies [57] V. E. Gusev and A. A. Karabutov, Laser Optoacoustics
ofmineralsandmineralsurfaces: Principlesandapplica- (American Institute of Physics, New York, 1993).
tions, Reviews in Mineralogy and Geochemistry 49, 221 [58] R. Xu and T. C. Chiang, Determination of phonon dis-
(2002). persion relations by X-ray thermal diffuse scattering,
[52] P.deVeraandR.Garcia-Molina,Electroninelasticmean Zeitschrift fu¨r Kristallographie 220, 1009 (2005).
free paths in condensed matter down to a few electron- [59] D. de Ligny and P. Richet, High-temperature heat cavolts, The Journal of Physical Chemistry C 123, 2075 pacityandthermalexpansionofSrTiO andSrZrO per-
3 3
(2019). ovskites, Phys. Rev. B 53, 3013 (1996).
[53] B. Ruta, F. Zontone, Y. Chushkin, G. Baldi, G. Pintori, [60] V.GlazovandA.Pashinkin,Thermalexpansionandheat
G.Monaco,B.Ruffl´e,andW.Kob,Hardx-raysaspump capacity of gaas and inas, Inorganic materials 36, 225
and probe of atomic motion in oxide glasses, Scientific (2000).

## Tables

**Table (Page 4):**

| A |  |
|---|---|
|  |  |


**Table (Page 5):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | q |  | G |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | q |  |  | G |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | G | = |  | ( | 1 | 1 | 2 |  | ) |  |  |  |
|  |  | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | = |  |  | 7 | . | 0 | p | s |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| L | A |  | 2 | n | d |  | h | a | r | m | o | n | i | c |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | L |  | A |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 16):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  | ntal |
|  |  | vert | ical |  | horizo | ntal |
|  |  |  |  |  |  |  |


**Table (Page 16):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 18):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | A |  |  |  |  |  |  |  |  |  | q |  |  | G |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | q |  |  | G |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | G |  | = |  | ( | 1 | 1 | 2 | ) |  |  |  |  |
|  |  |  | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | = |  |  | 7 | . | 0 |  | p | s |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | L | A |  | 2 | n | d |  | h | a | r |  | m |  | o | n | i | c |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | L |  | A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
