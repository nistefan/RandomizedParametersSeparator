import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:32983', '1:39487', '1:39099', '1:39126', '1:39264', '1:46700', '1:90569', '1:43002', '1:43364', '1:43677', '1:45650', '1:49019', '1:49365', '1:103392', '1:95097', '1:96259', '1:96728', '1:96742', '1:97272', '1:105064', '1:105044', '1:105123', '1:103038', '1:2271', '1:2416', '1:3725', '1:3733', '1:3845', '1:10567', '1:14595', '1:15556', '1:4628', '1:4812', '1:10372', '1:9198', '1:9388', '1:10190', '1:41929', '1:51220', '1:39116', '1:39117', '1:39165', '1:39499', '1:49495', '1:51033', '1:51119', '1:51364', '1:25030', '1:31767', '1:31828', '1:41979', '1:42247', '1:56554', '1:30584', '1:55384', '1:56504', '1:19689', '1:19643', '1:73943', '1:74252', '1:74332', '1:74381', '1:74391', '1:85168', '1:85376', '1:85419', '1:44158', '1:44572', '1:44587', '1:82742', '1:83341', '1:83650', '1:83996', '1:84955', '1:85176', '1:85620', '1:85661', '1:101607', '1:101871', '1:101986', '1:2043', '1:2454', '1:2750', '1:2803', '1:4363', '1:5522', '1:5715', '1:7938', '1:13220', '1:2710', '1:2762', '1:7176', '1:7030', '1:4852', '1:15525', '1:13069', '1:13180', '1:21116', '1:31198', '1:60042', '1:60872', '1:18552', '1:19351', '1:19338', '1:26255', '1:27339', '1:53804', '1:56770', '1:66061', '1:71567', '1:49457', '1:46248', '1:46621', '1:46860', '1:59037', '1:53646', '1:71048', '1:78167', '1:49858', '1:51050', '1:51577', '1:51804', '1:55136', '1:55247', '1:55485', '1:55488', '1:55748', '1:53171', '1:2312', '1:6019', '1:7193', '1:9326', '1:10137', '1:10396', '1:10872', '1:14141', '1:14873', '1:16035', '1:16701', '1:15517', '1:5206', '1:45185', '1:30936', '1:41199', '1:61657', '1:64458', '1:71650', '1:73062', '1:77840', '1:79889', '1:77810', '1:6930', '1:11175', '1:11808', '1:9384', '1:13705', '1:14649', '1:67864', '1:71786', '1:71810', '1:75313', '1:58659', '1:1201', '1:10721', '1:16098', '1:40449', '1:49406', '1:55930', '1:58661', '1:49471', '1:48525', '1:73765', '1:1458', '1:1720', '1:6302', '1:20692', '1:24326', '1:64872', '1:62720', '1:61228', '1:62511', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AAB00DE4-97F3-E911-A3C8-509A4C9EF8EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D28BE09F-34F2-E911-BBB7-509A4C9EF924.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8145C07-FDF2-E911-A902-509A4C9F8ADB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24CF0859-1FF5-E911-84A0-441EA1616D3A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8ABA5532-F3F4-E911-A0DF-00215AAA5746.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EC263BA-D9F2-E911-8E00-1866DA7F93EB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78B70150-BC12-EA11-8D6F-0CC47AFF23CE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FA6B6FC8-18F4-E911-A834-00259073E428.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C421938-2AF3-E911-9857-1866DA7F8ED8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/224CE38B-CBF2-E911-A69D-F01FAFE5F67D.root']);