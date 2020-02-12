import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:57126', '1:59498', '1:18885', '1:28636', '1:30208', '1:36235', '1:36240', '1:36242', '1:36146', '1:36203', '1:59506', '1:64065', '1:64243', '1:45714', '1:55811', '1:55883', '1:55991', '1:59828', '1:82039', '1:80543', '1:49340', '1:51610', '1:81809', '1:79908', '1:82767', '1:78875', '1:33049', '1:33083', '1:33096', '1:33184', '1:658', '1:717', '1:538', '1:6056', '1:7585', '1:8891', '1:7768', '1:8180', '1:12439', '1:8326', '1:29841', '1:30596', '1:17431', '1:73829', '1:78129', '1:66135', '1:51313', '1:51685', '1:55421', '1:80242', '1:13406', '1:8366', '1:10153', '1:12736', '1:33275', '1:33330', '1:33577', '1:37077', '1:33433', '1:33743', '1:40038', '1:40096', '1:30162', '1:39759', '1:42419', '1:44662', '1:61585', '1:38383', '1:38399', '1:38386', '1:38603', '1:38736', '1:38750', '1:80665', '1:13526', '1:2118', '1:10501', '1:11868', '1:16152', '1:16857', '1:12554', '1:15495', '1:49384', '1:50904', '1:63075', '1:80082', '1:80331', '1:80462', '1:80453', '1:80752', '1:58700', '1:60121', '1:1514', '1:15507', '1:14994', '1:25298', '1:23662', '1:24239', '1:25428', '1:25962', '1:12464', '1:33280', '1:22449', '1:60401', '1:94451', '1:94924', '1:95337', '1:17920', '1:19778', '1:35100', '1:64513', '1:78915', '1:60327', '1:60559', '1:35393', '1:35395', '1:35397', '1:35332', '1:38150', '1:50998', '1:63038', '1:62634', '1:94851', '1:57920', '1:61881', '1:58400', '1:57691', '1:57934', '1:62613', '1:31940', '1:31955', '1:26417', '1:26548', '1:36093', '1:36791', '1:42916', '1:40065', '1:51985', '1:64133', '1:51268', '1:40968', '1:41760', '1:52882', '1:47481', '1:7725', '1:23534', '1:26471', '1:9883', '1:10514', '1:25218', '1:12810', '1:13544', '1:14636', '1:14821', '1:3070', '1:12558', '1:39794', '1:27408', '1:47386', '1:31723', '1:35489', '1:37946', '1:37965', '1:14830', '1:33702', '1:22987', '1:27913', '1:28180', '1:19803', '1:53907', '1:30809', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/8E868E51-3918-EA11-8BDA-549F35AC7E8A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/6C4C1C19-2218-EA11-9016-FA163EB3E67B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/3407F705-A617-EA11-BF6D-FA163E3FEA2A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/B612A17D-4B18-EA11-8C76-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/7C99C8B6-E917-EA11-B271-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/F09390AA-F117-EA11-809E-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/FE05A194-3518-EA11-B9D2-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/84F25B88-BA17-EA11-A4B9-FA163E187AF5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/0C0A6865-BE17-EA11-A98A-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/7A0C5C94-3918-EA11-A400-0CC47A57CCE8.root']);