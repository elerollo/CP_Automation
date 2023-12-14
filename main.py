import os
import random
from FPS_tool import *
from STREAM_tool import *

capture_app = "MissingCaptureAppInfo"
application_name = "MissingApplicationNameInfo"
api = "MissingApiInfo"
work_week = "MissingWorkWeekInfo"
gpu = "MissingGPUInfo"
path = r"/Users/erykvest/Desktop/Test"
directoryContent = []
working_name = "MissingNameData"
scene_name = "MissingSceneInfo"
run_number = "MissingRunNumber"
old_file_directory = "NoData"
graphic_preset = "MissingPreset"
graphic_resolution = "MissingResolution"
raytracing = ""
driver = ""
upscaller = ""

def update_data():
    global capture_app, application_name, api, work_week

    print('Capture app:')
    capture_app = input()

    print('Application name:')
    application_name = input()

    print('API:')
    api = input()

    print('Workweek:')
    work_week = input()

def create_random_file():
    template_name = "CX_2023-12-11_13-53-54_Starfield_"

    all_gpus = ["A380", "4060", "A750", "A770", "3060"]
    all_scenes = ["Mine", "Mars", "Lab", "NeonCity"]
    all_extra_settings = ["DLSS", "XeSS", "RT", ""]
    all_drivers = ["Base", "AIL", ""]

    random_extra_setting = all_extra_settings[random.randint(0, 3)]
    random_gpu = all_gpus[random.randint(0, 4)]
    random_scene_name = all_scenes[random.randint(0, 3)]
    random_run_number = random.randint(1, 5)
    random_driver = all_drivers[random.randint(0, 2)]

    template_name = template_name + random_gpu + "_" + random_scene_name + "_" + str(random_run_number) + not_empty(random_extra_setting) + not_empty(random_driver) + ".png"
    return template_name


def test(number_of_files):
    global path

    for number in range(number_of_files):
        random_file = open(path + "/" + create_random_file(), 'w')
        random_file.close()

def is_raytracing_on():
    global graphic_resolution, raytracing

    if working_name.find('RT') != -1:
        graphic_resolution = "1080p"
        raytracing = "RT"
    else:
        raytracing = ""

def rename():
    global directoryContent, upscaller, working_name, scene_name, run_number, gpu, old_file_directory, graphic_resolution, extra_comment, driver

    directoryContent = os.listdir(path)

    for oldFile in directoryContent:
        if oldFile.split('_')[0] == "CX":
            working_name = oldFile
            working_name_data = working_name.split("_")
            scene_name = working_name_data[5]
            run_number = working_name_data[6]

            if working_name.find('Base') != -1:
                driver = "Base"
            elif working_name.find('AIL') != -1:
                driver = "AIL"
            else:
                driver = ""

            if working_name.find('XeSS') != -1:
                upscaller = "XeSS"
            elif working_name.find('DLSS') != -1:
                upscaller = "DLSS"
            else:
                upscaller = ""

            if working_name.find('A380') != -1:
                gpu = "A380"
                graphic_resolution = "1080p"
            elif working_name.find('A750') != -1:
                gpu = "A750"
                graphic_resolution = "1440p"
            elif working_name.find('A770') != -1:
                gpu = "A770"
                graphic_resolution = "1440p"
            elif working_name.find('4060') != -1:
                gpu = "4060"
                graphic_resolution = "1440p"
            elif working_name.find('3060') != -1:
                gpu = "3060"
                graphic_resolution = "1440p"
            else:
                gpu = "MissingGPUInfo"

            is_raytracing_on()

            if gpu == "A380":
                graphic_preset = "High"
            else:
                graphic_preset = "Ultra"


            old_file_directory = path + '/' + oldFile
            new_name = (path + '/' + capture_app + '_' + application_name + '_' + api + '_' + gpu + '_' + graphic_resolution + "_" + graphic_preset + not_empty(upscaller) + not_empty(raytracing) + '_' + scene_name + '_' + work_week + '_Run' + run_number + not_empty(driver) + '.png')
            os.rename(old_file_directory, new_name)
            print(capture_app, application_name, api, work_week, scene_name, run_number, graphic_preset, graphic_resolution, raytracing, driver, upscaller, gpu)
# gpu
# # path
# # directoryContent = []
# # old_file_directory = "NoData"
# graphic_preset = "MissingPreset"


def not_empty(file):
    if file == "":
        return file
    else:
        file = "_" + file
        return file
test(12)
update_data()
rename()

