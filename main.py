import re
from NetscapeBookmarksFileParser import creator

data = ['hello-world', 'hello-darkness-my-old-friend', 'hello-darkness-charlie-murphy', 'hello-satan']

outcome = {
    'hello': {
        'darkness': {
            'charlie': {
                'murphy': None,
            },
            'my': {
                'old': {
                    'friend': None,
                },
            },
        },
        'satan': None,
        'world': None,
    },
}

# regex to allow words starting with uk-, teamcity-, airbyte, data-
allowed = re.compile(r"^(uk|teamcity|airbyte|data)-")


def make_trie(links: list[str]):
    root = dict()
    for link in links:
        if not allowed.match(link):
            continue
        current_dict = root
        for word in link.split("-"):
            current_dict = current_dict.setdefault(word, {})
        current_dict[word] = f"https://github.com/marshmallow-insurance/{link}"
        current_dict = sorted(current_dict)
    return root


def make_data():
    from pathlib import Path
    repos = Path.home() / "projects" / "marshmallow"
    for repo in sorted(repos.iterdir()):
        if repo.is_dir():
            yield repo.name


def make_folder(name, parent=None):
    f = creator.BookmarkFolder()
    f.name = name
    f.parent = parent
    return f


def make_shortcut(name, href):
    s = creator.BookmarkShortcut()
    s.name = name
    s.href = href
    return s


def recurse_folder(trie: dict, folder=make_folder('repos')):
    for key, value in trie.items():
        if isinstance(value, dict):
            child = make_folder(key, parent=folder)
            folder.items.append(child)
            recurse_folder(value, folder=child)
        else:
            shortcut = make_shortcut(value, value)
            folder.items.append(shortcut)

    return folder


def build_folder():
    folder = recurse_folder(make_trie(make_data()))
    while True:
        parent = folder.parent
        if parent is None:
            return folder
        else:
            folder = parent


if __name__ == '__main__':
    trie = make_trie(make_data())
    folder = build_folder()
    out = creator.folder_creator(folder)
    from pathlib import Path
    outfile = Path.home() / "bookmarks.html"
    outfile.write_text("\n".join(out))
    pass





