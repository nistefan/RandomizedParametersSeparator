import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:9810', '1:10570', '1:11223', '1:13127', '1:13278', '1:19051', '1:20999', '1:39743', '1:44432', '1:81454', '1:32355', '1:44191', '1:93769', '1:86021', '1:84128', '1:85538', '1:71031', '1:92366', '1:70882', '1:28706', '1:25123', '1:82792', '1:85196', '1:86128', '1:87076', '1:89912', '1:91278', '1:91743', '1:102068', '1:102340', '1:102744', '1:102077', '1:102227', '1:12999', '1:10124', '1:12321', '1:47978', '1:40981', '1:66203', '1:52070', '1:58973', '1:65098', '1:71897', '1:78810', '1:89146', '1:6133', '1:7142', '1:101482', '1:8765', '1:27249', '1:41202', '1:51067', '1:32532', '1:32517', '1:66546', '1:67060', '1:67641', '1:18242', '1:67203', '1:65290', '1:79343', '1:70274', '1:8505', '1:8619', '1:9063', '1:10920', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78CEA8C6-3B04-EA11-A932-001E677925A0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0A05A38F-FD06-EA11-9A80-AC1F6B0DE3A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2226C86C-BD06-EA11-AD47-AC1F6B0DE296.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DCA075CC-F207-EA11-8401-48FD8EE73A81.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E32F162-BC12-EA11-946E-008CFAFD5234.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B80D0F07-BC12-EA11-9A6B-A4BF0112BC04.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/08A1C493-AF12-EA11-9AED-485B39897242.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60EDCC5C-BC12-EA11-91E4-0CC47A7034D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C94C93E-BC12-EA11-8B7E-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/32FA8D58-BC12-EA11-885A-6C2B599934B5.root']);