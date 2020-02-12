import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8689', '1:16838', '1:19434', '1:36171', '1:72418', '1:80116', '1:91458', '1:99957', '1:87012', '1:90151', '1:96513', '1:97178', '1:101096', '1:101838', '1:102089', '1:102318', '1:25091', '1:25365', '1:26113', '1:26133', '1:26251', '1:29036', '1:29803', '1:33070', '1:33766', '1:35892', '1:37044', '1:37691', '1:39588', '1:46227', '1:49129', '1:51544', '1:69273', '1:69763', '1:69925', '1:57721', '1:51452', '1:51507', '1:52081', '1:52143', '1:53024', '1:56271', '1:57024', '1:57088', '1:57105', '1:57811', '1:58234', '1:59568', '1:60272', '1:52114', '1:60436', '1:52537', '1:53717', '1:54568', '1:54961', '1:63005', '1:63830', '1:54336', '1:54353', '1:54409', '1:63753', '1:54669', '1:59781', '1:69647', '1:72725', '1:50071', '1:50753', '1:51206', '1:53425', '1:57398', '1:57683', '1:58346', '1:59262', '1:59399', '1:60813', '1:53742', '1:59207', '1:59927', '1:59935', '1:60857', '1:61218', '1:61989', '1:63023', '1:63748', '1:63776', '1:63788', '1:63833', '1:58897', '1:61981', '1:53872', '1:53969', '1:54642', '1:57638', '1:59462', '1:61519', '1:54546', '1:54604', '1:54869', '1:56514', '1:61292', '1:62019', '1:56357', '1:40732', '1:50857', '1:53268', '1:51245', '1:58417', '1:60795', '1:17227', '1:17277', '1:17351', '1:17363', '1:17467', '1:17504', '1:16535', '1:16543', '1:16880', '1:16934', '1:16936', '1:17053', '1:17181', '1:17186', '1:18178', '1:18179', '1:28723', '1:28373', '1:28230', '1:28277', '1:28330', '1:28334', '1:28335', '1:28391', '1:28424', '1:28433', '1:28490', '1:28468', '1:28594', '1:28655', '1:28805', '1:31029', '1:59518', '1:59502', '1:59543', '1:59670', '1:59969', '1:64032', '1:77218', '1:97057', '1:59362', '1:59773', '1:59982', '1:59873', '1:73916', '1:73953', '1:73957', '1:77135', '1:77385', '1:77507', '1:77789', '1:2033', '1:2077', '1:2167', '1:2259', '1:2360', '1:2378', '1:2382', '1:2043', '1:2045', '1:2148', '1:2239', '1:2692', '1:14447', '1:10408', '1:20076', '1:7861', '1:10277', '1:13334', '1:13979', '1:16036', '1:18444', '1:9606', '1:19952', '1:20455', '1:6906', '1:19813', '1:19905', '1:20953', '1:21862', '1:22428', '1:22444', '1:13073', '1:14150', '1:18225', '1:7926', '1:8125', '1:8131', '1:9014', '1:9274', '1:9452', '1:8993', '1:9358', '1:9733', '1:8788', '1:8936', '1:9022', '1:9349', '1:9351', '1:8283', '1:8285', '1:8406', '1:8461', '1:8479', '1:8558', '1:8931', '1:8941', '1:9472', '1:9507', '1:15647', '1:15961', '1:31676', '1:32716', '1:32092', '1:59897', '1:32728', '1:32731', '1:32872', '1:32986', '1:34783', '1:34788', '1:13215', '1:13637', '1:13733', '1:13918', '1:13977', '1:16590', '1:16727', '1:16914', '1:21973', '1:13585', '1:13857', '1:70189', '1:19174', '1:19322', '1:19293', '1:19345', '1:19366', '1:19749', '1:71794', '1:80436', '1:86658', '1:55365', '1:55947', '1:64575', '1:69148', '1:24635', '1:24652', '1:24662', '1:25114', '1:25285', '1:25294', '1:25302', '1:25226', '1:25357', '1:25637', '1:23530', '1:23846', '1:23891', '1:25076', '1:25182', '1:31652', '1:32340', '1:34214', '1:34789', '1:39642', '1:40243', '1:32328', '1:35730', '1:35898', '1:40842', '1:40980', '1:46470', '1:46493', '1:46601', '1:25347', '1:26585', '1:26782', '1:26828', '1:26969', '1:29002', '1:29085', '1:29198', '1:29293', '1:29340', '1:29342', '1:29348', '1:26818', '1:26949', '1:28290', '1:29192', '1:29224', '1:29297', '1:29186', '1:29327', '1:38048', '1:30762', '1:49081', '1:51531', '1:51708', '1:53301', '1:58175', '1:27097', '1:27115', '1:27225', '1:27267', '1:27277', '1:28273', '1:28302', '1:27276', '1:58262', '1:33097', '1:33113', '1:33124', '1:33150', '1:33264', '1:33566', '1:33576', '1:33839', '1:34082', '1:34143', '1:34187', '1:34224', '1:34272', '1:34288', '1:34289', '1:35893', '1:35974', '1:35979', '1:37167', '1:37313', '1:40589', '1:40711', '1:40577', '1:40876', '1:37969', '1:37994', '1:52388', '1:38662', '1:38664', '1:38671', '1:3504', '1:3635', '1:3774', '1:4013', '1:4024', '1:3317', '1:3362', '1:3375', '1:3409', '1:3426', '1:3446', '1:3509', '1:3514', '1:3590', '1:3626', '1:3660', '1:3947', '1:19044', '1:4628', '1:16371', '1:16492', '1:15612', '1:16090', '1:16488', '1:16568', '1:15895', '1:16254', '1:16517', '1:16555', '1:16338', '1:16449', '1:16450', '1:16459', '1:16587', '1:17500', '1:21100', '1:21238', '1:21756', '1:16151', '1:16165', '1:16168', '1:16176', '1:16950', '1:17544', '1:5502', '1:5612', '1:5613', '1:5776', '1:5305', '1:5400', '1:7165', '1:8347', '1:9100', '1:13809', '1:14937', '1:15227', '1:6117', '1:6651', '1:8657', '1:8696', '1:20225', '1:21225', '1:10160', '1:14258', '1:18181', '1:16370', '1:21114', '1:13258', '1:13493', '1:13630', '1:13778', '1:13875', '1:13901', '1:14378', '1:23341', '1:23342', '1:23471', '1:32042', '1:33519', '1:34071', '1:34138', '1:34984', '1:46423', '1:27593', '1:27893', '1:23542', '1:28641', '1:40054', '1:40175', '1:40141', '1:40361', '1:40636', '1:46404', '1:46705', '1:40126', '1:40152', '1:40160', '1:13133', '1:14096', '1:6510', '1:8249', '1:8942', '1:8987', '1:9098', '1:9790', '1:10350', '1:10814', '1:10910', '1:10966', '1:13219', '1:13616', '1:9011', '1:16905', '1:14597', '1:14841', '1:14977', '1:7011', '1:7389', '1:14023', '1:19151', '1:22203', '1:22228', '1:22988', '1:6679', '1:6895', '1:7169', '1:6769', '1:6816', '1:6820', '1:7123', '1:7213', '1:14889', '1:15189', '1:15376', '1:15450', '1:15493', '1:9385', '1:9415', '1:9425', '1:9894', '1:9167', '1:9357', '1:9475', '1:9525', '1:9719', '1:9753', '1:9474', '1:6634', '1:7027', '1:7034', '1:7259', '1:7335', '1:7398', '1:6665', '1:6867', '1:7001', '1:7059', '1:7210', '1:15645', '1:34358', '1:34451', '1:34507', '1:34713', '1:34718', '1:34853', '1:38041', '1:38215', '1:34476', '1:62988', '1:69016', '1:50739', '1:50998', '1:51153', '1:51291', '1:51358', '1:81580', '1:71315', '1:73535', '1:73769', '1:77893', '1:78915', '1:9163', '1:9666', '1:9209', '1:9611', '1:16295', '1:16574', '1:16752', '1:17019', '1:17380', '1:16182', '1:16225', '1:18039', '1:18143', '1:18176', '1:18217', '1:18240', '1:18260', '1:18405', '1:18467', '1:18528', '1:16796', '1:59475', '1:49523', '1:90749', '1:94906', '1:95155', '1:96629', '1:97366', '1:100469', '1:30141', '1:30144', '1:30153', '1:30158', '1:30188', '1:84444', '1:84474', '1:84967', '1:90877', '1:95974', '1:13740', '1:13773', '1:13775', '1:13836', '1:13886', '1:13895', '1:13928', '1:13974', '1:14079', '1:14227', '1:14355', '1:14422', '1:14518', '1:14554', '1:14101', '1:14124', '1:14159', '1:14231', '1:14314', '1:14320', '1:14393', '1:14509', '1:14556', '1:14606', '1:14669', '1:14760', '1:14784', '1:25614', '1:23235', '1:26334', '1:29624', '1:33994', '1:36676', '1:38610', '1:16505', '1:16527', '1:16558', '1:16559', '1:16707', '1:16721', '1:16889', '1:16894', '1:16955', '1:17315', '1:17327', '1:17463', '1:17538', '1:17970', '1:18115', '1:19145', '1:19176', '1:19227', '1:19518', '1:19567', '1:19593', '1:19624', '1:19499', '1:19684', '1:19769', '1:20015', '1:20163', '1:30731', '1:49006', '1:39808', '1:52027', '1:53554', '1:57185', '1:57720', '1:57736', '1:61578', '1:24838', '1:24884', '1:53071', '1:53223', '1:53236', '1:53238', '1:53286', '1:53303', '1:53362', '1:53148', '1:53170', '1:53188', '1:53356', '1:53412', '1:53690', '1:56012', '1:56038', '1:56127', '1:56175', '1:64502', '1:74094', '1:79205', '1:80118', '1:81651', '1:81745', '1:86270', '1:75012', '1:76230', '1:56712', '1:56717', '1:56812', '1:57120', '1:56676', '1:57167', '1:57171', '1:58053', '1:58152', '1:57749', '1:57755', '1:24570', '1:25033', '1:25058', '1:29939', '1:29767', '1:29786', '1:29859', '1:29887', '1:29953', '1:33007', '1:33058', '1:36101', '1:40198', '1:61310', '1:61439', '1:61387', '1:61408', '1:61590', '1:61595', '1:61848', '1:61945', '1:4196', '1:1968', '1:1972', '1:1989', '1:2000', '1:2177', '1:2455', '1:2059', '1:2180', '1:2190', '1:2200', '1:2308', '1:2320', '1:19052', '1:19109', '1:19527', '1:19072', '1:21336', '1:21467', '1:20778', '1:21091', '1:21205', '1:20738', '1:21051', '1:21298', '1:21310', '1:21490', '1:21547', '1:21561', '1:36541', '1:29703', '1:29726', '1:29741', '1:32346', '1:32356', '1:33317', '1:29874', '1:29882', '1:34333', '1:35343', '1:34828', '1:36211', '1:29689', '1:33073', '1:33245', '1:29971', '1:29990', '1:36424', '1:36448', '1:36542', '1:36589', '1:36590', '1:36598', '1:36740', '1:36765', '1:36768', '1:36801', '1:36813', '1:36820', '1:36754', '1:38433', '1:38466', '1:54756', '1:61810', '1:55770', '1:55798', '1:63408', '1:50863', '1:50879', '1:52307', '1:51634', '1:51784', '1:51745', '1:51805', '1:51970', '1:52032', '1:52076', '1:52154', '1:76981', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8A52D68A-9716-EA11-8A46-C81F66C09A78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3AA8A739-3B1A-EA11-8F16-0025901D08F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6C8ECEC3-DC18-EA11-A954-246E96D149A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DAB73933-B217-EA11-85E7-24BE05C3CBE1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E2A83DB0-0518-EA11-9905-FA163ECADB68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/46514FD2-CA17-EA11-A746-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/5CECA162-FA17-EA11-9B4F-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/18E400F5-FF17-EA11-A992-FA163E9F39BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DEE6096F-1D18-EA11-99A4-FA163E977168.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/404013D1-151C-EA11-A760-588A5AAEEBB8.root']);