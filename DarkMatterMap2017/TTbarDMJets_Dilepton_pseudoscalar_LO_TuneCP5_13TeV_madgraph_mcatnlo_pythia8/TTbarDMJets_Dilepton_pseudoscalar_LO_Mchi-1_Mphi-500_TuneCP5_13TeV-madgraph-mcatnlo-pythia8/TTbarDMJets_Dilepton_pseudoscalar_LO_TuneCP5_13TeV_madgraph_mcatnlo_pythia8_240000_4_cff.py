import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:15314', '1:15297', '1:18035', '1:18242', '1:13873', '1:17004', '1:17676', '1:20357', '1:20370', '1:20831', '1:20893', '1:23092', '1:23084', '1:14103', '1:23109', '1:20215', '1:23835', '1:21156', '1:21391', '1:21585', '1:24799', '1:19181', '1:17909', '1:17949', '1:22466', '1:22491', '1:24157', '1:11780', '1:11447', '1:17720', '1:17519', '1:17560', '1:18141', '1:18543', '1:12964', '1:19932', '1:17088', '1:17376', '1:22173', '1:23977', '1:15097', '1:16668', '1:21662', '1:14290', '1:14335', '1:14404', '1:14505', '1:15613', '1:15796', '1:21230', '1:21260', '1:17498', '1:16264', '1:16230', '1:19170', '1:19664', '1:20314', '1:20330', '1:19034', '1:20543', '1:20958', '1:24427', '1:24846', '1:21951', '1:24599', '1:16477', '1:16630', '1:16707', '1:16510', '1:23754', '1:23773', '1:23997', '1:21463', '1:24243', '1:24115', '1:11659', '1:11765', '1:11946', '1:18715', '1:20614', '1:20623', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/3A832396-BC0D-EA11-B1AC-AC1F6B0DE348.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/02308EE7-F002-EA11-880C-20040FF49604.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/CCA9164E-5912-EA11-8E3A-008CFAFC4340.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/DC613EB9-5812-EA11-B169-0242AC130003.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7E24AE60-BA02-EA11-B31A-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C02D6A28-D603-EA11-B438-246E96D14E34.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/5641A5DC-0A04-EA11-8D58-0CC47AFF01F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/34D2182A-0903-EA11-9CD9-A0369FE2C142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/5854FF44-98FE-E911-BBAE-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BE98A30F-72FC-E911-97EC-008CFAC91A1C.root']);