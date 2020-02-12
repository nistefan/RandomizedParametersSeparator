import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:19667', '1:19804', '1:19578', '1:19619', '1:19679', '1:19713', '1:19715', '1:19744', '1:19844', '1:27676', '1:27681', '1:34420', '1:34484', '1:34491', '1:34663', '1:34687', '1:34745', '1:34843', '1:34847', '1:34852', '1:34868', '1:36492', '1:36536', '1:36537', '1:38049', '1:38957', '1:40534', '1:33109', '1:27021', '1:32643', '1:33195', '1:33277', '1:33657', '1:33783', '1:28480', '1:28484', '1:28505', '1:28535', '1:28628', '1:28713', '1:28714', '1:28726', '1:28729', '1:28776', '1:28781', '1:28815', '1:28822', '1:28846', '1:28849', '1:28853', '1:28857', '1:28873', '1:28889', '1:33576', '1:33621', '1:33877', '1:33928', '1:33602', '1:33696', '1:33717', '1:34834', '1:34835', '1:2682', '1:32618', '1:32658', '1:38003', '1:45862', '1:46166', '1:46768', '1:95071', '1:95387', '1:95363', '1:97393', '1:99857', '1:99861', '1:16240', '1:16480', '1:16490', '1:16616', '1:16618', '1:16710', '1:83237', '1:85795', '1:88390', '1:88837', '1:91007', '1:91022', '1:91036', '1:91047', '1:91170', '1:91176', '1:91218', '1:91275', '1:91291', '1:91299', '1:91382', '1:88241', '1:88295', '1:88332', '1:88349', '1:40225', '1:45764', '1:40842', '1:44431', '1:50408', '1:50410', '1:50415', '1:50421', '1:50484', '1:51083', '1:58212', '1:58597', '1:58889', '1:58345', '1:58349', '1:58308', '1:88168', '1:88269', '1:1231', '1:1375', '1:1400', '1:1471', '1:1476', '1:1338', '1:1370', '1:1372', '1:1411', '1:1470', '1:3246', '1:3378', '1:3793', '1:4001', '1:3363', '1:3401', '1:3474', '1:28934', '1:28940', '1:28972', '1:28980', '1:28925', '1:36707', '1:38174', '1:38177', '1:38878', '1:38898', '1:40904', '1:40934', '1:43365', '1:43570', '1:43925', '1:43980', '1:44132', '1:19058', '1:19434', '1:19813', '1:19968', '1:20799', '1:20969', '1:21112', '1:21722', '1:17209', '1:19005', '1:19148', '1:27913', '1:70283', '1:70512', '1:70522', '1:70632', '1:73854', '1:74962', '1:77450', '1:72281', '1:72449', '1:72404', '1:72896', '1:75360', '1:75502', '1:77444', '1:73667', '1:66790', '1:70448', '1:71041', '1:73005', '1:68695', '1:64597', '1:64952', '1:65143', '1:65615', '1:64029', '1:64070', '1:64086', '1:64118', '1:64820', '1:65438', '1:69308', '1:69772', '1:98486', '1:98944', '1:102027', '1:96045', '1:96844', '1:99092', '1:100496', '1:72109', '1:72173', '1:72662', '1:74601', '1:74633', '1:73612', '1:73655', '1:97023', '1:99291', '1:102909', '1:103260', '1:96511', '1:14524', '1:19645', '1:20396', '1:18536', '1:19132', '1:21753', '1:24445', '1:24729', '1:28290', '1:28353', '1:28692', '1:32202', '1:27104', '1:27685', '1:27970', '1:28106', '1:74918', '1:72312', '1:73222', '1:73986', '1:74567', '1:75499', '1:74695', '1:81918', '1:82297', '1:82157', '1:82449', '1:82498', '1:82562', '1:82587', '1:91557', '1:91575', '1:93457', '1:91696', '1:95401', '1:96607', '1:97196', '1:97502', '1:100005', '1:92326', '1:95244', '1:96310', '1:96653', '1:96669', '1:93704', '1:93883', '1:93605', '1:93661', '1:93666', '1:93680', '1:41429', '1:41464', '1:41471', '1:48489', '1:54137', '1:54154', '1:54188', '1:54194', '1:54221', '1:57192', '1:55550', '1:55803', '1:56102', '1:81791', '1:81351', '1:81359', '1:91532', '1:94094', '1:92659', '1:92791', '1:100605', '1:100711', '1:100803', '1:102100', '1:102196', '1:102219', '1:102341', '1:102671', '1:96127', '1:104830', '1:99687', '1:100144', '1:99590', '1:100147', '1:100152', '1:100160', '1:100165', '1:106338', '1:73433', '1:74611', '1:68479', '1:70393', '1:70567', '1:71044', '1:95320', '1:95358', '1:95362', '1:95400', '1:95545', '1:95562', '1:97796', '1:99631', '1:99769', '1:104235', '1:104243', '1:104301', '1:104310', '1:106036', '1:106048', '1:106068', '1:105874', '1:105879', '1:105887', '1:105898', '1:105916', '1:105926', '1:105937', '1:105948', '1:50024', '1:50238', '1:50276', '1:50338', '1:50237', '1:50259', '1:50542', '1:50702', '1:50852', '1:60630', '1:60796', '1:61805', '1:62559', '1:63311', '1:64116', '1:64218', '1:62377', '1:64088', '1:64113', '1:64136', '1:64905', '1:65417', '1:96086', '1:96224', '1:96071', '1:96139', '1:96152', '1:96156', '1:96443', '1:96397', '1:96526', '1:62320', '1:62604', '1:62689', '1:62872', '1:63058', '1:62645', '1:62750', '1:63121', '1:63185', '1:72937', '1:72954', '1:81710', '1:82032', '1:82036', '1:82042', '1:82098', '1:82128', '1:82129', '1:96303', '1:97302', '1:99915', '1:100082', '1:67531', '1:67753', '1:67870', '1:67934', '1:67552', '1:84486', '1:84495', '1:84532', '1:83838', '1:83943', '1:84525', '1:84969', '1:85019', '1:85053', '1:85122', '1:85126', '1:85182', '1:94587', '1:94530', '1:94571', '1:94684', '1:94704', '1:99534', '1:99580', '1:99911', '1:99981', '1:21995', '1:24728', '1:52256', '1:52342', '1:52350', '1:52391', '1:52472', '1:52913', '1:53130', '1:53164', '1:55923', '1:56397', '1:57063', '1:57273', '1:57295', '1:80010', '1:80032', '1:102914', '1:102925', '1:39283', '1:39293', '1:39337', '1:39371', '1:39474', '1:39552', '1:39747', '1:39750', '1:39881', '1:39882', '1:39891', '1:40793', '1:40837', '1:40838', '1:40854', '1:40861', '1:62707', '1:62715', '1:63045', '1:76504', '1:76846', '1:76879', '1:76969', '1:77059', '1:77221', '1:76754', '1:100478', '1:100573', '1:100583', '1:100596', '1:78789', '1:78815', '1:78825', '1:80075', '1:80110', '1:80142', '1:36220', '1:38506', '1:38638', '1:38338', '1:42125', '1:42328', '1:41818', '1:50079', '1:50364', '1:50956', '1:50965', '1:92451', '1:92877', '1:96025', '1:96904', '1:97391', '1:99554', '1:100537', '1:92553', '1:96207', '1:97139', '1:98152', '1:98468', '1:99263', '1:88420', '1:88663', '1:88689', '1:88718', '1:88745', '1:88788', '1:88807', '1:88879', '1:104430', '1:104446', '1:12670', '1:19917', '1:19925', '1:19946', '1:20195', '1:20788', '1:20807', '1:61854', '1:61997', '1:62050', '1:62167', '1:62324', '1:62396', '1:62287', '1:62300', '1:65058', '1:65082', '1:64561', '1:63998', '1:67027', '1:67157', '1:65924', '1:65056', '1:81168', '1:81416', '1:81580', '1:81418', '1:87574', '1:65254', '1:65573', '1:65384', '1:65473', '1:65648', '1:65673', '1:65751', '1:68523', '1:68522', '1:70435', '1:70764', '1:70772', '1:70866', '1:71267', '1:71269', '1:71277', '1:91445', '1:91475', '1:94010', '1:94025', '1:94036', '1:94048', '1:93288', '1:17009', '1:17477', '1:20402', '1:24982', '1:19429', '1:20510', '1:20556', '1:21243', '1:21650', '1:19905', '1:26905', '1:68441', '1:51046', '1:50639', '1:51964', '1:51473', '1:52580', '1:69328', '1:69411', '1:69695', '1:65100', '1:66759', '1:80938', '1:80415', '1:80454', '1:84417', '1:85837', '1:78043', '1:78181', '1:79798', '1:84179', '1:84846', '1:84853', '1:92176', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/147D2FEE-7AF4-E911-AC32-FA163ED45046.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8D1CA51-35F3-E911-A13A-7CD30AD09C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/408D623C-B5F2-E911-BEF8-FA163EEBFC01.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B49C1D82-4EF3-E911-9E50-842B2B6AEA0E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4E56313-21F4-E911-B492-1866DA7F9419.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94284CBD-36F4-E911-88E6-A4BF012835C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AB8635C-CDF5-E911-B092-FA163EF38280.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/42C14BE8-BDF6-E911-95B1-AC1F6B56768A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7602BEA4-33F6-E911-95A7-FA163EB69FE7.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B87F77FB-EAF6-E911-A351-0090FAA57A00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E27EC42F-BBF9-E911-9830-B083FED429D5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38B76DAF-36F9-E911-9F0F-001F29089F68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B02AB0B8-ADFA-E911-BDE6-44A842CFD667.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92B1133B-96FA-E911-99FE-FA163E3BEC96.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C990481-CCF8-E911-B595-008CFAE45404.root']);