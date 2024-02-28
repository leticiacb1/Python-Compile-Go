VENV_DIR="venv"

.PHONY: test
test:
	@echo "-------------------------------------"
	@echo "            RUN TESTS                "
	@echo "-------------------------------------"
	
	@echo ">            TEST COMENTS                "
	cd .. && cd compiler && python3 -m pytest -s ../test/test_comments.py || { if [ $$? -ne 0 ]; then echo " [INFO] Test Comments failed!"; fi; }

.PHONY: clean
clean:
	@echo ">            CLEANING UP...                "
	@echo "[INFO] Deleting virtual environment..."
	rm -rf $(VENV_DIR)

all: test