import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:15358', '1:15239', '1:15343', '1:15457', '1:16281', '1:16313', '1:16647', '1:16678', '1:16680', '1:19846', '1:24560', '1:24912', '1:16084', '1:16163', '1:16317', '1:22774', '1:14847', '1:16679', '1:15228', '1:15883', '1:15889', '1:15537', '1:15138', '1:15945', '1:19503', '1:19716', '1:19391', '1:19359', '1:19472', '1:19513', '1:19604', '1:19675', '1:19862', '1:19887', '1:19930', '1:19934', '1:19942', '1:19837', '1:11497', '1:24832', '1:24725', '1:24956', '1:13311', '1:13698', '1:13700', '1:13640', '1:13688', '1:13804', '1:17153', '1:24473', '1:24874', '1:14818', '1:14771', '1:15043', '1:21017', '1:21042', '1:14982', '1:14985', '1:24679', '1:15603', '1:24938', '1:24603', '1:24516', '1:24709', '1:14035', '1:15666', '1:15674', '1:15763', '1:15778', '1:16864', '1:16970', '1:18533', '1:22697', '1:16649', '1:20011', '1:20647', '1:23858', '1:23315', '1:13341', '1:22692', '1:17019', '1:17144', '1:23399', '1:21571', '1:23089', '1:20467', '1:24043', '1:13066', '1:13152', '1:14412', '1:12532', '1:17730', '1:13455', '1:13654', '1:13870', '1:13639', '1:21754', '1:24825', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/E0882A51-5912-EA11-872C-008CFA14FA8C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/9A9349AB-E3F9-E911-978D-8CDCD4A99E60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/388A08FC-5812-EA11-9865-6CC2173BBF00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/185754CB-E6F8-E911-9AEA-0CC47A7E6A74.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/4A488A47-62F8-E911-9547-509A4C9EF93B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BA348E4D-E9FB-E911-88C9-38EAA78D8AD0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C03B7D07-11FB-E911-8BEE-A4BF01288315.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/10891AEF-94FA-E911-9D52-0CC47A7E69D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/4C0A70A8-F5FA-E911-93F3-008CFAC94124.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/F662FCA7-C5FB-E911-A302-38EAA78D8AF4.root']);