class SulDB:
	def __init__(DB, DBName: str) -> None: 
		DB.DBName = DBName

	def Create(DB) -> None:
		with open(DB.DBName + ".suldb", "w") as DBFile:
			DBFile.write("")

	def Write(DB, Data: str) -> None:
		with open(DB.DBName + ".suldb", "a") as DBFile:
			DBFile.write(Data + "\n")

	def Read(DB) -> str:
		with open(DB.DBName + ".suldb", "r") as DBFile:
			Data = []
			for Line in DBFile.readlines():
				Line = Line.replace("\n", "")
				Data.append(Line)

		return Data

	def DataAmount(DB, Data: str) -> int:
		DataList = DB.Read()
		
		return DataList.count(Data)

	def Replace(DB, Data: str) -> None:
	    for Item in Data:
	        DB.Write(Item)
	        
	def ReplaceItem(DB, OldItem: str, NewItem: str) -> None:
	    DataList = DB.Read()
	    DB.Create()
	    
	    for Item in DataList:
	        if Item == OldItem:
	            DB.Write(NewItem)
	        else:
	            DB.Write(Item)