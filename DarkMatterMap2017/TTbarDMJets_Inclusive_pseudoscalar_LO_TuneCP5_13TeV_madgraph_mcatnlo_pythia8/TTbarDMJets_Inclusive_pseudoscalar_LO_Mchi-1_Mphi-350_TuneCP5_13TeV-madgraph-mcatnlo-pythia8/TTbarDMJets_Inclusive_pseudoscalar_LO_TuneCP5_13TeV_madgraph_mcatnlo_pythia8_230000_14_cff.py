import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:80505', '1:90610', '1:91382', '1:101363', '1:98792', '1:94332', '1:101046', '1:101242', '1:102326', '1:101186', '1:101520', '1:2422', '1:9744', '1:11653', '1:10045', '1:31546', '1:18091', '1:25919', '1:14270', '1:14135', '1:14131', '1:14536', '1:51896', '1:52033', '1:21022', '1:15786', '1:17718', '1:19545', '1:44302', '1:41134', '1:58796', '1:25174', '1:25375', '1:25415', '1:42325', '1:42347', '1:42594', '1:42769', '1:42802', '1:42918', '1:44036', '1:44074', '1:44564', '1:57218', '1:72795', '1:78083', '1:82795', '1:83056', '1:87679', '1:88358', '1:86476', '1:86883', '1:86942', '1:87009', '1:89114', '1:90555', '1:90826', '1:91112', '1:91438', '1:96256', '1:91126', '1:94905', '1:87368', '1:88192', '1:104355', '1:101282', '1:101914', '1:105000', '1:1758', '1:1829', '1:4256', '1:53511', '1:59209', '1:59323', '1:7887', '1:8753', '1:8835', '1:8880', '1:9371', '1:9891', '1:41337', '1:41349', '1:32676', '1:49675', '1:8638', '1:8857', '1:9181', '1:27083', '1:27421', '1:59777', '1:2838', '1:19943', '1:32521', '1:70669', '1:39812', '1:40723', '1:41182', '1:30204', '1:39323', '1:62834', '1:53771', '1:57454', '1:62244', '1:44855', '1:44944', '1:44871', '1:44983', '1:42579', '1:52250', '1:62283', '1:66056', '1:81574', '1:70511', '1:70617', '1:71234', '1:77154', '1:106219', '1:24683', '1:24886', '1:24953', '1:70486', '1:84449', '1:70184', '1:70605', '1:84421', '1:84687', '1:88688', '1:96289', '1:97248', '1:85311', '1:82232', '1:82498', '1:6014', '1:40622', '1:40736', '1:52525', '1:52538', '1:22593', '1:22558', '1:22560', '1:22657', '1:27366', '1:82612', '1:82637', '1:82858', '1:83143', '1:83662', '1:83678', '1:83727', '1:43730', '1:46144', '1:58361', '1:40863', '1:90753', '1:93995', '1:43325', '1:43794', '1:43977', '1:44047', '1:47670', '1:47675', '1:47987', '1:13434', '1:24353', '1:87394', '1:106343', '1:106276', '1:106353', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6A721CBE-4B07-EA11-9750-0CC47A4D7646.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCF6B8AB-E003-EA11-AAE8-44A842BE8F7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9EAE1061-30F8-E911-B2D5-AC1F6B0F676C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/86727FE6-AF0A-EA11-B38D-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2A16734-8607-EA11-A7C2-0025905A6060.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/723E26E0-88FC-E911-A84F-0CC47AFCC666.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/643155F4-E80A-EA11-BD55-0CC47A7C3636.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC1243A5-AA0A-EA11-A2C9-0CC47A7C347A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24362999-4EFE-E911-BFEB-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1207CE62-4EF9-E911-85E0-C4346BC85718.root']);