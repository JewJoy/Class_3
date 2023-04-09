# Прикладное и Системное программирование

## Оглавление
- [Прикладное программирование](#Прикладное-программирование)
- [Системное программирование](#Системное-программирование)
- [Python?](#python?)
- [ООП?](#ООП?)
- [Установка и IDE](#Установка-и-IDE)
- [Полезности (информативная сноска)](#Полезности-(информативная-сноска))
___
## Прикладное программирование
Прикладное программирование - это область программирования, связанная с разработкой программного обеспечения для решения конкретных задач в различных областях, например, в финансах, медицине, образовании и т.д.
___
## Системное программирование
Системное программирование - это область программирования, связанная с созданием программного обеспечения, которое работает на более низком уровне компьютерной системы и обеспечивает ее функционирование. Эта область программирования включает в себя разработку операционных систем, драйверов устройств, систем безопасности, сетевых протоколов и других программных компонентов, необходимых для эффективного управления и использования компьютерной системы.

Как предмет в колледже (учебном заведении), системное программирование обычно включает изучение языков программирования, инструментов разработки, алгоритмов и структур данных, архитектуры компьютерных систем и других технических аспектов, связанных с разработкой системного программного обеспечения. Студенты обучаются созданию программных компонентов на более низком уровне их работы, управлению памятью, ресурсами и процессами, а также проектированию и отладке системного программного обеспечения.
___
## Python?
Python - это [интерпретируемый](#Интерпретируемый), высокоуровневый язык программирования, который отличается простым синтаксисом, гибкостью и удобством использования. Он был создан в конце 1980-х годов Гвидо ван Россумом.

Положительные стороны языка:
- Простой и читаемый синтаксис
- Широкая поддержка библиотек и модулей
- Поддержка многих парадигм программирования
- Интерпретируемый язык, что упрощает разработку и отладку кода
- Кроссплатформенность - возможность запускать код на различных операционных системах
- Большое сообщество и поддержка со стороны разработчиков
- Применение в различных областях, от научных вычислений до веб-разработки и машинного обучения.

Альтернативная сторона языка:
- Медленная скорость выполнения по сравнению с компилируемыми языками, такими как C++ или Java
- Непростая (местами ограниченная) поддержка многопоточности
- Отсутствие строгой типизации может привести к ошибкам в коде при работе с разными типами данных
- Более высокий уровень абстракции и удобочитаемость кода могут приводить к меньшей производительности и потреблению большего объема памяти.

> Все вышеперечисленные нюансы решаемы.

Python является языком программирования с поддержкой ООП. В Python все элементы являются объектами, даже простые типы данных, такие как числа и строки. ООП в Python основан на классах, которые определяют структуру и поведение объектов. Классы в Python могут наследоваться, иметь методы, переменные и многое другое.

___
## ООП?

ООП (Объектно-Ориентированное Программирование) - это [методология программирования](#Mетодология-программирования), которая основывается на представлении программы в виде совокупности объектов, каждый из которых имеет свойства (характеристики) и методы (действия), связанные с этим объектом.

В ООП программы разбиваются на более мелкие, самодостаточные части - объекты, которые могут взаимодействовать друг с другом, обмениваясь информацией и вызывая методы друг друга. Объекты могут наследовать свойства и методы других объектов, что делает код более гибким и удобным для работы с большими проектами.

ООП имеет несколько принципов, таких как инкапсуляция, наследование и полиморфизм, которые позволяют создавать более чистый, понятный и эффективный код. ООП используется в широком спектре приложений, от маленьких скриптов до больших проектов, таких как операционные системы и приложения для бизнеса.

___
## Установка и IDE

> В PyCharm установка Python автоматическая. (Но можно указывать уже скачанную версию питона, если необходимо)

Установка Python на компьютер может быть выполнена несколькими способами, в зависимости от операционной системы и конкретной версии Python, которую вы хотите установить.

Скачать установочный файл Python с официального сайта https://www.python.org/downloads/. На странице загрузки нужно выбрать нужную версию Python и операционную систему.

> Использовать можно любую IDE, но я рекомендую PyCharm

**PyCharm** - это интегрированная среда разработки (IDE) для языка программирования Python, разработанная компанией JetBrains.

[Официальный сайт](https://www.jetbrains.com/pycharm/)

Основные функции PyCharm включают:

- Редактор кода с подсветкой синтаксиса и автодополнением кода.
- Отладчик для поиска и исправления ошибок в коде.
- Встроенные инструменты для управления проектами, версионного контроля и сборки проектов.
- Инструменты для автоматического тестирования кода.
- Возможность интеграции с виртуальными средами и серверами для [деплоя](#Деплой) проектов.

___
## Полезности (информативная сноска)

### Деплой

Деплой (от англ. deployment) проектов - это процесс развертывания или установки приложений и программного обеспечения на удаленных серверах или хостингах, готовых к запуску и использованию. В контексте веб-разработки деплой проекта часто означает размещение веб-приложения на сервере, доступном для общего пользования в интернете.

Деплой может включать в себя различные шаги, такие как установка и настройка операционной системы, настройка серверного программного обеспечения, копирование файлов приложения на сервер, установка зависимостей и обновление баз данных, конфигурирование серверных настроек и другие шаги, необходимые для успешного запуска приложения на сервере.

Цель деплоя проектов состоит в том, чтобы обеспечить быстрый и надежный способ развертывания приложений на удаленных серверах, чтобы они были доступны для использования пользователями или другими приложениями.

___
### Mетодология программирования

Методология программирования - это система принципов, процедур и практик, используемых для разработки программного обеспечения. Цель методологии программирования состоит в том, чтобы упростить и улучшить процесс разработки программного обеспечения, чтобы оно было более эффективным, качественным и удобным для использования.

Существует множество методологий программирования, каждая из которых предлагает свой подход к разработке программного обеспечения. 


Более подробная информация на [википедии](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)

___
### Интерпретируемый

Интерпретируемый язык программирования - это язык программирования, который не требует компиляции в машинный код, а выполняется непосредственно в интерпретаторе. В отличие от компилируемых языков, таких как C++, интерпретируемые языки, например, Python, выполняются построчно, преобразуя исходный код программы в машинный код на лету в процессе выполнения программы.

