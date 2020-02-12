import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:62708', '1:70584', '1:88736', '1:83625', '1:84822', '1:104282', '1:2548', '1:7836', '1:96739', '1:103759', '1:103801', '1:103893', '1:103630', '1:103670', '1:103874', '1:105303', '1:105354', '1:105620', '1:105604', '1:105743', '1:105875', '1:106023', '1:106079', '1:106427', '1:106123', '1:101127', '1:106217', '1:2983', '1:3113', '1:3136', '1:3209', '1:5409', '1:7948', '1:7613', '1:8953', '1:9870', '1:16405', '1:16832', '1:16973', '1:21179', '1:21204', '1:21430', '1:21618', '1:23319', '1:26292', '1:17052', '1:17148', '1:17307', '1:17411', '1:18361', '1:18455', '1:19093', '1:21517', '1:27562', '1:28761', '1:31518', '1:17949', '1:19107', '1:19582', '1:31908', '1:17899', '1:24412', '1:25479', '1:26181', '1:21940', '1:23431', '1:31512', '1:48260', '1:96702', '1:97237', '1:98214', '1:98522', '1:98621', '1:96590', '1:97003', '1:97631', '1:97751', '1:98165', '1:101640', '1:101811', '1:101948', '1:102623', '1:101121', '1:101349', '1:101801', '1:102347', '1:102437', '1:103681', '1:102331', '1:101633', '1:19001', '1:18115', '1:18231', '1:18506', '1:22444', '1:22647', '1:22727', '1:27172', '1:28261', '1:28287', '1:28538', '1:28757', '1:28900', '1:29313', '1:18343', '1:18586', '1:22302', '1:22318', '1:27181', '1:27197', '1:27610', '1:57042', '1:57050', '1:57051', '1:57203', '1:57204', '1:57262', '1:57309', '1:57310', '1:57415', '1:57421', '1:57424', '1:57471', '1:57473', '1:57475', '1:57484', '1:57555', '1:57589', '1:57601', '1:57609', '1:57736', '1:57194', '1:57207', '1:57211', '1:57315', '1:57316', '1:57470', '1:57664', '1:57771', '1:57777', '1:57778', '1:57867', '1:57882', '1:58294', '1:58296', '1:58395', '1:84208', '1:95102', '1:83406', '1:91797', '1:95465', '1:105924', '1:106014', '1:70859', '1:95134', '1:96810', '1:103297', '1:59584', '1:59734', '1:59773', '1:59789', '1:59804', '1:59830', '1:59864', '1:59973', '1:60047', '1:60075', '1:65407', '1:77513', '1:77636', '1:77692', '1:77731', '1:77887', '1:77982', '1:82068', '1:82083', '1:82107', '1:82257', '1:82619', '1:91051', '1:83592', '1:85914', '1:86059', '1:86681', '1:87184', '1:87745', '1:89484', '1:98985', '1:103615', '1:105517', '1:101793', '1:102117', '1:102139', '1:102225', '1:102243', '1:102354', '1:104219', '1:104346', '1:91063', '1:91510', '1:92424', '1:92602', '1:92706', '1:93202', '1:94344', '1:94701', '1:90956', '1:91069', '1:91155', '1:91440', '1:91506', '1:91659', '1:91696', '1:91880', '1:91665', '1:91789', '1:92936', '1:48224', '1:48411', '1:48750', '1:48856', '1:49852', '1:52150', '1:56000', '1:56862', '1:62374', '1:55565', '1:89428', '1:91237', '1:92199', '1:89128', '1:89272', '1:89627', '1:93141', '1:93535', '1:93862', '1:94748', '1:94806', '1:94882', '1:95771', '1:96539', '1:101456', '1:102046', '1:102273', '1:104453', '1:101051', '1:101889', '1:101908', '1:102404', '1:104131', '1:104344', '1:87501', '1:94705', '1:95354', '1:95699', '1:85600', '1:86764', '1:88169', '1:89059', '1:89710', '1:89718', '1:89774', '1:89825', '1:89866', '1:89904', '1:89929', '1:89934', '1:89944', '1:89967', '1:90025', '1:92062', '1:92070', '1:92077', '1:92093', '1:92102', '1:92231', '1:92320', '1:101998', '1:102231', '1:102674', '1:104319', '1:101022', '1:101113', '1:101132', '1:101294', '1:101301', '1:101854', '1:102684', '1:104554', '1:104883', '1:101451', '1:101666', '1:102315', '1:102545', '1:102585', '1:104847', '1:104891', '1:104616', '1:104992', '1:104378', '1:104504', '1:91356', '1:91422', '1:91474', '1:91546', '1:91578', '1:91622', '1:91636', '1:91666', '1:91675', '1:91684', '1:91878', '1:91965', '1:91982', '1:92835', '1:92841', '1:92912', '1:92923', '1:92050', '1:92678', '1:95731', '1:97769', '1:97785', '1:93149', '1:95936', '1:96013', '1:96660', '1:97303', '1:97426', '1:98454', '1:97502', '1:97583', '1:97593', '1:97616', '1:97623', '1:97682', '1:97707', '1:97731', '1:97757', '1:97836', '1:97844', '1:97934', '1:98009', '1:98144', '1:98250', '1:98283', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4227006D-BC12-EA11-89BE-24BE05CEEC21.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4C1DE6F-BC12-EA11-AD6D-C0BFC0E56816.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/74A96878-BC12-EA11-8C73-0CC47AA989BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5ECC5C62-BD12-EA11-BF3F-AC1F6B0DE2EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7851C772-BC12-EA11-BDB4-0025905504C6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2AEF561-BD12-EA11-9091-AC1F6B595F6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B4B1C46E-BD12-EA11-BFF6-BC305B390A80.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CCAB0879-BC12-EA11-BA1C-3CFDFE63F4E0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6C681F0E-990A-EA11-9A16-0025905B85E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1CC07437-950A-EA11-BF7B-0025905B85E8.root']);