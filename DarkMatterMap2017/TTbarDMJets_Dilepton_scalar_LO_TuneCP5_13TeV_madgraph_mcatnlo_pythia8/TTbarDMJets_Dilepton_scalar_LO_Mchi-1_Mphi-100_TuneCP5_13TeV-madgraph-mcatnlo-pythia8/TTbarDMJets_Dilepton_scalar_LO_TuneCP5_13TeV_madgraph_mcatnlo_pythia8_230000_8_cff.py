import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:411', '1:1574', '1:1811', '1:15953', '1:17798', '1:18108', '1:105049', '1:105036', '1:105077', '1:105102', '1:105115', '1:105138', '1:105156', '1:105196', '1:105198', '1:105335', '1:105248', '1:96399', '1:103468', '1:104172', '1:14784', '1:14928', '1:14932', '1:14946', '1:14978', '1:16028', '1:16147', '1:16308', '1:79227', '1:79228', '1:79009', '1:79018', '1:79097', '1:79156', '1:79231', '1:79299', '1:96289', '1:96320', '1:96347', '1:96494', '1:96932', '1:96226', '1:96240', '1:96680', '1:96739', '1:60344', '1:59587', '1:59819', '1:59829', '1:59655', '1:84460', '1:84666', '1:84731', '1:84763', '1:84784', '1:84814', '1:96285', '1:96293', '1:96343', '1:96370', '1:91226', '1:91227', '1:91238', '1:91747', '1:91772', '1:91828', '1:91861', '1:80809', '1:81019', '1:81110', '1:81400', '1:80877', '1:81430', '1:81448', '1:81535', '1:96228', '1:96249', '1:96372', '1:96524', '1:96545', '1:96777', '1:96860', '1:96938', '1:97013', '1:97161', '1:98917', '1:98936', '1:91365', '1:91535', '1:91617', '1:91869', '1:91891', '1:91918', '1:92049', '1:99735', '1:99778', '1:33192', '1:33501', '1:34991', '1:37149', '1:37636', '1:33866', '1:34011', '1:34067', '1:34564', '1:34919', '1:47087', '1:47471', '1:47632', '1:47699', '1:47802', '1:47878', '1:56618', '1:78400', '1:84917', '1:83281', '1:88064', '1:78203', '1:78311', '1:79818', '1:82864', '1:85427', '1:71508', '1:76052', '1:78603', '1:80330', '1:97153', '1:83965', '1:14614', '1:15138', '1:15285', '1:15397', '1:15418', '1:15445', '1:15462', '1:15467', '1:15808', '1:17479', '1:18196', '1:27003', '1:27226', '1:27246', '1:27286', '1:27293', '1:27296', '1:27342', '1:27416', '1:28275', '1:28278', '1:28397', '1:41482', '1:41532', '1:41601', '1:48131', '1:15286', '1:18132', '1:18514', '1:18472', '1:19809', '1:19823', '1:19837', '1:19918', '1:19953', '1:21327', '1:21646', '1:21816', '1:24261', '1:24967', '1:17412', '1:16902', '1:28754', '1:33023', '1:33359', '1:26895', '1:33035', '1:33469', '1:32897', '1:32913', '1:33028', '1:27805', '1:27802', '1:19958', '1:19963', '1:20785', '1:20850', '1:20915', '1:20852', '1:20891', '1:20893', '1:20966', '1:21071', '1:21108', '1:21165', '1:21121', '1:49685', '1:49689', '1:40313', '1:40401', '1:40413', '1:40421', '1:40429', '1:40462', '1:40644', '1:40696', '1:40848', '1:40971', '1:43546', '1:43563', '1:60573', '1:60631', '1:61481', '1:61443', '1:61447', '1:41084', '1:41108', '1:41110', '1:41118', '1:41147', '1:41161', '1:41200', '1:41205', '1:41223', '1:41229', '1:41274', '1:41289', '1:41328', '1:41373', '1:41477', '1:41523', '1:41488', '1:44476', '1:46030', '1:46314', '1:46722', '1:46690', '1:47164', '1:48169', '1:48173', '1:48174', '1:48192', '1:48254', '1:48298', '1:48668', '1:3406', '1:4025', '1:4115', '1:4130', '1:4180', '1:4187', '1:4222', '1:4227', '1:16008', '1:16056', '1:16135', '1:16154', '1:16173', '1:49197', '1:45759', '1:45792', '1:45806', '1:45818', '1:46000', '1:46127', '1:47675', '1:47687', '1:47794', '1:47939', '1:51874', '1:51962', '1:52828', '1:66380', '1:70061', '1:71055', '1:64681', '1:64698', '1:64727', '1:64801', '1:64836', '1:64850', '1:64895', '1:64987', '1:67014', '1:64990', '1:65007', '1:65109', '1:65110', '1:65159', '1:65220', '1:65225', '1:80703', '1:80728', '1:81639', '1:84132', '1:84135', '1:84180', '1:83534', '1:85376', '1:85383', '1:85401', '1:85407', '1:85704', '1:85848', '1:85860', '1:86844', '1:86267', '1:86380', '1:86578', '1:86668', '1:86721', '1:86734', '1:86775', '1:97117', '1:105690', '1:105756', '1:105757', '1:105769', '1:105700', '1:24540', '1:24561', '1:26473', '1:26490', '1:26746', '1:26848', '1:28022', '1:28086', '1:28401', '1:28801', '1:32103', '1:32314', '1:32320', '1:32544', '1:32839', '1:32875', '1:32904', '1:28289', '1:77830', '1:28491', '1:28523', '1:28858', '1:32722', '1:32896', '1:32944', '1:34150', '1:34588', '1:100238', '1:70862', '1:70876', '1:71294', '1:71528', '1:71517', '1:76367', '1:79614', '1:80090', '1:83131', '1:85218', '1:96792', '1:106199', '1:2049', '1:3095', '1:3289', '1:3368', '1:3898', '1:4424', '1:4697', '1:4701', '1:4952', '1:1284', '1:4429', '1:15364', '1:15616', '1:16444', '1:17335', '1:17562', '1:18034', '1:18445', '1:20594', '1:20627', '1:21468', '1:24565', '1:24576', '1:26533', '1:27686', '1:26124', '1:32446', '1:34543', '1:37043', '1:28192', '1:32557', '1:37035', '1:26126', '1:32674', '1:32704', '1:34722', '1:35134', '1:35905', '1:38720', '1:32088', '1:34526', '1:34582', '1:33216', '1:36039', '1:36962', '1:38334', '1:46518', '1:33069', '1:36850', '1:45850', '1:87837', '1:88490', '1:94697', '1:91955', '1:91923', '1:95203', '1:95959', '1:96077', '1:96462', '1:38530', '1:40580', '1:43397', '1:43638', '1:45488', '1:42092', '1:42566', '1:43798', '1:28551', '1:33206', '1:33585', '1:33772', '1:32672', '1:53207', '1:53214', '1:51035', '1:51094', '1:51746', '1:52041', '1:52058', '1:52315', '1:49834', '1:50691', '1:33767', '1:41835', '1:47612', '1:39352', '1:40372', '1:61840', '1:62502', '1:62973', '1:63977', '1:67448', '1:58427', '1:58822', '1:59408', '1:59787', '1:60336', '1:56798', '1:57257', '1:76542', '1:75674', '1:75763', '1:76269', '1:77294', '1:91633', '1:99782', '1:99815', '1:103888', '1:103967', '1:104789', '1:5339', '1:5368', '1:5722', '1:5911', '1:7044', '1:7083', '1:7102', '1:7114', '1:8705', '1:10423', '1:10430', '1:10432', '1:10455', '1:10486', '1:10487', '1:10501', '1:10504', '1:10568', '1:10586', '1:10416', '1:10557', '1:12321', '1:12336', '1:12353', '1:12355', '1:12358', '1:12418', '1:14416', '1:14936', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E25E124-31F7-E911-BE4E-0CC47A1E0DC2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCE60212-4D10-EA11-BEE3-90E2BAD5729C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C9C3A0A-7FFF-E911-8CD0-0CC47A4DEDD4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90D49EF7-13F6-E911-9659-38EAA78E2C94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D8B5CBBC-35F0-E911-94CF-1418774A25AB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E06943C6-D5EF-E911-A278-10983627C3C1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1ABC4644-64F4-E911-A4E7-FA163E84EE9A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AF65E7A-6EF3-E911-9E38-141877641875.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0A2F042B-71EF-E911-9535-0CC47AF9739E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AA4C6F18-8AF7-E911-80DC-0CC47AD9901C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5EAB8AB1-6810-EA11-9F96-008CFA197D98.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/10AE8E18-9802-EA11-8C36-B083FED138B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0407705F-5610-EA11-BCA2-0CC47AD98CEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5E63A65D-5B07-EA11-9816-0CC47A7C345E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EA78600-8003-EA11-98EB-405CFDFF480E.root']);