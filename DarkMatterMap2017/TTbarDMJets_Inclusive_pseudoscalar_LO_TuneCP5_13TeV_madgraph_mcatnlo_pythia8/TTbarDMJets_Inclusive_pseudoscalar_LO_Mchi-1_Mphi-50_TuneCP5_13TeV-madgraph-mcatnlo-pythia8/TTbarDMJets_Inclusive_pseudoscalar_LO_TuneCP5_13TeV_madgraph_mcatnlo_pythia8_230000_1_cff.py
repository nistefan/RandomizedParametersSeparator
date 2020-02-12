import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:32463', '1:32503', '1:32588', '1:32634', '1:32585', '1:32730', '1:32766', '1:49559', '1:51315', '1:51353', '1:51356', '1:51466', '1:51472', '1:51476', '1:51517', '1:51526', '1:51536', '1:53320', '1:53322', '1:53406', '1:53431', '1:54279', '1:54534', '1:47459', '1:47461', '1:47598', '1:47606', '1:47970', '1:53359', '1:53364', '1:53463', '1:53464', '1:53811', '1:53840', '1:54085', '1:54213', '1:54349', '1:54430', '1:54513', '1:58467', '1:58507', '1:58624', '1:59010', '1:59140', '1:3431', '1:3443', '1:3454', '1:3943', '1:3953', '1:3997', '1:4058', '1:4140', '1:4182', '1:4458', '1:4486', '1:4609', '1:4642', '1:4778', '1:5038', '1:7939', '1:7949', '1:9088', '1:5593', '1:6075', '1:6121', '1:6361', '1:6375', '1:6497', '1:6641', '1:6644', '1:6665', '1:6780', '1:6876', '1:6916', '1:13340', '1:12850', '1:13247', '1:13279', '1:13321', '1:9599', '1:12747', '1:18032', '1:18085', '1:18112', '1:18226', '1:18227', '1:18295', '1:18332', '1:18423', '1:18445', '1:18504', '1:18510', '1:18561', '1:18818', '1:27654', '1:18414', '1:18523', '1:18657', '1:18677', '1:18442', '1:18465', '1:18497', '1:18578', '1:18612', '1:18732', '1:18748', '1:18758', '1:18976', '1:51461', '1:52102', '1:18425', '1:18629', '1:18749', '1:18274', '1:18324', '1:18329', '1:18341', '1:18354', '1:18415', '1:18458', '1:18634', '1:18762', '1:18845', '1:18877', '1:18896', '1:32574', '1:19838', '1:19911', '1:19932', '1:19239', '1:19293', '1:19405', '1:19421', '1:19449', '1:19457', '1:19556', '1:19742', '1:19751', '1:19875', '1:19885', '1:19995', '1:20077', '1:20508', '1:20827', '1:20905', '1:22656', '1:27659', '1:27673', '1:27781', '1:27829', '1:27830', '1:27843', '1:27876', '1:45699', '1:18737', '1:18803', '1:20393', '1:22092', '1:22118', '1:22207', '1:22216', '1:22705', '1:22742', '1:41473', '1:28134', '1:28150', '1:28468', '1:28516', '1:28541', '1:28577', '1:28583', '1:28630', '1:28826', '1:28829', '1:28834', '1:28872', '1:28937', '1:40991', '1:41009', '1:41027', '1:41031', '1:41033', '1:41114', '1:41130', '1:41139', '1:41246', '1:41273', '1:41292', '1:41132', '1:41265', '1:41368', '1:1751', '1:2614', '1:3042', '1:6529', '1:9536', '1:5518', '1:6171', '1:7967', '1:8221', '1:54141', '1:55290', '1:55636', '1:48507', '1:49683', '1:49919', '1:51377', '1:52198', '1:52441', '1:54338', '1:42109', '1:42508', '1:42532', '1:42582', '1:42630', '1:42653', '1:42667', '1:42727', '1:42789', '1:43031', '1:43039', '1:43044', '1:43055', '1:48619', '1:48646', '1:48663', '1:48778', '1:83943', '1:83951', '1:85400', '1:85480', '1:85619', '1:85794', '1:85854', '1:85934', '1:86675', '1:86705', '1:86707', '1:86726', '1:86772', '1:86813', '1:86844', '1:89334', '1:103101', '1:103212', '1:103223', '1:103302', '1:103380', '1:103432', '1:103497', '1:103543', '1:103600', '1:64885', '1:71402', '1:71487', '1:72556', '1:70166', '1:70292', '1:70385', '1:70430', '1:70505', '1:57224', '1:57233', '1:57248', '1:57628', '1:58295', '1:58304', '1:77197', '1:81205', '1:82078', '1:82362', '1:82591', '1:89223', '1:1785', '1:2070', '1:2362', '1:2426', '1:2485', '1:2775', '1:2807', '1:2810', '1:2241', '1:2379', '1:2501', '1:2541', '1:2581', '1:2712', '1:2743', '1:6101', '1:6123', '1:6139', '1:6464', '1:6357', '1:6382', '1:6584', '1:6593', '1:6884', '1:6908', '1:7034', '1:6804', '1:7131', '1:8076', '1:8457', '1:7196', '1:7197', '1:7358', '1:7609', '1:8253', '1:8303', '1:8391', '1:8497', '1:9607', '1:10613', '1:9839', '1:9953', '1:9968', '1:10237', '1:10371', '1:10414', '1:10483', '1:10609', '1:10645', '1:10679', '1:10718', '1:10823', '1:11148', '1:11405', '1:11768', '1:10783', '1:10831', '1:10944', '1:11154', '1:11558', '1:11835', '1:12830', '1:13978', '1:14129', '1:15091', '1:14026', '1:14266', '1:15057', '1:13945', '1:14314', '1:14075', '1:58104', '1:58224', '1:58355', '1:58364', '1:58230', '1:58602', '1:59088', '1:5693', '1:5701', '1:5976', '1:6010', '1:6589', '1:6647', '1:6899', '1:6906', '1:6911', '1:7159', '1:8042', '1:8103', '1:8373', '1:8567', '1:8778', '1:8860', '1:9622', '1:9882', '1:9091', '1:9472', '1:8407', '1:8488', '1:9172', '1:9576', '1:8926', '1:8934', '1:9073', '1:9229', '1:9373', '1:9511', '1:16438', '1:16541', '1:16821', '1:16866', '1:6006', '1:5999', '1:6110', '1:6128', '1:13313', '1:12144', '1:12270', '1:12281', '1:12404', '1:12666', '1:13028', '1:13288', '1:14490', '1:14507', '1:14628', '1:14790', '1:14837', '1:14975', '1:15029', '1:15151', '1:15306', '1:15548', '1:15662', '1:15709', '1:15799', '1:15929', '1:16461', '1:16498', '1:16595', '1:16729', '1:16889', '1:26996', '1:17415', '1:17458', '1:17520', '1:17524', '1:17586', '1:17983', '1:18126', '1:18139', '1:18382', '1:18391', '1:18821', '1:41557', '1:41558', '1:41571', '1:41604', '1:41616', '1:41654', '1:41669', '1:41568', '1:41603', '1:41650', '1:41651', '1:41662', '1:41666', '1:41694', '1:41738', '1:46059', '1:45710', '1:45719', '1:45741', '1:45747', '1:45748', '1:45860', '1:46223', '1:47024', '1:54763', '1:55815', '1:18772', '1:18888', '1:18917', '1:19042', '1:41775', '1:41799', '1:41897', '1:43062', '1:43105', '1:43142', '1:43202', '1:43224', '1:43474', '1:43519', '1:43733', '1:43898', '1:46051', '1:46213', '1:46349', '1:46485', '1:80345', '1:77906', '1:77914', '1:77986', '1:78028', '1:78100', '1:78206', '1:78214', '1:78358', '1:78610', '1:78756', '1:20713', '1:20861', '1:20862', '1:20863', '1:20964', '1:21014', '1:21025', '1:21167', '1:21232', '1:21438', '1:21442', '1:21819', '1:23014', '1:23147', '1:97343', '1:97351', '1:97378', '1:97562', '1:97852', '1:97930', '1:97954', '1:98354', '1:98699', '1:98780', '1:98920', '1:103235', '1:103301', '1:103342', '1:103457', '1:103195', '1:103200', '1:103226', '1:103480', '1:103489', '1:8166', '1:10410', '1:11979', '1:15687', '1:32637', '1:25433', '1:25530', '1:26166', '1:31777', '1:43350', '1:46011', '1:29555', '1:30192', '1:32632', '1:44667', '1:30751', '1:30875', '1:39134', '1:44262', '1:55571', '1:56583', '1:56668', '1:56780', '1:56846', '1:94765', '1:91843', '1:92815', '1:95579', '1:101415', '1:102622', '1:104600', '1:16765', '1:16847', '1:16858', '1:16952', '1:21448', '1:26209', '1:26324', '1:26566', '1:26776', '1:26823', '1:26948', '1:76757', '1:76774', '1:80614', '1:81238', '1:93864', '1:18024', '1:47517', '1:40547', '1:45862', '1:48575', '1:53157', '1:53595', '1:55269', '1:55478', '1:57179', '1:57367', '1:57874', '1:58833', '1:60279', '1:60700', '1:61061', '1:61578', '1:61623', '1:62598', '1:43986', '1:46193', '1:58486', '1:60441', '1:60579', '1:61570', '1:97421', '1:98501', '1:98728', '1:92251', '1:101117', '1:1014', '1:1022', '1:3797', '1:4283', '1:6398', '1:1549', '1:2619', '1:4534', '1:14080', '1:27426', '1:27484', '1:29090', '1:39493', '1:42794', '1:44304', '1:27606', '1:29837', '1:30147', '1:39325', '1:39462', '1:39959', '1:42369', '1:42522', '1:42539', '1:42677', '1:42848', '1:42959', '1:42960', '1:43407', '1:73901', '1:41148', '1:48645', '1:48940', '1:51585', '1:55450', '1:60049', '1:60170', '1:61827', '1:62354', '1:53518', '1:56855', '1:1522', '1:12914', '1:13913', '1:15149', '1:15162', '1:15432', '1:15478', '1:15659', '1:16888', '1:13330', '1:13650', '1:14436', '1:26545', '1:31135', '1:31855', '1:25977', '1:31929', '1:31953', '1:31964', '1:32000', '1:21069', '1:21341', '1:83632', '1:87729', '1:95829', '1:96527', '1:83724', '1:90914', '1:90942', '1:94721', '1:95067', '1:95912', '1:96512', '1:46714', '1:49489', '1:51285', '1:55360', '1:55499', '1:55506', '1:61032', '1:87801', '1:89700', '1:95472', '1:90747', '1:86523', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90043704-20FC-E911-8078-0CC47AFCC3D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/58F7196A-76FC-E911-8198-0025905C96E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B65A1C1B-7FFC-E911-92D1-0CC47AFCC392.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/30FB16E9-BC12-EA11-A843-7CD30AC03722.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70BD48D5-3CF5-E911-BBCD-D4856445E5A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E131ABC-63F2-E911-BBAD-441EA157ADE4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/00610B13-6BF2-E911-832F-98039B3B01B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2E996FF0-01F5-E911-BFCE-D4856444A744.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/501EAB60-EC02-EA11-9994-0CC47AFCC6B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3AF7C78E-7106-EA11-9305-0025905C3E68.root']);