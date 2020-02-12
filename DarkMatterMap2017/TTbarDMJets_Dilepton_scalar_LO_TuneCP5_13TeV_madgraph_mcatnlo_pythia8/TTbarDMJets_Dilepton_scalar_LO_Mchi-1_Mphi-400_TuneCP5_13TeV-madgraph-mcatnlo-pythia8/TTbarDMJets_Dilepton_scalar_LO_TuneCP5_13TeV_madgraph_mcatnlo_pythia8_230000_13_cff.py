import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:20394', '1:19190', '1:20803', '1:62372', '1:62017', '1:63286', '1:63883', '1:58711', '1:54432', '1:55402', '1:55699', '1:71024', '1:72912', '1:74279', '1:72304', '1:72313', '1:72904', '1:77388', '1:81940', '1:78042', '1:78931', '1:79402', '1:79534', '1:71135', '1:71492', '1:80320', '1:78478', '1:79025', '1:76319', '1:78019', '1:78616', '1:81777', '1:100932', '1:103020', '1:105128', '1:105193', '1:105400', '1:105441', '1:82811', '1:82904', '1:82906', '1:83331', '1:84136', '1:84147', '1:94450', '1:94871', '1:94996', '1:104174', '1:105483', '1:103913', '1:69818', '1:69828', '1:69896', '1:69909', '1:69916', '1:69942', '1:69980', '1:94781', '1:86682', '1:93374', '1:70240', '1:74434', '1:74440', '1:74075', '1:74093', '1:74153', '1:74030', '1:74046', '1:74080', '1:74154', '1:74135', '1:74261', '1:74272', '1:92443', '1:92459', '1:92817', '1:1123', '1:1271', '1:1299', '1:1300', '1:1329', '1:1376', '1:14018', '1:14054', '1:14531', '1:14569', '1:14597', '1:14627', '1:15111', '1:16483', '1:16677', '1:16955', '1:19306', '1:19562', '1:20047', '1:41850', '1:48637', '1:17870', '1:18312', '1:18331', '1:18439', '1:37784', '1:35539', '1:35612', '1:42249', '1:42323', '1:42361', '1:41755', '1:48077', '1:49494', '1:49957', '1:48313', '1:51069', '1:53334', '1:54760', '1:58654', '1:55522', '1:59632', '1:66735', '1:65250', '1:66027', '1:61199', '1:99705', '1:27809', '1:39016', '1:39376', '1:39201', '1:39231', '1:39651', '1:44697', '1:46331', '1:46086', '1:46264', '1:46365', '1:46072', '1:75043', '1:76472', '1:77016', '1:81018', '1:80760', '1:82154', '1:79824', '1:84781', '1:75805', '1:75927', '1:77253', '1:77304', '1:77358', '1:77390', '1:77593', '1:49096', '1:46355', '1:47862', '1:40566', '1:47131', '1:59620', '1:61357', '1:62180', '1:62169', '1:68895', '1:68944', '1:38803', '1:42606', '1:53019', '1:54886', '1:57555', '1:58660', '1:55569', '1:55587', '1:57679', '1:57231', '1:57602', '1:57974', '1:57780', '1:63728', '1:8688', '1:8766', '1:9917', '1:74828', '1:98378', '1:98387', '1:98670', '1:98742', '1:7089', '1:8762', '1:10936', '1:12002', '1:21362', '1:21367', '1:21421', '1:21450', '1:21708', '1:61017', '1:63833', '1:67281', '1:68444', '1:68657', '1:69972', '1:32761', '1:35022', '1:37097', '1:39659', '1:44658', '1:45001', '1:45403', '1:47168', '1:100237', '1:100375', '1:53367', '1:55545', '1:58024', '1:54232', '1:85681', '1:87374', '1:68581', '1:69110', '1:96961', '1:99415', '1:105942', '1:106205', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/922D5DD5-5710-EA11-BE57-AC1F6B595F4E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/58A27CA1-A5F6-E911-8978-0CC47A2B0744.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D6BD0C1E-CCF7-E911-9152-AC1F6B567730.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F030EDC5-1AF3-E911-9B33-002590DE6E6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/82662A5E-23EE-E911-8D5B-0CC47A7FC74A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/54235082-12F4-E911-A7A0-0CC47A1E0DCC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C924ADE-C9EE-E911-8597-C4544423E320.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/120CCF0F-55EF-E911-94EA-24BE05C48821.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5072FB7D-5910-EA11-81FB-28924A33B9FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/629E6C83-AC0D-EA11-83C5-0CC47A5FBE25.root']);