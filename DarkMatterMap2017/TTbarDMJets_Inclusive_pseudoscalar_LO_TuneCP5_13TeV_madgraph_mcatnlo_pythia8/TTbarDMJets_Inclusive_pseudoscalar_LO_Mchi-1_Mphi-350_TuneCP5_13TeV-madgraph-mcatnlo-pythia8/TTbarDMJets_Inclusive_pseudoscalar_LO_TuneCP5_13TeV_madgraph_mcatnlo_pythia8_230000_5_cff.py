import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:27975', '1:39518', '1:48133', '1:28148', '1:29494', '1:30449', '1:44440', '1:74409', '1:54006', '1:65264', '1:56671', '1:78469', '1:94385', '1:1044', '1:5254', '1:13879', '1:8365', '1:15425', '1:81518', '1:5055', '1:5120', '1:6707', '1:9066', '1:9171', '1:9309', '1:9512', '1:20283', '1:20513', '1:20507', '1:20794', '1:20802', '1:13783', '1:21113', '1:21428', '1:26381', '1:65928', '1:39943', '1:45707', '1:52489', '1:1137', '1:3398', '1:4945', '1:7357', '1:23260', '1:26153', '1:31538', '1:25848', '1:25913', '1:24494', '1:24496', '1:24520', '1:25749', '1:48501', '1:58212', '1:75327', '1:40993', '1:40967', '1:41176', '1:47366', '1:64981', '1:65836', '1:65860', '1:65871', '1:57643', '1:57822', '1:58059', '1:58625', '1:66545', '1:66721', '1:76672', '1:88563', '1:93257', '1:75371', '1:80131', '1:85838', '1:87781', '1:88020', '1:88327', '1:89106', '1:58699', '1:58780', '1:58854', '1:58895', '1:59062', '1:66018', '1:67021', '1:98860', '1:77827', '1:77925', '1:79669', '1:88445', '1:88728', '1:88735', '1:88747', '1:97963', '1:98694', '1:97503', '1:97779', '1:98169', '1:98963', '1:3243', '1:3503', '1:3680', '1:17022', '1:17217', '1:17272', '1:17273', '1:31542', '1:81084', '1:94674', '1:95869', '1:95828', '1:96068', '1:96730', '1:20854', '1:23081', '1:23771', '1:23778', '1:24196', '1:48006', '1:48202', '1:51346', '1:51347', '1:51666', '1:52136', '1:39367', '1:39721', '1:39900', '1:83839', '1:84192', '1:83774', '1:86293', '1:85380', '1:85510', '1:59916', '1:60002', '1:60303', '1:60423', '1:65803', '1:70599', '1:70787', '1:70876', '1:77293', '1:77462', '1:71853', '1:66910', '1:83114', '1:83138', '1:83142', '1:86828', '1:101099', '1:101603', '1:101632', '1:39254', '1:39260', '1:39356', '1:39415', '1:67336', '1:67742', '1:71375', '1:71501', '1:71538', '1:71889', '1:71508', '1:85545', '1:90089', '1:94306', '1:94665', '1:94874', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7624CF22-0CF9-E911-808F-20040FF492B8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/12EC825B-0CF9-E911-A9DF-48FD8E28297D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BEC2A377-41FA-E911-8025-003048CB8774.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8A5960E-7BFB-E911-95A4-002590DE6DD4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5C9FA45D-A7FB-E911-9447-509A4C9EF8EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8E3716C9-CDFB-E911-8B96-38EAA78D8ADC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3E02F6CD-ECFA-E911-8929-0025901D46E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/22CEA9F6-64FB-E911-A65E-FA163EA5C970.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7C02D95E-99FB-E911-8737-98039B3B01D2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/186E3CC5-81FB-E911-9317-A4BF01288315.root']);