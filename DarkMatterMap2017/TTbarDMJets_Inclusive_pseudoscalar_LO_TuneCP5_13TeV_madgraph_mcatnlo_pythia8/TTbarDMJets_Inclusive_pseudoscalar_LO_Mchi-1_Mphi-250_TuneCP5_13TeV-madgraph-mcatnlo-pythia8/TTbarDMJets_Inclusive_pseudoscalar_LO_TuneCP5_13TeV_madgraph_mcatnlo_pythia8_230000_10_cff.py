import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:15076', '1:15391', '1:28288', '1:42591', '1:42745', '1:91720', '1:94293', '1:97069', '1:98524', '1:96785', '1:65857', '1:72925', '1:23597', '1:18014', '1:22410', '1:22863', '1:18313', '1:19240', '1:19539', '1:44450', '1:44889', '1:88714', '1:54622', '1:61786', '1:64741', '1:73688', '1:66586', '1:72677', '1:91656', '1:92591', '1:83361', '1:84120', '1:27131', '1:28265', '1:28445', '1:45339', '1:71729', '1:75776', '1:75801', '1:73326', '1:75233', '1:67483', '1:80455', '1:95509', '1:24310', '1:24831', '1:24877', '1:24879', '1:24936', '1:25674', '1:25681', '1:25721', '1:25724', '1:25751', '1:47414', '1:82327', '1:75176', '1:70887', '1:70666', '1:83749', '1:85036', '1:79234', '1:16174', '1:20263', '1:23381', '1:102201', '1:47948', '1:18268', '1:18429', '1:18485', '1:44073', '1:25258', '1:25494', '1:42889', '1:12445', '1:29504', '1:98626', '1:98895', '1:83067', '1:92471', '1:93150', '1:92123', '1:92323', '1:47558', '1:47874', '1:47938', '1:47581', '1:47855', '1:49959', '1:71097', '1:72302', '1:72632', '1:81189', '1:82033', '1:96335', '1:86272', '1:87279', '1:52120', '1:52163', '1:52203', '1:52240', '1:52355', '1:53416', '1:70208', '1:65179', '1:104151', '1:104156', '1:104208', '1:30066', '1:32974', '1:98192', '1:98585', '1:104168', '1:89480', '1:29048', '1:105695', '1:98954', '1:105063', '1:106058', '1:106298', '1:101054', '1:102747', '1:104638', '1:5887', '1:6037', '1:5934', '1:7163', '1:7186', '1:7468', '1:7607', '1:67814', '1:20918', '1:81769', '1:81902', '1:62555', '1:101729', '1:102422', '1:104337', '1:104526', '1:56185', '1:61303', '1:29175', '1:52005', '1:52156', '1:52296', '1:5324', '1:6033', '1:5542', '1:5656', '1:5914', '1:5921', '1:5937', '1:6081', '1:6535', '1:9853', '1:9908', '1:9926', '1:12141', '1:12862', '1:15541', '1:8059', '1:8156', '1:9682', '1:10200', '1:10449', '1:10451', '1:15249', '1:16406', '1:16781', '1:16829', '1:13689', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C75EAD7-A60A-EA11-B2EA-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CAA33E3-B40A-EA11-B217-0CC47A4C8EB0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0C7BD80-B30A-EA11-990C-0CC47A7C345E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/827A94E9-460C-EA11-9197-0CC47A7C34D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C25D68E-CA0A-EA11-A4D3-0CC47A4D762E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EE4F23B9-260F-EA11-80C3-0CC47A4D7690.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4A38857F-43F9-E911-9334-0CC47A5FBE21.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/2A529D76-BC12-EA11-85B1-90B11C070100.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80404779-FBF6-E911-8982-AC1F6B0F71D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1A13F5EF-28F2-E911-9B0D-00215AA64960.root']);