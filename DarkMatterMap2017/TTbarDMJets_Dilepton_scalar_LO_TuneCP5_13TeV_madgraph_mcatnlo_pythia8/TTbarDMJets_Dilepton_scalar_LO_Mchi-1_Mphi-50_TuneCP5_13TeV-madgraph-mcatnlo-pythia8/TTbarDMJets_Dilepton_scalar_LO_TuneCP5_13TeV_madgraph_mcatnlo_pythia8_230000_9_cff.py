import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:51444', '1:51455', '1:51107', '1:51188', '1:51256', '1:51266', '1:51281', '1:51282', '1:51325', '1:51361', '1:57350', '1:67316', '1:67570', '1:67343', '1:67402', '1:67441', '1:67463', '1:67819', '1:67945', '1:67986', '1:67949', '1:67982', '1:68735', '1:69174', '1:69122', '1:69137', '1:92512', '1:92417', '1:92468', '1:92480', '1:92498', '1:92693', '1:92699', '1:78001', '1:78008', '1:78013', '1:78051', '1:78058', '1:78062', '1:78084', '1:78107', '1:78116', '1:78215', '1:78216', '1:78275', '1:83121', '1:79719', '1:82681', '1:83017', '1:83083', '1:83085', '1:83088', '1:83095', '1:83099', '1:83145', '1:95789', '1:96847', '1:97282', '1:85027', '1:85046', '1:85048', '1:85066', '1:85081', '1:85087', '1:85089', '1:85171', '1:85179', '1:102917', '1:380', '1:322', '1:329', '1:350', '1:372', '1:390', '1:414', '1:439', '1:607', '1:652', '1:905', '1:1184', '1:1303', '1:2756', '1:2758', '1:2759', '1:2761', '1:2783', '1:2974', '1:2978', '1:3659', '1:3682', '1:98939', '1:99390', '1:99400', '1:99503', '1:99849', '1:99886', '1:99974', '1:100016', '1:42517', '1:36628', '1:36925', '1:37831', '1:42118', '1:41007', '1:48567', '1:51411', '1:52379', '1:53205', '1:53220', '1:53266', '1:53503', '1:50944', '1:51597', '1:54017', '1:54155', '1:54414', '1:54421', '1:53830', '1:53981', '1:54028', '1:54032', '1:57055', '1:79775', '1:79800', '1:80824', '1:81405', '1:82369', '1:82381', '1:82404', '1:82410', '1:87813', '1:95461', '1:95557', '1:97789', '1:97951', '1:97976', '1:98299', '1:98733', '1:106168', '1:14574', '1:14916', '1:14929', '1:16066', '1:16300', '1:16486', '1:16676', '1:16761', '1:16853', '1:19677', '1:20574', '1:20652', '1:20721', '1:20722', '1:20900', '1:20680', '1:20798', '1:20816', '1:45137', '1:45690', '1:46410', '1:45831', '1:45837', '1:46173', '1:47380', '1:55323', '1:75324', '1:76229', '1:76714', '1:78121', '1:79191', '1:80117', '1:104169', '1:105587', '1:2024', '1:5063', '1:7095', '1:5026', '1:5029', '1:5253', '1:5385', '1:5388', '1:5402', '1:20490', '1:24051', '1:28961', '1:33012', '1:34775', '1:35690', '1:37321', '1:42787', '1:34218', '1:36786', '1:58529', '1:58892', '1:60422', '1:60946', '1:64768', '1:7521', '1:7537', '1:7683', '1:7731', '1:7907', '1:8009', '1:7691', '1:8493', '1:8876', '1:10264', '1:10266', '1:14288', '1:14558', '1:15932', '1:16227', '1:16265', '1:17124', '1:12676', '1:12694', '1:28176', '1:88192', '1:94906', '1:91352', '1:94511', '1:103274', '1:104818', '1:105785', '1:102384', '1:64260', '1:64371', '1:64431', '1:64926', '1:67131', '1:67163', '1:67209', '1:67210', '1:67223', '1:67312', '1:65888', '1:65975', '1:67056', '1:67273', '1:65811', '1:66065', '1:68158', '1:68159', '1:68184', '1:68229', '1:68936', '1:68880', '1:68925', '1:74755', '1:74785', '1:74801', '1:74903', '1:68960', '1:68985', '1:69100', '1:69091', '1:87894', '1:87921', '1:88021', '1:88039', '1:88067', '1:88133', '1:88152', '1:94539', '1:94844', '1:94917', '1:88334', '1:88370', '1:94409', '1:94449', '1:94900', '1:94663', '1:102439', '1:102459', '1:102487', '1:102673', '1:102681', '1:102491', '1:102494', '1:103555', '1:102396', '1:64980', '1:65009', '1:64781', '1:64821', '1:78932', '1:80045', '1:80053', '1:80131', '1:80188', '1:80205', '1:79064', '1:79123', '1:79160', '1:79170', '1:79187', '1:79192', '1:79241', '1:82586', '1:82628', '1:82638', '1:82668', '1:82727', '1:82750', '1:82593', '1:82606', '1:82610', '1:82637', '1:82658', '1:82662', '1:82663', '1:82688', '1:82694', '1:38142', '1:38224', '1:38253', '1:38368', '1:38373', '1:38419', '1:38437', '1:38447', '1:38513', '1:38607', '1:38660', '1:43004', '1:40283', '1:40591', '1:42394', '1:42770', '1:42298', '1:42312', '1:42410', '1:42462', '1:45140', '1:43795', '1:44221', '1:45008', '1:45039', '1:45223', '1:45257', '1:44424', '1:43762', '1:46758', '1:45093', '1:45198', '1:45253', '1:45255', '1:45267', '1:45317', '1:51658', '1:52265', '1:53088', '1:54506', '1:55338', '1:81280', '1:84479', '1:75355', '1:76853', '1:78002', '1:78952', '1:81324', '1:81939', '1:81363', '1:85055', '1:85056', '1:73147', '1:73289', '1:73263', '1:73268', '1:73474', '1:73549', '1:73557', '1:73611', '1:78733', '1:71469', '1:73377', '1:73412', '1:73430', '1:73774', '1:73782', '1:92042', '1:96078', '1:96641', '1:96673', '1:88531', '1:92368', '1:92746', '1:95321', '1:95504', '1:95538', '1:95619', '1:95642', '1:95926', '1:96034', '1:96129', '1:96577', '1:97673', '1:100515', '1:100741', '1:103029', '1:103222', '1:103762', '1:55222', '1:55433', '1:60196', '1:59167', '1:60531', '1:60823', '1:60916', '1:61813', '1:62288', '1:63618', '1:68257', '1:69633', '1:59658', '1:60172', '1:60266', '1:60623', '1:61213', '1:61902', '1:63684', '1:71697', '1:72383', '1:73830', '1:77889', '1:77915', '1:72377', '1:76049', '1:77056', '1:78360', '1:81433', '1:58785', '1:65212', '1:66014', '1:67757', '1:69682', '1:66908', '1:71300', '1:70276', '1:59340', '1:65243', '1:65300', '1:67790', '1:69034', '1:65196', '1:66017', '1:67788', '1:67974', '1:66357', '1:71276', '1:75932', '1:76379', '1:78538', '1:78858', '1:78992', '1:84655', '1:88607', '1:91904', '1:93711', '1:91513', '1:91548', '1:91607', '1:97532', '1:98174', '1:56785', '1:59538', '1:60375', '1:60804', '1:67227', '1:67353', '1:63339', '1:63509', '1:63546', '1:63769', '1:63901', '1:67132', '1:68596', '1:68902', '1:69298', '1:103288', '1:105582', '1:16704', '1:17612', '1:7551', '1:12961', '1:15216', '1:18147', '1:17819', '1:7246', '1:7303', '1:7387', '1:7452', '1:7493', '1:14359', '1:14489', '1:14490', '1:10452', '1:10491', '1:10493', '1:10457', '1:10552', '1:12800', '1:5156', '1:5238', '1:5265', '1:5276', '1:5295', '1:5314', '1:5420', '1:5593', '1:9079', '1:9129', '1:9055', '1:9096', '1:9127', '1:9132', '1:9153', '1:9161', '1:9165', '1:9169', '1:9260', '1:9263', '1:8307', '1:8386', '1:9732', '1:9743', '1:68606', '1:69291', '1:69320', '1:69337', '1:69362', '1:69395', '1:69416', '1:69443', '1:71750', '1:85227', '1:85236', '1:85578', '1:85659', '1:85766', '1:85768', '1:85790', '1:88940', '1:91425', '1:94319', '1:104075', '1:40211', '1:48792', '1:50335', '1:50545', '1:50678', '1:51512', '1:52068', '1:52208', '1:53175', '1:53404', '1:53789', '1:53893', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/06F65C32-13F3-E911-AC5A-002590DE6E30.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4253ADC4-03F5-E911-AFEA-AC1F6B0DE0A0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0014CD18-06F6-E911-8B27-FA163E69BD36.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E66B73CD-70F7-E911-8EBA-E0071B7A18F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/043AF729-4A10-EA11-B2D6-0CC47AFF2492.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/68454F20-060A-EA11-A63A-AC1F6BAC816C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D2B1428C-88F2-E911-B4D4-3417EBE705CD.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3C9F3E3A-5600-EA11-B8FE-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE1AA428-17F0-E911-A0AE-0CC47A4DEDB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A217F84B-F6F2-E911-84C6-A0369F5BD8D4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC608F2A-9802-EA11-984E-D48564599C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38FDE37B-BEFC-E911-B96A-001E67E5EDBB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/48D3300C-5110-EA11-A284-00259090822A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40DCE1CF-C002-EA11-B8F4-0CC47AFF0220.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8CD8C04A-5210-EA11-8222-0025904B04A8.root']);