import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8678', '1:11099', '1:8565', '1:8576', '1:8656', '1:9387', '1:11260', '1:11301', '1:11497', '1:11529', '1:11281', '1:11699', '1:12291', '1:14096', '1:19379', '1:19525', '1:20015', '1:20024', '1:20081', '1:20088', '1:20112', '1:20399', '1:20752', '1:20902', '1:28750', '1:28350', '1:32416', '1:66725', '1:77954', '1:79636', '1:80163', '1:80545', '1:42863', '1:21996', '1:44660', '1:47099', '1:27973', '1:29222', '1:30693', '1:30899', '1:32977', '1:29872', '1:30040', '1:32146', '1:32150', '1:32192', '1:44333', '1:77703', '1:77785', '1:82923', '1:84473', '1:84495', '1:85306', '1:88611', '1:78731', '1:78944', '1:95090', '1:95129', '1:95421', '1:83073', '1:87296', '1:81868', '1:84908', '1:85344', '1:70965', '1:82701', '1:89350', '1:89618', '1:90162', '1:90496', '1:65512', '1:65901', '1:67947', '1:74730', '1:41714', '1:76239', '1:77022', '1:81901', '1:90109', '1:90920', '1:89449', '1:27824', '1:28486', '1:28488', '1:29873', '1:30138', '1:30510', '1:20819', '1:24041', '1:25005', '1:65279', '1:73334', '1:79035', '1:79243', '1:79588', '1:80325', '1:72823', '1:80555', '1:81325', '1:81821', '1:70192', '1:82271', '1:82597', '1:82750', '1:83039', '1:86615', '1:83363', '1:83532', '1:84240', '1:88881', '1:89793', '1:91275', '1:102873', '1:101750', '1:102179', '1:102180', '1:102449', '1:102537', '1:102595', '1:102841', '1:102864', '1:102082', '1:102089', '1:102097', '1:102153', '1:102199', '1:102206', '1:102457', '1:6011', '1:1948', '1:4071', '1:8517', '1:8734', '1:9368', '1:9606', '1:9830', '1:10011', '1:12248', '1:12337', '1:28128', '1:28793', '1:29513', '1:29908', '1:30067', '1:30877', '1:42654', '1:44017', '1:44454', '1:45690', '1:45787', '1:47862', '1:49622', '1:52831', '1:53522', '1:54032', '1:54163', '1:55320', '1:28732', '1:64688', '1:66140', '1:65181', '1:65317', '1:65439', '1:73024', '1:73635', '1:72922', '1:76261', '1:45353', '1:52336', '1:54990', '1:57135', '1:57209', '1:59561', '1:59577', '1:59642', '1:56272', '1:57802', '1:59754', '1:60275', '1:61641', '1:62037', '1:70093', '1:104580', '1:1267', '1:5758', '1:15713', '1:1624', '1:8127', '1:11327', '1:13977', '1:14083', '1:16419', '1:101868', '1:102373', '1:102496', '1:104056', '1:104117', '1:8297', '1:8321', '1:8356', '1:8611', '1:8743', '1:8823', '1:8866', '1:8346', '1:8449', '1:8483', '1:8596', '1:11654', '1:40843', '1:41066', '1:41513', '1:48179', '1:48440', '1:48885', '1:49190', '1:49213', '1:51265', '1:51859', '1:32424', '1:32281', '1:32220', '1:32313', '1:32495', '1:32235', '1:32241', '1:32248', '1:32450', '1:32482', '1:66404', '1:66426', '1:66647', '1:66776', '1:66987', '1:67052', '1:67741', '1:67756', '1:67781', '1:55228', '1:60620', '1:57157', '1:61407', '1:62716', '1:65345', '1:66410', '1:66733', '1:67107', '1:73823', '1:65046', '1:76185', '1:86407', '1:8041', '1:8432', '1:8440', '1:8675', '1:8895', '1:8959', '1:10442', '1:10515', '1:8948', '1:10891', '1:10930', '1:10959', '1:14203', '1:14466', '1:15199', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78CEA8C6-3B04-EA11-A932-001E677925A0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0A05A38F-FD06-EA11-9A80-AC1F6B0DE3A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2226C86C-BD06-EA11-AD47-AC1F6B0DE296.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DCA075CC-F207-EA11-8401-48FD8EE73A81.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E32F162-BC12-EA11-946E-008CFAFD5234.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B80D0F07-BC12-EA11-9A6B-A4BF0112BC04.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/08A1C493-AF12-EA11-9AED-485B39897242.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60EDCC5C-BC12-EA11-91E4-0CC47A7034D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C94C93E-BC12-EA11-8B7E-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/32FA8D58-BC12-EA11-885A-6C2B599934B5.root']);