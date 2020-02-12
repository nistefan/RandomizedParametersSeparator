import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1691', '1:8279', '1:55', '1:9228', '1:9238', '1:8440', '1:7007', '1:7011', '1:7184', '1:9229', '1:9938', '1:8841', '1:9154', '1:286', '1:7475', '1:9652', '1:2885', '1:3184', '1:9531', '1:26059', '1:9504', '1:8320', '1:7231', '1:31859', '1:6049', '1:4020', '1:10430', '1:26055', '1:28339', '1:28610', '1:3822', '1:3827', '1:5602', '1:7569', '1:7294', '1:7703', '1:7588', '1:7858', '1:29077', '1:27522', '1:27531', '1:30175', '1:25832', '1:25842', '1:25844', '1:25849', '1:34230', '1:34350', '1:34347', '1:34368', '1:34378', '1:34418', '1:31146', '1:31157', '1:31491', '1:31301', '1:31433', '1:31498', '1:31504', '1:33092', '1:6520', '1:8669', '1:9074', '1:9181', '1:8768', '1:8846', '1:9225', '1:9977', '1:29438', '1:31883', '1:33804', '1:28608', '1:28078', '1:28543', '1:34166', '1:48', '1:568', '1:3137', '1:8823', '1:3239', '1:3998', '1:1696', '1:1474', '1:6079', '1:3177', '1:7547', '1:29451', '1:31852', '1:10679', '1:7110', '1:9675', '1:9738', '1:26841', '1:28383', '1:28058', '1:33759', '1:32296', '1:4304', '1:4828', '1:4293', '1:4540', '1:7342', '1:28668', '1:33199', '1:28782', '1:28904', '1:27037', '1:27175', '1:27183', '1:27871', '1:32337', '1:28817', '1:28890', '1:32336', '1:35943', '1:25410', '1:25694', '1:25695', '1:25076', '1:29132', '1:29133', '1:31792', '1:29969', '1:29970', '1:29986', '1:29990', '1:31454', '1:34414', '1:34422', '1:34502', '1:34460', '1:34488', '1:34496', '1:2426', '1:2503', '1:2531', '1:3362', '1:3400', '1:3892', '1:4905', '1:10133', '1:10609', '1:10668', '1:6330', '1:6339', '1:9396', '1:9405', '1:6489', '1:6612', '1:10152', '1:7000', '1:10790', '1:31391', '1:31405', '1:31224', '1:5857', '1:5874', '1:26160', '1:26374', '1:26411', '1:2455', '1:2540', '1:2596', '1:2598', '1:2746', '1:2861', '1:2863', '1:5121', '1:5894', '1:2794', '1:2809', '1:4565', '1:2790', '1:5459', '1:5900', '1:5907', '1:3844', '1:7563', '1:7566', '1:7555', '1:33892', '1:33636', '1:26362', '1:26427', '1:26451', '1:26464', '1:26666', '1:26772', '1:30093', '1:30095', '1:30370', '1:30559', '1:30652', '1:30908', '1:30920', '1:30924', '1:7643', '1:34163', '1:34788', '1:34895', '1:34902', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/1A72AD25-0811-EA11-8744-002590FD5E70.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/2E6C9CF8-CD0C-EA11-A22C-FA163EE977F5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/4439EC7A-6F10-EA11-AD4B-00269E95B0A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/74EEC12D-3D11-EA11-949E-0025904B0468.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/F863856F-8F0B-EA11-94A7-E0071B7AF550.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/ECA5C43E-3710-EA11-851D-0CC47AFEFDEC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/B273DBAE-9D0C-EA11-8DBE-FA163EA53B10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/6ECE9B2C-4A0B-EA11-A9AF-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/480CFFFA-4AF8-E911-864C-509A4C9F8A8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/20000/04750700-4D05-EA11-897F-0CC47AFB7DDC.root']);