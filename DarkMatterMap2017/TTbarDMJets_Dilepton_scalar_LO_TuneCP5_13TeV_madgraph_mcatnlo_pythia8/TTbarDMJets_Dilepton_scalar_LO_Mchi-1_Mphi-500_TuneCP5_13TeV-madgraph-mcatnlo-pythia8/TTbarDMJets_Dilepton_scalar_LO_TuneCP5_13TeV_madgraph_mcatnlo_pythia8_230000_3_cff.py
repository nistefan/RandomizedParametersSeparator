import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:19657', '1:19692', '1:19718', '1:19733', '1:27714', '1:34477', '1:34481', '1:34771', '1:34777', '1:34856', '1:34901', '1:34916', '1:34933', '1:36877', '1:42071', '1:33116', '1:28604', '1:28610', '1:28660', '1:28835', '1:28840', '1:33559', '1:34830', '1:34047', '1:38236', '1:98328', '1:16255', '1:16630', '1:16634', '1:86521', '1:86582', '1:87496', '1:87777', '1:88255', '1:88382', '1:88403', '1:39499', '1:40808', '1:44676', '1:44684', '1:48617', '1:43841', '1:47156', '1:50940', '1:50396', '1:50539', '1:50607', '1:50636', '1:50960', '1:51021', '1:51125', '1:51223', '1:51231', '1:51247', '1:58235', '1:58403', '1:58897', '1:59149', '1:59162', '1:58348', '1:58275', '1:58316', '1:87161', '1:87164', '1:87251', '1:88191', '1:88271', '1:88283', '1:1367', '1:1440', '1:1347', '1:1361', '1:1386', '1:1452', '1:1509', '1:3281', '1:3734', '1:3818', '1:3825', '1:3244', '1:3268', '1:28843', '1:28896', '1:28914', '1:28949', '1:28928', '1:28971', '1:32010', '1:38293', '1:40769', '1:40863', '1:40905', '1:44092', '1:44098', '1:21129', '1:18193', '1:19584', '1:28291', '1:73422', '1:72419', '1:75680', '1:77651', '1:57632', '1:70929', '1:68759', '1:69226', '1:64459', '1:64777', '1:65452', '1:68129', '1:70880', '1:71094', '1:71327', '1:96634', '1:99007', '1:104244', '1:75740', '1:98720', '1:21902', '1:24650', '1:26724', '1:28488', '1:28007', '1:28135', '1:28377', '1:28865', '1:72233', '1:72832', '1:74634', '1:75481', '1:81893', '1:82321', '1:82324', '1:82261', '1:82482', '1:82603', '1:82777', '1:85561', '1:91721', '1:92008', '1:96537', '1:93738', '1:93862', '1:93584', '1:93619', '1:41458', '1:48610', '1:53758', '1:55547', '1:56198', '1:91305', '1:91323', '1:91362', '1:91369', '1:91522', '1:91519', '1:94068', '1:94086', '1:93034', '1:96381', '1:100589', '1:100723', '1:100818', '1:102172', '1:102245', '1:102549', '1:102682', '1:102738', '1:96119', '1:100134', '1:100162', '1:100175', '1:100190', '1:100244', '1:106215', '1:75159', '1:71669', '1:72592', '1:95356', '1:95522', '1:95684', '1:99307', '1:99362', '1:99388', '1:99526', '1:99704', '1:104285', '1:106089', '1:106103', '1:50275', '1:50337', '1:50346', '1:50439', '1:50482', '1:50705', '1:62955', '1:64073', '1:64079', '1:64095', '1:95966', '1:96097', '1:96455', '1:62621', '1:62890', '1:62895', '1:74863', '1:82125', '1:82133', '1:82134', '1:82206', '1:96456', '1:97356', '1:99941', '1:100387', '1:67662', '1:67810', '1:67876', '1:84515', '1:83862', '1:83867', '1:83924', '1:85151', '1:94627', '1:20810', '1:20945', '1:21671', '1:21673', '1:21714', '1:24028', '1:24460', '1:27260', '1:24644', '1:52431', '1:52967', '1:53314', '1:56312', '1:78979', '1:39558', '1:39763', '1:40787', '1:40828', '1:40876', '1:58739', '1:59128', '1:76699', '1:76761', '1:76776', '1:100594', '1:78685', '1:79596', '1:80158', '1:38459', '1:38854', '1:38934', '1:42431', '1:42488', '1:36615', '1:38573', '1:48122', '1:48635', '1:50352', '1:50478', '1:50543', '1:50560', '1:50662', '1:50699', '1:51496', '1:100352', '1:97758', '1:20779', '1:62572', '1:64530', '1:64229', '1:64257', '1:64353', '1:64569', '1:65087', '1:65577', '1:87555', '1:65134', '1:65304', '1:65508', '1:65535', '1:65633', '1:65650', '1:65744', '1:65544', '1:68504', '1:70391', '1:71291', '1:71374', '1:94065', '1:17975', '1:21698', '1:21744', '1:20914', '1:50800', '1:51151', '1:51561', '1:52158', '1:52199', '1:52205', '1:52218', '1:52971', '1:58095', '1:69417', '1:64460', '1:84090', '1:80484', '1:80609', '1:84111', '1:86414', '1:88794', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/147D2FEE-7AF4-E911-AC32-FA163ED45046.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8D1CA51-35F3-E911-A13A-7CD30AD09C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/408D623C-B5F2-E911-BEF8-FA163EEBFC01.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B49C1D82-4EF3-E911-9E50-842B2B6AEA0E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4E56313-21F4-E911-B492-1866DA7F9419.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94284CBD-36F4-E911-88E6-A4BF012835C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AB8635C-CDF5-E911-B092-FA163EF38280.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/42C14BE8-BDF6-E911-95B1-AC1F6B56768A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7602BEA4-33F6-E911-95A7-FA163EB69FE7.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B87F77FB-EAF6-E911-A351-0090FAA57A00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E27EC42F-BBF9-E911-9830-B083FED429D5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38B76DAF-36F9-E911-9F0F-001F29089F68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B02AB0B8-ADFA-E911-BDE6-44A842CFD667.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92B1133B-96FA-E911-99FE-FA163E3BEC96.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C990481-CCF8-E911-B595-008CFAE45404.root']);