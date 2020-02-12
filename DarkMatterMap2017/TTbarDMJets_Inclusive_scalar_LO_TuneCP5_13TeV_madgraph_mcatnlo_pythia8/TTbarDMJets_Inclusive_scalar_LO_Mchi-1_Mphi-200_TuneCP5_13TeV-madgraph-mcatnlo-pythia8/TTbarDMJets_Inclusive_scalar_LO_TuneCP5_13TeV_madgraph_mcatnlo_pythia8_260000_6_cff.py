import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:5543', '1:5599', '1:5665', '1:5960', '1:5974', '1:36737', '1:17930', '1:20888', '1:92430', '1:15396', '1:15448', '1:10554', '1:10552', '1:10928', '1:13531', '1:23065', '1:17223', '1:17336', '1:17491', '1:23377', '1:23575', '1:12088', '1:11949', '1:12181', '1:37614', '1:39257', '1:39282', '1:35105', '1:35516', '1:35620', '1:35656', '1:63017', '1:57885', '1:36439', '1:36458', '1:36486', '1:23303', '1:23362', '1:101920', '1:28480', '1:28528', '1:74079', '1:50128', '1:50152', '1:36770', '1:36891', '1:36993', '1:36212', '1:33517', '1:33535', '1:33543', '1:53740', '1:56354', '1:63951', '1:64134', '1:64797', '1:99988', '1:100192', '1:100970', '1:1646', '1:4193', '1:4253', '1:4213', '1:21842', '1:21821', '1:22923', '1:21978', '1:30982', '1:58522', '1:27287', '1:28790', '1:10589', '1:35714', '1:36632', '1:52751', '1:21962', '1:22285', '1:22787', '1:29298', '1:30807', '1:31741', '1:31748', '1:32039', '1:32065', '1:32167', '1:31776', '1:57260', '1:52697', '1:83141', '1:84061', '1:2152', '1:2271', '1:46979', '1:40111', '1:23245', '1:24213', '1:30980', '1:28907', '1:28887', '1:39299', '1:55173', '1:89966', '1:91521', '1:49134', '1:54015', '1:61429', '1:61769', '1:53900', '1:10583', '1:6590', '1:8070', '1:8238', '1:8869', '1:9664', '1:48200', '1:48219', '1:45213', '1:45610', '1:10035', '1:23034', '1:23212', '1:23367', '1:565', '1:7147', '1:26844', '1:26812', '1:26730', '1:60635', '1:60985', '1:61495', '1:61664', '1:61773', '1:15249', '1:15538', '1:17167', '1:17217', '1:90215', '1:36146', '1:36148', '1:39938', '1:39111', '1:57355', '1:29784', '1:36322', '1:30660', '1:30791', '1:81971', '1:34102', '1:35146', '1:37326', '1:60757', '1:59011', '1:54253', '1:21598', '1:21697', '1:21456', '1:21650', '1:21690', '1:21714', '1:21153', '1:27240', '1:27379', '1:46479', '1:39342', '1:31567', '1:31806', '1:25542', '1:25674', '1:25804', '1:34891', '1:32631', '1:32678', '1:52723', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A2F9ADEF-4E18-EA11-AF7B-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/F28EB257-6118-EA11-9A40-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/36C76096-3C1A-EA11-A0D5-A0369F7FC4E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B0481AAA-8918-EA11-A0A3-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/50F00FB5-151C-EA11-92A8-0CC47A706CDE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8ADCCDDD-2018-EA11-8340-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2E1D0844-3F1A-EA11-8CBB-FA163EDB1C36.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/40D02E20-7319-EA11-8EAA-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1A4C2C9F-1A18-EA11-A66A-FA163E4874D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D2E6798B-D417-EA11-AAE5-EC0D9A8221D6.root']);