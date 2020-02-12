import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:26751', '1:26832', '1:29312', '1:29572', '1:29421', '1:32843', '1:42069', '1:92958', '1:93713', '1:94253', '1:95332', '1:104588', '1:95950', '1:96244', '1:97132', '1:12163', '1:12688', '1:45557', '1:48604', '1:59029', '1:71173', '1:70156', '1:70532', '1:20735', '1:21483', '1:21646', '1:22417', '1:22592', '1:65837', '1:71032', '1:71331', '1:74300', '1:83442', '1:85066', '1:22141', '1:22338', '1:38869', '1:38652', '1:50910', '1:95694', '1:98061', '1:98198', '1:34584', '1:37080', '1:37672', '1:38457', '1:38460', '1:79442', '1:79468', '1:79559', '1:79590', '1:80384', '1:91008', '1:92012', '1:94824', '1:98797', '1:9817', '1:10236', '1:10258', '1:10527', '1:10942', '1:29767', '1:30133', '1:32003', '1:39577', '1:89027', '1:103609', '1:103744', '1:103797', '1:103825', '1:105384', '1:10176', '1:10283', '1:10695', '1:11025', '1:11796', '1:54489', '1:54527', '1:54708', '1:55057', '1:55210', '1:82084', '1:78618', '1:79429', '1:82418', '1:83454', '1:13046', '1:13910', '1:17852', '1:17914', '1:19212', '1:19232', '1:23848', '1:54750', '1:55236', '1:55276', '1:55416', '1:56134', '1:63825', '1:63601', '1:69010', '1:69021', '1:32891', '1:30587', '1:30919', '1:32189', '1:32198', '1:35263', '1:35265', '1:37318', '1:50692', '1:1347', '1:6599', '1:8417', '1:9597', '1:15972', '1:92741', '1:94582', '1:5318', '1:14025', '1:13227', '1:37290', '1:37585', '1:50025', '1:68501', '1:50540', '1:57800', '1:57890', '1:61636', '1:104702', '1:104562', '1:106091', '1:18152', '1:18490', '1:71670', '1:72933', '1:84256', '1:85898', '1:83121', '1:79264', '1:83311', '1:83959', '1:94744', '1:95680', '1:14185', '1:15012', '1:1682', '1:6741', '1:10286', '1:17035', '1:91600', '1:94040', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/54925349-9519-EA11-8883-A0369FC5D904.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/E0951404-C619-EA11-B099-008CFA56D794.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/28EB89BA-D919-EA11-84D5-AC1F6B1AEFFC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/123DAC5E-E119-EA11-AA7C-0CC47A2B04A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/8AF33801-A818-EA11-ADA3-3417EBE700A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/04330BE3-4D19-EA11-B1D0-FA163EA7FFF8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/FEA9539C-0D19-EA11-88D3-FA163E800347.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/361BF4AC-E81A-EA11-92A9-001E675825D4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/628B0069-E81A-EA11-8EAC-AC1F6B5676BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/50B0175D-E81A-EA11-B967-90B11C443C1A.root']);