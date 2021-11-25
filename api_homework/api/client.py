from urllib.parse import urljoin
import requests
import api.credits as credits


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.csrf_token = None
        self.session = requests.Session()

    def post_login(self, email, password):
        headers = {
            'Referer': self.base_url
        }

        data = {
            'email': email,
            'password': password,
            'continue': credits.data_login_continue_url
        }
        self.session.post(credits.login_url, headers=headers, data=data,
                          allow_redirects=True)
        self.csrf_token = self.get_token()

    def get_token(self):
        csrf_token = self.session.get(credits.csrf_token_url).cookies.get('csrftoken')
        return csrf_token

    def post_upload_image(self, image):
        file = {
            'file': open(image, 'rb'),
        }
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        response = self.session.post(credits.upload_image_url, headers=headers, files=file)
        return response

    def get_url_id(self, url):
        response = self.session.get(urljoin(self.base_url, f'/api/v1/urls/?url={url}'))
        return response

    def post_create_campaign(self, name, image_id, url_id, objective='traffic', package_id=961):
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        json = {
            "banners": [{"content": {"image_240x400": {"id": image_id}}, "urls": {"primary": {"id": url_id}}}],
            "name": name,
            "objective": objective, "package_id": package_id
        }
        response = self.session.post(credits.campaigns_url, headers=headers, json=json)
        return response

    def delete_campaign(self, campaign_id):
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        response = self.session.delete(urljoin(self.base_url, f'api/v2/campaigns/{campaign_id}.json'), headers=headers)
        assert response.status_code == 204
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
        response = self.session.post(credits.segments_url,
                                     headers=headers, json=json)
        return response

    def post_delete_segment(self, segment_id, source_type='segment'):
        headers = {
            'X-CSRFToken': self.csrf_token
        }
        json = [{"source_id": segment_id, "source_type": source_type}]
        response = self.session.post(credits.delete_segments_url,
                                     headers=headers, json=json)
        return response

    def get_segment_status_code(self, segment_id):
        response = self.session.get(urljoin(self.base_url, f'/api/v2/remarketing/segments/{segment_id}.json'))
        return response.status_code

    def get_campaign_status(self, campaign_id):
        response = self.session.get(urljoin(self.base_url, f'/api/v2/campaigns/{campaign_id}.json?fields=issues'))
        assert response.status_code == 200
        return response.json().get('issues')[0]['code']

    @property
    def get_segments_id(self):
        res = self.session.get(credits.segments_url)
        return [x['id'] for x in res.json()['items']]

    @property
    def get_campaigns_id(self):
        res = self.session.get(urljoin(credits.campaigns_url, '?limit=250')).json()
        return [x['id'] for x in res['items']]
