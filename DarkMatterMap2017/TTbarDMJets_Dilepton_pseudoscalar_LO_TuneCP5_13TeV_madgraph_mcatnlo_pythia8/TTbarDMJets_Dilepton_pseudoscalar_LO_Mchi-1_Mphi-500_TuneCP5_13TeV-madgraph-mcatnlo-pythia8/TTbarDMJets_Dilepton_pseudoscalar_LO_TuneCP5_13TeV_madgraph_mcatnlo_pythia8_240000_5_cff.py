import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11481', '1:11538', '1:13751', '1:13801', '1:12587', '1:12021', '1:13365', '1:13477', '1:22355', '1:16636', '1:21424', '1:21941', '1:24008', '1:24228', '1:16158', '1:19035', '1:16530', '1:23711', '1:23724', '1:20765', '1:20072', '1:11855', '1:13224', '1:20458', '1:23631', '1:20891', '1:21090', '1:20697', '1:23212', '1:20425', '1:20443', '1:22268', '1:22962', '1:11070', '1:11131', '1:11172', '1:11260', '1:11443', '1:11529', '1:11142', '1:19047', '1:21957', '1:24224', '1:24748', '1:12667', '1:12902', '1:14672', '1:14677', '1:14689', '1:14769', '1:14773', '1:20212', '1:13584', '1:13742', '1:16008', '1:12438', '1:21839', '1:12118', '1:18051', '1:22535', '1:13111', '1:15703', '1:19407', '1:21319', '1:21337', '1:21360', '1:21393', '1:21482', '1:24023', '1:18220', '1:18230', '1:13025', '1:17266', '1:17420', '1:17530', '1:17558', '1:17623', '1:17682', '1:17884', '1:18449', '1:18430', '1:11055', '1:16841', '1:12209', '1:12204', '1:12321', '1:19245', '1:15999', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/123F7E8E-5D03-EA11-9334-AC1F6B0DE22A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/B8250FA8-83FB-E911-A7D4-008CFA11120C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/B22FB3E2-DFFD-E911-9DFA-002590DE6E5E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C40E7452-5912-EA11-8C49-002590907776.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/80573D6C-5204-EA11-BBF6-AC1F6B1AF05A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/460192A7-5812-EA11-8626-24BE05C6D731.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/EECFE0F0-5812-EA11-8006-506B4BF38278.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/76461747-E310-EA11-916B-38EAA78D8F94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7035F7D2-8F00-EA11-8C3D-D4AE52B21C6F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BE314DAC-0403-EA11-9DD2-0242AC130002.root']);