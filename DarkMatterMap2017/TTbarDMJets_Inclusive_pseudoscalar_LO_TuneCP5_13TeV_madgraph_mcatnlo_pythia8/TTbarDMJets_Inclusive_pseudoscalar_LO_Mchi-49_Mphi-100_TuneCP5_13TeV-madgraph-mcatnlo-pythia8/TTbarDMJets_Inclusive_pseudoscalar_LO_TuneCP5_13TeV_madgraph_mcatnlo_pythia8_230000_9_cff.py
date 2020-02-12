import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:70249', '1:82164', '1:89355', '1:103968', '1:106213', '1:106434', '1:106333', '1:5831', '1:6954', '1:5846', '1:20096', '1:20196', '1:23653', '1:27497', '1:42747', '1:17258', '1:19054', '1:19658', '1:19942', '1:23688', '1:98677', '1:101010', '1:102771', '1:101313', '1:102258', '1:105605', '1:102281', '1:104636', '1:17644', '1:21361', '1:27263', '1:27561', '1:22221', '1:27440', '1:57027', '1:57603', '1:57873', '1:58535', '1:58572', '1:106039', '1:90048', '1:103832', '1:105013', '1:59709', '1:59961', '1:59986', '1:77717', '1:77774', '1:77948', '1:78943', '1:82312', '1:82467', '1:89230', '1:85866', '1:104102', '1:95162', '1:91416', '1:91535', '1:49772', '1:51389', '1:51484', '1:53118', '1:54073', '1:56974', '1:97837', '1:101006', '1:101023', '1:104630', '1:101266', '1:97141', '1:89677', '1:89785', '1:89937', '1:90917', '1:92063', '1:92182', '1:92192', '1:102469', '1:101884', '1:102818', '1:102995', '1:104407', '1:104899', '1:91358', '1:91570', '1:92675', '1:96804', '1:97893', '1:98136', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4227006D-BC12-EA11-89BE-24BE05CEEC21.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E4C1DE6F-BC12-EA11-AD6D-C0BFC0E56816.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/74A96878-BC12-EA11-8C73-0CC47AA989BC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5ECC5C62-BD12-EA11-BF3F-AC1F6B0DE2EC.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7851C772-BC12-EA11-BDB4-0025905504C6.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2AEF561-BD12-EA11-9091-AC1F6B595F6E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B4B1C46E-BD12-EA11-BFF6-BC305B390A80.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/CCAB0879-BC12-EA11-BA1C-3CFDFE63F4E0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6C681F0E-990A-EA11-9A16-0025905B85E8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1CC07437-950A-EA11-BF7B-0025905B85E8.root']);