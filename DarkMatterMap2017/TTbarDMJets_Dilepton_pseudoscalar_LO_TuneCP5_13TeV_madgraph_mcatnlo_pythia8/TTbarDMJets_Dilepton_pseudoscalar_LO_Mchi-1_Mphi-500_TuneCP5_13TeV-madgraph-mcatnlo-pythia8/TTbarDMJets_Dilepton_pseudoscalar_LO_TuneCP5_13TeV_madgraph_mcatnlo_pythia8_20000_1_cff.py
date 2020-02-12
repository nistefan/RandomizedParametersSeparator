import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:5754', '1:30189', '1:31283', '1:31427', '1:31533', '1:34830', '1:34857', '1:34886', '1:35202', '1:26811', '1:26786', '1:26880', '1:26992', '1:28126', '1:30598', '1:28225', '1:28233', '1:31500', '1:31179', '1:28128', '1:28243', '1:28254', '1:28286', '1:28642', '1:31507', '1:31068', '1:26220', '1:26479', '1:29034', '1:29164', '1:29354', '1:33685', '1:33951', '1:33952', '1:818', '1:30537', '1:25025', '1:31699', '1:1530', '1:31268', '1:33420', '1:31568', '1:29625', '1:7287', '1:29161', '1:26432', '1:26459', '1:29367', '1:26712', '1:26744', '1:32148', '1:34863', '1:34894', '1:35875', '1:35854', '1:35286', '1:35814', '1:35837', '1:5841', '1:5849', '1:30057', '1:7849', '1:7860', '1:7876', '1:25124', '1:32906', '1:33487', '1:1356', '1:26070', '1:29814', '1:3754', '1:3808', '1:3826', '1:5405', '1:5443', '1:5549', '1:5692', '1:5826', '1:4732', '1:26239', '1:26385', '1:28171', '1:28170', '1:7307', '1:10570', '1:10822', '1:32589', '1:2827', '1:2930', '1:5305', '1:5682', '1:5713', '1:5715', '1:5723', '1:7564', '1:4881', '1:35422', '1:28173', '1:28302', '1:8020', '1:8217', '1:8724', '1:5506', '1:5803', '1:32438', '1:30470', '1:32517', '1:32521', '1:26484', '1:26490', '1:32724', '1:30288', '1:30641', '1:30388', '1:30491', '1:32166', '1:104', '1:361', '1:379', '1:404', '1:518', '1:541', '1:645', '1:8186', '1:8914', '1:9732', '1:1129', '1:1139', '1:32396', '1:32409', '1:25867', '1:3805', '1:5005', '1:5140', '1:732', '1:779', '1:786', '1:906', '1:8120', '1:4145', '1:4289', '1:4305', '1:4439', '1:31863', '1:4326', '1:4853', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/7E15F380-C80C-EA11-8CFD-FA163E3D586B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/0EC40F59-F00B-EA11-8CC9-FA163E6339E9.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/C6C5E95D-9C0D-EA11-9721-FA163EB8728A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B48F5F02-930D-EA11-8A90-509A4C9F888B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/261BE081-BC0E-EA11-BB60-0CC47A7E6A74.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/16D9952A-C30F-EA11-867C-98039B3B004A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/E847E4A2-B70E-EA11-9510-002590DD7E50.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/80CF3673-C50E-EA11-9F65-0CC47A7E68AA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B616D331-B10E-EA11-8B23-00266CF94C44.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/58865E3A-470F-EA11-99C4-AC1F6BC67D4A.root']);