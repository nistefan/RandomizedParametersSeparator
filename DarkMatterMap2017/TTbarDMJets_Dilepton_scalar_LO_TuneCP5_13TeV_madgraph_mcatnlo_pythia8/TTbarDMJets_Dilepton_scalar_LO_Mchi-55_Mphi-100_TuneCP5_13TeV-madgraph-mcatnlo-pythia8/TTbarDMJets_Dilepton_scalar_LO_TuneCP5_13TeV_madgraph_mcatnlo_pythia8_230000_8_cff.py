import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:436', '1:509', '1:1089', '1:1220', '1:1830', '1:1878', '1:4653', '1:2533', '1:2541', '1:7296', '1:20381', '1:10208', '1:16939', '1:105163', '1:104955', '1:97395', '1:105833', '1:16085', '1:16458', '1:24590', '1:79080', '1:79213', '1:79039', '1:79285', '1:79419', '1:96868', '1:96872', '1:96967', '1:96664', '1:96700', '1:96850', '1:60384', '1:59613', '1:59631', '1:59838', '1:59855', '1:59866', '1:84678', '1:84858', '1:91732', '1:91820', '1:80807', '1:81084', '1:80814', '1:80869', '1:80873', '1:96104', '1:96378', '1:96425', '1:96445', '1:96532', '1:96642', '1:96768', '1:96776', '1:97290', '1:98893', '1:91642', '1:91926', '1:99381', '1:99719', '1:99770', '1:37523', '1:34003', '1:46174', '1:55954', '1:78481', '1:83647', '1:87721', '1:85490', '1:75549', '1:75635', '1:76786', '1:76799', '1:12367', '1:15203', '1:15483', '1:15489', '1:17105', '1:18179', '1:18370', '1:27232', '1:27304', '1:27313', '1:27328', '1:27554', '1:28688', '1:28673', '1:41600', '1:18469', '1:18501', '1:18585', '1:19537', '1:19758', '1:21328', '1:21655', '1:21278', '1:17415', '1:32969', '1:33399', '1:33486', '1:20602', '1:20683', '1:20920', '1:21032', '1:21097', '1:40315', '1:40524', '1:56326', '1:61472', '1:62485', '1:62490', '1:62614', '1:44518', '1:41148', '1:41159', '1:41183', '1:44252', '1:44395', '1:45437', '1:45975', '1:45990', '1:47166', '1:47178', '1:48157', '1:48167', '1:48171', '1:48295', '1:48336', '1:4066', '1:4101', '1:4124', '1:4197', '1:4270', '1:4276', '1:16149', '1:47666', '1:47720', '1:47770', '1:47865', '1:47918', '1:52905', '1:52944', '1:53252', '1:66457', '1:64724', '1:64933', '1:65124', '1:65214', '1:65261', '1:83974', '1:81619', '1:84133', '1:85391', '1:86387', '1:86733', '1:86757', '1:86678', '1:105452', '1:105751', '1:26591', '1:26510', '1:32203', '1:28589', '1:34625', '1:71834', '1:73469', '1:87617', '1:97430', '1:404', '1:2514', '1:2714', '1:876', '1:1449', '1:3296', '1:769', '1:17279', '1:17827', '1:19138', '1:20529', '1:19509', '1:27288', '1:27622', '1:19614', '1:34823', '1:27826', '1:33062', '1:32700', '1:35384', '1:38048', '1:34598', '1:36680', '1:38994', '1:45116', '1:36971', '1:42277', '1:88239', '1:92989', '1:93530', '1:96081', '1:43144', '1:45025', '1:43183', '1:43280', '1:32040', '1:32519', '1:32715', '1:52222', '1:51842', '1:51927', '1:51957', '1:52451', '1:49600', '1:49943', '1:50829', '1:62857', '1:63326', '1:63547', '1:67331', '1:60104', '1:60162', '1:58332', '1:62938', '1:78717', '1:100331', '1:104353', '1:98010', '1:5366', '1:5627', '1:7306', '1:8224', '1:10435', '1:10494', '1:10528', '1:12352', '1:12393', '1:12401', '1:12448', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E25E124-31F7-E911-BE4E-0CC47A1E0DC2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCE60212-4D10-EA11-BEE3-90E2BAD5729C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C9C3A0A-7FFF-E911-8CD0-0CC47A4DEDD4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90D49EF7-13F6-E911-9659-38EAA78E2C94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D8B5CBBC-35F0-E911-94CF-1418774A25AB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E06943C6-D5EF-E911-A278-10983627C3C1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1ABC4644-64F4-E911-A4E7-FA163E84EE9A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AF65E7A-6EF3-E911-9E38-141877641875.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0A2F042B-71EF-E911-9535-0CC47AF9739E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AA4C6F18-8AF7-E911-80DC-0CC47AD9901C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5EAB8AB1-6810-EA11-9F96-008CFA197D98.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/10AE8E18-9802-EA11-8C36-B083FED138B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0407705F-5610-EA11-BCA2-0CC47AD98CEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5E63A65D-5B07-EA11-9816-0CC47A7C345E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EA78600-8003-EA11-98EB-405CFDFF480E.root']);