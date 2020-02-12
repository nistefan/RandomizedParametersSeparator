import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:6213', '1:23244', '1:23276', '1:6417', '1:6608', '1:23199', '1:23461', '1:23067', '1:23971', '1:23107', '1:6917', '1:23173', '1:6583', '1:6586', '1:23149', '1:23614', '1:6025', '1:6051', '1:23297', '1:23352', '1:23470', '1:6120', '1:6871', '1:6880', '1:23973', '1:6269', '1:6008', '1:23169', '1:6007', '1:6042', '1:6179', '1:6465', '1:23735', '1:6178', '1:6222', '1:6405', '1:6434', '1:6480', '1:6491', '1:23917', '1:6234', '1:23855', '1:6081', '1:23085', '1:6526', '1:6641', '1:23557', '1:6860', '1:6936', '1:6065', '1:23451', '1:23505', '1:6474', '1:6654', '1:6306', '1:23848', '1:6107', '1:6337', '1:6736', '1:6746', '1:6749', '1:6980', '1:23412', '1:23958', '1:23976', '1:23277', '1:23473', '1:6233', '1:23536', '1:6767', '1:23756', '1:23891', '1:6832', '1:23644', '1:23934', '1:6200', '1:6324', '1:6330', '1:6348', '1:6349', '1:23237', '1:23282', '1:23960', '1:23963', '1:23969', '1:23156', '1:23559', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/400CB5D1-810F-EA11-A161-6CC2173D5F20.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/FCE3C88D-9010-EA11-A7CD-00259073E40A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/F43393EB-8910-EA11-B587-40F2E9C6AD60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/9ED53426-8A10-EA11-9C66-EC0D9A82237E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/566FCDC3-9310-EA11-BBDF-3417EBE34CAB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/BAB93E73-9C10-EA11-8B08-002590DE6E74.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/C86ACE4C-8810-EA11-97AD-A0369FC5E49C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/564DFE4D-9110-EA11-8029-14DDA924324B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/240E538D-9610-EA11-86F5-FA163E994101.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/D0C0BC6C-6E0E-EA11-9E29-6CC21739DBD0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/2C37C489-9310-EA11-9066-44A842240F8D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/DAE6CB46-B210-EA11-963B-0025905A60DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/C6235FE3-4510-EA11-BC6C-0023AEEEB538.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/D43C62D9-8910-EA11-946B-0025905C3D98.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/88EEA3A6-9C10-EA11-B720-002590D9D8AC.root']);