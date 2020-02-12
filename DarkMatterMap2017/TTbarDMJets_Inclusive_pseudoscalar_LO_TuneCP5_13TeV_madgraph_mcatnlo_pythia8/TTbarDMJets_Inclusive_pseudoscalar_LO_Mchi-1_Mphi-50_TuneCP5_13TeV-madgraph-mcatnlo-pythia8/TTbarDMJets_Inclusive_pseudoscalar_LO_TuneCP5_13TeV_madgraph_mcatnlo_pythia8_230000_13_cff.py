import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:43999', '1:41725', '1:44826', '1:47532', '1:47572', '1:47783', '1:49912', '1:22891', '1:27222', '1:28555', '1:39607', '1:72403', '1:79746', '1:57703', '1:57713', '1:57795', '1:58145', '1:58276', '1:58289', '1:58306', '1:58492', '1:58527', '1:58761', '1:58783', '1:59041', '1:59055', '1:62071', '1:62260', '1:62307', '1:62316', '1:62446', '1:62520', '1:62527', '1:62623', '1:62642', '1:62682', '1:62738', '1:62859', '1:62074', '1:62590', '1:72407', '1:89855', '1:96842', '1:91691', '1:95123', '1:95273', '1:96042', '1:21476', '1:21735', '1:27345', '1:27574', '1:91225', '1:91881', '1:91897', '1:92985', '1:94041', '1:94578', '1:96093', '1:97879', '1:101762', '1:101772', '1:15563', '1:15993', '1:41017', '1:43731', '1:46834', '1:48470', '1:49397', '1:45822', '1:47121', '1:47177', '1:47418', '1:47866', '1:46004', '1:46142', '1:46162', '1:46177', '1:46189', '1:46230', '1:46106', '1:104437', '1:101685', '1:104776', '1:24054', '1:20167', '1:20183', '1:20233', '1:20256', '1:20430', '1:20519', '1:20639', '1:20783', '1:48629', '1:48815', '1:48373', '1:49064', '1:49074', '1:49389', '1:49632', '1:49648', '1:49768', '1:49834', '1:85584', '1:96344', '1:97768', '1:32126', '1:42268', '1:42484', '1:65133', '1:65406', '1:65578', '1:66001', '1:71298', '1:79608', '1:79691', '1:80215', '1:76640', '1:80638', '1:94270', '1:94457', '1:94507', '1:94529', '1:94562', '1:94586', '1:94664', '1:94767', '1:94769', '1:94805', '1:95032', '1:95064', '1:60741', '1:67308', '1:73257', '1:74358', '1:78802', '1:64127', '1:65636', '1:73568', '1:64114', '1:67688', '1:81270', '1:81780', '1:66812', '1:96525', '1:83555', '1:83584', '1:83732', '1:83746', '1:83805', '1:83819', '1:83883', '1:83993', '1:86029', '1:86077', '1:86183', '1:90027', '1:85849', '1:82781', '1:88210', '1:88304', '1:70085', '1:70513', '1:70611', '1:70636', '1:70745', '1:80090', '1:80334', '1:80504', '1:80570', '1:80763', '1:92513', '1:92641', '1:92666', '1:92837', '1:92853', '1:93128', '1:93210', '1:93267', '1:93298', '1:93413', '1:93494', '1:98212', '1:98369', '1:98638', '1:98723', '1:98855', '1:103019', '1:103021', '1:103078', '1:103180', '1:97368', '1:97647', '1:97889', '1:97996', '1:98043', '1:98051', '1:6997', '1:7756', '1:7789', '1:7990', '1:8060', '1:8148', '1:8943', '1:9223', '1:9764', '1:10007', '1:17155', '1:17408', '1:12771', '1:12782', '1:12904', '1:13284', '1:13520', '1:13843', '1:13863', '1:13462', '1:13752', '1:14614', '1:14474', '1:14604', '1:46367', '1:46387', '1:46501', '1:46529', '1:46759', '1:46959', '1:48075', '1:48642', '1:20038', '1:20065', '1:20071', '1:20159', '1:20201', '1:20305', '1:20308', '1:20362', '1:17050', '1:17070', '1:17075', '1:17078', '1:17112', '1:17156', '1:17167', '1:17187', '1:24338', '1:20980', '1:21094', '1:23515', '1:23572', '1:23696', '1:21197', '1:21320', '1:21386', '1:21601', '1:21669', '1:26250', '1:23343', '1:23704', '1:23717', '1:23941', '1:23972', '1:15080', '1:15318', '1:16240', '1:16590', '1:19061', '1:18013', '1:18066', '1:18110', '1:18156', '1:18158', '1:18202', '1:18205', '1:18216', '1:18224', '1:18239', '1:18190', '1:18402', '1:18435', '1:18482', '1:18483', '1:18714', '1:23552', '1:23802', '1:27622', '1:27646', '1:27702', '1:27750', '1:27751', '1:27792', '1:27840', '1:27945', '1:27999', '1:28326', '1:76448', '1:76468', '1:76537', '1:76575', '1:76588', '1:76589', '1:76599', '1:76650', '1:76655', '1:76658', '1:76519', '1:76527', '1:76592', '1:76612', '1:76947', '1:84340', '1:84341', '1:85959', '1:88474', '1:88733', '1:89097', '1:89121', '1:91426', '1:91475', '1:91543', '1:91553', '1:91699', '1:91742', '1:92839', '1:94111', '1:94153', '1:94113', '1:55767', '1:55783', '1:55828', '1:55882', '1:55913', '1:55916', '1:55926', '1:55956', '1:55963', '1:55964', '1:55990', '1:56024', '1:56030', '1:56032', '1:56111', '1:56235', '1:56296', '1:56384', '1:74753', '1:75266', '1:62964', '1:64058', '1:64100', '1:64110', '1:64254', '1:64287', '1:64417', '1:64481', '1:64652', '1:64674', '1:75665', '1:75699', '1:75835', '1:75942', '1:76018', '1:76065', '1:76252', '1:76315', '1:76535', '1:76858', '1:76996', '1:56493', '1:56507', '1:56515', '1:56529', '1:56532', '1:56541', '1:56714', '1:56914', '1:57011', '1:76665', '1:76683', '1:76692', '1:76707', '1:76822', '1:76827', '1:76884', '1:76921', '1:80115', '1:80142', '1:80149', '1:80154', '1:79830', '1:79845', '1:79854', '1:79909', '1:79940', '1:80059', '1:80261', '1:80269', '1:80318', '1:80324', '1:80333', '1:80447', '1:80546', '1:80578', '1:80676', '1:80820', '1:76063', '1:76908', '1:79993', '1:49717', '1:49784', '1:49728', '1:49743', '1:49761', '1:49763', '1:49773', '1:49786', '1:49903', '1:49930', '1:97021', '1:96737', '1:96753', '1:96853', '1:97209', '1:98321', '1:98322', '1:98666', '1:98703', '1:103126', '1:103178', '1:101124', '1:101136', '1:101152', '1:101201', '1:101207', '1:101315', '1:101439', '1:101442', '1:101448', '1:101513', '1:97429', '1:87615', '1:87706', '1:87451', '1:87795', '1:87852', '1:87996', '1:88017', '1:88142', '1:88200', '1:94337', '1:101995', '1:104903', '1:104999', '1:11736', '1:11744', '1:12012', '1:12409', '1:12643', '1:14721', '1:28061', '1:41081', '1:41381', '1:41485', '1:41751', '1:41910', '1:41978', '1:42079', '1:43907', '1:46083', '1:46420', '1:46630', '1:46679', '1:46751', '1:46914', '1:48200', '1:46468', '1:19561', '1:19646', '1:19652', '1:19709', '1:19743', '1:19746', '1:19840', '1:19854', '1:19884', '1:19900', '1:21768', '1:26291', '1:26331', '1:26333', '1:26350', '1:26363', '1:26422', '1:26434', '1:26470', '1:26535', '1:26402', '1:26598', '1:26645', '1:26707', '1:26724', '1:26657', '1:43463', '1:43464', '1:43467', '1:43483', '1:43493', '1:43634', '1:43659', '1:43681', '1:43683', '1:43687', '1:44001', '1:44211', '1:44268', '1:44315', '1:44517', '1:43802', '1:43812', '1:43813', '1:43948', '1:51584', '1:51948', '1:52629', '1:52880', '1:52927', '1:53132', '1:53151', '1:53192', '1:53277', '1:53280', '1:53296', '1:53312', '1:53767', '1:53824', '1:10875', '1:8881', '1:8905', '1:11050', '1:11946', '1:12468', '1:15826', '1:15940', '1:13980', '1:14118', '1:14766', '1:15103', '1:15896', '1:27022', '1:23057', '1:51264', '1:53282', '1:53412', '1:54593', '1:54829', '1:55998', '1:57048', '1:73636', '1:74385', '1:75032', '1:75074', '1:76817', '1:76833', '1:73005', '1:73169', '1:73668', '1:73757', '1:75683', '1:65365', '1:72803', '1:75001', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96B475A8-45F7-E911-A1D4-002590E7D7E2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4056591E-F209-EA11-A699-44A842CFD5BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/006C1B93-29F3-E911-9D2E-6C2B598FF86B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E90CC6C-9A07-EA11-9BAF-0CC47A7C3432.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/463016DD-5DFC-E911-A3BD-0CC47AFCC69E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCD2DC78-350F-EA11-A934-509A4C9F8A8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/36068975-BBFA-E911-8ED3-509A4C9EF923.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C6AA3D6D-A7FB-E911-B199-40F2E9C6ADBA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C4F880FC-64FC-E911-9F1D-0CC47AFF0188.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72568A99-5504-EA11-9A4E-14187764311A.root']);