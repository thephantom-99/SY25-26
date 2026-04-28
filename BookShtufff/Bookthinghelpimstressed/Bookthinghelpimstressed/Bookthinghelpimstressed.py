import requests
from bs4 import BeautifulSoup

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

<<<<<<< Updated upstream
# Convert word ratings to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

search_title = input("Enter a book title: ").lower()
found = False

for page in range(1, 51):  # site has 50 pages
    url = base_url.format(page)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error on page {page}")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
=======
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')  # Fixed: use .text, not .txt

    books = soup.find_all('article', class_='product_pod')  # Fixed: class_='product_pod'
>>>>>>> Stashed changes

    for book in books:
        title = book.h3.a['title']
        rating_class = book.find('p', class_='star-rating')['class']
        rating_word = rating_class[1]
        rating = rating_map[rating_word]

        if search_title in title.lower():
            print(f"\n✅ Found on page {page}")
            print(f"Title: {title}")
            print(f"Rating: {rating} / 5")

            # Optional: save to file
            with open("result.txt", "w") as f:
                f.write(f"Title: {title}\n")
                f.write(f"Rating: {rating} / 5\n")
                f.write(f"Page: {page}\n")

            found = True
            break

    if found:
        break

if not found:
    print("\n❌ Book not found across all pages.")