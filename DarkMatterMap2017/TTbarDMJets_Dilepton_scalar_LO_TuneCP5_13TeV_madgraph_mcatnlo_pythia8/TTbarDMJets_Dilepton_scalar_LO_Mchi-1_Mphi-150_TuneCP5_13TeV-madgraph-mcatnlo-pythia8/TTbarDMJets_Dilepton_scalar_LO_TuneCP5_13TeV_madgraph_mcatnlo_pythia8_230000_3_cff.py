import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:19706', '1:19781', '1:19802', '1:19836', '1:27204', '1:27657', '1:34784', '1:34896', '1:36379', '1:36417', '1:36425', '1:36577', '1:43028', '1:33278', '1:33156', '1:28503', '1:28698', '1:28760', '1:28804', '1:28866', '1:33389', '1:33455', '1:33640', '1:33906', '1:33954', '1:33968', '1:33553', '1:33697', '1:33701', '1:33729', '1:24682', '1:35774', '1:36947', '1:43355', '1:46450', '1:50005', '1:94840', '1:88275', '1:91068', '1:91073', '1:91350', '1:40166', '1:44609', '1:44633', '1:44635', '1:43540', '1:45758', '1:50374', '1:50515', '1:58484', '1:58519', '1:58566', '1:58414', '1:59010', '1:59022', '1:58265', '1:58361', '1:87135', '1:87137', '1:88146', '1:88291', '1:1224', '1:1269', '1:1402', '1:1346', '1:3258', '1:3348', '1:3351', '1:28852', '1:28894', '1:28998', '1:38158', '1:39503', '1:40701', '1:40944', '1:43438', '1:44066', '1:44093', '1:44119', '1:44216', '1:45059', '1:45091', '1:19648', '1:21771', '1:15691', '1:69757', '1:70196', '1:70894', '1:71896', '1:72092', '1:72838', '1:75025', '1:72415', '1:75990', '1:66763', '1:70047', '1:70498', '1:71186', '1:73132', '1:66012', '1:64046', '1:64886', '1:69867', '1:65280', '1:66707', '1:68530', '1:69518', '1:99481', '1:99523', '1:74114', '1:96093', '1:20438', '1:20630', '1:21858', '1:24245', '1:24582', '1:24086', '1:28168', '1:56839', '1:26213', '1:28158', '1:72559', '1:74574', '1:72686', '1:82238', '1:82327', '1:82289', '1:82349', '1:82356', '1:84011', '1:92083', '1:100411', '1:97403', '1:93728', '1:93677', '1:93695', '1:48497', '1:48526', '1:48583', '1:48625', '1:53732', '1:55183', '1:55763', '1:55777', '1:56095', '1:56137', '1:56143', '1:81328', '1:91313', '1:91430', '1:91432', '1:91634', '1:94085', '1:94136', '1:92411', '1:93035', '1:100592', '1:102365', '1:95992', '1:96115', '1:104825', '1:99746', '1:100168', '1:100195', '1:100130', '1:100154', '1:106197', '1:106324', '1:74585', '1:65192', '1:70491', '1:73446', '1:95305', '1:95317', '1:95325', '1:95337', '1:95394', '1:95508', '1:95513', '1:95519', '1:95563', '1:95672', '1:95679', '1:100115', '1:104241', '1:104246', '1:104299', '1:104316', '1:105935', '1:105963', '1:106133', '1:105888', '1:106226', '1:49913', '1:50031', '1:50087', '1:50282', '1:50363', '1:50365', '1:50375', '1:50589', '1:50884', '1:64050', '1:64200', '1:61548', '1:62022', '1:61973', '1:95955', '1:96212', '1:96223', '1:96128', '1:96248', '1:96420', '1:96451', '1:62702', '1:62709', '1:72925', '1:74744', '1:81715', '1:82119', '1:82214', '1:96430', '1:67510', '1:67530', '1:67536', '1:67803', '1:67813', '1:84518', '1:83701', '1:83708', '1:85035', '1:85188', '1:94683', '1:99999', '1:100403', '1:20933', '1:24527', '1:52302', '1:52326', '1:52412', '1:52416', '1:52595', '1:53026', '1:53058', '1:53359', '1:55904', '1:55926', '1:78955', '1:78983', '1:78999', '1:39379', '1:39457', '1:39548', '1:39757', '1:39900', '1:40798', '1:62971', '1:76631', '1:76650', '1:76671', '1:76704', '1:76868', '1:76964', '1:76715', '1:76724', '1:76750', '1:76777', '1:99836', '1:100570', '1:100597', '1:78703', '1:78837', '1:79090', '1:80091', '1:38460', '1:42024', '1:42149', '1:42208', '1:42257', '1:42418', '1:42476', '1:42748', '1:41680', '1:50921', '1:50990', '1:51013', '1:51218', '1:96263', '1:98316', '1:97006', '1:99505', '1:88669', '1:88835', '1:88968', '1:104440', '1:19935', '1:61867', '1:62062', '1:62143', '1:62312', '1:65951', '1:64237', '1:64518', '1:64536', '1:65153', '1:65558', '1:81165', '1:81570', '1:65141', '1:65369', '1:65523', '1:65360', '1:65457', '1:65509', '1:65622', '1:65663', '1:65745', '1:65769', '1:98834', '1:70740', '1:71390', '1:91736', '1:94055', '1:94060', '1:93256', '1:17997', '1:18073', '1:27776', '1:17987', '1:19783', '1:24262', '1:19597', '1:24504', '1:52051', '1:52452', '1:57718', '1:65019', '1:66805', '1:69604', '1:83016', '1:80986', '1:82806', '1:84405', '1:78246', '1:79278', '1:80620', '1:80935', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/147D2FEE-7AF4-E911-AC32-FA163ED45046.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8D1CA51-35F3-E911-A13A-7CD30AD09C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/408D623C-B5F2-E911-BEF8-FA163EEBFC01.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B49C1D82-4EF3-E911-9E50-842B2B6AEA0E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4E56313-21F4-E911-B492-1866DA7F9419.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94284CBD-36F4-E911-88E6-A4BF012835C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AB8635C-CDF5-E911-B092-FA163EF38280.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/42C14BE8-BDF6-E911-95B1-AC1F6B56768A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7602BEA4-33F6-E911-95A7-FA163EB69FE7.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B87F77FB-EAF6-E911-A351-0090FAA57A00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E27EC42F-BBF9-E911-9830-B083FED429D5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38B76DAF-36F9-E911-9F0F-001F29089F68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B02AB0B8-ADFA-E911-BDE6-44A842CFD667.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92B1133B-96FA-E911-99FE-FA163E3BEC96.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C990481-CCF8-E911-B595-008CFAE45404.root']);