import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:41875', '1:27870', '1:57794', '1:58341', '1:58897', '1:62306', '1:62411', '1:62448', '1:62537', '1:75240', '1:81014', '1:95420', '1:92574', '1:96945', '1:24549', '1:93395', '1:98017', '1:46030', '1:49915', '1:46222', '1:46274', '1:46236', '1:101467', '1:104686', '1:24016', '1:24030', '1:20634', '1:20745', '1:20872', '1:48249', '1:48346', '1:49267', '1:49062', '1:91552', '1:32380', '1:67525', '1:94362', '1:94870', '1:74896', '1:81614', '1:86109', '1:86344', '1:84863', '1:79840', '1:92562', '1:92635', '1:103008', '1:7003', '1:7279', '1:7610', '1:9186', '1:9629', '1:12521', '1:12879', '1:13435', '1:48180', '1:20303', '1:20363', '1:17100', '1:17161', '1:20985', '1:23525', '1:23545', '1:23565', '1:21945', '1:21966', '1:23936', '1:18042', '1:18046', '1:18077', '1:18129', '1:18232', '1:18644', '1:18767', '1:27726', '1:28056', '1:30991', '1:76622', '1:84301', '1:85468', '1:85593', '1:85667', '1:91451', '1:91604', '1:91390', '1:55789', '1:56112', '1:56129', '1:56136', '1:56385', '1:74883', '1:62960', '1:64085', '1:64409', '1:64556', '1:64757', '1:56687', '1:56876', '1:57022', '1:76851', '1:76853', '1:76867', '1:80140', '1:80486', '1:79843', '1:75878', '1:76647', '1:49765', '1:51095', '1:96747', '1:101144', '1:101303', '1:101400', '1:87145', '1:88574', '1:88665', '1:96934', '1:87704', '1:101631', '1:11745', '1:12279', '1:41519', '1:43854', '1:43908', '1:46760', '1:46772', '1:19713', '1:19779', '1:19845', '1:19902', '1:28560', '1:44056', '1:44064', '1:44176', '1:44209', '1:44476', '1:52751', '1:53043', '1:53303', '1:53513', '1:14242', '1:13818', '1:24203', '1:58197', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96B475A8-45F7-E911-A1D4-002590E7D7E2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4056591E-F209-EA11-A699-44A842CFD5BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/006C1B93-29F3-E911-9D2E-6C2B598FF86B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E90CC6C-9A07-EA11-9BAF-0CC47A7C3432.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/463016DD-5DFC-E911-A3BD-0CC47AFCC69E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCD2DC78-350F-EA11-A934-509A4C9F8A8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/36068975-BBFA-E911-8ED3-509A4C9EF923.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C6AA3D6D-A7FB-E911-B199-40F2E9C6ADBA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C4F880FC-64FC-E911-9F1D-0CC47AFF0188.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72568A99-5504-EA11-9A4E-14187764311A.root']);