import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:54195', '1:59470', '1:59494', '1:59811', '1:59935', '1:81436', '1:84433', '1:84472', '1:84865', '1:84922', '1:86037', '1:103023', '1:103054', '1:103059', '1:85481', '1:85524', '1:85538', '1:102951', '1:104744', '1:104750', '1:104755', '1:104882', '1:104885', '1:104814', '1:105035', '1:105052', '1:105021', '1:103036', '1:103852', '1:103889', '1:104896', '1:3691', '1:3698', '1:3803', '1:3894', '1:3943', '1:3988', '1:4325', '1:4328', '1:4773', '1:4892', '1:5070', '1:20182', '1:20271', '1:20278', '1:20286', '1:20289', '1:20310', '1:20411', '1:48823', '1:56692', '1:56703', '1:56963', '1:58157', '1:81273', '1:81659', '1:81544', '1:81605', '1:93822', '1:91801', '1:96548', '1:100105', '1:99854', '1:63475', '1:63789', '1:63941', '1:63949', '1:64000', '1:67079', '1:67118', '1:75665', '1:75681', '1:75724', '1:75863', '1:75906', '1:76309', '1:79592', '1:79600', '1:79608', '1:83976', '1:84519', '1:79744', '1:79831', '1:93618', '1:93643', '1:93682', '1:56569', '1:56615', '1:56910', '1:60789', '1:61165', '1:60895', '1:60911', '1:61032', '1:61086', '1:61467', '1:74820', '1:74920', '1:75301', '1:75470', '1:62942', '1:63252', '1:63345', '1:63348', '1:63616', '1:98142', '1:105129', '1:102168', '1:103713', '1:103747', '1:103772', '1:104010', '1:72990', '1:74132', '1:75016', '1:75018', '1:75524', '1:103634', '1:103693', '1:104122', '1:83868', '1:83957', '1:84821', '1:85281', '1:85289', '1:85476', '1:87150', '1:105154', '1:105177', '1:105302', '1:105297', '1:105306', '1:105310', '1:105340', '1:105341', '1:105346', '1:72862', '1:72884', '1:74158', '1:86907', '1:87024', '1:87295', '1:87394', '1:105594', '1:82350', '1:105432', '1:50272', '1:50826', '1:50872', '1:50901', '1:51694', '1:52621', '1:52649', '1:52779', '1:52817', '1:53524', '1:53827', '1:57377', '1:62038', '1:62138', '1:52887', '1:52894', '1:52938', '1:52963', '1:53053', '1:53128', '1:53263', '1:53288', '1:53370', '1:53380', '1:53393', '1:60425', '1:59319', '1:59342', '1:59329', '1:59359', '1:69179', '1:69991', '1:55924', '1:55935', '1:56393', '1:66143', '1:66184', '1:66198', '1:66689', '1:84129', '1:84224', '1:84289', '1:15737', '1:57762', '1:103463', '1:95234', '1:57683', '1:57756', '1:57900', '1:58146', '1:58300', '1:96211', '1:96696', '1:93614', '1:95941', '1:99548', '1:63653', '1:67105', '1:58665', '1:58899', '1:58963', '1:58941', '1:59012', '1:59552', '1:61556', '1:61984', '1:61388', '1:62313', '1:67380', '1:96639', '1:96756', '1:91764', '1:96099', '1:97109', '1:97129', '1:59006', '1:59054', '1:59127', '1:59215', '1:59390', '1:70470', '1:70550', '1:70579', '1:80112', '1:80402', '1:80463', '1:80751', '1:76369', '1:76482', '1:79877', '1:79905', '1:74614', '1:74623', '1:80273', '1:95742', '1:95869', '1:96924', '1:96960', '1:96971', '1:98430', '1:103466', '1:103478', '1:103495', '1:103501', '1:76241', '1:76278', '1:76560', '1:103375', '1:103386', '1:9406', '1:9651', '1:35822', '1:36745', '1:38056', '1:38896', '1:49586', '1:49691', '1:40745', '1:40758', '1:40956', '1:41115', '1:41423', '1:41473', '1:41661', '1:44062', '1:44113', '1:77885', '1:77899', '1:77926', '1:77985', '1:49060', '1:49127', '1:62879', '1:52375', '1:55722', '1:56089', '1:56245', '1:51407', '1:51527', '1:51547', '1:51827', '1:51839', '1:52369', '1:61456', '1:4447', '1:3787', '1:3837', '1:3960', '1:3973', '1:4472', '1:4821', '1:4927', '1:4999', '1:20072', '1:20078', '1:20091', '1:20135', '1:20225', '1:34288', '1:34361', '1:34502', '1:54339', '1:54387', '1:18253', '1:18384', '1:18470', '1:18576', '1:18695', '1:18951', '1:33124', '1:33140', '1:33229', '1:33237', '1:33325', '1:33382', '1:45815', '1:40902', '1:40982', '1:44097', '1:41348', '1:41371', '1:41406', '1:41459', '1:41649', '1:41679', '1:41722', '1:41736', '1:41772', '1:41965', '1:48656', '1:97448', '1:28127', '1:28338', '1:32545', '1:35548', '1:36879', '1:38731', '1:42185', '1:43213', '1:32104', '1:32711', '1:32712', '1:36633', '1:52987', '1:41439', '1:48020', '1:29', '1:352', '1:353', '1:359', '1:1065', '1:1096', '1:48198', '1:41802', '1:44144', '1:44591', '1:49333', '1:49342', '1:62731', '1:9188', '1:9200', '1:9400', '1:15214', '1:15340', '1:15490', '1:15772', '1:27221', '1:43597', '1:43513', '1:43815', '1:46136', '1:53113', '1:53217', '1:53331', '1:53441', '1:53610', '1:53611', '1:53807', '1:53828', '1:53831', '1:53842', '1:54164', '1:87939', '1:46829', '1:47040', '1:47099', '1:47291', '1:47379', '1:47391', '1:47394', '1:47408', '1:47508', '1:47515', '1:51786', '1:52216', '1:52278', '1:52322', '1:52457', '1:53783', '1:76566', '1:76899', '1:77046', '1:96163', '1:35818', '1:36546', '1:38230', '1:28391', '1:28759', '1:28856', '1:28965', '1:32242', '1:32776', '1:32380', '1:33291', '1:35172', '1:35241', '1:35296', '1:35597', '1:32397', '1:36100', '1:35889', '1:32968', '1:34234', '1:34273', '1:45113', '1:36959', '1:38050', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BA9C6D45-81F2-E911-B2AB-38EAA78D8F94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/36D78EB2-CCF3-E911-995B-B02628270130.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1053FDAA-ACF2-E911-84FC-0CC47AC33AB2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1AC0AA99-8FF2-E911-8744-509A4C9F888B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2239DCC-28F2-E911-AA3B-509A4C9EF8FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6C83F5CD-28F2-E911-81A0-3C4A92F7DD14.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2642BA0F-EAF2-E911-9804-BC305B390A66.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AA9B7C2D-13F3-E911-96B6-38EAA78D8AD0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D47796E2-24F3-E911-B8B9-0090FAA575D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/282DD46C-49F3-E911-BCB2-0CC47AFC3C76.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4C1F9DD3-CAF4-E911-A99D-0CC47A4DEF24.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FE80AD87-C6F3-E911-9889-FA163E75C7F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6A00BA3-1BF3-E911-8276-A0369FE2C05E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A20AA7F9-50F3-E911-BCB8-AC1F6B0DE2F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96F5ED8B-D4F3-E911-B505-FA163ED72B3C.root']);