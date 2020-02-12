import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1659', '1:1894', '1:1049', '1:1131', '1:1545', '1:1645', '1:1901', '1:3181', '1:3433', '1:3449', '1:3692', '1:3626', '1:4129', '1:26836', '1:31203', '1:31507', '1:3359', '1:3651', '1:3901', '1:3940', '1:3542', '1:3555', '1:3636', '1:4263', '1:4409', '1:5121', '1:5187', '1:4730', '1:4858', '1:4964', '1:5074', '1:4215', '1:19936', '1:27301', '1:27520', '1:28771', '1:27889', '1:30326', '1:40256', '1:43993', '1:56213', '1:60711', '1:40333', '1:41507', '1:41889', '1:48387', '1:39991', '1:62224', '1:62264', '1:62645', '1:42612', '1:42444', '1:42567', '1:42596', '1:75170', '1:1018', '1:1268', '1:1288', '1:1355', '1:2620', '1:2701', '1:2724', '1:4383', '1:4903', '1:6150', '1:10173', '1:13514', '1:13618', '1:21493', '1:23608', '1:51330', '1:42531', '1:40212', '1:87928', '1:87933', '1:12299', '1:6818', '1:2294', '1:3803', '1:5058', '1:102223', '1:102237', '1:101589', '1:101119', '1:1130', '1:1357', '1:1393', '1:1904', '1:1973', '1:1359', '1:1540', '1:31246', '1:31236', '1:56124', '1:28691', '1:28846', '1:29574', '1:29825', '1:21056', '1:70597', '1:89081', '1:90032', '1:89345', '1:102076', '1:101168', '1:101569', '1:74185', '1:66567', '1:87890', '1:90553', '1:91288', '1:91515', '1:95992', '1:98659', '1:105369', '1:90797', '1:103204', '1:103713', '1:105060', '1:105507', '1:106438', '1:3799', '1:31232', '1:7170', '1:16437', '1:11672', '1:9857', '1:12210', '1:17034', '1:17465', '1:17726', '1:47273', '1:47645', '1:75069', '1:75280', '1:45277', '1:45350', '1:45383', '1:45407', '1:45587', '1:58449', '1:58481', '1:58967', '1:59101', '1:59280', '1:101560', '1:101662', '1:102045', '1:66793', '1:67279', '1:71084', '1:89319', '1:89441', '1:89992', '1:90296', '1:90398', '1:90599', '1:91116', '1:103594', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0C06959B-34F2-E911-A007-40F2E9C6B000.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AADDDD37-EBF9-E911-B35C-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/282CD5F6-EEFA-E911-9E5C-98039B3B004E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E037B27-56F3-E911-8A41-38EAA78D8AF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A04310E4-3E07-EA11-8B88-0CC47AFF02E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/483332F2-DA07-EA11-AEAC-44A842CF0598.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AEC23971-74F7-E911-9030-44A842CFC98B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2F49560-5CF8-E911-A273-0CC47AD9914C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CFEC9C5-B0FB-E911-8390-28924A33AFC2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/228E8BD5-26F5-E911-B71D-509A4C9F8ADB.root']);