import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2313', '1:2694', '1:2938', '1:3239', '1:6164', '1:2651', '1:2795', '1:3252', '1:3636', '1:3641', '1:9261', '1:9302', '1:9795', '1:17779', '1:39753', '1:39868', '1:39898', '1:40369', '1:40401', '1:61135', '1:61146', '1:28590', '1:90674', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);