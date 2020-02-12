import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1809', '1:1996', '1:4226', '1:2484', '1:2925', '1:9242', '1:9329', '1:10183', '1:12703', '1:21522', '1:17826', '1:17837', '1:18476', '1:18739', '1:18753', '1:8584', '1:8919', '1:16217', '1:16244', '1:16656', '1:17876', '1:27813', '1:105065', '1:105039', '1:105105', '1:105169', '1:105187', '1:105237', '1:105239', '1:105349', '1:105352', '1:96220', '1:96654', '1:102214', '1:105016', '1:16053', '1:16080', '1:16117', '1:16142', '1:16179', '1:16369', '1:16606', '1:16643', '1:24075', '1:24627', '1:28179', '1:28718', '1:79194', '1:79063', '1:79069', '1:79082', '1:79104', '1:79134', '1:79195', '1:79286', '1:79316', '1:79317', '1:79388', '1:79406', '1:96323', '1:96415', '1:96435', '1:96458', '1:96937', '1:96600', '1:96649', '1:96674', '1:96931', '1:59511', '1:59745', '1:59763', '1:60004', '1:60388', '1:60393', '1:59582', '1:59769', '1:59777', '1:59837', '1:59858', '1:59867', '1:59664', '1:61978', '1:62465', '1:84451', '1:84477', '1:84599', '1:84700', '1:84758', '1:84760', '1:84816', '1:84840', '1:84873', '1:84888', '1:96258', '1:96346', '1:96349', '1:96363', '1:91755', '1:91831', '1:91843', '1:91858', '1:91863', '1:81291', '1:81335', '1:81343', '1:81368', '1:81376', '1:80816', '1:80852', '1:80875', '1:80998', '1:81478', '1:96219', '1:96242', '1:96308', '1:96390', '1:96437', '1:96561', '1:97010', '1:97078', '1:100883', '1:98877', '1:98906', '1:98937', '1:99454', '1:99876', '1:99955', '1:91895', '1:91920', '1:91929', '1:92043', '1:92053', '1:99565', '1:99632', '1:99638', '1:99792', '1:33815', '1:33952', '1:34052', '1:34503', '1:34840', '1:37162', '1:37268', '1:37329', '1:32965', '1:33464', '1:33586', '1:34097', '1:47387', '1:46129', '1:46980', '1:46982', '1:47197', '1:47416', '1:47512', '1:47630', '1:47834', '1:47858', '1:57620', '1:75346', '1:80943', '1:83159', '1:83841', '1:94466', '1:79323', '1:79762', '1:80741', '1:84389', '1:85436', '1:83447', '1:85429', '1:75199', '1:76156', '1:76217', '1:78656', '1:81153', '1:81209', '1:94121', '1:15132', '1:15423', '1:15495', '1:15518', '1:15552', '1:18057', '1:18449', '1:27210', '1:27266', '1:27283', '1:27285', '1:27290', '1:27306', '1:27319', '1:27376', '1:27404', '1:27406', '1:27422', '1:28681', '1:28706', '1:41502', '1:41517', '1:41543', '1:41608', '1:41984', '1:48147', '1:50192', '1:10714', '1:15521', '1:18401', '1:21198', '1:21214', '1:18484', '1:18625', '1:19545', '1:15505', '1:15511', '1:15865', '1:20565', '1:21670', '1:21695', '1:21719', '1:21721', '1:21041', '1:21774', '1:21962', '1:24490', '1:24712', '1:26010', '1:26858', '1:28243', '1:33031', '1:33515', '1:33865', '1:20843', '1:20863', '1:20978', '1:20861', '1:20996', '1:21006', '1:21017', '1:49674', '1:40286', '1:40318', '1:40427', '1:40464', '1:40467', '1:40472', '1:40586', '1:40967', '1:43550', '1:60517', '1:61172', '1:61462', '1:61591', '1:62127', '1:62534', '1:62566', '1:39778', '1:40675', '1:41023', '1:41045', '1:41073', '1:41120', '1:41151', '1:41191', '1:41221', '1:41255', '1:41316', '1:41357', '1:41378', '1:41484', '1:41519', '1:45905', '1:45932', '1:46281', '1:46298', '1:46855', '1:46617', '1:46647', '1:47137', '1:48170', '1:48211', '1:48265', '1:48282', '1:3375', '1:4139', '1:4166', '1:4179', '1:4195', '1:4254', '1:16004', '1:16036', '1:16055', '1:45785', '1:45906', '1:45908', '1:45992', '1:46014', '1:46280', '1:47696', '1:47768', '1:47799', '1:47890', '1:47937', '1:47923', '1:47924', '1:47929', '1:47932', '1:47941', '1:87596', '1:51857', '1:51923', '1:52886', '1:52888', '1:52925', '1:52929', '1:53482', '1:64731', '1:64809', '1:64818', '1:64928', '1:65006', '1:65077', '1:65101', '1:65167', '1:65181', '1:65249', '1:65256', '1:80329', '1:84122', '1:83508', '1:85406', '1:85414', '1:85787', '1:85827', '1:86828', '1:86341', '1:86360', '1:86489', '1:86604', '1:86618', '1:86669', '1:86676', '1:86708', '1:86799', '1:97098', '1:97218', '1:97427', '1:105445', '1:105449', '1:105463', '1:105699', '1:26409', '1:26751', '1:26866', '1:27619', '1:26939', '1:28427', '1:32793', '1:32932', '1:72206', '1:28636', '1:28796', '1:28968', '1:32031', '1:32046', '1:32754', '1:32811', '1:32866', '1:32880', '1:32895', '1:32936', '1:34072', '1:34088', '1:95595', '1:71866', '1:73789', '1:80120', '1:81957', '1:82625', '1:83129', '1:83235', '1:92903', '1:96554', '1:97322', '1:100661', '1:100764', '1:106242', '1:2663', '1:792', '1:1095', '1:1792', '1:1993', '1:386', '1:56835', '1:18465', '1:20553', '1:17896', '1:17958', '1:20708', '1:24505', '1:27169', '1:27281', '1:21917', '1:24325', '1:27017', '1:27245', '1:28956', '1:32404', '1:32792', '1:33143', '1:33975', '1:28205', '1:34071', '1:26782', '1:35633', '1:37023', '1:37390', '1:37558', '1:37637', '1:26321', '1:28576', '1:28757', '1:32627', '1:34546', '1:34607', '1:34632', '1:34655', '1:33940', '1:38031', '1:38181', '1:38412', '1:38024', '1:38380', '1:45199', '1:46670', '1:33610', '1:34684', '1:38132', '1:38589', '1:42200', '1:42244', '1:42269', '1:42445', '1:42637', '1:45443', '1:91589', '1:94913', '1:94933', '1:92957', '1:93513', '1:93095', '1:96429', '1:43477', '1:43653', '1:43982', '1:32030', '1:33190', '1:33541', '1:32154', '1:32647', '1:32663', '1:52206', '1:52685', '1:50844', '1:51012', '1:51412', '1:51503', '1:51553', '1:52131', '1:52345', '1:49230', '1:50488', '1:50735', '1:51020', '1:51215', '1:39743', '1:40435', '1:44340', '1:46941', '1:60178', '1:60265', '1:62785', '1:63066', '1:58281', '1:58496', '1:59419', '1:60040', '1:60310', '1:58313', '1:59338', '1:61897', '1:62532', '1:76265', '1:76763', '1:76764', '1:78779', '1:83884', '1:87539', '1:87927', '1:88966', '1:94181', '1:99257', '1:98785', '1:99246', '1:100336', '1:100784', '1:100785', '1:103172', '1:5335', '1:5464', '1:5597', '1:5716', '1:5779', '1:5938', '1:5956', '1:7002', '1:10104', '1:10218', '1:10406', '1:10444', '1:10522', '1:10541', '1:10544', '1:10550', '1:10585', '1:10593', '1:10381', '1:10400', '1:10511', '1:10518', '1:10545', '1:12310', '1:12329', '1:12420', '1:12441', '1:14867', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E25E124-31F7-E911-BE4E-0CC47A1E0DC2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCE60212-4D10-EA11-BEE3-90E2BAD5729C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C9C3A0A-7FFF-E911-8CD0-0CC47A4DEDD4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90D49EF7-13F6-E911-9659-38EAA78E2C94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D8B5CBBC-35F0-E911-94CF-1418774A25AB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E06943C6-D5EF-E911-A278-10983627C3C1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1ABC4644-64F4-E911-A4E7-FA163E84EE9A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AF65E7A-6EF3-E911-9E38-141877641875.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0A2F042B-71EF-E911-9535-0CC47AF9739E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AA4C6F18-8AF7-E911-80DC-0CC47AD9901C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5EAB8AB1-6810-EA11-9F96-008CFA197D98.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/10AE8E18-9802-EA11-8C36-B083FED138B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0407705F-5610-EA11-BCA2-0CC47AD98CEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5E63A65D-5B07-EA11-9816-0CC47A7C345E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EA78600-8003-EA11-98EB-405CFDFF480E.root']);