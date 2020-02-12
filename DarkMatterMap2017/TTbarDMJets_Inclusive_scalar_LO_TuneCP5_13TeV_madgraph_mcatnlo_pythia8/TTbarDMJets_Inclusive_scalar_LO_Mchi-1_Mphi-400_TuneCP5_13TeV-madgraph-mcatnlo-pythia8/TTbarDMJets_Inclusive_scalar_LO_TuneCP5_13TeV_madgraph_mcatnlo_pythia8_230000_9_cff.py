import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:21857', '1:22155', '1:22459', '1:21376', '1:21680', '1:21749', '1:52175', '1:69975', '1:68001', '1:98674', '1:52414', '1:60432', '1:75088', '1:78274', '1:70458', '1:77259', '1:99828', '1:99905', '1:98955', '1:99271', '1:100126', '1:31804', '1:35806', '1:40964', '1:67793', '1:68496', '1:67123', '1:67552', '1:60712', '1:63641', '1:20528', '1:10067', '1:10831', '1:13123', '1:14181', '1:27041', '1:30850', '1:39663', '1:40495', '1:58134', '1:27967', '1:52160', '1:53433', '1:27241', '1:28642', '1:28886', '1:61139', '1:59130', '1:59637', '1:60267', '1:60967', '1:70175', '1:70195', '1:71306', '1:62363', '1:74189', '1:74330', '1:74441', '1:74552', '1:75796', '1:95738', '1:95679', '1:95707', '1:95884', '1:60643', '1:60846', '1:60949', '1:61042', '1:61335', '1:61476', '1:61644', '1:67349', '1:72313', '1:72315', '1:73283', '1:77836', '1:98793', '1:97545', '1:99610', '1:26756', '1:33095', '1:76663', '1:97378', '1:100057', '1:102249', '1:102521', '1:97916', '1:99919', '1:99962', '1:100225', '1:100956', '1:86828', '1:90718', '1:85562', '1:88726', '1:91216', '1:86981', '1:89473', '1:89927', '1:766', '1:23254', '1:23431', '1:49926', '1:50097', '1:62326', '1:68099', '1:85353', '1:85398', '1:85419', '1:85459', '1:85949', '1:86361', '1:28139', '1:39501', '1:39623', '1:39760', '1:40068', '1:40885', '1:73049', '1:73278', '1:75355', '1:76506', '1:76529', '1:85941', '1:75700', '1:78355', '1:77587', '1:77927', '1:79321', '1:79440', '1:79505', '1:79529', '1:79539', '1:98816', '1:76093', '1:76266', '1:76627', '1:76194', '1:77644', '1:79138', '1:79139', '1:79273', '1:79341', '1:86437', '1:86508', '1:86666', '1:2974', '1:16430', '1:16454', '1:16583', '1:16827', '1:21204', '1:20061', '1:20167', '1:63007', '1:53726', '1:54093', '1:54169', '1:54026', '1:54182', '1:53194', '1:53302', '1:53161', '1:53473', '1:53602', '1:67112', '1:67154', '1:68318', '1:68657', '1:68753', '1:68912', '1:68951', '1:69209', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/183425A0-2CF9-E911-8A59-0CC47AC17502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/14013B83-ED0C-EA11-A969-0CC47A4C8E16.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D8BE5B85-CD00-EA11-8D89-008CFA197DDC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8EA49950-280B-EA11-8D88-0CC47A7C353E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C80BC002-AE01-EA11-8935-509A4C9EF929.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94EED3C0-3913-EA11-9D36-003048F1C4AC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CC49EA7-DAFA-E911-B4D9-549F3525C318.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7ED89422-6000-EA11-91BA-509A4C9EF8FF.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/02A19D30-BF01-EA11-8C20-0CC47AF973C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/986C80F8-D001-EA11-B39E-509A4C9F8A64.root']);