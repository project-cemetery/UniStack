# UniStack README

> если на машине установлены разные версии Python, то везде следует заменить `python/pip` на `python3/pip3` 

## Развертывание на локальной машине
+ `git clone git@bitbucket.org:GarikNovel/unistack.git`
+ `cd unistack`
+ `pip install -r requirements.txt --upgrade`
+ `python manage.py migrate`

## Работа с проектом локально
+ `git pull`
+ `pip install -r requirements.txt --upgrade`
+ `python manage.py migrate`
+ запустить сервер `python manage.py runserver 6340`
+ проект доступен в браузере [http://127.0.0.1:6340/](http://127.0.0.1:6340/)
+ выключить сервер – **control+C**

## Команды
### Получение данных из внешнего источника 
Команда загружает все полученные данные в базу данных. 
> `python manage.py parse [source]`

Доступные параметры для [source]

1. `fgos` – **направления подготовки** по группам с сайта [Федеральный портал: Российское образование](http://www.edu.ru/abitur/act.6/index.php)
2. `cities` – **города** по регионам и странам из таблицы [Cites for Migration](https://docs.google.com/spreadsheets/d/1Mp9r7CNxVnKip-tLAFpbGp4K_MY2iUrbrBOQBcsKLVE/edit?usp=sharing)
3. `universities --wave=n` – **увниверситеты** n-ой волны из таблицы [Universities for Migration](https://docs.google.com/spreadsheets/d/15Q8sDyG_eBUHMcriIAHTmwDcdSdJSSLNAo34iBZKyJk/edit?usp=sharing)
4. `exams` – **экзмены** из таблицы [Exams for Migration](https://docs.google.com/spreadsheets/d/1iw-Wv4omM8GoAhdF3yKBKXQzECZBFClRJIVsOrqcynU/edit#gid=0)
