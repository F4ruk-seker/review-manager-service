import json
import random
from comment.models import CommentModel

data = open('fake_data.json', 'r', encoding='utf-8')

data = json.loads(data.read())


for comment in data['text']:
    tag = random.randint(13, 18)
    ai_tag = random.randint(13, 18)

    CommentModel.objects.create(
        ai_tag_id=ai_tag,
        tag_id=tag,
        text=comment,
        branch_from_id='661f8f98-8e4b-47ce-9076-d203ac6c5d81'
    )
