from urllib.parse import urljoin
import requests


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.csrf_token = None
        self.session = requests.Session()

    def post_login(self, email, password):
        headers = {
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': email,
            'password': password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
        }
        self.session.post('https://auth-ac.my.com/auth?lang=ru&nosavelogin=0', headers=headers, data=data,
                          allow_redirects=True)
        self.csrf_token = self.get_token()

    def get_token(self):
        headers = self.session.get(urljoin(self.base_url, 'csrf/')).headers['Set-Cookie'].split(';')
        csrf_token = [h for h in headers if 'csrftoken' in h][0].split('=')[-1]
        return csrf_token

    def post_upload_image(self, image):
        file = {
            'file': open(image, 'rb'),
        }
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        response = self.session.post(urljoin(self.base_url, '/api/v2/content/static.json'), headers=headers, files=file)
        json_response = response.json()
        return json_response['id']

    def get_url_id(self, url):
        response = self.session.get(urljoin(self.base_url, f'/api/v1/urls/?url={url}'))
        json_response = response.json()
        return json_response['id']

    def post_create_campaign(self, name, image_id, url_id, objective='traffic', package_id=961):
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        json = {
            "banners": [{"content": {"image_240x400": {"id": image_id}}, "urls": {"primary": {"id": url_id}}}],
            "name": name,
            "objective": objective, "package_id": package_id
        }
        response = self.session.post(urljoin(self.base_url, '/api/v2/campaigns.json'), headers=headers, json=json)
        json_response = response.json()
        return json_response['id']

    def delete_campaign(self, campaign_id):
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        response = self.session.delete(urljoin(self.base_url, f'api/v2/campaigns/{campaign_id}.json'), headers=headers)
        return response

    def post_create_segment(self, name, pass_condition, object_type, left=365, right=0, seg_type='positive'):
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        json = {
            'name': name,
            'pass_condition': pass_condition,
            "relations": [{"object_type": object_type, "params": {"left": left, "right": right, "type": seg_type}}]
        }
        response = self.session.post(urljoin(self.base_url, '/api/v2/remarketing/segments.json?fields=id,name'),
                                     headers=headers, json=json)
        json_response = response.json()
        return json_response['id']

    def post_delete_segment(self, segment_id, source_type='segment'):
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        json = [{"source_id": segment_id, "source_type": source_type}]
        response = self.session.post(urljoin(self.base_url, '/api/v1/remarketing/mass_action/delete.json'),
                                     headers=headers, json=json)
        json_response = response.json()
        return json_response['successes'][0]['source_id']

    def get_segment_status_code(self, segment_id):
        response = self.session.get(urljoin(self.base_url, f'/api/v2/remarketing/segments/{segment_id}.json'))
        return response.status_code

    def get_campaign_status(self, campaign_id):
        response = self.session.get(urljoin(self.base_url, f'/api/v2/campaigns/{campaign_id}.json?fields=issues'))
        return response.json().get('issues')[0]['code']
