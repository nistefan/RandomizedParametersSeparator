import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:92527', '1:92529', '1:92530', '1:93791', '1:93804', '1:93216', '1:93229', '1:93405', '1:93403', '1:93118', '1:93062', '1:93067', '1:93566', '1:93599', '1:93819', '1:12377', '1:12382', '1:12405', '1:11563', '1:11405', '1:11455', '1:42251', '1:42324', '1:44043', '1:41491', '1:12299', '1:12307', '1:12314', '1:11345', '1:11355', '1:12644', '1:41354', '1:42704', '1:42731', '1:82139', '1:82149', '1:42277', '1:42428', '1:42442', '1:42448', '1:44465', '1:47571', '1:82234', '1:82280', '1:82287', '1:83815', '1:83825', '1:83429', '1:83439', '1:11139', '1:11318', '1:11652', '1:42308', '1:42640', '1:44350', '1:47958', '1:65772', '1:65986', '1:42720', '1:41090', '1:47243', '1:44564', '1:42325', '1:41396', '1:41414', '1:42808', '1:41889', '1:41900', '1:47397', '1:11244', '1:11572', '1:42600', '1:65470', '1:48656', '1:43194', '1:48936', '1:65205', '1:43906', '1:43889', '1:66663', '1:45264', '1:65257', '1:65105', '1:66657', '1:11118', '1:11288', '1:12171', '1:41478', '1:48681', '1:44746', '1:42904', '1:42970', '1:41486', '1:41822', '1:48730', '1:45987', '1:45998', '1:48230', '1:48247', '1:65635', '1:65804', '1:65873', '1:44521', '1:43268', '1:43289', '1:43348', '1:66212', '1:66641', '1:83084', '1:65885', '1:11003', '1:12214', '1:12257', '1:12262', '1:42918', '1:41033', '1:41400', '1:41276', '1:47774', '1:45162', '1:44308', '1:12776', '1:12778', '1:41037', '1:41312', '1:42822', '1:41609', '1:45232', '1:45344', '1:45349', '1:45576', '1:45601', '1:45348', '1:45605', '1:84823', '1:84251', '1:45495', '1:45563', '1:45977', '1:83153', '1:83767', '1:82938', '1:83453', '1:82373', '1:93476', '1:93689', '1:84911', '1:84930', '1:92110', '1:66939', '1:83076', '1:83072', '1:83532', '1:83704', '1:82439', '1:82440', '1:82618', '1:82668', '1:66585', '1:66525', '1:66559', '1:83442', '1:83887', '1:83912', '1:92713', '1:92089', '1:84292', '1:84293', '1:84799', '1:12729', '1:12856', '1:12943', '1:12946', '1:41930', '1:45106', '1:92971', '1:93195', '1:93228', '1:93237', '1:93252', '1:48892', '1:65163', '1:65166', '1:65179', '1:65631', '1:65644', '1:65653', '1:65664', '1:65799', '1:92394', '1:92502', '1:92557', '1:92561', '1:92566', '1:92802', '1:92859', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/CCB0C45C-6510-EA11-8402-0025905C53D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/6E48CFB0-B414-EA11-B703-003048F316A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/8493BC83-B911-EA11-968F-485B397717C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D0111189-740F-EA11-A3A6-D094662CEC35.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/2E27578F-4F10-EA11-AEBA-0025905C42A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/7A36FBD8-C811-EA11-9087-7CD30ACE142C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/56A7F3B9-3A10-EA11-A2BE-0025905C42A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C6C92169-6714-EA11-B417-90B11C443C96.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/28CECBEA-7E10-EA11-9B7F-0CC47AFF02D0.root']);