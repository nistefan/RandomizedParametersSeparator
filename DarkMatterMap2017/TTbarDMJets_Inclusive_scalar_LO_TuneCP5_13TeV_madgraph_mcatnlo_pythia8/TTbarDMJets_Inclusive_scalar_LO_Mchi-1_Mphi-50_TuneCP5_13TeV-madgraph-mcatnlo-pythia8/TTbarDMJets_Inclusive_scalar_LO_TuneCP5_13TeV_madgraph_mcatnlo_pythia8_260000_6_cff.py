import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:5529', '1:5558', '1:5572', '1:5591', '1:5595', '1:5638', '1:5777', '1:5812', '1:5819', '1:5837', '1:5838', '1:5976', '1:5978', '1:8195', '1:23060', '1:23062', '1:6754', '1:6997', '1:7287', '1:8164', '1:8187', '1:8299', '1:13085', '1:8338', '1:8346', '1:8721', '1:8981', '1:90541', '1:84992', '1:92423', '1:92427', '1:92437', '1:14903', '1:15072', '1:15566', '1:15567', '1:15594', '1:14861', '1:14875', '1:14876', '1:14916', '1:14991', '1:18028', '1:18075', '1:18084', '1:18091', '1:18132', '1:18215', '1:40448', '1:24597', '1:10480', '1:10714', '1:10594', '1:10677', '1:10896', '1:10999', '1:13015', '1:13408', '1:14001', '1:14145', '1:14161', '1:14186', '1:15146', '1:23076', '1:23085', '1:23136', '1:23263', '1:23299', '1:23372', '1:23393', '1:19037', '1:17109', '1:17184', '1:17199', '1:17233', '1:17394', '1:17412', '1:17450', '1:17516', '1:23373', '1:23539', '1:23900', '1:25684', '1:28416', '1:31576', '1:32245', '1:33060', '1:33091', '1:34262', '1:23579', '1:28688', '1:28696', '1:11879', '1:11954', '1:11957', '1:12103', '1:12111', '1:12158', '1:12481', '1:11919', '1:11927', '1:12104', '1:12107', '1:12109', '1:12112', '1:12184', '1:12197', '1:34701', '1:34962', '1:35163', '1:35317', '1:35384', '1:37077', '1:39322', '1:35138', '1:35297', '1:35526', '1:35713', '1:56352', '1:60452', '1:36435', '1:36419', '1:36474', '1:36485', '1:36488', '1:36503', '1:36551', '1:36391', '1:36497', '1:36574', '1:23097', '1:23119', '1:23149', '1:23230', '1:23240', '1:23279', '1:23216', '1:23239', '1:23264', '1:99908', '1:28343', '1:28473', '1:28570', '1:28610', '1:28506', '1:28523', '1:28544', '1:28545', '1:28558', '1:28571', '1:28625', '1:28652', '1:28804', '1:63204', '1:68427', '1:68592', '1:74081', '1:74107', '1:34517', '1:49315', '1:50088', '1:50120', '1:34720', '1:34954', '1:36903', '1:36904', '1:38148', '1:38172', '1:38277', '1:33239', '1:36075', '1:33523', '1:33525', '1:33560', '1:56905', '1:57097', '1:57286', '1:53994', '1:56022', '1:56436', '1:56536', '1:63584', '1:63831', '1:63989', '1:64000', '1:64009', '1:64132', '1:64156', '1:64187', '1:64294', '1:64517', '1:64659', '1:64963', '1:64416', '1:55279', '1:57675', '1:58349', '1:58786', '1:87558', '1:91159', '1:99943', '1:100573', '1:100883', '1:100890', '1:100400', '1:100458', '1:100558', '1:100620', '1:100882', '1:100903', '1:100905', '1:100962', '1:100978', '1:101255', '1:1240', '1:1286', '1:1296', '1:1316', '1:1350', '1:1354', '1:1420', '1:1566', '1:1567', '1:4134', '1:4148', '1:4206', '1:4221', '1:4224', '1:4238', '1:4249', '1:21933', '1:22345', '1:21780', '1:21798', '1:22349', '1:22454', '1:30876', '1:39041', '1:39162', '1:39179', '1:31234', '1:57512', '1:62048', '1:62897', '1:63246', '1:63516', '1:63524', '1:50719', '1:27286', '1:27337', '1:27676', '1:27701', '1:28692', '1:28719', '1:28711', '1:28784', '1:28792', '1:10524', '1:10598', '1:10605', '1:10653', '1:10673', '1:13094', '1:14139', '1:14179', '1:14299', '1:14315', '1:14388', '1:27521', '1:35583', '1:35291', '1:35431', '1:35520', '1:35545', '1:35549', '1:35573', '1:35704', '1:35757', '1:35616', '1:35646', '1:35743', '1:35973', '1:35997', '1:52742', '1:52766', '1:52794', '1:21969', '1:22142', '1:22194', '1:22491', '1:22369', '1:22385', '1:22861', '1:22921', '1:26701', '1:29123', '1:29212', '1:29714', '1:31583', '1:32489', '1:31716', '1:31740', '1:31767', '1:31781', '1:31787', '1:31789', '1:31953', '1:31990', '1:37897', '1:39558', '1:39971', '1:40487', '1:52638', '1:52907', '1:57179', '1:52498', '1:52645', '1:52864', '1:92227', '1:2427', '1:2666', '1:5221', '1:733', '1:881', '1:962', '1:2075', '1:2225', '1:40607', '1:46087', '1:46899', '1:40080', '1:40085', '1:40092', '1:40106', '1:24125', '1:23147', '1:27806', '1:31664', '1:32586', '1:37786', '1:24847', '1:30471', '1:31753', '1:58397', '1:28874', '1:28906', '1:28910', '1:28922', '1:28974', '1:29815', '1:31078', '1:31094', '1:28965', '1:28969', '1:30069', '1:30149', '1:29314', '1:30206', '1:39882', '1:88410', '1:99210', '1:36677', '1:36695', '1:36803', '1:56572', '1:56604', '1:56625', '1:49468', '1:49322', '1:50678', '1:49598', '1:53325', '1:54399', '1:59559', '1:60704', '1:63305', '1:50094', '1:53835', '1:56763', '1:59575', '1:59803', '1:60740', '1:9482', '1:8345', '1:8450', '1:8741', '1:8945', '1:9916', '1:9973', '1:15030', '1:15303', '1:6926', '1:9773', '1:16906', '1:21149', '1:45603', '1:48162', '1:48202', '1:48204', '1:48647', '1:48649', '1:48811', '1:43781', '1:45718', '1:9068', '1:9341', '1:9634', '1:10151', '1:10171', '1:10312', '1:15495', '1:23107', '1:23137', '1:23487', '1:23552', '1:23727', '1:23771', '1:27004', '1:27035', '1:27132', '1:27139', '1:10881', '1:2672', '1:2752', '1:4295', '1:7530', '1:7571', '1:7573', '1:7807', '1:2695', '1:2851', '1:3993', '1:5006', '1:6042', '1:6314', '1:6468', '1:6622', '1:6780', '1:26343', '1:26486', '1:26616', '1:26879', '1:26977', '1:26510', '1:26632', '1:26706', '1:26715', '1:26759', '1:29005', '1:29043', '1:29087', '1:26547', '1:26658', '1:26670', '1:26791', '1:26817', '1:26916', '1:60429', '1:60467', '1:60491', '1:60576', '1:60579', '1:60632', '1:60708', '1:60722', '1:61132', '1:61204', '1:61217', '1:61245', '1:60962', '1:61534', '1:61678', '1:61713', '1:60745', '1:60874', '1:60882', '1:13433', '1:13570', '1:13993', '1:15152', '1:16108', '1:16276', '1:16763', '1:17152', '1:13318', '1:13351', '1:13443', '1:13698', '1:71258', '1:74354', '1:79423', '1:80981', '1:81541', '1:87094', '1:29923', '1:36025', '1:36069', '1:36115', '1:33055', '1:33352', '1:33462', '1:33494', '1:33503', '1:33549', '1:33591', '1:33609', '1:33712', '1:30104', '1:33282', '1:33285', '1:32350', '1:32372', '1:32617', '1:32448', '1:34573', '1:37071', '1:39192', '1:33343', '1:56957', '1:56963', '1:56979', '1:57374', '1:29670', '1:29800', '1:29818', '1:29905', '1:32437', '1:32445', '1:33775', '1:34005', '1:36153', '1:36402', '1:29878', '1:36225', '1:36436', '1:36531', '1:30321', '1:30520', '1:30650', '1:30695', '1:30784', '1:30808', '1:30862', '1:30921', '1:30959', '1:31020', '1:30501', '1:30523', '1:30566', '1:30594', '1:30602', '1:30618', '1:30642', '1:30675', '1:30792', '1:30849', '1:30913', '1:40344', '1:40357', '1:40476', '1:40533', '1:40595', '1:40628', '1:40629', '1:40670', '1:40471', '1:40488', '1:40609', '1:40976', '1:76441', '1:80395', '1:81436', '1:85005', '1:34294', '1:37293', '1:34732', '1:35115', '1:35185', '1:35650', '1:35665', '1:35681', '1:35696', '1:58348', '1:58597', '1:58605', '1:58968', '1:59306', '1:59337', '1:59442', '1:59990', '1:60899', '1:61876', '1:90488', '1:90993', '1:54622', '1:58204', '1:21210', '1:21224', '1:21452', '1:21164', '1:21188', '1:21377', '1:21439', '1:21746', '1:21845', '1:21151', '1:21378', '1:21381', '1:24991', '1:27210', '1:27235', '1:27283', '1:27348', '1:27369', '1:27508', '1:27583', '1:40888', '1:46966', '1:50450', '1:50603', '1:50799', '1:51297', '1:51451', '1:51478', '1:31508', '1:31786', '1:31851', '1:31989', '1:32287', '1:32288', '1:32392', '1:32442', '1:32538', '1:32521', '1:32530', '1:32570', '1:32785', '1:25448', '1:25594', '1:25645', '1:25709', '1:38569', '1:38576', '1:38585', '1:38590', '1:38591', '1:25427', '1:25484', '1:25600', '1:25633', '1:25740', '1:25766', '1:25772', '1:26038', '1:26320', '1:26385', '1:26576', '1:26683', '1:25485', '1:25509', '1:25511', '1:25581', '1:25612', '1:32197', '1:32440', '1:32701', '1:34153', '1:34258', '1:34452', '1:32268', '1:32325', '1:32342', '1:32459', '1:32519', '1:32525', '1:32663', '1:32688', '1:32696', '1:32713', '1:32789', '1:34204', '1:34644', '1:34668', '1:34903', '1:34989', '1:35030', '1:35155', '1:58208', '1:59061', '1:60591', '1:52446', '1:55799', '1:55932', '1:56555', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A2F9ADEF-4E18-EA11-AF7B-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/F28EB257-6118-EA11-9A40-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/36C76096-3C1A-EA11-A0D5-A0369F7FC4E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B0481AAA-8918-EA11-A0A3-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/50F00FB5-151C-EA11-92A8-0CC47A706CDE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8ADCCDDD-2018-EA11-8340-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2E1D0844-3F1A-EA11-8CBB-FA163EDB1C36.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/40D02E20-7319-EA11-8EAA-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1A4C2C9F-1A18-EA11-A66A-FA163E4874D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D2E6798B-D417-EA11-AAE5-EC0D9A8221D6.root']);