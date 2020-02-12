import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2624', '1:2629', '1:3180', '1:3256', '1:2564', '1:2640', '1:2713', '1:2859', '1:2897', '1:2900', '1:3246', '1:3651', '1:10269', '1:10328', '1:9498', '1:39763', '1:39925', '1:40293', '1:40345', '1:40370', '1:63787', '1:28525', '1:28551', '1:28665', '1:39335', '1:39401', '1:63592', '1:63871', '1:84965', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);