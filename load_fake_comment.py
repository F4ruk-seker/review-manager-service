import json
import random
from comment.models import CommentModel

data = open('fake_data.json', 'r', encoding='utf-8')

data = json.loads(data.read())

print('na')

for comment in data['text']:
    print(comment)
    tag = random.randint(1, 6)
    ai_tag = random.randint(1, 6)

    CommentModel.objects.create(
        ai_tag_id=ai_tag,
        tag_id=tag,
        text=comment,
        branch_from_id='50837cc1-d61b-43d4-b1d1-6adafa39dbab'
    )
