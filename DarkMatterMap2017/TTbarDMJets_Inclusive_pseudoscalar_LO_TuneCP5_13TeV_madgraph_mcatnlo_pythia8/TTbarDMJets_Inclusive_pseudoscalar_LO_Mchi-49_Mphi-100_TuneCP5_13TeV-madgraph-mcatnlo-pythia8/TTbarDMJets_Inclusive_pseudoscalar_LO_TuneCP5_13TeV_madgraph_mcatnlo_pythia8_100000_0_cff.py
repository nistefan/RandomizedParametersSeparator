import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:31035', '1:31521', '1:31735', '1:29292', '1:29351', '1:69359', '1:69890', '1:82186', '1:82692', '1:93591', '1:93321', '1:94124', '1:95095', '1:104450', '1:97445', '1:97571', '1:11106', '1:11118', '1:11127', '1:11944', '1:12056', '1:45260', '1:56369', '1:59941', '1:70534', '1:97416', '1:21686', '1:21431', '1:21677', '1:22296', '1:74576', '1:86185', '1:84354', '1:84631', '1:84868', '1:84623', '1:83564', '1:84826', '1:84834', '1:86126', '1:31119', '1:38868', '1:38821', '1:40196', '1:40334', '1:97062', '1:37078', '1:37481', '1:38454', '1:38920', '1:72161', '1:75731', '1:73657', '1:73080', '1:10099', '1:10918', '1:11139', '1:29805', '1:39488', '1:105509', '1:95403', '1:105862', '1:10834', '1:10014', '1:10493', '1:10611', '1:54888', '1:54893', '1:55432', '1:79000', '1:13289', '1:14501', '1:17517', '1:17532', '1:17767', '1:17989', '1:101441', '1:23737', '1:23743', '1:55437', '1:29435', '1:29808', '1:30528', '1:32480', '1:35266', '1:37895', '1:37294', '1:6235', '1:83892', '1:91167', '1:5205', '1:5637', '1:6777', '1:7033', '1:13619', '1:13774', '1:15398', '1:15455', '1:33898', '1:50310', '1:50368', '1:50541', '1:50923', '1:60722', '1:55429', '1:56192', '1:104423', '1:104556', '1:18023', '1:18283', '1:18638', '1:18851', '1:72043', '1:73908', '1:76352', '1:78495', '1:83009', '1:94201', '1:86851', '1:79258', '1:1660', '1:2097', '1:8434', '1:91094', '1:92980', '1:95264', '1:97925', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/54925349-9519-EA11-8883-A0369FC5D904.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/E0951404-C619-EA11-B099-008CFA56D794.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/28EB89BA-D919-EA11-84D5-AC1F6B1AEFFC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/123DAC5E-E119-EA11-AA7C-0CC47A2B04A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/8AF33801-A818-EA11-ADA3-3417EBE700A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/04330BE3-4D19-EA11-B1D0-FA163EA7FFF8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/FEA9539C-0D19-EA11-88D3-FA163E800347.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/361BF4AC-E81A-EA11-92A9-001E675825D4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/628B0069-E81A-EA11-8EAC-AC1F6B5676BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/50B0175D-E81A-EA11-B967-90B11C443C1A.root']);