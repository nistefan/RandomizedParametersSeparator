import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:92528', '1:92534', '1:92539', '1:92575', '1:93805', '1:93759', '1:92970', '1:92994', '1:93243', '1:93254', '1:93286', '1:93351', '1:93386', '1:93291', '1:93309', '1:93374', '1:93546', '1:93080', '1:93081', '1:93089', '1:93582', '1:93584', '1:93591', '1:93654', '1:11180', '1:11181', '1:11262', '1:11589', '1:12139', '1:11429', '1:11431', '1:11439', '1:11445', '1:11456', '1:11460', '1:12362', '1:12234', '1:12569', '1:42055', '1:42326', '1:42591', '1:42678', '1:42700', '1:42698', '1:48655', '1:66886', '1:66156', '1:66672', '1:82378', '1:83904', '1:92138', '1:12295', '1:11354', '1:11730', '1:12920', '1:41003', '1:41216', '1:41374', '1:43939', '1:83433', '1:11100', '1:11148', '1:11200', '1:11790', '1:11795', '1:12175', '1:11696', '1:12267', '1:12368', '1:12889', '1:42629', '1:42924', '1:48714', '1:92683', '1:41663', '1:41654', '1:42962', '1:12241', '1:47980', '1:43004', '1:44848', '1:47918', '1:43243', '1:43298', '1:48659', '1:48668', '1:48915', '1:43620', '1:65119', '1:66566', '1:43897', '1:43908', '1:44993', '1:45405', '1:66527', '1:82595', '1:82599', '1:66079', '1:43866', '1:45307', '1:45541', '1:48844', '1:11402', '1:12015', '1:12208', '1:12209', '1:41833', '1:41837', '1:44177', '1:47779', '1:47899', '1:48676', '1:43139', '1:44607', '1:43661', '1:43664', '1:42908', '1:41082', '1:41824', '1:42519', '1:42753', '1:48826', '1:45989', '1:45999', '1:65810', '1:66071', '1:44522', '1:66411', '1:66881', '1:65954', '1:11074', '1:11816', '1:41776', '1:42633', '1:42912', '1:41422', '1:41542', '1:41670', '1:41027', '1:47170', '1:47951', '1:42328', '1:43110', '1:43506', '1:93633', '1:41273', '1:45693', '1:84242', '1:84231', '1:84350', '1:84847', '1:92097', '1:45280', '1:45564', '1:45959', '1:45961', '1:45962', '1:83177', '1:83860', '1:92500', '1:92606', '1:93478', '1:84923', '1:66688', '1:66919', '1:66931', '1:66882', '1:83065', '1:83148', '1:82421', '1:82456', '1:83598', '1:83695', '1:82433', '1:82437', '1:82438', '1:82575', '1:66508', '1:66549', '1:82857', '1:83830', '1:83881', '1:84507', '1:92074', '1:92122', '1:84300', '1:12685', '1:12728', '1:12730', '1:12743', '1:12957', '1:47439', '1:47582', '1:47699', '1:92969', '1:93234', '1:48891', '1:65169', '1:65607', '1:65651', '1:92620', '1:92670', '1:92551', '1:92785', '1:92803', '1:92894', '1:92917', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/CCB0C45C-6510-EA11-8402-0025905C53D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/6E48CFB0-B414-EA11-B703-003048F316A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/8493BC83-B911-EA11-968F-485B397717C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D0111189-740F-EA11-A3A6-D094662CEC35.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/2E27578F-4F10-EA11-AEBA-0025905C42A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/7A36FBD8-C811-EA11-9087-7CD30ACE142C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/56A7F3B9-3A10-EA11-A2BE-0025905C42A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C6C92169-6714-EA11-B417-90B11C443C96.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/28CECBEA-7E10-EA11-9B7F-0CC47AFF02D0.root']);