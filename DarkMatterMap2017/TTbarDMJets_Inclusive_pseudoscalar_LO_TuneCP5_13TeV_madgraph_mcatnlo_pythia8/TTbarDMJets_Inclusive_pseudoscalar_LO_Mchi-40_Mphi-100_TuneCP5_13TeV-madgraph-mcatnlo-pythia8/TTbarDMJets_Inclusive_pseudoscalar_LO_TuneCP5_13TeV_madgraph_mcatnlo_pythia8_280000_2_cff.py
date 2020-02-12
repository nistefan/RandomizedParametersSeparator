import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:63179', '1:50734', '1:57591', '1:57636', '1:57806', '1:57829', '1:82244', '1:85198', '1:64894', '1:64951', '1:64983', '1:65036', '1:86789', '1:97580', '1:72471', '1:65203', '1:99634', '1:69322', '1:83464', '1:87693', '1:1389', '1:5489', '1:15447', '1:16624', '1:14564', '1:61993', '1:62036', '1:62003', '1:50766', '1:50772', '1:50759', '1:50879', '1:83937', '1:91847', '1:93724', '1:86009', '1:86432', '1:7916', '1:13037', '1:12225', '1:21665', '1:31646', '1:33771', '1:33786', '1:33788', '1:49272', '1:37619', '1:33967', '1:60610', '1:31420', '1:31514', '1:79644', '1:38612', '1:66988', '1:65625', '1:65773', '1:89509', '1:72716', '1:73542', '1:72675', '1:90979', '1:68570', '1:68574', '1:68824', '1:68835', '1:74003', '1:72052', '1:71934', '1:72034', '1:72366', '1:80480', '1:82137', '1:85225', '1:82656', '1:90325', '1:96986', '1:105479', '1:74714', '1:75044', '1:79310', '1:80734', '1:86313', '1:86322', '1:86512', '1:4827', '1:5162', '1:9213', '1:22059', '1:22300', '1:22316', '1:54913', '1:54282', '1:77927', '1:81383', '1:80947', '1:80961', '1:80973', '1:81285', '1:79140', '1:71260', '1:84520', '1:105630', '1:105713', '1:105252', '1:49550', '1:49567', '1:61830', '1:66120', '1:61358', '1:61491', '1:59053', '1:58536', '1:89528', '1:90368', '1:67713', '1:78262', '1:85262', '1:75769', '1:64993', '1:71478', '1:71727', '1:71594', '1:65743', '1:66147', '1:66214', '1:75657', '1:67822', '1:67680', '1:83750', '1:95055', '1:98018', '1:105421', '1:90615', '1:91531', '1:105991', '1:52683', '1:77845', '1:94354', '1:97803', '1:97941', '1:91887', '1:100980', '1:105645', '1:105797', '1:53785', '1:57491', '1:59069', '1:53794', '1:53908', '1:54020', '1:54080', '1:68769', '1:68770', '1:57234', '1:68592', '1:68626', '1:60674', '1:98944', '1:61669', '1:70900', '1:86429', '1:92086', '1:94814', '1:63274', '1:71122', '1:76581', '1:79556', '1:64900', '1:65736', '1:65737', '1:75692', '1:87976', '1:92931', '1:44513', '1:45695', '1:43548', '1:60724', '1:60747', '1:60796', '1:60826', '1:61543', '1:60960', '1:60992', '1:60963', '1:60909', '1:61133', '1:61310', '1:61045', '1:61146', '1:61328', '1:71021', '1:71275', '1:70577', '1:70610', '1:70999', '1:33186', '1:34718', '1:33050', '1:33179', '1:33197', '1:33217', '1:33060', '1:63723', '1:78938', '1:79935', '1:75314', '1:75392', '1:75530', '1:76079', '1:56264', '1:54323', '1:68682', '1:63769', '1:89527', '1:79185', '1:99723', '1:99744', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/8867CCB3-B318-EA11-9095-0025905B859E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/6E39EBAF-B318-EA11-AA8D-AC1F6BAC7C10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/8CD12CC8-FE17-EA11-AB2D-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/BE1577AC-B318-EA11-84E0-0CC47A4C8E28.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/1CC8E6A9-B318-EA11-B94C-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/CC27F754-B118-EA11-82F0-AC1F6BAC8038.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/0C4EB1B9-B318-EA11-A9AA-0025905B8594.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/C0348BAE-B318-EA11-97D9-0CC47A4C8E22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/DE5063B5-B318-EA11-9FEF-0CC47A7C3450.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/66967FAD-B318-EA11-B842-0CC47A78A33E.root']);