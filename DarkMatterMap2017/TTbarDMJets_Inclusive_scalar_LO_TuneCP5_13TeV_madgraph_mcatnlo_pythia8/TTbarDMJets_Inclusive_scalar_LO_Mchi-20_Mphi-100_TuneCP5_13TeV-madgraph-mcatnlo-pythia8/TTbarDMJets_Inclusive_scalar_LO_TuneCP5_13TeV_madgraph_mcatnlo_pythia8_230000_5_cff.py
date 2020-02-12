import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:3766', '1:3889', '1:10236', '1:20487', '1:21909', '1:57210', '1:19553', '1:19699', '1:36711', '1:33605', '1:52272', '1:56363', '1:57607', '1:27309', '1:27346', '1:35346', '1:37092', '1:24861', '1:28981', '1:39224', '1:40509', '1:94212', '1:40965', '1:24215', '1:24996', '1:27183', '1:46263', '1:79511', '1:86282', '1:87843', '1:90752', '1:91204', '1:94963', '1:96032', '1:14870', '1:14941', '1:54761', '1:54866', '1:54950', '1:54980', '1:62322', '1:62371', '1:62509', '1:62563', '1:97297', '1:101141', '1:102185', '1:102514', '1:13272', '1:16163', '1:62195', '1:63428', '1:63650', '1:63668', '1:71512', '1:71868', '1:72350', '1:72942', '1:13769', '1:13396', '1:21615', '1:67529', '1:67590', '1:67728', '1:75319', '1:76090', '1:76853', '1:55039', '1:64925', '1:67338', '1:70155', '1:90807', '1:61278', '1:64364', '1:69615', '1:69655', '1:86101', '1:91467', '1:91860', '1:91977', '1:89735', '1:85274', '1:77757', '1:79070', '1:72186', '1:78845', '1:79367', '1:80155', '1:85875', '1:71875', '1:73260', '1:77019', '1:59227', '1:60213', '1:74151', '1:91160', '1:58059', '1:67418', '1:76543', '1:71211', '1:77194', '1:77448', '1:77664', '1:54195', '1:98339', '1:75946', '1:67636', '1:68782', '1:69334', '1:74983', '1:75778', '1:78861', '1:86294', '1:87316', '1:87841', '1:86488', '1:87456', '1:87968', '1:96055', '1:96734', '1:97638', '1:97654', '1:86396', '1:88763', '1:89506', '1:89748', '1:96398', '1:94528', '1:96495', '1:96988', '1:95785', '1:99513', '1:91513', '1:91584', '1:95604', '1:96057', '1:35830', '1:37222', '1:37251', '1:37322', '1:68191', '1:74585', '1:74970', '1:75255', '1:75847', '1:75988', '1:72627', '1:81020', '1:81274', '1:94006', '1:94421', '1:95343', '1:95507', '1:101458', '1:97259', '1:100567', '1:81481', '1:88907', '1:100243', '1:100676', '1:14430', '1:33059', '1:58551', '1:78520', '1:91242', '1:95245', '1:95315', '1:95068', '1:95399', '1:95433', '1:4690', '1:5697', '1:5786', '1:97877', '1:101922', '1:86000', '1:86476', '1:24721', '1:35837', '1:35917', '1:37460', '1:71631', '1:86336', '1:88905', '1:89291', '1:86707', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/663C015C-090B-EA11-BFB8-0CC47A4D761A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8C1F2C40-140B-EA11-B0C9-0CC47A4D76C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/50E09B46-0F0B-EA11-B430-0CC47A7C353E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/00B4F279-060B-EA11-B0D5-44A842CFD64D.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/42F08944-8A0B-EA11-81BC-0CC47A4D7670.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3CFE5F00-040C-EA11-BAEC-FA163E1C0945.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4429EB0E-E00D-EA11-864F-A4BF01287D43.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/86A930BC-3913-EA11-B2E6-6CC2173BC990.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/12FDBADE-3913-EA11-8539-001E67580724.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/14B38BBF-3913-EA11-82EE-141877410522.root']);