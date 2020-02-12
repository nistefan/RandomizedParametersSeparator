import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8577', '1:3240', '1:7944', '1:280', '1:3403', '1:26116', '1:33811', '1:33797', '1:3633', '1:29244', '1:2883', '1:7180', '1:29528', '1:26589', '1:9955', '1:26013', '1:3926', '1:7229', '1:7926', '1:29419', '1:6464', '1:9032', '1:28679', '1:26105', '1:28456', '1:5536', '1:30222', '1:27376', '1:34276', '1:25841', '1:34275', '1:34369', '1:31242', '1:31229', '1:31311', '1:9192', '1:8621', '1:9509', '1:28673', '1:7930', '1:9651', '1:31907', '1:26021', '1:3379', '1:3380', '1:3588', '1:3390', '1:2147', '1:33774', '1:31889', '1:31897', '1:4266', '1:10986', '1:26844', '1:26833', '1:26816', '1:32360', '1:6535', '1:10001', '1:4269', '1:4274', '1:28025', '1:26570', '1:26316', '1:27081', '1:35941', '1:25886', '1:34497', '1:34458', '1:2463', '1:2939', '1:3207', '1:6258', '1:6333', '1:6902', '1:31389', '1:31390', '1:26159', '1:30215', '1:1977', '1:1986', '1:4790', '1:2772', '1:5431', '1:5893', '1:7559', '1:25859', '1:31721', '1:26680', '1:30127', '1:30148', '1:30274', '1:30396', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/1A72AD25-0811-EA11-8744-002590FD5E70.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/2E6C9CF8-CD0C-EA11-A22C-FA163EE977F5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/4439EC7A-6F10-EA11-AD4B-00269E95B0A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/74EEC12D-3D11-EA11-949E-0025904B0468.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/F863856F-8F0B-EA11-94A7-E0071B7AF550.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/ECA5C43E-3710-EA11-851D-0CC47AFEFDEC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B273DBAE-9D0C-EA11-8DBE-FA163EA53B10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/6ECE9B2C-4A0B-EA11-A9AF-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/480CFFFA-4AF8-E911-864C-509A4C9F8A8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/04750700-4D05-EA11-897F-0CC47AFB7DDC.root']);