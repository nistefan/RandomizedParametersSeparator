import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:61554', '1:62750', '1:64189', '1:65583', '1:75917', '1:70199', '1:77583', '1:90482', '1:94142', '1:84238', '1:92189', '1:83352', '1:83604', '1:87525', '1:82367', '1:84451', '1:90263', '1:93206', '1:93520', '1:83525', '1:85851', '1:88593', '1:91532', '1:92970', '1:95691', '1:97286', '1:98231', '1:97574', '1:97706', '1:97947', '1:97957', '1:97973', '1:98221', '1:98222', '1:75474', '1:77524', '1:79946', '1:70230', '1:70481', '1:93476', '1:94482', '1:94603', '1:65935', '1:70226', '1:73430', '1:77751', '1:81227', '1:82408', '1:82447', '1:70687', '1:77540', '1:77849', '1:78264', '1:78793', '1:79887', '1:83461', '1:91401', '1:87626', '1:95414', '1:74203', '1:74947', '1:75094', '1:75661', '1:80666', '1:80669', '1:81329', '1:78269', '1:79936', '1:80019', '1:80066', '1:80301', '1:95706', '1:26259', '1:26323', '1:26387', '1:26405', '1:26435', '1:26494', '1:26510', '1:26610', '1:26614', '1:26891', '1:26906', '1:26987', '1:31028', '1:42326', '1:42715', '1:42847', '1:42996', '1:42756', '1:44005', '1:44009', '1:44358', '1:44368', '1:44098', '1:44100', '1:44178', '1:44210', '1:44363', '1:44375', '1:47019', '1:47360', '1:73530', '1:73767', '1:73927', '1:74261', '1:74415', '1:104458', '1:39924', '1:39926', '1:40043', '1:40293', '1:40617', '1:41248', '1:41776', '1:41817', '1:42004', '1:42036', '1:42149', '1:42191', '1:42199', '1:42386', '1:42400', '1:42418', '1:42450', '1:42491', '1:42730', '1:42868', '1:42990', '1:44090', '1:42850', '1:44091', '1:44157', '1:44344', '1:44609', '1:44619', '1:54656', '1:88141', '1:89672', '1:89773', '1:90021', '1:90167', '1:92974', '1:93091', '1:93230', '1:96237', '1:96526', '1:96396', '1:73588', '1:73693', '1:73805', '1:73813', '1:73953', '1:74101', '1:74213', '1:74318', '1:102323', '1:102372', '1:102409', '1:102520', '1:102560', '1:102700', '1:102710', '1:102812', '1:102863', '1:102872', '1:102889', '1:84428', '1:84450', '1:84581', '1:84588', '1:84693', '1:84725', '1:84811', '1:85104', '1:84937', '1:85088', '1:85309', '1:66456', '1:67492', '1:67800', '1:75761', '1:79865', '1:81724', '1:81877', '1:81978', '1:83960', '1:84770', '1:67515', '1:71665', '1:76978', '1:92633', '1:101596', '1:101538', '1:101604', '1:101679', '1:102546', '1:83810', '1:106251', '1:85902', '1:87601', '1:89548', '1:92824', '1:97193', '1:97246', '1:106105', '1:101992', '1:102965', '1:104008', '1:104900', '1:104914', '1:14357', '1:72309', '1:73061', '1:82623', '1:87765', '1:89040', '1:52081', '1:52083', '1:52424', '1:52478', '1:52548', '1:52602', '1:52633', '1:52657', '1:52781', '1:102978', '1:102989', '1:104038', '1:104095', '1:104122', '1:104160', '1:104274', '1:104418', '1:104472', '1:104473', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4D2AD02-D40A-EA11-A0B7-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E48D6400-92FB-E911-A2F9-0CC47A7FC6D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F89F393C-D012-EA11-B06C-44A842BE76FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/56BCA64F-BC12-EA11-86AC-002590D425C0.root']);