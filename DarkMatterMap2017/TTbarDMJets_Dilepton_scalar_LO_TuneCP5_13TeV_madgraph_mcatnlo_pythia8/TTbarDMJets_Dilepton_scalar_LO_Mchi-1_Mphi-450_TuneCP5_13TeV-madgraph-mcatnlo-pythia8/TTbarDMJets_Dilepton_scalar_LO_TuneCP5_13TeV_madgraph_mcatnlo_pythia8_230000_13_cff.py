import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:19669', '1:19673', '1:19919', '1:20456', '1:20586', '1:20930', '1:61433', '1:61764', '1:62349', '1:63405', '1:63907', '1:62856', '1:58132', '1:58186', '1:58450', '1:58481', '1:54921', '1:55444', '1:55517', '1:56041', '1:54401', '1:57647', '1:57346', '1:57868', '1:72371', '1:74146', '1:75294', '1:75392', '1:76710', '1:78591', '1:78884', '1:81121', '1:81061', '1:73626', '1:78739', '1:80309', '1:79348', '1:76490', '1:81142', '1:81604', '1:82896', '1:82903', '1:82921', '1:82967', '1:83009', '1:83031', '1:83926', '1:91166', '1:94196', '1:94369', '1:94935', '1:94957', '1:104079', '1:69613', '1:69629', '1:69863', '1:69912', '1:94854', '1:94858', '1:85820', '1:93369', '1:93885', '1:93333', '1:93403', '1:93932', '1:70105', '1:70201', '1:74379', '1:74508', '1:74082', '1:74115', '1:74147', '1:92242', '1:92245', '1:92441', '1:92381', '1:92397', '1:92406', '1:92801', '1:1256', '1:1260', '1:1456', '1:14306', '1:14657', '1:14666', '1:16691', '1:16715', '1:16814', '1:16993', '1:20010', '1:41936', '1:16383', '1:17835', '1:18011', '1:18116', '1:18208', '1:18287', '1:18425', '1:63017', '1:37453', '1:42477', '1:44593', '1:53396', '1:55423', '1:56010', '1:66981', '1:64253', '1:66005', '1:67577', '1:99543', '1:27848', '1:27927', '1:27852', '1:27933', '1:27965', '1:28469', '1:39011', '1:39022', '1:39007', '1:39038', '1:39192', '1:44724', '1:44861', '1:44865', '1:46200', '1:46100', '1:46312', '1:46333', '1:79895', '1:72465', '1:78139', '1:80166', '1:77159', '1:77276', '1:77513', '1:48602', '1:43207', '1:45222', '1:65536', '1:56825', '1:57210', '1:58854', '1:59778', '1:60352', '1:60628', '1:62737', '1:62801', '1:68748', '1:69007', '1:69256', '1:67991', '1:68383', '1:36199', '1:36240', '1:38205', '1:38237', '1:38270', '1:38679', '1:57623', '1:57917', '1:56215', '1:56941', '1:55686', '1:55976', '1:56211', '1:57077', '1:55730', '1:63461', '1:4829', '1:4885', '1:8691', '1:8753', '1:8861', '1:9888', '1:9890', '1:9948', '1:7684', '1:73712', '1:98429', '1:98440', '1:98464', '1:98490', '1:98518', '1:98589', '1:98692', '1:99642', '1:99647', '1:7262', '1:10686', '1:7235', '1:8256', '1:21418', '1:24287', '1:24794', '1:68368', '1:68398', '1:68655', '1:68762', '1:68818', '1:34423', '1:40394', '1:46678', '1:47151', '1:43719', '1:105605', '1:54616', '1:58254', '1:56193', '1:68558', '1:96873', '1:99772', '1:100222', '1:103405', '1:104804', '1:104171', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/922D5DD5-5710-EA11-BE57-AC1F6B595F4E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/58A27CA1-A5F6-E911-8978-0CC47A2B0744.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D6BD0C1E-CCF7-E911-9152-AC1F6B567730.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F030EDC5-1AF3-E911-9B33-002590DE6E6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/82662A5E-23EE-E911-8D5B-0CC47A7FC74A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/54235082-12F4-E911-A7A0-0CC47A1E0DCC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C924ADE-C9EE-E911-8597-C4544423E320.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/120CCF0F-55EF-E911-94EA-24BE05C48821.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5072FB7D-5910-EA11-81FB-28924A33B9FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/629E6C83-AC0D-EA11-83C5-0CC47A5FBE25.root']);