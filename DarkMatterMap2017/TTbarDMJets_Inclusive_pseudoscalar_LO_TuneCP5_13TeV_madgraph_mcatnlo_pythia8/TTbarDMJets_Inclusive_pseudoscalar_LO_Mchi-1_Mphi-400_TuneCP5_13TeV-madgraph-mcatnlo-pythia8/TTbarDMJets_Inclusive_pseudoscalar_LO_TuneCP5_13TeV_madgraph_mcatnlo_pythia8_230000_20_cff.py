import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:29269', '1:29447', '1:29608', '1:29778', '1:84487', '1:84870', '1:88476', '1:96913', '1:73289', '1:73401', '1:73159', '1:76147', '1:76374', '1:76150', '1:76645', '1:76897', '1:78558', '1:44853', '1:58466', '1:104574', '1:2051', '1:2211', '1:16095', '1:16390', '1:16711', '1:23043', '1:17474', '1:27983', '1:28105', '1:28156', '1:28563', '1:29641', '1:29966', '1:47854', '1:47973', '1:47977', '1:62787', '1:62868', '1:42840', '1:95468', '1:45162', '1:45243', '1:47085', '1:47765', '1:85594', '1:86841', '1:89662', '1:90733', '1:92700', '1:47316', '1:98233', '1:98918', '1:4531', '1:7746', '1:14608', '1:5827', '1:9285', '1:14918', '1:41860', '1:46091', '1:48317', '1:48993', '1:49371', '1:47817', '1:39201', '1:52434', '1:55729', '1:97158', '1:80096', '1:80305', '1:64343', '1:67045', '1:67786', '1:74337', '1:74572', '1:98277', '1:103835', '1:105244', '1:105861', '1:6239', '1:13480', '1:14494', '1:6481', '1:28038', '1:30897', '1:45224', '1:47546', '1:47909', '1:81145', '1:82109', '1:47309', '1:40277', '1:49414', '1:54100', '1:90827', '1:93101', '1:93318', '1:105819', '1:106047', '1:101376', '1:106104', '1:102013', '1:101289', '1:22105', '1:22549', '1:41025', '1:41039', '1:41048', '1:41344', '1:59227', '1:59332', '1:47098', '1:93729', '1:94691', '1:94788', '1:12603', '1:12441', '1:12640', '1:12865', '1:12894', '1:19191', '1:19309', '1:19506', '1:84681', '1:85061', '1:85410', '1:85677', '1:15814', '1:16016', '1:16024', '1:25106', '1:25320', '1:25608', '1:25615', '1:61574', '1:61952', '1:23584', '1:23787', '1:24288', '1:24529', '1:24675', '1:24518', '1:60292', '1:77204', '1:77225', '1:77401', '1:78139', '1:45504', '1:44705', '1:44778', '1:45039', '1:82044', '1:90748', '1:91820', '1:91845', '1:92566', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0AA4F2C-B6FB-E911-BABD-3417EBE70078.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA780643-AC10-EA11-8326-008CFAFBFB7C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5A31D770-76FC-E911-BA45-0CC47AFF0258.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/46E9ED6C-BB0A-EA11-AC8D-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72C119DC-BBF2-E911-B71C-1866DA85DFC0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2812357-95F8-E911-84BD-A4BF0126C074.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/28CA8532-26F8-E911-A6B7-0CC47AA98F98.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BEC88789-04FA-E911-82A0-0CC47A706CF0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D80C91DC-88FC-E911-8EA8-0CC47AFB8104.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E4D8B56-20F4-E911-AE7F-3C4A92F7DD14.root']);