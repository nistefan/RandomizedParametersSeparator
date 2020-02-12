import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:71435', '1:78325', '1:78515', '1:84204', '1:74141', '1:74327', '1:79846', '1:80692', '1:80790', '1:89819', '1:5426', '1:32762', '1:32872', '1:32941', '1:32966', '1:101826', '1:4854', '1:5959', '1:6708', '1:25786', '1:47103', '1:24442', '1:24827', '1:74801', '1:74971', '1:39903', '1:42136', '1:42168', '1:42188', '1:42382', '1:42649', '1:59347', '1:59518', '1:59719', '1:59796', '1:75182', '1:75524', '1:75909', '1:5132', '1:2033', '1:3621', '1:6820', '1:9945', '1:70102', '1:77113', '1:85213', '1:88909', '1:89225', '1:80963', '1:81801', '1:80493', '1:81597', '1:32478', '1:42906', '1:20368', '1:19318', '1:19859', '1:19686', '1:62142', '1:62717', '1:102194', '1:45794', '1:45811', '1:45869', '1:97624', '1:97749', '1:97902', '1:98298', '1:98533', '1:98537', '1:98651', '1:98070', '1:98225', '1:98588', '1:51431', '1:51447', '1:70674', '1:74127', '1:52192', '1:54879', '1:74158', '1:74346', '1:3678', '1:4178', '1:4340', '1:4365', '1:21157', '1:21408', '1:30354', '1:46018', '1:46064', '1:46256', '1:46291', '1:48491', '1:48564', '1:48603', '1:48648', '1:48679', '1:48691', '1:54512', '1:54779', '1:55319', '1:55586', '1:55704', '1:2230', '1:2519', '1:2546', '1:2949', '1:17604', '1:17689', '1:29125', '1:29168', '1:21700', '1:23084', '1:28760', '1:29058', '1:30050', '1:30052', '1:30389', '1:30429', '1:30459', '1:32011', '1:52736', '1:56875', '1:15772', '1:15805', '1:1019', '1:1801', '1:1831', '1:6915', '1:17316', '1:17503', '1:17807', '1:8502', '1:8615', '1:8197', '1:6843', '1:7137', '1:7659', '1:8400', '1:15521', '1:15636', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C7CCC2F-2BF0-E911-A9D8-24BE05C488E1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3C5331FC-79FB-E911-9DA3-A4BF01287D43.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7268BD3C-EBF9-E911-9D94-002590DE6DD4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78A56FCD-8E02-EA11-AAE1-F4E9D4D1EA90.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A413599C-04F9-E911-B9F1-0025901D0C54.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24B7C050-A40A-EA11-B9AD-0CC47A7C3444.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/620017DD-0BF3-E911-AD90-E4115BCE00BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/580EEBBB-69FC-E911-AF98-0CC47AFCC696.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1AD16148-BC12-EA11-A03F-FA163E64B350.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2B1F5FA-64FC-E911-B838-0CC47AFF0460.root']);