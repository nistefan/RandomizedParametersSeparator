import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:61843', '1:62076', '1:62089', '1:62149', '1:62208', '1:62209', '1:63028', '1:79870', '1:80086', '1:80096', '1:80907', '1:88647', '1:91220', '1:92179', '1:66665', '1:66798', '1:66871', '1:66822', '1:66836', '1:66856', '1:77150', '1:77099', '1:77103', '1:77282', '1:77078', '1:77383', '1:88278', '1:88832', '1:32142', '1:24285', '1:32615', '1:26410', '1:33481', '1:33345', '1:33994', '1:35099', '1:35277', '1:35448', '1:42107', '1:42578', '1:104526', '1:104568', '1:104575', '1:51963', '1:52095', '1:52879', '1:52747', '1:98787', '1:98911', '1:99269', '1:99354', '1:99356', '1:99378', '1:99386', '1:102779', '1:102807', '1:102841', '1:102844', '1:102874', '1:102895', '1:46409', '1:46433', '1:46451', '1:46503', '1:46581', '1:46657', '1:46817', '1:46905', '1:74721', '1:65376', '1:70964', '1:71803', '1:73266', '1:73367', '1:74553', '1:74796', '1:92660', '1:92747', '1:92757', '1:4312', '1:4321', '1:4332', '1:4487', '1:4535', '1:4865', '1:18524', '1:18684', '1:18782', '1:18802', '1:18872', '1:18876', '1:19075', '1:24592', '1:24600', '1:98126', '1:98197', '1:305', '1:1804', '1:7363', '1:8092', '1:21511', '1:10010', '1:12537', '1:34401', '1:38744', '1:87579', '1:19998', '1:20088', '1:20116', '1:20710', '1:20753', '1:20758', '1:21008', '1:21021', '1:55815', '1:55819', '1:55913', '1:55982', '1:47252', '1:40359', '1:44319', '1:47514', '1:92023', '1:92135', '1:92631', '1:92832', '1:92834', '1:12907', '1:14456', '1:14752', '1:41943', '1:41015', '1:48881', '1:83158', '1:83204', '1:83977', '1:60206', '1:60300', '1:67736', '1:68047', '1:69559', '1:69593', '1:69738', '1:69873', '1:64349', '1:65468', '1:94471', '1:97191', '1:97208', '1:18', '1:3009', '1:3105', '1:3121', '1:3186', '1:3300', '1:3306', '1:4360', '1:4548', '1:10978', '1:12113', '1:12081', '1:12155', '1:97340', '1:97587', '1:97611', '1:34635', '1:59880', '1:68322', '1:69837', '1:72005', '1:74625', '1:74692', '1:105226', '1:105260', '1:105284', '1:105301', '1:105364', '1:105370', '1:105505', '1:49330', '1:49485', '1:49821', '1:50704', '1:83510', '1:83613', '1:83672', '1:83722', '1:83770', '1:102962', '1:103533', '1:103574', '1:103625', '1:41260', '1:41310', '1:49394', '1:49914', '1:51605', '1:52285', '1:52399', '1:53290', '1:53318', '1:53406', '1:53515', '1:53535', '1:55413', '1:55726', '1:55950', '1:56207', '1:79369', '1:79076', '1:79455', '1:79471', '1:79479', '1:79492', '1:79759', '1:1597', '1:1635', '1:1777', '1:3507', '1:5867', '1:4872', '1:8582', '1:8641', '1:9663', '1:9775', '1:4267', '1:4291', '1:9801', '1:9802', '1:9811', '1:9827', '1:9915', '1:10357', '1:10583', '1:10604', '1:10647', '1:10658', '1:28386', '1:35015', '1:37536', '1:45020', '1:49028', '1:9633', '1:9656', '1:10597', '1:10615', '1:12282', '1:49973', '1:51876', '1:104632', '1:104768', '1:102784', '1:102809', '1:103368', '1:103898', '1:104023', '1:104080', '1:104089', '1:9698', '1:43372', '1:53013', '1:53502', '1:62168', '1:63685', '1:67400', '1:54933', '1:55329', '1:66585', '1:81977', '1:99460', '1:8551', '1:17853', '1:15367', '1:17015', '1:37883', '1:20705', '1:43354', '1:43817', '1:44100', '1:45440', '1:45459', '1:56857', '1:64096', '1:73434', '1:68979', '1:74640', '1:81881', '1:15343', '1:66639', '1:66736', '1:64190', '1:65757', '1:73347', '1:63858', '1:78320', '1:79304', '1:79603', '1:81906', '1:81938', '1:70648', '1:57043', '1:57027', '1:57152', '1:57327', '1:91121', '1:91422', '1:91452', '1:91688', '1:91805', '1:91967', '1:3180', '1:3443', '1:47065', '1:45289', '1:46957', '1:74847', '1:10130', '1:10172', '1:12159', '1:12683', '1:18295', '1:18781', '1:96588', '1:74726', '1:95215', '1:95960', '1:99525', '1:93658', '1:94672', '1:86507', '1:87717', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C2B2B4A5-90FA-E911-A1ED-FA163E596216.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44AD8F54-33FC-E911-BFC1-44A842CFD5D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BC0C7A45-B3FB-E911-9A20-0025905C53AA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/18D4DE3D-06FB-E911-9D07-0CC47A4DEE78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D60A6FA0-CCFC-E911-BDAF-0CC47A5FC679.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BCA2AA4C-68FB-E911-A22D-001CC4A6CCE6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/68A10C47-6CFF-E911-A5E7-0242AC1C0507.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70D242A1-7FFF-E911-934F-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C045F616-49FE-E911-9BA5-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FAD01C50-69FF-E911-BBD7-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE2BDBAA-1F02-EA11-9F99-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84EBD031-DAFE-E911-A032-002590DE39F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9AE2976D-2503-EA11-916D-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8BF48D7-28FF-E911-86D4-AC1F6BC67D46.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8A44B795-0403-EA11-B303-0CC47AFF014C.root']);