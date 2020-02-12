import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11208', '1:18107', '1:22854', '1:22254', '1:18277', '1:18381', '1:16223', '1:16405', '1:16578', '1:20835', '1:23097', '1:3519', '1:3521', '1:8286', '1:10063', '1:5616', '1:9801', '1:9895', '1:33900', '1:5362', '1:26500', '1:10436', '1:26531', '1:28873', '1:29930', '1:26995', '1:28109', '1:33262', '1:4007', '1:33935', '1:33995', '1:36951', '1:269', '1:31032', '1:26945', '1:28299', '1:32418', '1:31304', '1:33579', '1:7687', '1:3640', '1:3737', '1:4862', '1:6748', '1:28795', '1:30726', '1:7792', '1:29102', '1:31034', '1:31380', '1:4170', '1:1799', '1:6517', '1:34176', '1:8224', '1:26495', '1:23560', '1:23683', '1:23587', '1:25236', '1:34744', '1:965', '1:4250', '1:6793', '1:4187', '1:32367', '1:31646', '1:8595', '1:1908', '1:31571', '1:29912', '1:33547', '1:2424', '1:29672', '1:871', '1:1430', '1:1939', '1:35057', '1:35237', '1:34584', '1:36913', '1:1512', '1:29659', '1:27706', '1:36924', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/C05C8FB4-7916-EA11-94B4-3CFDFE639780.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8CE3EFE-5C17-EA11-9FAC-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/38055D26-8217-EA11-8707-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2013AFAC-6317-EA11-8CAA-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/FAF900D4-2917-EA11-A923-24BE05C68671.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/94A6ED48-3F18-EA11-A4C4-0CC47AD9908C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/CC0A7D01-3A1B-EA11-A119-0CC47A4DEF48.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/AAE9111D-211C-EA11-8C33-0CC47A5FC495.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/08CA66AF-FB16-EA11-8C68-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/D63E1E93-7217-EA11-A37B-B8CA3A70A410.root']);