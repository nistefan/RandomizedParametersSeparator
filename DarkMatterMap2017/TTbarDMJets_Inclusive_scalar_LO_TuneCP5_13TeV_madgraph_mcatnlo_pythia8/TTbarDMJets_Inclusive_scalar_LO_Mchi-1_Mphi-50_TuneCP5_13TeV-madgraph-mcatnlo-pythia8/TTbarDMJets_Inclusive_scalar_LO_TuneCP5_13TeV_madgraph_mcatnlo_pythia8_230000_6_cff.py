import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:50125', '1:50356', '1:51226', '1:51248', '1:51272', '1:51364', '1:51493', '1:51499', '1:51631', '1:51704', '1:51720', '1:50024', '1:51331', '1:53812', '1:53866', '1:56770', '1:57136', '1:1414', '1:2442', '1:8670', '1:9372', '1:13862', '1:14721', '1:18586', '1:6362', '1:8110', '1:8232', '1:10462', '1:16550', '1:17768', '1:17864', '1:17867', '1:96730', '1:98558', '1:100817', '1:100915', '1:58062', '1:71032', '1:70290', '1:72230', '1:72232', '1:72302', '1:73081', '1:73363', '1:90964', '1:95959', '1:97034', '1:98615', '1:99642', '1:79499', '1:95272', '1:95744', '1:97201', '1:97713', '1:97839', '1:98136', '1:98290', '1:101261', '1:95401', '1:96330', '1:97637', '1:99154', '1:99159', '1:99192', '1:99246', '1:99378', '1:99409', '1:99422', '1:99586', '1:99602', '1:99608', '1:99623', '1:99630', '1:99774', '1:99776', '1:99795', '1:99840', '1:99920', '1:100498', '1:100870', '1:76071', '1:62763', '1:76245', '1:76653', '1:76658', '1:78272', '1:62913', '1:62978', '1:63268', '1:63525', '1:63569', '1:63793', '1:63823', '1:64426', '1:55630', '1:61113', '1:62062', '1:64882', '1:67052', '1:77519', '1:77686', '1:79019', '1:79083', '1:79092', '1:79364', '1:79502', '1:79510', '1:79514', '1:79516', '1:79644', '1:77258', '1:77266', '1:77276', '1:77349', '1:77369', '1:77371', '1:77387', '1:77397', '1:77426', '1:77510', '1:77317', '1:77319', '1:77378', '1:77384', '1:77400', '1:77414', '1:77520', '1:77538', '1:77545', '1:77558', '1:77576', '1:77597', '1:81954', '1:98811', '1:98910', '1:98911', '1:98924', '1:99074', '1:99200', '1:99234', '1:99298', '1:99314', '1:99395', '1:99427', '1:99451', '1:99472', '1:99476', '1:99490', '1:99574', '1:99241', '1:99459', '1:99467', '1:99594', '1:99674', '1:99719', '1:3272', '1:3733', '1:4531', '1:10219', '1:18375', '1:20457', '1:20805', '1:1530', '1:6817', '1:14358', '1:16138', '1:18481', '1:20108', '1:20562', '1:21247', '1:17786', '1:10563', '1:15324', '1:16279', '1:16542', '1:17060', '1:17325', '1:18389', '1:19474', '1:18166', '1:26506', '1:26569', '1:29490', '1:36210', '1:38797', '1:62327', '1:94', '1:357', '1:2133', '1:2394', '1:7888', '1:20254', '1:107', '1:2571', '1:2885', '1:3397', '1:3762', '1:4515', '1:5900', '1:14872', '1:22092', '1:26881', '1:31868', '1:32601', '1:37624', '1:31254', '1:35041', '1:40282', '1:46494', '1:51798', '1:59365', '1:59681', '1:59695', '1:75242', '1:37130', '1:37414', '1:37498', '1:37908', '1:39635', '1:46371', '1:46389', '1:73974', '1:70364', '1:71472', '1:77486', '1:64511', '1:73724', '1:77170', '1:71067', '1:101631', '1:96906', '1:102140', '1:102203', '1:102204', '1:102255', '1:102257', '1:102526', '1:3296', '1:3423', '1:3583', '1:3701', '1:3802', '1:3964', '1:22875', '1:22754', '1:22969', '1:22595', '1:22904', '1:22984', '1:28395', '1:28666', '1:39803', '1:69200', '1:68606', '1:68862', '1:22824', '1:22827', '1:22834', '1:22866', '1:22868', '1:22876', '1:22878', '1:22888', '1:22890', '1:22902', '1:22938', '1:22947', '1:22963', '1:61298', '1:61282', '1:61339', '1:61342', '1:61363', '1:61369', '1:61420', '1:61428', '1:61456', '1:61504', '1:61549', '1:63330', '1:70705', '1:71285', '1:74799', '1:74826', '1:74881', '1:74937', '1:76526', '1:77068', '1:72723', '1:13442', '1:13716', '1:13894', '1:13911', '1:16008', '1:16056', '1:16641', '1:14381', '1:18223', '1:18504', '1:20148', '1:20442', '1:20856', '1:20986', '1:22437', '1:17051', '1:22003', '1:87361', '1:87631', '1:90088', '1:94131', '1:94178', '1:98901', '1:99441', '1:99907', '1:90177', '1:94445', '1:95672', '1:95767', '1:96318', '1:96470', '1:96736', '1:100049', '1:100226', '1:100748', '1:73786', '1:73789', '1:77509', '1:78551', '1:80207', '1:80311', '1:72933', '1:73988', '1:77615', '1:78979', '1:78997', '1:78888', '1:19949', '1:18286', '1:18311', '1:18820', '1:18822', '1:54143', '1:54222', '1:54689', '1:55006', '1:55043', '1:55048', '1:55077', '1:55102', '1:55137', '1:54201', '1:54227', '1:54444', '1:56397', '1:56518', '1:55992', '1:57572', '1:58730', '1:61385', '1:62010', '1:62057', '1:62075', '1:62298', '1:62311', '1:56721', '1:57328', '1:57919', '1:58228', '1:58690', '1:58869', '1:56834', '1:58625', '1:61834', '1:68609', '1:74468', '1:74472', '1:74487', '1:74511', '1:74576', '1:75854', '1:75803', '1:75832', '1:75869', '1:75820', '1:52472', '1:52195', '1:52252', '1:52350', '1:52358', '1:52561', '1:52732', '1:52763', '1:52779', '1:52926', '1:52981', '1:52989', '1:53052', '1:53139', '1:53141', '1:53274', '1:53451', '1:53621', '1:53722', '1:53789', '1:56858', '1:59823', '1:52932', '1:57007', '1:57084', '1:57145', '1:57159', '1:57226', '1:57236', '1:57283', '1:53647', '1:53656', '1:53664', '1:53716', '1:53842', '1:53899', '1:53914', '1:53971', '1:56929', '1:54412', '1:54435', '1:54448', '1:54459', '1:54490', '1:54503', '1:54512', '1:54517', '1:54520', '1:54474', '1:54496', '1:54875', '1:54905', '1:69648', '1:63382', '1:63400', '1:63366', '1:63380', '1:64934', '1:64942', '1:64944', '1:67001', '1:68460', '1:68466', '1:68489', '1:68999', '1:69506', '1:69507', '1:69533', '1:69548', '1:69586', '1:69628', '1:75166', '1:76254', '1:76264', '1:76278', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C40F6AE3-3913-EA11-9EE4-20CF305B05CE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D84D1EC9-3913-EA11-8DC0-0CC47A57CBCC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4687DD-3913-EA11-8B59-0CC47AFF23F2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96A24FE4-3913-EA11-AF76-38EAA78D8AF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A620E5CA-3913-EA11-A21F-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7EE607DD-3913-EA11-9A4B-98039B3B01BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50B737E7-3913-EA11-9E68-BC305B390AA7.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FC784550-7BF7-E911-AD10-0CC47A2B0392.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/36D0ACF7-0D0B-EA11-A998-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC089C57-AB01-EA11-8681-509A4C9EF929.root']);