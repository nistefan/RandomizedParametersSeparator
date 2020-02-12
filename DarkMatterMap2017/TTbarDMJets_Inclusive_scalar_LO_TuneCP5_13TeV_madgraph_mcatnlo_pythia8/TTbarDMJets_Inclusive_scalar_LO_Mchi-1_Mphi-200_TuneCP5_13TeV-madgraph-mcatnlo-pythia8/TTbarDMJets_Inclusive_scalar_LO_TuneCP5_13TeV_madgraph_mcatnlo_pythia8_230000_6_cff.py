import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:51630', '1:51250', '1:87579', '1:7250', '1:18523', '1:18911', '1:19598', '1:71246', '1:73490', '1:87576', '1:98690', '1:102296', '1:102330', '1:99085', '1:99193', '1:99293', '1:99515', '1:99843', '1:59084', '1:62994', '1:63707', '1:64549', '1:54199', '1:54819', '1:60753', '1:64238', '1:77657', '1:79313', '1:77261', '1:77403', '1:77415', '1:98921', '1:1092', '1:10711', '1:16041', '1:10348', '1:14319', '1:21784', '1:26575', '1:29290', '1:29621', '1:5698', '1:10607', '1:14567', '1:2214', '1:5709', '1:34271', '1:39629', '1:59375', '1:37495', '1:46527', '1:62830', '1:88989', '1:102075', '1:22382', '1:22639', '1:22641', '1:22895', '1:40063', '1:63847', '1:22945', '1:22978', '1:61432', '1:61500', '1:76971', '1:77081', '1:78916', '1:17798', '1:22418', '1:87605', '1:90458', '1:97866', '1:100033', '1:17710', '1:55036', '1:55204', '1:54319', '1:56631', '1:62125', '1:56916', '1:61592', '1:74540', '1:74583', '1:74920', '1:75434', '1:75800', '1:52819', '1:53432', '1:53536', '1:57258', '1:54507', '1:63390', '1:76240', '1:76265', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C40F6AE3-3913-EA11-9EE4-20CF305B05CE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D84D1EC9-3913-EA11-8DC0-0CC47A57CBCC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4687DD-3913-EA11-8B59-0CC47AFF23F2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96A24FE4-3913-EA11-AF76-38EAA78D8AF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A620E5CA-3913-EA11-A21F-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7EE607DD-3913-EA11-9A4B-98039B3B01BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50B737E7-3913-EA11-9E68-BC305B390AA7.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FC784550-7BF7-E911-AD10-0CC47A2B0392.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/36D0ACF7-0D0B-EA11-A998-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC089C57-AB01-EA11-8681-509A4C9EF929.root']);