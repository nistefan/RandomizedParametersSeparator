import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:23528', '1:23564', '1:19000', '1:18951', '1:15417', '1:15441', '1:15698', '1:16322', '1:19713', '1:19867', '1:12517', '1:20775', '1:16178', '1:16458', '1:18937', '1:22840', '1:14839', '1:16688', '1:15052', '1:15167', '1:15188', '1:15191', '1:15130', '1:15854', '1:15882', '1:19775', '1:19782', '1:19596', '1:19298', '1:19351', '1:19376', '1:19383', '1:19560', '1:19853', '1:11311', '1:12870', '1:12873', '1:12901', '1:12914', '1:12984', '1:24921', '1:13275', '1:13298', '1:13307', '1:13406', '1:13655', '1:13656', '1:24481', '1:24595', '1:14873', '1:14914', '1:14984', '1:21079', '1:14823', '1:21190', '1:15731', '1:15563', '1:24434', '1:14131', '1:14339', '1:16410', '1:15512', '1:16537', '1:16719', '1:16639', '1:12368', '1:16675', '1:16885', '1:23901', '1:13233', '1:13499', '1:13572', '1:22939', '1:17277', '1:17874', '1:20750', '1:20773', '1:24209', '1:21858', '1:24163', '1:24417', '1:13055', '1:13064', '1:15878', '1:21168', '1:21657', '1:12505', '1:17648', '1:17697', '1:21640', '1:13869', '1:13998', '1:13788', '1:21713', '1:24950', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/E0882A51-5912-EA11-872C-008CFA14FA8C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/9A9349AB-E3F9-E911-978D-8CDCD4A99E60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/388A08FC-5812-EA11-9865-6CC2173BBF00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/185754CB-E6F8-E911-9AEA-0CC47A7E6A74.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/4A488A47-62F8-E911-9547-509A4C9EF93B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/BA348E4D-E9FB-E911-88C9-38EAA78D8AD0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/C03B7D07-11FB-E911-8BEE-A4BF01288315.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/10891AEF-94FA-E911-9D52-0CC47A7E69D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/4C0A70A8-F5FA-E911-93F3-008CFAC94124.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/240000/F662FCA7-C5FB-E911-A302-38EAA78D8AF4.root']);