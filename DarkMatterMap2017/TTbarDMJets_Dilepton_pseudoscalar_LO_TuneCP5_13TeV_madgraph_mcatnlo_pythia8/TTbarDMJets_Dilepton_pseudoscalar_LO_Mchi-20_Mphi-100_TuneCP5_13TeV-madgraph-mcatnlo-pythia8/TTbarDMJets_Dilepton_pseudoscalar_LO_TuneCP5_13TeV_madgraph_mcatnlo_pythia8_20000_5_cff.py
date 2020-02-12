import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:30007', '1:4134', '1:4148', '1:4365', '1:10125', '1:4133', '1:4140', '1:4681', '1:34386', '1:32916', '1:32917', '1:32926', '1:33355', '1:33374', '1:2938', '1:2953', '1:3656', '1:26171', '1:29694', '1:28966', '1:10056', '1:32593', '1:30136', '1:30787', '1:475', '1:511', '1:7622', '1:3030', '1:3048', '1:3210', '1:3219', '1:25529', '1:27533', '1:3916', '1:3932', '1:6387', '1:30701', '1:27537', '1:3864', '1:4385', '1:4768', '1:9666', '1:33066', '1:33965', '1:9338', '1:9751', '1:31675', '1:42', '1:26659', '1:26672', '1:2637', '1:2653', '1:2721', '1:5379', '1:3766', '1:30129', '1:30163', '1:30180', '1:32151', '1:25305', '1:25518', '1:27352', '1:9', '1:8325', '1:7111', '1:29417', '1:1359', '1:29452', '1:31902', '1:32446', '1:28732', '1:32261', '1:9665', '1:10884', '1:8426', '1:144', '1:165', '1:2895', '1:3590', '1:31402', '1:3582', '1:3371', '1:3405', '1:7948', '1:29163', '1:7238', '1:29454', '1:4315', '1:31855', '1:28561', '1:28577', '1:5355', '1:7165', '1:30009', '1:30455', '1:30569', '1:30303', '1:32876', '1:35689', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/14EFC606-9F03-EA11-BEC2-FA163E20CD2B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/82C1E74A-2410-EA11-A821-0CC47AFF24BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/769118EE-1C11-EA11-91F3-0CC47AFF24D6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/50EC5EF4-EC0F-EA11-8370-0025905C9742.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/D0E075EA-80F0-E911-AFE4-FA163E6B2FF6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/EC527D3D-E804-EA11-8C2B-F01FAFE1584B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/908A6B0B-D00C-EA11-8974-FA163EB4F717.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B834EB07-6911-EA11-AEC1-B083FED0FFCF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/4C1F504F-7C0F-EA11-A076-6CC2173D4980.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/E28A9533-7414-EA11-803D-44A8420CC5E0.root']);