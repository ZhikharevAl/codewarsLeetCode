path = "/Users/lia/hello-world/hello-world.js"


def get_filename(path):
    return path.split("/")[-1].split(".")[0]


print(get_filename(path))
