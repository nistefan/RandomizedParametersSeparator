import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:15313', '1:15322', '1:15427', '1:18130', '1:18241', '1:11539', '1:11548', '1:13993', '1:13928', '1:14089', '1:14160', '1:16375', '1:16431', '1:23739', '1:23877', '1:23939', '1:20181', '1:21432', '1:19157', '1:19189', '1:17760', '1:22409', '1:22878', '1:24165', '1:24239', '1:24326', '1:11438', '1:11632', '1:11759', '1:11804', '1:11673', '1:11904', '1:13068', '1:13488', '1:17952', '1:17600', '1:18701', '1:15031', '1:13124', '1:13220', '1:13615', '1:15548', '1:21117', '1:21627', '1:14518', '1:15094', '1:15540', '1:15773', '1:15379', '1:16660', '1:21133', '1:23006', '1:12600', '1:18086', '1:15516', '1:19467', '1:16638', '1:20346', '1:20390', '1:21914', '1:21947', '1:21107', '1:15260', '1:15264', '1:16159', '1:16610', '1:20526', '1:20908', '1:21564', '1:24291', '1:24249', '1:24777', '1:11200', '1:11591', '1:18377', '1:18484', '1:23825', '1:23964', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/3A832396-BC0D-EA11-B1AC-AC1F6B0DE348.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/02308EE7-F002-EA11-880C-20040FF49604.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/CCA9164E-5912-EA11-8E3A-008CFAFC4340.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/DC613EB9-5812-EA11-B169-0242AC130003.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/7E24AE60-BA02-EA11-B31A-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C02D6A28-D603-EA11-B438-246E96D14E34.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/5641A5DC-0A04-EA11-8D58-0CC47AFF01F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/34D2182A-0903-EA11-9CD9-A0369FE2C142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/5854FF44-98FE-E911-BBAE-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BE98A30F-72FC-E911-97EC-008CFAC91A1C.root']);