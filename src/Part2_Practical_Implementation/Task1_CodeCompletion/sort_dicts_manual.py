def sort_dicts_by_key(data, key):
    """Sort a list of dictionaries by a specified key. Assumes key exists in every dict."""
    return sorted(data, key=lambda x: x[key])

if __name__ == '__main__':
    data = [{'name':'alice','age':30}, {'name':'bob','age':25}, {'name':'carol','age':28}]
    print(sort_dicts_by_key(data,'age'))
