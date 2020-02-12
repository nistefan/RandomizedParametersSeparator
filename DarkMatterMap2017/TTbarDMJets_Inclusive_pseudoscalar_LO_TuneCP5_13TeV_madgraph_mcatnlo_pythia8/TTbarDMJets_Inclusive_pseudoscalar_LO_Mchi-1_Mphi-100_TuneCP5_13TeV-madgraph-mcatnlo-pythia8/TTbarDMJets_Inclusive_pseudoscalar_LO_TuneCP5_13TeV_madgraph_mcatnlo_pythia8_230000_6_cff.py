import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:30951', '1:30959', '1:32058', '1:32658', '1:32666', '1:32733', '1:32544', '1:32577', '1:32598', '1:32606', '1:32633', '1:32660', '1:32674', '1:32887', '1:32908', '1:32950', '1:39683', '1:70071', '1:70564', '1:70629', '1:77171', '1:77295', '1:77383', '1:77553', '1:77641', '1:78960', '1:78992', '1:82110', '1:81560', '1:81641', '1:81826', '1:81852', '1:81942', '1:81949', '1:84545', '1:84756', '1:90287', '1:82807', '1:84980', '1:85343', '1:85625', '1:85728', '1:85901', '1:85989', '1:88998', '1:91054', '1:91156', '1:91912', '1:92460', '1:105228', '1:105367', '1:82929', '1:83190', '1:84082', '1:84092', '1:84317', '1:84351', '1:84543', '1:83179', '1:83313', '1:83367', '1:83440', '1:83535', '1:83500', '1:83875', '1:83886', '1:97216', '1:83835', '1:86255', '1:86480', '1:86503', '1:86551', '1:86637', '1:86650', '1:86893', '1:86951', '1:87053', '1:87065', '1:87078', '1:87185', '1:87227', '1:87344', '1:90116', '1:91399', '1:87251', '1:90318', '1:90477', '1:92752', '1:88573', '1:88771', '1:89077', '1:89432', '1:92761', '1:93401', '1:93747', '1:93885', '1:94009', '1:94176', '1:94415', '1:94086', '1:94519', '1:95360', '1:95537', '1:95613', '1:95777', '1:95895', '1:95959', '1:94850', '1:15861', '1:15975', '1:15987', '1:16445', '1:16940', '1:31504', '1:31522', '1:31661', '1:16741', '1:16883', '1:16896', '1:16908', '1:16944', '1:16987', '1:22644', '1:22873', '1:22887', '1:27007', '1:27023', '1:27079', '1:27080', '1:27299', '1:27404', '1:27412', '1:27428', '1:51333', '1:101753', '1:101933', '1:102010', '1:102285', '1:102300', '1:101940', '1:101970', '1:104868', '1:54082', '1:54184', '1:54200', '1:54265', '1:54304', '1:54314', '1:54324', '1:54352', '1:54551', '1:54557', '1:76594', '1:76595', '1:76726', '1:80011', '1:80075', '1:78025', '1:78085', '1:78209', '1:78263', '1:78456', '1:78491', '1:78499', '1:78628', '1:78630', '1:85327', '1:85829', '1:85837', '1:88087', '1:88137', '1:88139', '1:88987', '1:89143', '1:89151', '1:18514', '1:18559', '1:18614', '1:18622', '1:18641', '1:18703', '1:18729', '1:18798', '1:18800', '1:18806', '1:18884', '1:18900', '1:18916', '1:18966', '1:22019', '1:22027', '1:22033', '1:22400', '1:22164', '1:22196', '1:22203', '1:22242', '1:22415', '1:22422', '1:22529', '1:22157', '1:22190', '1:22200', '1:22277', '1:22451', '1:22581', '1:22588', '1:29059', '1:29440', '1:29446', '1:73007', '1:73028', '1:73096', '1:73254', '1:73377', '1:76288', '1:76296', '1:39418', '1:39533', '1:39687', '1:39757', '1:39776', '1:39822', '1:39849', '1:39850', '1:39969', '1:42063', '1:42064', '1:42115', '1:79874', '1:43228', '1:43349', '1:44113', '1:43300', '1:43302', '1:43323', '1:43337', '1:43340', '1:43348', '1:43353', '1:43356', '1:43391', '1:43409', '1:43427', '1:43444', '1:43528', '1:43545', '1:53633', '1:76207', '1:76469', '1:76174', '1:76176', '1:76308', '1:76314', '1:76323', '1:76340', '1:76362', '1:76370', '1:2129', '1:5095', '1:9032', '1:12863', '1:14746', '1:5050', '1:7499', '1:14145', '1:21450', '1:5917', '1:14427', '1:20898', '1:21146', '1:26754', '1:95531', '1:70799', '1:71803', '1:71907', '1:79095', '1:82361', '1:85655', '1:87188', '1:93007', '1:89448', '1:94230', '1:95291', '1:95494', '1:87816', '1:70165', '1:84941', '1:70667', '1:77729', '1:82080', '1:89292', '1:42134', '1:42224', '1:42216', '1:42302', '1:42323', '1:42331', '1:42509', '1:42690', '1:42724', '1:46833', '1:48546', '1:51005', '1:51021', '1:51035', '1:51040', '1:51064', '1:51134', '1:51151', '1:51156', '1:51205', '1:51216', '1:51236', '1:51270', '1:47391', '1:47440', '1:47441', '1:47495', '1:47498', '1:47502', '1:47564', '1:47650', '1:47672', '1:47700', '1:47713', '1:47723', '1:48760', '1:48879', '1:52578', '1:54366', '1:55030', '1:55233', '1:55289', '1:49378', '1:51358', '1:87015', '1:87283', '1:84830', '1:85187', '1:85791', '1:85869', '1:86875', '1:87005', '1:87760', '1:87846', '1:90339', '1:90345', '1:92491', '1:101002', '1:101338', '1:101641', '1:101690', '1:101740', '1:101773', '1:101820', '1:101991', '1:102346', '1:102601', '1:102731', '1:104272', '1:104298', '1:104313', '1:104345', '1:101149', '1:102955', '1:102822', '1:104361', '1:104634', '1:102355', '1:102717', '1:102758', '1:102766', '1:102910', '1:47223', '1:47229', '1:47605', '1:47844', '1:47804', '1:52071', '1:52072', '1:52327', '1:52465', '1:52466', '1:81139', '1:67686', '1:90847', '1:105647', '1:106027', '1:106107', '1:106312', '1:106359', '1:106393', '1:106417', '1:106423', '1:106426', '1:82040', '1:82293', '1:79483', '1:79606', '1:86992', '1:87266', '1:87542', '1:91292', '1:91000', '1:92142', '1:93822', '1:95732', '1:95742', '1:96149', '1:96118', '1:97009', '1:97260', '1:96812', '1:96818', '1:96824', '1:96834', '1:96923', '1:97241', '1:97379', '1:97464', '1:97554', '1:97604', '1:98230', '1:98256', '1:98289', '1:103253', '1:103275', '1:103381', '1:103506', '1:103242', '1:103258', '1:103281', '1:103322', '1:103385', '1:103390', '1:103442', '1:103450', '1:103493', '1:96766', '1:30987', '1:41180', '1:42768', '1:46661', '1:48772', '1:56220', '1:56366', '1:56382', '1:56883', '1:57025', '1:19867', '1:27112', '1:31527', '1:39643', '1:39653', '1:39732', '1:42407', '1:42518', '1:42772', '1:44497', '1:47077', '1:32257', '1:47479', '1:53383', '1:54482', '1:54806', '1:57286', '1:57517', '1:60197', '1:51443', '1:52844', '1:55625', '1:64008', '1:64120', '1:64194', '1:67963', '1:73399', '1:54946', '1:67650', '1:78275', '1:75780', '1:67891', '1:71075', '1:71102', '1:71107', '1:71183', '1:71222', '1:71334', '1:71448', '1:25314', '1:32547', '1:32646', '1:39086', '1:42431', '1:64235', '1:79232', '1:85932', '1:90755', '1:29582', '1:29733', '1:29857', '1:30717', '1:32007', '1:30612', '1:30864', '1:47872', '1:86971', '1:67260', '1:67989', '1:75988', '1:92540', '1:96329', '1:79659', '1:85006', '1:90419', '1:93186', '1:93209', '1:88424', '1:65127', '1:90230', '1:96807', '1:95599', '1:67924', '1:71256', '1:71337', '1:71274', '1:102641', '1:104765', '1:104873', '1:61296', '1:61769', '1:61806', '1:61815', '1:61931', '1:62229', '1:70554', '1:70652', '1:70735', '1:70746', '1:70800', '1:70914', '1:70968', '1:72759', '1:73396', '1:73403', '1:73997', '1:74292', '1:74459', '1:74765', '1:77060', '1:87529', '1:87844', '1:88046', '1:88179', '1:88261', '1:88351', '1:88385', '1:88463', '1:88821', '1:88861', '1:89160', '1:89227', '1:91648', '1:15374', '1:20995', '1:24028', '1:24179', '1:25344', '1:25563', '1:27192', '1:29434', '1:39614', '1:45508', '1:45873', '1:52167', '1:53589', '1:56732', '1:9155', '1:9537', '1:9625', '1:9641', '1:9690', '1:10149', '1:10287', '1:10555', '1:10798', '1:10952', '1:64573', '1:72273', '1:73559', '1:73681', '1:65253', '1:65368', '1:66195', '1:13625', '1:16658', '1:16820', '1:23826', '1:25114', '1:25862', '1:26006', '1:26347', '1:13640', '1:13909', '1:14068', '1:14206', '1:16335', '1:23019', '1:23140', '1:23647', '1:23860', '1:23885', '1:23966', '1:25341', '1:25351', '1:26298', '1:26330', '1:62135', '1:75709', '1:80108', '1:52471', '1:52655', '1:52767', '1:52851', '1:52964', '1:52986', '1:53023', '1:53089', '1:53131', '1:53153', '1:53176', '1:53207', '1:53235', '1:53250', '1:53314', '1:53453', '1:53517', '1:53580', '1:65169', '1:64599', '1:64707', '1:64720', '1:64796', '1:64888', '1:64929', '1:65001', '1:65151', '1:65202', '1:65459', '1:65468', '1:1544', '1:1602', '1:1726', '1:1805', '1:1928', '1:1989', '1:2002', '1:2121', '1:2603', '1:2891', '1:3536', '1:23045', '1:23172', '1:7652', '1:7924', '1:8393', '1:8539', '1:8548', '1:8607', '1:8664', '1:8787', '1:8808', '1:8923', '1:9177', '1:9270', '1:9340', '1:9372', '1:9410', '1:9613', '1:10022', '1:10795', '1:11014', '1:11265', '1:24245', '1:24265', '1:24397', '1:24537', '1:24540', '1:24615', '1:4530', '1:5204', '1:5238', '1:5303', '1:5374', '1:5383', '1:5425', '1:5568', '1:5747', '1:5750', '1:5658', '1:5723', '1:5843', '1:5853', '1:5929', '1:23410', '1:23669', '1:23750', '1:23897', '1:23902', '1:24039', '1:24053', '1:24218', '1:25025', '1:24250', '1:24718', '1:24902', '1:25050', '1:27066', '1:27548', '1:27432', '1:27553', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/509597B0-AEFB-E911-878E-002590DE3A92.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90776FDE-BDFB-E911-84D1-40F2E9C6ADBA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F6B93E96-C5FB-E911-9974-3417EBE7047A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BA100FA2-4EFE-E911-96A3-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F43443B4-ECFC-E911-BEB6-24BE05C4D8F1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BAA9281E-48FE-E911-B284-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/82DC5317-C9FE-E911-A8D4-0030487BB52E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A904563-4D00-EA11-8187-002481CFE1EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B29D7EA4-74FF-E911-97CA-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/56EB785D-ADFE-E911-8744-0CC47A5FC281.root']);