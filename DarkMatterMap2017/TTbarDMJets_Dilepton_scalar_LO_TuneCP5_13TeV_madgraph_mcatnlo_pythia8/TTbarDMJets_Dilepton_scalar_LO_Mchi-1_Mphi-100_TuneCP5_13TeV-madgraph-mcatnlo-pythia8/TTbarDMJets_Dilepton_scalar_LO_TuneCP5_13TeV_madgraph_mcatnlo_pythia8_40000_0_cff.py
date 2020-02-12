import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11297', '1:11694', '1:11737', '1:11767', '1:11804', '1:11810', '1:11938', '1:11963', '1:11684', '1:11721', '1:11742', '1:11822', '1:11837', '1:11907', '1:11956', '1:13329', '1:13049', '1:13285', '1:13377', '1:13414', '1:13429', '1:13502', '1:13596', '1:13632', '1:13202', '1:13311', '1:13398', '1:13416', '1:13449', '1:13445', '1:13503', '1:13513', '1:13801', '1:13768', '1:13782', '1:13807', '1:13817', '1:13839', '1:13860', '1:13979', '1:13852', '1:13976', '1:22076', '1:22077', '1:22063', '1:13434', '1:25455', '1:25544', '1:25448', '1:25525', '1:25680', '1:25725', '1:25733', '1:25742', '1:25913', '1:25613', '1:25749', '1:25903', '1:29226', '1:29230', '1:29260', '1:29274', '1:29280', '1:29448', '1:29493', '1:29584', '1:30062', '1:30047', '1:30048', '1:30069', '1:30081', '1:30100', '1:31145', '1:31147', '1:90118', '1:30194', '1:30138', '1:30153', '1:90950', '1:101990', '1:101991', '1:11046', '1:11148', '1:11393', '1:11421', '1:11298', '1:11530', '1:11911', '1:13254', '1:13678', '1:13955', '1:22298', '1:22995', '1:22996', '1:23000', '1:29010', '1:31124', '1:31141', '1:31164', '1:31380', '1:29515', '1:29521', '1:29570', '1:29594', '1:29596', '1:29609', '1:29571', '1:29575', '1:29654', '1:29663', '1:29634', '1:30180', '1:30315', '1:30321', '1:30471', '1:30384', '1:30387', '1:30592', '1:30600', '1:31239', '1:31214', '1:31424', '1:31439', '1:31929', '1:31950', '1:31957', '1:31993', '1:31500', '1:31448', '1:31463', '1:31531', '1:31542', '1:31600', '1:31582', '1:31622', '1:31938', '1:31620', '1:31644', '1:31652', '1:31687', '1:90024', '1:101030', '1:101060', '1:101288', '1:90040', '1:101274', '1:101345', '1:13986', '1:13977', '1:13989', '1:89772', '1:101046', '1:101047', '1:101050', '1:22201', '1:22312', '1:22584', '1:90068', '1:101304', '1:101307', '1:101308', '1:101295', '1:101347', '1:101350', '1:101381', '1:89904', '1:89934', '1:89945', '1:89955', '1:90003', '1:90006', '1:101661', '1:101370', '1:101373', '1:13190', '1:13919', '1:31348', '1:31357', '1:31786', '1:90690', '1:90674', '1:90711', '1:90892', '1:90921', '1:90949', '1:101998', '1:25016', '1:25026', '1:25041', '1:25073', '1:25080', '1:25090', '1:25093', '1:25177', '1:25204', '1:25312', '1:89601', '1:89208', '1:89621', '1:89907', '1:89870', '1:89876', '1:89554', '1:89585', '1:89597', '1:89928', '1:90503', '1:101870', '1:90540', '1:90549', '1:25512', '1:29106', '1:29200', '1:29205', '1:29221', '1:29259', '1:29300', '1:25761', '1:25799', '1:29004', '1:29137', '1:90042', '1:90055', '1:90057', '1:90200', '1:90201', '1:101130', '1:101188', '1:101302', '1:101326', '1:101411', '1:101428', '1:90443', '1:90496', '1:90497', '1:90516', '1:90110', '1:29603', '1:29219', '1:29227', '1:29344', '1:29384', '1:29323', '1:29948', '1:30022', '1:30026', '1:30027', '1:30102', '1:30106', '1:30107', '1:30120', '1:30122', '1:30123', '1:30127', '1:30173', '1:31751', '1:31546', '1:31613', '1:31632', '1:31667', '1:31752', '1:31676', '1:31678', '1:31691', '1:31706', '1:31707', '1:11450', '1:11979', '1:13008', '1:13631', '1:13942', '1:29038', '1:11462', '1:11465', '1:11474', '1:13014', '1:13036', '1:13933', '1:22241', '1:22259', '1:22690', '1:22971', '1:22975', '1:25124', '1:90369', '1:101135', '1:101434', '1:101573', '1:101901', '1:31965', '1:89041', '1:89113', '1:89234', '1:89245', '1:89473', '1:30534', '1:30549', '1:89365', '1:89369', '1:89675', '1:89802', '1:89807', '1:101124', '1:101198', '1:89151', '1:89692', '1:89328', '1:89714', '1:89761', '1:89262', '1:89282', '1:89285', '1:89659', '1:89669', '1:89713', '1:89001', '1:89319', '1:101196', '1:101217', '1:89350', '1:89994', '1:90416', '1:101145', '1:101208', '1:90417', '1:90981', '1:101139', '1:101691', '1:11209', '1:11288', '1:11400', '1:11520', '1:11645', '1:11517', '1:11993', '1:13025', '1:22245', '1:25282', '1:25587', '1:25592', '1:25944', '1:29334', '1:30537', '1:30930', '1:31135', '1:31827', '1:30951', '1:31470', '1:90411', '1:90421', '1:90373', '1:101576', '1:101473', '1:101499', '1:22180', '1:22236', '1:22240', '1:22588', '1:25166', '1:25271', '1:25273', '1:25694', '1:25818', '1:25828', '1:25278', '1:31810', '1:31819', '1:31867', '1:31869', '1:101563', '1:101568', '1:101569', '1:101687', '1:90413', '1:90977', '1:101561', '1:101564', '1:31854', '1:89673', '1:89726', '1:90324', '1:101543', '1:101554', '1:11507', '1:11572', '1:11580', '1:11609', '1:11460', '1:11678', '1:11714', '1:11813', '1:11833', '1:11732', '1:11770', '1:11705', '1:11724', '1:11771', '1:11855', '1:11857', '1:11904', '1:11783', '1:22287', '1:22590', '1:22594', '1:22683', '1:22688', '1:22693', '1:22394', '1:22421', '1:22441', '1:22513', '1:11216', '1:11285', '1:11321', '1:11573', '1:11101', '1:11203', '1:11217', '1:11236', '1:11243', '1:11246', '1:11454', '1:11455', '1:13315', '1:13091', '1:13095', '1:13227', '1:13071', '1:13528', '1:13075', '1:13353', '1:13312', '1:13350', '1:13357', '1:13489', '1:13616', '1:13627', '1:13698', '1:13918', '1:13828', '1:29133', '1:29134', '1:29135', '1:30327', '1:30760', '1:31269', '1:31286', '1:31290', '1:31319', '1:31366', '1:31367', '1:31408', '1:90005', '1:101066', '1:101095', '1:101136', '1:101173', '1:101190', '1:101252', '1:90744', '1:90798', '1:90799', '1:90891', '1:90882', '1:90886', '1:90898', '1:90906', '1:90919', '1:22128', '1:22129', '1:22007', '1:22097', '1:22159', '1:22292', '1:22415', '1:22417', '1:22432', '1:25557', '1:25540', '1:25636', '1:25642', '1:25654', '1:25659', '1:25667', '1:25780', '1:29062', '1:25981', '1:29100', '1:29101', '1:29111', '1:29454', '1:29465', '1:29510', '1:29616', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/BA08AC92-32EF-E911-82D8-441EA1616DEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/1A47AC00-7B03-EA11-9EE6-0CC47AF973C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DA862DF2-9F11-EA11-A5FB-C4346BC75558.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DC992538-9910-EA11-BF7F-0CC47A5FC281.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/163497F8-2D11-EA11-A132-6C2B599A050D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/0A3BC253-8411-EA11-A6F0-D8D385AF891A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/562C1852-3411-EA11-A53F-8CDCD4A9A484.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/E6105D38-A311-EA11-9524-0CC47A7E6A5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D86A4CB2-9014-EA11-8CA9-F01FAFE5CF52.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C0549F53-A714-EA11-8560-782BCB46E733.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/70D29667-41FB-E911-818C-38EAA78D8ACC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/B8C911EE-29F0-E911-8638-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/0E7BC3B3-0AFA-E911-8213-98039B3B01B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DE54B8C9-DA10-EA11-89A8-A4BF01125538.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/2ABD4E37-8F03-EA11-815A-1866DA86CCDF.root']);