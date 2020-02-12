import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:25044', '1:30003', '1:4769', '1:4919', '1:4924', '1:7376', '1:7382', '1:4330', '1:4333', '1:4641', '1:34406', '1:30570', '1:30621', '1:30912', '1:33361', '1:33385', '1:33450', '1:26179', '1:26243', '1:26981', '1:9339', '1:30882', '1:32678', '1:32157', '1:484', '1:604', '1:605', '1:7708', '1:7711', '1:9370', '1:9387', '1:29229', '1:29089', '1:3045', '1:3973', '1:4126', '1:4127', '1:5188', '1:7101', '1:6388', '1:31993', '1:31967', '1:5148', '1:8725', '1:4682', '1:29757', '1:29780', '1:9834', '1:31734', '1:939', '1:5806', '1:26684', '1:5174', '1:33051', '1:25134', '1:25272', '1:27402', '1:8282', '1:10607', '1:49', '1:8260', '1:3944', '1:30483', '1:30484', '1:31878', '1:28387', '1:29232', '1:10744', '1:9044', '1:9562', '1:10961', '1:9555', '1:4267', '1:6311', '1:3580', '1:10928', '1:26057', '1:26695', '1:2915', '1:2900', '1:2922', '1:3372', '1:29392', '1:31022', '1:29544', '1:28327', '1:28595', '1:28386', '1:5783', '1:5969', '1:9789', '1:9301', '1:30502', '1:30511', '1:30867', '1:30332', '1:35831', '1:35913', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/14EFC606-9F03-EA11-BEC2-FA163E20CD2B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/82C1E74A-2410-EA11-A821-0CC47AFF24BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/769118EE-1C11-EA11-91F3-0CC47AFF24D6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/50EC5EF4-EC0F-EA11-8370-0025905C9742.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/D0E075EA-80F0-E911-AFE4-FA163E6B2FF6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/EC527D3D-E804-EA11-8C2B-F01FAFE1584B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/908A6B0B-D00C-EA11-8974-FA163EB4F717.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B834EB07-6911-EA11-AEC1-B083FED0FFCF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/4C1F504F-7C0F-EA11-A076-6CC2173D4980.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/E28A9533-7414-EA11-803D-44A8420CC5E0.root']);