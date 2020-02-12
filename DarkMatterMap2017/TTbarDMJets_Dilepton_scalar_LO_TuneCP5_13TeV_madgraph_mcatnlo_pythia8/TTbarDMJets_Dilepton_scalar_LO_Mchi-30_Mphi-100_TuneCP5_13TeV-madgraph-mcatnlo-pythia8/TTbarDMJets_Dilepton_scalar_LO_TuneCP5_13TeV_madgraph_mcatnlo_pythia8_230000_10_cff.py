import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:72447', '1:73974', '1:75194', '1:75748', '1:97464', '1:97589', '1:97715', '1:97840', '1:97933', '1:97599', '1:97696', '1:97725', '1:106013', '1:103651', '1:42077', '1:42338', '1:42365', '1:42464', '1:39159', '1:39186', '1:39425', '1:50664', '1:86866', '1:86889', '1:26068', '1:26074', '1:26142', '1:26167', '1:26199', '1:26419', '1:26421', '1:26541', '1:26644', '1:84597', '1:84605', '1:84706', '1:84901', '1:84973', '1:98714', '1:100299', '1:100692', '1:100745', '1:15957', '1:16469', '1:15260', '1:16275', '1:14383', '1:12604', '1:15339', '1:15758', '1:15912', '1:15074', '1:15578', '1:15599', '1:17464', '1:15824', '1:17188', '1:39671', '1:40407', '1:45887', '1:47996', '1:61629', '1:21743', '1:21383', '1:21536', '1:21587', '1:26984', '1:88918', '1:94222', '1:42503', '1:37384', '1:100025', '1:103193', '1:102539', '1:103460', '1:99710', '1:100768', '1:26937', '1:26973', '1:38894', '1:34479', '1:34809', '1:35708', '1:35958', '1:36696', '1:37319', '1:37142', '1:37183', '1:37509', '1:38557', '1:38833', '1:67411', '1:68162', '1:69543', '1:71724', '1:70214', '1:62337', '1:60878', '1:69358', '1:82038', '1:86398', '1:102626', '1:24921', '1:51574', '1:51814', '1:53468', '1:53849', '1:51197', '1:57222', '1:16112', '1:17141', '1:24746', '1:27500', '1:37493', '1:35838', '1:37950', '1:49033', '1:84587', '1:79556', '1:40126', '1:45292', '1:47154', '1:47569', '1:55151', '1:56294', '1:87353', '1:65270', '1:71261', '1:73395', '1:83637', '1:87770', '1:83415', '1:82770', '1:95474', '1:96044', '1:96661', '1:100208', '1:4029', '1:4087', '1:4207', '1:4217', '1:68604', '1:50790', '1:51109', '1:51430', '1:63712', '1:56885', '1:59709', '1:62436', '1:68051', '1:94682', '1:86987', '1:87035', '1:87058', '1:87073', '1:87131', '1:87874', '1:100890', '1:100892', '1:100950', '1:100990', '1:102032', '1:102054', '1:100923', '1:102069', '1:99', '1:140', '1:288', '1:276', '1:684', '1:705', '1:620', '1:719', '1:741', '1:795', '1:849', '1:880', '1:2139', '1:2707', '1:1595', '1:1612', '1:1660', '1:1683', '1:1749', '1:1783', '1:1979', '1:1927', '1:1928', '1:18930', '1:18968', '1:18984', '1:18993', '1:20039', '1:50848', '1:51353', '1:14433', '1:15003', '1:14853', '1:14875', '1:54586', '1:54976', '1:56655', '1:58040', '1:91712', '1:91753', '1:103981', '1:2425', '1:2991', '1:2623', '1:2766', '1:3104', '1:5746', '1:5846', '1:17478', '1:18236', '1:17666', '1:17674', '1:17683', '1:17271', '1:44542', '1:44907', '1:44936', '1:45450', '1:45467', '1:53028', '1:55651', '1:55667', '1:57282', '1:68557', '1:68884', '1:63429', '1:63430', '1:63448', '1:92109', '1:93425', '1:94578', '1:91560', '1:91984', '1:94227', '1:94273', '1:96496', '1:95904', '1:64871', '1:64238', '1:64300', '1:64314', '1:64337', '1:64391', '1:67143', '1:78494', '1:78533', '1:78547', '1:78565', '1:78606', '1:78745', '1:78752', '1:78831', '1:88427', '1:88428', '1:88437', '1:88604', '1:88758', '1:81784', '1:81748', '1:81812', '1:81894', '1:81899', '1:81913', '1:97975', '1:97999', '1:98984', '1:99162', '1:99507', '1:98365', '1:99223', '1:99224', '1:8080', '1:8253', '1:8335', '1:9873', '1:12650', '1:12652', '1:12668', '1:14151', '1:15800', '1:16984', '1:17005', '1:17498', '1:17955', '1:20133', '1:87563', '1:26735', '1:24131', '1:24612', '1:24396', '1:24500', '1:24180', '1:24546', '1:24699', '1:24818', '1:27063', '1:39658', '1:44150', '1:45658', '1:45736', '1:47191', '1:47469', '1:48145', '1:86328', '1:86729', '1:86860', '1:85594', '1:338', '1:611', '1:1768', '1:1846', '1:16224', '1:16309', '1:18391', '1:21835', '1:27315', '1:32611', '1:34566', '1:370', '1:474', '1:555', '1:1058', '1:1119', '1:1213', '1:7245', '1:7500', '1:7509', '1:7554', '1:8199', '1:7896', '1:7929', '1:8314', '1:62003', '1:67300', '1:21872', '1:32635', '1:45396', '1:45438', '1:46588', '1:37468', '1:37951', '1:99502', '1:99532', '1:99564', '1:99717', '1:99723', '1:99725', '1:53964', '1:54236', '1:54315', '1:54349', '1:54542', '1:54622', '1:54631', '1:54696', '1:99337', '1:79433', '1:79448', '1:79395', '1:79426', '1:79446', '1:879', '1:41', '1:90', '1:1334', '1:17973', '1:18186', '1:17443', '1:20515', '1:19564', '1:19591', '1:24348', '1:24634', '1:27054', '1:732', '1:2153', '1:2371', '1:2430', '1:2551', '1:2927', '1:2093', '1:4964', '1:3008', '1:3783', '1:3502', '1:9268', '1:26769', '1:28733', '1:32437', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E28438A7-4910-EA11-910C-40F2E9C6AE26.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA25B1CE-CEF6-E911-B53C-246E96D14B5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/64F51C16-E1F6-E911-B326-B499BAAC03BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC7BC4C4-EBEF-E911-9B75-002590D9D8B8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2443D33F-8B0E-EA11-B3DB-6CC2173D44D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38867EE3-18EF-E911-ADE7-B8CA3A70A520.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DA35E849-52F8-E911-8ABB-002590D4FC5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A43B4BF7-9B0F-EA11-864B-509A4C84D1B1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5C477F16-6DFF-E911-BE38-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0EF3BEDD-37EE-E911-9652-089E0158CD57.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CECB7F44-C3F2-E911-8EFE-AC162DA6E2F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60FDD590-16F8-E911-89B9-003048F5B69E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CA9067BE-EBED-E911-A5CA-98039B3B0182.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/ACFC8763-7B04-EA11-A589-6CC2173C39E0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DA8DAF0B-9FED-E911-A23B-E0071B6CAD20.root']);