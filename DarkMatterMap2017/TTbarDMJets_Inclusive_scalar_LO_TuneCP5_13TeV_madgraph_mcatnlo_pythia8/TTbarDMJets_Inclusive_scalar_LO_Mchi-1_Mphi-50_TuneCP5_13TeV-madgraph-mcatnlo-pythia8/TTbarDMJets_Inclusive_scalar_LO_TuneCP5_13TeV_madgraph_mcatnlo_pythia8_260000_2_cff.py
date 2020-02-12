import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:3720', '1:3776', '1:3952', '1:3874', '1:14217', '1:17536', '1:19305', '1:20449', '1:22101', '1:5015', '1:4287', '1:4310', '1:4344', '1:4372', '1:4488', '1:4365', '1:4369', '1:4850', '1:5125', '1:5440', '1:5462', '1:4483', '1:4492', '1:14851', '1:22145', '1:16779', '1:12516', '1:12541', '1:12562', '1:14204', '1:14532', '1:14557', '1:14570', '1:14643', '1:14659', '1:14741', '1:14752', '1:14776', '1:14878', '1:14954', '1:14975', '1:15732', '1:19004', '1:19124', '1:17847', '1:28747', '1:32162', '1:34748', '1:9063', '1:9200', '1:9052', '1:10074', '1:16347', '1:21472', '1:22525', '1:22848', '1:16288', '1:17901', '1:21316', '1:21322', '1:21445', '1:32715', '1:33364', '1:49528', '1:31996', '1:27377', '1:27603', '1:62927', '1:63339', '1:63809', '1:69860', '1:69979', '1:63561', '1:23008', '1:23011', '1:23143', '1:23151', '1:23274', '1:10068', '1:10165', '1:10447', '1:13179', '1:10548', '1:10754', '1:10757', '1:26219', '1:26238', '1:26243', '1:26399', '1:26507', '1:26558', '1:26678', '1:26743', '1:26308', '1:26511', '1:26568', '1:26626', '1:26904', '1:26936', '1:26944', '1:33107', '1:33138', '1:33630', '1:33684', '1:30320', '1:30337', '1:30339', '1:30362', '1:30477', '1:30483', '1:34638', '1:37184', '1:39233', '1:39996', '1:40124', '1:32352', '1:32667', '1:32854', '1:34161', '1:34249', '1:34315', '1:34412', '1:34672', '1:32660', '1:32823', '1:74112', '1:80316', '1:90562', '1:91120', '1:102372', '1:36204', '1:36312', '1:36325', '1:36333', '1:36269', '1:36337', '1:36616', '1:36621', '1:36650', '1:57468', '1:57713', '1:57819', '1:58186', '1:58335', '1:58555', '1:59242', '1:59817', '1:59882', '1:57738', '1:57761', '1:57772', '1:57856', '1:57909', '1:57999', '1:86546', '1:95653', '1:97049', '1:100396', '1:58546', '1:58558', '1:58658', '1:58673', '1:58781', '1:58873', '1:59049', '1:59102', '1:59249', '1:59789', '1:60299', '1:89289', '1:90377', '1:94082', '1:94383', '1:94945', '1:100307', '1:94918', '1:95163', '1:99603', '1:99653', '1:99666', '1:100788', '1:100918', '1:101104', '1:65396', '1:65398', '1:46013', '1:46017', '1:46051', '1:46053', '1:91622', '1:98622', '1:101742', '1:90609', '1:38231', '1:38655', '1:37192', '1:37248', '1:37312', '1:50790', '1:53385', '1:60936', '1:61409', '1:57836', '1:57851', '1:57897', '1:58604', '1:58767', '1:58995', '1:59161', '1:59485', '1:58195', '1:58347', '1:58502', '1:58528', '1:58567', '1:58409', '1:37743', '1:38354', '1:38376', '1:38385', '1:38399', '1:40902', '1:50553', '1:59303', '1:61414', '1:50517', '1:86884', '1:87401', '1:61902', '1:75257', '1:77685', '1:78779', '1:69117', '1:72152', '1:74116', '1:74160', '1:74216', '1:76752', '1:56128', '1:56264', '1:56554', '1:56553', '1:56751', '1:56808', '1:57311', '1:57315', '1:56643', '1:89731', '1:57074', '1:58097', '1:58154', '1:58239', '1:68556', '1:77020', '1:80105', '1:80137', '1:80831', '1:87506', '1:79254', '1:81814', '1:81899', '1:87441', '1:89044', '1:89441', '1:6340', '1:14384', '1:14943', '1:20400', '1:22712', '1:6333', '1:7373', '1:10095', '1:10522', '1:14740', '1:18096', '1:18331', '1:22898', '1:6731', '1:16710', '1:17011', '1:17146', '1:17165', '1:17222', '1:8105', '1:8323', '1:59279', '1:28396', '1:28660', '1:28890', '1:28909', '1:29666', '1:26994', '1:29016', '1:29060', '1:29106', '1:29135', '1:29199', '1:29210', '1:29251', '1:29260', '1:29268', '1:29313', '1:29056', '1:29339', '1:29351', '1:32858', '1:32866', '1:33298', '1:57011', '1:57952', '1:59117', '1:59562', '1:63194', '1:81455', '1:85592', '1:91701', '1:54438', '1:57377', '1:53253', '1:17373', '1:17475', '1:17639', '1:17663', '1:17871', '1:17959', '1:17540', '1:17848', '1:17887', '1:17905', '1:17928', '1:18019', '1:18168', '1:18377', '1:18409', '1:18878', '1:17830', '1:17951', '1:54286', '1:17790', '1:21209', '1:21559', '1:21667', '1:17660', '1:17941', '1:17968', '1:18241', '1:18266', '1:18502', '1:17942', '1:19636', '1:20386', '1:20761', '1:21007', '1:21289', '1:35857', '1:58486', '1:49217', '1:51251', '1:24682', '1:24707', '1:24714', '1:24753', '1:24795', '1:24803', '1:37381', '1:22015', '1:22072', '1:22129', '1:22706', '1:22711', '1:22768', '1:22867', '1:22873', '1:22148', '1:22242', '1:22288', '1:22311', '1:22612', '1:22643', '1:22662', '1:26006', '1:22379', '1:23585', '1:37379', '1:23294', '1:23160', '1:23484', '1:23491', '1:23548', '1:23857', '1:23976', '1:24001', '1:24027', '1:24124', '1:24137', '1:24206', '1:24303', '1:25979', '1:26214', '1:28823', '1:33954', '1:37178', '1:37436', '1:37579', '1:25237', '1:25244', '1:25269', '1:25274', '1:25325', '1:25327', '1:25373', '1:25406', '1:25422', '1:25439', '1:25443', '1:25613', '1:25522', '1:25556', '1:25558', '1:25574', '1:25590', '1:37350', '1:37447', '1:37472', '1:37496', '1:37584', '1:37536', '1:37561', '1:37793', '1:40039', '1:40060', '1:40230', '1:40250', '1:40394', '1:40491', '1:40550', '1:40689', '1:40690', '1:13989', '1:15586', '1:6956', '1:6988', '1:17561', '1:18597', '1:20276', '1:21518', '1:25254', '1:25295', '1:7607', '1:14769', '1:17307', '1:20514', '1:18381', '1:18658', '1:19123', '1:19671', '1:19923', '1:20423', '1:20920', '1:22979', '1:22997', '1:18696', '1:18710', '1:19020', '1:19075', '1:30251', '1:33886', '1:34020', '1:34415', '1:34991', '1:36962', '1:52255', '1:24152', '1:24428', '1:24659', '1:24680', '1:24954', '1:30226', '1:39476', '1:40382', '1:40901', '1:24335', '1:33166', '1:62480', '1:64512', '1:78851', '1:28875', '1:30445', '1:31202', '1:31306', '1:31380', '1:32110', '1:27823', '1:27849', '1:27905', '1:27906', '1:27937', '1:27982', '1:36354', '1:54970', '1:55235', '1:55579', '1:62447', '1:55241', '1:73014', '1:52840', '1:52902', '1:52920', '1:52987', '1:56087', '1:56191', '1:56216', '1:53308', '1:53363', '1:53562', '1:53566', '1:53590', '1:56056', '1:63233', '1:498', '1:717', '1:864', '1:887', '1:895', '1:903', '1:948', '1:15467', '1:18950', '1:19494', '1:22981', '1:796', '1:16896', '1:25888', '1:25892', '1:25896', '1:25900', '1:25915', '1:25918', '1:25926', '1:25968', '1:25976', '1:26009', '1:26020', '1:26119', '1:26066', '1:26184', '1:26244', '1:26264', '1:26311', '1:26328', '1:26377', '1:26403', '1:26450', '1:26516', '1:26646', '1:34836', '1:36895', '1:36972', '1:37400', '1:37426', '1:37427', '1:37441', '1:37507', '1:37557', '1:37569', '1:37439', '1:37577', '1:25701', '1:25711', '1:25759', '1:25829', '1:25835', '1:25768', '1:25777', '1:25791', '1:25808', '1:25822', '1:25843', '1:25863', '1:25880', '1:25921', '1:26060', '1:26077', '1:34416', '1:34470', '1:32877', '1:32890', '1:32905', '1:32909', '1:32912', '1:32917', '1:32989', '1:32990', '1:33538', '1:33679', '1:36007', '1:36022', '1:36041', '1:36218', '1:62417', '1:62389', '1:64845', '1:76193', '1:78279', '1:69231', '1:75518', '1:88994', '1:89413', '1:70547', '1:94224', '1:97284', '1:39396', '1:40237', '1:33093', '1:33177', '1:33203', '1:4862', '1:6894', '1:15051', '1:15764', '1:17633', '1:18443', '1:20312', '1:21008', '1:21694', '1:25004', '1:25012', '1:25014', '1:25056', '1:25100', '1:25126', '1:4954', '1:4994', '1:5003', '1:5039', '1:5290', '1:5328', '1:5402', '1:5538', '1:5628', '1:5633', '1:39173', '1:7303', '1:7432', '1:7503', '1:7577', '1:7619', '1:7649', '1:7729', '1:7893', '1:7298', '1:7309', '1:7553', '1:7822', '1:51969', '1:62034', '1:64464', '1:64796', '1:51155', '1:51170', '1:51320', '1:51429', '1:13648', '1:13691', '1:13793', '1:13914', '1:13947', '1:14193', '1:14266', '1:14360', '1:13934', '1:13935', '1:16072', '1:16171', '1:16213', '1:16218', '1:16310', '1:14785', '1:66053', '1:37039', '1:36165', '1:36175', '1:36190', '1:36261', '1:36289', '1:36340', '1:36367', '1:36368', '1:36376', '1:36408', '1:36483', '1:36509', '1:36228', '1:36398', '1:36527', '1:36661', '1:74115', '1:77828', '1:36983', '1:38608', '1:38627', '1:37605', '1:39119', '1:39140', '1:39163', '1:39197', '1:43101', '1:43104', '1:44591', '1:36705', '1:65961', '1:73806', '1:74012', '1:74074', '1:74085', '1:74088', '1:12252', '1:41275', '1:41299', '1:42784', '1:47197', '1:43462', '1:48511', '1:65842', '1:44635', '1:83145', '1:83225', '1:11265', '1:11520', '1:11458', '1:11860', '1:12326', '1:33388', '1:40040', '1:46198', '1:27228', '1:40433', '1:40438', '1:46036', '1:46580', '1:49660', '1:50101', '1:41323', '1:41438', '1:41468', '1:42320', '1:42452', '1:42476', '1:42484', '1:42494', '1:42508', '1:42537', '1:42542', '1:42563', '1:42564', '1:42571', '1:42573', '1:42577', '1:42603', '1:42607', '1:42834', '1:47210', '1:47947', '1:74410', '1:74725', '1:74750', '1:75612', '1:75668', '1:76045', '1:76197', '1:77895', '1:68335', '1:70550', '1:71319', '1:74906', '1:67207', '1:68740', '1:76306', '1:100', '1:186', '1:235', '1:1060', '1:1301', '1:4506', '1:4757', '1:5562', '1:5600', '1:114', '1:3838', '1:3968', '1:4638', '1:4998', '1:5046', '1:21508', '1:21352', '1:21494', '1:20957', '1:20979', '1:21097', '1:21250', '1:21328', '1:21824', '1:22389', '1:22689', '1:22753', '1:22780', '1:21037', '1:21120', '1:21126', '1:21426', '1:21672', '1:64395', '1:64422', '1:67481', '1:67749', '1:67844', '1:68617', '1:68867', '1:69136', '1:69185', '1:69250', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54320079-E317-EA11-B1DF-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA975838-3C18-EA11-8F0A-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8A7D5B5-EE17-EA11-8D58-FA163EE3F24C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/76D2EDA7-0918-EA11-9BB4-FA163E20F521.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/768B8E9C-D417-EA11-B213-FA163ECFF9D5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E645838E-2C18-EA11-816C-FA163EE93463.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/060AC0C7-F517-EA11-AD2C-FA163E8B993E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DE51B3B4-8618-EA11-914B-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/9830A3F9-341A-EA11-A175-EC0D9A82264E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/5A3E632C-401A-EA11-80A3-6CC2173C4580.root']);