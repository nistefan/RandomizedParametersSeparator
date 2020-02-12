import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11584', '1:11748', '1:11945', '1:11950', '1:11933', '1:13064', '1:13090', '1:13266', '1:13325', '1:13348', '1:13390', '1:13440', '1:13516', '1:13748', '1:13161', '1:13865', '1:13912', '1:13953', '1:13851', '1:13862', '1:22061', '1:25470', '1:25549', '1:25561', '1:25522', '1:25898', '1:25707', '1:29340', '1:29449', '1:29455', '1:29467', '1:29473', '1:29902', '1:30070', '1:30064', '1:30076', '1:31407', '1:30151', '1:30135', '1:101979', '1:11846', '1:13137', '1:22568', '1:22571', '1:29350', '1:29605', '1:29618', '1:29172', '1:29650', '1:30188', '1:30238', '1:30270', '1:30328', '1:30347', '1:30353', '1:30447', '1:30378', '1:30386', '1:30632', '1:31351', '1:31427', '1:31434', '1:31513', '1:31597', '1:31917', '1:31926', '1:31949', '1:31659', '1:31615', '1:89874', '1:89929', '1:90022', '1:90033', '1:101013', '1:90018', '1:101314', '1:22102', '1:13853', '1:89830', '1:89848', '1:101008', '1:101023', '1:101036', '1:101043', '1:90193', '1:101300', '1:101322', '1:101344', '1:101346', '1:101364', '1:101389', '1:89906', '1:89939', '1:90004', '1:90317', '1:90701', '1:90315', '1:90696', '1:90710', '1:90807', '1:90808', '1:90916', '1:25015', '1:25036', '1:25064', '1:25117', '1:25179', '1:25203', '1:25321', '1:25328', '1:89850', '1:89862', '1:89873', '1:90510', '1:90561', '1:90589', '1:29118', '1:29214', '1:29270', '1:29130', '1:90056', '1:90138', '1:90188', '1:90189', '1:90199', '1:101413', '1:90234', '1:90349', '1:90446', '1:90444', '1:90514', '1:90529', '1:90550', '1:90597', '1:29113', '1:29357', '1:29361', '1:29367', '1:29373', '1:29375', '1:29377', '1:29382', '1:29698', '1:29626', '1:29929', '1:29943', '1:29960', '1:30000', '1:30041', '1:30044', '1:31540', '1:31563', '1:31574', '1:31673', '1:31681', '1:31695', '1:31698', '1:31703', '1:31718', '1:11988', '1:11995', '1:13635', '1:13733', '1:13932', '1:13604', '1:13935', '1:22239', '1:22974', '1:89723', '1:89748', '1:89798', '1:101115', '1:101557', '1:101555', '1:30850', '1:31970', '1:89077', '1:89132', '1:89009', '1:89476', '1:89368', '1:89728', '1:101205', '1:101214', '1:90372', '1:89654', '1:89161', '1:89263', '1:89289', '1:89697', '1:89778', '1:89253', '1:89657', '1:90008', '1:89435', '1:101241', '1:101224', '1:101232', '1:11370', '1:11407', '1:11278', '1:11868', '1:11978', '1:11981', '1:11994', '1:13024', '1:25608', '1:25122', '1:25126', '1:25280', '1:25821', '1:25838', '1:29161', '1:31727', '1:31804', '1:31857', '1:90412', '1:101433', '1:22175', '1:22176', '1:22978', '1:25274', '1:25275', '1:101122', '1:25954', '1:25956', '1:30502', '1:89800', '1:90975', '1:101550', '1:101009', '1:89653', '1:11577', '1:11619', '1:11628', '1:11688', '1:11712', '1:11789', '1:11696', '1:11706', '1:22290', '1:22542', '1:22566', '1:22592', '1:22603', '1:22684', '1:22691', '1:22395', '1:22501', '1:11183', '1:11598', '1:11226', '1:11265', '1:11286', '1:11699', '1:13113', '1:13228', '1:13313', '1:13265', '1:13542', '1:13614', '1:13693', '1:13697', '1:13825', '1:13830', '1:30904', '1:30920', '1:31289', '1:31235', '1:31240', '1:31368', '1:89977', '1:101039', '1:101078', '1:101074', '1:101254', '1:90804', '1:90925', '1:90940', '1:101854', '1:22139', '1:22137', '1:22444', '1:25575', '1:25584', '1:25517', '1:25572', '1:25643', '1:25690', '1:25703', '1:29058', '1:29060', '1:29117', '1:29204', '1:29098', '1:29503', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/BA08AC92-32EF-E911-82D8-441EA1616DEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/1A47AC00-7B03-EA11-9EE6-0CC47AF973C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DA862DF2-9F11-EA11-A5FB-C4346BC75558.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DC992538-9910-EA11-BF7F-0CC47A5FC281.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/163497F8-2D11-EA11-A132-6C2B599A050D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/0A3BC253-8411-EA11-A6F0-D8D385AF891A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/562C1852-3411-EA11-A53F-8CDCD4A9A484.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/E6105D38-A311-EA11-9524-0CC47A7E6A5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D86A4CB2-9014-EA11-8CA9-F01FAFE5CF52.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C0549F53-A714-EA11-8560-782BCB46E733.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/70D29667-41FB-E911-818C-38EAA78D8ACC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/B8C911EE-29F0-E911-8638-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/0E7BC3B3-0AFA-E911-8213-98039B3B01B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DE54B8C9-DA10-EA11-89A8-A4BF01125538.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/2ABD4E37-8F03-EA11-815A-1866DA86CCDF.root']);