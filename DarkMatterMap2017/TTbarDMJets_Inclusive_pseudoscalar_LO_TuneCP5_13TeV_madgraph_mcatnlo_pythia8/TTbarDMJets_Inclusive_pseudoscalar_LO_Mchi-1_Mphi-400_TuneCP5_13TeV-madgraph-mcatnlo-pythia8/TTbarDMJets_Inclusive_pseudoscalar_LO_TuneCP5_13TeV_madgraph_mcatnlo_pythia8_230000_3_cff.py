import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:23915', '1:52860', '1:54606', '1:60530', '1:93393', '1:93916', '1:60378', '1:61934', '1:62276', '1:61587', '1:61938', '1:73211', '1:88731', '1:98500', '1:103700', '1:103840', '1:71279', '1:75193', '1:75605', '1:78053', '1:72844', '1:16918', '1:31300', '1:31326', '1:31419', '1:31456', '1:51997', '1:53148', '1:55044', '1:22883', '1:22956', '1:29304', '1:29741', '1:46797', '1:46871', '1:46877', '1:46900', '1:48149', '1:53269', '1:24532', '1:12083', '1:17742', '1:24158', '1:18383', '1:28391', '1:56353', '1:58526', '1:22695', '1:29652', '1:27049', '1:77040', '1:78527', '1:79124', '1:81491', '1:87578', '1:52460', '1:54115', '1:54518', '1:85449', '1:51699', '1:52028', '1:67711', '1:71187', '1:70823', '1:71962', '1:72361', '1:72385', '1:73220', '1:83615', '1:83653', '1:83731', '1:83772', '1:97797', '1:83157', '1:54734', '1:54823', '1:61698', '1:58619', '1:59045', '1:59293', '1:59416', '1:61571', '1:60980', '1:62892', '1:84234', '1:84534', '1:83101', '1:61119', '1:82528', '1:83045', '1:83946', '1:2925', '1:3965', '1:6384', '1:7218', '1:7345', '1:7484', '1:7640', '1:7994', '1:12038', '1:12366', '1:23416', '1:51990', '1:51964', '1:52440', '1:52476', '1:52718', '1:53002', '1:53515', '1:59486', '1:59641', '1:60587', '1:61103', '1:61287', '1:61343', '1:61979', '1:54648', '1:54862', '1:54910', '1:57072', '1:3297', '1:16276', '1:60781', '1:65612', '1:88197', '1:65304', '1:17789', '1:19277', '1:19329', '1:26066', '1:30254', '1:61998', '1:74560', '1:75968', '1:80065', '1:101062', '1:90019', '1:60663', '1:95028', '1:8950', '1:28772', '1:47552', '1:89138', '1:73486', '1:82419', '1:84498', '1:88051', '1:90976', '1:91074', '1:70537', '1:83902', '1:4464', '1:5240', '1:5549', '1:8385', '1:2414', '1:2674', '1:2831', '1:2708', '1:2975', '1:3172', '1:7050', '1:13421', '1:13643', '1:14003', '1:15448', '1:23739', '1:23768', '1:45464', '1:45682', '1:45854', '1:49501', '1:49464', '1:49494', '1:49688', '1:21325', '1:21937', '1:31341', '1:31356', '1:31631', '1:31824', '1:31973', '1:48892', '1:51179', '1:51242', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E0B77C2-ACF2-E911-B839-44A8424762AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3A1BE4F7-5CF4-E911-B89E-00259073E40A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A4577A3-2BF6-E911-94E0-0CC47AD98D00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CC7FFA5E-9BF6-E911-93AA-0CC47AF97150.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D01DA64A-9AF5-E911-A0E9-D4856445E5A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/889C5882-D8F5-E911-8B63-FA163EE28B37.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8A4349A-CFF6-E911-AEDB-0CC47A2B03A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE4574FE-FCF6-E911-91C6-00259048AC12.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BEF69588-68F6-E911-821B-FA163EEB438E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/28FDC844-0CF8-E911-8538-002590D425C0.root']);