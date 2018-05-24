import re
import get_nv_id
import os
import logging
logging.basicConfig( level=logging.ERROR)

nvidlist = []
nvitedic = {}
ans = input('''get nv id from:
[1]custom file
[2]source file\n''')
if ans == '1':
    with open('./customize/nvid.txt', 'r') as nvids:
        for nvid in nvids:
            nvid = nvid.strip('\n')
            nvidlist.append(nvid)
else:
    nvidlist = get_nv_id.main()

path = "./qcn_xmlfile"
files= os.listdir(path)
file = files[0]
with open('./qcn_xmlfile/' + file, 'r') as nv:
    for nvitem in nv:
        try:
            nvid_xml = str(re.findall(r'<NvItem id="(\d+)"', nvitem)[0])
            nvitedic[nvid_xml] = nvitem
        except IndexError as e:
            logging.warn('{} do not include nvid'.format(nvitem))
            continue


#export xml fileConfig
with open('./result.xml', 'w') as xmlfile:
    xmlfile.write('<NvSource>\n')
    for nvid in nvidlist:
        try:
            xmlfile.write(nvitedic[nvid])
        except KeyError as e:
            logging.error('no found this nvid:{0}'.format(nvid))
            input()
            continue
    xmlfile.write('</NvSource>')



