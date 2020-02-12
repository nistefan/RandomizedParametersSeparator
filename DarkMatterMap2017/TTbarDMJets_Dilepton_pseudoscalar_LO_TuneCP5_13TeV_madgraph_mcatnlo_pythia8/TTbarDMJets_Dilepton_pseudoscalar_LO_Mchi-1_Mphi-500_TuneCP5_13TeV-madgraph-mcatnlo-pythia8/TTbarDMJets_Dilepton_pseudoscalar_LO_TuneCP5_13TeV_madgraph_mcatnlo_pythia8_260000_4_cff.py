import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11336', '1:20199', '1:18185', '1:17037', '1:18318', '1:18673', '1:16609', '1:22782', '1:23277', '1:3523', '1:5566', '1:7042', '1:7044', '1:7066', '1:4475', '1:4582', '1:6981', '1:8400', '1:8939', '1:9013', '1:4519', '1:9889', '1:9920', '1:9303', '1:33544', '1:26592', '1:28814', '1:28155', '1:2279', '1:5263', '1:26307', '1:33134', '1:34652', '1:32147', '1:35585', '1:33976', '1:33987', '1:35613', '1:35439', '1:36191', '1:36337', '1:38246', '1:3085', '1:5329', '1:185', '1:1568', '1:3508', '1:2264', '1:2270', '1:9798', '1:29833', '1:28169', '1:32076', '1:29689', '1:31541', '1:31551', '1:29924', '1:3271', '1:28749', '1:28871', '1:4586', '1:6934', '1:4861', '1:7035', '1:8246', '1:8732', '1:33539', '1:33535', '1:14691', '1:7671', '1:31582', '1:32039', '1:32050', '1:32054', '1:32224', '1:6511', '1:6550', '1:35367', '1:9029', '1:26546', '1:23478', '1:23510', '1:23628', '1:25094', '1:27200', '1:27600', '1:34196', '1:27755', '1:35028', '1:35841', '1:35748', '1:281', '1:1215', '1:8332', '1:8351', '1:9222', '1:2416', '1:32353', '1:29902', '1:29819', '1:869', '1:1951', '1:34761', '1:35127', '1:35514', '1:37164', '1:1394', '1:27726', '1:27905', '1:34197', '1:27008', '1:27053', '1:25402', '1:38521', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/C05C8FB4-7916-EA11-94B4-3CFDFE639780.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8CE3EFE-5C17-EA11-9FAC-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/38055D26-8217-EA11-8707-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2013AFAC-6317-EA11-8CAA-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/FAF900D4-2917-EA11-A923-24BE05C68671.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/94A6ED48-3F18-EA11-A4C4-0CC47AD9908C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/CC0A7D01-3A1B-EA11-A119-0CC47A4DEF48.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/AAE9111D-211C-EA11-8C33-0CC47A5FC495.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/08CA66AF-FB16-EA11-8C68-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D63E1E93-7217-EA11-A37B-B8CA3A70A410.root']);