import requests
import json
import math
import pandas as pd


class ProfReviewScraper:
    def __init__(self, profID, nReview):
        self.profID = profID
        self.nReview = nReview

    def getNumPage(self):
        numPage = self.nReview // 20 + 1
        return numPage

    def getAllReviews(self):
        numPage = self.getNumPage()
        ratingslist = []
        for i in range(1, numPage + 1):
            url = "https://www.ratemyprofessors.com/paginate/professors/ratings?tid=" + str(
                self.profID) + "&filter=&courseCode=&page=" + str(i)
            page = requests.get(url)
            jsonpage = json.loads(page.content)
            ratings = jsonpage["ratings"]
            ratingslist.extend(ratings)
        return ratingslist