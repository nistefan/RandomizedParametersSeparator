import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1884', '1:2917', '1:3416', '1:3579', '1:3757', '1:31276', '1:31287', '1:31673', '1:31702', '1:2799', '1:3197', '1:16654', '1:5080', '1:4437', '1:4446', '1:4136', '1:7398', '1:21302', '1:21543', '1:17219', '1:7169', '1:59056', '1:60593', '1:61227', '1:62478', '1:51185', '1:40946', '1:41437', '1:49754', '1:21095', '1:39596', '1:62644', '1:42707', '1:42330', '1:42588', '1:42637', '1:42673', '1:42914', '1:87907', '1:1187', '1:1189', '1:2531', '1:2908', '1:1919', '1:4167', '1:4676', '1:4097', '1:10659', '1:11190', '1:12460', '1:13026', '1:13277', '1:13492', '1:13539', '1:13776', '1:13809', '1:23470', '1:42378', '1:40147', '1:40200', '1:88954', '1:89051', '1:89180', '1:89840', '1:5059', '1:10559', '1:5706', '1:7309', '1:1780', '1:1871', '1:1402', '1:1605', '1:1608', '1:1644', '1:26711', '1:31158', '1:49963', '1:29444', '1:28392', '1:28490', '1:28498', '1:5651', '1:7257', '1:26617', '1:23508', '1:70719', '1:89824', '1:82085', '1:88495', '1:102212', '1:101192', '1:66217', '1:66552', '1:74006', '1:67247', '1:95034', '1:97346', '1:97762', '1:97909', '1:98764', '1:103053', '1:15454', '1:8897', '1:26953', '1:45572', '1:14308', '1:4979', '1:7934', '1:3104', '1:7075', '1:13205', '1:20125', '1:17831', '1:45919', '1:47255', '1:47361', '1:73600', '1:75808', '1:76425', '1:45625', '1:45610', '1:45852', '1:45885', '1:58196', '1:58490', '1:58740', '1:61209', '1:101639', '1:71060', '1:89436', '1:89877', '1:90188', '1:90754', '1:92539', '1:103769', '1:103731', '1:103953', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0C06959B-34F2-E911-A007-40F2E9C6B000.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AADDDD37-EBF9-E911-B35C-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/282CD5F6-EEFA-E911-9E5C-98039B3B004E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E037B27-56F3-E911-8A41-38EAA78D8AF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A04310E4-3E07-EA11-8B88-0CC47AFF02E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/483332F2-DA07-EA11-AEAC-44A842CF0598.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AEC23971-74F7-E911-9030-44A842CFC98B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2F49560-5CF8-E911-A273-0CC47AD9914C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CFEC9C5-B0FB-E911-8390-28924A33AFC2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/228E8BD5-26F5-E911-B71D-509A4C9F8ADB.root']);