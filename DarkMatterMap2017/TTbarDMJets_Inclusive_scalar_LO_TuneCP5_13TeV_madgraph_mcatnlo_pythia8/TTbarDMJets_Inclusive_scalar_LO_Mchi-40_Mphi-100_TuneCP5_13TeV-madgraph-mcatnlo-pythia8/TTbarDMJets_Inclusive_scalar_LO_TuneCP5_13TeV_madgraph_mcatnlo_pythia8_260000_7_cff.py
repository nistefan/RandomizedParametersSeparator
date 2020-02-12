import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2337', '1:2381', '1:2517', '1:2534', '1:2687', '1:2735', '1:2753', '1:2310', '1:3010', '1:2766', '1:2869', '1:3100', '1:3595', '1:9290', '1:9303', '1:9910', '1:10352', '1:10368', '1:9244', '1:18364', '1:16867', '1:17815', '1:17281', '1:39984', '1:40130', '1:28636', '1:28552', '1:63598', '1:63613', '1:63994', '1:64507', '1:89965', '1:94391', '1:84969', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);