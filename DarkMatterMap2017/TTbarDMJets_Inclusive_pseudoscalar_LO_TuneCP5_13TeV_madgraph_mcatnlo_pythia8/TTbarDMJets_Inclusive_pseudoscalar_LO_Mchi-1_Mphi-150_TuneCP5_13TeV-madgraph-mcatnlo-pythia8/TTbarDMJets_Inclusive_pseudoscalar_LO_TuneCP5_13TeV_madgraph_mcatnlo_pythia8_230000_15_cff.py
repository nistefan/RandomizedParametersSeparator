import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:22361', '1:22871', '1:22960', '1:27029', '1:8791', '1:11084', '1:11122', '1:11336', '1:11804', '1:15764', '1:20620', '1:20774', '1:20685', '1:21126', '1:21496', '1:21936', '1:51586', '1:24165', '1:24307', '1:24369', '1:28554', '1:28431', '1:28803', '1:27640', '1:27871', '1:27900', '1:28449', '1:28462', '1:28863', '1:32559', '1:32898', '1:41241', '1:41282', '1:41332', '1:41489', '1:55304', '1:49840', '1:56990', '1:58314', '1:59695', '1:71224', '1:73565', '1:79700', '1:79749', '1:73653', '1:78519', '1:80086', '1:74580', '1:5087', '1:4561', '1:4978', '1:5158', '1:58378', '1:70129', '1:70291', '1:70373', '1:98542', '1:56267', '1:58312', '1:58424', '1:55158', '1:55258', '1:55376', '1:55566', '1:55572', '1:55623', '1:56982', '1:58207', '1:96223', '1:96928', '1:97999', '1:13974', '1:14094', '1:14127', '1:14283', '1:22627', '1:22741', '1:22806', '1:24167', '1:27371', '1:27556', '1:28574', '1:12457', '1:3465', '1:4317', '1:12233', '1:15559', '1:12796', '1:44480', '1:47017', '1:17747', '1:23402', '1:17525', '1:26028', '1:27932', '1:26779', '1:28289', '1:28427', '1:40317', '1:44109', '1:45872', '1:80557', '1:81176', '1:81322', '1:61668', '1:94449', '1:19639', '1:25411', '1:25929', '1:27063', '1:10024', '1:11651', '1:11662', '1:19940', '1:24402', '1:20596', '1:20645', '1:15317', '1:15440', '1:16192', '1:16225', '1:15967', '1:16093', '1:16145', '1:16430', '1:21130', '1:21173', '1:21188', '1:21212', '1:21351', '1:21352', '1:32227', '1:32289', '1:32540', '1:42672', '1:43643', '1:43686', '1:43745', '1:45123', '1:45307', '1:56333', '1:56658', '1:56722', '1:56790', '1:56457', '1:55931', '1:56116', '1:56365', '1:14940', '1:15085', '1:73643', '1:87843', '1:79248', '1:66501', '1:66945', '1:101895', '1:86500', '1:87192', '1:96026', '1:96123', '1:96183', '1:95830', '1:44781', '1:44797', '1:45033', '1:45226', '1:54485', '1:54565', '1:97095', '1:97319', '1:97328', '1:105034', '1:103859', '1:103999', '1:101476', '1:104276', '1:73851', '1:73905', '1:74165', '1:86268', '1:86769', '1:86938', '1:87439', '1:96583', '1:97271', '1:97330', '1:96227', '1:96711', '1:98594', '1:93223', '1:93472', '1:93587', '1:93629', '1:93709', '1:93943', '1:95710', '1:97309', '1:97375', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EAC1941B-7FFC-E911-880C-0CC47AFF04B8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6ED558DA-D4FA-E911-8C22-14187734413C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/149CD343-22F3-E911-AB60-509A4C9F8A64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2CB7AD5-1CF8-E911-9A2B-C4544423E398.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7EC49D3B-40EF-E911-B70A-5065F381D2C1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E06BF93-D4F3-E911-BE1B-246E96D149B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CD26E41-F0F2-E911-987B-E4115BCE9004.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D628336E-680B-EA11-ABEF-0CC47A7C3450.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/52DEDB67-1508-EA11-A6C9-0CC47A78A42C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6A1D400-8EFE-E911-AEE5-0242AC1C0506.root']);