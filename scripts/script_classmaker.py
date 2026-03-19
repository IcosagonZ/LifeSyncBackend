class_dart = '''
  String name;
  String form;
  String type;
  double qty;
  double calories;
  double mass;
  double carbs;
  double protein;
  double fats;
  DateTime entry_date;
  String entry_note;
'''

class_split = class_dart.split()

class_python = ""

item_type = None
item_name = None

type_conversion = {
    "String":"str",
    "DateTime":"str",
    "double":"float",
    "int":"int"
}

for item in class_split:
    if(item_type==None):
        item_type = type_conversion[item]
    else:
        item_name = item

        class_python += "{}: {}\n".format(item_name[:-1], item_type)

        item_type = None

print(class_python)
