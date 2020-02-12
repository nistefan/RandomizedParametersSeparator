import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:68498', '1:70196', '1:70381', '1:70725', '1:70732', '1:71347', '1:71359', '1:71540', '1:71694', '1:71727', '1:70344', '1:70453', '1:70716', '1:73809', '1:73867', '1:73922', '1:73923', '1:74696', '1:74710', '1:71692', '1:87081', '1:87475', '1:88105', '1:94001', '1:97166', '1:97434', '1:98528', '1:99057', '1:99315', '1:99597', '1:100741', '1:74759', '1:95321', '1:95450', '1:96791', '1:96880', '1:97614', '1:98009', '1:98285', '1:99119', '1:102068', '1:87147', '1:88310', '1:89323', '1:89715', '1:89723', '1:90998', '1:96020', '1:96291', '1:96601', '1:89840', '1:69776', '1:70404', '1:70497', '1:70689', '1:71017', '1:71500', '1:72613', '1:85705', '1:85775', '1:85896', '1:85973', '1:86334', '1:86406', '1:86737', '1:101633', '1:101655', '1:77715', '1:77923', '1:77942', '1:78716', '1:79168', '1:79249', '1:79271', '1:79317', '1:79647', '1:79797', '1:79819', '1:79941', '1:77741', '1:78129', '1:78602', '1:79030', '1:79265', '1:79266', '1:79387', '1:79631', '1:79906', '1:90141', '1:90633', '1:102045', '1:102368', '1:90199', '1:94808', '1:95311', '1:91780', '1:88823', '1:90436', '1:94538', '1:94621', '1:94996', '1:95476', '1:97044', '1:100680', '1:101975', '1:78299', '1:95798', '1:99556', '1:102237', '1:88591', '1:95556', '1:97346', '1:97370', '1:98127', '1:58613', '1:75754', '1:15223', '1:32485', '1:67063', '1:69285', '1:71808', '1:75135', '1:78921', '1:23404', '1:27389', '1:28282', '1:28539', '1:25775', '1:28675', '1:32201', '1:32849', '1:32980', '1:31143', '1:31386', '1:32200', '1:32443', '1:32624', '1:32738', '1:32808', '1:32810', '1:50700', '1:50944', '1:6477', '1:6790', '1:7587', '1:8605', '1:8628', '1:8733', '1:8976', '1:9194', '1:10016', '1:14537', '1:8880', '1:9921', '1:13230', '1:15858', '1:18011', '1:20708', '1:36231', '1:36799', '1:38089', '1:38212', '1:38933', '1:38999', '1:36698', '1:36789', '1:37947', '1:38137', '1:38684', '1:38748', '1:100147', '1:100269', '1:101779', '1:101810', '1:101587', '1:101662', '1:101902', '1:56143', '1:57831', '1:95087', '1:95421', '1:96533', '1:98391', '1:98475', '1:99535', '1:101151', '1:96062', '1:98922', '1:58319', '1:99191', '1:96759', '1:99768', '1:101282', '1:96745', '1:6038', '1:6445', '1:8358', '1:10046', '1:13360', '1:6914', '1:6984', '1:7253', '1:8660', '1:8998', '1:9327', '1:9806', '1:9976', '1:10012', '1:10147', '1:10941', '1:14149', '1:20500', '1:68123', '1:64210', '1:71596', '1:71983', '1:74827', '1:77291', '1:77915', '1:78044', '1:79479', '1:81041', '1:81302', '1:81564', '1:67409', '1:70034', '1:70237', '1:77896', '1:80946', '1:85273', '1:85975', '1:88965', '1:88992', '1:89047', '1:90630', '1:70708', '1:77872', '1:85626', '1:86741', '1:86779', '1:88225', '1:88777', '1:88784', '1:88840', '1:87596', '1:89628', '1:94235', '1:49039', '1:51294', '1:51563', '1:54088', '1:54179', '1:54268', '1:59299', '1:60870', '1:50298', '1:53532', '1:55054', '1:62573', '1:62875', '1:64233', '1:54533', '1:62087', '1:61434', '1:61436', '1:102095', '1:102099', '1:102174', '1:102331', '1:102347', '1:102353', '1:102362', '1:102426', '1:102429', '1:68763', '1:69488', '1:69538', '1:68830', '1:68904', '1:69505', '1:75084', '1:75786', '1:76017', '1:76387', '1:70219', '1:85656', '1:87190', '1:79447', '1:79984', '1:38314', '1:38338', '1:38771', '1:38852', '1:46533', '1:89591', '1:94580', '1:94598', '1:94716', '1:94767', '1:94818', '1:94835', '1:94845', '1:94860', '1:94872', '1:94884', '1:94928', '1:94937', '1:94981', '1:95082', '1:95096', '1:95443', '1:95518', '1:95566', '1:95749', '1:95773', '1:95939', '1:98015', '1:98023', '1:98104', '1:98252', '1:99033', '1:99266', '1:97609', '1:97749', '1:97845', '1:97903', '1:97935', '1:98007', '1:67553', '1:67558', '1:67578', '1:67583', '1:67916', '1:67997', '1:85865', '1:85883', '1:85978', '1:86002', '1:86013', '1:86122', '1:86126', '1:86387', '1:86505', '1:86667', '1:86751', '1:86804', '1:86832', '1:86922', '1:87122', '1:87198', '1:86278', '1:86313', '1:91074', '1:91213', '1:91238', '1:91382', '1:91806', '1:59768', '1:60300', '1:68198', '1:68303', '1:68582', '1:68896', '1:68919', '1:69089', '1:69313', '1:69340', '1:75399', '1:75423', '1:75539', '1:68026', '1:68519', '1:70505', '1:70527', '1:70612', '1:70615', '1:70624', '1:70632', '1:70650', '1:70667', '1:70683', '1:70727', '1:70735', '1:70759', '1:70762', '1:70790', '1:70621', '1:70637', '1:70696', '1:70714', '1:70913', '1:68469', '1:69343', '1:69470', '1:69835', '1:70016', '1:70073', '1:70080', '1:70113', '1:70299', '1:70694', '1:70718', '1:70723', '1:70752', '1:70845', '1:70930', '1:71781', '1:71800', '1:71803', '1:71806', '1:71898', '1:72030', '1:72058', '1:77116', '1:77318', '1:77338', '1:77376', '1:77431', '1:77435', '1:73369', '1:73385', '1:74149', '1:74631', '1:75645', '1:75873', '1:75550', '1:75557', '1:75656', '1:75738', '1:75749', '1:75900', '1:75929', '1:76080', '1:76142', '1:76451', '1:76473', '1:76604', '1:80944', '1:88562', '1:91200', '1:91427', '1:91552', '1:91567', '1:91728', '1:91885', '1:91894', '1:91945', '1:91964', '1:99765', '1:99821', '1:99947', '1:99960', '1:99966', '1:98753', '1:78330', '1:90589', '1:6711', '1:6720', '1:6727', '1:6873', '1:6880', '1:6947', '1:7023', '1:7028', '1:7134', '1:7166', '1:7248', '1:7258', '1:7457', '1:7475', '1:7514', '1:7742', '1:7961', '1:7992', '1:7452', '1:59176', '1:59224', '1:59235', '1:59644', '1:59677', '1:59701', '1:59756', '1:59870', '1:59930', '1:59959', '1:59985', '1:60298', '1:60816', '1:61083', '1:61212', '1:61231', '1:63209', '1:63332', '1:63308', '1:63341', '1:63519', '1:63703', '1:63705', '1:63530', '1:63532', '1:63624', '1:63630', '1:31535', '1:31537', '1:31617', '1:31697', '1:31726', '1:31854', '1:31884', '1:32284', '1:32311', '1:89373', '1:89440', '1:89609', '1:89767', '1:89827', '1:89834', '1:89899', '1:90142', '1:88307', '1:88314', '1:88315', '1:88550', '1:88959', '1:89095', '1:89174', '1:89211', '1:89212', '1:89218', '1:89271', '1:89342', '1:89447', '1:89511', '1:89563', '1:89564', '1:89585', '1:89663', '1:90230', '1:90363', '1:90738', '1:90851', '1:91932', '1:91177', '1:91679', '1:54684', '1:54713', '1:54725', '1:54729', '1:54748', '1:54784', '1:54813', '1:54815', '1:54833', '1:54928', '1:54932', '1:55267', '1:55275', '1:55498', '1:56007', '1:56089', '1:56153', '1:56356', '1:56057', '1:62100', '1:62287', '1:63071', '1:63997', '1:62979', '1:63976', '1:64014', '1:64072', '1:64098', '1:64137', '1:64254', '1:64365', '1:67077', '1:67190', '1:67085', '1:68608', '1:69481', '1:69736', '1:69969', '1:69826', '1:69910', '1:75105', '1:76022', '1:34812', '1:34835', '1:34053', '1:34142', '1:34253', '1:34335', '1:34342', '1:34455', '1:34465', '1:34491', '1:34531', '1:34561', '1:34572', '1:34495', '1:34520', '1:34602', '1:34642', '1:34690', '1:34707', '1:34739', '1:34758', '1:34782', '1:34855', '1:35022', '1:35024', '1:51967', '1:50751', '1:50761', '1:50776', '1:50800', '1:50963', '1:50986', '1:51173', '1:51465', '1:51521', '1:51628', '1:51683', '1:51862', '1:52017', '1:52132', '1:50890', '1:51035', '1:51505', '1:51546', '1:51715', '1:51887', '1:52495', '1:53041', '1:70162', '1:70671', '1:90845', '1:90860', '1:90950', '1:94258', '1:94266', '1:94296', '1:94315', '1:94756', '1:94904', '1:70869', '1:71289', '1:71393', '1:71466', '1:71470', '1:71492', '1:71559', '1:71574', '1:70963', '1:71121', '1:71198', '1:71704', '1:72200', '1:72226', '1:73862', '1:85463', '1:85625', '1:87123', '1:87423', '1:89418', '1:94024', '1:94369', '1:94875', '1:94887', '1:95069', '1:95202', '1:91836', '1:91843', '1:91973', '1:94041', '1:94096', '1:94227', '1:94299', '1:94381', '1:79890', '1:81927', '1:81973', '1:85018', '1:81935', '1:81992', '1:85014', '1:85017', '1:85039', '1:85041', '1:85059', '1:85063', '1:85205', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A441E47-060B-EA11-B8B7-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/163322C0-3913-EA11-A823-509A4C730E32.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40429EB5-3913-EA11-8322-0CC47A4D7654.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B830E40B-4BFA-E911-AA8B-00259048AD6A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6A82999A-100B-EA11-A7F8-0025905A60A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E82B862B-29FD-E911-AE56-509A4C9F8888.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/826B13CB-B4FC-E911-8A17-509A4C9EF8EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2668A328-EA06-EA11-BCB2-0CC47A5FC2A1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D2A86121-C901-EA11-8DD5-509A4C9EF8FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/303FC9AB-D400-EA11-BF9F-38EAA78D8ADC.root']);