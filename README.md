
**Django Blog Project with Elasticsearch**

This is a Django-based blog project that stores blog entries in an Elasticsearch database. The project supports searching for terms in both the journal titles and texts.

**Prerequisites**

Before running this project, ensure you have the following installed:

Python 3

Django

Docker

Elasticsearch

**Installation steps**

Clone this repo

Run these commands

pip3 install django-elasticsearch-dsl

python manage.py migrate

python manage.py createsuperuser

docker-compose up

python manage.py runserver

**Working code snippet**
Get call
![image](https://github.com/siddhant21/Blog_project/assets/46870926/e879407b-cb59-47bd-bc51-b8dfbfd80018)


Post call
![image](https://github.com/siddhant21/Blog_project/assets/46870926/c3c6dc99-5975-4652-aaae-636bb7cd0509)

I have created Ui to show this more precisely how elasticsearch would get the query data
![image](https://github.com/siddhant21/Blog_project/assets/46870926/2c9378ba-7a56-45e0-baf0-f86ae7c6480d)

Add blog from UI
![image](https://github.com/siddhant21/Blog_project/assets/46870926/f978e506-4550-48a0-81d2-6280c7a58c22)




License
This project is licensed under the MIT License - see the LICENSE file for details.
