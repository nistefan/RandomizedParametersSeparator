import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:25199', '1:25201', '1:35705', '1:33335', '1:37513', '1:36895', '1:58366', '1:69317', '1:59650', '1:81547', '1:86301', '1:82246', '1:83080', '1:83732', '1:83861', '1:91339', '1:24173', '1:24430', '1:29784', '1:62735', '1:64139', '1:74232', '1:66603', '1:78724', '1:75012', '1:58412', '1:58778', '1:44577', '1:67784', '1:69070', '1:52165', '1:71191', '1:62236', '1:65879', '1:70188', '1:72705', '1:66668', '1:70346', '1:70819', '1:71336', '1:66071', '1:89166', '1:89184', '1:89419', '1:89969', '1:90250', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/FE3E37D1-F519-EA11-A345-0CC47A4D9A2C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/34BBDCBE-1118-EA11-AD6F-0CC47A5FBDC1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/34C26C6A-9D17-EA11-A4B4-FA163EBB2EC2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BE7E4D2C-4F18-EA11-B3C8-549F358EB721.root']);