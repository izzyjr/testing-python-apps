from unittest import TestCase
from blog.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Ralph')

        self.assertEqual('Test by Test Author (0 post)', b.__repr__())
        self.assertEqual('My Day by Ralph (0 post)', b2.__repr__())

    def test_repr_multiple_posts(self):
        b = Blog('My Day', 'Ralph')
        b.posts = ['Test', 'Test2']

        self.assertEqual('My Day by Ralph (2 posts)', b.__repr__())

