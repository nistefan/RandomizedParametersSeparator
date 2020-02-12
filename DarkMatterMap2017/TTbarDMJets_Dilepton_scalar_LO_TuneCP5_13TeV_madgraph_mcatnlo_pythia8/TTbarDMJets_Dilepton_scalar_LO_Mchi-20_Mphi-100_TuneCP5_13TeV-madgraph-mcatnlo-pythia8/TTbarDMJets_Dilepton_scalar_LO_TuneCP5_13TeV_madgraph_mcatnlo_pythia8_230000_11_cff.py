import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:54777', '1:54954', '1:55212', '1:55347', '1:55406', '1:58103', '1:57057', '1:57999', '1:70444', '1:70465', '1:61493', '1:62156', '1:62516', '1:84079', '1:84083', '1:82043', '1:82251', '1:82316', '1:82070', '1:82079', '1:82197', '1:82502', '1:82548', '1:85040', '1:2357', '1:8562', '1:8736', '1:12576', '1:7187', '1:10232', '1:18256', '1:50470', '1:49690', '1:49100', '1:50505', '1:51146', '1:82523', '1:82837', '1:84205', '1:88616', '1:91164', '1:93325', '1:94039', '1:87561', '1:85733', '1:82247', '1:83059', '1:83318', '1:83320', '1:87584', '1:87665', '1:87800', '1:92138', '1:93446', '1:98797', '1:7514', '1:8017', '1:8485', '1:8547', '1:9709', '1:10079', '1:14999', '1:12869', '1:14133', '1:17433', '1:41822', '1:41829', '1:41845', '1:49533', '1:86366', '1:88153', '1:92475', '1:91561', '1:94141', '1:95609', '1:103795', '1:12258', '1:12255', '1:66783', '1:68353', '1:69044', '1:70387', '1:71058', '1:72032', '1:72071', '1:72127', '1:72151', '1:74775', '1:75493', '1:75534', '1:77365', '1:74164', '1:79641', '1:79795', '1:94220', '1:92190', '1:92328', '1:1448', '1:1731', '1:1803', '1:664', '1:2962', '1:4518', '1:12897', '1:16749', '1:15700', '1:16359', '1:16436', '1:16889', '1:39557', '1:40503', '1:48372', '1:50712', '1:12457', '1:16260', '1:16770', '1:38277', '1:38587', '1:49907', '1:49704', '1:50236', '1:94149', '1:92667', '1:2272', '1:2375', '1:3028', '1:3038', '1:3117', '1:3125', '1:3155', '1:3185', '1:32174', '1:37011', '1:37863', '1:38770', '1:42191', '1:40205', '1:43999', '1:43054', '1:46487', '1:47366', '1:47684', '1:47783', '1:47784', '1:47826', '1:62538', '1:48029', '1:46039', '1:46439', '1:46479', '1:46586', '1:47721', '1:72245', '1:72818', '1:66053', '1:7376', '1:7655', '1:8384', '1:12308', '1:58470', '1:58959', '1:59996', '1:60795', '1:68701', '1:61097', '1:62721', '1:63297', '1:86319', '1:99472', '1:104741', '1:96734', '1:97261', '1:98400', '1:2416', '1:3301', '1:3399', '1:4203', '1:4301', '1:4084', '1:4335', '1:4358', '1:4364', '1:4373', '1:4432', '1:7540', '1:7639', '1:7702', '1:7767', '1:7778', '1:7954', '1:7962', '1:10753', '1:49581', '1:51127', '1:73669', '1:68448', '1:69093', '1:70116', '1:83324', '1:83855', '1:83858', '1:91873', '1:92108', '1:97699', '1:105396', '1:105405', '1:105419', '1:5628', '1:7417', '1:14849', '1:17250', '1:18068', '1:18072', '1:18155', '1:32905', '1:33457', '1:33809', '1:37408', '1:14143', '1:14186', '1:14197', '1:8974', '1:10328', '1:12486', '1:19492', '1:39602', '1:51920', '1:52493', '1:52874', '1:52923', '1:60513', '1:66144', '1:69241', '1:74462', '1:5203', '1:5427', '1:5703', '1:3410', '1:3433', '1:3561', '1:3574', '1:3607', '1:3641', '1:3867', '1:5145', '1:12753', '1:14043', '1:14084', '1:8514', '1:8573', '1:8727', '1:40185', '1:40385', '1:49160', '1:54324', '1:54525', '1:54487', '1:54529', '1:54585', '1:96771', '1:8717', '1:9110', '1:10255', '1:14013', '1:14027', '1:7365', '1:8839', '1:9033', '1:9233', '1:10861', '1:10882', '1:10977', '1:3606', '1:44435', '1:41794', '1:48289', '1:48798', '1:48756', '1:48864', '1:49699', '1:50011', '1:50432', '1:48396', '1:50574', '1:102723', '1:103105', '1:104500', '1:104799', '1:4582', '1:4592', '1:4739', '1:4745', '1:4848', '1:26105', '1:26219', '1:26846', '1:37047', '1:35076', '1:24057', '1:24316', '1:24684', '1:24750', '1:24808', '1:34114', '1:34147', '1:34398', '1:34634', '1:36125', '1:36223', '1:36250', '1:38444', '1:73744', '1:73917', '1:74168', '1:74207', '1:102405', '1:100982', '1:102004', '1:102187', '1:102223', '1:102280', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E2848B0E-44F2-E911-825D-509A4C9F8ADB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BEF0CDD4-E4F6-E911-83C1-0CC47A0AD6FC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/16FBEA03-EAF2-E911-B29A-44A842BECCB1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F83A579D-8B01-EA11-AABA-00259073E45A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/20F66F39-4203-EA11-A2F6-405CFDFF481B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4AA2791D-9EF2-E911-8C38-3417EBE74303.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96CDDC18-A20E-EA11-A3B2-00266CFFBF88.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/982A8027-7FEE-E911-B6C3-089E0158CD57.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4EE87D2-0B09-EA11-92AB-00266CF3E174.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C5B6E03-5CFF-E911-B90B-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D26BC5FF-970A-EA11-95B5-0CC47A4D7666.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AA873AAA-B402-EA11-9A84-0025905C9742.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B20562A7-710E-EA11-8BD4-0CC47A78A478.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4A15B08-AFEE-E911-9943-8CDCD4A99E08.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/529ABEDC-6210-EA11-9BFF-506B4BF38280.root']);