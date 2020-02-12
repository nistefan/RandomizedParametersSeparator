import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:37762', '1:37760', '1:38731', '1:68186', '1:35189', '1:37140', '1:37537', '1:99729', '1:99909', '1:100677', '1:34305', '1:38517', '1:38537', '1:36305', '1:36601', '1:68851', '1:38196', '1:34871', '1:952', '1:35026', '1:887', '1:35708', '1:573', '1:586', '1:608', '1:620', '1:726', '1:662', '1:686', '1:688', '1:839', '1:846', '1:919', '1:632', '1:868', '1:923', '1:35037', '1:35052', '1:35089', '1:35342', '1:35408', '1:68353', '1:68354', '1:68387', '1:68400', '1:68483', '1:68791', '1:68093', '1:68345', '1:63753', '1:68187', '1:68208', '1:63937', '1:35579', '1:68842', '1:99950', '1:99959', '1:100616', '1:100631', '1:69269', '1:100019', '1:37479', '1:37491', '1:37492', '1:36565', '1:36579', '1:36703', '1:36743', '1:38654', '1:38632', '1:38122', '1:38134', '1:99535', '1:99555', '1:100026', '1:37818', '1:38432', '1:99259', '1:99270', '1:99271', '1:99872', '1:99471', '1:99479', '1:100742', '1:69246', '1:69452', '1:69484', '1:69491', '1:69467', '1:69799', '1:99310', '1:99435', '1:99448', '1:99941', '1:100231', '1:99706', '1:35154', '1:35207', '1:33216', '1:33218', '1:33367', '1:99129', '1:99137', '1:69855', '1:35443', '1:37034', '1:37054', '1:37065', '1:38958', '1:38976', '1:99863', '1:100277', '1:99948', '1:68168', '1:68316', '1:68321', '1:68669', '1:100183', '1:99820', '1:69709', '1:100419', '1:100467', '1:100472', '1:65', '1:50918', '1:100123', '1:34911', '1:35493', '1:35663', '1:100957', '1:63184', '1:100562', '1:100966', '1:271', '1:35246', '1:35502', '1:274', '1:38242', '1:68507', '1:37310', '1:69930', '1:68857', '1:63134', '1:276', '1:37868', '1:34485', '1:34659', '1:36059', '1:38267', '1:69592', '1:69925', '1:37577', '1:37822', '1:36084', '1:37098', '1:33985', '1:38582', '1:63492', '1:63547', '1:69630', '1:99842', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/A05C630A-A414-EA11-9CD6-782BCB46E733.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/58D79BB6-9510-EA11-8714-1458D04903A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C03879B3-5610-EA11-B93C-0CC47AFCC38A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/1E7F164B-1910-EA11-88A8-B496914563F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D2233004-2E11-EA11-AA1C-0CC47AFCC6AE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DABA196E-5E11-EA11-9819-A4BF01158AD8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/4E080BCF-4A0C-EA11-9123-EC0D9A8221EE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/6CA1E0B5-EF11-EA11-AD13-008CFAFC5E8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/589DF99F-9814-EA11-9949-F01FAFE5D17E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/6C700416-9514-EA11-B5E8-F01FAFD9C64C.root']);