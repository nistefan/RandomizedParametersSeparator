import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:20894', '1:23153', '1:13642', '1:13325', '1:16575', '1:19223', '1:14266', '1:14980', '1:16699', '1:16845', '1:14199', '1:14627', '1:21146', '1:16810', '1:17064', '1:19073', '1:19098', '1:19153', '1:15087', '1:18083', '1:18573', '1:24769', '1:24734', '1:19221', '1:19421', '1:24520', '1:24702', '1:24863', '1:13416', '1:20759', '1:23304', '1:23679', '1:24584', '1:18792', '1:18944', '1:19074', '1:14025', '1:15704', '1:19459', '1:14349', '1:21243', '1:16175', '1:16416', '1:19015', '1:14430', '1:14456', '1:16357', '1:11496', '1:11501', '1:11875', '1:13648', '1:13895', '1:11948', '1:13713', '1:17056', '1:22785', '1:12315', '1:12246', '1:17137', '1:16250', '1:14521', '1:14209', '1:14192', '1:19661', '1:19662', '1:19912', '1:21201', '1:23762', '1:24926', '1:14635', '1:21139', '1:15538', '1:15716', '1:15757', '1:15627', '1:22550', '1:22695', '1:20517', '1:11920', '1:22246', '1:12997', '1:12342', '1:24848', '1:19241', '1:14227', '1:16209', '1:19135', '1:19143', '1:19334', '1:19335', '1:15842', '1:19299', '1:19687', '1:19891', '1:23800', '1:23880', '1:23896', '1:12506', '1:24974', '1:20044', '1:20287', '1:20367', '1:23951', '1:21281', '1:12157', '1:18123', '1:18364', '1:17400', '1:17275', '1:18528', '1:24406', '1:23293', '1:23391', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/148F57B3-5812-EA11-B6E6-002590A2BCBC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7E63DD98-DBFE-E911-9513-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/A8DEEED0-1003-EA11-9D36-AC1F6B596102.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/24BCCF52-D2FD-E911-ACC1-002590DE6E8A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/1C3C42AE-27FE-E911-8818-3417EBE7062D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/10FCB283-8203-EA11-B898-506B4BB134E6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/660B22F0-DD02-EA11-B269-1866DAEB3370.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C02A524E-9E03-EA11-95FC-002590E3A0FC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/E4248C11-C002-EA11-AB10-0CC47AFCC662.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/0C0E7588-6CFE-E911-AA00-EC0D9A8225FE.root']);