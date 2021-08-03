from cascade import asset
from cascade.util import resizer
import os
import pandas as pd
import requests
import threading
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)
spotlights = []


def load_csv(csv, t="student"):
    df = pd.read_csv(csv)
    spotlights = df.to_dict('records')
    for spotlight in spotlights:
        if t == "student":
            generate_student_spotlight(spotlight)
        elif t == "donor":
            generate_donor_spotlight(spotlight)
        elif t == "alumni":
            generate_alumni_spotlight(spotlight)


def create_images(image, path, site='semo playground'):
    if image is None or isinstance(image, float):
        return None

    img = {
        'mobile': {

        },
        'desktop': {

        },
        'path': path
    }

    img['mobile']['name'] = resizer.resize_image(image, 'mobile')
    img['desktop']['name'] = resizer.resize_image(image, 'desktop')

    img['mobile']['asset'] = asset.create_image(img['mobile']['name'], img['mobile']['name'].lower(), path, site)
    img['desktop']['asset'] = asset.create_image(img['desktop']['name'], img['desktop']['name'].lower(), path, site)

    img['mobile']['id'] = asset.upload_asset(img['mobile']['asset'], "jtrenaud1s", "**Circle19699**")
    img['desktop']['id'] = asset.upload_asset(img['desktop']['asset'], "jtrenaud1s", "**Circle19699**")

    task = threading.Thread(target=delete_file, args=(img['mobile']['name'],))
    task.start()

    task = threading.Thread(target=delete_file, args=(img['desktop']['name'],))
    task.start()

    task = threading.Thread(target=delete_file, args=(image,))
    task.start()

    return img


def delete_file(file):
    scheduler.enter(10, 1, os.remove, (file,))
    scheduler.run()


def generate_student_spotlight(spotlight):
    skip = ['Entry Id', 'Name', 'Last', 'Email address:', 'Home: City, State',
            'Program/Major', 'Year in School', 'Please share a photo of college life.',
            'Date Created', 'Created By', 'Last Updated', 'Updated By',
            'IP Address', 'Last Page Accessed', 'Completion Status']

    html = ""

    for key, value in spotlight.items():
        if key not in skip and not isinstance(value, float):
            html += f"<p><strong>{str(key).strip()}</strong></p>" \
                    f"<p>{str(value).strip()}</p>"

    first = str(spotlight['Name']).strip().capitalize()
    last = str(spotlight['Last']).strip().capitalize()
    title = str(spotlight['Year in School']).strip().capitalize()
    department = [str(spotlight['Program/Major']).strip()]
    roles = ['Other']
    email = str(spotlight['Email address:']).strip()
    hometown = str(spotlight['Home: City, State']).strip()
    image = spotlight['Please share a photo of college life.'] or None

    print(first, last)

    if not isinstance(image, float):
        img_data = requests.get(image.strip()).content
        with open(first + "-" + last + ".jpg", 'wb') as handler:
            handler.write(img_data)
            image = first + "-" + last + ".jpg"
    else:
        image = None

    page = create_spotlight("_testing/student-spotlights", first, last, title, roles, department, image, "", email, hometown, data=html)
    response = asset.upload_asset(page.page.to_dict(), "jtrenaud1s", "**Circle19699**")


def generate_donor_spotlight(spotlight):
    html = ""

    skip = ['Entry Id', 'Name', 'Last', 'Email', 'Phone Number',
            'Address', 'Address Line 2', 'City', 'State / Province / Region', 'Postal / Zip Code', 'Country',
            'Date Created', 'Created By', 'Last Updated', 'Updated By',
            'IP Address', 'Last Page Accessed', 'Completion Status']

    for key, value in spotlight.items():
        if key not in skip and not isinstance(value, float):
            html += f"<p><strong>{str(key).strip()}</strong></p>" \
                    f"<p>{str(value).strip()}</p>"

    first = str(spotlight['Name']).strip().capitalize()
    last = str(spotlight['Last']).strip().capitalize()
    email = str(spotlight['Email']).strip()
    phone = str(spotlight['Phone Number']).strip()
    address_1 = f"{spotlight['Address']}".strip()
    optional = f"{spotlight['Address Line 2']}<br />"
    address_2 = f"{spotlight['City']}, {spotlight['State / Province / Region']} {spotlight['Postal / Zip Code']}<br />{spotlight['Country']}"

    if not isinstance(spotlight['Address Line 2'], float):
        address_2 = optional + address_2

    print(first, last)

    page = create_donor_spotlight("_testing", first, last, phone, email, address_1, address_2, data=html)
    response = asset.upload_asset(page.page.to_dict(), "jtrenaud1s", "**Circle19699**")


def create_donor_spotlight(path, first, last, phone, email, address_1, address_2, prefix='',
                           middle='', suffix='', office_hours='', data=''):
    return asset.donor_spotlight(path,
                                 first.lower() + '-' + last.lower(),
                                 first, last,
                                 phone, email, address_1, address_2, middle=middle, suffix=suffix,
                                 data=data)


def generate_alumni_spotlight(spotlight):
    html = ""

    skip = ['Entry Id', 'Name', 'Last', 'Grad Year', 'Email address:', 'Phone Number', 'Employer', 'Job Title',
            'Address', 'Address Line 2', 'City', 'State / Province / Region', 'Postal / Zip Code', 'Country',
            'Date Created', 'Created By', 'Last Updated', 'Updated By', 'Attach a Photo',
            'IP Address', 'Last Page Accessed', 'Completion Status']

    for key, value in spotlight.items():
        if key not in skip and not isinstance(value, float):
            html += f"<p><strong>{str(key).strip()}</strong></p>" \
                    f"<p>{str(value).strip()}</p>"

    first = str(spotlight['Name']).strip().capitalize()
    last = str(spotlight['Last']).strip().capitalize()
    email = str(spotlight['Email address:']).strip()
    year = str(spotlight['Grad Year']).strip()
    title = str(spotlight['Job Title']).strip()
    employer = str(spotlight['Employer']).strip()
    address_1 = f"{spotlight['Address']}".strip()
    image = spotlight['Attach a Photo']
    optional = f"{spotlight['Address Line 2']}<br />"
    address_2 = f"{spotlight['City']}, {spotlight['State / Province / Region']} {spotlight['Postal / Zip Code']}<br />{spotlight['Country']}"

    if not isinstance(spotlight['Address Line 2'], float):
        address_2 = optional + address_2

    if not isinstance(image, float):
        img_data = requests.get(image.strip()).content
        with open(first + "-" + last + ".jpg", 'wb') as handler:
            handler.write(img_data)
            image = first + "-" + last + ".jpg"
    else:
        image = None


    print(first, last)

    page = create_alumni_spotlight("_testing/alumni-spotlights", first, last, year, title, employer, email, address_1, address_2, image,
                                   data=html)
    response = asset.upload_asset(page.page.to_dict(), "jtrenaud1s", "**Circle19699**")
    print(response)


def create_alumni_spotlight(path, first, last, year, title, employer, email, address_1, address_2, image, prefix='',
                            middle='', suffix='', office_hours='', data=''):
    images = create_images(image, path + "/_images")

    return asset.alumni_spotlight(path,
                                  first.lower() + '-' + last.lower(),
                                  first, last, year, title, employer,
                                  email, address_1, address_2,
                                  True if image is not None else False,
                                  images['mobile']['id'] if images is not None else '',
                                  images['desktop']['id'] if images is not None else '',
                                  ("Profile Image for " + first + " " + last) if images is not None else '',
                                  middle=middle, suffix=suffix,
                                  data=data)


def create_spotlight(path, first, last, title, roles, departments, image, phone='', email='', hometown='', prefix='', middle='',
                     suffix='', office_hours='', data=''):
    images = create_images(image, path + "/_images")


    """
    path, name, first, last, roles, departments, phone, email, image, image_mobile_id, image_desktop_id, image_alt
    
    """

    return asset.student_spotlight(path,
                                   first.lower() + '-' + last.lower(),
                                   first, last, roles, departments,

                                   True if image is not None else False,
                                   images['mobile']['id'] if images is not None else '',
                                   images['desktop']['id'] if images is not None else '',
                                   ("Profile Image for " + first + " " + last) if images is not None else '',
                                   prefix=prefix, middle=middle, suffix=suffix,
                                   office_hours=office_hours, data=data)


load_csv("spotlights.csv", "student")
load_csv("donors.csv", "donor")
load_csv("alumni.csv", "alumni")
