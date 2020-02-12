import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1711', '1:4049', '1:2346', '1:2506', '1:2577', '1:21810', '1:24678', '1:24908', '1:27216', '1:27561', '1:27576', '1:58042', '1:58112', '1:58613', '1:94904', '1:56806', '1:58322', '1:72293', '1:76614', '1:78497', '1:78502', '1:78506', '1:78573', '1:78736', '1:78917', '1:96935', '1:96838', '1:96848', '1:96917', '1:96928', '1:96972', '1:97041', '1:83871', '1:102288', '1:102305', '1:102320', '1:102352', '1:86458', '1:86550', '1:86575', '1:86591', '1:86598', '1:86614', '1:86619', '1:86645', '1:86670', '1:86960', '1:86968', '1:86989', '1:87088', '1:91992', '1:92096', '1:92105', '1:92356', '1:92422', '1:92429', '1:61288', '1:61432', '1:61538', '1:61565', '1:61506', '1:61569', '1:61681', '1:61989', '1:67462', '1:67276', '1:67978', '1:67303', '1:67617', '1:67746', '1:67807', '1:67808', '1:92618', '1:92755', '1:92783', '1:93076', '1:92871', '1:2534', '1:5713', '1:9463', '1:7677', '1:9693', '1:7706', '1:39738', '1:48288', '1:52263', '1:52035', '1:21224', '1:32963', '1:34134', '1:34142', '1:34410', '1:94305', '1:86435', '1:87610', '1:88203', '1:39061', '1:39421', '1:46057', '1:65480', '1:69327', '1:69445', '1:69414', '1:69485', '1:85488', '1:91107', '1:91283', '1:93398', '1:94868', '1:8554', '1:8916', '1:10235', '1:16400', '1:16741', '1:16744', '1:16892', '1:14986', '1:16556', '1:75828', '1:78883', '1:100368', '1:7335', '1:7094', '1:5121', '1:15080', '1:15087', '1:47106', '1:9813', '1:16425', '1:16451', '1:21870', '1:26031', '1:26088', '1:24129', '1:26297', '1:26572', '1:26584', '1:36914', '1:37305', '1:37748', '1:38592', '1:42057', '1:42902', '1:67828', '1:62728', '1:63239', '1:63579', '1:60433', '1:62898', '1:62914', '1:63981', '1:67520', '1:58184', '1:63409', '1:88296', '1:4609', '1:7649', '1:15027', '1:21193', '1:38499', '1:39232', '1:57175', '1:2942', '1:5687', '1:8143', '1:8675', '1:9707', '1:10702', '1:12041', '1:49838', '1:39676', '1:48409', '1:44686', '1:48907', '1:36929', '1:46347', '1:46991', '1:45590', '1:45596', '1:45983', '1:61223', '1:62157', '1:71561', '1:62992', '1:69788', '1:40947', '1:78708', '1:81887', '1:84430', '1:84725', '1:84835', '1:84956', '1:76387', '1:80026', '1:80573', '1:80577', '1:96977', '1:97555', '1:97746', '1:96541', '1:99775', '1:98564', '1:55076', '1:55084', '1:55106', '1:55148', '1:75106', '1:75172', '1:75175', '1:75579', '1:78951', '1:81091', '1:81557', '1:82521', '1:84045', '1:81225', '1:81235', '1:81242', '1:81293', '1:81297', '1:93566', '1:94081', '1:94138', '1:104831', '1:106272', '1:106336', '1:104417', '1:104536', '1:104650', '1:104676', '1:100035', '1:100181', '1:100309', '1:100323', '1:100378', '1:100392', '1:100408', '1:100426', '1:100663', '1:100678', '1:100709', '1:100837', '1:100840', '1:100903', '1:100754', '1:100759', '1:100963', '1:102131', '1:49612', '1:49626', '1:49630', '1:97102', '1:97138', '1:97631', '1:98026', '1:98038', '1:61044', '1:61255', '1:61189', '1:61270', '1:86519', '1:86542', '1:87226', '1:88026', '1:35159', '1:36058', '1:37102', '1:54063', '1:87093', '1:94920', '1:52952', '1:53488', '1:54231', '1:54611', '1:66825', '1:44448', '1:44844', '1:41793', '1:48731', '1:73459', '1:98488', '1:103190', '1:104348', '1:80047', '1:81113', '1:84196', '1:82220', '1:82552', '1:66534', '1:65984', '1:54589', '1:54755', '1:57425', '1:57506', '1:57901', '1:57423', '1:57588', '1:57821', '1:57931', '1:57965', '1:58003', '1:58015', '1:64249', '1:68841', '1:71241', '1:72706', '1:66720', '1:66383', '1:66721', '1:73590', '1:73372', '1:73391', '1:73452', '1:73534', '1:73541', '1:73591', '1:73601', '1:87211', '1:87220', '1:87293', '1:66425', '1:66656', '1:66671', '1:66482', '1:66567', '1:83202', '1:83242', '1:83345', '1:83369', '1:83398', '1:105658', '1:105612', '1:105674', '1:10941', '1:12035', '1:82674', '1:82790', '1:84979', '1:82854', '1:102518', '1:102559', '1:102589', '1:102603', '1:49166', '1:76989', '1:77043', '1:77778', '1:77845', '1:19136', '1:20148', '1:20178', '1:20236', '1:48490', '1:55414', '1:55688', '1:56344', '1:82661', '1:85584', '1:85613', '1:86183', '1:49056', '1:49384', '1:49481', '1:49661', '1:80682', '1:80879', '1:81062', '1:81117', '1:80254', '1:80311', '1:80474', '1:93720', '1:93729', '1:98818', '1:98829', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CA7CE758-D1F7-E911-B277-F01FAFD8F7D6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C1D320E-78EF-E911-A729-509A4C9EF924.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3E1280BB-BBF9-E911-80A0-FA163EA79D8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0E73436E-79EF-E911-89CC-E0071B73C630.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C45C6C1C-8C10-EA11-9B52-0025907D1D6C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F67A5D3B-B7F3-E911-9613-28924A3504DA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE1665D5-CBF7-E911-8868-14187741278B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F805B571-9702-EA11-AE26-B083FED138B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC6B26A7-88F2-E911-9CDE-C4544423E320.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7810BEF1-97F3-E911-8096-089E0158CDED.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8EB6E369-98F3-E911-9E0F-20CF3019DF13.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D074ADB4-D9F2-E911-B16F-1418774A2C9C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E8D7450-7FEF-E911-9BF4-509A4C9EF923.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72D74153-AB02-EA11-8630-0CC47AFCC41A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/34767E6C-04F3-E911-BB76-848F69FD0EAB.root']);