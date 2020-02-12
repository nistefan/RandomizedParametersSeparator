import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:25413', '1:36729', '1:81153', '1:89979', '1:35604', '1:49256', '1:49996', '1:68764', '1:68877', '1:75629', '1:58623', '1:60101', '1:60309', '1:56331', '1:72707', '1:58083', '1:56623', '1:51619', '1:53264', '1:54077', '1:52892', '1:63866', '1:62272', '1:49331', '1:28358', '1:28916', '1:59547', '1:2090', '1:2387', '1:2144', '1:15075', '1:7934', '1:8403', '1:8193', '1:9246', '1:8559', '1:9408', '1:8501', '1:38829', '1:20861', '1:31625', '1:32173', '1:31556', '1:31696', '1:55800', '1:32750', '1:13635', '1:13683', '1:15217', '1:13076', '1:19173', '1:19453', '1:19795', '1:68625', '1:25155', '1:25293', '1:23777', '1:23812', '1:31561', '1:35943', '1:39029', '1:32408', '1:46616', '1:25349', '1:26594', '1:28873', '1:49846', '1:59620', '1:61383', '1:28247', '1:28263', '1:33111', '1:34125', '1:38545', '1:17502', '1:16074', '1:16285', '1:16332', '1:16463', '1:15672', '1:16003', '1:16020', '1:22209', '1:5236', '1:5296', '1:6924', '1:6933', '1:10481', '1:14120', '1:15654', '1:21546', '1:13274', '1:13663', '1:14888', '1:15089', '1:15317', '1:23356', '1:34477', '1:34744', '1:46540', '1:46550', '1:27568', '1:46736', '1:40137', '1:10440', '1:10442', '1:13285', '1:13533', '1:13592', '1:25995', '1:7502', '1:7060', '1:7149', '1:14909', '1:15255', '1:15288', '1:9287', '1:9259', '1:9365', '1:9378', '1:9403', '1:9483', '1:7138', '1:7227', '1:6860', '1:7051', '1:7099', '1:7107', '1:7140', '1:7243', '1:6788', '1:23180', '1:50891', '1:51339', '1:9085', '1:9590', '1:9631', '1:16757', '1:16215', '1:87091', '1:29619', '1:30127', '1:84990', '1:14184', '1:16594', '1:20131', '1:20226', '1:30733', '1:30743', '1:61192', '1:53240', '1:53045', '1:53578', '1:56030', '1:56240', '1:91001', '1:62750', '1:67927', '1:56726', '1:56750', '1:58170', '1:58190', '1:58196', '1:29807', '1:29998', '1:36145', '1:61642', '1:61807', '1:61884', '1:62040', '1:62121', '1:2367', '1:3385', '1:4203', '1:4423', '1:4946', '1:19036', '1:19996', '1:21373', '1:21255', '1:21324', '1:36454', '1:31269', '1:32366', '1:29881', '1:36199', '1:32699', '1:32718', '1:33222', '1:36306', '1:36320', '1:36416', '1:36417', '1:36532', '1:36564', '1:36566', '1:36648', '1:55690', '1:50911', '1:50959', '1:51510', '1:51876', '1:51485', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8A52D68A-9716-EA11-8A46-C81F66C09A78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3AA8A739-3B1A-EA11-8F16-0025901D08F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6C8ECEC3-DC18-EA11-A954-246E96D149A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DAB73933-B217-EA11-85E7-24BE05C3CBE1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E2A83DB0-0518-EA11-9905-FA163ECADB68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/46514FD2-CA17-EA11-A746-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/5CECA162-FA17-EA11-9B4F-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/18E400F5-FF17-EA11-A992-FA163E9F39BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DEE6096F-1D18-EA11-99A4-FA163E977168.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/404013D1-151C-EA11-A760-588A5AAEEBB8.root']);