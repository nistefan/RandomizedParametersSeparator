import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2611', '1:2471', '1:2783', '1:2630', '1:2703', '1:2719', '1:2777', '1:2908', '1:3027', '1:3240', '1:4657', '1:8757', '1:10374', '1:9326', '1:9740', '1:39800', '1:39821', '1:40132', '1:40153', '1:40180', '1:40347', '1:60793', '1:39896', '1:84966', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);