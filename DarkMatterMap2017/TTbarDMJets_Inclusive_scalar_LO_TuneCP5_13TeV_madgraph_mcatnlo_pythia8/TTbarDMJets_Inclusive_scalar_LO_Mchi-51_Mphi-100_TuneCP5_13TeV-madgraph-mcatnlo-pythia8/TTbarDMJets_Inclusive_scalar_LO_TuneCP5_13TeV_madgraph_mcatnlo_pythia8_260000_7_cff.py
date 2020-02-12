import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2510', '1:2541', '1:3060', '1:2747', '1:2825', '1:3132', '1:3146', '1:3251', '1:8926', '1:9977', '1:10272', '1:18378', '1:17283', '1:17842', '1:39782', '1:39843', '1:39856', '1:40101', '1:40148', '1:40204', '1:40208', '1:63393', '1:61399', '1:61529', '1:86595', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);