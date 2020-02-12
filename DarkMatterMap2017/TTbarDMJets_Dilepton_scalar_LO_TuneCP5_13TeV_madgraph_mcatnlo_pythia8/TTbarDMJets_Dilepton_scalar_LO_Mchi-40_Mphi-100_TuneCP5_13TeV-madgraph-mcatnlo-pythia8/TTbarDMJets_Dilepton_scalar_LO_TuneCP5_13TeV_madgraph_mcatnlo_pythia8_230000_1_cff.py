import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:55642', '1:56402', '1:59147', '1:59156', '1:56357', '1:56412', '1:56459', '1:56487', '1:83514', '1:83530', '1:83540', '1:83606', '1:85548', '1:85599', '1:86687', '1:86797', '1:66138', '1:66376', '1:66430', '1:66313', '1:71061', '1:71110', '1:71372', '1:71217', '1:83457', '1:83996', '1:84732', '1:84257', '1:84277', '1:65563', '1:65569', '1:65657', '1:65679', '1:65773', '1:65815', '1:66000', '1:70149', '1:85471', '1:86453', '1:86631', '1:86722', '1:83349', '1:83624', '1:85382', '1:79962', '1:79986', '1:80953', '1:84024', '1:5074', '1:4271', '1:5018', '1:5123', '1:5200', '1:24914', '1:24958', '1:24969', '1:26026', '1:26091', '1:26158', '1:26160', '1:26279', '1:38471', '1:38566', '1:8561', '1:14122', '1:14220', '1:12341', '1:14080', '1:14269', '1:24070', '1:36410', '1:36505', '1:36539', '1:36645', '1:36669', '1:36740', '1:44196', '1:44303', '1:34815', '1:38053', '1:38088', '1:38243', '1:38198', '1:43309', '1:43319', '1:43351', '1:43367', '1:41455', '1:42624', '1:42885', '1:42892', '1:42994', '1:5653', '1:5609', '1:5762', '1:19793', '1:19831', '1:19926', '1:19937', '1:19860', '1:19861', '1:19881', '1:21022', '1:21090', '1:21255', '1:26819', '1:26969', '1:26977', '1:26999', '1:27166', '1:50301', '1:17716', '1:17869', '1:18313', '1:26915', '1:27613', '1:28053', '1:28055', '1:28358', '1:37526', '1:37587', '1:37706', '1:37551', '1:37555', '1:37640', '1:20275', '1:27262', '1:27856', '1:27863', '1:27702', '1:27749', '1:27520', '1:28050', '1:40288', '1:40753', '1:49194', '1:49339', '1:50741', '1:51255', '1:39616', '1:49847', '1:59998', '1:59940', '1:60381', '1:83574', '1:83644', '1:83688', '1:83698', '1:83723', '1:83726', '1:83730', '1:87464', '1:87478', '1:87390', '1:87407', '1:97509', '1:97428', '1:97463', '1:97588', '1:97750', '1:97753', '1:97980', '1:2560', '1:5367', '1:2339', '1:5561', '1:5575', '1:70464', '1:71648', '1:74151', '1:67703', '1:72889', '1:75089', '1:75421', '1:75592', '1:12592', '1:12637', '1:20457', '1:18297', '1:19281', '1:20241', '1:20495', '1:67152', '1:67423', '1:67554', '1:86774', '1:104695', '1:15987', '1:24567', '1:28920', '1:32071', '1:32084', '1:34020', '1:34769', '1:51997', '1:53174', '1:39514', '1:52804', '1:51322', '1:68300', '1:81624', '1:35952', '1:36454', '1:37693', '1:38518', '1:38721', '1:38885', '1:42260', '1:42722', '1:42730', '1:42771', '1:43071', '1:68870', '1:65626', '1:66446', '1:71640', '1:74010', '1:63277', '1:81387', '1:67666', '1:68204', '1:68437', '1:98146', '1:99555', '1:102902', '1:38828', '1:42315', '1:41820', '1:41821', '1:44331', '1:44501', '1:83504', '1:88590', '1:88833', '1:94799', '1:91311', '1:91777', '1:91837', '1:96291', '1:47568', '1:47753', '1:69642', '1:58173', '1:58190', '1:58210', '1:58318', '1:58631', '1:58819', '1:58845', '1:59105', '1:98313', '1:93466', '1:93488', '1:94742', '1:64135', '1:64273', '1:64372', '1:64676', '1:64814', '1:64822', '1:65034', '1:65041', '1:69460', '1:74334', '1:74287', '1:80001', '1:65273', '1:65328', '1:65439', '1:65469', '1:65069', '1:65070', '1:65189', '1:65408', '1:65572', '1:67583', '1:68233', '1:68261', '1:79971', '1:79988', '1:82022', '1:79149', '1:57541', '1:57560', '1:57660', '1:57396', '1:57407', '1:57419', '1:57534', '1:57593', '1:60899', '1:61245', '1:61277', '1:61392', '1:100348', '1:100644', '1:62461', '1:62601', '1:62670', '1:77117', '1:80265', '1:80623', '1:80802', '1:80917', '1:82093', '1:94003', '1:93802', '1:93808', '1:93824', '1:93851', '1:93882', '1:55005', '1:55194', '1:55271', '1:55809', '1:59773', '1:63342', '1:67715', '1:60307', '1:69683', '1:59544', '1:59657', '1:59576', '1:60830', '1:60871', '1:72367', '1:70977', '1:71611', '1:72118', '1:72156', '1:76716', '1:76986', '1:77211', '1:80416', '1:84401', '1:84427', '1:84765', '1:84775', '1:84448', '1:60639', '1:60745', '1:60780', '1:60879', '1:61090', '1:68056', '1:68730', '1:69173', '1:71570', '1:71573', '1:71619', '1:71738', '1:71752', '1:77414', '1:77447', '1:77864', '1:95022', '1:98668', '1:98749', '1:98783', '1:98805', '1:99830', '1:100243', '1:100288', '1:100308', '1:100330', '1:71894', '1:98331', '1:92852', '1:92925', '1:92983', '1:93245', '1:93255', '1:93360', '1:93427', '1:99951', '1:100357', '1:85260', '1:85262', '1:85273', '1:98874', '1:98945', '1:98953', '1:99229', '1:92066', '1:92110', '1:92592', '1:92666', '1:93128', '1:93583', '1:18457', '1:19017', '1:19021', '1:19051', '1:19105', '1:19160', '1:19210', '1:43842', '1:43866', '1:43869', '1:43963', '1:45280', '1:45381', '1:49755', '1:50051', '1:50104', '1:52471', '1:52544', '1:52739', '1:63886', '1:63898', '1:67011', '1:67021', '1:67162', '1:64084', '1:64091', '1:64537', '1:92988', '1:93363', '1:75262', '1:75583', '1:75542', '1:75668', '1:81806', '1:81809', '1:96595', '1:96620', '1:96622', '1:96672', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7E950A55-7FEF-E911-99DC-441EA1616D3A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A8DBB44-A8EE-E911-B7A4-38EAA78D8ADC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8AEFCC7-7EEE-E911-AEFD-0CC47AF97150.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80B375BC-64EF-E911-B7EE-509A4C8395C6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0610918D-54EF-E911-A116-1458D04903A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7A8B894E-5BEF-E911-8B06-3CFDFE7082F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A4B986E-79EF-E911-820B-0025904AC2C4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/065D3837-F2EF-E911-9DD3-44A842B4CC7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/98C92559-C3F2-E911-A525-A4BF0128811C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78F424B9-AEF2-E911-8B73-00E081B705EA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2074DF05-35F2-E911-9B9B-3417EBE706C3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A81CFE31-E1F2-E911-8D5C-A4BF01283D2E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE40E859-04F3-E911-BD9D-A4BF012881D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E609EEE8-57F0-E911-8275-002590DBE20C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE1D09DE-96F2-E911-A3BF-3417EBE74303.root']);