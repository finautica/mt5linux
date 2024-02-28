from rpyc.utils.classic import DEFAULT_SERVER_PORT, DEFAULT_SERVER_SSL_PORT
import os
from subprocess import Popen
import argparse


def main():
    parser = argparse.ArgumentParser(description='Create Server.')
    parser.add_argument('--host', type=str, default='localhost',
                        help='The host to connect to. The default is localhost')
    parser.add_argument('-p', '--port', type=int, default=DEFAULT_SERVER_PORT,
                        help=f'The TCP listener port (default = {DEFAULT_SERVER_PORT!r}, default for SSL = {DEFAULT_SERVER_SSL_PORT!r})')
    args = parser.parse_args()

    # Construct the path to the adjacent file
    server_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "server.py")

    Popen([
        "python",
        server_path,
        '--host',
        args.host,
        '-p',
        str(args.port),
    ], shell=True,
    ).wait()


if __name__ == '__main__':
    main()
