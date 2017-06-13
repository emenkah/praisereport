
test:
	mkdir -p plots
	cd code && python praise_report.py
clean:
	rm -rf plots
