import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:7209', '1:7331', '1:7379', '1:7652', '1:7790', '1:7216', '1:7264', '1:7344', '1:7385', '1:7404', '1:7612', '1:7629', '1:7946', '1:8094', '1:49326', '1:49705', '1:49740', '1:49958', '1:49973', '1:49433', '1:49434', '1:49464', '1:49491', '1:49497', '1:49505', '1:49665', '1:49676', '1:49738', '1:49739', '1:49794', '1:67833', '1:67700', '1:67823', '1:67899', '1:67845', '1:67856', '1:68258', '1:69710', '1:72551', '1:72674', '1:73212', '1:78307', '1:99430', '1:91125', '1:91132', '1:91188', '1:91205', '1:91245', '1:91259', '1:91293', '1:91308', '1:91349', '1:94509', '1:94511', '1:94730', '1:94888', '1:94698', '1:95085', '1:96323', '1:96361', '1:96477', '1:96547', '1:96654', '1:96727', '1:96752', '1:97445', '1:101558', '1:101706', '1:101843', '1:102222', '1:102252', '1:102312', '1:102314', '1:102319', '1:102337', '1:102346', '1:102356', '1:25965', '1:26905', '1:29162', '1:29482', '1:29568', '1:29632', '1:33586', '1:28027', '1:32224', '1:35825', '1:27987', '1:27996', '1:28040', '1:28818', '1:28915', '1:28997', '1:30035', '1:30134', '1:30813', '1:30881', '1:35132', '1:37038', '1:39886', '1:39978', '1:88087', '1:51702', '1:57810', '1:76733', '1:76740', '1:76743', '1:76750', '1:76786', '1:76788', '1:76859', '1:76871', '1:76879', '1:78782', '1:78805', '1:78846', '1:78874', '1:70091', '1:80767', '1:95729', '1:97401', '1:97649', '1:97878', '1:98626', '1:98244', '1:100518', '1:100638', '1:100737', '1:73142', '1:77285', '1:77777', '1:77882', '1:87531', '1:89163', '1:89911', '1:90936', '1:91449', '1:91630', '1:99150', '1:88802', '1:89066', '1:90825', '1:94979', '1:100141', '1:100206', '1:99214', '1:89027', '1:90958', '1:17563', '1:18354', '1:18358', '1:20160', '1:20223', '1:21158', '1:21303', '1:56402', '1:56440', '1:56942', '1:57170', '1:57308', '1:57479', '1:57641', '1:57892', '1:57913', '1:58064', '1:58202', '1:58248', '1:58396', '1:78763', '1:78787', '1:78850', '1:85589', '1:86864', '1:71903', '1:72203', '1:72294', '1:72328', '1:86877', '1:88398', '1:88780', '1:89118', '1:89379', '1:89381', '1:89392', '1:89739', '1:89878', '1:89890', '1:97290', '1:97801', '1:28267', '1:31066', '1:35174', '1:35540', '1:37111', '1:46290', '1:50122', '1:50502', '1:51522', '1:52560', '1:58514', '1:58703', '1:58841', '1:59035', '1:59078', '1:60033', '1:89157', '1:91725', '1:28941', '1:30789', '1:49418', '1:50057', '1:50114', '1:50381', '1:50620', '1:51317', '1:51337', '1:51404', '1:51557', '1:50197', '1:51009', '1:52151', '1:52421', '1:28030', '1:28159', '1:32763', '1:69492', '1:69616', '1:102004', '1:71757', '1:70339', '1:71221', '1:71223', '1:71324', '1:71751', '1:71841', '1:71760', '1:72859', '1:15797', '1:19930', '1:20432', '1:20629', '1:21738', '1:6654', '1:8543', '1:10148', '1:14123', '1:4914', '1:5019', '1:6529', '1:6974', '1:7979', '1:15140', '1:17426', '1:22540', '1:15883', '1:7767', '1:10722', '1:14687', '1:20892', '1:36323', '1:36696', '1:36802', '1:38603', '1:6384', '1:8146', '1:10333', '1:16377', '1:8492', '1:15780', '1:17674', '1:57962', '1:60012', '1:60098', '1:60147', '1:60628', '1:60693', '1:61173', '1:61286', '1:68874', '1:69405', '1:73492', '1:76613', '1:76810', '1:15739', '1:27002', '1:29208', '1:31547', '1:31603', '1:32199', '1:35322', '1:24270', '1:27507', '1:31174', '1:31243', '1:32081', '1:35965', '1:39983', '1:23982', '1:46888', '1:34316', '1:38888', '1:38895', '1:46383', '1:46436', '1:46460', '1:46588', '1:46625', '1:46836', '1:81401', '1:81636', '1:81768', '1:81776', '1:91879', '1:91951', '1:91979', '1:99539', '1:27340', '1:34620', '1:39240', '1:37075', '1:37365', '1:2569', '1:7491', '1:7758', '1:8443', '1:9184', '1:10104', '1:14155', '1:14228', '1:14868', '1:15661', '1:8486', '1:14645', '1:17678', '1:17987', '1:19951', '1:21781', '1:21901', '1:22138', '1:8709', '1:14317', '1:27398', '1:24423', '1:30376', '1:31118', '1:31489', '1:31522', '1:32160', '1:32176', '1:32178', '1:34341', '1:34538', '1:35019', '1:35283', '1:35484', '1:35741', '1:35786', '1:95056', '1:96315', '1:96462', '1:98987', '1:96026', '1:96399', '1:101926', '1:86627', '1:99497', '1:5877', '1:5965', '1:5993', '1:5801', '1:5815', '1:5850', '1:5854', '1:5864', '1:5923', '1:5958', '1:5986', '1:5999', '1:21927', '1:21949', '1:22463', '1:22665', '1:22680', '1:22719', '1:22759', '1:22770', '1:6236', '1:16203', '1:16402', '1:20146', '1:25707', '1:26488', '1:26501', '1:38263', '1:9862', '1:26116', '1:26564', '1:29040', '1:33141', '1:33276', '1:33892', '1:36685', '1:34074', '1:35982', '1:22014', '1:37922', '1:80568', '1:80955', '1:81028', '1:81054', '1:81061', '1:81077', '1:81102', '1:81130', '1:81148', '1:39929', '1:57957', '1:35053', '1:37503', '1:37878', '1:37750', '1:37783', '1:37814', '1:37885', '1:37887', '1:80779', '1:80803', '1:81231', '1:57834', '1:57844', '1:60819', '1:67477', '1:90055', '1:97249', '1:100291', '1:100932', '1:95576', '1:97748', '1:95614', '1:7221', '1:7380', '1:9489', '1:16155', '1:16514', '1:16840', '1:17565', '1:17611', '1:17690', '1:17974', '1:18728', '1:19846', '1:21137', '1:22942', '1:29944', '1:25043', '1:25838', '1:26366', '1:26723', '1:101716', '1:56279', '1:56481', '1:56593', '1:56709', '1:56828', '1:57064', '1:57137', '1:57453', '1:57684', '1:58313', '1:58663', '1:60105', '1:61088', '1:88699', '1:89330', '1:89946', '1:91247', '1:89384', '1:89455', '1:89638', '1:89789', '1:90403', '1:90651', '1:91858', '1:94485', '1:89496', '1:89538', '1:91534', '1:18152', '1:20201', '1:20577', '1:20690', '1:16688', '1:17624', '1:17697', '1:21750', '1:21754', '1:22653', '1:22929', '1:24074', '1:32815', '1:74873', '1:74977', '1:78237', '1:78420', '1:78462', '1:78636', '1:78824', '1:70053', '1:70112', '1:70378', '1:70421', '1:70474', '1:70875', '1:70939', '1:71071', '1:71201', '1:71815', '1:72740', '1:74262', '1:77827', '1:94869', '1:95830', '1:97320', '1:96996', '1:97338', '1:97933', '1:97293', '1:101945', '1:17235', '1:20156', '1:21340', '1:22111', '1:22215', '1:22634', '1:24819', '1:27572', '1:27983', '1:39485', '1:24024', '1:24340', '1:24357', '1:24559', '1:28072', '1:28123', '1:30781', '1:30848', '1:37716', '1:40046', '1:24088', '1:24242', '1:24599', '1:28324', '1:32814', '1:68630', '1:70449', '1:70490', '1:70552', '1:70553', '1:70617', '1:70698', '1:70796', '1:70925', '1:71243', '1:71277', '1:71404', '1:71444', '1:71474', '1:71745', '1:71871', '1:77043', '1:77205', '1:77843', '1:78689', '1:100876', '1:75734', '1:75742', '1:75981', '1:76181', '1:76218', '1:6526', '1:18040', '1:15731', '1:16264', '1:17651', '1:21632', '1:21822', '1:28914', '1:27397', '1:27518', '1:28515', '1:30029', '1:31457', '1:35929', '1:38444', '1:39878', '1:40720', '1:49883', '1:51137', '1:51402', '1:52429', '1:57394', '1:39185', '1:39995', '1:40479', '1:40984', '1:49472', '1:49583', '1:80980', '1:86031', '1:94341', '1:77768', '1:78642', '1:81704', '1:64787', '1:78255', '1:78269', '1:70064', '1:78179', '1:72144', '1:73966', '1:74705', '1:74712', '1:77122', '1:77523', '1:78139', '1:78198', '1:78585', '1:70042', '1:70973', '1:71192', '1:72335', '1:73592', '1:77162', '1:77165', '1:77359', '1:78253', '1:81430', '1:88558', '1:78634', '1:79525', '1:79921', '1:80694', '1:85753', '1:88112', '1:87231', '1:88446', '1:89778', '1:97188', '1:85481', '1:85613', '1:95317', '1:97174', '1:97653', '1:98854', '1:89624', '1:89666', '1:54255', '1:37639', '1:37688', '1:37796', '1:37868', '1:38909', '1:53674', '1:54059', '1:54081', '1:54108', '1:54147', '1:54152', '1:54155', '1:54166', '1:64554', '1:64669', '1:64706', '1:64735', '1:64849', '1:64871', '1:64879', '1:64885', '1:64905', '1:64943', '1:67342', '1:76393', '1:76517', '1:76524', '1:76478', '1:76488', '1:76516', '1:76555', '1:76616', '1:76654', '1:50814', '1:51888', '1:51900', '1:52046', '1:52184', '1:52362', '1:52705', '1:52727', '1:52808', '1:52851', '1:51127', '1:51260', '1:51601', '1:51617', '1:51621', '1:60756', '1:60773', '1:60873', '1:60879', '1:60898', '1:60988', '1:61004', '1:61843', '1:61875', '1:61912', '1:61944', '1:61976', '1:62871', '1:63011', '1:63013', '1:63031', '1:63765', '1:69152', '1:71018', '1:71033', '1:71039', '1:71126', '1:71271', '1:71367', '1:71427', '1:71438', '1:71786', '1:71846', '1:71883', '1:71924', '1:72074', '1:72095', '1:72096', '1:72103', '1:72216', '1:72246', '1:76723', '1:9228', '1:10888', '1:20170', '1:20454', '1:9896', '1:13472', '1:17665', '1:21071', '1:22240', '1:22295', '1:25101', '1:10755', '1:6656', '1:6524', '1:6689', '1:6738', '1:6774', '1:7453', '1:7769', '1:6751', '1:7077', '1:7682', '1:8662', '1:8929', '1:8969', '1:9382', '1:10024', '1:87677', '1:91882', '1:94256', '1:94270', '1:94455', '1:99108', '1:89633', '1:94924', '1:95013', '1:96000', '1:97009', '1:49811', '1:51156', '1:53695', '1:57307', '1:57324', '1:58016', '1:58496', '1:50131', '1:53002', '1:53935', '1:56198', '1:56667', '1:56784', '1:57150', '1:59466', '1:62716', '1:68035', '1:68051', '1:68248', '1:69324', '1:75006', '1:75055', '1:67538', '1:68906', '1:71951', '1:72671', '1:73168', '1:73538', '1:74271', '1:74485', '1:74501', '1:74909', '1:74939', '1:76605', '1:75316', '1:75660', '1:75720', '1:76059', '1:76088', '1:76211', '1:76228', '1:76357', '1:76875', '1:50558', '1:52018', '1:52438', '1:53468', '1:53628', '1:56250', '1:56599', '1:56997', '1:57530', '1:57579', '1:59118', '1:59239', '1:60119', '1:60161', '1:61067', '1:86293', '1:88462', '1:88895', '1:89248', '1:89669', '1:77918', '1:86463', '1:87075', '1:87136', '1:87232', '1:87507', '1:87588', '1:87612', '1:87622', '1:87824', '1:87941', '1:90003', '1:80269', '1:86112', '1:88963', '1:89021', '1:99477', '1:86393', '1:86399', '1:88630', '1:89009', '1:89668', '1:89872', '1:86307', '1:89842', '1:99243', '1:100910', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E0D04434-29FD-E911-8A06-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E2F140C-670A-EA11-AF1D-AC1F6BAC8038.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2C42B47-1A0B-EA11-8F90-0025905B8600.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EA482F8-20FE-E911-B746-0CC47AF9B2B6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92731751-11FE-E911-8809-0CC47AFF02E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/08535ED4-70F7-E911-BD73-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC2DA7CD-1E0B-EA11-804C-AC1F6BAC7F24.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70D87FC9-120B-EA11-946F-0CC47A4C8E26.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AAA24F3-4FFC-E911-AC32-00215A491956.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D24779ED-140B-EA11-B78B-0025905B858A.root']);