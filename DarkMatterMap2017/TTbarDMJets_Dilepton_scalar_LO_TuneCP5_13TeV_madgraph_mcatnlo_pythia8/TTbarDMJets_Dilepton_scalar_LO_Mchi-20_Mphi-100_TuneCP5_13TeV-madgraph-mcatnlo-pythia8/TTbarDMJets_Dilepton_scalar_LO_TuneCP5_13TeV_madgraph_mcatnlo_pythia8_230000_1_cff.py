import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:57444', '1:59125', '1:59197', '1:83053', '1:83539', '1:83570', '1:83607', '1:83716', '1:85579', '1:86688', '1:86792', '1:86546', '1:86558', '1:65660', '1:71180', '1:71426', '1:70778', '1:84645', '1:84533', '1:84630', '1:65600', '1:65697', '1:65837', '1:65793', '1:65819', '1:86347', '1:86718', '1:86767', '1:86778', '1:83748', '1:85377', '1:78877', '1:80479', '1:80495', '1:84019', '1:84038', '1:84065', '1:84073', '1:83501', '1:83521', '1:5178', '1:7703', '1:24812', '1:24953', '1:26125', '1:26173', '1:26177', '1:38483', '1:38590', '1:38608', '1:38522', '1:38644', '1:9841', '1:14152', '1:14603', '1:14608', '1:36266', '1:36330', '1:36472', '1:36743', '1:36753', '1:36828', '1:43628', '1:43652', '1:43706', '1:43792', '1:35222', '1:36734', '1:38279', '1:43114', '1:43348', '1:43448', '1:43666', '1:44456', '1:42235', '1:42672', '1:42842', '1:46012', '1:42772', '1:42878', '1:5481', '1:5568', '1:5710', '1:5726', '1:5734', '1:19705', '1:19838', '1:19920', '1:19951', '1:21157', '1:26745', '1:26933', '1:27188', '1:17736', '1:17807', '1:17831', '1:17895', '1:18080', '1:18094', '1:26839', '1:26960', '1:28077', '1:28342', '1:28425', '1:32809', '1:37502', '1:37914', '1:18319', '1:18654', '1:20247', '1:24382', '1:27581', '1:26310', '1:32585', '1:27463', '1:27497', '1:27884', '1:39991', '1:40643', '1:39864', '1:40324', '1:40393', '1:48155', '1:50498', '1:50693', '1:51735', '1:51862', '1:59704', '1:59736', '1:59909', '1:59942', '1:60554', '1:83733', '1:87373', '1:87338', '1:87355', '1:97612', '1:97752', '1:99052', '1:2173', '1:2448', '1:2847', '1:4161', '1:5027', '1:2477', '1:66903', '1:73756', '1:73876', '1:72880', '1:74837', '1:75313', '1:75451', '1:72380', '1:93089', '1:94743', '1:12581', '1:12614', '1:12736', '1:12785', '1:12968', '1:14259', '1:19311', '1:18289', '1:18326', '1:19270', '1:19277', '1:19588', '1:20385', '1:63450', '1:104402', '1:104700', '1:72445', '1:94565', '1:83452', '1:85112', '1:19040', '1:15955', '1:16872', '1:24161', '1:32078', '1:32255', '1:32467', '1:34413', '1:39456', '1:48251', '1:48447', '1:50845', '1:61205', '1:81525', '1:81606', '1:35480', '1:35707', '1:35974', '1:36286', '1:36437', '1:38657', '1:38830', '1:43175', '1:43671', '1:46457', '1:65712', '1:71743', '1:64844', '1:70675', '1:51052', '1:58605', '1:62766', '1:63437', '1:69529', '1:67839', '1:68031', '1:68053', '1:68669', '1:98002', '1:99431', '1:65893', '1:68722', '1:64252', '1:33248', '1:33272', '1:35482', '1:36953', '1:38910', '1:42187', '1:43978', '1:46291', '1:46692', '1:46953', '1:41815', '1:41979', '1:44045', '1:44046', '1:44065', '1:44392', '1:87950', '1:88655', '1:93512', '1:47310', '1:47351', '1:47485', '1:47494', '1:47497', '1:47555', '1:47883', '1:58324', '1:58681', '1:58691', '1:58706', '1:58720', '1:58755', '1:58926', '1:59143', '1:59176', '1:98327', '1:94740', '1:94991', '1:64009', '1:64039', '1:64152', '1:64470', '1:64648', '1:64715', '1:64845', '1:64849', '1:64907', '1:69306', '1:69626', '1:69717', '1:69689', '1:69702', '1:69739', '1:74340', '1:74377', '1:80389', '1:65043', '1:65071', '1:65241', '1:65320', '1:65539', '1:78355', '1:67572', '1:67578', '1:67883', '1:67910', '1:67935', '1:67955', '1:68217', '1:68254', '1:68268', '1:68318', '1:68335', '1:75782', '1:79979', '1:79425', '1:95107', '1:95115', '1:57538', '1:57575', '1:57586', '1:57730', '1:57401', '1:60559', '1:60582', '1:60704', '1:61007', '1:61326', '1:100338', '1:100339', '1:100520', '1:62633', '1:62896', '1:76807', '1:79108', '1:79152', '1:80341', '1:80775', '1:80583', '1:80616', '1:80786', '1:80921', '1:82051', '1:93471', '1:94005', '1:54891', '1:55022', '1:55269', '1:55320', '1:55818', '1:55850', '1:56940', '1:59366', '1:60518', '1:62536', '1:59310', '1:63800', '1:67451', '1:67611', '1:60445', '1:59673', '1:59733', '1:59834', '1:71034', '1:72021', '1:77008', '1:77122', '1:77220', '1:84548', '1:84633', '1:84638', '1:60775', '1:60690', '1:60834', '1:61064', '1:61463', '1:65836', '1:65898', '1:68393', '1:68214', '1:68385', '1:98548', '1:98585', '1:99484', '1:98385', '1:98469', '1:71502', '1:71636', '1:71630', '1:71719', '1:73020', '1:79874', '1:76015', '1:76289', '1:77406', '1:77435', '1:77527', '1:77606', '1:77925', '1:76066', '1:76159', '1:76192', '1:95051', '1:95074', '1:98151', '1:98795', '1:98815', '1:100201', '1:71633', '1:71771', '1:71873', '1:92856', '1:93142', '1:100063', '1:100067', '1:100615', '1:99901', '1:99908', '1:100358', '1:85312', '1:85315', '1:98772', '1:98900', '1:98907', '1:98951', '1:98960', '1:98994', '1:98999', '1:106287', '1:92550', '1:92569', '1:92579', '1:92541', '1:92558', '1:93106', '1:93473', '1:93600', '1:19217', '1:19231', '1:19644', '1:19661', '1:36110', '1:43748', '1:43772', '1:43831', '1:43946', '1:43974', '1:49863', '1:49958', '1:50305', '1:52445', '1:52560', '1:52677', '1:52774', '1:63473', '1:63891', '1:63801', '1:63894', '1:63897', '1:67165', '1:64114', '1:64519', '1:75558', '1:75641', '1:77745', '1:81669', '1:81746', '1:81752', '1:81804', '1:81822', '1:81927', '1:96563', '1:96722', '1:96752', '1:99890', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7E950A55-7FEF-E911-99DC-441EA1616D3A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A8DBB44-A8EE-E911-B7A4-38EAA78D8ADC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8AEFCC7-7EEE-E911-AEFD-0CC47AF97150.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80B375BC-64EF-E911-B7EE-509A4C8395C6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0610918D-54EF-E911-A116-1458D04903A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7A8B894E-5BEF-E911-8B06-3CFDFE7082F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A4B986E-79EF-E911-820B-0025904AC2C4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/065D3837-F2EF-E911-9DD3-44A842B4CC7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/98C92559-C3F2-E911-A525-A4BF0128811C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78F424B9-AEF2-E911-8B73-00E081B705EA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2074DF05-35F2-E911-9B9B-3417EBE706C3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A81CFE31-E1F2-E911-8D5C-A4BF01283D2E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE40E859-04F3-E911-BD9D-A4BF012881D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E609EEE8-57F0-E911-8275-002590DBE20C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE1D09DE-96F2-E911-A3BF-3417EBE74303.root']);