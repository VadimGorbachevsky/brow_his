# something like that
import unittest #from browserhistory import *
from  BrowserHistory import *
import inspect
import types
from typing import cast
from itertools import permutations



class BrowserHistoryTests(unittest.TestCase):

    #***********************
    # history list generation to back/forward tests
    #***********************
    def history_generation(self):
        tested_object = BrowserHistory(".");
        urls = list( permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g']) ) #5040 variants
        for i in range(5000):
            perm_as_normal_string = ''.join(urls[i]);
            tested_object.visit(perm_as_normal_string);

        last_perm = ''.join(urls[i])
        pre_last_perm = ''.join(urls[i-1])
        first_perm = ''.join(urls[0])
        second_perm = ''.join(urls[1])
        ten_step_ago_perm = ''.join(urls[i-10])
        ten_step_from_start_perm = ''.join(urls[10])
        return tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm;

    #************************
    #Firstly: All positions are normal on normal way?
    def creation_test(self):
        tested_object = BrowserHistory("www.something.some")
        self.assertEqual(tested_object.homepage, "www.something.some")
        self.assertEqual(tested_object.current_page, "www.something.some")
        #just for fun. but we can use this, if we really needed:
        #this_function_name = cast(types.FrameType, inspect.currentframe()).f_code.co_name
        #print(this_function_name + " SUCCES!");

#***************************************************************************************
# CONSTRAINTS TESTING
#***************************************************************************************

    #***************************************************************************************
    #• homepage consist of '.' or lower case English letters.   SAME url
    #***************************************************************************************
    # homepage
    #***********
    def normal_homepage(self):
        self.assertEqual(BrowserHistory("www.something.some").homepage, "www.something.some");
    def no_string_type_homepage(self):
        self.assertEqual(BrowserHistory(2).homepage, "www.browser_fail_FAQ.com");
    def with_numbers_homepage(self): # Numbers
        self.assertEqual(BrowserHistory("somethingwith0").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith1").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith2").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith3").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith4").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith5").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith6").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith7").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith8").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith9").homepage, "www.browser_fail_FAQ.com");
    def with_special_simbols_homepage(self): # Special simbols
        #math
        self.assertEqual(BrowserHistory("somethingwith-").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith+").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith*").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith/").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith%").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith=").homepage, "www.browser_fail_FAQ.com");

        #punctuation
        self.assertEqual(BrowserHistory("somethingwith!").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith?").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith,").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith;").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith:").homepage, "www.browser_fail_FAQ.com");

        #breack
        self.assertEqual(BrowserHistory("somethingwith(").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith)").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith[").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith]").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith{").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith}").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith<").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith>").homepage, "www.browser_fail_FAQ.com");

        #other
        self.assertEqual(BrowserHistory("somethingwith`").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith~").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith'").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith\"").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith_").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith@").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith#").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith$").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith^").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith&").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwith|").homepage, "www.browser_fail_FAQ.com");
    def with_big_case_homepage(self):
        self.assertEqual(BrowserHistory("somethingwithA").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithB").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithC").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithD").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithE").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithF").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithG").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithH").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithI").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithJ").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithK").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithL").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithM").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithN").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithO").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithP").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithR").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithS").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithT").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithQ").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithU").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithV").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithW").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithX").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithY").homepage, "www.browser_fail_FAQ.com");
        self.assertEqual(BrowserHistory("somethingwithZ").homepage, "www.browser_fail_FAQ.com");
    def with_spaces_homepage(self):
        self.assertEqual(BrowserHistory("somethingwith ").homepage, "www.browser_fail_FAQ.com"); #space
        self.assertEqual(BrowserHistory("somethingwith  ").homepage, "www.browser_fail_FAQ.com"); #\t
    def with_unsupported_lang_url(self):
        self.assertEqual(BrowserHistory("שדגי").homepage, "www.browser_fail_FAQ.com"); #space
        self.assertEqual(BrowserHistory("Текст").homepage, "www.browser_fail_FAQ.com"); #\t
    #***********
    # url
    #***********
    def normal_url(self):
        tested_object = BrowserHistory("www.something.some")
        tested_object.visit("www.anything.some")
        self.assertEqual(tested_object.current_page, "www.anything.some");
    def no_string_type_url(self):
        tested_object = BrowserHistory("www.something.some")
        tested_object.visit(2)
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
    def with_numbers_url(self): # Numbers
        tested_object = BrowserHistory("www.something.some")
        tested_object.visit("somethingwith0")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith1")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith2")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith3")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith4")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith5")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith6")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith7")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith8")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith9")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
    def with_special_simbols_url(self): # Special simbols
        tested_object = BrowserHistory("www.something.some")
        #math
        tested_object.visit("somethingwith-")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith+")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith*")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith/")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith%")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith=")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        #punctuation
        tested_object.visit("somethingwith!")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith?")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith,")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith;")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith:")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        #breack
        tested_object.visit("somethingwith(")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith)")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith[")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith]")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith{")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith}")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith>")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith<")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        #other
        tested_object.visit("somethingwith`")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith~")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith'")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith\"")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith_")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith@")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith#")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith$")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith^")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith&")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwith|")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
    def with_big_case_url(self):
        tested_object = BrowserHistory("www.something.some")
        tested_object.visit("somethingwithA")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithB")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithC")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithD")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithE")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithF")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithG")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithH")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithI")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithJ")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithK")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithL")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithM")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithN")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithO")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithP")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithR")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithS")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithT")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithQ")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithU")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithV")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithW")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithX")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithY")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("somethingwithZ")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
    def with_spaces_url(self):
        tested_object = BrowserHistory("www.something.some")
        tested_object.visit("somethingwith ")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com"); #space
        tested_object.visit("somethingwith  ")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com"); #\t
    def with_unsupported_lang_url(self):
        tested_object = BrowserHistory("www.something.some")
        tested_object.visit("שדגי")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");
        tested_object.visit("Текст")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com");

    #***************************************************************************************
    #• 1 <= homepage.length <= 20  SAME url
    #***************************************************************************************
    def void_homepage(self):
        self.assertEqual(BrowserHistory("").homepage, "www.browser_fail_FAQ.com"); # 0
    def morethantwentysimbols_homepage(self):
        self.assertEqual(BrowserHistory("morethantwentysimbols").homepage, "www.browser_fail_FAQ.com"); # 21
    def twenty_simbols_homepage(self):
        self.assertEqual(BrowserHistory("orethantwentysimbols").homepage, "orethantwentysimbols"); # 20
    def middle_homepage(self):
        self.assertEqual(BrowserHistory("eightsim").homepage, "eightsim"); # 8
    def one_simbol_homepage(self):
        self.assertEqual(BrowserHistory(".").homepage, ".");

    #***********
    # url
    #***********
    def void_url(self):
        tested_object = BrowserHistory("www.something.some")
        tested_object.visit("")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com"); # 0
    def morethantwentysimbols_url(self):
        tested_object = BrowserHistory("www.something.some")
        tested_object.visit("morethantwentysimbols")
        self.assertEqual(tested_object.current_page, "www.browser_fail_FAQ.com"); # 21
    def twenty_simbols_url(self):
        tested_object = BrowserHistory("www.something.some")
        tested_object.visit("orethantwentysimbols")
        self.assertEqual(tested_object.current_page, "orethantwentysimbols"); # 20
    def middle_url(self):
        tested_object = BrowserHistory("www.something.some")
        tested_object.visit("eightsim")
        self.assertEqual(tested_object.current_page, "eightsim"); # 8
    def one_simbol_url(self):
        tested_object = BrowserHistory("www.something.some")
        tested_object.visit(".")
        self.assertEqual(tested_object.current_page, ".");

    #***************************************************************************************
    #• 1 <= steps <= 100 BACK
    #***************************************************************************************
    def middle_steps_back(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        self.assertEqual(tested_object.back(10), ten_step_ago_perm);
    def max_steps_back(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        self.assertEqual(tested_object.back(4999), first_perm);
    def more_than_max_steps_back(self): # Test also covered THE END situaltion
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        self.assertEqual(tested_object.back(7000), first_perm);
    def zero_steps_back(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        self.assertEqual(tested_object.back(0), last_perm);
    def negative_steps_back(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        self.assertEqual(tested_object.back(-7), "www.browser_fail_FAQ.com");
    def one_steps_back(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        self.assertEqual(tested_object.back(1), pre_last_perm);
    def not_int_back(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        self.assertEqual(tested_object.back('asdas'), "www.browser_fail_FAQ.com");

    #***************************************************************************************
    #• 1 <= steps <= 100 FORWARD
    #***************************************************************************************
    def middle_steps_forward(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        tested_object.back(7000)
        self.assertEqual(tested_object.forward(10), ten_step_from_start_perm);
    def max_steps_forward(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        tested_object.back(7000)
        self.assertEqual(tested_object.forward(4999), last_perm);
    def more_than_max_steps_forward(self): # Test also covered THE END situaltion
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        tested_object.back(7000)
        self.assertEqual(tested_object.forward(7000), last_perm);
    def zero_steps_forward(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        tested_object.back(7000)
        self.assertEqual(tested_object.forward(0), first_perm);
    def negative_steps_forward(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        tested_object.back(7000)
        self.assertEqual(tested_object.forward(-7), "www.browser_fail_FAQ.com");
    def one_steps_forward(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        tested_object.back(7000)
        self.assertEqual(tested_object.forward(1), second_perm);
    def not_int_forward(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        self.assertEqual(tested_object.forward('asdas'), "www.browser_fail_FAQ.com");

    #***************************************************************************************
    #• At most 5000 calls will be made to visit, back, and forward
    #***************************************************************************************
    def max_items_limit_test(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        tested_object.visit("newpage")
        self.assertEqual(tested_object.back(1), last_perm); #Last now PRE_LAST cuz of shift
        self.assertEqual(tested_object.back(7000), second_perm); #Second now FIRST cuz of shift
        self.assertEqual(tested_object.forward(7000), "newpage"); #And new at the end

#***************************************************************************************
# FUNCTIONAL SCENARY FROM TR
#***************************************************************************************
    def scenary_test(self):
        tested_object = BrowserHistory("github.com");
        self.assertEqual(tested_object.current_page, "github.com");
        tested_object.visit("google.com");
        self.assertEqual(tested_object.current_page, "google.com");
        tested_object.visit("facebook.com");
        self.assertEqual(tested_object.current_page, "facebook.com");
        tested_object.visit("youtube.com");
        self.assertEqual(tested_object.current_page, "youtube.com");
        self.assertEqual(tested_object.back(1), "facebook.com");
        self.assertEqual(tested_object.back(1), "google.com");
        self.assertEqual(tested_object.forward(1), "facebook.com");
        tested_object.visit("linkedin.com");
        self.assertEqual(tested_object.current_page, "linkedin.com");
        self.assertEqual(tested_object.forward(2), "linkedin.com");
        self.assertEqual(tested_object.back(2), "facebook.com");
        self.assertEqual(tested_object.back(7), "github.com");


#***************************************************************************************
# GO!
#***************************************************************************************
tests = BrowserHistoryTests();
tests.creation_test();
tests.normal_homepage();
tests.no_string_type_homepage();
tests.with_numbers_homepage();
tests.with_special_simbols_homepage();
tests.with_big_case_homepage();
tests.with_spaces_homepage();
tests.with_unsupported_lang_url();
tests.normal_url();
tests.no_string_type_url();
tests.with_numbers_url();
tests.with_special_simbols_url();
tests.with_big_case_url();
tests.with_spaces_url();
tests.with_unsupported_lang_url();
tests.void_homepage();
tests.morethantwentysimbols_homepage();
tests.twenty_simbols_homepage();
tests.middle_homepage();
tests.one_simbol_homepage();
tests.void_url();
tests.morethantwentysimbols_url();
tests.twenty_simbols_url();
tests.middle_url();
tests.one_simbol_url();
tests.middle_steps_back();
tests.max_steps_back();
tests.more_than_max_steps_back();
tests.zero_steps_back();
tests.negative_steps_back();
tests.one_steps_back();
tests.not_int_back();
tests.middle_steps_forward();
tests.max_steps_forward();
tests.more_than_max_steps_forward();
tests.zero_steps_forward();
tests.negative_steps_forward();
tests.one_steps_forward();
tests.not_int_back();
tests.max_items_limit_test();
print("ALL TECHNICAL TESTS IS OK");
tests.scenary_test();
print("SCENARY TEST TESTS IS OK");
