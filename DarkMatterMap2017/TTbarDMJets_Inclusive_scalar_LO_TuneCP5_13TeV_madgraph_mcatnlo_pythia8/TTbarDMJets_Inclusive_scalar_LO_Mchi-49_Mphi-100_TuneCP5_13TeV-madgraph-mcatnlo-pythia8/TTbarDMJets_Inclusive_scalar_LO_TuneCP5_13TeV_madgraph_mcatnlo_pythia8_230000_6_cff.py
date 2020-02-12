import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:51443', '1:51525', '1:51614', '1:51769', '1:51792', '1:50066', '1:50520', '1:10884', '1:21701', '1:13853', '1:97109', '1:51047', '1:73078', '1:87860', '1:99297', '1:99167', '1:99262', '1:99563', '1:99655', '1:99750', '1:76190', '1:63459', '1:63076', '1:67093', '1:79292', '1:79635', '1:77487', '1:77468', '1:77565', '1:99389', '1:99207', '1:99460', '1:99766', '1:4153', '1:7395', '1:18812', '1:10062', '1:10790', '1:18717', '1:33384', '1:33890', '1:36482', '1:38395', '1:38465', '1:64099', '1:69625', '1:2470', '1:5748', '1:25034', '1:58858', '1:61002', '1:61110', '1:61118', '1:71234', '1:71429', '1:61942', '1:78714', '1:101998', '1:102153', '1:102395', '1:22939', '1:28764', '1:68600', '1:61400', '1:61611', '1:78373', '1:81004', '1:14762', '1:20839', '1:22137', '1:89555', '1:90424', '1:99742', '1:77646', '1:73859', '1:73949', '1:55103', '1:54229', '1:54317', '1:61299', '1:62122', '1:62251', '1:56558', '1:58268', '1:74572', '1:75810', '1:75851', '1:52586', '1:52811', '1:52829', '1:53420', '1:53688', '1:61462', '1:57103', '1:57110', '1:54397', '1:54424', '1:54820', '1:63398', '1:69617', '1:75089', '1:76234', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C40F6AE3-3913-EA11-9EE4-20CF305B05CE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D84D1EC9-3913-EA11-8DC0-0CC47A57CBCC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4687DD-3913-EA11-8B59-0CC47AFF23F2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96A24FE4-3913-EA11-AF76-38EAA78D8AF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A620E5CA-3913-EA11-A21F-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7EE607DD-3913-EA11-9A4B-98039B3B01BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50B737E7-3913-EA11-9E68-BC305B390AA7.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FC784550-7BF7-E911-AD10-0CC47A2B0392.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/36D0ACF7-0D0B-EA11-A998-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC089C57-AB01-EA11-8681-509A4C9EF929.root']);