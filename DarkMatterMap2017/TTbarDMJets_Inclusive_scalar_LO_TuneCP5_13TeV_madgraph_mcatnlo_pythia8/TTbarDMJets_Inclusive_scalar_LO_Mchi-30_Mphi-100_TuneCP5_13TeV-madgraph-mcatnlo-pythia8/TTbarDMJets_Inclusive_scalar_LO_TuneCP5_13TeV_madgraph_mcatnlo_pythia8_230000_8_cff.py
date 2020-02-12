import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:7184', '1:15400', '1:22625', '1:38700', '1:38883', '1:101510', '1:101747', '1:90304', '1:49747', '1:49767', '1:49775', '1:39088', '1:40145', '1:40327', '1:46045', '1:49072', '1:24313', '1:27764', '1:30037', '1:30088', '1:61100', '1:61455', '1:38939', '1:38959', '1:38978', '1:38993', '1:50172', '1:50434', '1:62814', '1:62953', '1:62963', '1:62859', '1:76316', '1:27797', '1:30170', '1:46144', '1:97117', '1:94967', '1:99282', '1:99930', '1:88403', '1:86771', '1:90492', '1:88702', '1:6864', '1:6467', '1:10064', '1:21391', '1:49287', '1:55060', '1:69331', '1:69774', '1:34777', '1:46974', '1:59266', '1:51822', '1:53034', '1:58120', '1:68755', '1:72068', '1:72534', '1:72765', '1:72946', '1:73023', '1:74293', '1:75836', '1:75857', '1:78719', '1:94121', '1:89449', '1:87994', '1:89906', '1:79641', '1:81240', '1:81338', '1:81417', '1:81519', '1:81743', '1:86808', '1:86939', '1:90067', '1:90709', '1:90767', '1:101814', '1:102405', '1:99959', '1:100754', '1:101364', '1:101563', '1:46398', '1:24743', '1:52555', '1:60010', '1:61168', '1:3148', '1:3151', '1:3326', '1:4032', '1:4099', '1:54578', '1:63606', '1:76341', '1:77013', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A4DE4FE0-3913-EA11-8646-002481CFE864.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CEDC54BD-3201-EA11-9A26-00215A49197E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D6BAC6CC-4F13-EA11-9382-008CFA0516BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2E7CDC91-E709-EA11-82C2-0CC47A4C8F08.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E954D3A-80F7-E911-85E2-AC1F6B0DE490.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7093C3A3-0A08-EA11-836E-AC1F6B0DE2A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE57EA42-FA0A-EA11-A431-0025905A497A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24279122-6000-EA11-AFE5-509A4C9EF8FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CCF160DF-3913-EA11-B4B1-7CD30AD092FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FA4AD288-700D-EA11-9E19-509A4C748095.root']);