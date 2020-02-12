import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11453', '1:13385', '1:20194', '1:12502', '1:22561', '1:21646', '1:15485', '1:16031', '1:16168', '1:23356', '1:11980', '1:20255', '1:23020', '1:23678', '1:20612', '1:16779', '1:20451', '1:20664', '1:22763', '1:22328', '1:22641', '1:22941', '1:11191', '1:11166', '1:15535', '1:24869', '1:24868', '1:12849', '1:12857', '1:12995', '1:14702', '1:14788', '1:14810', '1:17002', '1:22017', '1:22037', '1:22386', '1:22710', '1:21974', '1:11096', '1:12918', '1:22955', '1:11250', '1:23396', '1:19349', '1:19300', '1:21362', '1:21425', '1:21583', '1:21846', '1:12880', '1:12884', '1:12969', '1:18255', '1:22909', '1:17582', '1:18447', '1:18468', '1:13208', '1:12898', '1:12923', '1:18117', '1:18285', '1:18295', '1:22293', '1:16738', '1:19095', '1:19624', '1:19807', '1:22450', '1:12152', '1:17306', '1:17982', '1:22592', '1:19017', '1:19119', '1:19128', '1:19255', '1:15994', '1:16754', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/123F7E8E-5D03-EA11-9334-AC1F6B0DE22A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/B8250FA8-83FB-E911-A7D4-008CFA11120C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/B22FB3E2-DFFD-E911-9DFA-002590DE6E5E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C40E7452-5912-EA11-8C49-002590907776.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/80573D6C-5204-EA11-BBF6-AC1F6B1AF05A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/460192A7-5812-EA11-8626-24BE05C6D731.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/EECFE0F0-5812-EA11-8006-506B4BF38278.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/76461747-E310-EA11-916B-38EAA78D8F94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7035F7D2-8F00-EA11-8C3D-D4AE52B21C6F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BE314DAC-0403-EA11-9DD2-0242AC130002.root']);