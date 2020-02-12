import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:5813', '1:5862', '1:31092', '1:34078', '1:34083', '1:34112', '1:34144', '1:34637', '1:35298', '1:26845', '1:26852', '1:26871', '1:26912', '1:26868', '1:26900', '1:26958', '1:26991', '1:29280', '1:29622', '1:31181', '1:33671', '1:28125', '1:28133', '1:29013', '1:31627', '1:31689', '1:31763', '1:31332', '1:29162', '1:31076', '1:31207', '1:31213', '1:33597', '1:636', '1:1432', '1:26357', '1:26363', '1:29313', '1:29325', '1:29857', '1:33561', '1:33687', '1:33938', '1:30257', '1:25010', '1:29076', '1:30045', '1:30046', '1:30076', '1:28315', '1:29184', '1:31916', '1:33227', '1:33231', '1:1342', '1:1345', '1:1672', '1:2049', '1:2344', '1:31200', '1:31482', '1:31241', '1:31287', '1:31299', '1:33412', '1:1420', '1:3185', '1:4642', '1:5583', '1:5831', '1:5913', '1:26242', '1:26167', '1:26196', '1:2998', '1:26678', '1:26708', '1:7095', '1:9523', '1:29349', '1:5943', '1:5974', '1:29157', '1:26487', '1:26565', '1:29006', '1:28201', '1:26723', '1:26730', '1:26978', '1:34638', '1:34799', '1:34824', '1:34869', '1:35588', '1:35840', '1:35882', '1:35803', '1:35813', '1:5872', '1:5875', '1:27901', '1:7863', '1:7871', '1:7885', '1:8966', '1:25112', '1:25093', '1:25119', '1:25125', '1:8902', '1:9263', '1:7550', '1:33454', '1:33488', '1:33493', '1:10321', '1:10325', '1:10642', '1:10771', '1:1089', '1:8617', '1:6074', '1:5983', '1:33823', '1:3832', '1:5039', '1:3685', '1:5225', '1:5541', '1:5546', '1:5708', '1:5716', '1:4332', '1:5101', '1:28150', '1:28650', '1:33562', '1:26960', '1:28177', '1:10537', '1:10548', '1:10877', '1:10411', '1:10439', '1:10531', '1:10532', '1:10786', '1:10804', '1:10826', '1:10837', '1:10842', '1:10893', '1:10898', '1:28218', '1:32200', '1:32205', '1:501', '1:721', '1:739', '1:806', '1:2984', '1:7571', '1:7596', '1:9075', '1:4391', '1:6033', '1:6070', '1:6649', '1:32493', '1:4962', '1:4959', '1:4995', '1:8028', '1:8045', '1:8344', '1:32019', '1:29053', '1:29009', '1:29037', '1:30298', '1:30300', '1:30324', '1:30668', '1:30644', '1:30898', '1:32162', '1:365', '1:372', '1:389', '1:8980', '1:8982', '1:8998', '1:9601', '1:9582', '1:1133', '1:1166', '1:1262', '1:28130', '1:32442', '1:25863', '1:30145', '1:3859', '1:5004', '1:5015', '1:28141', '1:28148', '1:28275', '1:28283', '1:28623', '1:31565', '1:28358', '1:778', '1:2037', '1:2038', '1:2039', '1:2045', '1:3660', '1:8137', '1:8097', '1:8101', '1:8118', '1:8150', '1:4418', '1:4832', '1:6304', '1:33763', '1:4459', '1:10993', '1:9499', '1:9533', '1:9978', '1:10586', '1:34556', '1:10615', '1:6625', '1:6767', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/7E15F380-C80C-EA11-8CFD-FA163E3D586B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/0EC40F59-F00B-EA11-8CC9-FA163E6339E9.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/C6C5E95D-9C0D-EA11-9721-FA163EB8728A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B48F5F02-930D-EA11-8A90-509A4C9F888B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/261BE081-BC0E-EA11-BB60-0CC47A7E6A74.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/16D9952A-C30F-EA11-867C-98039B3B004A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/E847E4A2-B70E-EA11-9510-002590DD7E50.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/80CF3673-C50E-EA11-9F65-0CC47A7E68AA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B616D331-B10E-EA11-8B23-00266CF94C44.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/58865E3A-470F-EA11-99C4-AC1F6BC67D4A.root']);