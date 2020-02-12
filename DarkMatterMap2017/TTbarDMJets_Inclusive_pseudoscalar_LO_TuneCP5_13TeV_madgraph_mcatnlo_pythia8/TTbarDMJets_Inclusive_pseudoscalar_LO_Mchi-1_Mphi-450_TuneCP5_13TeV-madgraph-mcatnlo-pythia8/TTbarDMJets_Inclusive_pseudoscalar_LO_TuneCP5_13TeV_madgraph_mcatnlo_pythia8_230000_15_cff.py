import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8442', '1:11058', '1:11288', '1:11539', '1:11803', '1:11837', '1:11848', '1:20641', '1:20434', '1:20944', '1:20705', '1:20723', '1:20801', '1:20806', '1:20955', '1:21474', '1:21903', '1:23087', '1:24154', '1:24160', '1:24217', '1:24289', '1:24322', '1:28430', '1:27850', '1:28060', '1:28519', '1:28601', '1:28658', '1:28883', '1:41197', '1:41307', '1:54269', '1:56998', '1:58767', '1:60461', '1:64006', '1:64842', '1:67354', '1:71019', '1:81781', '1:72849', '1:71671', '1:72794', '1:78697', '1:4709', '1:6786', '1:58379', '1:70049', '1:70264', '1:55629', '1:56125', '1:56498', '1:59072', '1:55307', '1:55458', '1:55578', '1:55598', '1:55676', '1:56803', '1:56870', '1:56966', '1:57556', '1:58055', '1:58064', '1:96448', '1:96912', '1:97065', '1:97805', '1:98113', '1:13875', '1:14363', '1:14388', '1:14397', '1:22645', '1:22722', '1:22977', '1:22797', '1:22799', '1:27922', '1:27921', '1:2979', '1:2700', '1:9220', '1:14464', '1:24188', '1:14642', '1:27332', '1:24598', '1:40938', '1:42005', '1:45213', '1:81720', '1:47186', '1:75879', '1:88944', '1:17610', '1:17163', '1:10671', '1:19799', '1:19912', '1:19931', '1:24388', '1:24393', '1:15351', '1:15486', '1:16009', '1:15965', '1:16044', '1:20990', '1:21111', '1:21216', '1:21276', '1:21327', '1:21346', '1:21349', '1:42137', '1:42625', '1:45298', '1:45340', '1:45387', '1:45495', '1:45506', '1:56431', '1:49522', '1:51355', '1:55807', '1:55879', '1:55902', '1:56123', '1:56933', '1:59169', '1:14974', '1:15051', '1:62380', '1:98719', '1:78877', '1:83204', '1:101312', '1:102041', '1:66298', '1:86486', '1:86521', '1:86554', '1:86621', '1:86673', '1:86926', '1:87020', '1:96051', '1:96291', '1:95740', '1:47011', '1:54312', '1:54587', '1:54613', '1:96638', '1:97037', '1:97468', '1:97671', '1:103035', '1:97775', '1:103923', '1:103984', '1:104692', '1:104794', '1:73853', '1:74026', '1:74107', '1:74138', '1:96477', '1:96597', '1:96706', '1:96826', '1:97279', '1:96629', '1:98912', '1:93429', '1:93474', '1:93756', '1:96902', '1:97396', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EAC1941B-7FFC-E911-880C-0CC47AFF04B8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6ED558DA-D4FA-E911-8C22-14187734413C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/149CD343-22F3-E911-AB60-509A4C9F8A64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2CB7AD5-1CF8-E911-9A2B-C4544423E398.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7EC49D3B-40EF-E911-B70A-5065F381D2C1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E06BF93-D4F3-E911-BE1B-246E96D149B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CD26E41-F0F2-E911-987B-E4115BCE9004.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D628336E-680B-EA11-ABEF-0CC47A7C3450.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/52DEDB67-1508-EA11-A6C9-0CC47A78A42C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6A1D400-8EFE-E911-AEE5-0242AC1C0506.root']);