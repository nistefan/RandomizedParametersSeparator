import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:93768', '1:92954', '1:92962', '1:92988', '1:93208', '1:93494', '1:93344', '1:93348', '1:93056', '1:93060', '1:93101', '1:93587', '1:93594', '1:93559', '1:93612', '1:93648', '1:93659', '1:93661', '1:12396', '1:11271', '1:11489', '1:11564', '1:11585', '1:11432', '1:11434', '1:11339', '1:12355', '1:42253', '1:12321', '1:42594', '1:47637', '1:47631', '1:42736', '1:41190', '1:48304', '1:65970', '1:43657', '1:82652', '1:83040', '1:83906', '1:12322', '1:41214', '1:42735', '1:41338', '1:42708', '1:48779', '1:82099', '1:82132', '1:82130', '1:83582', '1:41350', '1:42422', '1:45938', '1:82225', '1:11625', '1:11695', '1:12363', '1:12373', '1:41767', '1:84266', '1:93995', '1:41650', '1:41278', '1:11184', '1:12144', '1:11493', '1:47521', '1:11830', '1:45180', '1:45249', '1:66719', '1:45829', '1:48478', '1:82464', '1:43967', '1:66219', '1:82597', '1:45498', '1:65261', '1:66021', '1:65823', '1:66027', '1:11119', '1:12339', '1:47266', '1:44127', '1:44512', '1:44519', '1:44181', '1:47897', '1:47902', '1:44586', '1:43250', '1:43254', '1:43662', '1:41820', '1:48353', '1:48232', '1:48438', '1:66064', '1:66680', '1:43284', '1:43414', '1:43421', '1:66187', '1:66313', '1:66464', '1:65951', '1:65902', '1:11092', '1:42037', '1:42910', '1:41026', '1:41418', '1:41712', '1:41017', '1:47232', '1:42988', '1:47962', '1:43505', '1:12722', '1:12769', '1:12770', '1:42851', '1:41057', '1:45354', '1:45604', '1:84239', '1:84246', '1:45310', '1:82454', '1:83687', '1:82928', '1:82936', '1:93687', '1:93811', '1:84912', '1:66807', '1:83644', '1:83645', '1:83147', '1:83167', '1:83526', '1:83592', '1:83606', '1:83661', '1:83703', '1:83730', '1:82671', '1:83407', '1:66517', '1:82751', '1:82760', '1:83448', '1:84489', '1:92126', '1:84893', '1:92119', '1:84316', '1:12768', '1:12791', '1:12827', '1:12955', '1:12995', '1:12949', '1:47433', '1:47437', '1:47747', '1:47755', '1:47761', '1:45075', '1:92924', '1:92967', '1:93220', '1:93249', '1:93272', '1:48902', '1:65160', '1:65162', '1:65172', '1:65609', '1:65650', '1:65880', '1:93188', '1:92388', '1:92399', '1:92403', '1:92510', '1:92623', '1:92830', '1:92840', '1:92548', '1:92890', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/CCB0C45C-6510-EA11-8402-0025905C53D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/6E48CFB0-B414-EA11-B703-003048F316A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/8493BC83-B911-EA11-968F-485B397717C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D0111189-740F-EA11-A3A6-D094662CEC35.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/2E27578F-4F10-EA11-AEBA-0025905C42A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/7A36FBD8-C811-EA11-9087-7CD30ACE142C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/56A7F3B9-3A10-EA11-A2BE-0025905C42A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C6C92169-6714-EA11-B417-90B11C443C96.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/28CECBEA-7E10-EA11-9B7F-0CC47AFF02D0.root']);