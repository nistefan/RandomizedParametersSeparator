import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:16882', '1:21117', '1:79400', '1:79924', '1:39496', '1:45581', '1:48899', '1:53656', '1:53861', '1:57049', '1:67088', '1:17123', '1:28614', '1:32773', '1:39711', '1:46842', '1:67845', '1:87055', '1:64534', '1:65924', '1:66176', '1:66192', '1:72183', '1:75483', '1:12495', '1:12496', '1:12630', '1:12951', '1:22607', '1:22688', '1:22697', '1:22793', '1:32132', '1:32165', '1:42179', '1:30714', '1:32255', '1:1587', '1:1162', '1:1749', '1:40399', '1:40520', '1:40377', '1:40464', '1:5982', '1:6760', '1:8591', '1:8893', '1:8986', '1:11645', '1:41439', '1:41487', '1:41731', '1:61741', '1:93955', '1:31851', '1:64651', '1:95390', '1:40629', '1:61764', '1:103439', '1:64836', '1:65119', '1:65742', '1:65746', '1:103799', '1:103807', '1:17073', '1:17387', '1:17857', '1:27481', '1:27697', '1:29387', '1:17677', '1:20117', '1:49369', '1:51800', '1:45649', '1:94958', '1:94000', '1:10300', '1:10714', '1:10793', '1:10884', '1:10902', '1:16484', '1:93527', '1:96990', '1:103259', '1:81928', '1:104076', '1:42635', '1:46247', '1:48589', '1:53366', '1:51953', '1:54869', '1:57767', '1:59289', '1:48613', '1:71933', '1:48702', '1:58794', '1:103228', '1:106175', '1:106191', '1:51014', '1:52111', '1:52137', '1:53447', '1:54950', '1:83997', '1:70828', '1:92995', '1:92444', '1:83771', '1:87859', '1:103277', '1:103831', '1:94145', '1:7054', '1:7418', '1:7721', '1:6287', '1:6685', '1:6693', '1:19447', '1:19645', '1:19663', '1:24174', '1:18958', '1:19128', '1:27460', '1:27499', '1:28418', '1:28961', '1:29192', '1:48489', '1:48503', '1:48548', '1:48737', '1:88865', '1:89117', '1:21625', '1:23033', '1:23054', '1:23220', '1:48966', '1:49068', '1:49077', '1:49106', '1:49187', '1:49221', '1:49260', '1:95408', '1:95707', '1:95808', '1:96433', '1:96675', '1:30309', '1:43046', '1:43784', '1:43022', '1:43048', '1:41750', '1:41932', '1:46229', '1:46257', '1:46289', '1:43408', '1:49095', '1:41127', '1:58558', '1:58667', '1:59819', '1:43722', '1:43746', '1:46785', '1:46715', '1:48439', '1:56691', '1:65623', '1:62285', '1:58153', '1:60566', '1:60846', '1:64183', '1:71042', '1:91950', '1:79139', '1:94730', '1:82823', '1:82045', '1:83808', '1:84546', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DE44FE63-EB02-EA11-A34D-7CD30AC030B4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/547119DF-1A04-EA11-B104-AC1F6BC67D48.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02B13BB9-62FF-E911-984A-90B11CBCFFEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9CBC629C-D702-EA11-B565-0CC47AFF0200.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/781E8649-6AF8-E911-BBF5-D4AE5264D710.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F82C7F4C-0708-EA11-9AA9-0CC47A5FC2A5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/183064D5-6CF3-E911-BF5D-003048F29A12.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44DAFF4C-FAF4-E911-B4FC-509A4C9EF93B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8C2ADF7-09F5-E911-BBA1-509A4C9F8888.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A1C1EEA-26F7-E911-8EBF-E0071B7A68F0.root']);