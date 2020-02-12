import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:41353', '1:41668', '1:41736', '1:41762', '1:41840', '1:41915', '1:45818', '1:45819', '1:48322', '1:84041', '1:82978', '1:82375', '1:82345', '1:83872', '1:83857', '1:84025', '1:84070', '1:84053', '1:84063', '1:84164', '1:84738', '1:92700', '1:93153', '1:93457', '1:44036', '1:47972', '1:44424', '1:44433', '1:41198', '1:47054', '1:47055', '1:47563', '1:82551', '1:83071', '1:48382', '1:65926', '1:66260', '1:66269', '1:66532', '1:82582', '1:66717', '1:66298', '1:66404', '1:66403', '1:66868', '1:66460', '1:66502', '1:66550', '1:82923', '1:83340', '1:82735', '1:82517', '1:82483', '1:82522', '1:83090', '1:12410', '1:12719', '1:12872', '1:45665', '1:45701', '1:48601', '1:83215', '1:83214', '1:83996', '1:42003', '1:12806', '1:42093', '1:42118', '1:47017', '1:12828', '1:12863', '1:42068', '1:42339', '1:42809', '1:42950', '1:44885', '1:44893', '1:92213', '1:92217', '1:93316', '1:83301', '1:93172', '1:11039', '1:11629', '1:11825', '1:11846', '1:11979', '1:84431', '1:84473', '1:92292', '1:92318', '1:84769', '1:92224', '1:92397', '1:92568', '1:92471', '1:92496', '1:11900', '1:11948', '1:11951', '1:12062', '1:12115', '1:12122', '1:12177', '1:11884', '1:48800', '1:48718', '1:65642', '1:66244', '1:82480', '1:84927', '1:92117', '1:93435', '1:93336', '1:93337', '1:47174', '1:47175', '1:47213', '1:48195', '1:65999', '1:83048', '1:84055', '1:48752', '1:43861', '1:45022', '1:45920', '1:48265', '1:82470', '1:83034', '1:84049', '1:41251', '1:44339', '1:44380', '1:44751', '1:44767', '1:43484', '1:65680', '1:43428', '1:45556', '1:48231', '1:45752', '1:65035', '1:65041', '1:45020', '1:45138', '1:48967', '1:43819', '1:43841', '1:44932', '1:44935', '1:45313', '1:92249', '1:48066', '1:48608', '1:12236', '1:12359', '1:12697', '1:12696', '1:47677', '1:43203', '1:43185', '1:82047', '1:83190', '1:83260', '1:66618', '1:42112', '1:42114', '1:48588', '1:48606', '1:93500', '1:93508', '1:93516', '1:47399', '1:47454', '1:44099', '1:44101', '1:44388', '1:84113', '1:93019', '1:84141', '1:84143', '1:84176', '1:92301', '1:84740', '1:84755', '1:93032', '1:93580', '1:11304', '1:12215', '1:42765', '1:42812', '1:45335', '1:48142', '1:45164', '1:48294', '1:12521', '1:47318', '1:47844', '1:47869', '1:44207', '1:45007', '1:45449', '1:48546', '1:44319', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/8026A6CC-9F0F-EA11-9BCD-3CFDFE63A880.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/CA0868E4-580F-EA11-A73F-14187751C030.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/F6C25D2B-6C10-EA11-A3AB-AC1F6B567680.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/82300CEE-C311-EA11-A7D4-0CC47AFCC4BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DE988EEC-0111-EA11-B2B7-00269E95B0A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/24390700-9E11-EA11-ACCD-6C2B5990D0B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/88C8B414-8510-EA11-8999-A4BF0108B89A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/84DA2C2E-B80B-EA11-9ED3-EC0D9A8225FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/7C848483-8210-EA11-9901-0CC47A7E69D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/AA6F0C5B-8710-EA11-8112-00266CFFBF64.root']);