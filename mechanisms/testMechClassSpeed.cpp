#include <iostream>

#include "mechanism.h"
#include "mechFree.h"
#include "mechFixed.h"
#include "mechRev.h"
#include "mechPris.h"
#include "mechRevPrisL.h"
#include "mechPrisPrisL.h"

//#include "../translator.h"
//#include "../setupUtils.h"
//#include "../logUtils.h"

#include "../stateStruct.h"
#include <time.h>

void printVect(std::vector<double> vect){
  for (size_t i=0; i<vect.size(); i++){
    std::cout << vect[i] << ",";
  }
  std::cout << std::endl;
}

double timeDiff(timespec& ts1, timespec& ts2){
  return (double) ts2.tv_sec - (double) ts1.tv_sec + ((double) ts2.tv_nsec - (double) ts1.tv_nsec)/1000000000; 
}

int main(){

  timespec ts1;
  timespec ts2;
      
  clock_gettime(CLOCK_REALTIME, &ts1); // get time before

  for(size_t i=0;i<1000;i++){
    // Primsmatic
    MechPris* pris = new MechPris();

    stateStruct prisState;
    prisState.model=3;
    prisState.params.push_back(0.1);
    prisState.params.push_back(0.0);
    prisState.params.push_back(0.7856);
    prisState.vars.push_back(0.0);
  
    std::vector<double> prisAction;
    prisAction.push_back(0.15);
    prisAction.push_back(0.05);

    stateStruct nextPrisState = pris->initAndSim(prisState,prisAction);
    delete pris;
  }

  clock_gettime(CLOCK_REALTIME, &ts2); // get time before

  std::cout << "Time:\n" << timeDiff(ts1,ts2) << std::endl;

  
  return 1;
}
