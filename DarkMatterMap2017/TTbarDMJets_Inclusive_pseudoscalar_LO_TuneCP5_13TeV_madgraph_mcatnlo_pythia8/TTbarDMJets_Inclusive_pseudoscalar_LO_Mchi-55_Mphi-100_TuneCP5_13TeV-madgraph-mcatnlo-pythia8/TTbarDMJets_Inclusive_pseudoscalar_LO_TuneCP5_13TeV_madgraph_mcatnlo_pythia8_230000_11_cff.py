import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1455', '1:1416', '1:1591', '1:4024', '1:31041', '1:31415', '1:3247', '1:3821', '1:3645', '1:4296', '1:4972', '1:5389', '1:5105', '1:23322', '1:17760', '1:26578', '1:29921', '1:32776', '1:41424', '1:49697', '1:40649', '1:40884', '1:49953', '1:52126', '1:48017', '1:42805', '1:62157', '1:42282', '1:42298', '1:42306', '1:42314', '1:42460', '1:42613', '1:62352', '1:73814', '1:80607', '1:64135', '1:95098', '1:2828', '1:7006', '1:4485', '1:13241', '1:13466', '1:21965', '1:23479', '1:39608', '1:42142', '1:43138', '1:88932', '1:89200', '1:1899', '1:12289', '1:12746', '1:12804', '1:6353', '1:6816', '1:7816', '1:8816', '1:10591', '1:8412', '1:104517', '1:95458', '1:98708', '1:98774', '1:86616', '1:102365', '1:102615', '1:101701', '1:102770', '1:1109', '1:1386', '1:1826', '1:1439', '1:26695', '1:26956', '1:31046', '1:31068', '1:28828', '1:28862', '1:29000', '1:29328', '1:29465', '1:28919', '1:5869', '1:88268', '1:93143', '1:102107', '1:101387', '1:66360', '1:75611', '1:83973', '1:90785', '1:92256', '1:84871', '1:84930', '1:105756', '1:15560', '1:24773', '1:44545', '1:7870', '1:12669', '1:9731', '1:1713', '1:20044', '1:20221', '1:20291', '1:17003', '1:17287', '1:17438', '1:17840', '1:17887', '1:75654', '1:45238', '1:45925', '1:45935', '1:47493', '1:58839', '1:59328', '1:101937', '1:102021', '1:66897', '1:67992', '1:89669', '1:90170', '1:90227', '1:91026', '1:91148', '1:91780', '1:103579', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0C06959B-34F2-E911-A007-40F2E9C6B000.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AADDDD37-EBF9-E911-B35C-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/282CD5F6-EEFA-E911-9E5C-98039B3B004E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E037B27-56F3-E911-8A41-38EAA78D8AF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A04310E4-3E07-EA11-8B88-0CC47AFF02E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/483332F2-DA07-EA11-AEAC-44A842CF0598.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AEC23971-74F7-E911-9030-44A842CFC98B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2F49560-5CF8-E911-A273-0CC47AD9914C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CFEC9C5-B0FB-E911-8390-28924A33AFC2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/228E8BD5-26F5-E911-B71D-509A4C9F8ADB.root']);