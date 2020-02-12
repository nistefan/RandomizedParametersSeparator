import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:54963', '1:59183', '1:59191', '1:56167', '1:56233', '1:56421', '1:56519', '1:54790', '1:81658', '1:83581', '1:83594', '1:82440', '1:86705', '1:71139', '1:70062', '1:70101', '1:70167', '1:70187', '1:70364', '1:70395', '1:70428', '1:70558', '1:66067', '1:72345', '1:70903', '1:71053', '1:71122', '1:71142', '1:71343', '1:71345', '1:71453', '1:83477', '1:83766', '1:83890', '1:65516', '1:65527', '1:65710', '1:65698', '1:65715', '1:65866', '1:65882', '1:66061', '1:82918', '1:83207', '1:83891', '1:86834', '1:82816', '1:83348', '1:83386', '1:85956', '1:79968', '1:5106', '1:5651', '1:3967', '1:5171', '1:24889', '1:26169', '1:26192', '1:26200', '1:26227', '1:38604', '1:38486', '1:38526', '1:43112', '1:14149', '1:14264', '1:14246', '1:36418', '1:36455', '1:36521', '1:36675', '1:36821', '1:43636', '1:43668', '1:43721', '1:37186', '1:36733', '1:38091', '1:38094', '1:38159', '1:43237', '1:43308', '1:43364', '1:43407', '1:43439', '1:43392', '1:43398', '1:43846', '1:44442', '1:42237', '1:42807', '1:5328', '1:5588', '1:5678', '1:5682', '1:5763', '1:19899', '1:19978', '1:20701', '1:20343', '1:20478', '1:27011', '1:27189', '1:17583', '1:17783', '1:17874', '1:18190', '1:18309', '1:26708', '1:26791', '1:27922', '1:37601', '1:37962', '1:15770', '1:18276', '1:24398', '1:26312', '1:28371', '1:27513', '1:27534', '1:27621', '1:27586', '1:27598', '1:27604', '1:27655', '1:27726', '1:27775', '1:39673', '1:39984', '1:40677', '1:40360', '1:104054', '1:50782', '1:50926', '1:49171', '1:49872', '1:59690', '1:60069', '1:60396', '1:83704', '1:83650', '1:83671', '1:83718', '1:83799', '1:87391', '1:87336', '1:87456', '1:97734', '1:99042', '1:97927', '1:2380', '1:2810', '1:5092', '1:5305', '1:2192', '1:5409', '1:60011', '1:68605', '1:74654', '1:12589', '1:12820', '1:12876', '1:12896', '1:12916', '1:19826', '1:20280', '1:21003', '1:63563', '1:106158', '1:72568', '1:19181', '1:19410', '1:27002', '1:32121', '1:49724', '1:50671', '1:48159', '1:53760', '1:49247', '1:50239', '1:53250', '1:53878', '1:51304', '1:60018', '1:61643', '1:69700', '1:81425', '1:81509', '1:81549', '1:33384', '1:35491', '1:36180', '1:36254', '1:36605', '1:36129', '1:38332', '1:43390', '1:46309', '1:68104', '1:62859', '1:68913', '1:81372', '1:67580', '1:60788', '1:64878', '1:33685', '1:38893', '1:42830', '1:41785', '1:41807', '1:41925', '1:41930', '1:41966', '1:42934', '1:44152', '1:44288', '1:44311', '1:44346', '1:104686', '1:93767', '1:88710', '1:93059', '1:94174', '1:47343', '1:47427', '1:47496', '1:47262', '1:47600', '1:58088', '1:58096', '1:58194', '1:58696', '1:58705', '1:58779', '1:59307', '1:93392', '1:93485', '1:64033', '1:64066', '1:64282', '1:64298', '1:64354', '1:64386', '1:64474', '1:64554', '1:64797', '1:69265', '1:69551', '1:69582', '1:69588', '1:69583', '1:69623', '1:69716', '1:69737', '1:69847', '1:74305', '1:74345', '1:74303', '1:74341', '1:65426', '1:65187', '1:65423', '1:68142', '1:79043', '1:95082', '1:95114', '1:95136', '1:57520', '1:57682', '1:60770', '1:60776', '1:60833', '1:61293', '1:100476', '1:100501', '1:100609', '1:100636', '1:62831', '1:76828', '1:79147', '1:80382', '1:80931', '1:80957', '1:80975', '1:80990', '1:81100', '1:94009', '1:94022', '1:94023', '1:93804', '1:93815', '1:93823', '1:93881', '1:93884', '1:54870', '1:55013', '1:55063', '1:55069', '1:61836', '1:62053', '1:62544', '1:60574', '1:60929', '1:67604', '1:69675', '1:59622', '1:59972', '1:59794', '1:60855', '1:71849', '1:71018', '1:72110', '1:76991', '1:77006', '1:77010', '1:77102', '1:77233', '1:84619', '1:84669', '1:84589', '1:61471', '1:65868', '1:65969', '1:65972', '1:68470', '1:68211', '1:98521', '1:98644', '1:98658', '1:98409', '1:71481', '1:71498', '1:71583', '1:71711', '1:71817', '1:76064', '1:76071', '1:94225', '1:95019', '1:95035', '1:95033', '1:95034', '1:98296', '1:100239', '1:100254', '1:100297', '1:71645', '1:71886', '1:71871', '1:71888', '1:71927', '1:71984', '1:73021', '1:99336', '1:92780', '1:92906', '1:92912', '1:93337', '1:93395', '1:99701', '1:100066', '1:100551', '1:100619', '1:99914', '1:100477', '1:85259', '1:85274', '1:85334', '1:98736', '1:98744', '1:98764', '1:98778', '1:98781', '1:98813', '1:98946', '1:99283', '1:92086', '1:92089', '1:92538', '1:92542', '1:92597', '1:92621', '1:93543', '1:93507', '1:14350', '1:18717', '1:19037', '1:19045', '1:19145', '1:19157', '1:19170', '1:19207', '1:19524', '1:43940', '1:43964', '1:45264', '1:45941', '1:49781', '1:49846', '1:49993', '1:52193', '1:52200', '1:52316', '1:52365', '1:52433', '1:52506', '1:52556', '1:52626', '1:52703', '1:63774', '1:63790', '1:63805', '1:63919', '1:63961', '1:63994', '1:67008', '1:64172', '1:64546', '1:64552', '1:94926', '1:93010', '1:93091', '1:93161', '1:75572', '1:75625', '1:75644', '1:75654', '1:75692', '1:81656', '1:81720', '1:81727', '1:81740', '1:81843', '1:81849', '1:81921', '1:96609', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7E950A55-7FEF-E911-99DC-441EA1616D3A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A8DBB44-A8EE-E911-B7A4-38EAA78D8ADC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8AEFCC7-7EEE-E911-AEFD-0CC47AF97150.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80B375BC-64EF-E911-B7EE-509A4C8395C6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0610918D-54EF-E911-A116-1458D04903A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7A8B894E-5BEF-E911-8B06-3CFDFE7082F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A4B986E-79EF-E911-820B-0025904AC2C4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/065D3837-F2EF-E911-9DD3-44A842B4CC7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/98C92559-C3F2-E911-A525-A4BF0128811C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78F424B9-AEF2-E911-8B73-00E081B705EA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2074DF05-35F2-E911-9B9B-3417EBE706C3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A81CFE31-E1F2-E911-8D5C-A4BF01283D2E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE40E859-04F3-E911-BD9D-A4BF012881D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E609EEE8-57F0-E911-8275-002590DBE20C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE1D09DE-96F2-E911-A3BF-3417EBE74303.root']);