import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:20583', '1:12268', '1:12526', '1:13758', '1:13966', '1:17431', '1:17708', '1:17963', '1:18093', '1:18867', '1:16695', '1:16703', '1:21618', '1:21745', '1:24185', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/2810000/4E15F603-5F16-EA11-917B-008CFAF29284.root']);