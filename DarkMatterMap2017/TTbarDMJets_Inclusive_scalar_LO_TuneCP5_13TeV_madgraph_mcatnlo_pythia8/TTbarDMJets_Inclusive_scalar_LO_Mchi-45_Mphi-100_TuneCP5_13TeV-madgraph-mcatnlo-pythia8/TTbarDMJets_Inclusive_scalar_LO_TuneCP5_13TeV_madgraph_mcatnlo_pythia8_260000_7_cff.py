import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2613', '1:2872', '1:3026', '1:2699', '1:2748', '1:2794', '1:3068', '1:3181', '1:9739', '1:17282', '1:40037', '1:40115', '1:39974', '1:40077', '1:40258', '1:60792', '1:63597', '1:29033', '1:39328', '1:87258', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);