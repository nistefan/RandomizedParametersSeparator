import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11591', '1:11925', '1:11931', '1:11718', '1:11863', '1:13401', '1:13412', '1:13595', '1:13625', '1:13260', '1:13268', '1:13371', '1:13349', '1:13410', '1:13462', '1:13483', '1:13800', '1:13757', '1:13765', '1:13750', '1:13864', '1:13969', '1:13975', '1:25545', '1:25499', '1:25518', '1:25568', '1:25831', '1:25899', '1:25607', '1:25754', '1:29261', '1:29311', '1:29422', '1:29477', '1:29552', '1:30078', '1:30114', '1:31389', '1:30130', '1:30145', '1:30159', '1:101993', '1:11143', '1:11417', '1:11479', '1:11532', '1:13170', '1:11917', '1:13258', '1:13956', '1:22327', '1:25842', '1:29520', '1:29545', '1:29610', '1:29576', '1:29632', '1:29635', '1:30052', '1:30342', '1:30380', '1:30433', '1:30448', '1:30373', '1:31885', '1:31887', '1:31900', '1:31934', '1:31963', '1:31633', '1:31460', '1:31471', '1:31511', '1:31595', '1:31918', '1:31653', '1:31696', '1:89523', '1:101012', '1:101071', '1:90051', '1:22088', '1:22093', '1:22122', '1:13984', '1:13985', '1:89865', '1:22994', '1:101328', '1:101356', '1:101309', '1:101340', '1:101343', '1:101361', '1:101368', '1:89890', '1:89936', '1:101332', '1:90329', '1:25136', '1:90895', '1:90338', '1:90687', '1:90912', '1:25058', '1:25212', '1:25319', '1:89851', '1:89854', '1:89898', '1:89570', '1:89587', '1:89938', '1:90606', '1:90454', '1:90498', '1:29224', '1:29264', '1:29286', '1:25788', '1:29084', '1:29153', '1:101627', '1:90441', '1:90475', '1:90515', '1:90547', '1:29428', '1:29431', '1:29519', '1:29565', '1:29122', '1:29351', '1:29355', '1:29369', '1:29370', '1:29192', '1:29327', '1:29704', '1:29942', '1:30034', '1:30119', '1:31583', '1:31608', '1:31689', '1:31702', '1:13004', '1:22173', '1:22539', '1:13039', '1:13109', '1:22252', '1:31880', '1:89448', '1:89827', '1:101438', '1:101479', '1:90355', '1:101443', '1:101487', '1:89081', '1:89086', '1:89115', '1:89243', '1:31814', '1:89164', '1:89353', '1:89719', '1:89731', '1:89756', '1:89288', '1:30530', '1:89310', '1:89984', '1:101797', '1:89339', '1:101146', '1:90389', '1:11091', '1:11213', '1:11522', '1:11750', '1:13892', '1:13923', '1:22356', '1:25588', '1:31813', '1:31847', '1:22463', '1:25119', '1:25953', '1:29178', '1:31858', '1:101452', '1:101892', '1:90395', '1:90433', '1:101583', '1:31836', '1:89785', '1:101392', '1:101457', '1:101899', '1:11538', '1:11570', '1:11734', '1:11640', '1:11749', '1:11673', '1:11683', '1:11700', '1:11715', '1:11728', '1:11764', '1:11809', '1:11842', '1:11906', '1:13997', '1:22544', '1:22593', '1:22616', '1:22471', '1:22497', '1:22515', '1:22482', '1:11315', '1:11338', '1:11612', '1:13070', '1:13331', '1:13333', '1:13351', '1:13608', '1:30757', '1:30788', '1:31260', '1:101056', '1:101156', '1:101080', '1:101260', '1:90869', '1:90885', '1:90942', '1:90992', '1:22436', '1:25435', '1:25514', '1:25722', '1:25723', '1:25766', '1:25774', '1:29055', '1:29006', '1:29127', '1:29446', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/BA08AC92-32EF-E911-82D8-441EA1616DEA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/1A47AC00-7B03-EA11-9EE6-0CC47AF973C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DA862DF2-9F11-EA11-A5FB-C4346BC75558.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DC992538-9910-EA11-BF7F-0CC47A5FC281.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/163497F8-2D11-EA11-A132-6C2B599A050D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/0A3BC253-8411-EA11-A6F0-D8D385AF891A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/562C1852-3411-EA11-A53F-8CDCD4A9A484.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/E6105D38-A311-EA11-9524-0CC47A7E6A5C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D86A4CB2-9014-EA11-8CA9-F01FAFE5CF52.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C0549F53-A714-EA11-8560-782BCB46E733.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/70D29667-41FB-E911-818C-38EAA78D8ACC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/B8C911EE-29F0-E911-8638-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/0E7BC3B3-0AFA-E911-8213-98039B3B01B2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DE54B8C9-DA10-EA11-89A8-A4BF01125538.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/2ABD4E37-8F03-EA11-815A-1866DA86CCDF.root']);