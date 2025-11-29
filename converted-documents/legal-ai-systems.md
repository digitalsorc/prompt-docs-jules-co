---
title: "Legal AI Systems"
original_file: "./Legal_AI_Systems.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["agents"]
keywords: ["proton", "lhc", "ldt", "page", "neutron", "epos", "angantyr", "cid", "sibyll", "qgsjetii"]
summary: "<!-- Page 1 -->

Constraining models of hadronic showers using
proton-Oxygen collisions at the LHC involving
proton/neutron tagging
Michael Pitt
𝑎,𝑏,∗
𝑎Ben-GurionUniversityoftheNegev,DepartmentofPhysics,Beer-Sheva,Israel
𝑏TheUniversityofKansas,DepartmentofPhysics,Lawrence,USA

### E-mail: michael.pitt@cern.ch

The study of hadronic showers, which are produced by cosmic rays penetrating the Earth’s
atmosphere, is essential for shedding light on the origins and characteristics of high-energy
parti"
related_documents: []
---

# Legal AI Systems

<!-- Page 1 -->

Constraining models of hadronic showers using
proton-Oxygen collisions at the LHC involving
proton/neutron tagging
Michael Pitt
𝑎,𝑏,∗
𝑎Ben-GurionUniversityoftheNegev,DepartmentofPhysics,Beer-Sheva,Israel
𝑏TheUniversityofKansas,DepartmentofPhysics,Lawrence,USA

### E-mail: michael.pitt@cern.ch

The study of hadronic showers, which are produced by cosmic rays penetrating the Earth’s
atmosphere, is essential for shedding light on the origins and characteristics of high-energy
particlesoriginatingfromspaceandreachingourplanet. AttheLargeHadronCollideratCERN,
thereareplanstoconductashortrunofproton–oxygencollisionsin2025torefinethemodeling
ofhadronicshowers. Thisworkexploresthepotentialimpactonconstrainingmodelsofhadronic
showersbymeasuringinteractionsfacilitatedbycolor-neutralobjectssuchasphotons,pomerons,
andpions. Theseinteractionsareoftencharacterizedbyhigh-energyprotonsorneutronsproduced
atforwardrapiditiesandcanbetaggedusingdedicatedforwardprotonandneutrondetectors.
XVIIIInternationalConferenceonTopicsinAstroparticleandUndergroundPhysics(TAUP2023)
28.08-01.09.2023
UniversityofVienna
∗Speaker
©Copyrightownedbytheauthor(s)underthetermsoftheCreativeCommons
Attribution-NonCommercial-NoDerivatives4.0InternationalLicense(CCBY-NC-ND4.0). https://pos.sissa.it/
4202
beF
02
]xe-peh[
2v76851.1132:viXra

<!-- Page 2 -->

ConstrainingmodelsofhadronicshowersattheLHC MichaelPitt

## Introduction

A vital component in studying the nature of Cosmic Rays (CRs) is the determination of the
massandenergyspectrabymeasuringprofilesoftheairshowersproducedbytheCRsandmatching
themtoprofilespredictedbyhadronicMonteCarlo(MC)simulations,whichareoftentunedusing
data from the Large Hadron Collider (LHC) [1–4]. Nonetheless, discrepancies between different
model predictions persist, even at LHC energies, leading to large uncertainties in understanding
the composition of CRs [5]. A short run of proton–oxygen (𝑝𝑂) collisions is scheduled during
LHCRun3[6],aimingtoimprovethemodelingofhadronicinteractions. Theprimaryfocusofthe
standardresearchprogramattheLHCwillbeonnon-diffractiveinteractions[7];however,diffractive
interactions, or in general any interaction involving color-neutral objects, can also be explored by
tagging forward protons in 𝑝𝑂 → 𝑝𝑋 interactions or forward neutrons in 𝑝𝑂 → 𝑛𝑋 interactions
(whereXrepresentthedissociationproductsfortheoxygenion),providingauniqueopportunityto
studythosecomponentswithbetterprecision. Figure1illustratesschematicdiagramsofprocesses
ofinterest.
p n
p p

## X 16 O X 16 O

Figure1: Schematicdiagramsof 𝑝𝑂 collisionswithanintactproton(left)oraneutron(right)producedat
veryforwardrapidities.
The color-neutral interactions are weakly constrained at the LHC, resulting in substantial
discrepanciesbetweentheexperimentaldataandthepredictionsofMCsimulations(e.g.,inprotonleadcollisions[8]),suggestingtherearemissinginteractionsnotincludedintheseeventgenerators,
whichcanbefurtherprobedusingforwardneutronandprotondetectors.

## ForwardprotonandneutrondetectorsattheLHC

The ATLAS forward proton (AFP) detector [14] and the CMS-TOTEM Precision Proton
Spectrometer (CT-PPS) [15], deployed during LHC Run 2 (2015–2018) by the ATLAS and the
CMS collaborations, are specialized near-beam detectors located approximately 200 meters from
theinteractionpoint(IP).Thesedetectorswereoperationalthroughoutthestandardhigh-luminosity
runsattheLHCanddeliveredabroadrangeofphysicsresultsprimarilydedicatedtostudyingthe
centralexclusiveproductionprocessesinproton–protoncollisions[9,10].
ThekinematicacceptanceforforwardprotonsiscontingentuponthearrangementoftheLHC
magnetic field. During standard LHC runs, protons that lose 1.5%–15% of their momentum are
consequently deflected from their trajectories into the proton detectors. A similar arrangement
is expected to apply to the upcoming 𝑝𝑂 run, providing the capability to measure the diffractive
componentofthetotal 𝑝𝑂 cross-sectionbytaggingtheintactprotons.
The zero-degree calorimeter (ZDC) is a specialized detector positioned at a zero-degree angle relative to the beamline, substantially contributing to the heavy-ion physics program at the
2

<!-- Page 3 -->


### ConstrainingmodelsofhadronicshowersattheLHC MichaelPitt

LHC [11, 12]. Its primary function is to detect the forward neutral particles produced in the
collisions, primarily spectators from ion disintegration. The ZDC detectors for both ATLAS and
CMS experiments are hosted in a dedicated slot inside the neutral beam absorbers (TAN) at a
distance of 140 meters from the IP, which shields the LHC machine components against neutral
particlesemergingfromtheIP.TheZDCiscapableofdetectingforwardneutronsandphotonswith
pseudorapidities greater than 8.5, and it consists of an electromagnetic section, approximately 30
radiationlengthslong,andthreehadronicmodules,eachabout1.15interactionlengthslong[11].

## NewconstrainsonMChadronicmodels

Colorlessinteractions(includingelastic,diffractive,andpionexchangeprocesses),accounting
for approximately 20% of the total 𝑝𝑂 cross-section, were simulated using different MC event
√
generatorsat 𝑆 = 9.9TeVassuminganintegratedluminosityof 𝐿 = 1𝑛𝑏−1 asitisexpected

### NN int

during the 𝑝𝑂 run in 2025. The typical spectra of forward protons and neutrons are depicted in
Figure 2, suggesting a high event rate within the kinematic range where the discrepancy between
themodelsisobserved.
1011
1010
109
108
107
1000 2000 3000 4000 5000 6000 7000
proton energy [GeV]
nib
/ stnevE
pO, s = 9.9 TeV

## Nn 1011

(cid:242) Ldt = 1 pb-1 EPOS-LHC Pythia8.3 Angantyr
Sibyll 2.3d 1010

## Qgsjetii-04

109
108
107
106
0 0.5 1 1.5 2 2.5 3
proton p [GeV]

## T

nib
/ stnevE
pO, s = 9.9 TeV

## Nn

(cid:242) Ldt = 1 pb-1 EPOS-LHC Pythia8.3 Angantyr
Sibyll 2.3d

## Qgsjetii-04

1011
1010
109
108
107
106
1000 2000 3000 4000 5000 6000 7000
neutron energy [GeV]
nib
/ stnevE
pO, s = 9.9 TeV

## Nn

(cid:242) Ldt = 1 pb-1 EPOS-LHC 1011 Pythia8.3 Angantyr

### Sibyll 2.3d


## Qgsjetii-04 1010

109
108
107
106
0 0.5 1 1.5 2 2.5 3
neutron p [GeV]

## T

nib
/ stnevE
pO, s = 9.9 TeV

## Nn

(cid:242) Ldt = 1 pb-1 EPOS-LHC Pythia8.3 Angantyr
Sibyll 2.3d

## Qgsjetii-04

Figure2: Differentialcross-sectionasafunctionofnucleonenergy(left)andtransversemomentum(right)for
protons(top)andneutrons(bottom),obtainedusingtheEPOS-LHC(magenta),Pythia8Angantyr(yellow),
Sibyll2.3d(green),andQGSJETII-04(blue)MCeventgenerators.
3

<!-- Page 4 -->


### ConstrainingmodelsofhadronicshowersattheLHC MichaelPitt

Interactionsinvolvingcolor-neutralmediatorsarealsocharacterizedbylargegapsintherapidity
distribution of the final-state particles, denoted as Δ𝜂 𝐹. In contrast to non-diffractive inelastic
events, where the probability of finding a continuous rapidity region Δ𝜂 𝐹 that is free of particles
is exponentially suppressed, color-neutral interactions such as those involving pomeron or pion
exchangearedistinctivefortheirapparentrapiditygaps,anddiscriminatingbetweenthesetopologies
(pomeron or pion exchange) is only achievable through proton and neutron tagging. Figure 3
illustrates the contribution from processes, with a proton or a neutron in the acceptance, as a
functionofΔ𝜂 .

## F

108
107
106
105
104
103
0 1 2 3 4 5 6 7 8 9D h

## F

nib
/
stnevE
EPOS-LHC Simulation pO, s = 9.9 TeV

## Nn

(cid:242)
Ldt = 1 nb-1
inclusive

### Proton in the acceptance (e = 2.29% )


### Neutron in the acceptance (e = 12.8% )

Figure 3: Contribution from 𝑝𝑂 → 𝑝𝑋 and 𝑝𝑂 → 𝑛𝑋 interactions with a proton or neutron within the
detectoracceptance. ThepeakintheΔ𝜂 distributioncorrespondstozero-biasevents(i.e.,noparticleswith

## F

an energy above 1 GeV are detected within the pseudorapidity range of |Δ𝜂| < 4.5). Figure adopted from
ref.[13].

## Conclusions

Forward neutron and proton detectors are expected to become increasingly vital during upcoming oxygen collisions, augmenting the scope of the existing physics research program. These
detectors will extend the measured phase space range, which is essential for refining our understandingofcolor-neutralinteractions. Theyarepoisedtoprovidepreciseconstraintsondiffractive
and elastic interactions in proton–ion collisions, including the first measurement of the elastic
componentofproton–oxygeninteractions.

### References

[1] T.Pierog,I.Karpenko,J.M.Katzy,E.YatsenkoandK.Werner,EPOSLHC:Testofcollective
hadronization with data measured at the CERN Large Hadron Collider. Phys. Rev. C 92
(2015)3,034906.
[2] F. Riehn, R. Engel, A. Fedynitch, T. K. Gaisser and T. Stanev, Hadronic interaction model
Sibyll2.3dandextensiveairshowers.Phys.Rev.D102(2020)6,063002.
4

<!-- Page 5 -->


### ConstrainingmodelsofhadronicshowersattheLHC MichaelPitt

[3] S.Ostapchenko,MonteCarlotreatmentofhadronicinteractionsinenhancedPomeronscheme:
IQGSJET-IImodel.Phys.Rev.D83(2011),014018.
[4] C. Bierlich, G. Gustafson, L. Lönnblad and H. Shah, The Angantyr model for Heavy-Ion
CollisionsinPYTHIA8.JHEP10((2018),134.
[5] A.D.Supanitsky,DeterminationoftheCosmic-RayChemicalComposition: OpenIssuesand
Prospects.Galaxies10(2022)3,75.
[6] R. Bruce, R. Alemany-Fernández, H. Bartosik, M. Jebramcik, J. Jowett and M. Schaumann,
StudiesforanLHCPilotRunwithOxygenBeamsProc.IPAC’21,Campinas,SP,Brazil,May
2021,pp.53–56.
[7] Brewer, JasmineandMazeliauskas, AleksasandvanderSchee, Wilke, OpportunitiesofOO
and 𝑝OcollisionsattheLHC.CERN-TH-2021-028
[8] CMSCollaboration.FirstmeasurementoftheforwardrapiditygapdistributioninpPbcolli-
√
sionsat 𝑠 =8.16TeV.Phys.Rev.D108,(2023)9,092004.

## Nn

[9] A. Sopczak, Overview of ATLAS Forward Proton (AFP) detectors in Run-2 and outlook for
Run-3analyses.arXiv:2307.09780[hep-ex].
[10] C. Royon, Recent results from the CMS Proton Precision Spectrometer. arXiv:2307.05321
[hep-ph].
[11] O. Surányi, A. Al-Bataineh, J. Bowen, S. Cooper, M. Csanád, V. Hagopian, D. Ingram,
C.Ferraioli,T.GrassiandR.Kellogg,etal.PerformanceoftheCMSZeroDegreeCalorimeters
inpPbcollisionsattheLHC.JINST 16,(2021)5,P05008.
[12] ATLASCollaboration.Evidenceforlight-by-lightscatteringinheavy-ioncollisionswiththe
ATLASdetectorattheLHC.NaturePhys.13,(2017)9,852-858.
[13] M. Pitt, Reducing model uncertainties using proton-oxygen collisions with proton/neutron
taggingattheLHC,PoSICRC2023,426(2023).
[14] L.Adamczyketal.,TechnicalDesignReportfortheATLASForwardProtonDetector.CERN-
LHCC-2015-009,ATLAS-TDR-024.https://cds.cern.ch/record/2017378
[15] CMS and TOTEM Collaborations, CMS-TOTEM Precision Proton Spectrometer. CERN-
LHCC-2014-021 ; TOTEM-TDR-003 ; CMS-TDR-013 https://cds.cern.ch/record/
1753795
5

## Tables

**Table (Page 3):**

| pO, s = 9.9 TeV nib NN 1011 / stnevE (cid:242) Ldt = 1 pb-1 EPOS-LHC Pythia8.3 Angantyr Sibyll 2.3d 1010 QGSJETII-04 109 108 107 1000 2000 3000 4000 5000 6000 7000 proton energy [GeV] | pO, s = 9.9 TeV 1011 nib NN / stnevE (cid:242) Ldt = 1 pb-1 EPOS-LHC Pythia8.3 Angantyr 1010 Sibyll 2.3d QGSJETII-04 109 108 107 106 0 0.5 1 1.5 2 2.5 3 proton p [GeV] T |
|---|---|
| pO, s = 9.9 TeV nib NN 1011 / stnevE (cid:242) Ldt = 1 pb-1 EPOS-LHC Pythia8.3 Angantyr Sibyll 2.3d 1010 QGSJETII-04 109 108 107 106 1000 2000 3000 4000 5000 6000 7000 neutron energy [GeV] | pO, s = 9.9 TeV nib NN 1011 / stnevE (cid:242) Ldt = 1 pb-1 EPOS-LHC Pythia8.3 Angantyr Sibyll 2.3d 1010 QGSJETII-04 109 108 107 106 0 0.5 1 1.5 2 2.5 3 neutron p [GeV] T |


**Table (Page 3):**

| EPOS-LHC Ldt = 1 pb-1 Pythia8.3 Angantyr Sibyll 2.3d QGSJETII-04 |
|---|
|  |


**Table (Page 3):**

| Ldt = 1 pb-1 |
|---|
|  |


**Table (Page 3):**

| EPOS-LHC Ldt = 1 pb-1 Pythia8.3 Angantyr Sibyll 2.3d QGSJETII-04 |
|---|
|  |


**Table (Page 3):**

| Ldt = 1 pb-1 |
|---|
|  |


**Table (Page 4):**

| (cid:242) Ldt = 1 nb-1 |  |
|---|---|
| inclusive Proton in the acceptance (e = 2.29% ) Neutron in the acceptance (e = 12.8% ) |  |
|  |  |


**Table (Page 4):**

|  |
|---|
|  |
