import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:41784', '1:44905', '1:48064', '1:49102', '1:68765', '1:68894', '1:68948', '1:68983', '1:69175', '1:69449', '1:69584', '1:99198', '1:16852', '1:17085', '1:17585', '1:62458', '1:67346', '1:69368', '1:77941', '1:70511', '1:70645', '1:70527', '1:70641', '1:70720', '1:70793', '1:70800', '1:74283', '1:74982', '1:75462', '1:3572', '1:2509', '1:9312', '1:103943', '1:15248', '1:15890', '1:15906', '1:17410', '1:17631', '1:18241', '1:18279', '1:18627', '1:21731', '1:27214', '1:27724', '1:27620', '1:533', '1:4479', '1:81', '1:1001', '1:1405', '1:7050', '1:8100', '1:8880', '1:8992', '1:10424', '1:12868', '1:14880', '1:3784', '1:4580', '1:2099', '1:2725', '1:2880', '1:1695', '1:2059', '1:3657', '1:4622', '1:32960', '1:28501', '1:42479', '1:12594', '1:16725', '1:34685', '1:19358', '1:24694', '1:26064', '1:27636', '1:2891', '1:5884', '1:5904', '1:5158', '1:42276', '1:43198', '1:35711', '1:38776', '1:38865', '1:42219', '1:68630', '1:59007', '1:61491', '1:64245', '1:69831', '1:15427', '1:24392', '1:24671', '1:19488', '1:19520', '1:24960', '1:27445', '1:27460', '1:27842', '1:27425', '1:21690', '1:32558', '1:18673', '1:70998', '1:75570', '1:77512', '1:85099', '1:67976', '1:68576', '1:71559', '1:73608', '1:82941', '1:4198', '1:4350', '1:8333', '1:8358', '1:10027', '1:10028', '1:10100', '1:10140', '1:10166', '1:9722', '1:10023', '1:10040', '1:10041', '1:10133', '1:10147', '1:10203', '1:10288', '1:10379', '1:12411', '1:12508', '1:12966', '1:7499', '1:7617', '1:9174', '1:7720', '1:8054', '1:8075', '1:8107', '1:8142', '1:7801', '1:8477', '1:9992', '1:63072', '1:10489', '1:10821', '1:14772', '1:14777', '1:14912', '1:15025', '1:16431', '1:88809', '1:91034', '1:91202', '1:57605', '1:57854', '1:62183', '1:63672', '1:63705', '1:67628', '1:67634', '1:62550', '1:63163', '1:68457', '1:66002', '1:66969', '1:64256', '1:64839', '1:67217', '1:88842', '1:92409', '1:88182', '1:94662', '1:77515', '1:77554', '1:77624', '1:77687', '1:100656', '1:100680', '1:100740', '1:104370', '1:106040', '1:105555', '1:105577', '1:105599', '1:106054', '1:105746', '1:105764', '1:105778', '1:2089', '1:2100', '1:2124', '1:2587', '1:2204', '1:2219', '1:44989', '1:45442', '1:28345', '1:45229', '1:46522', '1:65259', '1:65348', '1:66382', '1:70163', '1:451', '1:672', '1:884', '1:2217', '1:2674', '1:8630', '1:9075', '1:12709', '1:16916', '1:39470', '1:48125', '1:49260', '1:51749', '1:51755', '1:52376', '1:52555', '1:52562', '1:53008', '1:64725', '1:64640', '1:70152', '1:21727', '1:21862', '1:21881', '1:24023', '1:24365', '1:59702', '1:60182', '1:21863', '1:24186', '1:24205', '1:24279', '1:38411', '1:36231', '1:36317', '1:36322', '1:36395', '1:36506', '1:36550', '1:36662', '1:35003', '1:34396', '1:37592', '1:37365', '1:45518', '1:41035', '1:44718', '1:44741', '1:57368', '1:56440', '1:56721', '1:56734', '1:56762', '1:56808', '1:56816', '1:56878', '1:56977', '1:57099', '1:57115', '1:57116', '1:57220', '1:57340', '1:60275', '1:60313', '1:15113', '1:15133', '1:15297', '1:15408', '1:45744', '1:47122', '1:52936', '1:60444', '1:21935', '1:24636', '1:26231', '1:32957', '1:45485', '1:27962', '1:28002', '1:28096', '1:28154', '1:28203', '1:28250', '1:28441', '1:44719', '1:45597', '1:45756', '1:9867', '1:10138', '1:10279', '1:12338', '1:14692', '1:14573', '1:16074', '1:16799', '1:16925', '1:24639', '1:24642', '1:24748', '1:24775', '1:27421', '1:27462', '1:27474', '1:27711', '1:27924', '1:27961', '1:72623', '1:72680', '1:72688', '1:72697', '1:75160', '1:75176', '1:75217', '1:85984', '1:86125', '1:86239', '1:86681', '1:99780', '1:105910', '1:105897', '1:68018', '1:69191', '1:68286', '1:68689', '1:69135', '1:75727', '1:77284', '1:77305', '1:77044', '1:93900', '1:95749', '1:95814', '1:95829', '1:77127', '1:77412', '1:88831', '1:91204', '1:93241', '1:93839', '1:93993', '1:94505', '1:94542', '1:94558', '1:94612', '1:94642', '1:94666', '1:94680', '1:94719', '1:88467', '1:88574', '1:93946', '1:93986', '1:95621', '1:95638', '1:95975', '1:96000', '1:96013', '1:104963', '1:1650', '1:1886', '1:203', '1:406', '1:549', '1:821', '1:968', '1:15995', '1:16936', '1:14081', '1:17226', '1:17965', '1:18337', '1:34857', '1:35627', '1:37740', '1:48549', '1:48607', '1:50036', '1:50541', '1:50923', '1:32891', '1:38545', '1:38845', '1:42615', '1:42685', '1:43053', '1:46162', '1:46677', '1:40585', '1:45659', '1:46319', '1:47493', '1:43094', '1:43329', '1:43464', '1:46921', '1:39010', '1:44769', '1:40110', '1:40617', '1:47303', '1:47925', '1:47978', '1:50092', '1:53428', '1:1837', '1:3263', '1:3497', '1:45158', '1:44728', '1:45939', '1:50768', '1:51511', '1:49572', '1:49037', '1:94468', '1:93349', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84233716-610E-EA11-A99E-AC1F6B1AF194.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92C94FAE-5604-EA11-B1B4-AC1F6B1AF05A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA68F6BC-8307-EA11-95D2-1CC1DE055158.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/46E4AEC6-90ED-E911-B705-EC0D9A82262E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5EC502A2-6603-EA11-90F8-0CC47A4DED8C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8AA75E62-AB02-EA11-B51D-0025905C3E68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8DA5D68-F10B-EA11-AFB4-0025905B85E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78EFAF8D-1A04-EA11-8B9D-002590A83354.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2ABCC36E-6AFF-E911-8B20-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CED587AE-2CEF-E911-AD36-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E5BA0CA-85EE-E911-A8AF-C4544423E341.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B47C7A37-D803-EA11-AFBA-0CC47A5FA3BD.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/468AC653-A5F2-E911-B9B2-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9498531C-02EE-E911-B5FE-EC0D9A822626.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DEFACFCF-8E02-EA11-9176-AC1F6BABF8D5.root']);