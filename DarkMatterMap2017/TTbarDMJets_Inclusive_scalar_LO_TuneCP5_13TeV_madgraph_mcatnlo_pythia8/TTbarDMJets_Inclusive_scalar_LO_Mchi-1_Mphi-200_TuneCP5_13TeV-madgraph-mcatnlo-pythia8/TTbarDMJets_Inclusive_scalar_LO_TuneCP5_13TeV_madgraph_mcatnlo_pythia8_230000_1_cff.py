import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:7741', '1:8546', '1:14966', '1:6289', '1:30172', '1:35986', '1:28678', '1:57972', '1:8823', '1:14153', '1:17824', '1:18309', '1:15570', '1:16937', '1:20574', '1:37406', '1:37567', '1:46211', '1:52048', '1:58650', '1:54209', '1:59839', '1:55503', '1:55645', '1:55286', '1:55361', '1:55398', '1:72519', '1:9156', '1:26647', '1:26910', '1:14465', '1:18478', '1:18930', '1:78203', '1:40306', '1:52701', '1:52993', '1:52105', '1:54931', '1:68347', '1:95473', '1:99483', '1:101524', '1:101532', '1:54371', '1:54472', '1:57239', '1:78660', '1:78718', '1:78547', '1:78655', '1:88052', '1:88385', '1:88416', '1:88425', '1:88465', '1:89126', '1:75991', '1:76075', '1:76185', '1:76279', '1:76283', '1:76492', '1:76586', '1:76603', '1:75563', '1:75805', '1:87997', '1:89026', '1:88294', '1:88365', '1:102270', '1:102376', '1:15926', '1:20479', '1:23058', '1:23999', '1:32051', '1:37792', '1:34031', '1:34800', '1:53447', '1:74753', '1:53753', '1:1388', '1:1820', '1:1867', '1:72924', '1:72188', '1:72292', '1:72750', '1:87655', '1:88153', '1:71278', '1:71518', '1:71827', '1:71829', '1:94546', '1:94784', '1:94802', '1:96059', '1:96408', '1:98647', '1:99079', '1:35313', '1:35703', '1:69922', '1:71055', '1:72245', '1:69988', '1:75382', '1:76376', '1:76459', '1:76959', '1:56130', '1:56810', '1:56925', '1:57190', '1:56906', '1:57124', '1:61488', '1:61555', '1:61708', '1:61871', '1:63093', '1:61704', '1:61735', '1:63159', '1:101070', '1:1747', '1:3218', '1:9183', '1:77161', '1:76829', '1:49255', '1:40098', '1:46555', '1:58770', '1:60424', '1:87437', '1:87534', '1:94790', '1:94857', '1:94970', '1:95179', '1:101086', '1:100349', '1:101950', '1:73478', '1:73689', '1:73704', '1:86367', '1:86590', '1:88418', '1:88451', '1:88628', '1:88678', '1:88762', '1:96943', '1:96926', '1:96975', '1:101641', '1:89161', '1:89387', '1:89720', '1:96389', '1:96324', '1:96046', '1:96532', '1:96813', '1:101980', '1:101990', '1:100435', '1:100532', '1:100399', '1:101891', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7CF3F789-48F8-E911-9E95-AC1F6B34AC86.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94F3A535-95F8-E911-B0C4-A4BF01025A8B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC6D87E5-FEF8-E911-860A-20040FE9CF40.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6E13167A-04F9-E911-822D-AC1F6B0DE296.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02456201-BDFC-E911-8979-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B6336465-ACFA-E911-BCEA-0CC47AD98D6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6EDE0848-29FD-E911-8BAF-00215A49197E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/721E3057-28FC-E911-AF04-38EAA78D8960.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E05E587-1AFD-E911-8B60-002590DE6E1E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2236C272-34FD-E911-A005-0CC47A7E6B00.root']);