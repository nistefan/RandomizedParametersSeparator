import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:35871', '1:37627', '1:37994', '1:33332', '1:33702', '1:37599', '1:33687', '1:56009', '1:68463', '1:78592', '1:24300', '1:24413', '1:24635', '1:26016', '1:29787', '1:29812', '1:29909', '1:29941', '1:29809', '1:59629', '1:59875', '1:68909', '1:62146', '1:64397', '1:73386', '1:73423', '1:78619', '1:58469', '1:57335', '1:51355', '1:51384', '1:52955', '1:64864', '1:65476', '1:65681', '1:65353', '1:70965', '1:70326', '1:66942', '1:89142', '1:89144', '1:89177', '1:89185', '1:89467', '1:90043', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/FE3E37D1-F519-EA11-A345-0CC47A4D9A2C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/34BBDCBE-1118-EA11-AD6F-0CC47A5FBDC1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/34C26C6A-9D17-EA11-A4B4-FA163EBB2EC2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BE7E4D2C-4F18-EA11-B3C8-549F358EB721.root']);