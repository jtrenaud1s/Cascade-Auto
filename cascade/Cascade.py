class Page:

    def __init__(self, name, contentTypeId, contentTypePath, pageConfigurations, metadata, parentFolderId,
                 parentFolderPath, siteId, siteName, structuredData=[], linkRewriting="inherit", shouldBePublished=True,
                 shouldBeIndexed=True, expirationFolderRecycled=False, reviewOnSchedule=False, reviewEvery=180,
                 tags=[]):
        self.contentTypeId = contentTypeId
        self.contentTypePath = contentTypePath
        self.structuredData = structuredData
        self.pageConfigurations = pageConfigurations
        self.metadata = metadata
        self.parentfolderId = parentFolderId
        self.parentFolderPath = parentFolderPath
        self.siteId = siteId
        self.siteName = siteName
        self.tags = tags
        self.name = name
        self.linkRewriting = linkRewriting
        self.shouldBePublished = shouldBePublished
        self.shouldBeIndexed = shouldBeIndexed
        self.expirationFolderRecycled = expirationFolderRecycled
        self.reviewOnSchedule = reviewOnSchedule
        self.reviewEvery = reviewEvery

    def add_data_node(self, node):
        self.structuredData.append(node)

    def to_dict(self):
        return {
            'asset': {
                'page': {
                    'contentTypeId': self.contentTypeId,
                    'contentTypePath': self.contentTypePath,
                    'structuredData': {
                        'structuredDataNodes': [n.to_dict() for n in self.structuredData]
                    },
                    'pageConfigurations': [c.to_dict() for c in self.pageConfigurations],
                    'metadata': self.metadata.to_dict(),
                    'parentFolderId': self.parentfolderId,
                    'parentFolderPath': self.parentFolderPath,
                    'siteId': self.siteId,
                    'siteName': self.siteName,
                    'tags': self.tags,
                    'name': self.name,
                    'linkRewriting': self.linkRewriting,
                    'shouldBePublished': self.shouldBePublished,
                    'shouldBeIndexed': self.shouldBeIndexed,
                    'expirationFolderRecycled': self.expirationFolderRecycled,
                    'reviewOnSchedule': self.reviewOnSchedule,
                    'reviewEvery': self.reviewEvery
                }
            }
        }


class StructuredDataNode:

    def __init__(self, _type, identifier, text=None, child_nodes=[], assetType=None, fileId=None):
        self.type = _type
        self.identifier = identifier
        self.text = text
        self.child_nodes = child_nodes
        self.assetType = assetType
        self.fileId = fileId

    def add_data_node(self, node):
        self.child_nodes.append(node)

    def to_dict(self):
        data = {
            'type': self.type,
            'identifier': self.identifier,
            'recycled': False
        }

        if self.text is not None:
            data['text'] = self.text

        if self.assetType is not None:
            data['assetType'] = self.assetType

        if self.fileId is not None:
            data['fileId'] = self.fileId

        if len(self.child_nodes) > 0:
            children = []
            for child in self.child_nodes:
                children.append(child.to_dict())

            data['structuredDataNodes'] = children

        return data


class MetaData:
    def __init__(self, displayName='', title='', summary='', teaser='', keywords='', metaDescription='', author='',
                 dynamicFields=[]):
        self.displayName = displayName
        self.title = title
        self.summary = summary
        self.teaser = teaser
        self.keywords = keywords
        self.metaDescription = metaDescription
        self.author = author
        self.dynamicFields = dynamicFields

    def add_dynamic_field(self, dynamicField):
        self.dynamicFields.append(dynamicField)

    def to_dict(self):
        data = {
            'displayName': self.displayName,
            'title': self.title,
            'summary': self.summary,
            'teaser': self.teaser,
            'keywords': self.keywords,
            'metaDescription': self.metaDescription,
            'author': self.author,
            'dynamicFields': [f.to_dict() for f in self.dynamicFields]
        }
        return data


class DynamicField:
    def __init__(self, name, values=[]):
        self.name = name
        self.values = values

    def add_value(self, value):
        self.values.append(value)

    def to_dict(self):
        values = []

        for v in self.values:
            values.append({'value': v})
        return {
            'name': self.name,
            'fieldValues': values
        }


class PageConfiguration:
    def __init__(self, name, id, templateId, templatePath, defaultConfiguration=False, formatRecycled=False,
                 pageRegions=[], includeXMLDeclaration=False, publishable=False):
        self.name = name
        self.id = id
        self.templateId = templateId
        self.templatePath = templatePath
        self.defaultConfiguration = defaultConfiguration
        self.formatRecycled = formatRecycled
        self.pageRegions = pageRegions
        self.includeXMLDeclaration = includeXMLDeclaration
        self.publishable = publishable

    def to_dict(self):
        regions = []

        for region in self.pageRegions:
            regions.append(region.to_dict())

        data = {
            'name': self.name,
            'id': self.id,
            'templateId': self.templateId,
            'templatePath': self.templatePath,
            'defaultConfiguration': self.defaultConfiguration,
            'formatRecycled': self.formatRecycled,
            'pageRegions': regions,
            'includeXMLDeclaration': self.includeXMLDeclaration,
            'publishable': self.publishable
        }

        return data


class PageRegion:
    def __init__(self, id, name="DEFAULT", blockRecycled=False, noBlock=False, formatRecycled=False, noFormat=False,
                 formatId=None, formatPath=None):
        self.id = id
        self.name = name
        self.blockRecycled = blockRecycled
        self.noBlock = noBlock
        self.formatRecycled = formatRecycled
        self.noFormat = noFormat
        self.formatId = formatId
        self.formatPath = formatPath

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'blockRecycled': self.blockRecycled,
            'noBlock': self.noBlock,
            'formatRecycled': self.formatRecycled,
            'noFormat': self.noFormat
        }

        if self.formatId is not None:
            data['formatId'] = self.formatId
            data['formatPath'] = self.formatPath

        return data



