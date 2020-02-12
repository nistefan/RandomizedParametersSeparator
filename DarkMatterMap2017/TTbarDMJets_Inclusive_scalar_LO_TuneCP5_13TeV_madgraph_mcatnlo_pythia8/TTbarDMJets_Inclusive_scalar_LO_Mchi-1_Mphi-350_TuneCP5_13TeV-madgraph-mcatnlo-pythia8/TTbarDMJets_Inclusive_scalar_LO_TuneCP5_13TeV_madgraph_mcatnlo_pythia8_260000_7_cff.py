import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2509', '1:2492', '1:2503', '1:2555', '1:2582', '1:2770', '1:2763', '1:2786', '1:3002', '1:3638', '1:9308', '1:10325', '1:18411', '1:16858', '1:28601', '1:39827', '1:39877', '1:63855', '1:64489', '1:89588', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);