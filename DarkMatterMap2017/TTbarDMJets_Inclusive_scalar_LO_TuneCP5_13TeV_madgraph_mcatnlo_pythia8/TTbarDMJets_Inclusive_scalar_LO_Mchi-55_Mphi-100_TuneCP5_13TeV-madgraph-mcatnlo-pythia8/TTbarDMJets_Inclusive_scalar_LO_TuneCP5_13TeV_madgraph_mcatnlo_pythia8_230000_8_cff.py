import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:17328', '1:17409', '1:38698', '1:90861', '1:95230', '1:101733', '1:102104', '1:39331', '1:39906', '1:40408', '1:49115', '1:27634', '1:27956', '1:27957', '1:28202', '1:28649', '1:28811', '1:30191', '1:28082', '1:28859', '1:49667', '1:49734', '1:49849', '1:50090', '1:50037', '1:50159', '1:50377', '1:50349', '1:50487', '1:52790', '1:51210', '1:62842', '1:62914', '1:68852', '1:28607', '1:94514', '1:99659', '1:94850', '1:88058', '1:88454', '1:63729', '1:63735', '1:70645', '1:6094', '1:8791', '1:9956', '1:10509', '1:7944', '1:8240', '1:8556', '1:10049', '1:20652', '1:40460', '1:31127', '1:31207', '1:31365', '1:34946', '1:55349', '1:67322', '1:68731', '1:68736', '1:60856', '1:50805', '1:56325', '1:56498', '1:58277', '1:32062', '1:50582', '1:52869', '1:55949', '1:68733', '1:62268', '1:68281', '1:68898', '1:72111', '1:69179', '1:74318', '1:75939', '1:77434', '1:78902', '1:101399', '1:71104', '1:88730', '1:88741', '1:79433', '1:79461', '1:79822', '1:102363', '1:97042', '1:98022', '1:81525', '1:81639', '1:81708', '1:87486', '1:90054', '1:90083', '1:90526', '1:90789', '1:101443', '1:102031', '1:99825', '1:100007', '1:99921', '1:100031', '1:100176', '1:101240', '1:101660', '1:101833', '1:31368', '1:52510', '1:32456', '1:58141', '1:3059', '1:3302', '1:4094', '1:4127', '1:4654', '1:18884', '1:58091', '1:58504', '1:68331', '1:81296', '1:81361', '1:70083', '1:71816', '1:71329', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A4DE4FE0-3913-EA11-8646-002481CFE864.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CEDC54BD-3201-EA11-9A26-00215A49197E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D6BAC6CC-4F13-EA11-9382-008CFA0516BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2E7CDC91-E709-EA11-82C2-0CC47A4C8F08.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E954D3A-80F7-E911-85E2-AC1F6B0DE490.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7093C3A3-0A08-EA11-836E-AC1F6B0DE2A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE57EA42-FA0A-EA11-A431-0025905A497A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24279122-6000-EA11-AFE5-509A4C9EF8FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CCF160DF-3913-EA11-B4B1-7CD30AD092FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FA4AD288-700D-EA11-9E19-509A4C748095.root']);