import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:3788', '1:4072', '1:4209', '1:4883', '1:12460', '1:9047', '1:10207', '1:9107', '1:16724', '1:16730', '1:17770', '1:27749', '1:64205', '1:64348', '1:68456', '1:68561', '1:23231', '1:23249', '1:13147', '1:13193', '1:13315', '1:13355', '1:10276', '1:26235', '1:26260', '1:26144', '1:26310', '1:26283', '1:26496', '1:33031', '1:33581', '1:30410', '1:32045', '1:32189', '1:34039', '1:34362', '1:34581', '1:34817', '1:36645', '1:58086', '1:58092', '1:58863', '1:59704', '1:57888', '1:87188', '1:98075', '1:99591', '1:58596', '1:58743', '1:58776', '1:58859', '1:59325', '1:89884', '1:90512', '1:99617', '1:65394', '1:65416', '1:46019', '1:46072', '1:90973', '1:95131', '1:49692', '1:49965', '1:60900', '1:61010', '1:58424', '1:38798', '1:40379', '1:89023', '1:53191', '1:54090', '1:77537', '1:59215', '1:56144', '1:56285', '1:56330', '1:56376', '1:56328', '1:94064', '1:58088', '1:81689', '1:88820', '1:81321', '1:18015', '1:10029', '1:13695', '1:15745', '1:7700', '1:29321', '1:29058', '1:53258', '1:17742', '1:18070', '1:18592', '1:54283', '1:21190', '1:17722', '1:17861', '1:18184', '1:52238', '1:57433', '1:24764', '1:24770', '1:22315', '1:23038', '1:23427', '1:24012', '1:24146', '1:24193', '1:25314', '1:25354', '1:25451', '1:25358', '1:38549', '1:37728', '1:37789', '1:37812', '1:37838', '1:40255', '1:40259', '1:7260', '1:16369', '1:25251', '1:25256', '1:7755', '1:20633', '1:19260', '1:22065', '1:18551', '1:33979', '1:34229', '1:34949', '1:51751', '1:24511', '1:24459', '1:30864', '1:40325', '1:24972', '1:27268', '1:39305', '1:62535', '1:67110', '1:30081', '1:31356', '1:31494', '1:31607', '1:27945', '1:99100', '1:55603', '1:74350', '1:52943', '1:56115', '1:56152', '1:56278', '1:53565', '1:53759', '1:561', '1:695', '1:918', '1:19946', '1:908', '1:17416', '1:26082', '1:26272', '1:37417', '1:37419', '1:37431', '1:37604', '1:37606', '1:25677', '1:25846', '1:25801', '1:25845', '1:26084', '1:34043', '1:34269', '1:32908', '1:32939', '1:32979', '1:33460', '1:36012', '1:36129', '1:54734', '1:81855', '1:88432', '1:39243', '1:33170', '1:25075', '1:25106', '1:4996', '1:5103', '1:5401', '1:5589', '1:10734', '1:15329', '1:20184', '1:7384', '1:7635', '1:7789', '1:64067', '1:51185', '1:51580', '1:13768', '1:16115', '1:16318', '1:16324', '1:16334', '1:36234', '1:36299', '1:74118', '1:39058', '1:37782', '1:39219', '1:39286', '1:73716', '1:42763', '1:48505', '1:11268', '1:11336', '1:33423', '1:38439', '1:37992', '1:50308', '1:49035', '1:52646', '1:41453', '1:42622', '1:74726', '1:74946', '1:75049', '1:70047', '1:73649', '1:907', '1:2155', '1:3006', '1:4174', '1:4041', '1:1065', '1:22021', '1:21495', '1:21588', '1:21088', '1:21227', '1:21729', '1:67595', '1:67650', '1:69160', '1:69259', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54320079-E317-EA11-B1DF-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA975838-3C18-EA11-8F0A-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8A7D5B5-EE17-EA11-8D58-FA163EE3F24C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/76D2EDA7-0918-EA11-9BB4-FA163E20F521.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/768B8E9C-D417-EA11-B213-FA163ECFF9D5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E645838E-2C18-EA11-816C-FA163EE93463.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/060AC0C7-F517-EA11-AD2C-FA163E8B993E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DE51B3B4-8618-EA11-914B-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/9830A3F9-341A-EA11-A175-EC0D9A82264E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/5A3E632C-401A-EA11-80A3-6CC2173C4580.root']);