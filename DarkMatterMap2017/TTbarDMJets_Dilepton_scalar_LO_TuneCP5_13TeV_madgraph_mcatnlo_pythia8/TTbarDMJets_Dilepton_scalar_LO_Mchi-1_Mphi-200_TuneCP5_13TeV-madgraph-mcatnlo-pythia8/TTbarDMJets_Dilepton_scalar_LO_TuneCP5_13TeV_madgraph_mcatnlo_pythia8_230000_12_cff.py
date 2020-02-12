import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:41335', '1:48013', '1:52103', '1:49623', '1:48548', '1:68890', '1:69238', '1:103804', '1:17118', '1:17249', '1:62557', '1:62567', '1:62588', '1:63025', '1:63180', '1:70497', '1:70526', '1:71051', '1:72747', '1:72813', '1:74766', '1:2850', '1:2913', '1:3580', '1:3760', '1:2804', '1:104948', '1:15509', '1:15641', '1:15794', '1:17052', '1:17485', '1:17655', '1:18809', '1:18562', '1:35116', '1:26465', '1:27074', '1:121', '1:1107', '1:1116', '1:7494', '1:8201', '1:12901', '1:3024', '1:3187', '1:3897', '1:9545', '1:10003', '1:4200', '1:4403', '1:4524', '1:4995', '1:32719', '1:32756', '1:34054', '1:34116', '1:34519', '1:34678', '1:5346', '1:5189', '1:5951', '1:9009', '1:9497', '1:5116', '1:7056', '1:27569', '1:32679', '1:10035', '1:14331', '1:20366', '1:19874', '1:19915', '1:24811', '1:27192', '1:27498', '1:27791', '1:2642', '1:5952', '1:9514', '1:9668', '1:37046', '1:38736', '1:35796', '1:38647', '1:42217', '1:42421', '1:58100', '1:58113', '1:21818', '1:21824', '1:27176', '1:27757', '1:19204', '1:19400', '1:20757', '1:20777', '1:21160', '1:27780', '1:32612', '1:74933', '1:76103', '1:80572', '1:56759', '1:68571', '1:68579', '1:69006', '1:65449', '1:85854', '1:91536', '1:8174', '1:8192', '1:8281', '1:8427', '1:10263', '1:7183', '1:8571', '1:8676', '1:10012', '1:10073', '1:10194', '1:12522', '1:7520', '1:7623', '1:7759', '1:7817', '1:8179', '1:8208', '1:9246', '1:9249', '1:7873', '1:7937', '1:7957', '1:7970', '1:8055', '1:8374', '1:8484', '1:8583', '1:9584', '1:9609', '1:10834', '1:10836', '1:14805', '1:14832', '1:14917', '1:15033', '1:16323', '1:16332', '1:16413', '1:88830', '1:88854', '1:88887', '1:59985', '1:62519', '1:63267', '1:67521', '1:56272', '1:62504', '1:62499', '1:63182', '1:68922', '1:68819', '1:68827', '1:86258', '1:91398', '1:94509', '1:94761', '1:86468', '1:86996', '1:77546', '1:77602', '1:100939', '1:98013', '1:100652', '1:100761', '1:102152', '1:102156', '1:102177', '1:102269', '1:102437', '1:102512', '1:104345', '1:104360', '1:104469', '1:106046', '1:106074', '1:106117', '1:105730', '1:1239', '1:2101', '1:2516', '1:42412', '1:65405', '1:66285', '1:66879', '1:70337', '1:70370', '1:665', '1:787', '1:10976', '1:12067', '1:46407', '1:48158', '1:49180', '1:41789', '1:52551', '1:53033', '1:53890', '1:53897', '1:53933', '1:54553', '1:56328', '1:64757', '1:64600', '1:64732', '1:64666', '1:70153', '1:21343', '1:21613', '1:21814', '1:21899', '1:24003', '1:24194', '1:24204', '1:40845', '1:54812', '1:56622', '1:60151', '1:60168', '1:60702', '1:97301', '1:24055', '1:24211', '1:24214', '1:24410', '1:24422', '1:24440', '1:36209', '1:36276', '1:36548', '1:35355', '1:33991', '1:34966', '1:34305', '1:34325', '1:36846', '1:37761', '1:37348', '1:45537', '1:45613', '1:45653', '1:45657', '1:45688', '1:45841', '1:41029', '1:44188', '1:44240', '1:44293', '1:44348', '1:44474', '1:44488', '1:44564', '1:44605', '1:56715', '1:56793', '1:56924', '1:60797', '1:60291', '1:60456', '1:60469', '1:15112', '1:15213', '1:15222', '1:15136', '1:45772', '1:47067', '1:47128', '1:47022', '1:47140', '1:47150', '1:54362', '1:57494', '1:26120', '1:28227', '1:32265', '1:32403', '1:33171', '1:33177', '1:33322', '1:33334', '1:27966', '1:28003', '1:28161', '1:28241', '1:28356', '1:28421', '1:44747', '1:9893', '1:9982', '1:10184', '1:10324', '1:12230', '1:12366', '1:16146', '1:16940', '1:16943', '1:24513', '1:24624', '1:27348', '1:27675', '1:27721', '1:75136', '1:75168', '1:75216', '1:105966', '1:67932', '1:68387', '1:68520', '1:68536', '1:69112', '1:68887', '1:68766', '1:75702', '1:75714', '1:77382', '1:77398', '1:77726', '1:77760', '1:93939', '1:95395', '1:95898', '1:95973', '1:77109', '1:77164', '1:77265', '1:93280', '1:87379', '1:88480', '1:91015', '1:94188', '1:94439', '1:94636', '1:103492', '1:88460', '1:93689', '1:1011', '1:1373', '1:1923', '1:589', '1:17954', '1:20498', '1:14519', '1:16051', '1:15768', '1:41871', '1:41831', '1:50032', '1:36076', '1:46170', '1:46379', '1:46408', '1:43664', '1:45297', '1:46789', '1:47847', '1:47882', '1:43886', '1:47531', '1:50053', '1:53202', '1:53474', '1:53622', '1:427', '1:578', '1:745', '1:800', '1:48353', '1:49054', '1:51093', '1:51795', '1:51273', '1:92206', '1:91853', '1:92384', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84233716-610E-EA11-A99E-AC1F6B1AF194.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92C94FAE-5604-EA11-B1B4-AC1F6B1AF05A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA68F6BC-8307-EA11-95D2-1CC1DE055158.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/46E4AEC6-90ED-E911-B705-EC0D9A82262E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5EC502A2-6603-EA11-90F8-0CC47A4DED8C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8AA75E62-AB02-EA11-B51D-0025905C3E68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8DA5D68-F10B-EA11-AFB4-0025905B85E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78EFAF8D-1A04-EA11-8B9D-002590A83354.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2ABCC36E-6AFF-E911-8B20-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CED587AE-2CEF-E911-AD36-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E5BA0CA-85EE-E911-A8AF-C4544423E341.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B47C7A37-D803-EA11-AFBA-0CC47A5FA3BD.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/468AC653-A5F2-E911-B9B2-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9498531C-02EE-E911-B5FE-EC0D9A822626.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DEFACFCF-8E02-EA11-9176-AC1F6BABF8D5.root']);