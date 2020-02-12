import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:445', '1:453', '1:462', '1:504', '1:553', '1:640', '1:727', '1:19158', '1:18912', '1:18948', '1:19004', '1:19071', '1:19072', '1:19099', '1:19344', '1:21532', '1:103539', '1:104086', '1:21354', '1:96648', '1:103680', '1:103743', '1:46716', '1:46847', '1:46869', '1:46883', '1:46888', '1:46897', '1:46936', '1:48655', '1:50258', '1:85023', '1:80559', '1:80562', '1:80762', '1:76360', '1:15163', '1:15676', '1:15173', '1:21251', '1:26313', '1:20597', '1:32359', '1:37487', '1:76927', '1:28477', '1:19308', '1:19324', '1:19339', '1:19363', '1:19412', '1:19461', '1:80896', '1:63755', '1:63781', '1:63867', '1:69138', '1:69210', '1:69704', '1:72668', '1:73811', '1:71424', '1:71828', '1:30889', '1:31930', '1:52166', '1:47186', '1:47210', '1:55681', '1:55808', '1:57032', '1:60476', '1:62378', '1:67676', '1:67778', '1:67800', '1:71539', '1:73831', '1:32207', '1:32580', '1:32633', '1:32640', '1:76148', '1:78771', '1:47254', '1:47400', '1:47527', '1:66682', '1:73203', '1:78651', '1:79171', '1:79220', '1:79549', '1:4385', '1:57349', '1:59402', '1:58541', '1:58850', '1:59625', '1:58297', '1:60250', '1:60825', '1:62375', '1:58801', '1:77780', '1:77797', '1:77989', '1:82363', '1:84366', '1:84862', '1:78182', '1:78985', '1:83513', '1:82826', '1:82739', '1:84672', '1:86155', '1:90653', '1:101391', '1:101597', '1:101602', '1:88881', '1:94812', '1:86838', '1:88028', '1:85077', '1:86195', '1:91568', '1:93441', '1:89235', '1:86348', '1:93033', '1:89247', '1:89413', '1:89548', '1:89539', '1:101843', '1:101806', '1:3839', '1:2794', '1:3934', '1:74852', '1:74870', '1:77023', '1:77963', '1:76036', '1:76186', '1:31283', '1:31297', '1:30577', '1:30689', '1:30720', '1:65554', '1:74143', '1:89130', '1:7093', '1:15501', '1:15041', '1:15155', '1:15404', '1:16675', '1:19900', '1:11069', '1:30472', '1:30783', '1:47342', '1:25092', '1:25175', '1:25234', '1:25251', '1:31092', '1:31422', '1:31186', '1:101162', '1:101617', '1:90270', '1:101913', '1:56753', '1:101556', '1:11234', '1:11339', '1:11377', '1:13229', '1:13667', '1:13144', '1:25291', '1:31120', '1:31302', '1:60504', '1:61560', '1:63671', '1:22269', '1:20111', '1:39665', '1:52759', '1:53695', '1:47280', '1:56875', '1:56982', '1:59047', '1:59078', '1:58923', '1:54981', '1:54988', '1:55147', '1:79183', '1:79281', '1:82229', '1:82772', '1:75865', '1:75882', '1:75905', '1:75946', '1:76099', '1:76222', '1:77483', '1:77719', '1:90357', '1:90499', '1:90307', '1:90318', '1:101532', '1:28111', '1:34715', '1:52512', '1:46737', '1:45231', '1:39032', '1:39098', '1:39111', '1:39146', '1:63116', '1:47948', '1:51005', '1:51143', '1:55047', '1:75066', '1:75067', '1:75395', '1:75980', '1:72590', '1:65361', '1:71457', '1:73068', '1:65356', '1:66949', '1:66989', '1:69934', '1:72338', '1:72684', '1:81369', '1:72189', '1:74160', '1:76263', '1:76646', '1:78117', '1:78659', '1:78664', '1:78781', '1:11306', '1:13883', '1:31059', '1:13221', '1:13895', '1:13894', '1:22812', '1:22824', '1:22851', '1:22802', '1:22832', '1:22843', '1:22885', '1:59828', '1:56180', '1:63229', '1:89034', '1:89078', '1:89179', '1:89488', '1:89016', '1:89017', '1:89018', '1:89042', '1:89087', '1:103004', '1:103154', '1:103188', '1:2066', '1:3600', '1:7029', '1:93218', '1:102530', '1:103632', '1:103324', '1:104921', '1:19450', '1:25438', '1:25493', '1:25531', '1:31776', '1:29088', '1:89188', '1:101168', '1:25254', '1:25355', '1:25364', '1:66876', '1:71870', '1:72140', '1:72376', '1:22759', '1:24708', '1:31277', '1:31769', '1:31794', '1:31893', '1:31951', '1:32349', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E121475-8F16-EA11-8E04-A0369FE2C0B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/30928809-BC17-EA11-BB9F-FA163EB84C2E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/4E9AEF96-7917-EA11-924F-FA163EFE3C83.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3800FB9D-1118-EA11-AEEA-FA163E3C6BCA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA02D583-D717-EA11-8AB6-AC1F6B8DD1F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E962FC4-1218-EA11-A4E7-008CFA1983BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/18F8D4AE-5818-EA11-AC1B-002590DC0352.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6CF856BA-FF16-EA11-9606-AC1F6B0DE2E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8EE12E36-9617-EA11-B775-FA163ED521CB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54894913-D216-EA11-8F84-A0369FF88246.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1685CFE4-5118-EA11-95CB-003048F2E8C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8AC2DDFC-8E17-EA11-A339-FA163E5AB700.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/386B181A-9017-EA11-A440-5065F3816251.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2A1CF336-1318-EA11-B91E-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/48B048F8-9017-EA11-B603-FA163E7ED2D2.root']);