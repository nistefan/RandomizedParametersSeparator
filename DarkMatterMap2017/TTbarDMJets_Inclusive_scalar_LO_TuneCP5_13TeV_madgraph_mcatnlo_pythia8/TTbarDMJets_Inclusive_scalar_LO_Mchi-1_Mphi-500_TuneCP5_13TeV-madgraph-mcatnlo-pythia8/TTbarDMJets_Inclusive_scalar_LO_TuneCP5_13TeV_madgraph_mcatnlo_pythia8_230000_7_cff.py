import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:70013', '1:70215', '1:70546', '1:70870', '1:70972', '1:71563', '1:73324', '1:95280', '1:96344', '1:99438', '1:99637', '1:100546', '1:97184', '1:100799', '1:88180', '1:90060', '1:94331', '1:95541', '1:89113', '1:85733', '1:86415', '1:77374', '1:77727', '1:102077', '1:102139', '1:102388', '1:102427', '1:102459', '1:94377', '1:94313', '1:98032', '1:101460', '1:101935', '1:99964', '1:68588', '1:68154', '1:77995', '1:28866', '1:32549', '1:32567', '1:32825', '1:31621', '1:32078', '1:32248', '1:6104', '1:8856', '1:16883', '1:16949', '1:20846', '1:13111', '1:58087', '1:58218', '1:96696', '1:96978', '1:98046', '1:98254', '1:13032', '1:7632', '1:80889', '1:85100', '1:89786', '1:52764', '1:54890', '1:55090', '1:55505', '1:96798', '1:101754', '1:102309', '1:68682', '1:75042', '1:75866', '1:38736', '1:38825', '1:40304', '1:94859', '1:95531', '1:95681', '1:95806', '1:98064', '1:98130', '1:98268', '1:98412', '1:98445', '1:67949', '1:67976', '1:85839', '1:85879', '1:85987', '1:86156', '1:86524', '1:86682', '1:86926', '1:86494', '1:101966', '1:91111', '1:91419', '1:91693', '1:91820', '1:59387', '1:60259', '1:60323', '1:68334', '1:75413', '1:75451', '1:68006', '1:68513', '1:70699', '1:70943', '1:69314', '1:69403', '1:70243', '1:70556', '1:70622', '1:70742', '1:70784', '1:70918', '1:77420', '1:77437', '1:75501', '1:94348', '1:94478', '1:94619', '1:98387', '1:79590', '1:79729', '1:80624', '1:90990', '1:98799', '1:6704', '1:6717', '1:7208', '1:7644', '1:59077', '1:59448', '1:59570', '1:59587', '1:59595', '1:59699', '1:59952', '1:76290', '1:63070', '1:63082', '1:63217', '1:63260', '1:63669', '1:89281', '1:90671', '1:89140', '1:89181', '1:89280', '1:89309', '1:89343', '1:89414', '1:89601', '1:89612', '1:89667', '1:89782', '1:90365', '1:91674', '1:94330', '1:54651', '1:54681', '1:54745', '1:54811', '1:55105', '1:54896', '1:63225', '1:63955', '1:64335', '1:69672', '1:69722', '1:69785', '1:76120', '1:34028', '1:34075', '1:34098', '1:34108', '1:34434', '1:34481', '1:35020', '1:50038', '1:50825', '1:50906', '1:51190', '1:51847', '1:52642', '1:52748', '1:90852', '1:94419', '1:94768', '1:94969', '1:71011', '1:71232', '1:71671', '1:71761', '1:71206', '1:71255', '1:72229', '1:86944', '1:91870', '1:94017', '1:94137', '1:81949', '1:85011', '1:95754', '1:97288', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A441E47-060B-EA11-B8B7-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/163322C0-3913-EA11-A823-509A4C730E32.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40429EB5-3913-EA11-8322-0CC47A4D7654.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B830E40B-4BFA-E911-AA8B-00259048AD6A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6A82999A-100B-EA11-A7F8-0025905A60A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E82B862B-29FD-E911-AE56-509A4C9F8888.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/826B13CB-B4FC-E911-8A17-509A4C9EF8EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2668A328-EA06-EA11-BCB2-0CC47A5FC2A1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D2A86121-C901-EA11-8DD5-509A4C9EF8FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/303FC9AB-D400-EA11-BF9F-38EAA78D8ADC.root']);