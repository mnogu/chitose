from datetime import datetime
import json

from chitose import BskyAgent
from chitose import Blob
from chitose import Link
from chitose.app.bsky.feed.post import Post
from chitose.app.bsky.embed.images import Image
from chitose.app.bsky.embed.images import Images


# Replace YOUR_USERNAME, YOUR_PASSWORD, YOUR_IMAGE_PATH AND YOUR_DID
def main():
    agent = BskyAgent(service='https://bsky.social')
    agent.login(identifier='YOUR_USERNAME', password='YOUR_PASSWORD')

    with open('YOUR_IMAGE_PATH', 'rb') as in_f:
        res = agent.com.atproto.repo.upload_blob(in_f.read())

    d = json.loads(res)['blob']
    ref = Link(link=d['ref']['$link'])
    blob = Blob(ref=ref, mime_type=d['mimeType'], size=d['size'])

    image = Image(image=blob, alt='example')

    images = Images(images=[image])

    record = Post(text='post with an image test',
                  created_at=datetime.now().isoformat(), embed=images)
    agent.com.atproto.repo.create_record(
        repo='YOUR_DID', collection='app.bsky.feed.post', record=record)


if __name__ == "__main__":
    main()
