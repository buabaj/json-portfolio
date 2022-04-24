from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
async def portfolio():
    return {
            "name": "Jerry Buaba",
            "email": "buabajerry@gmail.com",
            "phone": "+233504782862",
            "about_me": "I am a software engineer with a passion for learning and building things that help people :)",
            "twitter": "https://twitter.com/buabaj_",
            "linkedin": "https://www.linkedin.com/in/jerrybuaba",
            "github": "https://github.com/buabaj",
            "blog": "https://buabajerry.medium.com",
            "skills": ['Software development(Backend)', 'Data Science and Machine Learning(NLP, Image Processing, Time series analysis and Prediction)', 'Distributed Version Control System(Git and Github)', 'Databases(SQL, NoSQL)', 'Data Analysis(Pandas, Numpy, Scikit-learn)'],
            "programming_languages":['Python', 'JavaScript', 'SQL'],
            "frameworks": ['Flask', 'FastAPI'],
            "work_experience": {
                1: {
                    "company": "Credit Locus",
                    "link": "https://www.creditlocus.com/",
                    "role": "Software Engineer",
                    "start_date": "May 2020",
                    "end_date": "Present",
                    "description":" yeah i built that b*tch!...with an amazing team of course"
                }
            },
            "projects": {
                1: {
                    "name": "Oval",
                    "description": "A wallet for your data, fast and secure.",
                    "link": "https://oval.so",
                },
                2: {
                    "name": "FastML",
                    "description": "A Python package for running multiple classification algorithms in as little as 4 lines.",
                    "link":"https://pypi.org/project/fastML/"
                },
                3: {
                    "name":"Xplore",
                    "description": "A python package built for data scientist or analysts, AI/ML engineers or researchers for exploring features of a dataset in one line of code for quick analysis before data wrangling and feature extraction.",
                    "link":"https://pypi.org/project/xplore/"
                }
                    
            },
            "education": {
                1: {
                    "school": "Kwame Nkrumah University of Science and Technology",
                    "degree": "Bachelor of Science in Climate Science",
                    "start_date": "September 2018",
                    "end_date": "May 2022",
                }
            },
            "hobbies": ['Watching anime', 'Playing video games', 'Listening to music']
        }




if __name__ == '__main__':
    uvicorn.run(app)