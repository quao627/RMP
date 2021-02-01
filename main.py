from RateMyProfScraper import RateMyProfScraper
from ProfReviewScraper import ProfReviewScraper
import pandas as pd

if __name__ == '__main__':
    school_id = 4002  # 4002 is the id for Vanderbilt University.

    scraper = RateMyProfScraper(school_id)
    school = scraper.createprofessorlist()
    school = pd.DataFrame(school)
    school.to_csv("School/Vanderbilt.csv")

    prof_id = 2197326  # 2197326 is the id for Prof. Daniel Arena
    num_review = school.loc[school.tid == prof_id, 'tNumRatings'].values[0]

    arena = ProfReviewScraper(prof_id, num_review)
    arena = pd.DataFrame(arena.getAllReviews())
    arena.to_csv("Ratings/Daniel_Arena.csv")



