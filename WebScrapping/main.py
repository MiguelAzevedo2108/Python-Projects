import requests
import bs4


def test1():
    result = requests.get("https://pt.wikipedia.org/wiki/Grace_Hopper")
    soup = bs4.BeautifulSoup(result.text, "lxml")

    # print de todos os campos da biografia
    # for item in soup.select('.toctext'):
    # print(item.text)

    res = requests.get("https://pt.wikipedia.org/wiki/Chris_Paul")

    soup = bs4.BeautifulSoup(res.text, "lxml")

    computer = soup.select('.thumbimage')[0]

    print(computer['src'])
    image_link = requests.get('hhtps://')


# Goal get tittle of every book with a 2 star rating from this end point
def titlebook():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"

    list = []

    for i in range(1, 51):
        scrape_url = base_url.format(i)

        res = requests.get(scrape_url)
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        books = soup.select(".product_pod")

        for book in books:
            if 'star-rating Two' in str(book):
                book_title = book.select('a')[1]['title']
                list.append(book_title)

    print(list)


def quotes():
    res = requests.get('http://quotes.toscrape.com')
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    quotes = []

    for quote in soup.select('.text'):
        quotes.append(quote.text)

    url = 'http://quotes.toscrape.com/page/'

    authors1 = set()

    page_valid = True

    page = 1

    while page_valid:
        page_url = url + str(page)

        res = requests.get(page_url)

        if res.text in 'No quotes found!':
            page_valid = False
            break

        soup1 = bs4.BeautifulSoup(res.text, "lxml")

        for name in soup1.select('.author'):
            authors1.add(name.text)

        page = +1


if __name__ == '__main__':
    quotes()
    # titlebook()
    print('PyCharm')
