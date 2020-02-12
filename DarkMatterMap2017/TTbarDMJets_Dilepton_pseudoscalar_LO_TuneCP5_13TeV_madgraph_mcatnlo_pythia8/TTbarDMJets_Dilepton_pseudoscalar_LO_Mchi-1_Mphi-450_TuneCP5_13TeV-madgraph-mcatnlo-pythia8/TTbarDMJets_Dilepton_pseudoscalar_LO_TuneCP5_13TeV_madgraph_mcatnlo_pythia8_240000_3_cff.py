import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:13015', '1:17754', '1:20936', '1:20557', '1:12933', '1:22537', '1:22437', '1:11599', '1:11305', '1:13052', '1:13794', '1:24066', '1:21411', '1:18323', '1:18654', '1:13840', '1:13945', '1:17199', '1:17883', '1:21495', '1:21519', '1:21774', '1:21786', '1:24137', '1:24395', '1:18829', '1:14418', '1:16926', '1:21414', '1:24201', '1:24268', '1:24445', '1:12251', '1:17933', '1:22414', '1:22453', '1:22614', '1:17430', '1:13997', '1:17005', '1:18898', '1:18737', '1:18862', '1:17773', '1:17939', '1:22164', '1:17052', '1:17109', '1:22690', '1:22591', '1:17296', '1:17366', '1:20071', '1:20593', '1:20545', '1:20207', '1:23098', '1:23461', '1:17937', '1:17938', '1:22656', '1:15770', '1:19032', '1:19031', '1:19485', '1:19883', '1:21859', '1:21505', '1:20504', '1:23805', '1:23972', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/AA555549-5912-EA11-8B41-3417EBE7063F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/0E098A33-3703-EA11-871C-0CC47A4D7650.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7C71D678-5A04-EA11-8EE7-0CC47A4D7626.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/96A81BD1-2810-EA11-96F8-0CC47A7C34A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/48005C4A-5912-EA11-A211-002590495B2C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/8C290DDD-3DFF-E911-9EE2-24BE05C49891.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/2E76A192-7DFF-E911-9EC9-008CFA110C70.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/98E4FECD-5812-EA11-A767-00259029E81A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/42071C23-1F03-EA11-9133-48FD8EE73AEF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/9E09CF11-7101-EA11-A096-0242AC130002.root']);