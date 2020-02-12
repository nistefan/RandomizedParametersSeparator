import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:15514', '1:42333', '1:42593', '1:52537', '1:31186', '1:18357', '1:27212', '1:19217', '1:19505', '1:19515', '1:43220', '1:44568', '1:65379', '1:62939', '1:67126', '1:72241', '1:95471', '1:102027', '1:105816', '1:28124', '1:28324', '1:44585', '1:45091', '1:45219', '1:91680', '1:90369', '1:19694', '1:20351', '1:20371', '1:20403', '1:20460', '1:20762', '1:24740', '1:24942', '1:25778', '1:47554', '1:70185', '1:64736', '1:85569', '1:77623', '1:86566', '1:90806', '1:9282', '1:23195', '1:23536', '1:26304', '1:31437', '1:81461', '1:8769', '1:11823', '1:101299', '1:101300', '1:101828', '1:102339', '1:102356', '1:66625', '1:47907', '1:18103', '1:18057', '1:18186', '1:40028', '1:46042', '1:47544', '1:90078', '1:94660', '1:4307', '1:15912', '1:10904', '1:20936', '1:29025', '1:29406', '1:30084', '1:30854', '1:30960', '1:82560', '1:98767', '1:98771', '1:82184', '1:83478', '1:83982', '1:91857', '1:49964', '1:48537', '1:48784', '1:72303', '1:85000', '1:85277', '1:87476', '1:52364', '1:52375', '1:52391', '1:70212', '1:70218', '1:102482', '1:28865', '1:47567', '1:47600', '1:49684', '1:104557', '1:104627', '1:45946', '1:29429', '1:103629', '1:105995', '1:97612', '1:86067', '1:105585', '1:103714', '1:105031', '1:101880', '1:6468', '1:7403', '1:7414', '1:7856', '1:8231', '1:20825', '1:24418', '1:24673', '1:98398', '1:101939', '1:102205', '1:104431', '1:51449', '1:53116', '1:62318', '1:62690', '1:62696', '1:5592', '1:6252', '1:5745', '1:6155', '1:9892', '1:9998', '1:10248', '1:11592', '1:11997', '1:14116', '1:14011', '1:7415', '1:10603', '1:9680', '1:10193', '1:15499', '1:16455', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C75EAD7-A60A-EA11-B2EA-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CAA33E3-B40A-EA11-B217-0CC47A4C8EB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0C7BD80-B30A-EA11-990C-0CC47A7C345E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/827A94E9-460C-EA11-9197-0CC47A7C34D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C25D68E-CA0A-EA11-A4D3-0CC47A4D762E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4F23B9-260F-EA11-80C3-0CC47A4D7690.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A38857F-43F9-E911-9334-0CC47A5FBE21.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2A529D76-BC12-EA11-85B1-90B11C070100.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80404779-FBF6-E911-8982-AC1F6B0F71D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A13F5EF-28F2-E911-9B0D-00215AA64960.root']);