import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:35195', '1:44751', '1:47709', '1:39345', '1:41668', '1:44663', '1:47609', '1:50001', '1:54765', '1:56316', '1:56532', '1:56794', '1:53421', '1:54808', '1:54817', '1:55330', '1:57079', '1:55805', '1:68567', '1:69104', '1:80820', '1:82872', '1:82292', '1:82733', '1:82766', '1:86157', '1:86560', '1:73618', '1:93667', '1:94580', '1:95088', '1:99315', '1:19042', '1:20947', '1:18596', '1:21430', '1:24353', '1:49666', '1:76272', '1:76400', '1:76657', '1:76941', '1:81309', '1:99109', '1:95816', '1:98898', '1:103177', '1:26216', '1:26408', '1:28240', '1:28557', '1:28816', '1:32599', '1:26295', '1:32414', '1:56150', '1:56346', '1:57133', '1:57666', '1:57935', '1:63626', '1:67822', '1:67625', '1:67798', '1:68128', '1:102873', '1:32123', '1:32212', '1:71429', '1:72011', '1:72162', '1:72555', '1:74637', '1:75124', '1:85797', '1:86753', '1:87793', '1:97372', '1:64447', '1:69768', '1:62124', '1:67241', '1:69204', '1:69232', '1:77953', '1:79098', '1:84096', '1:80410', '1:81083', '1:81115', '1:81555', '1:94306', '1:99882', '1:33887', '1:34837', '1:35138', '1:35164', '1:35168', '1:57304', '1:40149', '1:42969', '1:45890', '1:47045', '1:42168', '1:42243', '1:58444', '1:59002', '1:58830', '1:58838', '1:58867', '1:59170', '1:58642', '1:58687', '1:58742', '1:58747', '1:74199', '1:72638', '1:34006', '1:34183', '1:34577', '1:37943', '1:39508', '1:39939', '1:40202', '1:42000', '1:48422', '1:48555', '1:106206', '1:104472', '1:104540', '1:106339', '1:15124', '1:14701', '1:14913', '1:14987', '1:96464', '1:97030', '1:98503', '1:98949', '1:105721', '1:105723', '1:106016', '1:106019', '1:17675', '1:17758', '1:17768', '1:17771', '1:20351', '1:20583', '1:20585', '1:38409', '1:72754', '1:72792', '1:72817', '1:72886', '1:72930', '1:75302', '1:79311', '1:79552', '1:79585', '1:79624', '1:5871', '1:52184', '1:60843', '1:65286', '1:66583', '1:67999', '1:71311', '1:18615', '1:14623', '1:18678', '1:20640', '1:20109', '1:51383', '1:4386', '1:5555', '1:10159', '1:12475', '1:50096', '1:50546', '1:53102', '1:48516', '1:45102', '1:47655', '1:58054', '1:67674', '1:59703', '1:54637', '1:33891', '1:34370', '1:34874', '1:34905', '1:37016', '1:35732', '1:35973', '1:27542', '1:28314', '1:34726', '1:86993', '1:87778', '1:39504', '1:44166', '1:35192', '1:26872', '1:32846', '1:34422', '1:35462', '1:35657', '1:38096', '1:42763', '1:42856', '1:46144', '1:76040', '1:77961', '1:78980', '1:81025', '1:38', '1:73', '1:1002', '1:1624', '1:1882', '1:104670', '1:100384', '1:48578', '1:48622', '1:49493', '1:45354', '1:46992', '1:97973', '1:100037', '1:104123', '1:106349', '1:28058', '1:28144', '1:28187', '1:28215', '1:58865', '1:67230', '1:67426', '1:64130', '1:106297', '1:97549', '1:104098', '1:106299', '1:66462', '1:71767', '1:71882', '1:70430', '1:73732', '1:67586', '1:65191', '1:69892', '1:83274', '1:100230', '1:104589', '1:104775', '1:103285', '1:5862', '1:9407', '1:8121', '1:8331', '1:9280', '1:9613', '1:34756', '1:32091', '1:32619', '1:34094', '1:34351', '1:34493', '1:34585', '1:34724', '1:34960', '1:99049', '1:99157', '1:98872', '1:38193', '1:38722', '1:42959', '1:43643', '1:46151', '1:46172', '1:46744', '1:45713', '1:45144', '1:46567', '1:47690', '1:40604', '1:44746', '1:47169', '1:92198', '1:85393', '1:85496', '1:85779', '1:85683', '1:85732', '1:85792', '1:85809', '1:85858', '1:85865', '1:85877', '1:104796', '1:102877', '1:100385', '1:98602', '1:98640', '1:98645', '1:100511', '1:52972', '1:65726', '1:71489', '1:72161', '1:97167', '1:99367', '1:99537', '1:40091', '1:43273', '1:88501', '1:91375', '1:92391', '1:103862', '1:104029', '1:104218', '1:64751', '1:65617', '1:65675', '1:65709', '1:66124', '1:66162', '1:66202', '1:80385', '1:64594', '1:65318', '1:65517', '1:52825', '1:52975', '1:53093', '1:105476', '1:100458', '1:103710', '1:88898', '1:94435', '1:95266', '1:96926', '1:56076', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE6DCC6F-9702-EA11-8C9E-246E96D14D4C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/629AE047-9B03-EA11-AF08-0090FAA57770.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/74BFCEF5-7203-EA11-AC31-00259073E53A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8D6CEA6-5D03-EA11-9F3D-D48564593FA8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FED7A530-8703-EA11-9953-008CFAF28F22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4AC458D-3904-EA11-819B-0CC47AFF02CC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5AD9493D-D803-EA11-A326-002481CFE864.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8B96E8C-1B0B-EA11-B3FA-0CC47A4D75F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/548DD76C-8E0A-EA11-A159-0CC47A4C8E0E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4C7CE199-7F0A-EA11-B6D3-AC1F6BAC7EAC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A61B1E1C-3C0E-EA11-ADCF-506B4BB134E6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA16D4FD-B40E-EA11-AA73-AC1F6B1AEF94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E5B1D6C-8F0B-EA11-A380-FA163E1B56E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/06492256-3210-EA11-93C2-44A842BFA94B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D8A4A322-940F-EA11-9A4C-1CC1DE050110.root']);