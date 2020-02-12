import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:21211', '1:21566', '1:22256', '1:26700', '1:22683', '1:20288', '1:21384', '1:21764', '1:22972', '1:27842', '1:52621', '1:76442', '1:69155', '1:69222', '1:69329', '1:55650', '1:55945', '1:64949', '1:54236', '1:50614', '1:57679', '1:60174', '1:62305', '1:67042', '1:69201', '1:67968', '1:78414', '1:96001', '1:96579', '1:97619', '1:101464', '1:99647', '1:99727', '1:100679', '1:26348', '1:27361', '1:35194', '1:35622', '1:37310', '1:68795', '1:69263', '1:60517', '1:61373', '1:63055', '1:10862', '1:13091', '1:13422', '1:13626', '1:14287', '1:49413', '1:40279', '1:46664', '1:51120', '1:51804', '1:23020', '1:31788', '1:34220', '1:34844', '1:34921', '1:35371', '1:35395', '1:37210', '1:28231', '1:28249', '1:28418', '1:28484', '1:59988', '1:61304', '1:63711', '1:63934', '1:59753', '1:61957', '1:71204', '1:71172', '1:71779', '1:77399', '1:55805', '1:74201', '1:74385', '1:74447', '1:74521', '1:75802', '1:95617', '1:95725', '1:95817', '1:97608', '1:61046', '1:60969', '1:61030', '1:61371', '1:64051', '1:64256', '1:64309', '1:64362', '1:67103', '1:99320', '1:98282', '1:25962', '1:26242', '1:26559', '1:29727', '1:36714', '1:38064', '1:38208', '1:26130', '1:26688', '1:32172', '1:38437', '1:101991', '1:102228', '1:102284', '1:99993', '1:80099', '1:81572', '1:91368', '1:86550', '1:89773', '1:90799', '1:23422', '1:16923', '1:49810', '1:50106', '1:62522', '1:62548', '1:80827', '1:85383', '1:85345', '1:85348', '1:85393', '1:85478', '1:85954', '1:86170', '1:27990', '1:28560', '1:28762', '1:40935', '1:72834', '1:68521', '1:73231', '1:73270', '1:75498', '1:76479', '1:86838', '1:86943', '1:74075', '1:74352', '1:74605', '1:74767', '1:74855', '1:74998', '1:77833', '1:79166', '1:79289', '1:79438', '1:79470', '1:79675', '1:79682', '1:79619', '1:79895', '1:75104', '1:76668', '1:76856', '1:77553', '1:77770', '1:78648', '1:88608', '1:90139', '1:86451', '1:86504', '1:86966', '1:87276', '1:2665', '1:2663', '1:2696', '1:2801', '1:5902', '1:5928', '1:5932', '1:7183', '1:16493', '1:16651', '1:49882', '1:50201', '1:50550', '1:51464', '1:19801', '1:19131', '1:63004', '1:51570', '1:53555', '1:54021', '1:54050', '1:54107', '1:53516', '1:54137', '1:52826', '1:53129', '1:53270', '1:56715', '1:67086', '1:67105', '1:67194', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/183425A0-2CF9-E911-8A59-0CC47AC17502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/14013B83-ED0C-EA11-A969-0CC47A4C8E16.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D8BE5B85-CD00-EA11-8D89-008CFA197DDC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8EA49950-280B-EA11-8D88-0CC47A7C353E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C80BC002-AE01-EA11-8935-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94EED3C0-3913-EA11-9D36-003048F1C4AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CC49EA7-DAFA-E911-B4D9-549F3525C318.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7ED89422-6000-EA11-91BA-509A4C9EF8FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02A19D30-BF01-EA11-8C20-0CC47AF973C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/986C80F8-D001-EA11-B39E-509A4C9F8A64.root']);