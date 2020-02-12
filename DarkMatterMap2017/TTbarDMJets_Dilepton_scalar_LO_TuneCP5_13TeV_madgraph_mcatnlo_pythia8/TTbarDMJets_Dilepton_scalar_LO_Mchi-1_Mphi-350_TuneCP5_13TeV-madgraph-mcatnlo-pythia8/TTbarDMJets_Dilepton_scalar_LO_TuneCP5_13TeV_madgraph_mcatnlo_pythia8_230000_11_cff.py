import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:55284', '1:55858', '1:57315', '1:57752', '1:70314', '1:70421', '1:61554', '1:62215', '1:61578', '1:61882', '1:82008', '1:105127', '1:105148', '1:82259', '1:82262', '1:82295', '1:10548', '1:10053', '1:10143', '1:10402', '1:14858', '1:18429', '1:18601', '1:18989', '1:20674', '1:49836', '1:51368', '1:52775', '1:92226', '1:92979', '1:85946', '1:84076', '1:83084', '1:83108', '1:83258', '1:83352', '1:83584', '1:87572', '1:87668', '1:87773', '1:87857', '1:87998', '1:92156', '1:93319', '1:93371', '1:93495', '1:93548', '1:94346', '1:94469', '1:16680', '1:16806', '1:49392', '1:49484', '1:50010', '1:50210', '1:50991', '1:51226', '1:52838', '1:53023', '1:49450', '1:81255', '1:93562', '1:93175', '1:103605', '1:104053', '1:104579', '1:105108', '1:106148', '1:12153', '1:12247', '1:12259', '1:14409', '1:66924', '1:68094', '1:68896', '1:70037', '1:67873', '1:72102', '1:72158', '1:72119', '1:75483', '1:75494', '1:77959', '1:77348', '1:74237', '1:74395', '1:80024', '1:80548', '1:79634', '1:79666', '1:91157', '1:94374', '1:94400', '1:94464', '1:92167', '1:92270', '1:92298', '1:92307', '1:363', '1:4329', '1:7174', '1:12627', '1:12878', '1:15919', '1:16373', '1:41690', '1:41732', '1:48189', '1:48326', '1:9414', '1:35014', '1:35576', '1:37751', '1:33199', '1:36097', '1:36140', '1:36647', '1:36835', '1:37148', '1:35893', '1:38578', '1:52854', '1:49874', '1:50066', '1:50972', '1:49873', '1:49980', '1:2367', '1:2424', '1:3164', '1:3184', '1:3488', '1:16728', '1:42221', '1:46918', '1:47851', '1:47871', '1:67645', '1:65168', '1:41969', '1:42850', '1:47583', '1:47747', '1:47756', '1:7289', '1:7747', '1:7949', '1:7874', '1:8538', '1:12794', '1:21484', '1:58503', '1:62237', '1:67620', '1:68999', '1:82138', '1:93827', '1:97876', '1:100960', '1:104387', '1:102966', '1:3511', '1:3546', '1:3739', '1:9754', '1:9772', '1:4400', '1:7582', '1:7736', '1:7762', '1:7844', '1:7852', '1:7864', '1:10883', '1:39331', '1:70050', '1:70132', '1:83307', '1:91876', '1:91982', '1:92052', '1:97252', '1:97269', '1:105387', '1:5247', '1:5445', '1:7270', '1:5930', '1:9505', '1:17265', '1:17259', '1:17282', '1:18107', '1:18216', '1:18060', '1:37902', '1:10228', '1:40831', '1:51358', '1:51820', '1:53117', '1:52587', '1:58216', '1:60902', '1:61797', '1:60794', '1:73955', '1:5034', '1:5165', '1:5417', '1:5432', '1:5657', '1:3324', '1:3517', '1:3545', '1:3654', '1:4010', '1:12711', '1:12994', '1:14169', '1:14296', '1:9853', '1:8346', '1:8373', '1:8383', '1:8490', '1:40010', '1:40433', '1:40440', '1:39341', '1:39435', '1:54535', '1:54583', '1:8977', '1:14005', '1:9131', '1:10812', '1:10845', '1:10854', '1:10894', '1:678', '1:1028', '1:4091', '1:4571', '1:2058', '1:2206', '1:3534', '1:3840', '1:40926', '1:48659', '1:48660', '1:48827', '1:50266', '1:50551', '1:106285', '1:105367', '1:4515', '1:4755', '1:4786', '1:4826', '1:18642', '1:20883', '1:26357', '1:26574', '1:26578', '1:26620', '1:26737', '1:27209', '1:27276', '1:27297', '1:24594', '1:34918', '1:34931', '1:34950', '1:34987', '1:37068', '1:37071', '1:24399', '1:24543', '1:34382', '1:34265', '1:34440', '1:36053', '1:36258', '1:36265', '1:47958', '1:73824', '1:73866', '1:73875', '1:74054', '1:74057', '1:74195', '1:100991', '1:102116', '1:102146', '1:102183', '1:102184', '1:102194', '1:102257', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E2848B0E-44F2-E911-825D-509A4C9F8ADB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BEF0CDD4-E4F6-E911-83C1-0CC47A0AD6FC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/16FBEA03-EAF2-E911-B29A-44A842BECCB1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F83A579D-8B01-EA11-AABA-00259073E45A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/20F66F39-4203-EA11-A2F6-405CFDFF481B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4AA2791D-9EF2-E911-8C38-3417EBE74303.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96CDDC18-A20E-EA11-A3B2-00266CFFBF88.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/982A8027-7FEE-E911-B6C3-089E0158CD57.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4EE87D2-0B09-EA11-92AB-00266CF3E174.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C5B6E03-5CFF-E911-B90B-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D26BC5FF-970A-EA11-95B5-0CC47A4D7666.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AA873AAA-B402-EA11-9A84-0025905C9742.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B20562A7-710E-EA11-8BD4-0CC47A78A478.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4A15B08-AFEE-E911-9943-8CDCD4A99E08.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/529ABEDC-6210-EA11-9BFF-506B4BF38280.root']);