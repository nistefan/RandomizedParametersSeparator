import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:22464', '1:22480', '1:9882', '1:16096', '1:16284', '1:16343', '1:22317', '1:36759', '1:36766', '1:23559', '1:26344', '1:26413', '1:29861', '1:36039', '1:36536', '1:38860', '1:16403', '1:15635', '1:17346', '1:18297', '1:100669', '1:100700', '1:17908', '1:18020', '1:2273', '1:2328', '1:15186', '1:15626', '1:15150', '1:15427', '1:20355', '1:20320', '1:20625', '1:20642', '1:20719', '1:20890', '1:20938', '1:24412', '1:24441', '1:60637', '1:27190', '1:27651', '1:24822', '1:24858', '1:27553', '1:27912', '1:25714', '1:68981', '1:72190', '1:85866', '1:69472', '1:69867', '1:69873', '1:69996', '1:70207', '1:94677', '1:98298', '1:100209', '1:96966', '1:1466', '1:1511', '1:1932', '1:1954', '1:2122', '1:18656', '1:19067', '1:19558', '1:43379', '1:44000', '1:48336', '1:58', '1:120', '1:231', '1:300', '1:139', '1:9946', '1:2138', '1:2369', '1:6200', '1:804', '1:39127', '1:39246', '1:1066', '1:1085', '1:1192', '1:1275', '1:1339', '1:1337', '1:2081', '1:1668', '1:1471', '1:1600', '1:1641', '1:1677', '1:19239', '1:21396', '1:21768', '1:19645', '1:19700', '1:19702', '1:25199', '1:25330', '1:25350', '1:706', '1:744', '1:861', '1:789', '1:1071', '1:33904', '1:36798', '1:36940', '1:33852', '1:36107', '1:34078', '1:76337', '1:77458', '1:55126', '1:55479', '1:62782', '1:63056', '1:64594', '1:67851', '1:62109', '1:64665', '1:68405', '1:59055', '1:59099', '1:59871', '1:71864', '1:74694', '1:79405', '1:85142', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A2426674-3F1A-EA11-A7AE-EC0D9A82220E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8A8568B7-421A-EA11-804A-F01FAFE159DB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/CAF40DBB-151C-EA11-BE60-FA163E5CA4D1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/76305311-EA1E-EA11-AD5D-6CC2173BC990.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/0CE1922F-401A-EA11-ACBB-7CD30ABD2EE8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/F858F107-E417-EA11-87D2-FA163EA27966.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/22065D99-FF18-EA11-86AD-FA163E456613.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/64E80312-1C18-EA11-B3CE-00259048A860.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/28F0E26E-3F1A-EA11-976A-A0369FF88396.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1CAD6881-0218-EA11-B9CC-FA163EE6A76E.root']);