import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:51614', '1:52461', '1:53044', '1:57371', '1:76219', '1:79054', '1:80857', '1:81794', '1:9422', '1:103106', '1:1648', '1:4579', '1:5800', '1:7650', '1:8840', '1:12556', '1:14621', '1:104826', '1:14', '1:1056', '1:1489', '1:1547', '1:1980', '1:281', '1:4051', '1:4750', '1:58485', '1:58857', '1:58905', '1:60924', '1:61441', '1:59073', '1:62919', '1:71134', '1:71250', '1:71493', '1:71507', '1:71330', '1:71420', '1:100744', '1:18129', '1:18587', '1:19370', '1:33611', '1:33942', '1:43235', '1:43024', '1:45771', '1:100901', '1:97526', '1:99540', '1:100427', '1:100649', '1:93539', '1:99094', '1:96578', '1:98381', '1:21105', '1:21259', '1:21300', '1:21310', '1:21432', '1:21574', '1:94163', '1:94308', '1:93268', '1:93304', '1:93835', '1:84348', '1:85730', '1:85744', '1:85344', '1:88375', '1:15837', '1:15970', '1:16730', '1:39392', '1:39624', '1:39710', '1:39764', '1:39866', '1:42532', '1:43070', '1:48262', '1:48437', '1:48648', '1:48681', '1:43244', '1:43246', '1:43255', '1:43482', '1:43465', '1:43689', '1:59493', '1:62736', '1:62974', '1:63375', '1:63169', '1:64215', '1:55868', '1:88553', '1:88986', '1:91405', '1:95728', '1:95843', '1:16277', '1:16345', '1:16350', '1:16515', '1:34572', '1:17072', '1:17496', '1:21239', '1:21524', '1:21692', '1:24107', '1:21472', '1:21918', '1:45544', '1:45560', '1:48085', '1:63207', '1:63646', '1:63651', '1:63957', '1:63512', '1:53361', '1:56829', '1:53476', '1:53614', '1:54192', '1:54253', '1:54444', '1:54417', '1:26825', '1:38582', '1:42284', '1:49156', '1:16434', '1:17043', '1:41723', '1:48803', '1:49735', '1:71713', '1:70277', '1:71141', '1:71153', '1:71312', '1:71518', '1:73838', '1:33303', '1:37306', '1:35109', '1:35878', '1:53862', '1:58759', '1:59427', '1:56204', '1:56635', '1:57572', '1:95903', '1:100535', '1:99080', '1:55263', '1:55418', '1:53131', '1:53191', '1:53215', '1:53223', '1:53276', '1:53565', '1:77344', '1:72494', '1:75546', '1:76253', '1:93975', '1:91102', '1:91529', '1:96198', '1:96118', '1:93554', '1:96635', '1:97759', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D04FBF28-5110-EA11-9F76-0CC47A78A30E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/001D64CA-5310-EA11-96A2-FA163EAA9AA3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/627B982F-5410-EA11-A749-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8AEFEE41-5410-EA11-816C-002590550622.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8A9BBBA-6410-EA11-AA7E-3417EBE644B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3033B37D-5B10-EA11-8A42-44A8422411EB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6CB7815A-6D10-EA11-B8E3-1458D04903A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E684B189-9811-EA11-ABDA-EC0D9A0B30D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CB37202-E310-EA11-992E-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5E63C437-7B12-EA11-B95B-002590207D00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/003A79CB-B511-EA11-85AC-801844DEF068.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/34D10FD8-E5F5-E911-A5AB-FA163EDEF72A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F4956687-3FF3-E911-A4D7-0CC47AFC3C80.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/082F7BC8-A9FE-E911-88EE-7CD30AD08E8A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0100C7C-0CF7-E911-A60F-0242AC130002.root']);