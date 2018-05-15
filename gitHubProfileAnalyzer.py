import requests
import json

class gitHubProfileAnalyzer:
    ''' The GitHub Profile Analyzer '''

    URL = "https://api.github.com/users/"   # GitHub API

    def __init__(self, user_name):
        self.user_url = self.URL + user_name
    
    def get_status(self):
        r = requests.get(self.user_url)
        return r.status_code

    def get_info(self, url):
        r = requests.get(url)
        st = r.content.decode("utf-8")  # convert byte to str
        d = json.loads(st)              # convert str to dict
        return d

    def user_info(self):
        info = self.get_info(self.user_url)
        print("User Info:")
        print("Username\t: " + info['login'])
        print("ID\t\t: " + str(info['id']))
        print("Name\t\t: " + info['name'])
        print("GitHub URL\t: "+info['html_url'])
        print("Comapny\t\t: " + str(info['company']))
        # print(info)

    def user_followers(self):
        followers_url = self.user_url + "/followers"
        info = self.get_info(followers_url)
        # print(info)
        print("\n\nFollowers:\nName\t\tGitHub URL")
        c = 1
        for follower in info:
            print(str(c) + "." + follower['login'] + "\t" + follower['html_url'])
            c += 1

    def user_folllowing(self):
        following_url = self.user_url + "/following"
        info = self.get_info(following_url)
        print("\n\nFolLowings:\nName\t\tGitHub URL")
        c = 1
        for following in info:
            print(str(c) + "." + following['login'] + "\t" + following['html_url'])
            c += 1

    def user_starred(self):
        starred_url = self.user_url + "/starred"
        info = self.get_info(starred_url)
        print("\n\nStarred Repositories:")
        c = 1
        for starred in info:
            print(str(c) + "." + starred['name'])
            print("\t" + "Owner\t: " + starred['owner']['login'])
            print("\t " + "URL\t:" + starred['html_url'] + "\n")
            c += 1

def analyze():
    username = input("Enter the GitHub username > ")
    myObj = gitHubProfileAnalyzer(username)
    status = myObj.get_status()
    if status == requests.codes.ok:
        myObj.user_info()
        myObj.user_followers()
        myObj.user_folllowing()
        myObj.user_starred()
    elif status == requests.codes.not_found:
        print("Error 404: Page Not Found")
    else:
        print("Error " + str(status))

analyze()