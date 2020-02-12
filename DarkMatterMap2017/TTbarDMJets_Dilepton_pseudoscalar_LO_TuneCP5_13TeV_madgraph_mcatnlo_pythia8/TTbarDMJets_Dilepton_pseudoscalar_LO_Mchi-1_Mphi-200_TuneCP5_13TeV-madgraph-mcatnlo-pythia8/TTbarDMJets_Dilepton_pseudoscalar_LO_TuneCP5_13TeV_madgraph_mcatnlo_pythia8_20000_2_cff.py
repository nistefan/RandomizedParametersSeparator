import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:93', '1:108', '1:6850', '1:7954', '1:10000', '1:6904', '1:35333', '1:32509', '1:1663', '1:1928', '1:7673', '1:26095', '1:28559', '1:28585', '1:9375', '1:8803', '1:28554', '1:28494', '1:31598', '1:33129', '1:27536', '1:27591', '1:34238', '1:27367', '1:173', '1:9763', '1:35005', '1:35145', '1:35167', '1:9913', '1:1561', '1:4546', '1:9788', '1:10443', '1:10499', '1:10489', '1:32351', '1:28988', '1:451', '1:3426', '1:8816', '1:9194', '1:26087', '1:29538', '1:34551', '1:34665', '1:34683', '1:35666', '1:31931', '1:31938', '1:31942', '1:31950', '1:3915', '1:27039', '1:27795', '1:34189', '1:4018', '1:9486', '1:8233', '1:8240', '1:33453', '1:10849', '1:6656', '1:3404', '1:30016', '1:1678', '1:1684', '1:28699', '1:32300', '1:3958', '1:6894', '1:7970', '1:35084', '1:32233', '1:6970', '1:9092', '1:6343', '1:4099', '1:6271', '1:26321', '1:28878', '1:28946', '1:32308', '1:5972', '1:28881', '1:30540', '1:30802', '1:27512', '1:27641', '1:27589', '1:34800', '1:35730', '1:35979', '1:35812', '1:35928', '1:190', '1:9815', '1:6828', '1:2294', '1:5261', '1:4048', '1:5948', '1:31788', '1:29706', '1:2293', '1:2289', '1:31001', '1:4839', '1:5048', '1:5343', '1:34405', '1:25487', '1:34308', '1:25056', '1:29191', '1:29194', '1:29203', '1:669', '1:705', '1:735', '1:31940', '1:29505', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/CEEE39CF-5C0F-EA11-9E5E-AC1F6BC67D4C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/D25EF608-3810-EA11-B5EC-28924A33BBAA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/5AD8423B-1C10-EA11-8A4A-3CFDFE63D1C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/E6F3AA4D-3511-EA11-B1BC-7CD30AD08EDE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/1EFB970C-1D11-EA11-8149-20CF305B05F1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/408C9E07-8611-EA11-9D25-0CC47A1DF7FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/762C4946-6013-EA11-85FF-40F2E9C6ADF6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/50446C98-4814-EA11-9D07-F01FAFE15C56.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/2A5977D6-BF14-EA11-A82B-14187727F981.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/F40F4B0E-0214-EA11-B314-A4BF0108B532.root']);