import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:44324', '1:44361', '1:44575', '1:39791', '1:49108', '1:41650', '1:52974', '1:54371', '1:54905', '1:57151', '1:52590', '1:57109', '1:54744', '1:61396', '1:67012', '1:69055', '1:69562', '1:76106', '1:79822', '1:79021', '1:80574', '1:82105', '1:84201', '1:84422', '1:78099', '1:82870', '1:83355', '1:86680', '1:72544', '1:75553', '1:77592', '1:72509', '1:74672', '1:81308', '1:81401', '1:76507', '1:80239', '1:98765', '1:19171', '1:20892', '1:21546', '1:72605', '1:76107', '1:76328', '1:76417', '1:76434', '1:76723', '1:76729', '1:78657', '1:97966', '1:100485', '1:28197', '1:28593', '1:27514', '1:32050', '1:32029', '1:32534', '1:55719', '1:57103', '1:57110', '1:56566', '1:67845', '1:69318', '1:97185', '1:99322', '1:37238', '1:70595', '1:72656', '1:72782', '1:73996', '1:75095', '1:85121', '1:85628', '1:86170', '1:86283', '1:95298', '1:84438', '1:69455', '1:69832', '1:67861', '1:69324', '1:69993', '1:64405', '1:72277', '1:75379', '1:76046', '1:76092', '1:77121', '1:81761', '1:81971', '1:78251', '1:84279', '1:84806', '1:84811', '1:76313', '1:78049', '1:79465', '1:99349', '1:18408', '1:18645', '1:33878', '1:34990', '1:35086', '1:56292', '1:40062', '1:40120', '1:40222', '1:44985', '1:46217', '1:46526', '1:58528', '1:58585', '1:58589', '1:58611', '1:58638', '1:32924', '1:34195', '1:37591', '1:39446', '1:39594', '1:40671', '1:44198', '1:44263', '1:44378', '1:44726', '1:40109', '1:41166', '1:104753', '1:105023', '1:104628', '1:104646', '1:106166', '1:104811', '1:97708', '1:98150', '1:98962', '1:98973', '1:105798', '1:105802', '1:105831', '1:105815', '1:106255', '1:106121', '1:17767', '1:17912', '1:17700', '1:17729', '1:20591', '1:20666', '1:20867', '1:20903', '1:20911', '1:20913', '1:72778', '1:75121', '1:75284', '1:34025', '1:38195', '1:48485', '1:62576', '1:65371', '1:65404', '1:67047', '1:69732', '1:18002', '1:21226', '1:14213', '1:18659', '1:20406', '1:20514', '1:49903', '1:50958', '1:51999', '1:45800', '1:48271', '1:48303', '1:49389', '1:49752', '1:2131', '1:5342', '1:9670', '1:8972', '1:10029', '1:10124', '1:12505', '1:50738', '1:50896', '1:48274', '1:48912', '1:50012', '1:50035', '1:39473', '1:48662', '1:63115', '1:44273', '1:50657', '1:58775', '1:61314', '1:21850', '1:26056', '1:33976', '1:34174', '1:43863', '1:44220', '1:44673', '1:44696', '1:44810', '1:37623', '1:37671', '1:37767', '1:34638', '1:36011', '1:36055', '1:37716', '1:35351', '1:35645', '1:38286', '1:38755', '1:36510', '1:42381', '1:42535', '1:42670', '1:43339', '1:38914', '1:75479', '1:76468', '1:77499', '1:1061', '1:1331', '1:103643', '1:39539', '1:48177', '1:40609', '1:45301', '1:47298', '1:59920', '1:97328', '1:97826', '1:103040', '1:96989', '1:103502', '1:24556', '1:26393', '1:26537', '1:27923', '1:27779', '1:60280', '1:61710', '1:67595', '1:68209', '1:68212', '1:64596', '1:69441', '1:69611', '1:65200', '1:87055', '1:99720', '1:105409', '1:106301', '1:106144', '1:105939', '1:64585', '1:64976', '1:71015', '1:71183', '1:73625', '1:64312', '1:64475', '1:64533', '1:66843', '1:79863', '1:81395', '1:87400', '1:104297', '1:106204', '1:104844', '1:5625', '1:5934', '1:9032', '1:33373', '1:33378', '1:33642', '1:34117', '1:32268', '1:32654', '1:33288', '1:36865', '1:97511', '1:99443', '1:38595', '1:42214', '1:42301', '1:46563', '1:46725', '1:46752', '1:40184', '1:40494', '1:45276', '1:45566', '1:88529', '1:88791', '1:94024', '1:93225', '1:82997', '1:83754', '1:84582', '1:84644', '1:84493', '1:84895', '1:86402', '1:85828', '1:85885', '1:85911', '1:105683', '1:106329', '1:100371', '1:98510', '1:98649', '1:98655', '1:98699', '1:98700', '1:53101', '1:53240', '1:69491', '1:69917', '1:64997', '1:74193', '1:98120', '1:99375', '1:38619', '1:38659', '1:45237', '1:47193', '1:91829', '1:93084', '1:104327', '1:105885', '1:66069', '1:66194', '1:80434', '1:64869', '1:64885', '1:50755', '1:52346', '1:53194', '1:103316', '1:105491', '1:94299', '1:92683', '1:93751', '1:52547', '1:53615', '1:54128', '1:55280', '1:53320', '1:58536', '1:55506', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE6DCC6F-9702-EA11-8C9E-246E96D14D4C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/629AE047-9B03-EA11-AF08-0090FAA57770.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/74BFCEF5-7203-EA11-AC31-00259073E53A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8D6CEA6-5D03-EA11-9F3D-D48564593FA8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FED7A530-8703-EA11-9953-008CFAF28F22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4AC458D-3904-EA11-819B-0CC47AFF02CC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5AD9493D-D803-EA11-A326-002481CFE864.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8B96E8C-1B0B-EA11-B3FA-0CC47A4D75F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/548DD76C-8E0A-EA11-A159-0CC47A4C8E0E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4C7CE199-7F0A-EA11-B6D3-AC1F6BAC7EAC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A61B1E1C-3C0E-EA11-ADCF-506B4BB134E6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA16D4FD-B40E-EA11-AA73-AC1F6B1AEF94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E5B1D6C-8F0B-EA11-A380-FA163E1B56E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/06492256-3210-EA11-93C2-44A842BFA94B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D8A4A322-940F-EA11-9A4C-1CC1DE050110.root']);