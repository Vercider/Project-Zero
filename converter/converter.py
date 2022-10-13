import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='process excel files')
    parser.add_argument("folder_name", type=str, help="folder containing excel files")
    args = parser.parse_args()
    
    print("done")