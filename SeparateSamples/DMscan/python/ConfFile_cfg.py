import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList
process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/nfs/dust/cms/user/stefanon/DM_Sample_Production/SeparateDMsamples/CMSSW_9_4_15/src/FE6FA136-5A19-EA11-88F8-FA163E1FBD42.root'
        #'file:myfile.root'
    ),
#    lumisToProcess = cms.untracked.VLuminosityBlockRange(provideLumiNumber)          
    #lumisToProcess = cms.untracked.VLuminosityBlockRange('1:2708', '1:61575'),
   # lumisToSkip = cms.untracked.VLuminosityBlockRange('1:1-1:3'),
#    process.source.lumisToProcess.extend("2708")
#    lumisToProcess = cms.untracked.VLuminosityBlockRange(["2708": [1, 2]]),
)

process.myProducerLabel = cms.EDProducer('DMscan'
)


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
    
)

#process.out.outputCommands = cms.untracked.vstring(    "keep *",    "drop *_*_*_HLT",    "keep FEDRawDataCollection_*_*_*")

#### This shall produce  our lumi .txt file,
#### the associated created root file is meant to be deleted directly afterwards, so let's make that .root file as light as possible:

process.out.outputCommands = cms.untracked.vstring("drop *")
process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
