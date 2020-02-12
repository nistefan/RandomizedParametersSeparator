import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:5524', '1:5571', '1:5678', '1:5692', '1:5759', '1:5830', '1:5944', '1:6999', '1:7745', '1:8340', '1:15456', '1:14988', '1:24084', '1:10546', '1:10571', '1:13047', '1:13484', '1:13816', '1:19999', '1:17202', '1:17474', '1:51243', '1:11947', '1:12080', '1:12033', '1:12189', '1:34925', '1:34587', '1:35092', '1:37589', '1:37954', '1:35151', '1:35370', '1:36426', '1:36548', '1:36407', '1:36539', '1:36529', '1:23013', '1:23241', '1:23106', '1:23410', '1:94285', '1:97294', '1:28351', '1:28658', '1:35326', '1:74049', '1:74170', '1:74181', '1:49356', '1:49832', '1:50331', '1:34979', '1:36180', '1:33496', '1:33522', '1:63970', '1:64349', '1:50078', '1:51086', '1:100899', '1:100369', '1:100952', '1:1191', '1:1306', '1:1392', '1:1465', '1:4106', '1:2064', '1:21871', '1:22008', '1:21839', '1:39105', '1:54332', '1:27750', '1:35531', '1:35562', '1:35645', '1:56864', '1:22302', '1:22321', '1:25545', '1:29243', '1:32465', '1:31775', '1:31814', '1:31927', '1:31952', '1:40076', '1:52637', '1:52956', '1:57073', '1:52574', '1:52841', '1:52887', '1:403', '1:928', '1:1693', '1:46684', '1:24010', '1:24052', '1:24106', '1:30705', '1:30996', '1:28897', '1:30076', '1:29329', '1:86933', '1:36686', '1:36817', '1:56628', '1:54256', '1:61802', '1:53195', '1:56805', '1:7708', '1:8135', '1:8328', '1:13140', '1:20668', '1:48710', '1:9823', '1:9929', '1:23084', '1:23261', '1:23463', '1:6857', '1:5393', '1:26442', '1:26702', '1:26762', '1:61700', '1:60570', '1:61366', '1:13344', '1:15336', '1:36161', '1:30102', '1:30382', '1:39632', '1:31694', '1:32471', '1:33152', '1:33874', '1:36008', '1:36195', '1:30783', '1:30960', '1:30545', '1:30573', '1:30590', '1:30685', '1:30756', '1:30854', '1:81503', '1:34650', '1:35593', '1:58282', '1:61649', '1:21364', '1:46104', '1:27314', '1:40200', '1:31866', '1:31534', '1:32369', '1:25432', '1:25733', '1:26354', '1:25380', '1:25498', '1:31272', '1:32273', '1:32293', '1:50540', '1:54962', '1:58043', '1:59780', '1:60193', '1:60262', '1:63196', '1:52057', '1:52439', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A2F9ADEF-4E18-EA11-AF7B-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/F28EB257-6118-EA11-9A40-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/36C76096-3C1A-EA11-A0D5-A0369F7FC4E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B0481AAA-8918-EA11-A0A3-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/50F00FB5-151C-EA11-92A8-0CC47A706CDE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8ADCCDDD-2018-EA11-8340-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2E1D0844-3F1A-EA11-8CBB-FA163EDB1C36.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/40D02E20-7319-EA11-8EAA-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1A4C2C9F-1A18-EA11-A66A-FA163E4874D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D2E6798B-D417-EA11-AAE5-EC0D9A8221D6.root']);