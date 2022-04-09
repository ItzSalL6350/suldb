class SulDB:
	def __init__(DB, DBName) -> None: 
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