import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:303', '1:430', '1:479', '1:487', '1:19301', '1:19635', '1:18798', '1:18915', '1:19096', '1:19187', '1:99957', '1:104052', '1:103435', '1:102651', '1:103757', '1:103790', '1:46772', '1:46873', '1:46896', '1:46996', '1:46932', '1:47304', '1:47346', '1:48310', '1:48706', '1:48790', '1:49125', '1:49141', '1:50208', '1:54814', '1:54883', '1:80530', '1:80575', '1:80543', '1:80667', '1:105563', '1:105955', '1:2166', '1:2281', '1:2584', '1:15704', '1:16651', '1:76438', '1:76447', '1:78431', '1:75265', '1:15398', '1:15935', '1:15942', '1:15956', '1:18453', '1:32381', '1:32610', '1:19731', '1:19323', '1:19387', '1:79498', '1:79514', '1:79519', '1:77587', '1:69643', '1:73895', '1:72246', '1:71703', '1:31941', '1:51037', '1:47224', '1:46674', '1:46710', '1:55625', '1:62840', '1:68005', '1:59878', '1:66909', '1:70972', '1:32550', '1:47386', '1:47448', '1:47525', '1:58350', '1:61787', '1:61869', '1:81356', '1:81024', '1:77733', '1:2967', '1:3346', '1:3699', '1:1235', '1:4503', '1:58954', '1:61114', '1:58353', '1:61846', '1:82150', '1:82174', '1:84049', '1:81679', '1:82182', '1:84487', '1:79234', '1:82152', '1:82041', '1:82172', '1:83005', '1:83079', '1:101512', '1:101507', '1:101527', '1:101400', '1:101642', '1:87548', '1:91153', '1:87631', '1:87765', '1:87853', '1:88063', '1:89238', '1:89532', '1:87310', '1:89378', '1:89197', '1:89426', '1:101833', '1:97131', '1:3985', '1:4604', '1:3800', '1:3805', '1:4633', '1:72811', '1:72816', '1:75358', '1:75403', '1:72570', '1:72527', '1:76081', '1:76041', '1:76343', '1:31033', '1:31193', '1:31228', '1:31475', '1:31533', '1:30339', '1:30504', '1:30676', '1:30688', '1:30704', '1:75239', '1:76050', '1:89102', '1:89129', '1:14638', '1:15165', '1:16421', '1:16526', '1:16681', '1:17198', '1:20656', '1:30326', '1:30371', '1:30455', '1:30513', '1:30514', '1:58460', '1:59126', '1:62136', '1:25172', '1:25239', '1:31206', '1:31084', '1:31202', '1:90206', '1:90229', '1:90232', '1:101916', '1:41934', '1:101676', '1:11228', '1:11231', '1:11310', '1:13163', '1:22300', '1:25295', '1:31014', '1:31041', '1:31098', '1:31175', '1:31183', '1:29967', '1:31262', '1:61514', '1:62165', '1:63541', '1:17308', '1:18937', '1:20475', '1:26129', '1:26626', '1:39712', '1:52404', '1:52755', '1:46628', '1:52269', '1:56954', '1:53984', '1:53992', '1:54152', '1:55090', '1:85424', '1:80829', '1:75938', '1:76024', '1:90859', '1:90087', '1:90102', '1:90333', '1:101519', '1:101522', '1:30182', '1:26612', '1:26959', '1:34213', '1:46602', '1:43064', '1:39040', '1:39045', '1:39065', '1:39066', '1:39082', '1:39101', '1:39112', '1:62469', '1:49731', '1:44993', '1:74996', '1:75383', '1:75399', '1:71632', '1:66128', '1:66918', '1:71959', '1:72698', '1:73032', '1:72682', '1:74613', '1:76550', '1:81364', '1:81365', '1:80269', '1:80279', '1:11115', '1:11127', '1:22962', '1:90293', '1:13212', '1:13737', '1:13561', '1:13645', '1:22730', '1:22746', '1:22749', '1:22785', '1:22787', '1:22792', '1:22839', '1:22852', '1:22858', '1:22942', '1:63060', '1:89063', '1:89195', '1:89048', '1:103012', '1:103121', '1:103092', '1:103125', '1:103157', '1:103230', '1:103301', '1:1889', '1:1913', '1:12933', '1:17205', '1:95968', '1:95053', '1:95069', '1:96122', '1:102797', '1:25430', '1:25476', '1:25520', '1:31775', '1:101147', '1:101278', '1:25352', '1:25361', '1:25368', '1:25390', '1:65357', '1:66518', '1:73375', '1:70847', '1:19626', '1:19646', '1:24150', '1:25301', '1:33297', '1:33434', '1:34738', '1:30911', '1:31886', '1:31909', '1:31944', '1:31968', '1:31982', '1:31984', '1:31990', '1:32458', '1:32529', '1:42506', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E121475-8F16-EA11-8E04-A0369FE2C0B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/30928809-BC17-EA11-BB9F-FA163EB84C2E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/4E9AEF96-7917-EA11-924F-FA163EFE3C83.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3800FB9D-1118-EA11-AEEA-FA163E3C6BCA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA02D583-D717-EA11-8AB6-AC1F6B8DD1F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E962FC4-1218-EA11-A4E7-008CFA1983BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/18F8D4AE-5818-EA11-AC1B-002590DC0352.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6CF856BA-FF16-EA11-9606-AC1F6B0DE2E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8EE12E36-9617-EA11-B775-FA163ED521CB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54894913-D216-EA11-8F84-A0369FF88246.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1685CFE4-5118-EA11-95CB-003048F2E8C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8AC2DDFC-8E17-EA11-A339-FA163E5AB700.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/386B181A-9017-EA11-A440-5065F3816251.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2A1CF336-1318-EA11-B91E-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/48B048F8-9017-EA11-B603-FA163E7ED2D2.root']);