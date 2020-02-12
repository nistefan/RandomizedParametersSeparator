import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:20867', '1:23943', '1:14777', '1:13246', '1:14934', '1:16414', '1:16448', '1:14109', '1:16485', '1:16563', '1:21166', '1:21231', '1:14643', '1:14954', '1:17580', '1:22291', '1:19130', '1:19478', '1:19857', '1:15940', '1:16138', '1:16010', '1:15990', '1:23995', '1:16522', '1:16092', '1:16866', '1:17001', '1:23091', '1:12353', '1:13268', '1:13602', '1:19542', '1:15542', '1:16046', '1:15047', '1:15041', '1:21064', '1:14422', '1:14475', '1:11630', '1:13828', '1:12963', '1:17073', '1:12019', '1:12214', '1:12296', '1:12205', '1:12813', '1:14386', '1:11298', '1:14045', '1:21203', '1:23653', '1:14156', '1:15334', '1:15407', '1:15415', '1:15758', '1:15618', '1:15523', '1:15628', '1:15693', '1:15810', '1:15786', '1:11850', '1:11896', '1:13159', '1:22668', '1:22907', '1:16708', '1:21279', '1:21847', '1:24424', '1:15791', '1:15132', '1:16136', '1:15432', '1:16934', '1:14466', '1:15943', '1:19118', '1:19215', '1:23962', '1:19225', '1:24693', '1:19167', '1:23889', '1:24476', '1:12636', '1:24541', '1:20803', '1:23282', '1:22546', '1:18474', '1:18886', '1:18576', '1:18655', '1:23973', '1:23121', '1:23286', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/148F57B3-5812-EA11-B6E6-002590A2BCBC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7E63DD98-DBFE-E911-9513-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/A8DEEED0-1003-EA11-9D36-AC1F6B596102.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/24BCCF52-D2FD-E911-ACC1-002590DE6E8A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/1C3C42AE-27FE-E911-8818-3417EBE7062D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/10FCB283-8203-EA11-B898-506B4BB134E6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/660B22F0-DD02-EA11-B269-1866DAEB3370.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C02A524E-9E03-EA11-95FC-002590E3A0FC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/E4248C11-C002-EA11-AB10-0CC47AFCC662.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/0C0E7588-6CFE-E911-AA00-EC0D9A8225FE.root']);