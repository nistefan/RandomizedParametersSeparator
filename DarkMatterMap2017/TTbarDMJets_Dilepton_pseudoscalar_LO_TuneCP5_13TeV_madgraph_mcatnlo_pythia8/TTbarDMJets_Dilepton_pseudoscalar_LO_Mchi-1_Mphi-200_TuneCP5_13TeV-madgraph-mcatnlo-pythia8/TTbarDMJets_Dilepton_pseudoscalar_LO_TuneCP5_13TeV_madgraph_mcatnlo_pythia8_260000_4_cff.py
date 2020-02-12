import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11073', '1:11604', '1:11730', '1:12040', '1:22303', '1:18204', '1:18278', '1:16714', '1:18911', '1:20221', '1:20388', '1:5532', '1:4480', '1:8290', '1:10073', '1:8747', '1:12289', '1:3825', '1:5286', '1:26499', '1:29906', '1:29843', '1:26867', '1:2292', '1:5233', '1:5410', '1:9100', '1:26638', '1:34676', '1:30852', '1:32770', '1:33271', '1:33351', '1:36192', '1:36470', '1:36752', '1:37264', '1:36822', '1:36964', '1:36971', '1:194', '1:210', '1:1563', '1:5298', '1:9112', '1:2265', '1:28172', '1:28292', '1:3300', '1:3135', '1:29693', '1:29742', '1:29810', '1:31432', '1:29616', '1:30000', '1:7713', '1:3292', '1:3344', '1:28978', '1:4590', '1:6914', '1:29110', '1:31412', '1:8478', '1:25074', '1:28793', '1:8225', '1:6061', '1:6646', '1:6155', '1:6543', '1:26180', '1:23485', '1:23549', '1:23626', '1:35899', '1:78', '1:1097', '1:6546', '1:29685', '1:6952', '1:2775', '1:7016', '1:31019', '1:29375', '1:2282', '1:9164', '1:29928', '1:1270', '1:1409', '1:27877', '1:32299', '1:27276', '1:26302', '1:28961', '1:36419', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/C05C8FB4-7916-EA11-94B4-3CFDFE639780.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8CE3EFE-5C17-EA11-9FAC-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/38055D26-8217-EA11-8707-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2013AFAC-6317-EA11-8CAA-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/FAF900D4-2917-EA11-A923-24BE05C68671.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/94A6ED48-3F18-EA11-A4C4-0CC47AD9908C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/CC0A7D01-3A1B-EA11-A119-0CC47A4DEF48.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/AAE9111D-211C-EA11-8C33-0CC47A5FC495.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/08CA66AF-FB16-EA11-8C68-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D63E1E93-7217-EA11-A37B-B8CA3A70A410.root']);