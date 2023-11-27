import datetime

from django.test import TestCase
from django.urls import reverse

from tasks.models import Tag, Task


class ModelsTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="work")
        self.task = Task.objects.create(
            content="clean window",
            deadline=datetime.datetime.now(),
        )

    def test_tag_str(self):
        self.assertEqual(str(self.tag), self.tag.name)

    def test_task_str(self):
        self.assertEqual(str(self.task), self.task.content)


class TagViewsTestCase(TestCase):
    def test_create_tag_view(self):
        response = self.client.post(reverse("tasks:tag-create"),
                                    {"name": "animal"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 1)
        new_tag = Tag.objects.first()
        self.assertEqual(new_tag.name, "animal")

    def test_update_tag_view(self):
        tag = Tag.objects.create(name="shop")
        response = self.client.post(
            reverse("tasks:tag-update", args=[tag.pk]), {"name": "work"}
        )
        self.assertEqual(response.status_code, 302)
        updated_tag = Tag.objects.get(pk=tag.pk)
        self.assertEqual(updated_tag.name, "work")

    def test_delete_tag_view(self):
        tag = Tag.objects.create(name="test")
        response = self.client.post(reverse("tasks:tag-delete", args=[tag.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 0)
