import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:6614', '1:7038', '1:8281', '1:9688', '1:9819', '1:4826', '1:31578', '1:28359', '1:31183', '1:33990', '1:58890', '1:60659', '1:51795', '1:52370', '1:13117', '1:18574', '1:19859', '1:14469', '1:14945', '1:18705', '1:9427', '1:15440', '1:15512', '1:18583', '1:19409', '1:19704', '1:20056', '1:20484', '1:21382', '1:22799', '1:22883', '1:37471', '1:38453', '1:35050', '1:35414', '1:40241', '1:40637', '1:52568', '1:56688', '1:53683', '1:56868', '1:55590', '1:64911', '1:55108', '1:62356', '1:70459', '1:72009', '1:72181', '1:6608', '1:25220', '1:29385', '1:9596', '1:14126', '1:14458', '1:14759', '1:18137', '1:18849', '1:20153', '1:20249', '1:20948', '1:69247', '1:52460', '1:57883', '1:39676', '1:49369', '1:52269', '1:67537', '1:76200', '1:76647', '1:99545', '1:101768', '1:54926', '1:56608', '1:78382', '1:78518', '1:78646', '1:78678', '1:88508', '1:88635', '1:89150', '1:74822', '1:74868', '1:75649', '1:76026', '1:88524', '1:88301', '1:88338', '1:88514', '1:88527', '1:102097', '1:17246', '1:20128', '1:27565', '1:51931', '1:60228', '1:53077', '1:53128', '1:1551', '1:1557', '1:1849', '1:1856', '1:1875', '1:77297', '1:72176', '1:72640', '1:88186', '1:88634', '1:71153', '1:71513', '1:71556', '1:71603', '1:71634', '1:71726', '1:71838', '1:71861', '1:71958', '1:94512', '1:94795', '1:95064', '1:95116', '1:98696', '1:98706', '1:98713', '1:98865', '1:98899', '1:98966', '1:98994', '1:99215', '1:34548', '1:35437', '1:37778', '1:40996', '1:69800', '1:69869', '1:69862', '1:69939', '1:76244', '1:76263', '1:76421', '1:76446', '1:56891', '1:56507', '1:57083', '1:57643', '1:57740', '1:61243', '1:61300', '1:61470', '1:61636', '1:61388', '1:63192', '1:61623', '1:61639', '1:63096', '1:63130', '1:63134', '1:101069', '1:13090', '1:16141', '1:72553', '1:72934', '1:72945', '1:72959', '1:76907', '1:77137', '1:30012', '1:49344', '1:49444', '1:51399', '1:51060', '1:80405', '1:94936', '1:95040', '1:95108', '1:100941', '1:100966', '1:100204', '1:100322', '1:100332', '1:100340', '1:73631', '1:88034', '1:88362', '1:88539', '1:88054', '1:96762', '1:97092', '1:97384', '1:100321', '1:100451', '1:100570', '1:101656', '1:101672', '1:101749', '1:88786', '1:89643', '1:89698', '1:95994', '1:96705', '1:96869', '1:97213', '1:96860', '1:100554', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CF3F789-48F8-E911-9E95-AC1F6B34AC86.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94F3A535-95F8-E911-B0C4-A4BF01025A8B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC6D87E5-FEF8-E911-860A-20040FE9CF40.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E13167A-04F9-E911-822D-AC1F6B0DE296.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02456201-BDFC-E911-8979-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6336465-ACFA-E911-BCEA-0CC47AD98D6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6EDE0848-29FD-E911-8BAF-00215A49197E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/721E3057-28FC-E911-AF04-38EAA78D8960.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E05E587-1AFD-E911-8B60-002590DE6E1E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2236C272-34FD-E911-A005-0CC47A7E6B00.root']);