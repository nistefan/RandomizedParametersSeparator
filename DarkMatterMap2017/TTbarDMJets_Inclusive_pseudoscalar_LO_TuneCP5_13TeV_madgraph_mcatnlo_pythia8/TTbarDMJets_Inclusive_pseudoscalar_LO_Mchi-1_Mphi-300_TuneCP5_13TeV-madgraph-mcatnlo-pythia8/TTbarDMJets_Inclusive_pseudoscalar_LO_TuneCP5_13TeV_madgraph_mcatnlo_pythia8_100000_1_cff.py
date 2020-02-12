import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:48461', '1:48593', '1:48850', '1:48988', '1:63876', '1:64916', '1:87964', '1:83456', '1:83744', '1:53982', '1:60381', '1:48779', '1:76004', '1:75088', '1:57242', '1:65601', '1:71754', '1:74235', '1:74597', '1:74789', '1:77208', '1:85586', '1:94534', '1:68226', '1:69129', '1:69159', '1:69295', '1:69135', '1:77795', '1:82784', '1:74819', '1:86366', '1:84595', '1:86011', '1:95100', '1:104470', '1:23636', '1:23894', '1:24692', '1:17358', '1:19154', '1:22890', '1:1286', '1:18670', '1:18860', '1:22071', '1:22185', '1:80536', '1:70063', '1:70064', '1:82817', '1:83088', '1:12249', '1:12349', '1:12359', '1:12447', '1:12597', '1:70910', '1:77531', '1:77109', '1:78036', '1:82690', '1:82567', '1:70366', '1:86776', '1:84344', '1:85996', '1:95001', '1:95071', '1:85364', '1:86168', '1:86299', '1:9092', '1:1711', '1:4038', '1:8243', '1:8470', '1:2568', '1:5682', '1:8105', '1:6488', '1:16576', '1:70753', '1:82089', '1:82181', '1:34645', '1:36926', '1:36963', '1:36921', '1:62830', '1:64708', '1:63923', '1:78984', '1:84998', '1:86679', '1:154', '1:101805', '1:105417', '1:106261', '1:81422', '1:90051', '1:93846', '1:94792', '1:95263', '1:89788', '1:92906', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/96FE5273-B319-EA11-956A-002590491B22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/AE0B1823-231A-EA11-8338-44A8421274BD.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/DE7C9112-8319-EA11-8C22-24BE05C4D801.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/E6E5485B-E81A-EA11-8DC1-EC0D9A8221DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/A0C03570-4E19-EA11-8016-A0369FC5E090.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/3CAE5ACB-E81A-EA11-8693-008CFA0A565C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/C807253F-E81A-EA11-AD61-AC1F6B34A744.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/100000/5442FE0E-A719-EA11-8D98-0CC47A2B04A6.root']);