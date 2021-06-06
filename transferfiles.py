import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Aw7ghgTCHfA6-oXflve7Cwmw9sabD9ve6vOGz0LGm2F8Jp_VbjPAHYyiQjG4vF6dYAoBNF0tdoIYGznzxlF57MAAEmG2pwH56WFwaqho1X5q11nRc2zyf3xS9AoFCf-Zo6UJenXmYdZC'
    transferData = TransferData(access_token)

    file_from = 'c:/Python/101/cloud_storage.py'
    file_to = '/pythonprograms/cloud_storage.py'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()