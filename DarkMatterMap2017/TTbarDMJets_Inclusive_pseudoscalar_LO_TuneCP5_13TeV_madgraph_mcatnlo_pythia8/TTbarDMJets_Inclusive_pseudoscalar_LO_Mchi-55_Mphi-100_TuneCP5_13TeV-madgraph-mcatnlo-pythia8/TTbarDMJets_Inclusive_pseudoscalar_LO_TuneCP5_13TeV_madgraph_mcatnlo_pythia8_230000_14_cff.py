import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:97109', '1:82490', '1:103901', '1:105578', '1:106281', '1:101158', '1:101244', '1:101281', '1:98288', '1:103666', '1:101080', '1:101406', '1:102647', '1:102837', '1:104942', '1:101878', '1:102802', '1:101221', '1:8813', '1:10436', '1:23040', '1:28944', '1:39062', '1:49436', '1:13380', '1:13487', '1:14638', '1:14402', '1:14503', '1:15001', '1:51742', '1:52246', '1:55297', '1:21006', '1:15125', '1:15453', '1:15771', '1:15795', '1:17304', '1:17320', '1:17483', '1:19103', '1:19651', '1:27289', '1:52395', '1:25495', '1:42341', '1:42356', '1:42468', '1:42472', '1:56838', '1:66131', '1:71399', '1:70327', '1:79137', '1:79603', '1:70795', '1:54669', '1:88858', '1:86419', '1:86428', '1:86825', '1:89145', '1:92818', '1:87985', '1:86334', '1:94505', '1:92226', '1:93884', '1:84628', '1:85228', '1:101706', '1:106196', '1:101361', '1:102629', '1:7997', '1:8099', '1:19079', '1:52979', '1:53559', '1:53637', '1:53720', '1:54298', '1:59032', '1:59089', '1:59245', '1:7671', '1:18214', '1:32300', '1:40984', '1:41511', '1:41527', '1:41543', '1:41605', '1:32855', '1:8751', '1:8972', '1:9267', '1:9095', '1:9108', '1:27503', '1:27576', '1:31072', '1:3963', '1:9297', '1:16362', '1:4101', '1:17654', '1:30774', '1:70432', '1:79904', '1:80052', '1:80934', '1:30266', '1:52735', '1:51426', '1:54189', '1:54406', '1:45088', '1:60805', '1:73214', '1:62372', '1:70672', '1:70722', '1:70811', '1:77061', '1:97668', '1:102834', '1:98182', '1:98692', '1:24475', '1:24654', '1:24760', '1:82581', '1:82691', '1:86296', '1:83287', '1:86966', '1:65597', '1:70003', '1:84026', '1:85463', '1:79478', '1:6494', '1:6514', '1:6282', '1:6538', '1:40555', '1:40670', '1:40768', '1:52061', '1:52420', '1:58638', '1:58762', '1:58816', '1:27495', '1:83346', '1:83798', '1:48363', '1:48868', '1:44402', '1:44921', '1:44298', '1:44338', '1:47795', '1:15752', '1:21784', '1:31080', '1:83214', '1:105468', '1:79651', '1:103336', '1:106439', '1:106277', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6A721CBE-4B07-EA11-9750-0CC47A4D7646.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCF6B8AB-E003-EA11-AAE8-44A842BE8F7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9EAE1061-30F8-E911-B2D5-AC1F6B0F676C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/86727FE6-AF0A-EA11-B38D-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2A16734-8607-EA11-A7C2-0025905A6060.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/723E26E0-88FC-E911-A84F-0CC47AFCC666.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/643155F4-E80A-EA11-BD55-0CC47A7C3636.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC1243A5-AA0A-EA11-A2C9-0CC47A7C347A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24362999-4EFE-E911-BFEB-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1207CE62-4EF9-E911-85E0-C4346BC85718.root']);