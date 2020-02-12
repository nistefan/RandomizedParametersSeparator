import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:53114', '1:52817', '1:57090', '1:60916', '1:60997', '1:63067', '1:68369', '1:68670', '1:62866', '1:64719', '1:67056', '1:67100', '1:64470', '1:87352', '1:87454', '1:87530', '1:88014', '1:76774', '1:76709', '1:77683', '1:77750', '1:77926', '1:77971', '1:78001', '1:78890', '1:80058', '1:80234', '1:80306', '1:81723', '1:81801', '1:81880', '1:81890', '1:89780', '1:89838', '1:89471', '1:91619', '1:99829', '1:101343', '1:33963', '1:28572', '1:30613', '1:32993', '1:100572', '1:100715', '1:100780', '1:100852', '1:101057', '1:101102', '1:101489', '1:63014', '1:63288', '1:63323', '1:63472', '1:63547', '1:73129', '1:73191', '1:73337', '1:73401', '1:73441', '1:73556', '1:73666', '1:99791', '1:99713', '1:99718', '1:74590', '1:75630', '1:74911', '1:74922', '1:75050', '1:85622', '1:85670', '1:86069', '1:89130', '1:89177', '1:91300', '1:72010', '1:72045', '1:72139', '1:73027', '1:73087', '1:73266', '1:90186', '1:90341', '1:90428', '1:90163', '1:99365', '1:94397', '1:94018', '1:94336', '1:87216', '1:87229', '1:87781', '1:88137', '1:88357', '1:88672', '1:87881', '1:94481', '1:95482', '1:95961', '1:96141', '1:96050', '1:96185', '1:97888', '1:97995', '1:96205', '1:96243', '1:59813', '1:64450', '1:69904', '1:70959', '1:71982', '1:81721', '1:80478', '1:77850', '1:77897', '1:77930', '1:77937', '1:77973', '1:79175', '1:79329', '1:98382', '1:98991', '1:98565', '1:98733', '1:98734', '1:97250', '1:97788', '1:98144', '1:101811', '1:101867', '1:58813', '1:58816', '1:59274', '1:59333', '1:79582', '1:80026', '1:80122', '1:80263', '1:80300', '1:96307', '1:96763', '1:96873', '1:96969', '1:97007', '1:98129', '1:98216', '1:100429', '1:100447', '1:101697', '1:102050', '1:97721', '1:98167', '1:98253', '1:51061', '1:68346', '1:68803', '1:68834', '1:68883', '1:68913', '1:69541', '1:69595', '1:70128', '1:70130', '1:79728', '1:80006', '1:80233', '1:80312', '1:81789', '1:81809', '1:81829', '1:90947', '1:95188', '1:95387', '1:97828', '1:58615', '1:60425', '1:61823', '1:69068', '1:79832', '1:80217', '1:85400', '1:90101', '1:88801', '1:90413', '1:94093', '1:95667', '1:96651', '1:101055', '1:90368', '1:91850', '1:90192', '1:100335', '1:49840', '1:50688', '1:52626', '1:53281', '1:53344', '1:74256', '1:74304', '1:74311', '1:74331', '1:74376', '1:77731', '1:77761', '1:79900', '1:85105', '1:85549', '1:94721', '1:78372', '1:79121', '1:79415', '1:79809', '1:80076', '1:81122', '1:81235', '1:85526', '1:81549', '1:98817', '1:10774', '1:15690', '1:19660', '1:38404', '1:57357', '1:38112', '1:38487', '1:51327', '1:63166', '1:69251', '1:46789', '1:57592', '1:49333', '1:57116', '1:50611', '1:86908', '1:85688', '1:86689', '1:96605', '1:96674', '1:100642', '1:101845', '1:102164', '1:102169', '1:89370', '1:94895', '1:88500', '1:100239', '1:100311', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D0241D99-25FD-E911-9A16-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EAF2400-04FD-E911-8A7B-3417EBE70069.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7AC88287-1AFD-E911-9DB6-98039B3B0036.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/789A2143-22FD-E911-8F35-3417EBE74303.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/58846ADE-14FD-E911-8D76-0CC47A7E6A6C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5CEF96A1-4CFD-E911-A376-002590DBDFE2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AEFA4F64-4300-EA11-B353-8CDCD4A99E60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/08DA8782-82FF-E911-9D78-5065F381F1C1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AEB54D0F-B601-EA11-988C-38EAA78D89AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96081A56-F7FE-E911-9BCC-00259055CA34.root']);