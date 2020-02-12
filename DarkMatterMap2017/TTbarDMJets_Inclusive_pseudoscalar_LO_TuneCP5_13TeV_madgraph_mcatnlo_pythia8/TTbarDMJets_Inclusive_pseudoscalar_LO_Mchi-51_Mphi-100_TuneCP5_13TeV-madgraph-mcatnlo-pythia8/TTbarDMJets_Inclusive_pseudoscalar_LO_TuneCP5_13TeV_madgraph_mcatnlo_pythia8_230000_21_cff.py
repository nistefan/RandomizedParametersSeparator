import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:65565', '1:82322', '1:85889', '1:79767', '1:84136', '1:82237', '1:84076', '1:98207', '1:73940', '1:75368', '1:97894', '1:80863', '1:67274', '1:70566', '1:70747', '1:70074', '1:78640', '1:79575', '1:74677', '1:79930', '1:80246', '1:26071', '1:26371', '1:26437', '1:42854', '1:42992', '1:42841', '1:44126', '1:44206', '1:104491', '1:40640', '1:40641', '1:42379', '1:42396', '1:42869', '1:42845', '1:42866', '1:42923', '1:44238', '1:89925', '1:89938', '1:90128', '1:92829', '1:73725', '1:74458', '1:102388', '1:102562', '1:84476', '1:89446', '1:70555', '1:101765', '1:85648', '1:98317', '1:97377', '1:101897', '1:104227', '1:89723', '1:52073', '1:52348', '1:52408', '1:52509', '1:52517', '1:102983', '1:104479', '1:104724', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4D2AD02-D40A-EA11-A0B7-0025905B8582.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E48D6400-92FB-E911-A2F9-0CC47A7FC6D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F89F393C-D012-EA11-B06C-44A842BE76FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/56BCA64F-BC12-EA11-86AC-002590D425C0.root']);