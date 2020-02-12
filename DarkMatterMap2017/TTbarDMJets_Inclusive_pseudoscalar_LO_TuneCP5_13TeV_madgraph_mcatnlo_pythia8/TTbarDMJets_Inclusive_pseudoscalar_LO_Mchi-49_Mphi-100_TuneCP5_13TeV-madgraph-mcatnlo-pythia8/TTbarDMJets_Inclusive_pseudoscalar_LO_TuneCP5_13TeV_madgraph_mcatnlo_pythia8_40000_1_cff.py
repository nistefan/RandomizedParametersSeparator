import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:81', '1:768', '1:37796', '1:34631', '1:37746', '1:50435', '1:69553', '1:100213', '1:100648', '1:69690', '1:100139', '1:100179', '1:100283', '1:34466', '1:63531', '1:34394', '1:37349', '1:38167', '1:34668', '1:63111', '1:38187', '1:38263', '1:299', '1:872', '1:35119', '1:35709', '1:35932', '1:558', '1:713', '1:715', '1:706', '1:809', '1:816', '1:835', '1:821', '1:927', '1:35085', '1:68379', '1:68733', '1:68982', '1:68328', '1:68677', '1:100814', '1:100877', '1:697', '1:63637', '1:63725', '1:50422', '1:68966', '1:38016', '1:68180', '1:63901', '1:37909', '1:37976', '1:37485', '1:36563', '1:36778', '1:38631', '1:99551', '1:37601', '1:37714', '1:37724', '1:38435', '1:38468', '1:69873', '1:69882', '1:69904', '1:99099', '1:99135', '1:69823', '1:99257', '1:99478', '1:99497', '1:99870', '1:69176', '1:69522', '1:69244', '1:69417', '1:99526', '1:488', '1:35024', '1:33210', '1:37287', '1:99116', '1:99122', '1:34933', '1:35435', '1:37047', '1:37064', '1:68411', '1:68447', '1:38873', '1:38970', '1:38971', '1:50937', '1:99656', '1:99988', '1:99989', '1:38225', '1:68279', '1:99824', '1:100647', '1:100441', '1:100842', '1:34', '1:51', '1:70', '1:50950', '1:100125', '1:37106', '1:35413', '1:35604', '1:100956', '1:36351', '1:37331', '1:37825', '1:100079', '1:100086', '1:100152', '1:100199', '1:63140', '1:63550', '1:69018', '1:69906', '1:36973', '1:38214', '1:38216', '1:68867', '1:36654', '1:38577', '1:38588', '1:50406', '1:63334', '1:35778', '1:33684', '1:34342', '1:34673', '1:34872', '1:34846', '1:36074', '1:38284', '1:63121', '1:69587', '1:69664', '1:35211', '1:35749', '1:34300', '1:34355', '1:34500', '1:35735', '1:36002', '1:36019', '1:37174', '1:34319', '1:37346', '1:37407', '1:34387', '1:34398', '1:34649', '1:34670', '1:36310', '1:36536', '1:38159', '1:34654', '1:36309', '1:36611', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/A05C630A-A414-EA11-9CD6-782BCB46E733.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/58D79BB6-9510-EA11-8714-1458D04903A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C03879B3-5610-EA11-B93C-0CC47AFCC38A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/1E7F164B-1910-EA11-88A8-B496914563F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D2233004-2E11-EA11-AA1C-0CC47AFCC6AE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DABA196E-5E11-EA11-9819-A4BF01158AD8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/4E080BCF-4A0C-EA11-9123-EC0D9A8221EE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/6CA1E0B5-EF11-EA11-AD13-008CFAFC5E8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/589DF99F-9814-EA11-9949-F01FAFE5D17E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/6C700416-9514-EA11-B5E8-F01FAFD9C64C.root']);