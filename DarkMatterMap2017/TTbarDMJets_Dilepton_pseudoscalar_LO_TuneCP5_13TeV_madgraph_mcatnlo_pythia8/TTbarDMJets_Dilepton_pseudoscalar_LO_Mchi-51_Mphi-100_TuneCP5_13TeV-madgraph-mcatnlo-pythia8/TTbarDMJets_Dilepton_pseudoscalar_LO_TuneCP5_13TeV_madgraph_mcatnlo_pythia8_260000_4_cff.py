import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11082', '1:23656', '1:12311', '1:17639', '1:22585', '1:17260', '1:17292', '1:18341', '1:18326', '1:16368', '1:16483', '1:16494', '1:16633', '1:24398', '1:23171', '1:3528', '1:3526', '1:5531', '1:4476', '1:9858', '1:33286', '1:33292', '1:12313', '1:17177', '1:17802', '1:4522', '1:4535', '1:9862', '1:26624', '1:29904', '1:26875', '1:26956', '1:31439', '1:5252', '1:29649', '1:34678', '1:34680', '1:28938', '1:32129', '1:31489', '1:33985', '1:35078', '1:36466', '1:252', '1:9109', '1:25726', '1:2214', '1:31024', '1:33149', '1:26543', '1:28162', '1:3057', '1:28809', '1:30229', '1:31155', '1:33089', '1:33594', '1:2811', '1:26851', '1:3790', '1:28319', '1:28971', '1:32272', '1:6726', '1:4606', '1:4973', '1:26631', '1:31443', '1:28785', '1:7558', '1:14809', '1:28348', '1:31563', '1:4453', '1:6711', '1:4883', '1:35366', '1:1680', '1:4844', '1:4858', '1:26532', '1:28317', '1:23492', '1:23515', '1:27029', '1:34216', '1:27165', '1:34754', '1:34907', '1:35907', '1:35731', '1:107', '1:8450', '1:4307', '1:7469', '1:8836', '1:34517', '1:3573', '1:9970', '1:7956', '1:29918', '1:1918', '1:2422', '1:2530', '1:29768', '1:31372', '1:879', '1:1495', '1:1515', '1:27392', '1:35483', '1:38549', '1:26641', '1:28849', '1:26511', '1:27406', '1:27275', '1:30975', '1:30946', '1:36914', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/C05C8FB4-7916-EA11-94B4-3CFDFE639780.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8CE3EFE-5C17-EA11-9FAC-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/38055D26-8217-EA11-8707-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2013AFAC-6317-EA11-8CAA-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/FAF900D4-2917-EA11-A923-24BE05C68671.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/94A6ED48-3F18-EA11-A4C4-0CC47AD9908C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/CC0A7D01-3A1B-EA11-A119-0CC47A4DEF48.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/AAE9111D-211C-EA11-8C33-0CC47A5FC495.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/08CA66AF-FB16-EA11-8C68-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D63E1E93-7217-EA11-A37B-B8CA3A70A410.root']);