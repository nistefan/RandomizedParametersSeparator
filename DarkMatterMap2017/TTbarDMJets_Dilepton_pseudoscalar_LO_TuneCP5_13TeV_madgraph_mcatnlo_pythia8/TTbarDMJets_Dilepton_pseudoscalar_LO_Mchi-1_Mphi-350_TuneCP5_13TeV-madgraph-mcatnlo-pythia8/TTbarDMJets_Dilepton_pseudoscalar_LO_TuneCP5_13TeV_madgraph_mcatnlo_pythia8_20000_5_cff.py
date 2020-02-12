import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:25699', '1:25754', '1:25923', '1:2688', '1:4331', '1:4683', '1:4771', '1:4900', '1:10917', '1:4640', '1:4658', '1:4671', '1:4676', '1:32260', '1:26715', '1:4183', '1:26261', '1:9419', '1:9434', '1:30667', '1:31199', '1:593', '1:7817', '1:29207', '1:29084', '1:29094', '1:3223', '1:3975', '1:25363', '1:27556', '1:34689', '1:31989', '1:3323', '1:5001', '1:5129', '1:5248', '1:4634', '1:4711', '1:4937', '1:8047', '1:5834', '1:31284', '1:33075', '1:26553', '1:9784', '1:9832', '1:9833', '1:31553', '1:33186', '1:926', '1:1237', '1:1292', '1:2640', '1:2666', '1:33052', '1:25809', '1:25431', '1:27304', '1:27305', '1:34880', '1:8651', '1:948', '1:1719', '1:74', '1:4880', '1:26023', '1:25601', '1:31913', '1:29245', '1:4317', '1:9571', '1:9575', '1:2157', '1:2914', '1:6312', '1:7226', '1:6634', '1:6799', '1:30486', '1:2898', '1:5200', '1:3948', '1:7214', '1:28029', '1:28091', '1:28517', '1:9117', '1:9291', '1:28848', '1:32965', '1:35030', '1:35809', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/14EFC606-9F03-EA11-BEC2-FA163E20CD2B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/82C1E74A-2410-EA11-A821-0CC47AFF24BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/769118EE-1C11-EA11-91F3-0CC47AFF24D6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/50EC5EF4-EC0F-EA11-8370-0025905C9742.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/D0E075EA-80F0-E911-AFE4-FA163E6B2FF6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/EC527D3D-E804-EA11-8C2B-F01FAFE1584B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/908A6B0B-D00C-EA11-8974-FA163EB4F717.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B834EB07-6911-EA11-AEC1-B083FED0FFCF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/4C1F504F-7C0F-EA11-A076-6CC2173D4980.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/E28A9533-7414-EA11-803D-44A8420CC5E0.root']);