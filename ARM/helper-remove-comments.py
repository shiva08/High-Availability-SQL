import json5
import json

a = 'nested'
jsonfile = open(a +'.json', 'r')

content = json5.load(jsonfile)

f = open(a + '-no-comments.json','w' )
f.write(json.dumps(content, indent=4))


jsonfile.close()
f.close()
