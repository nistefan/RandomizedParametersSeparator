import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:1110', '1:1202', '1:1824', '1:16694', '1:19597', '1:54275', '1:17565', '1:28570', '1:98722', '1:97188', '1:43225', '1:51419', '1:54334', '1:64744', '1:51367', '1:67095', '1:78445', '1:102880', '1:102970', '1:104971', '1:84440', '1:28617', '1:57871', '1:79594', '1:59560', '1:61104', '1:95201', '1:83617', '1:98339', '1:86540', '1:88007', '1:19704', '1:54276', '1:39277', '1:55521', '1:53650', '1:52343', '1:52464', '1:52536', '1:53435', '1:61957', '1:61917', '1:62025', '1:62428', '1:61412', '1:61692', '1:66028', '1:66153', '1:12933', '1:14422', '1:16705', '1:95987', '1:94285', '1:52915', '1:59205', '1:59729', '1:60343', '1:58787', '1:61378', '1:58926', '1:67342', '1:67188', '1:45421', '1:22230', '1:41951', '1:59087', '1:59708', '1:64141', '1:71465', '1:43844', '1:51325', '1:52358', '1:52333', '1:53379', '1:53738', '1:60040', '1:71421', '1:90453', '1:96703', '1:97505', '1:88115', '1:82188', '1:86862', '1:101800', '1:81605', '1:81619', '1:81004', '1:56310', '1:54062', '1:54492', '1:64197', '1:72621', '1:73037', '1:76572', '1:65907', '1:71737', '1:72732', '1:82871', '1:93844', '1:97556', '1:101060', '1:101074', '1:101228', '1:102178', '1:103646', '1:103688', '1:103818', '1:103829', '1:105967', '1:105768', '1:106033', '1:105789', '1:55415', '1:59373', '1:59378', '1:71652', '1:71919', '1:71992', '1:72455', '1:67148', '1:71595', '1:97363', '1:97480', '1:95378', '1:88931', '1:95982', '1:95834', '1:101519', '1:105745', '1:88536', '1:91500', '1:94359', '1:98608', '1:102172', '1:77231', '1:105120', '1:104843', '1:80169', '1:80265', '1:80518', '1:19304', '1:23206', '1:26771', '1:30725', '1:75888', '1:81389', '1:43989', '1:25517', '1:23050', '1:26697', '1:27965', '1:30649', '1:39347', '1:30776', '1:44386', '1:29626', '1:47761', '1:53165', '1:56992', '1:76906', '1:76778', '1:79456', '1:80219', '1:15529', '1:16738', '1:70996', '1:89767', '1:81892', '1:77589', '1:81294', '1:84247', '1:89638', '1:91719', '1:84953', '1:78035', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CC916E5A-F8FE-E911-BC5C-3417EBE70078.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/261A750B-1502-EA11-A901-0026B9278651.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0DE8F81-AD03-EA11-895A-A0369FD0B142.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A23C784C-A502-EA11-A4FB-00259074AE52.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A6DE693B-2902-EA11-A934-AC1F6B0DE228.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/80593C2E-A502-EA11-A430-20CF3027A5F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/20F14403-9A02-EA11-9EF6-D48564599C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A6DC8DA6-9F03-EA11-A25B-CCC5E5F02BFB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B84232C7-D102-EA11-8D9E-A0369FC51EDC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/EC333E44-8703-EA11-9B66-0242AC1C0506.root']);