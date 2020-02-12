import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:14779', '1:15346', '1:15411', '1:18028', '1:18032', '1:23355', '1:24062', '1:11332', '1:11895', '1:13890', '1:23076', '1:20030', '1:20141', '1:20080', '1:16496', '1:16476', '1:16479', '1:23979', '1:20039', '1:20180', '1:20204', '1:20659', '1:20155', '1:20232', '1:19296', '1:16218', '1:19533', '1:19951', '1:17552', '1:24030', '1:24333', '1:24622', '1:11028', '1:11337', '1:11307', '1:11503', '1:11853', '1:13189', '1:18527', '1:18614', '1:15028', '1:19917', '1:17132', '1:17221', '1:17374', '1:15510', '1:23717', '1:15985', '1:20556', '1:20815', '1:21392', '1:21456', '1:14351', '1:14468', '1:14338', '1:14536', '1:14576', '1:14698', '1:15780', '1:15363', '1:15419', '1:16693', '1:21256', '1:21259', '1:24670', '1:17194', '1:15071', '1:15549', '1:15055', '1:19639', '1:20323', '1:19290', '1:21864', '1:24662', '1:21554', '1:21066', '1:24501', '1:24510', '1:19747', '1:16048', '1:16280', '1:20070', '1:23875', '1:20935', '1:24147', '1:24231', '1:24266', '1:11162', '1:11600', '1:18257', '1:18836', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/3A832396-BC0D-EA11-B1AC-AC1F6B0DE348.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/02308EE7-F002-EA11-880C-20040FF49604.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/CCA9164E-5912-EA11-8E3A-008CFAFC4340.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/DC613EB9-5812-EA11-B169-0242AC130003.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7E24AE60-BA02-EA11-B31A-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C02D6A28-D603-EA11-B438-246E96D14E34.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/5641A5DC-0A04-EA11-8D58-0CC47AFF01F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/34D2182A-0903-EA11-9CD9-A0369FE2C142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/5854FF44-98FE-E911-BBAE-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BE98A30F-72FC-E911-97EC-008CFAC91A1C.root']);