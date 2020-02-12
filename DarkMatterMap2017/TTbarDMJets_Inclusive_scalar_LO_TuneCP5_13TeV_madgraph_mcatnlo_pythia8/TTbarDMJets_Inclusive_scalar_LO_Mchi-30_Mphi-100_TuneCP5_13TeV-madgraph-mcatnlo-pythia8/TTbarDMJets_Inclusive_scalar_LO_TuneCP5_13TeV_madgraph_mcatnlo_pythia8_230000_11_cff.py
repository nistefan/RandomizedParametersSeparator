import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:7288', '1:7249', '1:49259', '1:49269', '1:49494', '1:49439', '1:49449', '1:50183', '1:67806', '1:67902', '1:72686', '1:72694', '1:73106', '1:78325', '1:91298', '1:91406', '1:94842', '1:94959', '1:96380', '1:96653', '1:97099', '1:97171', '1:97306', '1:102351', '1:31548', '1:28398', '1:28958', '1:30634', '1:30676', '1:39326', '1:69594', '1:72055', '1:81887', '1:96573', '1:97403', '1:97672', '1:97980', '1:98967', '1:100027', '1:77817', '1:80287', '1:90934', '1:96589', '1:96694', '1:88937', '1:89325', '1:95687', '1:90939', '1:87972', '1:91601', '1:90500', '1:90602', '1:95149', '1:16997', '1:17161', '1:20154', '1:22889', '1:57275', '1:57332', '1:57551', '1:57986', '1:58006', '1:58116', '1:58475', '1:70736', '1:71397', '1:86453', '1:97298', '1:37554', '1:91167', '1:49919', '1:50300', '1:50380', '1:50804', '1:51673', '1:58887', '1:71316', '1:10832', '1:20977', '1:6194', '1:21934', '1:8970', '1:20634', '1:22414', '1:36105', '1:13074', '1:60243', '1:34603', '1:23019', '1:27413', '1:27686', '1:32478', '1:39199', '1:46845', '1:39318', '1:40203', '1:22261', '1:38765', '1:38781', '1:81496', '1:101045', '1:37519', '1:39560', '1:7954', '1:20027', '1:19933', '1:21417', '1:30436', '1:30541', '1:31093', '1:31448', '1:31498', '1:32107', '1:32537', '1:34264', '1:35202', '1:35887', '1:90883', '1:100448', '1:87747', '1:100042', '1:22096', '1:22446', '1:29027', '1:29353', '1:33301', '1:26612', '1:29095', '1:33308', '1:37956', '1:80657', '1:27119', '1:78663', '1:86521', '1:94141', '1:98813', '1:9805', '1:26862', '1:17002', '1:98665', '1:57808', '1:58206', '1:90427', '1:89530', '1:18026', '1:17816', '1:21621', '1:22407', '1:75240', '1:78039', '1:78598', '1:70143', '1:70325', '1:70724', '1:97390', '1:99358', '1:21062', '1:22350', '1:28543', '1:30748', '1:37085', '1:70755', '1:71616', '1:71656', '1:77851', '1:76477', '1:14591', '1:19038', '1:35954', '1:49877', '1:49953', '1:51502', '1:57397', '1:31809', '1:32539', '1:49888', '1:49993', '1:40706', '1:88079', '1:90841', '1:80305', '1:77105', '1:55033', '1:70577', '1:87044', '1:97261', '1:99564', '1:37760', '1:37931', '1:37987', '1:53174', '1:54063', '1:54125', '1:64476', '1:64558', '1:64604', '1:64790', '1:64823', '1:64866', '1:64899', '1:67340', '1:68315', '1:76659', '1:51965', '1:51353', '1:51588', '1:60751', '1:60902', '1:60904', '1:61930', '1:61983', '1:63065', '1:71020', '1:71535', '1:71793', '1:72240', '1:72244', '1:7697', '1:13212', '1:13504', '1:17868', '1:7495', '1:25368', '1:6474', '1:8298', '1:7875', '1:87118', '1:94437', '1:96459', '1:52855', '1:58626', '1:58708', '1:58734', '1:59728', '1:51100', '1:51266', '1:52400', '1:57142', '1:62643', '1:68083', '1:74091', '1:74877', '1:74953', '1:74963', '1:51368', '1:53712', '1:56025', '1:56567', '1:56672', '1:68311', '1:86781', '1:86351', '1:86628', '1:87256', '1:87377', '1:87685', '1:72606', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E0D04434-29FD-E911-8A06-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E2F140C-670A-EA11-AF1D-AC1F6BAC8038.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2C42B47-1A0B-EA11-8F90-0025905B8600.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EA482F8-20FE-E911-B746-0CC47AF9B2B6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92731751-11FE-E911-8809-0CC47AFF02E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/08535ED4-70F7-E911-BD73-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC2DA7CD-1E0B-EA11-804C-AC1F6BAC7F24.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70D87FC9-120B-EA11-946F-0CC47A4C8E26.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AAA24F3-4FFC-E911-AC32-00215A491956.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D24779ED-140B-EA11-B78B-0025905B858A.root']);