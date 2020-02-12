import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:16997', '1:2005', '1:12943', '1:15070', '1:26474', '1:31017', '1:90879', '1:91322', '1:70772', '1:71228', '1:70682', '1:78190', '1:75701', '1:75768', '1:84255', '1:77679', '1:77702', '1:78548', '1:78710', '1:82346', '1:82727', '1:32302', '1:55043', '1:55988', '1:72634', '1:90114', '1:74678', '1:74679', '1:34032', '1:34881', '1:34991', '1:38643', '1:34055', '1:35870', '1:34904', '1:77470', '1:86517', '1:87245', '1:92951', '1:64080', '1:81040', '1:83962', '1:84862', '1:71318', '1:72450', '1:72710', '1:77188', '1:77199', '1:71372', '1:71373', '1:71412', '1:71990', '1:71955', '1:81272', '1:75026', '1:75061', '1:75284', '1:75341', '1:75429', '1:91325', '1:89826', '1:89833', '1:89915', '1:68293', '1:34251', '1:68609', '1:53976', '1:64542', '1:66948', '1:66315', '1:57013', '1:66751', '1:67452', '1:67524', '1:67504', '1:67265', '1:67278', '1:67509', '1:67408', '1:72139', '1:72333', '1:84867', '1:60898', '1:75096', '1:64260', '1:73683', '1:90758', '1:74095', '1:74353', '1:74524', '1:75649', '1:74692', '1:66638', '1:71203', '1:67479', '1:67585', '1:67316', '1:93544', '1:88514', '1:72552', '1:79280', '1:79328', '1:79380', '1:79727', '1:82849', '1:77557', '1:84468', '1:90518', '1:90521', '1:90682', '1:90693', '1:90899', '1:92002', '1:92032', '1:57901', '1:57963', '1:71051', '1:71194', '1:66719', '1:66680', '1:66934', '1:103006', '1:77327', '1:64437', '1:79520', '1:79616', '1:65404', '1:82916', '1:85165', '1:76244', '1:76526', '1:97760', '1:97900', '1:98372', '1:103596', '1:92685', '1:81305', '1:81117', '1:98359', '1:89041', '1:106122', '1:106198', '1:106260', '1:90343', '1:90469', '1:89204', '1:89214', '1:89199', '1:68174', '1:85126', '1:66507', '1:66876', '1:95998', '1:96108', '1:102787', '1:103477', '1:67943', '1:68123', '1:103327', '1:88894', '1:67910', '1:73052', '1:73444', '1:73451', '1:73270', '1:73335', '1:73337', '1:73426', '1:73515', '1:73378', '1:73703', '1:73790', '1:105663', '1:84477', '1:84731', '1:972', '1:973', '1:37920', '1:1004', '1:8295', '1:13211', '1:18522', '1:36961', '1:36966', '1:37607', '1:52584', '1:52810', '1:55730', '1:57528', '1:52519', '1:80979', '1:81954', '1:80275', '1:79835', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/1C9C6947-3818-EA11-B7C0-0CC47AA992AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/B28BC2BA-B318-EA11-B8C6-0025905A60A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/3E19ACBC-B318-EA11-B9D6-AC1F6BAC816E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/F0087DB3-B318-EA11-97EB-0025905A48E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/CC9AC8B3-B318-EA11-BB72-0025905B859E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/5EA0C1BE-B318-EA11-987C-AC1F6BAC7C4A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/52F0C4B8-B318-EA11-BE8C-0025905A60B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/AA45AB59-B118-EA11-91AB-0025905A6104.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/80F1D651-B118-EA11-91B6-0CC47A4D7644.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/D8D308B4-CA17-EA11-92E0-FA163E1C81E7.root']);