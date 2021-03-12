#Test exersise to PECAN AI
import collections

class BrowserHistory:
    FAIL_PAGE = "www.browser_fail_FAQ.com"; #TECH PAGE.
    MAX_COUNT = 4999;                       #BORDER FROM TR - 1 to use ">" and "<". More simple.

    # URL (MUST BE A STRING) AND (CONTAINS ONLY a-z AND DOTS) AND (HAVE SIZE FROM 1 TO 20):
    def value_test(self, target_string):
        if not(type(target_string) is str):
            return self.FAIL_PAGE;
        a = [x for x in target_string if ('a' <= x <= 'z') ] + [x for x in target_string if x == "."]
        if( len(a) == len(target_string) ) and ( 0 < len(a) < 21 ):
            return target_string;
        else:
            return self.FAIL_PAGE;

    def __init__(self, homepage):
        self.homepage = self.value_test(homepage);
        self.current_page = self.homepage;
        self.history_list = collections.deque();     #because easy to LIFO append/pop
        self.history_list.append(self.current_page);
        self.count = 1;                              #of all history
        self.position = 1;                           #of the current_page

    def visit(self, url):
        self.current_page = self.value_test(url);
        self.history_list.append(self.current_page);
        if(self.count > self.MAX_COUNT):                   #BORDER FROM TR
            self.history_list.popleft()               #History is LIFO
        else:
            self.count = self.count + 1;
            self.position = self.position + 1;

    def back(self, steps):
        if (not(type(steps) is int) or ( steps < 0 )): #ERROR
            self.visit(self.FAIL_PAGE);
            return self.current_page;
        if( steps == 0 ):                              #NOTHING
            return self.current_page;
        if( steps > self.position-1 ):                 #OVERFLOW
            self.current_page = self.history_list[0];
            self.position = 1
            return self.current_page;

        #AND IF ALL NORMAL
        self.current_page = self.history_list[self.position-1-steps];
        self.position = self.position-steps
        return self.current_page;

    def forward(self, steps):
        if (not(type(steps) is int) or ( steps < 0 )):  #ERROR
            self.visit(self.FAIL_PAGE);
            return self.current_page;
        if( steps == 0 ):                               #NOTHING
            return self.current_page;
        if( steps > (self.count-self.position) ):       #OVERFLOW
            self.current_page = self.history_list[self.count-1];
            self.position = self.count
            return self.current_page;

        #AND IF ALL NORMAL
        self.current_page = self.history_list[self.position+steps-1];
        self.position = self.position+steps
        return self.current_page;
