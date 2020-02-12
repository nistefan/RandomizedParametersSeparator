import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:18914', '1:20505', '1:20548', '1:17285', '1:61247', '1:61610', '1:61798', '1:61944', '1:62951', '1:62957', '1:63057', '1:63662', '1:56992', '1:58118', '1:58668', '1:55582', '1:57856', '1:66646', '1:70429', '1:75052', '1:75739', '1:77824', '1:76702', '1:75813', '1:77369', '1:81450', '1:78050', '1:73175', '1:71519', '1:82516', '1:78824', '1:78140', '1:81244', '1:78416', '1:75732', '1:76140', '1:77699', '1:81268', '1:82907', '1:82923', '1:84230', '1:94168', '1:94241', '1:94447', '1:94929', '1:94965', '1:94988', '1:104064', '1:104144', '1:104157', '1:104182', '1:104325', '1:104333', '1:105479', '1:103922', '1:103925', '1:69630', '1:69715', '1:69940', '1:69943', '1:69992', '1:94749', '1:94760', '1:86982', '1:87786', '1:86029', '1:86338', '1:87169', '1:88078', '1:91947', '1:92047', '1:93390', '1:93418', '1:93889', '1:74359', '1:74382', '1:74483', '1:74492', '1:74088', '1:74100', '1:74149', '1:92325', '1:92365', '1:92256', '1:1237', '1:1288', '1:1289', '1:12257', '1:14037', '1:14292', '1:14276', '1:14278', '1:14398', '1:14446', '1:14481', '1:14582', '1:14593', '1:14624', '1:14993', '1:16623', '1:16750', '1:19420', '1:49748', '1:50420', '1:16635', '1:51790', '1:17829', '1:17838', '1:17856', '1:17857', '1:17941', '1:18009', '1:18106', '1:18228', '1:18386', '1:33159', '1:37552', '1:34205', '1:49188', '1:49501', '1:52501', '1:55177', '1:57238', '1:60759', '1:59037', '1:68370', '1:68822', '1:68839', '1:99659', '1:99707', '1:99831', '1:27929', '1:27945', '1:28063', '1:27829', '1:39272', '1:39922', '1:44632', '1:44738', '1:44833', '1:44845', '1:39822', '1:51712', '1:46204', '1:46292', '1:46361', '1:78345', '1:78866', '1:78065', '1:78923', '1:75720', '1:75774', '1:77626', '1:48638', '1:48614', '1:35027', '1:36421', '1:38838', '1:43386', '1:46067', '1:46112', '1:38394', '1:43751', '1:39075', '1:47903', '1:55014', '1:55596', '1:55655', '1:58677', '1:59386', '1:59820', '1:60555', '1:35440', '1:36334', '1:38081', '1:38363', '1:54878', '1:58680', '1:57714', '1:57751', '1:68829', '1:4900', '1:8696', '1:73829', '1:98484', '1:98578', '1:98646', '1:99606', '1:10532', '1:10799', '1:7243', '1:7329', '1:7486', '1:21693', '1:24006', '1:24010', '1:49684', '1:41988', '1:62789', '1:68225', '1:68672', '1:32634', '1:32749', '1:32876', '1:34793', '1:34683', '1:35282', '1:35936', '1:37178', '1:45907', '1:46910', '1:55513', '1:54068', '1:54132', '1:56975', '1:57095', '1:57511', '1:83416', '1:88141', '1:68075', '1:68495', '1:86911', '1:103678', '1:105171', '1:105784', '1:104437', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/922D5DD5-5710-EA11-BE57-AC1F6B595F4E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/58A27CA1-A5F6-E911-8978-0CC47A2B0744.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D6BD0C1E-CCF7-E911-9152-AC1F6B567730.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F030EDC5-1AF3-E911-9B33-002590DE6E6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/82662A5E-23EE-E911-8D5B-0CC47A7FC74A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/54235082-12F4-E911-A7A0-0CC47A1E0DCC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C924ADE-C9EE-E911-8597-C4544423E320.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/120CCF0F-55EF-E911-94EA-24BE05C48821.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5072FB7D-5910-EA11-81FB-28924A33B9FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/629E6C83-AC0D-EA11-83C5-0CC47A5FBE25.root']);