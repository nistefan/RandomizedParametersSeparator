import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:74306', '1:75767', '1:72325', '1:97474', '1:97622', '1:97639', '1:97682', '1:97718', '1:97723', '1:97841', '1:96007', '1:39086', '1:39246', '1:39452', '1:50550', '1:50553', '1:50644', '1:87109', '1:87663', '1:86900', '1:26244', '1:26247', '1:26263', '1:26277', '1:26325', '1:26302', '1:26436', '1:26444', '1:73847', '1:84682', '1:84713', '1:84850', '1:84959', '1:98929', '1:99365', '1:100393', '1:100641', '1:100886', '1:100694', '1:15997', '1:17091', '1:12725', '1:14807', '1:14629', '1:16160', '1:16924', '1:17554', '1:15675', '1:60767', '1:61022', '1:61903', '1:61993', '1:62201', '1:62234', '1:62302', '1:21880', '1:21504', '1:21507', '1:24354', '1:94161', '1:38078', '1:38597', '1:35214', '1:98390', '1:98833', '1:102930', '1:103130', '1:102994', '1:103714', '1:26741', '1:27239', '1:27248', '1:28259', '1:28013', '1:33960', '1:35562', '1:35685', '1:37633', '1:37974', '1:51183', '1:55275', '1:56182', '1:37140', '1:37560', '1:37721', '1:37746', '1:38839', '1:42447', '1:67294', '1:68065', '1:68352', '1:64688', '1:66077', '1:66728', '1:66504', '1:70234', '1:60326', '1:103893', '1:64998', '1:51264', '1:50815', '1:56276', '1:57213', '1:58673', '1:58750', '1:58913', '1:59814', '1:27678', '1:37481', '1:37734', '1:83055', '1:84159', '1:45531', '1:45636', '1:46989', '1:71458', '1:73671', '1:73931', '1:74564', '1:50075', '1:99501', '1:103046', '1:103302', '1:64620', '1:70154', '1:88130', '1:64347', '1:64487', '1:65998', '1:98550', '1:3895', '1:3899', '1:4210', '1:63103', '1:50795', '1:50890', '1:50927', '1:51482', '1:60977', '1:60117', '1:60179', '1:60543', '1:60586', '1:61638', '1:62369', '1:62394', '1:61875', '1:91234', '1:91695', '1:105920', '1:86847', '1:87065', '1:87723', '1:100968', '1:102001', '1:102051', '1:100911', '1:220', '1:221', '1:269', '1:1544', '1:627', '1:897', '1:898', '1:912', '1:933', '1:2146', '1:2611', '1:1620', '1:1843', '1:1929', '1:1961', '1:4395', '1:18902', '1:18919', '1:18976', '1:18977', '1:20009', '1:44664', '1:52363', '1:14436', '1:14560', '1:14662', '1:14663', '1:14711', '1:14718', '1:15011', '1:55537', '1:56642', '1:57136', '1:57194', '1:56620', '1:56854', '1:56985', '1:92210', '1:92216', '1:92258', '1:92275', '1:92308', '1:92361', '1:3397', '1:2692', '1:2763', '1:2980', '1:42233', '1:5730', '1:5794', '1:5830', '1:5841', '1:5819', '1:5919', '1:5963', '1:14859', '1:15105', '1:17592', '1:17815', '1:17822', '1:44530', '1:44533', '1:52561', '1:53064', '1:56116', '1:54023', '1:54149', '1:56589', '1:63196', '1:63717', '1:60828', '1:64714', '1:64924', '1:63420', '1:63776', '1:63374', '1:67237', '1:91934', '1:91963', '1:91979', '1:94232', '1:94237', '1:94264', '1:95767', '1:95954', '1:64969', '1:65455', '1:64355', '1:64423', '1:64473', '1:78452', '1:78632', '1:78746', '1:81446', '1:88411', '1:81840', '1:81853', '1:81861', '1:95286', '1:95304', '1:95421', '1:95436', '1:95437', '1:95442', '1:95623', '1:95632', '1:95704', '1:95731', '1:97530', '1:99119', '1:98312', '1:98190', '1:98703', '1:99212', '1:7675', '1:7871', '1:8047', '1:8058', '1:8316', '1:8323', '1:8423', '1:8769', '1:8815', '1:8830', '1:9325', '1:14852', '1:12880', '1:17724', '1:18416', '1:19981', '1:27790', '1:24217', '1:24333', '1:33287', '1:33800', '1:24448', '1:24299', '1:24666', '1:24817', '1:27097', '1:27529', '1:26463', '1:26635', '1:26650', '1:27806', '1:47694', '1:40515', '1:48116', '1:48501', '1:47517', '1:83290', '1:87168', '1:88036', '1:1988', '1:7758', '1:10524', '1:12278', '1:12889', '1:16945', '1:9963', '1:16364', '1:16659', '1:19507', '1:21235', '1:24163', '1:34739', '1:26702', '1:34579', '1:1417', '1:1459', '1:1475', '1:1480', '1:7167', '1:7224', '1:7282', '1:7330', '1:7371', '1:7445', '1:8215', '1:8339', '1:8348', '1:9223', '1:8191', '1:42563', '1:37336', '1:99512', '1:99686', '1:99700', '1:79459', '1:79431', '1:79486', '1:86035', '1:87129', '1:104', '1:670', '1:978', '1:1647', '1:1842', '1:17332', '1:18417', '1:20578', '1:20593', '1:21126', '1:19189', '1:21072', '1:21829', '1:2033', '1:2154', '1:2156', '1:2373', '1:2379', '1:2461', '1:2512', '1:3876', '1:2255', '1:2548', '1:4561', '1:26805', '1:26851', '1:28678', '1:26513', '1:32616', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E28438A7-4910-EA11-910C-40F2E9C6AE26.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA25B1CE-CEF6-E911-B53C-246E96D14B5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/64F51C16-E1F6-E911-B326-B499BAAC03BA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC7BC4C4-EBEF-E911-9B75-002590D9D8B8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2443D33F-8B0E-EA11-B3DB-6CC2173D44D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38867EE3-18EF-E911-ADE7-B8CA3A70A520.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DA35E849-52F8-E911-8ABB-002590D4FC5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A43B4BF7-9B0F-EA11-864B-509A4C84D1B1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5C477F16-6DFF-E911-BE38-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0EF3BEDD-37EE-E911-9652-089E0158CD57.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CECB7F44-C3F2-E911-8EFE-AC162DA6E2F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60FDD590-16F8-E911-89B9-003048F5B69E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CA9067BE-EBED-E911-A5CA-98039B3B0182.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/ACFC8763-7B04-EA11-A589-6CC2173C39E0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DA8DAF0B-9FED-E911-A23B-E0071B6CAD20.root']);