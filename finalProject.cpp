#include <iostream>
#include <time.h>
using namespace std;
#include "checkInput.h"

//prototypes
int fib1(int pos);
int fib2(int pos);

int main() {
  int pos;
  clock_t start,end;
  int fibNum1,fibNum2;
  cout << "Enter a position: ";
  pos = getData(0,46,"Invalid input. Please enter a position between 0 and 46.");
  //recursive function
  start = clock();//start timing
  fibNum1 = fib1(pos);
  end = clock();//stop timing
  cout << "Recursive Elapsed time: " << (end-start) / double(CLOCKS_PER_SEC) * 1000 << " milliseconds" << endl;
  //non-recursive
  start = clock();//start timing
  fibNum2 = fib2(pos);
  end = clock();//stop timing
  cout << "Non-Recursive Elapsed time: " << (end-start) / double(CLOCKS_PER_SEC) * 1000 << " milliseconds" << endl;
  cout << "Fibonacci number at position " << pos << " is " << fibNum1 << endl;
  return 0;
}
//recursive function
int fib1(int pos)
{
  if(pos <= 1){
    return pos;
  }else{
    return fib1(pos-2) + fib1(pos-1);
  }
}
//non-recursive solution with O(n)
int fib2(int pos)
{
  int n1 = 0;
  int n2 = 1;
  int temp = 0;

  if(pos == 0){
    return 0;
  }
  for(int i = 2; i <= pos;i++)
  {
    temp = n1 + n2;
    n1 = n2;
    n2 = temp;
  }
  return n2;
}
