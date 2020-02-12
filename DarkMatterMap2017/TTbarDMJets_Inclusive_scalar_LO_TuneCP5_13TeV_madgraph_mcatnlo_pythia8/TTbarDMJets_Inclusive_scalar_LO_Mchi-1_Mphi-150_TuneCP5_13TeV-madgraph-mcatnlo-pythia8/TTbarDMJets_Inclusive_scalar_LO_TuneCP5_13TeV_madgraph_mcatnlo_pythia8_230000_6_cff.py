import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:51205', '1:52319', '1:52837', '1:53215', '1:57280', '1:20604', '1:20724', '1:6274', '1:6944', '1:13563', '1:15798', '1:97465', '1:100479', '1:100684', '1:40426', '1:56780', '1:91380', '1:70015', '1:78624', '1:95862', '1:96314', '1:99155', '1:99371', '1:61909', '1:63593', '1:62824', '1:62976', '1:31120', '1:64745', '1:77794', '1:77984', '1:79209', '1:79284', '1:79327', '1:79431', '1:79776', '1:77479', '1:77355', '1:99242', '1:99310', '1:1067', '1:3013', '1:4577', '1:10542', '1:14690', '1:13353', '1:10612', '1:22587', '1:16938', '1:18436', '1:20350', '1:26947', '1:38660', '1:543', '1:3696', '1:5656', '1:17836', '1:29498', '1:33669', '1:31208', '1:34924', '1:35705', '1:37113', '1:34190', '1:34389', '1:39550', '1:37055', '1:70076', '1:22591', '1:22845', '1:63950', '1:63978', '1:22814', '1:22962', '1:22964', '1:61297', '1:61538', '1:61629', '1:71084', '1:72359', '1:69674', '1:74880', '1:16486', '1:18107', '1:20013', '1:86694', '1:89294', '1:73787', '1:78417', '1:20264', '1:50557', '1:54183', '1:54247', '1:54352', '1:54360', '1:54406', '1:58795', '1:74910', '1:53335', '1:53380', '1:53738', '1:52899', '1:57005', '1:57208', '1:53964', '1:58881', '1:58899', '1:54410', '1:54451', '1:63427', '1:68457', '1:68557', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C40F6AE3-3913-EA11-9EE4-20CF305B05CE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D84D1EC9-3913-EA11-8DC0-0CC47A57CBCC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4687DD-3913-EA11-8B59-0CC47AFF23F2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96A24FE4-3913-EA11-AF76-38EAA78D8AF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A620E5CA-3913-EA11-A21F-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7EE607DD-3913-EA11-9A4B-98039B3B01BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50B737E7-3913-EA11-9E68-BC305B390AA7.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FC784550-7BF7-E911-AD10-0CC47A2B0392.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/36D0ACF7-0D0B-EA11-A998-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC089C57-AB01-EA11-8681-509A4C9EF929.root']);