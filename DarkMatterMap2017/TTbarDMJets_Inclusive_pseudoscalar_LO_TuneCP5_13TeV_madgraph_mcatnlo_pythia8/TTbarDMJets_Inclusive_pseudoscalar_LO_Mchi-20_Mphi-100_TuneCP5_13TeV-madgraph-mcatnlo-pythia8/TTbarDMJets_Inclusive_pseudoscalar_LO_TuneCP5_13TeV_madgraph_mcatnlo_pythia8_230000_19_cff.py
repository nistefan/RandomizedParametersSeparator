import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1175', '1:1226', '1:2135', '1:1668', '1:2689', '1:3471', '1:12677', '1:6328', '1:6882', '1:7047', '1:7094', '1:7709', '1:9444', '1:9465', '1:9522', '1:9644', '1:11829', '1:11980', '1:23250', '1:24140', '1:24941', '1:25524', '1:25781', '1:26397', '1:26398', '1:25811', '1:26037', '1:26884', '1:2173', '1:23224', '1:48324', '1:40961', '1:44525', '1:91698', '1:92845', '1:20857', '1:6084', '1:8850', '1:14051', '1:14707', '1:25162', '1:31680', '1:17171', '1:19192', '1:24092', '1:19649', '1:29934', '1:25745', '1:46060', '1:46201', '1:93688', '1:94652', '1:95308', '1:29147', '1:29301', '1:29342', '1:29374', '1:71935', '1:72485', '1:88212', '1:92388', '1:92532', '1:93993', '1:94526', '1:1896', '1:12916', '1:13389', '1:30912', '1:32016', '1:32055', '1:39095', '1:31590', '1:31659', '1:31734', '1:31778', '1:31916', '1:31926', '1:31927', '1:31952', '1:92916', '1:93168', '1:94011', '1:93714', '1:6425', '1:6947', '1:12530', '1:65772', '1:39666', '1:39788', '1:42360', '1:40284', '1:41778', '1:41908', '1:41950', '1:43767', '1:87399', '1:88231', '1:88488', '1:88667', '1:72934', '1:75726', '1:76182', '1:87850', '1:91027', '1:87854', '1:85339', '1:85199', '1:85454', '1:92564', '1:92986', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4AE2EE50-65FC-E911-B233-0CC47AFCC62A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/262322CD-2EF8-E911-8414-0CC47A2B04B6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E83181B8-B4FC-E911-8386-6CC2173D6B10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4881F73B-93FC-E911-ABAF-3417EBE70663.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/389B13D9-FA08-EA11-BC98-0025905A6064.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A96DA38-CBFA-E911-B1D9-28924A33B8AE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70F9F439-56F3-E911-9AA8-F4E9D4DF1780.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E64248C-BC12-EA11-9804-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8C2EB6F-BD12-EA11-A3F9-A0369F7FC544.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C484CA9C-D4F3-E911-A566-8CDCD4A99D14.root']);