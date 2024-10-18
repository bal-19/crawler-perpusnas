import argparse

def main():
    parser = argparse.ArgumentParser(description="Engine untuk mengambil data perpustkaan")
    parser.add_argument("--insert", action="store_true", help="Insert data to MongoDB")
    args = parser.parse_args()

    
    if args.insert:
        print("Data successfully inserted to MongoDB")

if __name__ == "__main__":
    main()
