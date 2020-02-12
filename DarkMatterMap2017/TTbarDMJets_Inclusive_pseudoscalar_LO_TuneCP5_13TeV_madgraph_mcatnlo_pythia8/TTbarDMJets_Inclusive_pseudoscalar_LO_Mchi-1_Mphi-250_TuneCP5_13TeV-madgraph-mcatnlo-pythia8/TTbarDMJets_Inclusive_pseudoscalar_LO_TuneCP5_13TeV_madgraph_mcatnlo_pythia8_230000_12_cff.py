import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:18336', '1:30916', '1:40834', '1:98234', '1:76857', '1:76939', '1:80404', '1:75883', '1:80185', '1:105679', '1:22758', '1:28031', '1:43936', '1:40142', '1:55152', '1:55424', '1:67624', '1:71542', '1:74510', '1:52491', '1:54083', '1:52154', '1:46098', '1:77705', '1:28892', '1:30022', '1:32240', '1:42966', '1:45532', '1:54131', '1:56840', '1:60726', '1:59025', '1:59785', '1:79875', '1:81064', '1:82635', '1:84028', '1:86720', '1:86745', '1:87318', '1:29365', '1:54741', '1:55036', '1:58159', '1:58358', '1:60252', '1:102536', '1:43758', '1:48137', '1:91991', '1:94060', '1:96422', '1:101919', '1:101967', '1:102368', '1:102446', '1:104209', '1:29718', '1:29682', '1:52653', '1:105830', '1:106029', '1:106086', '1:106295', '1:28902', '1:29524', '1:30615', '1:42864', '1:58172', '1:59271', '1:61214', '1:26678', '1:26686', '1:26811', '1:55952', '1:57725', '1:60058', '1:59632', '1:62769', '1:86156', '1:102824', '1:104819', '1:93560', '1:6445', '1:4166', '1:10445', '1:23208', '1:23370', '1:21281', '1:19874', '1:24519', '1:26778', '1:2888', '1:12639', '1:5160', '1:74624', '1:54457', '1:55003', '1:55813', '1:53573', '1:55891', '1:66234', '1:4376', '1:11232', '1:13307', '1:89111', '1:96788', '1:20028', '1:20037', '1:20097', '1:20169', '1:20170', '1:20178', '1:20179', '1:11442', '1:11547', '1:13171', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E9DF7BC-D2F9-E911-B963-B083FED04276.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3C3D00F4-CD0A-EA11-88A9-0025905B8606.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CD12387-68F6-E911-88C2-0CC47AD98CF2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CE823415-E20A-EA11-A829-0CC47A4C8EC6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40A9763B-3EF4-E911-9F26-A4BF012835C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE6B34A2-FB0A-EA11-92D9-0025905B856C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/88A1CEE3-EF06-EA11-8583-00269E95AF28.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC4A2E9C-CBF2-E911-BAB9-1866DA7F9816.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E65590CA-5900-EA11-8968-0025904B5F8C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D66BAE7C-37F7-E911-A016-FA163EE52FA2.root']);