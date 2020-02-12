import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:48521', '1:48620', '1:69108', '1:69459', '1:99553', '1:91632', '1:96761', '1:16537', '1:17131', '1:17535', '1:62584', '1:62587', '1:62795', '1:68004', '1:77971', '1:87319', '1:70637', '1:70698', '1:70734', '1:70761', '1:70838', '1:72240', '1:72209', '1:72467', '1:74786', '1:4809', '1:103857', '1:104684', '1:15327', '1:15536', '1:15876', '1:17933', '1:18321', '1:18436', '1:24387', '1:24689', '1:26561', '1:33953', '1:35564', '1:35929', '1:24541', '1:28023', '1:27516', '1:568', '1:4389', '1:4393', '1:137', '1:3227', '1:7334', '1:7737', '1:7879', '1:7999', '1:8450', '1:8707', '1:8864', '1:10051', '1:5618', '1:12908', '1:14412', '1:14445', '1:716', '1:764', '1:4052', '1:4588', '1:597', '1:2953', '1:3025', '1:3710', '1:4175', '1:8530', '1:8826', '1:9641', '1:10105', '1:1132', '1:3235', '1:3969', '1:4776', '1:32370', '1:32758', '1:34662', '1:5650', '1:5790', '1:2411', '1:2957', '1:3926', '1:36313', '1:12582', '1:16175', '1:20421', '1:19883', '1:21487', '1:21933', '1:24605', '1:24738', '1:27735', '1:2212', '1:2284', '1:2685', '1:9435', '1:9439', '1:19463', '1:46984', '1:38374', '1:59610', '1:64319', '1:65210', '1:69799', '1:18693', '1:21756', '1:19612', '1:27129', '1:27308', '1:21847', '1:24651', '1:27071', '1:18577', '1:94342', '1:64958', '1:64983', '1:68546', '1:70627', '1:73139', '1:75188', '1:7638', '1:8115', '1:8255', '1:8441', '1:7951', '1:8260', '1:8979', '1:10229', '1:10313', '1:12859', '1:12814', '1:7726', '1:9320', '1:7735', '1:8069', '1:8144', '1:8182', '1:7917', '1:7966', '1:7986', '1:8176', '1:8474', '1:8491', '1:9744', '1:9753', '1:9608', '1:9795', '1:8434', '1:8640', '1:10775', '1:10849', '1:10875', '1:14806', '1:14893', '1:14914', '1:14930', '1:14941', '1:14955', '1:14972', '1:16354', '1:16441', '1:88972', '1:88979', '1:88981', '1:60216', '1:54855', '1:61773', '1:61856', '1:67967', '1:68061', '1:62755', '1:63077', '1:64404', '1:67569', '1:68777', '1:87344', '1:88455', '1:93248', '1:88243', '1:91846', '1:87547', '1:88025', '1:77791', '1:77846', '1:100366', '1:100882', '1:97025', '1:100765', '1:100791', '1:100830', '1:102227', '1:102308', '1:102316', '1:102393', '1:102517', '1:104359', '1:104462', '1:104474', '1:105713', '1:106115', '1:106142', '1:105758', '1:2239', '1:2617', '1:2619', '1:45046', '1:47922', '1:42788', '1:47788', '1:65381', '1:65470', '1:70270', '1:70170', '1:70282', '1:625', '1:689', '1:2476', '1:2898', '1:10855', '1:15108', '1:17089', '1:45549', '1:49981', '1:51123', '1:51333', '1:64636', '1:64662', '1:64679', '1:21746', '1:21955', '1:21975', '1:24453', '1:24470', '1:77829', '1:59604', '1:59823', '1:59902', '1:60761', '1:61794', '1:49865', '1:51928', '1:56747', '1:60024', '1:60026', '1:60053', '1:60088', '1:60107', '1:24008', '1:24263', '1:24271', '1:24304', '1:24314', '1:24337', '1:24428', '1:36233', '1:36327', '1:36489', '1:36646', '1:35348', '1:34818', '1:34317', '1:34328', '1:37992', '1:38119', '1:45453', '1:45482', '1:45711', '1:44145', '1:44177', '1:44212', '1:44404', '1:44421', '1:44481', '1:44556', '1:56695', '1:56858', '1:56880', '1:56968', '1:57254', '1:60110', '1:60798', '1:60245', '1:15092', '1:15477', '1:15269', '1:45569', '1:45631', '1:45842', '1:46128', '1:46928', '1:47043', '1:47060', '1:46609', '1:47051', '1:47094', '1:47157', '1:47754', '1:51760', '1:53836', '1:28595', '1:28657', '1:32546', '1:32781', '1:27202', '1:33039', '1:43522', '1:46601', '1:27941', '1:28084', '1:28172', '1:28213', '1:28251', '1:44629', '1:44654', '1:10238', '1:10254', '1:12045', '1:12065', '1:12165', '1:12207', '1:16758', '1:16844', '1:16982', '1:24654', '1:85983', '1:86120', '1:86288', '1:99783', '1:68052', '1:68552', '1:68584', '1:68377', '1:68698', '1:68844', '1:68613', '1:75587', '1:77734', '1:77763', '1:77022', '1:77442', '1:95388', '1:95809', '1:95918', '1:77163', '1:77413', '1:77467', '1:77500', '1:77505', '1:77522', '1:91309', '1:88434', '1:91416', '1:93177', '1:93981', '1:94561', '1:94647', '1:94650', '1:103509', '1:88469', '1:88524', '1:93956', '1:93968', '1:95976', '1:95681', '1:96026', '1:72', '1:1357', '1:1640', '1:658', '1:944', '1:21000', '1:15146', '1:17293', '1:17384', '1:17386', '1:18089', '1:18191', '1:33155', '1:44971', '1:48496', '1:50150', '1:46049', '1:46098', '1:46392', '1:46521', '1:46546', '1:40130', '1:44621', '1:44678', '1:47274', '1:40060', '1:45570', '1:49801', '1:47098', '1:47349', '1:49949', '1:50069', '1:53372', '1:798', '1:45816', '1:48430', '1:48471', '1:48593', '1:49740', '1:49969', '1:40135', '1:51529', '1:52698', '1:53014', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84233716-610E-EA11-A99E-AC1F6B1AF194.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92C94FAE-5604-EA11-B1B4-AC1F6B1AF05A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA68F6BC-8307-EA11-95D2-1CC1DE055158.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/46E4AEC6-90ED-E911-B705-EC0D9A82262E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5EC502A2-6603-EA11-90F8-0CC47A4DED8C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8AA75E62-AB02-EA11-B51D-0025905C3E68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8DA5D68-F10B-EA11-AFB4-0025905B85E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78EFAF8D-1A04-EA11-8B9D-002590A83354.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2ABCC36E-6AFF-E911-8B20-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CED587AE-2CEF-E911-AD36-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E5BA0CA-85EE-E911-A8AF-C4544423E341.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B47C7A37-D803-EA11-AFBA-0CC47A5FA3BD.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/468AC653-A5F2-E911-B9B2-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9498531C-02EE-E911-B5FE-EC0D9A822626.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DEFACFCF-8E02-EA11-9176-AC1F6BABF8D5.root']);