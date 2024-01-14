This repository holds a Django based web application which is a Freelancing website i.e. RetroCraftHub and is a submission for IMG winter assignment.
Here recruiters can offer jobs and find young and experienced freelancers,
Whereas freelancers can lookout for job opportunities and explore trusted recruiters.

Even though, RetroCraftHub was supposed to be a team project, still I have made it on my own as a solo project.
In the process I learned how to make Django based websites from Newton School Coding for all.
This project is already deployed at https://kunal-retrocrafthub.onrender.com 

How to run on localhost:
1) Clone the repository and cd to the Freelancing-Website repository (master repo).
   
2) Go into settings.py inside RetroCraft_Hub (main project repo)
   
3) Find the first 3 commented lines which start with "###" and uncomment them, instead comment the 3 lines which are just over each one of them and save it. (Just like in the video at 1:45sec)
   This way we changed the project settings from production to localhost.
   
4) Create a virtual environment inside master repository and run it using
   >>> python -m venv env
   >>> .\env\Scripts\activate
   
5) Install all the modules in requirements.txt using
   >>> pip install -r requirements. txt
   
6) Finally
   >>> python manage.py runserver
   And visit (http://127.0.0.1:8000/)

Again Thanks to everyone at IMG

Made with ❤︎ by Kunal
