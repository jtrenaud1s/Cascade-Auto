from cascade.Cascade import PageRegion, PageConfiguration, MetaData, DynamicField, StructuredDataNode, Page


class AlumniSpotlight:
    def __init__(self, parentFolderId, parentFolderPath, siteId='80efea1596c98f631dc310ccfb483f98', siteName='semo playground', data={}):
        regions1 = [
            PageRegion('f4f4286c96c98f631dc310ccaf95215e')
        ]
        regions2 = [
            PageRegion('1a821dce96c98f631dc310cc0f88c595', formatId='1a83eee796c98f631dc310ccfd093139',
                       formatPath='semo.edu:_cms/formats/pages/peopleDetail'),

            PageRegion('f4f4284f96c98f631dc310cc25ba645b', formatId='f4f428ee96c98f631dc310ccd02e84aa',
                       formatPath='semo.edu:_cms/formats/global/header', name='HEADER'),

            PageRegion('f4f4284f96c98f631dc310cca81c72d3', formatId='f4f4290296c98f631dc310cc309bbe63',
                       formatPath='semo.edu:_cms/formats/global/scripts', name='SCRIPTS'),

            PageRegion('f509588696c98f631dc310cc476b767b', formatId='f51661b896c98f631dc310cc8befed39',
                       formatPath='semo.edu:_cms/formats/global/body/end', name="END"),

            PageRegion('f4f4284f96c98f631dc310cc379da5f6', formatId='f4f4291896c98f631dc310cca34d29e8',
                       formatPath='semo.edu:_cms/formats/global/footer', name='FOOTER'),

            PageRegion('f4f4284f96c98f631dc310cc10393632', formatId='f4f428de96c98f631dc310cc116d155e',
                       formatPath='semo.edu:_cms/formats/global/head', name='HEAD'),

            PageRegion('f509588796c98f631dc310ccf39d72db', formatId='f58040b396c98f631dc310ccb743f652',
                       formatPath='semo.edu:_cms/formats/global/menu', name='MENU'),

            PageRegion('f509588696c98f631dc310cc7105c62a', formatId='f517693e96c98f631dc310cca1e51d09',
                       formatPath='semo.edu:_cms/formats/global/pagewrapper/start', name='PAGEWRAPPER-START'),

            PageRegion('f509588696c98f631dc310cccdce4a0e', formatId='f516618096c98f631dc310cc0abb6a15',
                       formatPath='semo.edu:_cms/formats/global/body/start', name='BODY-START'),

            PageRegion('f509588696c98f631dc310cc1c24801c', formatId='f517695096c98f631dc310cc06792cd9',
                       formatPath='semo.edu:_cms/formats/global/pagewrapper/end', name='PAGEWRAPPER-END')
        ]

        configs = [
            PageConfiguration('XML', '1a821dce96c98f631dc310cc349b139d', 'f4f4286c96c98f631dc310ccc9103d5d',
                              'semo.edu:_cms/templates/XML-JSON', pageRegions=regions1),

            PageConfiguration('HTML', '1a821dce96c98f631dc310cc10b1e6a6', 'f4f4284f96c98f631dc310cc89afa841',
                              'semo.edu:_cms/templates/Default', pageRegions=regions2)
        ]

        metadata = MetaData(title=data['first'].capitalize() + ' ' + data['last'].capitalize(),dynamicFields=[DynamicField('show-on-search-results', ['No']),
                                           DynamicField('show-on-detail', ['No'])])

        data_nodes = [
            StructuredDataNode('group', 'name', child_nodes=[
                StructuredDataNode('text', 'prefix', ''),
                StructuredDataNode('text', 'first', data['first']),
                StructuredDataNode('text', 'middle', ''),
                StructuredDataNode('text', 'last', data['last']),
                StructuredDataNode('text', 'suffix', ''),
            ]),
            StructuredDataNode('group', 'position', child_nodes=[
                StructuredDataNode('text', 'title', data['title']),
                StructuredDataNode('text', 'role', '::CONTENT-XML-SELECTOR::Other'),
                StructuredDataNode('text', 'departments', data['employer'])
            ]),
            StructuredDataNode('group', 'image', child_nodes=[
                StructuredDataNode('text', 'showImage', 'Yes' if data['image'] is not None else 'No'),
                StructuredDataNode('asset', 'mobile', assetType='file', fileId=data['image_mobile_id']),
                StructuredDataNode('asset', 'desktop', assetType='file', fileId=data['image_desktop_id']),
                StructuredDataNode('text', 'alt', data['image_alt'])
            ]),
            StructuredDataNode('group', 'phone-numbers', child_nodes=[
                StructuredDataNode('group', 'phone-number', child_nodes=[
                    StructuredDataNode('text', 'label'),
                    StructuredDataNode('text', 'number')
                ]),
            ]),
            StructuredDataNode('group', 'email-addresses', child_nodes=[
                StructuredDataNode('group', 'email', child_nodes=[
                    StructuredDataNode('text', 'label'),
                    StructuredDataNode('text', 'address')
                ]),
            ]),
            StructuredDataNode('group', 'locations', child_nodes=[
                StructuredDataNode('group', 'location', child_nodes=[
                    StructuredDataNode('text', 'label', ),
                    StructuredDataNode('text', 'address-line-one'),
                    StructuredDataNode('text', 'address-line-two')
                ]),
            ]),
            StructuredDataNode('group', 'hours', child_nodes=[
                StructuredDataNode('text', 'content', ''),
            ]),
            StructuredDataNode('group', 'social', child_nodes=[
                StructuredDataNode('group', 'link', child_nodes=[
                    StructuredDataNode('text', 'type'),
                    StructuredDataNode('text', 'url')
                ]),
            ]),
            StructuredDataNode('group', 'pageIntro', child_nodes=[
                StructuredDataNode('text', 'description'),
                StructuredDataNode('text', 'content')
            ]),
            StructuredDataNode('group', 'row', child_nodes=[
                StructuredDataNode('text', 'type', 'WYSIWYG'),
                StructuredDataNode('asset', 'block', assetType='block'),
                StructuredDataNode('text', 'content', data['data'])
            ]),
        ]

        self.page = Page(data['first'].lower() + '-' + data['last'].lower(), '1a82a45596c98f631dc310ccc43434de', 'semo.edu:People Detail', configs, metadata, parentFolderId, parentFolderPath, siteId, siteName, structuredData=data_nodes)
