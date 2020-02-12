import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:3840', '1:4037', '1:4074', '1:20290', '1:29661', '1:4434', '1:4441', '1:4444', '1:4805', '1:4847', '1:12469', '1:8650', '1:9160', '1:9658', '1:17741', '1:21564', '1:57466', '1:23267', '1:10280', '1:13055', '1:26199', '1:26276', '1:26329', '1:26502', '1:26515', '1:26705', '1:26901', '1:33642', '1:34865', '1:36331', '1:36342', '1:36622', '1:58014', '1:58523', '1:57933', '1:89245', '1:94089', '1:65401', '1:38370', '1:37634', '1:59857', '1:57922', '1:58242', '1:58549', '1:58833', '1:59275', '1:58643', '1:37823', '1:52558', '1:38819', '1:60217', '1:72622', '1:75138', '1:56490', '1:56362', '1:56427', '1:56322', '1:81825', '1:8536', '1:10691', '1:22606', '1:16824', '1:28619', '1:29244', '1:29204', '1:17988', '1:18461', '1:17898', '1:18008', '1:18046', '1:18113', '1:18208', '1:19864', '1:35846', '1:24296', '1:40055', '1:24812', '1:22422', '1:21963', '1:22896', '1:24067', '1:46420', '1:23006', '1:23184', '1:23674', '1:23728', '1:24285', '1:23886', '1:28953', '1:37591', '1:25487', '1:25533', '1:25576', '1:25579', '1:40743', '1:13267', '1:13640', '1:22727', '1:18686', '1:18834', '1:18975', '1:34496', '1:34913', '1:35474', '1:24331', '1:24241', '1:24320', '1:55885', '1:31655', '1:27856', '1:29748', '1:33809', '1:55680', '1:78799', '1:52834', '1:56081', '1:56147', '1:54523', '1:53250', '1:53358', '1:53366', '1:53682', '1:760', '1:777', '1:814', '1:818', '1:911', '1:20537', '1:25932', '1:25654', '1:25665', '1:25682', '1:25899', '1:26002', '1:26053', '1:26087', '1:32958', '1:33540', '1:80309', '1:89648', '1:75721', '1:95787', '1:73267', '1:33191', '1:33241', '1:33249', '1:7423', '1:7470', '1:7478', '1:7536', '1:7583', '1:7717', '1:7883', '1:7989', '1:58705', '1:51977', '1:13811', '1:14499', '1:36214', '1:36336', '1:36449', '1:36239', '1:36256', '1:36660', '1:73864', '1:38616', '1:38630', '1:38647', '1:37411', '1:37831', '1:48562', '1:73727', '1:74050', '1:74072', '1:74140', '1:43519', '1:11143', '1:41288', '1:41294', '1:47188', '1:47204', '1:11267', '1:11871', '1:31842', '1:31270', '1:40934', '1:41708', '1:42465', '1:42504', '1:42567', '1:42659', '1:42832', '1:68480', '1:68603', '1:74597', '1:74931', '1:76177', '1:76275', '1:69108', '1:78168', '1:3085', '1:4029', '1:4458', '1:130', '1:5700', '1:21346', '1:21291', '1:22159', '1:64159', '1:64258', '1:67224', '1:67504', '1:67740', '1:68964', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54320079-E317-EA11-B1DF-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA975838-3C18-EA11-8F0A-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8A7D5B5-EE17-EA11-8D58-FA163EE3F24C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/76D2EDA7-0918-EA11-9BB4-FA163E20F521.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/768B8E9C-D417-EA11-B213-FA163ECFF9D5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E645838E-2C18-EA11-816C-FA163EE93463.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/060AC0C7-F517-EA11-AD2C-FA163E8B993E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DE51B3B4-8618-EA11-914B-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/9830A3F9-341A-EA11-A175-EC0D9A82264E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/5A3E632C-401A-EA11-80A3-6CC2173C4580.root']);