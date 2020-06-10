import requests
from bs4 import BeautifulSoup
from tqdm.auto import tqdm

if __name__ == '__main__':
    with requests.session() as sess, open('page.html', 'w') as f:
        f.write('<style>.item .correct { background-color: lightgreen; font-weight: bold;}</style>\n')
        for page in tqdm(range(1, 19)):
            f.write(f'<div class="item active"><h1>Тест {page}:</h1></div>')
            r = sess.get(f'https://eljob.ru/test/22_{page}')
            bs = BeautifulSoup(r.text, "html5lib")
            for div in bs.findAll("div", {"class": "item active"}):
                f.write(str(div))