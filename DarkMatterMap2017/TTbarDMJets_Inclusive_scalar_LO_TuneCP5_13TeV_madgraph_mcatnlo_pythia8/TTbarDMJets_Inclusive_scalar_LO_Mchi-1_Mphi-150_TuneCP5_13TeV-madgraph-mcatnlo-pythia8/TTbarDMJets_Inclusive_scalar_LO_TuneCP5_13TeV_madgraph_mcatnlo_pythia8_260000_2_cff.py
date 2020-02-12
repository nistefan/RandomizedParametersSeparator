import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:3789', '1:3810', '1:3827', '1:3846', '1:3953', '1:13201', '1:20907', '1:38358', '1:4376', '1:4460', '1:5442', '1:14525', '1:14621', '1:14667', '1:14957', '1:15852', '1:9192', '1:15856', '1:64475', '1:76258', '1:16127', '1:10017', '1:10198', '1:10844', '1:26318', '1:26482', '1:26497', '1:26383', '1:26895', '1:35340', '1:31818', '1:39500', '1:40545', '1:32676', '1:32829', '1:34606', '1:34849', '1:36197', '1:36297', '1:36316', '1:57989', '1:58003', '1:58376', '1:59641', '1:57754', '1:57823', '1:57824', '1:57886', '1:61660', '1:59797', '1:89770', '1:90402', '1:45015', '1:65399', '1:65406', '1:46073', '1:88421', '1:38233', '1:37224', '1:37302', '1:49878', '1:59420', '1:58279', '1:58466', '1:58517', '1:37686', '1:63463', '1:63998', '1:80246', '1:56156', '1:56391', '1:56464', '1:56561', '1:56695', '1:80218', '1:80089', '1:10027', '1:13731', '1:17551', '1:28586', '1:26972', '1:29172', '1:29065', '1:32841', '1:59497', '1:81931', '1:18030', '1:18151', '1:17810', '1:18087', '1:18827', '1:18844', '1:18460', '1:18527', '1:18607', '1:50861', '1:56945', '1:57387', '1:24729', '1:22079', '1:22290', '1:26140', '1:23334', '1:24162', '1:29994', '1:33987', '1:25272', '1:25440', '1:38554', '1:25588', '1:37733', '1:37644', '1:37846', '1:37968', '1:37979', '1:40313', '1:15678', '1:19937', '1:25604', '1:18654', '1:18712', '1:18811', '1:19169', '1:33897', '1:35403', '1:51758', '1:52271', '1:30747', '1:46384', '1:35991', '1:27510', '1:30884', '1:55729', '1:62141', '1:64151', '1:56151', '1:53312', '1:53318', '1:53745', '1:541', '1:595', '1:18433', '1:926', '1:25890', '1:25931', '1:26285', '1:26372', '1:36956', '1:33832', '1:38613', '1:25685', '1:25869', '1:25803', '1:32921', '1:32962', '1:32965', '1:33469', '1:73562', '1:75160', '1:76711', '1:75552', '1:34658', '1:33173', '1:6965', '1:15487', '1:21347', '1:21429', '1:25023', '1:4948', '1:7334', '1:58020', '1:64280', '1:67685', '1:13615', '1:13779', '1:13808', '1:13897', '1:16156', '1:16268', '1:16300', '1:14464', '1:36216', '1:36472', '1:36264', '1:39138', '1:37711', '1:39263', '1:73880', '1:73913', '1:74005', '1:74043', '1:74061', '1:74083', '1:44023', '1:44524', '1:45027', '1:44345', '1:43375', '1:65594', '1:82889', '1:11298', '1:11522', '1:18993', '1:42316', '1:42471', '1:64182', '1:75130', '1:75198', '1:76113', '1:805', '1:2678', '1:1317', '1:4463', '1:4870', '1:21526', '1:21246', '1:21478', '1:20980', '1:20989', '1:21670', '1:21267', '1:21549', '1:64271', '1:67520', '1:69049', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54320079-E317-EA11-B1DF-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA975838-3C18-EA11-8F0A-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8A7D5B5-EE17-EA11-8D58-FA163EE3F24C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/76D2EDA7-0918-EA11-9BB4-FA163E20F521.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/768B8E9C-D417-EA11-B213-FA163ECFF9D5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E645838E-2C18-EA11-816C-FA163EE93463.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/060AC0C7-F517-EA11-AD2C-FA163E8B993E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DE51B3B4-8618-EA11-914B-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/9830A3F9-341A-EA11-A175-EC0D9A82264E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/5A3E632C-401A-EA11-80A3-6CC2173C4580.root']);