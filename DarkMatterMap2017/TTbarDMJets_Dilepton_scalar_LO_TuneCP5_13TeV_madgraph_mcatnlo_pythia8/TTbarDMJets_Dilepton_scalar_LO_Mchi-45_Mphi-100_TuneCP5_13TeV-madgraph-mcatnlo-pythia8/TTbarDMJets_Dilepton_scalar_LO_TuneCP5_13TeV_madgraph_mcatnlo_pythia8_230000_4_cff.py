import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:61416', '1:61426', '1:61851', '1:61949', '1:62054', '1:62194', '1:62244', '1:62232', '1:80237', '1:80290', '1:80929', '1:80936', '1:80971', '1:91251', '1:91261', '1:66754', '1:66881', '1:66967', '1:69166', '1:77095', '1:77172', '1:77217', '1:77352', '1:88716', '1:24124', '1:27161', '1:27831', '1:24174', '1:26849', '1:34064', '1:34615', '1:37281', '1:37859', '1:37875', '1:104408', '1:104511', '1:104574', '1:104723', '1:104736', '1:51953', '1:52194', '1:52427', '1:99251', '1:99303', '1:99345', '1:99874', '1:102728', '1:102759', '1:102760', '1:102795', '1:102931', '1:46416', '1:46701', '1:46807', '1:46812', '1:64457', '1:70400', '1:71712', '1:73282', '1:92741', '1:92736', '1:92737', '1:93122', '1:4566', '1:4785', '1:18557', '1:18727', '1:18741', '1:18796', '1:18826', '1:18850', '1:19218', '1:98257', '1:891', '1:1795', '1:4686', '1:7972', '1:7993', '1:10889', '1:12057', '1:12083', '1:32621', '1:35668', '1:92682', '1:92731', '1:92795', '1:95235', '1:20662', '1:20744', '1:55754', '1:55786', '1:55831', '1:55861', '1:55912', '1:87015', '1:87681', '1:92652', '1:92823', '1:14068', '1:12936', '1:12958', '1:12997', '1:49044', '1:49569', '1:50428', '1:83156', '1:60210', '1:67758', '1:68123', '1:68744', '1:64143', '1:94236', '1:97099', '1:97268', '1:97228', '1:97250', '1:97263', '1:97285', '1:97351', '1:97539', '1:104282', '1:104491', '1:3136', '1:3201', '1:3352', '1:4280', '1:4805', '1:12173', '1:58839', '1:58998', '1:97326', '1:97333', '1:34772', '1:55523', '1:58580', '1:61765', '1:63606', '1:72513', '1:72523', '1:72643', '1:74372', '1:74399', '1:74314', '1:74346', '1:74500', '1:74506', '1:74628', '1:105225', '1:105259', '1:105365', '1:105359', '1:41462', '1:44425', '1:49326', '1:49368', '1:49693', '1:49811', '1:49859', '1:50176', '1:83432', '1:83567', '1:83667', '1:83805', '1:103093', '1:103452', '1:103645', '1:103655', '1:48835', '1:52301', '1:53157', '1:53172', '1:53437', '1:55282', '1:55287', '1:55641', '1:55750', '1:55851', '1:55886', '1:55944', '1:57361', '1:79157', '1:79201', '1:79379', '1:79616', '1:79290', '1:102898', '1:102911', '1:103286', '1:1530', '1:1688', '1:1594', '1:1798', '1:1821', '1:1869', '1:4100', '1:2820', '1:12570', '1:12607', '1:34084', '1:34968', '1:37638', '1:4133', '1:4314', '1:4228', '1:9466', '1:9704', '1:9804', '1:9831', '1:9926', '1:9998', '1:9458', '1:9515', '1:9830', '1:10590', '1:10662', '1:10680', '1:10685', '1:10720', '1:39464', '1:35114', '1:45494', '1:44329', '1:48491', '1:9701', '1:9711', '1:9683', '1:9692', '1:10638', '1:10692', '1:10710', '1:10719', '1:10628', '1:10698', '1:10730', '1:12565', '1:49611', '1:49615', '1:50314', '1:60864', '1:54271', '1:54641', '1:104321', '1:104412', '1:102820', '1:102823', '1:103929', '1:1291', '1:2004', '1:3716', '1:52220', '1:60723', '1:62390', '1:55327', '1:56065', '1:57487', '1:76406', '1:81943', '1:81978', '1:16627', '1:19141', '1:19249', '1:37696', '1:19592', '1:20856', '1:21569', '1:21674', '1:21728', '1:21830', '1:21911', '1:26145', '1:26570', '1:40218', '1:65820', '1:66769', '1:70237', '1:70900', '1:70928', '1:71177', '1:72505', '1:63354', '1:65520', '1:8976', '1:14554', '1:16220', '1:16513', '1:16423', '1:16861', '1:17707', '1:17816', '1:32789', '1:62990', '1:66281', '1:66442', '1:66450', '1:66559', '1:66621', '1:68578', '1:65294', '1:65549', '1:72192', '1:65599', '1:73396', '1:92208', '1:61057', '1:63300', '1:67037', '1:102334', '1:102954', '1:102438', '1:102608', '1:103927', '1:78598', '1:80261', '1:80658', '1:80676', '1:81694', '1:81936', '1:92289', '1:92295', '1:88242', '1:88802', '1:70971', '1:71843', '1:57339', '1:57049', '1:57218', '1:57239', '1:57331', '1:58931', '1:58880', '1:91399', '1:91426', '1:91444', '1:91656', '1:91823', '1:91941', '1:91946', '1:91953', '1:105007', '1:3207', '1:3713', '1:3971', '1:4966', '1:47297', '1:47723', '1:10533', '1:10607', '1:10933', '1:12315', '1:12881', '1:18528', '1:20084', '1:86572', '1:87771', '1:87957', '1:74750', '1:87701', '1:91511', '1:96187', '1:96923', '1:99617', '1:87650', '1:103076', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C2B2B4A5-90FA-E911-A1ED-FA163E596216.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44AD8F54-33FC-E911-BFC1-44A842CFD5D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BC0C7A45-B3FB-E911-9A20-0025905C53AA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/18D4DE3D-06FB-E911-9D07-0CC47A4DEE78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D60A6FA0-CCFC-E911-BDAF-0CC47A5FC679.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BCA2AA4C-68FB-E911-A22D-001CC4A6CCE6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/68A10C47-6CFF-E911-A5E7-0242AC1C0507.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70D242A1-7FFF-E911-934F-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C045F616-49FE-E911-9BA5-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FAD01C50-69FF-E911-BBD7-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE2BDBAA-1F02-EA11-9F99-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84EBD031-DAFE-E911-A032-002590DE39F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9AE2976D-2503-EA11-916D-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8BF48D7-28FF-E911-86D4-AC1F6BC67D46.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8A44B795-0403-EA11-B303-0CC47AFF014C.root']);