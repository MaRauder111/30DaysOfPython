def flatten(countries):
    return [sub for sub in countries]


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

print(flatten(countries))