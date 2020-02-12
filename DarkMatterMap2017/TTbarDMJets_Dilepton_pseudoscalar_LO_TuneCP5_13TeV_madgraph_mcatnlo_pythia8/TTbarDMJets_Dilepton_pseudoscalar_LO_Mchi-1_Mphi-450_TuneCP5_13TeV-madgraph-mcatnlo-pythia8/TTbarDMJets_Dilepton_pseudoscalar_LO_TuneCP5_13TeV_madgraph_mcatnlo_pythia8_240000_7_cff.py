import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11813', '1:11814', '1:13059', '1:13219', '1:13782', '1:17524', '1:22444', '1:22348', '1:18036', '1:18505', '1:18238', '1:18304', '1:17930', '1:17495', '1:22902', '1:12606', '1:17447', '1:12470', '1:12462', '1:17463', '1:15469', '1:15605', '1:23094', '1:23775', '1:21624', '1:13139', '1:20482', '1:23280', '1:16740', '1:16744', '1:14088', '1:16800', '1:16993', '1:15924', '1:11238', '1:11376', '1:11377', '1:14924', '1:21012', '1:21044', '1:24690', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/D268B341-2703-EA11-8548-0CC47A4D760C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/2A3A1901-D010-EA11-80A1-B083FED04276.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/2016D407-5912-EA11-9D15-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/0C8C135D-BC03-EA11-A032-0026B9277A3F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/4ED4C44C-25FC-E911-ADC7-509A4C9EF93B.root']);