import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:295', '1:304', '1:345', '1:400', '1:431', '1:503', '1:539', '1:19538', '1:19080', '1:19104', '1:19107', '1:19125', '1:21077', '1:98459', '1:98528', '1:103639', '1:104133', '1:103767', '1:103822', '1:46917', '1:46920', '1:46969', '1:46930', '1:48232', '1:49471', '1:50290', '1:55321', '1:80564', '1:80597', '1:80695', '1:105726', '1:2952', '1:5418', '1:23882', '1:75902', '1:15980', '1:17094', '1:17142', '1:18718', '1:24771', '1:27197', '1:81565', '1:80022', '1:80449', '1:15826', '1:27579', '1:32483', '1:19272', '1:19341', '1:19513', '1:79276', '1:77981', '1:63861', '1:69134', '1:69701', '1:65118', '1:71835', '1:64133', '1:31273', '1:46952', '1:47192', '1:47215', '1:46691', '1:56891', '1:63986', '1:67172', '1:67304', '1:70663', '1:70848', '1:72074', '1:72497', '1:32648', '1:32665', '1:56646', '1:57665', '1:60370', '1:58873', '1:61788', '1:61823', '1:61894', '1:62196', '1:62366', '1:74429', '1:79539', '1:79565', '1:77096', '1:69348', '1:2666', '1:2941', '1:858', '1:997', '1:3256', '1:56351', '1:62494', '1:62986', '1:59471', '1:80094', '1:86014', '1:81989', '1:84745', '1:84270', '1:84538', '1:85409', '1:90246', '1:101509', '1:101636', '1:101647', '1:101917', '1:101950', '1:101959', '1:83026', '1:88080', '1:87791', '1:88098', '1:89217', '1:86780', '1:92314', '1:92354', '1:92581', '1:93056', '1:89223', '1:89379', '1:89600', '1:89606', '1:87348', '1:92828', '1:92870', '1:89222', '1:89228', '1:89386', '1:89400', '1:89213', '1:89562', '1:89534', '1:101832', '1:101779', '1:101811', '1:101822', '1:2273', '1:2437', '1:2470', '1:2562', '1:72518', '1:75609', '1:76165', '1:76198', '1:76200', '1:31538', '1:30348', '1:30726', '1:30732', '1:89092', '1:16130', '1:17170', '1:15396', '1:16673', '1:17405', '1:21792', '1:11063', '1:33768', '1:30419', '1:41555', '1:45693', '1:60060', '1:61628', '1:62105', '1:62733', '1:25173', '1:25238', '1:30169', '1:31049', '1:31356', '1:31116', '1:31153', '1:31207', '1:31371', '1:101312', '1:101805', '1:90183', '1:90114', '1:90124', '1:101905', '1:101910', '1:62340', '1:90127', '1:90344', '1:101575', '1:101591', '1:11499', '1:29691', '1:31006', '1:31034', '1:31046', '1:31110', '1:31118', '1:31189', '1:29980', '1:30208', '1:31263', '1:31298', '1:61992', '1:62148', '1:59051', '1:63165', '1:13156', '1:22324', '1:15773', '1:18935', '1:20065', '1:20441', '1:28775', '1:39739', '1:50130', '1:50376', '1:51639', '1:39556', '1:55717', '1:57030', '1:56514', '1:50817', '1:59414', '1:53861', '1:53875', '1:53983', '1:54939', '1:55126', '1:55232', '1:75588', '1:83081', '1:75897', '1:75898', '1:75908', '1:90077', '1:90079', '1:90085', '1:90088', '1:90100', '1:90280', '1:90501', '1:26504', '1:28861', '1:28977', '1:26924', '1:28337', '1:32408', '1:51819', '1:47139', '1:46604', '1:35875', '1:38324', '1:43517', '1:39001', '1:39049', '1:39072', '1:39083', '1:39094', '1:39109', '1:39117', '1:39133', '1:44610', '1:41721', '1:52330', '1:49911', '1:52276', '1:49656', '1:72773', '1:72261', '1:72976', '1:74591', '1:74916', '1:65021', '1:65364', '1:66951', '1:71065', '1:64425', '1:65487', '1:73294', '1:66954', '1:78713', '1:76133', '1:78577', '1:81198', '1:11113', '1:11531', '1:30011', '1:30016', '1:11505', '1:30772', '1:13568', '1:13653', '1:22815', '1:22817', '1:22819', '1:22803', '1:22864', '1:22938', '1:25089', '1:59795', '1:61661', '1:62695', '1:62705', '1:71716', '1:89431', '1:89012', '1:89019', '1:89079', '1:89131', '1:89136', '1:89480', '1:103118', '1:103140', '1:103142', '1:103127', '1:103155', '1:103160', '1:103161', '1:103219', '1:103206', '1:9004', '1:12500', '1:15718', '1:96467', '1:102946', '1:105504', '1:96702', '1:99308', '1:19327', '1:19855', '1:25483', '1:25503', '1:25529', '1:29184', '1:24859', '1:25002', '1:101159', '1:25369', '1:33410', '1:75022', '1:19643', '1:21837', '1:21851', '1:21984', '1:25127', '1:24331', '1:24352', '1:24472', '1:24715', '1:26456', '1:33006', '1:31278', '1:31889', '1:31896', '1:31937', '1:31973', '1:31980', '1:32364', '1:32474', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E121475-8F16-EA11-8E04-A0369FE2C0B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/30928809-BC17-EA11-BB9F-FA163EB84C2E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/4E9AEF96-7917-EA11-924F-FA163EFE3C83.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3800FB9D-1118-EA11-AEEA-FA163E3C6BCA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA02D583-D717-EA11-8AB6-AC1F6B8DD1F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E962FC4-1218-EA11-A4E7-008CFA1983BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/18F8D4AE-5818-EA11-AC1B-002590DC0352.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6CF856BA-FF16-EA11-9606-AC1F6B0DE2E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8EE12E36-9617-EA11-B775-FA163ED521CB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54894913-D216-EA11-8F84-A0369FF88246.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1685CFE4-5118-EA11-95CB-003048F2E8C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8AC2DDFC-8E17-EA11-A339-FA163E5AB700.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/386B181A-9017-EA11-A440-5065F3816251.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2A1CF336-1318-EA11-B91E-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/48B048F8-9017-EA11-B603-FA163E7ED2D2.root']);