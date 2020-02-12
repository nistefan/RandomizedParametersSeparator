import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:59118', '1:50567', '1:50584', '1:50675', '1:57967', '1:64558', '1:67812', '1:84884', '1:65007', '1:84108', '1:74124', '1:65259', '1:65517', '1:65614', '1:83480', '1:93985', '1:11949', '1:13960', '1:77185', '1:50747', '1:50750', '1:50788', '1:96413', '1:103020', '1:86061', '1:86194', '1:93971', '1:93976', '1:85991', '1:86189', '1:86814', '1:87353', '1:31058', '1:31339', '1:21118', '1:33820', '1:33752', '1:33768', '1:35639', '1:35659', '1:33777', '1:34109', '1:47194', '1:47225', '1:40490', '1:31647', '1:37497', '1:33919', '1:38615', '1:38717', '1:50332', '1:50093', '1:68732', '1:68054', '1:95250', '1:66183', '1:72191', '1:72287', '1:72683', '1:72337', '1:73527', '1:74687', '1:74628', '1:74636', '1:74772', '1:90349', '1:91049', '1:68707', '1:68708', '1:68723', '1:68772', '1:68794', '1:68819', '1:68830', '1:100009', '1:72160', '1:72180', '1:71977', '1:78929', '1:79056', '1:79169', '1:86204', '1:104233', '1:86449', '1:22056', '1:22148', '1:87969', '1:81101', '1:80909', '1:78671', '1:79227', '1:79132', '1:71656', '1:71127', '1:71514', '1:82266', '1:82285', '1:82526', '1:82766', '1:83027', '1:105332', '1:105387', '1:105451', '1:49425', '1:58254', '1:58375', '1:67750', '1:67931', '1:78293', '1:89634', '1:76440', '1:64745', '1:65138', '1:76045', '1:66015', '1:73272', '1:72836', '1:67838', '1:74981', '1:74997', '1:96741', '1:106085', '1:66749', '1:57003', '1:80696', '1:86876', '1:78855', '1:92596', '1:105794', '1:105661', '1:105868', '1:68764', '1:68771', '1:68753', '1:95409', '1:95878', '1:77160', '1:78071', '1:62241', '1:70477', '1:87860', '1:95874', '1:70483', '1:90143', '1:63270', '1:64382', '1:64914', '1:64970', '1:65687', '1:65850', '1:86441', '1:86520', '1:87000', '1:91942', '1:92158', '1:61035', '1:61191', '1:61362', '1:60940', '1:61059', '1:60889', '1:61047', '1:61120', '1:61477', '1:67886', '1:70077', '1:70952', '1:81940', '1:34612', '1:37469', '1:78835', '1:78892', '1:79433', '1:81559', '1:75305', '1:75559', '1:76321', '1:81388', '1:68630', '1:63946', '1:64032', '1:79153', '1:78998', '1:100487', '1:101846', '1:104978', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/8867CCB3-B318-EA11-9095-0025905B859E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/6E39EBAF-B318-EA11-AA8D-AC1F6BAC7C10.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/8CD12CC8-FE17-EA11-AB2D-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/BE1577AC-B318-EA11-84E0-0CC47A4C8E28.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/1CC8E6A9-B318-EA11-B94C-0CC47A78A458.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/CC27F754-B118-EA11-82F0-AC1F6BAC8038.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/0C4EB1B9-B318-EA11-A9AA-0025905B8594.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/C0348BAE-B318-EA11-97D9-0CC47A4C8E22.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/DE5063B5-B318-EA11-9FEF-0CC47A7C3450.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/280000/66967FAD-B318-EA11-B842-0CC47A78A33E.root']);