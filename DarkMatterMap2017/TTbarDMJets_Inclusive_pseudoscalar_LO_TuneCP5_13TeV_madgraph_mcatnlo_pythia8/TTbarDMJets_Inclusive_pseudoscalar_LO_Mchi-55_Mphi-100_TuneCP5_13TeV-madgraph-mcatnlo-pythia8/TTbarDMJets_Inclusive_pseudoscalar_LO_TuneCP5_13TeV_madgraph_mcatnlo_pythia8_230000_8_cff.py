import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8564', '1:8694', '1:10355', '1:9475', '1:11019', '1:11304', '1:12678', '1:20269', '1:20382', '1:20910', '1:20925', '1:44425', '1:78415', '1:25971', '1:23025', '1:29912', '1:32324', '1:90467', '1:93721', '1:93581', '1:94741', '1:93103', '1:82829', '1:87684', '1:65244', '1:74616', '1:85118', '1:84895', '1:28116', '1:23855', '1:29197', '1:81824', '1:85720', '1:92021', '1:92169', '1:102033', '1:102651', '1:8844', '1:10883', '1:39537', '1:47986', '1:49928', '1:11003', '1:15210', '1:3437', '1:4895', '1:8040', '1:8240', '1:8265', '1:8730', '1:12801', '1:48834', '1:49938', '1:32347', '1:32541', '1:66402', '1:66815', '1:67368', '1:67603', '1:32951', '1:62405', '1:64369', '1:74417', '1:8561', '1:9526', '1:10304', '1:13617', '1:10663', '1:62980', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78CEA8C6-3B04-EA11-A932-001E677925A0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0A05A38F-FD06-EA11-9A80-AC1F6B0DE3A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2226C86C-BD06-EA11-AD47-AC1F6B0DE296.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DCA075CC-F207-EA11-8401-48FD8EE73A81.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E32F162-BC12-EA11-946E-008CFAFD5234.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B80D0F07-BC12-EA11-9A6B-A4BF0112BC04.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/08A1C493-AF12-EA11-9AED-485B39897242.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60EDCC5C-BC12-EA11-91E4-0CC47A7034D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C94C93E-BC12-EA11-8B7E-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/32FA8D58-BC12-EA11-885A-6C2B599934B5.root']);