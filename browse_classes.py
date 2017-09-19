import json 

f = open("imagenet_class_index.json","r")
class_index = json.loads(f.read())
class_to_wnid = {}
for i in range(1000):
    wnid, class_name = class_index[str(i)]
    class_to_wnid[class_name.lower()] = wnid
    
all_classes = class_to_wnid.keys()


query = raw_input("-->")
while query != "exit":
    search_results = list(filter(lambda x: query in x, all_classes))
    for r in search_results: 
        print "\n",r
    print "\n"
    query = raw_input("-->")
    
