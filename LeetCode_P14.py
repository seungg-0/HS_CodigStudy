class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        list_len_sep = []
        result_list = []
        result = ""

        if (len(strs) == 1) and (len(strs[0]) != 0):
            return strs[0]

        for i in range(0, len(strs)):
            list_len_sep.append(len(strs[i]))
            
        if min(list_len_sep) == 0:
            return ""

        for i in range(0, min(list_len_sep)):
            lis = []
            for j in range(0, len(strs)):
                lis.append(strs[j][i])
            del_dupl = set(lis)
            result_list.append(list(del_dupl))

        for i in range(0, len(result_list)):
            if len(result_list[0]) > 1:
                return ""

            elif len(result_list[i]) == 1:
                result += str(result_list[i][0])
                if i == (len(result_list) - 1):
                    return result
            else:
                return result
