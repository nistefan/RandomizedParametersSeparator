import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:34215', '1:39773', '1:44298', '1:40921', '1:44010', '1:45506', '1:47994', '1:56525', '1:57953', '1:56043', '1:57134', '1:52876', '1:55484', '1:55281', '1:55295', '1:67549', '1:59901', '1:82738', '1:79488', '1:81623', '1:82536', '1:86516', '1:96780', '1:100359', '1:75574', '1:75696', '1:78146', '1:78636', '1:78672', '1:87920', '1:100064', '1:102101', '1:19439', '1:20167', '1:21016', '1:24530', '1:76188', '1:76563', '1:76706', '1:76573', '1:76619', '1:76877', '1:76990', '1:77882', '1:99447', '1:99549', '1:102555', '1:26835', '1:28057', '1:19425', '1:27920', '1:32386', '1:100374', '1:57857', '1:69641', '1:60658', '1:69920', '1:67747', '1:69221', '1:69399', '1:97192', '1:95606', '1:98254', '1:99309', '1:100200', '1:37335', '1:37876', '1:73073', '1:73196', '1:73235', '1:73342', '1:71941', '1:72314', '1:72758', '1:75328', '1:75547', '1:76538', '1:84397', '1:83592', '1:84916', '1:85725', '1:85776', '1:86174', '1:86294', '1:85991', '1:87532', '1:68832', '1:69621', '1:69835', '1:69907', '1:62001', '1:65302', '1:84484', '1:72799', '1:75254', '1:84641', '1:84877', '1:81474', '1:18041', '1:33755', '1:33781', '1:33910', '1:35008', '1:35088', '1:40045', '1:44998', '1:47174', '1:42289', '1:42372', '1:42413', '1:42434', '1:58487', '1:58619', '1:58627', '1:58683', '1:33599', '1:34081', '1:37726', '1:44484', '1:44729', '1:44950', '1:48894', '1:47278', '1:47374', '1:106007', '1:104614', '1:105032', '1:106160', '1:106312', '1:104680', '1:106259', '1:104292', '1:104883', '1:14689', '1:14709', '1:14787', '1:16901', '1:97021', '1:98434', '1:98981', '1:98996', '1:105810', '1:105828', '1:105998', '1:105835', '1:105862', '1:17852', '1:17905', '1:17642', '1:17705', '1:17720', '1:17747', '1:17820', '1:17922', '1:20440', '1:20559', '1:20639', '1:20723', '1:20771', '1:20929', '1:75286', '1:105984', '1:79346', '1:79358', '1:79521', '1:79558', '1:3596', '1:9506', '1:33043', '1:34399', '1:35630', '1:45931', '1:71973', '1:19512', '1:20539', '1:21190', '1:17839', '1:18424', '1:20698', '1:5364', '1:5369', '1:5869', '1:40567', '1:51536', '1:52891', '1:48191', '1:49373', '1:51690', '1:41916', '1:61600', '1:62032', '1:50592', '1:48057', '1:60926', '1:60896', '1:18268', '1:32849', '1:33496', '1:36075', '1:33829', '1:34999', '1:35520', '1:37036', '1:37040', '1:46425', '1:24876', '1:42982', '1:83297', '1:83679', '1:40715', '1:41701', '1:44174', '1:44679', '1:47905', '1:44567', '1:34980', '1:42617', '1:38853', '1:46037', '1:76469', '1:77665', '1:78526', '1:78635', '1:78993', '1:94724', '1:1009', '1:1310', '1:1342', '1:49264', '1:51078', '1:42784', '1:47759', '1:40853', '1:103097', '1:17745', '1:26554', '1:27771', '1:28082', '1:28190', '1:26565', '1:26929', '1:27833', '1:63560', '1:69389', '1:64614', '1:64754', '1:68164', '1:69741', '1:87552', '1:100409', '1:103346', '1:105816', '1:64484', '1:66734', '1:66974', '1:70279', '1:71259', '1:73862', '1:64053', '1:64442', '1:80180', '1:85814', '1:103977', '1:104823', '1:103221', '1:104032', '1:5198', '1:5813', '1:9532', '1:7434', '1:34558', '1:32045', '1:34221', '1:34224', '1:34345', '1:36874', '1:96910', '1:98624', '1:100012', '1:35542', '1:38015', '1:42188', '1:42389', '1:42836', '1:46762', '1:46959', '1:68108', '1:43860', '1:45476', '1:46197', '1:46778', '1:39346', '1:39966', '1:44837', '1:48654', '1:93424', '1:91321', '1:82881', '1:83308', '1:83404', '1:85036', '1:82467', '1:86801', '1:87699', '1:85629', '1:85723', '1:85734', '1:85857', '1:85884', '1:100373', '1:98280', '1:98497', '1:98642', '1:100503', '1:100507', '1:17688', '1:53501', '1:97666', '1:97693', '1:97982', '1:99144', '1:106033', '1:45334', '1:91665', '1:92075', '1:92152', '1:93067', '1:65658', '1:66219', '1:66222', '1:80403', '1:65906', '1:51190', '1:52148', '1:50247', '1:50878', '1:55846', '1:92139', '1:105657', '1:105790', '1:106018', '1:95028', '1:102514', '1:105666', '1:105748', '1:105832', '1:105946', '1:96875', '1:93831', '1:97798', '1:54240', '1:57976', '1:56579', '1:56775', '1:56928', '1:57482', '1:58304', '1:58550', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE6DCC6F-9702-EA11-8C9E-246E96D14D4C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/629AE047-9B03-EA11-AF08-0090FAA57770.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/74BFCEF5-7203-EA11-AC31-00259073E53A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8D6CEA6-5D03-EA11-9F3D-D48564593FA8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FED7A530-8703-EA11-9953-008CFAF28F22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4AC458D-3904-EA11-819B-0CC47AFF02CC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5AD9493D-D803-EA11-A326-002481CFE864.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8B96E8C-1B0B-EA11-B3FA-0CC47A4D75F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/548DD76C-8E0A-EA11-A159-0CC47A4C8E0E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4C7CE199-7F0A-EA11-B6D3-AC1F6BAC7EAC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A61B1E1C-3C0E-EA11-ADCF-506B4BB134E6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA16D4FD-B40E-EA11-AA73-AC1F6B1AEF94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E5B1D6C-8F0B-EA11-A380-FA163E1B56E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/06492256-3210-EA11-93C2-44A842BFA94B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D8A4A322-940F-EA11-9A4C-1CC1DE050110.root']);