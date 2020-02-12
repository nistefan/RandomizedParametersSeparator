import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:40284', '1:47845', '1:52844', '1:55184', '1:57105', '1:77576', '1:84799', '1:79008', '1:80223', '1:80300', '1:81037', '1:8517', '1:8616', '1:9141', '1:9310', '1:9611', '1:9636', '1:10774', '1:103616', '1:14117', '1:12947', '1:15948', '1:80401', '1:1012', '1:1210', '1:1217', '1:1563', '1:1580', '1:4557', '1:34728', '1:59863', '1:59931', '1:60146', '1:67269', '1:71102', '1:71144', '1:71148', '1:71248', '1:71373', '1:71532', '1:71564', '1:71556', '1:99071', '1:99225', '1:98021', '1:98062', '1:98139', '1:98171', '1:98213', '1:98264', '1:98272', '1:100845', '1:9537', '1:19897', '1:33545', '1:33938', '1:38606', '1:45053', '1:45489', '1:46081', '1:97108', '1:100227', '1:102400', '1:103276', '1:98555', '1:100268', '1:92911', '1:96296', '1:97123', '1:97932', '1:99161', '1:21114', '1:21231', '1:21320', '1:21325', '1:21377', '1:94296', '1:94307', '1:94337', '1:94387', '1:94486', '1:93249', '1:88470', '1:88471', '1:91120', '1:94007', '1:103461', '1:15609', '1:15647', '1:15664', '1:15711', '1:15712', '1:15781', '1:15941', '1:16724', '1:40460', '1:41507', '1:48340', '1:48478', '1:43335', '1:43456', '1:43493', '1:44162', '1:84861', '1:62593', '1:63284', '1:64142', '1:64145', '1:56024', '1:56037', '1:55985', '1:56370', '1:56388', '1:56933', '1:57009', '1:88495', '1:88975', '1:94124', '1:95700', '1:95807', '1:95862', '1:95900', '1:97864', '1:98822', '1:98919', '1:99000', '1:16009', '1:16096', '1:16166', '1:16319', '1:16522', '1:16980', '1:16998', '1:17301', '1:17493', '1:17623', '1:21572', '1:21683', '1:21765', '1:21481', '1:24039', '1:48082', '1:48114', '1:63193', '1:63327', '1:63648', '1:63674', '1:48446', '1:48448', '1:48514', '1:53598', '1:54429', '1:54549', '1:54557', '1:61334', '1:33904', '1:35205', '1:37916', '1:28157', '1:28974', '1:32568', '1:36995', '1:38451', '1:51209', '1:17031', '1:17035', '1:26152', '1:50898', '1:51120', '1:72875', '1:73355', '1:73490', '1:74000', '1:74581', '1:34909', '1:35863', '1:37069', '1:37368', '1:35636', '1:35892', '1:35908', '1:36270', '1:58019', '1:58107', '1:92713', '1:92885', '1:92893', '1:92971', '1:96106', '1:99351', '1:95510', '1:95542', '1:96279', '1:97442', '1:53195', '1:54065', '1:54441', '1:54467', '1:54482', '1:53183', '1:53239', '1:53781', '1:54102', '1:57088', '1:72362', '1:74687', '1:75242', '1:77264', '1:75729', '1:76340', '1:77676', '1:78031', '1:93996', '1:95446', '1:97034', '1:96272', '1:96465', '1:97072', '1:98975', '1:91109', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/D04FBF28-5110-EA11-9F76-0CC47A78A30E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/001D64CA-5310-EA11-96A2-FA163EAA9AA3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/627B982F-5410-EA11-A749-0242AC1C0505.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/8AEFEE41-5410-EA11-816C-002590550622.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E8A9BBBA-6410-EA11-AA7E-3417EBE644B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3033B37D-5B10-EA11-8A42-44A8422411EB.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/6CB7815A-6D10-EA11-B8E3-1458D04903A8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/E684B189-9811-EA11-ABDA-EC0D9A0B30D0.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/0CB37202-E310-EA11-992E-0242AC130002.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/5E63C437-7B12-EA11-B95B-002590207D00.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/003A79CB-B511-EA11-85AC-801844DEF068.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/34D10FD8-E5F5-E911-A5AB-FA163EDEF72A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F4956687-3FF3-E911-A4D7-0CC47AFC3C80.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/082F7BC8-A9FE-E911-88EE-7CD30AD08E8A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/F0100C7C-0CF7-E911-A60F-0242AC130002.root']);