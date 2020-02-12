import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:36178', '1:36179', '1:37519', '1:37603', '1:37128', '1:36839', '1:37385', '1:37795', '1:38989', '1:38397', '1:36801', '1:38979', '1:38120', '1:36492', '1:36317', '1:36306', '1:36998', '1:36980', '1:36983', '1:37497', '1:37850', '1:37978', '1:38225', '1:37761', '1:38272', '1:38787', '1:38326', '1:37455', '1:37907', '1:37919', '1:37926', '1:36065', '1:36519', '1:36658', '1:38535', '1:38536', '1:38602', '1:36677', '1:36865', '1:38497', '1:36402', '1:37621', '1:37036', '1:38641', '1:36421', '1:38574', '1:37439', '1:37461', '1:37585', '1:36591', '1:36979', '1:38478', '1:36152', '1:36158', '1:38544', '1:38851', '1:38745', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/D0F8A41C-990E-EA11-A50D-AC1F6B1E3074.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/DCD9D649-2013-EA11-BBCA-98039B3B0032.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/88D5C4F6-9D0C-EA11-A344-24BE05C63681.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/14F851FE-6510-EA11-B76F-008CFAF74B22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/2AC7749D-2013-EA11-AAAA-001E67792738.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/8228DED2-F60C-EA11-9D11-002590FD5A78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/B4730441-2013-EA11-8532-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/98375E4E-2013-EA11-BDE2-7CD30AD095BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/86D1A249-EF0D-EA11-BAF6-008CFAE45108.root']);