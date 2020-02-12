import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:72145', '1:72674', '1:72625', '1:74182', '1:75581', '1:75642', '1:75694', '1:75735', '1:75791', '1:72452', '1:97605', '1:97613', '1:97677', '1:97771', '1:97832', '1:97867', '1:97595', '1:97837', '1:97892', '1:103692', '1:104224', '1:42073', '1:39195', '1:39221', '1:39261', '1:39267', '1:39268', '1:39306', '1:39310', '1:51800', '1:52217', '1:50319', '1:50475', '1:50547', '1:50587', '1:50628', '1:50739', '1:50821', '1:86736', '1:86768', '1:86773', '1:86818', '1:86822', '1:86830', '1:87101', '1:87571', '1:87597', '1:96402', '1:97294', '1:86929', '1:86950', '1:87010', '1:26238', '1:26055', '1:26082', '1:26109', '1:26304', '1:26319', '1:26329', '1:26333', '1:26291', '1:26394', '1:26399', '1:26424', '1:26651', '1:26690', '1:26719', '1:72148', '1:73726', '1:84822', '1:84847', '1:84910', '1:84924', '1:84939', '1:84942', '1:84944', '1:103357', '1:103879', '1:98905', '1:99711', '1:99968', '1:100027', '1:100059', '1:100380', '1:100547', '1:100549', '1:100559', '1:100648', '1:100679', '1:100684', '1:98675', '1:98685', '1:100690', '1:14245', '1:15144', '1:17367', '1:12809', '1:14305', '1:14310', '1:14377', '1:15620', '1:15759', '1:15764', '1:16395', '1:16976', '1:15451', '1:15938', '1:15972', '1:17017', '1:17461', '1:14707', '1:15626', '1:15687', '1:17173', '1:17981', '1:39116', '1:39497', '1:44922', '1:61460', '1:61933', '1:61970', '1:61974', '1:62142', '1:62438', '1:21986', '1:21452', '1:21464', '1:21747', '1:24695', '1:24079', '1:35405', '1:35443', '1:38141', '1:35951', '1:36464', '1:38005', '1:38133', '1:38601', '1:42033', '1:42133', '1:42817', '1:37386', '1:37515', '1:37806', '1:37815', '1:58372', '1:98372', '1:102638', '1:98373', '1:95690', '1:98124', '1:100750', '1:102773', '1:26949', '1:27756', '1:26941', '1:27495', '1:28036', '1:28960', '1:32511', '1:42473', '1:34027', '1:34311', '1:34624', '1:34761', '1:34766', '1:35495', '1:35826', '1:35935', '1:36567', '1:36712', '1:36793', '1:36838', '1:37248', '1:37899', '1:37945', '1:37976', '1:50163', '1:57462', '1:55141', '1:57202', '1:37370', '1:37450', '1:37480', '1:37494', '1:37583', '1:37656', '1:38539', '1:63640', '1:63895', '1:68716', '1:62506', '1:63413', '1:67236', '1:67719', '1:68659', '1:68791', '1:62865', '1:64161', '1:66478', '1:66793', '1:67959', '1:68795', '1:69304', '1:69369', '1:70742', '1:67351', '1:71000', '1:71219', '1:73692', '1:60377', '1:60876', '1:60138', '1:61053', '1:62206', '1:103164', '1:106216', '1:49268', '1:51213', '1:52344', '1:52732', '1:53311', '1:50917', '1:51692', '1:57385', '1:55061', '1:56060', '1:56599', '1:58902', '1:59768', '1:16241', '1:17470', '1:21739', '1:27751', '1:33779', '1:34286', '1:37727', '1:33516', '1:38235', '1:38654', '1:92292', '1:92701', '1:96896', '1:43623', '1:45050', '1:46390', '1:57459', '1:53470', '1:56000', '1:56784', '1:56849', '1:58323', '1:70817', '1:74529', '1:40055', '1:44643', '1:72186', '1:72249', '1:73572', '1:73779', '1:74691', '1:74771', '1:75492', '1:86354', '1:87731', '1:87855', '1:88009', '1:96658', '1:100488', '1:102433', '1:64048', '1:69679', '1:64236', '1:70322', '1:86213', '1:87210', '1:69469', '1:69511', '1:70018', '1:87968', '1:82809', '1:82828', '1:83226', '1:83346', '1:83371', '1:83442', '1:84235', '1:84344', '1:84385', '1:92913', '1:93167', '1:93257', '1:95794', '1:96375', '1:97711', '1:3766', '1:3768', '1:3794', '1:3914', '1:4055', '1:4005', '1:4028', '1:4034', '1:4037', '1:4046', '1:4086', '1:4208', '1:4218', '1:50863', '1:51367', '1:51509', '1:51521', '1:60999', '1:58978', '1:59621', '1:60118', '1:60973', '1:60081', '1:60488', '1:62997', '1:59751', '1:60271', '1:60314', '1:58175', '1:58196', '1:88542', '1:92738', '1:104850', '1:105591', '1:105931', '1:106210', '1:86873', '1:86908', '1:87081', '1:87108', '1:87130', '1:87146', '1:87163', '1:87708', '1:87709', '1:87729', '1:87740', '1:87745', '1:87814', '1:100858', '1:100897', '1:100930', '1:100922', '1:102036', '1:102086', '1:66', '1:91', '1:160', '1:183', '1:240', '1:284', '1:59', '1:196', '1:333', '1:583', '1:973', '1:618', '1:750', '1:760', '1:776', '1:786', '1:815', '1:817', '1:831', '1:833', '1:886', '1:896', '1:922', '1:4121', '1:2570', '1:2631', '1:2649', '1:2670', '1:1901', '1:1910', '1:1602', '1:1611', '1:1642', '1:1742', '1:1766', '1:1806', '1:1887', '1:1950', '1:1951', '1:1964', '1:1972', '1:4402', '1:18878', '1:18880', '1:18882', '1:18913', '1:18926', '1:39184', '1:44626', '1:46754', '1:49677', '1:50360', '1:14423', '1:14432', '1:14463', '1:14541', '1:14566', '1:14598', '1:14658', '1:14659', '1:14681', '1:14731', '1:14744', '1:14755', '1:16427', '1:53806', '1:53809', '1:55214', '1:56149', '1:56162', '1:56638', '1:56720', '1:58016', '1:58134', '1:91731', '1:92215', '1:92228', '1:103958', '1:103989', '1:2283', '1:2351', '1:2637', '1:2956', '1:3439', '1:3472', '1:3578', '1:3706', '1:2706', '1:2830', '1:2971', '1:3137', '1:3144', '1:5681', '1:5698', '1:5795', '1:5823', '1:5910', '1:5947', '1:5964', '1:5982', '1:5798', '1:5815', '1:5843', '1:5889', '1:5922', '1:5926', '1:5949', '1:5969', '1:17576', '1:17560', '1:17590', '1:17596', '1:17369', '1:18255', '1:18282', '1:17809', '1:17863', '1:17868', '1:53063', '1:62309', '1:63287', '1:68250', '1:67868', '1:65292', '1:66341', '1:68416', '1:73111', '1:63307', '1:63369', '1:63698', '1:63804', '1:63258', '1:63281', '1:63282', '1:63315', '1:63379', '1:63414', '1:67112', '1:67222', '1:68115', '1:68188', '1:88401', '1:95057', '1:91817', '1:91826', '1:91889', '1:91912', '1:91990', '1:94218', '1:94231', '1:94235', '1:94261', '1:94274', '1:94287', '1:96282', '1:96362', '1:95792', '1:95820', '1:95884', '1:64978', '1:65018', '1:65463', '1:64274', '1:64363', '1:64378', '1:64400', '1:64455', '1:64494', '1:63530', '1:63491', '1:67099', '1:67140', '1:78298', '1:78474', '1:78548', '1:78588', '1:78706', '1:78786', '1:78888', '1:78655', '1:78759', '1:78766', '1:81439', '1:81455', '1:81467', '1:88577', '1:88617', '1:88711', '1:88731', '1:88759', '1:81700', '1:81756', '1:95306', '1:95428', '1:95524', '1:95644', '1:95688', '1:95726', '1:99841', '1:98498', '1:99005', '1:99202', '1:98320', '1:98357', '1:98806', '1:7619', '1:7665', '1:7667', '1:7904', '1:8113', '1:8838', '1:16928', '1:15636', '1:17027', '1:17274', '1:18141', '1:20767', '1:86016', '1:26722', '1:24072', '1:24334', '1:24585', '1:24732', '1:24542', '1:21964', '1:24439', '1:24461', '1:24509', '1:24531', '1:33622', '1:24281', '1:24551', '1:27255', '1:27960', '1:27048', '1:28239', '1:45578', '1:38362', '1:46068', '1:47523', '1:40642', '1:41913', '1:45180', '1:47010', '1:47574', '1:48328', '1:45254', '1:87215', '1:82081', '1:82736', '1:85759', '1:80360', '1:86406', '1:88441', '1:88958', '1:88988', '1:82325', '1:415', '1:420', '1:3933', '1:9221', '1:16607', '1:7372', '1:12033', '1:18489', '1:9967', '1:9969', '1:12281', '1:15830', '1:17134', '1:18084', '1:18140', '1:18561', '1:20525', '1:20465', '1:20502', '1:24772', '1:27009', '1:27351', '1:24755', '1:26669', '1:26886', '1:27483', '1:429', '1:596', '1:823', '1:1128', '1:1463', '1:1498', '1:1512', '1:1540', '1:7122', '1:7234', '1:7265', '1:7292', '1:7343', '1:7373', '1:7392', '1:7439', '1:7477', '1:7480', '1:7485', '1:7497', '1:7543', '1:7563', '1:7797', '1:7805', '1:8466', '1:8468', '1:8135', '1:8150', '1:8369', '1:61268', '1:63170', '1:67682', '1:46591', '1:42580', '1:43379', '1:45427', '1:99439', '1:99522', '1:99568', '1:99677', '1:99698', '1:99745', '1:54056', '1:54096', '1:54114', '1:54204', '1:54333', '1:54380', '1:54516', '1:54548', '1:54593', '1:54690', '1:79416', '1:79437', '1:79405', '1:805', '1:98', '1:854', '1:1719', '1:1044', '1:1076', '1:17315', '1:17327', '1:18015', '1:18070', '1:18399', '1:17200', '1:18888', '1:20573', '1:20607', '1:20684', '1:19212', '1:20880', '1:27273', '1:17187', '1:19548', '1:20791', '1:18027', '1:21145', '1:27398', '1:27567', '1:2258', '1:2517', '1:2254', '1:2289', '1:2308', '1:2405', '1:2525', '1:2920', '1:4825', '1:4993', '1:2135', '1:2295', '1:2858', '1:2862', '1:2968', '1:3413', '1:3510', '1:3938', '1:3978', '1:4000', '1:4160', '1:4493', '1:4972', '1:3131', '1:4985', '1:26141', '1:26303', '1:27403', '1:28279', '1:26803', '1:28316', '1:3052', '1:5110', '1:5407', '1:28500', '1:34175', '1:33896', '1:35276', '1:37732', '1:37814', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E28438A7-4910-EA11-910C-40F2E9C6AE26.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA25B1CE-CEF6-E911-B53C-246E96D14B5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/64F51C16-E1F6-E911-B326-B499BAAC03BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC7BC4C4-EBEF-E911-9B75-002590D9D8B8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2443D33F-8B0E-EA11-B3DB-6CC2173D44D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38867EE3-18EF-E911-ADE7-B8CA3A70A520.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DA35E849-52F8-E911-8ABB-002590D4FC5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A43B4BF7-9B0F-EA11-864B-509A4C84D1B1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5C477F16-6DFF-E911-BE38-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0EF3BEDD-37EE-E911-9652-089E0158CD57.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CECB7F44-C3F2-E911-8EFE-AC162DA6E2F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60FDD590-16F8-E911-89B9-003048F5B69E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CA9067BE-EBED-E911-A5CA-98039B3B0182.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/ACFC8763-7B04-EA11-A589-6CC2173C39E0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DA8DAF0B-9FED-E911-A23B-E0071B6CAD20.root']);