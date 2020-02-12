import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:26871', '1:31244', '1:28692', '1:32083', '1:69241', '1:86816', '1:92576', '1:93215', '1:98822', '1:97014', '1:97784', '1:11253', '1:11409', '1:11447', '1:11953', '1:45276', '1:45395', '1:45549', '1:45638', '1:45646', '1:74254', '1:69958', '1:99050', '1:70297', '1:21317', '1:21329', '1:21714', '1:84916', '1:84485', '1:84758', '1:83556', '1:85081', '1:22256', '1:22394', '1:63178', '1:40227', '1:97540', '1:97804', '1:98228', '1:32961', '1:34598', '1:35330', '1:34721', '1:34747', '1:37720', '1:71273', '1:76910', '1:74331', '1:75849', '1:75201', '1:79693', '1:94940', '1:9808', '1:10041', '1:10277', '1:10654', '1:29751', '1:39145', '1:105279', '1:10210', '1:10423', '1:10480', '1:54615', '1:54616', '1:54736', '1:54832', '1:54839', '1:55204', '1:77741', '1:78003', '1:77310', '1:83261', '1:13048', '1:13183', '1:15275', '1:17399', '1:17526', '1:17721', '1:17808', '1:17999', '1:19053', '1:19135', '1:19224', '1:42634', '1:23279', '1:23658', '1:23752', '1:54989', '1:55131', '1:55291', '1:55464', '1:55732', '1:79488', '1:63594', '1:63929', '1:69679', '1:69681', '1:30928', '1:32182', '1:32229', '1:32269', '1:32393', '1:37575', '1:4467', '1:6115', '1:12133', '1:9563', '1:10868', '1:91491', '1:92919', '1:4605', '1:4728', '1:5198', '1:5237', '1:5695', '1:6021', '1:6914', '1:6960', '1:11208', '1:13472', '1:14593', '1:37836', '1:37413', '1:50001', '1:68917', '1:50691', '1:50924', '1:58371', '1:55302', '1:55310', '1:104429', '1:104661', '1:105996', '1:18252', '1:18642', '1:19903', '1:71630', '1:74930', '1:78357', '1:84384', '1:85148', '1:86370', '1:84483', '1:91628', '1:94024', '1:86361', '1:86806', '1:87989', '1:79244', '1:79282', '1:79665', '1:94161', '1:94797', '1:1599', '1:9421', '1:11676', '1:19034', '1:17042', '1:91124', '1:92517', '1:91988', '1:92810', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/54925349-9519-EA11-8883-A0369FC5D904.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/E0951404-C619-EA11-B099-008CFA56D794.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/28EB89BA-D919-EA11-84D5-AC1F6B1AEFFC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/123DAC5E-E119-EA11-AA7C-0CC47A2B04A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/8AF33801-A818-EA11-ADA3-3417EBE700A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/04330BE3-4D19-EA11-B1D0-FA163EA7FFF8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/FEA9539C-0D19-EA11-88D3-FA163E800347.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/361BF4AC-E81A-EA11-92A9-001E675825D4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/628B0069-E81A-EA11-8EAC-AC1F6B5676BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/50B0175D-E81A-EA11-B967-90B11C443C1A.root']);