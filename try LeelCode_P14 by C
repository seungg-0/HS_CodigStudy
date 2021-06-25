#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STRS_SIZE 200
#define MAX_STR_LENGTH 200
#define MAX_INT_LIST_SIZE 200

char * longestCommonPrefix(char ** strs, int strsSize){
    int* list_len_sep[MAX_INT_LIST_SIZE] = {};
    char* result[MAX_INT_LIST_SIZE] = {};
    char* result_list[MAX_INT_LIST_SIZE][MAX_INT_LIST_SIZE] = {};
    
    // 리스트에 문자열이 하나 존재하는 경우
    if ((sizeof(strs) == 1) && (sizeof(strs[0]) != 0))
        return strs[0];
    
    // 문자열 길이가 담긴 list 생성
    for (int i = 0; i < strsSize; ++i) {
        list_len_sep[i] = sizeof(strs[i]);
      
    int min = list_len_sep[0];
    for(int i = 0; i < sizeof(list_len_sep); i++) {
        if (list_len_sep[i] < min){
            min = list_len_sep[i];
    
        }
    }
    // "" 문자열이 포함된 경우
    if (min == 0) {
        return "";
    }
      
    for(int i = 0; i < min; i++){
        int* lis[MAX_INT_LIST_SIZE] = {};
        for(int j = 0; j < strsSize; j++){
            lis[i] = strs[j][i];
        }
        result_list[i] = lis[i];
        printf(result_list[i]);
    }  
  }
  return 0;
}

int main() {
  char* test[MAX_STRS_SIZE] = 
  {"double pointer use tutorial","to the moon", "three"};
  longestCommonPrefix(test, 3);
}
