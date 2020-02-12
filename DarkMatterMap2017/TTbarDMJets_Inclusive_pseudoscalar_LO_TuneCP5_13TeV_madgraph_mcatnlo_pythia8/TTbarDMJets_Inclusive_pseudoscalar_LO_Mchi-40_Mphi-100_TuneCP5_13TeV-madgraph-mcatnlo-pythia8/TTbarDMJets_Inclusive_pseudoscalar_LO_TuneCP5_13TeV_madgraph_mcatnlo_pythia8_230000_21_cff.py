import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:70854', '1:82471', '1:82554', '1:85517', '1:90994', '1:81505', '1:97553', '1:97816', '1:97948', '1:98062', '1:98103', '1:98483', '1:67571', '1:72279', '1:70215', '1:95276', '1:79773', '1:26594', '1:26760', '1:44364', '1:44312', '1:44357', '1:73645', '1:74522', '1:39925', '1:40592', '1:40983', '1:41428', '1:44106', '1:90194', '1:74110', '1:74239', '1:102302', '1:102389', '1:102512', '1:102937', '1:73488', '1:79444', '1:81091', '1:75793', '1:88819', '1:91837', '1:82761', '1:84276', '1:52213', '1:52323', '1:52671', '1:52745', '1:52806', '1:104493', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4D2AD02-D40A-EA11-A0B7-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E48D6400-92FB-E911-A2F9-0CC47A7FC6D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F89F393C-D012-EA11-B06C-44A842BE76FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/56BCA64F-BC12-EA11-86AC-002590D425C0.root']);