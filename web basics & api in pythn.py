#1 what is access token ?
print("An access token is an object that describes the security context of a process or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread. When a user logs on, the system verifies the user's password by comparing it with information stored in a security database. If the password is authenticated, the system produces an access token. Every process executed on behalf of this user has a copy of this access token.")
# access token
print("\n")
print("1008651176999641089-ziendYsODjVeTLg4N8uCGeJARKqNfz\n")


#2 Get IP address of some common sites
# Google IP address is
print("172.217.15.110")
# Facebook IP address is
print("31.13.65.36")
# Gmail IP address is
print("172.217.15.101\n")

#3
import tweepy
consumer_key = "2suvC3GdG84oDHOJQmALQEf1d"
consumer_secret = "xBCyY55Ym0YaIDSapn01v2Kzwo6mkYPdFYRQ7QTYeShVklLL4H"
access_token = "1008651176999641089-ziendYsODjVeTLg4N8uCGeJARKqNfz"
access_secret = "id4Lt89JafIbZc8gu58hruekpKZQzH6VH2mXrFHMlFPAe"

oauth = tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api = tweepy.API(oauth)
public_tweets = api.search("#RobinSharma")
print(public_tweets)
print("\n")


#4
print("API is a part of library which defines how an application communicates with external code.\nAPI can be written in any language.")
print("Library is written in same language which is a collection of all the functionalities required for the use case.\n")
# example
print("For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.")