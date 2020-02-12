import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:20883', '1:21581', '1:24132', '1:14814', '1:14824', '1:14828', '1:15109', '1:13301', '1:15021', '1:19988', '1:14128', '1:14229', '1:14633', '1:16542', '1:16801', '1:21050', '1:21058', '1:24978', '1:22404', '1:19048', '1:19091', '1:19525', '1:19825', '1:19386', '1:19124', '1:24116', '1:15738', '1:16034', '1:16144', '1:16286', '1:15065', '1:19708', '1:16251', '1:24791', '1:24827', '1:24569', '1:21963', '1:24486', '1:14000', '1:19147', '1:19222', '1:15679', '1:14007', '1:16789', '1:14408', '1:14414', '1:14474', '1:15073', '1:24948', '1:11859', '1:11891', '1:17290', '1:17328', '1:17345', '1:14395', '1:20305', '1:20395', '1:20588', '1:11209', '1:24258', '1:14141', '1:19669', '1:21196', '1:21240', '1:23918', '1:14221', '1:14921', '1:14966', '1:16674', '1:15571', '1:15579', '1:15643', '1:19574', '1:22240', '1:22685', '1:22346', '1:22467', '1:22583', '1:19944', '1:11768', '1:11761', '1:11927', '1:17923', '1:17958', '1:22151', '1:12678', '1:18189', '1:16836', '1:24646', '1:24957', '1:19696', '1:16283', '1:19040', '1:16295', '1:19080', '1:19340', '1:19884', '1:15919', '1:15853', '1:19442', '1:19582', '1:19050', '1:12294', '1:23193', '1:12265', '1:12465', '1:12488', '1:22229', '1:17032', '1:17170', '1:18682', '1:24929', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/148F57B3-5812-EA11-B6E6-002590A2BCBC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7E63DD98-DBFE-E911-9513-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/A8DEEED0-1003-EA11-9D36-AC1F6B596102.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/24BCCF52-D2FD-E911-ACC1-002590DE6E8A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/1C3C42AE-27FE-E911-8818-3417EBE7062D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/10FCB283-8203-EA11-B898-506B4BB134E6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/660B22F0-DD02-EA11-B269-1866DAEB3370.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C02A524E-9E03-EA11-95FC-002590E3A0FC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/E4248C11-C002-EA11-AB10-0CC47AFCC662.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/0C0E7588-6CFE-E911-AA00-EC0D9A8225FE.root']);