import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:7155', '1:31360', '1:34367', '1:28869', '1:23453', '1:28968', '1:38974', '1:29112', '1:38162', '1:38203', '1:38430', '1:38527', '1:38213', '1:68384', '1:81494', '1:81589', '1:85188', '1:1232', '1:1803', '1:2636', '1:5047', '1:1122', '1:1472', '1:1488', '1:1702', '1:3069', '1:4012', '1:4884', '1:4118', '1:22017', '1:26794', '1:26922', '1:33770', '1:33939', '1:35040', '1:37082', '1:32093', '1:39358', '1:30165', '1:34695', '1:56447', '1:49211', '1:57815', '1:63555', '1:50032', '1:60288', '1:8688', '1:8513', '1:10066', '1:10311', '1:10797', '1:23955', '1:26894', '1:28831', '1:34433', '1:32195', '1:34871', '1:34976', '1:37599', '1:102167', '1:89321', '1:88001', '1:88766', '1:88062', '1:88513', '1:88991', '1:13799', '1:14583', '1:15065', '1:626', '1:3126', '1:36597', '1:33064', '1:33614', '1:7203', '1:10764', '1:20196', '1:6664', '1:17797', '1:25188', '1:29063', '1:38519', '1:97662', '1:46208', '1:39697', '1:40662', '1:49458', '1:50872', '1:52895', '1:57216', '1:31630', '1:46379', '1:30154', '1:46984', '1:31994', '1:35054', '1:35061', '1:60641', '1:61760', '1:63544', '1:79239', '1:64115', '1:55534', '1:55870', '1:62902', '1:68844', '1:71041', '1:72449', '1:72965', '1:80352', '1:81977', '1:101931', '1:71049', '1:71364', '1:102124', '1:102132', '1:99161', '1:101678', '1:101271', '1:80366', '1:90349', '1:90433', '1:91593', '1:90348', '1:90336', '1:90478', '1:95212', '1:96576', '1:842', '1:2346', '1:2595', '1:3070', '1:2439', '1:3684', '1:2386', '1:3623', '1:3254', '1:3837', '1:3979', '1:3765', '1:4918', '1:29772', '1:31446', '1:32305', '1:23974', '1:24053', '1:24658', '1:31703', '1:31727', '1:37523', '1:49795', '1:51530', '1:24841', '1:39092', '1:39659', '1:2437', '1:2563', '1:8814', '1:826', '1:3500', '1:3581', '1:2480', '1:173', '1:471', '1:718', '1:1162', '1:1450', '1:2050', '1:3255', '1:3355', '1:1890', '1:4071', '1:5002', '1:67', '1:2619', '1:3484', '1:17755', '1:22327', '1:25336', '1:25875', '1:26332', '1:26814', '1:29111', '1:29369', '1:27148', '1:46594', '1:28346', '1:33417', '1:1933', '1:38723', '1:76805', '1:76813', '1:76825', '1:76947', '1:76967', '1:40439', '1:51727', '1:52039', '1:75941', '1:76191', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A29568F-0204-EA11-8E9E-20CF3027A6B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A57B881-3F03-EA11-8CAB-D48564594FB4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FA29DAC3-4304-EA11-8CA5-F01FAFD6996C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2CFB0664-3407-EA11-BC37-A0369FD0B3E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCBAF234-0107-EA11-95FC-0CC47A4DEDD6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C5438B6-1B08-EA11-B2E6-90B11CBCFFA9.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60A4990B-DB07-EA11-BFBE-44A842CFD5B1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0682B29D-DD08-EA11-AE0F-AC1F6BAC7ACC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/520DFFB1-110B-EA11-88A1-0CC47A7C353E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C157FD6-120B-EA11-8BA5-0025905A60C6.root']);