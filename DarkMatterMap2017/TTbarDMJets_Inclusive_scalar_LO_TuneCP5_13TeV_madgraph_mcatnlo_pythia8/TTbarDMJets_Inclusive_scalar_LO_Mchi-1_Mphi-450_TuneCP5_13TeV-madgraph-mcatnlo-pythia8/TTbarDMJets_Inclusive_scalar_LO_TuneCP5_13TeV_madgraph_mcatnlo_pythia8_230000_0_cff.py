import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2491', '1:5430', '1:9478', '1:19155', '1:21368', '1:38169', '1:39959', '1:40869', '1:8173', '1:8442', '1:8489', '1:13271', '1:13483', '1:13881', '1:18837', '1:21773', '1:24300', '1:27468', '1:35913', '1:36634', '1:38083', '1:38458', '1:38492', '1:38793', '1:16958', '1:17735', '1:17890', '1:20259', '1:20672', '1:40642', '1:49144', '1:50074', '1:50372', '1:51343', '1:58115', '1:61154', '1:62826', '1:68200', '1:75495', '1:75171', '1:76470', '1:59137', '1:60700', '1:68177', '1:1440', '1:5230', '1:2673', '1:3229', '1:5316', '1:5652', '1:21127', '1:21136', '1:18980', '1:36994', '1:49252', '1:49410', '1:24159', '1:26410', '1:26781', '1:36379', '1:56058', '1:27226', '1:24139', '1:27650', '1:63803', '1:71582', '1:80965', '1:6129', '1:6178', '1:7672', '1:13189', '1:15058', '1:64527', '1:32843', '1:31912', '1:33676', '1:34328', '1:50876', '1:51586', '1:16612', '1:25468', '1:29132', '1:29705', '1:33233', '1:26887', '1:38196', '1:81068', '1:81586', '1:81610', '1:86045', '1:91694', '1:7522', '1:9578', '1:9964', '1:10942', '1:14551', '1:56900', '1:76248', '1:69018', '1:76135', '1:68265', '1:76214', '1:64244', '1:76029', '1:870', '1:1537', '1:1998', '1:2071', '1:2774', '1:2999', '1:4524', '1:4943', '1:17799', '1:38251', '1:40312', '1:60028', '1:60789', '1:6532', '1:7019', '1:7447', '1:6426', '1:8580', '1:6693', '1:6822', '1:10307', '1:10827', '1:10385', '1:14419', '1:56367', '1:56540', '1:13823', '1:13304', '1:13945', '1:15776', '1:15800', '1:16536', '1:16591', '1:17442', '1:17682', '1:23635', '1:30147', '1:79716', '1:85843', '1:50113', '1:52571', '1:56199', '1:61029', '1:61925', '1:85497', '1:80362', '1:81133', '1:91015', '1:28281', '1:28489', '1:33449', '1:24498', '1:27534', '1:31167', '1:35458', '1:37335', '1:32666', '1:54411', '1:54516', '1:52024', '1:56652', '1:60489', '1:37305', '1:76458', '1:80152', '1:4351', '1:7370', '1:20734', '1:63455', '1:64857', '1:77513', '1:75164', '1:77367', '1:91294', '1:74751', '1:63262', '1:63658', '1:63673', '1:63760', '1:63573', '1:63700', '1:99270', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/440F2EF5-E1F2-E911-9C42-3CFDFE639760.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/084EC564-3BF4-E911-BB13-782BCB398AB3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1AB17DBB-D1F2-E911-915F-F01FAFE5F67D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D2F07667-1BF3-E911-9149-1866DA7F96FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/623CBCFE-5DF3-E911-A913-1866DA85D853.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D6F9C4ED-BDF6-E911-A882-F0D4E2E52394.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4293777-74F7-E911-A059-EC0D9A82237E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BAB2D1CF-4BF6-E911-B5F6-003048F59755.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5E84A7CC-2EF8-E911-816D-0CC47AA989C4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A742CF5-FEF8-E911-8BF1-AC1F6B0DE490.root']);