import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:32821', '1:39349', '1:46416', '1:46605', '1:58516', '1:59242', '1:90286', '1:43502', '1:45654', '1:103030', '1:105168', '1:105380', '1:105243', '1:103391', '1:103363', '1:103431', '1:2805', '1:2827', '1:3107', '1:3211', '1:3212', '1:3283', '1:3365', '1:4639', '1:5239', '1:5601', '1:5622', '1:5339', '1:5563', '1:9393', '1:3703', '1:4863', '1:5069', '1:5173', '1:11899', '1:9501', '1:9548', '1:9647', '1:11462', '1:39174', '1:39270', '1:24157', '1:24908', '1:25021', '1:25361', '1:25807', '1:25388', '1:25612', '1:43468', '1:43150', '1:55958', '1:56163', '1:56208', '1:56528', '1:30203', '1:30329', '1:55412', '1:56060', '1:19668', '1:22154', '1:22463', '1:73978', '1:74293', '1:74528', '1:85038', '1:85190', '1:85338', '1:85524', '1:85549', '1:85580', '1:44153', '1:44424', '1:44613', '1:44658', '1:44715', '1:44687', '1:44689', '1:15413', '1:3158', '1:11694', '1:7317', '1:15825', '1:20042', '1:44690', '1:47536', '1:58559', '1:19375', '1:26052', '1:27220', '1:39433', '1:48611', '1:49148', '1:49729', '1:57412', '1:64656', '1:71709', '1:71828', '1:73247', '1:74150', '1:41286', '1:46903', '1:49269', '1:46633', '1:60339', '1:52567', '1:51792', '1:51809', '1:51825', '1:52952', '1:55091', '1:55354', '1:53085', '1:53169', '1:53212', '1:53226', '1:5754', '1:8381', '1:16537', '1:8963', '1:12988', '1:60848', '1:61914', '1:28775', '1:39495', '1:41509', '1:61159', '1:62328', '1:73336', '1:66162', '1:66649', '1:72558', '1:83508', '1:88668', '1:9790', '1:2910', '1:3625', '1:14430', '1:67053', '1:76946', '1:65588', '1:66071', '1:61928', '1:62255', '1:5877', '1:5044', '1:13270', '1:13630', '1:14556', '1:40788', '1:74032', '1:73651', '1:2304', '1:5748', '1:12215', '1:17310', '1:20587', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AAB00DE4-97F3-E911-A3C8-509A4C9EF8EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D28BE09F-34F2-E911-BBB7-509A4C9EF924.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8145C07-FDF2-E911-A902-509A4C9F8ADB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24CF0859-1FF5-E911-84A0-441EA1616D3A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8ABA5532-F3F4-E911-A0DF-00215AAA5746.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EC263BA-D9F2-E911-8E00-1866DA7F93EB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78B70150-BC12-EA11-8D6F-0CC47AFF23CE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FA6B6FC8-18F4-E911-A834-00259073E428.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C421938-2AF3-E911-9857-1866DA7F8ED8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/224CE38B-CBF2-E911-A69D-F01FAFE5F67D.root']);