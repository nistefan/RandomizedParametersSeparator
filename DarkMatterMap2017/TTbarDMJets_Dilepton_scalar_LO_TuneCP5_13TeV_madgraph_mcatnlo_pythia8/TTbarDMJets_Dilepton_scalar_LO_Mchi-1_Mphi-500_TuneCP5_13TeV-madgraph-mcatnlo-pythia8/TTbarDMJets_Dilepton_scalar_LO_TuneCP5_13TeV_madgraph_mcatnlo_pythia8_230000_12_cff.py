import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:44955', '1:49049', '1:68692', '1:68757', '1:68950', '1:69780', '1:69924', '1:103400', '1:97760', '1:17316', '1:17395', '1:18793', '1:62842', '1:63660', '1:70486', '1:70568', '1:70541', '1:70653', '1:70694', '1:70760', '1:70776', '1:71020', '1:70914', '1:74782', '1:2536', '1:2589', '1:9313', '1:15877', '1:17859', '1:78862', '1:27305', '1:27980', '1:28357', '1:28376', '1:26997', '1:24998', '1:28329', '1:63', '1:402', '1:1017', '1:796', '1:3257', '1:4145', '1:7652', '1:7239', '1:7748', '1:12436', '1:5623', '1:9197', '1:12503', '1:12885', '1:14869', '1:16389', '1:3286', '1:4991', '1:2573', '1:2646', '1:8703', '1:10282', '1:1531', '1:1631', '1:1915', '1:4417', '1:4511', '1:4627', '1:4702', '1:4706', '1:32742', '1:34637', '1:3608', '1:7341', '1:3501', '1:21985', '1:38774', '1:38780', '1:12550', '1:12636', '1:12795', '1:20896', '1:27127', '1:27753', '1:27774', '1:24469', '1:24657', '1:2481', '1:2999', '1:9684', '1:5833', '1:5916', '1:9587', '1:43297', '1:43435', '1:36040', '1:38454', '1:42773', '1:45313', '1:46592', '1:58986', '1:60001', '1:60085', '1:64211', '1:21607', '1:27593', '1:27860', '1:27984', '1:19401', '1:27533', '1:27992', '1:34270', '1:18682', '1:18856', '1:82257', '1:59377', '1:62929', '1:67511', '1:69506', '1:69605', '1:8330', '1:9984', '1:10190', '1:7185', '1:10018', '1:10038', '1:10174', '1:12913', '1:12381', '1:12391', '1:12865', '1:8221', '1:8130', '1:8133', '1:8377', '1:8458', '1:10251', '1:9572', '1:9781', '1:8520', '1:8699', '1:10616', '1:10893', '1:12096', '1:12264', '1:10770', '1:10786', '1:10796', '1:10896', '1:88768', '1:88779', '1:88828', '1:88928', '1:56353', '1:62632', '1:69081', '1:64745', '1:68826', '1:68260', '1:94266', '1:77559', '1:77613', '1:77620', '1:77622', '1:77630', '1:77806', '1:98422', '1:99912', '1:100420', '1:96547', '1:100806', '1:102353', '1:102468', '1:104385', '1:104455', '1:106029', '1:105766', '1:105779', '1:2276', '1:2419', '1:45838', '1:47028', '1:47463', '1:42348', '1:43840', '1:45142', '1:46223', '1:69754', '1:71966', '1:70222', '1:70259', '1:70268', '1:70289', '1:2490', '1:4636', '1:5747', '1:8970', '1:52578', '1:53103', '1:64748', '1:64659', '1:64723', '1:64641', '1:64664', '1:64771', '1:21353', '1:21707', '1:21779', '1:21864', '1:24017', '1:24033', '1:24041', '1:57988', '1:60176', '1:60701', '1:21848', '1:21940', '1:21966', '1:21974', '1:22000', '1:24212', '1:24276', '1:36484', '1:36557', '1:36609', '1:34838', '1:34903', '1:38122', '1:45599', '1:45694', '1:45703', '1:41002', '1:44241', '1:44307', '1:44478', '1:44607', '1:44612', '1:44644', '1:56837', '1:57365', '1:56823', '1:56866', '1:56927', '1:57100', '1:60539', '1:60621', '1:60467', '1:14836', '1:15071', '1:15348', '1:15447', '1:15455', '1:15513', '1:15266', '1:15277', '1:15402', '1:46287', '1:47153', '1:47132', '1:55404', '1:56011', '1:56867', '1:57536', '1:59913', '1:56335', '1:26179', '1:27264', '1:26176', '1:27976', '1:28112', '1:28219', '1:28195', '1:28196', '1:28315', '1:44768', '1:9996', '1:10030', '1:10064', '1:10339', '1:12076', '1:12091', '1:12324', '1:14328', '1:14459', '1:15051', '1:15813', '1:16077', '1:16094', '1:16735', '1:16827', '1:16919', '1:24442', '1:24784', '1:24788', '1:27640', '1:27866', '1:27977', '1:86061', '1:72616', '1:72671', '1:75203', '1:75220', '1:85960', '1:85964', '1:85966', '1:86207', '1:86231', '1:86297', '1:86334', '1:86698', '1:105880', '1:67954', '1:68872', '1:68379', '1:68700', '1:68746', '1:68747', '1:69046', '1:68645', '1:68676', '1:68739', '1:75597', '1:77310', '1:77041', '1:77060', '1:77068', '1:93921', '1:93928', '1:95921', '1:77224', '1:77229', '1:77417', '1:77542', '1:82931', '1:92591', '1:94233', '1:94526', '1:94415', '1:94434', '1:94451', '1:94549', '1:94556', '1:94620', '1:103939', '1:88473', '1:88483', '1:88486', '1:88532', '1:88548', '1:88568', '1:88572', '1:93941', '1:93951', '1:1014', '1:1358', '1:17391', '1:15735', '1:18199', '1:35463', '1:37371', '1:39501', '1:49040', '1:50423', '1:46195', '1:45136', '1:45520', '1:45732', '1:43613', '1:40496', '1:44811', '1:39524', '1:40661', '1:47711', '1:40180', '1:47984', '1:50746', '1:706', '1:1302', '1:46877', '1:47061', '1:48511', '1:51345', '1:52324', '1:51533', '1:54159', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84233716-610E-EA11-A99E-AC1F6B1AF194.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92C94FAE-5604-EA11-B1B4-AC1F6B1AF05A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA68F6BC-8307-EA11-95D2-1CC1DE055158.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/46E4AEC6-90ED-E911-B705-EC0D9A82262E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5EC502A2-6603-EA11-90F8-0CC47A4DED8C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8AA75E62-AB02-EA11-B51D-0025905C3E68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8DA5D68-F10B-EA11-AFB4-0025905B85E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78EFAF8D-1A04-EA11-8B9D-002590A83354.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2ABCC36E-6AFF-E911-8B20-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CED587AE-2CEF-E911-AD36-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E5BA0CA-85EE-E911-A8AF-C4544423E341.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B47C7A37-D803-EA11-AFBA-0CC47A5FA3BD.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/468AC653-A5F2-E911-B9B2-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9498531C-02EE-E911-B5FE-EC0D9A822626.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DEFACFCF-8E02-EA11-9176-AC1F6BABF8D5.root']);