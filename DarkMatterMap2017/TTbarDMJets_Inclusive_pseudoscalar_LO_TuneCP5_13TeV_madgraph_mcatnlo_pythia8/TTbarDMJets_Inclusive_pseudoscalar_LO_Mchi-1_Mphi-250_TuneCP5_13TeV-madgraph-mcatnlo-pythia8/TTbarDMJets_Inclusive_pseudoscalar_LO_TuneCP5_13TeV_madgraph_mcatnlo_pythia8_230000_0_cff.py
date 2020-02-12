import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:88777', '1:93138', '1:101630', '1:7925', '1:8340', '1:8395', '1:8396', '1:8476', '1:23142', '1:52477', '1:52839', '1:61280', '1:61482', '1:54291', '1:54586', '1:58613', '1:59817', '1:76407', '1:85079', '1:85111', '1:89809', '1:90491', '1:7576', '1:7125', '1:7529', '1:8051', '1:8335', '1:8519', '1:9031', '1:9071', '1:9153', '1:9459', '1:9505', '1:9559', '1:46500', '1:46653', '1:46684', '1:46778', '1:46854', '1:46887', '1:52865', '1:52994', '1:53950', '1:54277', '1:12021', '1:12629', '1:13447', '1:55696', '1:55962', '1:23376', '1:27944', '1:28810', '1:53602', '1:53735', '1:55022', '1:40627', '1:83388', '1:95766', '1:96485', '1:96630', '1:87970', '1:91035', '1:1449', '1:15225', '1:4834', '1:12668', '1:1837', '1:5415', '1:29362', '1:29960', '1:47822', '1:13766', '1:14053', '1:17810', '1:27859', '1:20073', '1:18931', '1:23801', '1:1005', '1:1032', '1:1495', '1:1547', '1:8199', '1:8378', '1:8462', '1:31501', '1:6198', '1:6279', '1:3851', '1:3855', '1:3649', '1:3864', '1:4131', '1:15233', '1:8078', '1:8082', '1:6863', '1:8711', '1:5894', '1:9321', '1:14002', '1:46593', '1:46212', '1:18130', '1:41251', '1:43788', '1:45419', '1:42751', '1:78608', '1:90889', '1:47267', '1:4500', '1:8228', '1:57384', '1:60755', '1:76937', '1:87440', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A28F10B-AA07-EA11-B3F4-AC1F6B1B2364.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E0E93DFE-8FFB-E911-AE26-0CC47AFF01B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44DA73CB-BEFC-E911-AE13-001E67E5EDBB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D21296E4-5DFC-E911-9755-0025905C53D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/04526127-A3FB-E911-9F1B-0CC47AFEFDE4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1066B909-FF08-EA11-809A-AC1F6B1AEF94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2AA5595F-5BEF-E911-A3D3-D4AE528FF49B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8EFD98F-8FF2-E911-BA8E-0CC47A7E6A88.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/ECB29738-6AEF-E911-ADB3-E0071B740D90.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C9B1AC6-35F0-E911-A35E-F01FAFD9C1A8.root']);