import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:19663', '1:19630', '1:19700', '1:19750', '1:19779', '1:19878', '1:19888', '1:27906', '1:34467', '1:34507', '1:34665', '1:34768', '1:34844', '1:34846', '1:34854', '1:36374', '1:33211', '1:33059', '1:28499', '1:28645', '1:28649', '1:28697', '1:28723', '1:33443', '1:33921', '1:33579', '1:9213', '1:42234', '1:43579', '1:96829', '1:96791', '1:99942', '1:16674', '1:16721', '1:85778', '1:87518', '1:91071', '1:91080', '1:91273', '1:40124', '1:45869', '1:39725', '1:41830', '1:48019', '1:47004', '1:47707', '1:50378', '1:50399', '1:50469', '1:50483', '1:50486', '1:51074', '1:51113', '1:51285', '1:51298', '1:51834', '1:52162', '1:58398', '1:58630', '1:59032', '1:58346', '1:88396', '1:1479', '1:1485', '1:1392', '1:1413', '1:1490', '1:1673', '1:3323', '1:3360', '1:3577', '1:3238', '1:3388', '1:3400', '1:3409', '1:32135', '1:36602', '1:38762', '1:40702', '1:40816', '1:44127', '1:44186', '1:18574', '1:19481', '1:70504', '1:73518', '1:73700', '1:74887', '1:77598', '1:72008', '1:72504', '1:72910', '1:75619', '1:76347', '1:64794', '1:70591', '1:70402', '1:70425', '1:71855', '1:62811', '1:65008', '1:65148', '1:66677', '1:65365', '1:65621', '1:69932', '1:70763', '1:98837', '1:100651', '1:102565', '1:102645', '1:95409', '1:102153', '1:77732', '1:95714', '1:96121', '1:99238', '1:20328', '1:20447', '1:19449', '1:21653', '1:27672', '1:26646', '1:28012', '1:28152', '1:19704', '1:27024', '1:72872', '1:72895', '1:75291', '1:75003', '1:82236', '1:94816', '1:97026', '1:97079', '1:98625', '1:99276', '1:96699', '1:99256', '1:103681', '1:93718', '1:93766', '1:93908', '1:54106', '1:81734', '1:81764', '1:81320', '1:91298', '1:91545', '1:91615', '1:94101', '1:97271', '1:100298', '1:100762', '1:102647', '1:102734', '1:96501', '1:104829', '1:100161', '1:100169', '1:100290', '1:70940', '1:72359', '1:73437', '1:65235', '1:95342', '1:95378', '1:95397', '1:99550', '1:104227', '1:104261', '1:104302', '1:104309', '1:105838', '1:105854', '1:105882', '1:105922', '1:105968', '1:105973', '1:105980', '1:49997', '1:50165', '1:50330', '1:50227', '1:59397', '1:63456', '1:64104', '1:64076', '1:64201', '1:62597', '1:62746', '1:62747', '1:63177', '1:82029', '1:82103', '1:82127', '1:82130', '1:82204', '1:96316', '1:96364', '1:96575', '1:97226', '1:67575', '1:67685', '1:67844', '1:84530', '1:84542', '1:83901', '1:85059', '1:85172', '1:94496', '1:94560', '1:20828', '1:20955', '1:21604', '1:21663', '1:21767', '1:24111', '1:52417', '1:52726', '1:52771', '1:52986', '1:53042', '1:53167', '1:53319', '1:53322', '1:57033', '1:78887', '1:78890', '1:78904', '1:80027', '1:39336', '1:39354', '1:39498', '1:39526', '1:39843', '1:39870', '1:39893', '1:40788', '1:40782', '1:40856', '1:40862', '1:58740', '1:58877', '1:62664', '1:62694', '1:76643', '1:76837', '1:76968', '1:77360', '1:100577', '1:80058', '1:80065', '1:80141', '1:36211', '1:36308', '1:36397', '1:50614', '1:50616', '1:50737', '1:51873', '1:92236', '1:99531', '1:98474', '1:98908', '1:99982', '1:92649', '1:98240', '1:88563', '1:88885', '1:88924', '1:104442', '1:12756', '1:62045', '1:62417', '1:62247', '1:62339', '1:65150', '1:64401', '1:65808', '1:65269', '1:81181', '1:65140', '1:65362', '1:65433', '1:65667', '1:65728', '1:65805', '1:68087', '1:68434', '1:68477', '1:68502', '1:68545', '1:70386', '1:71297', '1:71307', '1:71387', '1:71396', '1:91442', '1:91471', '1:94028', '1:27718', '1:52066', '1:52565', '1:52820', '1:53712', '1:65121', '1:66419', '1:86047', '1:78609', '1:82705', '1:84643', '1:79689', '1:79714', '1:80886', '1:84291', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/147D2FEE-7AF4-E911-AC32-FA163ED45046.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8D1CA51-35F3-E911-A13A-7CD30AD09C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/408D623C-B5F2-E911-BEF8-FA163EEBFC01.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B49C1D82-4EF3-E911-9E50-842B2B6AEA0E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4E56313-21F4-E911-B492-1866DA7F9419.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94284CBD-36F4-E911-88E6-A4BF012835C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AB8635C-CDF5-E911-B092-FA163EF38280.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/42C14BE8-BDF6-E911-95B1-AC1F6B56768A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7602BEA4-33F6-E911-95A7-FA163EB69FE7.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B87F77FB-EAF6-E911-A351-0090FAA57A00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E27EC42F-BBF9-E911-9830-B083FED429D5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38B76DAF-36F9-E911-9F0F-001F29089F68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B02AB0B8-ADFA-E911-BDE6-44A842CFD667.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92B1133B-96FA-E911-99FE-FA163E3BEC96.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C990481-CCF8-E911-B595-008CFAE45404.root']);