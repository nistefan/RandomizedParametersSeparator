import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:18307', '1:23685', '1:24088', '1:21896', '1:13523', '1:13539', '1:11587', '1:20493', '1:17133', '1:17613', '1:17662', '1:14090', '1:16914', '1:19973', '1:19975', '1:23383', '1:20446', '1:23464', '1:21577', '1:21578', '1:24364', '1:24726', '1:16889', '1:16913', '1:16921', '1:17087', '1:22629', '1:17942', '1:24032', '1:24379', '1:11387', '1:11422', '1:11192', '1:13725', '1:22022', '1:12083', '1:17888', '1:12609', '1:18647', '1:18697', '1:12760', '1:18247', '1:18588', '1:18616', '1:15740', '1:19731', '1:15546', '1:16783', '1:19566', '1:20635', '1:21790', '1:21741', '1:14440', '1:14722', '1:15484', '1:19509', '1:19874', '1:16887', '1:21255', '1:21268', '1:22864', '1:15713', '1:15721', '1:15081', '1:19655', '1:15696', '1:15078', '1:20157', '1:20266', '1:20338', '1:20766', '1:20847', '1:15079', '1:19193', '1:24294', '1:24400', '1:21674', '1:21677', '1:21801', '1:21239', '1:24199', '1:24500', '1:15466', '1:16145', '1:16099', '1:23753', '1:24468', '1:16637', '1:11832', '1:20876', '1:23747', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/3A832396-BC0D-EA11-B1AC-AC1F6B0DE348.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/02308EE7-F002-EA11-880C-20040FF49604.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/CCA9164E-5912-EA11-8E3A-008CFAFC4340.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/DC613EB9-5812-EA11-B169-0242AC130003.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7E24AE60-BA02-EA11-B31A-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C02D6A28-D603-EA11-B438-246E96D14E34.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/5641A5DC-0A04-EA11-8D58-0CC47AFF01F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/34D2182A-0903-EA11-9CD9-A0369FE2C142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/5854FF44-98FE-E911-BBAE-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BE98A30F-72FC-E911-97EC-008CFAC91A1C.root']);