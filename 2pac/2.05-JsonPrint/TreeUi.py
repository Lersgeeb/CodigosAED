class TreeUl:

    def __init__(self):
        pass

    def convert(self,json,filename = "2pac//2.05-JsonPrint//index.html"):
        html = self.innerConvert(json)
        f = open(filename,"w")
        f.write(html)
        f.close()

    def innerConvert(self,json):
        html = ["<ul>"]
        for k,v in json.items():
            if(isinstance(v,dict)):
                html.append("<li>%s" % (k,))
                html.append(self.innerConvert(v))
                html.append("</li>")
            else:
                #html.append("<li>%s</li>"  % (v,))    
                html.append("<li>%s : %s</li>"  % (k,v))    
        html.append("</ul>")
        return "".join(html)
            

dct = { 
    "Root/":{ 
        "directorio1/":{
            "type":"folder",
            "date":"2019",
            "user":"myPc",
            "children":{
                "archive1":{
                    "type":"archive",
                    "extension":"mp3",
                    "date":"2019"},
                "dir1/":{
                    "type":"folder",
                    "date":"2019",
                    "user":"myPc",
                    "children":{
                        "archive1":{
                        "type":"archive",
                        "extension":"mp3",
                        "date":"2019"},
                        "archive2":{     
                        "type":"archive",
                        "extension":"mp4",
                        "date":"2019"}       
                    }   
                }
            }
        }, 
        "directorio2/":{
            "type":"folder",
            "date":"2019",
            "user":"myPc",
            "children":{}
        }, 
        "arvhivo1":{
            "type":"archive",
            "extension":"mp4",
            "date":"2019"
        }
    } 
}

dct2 = {"root/":{"Dir1/":{"Dir2/":{"Archive":{"size":200,"date":"2019"}},"Archive":{"size":200,"date":"2019"}}}}
t = TreeUl()
t.convert(dct2)
