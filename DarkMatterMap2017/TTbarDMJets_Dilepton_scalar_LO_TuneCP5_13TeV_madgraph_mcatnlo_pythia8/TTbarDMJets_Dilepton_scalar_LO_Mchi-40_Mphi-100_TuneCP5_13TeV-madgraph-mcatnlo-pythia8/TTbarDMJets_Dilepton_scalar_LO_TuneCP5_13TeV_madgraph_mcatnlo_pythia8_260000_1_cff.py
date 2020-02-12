import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:34959', '1:37401', '1:83219', '1:84704', '1:86279', '1:29894', '1:29914', '1:29916', '1:29921', '1:29928', '1:29934', '1:69319', '1:65323', '1:65792', '1:71490', '1:73977', '1:75362', '1:74477', '1:56594', '1:71197', '1:71720', '1:68694', '1:63639', '1:73426', '1:76800', '1:70227', '1:70351', '1:70665', '1:89146', '1:89173', '1:101108', '1:101113', '1:90176', '1:90157', '1:90252', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/FE3E37D1-F519-EA11-A345-0CC47A4D9A2C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/34BBDCBE-1118-EA11-AD6F-0CC47A5FBDC1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/34C26C6A-9D17-EA11-A4B4-FA163EBB2EC2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BE7E4D2C-4F18-EA11-B3C8-549F358EB721.root']);