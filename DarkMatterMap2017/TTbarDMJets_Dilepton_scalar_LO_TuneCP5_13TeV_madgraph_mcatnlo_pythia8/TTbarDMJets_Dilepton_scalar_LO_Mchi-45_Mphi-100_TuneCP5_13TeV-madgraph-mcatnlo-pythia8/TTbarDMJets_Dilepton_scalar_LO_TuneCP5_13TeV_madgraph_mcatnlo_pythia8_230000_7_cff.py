import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:598', '1:686', '1:3215', '1:4570', '1:2002', '1:2368', '1:68648', '1:68691', '1:27086', '1:26633', '1:32279', '1:32823', '1:34686', '1:56987', '1:56264', '1:57503', '1:57646', '1:72030', '1:74971', '1:76397', '1:76442', '1:78667', '1:78699', '1:78843', '1:78895', '1:78898', '1:96836', '1:96997', '1:97095', '1:97432', '1:83882', '1:102321', '1:102344', '1:102286', '1:85935', '1:85952', '1:86608', '1:86617', '1:86652', '1:86976', '1:91964', '1:61282', '1:61635', '1:61614', '1:62044', '1:67320', '1:67387', '1:67456', '1:67913', '1:92576', '1:92849', '1:92863', '1:5173', '1:5399', '1:7687', '1:7756', '1:8007', '1:14235', '1:14374', '1:21002', '1:5612', '1:7841', '1:7827', '1:39445', '1:44377', '1:45092', '1:50347', '1:20571', '1:21194', '1:21203', '1:21997', '1:34168', '1:33130', '1:33821', '1:33841', '1:33843', '1:91406', '1:91460', '1:91570', '1:94429', '1:86382', '1:86621', '1:48539', '1:48571', '1:52609', '1:68989', '1:67489', '1:68901', '1:86885', '1:88170', '1:91638', '1:10153', '1:12826', '1:14006', '1:14103', '1:14631', '1:72122', '1:76767', '1:77903', '1:92686', '1:5573', '1:7084', '1:7409', '1:7666', '1:5179', '1:5130', '1:8111', '1:12921', '1:14516', '1:15107', '1:15153', '1:15154', '1:14157', '1:14214', '1:14265', '1:14275', '1:9825', '1:16549', '1:21620', '1:24339', '1:24393', '1:24406', '1:21048', '1:26134', '1:26282', '1:38800', '1:42393', '1:42821', '1:42864', '1:63018', '1:63101', '1:63247', '1:67723', '1:63676', '1:58387', '1:58394', '1:87549', '1:98551', '1:87614', '1:88790', '1:91578', '1:91835', '1:1403', '1:7336', '1:8890', '1:16281', '1:21110', '1:42633', '1:49529', '1:44566', '1:2648', '1:5428', '1:7028', '1:7201', '1:7309', '1:7525', '1:37342', '1:43797', '1:45228', '1:46393', '1:46753', '1:43016', '1:47023', '1:61037', '1:62552', '1:59577', '1:62911', '1:64553', '1:63635', '1:43983', '1:79548', '1:84302', '1:84593', '1:84685', '1:78016', '1:78081', '1:78793', '1:79268', '1:79626', '1:81092', '1:96250', '1:97378', '1:97710', '1:98457', '1:96518', '1:98467', '1:98611', '1:99629', '1:102695', '1:54451', '1:54567', '1:54588', '1:54796', '1:55046', '1:75088', '1:75342', '1:75593', '1:78972', '1:81069', '1:81705', '1:84023', '1:81306', '1:93564', '1:94054', '1:94062', '1:94115', '1:94127', '1:94151', '1:94153', '1:104668', '1:104271', '1:104560', '1:104640', '1:104715', '1:100048', '1:100327', '1:100702', '1:100774', '1:100825', '1:100836', '1:100848', '1:102106', '1:102579', '1:102736', '1:102817', '1:49606', '1:97073', '1:98019', '1:61038', '1:61052', '1:61295', '1:61561', '1:62093', '1:63503', '1:63505', '1:86439', '1:86498', '1:87180', '1:76257', '1:76656', '1:88005', '1:35157', '1:50503', '1:52521', '1:53922', '1:85428', '1:85598', '1:55718', '1:52848', '1:54692', '1:66672', '1:67169', '1:64032', '1:40761', '1:40511', '1:48709', '1:48944', '1:50134', '1:73467', '1:73620', '1:70999', '1:71264', '1:71463', '1:71679', '1:73247', '1:100780', '1:103244', '1:79079', '1:80431', '1:84534', '1:65321', '1:65338', '1:54573', '1:54581', '1:54640', '1:54670', '1:54672', '1:54713', '1:54714', '1:54717', '1:54730', '1:54734', '1:57587', '1:57846', '1:57468', '1:57859', '1:74768', '1:64209', '1:64587', '1:65555', '1:66055', '1:66859', '1:65066', '1:70678', '1:71410', '1:66251', '1:66328', '1:66340', '1:66408', '1:66777', '1:66618', '1:73464', '1:73353', '1:73520', '1:73532', '1:73683', '1:73685', '1:73656', '1:86426', '1:87287', '1:87309', '1:66733', '1:66545', '1:83473', '1:82883', '1:82940', '1:83030', '1:83047', '1:83090', '1:83115', '1:83261', '1:83293', '1:83388', '1:105630', '1:105648', '1:105679', '1:10920', '1:10930', '1:10931', '1:10968', '1:10984', '1:12064', '1:12144', '1:12167', '1:82666', '1:82784', '1:82794', '1:82900', '1:82911', '1:82964', '1:84935', '1:84997', '1:82819', '1:102590', '1:102676', '1:102684', '1:49022', '1:48874', '1:48906', '1:48994', '1:49138', '1:77133', '1:77460', '1:77571', '1:77599', '1:77704', '1:19029', '1:19245', '1:20020', '1:20154', '1:55405', '1:55562', '1:55575', '1:55581', '1:55595', '1:55610', '1:55715', '1:83569', '1:37818', '1:49245', '1:49275', '1:49496', '1:49553', '1:49643', '1:49768', '1:49783', '1:49892', '1:80546', '1:80272', '1:80291', '1:80374', '1:92248', '1:82291', '1:82429', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CA7CE758-D1F7-E911-B277-F01FAFD8F7D6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C1D320E-78EF-E911-A729-509A4C9EF924.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3E1280BB-BBF9-E911-80A0-FA163EA79D8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0E73436E-79EF-E911-89CC-E0071B73C630.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C45C6C1C-8C10-EA11-9B52-0025907D1D6C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F67A5D3B-B7F3-E911-9613-28924A3504DA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE1665D5-CBF7-E911-8868-14187741278B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F805B571-9702-EA11-AE26-B083FED138B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC6B26A7-88F2-E911-9CDE-C4544423E320.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7810BEF1-97F3-E911-8096-089E0158CDED.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8EB6E369-98F3-E911-9E0F-20CF3019DF13.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D074ADB4-D9F2-E911-B16F-1418774A2C9C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E8D7450-7FEF-E911-9BF4-509A4C9EF923.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72D74153-AB02-EA11-8630-0CC47AFCC41A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/34767E6C-04F3-E911-BB76-848F69FD0EAB.root']);