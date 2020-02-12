import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2368', '1:2389', '1:2554', '1:2639', '1:2647', '1:2657', '1:2714', '1:2720', '1:2732', '1:2283', '1:2618', '1:3031', '1:13860', '1:10778', '1:2519', '1:2598', '1:2616', '1:2728', '1:2773', '1:2873', '1:2902', '1:2921', '1:2924', '1:3076', '1:3603', '1:3634', '1:3662', '1:8812', '1:8829', '1:8910', '1:9803', '1:9815', '1:9839', '1:9895', '1:9969', '1:17780', '1:17377', '1:39677', '1:39757', '1:39796', '1:39814', '1:39836', '1:39934', '1:39975', '1:40000', '1:40125', '1:40074', '1:40122', '1:40219', '1:40227', '1:40239', '1:40292', '1:40377', '1:40412', '1:61692', '1:69208', '1:61165', '1:28533', '1:28635', '1:28526', '1:28542', '1:28583', '1:39349', '1:39368', '1:39378', '1:39385', '1:39859', '1:39864', '1:63595', '1:63615', '1:64237', '1:64377', '1:64744', '1:89464', '1:89580', '1:90751', '1:84970', '1:84971', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A4DA97A2-ED17-EA11-B881-0242AC130002.root']);