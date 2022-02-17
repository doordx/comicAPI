# comicAPI

To Setup the app and display the results follow below steps.
1. Clone the repository.
2. Create the virtual environment using Anaconda.
3. Intall the requirements from requirements.txt.
4. To run the app and display result go to folder and type "python src/app.py".
5. You will see the following result.
  ~~~
  {"name": "Bowl", "alt_text": "For the moment it's a standoff", "num": 39, "link": "", "image": "bowl.jpg", "image_link": "https://imgs.xkcd.com/comics/bowl.jpg"}
  {"name": "Hobby", "alt_text": "The only one of these games I really played was Area 51", "num": 53, "link": "", "image": "hobby.jpg", "image_link": "https://imgs.xkcd.com/comics/hobby.jpg"}
  {"name": "The Cure", "alt_text": "My first try at drawing a real face in years", "num": 56, "link": "", "image": "the_cure.jpg", "image_link":    "https://imgs.xkcd.com/comics/the_cure.jpg"}
  ~~~
6. PS you need to set DB details in Config file and make the <IS_DATABASE_CONNECTED> flag TRUE. It is False by default. 
7. To get comics you need to set parameter "<FETCH_RECORD_THRESHHOLD>" in config File. The default size is 15.


##For More info Please contact repository Owner manishkhatri.in@gmail.com
