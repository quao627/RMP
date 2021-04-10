# RMP
This is a scraper that scrapes information about all the professors and reviews of a given school on RateMyProfessor.

It can be easily implemented by following these steps:
1. Search your school on RateMyProfessor website. 
2. After you are directed to the school page, you will see a "sid=xxxx" part in the link and "xxxx" is the unique id assign for the school.
3. Then, use the following python code:
```python
school_id = 4002  # 4002 is the id for Vanderbilt University.
scraper = RateMyProfScraper(school_id)
school = scraper.createprofessorlist()
```
4. If you want to get information about a specific professor including all of their reviews, find the professor id (tid) and run the following code:
```python
rof_id = 2197326  # 2197326 is the id for Prof. Daniel Arena
num_review = school.loc[school.tid == prof_id, 'tNumRatings'].values[0]
professor = ProfReviewScraper(prof_id, num_review)
reviews = professor.getAllReviews()
```

Check out the demo notebook for a sample output.
