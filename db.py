import sqlite3
def main():
    db=sqlite3.connect("zanyary.db")# Lere wtman peywendy bke be sql w database drwst bke be nawy zanyary,db
    db.row_factory=sqlite3.Row # ememan drwst krd bo ewey regebdat hemw row bxwenynewe le table y ADmin. be
    #shewy dictionary
    db.execute("create table if not exists Admin(Name text,Age int)") #lera wtman table drwst bke be nawy Admin
    #ke dw nrxy tyabet brytyn le NAme w Age
    db.execute("insert into Admin(Name,Age) values (?,?)",("Galla", 23)) #Lere zanyaryman nard bo zanyary.db le naw table
    #y Admin ke naw w age zyad bkat bo tableke."
    db.execute("insert into Admin(Name,Age) values (?,?)",("Karo", 20))
    db.commit() #Em krdare be commit esheke tewaw dekat yan naykat wate be nyweyy nayhelletewe. eger em
    #commit e da neny ewa hemw run ekan her heman data dedatewe, bellam xoy debet bo her run ek databse y nwe drwst
    #bkatewe eger heman shtysh bet.

    #db.execute("delete from Admin where name='Galla'") #beme detwany databse bsrrytewe.
    #db.execute("update Admin Set Age=21 where name='Karo'") #Lerewe detwany update y databse bkey.
    kurde=db.execute("select * from Admin") #lere demanewy hemww row e kany naw table ke bxwenetewe.
    #enja Chwyn row_factoryman drwstkrd
    for row in kurde:
        print("Name:{},Age:{}".format(row["Name"],row["Age"]))

if __name__ == '__main__':main()