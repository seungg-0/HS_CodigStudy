class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        list_len_sep = []
        result_list = []
        result = ""
        
        # 리스트에 문자열이 하나 존재하는 경우
        if (len(strs) == 1) and (len(strs[0]) != 0): 
            return strs[0]

        # 문자열의 길이가 담긴 list 생성
        for i in range(0, len(strs)):
            list_len_sep.append(len(strs[i]))
            
        # "" 문자열이 포함된 경우
        if min(list_len_sep) == 0:
            return ""

        # 이외의 경우
        for i in range(0, min(list_len_sep)):
            lis = []
            for j in range(0, len(strs)):
                lis.append(strs[j][i])
            del_dupl = set(lis)
            result_list.append(list(del_dupl))

        # output 생성
        for i in range(0, len(result_list)):
            if len(result_list[0]) > 1:
                return ""

            elif len(result_list[i]) == 1:
                result += str(result_list[i][0])
            else:
                break
        return result
