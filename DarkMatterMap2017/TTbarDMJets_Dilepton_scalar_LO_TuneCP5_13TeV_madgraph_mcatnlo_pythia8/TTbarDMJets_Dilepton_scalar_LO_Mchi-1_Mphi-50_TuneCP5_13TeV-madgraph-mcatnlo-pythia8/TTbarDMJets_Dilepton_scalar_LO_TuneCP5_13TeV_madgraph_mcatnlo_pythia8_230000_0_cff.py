import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1263', '1:4296', '1:346', '1:444', '1:1820', '1:3311', '1:3548', '1:2023', '1:2694', '1:3564', '1:3632', '1:8404', '1:16986', '1:18674', '1:32369', '1:33313', '1:34824', '1:34929', '1:37540', '1:37646', '1:35498', '1:35885', '1:38043', '1:53453', '1:58540', '1:58547', '1:61000', '1:52935', '1:67684', '1:68878', '1:69115', '1:69396', '1:63644', '1:62876', '1:63006', '1:67744', '1:66216', '1:69846', '1:69982', '1:68303', '1:68681', '1:68883', '1:69640', '1:69761', '1:63747', '1:65227', '1:71234', '1:72343', '1:74754', '1:75452', '1:58837', '1:60908', '1:59790', '1:72528', '1:72538', '1:72931', '1:77612', '1:2022', '1:2027', '1:1751', '1:1982', '1:2234', '1:3053', '1:3093', '1:3108', '1:2304', '1:2457', '1:2603', '1:2727', '1:26029', '1:26043', '1:26100', '1:26101', '1:26132', '1:26140', '1:27007', '1:42093', '1:42494', '1:42966', '1:46961', '1:44603', '1:40108', '1:40720', '1:40999', '1:42120', '1:43104', '1:14204', '1:14205', '1:15180', '1:15191', '1:15241', '1:15253', '1:15272', '1:15295', '1:15318', '1:15376', '1:15499', '1:15514', '1:15415', '1:15441', '1:15443', '1:15458', '1:15470', '1:15476', '1:15561', '1:15583', '1:15596', '1:15655', '1:15846', '1:15990', '1:17159', '1:17283', '1:17422', '1:17445', '1:26324', '1:26330', '1:26354', '1:26371', '1:26781', '1:26814', '1:26820', '1:26863', '1:26779', '1:26897', '1:26484', '1:26364', '1:26585', '1:39308', '1:44539', '1:53216', '1:53371', '1:53529', '1:53537', '1:53552', '1:53562', '1:53577', '1:53592', '1:53613', '1:53661', '1:53705', '1:53721', '1:53790', '1:53911', '1:53932', '1:77058', '1:79827', '1:84797', '1:83112', '1:87806', '1:86867', '1:87875', '1:91111', '1:79484', '1:79678', '1:79691', '1:79896', '1:79925', '1:28521', '1:28552', '1:28603', '1:28623', '1:28627', '1:28650', '1:28564', '1:28569', '1:28587', '1:28762', '1:28792', '1:64186', '1:64766', '1:64786', '1:64880', '1:65944', '1:66740', '1:69590', '1:66543', '1:73217', '1:70556', '1:103364', '1:103884', '1:75391', '1:75802', '1:77436', '1:77999', '1:78994', '1:81050', '1:81818', '1:77821', '1:78184', '1:81003', '1:81030', '1:81047', '1:78241', '1:78469', '1:78642', '1:78804', '1:86240', '1:84206', '1:84209', '1:84214', '1:84271', '1:84314', '1:84379', '1:84380', '1:84418', '1:84425', '1:84443', '1:84559', '1:84567', '1:84631', '1:96260', '1:95730', '1:95769', '1:95777', '1:95791', '1:95920', '1:96147', '1:96158', '1:96181', '1:96297', '1:21716', '1:21878', '1:24158', '1:24916', '1:24959', '1:19082', '1:26163', '1:26174', '1:26288', '1:26315', '1:21798', '1:39604', '1:39643', '1:39645', '1:39880', '1:39885', '1:39934', '1:40518', '1:42573', '1:42904', '1:44976', '1:44999', '1:45420', '1:44835', '1:47480', '1:47645', '1:47828', '1:48139', '1:48285', '1:32080', '1:32086', '1:32110', '1:32537', '1:32281', '1:32297', '1:32311', '1:32395', '1:32430', '1:32516', '1:39138', '1:39546', '1:39656', '1:39165', '1:39177', '1:39191', '1:39220', '1:39226', '1:39235', '1:39237', '1:39238', '1:39244', '1:39256', '1:39335', '1:39433', '1:39683', '1:42692', '1:42699', '1:42742', '1:42749', '1:42813', '1:46141', '1:46330', '1:46353', '1:46541', '1:46594', '1:36561', '1:36619', '1:38272', '1:40001', '1:40040', '1:40051', '1:40072', '1:40175', '1:40190', '1:40199', '1:40342', '1:35750', '1:37054', '1:37072', '1:37157', '1:37275', '1:37294', '1:37315', '1:35766', '1:35996', '1:37003', '1:37053', '1:37171', '1:48498', '1:48354', '1:48388', '1:48455', '1:48509', '1:48785', '1:48961', '1:49025', '1:72054', '1:72087', '1:72353', '1:74987', '1:76362', '1:76444', '1:76478', '1:76951', '1:77497', '1:77574', '1:78247', '1:78340', '1:76967', '1:76998', '1:77661', '1:78029', '1:78134', '1:78258', '1:78545', '1:86077', '1:85078', '1:85102', '1:85198', '1:85235', '1:85240', '1:79787', '1:79802', '1:79846', '1:85253', '1:85257', '1:85341', '1:85343', '1:88950', '1:91134', '1:91210', '1:53856', '1:53650', '1:53699', '1:53731', '1:53737', '1:53753', '1:53944', '1:53949', '1:53960', '1:54048', '1:54276', '1:75819', '1:71915', '1:71696', '1:71774', '1:71821', '1:71861', '1:71975', '1:73019', '1:73338', '1:71682', '1:71845', '1:71942', '1:71950', '1:73802', '1:73941', '1:73956', '1:73753', '1:73869', '1:73888', '1:73728', '1:73737', '1:73575', '1:73592', '1:73593', '1:74052', '1:73682', '1:73699', '1:73975', '1:87560', '1:85301', '1:86787', '1:86954', '1:87350', '1:87889', '1:88124', '1:88245', '1:88393', '1:88584', '1:88630', '1:88638', '1:74468', '1:74487', '1:74729', '1:74780', '1:74805', '1:74841', '1:74883', '1:75013', '1:95238', '1:80504', '1:80506', '1:80606', '1:80612', '1:80739', '1:80600', '1:80626', '1:80671', '1:80732', '1:80735', '1:80794', '1:80799', '1:95063', '1:95152', '1:95275', '1:95283', '1:95222', '1:95187', '1:95214', '1:2608', '1:2641', '1:15779', '1:15833', '1:16927', '1:17111', '1:17323', '1:17406', '1:17636', '1:17879', '1:18021', '1:18032', '1:18105', '1:19013', '1:19248', '1:19257', '1:33797', '1:40075', '1:39741', '1:40841', '1:44617', '1:53292', '1:57558', '1:60989', '1:63004', '1:68631', '1:52282', '1:54042', '1:56051', '1:57463', '1:58067', '1:53152', '1:58373', '1:58504', '1:57885', '1:57851', '1:59226', '1:59442', '1:61210', '1:58549', '1:57934', '1:59580', '1:58606', '1:59065', '1:59198', '1:59551', '1:61019', '1:61315', '1:19367', '1:19452', '1:19554', '1:19264', '1:19345', '1:19378', '1:19476', '1:19536', '1:19604', '1:41184', '1:41186', '1:41360', '1:51417', '1:51524', '1:51557', '1:51581', '1:51745', '1:51608', '1:51777', '1:51840', '1:51850', '1:51662', '1:51657', '1:70755', '1:70980', '1:71099', '1:71123', '1:70802', '1:70803', '1:70945', '1:70991', '1:76838', '1:78264', '1:78343', '1:78366', '1:78383', '1:78397', '1:78435', '1:78449', '1:78491', '1:78593', '1:78594', '1:86081', '1:86140', '1:86148', '1:86238', '1:86251', '1:86293', '1:86391', '1:86298', '1:86307', '1:86403', '1:1013', '1:1021', '1:1064', '1:3', '1:101', '1:149', '1:158', '1:230', '1:1126', '1:514', '1:810', '1:811', '1:822', '1:956', '1:1223', '1:1352', '1:1368', '1:1693', '1:2068', '1:2071', '1:2083', '1:2182', '1:2211', '1:945', '1:4085', '1:27107', '1:27035', '1:27092', '1:27098', '1:27105', '1:50167', '1:32766', '1:32938', '1:32951', '1:33067', '1:33136', '1:33153', '1:34080', '1:34194', '1:34199', '1:42797', '1:42828', '1:42871', '1:42924', '1:42936', '1:42948', '1:42983', '1:37745', '1:37785', '1:37837', '1:37787', '1:35286', '1:35248', '1:37250', '1:35704', '1:35923', '1:36041', '1:36086', '1:36094', '1:36102', '1:36123', '1:36236', '1:36377', '1:38861', '1:42097', '1:42143', '1:42174', '1:42207', '1:42296', '1:42311', '1:42584', '1:42648', '1:42652', '1:42675', '1:42700', '1:38795', '1:38863', '1:38912', '1:38929', '1:42038', '1:42041', '1:42156', '1:42179', '1:42245', '1:42641', '1:39855', '1:39874', '1:39899', '1:40633', '1:41113', '1:40746', '1:40878', '1:41024', '1:44572', '1:44587', '1:49223', '1:49235', '1:49285', '1:26482', '1:26539', '1:26540', '1:26542', '1:26573', '1:26640', '1:26912', '1:26923', '1:40260', '1:40406', '1:40660', '1:40755', '1:40795', '1:41044', '1:41056', '1:41097', '1:41250', '1:41266', '1:41219', '1:41235', '1:43076', '1:43585', '1:43601', '1:43658', '1:43178', '1:43195', '1:35049', '1:34077', '1:34202', '1:34203', '1:34211', '1:35911', '1:36065', '1:36069', '1:36071', '1:36192', '1:37398', '1:37403', '1:37483', '1:47360', '1:48364', '1:48373', '1:48535', '1:39600', '1:40743', '1:41090', '1:8650', '1:8654', '1:8730', '1:8906', '1:8968', '1:9288', '1:21313', '1:32266', '1:33615', '1:33620', '1:33650', '1:33637', '1:33677', '1:33688', '1:33832', '1:33819', '1:34069', '1:37898', '1:35133', '1:35524', '1:35567', '1:35609', '1:37754', '1:37797', '1:37813', '1:37857', '1:37966', '1:37989', '1:35148', '1:35249', '1:35263', '1:35460', '1:35493', '1:35526', '1:35534', '1:36682', '1:36710', '1:36790', '1:36920', '1:36928', '1:36932', '1:36976', '1:36692', '1:36701', '1:36742', '1:36763', '1:37713', '1:37954', '1:37978', '1:37380', '1:37578', '1:41480', '1:66042', '1:65904', '1:65945', '1:66507', '1:66224', '1:66362', '1:73015', '1:73026', '1:73036', '1:73046', '1:73162', '1:73244', '1:73325', '1:72365', '1:72477', '1:72285', '1:72317', '1:72735', '1:72779', '1:72877', '1:72440', '1:72519', '1:72575', '1:72658', '1:73481', '1:73483', '1:73770', '1:96584', '1:96727', '1:97558', '1:97817', '1:98232', '1:98252', '1:98506', '1:38244', '1:38552', '1:38688', '1:38804', '1:43084', '1:44279', '1:44406', '1:44757', '1:44783', '1:44788', '1:44876', '1:45386', '1:45424', '1:45770', '1:45810', '1:45917', '1:45925', '1:46554', '1:46063', '1:43433', '1:43498', '1:49535', '1:49539', '1:52031', '1:52039', '1:52046', '1:52081', '1:52091', '1:52154', '1:52161', '1:60329', '1:60359', '1:60361', '1:87489', '1:87501', '1:87599', '1:87646', '1:87660', '1:87662', '1:94785', '1:94793', '1:94809', '1:94818', '1:94901', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4643D148-8CEE-E911-99A7-549F351E4006.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/06C0880D-5BEE-E911-8B86-3417EBE7446B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F6171A5F-F2EF-E911-A256-00E081B705E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9AAAA0F6-25EF-E911-B7E1-A0369FC52524.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/18DA53CD-85EE-E911-A3D0-089E0158CC5B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84D69AFF-25EF-E911-8112-089E0158CDE1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9239CEF9-77EF-E911-B001-0CC47A7E69D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/548A6B80-19EF-E911-A713-506B4BB166B6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40CC65EC-25EF-E911-A3C8-3417EBE70684.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50378F1B-71EE-E911-AD26-38EAA78D8ADC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/88A32370-47EF-E911-8B0C-441EA1615D6A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A7EA364-40EF-E911-B34B-38EAA78D89AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D822EACF-33EF-E911-A627-38EAA78D8FB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CE68873-42F0-E911-99DB-441EA1616D3A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/969DC298-18EF-E911-A24A-38EAA78D8B54.root']);