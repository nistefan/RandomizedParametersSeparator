import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11054', '1:13062', '1:12527', '1:13053', '1:13419', '1:13537', '1:13538', '1:22363', '1:21696', '1:21806', '1:21912', '1:24245', '1:24638', '1:24840', '1:14949', '1:16063', '1:19583', '1:16408', '1:16450', '1:16579', '1:20274', '1:20910', '1:11893', '1:11965', '1:20407', '1:20411', '1:20524', '1:21253', '1:16516', '1:16682', '1:23194', '1:23218', '1:23363', '1:23349', '1:23357', '1:22959', '1:11075', '1:11140', '1:15007', '1:19288', '1:24225', '1:24773', '1:24890', '1:24745', '1:24993', '1:12591', '1:12830', '1:22963', '1:14687', '1:14727', '1:14750', '1:17171', '1:18539', '1:21878', '1:17523', '1:22626', '1:17732', '1:13186', '1:23605', '1:23750', '1:19463', '1:19496', '1:21458', '1:24112', '1:24323', '1:18370', '1:17139', '1:17145', '1:17148', '1:17607', '1:17679', '1:22068', '1:17821', '1:17940', '1:18457', '1:18473', '1:21744', '1:11161', '1:13372', '1:12939', '1:12981', '1:19018', '1:22930', '1:12433', '1:12257', '1:17478', '1:22131', '1:22366', '1:19207', '1:19271', '1:19051', '1:19062', '1:19278', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/123F7E8E-5D03-EA11-9334-AC1F6B0DE22A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/B8250FA8-83FB-E911-A7D4-008CFA11120C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/B22FB3E2-DFFD-E911-9DFA-002590DE6E5E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C40E7452-5912-EA11-8C49-002590907776.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/80573D6C-5204-EA11-BBF6-AC1F6B1AF05A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/460192A7-5812-EA11-8626-24BE05C6D731.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/EECFE0F0-5812-EA11-8006-506B4BF38278.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/76461747-E310-EA11-916B-38EAA78D8F94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7035F7D2-8F00-EA11-8C3D-D4AE52B21C6F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BE314DAC-0403-EA11-9DD2-0242AC130002.root']);