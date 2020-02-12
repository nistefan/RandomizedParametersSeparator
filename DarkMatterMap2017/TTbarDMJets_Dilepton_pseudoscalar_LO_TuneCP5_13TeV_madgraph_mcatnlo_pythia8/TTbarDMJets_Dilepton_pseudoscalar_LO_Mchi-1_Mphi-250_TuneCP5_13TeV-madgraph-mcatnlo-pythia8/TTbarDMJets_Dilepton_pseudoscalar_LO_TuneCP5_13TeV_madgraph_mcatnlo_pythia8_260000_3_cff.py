import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:4034', '1:33554', '1:31410', '1:31452', '1:4607', '1:5178', '1:5214', '1:5484', '1:11093', '1:11561', '1:16763', '1:17081', '1:17130', '1:20317', '1:20299', '1:20539', '1:23993', '1:9653', '1:9663', '1:33296', '1:28908', '1:32988', '1:26876', '1:28444', '1:28566', '1:29828', '1:15100', '1:19660', '1:15248', '1:16028', '1:25989', '1:30735', '1:30734', '1:32554', '1:25050', '1:35819', '1:2409', '1:2771', '1:9574', '1:33834', '1:7938', '1:27639', '1:27439', '1:27448', '1:27461', '1:1370', '1:17490', '1:20285', '1:6659', '1:3601', '1:4461', '1:28397', '1:28419', '1:28730', '1:20732', '1:27647', '1:27294', '1:1509', '1:1906', '1:1963', '1:12382', '1:14355', '1:14509', '1:29956', '1:29961', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E6257D83-1317-EA11-A6EB-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/B81B3698-BB1A-EA11-A4F3-1866DAEECFDC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/F687C5F2-B81A-EA11-873E-1866DA85D9A3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/804F1C83-4217-EA11-9F66-5065F38152E1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D439767D-BB1A-EA11-8852-0CC47A13D416.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/9247A6C1-241C-EA11-B393-7845C4FBBD07.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/008C7679-CE19-EA11-8221-3CFDFE6398A0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/EE260969-F618-EA11-BA38-001C23BED6B4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3A933B81-A818-EA11-9C04-0CC47AD98D0E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BE34C404-E419-EA11-A21F-B496910A8AC0.root']);