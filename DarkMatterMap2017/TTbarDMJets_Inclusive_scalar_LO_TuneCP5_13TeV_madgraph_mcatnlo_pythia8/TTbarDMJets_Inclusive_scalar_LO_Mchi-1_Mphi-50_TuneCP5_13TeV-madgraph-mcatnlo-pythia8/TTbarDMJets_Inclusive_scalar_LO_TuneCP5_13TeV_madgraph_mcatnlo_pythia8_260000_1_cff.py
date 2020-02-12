import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:9338', '1:9979', '1:9414', '1:25671', '1:25935', '1:25961', '1:25993', '1:33017', '1:33802', '1:33818', '1:33932', '1:33938', '1:9681', '1:10048', '1:10096', '1:10265', '1:10436', '1:73732', '1:13528', '1:13558', '1:14022', '1:14256', '1:13705', '1:13990', '1:14055', '1:15751', '1:15836', '1:15851', '1:17204', '1:17529', '1:18121', '1:19143', '1:19175', '1:19310', '1:13338', '1:14039', '1:56327', '1:14919', '1:15422', '1:15486', '1:15126', '1:15425', '1:16080', '1:15002', '1:15218', '1:15704', '1:15706', '1:15833', '1:20425', '1:20473', '1:20539', '1:20691', '1:20749', '1:20772', '1:20832', '1:20864', '1:20919', '1:20944', '1:21407', '1:20535', '1:20914', '1:27752', '1:27767', '1:27883', '1:28009', '1:28182', '1:28300', '1:28422', '1:30734', '1:30760', '1:30773', '1:30801', '1:30809', '1:30817', '1:30825', '1:30839', '1:30845', '1:30866', '1:31265', '1:31316', '1:31778', '1:31791', '1:29518', '1:29653', '1:29532', '1:29645', '1:29660', '1:50584', '1:50271', '1:50361', '1:50399', '1:50402', '1:50407', '1:50522', '1:50545', '1:50548', '1:50608', '1:50625', '1:54299', '1:54329', '1:54443', '1:54446', '1:54674', '1:74462', '1:78007', '1:78245', '1:59555', '1:74549', '1:6323', '1:6360', '1:8264', '1:8902', '1:9857', '1:10680', '1:17507', '1:17927', '1:29322', '1:29885', '1:36292', '1:13754', '1:21057', '1:29795', '1:26845', '1:26868', '1:26984', '1:29148', '1:21290', '1:26039', '1:26246', '1:26402', '1:26481', '1:26563', '1:26852', '1:26909', '1:26913', '1:26998', '1:25266', '1:25669', '1:25807', '1:42547', '1:44068', '1:47120', '1:43154', '1:47781', '1:43678', '1:45321', '1:25562', '1:26105', '1:25186', '1:25194', '1:25292', '1:25415', '1:25850', '1:26032', '1:26155', '1:26566', '1:26624', '1:29395', '1:29442', '1:29485', '1:29599', '1:29745', '1:29812', '1:36042', '1:36694', '1:38009', '1:38568', '1:42586', '1:42863', '1:44428', '1:44821', '1:44155', '1:44170', '1:44175', '1:44807', '1:48778', '1:43061', '1:43074', '1:43224', '1:43734', '1:44798', '1:44417', '1:48772', '1:50994', '1:52520', '1:62290', '1:62646', '1:55942', '1:67777', '1:67786', '1:68380', '1:68415', '1:69933', '1:48890', '1:96580', '1:97231', '1:98165', '1:96512', '1:97217', '1:98043', '1:101538', '1:101648', '1:79532', '1:79945', '1:80604', '1:80635', '1:42265', '1:42323', '1:41371', '1:41804', '1:41226', '1:42419', '1:13366', '1:13842', '1:14252', '1:14914', '1:15307', '1:15394', '1:16136', '1:17420', '1:17938', '1:56225', '1:57243', '1:55211', '1:62367', '1:62452', '1:49062', '1:59800', '1:51895', '1:53895', '1:58019', '1:63158', '1:50185', '1:50818', '1:57408', '1:61712', '1:61961', '1:62694', '1:67078', '1:43301', '1:43307', '1:43625', '1:45186', '1:48768', '1:45237', '1:45246', '1:45825', '1:48282', '1:48287', '1:44443', '1:43894', '1:44999', '1:65511', '1:45890', '1:45934', '1:45944', '1:123', '1:239', '1:20', '1:63', '1:83', '1:112', '1:125', '1:137', '1:157', '1:161', '1:168', '1:144', '1:556', '1:1744', '1:1752', '1:2577', '1:3004', '1:3784', '1:4505', '1:4789', '1:4911', '1:5054', '1:5170', '1:1387', '1:4298', '1:4300', '1:4301', '1:4330', '1:4437', '1:4464', '1:4575', '1:4314', '1:4332', '1:4355', '1:4653', '1:4667', '1:4675', '1:4695', '1:4704', '1:4708', '1:4707', '1:4731', '1:4732', '1:10931', '1:10955', '1:10996', '1:14041', '1:14366', '1:14380', '1:14438', '1:54049', '1:54176', '1:54541', '1:54700', '1:27367', '1:27385', '1:27473', '1:27530', '1:27693', '1:35838', '1:35912', '1:37450', '1:36596', '1:36642', '1:36662', '1:36722', '1:36763', '1:36752', '1:36885', '1:36912', '1:38670', '1:38689', '1:59416', '1:40398', '1:40399', '1:40400', '1:40633', '1:40914', '1:40959', '1:40643', '1:40712', '1:40808', '1:40809', '1:49588', '1:84999', '1:56565', '1:52934', '1:57409', '1:58470', '1:58632', '1:59588', '1:49826', '1:49843', '1:49929', '1:49947', '1:52323', '1:52606', '1:52713', '1:62567', '1:62588', '1:53390', '1:53398', '1:53422', '1:53500', '1:53503', '1:53560', '1:53615', '1:53622', '1:53640', '1:7806', '1:7953', '1:8037', '1:8553', '1:7865', '1:7935', '1:7955', '1:7985', '1:7995', '1:8012', '1:8197', '1:9057', '1:9104', '1:9143', '1:8119', '1:8121', '1:8129', '1:8504', '1:31770', '1:46349', '1:49689', '1:51186', '1:59284', '1:63342', '1:63538', '1:21013', '1:26247', '1:26407', '1:26827', '1:29901', '1:29933', '1:19714', '1:20675', '1:23043', '1:23055', '1:23083', '1:23049', '1:39018', '1:39497', '1:24114', '1:45411', '1:46124', '1:46150', '1:46165', '1:46179', '1:46213', '1:46232', '1:46328', '1:46361', '1:46376', '1:46351', '1:46748', '1:49009', '1:13378', '1:13403', '1:13437', '1:13524', '1:13662', '1:13667', '1:13309', '1:13519', '1:13567', '1:13622', '1:13623', '1:13641', '1:13642', '1:13650', '1:13788', '1:13946', '1:14060', '1:13704', '1:13967', '1:14594', '1:25055', '1:25064', '1:25142', '1:25158', '1:25174', '1:25525', '1:25577', '1:25909', '1:25951', '1:26553', '1:26937', '1:25495', '1:25507', '1:25546', '1:25621', '1:25626', '1:25658', '1:25666', '1:25678', '1:25752', '1:25763', '1:28553', '1:33358', '1:33362', '1:33371', '1:33393', '1:33396', '1:33442', '1:33446', '1:33458', '1:33812', '1:33863', '1:52983', '1:62581', '1:63227', '1:31612', '1:31624', '1:31888', '1:31916', '1:31976', '1:32046', '1:32870', '1:32878', '1:32030', '1:32136', '1:32139', '1:32208', '1:32329', '1:32566', '1:32568', '1:32662', '1:32694', '1:35840', '1:35849', '1:40656', '1:46526', '1:46687', '1:46799', '1:40811', '1:40814', '1:40816', '1:40969', '1:40977', '1:46074', '1:46161', '1:46168', '1:46176', '1:40858', '1:40871', '1:40896', '1:40978', '1:46107', '1:46123', '1:46132', '1:53288', '1:101533', '1:90191', '1:94660', '1:96469', '1:97889', '1:86073', '1:90632', '1:92424', '1:92425', '1:6267', '1:7419', '1:7544', '1:8719', '1:10335', '1:6008', '1:6989', '1:7187', '1:7381', '1:7594', '1:7756', '1:8407', '1:8858', '1:6300', '1:6802', '1:6803', '1:6940', '1:8090', '1:9738', '1:25189', '1:25416', '1:27355', '1:49417', '1:24081', '1:24092', '1:24203', '1:61469', '1:63636', '1:64157', '1:61457', '1:61478', '1:61502', '1:51414', '1:52295', '1:50006', '1:54465', '1:58010', '1:58420', '1:58576', '1:59984', '1:60484', '1:61203', '1:63113', '1:35042', '1:35310', '1:35489', '1:35643', '1:37045', '1:37273', '1:34872', '1:34899', '1:35060', '1:35079', '1:35136', '1:35143', '1:35235', '1:35257', '1:35306', '1:35328', '1:35347', '1:35426', '1:49163', '1:36915', '1:36971', '1:38269', '1:38287', '1:36998', '1:38262', '1:38535', '1:38543', '1:38017', '1:38095', '1:38328', '1:46098', '1:46201', '1:42756', '1:70035', '1:70096', '1:70197', '1:70434', '1:70447', '1:70455', '1:70468', '1:70200', '1:77725', '1:79421', '1:80416', '1:80711', '1:81540', '1:5032', '1:10986', '1:14655', '1:20732', '1:1755', '1:1756', '1:1806', '1:1848', '1:1888', '1:1953', '1:1814', '1:4568', '1:4616', '1:7705', '1:6011', '1:6113', '1:6746', '1:8009', '1:8112', '1:8210', '1:8251', '1:6073', '1:6453', '1:6945', '1:7513', '1:8398', '1:8624', '1:8841', '1:9188', '1:21516', '1:17924', '1:17926', '1:22272', '1:10275', '1:10839', '1:10847', '1:10423', '1:10699', '1:10845', '1:10853', '1:10933', '1:10943', '1:13011', '1:16404', '1:6095', '1:6500', '1:8035', '1:8563', '1:9558', '1:14132', '1:6096', '1:6183', '1:6442', '1:8196', '1:8683', '1:8824', '1:9454', '1:15535', '1:10821', '1:10769', '1:10800', '1:8006', '1:15042', '1:18660', '1:19353', '1:22809', '1:15478', '1:19742', '1:26833', '1:36266', '1:9422', '1:14211', '1:17120', '1:17490', '1:18967', '1:9736', '1:10257', '1:9229', '1:9278', '1:9334', '1:9335', '1:9369', '1:9400', '1:9409', '1:9395', '1:9451', '1:9776', '1:9841', '1:3321', '1:3349', '1:3378', '1:3387', '1:3389', '1:3391', '1:3405', '1:3417', '1:3835', '1:3849', '1:3273', '1:3295', '1:3306', '1:3311', '1:3579', '1:3770', '1:3989', '1:5581', '1:5667', '1:5870', '1:5872', '1:5248', '1:5508', '1:10478', '1:20466', '1:10084', '1:10702', '1:10914', '1:10998', '1:13034', '1:13105', '1:13169', '1:13220', '1:13277', '1:23102', '1:23112', '1:19492', '1:20998', '1:17656', '1:18154', '1:18210', '1:17112', '1:17258', '1:17531', '1:17693', '1:18513', '1:18577', '1:18585', '1:14825', '1:15331', '1:10685', '1:10690', '1:10749', '1:10927', '1:10960', '1:13068', '1:13607', '1:14014', '1:14043', '1:14112', '1:10671', '1:10688', '1:10906', '1:13102', '1:13110', '1:13281', '1:15839', '1:15988', '1:15998', '1:16101', '1:16499', '1:15860', '1:18004', '1:18141', '1:18269', '1:18474', '1:16030', '1:16128', '1:16185', '1:23295', '1:23290', '1:23419', '1:23494', '1:23533', '1:24107', '1:24698', '1:26629', '1:30485', '1:31322', '1:55940', '1:62609', '1:28039', '1:28055', '1:28067', '1:28070', '1:28111', '1:27532', '1:27557', '1:1106', '1:1497', '1:2107', '1:2460', '1:3276', '1:3481', '1:3806', '1:6929', '1:9622', '1:20376', '1:553', '1:2982', '1:3965', '1:29227', '1:32462', '1:46218', '1:46694', '1:23698', '1:23918', '1:35536', '1:49551', '1:49564', '1:51031', '1:51560', '1:53525', '1:23709', '1:23724', '1:23725', '1:23752', '1:23753', '1:23873', '1:40458', '1:59182', '1:60026', '1:60233', '1:59736', '1:60158', '1:61174', '1:3032', '1:3043', '1:3051', '1:3184', '1:3199', '1:3234', '1:3285', '1:5282', '1:6048', '1:6091', '1:6100', '1:6187', '1:6254', '1:6260', '1:6262', '1:6285', '1:6357', '1:6367', '1:6454', '1:6535', '1:6641', '1:3469', '1:5335', '1:5336', '1:5355', '1:5433', '1:5459', '1:6001', '1:6058', '1:6156', '1:6244', '1:6309', '1:6341', '1:6392', '1:6562', '1:6251', '1:7324', '1:7438', '1:7683', '1:7965', '1:8581', '1:9741', '1:10293', '1:10420', '1:14339', '1:9817', '1:10412', '1:9774', '1:9958', '1:9974', '1:16910', '1:16967', '1:18610', '1:27440', '1:60542', '1:76223', '1:76256', '1:23510', '1:23518', '1:23525', '1:23623', '1:23685', '1:23717', '1:23726', '1:23741', '1:23785', '1:23591', '1:23696', '1:23856', '1:25133', '1:23895', '1:23919', '1:34018', '1:36287', '1:23953', '1:23969', '1:23978', '1:27016', '1:28068', '1:28146', '1:28375', '1:28392', '1:87153', '1:57279', '1:57416', '1:57441', '1:57667', '1:57677', '1:57976', '1:58343', '1:58391', '1:57362', '1:57427', '1:57475', '1:57508', '1:57524', '1:57627', '1:57787', '1:101355', '1:10232', '1:10557', '1:10678', '1:10735', '1:13707', '1:14108', '1:14661', '1:15953', '1:18447', '1:19279', '1:19678', '1:19854', '1:21551', '1:10894', '1:36932', '1:36921', '1:38638', '1:39459', '1:39515', '1:39762', '1:39885', '1:39496', '1:39499', '1:39574', '1:39600', '1:39608', '1:39628', '1:39636', '1:39644', '1:39690', '1:39691', '1:49220', '1:49244', '1:49260', '1:49264', '1:49268', '1:49397', '1:49402', '1:49221', '1:23475', '1:23679', '1:27405', '1:30400', '1:30652', '1:34215', '1:23968', '1:25270', '1:25346', '1:27152', '1:27201', '1:26195', '1:26215', '1:26139', '1:26156', '1:26177', '1:37214', '1:35899', '1:36854', '1:37009', '1:37050', '1:37083', '1:37106', '1:37128', '1:37358', '1:37363', '1:37513', '1:37545', '1:35879', '1:35984', '1:37020', '1:56103', '1:56338', '1:56967', '1:56288', '1:36924', '1:36935', '1:38913', '1:56366', '1:56415', '1:56432', '1:56860', '1:56995', '1:26110', '1:26241', '1:26315', '1:26373', '1:26384', '1:26445', '1:26258', '1:26269', '1:26289', '1:26291', '1:26326', '1:38713', '1:38827', '1:38659', '1:38688', '1:38786', '1:28846', '1:28903', '1:28911', '1:28925', '1:31058', '1:31077', '1:31124', '1:31224', '1:31286', '1:29389', '1:29470', '1:29584', '1:29609', '1:29682', '1:29744', '1:29759', '1:29824', '1:49169', '1:86755', '1:88320', '1:89639', '1:90185', '1:86713', '1:96989', '1:97957', '1:100163', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/F8F7873D-FB17-EA11-AA6D-5065F3816251.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B6601206-7817-EA11-9917-B8CA3A70B608.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/7C989971-6D18-EA11-B717-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/EEEA473E-5B18-EA11-AC30-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8A2118DF-4E18-EA11-9797-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/542AEF48-3618-EA11-A4A0-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/00C3247C-0B18-EA11-A4D7-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/76F4BCBD-FD17-EA11-8346-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8D8F6E4-1718-EA11-BA45-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/56C0C349-3C18-EA11-8185-0242AC130002.root']);