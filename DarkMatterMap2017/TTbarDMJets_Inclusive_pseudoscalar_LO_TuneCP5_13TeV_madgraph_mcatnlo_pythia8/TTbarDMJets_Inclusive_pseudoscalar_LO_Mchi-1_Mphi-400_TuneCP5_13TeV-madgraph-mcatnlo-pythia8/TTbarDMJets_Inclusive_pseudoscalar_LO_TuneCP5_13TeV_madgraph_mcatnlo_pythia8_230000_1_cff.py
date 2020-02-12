import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:32501', '1:32825', '1:51190', '1:51317', '1:51379', '1:53194', '1:53396', '1:47604', '1:47932', '1:53696', '1:8325', '1:5703', '1:6476', '1:6602', '1:6940', '1:7327', '1:7723', '1:7724', '1:12813', '1:13117', '1:13459', '1:14130', '1:14730', '1:9564', '1:18174', '1:18314', '1:18376', '1:18452', '1:18476', '1:18567', '1:18491', '1:18684', '1:18838', '1:18975', '1:18285', '1:18303', '1:18459', '1:18538', '1:18779', '1:18879', '1:18978', '1:19928', '1:19999', '1:20008', '1:28009', '1:28181', '1:28461', '1:18663', '1:18721', '1:41602', '1:28353', '1:28509', '1:28683', '1:54658', '1:40992', '1:2856', '1:3093', '1:9147', '1:57023', '1:58225', '1:54166', '1:42096', '1:42570', '1:42622', '1:42793', '1:85194', '1:85392', '1:85534', '1:86669', '1:86867', '1:103047', '1:103213', '1:66581', '1:70277', '1:85511', '1:56954', '1:57298', '1:57390', '1:82466', '1:83396', '1:1653', '1:6341', '1:7814', '1:7951', '1:7326', '1:10216', '1:10349', '1:10360', '1:11519', '1:10709', '1:10830', '1:11194', '1:11664', '1:11681', '1:11915', '1:12483', '1:12694', '1:14423', '1:14491', '1:14926', '1:14177', '1:57726', '1:57727', '1:58103', '1:58706', '1:59124', '1:7960', '1:8965', '1:8887', '1:9050', '1:9058', '1:9308', '1:9503', '1:8806', '1:8894', '1:12882', '1:12905', '1:31074', '1:31215', '1:31455', '1:17421', '1:17551', '1:17613', '1:17626', '1:17650', '1:17696', '1:17876', '1:41805', '1:41670', '1:45640', '1:45844', '1:54794', '1:18813', '1:80633', '1:78375', '1:21274', '1:21687', '1:23170', '1:91123', '1:97595', '1:97638', '1:97850', '1:98110', '1:7425', '1:8869', '1:8991', '1:25445', '1:25607', '1:25741', '1:39919', '1:44199', '1:44457', '1:56320', '1:56390', '1:93743', '1:14171', '1:21416', '1:21641', '1:21698', '1:21763', '1:21779', '1:21880', '1:26383', '1:26452', '1:57405', '1:59836', '1:60010', '1:60135', '1:60788', '1:61523', '1:62737', '1:98478', '1:92260', '1:101326', '1:1695', '1:4015', '1:4688', '1:5543', '1:6082', '1:4137', '1:27055', '1:39571', '1:75372', '1:51716', '1:54931', '1:15228', '1:17919', '1:26897', '1:31928', '1:23002', '1:26980', '1:87202', '1:95282', '1:95856', '1:96340', '1:97176', '1:90290', '1:95271', '1:97642', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90043704-20FC-E911-8078-0CC47AFCC3D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/58F7196A-76FC-E911-8198-0025905C96E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B65A1C1B-7FFC-E911-92D1-0CC47AFCC392.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/30FB16E9-BC12-EA11-A843-7CD30AC03722.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70BD48D5-3CF5-E911-BBCD-D4856445E5A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E131ABC-63F2-E911-BBAD-441EA157ADE4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/00610B13-6BF2-E911-832F-98039B3B01B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2E996FF0-01F5-E911-BFCE-D4856444A744.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/501EAB60-EC02-EA11-9994-0CC47AFCC6B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3AF7C78E-7106-EA11-9305-0025905C3E68.root']);