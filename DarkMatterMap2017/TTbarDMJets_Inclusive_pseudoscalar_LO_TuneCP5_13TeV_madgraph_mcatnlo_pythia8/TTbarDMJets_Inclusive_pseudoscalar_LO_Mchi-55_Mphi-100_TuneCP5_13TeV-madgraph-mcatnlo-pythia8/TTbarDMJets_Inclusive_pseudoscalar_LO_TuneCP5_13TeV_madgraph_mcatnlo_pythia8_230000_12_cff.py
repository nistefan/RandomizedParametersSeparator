import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:28213', '1:28752', '1:44384', '1:47644', '1:22814', '1:105860', '1:66043', '1:97403', '1:76623', '1:76738', '1:76777', '1:98299', '1:105542', '1:105672', '1:105802', '1:18763', '1:28799', '1:39767', '1:42362', '1:32277', '1:40214', '1:39545', '1:51195', '1:54235', '1:53270', '1:54864', '1:55989', '1:56751', '1:65090', '1:66089', '1:66870', '1:52900', '1:57833', '1:40707', '1:49101', '1:49625', '1:82977', '1:84096', '1:85047', '1:23871', '1:28641', '1:42536', '1:60293', '1:59918', '1:104618', '1:87780', '1:87961', '1:86713', '1:90654', '1:88935', '1:89039', '1:90232', '1:47521', '1:28670', '1:30198', '1:30658', '1:42799', '1:54328', '1:58607', '1:104704', '1:104872', '1:94622', '1:43736', '1:43944', '1:48234', '1:102722', '1:104009', '1:29273', '1:29360', '1:29631', '1:29797', '1:29807', '1:29850', '1:51436', '1:51552', '1:51615', '1:51729', '1:51771', '1:105831', '1:106090', '1:106320', '1:28592', '1:30582', '1:42218', '1:45558', '1:54318', '1:58768', '1:60382', '1:26835', '1:31500', '1:31515', '1:58343', '1:59580', '1:59655', '1:57735', '1:57958', '1:60159', '1:61150', '1:81995', '1:4828', '1:16458', '1:16752', '1:23056', '1:31449', '1:19412', '1:21721', '1:24935', '1:26341', '1:7573', '1:15598', '1:16216', '1:21494', '1:25088', '1:55912', '1:52119', '1:54636', '1:64677', '1:65709', '1:66372', '1:7895', '1:8571', '1:15394', '1:43411', '1:61965', '1:73596', '1:70213', '1:101779', '1:91283', '1:104074', '1:20155', '1:20364', '1:11282', '1:12942', '1:15361', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E9DF7BC-D2F9-E911-B963-B083FED04276.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3C3D00F4-CD0A-EA11-88A9-0025905B8606.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CD12387-68F6-E911-88C2-0CC47AD98CF2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CE823415-E20A-EA11-A829-0CC47A4C8EC6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/40A9763B-3EF4-E911-9F26-A4BF012835C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE6B34A2-FB0A-EA11-92D9-0025905B856C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/88A1CEE3-EF06-EA11-8583-00269E95AF28.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC4A2E9C-CBF2-E911-BAB9-1866DA7F9816.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E65590CA-5900-EA11-8968-0025904B5F8C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D66BAE7C-37F7-E911-A016-FA163EE52FA2.root']);