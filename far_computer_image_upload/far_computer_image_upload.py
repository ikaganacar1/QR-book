from os import listdir,system
from publitio import PublitioAPI

class publitio_api:

    def __init__(self, api_key, api_secret):
        self.publitio_api = PublitioAPI(key=api_key, secret=api_secret)

    def upload_file(self, file_path, file_title, file_description):
        
        self.publitio_api.create_file(file = open(file_path,'rb'), title=file_title, description=file_description)
        #print("uploaded to publit")
  
    def delete_file(self,index):
        self.publitio_api.delete_file(self.get_file_id(index))
   
    def get_file_id(self,index):
        return self.publitio_api.list_files()['files'][index]['id']
      
    def get_url(self,index):
        return self.publitio_api.list_files()['files'][index]['url_preview']
     
    def get_list(self):
        return self.publitio_api.list_files()
        #{'success': True, 'code': 200, 'limit': 100, 'offset': 0, 'files_total': 0, 'files_count': 0, 'files': []}

def create_list_of_files(path):
    a = list()
    for files in listdir(path):
        a.append(str(files))
    
    a.sort()
    return a

def upload_file_to_publit(file_name):
    pt = publitio_api('r2xGdVpnmXkcs14tgpoX','rpJd0TxhrQ7P7zDQDzPQSX3k2RPm93k8')
    pt.upload_file(f"images/{file_name}","temp","temp")

    url = pt.get_url(-1)
    return str(url)


if __name__ == "__main__":
    lst = create_list_of_files("images")
    counter = len(lst)
    
    for i in range(len(lst)):
        upload_file_to_publit(lst[i])
        system('cls')
        yüzde = ((i+1)/counter)*100
        print(f"Toplam {len(lst)} fotoğraf.\n{(i+1)} tane yüklendi.\n%{yüzde}")