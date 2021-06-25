#include <stdio.h>
#include <stdlib.h>

#define MAX 200

char * append_null(char* str, int index) {
  str[index] = 0;
  return str;
}
char * longestCommonPrefix(char ** strs, int strsSize){
  char* common_str;
  common_str = malloc(MAX);
  // iterate common index of word
  for (int i = 0; i < MAX; ++i) {
    char ch = strs[0][i];
    if (ch == 0) {
      return append_null(common_str, i);
    }
    // iterate among words
    for (int j = 1; j < strsSize; ++j) {
      if (strs[j][i] != ch) {
        return append_null(common_str, i);
      }
    }
    // Proved ch is common string. So append ch to common_str[].
    common_str[i] = ch;
  }
  return 0;
}


int main() {
}
