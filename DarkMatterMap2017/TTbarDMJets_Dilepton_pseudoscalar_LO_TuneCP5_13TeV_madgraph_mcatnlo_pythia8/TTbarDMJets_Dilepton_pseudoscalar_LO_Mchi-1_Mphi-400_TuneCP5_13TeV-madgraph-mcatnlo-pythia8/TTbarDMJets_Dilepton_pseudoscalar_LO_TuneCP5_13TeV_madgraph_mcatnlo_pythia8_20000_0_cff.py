import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:366', '1:388', '1:3281', '1:3346', '1:4335', '1:8187', '1:8213', '1:9003', '1:9019', '1:9667', '1:9592', '1:9703', '1:9707', '1:8061', '1:8487', '1:8494', '1:10194', '1:10217', '1:10332', '1:10340', '1:10078', '1:10160', '1:33474', '1:33511', '1:34881', '1:34867', '1:620', '1:6270', '1:6912', '1:3244', '1:3933', '1:29000', '1:30315', '1:30349', '1:32691', '1:31460', '1:31935', '1:33349', '1:32824', '1:32888', '1:441', '1:4058', '1:4076', '1:4079', '1:4088', '1:1638', '1:1654', '1:1658', '1:1078', '1:2385', '1:3986', '1:4909', '1:4951', '1:6576', '1:6487', '1:6588', '1:6595', '1:6599', '1:6381', '1:6472', '1:25900', '1:34613', '1:1854', '1:7638', '1:33610', '1:34727', '1:35346', '1:1962', '1:1970', '1:2604', '1:25234', '1:27916', '1:35191', '1:35923', '1:7140', '1:7143', '1:7778', '1:9366', '1:9758', '1:9853', '1:33915', '1:33893', '1:2931', '1:2935', '1:2952', '1:2955', '1:2960', '1:3746', '1:3090', '1:31142', '1:31247', '1:31250', '1:33694', '1:33726', '1:33818', '1:33825', '1:33863', '1:33865', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/7C06E9B7-92EF-E911-A283-FA163EB32F6D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/BC5D928C-D6FA-E911-ADA7-FA163E94CF4C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/624B9086-6F08-EA11-A556-0CC47AFF0260.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/F4A80929-4310-EA11-ADD8-0025905C3E68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/C6CE0C9B-F40F-EA11-BDDA-0CC47AFCC3D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/6C31E4FA-E60F-EA11-857D-00266CFFBF84.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/504EFD08-4705-EA11-89D8-24BE05C63681.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/DAE6A191-5105-EA11-80D3-1866DA87A65E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B441DF92-5105-EA11-A535-8CDCD4A99E08.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/A47CB0A6-3408-EA11-BBF8-0CC47A7E6A74.root']);