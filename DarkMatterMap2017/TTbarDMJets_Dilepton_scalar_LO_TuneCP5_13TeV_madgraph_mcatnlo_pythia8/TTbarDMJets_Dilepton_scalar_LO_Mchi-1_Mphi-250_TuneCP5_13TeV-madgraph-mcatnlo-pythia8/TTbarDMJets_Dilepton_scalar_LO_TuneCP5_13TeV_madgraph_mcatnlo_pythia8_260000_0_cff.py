import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:262', '1:315', '1:690', '1:708', '1:711', '1:6781', '1:18877', '1:19035', '1:19456', '1:103615', '1:102654', '1:103696', '1:103727', '1:103735', '1:46792', '1:46863', '1:47056', '1:47421', '1:46935', '1:47429', '1:48074', '1:48237', '1:50385', '1:50143', '1:50341', '1:80579', '1:80513', '1:80582', '1:80747', '1:104410', '1:2718', '1:3847', '1:5377', '1:15122', '1:16136', '1:16678', '1:76022', '1:76296', '1:14304', '1:15992', '1:16686', '1:15872', '1:15977', '1:17594', '1:18630', '1:26296', '1:28199', '1:27258', '1:26450', '1:81973', '1:19352', '1:19801', '1:19416', '1:19438', '1:80996', '1:63725', '1:66314', '1:65253', '1:70955', '1:66755', '1:30510', '1:30902', '1:51675', '1:52837', '1:47081', '1:47184', '1:46709', '1:55695', '1:62798', '1:63280', '1:63742', '1:67212', '1:67503', '1:67880', '1:59948', '1:70524', '1:69521', '1:72100', '1:73376', '1:73952', '1:32249', '1:32559', '1:32574', '1:32597', '1:76135', '1:76765', '1:61749', '1:61919', '1:62210', '1:66423', '1:80079', '1:77568', '1:1881', '1:1912', '1:4035', '1:4517', '1:4631', '1:4834', '1:59400', '1:59415', '1:58776', '1:58808', '1:59201', '1:79933', '1:82023', '1:82146', '1:84297', '1:84349', '1:79124', '1:81615', '1:82137', '1:79873', '1:85601', '1:94030', '1:84794', '1:82155', '1:82203', '1:101518', '1:101651', '1:101915', '1:93200', '1:83775', '1:88392', '1:91573', '1:86411', '1:88143', '1:88814', '1:86553', '1:86629', '1:91977', '1:93165', '1:87178', '1:91525', '1:93364', '1:89225', '1:89062', '1:89200', '1:89433', '1:89547', '1:101837', '1:101834', '1:97689', '1:2120', '1:2336', '1:2350', '1:3855', '1:3970', '1:74878', '1:75414', '1:76404', '1:72423', '1:76110', '1:76215', '1:31039', '1:31199', '1:31292', '1:31310', '1:31325', '1:31532', '1:30340', '1:30590', '1:78248', '1:89128', '1:15755', '1:16221', '1:12886', '1:33724', '1:37369', '1:30415', '1:30441', '1:30491', '1:57578', '1:63517', '1:63522', '1:67308', '1:25221', '1:25309', '1:30610', '1:30168', '1:31086', '1:31181', '1:31209', '1:31350', '1:90261', '1:101318', '1:101650', '1:90182', '1:90187', '1:90116', '1:44400', '1:56696', '1:60285', '1:62751', '1:90131', '1:101674', '1:11250', '1:11373', '1:25696', '1:22569', '1:17467', '1:29788', '1:31003', '1:31036', '1:31085', '1:31123', '1:31252', '1:62033', '1:62073', '1:63634', '1:11386', '1:15692', '1:28717', '1:34304', '1:39088', '1:49660', '1:49051', '1:56022', '1:47367', '1:58407', '1:52781', '1:62229', '1:53929', '1:53931', '1:54009', '1:54088', '1:55123', '1:81353', '1:79215', '1:76023', '1:75884', '1:75954', '1:76194', '1:76164', '1:77455', '1:77570', '1:90281', '1:90095', '1:90512', '1:90537', '1:52573', '1:36899', '1:38201', '1:39009', '1:39025', '1:39085', '1:39114', '1:39130', '1:39154', '1:48210', '1:51894', '1:52355', '1:39958', '1:49737', '1:40752', '1:44366', '1:50123', '1:49607', '1:75117', '1:75687', '1:77055', '1:72973', '1:71513', '1:74239', '1:74730', '1:76004', '1:81166', '1:80280', '1:11103', '1:11197', '1:11215', '1:11218', '1:11257', '1:13909', '1:13545', '1:22606', '1:22752', '1:22777', '1:22786', '1:22859', '1:22631', '1:22485', '1:58065', '1:59888', '1:62026', '1:62327', '1:89472', '1:89495', '1:103095', '1:103112', '1:103123', '1:103271', '1:103455', '1:2179', '1:3223', '1:96845', '1:99920', '1:102619', '1:102597', '1:99227', '1:25429', '1:25534', '1:25537', '1:29886', '1:31796', '1:31780', '1:25358', '1:25363', '1:25425', '1:34699', '1:29838', '1:70576', '1:72370', '1:72500', '1:72515', '1:73496', '1:73887', '1:21081', '1:25299', '1:25846', '1:24721', '1:24346', '1:24851', '1:32575', '1:33226', '1:34254', '1:31660', '1:31946', '1:31975', '1:31987', '1:32503', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E121475-8F16-EA11-8E04-A0369FE2C0B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/30928809-BC17-EA11-BB9F-FA163EB84C2E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/4E9AEF96-7917-EA11-924F-FA163EFE3C83.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3800FB9D-1118-EA11-AEEA-FA163E3C6BCA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA02D583-D717-EA11-8AB6-AC1F6B8DD1F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E962FC4-1218-EA11-A4E7-008CFA1983BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/18F8D4AE-5818-EA11-AC1B-002590DC0352.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6CF856BA-FF16-EA11-9606-AC1F6B0DE2E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8EE12E36-9617-EA11-B775-FA163ED521CB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54894913-D216-EA11-8F84-A0369FF88246.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1685CFE4-5118-EA11-95CB-003048F2E8C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8AC2DDFC-8E17-EA11-A339-FA163E5AB700.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/386B181A-9017-EA11-A440-5065F3816251.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2A1CF336-1318-EA11-B91E-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/48B048F8-9017-EA11-B603-FA163E7ED2D2.root']);