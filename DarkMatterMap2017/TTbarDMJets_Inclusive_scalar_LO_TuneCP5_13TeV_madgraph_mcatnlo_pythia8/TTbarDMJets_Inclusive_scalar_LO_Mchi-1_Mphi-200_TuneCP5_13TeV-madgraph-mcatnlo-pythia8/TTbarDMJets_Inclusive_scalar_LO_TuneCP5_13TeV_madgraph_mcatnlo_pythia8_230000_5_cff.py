import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:3410', '1:33208', '1:33258', '1:36576', '1:52304', '1:58923', '1:34661', '1:40004', '1:24105', '1:39062', '1:39255', '1:46092', '1:49722', '1:32871', '1:35350', '1:10805', '1:13578', '1:14241', '1:14418', '1:62382', '1:100867', '1:102145', '1:102148', '1:9793', '1:16861', '1:20610', '1:55547', '1:54630', '1:54840', '1:62328', '1:63642', '1:63724', '1:67450', '1:72238', '1:70900', '1:71507', '1:13941', '1:55527', '1:75322', '1:88754', '1:89187', '1:91874', '1:64018', '1:63601', '1:68261', '1:69565', '1:85628', '1:91473', '1:91485', '1:91929', '1:91803', '1:87869', '1:89287', '1:89920', '1:88344', '1:79629', '1:79233', '1:81291', '1:80222', '1:80914', '1:81113', '1:81228', '1:72526', '1:72615', '1:75587', '1:80256', '1:86940', '1:87554', '1:89096', '1:16879', '1:20343', '1:58527', '1:59219', '1:59507', '1:6228', '1:34902', '1:60860', '1:69715', '1:80003', '1:88788', '1:71764', '1:57855', '1:51912', '1:52090', '1:97964', '1:98488', '1:62441', '1:74888', '1:87589', '1:88093', '1:101388', '1:79722', '1:85983', '1:86563', '1:88480', '1:88496', '1:95327', '1:96119', '1:87829', '1:95803', '1:91470', '1:95743', '1:96568', '1:96585', '1:96748', '1:35904', '1:37242', '1:37445', '1:38014', '1:67560', '1:72763', '1:74601', '1:71098', '1:78582', '1:81177', '1:89231', '1:94268', '1:5233', '1:102342', '1:96581', '1:85681', '1:99985', '1:14034', '1:67594', '1:88692', '1:100177', '1:95260', '1:95368', '1:4706', '1:4933', '1:5605', '1:5796', '1:101921', '1:86378', '1:20441', '1:27169', '1:81533', '1:90173', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/663C015C-090B-EA11-BFB8-0CC47A4D761A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C1F2C40-140B-EA11-B0C9-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50E09B46-0F0B-EA11-B430-0CC47A7C353E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/00B4F279-060B-EA11-B0D5-44A842CFD64D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/42F08944-8A0B-EA11-81BC-0CC47A4D7670.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3CFE5F00-040C-EA11-BAEC-FA163E1C0945.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4429EB0E-E00D-EA11-864F-A4BF01287D43.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/86A930BC-3913-EA11-B2E6-6CC2173BC990.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/12FDBADE-3913-EA11-8539-001E67580724.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/14B38BBF-3913-EA11-82EE-141877410522.root']);