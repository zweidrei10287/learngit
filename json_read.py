import os,sys
import cv2
import json

json_path = 'path/data_000001.json'
img_path = 'path/data_000001'

# json file read
json_lines = open(json_path,'r').readlines()
for line in json_lines:
    # json dict read
    json_dict = json.loads(line)
    # confirm image path & opencv read
    image_url = os.path.join(img_path,json_dict['image_key'])
    #print(image_url)
    img = cv2.imread(image_url)
    # read label info
	if "vehicle" in json_dict:
		rects = json_dict['vehicle']
		for rect in rects:
		#for idx,rect in enumerate(rects):
			#print ("idx: ",idx,"########","rect:",rect)
			bbox = rect['data']
			#print(bbox)
			#print((int(bbox[0]),int(bbox[1])),(int(bbox[2]),int(bbox[3])))
			#print ("id: " ,id)
			#print ("rects: ",rects)
			#bbox = id[4]
			# draw label on img
			#print(rect['attrs'])
			labels_x = min(bbox[0],bbox[2])
			labels_y = min(bbox[1],bbox[3])
			labels_dict = rect['attrs']
			offset = 0
			for item in labels_dict.items():
				key = item[0]
				value = item[1]
			#labels = open(labels_dict).readline()
				cv2.putText(img, str(key) + ':' + str(value), (int(labels_x),int(labels_y)+offset), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
				offset = offset + 20
			#labels = json.dumps(rect['attrs'])
			#print(labels)
			cv2.rectangle(img,(int(bbox[0]),int(bbox[1])),(int(bbox[2]),int(bbox[3])),(0,255,0),2)
		# show img
		#cv2.imshow('fff',img)
		#print img on screen
		cv2.imwrite("/home/zhouyuchuan/data/result/"+json_dict['image_key'],img) #save
