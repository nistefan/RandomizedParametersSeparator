import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11939', '1:11965', '1:11971', '1:11411', '1:11731', '1:13520', '1:13579', '1:13303', '1:13279', '1:13444', '1:13479', '1:13501', '1:13789', '1:13798', '1:13718', '1:13761', '1:13855', '1:13964', '1:22075', '1:13293', '1:25454', '1:25463', '1:25573', '1:25752', '1:29210', '1:29228', '1:29249', '1:29251', '1:29253', '1:29263', '1:29281', '1:29288', '1:29293', '1:29307', '1:29441', '1:29442', '1:29471', '1:30045', '1:30079', '1:30067', '1:30080', '1:30108', '1:30161', '1:30131', '1:101995', '1:11380', '1:11382', '1:13042', '1:13158', '1:13891', '1:22038', '1:22058', '1:22331', '1:22989', '1:25861', '1:29440', '1:29568', '1:29573', '1:29667', '1:29639', '1:30050', '1:30241', '1:30252', '1:30256', '1:30258', '1:30264', '1:30293', '1:30345', '1:30357', '1:30354', '1:30372', '1:31378', '1:31428', '1:31922', '1:31924', '1:31504', '1:31630', '1:31530', '1:31628', '1:31526', '1:31661', '1:31683', '1:89857', '1:90030', '1:101002', '1:101320', '1:13949', '1:22105', '1:13818', '1:13980', '1:13993', '1:13999', '1:14000', '1:89631', '1:101017', '1:101033', '1:22205', '1:22763', '1:22967', '1:101315', '1:101317', '1:101341', '1:101349', '1:101351', '1:89924', '1:89963', '1:101372', '1:90341', '1:90625', '1:90888', '1:90937', '1:25048', '1:25077', '1:25086', '1:25113', '1:25223', '1:25314', '1:25326', '1:25331', '1:89632', '1:89881', '1:89571', '1:89598', '1:29244', '1:29284', '1:29308', '1:25989', '1:29156', '1:90050', '1:90153', '1:90167', '1:90186', '1:101418', '1:101420', '1:101626', '1:90511', '1:90438', '1:90502', '1:90577', '1:29412', '1:29429', '1:29436', '1:29532', '1:29142', '1:29352', '1:29371', '1:29963', '1:30036', '1:31594', '1:31601', '1:31609', '1:31634', '1:31757', '1:31759', '1:11451', '1:13655', '1:13941', '1:31728', '1:11087', '1:13554', '1:13642', '1:13656', '1:89687', '1:101580', '1:30254', '1:89054', '1:89005', '1:30974', '1:89360', '1:89711', '1:89801', '1:89646', '1:89299', '1:89671', '1:89757', '1:89786', '1:89658', '1:90397', '1:90430', '1:11214', '1:11334', '1:11356', '1:11413', '1:11984', '1:13026', '1:13108', '1:13759', '1:13893', '1:22181', '1:22976', '1:25283', '1:30927', '1:31799', '1:31831', '1:31861', '1:90363', '1:90387', '1:101444', '1:101678', '1:101893', '1:22217', '1:22242', '1:22987', '1:25827', '1:25939', '1:25945', '1:25816', '1:31822', '1:89153', '1:11596', '1:11590', '1:11717', '1:11835', '1:11630', '1:11680', '1:11726', '1:11795', '1:11856', '1:11953', '1:11777', '1:22227', '1:22622', '1:22709', '1:22396', '1:22491', '1:11428', '1:11574', '1:11224', '1:11269', '1:11156', '1:11272', '1:11276', '1:13060', '1:13048', '1:13321', '1:13605', '1:13358', '1:13393', '1:29148', '1:30588', '1:30773', '1:31243', '1:31246', '1:31412', '1:31435', '1:101021', '1:101248', '1:90866', '1:90876', '1:90918', '1:90926', '1:90928', '1:90923', '1:22134', '1:22172', '1:13967', '1:22002', '1:22003', '1:22135', '1:22156', '1:22291', '1:22445', '1:25491', '1:25508', '1:25720', '1:25743', '1:29056', '1:29068', '1:29495', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/BA08AC92-32EF-E911-82D8-441EA1616DEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/1A47AC00-7B03-EA11-9EE6-0CC47AF973C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DA862DF2-9F11-EA11-A5FB-C4346BC75558.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DC992538-9910-EA11-BF7F-0CC47A5FC281.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/163497F8-2D11-EA11-A132-6C2B599A050D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/0A3BC253-8411-EA11-A6F0-D8D385AF891A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/562C1852-3411-EA11-A53F-8CDCD4A9A484.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/E6105D38-A311-EA11-9524-0CC47A7E6A5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D86A4CB2-9014-EA11-8CA9-F01FAFE5CF52.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C0549F53-A714-EA11-8560-782BCB46E733.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/70D29667-41FB-E911-818C-38EAA78D8ACC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/B8C911EE-29F0-E911-8638-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/0E7BC3B3-0AFA-E911-8213-98039B3B01B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DE54B8C9-DA10-EA11-89A8-A4BF01125538.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/2ABD4E37-8F03-EA11-815A-1866DA86CCDF.root']);