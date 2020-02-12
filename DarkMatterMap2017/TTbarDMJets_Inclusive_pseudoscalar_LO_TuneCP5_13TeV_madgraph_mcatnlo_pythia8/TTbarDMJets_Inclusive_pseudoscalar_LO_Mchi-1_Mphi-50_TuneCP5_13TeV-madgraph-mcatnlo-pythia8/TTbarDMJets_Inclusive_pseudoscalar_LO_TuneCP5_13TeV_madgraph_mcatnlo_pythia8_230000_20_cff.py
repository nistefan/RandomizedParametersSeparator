import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:29172', '1:29310', '1:29553', '1:29624', '1:29674', '1:29728', '1:29770', '1:29788', '1:29899', '1:29317', '1:29560', '1:29894', '1:30496', '1:49925', '1:72419', '1:73180', '1:73456', '1:72473', '1:72539', '1:72660', '1:72667', '1:72678', '1:72693', '1:72872', '1:72910', '1:72935', '1:72975', '1:77095', '1:77354', '1:77452', '1:77575', '1:84106', '1:84754', '1:88852', '1:97056', '1:97196', '1:97348', '1:72828', '1:73297', '1:73043', '1:73046', '1:73168', '1:73199', '1:73279', '1:73290', '1:76382', '1:76400', '1:76413', '1:76653', '1:76678', '1:76702', '1:76782', '1:76877', '1:76886', '1:76915', '1:76972', '1:78313', '1:78341', '1:78470', '1:78678', '1:78723', '1:7493', '1:10961', '1:11943', '1:12766', '1:14904', '1:6740', '1:8760', '1:9678', '1:44318', '1:45337', '1:45693', '1:55801', '1:64174', '1:72788', '1:75447', '1:48209', '1:48217', '1:48746', '1:49224', '1:49483', '1:48641', '1:48796', '1:48881', '1:48941', '1:49978', '1:53424', '1:55457', '1:56195', '1:56470', '1:56649', '1:57102', '1:58406', '1:71915', '1:94846', '1:91985', '1:101352', '1:102614', '1:102760', '1:98783', '1:104432', '1:104681', '1:102343', '1:104284', '1:1398', '1:1911', '1:2171', '1:2213', '1:2238', '1:2425', '1:2635', '1:2668', '1:2004', '1:2366', '1:2367', '1:2390', '1:2433', '1:2434', '1:2527', '1:15723', '1:16162', '1:16164', '1:16294', '1:16399', '1:16460', '1:16577', '1:16642', '1:16667', '1:16696', '1:23126', '1:23174', '1:23184', '1:23194', '1:23318', '1:23448', '1:23449', '1:17066', '1:17071', '1:17441', '1:17482', '1:17539', '1:17040', '1:17224', '1:17284', '1:17292', '1:27903', '1:28097', '1:28283', '1:28352', '1:28659', '1:28996', '1:28057', '1:28064', '1:28076', '1:28081', '1:28138', '1:28197', '1:28219', '1:28277', '1:28333', '1:28335', '1:28569', '1:29478', '1:29536', '1:29642', '1:29715', '1:29722', '1:29737', '1:29786', '1:29802', '1:29811', '1:29839', '1:29909', '1:30136', '1:53078', '1:47537', '1:47580', '1:47678', '1:47789', '1:62631', '1:62728', '1:62752', '1:42750', '1:42970', '1:42977', '1:43112', '1:43123', '1:44960', '1:45154', '1:45483', '1:45551', '1:45921', '1:47060', '1:47219', '1:47238', '1:47543', '1:47665', '1:83574', '1:85692', '1:88106', '1:88681', '1:89287', '1:90922', '1:91087', '1:91316', '1:91690', '1:91695', '1:92447', '1:92860', '1:93009', '1:93357', '1:88857', '1:90045', '1:91822', '1:92058', '1:90634', '1:92292', '1:94214', '1:93320', '1:95107', '1:98838', '1:47340', '1:47933', '1:82158', '1:82391', '1:80745', '1:81959', '1:82316', '1:85782', '1:98217', '1:98470', '1:98713', '1:81126', '1:81266', '1:81782', '1:98139', '1:98172', '1:98504', '1:98512', '1:98544', '1:98565', '1:98675', '1:98878', '1:98919', '1:104262', '1:104360', '1:6986', '1:8646', '1:8872', '1:12469', '1:14866', '1:7780', '1:8797', '1:9016', '1:12467', '1:14126', '1:15564', '1:40307', '1:43382', '1:45305', '1:46915', '1:46992', '1:46994', '1:48034', '1:48366', '1:49134', '1:49351', '1:59720', '1:28074', '1:28098', '1:28722', '1:29499', '1:29725', '1:30134', '1:30632', '1:32409', '1:32867', '1:42513', '1:42545', '1:30728', '1:61697', '1:42858', '1:47877', '1:59298', '1:60905', '1:49439', '1:49856', '1:49867', '1:51282', '1:52189', '1:54040', '1:54193', '1:51613', '1:52272', '1:52361', '1:52639', '1:56793', '1:57447', '1:93968', '1:93991', '1:97189', '1:98209', '1:80349', '1:80410', '1:80924', '1:72809', '1:65005', '1:66407', '1:73117', '1:82452', '1:96641', '1:98126', '1:98127', '1:103401', '1:103723', '1:105068', '1:105685', '1:103869', '1:103885', '1:105742', '1:105989', '1:103682', '1:6113', '1:11941', '1:15252', '1:16465', '1:5471', '1:9532', '1:11513', '1:15401', '1:6060', '1:8210', '1:12549', '1:16535', '1:7980', '1:17641', '1:18049', '1:18584', '1:19610', '1:20084', '1:27155', '1:28316', '1:28677', '1:28686', '1:29944', '1:30641', '1:31591', '1:32443', '1:42206', '1:42409', '1:44347', '1:44801', '1:58838', '1:77867', '1:79123', '1:79684', '1:79943', '1:81418', '1:82075', '1:82204', '1:84262', '1:85795', '1:78049', '1:83317', '1:84027', '1:25044', '1:44442', '1:28870', '1:43629', '1:43822', '1:46591', '1:48759', '1:49952', '1:56789', '1:43565', '1:48058', '1:52299', '1:55951', '1:56082', '1:58307', '1:58590', '1:84470', '1:88386', '1:88750', '1:89423', '1:89473', '1:89571', '1:89637', '1:90261', '1:90688', '1:90951', '1:93284', '1:93977', '1:90576', '1:91342', '1:91530', '1:92172', '1:103692', '1:103724', '1:103768', '1:105007', '1:105100', '1:105152', '1:105277', '1:105163', '1:105800', '1:106007', '1:106112', '1:89770', '1:89808', '1:92064', '1:92518', '1:95500', '1:96119', '1:96381', '1:96890', '1:89932', '1:96265', '1:72722', '1:74197', '1:74489', '1:75374', '1:75754', '1:76666', '1:91733', '1:98391', '1:105596', '1:105083', '1:102260', '1:102332', '1:102492', '1:102604', '1:101487', '1:103137', '1:103787', '1:103795', '1:103897', '1:105396', '1:105702', '1:106435', '1:106284', '1:22268', '1:22310', '1:22380', '1:22382', '1:22397', '1:22521', '1:22545', '1:22551', '1:22566', '1:22536', '1:22542', '1:40944', '1:40989', '1:41102', '1:41145', '1:41149', '1:41157', '1:41172', '1:41230', '1:41287', '1:58808', '1:58957', '1:59083', '1:59188', '1:59196', '1:59258', '1:59325', '1:59348', '1:59374', '1:59405', '1:59415', '1:59487', '1:59512', '1:59908', '1:59915', '1:45947', '1:45948', '1:47023', '1:47072', '1:47117', '1:47158', '1:45994', '1:47048', '1:47049', '1:47100', '1:47120', '1:47153', '1:47315', '1:47346', '1:65020', '1:65148', '1:65180', '1:65190', '1:65205', '1:65229', '1:65336', '1:65358', '1:65377', '1:65393', '1:65499', '1:65504', '1:65627', '1:65635', '1:65731', '1:65755', '1:65852', '1:93680', '1:94158', '1:94213', '1:94442', '1:94693', '1:94709', '1:11889', '1:12103', '1:12152', '1:12214', '1:12251', '1:12266', '1:12312', '1:12601', '1:12800', '1:12831', '1:27522', '1:19194', '1:19262', '1:19402', '1:19411', '1:19445', '1:19504', '1:19596', '1:19622', '1:85160', '1:85387', '1:85571', '1:85646', '1:85960', '1:15346', '1:15840', '1:16115', '1:16144', '1:16212', '1:16213', '1:16241', '1:16293', '1:23779', '1:25945', '1:25960', '1:25975', '1:25126', '1:25177', '1:25262', '1:25274', '1:25308', '1:25312', '1:25329', '1:25342', '1:25355', '1:25616', '1:27270', '1:25365', '1:25273', '1:25399', '1:25500', '1:25504', '1:25544', '1:25560', '1:25651', '1:25484', '1:25528', '1:25652', '1:61573', '1:62237', '1:23251', '1:23397', '1:23924', '1:24005', '1:24046', '1:24103', '1:24126', '1:24159', '1:24224', '1:24505', '1:24609', '1:24628', '1:24629', '1:24666', '1:24667', '1:24763', '1:24798', '1:23795', '1:23843', '1:23861', '1:23868', '1:23875', '1:23962', '1:24922', '1:24949', '1:24522', '1:24542', '1:24566', '1:24590', '1:24665', '1:24733', '1:77091', '1:77125', '1:77227', '1:77304', '1:77390', '1:77571', '1:78109', '1:78133', '1:40445', '1:40533', '1:40682', '1:40402', '1:40467', '1:40540', '1:40558', '1:40726', '1:40733', '1:40744', '1:40878', '1:40907', '1:40774', '1:40873', '1:40965', '1:40980', '1:41016', '1:42626', '1:42628', '1:42629', '1:44535', '1:44746', '1:44794', '1:44828', '1:44834', '1:44883', '1:44933', '1:44988', '1:45015', '1:45020', '1:45027', '1:45050', '1:45101', '1:45322', '1:96969', '1:97161', '1:97292', '1:97495', '1:97739', '1:97929', '1:97953', '1:98063', '1:82006', '1:82152', '1:82160', '1:82517', '1:82558', '1:83336', '1:90566', '1:90611', '1:90680', '1:91758', '1:91853', '1:91993', '1:94220', '1:103544', '1:103547', '1:103671', '1:103894', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0AA4F2C-B6FB-E911-BABD-3417EBE70078.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA780643-AC10-EA11-8326-008CFAFBFB7C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5A31D770-76FC-E911-BA45-0CC47AFF0258.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/46E9ED6C-BB0A-EA11-AC8D-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72C119DC-BBF2-E911-B71C-1866DA85DFC0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2812357-95F8-E911-84BD-A4BF0126C074.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/28CA8532-26F8-E911-A6B7-0CC47AA98F98.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BEC88789-04FA-E911-82A0-0CC47A706CF0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D80C91DC-88FC-E911-8EA8-0CC47AFB8104.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E4D8B56-20F4-E911-AE7F-3C4A92F7DD14.root']);