import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:68435', '1:98769', '1:99551', '1:71874', '1:72282', '1:87516', '1:87581', '1:88138', '1:97620', '1:97673', '1:98491', '1:98281', '1:98300', '1:8100', '1:8142', '1:8415', '1:7643', '1:13127', '1:14163', '1:6013', '1:7073', '1:14676', '1:18783', '1:91750', '1:91923', '1:95436', '1:96340', '1:96351', '1:100514', '1:100440', '1:101993', '1:101955', '1:27416', '1:24128', '1:39398', '1:40733', '1:30689', '1:32441', '1:51671', '1:30344', '1:31861', '1:39039', '1:28340', '1:39682', '1:34297', '1:55015', '1:55191', '1:55313', '1:67166', '1:67254', '1:67300', '1:67393', '1:67433', '1:74252', '1:68762', '1:68771', '1:64769', '1:61893', '1:63256', '1:63503', '1:63571', '1:70685', '1:71610', '1:72042', '1:72324', '1:72327', '1:72346', '1:72348', '1:74316', '1:69072', '1:69387', '1:72663', '1:78410', '1:78466', '1:78469', '1:78560', '1:81555', '1:81984', '1:80910', '1:81429', '1:85522', '1:17130', '1:10305', '1:71200', '1:53102', '1:57477', '1:58429', '1:57172', '1:69789', '1:76433', '1:51187', '1:56013', '1:57206', '1:68927', '1:69690', '1:71310', '1:71642', '1:86641', '1:85632', '1:85762', '1:86486', '1:87105', '1:102324', '1:75173', '1:102441', '1:88227', '1:89345', '1:90885', '1:91782', '1:78022', '1:78155', '1:78276', '1:78379', '1:86775', '1:87212', '1:18244', '1:13341', '1:21449', '1:38408', '1:19001', '1:19669', '1:20871', '1:40482', '1:53787', '1:36546', '1:57680', '1:49599', '1:36769', '1:38238', '1:86329', '1:87294', '1:87795', '1:100838', '1:14180', '1:18636', '1:21455', '1:7355', '1:19365', '1:54458', '1:61378', '1:62053', '1:68277', '1:76507', '1:63132', '1:68910', '1:61111', '1:102488', '1:90599', '1:90785', '1:90846', '1:90929', '1:90937', '1:74409', '1:73871', '1:73357', '1:73351', '1:74062', '1:74221', '1:75757', '1:71086', '1:78632', '1:78703', '1:87701', '1:87731', '1:15730', '1:29283', '1:38130', '1:21696', '1:26549', '1:26557', '1:63355', '1:63759', '1:64643', '1:60732', '1:51811', '1:52364', '1:52547', '1:68094', '1:85945', '1:95543', '1:99146', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CAE56D8E-3A00-EA11-A73F-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1EF4EBE2-ABFF-E911-8682-A4BF01011FD0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/04282D8B-D400-EA11-B7D4-0CC47AA98F96.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CE50307B-B601-EA11-B8E5-38EAA78D8AD0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1851DFBB-C602-EA11-B5C0-A0369FC513DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/583CB130-BF01-EA11-A2C7-0CC47AF973C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5CD29E7F-E702-EA11-B44A-009C02AAB4C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/743534C6-F402-EA11-898E-0CC47AFB7F5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/DC968BFC-3902-EA11-AF4E-A0369FE2C098.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CAFB17A7-8103-EA11-9701-0CC47AFC3C80.root']);