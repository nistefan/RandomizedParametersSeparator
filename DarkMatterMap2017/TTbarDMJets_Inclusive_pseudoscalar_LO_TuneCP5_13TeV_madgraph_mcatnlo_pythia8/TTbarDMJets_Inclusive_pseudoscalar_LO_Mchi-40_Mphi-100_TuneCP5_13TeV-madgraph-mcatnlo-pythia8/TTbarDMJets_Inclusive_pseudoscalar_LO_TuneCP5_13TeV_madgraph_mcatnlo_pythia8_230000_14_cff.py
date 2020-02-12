import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:46698', '1:82248', '1:85689', '1:95571', '1:101001', '1:101334', '1:97130', '1:95099', '1:101549', '1:101905', '1:104758', '1:104886', '1:104727', '1:101367', '1:101851', '1:2041', '1:7175', '1:18182', '1:45846', '1:42492', '1:44657', '1:104581', '1:42045', '1:53653', '1:13700', '1:14268', '1:14734', '1:14812', '1:14981', '1:51741', '1:55178', '1:14845', '1:15593', '1:19097', '1:19243', '1:19667', '1:52797', '1:53130', '1:62185', '1:42721', '1:42599', '1:42647', '1:42941', '1:44594', '1:60941', '1:79857', '1:54792', '1:102147', '1:86898', '1:86674', '1:86921', '1:86536', '1:91144', '1:88700', '1:89046', '1:89309', '1:91170', '1:91369', '1:91443', '1:91936', '1:86174', '1:93921', '1:96931', '1:86002', '1:86831', '1:87389', '1:104544', '1:101599', '1:102376', '1:1772', '1:1920', '1:1952', '1:7600', '1:8137', '1:52974', '1:52988', '1:53373', '1:53747', '1:54237', '1:59558', '1:7901', '1:8170', '1:8187', '1:8534', '1:8616', '1:8786', '1:8876', '1:22564', '1:30157', '1:32611', '1:32698', '1:32757', '1:8568', '1:8630', '1:9348', '1:18739', '1:27276', '1:27180', '1:27424', '1:27437', '1:26524', '1:26920', '1:9952', '1:8401', '1:29986', '1:30995', '1:32079', '1:39668', '1:39718', '1:39727', '1:80620', '1:39652', '1:42953', '1:43847', '1:39503', '1:45354', '1:62615', '1:57849', '1:62518', '1:60983', '1:70750', '1:70763', '1:70833', '1:77089', '1:77093', '1:77122', '1:77142', '1:97666', '1:101849', '1:104860', '1:24570', '1:24712', '1:24790', '1:24906', '1:24999', '1:70514', '1:85949', '1:77221', '1:83117', '1:84703', '1:72029', '1:78034', '1:81854', '1:88052', '1:75818', '1:79584', '1:77674', '1:77691', '1:77968', '1:77969', '1:82212', '1:6157', '1:6502', '1:40738', '1:40566', '1:40724', '1:40792', '1:52368', '1:58645', '1:58669', '1:58835', '1:58888', '1:22481', '1:22687', '1:22924', '1:22948', '1:27498', '1:27513', '1:27820', '1:82598', '1:40679', '1:54057', '1:43262', '1:46183', '1:49718', '1:58387', '1:43434', '1:43875', '1:43918', '1:44185', '1:47633', '1:14606', '1:88555', '1:98390', '1:105880', '1:106042', '1:106206', '1:106214', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6A721CBE-4B07-EA11-9750-0CC47A4D7646.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCF6B8AB-E003-EA11-AAE8-44A842BE8F7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9EAE1061-30F8-E911-B2D5-AC1F6B0F676C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/86727FE6-AF0A-EA11-B38D-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2A16734-8607-EA11-A7C2-0025905A6060.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/723E26E0-88FC-E911-A84F-0CC47AFCC666.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/643155F4-E80A-EA11-BD55-0CC47A7C3636.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC1243A5-AA0A-EA11-A2C9-0CC47A7C347A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24362999-4EFE-E911-BFEB-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1207CE62-4EF9-E911-85E0-C4346BC85718.root']);