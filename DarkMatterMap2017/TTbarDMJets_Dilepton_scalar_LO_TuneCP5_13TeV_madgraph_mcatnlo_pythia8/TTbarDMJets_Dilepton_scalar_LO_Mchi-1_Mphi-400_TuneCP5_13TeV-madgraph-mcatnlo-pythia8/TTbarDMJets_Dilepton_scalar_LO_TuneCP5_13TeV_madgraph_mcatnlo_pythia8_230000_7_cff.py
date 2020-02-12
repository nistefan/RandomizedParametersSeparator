import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:3299', '1:4387', '1:2503', '1:2818', '1:27501', '1:34636', '1:66049', '1:58006', '1:57764', '1:57799', '1:57638', '1:74409', '1:74959', '1:75771', '1:76354', '1:76378', '1:76616', '1:76620', '1:78496', '1:78618', '1:78631', '1:78676', '1:78885', '1:78886', '1:96840', '1:96893', '1:96970', '1:96994', '1:97038', '1:97071', '1:97088', '1:97339', '1:83844', '1:83874', '1:83918', '1:102209', '1:102291', '1:102299', '1:102355', '1:102356', '1:85990', '1:86610', '1:86671', '1:86922', '1:86975', '1:86979', '1:86994', '1:87052', '1:91956', '1:92006', '1:92030', '1:92094', '1:92128', '1:92547', '1:61355', '1:61372', '1:61507', '1:62509', '1:67069', '1:67260', '1:67265', '1:67357', '1:67376', '1:67391', '1:67406', '1:67256', '1:68213', '1:67610', '1:67749', '1:67588', '1:92629', '1:93066', '1:92945', '1:7934', '1:8926', '1:7179', '1:7015', '1:7017', '1:9680', '1:7294', '1:9616', '1:43844', '1:45745', '1:46840', '1:40050', '1:48151', '1:21143', '1:21164', '1:24225', '1:24246', '1:24524', '1:33886', '1:32991', '1:33670', '1:33692', '1:91189', '1:91297', '1:91447', '1:91530', '1:86362', '1:88131', '1:51080', '1:63356', '1:69465', '1:69474', '1:86812', '1:87842', '1:88099', '1:86124', '1:91509', '1:91819', '1:92577', '1:93991', '1:8935', '1:12842', '1:14532', '1:76111', '1:80915', '1:5619', '1:5415', '1:7005', '1:10427', '1:15102', '1:14094', '1:14105', '1:14120', '1:14124', '1:14258', '1:27271', '1:16564', '1:36697', '1:38903', '1:42079', '1:42090', '1:42215', '1:42775', '1:42824', '1:47654', '1:67197', '1:61636', '1:63752', '1:58896', '1:67044', '1:87934', '1:91851', '1:92752', '1:92760', '1:2743', '1:14466', '1:33699', '1:45546', '1:48991', '1:49448', '1:3339', '1:7021', '1:9013', '1:9540', '1:9679', '1:7773', '1:7813', '1:8706', '1:10660', '1:50180', '1:47126', '1:48304', '1:42957', '1:45143', '1:45325', '1:62010', '1:63628', '1:67408', '1:64008', '1:65812', '1:66597', '1:66739', '1:70826', '1:56627', '1:60095', '1:68197', '1:68472', '1:61299', '1:62498', '1:41905', '1:49557', '1:84563', '1:84965', '1:84981', '1:76160', '1:76380', '1:77029', '1:78732', '1:79622', '1:80949', '1:80979', '1:98452', '1:100942', '1:104876', '1:105525', '1:95625', '1:97743', '1:98145', '1:54544', '1:54840', '1:54951', '1:55097', '1:75079', '1:75191', '1:75200', '1:75211', '1:75504', '1:75725', '1:78953', '1:81036', '1:81126', '1:81216', '1:81579', '1:81587', '1:81276', '1:81289', '1:94034', '1:104372', '1:104396', '1:104414', '1:104698', '1:104788', '1:100009', '1:100029', '1:100302', '1:100316', '1:100337', '1:100691', '1:100693', '1:100779', '1:100817', '1:100851', '1:100873', '1:100712', '1:100775', '1:100796', '1:100822', '1:103203', '1:102233', '1:98040', '1:61134', '1:61159', '1:61419', '1:61572', '1:86482', '1:87103', '1:87186', '1:76251', '1:76725', '1:76738', '1:87997', '1:88024', '1:88045', '1:33011', '1:35626', '1:52796', '1:83032', '1:87761', '1:52207', '1:52898', '1:54057', '1:54069', '1:54425', '1:54459', '1:54555', '1:54661', '1:65025', '1:65162', '1:66579', '1:40270', '1:47075', '1:48918', '1:50280', '1:73815', '1:71520', '1:73306', '1:73444', '1:79022', '1:82726', '1:85773', '1:86086', '1:54648', '1:54685', '1:54736', '1:54737', '1:54759', '1:57874', '1:57987', '1:57582', '1:57833', '1:57909', '1:57937', '1:58060', '1:58129', '1:58145', '1:76374', '1:66100', '1:70436', '1:66267', '1:66320', '1:66377', '1:66713', '1:73204', '1:73344', '1:73429', '1:73516', '1:73529', '1:73533', '1:73544', '1:73623', '1:73694', '1:74123', '1:86181', '1:86332', '1:87283', '1:87318', '1:66392', '1:66476', '1:66489', '1:66556', '1:66827', '1:66979', '1:83046', '1:83123', '1:83341', '1:105633', '1:105669', '1:105635', '1:12170', '1:16410', '1:82669', '1:82929', '1:82986', '1:82988', '1:82850', '1:82865', '1:82953', '1:102502', '1:102616', '1:102667', '1:102701', '1:48972', '1:49029', '1:49224', '1:49229', '1:77428', '1:77510', '1:77788', '1:19182', '1:19198', '1:20058', '1:48626', '1:55162', '1:55203', '1:55357', '1:55445', '1:55458', '1:55480', '1:55606', '1:55635', '1:55795', '1:56364', '1:37750', '1:49416', '1:49509', '1:49871', '1:50688', '1:80224', '1:80236', '1:80285', '1:80363', '1:80450', '1:80456', '1:93768', '1:84081', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CA7CE758-D1F7-E911-B277-F01FAFD8F7D6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C1D320E-78EF-E911-A729-509A4C9EF924.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3E1280BB-BBF9-E911-80A0-FA163EA79D8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0E73436E-79EF-E911-89CC-E0071B73C630.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C45C6C1C-8C10-EA11-9B52-0025907D1D6C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F67A5D3B-B7F3-E911-9613-28924A3504DA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE1665D5-CBF7-E911-8868-14187741278B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F805B571-9702-EA11-AE26-B083FED138B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC6B26A7-88F2-E911-9CDE-C4544423E320.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7810BEF1-97F3-E911-8096-089E0158CDED.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8EB6E369-98F3-E911-9E0F-20CF3019DF13.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D074ADB4-D9F2-E911-B16F-1418774A2C9C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E8D7450-7FEF-E911-9BF4-509A4C9EF923.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72D74153-AB02-EA11-8630-0CC47AFCC41A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/34767E6C-04F3-E911-BB76-848F69FD0EAB.root']);