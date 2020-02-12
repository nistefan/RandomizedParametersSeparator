import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:28228', '1:28410', '1:28659', '1:34715', '1:35068', '1:23619', '1:28198', '1:28336', '1:28606', '1:32998', '1:35048', '1:37032', '1:37521', '1:37558', '1:37611', '1:25118', '1:28366', '1:28715', '1:33331', '1:26588', '1:29161', '1:29225', '1:36836', '1:36949', '1:38003', '1:38311', '1:38340', '1:38369', '1:38375', '1:38249', '1:38403', '1:38411', '1:38484', '1:35851', '1:35996', '1:37025', '1:68133', '1:68260', '1:69279', '1:69361', '1:81543', '1:81988', '1:88844', '1:55752', '1:62798', '1:64886', '1:64906', '1:75181', '1:76720', '1:94030', '1:81797', '1:88531', '1:183', '1:192', '1:1205', '1:1827', '1:1947', '1:2060', '1:2621', '1:3926', '1:5080', '1:5396', '1:5551', '1:5930', '1:2889', '1:2905', '1:4535', '1:5097', '1:5874', '1:3382', '1:5825', '1:9144', '1:17433', '1:9852', '1:10740', '1:15958', '1:16222', '1:18314', '1:22484', '1:26591', '1:26607', '1:26883', '1:33387', '1:36853', '1:7188', '1:13326', '1:20096', '1:59920', '1:23787', '1:37126', '1:38699', '1:23702', '1:28205', '1:28485', '1:32434', '1:34392', '1:34440', '1:35466', '1:23869', '1:34883', '1:39994', '1:23983', '1:31683', '1:34201', '1:35755', '1:40440', '1:53901', '1:56800', '1:57687', '1:58169', '1:60908', '1:50778', '1:52219', '1:52590', '1:61628', '1:63115', '1:50828', '1:53911', '1:51577', '1:53698', '1:58255', '1:58312', '1:52127', '1:52137', '1:6266', '1:7015', '1:9585', '1:10026', '1:8216', '1:8293', '1:8374', '1:9239', '1:9393', '1:9412', '1:9536', '1:9672', '1:10726', '1:10915', '1:13288', '1:9626', '1:10295', '1:10564', '1:10781', '1:102147', '1:23089', '1:28976', '1:31326', '1:31343', '1:32276', '1:35524', '1:37344', '1:37518', '1:28612', '1:28677', '1:34409', '1:38510', '1:23835', '1:32386', '1:34381', '1:35337', '1:37049', '1:95925', '1:97412', '1:102047', '1:102515', '1:87557', '1:88616', '1:88693', '1:88728', '1:88744', '1:88759', '1:89619', '1:90694', '1:90809', '1:88776', '1:100812', '1:88045', '1:99275', '1:99771', '1:102366', '1:90817', '1:90823', '1:87933', '1:88570', '1:88920', '1:88881', '1:89856', '1:90411', '1:523', '1:1738', '1:4962', '1:9704', '1:15498', '1:7948', '1:8560', '1:13496', '1:16744', '1:17074', '1:20055', '1:22490', '1:398', '1:487', '1:1342', '1:1481', '1:1716', '1:3358', '1:213', '1:3404', '1:3848', '1:4412', '1:4453', '1:4499', '1:5082', '1:5179', '1:5202', '1:5405', '1:21507', '1:37911', '1:26325', '1:36620', '1:25929', '1:26900', '1:29368', '1:33910', '1:23697', '1:6148', '1:13113', '1:15748', '1:21315', '1:22042', '1:22441', '1:6155', '1:9084', '1:9360', '1:10795', '1:8707', '1:9175', '1:9490', '1:17286', '1:7684', '1:96339', '1:97848', '1:98236', '1:101202', '1:101234', '1:96751', '1:97791', '1:97872', '1:74770', '1:74782', '1:74851', '1:78897', '1:23796', '1:24767', '1:46764', '1:27839', '1:39146', '1:39046', '1:39148', '1:46229', '1:90697', '1:79450', '1:36243', '1:36433', '1:33662', '1:38761', '1:38856', '1:49730', '1:49983', '1:50334', '1:51532', '1:52149', '1:50132', '1:50373', '1:52939', '1:60164', '1:60310', '1:60446', '1:60511', '1:60730', '1:60903', '1:55821', '1:30688', '1:34282', '1:25000', '1:31034', '1:46545', '1:54657', '1:75184', '1:75639', '1:69582', '1:69626', '1:24482', '1:24941', '1:30403', '1:30840', '1:37668', '1:58078', '1:58159', '1:60909', '1:74806', '1:74968', '1:79384', '1:79474', '1:79681', '1:79877', '1:80180', '1:80655', '1:80761', '1:80848', '1:80921', '1:64295', '1:67689', '1:64946', '1:75405', '1:55264', '1:55328', '1:62986', '1:64889', '1:74403', '1:78516', '1:71605', '1:73539', '1:73636', '1:77312', '1:68575', '1:71398', '1:72023', '1:73436', '1:73561', '1:94837', '1:95258', '1:97476', '1:100032', '1:99181', '1:70493', '1:71542', '1:72560', '1:70416', '1:71012', '1:71063', '1:71138', '1:71159', '1:71489', '1:71555', '1:71628', '1:70469', '1:73625', '1:99609', '1:102079', '1:102419', '1:79758', '1:87201', '1:87447', '1:95119', '1:95142', '1:87973', '1:88922', '1:90477', '1:91468', '1:74236', '1:97846', '1:98623', '1:99443', '1:100135', '1:100951', '1:101657', '1:101997', '1:76116', '1:76402', '1:76412', '1:76996', '1:97169', '1:102344', '1:81654', '1:88553', '1:90454', '1:90892', '1:91248', '1:91369', '1:91530', '1:90472', '1:91088', '1:91439', '1:91881', '1:88384', '1:88793', '1:88816', '1:89034', '1:89533', '1:89824', '1:89932', '1:90309', '1:90592', '1:90941', '1:94567', '1:100101', '1:28', '1:342', '1:429', '1:442', '1:675', '1:1030', '1:1220', '1:1321', '1:1529', '1:2186', '1:2330', '1:3186', '1:191', '1:209', '1:243', '1:328', '1:696', '1:1727', '1:1832', '1:2507', '1:3781', '1:3885', '1:728', '1:2046', '1:2260', '1:2317', '1:2538', '1:2674', '1:3566', '1:2194', '1:2406', '1:2693', '1:2788', '1:3210', '1:3315', '1:3372', '1:3705', '1:3756', '1:4053', '1:4746', '1:60939', '1:1657', '1:2175', '1:296', '1:591', '1:599', '1:1295', '1:4155', '1:4381', '1:1831', '1:2191', '1:3137', '1:3629', '1:22018', '1:22844', '1:32896', '1:34240', '1:35240', '1:35721', '1:36873', '1:25450', '1:26194', '1:28865', '1:29601', '1:31937', '1:32705', '1:28681', '1:24587', '1:27489', '1:27578', '1:27677', '1:30365', '1:30422', '1:30481', '1:32174', '1:32473', '1:32507', '1:34372', '1:49027', '1:50627', '1:51161', '1:51302', '1:51519', '1:51950', '1:23148', '1:35372', '1:39492', '1:23252', '1:27760', '1:27867', '1:34023', '1:40988', '1:28430', '1:34344', '1:37961', '1:2210', '1:2684', '1:2765', '1:3820', '1:5398', '1:5829', '1:5836', '1:5954', '1:7256', '1:8116', '1:9402', '1:575', '1:2448', '1:3573', '1:4734', '1:2451', '1:2472', '1:4770', '1:17', '1:160', '1:226', '1:233', '1:285', '1:446', '1:494', '1:495', '1:510', '1:520', '1:716', '1:732', '1:583', '1:1208', '1:1230', '1:1314', '1:1334', '1:1561', '1:1787', '1:3081', '1:3108', '1:3250', '1:3290', '1:3322', '1:2108', '1:2192', '1:2221', '1:2228', '1:585', '1:721', '1:1358', '1:1920', '1:3145', '1:4821', '1:61', '1:2303', '1:2457', '1:5268', '1:5417', '1:5690', '1:5845', '1:8832', '1:39940', '1:20049', '1:21492', '1:16458', '1:18889', '1:19232', '1:19644', '1:20357', '1:22204', '1:22666', '1:26340', '1:26421', '1:25914', '1:26842', '1:25721', '1:23203', '1:33383', '1:24245', '1:30928', '1:37019', '1:36624', '1:20053', '1:20495', '1:1885', '1:2023', '1:2038', '1:3009', '1:3047', '1:3363', '1:3368', '1:5330', '1:5357', '1:5450', '1:5489', '1:5653', '1:5711', '1:36708', '1:36733', '1:38280', '1:38350', '1:38857', '1:38979', '1:76700', '1:76744', '1:76830', '1:39679', '1:50612', '1:50715', '1:51763', '1:51808', '1:51818', '1:52019', '1:52113', '1:76371', '1:75906', '1:75963', '1:76035', '1:76050', '1:76051', '1:76064', '1:76067', '1:76198', '1:76203', '1:76227', '1:91695', '1:94761', '1:95334', '1:95881', '1:99861', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A29568F-0204-EA11-8E9E-20CF3027A6B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A57B881-3F03-EA11-8CAB-D48564594FB4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FA29DAC3-4304-EA11-8CA5-F01FAFD6996C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2CFB0664-3407-EA11-BC37-A0369FD0B3E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCBAF234-0107-EA11-95FC-0CC47A4DEDD6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C5438B6-1B08-EA11-B2E6-90B11CBCFFA9.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60A4990B-DB07-EA11-BFBE-44A842CFD5B1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0682B29D-DD08-EA11-AE0F-AC1F6BAC7ACC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/520DFFB1-110B-EA11-88A1-0CC47A7C353E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C157FD6-120B-EA11-8BA5-0025905A60C6.root']);