import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11309', '1:11438', '1:11443', '1:13225', '1:22028', '1:22315', '1:22338', '1:22429', '1:22440', '1:22528', '1:25419', '1:25912', '1:29761', '1:31077', '1:25892', '1:25894', '1:25897', '1:31774', '1:89519', '1:89528', '1:90829', '1:90849', '1:11541', '1:11847', '1:11920', '1:13132', '1:22200', '1:29540', '1:29548', '1:29527', '1:29775', '1:29742', '1:29752', '1:22610', '1:22649', '1:101909', '1:101921', '1:25132', '1:29075', '1:29400', '1:29401', '1:30521', '1:31722', '1:89440', '1:30787', '1:30917', '1:30944', '1:31012', '1:31019', '1:31022', '1:31043', '1:90877', '1:90959', '1:31056', '1:31064', '1:31074', '1:30683', '1:31576', '1:22927', '1:25034', '1:22883', '1:25029', '1:25088', '1:25315', '1:25796', '1:25803', '1:25792', '1:25965', '1:29149', '1:25964', '1:30215', '1:31225', '1:31330', '1:30286', '1:30294', '1:30299', '1:31485', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/EA250210-B311-EA11-8313-0CC47AFF0264.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/4ABB45F0-2C10-EA11-8C52-0CC47AFB7D60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/04CFEB6A-9810-EA11-9B8C-00266CFFC76C.root']);