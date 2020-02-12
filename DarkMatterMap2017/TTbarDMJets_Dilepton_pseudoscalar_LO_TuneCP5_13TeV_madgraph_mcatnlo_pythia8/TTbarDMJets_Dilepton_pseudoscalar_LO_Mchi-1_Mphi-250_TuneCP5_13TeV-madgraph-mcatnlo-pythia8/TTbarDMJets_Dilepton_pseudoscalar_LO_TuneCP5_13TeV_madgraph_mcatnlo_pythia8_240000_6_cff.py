import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:20027', '1:23221', '1:13701', '1:14783', '1:14795', '1:14798', '1:13753', '1:13989', '1:19729', '1:15384', '1:14639', '1:16407', '1:14278', '1:14893', '1:23169', '1:13546', '1:19072', '1:15048', '1:19614', '1:19590', '1:19610', '1:16130', '1:17790', '1:21129', '1:21161', '1:15575', '1:21954', '1:24571', '1:23045', '1:24753', '1:12909', '1:15293', '1:15776', '1:16823', '1:19419', '1:16272', '1:16307', '1:14284', '1:14733', '1:15662', '1:17449', '1:17658', '1:12288', '1:11971', '1:13047', '1:13063', '1:17155', '1:12962', '1:12976', '1:12297', '1:12347', '1:12162', '1:12330', '1:12691', '1:17176', '1:17193', '1:14374', '1:14380', '1:12878', '1:20934', '1:23227', '1:13921', '1:13949', '1:14186', '1:14203', '1:14205', '1:21209', '1:21212', '1:21241', '1:24986', '1:23911', '1:14195', '1:14200', '1:14226', '1:14655', '1:16584', '1:15416', '1:15794', '1:13160', '1:13333', '1:20580', '1:12910', '1:16457', '1:16822', '1:24701', '1:24298', '1:19572', '1:19466', '1:16990', '1:19381', '1:19890', '1:15912', '1:15944', '1:19260', '1:19567', '1:19623', '1:24631', '1:23881', '1:12916', '1:17018', '1:12359', '1:12376', '1:12580', '1:12999', '1:22886', '1:18249', '1:18264', '1:18164', '1:18494', '1:18584', '1:18601', '1:18658', '1:18672', '1:18787', '1:23145', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/148F57B3-5812-EA11-B6E6-002590A2BCBC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7E63DD98-DBFE-E911-9513-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/A8DEEED0-1003-EA11-9D36-AC1F6B596102.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/24BCCF52-D2FD-E911-ACC1-002590DE6E8A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/1C3C42AE-27FE-E911-8818-3417EBE7062D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/10FCB283-8203-EA11-B898-506B4BB134E6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/660B22F0-DD02-EA11-B269-1866DAEB3370.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C02A524E-9E03-EA11-95FC-002590E3A0FC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/E4248C11-C002-EA11-AB10-0CC47AFCC662.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/0C0E7588-6CFE-E911-AA00-EC0D9A8225FE.root']);