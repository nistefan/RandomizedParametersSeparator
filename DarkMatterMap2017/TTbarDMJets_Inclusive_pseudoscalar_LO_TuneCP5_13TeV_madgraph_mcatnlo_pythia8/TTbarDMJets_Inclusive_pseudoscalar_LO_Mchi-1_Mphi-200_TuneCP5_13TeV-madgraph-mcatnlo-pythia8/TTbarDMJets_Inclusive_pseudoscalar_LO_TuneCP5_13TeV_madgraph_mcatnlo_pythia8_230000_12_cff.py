import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:32691', '1:62714', '1:97790', '1:98389', '1:98964', '1:76510', '1:76931', '1:80654', '1:76739', '1:80307', '1:80713', '1:80875', '1:105677', '1:28888', '1:55148', '1:55001', '1:65707', '1:92293', '1:52281', '1:53318', '1:53410', '1:56629', '1:46678', '1:41742', '1:87700', '1:89786', '1:24057', '1:29605', '1:42313', '1:42800', '1:44489', '1:51668', '1:56459', '1:81024', '1:102006', '1:105876', '1:70320', '1:70922', '1:82126', '1:82588', '1:83129', '1:89695', '1:83903', '1:89074', '1:91070', '1:87479', '1:40580', '1:28048', '1:28588', '1:54044', '1:57436', '1:93466', '1:102592', '1:45985', '1:47769', '1:48261', '1:78821', '1:78965', '1:93339', '1:93344', '1:94357', '1:97911', '1:102414', '1:102447', '1:102594', '1:104073', '1:104072', '1:29270', '1:29598', '1:29683', '1:29709', '1:29796', '1:51566', '1:52613', '1:106053', '1:105923', '1:106133', '1:28721', '1:42034', '1:39401', '1:44187', '1:48768', '1:58681', '1:55757', '1:57541', '1:26605', '1:31969', '1:31979', '1:31498', '1:59705', '1:60759', '1:82442', '1:105059', '1:105905', '1:106232', '1:81654', '1:81790', '1:94933', '1:95713', '1:96117', '1:13669', '1:26114', '1:8647', '1:15693', '1:21233', '1:26276', '1:21091', '1:31248', '1:8528', '1:4734', '1:4971', '1:21638', '1:25305', '1:26727', '1:75010', '1:48848', '1:52866', '1:54480', '1:54934', '1:53343', '1:56233', '1:16596', '1:57832', '1:58642', '1:61788', '1:95502', '1:11374', '1:15489', '1:20225', '1:11646', '1:11683', '1:12513', '1:12525', '1:13191', '1:13473', '1:13553', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E9DF7BC-D2F9-E911-B963-B083FED04276.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3C3D00F4-CD0A-EA11-88A9-0025905B8606.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CD12387-68F6-E911-88C2-0CC47AD98CF2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CE823415-E20A-EA11-A829-0CC47A4C8EC6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40A9763B-3EF4-E911-9F26-A4BF012835C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE6B34A2-FB0A-EA11-92D9-0025905B856C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/88A1CEE3-EF06-EA11-8583-00269E95AF28.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC4A2E9C-CBF2-E911-BAB9-1866DA7F9816.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E65590CA-5900-EA11-8968-0025904B5F8C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D66BAE7C-37F7-E911-A016-FA163EE52FA2.root']);