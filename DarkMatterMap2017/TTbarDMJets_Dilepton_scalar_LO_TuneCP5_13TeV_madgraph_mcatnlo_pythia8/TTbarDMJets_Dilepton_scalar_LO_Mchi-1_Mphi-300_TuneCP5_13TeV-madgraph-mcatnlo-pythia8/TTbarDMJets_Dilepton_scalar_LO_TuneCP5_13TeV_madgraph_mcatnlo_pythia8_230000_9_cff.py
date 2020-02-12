import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:51222', '1:51288', '1:51291', '1:51295', '1:51486', '1:67374', '1:67566', '1:67867', '1:68009', '1:69152', '1:92506', '1:92722', '1:78067', '1:78092', '1:78120', '1:82468', '1:79158', '1:81184', '1:82493', '1:82550', '1:82101', '1:83025', '1:83072', '1:83114', '1:85038', '1:85052', '1:85095', '1:85116', '1:85159', '1:726', '1:677', '1:685', '1:1311', '1:1441', '1:2061', '1:2734', '1:2738', '1:2988', '1:2994', '1:2996', '1:3752', '1:4698', '1:98932', '1:99842', '1:99846', '1:99868', '1:38353', '1:40014', '1:40039', '1:40107', '1:49233', '1:48462', '1:49244', '1:53915', '1:54033', '1:54434', '1:53819', '1:53834', '1:53844', '1:53938', '1:54066', '1:79836', '1:80800', '1:80821', '1:80866', '1:82364', '1:82409', '1:82430', '1:95693', '1:96049', '1:96063', '1:98639', '1:99088', '1:99120', '1:14717', '1:14758', '1:14780', '1:15914', '1:16097', '1:16624', '1:16973', '1:17231', '1:17329', '1:19805', '1:20186', '1:20414', '1:20952', '1:20423', '1:20706', '1:20846', '1:45357', '1:45723', '1:47757', '1:47830', '1:76242', '1:79353', '1:79361', '1:105544', '1:105749', '1:2526', '1:5301', '1:7076', '1:7454', '1:7744', '1:2846', '1:18455', '1:32888', '1:32920', '1:33441', '1:34595', '1:37615', '1:56859', '1:60948', '1:61632', '1:68097', '1:7711', '1:7922', '1:7927', '1:8246', '1:8390', '1:8610', '1:8899', '1:10177', '1:16583', '1:15129', '1:17319', '1:12695', '1:12839', '1:87790', '1:93286', '1:96117', '1:103537', '1:99619', '1:100662', '1:64336', '1:64403', '1:64413', '1:64486', '1:64795', '1:65702', '1:67085', '1:67183', '1:67226', '1:65743', '1:65909', '1:67051', '1:67275', '1:67296', '1:66076', '1:68110', '1:68111', '1:68306', '1:68931', '1:69084', '1:87897', '1:88185', '1:88205', '1:94066', '1:93997', '1:94829', '1:94531', '1:94562', '1:102504', '1:102508', '1:102594', '1:102678', '1:92923', '1:93048', '1:64993', '1:80068', '1:80156', '1:79013', '1:79126', '1:79169', '1:79208', '1:82616', '1:82594', '1:82623', '1:82631', '1:82691', '1:38259', '1:38371', '1:38431', '1:38443', '1:38576', '1:38711', '1:43128', '1:40307', '1:45131', '1:45075', '1:45283', '1:45344', '1:45379', '1:44468', '1:45269', '1:45189', '1:45300', '1:46660', '1:46757', '1:46785', '1:46825', '1:46944', '1:49780', '1:53808', '1:54076', '1:54888', '1:55564', '1:57723', '1:79340', '1:78439', '1:73119', '1:73179', '1:73297', '1:73364', '1:73512', '1:73568', '1:73607', '1:91671', '1:76564', '1:76748', '1:76832', '1:73405', '1:73424', '1:96779', '1:97961', '1:95230', '1:95354', '1:95368', '1:95381', '1:95937', '1:100225', '1:99253', '1:104193', '1:56283', '1:59767', '1:58443', '1:61101', '1:58512', '1:68293', '1:69094', '1:60227', '1:60817', '1:61806', '1:72193', '1:77975', '1:61378', '1:64239', '1:70837', '1:71883', '1:71969', '1:71446', '1:73477', '1:71195', '1:65177', '1:65266', '1:65501', '1:68543', '1:69960', '1:71911', '1:88102', '1:76403', '1:82117', '1:91502', '1:91506', '1:91538', '1:91618', '1:60859', '1:60986', '1:105945', '1:17665', '1:17556', '1:18795', '1:17223', '1:17701', '1:17748', '1:7257', '1:7418', '1:14510', '1:10460', '1:10477', '1:10555', '1:12350', '1:12379', '1:12808', '1:5192', '1:5219', '1:5311', '1:5383', '1:7014', '1:9051', '1:9283', '1:8301', '1:9878', '1:9760', '1:68717', '1:69357', '1:69359', '1:69372', '1:69384', '1:69392', '1:69461', '1:69483', '1:69505', '1:69645', '1:85547', '1:85576', '1:85619', '1:85630', '1:85715', '1:85719', '1:85879', '1:85908', '1:85654', '1:85678', '1:85783', '1:91469', '1:94197', '1:94382', '1:104719', '1:50659', '1:52212', '1:52303', '1:52245', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/06F65C32-13F3-E911-AC5A-002590DE6E30.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4253ADC4-03F5-E911-AFEA-AC1F6B0DE0A0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0014CD18-06F6-E911-8B27-FA163E69BD36.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E66B73CD-70F7-E911-8EBA-E0071B7A18F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/043AF729-4A10-EA11-B2D6-0CC47AFF2492.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/68454F20-060A-EA11-A63A-AC1F6BAC816C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D2B1428C-88F2-E911-B4D4-3417EBE705CD.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3C9F3E3A-5600-EA11-B8FE-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE1AA428-17F0-E911-A0AE-0CC47A4DEDB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A217F84B-F6F2-E911-84C6-A0369F5BD8D4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC608F2A-9802-EA11-984E-D48564599C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38FDE37B-BEFC-E911-B96A-001E67E5EDBB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/48D3300C-5110-EA11-A284-00259090822A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40DCE1CF-C002-EA11-B8F4-0CC47AFF0220.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8CD8C04A-5210-EA11-8222-0025904B04A8.root']);