import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:41362', '1:41564', '1:41694', '1:41757', '1:41524', '1:45778', '1:45370', '1:45787', '1:45811', '1:45836', '1:82977', '1:66747', '1:83549', '1:84035', '1:83223', '1:83591', '1:82958', '1:66887', '1:82370', '1:82866', '1:82391', '1:83851', '1:84016', '1:84387', '1:92488', '1:92173', '1:84425', '1:92195', '1:44055', '1:44146', '1:47250', '1:43075', '1:44051', '1:43218', '1:43231', '1:43472', '1:43968', '1:47291', '1:47542', '1:48383', '1:48621', '1:48313', '1:65221', '1:66274', '1:66541', '1:66179', '1:82598', '1:66289', '1:66529', '1:66095', '1:66214', '1:66840', '1:82609', '1:66438', '1:66444', '1:82761', '1:83383', '1:66859', '1:82628', '1:82526', '1:12399', '1:12444', '1:12511', '1:44551', '1:48010', '1:48081', '1:48075', '1:65368', '1:83199', '1:83502', '1:12857', '1:42241', '1:48699', '1:48972', '1:84405', '1:93433', '1:93328', '1:93327', '1:83310', '1:93125', '1:93132', '1:11087', '1:11808', '1:11842', '1:11827', '1:11843', '1:84385', '1:84450', '1:84512', '1:84173', '1:84703', '1:84751', '1:84606', '1:92225', '1:92769', '1:92770', '1:12121', '1:11875', '1:11987', '1:12034', '1:42155', '1:48207', '1:48964', '1:65595', '1:66387', '1:84916', '1:93333', '1:84689', '1:92256', '1:93273', '1:65241', '1:65246', '1:83486', '1:43226', '1:43493', '1:43589', '1:43865', '1:43956', '1:45904', '1:48261', '1:65946', '1:66637', '1:82474', '1:83018', '1:84557', '1:84394', '1:92247', '1:41246', '1:44540', '1:44580', '1:44630', '1:43228', '1:48525', '1:65691', '1:44609', '1:45293', '1:45299', '1:45545', '1:66030', '1:82092', '1:83605', '1:48396', '1:43221', '1:45536', '1:45361', '1:48968', '1:44969', '1:44976', '1:45088', '1:45270', '1:93986', '1:12612', '1:12694', '1:12700', '1:12919', '1:42081', '1:42997', '1:47032', '1:47045', '1:47194', '1:41378', '1:43207', '1:48763', '1:65235', '1:43890', '1:82044', '1:82792', '1:83183', '1:82420', '1:83103', '1:83673', '1:83135', '1:83672', '1:42486', '1:42506', '1:42580', '1:47013', '1:42315', '1:42780', '1:65011', '1:65332', '1:65577', '1:93518', '1:93520', '1:93739', '1:93831', '1:47211', '1:44537', '1:44533', '1:47519', '1:43524', '1:44530', '1:93017', '1:84579', '1:84597', '1:84616', '1:92321', '1:92371', '1:11015', '1:11030', '1:11635', '1:12277', '1:41303', '1:42986', '1:43776', '1:43788', '1:43585', '1:45574', '1:48074', '1:45383', '1:65108', '1:48715', '1:48816', '1:12482', '1:12520', '1:12561', '1:12456', '1:12551', '1:42165', '1:43017', '1:47086', '1:47129', '1:44201', '1:47852', '1:45559', '1:44315', '1:47893', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/8026A6CC-9F0F-EA11-9BCD-3CFDFE63A880.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/CA0868E4-580F-EA11-A73F-14187751C030.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/F6C25D2B-6C10-EA11-A3AB-AC1F6B567680.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/82300CEE-C311-EA11-A7D4-0CC47AFCC4BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/DE988EEC-0111-EA11-B2B7-00269E95B0A4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/24390700-9E11-EA11-ACCD-6C2B5990D0B3.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/88C8B414-8510-EA11-8999-A4BF0108B89A.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/84DA2C2E-B80B-EA11-9ED3-EC0D9A8225FE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/7C848483-8210-EA11-9901-0CC47A7E69D8.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/40000/AA6F0C5B-8710-EA11-8112-00266CFFBF64.root']);