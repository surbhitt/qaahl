#!/usr/bin/env python3

from collections import deque
import requests
import bs4
from sys import argv

from classes import GraphNode
from visualization import draw 


base_url = ""

def make_req(url: str):
    try: 
         res = requests.get(url)
         return res
    except Exception as err:
        print(f"[ERR] For {url=}:", err)
        return -1

def build_url(url: str):
    if not url:
        print(f"DONT KNOW")
        return (base_url)
    if url.startswith("."):
        print(f"adding %s" %(base_url+url[2:]))
        return base_url+url[2:]
    print(f"adding %s" %url)
    return url

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

def handle_flags():
    pass

def main():
    global base_url
    base_url, flags = handle_args()
    head = GraphNode(base_url)
    url_queue = deque([[], [head]])
    depth = int(flags["-d"])
    while len(url_queue) !=0 and depth > 0:
        cur_depth_q = url_queue.pop()
        if len(cur_depth_q) == 0:
            print("broke cause the cur_depth_q was empty")
            break
        cur_url = cur_depth_q.pop()
        print(f"traversing         {cur_url.url=}")
        res = make_req(cur_url.url)
        if (res == -1): continue
        res_txt = res.text
        res_parsed = bs4.BeautifulSoup(res_txt, 'html.parser')
        for anchor in res_parsed.find_all('a'):
            constructed_url = build_url(anchor.get('href'))
            cur_url.paths.append(GraphNode(constructed_url))
            url_queue[0]+=cur_url.paths
        if len(cur_depth_q) != 0:
            url_queue.append(cur_depth_q)
        else:
             depth -= 1
             url_queue.appendleft([])
    draw(head) 
        
if __name__ == "__main__":
    main()

