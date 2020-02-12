import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:13161', '1:14480', '1:17875', '1:22024', '1:22869', '1:22925', '1:20716', '1:23134', '1:20829', '1:23117', '1:17584', '1:22078', '1:13618', '1:11616', '1:11846', '1:13500', '1:13604', '1:24108', '1:21484', '1:24042', '1:21477', '1:24077', '1:21491', '1:12786', '1:18262', '1:13984', '1:17555', '1:24064', '1:24153', '1:24238', '1:24321', '1:18596', '1:14196', '1:16415', '1:14231', '1:17749', '1:18969', '1:18393', '1:18648', '1:24803', '1:24812', '1:16847', '1:21423', '1:24704', '1:12071', '1:12117', '1:17617', '1:22694', '1:12622', '1:12647', '1:17548', '1:11791', '1:13223', '1:22091', '1:17511', '1:17928', '1:22649', '1:22896', '1:22871', '1:13321', '1:13377', '1:13378', '1:13864', '1:13069', '1:13037', '1:11258', '1:17159', '1:17302', '1:13906', '1:17673', '1:15646', '1:19058', '1:19149', '1:22465', '1:21884', '1:21496', '1:21759', '1:20489', '1:20631', '1:20741', '1:20906', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/AA555549-5912-EA11-8B41-3417EBE7063F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/0E098A33-3703-EA11-871C-0CC47A4D7650.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7C71D678-5A04-EA11-8EE7-0CC47A4D7626.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/96A81BD1-2810-EA11-96F8-0CC47A7C34A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/48005C4A-5912-EA11-A211-002590495B2C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/8C290DDD-3DFF-E911-9EE2-24BE05C49891.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/2E76A192-7DFF-E911-9EC9-008CFA110C70.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/98E4FECD-5812-EA11-A767-00259029E81A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/42071C23-1F03-EA11-9133-48FD8EE73AEF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/9E09CF11-7101-EA11-A096-0242AC130002.root']);