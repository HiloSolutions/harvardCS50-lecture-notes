#include <cs50.h>
#include <stdio.h>

int main(void)
{
  string name = get_string("What's your name?");
  printf("hello, %s\n", name);
}

int get_negative_int(void);

int main(void)
{
  int i - get_negative_int();
  printf("%i\n", i);
}

int get_negative_int(void)
{
  int n;
  do
  {
    n = get_int("Negative Integer: ");
  } while (n < 0);
  return n;
}

/* Instead of declaring a separate variable for each value*/

int main(void)
{
  int socre1 = get_int("Score: ");
  int socre2 = get_int("Score: ");
  int socre3 = get_int("Score: ");

  printf("Average: %f\n", (score1 + score2 + score3)) / (float)3;
}

/* We could do this and declare one variable and index the values part of that variable */

int main(void)
{
  int scores[3];
  scores[0] = get_int("Score: ");
  scores[1] = get_int("Score: ");
  scores[2] = get_int("Score: ");
  printf("Average: %f\n", (scores[0] + scores[1] + scores[3])) / (float);
}

/*we can design this array creation better using a loop*/

int main(void)
{
  int scores[3];
  for (int i = 0; i < 3; i++)
  {
    scores[i] = get_int("Score: ");
  }
  printf("Average: %f\n", (scores[0] + scores[1] + scores[3])) / (float);
}

/*we call this loop in more than one place by assigning it to a functionp*/
const int N = 3;

float average(int array[]);

int main(void)
{
  int scores[N];
  for (int i = 0; i < N; i++)
  {
    scores[i] = get_int("Score: ");
  }
  printf("Average: %f\n", average(N, scores));
}

float average(int length, int array[])
{
  sum = 0;
  for (int i = 0; i < length; i++) {
    sum  += array[i];
  }
  return sum / (float) length;
}


