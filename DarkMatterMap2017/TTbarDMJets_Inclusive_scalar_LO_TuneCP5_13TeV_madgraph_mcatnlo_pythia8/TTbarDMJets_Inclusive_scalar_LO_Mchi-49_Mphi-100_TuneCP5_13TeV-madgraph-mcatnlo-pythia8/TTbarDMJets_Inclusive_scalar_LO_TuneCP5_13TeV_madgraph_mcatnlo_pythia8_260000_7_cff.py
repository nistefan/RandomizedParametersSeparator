import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2405', '1:3062', '1:3096', '1:3220', '1:2760', '1:2918', '1:3600', '1:8894', '1:8912', '1:18339', '1:16853', '1:16859', '1:39775', '1:39818', '1:40008', '1:40026', '1:61421', '1:61550', '1:28519', '1:39373', '1:64106', '1:85617', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);