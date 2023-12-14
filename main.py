import os
import random
import datetime

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
raytracing = "MissingRaytracingInfo"
driver = "MissingDriverInfo"
upscaller = "MissingUpscalerInfo"
file_extension = "MissingFileExtensionInfo"
todays_date = datetime.date.today()

gpu_resolution_map = {
    'A380': '1080p',
    'A750': '1440p',
    'A770': '1440p',
    '4060': '1440p',
    '3060': '1440p'
}


def check_date(date):
    return datetime.date(date.year, date.month, date.day).isocalendar().week


def update_data():
    global capture_app, application_name, api, work_week

    print('Application name:')
    application_name = input()

    print('API:')
    api = input()


def create_random_file():
    template_name = "CX_2023-12-11_13-53-54_Starfield_"

    all_gpus = ["A380", "4060", "A750", "A770", "3060"]
    all_scenes = ["Mine", "Mars", "Lab", "NeonCity"]
    all_extra_settings = ["DLSS", "XeSS", "RT", ""]
    all_drivers = ["Base", "AIL", ""]

    random_extra_setting = random.choice(all_extra_settings)
    random_gpu = random.choice(all_gpus)
    random_scene_name = random.choice(all_scenes)
    random_run_number = random.randint(1, 5)
    random_driver = random.choice(all_drivers)

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


def check_extension(file_name):
    global file_extension
    file_extension = file_name.split('.')[1]

    if file_extension == "png":
        return "FPS"
    elif file_extension == "etl":
        return "ETL"
    elif file_extension == "lcs2":
        return "GFXBench"
    elif file_extension == "pix":
        return "PIX"
    else:
        return "Unknown"


def rename():
    global directoryContent, todays_date, upscaller, working_name, scene_name, run_number, gpu, old_file_directory, graphic_resolution, extra_comment, driver, capture_app, graphic_preset, work_week

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

            for gpu_name, resolution in gpu_resolution_map.items():
                if working_name.find(gpu_name) != -1:
                    gpu = gpu_name
                    graphic_resolution = resolution
                    is_raytracing_on()

            if gpu == "A380":
                graphic_preset = "High"
            elif working_name.find('High') != -1:
                graphic_preset = "High"
            elif working_name.find('Epic') != -1:
                graphic_preset = "Epic"
            elif working_name.find('VeryHigh') != -1:
                graphic_preset = "VeryHigh"
            else:
                graphic_preset = "Ultra"

            capture_app = check_extension(working_name)
            work_week = 'WW' + str(check_date(todays_date))

            old_file_directory = path + '/' + oldFile
            new_name = (path + '/' + capture_app + '_' + application_name + '_' + api + '_' + gpu + '_' + graphic_resolution + "_" + graphic_preset + not_empty(upscaller) + not_empty(raytracing) + '_' + scene_name + '_' + work_week + '_Run' + run_number + not_empty(driver) + '.png')
            os.rename(old_file_directory, new_name)


def not_empty(file):
    if file == "":
        return file
    else:
        file = "_" + file
        return file


test(1)
update_data()
rename()
