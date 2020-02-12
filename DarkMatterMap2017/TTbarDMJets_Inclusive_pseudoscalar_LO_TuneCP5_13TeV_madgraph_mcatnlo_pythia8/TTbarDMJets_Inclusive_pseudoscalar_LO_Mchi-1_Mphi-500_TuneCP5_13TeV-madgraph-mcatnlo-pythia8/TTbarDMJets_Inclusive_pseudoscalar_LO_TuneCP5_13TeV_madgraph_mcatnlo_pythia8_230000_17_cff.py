import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:16895', '1:80150', '1:40890', '1:41279', '1:52889', '1:61440', '1:71581', '1:79151', '1:40676', '1:46677', '1:47728', '1:49798', '1:40021', '1:97200', '1:80524', '1:73283', '1:73405', '1:75338', '1:12484', '1:12537', '1:12632', '1:12981', '1:13482', '1:13602', '1:14244', '1:22347', '1:22614', '1:22599', '1:22664', '1:30780', '1:32144', '1:30845', '1:1081', '1:1783', '1:24874', '1:89917', '1:90556', '1:90629', '1:7905', '1:8599', '1:8761', '1:9556', '1:9912', '1:10889', '1:15749', '1:41085', '1:41250', '1:41446', '1:41534', '1:41681', '1:41904', '1:95105', '1:95114', '1:43122', '1:54591', '1:73785', '1:80942', '1:39018', '1:57597', '1:64256', '1:66193', '1:75203', '1:56151', '1:61857', '1:62050', '1:62517', '1:66854', '1:106374', '1:96719', '1:87419', '1:64571', '1:64804', '1:64852', '1:103668', '1:17250', '1:17928', '1:27178', '1:24721', '1:46667', '1:49580', '1:49597', '1:105579', '1:87301', '1:87807', '1:87244', '1:92960', '1:93738', '1:10429', '1:10485', '1:10505', '1:10894', '1:14078', '1:90197', '1:92053', '1:97630', '1:81848', '1:81962', '1:81987', '1:53570', '1:48070', '1:98309', '1:106120', '1:103851', '1:105435', '1:105631', '1:106317', '1:53969', '1:51094', '1:55099', '1:88368', '1:90789', '1:92257', '1:87116', '1:105530', '1:105720', '1:106059', '1:106067', '1:4564', '1:7477', '1:6185', '1:6572', '1:6840', '1:9037', '1:17669', '1:19058', '1:19127', '1:19281', '1:19527', '1:19555', '1:19567', '1:24077', '1:24114', '1:24120', '1:24163', '1:19895', '1:27775', '1:28258', '1:28809', '1:29594', '1:48124', '1:48270', '1:48631', '1:48948', '1:56705', '1:88143', '1:88381', '1:88906', '1:89014', '1:89482', '1:23463', '1:49063', '1:49083', '1:96845', '1:40234', '1:40274', '1:30863', '1:43079', '1:43676', '1:43792', '1:40182', '1:43149', '1:40401', '1:40493', '1:40623', '1:46337', '1:46343', '1:41340', '1:49341', '1:49742', '1:60727', '1:62340', '1:62742', '1:81878', '1:48263', '1:46430', '1:46771', '1:48694', '1:49231', '1:51339', '1:55768', '1:51682', '1:52571', '1:57446', '1:62779', '1:55601', '1:58356', '1:61613', '1:62475', '1:66821', '1:79465', '1:79656', '1:81403', '1:93710', '1:84504', '1:85373', '1:88798', '1:85430', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DE44FE63-EB02-EA11-A34D-7CD30AC030B4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/547119DF-1A04-EA11-B104-AC1F6BC67D48.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02B13BB9-62FF-E911-984A-90B11CBCFFEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9CBC629C-D702-EA11-B565-0CC47AFF0200.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/781E8649-6AF8-E911-BBF5-D4AE5264D710.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F82C7F4C-0708-EA11-9AA9-0CC47A5FC2A5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/183064D5-6CF3-E911-BF5D-003048F29A12.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44DAFF4C-FAF4-E911-B4FC-509A4C9EF93B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8C2ADF7-09F5-E911-BBA1-509A4C9F8888.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A1C1EEA-26F7-E911-8EBF-E0071B7A68F0.root']);