import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8574', '1:19531', '1:29716', '1:36096', '1:52566', '1:53073', '1:53079', '1:24064', '1:30691', '1:37858', '1:40710', '1:40744', '1:46282', '1:34947', '1:24934', '1:28048', '1:30767', '1:37466', '1:40220', '1:85172', '1:96473', '1:13869', '1:14009', '1:15214', '1:15816', '1:14267', '1:53977', '1:54763', '1:64748', '1:68870', '1:55741', '1:62476', '1:62660', '1:102201', '1:102176', '1:9948', '1:19939', '1:15337', '1:22794', '1:54031', '1:57998', '1:63769', '1:70204', '1:70704', '1:77031', '1:13845', '1:22756', '1:68508', '1:69849', '1:76904', '1:69083', '1:69850', '1:71984', '1:78341', '1:88349', '1:89317', '1:89766', '1:89853', '1:94049', '1:64569', '1:54586', '1:61997', '1:63243', '1:64013', '1:64355', '1:69561', '1:75804', '1:85880', '1:91226', '1:91823', '1:91893', '1:91899', '1:91599', '1:88849', '1:89712', '1:79755', '1:79103', '1:79966', '1:81010', '1:81943', '1:72566', '1:73833', '1:77075', '1:85135', '1:85144', '1:85177', '1:85430', '1:88587', '1:4312', '1:58132', '1:59492', '1:88602', '1:58162', '1:51236', '1:64338', '1:70562', '1:81712', '1:85371', '1:71740', '1:79056', '1:88009', '1:52463', '1:51392', '1:52333', '1:97017', '1:96907', '1:76558', '1:67641', '1:67944', '1:73080', '1:85783', '1:87722', '1:85847', '1:86458', '1:96661', '1:94460', '1:94515', '1:95957', '1:96492', '1:96650', '1:96552', '1:99865', '1:99873', '1:99345', '1:95569', '1:96714', '1:35911', '1:36009', '1:37268', '1:72052', '1:75584', '1:71970', '1:72647', '1:72648', '1:72999', '1:78698', '1:89006', '1:89916', '1:91336', '1:101027', '1:101328', '1:99425', '1:99671', '1:89480', '1:96587', '1:79911', '1:85054', '1:14154', '1:17753', '1:25973', '1:73313', '1:90577', '1:95250', '1:95120', '1:95129', '1:95143', '1:95527', '1:4470', '1:4723', '1:4936', '1:5470', '1:5547', '1:5810', '1:99423', '1:86257', '1:86726', '1:35377', '1:94372', '1:75811', '1:88525', '1:101134', '1:88503', '1:94477', '1:98609', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/663C015C-090B-EA11-BFB8-0CC47A4D761A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C1F2C40-140B-EA11-B0C9-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50E09B46-0F0B-EA11-B430-0CC47A7C353E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/00B4F279-060B-EA11-B0D5-44A842CFD64D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/42F08944-8A0B-EA11-81BC-0CC47A4D7670.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3CFE5F00-040C-EA11-BAEC-FA163E1C0945.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4429EB0E-E00D-EA11-864F-A4BF01287D43.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/86A930BC-3913-EA11-B2E6-6CC2173BC990.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/12FDBADE-3913-EA11-8539-001E67580724.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/14B38BBF-3913-EA11-82EE-141877410522.root']);