import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:82064', '1:101116', '1:104295', '1:104311', '1:105848', '1:13850', '1:97305', '1:105351', '1:105442', '1:105943', '1:106380', '1:102038', '1:2990', '1:3924', '1:10729', '1:3890', '1:5977', '1:10003', '1:25398', '1:28790', '1:17984', '1:17970', '1:24149', '1:25534', '1:26154', '1:103974', '1:105874', '1:29321', '1:29792', '1:28616', '1:29459', '1:57326', '1:57349', '1:57374', '1:57468', '1:57513', '1:57314', '1:57971', '1:58002', '1:58382', '1:82622', '1:83681', '1:93490', '1:95555', '1:59507', '1:59750', '1:59766', '1:60054', '1:77514', '1:82718', '1:102161', '1:102288', '1:102327', '1:104193', '1:91216', '1:92730', '1:92764', '1:95552', '1:53074', '1:53004', '1:56122', '1:89895', '1:92132', '1:102062', '1:89914', '1:90049', '1:90058', '1:90906', '1:101876', '1:102831', '1:104564', '1:92734', '1:92822', '1:93097', '1:93264', '1:94450', '1:95281', '1:95862', '1:95565', '1:97591', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4227006D-BC12-EA11-89BE-24BE05CEEC21.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4C1DE6F-BC12-EA11-AD6D-C0BFC0E56816.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/74A96878-BC12-EA11-8C73-0CC47AA989BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5ECC5C62-BD12-EA11-BF3F-AC1F6B0DE2EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7851C772-BC12-EA11-BDB4-0025905504C6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2AEF561-BD12-EA11-9091-AC1F6B595F6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B4B1C46E-BD12-EA11-BFF6-BC305B390A80.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CCAB0879-BC12-EA11-BA1C-3CFDFE63F4E0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6C681F0E-990A-EA11-9A16-0025905B85E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1CC07437-950A-EA11-BF7B-0025905B85E8.root']);