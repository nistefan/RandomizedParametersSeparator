import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:51086', '1:51254', '1:51334', '1:51386', '1:51471', '1:51502', '1:67545', '1:68083', '1:67369', '1:67893', '1:68811', '1:68852', '1:69206', '1:92477', '1:92483', '1:92485', '1:92423', '1:92426', '1:92492', '1:92716', '1:93204', '1:77690', '1:78036', '1:78119', '1:78141', '1:79254', '1:82100', '1:85026', '1:737', '1:2732', '1:2771', '1:2803', '1:3504', '1:4610', '1:98934', '1:99858', '1:99871', '1:35857', '1:35449', '1:36706', '1:40019', '1:40068', '1:40169', '1:40193', '1:40213', '1:40215', '1:40256', '1:53222', '1:52429', '1:53812', '1:53956', '1:54001', '1:54798', '1:79771', '1:79817', '1:79825', '1:80848', '1:80860', '1:80884', '1:82399', '1:95570', '1:95652', '1:96032', '1:97785', '1:99053', '1:99153', '1:99210', '1:106165', '1:106270', '1:106291', '1:14329', '1:14669', '1:14699', '1:15993', '1:17090', '1:19904', '1:20577', '1:20617', '1:20770', '1:20817', '1:46004', '1:47403', '1:47772', '1:47822', '1:75582', '1:76781', '1:80067', '1:5054', '1:5483', '1:5564', '1:7184', '1:7205', '1:7513', '1:5159', '1:15892', '1:28834', '1:34455', '1:37631', '1:37699', '1:37663', '1:46551', '1:59142', '1:62095', '1:8380', '1:8462', '1:8785', '1:16701', '1:12793', '1:15854', '1:15924', '1:15936', '1:16990', '1:16995', '1:17145', '1:35353', '1:83622', '1:94043', '1:94331', '1:94492', '1:92793', '1:98903', '1:99475', '1:105566', '1:106221', '1:106220', '1:64317', '1:64434', '1:64465', '1:64799', '1:65606', '1:67093', '1:67110', '1:67148', '1:67252', '1:65789', '1:65886', '1:65985', '1:67065', '1:67295', '1:65788', '1:68234', '1:68319', '1:68863', '1:68915', '1:68904', '1:74907', '1:69042', '1:69106', '1:69019', '1:69031', '1:88055', '1:94658', '1:94706', '1:94872', '1:88322', '1:88335', '1:88379', '1:88387', '1:102432', '1:94489', '1:94603', '1:94644', '1:94661', '1:102440', '1:102466', '1:102523', '1:102546', '1:102548', '1:102627', '1:102668', '1:102476', '1:64882', '1:64996', '1:64861', '1:64789', '1:80109', '1:80113', '1:80160', '1:80185', '1:79067', '1:79164', '1:82601', '1:38223', '1:38449', '1:38478', '1:38495', '1:44050', '1:42135', '1:42640', '1:42669', '1:44243', '1:45244', '1:44302', '1:45296', '1:45347', '1:45316', '1:46775', '1:46815', '1:46955', '1:51648', '1:52469', '1:54094', '1:54556', '1:55951', '1:56068', '1:57495', '1:84647', '1:73321', '1:73585', '1:73637', '1:75972', '1:78126', '1:96787', '1:97363', '1:99106', '1:95949', '1:96027', '1:96030', '1:96201', '1:60233', '1:53865', '1:58396', '1:59563', '1:60509', '1:63656', '1:67170', '1:63445', '1:67837', '1:67888', '1:68069', '1:71169', '1:65927', '1:66900', '1:73511', '1:67415', '1:64052', '1:64621', '1:66914', '1:70072', '1:65651', '1:69962', '1:66633', '1:71078', '1:88074', '1:78056', '1:91512', '1:91580', '1:97659', '1:60940', '1:63985', '1:103803', '1:15825', '1:15911', '1:17821', '1:12760', '1:16145', '1:20601', '1:7155', '1:7260', '1:7463', '1:14345', '1:14363', '1:14338', '1:10558', '1:12829', '1:5101', '1:5201', '1:5303', '1:5304', '1:5360', '1:5292', '1:5617', '1:57617', '1:7016', '1:7036', '1:9069', '1:9123', '1:9130', '1:8252', '1:8401', '1:10340', '1:10468', '1:10820', '1:10885', '1:12384', '1:68671', '1:68719', '1:68798', '1:69426', '1:69452', '1:71727', '1:71735', '1:85234', '1:85697', '1:85934', '1:85632', '1:85670', '1:85762', '1:85769', '1:94978', '1:94323', '1:40776', '1:50489', '1:50594', '1:50683', '1:52244', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/06F65C32-13F3-E911-AC5A-002590DE6E30.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4253ADC4-03F5-E911-AFEA-AC1F6B0DE0A0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0014CD18-06F6-E911-8B27-FA163E69BD36.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E66B73CD-70F7-E911-8EBA-E0071B7A18F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/043AF729-4A10-EA11-B2D6-0CC47AFF2492.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/68454F20-060A-EA11-A63A-AC1F6BAC816C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D2B1428C-88F2-E911-B4D4-3417EBE705CD.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3C9F3E3A-5600-EA11-B8FE-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE1AA428-17F0-E911-A0AE-0CC47A4DEDB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A217F84B-F6F2-E911-84C6-A0369F5BD8D4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC608F2A-9802-EA11-984E-D48564599C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38FDE37B-BEFC-E911-B96A-001E67E5EDBB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/48D3300C-5110-EA11-A284-00259090822A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40DCE1CF-C002-EA11-B8F4-0CC47AFF0220.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8CD8C04A-5210-EA11-8222-0025904B04A8.root']);