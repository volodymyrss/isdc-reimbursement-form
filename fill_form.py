import subprocess
import yaml 
import json
import sys

import argparse


def process(input,output,fields,scale=1):
    command=[
        "convert",
        "-density",'%.5lg'%(scale*100),
        input+"[0]"
        ]

    for x,y,text in fields:
        command+=["-pointsize","10",
            "-gravity","NorthWest",
            "-annotate","+%.5lg+%.5lg"%(x*scale,y*scale),text]

    command+=["-quality","100",
        "-sharpen","0x1.0",
        output]

    p=subprocess.Popen(command)
    p.wait()

def line_fields():
    fields=[]
    fields+=[(x*30,10,str(x*30)) for x in range(100)]
    fields+=[(10,x*20,str(x*20)) for x in range(100)]
    return fields

def load_form_map():
    try:
        return json.load(open("form_map.json"))
    except:
        return yaml.load(open("form_map.yaml"))


def load_data(files):
    form_data={}
    for fd in files:
        try:
            d=json.load(open(fd))
        except:
            d=yaml.load(open(fd))
        form_data.update(d)

    return form_data


def fill_fields(fields,form_map,form_data):
    for k,v in form_map.items():
        print("field",k,v)
        if k in form_data:
            fields.append([v[0],v[1],str(form_data[k])])


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-l", "--lines", help="data",
                    action="store_true")
parser.add_argument("-d", "--data", help="data",
                    action="append")
parser.add_argument("-i", "--input", help="data")
parser.add_argument("-o", "--output", help="data")
parser.add_argument("-s", "--scale", help="data")
args = parser.parse_args()


if args.lines:
    fields=line_fields()
else:
    fields=[]

form_data=load_data(args.data)
print(form_data)

form_map=load_form_map()

fill_fields(fields,form_map,form_data)

process(input=args.input,output=args.output,fields=fields,scale=float(args.scale))
