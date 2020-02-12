import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:5924', '1:330', '1:2187', '1:6412', '1:779', '1:9064', '1:9615', '1:14048', '1:17866', '1:21626', '1:26918', '1:38065', '1:37900', '1:39203', '1:46685', '1:5372', '1:8054', '1:14801', '1:20546', '1:20838', '1:13362', '1:16624', '1:17064', '1:27891', '1:28940', '1:37229', '1:33718', '1:38027', '1:33927', '1:36063', '1:17192', '1:21917', '1:18501', '1:20803', '1:21033', '1:21363', '1:31468', '1:62036', '1:73585', '1:75226', '1:75724', '1:75887', '1:62812', '1:59593', '1:68693', '1:69462', '1:38226', '1:91360', '1:73855', '1:229', '1:3178', '1:3487', '1:4683', '1:5051', '1:5087', '1:2347', '1:5109', '1:9233', '1:9893', '1:10923', '1:17033', '1:17521', '1:17943', '1:15879', '1:16395', '1:57593', '1:24011', '1:24731', '1:27159', '1:28674', '1:30256', '1:39158', '1:61045', '1:79413', '1:72038', '1:78506', '1:80755', '1:81888', '1:86491', '1:5366', '1:6743', '1:6963', '1:7562', '1:8168', '1:13083', '1:13858', '1:28702', '1:29840', '1:29926', '1:51462', '1:15830', '1:17212', '1:18544', '1:34900', '1:34933', '1:35848', '1:37938', '1:26361', '1:26943', '1:36786', '1:86629', '1:86762', '1:86796', '1:86843', '1:24547', '1:7916', '1:10212', '1:8004', '1:15892', '1:9869', '1:13444', '1:34387', '1:27904', '1:49997', '1:57405', '1:58955', '1:67467', '1:67522', '1:67761', '1:69473', '1:75586', '1:75974', '1:421', '1:1576', '1:4250', '1:4289', '1:4917', '1:4967', '1:5303', '1:19371', '1:19844', '1:38227', '1:21715', '1:37620', '1:39493', '1:39784', '1:60864', '1:6539', '1:9071', '1:9579', '1:6855', '1:7215', '1:8229', '1:9780', '1:10668', '1:13357', '1:15299', '1:51441', '1:14835', '1:15873', '1:13329', '1:16667', '1:16755', '1:13627', '1:14336', '1:30324', '1:34194', '1:35147', '1:31526', '1:31801', '1:81272', '1:81993', '1:50121', '1:56226', '1:56740', '1:61779', '1:80355', '1:29182', '1:34879', '1:28298', '1:28982', '1:30156', '1:32583', '1:37237', '1:34948', '1:37859', '1:38242', '1:35472', '1:35975', '1:37320', '1:37346', '1:40409', '1:52552', '1:62393', '1:85338', '1:79951', '1:8774', '1:10547', '1:17906', '1:20351', '1:62777', '1:71108', '1:91304', '1:63314', '1:63432', '1:63543', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/440F2EF5-E1F2-E911-9C42-3CFDFE639760.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/084EC564-3BF4-E911-BB13-782BCB398AB3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1AB17DBB-D1F2-E911-915F-F01FAFE5F67D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D2F07667-1BF3-E911-9149-1866DA7F96FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/623CBCFE-5DF3-E911-A913-1866DA85D853.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D6F9C4ED-BDF6-E911-A882-F0D4E2E52394.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4293777-74F7-E911-A059-EC0D9A82237E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BAB2D1CF-4BF6-E911-B5F6-003048F59755.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5E84A7CC-2EF8-E911-816D-0CC47AA989C4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A742CF5-FEF8-E911-8BF1-AC1F6B0DE490.root']);