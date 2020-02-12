import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:28', '1:33', '1:373', '1:392', '1:394', '1:781', '1:3056', '1:3285', '1:3350', '1:4628', '1:8737', '1:31636', '1:8072', '1:8078', '1:8345', '1:10051', '1:5755', '1:10957', '1:10200', '1:10192', '1:33741', '1:6261', '1:4122', '1:10113', '1:10117', '1:3241', '1:3280', '1:28955', '1:30122', '1:32437', '1:31946', '1:33748', '1:32823', '1:32842', '1:539', '1:608', '1:3033', '1:4067', '1:4094', '1:1052', '1:2359', '1:2380', '1:2384', '1:2392', '1:3981', '1:6450', '1:6577', '1:6582', '1:6395', '1:6396', '1:6495', '1:6498', '1:6382', '1:6586', '1:30976', '1:30983', '1:10835', '1:1893', '1:1968', '1:1974', '1:10880', '1:10882', '1:33653', '1:1885', '1:1887', '1:1964', '1:2516', '1:2572', '1:25246', '1:34191', '1:34192', '1:27895', '1:34786', '1:10463', '1:10480', '1:10491', '1:9317', '1:7753', '1:7762', '1:9804', '1:33910', '1:33997', '1:35479', '1:30706', '1:31081', '1:31089', '1:31185', '1:31248', '1:31252', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/7C06E9B7-92EF-E911-A283-FA163EB32F6D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/BC5D928C-D6FA-E911-ADA7-FA163E94CF4C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/624B9086-6F08-EA11-A556-0CC47AFF0260.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/F4A80929-4310-EA11-ADD8-0025905C3E68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/C6CE0C9B-F40F-EA11-BDDA-0CC47AFCC3D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/6C31E4FA-E60F-EA11-857D-00266CFFBF84.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/504EFD08-4705-EA11-89D8-24BE05C63681.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/DAE6A191-5105-EA11-80D3-1866DA87A65E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B441DF92-5105-EA11-A535-8CDCD4A99E08.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/A47CB0A6-3408-EA11-BBF8-0CC47A7E6A74.root']);