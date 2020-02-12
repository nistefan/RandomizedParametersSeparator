import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2130', '1:2634', '1:2737', '1:2750', '1:24695', '1:49293', '1:49359', '1:49421', '1:49461', '1:49486', '1:49584', '1:49606', '1:50918', '1:50925', '1:50788', '1:59906', '1:60439', '1:9934', '1:9990', '1:10270', '1:14809', '1:15112', '1:15157', '1:67614', '1:67773', '1:72209', '1:70260', '1:70382', '1:70342', '1:70858', '1:53352', '1:55986', '1:55545', '1:55893', '1:33181', '1:39791', '1:46698', '1:31540', '1:31973', '1:32053', '1:32086', '1:32111', '1:50815', '1:50220', '1:50389', '1:50521', '1:50610', '1:50649', '1:50856', '1:59438', '1:60060', '1:64357', '1:64741', '1:64651', '1:68189', '1:68243', '1:68251', '1:68453', '1:68529', '1:71281', '1:71342', '1:71418', '1:71487', '1:71759', '1:72979', '1:23544', '1:23633', '1:27864', '1:30117', '1:39064', '1:27381', '1:31803', '1:53484', '1:53887', '1:54013', '1:54232', '1:56934', '1:55497', '1:55342', '1:55416', '1:55426', '1:55468', '1:55628', '1:58422', '1:58592', '1:59027', '1:58815', '1:59094', '1:59105', '1:75849', '1:74474', '1:75011', '1:75220', '1:80720', '1:31839', '1:31941', '1:94535', '1:94577', '1:94679', '1:94693', '1:94710', '1:94771', '1:94807', '1:94891', '1:94984', '1:55256', '1:55794', '1:62056', '1:55030', '1:55447', '1:102510', '1:10868', '1:17698', '1:17841', '1:20250', '1:20707', '1:39950', '1:32135', '1:32177', '1:32308', '1:32330', '1:32540', '1:32551', '1:46611', '1:46636', '1:46733', '1:46936', '1:72769', '1:72780', '1:71053', '1:72940', '1:77046', '1:77050', '1:77128', '1:73379', '1:73384', '1:73398', '1:73756', '1:101561', '1:101626', '1:101700', '1:102010', '1:69181', '1:69430', '1:75867', '1:69574', '1:69728', '1:75936', '1:75912', '1:77766', '1:78803', '1:89675', '1:99735', '1:94935', '1:96913', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FAC034E1-9601-EA11-9760-509A4C9EF923.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E078E352-23FD-E911-A003-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F61819D6-3913-EA11-B31C-FA163E8730E3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6329619-8EFC-E911-8FA7-38EAA78D8AF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/66CDCE78-55FD-E911-9168-98039B3B003A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/18954DF4-27FD-E911-8530-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90B4387D-20FE-E911-8A41-0CC47A7E6972.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/54A816C3-3913-EA11-AE8E-001E67A3FBAA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C2FD6BB4-3913-EA11-9241-008CFAC94014.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F655D1E5-3913-EA11-9544-B083FED12B5C.root']);