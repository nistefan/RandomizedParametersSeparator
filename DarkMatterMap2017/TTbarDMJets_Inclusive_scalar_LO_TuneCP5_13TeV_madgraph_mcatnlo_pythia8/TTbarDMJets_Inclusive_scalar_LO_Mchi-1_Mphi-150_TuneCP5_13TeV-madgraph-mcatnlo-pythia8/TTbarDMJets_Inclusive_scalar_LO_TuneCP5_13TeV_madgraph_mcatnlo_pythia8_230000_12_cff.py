import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2807', '1:2880', '1:2953', '1:24030', '1:49432', '1:49612', '1:49721', '1:49761', '1:50178', '1:50721', '1:50754', '1:51269', '1:51388', '1:10246', '1:10294', '1:10353', '1:14605', '1:67668', '1:67682', '1:67387', '1:67523', '1:67557', '1:67716', '1:67839', '1:72716', '1:70827', '1:53540', '1:56339', '1:55694', '1:55706', '1:55788', '1:55812', '1:55897', '1:55908', '1:61268', '1:62025', '1:62458', '1:62420', '1:62792', '1:62945', '1:67083', '1:55808', '1:55847', '1:55857', '1:56001', '1:62065', '1:62081', '1:62250', '1:30496', '1:30621', '1:31909', '1:32103', '1:50134', '1:50258', '1:50478', '1:50496', '1:50902', '1:59451', '1:59574', '1:60011', '1:64611', '1:64856', '1:68084', '1:68195', '1:68387', '1:68516', '1:70883', '1:71313', '1:71524', '1:77191', '1:30215', '1:54248', '1:56585', '1:57268', '1:55378', '1:55402', '1:55419', '1:55431', '1:55714', '1:55938', '1:58991', '1:59089', '1:59358', '1:74110', '1:80837', '1:31596', '1:31657', '1:31853', '1:31913', '1:31961', '1:96011', '1:96019', '1:94530', '1:94917', '1:94999', '1:95048', '1:95057', '1:96347', '1:96461', '1:96555', '1:97089', '1:96785', '1:55123', '1:55125', '1:55560', '1:94439', '1:97602', '1:98603', '1:100444', '1:94606', '1:97991', '1:98377', '1:98385', '1:98411', '1:96083', '1:96597', '1:96726', '1:16110', '1:17455', '1:17603', '1:39957', '1:32144', '1:32377', '1:32463', '1:32556', '1:37965', '1:38101', '1:46350', '1:46292', '1:46523', '1:46553', '1:46757', '1:46653', '1:46703', '1:46926', '1:46957', '1:49100', '1:72789', '1:72797', '1:74294', '1:74995', '1:75471', '1:70993', '1:71171', '1:71222', '1:71349', '1:76818', '1:77201', '1:101727', '1:75814', '1:76358', '1:75824', '1:78036', '1:78166', '1:78247', '1:78640', '1:88071', '1:88653', '1:95185', '1:100860', '1:96518', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FAC034E1-9601-EA11-9760-509A4C9EF923.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E078E352-23FD-E911-A003-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F61819D6-3913-EA11-B31C-FA163E8730E3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6329619-8EFC-E911-8FA7-38EAA78D8AF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/66CDCE78-55FD-E911-9168-98039B3B003A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/18954DF4-27FD-E911-8530-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90B4387D-20FE-E911-8A41-0CC47A7E6972.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/54A816C3-3913-EA11-AE8E-001E67A3FBAA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C2FD6BB4-3913-EA11-9241-008CFAC94014.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F655D1E5-3913-EA11-9544-B083FED12B5C.root']);