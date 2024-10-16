# pip install zmail

def base_use():
    import zmail
    server = zmail.server('xueda3122356@gmail.com', 'jishtrpmnetbfhvl')

    info = {
        'subject': 'ESL class',
        'from': 'teacher',
        'content_text': 'we have a class tomorrow',
    }

    server.send_mail(['xueda3122356@hotmail.com'], info)

def base_html():
    import zmail
    server = zmail.server('xueda3122356@gmail.com', 'jishtrpmnetbfhvl')

    info = {
        'subject': 'ESL class',
        'from': 'teacher',
        'content_html': '<h1>we have a class tomorrow</h1>',
    }

    server.send_mail(['xueda3122356@hotmail.com'], info)

def base_file():
    import zmail
    server = zmail.server('xueda3122356@gmail.com', 'jishtrpmnetbfhvl')

    info = {
        'subject': 'ESL class',
        'from': 'teacher',
        'content_html': '<h1>we have a class tomorrow</h1>',
        'attachments': ['./generate_data/21_word2pdf.pdf']
    }

    server.send_mail(['xueda3122356@hotmail.com'], info)

def get_mail():
    import zmail
    server = zmail.server('xueda3122356@gmail.com', 'jishtrpmnetbfhvl')

    last_mail = server.get_latest()
    
    print(last_mail.get('subject'))
    print(last_mail.get('from'))
    print(last_mail.get('to'))
    print(last_mail.get('content_text'))
    #print(last_mail.get('content_html'))
    print(last_mail.get('date'))

if __name__ == "__main__":
    get_mail()