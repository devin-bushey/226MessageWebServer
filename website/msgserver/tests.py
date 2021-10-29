from django.test import TestCase
from msgserver.models import Message

# Create your tests here.

class MessageTestCase(TestCase):
    def test_create(self):
        #print('[START TEST]: test_create')
        response = self.client.post("/msgserver/create/", {'key': '87654CBA', 'msg': 'Test Case #1'})
        m = Message.objects.get(key='87654CBA')
        #print('key: ', m.key, 'msg: ', m.msg)
        self.assertEqual(m.key, '87654CBA')
        self.assertEqual(m.msg, 'Test Case #1')

    def test_duplicate_msg(self):
        response = self.client.post("/msgserver/create/", {'key': '87654CBA', 'msg': 'Test Case #1'})
        response = self.client.post("/msgserver/create/", {'key': '87654CBA', 'msg': 'Test Case #1'})
        self.assertIn(b'Key already exists', response._container[0])

    def test_isKeyAlphanumeric(self):
        response = self.client.post("/msgserver/create/", {'key': '1234567!', 'msg': 'Test'})
        self.assertFormError(response, 'form', 'key', 'Key is not alphanumeric')
        try:
            Message.objects.get(key='12345!')
            self.fail()
        except Message.DoesNotExist:
            pass

    def test_key_length(self):
        response = self.client.post("/msgserver/create/", {'key': '1234567', 'msg': 'Test'})
        self.assertFormError(response, 'form', 'key', 'Key must have a length of 8')
        try:
            Message.objects.get(key='1234567')
            self.fail()
        except Message.DoesNotExist:
            pass

        
    def test_msg_length(self):
        response = self.client.post("/msgserver/create/", {'key': '1234567A', 'msg': ''})
        self.assertFormError(response, 'form', 'msg', 'This field is required.')
        try:
            Message.objects.get(key='1234567A')
            self.fail()
        except Message.DoesNotExist:
            pass
        
    def test_msg_update(self):
        response = self.client.post("/msgserver/create/", {'key': '1234567A', 'msg': 'Test'})
        m = Message.objects.get(key='1234567A')
        self.assertEqual(m.msg, 'Test')

        response = self.client.post("/msgserver/update/1234567A/", {'msg': 'Test Update'})
        m = Message.objects.get(key='1234567A')
        self.assertEqual(m.msg, 'Test Update')

    def test_json(self):
        response = self.client.post("/msgserver/create/", {'key': '1234567A', 'msg': 'Test'})
        response = self.client.post("/msgserver/create/", {'key': '1234567B', 'msg': 'Test'})
        response = self.client.post("/msgserver/")
        #print('[Response]:', response._container[0])
        self.assertEqual(response._container[0], b'{{"key": "1234567A", "msg": "Test"}{"key": "1234567B", "msg": "Test"}}')





