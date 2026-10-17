class Solution:

    def encode(self, strs: List[str]) -> str:
        temp_arr = []
        for i in range(len(strs)):
            if i > 0:
                temp_arr.append("+")
            for j in range(len(strs[i])):
                temp_arr.append(str(ord(strs[i][j])) + "E")
        return "EMPTY" if len(strs) == 0 else "".join(temp_arr)

    def decode(self, s: str) -> List[str]:
        temp_arr2 = []
        split_str = [] if s == "EMPTY" else s.split("+")
        for i in range(len(split_str)):
            split_word_ascii = split_str[i].split("E")
            decoded_word = ""
            for j in range(len(split_word_ascii) - 1):
                decoded_word += chr(int(split_word_ascii[j]))
            temp_arr2.append(decoded_word)
        return temp_arr2
