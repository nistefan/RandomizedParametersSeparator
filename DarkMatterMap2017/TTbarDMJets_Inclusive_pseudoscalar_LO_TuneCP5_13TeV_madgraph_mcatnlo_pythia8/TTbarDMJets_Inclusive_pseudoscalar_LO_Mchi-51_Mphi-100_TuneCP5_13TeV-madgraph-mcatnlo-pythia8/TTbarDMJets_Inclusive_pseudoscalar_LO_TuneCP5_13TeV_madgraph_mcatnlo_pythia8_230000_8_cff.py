import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8532', '1:11006', '1:11110', '1:12416', '1:20156', '1:20445', '1:25656', '1:78494', '1:28266', '1:30170', '1:44132', '1:72978', '1:27514', '1:30952', '1:42066', '1:42464', '1:42736', '1:42900', '1:93137', '1:70433', '1:90289', '1:84360', '1:89645', '1:89792', '1:64632', '1:72916', '1:67241', '1:78952', '1:28585', '1:20017', '1:24272', '1:72637', '1:72563', '1:79524', '1:83637', '1:90191', '1:102464', '1:4051', '1:8754', '1:14085', '1:9417', '1:11988', '1:22913', '1:28784', '1:30497', '1:44598', '1:47792', '1:65085', '1:66270', '1:74932', '1:104590', '1:66423', '1:60915', '1:104197', '1:6469', '1:12824', '1:102489', '1:7875', '1:8139', '1:8491', '1:48805', '1:51573', '1:32297', '1:32426', '1:32319', '1:32307', '1:32509', '1:32573', '1:66774', '1:66841', '1:67182', '1:67269', '1:67757', '1:46464', '1:61684', '1:67942', '1:71150', '1:11388', '1:12126', '1:11318', '1:14876', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78CEA8C6-3B04-EA11-A932-001E677925A0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0A05A38F-FD06-EA11-9A80-AC1F6B0DE3A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2226C86C-BD06-EA11-AD47-AC1F6B0DE296.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DCA075CC-F207-EA11-8401-48FD8EE73A81.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E32F162-BC12-EA11-946E-008CFAFD5234.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B80D0F07-BC12-EA11-9A6B-A4BF0112BC04.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/08A1C493-AF12-EA11-9AED-485B39897242.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60EDCC5C-BC12-EA11-91E4-0CC47A7034D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C94C93E-BC12-EA11-8B7E-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/32FA8D58-BC12-EA11-885A-6C2B599934B5.root']);