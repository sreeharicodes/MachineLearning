import numpy as np 
from numpy import linalg as la


import csv as csv


def GetData(data_file):
    csv_object = csv.reader(open(data_file,"rb"))        
    user_ratings = []
    for row in csv_object:
        user_ratings.append(row)
    user_ratings = np.array(user_ratings)
    return user_ratings.astype(np.int)

def GetRatings(user_rating,user,item):

    numitems = np.shape(user_rating)[1]
    total = 0
    simrating = 0

    for index in range(numitems):
        if user_rating[user,index] !=0:
           similarity = 0.5 + 0.5*np.corrcoef(user_rating[::,item],user_rating[::,index])[0][1]
           total += similarity
           simrating += similarity*user_rating[user,index]
    return simrating/total

def GetRatingsSVD(user_rating,user_rating_ld,user,item):

    numitems = np.shape(user_rating)[1]
    total = 0
    simrating = 0

    for index in range(numitems):
        if user_rating[user,index] !=0:
           similarity = 0.5 + 0.5*np.corrcoef(user_rating_ld[item,::],user_rating_ld[index,::])[0][1]
           total += similarity
           simrating += similarity*user_rating[user,index]
    return simrating/total



def RunWithoutSVD():
     print "SvdRec.py"
     file = 'recdata.txt'
     user_ratings= GetData(file)
     print user_ratings
     numusers = np.shape(user_ratings)[0]
     
     for user in range(numusers):
         not_rated = np.nonzero(user_ratings[user,:]==0)[0]
         ItemRatings = {}
         for item in not_rated:
             rating = GetRatings(user_ratings,user,item)
             ItemRatings[item] = rating  
     topItemRatings = sorted(ItemRatings.items(),key = lambda x :x[1],reverse=True)[:3]

     for key in topItemRatings:
         print key 

def RunWithSVD():
     print "SvdRec.py"
     file = 'recdata.txt'
     user_ratings= GetData(file)
     print user_ratings
     numusers = np.shape(user_ratings)[0]
     U,S,V = np.linalg.svd(user_ratings)

     Sigma = np.mat(np.eye(4)*S[:4])

     usigma = U[:,:4]*Sigma.I

     user_ratings_ld = user_ratings.T*usigma
     
     for user in range(numusers):
         not_rated = np.nonzero(user_ratings[user,:]==0)[0]
         ItemRatings = {}
         for item in not_rated:
             rating = GetRatingsSVD(user_ratings, user_ratings_ld,user,item)
             ItemRatings[item] = rating  
     topItemRatings = sorted(ItemRatings.items(),key = lambda x :x[1],reverse=True)[:3]

     for key in topItemRatings:
         print key 
 
 
       
if __name__ == '__main__':	
     RunWithoutSVD()
     print "--------------------------------"
     RunWithSVD()