import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:32117', '1:32252', '1:32312', '1:32546', '1:32612', '1:32795', '1:39300', '1:86790', '1:84156', '1:84667', '1:84788', '1:88466', '1:89625', '1:90082', '1:90335', '1:91287', '1:105473', '1:105485', '1:84561', '1:83307', '1:83598', '1:86576', '1:86665', '1:86782', '1:86945', '1:87214', '1:90509', '1:87759', '1:94148', '1:26794', '1:31149', '1:16965', '1:23477', '1:26165', '1:22733', '1:22944', '1:102297', '1:53956', '1:54093', '1:54164', '1:54182', '1:54250', '1:54446', '1:54672', '1:76660', '1:78146', '1:78385', '1:88996', '1:89099', '1:89166', '1:18595', '1:18628', '1:44674', '1:22522', '1:22254', '1:22298', '1:22334', '1:22321', '1:73338', '1:73418', '1:73128', '1:39568', '1:39629', '1:39755', '1:43383', '1:43394', '1:43397', '1:43461', '1:2142', '1:9135', '1:24635', '1:77395', '1:89335', '1:77874', '1:39863', '1:42209', '1:51141', '1:51163', '1:51165', '1:51295', '1:47393', '1:52547', '1:84030', '1:86206', '1:102636', '1:102633', '1:47829', '1:52453', '1:84846', '1:103794', '1:105234', '1:105597', '1:106394', '1:106424', '1:82163', '1:78706', '1:87509', '1:96805', '1:96851', '1:97881', '1:98245', '1:98338', '1:103250', '1:103347', '1:103310', '1:103473', '1:30276', '1:43717', '1:54887', '1:49109', '1:59557', '1:71223', '1:71199', '1:71210', '1:71442', '1:18486', '1:42446', '1:55064', '1:77169', '1:85150', '1:29550', '1:29663', '1:29799', '1:29817', '1:29874', '1:30458', '1:31917', '1:32088', '1:67957', '1:71164', '1:71207', '1:71272', '1:61299', '1:93720', '1:70963', '1:72832', '1:25046', '1:22872', '1:39476', '1:9568', '1:9618', '1:10871', '1:81587', '1:23828', '1:25102', '1:14150', '1:14299', '1:23648', '1:24400', '1:26176', '1:74986', '1:52626', '1:52853', '1:52981', '1:53129', '1:53592', '1:65157', '1:64891', '1:64986', '1:65360', '1:1373', '1:1553', '1:1810', '1:1917', '1:1965', '1:2977', '1:24596', '1:5213', '1:5327', '1:5588', '1:23844', '1:27216', '1:27272', '1:27337', '1:27354', '1:27565', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/509597B0-AEFB-E911-878E-002590DE3A92.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90776FDE-BDFB-E911-84D1-40F2E9C6ADBA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F6B93E96-C5FB-E911-9974-3417EBE7047A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BA100FA2-4EFE-E911-96A3-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F43443B4-ECFC-E911-BEB6-24BE05C4D8F1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BAA9281E-48FE-E911-B284-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/82DC5317-C9FE-E911-A8D4-0030487BB52E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A904563-4D00-EA11-8187-002481CFE1EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B29D7EA4-74FF-E911-97CA-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/56EB785D-ADFE-E911-8744-0CC47A5FC281.root']);