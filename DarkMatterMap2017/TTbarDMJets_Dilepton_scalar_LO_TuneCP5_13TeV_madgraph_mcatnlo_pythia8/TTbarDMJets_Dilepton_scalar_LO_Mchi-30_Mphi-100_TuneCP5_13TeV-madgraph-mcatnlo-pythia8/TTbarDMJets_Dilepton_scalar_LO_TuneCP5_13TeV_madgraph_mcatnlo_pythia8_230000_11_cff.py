import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:55000', '1:55035', '1:55331', '1:55361', '1:55375', '1:55429', '1:57148', '1:57201', '1:57261', '1:57509', '1:57522', '1:57526', '1:57535', '1:57551', '1:70339', '1:70392', '1:70406', '1:70455', '1:70462', '1:70531', '1:71188', '1:71193', '1:61492', '1:61763', '1:62020', '1:61743', '1:82186', '1:82055', '1:82072', '1:82237', '1:82337', '1:82529', '1:82565', '1:85017', '1:85032', '1:10670', '1:12447', '1:17974', '1:18024', '1:18170', '1:18283', '1:18292', '1:18426', '1:18488', '1:18677', '1:20403', '1:34735', '1:50762', '1:50861', '1:51488', '1:50576', '1:50621', '1:79102', '1:82179', '1:83937', '1:83050', '1:85097', '1:80664', '1:83049', '1:83132', '1:83303', '1:83586', '1:87575', '1:87591', '1:87645', '1:87750', '1:87797', '1:87970', '1:88011', '1:92267', '1:93452', '1:93533', '1:93549', '1:8444', '1:8858', '1:12766', '1:14565', '1:15736', '1:16454', '1:15689', '1:15801', '1:39940', '1:44763', '1:48362', '1:49215', '1:50234', '1:49679', '1:86584', '1:94244', '1:103447', '1:85839', '1:88412', '1:93693', '1:91597', '1:103108', '1:96966', '1:12279', '1:66785', '1:70001', '1:70019', '1:70020', '1:68036', '1:68291', '1:68378', '1:68776', '1:74265', '1:71990', '1:72040', '1:72094', '1:72107', '1:72129', '1:72164', '1:72134', '1:75457', '1:75482', '1:77362', '1:74166', '1:74210', '1:74214', '1:79692', '1:91122', '1:94361', '1:94391', '1:92175', '1:92763', '1:92796', '1:1294', '1:1873', '1:331', '1:4677', '1:4523', '1:10304', '1:10838', '1:51980', '1:7539', '1:7312', '1:10002', '1:12229', '1:12442', '1:12465', '1:35953', '1:37642', '1:35518', '1:35820', '1:38170', '1:48426', '1:49596', '1:50720', '1:50763', '1:93039', '1:93130', '1:2643', '1:3338', '1:38212', '1:42518', '1:38087', '1:44323', '1:47668', '1:47724', '1:47808', '1:47866', '1:47906', '1:44988', '1:47352', '1:47594', '1:42818', '1:42843', '1:42911', '1:42968', '1:47552', '1:47786', '1:64545', '1:75343', '1:8036', '1:8161', '1:8764', '1:8799', '1:10414', '1:55791', '1:56197', '1:60579', '1:69871', '1:63013', '1:63143', '1:63249', '1:67103', '1:67242', '1:85742', '1:87603', '1:98086', '1:104204', '1:104576', '1:85900', '1:97702', '1:106135', '1:96416', '1:2034', '1:2415', '1:2427', '1:2439', '1:2489', '1:2951', '1:3275', '1:3277', '1:3340', '1:3462', '1:3496', '1:3579', '1:3723', '1:3976', '1:9768', '1:4363', '1:4377', '1:7692', '1:7780', '1:68566', '1:70065', '1:83347', '1:83387', '1:91715', '1:97204', '1:97236', '1:97274', '1:105407', '1:105429', '1:2876', '1:5255', '1:5488', '1:5559', '1:5620', '1:5704', '1:5542', '1:17311', '1:17375', '1:17589', '1:18047', '1:18077', '1:18192', '1:18083', '1:18316', '1:26789', '1:32903', '1:33301', '1:33813', '1:36873', '1:8053', '1:12641', '1:8626', '1:10355', '1:52425', '1:52481', '1:53377', '1:69927', '1:5080', '1:5250', '1:5282', '1:5430', '1:5578', '1:3445', '1:3450', '1:3498', '1:3541', '1:3568', '1:3570', '1:3705', '1:3719', '1:4013', '1:12577', '1:8955', '1:10081', '1:8399', '1:8473', '1:8622', '1:10001', '1:8195', '1:36335', '1:36758', '1:40157', '1:40187', '1:40241', '1:40461', '1:39198', '1:39206', '1:39388', '1:49162', '1:54375', '1:54411', '1:54489', '1:54497', '1:54543', '1:9847', '1:9927', '1:10182', '1:10497', '1:14039', '1:10878', '1:9007', '1:9100', '1:10908', '1:58032', '1:622', '1:3262', '1:2102', '1:2833', '1:3921', '1:39523', '1:44897', '1:50161', '1:40796', '1:49178', '1:41652', '1:41770', '1:50412', '1:41750', '1:48371', '1:102569', '1:103113', '1:103661', '1:105161', '1:4530', '1:4688', '1:4705', '1:4722', '1:4748', '1:4817', '1:4824', '1:26400', '1:26428', '1:26647', '1:35074', '1:35075', '1:24059', '1:24148', '1:24528', '1:24669', '1:24744', '1:24786', '1:34390', '1:34476', '1:34505', '1:34511', '1:34555', '1:34586', '1:43022', '1:36093', '1:47999', '1:73904', '1:73943', '1:73961', '1:74003', '1:74026', '1:102010', '1:102075', '1:102154', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E2848B0E-44F2-E911-825D-509A4C9F8ADB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BEF0CDD4-E4F6-E911-83C1-0CC47A0AD6FC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/16FBEA03-EAF2-E911-B29A-44A842BECCB1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F83A579D-8B01-EA11-AABA-00259073E45A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/20F66F39-4203-EA11-A2F6-405CFDFF481B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4AA2791D-9EF2-E911-8C38-3417EBE74303.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96CDDC18-A20E-EA11-A3B2-00266CFFBF88.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/982A8027-7FEE-E911-B6C3-089E0158CD57.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4EE87D2-0B09-EA11-92AB-00266CF3E174.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C5B6E03-5CFF-E911-B90B-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D26BC5FF-970A-EA11-95B5-0CC47A4D7666.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AA873AAA-B402-EA11-9A84-0025905C9742.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B20562A7-710E-EA11-8BD4-0CC47A78A478.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4A15B08-AFEE-E911-9943-8CDCD4A99E08.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/529ABEDC-6210-EA11-9BFF-506B4BF38280.root']);