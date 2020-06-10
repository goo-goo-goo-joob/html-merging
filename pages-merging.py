from bs4 import BeautifulSoup
from tqdm.auto import tqdm

if __name__ == '__main__':
    with open('output.html', 'w') as f:
        for page in tqdm(range(1, 11)):
            with open('неделя{}.html'.format(page), 'r', encoding='utf8') as fr:
                bs = BeautifulSoup(fr.read(), "html5lib")    
            # f.write(f'<div class="item active"><h1>Тест {page}:</h1></div>')
            for div in bs.findAll("div", {"class": "xblock xblock-student_view xblock-student_view-vertical xblock-initialized"}):
                f.write(str(div))
