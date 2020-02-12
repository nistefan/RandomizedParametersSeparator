import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:53627', '1:56499', '1:57332', '1:62254', '1:81260', '1:82630', '1:85164', '1:87498', '1:87612', '1:93434', '1:96552', '1:96886', '1:97111', '1:94428', '1:106093', '1:90739', '1:90877', '1:94809', '1:101104', '1:101230', '1:101278', '1:101390', '1:101423', '1:101454', '1:101469', '1:101020', '1:101107', '1:101284', '1:101710', '1:98166', '1:94574', '1:94072', '1:94190', '1:94325', '1:95716', '1:97406', '1:97511', '1:97641', '1:101683', '1:102007', '1:102465', '1:101344', '1:101403', '1:104671', '1:105005', '1:104587', '1:97917', '1:98555', '1:104184', '1:104466', '1:104959', '1:104079', '1:104210', '1:5841', '1:7162', '1:8096', '1:9753', '1:15220', '1:11212', '1:25549', '1:1550', '1:4202', '1:6304', '1:32903', '1:20623', '1:27575', '1:31607', '1:39268', '1:39546', '1:42031', '1:42414', '1:42935', '1:45049', '1:47467', '1:47875', '1:45313', '1:47244', '1:18082', '1:47000', '1:49828', '1:46254', '1:41220', '1:49189', '1:13744', '1:13919', '1:13962', '1:13988', '1:14081', '1:14147', '1:14794', '1:14829', '1:14893', '1:15299', '1:15446', '1:18305', '1:18987', '1:13883', '1:13890', '1:13922', '1:14007', '1:14381', '1:14382', '1:14472', '1:14502', '1:14583', '1:14597', '1:14663', '1:14664', '1:14744', '1:14791', '1:14901', '1:14995', '1:15002', '1:15106', '1:15128', '1:15253', '1:15383', '1:15634', '1:51638', '1:51719', '1:51765', '1:51767', '1:51897', '1:51957', '1:51976', '1:55475', '1:14460', '1:14413', '1:14699', '1:14753', '1:14970', '1:15081', '1:15114', '1:15651', '1:15996', '1:16202', '1:16274', '1:16385', '1:16931', '1:16953', '1:15213', '1:15263', '1:15283', '1:15284', '1:15500', '1:15716', '1:15819', '1:26123', '1:26247', '1:26376', '1:17402', '1:17084', '1:17238', '1:17295', '1:17459', '1:17578', '1:17603', '1:17668', '1:17671', '1:17732', '1:17788', '1:17942', '1:19235', '1:19335', '1:19464', '1:27936', '1:28237', '1:44229', '1:44864', '1:45191', '1:48194', '1:49199', '1:49844', '1:58823', '1:59740', '1:61134', '1:61687', '1:25049', '1:25056', '1:25072', '1:25196', '1:25315', '1:25401', '1:25447', '1:42236', '1:42358', '1:42308', '1:42399', '1:42413', '1:42445', '1:42478', '1:42479', '1:42485', '1:42607', '1:42779', '1:42785', '1:64082', '1:64251', '1:64522', '1:64776', '1:73030', '1:78652', '1:79039', '1:79259', '1:79539', '1:81810', '1:82195', '1:82601', '1:71340', '1:72854', '1:77312', '1:54663', '1:54671', '1:54915', '1:102017', '1:83455', '1:92790', '1:97339', '1:88008', '1:88103', '1:88153', '1:88419', '1:88428', '1:88492', '1:86329', '1:86413', '1:86447', '1:87031', '1:87323', '1:86545', '1:86787', '1:88432', '1:89082', '1:89178', '1:90679', '1:91037', '1:91064', '1:91066', '1:91687', '1:91946', '1:92074', '1:106012', '1:83219', '1:86212', '1:87592', '1:91319', '1:91960', '1:84398', '1:84523', '1:85923', '1:86892', '1:89257', '1:91199', '1:92202', '1:93013', '1:94900', '1:91334', '1:91562', '1:92217', '1:92825', '1:93859', '1:93940', '1:96355', '1:97606', '1:84311', '1:84843', '1:85405', '1:86896', '1:87571', '1:93777', '1:94077', '1:94425', '1:86243', '1:89154', '1:90037', '1:94912', '1:102898', '1:105793', '1:105838', '1:105893', '1:106436', '1:101625', '1:102634', '1:102896', '1:104558', '1:105398', '1:104667', '1:104063', '1:101923', '1:104249', '1:104876', '1:104895', '1:102104', '1:102128', '1:102666', '1:104571', '1:102023', '1:102918', '1:4228', '1:4335', '1:4724', '1:4860', '1:1944', '1:1977', '1:5182', '1:7988', '1:8500', '1:8501', '1:19081', '1:52991', '1:53115', '1:53357', '1:53516', '1:53533', '1:53680', '1:53703', '1:53775', '1:53776', '1:54056', '1:54153', '1:54295', '1:54302', '1:58905', '1:58939', '1:58963', '1:59161', '1:59171', '1:59203', '1:59356', '1:59413', '1:59461', '1:59567', '1:59582', '1:7625', '1:8030', '1:8422', '1:8592', '1:8995', '1:9024', '1:9055', '1:9152', '1:9238', '1:9250', '1:24069', '1:18318', '1:22651', '1:29119', '1:32774', '1:42263', '1:42963', '1:44123', '1:40031', '1:40728', '1:41097', '1:41274', '1:41329', '1:41404', '1:41743', '1:41749', '1:46849', '1:46980', '1:32430', '1:32449', '1:32679', '1:32675', '1:32702', '1:32800', '1:49155', '1:49664', '1:49794', '1:49033', '1:8311', '1:8426', '1:8435', '1:8518', '1:8697', '1:8719', '1:8720', '1:8775', '1:8842', '1:8899', '1:8984', '1:9028', '1:9199', '1:9246', '1:9287', '1:9345', '1:9356', '1:9502', '1:9671', '1:25974', '1:26814', '1:27041', '1:27098', '1:27130', '1:27133', '1:27174', '1:27219', '1:27229', '1:27291', '1:27303', '1:27164', '1:27205', '1:27221', '1:27319', '1:27326', '1:27350', '1:27415', '1:27446', '1:27488', '1:59276', '1:59533', '1:59931', '1:25907', '1:25997', '1:26676', '1:26692', '1:26783', '1:26927', '1:31153', '1:2313', '1:10725', '1:10806', '1:20252', '1:21421', '1:21820', '1:23222', '1:31004', '1:31289', '1:31674', '1:17492', '1:17842', '1:17991', '1:20069', '1:28331', '1:29043', '1:29554', '1:30651', '1:43533', '1:75656', '1:70152', '1:70456', '1:70531', '1:80602', '1:30083', '1:44172', '1:46539', '1:22767', '1:27267', '1:28656', '1:30091', '1:42230', '1:58770', '1:30400', '1:44397', '1:44414', '1:51669', '1:57452', '1:27670', '1:32212', '1:42516', '1:44177', '1:54360', '1:57663', '1:62049', '1:62299', '1:44709', '1:44733', '1:44820', '1:44977', '1:45216', '1:44725', '1:44806', '1:44824', '1:44910', '1:45232', '1:45613', '1:64515', '1:52978', '1:52031', '1:59760', '1:60036', '1:62064', '1:62591', '1:72737', '1:73749', '1:76912', '1:53144', '1:53411', '1:57652', '1:60604', '1:60863', '1:60887', '1:60902', '1:62082', '1:62137', '1:62163', '1:62341', '1:70572', '1:70578', '1:70698', '1:70731', '1:70777', '1:70883', '1:70994', '1:73671', '1:77103', '1:77110', '1:77138', '1:77287', '1:101148', '1:101195', '1:101438', '1:101956', '1:102030', '1:102294', '1:102972', '1:104568', '1:98184', '1:24472', '1:24488', '1:24523', '1:24650', '1:24651', '1:24785', '1:24815', '1:24821', '1:24895', '1:24923', '1:24975', '1:24984', '1:25601', '1:70990', '1:77983', '1:85349', '1:86303', '1:86527', '1:70209', '1:70880', '1:70981', '1:77904', '1:83788', '1:84069', '1:88151', '1:88260', '1:89037', '1:70381', '1:84169', '1:84712', '1:85034', '1:85811', '1:86354', '1:86610', '1:88378', '1:88387', '1:88662', '1:83112', '1:84970', '1:86430', '1:87611', '1:96670', '1:97498', '1:97584', '1:97635', '1:97719', '1:92549', '1:92631', '1:67312', '1:78259', '1:67818', '1:78061', '1:86858', '1:70988', '1:90451', '1:92075', '1:75522', '1:75829', '1:78154', '1:79730', '1:80429', '1:81338', '1:81643', '1:77182', '1:77536', '1:77649', '1:77734', '1:77746', '1:77798', '1:77860', '1:77884', '1:77916', '1:77997', '1:82014', '1:82054', '1:82063', '1:82142', '1:82525', '1:6178', '1:6855', '1:6194', '1:6205', '1:6416', '1:6443', '1:6643', '1:6749', '1:6752', '1:40630', '1:40646', '1:40664', '1:40605', '1:40633', '1:40639', '1:40660', '1:40666', '1:40700', '1:40716', '1:40731', '1:40746', '1:40842', '1:40844', '1:51934', '1:52118', '1:52403', '1:52508', '1:58697', '1:58899', '1:22104', '1:22136', '1:22465', '1:22524', '1:22641', '1:22706', '1:22738', '1:22795', '1:22819', '1:22665', '1:22713', '1:22811', '1:22971', '1:23365', '1:27235', '1:27325', '1:27472', '1:27505', '1:27571', '1:27704', '1:27806', '1:27935', '1:27959', '1:82243', '1:82600', '1:82711', '1:82722', '1:82996', '1:83247', '1:84019', '1:40239', '1:41835', '1:49396', '1:55217', '1:58637', '1:62962', '1:40070', '1:46104', '1:46685', '1:48145', '1:48338', '1:49634', '1:49998', '1:58580', '1:51851', '1:43335', '1:43431', '1:43491', '1:43606', '1:43732', '1:43912', '1:44081', '1:44193', '1:44196', '1:44241', '1:44244', '1:44249', '1:44293', '1:44301', '1:47541', '1:47624', '1:47635', '1:47685', '1:47701', '1:47781', '1:47787', '1:47760', '1:47815', '1:47828', '1:47919', '1:47982', '1:47989', '1:47991', '1:13038', '1:16808', '1:21180', '1:26315', '1:31370', '1:31862', '1:21120', '1:26983', '1:31342', '1:31905', '1:24112', '1:25124', '1:82856', '1:98368', '1:72069', '1:77106', '1:79475', '1:82338', '1:82605', '1:90285', '1:91464', '1:94968', '1:95174', '1:95321', '1:95975', '1:98232', '1:87968', '1:91412', '1:98679', '1:106099', '1:106230', '1:106269', '1:106337', '1:106351', '1:106362', '1:106406', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6A721CBE-4B07-EA11-9750-0CC47A4D7646.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCF6B8AB-E003-EA11-AAE8-44A842BE8F7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9EAE1061-30F8-E911-B2D5-AC1F6B0F676C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/86727FE6-AF0A-EA11-B38D-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2A16734-8607-EA11-A7C2-0025905A6060.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/723E26E0-88FC-E911-A84F-0CC47AFCC666.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/643155F4-E80A-EA11-BD55-0CC47A7C3636.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC1243A5-AA0A-EA11-A2C9-0CC47A7C347A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24362999-4EFE-E911-BFEB-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1207CE62-4EF9-E911-85E0-C4346BC85718.root']);