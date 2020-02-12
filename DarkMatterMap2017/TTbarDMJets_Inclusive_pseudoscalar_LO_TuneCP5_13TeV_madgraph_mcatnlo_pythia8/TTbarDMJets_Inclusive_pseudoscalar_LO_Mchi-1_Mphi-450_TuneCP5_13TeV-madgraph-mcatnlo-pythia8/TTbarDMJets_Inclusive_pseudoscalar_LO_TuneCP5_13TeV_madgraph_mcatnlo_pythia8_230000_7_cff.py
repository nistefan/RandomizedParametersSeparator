import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1293', '1:14729', '1:1314', '1:15242', '1:19831', '1:18230', '1:24090', '1:31372', '1:72522', '1:87486', '1:87728', '1:97423', '1:55734', '1:55922', '1:57391', '1:102675', '1:102800', '1:102994', '1:102999', '1:94960', '1:46328', '1:64974', '1:71374', '1:76809', '1:81088', '1:77489', '1:89497', '1:98059', '1:54228', '1:45417', '1:52709', '1:56640', '1:61595', '1:57481', '1:57489', '1:52479', '1:52554', '1:53080', '1:61500', '1:62045', '1:62419', '1:61941', '1:64589', '1:66137', '1:66213', '1:66225', '1:70631', '1:13283', '1:21510', '1:21752', '1:23570', '1:21427', '1:21657', '1:82465', '1:85431', '1:51384', '1:53957', '1:58626', '1:58937', '1:59551', '1:57944', '1:62375', '1:60112', '1:61020', '1:65437', '1:66370', '1:65567', '1:66457', '1:66767', '1:71932', '1:86353', '1:83570', '1:47118', '1:40591', '1:49437', '1:39811', '1:59620', '1:64132', '1:67747', '1:67755', '1:71440', '1:51037', '1:52002', '1:52074', '1:52155', '1:52236', '1:52260', '1:52324', '1:53428', '1:53930', '1:59449', '1:59710', '1:92802', '1:98344', '1:73656', '1:105302', '1:104188', '1:81161', '1:81352', '1:81354', '1:81482', '1:81743', '1:81023', '1:81144', '1:81249', '1:81273', '1:60260', '1:64638', '1:73162', '1:76200', '1:74929', '1:78296', '1:81891', '1:93974', '1:96044', '1:101057', '1:101088', '1:103653', '1:105550', '1:105753', '1:105992', '1:59343', '1:59384', '1:59588', '1:59596', '1:71805', '1:67797', '1:82995', '1:84929', '1:95184', '1:103407', '1:101181', '1:104523', '1:104870', '1:102448', '1:105574', '1:105595', '1:57320', '1:77411', '1:94313', '1:106089', '1:101774', '1:101987', '1:104802', '1:79563', '1:80055', '1:80072', '1:23496', '1:25889', '1:23832', '1:77866', '1:79134', '1:85427', '1:94596', '1:46139', '1:59666', '1:21792', '1:24724', '1:30169', '1:30671', '1:39913', '1:48494', '1:49326', '1:49855', '1:43362', '1:51698', '1:79741', '1:11414', '1:16573', '1:16607', '1:16448', '1:16845', '1:84580', '1:98430', '1:98493', '1:90435', '1:92812', '1:94922', '1:70284', '1:83123', '1:86788', '1:90379', '1:98668', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CC916E5A-F8FE-E911-BC5C-3417EBE70078.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/261A750B-1502-EA11-A901-0026B9278651.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0DE8F81-AD03-EA11-895A-A0369FD0B142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A23C784C-A502-EA11-A4FB-00259074AE52.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A6DE693B-2902-EA11-A934-AC1F6B0DE228.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80593C2E-A502-EA11-A430-20CF3027A5F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/20F14403-9A02-EA11-9EF6-D48564599C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A6DC8DA6-9F03-EA11-A25B-CCC5E5F02BFB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B84232C7-D102-EA11-8D9E-A0369FC51EDC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC333E44-8703-EA11-9B66-0242AC1C0506.root']);