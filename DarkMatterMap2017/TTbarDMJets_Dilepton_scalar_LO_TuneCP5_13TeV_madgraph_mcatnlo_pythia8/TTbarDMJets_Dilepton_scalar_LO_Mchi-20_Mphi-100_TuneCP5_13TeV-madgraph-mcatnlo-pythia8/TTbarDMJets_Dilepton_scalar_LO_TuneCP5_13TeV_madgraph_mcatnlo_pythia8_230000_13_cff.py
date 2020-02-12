import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:21287', '1:19003', '1:19039', '1:62602', '1:58085', '1:58185', '1:58568', '1:55293', '1:58400', '1:70324', '1:73835', '1:74079', '1:72553', '1:72888', '1:77579', '1:78455', '1:70123', '1:71596', '1:81252', '1:76718', '1:78252', '1:78753', '1:78827', '1:99360', '1:99734', '1:102323', '1:106278', '1:82889', '1:82982', '1:83078', '1:84232', '1:91140', '1:94362', '1:94378', '1:94405', '1:94861', '1:94928', '1:103903', '1:103904', '1:104074', '1:104124', '1:103933', '1:69834', '1:69990', '1:94857', '1:94916', '1:86269', '1:86408', '1:86454', '1:86655', '1:87361', '1:87460', '1:91833', '1:92018', '1:92195', '1:88586', '1:70319', '1:70378', '1:74501', '1:74442', '1:74446', '1:74059', '1:74178', '1:74309', '1:1229', '1:1265', '1:1273', '1:1285', '1:1466', '1:14026', '1:14303', '1:14314', '1:14546', '1:14551', '1:14417', '1:14730', '1:16482', '1:16922', '1:16638', '1:17788', '1:17848', '1:17947', '1:17986', '1:18335', '1:18481', '1:37667', '1:38895', '1:32625', '1:34716', '1:35538', '1:42515', '1:42990', '1:48023', '1:50460', '1:58737', '1:56039', '1:67486', '1:64887', '1:69724', '1:75518', '1:99063', '1:27544', '1:27938', '1:28041', '1:39389', '1:44521', '1:44703', '1:44786', '1:39820', '1:39954', '1:46143', '1:46180', '1:46317', '1:46053', '1:46467', '1:74748', '1:76180', '1:76613', '1:76925', '1:77063', '1:76571', '1:79440', '1:80458', '1:48603', '1:49090', '1:36678', '1:42739', '1:40294', '1:45146', '1:55544', '1:57557', '1:62777', '1:68247', '1:67354', '1:67983', '1:36534', '1:38786', '1:42258', '1:55983', '1:57950', '1:58255', '1:58417', '1:57403', '1:57824', '1:62818', '1:62826', '1:68715', '1:68986', '1:4827', '1:4838', '1:8739', '1:8781', '1:8819', '1:98427', '1:98456', '1:98558', '1:98705', '1:99603', '1:99609', '1:99644', '1:5994', '1:7416', '1:9067', '1:10863', '1:21471', '1:21751', '1:21953', '1:24213', '1:24320', '1:24004', '1:24618', '1:24646', '1:24733', '1:67445', '1:67918', '1:34262', '1:35580', '1:35920', '1:45627', '1:47893', '1:45080', '1:45624', '1:54249', '1:56120', '1:57518', '1:58283', '1:86607', '1:67502', '1:67951', '1:68554', '1:68559', '1:69795', '1:104434', '1:104853', '1:105678', '1:104562', '1:104917', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/922D5DD5-5710-EA11-BE57-AC1F6B595F4E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/58A27CA1-A5F6-E911-8978-0CC47A2B0744.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D6BD0C1E-CCF7-E911-9152-AC1F6B567730.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F030EDC5-1AF3-E911-9B33-002590DE6E6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/82662A5E-23EE-E911-8D5B-0CC47A7FC74A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/54235082-12F4-E911-A7A0-0CC47A1E0DCC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C924ADE-C9EE-E911-8597-C4544423E320.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/120CCF0F-55EF-E911-94EA-24BE05C48821.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5072FB7D-5910-EA11-81FB-28924A33B9FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/629E6C83-AC0D-EA11-83C5-0CC47A5FBE25.root']);