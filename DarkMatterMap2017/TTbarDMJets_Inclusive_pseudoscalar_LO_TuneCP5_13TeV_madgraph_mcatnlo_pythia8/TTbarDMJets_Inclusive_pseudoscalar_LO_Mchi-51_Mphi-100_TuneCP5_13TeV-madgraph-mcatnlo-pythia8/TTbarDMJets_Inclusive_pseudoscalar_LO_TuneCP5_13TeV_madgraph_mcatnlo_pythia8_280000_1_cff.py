import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11134', '1:7205', '1:26957', '1:91077', '1:91249', '1:91306', '1:92967', '1:83137', '1:75647', '1:75898', '1:73130', '1:84018', '1:84099', '1:76368', '1:76618', '1:87433', '1:96768', '1:74710', '1:74810', '1:78371', '1:78477', '1:82473', '1:84439', '1:54038', '1:65784', '1:65875', '1:67828', '1:72172', '1:72517', '1:89738', '1:74406', '1:74536', '1:74697', '1:38779', '1:38780', '1:68034', '1:34553', '1:35899', '1:36048', '1:37190', '1:37226', '1:38072', '1:63238', '1:91086', '1:94155', '1:77036', '1:93386', '1:73792', '1:73489', '1:70368', '1:84979', '1:71124', '1:71391', '1:71527', '1:71748', '1:71968', '1:71972', '1:75108', '1:89164', '1:97712', '1:97971', '1:98484', '1:90299', '1:90609', '1:89305', '1:89823', '1:90148', '1:90266', '1:90408', '1:37418', '1:53865', '1:54110', '1:74672', '1:82987', '1:65209', '1:71211', '1:81478', '1:65726', '1:56826', '1:56962', '1:56621', '1:66307', '1:66574', '1:67427', '1:71001', '1:71014', '1:67261', '1:72198', '1:60858', '1:60627', '1:78536', '1:64527', '1:74188', '1:74258', '1:78222', '1:78504', '1:90193', '1:90305', '1:90443', '1:74187', '1:74341', '1:74387', '1:74467', '1:74482', '1:75803', '1:66481', '1:66492', '1:66529', '1:66686', '1:67465', '1:84944', '1:90044', '1:79639', '1:85063', '1:89601', '1:71882', '1:81992', '1:92193', '1:78329', '1:79228', '1:79399', '1:79486', '1:79292', '1:79300', '1:82909', '1:83136', '1:83144', '1:76020', '1:76531', '1:103165', '1:84085', '1:84696', '1:90971', '1:90991', '1:91150', '1:57618', '1:57660', '1:61533', '1:61550', '1:83912', '1:103103', '1:78063', '1:65241', '1:72524', '1:82772', '1:76720', '1:97508', '1:98636', '1:103471', '1:103485', '1:103685', '1:103695', '1:85587', '1:86866', '1:91110', '1:91613', '1:78782', '1:78897', '1:78970', '1:80958', '1:81080', '1:81143', '1:94175', '1:106241', '1:82810', '1:90359', '1:90638', '1:90734', '1:89572', '1:105706', '1:68167', '1:68171', '1:68178', '1:68179', '1:68182', '1:68244', '1:66485', '1:66565', '1:66782', '1:98979', '1:97664', '1:102105', '1:103397', '1:84705', '1:77303', '1:81838', '1:82129', '1:93998', '1:91649', '1:67933', '1:72186', '1:73363', '1:73384', '1:73360', '1:73395', '1:96219', '1:105306', '1:105593', '1:84500', '1:72', '1:45', '1:963', '1:287', '1:775', '1:37427', '1:3303', '1:1035', '1:36958', '1:38357', '1:51382', '1:57215', '1:57579', '1:59093', '1:51570', '1:80210', '1:81747', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/1C9C6947-3818-EA11-B7C0-0CC47AA992AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/B28BC2BA-B318-EA11-B8C6-0025905A60A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/3E19ACBC-B318-EA11-B9D6-AC1F6BAC816E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/F0087DB3-B318-EA11-97EB-0025905A48E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/CC9AC8B3-B318-EA11-BB72-0025905B859E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/5EA0C1BE-B318-EA11-987C-AC1F6BAC7C4A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/52F0C4B8-B318-EA11-BE8C-0025905A60B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/AA45AB59-B118-EA11-91AB-0025905A6104.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/80F1D651-B118-EA11-91B6-0CC47A4D7644.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/D8D308B4-CA17-EA11-92E0-FA163E1C81E7.root']);