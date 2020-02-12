import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:7420', '1:7669', '1:7541', '1:49880', '1:49902', '1:49911', '1:49424', '1:49539', '1:49561', '1:49610', '1:49700', '1:68679', '1:72563', '1:72573', '1:91237', '1:91222', '1:91269', '1:94994', '1:96583', '1:96611', '1:97273', '1:97348', '1:97351', '1:102343', '1:25407', '1:29641', '1:33668', '1:30224', '1:30671', '1:39054', '1:89616', '1:76761', '1:76798', '1:78766', '1:78881', '1:78963', '1:78306', '1:81297', '1:97519', '1:98206', '1:98772', '1:77279', '1:80328', '1:77700', '1:94088', '1:99692', '1:95469', '1:95703', '1:100068', '1:17371', '1:17904', '1:56662', '1:79680', '1:85789', '1:49922', '1:59553', '1:90634', '1:24440', '1:24178', '1:46230', '1:52741', '1:61440', '1:69095', '1:94195', '1:10347', '1:17661', '1:14771', '1:20601', '1:36235', '1:57968', '1:38037', '1:27746', '1:31492', '1:32243', '1:46756', '1:23950', '1:46566', '1:91871', '1:99531', '1:37405', '1:37428', '1:7103', '1:18749', '1:18845', '1:27063', '1:30328', '1:31261', '1:32152', '1:34773', '1:35551', '1:97569', '1:100283', '1:91326', '1:99356', '1:99494', '1:5863', '1:5832', '1:5927', '1:22451', '1:22526', '1:8163', '1:36226', '1:36254', '1:37919', '1:81156', '1:37883', '1:37886', '1:37713', '1:37724', '1:39788', '1:57852', '1:60324', '1:76187', '1:94636', '1:19208', '1:22960', '1:13541', '1:95998', '1:56280', '1:58272', '1:58324', '1:60052', '1:60332', '1:88803', '1:89793', '1:89971', '1:91492', '1:89587', '1:91556', '1:18874', '1:20253', '1:20322', '1:21451', '1:21813', '1:22363', '1:75528', '1:70721', '1:70932', '1:71950', '1:72349', '1:72897', '1:95265', '1:95389', '1:101428', '1:21929', '1:34934', '1:39461', '1:27410', '1:28299', '1:70294', '1:70400', '1:70627', '1:71181', '1:71186', '1:71290', '1:71790', '1:76629', '1:76130', '1:21913', '1:25827', '1:35385', '1:37383', '1:38066', '1:39481', '1:37771', '1:46089', '1:31663', '1:56959', '1:79607', '1:79875', '1:86795', '1:88096', '1:74961', '1:89199', '1:70046', '1:70842', '1:78301', '1:72331', '1:77998', '1:78028', '1:79526', '1:95625', '1:50622', '1:64590', '1:64717', '1:64792', '1:64850', '1:64874', '1:76145', '1:76146', '1:76583', '1:76684', '1:52217', '1:51122', '1:52847', '1:51114', '1:51632', '1:61901', '1:63048', '1:63927', '1:71019', '1:72108', '1:72119', '1:76727', '1:9838', '1:14240', '1:21444', '1:4356', '1:6682', '1:7326', '1:7804', '1:6968', '1:8646', '1:9642', '1:19971', '1:87682', '1:89191', '1:90258', '1:99069', '1:49136', '1:52369', '1:57907', '1:56137', '1:68504', '1:75131', '1:69871', '1:73619', '1:73822', '1:74036', '1:75731', '1:74558', '1:74969', '1:75169', '1:75534', '1:76105', '1:76602', '1:52213', '1:59354', '1:89406', '1:89509', '1:89969', '1:87618', '1:80255', '1:85101', '1:86083', '1:88732', '1:91562', '1:101775', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E0D04434-29FD-E911-8A06-0CC47AF971DE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4E2F140C-670A-EA11-AF1D-AC1F6BAC8038.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B2C42B47-1A0B-EA11-8F90-0025905B8600.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4EA482F8-20FE-E911-B746-0CC47AF9B2B6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92731751-11FE-E911-8809-0CC47AFF02E4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/08535ED4-70F7-E911-BD73-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/AC2DA7CD-1E0B-EA11-804C-AC1F6BAC7F24.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/70D87FC9-120B-EA11-946F-0CC47A4C8E26.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AAA24F3-4FFC-E911-AC32-00215A491956.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D24779ED-140B-EA11-B78B-0025905B858A.root']);