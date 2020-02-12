import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:4629', '1:4729', '1:8131', '1:8160', '1:8315', '1:8381', '1:8742', '1:8076', '1:8083', '1:10529', '1:10540', '1:10560', '1:5605', '1:5718', '1:8031', '1:10055', '1:8489', '1:8497', '1:8504', '1:10196', '1:10198', '1:10206', '1:10216', '1:10289', '1:10342', '1:10638', '1:5615', '1:10071', '1:10163', '1:10183', '1:31691', '1:31715', '1:33482', '1:33867', '1:600', '1:609', '1:3195', '1:3199', '1:629', '1:656', '1:3002', '1:3009', '1:4060', '1:6930', '1:8532', '1:8782', '1:10112', '1:26984', '1:28954', '1:28997', '1:30123', '1:32443', '1:32809', '1:31502', '1:33703', '1:33799', '1:32849', '1:8536', '1:4082', '1:2435', '1:1068', '1:1637', '1:1640', '1:1642', '1:3991', '1:7607', '1:4233', '1:4910', '1:6454', '1:6452', '1:6455', '1:6467', '1:6469', '1:10874', '1:10941', '1:1877', '1:1883', '1:1886', '1:1898', '1:1834', '1:1862', '1:1953', '1:2581', '1:2676', '1:10775', '1:10831', '1:10833', '1:10848', '1:10883', '1:33658', '1:35342', '1:1866', '1:1899', '1:2096', '1:2723', '1:2740', '1:2513', '1:2627', '1:2700', '1:25239', '1:27032', '1:34198', '1:34202', '1:34508', '1:34641', '1:34891', '1:35315', '1:35915', '1:9848', '1:29835', '1:29937', '1:29973', '1:28886', '1:33909', '1:35054', '1:33782', '1:33647', '1:2957', '1:2985', '1:3743', '1:3757', '1:10942', '1:31184', '1:31235', '1:33706', '1:33830', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/7C06E9B7-92EF-E911-A283-FA163EB32F6D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/BC5D928C-D6FA-E911-ADA7-FA163E94CF4C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/624B9086-6F08-EA11-A556-0CC47AFF0260.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/F4A80929-4310-EA11-ADD8-0025905C3E68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/C6CE0C9B-F40F-EA11-BDDA-0CC47AFCC3D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/6C31E4FA-E60F-EA11-857D-00266CFFBF84.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/504EFD08-4705-EA11-89D8-24BE05C63681.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/DAE6A191-5105-EA11-80D3-1866DA87A65E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B441DF92-5105-EA11-A535-8CDCD4A99E08.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/A47CB0A6-3408-EA11-BBF8-0CC47A7E6A74.root']);