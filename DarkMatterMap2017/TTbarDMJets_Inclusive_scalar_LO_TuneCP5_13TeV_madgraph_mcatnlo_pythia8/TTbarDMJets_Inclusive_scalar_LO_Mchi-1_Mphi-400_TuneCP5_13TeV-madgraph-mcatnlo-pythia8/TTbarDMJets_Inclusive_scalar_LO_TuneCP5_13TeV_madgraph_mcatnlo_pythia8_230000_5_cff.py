import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1588', '1:3393', '1:17610', '1:22366', '1:26836', '1:29783', '1:33841', '1:52312', '1:52959', '1:56009', '1:56214', '1:59625', '1:34232', '1:35158', '1:35528', '1:40493', '1:32278', '1:35293', '1:49254', '1:71681', '1:96520', '1:9340', '1:15117', '1:13855', '1:15681', '1:55462', '1:62153', '1:62432', '1:67760', '1:76460', '1:68370', '1:102410', '1:9283', '1:9931', '1:17160', '1:20086', '1:20192', '1:59008', '1:61792', '1:62099', '1:69703', '1:55069', '1:62862', '1:71768', '1:8533', '1:9588', '1:14749', '1:16725', '1:16758', '1:9884', '1:22804', '1:55368', '1:75364', '1:70174', '1:90264', '1:94248', '1:94302', '1:56633', '1:63091', '1:69819', '1:64232', '1:69484', '1:69566', '1:89999', '1:99528', '1:99604', '1:100100', '1:87252', '1:88719', '1:88778', '1:80961', '1:81006', '1:81932', '1:85049', '1:74193', '1:74469', '1:80092', '1:81317', '1:81733', '1:2894', '1:4214', '1:4304', '1:58256', '1:59747', '1:61124', '1:73091', '1:63629', '1:63732', '1:53865', '1:67684', '1:72929', '1:89407', '1:100137', '1:53581', '1:56242', '1:57756', '1:97453', '1:76070', '1:78371', '1:86819', '1:91665', '1:86956', '1:87974', '1:80494', '1:81369', '1:86738', '1:94787', '1:87741', '1:94122', '1:94883', '1:95895', '1:96593', '1:102070', '1:97466', '1:97214', '1:35807', '1:35822', '1:75863', '1:72637', '1:80874', '1:80893', '1:81245', '1:101671', '1:94325', '1:99439', '1:99540', '1:99559', '1:90188', '1:101339', '1:94340', '1:95629', '1:69743', '1:75023', '1:75345', '1:91268', '1:94184', '1:95067', '1:95153', '1:95383', '1:95388', '1:95466', '1:4922', '1:5458', '1:5472', '1:5661', '1:91243', '1:86143', '1:86223', '1:6184', '1:6434', '1:46106', '1:74820', '1:89072', '1:90249', '1:95909', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/663C015C-090B-EA11-BFB8-0CC47A4D761A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C1F2C40-140B-EA11-B0C9-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50E09B46-0F0B-EA11-B430-0CC47A7C353E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/00B4F279-060B-EA11-B0D5-44A842CFD64D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/42F08944-8A0B-EA11-81BC-0CC47A4D7670.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3CFE5F00-040C-EA11-BAEC-FA163E1C0945.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4429EB0E-E00D-EA11-864F-A4BF01287D43.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/86A930BC-3913-EA11-B2E6-6CC2173BC990.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/12FDBADE-3913-EA11-8539-001E67580724.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/14B38BBF-3913-EA11-82EE-141877410522.root']);