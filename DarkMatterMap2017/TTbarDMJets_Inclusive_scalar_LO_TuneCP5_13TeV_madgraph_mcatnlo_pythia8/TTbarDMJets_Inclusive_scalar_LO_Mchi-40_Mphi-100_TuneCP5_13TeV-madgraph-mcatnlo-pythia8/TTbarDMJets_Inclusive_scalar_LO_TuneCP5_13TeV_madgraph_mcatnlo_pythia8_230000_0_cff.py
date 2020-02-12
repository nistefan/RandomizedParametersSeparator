import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1620', '1:4602', '1:5206', '1:454', '1:1447', '1:3589', '1:2356', '1:1241', '1:3540', '1:7896', '1:10477', '1:19266', '1:21182', '1:22973', '1:33746', '1:38012', '1:38161', '1:5619', '1:9954', '1:14156', '1:13670', '1:16504', '1:33772', '1:33808', '1:18618', '1:18830', '1:19943', '1:20784', '1:39771', '1:49570', '1:60565', '1:64917', '1:67832', '1:69103', '1:3615', '1:4165', '1:10091', '1:14233', '1:15787', '1:24151', '1:49182', '1:49791', '1:46426', '1:49475', '1:50742', '1:51467', '1:26971', '1:36071', '1:36938', '1:26169', '1:26952', '1:33959', '1:17932', '1:70251', '1:91190', '1:73767', '1:85971', '1:7923', '1:10630', '1:10849', '1:13497', '1:15692', '1:28840', '1:32318', '1:38108', '1:32553', '1:34775', '1:30737', '1:32335', '1:14169', '1:14710', '1:15957', '1:18334', '1:19351', '1:18746', '1:33179', '1:33391', '1:33508', '1:38362', '1:80691', '1:81631', '1:30643', '1:40407', '1:39217', '1:8127', '1:8172', '1:13141', '1:15103', '1:15970', '1:27135', '1:30611', '1:27616', '1:46673', '1:56332', '1:56909', '1:68290', '1:68467', '1:635', '1:1265', '1:1851', '1:2401', '1:2764', '1:3816', '1:4471', '1:4218', '1:17304', '1:19406', '1:36537', '1:37223', '1:40518', '1:46452', '1:56319', '1:6877', '1:7040', '1:6490', '1:6550', '1:10191', '1:13345', '1:13361', '1:14000', '1:14379', '1:23326', '1:24255', '1:27426', '1:23740', '1:34842', '1:79034', '1:81666', '1:91297', '1:61133', '1:81333', '1:31465', '1:31796', '1:25881', '1:28369', '1:62483', '1:27818', '1:27917', '1:28537', '1:32936', '1:54828', '1:62702', '1:51469', '1:52715', '1:57266', '1:58793', '1:39870', '1:50048', '1:62258', '1:79937', '1:85214', '1:79536', '1:7500', '1:51825', '1:61179', '1:63057', '1:77980', '1:79095', '1:79173', '1:88901', '1:101514', '1:63930', '1:70976', '1:80563', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/440F2EF5-E1F2-E911-9C42-3CFDFE639760.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/084EC564-3BF4-E911-BB13-782BCB398AB3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1AB17DBB-D1F2-E911-915F-F01FAFE5F67D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D2F07667-1BF3-E911-9149-1866DA7F96FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/623CBCFE-5DF3-E911-A913-1866DA85D853.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D6F9C4ED-BDF6-E911-A882-F0D4E2E52394.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4293777-74F7-E911-A059-EC0D9A82237E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BAB2D1CF-4BF6-E911-B5F6-003048F59755.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5E84A7CC-2EF8-E911-816D-0CC47AA989C4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A742CF5-FEF8-E911-8BF1-AC1F6B0DE490.root']);