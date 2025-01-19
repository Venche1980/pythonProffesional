from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Определяем список ключевых слов
KEYWORDS = ['собеседования', 'Linux', 'хорошо', 'Go']


def get_habr_articles():
    # Инициализация драйвера Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        # Загружаем страницу
        driver.get('https://habr.com/ru/articles/')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )

        articles = driver.find_elements(By.TAG_NAME, 'article')

        matching_articles = []

        for article in articles:
            try:

                title = article.find_element(By.CSS_SELECTOR, 'h2 span').text.strip()

                if any(keyword.lower() in title.lower() for keyword in KEYWORDS):

                    link = article.find_element(By.CSS_SELECTOR, 'h2 a').get_attribute('href')
                    date_str = article.find_element(By.TAG_NAME, 'time').get_attribute('datetime')
                    date = datetime.fromisoformat(date_str).strftime('%Y-%m-%d %H:%M:%S')

                    matching_articles.append({
                        'date': date,
                        'title': title,
                        'link': link
                    })

            except Exception as e:
                print(f"Ошибка при обработке статьи: {e}")
                continue

        return matching_articles

    finally:
        driver.quit()


def main():
    articles = get_habr_articles()

    for article in articles:
        print(f"{article['date']} - {article['title']} - {article['link']}")


if __name__ == '__main__':
    main()