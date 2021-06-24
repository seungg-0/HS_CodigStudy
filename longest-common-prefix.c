#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STRS_SIZE 200
#define MAX_STR_LENGTH 200

char * longestCommonPrefix(char ** strs, int strsSize){
  for (int i = 0; i < strsSize; ++i) {
    printf("%s\n", strs[i]);
  }
  return 0;
}
int main() {
  char* test[MAX_STRS_SIZE] = 
  {"double pointer use tutorial","to the moon", "three"};
  longestCommonPrefix(test, 3);
}
