import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:13080', '1:11786', '1:17619', '1:17822', '1:17965', '1:22036', '1:22020', '1:17943', '1:17991', '1:20960', '1:23057', '1:23241', '1:11119', '1:20527', '1:17230', '1:17785', '1:22071', '1:17719', '1:17621', '1:22644', '1:22855', '1:20611', '1:11603', '1:13241', '1:13389', '1:21306', '1:21451', '1:21470', '1:21288', '1:21402', '1:11809', '1:11849', '1:11934', '1:11940', '1:21911', '1:21310', '1:24076', '1:21343', '1:21795', '1:18924', '1:13411', '1:17287', '1:21536', '1:12996', '1:18665', '1:16549', '1:18558', '1:24806', '1:24277', '1:12078', '1:12226', '1:12234', '1:12237', '1:17223', '1:17235', '1:11830', '1:18889', '1:17448', '1:17475', '1:17839', '1:22086', '1:22663', '1:22438', '1:22873', '1:22926', '1:22236', '1:11742', '1:13915', '1:17178', '1:20007', '1:13919', '1:13922', '1:17070', '1:17236', '1:17620', '1:15494', '1:19088', '1:22472', '1:22729', '1:20568', '1:21113', '1:21263', '1:21572', '1:21579', '1:20787', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/AA555549-5912-EA11-8B41-3417EBE7063F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/0E098A33-3703-EA11-871C-0CC47A4D7650.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7C71D678-5A04-EA11-8EE7-0CC47A4D7626.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/96A81BD1-2810-EA11-96F8-0CC47A7C34A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/48005C4A-5912-EA11-A211-002590495B2C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/8C290DDD-3DFF-E911-9EE2-24BE05C49891.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/2E76A192-7DFF-E911-9EC9-008CFA110C70.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/98E4FECD-5812-EA11-A767-00259029E81A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/42071C23-1F03-EA11-9133-48FD8EE73AEF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/9E09CF11-7101-EA11-A096-0242AC130002.root']);