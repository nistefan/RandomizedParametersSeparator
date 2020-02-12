import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:3887', '1:3892', '1:8337', '1:9912', '1:21770', '1:4493', '1:12539', '1:12542', '1:14725', '1:18114', '1:23104', '1:8691', '1:9168', '1:10110', '1:10237', '1:16191', '1:26726', '1:32227', '1:37480', '1:27496', '1:27637', '1:23133', '1:13382', '1:13391', '1:10127', '1:10394', '1:26290', '1:26306', '1:26778', '1:35354', '1:33656', '1:32594', '1:34127', '1:34460', '1:34692', '1:36867', '1:94640', '1:57599', '1:59187', '1:57910', '1:57938', '1:58553', '1:58757', '1:58768', '1:59062', '1:59280', '1:92326', '1:92453', '1:95452', '1:86071', '1:37330', '1:37642', '1:50713', '1:60943', '1:61021', '1:61724', '1:57964', '1:58620', '1:58692', '1:58215', '1:58550', '1:58583', '1:57222', '1:77271', '1:56142', '1:56145', '1:56238', '1:56312', '1:56442', '1:56524', '1:56912', '1:57318', '1:56449', '1:89415', '1:16668', '1:16992', '1:28132', '1:28407', '1:29003', '1:29156', '1:29194', '1:29448', '1:52805', '1:17832', '1:18198', '1:99853', '1:17657', '1:21489', '1:18321', '1:18541', '1:58491', '1:22048', '1:22429', '1:22808', '1:22173', '1:22910', '1:26014', '1:26103', '1:22530', '1:23497', '1:24016', '1:35511', '1:25476', '1:25587', '1:37720', '1:37757', '1:37884', '1:10000', '1:17099', '1:25108', '1:17899', '1:19006', '1:18651', '1:18961', '1:35480', '1:35569', '1:24055', '1:27618', '1:27941', '1:27979', '1:54460', '1:62882', '1:52936', '1:52984', '1:56233', '1:53441', '1:25889', '1:25912', '1:26001', '1:26062', '1:26127', '1:26249', '1:37532', '1:25812', '1:25819', '1:25837', '1:25848', '1:25902', '1:26023', '1:34029', '1:34146', '1:32876', '1:36131', '1:74046', '1:25003', '1:25086', '1:25096', '1:5181', '1:5596', '1:7894', '1:7413', '1:7706', '1:7843', '1:7342', '1:7439', '1:7772', '1:8088', '1:55059', '1:51565', '1:14514', '1:16172', '1:16269', '1:36209', '1:36358', '1:36412', '1:36430', '1:36475', '1:36236', '1:36280', '1:38620', '1:37524', '1:39132', '1:38734', '1:37832', '1:39237', '1:73914', '1:74096', '1:74108', '1:77721', '1:43995', '1:44338', '1:48761', '1:11341', '1:11523', '1:46697', '1:39523', '1:52627', '1:41440', '1:41458', '1:42478', '1:42587', '1:42661', '1:42860', '1:75427', '1:72027', '1:75588', '1:77783', '1:1033', '1:1945', '1:1957', '1:3857', '1:4992', '1:1327', '1:4016', '1:5120', '1:20850', '1:20949', '1:20987', '1:21419', '1:67536', '1:67652', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54320079-E317-EA11-B1DF-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA975838-3C18-EA11-8F0A-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/A8A7D5B5-EE17-EA11-8D58-FA163EE3F24C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/76D2EDA7-0918-EA11-9BB4-FA163E20F521.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/768B8E9C-D417-EA11-B213-FA163ECFF9D5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E645838E-2C18-EA11-816C-FA163EE93463.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/060AC0C7-F517-EA11-AD2C-FA163E8B993E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/DE51B3B4-8618-EA11-914B-003048CB8610.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/9830A3F9-341A-EA11-A175-EC0D9A82264E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/5A3E632C-401A-EA11-80A3-6CC2173C4580.root']);