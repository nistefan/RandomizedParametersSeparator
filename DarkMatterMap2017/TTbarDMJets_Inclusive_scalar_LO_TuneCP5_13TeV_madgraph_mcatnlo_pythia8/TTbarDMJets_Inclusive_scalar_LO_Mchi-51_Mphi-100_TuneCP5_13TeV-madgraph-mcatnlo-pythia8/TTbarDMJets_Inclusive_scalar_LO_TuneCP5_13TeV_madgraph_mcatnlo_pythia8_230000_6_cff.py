import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:34177', '1:50552', '1:50969', '1:50398', '1:14164', '1:20158', '1:8773', '1:9299', '1:72305', '1:73090', '1:73558', '1:78693', '1:87803', '1:96321', '1:101438', '1:99148', '1:99244', '1:99343', '1:99703', '1:100352', '1:75119', '1:76018', '1:76756', '1:76766', '1:61809', '1:63893', '1:64248', '1:54730', '1:54824', '1:55501', '1:67053', '1:79028', '1:79238', '1:77308', '1:77380', '1:77398', '1:77527', '1:98927', '1:99339', '1:99256', '1:99484', '1:3142', '1:14253', '1:10173', '1:14805', '1:29424', '1:55674', '1:69225', '1:3521', '1:8305', '1:2384', '1:10538', '1:14995', '1:19094', '1:34895', '1:32041', '1:37042', '1:60386', '1:37177', '1:37511', '1:46139', '1:46163', '1:62700', '1:77886', '1:71385', '1:81414', '1:71551', '1:101799', '1:3919', '1:22589', '1:22626', '1:22782', '1:22993', '1:63973', '1:69842', '1:22982', '1:22995', '1:61272', '1:61480', '1:61485', '1:61541', '1:80052', '1:81659', '1:94210', '1:16326', '1:20091', '1:21801', '1:81780', '1:88903', '1:89479', '1:94461', '1:95495', '1:87104', '1:94757', '1:100154', '1:72883', '1:73361', '1:80068', '1:78887', '1:20937', '1:18821', '1:54185', '1:54231', '1:62132', '1:62150', '1:56939', '1:58286', '1:74502', '1:74543', '1:74562', '1:52188', '1:52244', '1:52309', '1:52464', '1:52699', '1:52967', '1:53376', '1:53389', '1:57209', '1:57234', '1:53734', '1:58886', '1:54407', '1:54500', '1:63422', '1:63481', '1:63371', '1:64999', '1:67005', '1:67016', '1:67025', '1:67028', '1:67050', '1:69539', '1:69564', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C40F6AE3-3913-EA11-9EE4-20CF305B05CE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D84D1EC9-3913-EA11-8DC0-0CC47A57CBCC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4687DD-3913-EA11-8B59-0CC47AFF23F2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96A24FE4-3913-EA11-AF76-38EAA78D8AF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A620E5CA-3913-EA11-A21F-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7EE607DD-3913-EA11-9A4B-98039B3B01BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50B737E7-3913-EA11-9E68-BC305B390AA7.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FC784550-7BF7-E911-AD10-0CC47A2B0392.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/36D0ACF7-0D0B-EA11-A998-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC089C57-AB01-EA11-8681-509A4C9EF929.root']);