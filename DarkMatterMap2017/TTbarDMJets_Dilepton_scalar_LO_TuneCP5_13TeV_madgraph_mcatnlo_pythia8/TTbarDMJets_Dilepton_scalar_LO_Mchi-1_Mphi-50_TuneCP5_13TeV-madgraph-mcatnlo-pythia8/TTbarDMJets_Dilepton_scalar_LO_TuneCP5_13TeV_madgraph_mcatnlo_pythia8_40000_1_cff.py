import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:11313', '1:11496', '1:11502', '1:13217', '1:22021', '1:22026', '1:22027', '1:22351', '1:22308', '1:22516', '1:22526', '1:25445', '1:25812', '1:25904', '1:29083', '1:29096', '1:29167', '1:29168', '1:29331', '1:31066', '1:25810', '1:30775', '1:89396', '1:89496', '1:89501', '1:89520', '1:90847', '1:90838', '1:90843', '1:11033', '1:11528', '1:11549', '1:11550', '1:11658', '1:13126', '1:13182', '1:13670', '1:13779', '1:22030', '1:22198', '1:22221', '1:22365', '1:29309', '1:29529', '1:29751', '1:29753', '1:29997', '1:29700', '1:29702', '1:29722', '1:29723', '1:29731', '1:29745', '1:29746', '1:29748', '1:29758', '1:29760', '1:29773', '1:29854', '1:22624', '1:22641', '1:22652', '1:22673', '1:101928', '1:11893', '1:11901', '1:11903', '1:13385', '1:13519', '1:13471', '1:13527', '1:13541', '1:22670', '1:25346', '1:25404', '1:29027', '1:29396', '1:29397', '1:30526', '1:30548', '1:30923', '1:31783', '1:31785', '1:31788', '1:89194', '1:89441', '1:89453', '1:101171', '1:30763', '1:30770', '1:30793', '1:31018', '1:31553', '1:31556', '1:101141', '1:101632', '1:22514', '1:22715', '1:90867', '1:90943', '1:101836', '1:29685', '1:30009', '1:30012', '1:30013', '1:31078', '1:90066', '1:101178', '1:101629', '1:30685', '1:22845', '1:22853', '1:22856', '1:22823', '1:25019', '1:25027', '1:25045', '1:25053', '1:25107', '1:22879', '1:22948', '1:30739', '1:30742', '1:30758', '1:22882', '1:25021', '1:25038', '1:25044', '1:25062', '1:25734', '1:25767', '1:25768', '1:25782', '1:25798', '1:25909', '1:25807', '1:25967', '1:31737', '1:101183', '1:31253', '1:30216', '1:30220', '1:30225', '1:31770', '1:30206', '1:31097', '1:31334', '1:30057', '1:30265', '1:30288', '1:30318', '1:31488', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/EA250210-B311-EA11-8313-0CC47AFF0264.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/4ABB45F0-2C10-EA11-8C52-0CC47AFB7D60.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/04CFEB6A-9810-EA11-9B8C-00266CFFC76C.root']);