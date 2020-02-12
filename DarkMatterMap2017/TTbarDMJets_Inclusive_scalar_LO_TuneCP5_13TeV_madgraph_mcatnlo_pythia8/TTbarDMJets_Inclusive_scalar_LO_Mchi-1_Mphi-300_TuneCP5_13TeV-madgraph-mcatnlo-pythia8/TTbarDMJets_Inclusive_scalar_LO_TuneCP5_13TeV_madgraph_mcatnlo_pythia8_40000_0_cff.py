import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:41758', '1:41844', '1:41754', '1:41752', '1:65547', '1:45837', '1:48658', '1:45437', '1:45485', '1:45775', '1:45793', '1:45831', '1:45886', '1:45888', '1:48783', '1:82982', '1:82614', '1:82616', '1:83518', '1:66520', '1:83344', '1:83440', '1:92191', '1:93110', '1:93156', '1:93443', '1:44054', '1:44143', '1:47968', '1:47977', '1:47915', '1:44171', '1:44468', '1:43340', '1:83069', '1:48933', '1:65851', '1:83343', '1:66101', '1:66186', '1:66225', '1:66314', '1:66704', '1:66307', '1:66842', '1:82986', '1:66716', '1:66734', '1:82617', '1:66426', '1:82767', '1:83079', '1:83081', '1:12194', '1:12425', '1:48397', '1:48405', '1:48567', '1:48596', '1:65294', '1:42001', '1:47010', '1:42466', '1:41159', '1:45166', '1:43099', '1:43385', '1:43489', '1:48146', '1:93434', '1:84645', '1:93315', '1:93850', '1:84635', '1:82412', '1:83316', '1:93127', '1:93173', '1:93109', '1:12422', '1:11048', '1:11798', '1:11824', '1:11838', '1:84432', '1:84595', '1:92739', '1:92754', '1:92765', '1:92767', '1:92824', '1:92601', '1:92602', '1:11944', '1:11941', '1:65263', '1:65704', '1:65945', '1:65260', '1:66221', '1:66321', '1:66601', '1:82561', '1:82880', '1:82996', '1:84269', '1:82239', '1:84945', '1:92146', '1:84931', '1:41960', '1:66198', '1:66331', '1:43377', '1:43402', '1:48549', '1:48520', '1:65705', '1:65960', '1:82170', '1:84958', '1:92435', '1:44747', '1:43597', '1:45555', '1:65670', '1:65890', '1:65905', '1:65920', '1:93201', '1:45719', '1:48426', '1:43241', '1:43387', '1:43406', '1:43522', '1:43533', '1:43602', '1:43851', '1:43857', '1:84149', '1:93919', '1:93970', '1:93974', '1:93976', '1:48639', '1:48616', '1:65004', '1:12585', '1:42344', '1:43187', '1:43225', '1:43629', '1:65531', '1:45808', '1:43987', '1:65513', '1:82802', '1:82805', '1:83002', '1:83540', '1:83597', '1:83755', '1:42458', '1:42776', '1:42541', '1:42859', '1:93719', '1:48630', '1:65450', '1:65792', '1:65451', '1:93499', '1:93509', '1:93727', '1:44404', '1:44534', '1:44377', '1:48149', '1:93016', '1:84079', '1:92298', '1:92315', '1:92344', '1:92363', '1:92324', '1:92372', '1:93033', '1:12263', '1:42033', '1:41764', '1:43465', '1:43595', '1:43466', '1:48140', '1:45133', '1:48225', '1:48295', '1:12440', '1:12436', '1:12470', '1:41997', '1:47304', '1:44209', '1:44237', '1:47868', '1:47878', '1:47884', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/8026A6CC-9F0F-EA11-9BCD-3CFDFE63A880.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/CA0868E4-580F-EA11-A73F-14187751C030.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/F6C25D2B-6C10-EA11-A3AB-AC1F6B567680.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/82300CEE-C311-EA11-A7D4-0CC47AFCC4BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DE988EEC-0111-EA11-B2B7-00269E95B0A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/24390700-9E11-EA11-ACCD-6C2B5990D0B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/88C8B414-8510-EA11-8999-A4BF0108B89A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/84DA2C2E-B80B-EA11-9ED3-EC0D9A8225FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/7C848483-8210-EA11-9901-0CC47A7E69D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/AA6F0C5B-8710-EA11-8112-00266CFFBF64.root']);