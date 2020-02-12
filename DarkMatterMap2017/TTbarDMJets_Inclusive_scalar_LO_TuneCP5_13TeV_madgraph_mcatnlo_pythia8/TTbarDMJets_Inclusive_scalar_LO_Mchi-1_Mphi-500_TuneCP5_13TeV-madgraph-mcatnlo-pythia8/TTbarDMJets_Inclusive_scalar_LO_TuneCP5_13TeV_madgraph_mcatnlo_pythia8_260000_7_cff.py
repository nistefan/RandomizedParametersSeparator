import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2331', '1:2501', '1:2708', '1:2279', '1:2361', '1:2445', '1:2614', '1:3164', '1:9352', '1:17318', '1:17844', '1:39932', '1:39976', '1:40072', '1:40099', '1:62346', '1:28657', '1:39324', '1:39875', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);