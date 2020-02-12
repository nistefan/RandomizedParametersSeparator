import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:10043', '1:16814', '1:25996', '1:26104', '1:26989', '1:33085', '1:33099', '1:33116', '1:33267', '1:33913', '1:33925', '1:9537', '1:9603', '1:9640', '1:9898', '1:10006', '1:10178', '1:10262', '1:10330', '1:10429', '1:13310', '1:13402', '1:13420', '1:13534', '1:13639', '1:13664', '1:14192', '1:14250', '1:13236', '1:14087', '1:14692', '1:14859', '1:15718', '1:16260', '1:17857', '1:13702', '1:62217', '1:15031', '1:15453', '1:15519', '1:15551', '1:15468', '1:15474', '1:15504', '1:16048', '1:16061', '1:15404', '1:15623', '1:14777', '1:14783', '1:15247', '1:15709', '1:15766', '1:15871', '1:20598', '1:20435', '1:20456', '1:20465', '1:20555', '1:20621', '1:20670', '1:20945', '1:20891', '1:20900', '1:21031', '1:21386', '1:21408', '1:21543', '1:39431', '1:39443', '1:27742', '1:27885', '1:27901', '1:27994', '1:28129', '1:28510', '1:28535', '1:28664', '1:28730', '1:28917', '1:28057', '1:28187', '1:28291', '1:28301', '1:28308', '1:28317', '1:28332', '1:30739', '1:30751', '1:30777', '1:30821', '1:30846', '1:30847', '1:31276', '1:31314', '1:31332', '1:31800', '1:31841', '1:29513', '1:29521', '1:29526', '1:29530', '1:29552', '1:29636', '1:29650', '1:29665', '1:29681', '1:29528', '1:50570', '1:50154', '1:50286', '1:50289', '1:54293', '1:54786', '1:54795', '1:54807', '1:76288', '1:78896', '1:78593', '1:7631', '1:8019', '1:8805', '1:13247', '1:13781', '1:14756', '1:15646', '1:16024', '1:21535', '1:26668', '1:33958', '1:26773', '1:26787', '1:29837', '1:36495', '1:21087', '1:26619', '1:29662', '1:21015', '1:26451', '1:26530', '1:26749', '1:26933', '1:29101', '1:16961', '1:25022', '1:25286', '1:25575', '1:25833', '1:12820', '1:41672', '1:47683', '1:43182', '1:44575', '1:44750', '1:43691', '1:43814', '1:45266', '1:48318', '1:26064', '1:29150', '1:25585', '1:25681', '1:16248', '1:25356', '1:25374', '1:25623', '1:25696', '1:25907', '1:25913', '1:29077', '1:29499', '1:33338', '1:33547', '1:36051', '1:36353', '1:36415', '1:38205', '1:42474', '1:42585', '1:42846', '1:43027', '1:44790', '1:44813', '1:44835', '1:44144', '1:47547', '1:47679', '1:47830', '1:43212', '1:43309', '1:43736', '1:44804', '1:44805', '1:44986', '1:50436', '1:55626', '1:55754', '1:55961', '1:62278', '1:62342', '1:64241', '1:52432', '1:54072', '1:62257', '1:64165', '1:69105', '1:69958', '1:58880', '1:48893', '1:98060', '1:98076', '1:98585', '1:98773', '1:96628', '1:101161', '1:79533', '1:79898', '1:80094', '1:80653', '1:80661', '1:81795', '1:42260', '1:41772', '1:41779', '1:41793', '1:41830', '1:41355', '1:41376', '1:14367', '1:15915', '1:15976', '1:16095', '1:16581', '1:17979', '1:19619', '1:58728', '1:54711', '1:62933', '1:46246', '1:51928', '1:53852', '1:58011', '1:58573', '1:59146', '1:52156', '1:63565', '1:62163', '1:44475', '1:48773', '1:43614', '1:43746', '1:43886', '1:45238', '1:45832', '1:45848', '1:45851', '1:45853', '1:44444', '1:44447', '1:44452', '1:44474', '1:44477', '1:44480', '1:65512', '1:45402', '1:363', '1:19', '1:30', '1:69', '1:71', '1:87', '1:99', '1:102', '1:109', '1:143', '1:147', '1:150', '1:162', '1:16', '1:1618', '1:3398', '1:3995', '1:4797', '1:4828', '1:5517', '1:1282', '1:1284', '1:4091', '1:4532', '1:4554', '1:4343', '1:4383', '1:4399', '1:4730', '1:4751', '1:4729', '1:5151', '1:5171', '1:10508', '1:10809', '1:10850', '1:10965', '1:10971', '1:14340', '1:14448', '1:14454', '1:27652', '1:54087', '1:54567', '1:54616', '1:27497', '1:27641', '1:35919', '1:35923', '1:35928', '1:35936', '1:37327', '1:37369', '1:36600', '1:36614', '1:36618', '1:36644', '1:36687', '1:36716', '1:36726', '1:36757', '1:36772', '1:36839', '1:36855', '1:36872', '1:36878', '1:38564', '1:40496', '1:40635', '1:40659', '1:40763', '1:40779', '1:40425', '1:40534', '1:40639', '1:40663', '1:40676', '1:40678', '1:40684', '1:40717', '1:40735', '1:40776', '1:40765', '1:46485', '1:46486', '1:84998', '1:49379', '1:55909', '1:61166', '1:50931', '1:52844', '1:57562', '1:58021', '1:58108', '1:58122', '1:58480', '1:60538', '1:49841', '1:50733', '1:52842', '1:52721', '1:53800', '1:55891', '1:55948', '1:62026', '1:64096', '1:68042', '1:69971', '1:53365', '1:53373', '1:53396', '1:53399', '1:53458', '1:53486', '1:53508', '1:53517', '1:53526', '1:53551', '1:53591', '1:53599', '1:7785', '1:7799', '1:7800', '1:8093', '1:8562', '1:7857', '1:7864', '1:7874', '1:8448', '1:8594', '1:8758', '1:8878', '1:8911', '1:9137', '1:7956', '1:8194', '1:8211', '1:8446', '1:8462', '1:31756', '1:32261', '1:31466', '1:33020', '1:51740', '1:51894', '1:57418', '1:59792', '1:60450', '1:17854', '1:26589', '1:29435', '1:29817', '1:38741', '1:19342', '1:40372', '1:24098', '1:43568', '1:43773', '1:45644', '1:46135', '1:46173', '1:46182', '1:46320', '1:46330', '1:46108', '1:46247', '1:46878', '1:13245', '1:13273', '1:13400', '1:13555', '1:13676', '1:13529', '1:13574', '1:13666', '1:13762', '1:13956', '1:14029', '1:14052', '1:14069', '1:13584', '1:13706', '1:14484', '1:25458', '1:25936', '1:25942', '1:25953', '1:25955', '1:25982', '1:26307', '1:25532', '1:25627', '1:25727', '1:25762', '1:28420', '1:28555', '1:28684', '1:49207', '1:49155', '1:33386', '1:33397', '1:33408', '1:33428', '1:33435', '1:33444', '1:33443', '1:33453', '1:33815', '1:40968', '1:46081', '1:55165', '1:61822', '1:31610', '1:31677', '1:31734', '1:31905', '1:31908', '1:31932', '1:31969', '1:32187', '1:32220', '1:32758', '1:32975', '1:33406', '1:32055', '1:32058', '1:32088', '1:32137', '1:32412', '1:32545', '1:35367', '1:49091', '1:49329', '1:40726', '1:40798', '1:40835', '1:40903', '1:40923', '1:40947', '1:40954', '1:46071', '1:46082', '1:40856', '1:40857', '1:46245', '1:46261', '1:46342', '1:62001', '1:62009', '1:62503', '1:67612', '1:90386', '1:98591', '1:99225', '1:85901', '1:99456', '1:84379', '1:84521', '1:92428', '1:92465', '1:92468', '1:6003', '1:7121', '1:7763', '1:9342', '1:9943', '1:10494', '1:6114', '1:6211', '1:6397', '1:6625', '1:7310', '1:7740', '1:8220', '1:8420', '1:8561', '1:8761', '1:8787', '1:6421', '1:8026', '1:8106', '1:9218', '1:9220', '1:23930', '1:25796', '1:27120', '1:27339', '1:24497', '1:24630', '1:60801', '1:61828', '1:61061', '1:61062', '1:61091', '1:61185', '1:61233', '1:61320', '1:61322', '1:61358', '1:61481', '1:61588', '1:49754', '1:54004', '1:61242', '1:63206', '1:34897', '1:35025', '1:35027', '1:35261', '1:35521', '1:35625', '1:34875', '1:35037', '1:35065', '1:35144', '1:35243', '1:35413', '1:49162', '1:49165', '1:36943', '1:36968', '1:36977', '1:36987', '1:36991', '1:38079', '1:38209', '1:38241', '1:38270', '1:38273', '1:36959', '1:38021', '1:38184', '1:38228', '1:38237', '1:38373', '1:38530', '1:38546', '1:36995', '1:38034', '1:38046', '1:38216', '1:38359', '1:38542', '1:38658', '1:46148', '1:46167', '1:41729', '1:70234', '1:70460', '1:79808', '1:85150', '1:6661', '1:7815', '1:18085', '1:18288', '1:1759', '1:1775', '1:1783', '1:1788', '1:1807', '1:1872', '1:1879', '1:1901', '1:1912', '1:1913', '1:1944', '1:1948', '1:1958', '1:5037', '1:5724', '1:6089', '1:6844', '1:7009', '1:7624', '1:7988', '1:8122', '1:8160', '1:6294', '1:6391', '1:6448', '1:6534', '1:6681', '1:6787', '1:7302', '1:8487', '1:8925', '1:8956', '1:9604', '1:26775', '1:31746', '1:10415', '1:10866', '1:10879', '1:15899', '1:15964', '1:6257', '1:8133', '1:8166', '1:8701', '1:9972', '1:10632', '1:10816', '1:14033', '1:6315', '1:6549', '1:6686', '1:6687', '1:6879', '1:8449', '1:8473', '1:8895', '1:8928', '1:7177', '1:8192', '1:8962', '1:13825', '1:10796', '1:7122', '1:7510', '1:8243', '1:9659', '1:17480', '1:20039', '1:7228', '1:17372', '1:19968', '1:26622', '1:26711', '1:26849', '1:36047', '1:8985', '1:9526', '1:14650', '1:17701', '1:18774', '1:20102', '1:6690', '1:9610', '1:9751', '1:9768', '1:9730', '1:9237', '1:9260', '1:9440', '1:9381', '1:9388', '1:9418', '1:10253', '1:23044', '1:23052', '1:3293', '1:3327', '1:3364', '1:3444', '1:3477', '1:3574', '1:3845', '1:3624', '1:3632', '1:5534', '1:5570', '1:5602', '1:5742', '1:5914', '1:3713', '1:5377', '1:20321', '1:9863', '1:10009', '1:10115', '1:10278', '1:10285', '1:10961', '1:13129', '1:13180', '1:16256', '1:23218', '1:23219', '1:23224', '1:23226', '1:23243', '1:19983', '1:16685', '1:16716', '1:16854', '1:18080', '1:18131', '1:17216', '1:18522', '1:18588', '1:17169', '1:15347', '1:10637', '1:10683', '1:10706', '1:10718', '1:10886', '1:13470', '1:14077', '1:10712', '1:13119', '1:13240', '1:13263', '1:13280', '1:16362', '1:16451', '1:16473', '1:16489', '1:15767', '1:15924', '1:18012', '1:18059', '1:18108', '1:18126', '1:18189', '1:15914', '1:16004', '1:16133', '1:16297', '1:16368', '1:16784', '1:23418', '1:23429', '1:23444', '1:23474', '1:23574', '1:23589', '1:23606', '1:23652', '1:26201', '1:27467', '1:31290', '1:31587', '1:50444', '1:39951', '1:27638', '1:28050', '1:28071', '1:28088', '1:28103', '1:28124', '1:28151', '1:27526', '1:27544', '1:27548', '1:27589', '1:27609', '1:1383', '1:1772', '1:4223', '1:5081', '1:1635', '1:2253', '1:4093', '1:6742', '1:7630', '1:10323', '1:20992', '1:418', '1:2506', '1:5333', '1:35282', '1:40955', '1:46463', '1:46815', '1:49130', '1:49235', '1:51048', '1:51129', '1:53291', '1:53756', '1:23712', '1:23729', '1:23766', '1:23768', '1:23842', '1:23862', '1:23890', '1:40451', '1:59069', '1:59132', '1:59424', '1:59439', '1:59586', '1:59708', '1:60079', '1:60111', '1:60519', '1:60536', '1:60626', '1:60984', '1:61093', '1:61159', '1:61201', '1:61224', '1:61238', '1:3035', '1:3037', '1:3041', '1:3157', '1:3167', '1:3182', '1:3198', '1:6002', '1:6019', '1:6123', '1:6238', '1:6270', '1:6311', '1:6356', '1:6400', '1:6440', '1:6462', '1:6472', '1:6513', '1:6569', '1:3604', '1:3611', '1:3718', '1:4117', '1:70275', '1:5416', '1:5485', '1:6074', '1:6124', '1:6154', '1:6181', '1:6464', '1:6552', '1:6600', '1:6610', '1:6648', '1:6708', '1:6284', '1:8363', '1:13829', '1:10282', '1:9825', '1:9880', '1:10039', '1:10543', '1:16926', '1:16932', '1:17410', '1:40181', '1:53813', '1:53930', '1:59788', '1:23523', '1:23551', '1:23615', '1:23632', '1:23653', '1:23656', '1:23760', '1:23761', '1:23773', '1:23688', '1:23703', '1:23818', '1:23959', '1:26360', '1:29430', '1:33599', '1:34010', '1:32204', '1:33235', '1:33490', '1:38382', '1:23994', '1:23995', '1:27070', '1:27094', '1:27105', '1:28013', '1:28279', '1:28354', '1:28368', '1:88311', '1:99426', '1:57417', '1:57449', '1:57465', '1:57529', '1:57553', '1:57717', '1:58002', '1:58180', '1:58237', '1:58318', '1:58334', '1:57370', '1:57395', '1:57443', '1:57445', '1:57557', '1:57571', '1:57648', '1:57698', '1:57827', '1:57828', '1:92431', '1:10177', '1:10306', '1:10362', '1:10427', '1:10559', '1:10592', '1:10728', '1:10745', '1:10811', '1:10840', '1:14141', '1:14902', '1:14944', '1:15464', '1:17333', '1:18915', '1:20843', '1:10506', '1:10905', '1:36928', '1:38451', '1:38605', '1:38624', '1:38639', '1:38640', '1:38749', '1:38758', '1:39597', '1:39750', '1:39448', '1:39457', '1:39511', '1:39555', '1:39569', '1:39582', '1:39602', '1:39667', '1:49215', '1:49309', '1:49332', '1:49357', '1:49406', '1:49422', '1:49212', '1:49261', '1:49278', '1:49304', '1:49307', '1:49334', '1:49364', '1:49388', '1:49428', '1:49440', '1:23541', '1:23549', '1:23670', '1:23781', '1:23904', '1:27444', '1:28100', '1:23938', '1:23980', '1:23987', '1:23992', '1:25222', '1:25352', '1:25489', '1:27010', '1:27155', '1:27229', '1:26125', '1:26189', '1:26196', '1:26151', '1:26166', '1:26168', '1:35824', '1:37204', '1:37277', '1:37286', '1:35794', '1:37226', '1:37266', '1:37318', '1:37437', '1:35862', '1:35873', '1:35980', '1:37121', '1:53665', '1:53792', '1:53919', '1:56083', '1:56999', '1:57106', '1:36911', '1:36898', '1:56421', '1:56431', '1:56499', '1:56529', '1:56836', '1:56941', '1:56982', '1:56987', '1:57009', '1:57104', '1:26107', '1:26234', '1:26261', '1:26429', '1:26457', '1:26471', '1:26545', '1:26248', '1:26284', '1:26303', '1:26312', '1:26321', '1:26378', '1:38697', '1:38802', '1:38818', '1:38914', '1:38920', '1:28845', '1:28854', '1:28894', '1:28959', '1:28995', '1:30295', '1:31293', '1:29415', '1:29488', '1:29519', '1:29607', '1:29647', '1:29669', '1:29685', '1:29742', '1:29749', '1:29766', '1:29810', '1:29816', '1:29873', '1:29945', '1:50039', '1:55117', '1:57653', '1:85082', '1:85667', '1:91684', '1:91783', '1:79414', '1:98100', '1:99860', '1:100568', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/F8F7873D-FB17-EA11-AA6D-5065F3816251.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B6601206-7817-EA11-9917-B8CA3A70B608.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/7C989971-6D18-EA11-B717-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/EEEA473E-5B18-EA11-AC30-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8A2118DF-4E18-EA11-9797-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/542AEF48-3618-EA11-A4A0-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/00C3247C-0B18-EA11-A4D7-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/76F4BCBD-FD17-EA11-8346-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8D8F6E4-1718-EA11-BA45-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/56C0C349-3C18-EA11-8185-0242AC130002.root']);