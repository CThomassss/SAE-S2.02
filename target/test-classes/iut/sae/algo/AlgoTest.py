import unittest;

def RLE(in_str) : 
        # Provide your algo here
        res = "" 
        count = 1 
        i = 0 
        while i < len(in_str) - 1 :
            if in_str[i] == in_str[i+1] : 
                count+=1
                if count == 10 : 
                    res += "9" + in_str[i] 
                    count = 1 
            else : 
                res+= str(count) + in_str[i] 
                count = 1 
            i+=1
        res += str(count) + in_str[-1]
        return res 
    

def RLE(in_str, iteration)  :  
        # Provide your algo here
        rle = in_str 
        for rle in range(iteration) :
            rle = RLE(rle)
        return rle 
                                                      

def unRLE(in_str)  :
        # Provide your algo here
        res = "" 
        i = 0 
        while i < len(in_str) :
            if in_str[i].isdigit() :
                cpt = int(in_str[i])
                i += 1
                if i < len(in_str) : 
                    res += in_str[i] * cpt
            else :
                res += in_str[i]
            i += 1 
        return res 

def unRLE(in_str, iteration)  : 
        # Provide your algo here
        rle = in_str
        for rle in range(iteration) :
            rle = UnRLE(rle)
        return rle


class TestAlgoCorriger(unittest.TestCase):
    def test_RLE(self):
        self.assertEqual("", RLE(""))
        self.assertEqual("1a1b1c", RLE("abc"))
        self.assertEqual("1a2b3c", RLE("abbccc"))
        self.assertEqual("3a1b2a", RLE("aaabaa"))
        self.assertEqual("1a1A1a", RLE("aAa"))
        self.assertEqual("9W4W", RLE("WWWWWWWWWWWWW"))

        # Supplementary tests
        self.assertEqual("1a1b1c1A1B1C1D1E1d1e", RLE("abcABCDEde"))
        self.assertEqual("1a1b9B7B2b1c", RLE("abBBBBBBBBBBBBBBBBbbc"))
        self.assertEqual("2a", RLE("aa"))
        self.assertEqual("111213", RLE("123"))
        self.assertEqual("259n9n2n3z2r1t1r1y261019", RLE("55nnnnnnnnnnnnnnnnnnnnzzzrrtry6609"))

    def test_RLE_recursif(self):
        try:
            self.assertEqual("", RLE("", 1))
            self.assertEqual("", RLE("", 3))

            self.assertEqual("1a1b1c", RLE("abc", 1))
            self.assertEqual("1a2b3c", RLE("abbccc", 1))
            self.assertEqual("3a1b2a", RLE("aaabaa", 1))
            self.assertEqual("1a1A1a", RLE("aAa", 1))

            self.assertEqual("111a111b111c", RLE("abc", 2))
            self.assertEqual("311a311b311c", RLE("abc", 3))

            sae_ite20 = "1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211S1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211A1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211E1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211 1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211A1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211l1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211g1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123112221221321132132211231131122211331121321232221121113122113121113222123113221231231121113213221231221132221222112112322211o"
            self.assertEqual(sae_ite20, RLE("SAE Algo", 20))

            sae_ite15 = "311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211a311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211z311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211e311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211r311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211t311311222113111231133211121312211231131112311211133112111312211213211312111322211231131122111213122112311311221132211221121332211y"
            self.assertEqual(sae_ite15, RLE("azerty", 15))
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def test_unRLE(self):
        try:
            self.assertEqual("", unRLE(""))
            self.assertEqual("abc", unRLE("1a1b1c"))
            self.assertEqual("abbccc", unRLE("1a2b3c"))
            self.assertEqual("aaabaa", unRLE("3a1b2a"))
            self.assertEqual("aAa", unRLE("1a1A1a"))
            self.assertEqual("WWWWWWWWWWWWW", unRLE("9W4W"))

            # Supplementary tests
            self.assertEqual("aaAAaaBBaa", unRLE("2a2A2a2B2a"))
            self.assertEqual("aAAbbbBBBBccccc", unRLE("1a2A3b4B5c"))
            self.assertEqual("aAAbbbBBBBccccc", unRLE(RLE("aAAbbbBBBBccccc")))
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def test_unRLE_recursif(self):
        try:
            self.assertEqual("", unRLE("", 1))
            self.assertEqual("", unRLE("", 3))

            self.assertEqual("abc", unRLE("1a1b1c", 1))
            self.assertEqual("abbccc", unRLE("1a2b3c", 1))
            self.assertEqual("aaabaa", unRLE("3a1b2a", 1))
            self.assertEqual("aAa", unRLE("1a1A1a", 1))

            self.assertEqual("abc", unRLE("111a111b111c", 2))
            self.assertEqual("abc", unRLE("311a311b311c", 3))

            # Supplementary tests
            self.assertEqual("aaaavrrvr", unRLE("3114311a13211v3112311r13211v13211r", 4))
            self.assertEqual("zzzzERRTTTRZaz", unRLE(
                "1113122114111312211z31131122211E1113122112111312211R11131211121312211T31131122211R31131122211Z31131122211a31131122211z",
                6))
            self.assertEqual("azerty", unRLE(RLE("azerty", 15), 15))
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")


if __name__ == '__main__':
    unittest.main()