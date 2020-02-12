import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:5237', '1:5249', '1:5516', '1:28362', '1:487', '1:831', '1:9991', '1:826', '1:2391', '1:2535', '1:3383', '1:8364', '1:28560', '1:2522', '1:3260', '1:1160', '1:7217', '1:7974', '1:10310', '1:8696', '1:423', '1:2376', '1:1656', '1:33024', '1:6040', '1:25806', '1:25812', '1:29259', '1:4115', '1:6391', '1:10910', '1:7193', '1:3305', '1:3337', '1:7025', '1:26153', '1:5887', '1:7326', '1:28430', '1:809', '1:2561', '1:5099', '1:2711', '1:2443', '1:1438', '1:9476', '1:32057', '1:35909', '1:35102', '1:35110', '1:35206', '1:30320', '1:10614', '1:6134', '1:8877', '1:8907', '1:26099', '1:26076', '1:28021', '1:33719', '1:31728', '1:31861', '1:28224', '1:32785', '1:34018', '1:27637', '1:25648', '1:27106', '1:32047', '1:25326', '1:25335', '1:34990', '1:35584', '1:35596', '1:35652', '1:221', '1:225', '1:2228', '1:2247', '1:35147', '1:35137', '1:2175', '1:4456', '1:4618', '1:6882', '1:27159', '1:27167', '1:27686', '1:27176', '1:27335', '1:35591', '1:35904', '1:5500', '1:8934', '1:7530', '1:7592', '1:7603', '1:7604', '1:7666', '1:7825', '1:30117', '1:32165', '1:1119', '1:4370', '1:4655', '1:4723', '1:8041', '1:8067', '1:6997', '1:34944', '1:34946', '1:35209', '1:35281', '1:35339', '1:28260', '1:28276', '1:32222', '1:32383', '1:32673', '1:4270', '1:8674', '1:3600', '1:428', '1:3017', '1:26120', '1:505', '1:3273', '1:921', '1:25012', '1:25013', '1:1944', '1:1992', '1:28729', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/8CC573B4-D113-EA11-9998-901B0E542962.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B8C77942-A60E-EA11-AD67-0CC47A7E68AA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/925A0462-EE0E-EA11-82B0-00266CF3E248.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/8C61D84E-1210-EA11-B859-A4BF011258C8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/E8507146-790E-EA11-BB15-3417EBE7062D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/96D98A15-8114-EA11-A406-D4AE52901D6F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/42398EAC-8F14-EA11-9925-14187751C030.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/66967E0B-930E-EA11-8C76-A4BF012881D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/40EF351F-4F0E-EA11-B140-0CC47A7FC746.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/4058AFAB-E40E-EA11-AC71-98039B3B01D2.root']);