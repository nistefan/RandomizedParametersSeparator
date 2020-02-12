import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:14332', '1:14671', '1:14817', '1:14843', '1:14886', '1:44418', '1:91704', '1:98906', '1:65713', '1:19896', '1:26360', '1:19047', '1:19376', '1:19538', '1:42952', '1:44717', '1:66726', '1:62948', '1:72197', '1:91266', '1:82030', '1:82287', '1:83314', '1:83392', '1:83509', '1:83865', '1:84135', '1:28502', '1:29665', '1:47753', '1:59068', '1:74208', '1:81637', '1:67516', '1:95621', '1:20320', '1:25667', '1:25855', '1:43779', '1:70147', '1:70794', '1:64886', '1:72222', '1:73059', '1:90401', '1:94149', '1:20100', '1:31299', '1:83840', '1:4814', '1:5172', '1:8874', '1:15084', '1:101814', '1:67881', '1:24636', '1:18022', '1:18467', '1:28369', '1:40894', '1:44335', '1:28475', '1:39726', '1:44838', '1:90887', '1:25121', '1:25153', '1:25352', '1:25367', '1:25372', '1:25446', '1:4358', '1:7745', '1:20747', '1:77708', '1:98841', '1:86150', '1:92487', '1:92500', '1:47378', '1:47808', '1:85025', '1:85956', '1:52180', '1:52190', '1:52244', '1:70452', '1:70468', '1:70491', '1:70551', '1:96674', '1:30026', '1:47643', '1:105280', '1:97833', '1:89391', '1:96704', '1:87888', '1:88525', '1:88535', '1:28248', '1:39422', '1:28404', '1:58518', '1:106142', '1:103892', '1:103755', '1:101246', '1:4797', '1:5857', '1:5302', '1:5798', '1:6660', '1:7231', '1:7332', '1:7527', '1:13759', '1:62950', '1:62881', '1:20340', '1:20441', '1:26193', '1:24403', '1:60468', '1:98404', '1:98776', '1:102378', '1:104427', '1:27482', '1:60792', '1:61012', '1:62506', '1:29045', '1:30589', '1:52302', '1:62688', '1:5689', '1:5826', '1:5632', '1:9826', '1:9965', '1:10012', '1:10384', '1:11753', '1:15565', '1:14523', '1:9434', '1:9811', '1:10345', '1:14579', '1:14580', '1:16107', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C75EAD7-A60A-EA11-B2EA-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CAA33E3-B40A-EA11-B217-0CC47A4C8EB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0C7BD80-B30A-EA11-990C-0CC47A7C345E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/827A94E9-460C-EA11-9197-0CC47A7C34D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C25D68E-CA0A-EA11-A4D3-0CC47A4D762E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4F23B9-260F-EA11-80C3-0CC47A4D7690.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A38857F-43F9-E911-9334-0CC47A5FBE21.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2A529D76-BC12-EA11-85B1-90B11C070100.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80404779-FBF6-E911-8982-AC1F6B0F71D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A13F5EF-28F2-E911-9B0D-00215AA64960.root']);