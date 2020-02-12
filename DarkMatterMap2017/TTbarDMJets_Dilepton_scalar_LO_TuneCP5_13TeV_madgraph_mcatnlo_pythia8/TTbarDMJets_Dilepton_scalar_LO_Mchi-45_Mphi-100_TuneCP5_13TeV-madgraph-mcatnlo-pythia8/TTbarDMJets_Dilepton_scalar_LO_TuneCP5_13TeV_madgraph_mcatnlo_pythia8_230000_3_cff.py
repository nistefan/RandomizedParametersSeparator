import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:19583', '1:19659', '1:19725', '1:19771', '1:19866', '1:19943', '1:34500', '1:34515', '1:34548', '1:34806', '1:36382', '1:36493', '1:36509', '1:36516', '1:33196', '1:28498', '1:28597', '1:28619', '1:28621', '1:28637', '1:28721', '1:28724', '1:28850', '1:33364', '1:33540', '1:33572', '1:33693', '1:33836', '1:33939', '1:33575', '1:34676', '1:43096', '1:45481', '1:96801', '1:97284', '1:104495', '1:16457', '1:16593', '1:88765', '1:88811', '1:91038', '1:91284', '1:88244', '1:88391', '1:45263', '1:40415', '1:50433', '1:50564', '1:50595', '1:50611', '1:51210', '1:58406', '1:58306', '1:87143', '1:87156', '1:87256', '1:88184', '1:88302', '1:88304', '1:1250', '1:1551', '1:1428', '1:1665', '1:3230', '1:3237', '1:3250', '1:3282', '1:3460', '1:3465', '1:28811', '1:28966', '1:44120', '1:44200', '1:19188', '1:19354', '1:19372', '1:21146', '1:18091', '1:19275', '1:19343', '1:27743', '1:70292', '1:70415', '1:71880', '1:66630', '1:67010', '1:71907', '1:73249', '1:75437', '1:72280', '1:72479', '1:74788', '1:75901', '1:65664', '1:64959', '1:70126', '1:70328', '1:70941', '1:71132', '1:66390', '1:99032', '1:100471', '1:100473', '1:98989', '1:75655', '1:96125', '1:20422', '1:27036', '1:27099', '1:24451', '1:26813', '1:28166', '1:28818', '1:28875', '1:28948', '1:21989', '1:27413', '1:27708', '1:71734', '1:72462', '1:75417', '1:73980', '1:72726', '1:71660', '1:82269', '1:82340', '1:82165', '1:82290', '1:82432', '1:82436', '1:82464', '1:82588', '1:87798', '1:100329', '1:95663', '1:96718', '1:93708', '1:93775', '1:93875', '1:93892', '1:93664', '1:93918', '1:41411', '1:52976', '1:55794', '1:56110', '1:81281', '1:91241', '1:91307', '1:91381', '1:91540', '1:91566', '1:91593', '1:92537', '1:92655', '1:92658', '1:92775', '1:92970', '1:100802', '1:100879', '1:102653', '1:96123', '1:99665', '1:99587', '1:100145', '1:100150', '1:100264', '1:100140', '1:106296', '1:106340', '1:64770', '1:72424', '1:73112', '1:73526', '1:73580', '1:95313', '1:95377', '1:95617', '1:99266', '1:99274', '1:104229', '1:104230', '1:104237', '1:105826', '1:105933', '1:106193', '1:105871', '1:105912', '1:106245', '1:50098', '1:50350', '1:50759', '1:50851', '1:63257', '1:63960', '1:64158', '1:64187', '1:64192', '1:64225', '1:96229', '1:96440', '1:62676', '1:62697', '1:62706', '1:62943', '1:62641', '1:63197', '1:72917', '1:74935', '1:81701', '1:82132', '1:82135', '1:96333', '1:97298', '1:100075', '1:100305', '1:67493', '1:67678', '1:67923', '1:67656', '1:67792', '1:67811', '1:84491', '1:83833', '1:83896', '1:84048', '1:84529', '1:85152', '1:85155', '1:94497', '1:94529', '1:94918', '1:100074', '1:100091', '1:20845', '1:20987', '1:24725', '1:52368', '1:52406', '1:52734', '1:53060', '1:53165', '1:53306', '1:55908', '1:55910', '1:57313', '1:78937', '1:80043', '1:80021', '1:39333', '1:39691', '1:40801', '1:40789', '1:40803', '1:40864', '1:58999', '1:76639', '1:76642', '1:76875', '1:76961', '1:76720', '1:99839', '1:100441', '1:100601', '1:100604', '1:78791', '1:78846', '1:36326', '1:36574', '1:38623', '1:38340', '1:38767', '1:42031', '1:42148', '1:37251', '1:49858', '1:50004', '1:50102', '1:50366', '1:50723', '1:52389', '1:97036', '1:97621', '1:88690', '1:104413', '1:104447', '1:12538', '1:20292', '1:20360', '1:20760', '1:62058', '1:62241', '1:62329', '1:62344', '1:62278', '1:62357', '1:64366', '1:64382', '1:64438', '1:64483', '1:64495', '1:64589', '1:81556', '1:81673', '1:81193', '1:65643', '1:65699', '1:98843', '1:68079', '1:68420', '1:70781', '1:91435', '1:94099', '1:18261', '1:20045', '1:21151', '1:52307', '1:57211', '1:69554', '1:65278', '1:76327', '1:79038', '1:79789', '1:82840', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/147D2FEE-7AF4-E911-AC32-FA163ED45046.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F8D1CA51-35F3-E911-A13A-7CD30AD09C64.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/408D623C-B5F2-E911-BEF8-FA163EEBFC01.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B49C1D82-4EF3-E911-9E50-842B2B6AEA0E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D4E56313-21F4-E911-B492-1866DA7F9419.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/94284CBD-36F4-E911-88E6-A4BF012835C2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6AB8635C-CDF5-E911-B092-FA163EF38280.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/42C14BE8-BDF6-E911-95B1-AC1F6B56768A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7602BEA4-33F6-E911-95A7-FA163EB69FE7.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B87F77FB-EAF6-E911-A351-0090FAA57A00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E27EC42F-BBF9-E911-9830-B083FED429D5.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/38B76DAF-36F9-E911-9F0F-001F29089F68.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/B02AB0B8-ADFA-E911-BDE6-44A842CFD667.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/92B1133B-96FA-E911-99FE-FA163E3BEC96.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C990481-CCF8-E911-B595-008CFAE45404.root']);