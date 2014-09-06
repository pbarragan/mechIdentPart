#include <vector>
#include <iostream> // DELETE
#define _USE_MATH_DEFINES
#include <math.h> // cos, sin


int main(){
  std::vector<double> testVec0 (5,2.0);
  std::vector<double> testVec1 (5,0.0);
  std::vector<double> testVec;
  testVec.insert(testVec.end(),testVec0.begin(),testVec0.end());
  testVec.insert(testVec.end(),testVec1.begin(),testVec1.end());

  for (size_t i=0;i<testVec.size();i++){
    testVec[i] *= 2;
  }
  //std::vector<double> testVec (10,0.0);
  //std::cout << testVec(testVec.begin(),testVec.begin()+5).size() << std::endl;
  std::vector<double> testVec2;
  testVec2.assign(testVec.begin(),testVec.begin()+5);
  std::cout << testVec2.size() << std::endl;
  for (size_t i=0;i<testVec.size();i++){
    std::cout << testVec[i] << std::endl;
  }
  std::cout << std::endl;
  for (size_t i=0;i<testVec2.size();i++){
    std::cout << testVec2[i] << std::endl;
  }
  std::cout << std::endl;

  testVec2[2] = 1.0;

  for (size_t i=0;i<testVec.size();i++){
    std::cout << testVec[i] << std::endl;
  }
  std::cout << std::endl;
  for (size_t i=0;i<testVec2.size();i++){
    std::cout << testVec2[i] << std::endl;
  }
  std::cout << std::endl;

  testVec2.assign(testVec.begin()+5,testVec.end());

  for (size_t i=0;i<testVec.size();i++){
    std::cout << testVec[i] << std::endl;
  }
  std::cout << std::endl;
  for (size_t i=0;i<testVec2.size();i++){
    std::cout << testVec2[i] << std::endl;
  }
  std::cout << std::endl;

  return 1;
}
