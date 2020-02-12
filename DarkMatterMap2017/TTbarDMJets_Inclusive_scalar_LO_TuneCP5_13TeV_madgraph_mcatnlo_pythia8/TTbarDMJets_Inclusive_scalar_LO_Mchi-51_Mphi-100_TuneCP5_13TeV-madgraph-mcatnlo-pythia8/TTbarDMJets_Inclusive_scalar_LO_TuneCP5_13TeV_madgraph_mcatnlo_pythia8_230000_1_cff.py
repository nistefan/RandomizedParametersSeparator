import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:13192', '1:332', '1:28637', '1:32612', '1:57858', '1:53421', '1:57950', '1:58024', '1:59041', '1:18627', '1:20783', '1:19911', '1:20325', '1:21560', '1:28693', '1:35906', '1:37150', '1:57550', '1:58610', '1:53378', '1:39468', '1:55127', '1:64601', '1:17812', '1:17846', '1:22237', '1:29557', '1:14004', '1:15326', '1:19522', '1:20274', '1:20371', '1:20655', '1:21948', '1:20983', '1:69868', '1:23625', '1:52329', '1:60692', '1:49905', '1:51581', '1:56609', '1:59028', '1:74433', '1:87274', '1:89025', '1:100972', '1:90942', '1:97986', '1:100053', '1:100166', '1:54413', '1:54601', '1:54842', '1:54930', '1:54940', '1:54998', '1:57126', '1:57238', '1:78449', '1:78760', '1:88043', '1:88147', '1:88333', '1:88442', '1:88617', '1:89124', '1:74852', '1:75125', '1:75683', '1:88011', '1:89007', '1:89055', '1:89141', '1:89192', '1:88538', '1:101605', '1:101738', '1:102135', '1:102375', '1:21914', '1:29916', '1:36538', '1:30902', '1:31848', '1:24593', '1:51481', '1:57396', '1:53326', '1:53342', '1:53923', '1:53998', '1:56952', '1:51693', '1:57330', '1:53130', '1:53244', '1:53658', '1:1568', '1:1799', '1:1824', '1:1874', '1:2013', '1:77265', '1:72375', '1:72745', '1:87902', '1:87935', '1:87937', '1:88464', '1:71034', '1:71273', '1:71448', '1:71452', '1:71569', '1:71735', '1:71810', '1:94554', '1:94578', '1:94953', '1:95011', '1:95601', '1:96012', '1:96060', '1:98750', '1:34386', '1:35089', '1:35200', '1:35315', '1:35557', '1:35640', '1:37835', '1:40007', '1:69378', '1:69856', '1:69790', '1:69960', '1:75456', '1:75517', '1:76262', '1:76388', '1:76404', '1:76436', '1:76440', '1:76450', '1:76931', '1:76948', '1:101401', '1:57230', '1:57472', '1:58260', '1:61374', '1:61759', '1:61239', '1:61795', '1:61803', '1:61950', '1:101060', '1:24', '1:4763', '1:7472', '1:10341', '1:16418', '1:20873', '1:72786', '1:72922', '1:72973', '1:72988', '1:73041', '1:76656', '1:76958', '1:76961', '1:77288', '1:50749', '1:49870', '1:30706', '1:50433', '1:51308', '1:87245', '1:94941', '1:101074', '1:101082', '1:101386', '1:73580', '1:73709', '1:88151', '1:87812', '1:96367', '1:96432', '1:96478', '1:96619', '1:96918', '1:97157', '1:98825', '1:100455', '1:100580', '1:101761', '1:101793', '1:89829', '1:89862', '1:95978', '1:96099', '1:95990', '1:96349', '1:96608', '1:97270', '1:101892', '1:100138', '1:101908', '1:100401', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CF3F789-48F8-E911-9E95-AC1F6B34AC86.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94F3A535-95F8-E911-B0C4-A4BF01025A8B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC6D87E5-FEF8-E911-860A-20040FE9CF40.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E13167A-04F9-E911-822D-AC1F6B0DE296.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02456201-BDFC-E911-8979-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6336465-ACFA-E911-BCEA-0CC47AD98D6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6EDE0848-29FD-E911-8BAF-00215A49197E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/721E3057-28FC-E911-AF04-38EAA78D8960.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E05E587-1AFD-E911-8B60-002590DE6E1E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2236C272-34FD-E911-A005-0CC47A7E6B00.root']);