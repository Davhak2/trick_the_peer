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
		self.passwrd = False
		self.flag = False
		self.signals = {
			signal.SIGINT,
			signal.SIGQUIT,
			signal.SIGTSTP,
			signal.SIGTERM,
			signal.SIGHUP,
			signal.SIGUSR1,
			signal.SIGUSR2,
		}

		for sig in self.signals:
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
		effective_show = show_message and not self.hide_prompt
		if self.hide_prompt:
			self.hide_prompt = False
		if effective_show:
			if self.signal_attempts % 666 == 0:
				print("Ara de zzvcir eli paroly \"ElKompsBacChemToxni\" a")
			elif self.signal_attempts % 50 == 0:
				print("Ara de asum em anasun erkir a")
			elif self.signal_attempts % 15 == 0:
				print("Ba urish vonc es ape?")
			elif self.signal_attempts % 11 == 0:
				print("Axjkeq jan vor hasneq 500 drami indzi dzen ktaq")
			elif self.signal_attempts % 5 == 0:
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
		self.locked_until = time.time() + 30
		self.clear_tab()
		print("⏳ Too many attempts! Locked for 30 seconds...")
		while time.time() < self.locked_until:
			time.sleep(1)
		self.attempts = 0
		self.clear_tab(show_message=False)
		print("✅ You can try again now.")

	def default_loop(self):
		while True:
			if time.time() >= self.locked_until and not self.passwrd:
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
				self.clear_tab()
				print("Chkpav ynger jan")
			except EOFError:
				if time.time() < self.locked_until:
					print("⏳ Locked! Please wait...")
					time.sleep(1)
					continue
				print("\nDavay de paroly asa")
				self.passwrd = True
				try:
					password = input("").strip()
					if password == self.secret:
						self.mission_success()
					else:
						self.hide_prompt = True
						self.clear_tab()
						print("Chkpav ynger jan")
						self.attempts += 1
						if self.attempts % 5 == 0:
							self.lockout()
				except (EOFError, KeyboardInterrupt):
					self.clear_tab(show_message=False)
				finally:
					self.passwrd = False
			except KeyboardInterrupt:
				if time.time() < self.locked_until:
					print("⏳ Locked! Please wait...")
					time.sleep(1)
					continue
				self.clear_tab()

if __name__ == "__main__":
	Trick().run()
