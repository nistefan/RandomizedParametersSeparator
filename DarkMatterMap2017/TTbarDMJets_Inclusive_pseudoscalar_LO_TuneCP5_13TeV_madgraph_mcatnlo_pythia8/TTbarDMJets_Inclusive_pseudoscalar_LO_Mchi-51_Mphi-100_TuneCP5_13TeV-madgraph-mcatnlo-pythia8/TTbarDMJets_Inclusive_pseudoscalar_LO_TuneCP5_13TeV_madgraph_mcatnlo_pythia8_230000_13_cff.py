import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:24093', '1:27003', '1:29507', '1:58201', '1:58313', '1:58511', '1:58730', '1:59040', '1:59163', '1:62763', '1:62764', '1:62771', '1:62808', '1:83282', '1:13908', '1:15312', '1:40757', '1:47638', '1:47971', '1:46286', '1:19839', '1:24032', '1:20191', '1:20407', '1:20573', '1:20808', '1:48587', '1:48799', '1:49529', '1:64445', '1:91250', '1:32120', '1:78762', '1:79326', '1:80527', '1:94367', '1:94740', '1:94781', '1:94837', '1:94967', '1:95317', '1:95349', '1:95439', '1:95601', '1:75184', '1:79401', '1:80757', '1:81195', '1:83196', '1:83768', '1:70002', '1:92722', '1:93233', '1:93370', '1:93388', '1:103031', '1:98642', '1:103074', '1:103219', '1:7521', '1:7740', '1:7878', '1:8271', '1:13892', '1:46237', '1:46241', '1:46857', '1:20126', '1:20127', '1:20357', '1:20360', '1:17183', '1:23523', '1:23587', '1:21407', '1:21673', '1:21968', '1:23108', '1:23820', '1:15182', '1:15320', '1:18008', '1:18010', '1:18044', '1:27953', '1:27986', '1:28224', '1:30974', '1:76625', '1:84051', '1:85491', '1:85642', '1:85707', '1:88878', '1:91337', '1:91441', '1:91705', '1:92830', '1:55739', '1:55996', '1:56216', '1:56217', '1:64076', '1:64222', '1:64710', '1:75464', '1:76471', '1:76893', '1:76956', '1:56523', '1:56593', '1:56702', '1:56720', '1:56889', '1:56956', '1:57052', '1:76746', '1:76806', '1:80372', '1:75634', '1:76795', '1:76973', '1:79723', '1:49626', '1:96524', '1:96924', '1:98435', '1:101310', '1:101391', '1:87155', '1:88437', '1:88671', '1:97212', '1:87585', '1:87661', '1:87708', '1:88010', '1:11874', '1:12264', '1:41972', '1:44258', '1:46265', '1:46375', '1:46598', '1:46606', '1:19455', '1:19574', '1:19578', '1:19644', '1:19653', '1:19669', '1:19732', '1:19737', '1:26484', '1:26527', '1:26472', '1:43639', '1:52766', '1:52823', '1:52935', '1:11195', '1:14750', '1:15093', '1:15264', '1:20738', '1:62629', '1:74175', '1:71054', '1:74159', '1:73563', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/96B475A8-45F7-E911-A1D4-002590E7D7E2.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/4056591E-F209-EA11-A699-44A842CFD5BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/006C1B93-29F3-E911-9D2E-6C2B598FF86B.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/9E90CC6C-9A07-EA11-9BAF-0CC47A7C3432.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/463016DD-5DFC-E911-A3BD-0CC47AFCC69E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/FCD2DC78-350F-EA11-A934-509A4C9F8A8E.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/36068975-BBFA-E911-8ED3-509A4C9EF923.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C6AA3D6D-A7FB-E911-B199-40F2E9C6ADBA.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/C4F880FC-64FC-E911-9F1D-0CC47AFF0188.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/72568A99-5504-EA11-9A4E-14187764311A.root']);