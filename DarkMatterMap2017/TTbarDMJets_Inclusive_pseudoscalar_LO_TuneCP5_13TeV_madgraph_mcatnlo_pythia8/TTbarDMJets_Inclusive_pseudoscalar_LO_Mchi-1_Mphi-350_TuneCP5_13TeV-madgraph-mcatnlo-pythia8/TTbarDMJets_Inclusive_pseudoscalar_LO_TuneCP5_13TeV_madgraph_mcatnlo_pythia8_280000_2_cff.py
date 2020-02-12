import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:50582', '1:50610', '1:50705', '1:65163', '1:80111', '1:65192', '1:65224', '1:100002', '1:70194', '1:7891', '1:16393', '1:14653', '1:14451', '1:15641', '1:20072', '1:62402', '1:50779', '1:86052', '1:86312', '1:31152', '1:31240', '1:23006', '1:33677', '1:33816', '1:33281', '1:33773', '1:33851', '1:55161', '1:33829', '1:33964', '1:60160', '1:18450', '1:40033', '1:44539', '1:48469', '1:40855', '1:45868', '1:46173', '1:49289', '1:55156', '1:31416', '1:31432', '1:31545', '1:31677', '1:31707', '1:35466', '1:35476', '1:37914', '1:67738', '1:61861', '1:33978', '1:37970', '1:38042', '1:50094', '1:50263', '1:94867', '1:67103', '1:65660', '1:65872', '1:65932', '1:72359', '1:73429', '1:95651', '1:68805', '1:99741', '1:72123', '1:72072', '1:77654', '1:74662', '1:74716', '1:74846', '1:78925', '1:79118', '1:87533', '1:103345', '1:86416', '1:86471', '1:22083', '1:22131', '1:22204', '1:22275', '1:22294', '1:58529', '1:77520', '1:86593', '1:81308', '1:80903', '1:78737', '1:78899', '1:79019', '1:78896', '1:71525', '1:81764', '1:82895', '1:105551', '1:105129', '1:105283', '1:105403', '1:53295', '1:65250', '1:67245', '1:61331', '1:73385', '1:78798', '1:52845', '1:64876', '1:66139', '1:66245', '1:72840', '1:67705', '1:67938', '1:73459', '1:74476', '1:77352', '1:83628', '1:86502', '1:91815', '1:85853', '1:55000', '1:72615', '1:73328', '1:59612', '1:82277', '1:82555', '1:94948', '1:97152', '1:91424', '1:94144', '1:94269', '1:100117', '1:105869', '1:105900', '1:105909', '1:53704', '1:56282', '1:68594', '1:68599', '1:68601', '1:68621', '1:95400', '1:95525', '1:61564', '1:85055', '1:89510', '1:63057', '1:63275', '1:63278', '1:63632', '1:63645', '1:66805', '1:71438', '1:81212', '1:64557', '1:65863', '1:65703', '1:66448', '1:86993', '1:87092', '1:87171', '1:105371', '1:105503', '1:105635', '1:45677', '1:47095', '1:40904', '1:43460', '1:94464', '1:95240', '1:60650', '1:60651', '1:60770', '1:61139', '1:61126', '1:61074', '1:61250', '1:61057', '1:60904', '1:60906', '1:61353', '1:61387', '1:61714', '1:71684', '1:88294', '1:82114', '1:33106', '1:33168', '1:33193', '1:75443', '1:78368', '1:79643', '1:80303', '1:81911', '1:87047', '1:76345', '1:73083', '1:55280', '1:57280', '1:68666', '1:68752', '1:63997', '1:77608', '1:83265', '1:82751', '1:83004', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/8867CCB3-B318-EA11-9095-0025905B859E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/6E39EBAF-B318-EA11-AA8D-AC1F6BAC7C10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/8CD12CC8-FE17-EA11-AB2D-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/BE1577AC-B318-EA11-84E0-0CC47A4C8E28.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/1CC8E6A9-B318-EA11-B94C-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/CC27F754-B118-EA11-82F0-AC1F6BAC8038.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/0C4EB1B9-B318-EA11-A9AA-0025905B8594.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/C0348BAE-B318-EA11-97D9-0CC47A4C8E22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/DE5063B5-B318-EA11-9FEF-0CC47A7C3450.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/66967FAD-B318-EA11-B842-0CC47A78A33E.root']);