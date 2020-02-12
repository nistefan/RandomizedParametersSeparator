import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:683', '1:1420', '1:3616', '1:4525', '1:2500', '1:8038', '1:33911', '1:37145', '1:37605', '1:42411', '1:53465', '1:58411', '1:60166', '1:55473', '1:61568', '1:28918', '1:67286', '1:67675', '1:67840', '1:69161', '1:57738', '1:60512', '1:61146', '1:62336', '1:62354', '1:67651', '1:64884', '1:66604', '1:67993', '1:68540', '1:67581', '1:68171', '1:69959', '1:75331', '1:75428', '1:75460', '1:70736', '1:56262', '1:60709', '1:58453', '1:71599', '1:75415', '1:75551', '1:1725', '1:1781', '1:2741', '1:26012', '1:26015', '1:26083', '1:44081', '1:14266', '1:15303', '1:15386', '1:15342', '1:15480', '1:15523', '1:15572', '1:17278', '1:17286', '1:26352', '1:26880', '1:26576', '1:26525', '1:43855', '1:46462', '1:53554', '1:53716', '1:53771', '1:84609', '1:83929', '1:88406', '1:88265', '1:79711', '1:79928', '1:80066', '1:28533', '1:28596', '1:28624', '1:28567', '1:28568', '1:28574', '1:28761', '1:65076', '1:66701', '1:73741', '1:73259', '1:78580', '1:78989', '1:80960', '1:81014', '1:76963', '1:77446', '1:78821', '1:81303', '1:84485', '1:84527', '1:84603', '1:84629', '1:95475', '1:95795', '1:95841', '1:95857', '1:95874', '1:96157', '1:24656', '1:24816', '1:24825', '1:24826', '1:18918', '1:19683', '1:21156', '1:26143', '1:26217', '1:26284', '1:26299', '1:24098', '1:39479', '1:39629', '1:42078', '1:44942', '1:45660', '1:44839', '1:28921', '1:32097', '1:32486', '1:32272', '1:32368', '1:48136', '1:39187', '1:39219', '1:39287', '1:39294', '1:39297', '1:42697', '1:42713', '1:46087', '1:46094', '1:38099', '1:40136', '1:40144', '1:40168', '1:40210', '1:40212', '1:40337', '1:37063', '1:37151', '1:37193', '1:37006', '1:48359', '1:48392', '1:48432', '1:48932', '1:74848', '1:76489', '1:72126', '1:72228', '1:74943', '1:77328', '1:78022', '1:78066', '1:78073', '1:78232', '1:78312', '1:78555', '1:85071', '1:85202', '1:91172', '1:85258', '1:85283', '1:85359', '1:50411', '1:54419', '1:54104', '1:54285', '1:54314', '1:71662', '1:71804', '1:71906', '1:71904', '1:71971', '1:73264', '1:71823', '1:73751', '1:73799', '1:73902', '1:87008', '1:87334', '1:87337', '1:87901', '1:88386', '1:88478', '1:88530', '1:74471', '1:74579', '1:74584', '1:74757', '1:74850', '1:74876', '1:75024', '1:80634', '1:80672', '1:80724', '1:80746', '1:80796', '1:81068', '1:95173', '1:17979', '1:19506', '1:19621', '1:19735', '1:19756', '1:45501', '1:47702', '1:39367', '1:40251', '1:40399', '1:55085', '1:63550', '1:53269', '1:56044', '1:57948', '1:53765', '1:56166', '1:56254', '1:56699', '1:60868', '1:55784', '1:56247', '1:60214', '1:59585', '1:58764', '1:59541', '1:19566', '1:19316', '1:19398', '1:41180', '1:41435', '1:41570', '1:41578', '1:41622', '1:51320', '1:51453', '1:51633', '1:51772', '1:50128', '1:50146', '1:51651', '1:51710', '1:70808', '1:70936', '1:70958', '1:71049', '1:70822', '1:70829', '1:70879', '1:70884', '1:70996', '1:71046', '1:76809', '1:78178', '1:78190', '1:78314', '1:78328', '1:78367', '1:78374', '1:86200', '1:86205', '1:86440', '1:86306', '1:86325', '1:217', '1:17', '1:67', '1:186', '1:1151', '1:407', '1:4486', '1:1733', '1:2013', '1:2202', '1:4695', '1:4791', '1:955', '1:4716', '1:27019', '1:27040', '1:32632', '1:32909', '1:32997', '1:33100', '1:33131', '1:33138', '1:42475', '1:42938', '1:37812', '1:35308', '1:35315', '1:35254', '1:36169', '1:36191', '1:38811', '1:42190', '1:42626', '1:42677', '1:42691', '1:42002', '1:42177', '1:42502', '1:42736', '1:42760', '1:39809', '1:39851', '1:49266', '1:49388', '1:49321', '1:26367', '1:26680', '1:26693', '1:26785', '1:26928', '1:40916', '1:41063', '1:41257', '1:46201', '1:43620', '1:34182', '1:35778', '1:35894', '1:35946', '1:36033', '1:39723', '1:40231', '1:41299', '1:40082', '1:40266', '1:8647', '1:8695', '1:8922', '1:8936', '1:21274', '1:21302', '1:21311', '1:21601', '1:33766', '1:33838', '1:34004', '1:37979', '1:35674', '1:42519', '1:37120', '1:37258', '1:37266', '1:37826', '1:37832', '1:35371', '1:35484', '1:35346', '1:35347', '1:36709', '1:36770', '1:36813', '1:37381', '1:65857', '1:65938', '1:65978', '1:66643', '1:72217', '1:73206', '1:73277', '1:73331', '1:72237', '1:72251', '1:72257', '1:72352', '1:72501', '1:83997', '1:85439', '1:72271', '1:73283', '1:73336', '1:72439', '1:72645', '1:72650', '1:96579', '1:96820', '1:97316', '1:98054', '1:98092', '1:38255', '1:38738', '1:43079', '1:44260', '1:44770', '1:45401', '1:45460', '1:45776', '1:45900', '1:43301', '1:49431', '1:52006', '1:52014', '1:52890', '1:87497', '1:94767', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4643D148-8CEE-E911-99A7-549F351E4006.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/06C0880D-5BEE-E911-8B86-3417EBE7446B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F6171A5F-F2EF-E911-A256-00E081B705E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9AAAA0F6-25EF-E911-B7E1-A0369FC52524.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/18DA53CD-85EE-E911-A3D0-089E0158CC5B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84D69AFF-25EF-E911-8112-089E0158CDE1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9239CEF9-77EF-E911-B001-0CC47A7E69D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/548A6B80-19EF-E911-A713-506B4BB166B6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40CC65EC-25EF-E911-A3C8-3417EBE70684.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50378F1B-71EE-E911-AD26-38EAA78D8ADC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/88A32370-47EF-E911-8B0C-441EA1615D6A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A7EA364-40EF-E911-B34B-38EAA78D89AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D822EACF-33EF-E911-A627-38EAA78D8FB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CE68873-42F0-E911-99DB-441EA1616D3A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/969DC298-18EF-E911-A24A-38EAA78D8B54.root']);