# БФТ QA 2023 БФУ. Ягубков Даниил

<div>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Packaged with Poetry](https://img.shields.io/badge/packaging-poetry-cyan.svg)](https://python-poetry.org/)<br>
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Pytest](https://img.shields.io/badge/pytest-7.4.3-blue.svg)](https://docs.pytest.org/en/7.4.x/)
[![Playwright](https://img.shields.io/badge/playwright-1.39.0-blue.svg)](https://playwright.dev/python/docs/intro)

</div>

## Где лежит отчет о тестировании?
1. Онлайн - [GitHub Pages](https://pheezz.github.io/bft-2023-ikbfu-test/?sort=result)
2. Локально - `reports/report.html`


## Как запустить тесты?

1. Установить [poetry](https://python-poetry.org/docs/#installing-with-pipx) поверх python 3.11
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