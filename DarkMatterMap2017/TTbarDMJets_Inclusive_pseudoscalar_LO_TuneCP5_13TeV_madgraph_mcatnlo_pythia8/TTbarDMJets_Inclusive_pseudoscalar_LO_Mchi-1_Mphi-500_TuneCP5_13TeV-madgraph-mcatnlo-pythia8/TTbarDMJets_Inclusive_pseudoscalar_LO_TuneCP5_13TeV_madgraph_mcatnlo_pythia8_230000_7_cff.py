import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8782', '1:24919', '1:31948', '1:17602', '1:30452', '1:39306', '1:97447', '1:87599', '1:87752', '1:84167', '1:54701', '1:55764', '1:56742', '1:91777', '1:64680', '1:102681', '1:60835', '1:73108', '1:96988', '1:97594', '1:52904', '1:61492', '1:61632', '1:61666', '1:62298', '1:64574', '1:97653', '1:13163', '1:13578', '1:14670', '1:15064', '1:16338', '1:20515', '1:20706', '1:23903', '1:23302', '1:23464', '1:94057', '1:82116', '1:54664', '1:54665', '1:54787', '1:57226', '1:54525', '1:57642', '1:59880', '1:62275', '1:60096', '1:71490', '1:71609', '1:82144', '1:22187', '1:41129', '1:46396', '1:49353', '1:83460', '1:56447', '1:81704', '1:61736', '1:64140', '1:64204', '1:64285', '1:64311', '1:101120', '1:101379', '1:67958', '1:72065', '1:51774', '1:51799', '1:52178', '1:52496', '1:51301', '1:51944', '1:52202', '1:52937', '1:53179', '1:59538', '1:60164', '1:82820', '1:87702', '1:98885', '1:97937', '1:105161', '1:87815', '1:106077', '1:81192', '1:81449', '1:64901', '1:76026', '1:81058', '1:93024', '1:94733', '1:98155', '1:90897', '1:101048', '1:101452', '1:103595', '1:103610', '1:103992', '1:103613', '1:103712', '1:103732', '1:103790', '1:103813', '1:105739', '1:71905', '1:72106', '1:67190', '1:71156', '1:96775', '1:103111', '1:103130', '1:105966', '1:106243', '1:101260', '1:104443', '1:105583', '1:105982', '1:51581', '1:54367', '1:91509', '1:93926', '1:92849', '1:97994', '1:104605', '1:104927', '1:101409', '1:79164', '1:16284', '1:20302', '1:24311', '1:26651', '1:66115', '1:83451', '1:87910', '1:88438', '1:89584', '1:52117', '1:52423', '1:21874', '1:19119', '1:31817', '1:25882', '1:26239', '1:18101', '1:45620', '1:53278', '1:59606', '1:52539', '1:61752', '1:79351', '1:16677', '1:16569', '1:84125', '1:92339', '1:65778', '1:66826', '1:72869', '1:90283', '1:86785', '1:97926', '1:85504', '1:70421', '1:78042', '1:87766', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CC916E5A-F8FE-E911-BC5C-3417EBE70078.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/261A750B-1502-EA11-A901-0026B9278651.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0DE8F81-AD03-EA11-895A-A0369FD0B142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A23C784C-A502-EA11-A4FB-00259074AE52.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A6DE693B-2902-EA11-A934-AC1F6B0DE228.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80593C2E-A502-EA11-A430-20CF3027A5F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/20F14403-9A02-EA11-9EF6-D48564599C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A6DC8DA6-9F03-EA11-A25B-CCC5E5F02BFB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B84232C7-D102-EA11-8D9E-A0369FC51EDC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC333E44-8703-EA11-9B66-0242AC1C0506.root']);