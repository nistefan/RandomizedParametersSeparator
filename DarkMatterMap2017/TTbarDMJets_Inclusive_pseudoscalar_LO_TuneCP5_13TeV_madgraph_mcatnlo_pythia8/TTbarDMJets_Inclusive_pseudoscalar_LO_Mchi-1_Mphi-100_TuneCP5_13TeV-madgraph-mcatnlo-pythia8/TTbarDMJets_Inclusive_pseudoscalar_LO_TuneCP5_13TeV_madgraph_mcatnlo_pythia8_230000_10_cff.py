import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:14769', '1:14864', '1:14942', '1:15013', '1:15039', '1:15078', '1:15157', '1:15240', '1:15315', '1:15380', '1:15415', '1:15504', '1:88318', '1:98292', '1:91218', '1:91833', '1:92173', '1:94303', '1:95567', '1:97061', '1:96653', '1:97830', '1:98164', '1:98181', '1:98759', '1:51913', '1:53380', '1:64958', '1:65055', '1:66085', '1:66098', '1:71480', '1:71488', '1:71731', '1:71733', '1:72461', '1:17023', '1:23364', '1:23547', '1:24365', '1:47335', '1:47350', '1:17573', '1:18157', '1:27087', '1:27252', '1:27891', '1:28559', '1:28932', '1:19211', '1:24833', '1:24963', '1:17948', '1:17958', '1:17992', '1:17996', '1:19069', '1:19159', '1:19166', '1:19244', '1:19456', '1:19465', '1:19496', '1:102779', '1:43096', '1:43083', '1:43147', '1:42955', '1:44487', '1:87946', '1:88836', '1:64207', '1:66175', '1:62418', '1:65369', '1:71693', '1:71885', '1:72486', '1:72811', '1:64865', '1:67296', '1:67361', '1:67555', '1:67897', '1:71226', '1:71379', '1:72281', '1:72906', '1:73276', '1:73591', '1:71728', '1:77031', '1:78044', '1:88843', '1:83237', '1:83371', '1:83459', '1:83869', '1:84258', '1:17226', '1:17236', '1:19401', '1:19795', '1:22436', '1:22821', '1:29181', '1:44618', '1:44970', '1:47043', '1:47591', '1:44445', '1:45336', '1:47032', '1:47125', '1:47880', '1:52472', '1:65783', '1:62417', '1:72344', '1:76641', '1:73351', '1:74082', '1:74126', '1:74408', '1:74564', '1:72266', '1:78665', '1:79579', '1:79627', '1:80440', '1:72449', '1:71365', '1:74681', '1:80408', '1:64533', '1:66859', '1:67842', '1:71979', '1:72068', '1:73923', '1:79149', '1:80660', '1:19705', '1:19824', '1:20336', '1:20344', '1:20380', '1:20414', '1:20471', '1:20487', '1:20523', '1:20550', '1:20610', '1:20640', '1:20671', '1:20753', '1:20790', '1:54404', '1:24781', '1:24934', '1:25000', '1:25592', '1:25639', '1:25668', '1:25723', '1:25732', '1:25736', '1:25742', '1:25770', '1:25844', '1:25852', '1:43905', '1:48256', '1:47421', '1:47497', '1:47636', '1:70160', '1:70324', '1:84744', '1:85300', '1:89522', '1:89849', '1:70560', '1:83090', '1:84239', '1:64927', '1:66656', '1:67158', '1:73372', '1:76602', '1:76864', '1:80381', '1:65423', '1:70576', '1:71447', '1:74501', '1:74633', '1:77148', '1:77273', '1:89728', '1:94466', '1:96774', '1:70143', '1:72417', '1:75355', '1:82960', '1:83011', '1:83098', '1:83188', '1:83433', '1:83565', '1:77268', '1:83538', '1:82563', '1:85457', '1:88761', '1:65035', '1:66327', '1:72644', '1:75840', '1:78579', '1:70814', '1:84878', '1:91526', '1:94547', '1:83587', '1:2887', '1:5605', '1:9667', '1:13823', '1:14421', '1:20019', '1:20133', '1:20606', '1:21026', '1:21547', '1:23354', '1:23994', '1:26666', '1:64695', '1:65944', '1:67542', '1:81538', '1:93574', '1:4326', '1:5220', '1:7087', '1:7931', '1:14057', '1:7784', '1:9961', '1:11505', '1:11833', '1:13263', '1:101206', '1:101308', '1:101557', '1:102218', '1:102671', '1:102907', '1:64404', '1:64770', '1:65457', '1:65559', '1:65571', '1:65792', '1:66318', '1:66950', '1:71607', '1:72074', '1:58498', '1:47896', '1:47910', '1:17925', '1:18087', '1:18121', '1:18162', '1:18176', '1:18325', '1:18378', '1:18421', '1:18572', '1:18073', '1:18200', '1:45827', '1:45956', '1:28792', '1:30116', '1:30262', '1:39953', '1:44107', '1:28833', '1:30171', '1:39513', '1:42774', '1:42903', '1:47089', '1:89771', '1:25011', '1:25154', '1:25234', '1:25362', '1:25373', '1:25503', '1:42887', '1:43010', '1:42884', '1:4104', '1:5445', '1:8229', '1:9034', '1:1369', '1:7698', '1:7730', '1:14518', '1:19497', '1:18911', '1:27758', '1:29666', '1:42086', '1:70694', '1:77133', '1:81649', '1:98627', '1:98879', '1:82516', '1:83201', '1:83348', '1:83858', '1:83890', '1:96131', '1:96898', '1:92105', '1:92200', '1:92215', '1:92615', '1:92684', '1:92704', '1:93189', '1:91598', '1:91601', '1:91850', '1:47286', '1:47307', '1:47436', '1:47468', '1:47623', '1:47625', '1:47631', '1:47708', '1:47752', '1:47882', '1:47906', '1:47972', '1:47588', '1:47654', '1:47784', '1:47825', '1:47865', '1:47912', '1:47946', '1:48392', '1:66165', '1:71284', '1:71795', '1:72008', '1:67774', '1:73301', '1:74556', '1:75188', '1:75953', '1:81300', '1:81463', '1:84371', '1:84766', '1:85039', '1:85268', '1:85813', '1:85915', '1:85980', '1:86706', '1:87086', '1:87622', '1:85890', '1:51578', '1:52040', '1:52112', '1:52125', '1:52170', '1:52193', '1:52196', '1:52201', '1:52283', '1:52287', '1:52293', '1:52322', '1:52389', '1:52438', '1:66657', '1:70022', '1:70046', '1:70170', '1:70200', '1:70219', '1:70462', '1:64890', '1:65191', '1:65318', '1:65545', '1:65774', '1:65861', '1:65973', '1:102336', '1:102495', '1:22327', '1:22369', '1:22594', '1:23727', '1:27747', '1:30335', '1:30512', '1:32992', '1:44145', '1:47065', '1:29284', '1:39251', '1:39713', '1:39965', '1:47317', '1:47487', '1:47661', '1:47737', '1:46507', '1:49180', '1:103697', '1:105409', '1:105465', '1:105825', '1:98107', '1:98779', '1:102971', '1:104003', '1:104030', '1:104099', '1:104602', '1:106169', '1:91212', '1:88251', '1:88321', '1:88487', '1:88791', '1:89238', '1:89241', '1:89255', '1:89472', '1:89605', '1:91108', '1:88305', '1:88306', '1:88379', '1:89369', '1:27711', '1:47739', '1:27815', '1:28346', '1:32051', '1:45856', '1:96833', '1:97646', '1:98630', '1:105027', '1:105841', '1:105849', '1:90428', '1:96161', '1:105116', '1:92410', '1:106225', '1:105222', '1:105441', '1:106154', '1:101272', '1:101330', '1:101591', '1:101842', '1:101947', '1:105665', '1:5490', '1:5627', '1:5296', '1:5319', '1:5414', '1:5424', '1:5864', '1:5902', '1:5944', '1:6080', '1:6578', '1:6841', '1:6955', '1:10756', '1:10496', '1:7133', '1:7160', '1:7670', '1:7323', '1:7361', '1:7423', '1:7479', '1:7511', '1:7590', '1:7661', '1:7704', '1:7811', '1:7915', '1:7993', '1:8131', '1:46722', '1:31323', '1:78436', '1:81753', '1:84833', '1:91022', '1:95615', '1:62658', '1:20326', '1:20476', '1:20541', '1:20572', '1:20690', '1:20712', '1:81722', '1:81853', '1:81909', '1:81989', '1:26220', '1:24868', '1:25489', '1:75130', '1:79682', '1:103037', '1:106223', '1:98802', '1:102521', '1:104829', '1:102617', '1:104354', '1:104706', '1:104053', '1:104187', '1:104211', '1:104280', '1:104312', '1:104416', '1:104421', '1:30548', '1:42231', '1:51583', '1:52836', '1:57581', '1:61671', '1:29174', '1:29946', '1:51701', '1:51710', '1:51782', '1:51935', '1:52251', '1:52292', '1:53111', '1:53629', '1:61424', '1:62439', '1:62536', '1:62788', '1:62802', '1:62804', '1:5355', '1:6122', '1:5470', '1:5535', '1:5551', '1:5557', '1:5567', '1:5720', '1:5825', '1:5948', '1:10368', '1:9617', '1:9658', '1:9674', '1:9812', '1:9935', '1:10029', '1:10044', '1:10110', '1:9739', '1:9819', '1:9950', '1:10052', '1:10182', '1:11615', '1:11752', '1:12400', '1:12068', '1:12716', '1:13851', '1:14376', '1:14660', '1:15533', '1:15540', '1:13601', '1:14772', '1:14894', '1:7262', '1:7407', '1:7530', '1:7538', '1:7634', '1:8425', '1:9426', '1:9981', '1:9593', '1:9706', '1:9707', '1:10223', '1:10336', '1:14450', '1:15370', '1:15434', '1:15573', '1:15661', '1:15686', '1:15702', '1:15710', '1:15815', '1:15832', '1:16382', '1:16424', '1:16463', '1:16813', '1:13673', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C75EAD7-A60A-EA11-B2EA-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CAA33E3-B40A-EA11-B217-0CC47A4C8EB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0C7BD80-B30A-EA11-990C-0CC47A7C345E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/827A94E9-460C-EA11-9197-0CC47A7C34D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C25D68E-CA0A-EA11-A4D3-0CC47A4D762E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4F23B9-260F-EA11-80C3-0CC47A4D7690.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A38857F-43F9-E911-9334-0CC47A5FBE21.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2A529D76-BC12-EA11-85B1-90B11C070100.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80404779-FBF6-E911-8982-AC1F6B0F71D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A13F5EF-28F2-E911-9B0D-00215AA64960.root']);