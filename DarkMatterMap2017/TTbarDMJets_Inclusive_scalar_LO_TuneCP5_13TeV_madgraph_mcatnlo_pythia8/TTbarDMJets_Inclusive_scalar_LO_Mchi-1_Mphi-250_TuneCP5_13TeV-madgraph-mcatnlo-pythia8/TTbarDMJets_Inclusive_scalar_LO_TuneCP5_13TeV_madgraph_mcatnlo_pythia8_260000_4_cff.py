import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:19807', '1:52299', '1:52695', '1:29961', '1:29406', '1:36032', '1:36056', '1:54374', '1:54239', '1:79845', '1:96036', '1:85110', '1:70288', '1:70312', '1:51406', '1:51423', '1:52069', '1:100796', '1:42211', '1:31105', '1:31601', '1:31673', '1:61267', '1:57410', '1:57631', '1:18025', '1:19157', '1:18582', '1:55182', '1:53417', '1:67082', '1:74456', '1:74837', '1:78727', '1:62394', '1:56512', '1:15221', '1:17784', '1:2776', '1:2829', '1:2849', '1:2936', '1:3237', '1:3680', '1:6173', '1:6245', '1:6488', '1:6543', '1:6554', '1:6585', '1:4500', '1:8436', '1:8745', '1:13871', '1:14619', '1:12216', '1:19659', '1:19919', '1:20217', '1:22270', '1:21818', '1:30702', '1:31027', '1:31079', '1:31505', '1:31890', '1:31914', '1:33670', '1:56028', '1:3193', '1:6702', '1:9949', '1:10533', '1:16928', '1:3330', '1:4242', '1:4637', '1:4642', '1:19332', '1:19907', '1:21244', '1:21585', '1:19263', '1:19798', '1:34541', '1:35215', '1:52737', '1:52994', '1:53124', '1:3354', '1:3373', '1:3386', '1:3922', '1:4692', '1:23880', '1:24950', '1:30313', '1:30617', '1:33585', '1:64308', '1:46541', '1:964', '1:992', '1:1018', '1:1190', '1:4844', '1:4913', '1:22052', '1:22056', '1:22608', '1:37034', '1:33900', '1:23309', '1:30246', '1:35828', '1:8074', '1:19056', '1:67474', '1:29432', '1:29401', '1:29773', '1:77835', '1:14746', '1:23486', '1:23492', '1:46417', '1:49017', '1:46464', '1:88092', '1:52092', '1:58270', '1:4977', '1:5124', '1:5263', '1:5386', '1:5582', '1:22603', '1:23907', '1:35388', '1:28014', '1:28174', '1:27682', '1:27726', '1:36352', '1:15655', '1:15236', '1:46248', '1:46006', '1:41253', '1:56638', '1:56644', '1:56782', '1:61804', '1:29122', '1:29507', '1:29593', '1:33223', '1:33725', '1:65022', '1:65064', '1:65072', '1:49167', '1:67834', '1:64211', '1:64600', '1:64818', '1:68234', '1:72978', '1:77910', '1:9551', '1:54244', '1:54881', '1:53970', '1:58973', '1:20648', '1:25185', '1:19827', '1:24118', '1:27919', '1:30714', '1:23155', '1:24782', '1:24808', '1:28438', '1:28849', '1:60371', '1:60388', '1:4417', '1:4581', '1:4705', '1:4969', '1:29713', '1:31352', '1:23701', '1:23887', '1:23896', '1:29460', '1:29455', '1:51371', '1:57094', '1:58811', '1:24481', '1:38754', '1:39376', '1:57430', '1:57674', '1:57497', '1:58197', '1:58229', '1:58336', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/084A337E-FD17-EA11-91CB-FA163EC15C58.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D2D09D4C-FB1C-EA11-B826-AC1F6BAC8038.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3CABE68A-DF17-EA11-A397-EC0D9A89AA0A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1C65D4CB-F817-EA11-A4F0-5065F381E151.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B8C02DCD-DD17-EA11-A4CA-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BCE9B05F-8F19-EA11-A91E-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/34703F54-3C18-EA11-8F76-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8AF4123C-2418-EA11-91CC-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D0D3DE95-0618-EA11-BC35-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/12F05E8A-0618-EA11-9978-24BE05CE3EA1.root']);