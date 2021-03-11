# something like that
import unittest #from browserhistory import *
from  BrowserHistory import *
class BrowserHistoryTests(unittest.TestCase):
    def test_first(self):
        self.assertEqual(BrowserHistory("ololo").homepage, "ololo")

a = BrowserHistoryTests();
a.test_first();
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
