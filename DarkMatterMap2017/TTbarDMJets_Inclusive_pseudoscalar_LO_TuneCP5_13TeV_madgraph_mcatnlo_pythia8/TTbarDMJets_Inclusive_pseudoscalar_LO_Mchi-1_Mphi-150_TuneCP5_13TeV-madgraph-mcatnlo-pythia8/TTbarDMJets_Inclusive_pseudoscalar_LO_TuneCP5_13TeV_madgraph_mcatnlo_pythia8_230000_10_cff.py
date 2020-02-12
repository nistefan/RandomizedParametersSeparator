import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:14682', '1:15059', '1:15083', '1:42602', '1:94069', '1:94154', '1:98847', '1:64434', '1:67041', '1:19524', '1:26207', '1:23789', '1:17936', '1:19115', '1:19215', '1:19492', '1:44740', '1:65500', '1:67499', '1:72740', '1:83450', '1:83534', '1:87043', '1:27245', '1:28797', '1:47389', '1:64061', '1:73090', '1:52926', '1:74118', '1:78476', '1:20377', '1:20397', '1:20502', '1:20741', '1:20814', '1:20869', '1:24737', '1:24887', '1:25699', '1:25738', '1:47367', '1:47681', '1:65927', '1:70848', '1:70485', '1:70721', '1:77269', '1:77682', '1:70673', '1:93622', '1:20157', '1:21604', '1:23385', '1:75337', '1:8632', '1:8957', '1:101130', '1:64056', '1:65677', '1:66375', '1:47861', '1:28094', '1:44061', '1:24983', '1:25439', '1:25454', '1:4237', '1:18469', '1:32028', '1:32333', '1:103555', '1:82298', '1:82491', '1:83335', '1:91550', '1:91481', '1:91517', '1:93089', '1:47888', '1:47969', '1:83520', '1:71025', '1:67811', '1:72708', '1:84143', '1:84401', '1:87557', '1:51967', '1:52078', '1:52105', '1:52109', '1:52386', '1:52457', '1:54912', '1:70426', '1:65514', '1:82053', '1:97356', '1:97500', '1:102734', '1:104492', '1:30522', '1:42466', '1:29867', '1:47252', '1:98303', '1:98304', '1:88608', '1:89523', '1:91232', '1:88785', '1:88794', '1:46178', '1:29567', '1:93910', '1:105415', '1:82303', '1:97392', '1:98293', '1:105272', '1:101224', '1:5837', '1:8049', '1:7256', '1:7516', '1:8119', '1:64352', '1:62655', '1:62837', '1:82017', '1:62392', '1:104420', '1:104401', '1:57299', '1:62821', '1:5956', '1:5964', '1:6294', '1:10133', '1:13332', '1:7253', '1:16325', '1:16617', '1:14838', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C75EAD7-A60A-EA11-B2EA-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CAA33E3-B40A-EA11-B217-0CC47A4C8EB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0C7BD80-B30A-EA11-990C-0CC47A7C345E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/827A94E9-460C-EA11-9197-0CC47A7C34D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C25D68E-CA0A-EA11-A4D3-0CC47A4D762E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4F23B9-260F-EA11-80C3-0CC47A4D7690.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A38857F-43F9-E911-9334-0CC47A5FBE21.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2A529D76-BC12-EA11-85B1-90B11C070100.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80404779-FBF6-E911-8982-AC1F6B0F71D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A13F5EF-28F2-E911-9B0D-00215AA64960.root']);