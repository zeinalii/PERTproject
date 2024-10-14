

import argparse
from models.show_graph import show_graph

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Show graph from Excel data file.")
    
    parser.add_argument("file_path", help="Path to the Excel data file")
    
    args = parser.parse_args()
    show_graph(args.file_path)