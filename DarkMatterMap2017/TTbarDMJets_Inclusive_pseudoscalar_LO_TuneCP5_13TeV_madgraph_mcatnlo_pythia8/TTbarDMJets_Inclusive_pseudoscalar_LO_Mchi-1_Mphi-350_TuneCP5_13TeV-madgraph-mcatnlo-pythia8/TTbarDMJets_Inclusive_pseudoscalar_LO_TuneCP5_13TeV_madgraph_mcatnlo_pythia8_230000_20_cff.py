import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:29438', '1:29219', '1:30069', '1:30189', '1:73715', '1:72661', '1:72676', '1:72684', '1:84480', '1:88577', '1:97207', '1:73274', '1:76385', '1:76789', '1:78255', '1:78428', '1:13362', '1:44622', '1:47560', '1:47895', '1:73972', '1:71236', '1:74021', '1:41671', '1:49910', '1:54545', '1:56041', '1:55393', '1:86136', '1:104566', '1:104933', '1:104029', '1:2461', '1:16111', '1:16734', '1:16756', '1:23058', '1:17324', '1:17338', '1:17350', '1:17417', '1:28068', '1:28089', '1:29382', '1:29519', '1:29566', '1:29649', '1:29657', '1:29738', '1:29818', '1:30001', '1:47711', '1:47799', '1:62756', '1:62761', '1:62949', '1:44894', '1:45029', '1:45120', '1:45565', '1:47122', '1:47826', '1:90932', '1:92728', '1:47357', '1:47578', '1:89993', '1:80965', '1:90166', '1:98285', '1:98702', '1:81404', '1:98593', '1:98754', '1:98862', '1:104267', '1:7077', '1:10342', '1:2915', '1:5491', '1:15733', '1:13864', '1:28463', '1:28756', '1:29889', '1:32445', '1:42741', '1:47585', '1:47690', '1:49050', '1:54598', '1:51895', '1:54820', '1:96797', '1:78307', '1:65108', '1:72654', '1:98419', '1:105493', '1:105723', '1:96038', '1:12139', '1:7712', '1:44165', '1:79018', '1:78668', '1:82744', '1:80214', '1:82813', '1:84176', '1:17096', '1:32489', '1:48304', '1:48736', '1:51784', '1:55449', '1:58532', '1:91206', '1:92372', '1:103821', '1:103881', '1:103987', '1:105140', '1:105180', '1:105329', '1:103747', '1:105775', '1:106132', '1:92594', '1:92882', '1:78265', '1:81257', '1:81646', '1:72931', '1:102505', '1:105873', '1:22129', '1:22269', '1:22445', '1:22439', '1:40940', '1:41002', '1:41183', '1:41160', '1:41335', '1:59106', '1:59675', '1:45916', '1:47248', '1:47278', '1:65447', '1:65854', '1:65887', '1:93764', '1:94885', '1:94913', '1:12690', '1:12734', '1:27395', '1:19147', '1:19181', '1:19279', '1:19294', '1:19321', '1:19326', '1:19347', '1:19372', '1:19481', '1:40706', '1:84649', '1:85441', '1:85451', '1:86088', '1:86412', '1:86461', '1:15314', '1:15859', '1:15778', '1:16015', '1:24933', '1:25712', '1:25841', '1:25920', '1:25142', '1:25172', '1:25195', '1:25473', '1:25624', '1:24642', '1:24747', '1:23965', '1:25094', '1:60680', '1:77090', '1:78140', '1:40956', '1:45480', '1:97845', '1:82118', '1:82424', '1:90696', '1:90724', '1:91786', '1:103649', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0AA4F2C-B6FB-E911-BABD-3417EBE70078.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA780643-AC10-EA11-8326-008CFAFBFB7C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5A31D770-76FC-E911-BA45-0CC47AFF0258.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/46E9ED6C-BB0A-EA11-AC8D-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72C119DC-BBF2-E911-B71C-1866DA85DFC0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2812357-95F8-E911-84BD-A4BF0126C074.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/28CA8532-26F8-E911-A6B7-0CC47AA98F98.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BEC88789-04FA-E911-82A0-0CC47A706CF0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D80C91DC-88FC-E911-8EA8-0CC47AFB8104.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E4D8B56-20F4-E911-AE7F-3C4A92F7DD14.root']);