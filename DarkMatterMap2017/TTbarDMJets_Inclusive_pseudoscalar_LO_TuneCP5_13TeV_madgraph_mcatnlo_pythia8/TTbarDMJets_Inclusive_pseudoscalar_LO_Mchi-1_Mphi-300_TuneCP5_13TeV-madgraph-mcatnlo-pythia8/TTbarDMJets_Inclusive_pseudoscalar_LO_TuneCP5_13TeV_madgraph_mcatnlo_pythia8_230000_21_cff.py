import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:71254', '1:70453', '1:84174', '1:86778', '1:95284', '1:97173', '1:80000', '1:97750', '1:98083', '1:98180', '1:98371', '1:85071', '1:90085', '1:77345', '1:79460', '1:78122', '1:87938', '1:83249', '1:87359', '1:89477', '1:80091', '1:26460', '1:42734', '1:44024', '1:44026', '1:42829', '1:42985', '1:44170', '1:44392', '1:73669', '1:73904', '1:74060', '1:74167', '1:40569', '1:40600', '1:40638', '1:41193', '1:41322', '1:41518', '1:41768', '1:41224', '1:42818', '1:44213', '1:44610', '1:89926', '1:73701', '1:74277', '1:102384', '1:102386', '1:102461', '1:84985', '1:75086', '1:75112', '1:81640', '1:83906', '1:97310', '1:13174', '1:14333', '1:88311', '1:52454', '1:52569', '1:52609', '1:52690', '1:52789', '1:104248', '1:104399', '1:104488', '1:104666', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4D2AD02-D40A-EA11-A0B7-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E48D6400-92FB-E911-A2F9-0CC47A7FC6D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F89F393C-D012-EA11-B06C-44A842BE76FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/56BCA64F-BC12-EA11-86AC-002590D425C0.root']);