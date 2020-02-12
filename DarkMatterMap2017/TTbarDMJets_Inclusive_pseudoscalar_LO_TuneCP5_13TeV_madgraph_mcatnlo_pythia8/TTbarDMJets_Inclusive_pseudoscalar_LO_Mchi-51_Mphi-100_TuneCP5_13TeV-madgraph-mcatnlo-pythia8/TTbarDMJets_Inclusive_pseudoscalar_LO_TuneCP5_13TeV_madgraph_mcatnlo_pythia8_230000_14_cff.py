import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:57505', '1:79984', '1:80367', '1:86187', '1:95864', '1:105570', '1:105970', '1:101075', '1:101172', '1:101190', '1:101333', '1:101484', '1:101016', '1:101449', '1:101855', '1:94964', '1:104148', '1:98137', '1:102728', '1:101980', '1:31118', '1:23175', '1:20444', '1:25952', '1:39573', '1:45466', '1:27313', '1:41902', '1:49712', '1:49822', '1:13588', '1:13895', '1:13914', '1:14250', '1:14524', '1:14575', '1:14917', '1:15065', '1:14631', '1:14859', '1:27138', '1:51594', '1:51618', '1:51867', '1:15015', '1:15173', '1:15308', '1:15625', '1:15781', '1:17378', '1:19019', '1:59721', '1:61643', '1:25083', '1:42339', '1:42557', '1:42828', '1:64813', '1:75587', '1:77015', '1:79495', '1:79878', '1:96761', '1:86606', '1:86753', '1:89414', '1:90484', '1:90931', '1:91031', '1:95104', '1:91643', '1:87136', '1:87157', '1:91716', '1:87927', '1:96627', '1:84223', '1:85777', '1:87295', '1:95956', '1:86339', '1:90557', '1:94653', '1:101756', '1:101859', '1:106190', '1:102230', '1:104404', '1:104628', '1:104823', '1:101698', '1:102438', '1:102289', '1:4919', '1:5479', '1:4123', '1:9798', '1:54214', '1:58962', '1:59057', '1:7647', '1:8130', '1:8994', '1:30975', '1:41080', '1:41146', '1:32692', '1:32715', '1:32778', '1:8387', '1:9052', '1:9288', '1:26973', '1:27002', '1:27067', '1:27583', '1:1656', '1:15208', '1:26780', '1:31057', '1:31541', '1:29832', '1:17638', '1:42632', '1:70172', '1:70318', '1:18989', '1:32514', '1:41280', '1:41539', '1:39263', '1:30935', '1:39486', '1:51991', '1:54011', '1:45062', '1:45470', '1:52353', '1:62356', '1:57840', '1:76430', '1:77097', '1:77236', '1:104996', '1:24563', '1:24613', '1:82172', '1:83060', '1:85825', '1:85591', '1:96933', '1:97453', '1:79427', '1:77518', '1:78403', '1:79159', '1:78345', '1:81028', '1:82200', '1:87169', '1:5966', '1:6125', '1:6418', '1:6700', '1:7072', '1:7458', '1:40513', '1:40574', '1:40837', '1:40860', '1:52264', '1:52289', '1:52377', '1:52428', '1:58786', '1:58809', '1:22233', '1:22271', '1:22703', '1:22784', '1:22828', '1:22826', '1:22958', '1:29833', '1:27234', '1:27812', '1:82366', '1:82900', '1:82973', '1:84058', '1:47484', '1:44661', '1:43488', '1:47668', '1:47736', '1:47853', '1:21124', '1:26147', '1:26420', '1:31277', '1:25904', '1:66925', '1:103066', '1:82905', '1:86073', '1:87940', '1:95623', '1:106313', '1:106410', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6A721CBE-4B07-EA11-9750-0CC47A4D7646.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCF6B8AB-E003-EA11-AAE8-44A842BE8F7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9EAE1061-30F8-E911-B2D5-AC1F6B0F676C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/86727FE6-AF0A-EA11-B38D-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2A16734-8607-EA11-A7C2-0025905A6060.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/723E26E0-88FC-E911-A84F-0CC47AFCC666.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/643155F4-E80A-EA11-BD55-0CC47A7C3636.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC1243A5-AA0A-EA11-A2C9-0CC47A7C347A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24362999-4EFE-E911-BFEB-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1207CE62-4EF9-E911-85E0-C4346BC85718.root']);