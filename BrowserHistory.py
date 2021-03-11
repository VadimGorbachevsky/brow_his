#Test exersise to PECAN AI

class BrowserHistory:

    def __init__(self, homepage):
        #super(, self).__init__();
        self.homepage = homepage;
        if not(type(homepage) is str):
            self.homepage = "www.fail.com";
        self.current_page = homepage;


    #def BrowserHistory(string homepage):
        #self.homepage = homepage;

#    ~BrowserHistory(self):

    def visit(self, url):
        self.current_page;
    def back( steps):
        return current_page;
    def forward( steps):
        return current_page;

test_case = BrowserHistory("google.com");
