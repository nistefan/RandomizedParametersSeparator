import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:29244', '1:29706', '1:72289', '1:72465', '1:72500', '1:77582', '1:77711', '1:88452', '1:88510', '1:88597', '1:97050', '1:73177', '1:73296', '1:73070', '1:73251', '1:76156', '1:76861', '1:78306', '1:78532', '1:78917', '1:10160', '1:45621', '1:45726', '1:45669', '1:55659', '1:65955', '1:49982', '1:56275', '1:102610', '1:98773', '1:103115', '1:2268', '1:2376', '1:15810', '1:16099', '1:16242', '1:16267', '1:16404', '1:23444', '1:17045', '1:17043', '1:28518', '1:29681', '1:29707', '1:29980', '1:47565', '1:47771', '1:62704', '1:62813', '1:44732', '1:45864', '1:47132', '1:92555', '1:94476', '1:81976', '1:84845', '1:98111', '1:98444', '1:98582', '1:6679', '1:15290', '1:4819', '1:9771', '1:11697', '1:41883', '1:46826', '1:46932', '1:58080', '1:40336', '1:53665', '1:54467', '1:52760', '1:81522', '1:79968', '1:64484', '1:72284', '1:73190', '1:97884', '1:105233', '1:103102', '1:4590', '1:14849', '1:5898', '1:23268', '1:28225', '1:28492', '1:32129', '1:47519', '1:82677', '1:84049', '1:87346', '1:78718', '1:20978', '1:55149', '1:58677', '1:90765', '1:106370', '1:87139', '1:91341', '1:91868', '1:82914', '1:106141', '1:22469', '1:22543', '1:40996', '1:41032', '1:41045', '1:41061', '1:41189', '1:41238', '1:59367', '1:59923', '1:47139', '1:47226', '1:65012', '1:65756', '1:65886', '1:93637', '1:94619', '1:11765', '1:12203', '1:19282', '1:19586', '1:19608', '1:84659', '1:85765', '1:85938', '1:15566', '1:16147', '1:25830', '1:25501', '1:25492', '1:61831', '1:23455', '1:24561', '1:24645', '1:77124', '1:77376', '1:77619', '1:77625', '1:40426', '1:40542', '1:40696', '1:40412', '1:40428', '1:44768', '1:44827', '1:44881', '1:44900', '1:46977', '1:82865', '1:91762', '1:92587', '1:94232', '1:94621', '1:103525', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0AA4F2C-B6FB-E911-BABD-3417EBE70078.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA780643-AC10-EA11-8326-008CFAFBFB7C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5A31D770-76FC-E911-BA45-0CC47AFF0258.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/46E9ED6C-BB0A-EA11-AC8D-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72C119DC-BBF2-E911-B71C-1866DA85DFC0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2812357-95F8-E911-84BD-A4BF0126C074.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/28CA8532-26F8-E911-A6B7-0CC47AA98F98.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BEC88789-04FA-E911-82A0-0CC47A706CF0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D80C91DC-88FC-E911-8EA8-0CC47AFB8104.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E4D8B56-20F4-E911-AE7F-3C4A92F7DD14.root']);