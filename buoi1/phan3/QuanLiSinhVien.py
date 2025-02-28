from SinhVien import SinhVien

class QuanLiSinhVien:
    listSinhVien = []
    
    def generateID(self):
        maxId = 1
        if(self.SoLuongSinhVien()> 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập giới tính sinh viên: ")
        diemTB = float(input("Nhập điểm trung bình sinh viên: "))
        sv = SinhVien(svId,name,sex,major,diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, ID): 
        sv:SinhVien = self.findByID(ID)
        if( sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập giới tính sinh viên: ")
            diemTB = float(input("Nhập điểm trung bình sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID = {} không tồn tại." .format(ID))
            
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id,reverse=False)
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name,reverse=False)
    def sortByDiemTb(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB,reverse=False)
    
    def findById(self, ID):
        searchResult = None
        if(self.soLuongSinhVien()>0):
            for sv in self.listSinhVien:
                if(sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []