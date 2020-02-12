import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:25148', '1:25502', '1:25608', '1:27279', '1:35791', '1:12159', '1:12270', '1:12907', '1:12988', '1:18726', '1:18082', '1:20103', '1:20128', '1:20136', '1:20230', '1:18158', '1:18079', '1:18201', '1:15231', '1:15265', '1:23262', '1:20510', '1:20540', '1:20691', '1:20805', '1:20210', '1:1107', '1:28415', '1:29413', '1:29683', '1:7554', '1:33792', '1:10627', '1:132', '1:307', '1:3887', '1:9204', '1:8352', '1:26089', '1:29252', '1:30827', '1:32986', '1:25483', '1:27087', '1:25676', '1:25727', '1:25471', '1:25161', '1:32102', '1:30858', '1:30495', '1:30516', '1:30862', '1:9964', '1:25216', '1:28465', '1:2636', '1:2773', '1:28191', '1:6674', '1:26353', '1:26436', '1:26441', '1:33277', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/569B4D10-211C-EA11-A715-FA163E37F419.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/30550AAC-B81A-EA11-BAC1-0CC47A5FC2A1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2E4A544D-FB1C-EA11-976A-AC1F6BAC7C10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/60FE314E-FF17-EA11-BF96-0025905C53A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/7461BAF6-B81A-EA11-B8C8-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/281F6DB4-B81A-EA11-ABBF-FA163EB32F6D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/68FB54A5-D319-EA11-9BF2-0CC47A2AED8A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D4CB8FB4-D419-EA11-8898-E0071B6C9DF0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/44A61A10-EA1E-EA11-B484-AC1F6B1AF194.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/74DE8B80-0B18-EA11-9093-3CFDFE63F840.root']);