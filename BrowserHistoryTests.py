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
        self.assertEqual(BrowserHistory("www.something.some").homepage, "www.something.some")
            #just for fun. but we can use this, if we want:
            #this_function_name = cast(types.FrameType, inspect.currentframe()).f_code.co_name
            #print(this_function_name + " SUCCES!");
        #TODO: Other parameters
        #self.assertEqual(BrowserHistory("ololo").current_page, "ololo")
        #self.assertEqual(BrowserHistory("ololo").current_page, "ololo")
        #self.assertEqual(BrowserHistory("ololo").current_page, "ololo")
        #self.assertEqual(BrowserHistory("ololo").current_page, "ololo")

#***************************************************************************************
# CONSTRAINTS TESTING
#***************************************************************************************
    #• At most 5000 calls will be made to visit, back, and forwa

    #***************************************************************************************
    #• homepage and url consist of '.' or lower case English letters.
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
    #***********
    # url
    #***********
    def normal_url(self):
            self.assertEqual(BrowserHistory("www.something.some").homepage, "www.something.some");
    def no_string_type_url(self):
            self.assertEqual(BrowserHistory(2).homepage, "www.browser_fail_FAQ.com");
    def with_numbers_url(self): # Numbers
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
    def with_special_simbols_url(self): # Special simbols
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
    def with_big_case_url(self):
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
    def with_spaces_url(self):
            self.assertEqual(BrowserHistory("somethingwith ").homepage, "www.browser_fail_FAQ.com"); #space
            self.assertEqual(BrowserHistory("somethingwith  ").homepage, "www.browser_fail_FAQ.com"); #\t

    #***************************************************************************************
    #• 1 <= homepage.length <= 20
    #***************************************************************************************
    def void_homepage(self):
        self.assertEqual(BrowserHistory("").homepage, "www.browser_fail_FAQ.com"); # 0
    def morethantwentysimbols_homepage(self):
        self.assertEqual(BrowserHistory("morethantwentysimbols").homepage, "www.browser_fail_FAQ.com"); # 21
    def twenty_simbols_homepage(self):
        self.assertEqual(BrowserHistory("orethantwentysimbols").homepage, "www.browser_fail_FAQ.com"); # 20
    def middle_homepage(self):
        self.assertEqual(BrowserHistory("eightsim").homepage, "www.browser_fail_FAQ.com"); # 8
    def one_simbol_homepage(self):
        self.assertEqual(BrowserHistory(".").homepage, "www.browser_fail_FAQ.com");

    #***********
    # url
    #***********
    def void_url(self):
        self.assertEqual(BrowserHistory("").homepage, "www.browser_fail_FAQ.com"); # 0
    def morethantwentysimbols_url(self):
        self.assertEqual(BrowserHistory("morethantwentysimbols").homepage, "www.browser_fail_FAQ.com"); # 21
    def twenty_simbols_url(self):
        self.assertEqual(BrowserHistory("orethantwentysimbols").homepage, "www.browser_fail_FAQ.com"); # 20
    def middle_url(self):
        self.assertEqual(BrowserHistory("eightsim").homepage, "www.browser_fail_FAQ.com"); # 8
    def one_simbol_url(self):
        self.assertEqual(BrowserHistory(".").homepage, "www.browser_fail_FAQ.com");

    # TODO: The same to the url-changing / I prefer ONE func

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
        self.assertEqual(tested_object.forward(-7), "www.browser_fail_FAQ.com"]);
    def one_steps_forward(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        tested_object.back(7000)
        self.assertEqual(tested_object.forward(1), second_perm);
    def not_int_back(self):
        tested_object, last_perm, pre_last_perm, first_perm, second_perm, ten_step_ago_perm, ten_step_from_start_perm = self.history_generation();
        self.assertEqual(tested_object.forward('asdas'), "www.browser_fail_FAQ.com");

#***************************************************************************************
# FUNCTIONAL SCENARY FROM TR
#***************************************************************************************
    def scenary_test(self):
        tested_object = BrowserHistory("github.com");
        self.assertEqual(tested_object.visit("google.com").current_page, "google.com");
        self.assertEqual(tested_object.visit("facebook.com").current_page, "facebook.com");
        self.assertEqual(tested_object.visit("youtube.com").current_page, "youtube.com");
        self.assertEqual(tested_object.back(1), "facebook.com");
        self.assertEqual(tested_object.back(1), "google.com");
        self.assertEqual(tested_object.forward(1), "facebook.com");
        self.assertEqual(tested_object.visit("linkedin.com").current_page, "linkedin.com");
        self.assertEqual(tested_object.forward(2), "linkedin.com");
        self.assertEqual(tested_object.back(2), "google.com");
        self.assertEqual(tested_object.back(7), "github.com");



tests = BrowserHistoryTests();
tests.creation_test();
tests.middle_steps_back();
