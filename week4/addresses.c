#include <stdio.h>


// base case
void base(int n)
{
  printf("Base: %i\n", n);
}


// prints the pointer/address
void pointer(int n)
{
  int *p = &n; //assigning address of n to variable in p.
  printf("Pointer: %p\n", p);
}


// goes to the address
go(int n)
{
  int *p = &n;
  printf("Go: %i\n", *p); // just n
}


// call the functions on the page
int main(void)
{
  int n = 50;
  base(n);
  pointer(n);
  go(n);
  return 0;
}