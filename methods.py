def transform(method, locator, text):
    locator = locator.format(text)
    return method, locator
