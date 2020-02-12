import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:23022', '1:18161', '1:18755', '1:15312', '1:16282', '1:19603', '1:19733', '1:19854', '1:23630', '1:15656', '1:16179', '1:16325', '1:16203', '1:14865', '1:16378', '1:16692', '1:16533', '1:15093', '1:15168', '1:15244', '1:15975', '1:15734', '1:15741', '1:19673', '1:19719', '1:19522', '1:19692', '1:19725', '1:19822', '1:19977', '1:19986', '1:19569', '1:19573', '1:12879', '1:24737', '1:24864', '1:24900', '1:13291', '1:13303', '1:13712', '1:14821', '1:14900', '1:21024', '1:24860', '1:15465', '1:15491', '1:15530', '1:24308', '1:24649', '1:24682', '1:14319', '1:14331', '1:14345', '1:16418', '1:16631', '1:15497', '1:16755', '1:16880', '1:18683', '1:22502', '1:22597', '1:22717', '1:22765', '1:14117', '1:20414', '1:20435', '1:20579', '1:20064', '1:20725', '1:20126', '1:13044', '1:13051', '1:22680', '1:17349', '1:17214', '1:23530', '1:21843', '1:24148', '1:23229', '1:24055', '1:11868', '1:13034', '1:13002', '1:13137', '1:14415', '1:14298', '1:14600', '1:14730', '1:14747', '1:14724', '1:21822', '1:21830', '1:21688', '1:12299', '1:13765', '1:13861', '1:21217', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/E0882A51-5912-EA11-872C-008CFA14FA8C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/9A9349AB-E3F9-E911-978D-8CDCD4A99E60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/388A08FC-5812-EA11-9865-6CC2173BBF00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/185754CB-E6F8-E911-9AEA-0CC47A7E6A74.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/4A488A47-62F8-E911-9547-509A4C9EF93B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BA348E4D-E9FB-E911-88C9-38EAA78D8AD0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C03B7D07-11FB-E911-8BEE-A4BF01288315.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/10891AEF-94FA-E911-9D52-0CC47A7E69D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/4C0A70A8-F5FA-E911-93F3-008CFAC94124.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/F662FCA7-C5FB-E911-A302-38EAA78D8AF4.root']);