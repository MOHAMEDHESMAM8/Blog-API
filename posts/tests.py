from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from rest_framework import  status
from django.urls import reverse


# Create your tests here.

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="testuser",
            email="testuser@gmail.com",
            password="secret"
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title=" test title",
            body="test body"
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, " test title")
        self.assertEqual(self.post.body, "test body")
        self.assertEqual(str(self.post), " test title")

    def test_api_postList(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(response, self.post)

    def test_api_postDetails(self):
        response = self.client.get(
            reverse("post_detail",
                    kwargs={"pk": self.post.id})
            , format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(response, " test title")
