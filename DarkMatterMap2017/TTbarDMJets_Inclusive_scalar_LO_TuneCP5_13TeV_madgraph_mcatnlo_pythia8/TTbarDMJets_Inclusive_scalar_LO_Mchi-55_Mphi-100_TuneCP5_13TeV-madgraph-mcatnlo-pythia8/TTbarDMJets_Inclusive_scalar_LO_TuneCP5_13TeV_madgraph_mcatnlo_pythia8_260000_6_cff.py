import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:5559', '1:5695', '1:5774', '1:5908', '1:5975', '1:6850', '1:8031', '1:7300', '1:84993', '1:92438', '1:18021', '1:15488', '1:10655', '1:10672', '1:10694', '1:10496', '1:13063', '1:13080', '1:13343', '1:14025', '1:14051', '1:15641', '1:17918', '1:18963', '1:17048', '1:17185', '1:28672', '1:11888', '1:12072', '1:11881', '1:12074', '1:12091', '1:12202', '1:34834', '1:34961', '1:35201', '1:39095', '1:35249', '1:35416', '1:35669', '1:49708', '1:36442', '1:36445', '1:36476', '1:23005', '1:23359', '1:23368', '1:23415', '1:90200', '1:95247', '1:28457', '1:28579', '1:28548', '1:31116', '1:31147', '1:74196', '1:35252', '1:50291', '1:50354', '1:50477', '1:35220', '1:33246', '1:33514', '1:33646', '1:33583', '1:56157', '1:57194', '1:64757', '1:64878', '1:52698', '1:50573', '1:100988', '1:100996', '1:1277', '1:1347', '1:1469', '1:1523', '1:4290', '1:22465', '1:39175', '1:63604', '1:27255', '1:27669', '1:28720', '1:14285', '1:35992', '1:37190', '1:52792', '1:22433', '1:22497', '1:22836', '1:29286', '1:29738', '1:32231', '1:31731', '1:31755', '1:52562', '1:84403', '1:2412', '1:39979', '1:46134', '1:40102', '1:24020', '1:24161', '1:24165', '1:58378', '1:28920', '1:30021', '1:39279', '1:55246', '1:70588', '1:36665', '1:56618', '1:49116', '1:59121', '1:53543', '1:53643', '1:6196', '1:10885', '1:6452', '1:9006', '1:14405', '1:6172', '1:21404', '1:48266', '1:48271', '1:65153', '1:23090', '1:2813', '1:6861', '1:26600', '1:26735', '1:26446', '1:26819', '1:60607', '1:61105', '1:61199', '1:61737', '1:15136', '1:13475', '1:71276', '1:74322', '1:79436', '1:33311', '1:33497', '1:33550', '1:39722', '1:57358', '1:29564', '1:29688', '1:36067', '1:30360', '1:30455', '1:30558', '1:40594', '1:80943', '1:34804', '1:35627', '1:58614', '1:21433', '1:21482', '1:21685', '1:27289', '1:27391', '1:27626', '1:52543', '1:31997', '1:38575', '1:25392', '1:25646', '1:26159', '1:26253', '1:32327', '1:34267', '1:32275', '1:32307', '1:32615', '1:32755', '1:32777', '1:63001', '1:34896', '1:52957', '1:53353', '1:62445', '1:62456', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A2F9ADEF-4E18-EA11-AF7B-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/F28EB257-6118-EA11-9A40-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/36C76096-3C1A-EA11-A0D5-A0369F7FC4E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B0481AAA-8918-EA11-A0A3-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/50F00FB5-151C-EA11-92A8-0CC47A706CDE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8ADCCDDD-2018-EA11-8340-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2E1D0844-3F1A-EA11-8CBB-FA163EDB1C36.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/40D02E20-7319-EA11-8EAA-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1A4C2C9F-1A18-EA11-A66A-FA163E4874D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D2E6798B-D417-EA11-AAE5-EC0D9A8221D6.root']);