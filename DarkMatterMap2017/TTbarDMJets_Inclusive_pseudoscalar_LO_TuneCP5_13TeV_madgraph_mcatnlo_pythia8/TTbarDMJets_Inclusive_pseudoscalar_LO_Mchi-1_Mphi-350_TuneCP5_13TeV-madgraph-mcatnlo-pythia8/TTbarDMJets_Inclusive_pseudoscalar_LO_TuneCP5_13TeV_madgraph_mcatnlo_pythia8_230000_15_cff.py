import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:18817', '1:22443', '1:11052', '1:11100', '1:11406', '1:15724', '1:20892', '1:20576', '1:20583', '1:21605', '1:21699', '1:21798', '1:21893', '1:23908', '1:24301', '1:24306', '1:28299', '1:28546', '1:28036', '1:28212', '1:28380', '1:28584', '1:28820', '1:41385', '1:41405', '1:41516', '1:44169', '1:54625', '1:55051', '1:49985', '1:56729', '1:57807', '1:59661', '1:72326', '1:72845', '1:80212', '1:72715', '1:75465', '1:75843', '1:76445', '1:76560', '1:80706', '1:4652', '1:4662', '1:6735', '1:6789', '1:56115', '1:56198', '1:56513', '1:58569', '1:55198', '1:55336', '1:55727', '1:56682', '1:56984', '1:57945', '1:58041', '1:58053', '1:58184', '1:58185', '1:14121', '1:14351', '1:14407', '1:14444', '1:22377', '1:27274', '1:27799', '1:28493', '1:27685', '1:27809', '1:3327', '1:7432', '1:9310', '1:9391', '1:12175', '1:6277', '1:9454', '1:10912', '1:15986', '1:16140', '1:13262', '1:16379', '1:10310', '1:26793', '1:31039', '1:10730', '1:15612', '1:16636', '1:22610', '1:27535', '1:40007', '1:75901', '1:73340', '1:90782', '1:17552', '1:18070', '1:9841', '1:10568', '1:11174', '1:19985', '1:16409', '1:16454', '1:16506', '1:21058', '1:21060', '1:21085', '1:21087', '1:21256', '1:21296', '1:32282', '1:32558', '1:42120', '1:42251', '1:42874', '1:43627', '1:43696', '1:43710', '1:45134', '1:45471', '1:56773', '1:56180', '1:56139', '1:56618', '1:56683', '1:56733', '1:58386', '1:14386', '1:14637', '1:14865', '1:67229', '1:67266', '1:79655', '1:81177', '1:84212', '1:66646', '1:66679', '1:66750', '1:66905', '1:66944', '1:67076', '1:86708', '1:87125', '1:87146', '1:93569', '1:93703', '1:95952', '1:96152', '1:106108', '1:104768', '1:95736', '1:95967', '1:54452', '1:54556', '1:96500', '1:96509', '1:96745', '1:96882', '1:103162', '1:103824', '1:105410', '1:102398', '1:102649', '1:102874', '1:73718', '1:73838', '1:73946', '1:73970', '1:74007', '1:74143', '1:88000', '1:96608', '1:97091', '1:96403', '1:98100', '1:103064', '1:93132', '1:93244', '1:93390', '1:93510', '1:93715', '1:95902', '1:97244', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EAC1941B-7FFC-E911-880C-0CC47AFF04B8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6ED558DA-D4FA-E911-8C22-14187734413C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/149CD343-22F3-E911-AB60-509A4C9F8A64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2CB7AD5-1CF8-E911-9A2B-C4544423E398.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7EC49D3B-40EF-E911-B70A-5065F381D2C1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E06BF93-D4F3-E911-BE1B-246E96D149B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CD26E41-F0F2-E911-987B-E4115BCE9004.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D628336E-680B-EA11-ABEF-0CC47A7C3450.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/52DEDB67-1508-EA11-A6C9-0CC47A78A42C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6A1D400-8EFE-E911-AEE5-0242AC1C0506.root']);