class Udacian:
    def __init__(self,Udacian_name,Udacian_city,Udacian_enrollment,Udacian_nanodegree,Udacian_status):
        self.name=Udacian_name
        self.city=Udacian_city
        self.enrollment=Udacian_enrollment
        self.nanodegree=Udacian_nanodegree
        self.status=Udacian_status
    
        print "name:"+self.name+"  city:"+self.city+"  enrollment:"+self.enrollment+"  nanodegree:" +self.nanodegree+ "  status:"+self.status
    def Add(self):
        print "name:" + self.name + "  city:" + self.city + "  enrollment:" + self.enrollment + "  nanodegree:" + self.nanodegree + "  status:" + self.status





user = Udacian("mufadal","Makkah","computer","full stack web developer","student")

user.Print()
