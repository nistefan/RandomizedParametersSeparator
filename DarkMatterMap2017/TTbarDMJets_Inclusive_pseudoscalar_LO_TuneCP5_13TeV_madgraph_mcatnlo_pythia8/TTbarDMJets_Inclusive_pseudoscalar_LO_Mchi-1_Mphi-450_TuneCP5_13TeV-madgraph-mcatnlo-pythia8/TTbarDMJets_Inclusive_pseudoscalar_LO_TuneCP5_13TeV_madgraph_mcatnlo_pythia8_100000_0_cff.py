import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:26840', '1:26998', '1:28700', '1:30828', '1:69237', '1:76119', '1:83084', '1:82179', '1:82309', '1:86022', '1:86800', '1:91650', '1:94768', '1:95092', '1:104593', '1:98450', '1:97149', '1:11698', '1:11708', '1:11925', '1:11954', '1:12552', '1:45258', '1:53052', '1:53890', '1:70041', '1:20991', '1:21541', '1:66442', '1:66624', '1:67177', '1:75111', '1:85222', '1:86393', '1:83430', '1:22051', '1:22222', '1:22336', '1:22500', '1:26892', '1:31363', '1:38486', '1:40331', '1:40342', '1:97140', '1:34595', '1:34691', '1:37612', '1:37449', '1:37690', '1:38452', '1:38859', '1:73082', '1:74234', '1:74428', '1:74744', '1:95449', '1:96980', '1:97315', '1:11909', '1:30323', '1:32829', '1:30821', '1:32071', '1:42822', '1:102253', '1:91717', '1:103708', '1:10229', '1:10380', '1:10537', '1:11863', '1:54449', '1:54728', '1:54851', '1:82629', '1:83105', '1:14574', '1:17750', '1:17883', '1:17977', '1:19137', '1:85622', '1:23918', '1:23975', '1:54744', '1:55147', '1:55407', '1:55470', '1:56007', '1:63596', '1:63813', '1:69096', '1:69629', '1:29935', '1:32177', '1:32400', '1:39579', '1:16239', '1:87201', '1:87235', '1:95784', '1:5387', '1:5538', '1:6449', '1:13136', '1:12326', '1:12949', '1:13660', '1:35775', '1:50275', '1:50961', '1:50969', '1:54029', '1:54428', '1:60354', '1:104530', '1:18031', '1:18381', '1:18517', '1:75705', '1:86208', '1:85543', '1:86880', '1:87459', '1:79771', '1:83373', '1:94307', '1:94438', '1:95314', '1:15479', '1:16032', '1:16787', '1:4293', '1:19056', '1:17025', '1:91378', '1:95298', '1:98050', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/54925349-9519-EA11-8883-A0369FC5D904.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/E0951404-C619-EA11-B099-008CFA56D794.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/28EB89BA-D919-EA11-84D5-AC1F6B1AEFFC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/123DAC5E-E119-EA11-AA7C-0CC47A2B04A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/8AF33801-A818-EA11-ADA3-3417EBE700A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/04330BE3-4D19-EA11-B1D0-FA163EA7FFF8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/FEA9539C-0D19-EA11-88D3-FA163E800347.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/361BF4AC-E81A-EA11-92A9-001E675825D4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/628B0069-E81A-EA11-8EAC-AC1F6B5676BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/50B0175D-E81A-EA11-B967-90B11C443C1A.root']);