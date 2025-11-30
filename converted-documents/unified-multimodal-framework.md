---
title: "Unified Multimodal Framework"
original_file: "./Unified_Multimodal_Framework.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "agents", "fine-tuning"]
keywords: ["blockchain", "smart", "contract", "our", "transaction", "cross", "border", "framework", "transactions", "financial"]
summary: "<!-- Page 1 -->


### Smart Contracts, Smarter Payments: Innovating

Cross Border Payments and Reporting Transactions

### Maruf Ahmed Mridul Kaiyang Chang

Department of Computer Science Department of Computer Science
Rensselaer Polytechnic Institute Rensselaer Polytechnic Institute

### Troy, NY, USA Troy, NY, USA

mridum@rpi.edu changk2@rpi.edu

### Aparna Gupta Oshani Seneviratne


### Lally School of Management Department of Computer Science

Rensselaer Polytechnic Institute Rensselaer Poly"
related_documents: []
---

# Unified Multimodal Framework

<!-- Page 1 -->


### Smart Contracts, Smarter Payments: Innovating

Cross Border Payments and Reporting Transactions

### Maruf Ahmed Mridul Kaiyang Chang

Department of Computer Science Department of Computer Science
Rensselaer Polytechnic Institute Rensselaer Polytechnic Institute

### Troy, NY, USA Troy, NY, USA

mridum@rpi.edu changk2@rpi.edu

### Aparna Gupta Oshani Seneviratne


### Lally School of Management Department of Computer Science

Rensselaer Polytechnic Institute Rensselaer Polytechnic Institute

### Troy, NY Troy, NY, USA

guptaa@rpi.edu senevo@rpi.edu
Abstract—The global financial landscape is experiencing sig- bersome, opaque, and costly process that impacts consumers,
nificant transformation driven by technological advancements businesses, and financial institutions engaged in global trade
andevolvingmarketdynamics.Moreover,blockchaintechnology
and remittances.
has become a pivotal platform with widespread applications,
The quest for a solution to this problem has been onespecially in finance. Cross-border payments have emerged as
a key area of interest, with blockchain offering inherent benefits going throughout international commerce, where the need
suchasenhancedsecurity,transparency,andefficiencycompared to facilitate payments across borders has always been critto traditional banking systems. This paper presents a novel ical. In response to these enduring challenges, emerging
frameworkleveragingblockchaintechnologyandsmartcontracts
fintech solutions, particularly those involving Decentralized
toemulatecross-borderpayments,ensuringinteroperabilityand

### Finance (DeFi) using blockchain technology, could provide

compliance with international standards such as ISO20022. Key
contributionsofthispaperincludeanovelprototypeframework promising avenues that could potentially revolutionize crossforimplementingsmartcontractsandwebclientsforstreamlined border payments within the next decade [2]. Blockchain’s
transactions and a mechanism to translate ISO20022 standard inherent attributes—decentralization, immutability, and transmessages. Our framework can provide a practical solution
parency—offer a new paradigm for addressing the inefficienfor secure, efficient, and transparent cross-border transactions,
cies and complexities of traditional payment systems.
contributing to the ongoing evolution of global finance and the
emerging landscape of decentralized finance. Recognizingthetransformativepotentialofblockchaintech-
Index Terms—Blockchain, Smart Contracts, Cross-Border nology, we contribute to advancing cross-border payment
Payments, ISO20022, FinTech, Interoperability, Decentralized systems by developing a framework that leverages blockchain
Finance.
technologyandsmartcontractstoenableseamless,secure,and
efficient international transactions. Our contributions include:

## I. Introduction

• Proposing a novel framework for cross-border payments
Cross-border payments face several significant challenges
leveraging blockchain technology in an interoperable
affecting efficiency, cost, and accessibility. Traditional interecosystem.
national transactions are often slow, taking days to complete
• Implementation of the proposed framework, integrating
due to the involvement of multiple intermediaries such as
smartcontractsandwebclientstostreamlinetransactions
correspondent banks [1]. Each intermediary adds time and
and ensure transparency, efficiency, and security.
increases transaction fees, making cross-border payments ex-
• Development of mechanisms for translating ISO20022
pensive. Moreover, the lack of transparency in the process
standard messages using a web client, facilitating seamcan lead to uncertainties regarding transaction status and final
less communication and interoperability across disparate
settlement times. Regulatory compliance is another hurdle, as
systems.
transactions must adhere to the varying financial regulations
ofeachcountryinvolved,whichincludesfulfillinganti-money II. BACKGROUND
laundering (AML) and combating the financing of terror-

### A. Blockchain Technologies

ism (CFT) requirements. Additionally, currency conversion
in these transactions introduces further complexity and cost, Over the past decade, technological advancements have
with fluctuating exchange rates potentially affecting the final reshaped the landscape of these transactions, with blockchain
amounts received by beneficiaries. These issues create a cum- technology emerging as a disruptive force. One of the notable
4202
luJ
72
]EC.sc[
1v38291.7042:viXra

<!-- Page 2 -->

shifts has been the growing prominence of blockchain tech- messages for financial transactions. The abbreviation pacs
nology in facilitating cross-border payments [3]. Blockchain, standsfor“PaymentsClearingandSettlement,”andthe.008
originally introduced as the underlying technology behind identifies the specific message type for customer credit transcryptocurrencies like Bitcoin [4], has evolved into a versatile fers. These messages form the foundation of transaction manplatform with applications across various sectors, including agement within CBPR+, covering initiation, status reporting,
finance.Thedecentralizedandimmutablenatureofblockchain and error handling.
offers inherent advantages for cross-border payments, promis-

### C. Blockchain for Cross Border Payments

ing enhanced security, transparency, and efficiency compared
to traditional banking systems. As a result, academia and Emerging technologies like smart contracts and DeFi
industry have turned their attention to exploring blockchain’s present new opportunities for streamlining cross-border paypotential to revolutionize international financial transactions. ments.However,despitethepromiseofblockchainandrelated
Originally defined by Nick Szabo [5] and popularized technologies,challengespersistinachievingwidespreadadopby Vitalik Buterin on the Ethereum ecosystem [6], smart tion and scalability in cross-border payments. Many issues,
contracts are self-executing code that is deployed across a such as transaction finality, regulatory compliance, and user
distributed, decentralized blockchain network, which results experience, remain areas of active research and development
in transactions that are trackable and irreversible. Since smart [1], [12]. In exploring blockchain technology for cross-border
contracts automate and enforce the terms of agreements with- payments, blockchain interoperability emerges as a crucial
out intermediaries, they offer potential cost savings and effi- element, profoundly discussed by Mohanty et al. [13] and
ciencygainsininternationaltransactions[7].Meanwhile,DeFi Belchior et al. [14]. These studies underscore the necessity
protocols leverage blockchain technology to create decentral- of seamless integration across different blockchain systems to
ized financial ecosystems that offer open, interoperable, and enable more robust and sustainable financial infrastructures,
transparent financial services [8]. However, there is a critical which directly informs the objectives of our project.
interoperability issue among different blockchain platforms, Deng [3] analyzes the application modes and advantages of
with several blockchain interoperability platforms developed blockchain technology in cross-border payments, highlighting
to address the challenges and risks associated with adopt- its potential to address the shortcomings of traditional crossing a single blockchain implementation [9]. In our CBPR+ border trade. Deng’s insights provide valuable context for
implementation, we assumed EVM-compatible interoperable understanding the challenges and opportunities of leveraging
blockchains would interact seamlessly to ensure compliance blockchain for international transactions. Similarly, Isaksen
with international standards such as ISO20022. [15] investigates how blockchain technology may benefit
banks’ positions in the cross-border payment segment. By

### B. Cross-Border Payments and Reporting Plus (CBPR+)

exploring the potential benefits and challenges of utilizing

### CBPR+isanindustry-ledinitiativethataimstostandardize

blockchaininfinancialinstitutions,Isaksenoffersinsightsinto
global payment transactions and harmonize standards. It fothe practical implications and adoption barriers of blockchain
cusesonimprovingtheefficiencyofcross-borderpayments.It
technologyinreal-worldfinancialsystems.Thisunderstanding
utilizes the ISO20022 [10] messaging format to ensure a coniscrucialfordesigningsolutionsthatalignwiththeneedsand
sistent customer experience across geographical boundaries.
constraintsofexistingfinancialinfrastructures.He[1]analyzes

### ISO20022offersaricherandmoreflexiblestandardcompared

the broader context of digitization in cross-border payments,
to its predecessors, facilitating innovation and efficiency in
noting significant global efforts to enhance transactional efcross-border payment systems. Adopting international stanficiency. This perspective is valuable for understanding the
dards,suchasISO20022,isessentialinstandardizingcommuenvironmental and systemic changes influencing our research
nication protocols and data formats in financial transactions
direction. Meanwhile, Le Quoc et al. [16] offer a specific ex-
[11]. The adoption and impact of ISO20022 in facilitating
ample of blockchain application in the letter-of-credit system
effectivecommunicationandstandardizationinfinancialtransforinternationaltrade,presentingacasestudythatmirrorsthe
actions are critically examined by Bouille and Haase [11] and
potential applications of our research. Zilnieks and Erins [12]
further elaborated by McGill [10]. Their discussions emphaexplore cross-chain bridges to standardize distributed ledger
sizetheimportanceofthisstandardinensuringinteroperability
technologies,adiscussionparticularlyrelevanttoourproject’s
andefficiency,whichiscrucialfortheframeworkourresearch
aim to enable smooth interoperable transactions across difseeks to develop.
ferent blockchain platforms. Another related work by Scha¨r

### TheCBPR+processinvolvesaseriesofISO20022message

[8] discusses DeFi, providing insights into the infrastructure
exchanges facilitating seamless fund transfers across borders.
and potential of blockchain-based financial markets to offer

### Key messages include but are not limited to the following:

more open, interoperable, and transparent services. Together,
• pacs.008:CustomerCreditTransferInitiationmessage these contributions provide a comprehensive backdrop against
• pacs.002: Payment Status Report message which our research is situated. They illuminate the current
• pacs.004: Payment Return message state of blockchain technology in financial applications and
The term pacs.008 is a specific identifier within the highlight the diverse approaches and potential enhancements
ISO 20022 standard for financial messaging, defining various that our project could integrate. By leveraging these insights,

<!-- Page 3 -->

our framework aims to contribute effectively to the evolving • Account Management: This smart contract manages
landscape of global financial transactions, offering solutions two distinct account types: Nostro Accounts and General
that are not only technologically advanced but also aligned Accounts. Nostro Accounts facilitate holding funds in
with global financial practices and standards. foreigncurrencies,essentialforcross-bordertransactions,
Our proposed solution aims to enable seamless, secure, while General Accounts cater to everyday transactional
and efficient international transactions leveraging blockchain needs. Account creation within the contract involves
technologiesandexistingstandardstoprovideinteroperability specifying a unique account number and distinguishing
with existing systems and regulatory compliance. At the heart betweenaccounttypes.Thespecificaccountmanagement
of our transaction system lies the smart contracts, robust and actions include mapping and tracking account addresses,
autonomous entities deployed on Ethereum Virtual Machine verifying account existence and uniqueness, and main-
(EVM) compatible blockchains to demonstrate the system’s taining a state variable for tracking available funds in
interoperability for smarter payments in cross-border sce- each account.
narios. Our smart contract-based implementation embodies • Transaction Details: Solidity structs define structured
the principles of transparency, efficiency, and security within data entities to capture and process transaction dethe decentralized network and is also interoperable through tails. These structs encapsulate essential transactional
standards. information, including currency and amounts (Amount),
debtor instructions (DbtrInstruction), and com-

## Iii. Methodology

prehensive transaction metadata (MsgInfo). Mirror-
Our methodology includes a blockchain-based framework ing the ISO20022 message structures, these defined
to replicate and enhance the CBPR+ process. It uses smart structs enable the seamless integration of cross-border
contractsandwebclientstostreamlineandsecurecross-border payment transactions within the blockchain framework.
transactions within a decentralized environment. Within our For example, the following code snippet shows the
framework, the smart contract serves as an autonomous agent DbtrInstruction struct in the smart contract.
managing the logic and state of each transaction, while the struct DbtrInstruction {
web client acts as the interface between traditional banking Amount IntrBkSttlmAmt;
address DbtrAgt;
systems and a blockchain. Together, they emulate the CBPR+
string DbtrAcct;
process in a distributed ledger environment. string DbtrAgtIsoMsg;
address NxtAgt;

### A. Detailed System Architecture }

To illustrate our framework’s functionality, let’s consider For this specific data structure, the web client exa simulated CBPR+ transaction scenario involving multiple tracts the required information from the XML-formatted
banks across different blockchains. Refer to Figure 1 for a pacs.008 message using the following Python funcdepiction of the following discussion. The workflow initiates tion, where the specific attributes correspond directly to
with the debtor, who provides transaction instructions. The theISO20022dataschematofacilitateeaseofintegration
debtor’sagentbank(BankA)communicatestheseinstructions and maintain consistency. This implementation enhances
to its corresponding smart contract, which debits the debtor’s interoperability and compatibility with external systems
account and emits a confirmation message. Subsequently, the and messaging standards by standardizing transactional
web client generates an ISO20022 pacs.008 message for data formats.
the next agent and triggers the respective smart contract. This def get_debtor_instructions(xml_data):
process iterates sequentially through intermediary banks until
dict_data = convert_to_dict(xml_data)
reaching the creditor agent, concluding the transaction.
1) Smart Contracts: Engineered to emulate and enhance dbtr_instruction = {
"IntrBkSttlmAmt": dict_data[’Document’]
the CBPR+ methodology, the smart contracts encapsulate the
[’FIToFICstmrCdtTrf’][’CdtTrfTxInf’]
essential functions and rules governing cross-border payment [’IntrBkSttlmAmt’],
transactions, from initialization and access control to transac- "DbtrAgt": dict_data[’Document’]
[’FIToFICstmrCdtTrf’][’CdtTrfTxInf’]
tional validation and event-driven communication.
[’DbtrAgt’][’FinInstnId’][’BICFI’],
• Initialization and Access Control: This smart contract "DbtrAcct": dict_data[’Document’]
[’FIToFICstmrCdtTrf’][’CdtTrfTxInf’]
establishesanaccesscontrolhierarchyupondeployment,
[’DbtrAcct’][’Id’][’Othr’][’Id’],
designating the deploying address as the owner with ad- "DbtrAgtIsoMsg": xml_data,
ministrative privileges. Role-based access control mech- "NxtAgt": dict_data[’Document’]
[’FIToFICstmrCdtTrf’][’GrpHdr’]
anisms ensure that only authorized entities can execute
[’InstdAgt’][’FinInstnId’][’BICFI’]
critical functions that alter the contract’s state or con- }
figuration. By enforcing access restrictions, the contract
return dbtr_instruction
safeguards against unauthorized manipulation or misuse,
preserving the integrity and reliability of the transaction • Transactional Methods: The key to the smart contract’s
functionality is transactional methods, which are resystem.

<!-- Page 4 -->

Fig.1. WorkflowoftheFrameworkforanExampleTransactioninvolvingaDebtorandCreditorforaCrossBorderPayment.
sponsible for initiating, validating, and processing cross- Uponparsingtheincomingmessage,thewebclientstrucborder payment transactions. The functions in the smart tures all the transaction requests in a format compatible
contract,alongsidemakingthetransactions,serveasgate- with the smart contract’s defined data structures. This
keepers, ensuring the security, integrity, and validity of process involves mapping parsed data to corresponding
fundtransfers.Theyvalidateaccountexistence,balances, fields within the DbtrInstruction struct, ensuring
and transaction parameters before initiating fund trans- integration with the contract’s transactional methods.
fers. They also incorporate comprehensive checks such Moreover, the web client continuously monitors contract
as control sum verification and nostro account balance events to facilitate the modification of ISO messages.
validation. When triggered by events such as MakeTransfer or
• Event-Driven Confirmation Mechanism: The PassISOMessageAlong emitted by the smart consmart contract employs an event-driven confirmation tract, the web client takes in the updated ISO message
mechanism to facilitate real-time communication and as an instruction set for the next agent in the process.
transactional synchronization. At crucial transactional • Transaction Initiation and Propagation: Facilitating
milestones, the contract emits events such as transactioninitiationandpropagationisacorefunctionof
MakeTransfer and PassISOMessageAlong, the web client, serving as the intermediary between user
signaling transaction state changes and facilitating instructionsandsmartcontractexecution.Uponreceiving
communication with external systems, including web debtorinstructions,thewebclientinitiatestransactionsby
clients that correspond to different organizations within interfacingwiththeinitiate_transferfunctionof
our simulated system. These events serve as immutable the smart contract.
audit trails, providing a transparent history of transaction In this process, the web client extracts pertinent details
actions and enabling stakeholders to verify transactional from the debtor’s instructions, such as payment amounts,
integrity and compliance with regulatory standards. beneficiaryinformation,andtransactionmetadata.Itthen
By leveraging event-driven mechanisms, the contract passesthisstructureddatatothesmartcontract,initiating
enhances transparency, accountability, and trust within the transaction. Concurrently, the web client monitors
the cross-border payment ecosystem. transaction progress through emitted contract events,
2) Web Client: The web client plays an important role updating transactional states and facilitating subsequent
within our framework, bridging traditional banking systems actions. As transaction events unfold, the web client
andthedecentralizedblockchainnetwork.Itsprimaryfunction dynamically propagates transaction updates to relevant
is to orchestrate the flow of cross-border payment transac- parties within the blockchain network.
tions, ensuring seamless communication, data integrity, and • Event Handling: The web client’s event-handling catransactionaltransparency.Thewebclient’smajorrolesareas pabilities are important in maintaining transactional infollows: tegrity and facilitating real-time communication between
• Message Parsing and Construction: This component theblockchainframeworkandexternalsystems.Designed
ensures the accurate interpretation and transmission of to respond to contract events triggered during transaction
ISO20022 messages within our framework. The web execution, the web client employs event-driven mechaclientdissectsincomingpacs.008messages,extracting nisms to synchronize transactional states and propagate
essential transaction details such as the debtor’s instruc- updates.
tions, payment amounts, and beneficiary information. Upon receiving event notifications from the smart con-

<!-- Page 5 -->

tract, the web client dynamically triggers corresponding • Audit Trails: Our framework maintains comprehenactions based on predefined event handlers. For instance, sive audit trails through event-driven mechanisms, prowhen notified of a MakeTransfer event indicating viding transparent and verifiable transaction histothe need to craft an outgoing ISO message, the web ries. Contract events such as MakeTransfer and
client invokes message construction routines, incorporat- PassISOMessageAlong are recorded in immutable
ing transactional details and metadata. audit logs, capturing key transactional actions and state
Similarly, PassISOMessageAlong events signal the changes. These audit trails enable stakeholders to trace
requirement to transmit updated ISO messages to subse- transactionalactivities,verifycompliancewithregulatory
quenttransactionalparticipants,promptingthewebclient standards, and detect anomalous behavior.
to initiate message transmission protocols.
• Interaction with Smart Contract: The web client and

## Iv. Evaluation

smart contract form our framework’s backbone of trans- In this section, we evaluate the performance and costactional operations. Through seamless communication effectiveness of our blockchain-based framework for CBPR+.
channels, the web client orchestrates transaction execu- We present gas consumption metrics obtained from a local
tion and state management, leveraging the capabilities of development environment using the Ganache Command Line
the underlying smart contract infrastructure. Interface1 and the live testnet deployment on the Sepolia test
When triggered by user instructions or contract events, Ethereum network2. Additionally, we discuss the implications
the web client interfaces with the smart contract through of gas consumption on transaction fees and contract deploystructured function calls, passing relevant transactional ment costs.
dataandmetadata.Thesefunctioncallsinvokepredefined

### A. Gas Consumption Metrics

contract methods responsible for transaction initiation,
validation, and propagation, ensuring the seamless exe- Gas consumption metrics provide insights into the compucution of cross-border payment transactions. tational efficiency and resource utilization of smart contract
Furthermore, the web client monitors contract events, operationswithintheblockchainnetwork.TableIsummarizes
dynamicallyrespondingtostatechangesandtransactional the gas consumption statistics obtained from our gas report
progress. Upon receiving event notifications from the analysis during testing.
smart contract, the web client initiates corresponding
actions, updating transactional states and propagating TABLEI
transactional updates to relevant stakeholders. GASCONSUMPTIONMETRICS(GASUNITS)
The symbiotic relationship between the web client and FunctionName min avg median max #calls
the smart contract facilitates the seamless execution and create account 26660 43201 46560 69676 17
deposit 30351 38939 38939 47527 12
management of cross-border payment transactions within the
get balance 921 921 921 921 14
blockchain framework, ensuring transactional integrity, transinitiate transfer 121580 121580 126279 131428 12
parency, and efficiency. make transfer 135213 135213 140352 146192 12
B. Security Protocols The gas report provides detailed information on gas consumption for each smart contract function, including mini-
Our framework incorporates comprehensive security meamum, average, median, and maximum gas costs per funcsures at various levels of the transactional lifecycle to safetion call. These metrics offer insights into the computational
guard transactional integrity and protect sensitive financial
complexityandresourcerequirementsofindividualoperations
data.
within the smart contract.
• AccessControl:Oursmartcontractimplementsstringent
access control mechanisms, restricting critical functions B. Transaction Fees and Contract Deployment Costs
to authorized entities such as account holders or institu- Transaction fees and contract deployment costs are crittional owners. By validating user identities and permis- ical considerations for assessing the economic viability of
sions, the contract ensures that only authorized parties blockchain-basedsolutions.Thefollowingmetricsindicatethe
can execute sensitive operations, mitigating the risk of costofexecutingtransactionsanddeployingsmartcontractson
unauthorized access or manipulation. the Sepolia Testnet. The deployed contract address on Sepolia
• Transaction Integrity: Leveraging structured data and is 0x7bD82fFA76A4a45ddF468c7106536354c9cc6909.
Solidity’s type system, our smart contract enforces transactionvalidationprotocols,verifyingtransactionalparam-
1Ganache(https://archive.trufflesuite.com/ganache)isacommand-linetool
designed for Ethereum developers to create and manage personal Ethereum
eters and data integrity before processing. By encoding
blockchainsfortestinganddevelopmentpurposes.
transactionswithinpredefineddatastructuresandenforc- 2Sepolia (https://sepolia.etherscan.io) is one of the several test networks
ing type validation, the contract mitigates the risk of used by the Ethereum blockchain for development and testing purposes.
Unlike the Ethereum mainnet, where real transactions occur with actual
fraudulent or malicious transactions, safeguarding transeconomicvalue,Sepoliaprovidesacontrolledenvironmentwheredevelopers
actional integrity and consistency. cantestnewapplications,smartcontracts,andupgradeswithoutfinancialrisk.

<!-- Page 6 -->

• Transaction Fees: 0.003543387976528597 ETH we must consider certain factors when implementing smart
• Gas Fees: 3.095497367 Gwei contractsacrossvariousblockchainplatformsconcerningtheir
Transaction fees are calculated based on the gas consumed termination mechanisms [17], especially in light of regulatory
byeachtransaction,whilegasfeesrepresentthepriceperunit changes such as the EU Data Act. We may also need to
of gas specified in Gwei3. handle unexpected situations that may arise during normal
businessoperationsrelatingtocross-borderpaymentactivities,
V. DISCUSSION such as account recovery in case of a catastrophic failure in
Ourimplementationoftheblockchain-basedframeworkfor one of the entities engaged in the trade [18]. In such cases,
cross-border payments, leveraging smart contracts and web we could leverage supplementary techniques to strengthen
clients, represents a significant step towards enhancing the the smart contract logic, such as computational social choice
efficiency and security of global financial transactions. By mechanisms [19] and ontology-aided mechanisms [20]. This
replicating and streamlining the CBPR+ process within a flexibility empowers financial institutions to adapt the framedecentralized environment, our framework offers a promising work to their specific use cases while maintaining compliance
solution to the challenges associated with traditional cross- with relevant regulations.
border payment systems.
C. Message Parsing and Information Extraction

### A. Flexibility and Customizability

Similarly, the web client’s predefined instructions for mes-
One key advantage of our framework is its flexibility sage parsing and information extraction represent a starting
and customizability, which allows it to accommodate diverse pointforprocessingISO20022messageswithintheblockchain
transactional requirements and be robust against any changes framework. However, the specific information required for
to regulatory frameworks governing smart contract applica- transaction processing may vary depending on the transaction
tions.Financialinstitutionsdeployingourframeworkhavethe type and regulatory requirements. Financial institutions deflexibility to customize the smart contract logic and message ploying our framework must assess their specific information
parsingrulesaccordingtotheirspecificneedsandcompliance needs and customize the message parsing rules accordingly.
requirements. As long as the financial institutions can deter- Providing an easily configurable and extensible framework
mine which portions of the ISO20022 messages are necessary empowers financial institutions to tailor the system to their
to process their existing transactions, they can easily modify unique operational requirements while ensuring interoperabiltheextractedmessagefieldsandimplementthesmartcontract ity and compliance with industry standards.
logicwithinourframeworktoachievetheirspecificusecases. Drawingparallelsfromourpriorwork,theBlockIoTproject
Additionally,financialinstitutionscanensurecompliancewith introduced a robust mechanism for integrating data from varvarious regulatory requirements by embedding specific rules ious sources in an interoperable manner that allows seamless
and standards directly into the smart contracts. This cus- incorporation of diverse data types, ensuring comprehensive
tomization flexibility ensures the framework remains agile data availability for subsequent processing in healthcare sceand responsive to evolving market demands and regulatory narios [21]. Similarly, in our financial framework, integrating
changes. It is important to note that legacy systems must be various data sources—such as customer information, transmade blockchain-compatible to integrate with our framework. action history, and regulatory guidelines—can enhance the
Tofacilitatesmoothintegrationwithexistinglegacysystemsin completeness and accuracy of cross-border payment transacfinancial institutions, a future version of our framework could tions.Additionally,theseinformationextractionprocessescan
include Web3-enabled adapters or middleware solutions that be made more streamlined using an off-chain read-executebridgethegapbetweenthelegacyinfrastructureandoursmart transact-erase-loop[22],whichwillensurethatonlythenecescontract-based framework, ensuring seamless data flow and sarydataisprocessedandstoredon-chain,optimizingresource
operational continuity. utilizationandmaintainingprivacy,whilebeingup-to-dateand
providing higher throughput.

### B. Smart Contract Logic

The smart contract is the backbone of our transaction VI. RELATEDWORK
system, encapsulating the core functions and rules governing Emerging technologies and innovative approaches also sigcross-border payments. However, the logic embedded within nificantly enhance the security and efficiency of cross-border
the smart contract is scenario-dependent and may vary based payments. For instance, Vinayak et al. [7] propose a solution
on the type of transaction and regulatory framework. Our for the automation and transparency of smart contracts on
implementation provides a starting point for financial insti- distributedledgers,similartoourwork.However,ourresearch
tutions to build upon, allowing them to update and modify offers a more comprehensive and globally applicable soluthe smart contract logic to align with their unique business tion compared to their narrower focus on collateral manageprocesses, use cases, and regulatory obligations. However, ment within financial institutions. Furthermore, Narendra and

### Aghila[23]focusonaquantum-resistantsmartcontractmodel,

3GWei,whichisacommonlyusedunitofmeasurementinEthereum.Wei
suggesting a frontier for future-proof financial transactions
isthesmallestdenominationofEther,thenativecryptocurrencyofEthereum.
OneGWeiisequivalenttoonebillionwei. prioritizing security. However, their model does not address

<!-- Page 7 -->

interoperability, a key aspect of our framework designed to use of smart contracts on an EVM-compatible blockchain,
ensure seamless global transactions. Flynn et al. [24] presents we enforce stringent access controls and transaction integrity
a data- and language-agnostic system designed to integrate whileenablingreal-timetransactionalupdatesviaanadvanced
and analyze data from various sources in DeFi with interop- event-driven architecture. This process results in a robust syserability and scalability in mind, where they showcase how tem that reduces risks and enhances transparency throughout
different programming languages can interact with a unified thetransactionlifecycle.Additionally,theflexibilityembedded
backendsystem.However,unliketheirwork,wehavefocused withinoursmartcontractdesignallowsforcustomadaptations
on international standards such as ISO20022 in achieving to meet diverse regulatory and institutional needs, making
interoperability. Li et al. emphasize using standardized on- our system highly adaptable to future changes in the global
tological concepts to ensure interoperability and trustworthy financial landscape.
data sharing across institutions and mining transaction logs to Our research contributes to the evolving financial technoldetectanomaliesandmisuse[25].Inourframeworkforcross- ogy landscape by providing a scalable, secure, and efficient
border payments, we aim to achieve similar interoperability framework for cross-chain transactions. The adoption of this
and compliance by leveraging international standards such as framework by financial institutions and regulatory bodies can
ISO20022 and blockchain-based transactions. leadtosignificantimprovementsincross-borderpaymentpro-
Additionally, there are several efforts to automatically gen- cesses, reducing transaction times and costs while enhancing
eratesmartcontracts,whichsimplifiestheimplementationpro- compliance and security. Furthermore, by demonstrating the
cess. For example, Choudhury et al. [26], Tateishi et al. [27], feasibility and benefits of a blockchain-based approach, we
and Frantz and Nowostawski [28] have all contributed to this pave the way for future innovations that can build on our
field, each focusing on distinct applications and methods. Yet, foundational work.
all share the common objective of translating business logic Future research could explore the integration of advanced
into executable code. Another such work is the methodology machine-learning techniques for real-time fraud detection and
to automate construction payments by formalizing them into anomaly monitoring within the transaction process. Additionsmart contracts proposed by Luo, Han, et al. [29]. However, ally, expanding the framework to support multiple non-EVM
while these automation approaches facilitate smart contract blockchain platforms could further enhance interoperability
creation, they lack the precision needed for sensitive tasks and user adoption. Collaborations with regulatory bodies to
like cross-border payments. Given the complexity and critical refine and standardize smart contract protocols will be essenimportance of financial standards like ISO20022 in enabling tial to ensure the widespread acceptance and reliability of this
cross-border interoperable financial transactions, our frame- technology.
work’s tailored approach to ISO20022 translations ensures a

### In summary, our blockchain-based framework offers a

higher level of expressivity and compliance with regulatory
flexible, customizable, and secure solution for cross-border
bodies. Furthermore, Kang et al. [30] investigate the potential
payments, addressing the inefficiencies and complexities of
of Large Language Models (LLMs) to automate health intraditional financial (TradFi) systems. By integrating smart
surance processes by generating smart contracts from textual
contracts, web clients, and advanced data processing techpolicies.VanWoenseletal.[31]exploretranslatinghigh-level
niques,ourframeworksetsanewstandardforglobalfinancial
decisionlogicfromclinicalpracticeguidelinesintoexecutable
transactions, promoting transparency, compliance, and effismart contracts on blockchain platforms like Ethereum and
ciency. This innovation bridges the gap between TradFi and

### HyperledgerFabric.Boththeseworksemphasizetransforming

DeFi, leveraging the strengths of blockchain technology to
domain-specific rules and guidelines from healthcare into
enhance financial operations in both domains. By providing
smart contracts, similar to our goal of implementing crossa robust, adaptable, and secure solution, we contribute to the
border payments and reporting transactions in the finance
broadergoalofcreatingamoretransparentandefficientglobal
domain.
financial system, which will ultimately benefit consumers,
financial institutions, and regulatory authorities alike. By

## Vii. Conclusion

adoptingourframework,financialinstitutionscanbenefitfrom
Our proposed blockchain-based framework offers an inthe robustness and transparency of DeFi while maintaining
novative solution for enhancing the efficiency and security
theregulatorycomplianceandoperationalstabilityessentialto
of cross-chain transactions. By integrating smart contracts
TradFi, ultimately resulting in a more integrated and efficient
and web clients, we align closely with the CBPR+ initiative
global financial ecosystem.
and employ the ISO20022 messaging format to guarantee a
uniform user experience globally. Our framework facilitates a
seamless,secure,andefficientmechanismformanagingcross- RESOURCES
chain transactions, which are crucial in today’s globalized
blockchain economy. The source code of our implementation is available
The detailed system architecture and security protocols we athttps://github.com/blockchain-interoperability/bi-in-finance,
have developed ensure that our framework replicates and along with a video demonstration of an example transaction
augments the current CBPR+ process. Through the strategic using our implemented framework.

<!-- Page 8 -->

ACKNOWLEDGMENTS [13] D.Mohanty,D.Anand,H.M.Aljahdali,andS.G.Villar,“Blockchain
interoperability:Towardsasustainablepaymentsystem,”Sustainability,
The authors acknowledge the support from NSF IUCRC
vol.14,no.2,p.913,2022.
CRAFT Center research grant (CRAFT Grant #22008) for [14] R. Belchior, A. Vasconcelos, S. Guerreiro, and M. Correia, “A survey
this research. The opinions expressed in this publication do on blockchain interoperability: Past, present, and future trends,” ACM
ComputingSurveys(CSUR),vol.54,no.8,pp.1–41,2021.
not necessarily represent the views of NSF IUCRC CRAFT.
[15] M.Isaksen,“Blockchain:Thefutureofcrossborderpayments,”Master’s
We are also grateful for the advice from our CRAFT Industry thesis,UniversityofStavanger,Norway,2018.
Advisory Board members in shaping this work, especially [16] K.LeQuoc,P.N.Trong,H.LeVan,H.K.Vo,H.H.Luong,K.T.Dang,

### K.H.Gia,L.V.C.Phu,D.N.T.Quoc,H.T.Nguyenetal.,“of-credit

the input from Jack Pouderoyen and Giri Krishnapillai from
chain:Cross-borderexchangebasedonblockchainandsmartcontracts,”
SWIFT. InternationalJournalofAdvancedComputerScienceandApplications,
vol.13,no.8,2022.
[20] F.Mohsin,X.Zhao,Z.Hong,G.deMel,L.Xia,andO.Seneviratne,

## References

“Ontologyaidedsmartcontractexecutionforunexpectedsituations.”in
[1] D. He, “Digitalization of cross-border payments,” China Economic BlockSW/CKG@ISWC,2019,2019.
Journal,vol.14,no.1,pp.26–38,2021. [21] M. Shukla, J. Lin, and O. Seneviratne, “BlockIoT: Blockchain-based
[2] U. Bindseil and G. Pantelopoulos, “Towards the holy grail of cross- healthdataintegrationusingIoTdevices,”inAMIAAnnualSymposium
borderpayments,”2022. Proceedings, vol. 2021. American Medical Informatics Association,
[3] Q.Deng,“Applicationanalysisonblockchaintechnologyincross-border 2021,p.1119.
payment,”in5thInternationalConferenceonFinancialInnovationand [22] ——, “BlockIoT-RETEL: Blockchain and IoT based read-execute-
EconomicDevelopment(ICFIED2020). AtlantisPress,2020,pp.287– transact-erase-loop environment for integrating personal health data,”
295. in 2021 IEEE International Conference on Blockchain (Blockchain).
[4] M.Crosby,P.Pattanayak,S.Verma,V.Kalyanaramanetal.,“Blockchain IEEE,2021,pp.237–243.
technology:Beyondbitcoin,”Appliedinnovation,vol.2,no.6-10,p.71, [23] K. Narendra and G. Aghila, “Fortis-a´myna-smart contract model for
2016. crossborderfinancialtransactions,”ICTExpress,vol.7,no.3,pp.269–
[5] N. Szabo, “Smart contracts: building blocks for digital markets,” EX- 273,2021.
TROPY: The Journal of Transhumanist Thought,(16), vol. 18, no. 2, [24] C.Flynn,K.P.Bennett,J.S.Erickson,A.Green,andO.Seneviratne,
p.28,1996. “Enabling Cross-Language Data Integration and Scalable Analytics in
[6] V. Buterin et al., “A next-generation smart contract and decentralized DecentralizedFinance,”in2023IEEEInternationalConferenceonBig
applicationplatform,”whitepaper,vol.3,no.37,pp.2–1,2014. Data(BigData). IEEE,2023,pp.4290–4299.
[7] M. Vinayak, S. dos Santos, R. K. Thulasiram, P. Thulasiraman, and [25] M.Li,L.Xia,andO.Seneviratne,“Leveragingstandardsbasedontologi-
S.S.Appadoo,“Designandimplementationoffinancialsmartcontract calconceptsindistributedledgers:ahealthcaresmartcontractexample,”
services on blockchain,” in 2019 IEEE 10th Annual Information Tech- in 2019 IEEE International Conference on Decentralized Applications
nology,ElectronicsandMobileCommunicationConference(IEMCON). andInfrastructures(DAPPCON). IEEE,2019,pp.152–157.
IEEE,2019,pp.1023–1030. [26] O. Choudhury, N. Rudolph, I. Sylla, N. Fairoza, and A. Das, “Auto-
[8] F. Scha¨r, “Decentralized finance: On blockchain-and smart contract- generation of smart contracts from domain-specific ontologies and
basedfinancialmarkets,”FRBofSt.LouisReview,2021. semantic rules,” in 2018 IEEE International Conference on Internet
[9] I. Kang, A. Gupta, and O. Seneviratne, “Blockchain interoperability of Things (iThings) and IEEE Green Computing and Communications
landscape,” in 2022 IEEE International Conference on Big Data (Big (GreenCom) and IEEE Cyber, Physical and Social Computing (CP-
Data). IEEE,2022,pp.3191–3200. SCom)andIEEESmartData(SmartData). IEEE,2018,pp.963–970.
[10] R.K.McGill,“Isostandards,”inCross-BorderInvestmentWithholding [27] T. Tateishi, S. Yoshihama, N. Sato, and S. Saito, “Automatic smart
Tax: A Practical Guide for Investors and Intermediaries. Springer, contractgenerationusingcontrollednaturallanguageandtemplate,”IBM
2023,pp.211–218. JournalofResearchandDevelopment,vol.63,no.2/3,pp.6–1,2019.
[11] I. Bouille and T. Haase, “Adoption of global market practice for [28] C.K.FrantzandM.Nowostawski,“Frominstitutionstocode:Towards
payments will pave the road to a successful global migration to iso automatedgenerationofsmartcontracts,”in2016IEEE1stInternational
20022,” Journal of Payments Strategy & Systems, vol. 13, no. 2, pp. WorkshopsonFoundationsandApplicationsofSelf*Systems(FAS*W).
104–112,2019. IEEE,2016,pp.210–215.
[12] V. Zilnieks and I. Erins, “Cross-chain bridges: A potential solution [29] H. Luo, M. Das, J. Wang, and J. C. Cheng, “Construction payment
to standardising distributed ledger technology in payment systems.” automation through smart contract-based blockchain framework,” in
InformationTechnology&ManagementScience,vol.26,2023. ISARC.Proceedingsoftheinternationalsymposiumonautomationand
[17] O. Seneviratne, “The Feasibility of a Smart Contract” Kill Switch”,” roboticsinconstruction,vol.36. IAARCPublications,2019,pp.1254–
arXivpreprintarXiv:2407.10302,2024. 1260.
[18] Y.Zhu,L.Xia,andO.Seneviratne,“Aproposalforaccountrecoveryin [30] I.Kang,W.VanWoensel,andO.Seneviratne,“UsingLargeLanguage
decentralizedapplications,”in2019IEEEInternationalConferenceon Models for Generating Smart Contracts for Health Insurance from
Blockchain(Blockchain). IEEEComputerSociety,2019,pp.148–155. TextualPolicies,”arXivpreprintarXiv:2407.07019,2024.
[19] S. Liu, F. Mohsin, L. Xia, and O. Seneviratne, “Strengthening smart [31] W.VanWoensel,M.Shukla,andO.Seneviratne,“TranslatingClinical
contractstohandleunexpectedsituations,”in2019IEEEInternational Decision Logic Within Knowledge Graphs to Smart Contracts,” in
Conference on Decentralized Applications and Infrastructures (DAPP- Proceedingsofthe6thWorkshoponSemanticWebSolutionsforLarge-
CON). IEEEComputerSociety,2019,pp.182–187. ScaleBiomedicalDataAnalyticsco-locatedwithESWC2023,2023.

## Tables

**Table (Page 5):**

| FunctionName | min | avg | median | max | #calls |
|---|---|---|---|---|---|
| create account | 26660 | 43201 | 46560 | 69676 | 17 |
| deposit | 30351 | 38939 | 38939 | 47527 | 12 |
| get balance | 921 | 921 | 921 | 921 | 14 |
| initiate transfer | 121580 | 121580 | 126279 | 131428 | 12 |
| make transfer | 135213 | 135213 | 140352 | 146192 | 12 |
