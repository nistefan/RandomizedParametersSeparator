import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:50704', '1:50622', '1:74286', '1:76871', '1:64821', '1:64912', '1:64968', '1:65030', '1:64997', '1:76347', '1:78483', '1:80152', '1:65207', '1:65297', '1:65435', '1:65535', '1:65606', '1:99640', '1:96398', '1:86147', '1:5140', '1:11710', '1:13118', '1:13804', '1:15666', '1:27582', '1:31980', '1:19461', '1:61852', '1:50792', '1:50839', '1:50846', '1:103742', '1:93787', '1:86214', '1:87364', '1:99569', '1:69745', '1:99635', '1:20439', '1:26926', '1:12497', '1:21462', '1:33811', '1:33287', '1:33762', '1:54940', '1:33849', '1:40276', '1:42017', '1:40025', '1:31694', '1:31788', '1:36482', '1:66701', '1:61870', '1:61876', '1:38771', '1:68960', '1:68050', '1:67071', '1:67120', '1:66062', '1:72409', '1:72426', '1:72491', '1:72538', '1:72571', '1:72192', '1:73528', '1:75024', '1:68573', '1:95995', '1:68837', '1:73217', '1:73361', '1:73232', '1:73347', '1:73370', '1:74070', '1:71746', '1:72258', '1:72268', '1:72271', '1:75671', '1:70732', '1:85085', '1:97995', '1:74464', '1:74707', '1:80366', '1:12548', '1:14692', '1:22066', '1:77367', '1:96461', '1:79852', '1:81093', '1:81413', '1:79174', '1:78922', '1:79131', '1:71146', '1:84132', '1:49441', '1:65412', '1:67916', '1:61460', '1:58374', '1:58635', '1:78667', '1:86588', '1:71454', '1:72027', '1:72158', '1:77534', '1:76426', '1:76466', '1:76473', '1:64763', '1:64861', '1:75330', '1:80068', '1:71588', '1:65908', '1:66329', '1:73417', '1:73574', '1:77609', '1:87757', '1:87891', '1:103132', '1:103148', '1:103190', '1:91285', '1:75513', '1:76148', '1:56135', '1:67909', '1:90666', '1:95182', '1:99798', '1:105654', '1:105795', '1:105902', '1:68761', '1:68584', '1:95391', '1:95581', '1:95672', '1:95938', '1:78073', '1:61557', '1:62060', '1:86652', '1:86229', '1:63279', '1:63768', '1:63881', '1:79148', '1:65508', '1:65752', '1:67085', '1:86936', '1:87109', '1:105607', '1:68085', '1:68086', '1:42936', '1:45110', '1:45301', '1:47949', '1:40858', '1:60642', '1:60666', '1:60862', '1:60979', '1:60938', '1:60943', '1:60956', '1:61102', '1:61030', '1:61182', '1:61393', '1:61498', '1:71100', '1:67877', '1:89339', '1:70044', '1:70612', '1:33202', '1:78084', '1:81554', '1:76092', '1:73965', '1:63724', '1:69652', '1:85044', '1:88265', '1:79500', '1:83014', '1:100994', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/8867CCB3-B318-EA11-9095-0025905B859E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/6E39EBAF-B318-EA11-AA8D-AC1F6BAC7C10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/8CD12CC8-FE17-EA11-AB2D-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/BE1577AC-B318-EA11-84E0-0CC47A4C8E28.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/1CC8E6A9-B318-EA11-B94C-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/CC27F754-B118-EA11-82F0-AC1F6BAC8038.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/0C4EB1B9-B318-EA11-A9AA-0025905B8594.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/C0348BAE-B318-EA11-97D9-0CC47A4C8E22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/DE5063B5-B318-EA11-9FEF-0CC47A7C3450.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/66967FAD-B318-EA11-B842-0CC47A78A33E.root']);