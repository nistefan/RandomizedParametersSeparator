import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:59854', '1:93238', '1:97609', '1:94699', '1:94950', '1:97744', '1:106282', '1:103377', '1:103673', '1:105153', '1:105536', '1:67553', '1:60575', '1:60265', '1:66136', '1:73431', '1:74276', '1:75325', '1:75632', '1:76129', '1:66388', '1:67704', '1:74593', '1:88030', '1:88811', '1:89716', '1:89742', '1:90619', '1:91555', '1:91886', '1:93417', '1:93482', '1:93754', '1:97182', '1:97807', '1:103114', '1:103899', '1:73597', '1:74090', '1:74360', '1:75707', '1:76852', '1:79042', '1:79341', '1:81881', '1:71870', '1:72772', '1:76756', '1:78478', '1:78541', '1:78551', '1:75209', '1:80268', '1:13525', '1:14447', '1:14552', '1:14803', '1:14906', '1:15056', '1:15189', '1:16975', '1:24866', '1:24869', '1:24901', '1:24909', '1:24918', '1:27124', '1:25107', '1:25221', '1:25237', '1:25268', '1:25294', '1:25414', '1:31086', '1:31187', '1:31282', '1:31290', '1:31327', '1:31278', '1:31351', '1:31393', '1:31427', '1:31430', '1:31529', '1:51736', '1:51812', '1:22729', '1:22779', '1:22843', '1:22899', '1:22933', '1:22941', '1:22991', '1:22926', '1:29158', '1:29241', '1:29380', '1:29417', '1:29290', '1:29307', '1:46632', '1:46642', '1:48026', '1:48139', '1:48240', '1:5617', '1:13116', '1:16410', '1:19662', '1:20977', '1:23701', '1:23782', '1:24688', '1:24912', '1:7227', '1:13935', '1:20581', '1:26117', '1:17878', '1:21833', '1:27194', '1:29482', '1:39736', '1:18489', '1:18544', '1:28100', '1:29461', '1:29742', '1:32818', '1:45746', '1:47097', '1:47818', '1:53821', '1:54181', '1:55054', '1:56685', '1:57295', '1:58305', '1:56481', '1:58256', '1:59187', '1:17908', '1:23154', '1:23406', '1:26749', '1:18661', '1:29670', '1:30371', '1:30679', '1:30744', '1:32353', '1:32680', '1:26157', '1:27285', '1:27964', '1:28178', '1:28576', '1:30502', '1:31181', '1:31668', '1:32599', '1:55046', '1:81140', '1:85618', '1:77493', '1:83224', '1:83660', '1:84812', '1:85970', '1:86397', '1:78215', '1:96920', '1:81860', '1:79026', '1:79790', '1:80300', '1:80321', '1:81344', '1:81445', '1:95495', '1:91168', '1:92439', '1:94669', '1:52713', '1:58089', '1:67823', '1:72031', '1:72928', '1:76927', '1:79598', '1:46713', '1:46963', '1:46985', '1:48072', '1:48077', '1:48092', '1:48095', '1:48121', '1:48132', '1:48398', '1:48419', '1:48432', '1:48479', '1:51697', '1:51723', '1:51728', '1:51752', '1:51866', '1:51980', '1:51998', '1:52233', '1:52276', '1:52313', '1:52328', '1:52372', '1:86763', '1:86873', '1:87306', '1:87345', '1:87367', '1:87428', '1:87579', '1:87584', '1:87591', '1:87616', '1:87744', '1:67314', '1:67694', '1:71147', '1:70010', '1:70084', '1:70101', '1:70238', '1:70254', '1:70319', '1:70361', '1:70416', '1:70472', '1:70661', '1:70805', '1:77120', '1:77121', '1:70765', '1:77161', '1:71291', '1:71355', '1:71406', '1:71492', '1:71544', '1:71811', '1:72595', '1:72848', '1:73016', '1:73154', '1:74372', '1:83092', '1:83097', '1:83120', '1:83609', '1:83620', '1:83623', '1:83631', '1:97153', '1:97542', '1:83055', '1:83146', '1:83178', '1:83641', '1:96619', '1:86633', '1:87391', '1:87401', '1:87691', '1:54506', '1:54749', '1:54804', '1:54922', '1:55010', '1:55026', '1:55317', '1:55382', '1:55431', '1:55471', '1:55568', '1:55689', '1:55973', '1:56177', '1:58585', '1:58727', '1:58851', '1:58894', '1:58920', '1:58936', '1:58999', '1:59008', '1:59027', '1:59044', '1:59175', '1:59284', '1:59301', '1:59409', '1:59426', '1:103172', '1:61106', '1:61223', '1:61253', '1:61374', '1:61406', '1:61447', '1:61470', '1:61486', '1:60754', '1:60849', '1:60860', '1:60883', '1:60996', '1:61034', '1:61058', '1:61075', '1:62665', '1:62782', '1:78595', '1:78722', '1:70248', '1:70358', '1:82946', '1:82955', '1:84153', '1:84792', '1:84875', '1:83074', '1:83075', '1:82463', '1:82478', '1:83257', '1:83094', '1:83490', '1:83743', '1:84098', '1:84270', '1:84521', '1:85257', '1:97409', '1:61284', '1:61286', '1:61307', '1:61395', '1:61479', '1:82267', '1:82381', '1:82414', '1:83021', '1:3178', '1:3299', '1:3446', '1:3912', '1:4062', '1:4078', '1:4159', '1:4198', '1:4487', '1:6379', '1:6521', '1:6654', '1:6858', '1:6992', '1:7013', '1:7039', '1:7370', '1:7421', '1:7436', '1:7483', '1:7706', '1:11883', '1:13188', '1:11993', '1:12923', '1:13646', '1:14042', '1:15376', '1:23294', '1:52132', '1:52197', '1:52541', '1:52669', '1:52887', '1:52895', '1:53172', '1:59485', '1:59616', '1:59735', '1:60027', '1:60045', '1:60182', '1:60264', '1:60807', '1:60945', '1:62253', '1:62350', '1:54495', '1:54526', '1:54641', '1:54674', '1:54700', '1:54709', '1:54716', '1:54748', '1:54846', '1:57775', '1:57996', '1:56821', '1:56950', '1:57062', '1:2790', '1:11820', '1:14184', '1:2175', '1:10921', '1:12022', '1:12791', '1:1729', '1:9478', '1:9848', '1:11297', '1:11772', '1:13710', '1:13983', '1:2117', '1:13216', '1:15890', '1:105220', '1:43475', '1:48475', '1:52168', '1:58266', '1:58636', '1:58753', '1:59448', '1:60457', '1:60825', '1:56856', '1:57821', '1:62063', '1:66291', '1:73921', '1:79105', '1:52919', '1:58241', '1:58944', '1:61251', '1:62529', '1:62797', '1:64681', '1:64864', '1:67458', '1:67728', '1:20473', '1:21308', '1:21980', '1:23630', '1:23790', '1:25947', '1:17937', '1:25645', '1:26175', '1:31030', '1:105426', '1:105538', '1:24447', '1:23617', '1:27698', '1:28216', '1:30120', '1:39800', '1:43923', '1:45993', '1:61495', '1:62912', '1:80436', '1:102151', '1:104790', '1:105522', '1:105288', '1:106294', '1:101146', '1:101769', '1:102083', '1:102476', '1:55293', '1:64073', '1:64320', '1:64996', '1:65569', '1:67387', '1:88164', '1:88551', '1:91018', '1:94667', '1:105257', '1:77003', '1:83601', '1:84142', '1:85635', '1:88291', '1:105229', '1:105708', '1:105239', '1:6903', '1:8652', '1:10070', '1:21086', '1:23616', '1:24565', '1:25774', '1:17193', '1:21156', '1:21866', '1:31306', '1:28774', '1:29505', '1:39701', '1:82228', '1:67450', '1:70509', '1:84250', '1:82183', '1:84435', '1:70309', '1:70979', '1:84299', '1:84409', '1:84964', '1:85731', '1:4496', '1:4601', '1:4702', '1:5047', '1:5297', '1:5411', '1:5698', '1:6085', '1:6623', '1:7096', '1:7759', '1:8113', '1:8192', '1:8272', '1:8282', '1:2150', '1:2159', '1:2586', '1:2595', '1:2626', '1:2650', '1:2676', '1:2778', '1:2756', '1:2894', '1:4163', '1:4255', '1:4279', '1:4391', '1:4480', '1:4878', '1:13155', '1:13280', '1:13405', '1:14619', '1:14684', '1:15000', '1:14997', '1:15170', '1:15297', '1:15344', '1:15387', '1:15393', '1:15403', '1:15417', '1:15665', '1:23764', '1:23805', '1:23881', '1:23893', '1:23913', '1:23977', '1:25037', '1:25038', '1:25118', '1:25141', '1:25302', '1:24862', '1:54926', '1:57856', '1:57900', '1:58128', '1:43868', '1:43946', '1:43958', '1:44072', '1:44105', '1:44574', '1:45261', '1:45724', '1:45733', '1:45790', '1:45821', '1:45842', '1:45907', '1:46000', '1:47062', '1:47084', '1:47157', '1:49372', '1:49393', '1:49480', '1:49482', '1:49511', '1:49528', '1:49532', '1:49546', '1:49563', '1:49603', '1:49673', '1:56626', '1:56652', '1:56666', '1:56753', '1:56757', '1:57162', '1:57184', '1:57186', '1:57257', '1:57394', '1:57500', '1:57519', '1:57525', '1:1105', '1:1134', '1:1261', '1:1284', '1:1588', '1:4295', '1:4331', '1:2132', '1:2149', '1:2263', '1:2267', '1:2358', '1:2479', '1:2652', '1:2765', '1:3013', '1:3085', '1:3090', '1:3160', '1:21215', '1:21330', '1:21627', '1:21771', '1:21817', '1:21881', '1:21928', '1:21938', '1:21958', '1:21992', '1:23111', '1:23112', '1:23201', '1:23239', '1:23497', '1:23543', '1:31139', '1:31474', '1:31766', '1:31966', '1:31844', '1:31992', '1:31996', '1:49987', '1:51034', '1:51056', '1:51073', '1:51082', '1:51171', '1:51273', '1:51293', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E0B77C2-ACF2-E911-B839-44A8424762AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3A1BE4F7-5CF4-E911-B89E-00259073E40A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A4577A3-2BF6-E911-94E0-0CC47AD98D00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CC7FFA5E-9BF6-E911-93AA-0CC47AF97150.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D01DA64A-9AF5-E911-A0E9-D4856445E5A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/889C5882-D8F5-E911-8B63-FA163EE28B37.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8A4349A-CFF6-E911-AEDB-0CC47A2B03A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE4574FE-FCF6-E911-91C6-00259048AC12.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BEF69588-68F6-E911-821B-FA163EEB438E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/28FDC844-0CF8-E911-8538-002590D425C0.root']);