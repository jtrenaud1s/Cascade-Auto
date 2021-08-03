from cascade.util.helper import img_to_cascade
import requests

from cascade.page.AlumniSpotlight import AlumniSpotlight
from cascade.page.DonorSpotlight import DonorSpotlight
from cascade.page.StudentSpotlight import StudentSpotlight


def create_image(image, name, path, site):
    return {
        "asset": {
            "file": {
                "data": img_to_cascade(image),
                'rewriteLinks': False,
                'linkRewriting': 'inherit',
                'shouldBePublished': True,
                'shouldBeIndexed': True,
                'expirationFolderRecycled': False,
                'metadataSetId': '80f05dbd96c98f631dc310cc38be26a9',
                'metadataSetPath': 'Default',
                'metadata': {
                    'displayName': '',
                    'title': '',
                    'summary': '',
                    'teaser': '',
                    'keywords': '',
                    'metaDescription': '',
                    'author': ''
                },
                'reviewOnSchedule': False,
                'reviewEvery': 180,
                'parentFolderPath': path,
                'siteName': site,
                'tags': [],
                'name': name,
            }
        }
    }


def student_spotlight(path, name, first, last, roles, departments,  image, image_mobile_id,
                      image_desktop_id, image_alt, phone='', email='', address='', address_line_2='', city='', state='', zip_code='',
                      country='', prefix='', middle='', suffix='', office_hours='', data=''):
    page_data = {
        'path': path,
        'name': name,
        'first': first.capitalize(),
        'last': last.capitalize(),
        'roles': roles,
        'departments': departments,
        'phone': phone,
        'title': 'Student',
        'email': email,
        'address': address,
        'address_line_2': address_line_2,
        'image': image,
        'image_mobile_id': image_mobile_id,
        'image_desktop_id': image_desktop_id,
        'image_alt': image_alt,
        'city': city,
        'state': state,
        'zip': zip_code,
        'country': country,
        'prefix': prefix,
        'middle': middle,
        'suffix': suffix,
        'office_hours': office_hours,
        'data': data
    }
    return StudentSpotlight('bf5d4def96c98f63204015ee6b5e8220', '_testing/student-spotlights', '80efea1596c98f631dc310ccfb483f98',
                            data=page_data)


def donor_spotlight(path, name, first, last, phone, email, address_1, address_2, prefix='', middle='', suffix='', data=''):
    page_data = {
        'path': path,
        'name': name,
        'first': first,
        'last': last,
        'phone': phone,
        'email': email,
        'prefix': prefix,
        'middle': middle,
        'suffix': suffix,
        'address_1': address_1,
        'address_2': address_2,
        'office_hours': '',
        'data': data
    }

    return DonorSpotlight('bf7319df96c98f63204015ee75e83832', '_testing/donor-spotlights', '80efea1596c98f631dc310ccfb483f98',
                          data=page_data)

def alumni_spotlight(path, name, first, last, year, title, employer, email, address_1, address_2, image, image_mobile_id,
                      image_desktop_id, image_alt, prefix='', middle='', suffix='', data=''):
    page_data = {
        'path': path,
        'name': name,
        'first': first,
        'last': last,
        'email': email,
        'year': year,
        'prefix': prefix,
        'title': title,
        'employer': employer,
        'middle': middle,
        'suffix': suffix,
        'address_1': address_1,
        'address_2': address_2,
        'image': image,
        'image_mobile_id': image_mobile_id,
        'image_desktop_id': image_desktop_id,
        'image_alt': image_alt,
        'office_hours': '',
        'data': data
    }

    return AlumniSpotlight('bfc8e85696c98f63204015eece83778f', '_testing/alumni-spotlights', '80efea1596c98f631dc310ccfb483f98',
                          data=page_data)


def upload_asset(asset, username, password):
    host = f'https://cms.semo.edu:8443/api/v1/create?u={username}&p={password}'
    response = requests.post(host, json=asset)
    message = response.json()
    if message['success']:
        return message['createdAssetId']

    return response.text
