import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:54252', '1:55659', '1:57010', '1:59211', '1:56333', '1:56385', '1:56466', '1:83033', '1:83062', '1:83421', '1:83427', '1:83552', '1:83589', '1:83588', '1:82434', '1:82439', '1:82469', '1:86696', '1:86714', '1:66259', '1:71002', '1:70892', '1:70904', '1:71014', '1:71085', '1:71338', '1:71445', '1:83475', '1:83791', '1:84549', '1:65519', '1:65586', '1:65656', '1:65750', '1:65842', '1:83571', '1:86770', '1:80446', '1:80959', '1:84056', '1:7087', '1:7556', '1:24821', '1:26089', '1:26198', '1:38494', '1:38569', '1:14051', '1:24074', '1:36300', '1:36306', '1:36312', '1:36611', '1:36661', '1:36687', '1:36749', '1:36822', '1:43617', '1:43714', '1:43781', '1:44296', '1:37173', '1:35234', '1:38247', '1:38275', '1:38349', '1:43007', '1:43238', '1:43268', '1:43269', '1:43276', '1:43414', '1:41841', '1:42680', '1:42801', '1:42858', '1:5347', '1:5411', '1:5455', '1:5479', '1:19662', '1:19815', '1:19871', '1:19901', '1:19857', '1:19928', '1:20916', '1:21253', '1:26770', '1:26843', '1:27193', '1:17457', '1:17946', '1:28184', '1:28820', '1:32834', '1:37486', '1:37602', '1:37944', '1:37669', '1:37926', '1:21583', '1:26021', '1:27822', '1:27964', '1:27969', '1:32076', '1:32325', '1:27473', '1:27767', '1:27878', '1:27458', '1:27565', '1:27653', '1:27734', '1:36360', '1:40449', '1:40624', '1:39961', '1:40744', '1:94834', '1:95479', '1:39803', '1:40244', '1:40748', '1:40859', '1:41372', '1:47475', '1:49344', '1:51117', '1:51253', '1:60246', '1:59815', '1:59958', '1:60234', '1:60248', '1:60526', '1:83654', '1:83635', '1:83646', '1:83681', '1:83780', '1:87395', '1:97406', '1:97924', '1:99009', '1:99026', '1:97943', '1:2462', '1:5087', '1:5100', '1:5103', '1:5224', '1:5267', '1:5425', '1:5456', '1:5848', '1:14964', '1:68726', '1:70717', '1:73965', '1:74186', '1:75321', '1:72117', '1:72890', '1:92251', '1:93367', '1:93470', '1:93773', '1:94855', '1:12952', '1:12900', '1:14284', '1:14542', '1:14572', '1:14691', '1:19808', '1:18177', '1:18198', '1:19084', '1:67061', '1:67126', '1:88073', '1:105542', '1:72825', '1:15840', '1:15958', '1:16868', '1:16977', '1:21867', '1:24315', '1:32087', '1:32475', '1:52175', '1:54061', '1:51818', '1:61995', '1:62491', '1:68564', '1:69914', '1:81435', '1:81599', '1:35488', '1:35659', '1:36316', '1:36342', '1:36801', '1:38196', '1:42344', '1:42625', '1:42831', '1:43605', '1:43710', '1:43822', '1:46381', '1:46934', '1:67138', '1:65161', '1:67664', '1:68453', '1:81347', '1:67924', '1:68553', '1:102910', '1:37270', '1:46293', '1:46422', '1:46564', '1:41918', '1:88886', '1:87978', '1:91821', '1:47320', '1:47344', '1:47357', '1:47544', '1:47445', '1:47518', '1:47580', '1:47631', '1:47748', '1:58084', '1:58197', '1:58206', '1:58315', '1:58486', '1:58713', '1:58818', '1:58893', '1:58934', '1:59080', '1:59323', '1:93291', '1:93388', '1:93472', '1:94725', '1:63306', '1:64330', '1:64717', '1:69516', '1:69668', '1:69709', '1:69764', '1:72212', '1:74289', '1:74381', '1:80417', '1:65263', '1:65414', '1:65164', '1:65166', '1:67908', '1:68050', '1:68146', '1:68222', '1:68287', '1:68021', '1:75789', '1:92692', '1:92697', '1:95090', '1:95139', '1:95195', '1:57484', '1:57569', '1:57658', '1:57891', '1:57474', '1:60486', '1:60695', '1:61233', '1:61347', '1:100508', '1:100552', '1:100564', '1:100613', '1:100614', '1:100624', '1:100637', '1:100675', '1:62571', '1:62673', '1:62774', '1:62918', '1:76584', '1:79031', '1:79101', '1:79109', '1:79143', '1:80284', '1:80908', '1:81568', '1:95768', '1:54932', '1:54955', '1:55110', '1:55223', '1:55360', '1:55488', '1:63953', '1:60558', '1:60566', '1:69681', '1:59502', '1:59600', '1:59936', '1:59944', '1:72179', '1:72188', '1:72223', '1:72159', '1:72174', '1:77000', '1:77090', '1:77130', '1:77138', '1:77195', '1:84546', '1:84651', '1:84789', '1:60577', '1:60820', '1:61043', '1:61137', '1:65834', '1:68301', '1:68718', '1:98563', '1:98617', '1:71529', '1:71655', '1:71666', '1:71746', '1:71638', '1:71809', '1:71964', '1:77552', '1:77711', '1:77950', '1:76162', '1:92160', '1:95010', '1:95061', '1:98684', '1:71653', '1:71801', '1:71816', '1:71875', '1:71952', '1:73034', '1:99403', '1:92844', '1:92937', '1:92965', '1:92999', '1:93037', '1:93240', '1:93312', '1:99708', '1:99709', '1:99952', '1:99962', '1:85195', '1:85270', '1:85277', '1:85288', '1:85317', '1:98667', '1:98679', '1:98726', '1:98745', '1:98755', '1:98884', '1:98969', '1:92070', '1:92102', '1:92515', '1:92546', '1:92599', '1:93550', '1:19106', '1:19124', '1:19175', '1:19256', '1:15433', '1:19766', '1:19782', '1:36235', '1:43764', '1:43854', '1:43991', '1:45421', '1:45989', '1:49885', '1:49925', '1:49952', '1:50009', '1:50095', '1:50310', '1:52300', '1:52308', '1:52482', '1:52505', '1:52691', '1:63828', '1:63887', '1:63888', '1:63908', '1:67022', '1:67019', '1:64092', '1:64555', '1:64584', '1:93063', '1:93075', '1:93136', '1:93143', '1:93154', '1:75604', '1:81678', '1:81728', '1:81805', '1:81948', '1:96744', '1:99776', '1:100142', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7E950A55-7FEF-E911-99DC-441EA1616D3A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A8DBB44-A8EE-E911-B7A4-38EAA78D8ADC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8AEFCC7-7EEE-E911-AEFD-0CC47AF97150.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80B375BC-64EF-E911-B7EE-509A4C8395C6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0610918D-54EF-E911-A116-1458D04903A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7A8B894E-5BEF-E911-8B06-3CFDFE7082F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A4B986E-79EF-E911-820B-0025904AC2C4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/065D3837-F2EF-E911-9DD3-44A842B4CC7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/98C92559-C3F2-E911-A525-A4BF0128811C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78F424B9-AEF2-E911-8B73-00E081B705EA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2074DF05-35F2-E911-9B9B-3417EBE706C3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A81CFE31-E1F2-E911-8D5C-A4BF01283D2E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE40E859-04F3-E911-BD9D-A4BF012881D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E609EEE8-57F0-E911-8275-002590DBE20C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE1D09DE-96F2-E911-A3BF-3417EBE74303.root']);