// -*- C++ -*-
//
// Package:    SeparateSamples/DMscan
// Class:      DMscan
// 
/**\class DMscan DMscan.cc SeparateSamples/DMscan/plugins/DMscan.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Nicole Stefanov
//         Created:  Sun, 02 Feb 2020 01:10:01 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"


#include <iostream>
#include <string>
#include <regex>
#include <fstream>
#include <sstream>
#include <unordered_map>

#include <boost/algorithm/string.hpp>


#include <FWCore/Framework/interface/Run.h>
#include <FWCore/Framework/interface/EDProducer.h>

#include <FWCore/Utilities/interface/InputTag.h>


#include <SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h>
#include <SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h>
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoProduct.h"


//
// class declaration
//

class DMscan : public edm::stream::EDProducer<> {
   public:
      explicit DMscan(const edm::ParameterSet&);
      ~DMscan();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginStream(edm::StreamID) override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endStream() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
     
      edm::EDGetTokenT<GenLumiInfoHeader> tok_genlumiheader_;
      
      //  edm::EDGetTokenT<GenLumiInfoProduct> tok_genlumiinfo_;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//
//  int i =0;
int countEventsInLumiblock = 1;
std::string GettingTotalSampleStructure = "GettingTotalSampleStructure_Sub.txt";
std::string GettingAllLumiBlocks = "GettingAllLumiBlocks_Sub.txt";

//
// static data member definitions
//

//
// constructors and destructor
//
DMscan::DMscan(const edm::ParameterSet& iConfig)
//: tag_GenLumiInfoHeader_(iConfig.getParameter<edm::InputTag>("GenLumiInfoHeader"))

  :  tok_genlumiheader_(consumes<GenLumiInfoHeader,edm::InLumi>(edm::InputTag("generator")))
     // tok_genlumiinfo_(consumes<GenLumiInfoProduct,edm::InLumi>(edm::InputTag("luminosity")))
{    
//genLumiHeaderToken_ = consumes<GenLumiInfoHeader,edm::InLumi>(tag_GenLumiInfoHeader_);
    //produces<GenLumiInfoHeader, edm::Transition::BeginLuminosityBlock>();
  //  produces<std::vector<double> >();

   //register your products
/* Examples
   produces<ExampleData2>();

   //if do put with a label
   produces<ExampleData2>("label");
 
   //if you want to put into the Run
   produces<ExampleData2,InRun>();
*/
   //now do what ever other initialization is needed
  
}


DMscan::~DMscan()
{
 
   // do anything here that needs to be done at destruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
DMscan::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
 using namespace edm;
 countEventsInLumiblock +=1;

/* This is an event example
   //Read 'ExampleData' from the Event
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);

   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event
   iEvent.put(std::make_unique<ExampleData2>(*pIn));
*/

/* this is an EventSetup example
   //Read SetupData from the SetupRecord in the EventSetup
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
*/
 
}

// ------------ method called once each stream before processing any runs, lumis or events  ------------
void
DMscan::beginStream(edm::StreamID)
{
}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void
DMscan::endStream() {
  std::ofstream AllFiles;
  AllFiles.open(GettingTotalSampleStructure, std::ios::app);
  AllFiles<<"\n\n";
  //       myfile<<model<<" "<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"\n";                                                                                                                      
  AllFiles.close();

}

// ------------ method called when starting to processes a run  ------------
/*
void
DMscan::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
DMscan::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------

void DMscan::beginLuminosityBlock(edm::LuminosityBlock const& iLumi, edm::EventSetup const& iEvent){
  
     edm::Handle<GenLumiInfoHeader> gen_header;
     iLumi.getByToken(tok_genlumiheader_, gen_header);  
     std::string model = gen_header->configDescription();
     //For testing ...
     //    std::cout<<"model is "<<model<<std::endl;


     //std::cout<<" i is "<<i<<std::endl;
     //i +=1;
     //edm::Handle<GenLumiInfoProduct> genLumiInfo;
     //iLumi.getByToken(tok_genlumiinfo_, genLumiInfo);

     //For testing ...  
     //     std::cout<<iLumi.luminosityBlock()<<std::endl;
     //std::cout<<iLumi.run()<<std::endl;
     countEventsInLumiblock = 0;
     //Some testing ...
     /*     if(model=="/TTbarDMJets_Dilepton_scalar_LO_Mchi-51_Mphi-100_TuneCP5_13TeV-madgraph-mcatnlo-pythia8"){
       std::cout<<"True \n";} 
     */
       std::ofstream myfile; 
       std::string whatFileToWriteIn = model.erase(0, 1); 
       //std::ifstream ifile;
       //ifile.open(whatFileToWritein);
       //if(ifile){
       //For testing
       //	 std::cout<<"found file "<<std::endl;
	 myfile.open(whatFileToWriteIn+"_Sub.txt", std::ios::app); 
	 myfile<<"'"<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"', ";
	 //       myfile<<model<<" "<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"\n";
	 myfile.close();

	 std::ofstream myfile1;

	 myfile1.open(whatFileToWriteIn+"Events_Sub.txt", std::ios::app);
         myfile1<<"['"<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"', ";
         //       myfile<<model<<" "<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"\n";                                                                       
         myfile1.close();

	 /*}
       else{
	 std::cout<<"couldn't find file "<<std::endl;
	 myfile.open(whatFileToWriteIn+".txt", std::ios::app);
         myfile<<"[ '"<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"', ";
         //       myfile<<model<<" "<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"\n";                                                                      
         myfile.close();
	 }*/
       //To check for dublicates; 
       std::ofstream AllFiles;
       AllFiles.open(GettingTotalSampleStructure, std::ios::app);
       AllFiles<<model<<" "<<"'"<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"', ";
       //       myfile<<model<<" "<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"\n";                                                               
       AllFiles.close();

       //     }
       std::ofstream AllLumi;
       AllLumi.open(GettingAllLumiBlocks, std::ios::app);
       AllLumi<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"\n";
       AllLumi.close();
   

  /*  edm::Handle<GenLumiInfoHeader> gen_header;
      iLumi.getByToken(genLumiHeaderToken_, gen_header);*/
  
       //std::cout<<"gen_header.configDescription()._M_current is \n"; //<<gen_header->configDescription()._M_current<<std::endl; 

}

 
// ------------ method called when ending the processing of a luminosity block  ------------

void
DMscan::endLuminosityBlock(edm::LuminosityBlock const& iLumi, edm::EventSetup const&)
{

  // For testing purposes ...
  edm::Handle<GenLumiInfoHeader> gen_header;
  iLumi.getByToken(tok_genlumiheader_, gen_header);
  std::string model = gen_header->configDescription();
  std::string whatFileToWriteIn = model.erase(0, 1);
  //std::cout<<"model is "<<model<<std::endl;
  //std::cout<<"countEventsInLumiblock is "<<countEventsInLumiblock<<std::endl;
  std::ofstream AllFiles;
  AllFiles.open(GettingTotalSampleStructure, std::ios::app);
  AllFiles<<" "<<countEventsInLumiblock<<"\n";
  //       myfile<<model<<" "<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"\n";                                                                 
  AllFiles.close();
  std::ofstream myfile1;

  myfile1.open(whatFileToWriteIn+"Events_Sub.txt", std::ios::app);
  myfile1<<", "<<countEventsInLumiblock<<"], ";
  //       myfile<<model<<" "<<iLumi.run()<<":"<<iLumi.luminosityBlock()<<"\n";                                                                      \
                                                                                                                                                           
  myfile1.close();


}

 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DMscan::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DMscan);
