import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:28481', '1:6028', '1:6159', '1:2940', '1:28090', '1:25800', '1:25823', '1:30230', '1:6125', '1:754', '1:887', '1:1936', '1:2648', '1:2987', '1:3687', '1:7336', '1:7884', '1:461', '1:2004', '1:2013', '1:2016', '1:4899', '1:4928', '1:4994', '1:4970', '1:4694', '1:4710', '1:4713', '1:10375', '1:32944', '1:4731', '1:7340', '1:7352', '1:7358', '1:4692', '1:4767', '1:4902', '1:10203', '1:10114', '1:5522', '1:5694', '1:31062', '1:31473', '1:31584', '1:33304', '1:33350', '1:33808', '1:33394', '1:33407', '1:1295', '1:26189', '1:28196', '1:28198', '1:10049', '1:10664', '1:10671', '1:10680', '1:10806', '1:34242', '1:3632', '1:4878', '1:4884', '1:6067', '1:26283', '1:31992', '1:34629', '1:34655', '1:28525', '1:9477', '1:7205', '1:28655', '1:33787', '1:25217', '1:25391', '1:27809', '1:6037', '1:10718', '1:35070', '1:27715', '1:34177', '1:32238', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/A0F0DC20-9D10-EA11-AD40-0425C5DE7BF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/CABD0001-7C04-EA11-9F9B-0CC47AA992AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/5A16F5BD-E5FB-E911-9C5C-38EAA78D8B54.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/88084C38-5AF0-E911-8968-00E081B7B442.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/1AFCF3E7-9B03-EA11-A974-FA163E6A45C8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/3873C66F-D70F-EA11-B305-0CC47AFF2496.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B6B9CD90-F40F-EA11-AF38-509A4C74913F.root']);