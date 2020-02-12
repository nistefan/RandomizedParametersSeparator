import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:45037', '1:30650', '1:57851', '1:57929', '1:58260', '1:58325', '1:58419', '1:58679', '1:62576', '1:62683', '1:93679', '1:98497', '1:96428', '1:28327', '1:28548', '1:15572', '1:15847', '1:45942', '1:47824', '1:49931', '1:46055', '1:46112', '1:46187', '1:46167', '1:46215', '1:19966', '1:24145', '1:20161', '1:48765', '1:48800', '1:49445', '1:79182', '1:57940', '1:67960', '1:73172', '1:81864', '1:93437', '1:67792', '1:71267', '1:81706', '1:83568', '1:83934', '1:86199', '1:86230', '1:86288', '1:81236', '1:92738', '1:92965', '1:93404', '1:98427', '1:98718', '1:103058', '1:103089', '1:103207', '1:97528', '1:98101', '1:7733', '1:7846', '1:9859', '1:9997', '1:12780', '1:13145', '1:13300', '1:13926', '1:46764', '1:46998', '1:20002', '1:20294', '1:20335', '1:20369', '1:23631', '1:23643', '1:23105', '1:23372', '1:23452', '1:23691', '1:15740', '1:18192', '1:18743', '1:27665', '1:27872', '1:30849', '1:30850', '1:76453', '1:76561', '1:76643', '1:76536', '1:85715', '1:85945', '1:88757', '1:92814', '1:94005', '1:94087', '1:55762', '1:55809', '1:56018', '1:56141', '1:56229', '1:56232', '1:56350', '1:56386', '1:56451', '1:64439', '1:64514', '1:64731', '1:76624', '1:76988', '1:56427', '1:56443', '1:56605', '1:56711', '1:56808', '1:56869', '1:56918', '1:76731', '1:76796', '1:76868', '1:80089', '1:80439', '1:76391', '1:49645', '1:49961', '1:49965', '1:98363', '1:101178', '1:87121', '1:87149', '1:87339', '1:87608', '1:87485', '1:88119', '1:102396', '1:11875', '1:12255', '1:41724', '1:42027', '1:46221', '1:46910', '1:19873', '1:28813', '1:26364', '1:26447', '1:26665', '1:44251', '1:44437', '1:44444', '1:44576', '1:44597', '1:51086', '1:57575', '1:58317', '1:60152', '1:64431', '1:74312', '1:67067', '1:67068', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96B475A8-45F7-E911-A1D4-002590E7D7E2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4056591E-F209-EA11-A699-44A842CFD5BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/006C1B93-29F3-E911-9D2E-6C2B598FF86B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E90CC6C-9A07-EA11-9BAF-0CC47A7C3432.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/463016DD-5DFC-E911-A3BD-0CC47AFCC69E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCD2DC78-350F-EA11-A934-509A4C9F8A8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/36068975-BBFA-E911-8ED3-509A4C9EF923.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C6AA3D6D-A7FB-E911-B199-40F2E9C6ADBA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C4F880FC-64FC-E911-9F1D-0CC47AFF0188.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72568A99-5504-EA11-9A4E-14187764311A.root']);