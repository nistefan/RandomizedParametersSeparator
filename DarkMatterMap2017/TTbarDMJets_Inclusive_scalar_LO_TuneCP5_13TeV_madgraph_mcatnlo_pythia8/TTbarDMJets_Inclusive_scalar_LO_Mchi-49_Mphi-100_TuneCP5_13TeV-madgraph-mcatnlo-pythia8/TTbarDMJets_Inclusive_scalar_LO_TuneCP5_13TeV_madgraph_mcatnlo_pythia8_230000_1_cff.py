import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:7152', '1:8531', '1:9054', '1:5722', '1:8467', '1:28566', '1:31026', '1:32083', '1:26000', '1:28053', '1:28815', '1:52457', '1:18747', '1:18267', '1:18338', '1:21674', '1:22802', '1:31249', '1:40036', '1:57369', '1:57729', '1:52268', '1:53604', '1:53968', '1:54787', '1:55144', '1:55902', '1:55099', '1:55846', '1:62470', '1:70384', '1:71867', '1:73035', '1:74834', '1:22026', '1:16181', '1:25211', '1:26341', '1:29506', '1:18777', '1:78193', '1:23277', '1:23286', '1:50518', '1:52550', '1:59171', '1:59258', '1:51107', '1:63210', '1:96093', '1:101881', '1:94338', '1:94500', '1:99462', '1:100224', '1:100272', '1:101509', '1:101734', '1:54594', '1:54883', '1:54910', '1:56745', '1:78071', '1:78576', '1:78601', '1:88414', '1:88415', '1:75068', '1:75488', '1:76081', '1:76101', '1:89062', '1:88835', '1:88396', '1:21532', '1:22774', '1:16817', '1:26898', '1:29764', '1:29957', '1:34307', '1:23244', '1:23942', '1:24691', '1:30160', '1:35177', '1:35390', '1:35585', '1:51642', '1:1592', '1:1845', '1:1864', '1:1707', '1:1993', '1:72281', '1:72296', '1:72420', '1:72595', '1:72619', '1:72664', '1:87883', '1:87900', '1:87951', '1:88163', '1:88245', '1:88248', '1:88283', '1:71608', '1:71617', '1:71812', '1:71813', '1:72090', '1:94424', '1:94588', '1:94604', '1:96010', '1:99096', '1:34547', '1:35122', '1:37950', '1:69893', '1:76398', '1:56146', '1:57059', '1:56517', '1:56988', '1:61531', '1:61543', '1:61710', '1:61641', '1:61720', '1:61615', '1:63114', '1:63117', '1:61934', '1:71129', '1:100975', '1:101093', '1:5084', '1:15659', '1:72545', '1:72626', '1:72630', '1:72838', '1:72905', '1:76857', '1:76899', '1:77113', '1:77175', '1:78008', '1:39684', '1:87311', '1:87397', '1:95031', '1:101046', '1:101079', '1:100974', '1:101400', '1:101513', '1:101405', '1:73459', '1:73469', '1:73471', '1:73491', '1:73565', '1:73661', '1:86835', '1:88047', '1:96942', '1:96974', '1:98049', '1:100525', '1:100531', '1:101634', '1:102345', '1:88561', '1:88676', '1:89801', '1:89295', '1:90008', '1:90033', '1:98312', '1:97124', '1:96412', '1:96687', '1:98930', '1:100982', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CF3F789-48F8-E911-9E95-AC1F6B34AC86.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94F3A535-95F8-E911-B0C4-A4BF01025A8B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC6D87E5-FEF8-E911-860A-20040FE9CF40.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E13167A-04F9-E911-822D-AC1F6B0DE296.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02456201-BDFC-E911-8979-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6336465-ACFA-E911-BCEA-0CC47AD98D6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6EDE0848-29FD-E911-8BAF-00215A49197E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/721E3057-28FC-E911-AF04-38EAA78D8960.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E05E587-1AFD-E911-8B60-002590DE6E1E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2236C272-34FD-E911-A005-0CC47A7E6B00.root']);