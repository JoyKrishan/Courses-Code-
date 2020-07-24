import xml.etree.ElementTree as ET
#data is a multi-line string
data='''
<person>
    <name>Joy Krishan</name>
    <phone type='intl'>
        +880 174 612 01 46
    </phone>
    <email hide='yes'/>
</person>'''

tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Email Hidden ?',tree.find('email').get('hide'))

data_2='''
<stuffs>
    <users>
        <user x='2'>
            <id>007</id>
            <name>Joy Krishan</name>
        </user>
        <user x="7">
            <id>002</id>
            <name>Dr Chuck</name>
        </user>
    </users>
</stuffs>'''

tree=ET.fromstring(data_2)
lst=tree.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name :',item.find('name').text)
    print('ID :',item.find('id').text)
