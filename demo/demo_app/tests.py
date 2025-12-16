from django.test import TestCase
from .models import NotesDemo
from django.urls import reverse
from datetime import date as d


class NotesTest(TestCase):
    def setUp(self):
        """
        creating a dummy piece of data to test. at the same time
         making sure it can be created
        :return:
        """
        NotesDemo.objects.create(label="Test Label", first_name="Justin", last_name="Case",
                                 content="This is test content", date=d(1111, 11, 1))
        note = NotesDemo.objects.get(label="Test Label")
        self.id_to_test = note.id

    def test_object(self):
        """
        Making sure that the entry is actually saved correctly
        without anything changing.
        :return:
        """
        note = NotesDemo.objects.get(label="Test Label")
        first_name = note.first_name
        last_name = note.last_name
        content = note.content
        current_date = note.date
        self.assertEqual(first_name, 'Justin')
        self.assertEqual(last_name, 'Case')
        self.assertEqual(content, 'This is test content')
        self.assertEqual(current_date, d(1111, 11, 1))

    def test_object_modification(self):
        """
        testing that if something is saved it stays saved
        :return:
        """
        note = NotesDemo.objects.get(label="Test Label")
        note.first_name = 'Jack'
        note.save()

        note = NotesDemo.objects.get(label="Test Label")
        first_name = note.first_name
        self.assertEqual(first_name, 'Jack')

    # def test_object_deletion(self):
    #     """
    #     Making sure that the deletion actually works
    #     :return:
    #     """
    #     note = NotesDemo.objects.get(label="Test Label")
    #     note.delete()
    #
    #     with self.assertRaises(NotesDemo.DoesNotExist):
    #         note = NotesDemo.objects.get(label="Test Label")

    def test_home_page(self):
        response = self.client.get(reverse('Home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome")

    def test_list_page(self):
        response = self.client.get(reverse('List'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Label")

    def test_edit_page(self):
        response = self.client.get(reverse(f'Update', args=[str(self.id_to_test)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Label")

    def test_deletion_page(self):
        response = self.client.get(reverse(f'Delete', args=[str(self.id_to_test)]))
        self.assertEqual(response.status_code, 302)




