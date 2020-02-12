import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:3914', '1:3938', '1:3960', '1:4039', '1:6131', '1:38309', '1:3969', '1:3977', '1:4498', '1:4885', '1:4473', '1:5358', '1:12478', '1:12483', '1:15102', '1:14524', '1:14886', '1:14894', '1:14590', '1:32291', '1:38961', '1:9053', '1:10052', '1:9101', '1:16223', '1:16242', '1:21958', '1:26718', '1:29893', '1:16474', '1:10390', '1:26227', '1:26193', '1:26230', '1:26662', '1:33635', '1:30418', '1:32295', '1:34395', '1:79275', '1:79775', '1:89583', '1:90573', '1:99226', '1:36655', '1:36305', '1:58459', '1:59584', '1:58563', '1:58681', '1:58762', '1:84433', '1:90369', '1:100751', '1:100112', '1:94821', '1:37288', '1:37632', '1:37680', '1:56649', '1:57757', '1:58363', '1:58530', '1:58735', '1:52072', '1:38790', '1:40404', '1:53167', '1:63910', '1:81910', '1:87960', '1:75172', '1:77187', '1:56101', '1:56174', '1:56392', '1:58133', '1:89953', '1:79586', '1:21791', '1:14839', '1:36040', '1:29531', '1:29088', '1:29155', '1:29350', '1:32840', '1:77834', '1:87297', '1:63026', '1:63148', '1:18204', '1:18351', '1:18690', '1:18785', '1:17821', '1:18348', '1:17650', '1:18005', '1:18033', '1:24676', '1:24773', '1:22435', '1:23798', '1:35152', '1:37497', '1:37739', '1:37682', '1:37976', '1:40246', '1:40489', '1:40524', '1:40606', '1:18282', '1:10674', '1:19216', '1:25036', '1:25079', '1:25249', '1:7067', '1:10782', '1:19559', '1:20952', '1:20991', '1:18671', '1:18673', '1:18897', '1:18949', '1:18997', '1:19153', '1:33975', '1:34041', '1:34953', '1:52755', '1:30973', '1:27586', '1:31802', '1:32060', '1:27973', '1:72026', '1:53347', '1:53567', '1:53709', '1:56063', '1:14016', '1:14639', '1:19646', '1:641', '1:26423', '1:36952', '1:38635', '1:37603', '1:37528', '1:25693', '1:25810', '1:25824', '1:25786', '1:25876', '1:25898', '1:34042', '1:34165', '1:32973', '1:36192', '1:36244', '1:36249', '1:73691', '1:101544', '1:32115', '1:39727', '1:25038', '1:7327', '1:7764', '1:51568', '1:51986', '1:14622', '1:16123', '1:14593', '1:36233', '1:36324', '1:36272', '1:36651', '1:77831', '1:39222', '1:73759', '1:42991', '1:45045', '1:48751', '1:48758', '1:65256', '1:83032', '1:18485', '1:49230', '1:37980', '1:46996', '1:42314', '1:77990', '1:2589', '1:5427', '1:5569', '1:489', '1:1433', '1:21434', '1:21356', '1:22286', '1:22351', '1:21297', '1:67407', '1:67611', '1:67862', '1:68269', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54320079-E317-EA11-B1DF-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA975838-3C18-EA11-8F0A-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8A7D5B5-EE17-EA11-8D58-FA163EE3F24C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/76D2EDA7-0918-EA11-9BB4-FA163E20F521.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/768B8E9C-D417-EA11-B213-FA163ECFF9D5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E645838E-2C18-EA11-816C-FA163EE93463.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/060AC0C7-F517-EA11-AD2C-FA163E8B993E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DE51B3B4-8618-EA11-914B-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/9830A3F9-341A-EA11-A175-EC0D9A82264E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/5A3E632C-401A-EA11-80A3-6CC2173C4580.root']);