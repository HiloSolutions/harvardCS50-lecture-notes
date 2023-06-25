# Steps of Compiling
The compilation process in C transforms a human-readable code into a machine-readable format. For C programming language, it happens before a program starts executing to check the syntax and semantics of the code.

What happens when we run 
```
make
```

1. **Preprocessing (.c -> .i):** Converts #includes to something else.
2. **Compiling (.i -> .s):** Converts intermediate code to assebly code.
3. **Assembly (.s -> .o):** Converts compiled code to binary (machine code). There is a 1:1 relationship b/w assebled code and machine code.
4. **Linking (.o -> .out):** Combines everything together

## STEP 1: Preprocessing (.c -> .i)
Done by using the pre-processor tool (A pre-written program invoked by the system during the compilation).
* Comments are removed
* Hashes removed
* Macros Expansion
```
#include <cs50.h>
#include <stdio.h>

int main(void)
{
  string name = get_string("What's your name?");
  printf("hello, %s\n", name);
}
```


### Preprocessor Directive
**Hash (#):** a preprocessor directive. Anything with this symbol in front of it should be processed before anything else happens.
You can think of include lines as temporary placeholders for what will later be a global find and replace by the compiler.

```
get_string()
```
was not declared in the code example because it was declared in the **cs50.h** file.


### Function Prototype / Declaration
How a function is decreed to exist.

**Example 1**
```
string get_string(string prompt);
```
1. function name: **get_string**
2. arguments: **string prompt** a prompt that will receive a string of text.
3. return value: will be a **string**

**Example 2**
```
int printf(string format, ...);
```
1. function name: *printf**
2. argument1: **string format** Takes a string that you will want to format.
3. argument2: **...** You can plug in some number of variables
4. return value: will be a **number** although programmer tends to not look at this.


## STEP 2: Compiling (.i -> .s)
Intermediate file to assembly file
The whole program code is parsed (syntax analysis) by the compiler software in one go, and it tells us about any syntax errors or warnings present in the source code through the terminal window.


## STEP 3: Assembling (.s -> .o)
Assembly level code (.s file) is converted into a machine-understandable code (in binary/hexadecimal form) using an assembler. 
Assembly Language - hard to learn but highly specific to computer language. Less abstracted than C. But still not 0/1 so needs a bit more translation to be used by the computer.


## STEP 4: Linking (.o -> .out)
Linking is a process of including the library files into our program. 


# Arrays
## Data Types
**bool:** 1 byte (T / F)
**int:** 4 bytes (-2000000000 - 2000000000)
**long:** 8 bytes (E or	1,000,000,000,000,000,000 or 1 quintillion)
**float:** 4 bytes (4 billion)
**double:** 8 bytes (more precise than float)
**char:** 1 byte
**string:** ? bytes
...

## Declaring an Array
```
int scores[n];
```

where n = length.

**Instead of declaring a separate variable for each value**
```
int main(void)
{
  int socre1 = get_int("Score: );
  int socre2 = get_int("Score: );
  int socre3 = get_int("Score: );

  printf("Average: %f\n", (score1 + score2 + score3)) / (float) 3;
}
```
**We could do this and declare one variable and index the values part of that variable**
```
int main(void)
{
int scores[3];
scores[0] = get_int("Score: );
scores[1] = get_int("Score: );
scores[2] = get_int("Score: );
printf("Average: %f\n", (scores[0] + scores[1] + scores[3])) / (float);
}
```

**we can design this array creation better using a loop**
```
int main(void)
{
int scores[3];
for (int i = 0; i < 3; i++) {
  scores[i] = get_int("Score: );
}
printf("Average: %f\n", (scores[0] + scores[1] + scores[3])) / (float);
}
```


# Strings
variable length
Just an array of characters represented in ""

**HOW DO YOU KNOW where they end?!**
1 extra byte is added to the end of every string to represent the end
```
\0
```
**Nul:** special null charaacter. zero above represented as a character meaning zero and the end of the string. How printf() knows when to stop printing.

# Command Line Arguments


# Exit Status
When your main function exits, a secret integer is created and will create some kind of error message.

# Cryptography
