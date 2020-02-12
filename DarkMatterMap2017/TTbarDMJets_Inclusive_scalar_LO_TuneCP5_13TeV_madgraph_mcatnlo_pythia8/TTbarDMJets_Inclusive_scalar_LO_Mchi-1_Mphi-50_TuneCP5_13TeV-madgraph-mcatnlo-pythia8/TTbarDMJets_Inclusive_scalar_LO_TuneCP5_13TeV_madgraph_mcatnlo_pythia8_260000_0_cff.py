import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:51707', '1:52544', '1:60347', '1:60886', '1:63387', '1:63438', '1:51657', '1:54667', '1:54732', '1:63977', '1:68061', '1:72477', '1:73838', '1:73905', '1:73936', '1:78622', '1:69808', '1:70859', '1:71136', '1:72369', '1:72588', '1:80444', '1:80687', '1:96047', '1:100766', '1:87636', '1:89659', '1:91314', '1:96263', '1:96777', '1:101191', '1:95761', '1:95769', '1:101331', '1:95899', '1:98284', '1:101550', '1:101682', '1:102102', '1:80432', '1:80459', '1:80493', '1:80942', '1:8568', '1:8690', '1:8703', '1:9074', '1:9132', '1:9147', '1:13191', '1:14334', '1:14582', '1:14584', '1:14640', '1:14680', '1:14753', '1:14820', '1:16929', '1:25578', '1:33482', '1:36565', '1:38394', '1:38955', '1:15285', '1:15380', '1:15518', '1:15778', '1:15795', '1:16391', '1:72938', '1:73063', '1:75475', '1:77773', '1:78453', '1:67313', '1:69255', '1:78757', '1:55746', '1:55931', '1:55935', '1:62475', '1:62492', '1:62495', '1:62605', '1:62611', '1:59714', '1:59970', '1:60021', '1:60055', '1:60073', '1:60094', '1:60159', '1:60178', '1:60234', '1:60237', '1:60297', '1:60314', '1:60354', '1:70224', '1:80639', '1:85080', '1:72015', '1:80467', '1:87328', '1:87375', '1:87393', '1:89253', '1:96724', '1:99284', '1:78597', '1:80340', '1:80629', '1:80383', '1:80529', '1:80531', '1:80532', '1:80543', '1:80570', '1:80597', '1:80601', '1:80608', '1:80610', '1:80652', '1:86251', '1:86261', '1:86279', '1:86304', '1:86379', '1:86434', '1:86604', '1:86654', '1:87614', '1:87629', '1:87648', '1:87651', '1:87744', '1:87813', '1:87815', '1:90149', '1:90640', '1:90803', '1:89200', '1:89204', '1:89314', '1:91651', '1:91673', '1:91675', '1:91698', '1:91702', '1:91731', '1:91747', '1:91761', '1:91821', '1:2545', '1:154', '1:325', '1:501', '1:509', '1:525', '1:566', '1:614', '1:622', '1:636', '1:757', '1:2242', '1:5241', '1:7411', '1:7711', '1:7871', '1:313', '1:326', '1:455', '1:483', '1:592', '1:1560', '1:2533', '1:4182', '1:4736', '1:5568', '1:6022', '1:6062', '1:6922', '1:7053', '1:7079', '1:7167', '1:650', '1:683', '1:691', '1:542', '1:22113', '1:22168', '1:22179', '1:22181', '1:22821', '1:59426', '1:53779', '1:53821', '1:53931', '1:53996', '1:58029', '1:174', '1:212', '1:215', '1:218', '1:232', '1:275', '1:298', '1:309', '1:312', '1:320', '1:324', '1:341', '1:353', '1:3882', '1:3907', '1:4851', '1:5521', '1:9646', '1:391', '1:394', '1:419', '1:441', '1:447', '1:529', '1:535', '1:463', '1:605', '1:618', '1:693', '1:4703', '1:6347', '1:6882', '1:7046', '1:7078', '1:1291', '1:32886', '1:32893', '1:32895', '1:32951', '1:34123', '1:77044', '1:81766', '1:73268', '1:73362', '1:73378', '1:73971', '1:73993', '1:73849', '1:98189', '1:22336', '1:22337', '1:22384', '1:22919', '1:22927', '1:22934', '1:22936', '1:22971', '1:59778', '1:57995', '1:58200', '1:32760', '1:34252', '1:73646', '1:73890', '1:90524', '1:53848', '1:58358', '1:58367', '1:58387', '1:94718', '1:101259', '1:97699', '1:98979', '1:99129', '1:99981', '1:14128', '1:14183', '1:14191', '1:14200', '1:14246', '1:14313', '1:14327', '1:14328', '1:14353', '1:14395', '1:14400', '1:14402', '1:14291', '1:14436', '1:14602', '1:14649', '1:14761', '1:15069', '1:15365', '1:16410', '1:15250', '1:15254', '1:15308', '1:15477', '1:15609', '1:15714', '1:15534', '1:15762', '1:15913', '1:16088', '1:16352', '1:16565', '1:16679', '1:16799', '1:17668', '1:17673', '1:17757', '1:17763', '1:19728', '1:17588', '1:17750', '1:17865', '1:20756', '1:20911', '1:16892', '1:16931', '1:16989', '1:17085', '1:17094', '1:17142', '1:17191', '1:17313', '1:16994', '1:17008', '1:17043', '1:17065', '1:17124', '1:17163', '1:17262', '1:17270', '1:17278', '1:17294', '1:17317', '1:17374', '1:17594', '1:17280', '1:20997', '1:28023', '1:28271', '1:24110', '1:24223', '1:24337', '1:24411', '1:24629', '1:24928', '1:24938', '1:31022', '1:31103', '1:39161', '1:56854', '1:57882', '1:60440', '1:73968', '1:85362', '1:85885', '1:68086', '1:34331', '1:34332', '1:32720', '1:32721', '1:32812', '1:32971', '1:34635', '1:33077', '1:34124', '1:34747', '1:54221', '1:58300', '1:73831', '1:80762', '1:8275', '1:25851', '1:26856', '1:38013', '1:8500', '1:8541', '1:8585', '1:8666', '1:8682', '1:8793', '1:8817', '1:8610', '1:8751', '1:8975', '1:9242', '1:13330', '1:10746', '1:11153', '1:11157', '1:11813', '1:11817', '1:12146', '1:12147', '1:12157', '1:11229', '1:11284', '1:11380', '1:11389', '1:11512', '1:11592', '1:11613', '1:11619', '1:30219', '1:24234', '1:24478', '1:24513', '1:30387', '1:35909', '1:24275', '1:39350', '1:40283', '1:50507', '1:56622', '1:57127', '1:57152', '1:57734', '1:59994', '1:24476', '1:21883', '1:21956', '1:21997', '1:22076', '1:21608', '1:21627', '1:21648', '1:21688', '1:21725', '1:21743', '1:21874', '1:21880', '1:21920', '1:21955', '1:22016', '1:22077', '1:21643', '1:22277', '1:22658', '1:31239', '1:30200', '1:30655', '1:30608', '1:30690', '1:30803', '1:30957', '1:31542', '1:30347', '1:30350', '1:33403', '1:33478', '1:33501', '1:33512', '1:33641', '1:33821', '1:33828', '1:33834', '1:36001', '1:101', '1:315', '1:336', '1:604', '1:761', '1:1763', '1:3584', '1:2326', '1:2846', '1:3466', '1:3596', '1:5129', '1:3074', '1:11569', '1:12968', '1:42079', '1:42272', '1:42392', '1:41168', '1:41183', '1:41186', '1:41377', '1:41681', '1:41702', '1:42416', '1:42724', '1:12682', '1:42245', '1:42247', '1:15371', '1:16428', '1:43641', '1:43644', '1:43650', '1:45587', '1:45791', '1:48332', '1:65214', '1:65225', '1:1390', '1:4063', '1:5813', '1:6112', '1:6558', '1:8157', '1:8482', '1:9048', '1:18383', '1:13016', '1:13347', '1:15204', '1:15469', '1:15542', '1:15648', '1:13549', '1:13713', '1:15025', '1:16290', '1:16556', '1:18346', '1:11197', '1:11527', '1:11533', '1:11542', '1:11561', '1:11570', '1:11574', '1:11723', '1:11734', '1:11736', '1:12645', '1:11461', '1:11466', '1:41493', '1:42550', '1:42556', '1:42558', '1:42560', '1:12922', '1:42065', '1:42219', '1:42222', '1:42226', '1:42237', '1:42330', '1:42331', '1:42361', '1:12980', '1:12986', '1:41191', '1:41492', '1:41502', '1:41517', '1:41682', '1:41698', '1:42699', '1:41503', '1:59808', '1:57782', '1:54180', '1:54634', '1:32982', '1:34228', '1:34993', '1:37033', '1:37193', '1:37641', '1:37833', '1:66084', '1:48831', '1:48835', '1:48848', '1:48851', '1:48854', '1:48858', '1:48865', '1:48866', '1:55317', '1:50965', '1:52089', '1:57180', '1:51538', '1:52545', '1:24735', '1:39291', '1:51812', '1:53446', '1:49446', '1:49805', '1:52397', '1:52838', '1:57431', '1:57598', '1:51992', '1:60514', '1:34174', '1:34579', '1:35319', '1:35581', '1:35818', '1:40668', '1:46956', '1:46336', '1:46680', '1:46943', '1:49749', '1:49867', '1:52356', '1:46760', '1:82064', '1:82076', '1:82094', '1:82109', '1:82124', '1:82137', '1:79376', '1:86598', '1:87171', '1:91683', '1:77373', '1:89654', '1:82202', '1:82207', '1:82219', '1:14840', '1:15334', '1:43453', '1:48439', '1:48458', '1:11741', '1:11750', '1:32415', '1:37409', '1:24598', '1:30837', '1:39592', '1:46513', '1:65474', '1:65477', '1:65480', '1:65490', '1:65495', '1:65515', '1:65519', '1:65520', '1:65528', '1:45864', '1:45874', '1:45869', '1:45940', '1:48473', '1:65236', '1:45260', '1:65539', '1:65540', '1:48384', '1:47158', '1:47305', '1:47315', '1:47325', '1:66110', '1:68139', '1:72808', '1:92663', '1:93230', '1:93401', '1:86552', '1:54755', '1:55667', '1:64445', '1:88078', '1:89845', '1:90260', '1:90268', '1:90282', '1:90317', '1:90335', '1:90356', '1:90867', '1:90900', '1:31019', '1:36771', '1:37692', '1:28056', '1:32230', '1:34208', '1:39890', '1:46740', '1:35109', '1:18957', '1:39420', '1:50169', '1:53687', '1:57776', '1:61253', '1:27393', '1:50645', '1:52276', '1:54887', '1:39128', '1:78009', '1:78068', '1:78100', '1:78361', '1:78381', '1:78435', '1:80745', '1:80749', '1:81277', '1:81284', '1:83979', '1:83981', '1:83982', '1:83983', '1:93334', '1:45783', '1:45816', '1:45937', '1:45955', '1:48312', '1:48904', '1:65183', '1:65204', '1:45849', '1:48946', '1:65203', '1:65849', '1:65861', '1:65862', '1:48929', '1:48932', '1:65974', '1:44949', '1:47148', '1:47149', '1:70106', '1:86889', '1:88309', '1:91388', '1:91422', '1:70633', '1:70860', '1:71092', '1:78670', '1:78740', '1:80681', '1:77594', '1:80797', '1:75601', '1:75613', '1:75619', '1:75745', '1:75773', '1:78148', '1:78163', '1:78219', '1:78227', '1:78229', '1:78312', '1:76676', '1:78859', '1:96257', '1:96778', '1:96793', '1:96816', '1:98027', '1:97959', '1:80962', '1:81458', '1:81529', '1:81587', '1:79698', '1:79714', '1:79798', '1:79863', '1:79870', '1:80248', '1:80666', '1:80740', '1:80799', '1:80708', '1:81216', '1:80830', '1:81395', '1:81399', '1:83946', '1:83954', '1:83955', '1:83959', '1:83965', '1:93617', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8043D626-B016-EA11-8A6B-14187751C239.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D6C9BD41-E917-EA11-AC25-24BE05C63631.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/98533757-B016-EA11-BA5A-3417EBE51901.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/88043001-7B17-EA11-92B4-9CDC714AE580.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2A4E415B-BF17-EA11-B25D-EC0D9A8221CE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B855FCAA-0F18-EA11-91AF-A0369F30FFD2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1054BB23-6E17-EA11-A63C-A0369F3102F6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/7830E6AA-AE17-EA11-830F-E0071B7AD580.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/EA8BAF91-6317-EA11-B8EA-B8CA3A70A5E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BCA7C346-9817-EA11-A3E0-0242AC1C0500.root']);