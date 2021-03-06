import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:76016', '1:80831', '1:86094', '1:85331', '1:91134', '1:101222', '1:101921', '1:95723', '1:97765', '1:101322', '1:102878', '1:101481', '1:101838', '1:104690', '1:104731', '1:104910', '1:104966', '1:11917', '1:21676', '1:21781', '1:14369', '1:26218', '1:23493', '1:28623', '1:18446', '1:40462', '1:43635', '1:43650', '1:46774', '1:47757', '1:47628', '1:47629', '1:44297', '1:47744', '1:13812', '1:13404', '1:13418', '1:14488', '1:14164', '1:14480', '1:14811', '1:14946', '1:15239', '1:16956', '1:17994', '1:19035', '1:19699', '1:24708', '1:60991', '1:61429', '1:42318', '1:42615', '1:42662', '1:44473', '1:83386', '1:90295', '1:88186', '1:86348', '1:86954', '1:86530', '1:90588', '1:90961', '1:91683', '1:95275', '1:105112', '1:105291', '1:105636', '1:91923', '1:83226', '1:86686', '1:91619', '1:84761', '1:85912', '1:93513', '1:95759', '1:97197', '1:84044', '1:92157', '1:102750', '1:104812', '1:101405', '1:102669', '1:102672', '1:1820', '1:1862', '1:4669', '1:53439', '1:53576', '1:53657', '1:58964', '1:59177', '1:59438', '1:59445', '1:8549', '1:8640', '1:8928', '1:9733', '1:40371', '1:32877', '1:8993', '1:27228', '1:27286', '1:27465', '1:27560', '1:25901', '1:27529', '1:32045', '1:26888', '1:26146', '1:17460', '1:19953', '1:39587', '1:73988', '1:70153', '1:70207', '1:80966', '1:22450', '1:52209', '1:44316', '1:44477', '1:45069', '1:44937', '1:45211', '1:72478', '1:64001', '1:70645', '1:70785', '1:70808', '1:70888', '1:77004', '1:77067', '1:77092', '1:77243', '1:101435', '1:105345', '1:106388', '1:24512', '1:24753', '1:24775', '1:24885', '1:84283', '1:85713', '1:82577', '1:83676', '1:74977', '1:79948', '1:80071', '1:77651', '1:82273', '1:7127', '1:6160', '1:40674', '1:40840', '1:52241', '1:52388', '1:52516', '1:52549', '1:58824', '1:22711', '1:27316', '1:27359', '1:27445', '1:27634', '1:27828', '1:82242', '1:82412', '1:82681', '1:48032', '1:48797', '1:48825', '1:51519', '1:58404', '1:46418', '1:46658', '1:44406', '1:43303', '1:43358', '1:43501', '1:43593', '1:44341', '1:47649', '1:47812', '1:26634', '1:86803', '1:95278', '1:106138', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6A721CBE-4B07-EA11-9750-0CC47A4D7646.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCF6B8AB-E003-EA11-AAE8-44A842BE8F7E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9EAE1061-30F8-E911-B2D5-AC1F6B0F676C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/86727FE6-AF0A-EA11-B38D-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2A16734-8607-EA11-A7C2-0025905A6060.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/723E26E0-88FC-E911-A84F-0CC47AFCC666.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/643155F4-E80A-EA11-BD55-0CC47A7C3636.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC1243A5-AA0A-EA11-A2C9-0CC47A7C347A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24362999-4EFE-E911-BFEB-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1207CE62-4EF9-E911-85E0-C4346BC85718.root']);