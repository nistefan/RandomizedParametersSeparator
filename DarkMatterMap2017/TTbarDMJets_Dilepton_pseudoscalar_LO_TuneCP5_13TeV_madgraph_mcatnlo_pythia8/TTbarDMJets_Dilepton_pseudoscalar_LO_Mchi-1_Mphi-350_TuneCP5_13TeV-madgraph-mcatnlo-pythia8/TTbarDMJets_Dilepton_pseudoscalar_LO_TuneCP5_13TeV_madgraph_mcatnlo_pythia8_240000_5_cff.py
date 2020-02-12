import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11947', '1:13135', '1:13985', '1:21562', '1:16045', '1:23546', '1:23836', '1:16642', '1:20654', '1:20781', '1:23114', '1:22485', '1:22607', '1:22515', '1:22518', '1:11118', '1:11474', '1:11014', '1:11148', '1:21716', '1:24184', '1:24783', '1:24260', '1:24754', '1:12833', '1:12897', '1:14703', '1:14761', '1:20006', '1:20806', '1:13109', '1:24886', '1:13229', '1:13452', '1:23116', '1:19799', '1:19293', '1:19446', '1:21303', '1:21377', '1:21490', '1:21707', '1:12967', '1:17042', '1:17674', '1:13715', '1:17602', '1:18469', '1:18512', '1:21742', '1:11138', '1:13520', '1:18324', '1:12293', '1:22619', '1:17793', '1:22631', '1:17568', '1:19134', '1:19029', '1:19401', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/123F7E8E-5D03-EA11-9334-AC1F6B0DE22A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/B8250FA8-83FB-E911-A7D4-008CFA11120C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/B22FB3E2-DFFD-E911-9DFA-002590DE6E5E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C40E7452-5912-EA11-8C49-002590907776.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/80573D6C-5204-EA11-BBF6-AC1F6B1AF05A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/460192A7-5812-EA11-8626-24BE05C6D731.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/EECFE0F0-5812-EA11-8006-506B4BF38278.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/76461747-E310-EA11-916B-38EAA78D8F94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7035F7D2-8F00-EA11-8C3D-D4AE52B21C6F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BE314DAC-0403-EA11-9DD2-0242AC130002.root']);