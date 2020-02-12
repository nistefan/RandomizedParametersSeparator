import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:7290', '1:7345', '1:7386', '1:7751', '1:7279', '1:7315', '1:49384', '1:49578', '1:49741', '1:49831', '1:50025', '1:49603', '1:51073', '1:67765', '1:99197', '1:91251', '1:91280', '1:95292', '1:95651', '1:96417', '1:96652', '1:96670', '1:97101', '1:101836', '1:33643', '1:28960', '1:46121', '1:27964', '1:28439', '1:28568', '1:28939', '1:30077', '1:30122', '1:39216', '1:39854', '1:78839', '1:69619', '1:69630', '1:79866', '1:72639', '1:96637', '1:77722', '1:73143', '1:89993', '1:91569', '1:95445', '1:99080', '1:99110', '1:100151', '1:100238', '1:18855', '1:21206', '1:18611', '1:20799', '1:20138', '1:56538', '1:56645', '1:56824', '1:57341', '1:57632', '1:58030', '1:58321', '1:60069', '1:78870', '1:72228', '1:73982', '1:81446', '1:87610', '1:89859', '1:30701', '1:59454', '1:24048', '1:50471', '1:50219', '1:58444', '1:17076', '1:20266', '1:20453', '1:8244', '1:36493', '1:57960', '1:60464', '1:60480', '1:60739', '1:60774', '1:61038', '1:61255', '1:67850', '1:68635', '1:75371', '1:27754', '1:27810', '1:38887', '1:46448', '1:81642', '1:81881', '1:91992', '1:101077', '1:99525', '1:49790', '1:57650', '1:7507', '1:9021', '1:15735', '1:18512', '1:22331', '1:22582', '1:57091', '1:27078', '1:32118', '1:94966', '1:98125', '1:5953', '1:5989', '1:22499', '1:22703', '1:29677', '1:33274', '1:33955', '1:23439', '1:27403', '1:38000', '1:38930', '1:37751', '1:37869', '1:37700', '1:38906', '1:80780', '1:94456', '1:95128', '1:100805', '1:6372', '1:15715', '1:16954', '1:19288', '1:36463', '1:100477', '1:56733', '1:56893', '1:57406', '1:57645', '1:60301', '1:89228', '1:89799', '1:99999', '1:17229', '1:21059', '1:21086', '1:21161', '1:22516', '1:77858', '1:80422', '1:17740', '1:24324', '1:39382', '1:27924', '1:70846', '1:71274', '1:71337', '1:71937', '1:78659', '1:16833', '1:22781', '1:31123', '1:37983', '1:49473', '1:51828', '1:52104', '1:56483', '1:58315', '1:87756', '1:75033', '1:73213', '1:73812', '1:89175', '1:94236', '1:100893', '1:90285', '1:95571', '1:99133', '1:100837', '1:54006', '1:64462', '1:64616', '1:64674', '1:64686', '1:64729', '1:64827', '1:76414', '1:76623', '1:76505', '1:76511', '1:76599', '1:76836', '1:76840', '1:76861', '1:50668', '1:52014', '1:52129', '1:52700', '1:52710', '1:51460', '1:60999', '1:61878', '1:61896', '1:61898', '1:62992', '1:71015', '1:71493', '1:71914', '1:71942', '1:71948', '1:76251', '1:9515', '1:15728', '1:14565', '1:17731', '1:25025', '1:7173', '1:6302', '1:7207', '1:7518', '1:88689', '1:53022', '1:57134', '1:59288', '1:56162', '1:74801', '1:75886', '1:76501', '1:75692', '1:76611', '1:52536', '1:58520', '1:63907', '1:79612', '1:90004', '1:91796', '1:89236', '1:89410', '1:90399', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E0D04434-29FD-E911-8A06-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E2F140C-670A-EA11-AF1D-AC1F6BAC8038.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2C42B47-1A0B-EA11-8F90-0025905B8600.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EA482F8-20FE-E911-B746-0CC47AF9B2B6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92731751-11FE-E911-8809-0CC47AFF02E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/08535ED4-70F7-E911-BD73-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC2DA7CD-1E0B-EA11-804C-AC1F6BAC7F24.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70D87FC9-120B-EA11-946F-0CC47A4C8E26.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AAA24F3-4FFC-E911-AC32-00215A491956.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D24779ED-140B-EA11-B78B-0025905B858A.root']);