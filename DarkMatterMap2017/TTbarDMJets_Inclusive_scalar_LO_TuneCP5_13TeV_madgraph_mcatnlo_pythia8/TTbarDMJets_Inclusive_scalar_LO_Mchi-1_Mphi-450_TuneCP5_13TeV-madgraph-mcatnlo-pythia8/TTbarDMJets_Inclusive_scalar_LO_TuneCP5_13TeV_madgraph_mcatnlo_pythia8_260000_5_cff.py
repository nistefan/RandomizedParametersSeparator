import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:13398', '1:79091', '1:79545', '1:86056', '1:25660', '1:40939', '1:52473', '1:61101', '1:63476', '1:53669', '1:54109', '1:58578', '1:62360', '1:50305', '1:59327', '1:59947', '1:60508', '1:63383', '1:50209', '1:52002', '1:53411', '1:53547', '1:16987', '1:16800', '1:16855', '1:16890', '1:17137', '1:17197', '1:18071', '1:28016', '1:28367', '1:28386', '1:28411', '1:28527', '1:59533', '1:59541', '1:98052', '1:59324', '1:59379', '1:59804', '1:59880', '1:73950', '1:77784', '1:2158', '1:2247', '1:10146', '1:21302', '1:8290', '1:8867', '1:9533', '1:8284', '1:8391', '1:8769', '1:31622', '1:32206', '1:31680', '1:32140', '1:34868', '1:13125', '1:13383', '1:13432', '1:13879', '1:13194', '1:22278', '1:13331', '1:13834', '1:19377', '1:19777', '1:19257', '1:73253', '1:67208', '1:69731', '1:25122', '1:25175', '1:25200', '1:29338', '1:23644', '1:39910', '1:26608', '1:26717', '1:29052', '1:29159', '1:28104', '1:28467', '1:29211', '1:29236', '1:29292', '1:29320', '1:52251', '1:58660', '1:28051', '1:28156', '1:33098', '1:33123', '1:33263', '1:33536', '1:33564', '1:34045', '1:34219', '1:37304', '1:38471', '1:38584', '1:38607', '1:38687', '1:3418', '1:3639', '1:6229', '1:15900', '1:16267', '1:16456', '1:16478', '1:17564', '1:5694', '1:5556', '1:5383', '1:6561', '1:10099', '1:13916', '1:15007', '1:22192', '1:22924', '1:10521', '1:46374', '1:46481', '1:35821', '1:46657', '1:40150', '1:10580', '1:21600', '1:10595', '1:13428', '1:17171', '1:10343', '1:7062', '1:15644', '1:15662', '1:15775', '1:9324', '1:6642', '1:6745', '1:6812', '1:6973', '1:7180', '1:46341', '1:34357', '1:34373', '1:34778', '1:55229', '1:51172', '1:51174', '1:51734', '1:9574', '1:16207', '1:49399', '1:31197', '1:30083', '1:30125', '1:30168', '1:13756', '1:14325', '1:14808', '1:25617', '1:25650', '1:37287', '1:16809', '1:16999', '1:17016', '1:17599', '1:19470', '1:19528', '1:19610', '1:50486', '1:53166', '1:56755', '1:24809', '1:53160', '1:53222', '1:56163', '1:56180', '1:74232', '1:81761', '1:85754', '1:68394', '1:58025', '1:58119', '1:58142', '1:58223', '1:29904', '1:61667', '1:61811', '1:61849', '1:61854', '1:61888', '1:4208', '1:4367', '1:4536', '1:4640', '1:4973', '1:2248', '1:2316', '1:21540', '1:20717', '1:20831', '1:20966', '1:21098', '1:21131', '1:21462', '1:21178', '1:21435', '1:21469', '1:32370', '1:32354', '1:33043', '1:34150', '1:32552', '1:32565', '1:33154', '1:36452', '1:36550', '1:36680', '1:36524', '1:36605', '1:36625', '1:50533', '1:57271', '1:64415', '1:64504', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8A52D68A-9716-EA11-8A46-C81F66C09A78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3AA8A739-3B1A-EA11-8F16-0025901D08F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6C8ECEC3-DC18-EA11-A954-246E96D149A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DAB73933-B217-EA11-85E7-24BE05C3CBE1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E2A83DB0-0518-EA11-9905-FA163ECADB68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/46514FD2-CA17-EA11-A746-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/5CECA162-FA17-EA11-9B4F-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/18E400F5-FF17-EA11-A992-FA163E9F39BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DEE6096F-1D18-EA11-99A4-FA163E977168.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/404013D1-151C-EA11-A760-588A5AAEEBB8.root']);