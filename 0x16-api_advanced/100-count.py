#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively counts and prints the occurrences of keywords in hot articles.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): The 'after' parameter for pagination.
        counts (dict): Dictionary to store the counts of keywords.

    Returns:
        None
    """
    if counts is None:
        counts = {}

    if after is None:
        headers = {"User-Agent": "custom-agent"}  # Set a custom User-Agent to avoid Too Many Requests error
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        params = {"limit": 100}
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])

            for child in children:
                title = child.get("data", {}).get("title", "").lower()
                for word in word_list:
                    count = title.count(word.lower())
                    if count > 0:
                        counts[word] = counts.get(word, 0) + count

            after = data.get("after")
            if after:
                count_words(subreddit, word_list, after, counts)
            else:
                print_results(counts)
        else:
            print("Error: Unable to fetch data from Reddit API.")
    except Exception as e:
        print("Error:", e)

def print_results(counts):
    """
    Prints the results in the required format.

    Args:
        counts (dict): Dictionary containing keyword counts.

    Returns:
        None
    """
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print("{}: {}".format(word, count))

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])

