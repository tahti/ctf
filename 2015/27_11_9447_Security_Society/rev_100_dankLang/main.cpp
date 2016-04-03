#include <iostream>
#include <cstring>
#include <cmath>
#include <sys/resource.h>
#include "InfInt.h"
constexpr int64_t MAX = 13379447l;
InfInt doot[MAX];
InfInt dootT[MAX];

bool failD[MAX + 2];
int64_t br[MAX + 2];

void fill_doot() {
  int64_t i = 0;
  for(i = 0; i <MAX; i++){
    doot[i] = i;
  }
  dootT[0] = 0;
  std::cerr<<"."<<std::endl;
  for(i = 1; i <MAX; i++){
    dootT[i] = dootT[i - 1] + doot[i - 1] ;
  }

  doot[0] = 0;
  doot[1] = 0;
  std::cerr<<"."<<std::endl;
  for(i = 2; i <MAX; i++){
    doot[i] = doot[i - 1] + dootT[i - 1];
  }

  dootT[0] = 0;
  dootT[1] = 0;
  dootT[2] = 0;
  std::cerr<<"."<<std::endl;
  for(i = 3; i <MAX; i++){
    dootT[i] = dootT[i - 1] + doot[i - 1];
  }

  doot[0] = 0;
  doot[1] = 0;
  doot[2] = 0;
  doot[3] = 0;
  std::cerr<<"+"<<std::endl;
  for(i = 4; i <MAX; i++){
    doot[i] = doot[i - 1] + dootT[i - 1];
  }
  std::cerr<<"*"<<std::endl;
}


void FillFail() {
  int64_t i = 2;
  std::fill_n(failD, MAX + 1, true);
  int64_t uB = (int64_t)sqrt((double)(MAX + 1)) + 1;
  memset(failD, 1, sizeof(bool) * (MAX + 1));
  for (int64_t i= 2; i < MAX + 1; i++){
    if (failD[i]) {
      for (int64_t k = i * i; k <= MAX + 1; k += i) {
        failD[k] = false;
      }
    }
  }
}


void FillBr() {
  int64_t memes = MAX;
  const int64_t U = 987654321l;
  br[0] = 0;
  br[1] = 1;
  br[2] = 1;
  int64_t i = 3;
  while (i < memes) {
    br[i] = (br[i-1] + br[i-2]) % U;
    i++;
  }
}

struct test {


InfInt epicfail(int64_t memes) {  // 13379447
  InfInt wow = 0;
  if (memes > 1) {
    if(failD[memes]) {
      wow = bill(memes - 1) + 1;
    } else {
      wow = such(memes - 1);
    }
  }

  return wow;
}

InfInt bill(int64_t memes) {
  InfInt wew;
  //std::cout<<"bill  memes:"<<memes<<std::endl;
  InfInt wow = br[memes];
  if ((wow % 3) == 0) {
    wew = such(memes - 1);
    wow++;
  }
  else {
    wew = epicfail(memes - 1);
  }
  wow = wew + wow;
  return wow;
}

InfInt such(int64_t memes) {
  InfInt wew = doot[memes];
  InfInt wow = wew;
  if ((wow % 7) == 0) {
    wew = bill(memes - 1);
    wow = wow + 1;
  } else {
    wew = epicfail(memes - 1);
  }
  wow = wew + wow;
  return wow;
}

};

int main() {
  test t;
  fill_doot();
  FillFail();
  FillBr();
  const rlim_t kStackSize = 16*16 * 16 * MAX;   // min stack size = 16 MB
  struct rlimit rl;
  int64_t result = getrlimit(RLIMIT_STACK, &rl);
  std::cout<<result<<std::endl;
  if (result == 0) {
    if (rl.rlim_cur < kStackSize) {
      rl.rlim_cur = kStackSize;
      result = setrlimit(RLIMIT_STACK, &rl);
      if (result != 0) {
          fprintf(stderr, "setrlimit returned result = %d\n", result);
      }
    }
  }
  int64_t memes = 13379447;
  InfInt wew  = t.epicfail(memes);
  std::cout<<wew.toString()<<std::endl;
  //return (int)wew;
  return 0; 
  /*>thank mr skeltal*/
}

