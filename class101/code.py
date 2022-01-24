from os import access
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token =  access_token
    
    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BAqT23rRm_mEQVOJBonEu6RZHIHyAsoBMYno5JN_053lcCoRv4WOJwAxcBJDZ7lcFSHq5CUFpTyihxVXshGND49VKOkSFBnTxIV2D2JUpif5YU5BBDvs70VhUBrvLvYLTpyXUpM'
    transferData = TransferData(access_token)

    file_from = input('Enter your source pack')
    file_to = input('Enter destination path')
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
    