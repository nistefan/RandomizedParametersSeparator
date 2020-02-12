import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:6625', '1:23236', '1:23248', '1:23312', '1:23335', '1:6575', '1:6824', '1:6100', '1:6267', '1:6394', '1:6418', '1:6447', '1:23622', '1:23636', '1:23226', '1:23007', '1:23049', '1:23059', '1:23070', '1:6897', '1:23238', '1:23267', '1:23955', '1:6953', '1:23120', '1:23448', '1:23383', '1:23095', '1:23106', '1:23597', '1:6277', '1:6970', '1:6615', '1:6985', '1:6988', '1:23176', '1:6020', '1:6054', '1:6078', '1:23322', '1:23318', '1:23323', '1:6143', '1:6568', '1:6823', '1:6853', '1:6225', '1:6227', '1:6243', '1:6393', '1:23036', '1:23151', '1:23163', '1:23204', '1:6027', '1:6038', '1:23343', '1:6244', '1:6435', '1:23755', '1:6452', '1:6462', '1:6714', '1:6837', '1:23975', '1:6362', '1:6639', '1:6926', '1:23481', '1:23715', '1:6427', '1:6448', '1:6207', '1:6301', '1:23445', '1:23617', '1:23865', '1:6748', '1:6756', '1:23100', '1:6344', '1:6513', '1:23407', '1:23422', '1:23571', '1:6636', '1:23218', '1:23292', '1:23701', '1:6231', '1:23648', '1:23759', '1:23761', '1:6206', '1:23920', '1:23987', '1:6548', '1:23879', '1:23916', '1:23924', '1:23896', '1:23905', '1:6284', '1:6501', '1:6505', '1:6097', '1:6131', '1:23250', '1:6319', '1:6915', '1:23124', '1:23182', '1:23109', '1:23116', '1:23403', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/400CB5D1-810F-EA11-A161-6CC2173D5F20.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/FCE3C88D-9010-EA11-A7CD-00259073E40A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/F43393EB-8910-EA11-B587-40F2E9C6AD60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/9ED53426-8A10-EA11-9C66-EC0D9A82237E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/566FCDC3-9310-EA11-BBDF-3417EBE34CAB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/BAB93E73-9C10-EA11-8B08-002590DE6E74.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/C86ACE4C-8810-EA11-97AD-A0369FC5E49C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/564DFE4D-9110-EA11-8029-14DDA924324B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/240E538D-9610-EA11-86F5-FA163E994101.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/D0C0BC6C-6E0E-EA11-9E29-6CC21739DBD0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/2C37C489-9310-EA11-9066-44A842240F8D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/DAE6CB46-B210-EA11-963B-0025905A60DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/C6235FE3-4510-EA11-BC6C-0023AEEEB538.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/D43C62D9-8910-EA11-946B-0025905C3D98.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/88EEA3A6-9C10-EA11-B720-002590D9D8AC.root']);