import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:8777', '1:18216', '1:18397', '1:23264', '1:20083', '1:957', '1:3180', '1:7980', '1:2902', '1:33758', '1:9961', '1:523', '1:18477', '1:18545', '1:19382', '1:19576', '1:20498', '1:20288', '1:20845', '1:38600', '1:37131', '1:37176', '1:37173', '1:8359', '1:8596', '1:81', '1:6869', '1:10451', '1:10472', '1:5659', '1:7274', '1:7452', '1:7927', '1:2121', '1:5164', '1:5165', '1:5172', '1:5515', '1:8915', '1:8916', '1:10442', '1:260', '1:37552', '1:29642', '1:30828', '1:3504', '1:3514', '1:5556', '1:5707', '1:6849', '1:1604', '1:31810', '1:33164', '1:7420', '1:25065', '1:25491', '1:5461', '1:5513', '1:10213', '1:10360', '1:14861', '1:15117', '1:10856', '1:28880', '1:25084', '1:27621', '1:35221', '1:35363', '1:35392', '1:35566', '1:237', '1:1735', '1:1763', '1:1776', '1:1810', '1:6807', '1:4571', '1:4605', '1:9810', '1:5495', '1:5496', '1:14563', '1:14759', '1:14796', '1:14883', '1:14912', '1:14913', '1:1603', '1:7033', '1:7122', '1:4886', '1:27111', '1:30750', '1:32329', '1:26917', '1:26924', '1:25887', '1:25708', '1:32137', '1:32547', '1:27623', '1:36027', '1:36262', '1:36263', '1:36888', '1:37420', '1:37115', '1:37311', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/023B2C6F-1C1A-EA11-BD6A-B496910A0554.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/848B39AC-B81A-EA11-AAF0-0CC47AFF249E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/EC96E3DC-9E18-EA11-9E23-0025905C42F4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/9ADE1793-B116-EA11-A425-1866DA85DC8B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/E2704869-2A17-EA11-9700-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2412ABD9-4B17-EA11-BDE5-0242AC1C0501.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/922E001D-4717-EA11-8BA3-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/2A6C0B95-6A18-EA11-A67F-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/48D42C93-3917-EA11-AF57-0242AC1C0502.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/260000/88D67FC8-8217-EA11-9DC9-0242AC1C0501.root']);