import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:32456', '1:32602', '1:32610', '1:32813', '1:32934', '1:70114', '1:81851', '1:82199', '1:84261', '1:84269', '1:85736', '1:90146', '1:90513', '1:90834', '1:91045', '1:91627', '1:91732', '1:91830', '1:91969', '1:92241', '1:82924', '1:84349', '1:84456', '1:83412', '1:83856', '1:84060', '1:83940', '1:86475', '1:87054', '1:92661', '1:92697', '1:93681', '1:94147', '1:94267', '1:94316', '1:94511', '1:95241', '1:16623', '1:16739', '1:16873', '1:16989', '1:22781', '1:22783', '1:22857', '1:22862', '1:22907', '1:27396', '1:27452', '1:49920', '1:102170', '1:54015', '1:54229', '1:54395', '1:54543', '1:54676', '1:78432', '1:78596', '1:85308', '1:85408', '1:88893', '1:89109', '1:18550', '1:18621', '1:18671', '1:18705', '1:18752', '1:18864', '1:22512', '1:22595', '1:22611', '1:39423', '1:39802', '1:39821', '1:39867', '1:39872', '1:42055', '1:42138', '1:43216', '1:44008', '1:43648', '1:76240', '1:76170', '1:76183', '1:76431', '1:6319', '1:16110', '1:89898', '1:70370', '1:86649', '1:84424', '1:86024', '1:89096', '1:89289', '1:46841', '1:48223', '1:48650', '1:51043', '1:51251', '1:47372', '1:47505', '1:47526', '1:47647', '1:88371', '1:88425', '1:101778', '1:101951', '1:102228', '1:102739', '1:47803', '1:106350', '1:95857', '1:95997', '1:97262', '1:98067', '1:98143', '1:103256', '1:103312', '1:103361', '1:103459', '1:96493', '1:56455', '1:56519', '1:51018', '1:81955', '1:19581', '1:28513', '1:44772', '1:78607', '1:79443', '1:93582', '1:29671', '1:29800', '1:30025', '1:30688', '1:47619', '1:93485', '1:82628', '1:71004', '1:104624', '1:70001', '1:73186', '1:73265', '1:77187', '1:87618', '1:88983', '1:25523', '1:29704', '1:32082', '1:9463', '1:9942', '1:65505', '1:74343', '1:14262', '1:16408', '1:23810', '1:24455', '1:24489', '1:13931', '1:13933', '1:14166', '1:14296', '1:16327', '1:16844', '1:24398', '1:26290', '1:66328', '1:81578', '1:52972', '1:53104', '1:53348', '1:53454', '1:53525', '1:64682', '1:64833', '1:65135', '1:65248', '1:65261', '1:1276', '1:1503', '1:1888', '1:2064', '1:7751', '1:8300', '1:10275', '1:11648', '1:24507', '1:24621', '1:24640', '1:5317', '1:5393', '1:5762', '1:5952', '1:25989', '1:23783', '1:27544', '1:27651', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/509597B0-AEFB-E911-878E-002590DE3A92.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90776FDE-BDFB-E911-84D1-40F2E9C6ADBA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F6B93E96-C5FB-E911-9974-3417EBE7047A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BA100FA2-4EFE-E911-96A3-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F43443B4-ECFC-E911-BEB6-24BE05C4D8F1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BAA9281E-48FE-E911-B284-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/82DC5317-C9FE-E911-A8D4-0030487BB52E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A904563-4D00-EA11-8187-002481CFE1EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B29D7EA4-74FF-E911-97CA-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/56EB785D-ADFE-E911-8744-0CC47A5FC281.root']);