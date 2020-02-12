import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11111', '1:11596', '1:22163', '1:22620', '1:17061', '1:22839', '1:22632', '1:18965', '1:18583', '1:23632', '1:23655', '1:7057', '1:5530', '1:4592', '1:8293', '1:8393', '1:8551', '1:8738', '1:33290', '1:5630', '1:9794', '1:25990', '1:33238', '1:33643', '1:33138', '1:33272', '1:33275', '1:33276', '1:33375', '1:35723', '1:27517', '1:5620', '1:33142', '1:33147', '1:26539', '1:28930', '1:28694', '1:29352', '1:31623', '1:2964', '1:2967', '1:2779', '1:3729', '1:29098', '1:8739', '1:9002', '1:28775', '1:7464', '1:4325', '1:4244', '1:10030', '1:8270', '1:23552', '1:23620', '1:23457', '1:23499', '1:23642', '1:23644', '1:25099', '1:27485', '1:34340', '1:35091', '1:35745', '1:1003', '1:6736', '1:8339', '1:8776', '1:10416', '1:10431', '1:8278', '1:2785', '1:29818', '1:28791', '1:1916', '1:1252', '1:35159', '1:35097', '1:35459', '1:36786', '1:36787', '1:36616', '1:36500', '1:26518', '1:28869', '1:26306', '1:31023', '1:27708', '1:35076', '1:27309', '1:25672', '1:32419', '1:32961', '1:36044', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/C05C8FB4-7916-EA11-94B4-3CFDFE639780.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8CE3EFE-5C17-EA11-9FAC-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/38055D26-8217-EA11-8707-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2013AFAC-6317-EA11-8CAA-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/FAF900D4-2917-EA11-A923-24BE05C68671.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/94A6ED48-3F18-EA11-A4C4-0CC47AD9908C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/CC0A7D01-3A1B-EA11-A119-0CC47A4DEF48.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/AAE9111D-211C-EA11-8C33-0CC47A5FC495.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/08CA66AF-FB16-EA11-8C68-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D63E1E93-7217-EA11-A37B-B8CA3A70A410.root']);