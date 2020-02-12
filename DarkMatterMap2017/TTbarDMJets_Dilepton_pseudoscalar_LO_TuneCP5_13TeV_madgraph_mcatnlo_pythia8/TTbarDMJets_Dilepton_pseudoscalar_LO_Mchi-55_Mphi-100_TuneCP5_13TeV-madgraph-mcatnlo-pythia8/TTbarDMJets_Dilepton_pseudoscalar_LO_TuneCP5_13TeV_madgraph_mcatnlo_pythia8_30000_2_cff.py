import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:37965', '1:38189', '1:36991', '1:38878', '1:36805', '1:37183', '1:37507', '1:37847', '1:38414', '1:38971', '1:38945', '1:37579', '1:37587', '1:38079', '1:38090', '1:38658', '1:36898', '1:37752', '1:37849', '1:38229', '1:38240', '1:38245', '1:38013', '1:38525', '1:38976', '1:38780', '1:37117', '1:36237', '1:36775', '1:37065', '1:37259', '1:38284', '1:37922', '1:37932', '1:36714', '1:38408', '1:36050', '1:36054', '1:36514', '1:36533', '1:36638', '1:36664', '1:37012', '1:37667', '1:37895', '1:36245', '1:36392', '1:36181', '1:36410', '1:36411', '1:36944', '1:38122', '1:36121', '1:36252', '1:37157', '1:37006', '1:37066', '1:36330', '1:36790', '1:36496', '1:36986', '1:38132', '1:36854', '1:36107', '1:36895', '1:38217', '1:38798', '1:38243', '1:38647', '1:38652', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/D0F8A41C-990E-EA11-A50D-AC1F6B1E3074.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/DCD9D649-2013-EA11-BBCA-98039B3B0032.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/88D5C4F6-9D0C-EA11-A344-24BE05C63681.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/14F851FE-6510-EA11-B76F-008CFAF74B22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/2AC7749D-2013-EA11-AAAA-001E67792738.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/8228DED2-F60C-EA11-9D11-002590FD5A78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/B4730441-2013-EA11-8532-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/98375E4E-2013-EA11-BDE2-7CD30AD095BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/86D1A249-EF0D-EA11-BAF6-008CFAE45108.root']);