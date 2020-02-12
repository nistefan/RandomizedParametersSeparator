import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:14894', '1:15362', '1:18252', '1:23471', '1:23842', '1:21826', '1:24135', '1:11264', '1:11349', '1:11555', '1:20081', '1:13769', '1:13981', '1:20629', '1:20896', '1:23323', '1:13667', '1:13683', '1:13816', '1:20549', '1:14216', '1:14255', '1:23382', '1:20208', '1:20146', '1:23437', '1:21374', '1:21447', '1:21569', '1:24109', '1:19039', '1:21789', '1:16972', '1:12027', '1:22853', '1:24731', '1:11486', '1:11715', '1:11879', '1:11864', '1:12422', '1:11583', '1:17844', '1:12612', '1:15307', '1:16002', '1:22402', '1:21506', '1:19476', '1:19599', '1:20585', '1:14806', '1:14868', '1:15576', '1:15413', '1:16465', '1:12767', '1:17961', '1:22598', '1:18822', '1:19125', '1:19754', '1:15131', '1:16376', '1:20712', '1:20575', '1:23638', '1:24951', '1:24071', '1:24407', '1:24653', '1:24460', '1:15230', '1:15473', '1:15393', '1:16182', '1:16427', '1:16500', '1:16786', '1:16527', '1:16511', '1:20474', '1:21883', '1:24558', '1:24172', '1:24215', '1:24484', '1:16247', '1:16372', '1:16574', '1:11721', '1:11282', '1:11797', '1:11918', '1:11939', '1:17059', '1:22015', '1:22136', '1:22426', '1:18925', '1:20646', '1:20660', '1:20764', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/3A832396-BC0D-EA11-B1AC-AC1F6B0DE348.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/02308EE7-F002-EA11-880C-20040FF49604.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/CCA9164E-5912-EA11-8E3A-008CFAFC4340.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/DC613EB9-5812-EA11-B169-0242AC130003.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7E24AE60-BA02-EA11-B31A-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C02D6A28-D603-EA11-B438-246E96D14E34.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/5641A5DC-0A04-EA11-8D58-0CC47AFF01F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/34D2182A-0903-EA11-9CD9-A0369FE2C142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/5854FF44-98FE-E911-BBAE-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BE98A30F-72FC-E911-97EC-008CFAC91A1C.root']);