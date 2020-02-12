import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:17179', '1:88306', '1:102413', '1:35663', '1:40388', '1:46419', '1:58752', '1:60207', '1:50752', '1:57928', '1:60598', '1:61679', '1:54535', '1:57469', '1:54368', '1:63534', '1:52341', '1:16959', '1:18413', '1:28149', '1:28415', '1:28425', '1:28986', '1:59525', '1:59548', '1:59552', '1:59606', '1:59682', '1:59912', '1:60000', '1:77839', '1:59355', '1:59881', '1:77360', '1:20077', '1:21538', '1:8659', '1:7091', '1:16159', '1:16320', '1:8273', '1:8447', '1:8350', '1:8384', '1:9203', '1:9219', '1:9428', '1:9476', '1:8349', '1:9241', '1:9066', '1:8357', '1:31720', '1:32190', '1:34132', '1:34457', '1:13970', '1:19158', '1:19327', '1:19357', '1:21633', '1:75320', '1:25232', '1:25310', '1:25874', '1:23736', '1:25243', '1:26661', '1:27721', '1:39026', '1:39414', '1:39961', '1:40154', '1:26618', '1:26831', '1:29013', '1:29029', '1:29102', '1:29245', '1:28736', '1:29241', '1:29282', '1:36923', '1:52668', '1:58622', '1:27861', '1:28096', '1:33279', '1:34058', '1:34115', '1:34284', '1:51915', '1:38656', '1:3480', '1:3902', '1:3667', '1:3673', '1:3691', '1:15977', '1:16506', '1:16995', '1:16665', '1:16126', '1:16467', '1:21554', '1:17574', '1:5624', '1:5716', '1:5426', '1:6423', '1:6762', '1:15130', '1:10953', '1:16579', '1:17597', '1:29734', '1:27531', '1:46023', '1:14926', '1:16122', '1:18134', '1:18471', '1:6819', '1:14807', '1:14799', '1:14898', '1:15271', '1:15312', '1:15513', '1:16002', '1:9075', '1:9499', '1:9524', '1:6740', '1:6886', '1:6961', '1:6982', '1:35563', '1:36282', '1:74130', '1:50770', '1:51373', '1:51755', '1:72882', '1:9123', '1:9213', '1:9683', '1:18216', '1:18298', '1:18500', '1:16427', '1:17335', '1:30152', '1:14306', '1:14311', '1:14654', '1:33240', '1:16640', '1:16712', '1:16829', '1:53067', '1:53770', '1:53892', '1:53925', '1:71543', '1:81777', '1:85443', '1:68362', '1:68952', '1:57151', '1:58038', '1:58128', '1:58220', '1:57494', '1:57752', '1:24503', '1:24506', '1:24522', '1:25037', '1:25087', '1:33148', '1:29931', '1:29999', '1:29995', '1:61562', '1:61368', '1:61867', '1:4066', '1:1997', '1:2572', '1:21590', '1:20921', '1:20964', '1:21132', '1:32775', '1:29955', '1:32064', '1:32216', '1:33266', '1:33182', '1:36453', '1:36718', '1:36864', '1:51639', '1:52016', '1:53143', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8A52D68A-9716-EA11-8A46-C81F66C09A78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3AA8A739-3B1A-EA11-8F16-0025901D08F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6C8ECEC3-DC18-EA11-A954-246E96D149A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DAB73933-B217-EA11-85E7-24BE05C3CBE1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E2A83DB0-0518-EA11-9905-FA163ECADB68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/46514FD2-CA17-EA11-A746-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/5CECA162-FA17-EA11-9B4F-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/18E400F5-FF17-EA11-A992-FA163E9F39BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DEE6096F-1D18-EA11-99A4-FA163E977168.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/404013D1-151C-EA11-A760-588A5AAEEBB8.root']);