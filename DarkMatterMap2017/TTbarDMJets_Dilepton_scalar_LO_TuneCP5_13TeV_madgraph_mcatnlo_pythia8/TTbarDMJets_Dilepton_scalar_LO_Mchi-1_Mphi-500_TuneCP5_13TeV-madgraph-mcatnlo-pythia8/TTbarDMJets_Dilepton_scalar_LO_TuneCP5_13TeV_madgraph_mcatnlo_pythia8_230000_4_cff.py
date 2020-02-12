import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:61424', '1:61559', '1:61690', '1:61890', '1:62243', '1:79859', '1:80554', '1:80920', '1:88661', '1:88702', '1:91247', '1:66738', '1:66796', '1:66928', '1:66764', '1:66983', '1:71687', '1:77209', '1:77151', '1:77087', '1:77319', '1:77339', '1:88285', '1:88294', '1:88608', '1:88624', '1:91402', '1:94340', '1:17442', '1:21865', '1:24084', '1:24837', '1:32562', '1:33045', '1:33094', '1:33135', '1:34355', '1:35644', '1:33119', '1:35102', '1:43916', '1:104547', '1:104598', '1:104710', '1:51948', '1:52209', '1:52387', '1:52477', '1:52518', '1:52605', '1:52736', '1:52400', '1:52453', '1:52548', '1:53258', '1:98810', '1:98812', '1:99676', '1:99286', '1:99350', '1:99931', '1:102765', '1:102813', '1:102824', '1:102869', '1:102870', '1:46458', '1:46794', '1:70966', '1:71009', '1:71957', '1:73195', '1:71766', '1:72106', '1:92727', '1:92732', '1:92739', '1:93199', '1:93186', '1:93194', '1:93216', '1:92668', '1:92959', '1:93000', '1:4338', '1:4456', '1:4422', '1:4460', '1:4556', '1:4492', '1:18559', '1:18884', '1:98097', '1:98183', '1:98185', '1:98199', '1:98366', '1:98408', '1:4947', '1:5012', '1:26629', '1:7299', '1:14513', '1:37851', '1:46171', '1:21232', '1:20654', '1:20998', '1:54780', '1:55823', '1:40366', '1:45749', '1:47120', '1:40431', '1:40456', '1:41392', '1:43929', '1:73790', '1:14833', '1:14584', '1:14615', '1:14622', '1:14642', '1:45087', '1:42814', '1:43233', '1:46269', '1:47162', '1:44752', '1:48821', '1:83201', '1:83285', '1:83968', '1:60215', '1:60239', '1:60840', '1:68338', '1:68486', '1:68626', '1:69097', '1:69273', '1:69410', '1:69608', '1:69753', '1:65349', '1:97267', '1:97480', '1:97140', '1:97143', '1:97277', '1:97314', '1:97389', '1:97536', '1:12022', '1:12121', '1:12158', '1:12079', '1:12097', '1:54627', '1:58471', '1:97112', '1:97359', '1:97594', '1:34764', '1:58832', '1:60523', '1:65862', '1:67420', '1:75325', '1:74238', '1:74251', '1:74276', '1:74360', '1:74411', '1:74416', '1:74476', '1:74495', '1:74635', '1:74656', '1:105213', '1:105371', '1:105368', '1:41071', '1:48952', '1:49226', '1:83717', '1:102988', '1:103442', '1:103451', '1:53124', '1:53508', '1:55669', '1:55782', '1:55842', '1:55971', '1:57234', '1:57262', '1:79159', '1:79161', '1:79222', '1:79430', '1:79511', '1:79307', '1:79767', '1:103407', '1:1524', '1:1583', '1:1601', '1:1706', '1:1713', '1:1558', '1:1614', '1:1721', '1:1737', '1:1750', '1:1761', '1:1817', '1:16314', '1:17029', '1:17366', '1:3448', '1:9644', '1:4264', '1:4288', '1:9793', '1:9803', '1:9872', '1:10442', '1:10449', '1:10626', '1:10634', '1:10639', '1:10640', '1:10642', '1:10667', '1:10671', '1:10732', '1:33995', '1:38551', '1:49664', '1:49680', '1:33431', '1:41863', '1:49355', '1:9662', '1:9697', '1:9706', '1:9715', '1:59699', '1:12738', '1:12740', '1:12784', '1:51880', '1:52670', '1:53015', '1:53163', '1:64672', '1:69647', '1:54632', '1:54642', '1:54767', '1:103911', '1:104025', '1:104044', '1:104288', '1:104509', '1:104531', '1:104594', '1:104606', '1:104720', '1:104734', '1:104754', '1:104760', '1:106090', '1:106192', '1:106203', '1:102799', '1:102834', '1:103647', '1:104145', '1:421', '1:9607', '1:50646', '1:52125', '1:53379', '1:53800', '1:55694', '1:81990', '1:84037', '1:84086', '1:7020', '1:12227', '1:34009', '1:37257', '1:50694', '1:27968', '1:32230', '1:40608', '1:47422', '1:69806', '1:70487', '1:73748', '1:77321', '1:81919', '1:84292', '1:100128', '1:14050', '1:14430', '1:17800', '1:15281', '1:17559', '1:17607', '1:17944', '1:66673', '1:70039', '1:65228', '1:66088', '1:66134', '1:71762', '1:71778', '1:71895', '1:73251', '1:63191', '1:97219', '1:102065', '1:104263', '1:79512', '1:91739', '1:93436', '1:71092', '1:71113', '1:57069', '1:57263', '1:91085', '1:91090', '1:91423', '1:91463', '1:91787', '1:91924', '1:18633', '1:20222', '1:92107', '1:92119', '1:93127', '1:93510', '1:95883', '1:96939', '1:97663', '1:92920', '1:93896', '1:86394', '1:86491', '1:87249', '1:102718', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C2B2B4A5-90FA-E911-A1ED-FA163E596216.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44AD8F54-33FC-E911-BFC1-44A842CFD5D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BC0C7A45-B3FB-E911-9A20-0025905C53AA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/18D4DE3D-06FB-E911-9D07-0CC47A4DEE78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D60A6FA0-CCFC-E911-BDAF-0CC47A5FC679.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BCA2AA4C-68FB-E911-A22D-001CC4A6CCE6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/68A10C47-6CFF-E911-A5E7-0242AC1C0507.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70D242A1-7FFF-E911-934F-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C045F616-49FE-E911-9BA5-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FAD01C50-69FF-E911-BBD7-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE2BDBAA-1F02-EA11-9F99-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84EBD031-DAFE-E911-A032-002590DE39F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9AE2976D-2503-EA11-916D-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8BF48D7-28FF-E911-86D4-AC1F6BC67D46.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8A44B795-0403-EA11-B303-0CC47AFF014C.root']);