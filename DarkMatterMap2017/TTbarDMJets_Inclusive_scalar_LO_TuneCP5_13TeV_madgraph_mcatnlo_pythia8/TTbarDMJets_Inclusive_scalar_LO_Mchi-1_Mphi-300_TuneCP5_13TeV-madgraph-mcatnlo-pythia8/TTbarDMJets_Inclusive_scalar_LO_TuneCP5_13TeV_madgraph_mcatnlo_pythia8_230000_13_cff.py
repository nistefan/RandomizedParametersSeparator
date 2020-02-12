import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:78058', '1:78643', '1:78562', '1:91515', '1:75239', '1:79226', '1:35795', '1:53802', '1:37847', '1:37930', '1:39624', '1:39734', '1:62176', '1:62977', '1:40270', '1:58910', '1:54999', '1:61746', '1:54979', '1:55964', '1:55988', '1:64677', '1:67079', '1:64950', '1:67010', '1:64978', '1:64996', '1:68034', '1:67239', '1:67404', '1:67426', '1:69724', '1:75194', '1:75514', '1:75531', '1:75556', '1:14628', '1:16394', '1:16420', '1:18740', '1:7656', '1:16759', '1:18120', '1:6159', '1:10715', '1:16227', '1:19104', '1:27080', '1:34798', '1:97527', '1:94453', '1:70820', '1:70302', '1:70916', '1:80838', '1:88700', '1:91839', '1:91634', '1:102386', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C01DAC7D-3A13-EA11-AAE5-90E2BAD1C9A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44EF9CBA-3913-EA11-94B8-E0071B73B6D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0ADEA135-D803-EA11-953D-B02628342210.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3EA80BAD-9601-EA11-872F-8CDCD4A99E60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE827094-2BFD-E911-A20A-0CC47A2B03A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EA216DD2-5504-EA11-86F9-48D539F38676.root']);