#Test exersise to PECAN AI
import collections

class BrowserHistory:
    FAIL_PAGE = "www.browser_fail_FAQ.com";
    MAX_COUNT = 5000;

    def __init__(self, homepage):
        # URL MUST BE A STRING
        if not(type(homepage) is str):
            self.homepage = self.FAIL_PAGE;
        else:
            # Take only a-z and dots:
            a = [x for x in homepage if ('a' <= x <= 'z') ] + [x for x in homepage if x == "."]
            if( len(a) == len(homepage) ) and ( 0 < len(a) < 21 ):
                self.homepage = homepage;
            else:
                self.homepage = self.FAIL_PAGE;
        self.current_page = self.homepage;
        self.history_list = collections.deque(self.current_page);
        self.count = 1;
        self.position = 1;

    def visit(self, url):
        # URL MUST BE A STRING
        if not(type(url) is str):
            self.current_page = self.FAIL_PAGE;
            return;
        # Take only a-z and dots:
        a = [x for x in url if ('a' <= x <= 'z') ] + [x for x in url if x == "."];
        if( len(a) != len(url) ) or ( len(a) > 20 ) or ( len(a) == 0 ):
            self.current_page = self.FAIL_PAGE;
            return;
        # IF ALL OK:
        self.current_page = url;
        self.history_list.append(url);
        if(self.count > 4999):
            self.history_list.popleft()
        else:
            self.count = self.count + 1;
            self.position = self.position + 1;

    def back(self, steps):
        if not(type(steps) is int):
            self.current_page = self.FAIL_PAGE;
            return self.current_page;
        if( steps < 0 ):
            self.current_page = self.FAIL_PAGE;
            return self.current_page;
        if( steps == 0 ):
            return self.current_page;
        if( steps > self.count ):
            self.current_page = self.history_list[0];
            self.position = 0
            return self.current_page;
        self.current_page = self.history_list[self.position-1-steps];
        self.position = self.position-steps
        return self.current_page;

    def forward(self, steps):
        if not(type(steps) is int):
            self.current_page = self.FAIL_PAGE;
            return self.current_page;
        if( steps < 0 ):
            self.current_page = self.FAIL_PAGE;
            return self.current_page;
        if( steps == 0 ):
            return self.current_page;
        if( steps > self.count ):
            self.current_page = self.history_list[0];
            return self.current_page;
        self.current_page = self.history_list[self.position-1+steps];
        self.position = self.position+steps
        return self.current_page;
