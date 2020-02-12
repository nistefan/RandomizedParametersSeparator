import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:104467', '1:7533', '1:7633', '1:7783', '1:21884', '1:23005', '1:23010', '1:25951', '1:32729', '1:40793', '1:46192', '1:46711', '1:48009', '1:52214', '1:52603', '1:53084', '1:52607', '1:53644', '1:53970', '1:54106', '1:54137', '1:54739', '1:59219', '1:84576', '1:85460', '1:7226', '1:6860', '1:7117', '1:8077', '1:8633', '1:9572', '1:9662', '1:46767', '1:46809', '1:46864', '1:53376', '1:54042', '1:54343', '1:12522', '1:53659', '1:55214', '1:55678', '1:55777', '1:55792', '1:56067', '1:27480', '1:27669', '1:54698', '1:55068', '1:41441', '1:40795', '1:41523', '1:43818', '1:77334', '1:83567', '1:84921', '1:88322', '1:89659', '1:94642', '1:1165', '1:2328', '1:4777', '1:4347', '1:11226', '1:2518', '1:5109', '1:9415', '1:22612', '1:29968', '1:1835', '1:11967', '1:10790', '1:16503', '1:28884', '1:23912', '1:1537', '1:1190', '1:1546', '1:1586', '1:7666', '1:7774', '1:7963', '1:8622', '1:6313', '1:6068', '1:6086', '1:6202', '1:6298', '1:3842', '1:5594', '1:3823', '1:12755', '1:12594', '1:12599', '1:1198', '1:1494', '1:1774', '1:10327', '1:43570', '1:43649', '1:57635', '1:64361', '1:51238', '1:53769', '1:91273', '1:93200', '1:47199', '1:11321', '1:3418', '1:7352', '1:7868', '1:8184', '1:9107', '1:55859', '1:60844', '1:60600', '1:96021', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A28F10B-AA07-EA11-B3F4-AC1F6B1B2364.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E0E93DFE-8FFB-E911-AE26-0CC47AFF01B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44DA73CB-BEFC-E911-AE13-001E67E5EDBB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D21296E4-5DFC-E911-9755-0025905C53D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/04526127-A3FB-E911-9F1B-0CC47AFEFDE4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1066B909-FF08-EA11-809A-AC1F6B1AEF94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2AA5595F-5BEF-E911-A3D3-D4AE528FF49B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8EFD98F-8FF2-E911-BA8E-0CC47A7E6A88.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/ECB29738-6AEF-E911-ADB3-E0071B740D90.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C9B1AC6-35F0-E911-A35E-F01FAFD9C1A8.root']);