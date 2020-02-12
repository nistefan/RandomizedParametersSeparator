import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:38474', '1:37453', '1:36211', '1:36539', '1:36731', '1:36833', '1:37384', '1:37505', '1:37739', '1:37803', '1:37865', '1:38964', '1:38970', '1:38983', '1:36135', '1:38141', '1:36498', '1:36360', '1:38383', '1:36959', '1:38019', '1:38691', '1:36904', '1:37435', '1:37952', '1:36929', '1:36997', '1:37906', '1:38220', '1:38681', '1:38717', '1:37107', '1:38197', '1:36933', '1:38591', '1:36385', '1:38796', '1:37163', '1:37787', '1:37923', '1:36056', '1:36073', '1:36715', '1:36085', '1:36690', '1:36828', '1:37509', '1:38405', '1:36391', '1:36687', '1:36936', '1:36956', '1:38135', '1:38492', '1:37963', '1:37365', '1:37209', '1:38115', '1:36118', '1:38899', '1:36160', '1:37460', '1:36883', '1:36333', '1:36366', '1:36212', '1:38457', '1:38522', '1:38932', '1:38275', '1:38710', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/D0F8A41C-990E-EA11-A50D-AC1F6B1E3074.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/DCD9D649-2013-EA11-BBCA-98039B3B0032.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/88D5C4F6-9D0C-EA11-A344-24BE05C63681.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/14F851FE-6510-EA11-B76F-008CFAF74B22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/2AC7749D-2013-EA11-AAAA-001E67792738.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/8228DED2-F60C-EA11-9D11-002590FD5A78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/B4730441-2013-EA11-8532-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/98375E4E-2013-EA11-BDE2-7CD30AD095BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/86D1A249-EF0D-EA11-BAF6-008CFAE45108.root']);