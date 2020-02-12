import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:267', '1:280', '1:313', '1:341', '1:382', '1:423', '1:552', '1:575', '1:592', '1:3594', '1:18910', '1:19237', '1:50191', '1:24301', '1:98972', '1:103620', '1:103798', '1:103960', '1:19830', '1:103748', '1:103701', '1:103733', '1:46706', '1:46891', '1:46933', '1:47000', '1:48105', '1:48115', '1:48213', '1:50257', '1:53843', '1:80475', '1:80485', '1:80645', '1:9728', '1:23460', '1:16006', '1:76020', '1:76061', '1:14385', '1:15658', '1:15693', '1:17086', '1:18003', '1:18990', '1:27504', '1:27996', '1:32189', '1:28475', '1:19288', '1:77994', '1:63732', '1:67364', '1:64817', '1:68641', '1:73920', '1:74292', '1:74343', '1:65203', '1:70359', '1:71859', '1:72234', '1:31257', '1:31299', '1:30890', '1:51802', '1:47093', '1:46713', '1:56583', '1:57048', '1:61886', '1:67359', '1:69425', '1:69900', '1:73942', '1:31969', '1:32566', '1:32567', '1:32624', '1:75591', '1:55580', '1:62227', '1:62260', '1:62333', '1:81735', '1:77137', '1:77724', '1:2174', '1:2270', '1:2275', '1:2277', '1:3037', '1:881', '1:56856', '1:58727', '1:59766', '1:60057', '1:60097', '1:82554', '1:82746', '1:84795', '1:84819', '1:79745', '1:79731', '1:83262', '1:101648', '1:83673', '1:86228', '1:88708', '1:88289', '1:86147', '1:87794', '1:87075', '1:87299', '1:92087', '1:88838', '1:89224', '1:89236', '1:89211', '1:89430', '1:89551', '1:89425', '1:89538', '1:89552', '1:101850', '1:101853', '1:101804', '1:101823', '1:101830', '1:1578', '1:2816', '1:2879', '1:78040', '1:81379', '1:75051', '1:76100', '1:76227', '1:31179', '1:30684', '1:30741', '1:30746', '1:66622', '1:71325', '1:72369', '1:74419', '1:16363', '1:16740', '1:17548', '1:11066', '1:35303', '1:30055', '1:30492', '1:55356', '1:61083', '1:25333', '1:25184', '1:25263', '1:30634', '1:31081', '1:31102', '1:90979', '1:101633', '1:90011', '1:90283', '1:90216', '1:90218', '1:60205', '1:60792', '1:101449', '1:11252', '1:11254', '1:11284', '1:11383', '1:11663', '1:22189', '1:22585', '1:29694', '1:31047', '1:31191', '1:31210', '1:29979', '1:61976', '1:67167', '1:66094', '1:11544', '1:20049', '1:39050', '1:39119', '1:39068', '1:49270', '1:50736', '1:51942', '1:47246', '1:52993', '1:56883', '1:53924', '1:54165', '1:54772', '1:55634', '1:75062', '1:79070', '1:80719', '1:82419', '1:75913', '1:75914', '1:90074', '1:90459', '1:90504', '1:26553', '1:42655', '1:39141', '1:39143', '1:45774', '1:50779', '1:51278', '1:52790', '1:51539', '1:50050', '1:51479', '1:52013', '1:75426', '1:75826', '1:74740', '1:71566', '1:66868', '1:70722', '1:70984', '1:65435', '1:66953', '1:76207', '1:78842', '1:81129', '1:80287', '1:11260', '1:11303', '1:13224', '1:22751', '1:22808', '1:22814', '1:22831', '1:22846', '1:22855', '1:22926', '1:22886', '1:61946', '1:62454', '1:61500', '1:89428', '1:89071', '1:89073', '1:89084', '1:89141', '1:89610', '1:103137', '1:103133', '1:103135', '1:103204', '1:534', '1:3733', '1:4763', '1:12590', '1:12832', '1:15044', '1:99909', '1:102749', '1:103088', '1:105045', '1:93683', '1:25382', '1:25487', '1:31140', '1:24857', '1:30525', '1:89436', '1:89794', '1:25379', '1:21749', '1:21885', '1:25145', '1:25300', '1:24473', '1:32760', '1:33418', '1:33459', '1:31904', '1:31936', '1:31994', '1:32509', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E121475-8F16-EA11-8E04-A0369FE2C0B0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/30928809-BC17-EA11-BB9F-FA163EB84C2E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/4E9AEF96-7917-EA11-924F-FA163EFE3C83.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/3800FB9D-1118-EA11-AEEA-FA163E3C6BCA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/BA02D583-D717-EA11-8AB6-AC1F6B8DD1F8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6E962FC4-1218-EA11-A4E7-008CFA1983BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/18F8D4AE-5818-EA11-AC1B-002590DC0352.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/6CF856BA-FF16-EA11-9606-AC1F6B0DE2E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8EE12E36-9617-EA11-B775-FA163ED521CB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/54894913-D216-EA11-8F84-A0369FF88246.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1685CFE4-5118-EA11-95CB-003048F2E8C0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8AC2DDFC-8E17-EA11-A339-FA163E5AB700.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/386B181A-9017-EA11-A440-5065F3816251.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2A1CF336-1318-EA11-B91E-0242AC1C0500.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/48B048F8-9017-EA11-B603-FA163E7ED2D2.root']);