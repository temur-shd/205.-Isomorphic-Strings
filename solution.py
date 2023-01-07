class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {} #python map gödterimi

        """for i in range(len(s)):
            c1,c2 = s[i], t[i]"""
        for c1,c2 in zip(s,t):

            if ((c1 in mapST  and mapST[c1] != c2) or (c2 in mapTS  and mapTS[c] != c1):
                return False
            mapST[c1] = c2  #map içinde karakter 1 (c1) karakter 2 ye atama 
            mapTS[c2] = c1
        return True
