import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2477', '1:2977', '1:3055', '1:6672', '1:2578', '1:2677', '1:3045', '1:8950', '1:9796', '1:9957', '1:10382', '1:9872', '1:13824', '1:13966', '1:40187', '1:40417', '1:61156', '1:28627', '1:28671', '1:28503', '1:28632', '1:39416', '1:99954', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);