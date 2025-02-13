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


data = ['hello-world', 'hello-darkness-my-old-friend', 'hello-darkness-charlie-murphy', 'hello-satan']


def make_trie(links: list[str]):
    root = dict()
    for link in links:
        current_dict = root
        for word in link.split("-"):
            current_dict = current_dict.setdefault(word, {})
        current_dict[word] = link
        current_dict = sorted(current_dict)
    return root


def make_data():
    from pathlib import Path
    repos = Path.home() / "projects" / "marshmallow"
    for repo in sorted(repos.iterdir()):
        if repo.is_dir():
            yield repo.name


def make_html(trie: dict):
    pass


if __name__ == '__main__':

    trie = make_trie(make_data())
    pass





