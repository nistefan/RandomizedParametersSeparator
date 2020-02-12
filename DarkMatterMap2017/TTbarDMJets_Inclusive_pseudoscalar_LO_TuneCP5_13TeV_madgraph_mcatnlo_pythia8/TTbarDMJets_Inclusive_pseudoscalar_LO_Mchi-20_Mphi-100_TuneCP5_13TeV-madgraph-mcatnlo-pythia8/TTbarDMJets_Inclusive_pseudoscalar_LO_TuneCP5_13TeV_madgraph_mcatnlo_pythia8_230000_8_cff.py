import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8941', '1:8520', '1:13477', '1:19444', '1:20332', '1:19664', '1:39122', '1:30857', '1:81664', '1:28319', '1:29871', '1:32322', '1:32689', '1:77362', '1:78912', '1:81650', '1:95357', '1:84511', '1:85505', '1:28673', '1:20939', '1:39699', '1:45190', '1:72013', '1:72878', '1:82449', '1:85043', '1:86209', '1:86403', '1:89620', '1:102280', '1:102804', '1:102868', '1:102074', '1:102090', '1:102292', '1:5144', '1:5690', '1:8390', '1:8597', '1:13540', '1:11470', '1:44915', '1:44997', '1:45473', '1:47742', '1:64145', '1:66942', '1:56434', '1:5591', '1:12503', '1:14395', '1:101629', '1:101660', '1:8402', '1:8468', '1:8856', '1:8924', '1:8604', '1:24044', '1:41362', '1:48130', '1:32360', '1:67318', '1:55356', '1:62251', '1:64474', '1:72549', '1:73271', '1:80397', '1:10385', '1:10987', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78CEA8C6-3B04-EA11-A932-001E677925A0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0A05A38F-FD06-EA11-9A80-AC1F6B0DE3A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2226C86C-BD06-EA11-AD47-AC1F6B0DE296.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DCA075CC-F207-EA11-8401-48FD8EE73A81.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E32F162-BC12-EA11-946E-008CFAFD5234.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B80D0F07-BC12-EA11-9A6B-A4BF0112BC04.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/08A1C493-AF12-EA11-9AED-485B39897242.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60EDCC5C-BC12-EA11-91E4-0CC47A7034D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C94C93E-BC12-EA11-8B7E-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/32FA8D58-BC12-EA11-885A-6C2B599934B5.root']);