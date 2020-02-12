import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11442', '1:22368', '1:22428', '1:25422', '1:25877', '1:29044', '1:25882', '1:25900', '1:25993', '1:89390', '1:89402', '1:89494', '1:89511', '1:90827', '1:90243', '1:90328', '1:11655', '1:13124', '1:13152', '1:29561', '1:29562', '1:29643', '1:29712', '1:22645', '1:22665', '1:22706', '1:101907', '1:101919', '1:13530', '1:22657', '1:22661', '1:22674', '1:22680', '1:22830', '1:29173', '1:101652', '1:22724', '1:101817', '1:101818', '1:29675', '1:30006', '1:30669', '1:30710', '1:31578', '1:90031', '1:22847', '1:22890', '1:22957', '1:25022', '1:25337', '1:25984', '1:25987', '1:25982', '1:31236', '1:31317', '1:31322', '1:31336', '1:30312', '1:31495', '1:31766', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/EA250210-B311-EA11-8313-0CC47AFF0264.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/4ABB45F0-2C10-EA11-8C52-0CC47AFB7D60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/04CFEB6A-9810-EA11-9B8C-00266CFFC76C.root']);