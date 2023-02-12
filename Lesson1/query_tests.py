def parse(query: str) -> dict:
    query_parameters = {}
    if query.find('?') + 1 < len(query) and query.find('?') != -1:
        list_parameters = query.split('?')[1].split('&')
        for x in list_parameters:
            if x:
                key, val = x.split('=')
                query_parameters[key] = val
    return query_parameters


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}


def parse_cookie(query: str) -> dict:
    cookie_parameters = {}
    if query.find(';') != -1:
        list_parameters = query.split(';')
        for x in list_parameters:
            if x:
                key, val = x.split('=', 1)
                cookie_parameters[key] = val
    return cookie_parameters


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}
