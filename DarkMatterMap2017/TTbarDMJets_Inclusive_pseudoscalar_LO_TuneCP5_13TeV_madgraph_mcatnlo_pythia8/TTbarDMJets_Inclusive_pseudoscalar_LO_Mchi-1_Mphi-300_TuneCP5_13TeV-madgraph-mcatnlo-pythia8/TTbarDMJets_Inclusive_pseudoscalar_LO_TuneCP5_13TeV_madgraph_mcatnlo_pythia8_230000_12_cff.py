import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:27171', '1:28354', '1:40859', '1:45392', '1:62707', '1:80405', '1:95583', '1:95811', '1:96085', '1:96752', '1:97137', '1:97888', '1:98024', '1:75976', '1:80104', '1:80500', '1:80502', '1:76082', '1:76260', '1:80299', '1:22765', '1:27429', '1:42062', '1:42125', '1:29924', '1:49803', '1:51370', '1:51796', '1:52877', '1:54500', '1:82306', '1:75291', '1:76186', '1:67223', '1:67905', '1:96919', '1:52239', '1:55227', '1:56148', '1:43740', '1:48924', '1:89122', '1:25710', '1:28845', '1:29815', '1:30817', '1:32526', '1:32936', '1:32964', '1:39352', '1:39497', '1:39734', '1:47020', '1:54391', '1:72342', '1:75930', '1:76879', '1:102480', '1:89179', '1:29648', '1:42256', '1:44852', '1:29026', '1:44892', '1:42158', '1:54374', '1:101894', '1:92331', '1:94114', '1:48275', '1:48327', '1:77167', '1:92350', '1:95101', '1:98195', '1:106381', '1:106413', '1:102460', '1:102533', '1:103947', '1:29346', '1:29400', '1:51649', '1:105826', '1:105942', '1:106032', '1:19670', '1:28830', '1:28908', '1:28909', '1:29451', '1:39035', '1:39870', '1:45259', '1:56897', '1:54690', '1:61747', '1:26833', '1:26985', '1:31986', '1:31490', '1:31378', '1:57612', '1:58834', '1:61816', '1:62182', '1:62746', '1:42723', '1:94695', '1:4653', '1:7259', '1:9947', '1:13976', '1:23419', '1:17436', '1:19084', '1:23080', '1:20241', '1:25161', '1:2843', '1:49993', '1:54772', '1:54788', '1:56251', '1:54066', '1:55915', '1:75593', '1:65333', '1:71469', '1:13964', '1:3472', '1:11065', '1:11322', '1:16530', '1:26137', '1:53730', '1:71570', '1:73622', '1:88195', '1:95325', '1:20076', '1:20110', '1:11641', '1:11727', '1:11799', '1:12343', '1:14110', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E9DF7BC-D2F9-E911-B963-B083FED04276.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3C3D00F4-CD0A-EA11-88A9-0025905B8606.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CD12387-68F6-E911-88C2-0CC47AD98CF2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CE823415-E20A-EA11-A829-0CC47A4C8EC6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40A9763B-3EF4-E911-9F26-A4BF012835C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE6B34A2-FB0A-EA11-92D9-0025905B856C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/88A1CEE3-EF06-EA11-8583-00269E95AF28.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC4A2E9C-CBF2-E911-BAB9-1866DA7F9816.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E65590CA-5900-EA11-8968-0025904B5F8C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D66BAE7C-37F7-E911-A016-FA163EE52FA2.root']);