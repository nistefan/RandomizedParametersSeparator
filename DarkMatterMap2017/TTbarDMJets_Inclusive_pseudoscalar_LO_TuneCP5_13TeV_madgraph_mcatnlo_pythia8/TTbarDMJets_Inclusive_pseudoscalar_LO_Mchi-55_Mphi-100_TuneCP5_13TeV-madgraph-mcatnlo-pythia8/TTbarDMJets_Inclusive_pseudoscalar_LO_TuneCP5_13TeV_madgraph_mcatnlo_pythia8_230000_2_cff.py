import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:39502', '1:39107', '1:39130', '1:39183', '1:39226', '1:39302', '1:46369', '1:46564', '1:46600', '1:46811', '1:90187', '1:90546', '1:42321', '1:43219', '1:43511', '1:45670', '1:45972', '1:49756', '1:103140', '1:105172', '1:105527', '1:2036', '1:2302', '1:2737', '1:3477', '1:5654', '1:5774', '1:5796', '1:5903', '1:4683', '1:4743', '1:5001', '1:5163', '1:4775', '1:4816', '1:5062', '1:5196', '1:5322', '1:5432', '1:5515', '1:10475', '1:9258', '1:9538', '1:13972', '1:10565', '1:30253', '1:32414', '1:51344', '1:51352', '1:51362', '1:51395', '1:39485', '1:42212', '1:51493', '1:24231', '1:24893', '1:31790', '1:43380', '1:43578', '1:55825', '1:55876', '1:56244', '1:56655', '1:30451', '1:30591', '1:19697', '1:20005', '1:20095', '1:19870', '1:19906', '1:19947', '1:24096', '1:70105', '1:66795', '1:73955', '1:74214', '1:74281', '1:85033', '1:85475', '1:44125', '1:44413', '1:44569', '1:44635', '1:44678', '1:44483', '1:44550', '1:44570', '1:89737', '1:83255', '1:83691', '1:83893', '1:85062', '1:85702', '1:90112', '1:101627', '1:5170', '1:2932', '1:5190', '1:8275', '1:8706', '1:31107', '1:31621', '1:7290', '1:13572', '1:15148', '1:15999', '1:13361', '1:13409', '1:21829', '1:45957', '1:57055', '1:17321', '1:19116', '1:19910', '1:17414', '1:54002', '1:48905', '1:49178', '1:49711', '1:54730', '1:56218', '1:56976', '1:55555', '1:66568', '1:74147', '1:75537', '1:41814', '1:52261', '1:60299', '1:61269', '1:57100', '1:49979', '1:51009', '1:51017', '1:51753', '1:55082', '1:55246', '1:55463', '1:55526', '1:52961', '1:2216', '1:8795', '1:6594', '1:8227', '1:4110', '1:14106', '1:106006', '1:58308', '1:59934', '1:58802', '1:59566', '1:87546', '1:64467', '1:71175', '1:74125', '1:64954', '1:80004', '1:82374', '1:84042', '1:88350', '1:83046', '1:85328', '1:84820', '1:11353', '1:11991', '1:56174', '1:65045', '1:74938', '1:75702', '1:75833', '1:64580', '1:62106', '1:5692', '1:6988', '1:11957', '1:11650', '1:39928', '1:45450', '1:48024', '1:41572', '1:49940', '1:79206', '1:78873', '1:1570', '1:8320', '1:13267', '1:41985', '1:58906', '1:59816', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AAB00DE4-97F3-E911-A3C8-509A4C9EF8EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D28BE09F-34F2-E911-BBB7-509A4C9EF924.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8145C07-FDF2-E911-A902-509A4C9F8ADB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24CF0859-1FF5-E911-84A0-441EA1616D3A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8ABA5532-F3F4-E911-A0DF-00215AAA5746.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EC263BA-D9F2-E911-8E00-1866DA7F93EB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78B70150-BC12-EA11-8D6F-0CC47AFF23CE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FA6B6FC8-18F4-E911-A834-00259073E428.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C421938-2AF3-E911-9857-1866DA7F8ED8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/224CE38B-CBF2-E911-A69D-F01FAFE5F67D.root']);