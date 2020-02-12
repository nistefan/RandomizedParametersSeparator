import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:3388', '1:29470', '1:5478', '1:5829', '1:28377', '1:35997', '1:670', '1:681', '1:706', '1:723', '1:29794', '1:33734', '1:839', '1:1416', '1:3133', '1:7487', '1:6150', '1:2524', '1:7472', '1:9686', '1:7862', '1:33377', '1:1929', '1:25820', '1:29169', '1:28529', '1:4100', '1:4929', '1:10130', '1:10830', '1:3315', '1:3321', '1:3853', '1:6619', '1:2541', '1:26813', '1:30342', '1:30348', '1:32393', '1:34173', '1:35208', '1:34980', '1:35262', '1:35275', '1:3396', '1:10280', '1:4321', '1:9242', '1:6124', '1:29260', '1:31832', '1:26098', '1:28079', '1:29256', '1:29386', '1:28394', '1:32278', '1:28301', '1:34004', '1:34681', '1:25209', '1:32313', '1:32407', '1:25459', '1:25307', '1:25348', '1:34021', '1:34699', '1:34052', '1:35969', '1:209', '1:241', '1:2178', '1:34913', '1:35041', '1:33729', '1:25427', '1:30717', '1:32013', '1:25484', '1:30859', '1:4444', '1:4859', '1:6779', '1:6787', '1:10509', '1:27645', '1:27696', '1:27329', '1:27343', '1:27527', '1:35869', '1:35872', '1:33104', '1:7723', '1:7806', '1:7822', '1:30287', '1:9586', '1:9621', '1:30791', '1:30942', '1:32203', '1:4735', '1:4626', '1:8090', '1:8214', '1:3719', '1:3723', '1:3680', '1:32208', '1:32760', '1:32634', '1:32806', '1:30328', '1:3606', '1:3140', '1:7440', '1:992', '1:2486', '1:9393', '1:10132', '1:643', '1:935', '1:3039', '1:1303', '1:1334', '1:1875', '1:1901', '1:2616', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/8CC573B4-D113-EA11-9998-901B0E542962.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B8C77942-A60E-EA11-AD67-0CC47A7E68AA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/925A0462-EE0E-EA11-82B0-00266CF3E248.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/8C61D84E-1210-EA11-B859-A4BF011258C8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/E8507146-790E-EA11-BB15-3417EBE7062D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/96D98A15-8114-EA11-A406-D4AE52901D6F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/42398EAC-8F14-EA11-9925-14187751C030.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/66967E0B-930E-EA11-8C76-A4BF012881D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/40EF351F-4F0E-EA11-B140-0CC47A7FC746.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/4058AFAB-E40E-EA11-AC71-98039B3B01D2.root']);