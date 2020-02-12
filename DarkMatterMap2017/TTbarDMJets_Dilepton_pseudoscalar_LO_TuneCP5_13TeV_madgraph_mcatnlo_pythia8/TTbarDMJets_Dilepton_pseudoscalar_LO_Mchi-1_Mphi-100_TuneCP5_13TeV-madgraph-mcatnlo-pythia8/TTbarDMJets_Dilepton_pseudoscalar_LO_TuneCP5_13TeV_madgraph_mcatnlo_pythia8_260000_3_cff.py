import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2267', '1:5275', '1:4005', '1:4043', '1:2315', '1:5472', '1:5685', '1:1543', '1:2314', '1:33139', '1:33154', '1:2263', '1:5966', '1:31409', '1:2465', '1:2966', '1:2981', '1:2983', '1:1619', '1:3541', '1:1629', '1:31456', '1:31457', '1:33215', '1:1737', '1:1761', '1:4452', '1:4494', '1:2000', '1:5115', '1:11109', '1:19292', '1:17106', '1:20302', '1:20708', '1:9581', '1:9689', '1:28914', '1:30170', '1:32335', '1:28521', '1:29939', '1:31755', '1:15431', '1:15310', '1:28783', '1:29644', '1:32123', '1:30744', '1:30745', '1:25490', '1:30358', '1:25042', '1:35823', '1:31996', '1:7177', '1:28020', '1:28476', '1:31853', '1:29958', '1:30277', '1:30238', '1:30366', '1:5976', '1:29473', '1:25181', '1:25184', '1:25185', '1:2891', '1:3038', '1:7466', '1:7471', '1:31367', '1:27255', '1:30996', '1:25571', '1:25581', '1:311', '1:2075', '1:3970', '1:4879', '1:12670', '1:17914', '1:27012', '1:20242', '1:20487', '1:7995', '1:9635', '1:9985', '1:28052', '1:2051', '1:4855', '1:27290', '1:1516', '1:1863', '1:2447', '1:2180', '1:2189', '1:1541', '1:5763', '1:12372', '1:14383', '1:29985', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E6257D83-1317-EA11-A6EB-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B81B3698-BB1A-EA11-A4F3-1866DAEECFDC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/F687C5F2-B81A-EA11-873E-1866DA85D9A3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/804F1C83-4217-EA11-9F66-5065F38152E1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D439767D-BB1A-EA11-8852-0CC47A13D416.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/9247A6C1-241C-EA11-B393-7845C4FBBD07.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/008C7679-CE19-EA11-8221-3CFDFE6398A0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/EE260969-F618-EA11-BA38-001C23BED6B4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3A933B81-A818-EA11-9C04-0CC47AD98D0E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BE34C404-E419-EA11-A21F-B496910A8AC0.root']);