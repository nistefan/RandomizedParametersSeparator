import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:32596', '1:32793', '1:51375', '1:51491', '1:51576', '1:47485', '1:53240', '1:53243', '1:53531', '1:53860', '1:54000', '1:54064', '1:54455', '1:4081', '1:4243', '1:4418', '1:4638', '1:5710', '1:6597', '1:12685', '1:12964', '1:9687', '1:9701', '1:18153', '1:18266', '1:18312', '1:18389', '1:18696', '1:18683', '1:18424', '1:18855', '1:18371', '1:22007', '1:19388', '1:19391', '1:19701', '1:27712', '1:27967', '1:28571', '1:18784', '1:18810', '1:22110', '1:22717', '1:28387', '1:28487', '1:28561', '1:57864', '1:46850', '1:3125', '1:57590', '1:51060', '1:53753', '1:54256', '1:42556', '1:42586', '1:42652', '1:42692', '1:42806', '1:42951', '1:86710', '1:103079', '1:71276', '1:72751', '1:70026', '1:70062', '1:70162', '1:70206', '1:70296', '1:57348', '1:57511', '1:57610', '1:58195', '1:58263', '1:105089', '1:78863', '1:82095', '1:2338', '1:2460', '1:2686', '1:2631', '1:6324', '1:6350', '1:6349', '1:6616', '1:6691', '1:6827', '1:6965', '1:6917', '1:7853', '1:8132', '1:10409', '1:10724', '1:11300', '1:11535', '1:10928', '1:11225', '1:11421', '1:11784', '1:12684', '1:14265', '1:14654', '1:14939', '1:14325', '1:57823', '1:6351', '1:6783', '1:7636', '1:7851', '1:8613', '1:8886', '1:9005', '1:9504', '1:14717', '1:14922', '1:15062', '1:16230', '1:31221', '1:31679', '1:17433', '1:17487', '1:17528', '1:18945', '1:41515', '1:41532', '1:41658', '1:41685', '1:41739', '1:45725', '1:45999', '1:18927', '1:43085', '1:43930', '1:46037', '1:46119', '1:46347', '1:80205', '1:77834', '1:77913', '1:78090', '1:21090', '1:21160', '1:98013', '1:98431', '1:103335', '1:103470', '1:8002', '1:8529', '1:10847', '1:43065', '1:46034', '1:30783', '1:39482', '1:42754', '1:42926', '1:55587', '1:92854', '1:91929', '1:94517', '1:95148', '1:104598', '1:13768', '1:15219', '1:76855', '1:81499', '1:39417', '1:48340', '1:48478', '1:57634', '1:58416', '1:59793', '1:61015', '1:95374', '1:98973', '1:90995', '1:101261', '1:3570', '1:1557', '1:1865', '1:44231', '1:44575', '1:30238', '1:53683', '1:58520', '1:6652', '1:11369', '1:25425', '1:21293', '1:97263', '1:51039', '1:51323', '1:53612', '1:54600', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90043704-20FC-E911-8078-0CC47AFCC3D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/58F7196A-76FC-E911-8198-0025905C96E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B65A1C1B-7FFC-E911-92D1-0CC47AFCC392.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/30FB16E9-BC12-EA11-A843-7CD30AC03722.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70BD48D5-3CF5-E911-BBCD-D4856445E5A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E131ABC-63F2-E911-BBAD-441EA157ADE4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/00610B13-6BF2-E911-832F-98039B3B01B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2E996FF0-01F5-E911-BFCE-D4856444A744.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/501EAB60-EC02-EA11-9994-0CC47AFCC6B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3AF7C78E-7106-EA11-9305-0025905C3E68.root']);