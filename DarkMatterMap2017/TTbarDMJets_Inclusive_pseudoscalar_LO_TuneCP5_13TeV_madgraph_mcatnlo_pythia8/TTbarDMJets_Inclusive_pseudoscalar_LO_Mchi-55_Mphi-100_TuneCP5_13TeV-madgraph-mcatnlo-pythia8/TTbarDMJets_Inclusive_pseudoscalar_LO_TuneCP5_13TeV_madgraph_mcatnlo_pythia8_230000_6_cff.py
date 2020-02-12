import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:39680', '1:70475', '1:70720', '1:81431', '1:81633', '1:81666', '1:81820', '1:89325', '1:85205', '1:90156', '1:90209', '1:90366', '1:90429', '1:90538', '1:90582', '1:91465', '1:105360', '1:83581', '1:83052', '1:83268', '1:83298', '1:83505', '1:83571', '1:84110', '1:84113', '1:84251', '1:87052', '1:87337', '1:94336', '1:92624', '1:88695', '1:92653', '1:94350', '1:94073', '1:96324', '1:26930', '1:31796', '1:16945', '1:27150', '1:102066', '1:102098', '1:102319', '1:101941', '1:53874', '1:54190', '1:54209', '1:54249', '1:54539', '1:54661', '1:78004', '1:78461', '1:85942', '1:89124', '1:93952', '1:18571', '1:18712', '1:18843', '1:18956', '1:18979', '1:18988', '1:22163', '1:22219', '1:22165', '1:72982', '1:73131', '1:73312', '1:76551', '1:39787', '1:39856', '1:42121', '1:43249', '1:43342', '1:43412', '1:76325', '1:76356', '1:1559', '1:15555', '1:25217', '1:95361', '1:95418', '1:76249', '1:93348', '1:93467', '1:42299', '1:42617', '1:48933', '1:47262', '1:47334', '1:47677', '1:47691', '1:48375', '1:55127', '1:49981', '1:88285', '1:101346', '1:101733', '1:101739', '1:102214', '1:102334', '1:104943', '1:47594', '1:47725', '1:103705', '1:77821', '1:82422', '1:82493', '1:87128', '1:87548', '1:87636', '1:90869', '1:92154', '1:95479', '1:97004', '1:97424', '1:97955', '1:103249', '1:103273', '1:103354', '1:103404', '1:103311', '1:103476', '1:96639', '1:44164', '1:58965', '1:27527', '1:28712', '1:57306', '1:30227', '1:57350', '1:66989', '1:77735', '1:29667', '1:29749', '1:31843', '1:102764', '1:102780', '1:61898', '1:77709', '1:88364', '1:88408', '1:88717', '1:89010', '1:89034', '1:4759', '1:49701', '1:53263', '1:10717', '1:66008', '1:73762', '1:13859', '1:26156', '1:14207', '1:23283', '1:24270', '1:25276', '1:59023', '1:64169', '1:53079', '1:53510', '1:65034', '1:64617', '1:64671', '1:64761', '1:65130', '1:65452', '1:1076', '1:1252', '1:3039', '1:5665', '1:5984', '1:23386', '1:23746', '1:27207', '1:27210', '1:27361', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/509597B0-AEFB-E911-878E-002590DE3A92.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90776FDE-BDFB-E911-84D1-40F2E9C6ADBA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F6B93E96-C5FB-E911-9974-3417EBE7047A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BA100FA2-4EFE-E911-96A3-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F43443B4-ECFC-E911-BEB6-24BE05C4D8F1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BAA9281E-48FE-E911-B284-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/82DC5317-C9FE-E911-A8D4-0030487BB52E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A904563-4D00-EA11-8187-002481CFE1EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B29D7EA4-74FF-E911-97CA-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/56EB785D-ADFE-E911-8744-0CC47A5FC281.root']);