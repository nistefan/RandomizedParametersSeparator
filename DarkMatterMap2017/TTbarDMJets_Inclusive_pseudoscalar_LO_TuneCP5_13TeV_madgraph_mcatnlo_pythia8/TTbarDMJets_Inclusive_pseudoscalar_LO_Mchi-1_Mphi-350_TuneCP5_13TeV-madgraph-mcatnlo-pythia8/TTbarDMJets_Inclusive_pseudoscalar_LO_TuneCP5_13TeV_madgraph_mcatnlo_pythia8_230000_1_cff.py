import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:51345', '1:51376', '1:51515', '1:53452', '1:53512', '1:53556', '1:53791', '1:54253', '1:58630', '1:4300', '1:5019', '1:5124', '1:5972', '1:9451', '1:13051', '1:18012', '1:18026', '1:18104', '1:18349', '1:18511', '1:18515', '1:18694', '1:18751', '1:18854', '1:18903', '1:18167', '1:18516', '1:18893', '1:19927', '1:19934', '1:19551', '1:27658', '1:27788', '1:45983', '1:18615', '1:18939', '1:22174', '1:28428', '1:28679', '1:28817', '1:28988', '1:41206', '1:41242', '1:41247', '1:3060', '1:3732', '1:3740', '1:7350', '1:7368', '1:10547', '1:6560', '1:57836', '1:51189', '1:51543', '1:85559', '1:97856', '1:72418', '1:70148', '1:70375', '1:56828', '1:57230', '1:57312', '1:57329', '1:57372', '1:58116', '1:82176', '1:82961', '1:83290', '1:2419', '1:2727', '1:2759', '1:3714', '1:6229', '1:6504', '1:6625', '1:6795', '1:6811', '1:6941', '1:8789', '1:7480', '1:7797', '1:7959', '1:10214', '1:10528', '1:10694', '1:11034', '1:11624', '1:11032', '1:11203', '1:11551', '1:15016', '1:14437', '1:14949', '1:57711', '1:58106', '1:58348', '1:58483', '1:58750', '1:58970', '1:5994', '1:7977', '1:8883', '1:8829', '1:9154', '1:9438', '1:9569', '1:9127', '1:5734', '1:5839', '1:6337', '1:14973', '1:16156', '1:31335', '1:31602', '1:31709', '1:17511', '1:17652', '1:17875', '1:17940', '1:18253', '1:41661', '1:41790', '1:41652', '1:41693', '1:41699', '1:41737', '1:45740', '1:55613', '1:18935', '1:18766', '1:22031', '1:45974', '1:80051', '1:80327', '1:77985', '1:78052', '1:78487', '1:21598', '1:21706', '1:98249', '1:98643', '1:103314', '1:103349', '1:103357', '1:103331', '1:103364', '1:103374', '1:103465', '1:5229', '1:6520', '1:8351', '1:8570', '1:8586', '1:10863', '1:43352', '1:43719', '1:39019', '1:44181', '1:56749', '1:56894', '1:57308', '1:101399', '1:101407', '1:26266', '1:75217', '1:81525', '1:32268', '1:46385', '1:53168', '1:55738', '1:62330', '1:62371', '1:62973', '1:94036', '1:92879', '1:101576', '1:101598', '1:1573', '1:1686', '1:1840', '1:2375', '1:28403', '1:39001', '1:39940', '1:42821', '1:55104', '1:15396', '1:16603', '1:16839', '1:13594', '1:14301', '1:14560', '1:25149', '1:25789', '1:25903', '1:26758', '1:23700', '1:31480', '1:23830', '1:95161', '1:53919', '1:53443', '1:83575', '1:104469', '1:97523', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90043704-20FC-E911-8078-0CC47AFCC3D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/58F7196A-76FC-E911-8198-0025905C96E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B65A1C1B-7FFC-E911-92D1-0CC47AFCC392.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/30FB16E9-BC12-EA11-A843-7CD30AC03722.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70BD48D5-3CF5-E911-BBCD-D4856445E5A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E131ABC-63F2-E911-BBAD-441EA157ADE4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/00610B13-6BF2-E911-832F-98039B3B01B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2E996FF0-01F5-E911-BFCE-D4856444A744.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/501EAB60-EC02-EA11-9994-0CC47AFCC6B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3AF7C78E-7106-EA11-9305-0025905C3E68.root']);