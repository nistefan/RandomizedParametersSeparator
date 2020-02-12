import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:4494', '1:1081', '1:4052', '1:3608', '1:50798', '1:52761', '1:31165', '1:62027', '1:55669', '1:67906', '1:78171', '1:99444', '1:101433', '1:100161', '1:38897', '1:49876', '1:54532', '1:54557', '1:54620', '1:62320', '1:62331', '1:62823', '1:62865', '1:74586', '1:74600', '1:74690', '1:87409', '1:87503', '1:88025', '1:90579', '1:90614', '1:89823', '1:94085', '1:267', '1:3700', '1:3741', '1:19112', '1:39013', '1:39986', '1:50396', '1:54547', '1:54731', '1:61106', '1:61749', '1:62685', '1:67373', '1:86570', '1:91152', '1:95004', '1:95041', '1:101959', '1:14983', '1:34513', '1:33457', '1:34716', '1:34263', '1:35389', '1:27784', '1:27857', '1:30132', '1:80758', '1:60408', '1:60482', '1:79078', '1:85034', '1:85869', '1:79637', '1:68114', '1:69039', '1:60184', '1:60578', '1:60838', '1:87121', '1:86706', '1:86711', '1:87046', '1:87102', '1:87186', '1:79064', '1:97397', '1:98501', '1:98561', '1:98754', '1:98777', '1:99016', '1:100006', '1:100229', '1:98512', '1:98821', '1:100503', '1:2943', '1:3854', '1:4299', '1:4659', '1:7735', '1:8076', '1:17230', '1:38219', '1:10163', '1:15098', '1:19341', '1:33454', '1:33937', '1:33940', '1:63353', '1:63603', '1:63786', '1:86051', '1:3470', '1:5326', '1:21198', '1:17206', '1:17040', '1:19320', '1:29696', '1:22496', '1:75829', '1:22131', '1:26487', '1:75825', '1:74022', '1:71691', '1:77432', '1:77515', '1:86915', '1:96130', '1:85058', '1:85352', '1:90888', '1:96744', '1:89180', '1:90828', '1:98439', '1:97219', '1:90517', '1:87487', '1:27177', '1:31876', '1:28807', '1:3712', '1:13358', '1:35039', '1:24247', '1:46109', '1:90764', '1:51836', '1:52197', '1:52262', '1:52408', '1:52831', '1:60718', '1:60919', '1:60383', '1:60561', '1:61250', '1:62827', '1:64037', '1:68734', '1:68840', '1:55489', '1:69986', '1:73048', '1:73980', '1:75876', '1:73575', '1:73687', '1:78270', '1:4322', '1:4375', '1:5684', '1:19611', '1:15584', '1:17128', '1:22581', '1:18734', '1:55079', '1:78115', '1:3419', '1:4474', '1:4482', '1:2432', '1:58715', '1:30190', '1:40289', '1:31743', '1:49108', '1:70107', '1:77760', '1:77769', '1:72969', '1:81046', '1:86909', '1:80605', '1:85320', '1:87019', '1:75763', '1:78707', '1:6795', '1:7270', '1:14082', '1:14824', '1:16025', '1:19543', '1:18219', '1:20123', '1:20963', '1:95209', '1:95893', '1:96444', '1:97692', '1:86688', '1:81440', '1:81493', '1:85663', '1:70572', '1:72178', '1:73825', '1:77310', '1:79045', '1:80028', '1:100887', '1:88632', '1:90743', '1:101746', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2C0E7C34-2900-EA11-B381-0242AC1C0507.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1680776D-2A00-EA11-9D4C-0CC47AF9739E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7E4F3988-2C03-EA11-81C0-F04DA274BCCE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50DF8EAD-BF01-EA11-BF59-509A4C9F8A64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A43FC48E-E902-EA11-B9A7-0CC47AFF0610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/825E2C46-8810-EA11-9BC6-0242AC1C0506.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DAFBB154-B608-EA11-91B7-44A8423524BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50814A83-CCF8-E911-8AD8-008CFAC93FB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5807D4F7-A407-EA11-9B1B-0CC47A4D765A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/940D11F2-040B-EA11-BD0B-0CC47A4D76B2.root']);