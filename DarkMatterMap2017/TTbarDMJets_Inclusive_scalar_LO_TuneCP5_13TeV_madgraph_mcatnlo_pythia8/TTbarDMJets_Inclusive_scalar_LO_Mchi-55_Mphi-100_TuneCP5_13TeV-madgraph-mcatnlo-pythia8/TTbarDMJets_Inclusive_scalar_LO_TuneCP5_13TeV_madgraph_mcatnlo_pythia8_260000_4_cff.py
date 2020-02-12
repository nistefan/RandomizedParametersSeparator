import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:19372', '1:27368', '1:24965', '1:24903', '1:27145', '1:27261', '1:52035', '1:52342', '1:52689', '1:36561', '1:29529', '1:29656', '1:29687', '1:56574', '1:54200', '1:54202', '1:54208', '1:54224', '1:54297', '1:90431', '1:90646', '1:99816', '1:70203', '1:51534', '1:98251', '1:31200', '1:31589', '1:31407', '1:31515', '1:34080', '1:60509', '1:61024', '1:57289', '1:57534', '1:57574', '1:57715', '1:53029', '1:21102', '1:18923', '1:70408', '1:70462', '1:74087', '1:78806', '1:55875', '1:62098', '1:62116', '1:62222', '1:16014', '1:2861', '1:2980', '1:3248', '1:6197', '1:6291', '1:6373', '1:10949', '1:13464', '1:13764', '1:13997', '1:14613', '1:11840', '1:19481', '1:18862', '1:18902', '1:19772', '1:20277', '1:22051', '1:22086', '1:30939', '1:30897', '1:30983', '1:31031', '1:31455', '1:57616', '1:3057', '1:5985', '1:19990', '1:5465', '1:4613', '1:4622', '1:21666', '1:19076', '1:19354', '1:52867', '1:3443', '1:3530', '1:3563', '1:3956', '1:3671', '1:4307', '1:12442', '1:12556', '1:23655', '1:23913', '1:23989', '1:33463', '1:30467', '1:30502', '1:30548', '1:30615', '1:38423', '1:63755', '1:49077', '1:743', '1:993', '1:784', '1:1074', '1:1055', '1:4891', '1:4766', '1:4799', '1:5085', '1:21642', '1:24210', '1:30230', '1:30265', '1:30297', '1:40701', '1:7967', '1:7972', '1:8154', '1:7968', '1:18554', '1:18644', '1:18852', '1:19071', '1:18697', '1:19359', '1:29255', '1:29263', '1:33005', '1:9595', '1:10111', '1:9543', '1:16098', '1:17104', '1:9987', '1:23330', '1:23354', '1:23482', '1:46159', '1:49020', '1:46381', '1:51678', '1:5062', '1:5128', '1:5224', '1:5253', '1:5385', '1:22623', '1:22776', '1:27163', '1:28166', '1:36360', '1:15148', '1:15162', '1:18191', '1:46204', '1:46164', '1:41140', '1:56646', '1:56731', '1:29646', '1:33716', '1:64117', '1:67125', '1:68140', '1:86643', '1:79251', '1:79492', '1:80439', '1:9552', '1:9577', '1:9550', '1:54489', '1:53908', '1:25170', '1:19810', '1:19812', '1:24160', '1:24387', '1:24426', '1:24977', '1:28824', '1:59369', '1:59806', '1:4603', '1:4650', '1:4641', '1:4986', '1:29699', '1:24835', '1:31577', '1:23598', '1:29476', '1:24391', '1:24408', '1:24526', '1:24636', '1:24668', '1:24886', '1:52885', '1:39710', '1:39715', '1:39798', '1:39308', '1:57525', '1:57481', '1:57563', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/084A337E-FD17-EA11-91CB-FA163EC15C58.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D2D09D4C-FB1C-EA11-B826-AC1F6BAC8038.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3CABE68A-DF17-EA11-A397-EC0D9A89AA0A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1C65D4CB-F817-EA11-A4F0-5065F381E151.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B8C02DCD-DD17-EA11-A4CA-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BCE9B05F-8F19-EA11-A91E-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/34703F54-3C18-EA11-8F76-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8AF4123C-2418-EA11-91CC-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D0D3DE95-0618-EA11-BC35-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/12F05E8A-0618-EA11-9978-24BE05CE3EA1.root']);