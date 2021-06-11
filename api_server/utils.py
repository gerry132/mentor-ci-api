

def get_json_data():
    try:
        with open('api_server/data/test.json') as json_file:
            json_contents = json_file.read()
            return json_contents
    except Exception as e:
        print('Something went wrong: {}', e)
        return False

