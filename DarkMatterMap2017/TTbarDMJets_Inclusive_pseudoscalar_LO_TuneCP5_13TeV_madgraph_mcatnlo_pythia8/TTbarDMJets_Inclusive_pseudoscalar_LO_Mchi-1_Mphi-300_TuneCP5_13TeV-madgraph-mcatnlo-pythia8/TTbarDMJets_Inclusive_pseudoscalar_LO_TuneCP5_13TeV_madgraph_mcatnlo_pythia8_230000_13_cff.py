import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:40648', '1:48400', '1:39645', '1:57842', '1:58095', '1:58192', '1:59225', '1:62305', '1:62574', '1:62811', '1:81395', '1:86676', '1:21365', '1:23999', '1:29918', '1:45939', '1:46227', '1:101071', '1:24152', '1:20411', '1:20435', '1:48356', '1:48624', '1:48680', '1:75387', '1:32639', '1:65495', '1:75899', '1:94895', '1:94909', '1:95179', '1:95259', '1:95277', '1:95356', '1:95447', '1:65894', '1:83715', '1:83696', '1:86295', '1:84992', '1:70134', '1:70646', '1:92520', '1:93340', '1:98375', '1:103179', '1:97662', '1:7618', '1:7773', '1:7991', '1:9070', '1:12885', '1:14852', '1:46403', '1:46618', '1:48019', '1:14641', '1:20208', '1:20237', '1:17128', '1:17135', '1:17159', '1:23556', '1:23428', '1:26267', '1:21827', '1:23186', '1:23938', '1:27928', '1:27994', '1:28199', '1:76505', '1:76495', '1:85730', '1:91747', '1:91373', '1:64092', '1:64531', '1:76436', '1:76566', '1:76705', '1:56475', '1:56566', '1:56737', '1:76670', '1:80057', '1:81394', '1:80164', '1:80650', '1:80717', '1:80722', '1:76276', '1:49738', '1:49757', '1:49839', '1:96682', '1:96801', '1:96868', '1:97296', '1:97311', '1:98402', '1:103107', '1:87481', '1:87625', '1:87669', '1:87725', '1:88014', '1:101730', '1:102135', '1:102269', '1:12625', '1:18534', '1:41370', '1:45601', '1:19536', '1:19572', '1:19638', '1:19681', '1:19718', '1:19856', '1:26558', '1:26730', '1:26641', '1:43516', '1:43605', '1:44203', '1:52847', '1:16801', '1:15037', '1:15191', '1:15409', '1:51505', '1:53468', '1:64353', '1:74653', '1:76191', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96B475A8-45F7-E911-A1D4-002590E7D7E2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4056591E-F209-EA11-A699-44A842CFD5BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/006C1B93-29F3-E911-9D2E-6C2B598FF86B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E90CC6C-9A07-EA11-9BAF-0CC47A7C3432.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/463016DD-5DFC-E911-A3BD-0CC47AFCC69E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCD2DC78-350F-EA11-A934-509A4C9F8A8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/36068975-BBFA-E911-8ED3-509A4C9EF923.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C6AA3D6D-A7FB-E911-B199-40F2E9C6ADBA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C4F880FC-64FC-E911-9F1D-0CC47AFF0188.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72568A99-5504-EA11-9A4E-14187764311A.root']);