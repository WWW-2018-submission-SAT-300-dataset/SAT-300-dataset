import requests

r = requests.get(
    'https://raw.githubusercontent.com/WWW-2018-submission-SAT-300-dataset/SAT-300-dataset/master/SAT-300.json')

if r.status_code != requests.codes.ok:
    print("The request to the dataset's GitHub repository failed!")
else:
    json_contents = r.json()

    html_file = open('SAT-300.html', 'w')

    html_file.write("""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <title>SAT-300 dataset</title>
                        </head>
                        <body>""")

    disambiguated_text_index = 0

    for disambiguated_text in json_contents['disambiguated_texts']:
        disambiguated_text_index += 1

        disambiguated_entities = disambiguated_text['disambiguated_entities']

        html_file.write('<b>{}</b>. '.format(disambiguated_text_index))
        text = disambiguated_text['text']

        char_index = 0

        for char in text:
            if not disambiguated_entities:
                html_file.write(text[char_index:])
                break
            if disambiguated_entities[0]['start_offset'] == char_index:
                html_file.write('<a href="{}">'.format(disambiguated_entities[0]['GKG_url']))
            html_file.write(char)
            if disambiguated_entities[0]['end_offset'] == char_index + 1:
                html_file.write('</a>')
                del disambiguated_entities[0]
            char_index += 1

        html_file.write('<br>\n<br>\n')

    html_file.write("""</body>
                        </html>""")

    html_file.close()
