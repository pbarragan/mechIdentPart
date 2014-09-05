#include <vector>
#include <iostream> // DELETE
#define _USE_MATH_DEFINES
#include <math.h> // cos, sin
#include "../Eigen/Dense"
#include "logUtils.h"

////////////////////////////////////////////////////////////////////////////////
//                            Particle Section                                //
////////////////////////////////////////////////////////////////////////////////

// SAMPLING SECTION

using Eigen::MatrixXd;
using Eigen::VectorXd;

std::vector<double> standardGaussianVariates(){
  double x1 = ((double)rand()/(double)RAND_MAX);
  double x2 = ((double)rand()/(double)RAND_MAX);
  std::vector<double> variates;
  variates.push_back(sqrt(-2*logUtils::safe_log(x1))*cos(2*M_PI*x2));
  variates.push_back(sqrt(-2*logUtils::safe_log(x1))*sin(2*M_PI*x2));
  return variates;
}

void sampleParticle(){
  unsigned int size = 2;
  Eigen::MatrixXd Cov = MatrixXd::Zero(size,size);
  Eigen::VectorXd mu = VectorXd::Zero(size);
  for (size_t i=0; i<size; i++){
    Cov(i,i) = 0.1;
  }
  Eigen::MatrixXd A( Cov.llt().matrixL() );
  Eigen::VectorXd z = VectorXd::Zero(size);
  for (size_t i=0; i<size; i+=2){
    std::vector<double> variates = standardGaussianVariates();
    z[i] = variates[0];
    if (i != size-1) z[i+1] = variates[1];
  }
  Eigen::VectorXd x = mu+A*z;
  std::cout << x << std::endl;
}

int main(){
  srand((unsigned)time(NULL));
  //std::cout << rand() << std::endl;
  for (size_t i=0;i<30;i++){
    sampleParticle();
    std::cout << std::endl;  
  }
  return 1;
}
