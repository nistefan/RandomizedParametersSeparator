import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:133', '1:356', '1:341', '1:357', '1:34613', '1:36531', '1:36858', '1:35693', '1:33790', '1:33399', '1:33453', '1:33471', '1:33558', '1:33574', '1:33580', '1:33516', '1:33526', '1:34945', '1:68369', '1:68373', '1:68376', '1:68334', '1:34145', '1:37618', '1:34437', '1:38912', '1:36860', '1:34742', '1:34782', '1:34792', '1:36173', '1:36245', '1:36272', '1:36275', '1:38949', '1:68100', '1:38496', '1:38895', '1:68060', '1:50577', '1:50614', '1:50769', '1:50827', '1:50926', '1:985', '1:50079', '1:38148', '1:37790', '1:33998', '1:34316', '1:38308', '1:33700', '1:34411', '1:37644', '1:63662', '1:63668', '1:63697', '1:63986', '1:63990', '1:69141', '1:69145', '1:69154', '1:69209', '1:99233', '1:99348', '1:99381', '1:99389', '1:99407', '1:99128', '1:99267', '1:99360', '1:99339', '1:99303', '1:99429', '1:99443', '1:99306', '1:99399', '1:99413', '1:100326', '1:35138', '1:35500', '1:35917', '1:37506', '1:33933', '1:36051', '1:36054', '1:37517', '1:37530', '1:37533', '1:99088', '1:99638', '1:34254', '1:36452', '1:33935', '1:36587', '1:50048', '1:34890', '1:38645', '1:68284', '1:50046', '1:63754', '1:69791', '1:63712', '1:63715', '1:63948', '1:69952', '1:100060', '1:290', '1:34021', '1:36044', '1:33100', '1:33285', '1:33305', '1:33430', '1:100257', '1:50424', '1:50615', '1:50724', '1:50297', '1:34994', '1:34885', '1:50630', '1:50684', '1:50842', '1:50865', '1:50599', '1:63452', '1:99699', '1:85', '1:401', '1:34231', '1:100271', '1:100607', '1:34019', '1:34253', '1:35866', '1:100917', '1:100969', '1:33011', '1:33017', '1:37850', '1:37874', '1:34049', '1:37558', '1:34472', '1:34468', '1:36071', '1:100529', '1:38439', '1:38729', '1:38775', '1:68138', '1:68190', '1:68205', '1:69088', '1:35228', '1:35741', '1:33881', '1:33887', '1:34975', '1:34979', '1:36664', '1:37298', '1:33646', '1:33693', '1:34045', '1:37363', '1:34057', '1:69692', '1:33592', '1:34334', '1:34381', '1:63194', '1:63542', '1:50247', '1:63562', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/ACA45E67-4710-EA11-993D-AC1F6B1AF142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/EE07DEB0-7311-EA11-88E2-7CD30ACE1479.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DEA7093A-5810-EA11-9AB2-0CC47AFF0454.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/62D36710-EC10-EA11-A1B6-98039B3B003A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/46F6364E-2311-EA11-A748-0CC47A1DF800.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/8CF037CB-4710-EA11-80A5-0CC47A5FC281.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/88FDBA27-9A11-EA11-B345-A0369FC524AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/B0B5A181-2812-EA11-B322-B083FED1321B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/B6F2C869-7914-EA11-8091-F01FAFD69D00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/62A1C426-9D14-EA11-86E0-1418774A24C6.root']);