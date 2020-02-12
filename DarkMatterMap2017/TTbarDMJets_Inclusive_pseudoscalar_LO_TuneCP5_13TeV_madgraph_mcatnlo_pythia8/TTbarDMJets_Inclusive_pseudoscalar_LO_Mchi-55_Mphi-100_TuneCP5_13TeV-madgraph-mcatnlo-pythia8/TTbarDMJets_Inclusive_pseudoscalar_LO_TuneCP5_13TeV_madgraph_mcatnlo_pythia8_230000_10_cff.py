import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:15008', '1:15021', '1:15089', '1:15101', '1:42210', '1:96125', '1:97076', '1:97419', '1:98310', '1:52397', '1:64037', '1:65793', '1:66320', '1:47413', '1:28041', '1:19242', '1:19348', '1:19495', '1:62818', '1:71281', '1:71614', '1:71657', '1:67654', '1:67784', '1:82302', '1:82416', '1:83350', '1:83354', '1:83469', '1:83489', '1:28320', '1:45816', '1:45582', '1:47425', '1:52048', '1:64345', '1:80043', '1:81580', '1:92868', '1:73900', '1:20418', '1:20626', '1:25868', '1:47641', '1:47779', '1:70702', '1:77098', '1:79574', '1:79873', '1:80319', '1:11344', '1:31027', '1:64326', '1:8363', '1:15956', '1:102891', '1:64186', '1:64915', '1:65280', '1:66480', '1:67127', '1:20676', '1:24915', '1:18015', '1:18315', '1:18322', '1:18333', '1:28242', '1:20530', '1:44086', '1:25024', '1:25304', '1:44518', '1:45330', '1:98909', '1:82464', '1:82832', '1:82887', '1:83236', '1:92249', '1:92317', '1:47621', '1:47669', '1:49921', '1:49951', '1:48748', '1:72291', '1:75806', '1:72662', '1:79713', '1:82615', '1:85772', '1:84654', '1:86725', '1:87177', '1:87695', '1:88196', '1:52009', '1:52124', '1:70168', '1:70348', '1:70365', '1:70503', '1:65714', '1:65879', '1:104098', '1:47593', '1:105347', '1:105884', '1:98735', '1:98790', '1:104353', '1:104384', '1:104915', '1:88355', '1:89400', '1:89513', '1:96889', '1:102716', '1:5367', '1:5548', '1:5641', '1:5935', '1:6726', '1:7677', '1:7194', '1:7209', '1:7283', '1:7300', '1:7637', '1:51320', '1:76528', '1:88136', '1:20582', '1:81382', '1:81907', '1:24792', '1:97892', '1:98171', '1:98554', '1:98751', '1:104097', '1:104173', '1:104780', '1:27363', '1:30322', '1:51692', '1:51916', '1:61821', '1:62301', '1:62680', '1:62809', '1:62965', '1:5485', '1:5681', '1:6447', '1:9278', '1:9763', '1:9844', '1:10465', '1:12368', '1:14757', '1:14912', '1:15369', '1:15637', '1:15695', '1:16172', '1:16269', '1:16343', '1:16504', '1:16562', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C75EAD7-A60A-EA11-B2EA-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CAA33E3-B40A-EA11-B217-0CC47A4C8EB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0C7BD80-B30A-EA11-990C-0CC47A7C345E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/827A94E9-460C-EA11-9197-0CC47A7C34D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C25D68E-CA0A-EA11-A4D3-0CC47A4D762E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4F23B9-260F-EA11-80C3-0CC47A4D7690.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A38857F-43F9-E911-9334-0CC47A5FBE21.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2A529D76-BC12-EA11-85B1-90B11C070100.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80404779-FBF6-E911-8982-AC1F6B0F71D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A13F5EF-28F2-E911-9B0D-00215AA64960.root']);