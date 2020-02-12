import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:37703', '1:37704', '1:37782', '1:35739', '1:100161', '1:100538', '1:100652', '1:100206', '1:100102', '1:100180', '1:100532', '1:161', '1:254', '1:34183', '1:37365', '1:36359', '1:38219', '1:38589', '1:38270', '1:63498', '1:38279', '1:38282', '1:36012', '1:35012', '1:35044', '1:35048', '1:35088', '1:35109', '1:479', '1:505', '1:562', '1:569', '1:582', '1:585', '1:591', '1:600', '1:614', '1:702', '1:707', '1:716', '1:823', '1:841', '1:856', '1:629', '1:818', '1:35090', '1:35574', '1:35605', '1:35635', '1:68985', '1:100874', '1:100800', '1:63749', '1:38799', '1:68227', '1:63031', '1:99961', '1:99963', '1:69267', '1:34522', '1:37467', '1:36271', '1:36282', '1:36303', '1:36477', '1:36693', '1:36705', '1:36719', '1:36574', '1:36781', '1:36948', '1:38648', '1:38707', '1:38758', '1:100995', '1:69647', '1:37597', '1:37715', '1:37917', '1:99170', '1:99092', '1:99282', '1:100380', '1:99882', '1:69293', '1:69348', '1:69374', '1:69391', '1:69544', '1:99700', '1:100', '1:35233', '1:33233', '1:33240', '1:37150', '1:69804', '1:99158', '1:69826', '1:69840', '1:69847', '1:68437', '1:68467', '1:38843', '1:38866', '1:99761', '1:99874', '1:99966', '1:37785', '1:68176', '1:68646', '1:68699', '1:69009', '1:99212', '1:69582', '1:69670', '1:99920', '1:69996', '1:100457', '1:34195', '1:50694', '1:35548', '1:35606', '1:35626', '1:35807', '1:35821', '1:34887', '1:63161', '1:100501', '1:36409', '1:201', '1:35245', '1:137', '1:164', '1:35158', '1:35219', '1:37306', '1:37870', '1:100540', '1:63133', '1:63139', '1:63307', '1:69924', '1:38095', '1:34675', '1:36663', '1:36671', '1:36660', '1:38574', '1:50015', '1:63226', '1:259', '1:34513', '1:36328', '1:36067', '1:38170', '1:63125', '1:69058', '1:69061', '1:69066', '1:35178', '1:37360', '1:34373', '1:35854', '1:36032', '1:36070', '1:34321', '1:34483', '1:36669', '1:37083', '1:33616', '1:38252', '1:100624', '1:69631', '1:100192', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/A05C630A-A414-EA11-9CD6-782BCB46E733.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/58D79BB6-9510-EA11-8714-1458D04903A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C03879B3-5610-EA11-B93C-0CC47AFCC38A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/1E7F164B-1910-EA11-88A8-B496914563F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D2233004-2E11-EA11-AA1C-0CC47AFCC6AE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DABA196E-5E11-EA11-9819-A4BF01158AD8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/4E080BCF-4A0C-EA11-9123-EC0D9A8221EE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/6CA1E0B5-EF11-EA11-AD13-008CFAFC5E8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/589DF99F-9814-EA11-9949-F01FAFE5D17E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/6C700416-9514-EA11-B5E8-F01FAFD9C64C.root']);