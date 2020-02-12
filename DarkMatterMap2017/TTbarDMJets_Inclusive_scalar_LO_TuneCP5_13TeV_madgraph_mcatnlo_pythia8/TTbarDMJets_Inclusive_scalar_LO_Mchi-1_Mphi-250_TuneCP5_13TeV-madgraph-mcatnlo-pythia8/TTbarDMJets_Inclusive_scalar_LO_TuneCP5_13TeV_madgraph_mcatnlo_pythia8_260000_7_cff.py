import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2334', '1:2583', '1:2740', '1:2754', '1:2391', '1:3104', '1:3188', '1:7714', '1:2631', '1:2816', '1:2843', '1:2898', '1:3019', '1:3249', '1:3607', '1:9266', '1:9361', '1:18390', '1:39806', '1:40266', '1:28534', '1:28584', '1:28600', '1:84968', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);