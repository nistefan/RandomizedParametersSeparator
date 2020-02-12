import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:61513', '1:61859', '1:63053', '1:80078', '1:80270', '1:91229', '1:92169', '1:66687', '1:66862', '1:66887', '1:66794', '1:66891', '1:66993', '1:69572', '1:77155', '1:77179', '1:77107', '1:77257', '1:77346', '1:77384', '1:77395', '1:77411', '1:88297', '1:88306', '1:88631', '1:88648', '1:88766', '1:94272', '1:24027', '1:20390', '1:26998', '1:27599', '1:32669', '1:35466', '1:37710', '1:104537', '1:104603', '1:52203', '1:52639', '1:98808', '1:99657', '1:99259', '1:99285', '1:99418', '1:99466', '1:99488', '1:102724', '1:102769', '1:4223', '1:46580', '1:46633', '1:46696', '1:64633', '1:73333', '1:73562', '1:74689', '1:93214', '1:93242', '1:93191', '1:93231', '1:92944', '1:4313', '1:4337', '1:4348', '1:4846', '1:4863', '1:4886', '1:18542', '1:18550', '1:18725', '1:18768', '1:19089', '1:24586', '1:98074', '1:98195', '1:1704', '1:1780', '1:2109', '1:4018', '1:4756', '1:2318', '1:4672', '1:9678', '1:5231', '1:10014', '1:12034', '1:10330', '1:16390', '1:35361', '1:38783', '1:87063', '1:20704', '1:19995', '1:20993', '1:55038', '1:55804', '1:55890', '1:45863', '1:46967', '1:43966', '1:45399', '1:71402', '1:92437', '1:92535', '1:92645', '1:92808', '1:91152', '1:14177', '1:14207', '1:12945', '1:12957', '1:12985', '1:14300', '1:14495', '1:14720', '1:39172', '1:50291', '1:49888', '1:83197', '1:83250', '1:83985', '1:83989', '1:60228', '1:60302', '1:62631', '1:67912', '1:68560', '1:69305', '1:69600', '1:64012', '1:64331', '1:69787', '1:97018', '1:97401', '1:97465', '1:97499', '1:97211', '1:97258', '1:97293', '1:97345', '1:97397', '1:97423', '1:97541', '1:332', '1:3208', '1:4309', '1:4374', '1:4567', '1:12066', '1:12077', '1:12112', '1:12116', '1:12193', '1:12199', '1:12557', '1:56945', '1:97491', '1:97552', '1:97732', '1:34007', '1:34165', '1:75072', '1:74364', '1:74247', '1:74319', '1:74373', '1:74472', '1:74486', '1:74384', '1:74499', '1:74605', '1:74644', '1:105271', '1:105334', '1:105355', '1:39574', '1:48867', '1:49246', '1:49283', '1:50108', '1:83362', '1:83526', '1:83572', '1:83583', '1:83737', '1:83794', '1:103450', '1:103607', '1:103610', '1:45478', '1:49281', '1:51664', '1:52814', '1:53123', '1:53293', '1:55579', '1:55589', '1:55755', '1:55820', '1:57352', '1:79060', '1:79085', '1:79199', '1:79238', '1:79496', '1:79748', '1:79263', '1:79312', '1:103415', '1:1634', '1:1570', '1:1625', '1:1759', '1:4164', '1:9717', '1:9806', '1:9821', '1:9901', '1:10408', '1:10436', '1:10446', '1:9797', '1:9810', '1:9834', '1:10567', '1:10599', '1:10613', '1:10700', '1:10716', '1:12297', '1:41674', '1:49170', '1:38708', '1:10619', '1:10603', '1:10689', '1:10717', '1:12648', '1:12713', '1:48724', '1:41813', '1:48092', '1:51884', '1:54264', '1:54635', '1:54651', '1:54703', '1:54723', '1:54768', '1:104212', '1:104293', '1:104663', '1:104681', '1:102839', '1:104239', '1:141', '1:1916', '1:4747', '1:2110', '1:3049', '1:8657', '1:59498', '1:60826', '1:67767', '1:55328', '1:81995', '1:84014', '1:84171', '1:100108', '1:10007', '1:15575', '1:16820', '1:16918', '1:16966', '1:37363', '1:19432', '1:21267', '1:21136', '1:21773', '1:27580', '1:27595', '1:28455', '1:43139', '1:69848', '1:74626', '1:81994', '1:14100', '1:14234', '1:16557', '1:16198', '1:17063', '1:66276', '1:64815', '1:65287', '1:65887', '1:74758', '1:71223', '1:71242', '1:71283', '1:71382', '1:71474', '1:93235', '1:68733', '1:69366', '1:62901', '1:103079', '1:80206', '1:80393', '1:81888', '1:81904', '1:79017', '1:79045', '1:79155', '1:79523', '1:79588', '1:97799', '1:91370', '1:91871', '1:92218', '1:93356', '1:71027', '1:71059', '1:71552', '1:57080', '1:57084', '1:57173', '1:91185', '1:91217', '1:91312', '1:91379', '1:91384', '1:91658', '1:91779', '1:91784', '1:91928', '1:4565', '1:3010', '1:3444', '1:3744', '1:47861', '1:43993', '1:45221', '1:74822', '1:8993', '1:10226', '1:10284', '1:12600', '1:18111', '1:20025', '1:98466', '1:99651', '1:72565', '1:72797', '1:92124', '1:93073', '1:97385', '1:97517', '1:99121', '1:93019', '1:93860', '1:100849', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C2B2B4A5-90FA-E911-A1ED-FA163E596216.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/44AD8F54-33FC-E911-BFC1-44A842CFD5D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BC0C7A45-B3FB-E911-9A20-0025905C53AA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/18D4DE3D-06FB-E911-9D07-0CC47A4DEE78.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D60A6FA0-CCFC-E911-BDAF-0CC47A5FC679.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BCA2AA4C-68FB-E911-A22D-001CC4A6CCE6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/68A10C47-6CFF-E911-A5E7-0242AC1C0507.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70D242A1-7FFF-E911-934F-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C045F616-49FE-E911-9BA5-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FAD01C50-69FF-E911-BBD7-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/BE2BDBAA-1F02-EA11-9F99-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/84EBD031-DAFE-E911-A032-002590DE39F0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9AE2976D-2503-EA11-916D-0025905C53DC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A8BF48D7-28FF-E911-86D4-AC1F6BC67D46.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8A44B795-0403-EA11-B303-0CC47AFF014C.root']);