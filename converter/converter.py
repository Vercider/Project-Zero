import argparse
import glob

def get_file_names(folder_name):
    return glob.glob(folder_name + "*.xlsx")

if __name__ == '__main__':
    # set up parser
    parser = argparse.ArgumentParser(description='process excel files')
    parser.add_argument("folder_name", 
                        type=str, help="folder containing excel files")
    
    args = parser.parse_args()
    file_names = get_file_names(args.folder_name)
    
    print(file_names)
    
    print("done")