class_dart = '''
  String name;
  String type;
  int duration;
  double calories;
  int reps;
  double weight;
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
    "int":"int",
    "bool":"bool"
}

for item in class_split:
    if(item_type==None):
        item_type = type_conversion[item]
    else:
        item_name = item

        class_python += "{}: {}\n".format(item_name[:-1], item_type)

        item_type = None

print(class_python)
