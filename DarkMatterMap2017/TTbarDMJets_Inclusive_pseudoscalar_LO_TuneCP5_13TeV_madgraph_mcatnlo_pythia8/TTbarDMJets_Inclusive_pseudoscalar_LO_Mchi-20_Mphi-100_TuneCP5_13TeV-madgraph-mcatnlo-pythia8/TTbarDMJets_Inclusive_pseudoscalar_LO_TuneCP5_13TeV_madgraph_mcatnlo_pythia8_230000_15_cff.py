import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:18535', '1:18706', '1:11257', '1:11335', '1:15878', '1:20785', '1:20924', '1:20782', '1:21854', '1:21872', '1:21887', '1:21905', '1:21888', '1:24017', '1:24184', '1:24312', '1:24411', '1:28680', '1:27749', '1:28980', '1:28222', '1:28788', '1:32363', '1:41263', '1:41324', '1:41326', '1:41389', '1:41440', '1:41488', '1:41508', '1:51909', '1:53086', '1:55720', '1:55781', '1:56026', '1:52786', '1:55375', '1:65702', '1:66220', '1:78730', '1:80933', '1:80076', '1:4765', '1:5090', '1:6432', '1:70146', '1:65652', '1:98567', '1:58689', '1:59049', '1:55199', '1:55484', '1:55534', '1:56819', '1:57645', '1:58072', '1:96280', '1:96464', '1:98583', '1:14048', '1:14291', '1:14298', '1:14545', '1:28483', '1:27419', '1:3277', '1:10117', '1:10879', '1:9002', '1:14261', '1:15177', '1:16369', '1:23409', '1:27536', '1:39689', '1:40126', '1:39902', '1:45901', '1:80030', '1:81467', '1:81865', '1:80750', '1:17612', '1:17637', '1:27045', '1:9816', '1:10462', '1:10667', '1:10865', '1:10954', '1:11263', '1:20378', '1:15908', '1:21375', '1:21054', '1:21119', '1:21222', '1:21314', '1:21337', '1:21353', '1:31075', '1:32194', '1:32203', '1:32320', '1:32734', '1:42163', '1:43319', '1:43490', '1:43622', '1:43620', '1:43830', '1:43831', '1:44331', '1:44891', '1:44916', '1:45010', '1:45030', '1:45180', '1:45239', '1:45293', '1:45348', '1:45379', '1:56332', '1:51192', '1:55840', '1:55904', '1:56073', '1:56245', '1:15348', '1:14399', '1:14458', '1:14872', '1:60911', '1:73920', '1:66787', '1:86048', '1:66628', '1:66744', '1:66831', '1:66959', '1:67099', '1:86580', '1:86643', '1:86930', '1:87207', '1:87246', '1:96136', '1:94812', '1:95444', '1:44498', '1:44920', '1:45840', '1:54239', '1:54355', '1:101512', '1:96935', '1:97159', '1:98434', '1:103800', '1:103905', '1:103911', '1:103837', '1:103922', '1:105014', '1:102642', '1:73992', '1:73947', '1:74164', '1:86241', '1:86646', '1:86768', '1:87990', '1:96654', '1:95434', '1:96072', '1:103120', '1:93620', '1:94037', '1:96271', '1:97431', '1:97439', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EAC1941B-7FFC-E911-880C-0CC47AFF04B8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6ED558DA-D4FA-E911-8C22-14187734413C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/149CD343-22F3-E911-AB60-509A4C9F8A64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2CB7AD5-1CF8-E911-9A2B-C4544423E398.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7EC49D3B-40EF-E911-B70A-5065F381D2C1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E06BF93-D4F3-E911-BE1B-246E96D149B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CD26E41-F0F2-E911-987B-E4115BCE9004.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D628336E-680B-EA11-ABEF-0CC47A7C3450.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/52DEDB67-1508-EA11-A6C9-0CC47A78A42C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6A1D400-8EFE-E911-AEE5-0242AC1C0506.root']);