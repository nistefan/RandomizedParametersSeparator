import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:61792', '1:61803', '1:61930', '1:62233', '1:80128', '1:80137', '1:80289', '1:80256', '1:92173', '1:66648', '1:66885', '1:66866', '1:69255', '1:69694', '1:77158', '1:77270', '1:77378', '1:88314', '1:24617', '1:24743', '1:32496', '1:32680', '1:32690', '1:33102', '1:33488', '1:33986', '1:32586', '1:36983', '1:38100', '1:104394', '1:104406', '1:104517', '1:104518', '1:104521', '1:104522', '1:104554', '1:104717', '1:51949', '1:52258', '1:52267', '1:52645', '1:52509', '1:52765', '1:99261', '1:99311', '1:99323', '1:102775', '1:102894', '1:46732', '1:46874', '1:70269', '1:71675', '1:71790', '1:71921', '1:70617', '1:70677', '1:73320', '1:73935', '1:73329', '1:91378', '1:93226', '1:92642', '1:92644', '1:92753', '1:4345', '1:4469', '1:4461', '1:4483', '1:4810', '1:4820', '1:4497', '1:18647', '1:18804', '1:18980', '1:19006', '1:19007', '1:19015', '1:19020', '1:19219', '1:98186', '1:98211', '1:98214', '1:98448', '1:1772', '1:1836', '1:1877', '1:4062', '1:2162', '1:9654', '1:7304', '1:8455', '1:32860', '1:33061', '1:35899', '1:92786', '1:21238', '1:20747', '1:54783', '1:55837', '1:55897', '1:55949', '1:43368', '1:43574', '1:45028', '1:45182', '1:45446', '1:46219', '1:72943', '1:92127', '1:92449', '1:88654', '1:12931', '1:12949', '1:14606', '1:47190', '1:35671', '1:43168', '1:43334', '1:39979', '1:48294', '1:48937', '1:49316', '1:48011', '1:48771', '1:49705', '1:83162', '1:83282', '1:83247', '1:83249', '1:83273', '1:83981', '1:60221', '1:60211', '1:60362', '1:68714', '1:69201', '1:69552', '1:69766', '1:64191', '1:64656', '1:97012', '1:97022', '1:97096', '1:97200', '1:3065', '1:3072', '1:3302', '1:4690', '1:12016', '1:12111', '1:12142', '1:12161', '1:97325', '1:97368', '1:97429', '1:97437', '1:97452', '1:97568', '1:97675', '1:34786', '1:37709', '1:56670', '1:57725', '1:58448', '1:74544', '1:74358', '1:74546', '1:74688', '1:103440', '1:105250', '1:105276', '1:48600', '1:49174', '1:49212', '1:49571', '1:49618', '1:49709', '1:50184', '1:83392', '1:83441', '1:83543', '1:83547', '1:83550', '1:83576', '1:83601', '1:83619', '1:83670', '1:83769', '1:83803', '1:103159', '1:103564', '1:41402', '1:49002', '1:49502', '1:50387', '1:53046', '1:53179', '1:53532', '1:55662', '1:79092', '1:76692', '1:103239', '1:103259', '1:103340', '1:103371', '1:103690', '1:1582', '1:1621', '1:1637', '1:1604', '1:1674', '1:1729', '1:8692', '1:12798', '1:5594', '1:7218', '1:34113', '1:34863', '1:10973', '1:9918', '1:10440', '1:10754', '1:10902', '1:9576', '1:10627', '1:10650', '1:10704', '1:37904', '1:36922', '1:38543', '1:49119', '1:50019', '1:9660', '1:9714', '1:12012', '1:41846', '1:48685', '1:49743', '1:51887', '1:54606', '1:54704', '1:91067', '1:104211', '1:104801', '1:106127', '1:102729', '1:103406', '1:104117', '1:3143', '1:3135', '1:9453', '1:8608', '1:60937', '1:62252', '1:80993', '1:81979', '1:81987', '1:81992', '1:16131', '1:17949', '1:15078', '1:26903', '1:32262', '1:66647', '1:73385', '1:72751', '1:66995', '1:71614', '1:14198', '1:17162', '1:17550', '1:17609', '1:64491', '1:66435', '1:64949', '1:65106', '1:65125', '1:65766', '1:65823', '1:66097', '1:72108', '1:70307', '1:70731', '1:71272', '1:67450', '1:68499', '1:102349', '1:80499', '1:81304', '1:81911', '1:88282', '1:88698', '1:91208', '1:70104', '1:70137', '1:57214', '1:57252', '1:57045', '1:57118', '1:57284', '1:91076', '1:91330', '1:91436', '1:91655', '1:91673', '1:91909', '1:1801', '1:3609', '1:4723', '1:86564', '1:91954', '1:97580', '1:92951', '1:93541', '1:102636', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C2B2B4A5-90FA-E911-A1ED-FA163E596216.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44AD8F54-33FC-E911-BFC1-44A842CFD5D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BC0C7A45-B3FB-E911-9A20-0025905C53AA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/18D4DE3D-06FB-E911-9D07-0CC47A4DEE78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D60A6FA0-CCFC-E911-BDAF-0CC47A5FC679.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BCA2AA4C-68FB-E911-A22D-001CC4A6CCE6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/68A10C47-6CFF-E911-A5E7-0242AC1C0507.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70D242A1-7FFF-E911-934F-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C045F616-49FE-E911-9BA5-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FAD01C50-69FF-E911-BBD7-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE2BDBAA-1F02-EA11-9F99-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84EBD031-DAFE-E911-A032-002590DE39F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9AE2976D-2503-EA11-916D-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8BF48D7-28FF-E911-86D4-AC1F6BC67D46.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8A44B795-0403-EA11-B303-0CC47AFF014C.root']);