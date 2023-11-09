# БФТ QA 2023 БФУ. Ягубков Даниил

## Где лежит отчет о тестировании?
```bash
reports/report.html
```

## Как запустить тесты?

1. Установить [poetry](https://python-poetry.org/docs/#installing-with-pipx)
2. Установить зависимости
```bash
poetry install
```

3. Задать переменные окружения в `source/configuration/.env`
```ini
STACKOVERFLOW_LOGIN = <str>
STACKOVERFLOW_PASSWORD = <str>
```

4. Запустить тесты
```bash
pytest
```

5. (Опционально) Запуск тестов с генерацией отчета
```bash
pytest -s -v --headed --html=reports/report.html
```