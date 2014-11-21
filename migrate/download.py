import csv
import wget
import subprocess

with open('resources.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        uuid = row[1]
        owner = row[2]
	command = "geonode importlayers -v 3 -u %s %s.*" % (owner, name)
	print command
	print subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
    #download_url = "http://ebolageonode.org/geoserver/wfs?format_options=charset%3AUTF-8&typename=geonode%3A" + name + "&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature"
    #print download_url
    #metadata_url = "http://ebolageonode.org/catalogue/csw?outputschema=http%3A%2F%2Fwww.isotc211.org%2F2005%2Fgmd&service=CSW&request=GetRecordById&version=2.0.2&elementsetname=full&id=" + uuid
    #wget.download(download_url, out=(name + ".zip"), bar=wget.bar_thermometer)
    #wget.download(metadata_url, out=(name + ".shp.xml"))
