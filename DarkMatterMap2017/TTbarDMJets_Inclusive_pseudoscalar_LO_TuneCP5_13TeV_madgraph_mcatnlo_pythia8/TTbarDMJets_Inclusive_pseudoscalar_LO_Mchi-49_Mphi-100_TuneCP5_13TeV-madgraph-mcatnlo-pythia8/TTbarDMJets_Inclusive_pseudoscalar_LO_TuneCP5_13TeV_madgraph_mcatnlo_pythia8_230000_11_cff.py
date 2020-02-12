import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8193', '1:3375', '1:3473', '1:3814', '1:3660', '1:31382', '1:31414', '1:6703', '1:6794', '1:6828', '1:7570', '1:3873', '1:4230', '1:4729', '1:20984', '1:20068', '1:20997', '1:29757', '1:47390', '1:58988', '1:62158', '1:62430', '1:62666', '1:42443', '1:44049', '1:74457', '1:2836', '1:4427', '1:4451', '1:4452', '1:4666', '1:4779', '1:6557', '1:6729', '1:6996', '1:7007', '1:4866', '1:10753', '1:11021', '1:11576', '1:13901', '1:13458', '1:21908', '1:23089', '1:23232', '1:23560', '1:23613', '1:23945', '1:39981', '1:8244', '1:11960', '1:5660', '1:6159', '1:11586', '1:5893', '1:8110', '1:8639', '1:103907', '1:101100', '1:102729', '1:1657', '1:1732', '1:1941', '1:1576', '1:1847', '1:31104', '1:31180', '1:31146', '1:28982', '1:29315', '1:15117', '1:21055', '1:21245', '1:8818', '1:26179', '1:70177', '1:89741', '1:93095', '1:90348', '1:101017', '1:101032', '1:102552', '1:101600', '1:74454', '1:76287', '1:85064', '1:83365', '1:98068', '1:106391', '1:105020', '1:105482', '1:15616', '1:13589', '1:14833', '1:15158', '1:20342', '1:15645', '1:8898', '1:4040', '1:5165', '1:12013', '1:20020', '1:20134', '1:20265', '1:17705', '1:17759', '1:45880', '1:47012', '1:47280', '1:47282', '1:47338', '1:75031', '1:75704', '1:76165', '1:45267', '1:45493', '1:45780', '1:47516', '1:48896', '1:58221', '1:101893', '1:67155', '1:67529', '1:67667', '1:67765', '1:67887', '1:71052', '1:95721', '1:89279', '1:90282', '1:90316', '1:103753', '1:103567', '1:103584', '1:103975', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0C06959B-34F2-E911-A007-40F2E9C6B000.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AADDDD37-EBF9-E911-B35C-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/282CD5F6-EEFA-E911-9E5C-98039B3B004E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E037B27-56F3-E911-8A41-38EAA78D8AF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A04310E4-3E07-EA11-8B88-0CC47AFF02E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/483332F2-DA07-EA11-AEAC-44A842CF0598.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AEC23971-74F7-E911-9030-44A842CFC98B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2F49560-5CF8-E911-A273-0CC47AD9914C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CFEC9C5-B0FB-E911-8390-28924A33AFC2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/228E8BD5-26F5-E911-B71D-509A4C9F8ADB.root']);