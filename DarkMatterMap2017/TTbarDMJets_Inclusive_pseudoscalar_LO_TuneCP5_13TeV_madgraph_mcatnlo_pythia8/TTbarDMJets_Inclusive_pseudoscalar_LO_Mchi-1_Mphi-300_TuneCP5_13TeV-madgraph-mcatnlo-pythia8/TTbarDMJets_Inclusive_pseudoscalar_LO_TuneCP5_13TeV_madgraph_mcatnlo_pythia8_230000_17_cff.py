import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:21370', '1:60913', '1:78356', '1:42873', '1:46906', '1:55498', '1:58394', '1:17032', '1:30080', '1:18308', '1:29723', '1:40005', '1:40643', '1:70492', '1:91321', '1:90880', '1:64318', '1:64444', '1:64979', '1:67955', '1:76962', '1:84727', '1:12494', '1:12504', '1:13331', '1:13865', '1:22999', '1:32066', '1:30970', '1:32295', '1:40440', '1:40382', '1:40610', '1:90144', '1:90168', '1:90192', '1:90199', '1:6500', '1:11725', '1:9781', '1:10307', '1:10797', '1:41754', '1:62098', '1:31914', '1:49249', '1:61940', '1:71586', '1:75824', '1:57331', '1:64875', '1:84806', '1:65080', '1:76164', '1:49534', '1:65047', '1:67352', '1:56421', '1:57694', '1:96310', '1:104027', '1:64440', '1:64456', '1:64585', '1:64667', '1:65008', '1:65110', '1:65794', '1:19273', '1:32742', '1:27908', '1:41373', '1:75506', '1:80608', '1:90989', '1:83582', '1:83194', '1:83355', '1:83669', '1:83991', '1:87717', '1:92856', '1:94054', '1:87763', '1:10838', '1:103194', '1:101478', '1:101572', '1:102455', '1:40921', '1:49796', '1:52427', '1:56230', '1:64605', '1:48297', '1:98970', '1:103318', '1:53246', '1:51969', '1:53218', '1:55695', '1:55873', '1:77272', '1:87012', '1:88090', '1:84639', '1:92443', '1:92937', '1:96322', '1:7532', '1:17945', '1:19199', '1:19491', '1:19648', '1:19844', '1:27476', '1:27637', '1:28450', '1:28986', '1:29064', '1:29585', '1:30594', '1:48239', '1:48291', '1:48836', '1:87874', '1:89116', '1:23162', '1:23258', '1:23269', '1:23378', '1:49047', '1:49099', '1:49168', '1:49172', '1:40099', '1:40131', '1:40192', '1:30398', '1:45319', '1:43289', '1:40360', '1:40465', '1:40525', '1:41722', '1:41726', '1:46267', '1:49543', '1:62777', '1:46359', '1:48556', '1:51849', '1:58760', '1:59252', '1:58235', '1:60903', '1:62699', '1:56480', '1:57031', '1:57574', '1:58069', '1:59698', '1:57485', '1:82778', '1:84982', '1:78792', '1:81645', '1:80456', '1:80987', '1:81434', '1:85008', '1:82942', '1:84177', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DE44FE63-EB02-EA11-A34D-7CD30AC030B4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/547119DF-1A04-EA11-B104-AC1F6BC67D48.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02B13BB9-62FF-E911-984A-90B11CBCFFEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9CBC629C-D702-EA11-B565-0CC47AFF0200.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/781E8649-6AF8-E911-BBF5-D4AE5264D710.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F82C7F4C-0708-EA11-9AA9-0CC47A5FC2A5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/183064D5-6CF3-E911-BF5D-003048F29A12.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44DAFF4C-FAF4-E911-B4FC-509A4C9EF93B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8C2ADF7-09F5-E911-BBA1-509A4C9F8888.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A1C1EEA-26F7-E911-8EBF-E0071B7A68F0.root']);