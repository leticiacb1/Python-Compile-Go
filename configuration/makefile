VENV_DIR="venv"

run_tests:
	@echo "-------------------------------------"
	@echo "            RUN TESTS                "
	@echo "-------------------------------------"


	@echo ">            TEST COMENTS                "
	pytest test/test_comments.py || { if [ $$? -ne 0 ]; then echo " [INFO] Test Comments failed!"; fi; }

	@echo ">            TEST DELIMITERS                "
	pytest test/test_delimiters.py || { if [ $$? -ne 0 ]; then echo " [INFO] Test Delimiters failed!"; fi; }

	@echo ">            TEST CALCULATOR                "
	pytest test/test_simple_calculator.py || { if [ $$? -ne 0 ]; then echo " [INFO] Test Calculator failed!"; fi; }

	@echo ">           TEST UNARY OP.                "
	pytest test/test_unary_operators.py || { if [ $$? -ne 0 ]; then echo " [INFO] Test Unary Operators failed!"; fi; }


clean:
	@echo ">            CLEANING UP...                "
	@echo "[INFO] Deleting virtual environment..."
	rm -rf $(VENV_DIR)