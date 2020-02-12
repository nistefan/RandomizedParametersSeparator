import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:92569', '1:92574', '1:92862', '1:93087', '1:93097', '1:93274', '1:92961', '1:93120', '1:93202', '1:93223', '1:93232', '1:93280', '1:93284', '1:93362', '1:93369', '1:93489', '1:93054', '1:93372', '1:92983', '1:92984', '1:12385', '1:12387', '1:11588', '1:11408', '1:11428', '1:11436', '1:11440', '1:11457', '1:11763', '1:11868', '1:12211', '1:12964', '1:12977', '1:47623', '1:47632', '1:41514', '1:42710', '1:45824', '1:44640', '1:66535', '1:84228', '1:84427', '1:12308', '1:11340', '1:11767', '1:42264', '1:42090', '1:41241', '1:41244', '1:41691', '1:82087', '1:65840', '1:83924', '1:83432', '1:83931', '1:11147', '1:11634', '1:11662', '1:11666', '1:12408', '1:42297', '1:42675', '1:44771', '1:44772', '1:48199', '1:66634', '1:84272', '1:41101', '1:47245', '1:42283', '1:42871', '1:42926', '1:11259', '1:47277', '1:12969', '1:41330', '1:47335', '1:47342', '1:47469', '1:44962', '1:65151', '1:48930', '1:48275', '1:66574', '1:43904', '1:43940', '1:43960', '1:43730', '1:45179', '1:66521', '1:45409', '1:48457', '1:65686', '1:65098', '1:45241', '1:66106', '1:11124', '1:11654', '1:12016', '1:12673', '1:12681', '1:44527', '1:47775', '1:43043', '1:43167', '1:43692', '1:45312', '1:42965', '1:41834', '1:41855', '1:42797', '1:42804', '1:93699', '1:45254', '1:48688', '1:45975', '1:48235', '1:48348', '1:48900', '1:65808', '1:65820', '1:66097', '1:82541', '1:43316', '1:66441', '1:66809', '1:66890', '1:82196', '1:65921', '1:65950', '1:11090', '1:11028', '1:42923', '1:42061', '1:42942', '1:42928', '1:41088', '1:41580', '1:41114', '1:41136', '1:47184', '1:43508', '1:44179', '1:93193', '1:12727', '1:12739', '1:12775', '1:12836', '1:42818', '1:42826', '1:45590', '1:45598', '1:45606', '1:45611', '1:45612', '1:45639', '1:84252', '1:84258', '1:84328', '1:84842', '1:84844', '1:82291', '1:82988', '1:83152', '1:83097', '1:83122', '1:66806', '1:84874', '1:92133', '1:93472', '1:93485', '1:93779', '1:93796', '1:93842', '1:92093', '1:92108', '1:66869', '1:83646', '1:83465', '1:83468', '1:66116', '1:83113', '1:83609', '1:83688', '1:83732', '1:83757', '1:82434', '1:66270', '1:82765', '1:82339', '1:83918', '1:83922', '1:83813', '1:84492', '1:92120', '1:84377', '1:84785', '1:84875', '1:12725', '1:12731', '1:12755', '1:12967', '1:12992', '1:12734', '1:47444', '1:47487', '1:92977', '1:93227', '1:65081', '1:65612', '1:92386', '1:92668', '1:92501', '1:92831', '1:92832', '1:92546', '1:92777', '1:92897', '1:92854', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/CCB0C45C-6510-EA11-8402-0025905C53D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/6E48CFB0-B414-EA11-B703-003048F316A6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/8493BC83-B911-EA11-968F-485B397717C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/D0111189-740F-EA11-A3A6-D094662CEC35.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/2E27578F-4F10-EA11-AEBA-0025905C42A2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/7A36FBD8-C811-EA11-9087-7CD30ACE142C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/56A7F3B9-3A10-EA11-A2BE-0025905C42A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/C6C92169-6714-EA11-B417-90B11C443C96.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/28CECBEA-7E10-EA11-9B7F-0CC47AFF02D0.root']);