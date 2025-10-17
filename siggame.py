import signal
import sys
import os
import time
import threading

class Trick:
	def __init__(self):
		self.secret = "ElKompsBacChemToxni"
		self.attempts = 0
		self.locked_until = 0
		self.signal_attempts = 0
		self.waiting_for_password = False
		self.signals = {
			signal.SIGINT:   "",
			signal.SIGQUIT:  "",
			signal.SIGTSTP:  "",
			signal.SIGTERM:  "",
			signal.SIGHUP:   "",
			signal.SIGUSR1:  "",
			signal.SIGUSR2:  "",
		}

		for sig, msg in self.signals.items():
			try:
				signal.signal(sig, self.handler)
			except (OSError, RuntimeError, ValueError):
				pass

	def handler(self, signum, frame):
		if time.time() < self.locked_until:
			print("⏳ Locked! Please wait...")
			return
		self.signal_attempts += 1
		self.clear_tab()

	def clear_tab(self, show_message=True):
		os.system('clear' if os.name == 'posix' else 'cls')
		if show_message:
			if self.signal_attempts >= 10:
				print("Vay es el gitei qez ruchken a petq")
			else:
				print("Ujex qashi")


	def mission_success(self):
		self.clear_tab(show_message=False)
		print("🎉 Congratulations! You discovered the secret phrase.")
		print("Now do these commands:")
		print("  vim .zshrc")
		print("  delete python3 siggame.py command")
		print("  source .zshrc")
		sys.exit(0)

	def lockout(self):
		self.locked_until = time.time() + 60
		self.clear_tab()
		print("⏳ Too many attempts! Locked for 60 seconds...")
		while time.time() < self.locked_until:
			time.sleep(1)
		self.attempts = 0
		self.clear_tab(show_message=False)
		print("✅ You can try again now.")

	def default_loop(self):
		while True:
			if time.time() >= self.locked_until and not self.waiting_for_password:
				print("la", end="", flush=True)
			time.sleep(0.08)

	def run(self):
		print("Welcome to the program Qashvar!!!\nTry to exit from here")

		default_thread = threading.Thread(target=self.default_loop, daemon=True)
		default_thread.start()

		while True:
			try:
				if time.time() < self.locked_until:
					print("⏳ Locked! Please wait...")
					time.sleep(1)
					continue
				line = input("").strip()
				print("Chkpav ynger jan")
				self.clear_tab()
			except EOFError:
				if time.time() < self.locked_until:
					print("⏳ Locked! Please wait...")
					time.sleep(1)
					continue
				print("\nDavay de paroly asa")
				self.waiting_for_password = True
				try:
					password = input("").strip()
					if password == self.secret:
						self.mission_success()
					else:
						print("Chkpav ynger jan")
						self.clear_tab()
						self.attempts += 1
						if self.attempts % 5 == 0:
							self.lockout()
				except (EOFError, KeyboardInterrupt):
					self.clear_tab(show_message=False)
				finally:
					self.waiting_for_password = False
			except KeyboardInterrupt:
				if time.time() < self.locked_until:
					print("⏳ Locked! Please wait...")
					time.sleep(1)
					continue
				self.clear_tab()

if __name__ == "__main__":
	Trick().run()
