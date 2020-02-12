import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:67', '1:320', '1:334', '1:7428', '1:26118', '1:26049', '1:9676', '1:29388', '1:29414', '1:26847', '1:28064', '1:33757', '1:9540', '1:9642', '1:2138', '1:6971', '1:28342', '1:3829', '1:5418', '1:5464', '1:29324', '1:7873', '1:26521', '1:30018', '1:34361', '1:34409', '1:31116', '1:31341', '1:9050', '1:9190', '1:8438', '1:28573', '1:28596', '1:26110', '1:325', '1:2068', '1:2131', '1:3889', '1:3995', '1:6533', '1:3382', '1:31317', '1:10692', '1:7971', '1:29411', '1:28713', '1:3412', '1:4428', '1:6361', '1:33148', '1:28798', '1:25684', '1:29989', '1:34465', '1:35829', '1:35959', '1:9389', '1:6597', '1:6961', '1:10768', '1:10789', '1:31171', '1:31260', '1:2781', '1:3295', '1:2774', '1:5291', '1:5884', '1:7567', '1:25864', '1:31709', '1:31712', '1:33891', '1:33645', '1:26721', '1:26691', '1:30206', '1:30253', '1:30925', '1:7551', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/1A72AD25-0811-EA11-8744-002590FD5E70.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/2E6C9CF8-CD0C-EA11-A22C-FA163EE977F5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/4439EC7A-6F10-EA11-AD4B-00269E95B0A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/74EEC12D-3D11-EA11-949E-0025904B0468.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/F863856F-8F0B-EA11-94A7-E0071B7AF550.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/ECA5C43E-3710-EA11-851D-0CC47AFEFDEC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B273DBAE-9D0C-EA11-8DBE-FA163EA53B10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/6ECE9B2C-4A0B-EA11-A9AF-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/480CFFFA-4AF8-E911-864C-509A4C9F8A8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/04750700-4D05-EA11-897F-0CC47AFB7DDC.root']);