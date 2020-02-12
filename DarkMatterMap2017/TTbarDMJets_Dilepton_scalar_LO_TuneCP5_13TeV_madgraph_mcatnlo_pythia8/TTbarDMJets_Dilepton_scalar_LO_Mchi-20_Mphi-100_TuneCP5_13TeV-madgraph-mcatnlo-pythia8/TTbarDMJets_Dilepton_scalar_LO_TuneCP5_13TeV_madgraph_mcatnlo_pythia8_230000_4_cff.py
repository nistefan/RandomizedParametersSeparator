import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:61580', '1:61861', '1:61939', '1:62078', '1:62086', '1:62988', '1:62979', '1:63149', '1:79732', '1:80080', '1:80088', '1:80095', '1:80116', '1:80234', '1:80303', '1:80310', '1:88668', '1:88677', '1:88681', '1:91258', '1:91286', '1:92205', '1:66883', '1:66952', '1:71691', '1:77182', '1:77141', '1:77208', '1:77246', '1:77386', '1:88763', '1:91654', '1:24601', '1:24853', '1:27999', '1:32477', '1:34873', '1:24934', '1:34372', '1:35959', '1:37273', '1:38544', '1:104489', '1:104504', '1:104555', '1:52202', '1:52347', '1:52394', '1:52413', '1:52557', '1:52295', '1:52410', '1:99664', '1:99278', '1:99320', '1:99471', '1:99855', '1:102746', '1:102745', '1:102751', '1:102789', '1:102838', '1:102868', '1:102886', '1:102852', '1:102891', '1:46406', '1:46494', '1:46625', '1:46845', '1:46903', '1:70661', '1:70973', '1:71557', '1:73514', '1:77126', '1:93201', '1:92790', '1:92794', '1:92900', '1:92909', '1:4454', '1:4536', '1:4889', '1:18420', '1:18698', '1:18777', '1:18788', '1:18897', '1:18952', '1:18960', '1:19229', '1:98059', '1:98090', '1:98149', '1:98192', '1:843', '1:4946', '1:6000', '1:21518', '1:2779', '1:12017', '1:28202', '1:42879', '1:91257', '1:92765', '1:21245', '1:19996', '1:20671', '1:55288', '1:55752', '1:47902', '1:38510', '1:46274', '1:46373', '1:86815', '1:91046', '1:92838', '1:92952', '1:91146', '1:14299', '1:12928', '1:12930', '1:12967', '1:14775', '1:37374', '1:39046', '1:41937', '1:49191', '1:50131', '1:83257', '1:60218', '1:60321', '1:65233', '1:65925', '1:97145', '1:97384', '1:97508', '1:97135', '1:97152', '1:97216', '1:97366', '1:3046', '1:3089', '1:3111', '1:3309', '1:3341', '1:4290', '1:4357', '1:4384', '1:4498', '1:4811', '1:12008', '1:12031', '1:12110', '1:12157', '1:12162', '1:58465', '1:97352', '1:97376', '1:97545', '1:97629', '1:33613', '1:34297', '1:34897', '1:69711', '1:72516', '1:72669', '1:63062', '1:63841', '1:74223', '1:74447', '1:74478', '1:74513', '1:74425', '1:74531', '1:74557', '1:103430', '1:105499', '1:39833', '1:48559', '1:48802', '1:49225', '1:49302', '1:49546', '1:50132', '1:83365', '1:83393', '1:83697', '1:83735', '1:83818', '1:83851', '1:103567', '1:103644', '1:41239', '1:48324', '1:53146', '1:55825', '1:55839', '1:55876', '1:56108', '1:76520', '1:79644', '1:79749', '1:79349', '1:79766', '1:102851', '1:103409', '1:1607', '1:1753', '1:4118', '1:8552', '1:8849', '1:9655', '1:10275', '1:4251', '1:10953', '1:10957', '1:12467', '1:9591', '1:9796', '1:9807', '1:9885', '1:10447', '1:9848', '1:10591', '1:10620', '1:10668', '1:42072', '1:37714', '1:9657', '1:9612', '1:9726', '1:10575', '1:10687', '1:10657', '1:10674', '1:10697', '1:10725', '1:12684', '1:12773', '1:48044', '1:48530', '1:50568', '1:53403', '1:54764', '1:104620', '1:104702', '1:104759', '1:102787', '1:103403', '1:103664', '1:103760', '1:103851', '1:94', '1:2011', '1:3972', '1:3425', '1:9159', '1:9299', '1:9372', '1:9445', '1:8494', '1:40164', '1:51450', '1:51770', '1:52918', '1:53065', '1:60626', '1:55198', '1:84103', '1:99347', '1:99971', '1:16235', '1:17842', '1:17102', '1:28626', '1:32229', '1:19320', '1:21558', '1:26655', '1:43314', '1:45130', '1:65649', '1:65661', '1:66275', '1:70714', '1:71572', '1:74097', '1:72866', '1:12523', '1:14073', '1:14141', '1:15055', '1:16206', '1:17495', '1:17706', '1:28686', '1:66641', '1:65798', '1:71035', '1:71292', '1:73295', '1:73456', '1:68836', '1:69735', '1:62909', '1:63532', '1:68010', '1:100282', '1:102855', '1:103842', '1:76209', '1:80152', '1:80514', '1:79560', '1:80555', '1:97283', '1:91796', '1:86677', '1:87739', '1:91336', '1:71019', '1:71043', '1:71231', '1:73033', '1:57176', '1:57301', '1:57143', '1:57144', '1:57260', '1:91091', '1:91093', '1:91179', '1:91274', '1:91302', '1:91331', '1:91349', '1:91458', '1:91474', '1:43834', '1:45122', '1:47063', '1:43180', '1:10057', '1:10291', '1:18028', '1:18359', '1:18363', '1:97788', '1:99006', '1:74709', '1:74718', '1:92079', '1:93171', '1:94701', '1:96446', '1:94630', '1:99306', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C2B2B4A5-90FA-E911-A1ED-FA163E596216.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44AD8F54-33FC-E911-BFC1-44A842CFD5D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BC0C7A45-B3FB-E911-9A20-0025905C53AA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/18D4DE3D-06FB-E911-9D07-0CC47A4DEE78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D60A6FA0-CCFC-E911-BDAF-0CC47A5FC679.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BCA2AA4C-68FB-E911-A22D-001CC4A6CCE6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/68A10C47-6CFF-E911-A5E7-0242AC1C0507.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70D242A1-7FFF-E911-934F-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C045F616-49FE-E911-9BA5-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FAD01C50-69FF-E911-BBD7-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE2BDBAA-1F02-EA11-9F99-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84EBD031-DAFE-E911-A032-002590DE39F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9AE2976D-2503-EA11-916D-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8BF48D7-28FF-E911-86D4-AC1F6BC67D46.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8A44B795-0403-EA11-B303-0CC47AFF014C.root']);