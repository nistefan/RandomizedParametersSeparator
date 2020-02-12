import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:34232', '1:32659', '1:34100', '1:47307', '1:47538', '1:39481', '1:47679', '1:47986', '1:48297', '1:52678', '1:56311', '1:50222', '1:50707', '1:54215', '1:54738', '1:54045', '1:55379', '1:58472', '1:61404', '1:74984', '1:75567', '1:76098', '1:80890', '1:84177', '1:84210', '1:82374', '1:85512', '1:78041', '1:79185', '1:81882', '1:94206', '1:95593', '1:97144', '1:96991', '1:99173', '1:18708', '1:19596', '1:19693', '1:21696', '1:24619', '1:54279', '1:75473', '1:76473', '1:76845', '1:95198', '1:98102', '1:100525', '1:100541', '1:32500', '1:26700', '1:28527', '1:54320', '1:55961', '1:56141', '1:57248', '1:56038', '1:63122', '1:67233', '1:68363', '1:100267', '1:33888', '1:37397', '1:72019', '1:75081', '1:75639', '1:77218', '1:85644', '1:85703', '1:87370', '1:87942', '1:87936', '1:59955', '1:64752', '1:68994', '1:69670', '1:69946', '1:67720', '1:67884', '1:72250', '1:84739', '1:79394', '1:96348', '1:18534', '1:18540', '1:18552', '1:18610', '1:18851', '1:33763', '1:33966', '1:34102', '1:35119', '1:46443', '1:42175', '1:42264', '1:58510', '1:58855', '1:58601', '1:74527', '1:75240', '1:72607', '1:32213', '1:32915', '1:34038', '1:34045', '1:35622', '1:37405', '1:39055', '1:44598', '1:44896', '1:47689', '1:41783', '1:45359', '1:106109', '1:106152', '1:104649', '1:106162', '1:106222', '1:104866', '1:104800', '1:15095', '1:15115', '1:14749', '1:14771', '1:14779', '1:14790', '1:14951', '1:14984', '1:96626', '1:98284', '1:105717', '1:105827', '1:105834', '1:105864', '1:106163', '1:17652', '1:17645', '1:17723', '1:17813', '1:17921', '1:17939', '1:20605', '1:20632', '1:20637', '1:20673', '1:20781', '1:20795', '1:20878', '1:72572', '1:72752', '1:75020', '1:75046', '1:75322', '1:75332', '1:79335', '1:79537', '1:79625', '1:899', '1:2014', '1:15608', '1:28782', '1:58244', '1:63240', '1:104961', '1:21397', '1:21713', '1:18651', '1:20439', '1:19437', '1:44262', '1:52596', '1:48804', '1:50225', '1:7903', '1:9097', '1:48425', '1:51327', '1:51439', '1:44228', '1:47860', '1:48290', '1:50807', '1:62763', '1:63825', '1:58092', '1:60593', '1:61511', '1:67033', '1:36237', '1:33855', '1:35537', '1:35202', '1:21998', '1:32235', '1:34296', '1:47973', '1:48233', '1:50431', '1:83807', '1:35507', '1:35603', '1:37985', '1:26904', '1:33193', '1:34347', '1:35824', '1:36478', '1:42693', '1:42762', '1:76461', '1:77120', '1:78405', '1:78487', '1:81079', '1:112', '1:1018', '1:1473', '1:103815', '1:106003', '1:51135', '1:51138', '1:45436', '1:45662', '1:45383', '1:47452', '1:58886', '1:26516', '1:26838', '1:26850', '1:28044', '1:26811', '1:62904', '1:63370', '1:69910', '1:64271', '1:64469', '1:69948', '1:87061', '1:87553', '1:105356', '1:106066', '1:105025', '1:65330', '1:66582', '1:66880', '1:70540', '1:71503', '1:65170', '1:66841', '1:69381', '1:69998', '1:77942', '1:92263', '1:104471', '1:105919', '1:105743', '1:104330', '1:103401', '1:105332', '1:4069', '1:7295', '1:8842', '1:12171', '1:33475', '1:32191', '1:32303', '1:35855', '1:93925', '1:97879', '1:100512', '1:45124', '1:46765', '1:69803', '1:43960', '1:46687', '1:39878', '1:40100', '1:44732', '1:44805', '1:44834', '1:39214', '1:47539', '1:47660', '1:88736', '1:94032', '1:82459', '1:83175', '1:83265', '1:85468', '1:85472', '1:82343', '1:84459', '1:84671', '1:85705', '1:85708', '1:85845', '1:85881', '1:102465', '1:102892', '1:98260', '1:98529', '1:98547', '1:98576', '1:98629', '1:98632', '1:100491', '1:69699', '1:39890', '1:49137', '1:94614', '1:104357', '1:105453', '1:64609', '1:66099', '1:66115', '1:66210', '1:80388', '1:64893', '1:65528', '1:50261', '1:52850', '1:102421', '1:105646', '1:106105', '1:106327', '1:105509', '1:105628', '1:105667', '1:105803', '1:105958', '1:94520', '1:54187', '1:58388', '1:58632', '1:58752', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE6DCC6F-9702-EA11-8C9E-246E96D14D4C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/629AE047-9B03-EA11-AF08-0090FAA57770.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/74BFCEF5-7203-EA11-AC31-00259073E53A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8D6CEA6-5D03-EA11-9F3D-D48564593FA8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FED7A530-8703-EA11-9953-008CFAF28F22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4AC458D-3904-EA11-819B-0CC47AFF02CC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5AD9493D-D803-EA11-A326-002481CFE864.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8B96E8C-1B0B-EA11-B3FA-0CC47A4D75F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/548DD76C-8E0A-EA11-A159-0CC47A4C8E0E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4C7CE199-7F0A-EA11-B6D3-AC1F6BAC7EAC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A61B1E1C-3C0E-EA11-ADCF-506B4BB134E6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA16D4FD-B40E-EA11-AA73-AC1F6B1AEF94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E5B1D6C-8F0B-EA11-A380-FA163E1B56E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/06492256-3210-EA11-93C2-44A842BFA94B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D8A4A322-940F-EA11-9A4C-1CC1DE050110.root']);