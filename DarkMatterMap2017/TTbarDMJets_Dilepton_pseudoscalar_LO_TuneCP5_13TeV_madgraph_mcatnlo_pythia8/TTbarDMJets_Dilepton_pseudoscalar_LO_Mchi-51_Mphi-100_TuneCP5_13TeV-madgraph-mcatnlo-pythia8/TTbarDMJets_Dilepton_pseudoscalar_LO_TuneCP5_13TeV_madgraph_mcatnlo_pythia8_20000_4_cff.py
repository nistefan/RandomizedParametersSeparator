import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:9097', '1:9201', '1:29516', '1:29186', '1:1116', '1:31860', '1:1375', '1:7450', '1:3951', '1:29684', '1:3793', '1:3831', '1:5437', '1:5535', '1:5916', '1:8981', '1:29078', '1:30021', '1:30088', '1:34408', '1:30345', '1:31158', '1:31333', '1:31314', '1:31642', '1:8604', '1:8520', '1:9066', '1:10970', '1:26082', '1:47', '1:330', '1:332', '1:151', '1:304', '1:9091', '1:4278', '1:3384', '1:29401', '1:9661', '1:9691', '1:26830', '1:28401', '1:28530', '1:32301', '1:6365', '1:9986', '1:4429', '1:30200', '1:27944', '1:28792', '1:28879', '1:30809', '1:31778', '1:29947', '1:34503', '1:34379', '1:34396', '1:34415', '1:34417', '1:35799', '1:3029', '1:10590', '1:10605', '1:10670', '1:9924', '1:6496', '1:6596', '1:6600', '1:8087', '1:31141', '1:31251', '1:31392', '1:31641', '1:880', '1:2341', '1:1826', '1:26430', '1:2354', '1:2470', '1:2580', '1:2763', '1:3659', '1:5084', '1:7813', '1:7528', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/1A72AD25-0811-EA11-8744-002590FD5E70.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/2E6C9CF8-CD0C-EA11-A22C-FA163EE977F5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/4439EC7A-6F10-EA11-AD4B-00269E95B0A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/74EEC12D-3D11-EA11-949E-0025904B0468.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/F863856F-8F0B-EA11-94A7-E0071B7AF550.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/ECA5C43E-3710-EA11-851D-0CC47AFEFDEC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B273DBAE-9D0C-EA11-8DBE-FA163EA53B10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/6ECE9B2C-4A0B-EA11-A9AF-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/480CFFFA-4AF8-E911-864C-509A4C9F8A8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/04750700-4D05-EA11-897F-0CC47AFB7DDC.root']);