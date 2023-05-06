from chitose.agent import BskyAgent


def main():
    agent = BskyAgent(service='https://bsky.social')
    agent.login(identifier='YOUR_USERNAME', password='YOUR_PASSWORD')
    print(agent.app.bsky.actor.get_profiles(
        actors=['ONE_USERNAME', 'ANOTHER_USERNAME']))


if __name__ == "__main__":
    main()
