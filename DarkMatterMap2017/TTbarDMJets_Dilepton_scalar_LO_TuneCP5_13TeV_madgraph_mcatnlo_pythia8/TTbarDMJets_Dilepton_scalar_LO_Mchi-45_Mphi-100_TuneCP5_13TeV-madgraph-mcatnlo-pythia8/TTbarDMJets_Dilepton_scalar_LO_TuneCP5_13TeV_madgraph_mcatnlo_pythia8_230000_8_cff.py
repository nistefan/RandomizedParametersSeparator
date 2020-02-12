import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1195', '1:4225', '1:7400', '1:9151', '1:9418', '1:26138', '1:18834', '1:8937', '1:18246', '1:21580', '1:28295', '1:105093', '1:105119', '1:105120', '1:105158', '1:105165', '1:105176', '1:103335', '1:14798', '1:14958', '1:14998', '1:15021', '1:16013', '1:16654', '1:28504', '1:79051', '1:79107', '1:79265', '1:79396', '1:96342', '1:96424', '1:96869', '1:96589', '1:96682', '1:59624', '1:59746', '1:59870', '1:59874', '1:59678', '1:62978', '1:84584', '1:84677', '1:84723', '1:84776', '1:84899', '1:96373', '1:96257', '1:91242', '1:91254', '1:80815', '1:81823', '1:81829', '1:81845', '1:81846', '1:81464', '1:81495', '1:81513', '1:81519', '1:96096', '1:96322', '1:96473', '1:100885', '1:98875', '1:99932', '1:100014', '1:91612', '1:91908', '1:91936', '1:100032', '1:33694', '1:67337', '1:46702', '1:47636', '1:47975', '1:72388', '1:78090', '1:83065', '1:79949', '1:81892', '1:85426', '1:85452', '1:75541', '1:10431', '1:15440', '1:15488', '1:16655', '1:27310', '1:27350', '1:27367', '1:27719', '1:28384', '1:28393', '1:41536', '1:41602', '1:41618', '1:12129', '1:18508', '1:21125', '1:19550', '1:19572', '1:21139', '1:21288', '1:21615', '1:21627', '1:21642', '1:21706', '1:21745', '1:15380', '1:27858', '1:32900', '1:20805', '1:20839', '1:20854', '1:20864', '1:21055', '1:40289', '1:40419', '1:40522', '1:40568', '1:43535', '1:43529', '1:59546', '1:60590', '1:60647', '1:60983', '1:60981', '1:41106', '1:41240', '1:41347', '1:41503', '1:44271', '1:45169', '1:46257', '1:46354', '1:48178', '1:48245', '1:48264', '1:48384', '1:4099', '1:4140', '1:4171', '1:4229', '1:16022', '1:16150', '1:45757', '1:47672', '1:47686', '1:47716', '1:51898', '1:52926', '1:64800', '1:64828', '1:64890', '1:64940', '1:65211', '1:80364', '1:80378', '1:84139', '1:84152', '1:85378', '1:85387', '1:86331', '1:86353', '1:86485', '1:86700', '1:86703', '1:86758', '1:96631', '1:105731', '1:105755', '1:27739', '1:32805', '1:32857', '1:28442', '1:28700', '1:28969', '1:28359', '1:28879', '1:32759', '1:32940', '1:70906', '1:73398', '1:85582', '1:98072', '1:3598', '1:4913', '1:334', '1:1845', '1:3280', '1:4440', '1:17255', '1:17284', '1:18454', '1:15673', '1:27696', '1:28218', '1:37420', '1:27821', '1:32739', '1:36072', '1:38051', '1:38438', '1:42482', '1:38574', '1:38779', '1:42956', '1:86343', '1:91409', '1:91874', '1:94677', '1:96073', '1:40541', '1:43875', '1:45192', '1:45448', '1:38939', '1:43587', '1:34759', '1:51652', '1:51668', '1:52706', '1:52697', '1:41685', '1:48982', '1:51591', '1:51993', '1:49884', '1:41761', '1:39318', '1:62363', '1:62644', '1:67009', '1:67208', '1:67317', '1:67762', '1:56644', '1:58362', '1:58807', '1:58817', '1:61241', '1:60156', '1:60407', '1:76694', '1:76751', '1:85459', '1:96621', '1:98543', '1:97016', '1:100747', '1:5333', '1:5890', '1:7041', '1:7080', '1:7082', '1:7110', '1:7112', '1:7325', '1:10391', '1:10530', '1:10413', '1:10499', '1:10526', '1:10549', '1:12374', '1:14872', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E25E124-31F7-E911-BE4E-0CC47A1E0DC2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCE60212-4D10-EA11-BEE3-90E2BAD5729C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C9C3A0A-7FFF-E911-8CD0-0CC47A4DEDD4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/90D49EF7-13F6-E911-9659-38EAA78E2C94.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D8B5CBBC-35F0-E911-94CF-1418774A25AB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E06943C6-D5EF-E911-A278-10983627C3C1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1ABC4644-64F4-E911-A4E7-FA163E84EE9A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AF65E7A-6EF3-E911-9E38-141877641875.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0A2F042B-71EF-E911-9535-0CC47AF9739E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AA4C6F18-8AF7-E911-80DC-0CC47AD9901C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5EAB8AB1-6810-EA11-9F96-008CFA197D98.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/10AE8E18-9802-EA11-8C36-B083FED138B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0407705F-5610-EA11-BCA2-0CC47AD98CEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5E63A65D-5B07-EA11-9816-0CC47A7C345E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EA78600-8003-EA11-98EB-405CFDFF480E.root']);