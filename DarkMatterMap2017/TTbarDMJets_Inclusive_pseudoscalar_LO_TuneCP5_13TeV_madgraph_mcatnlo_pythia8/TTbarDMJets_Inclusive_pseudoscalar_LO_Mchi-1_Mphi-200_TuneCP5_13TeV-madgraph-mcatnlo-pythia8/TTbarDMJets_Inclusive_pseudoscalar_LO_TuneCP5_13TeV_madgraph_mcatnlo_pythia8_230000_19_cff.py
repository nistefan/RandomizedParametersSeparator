import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1394', '1:1410', '1:1670', '1:2484', '1:2606', '1:2726', '1:1959', '1:2190', '1:2761', '1:3363', '1:11932', '1:12069', '1:12410', '1:12482', '1:12864', '1:13470', '1:6102', '1:6585', '1:7185', '1:6927', '1:9927', '1:9339', '1:9409', '1:24294', '1:25467', '1:25630', '1:26228', '1:26501', '1:26606', '1:26638', '1:25756', '1:26076', '1:13654', '1:13881', '1:15756', '1:21371', '1:26689', '1:40141', '1:41179', '1:43465', '1:74035', '1:75317', '1:75577', '1:86794', '1:91418', '1:23507', '1:26461', '1:20505', '1:21907', '1:26244', '1:31704', '1:31924', '1:17006', '1:51588', '1:26652', '1:73603', '1:24438', '1:24445', '1:24560', '1:46068', '1:46103', '1:46109', '1:28663', '1:29010', '1:29113', '1:29129', '1:29356', '1:29455', '1:72496', '1:72791', '1:72818', '1:72891', '1:87955', '1:90008', '1:89089', '1:101892', '1:93399', '1:93657', '1:93920', '1:94558', '1:1498', '1:6864', '1:12823', '1:12839', '1:12888', '1:12903', '1:13214', '1:13228', '1:13285', '1:13506', '1:13940', '1:30640', '1:30653', '1:31589', '1:31645', '1:31665', '1:31792', '1:31835', '1:31836', '1:31898', '1:31944', '1:93203', '1:93798', '1:93699', '1:93853', '1:2018', '1:3103', '1:12340', '1:13874', '1:4399', '1:10704', '1:2971', '1:7380', '1:12477', '1:13088', '1:13327', '1:15946', '1:16188', '1:40053', '1:43726', '1:43777', '1:88230', '1:88666', '1:75717', '1:76358', '1:87737', '1:91294', '1:84577', '1:85500', '1:85717', '1:92427', '1:94412', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4AE2EE50-65FC-E911-B233-0CC47AFCC62A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/262322CD-2EF8-E911-8414-0CC47A2B04B6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E83181B8-B4FC-E911-8386-6CC2173D6B10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4881F73B-93FC-E911-ABAF-3417EBE70663.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/389B13D9-FA08-EA11-BC98-0025905A6064.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A96DA38-CBFA-E911-B1D9-28924A33B8AE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70F9F439-56F3-E911-9AA8-F4E9D4DF1780.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E64248C-BC12-EA11-9804-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8C2EB6F-BD12-EA11-A3F9-A0369F7FC544.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C484CA9C-D4F3-E911-A566-8CDCD4A99D14.root']);