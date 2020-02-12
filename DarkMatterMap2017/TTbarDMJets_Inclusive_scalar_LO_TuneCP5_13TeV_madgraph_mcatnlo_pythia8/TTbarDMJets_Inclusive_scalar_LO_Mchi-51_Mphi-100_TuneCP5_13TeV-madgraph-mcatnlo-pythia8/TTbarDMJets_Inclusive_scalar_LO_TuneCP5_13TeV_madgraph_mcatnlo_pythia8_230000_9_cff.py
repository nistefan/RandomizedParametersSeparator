import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:18614', '1:40928', '1:56556', '1:61022', '1:68650', '1:68926', '1:76354', '1:62600', '1:62751', '1:67848', '1:62308', '1:62880', '1:67546', '1:54158', '1:51539', '1:52949', '1:53515', '1:61208', '1:62876', '1:68431', '1:68869', '1:74300', '1:97682', '1:99937', '1:99157', '1:99274', '1:30318', '1:32438', '1:38333', '1:39904', '1:46088', '1:55637', '1:55761', '1:62243', '1:69076', '1:50639', '1:55098', '1:67603', '1:56405', '1:63138', '1:56300', '1:60769', '1:22822', '1:13137', '1:13374', '1:13884', '1:15682', '1:13319', '1:24304', '1:24828', '1:46893', '1:51819', '1:53445', '1:56076', '1:32949', '1:34619', '1:37035', '1:28597', '1:28766', '1:28776', '1:59745', '1:60241', '1:61508', '1:59259', '1:59289', '1:59436', '1:59735', '1:59799', '1:59852', '1:72823', '1:55651', '1:74423', '1:75183', '1:95615', '1:97317', '1:97362', '1:60888', '1:61280', '1:61582', '1:64068', '1:64300', '1:64543', '1:64563', '1:67137', '1:67253', '1:67331', '1:67587', '1:72223', '1:73263', '1:73311', '1:101784', '1:26805', '1:26981', '1:33066', '1:38279', '1:38355', '1:99139', '1:101880', '1:81897', '1:94534', '1:23179', '1:23423', '1:23738', '1:24516', '1:30210', '1:30421', '1:31995', '1:51025', '1:49925', '1:50098', '1:62637', '1:62477', '1:62601', '1:62651', '1:85265', '1:85357', '1:85427', '1:85458', '1:85600', '1:85717', '1:85991', '1:86353', '1:30033', '1:39460', '1:39705', '1:39866', '1:39873', '1:40384', '1:40797', '1:72672', '1:91905', '1:91997', '1:73157', '1:73181', '1:73206', '1:76560', '1:78019', '1:77570', '1:79213', '1:91652', '1:98329', '1:76082', '1:78712', '1:78785', '1:78948', '1:88094', '1:88110', '1:86443', '1:86672', '1:86809', '1:86964', '1:88098', '1:3124', '1:5856', '1:5894', '1:16632', '1:16732', '1:49063', '1:50578', '1:50728', '1:52001', '1:18439', '1:20092', '1:20213', '1:54037', '1:54162', '1:54007', '1:54276', '1:52809', '1:53048', '1:53056', '1:56614', '1:56869', '1:69050', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/183425A0-2CF9-E911-8A59-0CC47AC17502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/14013B83-ED0C-EA11-A969-0CC47A4C8E16.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D8BE5B85-CD00-EA11-8D89-008CFA197DDC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8EA49950-280B-EA11-8D88-0CC47A7C353E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C80BC002-AE01-EA11-8935-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94EED3C0-3913-EA11-9D36-003048F1C4AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CC49EA7-DAFA-E911-B4D9-549F3525C318.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7ED89422-6000-EA11-91BA-509A4C9EF8FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02A19D30-BF01-EA11-8C20-0CC47AF973C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/986C80F8-D001-EA11-B39E-509A4C9F8A64.root']);