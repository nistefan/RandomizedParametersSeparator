import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:13125', '1:18625', '1:13474', '1:13613', '1:13449', '1:17454', '1:13491', '1:13929', '1:12016', '1:12344', '1:22359', '1:18500', '1:12104', '1:22981', '1:12584', '1:22555', '1:22775', '1:13908', '1:21623', '1:15342', '1:19695', '1:18594', '1:18942', '1:16245', '1:16392', '1:14235', '1:20924', '1:21607', '1:21721', '1:13647', '1:14067', '1:16986', '1:16192', '1:19266', '1:15590', '1:11227', '1:11393', '1:11390', '1:11285', '1:11351', '1:14939', '1:14968', '1:21200', '1:24645', '1:24733', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/D268B341-2703-EA11-8548-0CC47A4D760C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/2A3A1901-D010-EA11-80A1-B083FED04276.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/2016D407-5912-EA11-9D15-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/0C8C135D-BC03-EA11-A032-0026B9277A3F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/4ED4C44C-25FC-E911-ADC7-509A4C9EF93B.root']);