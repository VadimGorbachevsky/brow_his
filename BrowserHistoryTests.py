# something like that
import unittest #from browserhistory import *
from  BrowserHistory import *
import inspect
import types
from typing import cast



class BrowserHistoryTests(unittest.TestCase):

    #***********************
    #history list generation
    #***********************
    def history_generation():
        tested_object = BrowserHistory(".");

        askii_a = 97;
        askii_y = 121;
        letter = askii_a;
        url = chr(letter);

        for i in range(5000):
            url = url[:-1] + chr(letter); #Change last simbol to new
            tested_object.visit(url);
            if(letter <= askii_y):
                letter = letter + 1;
            else: #Current letter is "z"
                letter = askii_a;
                url = url + chr(letter); #Add new simbol to changing

        return tested_object;
    #************************

    #All positions are normal on normal way?
    def creation_test(self):
        self.assertEqual(BrowserHistory("www.someth2ing.some").homepage, "www.something.some")

        #just for fun. but we can use this, if we want:

        #this_function_name = cast(types.FrameType, inspect.currentframe()).f_code.co_name
        #print(this_function_name + " SUCCES!");

        #TODO: Other parameters
        #self.assertEqual(BrowserHistory("ololo").current_page, "ololo")
        #self.assertEqual(BrowserHistory("ololo").current_page, "ololo")
        #self.assertEqual(BrowserHistory("ololo").current_page, "ololo")
        #self.assertEqual(BrowserHistory("ololo").current_page, "ololo")

    #Constraints testing pack:
    #• homepage and url consist of '.' or lower case English letters.
    #• 1 <= url.length <= 20
    #• At most 5000 calls will be made to visit, back, and forwa

    #***************************************************************************************
    #• homepage and url consist of '.' or lower case English letters.
    #***************************************************************************************
    # MB is better to make ONE function to test
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

    # TODO: The same to the url-changing / I prefer ONE func

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
        self.assertEqual(BrowserHistory(".").homepage, "www.browser_fail_FAQ.com"); # 1

    #***************************************************************************************
    #• 1 <= steps <= 100 BACK
    #***************************************************************************************
    def middle_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(10), tested_object.history_list[]);
    def max_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(4999), "a");
    def more_than_max_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(7000), "a");
    def zero_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(0), "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyya");
    def negative_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(-7), "www.browser_fail_FAQ.com");
    def one_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(1), "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy");

    #***************************************************************************************
    #• 1 <= steps <= 100 FORWARD
    #***************************************************************************************
    def middle_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(10), tested_object.history_list[]); # 1
    def max_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(4999), tested_object.history_list[]); # 1
    def more_than_max_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(7000), tested_object.history_list[]); # 1
    def zero_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(0), tested_object.history_list[]); # 1
    def negative_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(-7), tested_object.history_list[]); # 1
    def one_steps_back(self):
        tested_object = history_generation();
        self.assertEqual(tested_object.back(1), tested_object.history_list[]); # 1




tests = BrowserHistoryTests();
tests.creation_test();

#BrowserHistory browserHistory = new BrowserHistory("github.com");
#browserHistory.visit("google.com"); // You are in "github.com". Visit
#"google.com"
#browserHistory.visit("facebook.com"); // You are in "google.com". Visit
#"facebook.com"
#browserHistory.visit("youtube.com"); // You are in "facebook.com". Visit
#"youtube.com"
#browserHistory.back(1); // You are in "youtube.com", move back to
#"facebook.com" return "facebook.com"
#browserHistory.back(1); // You are in "facebook.com", move back to
#"google.com" return "google.com"
#browserHistory.forward(1); // You are in "google.com", move forward to
#"facebook.com" return "facebook.com"
#browserHistory.visit("linkedin.com"); // You are in "facebook.com". Visit
#"linkedin.com"
#browserHistory.forward(2); // You are in "linkedin.com", you cannot
#move forward any steps.
#browserHistory.back(2); // You are in "linkedin.com", move back two
#steps to "facebook.com" then to "google.com". return "google.com"
#browserHistory.back(7); // You are in "google.com", you can move
#back only one step to "github.com". return "github.com"
