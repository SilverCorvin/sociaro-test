# Sociaro-test
Тестовое задание № 1
## Загрузка
Для загрузки данного репозитория, выполните в консоли:

    $ git clone https://github.com/SilverCorvin/sociaro-test.git

### Запуск
Для запуска выполните:  
    
    $ docker-compose build && docker-compose up

### Вход
Для входа использутей URL [http://127.0.0.1:8000/manage/index](http://127.0.0.1:8000/manage/index)

### Комментарии к тестовому заданию
* Management команда называется processvideo
* Вместо management, для задач описанных в тестовом задании, лучше использовать Celery
* По правилам python лучше не исользовать дефис в наименованиях переменных, модулей и пакетов "-".    
При попытке создать проект с наименованием video-previewer происходит ошибка:    
CommandError: 'video-previewer' is not a valid project name. Please make sure the name is a valid identifier.
* Невозможно создать приложение с наименованием manage, так как данное имя конфликтует с именем существующего Python модуля    
CommandError: 'manage' conflicts with the name of an existing Python module and cannot be used as an app name. Please try another name.
