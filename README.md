Пояснительная записка к проекту
===========
Для начала игры нужно запустить файл EntreMenu.py

Коллекционные карточная игра – разновидность игр, которая быра выбрана для данного проекта. Для создания своей игры нашей команде понадобилось реализовать следующий функционал

Регистрация и вход в приложение
===========
Перед началом игры нужно пройти простую регистрацию или в свой аккаунт. Это нужно для определения общей характеристики игрока (его уровень, кол-во побед, проигрышей и т.д.). Для регистрации нужно ввести пароль в соответствии с требованиями. После чего пользователь может зайти в игру 
Основное окно
В основном окне пользователь может:
1)	 Открыть правила
2)	 Открыть настройки
3)	 Начать игру
4)	 Выйти из игры

Правила
===========
Окно, где игроки могут посмотреть описание игры. Сложных функций и механик в этом окне нет. Для перехода назад есть кнопка “Назад”.
Настройки

Настройки
===========
Окно, где игрок может отрегулировать громкость музыки. Ползунок отвечает за эту регулировку. Для перехода назад нужно нажать на кнопку “Назад”.

Выйти
===========
Кнопка, которая выключит программу. Это всё, что требуется от этой функции.

Игра
===========
Перед игрой надо выбрать режим игры. От режима будет зависеть количество здоровья игрока и задний экран.
В игре игроки играют на доске с колодами карт. В начале матча у каждого противника по 5 карт на руке, в конце раунда они получают по 1-ой карте.  Игрок может сыграть карту и потратить ману, если маны не хватит, то карту нельзя будет сыграть.
Каждая карта имеет свои характеристики (хп, атаку, затрату маны и т.д.). Они определяют действие карт на поле боя. Игрок может играть только своими картами.

Завершить ход можно:
1.	Потратив всю ману. Ход перейдёт другому автоматически
2.	Нажав на кнопку ход.
3.	По истечению времени (На все действие в раунде даётся 45 секунд!)

Игрок выигрывает, если враг погибает и наоборот, если пользователь умирает, то поражение. В конце игры можно увидеть свою статистику.
