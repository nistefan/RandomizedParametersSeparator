import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:29425', '1:6043', '1:3751', '1:9467', '1:25700', '1:30278', '1:4016', '1:7383', '1:35502', '1:841', '1:938', '1:2628', '1:2639', '1:2999', '1:3639', '1:3672', '1:3678', '1:10241', '1:10253', '1:2011', '1:2014', '1:2029', '1:4895', '1:4734', '1:4982', '1:4689', '1:25758', '1:25759', '1:34441', '1:34469', '1:4715', '1:10245', '1:4716', '1:10076', '1:10240', '1:10251', '1:10257', '1:34364', '1:33402', '1:1328', '1:30954', '1:26222', '1:33029', '1:10422', '1:6081', '1:10711', '1:26052', '1:28414', '1:1006', '1:1500', '1:7942', '1:1285', '1:33779', '1:27038', '1:27808', '1:34132', '1:28664', '1:27593', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/A0F0DC20-9D10-EA11-AD40-0425C5DE7BF4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/CABD0001-7C04-EA11-9F9B-0CC47AA992AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/5A16F5BD-E5FB-E911-9C5C-38EAA78D8B54.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/88084C38-5AF0-E911-8968-00E081B7B442.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/1AFCF3E7-9B03-EA11-A974-FA163E6A45C8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/3873C66F-D70F-EA11-B305-0CC47AFF2496.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B6B9CD90-F40F-EA11-AF38-509A4C74913F.root']);