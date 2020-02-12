import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:80873', '1:77818', '1:85411', '1:90136', '1:97858', '1:93405', '1:73365', '1:80730', '1:85223', '1:93875', '1:75639', '1:76295', '1:78374', '1:79938', '1:80190', '1:81933', '1:91948', '1:26456', '1:26810', '1:31026', '1:31036', '1:44006', '1:42851', '1:44320', '1:73508', '1:74248', '1:74288', '1:40432', '1:40561', '1:40722', '1:41150', '1:41377', '1:42410', '1:44221', '1:42744', '1:42752', '1:89998', '1:73676', '1:102551', '1:102790', '1:80401', '1:74552', '1:79006', '1:104315', '1:94109', '1:96504', '1:97052', '1:101040', '1:104728', '1:52307', '1:52593', '1:52614', '1:52803', '1:52816', '1:104509', '1:104609', '1:104640', '1:104713', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4D2AD02-D40A-EA11-A0B7-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E48D6400-92FB-E911-A2F9-0CC47A7FC6D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F89F393C-D012-EA11-B06C-44A842BE76FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/56BCA64F-BC12-EA11-86AC-002590D425C0.root']);