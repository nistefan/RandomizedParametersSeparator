import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:67808', '1:78401', '1:70980', '1:72234', '1:72417', '1:76913', '1:77097', '1:79319', '1:89156', '1:97143', '1:97179', '1:80500', '1:9109', '1:9157', '1:14552', '1:14795', '1:14803', '1:15381', '1:73335', '1:69450', '1:55906', '1:55915', '1:62478', '1:57297', '1:59836', '1:59861', '1:59875', '1:60034', '1:60092', '1:60273', '1:57317', '1:81915', '1:87460', '1:99876', '1:80585', '1:80822', '1:86227', '1:86397', '1:87623', '1:90114', '1:89194', '1:89290', '1:90115', '1:124', '1:249', '1:427', '1:603', '1:662', '1:384', '1:512', '1:345', '1:4425', '1:6322', '1:6678', '1:6896', '1:7029', '1:516', '1:22320', '1:53939', '1:53948', '1:383', '1:7484', '1:19428', '1:511', '1:1434', '1:6110', '1:6241', '1:6960', '1:34027', '1:32633', '1:80146', '1:22410', '1:53982', '1:88097', '1:97422', '1:97802', '1:14435', '1:14522', '1:14218', '1:14853', '1:15053', '1:19599', '1:15316', '1:16281', '1:16541', '1:17556', '1:17718', '1:17759', '1:17766', '1:20701', '1:20886', '1:21049', '1:21052', '1:17086', '1:17144', '1:17466', '1:17469', '1:16882', '1:24200', '1:24394', '1:32793', '1:32953', '1:32826', '1:35067', '1:35204', '1:14322', '1:8348', '1:8776', '1:8899', '1:9027', '1:9249', '1:11134', '1:11137', '1:11161', '1:11361', '1:12044', '1:24251', '1:34064', '1:40406', '1:56375', '1:56539', '1:24854', '1:21614', '1:21664', '1:21721', '1:21879', '1:21890', '1:21639', '1:22150', '1:30524', '1:30546', '1:30325', '1:30592', '1:30778', '1:30868', '1:33616', '1:33871', '1:369', '1:1593', '1:1937', '1:667', '1:42387', '1:42391', '1:41339', '1:42701', '1:42727', '1:42551', '1:65233', '1:6451', '1:7508', '1:20150', '1:18571', '1:15179', '1:12607', '1:11465', '1:12924', '1:42232', '1:41208', '1:41501', '1:60836', '1:34994', '1:35133', '1:37057', '1:48833', '1:48847', '1:65988', '1:63163', '1:53610', '1:63625', '1:50303', '1:59715', '1:34559', '1:82059', '1:82104', '1:81332', '1:15350', '1:44898', '1:27332', '1:31280', '1:35939', '1:39189', '1:40586', '1:46769', '1:67153', '1:65489', '1:65498', '1:65514', '1:45877', '1:43725', '1:43606', '1:43610', '1:65200', '1:74756', '1:92205', '1:86536', '1:55796', '1:62206', '1:88086', '1:90047', '1:90198', '1:90762', '1:90895', '1:33197', '1:38821', '1:34492', '1:34711', '1:46041', '1:24221', '1:37037', '1:31178', '1:46809', '1:52332', '1:62218', '1:70923', '1:45401', '1:48944', '1:65856', '1:79867', '1:71961', '1:87759', '1:75737', '1:75751', '1:78200', '1:78275', '1:98317', '1:81012', '1:81456', '1:79853', '1:79859', '1:80685', '1:81185', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8043D626-B016-EA11-8A6B-14187751C239.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D6C9BD41-E917-EA11-AC25-24BE05C63631.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/98533757-B016-EA11-BA5A-3417EBE51901.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/88043001-7B17-EA11-92B4-9CDC714AE580.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2A4E415B-BF17-EA11-B25D-EC0D9A8221CE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B855FCAA-0F18-EA11-91AF-A0369F30FFD2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1054BB23-6E17-EA11-A63C-A0369F3102F6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/7830E6AA-AE17-EA11-830F-E0071B7AD580.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/EA8BAF91-6317-EA11-B8EA-B8CA3A70A5E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BCA7C346-9817-EA11-A3E0-0242AC1C0500.root']);