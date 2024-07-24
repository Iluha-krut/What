def sorting():
    sp_titles = open('Список.txt', 'r')
    teg1 = ['БПЛА', 'Беспилот', 'беспилот', 'Дрон', 'дрон', 'ЛА', 'БАС', 'оптер']
    sp_teg1 = []
    for title in sp_titles:
        with open(title.strip() + '.txt', 'r', encoding='utf-8') as f:
            article_link = ''
            article_text = ''
            for line in f:
                article_text += line.strip() + '\n'
                if 'Cсылка на статью' in line:
                    article_link = line.strip()
            count1 = 0
            for i in teg1:
                count1 += article_text.count(i)
            if count1 >= 2:
                if article_link != '':
                    sp_teg1.append(article_link + '\n')

    teg_selhoz = ['СХ', 'Сель', 'сель', 'Хозяйственн', 'хозяйственн', 'Агро', 'агро', 'Ферм', 'ферм']
    sp_selhoz = open('Сельхоз.txt', 'w', encoding='utf-8')
    sp_bpla = sp_teg1
    sp_another = open('Другое.txt', 'w', encoding='utf-8')
    for title in sp_bpla:
        f = open(title[:title.find("Cсылка") - 1].strip() + 'txt', 'r', encoding='utf-8')
        text = f.read()
        count = 0
        for word in teg_selhoz:
            count += text.count(word)
        if count >= 1:
            sp_selhoz.write(title.strip() + '\n')
        else:
            sp_another.write(title.strip() + '\n')
    sp_selhoz.close()
