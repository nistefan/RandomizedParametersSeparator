import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:23936', '1:34340', '1:26703', '1:26987', '1:29055', '1:36951', '1:38097', '1:37141', '1:87761', '1:4391', '1:3061', '1:3158', '1:4903', '1:10861', '1:26696', '1:33341', '1:24615', '1:50253', '1:61051', '1:57253', '1:9617', '1:8918', '1:10060', '1:31605', '1:32737', '1:32969', '1:96541', '1:88724', '1:90744', '1:94665', '1:172', '1:17725', '1:16054', '1:1225', '1:1248', '1:2216', '1:344', '1:34818', '1:29844', '1:22775', '1:6455', '1:6764', '1:9091', '1:7100', '1:17018', '1:17059', '1:49664', '1:96801', '1:85079', '1:80488', '1:39256', '1:58095', '1:60608', '1:51607', '1:57971', '1:60187', '1:60391', '1:39247', '1:30684', '1:69002', '1:23505', '1:30287', '1:31532', '1:63722', '1:72148', '1:79236', '1:55978', '1:61235', '1:54873', '1:71008', '1:79752', '1:73122', '1:73172', '1:81612', '1:96118', '1:71638', '1:72079', '1:99093', '1:99550', '1:99624', '1:100308', '1:75758', '1:76979', '1:80235', '1:90733', '1:90430', '1:90554', '1:94856', '1:2927', '1:3205', '1:355', '1:2333', '1:2790', '1:2866', '1:3242', '1:1323', '1:1359', '1:2600', '1:263', '1:5189', '1:31141', '1:23430', '1:51473', '1:24338', '1:8966', '1:9322', '1:3819', '1:5031', '1:4014', '1:93', '1:397', '1:702', '1:1005', '1:1084', '1:1288', '1:1766', '1:3106', '1:3141', '1:2073', '1:2105', '1:2183', '1:3495', '1:5367', '1:3657', '1:4143', '1:17100', '1:25481', '1:25818', '1:25867', '1:26396', '1:37018', '1:17436', '1:19479', '1:19462', '1:19501', '1:1918', '1:1950', '1:5203', '1:5586', '1:5590', '1:38020', '1:76394', '1:50596', '1:52015', '1:75893', '1:76053', '1:97374', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A29568F-0204-EA11-8E9E-20CF3027A6B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9A57B881-3F03-EA11-8CAB-D48564594FB4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FA29DAC3-4304-EA11-8CA5-F01FAFD6996C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2CFB0664-3407-EA11-BC37-A0369FD0B3E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCBAF234-0107-EA11-95FC-0CC47A4DEDD6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C5438B6-1B08-EA11-B2E6-90B11CBCFFA9.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/60A4990B-DB07-EA11-BFBE-44A842CFD5B1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0682B29D-DD08-EA11-AE0F-AC1F6BAC7ACC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/520DFFB1-110B-EA11-88A1-0CC47A7C353E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C157FD6-120B-EA11-8BA5-0025905A60C6.root']);