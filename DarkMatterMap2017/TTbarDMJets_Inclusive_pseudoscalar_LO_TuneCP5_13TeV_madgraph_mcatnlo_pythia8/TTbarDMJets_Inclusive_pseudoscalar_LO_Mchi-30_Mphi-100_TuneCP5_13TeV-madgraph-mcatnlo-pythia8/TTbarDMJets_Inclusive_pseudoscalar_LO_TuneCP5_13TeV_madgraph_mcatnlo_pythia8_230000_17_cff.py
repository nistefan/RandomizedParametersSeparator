import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:14443', '1:25206', '1:67522', '1:78354', '1:79318', '1:79470', '1:19092', '1:28186', '1:64035', '1:43675', '1:22328', '1:27435', '1:27493', '1:27774', '1:46637', '1:51460', '1:60809', '1:48610', '1:82639', '1:82645', '1:97236', '1:58720', '1:64350', '1:14358', '1:22462', '1:22601', '1:22787', '1:30894', '1:30922', '1:32270', '1:32292', '1:32386', '1:32642', '1:30810', '1:30829', '1:30966', '1:32092', '1:1910', '1:3640', '1:1218', '1:40296', '1:40358', '1:90223', '1:90630', '1:7998', '1:11041', '1:11423', '1:9518', '1:41162', '1:41644', '1:41880', '1:62132', '1:64831', '1:77444', '1:61225', '1:65161', '1:73968', '1:74424', '1:75269', '1:52562', '1:52640', '1:61832', '1:96601', '1:102506', '1:101466', '1:103669', '1:103665', '1:17874', '1:23580', '1:44282', '1:44842', '1:51500', '1:52041', '1:52326', '1:53066', '1:106208', '1:93496', '1:94351', '1:11018', '1:14905', '1:16488', '1:97880', '1:103827', '1:81823', '1:81986', '1:81994', '1:40446', '1:57283', '1:58721', '1:71011', '1:48195', '1:97071', '1:103699', '1:90370', '1:49655', '1:52043', '1:55594', '1:55622', '1:101253', '1:70921', '1:77933', '1:85700', '1:91981', '1:93288', '1:88533', '1:88344', '1:73957', '1:96859', '1:106331', '1:4286', '1:4395', '1:4463', '1:7693', '1:6558', '1:6583', '1:9283', '1:19157', '1:19606', '1:19057', '1:28307', '1:29091', '1:29576', '1:48219', '1:48322', '1:48795', '1:48981', '1:89237', '1:89248', '1:23008', '1:23188', '1:23231', '1:49012', '1:96451', '1:30771', '1:40321', '1:30010', '1:30075', '1:30345', '1:30547', '1:30585', '1:41730', '1:43808', '1:43014', '1:43287', '1:40383', '1:40494', '1:40508', '1:40708', '1:46345', '1:41698', '1:49027', '1:49103', '1:49707', '1:40536', '1:42798', '1:49060', '1:49487', '1:51078', '1:51531', '1:52294', '1:46023', '1:46773', '1:49416', '1:49812', '1:46802', '1:46970', '1:48532', '1:48945', '1:51865', '1:48231', '1:48360', '1:49898', '1:59201', '1:62140', '1:61107', '1:58925', '1:59125', '1:65900', '1:71135', '1:92327', '1:79457', '1:81702', '1:85461', '1:85870', '1:84086', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DE44FE63-EB02-EA11-A34D-7CD30AC030B4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/547119DF-1A04-EA11-B104-AC1F6BC67D48.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02B13BB9-62FF-E911-984A-90B11CBCFFEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9CBC629C-D702-EA11-B565-0CC47AFF0200.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/781E8649-6AF8-E911-BBF5-D4AE5264D710.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F82C7F4C-0708-EA11-9AA9-0CC47A5FC2A5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/183064D5-6CF3-E911-BF5D-003048F29A12.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44DAFF4C-FAF4-E911-B4FC-509A4C9EF93B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8C2ADF7-09F5-E911-BBA1-509A4C9F8888.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A1C1EEA-26F7-E911-8EBF-E0071B7A68F0.root']);