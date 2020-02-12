import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:37724', '1:37649', '1:37703', '1:37716', '1:37705', '1:37813', '1:37842', '1:36062', '1:36653', '1:37040', '1:37400', '1:37408', '1:37310', '1:37343', '1:36821', '1:38560', '1:38152', '1:36266', '1:37526', '1:36405', '1:36598', '1:37134', '1:37139', '1:37175', '1:37230', '1:37214', '1:38259', '1:38698', '1:38832', '1:38713', '1:38714', '1:38751', '1:38756', '1:38846', '1:38748', '1:38910', '1:38913', '1:38887', '1:38888', '1:38000', '1:38333', '1:38367', '1:38322', '1:38625', '1:38679', '1:38075', '1:38077', '1:38174', '1:37275', '1:38016', '1:36028', '1:37216', '1:38764', '1:36528', '1:38599', '1:38740', '1:37809', '1:36921', '1:38253', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/44F3970C-2013-EA11-B446-FA163EBCA6D3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/02411F4C-2013-EA11-A054-8CDCD4A99E60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/402CE14C-2013-EA11-B4FC-AC1F6B0DE0C4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/7899D954-2013-EA11-BDE8-0025901D40A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/A276AE46-2013-EA11-A94A-6C2B59993480.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/6649DC3B-2013-EA11-913E-3CFDFE639860.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/AAA680C2-6713-EA11-A81B-44A842BE76FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/C267E94F-2013-EA11-9D17-0CC47A7C34A0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/50C88150-2013-EA11-A4EA-0242AC1C0504.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/30000/FC9588B2-570D-EA11-8AF2-AC1F6B567680.root']);