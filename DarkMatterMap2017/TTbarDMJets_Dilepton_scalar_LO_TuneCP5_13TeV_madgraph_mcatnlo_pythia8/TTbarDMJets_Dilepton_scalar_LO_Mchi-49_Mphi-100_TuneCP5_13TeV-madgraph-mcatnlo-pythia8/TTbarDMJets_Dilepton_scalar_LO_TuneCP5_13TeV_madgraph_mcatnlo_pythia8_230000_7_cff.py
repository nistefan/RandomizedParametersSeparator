import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:128', '1:3122', '1:3165', '1:3411', '1:154', '1:2082', '1:2105', '1:2305', '1:2459', '1:21938', '1:24020', '1:27377', '1:27478', '1:56609', '1:58376', '1:57483', '1:88629', '1:57727', '1:58011', '1:55689', '1:72945', '1:75589', '1:75971', '1:76456', '1:76470', '1:76544', '1:78558', '1:78760', '1:78799', '1:96865', '1:96979', '1:97086', '1:97317', '1:83897', '1:83963', '1:84360', '1:84368', '1:84384', '1:102163', '1:102215', '1:102418', '1:102273', '1:102332', '1:86577', '1:86916', '1:86947', '1:86970', '1:87072', '1:87087', '1:91980', '1:92000', '1:92342', '1:92438', '1:92521', '1:61375', '1:67712', '1:67742', '1:93021', '1:92996', '1:93335', '1:7009', '1:7229', '1:5550', '1:5858', '1:9519', '1:9562', '1:9763', '1:7833', '1:43734', '1:48895', '1:20563', '1:20675', '1:20709', '1:21148', '1:24621', '1:34016', '1:34022', '1:34108', '1:33254', '1:33505', '1:33732', '1:33840', '1:86755', '1:87951', '1:91276', '1:48126', '1:63596', '1:69177', '1:69656', '1:69710', '1:69928', '1:87441', '1:87890', '1:88012', '1:86464', '1:87004', '1:87809', '1:94260', '1:93353', '1:94246', '1:91131', '1:12956', '1:16015', '1:15365', '1:72014', '1:72786', '1:81723', '1:5897', '1:7536', '1:7538', '1:7589', '1:5673', '1:5684', '1:4107', '1:14392', '1:15064', '1:14093', '1:14215', '1:9889', '1:9908', '1:16531', '1:16532', '1:16575', '1:19829', '1:24321', '1:24623', '1:24834', '1:24687', '1:36688', '1:37735', '1:38753', '1:42308', '1:47659', '1:61666', '1:67614', '1:63048', '1:59407', '1:61723', '1:62250', '1:62748', '1:62863', '1:63411', '1:86118', '1:86185', '1:91390', '1:92373', '1:94688', '1:40533', '1:52982', '1:45074', '1:5028', '1:7290', '1:7592', '1:9487', '1:47146', '1:39746', '1:48423', '1:42728', '1:43298', '1:43554', '1:45539', '1:56331', '1:62048', '1:61402', '1:63385', '1:68091', '1:65720', '1:68114', '1:68187', '1:67567', '1:47511', '1:84555', '1:84568', '1:79198', '1:96839', '1:97662', '1:98228', '1:104050', '1:104256', '1:96675', '1:97686', '1:54576', '1:54674', '1:54688', '1:55019', '1:75053', '1:75074', '1:75628', '1:78943', '1:78950', '1:81150', '1:78711', '1:81310', '1:93563', '1:94159', '1:104558', '1:104795', '1:106232', '1:106326', '1:104441', '1:104552', '1:104721', '1:100399', '1:100440', '1:100714', '1:100789', '1:100793', '1:100786', '1:100853', '1:100862', '1:102547', '1:102721', '1:97574', '1:97781', '1:61186', '1:61202', '1:67086', '1:86416', '1:86431', '1:86456', '1:86475', '1:86508', '1:86518', '1:87182', '1:87187', '1:76742', '1:88003', '1:41814', '1:84707', '1:85556', '1:52475', '1:52641', '1:52805', '1:54219', '1:54510', '1:54546', '1:64174', '1:64575', '1:44382', '1:47035', '1:39906', '1:44362', '1:47415', '1:39071', '1:48240', '1:50255', '1:73299', '1:71206', '1:71676', '1:71783', '1:73110', '1:97011', '1:84154', '1:85533', '1:85667', '1:64847', '1:65530', '1:64451', '1:54582', '1:54751', '1:57840', '1:57990', '1:58039', '1:64812', '1:66279', '1:66323', '1:66324', '1:66359', '1:73384', '1:73508', '1:73624', '1:85916', '1:86313', '1:86381', '1:87269', '1:87271', '1:87305', '1:66391', '1:66471', '1:66513', '1:66864', '1:66944', '1:66968', '1:83998', '1:82838', '1:83034', '1:83058', '1:83074', '1:83096', '1:83222', '1:83228', '1:105651', '1:105609', '1:105655', '1:10932', '1:10918', '1:16399', '1:82682', '1:82771', '1:82775', '1:84984', '1:84985', '1:84999', '1:82868', '1:102613', '1:12776', '1:48742', '1:49208', '1:49216', '1:77490', '1:77578', '1:77632', '1:77642', '1:77644', '1:77650', '1:77753', '1:77798', '1:19137', '1:19243', '1:20011', '1:20024', '1:20096', '1:20098', '1:20142', '1:20161', '1:49000', '1:55219', '1:55260', '1:55289', '1:55364', '1:55632', '1:55712', '1:55774', '1:56352', '1:79081', '1:82139', '1:83806', '1:86208', '1:37743', '1:37880', '1:49271', '1:49378', '1:49526', '1:49782', '1:49799', '1:49889', '1:49545', '1:49753', '1:80194', '1:80451', '1:81109', '1:80259', '1:80453', '1:80455', '1:94224', '1:86256', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CA7CE758-D1F7-E911-B277-F01FAFD8F7D6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C1D320E-78EF-E911-A729-509A4C9EF924.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3E1280BB-BBF9-E911-80A0-FA163EA79D8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0E73436E-79EF-E911-89CC-E0071B73C630.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C45C6C1C-8C10-EA11-9B52-0025907D1D6C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F67A5D3B-B7F3-E911-9613-28924A3504DA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE1665D5-CBF7-E911-8868-14187741278B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F805B571-9702-EA11-AE26-B083FED138B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC6B26A7-88F2-E911-9CDE-C4544423E320.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7810BEF1-97F3-E911-8096-089E0158CDED.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8EB6E369-98F3-E911-9E0F-20CF3019DF13.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D074ADB4-D9F2-E911-B16F-1418774A2C9C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E8D7450-7FEF-E911-9BF4-509A4C9EF923.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72D74153-AB02-EA11-8630-0CC47AFCC41A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/34767E6C-04F3-E911-BB76-848F69FD0EAB.root']);