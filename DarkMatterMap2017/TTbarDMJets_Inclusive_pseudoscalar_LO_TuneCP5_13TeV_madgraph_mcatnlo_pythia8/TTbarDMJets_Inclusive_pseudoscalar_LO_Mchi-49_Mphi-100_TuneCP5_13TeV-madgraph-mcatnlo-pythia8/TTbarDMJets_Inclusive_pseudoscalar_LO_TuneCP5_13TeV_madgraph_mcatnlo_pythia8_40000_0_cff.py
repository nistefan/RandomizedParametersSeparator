import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:130', '1:355', '1:381', '1:35431', '1:36533', '1:36864', '1:36936', '1:37789', '1:100846', '1:35522', '1:35704', '1:35560', '1:33566', '1:33548', '1:33703', '1:33708', '1:68270', '1:68362', '1:68333', '1:68421', '1:37494', '1:37504', '1:37615', '1:37772', '1:34441', '1:34744', '1:36165', '1:68397', '1:50562', '1:38989', '1:50588', '1:50607', '1:50629', '1:50682', '1:37', '1:38050', '1:38653', '1:68045', '1:38147', '1:33718', '1:38420', '1:38421', '1:33732', '1:33736', '1:33746', '1:33627', '1:33792', '1:34160', '1:34313', '1:34418', '1:34438', '1:34534', '1:34572', '1:34711', '1:34732', '1:37988', '1:63700', '1:69147', '1:69155', '1:99342', '1:99350', '1:99374', '1:100278', '1:100314', '1:813', '1:960', '1:987', '1:35878', '1:37509', '1:36036', '1:37520', '1:37513', '1:63767', '1:63807', '1:63981', '1:69563', '1:99081', '1:100010', '1:100134', '1:635', '1:50252', '1:63351', '1:34258', '1:34281', '1:38101', '1:50070', '1:63897', '1:99043', '1:99246', '1:69775', '1:69323', '1:100174', '1:99193', '1:33950', '1:36041', '1:37470', '1:37778', '1:33040', '1:33294', '1:33297', '1:69561', '1:99783', '1:36762', '1:36765', '1:36787', '1:36894', '1:36896', '1:50122', '1:50300', '1:50511', '1:50216', '1:69734', '1:99256', '1:57', '1:33961', '1:38061', '1:38695', '1:37440', '1:68306', '1:50658', '1:50580', '1:63399', '1:99505', '1:99703', '1:99865', '1:99447', '1:99667', '1:84', '1:302', '1:322', '1:333', '1:430', '1:34220', '1:34221', '1:38066', '1:38684', '1:100055', '1:100898', '1:100720', '1:37304', '1:37637', '1:36006', '1:36021', '1:34693', '1:34854', '1:38262', '1:38271', '1:33681', '1:34486', '1:34494', '1:34849', '1:36620', '1:100554', '1:36605', '1:68127', '1:68520', '1:68530', '1:68661', '1:63196', '1:69589', '1:35199', '1:37828', '1:69546', '1:37869', '1:37902', '1:38281', '1:35858', '1:63745', '1:69660', '1:33005', '1:34407', '1:34386', '1:33069', '1:34058', '1:38542', '1:63783', '1:63790', '1:63818', '1:100099', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/ACA45E67-4710-EA11-993D-AC1F6B1AF142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/EE07DEB0-7311-EA11-88E2-7CD30ACE1479.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DEA7093A-5810-EA11-9AB2-0CC47AFF0454.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/62D36710-EC10-EA11-A1B6-98039B3B003A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/46F6364E-2311-EA11-A748-0CC47A1DF800.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/8CF037CB-4710-EA11-80A5-0CC47A5FC281.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/88FDBA27-9A11-EA11-B345-A0369FC524AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/B0B5A181-2812-EA11-B322-B083FED1321B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/B6F2C869-7914-EA11-8091-F01FAFD69D00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/62A1C426-9D14-EA11-86E0-1418774A24C6.root']);