import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, lumisToProcess = cms.untracked.VLuminosityBlockRange('1:6666', '1:1994', '1:3571', '1:3709', '1:3868', '1:3878', '1:3981', '1:3983', '1:3997', '1:4326', '1:4349', '1:20051', '1:20090', '1:20117', '1:20227', '1:20232', '1:34427', '1:34488', '1:34520', '1:34656', '1:18409', '1:18494', '1:18650', '1:18712', '1:32980', '1:32988', '1:33372', '1:45808', '1:45981', '1:48052', '1:48079'),) #lumisToProcess = cms.untracked.VLuminosityBlockRange('1:2708', '1:61575'),)
readFiles.extend( ['/store/user/nstefano/FE6FA136-5A19-EA11-88F8-FA163E1FBD42.root', '/store/user/nstefano/7E010F67-5A19-EA11-9E48-C45444922B77.root', '/store/user/nstefano/282DD46C-49F3-E911-BCB2-0CC47AFC3C76.root']);



