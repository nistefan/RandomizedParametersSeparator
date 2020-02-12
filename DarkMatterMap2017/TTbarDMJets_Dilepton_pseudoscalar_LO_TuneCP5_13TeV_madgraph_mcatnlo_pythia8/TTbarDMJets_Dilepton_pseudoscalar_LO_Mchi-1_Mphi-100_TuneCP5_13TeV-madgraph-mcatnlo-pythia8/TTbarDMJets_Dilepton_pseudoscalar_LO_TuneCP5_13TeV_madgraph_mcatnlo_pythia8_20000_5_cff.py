import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:25704', '1:30167', '1:30176', '1:25019', '1:25904', '1:30014', '1:4138', '1:4163', '1:4656', '1:4672', '1:7377', '1:10953', '1:4154', '1:4157', '1:4334', '1:4379', '1:4646', '1:34421', '1:30897', '1:32819', '1:33357', '1:33365', '1:33370', '1:33376', '1:33388', '1:33389', '1:33419', '1:2936', '1:2982', '1:26386', '1:10754', '1:31976', '1:33582', '1:10406', '1:10908', '1:33821', '1:10109', '1:10111', '1:6995', '1:9412', '1:32656', '1:30121', '1:30879', '1:32186', '1:98', '1:659', '1:7707', '1:7901', '1:9368', '1:29486', '1:29487', '1:33862', '1:29223', '1:29228', '1:29481', '1:29220', '1:29221', '1:3031', '1:3036', '1:3044', '1:3198', '1:3214', '1:3972', '1:3977', '1:6337', '1:6338', '1:6347', '1:6354', '1:6357', '1:4104', '1:4108', '1:4206', '1:4193', '1:4907', '1:25517', '1:27544', '1:3934', '1:5089', '1:5090', '1:27530', '1:27579', '1:29183', '1:28728', '1:35889', '1:3769', '1:3806', '1:4648', '1:4660', '1:4679', '1:4680', '1:8030', '1:8043', '1:5704', '1:33093', '1:33106', '1:26560', '1:26587', '1:29670', '1:29931', '1:1588', '1:33538', '1:33545', '1:9330', '1:9439', '1:9870', '1:9901', '1:31462', '1:33214', '1:33916', '1:1316', '1:2949', '1:2625', '1:2709', '1:2729', '1:2736', '1:2741', '1:2742', '1:5772', '1:5087', '1:5176', '1:5888', '1:8857', '1:25037', '1:28120', '1:30118', '1:30134', '1:25137', '1:25265', '1:25224', '1:25306', '1:25309', '1:25350', '1:25356', '1:27316', '1:10311', '1:1460', '1:1699', '1:29398', '1:2886', '1:7969', '1:29546', '1:7983', '1:29478', '1:31884', '1:30485', '1:30612', '1:30619', '1:32010', '1:32227', '1:32499', '1:25367', '1:9052', '1:31854', '1:10927', '1:6235', '1:6685', '1:9564', '1:9729', '1:10845', '1:10895', '1:10912', '1:167', '1:955', '1:961', '1:3123', '1:3406', '1:4398', '1:3168', '1:3170', '1:3174', '1:3996', '1:6020', '1:28442', '1:30610', '1:1001', '1:3385', '1:2101', '1:7972', '1:29291', '1:31359', '1:9237', '1:4241', '1:4297', '1:29170', '1:29537', '1:28550', '1:28407', '1:28666', '1:5734', '1:9792', '1:9325', '1:25746', '1:25783', '1:30481', '1:25753', '1:30581', '1:27446', '1:27555', '1:28850', '1:30190', '1:30193', '1:30448', '1:30297', '1:35890', '1:35906', '1:35787', '1:35695', '1:35780', '1:35784', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/14EFC606-9F03-EA11-BEC2-FA163E20CD2B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/82C1E74A-2410-EA11-A821-0CC47AFF24BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/769118EE-1C11-EA11-91F3-0CC47AFF24D6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/50EC5EF4-EC0F-EA11-8370-0025905C9742.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/D0E075EA-80F0-E911-AFE4-FA163E6B2FF6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/EC527D3D-E804-EA11-8C2B-F01FAFE1584B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/908A6B0B-D00C-EA11-8974-FA163EB4F717.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B834EB07-6911-EA11-AEC1-B083FED0FFCF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/4C1F504F-7C0F-EA11-A076-6CC2173D4980.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/E28A9533-7414-EA11-803D-44A8420CC5E0.root']);