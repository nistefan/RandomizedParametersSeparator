import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:6840', '1:4747', '1:939', '1:7605', '1:7622', '1:20593', '1:38498', '1:17850', '1:24319', '1:27192', '1:33872', '1:38919', '1:38461', '1:13523', '1:16162', '1:18756', '1:28138', '1:49964', '1:54220', '1:62313', '1:62421', '1:62679', '1:62852', '1:63384', '1:61575', '1:68021', '1:75090', '1:75111', '1:75330', '1:69458', '1:62413', '1:58922', '1:60183', '1:64494', '1:67298', '1:67567', '1:3402', '1:2376', '1:5546', '1:1168', '1:13828', '1:16481', '1:17097', '1:21112', '1:22417', '1:9728', '1:49243', '1:49301', '1:50204', '1:50949', '1:26146', '1:26942', '1:29936', '1:25885', '1:29536', '1:29959', '1:36808', '1:23528', '1:24227', '1:24261', '1:24318', '1:24490', '1:28769', '1:37904', '1:72147', '1:30202', '1:46021', '1:85924', '1:91062', '1:2668', '1:15355', '1:16302', '1:26495', '1:26535', '1:26838', '1:28718', '1:33647', '1:28075', '1:28517', '1:28999', '1:32818', '1:30340', '1:30453', '1:39347', '1:16083', '1:18372', '1:19613', '1:25695', '1:29037', '1:36356', '1:100467', '1:80704', '1:81588', '1:27011', '1:46883', '1:49088', '1:7529', '1:8030', '1:13522', '1:14704', '1:15320', '1:35183', '1:56368', '1:67469', '1:69344', '1:69900', '1:745', '1:982', '1:4775', '1:5380', '1:15859', '1:36457', '1:36222', '1:37110', '1:46654', '1:63622', '1:46487', '1:58490', '1:60790', '1:8571', '1:6153', '1:8807', '1:6046', '1:6776', '1:8596', '1:10660', '1:13388', '1:50696', '1:60522', '1:54302', '1:13613', '1:15763', '1:67597', '1:24480', '1:35609', '1:39626', '1:39745', '1:27311', '1:77898', '1:56071', '1:56100', '1:57252', '1:61524', '1:81388', '1:91005', '1:33422', '1:28003', '1:33659', '1:32467', '1:34522', '1:37196', '1:37352', '1:35309', '1:53328', '1:54825', '1:61591', '1:57130', '1:60699', '1:46058', '1:40328', '1:54157', '1:77590', '1:77939', '1:79848', '1:354', '1:14172', '1:20538', '1:20578', '1:52734', '1:79944', '1:81710', '1:85652', '1:88313', '1:72020', '1:73667', '1:63566', '1:63695', '1:63716', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/440F2EF5-E1F2-E911-9C42-3CFDFE639760.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/084EC564-3BF4-E911-BB13-782BCB398AB3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1AB17DBB-D1F2-E911-915F-F01FAFE5F67D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D2F07667-1BF3-E911-9149-1866DA7F96FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/623CBCFE-5DF3-E911-A913-1866DA85D853.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D6F9C4ED-BDF6-E911-A882-F0D4E2E52394.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4293777-74F7-E911-A059-EC0D9A82237E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BAB2D1CF-4BF6-E911-B5F6-003048F59755.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5E84A7CC-2EF8-E911-816D-0CC47AA989C4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A742CF5-FEF8-E911-8BF1-AC1F6B0DE490.root']);