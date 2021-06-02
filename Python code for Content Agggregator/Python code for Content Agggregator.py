""" Content Aggregator"""
print('\n\n\n******************************************HELLO! WELCOME TO ABC, AND THANK YOU FOR VISITING OUR WEBSITE******************************************\n\n******************************HERE WE OFFERS LATEST AND AUTHENTIC NEWS FROM VARIOUS WEBSITES. THUS SAVING YOUR TIME!!!******************************\n\n********************************************************************HAVE A LOOK!!!********************************************************************')
print("""
                                                    
         ,--.                                       
       ,--.'|    ,---,.           .---.  .--.--.    
   ,--,:  : |  ,'  .' |          /. ./| /  /    '.  
,`--.'`|  ' :,---.'   |      .--'.  ' ;|  :  /`. /  
|   :  :  | ||   |   .'     /__./ \ : |;  |  |--`   
:   |   \ | ::   :  |-, .--'.  '   \' .|  :  ;_     
|   : '  '; |:   |  ;/|/___/ \ |    ' ' \  \    `.  
'   ' ;.    ;|   :   .';   \  \;      :  `----.   \ 
|   | | \   ||   |  |-, \   ;  `      |  __ \  \  | 
'   : |  ; .''   :  ;/|  .   \    .\  ; /  /`--'  / 
|   | '`--'  |   |    \   \   \   ' \ |'--'.     /  
'   : |      |   :   .'    :   '  |--"   `--'---'   
;   |.'      |   | ,'       \   \ ;                 
'---'        `----'          '---"                  
                                                    
""")
import urllib, os, requests, datetime, subprocess
import praw, pprint
import feedparser
reddit = praw.Reddit(client_id='XXXXXXX',
                     client_secret='XXXXXXXXXXX',
                     grant_type_access='client_credentials',
                     user_agent='script/1.0')

class News:
    def Indian_News(self):
        newsfeed = feedparser.parse(
            "http://feeds.feedburner.com/ndtvnews-india-news"
        )
        print("\n\n\nToday's News: ")
        for i in range(0, 20):
            entry = newsfeed.entries[i]
            print(entry.title)
            print(entry.summary)
            print("\n------News Link--------")
            print(entry.link)
            print("\n###########################################\n")
        print('-------------------------------------------------------------------------------------------------------')
class Medium:
    def medium_programming(self):
        feed_programming = feedparser.parse(
            "https://medium.com/feed/tag/programming"
        )
        print("\n\n\nProgramming Today: ")
        for i in range(10):
            entry = feed_programming.entries[i]
            print(entry.title)
            print("\nURL: " + entry.link)
            print("\n###########################################\n")
        print('-------------------------------------------------------------------------------------------------------')
    def medium_python(self):
        feed_python = feedparser.parse(
            "https://medium.com/feed/tag/python"
        )
        print("\n\n\nPython Today: ")
        for i in range(10):
            entry = feed_python.entries[i]
            print(entry.title)
            print("\nURL: " + entry.link)
            print("\n###########################################\n")
        print('-------------------------------------------------------------------------------------------------------')
    def medium_developer(self):
        feed_developer = feedparser.parse(
            "https://medium.com/feed/tag/developer"
        )
        print("\n\n\nDeveloper News Today: ")
        for i in range(5):
            entry = feed_developer.entries[i]
            print(entry.title)
            print("\nURL: " + entry.link)
            print("\n###########################################\n")
        print('-------------------------------------------------------------------------------------------------------')
News_object = News()
Medium_object = Medium()
if __name__ == "__main__":
    News_object.Indian_News()
    Medium_object.medium_python()
    Medium_object.medium_programming()
    Medium_object.medium_developer()

print('WE HOPE YOU LIKED OUR CONTENT!!!\nYOU CAN ALSO BECOME OUR PREMIUM MEMBER AND UNLOCK MORE FEATURES OF THIS WEBSITE AND MORE EXCITING CONTENT.\nDO YOU WANT TO BECOME A PREMIUM MEMBER???')
answer = input("Enter yes or no: ")
if answer == "yes":
	import webbrowser
	webbrowser.open('https://www.messenger.com/t/106138404741481')
elif answer == "no":
	print('That OK!!!\nTHANKS FOR VISITING............') 
else:
	print("Please enter yes or no.") 
