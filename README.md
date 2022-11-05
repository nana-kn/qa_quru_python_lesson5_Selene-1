# qa_quru_python_lesson5_Selene_1

В новом проекте, соответствующему базовому формату «проекта для автотестов», разработай автотест на заполнение и отправку формы https://demoqa.com/automation-practice-form
Запушьте код в github-репозиторий и дайте на него ссылку в качестве ответа на домашнее задание.

Условия:
- Библиотеки, разрешенные к использованию: pytest, selene.
- Можно использовать функции для определения фикстур для прекондишенов к тесту.
- Если часть сценария является прекондишеном к тесту и включает низкоуровневый технический код (например, ожидание догрузки рекламы и удаление ее со страницы с помощью JavaScript)  тогда можно соответствующий код вынести в функцию с читабельным именем, определив ее в этом же файле с тестом.
- Не обязательно, но можно использовать функции для рефакторинга частей кода, которые повторяются, при этом приводя либо к слишком громоздкому коду, либо высокому риску изменений в будущем.
- Нельзя использовать функции с целью создания более читабельных абстракций для действий над элементами.
- Можно использовать переменные для самодокументирования элементов с нечитабельными селекторами. Нечитабельным считается селектор не использующий терминов полностью отображающих пользу элемента на странице. Цель – выжать максимум по "читабельности" из тех селекторов которые можно построить, при этом, стараясь подобрать селекторы максимально стабильные, минимально «хрупкие», минимизируя использование переменных с целью самодокументирования.

Дополнительно:
- Реализуй автотест на таблицу по адресу https://demoqa.com/webtables включающий шаги: 1) добавить новую четвертую строку 2) отредактировать все поля во второй строке; 3) удалить третью строку;
