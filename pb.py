from publitio import PublitioAPI

class publitio_api:

    def __init__(self, api_key, api_secret):
        self.publitio_api = PublitioAPI(key=api_key, secret=api_secret)

    def upload_file(self, file_path, file_title, file_description):
        
        self.publitio_api.create_file(file = open(file_path,'rb'), title=file_title, description=file_description)
        print("uploaded to publit")
  
    def delete_file(self,index):
        self.publitio_api.delete_file(self.get_file_id(index))
   
    def get_file_id(self,index):
        return self.publitio_api.list_files()['files'][index]['id']
      
    def get_url(self,index):
        return self.publitio_api.list_files()['files'][index]['url_preview']
     
    def get_list(self,offset,limit):
        return self.publitio_api.list_files(limit=limit,offset=offset)
        #{'success': True, 'code': 200, 'limit': 100, 'offset': 0, 'files_total': 0, 'files_count': 0, 'files': []}





