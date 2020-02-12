import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:82370', '1:71635', '1:75439', '1:80403', '1:74734', '1:81209', '1:81983', '1:90830', '1:4410', '1:4430', '1:32894', '1:32883', '1:32955', '1:101654', '1:101675', '1:101688', '1:101797', '1:5757', '1:6829', '1:7106', '1:7200', '1:7429', '1:25943', '1:26036', '1:26044', '1:31008', '1:31632', '1:24550', '1:74690', '1:74842', '1:42097', '1:42537', '1:42641', '1:59315', '1:59999', '1:75083', '1:75204', '1:75263', '1:75348', '1:75538', '1:6399', '1:7100', '1:7885', '1:8854', '1:91992', '1:70322', '1:70606', '1:91138', '1:94172', '1:80849', '1:81883', '1:80639', '1:32348', '1:31384', '1:24124', '1:17952', '1:30555', '1:19288', '1:91825', '1:59621', '1:94347', '1:45743', '1:45843', '1:45945', '1:45973', '1:97628', '1:98464', '1:48244', '1:51145', '1:51366', '1:82097', '1:84226', '1:88199', '1:61737', '1:58302', '1:62513', '1:67526', '1:4161', '1:5056', '1:5195', '1:4527', '1:4794', '1:20285', '1:20851', '1:21518', '1:21520', '1:30430', '1:30689', '1:30888', '1:32104', '1:8792', '1:10708', '1:46029', '1:46151', '1:46469', '1:48552', '1:48553', '1:48620', '1:48668', '1:48681', '1:48701', '1:2552', '1:2854', '1:3078', '1:29088', '1:29136', '1:29142', '1:29159', '1:21554', '1:28143', '1:28866', '1:29372', '1:30220', '1:29940', '1:30656', '1:14162', '1:15595', '1:15753', '1:62783', '1:62791', '1:62831', '1:62969', '1:1849', '1:17328', '1:17381', '1:17646', '1:39044', '1:23753', '1:23453', '1:26512', '1:8830', '1:7124', '1:8171', '1:8262', '1:15295', '1:15664', '1:15682', '1:16273', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C7CCC2F-2BF0-E911-A9D8-24BE05C488E1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3C5331FC-79FB-E911-9DA3-A4BF01287D43.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7268BD3C-EBF9-E911-9D94-002590DE6DD4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78A56FCD-8E02-EA11-AAE1-F4E9D4D1EA90.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A413599C-04F9-E911-B9F1-0025901D0C54.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24B7C050-A40A-EA11-B9AD-0CC47A7C3444.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/620017DD-0BF3-E911-AD90-E4115BCE00BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/580EEBBB-69FC-E911-AF98-0CC47AFCC696.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1AD16148-BC12-EA11-A03F-FA163E64B350.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2B1F5FA-64FC-E911-B838-0CC47AFF0460.root']);