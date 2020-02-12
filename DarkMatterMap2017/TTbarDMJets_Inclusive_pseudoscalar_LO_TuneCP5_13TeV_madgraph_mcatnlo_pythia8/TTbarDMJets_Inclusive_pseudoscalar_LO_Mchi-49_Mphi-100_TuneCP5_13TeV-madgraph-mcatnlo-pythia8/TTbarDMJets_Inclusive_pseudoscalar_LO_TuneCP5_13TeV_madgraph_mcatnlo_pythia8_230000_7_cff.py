import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1180', '1:1222', '1:8165', '1:19477', '1:26781', '1:97782', '1:89746', '1:91042', '1:48445', '1:59647', '1:47794', '1:51616', '1:56463', '1:48080', '1:74128', '1:83864', '1:87748', '1:102805', '1:104887', '1:97366', '1:23183', '1:18212', '1:27941', '1:32924', '1:39290', '1:42032', '1:41757', '1:58125', '1:59920', '1:90844', '1:86975', '1:90885', '1:97969', '1:55268', '1:55657', '1:48916', '1:52334', '1:52743', '1:53031', '1:61350', '1:61766', '1:61776', '1:62021', '1:62035', '1:62277', '1:62287', '1:62385', '1:66000', '1:66295', '1:90097', '1:101523', '1:102964', '1:21304', '1:21902', '1:91823', '1:52773', '1:53384', '1:58649', '1:57716', '1:58174', '1:59870', '1:60424', '1:61289', '1:62466', '1:65438', '1:75528', '1:64586', '1:64750', '1:66014', '1:88950', '1:18259', '1:40872', '1:41040', '1:44646', '1:40143', '1:42611', '1:59126', '1:59135', '1:59411', '1:60187', '1:62304', '1:64172', '1:64190', '1:64293', '1:67228', '1:71813', '1:51659', '1:52568', '1:52795', '1:53057', '1:53209', '1:53526', '1:59402', '1:59820', '1:59936', '1:98892', '1:98586', '1:72189', '1:94835', '1:97369', '1:91634', '1:81298', '1:81323', '1:81444', '1:81562', '1:81735', '1:81396', '1:46898', '1:53688', '1:61607', '1:64025', '1:64081', '1:64793', '1:66197', '1:74309', '1:89170', '1:93085', '1:93659', '1:96255', '1:102254', '1:103854', '1:103878', '1:105609', '1:56191', '1:57043', '1:71887', '1:67017', '1:87582', '1:88281', '1:97117', '1:98362', '1:70929', '1:93555', '1:104821', '1:102542', '1:104596', '1:105975', '1:105844', '1:58472', '1:48235', '1:75363', '1:83385', '1:87787', '1:93962', '1:101530', '1:101645', '1:79756', '1:80281', '1:23627', '1:21506', '1:30468', '1:47905', '1:43557', '1:53059', '1:23585', '1:24001', '1:20147', '1:20660', '1:25436', '1:25655', '1:28107', '1:32986', '1:42585', '1:48274', '1:55971', '1:40920', '1:58955', '1:72688', '1:72941', '1:76925', '1:79699', '1:9158', '1:13942', '1:88678', '1:97798', '1:71850', '1:91712', '1:92198', '1:88710', '1:76904', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CC916E5A-F8FE-E911-BC5C-3417EBE70078.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/261A750B-1502-EA11-A901-0026B9278651.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0DE8F81-AD03-EA11-895A-A0369FD0B142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A23C784C-A502-EA11-A4FB-00259074AE52.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A6DE693B-2902-EA11-A934-AC1F6B0DE228.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80593C2E-A502-EA11-A430-20CF3027A5F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/20F14403-9A02-EA11-9EF6-D48564599C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A6DC8DA6-9F03-EA11-A25B-CCC5E5F02BFB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B84232C7-D102-EA11-8D9E-A0369FC51EDC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC333E44-8703-EA11-9B66-0242AC1C0506.root']);