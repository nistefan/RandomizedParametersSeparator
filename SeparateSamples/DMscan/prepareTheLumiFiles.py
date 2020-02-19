#!/usr/bin/env python
__author__ = 'Nicole Stefanov'
__date__ = 2020/02/08

import os
import sys
import subprocess

pathArray =[]
ThisDirectory = os.listdir(".")

print(ThisDirectory)

for item_ThisDirectory in ThisDirectory:
    if "Roadmap" in item_ThisDirectory:
        pathArray.append(item_ThisDirectory)
print(pathArray)

#For testing
#sys.exit()

## For manual setting of pathArray, without '/'
#pathArray =['Roadmap_TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV_madgraph_mcatnlo_pythia8',
#            'Roadmap_TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV_madgraph_mcatnlo_pythia8',
            #'Roadmap_TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV_madgraph_mcatnlo_pythia8',
            #'Roadmap_TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV_madgraph_mcatnlo_pythia8' 
#]

i=1
for path in pathArray:
    CreateNewDirectory = path[8:]
    print(CreateNewDirectory)
    if not os.path.exists(CreateNewDirectory):
        os.makedirs(CreateNewDirectory)
    getSubdirectory = []
    subdirectory = os.listdir(path)
    print(subdirectory)
    
    print("This is subdirectory "+str(i))
    for item_subdirectory in subdirectory:
        print(item_subdirectory)
        absolutePath_item_subdirectory = path+"/"+str(item_subdirectory)
        print(absolutePath_item_subdirectory)
        if os.path.isdir(absolutePath_item_subdirectory):
            getSubdirectoriesFiles = os.listdir(absolutePath_item_subdirectory)
            matchPy = [ ]
            matchPy = [ f for f in getSubdirectoriesFiles if ".py" in f]
            print(matchPy)
            matchPy = matchPy[0]
            for item_getSubdirectoriesFiles in getSubdirectoriesFiles:
                if "Events" not in item_getSubdirectoriesFiles and "Getting" not in item_getSubdirectoriesFiles and ".py" not in item_getSubdirectoriesFiles:
                    absolutePath_item_getSubdirectoriesFiles = absolutePath_item_subdirectory+"/"+item_getSubdirectoriesFiles
                    print(item_getSubdirectoriesFiles)
                    print(absolutePath_item_getSubdirectoriesFiles)
                    if not os.path.exists(CreateNewDirectory+"/"+item_getSubdirectoriesFiles[:-8]):
                         os.makedirs(CreateNewDirectory+"/"+item_getSubdirectoriesFiles[:-8])
                    print(item_getSubdirectoriesFiles[:-8])
#                    if ".py" not in item_getSubdirectoriesFiles:
                    if not os.path.exists(CreateNewDirectory+"/"+item_getSubdirectoriesFiles[:-8]):
                             os.makedirs(CreateNewDirectory+"/"+item_getSubdirectoriesFiles[:-8]) 
                    with open(absolutePath_item_getSubdirectoriesFiles, 'r') as lumis:
                            getlumis = lumis.read().replace('\n', '')
                            #print(getlumis)
                    print(CreateNewDirectory)
                    print(item_getSubdirectoriesFiles[:-8])
                    print(matchPy)
                    ToCopy = "cp "+absolutePath_item_subdirectory+"/"+matchPy+" "+CreateNewDirectory+"/"+item_getSubdirectoriesFiles[:-8]+"/"+matchPy
                    print(ToCopy)
                    subprocess.Popen([ToCopy], shell=True,
                                         stdout=subprocess.PIPE).communicate()[0]
                    whatToReplace1 ='sed -i "s/# //g" '+CreateNewDirectory+'/'+item_getSubdirectoriesFiles[:-8]+'/'+matchPy
                    whatToReplace2 ='sed -i "s/YOUR_LUMIBLOCKS/*('+getlumis+')/g" '+CreateNewDirectory+'/'+item_getSubdirectoriesFiles[:-8]+'/'+matchPy
#                        print(whatToReplace1)
#                        print(whatToReplace2)
                    subprocess.Popen([whatToReplace1], shell=True,
                                         stdout=subprocess.PIPE).communicate()[0]
                    subprocess.Popen([whatToReplace2], shell=True,
                                         stdout=subprocess.PIPE).communicate()[0]
# For testing
#    sys.exit() 
    i+=1
