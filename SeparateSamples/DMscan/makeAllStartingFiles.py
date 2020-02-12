#!/usr/bin/env python
__author__ = 'Nicole Stefanov'
__date__ = 2020/02/05


import os
import sys
import subprocess



def sliceList(listName, NElements):
    '''Split the list, into sublists with max. NElements, each'''
    Tlength= len(listName)
    print("Tlength")
    print(Tlength)
    if NElements > Tlength:
        NElements = Tlength
    print("NElements ")
    print(NElements)
    assert 0 < NElements
    numberOfSlices = Tlength/NElements
    print("numberOfSlices")
    print(numberOfSlices)
  #  whatToreturn = []
    for part in range(0, Tlength, NElements):
        print(part)
        print(part)
        print("listName[part:part+NElements]")
        print(listName[part:part+NElements])
#1        whatToreturn.append(listName[part:part+NElements])
    return [listName[part:part+NElements] for part in range(0, Tlength, NElements)]
#    return whatToreturn #[listName[part:part+NElements] for part in range(0, Tlength, NElements)]

################# Example path names, change as needed
pathArray =[
    '/pnfs/desy.de/cms/tier2/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/',
    '/pnfs/desy.de/cms/tier2/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/',
    '/pnfs/desy.de/cms/tier2/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/',
    '/pnfs/desy.de/cms/tier2/store/mc/RunIIFall17MiniAODv2/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/'
]
##                                                                                                                                                          
## Now let's start the script run, looping over all directories provided in pathArray                                                                       
######################################################################################                                                                      
######################################################################################                                                                      

sliceSize = 10

for path in pathArray:

  files = []
  # r=root, d=directories, f = files  ### here root does not refer to .root-files
  for r, d, f in os.walk(path):
    for file in f:
        if '.root' in file:
            getfilepath = os.path.join(r, file).split("/pnfs/desy.de/cms/tier2")[1]
            files.append(getfilepath)

  ### This FileNumberInDirectory is split in packages of sliceSize defined above. 
  print("FileNumberInDirectory is "+str(len(files)))
#  print(files)
 
  getUmbrellaSampleName = path.split("/")[-4]
  #if len(files) >= 255:
#    list_subfolders_with_paths = [fg.path for fg in os.scandir(path) if fg.is_dir()]
  getsubdirectories = [x[0] for x in os.walk(path)]
  getsubdirectories.pop(0)
  print(getsubdirectories)
#    print(list_subfolders_with_paths)
     #sys.exit()
#  continue
  getAllcmsRunCommands = []
  for item_getsubdirectories in getsubdirectories:
    subfiles = []
    # r=root, d=directories, f = files  ### here root does not refer to .root-files
    for r_level, d_level, f_level in os.walk(item_getsubdirectories):
      for item_f_level in f_level:
        if '.root' in item_f_level:
            getfilepath = os.path.join(r_level, item_f_level).split("/pnfs/desy.de/cms/tier2")[1]
            subfiles.append(getfilepath)
#    print(subfiles)
    print("len(subfiles)")
    print(len(subfiles))
    #if(len(subfiles)>10):
     #   sliceSize = 10
    #else: sliceSize = len(subfiles)
    thislists = sliceList(subfiles, sliceSize)
    print("len(thislists)")
    print(len(thislists))
    i = 0
    for item_thislists in thislists:
        print("item_thislists")
        print(item_thislists)
        print("Got sublists of "+str(sliceSize))
#        continue
    #sys.exit()
        getsuffix = item_getsubdirectories.split("/")[-1]+"_"+str(i)
        getUmbrellaSampleNameMod = getUmbrellaSampleName + "_"+getsuffix
        getUmbrellaSampleNameMod = getUmbrellaSampleNameMod.replace("-", "_")
        getAllcmsRunCommands.append("cmsRun python/"+getUmbrellaSampleNameMod+"_cfg.py \n\n")
        with open("python/"+getUmbrellaSampleNameMod+'_cff.py', 'a')  as writeObj:
            writeObj.write("import FWCore.ParameterSet.Config as cms\n")
            writeObj.write("maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )\n")
            writeObj.write("readFiles = cms.untracked.vstring()\n")
            writeObj.write("source = cms.Source (\"PoolSource\",fileNames = readFiles, # lumisToProcess = cms.untracked.VLuminosityBlockRange(YOUR_LUMIBLOCKS)\n")
            writeObj.write(")\n")
            writeObj.write("readFiles.extend( ")
            writeObj.write(str(item_thislists)+");")
    
        with open("python/"+getUmbrellaSampleNameMod+'_cfg.py', 'a') as writeNextObj:
            writeNextObj.write("import FWCore.ParameterSet.Config as cms\n")
            writeNextObj.write("import FWCore.PythonUtilities.LumiList as LumiList\n")
            writeNextObj.write("import SeparateSamples.DMscan."+getUmbrellaSampleNameMod+"_cff\n\n")
            writeNextObj.write("process = cms.Process(\"OWNPARTICLES\")\n\n")
            writeNextObj.write("process.load(\"FWCore.MessageService.MessageLogger_cfi\")\n\n")
            writeNextObj.write("process.MessageLogger.cerr.FwkReport.reportEvery = 10000\n\n")
            writeNextObj.write("process.extend(SeparateSamples.DMscan."+getUmbrellaSampleNameMod+"_cff)\n\n")
            writeNextObj.write("process.myProducerLabel = cms.EDProducer('DMscan')\n\n\n")
            writeNextObj.write("process.out = cms.OutputModule(\"PoolOutputModule\",\n    fileName = cms.untracked.string('myOutputFile.root')\n\n)\n\n")
            writeNextObj.write("process.out.outputCommands = cms.untracked.vstring(\"drop *\")\nprocess.p = cms.Path(process.myProducerLabel)\n\nprocess.e = cms.EndPath(process.out)")
        i +=1
  with open(getUmbrellaSampleName+".sh", 'a') as writeShellFile:
      writeShellFile.write("#!/bin/bash\n\n")
      for item_getAllcmsRunCommands in getAllcmsRunCommands:
          giveDirectorySuffix = item_getAllcmsRunCommands.split("/")[1].split("_cfg.py")[0] #split("madgraph_mcatnlo_pythia8_")[1].split("_cfg.py")[0] 
          if not os.path.exists(giveDirectorySuffix):
              os.makedirs(giveDirectorySuffix)
          subprocess.Popen(["cp python/"+giveDirectorySuffix+"_cff.py"+" "+giveDirectorySuffix+"/." ], shell=True,
                          stdout=subprocess.PIPE).communicate()[0]
          writeShellFile.write(item_getAllcmsRunCommands)
#          writeShellFile.write("mkdir "+str(giveDirectorySuffix)+"\n \n")
          writeShellFile.write("mv *_Sub.txt "+str(giveDirectorySuffix)+"/. \n \n")
        
