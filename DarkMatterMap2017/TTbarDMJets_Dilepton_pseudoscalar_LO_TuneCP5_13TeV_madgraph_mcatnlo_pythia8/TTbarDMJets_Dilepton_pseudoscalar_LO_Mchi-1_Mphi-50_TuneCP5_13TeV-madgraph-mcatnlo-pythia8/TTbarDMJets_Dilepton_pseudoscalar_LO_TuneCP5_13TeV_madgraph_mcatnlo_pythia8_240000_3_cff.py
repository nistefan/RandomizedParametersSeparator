import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11925', '1:11990', '1:13041', '1:13122', '1:13156', '1:11451', '1:11541', '1:11545', '1:17742', '1:17870', '1:17908', '1:17910', '1:17361', '1:17388', '1:17453', '1:17465', '1:17733', '1:17835', '1:17924', '1:18000', '1:20984', '1:23026', '1:23066', '1:23311', '1:23368', '1:23377', '1:11176', '1:20655', '1:17096', '1:17825', '1:17608', '1:17736', '1:22339', '1:11041', '1:20843', '1:13881', '1:13933', '1:13957', '1:11612', '1:13213', '1:13309', '1:13521', '1:13610', '1:13650', '1:21296', '1:21297', '1:13165', '1:11672', '1:11943', '1:13076', '1:13093', '1:21285', '1:21443', '1:21989', '1:21902', '1:21920', '1:21379', '1:21376', '1:21318', '1:21381', '1:21295', '1:21396', '1:21413', '1:21600', '1:21999', '1:21338', '1:21575', '1:21903', '1:21929', '1:21993', '1:24144', '1:21492', '1:12530', '1:18261', '1:18418', '1:13060', '1:13206', '1:17278', '1:17294', '1:17684', '1:17688', '1:17849', '1:21551', '1:24082', '1:18371', '1:18893', '1:18910', '1:18680', '1:18687', '1:18382', '1:18948', '1:18977', '1:14012', '1:14014', '1:14875', '1:14210', '1:16398', '1:16518', '1:18501', '1:18844', '1:24375', '1:24706', '1:24798', '1:24057', '1:16087', '1:16782', '1:21841', '1:24647', '1:22757', '1:12998', '1:22643', '1:22835', '1:17313', '1:13405', '1:17181', '1:17211', '1:17561', '1:13948', '1:11608', '1:11862', '1:13552', '1:13872', '1:12839', '1:18728', '1:12352', '1:18014', '1:18641', '1:17410', '1:22046', '1:22063', '1:22094', '1:22928', '1:13871', '1:20171', '1:12018', '1:17045', '1:22039', '1:22913', '1:13151', '1:17013', '1:23112', '1:17317', '1:23446', '1:23422', '1:13545', '1:13899', '1:13611', '1:13897', '1:17166', '1:15336', '1:19249', '1:15014', '1:19026', '1:20711', '1:20728', '1:20963', '1:20978', '1:16979', '1:21284', '1:21513', '1:21588', '1:21489', '1:21580', '1:21766', '1:20496', '1:23924', '1:23769', '1:23801', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/AA555549-5912-EA11-8B41-3417EBE7063F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/0E098A33-3703-EA11-871C-0CC47A4D7650.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7C71D678-5A04-EA11-8EE7-0CC47A4D7626.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/96A81BD1-2810-EA11-96F8-0CC47A7C34A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/48005C4A-5912-EA11-A211-002590495B2C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/8C290DDD-3DFF-E911-9EE2-24BE05C49891.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/2E76A192-7DFF-E911-9EC9-008CFA110C70.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/98E4FECD-5812-EA11-A767-00259029E81A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/42071C23-1F03-EA11-9133-48FD8EE73AEF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/9E09CF11-7101-EA11-A096-0242AC130002.root']);