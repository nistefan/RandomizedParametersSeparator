import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:131', '1:310', '1:352', '1:384', '1:385', '1:390', '1:392', '1:22', '1:93', '1:110', '1:239', '1:242', '1:344', '1:389', '1:4', '1:903', '1:35094', '1:126', '1:135', '1:578', '1:37692', '1:34590', '1:34636', '1:34637', '1:36270', '1:36564', '1:36690', '1:36478', '1:36525', '1:100704', '1:100928', '1:100715', '1:100820', '1:100835', '1:100838', '1:100852', '1:35609', '1:35651', '1:327', '1:35401', '1:35529', '1:35593', '1:35613', '1:35551', '1:35717', '1:35539', '1:35564', '1:35571', '1:100409', '1:100821', '1:33656', '1:33354', '1:33363', '1:33381', '1:33412', '1:33415', '1:33427', '1:33446', '1:33463', '1:33466', '1:33486', '1:33497', '1:33541', '1:33557', '1:69893', '1:33512', '1:33518', '1:33525', '1:33482', '1:33508', '1:33522', '1:33536', '1:33565', '1:33572', '1:33585', '1:33705', '1:33729', '1:36227', '1:68106', '1:68126', '1:68264', '1:68363', '1:68371', '1:68393', '1:68183', '1:68346', '1:68384', '1:34095', '1:34132', '1:34308', '1:34315', '1:35446', '1:35521', '1:37613', '1:37621', '1:37936', '1:38917', '1:36856', '1:34733', '1:34734', '1:34740', '1:34787', '1:34795', '1:34796', '1:34797', '1:34802', '1:34808', '1:34942', '1:34951', '1:34954', '1:36157', '1:36158', '1:36230', '1:36241', '1:36263', '1:36266', '1:36268', '1:36370', '1:38918', '1:38967', '1:38983', '1:68242', '1:68405', '1:68415', '1:68418', '1:38945', '1:38964', '1:38973', '1:68428', '1:68433', '1:38996', '1:50559', '1:50545', '1:50570', '1:50589', '1:50598', '1:50602', '1:50642', '1:50659', '1:50670', '1:50680', '1:50683', '1:50749', '1:50787', '1:50789', '1:50854', '1:50945', '1:50948', '1:26', '1:35894', '1:36458', '1:68001', '1:68277', '1:50051', '1:50798', '1:63113', '1:38145', '1:38149', '1:35961', '1:34289', '1:34949', '1:36866', '1:38744', '1:38307', '1:38318', '1:38319', '1:38320', '1:38327', '1:38403', '1:38413', '1:33622', '1:33649', '1:33652', '1:33653', '1:33739', '1:33637', '1:33738', '1:33763', '1:33819', '1:33804', '1:34168', '1:34414', '1:34427', '1:34431', '1:34439', '1:34448', '1:34451', '1:34460', '1:34454', '1:34743', '1:34763', '1:34764', '1:34770', '1:37956', '1:37963', '1:37978', '1:37981', '1:37984', '1:37987', '1:37998', '1:37159', '1:37278', '1:37482', '1:37638', '1:37020', '1:63655', '1:63657', '1:63670', '1:63671', '1:63958', '1:63988', '1:69128', '1:69133', '1:69138', '1:69165', '1:69177', '1:69190', '1:69132', '1:69506', '1:99326', '1:99327', '1:99180', '1:99261', '1:99281', '1:99294', '1:99309', '1:99344', '1:99345', '1:99359', '1:99367', '1:99370', '1:99373', '1:99376', '1:99396', '1:99414', '1:99470', '1:99340', '1:99395', '1:69921', '1:99346', '1:99347', '1:99420', '1:99383', '1:99484', '1:99500', '1:99508', '1:99525', '1:99300', '1:99318', '1:99400', '1:99440', '1:99441', '1:99288', '1:99689', '1:100069', '1:100241', '1:100329', '1:100353', '1:100373', '1:100386', '1:100415', '1:100425', '1:100438', '1:100439', '1:100448', '1:99862', '1:99902', '1:100074', '1:100294', '1:100328', '1:100368', '1:100374', '1:99456', '1:76', '1:214', '1:764', '1:799', '1:807', '1:35876', '1:37081', '1:37197', '1:37230', '1:33941', '1:37721', '1:99760', '1:995', '1:34826', '1:36469', '1:37519', '1:37527', '1:37531', '1:37628', '1:63764', '1:63864', '1:99225', '1:99085', '1:99207', '1:69950', '1:69954', '1:99589', '1:99782', '1:69980', '1:99775', '1:99799', '1:99955', '1:100490', '1:50808', '1:50907', '1:63157', '1:63368', '1:34202', '1:34225', '1:34535', '1:34931', '1:36397', '1:36449', '1:36450', '1:36456', '1:34929', '1:36413', '1:36434', '1:36468', '1:38055', '1:50066', '1:50067', '1:34229', '1:38077', '1:68287', '1:68299', '1:50047', '1:50077', '1:63620', '1:63647', '1:63650', '1:63874', '1:63934', '1:69022', '1:69031', '1:69034', '1:69042', '1:69050', '1:69760', '1:69788', '1:69781', '1:69783', '1:63954', '1:63956', '1:69334', '1:69785', '1:69979', '1:99740', '1:100587', '1:63999', '1:69985', '1:99199', '1:99542', '1:99547', '1:99567', '1:99571', '1:99769', '1:99808', '1:100734', '1:100983', '1:62', '1:754', '1:976', '1:35131', '1:37379', '1:37515', '1:37632', '1:34919', '1:34939', '1:36438', '1:36569', '1:36751', '1:38673', '1:33056', '1:33081', '1:33089', '1:33095', '1:33098', '1:33103', '1:33104', '1:33118', '1:33130', '1:33137', '1:33086', '1:33099', '1:33101', '1:33314', '1:33319', '1:33321', '1:33325', '1:33368', '1:33435', '1:33436', '1:69039', '1:69773', '1:99778', '1:100036', '1:36548', '1:36683', '1:36702', '1:36730', '1:36752', '1:36754', '1:36766', '1:36794', '1:36847', '1:36859', '1:36899', '1:36944', '1:36892', '1:36903', '1:50112', '1:50221', '1:50222', '1:50301', '1:50389', '1:50452', '1:50497', '1:50517', '1:50518', '1:50520', '1:50530', '1:50532', '1:50566', '1:50613', '1:50657', '1:50742', '1:50226', '1:50232', '1:50377', '1:50397', '1:50390', '1:50174', '1:50298', '1:50420', '1:99253', '1:99068', '1:69732', '1:100063', '1:99811', '1:100586', '1:34824', '1:34918', '1:34996', '1:38067', '1:38084', '1:35728', '1:38051', '1:68308', '1:68309', '1:99971', '1:50579', '1:50678', '1:50681', '1:50790', '1:50843', '1:50866', '1:50871', '1:50688', '1:63383', '1:63419', '1:63569', '1:50979', '1:63388', '1:50892', '1:99530', '1:99492', '1:99493', '1:99905', '1:99943', '1:99949', '1:99860', '1:99871', '1:99875', '1:99880', '1:99969', '1:99973', '1:99419', '1:99428', '1:99438', '1:99685', '1:99921', '1:99923', '1:118', '1:253', '1:82', '1:91', '1:92', '1:104', '1:115', '1:123', '1:400', '1:18', '1:292', '1:435', '1:470', '1:34222', '1:38033', '1:38036', '1:38039', '1:38047', '1:38054', '1:38662', '1:63353', '1:99773', '1:100047', '1:100594', '1:100578', '1:34034', '1:100493', '1:100713', '1:100897', '1:100900', '1:100913', '1:100891', '1:100929', '1:100932', '1:100722', '1:33006', '1:33008', '1:37853', '1:33983', '1:34469', '1:34473', '1:34971', '1:37089', '1:37092', '1:37382', '1:34983', '1:36612', '1:37345', '1:37559', '1:37566', '1:37829', '1:37876', '1:37879', '1:34648', '1:34660', '1:34677', '1:34838', '1:34843', '1:36538', '1:34842', '1:36249', '1:36252', '1:36971', '1:38169', '1:38287', '1:38275', '1:38280', '1:33682', '1:34484', '1:36642', '1:34863', '1:36633', '1:36656', '1:100546', '1:34661', '1:34647', '1:36287', '1:38177', '1:38520', '1:38572', '1:34858', '1:100207', '1:100224', '1:100690', '1:100933', '1:100934', '1:36604', '1:50037', '1:50041', '1:38734', '1:38774', '1:68048', '1:68116', '1:68128', '1:68143', '1:68513', '1:68636', '1:68652', '1:68654', '1:68703', '1:63189', '1:63192', '1:63199', '1:63208', '1:69713', '1:50648', '1:63478', '1:63479', '1:63315', '1:63592', '1:63600', '1:63716', '1:63817', '1:63977', '1:69084', '1:69613', '1:69097', '1:69620', '1:35192', '1:35258', '1:35515', '1:35839', '1:35856', '1:33880', '1:38183', '1:38253', '1:100635', '1:33001', '1:34379', '1:37234', '1:37353', '1:37878', '1:34185', '1:34338', '1:34372', '1:36083', '1:37258', '1:37329', '1:35250', '1:35762', '1:35842', '1:69110', '1:69632', '1:69668', '1:69639', '1:69717', '1:69719', '1:69933', '1:99928', '1:99845', '1:33002', '1:33889', '1:33915', '1:34336', '1:63559', '1:63516', '1:34827', '1:36631', '1:37861', '1:33912', '1:33990', '1:35140', '1:35851', '1:35855', '1:37113', '1:34699', '1:35859', '1:36653', '1:36670', '1:37554', '1:34701', '1:37126', '1:63617', '1:63747', '1:50244', '1:63493', '1:63534', '1:63305', '1:63505', '1:63788', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/ACA45E67-4710-EA11-993D-AC1F6B1AF142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/EE07DEB0-7311-EA11-88E2-7CD30ACE1479.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DEA7093A-5810-EA11-9AB2-0CC47AFF0454.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/62D36710-EC10-EA11-A1B6-98039B3B003A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/46F6364E-2311-EA11-A748-0CC47A1DF800.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/8CF037CB-4710-EA11-80A5-0CC47A5FC281.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/88FDBA27-9A11-EA11-B345-A0369FC524AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/B0B5A181-2812-EA11-B322-B083FED1321B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/B6F2C869-7914-EA11-8091-F01FAFD69D00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/62A1C426-9D14-EA11-86E0-1418774A24C6.root']);