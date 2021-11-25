import pytest
import faker
from base import ApiBase

fake = faker.Faker()


class TestApi(ApiBase):
    @pytest.mark.API('API')
    def test_create_campaign(self):
        campaign_id, campaign_status = ApiBase.create_campaign(self)
        assert campaign_status == "NO_ALLOWED_BANNERS"
        assert campaign_id in self.api_client.get_campaigns_id
        self.api_client.delete_campaign(campaign_id)

    @pytest.mark.API('API')
    def test_create_segment(self):
        segment_id = ApiBase.create_segment(self)
        segment_status_code = self.api_client.get_segment_status_code(segment_id)
        assert segment_status_code == 200
        assert segment_id in self.api_client.get_segments_id
        self.api_client.post_delete_segment(segment_id)

    @pytest.mark.API('API')
    def test_delete_segment(self):
        segment_id = ApiBase.create_segment(self)
        delete_segment_id = ApiBase.delete_segment(self, segment_id)
        segment_status_code = self.api_client.get_segment_status_code(delete_segment_id)
        assert segment_status_code == 404
        assert segment_id not in self.api_client.get_segments_id
