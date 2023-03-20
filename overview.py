from tabulate import tabulate

data = [
    ["Sensor Data", "Lidar Data"],
    ["Sensor Data", "Camera Data"],
    ["Maps", "Maps"],
    ["Format", "Modular Dataset"],
    ["Labels", "3D Bounding Boxes"],
    ["Labels", "2D Bounding Boxes"],
    ["Labels", "Key Points"],
    ["Labels", "2D-to-3D Correspondence"],
    ["Labels", "3D Semantic Segmentation"],
    ["Labels", "2D Video Panoptic Segmentation"],

]

headers = ["Name", "Type"]

print(tabulate(data, headers=headers, tablefmt="grid"))
