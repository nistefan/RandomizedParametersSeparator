import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:15734', '1:20030', '1:20886', '1:17108', '1:18764', '1:20509', '1:20590', '1:20946', '1:52240', '1:61910', '1:61918', '1:61929', '1:62299', '1:61182', '1:62163', '1:62757', '1:62891', '1:62935', '1:63940', '1:63135', '1:58111', '1:58491', '1:54435', '1:54681', '1:55598', '1:55653', '1:55780', '1:70749', '1:71308', '1:72091', '1:72873', '1:74892', '1:81191', '1:75514', '1:76548', '1:80014', '1:70985', '1:70995', '1:71542', '1:73041', '1:73653', '1:80709', '1:78211', '1:81736', '1:75283', '1:78012', '1:78639', '1:78662', '1:104267', '1:82891', '1:82912', '1:82919', '1:82928', '1:82936', '1:82978', '1:82979', '1:82989', '1:84044', '1:84051', '1:84141', '1:84149', '1:84176', '1:84181', '1:84353', '1:91163', '1:94280', '1:94315', '1:94448', '1:94845', '1:94862', '1:94878', '1:94927', '1:103899', '1:104058', '1:104077', '1:104090', '1:104110', '1:104131', '1:104168', '1:104175', '1:104323', '1:104326', '1:103916', '1:103920', '1:103923', '1:69790', '1:69949', '1:94797', '1:85024', '1:86281', '1:86445', '1:86870', '1:87115', '1:87436', '1:87624', '1:88208', '1:91056', '1:86552', '1:88139', '1:91986', '1:93377', '1:93384', '1:93445', '1:93865', '1:93913', '1:93914', '1:93926', '1:93959', '1:70059', '1:70122', '1:70133', '1:70194', '1:74393', '1:74410', '1:74503', '1:74505', '1:74021', '1:74032', '1:74044', '1:74090', '1:74098', '1:74102', '1:74110', '1:74144', '1:74274', '1:92327', '1:92446', '1:92810', '1:1527', '1:1529', '1:1218', '1:1222', '1:1226', '1:1306', '1:1337', '1:1295', '1:1472', '1:14072', '1:14291', '1:14308', '1:14317', '1:14327', '1:14577', '1:14590', '1:14591', '1:14619', '1:14649', '1:14678', '1:14997', '1:16365', '1:16551', '1:16727', '1:16828', '1:20046', '1:16246', '1:40826', '1:17789', '1:17832', '1:17846', '1:17871', '1:17889', '1:18334', '1:18462', '1:34606', '1:35431', '1:35955', '1:37848', '1:38027', '1:38065', '1:28410', '1:32930', '1:34148', '1:37490', '1:48436', '1:48391', '1:50043', '1:51835', '1:57641', '1:58690', '1:55004', '1:58751', '1:62945', '1:66052', '1:64206', '1:65525', '1:70398', '1:99317', '1:99774', '1:99819', '1:27583', '1:27892', '1:27948', '1:39035', '1:39382', '1:44545', '1:44722', '1:44784', '1:44914', '1:39817', '1:39839', '1:46306', '1:46430', '1:46089', '1:46108', '1:46119', '1:46181', '1:46186', '1:46272', '1:46055', '1:46464', '1:72987', '1:74980', '1:75412', '1:76452', '1:76479', '1:77283', '1:77717', '1:77897', '1:81573', '1:75506', '1:75976', '1:77110', '1:48623', '1:48639', '1:49067', '1:35876', '1:35944', '1:36871', '1:38745', '1:42591', '1:42795', '1:45510', '1:45982', '1:46405', '1:64532', '1:52836', '1:55127', '1:56672', '1:57466', '1:59844', '1:62521', '1:60397', '1:60439', '1:60672', '1:60801', '1:61185', '1:58625', '1:68508', '1:68741', '1:68742', '1:68877', '1:35667', '1:36183', '1:36264', '1:36824', '1:38146', '1:36915', '1:42895', '1:53283', '1:54725', '1:55082', '1:55600', '1:57570', '1:57670', '1:57734', '1:58020', '1:58688', '1:59232', '1:59233', '1:59273', '1:55507', '1:57094', '1:57639', '1:55677', '1:55979', '1:56050', '1:57402', '1:57546', '1:54781', '1:56266', '1:57311', '1:57800', '1:63604', '1:69346', '1:4901', '1:4951', '1:8686', '1:8765', '1:8788', '1:8818', '1:8822', '1:8829', '1:8848', '1:9934', '1:98419', '1:98435', '1:98507', '1:98557', '1:98580', '1:8905', '1:8995', '1:10600', '1:10847', '1:10961', '1:12090', '1:7118', '1:8011', '1:20532', '1:20897', '1:21366', '1:21375', '1:21402', '1:21413', '1:24160', '1:24363', '1:21427', '1:24716', '1:50185', '1:62481', '1:62700', '1:63659', '1:67348', '1:68683', '1:68756', '1:69447', '1:69829', '1:32750', '1:34659', '1:35547', '1:40208', '1:40768', '1:40979', '1:43524', '1:43737', '1:43849', '1:43957', '1:96284', '1:97311', '1:105230', '1:54368', '1:54636', '1:57172', '1:56026', '1:56079', '1:56217', '1:56359', '1:57527', '1:58072', '1:58802', '1:55112', '1:55577', '1:56240', '1:87119', '1:68510', '1:68956', '1:69045', '1:100219', '1:103621', '1:105159', '1:103807', '1:104258', '1:104776', '1:105977', '1:106239', '1:106314', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/922D5DD5-5710-EA11-BE57-AC1F6B595F4E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/58A27CA1-A5F6-E911-8978-0CC47A2B0744.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D6BD0C1E-CCF7-E911-9152-AC1F6B567730.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F030EDC5-1AF3-E911-9B33-002590DE6E6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/82662A5E-23EE-E911-8D5B-0CC47A7FC74A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/54235082-12F4-E911-A7A0-0CC47A1E0DCC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C924ADE-C9EE-E911-8597-C4544423E320.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/120CCF0F-55EF-E911-94EA-24BE05C48821.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5072FB7D-5910-EA11-81FB-28924A33B9FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/629E6C83-AC0D-EA11-83C5-0CC47A5FBE25.root']);