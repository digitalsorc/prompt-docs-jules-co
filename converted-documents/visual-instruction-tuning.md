---
title: "Visual Instruction Tuning"
original_file: "./Visual_Instruction_Tuning.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "react", "evaluation", "multimodal"]
keywords: ["data", "talys", "energy", "cross", "nuclear", "mev", "were", "default", "sheets", "was"]
summary: "<!-- Page 1 -->

Measurement of Proton-Induced Reactions on Lanthanum from 55–200 MeV by

### Stacked-Foil Activation

Jonathan T. Etienne Vermeulen1
1Los Alamos National Laboratory, Los Alamos, NM 87545, USA
2Brookhaven National Laboratory, Upton, NY 11973, USA
3University of California, Berkeley, Berkeley, CA 94720, USA
4Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA
(Dated: February 29, 2024)
Cerium-134 is an isotope desired for applications as a chemical analogue to the promi"
related_documents: []
---

# Visual Instruction Tuning

<!-- Page 1 -->

Measurement of Proton-Induced Reactions on Lanthanum from 55–200 MeV by

### Stacked-Foil Activation

Jonathan T. Morrell,1 Ellen M. O’Brien,1 Michael Skulski,2 Andrew S. Voyles,3 Dmitri
G. Medvedev,2 Veronika Mocko,1 Lee A. Bernstein,4,3 and C. Etienne Vermeulen1
1Los Alamos National Laboratory, Los Alamos, NM 87545, USA
2Brookhaven National Laboratory, Upton, NY 11973, USA
3University of California, Berkeley, Berkeley, CA 94720, USA
4Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA
(Dated: February 29, 2024)
Cerium-134 is an isotope desired for applications as a chemical analogue to the promising therapeutic radionuclide 225Ac, for use in bio-distribution assays as an in vivo generator of the shortlived positron-emitting isotope 134La. In the 50–100 MeV energy range relevant to the production
of 134Ce by means of high-energy proton bombardment of lanthanum, existing cross section data
are discrepant and have gaps at important energies. To address these deficiencies, a series of 17
139La foils (99.919% natural abundance) were irradiated in two stacked-target experiments: one at
the Los Alamos National Laboratory’s Isotope Production Facility (IPF) with an incident proton
energy of 100 MeV, and a second at Brookhaven National Laboratory’s Brookhaven Linac Isotope
Producer (BLIP) with an incident proton energy of 200 MeV — a complete energy range spanning
approximately 55–200 MeV. Cross sections are reported for 30 products of 139La(p,x) reactions
(representing up to 55% of the total non-elastic cross section), in addition to 24 residual products measured in the natCu and natTi foils that were used as proton flux monitors. The measured
production cross sections for 139La reactions were compared to literature data as well as default
calculationsfromthenuclearreactionmodelingcodesTALYS,EMPIREandALICE,aswellasthe
TENDL-2023library. Thedefaultcalculationstypicallyexhibitedpoorpredictivecapability,dueto
thecomplexityofmultipleinteractingphysicsmodelsinthisenergyrange,anddeficienciesinpreequilibrium reaction modeling. Building upon previous efforts to evaluate proton-induced reactions
inthisenergyrange,aparameteradjustmentprocedurewasperformedupontheopticalmodeland
the two-component exciton model using the TALYS-2.0 code. This resulted in an improvement in
139La(p,x) cross sections for applications including isotope production, over default predictions.
I. INTRODUCTION 3.234 (7) h 209Pb [4–8]. Having a characteristic range of
50–100 µm in human tissue, these emitted alpha particleshaveahighlikelihoodofkillingcancerouscellswhile
Protonacceleratorsoperatingintheapproximately10– sparingnearbyhealthytissue,providedasufficientlyspe-
200 MeV energy range are advantageous for the produc- cificcancer-targetingvector. Oneexampleofapromising
tion of radioisotopes having characteristics of simultane- vector is PSMA-617 (prostate-specific membrane antious high activity and high specific activity, i.e., having a gen), which has shown efficacy (defined as a decrease
high ratio of the desired radionuclide to “cold” (stable) in prostate-specific antigen, or PSA, serum concentraimpurities. These characteristics are generally advanta- tionof≥50%)in66%ofpatientsafflictedwithadvanced
geous to the field of nuclear medicine for the creation (metastatic)prostatecancer,accordingtoarecentmetaof radiopharmaceuticals used in the diagnosis and treat- analysis [9].
ment of various diseases, such as cancers. For example,
one such radionuclide we are interested in producing is An important aspect of treatment planning in tar-
134Ce,whichhasapplicationsasapositron-emittingana- geted radionuclide therapy is the ability to assay the
logue of the therapeutic isotope 225Ac. bio-distributionoftheinjectedradiopharmaceutical,typically with clinical positron-emission tomography (PET)
Actinium-225isanalpha-emittingradionuclidethatis scanners [10]. Unfortunately, 225Ac lacks positron emiscurrently under study for the treatment of various forms sions in any of its decay products, negating the possiof cancer, such as advanced prostate cancer and acute bility of performing such scans directly. Instead, the
myeloid leukemia [1–3]. With a half-life of 9.9203 (3) therapeutic targeting vector must be radiolabeled with
days, 225Acquicklydecaysto 209Bithroughtheemission a positron-emitting chemical analogue of actinium. Reof four 5–8 MeV α particles and two β− particles, with cent studies have demonstrated the ability of 134Ce to
the longest-lived intermediate decay product being the act as a PET imaging surrogate for drug conjugates in-
4202
beF
72
]xe-lcun[
1v39871.2042:viXra

<!-- Page 2 -->

2
corporating 225Acforlong-termtumortargeting[11–13]. Thesedatawereusedtoqualitativelyassessthepredic-
Cerium-134 decays with a half-life of 3.16 (4) days to tions of various nuclear reaction modeling codes, as well
134La (T = 6.45 (16) min), which emits a positron astodeterminehowwellthefittingproceduredeveloped
1/2
in approximately 64% of decays [14]. Therefore, 134Ce, in Fox et al. for the existing lanthanum data set (previacting as a chemical analogue to actinium, serves as an ously extending only up to 90 MeV) extrapolated to the
in-vivo generator of the positron-emitter 134La. new100–200MeVmeasurements[21]. Whiletheextrapolationwasgenerallybetterthanthedefaultpredictions,
Cerium-134 could be produced by proton accel- there was considerable room for improvement, which we
erators using natural targets of lanthanum, cerium, performed with an optimization of selected preequilibpraseodymium, neodymium or even samarium, however rium and optical model parameters using the TALYS-
the (p,6n) reaction on 139La (99.9119% natural abun- 2.0 code [22]. As part of this optimization procedure
dance) is generally predicted to have the highest 134Ce we compared various optimization algorithms, figure-ofyield of these options. The 140Ce(p,7n)134Pr production merit weighting procedures, and sensitivities for various
routeistheoreticallyinterestingbecauseitcouldproduce TALYS parameters. These results arevital to improving
134Ce with a higher radiopurity than using a lanthanum the quality of nuclear data evaluations for these hightarget; however, the ≈11 min half-life of 134Pr is too energy charged particle reaction pathways.
short for practical radiochemical separations, which may
take several hours to days [14]. By this time, the product 134Cewouldbechemicallyindistinguishablefromthe
target material, and therefore the separation would be II. EXPERIMENTAL METHODS AND

## Materials

impossible.

### Currently available cross section data for the

139La(p,6n)134Ce reaction extends from approximately Inthiswork,anumberofproton-inducednuclearreac-
50–90 MeV [15–17]. However, there are only two data tion cross sections were measured using the stacked-foil
points above 70 MeV, where the peak of the cross sec- activationmethod. Thesemeasurementswereperformed
tion is expected, and the three available data sets are as part of a Tri-lab collaboration between Los Alamos
generallydiscrepantbeyondtheirreportederrormargins, NationalLaboratory(LANL),BrookhavenNationalLableading to calls for improvements in these data [18]. The oratory (BNL) and Lawrence Berkeley National Laboraprimary goal of this study was to address these discrep- tory (LBNL). Two sets of foils were irradiated: one at
ancies with additional measurements in the 55–100 MeV the LANL Isotope Production Facility (IPF) with an inenergyrange,aswellastoextendthedatasetwithmea- cident proton energy of 100 MeV, and a second at the
surements up to approximately 200 MeV, which would BNL Brookhaven Linac Isotope Producer (BLIP) with
characterize the preequilibrium tail for the 134Ce prod- 200 MeV protons. We will be referring to these irradiauct. Thiswasdoneusingthestacked-foilactivationtech- tions as the “LANL stack” and the “BNL stack” respecnique, in which a set of thin foils are simultaneously ir- tively.
radiated with a proton beam, such that the beam loses
energyasitpassesthrougheachfoilinthestack[19,20].
By measuring the induced radioactivity for each foil in

### II.1. Stack Design and Irradiations

the stack, the radionuclide production cross sections can
be inferred as a function of proton energy. One benefit
of this technique is that while the experiment was de-

### In the stacked-foil (sometimes called stacked-target)

signed around the measurement of the (p,6n) cross secactivation method, a set of thin foils are arranged in a
tion, many more radionuclide production cross sections
“stack” and irradiated with charged particles: protons
couldbesimultaneouslydetermined. Inthisexperiment,
in this case. As the proton beam traverses each suc-
30 distinct reaction channels were observed in the lancessive foil in the stack, its average energy is degraded
thanum targets, comprising an estimated 55% of the tovia stopping interactions within the foils, such that each
tal non-elastic cross section (based on the TENDL-2023
foil is activated at a slightly lower proton energy than
non-elasticcrosssection),withanadditional24products
measuredinthe natCuand natTifoilsusedasprotonflux the foil preceding it. Each foil was paired with multiple
“monitor” foils, which served as a measure of the beam
monitors. This represents the most extensive measurecurrent and energy at each point in the stack. In our
ment of proton-induced reactions on lanthanum to date,
experiment, additional “degraders” made of thick pieces
and the first measurement above 100 MeV. The resultof aluminum or copper were used to further decrease the
ing data set provides an exquisite sensitivity to the nuenergy between each set of foils. Following a stacked-foil
clear reaction processes relevant to the formation of the
irradiation,theproton-inducedreactionproductscreated
associated radionuclides, such as preequilibrium particle
ineachfoilareassayedviagammaspectrometry. Theasemission.
sayedproductionratesforeachisotope,R ,arerelatedto
i
thefoil’sarealdensity,ρr,theaverageprotoncurrent,I ,
p

<!-- Page 3 -->

3
and the cross section for the production of each isotope,
σ according to
i
R =(ρr)I σ (1)
i p i
where the standard units for R , ρr, I and σ are
i p i
s−1, atoms·cm−2, s−1 andcm2, respectively. Usingthis
equation, the reaction cross section can be calculated so
long as the beam current and areal densities are wellknown. This is often referred to as the “thin-target”
activation equation [19, 20]. It is based on the assumption that both the proton current and the cross section
are approximately constant within the foil — which can
only be the case for foils thin enough such that their energy degradation is much less than the incident proton
energy. An additional feature of these experiments is
FIG. 1: Photo of an individual lanthanum foil sealed in
in the determination of proton beam currents, I , using
p Kapton polyimide tape, and secured to the acrylic
“monitor” foils, rather than external diagnostics such as
frame before the irradiation.
a Faraday cup — the use of which is precluded by the
physical layouts of both the IPF and BLIP irradiation
stations. This monitor foil method relies upon the activation of thin foils having well-characterized “monitor γ-ray spectrometry background in the form of 1.368 and
reaction” cross sections, and using Eq. 1 to calculate I 2.754 MeV photo-peaks and associated Compton scatp
using a known value of σ . tering events [19, 24]. The mounting frames were also
i
machined out of acrylic, for this same reason.

### Ourexperimentconsistedoftwoseparateirradiations:

one stack of ten lanthanum foils irradiated at the LANL The LANL stack made use of natural titanium and
IPF with 100 MeV protons, and a stack of seven lan- copperasmonitorfoils,observingthe 46Scand 48Vmonthanum foils irradiated at the BNL BLIP with 200 MeV itor reaction products in titanium and 62Zn, 65Zn, 56Co
protons. The lanthanum foils used in this experiment and 58Co in copper. In the BNL stack, aluminum was
were identical for both irradiations, all of at least 99% usedinsteadoftitanium, wherethe 22Naand 24Namonpurity by metals basis, purchased from Goodfellow Cor- itor channels were observed. All of these foils were cut
poration (Coraopolis, PA 15108, USA). These consisted from sheets of 25 µm nominal thickness into approxof natural (i.e., non-enriched) lanthanum metal, which imately 25.4 mm squares, which were also measured,
is constituted of 99.9119% 139La and the remainder of weighed and mounted to their frames in Kapton tape
138La [23]. Each foil had a nominal thickness of 25 µm in a similar manner as described for the lanthanum foils.
andwasapproximately25.4mmsquare. Oxidationofthe Forbothstacks,onemonitorfoilofeachmaterialwascolanthanummetalwasminimizedbyhandlingthefoilsin- irradiatedwitheachlanthanumfoil,suchthattherewere
side of a glove box with an inert (dry argon) cover gas. 20 monitor foils irradiated in the LANL stack and 14 in
Figure 1 shows a typical preparation of one of the lan- the BNL stack. The respective metals-basis purities for
thanum foils used in the experiment. Slight oxidation the titanium, copper and aluminum monitor foils used
can be seen along the lower edge of the foil, however, in this experiment were 99.95%, 99.99% and 99.999%,
oxidation in the beam-strike area (center) was minimal respectively.
prior to irradiation.

### The degraders used in the LANL stack were made

Priortoirradiation,thedimensionsandmassesofeach from110-Copperalloysheetsfordegraders1–4and6065-
of these foils were measured in the argon-filled glovebox, Aluminum alloy sheets for degraders 5–9, with thickwith a 1–2% accuracy in the areal density. The foils nesses ranging from approximately 0.6–1.5 mm. The
were then suspended in the center of a plastic mount- BNL stack made use of 110-Copper degraders, machined
ing frame, sealed between two pieces of 3M 5413-Series from plates ranging between 3.7–5.1 mm in thickness.
Kapton polyimide film tape, which consist of a 25 µm Each degrader was also carefully measured and weighed
polyimide backing material and a ≈ 43 µm layer of to determine its areal density. Finally, a stainless steel
acrylic adhesive. The adhesive was specifically chosen “profile monitor” foil was placed in front of and beto be free of silicon, which under proton bombardment hind each stack, with a nominal thickness of 100 µm.
has been shown to lead to the production of 24Na: a The purpose of these foils was to be used as a postcontaminantthatwouldinterferewiththe 27Al(p,x)24Na irradiation check of the beamspot entering and exiting
monitorreactionchannel,andalsoproduceanunwanted thestack,bymappingtheinducedactivationprofilewith

<!-- Page 4 -->

4
radiochromic film (Gafchromic EBT3). For both irradi- rentreadingsrecordedatafrequencyofapproximately20
ations, the profile monitor foils confirmed that the beam timesperminute. Theresolutionofeachcurrentmonitor
was well-contained within the approximately 25 mm by was 1 nA, and the beam current was stable over the du-
25 mm area of the foils, in the center of the stack. The ration of both irradiations with an RMS fluctuation less
complete specifications of both BNL and LANL stacks than 3 nA. The measurements of the inductive pickup
can be found in Appendix B. current monitors agreed quite well with the current determined using the monitor foils in the first (highest-
Since both IPF and BLIP are high-power production energy) compartment. However, scattering and absorpfacilities with water-cooled irradiation stations that are tion of protons within the stacks themselves caused the
onlyaccessibleremotely,andrequirethatallmaterialsbe beam current to drop as the beam traversed the stack.
introduced into a hot cell and handled with telemanipulators, a specially designed sample irradiation box was
required for both irraditions. It was critical that this
sample irradiation box was leak tight, as the lanthanum
foils would rapidly oxidize if exposed to the cooling wa- II.2. Gamma Spectrometry
ter. This had the added benefit of significantly minimizingsurfacecontaminationonthefoils. PhotosofthetargetboxesusedintheLANLandBNLirradiationscanbe Following each irradiation the target boxes were reseeninFig. 2,withredarrowsindicatingthedirectionof trieved from each respective hot cell, and the foils were
theincidentbeam. Bothtargetboxeswererelativelysim- separatedandplacedintoindividualplasticbagsmadeof
ilarindesign. Theywerebothmachinedfromaluminum, 50 µm thick polyethylene in order to prevent the spread
with a cutout in the front to minimize the thickness of of radioactive contamination during the gamma-ray asthe entrance window, and both had a water-tight seal say. Thetimebetweenend-of-bombardmentandthefirst
provided by an aluminum lid (not pictured) that bolts count of the lanthanum foils was approximately 2 hours
to the top of the box. In both cases, the experimental at LANL and 1 hour at BNL, which meant the product
foils in each compartment between degraders — La, Cu with the shortest half-life that was independently meaand Ti for LANL and La, Cu and Al for BNL — were suredwas132mLa,withahalf-lifeof24.3(5)min[25]. The
bundledtogetherintopacketsusingbalingwire,toaidin gamma counting process had differences between each
sample retrieval with hot cell telemanipulators after the site, but in general, short, initial counts were taken at
irradiation. the respective production facilities to capture the shortlivedproducts,afterwhichthefoilsweretransferredtoa
secondaryon-sitecountinglaboratorywherethegammaray background was lower. All gamma-ray assays were
performed using mechanically cooled High-Purity Germanium (HPGe) detectors.
At LANL, the first counts of the lanthanum foils were
performed using an ORTEC GEM p-type coaxial HPGe
detector (model GEM20P-PLUS), at a distance ranging
from 35–44 cm from the entrance window of the detector. These counts ranged in duration from 2–4 minutes,
with the five highest-energy foils being counted twice,
and the five lowest-energy foils being counted once. Following this, all the foils were transferred to a secondary
on-site counting laboratory — internally referred to as
“TarDIS” — which houses two ORTEC GEM p-type
FIG. 2: Photos of the experimental target boxes used in
coaxial HPGe detectors (model GEM20P4-70-PL). All
the LANL (left) and BNL (right) irradiations.
of the three detectors described utilize transistor-reset

### Individual foil packets can be seen bundled together

preamplifiers, which allowed for count rates of approxiwith wire, for ease of manipulation inside of the hot
mately 3 kHz at a dead-time of approximately 5%, while
cells. The red arrows indicate the orientation of the
still maintaining good energy resolution (approximately
incident proton beam.
1.85 keV FWHM at 1.33 MeV). At the TarDIS counting lab, the count plan was to cycle all of the foils be-
Both stacks were irradiated with a nominal beam cur- tweenbothdetectorsovera45dayperiod,withthecount
rent of 200 nA for a duration of 1 hour, 6 seconds at lengthincreasingfrom10minutesatthebeginningofthe
LANL and 1 hour, 1 minute at BNL. The LANL irra- period to 24 hours at the end. However, one of the two
diation took place on 13 September, 2022 and the BNL detectorssufferedanelectronicmalfunctionafterapproxirradiation took place on 17 March, 2023. Both facilities imately 36 hours, and was replaced with the GEM20P-
utilized an inductive pickup current monitor, with cur- PLUS that had been used previously at the IPF loca-

<!-- Page 5 -->

5
tion. Initially the foils were counted 45 cm from the generate the response functions (energy, resolution and
detector face, and were gradually brought closer in as efficiency)foreachdetector[26]. CURIEwasalsousedto
they decayed, to as close as 10 cm. The same Eckert calculateproductionratesforeachproductisotopebased
& Ziegler source set was used to calibrate all three de- on the peak fits in each foil. For the monitor foils, these
tectors, which consisted of 152Eu, 133Ba, 137Cs and 60Co productionrateswereusedtocalculatethebeamcurrent
sealed point sources, of known activity (provided by the witnessedbyeachfoil,andCURIEwasusedtodetermine
manufacturer) with a listed 95% confidence interval of the proton energy distributions within each foil. These
±3%. calculatedprotonenergieswerethenrefinedusingavarianceminimizationprocedure. Finally,thebeamcurrents
At BNL, two ORTEC GEM p-type coaxial HPGe de- from the monitor foils were used to calculate the residtectors were used for the initial lanthanum foil counts at ualnuclideproductioncrosssectionsfromtheproduction
theBLIPfacility—onehavingatransistor-resetpream- rates measured in the lanthanum foils, according to Eq.
plifier and another having a standard charge-sensitive 1. The uncertainties in the reported cross sections are
preamplifier. Eachofthe7lanthanumfoilswerecounted attributable to: statistical and systematic uncertainties
once on each detector, for approximately 10 minutes per from the peak fits, uncertainties in isotope half-lives and
count, at a distance of 62 cm on the charge-sensitive de- decaygammabranchingratios,uncertaintiesinthemeatector and 45 cm on the transistor-reset detector. Lead suredfoilarealdensity,systematicuncertaintiesfromthe
shielding was used to minimize the environmental back- production rate determination, uncertainty in the evaluground in the detector, however the samples were suf- ated monitor cross sections, and uncertainty in the deficiently far from the lead shielding so as to avoid sub- tector efficiency.
stantial Compton-scattered background and lead x-rays.

### After the BLIP counts, the foils were transferred to a

separate on-site counting laboratory, where three p-type
HGPe detectors were utilized for gamma counting: an III.1. Calibration and Peak Fitting

### ORTECIDM-200-V,anORTECTrans-SPEC-DX-100T,

and an ORTEC GEM20P4-70-PL. The IDM and Trans-
SPEC utilize charge-sensitive preamplifiers, while the The analysis of the measured gamma-ray spectra was
GEM20P4 makes use of a transistor-reset preamplifier. performed using the CURIE python library. The detec-
The lanthanum foils were preferentially counted on the torresponsefunctionsconsistedofenergy,resolutionand
transistor-reset detector for the sake of improved statis- efficiency calibrations which were determined from a set
tics, however each lanthanum, copper and aluminum foil of calibration standards of known activity, as described
was counted on every detector to minimize the potential in Section II.2. This procedure was performed for each
ofsystematiceffectsarisingfromanysingledetector. The detector, at every distance that was used to count the
foil-to-detectorcountingdistancesvariedfrom10–59cm, experimental foils. Because the BNL foils were counted
dependingonthedetector,thefoilbeingcountedandthe at BNL and LANL, with two different sets of calibration
decaytime. TheBLIPandon-sitedetectorswereallcal- sources used between them, a cross-calibration was peribrated using the same source set: 152Eu, 133Ba, 137Cs, formedtoensurethedetectorefficiencieswereconsistent
60Co, and 241Am point sources procured from Eckert & between the two sites. The calibration functions for the
Ziegler, with a listed 95% confidence interval of ±3%. energyandresolutioncalibrationwerequadraticandlin-
After 7 days of counting at the BNL on-site counting ear, respectively, whereas the efficiency function used by
laboratory, the foils were shipped to the TarDIS labo- CURIE consists of a semi-empirical “physical” efficiency
ratory used in the LANL irradiation, where they were model, based on the work of Vidmar et al. [27].
counted on the two ORTEC GEM20P4-70-PL detectors
for an additional 35 day period, at a distance of 10 cm. The main advantage of using such a model for the ef-
The calibration source set was the same as previously ficiency is in its ability to extrapolate well to energies
described for that location. above which calibration data are available, as demonstrated in Fig. 3. The black, dashed line shows the
original fit to the efficiency data which were taken from
the calibration sources, for which the photopeak energy
ranged from 53.1622 keV (a minor line in 133Ba) to a
III. DATA ANALYSIS maximum energy of 1528.1 keV, from 152Eu [28, 29].
However, the gamma spectra collected from the experimentalfoilsextendedashighasthe3009.645keVgamma
Theresidualnuclideproductioncrosssectionswereex- line in 56Co, well above the highest calibration energy
tracted from the measured gamma-ray spectra in a con- [30].
sistent manner for both irradiations. The open-source
CURIE python library was used for isotope identifica- To correctly estimate the detector efficiencies above
tion and to extract the number of measured counts from approximately1500keV,anextrapolationprocedurewas
each photopeak in the measured spectra, as well as to performed from the spectra collected during the exper-

<!-- Page 6 -->

6
10 1
0 500 1000 1500 2000 2500
Photon Energy (keV)
)%(
ycneiciffE
not be resolved due to issues such as interference from
Original Data neighboring lines. However, certain isotopes share decay
Original Fit gammas of the exact same energy, for example 132mLa
Extrapolated Data and 132gLa, which both decay into 132Ba and therefore

### Extrapolated Fit

haveanumberofidenticallines. Inthesecases,theoverlapping peaks were excluded in favor of isolated decay
gammas from those isotopes. Fig. 4 also illustrates the
advantage of using a semi-automated peak fitting code
like CURIE for the analysis, as the spectrum is clearly
very complex and contains too many individual gamma
lines for identifying and/or fitting individual peaks to
be practical. In total, the entire data set (comprised of
spectra from both irradiations) contained approximately
75,000 individual peak fits from 644 gamma spectra.

### III.2. Production Rate Determination

FIG. 3: Comparison of “physical” efficiency model fit to
original efficiency data taken from the calibration
sources (black, dashed line), versus the fit to efficiency
The production rates were determined for each indidata that was extrapolated from the experimental foil
vidual isotope by first using the number of counts, N ,
measurements (red, solid line). c
from each observed photopeak, and calculating the corresponding number of decays according to:
iment, using isotopes having decay gammas both below
1500 keV (known efficiency) and above 1500 keV (un-

### N t

known efficiency). The high-energy efficiency was esti- N = c real (2)
mated by multiplying the known low-energy efficiency D I γ ϵ(E γ )t live
by the appropriate ratios of I and measured photopeak
γ
counts. Examplesofisotopeswithgammaemissionsboth
where I is the gamma branching ratio, ϵ(E ) is the
aboveandbelow1500keVthatwereusedinthisextrapo- γ γ
lation are 133mCe, 129mBa, 132La and 56Co. This extrap- detector efficiency at energy E γ , and t real and t live are
therealandlivetimesofthedataacquisitionsystem,reolation is also shown in Fig. 3 as red points, with the
spectively. Thesedecaysareassociatedwithagivenstart
solidredlineindicatingafittoboththecalibrationdata
and stop time, t and t . The CURIE library im-
(blackpoints)andtheextrapolateddata(redpoints). As start stop
plements the general solution to the Bateman equations
can be seen, the original calibration (dashed black) exfor radioactive production and decay [33], and solves for
trapolated very well to higher energy. This would likely
theproductionratesofanynumberofisotopesinadecay
not have been the case for a log-polynomial fit to the
chain(originatingfromthesameparentradionuclide)by
same data.
taking advantage of the fact that the Bateman solutions
Minorcorrectionfactorswereappliedtotheefficiency, are additive, and converting the problem into a linear
withageometrycorrectionfactoraccountingforthefact system of the form:
that the experimental “source” (activated foil) was not
a perfect point source, but rather a distributed source
over the beam-strike area. An additional correction fac-

## M¯ ·R⃗ =N⃗ (3)

tor accounted for attenuation through the Kapton tape D
and polyethylene encapsulation, as well as within the
foils themselves (self-attenuation). The attenuation corwhereN⃗ isavectorofobserveddecaysforallisotopes
rection factors were derived from the XCOM library of D
in the chain, R⃗ is a vector of production rates, and M¯ is
photon attenuation coefficients [31, 32]. These correca matrix of decays calculated from a decay chain of unit
tions were generally quite small, with the largest geometry correction being 0.35% and the largest attenuation production rates for a single isotope in R⃗, during the
correction being 7.91%. interval t start to t stop of the associated element of N⃗ D .

### While CURIE only implements this approach for decay

An example of a collected γ-ray spectrum with peaks chainswithasingleparentisotope,thismethodologywas
fit using the CURIE code can be seen in Fig. 4. In extended to work for multiple decay chains feeding the
general, the resolution of the HPGe detectors was quite same isotopes, which was required in this work to fit the
good, such that there were very few peaks which could A=132 and A=133 decay chains.

<!-- Page 7 -->

7
105
104
103
102
200 400 600 800 1000 1200
Photon Energy (keV)
)1

### Vek(

stnuoC
131La 133La
132Ce 135Ce
132La 135La
133m1Ba 137Ce
133Ce 137m1Ce
133m1Ce
FIG. 4: Example of a gamma-ray spectrum with peaks identified and fit using CURIE – from the first lanthanum
foil in the LANL stack, irradiated with approximately 91.3 MeV protons. This spectrum was collected
approximately 4 hours after the end-of-bombardment.

### An example of this fit to the A = 133 decay chain

is shown in Fig. 5, which fit the production rates of
133mCe, 133gCe, 133Laand 133mBa. While 133gBaislikely
also independently produced, it was not quantified with
sufficientsensitivitytodistinguishitsindependentlyproduced activity from in-feeding from the other isotopes.
Such an approach is very necessary in this case, as both
133mCe and 133gCe decay into 133La (i.e., 133La has two
parentisotopes),andallisotopesinthissystemfeedinto
133gBa. Therefore, there is neither a simple equation for
calculating the production rate of a given isotope from
measured activities, nor for calculating the measured activities from the number of observed decays.
106
105
104
103
102
101
100
100 101 102 103
Time (h)
)qB(
ytivitcA

### Thehalf-livesandmajorgammabranchingratiosused

for each of the isotopes observed in this study are listed
in Tables X and XI in Appendix C. The uncertainties
in the half-lives and gamma branching ratios were used
in the determination of the uncertainties in production
rates, however in general these were much smaller than
the systematic uncertainties associated with the gamma
counting process.
One additional feature of this data set was the presence of secondary (mostly thermal) neutrons, resulting from spallation reactions in the stack, and subsequent thermalization in the surrounding cooling water.
This could potentially inflate our determination of reaction rates through (n,x) reactions resulting in the same
product. Conveniently, we were able to use the 140La
133m1Ce (T 1/2 = 1.67855(12) d) product, resulting from neutron
133Ce capture on the lanthanum foils, as a neutron flux mon-
133La itor [34]. This was used in combination with a FLUKA
133m1Ba Monte Carlo simulation to determine the neutron flux
133Ba
profile throughout the stack [35], showing that only the
64Cu production rate in the copper monitor foils had
a non-negligible contribution from secondary neutrons
(fromthecapturereactionon 63Cu). Thiseffecthasbeen
corrected for in the reported cross sections.

### III.3. Beam Currents and Energy Determination


### The proton beam currents witnessed by each foil in

each of the two irradiated stacks were determined us-

### FIG. 5: Example of a fit to the A=133 decay chain in

ing a set of monitor foils, which have well-characterized
a lanthanum foil irradiated with approximately 160
reaction channels that are included in the list of beam
MeV protons at BNL.
monitor reactions from the IAEA charged-particle cross

<!-- Page 8 -->

8
section database for medical radionuclide production
220
[36]. This method is well described in other publications
[19, 21], and has some advantages and disadvantages
compared to other methods of measuring beam current.
200
The main disadvantage is that the accuracy of the mea- LANL
sured cross sections cannot exceed that of the monitor
62Zn
65Zn
reaction cross sections, and in particular, any unknown 180
56Co
systematic errors in the monitor cross sections will be 58Co
applied (proportionally) to the measured cross sections. 46Sc
However, these effects can be mitigated by using multi-

## 160 48V

ple monitor reaction channels in multiple foil materials,
50 60 70 80 90 100
andbycomparingthemonitorfoil-derivedbeamcurrents
tobeamcurrentsdeterminedbyelectronicmeasurement, BNL 56Co
such as an inductive-pickup current monitor. The main 58Co 62Zn
22Na 65Zn
advantageofthismethodisthatitcancorrectlyaccount
250 24Na
forbeamcurrentlosseswithinthestack,whichwouldnot
be observable with an electronic beam current monitor.
Also, issuessuchaselectronsuppressionorothersources 200
of “dark current” do not impact the measurement.

### The beam current for an individual monitor channel 150

is calculated from a measured production rate, R i , using 100 120 140 160 180 200
Eq. 1 where the cross section used is the flux-averaged Proton Energy (MeV)
cross section:
(cid:82)∞
σ(E)ψ(E)dE
σ¯ = 0 (4)
(cid:82)∞
ψ(E)dE
0
whereσ(E)istherecommendedcrosssectionfromthe

### IAEAbeammonitorlibrary[36], andψ(E)istheproton

flux calculated using a 1-D Monte Carlo stopping power
code implemented in CURIE, which uses the Anderson
& Ziegler formalism for stopping powers [26, 37]. This
treatmentaccountsforthebeamstragglingwhichoccurs
towards the back of the stack. This was particularly significant for the BNL data set, which was degraded from
200MeVincidentenergydowntojustunder100MeVin
the rear foil.
Themeasuredbeamcurrentsfromeachreactionchannelasafunctionofprotonenergywerecompiledforboth
stacks, and fit with a linear function (I = I +m·E)
0
for the BNL stack and a square-root function (I =
√
I +m· E−45) for the LANL stack. The measured
0
per-channelbeamcurrentsandattendingfitscanbeseen
inFig. 6,withtheLANLstackshownintheupperpanel
and the BNL stack shown in the lower panel.

### OnecomplicationfortheBNLstackwasthatonlythe

27Al(p,x)22Naand natCu(p,x)58Coreactionshaverecommended cross sections above 100 MeV, despite many experimental measurements in this energy region for the
productionof 24Na(from 27Al)and 56Co, 62Znand 65Zn
(from natCu), which were all observed reaction products in the monitor foils, and have IAEA-recommended
cross sections below 100 MeV. To improve the quality
of the beam current determination for the BNL stack,
)An(
tnerruC
maeB

### FIG. 6: Beam currents measured in each of the 6

monitor reaction channels utilized by the LANL stack
(top) and BNL stack (bottom). The black line on each
plot indicates a fit to the calculated beam currents as a
function of energy.
a down-selected set of experimental data were used to
generate monitor reaction cross sections in this energy
region. This was done by performing a regression of
thefollowing3-parameterlog-polynomialfunctiontothe
down-selected cross section data:
(cid:16)c
σ(E)=σ + 1 ln(E−60)2

## 100 E

c c (cid:17)
+ 2 ln(E−60)+ 3 (E−100) (5)

## E E

whereσ istheIAEA-recommendedcrosssectionfor
100
thatchannelat100MeV,andc ,c andc areadjustable
1 2 3
parameters. This functional form was selected to ensure
that the fitted cross section agreed with the IAEA evaluationat100MeV.Theresultingfitstotheseadditional
monitorchannelscanbeseeninAppendixA.Therewere
significant discrepancies between our apparent cross sections and the natCu(p,x)58Co IAEA reference cross sections, which may indicate the need for future study of
this channel [36].

### The energy distributions predicted by the Anderson-

ZieglercalculationinCURIEwereadjustedusinga“varianceminimization”methodology,similartothemethods
described in Graves et al. and Voyles et al. [19, 20]. In

<!-- Page 9 -->

9
this approach, a multiplier to the areal densities of all
stack elements (∆ρ), as well as the incident energy (E )
0
aretreatedasfreeparameters, andarevariedinorderto
minimizeagoodness-of-fitparameter: inthiscasethereduced χ2 (or χ2). The purpose of this is not to presume
ν
that the densities of the stack elements or the incident
energy were not well-known, but rather to correct for
unaccountedsystematicsinthecalculationofthe proton
energy spectra. A plot showing the calculation of the χ2
ν
for variation of ∆ρ and E for the LANL stack can be
0
seen in Fig. 7. For the LANL stack, the optimum E
0
and ∆ρ were found to be 99 MeV and -6.65%. For the

### BNLstack,only∆ρwasoptimizedusingthismethod,as

there was not sufficient sensitivity of χ2 to the incident
ν
energy. The resulting optimum density change for the
BNL stack was found to be +1.75%.
0.700
0.675
0.650
0.625
0.600
0.575
0.550
0.525
10 8 6 4 2 0
Density Variation (%)
2
decudeR
The results are shown in comparison to previous measurementsfromT´ark´anyietal.,Morrelletal. andBecker
et al. [15–17]. In general, the results show good agreement with previous measurements. Interestingly, the
134Ceproductioncrosssectionabove100MeVwasmuch
larger than expected, which could have implications for
medical isotope production applications. This work representsthefirstmeasurementofproton-inducedreactions
on lanthanum above 100 MeV, as well as the first measurement of many of these reaction products. Notably,
theobservationof 130Cerepresentsthefirstmeasurement
of an exclusive (p,10n) excitation function (i.e., a cross
section curve measured at multiple energies, including
the threshold) in this energy range.

### In addition, we compare our results to the TENDL-

2023 evaluation, as well as default predictions from
TALYS-2.0, EMPIRE-3.2.3, and ALICE-20 [22, 38–40].
A complete description of the default models used by

### E0 = 98.0 (MeV)

E0 = 98.5 (MeV) each of these codes that are relevant to intermediate-
E0 = 99.0 (MeV) energy proton-induced reactions can be found in Fox et
E0 = 99.5 (MeV) al. [21]. The relevant differences are in the optical mod-

### E0 = 100.0 (MeV)

els (Koning-Delaroche in TALYS and EMPIRE versus

### E0 = 100.5 (MeV)

E0 = 101.0 (MeV) Becchetti-Greenlees in ALICE), the level density models
(CT Fermi gas in TALYS, enhanced GSM in EMPIRE,
and shell-dependent Kataria-Ramamurthy in ALICE) as
wellasthedefaultpreequilibriummodels. TALYSimplements a two-component exciton model, which has been
parameterized with a global fit to emission spectra for

### A ≥ 24 and incident energies between 7 and 200 MeV

[41]. The default preequilibrium model in EMPIRE is

### PCROSS,amoresimplisticone-componentexcitonmodel,

whileALICEmakesuseoftheHybridMonte-CarloSimulation(HMS)precompounddecaymodel. Additionally,
the treatment of angular momentum in ALICE is gener-
FIG. 7: Reduced χ2 of the fit to the LANL monitor foil
allypoorerthantheothertwocodes,whichtendstolead
data, plotted as a function of degrader density variation
toinaccurateisomericratiopredictions. Overall,allthree
and incident proton energy.
codesstruggledtopredictmanyofthemulti-particle-out
channels, which would seem to indicate a deficiency in
the preequilibrium models used by these codes. A selected parameter adjustment using the TALYS-2.0 code
wasperformedinthiswork,whichisdescribedinSection
IV. RESULTS AND DISCUSSION V, and the results are shown here for comparison.
The cross sections for the products observed in this
work were calculated from the measured production
rates, R , the areal densities (ρr) and monitor-foil de- IV.1. 139La(p,6n)134Ce Cross Section
i
rived beam currents I , using Eq. 1. The uncertainties
p
in the cross sections were calculated as the quadrature
sum of the uncertainties from these three sources. The Cerium-134isachallengingisotopetoquantify,dueto
results of these measurements are tabulated in Table I its relatively weak gamma-emission probability, with the
for the 139La products, Table II for products in the cop- 0.209(15)%, 130.4 keV gamma being the strongest emisperfoils,andsimilarlyinTableIIIfortitaniumproducts. sion [14]. Because the 134Ce production cross section is
Theresultsforselectedreactionchannelsthatareofpar- generallyquitehighintheenergyregionexploredinthis
ticularinterestformedicalapplicationsorfromanuclear work,itisnotthecountingstatisticsthatareachallenge.
reaction modeling perspective are discussed below. Rather, it is the fact that in this photon energy range
thereisasignificantComptonbackgroundformosttypes
ofHPGedetectors,includingthoseusedinthismeasure-

<!-- Page 10 -->

10
TABLE I: Summary of lanthanum cross sections measured in this work. Subscripts (c) and (i) indicate cumulative
and independently measured cross sections, respectively. The subscript (m+) indicates the cross section includes
contributions from one or more isomers of the same product isotope, but is otherwise independent of feeding from
other products. Uncertainties are given in the least significant digit, i.e., 188.4(21) means 188.4±2.1, etc.
139La(p,x) Production cross sections (mb)
E (MeV) 188.3(21) 172.8(22) 158.5(23) 143.2(25) 127.9(27) 113.1(29) 96.7(33) 91.3(11) 86.1(11)
p
81.7(11) 77.8(12) 73.7(12) 70.0(13) 66.9(13) 64.1(14) 61.1(14) 58.0(15) -
139Ce 4.04(28) 4.53(28) 5.02(30) 5.52(28) 6.18(40) 6.49(26) 7.66(46) 7.96(27) 8.14(29)
(m+)
8.89(30) 8.49(31) 9.48(33) 9.61(34) 11.28(38) 10.86(39) 11.55(40) 12.33(49) -
137mCe 14.53(55) 16.90(61) 18.28(67) 20.59(73) 23.82(85) 26.75(99) 31.4(13) 34.0(12) 36.9(12)
(i)
39.9(14) 40.4(14) 44.9(16) 47.6(16) 54.4(19) 56.7(19) 60.0(21) 67.3(24) -
137gCe - 5.3(13) 5.26(84) 3.9(18) 7.5(20) 4.8(22) - 13.4(18) 13.5(13)
(i)
11.5(27) 14.3(31) 18.0(37) 21.0(23) 22.9(36) 24.0(28) 22.6(27) 27.2(39) -
136Cs 0.506(31) 0.490(28) 0.431(23) 0.388(19) 0.321(18) 0.255(17) 0.176(12) 0.1038(75) 0.101(23)
(m+)
0.097(18) 0.150(67) - 0.229(62) 0.131(30) 0.134(16) 0.093(12) 0.082(20) -
135La 86.3(54) 121.4(91) 104.3(84) 121.2(74) 136.3(87) 162(12) 161(14) 134.5(87) 147(11)
(i)
141.8(83) 139.5(94) 141(10) 139(11) 149(12) 145(12) 140(12) 140(11) -
135Ce 24.73(91) 28.3(10) 31.6(11) 35.8(12) 44.7(15) 52.0(18) 67.0(25) 76.8(25) 85.0(28)
(m+)
97.1(31) 103.3(34) 129.3(42) 157.8(52) 208.3(68) 256.6(84) 319(10) 410(14) -
135mBa 17.42(71) 18.18(71) 17.00(61) 16.59(61) 15.91(61) 15.01(63) 12.64(50) 11.51(61) 11.33(69)
(i)
8.76(34) 8.48(45) 6.44(48) 7.96(63) 6.12(71) - - - -
134Ce 30.2(23) 35.1(28) 35.2(20) 39.9(16) 49.5(20) 62.2(25) 87.0(35) 97.9(34) 118.2(40)
(i)
151.5(51) 181.3(59) 239.4(78) 265.2(87) 285.9(94) 244.0(80) 179.8(61) 107.4(41) -
133La 106.0(38) 119.7(41) 124.8(42) 145.7(49) 164.7(56) 169.1(59) 169.5(64) 187.6(60) 183.1(59)
(i)
130.8(42) 88.7(28) 57.6(18) 24.56(78) 12.62(40) 4.41(14) - - -
133mCe 16.49(59) 18.48(64) 21.81(73) 27.08(90) 37.5(13) 45.6(16) 73.2(27) 110.6(35) 123.6(40)
(i)
133.0(42) 98.4(31) 67.0(21) 30.91(99) 11.02(35) 2.540(82) 0.500(16) - -
133gCe 3.32(12) 3.75(13) 4.72(16) 5.45(18) 7.15(24) 9.04(32) 14.17(53) 19.84(64) 23.25(74)
(i)
25.03(80) 20.79(66) 14.81(47) 8.26(26) 2.982(95) 0.640(21) - - -
133mBa 20.97(75) 20.98(72) 20.34(68) 19.64(65) 18.28(62) 15.25(53) 10.53(39) 10.57(34) 8.48(27)
(i)
6.81(22) 5.59(18) 5.23(17) 5.33(17) 6.05(19) 6.59(21) 7.32(24) 9.30(30) -
132mLa 43.7(16) 42.1(15) 49.5(17) 58.7(20) 68.5(23) 63.4(22) 38.6(14) 33.9(11) 19.75(63)
(i)
9.68(31) 3.96(13) 1.420(45) - - - - - -
132Cs 5.53(21) 5.22(19) 4.64(16) 4.26(15) 3.71(13) 3.17(12) 2.74(11) 2.527(84) 2.499(85)
(i)
2.399(79) 2.156(74) 1.961(66) 1.703(58) 1.469(52) 1.096(38) 0.690(26) 0.386(14) -
132Ce 17.38(63) 18.23(63) 21.47(72) 26.15(87) 36.7(12) 50.0(18) 58.5(22) 71.4(23) 37.1(12)
(m+)
14.48(46) 3.20(10) 0.508(16) - - - - - -
131La 66.9(26) 73.1(27) 79.8(30) 89.9(33) 97.1(37) 84.1(33) 16.70(88) 6.94(55) 1.82(32)
(c)
131Ba 20.8(14) 18.9(13) 13.8(14) 10.3(15) 8.2(18) 4.2(15) 7.88(70) 12.18(64) 15.29(59)
(m+)
- 20.49(66) 21.15(68) 16.28(52) 12.38(40) 6.83(22) 2.791(93) 0.685(25) -
130Ce 7.31(41) 7.67(51) 9.63(47) 11.80(61) 11.18(46) 2.84(32) - - -
(i)
129Cs 30.0(11) 24.35(84) 20.37(69) 18.26(61) 16.81(57) 14.70(52) 7.81(29) - 1.660(85)
(m+)
129mBa 10.07(36) 9.41(33) 8.09(27) 6.54(22) 4.65(16) 4.85(17) 3.27(12) - -
(c)
129gBa 32.6(12) 34.3(12) 33.9(11) 25.61(85) 10.63(36) 5.87(21) 3.51(13) 3.18(10) 1.939(62)
(c)
128Ba 35.7(13) 32.0(12) 24.42(87) 15.34(54) 13.50(48) 10.14(37) 0.701(31) - -
(c)
127Xe 33.7(13) 26.2(10) 23.08(83) 19.79(70) 11.26(46) 2.17(10) 0.701(34) - -
(c)
127Cs 34.8(16) 28.8(12) 23.49(93) 19.10(96) 12.62(76) - - - -
(c)
126I 0.766(81) 0.743(85) 0.413(31) 0.262(30) 0.33(10) - - - -
(i)
126Ba 6.79(44) 4.14(30) 3.75(35) 2.84(29) 1.32(28) - - - -
(c)
125Xe 16.58(66) 12.64(45) 7.98(28) 2.856(99) 1.380(54) 0.556(26) - - -
(c)
125Cs 19.5(44) 14.0(27) 8.9(19) - - - - - -
(c)
123Xe 4.31(23) 2.084(90) 1.261(72) 0.622(64) - - - - -
(c)
123I 1.51(25) 1.047(86) 0.745(85) 0.352(77) - - - - -
(i)

<!-- Page 11 -->

11
TABLE II: Summary of copper cross sections measured in this work. The uncertainty format and subscript
designations (c), (i) and (m+) remain the same as in Table I. Products which were used as beam current monitors
(and are therefore somewhat circular) are indicated with a ∗, e.g. 65Zn* .
(i)
natCu(p,x) Production cross sections (mb)
E (MeV) 188.2(21) 172.7(22) 158.3(23) 143.0(25) 127.8(27) 112.9(29) 96.5(33) 91.1(11) 85.9(11)
p
81.5(11) 77.5(12) 73.4(12) 69.8(13) 66.6(13) 63.8(14) 60.8(14) 57.7(15) -
65Zn* 1.240(77) 1.450(92) 1.565(78) 1.589(85) 1.717(97) 1.96(11) 2.42(11) 2.512(81) 2.523(81)
(i)
2.82(19) 2.90(13) 3.27(18) 3.28(10) 3.59(15) 3.65(16) 4.07(14) 4.16(14) -
64Cu 24.8(12) 29.1(25) 32.2(34) 30.6(13) 37.5(13) 35.0(25) 41.7(17) 37.3(19) 40.1(27)
(i)
43.9(16) 40.0(49) 42.7(23) 47.2(35) 48.7(24) 49.0(29) 50.6(20) 49.7(26) -
62Zn* 2.19(10) 2.74(11) 2.89(12) 3.09(13) 3.54(13) 3.75(19) 4.55(20) 4.96(19) 5.16(17)
(i)
5.77(22) 6.04(21) 6.70(26) 7.26(26) 8.03(30) 8.56(30) 9.29(32) 10.36(37) -
61Cu 31.2(16) 37.2(17) 38.3(16) 39.2(18) 44.4(20) 45.9(22) 53.3(25) 56.2(21) 61.1(22)
(c)
65.4(23) 69.2(25) 74.9(26) 79.6(28) 82.9(29) 85.4(30) 86.2(31) 89.6(32) -
60Co 10.89(71) 11.47(62) 11.50(63) 11.22(53) 11.14(54) 10.98(44) 11.25(52) - 11.8(16)
(m+)
14.0(60) 10.59(98) 13.8(50) 9.99(70) 13.6(56) 10.38(73) 14.7(23) 11.00(60) -
59Fe 1.206(49) 1.158(42) 1.138(40) 1.069(36) 1.024(50) 0.953(34) 0.837(35) 0.793(28) 0.787(27)
(i)
0.787(43) 0.771(27) 0.741(85) 0.720(26) 0.695(27) 0.630(23) 0.577(54) 0.496(16) -
58Co* 42.9(18) 44.6(20) 43.2(16) 44.3(17) 44.8(18) 47.3(17) 48.2(18) 50.5(17) 50.4(18)
(m+)
51.0(23) 47.4(17) 44.1(14) 39.1(15) 37.0(12) 33.1(12) 31.4(10) 30.4(11) -
57Ni 1.848(81) 1.955(82) 1.905(81) 1.938(88) 1.947(87) 1.845(85) 1.570(76) 1.467(78) 1.280(58)
(c)
1.213(47) 1.118(58) 1.261(53) 1.377(70) 1.576(65) 1.827(74) 2.09(10) 2.28(10) -
57Co 41.5(18) 41.8(17) 41.8(17) 42.5(19) 42.4(18) 41.6(18) 40.1(19) 40.3(17) 38.2(13)
(i)
36.6(13) 35.1(12) 35.3(13) 36.5(13) 40.2(15) 43.2(15) 48.8(20) 54.1(19) -
56Ni 0.140(21) 0.128(16) 0.144(23) 0.141(15) 0.115(10) 0.0781(53) 0.0701(68) - 0.096(10)
(c)
- 0.108(12) - 0.132(22) - - - - -
56Mn 2.331(92) 2.50(10) 2.39(13) 1.945(69) 1.988(75) 1.508(56) 1.123(58) 1.162(49) 1.144(47)
(i)
1.084(62) 1.047(43) 0.993(44) 0.734(70) 0.614(56) 0.490(39) 0.408(44) 0.340(31) -
56Co* 12.67(48) 12.17(46) 12.29(44) 12.21(44) 11.81(41) 11.06(41) 10.10(40) 10.53(39) 10.76(36)
(c)
12.22(47) 12.81(44) 14.09(62) 12.76(46) 11.49(66) 8.22(30) 5.71(35) 2.73(10) -
55Co 2.005(85) 2.014(83) 2.006(93) 1.870(82) 1.735(67) 1.568(84) 1.619(85) 1.719(85) 1.529(64)
(c)
1.238(51) 0.916(53) 0.465(28) 0.211(28) 0.105(18) 0.061(17) 0.042(11) 0.053(15) -
54Mn 16.69(62) 15.46(57) 14.76(68) 13.57(55) 11.90(49) 10.45(40) 6.94(30) 6.18(20) 4.68(15)
(i)
3.90(15) 3.55(17) 3.68(20) 3.98(15) 4.53(21) - - - -
52Mn 5.31(21) 4.89(20) 4.20(16) 3.61(13) 2.68(11) 1.959(77) 1.763(77) 1.752(61) 1.250(43)
(c)
0.841(31) 0.394(16) - 0.047(16) - - - - -
51Cr 11.65(46) 9.75(38) 8.16(31) 6.36(24) 5.09(21) 3.94(17) 1.464(88) - -
(c)
48V* 1.957(71) 1.454(56) 1.072(37) 0.691(24) 0.449(15) 0.300(13) 0.0553(48) - -
(i)
TABLE III: Summary of titanium cross sections measured in this work. The uncertainty format and subscript
designations (c), (i) and (m+) remain the same as in Table I. Products which were used as beam current monitors
(and are therefore somewhat circular) are indicated with a ∗, e.g. 48V* .
(i)
natTi(p,x) Production cross sections (mb)
E (MeV) 90.9(11) 85.6(11) 81.2(11) 77.3(12) 73.1(12) 69.5(13) 66.3(13) 63.5(14) 60.5(14)
p
48V* 7.15(27) 7.84(28) 8.11(30) 8.96(32) 9.30(33) 10.53(38) 10.75(43) 11.81(43) 11.93(51)
(i)
48Sc 2.50(30) 2.60(33) 2.49(36) 2.68(38) 2.48(41) 2.23(47) 2.33(47) 2.05(39) 1.98(35)
(i)
47Sc 19.87(86) 20.13(69) 20.11(89) 20.76(79) 20.5(11) 20.97(69) 20.97(71) 21.06(68) 21.14(69)
(i)
46Sc* 39.5(15) 40.8(14) 41.9(14) 43.9(15) 44.5(15) 45.9(15) 46.0(15) 48.1(16) 49.1(17)
(m+)
44mSc 18.38(70) 19.35(81) 20.53(79) 21.45(81) 20.94(79) 19.56(84) 17.94(83) 16.63(76) 14.26(63)
(i)
43Sc 27.6(53) 28.7(56) 24.9(63) 26.5(66) - - - - -
(c)
43K 1.706(82) 1.619(98) 1.497(64) 1.402(57) 1.366(54) 1.369(59) 1.298(45) 1.383(47) 1.437(59)
(c)
42K 5.81(44) 6.01(40) 5.87(40) 6.39(44) 6.10(42) 6.60(43) 6.41(42) 6.22(42) 5.26(34)
(i)

<!-- Page 12 -->

12
ment, arising from higher energy gamma-rays scattering
out of the detector. Additionally, above proton energies
ofapproximately60MeV,the(T =11.50day)product
1/2
131Ba is produced, which has a 2.18(3)% gamma emission at 133.617 keV, which may interfere with the 130.4
keV 134Ce emission depending on the resolution of the
detector.
Instead, the preferred signature for 134Ce is the
5.04(20)%, 604.721 keV gamma emitted by its decay
product 134La. Lanthanum-134 has a half-life of only
6.45 minutes, much shorter than the 3.16 day half-life of
134Ce, which means it reaches secular equilibrium with
134Ce after only a few hours. However, even this approach is not foolproof, as the (T = 17.7 h) 135Ce
1/2
isotope produced via the (p,5n) channel emits multiple
gamma-rays which overlap at this energy, meaning it
must have time to sufficiently decay (≈ 7 days) before
the 134La decay can be observed without contamination.

### The measured cross sections for 134Ce production can

be seen in Fig. 8 in comparison to other measurements
and theoretical predictions. The most notable result is
that the measured cross sections were much higher than
theoretical predictions in the 100–200 MeV energy region. This may have implications for bulk production of
this isotope for medical applications, as it would imply a
higher production rate at facilities utilizing these higher
energy beams than theoretical estimates had previously
suggested.
300
250
200
150
100
50
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
gamma branch discussed previously. While that gamma
decay was observed in this work, it was supplemented
with the 134La decay gamma at 604.721 keV, which typically had lower peak fitting uncertainties than the 130.4
keV gamma.

### In addition to under-predicting the cross section at

high energy, the default models generally struggled to
predict the centroid energy of the “compound peak”,
though not as significantly as has been reported in previous versions of these codes [16]. We expect this is due
to differences in the predicted neutron emission spectra
arising from the different level densities and preequilibrium reaction models used by each code, which would
affect how much energy is “carried away” by these neutrons prior to the nucleus reaching a compound state.

### In the adjusted TALYS-2.0 model, this effect has been

improved, though not completely corrected, with modifications to the default preequilbrium parameters, to be
discussed in more detail below.

### IV.2. 139La(p,n)139Ce Cross Section

The product 139Ce was measured via its 79.90(5)% intensity, 165.86 keV gamma emission, which was clearly
observable several days after the end-of-bombardment
due to this isotope’s relatively long half-life of
137.641(20) days. This also included feeding from the
139mCe isomer, which has a half-life of only 57.58(32)
139La(p,6n)134Ce (i) s, and decays via a 100% isomeric transition to the
ground state. The measured cross sections for the

## Tendl-2023

139La(p,n)139Ce channel can be seen in Fig. 9.
TALYS-2.0 (default) (m+)
TALYS-2.0 (adjusted)

### ALICE-20 (default)

EMPIRE-3.2.3 (default)

### This Work


### K.V.Becker (2020)

J.T.Morrell (2019)
F.Tarkanyi (2017)
102
101
FIG. 8: Measured cross sections for the
139La(p,6n)134Ce reaction.
0 50 100 150 200

### Proton Energy (MeV)


### In general these results agree quite well with previous

measurements. However, there is a significant difference
in the two highest energy data points from Becker et al.,
which is not explained by the reported error margins.
One potential source of discrepancy could be the choice
ofgammalineusedforquantifying134Ce,astheBeckeret
al. measurementreliedsolelyuponthe0.209%,130.4keV
)bm(
noitceS
ssorC
139La(p,n)139Ce
(m+)

### TENDL-2023 K.V.Becker (2020)


### TALYS-2.0 (default) J.T.Morrell (2019)

TALYS-2.0 (adjusted) F.Tarkanyi (2017) ALICE-20 (default) H.E.Hassan (2007)
EMPIRE-3.2.3 (default) J.Wing (1962)

### This Work

FIG. 9: Measured cross sections for the 139La(p,n)139Ce
reaction.

### The results agree quite well with most of the existing

measurements, although there is a large amount of scat-

<!-- Page 13 -->

13
ter in these data. It is unclear why this might be the
case, as the 165.86 keV gamma line is well-isolated from
contaminants and quite strong, but could be attributed
to poor counting statistics in these measurements if the
lanthanum foil were not counted a sufficient length of
time — in our experiment the 165.86 keV line typically
had a count rate below 1 s−1.
102
In general the reaction modeling is quite good, with

### ALICEgenerallyperformingbestatlowenergyandEM-


### PIRE being the best code at predicting the high-energy

behavior. Similar to the (p,6n) channel, the cross section in the 100–200 MeV region was higher than most of
the codes predicted, although by a far smaller percent- 101
age. This may also have significance for medical isotope
25 50 75 100 125 150 175 200
productionapplications,as 139Ceistheprimarycontam-

### Proton Energy (MeV)

inant of concern when producing 134Ce, due to its long
half-life and inability to be chemically separated from
134Ce [11, 13]. Therefore, this cross section sets a fundamentallowerlimittothepossibleradiopuritywithwhich
134Ce can be produced.

### IV.3. 139La(p,3n)137m,gCe Cross Sections

Both the isomer (J = 11/2−) and ground state
π
(J = 3/2+) of 137Ce were independently observed in
π
this work, formed through the (p,3n) reaction channel.
The measured cross sections for the formation of these
products are shown in Fig. 10.
The 137mCe isomer decays with a 1.433(13) day halflife, mostly via an isomeric transition to the ground
state, accompanied by a 254.29 keV gamma emission
with an 11.1(4)% branching ratio. This allowed the production of the isomer to be quantified relatively accurately. Unfortunately, the fact that the isomer feeds
into the shorter-lived (T = 9.0(3) h) ground state
1/2
makes the quantification of the ground state population
somewhat difficult. This is compounded by the relatively weak gamma-emission probability of the ground
state, with a 1.680(84)% intense 447.15 keV gamma being the strongest emission. Distinguishing the independent 137Ce ground state production from isomeric feeding required fitting spectra shortly (a few hours) after
the end-of-bombardment, where the signal-to-noise ratio of the 477.15 keV gamma line was quite low due to
theComptoncontinuumarisingfrommanyhigherenergy
gamma decays. Therefore the uncertainty on this cross
section was generally very large, and a few of the BNL
data points were omitted as the uncertainty was greater
than 50%.

### In both the isomer and ground state, there is good

agreement with existing measurements. While there is
a significant amount of fluctuation in the ground state
data, this is generally within the large error bounds that
)bm(
noitceS
ssorC
139La(p,3n)137mCe
(i)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)

### ALICE-20 (default)

EMPIRE-3.2.3 (default)

### This Work


### K.V.Becker (2020)

J.T.Morrell (2019)
F.Tarkanyi (2017)
102
101
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,3n)137gCe
(i)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)

### ALICE-20 (default)

EMPIRE-3.2.3 (default)

### This Work


### K.V.Becker (2020)

J.T.Morrell (2019)

### F.Tarkanyi (2017)


### FIG. 10: Measured cross sections for the

139La(p,3n)137mCe (top) and 139La(p,3n)137gCe
(bottom) reactions.
arise from the difficulty described above. Most of the reactionmodelingcodesproducedreasonablepredictionsof
the 137mCe (isomer) population, with ALICE-20 giving
thebestresultacrossthespanofenergies. However,AL-

### ICEgreatlyunder-predictedthegroundstatepopulation,

and due to the rather large variability in the measured
data for 137gCe, it is unclear which of the other models
performed best. Because most of the (p,3n) cross section populates the isomer, the total cross section for this
channel is relatively well-predicted by the models, with
only ALICE greatly over-predicting the m/g (isomer-toground state) ratio. This is in accordance with a general
observation of relatively poor angular momentum modeling in ALICE [21, 42].

<!-- Page 14 -->

14

### IV.4. 139La(p,5n)135Ce Cross Section


### Thepopulationof135Ceviathe(p,5n)reactionchannel

was relatively well-quantified, due to a large number of
intense gamma emissions ranging from 119.52 keV (I =
γ
1.30(9)%) to 1184.09 keV (I = 1.09(5)%), six of which
γ
had a gamma branching ratio greater than 10%. This
cross section also includes the population of the 135mCe
isomer, as its 20(1) second half-life was too short to be
independently measured before it decayed with a 100%
isomeric transition to the ground state. The measured
cross sections for this channel are plotted in Fig. 11.
500
400
300
200
100
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
longthatthe 134Ce/139Ceratioissignificantlyimpacted.
Because of the trade-off between 135Ce and 139Ce impurity, it is essential to measure the magnitude and energy
dependence of each of these cross sections if one is to
optimize the 134Ce production scenario.

### IV.5. 139La(p,7n)133m,gCe Cross Sections

Theisomer(J =9/2−)andgroundstate(J =1/2+)
π π
of 133Cewereaccuratelyquantifiedviaalargenumberof
gamma decays in the (T = 5.1(3) h) isomer, and the
1/2
15.9(23)% intense 76.9 keV gamma emission from the
(T =97(4) min) ground state. Unlike the (p,3n) reac-
139La(p,5n)135Ce
(m+)
tio
1
n
/2
populating 137Ce, thegroundstateof 133Cewasrel-
TENDL-2023 atively straightforward to independently quantify due to
TALYS-2.0 (default) theisomerexclusivelydecayingto 133La,withnopopula-

### TALYS-2.0 (adjusted)

ALICE-20 (default) tionofthegroundstateof 133Ce. Themainchallengeas-
EMPIRE-3.2.3 (default) sociatedwiththese(p,7n)channelswastoensureconsis-
This Work tencywiththeotherproductsintheoverlappingA=133

### K.V.Becker (2020)

decay chains: 133La, 133mBa and 133gBa. However, this

### J.T.Morrell (2019)

F.Tarkanyi (2017) did not have any impact on the accuracy of the 133m,gCe
products themselves. The measured cross sections can
be seen in Fig. 12.

### The experimental data on these channels are quite

sparse, with only four measurements of 133mCe from
Becker et al. and two from T´ark´anyi et al. [15, 17].

### However, where they overlap, the agreement is quite

good. The consistency of the measurements in this and
FIG. 11: Measured cross sections for the otherchannelswouldseemtoindicatethatthebeamcur-
139La(p,5n)135Ce reaction. rent determination and energy assignments of the various measurements agree quite well, and that any systematic differences are likely attributable to specifics of

### Theresultsofthisworkshowexcellentagreementwith

theactivitydetermination(counting,peak-fitting,decayprevious measurements, likely due to the large produccorrections, etc.) associated with individual isotopes,
tion cross section and high accuracy with which this isorather than some global difference.
tope’s activity can be quantified. TALYS and ALICE
show good agreement in the prediction of the compound For both 133mCe and 133gCe, no particular reaction
peak, though ALICE somewhat over-estimates the max- modelgivesasatisfactorypredictionofthecrosssection.
imum cross section. EMPIRE struggled to predict both Most of the models over-predict the ground state poputhe centroid energy and magnitude of the compound lationandunder-predicttheisomer,exceptforEMPIRE
peak,althoughithasthebestpredictionabove≈70MeV. which under-predicts them both. Once again, ALICE
This could be a result of better preequilibrium modeling givesverypoorpredictionsofthem/gratio,withalmost
parameters used in the EMPIRE exciton model. How- nopopulationoftheisomer. Also, thedefaultcodesgive
ever, it could also be a numerical artifact arising from generally poor predictions of the centroid energy of the
EMPIRE’s limitations on the number of tracked ejectile compound peak and the overall shape, which we likely
particles, essentially forcing the cross section to be arti- attribute to the preequilibrium modeling.
ficially higher at high energies.

### For medical isotope production applications, 135Ce

(T 1/2 = 17.7(3) h) is the longest-lived contaminant IV.6. 139La(p,10n)130Ce Cross Section
to 134Ce production, aside from the much longer-lived
139Ce, and cannot be chemically removed. However, because the 135Ce half-life is shorter than 134Ce, the ra- While many other reaction channels were observed,
diopurity of 134Ce can be improved by waiting for 135Ce one final product isotope that is particularly interesting
to decay away — although the decay time cannot be so is 130Ce, resulting from the exclusive (p,10n) reaction

<!-- Page 15 -->

15
150
125
100
75
50
25
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,7n)133mCe
(i)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)

### ALICE-20 (default)

EMPIRE-3.2.3 (default)

### This Work

K.V.Becker (2020)
F.Tarkanyi (2017)
40
30
20
10
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
thereforethe357.4keV(I =81(4)%)gammafrom130La
γ
was used to quantify the 130Ce production rate instead.
Becauseofthe8.7(1)minhalf-lifeof 130La,afterapproximately 90 minutes of decay the entire 130La population
wasattributableto 130Cedecay, whichwasconfirmedby
fitting the decay of the 357.4 keV line with the 22.9(5)
minutehalf-lifeof130Ce. Theresultsofthismeasurement
are plotted in Fig. 13.
20
15
10
139La(p,7n)133gCe
(i)
5

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)

### ALICE-20 (default) 0


### EMPIRE-3.2.3 (default)

40 60 80 100 120 140 160 180 200

### This Work


### Proton Energy (MeV)


### FIG. 12: Measured cross sections for the

139La(p,7n)133mCe (top) and 139La(p,7n)133gCe
(bottom) reactions.
on 139La. We believe that this represents the first measurementofanindependent, exclusive(p,10n)excitation
function in this energy range in the literature. While
therearetwomeasurementsofthe 124Sn(p,10n)115Sbreactionontintargetsenrichedin 124SnfromAlexandryan
et al. and Balabekyan et al., they were each only measured at one energy point — 660 MeV and 3.65 GeV,
respectively — and therefore did not capture either the
threshold of the reaction or the shape of its excitation
function [43, 44]. Also, while there are several measurements of residual products resulting from (p,10n) reactions,theyareeithercumulativecrosssectionsorinclude
contributions from other target isotopes.

### While 130Ce does have uniquely identifying gamma

emissions, the initial counts after end-of-bombardment
had contaminating gamma lines in the 130Ce peaks, and
)bm(
noitceS
ssorC
139La(p,10n)130Ce
(i)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)

### ALICE-20 (default)

EMPIRE-3.2.3 (default)

### This Work

FIG. 13: Measured cross sections for the
139La(p,10n)130Ce reaction.
The results are significantly discrepant with the modeled cross sections, indicating that a significant parameter adjustment is necessary. Interestingly, the measurement showed almost no compound peak. Although it is
possibletherearenotenoughenergypointstoresolvethe
compound peak, the data seem to suggest that the compoundmechanismissignificantlydampedinthischannel,
and presumably for higher (p,xn) channels as well.

## V. Charged Particle Reaction


## Modeling


### The comparison of the cross sections measured in

this work to the three nuclear reaction modeling codes

### TALYS, EMPIRE and ALICE, as well as TENDL-2023,

showed a clear need for a parameter adjustment from
the default models. Additionally, while the adjusted parameter set from Fox et al. fit the available data well,
it did not extrapolate to our new measurements above
100 MeV. In this work, we apply a modified version of
theTALYS-basedresidualproductfittingprocedurethat
was introduced in Fox et al. to the new set of measured cross sections [21]. In conjunction with literature
data, these new measurements represent up to approximately 55% of the entire non-elastic cross section of proton reactions on lanthanum, for a combined 30 reaction

<!-- Page 16 -->

16
channels, ranging in energy from 4.5–188.4 MeV. This considered in the optimization, particularly the neutron
provided a unique opportunity to explore the nuclear re- optical model parameters and additional preequilibrium
action physics of this system. The motivation for using model parameters: specifically the Rnunu, Rnupi, Rpinu
TALYSoverotherreactionmodelingcodeshasbeenwell and Rpipi modifiers to the matrix element, as well as
described in Fox et al., but we will reiterate the bene- Rgamma. Finally, we did not perform any isotope-specific
fits to TALYS being the accessibility of this code (and level density adjustments using the ptable parameter,
its underlying models), as well as the perception that however this would certainly be useful if one wished to
the two-component exciton model employed by TALYS provide the best interpolation of the data.
is the most physically justified out of the default models
inthemostprominentlyusedcodes(e.g. EMPIRE,CoH, While a number of parameter optimization algorithms
ALICE) [21, 22, 39, 40, 45]. were considered for this work, the method with the best
performance (best improvement over default TALYS)
was actually the simplest method: sequentially optimizingoneparameteratatime. Conventionalregressionand
V.1. Fitting Procedure simulated annealing methods were also attempted, but
failed to produce a satisfactory result. This method of
sequentially optimizing the parameters for specific mod-
The parameter adjustment procedure used to improve els within TALYS has a number of advantages over less
the predicted cross sections was inspired by the recent physically-motivated evaluation methods. One of the
work of Fox et al., which proposed a particular sequence most obvious advantages is that TALYS contains over
of parameters to be optimized, with the specific goal 400 adjustable parameters, some of which are numeriof fitting high-energy proton-induced reaction data [21]. cal, some are yes/no, some require a choice from a num-
Our general approach can be outlined as follows: ber of options, and some even require a file input. This
means that one could not optimize all parameters in

### TALYS using conventional methods such as linear re-


## Down-select data to strongest, independently mea- gression, and even if one were to use a more global opsured reaction channels. We will refer to this as timization approach such as a machine learning model,

“training” data. there are likely not enough experimental data available
to train such a model on the full parameter space. In-

## Choose a goodness-of-fit metric to be optimized.

stead,aphysically-motivatedevaluationapproachallows
one to down-select to a much smaller subset of param-

## Optimize base-model selection parameters, e.g.,

eters, based on which parameters are relevant to the
ldmodel, strength, deuteronomp and alphaomp.
data being fit, as well as eliminating parameters which

## Adjust major optical model parameters, primarily have been well-constrained by other experiments. Even

rvadjustandavadjustforbothneutronsandpro- then, there may still be dozens of relevant parameters to
tons. a data set like the stacked-foil measurement performed
here, which may overwhelm a conventional regression al-

## Adjust major preequilibrium exciton model pagorithm, particularly when the effects of one parameter

rameters, primarily M2constant, M2limit and are highly correlated with another. We hypothesize that
M2shift.
thestrongsensitivitiesandcorrelationsofourproblemto
these parameters are the reason that sequential parame-

## Adjust minor parameters, e.g., Rgamma, Cstrip a,

ter optimization provided the best results.
etc.

### Following the procedure outlined above, we selected


## Iterate through steps 4–6 until convergence in the

our“training”datasetfromthe18largestcrosssections
goodness-of-fit metric.
inTableIwhichwereindependentlymeasured,including

## Validate using the unused (cumulative) channels products with contributions from an isomer but no feedexcluded from step 1. ing from other isotopes, i.e., cross sections subscripted

(i) or (m+). The 12 remaining cross section channels
were reserved for validation. In Fox et al. two goodness-
There are three primary differences between the pro- of-fitmetricswereused: reduced-χ2(χ2)weightedbythe
ν
posed approach and the work of Fox et al. First, we maximumcrosssectioninachannel,andχ2 weightedby
ν
adjusted the optical model parameters before other pa- the integrated cross section in a channel. The reasoning
rameters, rather than after the preequilibrium optimiza- behind using a weighted χ2 is that the larger reaction
ν
tion. This was motivated by the fact that optical model channels(eitherbymaximumorintegratedcrosssection)
parameters determine the magnitude of the non-elastic contain more information relevant to the models being
cross section, which should be fixed before modifying optimized, andthusshouldbeweightedheavierthanthe
parameters which affect channel-to-channel competition. minor channels. Because we preferred to optimize on a
Second, we greatly increased the number of parameters

<!-- Page 17 -->

17
TABLE IV: Summary of TALYS-2.0 base-model TABLE VI: Summary of preequilibrium parameters
selection parameters. explored in TALYS-2.0 modeling. Parameters at the
limits of the constraints are indicated with a ∗. Defaults
for Rnunu and Rgamma were 1.5 and 2.0, respectively, all
Parameter Best Sensitivity Default Options
others were 1.
ldmodel 5 84.2 1 1–6
strength 10 46.1 9 1–10
deuteronomp 2 21.6 1 1–5 Parameter Best Sensitivity Constraints
alphaomp 4 8.48 6 1–8 M2constant 1.055 134 0.2–5
preeqspin 3 2.08 1 1–3 M2shift 1.196 109 0.2–5
M2limit 1.926 37.1 0.2–5

### Rnunu 1.66 33.3 0.1–10

TABLE V: Summary of optical model parameters

### Rnupi 0.16 35.7 0.1–10

explored in TALYS-2.0 modeling. Parameters at the Rpinu 2.21 38.0 0.1–10
limits of the constraints are indicated with a ∗. Defaults Rpipi 0.1∗ 6.65 0.1–10
for all parameters were 1. Rgamma 0.1∗ 0.1 0.1–10

### Cstrip a 0.1∗ 4.2 0.1–10

Parameter Best Sensitivity Constraints
rvadjust n 0.977 4523 0.95–1.05
avadjust n 1.076 291 0.75–1.25
rvadjust p 0.9∗ 59.1 0.9–1.1 inweighted-χ2 ν tothepercentchangeintheparameter—
avadjust p 1.0118 30.8 0.7–1.3 evaluated at the default value for that parameter. This
w1adjust n 4∗ 5.79 0.25–4 was used to inform the order in which the parameters
w2adjust n 1.51 8.92 0.25–4 were optimized, as well as the range of allowed values.
w1adjust p 4∗ 18.5 0.25–4 Parameterswithveryhighsensitivities,suchasrvadjust
w2adjust p 1.83 19.3 0.25–4
n, were constrained to be much closer to the default values. Additionally, because rvadjust and avadjust correspondtothewidthanddiffusenessoftheoptical-model
singlefigure-of-merit,weoptedtousetheaverageofthese wellpotential,whichhavefairlywell-constrainedsystemtwo (max and integral) weights. Also, because 134Ce is atics, the allowed range of values was more limited than
a reactionchannel withparticular value forapplications, for other parameters [48]. The resulting optimized optheweightforthe 134Cechannelwasselectivelydoubled. tical model parameters, as well as the associated sensitivities and parameter constraints, are given in Table V.
The first set of parameters to be optimized were re- In most cases the imposed constraints were more strict
lated to selection of the base-models, such as level den- than those required by TALYS. Because of the relatively
sity and gamma strength. The sensitivity to each base- largesensitivityofthesecalculationstoopticalmodelpamodel parameter was first calculated, in order to decide rameters, the resulting “best” values were very near the
if the parameter should be included, as well as to in- default values, with the exception of w1adjust for both
form the optimization order. Because these are discrete protons and neutrons, which relate to the magnitude of
parameters, the “sensitivity” was calculated as the max- the imaginary component of the optical model potential,
imum percentage change (not necessarily improvement) primarily impacting the elastic to non-elastic cross secin weighted-χ2, out of the whole set of options. The tion ratio.
ν
base-model parameters were then optimized in order of
highestsensitivity. Theresulting“best”modelselection, Thesameapproachwastakenforoptimizingthepreerange of options, default options and sensitivities are quilibrium parameters, with the results shown in Table
givenforeachofthe5consideredparametersinTableIV. VI. The most significant change (from defaults) was to
It was found that ldmodel 5 and strength 10 were the M2limit, which affects the asymptotic behavior of the
best options, corresponding to the Gogny Hartree-Fock- exciton transition rates. This seemed to be necessary
Bogoluybov (HFB) level densities and Skyrme (HFB) + to account for the significant enhancement (over default
QRPA corrected strength tables, respectively [46, 47]. predictions)ofthepreequilibriumtailseeninmostofthe
Also,notethateachmodelwasrunwiththeoptionbins (p,xn) channels, which occurred above 100 MeV. The ef-
0, which scales the number of excitation energy bins as fects of this are quite apparent in the (p,6n) and (p,8n)
the incident energy increases. cross sections plotted in Fig. 14, where almost every
other prediction is a factor of 2–5 low in this energy re-
Following the base-model selections, the continuous- gion. Other significant changes were to Rgamma, which
variable parameters were optimized iteratively, begin- is a competing mechanism for de-excitation to neutron
ning with the optical model parameters. For the opti- emission, as well as to Cstrip a, which affects the magcal model and preequilibrium parameters, the sensitivity nitudeofthepreequilibriumcontributionsto(p,α)chanwas calculated as dχ2/dp, or the ratio of percent change nels.
ν

<!-- Page 18 -->

18
300
250
200
150
100
50
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,6n)134Ce
(i)

## Tendl-2023

TALYS-2.0 (default) 100
TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)

### This Work 80


### K.V.Becker (2020)

J.T.Morrell (2019) 60
F.Tarkanyi (2017)
40
20
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,8n)132Ce
(m+)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)

### This Work


### K.V.Becker (2020)

FIG. 14: Comparison of predicted and observed cross sections for the 134Ce (left) and 132Ce (right) products, which
were used as training data for the parameter adjustments.
TABLE VII: Summary of TALYS-2.0 modeling results. inFig. 15,withadditionalresultsplottedinFigs. 16and

## Ingeneral,thefittothevalidationdatasetwasmuch

worse than the training set, as one might expect. How-

### Source Training χ2 Validation χ2

ν ν ever,thefitstillrepresentsanimprovementoverallofthe
TENDL-2023 633 412 modeling codes run with default values, as well as over

### TALYS-2.0 default 2012 4769

the Fox adjustment (for reasons previously discussed).

### TALYS-2.0 adjusted 73.5 3663

Our adjustment performed worse than the TENDL-2023

### TALYS-1.9 (M.B. Fox) 638 5515

evaluation on the validation data, which seems to be at-

### EMPIRE-3.2.3 default 879 3515

tributed to a significant over-prediction of many barium

### ALICE-20 default 6741 7.11×104

and iodine channels. This could be due to over-fitting,
i.e., using too many parameters in our adjustment, or
could be due to making adjustments that were too large
andarethereforenon-physical. Whilethisdoeshighlight
The completed parameter adjustment resulted in sigthe challenges of performing reaction evaluations on innificant improvements to cross section predictions in the
complete data sets, and the need for more work on this
“training” data set, over default predictions. The resulting improvement in the weighted-χ2 figure-of-merit topic, the improvement over default predictions for both
ν trainingandvalidationdatasetsimpliessomeamountof
can be seen in Table VII, in comparison to TENDL-
physical consistency in our adjustments.
2023, default predictions from TALYS-2.0, EMPIRE-
3.2.3, ALICE-20 as well as the parameter adjustment
resulting from the work of M.B. Fox et al., which was
calculated with TALYS-1.9 as this was the TALYS version used in that work [21]. While the Fox adjustment VI. SUMMARY AND CONCLUSIONS
performedwellonthedatathatwasavailableatthetime,
that data did not include any energies above 100 MeV,
and unfortunately as a result did not extrapolate well Inthisworkweconductedtwostacked-foilirradiations
to the new 100–200 MeV measurements collected in this —attheLANLIsotopeProductionFacilityandtheBNL
work. However, the Fox parameters still represent an Brookhaven Linac Isotope Producer — resulting in 30
improvement over default predictions. measurementsof 139La(p,x)crosssectionchannelsinthe
55–200 MeV proton energy range. Many of these cross
We also performed a validation of the parameter ad- sections represent the first observation of certain reacjustmentsagainstthevariousotherpredictions,usingthe tion products, and for all of the observed products this
unused “validation” data set, mostly comprising the cu- represents the first set of measurements above 100 MeV.
mulative channels. The weighted-χ2 for the validation Additionally,thefidelityofcertainchannelsbetween70–
ν
data are also given in Table VII, where the weights were 100MeVwasimprovedwithmeasurementsatadditional
again determined as the average of the two weighting proton energies, notably 134Ce. The 134Ce product repmethods (max and integral) from the Fox et al. work resents a significant interest to the medical isotope pro-
[21]. Two of the 12 validation channels are also plotted duction community. The reported finding that the cross

<!-- Page 19 -->

19
140
120
100
80
60
40
20
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)131La
(c)
60

## Tendl-2023

TALYS-2.0 (default)
50
TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)
This Work 40
30
20
10
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)129gBa
(c)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)

### This Work

FIG. 15: Comparison of predicted and observed cross sections for the 131La (left) and 129gBa (right) products, which
were used to validate the parameter adjustments.
sectionwashigherthanpredictedabove100MeVislikely
tobeofinterestforthatapplication. Also,webelievethe ACKNOWLEDGEMENTS
139La(p,10n)130Ce reaction measured in this work to be
the first measurement of an exclusive (p,10n) excitation
function reported in the literature. In general, the sig- We wish to acknowledge our thanks to the operators
nificantdiscrepanciesbetweentheobservedcrosssections oftheLANLIPFfortheirassistanceandsupportduring
anddefaultmodelpredictionssuggestsaneedtousecau- the LANL irradiation: Anthony Koppi, Ross Capon and
tion when relying upon such predictions for applications Nathan Kollarik. Additionally, we thank the BNL BLIP
where little or no experimental data exist. operators Henryk Chelminski and David O’Rourke. We
are grateful to Ben Stein for the use of the LANL glove-
The cross sections measured in this work represent box for the preparation and storage of the lanthanum
a significant proportion of the non-elastic cross section, foils. We acknowledge Deepak Raparia, head of the
whichweestimatetobeashighas55%oftheentirenon- Pre-Injector Systems group at BNL-CAD for supportelasticcrosssection. Theextensivenatureofthisdataset ing the BLIP beam tuning. We would also like to thank
enabled a comprehensive parameter adjustment for the the LANSCE Accelerator Operations support staff, and
p+139La system. Using the TALYS-2.0 nuclear reaction acknowledge the support from the LANSCE radiologimodelingcode,parameteradjustmentsweremadetothe cal control technicians. Additionally, we are grateful to
optical model and to the two-component exciton model Patrick Sullivan and Vicki Litton for their support with
forpreequilibrium. Theadjustmentprocedureresultedin radiological controls at BNL.
an improvement in the overall fit to the measured data,
which we believe to be physically consistent based on This research is supported by the U.S. Departan improvement in cumulative reaction channels which ment of Energy Isotope Program, managed by the
were not used as part of the data set for the parameter Office of Science for Isotope R&D and Production.
optimization. The results corroborate previous findings This work was carried out under Lawrence Berkesuggesting the need to incorporate residual product ex- ley National Laboratory (Contract No. DE-AC02-
citation functions into exciton model parameterization 05CH11231),LosAlamosNationalLaboratory(Contract
studies, particularly at high energy [21]. No. 89233218CNA000001) and Brookhaven National
Laboratory (Contract No. DEAC02-98CH10886).

### Theanalysiscodeusedtoconvertthespectraintocross

sections, as well as the gamma-ray spectra and all other This material is approved for public release; distriburaw data generated during this work, have been stored tion unlimited (LA-UR-24-21320).
in a LANL archive, and are available upon request to
the corresponding author. Upon publication, the cross
section data will be incorporated into EXFOR [49].

<!-- Page 20 -->

20
0.6
0.5
0.4
0.3
0.2
0.1
0.0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)136Cs(m+)

## Tendl-2023

TALYS-2.0 (default) 250 TALYS-2.0 (adjusted) TALYS-1.9 (M.B. Fox)
This Work 200
150
100
50
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)135La(i)
25

### TENDL-2023 This Work

TALYS-2.0 (default) K.V.Becker (2020) TALYS-2.0 (adjusted) J.T.Morrell (2019) 20 TALYS-1.9 (M.B. Fox) F.Tarkanyi (2017)
15
10
5
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)135mBa(i)

## Tendl-2023

TALYS-2.0 (default) TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)
This Work
300
250
200
150
100
50
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)133La(i)

### TENDL-2023 This Work 35


### TALYS-2.0 (default) K.V.Becker (2020)

TALYS-2.0 (adjusted) F.Tarkanyi (2017) 30
TALYS-1.9 (M.B. Fox)
25
20
15
10
5
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)133mBa(i)

### TENDL-2023 This Work 70


### TALYS-2.0 (default) K.V.Becker (2020)

TALYS-2.0 (adjusted) J.T.Morrell (2019) 60
TALYS-1.9 (M.B. Fox) F.Tarkanyi (2017)
50
40
30
20
10
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)132mLa(i)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)
This Work
6
5
4
3
2
1
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)132Cs(i)

## Tendl-2023 50


### TALYS-2.0 (default)


### TALYS-2.0 (adjusted)

TALYS-1.9 (M.B. Fox) 40

### This Work


### K.V.Becker (2020)

J.T.Morrell (2019) 30
20
10
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)131Ba(m+)

### TENDL-2023 This Work 30


### TALYS-2.0 (default) K.V.Becker (2020)

TALYS-2.0 (adjusted) F.Tarkanyi (2017)
TALYS-1.9 (M.B. Fox) 25
20
15
10
5
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)129Cs(m+)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)

### This Work

FIG. 16: Comparison of measured cross sections to TENDL-2023 and TALYS-2.0 predictions using default
parameters, the parameter adjustments of Fox et al., and the adjustments performed in this work [21].
[1] C. Kratochwil, F. Bruchertseifer, F. L. Giesel, [5] A. K. Jain, S. Singh, S. Kumar, and J. K. Tuli, Nuclear
M. Weis, F. A. Verburg, F. Mottaghy, K. Kopka, Data Sheets for A = 221, Nuclear Data Sheets 108, 883
C. Apostolidis, U. Haberkorn, and A. Morgenstern, (2007).
225Ac-PSMA-617 for PSMA-Targeted α-Radiation [6] F. Kondev, E. McCutchan, B. Singh, K. Banerjee,
Therapy of Metastatic Castration-Resistant Prostate S. Bhattacharya, A. Chakraborty, S. Garg, N. Jovance-
Cancer, Journal of Nuclear Medicine 57, 1941 (2016), vic,S.Kumar,S.Rathi,T.Roy,J.Lee,andR.Shearman,
https://jnm.snmjournals.org/content/57/12/1941.full.pdf. Nuclear Data Sheets for A=217, Nuclear Data Sheets
[2] N. L. of Medicine (US), A Study of JNJ-69086420, 147, 382 (2018).
an Actinium-225-Labeled Antibody Targeting Hu- [7] M. Basunia, Nuclear Data Sheets for A = 213, Nuclear
man Kallikrein-2 (hK2) for Advanced Prostate Can- Data Sheets 108, 633 (2007).
cer, https://clinicaltrials.gov/study/NCT04644770 [8] J. Chen and F. Kondev, Nuclear Data Sheets for A =
(2024), Identifier NCT04644770. 209, Nuclear Data Sheets 126, 373 (2015).
[3] N. L. of Medicine (US), Venetoclax and Lintuzumab- [9] J. Ma, L. Li, T. Liao, W. Gong, and C. Zhang, Efficacy
Ac225inAMLPatients,https://clinicaltrials.gov/ andSafetyof225Ac-PSMA-617-TargetedAlphaTherapy
study/NCT03867682 (2023), Identifier NCT03867682. in Metastatic Castration-Resistant Prostate Cancer: A
[4] A.Jain,R.Raut,andJ.Tuli,NuclearDataSheetsforA Systematic Review and Meta-Analysis, Frontiers in On-
= 225, Nuclear Data Sheets 110, 1409 (2009). cology 12 (2022).

<!-- Page 21 -->

21
[10] R. M. Pallares and R. J. Abergel, Development baum, C. S. Cutler, D. G. Medvedev, F. M. Nortier,
of radiopharmaceuticals for targeted alpha therapy: E. M. O’Brien, and C. Vermeulen, Investigating high-
Where do we stand?, Frontiers in Medicine 9, energyproton-inducedreactionsonsphericalnuclei: Im-
10.3389/fmed.2022.1020188 (2022). plications for the preequilibrium exciton model, Phys.
[11] T.Bailey,V.Mocko,K.Shield,D.An,A.Akin,E.Birn- Rev. C 103, 034601 (2021).
baum, M. Brugh, J. Cooley, J. Engle, M. Fassbender, [22] Koning,Arjan,Hilaire,Stephane,andGoriely,Stephane,
S.Gauny,A.Lakes,F.Nortier,E.O’Brien,S.Thieman, TALYS: modeling of nuclear reactions, Eur. Phys. J. A
F. White, C. Vermeulen, S. Kozimor, and R. Abergel, 59, 131 (2023).
Developing the 134Ce and 134La pair as companion [23] W.Huang,M.Wang,F.Kondev,G.Audi,andS.Naimi,
positron emission tomography diagnostic isotopes for TheAME2020atomicmassevaluation(I).Evaluationof
225Ac and 227Th radiotherapeutics, Nature Chemistry inputdata,andadjustmentprocedures*,ChinesePhysics

## 13 (2021). C 45, 030002 (2021).

[12] T.A.Bailey,J.N.Wacker,D.D.An,K.P.Carter,R.C. [24] R. Firestone, Nuclear Data Sheets for A = 24, Nuclear
Davis,V.Mocko,J.Larrabee,K.M.Shield,M.N.Lam, Data Sheets 108, 2319 (2007).
C. H. Booth, and R. J. Abergel, Evaluation of 134Ce as [25] Y.Khazov,A.Rodionov,S.Sakharov,andB.Singh,Nua PET imaging surrogate for antibody drug conjugates clear Data Sheets for A=132, Nuclear Data Sheets 104,
incorporating225Ac,NuclearMedicineandBiology110- 497 (2005).
111, 28 (2022). [26] J.T.Morrell,Curie: Apythontoolkittoaidintheanal-
[13] K. N. Bobba, A. P. Bidkar, N. Meher, C. Fong, ysis of experimental nuclear data (2019–), [Online; ac-
A. Wadhwa, S. Dhrona, A. Sorlin, S. Bidlingmaier, cessed January 24, 2024.].
B. Shuere, J. He, D. M. Wilson, B. Liu, Y. Seo, [27] T. Vidmar, M. Korun, A. Likar, and R. Martinˇciˇc, A
H. F. VanBrocklin, and R. R. Flavell, Evaluation semi-empiricalmodeloftheefficiencycurveforextended
of 134Ce/134La as a PET Imaging Theranostic Pair sourcesingamma-rayspectrometry,NuclearInstruments
for 225Ac alpha-Radiotherapeutics, Journal of Nuclear and Methods in Physics Research Section A: Acceler-
Medicine 10.2967/jnumed.122.265355 (2023). ators, Spectrometers, Detectors and Associated Equip-
[14] A. Sonzogni, Nuclear Data Sheets for A = 134, Nuclear ment 470, 533 (2001).
Data Sheets 103, 1 (2004). [28] Y. Khazov, A. Rodionov, and F. Kondev, Nuclear Data
[15] F.Ta´rka´nyi,A.Hermanne,F.Ditro´i,andS.Taka´cs,Ac- SheetsforA=133,NuclearDataSheets112,855 (2011).
tivation cross section data of proton induced nuclear re- [29] M. Martin, Nuclear Data Sheets for A = 152, Nuclear
actions on lanthanum in the 34–65 MeV energy range Data Sheets 114, 1497 (2013).
and application for production of medical radionuclides, [30] H. Junde, H. Su, and Y. Dong, Nuclear Data Sheets for
Journal of Radioanalytical and Nuclear Chemistry 312, A = 56, Nuclear Data Sheets 112, 1513 (2011).
691 (2017). [31] M. J. Berger, J. H. Hubbell, S. M. Seltzer, J. Chang,
[16] Morrell,JonathanT.,Voyles,AndrewS.,Basunia,M.S., J. S. Coursey, R. Sukumar, D. S. Zucker, and K. Olsen,
Batchelder, Jon C., Matthews, Eric F., and Bernstein, XCOM: Photon cross section database (version 1.5),
Lee A., Measurement of 139La(p,x) cross sections from (2010).
35–60MeVbystacked-targetactivation,Eur.Phys.J.A [32] J. H. Hubbell and S. M. Seltzer, Tables of X-ray mass
56, 13 (2020). attenuation coefficients and mass energy-absorption co-
[17] K. Becker, E. Vermeulen, C. Kutyreff, E. O’Brien, efficients 1 keV to 20 MeV for elements Z= 1 to 92
J. Morrell, E. Birnbaum, L. Bernstein, F. Nortier, and and48additionalsubstancesofdosimetricinterest,Tech.
J.Engle,Crosssectionmeasurementsforprotoninduced Rep. (National Inst. of Standards and Technology-PL,
reactionsonnaturalLa,NuclearInstrumentsandMeth- Gaithersburg, MD (United States, 1995).
ods in Physics Research Section B: Beam Interactions [33] H.Bateman,Thesolutionofasystemofdifferentialequawith Materials and Atoms 468, 81 (2020). tions occurring in the theory of radioactive transforma-
[18] S. Qaim, New directions in nuclear data research tions, In Proc. Campridge Philos. Soc. 15, 423 (1910).
for accelerator-based production of medical radionu- [34] N. Nica, Nuclear Data Sheets for A=140, Nuclear Data
clides,JournalofRadioanalyticalandNuclearChemistry Sheets 154, 1 (2018).
(2024). [35] G. Battistoni, T. Boehlen, F. Cerutti, P. W. Chin,
[19] A. S. Voyles, L. A. Bernstein, E. R. Birnbaum, J. W. L. S. Esposito, A. Fasso`, A. Ferrari, A. Lechner,
Engle,S.A.Graves,T.Kawano,A.M.Lewis,andF.M. A. Empl, A. Mairani, A. Mereghetti, P. G. Ortega,
Nortier, Excitation functions for (p,x) reactions of nio- J. Ranft, S. Roesler, P. R. Sala, V. Vlachoudis, and
bium in the energy range of Ep=40–90MeV, Nuclear G. Smirnov, Overview of the FLUKA code, Annals of
Instruments and Methods in Physics Research Section Nuclear Energy 82, 10 (2015), joint International Con-
B:BeamInteractionswithMaterialsandAtoms429,53 ference on Supercomputing in Nuclear Applications and
(2018). Monte Carlo 2013, SNA + MC 2013. Pluri- and Trans-
[20] S. A. Graves, P. A. Ellison, T. E. Barnhart, H. F. Val- disciplinarity, Towards New Modeling and Numerical
dovinos, E. R. Birnbaum, F. M. Nortier, R. J. Nickles, Simulation Paradigms.
andJ.W.Engle,Nuclearexcitationfunctionsofproton- [36] A. Hermanne, A. V. Ignatyuk, R. Capote, B. V. Carlinducedreactions(Ep=35–90MeV)fromFe,Cu,andAl, son, J. W. Engle, M. A. Kellett, T. Kib´edi, G. Kim,
Nuclear Instruments and Methods in Physics Research F. G. Kondev, M. Hussain, O. Lebeda, A. Luca, Y. Na-
Section B: Beam Interactions with Materials and Atoms gai, H. Naik, A. L. Nichols, F. M. Nortier, S. V. Surya-
386, 44 (2016). narayana, S. Tak´acs, F. T. Ta´rka´nyi, and M. Verpelli,
[21] M. B. Fox, A. S. Voyles, J. T. Morrell, L. A. Bernstein, Reference Cross Sections for Charged-particle Monitor
A.M.Lewis,A.J.Koning,J.C.Batchelder,E.R.Birn- Reactions, Nuclear Data Sheets 148, 338 (2018).

<!-- Page 22 -->

22
[37] J. F. Ziegler, M. Ziegler, and J. Biersack, SRIM – The F.Ta´rka´nyi, V.Varlamov, J.Wang, S. Yang, V.Zerkin,
stoppingandrangeofionsinmatter(2010),NuclearIn- and Y. Zhuang, Towards a More Complete and Accustruments and Methods in Physics Research Section B: rate Experimental Nuclear Reaction Data Library (EX-
Beam Interactions with Materials and Atoms 268, 1818 FOR): InternationalCollaborationBetweenNuclearRe-
(2010),19thInternationalConferenceonIonBeamAnal- actionDataCentres(NRDC),NuclearDataSheets120,
ysis. 272 (2014).
[38] D. Rochman, A. J. Koning, J. C. Sublet, M. Fleming, [50] P. K. Joshi, B. Singh, S. Singh, and A. K. Jain, Nuclear
E.Bauge,S.Hilaire,P.Romain,B.Morillon,H.Duarte, Data Sheets for A = 139, Nuclear Data Sheets 138, 1
S.Goriely,etal.,TheTENDLlibrary: Hope,realityand (2016).
future, in EPJ web of conferences, Vol. 146 (EDP Sci- [51] E.BrowneandJ.Tuli,NuclearDataSheetsforA=137,
ences, 2017) p. 02006. Nuclear Data Sheets 108, 2173 (2007).
[39] M. Herman, R. Capote, B. Carlson, P. Obloˇzinsky´, [52] E.McCutchan,NuclearDataSheetsforA=136,Nuclear
M. Sin, A. Trkov, H. Wienke, and V. Zerkin, EMPIRE: Data Sheets 152, 331 (2018).
Nuclear Reaction Model Code System for Data Evalua- [53] B. Singh, A. A. Rodionov, and Y. L. Khazov, Nuclear
tion,NuclearDataSheets108,2655 (2007),specialIssue Data Sheets for A = 135, Nuclear Data Sheets 109, 517
on Evaluations of Neutron Cross Sections. (2008).
[40] M. Blann and J. Bisplinghoff, Code AL- [54] Y. Khazov, I. Mitropolsky, and A. Rodionov, Nuclear
ICE/LIVERMORE 82 (1982). DataSheetsforA=131,NuclearDataSheets107,2715
[41] A. Koning and M. Duijvestijn, A global pre-equilibrium (2006).
analysis from 7 to 200 MeV based on the optical model [55] B.Singh,NuclearDataSheetsforA=130,NuclearData
potential, Nuclear Physics A 744, 15 (2004). Sheets 93, 33 (2001).
[42] M. B. Fox, A. S. Voyles, J. T. Morrell, L. A. Bernstein, [56] J. Timar, Z. Elekes, and B. Singh, Nuclear Data Sheets
J. C. Batchelder, E. R. Birnbaum, C. S. Cutler, A. J. for A = 129, Nuclear Data Sheets 121, 143 (2014).
Koning, A. M. Lewis, D. G. Medvedev, F. M. Nortier, [57] Z. Elekes and J. Timar, Nuclear Data Sheets for A =
E. M. O’Brien, and C. Vermeulen, Measurement and 128, Nuclear Data Sheets 129, 191 (2015).
modelingofproton-inducedreactionsonarsenicfrom35 [58] A.Hashizume,NuclearDataSheetsforA=127,Nuclear
to 200 MeV, Phys. Rev. C 104, 064615 (2021). Data Sheets 112, 1647 (2011).
[43] V. Alexandryan, G. Ivazyan, A. Balabekyan, A. Danag- [59] H. Iimura, J. Katakura, and S. Ohya, Nuclear Data
ulyan,V.Kalinnikov,V.Stegailov,andJ.Fra´na,Studyof Sheets for A=126, Nuclear Data Sheets 180, 1 (2022).
isomericratiosofproton-nucleuscrosssectionsontiniso- [60] J. Katakura, Nuclear Data Sheets for A = 125, Nuclear
topes, Physics of Atomic Nuclei - PHYS ATOM NUCL- Data Sheets 112, 495 (2011).
ENGL TR 59, 560 (1996). [61] J. Chen, Nuclear Data Sheets for A=123, Nuclear Data
[44] A. Balabekyan, A. Danagulyan, J. Drnoyan, N. De- Sheets 174, 1 (2021).
mekhina, J. Adam, V. Kalinnikov, M. Krivopustov, [62] E. Browne and J. Tuli, Nuclear Data Sheets for A = 65,
V. Pronskikh, V. Stegailov, A. Solnyshkin, P. Caloun, Nuclear Data Sheets 111, 2425 (2010).
and V. Tsoupko-Sitnikov, Investigation of spallation re- [63] A. L. Nichols, B. Singh, and J. K. Tuli, Nuclear Data
actions on 120 Sn and ( d, xn ), ( d, pxn ), ( p, xn ), SheetsforA=62,NuclearDataSheets113,973 (2012).
and(p,pxn)reactionsonenrichedtinisotopes,Physics [64] K.ZuberandB.Singh,NuclearDataSheetsforA=61,
of Atomic Nuclei - PHYS ATOM NUCL-ENGL TR 68, Nuclear Data Sheets 125, 1 (2015).
171 (2005). [65] E. Browne and J. Tuli, Nuclear Data Sheets for A = 60,
[45] T. Kawano, CoH3: The Coupled-Channels and Hauser- Nuclear Data Sheets 114, 1849 (2013).
Feshbach Code, in Compound-Nuclear Reactions, edited [66] M. S. Basunia, Nuclear Data Sheets for A=59, Nuclear
by J. Escher, Y. Alhassid, L. A. Bernstein, D. Brown, Data Sheets 151, 1 (2018).
C.Fr¨ohlich,P.Talou,andW.Younes(SpringerInterna- [67] C. D. Nesaraja, S. D. Geraedts, and B. Singh, Nuclear
tional Publishing, Cham, 2021) pp. 27–34. Data Sheets for A = 58, Nuclear Data Sheets 111, 897
[46] S. Goriely, S. Hilaire, and A. J. Koning, Improved mi- (2010).
croscopicnuclearleveldensitieswithintheHartree-Fock- [68] M.Bhat,NucleardatasheetsupdateforA=57,Nuclear
Bogoliubovpluscombinatorialmethod,Phys.Rev.C78, Data Sheets 67, 195 (1992).
064307 (2008). [69] H.Junde,NuclearDataSheetsforA=55,NuclearData
[47] S. Goriely, S. Hilaire, S. P´eru, and K. Sieja, Gogny- Sheets 109, 787 (2008).
HFB+QRPAdipolestrengthfunctionanditsapplication [70] H. Junde and H. Su, Nuclear Data Sheets for A = 54,
to radiative nucleon capture cross section, Phys. Rev. C Nuclear Data Sheets 107, 1393 (2006).
98, 014327 (2018). [71] J. Huo, S. Huo, and C. Ma, Nuclear Data Sheets for A
[48] A. J. Koning and J. P. Delaroche, Local and global nu- = 52, Nuclear Data Sheets 108, 773 (2007).
cleon optical models from 1 keV to 200 MeV, Nuclear [72] J. Wang and X. Huang, Nuclear Data Sheets for A=51,
Physics A 713, 231 (2003). Nuclear Data Sheets 144, 1 (2017).
[49] N. Otuka, E. Dupont, V. Semkova, B. Pritychenko, [73] J. Chen, Nuclear Data Sheets for A=48, Nuclear Data
A. Blokhin, M. Aikawa, S. Babykina, M. Bossant, Sheets 179, 1 (2022).
G. Chen, S. Dunaeva, R. Forrest, T. Fukahori, N. Fu- [74] T. Burrows, Nuclear Data Sheets for A = 47, Nuclear
rutachi, S. Ganesan, Z. Ge, O. Gritzay, M. Herman, Data Sheets 108, 923 (2007).
S. Hlavaˇc, K. Kato˜, B. Lalremruata, Y. Lee, A. Mak- [75] S.-C.Wu,NuclearDataSheetsforA=46,NuclearData
inaga, K. Matsumoto, M. Mikhaylyukova, G. Pikulina, Sheets 91, 1 (2000).
V. Pronyaev, A. Saxena, O. Schwerer, S. Simakov, [76] J.ChenandB.Singh,NuclearStructureandDecayData
N. Soppera, R. Suzuki, S. Taka´cs, X. Tao, S. Taova, for A=44 Isobars, Nuclear Data Sheets 190, 1 (2023).

<!-- Page 23 -->

23
[77] B. Singh and J. Chen, Nuclear Data Sheets for A = 43,
Nuclear Data Sheets 126, 1 (2015).
[78] J. Chen and B. Singh, Nuclear Data Sheets for A = 42,
Nuclear Data Sheets 135, 1 (2016).
[79] M.S.Basunia,NuclearDataSheetsforA=22,Nuclear
Data Sheets 127, 69 (2015).

### Appendix A: Cross Sections


### Plotsofadditionalcrosssectionsmeasuredinthiswork

that were not discussed in the main text are shown in
Figs. 17 and 18.
Plotsofthemonitorreactioncrosssectionsthatwere
extrapolatedtothe100–200MeVenergyrangeareshown
in Fig. 19, in comparison with the “effective” cross sections that are constituted by the measured beam currents.

<!-- Page 24 -->

24
17.5
15.0
12.5
10.0
7.5
5.0
2.5
0.0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)129mBa
(c)

## Tendl-2023 60


### TALYS-2.0 (default)

TALYS-2.0 (adjusted) 50
TALYS-1.9 (M.B. Fox)
This Work
40
30
20
10
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)128Ba
(c)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)
This Work
50
40
30
20
10
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)127Xe
(c)
60

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted) 50
TALYS-1.9 (M.B. Fox)
This Work 40
30
20
10
0
40 60 80 100 120 140 160 180 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)127Cs
(c)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)
This Work
1.2
1.0
0.8
0.6
0.4
0.2
0.0
40 60 80 100 120 140 160 180 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)126I
(i)
10
8

## Tendl-2023

TALYS-2.0 (default)
6
TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)
This Work 4
2
0
40 60 80 100 120 140 160 180 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)126Ba
(c)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)

### This Work

FIG. 17: Comparison of measured cross sections to TENDL-2023 and TALYS-2.0 predictions using default
parameters, the parameter adjustments of Fox et al., and the adjustments performed in this work [21].

<!-- Page 25 -->

25
25
20
15
10
5
0
40 60 80 100 120 140 160 180 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)125Xe
(c)

## Tendl-2023

TALYS-2.0 (default) 30

### TALYS-2.0 (adjusted)

TALYS-1.9 (M.B. Fox) 25
This Work
20
15
10
5
0
40 60 80 100 120 140 160 180 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)125Cs
(c)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)
This Work
7
6
5
4
3
2
1
0
40 60 80 100 120 140 160 180 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)123Xe
(c)

## Tendl-2023 2.5


### TALYS-2.0 (default)


### TALYS-2.0 (adjusted)

TALYS-1.9 (M.B. Fox) 2.0
This Work
1.5
1.0
0.5
0.0
40 60 80 100 120 140 160 180 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
139La(p,x)123I
(i)

## Tendl-2023


### TALYS-2.0 (default)

TALYS-2.0 (adjusted)
TALYS-1.9 (M.B. Fox)

### This Work

FIG. 18: Comparison of measured cross sections to TENDL-2023 and TALYS-2.0 predictions using default
parameters, the parameter adjustments of Fox et al., and the adjustments performed in this work [21].

<!-- Page 26 -->

26
50
40
30
20
10
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
27Al(p,x)22Na
IAEA CP-Reference (2017)
Literature Data
This Work
15
10
5
0
0 50 100 150 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
27Al(p,x)24Na
IAEA CP-Reference (2017)

### Fit

Literature Data
This Work
20
15
10
5
0
40 60 80 100 120 140 160 180 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
natCu(p,x)56Co
IAEA CP-Reference (2017)

### Fit 80

Literature Data
This Work
60
40
20
0
25 50 75 100 125 150 175 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
natCu(p,x)58Co
IAEA CP-Reference (2017)
Literature Data
This Work
102
101
100
0 50 100 150 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
natCu(p,x)62Zn
IAEA CP-Reference (2017)

### Fit

Literature Data 102
This Work
101
100
0 50 100 150 200
Proton Energy (MeV)
)bm(
noitceS
ssorC
natCu(p,x)65Zn
IAEA CP-Reference (2017)

### Fit

Literature Data

### This Work

FIG. 19: Experimental and evaluated monitor cross sections for the production of 22Na (top-left), 24Na (top-right),
56Co (middle-left), 58Co (middle-right), 62Zn (bottom-left) and 65Zn (bottom-right) [36].

<!-- Page 27 -->

27
Appendix B: Stack Design TABLE IX: Details of the stack used in the BNL
irradiation. Uncertainties are listed in the least
significant digit, that is, 17.32(31) means 17.32 ± 0.31.

### A list of every component of the experimental stacks

used in both irradiations can be found in Table VIII for Foil Id Compound ∆x (mm) ρ∆x (mg/cm2)
the LANL irradiation and Table IX for the BNL irradia-
La01 La 0.028 17.32(31)
tion.
Cu01 Cu 0.021 18.81(26)

### Al01 Al 0.0267 7.19(13)

TABLE VIII: Details of the stack used in the LANL

### D1 Cu 5.11 4570

irradiation. Uncertainties are listed in the least La02 La 0.0272 16.77(30)
significant digit, that is, 15.51(28) means 15.51 ± 0.28. Cu02 Cu 0.0206 18.39(26)

### Al02 Al 0.0274 7.40(14)

Foil Id Compound ∆x (mm) ρ∆x (mg/cm2) D2 Cu 4.46 3990

### La03 La 0.0276 17.02(31)

La01 La 0.0251 15.51(28) Cu03 Cu 0.0212 18.98(26)
Cu01 Cu 0.0213 19.05(26) Al03 Al 0.0265 7.15(13)
Ti01 Ti 0.0344 15.56(19) D3 Cu 4.46 3990

### D1 Cu 1.02 909 La04 La 0.0279 17.24(31)

La02 La 0.0288 17.81(32) Cu04 Cu 0.0211 18.86(26)
Cu02 Cu 0.0214 19.15(27) Al04 Al 0.0269 7.26(13)
Ti02 Ti 0.0346 15.65(19) D4 Cu 4.12 3690

### D2 Cu 0.794 710 La05 La 0.0274 16.92(31)

La03 La 0.0286 17.67(32) Cu05 Cu 0.0215 19.21(27)
Cu03 Cu 0.0208 18.61(26) Al05 Al 0.0269 7.26(13)

### Ti03 Ti 0.034 15.37(18) D5 Cu 3.7 3310


### D3 Cu 0.663 593 La06 La 0.0277 17.09(31)

La04 La 0.025 15.45(28) Cu06 Cu 0.0214 19.11(27)
Cu04 Cu 0.0214 19.11(27) Al06 Al 0.027 7.29(13)

### Ti04 Ti 0.034 15.37(18) D6 Cu 3.7 3310


### D4 Cu 0.67 599 La07 La 0.0243 14.99(27)

La05 La 0.0251 15.48(28) Cu07 Cu 0.0211 18.92(26)
Cu05 Cu 0.0215 19.20(27)
Ti05 Ti 0.0346 15.64(19)

### D5 Al 1.53 414

La06 La 0.0243 14.98(27)
Cu06 Cu 0.0213 19.05(26)
Ti06 Ti 0.0339 15.30(18)

### D6 Al 1.2 324

La07 La 0.0283 17.47(32)
Cu07 Cu 0.0215 19.24(27)
Ti07 Ti 0.0343 15.49(19)

### D7 Al 1.02 275


### La08 La 0.0246 15.17(27)

Cu08 Cu 0.0213 19.10(27) Appendix C: Relevant Nuclear Data
Ti08 Ti 0.0348 15.72(19)

### D8 Al 1.02 275


### La09 La 0.0241 14.85(27)

Theprincipalgamma-raydecaydatausedintheacti-

### Cu09 Cu 0.0208 18.65(26)

vation analysis of the lanthanum foils are given in Table

### Ti09 Ti 0.0343 15.52(19)

X. The principal gamma-ray decay data used in the ac-

### D9 Al 1.02 275

La10 La 0.0305 18.81(34) tivation analysis of the aluminum, copper and titanium
Cu10 Cu 0.0208 18.63(26) monitor foils are given in Table XI.
Ti10 Ti 0.0334 15.11(18)

<!-- Page 28 -->

28
TABLE X: Principle γ-ray data for lanthanum TABLE XI: Principle γ-ray data for monitor foil
products, from ENSDF [14, 25, 28, 50–61]. products, from ENSDF [24, 30, 62–79]. Uncertainties
Uncertainties are listed in the least significant digit, are listed in the least significant digit, that is, 243.93(9)
that is, 137.641(20) d means 137.641 ± 0.020 d. d means 243.93 ± 0.09 d.
Isotope γ Energy (keV) I (%) T Isotope γ Energy (keV) I (%) T
γ 1/2 γ 1/2
139Ce 165.8575 79.90(5) 137.641(20) d 65Zn 1115.539 50.04(10) 243.93(9) d
137Ce 447.15 1.680(84) 9.0(3) h 63Zn 669.62 8.20(41) 38.47(5) min
137mCe 254.29 11.1(4) 1.433(13) d 962.06 6.5(4)
136Cs 818.514 99.7(50) 13.16(3) d 62Zn 596.56 26.0(13) 9.26(2) h
340.547 42.2(13) 548.35 15.3(14)
135Ce 265.56 41.8(14) 17.7(3) h 61Cu 282.956 12.20(61) 3.333(5) h
300.07 23.5(5) 656.008 10.8(20)
135La 480.51 1.520(76) 19.5(2) h 60Cu 1332.5 88.0(44) 23.7(4) min
135mBa 268.218 16.00(40) 1.1958(83) d 1791.6 45.4(23)
134Ce 130.4 0.209(15) 3.16(4) d 60Co 1332.492 99.9826(6) 5.27113(38) y
134La 604.721 5.04(20) 6.45(16) min 1173.228 99.85(3)
133Ce 97.261 46.0(7) 1.617(67) h 59Fe 1099.245 56.5(18) 44.495(9) d
76.9 15.9(23) 1291.59 43.2(14)
133mCe 477.22 39.3(20) 4.9(4) h 58Co 810.7593 99.4(50) 70.86(6) d
58.39 19.3(4) 57Ni 1377.63 81.7(24) 1.4833(25) d
133La 278.835 2.44(13) 3.912(8) h 127.164 16.7(5)
302.38 1.61(8) 57Co 122.06065 85.60(17) 271.74(6) d
133mBa 275.925 17.69(88) 1.6208(42) d 136.47356 10.68(8)
133Ba 356.0129 62.0(31) 10.516(19) y 56Ni 158.38 98.8(10) 6.075(10) d
80.9979 32.9(3) 749.95 49.5(12)
132Ce 182.11 77.4(39) 3.51(11) h 56Co 846.77 99.9(50) 77.233(27) d
155.37 10.5(5) 1238.288 66.46(12)
132La 464.55 76.0(6) 4.8(2) h 56Mn 846.7638 98.8(49) 2.5789(1) h
567.14 15.7(15) 1810.726 26.9(4)
132mLa 135.8 49.0(4) 24.3(5) min 55Co 931.1 75.0(38) 17.53(3) h
390.51 4.8(9) 477.2 20.2(17)
132Cs 667.714 97.6(49) 6.480(6) d 54Mn 834.848 99.976(1) 312.05(4) d
131La 108.081 25.0(8) 59.0(2) min 52Mn 1434.092 100.0(14) 5.591(3) d
417.783 18.0(6) 935.544 94.5(13)
131Ba 496.321 48.0(24) 11.50(6) d 51Cr 320.0824 9.91(1) 27.7010(11) d
123.804 29.8(3) 48V 983.525 99.98(4) 15.9735(25) d
130La 357.4 81.0(4) 8.7(1) min 1312.106 98.2(3)
550.7 25.9(19) 48Sc 1037.522 97.60(70) 1.8196(37) d
129Ba 214.3 13.4(7) 2.23(11) h 175.361 7.48(10)
220.83 8.5(4) 47Sc 159.381 68.30(40) 3.34920(60) d
129mBa 1459.1 50.0(2) 2.16(2) h 46Sc 1120.545 99.9870(10) 83.790(40) d
202.38 33.7(6) 889.277 99.9840(10)
129Cs 371.918 30.6(17) 1.3358(25) d 44Sc 1157.02 99.90(40) 3.970(40) h
411.49 22.3(12) 44mSc 271.241 86.70(30) 2.4421(42) d
128Ba 273.44 14.50(72) 2.43(5) d 1126.06 1.200(60)
128Cs 442.901 26.8(13) 3.62(2) min 43K 372.76 86.8(43) 22.30(10) h
526.557 2.41(12) 617.49 79.20(60)
127Cs 411.95 62.9(31) 6.25(10) h 42K 1524.6 18.08(90) 12.360(12) h
124.7 11.38(22) 24Na 1368.626 99.9936(15) 14.997(12) h
127Xe 202.86 68.7(34) 36.4(1) d 2754.007 99.855(5)
172.132 25.7(9) 22Na 1274.537 99.940(14) 2.6027(10) y
126Ba 233.6 19.6(18) 1.667(33) h
257.6 7.6(7)
126I 388.633 35.6(6) 12.93(5) d
666.331 32.9(7)
125Cs 112.0 8.60(43) 46.7(1) min
712.0 3.50(18)
125Xe 188.418 53.8(27) 16.9(2) h
243.378 30.0(6)
123Xe 148.9 48.9(24) 2.08(2) h
1093.4 2.79(25)
123I 158.97 83.3(42) 13.2234(19) h