import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:23244', '1:23331', '1:24274', '1:14789', '1:14827', '1:14854', '1:14863', '1:14864', '1:11861', '1:14590', '1:19036', '1:16390', '1:16757', '1:16795', '1:14929', '1:21148', '1:14606', '1:14632', '1:14669', '1:13021', '1:20026', '1:20062', '1:17086', '1:20472', '1:12816', '1:15891', '1:18479', '1:21935', '1:23751', '1:23843', '1:24694', '1:24661', '1:16040', '1:16073', '1:15609', '1:19314', '1:16110', '1:11163', '1:13375', '1:23709', '1:12185', '1:13237', '1:15825', '1:19280', '1:16790', '1:14219', '1:14403', '1:15761', '1:14434', '1:14442', '1:14452', '1:19067', '1:16255', '1:24823', '1:13821', '1:17209', '1:12114', '1:12346', '1:12098', '1:12396', '1:17336', '1:12994', '1:20779', '1:11724', '1:13802', '1:14036', '1:14217', '1:19686', '1:21233', '1:24393', '1:16488', '1:15708', '1:15771', '1:19570', '1:22417', '1:22595', '1:19947', '1:19958', '1:11579', '1:11928', '1:11985', '1:17917', '1:22014', '1:22239', '1:22290', '1:12686', '1:22567', '1:22486', '1:17756', '1:24656', '1:24672', '1:16426', '1:21986', '1:15068', '1:15735', '1:19332', '1:19753', '1:16296', '1:15753', '1:14139', '1:19840', '1:19872', '1:15798', '1:15807', '1:16224', '1:16233', '1:16297', '1:15847', '1:15935', '1:19308', '1:15932', '1:19575', '1:19622', '1:19180', '1:12334', '1:12888', '1:22434', '1:22005', '1:20563', '1:20312', '1:20851', '1:23607', '1:12249', '1:22357', '1:17284', '1:18525', '1:18684', '1:18606', '1:18054', '1:18340', '1:18356', '1:18914', '1:18801', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/148F57B3-5812-EA11-B6E6-002590A2BCBC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7E63DD98-DBFE-E911-9513-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/A8DEEED0-1003-EA11-9D36-AC1F6B596102.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/24BCCF52-D2FD-E911-ACC1-002590DE6E8A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/1C3C42AE-27FE-E911-8818-3417EBE7062D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/10FCB283-8203-EA11-B898-506B4BB134E6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/660B22F0-DD02-EA11-B269-1866DAEB3370.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C02A524E-9E03-EA11-95FC-002590E3A0FC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/E4248C11-C002-EA11-AB10-0CC47AFCC662.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/0C0E7588-6CFE-E911-AA00-EC0D9A8225FE.root']);