import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:47695', '1:47736', '1:51400', '1:55225', '1:55621', '1:55757', '1:57044', '1:84155', '1:84242', '1:81640', '1:81824', '1:8575', '1:9117', '1:9166', '1:9531', '1:9627', '1:9674', '1:10766', '1:97713', '1:104112', '1:104429', '1:104858', '1:850', '1:1059', '1:5285', '1:8472', '1:8934', '1:14957', '1:16237', '1:1206', '1:1442', '1:480', '1:782', '1:4658', '1:60255', '1:61138', '1:60188', '1:62100', '1:63021', '1:63787', '1:105941', '1:71440', '1:71486', '1:71509', '1:71565', '1:71580', '1:98046', '1:98123', '1:119', '1:14119', '1:18332', '1:18354', '1:32022', '1:64669', '1:38502', '1:45041', '1:40469', '1:45191', '1:45692', '1:96040', '1:98162', '1:102566', '1:98732', '1:102302', '1:103150', '1:97857', '1:97873', '1:97032', '1:97044', '1:97745', '1:97907', '1:98910', '1:97425', '1:21161', '1:21296', '1:21403', '1:21453', '1:21564', '1:94189', '1:94355', '1:93310', '1:83760', '1:88556', '1:88990', '1:15806', '1:15931', '1:16310', '1:16433', '1:28691', '1:39636', '1:39770', '1:42524', '1:48300', '1:48360', '1:43340', '1:43350', '1:43472', '1:43544', '1:43650', '1:43680', '1:84872', '1:59237', '1:62853', '1:62885', '1:63203', '1:63333', '1:63357', '1:59906', '1:55902', '1:55930', '1:55989', '1:56062', '1:55986', '1:88559', '1:94083', '1:94528', '1:95456', '1:95588', '1:97870', '1:16109', '1:16152', '1:16352', '1:16543', '1:16658', '1:16669', '1:16690', '1:34436', '1:16934', '1:17077', '1:17597', '1:21724', '1:21776', '1:21793', '1:21340', '1:21482', '1:21469', '1:21897', '1:45509', '1:45551', '1:63200', '1:63323', '1:63555', '1:63872', '1:63899', '1:67002', '1:67043', '1:63510', '1:63753', '1:48582', '1:51429', '1:54015', '1:56813', '1:59154', '1:59155', '1:54034', '1:54476', '1:54466', '1:58793', '1:61235', '1:62258', '1:4943', '1:28481', '1:33747', '1:26721', '1:16563', '1:16585', '1:16777', '1:73773', '1:73399', '1:73523', '1:34473', '1:37089', '1:36359', '1:36408', '1:55721', '1:59896', '1:53687', '1:55108', '1:56582', '1:56905', '1:57766', '1:59256', '1:92934', '1:54113', '1:54948', '1:55023', '1:75535', '1:75975', '1:76475', '1:77293', '1:72784', '1:77507', '1:92192', '1:93795', '1:93983', '1:96305', '1:95008', '1:93560', '1:96151', '1:99289', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D04FBF28-5110-EA11-9F76-0CC47A78A30E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/001D64CA-5310-EA11-96A2-FA163EAA9AA3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/627B982F-5410-EA11-A749-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8AEFEE41-5410-EA11-816C-002590550622.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8A9BBBA-6410-EA11-AA7E-3417EBE644B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3033B37D-5B10-EA11-8A42-44A8422411EB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6CB7815A-6D10-EA11-B8E3-1458D04903A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E684B189-9811-EA11-ABDA-EC0D9A0B30D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CB37202-E310-EA11-992E-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5E63C437-7B12-EA11-B95B-002590207D00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/003A79CB-B511-EA11-85AC-801844DEF068.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/34D10FD8-E5F5-E911-A5AB-FA163EDEF72A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F4956687-3FF3-E911-A4D7-0CC47AFC3C80.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/082F7BC8-A9FE-E911-88EE-7CD30AD08E8A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0100C7C-0CF7-E911-A60F-0242AC130002.root']);