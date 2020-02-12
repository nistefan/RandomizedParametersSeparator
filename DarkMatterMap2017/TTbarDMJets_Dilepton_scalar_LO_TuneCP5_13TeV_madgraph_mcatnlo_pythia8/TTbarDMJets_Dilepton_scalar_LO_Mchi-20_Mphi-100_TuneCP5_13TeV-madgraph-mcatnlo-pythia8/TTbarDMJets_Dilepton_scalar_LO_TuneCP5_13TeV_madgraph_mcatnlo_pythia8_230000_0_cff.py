import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1262', '1:753', '1:3748', '1:7668', '1:34173', '1:32922', '1:35009', '1:37565', '1:54521', '1:55447', '1:59645', '1:69659', '1:55833', '1:58670', '1:59072', '1:59871', '1:60524', '1:61327', '1:61955', '1:64610', '1:64629', '1:69200', '1:69493', '1:68266', '1:66660', '1:59830', '1:74667', '1:1790', '1:3011', '1:3043', '1:2444', '1:26013', '1:42448', '1:45230', '1:48658', '1:52226', '1:15225', '1:15234', '1:15311', '1:15329', '1:15361', '1:15391', '1:38400', '1:38917', '1:15430', '1:15550', '1:15588', '1:15591', '1:15787', '1:17061', '1:17203', '1:17364', '1:26474', '1:43971', '1:45419', '1:47521', '1:44965', '1:72807', '1:53109', '1:53212', '1:53521', '1:53955', '1:83864', '1:84958', '1:85764', '1:86882', '1:83322', '1:84198', '1:84771', '1:86883', '1:87121', '1:91596', '1:79683', '1:79715', '1:79915', '1:79957', '1:28404', '1:28509', '1:28550', '1:28562', '1:28549', '1:28763', '1:28951', '1:64742', '1:69487', '1:70917', '1:71960', '1:77956', '1:79531', '1:77555', '1:77842', '1:78582', '1:80956', '1:78096', '1:78788', '1:86249', '1:86463', '1:86520', '1:84193', '1:84312', '1:84446', '1:95859', '1:95866', '1:95993', '1:96178', '1:96270', '1:18785', '1:24815', '1:20859', '1:26107', '1:26211', '1:39849', '1:40634', '1:45545', '1:44863', '1:44909', '1:47417', '1:47428', '1:47488', '1:48161', '1:48182', '1:32058', '1:32223', '1:32181', '1:39145', '1:39247', '1:39537', '1:39666', '1:39254', '1:39660', '1:41508', '1:41528', '1:42705', '1:36579', '1:40094', '1:40189', '1:40204', '1:40207', '1:35734', '1:35852', '1:35867', '1:48397', '1:48770', '1:48816', '1:72944', '1:75890', '1:76486', '1:75924', '1:77762', '1:78163', '1:78260', '1:78336', '1:78388', '1:78475', '1:78499', '1:86068', '1:85098', '1:85216', '1:86026', '1:79841', '1:85329', '1:85901', '1:91115', '1:91116', '1:51538', '1:54364', '1:53690', '1:53749', '1:71661', '1:73051', '1:73080', '1:71820', '1:73853', '1:73665', '1:74055', '1:73697', '1:73992', '1:83450', '1:83455', '1:85649', '1:86823', '1:87995', '1:88511', '1:74475', '1:74583', '1:74659', '1:74668', '1:74818', '1:74827', '1:74843', '1:95237', '1:80596', '1:80655', '1:81390', '1:95161', '1:95163', '1:95240', '1:95253', '1:95382', '1:95219', '1:95226', '1:15679', '1:15831', '1:17968', '1:19483', '1:19745', '1:43473', '1:46820', '1:44528', '1:55353', '1:59995', '1:60955', '1:55675', '1:57369', '1:57845', '1:52540', '1:57861', '1:54010', '1:56567', '1:57662', '1:60787', '1:56004', '1:58270', '1:59102', '1:59706', '1:19225', '1:19282', '1:19403', '1:19426', '1:19431', '1:19470', '1:19511', '1:19518', '1:41125', '1:41195', '1:41259', '1:41303', '1:41552', '1:41572', '1:41611', '1:51392', '1:51771', '1:51677', '1:51669', '1:71095', '1:71136', '1:70751', '1:70883', '1:71004', '1:78301', '1:78346', '1:78407', '1:78412', '1:78413', '1:78437', '1:78438', '1:78456', '1:78637', '1:86087', '1:86103', '1:86167', '1:86182', '1:86263', '1:86299', '1:1098', '1:207', '1:211', '1:223', '1:1134', '1:1191', '1:824', '1:930', '1:3612', '1:4039', '1:4553', '1:4744', '1:27066', '1:32983', '1:32998', '1:33025', '1:33080', '1:33162', '1:33168', '1:34106', '1:34269', '1:42340', '1:42940', '1:42953', '1:42954', '1:37794', '1:35135', '1:35281', '1:36049', '1:42016', '1:42203', '1:42414', '1:42628', '1:38737', '1:38775', '1:38892', '1:38943', '1:42051', '1:42399', '1:39804', '1:40731', '1:41016', '1:40219', '1:40487', '1:40722', '1:44597', '1:49414', '1:49310', '1:49337', '1:26343', '1:26346', '1:26459', '1:26511', '1:26681', '1:40295', '1:40657', '1:40690', '1:40830', '1:41041', '1:41226', '1:34807', '1:34063', '1:35828', '1:35833', '1:36014', '1:36070', '1:36088', '1:37202', '1:37206', '1:37391', '1:37392', '1:42501', '1:40682', '1:41313', '1:48632', '1:41033', '1:44445', '1:8722', '1:8774', '1:8786', '1:21322', '1:35360', '1:33503', '1:33673', '1:33739', '1:33812', '1:34048', '1:36864', '1:35408', '1:35454', '1:26616', '1:37940', '1:36837', '1:36839', '1:36940', '1:38115', '1:37413', '1:37539', '1:39510', '1:65908', '1:65845', '1:65869', '1:66211', '1:66338', '1:66349', '1:73239', '1:73260', '1:73312', '1:72373', '1:72557', '1:85540', '1:72300', '1:72819', '1:72842', '1:73747', '1:72597', '1:72602', '1:95390', '1:96716', '1:97477', '1:97550', '1:98027', '1:98223', '1:98492', '1:38222', '1:38757', '1:38763', '1:44490', '1:44653', '1:44739', '1:44744', '1:44836', '1:44846', '1:44895', '1:45418', '1:45479', '1:46103', '1:46444', '1:49438', '1:52001', '1:52016', '1:52138', '1:60335', '1:60363', '1:60865', '1:87620', '1:87627', '1:87666', '1:94802', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4643D148-8CEE-E911-99A7-549F351E4006.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/06C0880D-5BEE-E911-8B86-3417EBE7446B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F6171A5F-F2EF-E911-A256-00E081B705E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9AAAA0F6-25EF-E911-B7E1-A0369FC52524.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/18DA53CD-85EE-E911-A3D0-089E0158CC5B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84D69AFF-25EF-E911-8112-089E0158CDE1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9239CEF9-77EF-E911-B001-0CC47A7E69D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/548A6B80-19EF-E911-A713-506B4BB166B6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40CC65EC-25EF-E911-A3C8-3417EBE70684.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50378F1B-71EE-E911-AD26-38EAA78D8ADC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/88A32370-47EF-E911-8B0C-441EA1615D6A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A7EA364-40EF-E911-B34B-38EAA78D89AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D822EACF-33EF-E911-A627-38EAA78D8FB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CE68873-42F0-E911-99DB-441EA1616D3A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/969DC298-18EF-E911-A24A-38EAA78D8B54.root']);