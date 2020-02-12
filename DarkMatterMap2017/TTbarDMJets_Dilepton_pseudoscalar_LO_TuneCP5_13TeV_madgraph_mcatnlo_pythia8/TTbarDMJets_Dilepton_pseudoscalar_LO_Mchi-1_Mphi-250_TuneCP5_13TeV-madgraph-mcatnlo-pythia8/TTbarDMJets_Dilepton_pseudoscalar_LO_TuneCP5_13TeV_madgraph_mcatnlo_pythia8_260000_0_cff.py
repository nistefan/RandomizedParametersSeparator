import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:4596', '1:310', '1:9358', '1:18420', '1:18433', '1:23050', '1:23540', '1:31664', '1:7444', '1:26209', '1:2084', '1:455', '1:20828', '1:20085', '1:37431', '1:38632', '1:38693', '1:38849', '1:8605', '1:152', '1:8838', '1:3076', '1:29099', '1:5643', '1:9273', '1:2067', '1:2136', '1:4354', '1:29754', '1:29778', '1:29784', '1:33184', '1:5518', '1:5805', '1:9767', '1:9754', '1:32424', '1:26552', '1:37878', '1:29703', '1:30185', '1:30627', '1:28876', '1:3507', '1:3500', '1:7036', '1:5657', '1:4622', '1:5647', '1:25959', '1:25974', '1:25711', '1:15003', '1:15009', '1:28764', '1:12187', '1:27636', '1:25626', '1:27921', '1:34304', '1:35135', '1:35239', '1:35412', '1:35974', '1:9128', '1:3075', '1:3074', '1:6461', '1:6402', '1:6803', '1:5310', '1:7138', '1:4604', '1:9333', '1:14763', '1:14891', '1:7147', '1:9869', '1:27390', '1:27874', '1:26936', '1:26887', '1:26926', '1:34281', '1:27102', '1:27145', '1:36030', '1:37089', '1:38929', '1:35673', '1:37291', '1:37308', '1:37299', '1:37305', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/023B2C6F-1C1A-EA11-BD6A-B496910A0554.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/848B39AC-B81A-EA11-AAF0-0CC47AFF249E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/EC96E3DC-9E18-EA11-9E23-0025905C42F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/9ADE1793-B116-EA11-A425-1866DA85DC8B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E2704869-2A17-EA11-9700-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2412ABD9-4B17-EA11-BDE5-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/922E001D-4717-EA11-8BA3-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2A6C0B95-6A18-EA11-A67F-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/48D42C93-3917-EA11-AF57-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/88D67FC8-8217-EA11-9DC9-0242AC1C0501.root']);