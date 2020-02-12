import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:2686', '1:3307', '1:5793', '1:7703', '1:19185', '1:30133', '1:35542', '1:46650', '1:27140', '1:37966', '1:73805', '1:69496', '1:97162', '1:101699', '1:102360', '1:54598', '1:54617', '1:54666', '1:62424', '1:62380', '1:62847', '1:62341', '1:62853', '1:70001', '1:70585', '1:70981', '1:70983', '1:71100', '1:74626', '1:74641', '1:85840', '1:91109', '1:88016', '1:90040', '1:90442', '1:90605', '1:222', '1:8091', '1:15044', '1:54864', '1:69022', '1:76361', '1:97336', '1:18234', '1:22134', '1:28977', '1:34805', '1:34584', '1:31965', '1:32348', '1:57568', '1:31071', '1:73903', '1:73918', '1:37112', '1:56378', '1:27793', '1:79677', '1:85447', '1:85601', '1:68632', '1:86619', '1:85682', '1:102408', '1:55679', '1:55833', '1:68024', '1:68073', '1:68161', '1:60201', '1:60533', '1:60160', '1:79130', '1:79246', '1:70295', '1:70444', '1:70581', '1:98598', '1:98697', '1:98729', '1:98770', '1:98800', '1:98954', '1:99044', '1:4265', '1:381', '1:8239', '1:19663', '1:20611', '1:19754', '1:21486', '1:36720', '1:18231', '1:63758', '1:5110', '1:15158', '1:17401', '1:19966', '1:13042', '1:36404', '1:26135', '1:89099', '1:21730', '1:55189', '1:67645', '1:75144', '1:75987', '1:76447', '1:62687', '1:76118', '1:71284', '1:80326', '1:81454', '1:81938', '1:85030', '1:99715', '1:99263', '1:90881', '1:99622', '1:99680', '1:90654', '1:97386', '1:100010', '1:310', '1:4825', '1:19081', '1:34055', '1:34356', '1:35949', '1:30492', '1:37253', '1:64519', '1:19086', '1:37235', '1:51227', '1:53040', '1:35781', '1:58144', '1:57306', '1:55324', '1:67539', '1:69414', '1:74341', '1:74461', '1:75469', '1:78489', '1:75673', '1:5520', '1:4898', '1:5139', '1:5264', '1:5349', '1:16118', '1:21181', '1:21359', '1:21609', '1:21222', '1:21618', '1:14455', '1:14932', '1:15133', '1:15540', '1:74928', '1:75297', '1:78316', '1:1401', '1:1985', '1:2436', '1:23853', '1:27315', '1:30392', '1:30644', '1:31206', '1:34405', '1:39846', '1:85301', '1:70072', '1:71074', '1:78994', '1:81574', '1:86331', '1:85043', '1:75596', '1:76127', '1:78389', '1:101689', '1:74730', '1:13092', '1:20461', '1:20819', '1:25520', '1:29752', '1:38981', '1:100902', '1:101972', '1:102211', '1:102250', '1:97684', '1:100364', '1:85048', '1:80948', '1:81149', '1:81065', '1:94110', '1:94180', '1:94788', '1:102263', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2C0E7C34-2900-EA11-B381-0242AC1C0507.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1680776D-2A00-EA11-9D4C-0CC47AF9739E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7E4F3988-2C03-EA11-81C0-F04DA274BCCE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50DF8EAD-BF01-EA11-BF59-509A4C9F8A64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A43FC48E-E902-EA11-B9A7-0CC47AFF0610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/825E2C46-8810-EA11-9BC6-0242AC1C0506.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DAFBB154-B608-EA11-91B7-44A8423524BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50814A83-CCF8-E911-8AD8-008CFAC93FB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5807D4F7-A407-EA11-9B1B-0CC47A4D765A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/940D11F2-040B-EA11-BD0B-0CC47A4D76B2.root']);