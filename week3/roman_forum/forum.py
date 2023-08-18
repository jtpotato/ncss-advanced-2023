from post import Post
from thread import Thread


class Forum:
  def __init__(self):
    """
    Perform initialisation of a new Forum object, as needed.
    """
    self.threads: list[Thread] = []
  
  def get_threads(self):
    """
    Returns a list of Threads in the Forum, in the order that they were published.
    """
    return self.threads
  
  def publish(self, title, content, author):
    """
    Creates a new Thread with the given title and adds it to the Forum.
    The content and author are provided to allow you to create the first Post object.
    Threads are stored in the order that they are published.
    Returns the new Thread object.
    """
    thread = Thread(title, Post(content, author))
    self.threads.append(thread)
    return thread
  
  def search_by_tag(self, tag):
    """
    Searches all forum Threads for any that contain the given tag.
    Returns a list of matching Thread objects in the order they were published.
    """
    threads_with_tag = []
    for thread in self.threads:
      if tag in thread.get_tags():
        threads_with_tag.append(thread)
    return threads_with_tag
  
  def search_by_author(self, author):
    """
    Searches all forum Threads for Posts by the given author.
    Returns a list of matching Post objects in any order you like.
    """
    posts_with_author = []
    for thread in self.threads:
      for post in thread.get_posts():
        if post.get_author() == author:
          posts_with_author.append(post)
    return posts_with_author