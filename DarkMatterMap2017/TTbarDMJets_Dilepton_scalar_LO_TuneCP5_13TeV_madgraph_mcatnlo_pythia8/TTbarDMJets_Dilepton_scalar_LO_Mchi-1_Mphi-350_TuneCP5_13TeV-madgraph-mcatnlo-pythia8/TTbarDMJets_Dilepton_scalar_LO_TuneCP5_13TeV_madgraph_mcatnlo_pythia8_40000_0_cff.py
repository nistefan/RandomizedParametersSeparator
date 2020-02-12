import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11741', '1:11848', '1:13615', '1:13630', '1:13195', '1:13277', '1:13381', '1:13397', '1:13454', '1:13443', '1:13448', '1:13709', '1:13710', '1:13763', '1:13766', '1:13901', '1:13965', '1:13962', '1:13436', '1:25471', '1:25675', '1:25885', '1:25730', '1:25756', '1:25801', '1:29273', '1:29276', '1:29301', '1:29423', '1:29445', '1:29558', '1:30073', '1:30113', '1:31115', '1:30137', '1:30150', '1:11525', '1:13146', '1:13177', '1:22041', '1:22043', '1:25143', '1:25932', '1:25405', '1:30177', '1:29569', '1:29591', '1:29608', '1:30261', '1:30374', '1:30625', '1:31429', '1:31905', '1:31490', '1:31492', '1:31466', '1:31927', '1:31662', '1:31674', '1:90045', '1:101275', '1:101310', '1:101334', '1:22092', '1:13848', '1:13904', '1:13913', '1:22054', '1:22125', '1:89712', '1:101026', '1:22573', '1:101325', '1:101362', '1:101297', '1:101366', '1:101387', '1:89914', '1:89952', '1:89966', '1:90007', '1:90645', '1:31126', '1:31170', '1:90737', '1:90781', '1:25215', '1:25410', '1:89611', '1:89617', '1:89622', '1:89869', '1:89553', '1:90557', '1:29229', '1:29231', '1:29252', '1:29297', '1:29302', '1:29306', '1:25594', '1:29160', '1:89596', '1:89947', '1:90037', '1:90155', '1:90166', '1:101415', '1:101427', '1:90450', '1:90460', '1:90525', '1:29364', '1:29328', '1:29904', '1:29956', '1:30025', '1:30126', '1:31764', '1:31587', '1:31602', '1:31629', '1:31671', '1:11006', '1:11432', '1:13097', '1:13243', '1:13634', '1:13649', '1:13570', '1:13730', '1:22178', '1:11468', '1:11871', '1:13544', '1:13548', '1:22212', '1:22981', '1:31361', '1:89330', '1:89684', '1:89825', '1:90351', '1:30355', '1:89029', '1:89069', '1:89072', '1:89108', '1:89491', '1:89695', '1:89280', '1:89373', '1:89375', '1:89676', '1:89706', '1:89821', '1:89837', '1:89838', '1:89255', '1:89296', '1:101144', '1:89993', '1:11211', '1:11372', '1:13028', '1:25600', '1:13900', '1:22179', '1:22979', '1:25837', '1:29464', '1:30958', '1:31821', '1:89364', '1:101441', '1:22174', '1:22183', '1:25272', '1:25868', '1:25695', '1:29164', '1:29180', '1:89345', '1:30501', '1:31816', '1:31863', '1:31868', '1:101484', '1:90392', '1:90973', '1:101594', '1:90320', '1:101547', '1:89292', '1:101390', '1:101540', '1:101560', '1:89649', '1:11575', '1:11593', '1:11635', '1:11191', '1:11711', '1:11782', '1:11763', '1:11671', '1:11685', '1:11691', '1:11716', '1:11719', '1:11720', '1:11838', '1:22564', '1:22607', '1:22623', '1:22662', '1:22681', '1:22741', '1:22004', '1:22502', '1:22508', '1:11112', '1:11566', '1:11607', '1:11169', '1:11232', '1:13006', '1:13058', '1:13067', '1:13537', '1:13072', '1:13292', '1:13199', '1:13425', '1:13701', '1:13911', '1:25595', '1:30810', '1:31279', '1:31301', '1:31303', '1:31405', '1:101024', '1:89974', '1:89976', '1:101049', '1:101336', '1:101087', '1:101186', '1:101261', '1:90806', '1:90909', '1:90914', '1:90904', '1:90922', '1:90929', '1:90993', '1:90994', '1:90935', '1:22098', '1:22107', '1:22113', '1:22148', '1:22438', '1:25599', '1:25629', '1:25638', '1:25711', '1:25729', '1:25740', '1:29123', '1:29443', '1:29453', '1:29472', '1:29501', '1:29614', '1:29620', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/BA08AC92-32EF-E911-82D8-441EA1616DEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/1A47AC00-7B03-EA11-9EE6-0CC47AF973C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DA862DF2-9F11-EA11-A5FB-C4346BC75558.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DC992538-9910-EA11-BF7F-0CC47A5FC281.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/163497F8-2D11-EA11-A132-6C2B599A050D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/0A3BC253-8411-EA11-A6F0-D8D385AF891A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/562C1852-3411-EA11-A53F-8CDCD4A9A484.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/E6105D38-A311-EA11-9524-0CC47A7E6A5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D86A4CB2-9014-EA11-8CA9-F01FAFE5CF52.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C0549F53-A714-EA11-8560-782BCB46E733.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/70D29667-41FB-E911-818C-38EAA78D8ACC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/B8C911EE-29F0-E911-8638-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/0E7BC3B3-0AFA-E911-8213-98039B3B01B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DE54B8C9-DA10-EA11-89A8-A4BF01125538.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/2ABD4E37-8F03-EA11-815A-1866DA86CCDF.root']);