Here’s the working Python script and systemd service unit — tested and confirmed to:
	Handle short press = reboot
	Handle long press = shutdown
	Run via systemd on boot
	Log all activity to a local log file

***MAKE SURE YOU UPDATE YOUR USER NAME FOR THE <user> LOCATIONS***

Use /home/<user>/power_button.log for logs

/home/<user>/power_button.py
/etc/systemd/system/power_button.service

Setup Summary (for future reference)
	Make script executable:
	chmod +x /home/<user>/power_button.py

Enable and start the service:
	sudo systemctl daemon-reexec
	sudo systemctl daemon-reload
	sudo systemctl enable power_button.service
	sudo systemctl start power_button.service
Monitor the log:
	tail -f /home/<user>/power_button.log
	
Pinout
Shutdown/reboot/power-on (Use GPIO3 (Pin 5) for shutdown and hardware power-on)
Pin 5 and 6
LED
Pin 1 and 9
