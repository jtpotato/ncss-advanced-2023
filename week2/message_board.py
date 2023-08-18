import operator

def get_ranking_level(upvotes):
    if upvotes == 0:
        return "Insignificantly Evil"
    elif upvotes < 20:
        return "Cautiously Evil"
    elif upvotes < 100:
        return "Justifiably Evil"
    elif upvotes < 500:
        return "Wickedly Evil"
    elif upvotes >= 500:
        return "Diabolically Evil"


def author_rankings(thread_list):
    # TODO: Determine (author, upvotes, ranking) over all threads.
    authors = {}
    for thread in thread_list:
        for post in thread["posts"]:
            author = post["author"]
            upvotes = post["upvotes"]
            if author not in authors:
                authors[author] = upvotes
            else:
                authors[author] += upvotes

    return_list = []

    for author in authors:
        return_list.append(tuple((author, authors[author], get_ranking_level(authors[author]))))

    return_list = sorted(return_list, key=operator.itemgetter(0), reverse=False)
    return_list = sorted(return_list, key=operator.itemgetter(1), reverse=True)

    return return_list


if __name__ == "__main__":
    # Example calls to your function.
    print(
        author_rankings(
            [
                {
                    "title": "Invade Manhatten, anyone?",
                    "tags": ["world-domination", "hangout"],
                    "posts": [
                        {
                            "author": "Mr. Sinister",
                            "content": "I'm thinking 9 pm?",
                            "upvotes": 2,
                        },
                        {
                            "author": "Mystique",
                            "content": "Sounds fun!",
                            "upvotes": 0,
                        },
                        {
                            "author": "Magneto",
                            "content": "I'm in!",
                            "upvotes": 0,
                        },
                    ],
                }
            ]
        )
    )
