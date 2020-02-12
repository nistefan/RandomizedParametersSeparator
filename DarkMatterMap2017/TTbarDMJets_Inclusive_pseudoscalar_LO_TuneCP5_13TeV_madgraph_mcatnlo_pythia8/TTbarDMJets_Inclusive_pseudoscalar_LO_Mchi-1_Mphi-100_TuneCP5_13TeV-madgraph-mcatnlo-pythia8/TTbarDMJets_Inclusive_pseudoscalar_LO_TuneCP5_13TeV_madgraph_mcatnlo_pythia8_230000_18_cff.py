import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange(*('1:70067', '1:70521', '1:70651', '1:75501', '1:77087', '1:77290', '1:77330', '1:77694', '1:78585', '1:70710', '1:77454', '1:82112', '1:82215', '1:82700', '1:85130', '1:71548', '1:72318', '1:71433', '1:71577', '1:71667', '1:73206', '1:73554', '1:75125', '1:75278', '1:75365', '1:81385', '1:80358', '1:80765', '1:79178', '1:80564', '1:80882', '1:75255', '1:89835', '1:90841', '1:91178', '1:4048', '1:4414', '1:4454', '1:4704', '1:4713', '1:5030', '1:5052', '1:5167', '1:5171', '1:5214', '1:5223', '1:5450', '1:5526', '1:5653', '1:19259', '1:32683', '1:32722', '1:32741', '1:32860', '1:32976', '1:32892', '1:39076', '1:39077', '1:39100', '1:39252', '1:101517', '1:101558', '1:101770', '1:101783', '1:101852', '1:101656', '1:101792', '1:5911', '1:6136', '1:6344', '1:6444', '1:6605', '1:6651', '1:6874', '1:6987', '1:7017', '1:7188', '1:7314', '1:25448', '1:25456', '1:25706', '1:25739', '1:25763', '1:25795', '1:25814', '1:25851', '1:25859', '1:25941', '1:25973', '1:26050', '1:26223', '1:26374', '1:26588', '1:26596', '1:25867', '1:25886', '1:25893', '1:25991', '1:26320', '1:31210', '1:31689', '1:39602', '1:40636', '1:41892', '1:48821', '1:54614', '1:61487', '1:61964', '1:80839', '1:78340', '1:104064', '1:24058', '1:25081', '1:25082', '1:24433', '1:74683', '1:74822', '1:74893', '1:74762', '1:74837', '1:74867', '1:74868', '1:74973', '1:75022', '1:75043', '1:75011', '1:75658', '1:39409', '1:42033', '1:42075', '1:42130', '1:42147', '1:42178', '1:42186', '1:42265', '1:42309', '1:42317', '1:42374', '1:42583', '1:42698', '1:42699', '1:40583', '1:59186', '1:59391', '1:59574', '1:59722', '1:59763', '1:59844', '1:59979', '1:59997', '1:60061', '1:60062', '1:60093', '1:60115', '1:60140', '1:60150', '1:75186', '1:75227', '1:75060', '1:75062', '1:75239', '1:75259', '1:76036', '1:74998', '1:75386', '1:5289', '1:14976', '1:3137', '1:4528', '1:15846', '1:9632', '1:11600', '1:16481', '1:82260', '1:84553', '1:85135', '1:85670', '1:85727', '1:93606', '1:82627', '1:86040', '1:91737', '1:91931', '1:92125', '1:80857', '1:81363', '1:81765', '1:81833', '1:81411', '1:81476', '1:81477', '1:81508', '1:81553', '1:81589', '1:81601', '1:81688', '1:80226', '1:81263', '1:81630', '1:81513', '1:81727', '1:81761', '1:29335', '1:29514', '1:32186', '1:39109', '1:42083', '1:17371', '1:17679', '1:19476', '1:27414', '1:28012', '1:28911', '1:29076', '1:19862', '1:17792', '1:18051', '1:17858', '1:21769', '1:23216', '1:17560', '1:19153', '1:19657', '1:17971', '1:27195', '1:27348', '1:27543', '1:92681', '1:98956', '1:87769', '1:90528', '1:90910', '1:93442', '1:93877', '1:95636', '1:95773', '1:95799', '1:96268', '1:88249', '1:89790', '1:89905', '1:91145', '1:56031', '1:61859', '1:62534', '1:82698', '1:85106', '1:85756', '1:86289', '1:86541', '1:86988', '1:90652', '1:91192', '1:91635', '1:45605', '1:45632', '1:45648', '1:45681', '1:45694', '1:45775', '1:45810', '1:45795', '1:45870', '1:45924', '1:45950', '1:45961', '1:97661', '1:97764', '1:97901', '1:98020', '1:98132', '1:98261', '1:98328', '1:98557', '1:51146', '1:51380', '1:67102', '1:84643', '1:87829', '1:88246', '1:52907', '1:52949', '1:54350', '1:54962', '1:55771', '1:57859', '1:62279', '1:62499', '1:64137', '1:64630', '1:51042', '1:52418', '1:52763', '1:53467', '1:54285', '1:54752', '1:56550', '1:56848', '1:61313', '1:55569', '1:65549', '1:67273', '1:72641', '1:73769', '1:75169', '1:75680', '1:66764', '1:67288', '1:71106', '1:72006', '1:72616', '1:73050', '1:74694', '1:3554', '1:3926', '1:4049', '1:4072', '1:3952', '1:3976', '1:4088', '1:4218', '1:4299', '1:4874', '1:4914', '1:4923', '1:5023', '1:4413', '1:4421', '1:4649', '1:20406', '1:20429', '1:20455', '1:20555', '1:20901', '1:20972', '1:21297', '1:21410', '1:21459', '1:30341', '1:30379', '1:30403', '1:30405', '1:30492', '1:30517', '1:30549', '1:30727', '1:30833', '1:30890', '1:30915', '1:30996', '1:32024', '1:32030', '1:55940', '1:8827', '1:9215', '1:9676', '1:9971', '1:10058', '1:10197', '1:10233', '1:10332', '1:10955', '1:10963', '1:46078', '1:46143', '1:46207', '1:46308', '1:46311', '1:46313', '1:46312', '1:46320', '1:46358', '1:46376', '1:46424', '1:46560', '1:48376', '1:48561', '1:48591', '1:48594', '1:48622', '1:48677', '1:48693', '1:48712', '1:48731', '1:48843', '1:54635', '1:54769', '1:54822', '1:54845', '1:54878', '1:54957', '1:55157', '1:55279', '1:55282', '1:55306', '1:55347', '1:55846', '1:55870', '1:55961', '1:55983', '1:2056', '1:2077', '1:2204', '1:2260', '1:2324', '1:2325', '1:2713', '1:2754', '1:2861', '1:3121', '1:3191', '1:20226', '1:20784', '1:20896', '1:17628', '1:17629', '1:17636', '1:17693', '1:17884', '1:29006', '1:29013', '1:29072', '1:29078', '1:21694', '1:21935', '1:21951', '1:23083', '1:23107', '1:23210', '1:25003', '1:24083', '1:27882', '1:28500', '1:28701', '1:29115', '1:29251', '1:29537', '1:29569', '1:29697', '1:29860', '1:29964', '1:29998', '1:30059', '1:30255', '1:49542', '1:30021', '1:30038', '1:30155', '1:30310', '1:30313', '1:30463', '1:30506', '1:30628', '1:32067', '1:32790', '1:52651', '1:52660', '1:52905', '1:52914', '1:52928', '1:52971', '1:53013', '1:53014', '1:60935', '1:60958', '1:61408', '1:57004', '1:3708', '1:14030', '1:14062', '1:14540', '1:15931', '1:16080', '1:16625', '1:16668', '1:16681', '1:16687', '1:15748', '1:62903', '1:81813', '1:1551', '1:1694', '1:1719', '1:1735', '1:1753', '1:1756', '1:1821', '1:1870', '1:1606', '1:1665', '1:1667', '1:1811', '1:1814', '1:1955', '1:2010', '1:7561', '1:17252', '1:17275', '1:17323', '1:17357', '1:17362', '1:17390', '1:17419', '1:17443', '1:17455', '1:17463', '1:17464', '1:17507', '1:17709', '1:17714', '1:17729', '1:17851', '1:39175', '1:26009', '1:26130', '1:26269', '1:26113', '1:26248', '1:26379', '1:6745', '1:8559', '1:8725', '1:8752', '1:8903', '1:8992', '1:9006', '1:9051', '1:9985', '1:10142', '1:10207', '1:10259', '1:10292', '1:8384', '1:6738', '1:6756', '1:6850', '1:7240', '1:8070', '1:8116', '1:8125', '1:8133', '1:8204', '1:8308', '1:8328', '1:8377', '1:9106', '1:9111', '1:9222', '1:9231', '1:27009', '1:25423', '1:16158', '1:16486', '1:16515', '1:24451', '1:24663', ))
)
readFiles.extend( ['/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1C7CCC2F-2BF0-E911-A9D8-24BE05C488E1.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/3C5331FC-79FB-E911-9DA3-A4BF01287D43.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/7268BD3C-EBF9-E911-9D94-002590DE6DD4.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/78A56FCD-8E02-EA11-AAE1-F4E9D4D1EA90.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A413599C-04F9-E911-B9F1-0025901D0C54.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/24B7C050-A40A-EA11-B9AD-0CC47A7C3444.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/620017DD-0BF3-E911-AD90-E4115BCE00BE.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/580EEBBB-69FC-E911-AF98-0CC47AFCC696.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/1AD16148-BC12-EA11-A03F-FA163E64B350.root', '/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/230000/A2B1F5FA-64FC-E911-B838-0CC47AFF0460.root']);