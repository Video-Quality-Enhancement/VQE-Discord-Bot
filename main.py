import os
from dotenv import load_dotenv
from bot import MyClient

def main():
    load_dotenv()
    client = MyClient()
    client.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    main()
