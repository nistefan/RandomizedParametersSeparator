import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:9402', '1:5350', '1:31373', '1:2645', '1:3109', '1:3066', '1:2300', '1:803', '1:819', '1:836', '1:907', '1:909', '1:9909', '1:9912', '1:1546', '1:3098', '1:2176', '1:9880', '1:9819', '1:9837', '1:9919', '1:27174', '1:27932', '1:27626', '1:27853', '1:27870', '1:27942', '1:29711', '1:29852', '1:30204', '1:30289', '1:30322', '1:36100', '1:37021', '1:1181', '1:4367', '1:25662', '1:27059', '1:27168', '1:27951', '1:27854', '1:25899', '1:25902', '1:30655', '1:30922', '1:3418', '1:4342', '1:1200', '1:1206', '1:33264', '1:20993', '1:11182', '1:11108', '1:20895', '1:20919', '1:20920', '1:20957', '1:20973', '1:11719', '1:11654', '1:11637', '1:11639', '1:13016', '1:7162', '1:7130', '1:7726', '1:10508', '1:9583', '1:10937', '1:10172', '1:10175', '1:25857', '1:19685', '1:25967', '1:25977', '1:30709', '1:32574', '1:32563', '1:27934', '1:27941', '1:32023', '1:29100', '1:29121', '1:29142', '1:29975', '1:31762', '1:4442', '1:27610', '1:27987', '1:25297', '1:25349', '1:23470', '1:23450', '1:23465', '1:23897', '1:23953', '1:25752', '1:25756', '1:26823', '1:35092', '1:25701', '1:25702', '1:25825', '1:27292', '1:25443', '1:35019', '1:27464', '1:27468', '1:25802', '1:34081', '1:34095', '1:34103', '1:850', '1:33963', '1:33979', '1:32820', '1:32822', '1:32898', '1:32728', '1:32839', '1:32759', '1:33889', '1:35393', '1:3445', '1:6761', '1:7027', '1:1674', '1:1740', '1:9276', '1:26001', '1:26590', '1:28695', '1:28803', '1:27095', '1:27742', '1:25888', '1:4977', '1:29759', '1:28772', '1:2312', '1:1539', '1:5271', '1:14400', '1:25921', '1:30104', '1:32140', '1:25198', '1:27209', '1:27219', '1:27581', '1:27585', '1:32033', '1:6703', '1:7105', '1:12495', '1:12605', '1:12041', '1:23192', '1:23073', '1:23635', '1:21604', '1:21734', '1:21764', '1:22093', '1:21748', '1:21821', '1:21828', '1:24009', '1:22122', '1:21752', '1:12319', '1:22814', '1:17816', '1:12583', '1:12699', '1:12761', '1:12797', '1:12494', '1:13587', '1:17182', '1:17814', '1:12714', '1:18105', '1:18112', '1:18135', '1:15291', '1:18159', '1:19195', '1:22356', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/88AF5F29-0A17-EA11-A681-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/1EEC8579-5217-EA11-BA02-506B4BB16ADE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/F63A221A-4818-EA11-9A9A-24BE05CEED81.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/FA2C66CA-D518-EA11-B1F3-782BCB3BCA77.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/704ECD71-3617-EA11-A365-24BE05C656A1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/8AFB2568-3318-EA11-8096-0CC47A13CD9C.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E020F01A-9617-EA11-8CF7-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/EC947F03-4E17-EA11-A23D-EC0D9A8221CE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2A02A4C1-B418-EA11-B7C7-6C2B5999349F.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/829E2B4B-F018-EA11-8997-FA163E5F372F.root']);