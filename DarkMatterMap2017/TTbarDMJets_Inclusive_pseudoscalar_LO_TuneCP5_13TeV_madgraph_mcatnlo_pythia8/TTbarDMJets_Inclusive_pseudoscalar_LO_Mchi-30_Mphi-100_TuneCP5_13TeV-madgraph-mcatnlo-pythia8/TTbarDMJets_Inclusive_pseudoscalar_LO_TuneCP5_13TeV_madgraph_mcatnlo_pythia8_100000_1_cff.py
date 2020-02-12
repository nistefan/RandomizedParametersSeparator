import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:36724', '1:37654', '1:48471', '1:48764', '1:49237', '1:49256', '1:78739', '1:92840', '1:86041', '1:48767', '1:61513', '1:74044', '1:72516', '1:84122', '1:84417', '1:72833', '1:74526', '1:74625', '1:89532', '1:89653', '1:66536', '1:66810', '1:67020', '1:72078', '1:74731', '1:74657', '1:78017', '1:95426', '1:69197', '1:69173', '1:94685', '1:76172', '1:84404', '1:84847', '1:95452', '1:90494', '1:21599', '1:24464', '1:24686', '1:18791', '1:19693', '1:22096', '1:72102', '1:11872', '1:12059', '1:12849', '1:77784', '1:77881', '1:82138', '1:75890', '1:77404', '1:82512', '1:73869', '1:75079', '1:70398', '1:70947', '1:77043', '1:95015', '1:95159', '1:3253', '1:3763', '1:3784', '1:5787', '1:9295', '1:9659', '1:6288', '1:2329', '1:8020', '1:12232', '1:7968', '1:10760', '1:70771', '1:95052', '1:95075', '1:70797', '1:77510', '1:77835', '1:82113', '1:34775', '1:34756', '1:38441', '1:64231', '1:64359', '1:64498', '1:65081', '1:63854', '1:70295', '1:77102', '1:35204', '1:35210', '1:34371', '1:34388', '1:34044', '1:37565', '1:21516', '1:101271', '1:105023', '1:105037', '1:93786', '1:95362', '1:81113', '1:89322', '1:92938', '1:94375', '1:104403', '1:92780', '1:92920', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/96FE5273-B319-EA11-956A-002590491B22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/AE0B1823-231A-EA11-8338-44A8421274BD.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/DE7C9112-8319-EA11-8C22-24BE05C4D801.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/E6E5485B-E81A-EA11-8DC1-EC0D9A8221DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/A0C03570-4E19-EA11-8016-A0369FC5E090.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/3CAE5ACB-E81A-EA11-8693-008CFA0A565C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/C807253F-E81A-EA11-AD61-AC1F6B34A744.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/5442FE0E-A719-EA11-8D98-0CC47A2B04A6.root']);