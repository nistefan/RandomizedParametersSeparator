import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:14656', '1:15296', '1:42665', '1:91005', '1:92996', '1:94065', '1:96094', '1:97450', '1:96916', '1:72382', '1:72942', '1:47075', '1:24709', '1:17657', '1:17790', '1:18765', '1:102403', '1:43290', '1:56787', '1:67191', '1:65100', '1:90220', '1:83375', '1:83916', '1:84185', '1:84436', '1:18599', '1:22201', '1:44809', '1:44836', '1:64764', '1:75249', '1:81548', '1:80701', '1:66470', '1:72246', '1:97672', '1:24308', '1:20312', '1:20472', '1:20478', '1:20490', '1:20565', '1:52227', '1:24829', '1:24891', '1:24910', '1:24988', '1:25687', '1:47381', '1:73179', '1:74047', '1:74781', '1:76895', '1:67937', '1:77068', '1:78069', '1:70030', '1:70070', '1:77868', '1:84296', '1:77704', '1:73019', '1:97317', '1:87414', '1:23478', '1:23673', '1:31145', '1:71957', '1:12156', '1:12812', '1:16376', '1:101722', '1:102266', '1:67850', '1:18222', '1:18234', '1:18420', '1:30687', '1:39358', '1:44154', '1:44953', '1:24995', '1:25017', '1:25385', '1:2989', '1:11255', '1:30004', '1:30142', '1:30245', '1:42733', '1:92417', '1:98733', '1:98791', '1:83057', '1:91956', '1:92201', '1:92367', '1:94606', '1:47499', '1:47566', '1:48284', '1:48397', '1:71868', '1:74944', '1:72765', '1:84490', '1:85763', '1:86182', '1:52034', '1:64913', '1:65309', '1:65617', '1:65782', '1:96037', '1:104286', '1:44475', '1:30213', '1:98442', '1:87875', '1:88226', '1:88477', '1:89265', '1:89269', '1:96663', '1:91222', '1:91247', '1:28629', '1:43355', '1:45411', '1:105946', '1:106268', '1:96260', '1:105962', '1:106162', '1:106250', '1:101791', '1:101295', '1:5775', '1:5264', '1:5800', '1:5925', '1:7515', '1:7204', '1:8097', '1:72518', '1:81147', '1:94141', '1:20571', '1:20701', '1:20833', '1:20926', '1:24555', '1:102508', '1:53499', '1:62034', '1:5575', '1:5931', '1:6091', '1:9966', '1:10109', '1:9608', '1:9900', '1:10377', '1:11867', '1:12733', '1:14661', '1:7764', '1:8595', '1:9831', '1:11606', '1:16358', '1:16391', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C75EAD7-A60A-EA11-B2EA-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CAA33E3-B40A-EA11-B217-0CC47A4C8EB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0C7BD80-B30A-EA11-990C-0CC47A7C345E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/827A94E9-460C-EA11-9197-0CC47A7C34D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C25D68E-CA0A-EA11-A4D3-0CC47A4D762E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4F23B9-260F-EA11-80C3-0CC47A4D7690.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A38857F-43F9-E911-9334-0CC47A5FBE21.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2A529D76-BC12-EA11-85B1-90B11C070100.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80404779-FBF6-E911-8982-AC1F6B0F71D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A13F5EF-28F2-E911-9B0D-00215AA64960.root']);