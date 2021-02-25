# Day 7 - Bubble sorting

user_boxes = {'weight': [4,2,18,21,14,13],
              'box_name': ['box1','box2', 'box3', 'box4', 'box5', 'box6']
             }


def sort_box(user_boxes):
  weight = user_boxes["weight"]
  box = user_boxes["box_name"]
  box_sorted = []
  for i in range(len(weight)):
    for j in range(len(weight)-1):
      if weight[j] > weight[j+1]:
        value = weight[j]
        value1 = box[j]
        weight[j] = weight[j+1]
        box[j] = box[j+1]
        weight[j+1] = value
        box[j+1] = value1
  print(weight,box)

sort_box(user_boxes)