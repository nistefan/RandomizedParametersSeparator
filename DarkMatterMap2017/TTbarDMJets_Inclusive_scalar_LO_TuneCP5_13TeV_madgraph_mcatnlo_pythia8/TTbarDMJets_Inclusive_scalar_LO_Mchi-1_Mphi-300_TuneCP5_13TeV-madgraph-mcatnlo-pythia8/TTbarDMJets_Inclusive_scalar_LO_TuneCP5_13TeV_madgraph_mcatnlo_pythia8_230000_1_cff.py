import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:7856', '1:10226', '1:5763', '1:34400', '1:35160', '1:32033', '1:51864', '1:60539', '1:6660', '1:6809', '1:8451', '1:9824', '1:15037', '1:15599', '1:10433', '1:15480', '1:19926', '1:32343', '1:59170', '1:59963', '1:61427', '1:58796', '1:59138', '1:59859', '1:34322', '1:55665', '1:67368', '1:71943', '1:74551', '1:70082', '1:23543', '1:26792', '1:29120', '1:19830', '1:14412', '1:15968', '1:20464', '1:21869', '1:20552', '1:21197', '1:31984', '1:51802', '1:52442', '1:58679', '1:60537', '1:51314', '1:52206', '1:50500', '1:52706', '1:68407', '1:74824', '1:76534', '1:98936', '1:97917', '1:99537', '1:99698', '1:100011', '1:100021', '1:100045', '1:100084', '1:100167', '1:54378', '1:54818', '1:54858', '1:54891', '1:56746', '1:78579', '1:78755', '1:78998', '1:78541', '1:88709', '1:89030', '1:71613', '1:75690', '1:76117', '1:76565', '1:88940', '1:88342', '1:101732', '1:17788', '1:21679', '1:30883', '1:35018', '1:39581', '1:31024', '1:53016', '1:53534', '1:52177', '1:53090', '1:75435', '1:1517', '1:1589', '1:1715', '1:1724', '1:37890', '1:37893', '1:77177', '1:77249', '1:77275', '1:72490', '1:72498', '1:72875', '1:87720', '1:88125', '1:88215', '1:88286', '1:88361', '1:88988', '1:71155', '1:71288', '1:71413', '1:71532', '1:71553', '1:71606', '1:94779', '1:94849', '1:94897', '1:95221', '1:95627', '1:95731', '1:98146', '1:98923', '1:99076', '1:99336', '1:35181', '1:35380', '1:35565', '1:69896', '1:69928', '1:69945', '1:71558', '1:71939', '1:69831', '1:75381', '1:75470', '1:75506', '1:76432', '1:56259', '1:56494', '1:56801', '1:57132', '1:56315', '1:56914', '1:57076', '1:57383', '1:61158', '1:61287', '1:61356', '1:61390', '1:63085', '1:63177', '1:61618', '1:63077', '1:63108', '1:63155', '1:71643', '1:101036', '1:750', '1:8631', '1:15015', '1:15820', '1:16765', '1:19703', '1:72641', '1:72809', '1:72911', '1:72960', '1:73018', '1:73236', '1:76908', '1:76919', '1:76943', '1:40569', '1:53275', '1:53983', '1:27408', '1:53072', '1:87268', '1:87348', '1:101042', '1:101487', '1:100316', '1:100921', '1:73481', '1:86501', '1:86605', '1:88523', '1:87443', '1:96357', '1:96488', '1:96691', '1:96925', '1:97165', '1:97431', '1:97433', '1:100486', '1:100601', '1:100761', '1:100859', '1:101826', '1:88574', '1:89264', '1:89594', '1:89647', '1:89570', '1:89784', '1:89876', '1:95996', '1:96215', '1:96403', '1:96413', '1:96964', '1:97149', '1:100373', '1:101944', '1:100511', '1:101005', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CF3F789-48F8-E911-9E95-AC1F6B34AC86.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94F3A535-95F8-E911-B0C4-A4BF01025A8B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC6D87E5-FEF8-E911-860A-20040FE9CF40.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E13167A-04F9-E911-822D-AC1F6B0DE296.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02456201-BDFC-E911-8979-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6336465-ACFA-E911-BCEA-0CC47AD98D6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6EDE0848-29FD-E911-8BAF-00215A49197E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/721E3057-28FC-E911-AF04-38EAA78D8960.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E05E587-1AFD-E911-8B60-002590DE6E1E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2236C272-34FD-E911-A005-0CC47A7E6B00.root']);