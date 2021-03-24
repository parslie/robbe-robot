TARGET_NAME=robbe
BIN_FOLDER=$(HOME)/Scripts/bin
TARGET_FOLDER=$(HOME)/Scripts/$(TARGET_NAME)

all:
	echo "Run make linux OR make windows instead..."

linux:
	mkdir -p $(TARGET_FOLDER)
	mkdir -p $(BIN_FOLDER)
	cp -r venv/ $(TARGET_FOLDER)/venv/ 
	cp src/** $(TARGET_FOLDER)/
	cp start.sh $(TARGET_FOLDER)/$(TARGET_NAME)
	chmod +x $(TARGET_FOLDER)/$(TARGET_NAME)

	rm -f $(BIN_FOLDER)/$(TARGET_NAME)
	ln -s $(TARGET_FOLDER)/$(TARGET_NAME) $(BIN_FOLDER)/$(TARGET_NAME)

rpi:	
	killall -q python3
	make linux
	robbe &
