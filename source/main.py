import argparse
import asyncio

if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("-c", "--config", dest="config", type=str, default="config.ini")
    argp.add_argument("-d", "--destination", dest="destination", type=str)
    argp.add_argument("-o", "--output", dest="output", type=str)

    argp_sub = argp.add_subparsers(title="action", help="-h / --help to see usage")

    argp_crawler = argp_sub.add_parser("crawler")
    argp_crawler.set_defaults(which="crawler")
    argp_crawler.add_argument("--mode", dest="mode", type=str)
    argp_crawler.add_argument("--type", dest="type", type=str)

    args = argp.parse_args()
    if args.which == "crawler":
        if args.mode == "perpusnas":
            if args.type == "get_perpustakaan":
                from controllers.perpusnas.get_perpustakaan import PerpusnasGetPerpustakaan

                c = PerpusnasGetPerpustakaan(**args.__dict__)
                asyncio.run(c.main())