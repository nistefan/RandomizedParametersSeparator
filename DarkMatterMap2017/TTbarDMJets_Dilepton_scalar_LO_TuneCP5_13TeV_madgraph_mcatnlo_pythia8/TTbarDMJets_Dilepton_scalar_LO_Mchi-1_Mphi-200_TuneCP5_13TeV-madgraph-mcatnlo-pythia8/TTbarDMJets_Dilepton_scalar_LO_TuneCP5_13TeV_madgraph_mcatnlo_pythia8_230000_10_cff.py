import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:72458', '1:75526', '1:75669', '1:72324', '1:72851', '1:97524', '1:97780', '1:97694', '1:42346', '1:42354', '1:42467', '1:39122', '1:39126', '1:39210', '1:39228', '1:39582', '1:41486', '1:51565', '1:51703', '1:50526', '1:50631', '1:50669', '1:50748', '1:86772', '1:86809', '1:86821', '1:87086', '1:87110', '1:86932', '1:87005', '1:26086', '1:26307', '1:28684', '1:28687', '1:78970', '1:84934', '1:100018', '1:100654', '1:100274', '1:100686', '1:4980', '1:15751', '1:17346', '1:17460', '1:14483', '1:16143', '1:16961', '1:14175', '1:14294', '1:14467', '1:15004', '1:15193', '1:15930', '1:16000', '1:16711', '1:15371', '1:17419', '1:17449', '1:17472', '1:15093', '1:15857', '1:17178', '1:44657', '1:59595', '1:60963', '1:62362', '1:21444', '1:21447', '1:36331', '1:38084', '1:38508', '1:42112', '1:42820', '1:55814', '1:98935', '1:98982', '1:99413', '1:103243', '1:27235', '1:27423', '1:28370', '1:32012', '1:38758', '1:33907', '1:34132', '1:34866', '1:35699', '1:35950', '1:36000', '1:36197', '1:37458', '1:37708', '1:37970', '1:38302', '1:57071', '1:57594', '1:68474', '1:68900', '1:69024', '1:64710', '1:66290', '1:69721', '1:63434', '1:60139', '1:61439', '1:69615', '1:99189', '1:99450', '1:102015', '1:18943', '1:20596', '1:26067', '1:56112', '1:57763', '1:56157', '1:56913', '1:58238', '1:17268', '1:24562', '1:27828', '1:27994', '1:32626', '1:34682', '1:36991', '1:79964', '1:82033', '1:84211', '1:83633', '1:45991', '1:46821', '1:54013', '1:70304', '1:70571', '1:72887', '1:49016', '1:72034', '1:72175', '1:72393', '1:87090', '1:87895', '1:88047', '1:100482', '1:65068', '1:70320', '1:86188', '1:84455', '1:92719', '1:95323', '1:97115', '1:3759', '1:3767', '1:3795', '1:3838', '1:50765', '1:50938', '1:51131', '1:51342', '1:51432', '1:60101', '1:59440', '1:60039', '1:62379', '1:76920', '1:105662', '1:86953', '1:87018', '1:87019', '1:87084', '1:87141', '1:87154', '1:87819', '1:87862', '1:100927', '1:100966', '1:100977', '1:100978', '1:100993', '1:102043', '1:39', '1:159', '1:172', '1:300', '1:835', '1:909', '1:4104', '1:4112', '1:4116', '1:2260', '1:2720', '1:1791', '1:1831', '1:1619', '1:1676', '1:1709', '1:1740', '1:1953', '1:1977', '1:18890', '1:18907', '1:18909', '1:18911', '1:18940', '1:18970', '1:18988', '1:20027', '1:51837', '1:51878', '1:52241', '1:52928', '1:14439', '1:14544', '1:14553', '1:14934', '1:14897', '1:56744', '1:91769', '1:91774', '1:103445', '1:103952', '1:103985', '1:2645', '1:2753', '1:5719', '1:5775', '1:5776', '1:5825', '1:5970', '1:17629', '1:17563', '1:17823', '1:44510', '1:44924', '1:57692', '1:55149', '1:62437', '1:69018', '1:70820', '1:63380', '1:91822', '1:91834', '1:91996', '1:94290', '1:92799', '1:95763', '1:95839', '1:95923', '1:96468', '1:96495', '1:95824', '1:64429', '1:64837', '1:64972', '1:64977', '1:64297', '1:64482', '1:78403', '1:78428', '1:78693', '1:78839', '1:78778', '1:81443', '1:88407', '1:88452', '1:81716', '1:81726', '1:81738', '1:81772', '1:81847', '1:81955', '1:95291', '1:98125', '1:99112', '1:98206', '1:98723', '1:8153', '1:8634', '1:12747', '1:12998', '1:16252', '1:17100', '1:18372', '1:14095', '1:19480', '1:21208', '1:24029', '1:24088', '1:27357', '1:24773', '1:21957', '1:21981', '1:24373', '1:24477', '1:24512', '1:24514', '1:24417', '1:27020', '1:27683', '1:45579', '1:46262', '1:47969', '1:39700', '1:45006', '1:48781', '1:49128', '1:44480', '1:49097', '1:88331', '1:88618', '1:88815', '1:94604', '1:83097', '1:83615', '1:85755', '1:87468', '1:16842', '1:16664', '1:18529', '1:9936', '1:9960', '1:9962', '1:15812', '1:18971', '1:17140', '1:18247', '1:19165', '1:27558', '1:33038', '1:426', '1:1131', '1:1197', '1:1301', '1:1394', '1:7236', '1:7238', '1:7264', '1:7313', '1:7345', '1:7512', '1:7547', '1:8210', '1:7909', '1:8216', '1:8044', '1:59479', '1:67279', '1:32622', '1:45004', '1:37308', '1:37333', '1:37445', '1:99498', '1:99562', '1:99685', '1:99766', '1:54003', '1:54181', '1:54477', '1:54499', '1:54684', '1:79467', '1:79472', '1:79474', '1:728', '1:783', '1:882', '1:57', '1:572', '1:953', '1:1067', '1:1823', '1:1164', '1:18097', '1:15850', '1:20055', '1:20431', '1:19505', '1:21067', '1:2400', '1:2207', '1:2386', '1:2632', '1:2744', '1:2329', '1:2026', '1:2401', '1:2919', '1:3685', '1:3903', '1:4143', '1:4969', '1:3782', '1:27830', '1:24080', '1:3420', '1:3962', '1:26670', '1:34926', '1:33885', '1:35129', '1:35532', '1:35755', '1:37756', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E28438A7-4910-EA11-910C-40F2E9C6AE26.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA25B1CE-CEF6-E911-B53C-246E96D14B5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/64F51C16-E1F6-E911-B326-B499BAAC03BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC7BC4C4-EBEF-E911-9B75-002590D9D8B8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2443D33F-8B0E-EA11-B3DB-6CC2173D44D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38867EE3-18EF-E911-ADE7-B8CA3A70A520.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DA35E849-52F8-E911-8ABB-002590D4FC5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A43B4BF7-9B0F-EA11-864B-509A4C84D1B1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5C477F16-6DFF-E911-BE38-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0EF3BEDD-37EE-E911-9652-089E0158CD57.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CECB7F44-C3F2-E911-8EFE-AC162DA6E2F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60FDD590-16F8-E911-89B9-003048F5B69E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CA9067BE-EBED-E911-A5CA-98039B3B0182.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/ACFC8763-7B04-EA11-A589-6CC2173C39E0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DA8DAF0B-9FED-E911-A23B-E0071B6CAD20.root']);