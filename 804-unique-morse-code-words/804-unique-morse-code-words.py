class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        file = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dict_ ={}
        string = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(file)):
            dict_[string[i]] = file[i]
        res_dict = {}
        for word in words:
            conc = ""
            for char in word:
                conc+= dict_[char]
            res_dict[conc]= 1
        
                
            print(conc)
        # print(dict_)
        return len(res_dict)