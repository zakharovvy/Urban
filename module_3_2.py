def send_email (message, recipient,*, sender = "university.help@gmail.com"):
    if '@' not in recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not (sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net")):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('May the Force be with you', 'kenobi.sw@gmail.com')
send_email('Почему ты такой серьезный???', 'batman@mail.ru', sender='joker.dark.knight@gmail.com')
send_email('Жизнь — как коробка шоколадных конфет...', 'watcher@mail.ru', sender='forest.gump@mail.uk')
send_email('I will be back', 'terminator@mail.ru', sender='terminator@mail.ru')


