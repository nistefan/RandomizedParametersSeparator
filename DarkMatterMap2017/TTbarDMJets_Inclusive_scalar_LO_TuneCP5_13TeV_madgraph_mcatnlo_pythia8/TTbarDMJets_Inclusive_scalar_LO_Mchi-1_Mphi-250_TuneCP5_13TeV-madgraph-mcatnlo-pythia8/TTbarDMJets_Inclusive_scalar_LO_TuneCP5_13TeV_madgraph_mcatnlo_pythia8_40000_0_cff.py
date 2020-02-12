import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:41351', '1:41755', '1:41914', '1:47043', '1:47056', '1:47057', '1:45379', '1:45429', '1:45891', '1:66573', '1:66136', '1:66164', '1:66728', '1:82959', '1:84488', '1:92186', '1:92129', '1:84737', '1:93157', '1:47981', '1:43025', '1:44487', '1:44490', '1:43232', '1:66424', '1:66503', '1:82607', '1:66875', '1:82737', '1:82777', '1:82911', '1:66211', '1:66224', '1:66668', '1:66166', '1:66448', '1:66554', '1:83338', '1:83348', '1:83382', '1:82769', '1:83064', '1:12756', '1:12780', '1:12789', '1:12796', '1:12851', '1:12854', '1:12862', '1:44545', '1:48413', '1:45338', '1:65293', '1:65315', '1:65343', '1:65456', '1:83185', '1:83503', '1:42185', '1:42205', '1:42351', '1:47008', '1:44959', '1:45161', '1:93321', '1:93849', '1:93452', '1:83293', '1:93124', '1:11089', '1:12159', '1:11989', '1:84708', '1:92226', '1:92307', '1:92332', '1:92755', '1:92454', '1:11903', '1:12065', '1:12071', '1:12079', '1:65598', '1:65965', '1:66589', '1:82564', '1:82874', '1:66801', '1:84948', '1:65589', '1:82496', '1:83218', '1:66201', '1:82895', '1:82155', '1:84531', '1:84194', '1:11095', '1:42796', '1:43092', '1:44526', '1:45019', '1:43165', '1:43431', '1:65702', '1:65914', '1:65907', '1:45717', '1:43404', '1:48251', '1:48269', '1:65944', '1:44970', '1:45082', '1:45084', '1:45009', '1:45296', '1:45543', '1:45544', '1:84540', '1:92240', '1:92267', '1:92281', '1:84666', '1:84672', '1:84680', '1:93997', '1:93989', '1:12583', '1:12407', '1:12691', '1:12698', '1:12702', '1:47030', '1:47652', '1:47667', '1:47674', '1:43183', '1:43321', '1:43977', '1:45814', '1:65825', '1:45820', '1:42457', '1:42522', '1:42534', '1:45759', '1:65375', '1:65584', '1:65778', '1:48014', '1:65793', '1:65389', '1:93427', '1:93513', '1:44532', '1:44618', '1:44330', '1:44577', '1:44780', '1:92847', '1:84081', '1:84136', '1:84578', '1:92325', '1:84743', '1:84753', '1:84761', '1:92295', '1:93026', '1:93036', '1:84933', '1:41154', '1:41887', '1:43577', '1:43766', '1:48224', '1:48774', '1:48804', '1:12453', '1:12493', '1:12474', '1:12505', '1:12517', '1:43018', '1:44087', '1:41970', '1:41978', '1:47130', '1:47136', '1:44206', '1:47866', '1:47885', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/8026A6CC-9F0F-EA11-9BCD-3CFDFE63A880.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/CA0868E4-580F-EA11-A73F-14187751C030.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/F6C25D2B-6C10-EA11-A3AB-AC1F6B567680.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/82300CEE-C311-EA11-A7D4-0CC47AFCC4BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DE988EEC-0111-EA11-B2B7-00269E95B0A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/24390700-9E11-EA11-ACCD-6C2B5990D0B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/88C8B414-8510-EA11-8999-A4BF0108B89A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/84DA2C2E-B80B-EA11-9ED3-EC0D9A8225FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/7C848483-8210-EA11-9901-0CC47A7E69D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/AA6F0C5B-8710-EA11-8112-00266CFFBF64.root']);