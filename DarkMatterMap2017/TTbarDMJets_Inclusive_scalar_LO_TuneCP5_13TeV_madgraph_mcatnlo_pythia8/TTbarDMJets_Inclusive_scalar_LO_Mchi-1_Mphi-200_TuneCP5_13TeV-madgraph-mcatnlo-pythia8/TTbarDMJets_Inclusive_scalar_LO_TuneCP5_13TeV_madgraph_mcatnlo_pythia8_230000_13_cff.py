import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:52008', '1:55263', '1:78528', '1:102163', '1:88379', '1:91981', '1:88424', '1:32855', '1:37549', '1:39079', '1:39137', '1:39323', '1:39453', '1:62244', '1:62624', '1:62741', '1:40317', '1:46158', '1:46409', '1:46522', '1:49071', '1:54511', '1:57263', '1:58216', '1:62041', '1:55055', '1:55093', '1:55809', '1:64739', '1:67006', '1:67150', '1:67361', '1:67507', '1:67859', '1:67993', '1:67264', '1:67457', '1:69747', '1:69749', '1:74121', '1:74171', '1:74202', '1:6406', '1:8169', '1:15291', '1:16852', '1:19407', '1:13266', '1:16216', '1:7458', '1:9569', '1:14698', '1:17288', '1:17331', '1:19146', '1:19243', '1:19274', '1:27090', '1:32934', '1:96090', '1:30703', '1:101885', '1:74489', '1:74959', '1:70108', '1:73678', '1:80308', '1:88297', '1:80081', '1:89045', '1:77230', '1:89377', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C01DAC7D-3A13-EA11-AAE5-90E2BAD1C9A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44EF9CBA-3913-EA11-94B8-E0071B73B6D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0ADEA135-D803-EA11-953D-B02628342210.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3EA80BAD-9601-EA11-872F-8CDCD4A99E60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE827094-2BFD-E911-A20A-0CC47A2B03A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA216DD2-5504-EA11-86F9-48D539F38676.root']);