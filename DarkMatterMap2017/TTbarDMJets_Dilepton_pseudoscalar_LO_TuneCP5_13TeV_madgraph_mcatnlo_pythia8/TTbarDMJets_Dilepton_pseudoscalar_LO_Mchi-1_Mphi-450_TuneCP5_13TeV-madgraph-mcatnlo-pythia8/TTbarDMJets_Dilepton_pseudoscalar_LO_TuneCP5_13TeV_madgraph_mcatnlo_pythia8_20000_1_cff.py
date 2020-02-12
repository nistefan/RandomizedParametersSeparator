import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:31550', '1:34829', '1:34856', '1:26866', '1:26979', '1:28344', '1:28259', '1:28354', '1:28363', '1:28372', '1:29891', '1:31255', '1:31270', '1:31424', '1:26463', '1:26614', '1:29353', '1:33595', '1:33599', '1:33705', '1:30155', '1:30346', '1:25020', '1:25915', '1:30020', '1:29282', '1:25914', '1:30006', '1:1330', '1:1440', '1:1493', '1:1851', '1:33057', '1:33342', '1:33422', '1:1436', '1:2945', '1:2554', '1:29248', '1:28228', '1:26688', '1:26739', '1:26975', '1:34006', '1:34010', '1:34664', '1:34860', '1:34883', '1:35865', '1:35897', '1:35842', '1:35816', '1:7910', '1:7984', '1:7992', '1:25105', '1:33634', '1:10530', '1:10412', '1:10631', '1:3602', '1:1454', '1:8623', '1:1683', '1:6409', '1:26240', '1:32774', '1:3637', '1:3742', '1:3828', '1:5223', '1:5573', '1:5693', '1:26349', '1:26380', '1:26443', '1:28192', '1:31108', '1:10776', '1:10797', '1:32608', '1:507', '1:648', '1:697', '1:2972', '1:2994', '1:5479', '1:5524', '1:4967', '1:8040', '1:8077', '1:8228', '1:5801', '1:29010', '1:32647', '1:32734', '1:30398', '1:30209', '1:364', '1:9608', '1:10955', '1:8935', '1:9173', '1:9579', '1:1118', '1:1132', '1:2798', '1:28989', '1:32402', '1:4164', '1:5042', '1:26969', '1:28645', '1:904', '1:915', '1:8125', '1:8142', '1:4372', '1:4637', '1:4791', '1:4825', '1:4091', '1:4847', '1:6632', '1:34169', '1:35083', '1:35833', '1:10623', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/7E15F380-C80C-EA11-8CFD-FA163E3D586B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/0EC40F59-F00B-EA11-8CC9-FA163E6339E9.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/C6C5E95D-9C0D-EA11-9721-FA163EB8728A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B48F5F02-930D-EA11-8A90-509A4C9F888B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/261BE081-BC0E-EA11-BB60-0CC47A7E6A74.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/16D9952A-C30F-EA11-867C-98039B3B004A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/E847E4A2-B70E-EA11-9510-002590DD7E50.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/80CF3673-C50E-EA11-9F65-0CC47A7E68AA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B616D331-B10E-EA11-8B23-00266CF94C44.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/58865E3A-470F-EA11-99C4-AC1F6BC67D4A.root']);