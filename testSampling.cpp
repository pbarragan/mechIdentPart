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

Eigen::VectorXd sampleParticle(){
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
  //std::cout << x << std::endl;
  //std::cout << x[0] << std::endl;
  //std::cout << x(0) << std::endl;
  return x;
}

int main(){
  srand((unsigned)time(NULL));
  //std::cout << rand() << std::endl;
  std::vector<Eigen::VectorXd> samples;
  for (size_t i=0;i<100;i++){
    samples.push_back(sampleParticle());
    //std::cout << std::endl;  
  }
  // calc mean
  Eigen::VectorXd mu = VectorXd::Zero(size);
  Eigen::MatrixXd Cov = MatrixXd::Zero(size,size);

  for (size_t i=0;i<samples.size();i++){
    mu += samples[i];
  }
  mu /= samples.size();

  for (size_t i=0;i<samples.size();i++){
    cov += (samples[i]-mu)*(samples[i]-mu).transpose();
  }

  cov /= samples.size();

  std::cout << mu << std::endl;
  std::cout << cov << std::endl;

  return 1;
}
