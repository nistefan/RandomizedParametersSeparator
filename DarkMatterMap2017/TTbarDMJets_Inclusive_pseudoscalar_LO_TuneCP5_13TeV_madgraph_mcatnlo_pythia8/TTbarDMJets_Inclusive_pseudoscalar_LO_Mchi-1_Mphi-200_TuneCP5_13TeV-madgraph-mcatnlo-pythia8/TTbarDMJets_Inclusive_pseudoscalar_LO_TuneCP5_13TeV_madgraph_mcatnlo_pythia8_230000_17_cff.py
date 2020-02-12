import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:16914', '1:73555', '1:73847', '1:27593', '1:54801', '1:56661', '1:80024', '1:47110', '1:46443', '1:85285', '1:64399', '1:64520', '1:64552', '1:73680', '1:75047', '1:75144', '1:73981', '1:75451', '1:94714', '1:12526', '1:12777', '1:13386', '1:13548', '1:13580', '1:22464', '1:22509', '1:22569', '1:22591', '1:22715', '1:22755', '1:32057', '1:32305', '1:32326', '1:32657', '1:1754', '1:1999', '1:1343', '1:1673', '1:1819', '1:1942', '1:1985', '1:40416', '1:40373', '1:40711', '1:89398', '1:89899', '1:90208', '1:90468', '1:91015', '1:8698', '1:10400', '1:14979', '1:41260', '1:41281', '1:41451', '1:42100', '1:61719', '1:93832', '1:26609', '1:31434', '1:80364', '1:80511', '1:74389', '1:57460', '1:64233', '1:66466', '1:67326', '1:98891', '1:102867', '1:65340', '1:65354', '1:81288', '1:17031', '1:17103', '1:17988', '1:17737', '1:40785', '1:53329', '1:62308', '1:64450', '1:83859', '1:94571', '1:95712', '1:10404', '1:10641', '1:10674', '1:85714', '1:97522', '1:97087', '1:81960', '1:57192', '1:59024', '1:46293', '1:46324', '1:64199', '1:103127', '1:103978', '1:48289', '1:49472', '1:53375', '1:55085', '1:56270', '1:86497', '1:94048', '1:77993', '1:83107', '1:85663', '1:4083', '1:4644', '1:7688', '1:18052', '1:17975', '1:19108', '1:24006', '1:24222', '1:19973', '1:22049', '1:25309', '1:25610', '1:28476', '1:28904', '1:28936', '1:29195', '1:48349', '1:48368', '1:48539', '1:56708', '1:88866', '1:89013', '1:89247', '1:89611', '1:23249', '1:23465', '1:23468', '1:49125', '1:49132', '1:49138', '1:56197', '1:96059', '1:96069', '1:96392', '1:96572', '1:96669', '1:96828', '1:40004', '1:40128', '1:30392', '1:30399', '1:30423', '1:30789', '1:43063', '1:43161', '1:43311', '1:43539', '1:43001', '1:46569', '1:41664', '1:41781', '1:41886', '1:43526', '1:28727', '1:48775', '1:59224', '1:60710', '1:62992', '1:73986', '1:48780', '1:49521', '1:46268', '1:55865', '1:81281', '1:51041', '1:58081', '1:62278', '1:58951', '1:60139', '1:60782', '1:61992', '1:82617', '1:81952', '1:84331', '1:88471', '1:84522', '1:84013', '1:84380', '1:84665', '1:87060', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DE44FE63-EB02-EA11-A34D-7CD30AC030B4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/547119DF-1A04-EA11-B104-AC1F6BC67D48.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02B13BB9-62FF-E911-984A-90B11CBCFFEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9CBC629C-D702-EA11-B565-0CC47AFF0200.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/781E8649-6AF8-E911-BBF5-D4AE5264D710.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F82C7F4C-0708-EA11-9AA9-0CC47A5FC2A5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/183064D5-6CF3-E911-BF5D-003048F29A12.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44DAFF4C-FAF4-E911-B4FC-509A4C9EF93B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8C2ADF7-09F5-E911-BBA1-509A4C9F8888.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A1C1EEA-26F7-E911-8EBF-E0071B7A68F0.root']);