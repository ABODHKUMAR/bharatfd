# Disclaimer 
pramodkumar5921 is my brother only, I was fixing some coding issues on git due, due to which I need set his email and password,
I forgot to remove it on my PC.


# Run Backend
    1. cd faq_backend
    2. 4. python manage.py makemigrations
    3. python manage.py migrate
    4. python manage.py runserver # By default it will take 8000 port

# APIs  four
    1. Two Api to server static pages UI
        1.1.1 http://127.0.0.1:8000/api/add_faq/        # to add your FAQs on local
        1.1.2 https://bharatfd.vercel.app/api/add_faq/   # on deployed on vercel 


        1.2.1  http://127.0.0.1:8000/api/faq/          # to see you FAQ based on language choosen
        1.2.2 https://bharatfd.vercel.app/api/faq/     # On deployed on vercel

    2. Two API on backend
        2.1.1 http://127.0.0.1:8000/api/faqs/?lang=en  # to get Array of Object of All FAQ based on Languages like en for English
        2.1.2 https://bharatfd.vercel.app/api/faqs/?lang=en # on deployed on vercel

        2.2.1  http://127.0.0.1:8000/api/create_faq/   # post your FAQs 
            body - JSON Data be Like :
            {
                "question":"What is the largest planet in our solar system?",
                "answer":"Jupiter"
            }

        2.2.2  https://bharatfd.vercel.app/api/create_faq/     


# API ISSUES on Deployment
1. This api not work on deployment (https://bharatfd.vercel.app/api/create_faq/) because I am using db.sqlite3 as database on  deployment we cant add any Data to this but we perform read operation on that.

2. This required only remote database configuration, I dont have any backend Database sever, I tried to find any remote Free Database server but most giving version issues, as this requied 8+ mysql version.


# Is Redis caching functionality used in the project?
Yes, I have used Redis caching functionality to fetch data from the cache if available.


# By default English language will be appear if desired langauage is not present.

# Need changes 

I direclty pushed redis URL to git, Once you see work.


