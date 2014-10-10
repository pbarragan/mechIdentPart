#include "translator.h"
#include "logUtils.h"

//include mechanisms
#include "mechanisms/mechFree.h"
#include "mechanisms/mechFixed.h"
#include "mechanisms/mechRev.h"
#include "mechanisms/mechPris.h"
#include "mechanisms/mechRevPrisL.h"
#include "mechanisms/mechPrisPrisL.h"

#include <iostream> // DELETE

enum MechTypes
  {
    MECH_FREE,
    MECH_FIXED,
    MECH_REV,
    MECH_PRIS,
    MECH_REV_PRIS_L,
    MECH_PRIS_PRIS_L
  };

Mechanism* translator::createMechanism(int choice){
  Mechanism* mechPtr;
  switch(choice){
  case MECH_FREE:
    mechPtr = new MechFree();
    break;
  case MECH_FIXED:
    mechPtr = new MechFixed();
    break;
  case MECH_REV:
    mechPtr = new MechRev();
    break;
  case MECH_PRIS:
    mechPtr = new MechPris();
    break;
  case MECH_REV_PRIS_L:
    mechPtr = new MechRevPrisL();
    break;
  case MECH_PRIS_PRIS_L:
    mechPtr = new MechPrisPrisL();
    break;
  }
  return mechPtr;
}

// overloaded
stateStruct translator::stateTransition(stateStruct& state, std::vector<double>& action){
  // Go back to this
  /* 
  Mechanism* mechPtr = createMechanism(state.model);
  stateStruct nextState = mechPtr->initAndSim(state,action);
  delete mechPtr;
  return nextState;
  */
  // Just for now to speed things up
  stateStruct nextState = state;

  if (state.model == 0){
    // Perfect relative motion from current location
    nextState.vars[0] += action[0];
    nextState.vars[1] += action[1];
  }
  else if (state.model == 1){
    // Do nothing
  }
  else if (state.model == 2){
    // Calculate equilibrium point
    double x = action[0]+state.params[2]*cos(state.vars[0]);
    double y = action[1]+state.params[2]*sin(state.vars[0]);
    nextState.vars[0] = atan2(y,x);
    /*
      for (size_t j=0;j<state.params.size();j++){
      state.params[j] 
      //+= 0.01*(2*(actionSelection::randomDouble()-0.5));
      += RealWorld::gaussianNoise();
      }
    */
  }
  else if (state.model == 3){
    // Calculate equilibrium point
    nextState.vars[0] += action[0]*cos(state.params[2])
      +action[1]*sin(state.params[2]);
  }
  else{
    Mechanism* mechPtr = createMechanism(state.model);
    nextState = mechPtr->initAndSim(state,action);
    delete mechPtr;
  }	

  // THIS IS VERY TEMPORARY
  // add noise
  double sig = 0.001; // standard deviation of noise - it worked when it was 0.00001 - still worked with 0.01
  double mu = 0.0; // mean of noise
  for (size_t i=0;i<nextState.vars.size();i++){
    double x1 = ((double)rand()/(double)RAND_MAX);
    double x2 = ((double)rand()/(double)RAND_MAX);
    nextState.vars[i] += sqrt(-2*logUtils::safe_log(x1))*cos(2*M_PI*x2)*sig+mu;
  }

  return nextState;
}

// overloaded
stateStruct translator::stateTransition(stateStruct& state, std::vector<double>& action, sasUtils::mapPairSVS& sasList){
  stateStruct nextState = sasUtils::getFromSAS(sasList,state,action);
  // DELETE
  /*
  if (nextState.model == 4){
    MechRevPrisL mech;
    std::vector<double> hold = mech.stToRbt(nextState);
    std::cout << "model 4 r:" << nextState.params[2] << std::endl;
    std::cout << "model 4 d start:" << state.vars[1] << std::endl;
    std::cout << "model 4 d next:" << nextState.vars[1] << std::endl;
    std::cout << "action:" << action[0] << "," << action[1] << std::endl;
    std::cout << "model 4 in rbt:" << std::endl;
    std::cout << hold[0] << std::endl;
    std::cout << hold[1] << std::endl;
  }
  */
  return nextState;
}

std::vector<double> translator::translateStToObs(stateStruct& state){
  Mechanism* mechPtr = createMechanism(state.model);
  std::vector<double> stateInObs = mechPtr->stToObs(state);
  delete mechPtr;
  return stateInObs;
}

std::vector<double> translator::translateStToRbt(stateStruct& state){
  Mechanism* mechPtr = createMechanism(state.model);
  std::vector<double> stateInRbt = mechPtr->stToRbt(state);
  delete mechPtr;
  return stateInRbt;
}

std::vector<double> translator::translateSensToObs(std::vector<double>& obs){
  Mechanism* mechPtr = new Mechanism();
  std::vector<double> sensInObs = mechPtr->sensToObs(obs);
  delete mechPtr;
  return sensInObs;
}

bool translator::isStateValid(stateStruct& state,std::vector< std::vector<double> >& workspace){
  Mechanism* mechPtr = createMechanism(state.model);
  bool valid = mechPtr->isStateValid(state,workspace);
  delete mechPtr;
  return valid;
}
