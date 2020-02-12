import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2591', '1:2623', '1:2729', '1:3078', '1:2586', '1:2608', '1:2689', '1:2707', '1:2736', '1:2769', '1:3075', '1:3149', '1:9888', '1:9904', '1:13963', '1:39919', '1:40211', '1:40286', '1:40381', '1:61162', '1:61517', '1:28559', '1:28575', '1:39351', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);