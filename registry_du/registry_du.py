#!/usr/bin/env python3
import sys
import os
import json
from terminaltables import AsciiTable

def walk_through_repo(path):

    image_with_size_dict = {}
    project_with_size_dict = {}

    repositories_path = path + "/repositories/"
    for (dirpath, dirnames, filenames) in os.walk(repositories_path):
        for dirname in dirnames:
            if "current" in dirname:
                
                image_with_tag = dirpath.replace(repositories_path,"").replace('/_manifests/tags/',":")

                image_manifest_file = dirpath + "/" + dirname + "/link"
                with open(image_manifest_file,"r") as f:
                   manifest_hash = f.readline().split(":")[1]

                manifest_json_path = path + "/blobs/sha256/" + manifest_hash[0:2] + "/" + manifest_hash + "/data"
                
                image_size_byte = 0
                try:
                    with open(manifest_json_path,"r") as f:
                        manifest_json = json.load(f)
                    try:
                        for layer in manifest_json['layers']:
                            image_size_byte += int(layer['size']) 
                    except:
                        pass
                except:
                    pass

                image_with_size_dict[image_with_tag] = image_size_byte


                project_name = image_with_tag.split('/',1)[0]
                if project_name in project_with_size_dict:
                    project_with_size_dict[project_name] += image_size_byte
                else:
                    project_with_size_dict[project_name] = image_size_byte
                

    return project_with_size_dict,image_with_size_dict


def main():
    registry_path = sys.argv[1]

    print("Registry Path is: " + registry_path)
    project_with_size_dict,image_with_size_dict = walk_through_repo(registry_path)

    project_with_size_dict = {k: v for k, v in sorted(project_with_size_dict.items(), key=lambda item: item[1])}
    image_with_size_dict =  {k: v for k, v in sorted(image_with_size_dict.items(), key=lambda item: item[1])}

    project_table_data = []
    for key,value in project_with_size_dict.items():
        project_table_data.append([key,round(value/(1024*1024),2)])
    project_table_data.reverse()
    project_table_data.insert(0,['Project Name','Size(MiB)'])

    image_table_data = []
    for key,value in image_with_size_dict.items():
        image_table_data.append([key,round(value/(1024*1024),2)])
    image_table_data.reverse()
    image_table_data.insert(0,['Image Name','Size(MiB)'])
    image_table_data = image_table_data[0:20]

    project_table = AsciiTable(project_table_data)
    project_table.title = 'Project-Size'
    print(project_table.table)

    image_table = AsciiTable(image_table_data)
    image_table.title = 'Image-Size'
    print(image_table.table)