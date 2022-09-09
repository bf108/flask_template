from os import environ, path

print(path.dirname(__file__))
base_dir = path.abspath(path.dirname(__file__))
print(base_dir)
print(path.join(base_dir, '.env'))
