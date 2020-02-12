import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:32875', '1:32883', '1:33330', '1:33332', '1:33338', '1:33344', '1:35171', '1:35283', '1:35530', '1:23999', '1:26850', '1:35598', '1:27876', '1:35067', '1:34247', '1:34352', '1:34354', '1:28221', '1:32590', '1:34459', '1:34003', '1:34117', '1:29513', '1:35705', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/ECAA5628-DF19-EA11-B3DA-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E6CE347E-2018-EA11-8EBA-AC1F6B34AA78.root']);