import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:63158', '1:50718', '1:57569', '1:78977', '1:81074', '1:64992', '1:73282', '1:65276', '1:99625', '1:83205', '1:5103', '1:14925', '1:15730', '1:13747', '1:15736', '1:21689', '1:61601', '1:61888', '1:61730', '1:61916', '1:62111', '1:50767', '1:50814', '1:50739', '1:50852', '1:50831', '1:65282', '1:86158', '1:86211', '1:69724', '1:91539', '1:21279', '1:31216', '1:21037', '1:33559', '1:33745', '1:34294', '1:33843', '1:33852', '1:37499', '1:37952', '1:37997', '1:46047', '1:48023', '1:49283', '1:49409', '1:31359', '1:31580', '1:31695', '1:35486', '1:62005', '1:37624', '1:50261', '1:50317', '1:93204', '1:94865', '1:65610', '1:66607', '1:65624', '1:66053', '1:89750', '1:89782', '1:72230', '1:72254', '1:73357', '1:89646', '1:95993', '1:68724', '1:68735', '1:68787', '1:68801', '1:68818', '1:68832', '1:73709', '1:74001', '1:72166', '1:72212', '1:72292', '1:71974', '1:76613', '1:89714', '1:89958', '1:74430', '1:80908', '1:79186', '1:79338', '1:86884', '1:86894', '1:86337', '1:86571', '1:22040', '1:22048', '1:22099', '1:22162', '1:78609', '1:54413', '1:77388', '1:77496', '1:77508', '1:86375', '1:80824', '1:79146', '1:71123', '1:105162', '1:105203', '1:105424', '1:105436', '1:52996', '1:53469', '1:78887', '1:72829', '1:78520', '1:89906', '1:94737', '1:71479', '1:73623', '1:76399', '1:64847', '1:64848', '1:65113', '1:67858', '1:75622', '1:71585', '1:71692', '1:66040', '1:66159', '1:67675', '1:82686', '1:77515', '1:77546', '1:103384', '1:103549', '1:105724', '1:105823', '1:105915', '1:65453', '1:76648', '1:56194', '1:60822', '1:72453', '1:82547', '1:83266', '1:100987', '1:101011', '1:104817', '1:105541', '1:105646', '1:105659', '1:105748', '1:53324', '1:59035', '1:61483', '1:65523', '1:65570', '1:54053', '1:57067', '1:57369', '1:95417', '1:95549', '1:95671', '1:77777', '1:62070', '1:90083', '1:90853', '1:94034', '1:94050', '1:89769', '1:94855', '1:63281', '1:63290', '1:63292', '1:63892', '1:65440', '1:76111', '1:64314', '1:64581', '1:64800', '1:65616', '1:65766', '1:74370', '1:74632', '1:86932', '1:92713', '1:105525', '1:105746', '1:68056', '1:68063', '1:45488', '1:45653', '1:41628', '1:43443', '1:98834', '1:88068', '1:60601', '1:60869', '1:60908', '1:61131', '1:61463', '1:60871', '1:61537', '1:71029', '1:73116', '1:82557', '1:70294', '1:70709', '1:33269', '1:33091', '1:33211', '1:80718', '1:86146', '1:76175', '1:76344', '1:55123', '1:56549', '1:57269', '1:68569', '1:68754', '1:99057', '1:99079', '1:77123', '1:78886', '1:79250', '1:79638', '1:82348', '1:82608', '1:99733', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/8867CCB3-B318-EA11-9095-0025905B859E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/6E39EBAF-B318-EA11-AA8D-AC1F6BAC7C10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/8CD12CC8-FE17-EA11-AB2D-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/BE1577AC-B318-EA11-84E0-0CC47A4C8E28.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/1CC8E6A9-B318-EA11-B94C-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/CC27F754-B118-EA11-82F0-AC1F6BAC8038.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/0C4EB1B9-B318-EA11-A9AA-0025905B8594.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/C0348BAE-B318-EA11-97D9-0CC47A4C8E22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/DE5063B5-B318-EA11-9FEF-0CC47A7C3450.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/66967FAD-B318-EA11-B842-0CC47A78A33E.root']);