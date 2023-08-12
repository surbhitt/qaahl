#!/usr/bin/env python3

from collections import deque
import requests
import bs4
from sys import argv

# ----------------------------------------------------------------- modules
from classes import GraphNode
from visualization import draw 

# ----------------------------------------------------------------- global
base_url = ""
noted_links = set()

# ----------------------------------------------------------------- function
# make request to the url
def make_req(url: str):
    try: 
         res = requests.get(url)
         return res
    except Exception as err:
        print(f"[ERR] For {url=}:", err)
        return -1

# extracts the command line arguments
def handle_args():
    if (len(argv) < 2):
        print("-- No link passed")
        exit(1)
    
    flags = {"-d": "1"}
    base_url = "" 
    
    i = 1
    while i < len(argv):
        if argv[i].startswith("-"):
            flags[argv[i]] = argv[i+1]
            i+=1
        elif argv[i].startswith("http"):
            base_url = argv[i]
        else:
            print("[ERR] Argument unrecognised:", argv[i])
            exit(1)
        i+=1
    if base_url == "":
        print("-- No link passed")
        exit(1)

    return base_url, flags

# TODO: handle flags better and do something about it
def handle_flags():
    pass

# Entry Point ...
def main():
    global base_url, noted_links
    # extracting from commandline args
    base_url, flags = handle_args()
    # creating the base_head of the graph
    head_node = GraphNode(base_url)
    
    # =---> 
    node_queue = deque([[], [head_node]])
    depth = int(flags["-d"])

    while len(node_queue) !=0 and depth > 0:
        cur_depth_q = node_queue.pop()
        # TODO: secure this check
        if len(cur_depth_q) == 0:
            print("broke cause the cur_depth_q was empty")
            break
        cur_node = cur_depth_q.pop()
        print(f"traversing         {cur_node.rel_path=}")
        res = make_req(cur_node.rel_path)
        if (res == -1): continue
        res_txt = res.text
        res_parsed = bs4.BeautifulSoup(res_txt, 'html.parser')
        for anchor in res_parsed.find_all('a'):
            link = anchor.get('href')
            if link not in noted_links:
                noted_links.add(link)
                cur_node.paths.append(GraphNode(link))
            node_queue[0]+=cur_node.paths
        if len(cur_depth_q) != 0:
            node_queue.append(cur_depth_q)
        else:
             depth -= 1
             node_queue.appendleft([])
    draw(head_node) 
        
if __name__ == "__main__":
    main()

