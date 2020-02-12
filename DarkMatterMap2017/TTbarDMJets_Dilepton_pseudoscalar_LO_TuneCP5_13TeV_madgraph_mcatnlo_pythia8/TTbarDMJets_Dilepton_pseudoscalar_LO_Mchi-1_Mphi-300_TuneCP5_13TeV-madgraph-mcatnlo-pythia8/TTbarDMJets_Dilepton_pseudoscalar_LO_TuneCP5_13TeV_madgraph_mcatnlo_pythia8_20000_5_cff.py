import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:30043', '1:30077', '1:25750', '1:30015', '1:30019', '1:4156', '1:7685', '1:10944', '1:10945', '1:10950', '1:26737', '1:26152', '1:26214', '1:10661', '1:10802', '1:33721', '1:8805', '1:9411', '1:9417', '1:30147', '1:30881', '1:31499', '1:467', '1:470', '1:3089', '1:6000', '1:7628', '1:7644', '1:29091', '1:4192', '1:27551', '1:5186', '1:5205', '1:25553', '1:25575', '1:5011', '1:5028', '1:5035', '1:5147', '1:4741', '1:4744', '1:4746', '1:4971', '1:5836', '1:31291', '1:33875', '1:1240', '1:1301', '1:26754', '1:2675', '1:5770', '1:3770', '1:25043', '1:30144', '1:30186', '1:30263', '1:25257', '1:27323', '1:27362', '1:16', '1:8763', '1:8716', '1:29443', '1:982', '1:5919', '1:29407', '1:26184', '1:2105', '1:29463', '1:31658', '1:33777', '1:31896', '1:6223', '1:6314', '1:10763', '1:6523', '1:10846', '1:2081', '1:3126', '1:3530', '1:4399', '1:6796', '1:7513', '1:6720', '1:32523', '1:1498', '1:2916', '1:5768', '1:8261', '1:4310', '1:29178', '1:28010', '1:7769', '1:9293', '1:30191', '1:27540', '1:30504', '1:30869', '1:30429', '1:30427', '1:32892', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/14EFC606-9F03-EA11-BEC2-FA163E20CD2B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/82C1E74A-2410-EA11-A821-0CC47AFF24BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/769118EE-1C11-EA11-91F3-0CC47AFF24D6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/50EC5EF4-EC0F-EA11-8370-0025905C9742.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/D0E075EA-80F0-E911-AFE4-FA163E6B2FF6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/EC527D3D-E804-EA11-8C2B-F01FAFE1584B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/908A6B0B-D00C-EA11-8974-FA163EB4F717.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B834EB07-6911-EA11-AEC1-B083FED0FFCF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/4C1F504F-7C0F-EA11-A076-6CC2173D4980.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/E28A9533-7414-EA11-803D-44A8420CC5E0.root']);