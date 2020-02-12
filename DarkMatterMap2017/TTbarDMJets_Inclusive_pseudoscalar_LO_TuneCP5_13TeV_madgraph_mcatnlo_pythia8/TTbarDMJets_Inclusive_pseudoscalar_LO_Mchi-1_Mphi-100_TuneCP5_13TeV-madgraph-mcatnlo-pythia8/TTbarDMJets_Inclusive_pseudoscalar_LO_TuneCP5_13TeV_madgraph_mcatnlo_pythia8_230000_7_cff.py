import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8359', '1:10697', '1:10825', '1:10939', '1:13395', '1:16540', '1:16932', '1:1233', '1:5729', '1:8999', '1:15604', '1:11378', '1:16345', '1:16938', '1:19510', '1:24266', '1:24652', '1:25232', '1:25824', '1:18431', '1:23785', '1:24225', '1:30118', '1:31713', '1:32516', '1:42788', '1:104141', '1:64325', '1:82206', '1:89705', '1:82889', '1:87218', '1:89107', '1:97806', '1:92554', '1:95300', '1:51135', '1:51235', '1:52621', '1:56276', '1:56915', '1:59322', '1:59633', '1:29512', '1:42300', '1:51215', '1:56023', '1:56832', '1:58376', '1:58781', '1:59476', '1:86906', '1:64360', '1:72368', '1:64306', '1:72324', '1:88401', '1:67532', '1:78888', '1:80243', '1:102608', '1:102689', '1:102704', '1:102727', '1:102737', '1:102839', '1:102976', '1:104882', '1:104922', '1:97944', '1:21457', '1:25333', '1:31865', '1:32799', '1:41297', '1:48233', '1:48298', '1:48684', '1:48943', '1:49947', '1:55221', '1:55842', '1:58287', '1:62117', '1:76414', '1:61910', '1:65332', '1:74562', '1:76873', '1:51392', '1:52647', '1:56947', '1:59173', '1:59585', '1:59715', '1:59798', '1:61608', '1:53310', '1:55855', '1:58033', '1:61840', '1:62712', '1:77909', '1:91092', '1:93271', '1:82732', '1:88748', '1:94617', '1:84162', '1:97678', '1:106135', '1:48567', '1:48740', '1:55034', '1:57303', '1:57928', '1:60625', '1:60951', '1:61318', '1:62262', '1:58183', '1:58734', '1:59626', '1:61295', '1:52436', '1:52456', '1:52493', '1:52512', '1:52590', '1:52618', '1:52944', '1:52957', '1:53017', '1:53024', '1:53055', '1:53146', '1:53152', '1:53403', '1:61369', '1:61476', '1:61531', '1:61532', '1:61538', '1:61645', '1:61758', '1:62160', '1:62319', '1:61311', '1:61814', '1:62065', '1:62314', '1:64339', '1:64375', '1:64511', '1:66129', '1:66258', '1:80259', '1:90862', '1:95353', '1:98028', '1:9854', '1:9967', '1:12524', '1:12590', '1:12616', '1:12853', '1:13157', '1:14112', '1:14216', '1:14726', '1:14761', '1:14897', '1:15112', '1:15243', '1:16531', '1:16565', '1:16718', '1:101042', '1:101122', '1:20266', '1:20458', '1:21127', '1:21336', '1:23634', '1:23797', '1:21512', '1:21911', '1:21957', '1:21977', '1:94528', '1:82070', '1:91808', '1:97072', '1:86969', '1:98415', '1:98807', '1:52542', '1:52622', '1:53605', '1:53686', '1:58710', '1:58819', '1:58928', '1:59648', '1:52332', '1:58521', '1:58716', '1:59311', '1:59313', '1:61809', '1:62404', '1:62502', '1:62672', '1:57745', '1:60057', '1:60497', '1:60578', '1:61370', '1:65152', '1:65540', '1:64433', '1:64546', '1:65072', '1:66612', '1:66995', '1:65940', '1:67382', '1:67463', '1:64779', '1:64588', '1:64620', '1:65363', '1:66894', '1:67674', '1:70649', '1:83189', '1:94945', '1:29982', '1:40758', '1:40949', '1:46790', '1:47312', '1:47968', '1:18616', '1:32006', '1:39220', '1:44428', '1:44478', '1:29036', '1:48111', '1:43968', '1:58852', '1:59783', '1:59824', '1:59848', '1:60113', '1:60434', '1:81541', '1:61002', '1:61009', '1:64156', '1:64327', '1:64335', '1:67124', '1:67643', '1:67724', '1:67974', '1:67996', '1:68000', '1:71564', '1:72347', '1:39202', '1:51159', '1:51524', '1:51624', '1:51751', '1:51814', '1:51838', '1:51951', '1:51968', '1:52049', '1:52122', '1:52301', '1:52366', '1:52374', '1:52551', '1:43066', '1:45302', '1:51880', '1:51919', '1:52195', '1:52446', '1:53476', '1:53801', '1:59424', '1:59443', '1:59562', '1:60032', '1:60167', '1:60337', '1:60351', '1:75837', '1:79209', '1:65182', '1:65963', '1:72622', '1:74578', '1:76509', '1:79430', '1:81596', '1:76328', '1:82474', '1:84567', '1:90262', '1:94218', '1:98086', '1:98949', '1:86053', '1:94162', '1:96848', '1:87273', '1:89954', '1:91425', '1:96592', '1:85885', '1:87639', '1:91125', '1:91748', '1:101134', '1:103765', '1:81174', '1:81314', '1:81330', '1:81547', '1:81550', '1:81566', '1:81679', '1:81728', '1:80872', '1:81150', '1:81151', '1:43567', '1:43742', '1:51600', '1:56132', '1:62180', '1:62908', '1:64107', '1:64202', '1:64218', '1:64269', '1:64272', '1:64662', '1:64905', '1:79221', '1:79238', '1:80843', '1:80844', '1:92682', '1:72053', '1:72986', '1:74170', '1:65546', '1:66956', '1:67118', '1:79241', '1:95074', '1:70478', '1:82585', '1:94910', '1:70541', '1:92174', '1:96936', '1:102274', '1:101012', '1:101063', '1:102204', '1:102240', '1:102256', '1:101027', '1:101085', '1:101138', '1:101156', '1:101199', '1:101268', '1:101424', '1:101447', '1:101533', '1:101850', '1:102417', '1:102881', '1:104049', '1:103664', '1:103914', '1:103920', '1:103717', '1:103719', '1:103757', '1:105617', '1:105903', '1:106372', '1:105611', '1:105674', '1:105798', '1:105804', '1:105839', '1:105613', '1:105773', '1:105780', '1:59490', '1:59608', '1:59732', '1:59981', '1:60383', '1:60399', '1:71531', '1:71547', '1:71732', '1:71781', '1:71862', '1:71878', '1:71902', '1:71928', '1:71942', '1:71944', '1:71945', '1:72048', '1:72097', '1:72098', '1:72113', '1:72193', '1:72235', '1:72357', '1:72358', '1:72464', '1:102549', '1:102150', '1:102406', '1:102451', '1:67018', '1:67056', '1:67163', '1:67692', '1:67795', '1:71037', '1:71562', '1:70598', '1:83938', '1:84210', '1:93069', '1:95355', '1:96065', '1:96671', '1:86804', '1:87112', '1:91146', '1:106220', '1:86155', '1:96225', '1:98109', '1:98618', '1:94184', '1:94324', '1:96239', '1:85868', '1:95504', '1:106057', '1:106315', '1:106373', '1:101936', '1:104572', '1:104678', '1:101671', '1:102468', '1:102474', '1:102838', '1:104133', '1:104206', '1:62684', '1:45674', '1:52834', '1:58620', '1:73421', '1:73577', '1:93167', '1:95470', '1:73471', '1:73505', '1:75378', '1:81763', '1:87326', '1:94279', '1:104771', '1:106088', '1:104290', '1:104670', '1:105182', '1:106080', '1:101394', '1:102584', '1:79279', '1:79438', '1:79521', '1:80046', '1:80517', '1:80535', '1:80583', '1:13986', '1:17014', '1:17845', '1:19142', '1:19160', '1:20067', '1:23546', '1:23649', '1:23954', '1:12370', '1:25476', '1:25478', '1:25606', '1:30599', '1:39722', '1:64208', '1:74437', '1:75166', '1:75312', '1:80010', '1:80862', '1:65027', '1:72717', '1:79184', '1:79823', '1:81146', '1:84934', '1:85450', '1:85819', '1:89431', '1:90547', '1:90928', '1:91784', '1:93963', '1:77598', '1:78142', '1:95155', '1:59757', '1:52237', '1:54071', '1:54693', '1:59953', '1:62570', '1:65062', '1:45960', '1:54439', '1:57000', '1:20268', '1:20543', '1:21838', '1:25239', '1:25744', '1:25775', '1:25834', '1:25905', '1:20617', '1:24117', '1:24399', '1:24619', '1:24946', '1:25539', '1:24079', '1:24734', '1:25761', '1:25963', '1:75394', '1:75777', '1:22177', '1:24052', '1:30730', '1:39128', '1:39604', '1:42001', '1:42681', '1:18630', '1:39193', '1:42465', '1:42833', '1:44051', '1:44423', '1:44788', '1:73474', '1:29497', '1:29973', '1:47922', '1:48168', '1:48184', '1:66632', '1:72201', '1:40037', '1:41675', '1:43669', '1:58154', '1:49830', '1:39036', '1:39933', '1:56546', '1:45685', '1:76083', '1:88275', '1:76779', '1:79166', '1:79717', '1:80088', '1:80095', '1:80304', '1:80347', '1:6694', '1:10672', '1:15202', '1:5795', '1:6273', '1:8185', '1:8455', '1:9397', '1:10298', '1:14547', '1:16766', '1:16372', '1:16561', '1:16594', '1:16621', '1:16650', '1:16707', '1:16806', '1:60176', '1:70459', '1:73545', '1:75340', '1:84200', '1:93191', '1:61446', '1:73121', '1:73153', '1:73367', '1:80449', '1:89276', '1:93954', '1:70173', '1:76960', '1:82716', '1:70970', '1:82881', '1:82992', '1:83627', '1:86455', '1:87838', '1:73409', '1:78204', '1:84464', '1:88160', '1:89417', '1:94798', '1:96012', '1:98536', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CC916E5A-F8FE-E911-BC5C-3417EBE70078.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/261A750B-1502-EA11-A901-0026B9278651.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0DE8F81-AD03-EA11-895A-A0369FD0B142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A23C784C-A502-EA11-A4FB-00259074AE52.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A6DE693B-2902-EA11-A934-AC1F6B0DE228.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80593C2E-A502-EA11-A430-20CF3027A5F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/20F14403-9A02-EA11-9EF6-D48564599C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A6DC8DA6-9F03-EA11-A25B-CCC5E5F02BFB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B84232C7-D102-EA11-8D9E-A0369FC51EDC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC333E44-8703-EA11-9B66-0242AC1C0506.root']);