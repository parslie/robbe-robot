BIN_NAME=robbe
INSTALL_DIR=$(HOME)/Scripts/prog/$(BIN_NAME)
LINK_DIR=$(HOME)/Scripts/bin

install-rpi:
	mkdir -p $(INSTALL_DIR)
	mkdir -p $(LINK_DIR)
	cp -r venv/ $(INSTALL_DIR)/venv/
	cp src/** $(INSTALL_DIR)/
	cp start.sh $(INSTALL_DIR)/$(BIN_NAME)
	chmod +x $(INSTALL_DIR)/$(BIN_NAME)

	rm -f $(LINK_DIR)/$(BIN_NAME)
	ln -s $(INSTALL_DIR)/$(BIN_NAME) $(LINK_DIR)/$(BIN_NAME)
