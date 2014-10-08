import csv
import sys
import json

main_categories = {}

with open(sys.argv[1],"rU") as f:
	reader = csv.reader(f, delimiter=',')
	next(reader)

	for row in reader:
		main_category = row[0]
		sub_category = row[1]
		sentence = row[2]

		main_category_object = main_categories.get(main_category, {"name" : main_category})
		main_categories[main_category] = main_category_object
		if (sub_category == ""):
			main_category_object["sentences"] = main_category_object.get("sentences", [])
			main_category_object["sentences"].append(sentence)
		else:
			sub_category_object = main_category_object.get(sub_category, {"name" : sub_category, "sentences":[]})
			main_category_object[sub_category] = sub_category_object
			sub_category_object["sentences"].append(sentence)
			#sub_category_object["size"] = len(sub_category_object["sentences"])

main_categories_list = []
for main_category, main_category_object in main_categories.iteritems():
	main_category_children = []
	if ("sentences" in main_category_object):
		main_categories_list.append({"name" : main_category, "sentences" : main_category_object["sentences"]})
	else:
		for sub_category, sub_category_object in main_category_object.iteritems():
			if (isinstance(sub_category_object, basestring)):
				continue
			main_category_children.append(sub_category_object)
		main_categories_list.append({"name" : main_category, "children" : main_category_children})

super_main_category = {"name" : "analytics", "children" : main_categories_list}
print json.dumps(super_main_category, indent=4, sort_keys=True)
