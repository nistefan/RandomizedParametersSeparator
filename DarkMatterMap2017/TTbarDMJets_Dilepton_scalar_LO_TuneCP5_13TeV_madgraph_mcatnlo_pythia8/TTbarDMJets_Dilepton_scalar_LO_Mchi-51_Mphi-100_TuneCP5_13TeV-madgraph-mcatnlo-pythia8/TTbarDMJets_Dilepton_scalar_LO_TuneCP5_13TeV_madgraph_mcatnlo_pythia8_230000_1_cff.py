import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:59091', '1:56285', '1:56334', '1:56350', '1:56428', '1:56462', '1:56467', '1:56476', '1:56490', '1:83130', '1:83444', '1:83486', '1:83546', '1:82463', '1:85551', '1:85622', '1:85702', '1:85713', '1:86574', '1:71026', '1:71273', '1:71405', '1:64506', '1:65093', '1:70100', '1:70217', '1:66608', '1:71126', '1:71128', '1:71163', '1:71271', '1:71274', '1:71275', '1:71425', '1:83810', '1:83842', '1:65783', '1:65787', '1:65832', '1:65939', '1:66054', '1:70658', '1:86776', '1:86800', '1:83721', '1:79939', '1:79943', '1:84036', '1:84052', '1:84118', '1:83536', '1:4344', '1:5602', '1:5865', '1:7127', '1:3730', '1:3944', '1:5069', '1:5081', '1:9247', '1:24807', '1:24882', '1:26075', '1:26147', '1:26228', '1:26236', '1:26257', '1:26262', '1:38593', '1:38613', '1:38627', '1:43077', '1:14064', '1:14135', '1:14140', '1:14240', '1:14465', '1:36401', '1:36471', '1:36560', '1:36667', '1:36788', '1:41712', '1:34791', '1:38118', '1:38207', '1:38249', '1:38389', '1:38176', '1:43281', '1:43283', '1:43286', '1:43383', '1:43403', '1:42343', '1:42737', '1:42777', '1:42832', '1:42840', '1:46021', '1:5736', '1:5750', '1:5761', '1:19665', '1:21029', '1:21095', '1:21187', '1:26829', '1:27382', '1:26952', '1:26978', '1:17022', '1:17775', '1:17858', '1:17867', '1:18023', '1:18065', '1:26712', '1:26725', '1:26987', '1:28073', '1:28075', '1:28116', '1:28140', '1:28246', '1:28709', '1:37666', '1:37650', '1:15628', '1:21545', '1:27043', '1:27250', '1:27804', '1:26182', '1:26498', '1:34747', '1:27530', '1:27584', '1:27917', '1:40621', '1:40765', '1:50078', '1:50733', '1:41013', '1:41127', '1:51371', '1:51727', '1:60428', '1:60934', '1:59882', '1:60383', '1:83680', '1:83627', '1:83694', '1:83744', '1:87402', '1:87408', '1:87447', '1:87364', '1:87412', '1:87413', '1:87440', '1:97507', '1:97485', '1:97487', '1:97560', '1:97930', '1:99066', '1:2944', '1:5423', '1:5440', '1:5828', '1:5894', '1:60409', '1:70547', '1:70614', '1:71831', '1:71841', '1:73780', '1:74949', '1:76094', '1:91407', '1:94880', '1:12535', '1:12754', '1:12858', '1:14096', '1:19835', '1:18308', '1:18588', '1:19038', '1:19049', '1:19262', '1:19376', '1:20089', '1:20487', '1:63601', '1:63806', '1:83057', '1:104783', '1:104893', '1:105800', '1:106099', '1:87404', '1:19032', '1:19070', '1:16443', '1:32070', '1:32371', '1:32753', '1:48459', '1:50368', '1:51157', '1:54300', '1:40554', '1:48753', '1:57877', '1:51161', '1:35231', '1:35634', '1:36461', '1:36470', '1:36396', '1:36769', '1:38556', '1:42505', '1:38907', '1:38988', '1:43135', '1:46661', '1:46884', '1:69651', '1:66098', '1:64427', '1:67253', '1:64199', '1:73436', '1:74113', '1:74344', '1:51042', '1:58678', '1:67475', '1:68574', '1:68941', '1:67795', '1:104042', '1:34763', '1:42388', '1:35961', '1:47231', '1:41848', '1:44053', '1:44077', '1:44514', '1:44161', '1:44291', '1:87259', '1:88724', '1:91565', '1:92046', '1:93468', '1:47348', '1:47285', '1:47381', '1:47529', '1:47579', '1:47581', '1:47610', '1:47633', '1:69660', '1:58174', '1:58282', '1:58553', '1:58558', '1:58623', '1:59193', '1:98332', '1:93440', '1:93482', '1:94265', '1:94746', '1:94759', '1:64111', '1:69634', '1:69347', '1:69707', '1:69809', '1:69830', '1:72218', '1:74312', '1:74327', '1:74315', '1:65112', '1:65119', '1:65344', '1:65370', '1:65403', '1:65419', '1:65497', '1:65367', '1:65409', '1:78869', '1:67823', '1:67985', '1:68125', '1:68205', '1:68278', '1:68650', '1:79987', '1:92690', '1:95124', '1:95170', '1:57517', '1:57809', '1:60622', '1:60997', '1:61294', '1:61371', '1:61399', '1:64010', '1:65026', '1:100608', '1:62762', '1:62883', '1:78356', '1:79007', '1:79052', '1:80262', '1:80333', '1:80599', '1:80624', '1:80761', '1:80783', '1:93806', '1:93812', '1:54810', '1:55139', '1:55228', '1:55852', '1:61665', '1:63496', '1:63859', '1:59516', '1:59993', '1:60052', '1:59840', '1:59860', '1:71103', '1:65182', '1:71869', '1:72070', '1:72176', '1:70726', '1:76664', '1:76739', '1:76797', '1:77062', '1:80421', '1:80437', '1:84412', '1:84544', '1:84554', '1:84662', '1:84762', '1:84808', '1:84575', '1:84796', '1:60866', '1:60885', '1:65968', '1:68264', '1:68690', '1:98392', '1:98832', '1:71607', '1:71610', '1:71622', '1:71889', '1:71947', '1:73006', '1:79374', '1:77496', '1:76195', '1:76210', '1:88578', '1:95012', '1:95037', '1:94866', '1:100283', '1:71637', '1:71937', '1:92907', '1:93119', '1:92853', '1:92968', '1:92969', '1:93138', '1:93221', '1:93328', '1:100045', '1:100514', '1:100563', '1:100600', '1:100620', '1:99907', '1:99918', '1:85282', '1:85300', '1:85316', '1:98659', '1:98761', '1:98889', '1:98909', '1:98959', '1:98986', '1:99036', '1:99277', '1:106265', '1:92093', '1:92098', '1:92158', '1:92570', '1:92531', '1:92643', '1:93183', '1:93989', '1:93463', '1:17397', '1:15432', '1:17098', '1:19202', '1:19531', '1:36111', '1:43765', '1:45005', '1:45022', '1:45517', '1:49778', '1:49835', '1:50047', '1:52550', '1:52689', '1:63814', '1:63882', '1:64151', '1:92915', '1:93103', '1:93297', '1:75556', '1:75590', '1:81566', '1:81607', '1:81613', '1:81632', '1:81650', '1:81717', '1:96576', '1:96659', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7E950A55-7FEF-E911-99DC-441EA1616D3A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A8DBB44-A8EE-E911-B7A4-38EAA78D8ADC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8AEFCC7-7EEE-E911-AEFD-0CC47AF97150.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80B375BC-64EF-E911-B7EE-509A4C8395C6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0610918D-54EF-E911-A116-1458D04903A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7A8B894E-5BEF-E911-8B06-3CFDFE7082F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A4B986E-79EF-E911-820B-0025904AC2C4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/065D3837-F2EF-E911-9DD3-44A842B4CC7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/98C92559-C3F2-E911-A525-A4BF0128811C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78F424B9-AEF2-E911-8B73-00E081B705EA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2074DF05-35F2-E911-9B9B-3417EBE706C3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A81CFE31-E1F2-E911-8D5C-A4BF01283D2E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE40E859-04F3-E911-BD9D-A4BF012881D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E609EEE8-57F0-E911-8275-002590DBE20C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE1D09DE-96F2-E911-A3BF-3417EBE74303.root']);