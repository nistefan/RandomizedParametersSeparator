import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:95077', '1:101436', '1:101938', '1:98271', '1:102399', '1:101169', '1:101532', '1:104814', '1:102548', '1:104434', '1:104960', '1:6744', '1:10107', '1:5420', '1:43531', '1:43536', '1:48307', '1:13929', '1:13984', '1:14228', '1:13661', '1:14549', '1:14650', '1:52229', '1:15463', '1:16234', '1:17271', '1:17623', '1:19550', '1:28469', '1:25062', '1:25189', '1:42291', '1:42380', '1:42609', '1:42803', '1:44102', '1:44311', '1:44621', '1:56968', '1:51628', '1:56574', '1:64177', '1:74674', '1:83795', '1:85818', '1:85874', '1:88144', '1:88484', '1:86955', '1:90653', '1:83659', '1:85433', '1:97085', '1:84053', '1:90206', '1:101736', '1:106156', '1:102072', '1:104603', '1:104813', '1:102985', '1:3744', '1:4233', '1:5459', '1:53370', '1:53550', '1:53803', '1:54297', '1:54345', '1:59333', '1:59590', '1:59962', '1:8050', '1:8062', '1:8742', '1:8766', '1:8912', '1:9145', '1:32491', '1:42084', '1:40743', '1:41244', '1:41529', '1:41878', '1:46594', '1:49042', '1:8834', '1:8890', '1:9311', '1:9380', '1:27121', '1:27278', '1:27294', '1:5134', '1:5385', '1:11658', '1:21455', '1:31987', '1:29984', '1:41379', '1:43168', '1:43798', '1:70701', '1:80448', '1:80795', '1:45006', '1:29917', '1:55959', '1:22910', '1:42354', '1:52303', '1:44685', '1:44807', '1:44814', '1:45038', '1:45098', '1:45137', '1:44724', '1:72073', '1:57905', '1:62121', '1:77011', '1:77198', '1:24697', '1:84355', '1:84856', '1:85848', '1:77473', '1:86105', '1:87884', '1:97761', '1:74200', '1:80037', '1:76212', '1:79681', '1:77309', '1:87430', '1:5978', '1:5992', '1:6389', '1:7016', '1:6190', '1:6433', '1:6653', '1:6734', '1:7095', '1:40552', '1:40697', '1:40714', '1:52249', '1:22670', '1:22743', '1:22751', '1:22803', '1:22557', '1:27310', '1:27422', '1:27586', '1:27641', '1:83638', '1:49280', '1:44322', '1:47548', '1:47770', '1:47903', '1:12519', '1:15501', '1:21584', '1:31304', '1:21537', '1:24458', '1:93549', '1:95751', '1:87446', '1:87721', '1:106094', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6A721CBE-4B07-EA11-9750-0CC47A4D7646.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCF6B8AB-E003-EA11-AAE8-44A842BE8F7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9EAE1061-30F8-E911-B2D5-AC1F6B0F676C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/86727FE6-AF0A-EA11-B38D-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2A16734-8607-EA11-A7C2-0025905A6060.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/723E26E0-88FC-E911-A84F-0CC47AFCC666.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/643155F4-E80A-EA11-BD55-0CC47A7C3636.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC1243A5-AA0A-EA11-A2C9-0CC47A7C347A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24362999-4EFE-E911-BFEB-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1207CE62-4EF9-E911-85E0-C4346BC85718.root']);