import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:336', '1:374', '1:653', '1:3611', '1:19563', '1:19224', '1:19479', '1:100493', '1:103660', '1:21368', '1:103725', '1:47281', '1:48212', '1:49095', '1:49405', '1:50306', '1:50358', '1:53848', '1:54839', '1:80528', '1:80553', '1:105015', '1:5518', '1:6813', '1:23201', '1:23371', '1:76316', '1:15778', '1:16657', '1:17355', '1:17617', '1:18483', '1:20353', '1:26768', '1:28180', '1:32367', '1:76398', '1:81575', '1:19606', '1:19332', '1:19433', '1:19454', '1:19530', '1:79004', '1:79020', '1:63328', '1:63344', '1:63391', '1:67897', '1:66613', '1:72210', '1:73448', '1:73855', '1:73284', '1:31272', '1:30893', '1:30914', '1:31940', '1:46277', '1:50805', '1:46689', '1:54702', '1:63070', '1:67274', '1:67533', '1:59619', '1:73205', '1:69811', '1:70342', '1:72401', '1:32673', '1:76142', '1:77258', '1:56822', '1:60364', '1:54054', '1:55591', '1:62218', '1:62364', '1:65526', '1:79078', '1:79326', '1:106323', '1:2621', '1:2726', '1:3305', '1:3316', '1:3103', '1:4931', '1:59101', '1:59641', '1:60793', '1:61206', '1:61191', '1:61742', '1:63764', '1:77807', '1:82073', '1:82333', '1:84729', '1:79786', '1:81482', '1:82834', '1:84501', '1:84504', '1:85340', '1:86126', '1:93432', '1:79725', '1:84885', '1:101940', '1:101945', '1:84719', '1:85867', '1:91031', '1:94335', '1:88515', '1:86358', '1:91686', '1:89478', '1:89549', '1:89607', '1:101840', '1:101863', '1:101839', '1:101784', '1:90980', '1:101831', '1:2298', '1:2454', '1:2586', '1:2667', '1:2912', '1:76090', '1:76123', '1:76552', '1:31537', '1:30359', '1:30673', '1:30727', '1:74234', '1:75278', '1:77280', '1:15401', '1:30430', '1:30494', '1:30782', '1:30786', '1:60030', '1:25232', '1:25255', '1:25674', '1:30174', '1:31044', '1:31352', '1:31440', '1:31048', '1:31103', '1:31122', '1:31146', '1:89834', '1:90096', '1:101616', '1:89902', '1:90271', '1:90120', '1:22086', '1:31190', '1:29977', '1:30213', '1:30226', '1:64147', '1:65578', '1:13172', '1:11485', '1:26675', '1:50285', '1:53024', '1:39563', '1:41638', '1:46868', '1:47361', '1:56543', '1:53928', '1:53950', '1:54119', '1:54172', '1:54993', '1:80708', '1:84275', '1:75963', '1:75965', '1:76021', '1:90268', '1:90276', '1:90093', '1:90109', '1:101803', '1:29393', '1:26429', '1:26520', '1:26605', '1:28613', '1:46729', '1:47037', '1:39095', '1:39115', '1:39505', '1:48868', '1:48886', '1:51038', '1:48813', '1:51773', '1:52231', '1:52008', '1:72795', '1:75090', '1:75455', '1:72442', '1:72861', '1:72922', '1:74670', '1:74803', '1:73166', '1:73524', '1:66444', '1:11072', '1:11078', '1:22961', '1:89407', '1:31566', '1:13746', '1:13639', '1:13663', '1:13896', '1:22784', '1:22801', '1:22804', '1:22821', '1:22912', '1:61868', '1:62902', '1:66593', '1:66594', '1:89021', '1:89067', '1:89637', '1:102990', '1:103011', '1:103184', '1:103224', '1:103269', '1:103333', '1:2440', '1:3335', '1:15013', '1:96556', '1:99057', '1:102118', '1:102126', '1:102142', '1:95174', '1:96613', '1:19587', '1:20995', '1:29257', '1:31771', '1:89148', '1:25356', '1:25388', '1:72960', '1:73146', '1:73859', '1:24235', '1:24494', '1:24850', '1:24968', '1:33259', '1:32434', '1:32902', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E121475-8F16-EA11-8E04-A0369FE2C0B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/30928809-BC17-EA11-BB9F-FA163EB84C2E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/4E9AEF96-7917-EA11-924F-FA163EFE3C83.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3800FB9D-1118-EA11-AEEA-FA163E3C6BCA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA02D583-D717-EA11-8AB6-AC1F6B8DD1F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E962FC4-1218-EA11-A4E7-008CFA1983BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/18F8D4AE-5818-EA11-AC1B-002590DC0352.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6CF856BA-FF16-EA11-9606-AC1F6B0DE2E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8EE12E36-9617-EA11-B775-FA163ED521CB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54894913-D216-EA11-8F84-A0369FF88246.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1685CFE4-5118-EA11-95CB-003048F2E8C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8AC2DDFC-8E17-EA11-A339-FA163E5AB700.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/386B181A-9017-EA11-A440-5065F3816251.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2A1CF336-1318-EA11-B91E-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/48B048F8-9017-EA11-B603-FA163E7ED2D2.root']);